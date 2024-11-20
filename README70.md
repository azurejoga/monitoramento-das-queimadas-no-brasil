# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a55b1132-a544-3db5-9ef7-f1df61787661 | -4.44878 | -46.59339 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c3e3edab-2377-36aa-a131-bc0c813aaef5 | -1.51977 | -55.48908 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f39b84e-e433-3c2c-8d00-0ca986b60562 | -4.44871 | -46.57983 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8e30c6ae-a4ec-3c98-bb07-0fe4c1e2f7da | -2.58415 | -51.92328 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b4f26bd-9eca-36fa-882c-bc90fb453fae | -3.19812 | -54.31905 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5af4a49f-0f4e-354a-9830-ae7411df40d9 | -1.17124 | -53.67622 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82ed5bae-775a-3fd4-a276-9f2a0efb81fe | -1.4467 | -47.11988 | 2024-11-20 05:14:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8ad5488-9542-3e38-941e-cc34242f34ae | -2.78657 | -51.72038 | 2024-11-20 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74f4482b-4ce0-3c59-9876-bc03ed270dc8 | -3.2949 | -53.85658 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 428cb034-50f7-31aa-9be1-981ffe89b2d3 | -1.20343 | -51.77877 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce09816e-1054-3e77-922e-0666758553a2 | -1.49085 | -51.13793 | 2024-11-20 05:14:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9243bd67-4c85-3c97-abb3-39ef5f841d49 | -2.4543 | -49.1528 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b0b79d2-e208-31d3-a766-45331f760885 | -3.04552 | -54.40067 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a31152f-f75d-3d66-a4b9-8353eb1ac04b | -2.76636 | -53.21748 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90bba88e-83f7-3266-a923-8c4ad15171e3 | -2.89259 | -48.27603 | 2024-11-20 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5e67bfd4-81a5-324e-af99-50e5fc07846c | -1.34515 | -55.44382 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d9de0a0-7c96-38b1-acda-8e99b1d2dec8 | -1.51493 | -52.09321 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ca72297-cac6-3e74-9f94-08e625129423 | -0.11144 | -51.43581 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abcc84db-6efb-3e46-826c-84059a979d7d | -1.21961 | -51.74497 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4df584c0-88d8-3541-ac71-b56d087ae803 | -4.55281 | -48.00685 | 2024-11-20 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c9132b3-a3f4-3348-9bdc-2593588382e6 | -4.24925 | -53.67124 | 2024-11-20 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b80a8119-894f-39da-8acd-e882c918f8cf | -1.15235 | -53.51947 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8252d46-e7e2-30cb-95aa-69e926d3b9b2 | -1.89835 | -53.33321 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf97a992-30ee-3faa-a7af-55dbce505402 | -2.26531 | -45.46498 | 2024-11-20 05:14:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c80720ab-affd-393c-9ad0-3fe460bdf534 | -1.78754 | -53.5901 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3a72f34-a51e-33ea-aed4-603f39453af7 | -3.03577 | -49.46083 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0bee3815-0cec-358a-87ba-268f1a45c5f9 | -3.0405 | -49.46468 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17c910de-dea4-350b-804e-2ddf926f5211 | -2.76262 | -54.07756 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 785fb8b7-4b05-31b5-abe4-956097994e37 | -6.24744 | -47.26804 | 2024-11-20 05:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cd62450-e7f3-3b4c-8eb7-1e1d36a8d552 | 0.36985 | -53.82021 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d94ddc98-e817-3d76-b70d-d0ae5b57338f | -2.74773 | -51.8283 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 716f7307-a86f-3f63-b63c-3265d973004a | -1.64746 | -52.66861 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae8716ee-0f16-3eb1-a638-a6bac7e93bdf | -1.64635 | -52.67581 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffcbb809-d4cb-31b5-a7aa-f02d79def3b0 | -4.0591 | -54.05146 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc1ea435-a473-334d-a4ca-9884012e9cf6 | -1.14341 | -51.69563 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d3d7f9c-28a0-3d4d-8945-fa06a7f601a1 | -3.05972 | -54.40752 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfde25c6-e038-3c08-aca4-167f11d2814a | -1.32289 | -52.40363 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a3a7ff4d-bb44-30ba-832d-51e4270913f2 | -4.05208 | -54.37717 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8374b356-72e3-3fd0-9c96-c29c85fcdb62 | -1.64877 | -52.68724 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65841638-ddce-3591-9386-d35e74101ef8 | -2.00264 | -46.60682 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e87a306d-a7bf-3ea1-8ef6-477ee3742b91 | -0.81818 | -52.48513 | 2024-11-20 05:14:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59cb6143-35a5-3b70-ac0d-275a6363f7f7 | -1.24648 | -52.03785 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96ef088c-77bd-32f8-b3fc-cfb68490c59b | -2.48963 | -49.02866 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a49dc392-d787-3275-8e1c-6f092507711b | -1.47732 | -51.13588 | 2024-11-20 05:14:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 295e5d2a-cffe-3f09-ade3-eeaa31a8fc4e | -1.32594 | -52.39985 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| af87d547-45fc-3afc-a595-d96da8131ba2 | -2.72107 | -49.33998 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2bb91d5-7e72-340b-b08a-aa01c7eb17de | -1.86774 | -56.40359 | 2024-11-20 05:14:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49af7aba-a42b-3d42-813f-6bd97d7bf7d6 | -3.08296 | -54.66539 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7074856d-c9fb-3e3a-9cd9-3f67f947053b | -0.24693 | -48.5938 | 2024-11-20 05:14:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ce2beea-b4ca-37b2-82ed-c7be2c064178 | -2.75647 | -54.06719 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8908910d-2bc6-3b9e-97ec-1e8bc27fc3ef | -1.20153 | -51.77556 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d14bf4c1-315e-3bc4-a1e1-fbe2411c1994 | -1.1119 | -52.39456 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e02a285-f4ed-36df-8add-b7fbfc94cf54 | -1.20841 | -51.75991 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85ca4d4b-4477-33b0-aebd-85eb9b1c661c | -2.63219 | -54.26855 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0f602df-9db7-3c1e-8f3f-e946172741ed | -1.1947 | -53.6753 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1b79f7b5-3601-3bbf-84ed-ee22344c9bf0 | -1.96264 | -49.55264 | 2024-11-20 05:14:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fba5172-1b1e-31c6-95e5-d4521cc7e7a5 | -1.20712 | -51.7543 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9dd162a4-b95a-3679-903c-18aef1880e31 | -2.96992 | -49.2914 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43c4384f-afee-38bb-8a8b-07dd2d1ed091 | -4.93736 | -50.64963 | 2024-11-20 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec045997-e021-3821-a111-4acbb76309fb | -3.35905 | -53.40286 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7d88c3f-182b-332f-8b97-5c7f701abdf4 | -4.9357 | -50.64743 | 2024-11-20 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 813f53d1-8876-3dd5-85cd-b91051e2eb53 | -3.7412 | -52.40422 | 2024-11-20 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8413a89-8649-38db-89e8-f1be487a4981 | -4.44081 | -46.58928 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9bd64ced-ea5f-3f94-acf5-e11f7ecc1fd6 | -1.70903 | -52.48716 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 37a4f798-fd7c-388b-a341-8334a46d3702 | -1.64118 | -52.6824 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04f0f0cb-4844-369f-ad1c-168a20e05e41 | -1.05015 | -51.74163 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fd7e10b-ad87-31d1-8759-02c1fc80ea6e | -4.05226 | -54.37485 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf74762-fc2a-3b1e-9ca4-4e3c823dd09f | -2.82865 | -51.82773 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d54e4da-8432-34ae-b512-bb9bfef96c9a | -2.91745 | -53.07261 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c869e948-906f-3ccd-8edc-97bfef886c2c | -1.13234 | -51.68132 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b20af1aa-3ee3-3d40-bd5a-0e66fe928e62 | -2.22249 | -46.48214 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc5f913f-d9c7-3767-b48f-d03d3b0ad344 | -0.89662 | -51.72337 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15879e68-bf82-3510-b629-2d36f0a02ce4 | -1.59801 | -47.14515 | 2024-11-20 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d716945b-6d67-32d7-8de3-7e30f818445d | -3.37624 | -44.43504 | 2024-11-20 05:14:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14cd9dca-4eee-3fe4-9a43-7e79828256ff | -2.13684 | -48.57075 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 2f59aac5-0a42-3699-b42f-2d821f2a4f30 | -4.38016 | -47.77635 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 339e55e5-39b6-3877-8952-749de07a3b16 | -1.62341 | -52.25834 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72dcb03a-3a88-3e25-a020-1f47195d232f | -2.7733 | -48.58063 | 2024-11-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bb3a7d3-7594-3978-928b-adc58e9a6eb2 | -3.24103 | -54.16195 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63f0c8de-c235-3ed8-8916-ea6578b59601 | -1.45328 | -47.1165 | 2024-11-20 05:14:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b8fb374-2a3c-3e24-ae00-d337564c1ae2 | -3.08965 | -54.67085 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7258f264-bad3-3672-ab4c-5081d135a87d | -2.06216 | -53.44275 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7c3ea99-add7-3e60-ba67-215d08f3d697 | -1.7224 | -52.6945 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d05fc72-0a83-3ab0-81da-43bad1ded8d2 | -2.1379 | -48.57259 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ac69b119-4c13-393a-a6d3-9a32e961b32b | -2.44953 | -49.14884 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d369722e-9b8c-391e-a827-c710f1bd7392 | -1.3058 | -52.40482 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb1269ad-7dea-3ac2-829b-6dcd54b8f30c | -1.21019 | -51.76311 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad0f1de4-86c7-35a3-b60a-78f920a5d26e | -1.32482 | -52.40725 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dcaf3bae-de53-3bb6-8c0e-485446f9e0b2 | -4.11134 | -51.0546 | 2024-11-20 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bab8689a-324f-3f01-8596-a94f0162d323 | -2.93361 | -48.33598 | 2024-11-20 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04ad9dbb-37fc-393e-bd27-fdccd23b768d | -3.42982 | -53.28667 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 032a221b-a073-3a97-a34e-af1f7b4ca63f | -3.38671 | -53.27291 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5c9b347-0f71-3b00-9d13-caf4717644c2 | -0.91433 | -51.77973 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73eeda0f-279d-3963-a10e-cffb827ab38b | -1.83424 | -55.04652 | 2024-11-20 05:14:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8ffddd6-857f-38f8-a205-40199c8f8ad1 | -1.44767 | -52.66856 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a9bd8d3-43a2-3f08-acc3-be9879ae364e | -1.72648 | -52.69513 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 468998ae-9020-36e4-8ceb-b91c71527f81 | -2.41702 | -45.81922 | 2024-11-20 05:14:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1990f86-6b7a-3d64-9d97-65d8e412dc17 | -1.64052 | -52.60452 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5124969a-bb03-33b0-a136-452a789f492e | -1.21758 | -51.7434 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 953136da-42ef-34a4-86e2-d4e4a1f9c3f8 | -2.99895 | -52.37072 | 2024-11-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README71.md)
