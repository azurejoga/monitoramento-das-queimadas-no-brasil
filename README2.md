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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d530d90c-3341-3c49-94af-22208b9e93c9 | -7.08 | -59.17 | 2026-08-26 00:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 104ef8ef-7169-3121-8b52-303ceee5a1f1 | -12.77 | -44.29 | 2026-08-26 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13d2e387-0bac-3cc3-ab88-fd712fe612ad | -10.75 | -54.09 | 2026-08-26 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 386edfaf-e3fc-3534-8025-32289cd92452 | -7.05 | -59.24 | 2026-08-26 00:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47149b3b-447f-3f77-ac65-4a49ad08b1e1 | -10.74 | -53.96 | 2026-08-26 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6875c947-af2e-32b4-b3d2-d861eefe25a8 | -7.08 | -59.24 | 2026-08-26 00:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a1113c4-ae8b-347c-96c6-c82a18b2e3c1 | 1.51 | -55.9638 | 2026-08-26 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 59311a89-df21-364f-93ae-c9e54c9191a1 | -13.2277 | -51.3973 | 2026-08-26 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 8c89d27d-8e69-3767-b507-1acbff89d3f8 | 1.5284 | -55.9439 | 2026-08-26 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2a1e2a2d-78c0-3573-9ba8-a8e89ba39469 | -11.4302 | -44.5382 | 2026-08-26 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c5511045-446a-3030-b28a-5bbdae29503d | -13.2259 | -51.504 | 2026-08-26 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 28b72392-c70e-3a74-b8f5-6c96681d111a | -9.6022 | -55.128 | 2026-08-26 00:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a8bae643-5041-3af1-ace6-f564fd8406cd | -17.482 | -39.9449 | 2026-08-26 00:20:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 214.1 |
| e52877f0-2a19-373f-90ec-e1f3f605b585 | -9.6586 | -55.1036 | 2026-08-26 00:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d0267ed9-5c8b-3acc-af87-15e78aeaa642 | -10.3723 | -45.0767 | 2026-08-26 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| fd56e5dc-e9ac-3166-b875-8bece3bd12bb | -11.9807 | -45.8858 | 2026-08-26 00:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4d98e2c3-831a-3132-b2a0-8d3d0c3f6d1f | -12.7797 | -44.2576 | 2026-08-26 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a49c77e3-65fe-3015-a1da-28804d0da19a | -17.4828 | -39.9188 | 2026-08-26 00:20:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 189.6 |
| 4df8b9bc-8b17-38b4-9bb6-d0606e5f54fd | -10.3727 | -45.0537 | 2026-08-26 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 249.9 |
| 9d6deed2-0d67-3edb-9809-ae857b049c13 | -13.2256 | -51.5253 | 2026-08-26 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d517d888-0379-3bb0-88ea-b63948d498d1 | -12.0358 | -46.0146 | 2026-08-26 00:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4a5b39f2-48a5-393e-ad70-fb7e3aebfa21 | -13.2448 | -51.5229 | 2026-08-26 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 489f40a6-90a1-3f0b-919f-7707c0341d04 | -6.1286 | -57.8198 | 2026-08-26 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 10ba47df-6663-3eaa-b34d-4b7ebcc74404 | -6.1102 | -57.8205 | 2026-08-26 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5cbd9aba-bcb6-3b8f-ab66-4abe9e2e5f71 | -12.0354 | -46.0374 | 2026-08-26 00:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ac6a65d1-a0b8-3982-9598-7578d5d5ea09 | -7.4474 | -43.1163 | 2026-08-26 00:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 1352c83c-fe86-35cc-8e06-87ba3767450c | -7.5289 | -61.3825 | 2026-08-26 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| de9c6bef-8e0d-3268-8c2d-613e380d4dad | -7.5104 | -61.3832 | 2026-08-26 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| caae6ced-fe30-3e24-bfe6-42303e9cf788 | 1.4918 | -55.9443 | 2026-08-26 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c36b8fac-d8c5-3df3-b609-ae41b49854d4 | -6.641 | -58.4987 | 2026-08-26 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| b4f632bc-6a97-3ebe-84aa-fab974b3a182 | -2.7948 | -49.582 | 2026-08-26 00:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c50cb865-ad10-3125-9ed6-f6140859bda5 | -10.9848 | -51.1655 | 2026-08-26 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c11321de-3b4c-3aac-9c17-0e11f07d55ab | -6.6595 | -58.498 | 2026-08-26 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 716f557d-76b4-3fea-9c6b-5358527de5ff | -12.7603 | -44.2608 | 2026-08-26 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 411eec64-f94a-3a4a-93c1-13a52fa74031 | -11.2732 | -47.0669 | 2026-08-26 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 44c77a7e-c9c7-36a9-a74c-60cf1141d3d2 | -6.6226 | -58.4995 | 2026-08-26 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| f9380177-6fa9-3ac5-bf5e-3df6c209d43f | 1.5101 | -55.9441 | 2026-08-26 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 3199c9f5-b2ed-3daf-9343-b5ee32a750e9 | -9.6024 | -55.1078 | 2026-08-26 00:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 2051c4c9-7b58-3686-a968-98744d30bf4a | -7.4663 | -43.1144 | 2026-08-26 00:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| bf59eff2-7d8d-3b1b-988b-67abb955c462 | -10.3918 | -45.0512 | 2026-08-26 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| cf02352e-94c0-341a-bc3a-1f713bbba60d | -9.6588 | -55.0834 | 2026-08-26 00:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c2189225-7e58-3249-8ce1-ed8cb8cabe1c | -2.5042 | -48.1366 | 2026-08-26 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 1117d93c-a367-33b8-824b-4714c2427d1b | -6.6409 | -58.5181 | 2026-08-26 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| a925bde5-fab2-3165-b24a-1c899bea3a53 | -6.6225 | -58.5189 | 2026-08-26 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 38bea4ce-79ef-37f1-ae3a-73072f8384f1 | -5.6479 | -46.9467 | 2026-08-26 00:20:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| cba09cca-a64c-33cb-a2f6-170d8404d5bf | -7.767 | -44.7543 | 2026-08-26 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a1730012-3cc8-3193-bd38-8e598b8cc115 | -13.2451 | -51.5016 | 2026-08-26 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 38f2dcbd-99e8-3e77-9c48-22d37e0fcfd2 | 1.4917 | -55.964 | 2026-08-26 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d8d71034-c3fb-3f22-a837-717ec9047c0d | -11.411 | -44.541 | 2026-08-26 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 3541e0b4-48d9-3f68-b143-707e6c6a5d58 | -7.2856 | -44.0875 | 2026-08-26 00:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 32c5e7a3-e54a-387f-97bc-cb6640026168 | -13.2835 | -51.4968 | 2026-08-26 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3ffb7341-f8a3-3f37-a94c-c4456a7f68ee | -7.7481 | -44.7561 | 2026-08-26 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7ca6b494-c4c2-37d1-b1b0-37577883164e | -6.2676 | -53.3768 | 2026-08-26 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 88857817-c28f-3572-944f-27d24d7c93aa | -12.7608 | -44.2373 | 2026-08-26 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| d4d04223-e559-376c-8431-0e68ef290697 | -5.6666 | -46.9455 | 2026-08-26 00:30:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 63e2e455-c1a3-3eca-a881-6fe1adf7265f | -7.2856 | -44.0875 | 2026-08-26 00:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4db2fa1d-e4f1-3772-96ea-839722a11493 | -10.7784 | -54.0368 | 2026-08-26 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 290.1 |
| 5383cdc7-d91c-3f73-ab5b-4f12d989b1d1 | -12.7603 | -44.2608 | 2026-08-26 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5bd15390-f2b8-312a-83fa-caa5df9fc394 | -6.6225 | -58.5189 | 2026-08-26 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 89f5ca5d-b98c-36a3-9abd-8653779ddee5 | -10.76 | -53.9974 | 2026-08-26 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 9dd51d6f-2595-343b-b6e3-e1b39bed1e69 | -13.2256 | -51.5253 | 2026-08-26 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 812fbb10-6337-3686-9e02-d876b2c2d8f5 | -6.6226 | -58.4995 | 2026-08-26 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| ac03da1a-0ec9-3e5d-99a1-f2067cd3954a | -10.7598 | -54.0179 | 2026-08-26 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 320.7 |
| 39a0439a-6d67-3084-b19e-8024377a8c50 | -7.5104 | -61.3832 | 2026-08-26 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 4025c595-9c25-371c-98ff-d4950d3dc36d | -12.0354 | -46.0374 | 2026-08-26 00:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 3aaf814a-2d31-3f06-be2f-c409e0a5a212 | -7.3034 | -49.5414 | 2026-08-26 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| c4e1df68-fec1-3543-a8fa-669ed2a9b478 | -6.641 | -58.4987 | 2026-08-26 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 9bd58ef6-d6ab-3626-bd8e-578c62365e06 | -10.9848 | -51.1655 | 2026-08-26 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 4ec7de25-0f8d-3557-b822-cd33ce24823a | -10.7787 | -54.0163 | 2026-08-26 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 9ff80dea-7c92-30a6-ad48-064be321713f | 1.5101 | -55.9441 | 2026-08-26 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 129e3591-ed93-3e25-806b-2af24e758128 | 1.4918 | -55.9443 | 2026-08-26 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0c175733-04c1-39b5-9ec1-8c919d5fcffb | -10.7409 | -54.0196 | 2026-08-26 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 48157702-dd9d-3364-9359-0bee9f924569 | -11.4302 | -44.5382 | 2026-08-26 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 79b08217-3a71-32d7-821b-305c35a405e3 | -6.1285 | -57.8393 | 2026-08-26 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 432e4543-f055-3dba-ac05-e3d990e27f8b | -6.6595 | -58.498 | 2026-08-26 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 2894640d-64b8-3f6f-b066-a2f13fd0c603 | -10.3727 | -45.0537 | 2026-08-26 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 226.7 |
| 2e897f12-d4eb-3a4b-a844-f3529a00448f | -9.6024 | -55.1078 | 2026-08-26 00:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 6416da3d-149c-3dcc-ac72-043fc21f14a5 | -11.9807 | -45.8858 | 2026-08-26 00:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6525d8af-5db2-3078-ab39-81260b8d0e1b | -7.5289 | -61.3825 | 2026-08-26 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| fce4da0c-cb96-372e-ac9c-c87fd56c1096 | -11.411 | -44.541 | 2026-08-26 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3cf70d88-64b6-39bc-a35d-4747705b2ed1 | -13.2451 | -51.5016 | 2026-08-26 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 876372c1-73a8-33bc-9e70-898bd851e3ba | -12.7797 | -44.2576 | 2026-08-26 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4e05d7f5-9b85-3d18-a7cc-04fa49eaa08f | -9.6212 | -55.1064 | 2026-08-26 00:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| fa146016-413b-3740-951c-39d2097595bf | -6.2677 | -53.3565 | 2026-08-26 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4a8d1815-21eb-3a95-bcf2-cbebe94ffdea | -7.767 | -44.7543 | 2026-08-26 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 43cbd012-b23d-305a-bcc3-2b3ba260edf2 | -2.5042 | -48.1366 | 2026-08-26 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| f9f6f2c3-d03f-35f7-a63c-221ca29daeb7 | -6.1102 | -57.8205 | 2026-08-26 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 79f98b5d-e19d-31c5-b56f-813f88292672 | 1.4917 | -55.964 | 2026-08-26 00:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b2373ee8-5f23-3c27-a21a-8f11823cec0d | -11.9615 | -45.8885 | 2026-08-26 00:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 28245ba6-44d0-3ef6-85b4-574dd577b629 | -12.0358 | -46.0146 | 2026-08-26 00:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 7107bca6-876a-3b50-a0e4-a9ea7e6184ba | -6.6409 | -58.5181 | 2026-08-26 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 894df1bf-524b-3efb-a638-20ea4541982d | -10.7596 | -54.0384 | 2026-08-26 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 436.6 |
| 2dede49b-586b-3a6c-b678-1970924bef0f | -10.3723 | -45.0767 | 2026-08-26 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 158.5 |
| e00177dc-352a-3ffe-800b-dc201d4516ca | -13.2259 | -51.504 | 2026-08-26 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8cee7295-7916-392b-8df3-3a06870ca943 | -13.2448 | -51.5229 | 2026-08-26 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b6494c62-baeb-3652-a7f1-e29e134bf230 | -6.1286 | -57.8198 | 2026-08-26 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 4d85922e-15b6-300b-a4b6-894374470826 | -10.9845 | -51.1867 | 2026-08-26 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 16ac0a83-4f6c-3ac2-834e-728318c27fda | -2.7948 | -49.582 | 2026-08-26 00:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e79aa694-0fa9-391e-9c29-f70f2c61de5e | 1.5101 | -55.9441 | 2026-08-26 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| baada526-9c8a-34b7-96d7-28f0077ed12a | -9.6024 | -55.1078 | 2026-08-26 00:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |


[Clique aqui para ver as próximas entradas](README3.md)
