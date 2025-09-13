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
| 6d9861db-567f-3b11-a4e1-d688bee6cd50 | -15.68944 | -49.90107 | 2025-09-13 04:10:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 640574b3-71fc-34f8-b8a7-5e32f5aeb579 | -17.28974 | -47.24474 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 53b8f5ab-68f4-3eb2-8af4-dc58d00372cf | -20.38828 | -45.54096 | 2025-09-13 04:10:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 312e2bc6-bee6-334c-8578-78c78c37a802 | -17.99289 | -46.94008 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 428469c8-16bc-3755-a644-aecc2308168c | -22.78628 | -47.80493 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bebf20d-1945-3c7a-bfc4-e12c3813aeab | -15.15741 | -52.47944 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1bc321d6-06e7-3079-92b8-c72d3fec0cb1 | -20.44336 | -46.45492 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81ef5d7d-b98a-37dc-9e8c-9d450a8e713b | -22.25795 | -49.56662 | 2025-09-13 04:10:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 77a95b09-d1e6-3ffb-abfa-ea5fbb68bf6f | -17.23563 | -50.23494 | 2025-09-13 04:10:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f858a22c-300c-39f6-a151-3ca954bedc74 | -18.3936 | -44.09758 | 2025-09-13 04:10:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d777be-94e6-39a5-b7cf-cc78f1aa774d | -20.25373 | -44.18363 | 2025-09-13 04:10:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 51576ad1-1c77-3908-bd2d-92efc9c53556 | -21.62312 | -46.81509 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| a512a598-0189-3c62-b2fb-6727fb2c2af3 | -15.68972 | -50.58592 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65657e35-d72f-31cf-a65b-eb163424d4a2 | -19.98094 | -46.90743 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 384a2882-6363-3f4b-8c3b-6a3c33bf598b | -18.59144 | -47.19491 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 517af777-9eeb-3583-b299-fff4ae02d714 | -15.15509 | -52.49113 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e168253-33cd-319c-a7e3-3a2362717331 | -15.76802 | -52.24256 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e647fda3-70af-3df4-8561-4de04dceeff7 | -20.56998 | -43.75148 | 2025-09-13 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3b58578a-a5d6-3fc2-8dd8-dd016c4ce135 | -15.38141 | -52.10427 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5764d20-e4f8-3bf4-8b71-f4eace95425e | -22.25027 | -46.15049 | 2025-09-13 04:10:00 | NOAA-20 | BORDA DA MATA | MINAS GERAIS | Brasil | 3108305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7f85b74a-6f81-3133-b714-614d9372d676 | -19.90999 | -43.85644 | 2025-09-13 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29005f60-39aa-3a30-889e-f1af51c723f1 | -15.68703 | -50.57575 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8cfbd91c-2fc1-3b9e-94c2-118044d56c22 | -21.66961 | -45.39206 | 2025-09-13 04:10:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fc268f4e-70cd-3dd9-9b5d-915258ef7607 | -17.29125 | -47.23608 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db890c8c-c438-3d03-bf04-9916dfb2def8 | -16.40989 | -49.03615 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a702ff6d-fbea-3c10-a101-907860336092 | -18.6223 | -44.26327 | 2025-09-13 04:10:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a172ada4-e4e9-3038-9214-5789916fef82 | -15.54243 | -47.94878 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 62cbdd62-38f3-3ae7-ab0a-0a21275e5ebe | -16.53322 | -51.7368 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f0447a7-1a5b-3411-bda2-879103cdd5ab | -17.54741 | -44.55238 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9902e193-9502-39a9-81a4-afb1edede329 | -16.35635 | -51.50743 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 713ab6d1-7f9a-372d-a39d-dcf37bc4c01c | -21.61082 | -46.80504 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d0e650a4-e65b-301a-abf2-3d1202c831df | -17.34166 | -46.67111 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1ff81aa-b469-3ac4-ad50-33d334e74e48 | -20.09146 | -46.93924 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d0fa317-d1ec-361c-8349-bc59c9df9b03 | -21.62378 | -46.81115 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e32d5080-b081-353c-bccf-b2b5f2038b40 | -15.16334 | -50.16167 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 773f4a4d-8997-3557-8d20-40d9ad8bd41c | -17.40881 | -44.01328 | 2025-09-13 04:10:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f595515-bccf-3534-9014-29d27e1270cb | -16.5605 | -49.21893 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 289ef99c-634a-300f-a885-5f3e310bbdf6 | -16.53685 | -51.74344 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8607d62d-2768-3ccd-a5d8-7440f467610b | -16.41404 | -49.24013 | 2025-09-13 04:10:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84b0fe41-a198-3e4e-9c22-0082e88cb4d3 | -15.16269 | -52.47969 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bea09b0c-76cc-3d49-8e39-6ee65d498e9e | -16.64822 | -49.78733 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef30d51a-47c1-3ea3-8319-9fc633a44212 | -15.58976 | -54.75781 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4287434a-0012-308b-9acd-688cd92e1f68 | -16.33315 | -51.54612 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d6396af-788b-3c3c-9ee2-a48887416653 | -15.5502 | -54.80907 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8606fc94-3d73-34b0-884a-17e5e38d300f | -16.5248 | -51.75623 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca3113bf-0e05-3595-a122-9f2d1c2644e3 | -19.97111 | -47.5953 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 295dded5-42e8-3df1-92ae-30d555f684db | -16.40929 | -49.2431 | 2025-09-13 04:10:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0d1b354-7ff2-3304-8432-36f958b660a2 | -16.366 | -51.53276 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 396c5dc9-5d39-3a8f-87a4-49fc5afe5365 | -20.72643 | -56.74403 | 2025-09-13 04:10:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0944628-ead8-3adf-8bc8-22dd3f794522 | -16.41473 | -49.2364 | 2025-09-13 04:10:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba34bda2-cf31-31a5-88de-781a3c1e34c5 | -18.38972 | -44.10064 | 2025-09-13 04:10:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c74813a-a049-306a-9d52-d7bce02086dc | -18.89115 | -47.05743 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 686d7d18-4101-30f3-afa8-59d8b8ff85d6 | -17.54525 | -44.54456 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f370f45e-89eb-3ca1-80eb-84bcf80fbc70 | -18.15937 | -49.18527 | 2025-09-13 04:10:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 73441df4-27ce-321e-9a4a-976149fd3f01 | -19.33249 | -45.11568 | 2025-09-13 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fbef74b7-646c-3915-9982-960e7db0faed | -17.94907 | -46.00212 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82be84ec-33c4-3e79-b3ca-87eba95e9be1 | -17.28181 | -47.24767 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 825b5452-1d35-3608-a276-2c9396a252fc | -20.54933 | -45.83069 | 2025-09-13 04:10:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7867b70-ec6e-369c-ab04-caff58ab904e | -20.5925 | -44.90223 | 2025-09-13 04:10:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e23eed19-4504-3cf9-8c35-9ec4c97831d4 | -17.34236 | -46.667 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea24dff9-7d97-3fd7-89f2-834030630fb0 | -17.4451 | -49.23579 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c993c82-e2af-3233-8665-e5a53b3dcc0d | -16.07376 | -49.99592 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0f760882-a523-3b4d-bb79-9800a69f5fc4 | -15.7592 | -53.49849 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3255ab47-dea8-37e6-88e4-f041d7fe72a4 | -19.64004 | -45.08324 | 2025-09-13 04:10:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4fb95017-b428-397e-9d01-439eb6e7ec09 | -18.06453 | -45.45198 | 2025-09-13 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc311ddd-5561-3745-9505-2c11bd1ffd68 | -16.09012 | -49.95564 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| eff872fd-9e89-34f2-b4d5-91d022b4af5a | -15.14255 | -48.31207 | 2025-09-13 04:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3033bb4f-851d-36ff-bb2c-4a8c98d80d00 | -20.64416 | -48.69511 | 2025-09-13 04:10:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e7d7076-f7ca-3fd9-9231-24ac789255a0 | -17.99714 | -46.93652 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b0405a9-8b67-3a65-a578-a1688bd7e6ef | -15.58642 | -54.75322 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ebe1bdb4-1c8e-33c9-a428-14c54a4bfa6e | -18.00276 | -46.92498 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a432bc1e-cb10-3768-9b8c-907ee61a24b0 | -20.4542 | -46.43681 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a76a279-a2a3-389b-a7e0-c6e28964108e | -15.10083 | -50.18422 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99926d9e-d5e1-3b54-8c70-56619f5dfcd2 | -19.25794 | -51.43249 | 2025-09-13 04:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6635bcb6-af69-3dba-8f8d-f39b8545b3f0 | -18.47394 | -39.76662 | 2025-09-13 04:10:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| dc389a25-3685-303b-9f2e-35200a75c00b | -16.68969 | -49.17537 | 2025-09-13 04:10:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed89a1ab-5184-339b-87e3-3289c3b511ff | -15.71299 | -50.58603 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| be02c735-2d75-3967-a0aa-3e883a4805a3 | -19.63669 | -43.73882 | 2025-09-13 04:10:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45e6a095-4868-3cf9-8996-048dfb0765d2 | -15.2014 | -56.6813 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2fbbfe9a-f47f-3e0e-9ebd-a71d92998206 | -18.13668 | -48.45692 | 2025-09-13 04:10:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3710d989-2dbf-3bf0-acdf-3f7f1ff7d121 | -17.67699 | -47.86499 | 2025-09-13 04:10:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 301d61eb-37ac-3727-b215-f52422e87636 | -16.06354 | -50.00303 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 937c6141-3d92-3182-a0b6-396882a8df94 | -16.40621 | -45.67429 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33cecad6-23e1-3005-955f-64ca83036b6c | -21.6265 | -46.81579 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3d6d7056-fa0d-3ade-a128-7c6cba3fa810 | -16.64495 | -49.78155 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c63ddb5f-fcdd-300a-9aa4-7d36b68c6932 | -20.42637 | -49.94134 | 2025-09-13 04:10:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94b98ea6-57d4-32eb-b8b6-0b2bfe735069 | -15.76405 | -53.4963 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b6278a6-1a4c-3a29-8353-56b61920e497 | -15.69153 | -50.57652 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c03f6aea-8d06-3933-9e5a-9138008a6a95 | -15.13976 | -52.4877 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26e90d60-e36e-37d4-8423-cda3469a5321 | -17.3894 | -43.52864 | 2025-09-13 04:10:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b62d6a75-9790-3c07-a15d-f0d3611957a6 | -18.96329 | -48.59958 | 2025-09-13 04:10:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b394e00-b488-39b8-b7f9-8cc9b0e8a10c | -15.16043 | -50.12846 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93a880a5-30ba-3db0-b0f8-5e6786736329 | -16.08867 | -49.96344 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a720e967-8e1d-3eeb-9c20-33077a01484e | -16.14336 | -49.92235 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7cdd1cd-1d35-3963-be10-99e61f68a708 | -17.28767 | -47.23537 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50af98eb-207a-33ac-b40f-e5cdb30fc969 | -20.65153 | -48.6966 | 2025-09-13 04:10:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bdea4aa-aa78-36ff-901b-4cf8fe846d3b | -15.59465 | -54.76355 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96084fbc-a4c4-3df8-b674-8278b79cc9cb | -20.37057 | -50.12702 | 2025-09-13 04:10:00 | NOAA-20 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d317e93d-6ca8-3441-aeea-7425c4d4ed4e | -17.37291 | -41.71296 | 2025-09-13 04:10:00 | NOAA-20 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c5e9899c-e472-3ab9-8863-755460388cfe | -20.33433 | -46.667 | 2025-09-13 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README65.md)
