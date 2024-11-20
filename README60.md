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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bcfb010-847a-374e-b764-cbc650ce3835 | -0.90693 | -51.7374 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05d3fc79-c2da-3ba6-a3a1-a0490ead6501 | -9.18053 | -44.71878 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd3c0819-fec1-37ea-9a8a-6b3df1c95e0f | -3.19622 | -54.32253 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d47a0f48-b510-3f06-aaf5-77ea1d76eb08 | -2.93287 | -48.33443 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa9d8008-bf0b-3ae0-8d68-64aab85d9803 | -3.81874 | -51.35822 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b2698ba4-b323-3634-8a11-f48d29be9b82 | -5.45084 | -49.6852 | 2024-11-20 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bee93c7-d56b-3bb2-bcbc-5efda618b45b | -2.60807 | -48.21565 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1043aa1-1d74-35f2-9e19-a06fd7d803b6 | -2.6238 | -54.2687 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b82b6406-8214-3d00-82df-3ec59b5c716d | -1.63313 | -52.629 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4086a2ef-c236-3da7-af22-56fabca8e17b | -1.39121 | -55.62197 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bbb4722-ae0c-3f9d-a04c-5c2c7e4dbe64 | -2.10572 | -50.65371 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f3ae6c-c8cb-3f80-8574-5ace49d069c8 | -5.16362 | -49.65482 | 2024-11-20 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 495d587b-aa85-3289-b761-1ccddc0ede28 | -4.46352 | -46.584 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbec6572-09b4-3229-90f3-c42d21e2c38d | -4.16696 | -46.81869 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbe35393-d376-3cac-af6a-4f820db4993d | -2.61076 | -48.24665 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f3ed626-71a2-3da5-b84d-10599f454418 | -1.52174 | -55.48471 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a025da9-8f72-33dd-86ee-be6c04d55d5d | -4.99203 | -46.92827 | 2024-11-20 04:50:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 098d0ab8-28f3-3cfc-acc4-197a1349d5fd | -2.74384 | -51.82332 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| adee65e4-fc92-3114-88e0-645a81c3dde3 | -4.49054 | -46.71347 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a27a3be1-fc40-3f9b-b80f-5906098c8a4c | -1.36646 | -55.37349 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f79c0354-01b0-377b-94c1-a0c9a5118c57 | -2.26178 | -50.79964 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86aa570d-408a-3649-a1c8-6a859226fab8 | -2.65885 | -46.24116 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7466157-afa3-389e-b964-ea7b87e3a3dd | -3.28719 | -53.8283 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 530edb95-6552-3f41-b490-2f6156057928 | -3.04547 | -54.40859 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed895285-cd8f-374e-83fd-50b01b2a0515 | -3.2933 | -53.85623 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73b7f3a3-c61b-3c4d-839f-7d710d9b2da8 | -2.19399 | -49.75388 | 2024-11-20 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5ab867a-12f2-3238-82a1-c5fa74cc6410 | -0.92806 | -51.6414 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b062dc1-c5fb-3bf9-aa01-c2b1add5863e | -2.45546 | -49.15077 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b563d4c-654d-389e-8d39-16c6a04781c2 | -6.82103 | -43.28661 | 2024-11-20 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 349eca92-159e-31a8-88a4-5f317bee1960 | -1.10222 | -51.74341 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 027b835f-175e-32b4-ba8d-ccbf4718a047 | -3.70308 | -43.47241 | 2024-11-20 04:50:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e426ac9-4c0b-3c81-b2c4-b287272784ae | -4.3667 | -50.73083 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1bc3359-f1c5-3a00-ab95-216ca4675b31 | -3.55455 | -53.5354 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 782b3ceb-9831-3fcc-a3ca-05c1a6fa1c6c | -2.29856 | -49.00069 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af3aeff4-d88b-3b0b-a732-7b0cadbc8c68 | -1.19608 | -53.67398 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 67c3623b-ec05-3424-aaa5-b49d93da794d | -3.70976 | -51.84058 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d56b798-2c1c-3244-b3ef-b4ea1bad3b3e | -1.33904 | -51.39869 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a890b661-9afe-34e8-b2e5-01fcab3c1515 | -4.69933 | -47.96036 | 2024-11-20 04:50:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e72e33b-4f1e-39f3-911b-ed19809dceb2 | -2.02348 | -51.17738 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbbb77ae-6a8b-33ef-a21a-5dfffed394af | -1.62471 | -52.61675 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcfe5f5a-8ebe-336e-b2bd-34f5edfd6a89 | -1.95983 | -48.67631 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f05d9b4e-d765-3e73-bb09-2fa633d5ef72 | -1.09835 | -51.74635 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 393c6f52-aaa1-34a8-a7fc-712337905446 | -1.20113 | -51.77991 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bb7575a-6d98-3276-a57a-75bdb94fbb90 | -5.18372 | -45.44255 | 2024-11-20 04:50:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d63d422f-4aac-3003-8c05-fff8f353898d | -2.29805 | -50.65511 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abcc6b54-76e1-342c-808b-89f29a098051 | -0.7812 | -51.7604 | 2024-11-20 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6377582-c044-3e3e-a5d1-dc92cc42e912 | -0.95262 | -51.7231 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 367a7c52-1619-3ed6-a81a-10a0bca5ffaa | -2.02734 | -51.17445 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89c0665e-a947-3e90-896a-3b2977bcd128 | -1.26892 | -52.70363 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2e5229f-8701-339b-b8d7-38e72e6b9d63 | -2.72942 | -49.33994 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b75e70f4-8a5d-3a50-88ea-6e23247fbea6 | -2.86421 | -51.78906 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11975c7f-fe26-3728-82d9-876098c8a1dd | -4.78926 | -50.48232 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 219da245-d4ef-35f3-a794-c2911968aaf5 | -1.66339 | -52.66253 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74f19837-586c-3c76-a060-b351981ff3fe | -2.92006 | -53.06263 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 767c1b36-cf7b-3697-bafa-87d7a1406dda | -0.92616 | -52.0642 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d183b14-6e30-36fd-8413-6d3ed9451445 | -1.2337 | -51.74601 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52f5bf9b-1af7-33f4-8a3a-24157b791dc0 | -1.30861 | -52.40773 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0986405f-73bd-3dab-965a-b373ff5d21a9 | -1.41331 | -52.38787 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a03be95c-0020-3f5b-841b-8448b243e99c | -2.80514 | -51.80109 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c01054a-fb78-3e0d-9fbe-fa05aa9f971e | -2.68487 | -48.51434 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41a983ab-c5f1-3eba-bb4f-44278c1f0ab1 | -2.95616 | -48.3293 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0295e08-c34f-3c76-92e3-f8565826f790 | -1.38528 | -51.55391 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04d5d695-56ee-3857-8550-69a6faf26218 | -2.20855 | -50.53358 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 402d86a6-a21b-343d-a648-35a2d939de15 | -2.28185 | -48.49152 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2677c19-bf3b-35b2-8320-795bd390295b | -1.64315 | -52.68126 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38baa089-0524-3911-bb4d-8109004b586b | -2.21587 | -48.77117 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47075070-4989-3a43-983f-1e29f08cb1e6 | -1.12277 | -52.2781 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 105a8580-fe72-33ed-be10-2ea05f3eba86 | -2.03344 | -51.17894 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b7996d2-6513-3d2d-b21c-16b3b629551c | -3.65047 | -54.32612 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56370bb6-baf7-3184-9a1c-98eab33786df | -3.80725 | -52.31562 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcb2c820-022f-301f-a9bb-94cdd2a304d7 | -2.41065 | -49.06893 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e01059b7-da45-31e6-a3f9-1b15ad4f99d3 | -2.84623 | -54.00621 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 880972c3-0387-3cb6-8094-6ccc7bfd9454 | -3.75704 | -51.34528 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 150f7072-524f-3fb7-b304-872b8b5bd5e4 | -2.88172 | -49.16884 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9239cd3-3cde-313a-854f-670174d00cfa | -1.62967 | -52.67916 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e17e0fdc-38ee-32a2-893a-397506efbe1f | -1.34063 | -51.85822 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74322bab-24f3-3e23-bd37-abf7109edc2c | -1.64765 | -52.67467 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4d3ef2e-ab77-3564-bd2d-de18dc640b4a | -2.17084 | -49.31563 | 2024-11-20 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca21e412-0006-3705-98b2-604fa1701491 | -3.05675 | -54.40624 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4dae684-e370-3ff8-839d-9f97b4af4a0f | -1.79409 | -48.05994 | 2024-11-20 04:50:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 882ecb62-b630-3f6f-97ba-f0fefb29282b | -1.13248 | -51.68086 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a60620a-34f5-3f91-962d-841daa37f81b | -1.14264 | -53.6663 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75ba27c6-afc5-351e-8d44-d5e1203f263f | -2.3845 | -53.66385 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 739d8ed4-ee71-3d57-be0d-7390bdbccd90 | -1.96069 | -49.54922 | 2024-11-20 04:50:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31a1d0bb-3927-3a54-aaef-426199fbeccf | -3.00735 | -51.0077 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8605c583-1a0a-330f-95db-536c77bc3c32 | -3.48541 | -50.31406 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 712b1aa4-6c8f-3dce-8665-5575be917f0f | -2.89812 | -53.04818 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38c124a5-6dd2-37e9-900f-4783aee98c4a | -2.62408 | -47.96494 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17c2a4b5-23ac-37e7-869c-c8f06bb5fbc9 | -1.20276 | -51.76954 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23080d36-4e53-3b9e-a78a-04a5549699c5 | -2.84972 | -54.00676 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5c9c94b-849a-3bc8-a8a4-fc2162fe9af4 | -2.16946 | -48.39972 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f8031e9-2a45-3874-8754-9d09ce0d0858 | -3.36837 | -54.10489 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b13b9ab5-f7c4-3e8c-a219-f8517c55a8ad | -3.78053 | -47.48411 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 523a3251-8162-3d47-bf73-52aaedebc1f5 | -1.51726 | -52.08886 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0243b70-63e9-3e02-8b79-a97d906f6a78 | -3.65812 | -54.32331 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49be4b04-e8b1-3a87-a6e9-50dca57149f0 | -2.62341 | -47.96934 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cae6f6ee-bb79-3682-ae0c-39aa1ed3502e | -3.94845 | -47.00662 | 2024-11-20 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7af5a65c-9ce7-3add-9137-86bb3053af94 | -7.21286 | -54.99799 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48acd4d4-468c-370b-8f04-51f47c6ff116 | -1.21322 | -51.74637 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23c758fe-797f-33a1-a3b3-dd4854e33ef7 | -5.78908 | -48.15724 | 2024-11-20 04:50:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README61.md)
