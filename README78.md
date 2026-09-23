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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecf45eef-50fc-3156-81b1-20caf7da3a5b | -3.15914 | -57.69421 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| edb4398f-c5ee-34ee-9bdd-d6c97fb1b324 | -10.91714 | -53.95282 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e9c0131-fd5a-37a7-b0ed-e2a86280ff6c | -7.04604 | -62.93567 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 737a830f-06d5-3f6e-9db9-7538054b04c8 | -7.17617 | -48.62772 | 2026-09-23 05:04:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c11878b-db57-32e4-bd0f-8e8a1a492cd1 | -8.30929 | -50.81309 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5ed1a71-195f-359e-b647-bde105f66734 | -8.73621 | -54.97553 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4853bda-14e3-3554-9407-a5d17d1f723b | -5.88167 | -51.57156 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52751f76-ba37-3ab7-9df4-f96b15f03885 | -6.61078 | -59.94902 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a06ff80e-4c76-3bd1-acbe-9c98463d96a1 | -6.28198 | -52.95559 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 838df679-e70d-388b-b8d5-b9b6b1d11244 | -6.60627 | -43.73723 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 86d72bc7-c628-3148-833a-976441034077 | -5.99994 | -44.2583 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5796599b-9f53-31d1-b60b-2b894a823f2d | -7.14209 | -48.42577 | 2026-09-23 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72c4a196-f3d2-397e-8e07-f59e108c46b3 | -6.95359 | -59.82725 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84bf12f8-1954-3b56-8294-1419c50e7d1e | -11.42927 | -47.37733 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5cf1e57-dd16-31b3-8513-f1ee1e8dee5e | -6.4697 | -59.96759 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e79d5c51-6335-3dcc-8a61-18037749288e | -6.8914 | -46.54115 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd46ab19-3346-3d56-83eb-e9f0c49ce499 | -6.17879 | -52.80037 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7296fe9e-0e8c-3b93-abad-c47f527177c3 | -5.41467 | -49.26562 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 764b6c17-88f5-3eb1-ab88-e468ee04a957 | -6.38958 | -55.20129 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6232002c-1eae-3af0-9df4-091085cdd43d | -3.1609 | -58.12071 | 2026-09-23 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5ac68587-156e-3eca-96fd-73f63d3fbc3e | -10.45497 | -44.94773 | 2026-09-23 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d691aa8-83b2-37ba-884f-c2f238c4ac73 | -7.88313 | -61.18296 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09268c0d-bc59-3f28-9a03-05dc88196ea9 | -7.32498 | -55.59619 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 461e12a9-f211-3412-aa02-6fe8f2d2bd03 | -6.12836 | -59.93242 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4887eb97-f5e0-35e9-bb6f-ba9656cc8c75 | -3.90026 | -60.59148 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c654cfd-a23b-3465-830c-17bb257b7ea2 | -6.43603 | -48.45363 | 2026-09-23 05:04:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dcec01f-cdcb-31e8-aebc-5676dbda1cd1 | -6.09873 | -57.67955 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b971651b-de7c-3277-89f8-1e6848b03f53 | -5.92558 | -59.91471 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 6f62757c-b34f-3f20-9532-868c0025d952 | -7.43824 | -49.83971 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 452f2e42-ff68-33d0-a750-057d3955cec2 | -8.32896 | -50.82405 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d5e4649-5489-33b6-96ef-6d0bed0f574c | -6.89826 | -46.5552 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b737ba5d-1be2-355c-a05a-d35c84e476ba | -6.05566 | -46.35238 | 2026-09-23 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9d9795e-f60d-39eb-926e-e50531fd37a8 | -5.14668 | -60.30396 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 666fcdc6-5202-3f94-adcb-ff2239e0ae08 | -11.63515 | -50.9548 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b4ce8f5-81ed-36f8-b504-ab8f34ab9e04 | -6.2957 | -57.74339 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d5778e1-e6ba-3557-9827-a225ffca256d | -6.6434 | -59.92905 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 025de7ed-89e8-3709-b9a4-8caf9030ffa5 | -6.73178 | -55.07415 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ea01dc0-6f51-3a7c-b85a-dc12fc3f0865 | -6.57516 | -44.14773 | 2026-09-23 05:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1644338-5f78-32ee-aae7-8c14bb86e7be | -5.80245 | -52.09675 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8312c35b-f871-36af-843c-5d207a7322fd | -5.81154 | -49.15216 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8cd83b57-d269-3085-b4aa-c5c6e3828dac | -6.45561 | -54.9954 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8329a62a-8185-3574-a7c9-71603f41125b | -5.8312 | -52.04428 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 006de3af-e96d-3fee-92a3-eae4d2ac1107 | -3.82411 | -58.88305 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a20d34ec-b6a9-37f5-98ee-04c3b8492112 | -9.18553 | -65.86 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0dab505c-c68d-3584-9519-f73ae66242f4 | -11.29143 | -51.37508 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6a8647a3-cfac-3760-a7cb-eeaa3ac5ed96 | -6.11171 | -59.88808 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70e80e92-0eb2-394b-aaaa-17ac469cc6ee | -6.1277 | -55.8197 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8d7cdfa-59aa-39ef-ae3b-e1f0dd671eac | -4.45063 | -55.07633 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2631f6e-3a4c-3bc1-9bf9-73828ecd90ce | -6.30264 | -57.75201 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68d3294d-77b2-336e-8a07-71f02a9c8768 | -8.33184 | -50.82847 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d7fbb5d-ee70-3ae3-a399-be0609698ec1 | -3.10665 | -60.71626 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a18e339f-aa1b-3823-b2dc-46cc9704aaeb | -5.14601 | -60.30229 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b545d876-9315-3ee7-9433-de5bdf1cd34f | -8.58834 | -53.11361 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36d4ae29-163b-305b-a351-c3dfd3062d11 | -8.86231 | -50.19003 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9ba9686-1379-3134-8101-9b82400204a1 | -6.37829 | -42.79236 | 2026-09-23 05:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6aec0614-c81f-3b89-b556-fefea2ea62b0 | -11.63208 | -50.97528 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 336e3466-d1de-3d2d-87bc-49c213b580fd | -6.34233 | -49.87519 | 2026-09-23 05:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f8c92ec-962f-3834-b96d-6896f87e2f1f | -3.77036 | -60.72572 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e5fe951-8614-3285-beb6-b8c76cb6511f | -3.10772 | -60.70986 | 2026-09-23 05:04:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a195b8d-e555-348b-9c97-5d3f35f9d75d | -3.85707 | -58.82645 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 107ed102-97d1-3501-9d80-65fa519c64b5 | -9.86956 | -48.40005 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 96768f66-bec6-3aec-b1a3-905db1ee55b0 | -6.67639 | -55.05727 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 340f71b6-c129-3168-a87e-827132859dc2 | -8.19721 | -54.72142 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1d70587-db17-3a84-84d7-8f6a8e19d522 | -6.73145 | -55.09816 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 751317d9-9594-373b-b503-3d81db85d7c2 | -6.74324 | -55.09206 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfb6b2a0-daba-32cf-9ff9-8cdac365542e | -8.92531 | -61.48605 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e083f3cd-565c-396b-aad0-5d8e251aaf0e | -7.12927 | -43.07092 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 036f25f5-cb26-3f63-a1ba-5d62da181a2e | -11.12369 | -51.05161 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f96c28d1-13d4-3167-8bf1-d1aeb1e3d523 | -10.90876 | -51.52104 | 2026-09-23 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dcc3939-eba8-3f14-bba7-6c6ce43c904f | -6.88804 | -43.63485 | 2026-09-23 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 142d4596-76b8-3f36-a041-27794e2e69c3 | -6.68755 | -55.05903 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36730509-fb02-342d-a95c-12b6221f9d04 | -11.13042 | -49.45352 | 2026-09-23 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ff72bc89-7e03-3a50-9e45-de10209e7716 | -3.78625 | -60.75988 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b0470e9-f1a9-333b-9161-18fe08bfd904 | -3.07444 | -58.40107 | 2026-09-23 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 554ce036-4aef-3855-9ab9-14f750ae7203 | -5.89199 | -52.28167 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c7546b4-b411-3d2d-9c31-c0fb4fbf80be | -6.66317 | -50.94774 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b42fd03-5b65-3293-8ac1-468c32706c18 | -8.65719 | -50.11936 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbc2b21b-c7d9-3d14-ab45-f206da59ba4a | -5.61869 | -45.24424 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fc9f5847-b796-3da6-9a6d-6a2c38f82b9f | -5.65383 | -60.21278 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e056fc10-b9f9-39a3-abfe-e5d543367433 | -7.56216 | -55.0233 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d49b5f6-c1ad-38f0-b836-e68044510170 | -6.5743 | -44.15378 | 2026-09-23 05:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 160e28f0-87ee-3f4f-91e3-6d73ebf80413 | -10.96964 | -54.15316 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5af52b20-11c2-3c54-8efc-7a708c38faeb | -6.62169 | -43.7426 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0b7131c2-b7bf-3e36-9a76-6d5a7f501360 | -4.09245 | -62.09343 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ece22877-c5ed-3bcc-b01a-16eaeb8e21cb | -11.11956 | -51.05507 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a2877e6-2faa-329b-9b2e-2c9179affe25 | -6.11142 | -44.14936 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eff6c336-0d32-3ccf-b147-2dfb942fef94 | -6.67989 | -55.05785 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 50bb0bb4-235b-3e95-be51-1d559a12bf31 | -10.87402 | -54.09407 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cda150c-3025-3757-9dad-a062a75a474b | -8.25153 | -54.77588 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64a74dfd-cb95-30ac-9aa8-ff415d63e3b6 | -6.75153 | -59.06098 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04848e23-c4c9-3c55-8e71-03a469f6210f | -9.94219 | -48.47178 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1753f8d-5a28-30eb-ae01-9d0f47eda602 | -6.33393 | -59.96185 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35d4ed24-9461-3716-8b87-1f28fa05781d | -6.04489 | -57.82393 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13d3768d-d52c-327b-99c4-2b27b51f3486 | -6.17856 | -53.29012 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad49d6fe-9830-371e-b1f3-d97dac22df84 | -6.89385 | -43.63234 | 2026-09-23 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ebe65af-beb1-3e8d-b7d7-8c3ac3b639d0 | -11.10894 | -51.05343 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a055e265-f413-38eb-ba95-12d338820e6b | -6.61448 | -59.92235 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 9779f4bc-3945-3265-8f70-e4a783096228 | -6.66815 | -55.0638 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cd8cbf81-af2a-354e-b09e-6b6f9fdee4a0 | -3.19073 | -60.4351 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff6df57-a334-35b5-8f58-bf4c6cd0276b | -8.38305 | -45.59283 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README79.md)
