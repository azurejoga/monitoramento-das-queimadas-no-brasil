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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fe68e0f-e99f-37e9-8fea-808d96f67178 | -4.51086 | -54.96103 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce280d2f-3763-3e18-9825-284bfc12a2e7 | -6.90235 | -59.03089 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 577e54fa-9b81-341b-9653-13aa15bcabc6 | -3.40122 | -61.07453 | 2026-09-17 05:36:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff0ab752-1dfd-33f2-afad-0001bbdcfd61 | -6.70887 | -58.80708 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2577facc-4ac2-32b8-8b70-c3515b0d175e | -9.28226 | -60.62893 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a95a3fa8-e2db-30a2-a486-550240a543b6 | -4.5148 | -54.96618 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 816f0f97-f066-3edb-ba39-62864a130c0d | -8.49583 | -57.64791 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da0e4608-5f4e-3ff5-a13b-84ee2b8218b5 | -9.09559 | -60.95971 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 611146e4-f2eb-3897-adf4-c8dcd2d7a5c5 | -8.91906 | -62.39583 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0506b2a-d85a-3742-a09f-94a8eed2fa79 | -8.00272 | -61.37222 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4236758c-b9a9-3da7-bba8-ff795b22c818 | -6.32913 | -60.00743 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de3d6589-c641-39da-a618-29608ccfb68a | -5.15526 | -55.94746 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798ee6c8-3d20-37b9-8315-469444b29565 | -5.14846 | -55.93363 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a3f3211-a9cc-3089-b3d5-439420132cbb | -8.64261 | -66.58088 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e0c510e7-1de5-3e32-bbf4-1996b2a7be71 | -9.10361 | -60.97633 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f10cf9e2-e79f-3b67-966d-051f1e3464fa | -8.09219 | -61.81986 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 769d65ee-e1af-30bc-b6e6-544677d84e1a | -6.93119 | -63.02311 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e6ff3d0-af7d-3b89-b3f4-d1c2455b4b2b | -9.9088 | -57.06484 | 2026-09-17 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fea7936-41c3-3246-bb80-06f60bb13455 | -6.30739 | -55.15636 | 2026-09-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64f7e3ac-2510-3043-b811-593e7f18cb5e | -8.60289 | -64.099 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a335d6c6-1bd5-395a-b60e-3a736a13964f | -5.90468 | -52.09553 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee306c21-fd56-36dd-8146-cbe6ca9eb8f5 | -4.49854 | -55.50264 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 511064de-7051-37d0-90d3-c49efb031362 | -8.48113 | -57.63494 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6fd9144d-4ea8-3aee-b02e-238ab66ca2da | -8.00608 | -61.37274 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac12f195-40f1-33c8-a07d-33221d286636 | -7.06541 | -63.07609 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93768c5f-b124-3558-8633-8a3d1829b3c6 | -5.66346 | -60.24027 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f54579e5-9708-3fb2-b265-58402d942364 | -5.14414 | -55.93289 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 188f708c-a7b9-3ff6-a0a5-f6a233d133e0 | -9.48939 | -56.75797 | 2026-09-17 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f80573-a501-31d8-a24d-73f2800d73f1 | -6.35973 | -58.28425 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24f9f71c-91a4-39ef-bcb1-784627bec8cc | -6.30809 | -55.15145 | 2026-09-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ab9f7f6-f438-317e-a26a-0a72f68bd463 | -4.85922 | -56.02575 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3894abe8-042c-369e-bed4-a7715a6d9d3d | -4.39934 | -55.44473 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 836157bb-d432-3e00-aef3-e7d82c43eda7 | -6.84681 | -62.8916 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76ac4d72-1cc1-3884-8928-aca8b3faf20b | -7.60675 | -67.32056 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b617a9d-f420-3c76-b11d-b42bf67640dc | -3.69896 | -60.60911 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c7c4149-81fa-3371-a3c1-44a298d0bb2a | -6.34562 | -51.7776 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 559027c4-eba0-3986-b552-4f6b99c415df | -6.79684 | -59.18579 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f7d8e36-b2cb-3247-961f-945add104d20 | -6.20998 | -55.28348 | 2026-09-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb723720-c99a-34ee-97e9-8d41fd597213 | -6.31121 | -62.67063 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8866e75-19f4-3ef0-a579-1c56ad2785c4 | -6.36364 | -58.28287 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a99d457-3d35-3a8e-b9f6-26bf4cb7b101 | -4.54797 | -54.93283 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d831fc61-3c39-39c6-ad0d-4c3ce5092038 | -6.8011 | -59.18213 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 915cfd84-2a97-35ab-aa50-c758584b29d4 | -4.51754 | -54.94761 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09c51348-7101-381f-a6c5-5035fb09b38e | -8.91465 | -62.40229 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 111d20ab-e6e1-32b4-a19f-a9f2ccf34d8c | -8.76982 | -61.39444 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79330bcc-918d-37c9-9c4a-1da5d1331907 | -9.49434 | -56.75441 | 2026-09-17 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b73065b-2475-3634-a0cc-e58bdc842737 | -7.6107 | -67.24857 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f091b341-edf5-3d04-a9b7-ab467d7a35c3 | -8.59895 | -64.10204 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d357877c-2c7b-393b-804a-45ce1cea712a | -9.28053 | -60.61675 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 688fd61a-d955-3bf6-b085-877596b0ccf6 | -9.40662 | -60.35363 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc919a5c-7553-3542-a5f2-bdde1092347b | -4.8614 | -56.02806 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da0883a5-41bb-3d23-899f-840510db44d1 | -9.10359 | -60.95324 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 404a25ca-1e28-3743-a7ba-dc6de09c6afe | -7.79848 | -66.91576 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8406d3f7-ef40-3f80-a2dc-f9bf061e2e2f | -6.80064 | -58.79271 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0481982-3387-3b4e-8e88-3061a1419438 | -9.09734 | -60.99456 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 045143ed-ca2a-3cfb-a301-524703e2aad7 | -4.53807 | -54.93605 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b3d5d1e-626d-3a81-bab8-71071bee5ca4 | -8.22383 | -61.50207 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc88c556-7659-3c99-8b4f-16c3653bf89f | -3.70342 | -60.60257 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5a4a933-e27f-327e-85c9-349956257fba | -6.70185 | -59.46081 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b20a455e-ef80-300e-8d39-b662a1c596af | -7.55367 | -62.33287 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c0529f1-ef7b-3471-a5d7-e0676dfd64f9 | -6.79511 | -59.1726 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecd9875d-06f1-3c1b-804b-132a7049901a | -6.68673 | -58.85291 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df581928-6ea2-32fd-87cb-e8adcd4fae31 | -9.38191 | -60.30189 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e21ac05-173b-3776-9f8f-5f9f257ddfaa | -4.39381 | -55.44578 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc01943d-a0f3-3023-897a-c8dc5ae0248a | -4.51341 | -54.97554 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e5aaffc7-b39a-324c-bc85-c0f7f2f4699f | -6.84736 | -62.88812 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c339907e-d3d5-3d53-9acf-45f5d790be69 | -4.50952 | -54.97015 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad31eacd-dfc5-3e46-8c14-fd11f2447118 | -8.49228 | -57.64378 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c6f8179-1b02-3dd1-958f-eba8cf1b55e4 | -9.31305 | -60.27906 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c74162c4-600d-340d-8131-3e1d4b3be779 | -9.29281 | -60.53503 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe0052dd-a013-3039-92ea-c2331daf1aff | -5.9129 | -59.93797 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f599c2d-1aa6-3371-8cef-5d50f5543c1a | -5.92543 | -51.64804 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f7affc7-c352-35fe-a410-b028eef4e542 | -9.59453 | -60.51874 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cc2e2e2-fd08-35f0-a4ff-94c6a214a7a5 | -6.79385 | -59.18102 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 014d7cbc-b592-3262-a448-f160c4dcda32 | -4.51412 | -54.97072 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ce22c7b-e170-321b-aa8c-7be46c3b3d75 | -6.68607 | -58.85725 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45fe2635-3cf8-37ba-b73b-4e365980453b | -6.33027 | -60.02331 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb4d3ab5-a26e-39f3-8596-392788bd0cd4 | -5.15588 | -55.94332 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d42b2962-f134-31ce-a37f-d81ff4e6e6ad | -9.09845 | -60.964 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2c706ef-0e34-333c-9e32-4a3e2466e68a | -4.39494 | -55.4439 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4577db38-5ccf-3cd4-877d-fd08e97c0dc1 | -4.39886 | -55.44223 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daf69134-d2fe-323b-a98e-304f867ed18e | -4.862 | -56.02399 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ef38c02-4c78-3342-a8f4-7e8152627619 | -9.09618 | -60.97902 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88dcb616-fee4-3753-8a33-bb42ff803a0d | -7.79386 | -66.91987 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d3a381f-a97c-3e56-99cc-1f94f8ff7521 | -9.28633 | -60.62558 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 260c1940-450e-3b06-9671-e0083b4964ed | -9.77246 | -60.46746 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c5d8ac0-db5b-39ab-9f83-d0182b6e07ec | -9.25039 | -60.79322 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d62dc4d-3d95-3f73-a003-ca94f3571753 | -4.49423 | -55.4956 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcdaf262-e0db-38b6-98fa-812bc36a0103 | -6.90474 | -59.04002 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e7ead18-1c67-3b46-ba06-40f4f519c517 | -5.88769 | -52.09221 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 278c3d88-b1fc-3eb4-b048-d3a975486997 | -6.2009 | -57.77868 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f8065e7-8738-35c5-9c3b-b558b63e6db7 | -9.07188 | -61.00265 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de7d071c-d0b0-3382-886c-23dea3725239 | -5.75158 | -57.59628 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a9ec4c6-5ab3-3283-b590-85de7e3fe488 | -8.11165 | -64.11597 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b6e1a44-41cf-3b34-9d9a-0edf8380e864 | -4.38646 | -56.35151 | 2026-09-17 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efb28873-430a-3435-90a7-308aa1f74a7e | -5.92665 | -51.64971 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7ee56f4-3c5f-3f6a-b62d-4d43364ee9a8 | -3.70231 | -60.63129 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11107d4d-0682-33c8-b023-dd619166c82f | -9.40906 | -62.71381 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b7ed68c-a37d-3c95-bcea-bf1f7d65bcf6 | -6.35916 | -58.28693 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd9892b4-107e-3e18-b54b-44c8f6bff840 | -8.88147 | -62.39703 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README76.md)
