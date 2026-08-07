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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bf41b56-de6b-39e9-a718-ba45dd09a262 | -14.41964 | -45.6797 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcf7ae13-60af-38ff-a0ce-5e4a0fb88bc6 | -16.69016 | -51.36393 | 2026-08-07 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24ed549f-b185-34b0-a599-40f31bf9c7e4 | -13.68865 | -51.98062 | 2026-08-07 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79bd580c-2f16-3683-9858-376b08e3a270 | -16.18459 | -46.22799 | 2026-08-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64cdbcf3-0dbd-34da-b158-cc41c8e5163e | -14.42438 | -45.67249 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9f9fead-5b57-3722-83f9-a35f2ed3a960 | -12.55199 | -46.96505 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f236868-bf6b-32e0-bc1f-892ac8d3ac59 | -16.5332 | -49.42094 | 2026-08-07 04:10:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17bd590b-7f6e-3440-95ba-70be6817892a | -10.49027 | -46.69277 | 2026-08-07 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64359d52-3b9d-3802-8b59-61173cb386ad | -17.5363 | -45.35469 | 2026-08-07 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7f56328-6452-3f6e-b2c7-d86e06099067 | -18.33458 | -43.91537 | 2026-08-07 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87f7451b-4a95-3f41-b0cf-ac58917fe38b | -11.14938 | -54.90853 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8f74fcc-4587-3f72-929c-74b04ebe333b | -17.93377 | -45.20786 | 2026-08-07 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7618fd5-71f3-330c-adcb-d7c10c180fb2 | -12.55222 | -46.94098 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c86f35b2-e3d2-36c2-855f-10ed3c3f5b3c | -12.565 | -46.93393 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0b1f62b-a517-3909-bfe6-a755fdd813de | -11.1304 | -54.90408 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 973c2921-9726-3db7-90d8-71564d257ab2 | -13.76807 | -47.18375 | 2026-08-07 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d5e5cea-d940-3e59-9fd8-1239eb3ce373 | -11.32403 | -45.20844 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2223a8a-3f5a-35a3-99a8-dca63027e6d1 | -12.63137 | -46.89058 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b7ad3ed-5fa5-328c-b38e-c4650a1e0dee | -14.3354 | -54.92958 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce2806bf-7fe5-39c2-ac9c-3a44117d3b3d | -13.93885 | -47.36351 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee205135-1d9f-3bf7-b576-561391546b83 | -11.13564 | -54.91094 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba99585d-e1fa-3688-b90d-ba0e444350f1 | -11.12787 | -54.90755 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c80e20ec-799b-3871-be50-c9df1a87d70e | -12.556 | -46.94145 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ee6bcce-42c9-3d58-99f9-9c582f6b6411 | -11.15175 | -44.47726 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01542c5f-9826-3883-b1bb-a4ef9577480b | -11.12904 | -44.48526 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d25a409-c769-3ac3-9c5b-5b27cc713558 | -14.21292 | -40.98694 | 2026-08-07 04:10:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6f7c0944-ad1d-3182-a39d-687de71d6489 | -12.00025 | -45.13454 | 2026-08-07 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 470a8b1f-d0ab-39b6-9b56-ca18ed551e25 | -17.84421 | -44.48913 | 2026-08-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a15ee458-6537-3dbd-946d-7327ec20d5be | -14.2723 | -45.29197 | 2026-08-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 899ab8df-351f-33b1-968f-11eb012ac132 | -11.46681 | -44.57106 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9575fc02-0d98-36ff-bea8-aabecd56c95c | -13.83583 | -53.71587 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e97f8407-a689-30c7-a365-77a06d6f7141 | -11.1601 | -54.85538 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0863e4bd-560e-3e87-8a49-380ec144c189 | -16.68824 | -51.37408 | 2026-08-07 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14af4080-eca7-3de1-8a4a-d34edfc416c4 | -12.90383 | -45.64617 | 2026-08-07 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c91600b5-a06e-3a6c-a12e-6674a182196e | -11.13646 | -44.48264 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2de0e096-6b8a-3cbc-8f94-edec3e384acc | -11.13466 | -54.8831 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17450769-a4bc-3ceb-9a40-4289745de718 | -12.33446 | -53.16672 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44522161-85bc-3bf5-ac0b-ce2797dbf7ff | -11.15114 | -44.48098 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afb961a6-5ba5-3b6d-9a56-babc92b1b230 | -11.15795 | -44.48209 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69043bfe-4113-363d-856f-b6aa1588b680 | -11.14107 | -44.47573 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2dbd7594-b6ae-35d7-bac3-a9e5d6fed9a0 | -12.61067 | -43.40691 | 2026-08-07 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e71d848b-debe-38cc-9514-788cc6c5ebbe | -14.27107 | -45.29957 | 2026-08-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 351916b5-a311-359a-8236-f748af2a3d4e | -15.07953 | -53.58879 | 2026-08-07 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db5c9ecf-d7b5-3b73-8015-ba4ac15e4f0b | -11.12893 | -54.90217 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16aa50a5-5d08-35f6-ab65-d047ff2173d1 | -12.31353 | -44.8721 | 2026-08-07 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 067214f8-6ffa-3ff4-ad42-ff3379d7933b | -12.562 | -46.92885 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e28ae95-6659-3739-959e-7e5fd6cc8faa | -15.92749 | -43.98483 | 2026-08-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49d2c4e8-0465-3a15-aab3-2a9c87389dd9 | -12.13366 | -39.76686 | 2026-08-07 04:10:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fee5664a-16ab-3e88-802d-6d538f7c8848 | -13.96139 | -47.36993 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73b111ba-0160-3a8f-b253-1549b50fa4e2 | -13.00463 | -42.66878 | 2026-08-07 04:10:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 91ec5fcf-d7f1-30bf-9b1d-f0e553fb89f4 | -14.99183 | -47.86718 | 2026-08-07 04:10:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b4cb547-134a-339e-b668-52df097da762 | -12.14323 | -48.26515 | 2026-08-07 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b907161-80f7-3337-84d5-7e2e357d6037 | -16.52915 | -49.42001 | 2026-08-07 04:10:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5b1887e-0683-343c-a9d4-4910992efc5a | -11.15393 | -44.48526 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d7b84eb-58ff-31ae-b0ef-094bebb05e27 | -12.55672 | -46.93722 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a88355b3-9000-3996-a24b-8a89fd07200a | -15.93024 | -43.98896 | 2026-08-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04502591-972f-3e5a-89bf-96ad227c2f37 | -11.13826 | -44.47142 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 999882c2-6b52-3e5d-bf55-aeca3eac4118 | -14.35231 | -54.90921 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4a686867-c50c-3d53-8e4e-f1d62dd901cd | -11.46062 | -44.56277 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a2fe5174-ef69-3f57-96b1-396dbb04e381 | -14.20944 | -40.9864 | 2026-08-07 04:10:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 604d51a0-125e-37f6-8a41-80af32cd6ae4 | -11.14167 | -44.47199 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11b52759-4b12-3c23-a278-33ffc3420965 | -10.63599 | -47.49258 | 2026-08-07 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbc19b68-d36e-3e7d-a930-18536d0b5a62 | -12.56124 | -46.93331 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65b33ba0-e37d-33ed-ab9a-68ea9e905ed9 | -13.78134 | -48.50257 | 2026-08-07 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5f8ca5c-b342-3540-a6cf-8fc2803ed626 | -13.82058 | -53.72139 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27e9f365-71e3-33ad-8175-ddca97bf2db9 | -14.43065 | -45.67758 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b797bd7c-5ecc-3a82-ab91-75a508c255f7 | -11.12403 | -54.90285 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66d7d95d-804d-3c99-aa2f-c930012bbc2a | -11.15454 | -44.48153 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 127f5c21-962a-307a-8440-81bb54c369e6 | -11.12997 | -54.89683 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fb693ee-deaf-3777-a69f-f2d3fa16d4e7 | -15.90129 | -48.00868 | 2026-08-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69908c31-531b-3a68-b809-cff250430d3c | -11.14387 | -44.48003 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8eb3a8cf-7d0d-32a8-8d35-bea47f27509c | -11.14889 | -44.49234 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5748a4f1-253d-3c23-b069-fdb5337fa20e | -11.13486 | -44.47085 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3735b829-1110-3250-82f5-cca3b18ae773 | -14.43192 | -45.66979 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 756d7d42-803f-32d0-8563-9c305c32915c | -11.14488 | -44.49553 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b3df3fb-e7b6-368c-8b93-f97bb421939c | -15.89759 | -48.01053 | 2026-08-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b49a3850-9b59-34b7-b851-c9dd02498dd1 | -11.14267 | -44.4875 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5aa333c-42e3-3633-9df7-6fb0b3f03cb0 | -15.87164 | -43.6019 | 2026-08-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69847b49-eeed-35c8-90eb-e447026d9dd4 | -10.49373 | -46.64959 | 2026-08-07 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03d3e2bd-aded-3644-aeae-6e08ea557405 | -12.56874 | -46.9346 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6582e73-9c5e-310e-bd58-bd5576f0b61a | -14.34908 | -54.91784 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 389440f6-e251-3f7d-aa8e-0fe958a766f7 | -14.35135 | -54.91375 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 838bfcf9-3acf-3e0c-a791-927d37c485bd | -13.94046 | -47.35662 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec148d73-9f75-337f-8246-e1934ae76520 | -12.87362 | -52.8231 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77084167-21d2-3fd1-bf1d-b8964d3bcbe5 | -11.13926 | -44.48695 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c25d1699-80d2-3116-a98d-69abe321a1b5 | -12.49064 | -50.37 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c79a68aa-dc7b-31a3-9c8c-ab3493eaac9d | -12.56049 | -46.93772 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99aed627-b6a0-3406-b65f-7b233d29796c | -14.16209 | -54.00188 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c726521c-4e6f-3d19-98f2-e4c494f58d45 | -11.46343 | -44.56708 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b948e39b-a9af-3f7d-884f-cc41b97db953 | -11.13706 | -44.4789 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d88efac5-fea2-3ea6-8175-7700034f6be2 | -12.33151 | -53.16949 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5aec3e7b-bc9d-3090-b66d-00816475abd2 | -15.87495 | -43.60245 | 2026-08-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e04bd7fc-d811-3122-b63c-7e5ecfa1ae44 | -11.14447 | -44.4763 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc6a0ee2-38e4-39f4-a629-444e5c7da02d | -15.90045 | -48.0134 | 2026-08-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c2347f0-03e5-3f23-86c5-ada0ad8f3399 | -13.82938 | -53.71859 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a9c02f2a-26b7-3f83-b793-e3a9551e3cd8 | -16.16481 | -47.99547 | 2026-08-07 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e6d1e9e-de86-3d2e-9284-730658e99ee1 | -11.14047 | -44.47946 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 1781c9eb-5a85-3b0b-8f7e-05caa2675cc2 | -14.42847 | -45.66919 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c771f492-6758-3963-b5ee-b78a45464e8e | -15.08822 | -52.76775 | 2026-08-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3027546c-1480-36fd-bfbe-5f17c0e88bf6 | -11.18024 | -54.85366 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README10.md)
