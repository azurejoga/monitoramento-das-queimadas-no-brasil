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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ae17e22-3995-3077-acdf-da1a5daf7c93 | -7.3157 | -44.7515 | 2025-10-13 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 0a5679bf-fdc7-30f5-909c-e1891fa8c219 | -3.0726 | -49.404 | 2025-10-13 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| cf0b1878-0bf7-3d3e-82db-da736f6d7fa1 | -16.1207 | -53.9625 | 2025-10-13 01:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 2d6ab096-d7f1-3440-8c01-d348528a7ead | -17.3384 | -53.7922 | 2025-10-13 01:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d64167fc-62e2-3eaa-abc8-3a740936656d | -14.2825 | -51.5384 | 2025-10-13 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 97769909-8214-3341-9096-86e32e9c742a | -14.3019 | -51.5359 | 2025-10-13 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3d0e1cf5-c303-31c6-bec8-9cfe55ab9da1 | -2.5424 | -47.7893 | 2025-10-13 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 688ae32f-63cd-3c95-aa07-41d6f4bf5cfb | -2.5423 | -47.811 | 2025-10-13 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 3341ae67-cb7a-38cb-ba61-7d8d386afa70 | -16.1203 | -53.9836 | 2025-10-13 01:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 5290938c-7ca1-380a-8883-4b4b6fcfaee4 | -2.5239 | -47.7899 | 2025-10-13 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 157d9e55-ded0-3479-84bd-b3ddc6ad3d62 | -13.4977 | -51.2992 | 2025-10-13 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 065844a8-8a50-373f-964a-2e420b6f1d3c | -10.809 | -43.9979 | 2025-10-13 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5a719348-882c-3da1-86c9-c47417bfafe8 | -7.5449 | -46.089 | 2025-10-13 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 7096a5cd-ec3e-31ad-905e-99f7cf4d7f7b | -17.338 | -53.8135 | 2025-10-13 01:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 4a1233f6-bef1-3dc4-9a7c-02996b25d18d | -2.5238 | -47.8115 | 2025-10-13 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 7454f115-b77e-3ba7-b6cf-06a0c14b1b22 | -13.8563 | -45.498 | 2025-10-13 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 861f2238-5521-33ec-8354-c878b8b4b510 | -3.0726 | -49.404 | 2025-10-13 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| bce5cc91-b9e9-3d12-8904-ed36208e6391 | -17.3384 | -53.7922 | 2025-10-13 01:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 16da29d9-5181-3aec-ba45-1a124012c594 | -2.5239 | -47.7899 | 2025-10-13 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| eb0477bf-2ba5-350a-94f2-3867ab886a22 | -2.5424 | -47.7893 | 2025-10-13 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 64247052-96d8-3460-94de-06e6448ad094 | -2.5423 | -47.811 | 2025-10-13 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 7f0daa53-9630-33a8-ae99-d72183e43e8f | -16.1203 | -53.9836 | 2025-10-13 01:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b011a3f1-d66b-3c00-84d2-5c079dd2a4d8 | -16.1207 | -53.9625 | 2025-10-13 01:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5606f351-9d79-3bcc-9811-ef8a868533b9 | -10.8093 | -43.9744 | 2025-10-13 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 3e0534f4-0362-3ec3-b9e2-58a1ab81440d | -14.3015 | -51.5573 | 2025-10-13 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 17b59c61-3313-3f8c-a5ce-e0b8e104ab30 | -3.0726 | -49.404 | 2025-10-13 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| a16a4473-196e-3a1d-bf1d-308383b20aa7 | -2.5239 | -47.7899 | 2025-10-13 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6be9f36d-2bf1-3e9e-bed2-874641697ad9 | -7.5449 | -46.089 | 2025-10-13 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e147b594-783b-336e-bb7a-5f4d67b2e72e | -2.5423 | -47.811 | 2025-10-13 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| bbfad89d-3972-33f6-a31d-151b9a3acccc | -16.1207 | -53.9625 | 2025-10-13 02:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 83b6fb20-b316-329e-acb6-bdf32abda419 | -17.338 | -53.8135 | 2025-10-13 02:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 7954dacc-b993-3b96-bb3a-3cc128f95759 | -14.3019 | -51.5359 | 2025-10-13 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| f157c4c4-5339-3770-8019-75c8ffc38c42 | -17.3384 | -53.7922 | 2025-10-13 02:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 92.6 |
| dd96cc64-922c-394f-bad5-162e2518d595 | -2.5238 | -47.8115 | 2025-10-13 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 01a12c3f-a262-3099-a272-85a7eedc7b65 | -2.5424 | -47.7893 | 2025-10-13 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| d05c7d36-4cc0-32cd-b086-cadc13f3c016 | -14.2825 | -51.5384 | 2025-10-13 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c93d5467-769e-3dba-8207-39620bde2724 | -10.8093 | -43.9744 | 2025-10-13 02:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 803cdd04-623c-3be6-b633-28648eed757b | -16.1203 | -53.9836 | 2025-10-13 02:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 7fd11b9d-5da3-3796-93c4-8b3a88429d84 | -14.2825 | -51.5384 | 2025-10-13 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ee21880d-1a98-3846-866f-b2286473bf64 | -2.5239 | -47.7899 | 2025-10-13 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f6b3c2bf-14cf-3f3a-b40e-2d5bb39029ba | -2.5238 | -47.8115 | 2025-10-13 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 9f059cd2-0917-3dc3-a198-1b9b2cf78341 | -14.2639 | -51.4982 | 2025-10-13 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 90e26a28-2cde-3b8b-98fb-03b26e1b42f9 | -3.0726 | -49.404 | 2025-10-13 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 1b4da557-8240-3dcf-b124-1d31920cc358 | -16.9686 | -45.5582 | 2025-10-13 02:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 1959770e-2d35-3b67-9375-69aff5bbf38f | -14.3015 | -51.5573 | 2025-10-13 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 21b082a0-7271-34fb-bee5-ad9e85620115 | -7.4863 | -44.621 | 2025-10-13 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 65ece697-3d7d-3af3-8d11-61d2b4e4a0b6 | -7.5054 | -44.5962 | 2025-10-13 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 425af9fe-894f-33d8-8e6a-93c2472bacef | -5.0994 | -43.1977 | 2025-10-13 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 299f9027-ef9b-35fc-aae4-78e3d9897a92 | -14.2636 | -51.5196 | 2025-10-13 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 86fc375e-e26c-3599-a474-cc1050193a31 | -7.5449 | -46.089 | 2025-10-13 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b529fa51-52f4-312b-9467-ca2c165333d2 | -14.3208 | -51.5547 | 2025-10-13 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 95fd5019-5628-3466-82c5-f2df2310f911 | -10.8093 | -43.9744 | 2025-10-13 02:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1e723a07-d5d4-3df4-928f-7fb4a5279ec5 | -17.338 | -53.8135 | 2025-10-13 02:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| ca882de5-84ff-3d7f-aff8-3463353ae099 | -2.5424 | -47.7893 | 2025-10-13 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| fd964e0e-5b47-3c26-9c5f-57513c4b2376 | -7.4866 | -44.598 | 2025-10-13 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| b6e7ccc5-543f-3cc6-9ce7-d111700a33b5 | -7.5052 | -44.6192 | 2025-10-13 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| b23608d2-6b4f-3f16-a0a3-659a0e5972c5 | -14.3019 | -51.5359 | 2025-10-13 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 46e90bd2-0ab0-37c9-8c18-e7ba594a8bfb | -17.3384 | -53.7922 | 2025-10-13 02:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 17bb28e2-d49b-32a2-bb00-296877992f2a | -2.5423 | -47.811 | 2025-10-13 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 31a84d23-3d8c-3303-bc36-0cc1e7a42d06 | -2.5423 | -47.811 | 2025-10-13 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| a9ce7137-4b17-3c7c-89e1-be5d34b1703f | -8.8347 | -45.283 | 2025-10-13 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| dc845580-0c60-32a8-b42d-50206345ce13 | -2.5239 | -47.7899 | 2025-10-13 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 10050ee0-7da4-33ab-931e-b0f372ee9510 | -8.8539 | -45.2581 | 2025-10-13 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 290.5 |
| 771d9e03-64b6-3072-b952-eb75ee1f8d5f | -8.8353 | -45.2373 | 2025-10-13 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9bd29057-0195-3b35-b04f-6d86ac6e2c08 | -7.5054 | -44.5962 | 2025-10-13 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b6efa720-52a2-3edc-8df8-d6a3eb48b97a | -16.1207 | -53.9625 | 2025-10-13 02:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1d83c3b2-0fd0-3b56-8917-9c58a20a8a05 | -2.5238 | -47.8115 | 2025-10-13 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3f3225a5-452c-340c-b7ea-96d885751b20 | -7.4863 | -44.621 | 2025-10-13 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 0c333d82-e34f-3710-8268-f6b67d7d49dc | -2.5424 | -47.7893 | 2025-10-13 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 056c70a0-7bec-33af-8539-cdb03e9dfab9 | -8.835 | -45.2602 | 2025-10-13 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 273.8 |
| 541c5a6e-04b1-3016-9fa3-9e40d332f5a0 | -7.4866 | -44.598 | 2025-10-13 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b9e7c1ea-2f4b-33fd-b293-edbfd1a3382e | -17.3384 | -53.7922 | 2025-10-13 02:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4f06266d-be6a-3c7f-955a-a77f9a6532c0 | -17.338 | -53.8135 | 2025-10-13 02:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e4326bde-f53b-37e1-9c84-7af08e34f81e | -7.5449 | -46.089 | 2025-10-13 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 3b337b49-6fc9-3535-924a-eaf0a55eba1c | -16.1203 | -53.9836 | 2025-10-13 02:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a426820d-76de-3692-b8cd-41bac2b0107f | -8.8536 | -45.2809 | 2025-10-13 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 98d0982a-b6af-3f31-8117-9acd9622dab2 | -8.8536 | -45.2809 | 2025-10-13 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2b0f0714-4ea0-3b73-800b-55522b6fdc5b | -14.3019 | -51.5359 | 2025-10-13 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 33a2ca1d-d257-30bc-a09e-225afcd94216 | -15.7027 | -46.5983 | 2025-10-13 02:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d3b0eac3-c078-3800-9661-a04f1265163b | -17.3384 | -53.7922 | 2025-10-13 02:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 9ac4947f-d240-3bcc-ae64-351b4b71d816 | -17.338 | -53.8135 | 2025-10-13 02:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0c29ce32-60ce-3d7e-89c3-1de92eda1224 | -14.3015 | -51.5573 | 2025-10-13 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c9fde466-37ad-333a-987b-a9a2b47a703e | -2.5423 | -47.811 | 2025-10-13 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| bea0eb6f-f60b-39aa-90cd-e32d1bbe94d1 | -8.8539 | -45.2581 | 2025-10-13 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 85bc6f27-7ed1-3ec3-ab0c-1e2da4032970 | -16.1203 | -53.9836 | 2025-10-13 02:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 0ffede57-1e39-3620-97f5-6a1dda82097c | -2.5238 | -47.8115 | 2025-10-13 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f46110ce-a072-33be-be5b-b5466cb3a8bd | -7.4866 | -44.598 | 2025-10-13 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| eb9226c7-7a9b-3e26-91f9-8f9006513a53 | -7.4863 | -44.621 | 2025-10-13 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c6d0afd0-34b8-360c-990e-3718c5641245 | -7.5449 | -46.089 | 2025-10-13 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| fd7bc3ea-4405-3067-aff3-d9b263cb85d6 | -2.5424 | -47.7893 | 2025-10-13 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 53f6e52f-6837-3ec6-88e9-aa8371b5bd58 | -14.3208 | -51.5547 | 2025-10-13 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 11e21d02-9cc8-3314-ba84-a451a6fc67d8 | -8.835 | -45.2602 | 2025-10-13 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| c0f962d4-7217-3991-9484-f938aaf003c6 | -7.5052 | -44.6192 | 2025-10-13 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 24e18a0d-d701-3987-99d5-f578af25746a | -7.5054 | -44.5962 | 2025-10-13 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 2819b1ec-03d7-3528-b35b-fa7cd44be94c | -17.338 | -53.8135 | 2025-10-13 02:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 95.2 |
| bdd33bec-2364-3226-9ed5-a537885aba8e | -4.4886 | -44.9382 | 2025-10-13 02:40:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7d372cf9-c4ef-34b9-827f-278fcd953fe2 | -7.5449 | -46.089 | 2025-10-13 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9b2932d9-bc12-38f8-bed8-b712fda8772f | -14.3019 | -51.5359 | 2025-10-13 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 65d2180a-4209-3cc1-8133-c16f84fc1f62 | -14.3015 | -51.5573 | 2025-10-13 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| bfdb9fa5-4ec1-33dc-9804-c43db56cd6ad | -2.5238 | -47.8115 | 2025-10-13 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |


[Clique aqui para ver as próximas entradas](README6.md)
