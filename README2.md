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
| 6bc45653-ea70-32a8-b5f3-3a4e3aa5d766 | -3.75941 | -41.02777 | 2025-03-24 04:00:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9580eca1-64f6-3a0f-8ccc-8ec35c419114 | -7.0567 | -44.38562 | 2025-03-24 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bc48619-6af3-362c-9a7e-d57d8194d281 | -8.10455 | -43.13315 | 2025-03-24 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c21194d5-3182-3805-b620-b651a5045df0 | -9.03187 | -38.51017 | 2025-03-24 04:02:00 | NOAA-21 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15d93c78-b12d-3566-a5b3-3f7273f8a0fa | -8.87754 | -36.53078 | 2025-03-24 04:02:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 15f7158e-9d20-3f02-970f-4143b535e15d | -8.1103 | -43.14231 | 2025-03-24 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e49fc60d-c404-34f5-94d8-6a5c2a07e55b | -10.00966 | -44.48258 | 2025-03-24 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f84fea6-ca9e-3d0b-8fb3-3ab7e1aae776 | -8.0728 | -34.97486 | 2025-03-24 04:02:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 72781120-f683-3a05-ad57-f9fc9b9248bf | -8.87832 | -36.52826 | 2025-03-24 04:02:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8da1b104-6d0b-3495-8acb-4a454ffe70ce | -7.06053 | -44.38627 | 2025-03-24 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bb1b74e-1a02-3468-a2bd-2d6d31815659 | -6.24731 | -44.82502 | 2025-03-24 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 577d9530-e2a6-30c0-83f3-633fa957518b | -8.39024 | -35.02291 | 2025-03-24 04:02:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be8325dc-8e58-3ac1-a948-ebf2acb72a70 | -17.75228 | -42.89399 | 2025-03-24 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38dfd52a-f8a5-3d50-a31a-b17024932647 | -15.51601 | -42.60321 | 2025-03-24 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3afe8f82-3b44-33d4-bf30-71e267caec33 | -19.40319 | -43.53028 | 2025-03-24 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 746597d9-acb9-3522-8f96-3da3f682712d | -19.71715 | -40.35642 | 2025-03-24 04:04:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3adb701-8a01-356d-8ce7-d866fb1f906d | -18.04128 | -39.92511 | 2025-03-24 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 30df7316-240e-30b9-a9f6-17db19499108 | -16.67997 | -43.88395 | 2025-03-24 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0597e4e8-0a8d-3017-b434-b9fb127023fa | -17.37818 | -42.48283 | 2025-03-24 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fde8564e-0f13-387a-96da-4af4105a8452 | -17.59522 | -43.1981 | 2025-03-24 04:04:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 532e8a6b-fe53-306c-b9c5-a76b3b381531 | -19.39988 | -43.52969 | 2025-03-24 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c46e8769-f10a-3e44-9a7b-59ee5a6e168a | -17.6779 | -42.74056 | 2025-03-24 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b2fd055-3bca-354d-ab40-0f516012f036 | -19.43591 | -43.51725 | 2025-03-24 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1d26c3a-c483-3fd5-8f85-87d02da8e9a1 | -17.34801 | -43.86124 | 2025-03-24 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c9a7f14-c431-3c3e-899c-da75b863737d | -15.51658 | -42.59962 | 2025-03-24 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1313d0a8-c83c-35d6-a491-657ad10dbfed | -17.67734 | -42.74417 | 2025-03-24 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 770691b6-18db-3920-a4cb-353fff9334df | -17.77918 | -42.80957 | 2025-03-24 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f3355f1-dcc8-3c51-a865-b555f18582dd | -18.04068 | -39.92666 | 2025-03-24 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0c7f1188-0a1b-3fa0-b770-fe20c6f32dd6 | -17.35136 | -43.86184 | 2025-03-24 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5c57342-2470-37ea-b801-9bc64f758f35 | -17.78249 | -42.81014 | 2025-03-24 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ad36a73-5d53-384f-9c42-cba6dfc08907 | -21.61326 | -48.47728 | 2025-03-24 04:06:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22aa6dea-d0ed-3ff4-b3aa-4b7dacba3e32 | -24.55577 | -50.80556 | 2025-03-24 04:06:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 228a5359-03b7-31d1-a1be-84e953d8e680 | -23.98609 | -48.91558 | 2025-03-24 04:06:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95f44734-573b-3c12-92e7-014c7bd0c962 | -25.19263 | -49.32531 | 2025-03-24 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 371d573e-ef40-366a-8e03-3c97b1e77507 | -23.9842 | -48.91874 | 2025-03-24 04:06:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d92c1c36-85e8-329a-8e70-23f5e64bf7c2 | -22.53877 | -48.81155 | 2025-03-24 04:06:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b192f76f-5820-3513-8f48-14342cb58504 | -23.40699 | -46.55513 | 2025-03-24 04:06:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5e4186ba-7298-3ebb-806c-babd4ab67ae9 | -24.54983 | -50.81304 | 2025-03-24 04:06:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fc032f10-1d95-339a-8563-dddb988b376c | -24.54396 | -50.798 | 2025-03-24 04:06:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6acba98e-3cc1-393d-93ac-0a1a9c999cb2 | -23.34054 | -46.7725 | 2025-03-24 04:06:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1ca53e67-ef8d-3849-8fa9-26c465f54673 | -25.46173 | -49.19638 | 2025-03-24 04:06:00 | NOAA-21 | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dda4e3f9-5c6e-3bda-91db-2f87e32debe3 | -24.55068 | -50.80879 | 2025-03-24 04:06:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 54dc0a57-3ee4-3dcc-b2e2-0195db3d9692 | -23.69838 | -55.25641 | 2025-03-24 04:06:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 314df3b1-4df7-3e59-8023-f9ecc83d778e | -24.55493 | -50.80976 | 2025-03-24 04:06:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dc675836-0ea7-33e5-9ebe-c1ccd174c24b | -24.24459 | -50.74028 | 2025-03-24 04:06:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ddf9f40a-64f2-3b61-a616-c512253c6bc2 | -20.78333 | -49.84974 | 2025-03-24 04:06:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e59dbb5-edbf-39e3-94bb-961481d773c4 | -30.75694 | -53.33698 | 2025-03-24 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| adc687e7-a619-31a8-9840-f9b715521333 | -28.58714 | -49.44312 | 2025-03-24 04:08:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 12d6c682-e494-3d4f-b699-c96b3ba1e5f3 | -27.33687 | -50.57678 | 2025-03-24 04:08:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 53505967-bc19-32aa-81df-ff05e243dfc4 | -26.95401 | -51.28582 | 2025-03-24 04:08:00 | NOAA-21 | IOMERÊ | SANTA CATARINA | Brasil | 4207577 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 64b6ec27-f8ef-3dab-be86-05fc3ea2ffd4 | -28.58579 | -49.4399 | 2025-03-24 04:08:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1afd8fea-c172-3459-888c-b2fe16ee982f | -29.20622 | -51.89546 | 2025-03-24 04:08:00 | NOAA-21 | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4ad2ec05-cc88-3083-89cf-856a752ad2a1 | 4.0758 | -61.5602 | 2025-03-24 04:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 629ba9b9-d4e6-3aa0-b464-fdd9ebdb2d07 | 4.0758 | -61.5602 | 2025-03-24 04:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 35a88e9b-3e17-3b59-a815-087067049359 | -6.24425 | -44.82656 | 2025-03-24 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9db9a1e2-836c-348d-a605-a973d52ab1d2 | -1.9467 | -47.9148 | 2025-03-24 04:25:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4402159b-d732-395a-9787-1e327aca516e | -8.10295 | -43.13206 | 2025-03-24 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 55b67b16-57ee-3b15-b853-494675859b25 | -8.10901 | -43.14179 | 2025-03-24 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a3e6fde0-894b-3ae3-98b7-a53c7b9e6dfa | -3.75791 | -41.02962 | 2025-03-24 04:25:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e722ad5a-c72e-3856-89fd-e45e8aa5fadb | -7.05851 | -44.3855 | 2025-03-24 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d220210-542d-3b0c-826e-891cdcbeaee0 | -3.75822 | -41.02779 | 2025-03-24 04:25:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bff3eb2b-32a4-3ed6-a67c-18ed2e026702 | -7.05508 | -44.38498 | 2025-03-24 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4332e8b1-11ff-3ca7-a7a7-621f0cd57646 | -17.59501 | -43.19666 | 2025-03-24 04:27:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f72d4476-8b6f-3c75-8d64-33b6e30b9ece | -15.56996 | -47.85572 | 2025-03-24 04:27:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 177dad2b-32ad-32e9-ae6e-74c603f19bad | -15.51641 | -42.60227 | 2025-03-24 04:27:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec478ef1-2216-3b06-a54b-0b87b201bb81 | -17.77797 | -42.80792 | 2025-03-24 04:27:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db5fb3b4-f740-3a2c-aed2-76d31da88509 | -15.51693 | -42.5983 | 2025-03-24 04:27:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5e2ea2d-f7c5-325f-a4e5-616c3f5cd536 | -17.34878 | -43.86056 | 2025-03-24 04:27:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 734cdbc4-41cf-3ddf-8575-e85c397bf8a6 | -14.60431 | -50.26859 | 2025-03-24 04:27:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afdde022-dac5-3824-b424-11d909e99393 | -15.51224 | -42.60164 | 2025-03-24 04:27:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abd74822-7881-38aa-9c76-fcc6a1815525 | -17.34962 | -43.86343 | 2025-03-24 04:27:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3495ff2-bd26-334e-9e26-f7d527127870 | -17.88353 | -42.64579 | 2025-03-24 04:27:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4bad60fa-a362-3307-8f13-93495b429c6c | -14.60712 | -50.27309 | 2025-03-24 04:27:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b28cfe9d-8aad-3016-abd4-340e207ad4f2 | -10.00791 | -44.48188 | 2025-03-24 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25272676-2444-3c1e-9ea7-77c6fb88c9e8 | -21.61392 | -48.4775 | 2025-03-24 04:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c139e818-c7b1-39e9-a0f5-91567b59890f | -21.61055 | -48.47692 | 2025-03-24 04:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d07152a-88c5-3c1b-8573-4d380fb811e0 | -19.427 | -43.51527 | 2025-03-24 04:29:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3665e73e-ed35-3708-b13e-a587662697c7 | -19.43043 | -43.51322 | 2025-03-24 04:29:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efe95d18-f2f9-37ee-8b80-f7ce3931882f | -23.33792 | -46.77256 | 2025-03-24 04:29:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b10ed60f-05ec-3d40-a41f-95a5e4d66b08 | -19.43408 | -43.51764 | 2025-03-24 04:29:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccb028c8-2125-3a47-97a6-7b65a4abae96 | 4.0758 | -61.5602 | 2025-03-24 04:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a3197929-5ad4-3f93-8411-f6158bc03b1e | -28.58515 | -49.4427 | 2025-03-24 04:32:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2c8fc0d7-ccf1-3ed4-a509-8a8d31661a66 | -26.9533 | -51.28377 | 2025-03-24 04:32:00 | NPP-375D | IOMERÊ | SANTA CATARINA | Brasil | 4207577 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 74163c38-8d16-3479-a654-e8867e94a37f | -28.45266 | -50.84204 | 2025-03-24 04:32:00 | NPP-375D | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7bb047b8-bd79-341f-a24c-23a74d83d204 | -23.69625 | -55.25515 | 2025-03-24 04:32:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3f42c609-6f66-3cd6-9cfb-1b96cf463251 | -29.20549 | -51.8979 | 2025-03-24 04:32:00 | NPP-375D | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e8a99e7-139e-3185-a2cf-068bd482cb52 | -24.55503 | -50.80803 | 2025-03-24 04:32:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8987ef9b-e70a-327f-9d7f-3b44e7bfaf69 | -24.5511 | -50.81119 | 2025-03-24 04:32:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 52244305-5e8b-35a6-8765-97e43a6902bb | -24.54777 | -50.81055 | 2025-03-24 04:32:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d4bf05ca-ed8b-33c8-9da3-719b02e89024 | -27.33478 | -50.57598 | 2025-03-24 04:32:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54763cfe-ac60-3890-a56b-ad81bc27fcaa | -26.99003 | -51.98173 | 2025-03-24 04:32:00 | NPP-375D | IRANI | SANTA CATARINA | Brasil | 4207809 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4cc8dfac-2b30-3dc3-ae50-a79daab74141 | -25.56855 | -49.36517 | 2025-03-24 04:32:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f04dc31-c076-3bcc-a686-33c1078057ac | -24.55171 | -50.80739 | 2025-03-24 04:32:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e7059b75-6fbe-308a-9045-13b0df77f6d0 | -23.70016 | -55.25603 | 2025-03-24 04:32:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b6c18e8-8e69-39a5-91ee-42578566f42f | -25.19079 | -49.32625 | 2025-03-24 04:32:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0fccac17-e12e-3825-8c54-c4e77bfd4df0 | -29.95212 | -51.61666 | 2025-03-24 04:32:00 | NPP-375D | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| a01deb36-2f21-3cd8-b924-973691ad9e07 | -30.756 | -53.33539 | 2025-03-24 04:34:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| f184ac31-8b4f-3b46-9b32-3539a679e3dc | 4.0758 | -61.5602 | 2025-03-24 04:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 3fbf951b-5f6d-30c3-8b29-ae0f663fcf8e | 4.07454 | -61.56885 | 2025-03-24 04:46:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1113cec0-65df-361f-a797-175f59579f82 | 4.09866 | -61.56036 | 2025-03-24 04:46:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
