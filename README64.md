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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f8468c8-2ccc-3b73-9e0c-3135176ff982 | -9.65839 | -43.85682 | 2025-09-28 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b736d92-285c-3cd0-92cc-2f3e1478a255 | -10.17064 | -49.36956 | 2025-09-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 661c04eb-c987-3abc-828e-f5644c8a7730 | -11.41262 | -46.94988 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c1151c6-105a-3cc5-9a8b-7653e3dc0b86 | -6.61445 | -45.08519 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea7da70e-13fc-39c2-be25-857860dbd9f7 | -6.89883 | -45.70132 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0981921b-1297-329f-b636-2c0e10ccd10f | -7.119 | -45.06775 | 2025-09-28 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae33083e-fa93-3bd2-9d9c-b0d20df49df4 | -6.40201 | -42.90438 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 91fe33bf-0ee1-34ee-8589-d556a726bd1f | -11.44114 | -44.99965 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23d6a869-f94e-396e-adee-7063af5cb097 | -10.80119 | -45.36712 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b507d113-f3d2-3d05-8f73-d366c73c01ea | -11.95014 | -47.91264 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b17ac348-6955-3c8f-9b4d-941a9799dbb1 | -12.88681 | -47.0957 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42d4b331-3aa3-3666-abb8-11c3b96a19e7 | -10.18491 | -44.83387 | 2025-09-28 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb677e5d-efa9-306d-ac8d-0174d6422eec | -6.70652 | -44.57978 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ae0acad-5d51-38f7-a7f4-0ca10ed8c5be | -9.75313 | -45.7884 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e77a696f-0c0e-347d-a779-d632f45b9207 | -8.18044 | -46.38401 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e8f57c2-1e84-3632-b188-89cb72fb9a23 | -6.64922 | -43.87673 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24829fea-618a-3dd9-9537-ef48a1a5fdf5 | -8.47964 | -47.79465 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02786f8e-048a-3b50-982b-c8c05c1db28c | -6.48736 | -44.25193 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dab58c7b-c079-3985-8531-c3a8c00a0deb | -8.49756 | -44.7277 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 414d58cd-1f66-3c3f-bdab-01bb4d13dbf1 | -11.51187 | -46.94412 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03fb08f8-2268-38e2-8aaf-7ff55bdf7f0b | -6.15553 | -42.80519 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c2ed3ef0-9f76-3e63-8448-c69b5efe2b6c | -7.38089 | -47.03662 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7da4e19c-2c1f-3297-adcc-e8439029a726 | -9.35904 | -47.62815 | 2025-09-28 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0efb7bdd-ab11-3cc8-9fdd-b9e3c566ec66 | -7.24618 | -44.75853 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac0b689d-5ee9-33bd-b796-e5653a309a9b | -7.37314 | -47.04253 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c2d7a22-5037-3b5d-9396-a80bd0c7690b | -6.98858 | -43.78248 | 2025-09-28 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2f2ef07-e50b-3afd-85a6-a1e6fc0131e1 | -11.77749 | -43.76305 | 2025-09-28 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a12a6d46-8114-3f55-b317-19ab8dd22e9b | -6.4889 | -45.9108 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad8c1309-8a73-3c00-8edb-da235586c7ca | -12.0061 | -47.98686 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 171e7acc-3131-3a01-a8a1-47e5fbec4959 | -9.07932 | -47.59322 | 2025-09-28 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 542062e7-7feb-3291-94f1-36cd6d51c94f | -6.20873 | -42.84758 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 98af3c64-43ae-386d-9fa7-9250fd590464 | -11.60054 | -45.44857 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0c8e5ac-1d1c-3c9f-b57a-ae7f134aa53f | -6.54382 | -43.8229 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fc87599-35b2-3bd9-b457-fba76ef12e64 | -6.61165 | -45.08115 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9e8582f-acbd-3a72-b9a6-99071bf9ea00 | -7.75767 | -46.99673 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92335b7b-0f09-36f3-af54-b31d6ba0792d | -7.05765 | -46.41868 | 2025-09-28 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b73db204-ad59-3f3d-97ef-fad3060c01b4 | -6.42776 | -43.07566 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9973a4c2-7753-3268-a4c4-8f975db5735d | -7.02948 | -44.75537 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b4adf93-fe1f-3972-bb30-b2e03756b4f6 | -12.88986 | -45.17313 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 721e4e0c-dc76-3705-87be-556ada642cec | -7.75104 | -46.99567 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d29ea6af-e8e2-30e3-8e70-ab9e843a1499 | -8.47258 | -46.42739 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86f50ba1-7317-3e21-957c-ffa685ac963e | -5.39721 | -45.85531 | 2025-09-28 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96e34479-9d1b-34d9-9881-bbf124c4bfd7 | -12.00362 | -47.89587 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a51e3bc-54b1-3903-9563-b250b90108a5 | -8.28276 | -45.44389 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df2383d2-65b3-3877-96b4-b1e482d0a617 | -7.37205 | -47.02805 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bcd92a5e-d14e-34c6-8ac4-d8266f4d7c0c | -6.20081 | -42.85075 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33c42cb5-8b10-3b88-86f7-9c5166b491e8 | -11.96926 | -48.00634 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75d4ba5b-8c55-3914-9cb8-6222f1e0cb0f | -12.00199 | -47.88477 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3172e37f-5ce1-34a1-bc79-52a0497b14b9 | -5.59762 | -45.13998 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80369376-e3a0-3354-a207-d1953e0313ec | -9.29764 | -45.70325 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebbac081-6971-3caf-bb3a-64e16ac49403 | -9.35628 | -47.62408 | 2025-09-28 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef876beb-c445-310b-892f-4de9cc80ab56 | -12.02174 | -47.93148 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06c390ce-0242-36e5-b73a-959869d2a9e4 | -12.93068 | -45.16319 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c13150d2-b9a3-345c-8cf9-9f5f0c1f1891 | -8.64067 | -44.8441 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d1c665f-4440-31b3-bacb-2b487c3b6102 | -11.37982 | -44.93383 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8a039ae-a561-3caa-83e3-132c4c628159 | -11.38721 | -46.93857 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf3f6bfe-0b2c-386d-9b7b-b73d43ed8dc7 | -12.0003 | -47.89533 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9a18cbd-e550-3850-a0f6-f424cd51091b | -9.90826 | -58.56742 | 2025-09-28 04:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8115bb9d-52bb-35db-971f-574233a2089f | -11.44701 | -44.98436 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 604dffa3-be37-311f-aa1c-39602d1c87a0 | -11.42911 | -44.9615 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1475afa-20fd-37eb-898a-d62ec8a2810a | -10.41906 | -46.15583 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a93152af-6174-3cd1-ab95-5421e9127995 | -11.95661 | -47.97889 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e5552d4-3525-3312-aeec-f1c2fcd1f568 | -6.78284 | -44.08417 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 82f82c8b-f2f0-392d-9fbe-1fb917613e80 | -6.78522 | -44.04559 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59529cdc-f7a7-3bcf-bb57-ff03c9d7b4be | -10.7196 | -48.0007 | 2025-09-28 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 885b4fbf-7263-3208-aa08-49d9ecc06ee8 | -7.00248 | -45.62444 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 62211322-9086-3c07-8850-3e1c168cf21e | -7.15276 | -45.5076 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eca3748-b336-38f3-a661-452e40273d73 | -10.19711 | -58.22468 | 2025-09-28 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e34477bb-1ad2-3fab-b11b-2397933d6534 | -12.00581 | -47.90346 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31b5ccca-86d2-3f7b-a31a-74af2413a7cc | -6.40005 | -43.95769 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae12281e-2d67-341b-8e96-ab4552fb59db | -11.36996 | -45.02447 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a5acef0-9a22-3d16-b037-69b0c8835c81 | -11.4241 | -46.63717 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4fda955-16cc-3765-afac-01f4463b7d8a | -6.50483 | -54.86821 | 2025-09-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 325a09a9-a510-3baf-a293-0c593573a605 | -11.61973 | -52.85904 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23b465c6-3e94-3a77-a3af-136cc946be30 | -11.14349 | -54.31395 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bd5c6740-67d1-3692-996c-908961bb3112 | -11.98502 | -47.88577 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6249236-b508-3d12-8a1f-1256aa4a4fec | -11.35504 | -45.05334 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d68193e6-87e4-3a35-a3b5-ea619518f2c9 | -9.28824 | -45.70565 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56f9ebb1-5f24-35de-8d73-52ef11907289 | -7.37592 | -47.02509 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8d53246c-b1c6-3c18-8ea7-699d47583d8a | -7.37757 | -47.03609 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba8dba85-4a38-345f-916d-e31fb47337b0 | -12.89235 | -47.10385 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cebd28b8-717a-35d2-aae9-6647665b897e | -6.54126 | -43.82563 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71ba16bb-7698-3ac7-997e-dbf157a2b57e | -7.32228 | -45.98868 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b0597e3-a762-33cc-9885-5fa972a54027 | -7.10342 | -44.23227 | 2025-09-28 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fd2bd44-b8f4-3a75-a9f4-d823779f7ec7 | -11.60547 | -44.38308 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c10f7cf-6a00-367e-ac1c-2719cba184c5 | -7.38033 | -47.04012 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87dd212a-1dd4-33d7-afcc-b526a3538d7c | -10.0043 | -46.70686 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38ee253b-68ea-3784-b804-19cd08b4b2ca | -10.29526 | -45.40057 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6902516b-a6b7-3e03-aec6-fc6505900ce7 | -12.69181 | -45.47512 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb6e01a4-7479-3052-872b-d1092239988f | -12.00087 | -47.8918 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ac7b8d6-d934-3826-a97f-9b7c379af626 | -6.54591 | -43.81842 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f778e57f-5628-3d06-aa8a-80ec1a061645 | -6.53621 | -44.9786 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1343a23a-bc60-3350-a4d3-6dfb1fe1a75d | -5.88147 | -43.19511 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 26fad0be-82aa-34fb-b755-d7a36f4426d4 | -6.02012 | -45.41396 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c94ccfc5-4625-354d-9907-7f53972fa5ac | -12.97804 | -46.90256 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2919b4e9-4309-3f00-82b9-9ff20e4b2977 | -11.99586 | -47.90186 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0b2dddc-22b8-3d02-91ae-18fc7f77ecb2 | -6.1549 | -42.80945 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e80bfc5d-a709-3735-b6ce-b8bd981baff7 | -9.67695 | -44.52326 | 2025-09-28 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2614eba2-628b-30b2-a23e-da6caf95208d | -10.76768 | -45.38108 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 025704b5-0974-38e7-abe5-0f456b36d33a | -7.16717 | -45.50265 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README65.md)
