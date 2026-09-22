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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5c9b7e9-e6a8-3f10-8d9b-6e8916d069d3 | -8.80176 | -60.80637 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b16370f8-9a42-3c82-848d-97a39e077208 | -9.56667 | -66.01986 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3c1c9f1-fc53-3962-89fd-72f9c114884a | -10.46819 | -69.19707 | 2026-09-22 05:44:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1eee2a9f-775d-356e-9034-411e6db2b7ed | -8.79195 | -60.79575 | 2026-09-22 05:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 627ccdd9-e862-3803-9333-c36ac62bba58 | -9.37293 | -68.65822 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2b23a2b-f77f-3a44-a7cc-df6712218d7c | -13.50724 | -51.52188 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 21fd7717-1b90-355e-bbfb-7b75f6c50686 | -9.55423 | -66.03268 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fddd9b6b-613b-3ff6-94d3-ba8bc1250e45 | -12.79806 | -54.06549 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 606bc716-b6ba-3425-b81c-44de687ca6bb | -10.60653 | -53.99639 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 38cc2cb5-fc12-3938-926e-9ce858083777 | -9.76155 | -65.05822 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2a5137e-d9b6-3df1-88ee-1429c76e08bb | -11.31919 | -54.03992 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97236d08-ba78-3871-8818-5e03eee1f3da | -10.86988 | -57.17074 | 2026-09-22 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| adfe2486-b018-3f7a-9785-a7101e631de7 | -9.13464 | -67.9485 | 2026-09-22 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db9745fe-9556-3b4a-884d-3ab7a41ce2e2 | -10.90464 | -53.96083 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21573e7d-b881-3283-8152-cf8a1dd36aa1 | -7.92594 | -71.34345 | 2026-09-22 05:44:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1a4ed0a-9010-3cf1-a61f-46d0b57e8a13 | -8.52176 | -67.00755 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b64c897-7507-3f5c-8c2b-2230ac4c2ad8 | -11.31887 | -51.36185 | 2026-09-22 05:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 105dac21-da88-3235-a430-ec7bdcc3a08f | -11.96561 | -64.04202 | 2026-09-22 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 681754ae-4f86-3d17-bb8e-85b77976307b | -9.3984 | -65.91779 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a23758b8-27f6-3327-8181-941966d310bd | -11.15277 | -51.10178 | 2026-09-22 05:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c4f7a78-4b2f-3521-ae30-0250d00469e8 | -9.55276 | -65.999 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0a620f9-184f-362f-b80b-ab5c3e3f6e46 | -10.59949 | -54.0044 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f4015b2-015d-3c83-b207-3a7271460661 | -9.10362 | -65.36907 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 782ee471-eee4-3091-8252-7e581ea8e1b2 | -9.82347 | -65.0109 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65281904-2188-37ab-b4e0-95ca4dd01bcc | -9.56712 | -66.03852 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d8102f6-ad9f-3108-af98-842a8d4ffbe2 | -9.11192 | -65.38129 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3831438a-6a59-38b7-b1e4-545f6aea89ef | -11.31267 | -54.04355 | 2026-09-22 05:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7128856-52c1-382a-ab4d-b4bc6efd2871 | -9.35393 | -65.73454 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9946ed38-2da9-3355-8a36-8f38a50e7d3b | -12.80033 | -54.04667 | 2026-09-22 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef23da23-14d0-3ca3-939c-99d506f8f0ad | -9.55071 | -66.05442 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3360e900-a59b-3b52-b1c2-b96407cbf3e9 | -9.36992 | -68.65541 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8636aaac-5ca2-3aaa-9204-94a6805d8305 | -9.11305 | -65.37423 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d9a92ec-25ad-3c28-9108-6947023ca44d | -9.09973 | -65.37206 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c47329c-0fa0-3539-960a-67760d0ab943 | -14.04585 | -52.06394 | 2026-09-22 05:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b31deb4-a3e5-3893-ac90-f263251de5cb | -10.13155 | -68.30817 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afa1b7f1-b251-3707-b5fc-f26c6340b746 | -9.67044 | -66.82915 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfdabd4d-3b24-3d53-9d58-6d603675de4e | -9.56052 | -66.01511 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5733a0eb-868e-3dfb-933f-458df5543147 | -11.16545 | -51.1176 | 2026-09-22 05:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e490fb40-d527-32df-ab30-56707d9bfeed | -10.90315 | -54.07314 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69478c61-1c3e-3e01-98b1-00df0dbe0d9c | -11.3273 | -51.36829 | 2026-09-22 05:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9edb98f-f7a5-34b3-9d92-ccc57b539864 | -9.13536 | -67.94421 | 2026-09-22 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67f635ff-fd65-3940-b26e-21620475b485 | -10.22077 | -59.40205 | 2026-09-22 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d52e71a6-494b-35e5-8f74-b6cd61f85ae8 | -9.2976 | -58.91765 | 2026-09-22 05:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2867f84c-2d6a-3a34-8adb-545bbb920843 | -9.50331 | -66.73102 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a2d97e0-06a7-3bdb-a2d9-f38b0f3e9190 | -9.74425 | -68.44305 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d197395-ecb4-381e-a041-5216995bb346 | -9.87455 | -55.72763 | 2026-09-22 05:44:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3587a9e2-03d2-362d-947b-628ce4a52314 | -13.51282 | -51.50864 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| eed7edc2-905f-31eb-9ec4-129b6f255595 | -13.5223 | -51.51614 | 2026-09-22 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 63fad865-7387-3888-a183-8d384030d5bb | -8.73403 | -72.79491 | 2026-09-22 05:44:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aa2a4d4-90b0-3ce7-9013-381d74fa0b9c | -9.67235 | -54.33954 | 2026-09-22 05:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfbbf872-f5c6-3e85-abb7-99e6cb2f6fd3 | -9.09583 | -65.37505 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78611d60-e762-316a-84dc-b5ff88790528 | -9.18713 | -65.85798 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6fbd01e-87b6-3d5d-ac63-d194d9c81280 | -9.28646 | -60.63539 | 2026-09-22 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5582ca8-9fcf-3a22-bf11-996f3c590ce4 | -9.5513 | -66.05079 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0917ee19-1a00-340c-bbfa-05a1619df51e | -9.30385 | -69.35904 | 2026-09-22 05:44:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4490d09-a27e-3a0d-b92d-ac79cd34729e | -10.74268 | -68.53036 | 2026-09-22 05:44:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6752f21-a1f2-320c-9564-bd791dec87cd | -10.06821 | -68.47905 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8289b336-da09-3bdd-a37d-a70a0a87d4bf | -10.90086 | -53.97168 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2990c7b6-3bc3-3365-a35d-c8d6da6d1763 | -8.79425 | -69.02135 | 2026-09-22 05:44:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc6898f4-92ef-34c2-87e9-202e462f828f | -11.15912 | -51.10969 | 2026-09-22 05:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9ef50df-1225-32f5-b48c-cfd86800561e | -10.91825 | -53.94909 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04628ff3-86e0-3138-b3b0-05eded977ac4 | -9.55994 | -66.01873 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c955a7ca-2708-3968-944e-2d60fff0b5b4 | -9.55759 | -66.03324 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6553b71f-6a3a-38eb-a3ef-2f890a8dcb6f | -9.18494 | -65.85025 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2642a890-33ff-3ba1-9a19-bea17e1005eb | -13.29753 | -51.80169 | 2026-09-22 05:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d33208e7-7bbf-3975-9689-15c16cd333bc | -9.55877 | -66.02599 | 2026-09-22 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd4e8d57-fe0c-31f2-bca8-edca02716ee0 | -9.11248 | -65.37775 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 224bcb17-bcd7-3bc6-b486-db58394e5b21 | -10.89489 | -53.97076 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3021b305-5b6f-3fa5-8c75-0568f91a0aeb | -10.93455 | -58.33999 | 2026-09-22 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83346bac-46ba-3ea3-a46f-bf2f2d200a68 | -8.52943 | -67.00475 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec2ee791-d1a1-3f80-b1ad-03188776138e | -8.54534 | -67.03999 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bf6e41e-95d1-3589-8e13-a78997aa6ddd | -10.22752 | -68.75005 | 2026-09-22 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4abaaaa1-0960-3ef8-8125-d65ecc697032 | -10.60815 | -53.98329 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c03847bd-6dc3-3d49-989a-fd98ca7a227e | -9.12201 | -65.86602 | 2026-09-22 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d12c1d4-985f-3bf3-a272-4766c2678104 | -11.32592 | -51.36271 | 2026-09-22 05:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5ead5da-7b55-3c81-9e49-861c2b658976 | -11.04799 | -54.15217 | 2026-09-22 05:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffeb7156-e68c-3a38-ad5d-316301189e79 | -11.99324 | -58.07792 | 2026-09-22 05:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba50e639-b4c7-3e2d-b7fc-a3557201b14e | -16.84831 | -56.7882 | 2026-09-22 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 71c78a8f-4a38-3f6d-81aa-3478dec506d0 | -16.84869 | -56.78469 | 2026-09-22 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8b22570a-4519-34fe-8c00-92f6761f9b7c | -16.84292 | -56.78755 | 2026-09-22 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 18865d74-29b6-3c0d-a2a8-09e56cc051bb | -9.23507 | -46.1629 | 2026-09-22 06:01:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 439.3 |
| b47daeeb-ce7f-3535-a126-8ca9c7e5651f | -8.78879 | -44.26324 | 2026-09-22 06:01:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 50d788a5-9099-38dd-896b-8cb20d787fbe | -8.79648 | -44.28303 | 2026-09-22 06:01:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 4d165a1e-8716-306c-be36-9c2a48d4904e | -5.75062 | -45.09127 | 2026-09-22 06:01:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 2d895717-0579-36f9-a65b-fbe4838b1c48 | -4.83129 | -42.86802 | 2026-09-22 06:01:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 049b9359-7cad-3787-a257-a000a7937dba | -3.68584 | -42.95092 | 2026-09-22 06:01:00 | AQUA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 73cebb1f-0598-33e2-9c70-16ec21be1f6e | -8.78641 | -44.25623 | 2026-09-22 06:01:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| ffe0dcb6-b697-3032-accf-a4288120261a | -4.94232 | -38.09086 | 2026-09-22 06:01:00 | AQUA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 887f6b22-d165-3c1a-8750-227500db3c94 | -9.24133 | -46.12787 | 2026-09-22 06:01:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 62ad8a96-7b82-381a-b0a4-664b2c129e32 | -6.47721 | -42.77183 | 2026-09-22 06:01:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 2e1b54eb-da2b-31b8-8d90-99c5242daabe | -5.75628 | -45.05756 | 2026-09-22 06:01:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d2e849d2-6b55-37ac-a304-6e55016a951f | -8.78448 | -44.28773 | 2026-09-22 06:01:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7f3db7c0-3011-3211-afc1-c813aa4a0708 | -11.13953 | -42.83133 | 2026-09-22 06:01:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 606a830e-2bc9-32a3-b7b8-683d044d9d2b | -7.35894 | -45.3437 | 2026-09-22 06:01:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| c5b4c5dd-b143-3c4f-8e37-e78c128d3f2a | -8.78243 | -44.27987 | 2026-09-22 06:01:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 833b352c-4df1-3048-8e1f-db04bc1cb073 | -11.14306 | -42.8447 | 2026-09-22 06:01:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 26c7b763-f748-3c30-b796-6fa34b12128d | -11.14602 | -42.82706 | 2026-09-22 06:01:00 | AQUA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c2370c75-10b2-3e5a-bfd9-4ef16c306df7 | -11.87544 | -46.857 | 2026-09-22 06:03:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| bf4130eb-4146-336b-99ce-7246c6889906 | -12.56989 | -45.95757 | 2026-09-22 06:03:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 206667f9-5686-363e-a3c3-3d4a08b90123 | -12.844 | -44.3235 | 2026-09-22 06:03:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |


[Clique aqui para ver as próximas entradas](README119.md)
