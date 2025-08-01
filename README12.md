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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5fce765-59f0-3f1d-bb98-5e28e799f01e | -22.59441 | -42.10415 | 2025-08-01 03:53:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1369b5cc-5170-3de7-bd02-9c31d085f833 | -20.44426 | -46.43077 | 2025-08-01 03:53:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4aac48a0-0469-33df-af25-946c71fc1a27 | -21.14025 | -42.02758 | 2025-08-01 03:53:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4352c9d5-f2e1-3f37-b2b5-ba2dade1ebf8 | -20.6128 | -46.04123 | 2025-08-01 03:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15c1de94-ed39-3970-bf5a-05c776e5b4d6 | -19.45578 | -45.30765 | 2025-08-01 03:53:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16ca234a-8fde-3abc-89e9-30c6c6c151c4 | -19.70678 | -46.79889 | 2025-08-01 03:53:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e43f5bb-f328-38d1-ad01-10becea28536 | -20.43839 | -46.43101 | 2025-08-01 03:53:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c56e88d-d430-3192-bae5-a3e78623e7a5 | -20.01532 | -47.38374 | 2025-08-01 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c72af84a-92f2-35b3-9361-a8f49be3117f | -20.61262 | -46.03936 | 2025-08-01 03:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7200bd99-63ee-3ca2-b76f-c354e348981a | -19.48679 | -43.8542 | 2025-08-01 03:53:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe37bb74-df26-37ac-84a3-2ecffaf703a1 | -19.45386 | -45.30723 | 2025-08-01 03:53:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edd96a85-7e08-3b0d-b878-057431873f40 | -22.63046 | -47.20061 | 2025-08-01 03:53:00 | NPP-375D | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39694fd9-df6e-395f-a181-da6e6ad7e739 | -20.52989 | -46.10836 | 2025-08-01 03:53:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ecf35aa-58e2-3649-9251-fa6d617b13ca | -20.45022 | -46.42332 | 2025-08-01 03:53:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff272def-1522-3a3a-837e-90296ec4b3ef | -20.4451 | -46.4265 | 2025-08-01 03:53:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f67c8a48-fc07-3e3d-a9e8-2043af337787 | -20.45533 | -46.42015 | 2025-08-01 03:53:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab206926-0761-34ca-9fb4-b6ba0d98681b | -21.47676 | -46.71199 | 2025-08-01 03:53:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6e5429d-942c-3f32-b42e-66ab3788cca5 | -22.05015 | -46.81225 | 2025-08-01 03:53:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b4c2c27f-8b8c-36ee-a403-4e324bf55534 | -21.24795 | -48.56855 | 2025-08-01 03:53:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f640e5a5-9656-31d3-b02f-3ccc927b191e | -20.43913 | -46.43399 | 2025-08-01 03:53:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49f8ffe4-a640-37b1-bb5e-24dd55c49b43 | -19.45039 | -45.9991 | 2025-08-01 03:53:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0561273-15c7-38ab-89af-bb9428c06c77 | -20.44338 | -46.43517 | 2025-08-01 03:53:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bd2f98b-2a10-3bc0-bf5d-41d28b516e4f | -19.96279 | -44.6908 | 2025-08-01 03:53:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 624a6c69-5ac8-3345-ac42-3cd1dc7b047b | -22.71246 | -43.76586 | 2025-08-01 03:53:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b6692f6-d02f-37f2-9411-3aed8c38eb60 | -19.801 | -44.65385 | 2025-08-01 03:53:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7ab474c0-62bd-36ed-9280-2ad53de44dfd | -20.44085 | -46.42533 | 2025-08-01 03:53:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfa35e21-9892-3e14-8097-092742cd4f4f | -22.51391 | -47.21742 | 2025-08-01 03:53:00 | NPP-375D | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 236e6a75-ed72-35cf-9efe-d3848c6062a4 | -20.01193 | -47.38508 | 2025-08-01 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 311b9279-32f0-337b-be0f-3a6348fb9888 | -22.51822 | -47.21861 | 2025-08-01 03:53:00 | NPP-375D | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 463fec2f-c3b4-36f1-8ad5-a496d3ad87f0 | -20.38394 | -45.50232 | 2025-08-01 03:53:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13fecaba-475e-30b2-8873-a631f8082e46 | -20.45105 | -46.41915 | 2025-08-01 03:53:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 792e7fd3-0979-330a-b0f2-bd957a444282 | -19.70431 | -46.79699 | 2025-08-01 03:53:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed348ec-00b7-3fcf-8fe4-7c96678d2e4b | -17.82816 | -44.57791 | 2025-08-01 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c91ab4f-8e29-3fb3-bfa2-ddfd794bfa6c | -16.68458 | -49.39311 | 2025-08-01 03:53:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90e58743-98da-35d7-97f8-fbf7720630f4 | -16.3607 | -49.48688 | 2025-08-01 03:53:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adec3881-2cca-3315-b94e-7ba3800320da | -17.67866 | -44.43811 | 2025-08-01 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 744480fb-f2f9-3ca8-a1c2-9508ecfd8ce4 | -18.5434 | -46.69003 | 2025-08-01 03:53:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8da02170-705c-3b3a-9303-d0b32ff82755 | -18.44616 | -46.92211 | 2025-08-01 03:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21275374-18d8-324d-8738-86abc55219b6 | -18.21633 | -44.71478 | 2025-08-01 03:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00120fb9-6b6d-3e12-9a8e-9eaa507070e0 | -16.69015 | -49.39438 | 2025-08-01 03:53:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51055c50-2193-3d84-94d3-4321950a7da1 | -18.53737 | -44.60538 | 2025-08-01 03:53:00 | NPP-375D | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bc10716-de3c-3546-8351-0ff274f15e04 | -18.45079 | -46.92298 | 2025-08-01 03:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bde9873a-843f-30a1-9d87-f2adf6e18926 | -24.52274 | -50.7929 | 2025-08-01 03:55:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f02c0485-706f-3d20-a544-f98532629664 | -23.5252 | -47.8321 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| c6b9fb9d-a6aa-3249-8f84-fa3df73e1270 | -28.31566 | -49.55433 | 2025-08-01 03:55:00 | NPP-375D | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e864b8e7-e679-32da-9487-75f7775c9be4 | -28.64656 | -50.02174 | 2025-08-01 03:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 36ca33fc-1c23-3ca1-930f-95ed8b70d84f | -23.5198 | -47.83591 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.6 |
| d87ac26d-cc6e-3ab9-b254-75d6912266ee | -28.18455 | -49.60769 | 2025-08-01 03:55:00 | NPP-375D | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 10c22934-e861-3432-a4e4-42de6f7ced72 | -25.09884 | -49.51255 | 2025-08-01 03:55:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4ba16a71-53ff-3e8c-9948-421a517dd246 | -23.12782 | -48.78305 | 2025-08-01 03:55:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56999e6e-e54b-3914-8c02-5be3a644671e | -24.52713 | -50.7977 | 2025-08-01 03:55:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a8f8cef2-05a1-353f-bc8b-d74b6dc32842 | -29.28757 | -50.49207 | 2025-08-01 03:55:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c3c32441-90ac-35e8-a462-3ff286d8a840 | -24.52231 | -50.79647 | 2025-08-01 03:55:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dee9d147-aba1-314e-bb87-afb0e0e65d40 | -23.51534 | -47.835 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.4 |
| 4d26800e-181b-3502-aa22-8513f41e1560 | -22.95584 | -49.12475 | 2025-08-01 03:55:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1f91f38-f870-36ee-8a75-6a67ebde02b1 | -23.5179 | -47.8325 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| 93a595d3-18ac-3600-9181-e2c67bfbe640 | -23.5319 | -47.07079 | 2025-08-01 03:55:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b3479c2e-0e0a-3739-997c-6b311b94d375 | -28.25262 | -49.71262 | 2025-08-01 03:55:00 | NPP-375D | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0bc4c7c0-ccb3-32f4-9a20-46a0c081b011 | -28.64238 | -50.02304 | 2025-08-01 03:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 14540da0-ff56-3b58-84da-165f8aeec619 | -23.52678 | -47.83446 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f753cb14-9ba2-310f-bce2-c25a8ce5b442 | -28.18464 | -49.6089 | 2025-08-01 03:55:00 | NPP-375D | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e225c0e2-338e-3f5f-ad40-03fe483ba700 | -29.07191 | -50.92673 | 2025-08-01 03:55:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e29efe8-3589-3be8-9516-43deec49ca63 | -22.70086 | -48.0465 | 2025-08-01 03:55:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42fa52ff-d829-305a-8910-7c4b32e1e8de | -23.51632 | -47.83014 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| d7bf9156-d1ea-3595-b097-a6e0cf06f90c | -28.98063 | -50.44667 | 2025-08-01 03:55:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 91c267d4-35d8-33b2-880b-5560139bb199 | -24.522 | -50.79615 | 2025-08-01 03:55:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 238cf9da-83fe-316f-bfde-549718d0ff25 | -23.52134 | -47.83827 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| a3f3bcaa-4fb4-31a3-9761-d7de6be2b6de | -29.2891 | -50.49341 | 2025-08-01 03:55:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0433b352-eb08-3bf6-88be-11679a43f5c7 | -23.52424 | -47.83687 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.6 |
| fff613da-fe30-36f4-b35c-fa7067762457 | -24.52744 | -50.79805 | 2025-08-01 03:55:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 743d9a7d-55bd-3043-9111-edbd97f4629d | -23.52077 | -47.83107 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 0cc94b68-ec97-3275-ae77-b8d35890f303 | -28.28809 | -49.90029 | 2025-08-01 03:55:00 | NPP-375D | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4b513698-c81c-3a87-8ea5-7fb1b9e1b554 | -23.51688 | -47.83737 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| 69e9374a-807a-302e-999c-588713f34bcc | -29.20496 | -50.7772 | 2025-08-01 03:55:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5f9b6342-0ece-320f-86cd-f72b3b744ae3 | -23.52234 | -47.83345 | 2025-08-01 03:55:00 | NPP-375D | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| a145ed7f-afdc-3985-976b-533e90bfedce | -22.96068 | -49.12595 | 2025-08-01 03:55:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab9a6880-41f9-3df4-a26d-b7ba7745f9c9 | -29.00636 | -50.16386 | 2025-08-01 03:55:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e7761855-357e-3b05-88ec-f6bf4b42e4e1 | -6.7478 | -59.1716 | 2025-08-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 39796faf-a6fa-3daf-98f1-2ac13560e156 | -8.051 | -43.1237 | 2025-08-01 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 3f284682-3c81-3b1f-9042-81e0db4ed5fe | -6.7295 | -59.153 | 2025-08-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 7db3a206-7039-38a0-b9da-cff0935c5b6a | -8.0321 | -43.1257 | 2025-08-01 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 176435de-172e-33e2-ae85-a191ce083bd7 | -6.7294 | -59.1723 | 2025-08-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 232.6 |
| de703706-c514-3d48-a6d7-0a4dd86f9087 | -8.0513 | -43.1001 | 2025-08-01 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| d87d50f8-e806-380a-9c25-ab1cf8d9f5ff | -6.6328 | -59.9841 | 2025-08-01 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| fd944251-1f64-3ebc-894f-e12d340df3ad | -6.7477 | -59.1909 | 2025-08-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 751886be-c36a-36d8-be5f-47c5c5aafe42 | -6.7293 | -59.1916 | 2025-08-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 569e4769-388b-3208-9074-76ac6d053793 | -6.748 | -59.1523 | 2025-08-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 7997d9ff-6c74-3a95-b56d-e252e565cad9 | -8.0324 | -43.1022 | 2025-08-01 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| b10cde53-2c01-3e6f-81d2-0efcb5db8dba | -6.7478 | -59.1716 | 2025-08-01 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 26fc5109-96b2-3276-b821-d1a2b2855b30 | -6.7295 | -59.153 | 2025-08-01 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 1a04b9ef-e62e-360c-a47d-04ec1643de39 | -6.7294 | -59.1723 | 2025-08-01 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 269.7 |
| 81086397-c4ca-3718-9904-bd08718c2137 | -8.051 | -43.1237 | 2025-08-01 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 2a5ed4d8-6671-398c-bdac-08b1ed703afb | -8.0321 | -43.1257 | 2025-08-01 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.1 |
| ab756f84-4c45-3b07-b3d0-ea2569a1c6e4 | -6.748 | -59.1523 | 2025-08-01 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 8dcefe0f-b169-378a-91c0-e6bd3b640b98 | -8.0513 | -43.1001 | 2025-08-01 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| f33977a0-dec2-3e76-98a4-d24fd32d7fd8 | -8.0324 | -43.1022 | 2025-08-01 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 7de56433-5794-33b0-a01b-36f7df0bf838 | -6.7293 | -59.1916 | 2025-08-01 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0c46714e-bd30-329c-a371-5f8099ce6b99 | -3.50257 | -43.24365 | 2025-08-01 04:12:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a52b6417-8612-3282-966c-15711466e0ca | -5.48441 | -42.15684 | 2025-08-01 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ead473bd-91d9-3df6-b677-6eb70e22f53a | -4.30679 | -48.1013 | 2025-08-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README13.md)
