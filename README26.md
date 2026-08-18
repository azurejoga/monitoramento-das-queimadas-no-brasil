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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d38dc34-68c1-3141-a082-315a68e61434 | -14.04895 | -53.68784 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2d32b77-126c-3248-8c92-47eb4a616067 | -11.3609 | -46.39382 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 649b84ff-aa3b-3c6b-945a-91819cc4ee57 | -14.03998 | -53.69019 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 576c62ee-f92c-34ed-9291-d762ef55702d | -16.26893 | -49.30199 | 2026-08-18 04:40:00 | NPP-375D | DAMOLÂNDIA | GOIÁS | Brasil | 5206800 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 45eba8a0-56d0-3f14-9a19-ddbfa06ec263 | -8.89968 | -60.55307 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 347239ce-eece-3f42-a706-3b58bfef6e75 | -14.28007 | -51.93244 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a34cd57b-b279-3631-bc44-1f54a5b03cb4 | -9.42746 | -60.43676 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f759a5c-6bda-3845-b93e-ba5832cabaa7 | -12.70496 | -48.51907 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e65ad12-19d0-3baf-a536-2c957266d70d | -13.4254 | -54.39352 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36b4306b-bf46-3fff-b6a1-c5931fb60de7 | -15.22612 | -57.65039 | 2026-08-18 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 993ee8b0-e415-303f-b404-c6ec312c93c3 | -14.17422 | -52.93515 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 348885ba-5578-3864-963b-ef38d9cf8527 | -12.51482 | -47.86589 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5fd2fb9-f77c-33b0-8091-ab6cbf0c7e9f | -15.08353 | -48.69564 | 2026-08-18 04:40:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ea22486-e5c8-33d9-aca0-8e5719bddc16 | -14.81804 | -46.6349 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d3272189-3696-3596-be51-c67e8cf21945 | -11.12811 | -47.28329 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 395a1020-8dfe-3a17-ac35-afe0668fa3eb | -17.3541 | -45.61905 | 2026-08-18 04:40:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08ac9f61-e07b-3f08-86ab-0f49c787eae8 | -14.87373 | -46.63622 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 070360dd-90ad-39d1-98c9-4076edcad943 | -12.70553 | -48.51551 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a7fe5a8-e789-3d69-8640-489b824f71db | -14.17686 | -52.92782 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c139fbc-9507-3408-a5b5-81593ed9615e | -14.36009 | -51.87622 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88cce9e9-d9fc-30de-886b-66a3ca84fe75 | -14.16688 | -52.91537 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bfb686a-3cfb-3650-b584-3feae073138c | -12.46729 | -54.17865 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23aa5ae2-0d2a-38d1-b9a3-dac42c9c87d8 | -13.41624 | -57.04266 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1986f20-e357-3e51-82fb-5c50df828ad0 | -14.3593 | -51.88069 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6ff6d64-bc3e-34ac-bb03-610ff7c0e9d2 | -9.42579 | -60.40971 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75e04d78-9cdb-3cc4-a9ca-b7b8ababebf6 | -14.35535 | -51.87215 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cdca4f4e-80b2-31ea-bb7c-31872ed71c89 | -9.42937 | -60.42673 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a12c95a0-261a-3d29-9faf-c0dcd36d08a8 | -14.03172 | -53.6887 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fb2c115-b5b9-3388-8e71-56498795eb48 | -11.52166 | -46.63231 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4492e45e-7f8b-3952-84af-ed9e8c180a20 | -16.22809 | -57.6477 | 2026-08-18 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e10b77ec-9138-3f99-a24d-09a01cbfd856 | -15.24637 | -56.48657 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae45c85a-9885-3faf-ac05-91ab9b3bfc07 | -11.24578 | -54.82824 | 2026-08-18 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53710499-ecdc-3510-bdc5-3443408167b5 | -14.8339 | -46.64552 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 843fd59a-6b8d-36f1-bd3d-5233e1e074c7 | -10.26773 | -50.4101 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb558ade-cc4c-35c1-9f34-053e1bca4923 | -11.31959 | -55.22548 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a62cb4a-ebb7-3d7d-8f48-5910ba11a825 | -11.35469 | -46.38153 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df36ffd3-8531-308b-b03b-9b69723fdc71 | -11.52778 | -46.63704 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7bc8192-a271-3e1b-9568-83e1241dbb8b | -14.05305 | -53.68872 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c9d7ff1-6639-3bd7-8172-071451e7e655 | -16.5738 | -51.62259 | 2026-08-18 04:40:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32d1ca66-5a85-3b45-be3e-fabf4fe95602 | -11.47362 | -46.56613 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 094d7f92-6657-3205-90b4-3bcaf19fc7f4 | -13.41039 | -54.32827 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc0289c-a3e8-3cd5-ac57-7cbf334ca774 | -11.82162 | -56.60537 | 2026-08-18 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69ae5fbe-53c0-3efd-9ac2-6da55a9d675a | -11.3065 | -46.33698 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b036386a-839f-3af2-b153-6e4e3502250d | -11.5323 | -46.64098 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf3cc24f-c87d-31bc-a361-83b56362d693 | -12.39997 | -54.95544 | 2026-08-18 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6eaf3fbb-3ec4-3fd7-b899-23fe27cd6683 | -8.90397 | -60.56791 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddbf305f-3540-32c0-b3ee-d22bdaca6677 | -18.24623 | -45.20374 | 2026-08-18 04:40:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3489c2c-9240-3ce8-9b1e-5f8fa5028617 | -14.85269 | -46.63672 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e52a0e2-ef7b-3859-8ada-0a3a7c237a1c | -14.35798 | -51.86661 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aa2f3636-dfe3-3c1a-ab0d-5070be5b0a26 | -14.42436 | -51.8788 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c70559ad-e6a2-38a0-a7bd-5e5105e6358b | -14.1839 | -52.9265 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3e7b11d4-0c46-34e7-be26-7cf9afdd1aeb | -14.03508 | -53.68523 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa15163c-6f69-3edf-9e24-c515fba568c9 | -14.16728 | -52.92862 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b880f2ab-fe10-322c-aaf7-e726d9e25cbe | -12.39819 | -54.96532 | 2026-08-18 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa81ffde-7794-388c-8c45-701ba65db300 | -8.96175 | -60.53114 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2988f83b-da93-3ab4-b458-437b4aafa7ad | -12.72917 | -48.45351 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bba109bd-440c-3a00-9be0-f4fd983c2a53 | -10.56606 | -51.97368 | 2026-08-18 04:40:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55a195c5-854f-375d-80b6-beb896b31d5c | -14.17079 | -52.91619 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8bd6c054-dbcc-309f-b000-b16dd1badbdb | -11.53285 | -46.63745 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2738aa2a-7f7d-30cd-89a2-20b256a1109b | -17.45932 | -47.86081 | 2026-08-18 04:40:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20431b90-7abc-3efd-bf3e-5dc8b4e2d1fd | -9.42503 | -60.41247 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06a38346-e233-3ffc-9ea7-9173bf88c9dd | -11.29808 | -46.32452 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f0c2099-54b8-3f36-8a19-2e6d20369d73 | -14.25123 | -51.92248 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5c69012f-12df-39ac-ab0b-fa45cad4ba7b | -11.12867 | -47.2798 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed8cb495-89e8-3f5c-b469-55005c7c9900 | -15.9219 | -56.49927 | 2026-08-18 04:40:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 685f966c-e1d9-3fdf-b473-55c18a088c76 | -13.44606 | -43.84219 | 2026-08-18 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2c3be5c-e4fc-3d8e-a73a-eb8b6a87c182 | -11.7227 | -54.61779 | 2026-08-18 04:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd6e2a55-3845-3ee9-adb1-5660d77d043f | -14.6269 | -54.46203 | 2026-08-18 04:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5572942-3081-3b01-8dfa-dc21ec1aada5 | -15.92011 | -55.54021 | 2026-08-18 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf99344b-a948-3a7e-b3d5-ea74584521f6 | -13.4585 | -51.79863 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc717869-eb47-3b56-86e9-7e9ff0b88e6a | -12.39795 | -54.95854 | 2026-08-18 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 07294e66-f14d-3c1b-a185-8b9bf6c25bb4 | -11.33569 | -55.27278 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 343f5d5e-1b4f-39b1-98db-870c39942c8d | -11.38723 | -46.40164 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f14bf5cd-92a4-38f8-ac64-58878015d782 | -14.35591 | -51.92147 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdf16643-f4dd-34dc-af95-9d7d231bee8f | -15.27741 | -56.494 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95445bc3-3ab0-363b-8bbb-691962f00d2c | -15.38676 | -52.79115 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce5fec13-0463-3511-a2e9-68bfac23093b | -15.23003 | -57.65818 | 2026-08-18 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c2541cf-e28e-39a1-a7da-68221e8937ee | -14.35981 | -51.86835 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dfa3d5e-7c8d-3447-8602-6a0aa1da6d68 | -17.10475 | -46.57673 | 2026-08-18 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4de1ac5-27b4-39a4-a0d1-584045a952cc | -13.42613 | -57.07462 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47518082-ca2f-37d4-995f-63b74a9fcb2c | -15.64674 | -54.80877 | 2026-08-18 04:40:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa93d9e3-7088-3c60-847e-5c0508d9a1b5 | -9.16821 | -59.69906 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23eafbd1-3311-3662-96eb-2b9b00e79ae2 | -14.84243 | -46.63526 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e249349-bd71-3202-8bb7-de7ff0cf8962 | -13.41474 | -54.37787 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 10f2e148-842e-344a-9cb1-6c9a3740783f | -13.55064 | -51.69316 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c1615d5-7f8a-395d-824f-070b75b32104 | -14.16869 | -52.90504 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b024dbe-60e7-3ab5-b489-abbbdb498d21 | -17.98426 | -44.43009 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26d7950e-6b1f-3992-9c63-06efa554badc | -11.12548 | -46.49614 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c87c13f-1fd9-3e3e-a042-7136852c9ea7 | -11.34216 | -45.92358 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 635164ee-0685-39bc-9493-c80e7019b6bc | -14.03853 | -53.68985 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce67abf6-e0c3-394a-a2a3-c025f72994bb | -12.01088 | -46.49846 | 2026-08-18 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88442a7d-8cd0-399b-854d-db65e75a5a53 | -11.14139 | -47.28545 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97e50231-fede-3e1e-b584-b1e651e6f4d3 | -14.15699 | -52.90245 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb51edcf-c806-3392-a591-4f850c9799dc | -14.49998 | -45.67372 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01f704f6-80d6-32bf-ba60-4e5ef2cfd8a4 | -14.83622 | -46.65326 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f305e99e-c5dd-3db2-9f64-296ba4164053 | -14.17789 | -52.91491 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d1b522b4-40ec-3380-9f5c-f42865aaf73b | -12.46415 | -54.19579 | 2026-08-18 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2fe953b-39fb-3171-a632-95926a22a1aa | -11.35643 | -46.40049 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80c2df75-0a03-31cf-aaf7-257c359eee2e | -13.41988 | -54.32558 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2c2a322-14a8-3c64-8f30-204b076ebcc6 | -14.44466 | -51.82728 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README27.md)
