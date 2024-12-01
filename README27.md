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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca6ca312-c394-3496-b70c-30258d3e9fff | -3.59293 | -50.37827 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8931814-53c0-39e0-9f9c-6bdf214e8442 | -2.46833 | -46.56909 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef3216b4-2472-35f1-ac2d-e836839c084b | -2.83302 | -54.0965 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62ae5881-0a11-38e8-874c-d26e1b6362eb | -2.63166 | -46.20319 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07493a25-55ee-3de5-ba86-62492d6d8297 | -4.00243 | -44.75681 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 47459118-4f10-3370-a531-899408fd8514 | -3.5428 | -50.18325 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3d16d3c-3781-393e-94df-ad5d5e7a581d | -2.63681 | -54.22614 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 800203cf-a57f-35e7-9650-73c40d145169 | -1.07252 | -53.63369 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acae2adc-95d0-3002-9a4e-fa6af81b7dfe | -3.52685 | -50.4747 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c70f6e00-fb79-39b5-ae66-c8e50f20255f | -3.06296 | -50.33199 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26e52960-a1bc-3249-add0-4616b18ac3d3 | -2.1486 | -54.87531 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6aa68036-37d0-33d2-9230-e4224360d603 | -1.04251 | -51.73594 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 425e283d-6425-3c26-8e24-17f44aed54cd | -2.04471 | -54.66834 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b268a7f-3793-3e8d-8f43-335ed65fcd64 | -1.32584 | -51.67308 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4b68147d-a76b-3bcc-8a94-75aa3276d50c | 1.25737 | -50.68993 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cd1c8ee-da3a-37c8-b6ee-47311549ecec | -3.27205 | -50.21692 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7a68e77-3146-33b0-8cb8-f70ea13557be | -4.53795 | -45.69817 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 06e40efd-3716-338b-88bc-167b1c7c2ed5 | -1.27596 | -54.55738 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67b92c9f-3a17-3e6a-9dd6-346491090c5e | -3.10677 | -50.36446 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa3d9012-9748-3757-8970-e6a40e4802ef | -4.69918 | -42.396 | 2024-12-01 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e46c0f67-f883-3a62-8141-9933622f956e | -3.13988 | -45.98529 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c26314cf-6a70-3a6b-b38f-23aab3f06eab | -2.26493 | -50.71851 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b676165d-1e78-375b-8627-5ac7209e71f0 | -3.67759 | -44.70222 | 2024-12-01 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9937c4d5-be78-3ba7-a3bb-51f6fbb0ddd0 | 0.98068 | -50.12598 | 2024-12-01 04:21:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a276c25-c29c-3e21-8f77-238ecab59346 | -4.05979 | -46.82553 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cad76e7-4418-3b90-85a9-f8e027500a86 | -3.88762 | -46.40738 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55d02cac-137a-3245-acf1-07fa4d77b51c | -3.82339 | -46.59384 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55930a92-65bd-37de-b4cf-9f521ea3072a | -3.85284 | -46.53642 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79433871-fcd3-3024-8e7f-98d1326d10f1 | -2.56103 | -46.40186 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3367df6-0961-358e-981c-3e364169c23c | -2.57766 | -51.88515 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57855c71-ce1e-3ca4-80f0-7f834402ab65 | -3.07458 | -53.80777 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04c03d70-51a4-35d5-98f5-a978dfe04106 | -2.75209 | -51.66142 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2380e9f2-c7dd-3b38-abf1-41ad9bc4ce9b | -4.5525 | -43.29871 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 68ee0f15-767b-390f-a64d-d9589d87fd43 | -3.09004 | -50.35753 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 534109d8-e68b-3e2f-be65-cd24adad4db2 | -1.67307 | -46.22881 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 789394f9-ce0a-39e2-b7b9-50fbf0bdd437 | -1.67062 | -53.77873 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3f9e5e5b-6403-3c3a-bc94-ffca8462f1b3 | -2.56675 | -46.41058 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 874a9323-3df7-3922-b5b3-ae7ea46d5eaf | -3.08745 | -51.07452 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0b73038-fa71-355f-bee3-053d446d6020 | -3.38075 | -50.1144 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 389a0b1c-3e68-37bb-be11-a868b2d3daa9 | -2.87489 | -46.79494 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9e26a7c-dc72-3f7f-93d7-06384dc64329 | -1.36039 | -55.15294 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e951649-10e2-320f-ad7e-c3febe59459e | -3.46696 | -50.27053 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 68df83b2-4527-34fc-88ac-21c1a0080b35 | -1.08888 | -53.63952 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46f92fb4-fe91-3949-9170-69fafa569562 | -2.75129 | -51.75736 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cbda997b-c60d-3d57-ba06-2818c4a52785 | -2.32057 | -53.85213 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5819757-a15f-307b-992b-6548e6db8ee9 | -4.03607 | -46.9291 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a35c9887-2679-35e7-a213-be98b9540908 | -3.93407 | -46.70809 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75e9136c-8456-352a-babb-79f5e1855793 | -3.03852 | -51.48021 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05678eee-756c-3c18-813a-bc5b82628521 | -3.8485 | -46.52395 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c859939c-78cf-3e01-8b62-4256c44ca62e | -3.29477 | -47.02817 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a19e59f-ba05-3307-bcd6-492c93c7f81f | -3.4642 | -50.27121 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 65764d30-0f17-341a-97be-43b02e4bebfa | -3.00695 | -53.23183 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa2196f7-c1c2-35b7-9aa2-bb77d6517011 | -2.12437 | -50.63243 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70b2f29c-278a-310b-b062-a03ab1707eb7 | -2.19121 | -53.77539 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ddfb7ea6-6689-3550-a341-671f80c061a6 | -4.23744 | -46.61538 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c6b0726-69fb-307d-bf6d-652b93231f6f | -2.81894 | -46.85101 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27a3a918-3f2b-34fa-a412-6f49900a5251 | -2.789 | -49.82904 | 2024-12-01 04:21:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67e3cc11-00c2-35ef-b8b2-b346af8605bd | -2.12226 | -45.96099 | 2024-12-01 04:21:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2315b3c-d46f-372b-8c8b-d6c2165dd400 | -2.86901 | -53.98618 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42bd2b34-f3c4-3cff-ac0e-3c72805cc915 | -1.00293 | -51.72987 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea15446a-3e65-3a0e-8645-ea851bf47734 | -4.09472 | -46.1406 | 2024-12-01 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36f940e6-d700-3344-b25b-b744bf47a0fb | -1.49881 | -52.60437 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54cab985-338d-36b6-85c8-c78690bad894 | -3.32521 | -50.18781 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56dfdbb8-21c3-34b2-8bde-7db5e9644e2c | -2.44327 | -53.61859 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b851ab67-035e-3625-a16a-47b131c6dd79 | -1.6069 | -46.23021 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e5b422c-2087-3725-8a51-4f5d9cb61f3c | -3.14407 | -53.83378 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9dcf8e5-3f2e-3f87-8859-918c2c9db2c8 | -3.26657 | -50.09605 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 913bf445-5659-3fdb-af06-a01f058868e1 | -3.09873 | -53.72914 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52831f77-28e4-37db-86fb-a6995a2c129d | -2.65504 | -51.86982 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e4f96423-b170-3b5a-9fd7-4d2d9efd5fb9 | -3.0322 | -51.53737 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 832c6566-501b-3d89-afbc-2c4f48b55928 | -2.32933 | -50.6757 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f69b74f-662f-3c6c-bf21-e1245df10d7e | -3.93181 | -46.50644 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c5dfaf6-9ce0-3925-9f50-4489514a261e | -4.0019 | -44.76026 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 943018a5-0eb8-35eb-b358-122f67e06de3 | -1.23135 | -51.80991 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 284ed232-1560-3f08-a2ec-9f75bd475306 | -2.46772 | -46.57298 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39209875-667b-3d63-b99e-1aee95a5583f | -3.41527 | -50.2466 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7cb0285-3ff1-3a23-9321-000d6a048976 | -3.68597 | -50.23895 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ae609c6-47c6-3ca7-9886-2845457b4c7d | -3.32562 | -45.29852 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b8c7789-77ba-3f27-8f64-cc88bdfa8f3d | -2.08758 | -50.64702 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fa8a580-b980-3ca9-b4b4-d1c6f31f896a | -3.38269 | -49.8583 | 2024-12-01 04:21:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f5f36aa-0833-3d42-9012-2a0a28ae66f8 | -2.48037 | -54.014 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07a0e671-cd19-3293-8543-fcf407dffe6e | -2.47183 | -46.56963 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d44a86a3-3e38-3161-9e5c-08d664807c71 | -3.36608 | -51.12763 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3ea5c70-d208-3c89-8b51-b185b2ba7fac | -0.9618 | -51.659 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fff92178-9a0a-3eca-bb60-def669d5d9fd | -3.98947 | -46.65049 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc683464-df69-3997-94b1-4f8be5a9614d | -1.07761 | -53.63795 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f6054c6-6f55-39d6-9a50-53768a4ca925 | -2.73723 | -54.03939 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f430d09c-9d4e-3565-a687-45e40775b2a5 | -3.01098 | -51.79034 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fdf90408-dc77-36dc-a5db-c1b17a4c0080 | -1.27579 | -47.86874 | 2024-12-01 04:21:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 24df8c70-e55c-394d-a6d1-4f7503457a77 | -3.26396 | -48.7715 | 2024-12-01 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee5eb2ed-282b-3d29-9c66-6c174a568c77 | -2.65589 | -46.57764 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e267df-7633-3405-9fe5-bc78c04c60ad | -1.99271 | -48.67388 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d45735d-b9b9-3737-837a-087cff06b8fc | -1.51595 | -45.91055 | 2024-12-01 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 596b2bf0-0b83-3139-b160-ff2079e47c2e | -2.44213 | -53.62555 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35eecfc4-c4bb-3e1a-af35-86d64cff2aab | -2.04688 | -51.19465 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b8f2016a-00bf-325f-a672-5044b9cea9e1 | -3.22064 | -45.76687 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5b537a4-d74b-3519-9306-483e2ca24078 | -3.46485 | -50.26715 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 56a845c5-80e3-3412-b22d-d4dfc080b7d2 | -2.94759 | -45.71335 | 2024-12-01 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13af819c-d588-3b06-9b9f-284e99cbe40e | -3.14558 | -51.29645 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3e3295f-596e-31ae-a10a-de6c0598cb15 | -4.17662 | -44.42444 | 2024-12-01 04:21:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README28.md)
