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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b941f7f-5bad-3e0f-b0f2-2e7741ebc354 | -16.44913 | -49.28431 | 2025-09-07 04:21:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a044faa-f244-38ce-8ff3-5d8cd4d86fca | -13.01167 | -54.84718 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c2da626-f90e-3cd7-958a-c6c67c9552ba | -17.68964 | -44.51513 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ccc4d26-0a8b-3d06-93bc-d427852177a3 | -15.73262 | -47.02486 | 2025-09-07 04:21:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b148c626-4d6b-369a-bf62-6af2e947c3be | -14.53705 | -53.15188 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1577019-9826-371c-a45f-7325bcbcbf8d | -13.91595 | -48.02803 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79eef633-3030-3e3d-b5a1-97c3a5a55475 | -13.9181 | -48.03619 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6f5d89d-fb6c-34fe-b62e-ee54e628d13a | -15.01052 | -48.00753 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70bac6ed-5530-311d-aa0d-2f1e30830faa | -15.7314 | -53.5497 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5603f337-e29d-3e2b-bbc9-719111cff87f | -12.93865 | -54.77094 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 275c8eb2-95d5-359f-84f2-55c3c42f48ca | -12.94699 | -54.78201 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26f60ca4-013c-3cd6-a1b8-c6423a2f85c1 | -14.26842 | -44.97244 | 2025-09-07 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da20b6fd-3964-341a-ad48-ee99913b0fa2 | -12.63853 | -56.98563 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adbec023-282d-3323-ab3e-65061d94711b | -13.05771 | -47.1177 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d484e62-b314-36bd-8023-1bdedf9786b5 | -19.12208 | -46.45118 | 2025-09-07 04:21:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 569a86fa-0105-3409-bdd7-03b57c924d31 | -13.66389 | -46.96149 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9446feeb-605a-31ea-99d9-112191c1c111 | -15.59339 | -48.49709 | 2025-09-07 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a55c5a9-9951-3626-865f-ddc5477f46df | -21.2047 | -44.33672 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a85ef858-85dc-3af9-b598-543bb9e4cad4 | -17.68107 | -43.53191 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 212492d5-585a-3030-b25a-1f5109740d61 | -18.72995 | -49.62506 | 2025-09-07 04:21:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45f52f09-6f2c-3bae-ba4f-3dc9301feb1a | -14.56751 | -49.12989 | 2025-09-07 04:21:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe9a0f06-91dc-3415-8b97-b8e753939ccf | -15.17309 | -52.39791 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ab95c4a-3a9d-3fd8-b6f9-4ada2634bf59 | -19.48489 | -47.75381 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86bebfe0-ca69-385e-a143-1895e39a8c2d | -16.53706 | -45.09506 | 2025-09-07 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 921bc393-1a4e-3c27-b00a-2872f61bddd9 | -14.48673 | -48.76039 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c25a4a29-c45b-3d7e-a526-7c30a488c55c | -17.6744 | -43.53848 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80f94cfa-5cc6-3e12-b194-dc0264f6a9ac | -19.47754 | -47.7788 | 2025-09-07 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7264d2cd-987b-3f9b-b308-71f9d47ad83f | -15.58661 | -48.49591 | 2025-09-07 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5de1ae89-320a-3401-97f2-1ded7496ec81 | -13.26132 | -46.88763 | 2025-09-07 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 702db9c3-e756-3b4e-b772-e9b78e1c22fb | -14.74173 | -47.50594 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1ab5ec1-4099-3bce-a893-9ec3db4497ca | -13.79665 | -52.77211 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a625c43c-4a39-31f4-9b8b-f7449737832e | -19.47379 | -47.75938 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 711fae45-b384-3281-a479-a310d54e4e4f | -16.34022 | -52.95932 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9a02e5f-4487-3151-a4ed-57f237ea904b | -13.29215 | -51.7451 | 2025-09-07 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f80e2abe-b16e-3d17-a445-200281d8607c | -13.903 | -54.0064 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 767e874e-5a2d-3154-8e01-5573dab089ca | -17.70712 | -49.10912 | 2025-09-07 04:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd9623e5-8802-3320-8207-86d84db1f815 | -19.4699 | -47.76245 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 33.4 |
| c52a8ac1-973a-3300-849d-94a4a6d43a59 | -15.69799 | -53.56351 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b23d3d4a-f703-3f56-9dce-6e109f8783ec | -16.33471 | -52.94199 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d762224-2436-3437-95be-7354ba70e3b8 | -13.89356 | -53.99804 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58eb081c-400d-3a48-9b38-bd4dc41673db | -18.11731 | -44.49834 | 2025-09-07 04:21:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d0cd6aa-4450-38cd-a924-eaf101abef76 | -17.67673 | -43.53605 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ac93f3bb-72dd-3365-ae49-e77fca6b0b0e | -13.79105 | -43.16288 | 2025-09-07 04:21:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f36d568-20e0-3c5f-b948-c43a98c1863b | -13.0438 | -47.11907 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8db4cef7-e379-31a9-8a8c-04fe27cdbed2 | -17.3996 | -49.30911 | 2025-09-07 04:21:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47222c35-75f7-346f-a2ab-824e1727e946 | -16.97581 | -45.83256 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eca7e677-bc44-3231-a38f-405f76be0014 | -12.99703 | -48.04724 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 709a6aa2-aa4b-3ea7-b8ae-a5418f77fba7 | -20.5486 | -46.45176 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70bdaf0a-9d31-3003-93a6-1fc21f98a9cc | -13.82809 | -46.26868 | 2025-09-07 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 441b97af-3fda-3074-9a03-7ea73b08d240 | -13.30446 | -51.74733 | 2025-09-07 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2a36a83b-07d1-3d83-8853-9a040314198e | -20.35711 | -43.88145 | 2025-09-07 04:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 23b549a2-a119-3d72-88fb-f3e6a34b82a6 | -15.10163 | -48.13738 | 2025-09-07 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6894cada-5543-3576-8a25-f2e525d060c9 | -14.56332 | -49.13339 | 2025-09-07 04:21:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68382f31-554a-32cb-a040-cf3154d68b84 | -14.65846 | -46.81668 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ca81875-63cb-3f52-b9fb-8e2359274c53 | -20.53558 | -46.44613 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 92a80278-5fdb-30c9-a6c0-cc3592c60b56 | -14.48828 | -48.77243 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b78e1388-218a-36eb-912a-4b59057188c5 | -13.83307 | -46.25859 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ec3fef5-45b1-3c81-81a6-69c6eb8a7b50 | -20.5452 | -46.45133 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64376e48-a0fa-3d59-9137-7cedfb5ea838 | -17.70444 | -47.65334 | 2025-09-07 04:21:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95a6f73b-4cee-3070-96e9-d9d51d1d6c62 | -17.40646 | -49.31037 | 2025-09-07 04:21:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30084ca9-d787-387c-92e9-4eb89c51c551 | -13.8524 | -46.2436 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a849c82-eda9-3d5c-99f4-037fcbbb3408 | -18.69038 | -44.44956 | 2025-09-07 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b46bc844-bbe2-38df-9885-177a55c3dd70 | -16.93872 | -45.75805 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfd2c91a-568e-30b4-b303-0aca7fbfddac | -20.25871 | -44.53171 | 2025-09-07 04:21:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| df6a126e-1f00-3190-bfc4-99e4a67b6279 | -14.7866 | -48.11012 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9357a48-10a1-3b81-a937-a5afc31e4e4d | -13.06104 | -47.11827 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f1a1704-8a5f-31a8-ac54-d0717907366f | -20.09008 | -44.29326 | 2025-09-07 04:21:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4367ec34-6373-3740-be69-8922831580a6 | -19.48143 | -47.77573 | 2025-09-07 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a29e5901-c8cb-387d-8e12-8dd411d166f6 | -12.92741 | -54.77507 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8953c903-d1ed-39bf-94e4-76028430eed1 | -14.56064 | -43.72646 | 2025-09-07 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af5396a0-3f89-36c4-834a-22852df97b65 | -19.47322 | -47.76303 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 33.4 |
| fc6e1b6d-c6eb-30fb-9368-e8e689108145 | -17.57511 | -49.79291 | 2025-09-07 04:21:00 | NOAA-20 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54d962d8-4a15-3a09-b1ff-6cdf6530ed54 | -13.05215 | -48.05294 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89ff3af3-11aa-3cde-a88b-89497ff5ee43 | -12.77447 | -52.95243 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ac20c76-76a1-36c8-844c-e02b9edd840e | -14.8209 | -48.18393 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0a6201f-9d68-3129-9764-be187b3015e0 | -13.84467 | -46.24958 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4849084a-fce1-3ed5-b2fd-decd06e26014 | -12.82154 | -56.52092 | 2025-09-07 04:21:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30e9a6c9-7def-3b3f-a362-5eb3898fcd27 | -13.00566 | -54.82399 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30e98ecd-4b60-3765-8919-c66435006a4d | -13.04037 | -48.03938 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cadaebae-6c51-32fc-ac91-7c2d8127b97a | -19.48533 | -47.77266 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 922d478e-0e48-340f-941f-32b9a5465579 | -19.48546 | -47.75016 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f4289ce-54bc-3c9d-b9f6-4d5585833f83 | -12.93246 | -54.77599 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 328faf53-a095-3453-8701-11ea72c6e98c | -14.49589 | -53.24986 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5f97415-78c9-3a4f-a1c6-200d80d265a9 | -17.22349 | -46.71635 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c4aae13-42db-3387-9bcc-67a23b54c173 | -15.67874 | -43.23024 | 2025-09-07 04:21:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f6b4f36e-a03c-3ea1-a435-2ccac065016b | -18.36205 | -43.92025 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 643db30b-dc61-300f-a055-74bf28a3ad88 | -11.16369 | -59.15955 | 2025-09-07 04:21:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6faf1fc-89c2-3cfe-98e4-9e625197f1a6 | -17.67991 | -43.55317 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba273d2a-538d-371f-a01a-953142054f09 | -14.26785 | -44.97618 | 2025-09-07 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d53821d2-d3ec-31b1-9ab3-77b2d6672c67 | -15.53697 | -48.37508 | 2025-09-07 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 887e4373-f782-39ed-b63b-7801768b4261 | -12.61562 | -56.98504 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab955dcc-0ad7-3d06-8439-30779c294a9f | -13.05773 | -48.06168 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aedbaa17-7390-3820-9add-794d60f700c6 | -14.80744 | -48.10984 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e21ba9e-d758-3a0d-b6fb-7072c01f34da | -22.14749 | -49.12068 | 2025-09-07 04:23:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 202f9789-7a8a-3903-9209-c92b41f45c1b | -21.83589 | -46.46661 | 2025-09-07 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a5c5ba99-df00-35b2-a8b4-926e97f914d2 | -19.86079 | -57.89166 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1eaeecd7-c75f-3dd6-b517-ced009be2078 | -24.15206 | -49.52325 | 2025-09-07 04:23:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4817b499-a297-3e42-8ec0-eafe42d13862 | -22.70184 | -53.25047 | 2025-09-07 04:23:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 599c6068-87b7-308f-bc77-eded65b5423f | -19.87608 | -57.89927 | 2025-09-07 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 83ee536a-10f4-3750-87e9-cbde34f5889a | -22.42109 | -47.43954 | 2025-09-07 04:23:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README64.md)
