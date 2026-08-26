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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65ad2b06-a68f-3339-b8f8-f5b1fecafe6a | -9.1896 | -50.0032 | 2026-08-26 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 0a6055f6-c2e4-3b16-b260-220dceb5e390 | -11.7354 | -54.5431 | 2026-08-26 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 124.9 |
| e2d07c04-8e0e-3962-ab4c-aa519e35f87e | -8.167 | -47.5201 | 2026-08-26 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| a74fa73e-6b95-3589-8d1a-6677dcc29008 | -6.7648 | -59.4408 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 0bea7384-e732-3f5d-b1f1-dc9e88eef466 | -11.7733 | -54.5396 | 2026-08-26 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 196.9 |
| 5c4b6207-e467-36d6-b3b3-de08fc26920f | -11.3702 | -50.6993 | 2026-08-26 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 282.6 |
| 135fbb69-c6dc-35de-bfeb-df0c138d4272 | -6.695 | -58.7291 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 44c653d1-8392-3a09-ae41-fb561752eaa4 | -6.8008 | -59.5934 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2d41e0f0-e2cc-3974-8cc2-1cd85948ade8 | -9.1896 | -50.0032 | 2026-08-26 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 993b4831-1d06-3e0f-87a6-98bceac41245 | -6.7834 | -59.4016 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| bf1e7825-2819-363f-b8cd-e80a85629da6 | -6.6952 | -58.7097 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7cad49a6-af56-3a0f-93ca-9860b0fee2ec | -13.6044 | -51.8182 | 2026-08-26 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 190.3 |
| ca211ad4-c334-323d-8b1d-95049a2e5db5 | -6.4232 | -54.9632 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 159dce73-e1dd-3143-9db4-93a2abb28232 | -9.1315 | -57.5703 | 2026-08-26 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 894e44d4-b713-31c7-b96f-b53d81b14005 | -13.2095 | -51.3356 | 2026-08-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.3 |
| c10eb1d7-27b1-3aae-b858-3cb516be3548 | -11.1561 | -54.0028 | 2026-08-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e5f43396-9cf8-33bb-aa80-27ae13e030b2 | -6.7833 | -59.4208 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8814f9a3-aa2f-38a9-89b5-989bff3dc2f3 | -5.9196 | -43.6497 | 2026-08-26 15:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 10dfb53d-1963-30c1-8809-4e1ff95686d5 | -10.7793 | -50.975 | 2026-08-26 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 91d572d6-8704-3622-9579-dc21869668f9 | -4.8002 | -43.1709 | 2026-08-26 15:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 6819019c-56ac-346a-b26b-2b421b3ee954 | -6.7691 | -58.6873 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| be793c9a-ef38-30f8-aa9b-e0ca71e9ae75 | -10.95 | -49.5877 | 2026-08-26 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 1d2e6320-1334-3af0-9997-2afc4cc523f4 | -10.779 | -50.9962 | 2026-08-26 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| fc0c1312-994a-332f-a737-b3f5381373fb | -13.2092 | -51.3569 | 2026-08-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 71958ce2-2756-347f-9e5d-a25dd9ad8f7e | -9.406 | -60.5711 | 2026-08-26 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| c263d4b6-c006-3728-af8a-5a8a32e0dd37 | -13.5851 | -51.8206 | 2026-08-26 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 453cd660-b477-3c8b-adcc-dc06e259ac37 | -6.583 | -58.9658 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a5ab36bb-c112-3793-97dd-b950e876f1a3 | -6.8246 | -58.6655 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 5ab048f4-3297-3e8e-a245-998ad60a5e54 | -8.6161 | -54.7137 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1c939214-bbef-38ed-9e9e-c199b6078f92 | -10.9664 | -51.1251 | 2026-08-26 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 066fd797-2346-3cb9-9944-23d1104704be | -6.8019 | -59.4008 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 212ae334-7e4c-3841-a7c7-26b2552043d6 | -7.0058 | -59.2382 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 76f81d0b-a4d8-33de-8fe6-88298171c551 | -6.5138 | -55.2387 | 2026-08-26 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2d599d80-77ea-33eb-8bca-af4cd8b6dd76 | -9.9708 | -53.9419 | 2026-08-26 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 6a1ab14c-581a-3d00-b286-57af2b9b7062 | -8.9421 | -45.7253 | 2026-08-26 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| d92dc8b5-9a14-317a-9b5a-41cb1eb2a3c7 | -9.6022 | -55.128 | 2026-08-26 15:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 5b2701ad-38e1-3e1a-aed0-22bc73a809e2 | -7.0815 | -42.1824 | 2026-08-26 15:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| eb5c8a83-2e68-38dc-9915-c3b09fc1e1a8 | -9.659 | -55.0632 | 2026-08-26 15:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f6861df8-f184-3a37-bc50-8b141e3b211a | -11.3705 | -50.6779 | 2026-08-26 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3785593d-772c-33aa-b2ed-570043c52e9f | -14.3179 | -51.726 | 2026-08-26 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c07da95d-6542-393e-9f46-45099db1d55c | -12.1417 | -43.3945 | 2026-08-26 15:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 3acbdc64-8b7b-376b-af03-ce700cfcc17f | -8.5962 | -54.8563 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8c3a245f-5e76-35bb-95ab-8bd491b12a51 | -6.5093 | -53.2619 | 2026-08-26 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 783b4b69-4c12-3acc-aa62-8e4abfe899d5 | -7.6649 | -47.1242 | 2026-08-26 15:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 78b36ffa-f380-3214-bb07-6593f1a0838b | -6.1477 | -57.702 | 2026-08-26 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 1fe4292a-da2c-32c0-b5f2-6904de63a915 | -8.5975 | -54.715 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6518664a-5d55-3b85-af3a-14f3613f8640 | -9.6024 | -55.1078 | 2026-08-26 15:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 363.7 |
| 048943e4-8710-331d-a78a-1f6ae64c8892 | -8.5365 | -55.2826 | 2026-08-26 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 23602c7b-4be0-3d0e-833b-cddd48540561 | -6.6233 | -58.383 | 2026-08-26 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ccc015a4-9162-3f4f-a364-d683402721b4 | -3.2178 | -61.2551 | 2026-08-26 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 232.5 |
| f45d9b0e-726a-3c9c-b4b5-c203e4b7f11f | -8.5173 | -55.3441 | 2026-08-26 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d75abf34-7e4c-3faa-b5a5-0e1598a51a45 | -6.7815 | -59.748 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| dad5b5c4-6ad5-3289-983b-1ea2b4c55ccb | -6.1176 | -59.9261 | 2026-08-26 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a94af203-3b4f-399c-9887-d153990b77c8 | -6.6227 | -58.4801 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 68945f4c-daee-322b-be81-d1e25ba95b8c | -8.7584 | -49.9566 | 2026-08-26 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 178.8 |
| 9bf5b6cd-81cf-3b00-946f-4ca7574cb043 | -6.8247 | -58.6461 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 4874c07a-9fb8-3115-b54a-690534901981 | -7.1536 | -51.6584 | 2026-08-26 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1319c29e-d440-325a-b7e3-e0937fcb9e26 | -6.8061 | -58.6663 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| fd130826-68df-32a8-9e6c-294de6e605b5 | -6.7661 | -45.2551 | 2026-08-26 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 50024cad-430d-3ef9-a422-5ca2f5f9a942 | -3.2178 | -61.2362 | 2026-08-26 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 457.6 |
| 652a211f-6bc5-3a6a-9695-ecef46b5028f | -8.6415 | -50.3495 | 2026-08-26 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 14c553e7-06d8-3215-8e30-e54c49bdbef8 | -10.7982 | -50.973 | 2026-08-26 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 60cea98d-8c9d-3efc-b75a-97fce204bfdf | -3.1266 | -61.2188 | 2026-08-26 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8cd4b1c1-37fb-30e3-b7b6-d88576128576 | -7.3663 | -55.1734 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fe1d39ba-324c-357c-9e06-e71e2d9ee904 | -6.235 | -55.4715 | 2026-08-26 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e7c42f98-ce09-346a-b59e-c90e6d525ef2 | -15.7878 | -56.452 | 2026-08-26 15:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9308feb5-5eb8-3a2c-8515-c238be4fb17c | -8.7769 | -49.9763 | 2026-08-26 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 252.3 |
| 861de029-2f13-3e86-aba0-220d5d79e45e | -13.3402 | -48.2079 | 2026-08-26 15:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 307c4868-797d-387e-8225-c4ef660fd3ac | -8.1669 | -54.9648 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 7b0379f1-e4ae-31dc-819f-4bfcdd60fb45 | -10.5596 | -50.4449 | 2026-08-26 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 151c3361-d53d-3cf9-9bf6-33ff225db46c | -7.6461 | -47.1258 | 2026-08-26 15:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 449.1 |
| f0223a82-6fe7-35dc-b01c-7c7dd301b5f0 | -6.7296 | -59.1337 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a72abed8-4d46-35f1-a145-934b97efe083 | -3.2179 | -61.2174 | 2026-08-26 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| e98c9c62-13ff-352a-baf3-849ce471f2ce | -6.0807 | -59.9465 | 2026-08-26 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7554a53f-9d31-3e5f-af80-30d76bcf1767 | -8.5177 | -55.3039 | 2026-08-26 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| eeec7b9d-4bc3-365e-bafd-f570ff52641a | -9.7249 | -49.3296 | 2026-08-26 15:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| d93a643f-216e-3bed-9342-ff55f246302d | -13.2479 | -51.3308 | 2026-08-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 535.4 |
| 875a1a03-5842-369c-967f-2c4c265f8fa9 | -8.8187 | -49.6093 | 2026-08-26 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 280.8 |
| c3f015da-f34c-39db-b9d5-efb0d7768a39 | -6.8192 | -59.5927 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 70a367c6-cb70-3899-a67d-db7ba8e3b84b | -13.2476 | -51.3521 | 2026-08-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 255.8 |
| f572da50-4e37-36c2-b4ad-8931cf8b5066 | -6.8062 | -58.6469 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 07bcc365-2011-3d3f-ae7d-d0609613b214 | -6.1107 | -57.723 | 2026-08-26 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 446fb202-89c9-31f2-8072-aa99f230bd84 | -11.7546 | -54.5209 | 2026-08-26 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 623.7 |
| ec94dca2-4b8d-3be2-aeb9-30480b6c6c17 | -7.4036 | -55.1513 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a9b783a6-c4c5-3fff-8fed-250939d6e92b | -11.7357 | -54.5227 | 2026-08-26 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 218.4 |
| c2edc813-314b-3bf1-8862-31b91daf5fd5 | -11.6025 | -46.7542 | 2026-08-26 15:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 7c58172b-a7a7-36f9-9425-e7aeb0ef0e6b | -13.2287 | -51.3332 | 2026-08-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 219.5 |
| 2d40833e-b179-3cec-8d44-5133724d4d38 | -6.5829 | -58.9851 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 65e68450-3c44-3ac9-8008-35c9d13a706a | -5.6035 | -45.5465 | 2026-08-26 15:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| e52d0786-5b31-3f35-b933-0e4dddb0b3eb | -7.1309 | -42.7945 | 2026-08-26 15:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| de62ebc4-2b8f-3e8d-90a5-9d91f500ec71 | -7.5015 | -44.9397 | 2026-08-26 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 065cdb6d-4aba-3c9a-8a88-fcdaeaf8d33e | -11.7544 | -54.5414 | 2026-08-26 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 416.7 |
| 69b14e37-89c3-3ab5-a93d-76dc2433ca25 | -8.1667 | -54.985 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| da1a761c-a87e-3ca1-822f-edc00091f008 | -9.1899 | -49.9818 | 2026-08-26 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 6a8f2642-687e-3254-a0c7-50144e841705 | -10.3145 | -50.4061 | 2026-08-26 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| dc0be8d5-79d5-3aaf-9d01-96eca71a8284 | -7.52 | -44.9608 | 2026-08-26 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 535a5e8a-681f-3f09-aa33-ac903dbf7bcb | -9.1711 | -49.9835 | 2026-08-26 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 2507980e-1e51-3343-918a-0679fd9633fe | -6.676 | -58.8267 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ee68ac98-76df-38be-a878-915821ebf600 | -8.7582 | -49.978 | 2026-08-26 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 239.9 |
| f4d943e2-5c15-3ed2-815f-b862c46a67f5 | -11.1939 | -53.9993 | 2026-08-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 361.7 |


[Clique aqui para ver as próximas entradas](README91.md)
