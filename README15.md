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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a5d9cf9-880a-369d-9724-0d59b3d50fd8 | -4.1943 | -50.6281 | 2025-11-10 04:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 4798a53a-19fb-3463-b12b-3267b63d3728 | -4.2128 | -50.6273 | 2025-11-10 04:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 254611ab-f0e6-3e51-8976-fc2cabe2350f | -4.2128 | -50.6273 | 2025-11-10 04:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ebf4b09b-f9b5-327f-b6e9-45e43f240ce1 | -4.2128 | -50.6273 | 2025-11-10 05:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c0d72113-ed76-3779-b618-ec63d276845f | -3.28041 | -51.11795 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cbab9227-26fe-3130-bd04-f45737d51493 | -1.76627 | -55.03343 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12d26cf4-a6bf-3690-bb9e-0fca0d50126d | -2.45078 | -49.03022 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 484d7207-5547-3230-ab86-ae9ff5171f7c | -3.1487 | -54.98437 | 2025-11-10 05:08:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b95c3e6a-3141-3dba-ba16-f0afa4b4d0e7 | -2.97231 | -49.82188 | 2025-11-10 05:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed2e0bc3-7dd1-3bcf-a080-28a18ebf67f7 | -1.94315 | -54.57136 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16c50d12-6e56-3839-a63d-45bf443484c0 | -3.33369 | -49.92726 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a63ac557-75d6-3a05-a521-d935bde49d57 | -3.44961 | -50.48027 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 26b83d18-ff53-3d50-bd01-9e579f74b61c | -2.0326 | -56.63639 | 2025-11-10 05:08:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eee0f0f-0fe8-38a1-8575-5d259e7c0509 | -2.26674 | -56.12202 | 2025-11-10 05:08:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5159b679-073f-34b7-a2a2-cd097a7a2679 | -2.87873 | -53.15606 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 481b4502-a7e4-3751-a699-284fb7c5068b | -3.10819 | -50.19909 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bdbf2667-e095-3a30-a7d6-3ec94804e2b1 | -2.64642 | -54.8152 | 2025-11-10 05:08:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e64843eb-f5ac-3b31-bc71-6b64cd6bbb99 | -3.07735 | -49.37907 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc88fbab-8d42-39b4-8370-4a12ca486530 | -3.40989 | -50.2613 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1679b94b-80f4-3eed-9c16-669d89a85fea | -2.6424 | -49.21859 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19634b60-f17b-3f3d-a372-9f3a340a34d6 | -3.26196 | -50.07399 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e27fd50e-d6b8-39bc-b0ef-9201df1e8f06 | -2.32631 | -48.59426 | 2025-11-10 05:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de5c89c7-afe7-31bc-960b-74ee8d135700 | -3.64099 | -51.94169 | 2025-11-10 05:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e52dc21-126b-3297-bdb3-6a53bcc9b9ab | -3.09396 | -50.32174 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd0cb245-7f23-3963-a04e-216d5098dede | -2.19754 | -51.36563 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7888a812-272d-3a53-8f87-50ea4c3336c0 | -3.2869 | -53.82042 | 2025-11-10 05:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28c60db5-d833-325c-ab28-18b5f877e45c | -2.97012 | -49.82322 | 2025-11-10 05:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c1963f6-9f73-303a-aebd-af748360e11c | -3.27882 | -52.96567 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af21e6fd-bee3-3267-a79b-84d5e9653a57 | -3.32391 | -53.36214 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68ec1dd1-a1f2-3943-be67-9c9f55e00fe9 | -1.45479 | -55.50533 | 2025-11-10 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fc075ba-1d72-371e-ada3-1b60d69d5ba5 | 0.9799 | -50.06705 | 2025-11-10 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd6ccd35-84b0-3384-842b-a386bda3300a | -2.467 | -48.79932 | 2025-11-10 05:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 630981fe-df08-3f4d-8c48-823610eb2bc5 | -2.48254 | -48.36929 | 2025-11-10 05:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65553303-c588-390a-b777-0d0d714b004c | -2.97162 | -49.82636 | 2025-11-10 05:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d09f7b1-3e47-3889-bddc-229323f8e4fe | -3.27985 | -51.12165 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aad9b990-d4b9-3000-a90f-8143aba542e8 | -3.69962 | -50.18989 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b7c2fa98-3846-3aed-907d-4b778c511053 | -3.4971 | -50.48762 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c91010a-4374-32e1-a62c-70631b1f200a | -3.14228 | -50.27648 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25a1593c-3c44-32bf-9109-ca6055d4809f | -2.60688 | -49.23299 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a2395ed-f6ad-3dd8-996d-6691ba2f9697 | -2.44311 | -49.22581 | 2025-11-10 05:08:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 710c937b-dda8-30d1-9436-aef4c973b011 | -3.32539 | -49.92144 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd2c962b-e2a5-3f5b-9145-cdd034338813 | -3.46289 | -50.03021 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5894ab82-fd7f-3e7e-843a-25e429261b0f | 1.26146 | -51.26914 | 2025-11-10 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d24a4e2d-d6f8-3bcc-8ed0-204656d574f9 | -3.15043 | -50.6045 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0b1c62a-d221-38c4-b77f-cd027f7a0db0 | -2.12165 | -52.28457 | 2025-11-10 05:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a67eae5-0c9e-392d-ac78-96dab704ac19 | -2.29464 | -47.8725 | 2025-11-10 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3586ddeb-3216-307e-897c-d6e17c1c2535 | -1.79396 | -48.06884 | 2025-11-10 05:08:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98fd26fe-c57a-3d65-8b1b-a279c412ef8f | -2.9729 | -47.89684 | 2025-11-10 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60009c9a-e821-30b8-ae32-a4380e187701 | -3.85883 | -50.18151 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d020637-8844-393d-a5b4-f56e9450e35c | -2.99027 | -52.8204 | 2025-11-10 05:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3071d390-998f-3745-927e-ad9df0f7ce02 | -3.89748 | -43.44509 | 2025-11-10 05:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3effd2cc-072b-3a8e-908d-f71199486f42 | 0.97576 | -50.06769 | 2025-11-10 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54922acc-54a4-3cf4-a67f-7a1aa216c0cc | -3.53658 | -50.85626 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ade83dc-c505-3571-816b-7fdd3e88779a | -2.24678 | -48.37014 | 2025-11-10 05:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d7d5205-0fc3-3e76-b144-ff2848e96022 | -3.58233 | -50.28419 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ad065ff-f645-3b52-9002-a1c8af671350 | -1.76736 | -55.02639 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2def4960-efe9-3fb9-9590-55cb2985dcc5 | -3.47459 | -48.97837 | 2025-11-10 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4d82018e-b1a6-3fcf-a05b-8e15c89b4efb | -2.64138 | -49.2158 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d13b292-0ce4-3676-9581-4a8f88da2bfb | -2.34307 | -47.03217 | 2025-11-10 05:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca36af7-1994-39b2-894b-356c10bf2ee2 | -2.46756 | -56.10062 | 2025-11-10 05:08:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eb9b744-5313-34bf-88ae-f68d6647683b | -2.62922 | -49.2114 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01cc8852-7366-36c8-9be9-88ecdd95c73a | -1.79439 | -48.06599 | 2025-11-10 05:08:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0583cf-a0f0-352c-bf38-e536ab07f363 | -1.63025 | -53.68539 | 2025-11-10 05:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0992900-12f9-3ade-9258-cfb8569a3323 | -1.76682 | -55.02991 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb2814aa-4c49-3d22-9537-5b362575508d | -3.6952 | -50.18921 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 328bb2c1-4fbe-390b-a94f-2e059d6e1534 | -3.0983 | -50.32239 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbc37ed0-e438-3449-8e7b-bfc6a920beeb | -2.4771 | -55.73232 | 2025-11-10 05:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27288b63-4b40-3b06-869c-811e3fc373b9 | -3.34603 | -50.20784 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 453c28f2-2e4f-3f45-930f-f13258548738 | -2.60761 | -49.22815 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed949283-9f53-315c-9939-bf54590816ef | -1.34012 | -54.60551 | 2025-11-10 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e6159b1-01d5-35f6-9e2b-dc51e42ec279 | -3.33428 | -53.2444 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1c5c950-20b9-3b75-a324-57d1b6880b28 | -3.22845 | -48.79162 | 2025-11-10 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad58b094-1d3c-37c9-815c-594127951a33 | -2.98657 | -52.81983 | 2025-11-10 05:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d033653a-42c7-3541-8e61-51f0c698c468 | -3.49648 | -50.49171 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 959aba73-681d-3fbe-9890-54e09abb50d7 | -3.10882 | -50.19491 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 17ecd7e4-5e46-30cd-8f18-5eb298af0b11 | -3.26699 | -50.04586 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afdfa462-422e-31bf-a875-236ad4d2d8d0 | -3.14814 | -54.98797 | 2025-11-10 05:08:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5359bc93-11ab-3d63-9b30-ee125432e0c8 | -3.09392 | -49.26717 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0710734f-6e11-3d62-b058-7268b3ef9d97 | -1.67774 | -53.72429 | 2025-11-10 05:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b217631-e751-3c71-9dad-5a3368c2ed23 | -3.32987 | -49.92214 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff38f015-0559-3495-b9c9-d8548dc9c10e | -3.22442 | -48.78556 | 2025-11-10 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe66d125-46df-3c9d-8ae6-5174788ead18 | -2.60223 | -49.23226 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b37269e5-cb0f-3b55-8ee2-1f6e472eb791 | -3.3129 | -50.15707 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd4fa8b9-5d34-3e8f-a56a-d56d18aca769 | -2.29628 | -47.87266 | 2025-11-10 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3d9b449-2230-3505-8fdf-fd280077897f | -3.33387 | -49.89526 | 2025-11-10 05:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19d8800e-833d-3953-9f8e-88b7d85fa788 | -3.47536 | -48.97315 | 2025-11-10 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c4e2623f-8067-34d6-81cb-6da5cc2ea02c | -1.97013 | -54.41908 | 2025-11-10 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea4b1d26-1028-3a24-a10d-3d00e40c568a | -2.62815 | -49.2086 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7aa14c18-9db3-32ea-9e36-b16c7546a4c5 | 0.71987 | -51.47343 | 2025-11-10 05:08:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3c40aa8-1930-32ef-b72d-dd51d570e190 | -2.62743 | -49.2135 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 564fd2db-9e7e-3189-89d5-f311b89b5990 | -2.60836 | -49.22329 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 027f208b-504a-35d4-9555-f57f6a972a68 | -2.60371 | -49.22256 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 781ee819-416d-3729-91e5-1ca627fc9a13 | -3.25691 | -50.07761 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f536f6ed-5021-3d17-9d59-dc881829dd62 | -3.09894 | -50.31823 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a9a382f-173d-3afa-bd33-86d126e9ab35 | -1.25551 | -53.33966 | 2025-11-10 05:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a3be6cb-dd37-35b5-82b3-2474394f6acc | -3.22361 | -48.79088 | 2025-11-10 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1fd0faa4-bb96-3363-bec9-704af93e580f | -2.19859 | -48.24286 | 2025-11-10 05:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3e1146c-9218-3c80-b79f-f8d703ea3fb1 | -2.1444 | -51.1348 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c14342ed-2ee6-32f4-a340-dda7064d44ea | -3.06064 | -50.21759 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fb7acf9-85aa-3ebf-bca1-67fee9489667 | -2.84672 | -54.08496 | 2025-11-10 05:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README16.md)
