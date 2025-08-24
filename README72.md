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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6c0d43d-8584-3882-9f2b-68392bc09c31 | -6.68141 | -58.85688 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d3295bc-3a20-3d81-bd8b-5f41ac923898 | -5.61455 | -60.23548 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffbc3e96-c3d9-3f7a-ba0a-fd3e727d9fb6 | -6.9344 | -62.98236 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc6a4861-55d9-32ea-a205-8fa0616c18df | -11.99327 | -61.02331 | 2025-08-24 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c3cebe0-4105-3a46-a774-ca022c1e9c3f | -7.43188 | -60.62184 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 013f08eb-11b9-3ca7-bfb4-71482bccce82 | -14.29876 | -58.49532 | 2025-08-24 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e53863c-b779-30ad-9fdb-4ec006eda6d8 | -7.30208 | -59.62521 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a61b602-a93e-3060-ad7d-83eeeb8f6752 | -13.66285 | -59.83664 | 2025-08-24 05:23:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21469aee-39ee-3eb2-a789-efc951ce2534 | -3.43522 | -49.04983 | 2025-08-24 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 11567ea9-d31e-3e2c-a39f-1e3b2e0c37e1 | -6.31337 | -59.87263 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 465e4488-f498-3b3b-a037-5fb0ee48f417 | -11.69417 | -60.18716 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7b4e84a-5450-3553-92e3-d78664a5871b | -7.79072 | -61.57623 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 846f4429-d6af-3d98-b454-cb457440db47 | -12.59246 | -60.35774 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| db98eb4c-3081-3b8b-9b33-42964a7c7355 | -11.8312 | -55.21481 | 2025-08-24 05:23:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5360af73-4d46-3571-88f7-d213f2b7ac5a | -3.51247 | -47.20455 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc0c352e-9b84-3b4d-a189-7ed4631c95ff | -7.554 | -63.85652 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd9a9a7c-c027-346d-bdf3-22dba1618f30 | -14.34551 | -58.59666 | 2025-08-24 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d911914-05cb-34ad-b1f7-e860865610ab | -2.93205 | -53.69722 | 2025-08-24 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a784bad-7d09-36cb-87e4-59389b735638 | -13.02778 | -56.87908 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd98aafd-153f-3687-bacb-d7913a40c20f | -11.69473 | -60.18345 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90e9f9d9-5640-3ead-b05c-a8c28883a697 | -7.02484 | -55.43845 | 2025-08-24 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3789ff31-0298-3fa5-b027-0b8aa6d7470e | -11.70095 | -60.18823 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6b90bd3-2d51-3b4c-838f-6c105bcc72e2 | -3.89751 | -54.68913 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c561e112-7f4f-3d7e-9a9f-fca7e2429f93 | -6.57711 | -59.87768 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dc170d7-6b5a-375f-af68-e0f82cbd72b7 | -3.43913 | -49.0503 | 2025-08-24 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 24979212-4b08-3860-a9cf-14659699f8de | -6.92018 | -52.85443 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a340106f-f286-3fa6-857a-96ab27ab6c15 | -9.49711 | -68.47005 | 2025-08-24 05:23:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ad09ff3-9b41-307e-bc16-9874633c3234 | -6.68539 | -58.85372 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6bd0d5f0-1d7e-35fc-a9f6-c7f3180533cb | -9.68597 | -48.34924 | 2025-08-24 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5c9bf41-78d8-3476-b4db-c0c50cbae6f3 | -14.84669 | -48.31911 | 2025-08-24 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5eef0d51-7838-3623-bcf2-f32799aefd13 | -14.29163 | -60.3866 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a7ef04-08b1-3da9-9eb9-ca680af10afc | -5.75381 | -57.59198 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fe30bd7-f6b4-3db2-b913-66a3beda87a9 | -5.88049 | -57.75796 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 159f0482-b39a-32de-81c6-7ec0cab8d319 | -5.75208 | -57.57928 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2b61154a-23e9-3a0b-b669-b8cb6a89ae32 | -5.79842 | -59.21548 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b68e1e0a-c3fa-3990-9697-5310367a7ab8 | -7.4944 | -63.81721 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c27883c2-31f9-32b5-8b12-c2ef3e2eeef5 | -20.35027 | -51.66995 | 2025-08-24 05:23:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 169.9 |
| d7f3c485-d2ec-306a-90c2-f6604e734c48 | -4.93577 | -55.82077 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43a705fc-07c4-3bda-9a07-4ee1d2357093 | -6.38448 | -62.91155 | 2025-08-24 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a58d7494-e5d2-3cfd-80f4-7edca4ef9972 | -7.31434 | -59.61253 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abb91f85-52ee-39de-b22f-883a1fb1c8dc | -14.28878 | -60.38218 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4198528d-d9ee-38c3-97b4-8a04608bdcf1 | -3.83981 | -55.96381 | 2025-08-24 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d150cbe-933b-3f72-b008-ceb296a247d9 | -5.74964 | -57.59548 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de820cd4-c60a-3d88-999a-f18f5e383bae | -11.697 | -60.19138 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daae04cd-795d-3ff5-9093-40bde002e109 | -7.43759 | -60.63015 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50d53f85-0cda-331e-9b30-c37bf502dcfe | -14.29334 | -60.37521 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2be427a7-1ff4-36dc-96ae-b614a835ae53 | -5.74913 | -57.57467 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc6ca46a-907e-3c6f-a967-dbbeb75a2248 | -7.78519 | -61.56818 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53eb40e4-0744-3742-8f3e-d9cd60518a5f | -14.81472 | -55.97724 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| db5b0ce8-f12a-3035-aa7e-240843096bae | -6.58431 | -59.87521 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 350b6abd-4206-3ab6-a371-c7914b5bfab3 | -5.42102 | -60.16998 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 573e9d11-db8d-34b1-bf1a-e8288019dacc | -14.29505 | -60.38721 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 356bc5fb-4aae-3a09-80e9-ac81e28074c7 | -6.91778 | -62.90932 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e5302ae-7ac8-358d-b368-aab2d9075175 | -5.80513 | -59.21654 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03c808fd-0969-35dd-9bad-6268204221a1 | -22.7988 | -43.68796 | 2025-08-24 05:23:00 | AQUA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 26ebdbac-6d1d-308e-a659-1df7a1484098 | -6.46468 | -53.4015 | 2025-08-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 666df883-b6df-3e7f-8a5d-94fca5bcc9b2 | -7.56048 | -63.86182 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 748e1a68-360b-3da9-bd8c-2c0bcbf1e06b | -10.41939 | -64.43107 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7271fe7b-a85e-3dfb-bcca-a0a793cb0521 | -10.41721 | -64.4223 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.9 |
| a8444de1-b693-328f-bb6e-630b00eff4da | -4.55968 | -55.96618 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29589086-e4e3-3ebf-a371-3f9834a03105 | -7.36223 | -57.6313 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 546011d2-e19d-349f-a459-3677cb0778fa | -12.72411 | -48.14243 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 395eb7a9-295b-3d86-97a4-7b7a9e9b9b60 | -9.49762 | -68.47447 | 2025-08-24 05:23:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2500ef01-7b1e-3ed1-9bca-308d74f20eb3 | -7.54528 | -63.84245 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99a74b0f-ed4a-362f-98a3-ebb97ada82fb | -15.35264 | -53.92059 | 2025-08-24 05:23:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20a81f06-879c-3dcc-b3fc-04031ca81a34 | -6.30786 | -59.88607 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 023e91ab-adab-3ed5-b6e2-90509b1ecd89 | -5.79395 | -59.22206 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88d9698c-8139-31d3-a5fd-a66547567123 | -5.8001 | -59.22667 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a789df32-18d9-3ff2-a8d0-d17e891a535f | -6.31005 | -59.87212 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a387b22-ea9c-3f7b-8d83-93c5d27423bf | -5.42981 | -60.15721 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50fde311-eb76-34a7-abe3-86f0ab36a0dc | -5.42596 | -60.16015 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90af63f1-f6f7-3ec3-b269-964265fa9e66 | -12.7329 | -48.12691 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ddca6ae8-bdf8-32a0-a438-397381ccb7d6 | -13.62315 | -48.16549 | 2025-08-24 05:23:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ced8e0f4-5adb-3f2e-bc54-f0bfc8f9ea03 | -5.74191 | -57.5984 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21f424b5-063c-389a-be17-c9375a63e8ab | -2.63279 | -58.10704 | 2025-08-24 05:23:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b318ca2f-b77c-3f6f-b7c5-5bef6164c40a | -4.94356 | -55.82189 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a59f965-5afb-3021-a6eb-8b0d454c1556 | -4.93894 | -55.82619 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f84094ae-fcda-335f-a586-06111e3bc663 | -7.56367 | -63.85654 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a0bdbc7-404d-31a5-9360-7ae0fe6e7115 | -8.76144 | -49.97501 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe0f14c7-5baa-39ba-92a5-d4fe35af5edc | -5.4304 | -60.17499 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99cb4ec0-11e4-37cb-9234-9fef90719bc8 | -6.62807 | -58.54318 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c88c98fa-d8b1-326f-8957-2d3f4e7fc127 | -5.87928 | -57.76587 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d09b668a-1a5d-3190-a279-e06976c1ef5d | -5.7973 | -59.22259 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc61a647-54f9-39d7-82ae-0bebe6c1322e | -8.76082 | -49.97962 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c33363-bfe2-324b-9aa2-985f46c20c5f | -6.63339 | -60.01881 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f34901da-d8f6-3f7c-a679-82ace4923178 | -12.7248 | -48.13555 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| de2caa3d-5105-318c-ba55-b0b2f38c90e8 | -3.13327 | -58.04121 | 2025-08-24 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13cfe648-30d9-3ebb-a27b-67530de2aaaf | -5.81042 | -59.21719 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 831c6252-074e-3786-9613-e064c52669ac | -12.73617 | -48.12808 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5c65ac02-5239-3369-b971-8c70a0455820 | -5.61125 | -60.23496 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f77a9775-af32-3243-b94d-2aae208a7649 | -7.29873 | -59.62468 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ce72b23-c870-3464-8b38-696bf7cf757d | -6.68881 | -58.85424 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9428be8a-9fb6-342f-a29d-7b0fb1169096 | -5.42927 | -60.16066 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 035dfc45-7573-36b7-a089-496152be1d14 | -7.62502 | -63.48457 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f177aa96-6914-30b5-a889-4643412692d5 | -6.87439 | -59.82371 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3225b603-3ada-324b-ae31-2e6311b923f7 | -7.79625 | -61.58429 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5955da3-f2b5-3674-a19d-bebe877080fb | -7.49797 | -63.8178 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86aae210-325f-3ffb-abba-4a99c9a98fb0 | -5.7532 | -57.59602 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49c806a1-1ee1-3fb6-9755-97c8d35ede59 | -6.68085 | -58.86056 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a076b4fc-0b3b-3d44-ab6b-58ad477dd521 | -3.78743 | -47.56559 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README73.md)
