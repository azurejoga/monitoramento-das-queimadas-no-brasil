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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66f3de84-eb7b-3ed9-84e0-9a7c5cf3dafc | -14.43326 | -51.93997 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62f1d868-88b7-3c06-976f-3ea01fcdb964 | -14.09899 | -53.62561 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 501a0d24-d80a-3753-b327-138428a104df | -14.43814 | -51.94909 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c52023a-e797-3f16-820f-e6671e172fb5 | -14.43101 | -51.85401 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab82a4eb-2b31-35cb-9ef4-a61ca0b1ee87 | -11.50435 | -54.63833 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 728e992a-cf4f-3bc5-b520-dcf6ff2d4489 | -14.13437 | -53.68501 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ba0afbc-efca-3f5f-bba4-1df78e545a13 | -8.96793 | -60.51403 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e72581e-5385-3356-9d66-9800ad44ca0d | -11.11438 | -62.89358 | 2026-08-15 05:36:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c56af616-d0de-3dd0-a0eb-1d8431370872 | -14.43703 | -51.90632 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| fbe0ab2f-6a8c-3e76-b548-4436264c78cc | -14.71544 | -52.88519 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 938e66e4-4f3d-3a50-8f24-976f2868eeb5 | -14.30371 | -53.06816 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06fba8c0-4e9d-3f2e-b878-949bd72d361e | -9.07639 | -61.39569 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5efe3ed-1e59-38eb-a485-2917ef8a020c | -11.50499 | -54.63341 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e162fb7-8512-3903-8b0e-12b028133425 | -14.43309 | -51.88864 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 507d1ca0-6aeb-3230-bd84-86997d7a531c | -8.79292 | -64.03587 | 2026-08-15 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d8f3cff-db6b-38d8-b21f-68e877ba689b | -11.51372 | -54.63951 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23fc180b-7bf8-34b4-a90c-32791a61e7ad | -14.72053 | -52.88947 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d63f24dd-9092-379f-886a-ee42d25a8228 | -10.51807 | -50.16002 | 2026-08-15 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b20c7c3d-8951-3f59-842d-a93b08a3a680 | -8.9852 | -60.53482 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d315a846-8a45-3f96-b509-bc2acdc449bb | -8.98241 | -60.53077 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87d7c58e-cbb0-3178-9ac3-b46f46285f3a | -14.41951 | -51.90411 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf4f5fb7-b6e6-3307-9f5e-2aabfba35ce3 | -10.41164 | -47.97243 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2cf1988e-4a80-3d34-967c-865f2eb9f5db | -12.69473 | -48.45126 | 2026-08-15 05:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 159d2406-13de-3cfa-80b0-e9bececc0c9b | -14.40911 | -51.89698 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2f07419-f448-3fbb-afbd-d8329db952c9 | -13.42539 | -57.05106 | 2026-08-15 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e1cb8d8-1ff6-38de-97f1-e709890dfab8 | -9.4837 | -51.61543 | 2026-08-15 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dba89782-9f16-313e-a5b7-3e63a5c0830b | -14.33515 | -53.30568 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76d56144-ca50-34a6-9691-88fcf93dde89 | -11.58922 | -62.13293 | 2026-08-15 05:36:00 | NPP-375D | NOVO HORIZONTE DO OESTE | RONDÔNIA | Brasil | 1100502 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5849fb3d-5ec8-3244-a344-8f8dd002801a | -14.41904 | -51.90833 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 676c1d12-9df3-3e43-b4be-4050e1e0cb66 | -14.44824 | -51.91198 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9970a70-ec8a-3f1a-a66c-28a9871dcfdb | -12.70115 | -48.45769 | 2026-08-15 05:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42756d32-df97-3bdd-94d1-058d450f6ed5 | -14.44335 | -51.9028 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| a5bf54e3-b44f-3937-84c2-1772968756af | -14.71504 | -52.88634 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f433da02-338a-3086-99bd-3f1f52ae897f | -14.12918 | -53.68443 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c848a35d-f3fb-3e5a-a781-4e5e3b64d3f8 | -9.48416 | -51.61184 | 2026-08-15 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e930303c-ffaf-32f4-ad75-192b142a3b8a | -9.71317 | -69.06749 | 2026-08-15 05:36:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dcce1e2-dedd-38dd-94b7-baa72c313e48 | -13.76123 | -53.43293 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41e0228e-dc77-325f-8188-0228b4876341 | -14.42724 | -51.88792 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51d3c312-f8bb-3ac6-94a4-c8cdec834def | -13.23255 | -54.17379 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b4022db-4c18-369d-8bd1-7fc80b318341 | -8.95517 | -60.53006 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64259ca1-798c-3260-8d51-73b827bd6cf1 | -14.09379 | -53.62504 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6f921cf-7e55-3805-9c49-2f27a84dcf7f | -7.58268 | -61.23422 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c043ec8d-5fb1-36e2-a78b-a3d23ccfc998 | -7.58987 | -61.2318 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b646543-1488-3766-a8d1-10899163ef15 | -12.68787 | -48.44873 | 2026-08-15 05:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b59d5e1b-b0d2-3939-957a-7eadee489c5c | -15.03961 | -52.69061 | 2026-08-15 05:36:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4eaa1d1-175c-3e2d-9604-1bc726dd74df | -14.44383 | -51.89855 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 19f3f39f-0f92-314c-919b-2851df2bb4a0 | -14.13513 | -53.67871 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47f53623-b6c2-33ee-bcf5-5a3460daf01e | -13.28085 | -54.20032 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b23befb9-f463-3f57-b4b1-f21c41e49c4f | -11.50272 | -54.63161 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 339d050b-3c24-3ecb-9ed5-0e020d8ae0f9 | -9.34828 | -62.36242 | 2026-08-15 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb215378-d0c6-3cca-8463-b5d80a3553f2 | -14.09042 | -54.5266 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efdded52-c218-3d78-83b3-479885f92dbc | -8.89776 | -60.55359 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be7af9a4-241f-39f3-8c22-80339328d14c | -14.43279 | -51.94416 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e91ce27c-2b10-3573-a759-51c6382cb55e | -13.26671 | -54.19268 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2de9e015-b4ef-31ef-be78-6abd4460fb3b | -8.96848 | -60.5105 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dcee438-cdc3-3998-a516-c155d9717db3 | -13.27979 | -54.19744 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9038811f-483d-3788-8dff-580bdc042918 | -11.24163 | -54.83768 | 2026-08-15 05:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38bb717f-f1ba-357d-9285-708659fe67d0 | -7.58544 | -61.23823 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e240d0fa-7205-327e-af08-66c3aa57b25d | -10.72351 | -50.56247 | 2026-08-15 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b1f79c39-323a-3544-ac74-44fcf19fdb38 | -14.42535 | -51.90485 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c9a0f287-73ea-330c-a869-e79820871e0e | -14.08174 | -53.67922 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d444d895-8794-3392-902a-023763983237 | -12.06059 | -58.04479 | 2026-08-15 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6630d598-569a-3dc3-bf0f-4f48ea5b4f3f | -11.50741 | -54.63217 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c929bf05-41cf-3d19-9195-add135a03a80 | -7.58655 | -61.23127 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4e84ca9-65df-3cba-81c1-fdf5531b8f2b | -8.60916 | -54.6701 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d8e2b62-51de-3883-9a93-f9799cc25479 | -14.49345 | -52.03194 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a3cc2c-c404-39ff-aa11-7ad55b5d82ac | -8.61362 | -54.67074 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 843a4367-6d64-37b8-8262-40255cc5f805 | -14.72011 | -52.89318 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a00aa86e-3413-3409-9afa-e2c5f650698a | -8.96075 | -60.53817 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98b04383-3521-3e7f-8ab1-08d7d8913e09 | -14.4517 | -51.93375 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1041b306-fe7f-3b0b-9b23-0487c546127d | -9.34886 | -62.35886 | 2026-08-15 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20268044-f063-3f5e-8a69-abdda3e720e8 | -7.59043 | -61.22832 | 2026-08-15 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f397b44-9b23-3574-858f-3c83de5c3c77 | -14.33475 | -53.30901 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 999732d8-b351-32d0-b6a4-07888d8cd19e | -9.97801 | -53.94375 | 2026-08-15 05:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| de3dcca8-797a-3219-9bd9-5c3c8578ed37 | -14.30949 | -53.06571 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4941a42d-ad05-3f0c-8bf4-1ae544e7b957 | -8.95459 | -60.51191 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2fdb52a-991a-308e-b49e-e20ea0007199 | -13.80696 | -53.80024 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2993e59-4c18-3815-81bd-99bb55f3eba1 | -9.4776 | -60.54005 | 2026-08-15 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 328063fd-bdbd-3382-a433-f40a133d54b7 | -9.47814 | -60.53651 | 2026-08-15 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caaa82d0-f2a8-3cf1-9633-70e3e3c71478 | -14.43894 | -51.88934 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9535a7d0-595f-3109-a838-d587098ae9ce | -9.70743 | -69.07187 | 2026-08-15 05:36:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80bc60ad-88c1-3f7f-bec6-85a0d5025408 | -13.2452 | -54.19287 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 516244dd-1889-30c1-aec8-4af3a89bef96 | -14.7265 | -52.88612 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6656f33-dc50-322b-8499-6ab9376bd085 | -14.44776 | -51.91621 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 041e852f-507f-3319-a52b-f9c26aa00c3f | -13.2382 | -54.16887 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38c2044f-e290-3c47-98e7-9f49138b12e9 | -10.41088 | -47.97923 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5fa7f725-a84b-360e-bde9-92f84ce1face | -14.42582 | -51.90063 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 1c901d06-0485-3c78-901b-63efd857cbcf | -8.98464 | -60.53835 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8cd33d0-105d-38b5-8a7b-6cce77778156 | -10.42021 | -47.98209 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8203bc30-3ba7-3f26-87d9-3eaf7d29bde6 | -14.4492 | -51.90351 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b6a19d9-b621-3cd2-97d8-f3543e6d7371 | -8.90054 | -60.55764 | 2026-08-15 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| df58c36e-a5ad-3da1-a51c-43af5b3d3d7e | -10.72408 | -50.55789 | 2026-08-15 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c5384012-b982-32be-871d-21c2856e633c | -11.50673 | -54.63712 | 2026-08-15 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a897949a-2e4e-3d45-89dd-d0d77c7f3ccb | -13.81029 | -53.81531 | 2026-08-15 05:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfec9081-1540-3454-8772-fa2305716634 | -14.45217 | -51.92957 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b8cd268-bbe4-392d-be2f-c4906eb55560 | -10.40685 | -47.97378 | 2026-08-15 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c55d6a2b-da02-3a1b-9c72-36bfd4fd082a | -14.42931 | -51.92242 | 2026-08-15 05:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fae2b44d-9e80-3dca-9670-19c23b6724de | -9.61238 | -63.44591 | 2026-08-15 05:36:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d3db520-afa2-3b65-b1e3-834fee0457f7 | -14.30409 | -53.06494 | 2026-08-15 05:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bacc8db3-5cdf-3c2e-bc26-64d1c7d43203 | -8.65303 | -54.69678 | 2026-08-15 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README43.md)
