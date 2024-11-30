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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 964d8352-0779-381a-a200-94bf243630a7 | -3.0943 | -54.29406 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 05d72c20-bfb2-3d1e-8dbb-b3f52421a70e | -2.65671 | -54.08964 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 857f0fa0-c254-391a-99a0-8daeb6c0cf80 | -3.7078 | -47.14205 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00a52ae4-ce08-34ac-94e9-2bf66d1cba59 | -1.04426 | -53.36261 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c311779-7721-3ce1-8100-dcc987cfb712 | -1.00268 | -51.72095 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fd3c2a5-56de-3d99-8492-379a5b24a7c1 | -2.40975 | -53.82562 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f51c0615-79ca-3d84-9ba3-bd4b9ebbc6b2 | -2.60601 | -54.28148 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0334d5d-0268-37db-a911-353a3ba8d200 | -4.02538 | -54.6345 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f2e23a6-1a90-3b91-b820-feb4ef39433e | 0.58791 | -50.80339 | 2024-11-30 05:01:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f1746cc-3d90-3ef3-91e7-b140768de6a2 | -2.61482 | -51.80594 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c4e076c-f9cc-3e7a-b6dc-42e88702f2a7 | -3.94872 | -49.95374 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18f0eddd-1173-384f-a66f-df83214c84cd | -1.17577 | -51.95301 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6455d0c7-18e9-32cd-8121-5d1003e2ce79 | -1.43283 | -55.24088 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b967926-d290-3ee6-a288-b95870aafe58 | -0.81907 | -51.60466 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e64f24d2-3fe2-3dd0-b8a3-03d70ce94265 | -3.73628 | -53.73495 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25869f53-6d83-3c8f-9d76-dd579abaff41 | -4.07213 | -46.82285 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f5d7cd3-a595-34ab-85d2-eac8b03c66c2 | -3.08065 | -53.30624 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 494cdebe-2c36-3e0d-ad8d-6f38788c8a1b | -0.19503 | -51.53935 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c9bb8e8-7540-32d9-908f-7811d89251f4 | -2.52654 | -54.25154 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff45a8fa-e04d-3b03-b95f-3aaaaae4b106 | -1.63342 | -54.35675 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cd9025b-fd73-3271-b026-af9ee5a27eb3 | -3.1242 | -53.27121 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48a90f05-00fb-3fbf-9f28-3b246c12861e | -3.61549 | -49.97133 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9edf9edf-80b6-34b5-9be2-e6b9afc05297 | -1.14655 | -53.70593 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70e8db2d-dda5-312f-98dd-06ce09aa979b | -2.8603 | -53.93153 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 420ece19-be4e-343f-bb97-2cf9ad98a14f | -3.21259 | -53.37841 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 569eb1a5-49e9-3673-a2bc-539772e3725c | -7.9169 | -61.54853 | 2024-11-30 05:03:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66c77d1a-e103-3d0d-bab4-c810985fa8c7 | -6.53641 | -55.05746 | 2024-11-30 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 978a1cef-55e5-383b-b269-fd56a9c31fcd | -6.26283 | -44.96661 | 2024-11-30 05:03:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fa6a1392-7cf1-3bf6-af9d-4673354f2467 | -3.792 | -58.97661 | 2024-11-30 05:03:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf7c25e6-8d36-34da-b723-08e77e1dab82 | -6.29053 | -44.75843 | 2024-11-30 05:03:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6724bb1-fa29-376c-8f55-c5d22d616f99 | -3.79649 | -58.97271 | 2024-11-30 05:03:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7db12261-9e4e-371f-b12d-577fa62bc804 | -6.2128 | -44.50328 | 2024-11-30 05:03:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b706ab1a-2e93-3853-9ee6-a677bca51375 | -9.2007 | -63.6139 | 2024-11-30 05:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 371a89aa-937d-3947-9225-f77599f5f609 | -10.87888 | -54.31878 | 2024-11-30 05:03:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d63ea09e-dd7c-3f13-9315-f292b8158a38 | -9.37896 | -63.58103 | 2024-11-30 05:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 040f843c-f880-3b9b-aa11-1a98cab6d2e5 | -3.79576 | -58.97721 | 2024-11-30 05:03:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9413afe4-b6fd-36ee-a5c0-0dc8635a89f0 | -6.70572 | -47.26859 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3bfacbc-9653-3356-8296-b5c37fc14853 | -5.18861 | -60.26225 | 2024-11-30 05:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10d952e6-72c3-3ddc-99cd-8e846f00ac91 | -5.74618 | -46.17942 | 2024-11-30 05:03:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79817a1c-ef98-3b22-9f93-3205296432e2 | -7.8954 | -63.26191 | 2024-11-30 05:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4898a74-0fc5-3a7f-a3f7-77595d487ede | -6.13935 | -43.948 | 2024-11-30 05:03:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7f30647-2b41-3d7c-9f32-f0f45b5333a7 | -9.36251 | -58.23943 | 2024-11-30 05:03:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32946de9-6b03-3a5d-b78a-64401604ced0 | -8.37932 | -44.47775 | 2024-11-30 05:03:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03e48d97-4f05-3805-b1a9-237cbb1a9bd9 | -9.18265 | -49.5014 | 2024-11-30 05:03:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab6c0911-4e88-3c78-b4ec-217386d0cd16 | -4.45878 | -56.18018 | 2024-11-30 05:03:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dfc857f-8b7e-3b03-83ca-a1b66aaba89b | -9.15333 | -62.71416 | 2024-11-30 05:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac0de1af-561a-303d-84dd-cc6eb8ad019e | -6.13861 | -43.9535 | 2024-11-30 05:03:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1503d7b3-909c-3e81-bf5f-1e6009358a07 | -9.20175 | -63.61706 | 2024-11-30 05:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7f9b94f-66af-3ae9-b359-8af8a8489709 | -6.26017 | -44.96919 | 2024-11-30 05:03:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 66336ba7-13fc-31bc-988f-284ea2ebf452 | -9.36191 | -58.24317 | 2024-11-30 05:03:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51224270-364e-3994-945a-3292b40aabe1 | -3.51657 | -62.84531 | 2024-11-30 05:03:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e7aa7a3-4073-34aa-985f-228c3ef335a6 | -6.53695 | -55.05397 | 2024-11-30 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 941d6abe-f241-39e9-bb5a-a74dc3b92b62 | -6.41435 | -52.43428 | 2024-11-30 05:03:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80dbae1b-a463-30a9-b43e-4fa18d5beb36 | -7.98034 | -55.30395 | 2024-11-30 05:03:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 114a38cc-c144-3c7a-83af-090d8da29d8e | -9.04206 | -50.00938 | 2024-11-30 05:03:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e1924e8-4cd3-3c9e-9b4e-64ef46859c36 | -8.82444 | -49.69294 | 2024-11-30 05:03:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25597127-e3a0-3d7d-af92-2d1ca16b1633 | -9.57834 | -62.65503 | 2024-11-30 05:03:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5870df9d-2e4b-3d63-9ffb-5b62ebb07c05 | -7.8621 | -45.92446 | 2024-11-30 05:03:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 969b9a09-b287-3c03-b9e0-daf9d0393fe2 | -5.18462 | -60.26159 | 2024-11-30 05:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07aa4fe9-08b8-35c9-bdb6-61a581c3b9cd | -3.51834 | -62.84663 | 2024-11-30 05:03:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ac29294-ef34-395c-b0ba-e8bcb0ed9067 | -9.37983 | -63.57615 | 2024-11-30 05:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 255add24-9b63-3abc-8be4-8b3ce428e74d | -6.70311 | -47.26536 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2c14299-13e6-37f1-8615-9b849340b25d | -6.70059 | -47.26775 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4c630ff-71c8-3c77-b89f-f5383436a0bf | -6.70616 | -47.26553 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 993ef87b-937b-3b31-bfbe-042eec24f206 | -11.41367 | -45.09797 | 2024-11-30 05:03:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f740887b-fd41-390a-9819-192075ed689d | -6.28993 | -44.763 | 2024-11-30 05:03:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5318150f-f100-3dd7-b9e7-152852e5f0f6 | -6.22921 | -47.28346 | 2024-11-30 05:03:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bfa7535-912e-3abd-bec5-3214abe731ca | -8.38628 | -44.47358 | 2024-11-30 05:03:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7abfcb6f-e993-3b05-9cb1-7303e51d0009 | -11.4107 | -45.09717 | 2024-11-30 05:03:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d744ad90-5ec3-3796-95ee-53f5ab06dfae | -6.70824 | -47.26622 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7176b8d5-ee61-3dde-9d8c-b0a04f32b712 | -6.25422 | -44.96831 | 2024-11-30 05:03:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be1f7990-1b50-313d-aebe-fbc68d3898a4 | -6.0063 | -57.84 | 2024-11-30 05:03:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa0abb7a-d791-34ca-b1a7-6008aa46c74b | -6.07575 | -48.04443 | 2024-11-30 05:03:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 132efe7c-3e3c-3fb3-a467-55a6627754be | -5.51139 | -46.25387 | 2024-11-30 05:03:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fc74dcb-85a8-3666-916e-33a773a9177f | -6.25628 | -44.97024 | 2024-11-30 05:03:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4d6ea3b8-426c-39ae-a3ac-e3f81eaaa787 | -9.04647 | -50.00998 | 2024-11-30 05:03:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fff829aa-9492-342a-8392-47f82b61e9db | -7.98423 | -55.30095 | 2024-11-30 05:03:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef31b5f7-04d4-3d01-9e2d-e88d4d75e9cf | -7.09048 | -59.78633 | 2024-11-30 05:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b10fea4-c39d-3fb5-a713-9301755ee35b | -6.0854 | -48.04593 | 2024-11-30 05:03:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 321fb885-c270-34f2-b5e5-e1f2b74443a4 | -3.78824 | -58.976 | 2024-11-30 05:03:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5ca4abd-cd74-38a2-aca3-796777f3fc26 | -6.08058 | -48.04515 | 2024-11-30 05:03:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5d552cd-f695-3dbb-8dd3-ab55808a3cf6 | -6.00692 | -57.83621 | 2024-11-30 05:03:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 420a0d1a-cdbc-3ba6-a852-ac18895bb5d5 | -11.41641 | -45.10302 | 2024-11-30 05:03:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd6a62f8-7ae8-379a-bf65-6e2bfbc90850 | -6.70782 | -47.26928 | 2024-11-30 05:03:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36bd55a9-1112-314f-a18d-8f3a05789d9f | -4.23672 | -57.59862 | 2024-11-30 05:03:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d69cbc38-b6b0-338b-95ee-22ee91109907 | -9.15191 | -63.24599 | 2024-11-30 05:03:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49ba5af4-1254-3f84-be84-bc46e28a8e0c | -7.89453 | -63.26681 | 2024-11-30 05:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d87ec4e8-25a2-3f66-a02a-e6d7fb66cf0f | -10.2256 | -59.08501 | 2024-11-30 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0c93750-8245-3aa9-8ee9-e61aa21a7fe8 | -8.14147 | -54.85177 | 2024-11-30 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05bde461-b20a-30ed-a97e-7b17a0ec4d18 | -3.79273 | -58.9721 | 2024-11-30 05:03:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 214ee1bf-d339-387b-96a7-18ec5f635a91 | -9.20267 | -63.61204 | 2024-11-30 05:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0456db6-ce85-3f0f-8922-c6e083962071 | -3.52623 | -62.77101 | 2024-11-30 05:03:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e315ed7-64a4-3de1-a109-4665eb7e2797 | -6.12401 | -44.92038 | 2024-11-30 05:03:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f0bf92c-ae2f-36c2-b85a-d16b3bbc79f7 | -6.41372 | -52.43851 | 2024-11-30 05:03:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4e4d929-786c-3f5d-8209-21cc16dd694f | -5.65774 | -51.46988 | 2024-11-30 05:03:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb12ff61-5ea6-3ae5-9eca-c3a30d2e8b45 | -3.79128 | -58.98113 | 2024-11-30 05:03:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 141f661d-9cdf-35ea-a5d2-934c79cafe70 | -10.2221 | -59.08439 | 2024-11-30 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ee06173-699a-3b3c-b0fd-92d09654805c | -6.53307 | -55.05694 | 2024-11-30 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8da912f7-ed86-3d33-946c-3a36dc9ff142 | -6.22413 | -47.28262 | 2024-11-30 05:03:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9687d903-a81f-387b-bd8b-8d260a87e8b5 | -3.52788 | -62.77563 | 2024-11-30 05:03:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README118.md)
