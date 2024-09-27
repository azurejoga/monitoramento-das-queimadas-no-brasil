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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 948fc8f7-4451-3824-ab34-97a6ae932509 | -16.89318 | -58.03455 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9eb77079-66db-3206-972a-f7836c34ee90 | -16.88883 | -58.03397 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| af4b98ef-c444-3204-b33f-6cec8b40f43f | -16.88828 | -58.03829 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d565a314-cff6-368a-8ecb-4037af94ab48 | -16.88447 | -58.03339 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f22510d8-2b5a-328a-a02d-561381d65dff | -16.88066 | -58.02846 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f794b7dc-7bba-3534-a37b-05c7af0587c1 | -16.88011 | -58.03279 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 7a55c8ed-6a14-32de-b3fa-2e80b0302083 | -16.87741 | -58.01919 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e2246319-08fd-3d8b-b3ff-7a2a68c0fef1 | -16.87686 | -58.02353 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8a8984a0-a903-38d5-944b-bac7d93720f2 | -16.83607 | -57.7387 | 2024-09-27 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bbec24dc-89a9-373f-aaf7-a19a7b6c038c | -14.04101 | -57.90836 | 2024-09-27 05:29:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7075857-4085-3a33-acde-e0de79fe5fd9 | -14.03679 | -57.90776 | 2024-09-27 05:29:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| be16c09f-ab3e-310b-814d-b56e3b8d706a | -14.04154 | -57.90431 | 2024-09-27 05:29:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18b3a94b-16ea-3e0f-a95a-e0e0d114a473 | -14.03309 | -57.90314 | 2024-09-27 05:29:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 91f017c1-7502-36a2-ad0a-9a1eedf49952 | -14.03257 | -57.90718 | 2024-09-27 05:29:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b9454385-cf73-350c-8500-635e4072705e | -14.43519 | -60.11911 | 2024-09-27 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82e3cbf5-867d-3370-91a1-413d1d41d207 | -13.71569 | -60.06862 | 2024-09-27 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7052aaa9-4e99-364e-a61f-445943f2d67f | -13.71136 | -60.07251 | 2024-09-27 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e41aa50-38af-3eee-b4c5-9c47ab37e1e8 | -12.50079 | -60.74669 | 2024-09-27 05:29:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e161fe4c-adbb-3b86-a0b0-319ad30f3d8a | -8.9978 | -67.3724 | 2024-09-27 05:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 7c745720-38ae-3261-9b88-643be1a2b060 | -8.9977 | -67.3909 | 2024-09-27 05:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 3f9e1252-7306-37c0-a130-b11405b8f08a | -9.3028 | -65.3528 | 2024-09-27 05:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 461e3c18-9344-3617-8c92-8afc78ea92bc | -8.9978 | -67.3724 | 2024-09-27 06:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0f38e17d-297e-3acf-9482-78239e6e1bd8 | -16.8933 | -58.0213 | 2024-09-27 06:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 9af086ca-cba9-3361-af3d-37d681a0cee6 | -8.9978 | -67.3724 | 2024-09-27 06:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7dd57339-21c7-3246-bb1e-209385717055 | -12.7659 | -62.6342 | 2024-09-27 06:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a9fc8197-7c8b-3e80-a017-7a43b7a21347 | 0.91124 | -51.99012 | 2024-09-27 06:18:00 | AQUA_M-M | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 646a5739-10a5-361b-822e-cee4fcf554a5 | 0.91039 | -51.98326 | 2024-09-27 06:18:00 | AQUA_M-M | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 301c0d30-35c9-3fe7-945d-88761084871a | -1.74511 | -55.23676 | 2024-09-27 06:18:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 86f9664c-2361-3186-a95d-34fbfa239739 | -1.45696 | -55.49136 | 2024-09-27 06:18:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 138e6314-dfa2-3e11-92a3-a11231e7fab2 | -1.45465 | -55.50708 | 2024-09-27 06:18:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 775afcf3-996b-34e9-b680-a177bb643b69 | -3.01747 | -51.03318 | 2024-09-27 06:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 7670dcea-8ff7-3262-b06a-125fa9ff240b | -3.015 | -51.02492 | 2024-09-27 06:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6575db02-991b-3d67-aca2-efd0b2afed9d | -3.0124 | -51.071 | 2024-09-27 06:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 3a22d86f-f6b7-3632-b684-a19a5de66ab2 | -3.00965 | -51.0629 | 2024-09-27 06:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 31d50efe-7b02-33b5-9858-e4114a175226 | -2.87531 | -51.66401 | 2024-09-27 06:20:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d9a930bd-ebb6-35c5-a831-e525bf4efab8 | -2.86691 | -51.65863 | 2024-09-27 06:20:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 796c11cc-b894-3090-9627-8706131f71f1 | -2.85915 | -51.66161 | 2024-09-27 06:20:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 936d9973-5496-36ee-a1ff-901742718a76 | -2.92254 | -57.84474 | 2024-09-27 06:20:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 36f25a10-ef3a-3163-9609-1e583f78056f | -2.71579 | -57.50273 | 2024-09-27 06:20:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 70250164-49af-3216-a7d4-e84b710f2b53 | -2.68365 | -57.58192 | 2024-09-27 06:20:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6da2855d-671e-345b-bc52-0f1b3cdf572e | -3.62868 | -58.55596 | 2024-09-27 06:20:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 54f62a9f-3672-3eba-aff4-e0f690df7e07 | -3.62718 | -58.56642 | 2024-09-27 06:20:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 4f49da3d-5133-3127-bb66-587330472f02 | -3.62469 | -58.5594 | 2024-09-27 06:20:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 72b67904-cae3-37d8-b50c-dbad42bdce7c | -1.50051 | -61.59325 | 2024-09-27 06:20:00 | AQUA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6fde5d55-866b-361d-9d27-0a1db0e2df8f | -8.52063 | -62.05073 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7f9e99c6-497f-3952-8cab-8c4393113691 | -8.51984 | -62.05711 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 69a9db02-0da0-3a88-a9ac-ce0fb17d8c2e | -8.51903 | -62.06367 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 15533f4a-06f0-366b-acf9-97035ad82972 | -7.92651 | -61.27856 | 2024-09-27 06:20:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fcc203de-4326-355e-829f-ede345736896 | -7.92566 | -61.28555 | 2024-09-27 06:20:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 782b1e68-318f-3f45-9eb8-b4cd1b45dbb2 | -7.92323 | -61.27437 | 2024-09-27 06:20:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d68119b1-5a54-3368-92ae-5fb0f43b388a | -7.92233 | -61.2814 | 2024-09-27 06:20:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9e8e6198-b6ba-3086-be90-6b6e2b740932 | -7.91939 | -61.27745 | 2024-09-27 06:20:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1982c23e-68da-3197-882e-f2ba6b62e0ad | -7.91854 | -61.28452 | 2024-09-27 06:20:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bfc25fcf-dd59-3f67-abfa-78f3b2c05b2f | -7.9161 | -61.2734 | 2024-09-27 06:20:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 85610dc1-a593-3377-9d68-ee2577e40285 | -7.89573 | -71.61705 | 2024-09-27 06:20:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61314c3b-84e5-3ae0-b2d4-f3951d728c16 | -7.80468 | -72.26804 | 2024-09-27 06:20:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bf8c966-e59e-361c-91b2-0757fab1d88e | -7.79516 | -72.283 | 2024-09-27 06:20:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0cae8844-d28e-32ab-905e-3423528c1251 | -7.655 | -72.46612 | 2024-09-27 06:20:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41c6c4c3-0a84-3b45-b909-0419badb6879 | -7.65441 | -72.47005 | 2024-09-27 06:20:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17808d00-9395-34d3-be22-2442023906d6 | -7.65434 | -73.04541 | 2024-09-27 06:20:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be278db9-eb13-3b3d-8823-4465bf3129e7 | -7.48878 | -72.84361 | 2024-09-27 06:20:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3534f05e-9505-3803-bf47-059fe5420f28 | -7.42232 | -72.70576 | 2024-09-27 06:20:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1129b829-38f0-3c4f-bf7f-ba41c2bdc955 | -7.42143 | -72.70468 | 2024-09-27 06:20:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b28390c8-1b33-3115-86ce-89c24cc4be78 | -7.42086 | -72.7085 | 2024-09-27 06:20:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd18ee49-b454-3e8e-a6eb-bbc05cb90653 | -6.96799 | -62.924 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e17fcbc-e040-340a-8bd0-6c82bb1496ed | -6.966 | -62.92636 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0166b02d-020a-336e-ad14-587dfc827aa2 | -6.96226 | -62.91782 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88c53d5a-2619-3d46-b635-7e777d792226 | -6.96158 | -62.92313 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe339e7c-883b-3093-8fd3-2b51eca782b2 | -6.9596 | -62.9255 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e7354c2-09a5-3180-b4df-145d2420b48d | -6.93802 | -71.48779 | 2024-09-27 06:20:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7296ae3-1a9e-3403-81cf-fc2ed534de06 | -6.93767 | -63.11012 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d479ee1-d24f-3bd3-9ba0-19f0b33c8497 | -6.93702 | -63.11525 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c6b919c-c468-33e9-aff1-ad281e74d338 | -6.93446 | -63.11198 | 2024-09-27 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 614352c9-4bd1-31af-8422-3c94ada1a7cd | -6.82817 | -63.15882 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f6f977f-75a3-340d-8718-71b6dc81382c | -6.82748 | -63.16384 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a85e7e2-aa8c-3ce7-9c52-de3027eff2e8 | -6.82554 | -63.15822 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f864fe8-3cbe-3e57-ac3e-88cb15ea90e1 | -6.82489 | -63.16327 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81b05982-008a-319f-99a3-b2694e5a3af8 | -6.82187 | -63.15797 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a3563c53-f3ce-3b85-8b90-84f58f2f3a0d | -6.82118 | -63.16302 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6cd61ef8-f2f3-3853-ba5e-6acb53da1c69 | -6.81925 | -63.15733 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2558ed9e-e911-3efb-b00e-b3a4477bca5b | -6.8186 | -63.16239 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f6a7a896-6044-392f-82d7-df18af6ada6e | -6.81557 | -63.15707 | 2024-09-27 06:20:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f242dfa9-f86f-3a59-b753-9a2c7ecf5433 | -6.26417 | -62.47556 | 2024-09-27 06:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d268a045-dbc8-308e-9bd7-1775b62cf0c7 | -6.26409 | -62.47675 | 2024-09-27 06:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| d05215ef-4075-3169-a388-21b02bd5d4a6 | -6.25181 | -62.46932 | 2024-09-27 06:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d9d955f0-7fb6-3ec2-bebe-c190623c2020 | -6.25832 | -62.47027 | 2024-09-27 06:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b7398dc-c6a9-3054-aada-32c7a8dfa9c4 | -3.86532 | -65.15754 | 2024-09-27 06:20:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a62dd6a8-1c55-3e40-bd61-389e5eb523ea | -3.85002 | -69.43359 | 2024-09-27 06:20:00 | NOAA-21 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a42edcef-f989-3d60-a465-4e6ab19ac041 | -3.70689 | -69.39471 | 2024-09-27 06:20:00 | NOAA-21 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b575ed43-3bbd-3ae1-be1f-99bb41e23e52 | -3.70293 | -69.39408 | 2024-09-27 06:20:00 | NOAA-21 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4aff60cd-6980-3aee-b4c5-5ef0309ca388 | -3.27428 | -69.04872 | 2024-09-27 06:20:00 | NOAA-21 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 407d5142-d787-39f5-934e-96305f70ec04 | -10.03784 | -53.41963 | 2024-09-27 06:22:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c7723fe4-442f-3ecf-881b-05409b2641aa | -10.02495 | -53.44345 | 2024-09-27 06:22:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 3ba89edb-f838-3b45-bd5f-c1b1de628981 | -12.49607 | -53.45946 | 2024-09-27 06:22:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d346b666-61a7-301d-bc98-19fe6bfc13fc | -11.20725 | -54.77802 | 2024-09-27 06:22:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 1587a1a6-64d9-3259-a903-7f9fe49f27d0 | -11.20476 | -54.77287 | 2024-09-27 06:22:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 6555e15b-f057-3ea8-9514-ad4ab2c86994 | -11.19268 | -53.89296 | 2024-09-27 06:22:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 691c80f7-05ce-3d82-808a-36cd2badf1dd | -11.18746 | -53.89982 | 2024-09-27 06:22:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.9 |
| d2ee4cfb-7823-3f2d-bd41-a93b4d36a764 | -10.92341 | -54.2378 | 2024-09-27 06:22:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 8f2e69cb-da79-3792-8237-e0aa4e52caa2 | -10.92248 | -54.24272 | 2024-09-27 06:22:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |


[Clique aqui para ver as próximas entradas](README128.md)
