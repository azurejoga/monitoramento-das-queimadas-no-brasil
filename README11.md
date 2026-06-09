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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b43eae5-7704-3cb4-85ac-ac7cfff45540 | -11.59127 | -58.51016 | 2026-06-09 04:49:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ec31c9a-d369-38b5-9499-f8930a28b759 | -7.60389 | -46.46982 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e19b9231-b44f-35ee-bf5e-712be34562e4 | -8.72207 | -48.07859 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96d81ecb-a9c8-37e4-b262-5cb30cd03b56 | -7.89257 | -47.09807 | 2026-06-09 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 403f2785-3f18-3a8d-bb52-4e692b5b9567 | -11.27116 | -44.5292 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fba0a8bb-26ce-382e-9f24-46952cca90da | -9.3107 | -45.48509 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4320cee5-88c9-3c64-a701-c81af78510e3 | -11.34626 | -45.61823 | 2026-06-09 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d117ba98-b493-3637-b3d2-9ea5e8eace32 | -11.35034 | -45.61882 | 2026-06-09 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7bb069d-8e3a-33de-8e35-090244f7659f | -12.36053 | -47.89573 | 2026-06-09 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31025acc-9c75-33e6-9f6c-ddd8d14f52af | -12.22342 | -43.99425 | 2026-06-09 04:49:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77a84ded-2665-33be-9e8e-d62ec70cfa95 | -11.55051 | -52.78434 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 446547be-95e6-33d9-bc1a-089b548cd99f | -11.90003 | -57.78196 | 2026-06-09 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e28bc5de-87c2-340f-9af6-474d7a0326c4 | -11.02731 | -44.31698 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26a5ba1a-b967-34a6-86f8-38ee9c99f56a | -11.89982 | -57.78401 | 2026-06-09 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3299f87c-0cde-31b8-a604-4ff3efe2b9c8 | -12.03162 | -47.80457 | 2026-06-09 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5534b8a3-2673-3e6f-9861-62172ff28529 | -11.64615 | -52.86246 | 2026-06-09 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2f4f318-9476-376c-8fb0-f869802796fa | -13.49535 | -56.5756 | 2026-06-09 04:49:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb6e64f0-2a04-30b8-9d43-bb809ea82dc8 | -12.4678 | -55.1324 | 2026-06-09 04:49:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5b3e1a1-7077-315c-b5c3-8c66503a4da8 | -12.05693 | -49.76189 | 2026-06-09 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f2ff52d2-3a04-3699-a585-509d867c77ae | -13.25835 | -44.39452 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 627cf993-712b-3d69-be4a-71fb23fe708d | -11.47787 | -57.1175 | 2026-06-09 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c962f64-527b-3c0f-bc59-4ea7fb859126 | -11.90069 | -57.77934 | 2026-06-09 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdc48aec-71b1-3116-8ca8-639bafc9fd17 | -10.17221 | -51.66171 | 2026-06-09 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fbbfd95-6dd7-3f18-9dfe-cfad1277d3dc | -10.3871 | -49.44945 | 2026-06-09 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66725d2c-2b88-360b-9188-74df0fcbcc16 | -11.27555 | -44.52979 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 744643d6-2c0d-3728-9a06-b01e4fc7c61e | -11.57129 | -54.58451 | 2026-06-09 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca75f441-36a7-385b-b6f3-d0f5a823b6a5 | -12.03523 | -47.8052 | 2026-06-09 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01c25ac0-3782-3f95-9c40-c10c39a56a7b | -12.48603 | -46.27327 | 2026-06-09 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dee168a3-4938-3081-ba0a-bc044a4b42a3 | -11.26713 | -53.97483 | 2026-06-09 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b196701-545b-3fd7-b59e-16fb53609922 | -10.45412 | -46.47514 | 2026-06-09 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f98523b-50cd-3281-9b1c-dcbadd8df068 | -12.77191 | -46.82146 | 2026-06-09 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29181f16-a794-3c24-8a9a-c8ba888a4e48 | -7.9052 | -47.08746 | 2026-06-09 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d354078-2d6d-3313-ad5d-60188c7551ab | -7.37707 | -49.85234 | 2026-06-09 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 831e1359-12f4-3b98-ab2c-b1b4515ead5f | -15.18124 | -43.8575 | 2026-06-09 04:49:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 169be812-4d96-35e9-9710-35d12e809b69 | -10.14727 | -47.64811 | 2026-06-09 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 926b60e4-03b2-382d-9d2f-867b1cfe2c88 | -10.89977 | -49.35483 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 700fe6d4-ea69-373e-b2d9-36909e795d8c | -11.55395 | -52.78492 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8ebd5682-855e-32a3-9a11-4bed9d7fb953 | -12.04448 | -45.29493 | 2026-06-09 04:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 464c982f-b116-39ee-b574-fa5a87f93621 | -11.47349 | -57.11678 | 2026-06-09 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a79b844c-c102-3fa8-8ca0-bc399d78d4c5 | -10.85438 | -53.74165 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f9977e6-8ba4-383c-8bbc-674fa6d3685e | -17.59105 | -46.64815 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4977e1ae-c6c0-3f19-863c-10f2a4e993d9 | -17.58173 | -46.65475 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 853c94de-a725-3ad4-a688-f42ec5949662 | -17.45114 | -47.18867 | 2026-06-09 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e570678-a72a-3a6e-b459-ae3b3df00f8d | -21.20308 | -48.52184 | 2026-06-09 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c327880-522a-33dd-bb16-5e78057e996c | -15.30127 | -47.54603 | 2026-06-09 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10d9628f-7274-3882-a818-acb529119efc | -14.29157 | -57.71289 | 2026-06-09 04:51:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21877d2e-0de1-39e8-b57f-7261aa58e557 | -16.72758 | -43.37034 | 2026-06-09 04:51:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe9f891e-7546-35e2-ae78-d6991f0aadd7 | -21.20765 | -48.5172 | 2026-06-09 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e659a575-e90d-3437-b9c6-6dcb9578ddba | -19.28268 | -49.73707 | 2026-06-09 04:51:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 274d8157-a405-361a-b94c-12d67f8436a6 | -21.54556 | -47.04306 | 2026-06-09 04:51:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a29b06b-b262-37fc-9a0e-e51bf3960e47 | -19.47409 | -49.57013 | 2026-06-09 04:51:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6b287d6-87c8-3cae-8dee-36d44f999626 | -21.20375 | -48.51663 | 2026-06-09 04:51:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55f05ac7-5985-38c7-afb9-740705a09716 | -16.70601 | -48.87644 | 2026-06-09 04:51:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7f79a03-be97-35bd-8f97-ffa5a6e8836d | -19.03002 | -52.80433 | 2026-06-09 04:51:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94d60f63-9813-37de-a53b-b2e8a05a9a20 | -17.58689 | -46.64753 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f9619eb-a741-383b-8ea8-69a8cf973008 | -21.71258 | -47.14008 | 2026-06-09 04:51:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a741743-8041-341d-8f17-36ac9ec2794a | -15.22496 | -50.85863 | 2026-06-09 04:51:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ebba2a5-3078-3b93-af56-f15d6247c9a2 | -16.54857 | -51.75 | 2026-06-09 04:51:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08c2b865-74af-3b91-a5b1-9b479cdee72a | -17.58956 | -46.65983 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 071330cc-94bd-314d-8477-12642a796145 | -17.58639 | -46.65145 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b162956e-b2c3-3e6b-8325-26ee47469106 | -19.90824 | -47.97926 | 2026-06-09 04:51:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96c27856-09fb-3b50-a8ab-f6c8f13c66ab | -17.59055 | -46.65207 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b22c080e-aa7b-3fc6-964c-7dc5d20f7531 | -15.18616 | -55.21992 | 2026-06-09 04:51:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd5b068e-26f7-38d0-9dea-c20ae7306474 | -20.28711 | -53.1288 | 2026-06-09 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 14f6372a-ec0b-3e7f-bafd-4622e2ff7980 | -20.69337 | -44.27859 | 2026-06-09 04:51:00 | NPP-375D | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 506b680f-3e2f-3a10-a3af-725098daaa5e | -20.05197 | -54.73079 | 2026-06-09 04:51:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c4238aa-942c-365e-bb26-5c4811692fdc | -15.22161 | -50.85807 | 2026-06-09 04:51:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4920319c-e90c-386f-b438-b74cf0d043a3 | -21.42914 | -48.64722 | 2026-06-09 04:51:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aee3818-86cd-31b1-8afb-18c60d4d3684 | -14.29262 | -57.71097 | 2026-06-09 04:51:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95600a8e-a674-3bb7-9c1e-17f26e332d78 | -16.12548 | -50.96968 | 2026-06-09 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd27e9b8-7630-365f-8ea6-2395369fc38c | -17.58589 | -46.65536 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e8ec957-8072-3b6f-9c4c-16fa112e2389 | -15.53271 | -56.04255 | 2026-06-09 04:51:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 012d3e75-25d7-3b4a-910e-7aee9038d7b6 | -17.59155 | -46.64423 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 308f596f-145b-3a50-9059-414a067809c1 | -17.44713 | -47.18808 | 2026-06-09 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7497e65b-769b-3726-a713-38657fe4619d | -19.90895 | -47.97378 | 2026-06-09 04:51:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44ee9931-041f-3fba-b317-d145b0ce5225 | -17.58223 | -46.65086 | 2026-06-09 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f53c544b-4d4f-330b-8f0a-94d207c8d7ea | -23.56354 | -47.51255 | 2026-06-09 04:53:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 758cbc11-fd99-38d1-92de-975fa138d90d | -22.96453 | -46.96236 | 2026-06-09 04:53:00 | NPP-375D | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b782164e-da80-3ea7-ac52-7097dc5a7ca8 | -23.01894 | -46.67475 | 2026-06-09 04:53:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9eee0a8b-b1fd-3f20-800d-3385b82cc7d3 | -22.80416 | -49.34891 | 2026-06-09 04:53:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37692d0f-b25f-39f1-8064-c108e2605e17 | -23.54506 | -47.63535 | 2026-06-09 04:53:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4f0f21a4-47f8-3336-8d82-137faa7163fd | -22.80035 | -49.34838 | 2026-06-09 04:53:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 400342a3-0544-3012-ac2e-f6084d2403c1 | -23.51588 | -48.56653 | 2026-06-09 04:53:00 | NPP-375D | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1e0a8cb-16c6-322b-bd44-48b25a9de50c | -23.01842 | -46.67939 | 2026-06-09 04:53:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3b994bdd-45bc-38ea-978d-d515032d46e8 | -23.78014 | -49.04184 | 2026-06-09 04:53:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77873f71-2eaa-3539-a0bb-33a1bbf8b7b5 | -10.6498 | -49.3834 | 2026-06-09 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| b9773869-07f8-3cb0-8dc6-53bce30ef602 | -13.2597 | -44.388 | 2026-06-09 05:00:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 679a859f-021d-3b7b-9c6d-22bc85865411 | -5.04371 | -43.2631 | 2026-06-09 05:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1c118874-62e8-38ef-af2b-298f2c4be437 | -4.6443 | -43.04673 | 2026-06-09 05:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c809b68-b092-39c0-afdc-c6de215394b9 | -4.64284 | -43.04895 | 2026-06-09 05:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29788b0e-cc40-3751-81d5-4d4f98bd5c31 | -3.49743 | -48.03433 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f4ed2c8-b115-3df2-ad23-7855fc1e0e37 | -5.04354 | -43.26616 | 2026-06-09 05:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04a9ed6b-b378-3b87-afa2-a30938699ca6 | -3.4956 | -48.03679 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b5c5eea-35ce-3043-9296-59e070fda363 | -3.49097 | -48.03588 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 28bc9c83-3dd2-38b1-88f7-dfa8470b9f5b | -3.50205 | -48.03517 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3912cf6-2620-38f7-8959-af608faf4b88 | -4.63693 | -43.05136 | 2026-06-09 05:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37355720-9190-3b8f-bef0-a09cbb70e66f | -4.63627 | -43.048 | 2026-06-09 05:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35e93862-cfd3-33ae-ba56-cbd6458f1c83 | -3.50022 | -48.03764 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0072fa94-05c9-3113-99b7-78118f51d6cc | -3.4928 | -48.03349 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1c00a9d-cda7-38e6-a9b2-b87c38d38956 | -3.49206 | -48.0383 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README12.md)
