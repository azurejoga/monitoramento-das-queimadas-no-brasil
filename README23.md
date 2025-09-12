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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 582b1cdd-338c-31e2-9798-8bdce52c7777 | -18.65593 | -47.66136 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32653103-04ac-3455-b164-af8729b20a5c | -21.9681 | -47.55891 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40406f17-f936-3d29-a2b3-a04caa7e8b60 | -19.14454 | -47.6954 | 2025-09-12 03:40:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57b52486-ad37-356f-aea7-a66ffa116efa | -17.27567 | -46.08484 | 2025-09-12 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 717e252e-ff36-3b9c-8c29-74593a0a5b55 | -23.10306 | -47.50552 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e358491d-48ca-3c3e-be05-06adbdfba53e | -20.6562 | -46.53483 | 2025-09-12 03:40:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c9f7668-9361-3bde-92d6-4b883538f68d | -18.66045 | -47.66785 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abfe53da-83b2-3c4c-a886-c1c1611da0f8 | -18.65694 | -47.65683 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11c2c869-8144-36dc-acfa-3e914d5ca8c7 | -21.94296 | -47.56099 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97cab5d5-0afd-38a4-8e39-b6deda3abb3f | -17.43072 | -49.22908 | 2025-09-12 03:40:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f25ad6f-0f5f-396a-a08c-204995d2e6a7 | -17.34734 | -46.69442 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 132db272-900f-36ec-bb17-c030501b449e | -23.11733 | -47.49075 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ef95af97-611a-357a-9d47-f2b8e17f625b | -18.64615 | -48.15062 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c4602513-668f-39df-b42a-589f2fb63c89 | -16.4326 | -49.0274 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 423a6940-fa66-31e9-8c6f-b44b3fd57c12 | -19.99811 | -46.91851 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb27f0d9-46c2-342e-baef-ef16500064b5 | -19.99447 | -46.92399 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dad7de9-59ff-3000-be9d-b2d3c02af165 | -16.81224 | -47.82965 | 2025-09-12 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 033d7ac9-d74d-378a-8258-0ee5fc94db0d | -21.18858 | -47.51771 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 6ef96289-fd46-3912-a1f8-0c0f455549d7 | -19.23184 | -48.04453 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ac994a31-bc2f-333a-8a0e-890657b2dfb3 | -19.99607 | -46.91647 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba8a9fef-3c47-3d0f-afb2-116acbcca4e8 | -21.18629 | -47.52394 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 38cf25d3-84d3-370b-847b-deb41b8977db | -17.13743 | -48.49321 | 2025-09-12 03:40:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a379ede-33dd-3e1c-9579-725c4879b393 | -23.3455 | -47.19635 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f66d2249-1276-3c45-8c5b-1039f6b9d449 | -18.65121 | -47.6554 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c09e9600-5762-3095-8291-e2bb8836ca14 | -21.33055 | -45.01466 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 46b4e952-6bf7-3e5a-a0a7-35966cbcdb71 | -17.1381 | -48.50143 | 2025-09-12 03:40:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0bf15f10-906d-3e74-871a-6c202b71a67a | -19.66293 | -44.90587 | 2025-09-12 03:40:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| dfd0c3e9-d99e-3e16-b15d-d00944a571d8 | -19.66189 | -45.85931 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d937976c-caa6-33da-8860-83b5063abd47 | -18.65563 | -47.66218 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c48eca07-6498-30ce-84f3-5251b703a836 | -18.01811 | -46.85831 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba1332e5-cd64-3825-a60c-ccaa1eb026e7 | -21.19167 | -47.52548 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 13c06770-396d-3094-a625-dff2a8aab296 | -21.33064 | -45.0379 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d0897503-e046-3cdc-9a21-986c0639e2e6 | -19.63317 | -41.57628 | 2025-09-12 03:40:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 18b54f60-c70f-3e72-86d1-c4d83a169567 | -20.55837 | -46.9328 | 2025-09-12 03:40:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 016207de-8336-3f86-8e8a-d50639659486 | -20.17322 | -44.62393 | 2025-09-12 03:40:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 694b9d27-3754-3477-84c8-2a067add0b93 | -23.28022 | -46.47612 | 2025-09-12 03:40:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c0a74401-582a-3438-a209-2eb75e6b20fe | -20.70735 | -46.05761 | 2025-09-12 03:40:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96fc4116-038d-3c3a-af7c-74cc3e0d3283 | -22.40319 | -46.75028 | 2025-09-12 03:40:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 3a25e7d3-0e30-3a58-8f59-bad436ba8ab5 | -18.05985 | -45.43482 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43d084f6-f0d4-3fcf-8c3a-d54eec6af8b4 | -19.99986 | -46.92508 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aefd554d-7875-36eb-ab91-be1c26672e50 | -23.13295 | -47.4946 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 259b2914-c584-34c4-beb0-dc039ac7d0b5 | -17.33694 | -46.66939 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01a92d78-2e8c-3027-9f6b-be6b5fdbbfb1 | -20.72924 | -42.15171 | 2025-09-12 03:40:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ec53536d-4b81-3b84-813b-bf8163eabf37 | -19.9991 | -47.61537 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc25af72-df9e-36bf-9464-685acafbe3c7 | -16.42186 | -49.04487 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a53fc66e-634f-30e9-b6f7-eacd8ee30f60 | -20.28149 | -42.88762 | 2025-09-12 03:40:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9495c799-8f78-39f6-b82e-6532d171b1d7 | -23.49626 | -47.26329 | 2025-09-12 03:40:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 986931f8-d412-374a-b103-6f4aa9abbcb9 | -18.82683 | -46.88446 | 2025-09-12 03:40:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8542d2ea-5d2a-34ef-85c8-26fc16193e51 | -22.40389 | -46.74701 | 2025-09-12 03:40:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 711363bc-beb9-3d4c-9d8e-0da5c1c225b4 | -19.9973 | -46.9222 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50ecc333-6c56-3213-840d-63f4f13d9ecb | -20.00067 | -46.92128 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b471fa5-21ba-3485-9251-f586293d33be | -21.94754 | -47.56588 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| effea745-2a15-3faa-bb10-d1c47c9c3f43 | -16.95641 | -45.81897 | 2025-09-12 03:40:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc682602-0456-3975-87d1-e1fb9b8d2512 | -20.29865 | -46.57072 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e275e17c-559a-364d-b4a2-fb56d3039071 | -21.33435 | -43.51038 | 2025-09-12 03:40:00 | NOAA-21 | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 42e7cbf3-1c52-3262-887f-47c4c6439dd0 | -19.97459 | -47.59352 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76171491-71be-340c-ae3f-ac6f0bb92320 | -23.13737 | -47.15582 | 2025-09-12 03:40:00 | NOAA-21 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| beebecf7-0425-32b3-a5a9-8a104badc932 | -19.66366 | -44.90261 | 2025-09-12 03:40:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8607d644-cc3f-3d78-8355-b132a9af3a94 | -17.56744 | -44.55095 | 2025-09-12 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e381b669-b1fa-3a9f-a263-c5e3e4b4726d | -22.86798 | -46.40385 | 2025-09-12 03:40:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 47c8fdd9-0f70-3b5a-b844-9b5b553d7678 | -19.74628 | -46.09079 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d822a4ce-4ae2-38d6-aaaf-a528829995e0 | -17.79966 | -42.5693 | 2025-09-12 03:40:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 07c602e6-0cd9-3abf-a66f-cebca949f66f | -17.14628 | -48.49386 | 2025-09-12 03:40:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c1bcfd6-804b-32ce-a0aa-942391d36466 | -18.60114 | -47.18777 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 094e0c09-dd9c-3484-98ce-de3625d98fb0 | -18.05207 | -45.44673 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190a1eec-44c6-3fd8-bd19-63dbe479de99 | -20.35503 | -48.40596 | 2025-09-12 03:40:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6dacff7-5b16-3963-91ff-3175907f9759 | -18.14334 | -43.22918 | 2025-09-12 03:40:00 | NOAA-21 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b576843-7a8c-390e-b5e4-57fbe7f7dc17 | -19.62235 | -46.439 | 2025-09-12 03:40:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92163202-e266-3d03-a809-8b6e43ba14aa | -22.60518 | -47.28081 | 2025-09-12 03:40:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d710beb-6710-33d0-9125-37c5f07c74d9 | -18.66072 | -47.667 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e77cfe4-ba3b-340c-859b-ffb979f60342 | -19.99527 | -46.92023 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c849b0f-5b9e-333a-abd4-af977a8c25bc | -23.34864 | -47.24022 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 08b1c968-76b4-3435-bce5-255e034a4821 | -17.6665 | -46.68055 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 18099281-e5d4-39fb-81d2-0f5dc10e1cbb | -23.13813 | -47.15239 | 2025-09-12 03:40:00 | NOAA-21 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| bbe97d01-8f05-355d-af93-15a5aa06db16 | -18.74958 | -47.62261 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6dba7e8-72da-3c59-a301-0b0dd4dc22c0 | -16.41673 | -45.68919 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27a8fc52-8f43-36e7-94bd-3854780ff0da | -19.99846 | -47.64478 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 994e67c1-a096-3fab-aa1c-61b0ba15b177 | -19.75645 | -46.09336 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 261180d2-1b4c-315d-9d61-7e69c95aa9df | -17.13914 | -48.49668 | 2025-09-12 03:40:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38bc9ce3-d9ce-364b-b770-278a949c0a67 | -20.11666 | -42.35251 | 2025-09-12 03:40:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f4765cc8-ef8f-332c-b96a-2594a8322050 | -17.91306 | -45.90591 | 2025-09-12 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2994ecf2-dd06-3f54-94c6-82c94aae961d | -21.36729 | -45.16936 | 2025-09-12 03:40:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4cdc41b8-5691-3c7d-9677-ef32ba4e942a | -18.76633 | -48.19704 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 687e6ca8-7a5a-34f0-b40f-e069222770e2 | -19.86598 | -44.93386 | 2025-09-12 03:40:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f6a740b8-972e-3d81-a34f-adedab77d8a3 | -20.5701 | -43.74199 | 2025-09-12 03:40:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c47ee5a1-9041-383d-a929-93c97a80b60e | -18.77332 | -48.19368 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4daf193-b756-3363-93be-02a7b7e8f637 | -22.19223 | -49.59472 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dee333db-3b4c-38a4-8d5c-cd49a705f17a | -23.1233 | -47.48858 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6105902-71d9-3155-abb5-74aafa7900f2 | -19.83848 | -44.58573 | 2025-09-12 03:40:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 41da3846-781f-334d-a3f1-5db546e21e25 | -18.65466 | -47.66673 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1ddc1b3-8f5b-311b-a389-82e36c2c3d70 | -18.97484 | -41.52685 | 2025-09-12 03:40:00 | NOAA-21 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 4f480034-cc95-3cdd-b0c7-aa7b813ba47c | -22.83306 | -47.46161 | 2025-09-12 03:40:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da9c2971-3b12-3809-967d-2486de675bc0 | -16.81328 | -47.82487 | 2025-09-12 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f45ef826-feaf-3566-be19-70174d8238c7 | -20.35281 | -49.96074 | 2025-09-12 03:40:00 | NOAA-21 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f85a9408-e5ff-35a5-be57-89d17591d42d | -19.23092 | -48.04277 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85eb6b65-446d-35a1-b1eb-e7ba8f526ddc | -20.69844 | -46.07504 | 2025-09-12 03:40:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79c1febc-20d6-38c0-99ad-20144cd2a7e6 | -20.26854 | -42.12457 | 2025-09-12 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 7e66c08c-eb5e-348b-83e0-aa9c4194b0f2 | -22.61014 | -46.41773 | 2025-09-12 03:40:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1c5ce60c-e4fe-3f35-aeaa-84232ecb8621 | -23.15412 | -48.25254 | 2025-09-12 03:40:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5a7e0d7a-fa73-3e11-94d9-8dece61fdda0 | -15.86666 | -48.33739 | 2025-09-12 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
