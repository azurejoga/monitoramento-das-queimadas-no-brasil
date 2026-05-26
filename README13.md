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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a364cfb-5af7-338b-85f8-8f559e56a38e | -12.05274 | -57.41949 | 2026-05-26 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b90b8224-56d5-3105-9cca-5a7938cf17b6 | -10.15174 | -65.18059 | 2026-05-26 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed9a36fd-c194-3d0c-bd22-f6e74e4d870d | -11.35392 | -52.96666 | 2026-05-26 05:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 297110d3-952b-379d-b337-37f0732200d7 | -11.3547 | -52.95978 | 2026-05-26 05:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 79c7f2b5-b5f3-331a-88bb-e855c8f2dad6 | -9.55709 | -64.62698 | 2026-05-26 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c853daa-803f-3a8b-beab-9156cbf264a1 | -11.73651 | -54.81311 | 2026-05-26 05:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 351ebdd5-ee10-3393-8885-3b0d1d1db830 | -11.177 | -55.91915 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e30c80b-ec0b-39da-95e5-06223f0d5b12 | -11.40218 | -57.54587 | 2026-05-26 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a8192a1-d181-3484-8c1e-d93bc3e393c3 | -10.14457 | -64.88589 | 2026-05-26 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d905ade-48fe-36e8-a6ed-2b008887992b | -11.21437 | -53.82968 | 2026-05-26 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d55ec48-dfcd-37ce-8eb3-3ae8a82bce22 | -11.21506 | -53.82364 | 2026-05-26 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93332866-d8ac-3912-8f21-b4b9b80d5402 | -11.21879 | -53.82428 | 2026-05-26 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7efef8e1-977b-3280-baea-edbdcc1d98eb | -11.5494 | -56.9315 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9c5f417-295b-3b16-8fe4-b69239dfb8ec | -11.18136 | -55.9172 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3cc5853e-6537-347c-bb29-fe52ee2600e6 | -11.54894 | -56.93518 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a521fe9-ce96-36dc-a504-b64a36260188 | -10.91324 | -54.11557 | 2026-05-26 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12651a14-3cfc-3d75-8382-cff952b22acc | -6.52271 | -55.06609 | 2026-05-26 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28881cae-43ea-3d77-9dce-1b9445cfcaae | -6.52214 | -55.07013 | 2026-05-26 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfe2abe1-7c2c-3686-9b66-f5eb17c9280a | -11.91485 | -57.03938 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e52f9f0d-549e-3c8e-a9c8-981524291cab | -11.18401 | -55.91121 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 431d9906-54c2-3dfd-83c9-fee7a40e58ab | -9.56836 | -62.47908 | 2026-05-26 05:53:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc4808a3-2091-3661-b61b-4790733f9296 | -11.18189 | -55.91277 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 036b2c36-cdac-370b-8554-2b988d4255a1 | -11.96572 | -56.81034 | 2026-05-26 05:53:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bdfd547-ece4-3104-b7b4-9c9794f3c5e0 | -10.14508 | -64.88548 | 2026-05-26 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc267b90-a70b-39c9-ad97-05a01e5f251b | -11.56008 | -56.93641 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66f557d2-3884-32e0-8fe6-66ff3599d367 | -10.14837 | -65.18005 | 2026-05-26 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6be6fb3-759d-38d3-979d-119f91fafe6c | -11.27569 | -53.97086 | 2026-05-26 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c26736b-d435-3349-8e58-c6a3d975ffe4 | -6.52329 | -55.06203 | 2026-05-26 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0de77d31-2a05-3c56-8c81-b5ab27ead792 | -10.14452 | -64.88916 | 2026-05-26 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc4ac616-0524-30df-a774-b277ac0e0adb | -11.21807 | -53.83023 | 2026-05-26 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2924610c-7f7c-3e55-9053-cc2b1ca7fae3 | -10.03506 | -59.36235 | 2026-05-26 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9a18cf5-7535-33c4-8034-30d10aa1d5e1 | -11.40543 | -57.5494 | 2026-05-26 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2fe93fb-c8cf-33ee-bd68-0ea1e10a078a | -9.93816 | -65.00703 | 2026-05-26 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91c1646b-1dde-3bb5-8a79-486ddc30cce7 | -11.18345 | -55.91558 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 082ed5bf-feaa-307c-8036-795383555e83 | -6.52121 | -55.06353 | 2026-05-26 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4ec93bd-2a17-3a4c-819f-e0078d7d3702 | -10.91983 | -54.11634 | 2026-05-26 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16b81ee8-b7c3-31a9-b16a-c3104f7cf63f | -10.03571 | -59.3576 | 2026-05-26 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8ee93be-8ae8-3198-891e-350607ede252 | -11.17495 | -55.92065 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c055da0d-1d53-3817-8603-7ba273e5d125 | -12.05082 | -57.41975 | 2026-05-26 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 410d4904-76a8-3583-8231-8fb156465c48 | -11.17756 | -55.91473 | 2026-05-26 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8507ac9f-7a60-3732-a4ab-e88a4fedb70d | -11.361 | -52.96752 | 2026-05-26 05:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1609fcc4-b5ac-3bdb-ad8b-8c9b45cf96d4 | -10.91918 | -54.12181 | 2026-05-26 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b001c3de-06a4-36f8-adf3-57bfb4cece36 | -11.40175 | -57.54916 | 2026-05-26 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02e9780f-a552-3261-a9b2-5d0ae92045e0 | -11.39686 | -57.54519 | 2026-05-26 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80fb028f-7f13-3b53-a24a-bc07139a2030 | -11.36257 | -52.9537 | 2026-05-26 05:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 95d79a4e-dc15-34e3-bd51-58d828eee2dc | -11.40051 | -57.54542 | 2026-05-26 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b086ea71-1209-3204-9ba4-a64680a5b024 | -12.05816 | -57.42021 | 2026-05-26 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ddf4c23-66d3-3284-be18-4588bfed6945 | -11.4001 | -57.54874 | 2026-05-26 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4eb0ac4-4130-39b1-a8a9-1d57a33354fe | -10.1523 | -65.17698 | 2026-05-26 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87a2b30b-1dae-32f8-b2b7-01b0e95c3018 | -11.9153 | -57.0357 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66877cc8-7b06-3cdc-bb73-314c787e12cb | -12.05623 | -57.42044 | 2026-05-26 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 448421a7-50b5-3f7d-907a-a75c232c22de | -11.55451 | -56.93581 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fc52b0c-f9bd-3662-9c2f-5e8327e5058c | -11.36178 | -52.96067 | 2026-05-26 05:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 3fe86d9b-154a-3b06-9b7a-b806c7e92c8d | -11.55404 | -56.93946 | 2026-05-26 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78bafd74-0000-3dda-9c8d-3289c9f4f3ee | -11.35549 | -52.95279 | 2026-05-26 05:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| bbcde221-85df-3e7c-9101-f1dfc9aab78b | -6.52066 | -55.06758 | 2026-05-26 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 380b8cc4-22ad-30ad-bc8c-3837c8289255 | -11.73713 | -54.80799 | 2026-05-26 05:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b70484c7-4363-34b1-b23e-8939d2ac5723 | -12.14041 | -64.27112 | 2026-05-26 05:55:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2763e93c-44e5-3c4b-ba08-698fabc60489 | -12.13688 | -64.27059 | 2026-05-26 05:55:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c575568b-55f4-3449-8b33-072914565256 | -10.5978 | -44.31314 | 2026-05-26 05:57:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2bf98a4b-21e6-334a-b4fd-33a39f5ad7f0 | -7.1279 | -44.06338 | 2026-05-26 05:57:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a7a6d5c5-8f59-3bce-a8c9-a7c704a8f68e | -5.78458 | -45.11752 | 2026-05-26 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| afe7bd93-585f-3b71-909d-e2a6b50c23d0 | -10.59547 | -44.32732 | 2026-05-26 05:57:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bc024d28-264c-37b6-a094-68415931894c | -5.30304 | -43.0612 | 2026-05-26 05:57:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a56d7f56-69df-3aa7-8a2c-2412691f6399 | -5.78887 | -45.10291 | 2026-05-26 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 473d583e-9a12-301c-99f5-728d92555a5f | -5.78556 | -45.12277 | 2026-05-26 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| c5e8f507-0353-3d98-970f-f04916c81686 | -8.55269 | -45.98101 | 2026-05-26 05:57:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 91914d27-aede-3b5f-b6bf-7f88b762176e | -7.13931 | -44.065 | 2026-05-26 05:57:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 3f485222-5222-3769-a83b-dfcea8150551 | -11.3584 | -52.9514 | 2026-05-26 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 58aceae1-00be-33cd-98d1-092c8cccb1c2 | -11.3584 | -52.9514 | 2026-05-26 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ea5d5eb4-8a2b-30c3-a30e-d9030e757aaf | -9.55809 | -64.62811 | 2026-05-26 06:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01f3ec79-ea82-3295-815c-3c5a45474bb7 | -12.13946 | -64.27048 | 2026-05-26 06:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1993c534-7aa7-3f0e-80b6-e6536835b14c | -10.15114 | -65.18204 | 2026-05-26 06:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c1c0495-c9a4-36ed-89dc-f851eb63646e | -10.15182 | -65.17705 | 2026-05-26 06:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aaa6674-edca-3402-8a20-2e5d13e6befb | -12.13699 | -64.2699 | 2026-05-26 06:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83f6d27f-39b5-3edd-8f8a-8a0a6f4ace75 | -11.3584 | -52.9514 | 2026-05-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 15e5f772-d19e-30e5-9941-a2934c6ed997 | -11.3581 | -52.9722 | 2026-05-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b9fc9d17-5cea-3310-8249-ed8ed59555ee | -11.3581 | -52.9722 | 2026-05-26 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 833ffd4b-627c-31db-9362-b91b506784c9 | -11.3584 | -52.9514 | 2026-05-26 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 41ea0016-ca1e-3f2d-a6ca-b7a824759217 | -11.3584 | -52.9514 | 2026-05-26 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 0677bbf3-9b9d-3c61-a8ec-873594c872d1 | -11.3584 | -52.9514 | 2026-05-26 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c44f43f1-c53a-352b-9ba6-90fcabe7b212 | -11.3584 | -52.9514 | 2026-05-26 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 23728de9-11f4-3b15-a0fd-04934d49de89 | -11.3584 | -52.9514 | 2026-05-26 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 7dd9cf51-8ff2-386d-9b12-5c1ede15e6c0 | -11.3581 | -52.9722 | 2026-05-26 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 15205417-d58f-3eeb-9642-5acc89de774c | -11.3584 | -52.9514 | 2026-05-26 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 3e1baa44-810a-381f-861e-9b7a1f578eec | -11.3581 | -52.9722 | 2026-05-26 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f3c0caea-674d-377a-8d8c-182a23c4fa6b | -11.3584 | -52.9514 | 2026-05-26 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 9ecf8189-3708-3b9b-aca4-b5d95b75eb49 | -11.3581 | -52.9722 | 2026-05-26 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 170ed2d8-1c93-32f4-bce7-1be5cee5fd87 | -11.3584 | -52.9514 | 2026-05-26 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 4bfbd122-8c15-3a56-918f-a064b15b3efd | -11.3584 | -52.9514 | 2026-05-26 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 695b7adf-39ab-3849-8ae6-05daaff29012 | -11.3581 | -52.9722 | 2026-05-26 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ab865244-55e9-3dda-8ec1-1548b29b91c0 | -11.3584 | -52.9514 | 2026-05-26 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 9d2abc6f-cdd0-308e-aed4-3b9a9692dcbe | -11.3584 | -52.9514 | 2026-05-26 08:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 4fcedce9-5859-3986-9fd7-29c334d86e6b | -11.3581 | -52.9722 | 2026-05-26 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 763d5a69-31a3-3c7b-890a-b90defc850a3 | -11.3584 | -52.9514 | 2026-05-26 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 75f60cf3-b111-3d9d-8161-13cfd376cd2f | -11.3581 | -52.9722 | 2026-05-26 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5ffd81da-27d8-34d9-a615-924d8845ee52 | -11.3584 | -52.9514 | 2026-05-26 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 68db1397-3e5d-3104-8898-0c3f6efc74a9 | -11.3581 | -52.9722 | 2026-05-26 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7c04d5b6-dd16-3af3-ae38-3de11a65169f | -11.3584 | -52.9514 | 2026-05-26 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 5f4fe23c-8b7a-31b2-87aa-9a6add9abaf3 | -11.3584 | -52.9514 | 2026-05-26 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |


[Clique aqui para ver as próximas entradas](README14.md)
