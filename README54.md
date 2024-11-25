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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3352adb-607c-3f06-b2ba-fe0214900975 | -2.14056 | -52.08994 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7338edbd-b7e3-3924-bd9d-9fbd48445e3a | -1.45965 | -51.11785 | 2024-11-25 05:20:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 107c3538-4cd6-3de0-a789-c755cfc90275 | -3.28817 | -53.84163 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504e3a08-0a87-3750-a7a4-77916b1576b3 | -1.78265 | -52.74017 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa777eba-cd8f-3ab1-b82a-c2bf5877dbc4 | -2.22 | -53.61623 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4b99995-0d4b-38b5-b045-8f1924baf238 | -3.51666 | -53.78982 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fee68a71-d804-36f2-9fa0-1cdf9193c9b2 | -3.37029 | -53.06329 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51eed629-e6bb-38c6-a5c9-68ab1a2b9f48 | -0.27397 | -51.61397 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2754343d-7edb-3906-878b-55bd0f607a26 | -2.58142 | -53.96665 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d92bde29-65bb-3c4c-9cad-866a89b831fc | -3.53359 | -54.49403 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d14ddd-6967-398a-a54a-14bee2cfbbce | -3.24467 | -54.72076 | 2024-11-25 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3769c8be-a673-349a-8934-078b9d8f07ff | -3.49575 | -50.46541 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04e9b7be-86f1-3939-96b4-09dd09174460 | -3.51603 | -53.82268 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcea8604-83ec-30f6-9e9a-29c3a71ddc98 | -3.31434 | -54.09515 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe38cb65-03eb-3453-898e-b3245b48b051 | 1.97504 | -60.90599 | 2024-11-25 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a244137c-23e1-3f56-8c27-d328cec932fa | -1.41069 | -53.39914 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 476dfc7d-a1d9-35f6-8e03-9142a37b9785 | -2.90226 | -51.56975 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d819031-e40e-3387-bf7c-aaf38ee7143a | -3.2844 | -53.01078 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84ce0dce-101b-369f-a742-2ee1fe2c2904 | -1.27463 | -52.17222 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a74b674a-3baf-3f28-87ee-242545392434 | -2.63016 | -51.77264 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4031e9e5-3f75-3677-99fe-43b3216cd339 | -3.4332 | -53.87634 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf4c943b-3a92-394d-ba4e-803f904d5637 | -2.7859 | -54.04375 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5381582d-e093-3f60-9970-414c97849ece | -2.82666 | -54.03013 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14fcb4f8-6a67-3f29-b604-d5a45ec1f9b6 | -1.79367 | -52.05272 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3ca3cea-5058-3cbb-ada3-eed018aa45a8 | -0.91064 | -51.64904 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba0fae4c-91f5-315f-ae60-3dfc66817563 | -1.25698 | -51.75151 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a19a609-f83a-3fe2-ba1e-55711e6c8656 | -2.35676 | -53.71434 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c72b7b94-0be5-3851-8544-97ab175e87b4 | -1.46055 | -51.11694 | 2024-11-25 05:20:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99d3ac30-f93b-3eda-97de-deb7623c82c3 | -1.19034 | -51.77098 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9965bc76-80e7-323c-b4e6-9097ba01e679 | -3.65885 | -54.42508 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f070b9b-168a-3351-ba25-9289752141f6 | -4.1377 | -54.3399 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2195da-1e7a-3d81-b018-00501a3aac9e | -1.71817 | -52.72751 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18a2adf7-2ea3-3099-a404-0b066c70dd04 | -1.30342 | -51.73728 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52794b14-bab0-3252-9830-7950bca58f48 | -3.16617 | -53.64415 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c6542f4-5389-3af8-a55e-a00c6617bfa1 | -2.32905 | -53.86338 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 72a2216e-5c15-30e5-8450-9d8f7556c66e | -3.37578 | -54.67884 | 2024-11-25 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02e235a9-c82c-3388-ae0f-2d4670a346d9 | -2.92824 | -51.76976 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 615d85de-485d-32fd-a66b-6714461cfff5 | -2.90268 | -51.56689 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79d40578-6c51-3df7-986a-41cd503c5f60 | -2.32824 | -53.86932 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 04fc0bc0-5fb9-3bd0-8495-f633efc848d7 | -2.94819 | -51.43215 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc336733-3579-3f84-b5b0-b2fc8c6775e6 | -1.36753 | -53.83678 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eec1f1a2-ce00-3fc9-842b-8eceadeb432d | -4.41816 | -49.71029 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dd7482b-6d8b-3dd7-86a3-4e01be9efa32 | -1.25278 | -51.74852 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64155183-405f-3179-a758-646363c6ded2 | -3.2486 | -53.27726 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32109e2d-fb5f-3c6a-950d-5c296d3d6aa8 | -1.76812 | -53.62929 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53430c1c-9ccc-33e0-a141-ea7f66de01c3 | -2.79128 | -53.00836 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26828763-1ed5-3770-9cc7-a06d48740c00 | 1.41494 | -55.89194 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 646e1b53-8d6b-35bc-ab9f-1d6b475a4593 | -2.8005 | -54.11645 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1028d949-7940-342e-a51a-4690428dbcf0 | -3.62432 | -55.30499 | 2024-11-25 05:20:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 309a6883-4e45-3944-b530-589dc614757d | -3.81675 | -52.00017 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b70a4d6e-c135-3c13-92b9-e18c7b93e24f | -1.76031 | -52.70415 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed4f2ee2-01b1-3163-8a95-562482e48a7f | -2.80108 | -54.11264 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47f6964b-43e1-30a2-aee2-e7224652a449 | -3.22131 | -53.93674 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68c88f4b-0e08-3b52-bfd2-fa8bbbb3d7ab | -1.36506 | -53.83626 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04bce807-25a8-3800-95a2-923045a5dedf | -2.90265 | -51.56576 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 305841a3-e096-37e5-8c35-3a83bd33e4a2 | -3.10075 | -53.74066 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58c23318-bd62-3776-ab08-5c36d775d51a | -3.106 | -53.98611 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2b7c165-280a-3d1e-98bc-f48d6e9be821 | -3.67741 | -54.5834 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11562cf0-5713-3fd7-85bd-3fe21ac664a8 | -1.13061 | -54.17559 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfb0f008-bbd7-3f9f-bdea-db5872d3299a | -1.15347 | -53.4085 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce7261ad-2391-320b-823d-699e307a3c30 | 0.95153 | -50.73814 | 2024-11-25 05:20:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5026ad2c-8208-3485-a464-d92b034a98ce | -3.55297 | -51.52628 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 679cdd66-3b81-3e18-b984-62a4a67e47a8 | -0.95133 | -51.63546 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15896fff-ee2e-357f-94b0-41b5139c70cd | -1.77046 | -52.72902 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 51a421e5-3eae-3bd2-a21c-c1f60a79857f | -1.66172 | -53.81414 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5649c6e4-9b45-3ca8-997f-8d28ee4c1cae | -4.22678 | -53.49287 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e76e8ca4-ac29-33fb-bd81-1a120c6a1fd7 | -0.89445 | -51.7211 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 973131e8-b968-3856-ad1d-dbdd207d63a2 | 1.7076 | -55.82022 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07aec863-9d2e-3991-86b9-d12469d75c32 | -3.00228 | -51.55019 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ea9dfc0-1bb2-33b6-9eba-510e636df63f | -3.38422 | -50.73333 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e46ee53-00a5-38bc-8609-4f8ba6403881 | -2.21548 | -46.39174 | 2024-11-25 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 278750d9-2b29-37c2-88c1-f8cf159090e9 | -4.2545 | -48.71876 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e3789be4-d884-3748-8898-96e199a9cf79 | -1.60435 | -52.5859 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c310d2e-1b1e-32c8-95e2-544f5f2c039c | -3.24794 | -53.2816 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44c98dea-b922-3c8f-a658-03ea3071c9ab | -3.25884 | -53.26985 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48250beb-1dc9-35b1-9245-d07c9669e9d8 | -1.75741 | -52.66151 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4c2c5e9-b38e-3526-8073-768b3037b8b5 | -2.31606 | -53.60957 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce179b93-9537-3851-8f15-83ef2d5e9c44 | -3.28998 | -53.85838 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc69e2a2-0427-32e5-82ce-d535f0016b3a | -3.10154 | -51.50473 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 615f02ae-84d3-3db1-898b-a3931faa660c | -3.25119 | -54.23093 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d74e14b-d51c-3eab-a595-b9557b95ccf9 | -1.74196 | -52.73397 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23401285-f589-3a35-a3ed-d5e9f400a520 | -0.35362 | -51.97258 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9b49b4c-88bd-32d8-8368-93993da1597d | -1.75218 | -52.66542 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 740cadfc-918f-305f-b7b4-ec2c948cdf38 | -4.20025 | -50.23684 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 367db5cb-f2b2-3d0b-a899-ee3e2fd0b962 | -1.52107 | -52.07871 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 986a8d35-9983-328c-8cc3-2016da6ceb1d | -2.89783 | -51.77124 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1750077-1a45-3477-8004-63af071778d9 | -2.33645 | -52.18634 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38a9aa98-118c-3eb4-bc7b-1dcc1bffc9c3 | -1.75864 | -52.70568 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f990070c-bed8-3101-b86c-e4d01922c402 | -3.24814 | -54.22265 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8772a8db-6ebd-392e-97bc-464a50de9c2f | -3.76088 | -52.34967 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78242504-b038-3d02-bdd3-c4dbc20fd1fd | -1.48806 | -52.51782 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82d97488-adfb-3bdc-98b1-a8c01a01c4e7 | -2.87298 | -55.18116 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f89ef85a-849c-3b31-b974-e167d41e57f7 | -2.19132 | -53.80247 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b762f5e5-63e1-3597-98bc-022aff1caafa | -3.50305 | -53.82113 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b847006-7286-34fb-af44-91ff937f8075 | -2.33187 | -53.87386 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b2e4c08b-f7d3-345b-8588-bf8846e9d5e1 | -1.60035 | -52.26991 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c180200-f2a7-3527-aa3d-bd8e875a42d4 | -2.97844 | -54.08647 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 306d2e54-243b-380d-8cdf-5efb333dcbf9 | -2.33304 | -53.86607 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b36ee174-b003-3457-87a1-85e8b307a09f | -1.44359 | -53.40298 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b23c8ab-7b00-3900-abfa-58421d0c42e4 | -1.768 | -52.71466 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README55.md)
