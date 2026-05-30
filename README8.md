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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fa6f1c0-b0ae-3141-a9c9-ea1716500282 | -7.33838 | -49.85534 | 2026-05-30 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b52845e5-af08-31f0-a18a-566a371af3fe | -6.2361 | -48.45229 | 2026-05-30 04:53:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95b622c9-39b0-3c14-8949-33187783d077 | -7.34132 | -49.85997 | 2026-05-30 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 294f51d7-9be9-30d3-99f7-f764cb3fa07b | -14.12899 | -58.94907 | 2026-05-30 04:55:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f38894c-f7b4-3520-b4f3-56c8130b24a6 | -14.12988 | -58.94405 | 2026-05-30 04:55:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e5a1b83-f835-3d5b-a1e8-9f85a8193c52 | -9.45867 | -57.84607 | 2026-05-30 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96c716b5-a3d5-3faf-b5e3-cc0b1286554c | -10.13043 | -52.40104 | 2026-05-30 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b15b3ab-77ed-3b79-86c9-973bac60a22e | -10.50752 | -48.09809 | 2026-05-30 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05c39831-1d83-3575-b99b-381facb2991e | -11.60025 | -47.44407 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f556e79f-4219-36cf-9a97-1df34f177d1a | -11.16752 | -46.79065 | 2026-05-30 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fb1e271-6559-3efc-88ee-fa6a5060b019 | -11.6978 | -44.16199 | 2026-05-30 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b8fb916-76f3-3b3b-8837-020dd71cb986 | -10.76184 | -46.98622 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5db9bc2d-8978-3046-bd47-862e0e62fa64 | -8.72288 | -47.83692 | 2026-05-30 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8b783b2-120f-3836-8a93-7aacd64b5ac3 | -11.16266 | -46.7877 | 2026-05-30 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c976b0f0-a1d7-3342-9658-e28cf239f4d8 | -14.13252 | -58.92895 | 2026-05-30 04:55:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68f570d1-e48c-362b-b3c3-34d16cf735c7 | -11.76472 | -47.06499 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 467aa199-882d-3625-ba53-7a4eef588033 | -11.58691 | -47.44017 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9aa78d7-f63e-3a8c-ab87-73feae317da6 | -10.38629 | -49.44524 | 2026-05-30 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1caa2868-4556-354b-a5d5-b6e92b7d6501 | -11.79883 | -57.00921 | 2026-05-30 04:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df09568a-6669-3112-8bb9-459545fcb712 | -15.58662 | -46.81207 | 2026-05-30 04:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96fc9783-73cb-3d33-a69a-4dab4706d391 | -10.8137 | -46.89152 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 420a95a9-458a-33eb-bee7-068da07614ca | -12.00085 | -47.76646 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a3c8aaa-b1e3-368a-bc24-33c19fc3a774 | -10.78014 | -46.95269 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9cebbf0-dbd6-3c7a-9b10-489ba51cfc60 | -10.29443 | -54.33221 | 2026-05-30 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 245d1c9a-964e-37d3-897b-1213bf722788 | -11.92336 | -43.92583 | 2026-05-30 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42ba08bb-6d87-3313-8853-cd29664be98c | -8.54063 | -51.48752 | 2026-05-30 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bd8fe7b-e058-3aee-9929-7c7f3362b082 | -11.53556 | -46.43924 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dbbfbd0-77d7-3eb2-8442-84020a15cea5 | -10.85055 | -48.33962 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee9f4ffe-cc3b-32e3-8b09-1ea8e34828c9 | -8.91309 | -51.84526 | 2026-05-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a79ccc7-4a42-320d-a9fc-ccb3d48c4aaf | -10.84097 | -46.92741 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0d0c894-d545-379c-a49d-d72465d8ae8a | -10.84277 | -46.91402 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b4ff8ce-e51a-3969-a3f4-638e4bc85bb1 | -10.80298 | -48.29567 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8c1bb168-b925-3a69-8dea-3403e8b812df | -10.84647 | -48.33905 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aba9982-c46f-3747-af9a-7401bef7261f | -12.52501 | -57.21862 | 2026-05-30 04:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a059a2c-5efe-35d5-98a8-49ad87516dd5 | -12.6771 | -54.58259 | 2026-05-30 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9333db1-1ec1-368b-8926-eb090c76058e | -10.76608 | -46.95536 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 731f529d-2547-385d-9f1b-0c35b8c67177 | -10.80087 | -46.95395 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b324ddb-0366-3b9f-b20b-632bd1ed7fe2 | -11.70282 | -44.16315 | 2026-05-30 04:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a83b9287-0fac-3d15-b4e6-b6ba838fd3ca | -12.13307 | -47.21456 | 2026-05-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5b46cef-0d93-3f27-8e52-3d4682d44e15 | -10.77197 | -46.97879 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e0dfa84-fec4-38bd-9605-c66c235a88cb | -10.76669 | -46.95092 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 958654c7-1c75-378b-9a4c-1f9d7e5aecf2 | -12.31932 | -47.89558 | 2026-05-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b75ec15-31cb-35d5-9555-f028b94f15a5 | -11.60006 | -47.44198 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aafc2286-029f-3ce0-a72e-ecf0323b1fdc | -11.76536 | -47.06037 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d57650f0-9be1-38be-b0e5-ad0db4f842de | -11.9763 | -47.89392 | 2026-05-30 04:55:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ee32457-4cc0-39f7-a6c8-b97a9daea566 | -10.84421 | -46.93733 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 679f4b64-fddb-3ca9-8c62-183cd8ccd671 | -12.68098 | -54.5796 | 2026-05-30 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e48ccb0-0313-3215-ad73-0f9f726cb332 | -10.77565 | -46.95213 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a433074-2a21-3ac1-be7a-144c6ad8d00d | -10.11012 | -52.16305 | 2026-05-30 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf4ea4b5-de1f-3ed1-aebd-0875cc91025b | -14.05989 | -53.36964 | 2026-05-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5502d0a-5e95-3b89-aec6-e7f63c4f5650 | -10.76791 | -46.94199 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a01c1e3-28d0-3ef2-80ca-9902828ea380 | -11.76038 | -47.07602 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7a87cda-ef55-30ca-9be2-a05cf58b6238 | -9.39733 | -48.45184 | 2026-05-30 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6a19f88-227b-3c7d-bfb4-717f381f56f4 | -10.78263 | -46.93463 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c90fc7ad-79a2-3d27-8eaa-46b5c1495b3a | -10.06082 | -49.11223 | 2026-05-30 04:55:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 606474b7-e4b8-3cc2-a46b-633decf7f790 | -11.91182 | -43.83522 | 2026-05-30 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a4b614d-c793-3904-b891-6d6e0968632a | -11.92895 | -43.92656 | 2026-05-30 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c311b97d-4dd2-3a89-9bfe-4e3008b45dce | -10.80314 | -46.95144 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a6f335-3880-390b-9f64-32102759aae6 | -9.80059 | -48.92635 | 2026-05-30 04:55:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab5d1547-839d-352b-9a9f-72c707629444 | -10.75796 | -46.98125 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07b68e7b-a31e-3c5a-8163-61f2f33e1f12 | -12.7035 | -44.79176 | 2026-05-30 04:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a9b92a8-ff99-3ab1-bb6e-a4a9c4095a9e | -10.80438 | -46.94255 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0078630-fef8-36bd-9abe-6e22fda81a0e | -10.76487 | -46.96416 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72feffc8-2720-357c-a8bc-58ff928cd07d | -10.56614 | -46.84513 | 2026-05-30 04:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b86d85d-3255-3a4c-b437-36e786b6607e | -10.13923 | -52.13068 | 2026-05-30 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71248fe0-8cfb-3843-a7ee-b0088b3a4173 | -10.84301 | -46.94624 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 7b9df100-4cfe-3ee5-af56-60fce576e94b | -10.04746 | -51.65966 | 2026-05-30 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 096a2666-ba99-378b-b442-564a396b2080 | -10.63378 | -49.73133 | 2026-05-30 04:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69049550-b5f6-3771-8069-994b4c762e52 | -10.78201 | -46.93912 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0fad839a-9ee3-3e16-93b4-9be34fff1674 | -10.7598 | -46.96789 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 234e4a66-b440-36c0-a729-6c5e1acc2090 | -10.77178 | -46.94706 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2db98ab-27c5-3716-b2a2-d34a29cf1afb | -10.62945 | -48.31903 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7a7e774-722a-3a4b-95ae-561332dd7a8b | -10.84546 | -46.92804 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a225444c-ef0e-392e-988f-c8acd9bc265b | -10.76547 | -46.95976 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a7ed3e9-ebe0-38b2-88d9-47a8914e6906 | -12.00958 | -45.35796 | 2026-05-30 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3de3375-96be-3e48-a441-cceea074840f | -10.81429 | -46.88704 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a2a3a22-2679-3fc7-8806-f6f931653047 | -10.8481 | -46.94234 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 92228f36-4783-389e-b5a7-385c5a3e8c38 | -10.11348 | -52.16359 | 2026-05-30 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9321e226-c261-3aa3-a35a-6b20a9f44eed | -11.76219 | -47.06212 | 2026-05-30 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 592afd8e-8ecc-3114-ab57-f7bdc3a6ebe7 | -10.8182 | -46.89207 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c218e4b4-dd73-3528-b9f3-faf7052abe95 | -9.9267 | -48.69071 | 2026-05-30 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1fd153d3-2d5c-37ff-846f-f20a8436cd83 | -14.12599 | -58.94336 | 2026-05-30 04:55:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50ab6a27-1042-3de0-8e17-9ebf179f7cfb | -10.82243 | -46.92918 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ea1b5e0-6b7e-336f-bacb-0da4089b7da2 | -10.7604 | -46.96346 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaebcc4a-789d-34fe-8889-3f7a08df0cb4 | -9.92745 | -48.68559 | 2026-05-30 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d85afed1-b02c-374c-95b1-d26763cf11fe | -9.45161 | -51.82796 | 2026-05-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61dd4648-3670-3503-8a25-bb37792f2039 | -12.80069 | -54.86915 | 2026-05-30 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6428407c-fd9e-379e-9654-9f2258366a53 | -9.89094 | -52.44049 | 2026-05-30 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d0731b0-48a6-3f94-b4b3-17b2a569e5e4 | -10.98831 | -49.04204 | 2026-05-30 04:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0321ca3-7098-376c-a8ed-605e564aa2f0 | -10.84218 | -46.91836 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1d798f4-0c28-37f5-9114-9c907b9a2682 | -10.84158 | -46.92282 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab152039-245e-3e4e-9e54-bc4ca9f365cd | -10.78856 | -48.54115 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdd484bf-1696-38ab-ad06-775b0493b66e | -9.36922 | -50.54652 | 2026-05-30 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ad2c55-dd44-3530-9d36-d07a27753356 | -11.59129 | -47.4408 | 2026-05-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb3bab3b-f7d1-315d-89c7-95012fbd8dd8 | -11.69734 | -44.16243 | 2026-05-30 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2d44d95-c361-3f26-b52e-b2189a841bc1 | -11.97953 | -47.89366 | 2026-05-30 04:55:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 720a5e76-c5cc-35c0-a15f-ce9eb60a7ec5 | -10.62894 | -48.32269 | 2026-05-30 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e9332338-a48e-3a13-a1b6-c412c3d79f5f | -10.84483 | -46.93268 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| beb4d82d-112e-3700-8527-e259b46b1f2a | -10.76404 | -46.93692 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 020a4bc0-ef84-328a-98b3-271a3b453f7c | -10.8475 | -46.94679 | 2026-05-30 04:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README9.md)
