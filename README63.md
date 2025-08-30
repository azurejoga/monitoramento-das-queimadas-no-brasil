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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d68023a3-16b5-3dcd-9e76-a6cc8c930c59 | -9.44661 | -62.32065 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9b0c76c-2acd-3fe6-abe9-deba6ebac1ec | -9.4641 | -62.3334 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 16ef6d3c-bc52-3a9d-a76b-4146bfba6659 | -9.21956 | -60.80795 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58bd1b40-47db-3aae-a440-442f6aa7ec4f | -11.92301 | -46.69435 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e39abcae-4869-3e5a-95a8-8361cd20846e | -9.51338 | -54.44048 | 2025-08-30 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6d9cb67-1e0a-37e6-8027-01783df03a52 | -11.14358 | -47.15637 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a8196ef-63e8-335d-80a5-8c972f43fd3a | -11.8709 | -46.39221 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 171da73a-9d66-35cb-b0ba-37078421612a | -10.07534 | -58.36108 | 2025-08-30 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2713de60-a1a1-34c9-b444-f31fb7c52df0 | -5.99783 | -57.85468 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eee78586-2589-37a5-81a3-f7445c8dc4fd | -9.45267 | -62.33134 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| cbcbda4b-b48b-3844-964a-f0b3057a5e81 | -9.70917 | -61.30929 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b7503e5-3a16-316a-b6ac-ff4edb499361 | -9.17514 | -65.55699 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aadbdeda-e38d-3cd4-8d5b-2e5b4f8152f7 | -8.24955 | -61.45174 | 2025-08-30 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 497a485e-337d-353d-875a-7661fed3ebb9 | -8.55055 | -63.02654 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee65707c-b906-31bf-bd3a-4abd2b1d9a14 | -8.88024 | -60.7328 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 198eff55-eb09-3834-9af0-4cc637f3182f | -9.29708 | -56.81707 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6f972c5-09e5-396d-a708-0fe2468cfa48 | -8.55458 | -63.02726 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1a12ed2c-6bb5-3153-8106-a810da40ae8b | -9.45113 | -60.57212 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 867e4edd-87d0-3919-922a-1dea344ea0ce | -11.89199 | -46.72169 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c759ac0-c1bc-3c17-b1e4-f2e28053aa2a | -9.25493 | -65.85442 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b512c3f-92df-3318-9d4a-51fdcf283f7b | -5.82162 | -46.36381 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| de5c8fdb-0928-3c2f-aa35-92a4404cf0f7 | -11.87919 | -46.37405 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dd347fb-5427-3b04-acd3-3cdad0c42ecc | -9.45285 | -60.54032 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 82bc1026-9614-31dd-b12f-4400bbae2b39 | -10.02651 | -48.06136 | 2025-08-30 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3dcd373-a168-3cb7-837d-a1e0d7ad1787 | -9.58532 | -54.48158 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4d306c3-167b-3f9e-9ecc-9cf569e9f266 | -8.55923 | -63.02438 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 26c957ad-d3cd-3370-8e0c-72c790819093 | -9.44612 | -60.55918 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f67f7478-7dcc-39c5-aaad-96ecd18f0371 | -11.0676 | -52.05069 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3942a9a7-3229-3233-bfde-17a5b513986f | -9.4525 | -62.3558 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eafe2c26-122c-3641-bbbf-985d503d7118 | -8.95353 | -65.96289 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a5f7da5-1fad-3557-8a8c-77b3f3e6bf48 | -10.49302 | -51.62724 | 2025-08-30 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 38a8c99f-a1c8-3161-9bf9-10ef2719c8ed | -11.89004 | -46.39355 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc8c2f83-8ec1-3226-a84c-d10dd9312f5a | -11.07262 | -52.04679 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c45014e-d86c-3bde-84f0-002eee564e67 | -9.11665 | -65.7719 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffea30a5-e3f1-3841-b3b2-ccf39ae03ace | -9.44547 | -60.56308 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f4fd9750-df30-35e4-8af5-9ffce70b4fcf | -8.18093 | -61.36974 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0a1ca8a-9b68-3dfe-90b8-f8a1daa8e671 | -9.20655 | -59.54209 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4db9354f-d57c-337d-b526-1ffbb6527b2d | -9.19449 | -61.02449 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa458d84-891f-3e86-91aa-286aca27b5a4 | -9.15045 | -59.55902 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 90b707f3-45ce-3a29-ad74-370470bfa857 | -9.44505 | -60.5355 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a0647f3-827f-3919-be92-25896e7c0851 | -8.90446 | -62.10378 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7fbfdb2c-448b-3c43-9fa8-a353ae1efa63 | -9.44252 | -60.55107 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4a9a4fd7-bf5b-3a80-bea0-5d0ae42e2970 | -9.11759 | -65.76669 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7cd18906-1a9a-3027-af96-d76f5246f4fd | -9.45852 | -60.54929 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6862dd10-c5d5-3347-9d74-84cfffe63485 | -10.02707 | -46.02945 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7496b321-9789-3d9b-a21a-fe89049a504f | -10.07203 | -58.36055 | 2025-08-30 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a248da-f88a-3bbc-9b29-d0599dfc15ce | -10.37296 | -57.82778 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 424b9dbf-05e9-3143-acc5-77e21859f094 | -9.4535 | -60.53642 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa0ddf98-543f-37ed-8280-f02f8976b94a | -9.45202 | -60.53665 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39fa29dd-f3ee-3315-8cf2-803c66e5f332 | -6.88369 | -56.47375 | 2025-08-30 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 122fb706-5f0b-3f47-a13b-7df6f2a31730 | -9.43617 | -60.54604 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19cd4835-f869-310f-ad1e-51de23893c94 | -10.37074 | -57.82022 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 832afb84-d4b0-3f1f-95a8-c5d354ca11ea | -6.63474 | -55.27004 | 2025-08-30 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 617acbf6-0fe3-310c-b803-bcb8c0150f04 | -7.11685 | -44.60112 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6fd5f405-481c-3dd5-b374-f12697a3826c | -9.28118 | -60.45766 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8401b05-c08c-340c-ae3c-8300dda59445 | -11.86332 | -46.39699 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58da8871-b350-3583-9123-4cb6ad5c5922 | -8.17948 | -61.37848 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8e0bd8a-79a6-3778-904c-9c0dfd1d37b2 | -9.45075 | -60.54446 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 070f9dbb-193a-3039-8a0d-d41762fb4982 | -9.43438 | -62.32338 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5acb294-ff91-3f06-8b29-36a89c4b593e | -11.83517 | -46.46916 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 09336342-ad80-3a1e-8ac0-3e4300ab556b | -10.45254 | -57.96979 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd98a24c-69a4-3b85-9ebe-0b0c2d0bb878 | -11.84601 | -46.43909 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0c4ba4f5-dc5d-3d56-aac6-0086279f0023 | -11.85773 | -46.39245 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b0d75a2-80e3-3354-9300-a1e094331b32 | -6.34466 | -58.17429 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ab11557-e4e5-39fd-a61b-57157ba70292 | -10.44509 | -51.35817 | 2025-08-30 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f4caae3-288e-33c0-b9de-9dde25e1ff2d | -6.76644 | -43.78627 | 2025-08-30 05:10:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f505fdfe-853d-3d64-b7a5-1415ecd5363b | -10.66953 | -48.73431 | 2025-08-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64af1ca2-b480-3ce2-8043-1fb5a171dc1b | -9.4496 | -60.55977 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cfb7de63-5eb7-3977-8fad-6c8dd681c774 | -8.8725 | -60.73562 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 425f19d7-7083-34cc-a59a-9aa9d372b47d | -11.83689 | -46.86546 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffcbef42-3e39-34b2-9e6f-fa7a1553b283 | -9.44315 | -60.54718 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7bfeaee1-6bab-3079-ac43-5742ab6c83b6 | -8.88798 | -60.72997 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce75b504-4a52-32eb-8592-95dbbe5248ac | -9.17118 | -59.58111 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07c7c9fa-0744-39e5-8720-9f6dc7705e69 | -8.89987 | -62.10784 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c82acbec-553e-32cd-87e8-eca15d479936 | -11.82868 | -46.46875 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ca486112-732d-31db-8c75-996cad3d6006 | -9.2517 | -56.8983 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4475014-b4a9-360e-baa7-156c94b4d6bd | -7.95985 | -46.39198 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f874e7de-132a-39cb-9b90-1b0f30f56dc6 | -8.55176 | -63.0194 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25a4c91c-7ac2-371b-a74a-3f5f7cef1fda | -10.36247 | -59.20331 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82a9264e-57c9-348e-ac69-5aa05212c2e1 | -8.56196 | -51.31178 | 2025-08-30 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c92c569-4100-3bae-a9e2-ce462c3c8d73 | -6.78159 | -43.78118 | 2025-08-30 05:10:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9bebaede-5468-3e76-b6a0-dae38e2f12a8 | -7.19752 | -43.7051 | 2025-08-30 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f3f6c75-ed57-3743-8676-977650230f06 | -5.69469 | -45.96024 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea270642-3529-3d35-a63e-dd711c4ee2b7 | -11.83002 | -46.86967 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c5d6b7a-cbb4-322f-9c54-eb3fc8c69a47 | -11.87243 | -46.37855 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c420d6ad-3a4e-3dcf-a072-ee1450efec2b | -11.88946 | -46.39843 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05fa7d01-3942-3ee6-8294-c4c806efb718 | -8.96004 | -65.96896 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3c14410-38b5-37dc-8529-6327956ffcf0 | -5.82592 | -46.36236 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e638ddbc-954c-3184-914a-3721d2ca8762 | -8.56387 | -63.02152 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14f71192-7818-3cf3-be21-e4199e2acab1 | -9.61925 | -45.96248 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1259288c-3ec3-3a0c-ab66-ecf8d14b3f08 | -8.90146 | -62.09846 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c572b54e-69da-38e9-8b8c-291a8614decc | -8.18244 | -61.38346 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3dab754-e395-3076-b6cd-5b08ff689b0d | -9.15987 | -59.58676 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40d585c5-a753-38a3-86ad-4ebdc43ca70f | -9.43998 | -60.5667 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 78755c55-79e2-3dea-ad7f-a760f2cfee21 | -5.70084 | -45.96114 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf41b543-c9c7-3015-aca8-5adcc5c4ca62 | -10.37628 | -57.8283 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cb5c2b3-c361-3c1b-813a-3546c84ab332 | -9.44677 | -60.55527 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4d353a8a-efd4-38ec-a2c0-8e84ab27f879 | -9.21738 | -46.75451 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12ef3fea-5c95-3665-8a64-bad089db8102 | -7.4325 | -44.80469 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e7bb6af-c816-3c9a-9ee4-a5fa6e1f763f | -9.1764 | -59.57821 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README64.md)
