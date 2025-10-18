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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e589ad02-5479-32e9-9fbc-4ef75806b33d | -18.24006 | -42.5108 | 2025-10-18 04:04:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5feede21-c18e-3848-ae15-afffd8e2887d | -17.8851 | -42.25822 | 2025-10-18 04:04:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 941cd73a-e76e-3911-98b9-aedd41781a77 | -14.91301 | -46.72852 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 886a9f7d-2982-324f-abcd-8ba2a593fb36 | -16.59242 | -42.43183 | 2025-10-18 04:04:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f51bad8-9b5e-38f0-9d65-b72bc23caff1 | -15.0483 | -46.60665 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e6bdc119-e386-32fb-b14e-536d16943db2 | -14.26296 | -51.8642 | 2025-10-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 838e3600-4a78-3866-aaf9-22fdc6fecdac | -14.9277 | -46.71475 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03b8788a-2fa0-3cf1-8dd4-fd264fcc2d89 | -14.92286 | -46.71905 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2880c0f-d757-33ea-a3e9-3e8565e06609 | -15.60207 | -42.38939 | 2025-10-18 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a83c4d7-9c41-357c-8c3e-680dfa844947 | -15.08127 | -48.45858 | 2025-10-18 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8a2b5ec-6465-356e-9199-41f7d1e93a38 | -14.92375 | -46.71415 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 088731cf-e1f3-301e-8c61-57d7639ee541 | -15.92633 | -45.69807 | 2025-10-18 04:04:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e171e332-e3bd-3fa7-ac49-0247a7e2f862 | -14.92052 | -46.71177 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ffda31de-014f-38ca-8fc3-a77a456b4e63 | -17.72647 | -44.36131 | 2025-10-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 988e729d-0491-3bc5-baa1-da96a7af82a0 | -14.90769 | -52.4061 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87c29b9f-70a7-34de-91f5-2fa0275efc26 | -14.93736 | -46.70623 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 45bac2da-8bfd-3210-810e-30ab0c55e11f | -15.96252 | -41.8721 | 2025-10-18 04:04:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81677209-e7b0-3960-9423-d0deb8ec6a04 | -15.52998 | -45.70324 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d59c57f-7311-3426-8569-900e2e0dbb99 | -15.77313 | -41.33494 | 2025-10-18 04:04:00 | NOAA-21 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b351906f-0bb4-36d3-8570-5cb02e833024 | -17.49314 | -43.46498 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b734961-5533-3aca-a270-b5a6c2c028eb | -15.05612 | -46.60795 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36fdc666-b0c6-3cfe-9c4d-1bb2ae83a093 | -15.78999 | -43.64939 | 2025-10-18 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad560e9e-7bd4-33d2-af64-57e0ed6ebb98 | -17.12632 | -42.78011 | 2025-10-18 04:04:00 | NOAA-21 | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dc0f37b9-8b40-3b83-98fb-17e67eebcfd4 | -15.09126 | -44.00124 | 2025-10-18 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40fe942b-c187-3fc2-9823-cedd2f14f6b4 | -15.74915 | -41.90959 | 2025-10-18 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df7ec2fb-283f-396e-9974-2082abf5f4d6 | -17.98067 | -47.88266 | 2025-10-18 04:04:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dee498e-249f-3d7a-8c54-a2789e167787 | -16.20382 | -44.75488 | 2025-10-18 04:04:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab77c570-0c2b-3b9a-8941-a2b6bb077c46 | -14.90362 | -52.39706 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e022b8ac-7a76-32bb-a227-2a82ebe238ba | -17.49374 | -43.46129 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 507e11c0-5b9a-31cb-bc10-9c517dd65823 | -18.40338 | -41.82675 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7e587278-caab-311f-b893-b15c313a94eb | -18.37649 | -55.43758 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4360709b-5ff6-3c3f-93bd-7e9872a7e222 | -14.26188 | -51.8638 | 2025-10-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 08a1af48-4181-349f-9fb6-5c012c336324 | -19.56677 | -45.34385 | 2025-10-18 04:04:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 022029eb-d25d-32cc-8f16-73f1169e1a27 | -15.45184 | -45.93982 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5bc2e2d-05bc-3883-93f1-559efc35b787 | -14.91386 | -46.72663 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2092a5fd-c749-3209-bc5f-41a99cbb48f2 | -15.96582 | -41.87265 | 2025-10-18 04:04:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98ae7589-82c8-3a30-9740-322e2e50db11 | -14.97561 | -47.09591 | 2025-10-18 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24889640-b738-371a-9375-0020a72b8408 | -14.9189 | -46.71851 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb0f1e57-b3eb-3bae-9c93-1261fe973f21 | -15.53156 | -45.69432 | 2025-10-18 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 030c31d7-8d5d-3767-a6a6-8221f724d252 | -15.04179 | -46.61882 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d68bc226-67f8-3360-b4fc-5c115999489b | -17.49042 | -43.46068 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fe762a2-32ba-3610-a705-1b1f1b1527ec | -14.90685 | -52.39285 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 444d800e-43f8-3eda-8a43-205e6cbc8cac | -18.38172 | -55.47368 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 2ac6db47-8cff-3606-a164-57ef7131e31a | -17.1945 | -46.9688 | 2025-10-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59baaf14-29ba-3d65-80ad-61fea409117c | -15.77644 | -41.33548 | 2025-10-18 04:04:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 808fd449-9b70-36cf-8dcb-6472b51b4bf2 | -14.50406 | -45.61246 | 2025-10-18 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 198a53fd-aebc-35df-a4f2-cb2223499bc5 | -15.79336 | -43.64998 | 2025-10-18 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17959119-3de8-3b5b-a4cd-01da8379152b | -15.46492 | -43.20294 | 2025-10-18 04:04:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c0a7dfcf-6c2a-359a-a9de-3477119eae58 | -18.28087 | -42.59956 | 2025-10-18 04:04:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f98e732c-bac3-3852-9190-a0e131b593a6 | -19.86487 | -43.66544 | 2025-10-18 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 208ac40d-059a-3ca2-b269-b33ec01a7dc0 | -15.52824 | -41.2026 | 2025-10-18 04:04:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e91c244-176a-31b7-8f54-430b299408d0 | -18.38682 | -55.48076 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 014e0366-41c6-3f66-ae01-07ad1a8ef689 | -15.55761 | -42.34905 | 2025-10-18 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e467081b-4d2e-384c-ab3b-5e3a937d86c6 | -15.5465 | -47.27755 | 2025-10-18 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d70cf5e5-c427-3cb2-9f21-3c81786c3715 | -18.4056 | -41.83459 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 28b30ef8-d7cb-322c-834f-6b9717908014 | -18.39316 | -55.48234 | 2025-10-18 04:04:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d9d619eb-6ebb-33d8-a9c4-1a93d977765d | -18.40671 | -41.8273 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e497bc0f-82a3-3ecb-91ca-cbda828c00fc | -14.91965 | -46.71671 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5aa6e4e-b948-3c3a-b1fd-aee99384516b | -14.92842 | -46.71299 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 074d8e50-1a2a-3366-8036-5b0a818b178f | -15.04831 | -46.60451 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33db5429-0320-3b03-8aea-987add21084b | -19.59012 | -42.0222 | 2025-10-18 04:04:00 | NOAA-21 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7492eedf-5a87-3d49-95e1-64454eb4e2fb | -14.90519 | -52.38931 | 2025-10-18 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5281f8ef-2f88-31e0-a5cd-f98a2b20218d | -14.93184 | -48.52769 | 2025-10-18 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99b35ce4-eb15-33c6-9101-c88f5680c743 | -17.62322 | -44.72418 | 2025-10-18 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4de1717c-1055-3eae-9761-57e7d3316f75 | -18.12846 | -42.74735 | 2025-10-18 04:04:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a8b308bb-5f54-3e1e-9097-57605ee2fddf | -15.78362 | -41.33295 | 2025-10-18 04:04:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| a91019ee-78c7-3a5a-be66-9cfea76a828b | -14.91397 | -46.72322 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 152c402c-2b12-3e45-bf2c-ea3aff9a6caa | -18.39728 | -41.84445 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cbc87f2d-3dda-3a21-b662-28202eae887f | -15.05222 | -46.60723 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e0666c9-c6c2-3a95-9b4c-e9004f336811 | -18.40837 | -41.83878 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6ce356d2-0c56-3afa-9159-c85b01abd1aa | -17.84543 | -42.62131 | 2025-10-18 04:04:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 621e1211-f097-36e6-8934-6e11a00bea4d | -15.0591 | -46.61375 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cc7d3bc-082f-3034-a74b-c979f2dd9a13 | -17.95895 | -41.97734 | 2025-10-18 04:04:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c42f5062-0e1a-38cf-b3e6-885ee0ccfcde | -14.26925 | -51.86156 | 2025-10-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| edd0d974-7837-3cb0-a465-fc38677061a7 | -14.93163 | -46.71547 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a91eb6c8-2324-34bb-be8c-8fad8256790b | -15.60151 | -42.39296 | 2025-10-18 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f42d015-c449-36e7-94e1-cc94e470ce94 | -16.19505 | -44.2176 | 2025-10-18 04:04:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c50f7f6a-cc6b-38bb-8107-aecbc5125439 | -17.19263 | -46.97912 | 2025-10-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 929380b0-3092-302b-a601-56ba21e3935c | -17.50099 | -43.45877 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bb0a74a-c32c-370f-b362-f228fb437c91 | -18.40227 | -41.83405 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 8a0ae2c7-a7de-313c-a6ec-e65a3a13c258 | -17.72618 | -44.35798 | 2025-10-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53345734-64fb-35bb-ae52-a79857870480 | -17.50039 | -43.46246 | 2025-10-18 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7fd184b-72fd-3717-98cf-704bbca51632 | -15.25317 | -43.2495 | 2025-10-18 04:04:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8125ad7-0516-3ac5-9f3c-0f2e4c250e0e | -20.05325 | -44.75015 | 2025-10-18 04:04:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e63b660-9af8-335b-ab73-6450875a4aae | -18.40504 | -41.83823 | 2025-10-18 04:04:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4a6bb72f-faac-3ab3-aa27-04f8c49c6a15 | -15.4716 | -42.8867 | 2025-10-18 04:04:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 817a42ec-6a02-3c49-9a59-0684e0bb6761 | -17.8493 | -42.61827 | 2025-10-18 04:04:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d69ed2c6-7af8-3f66-82ca-5cf6068f4874 | -19.21004 | -42.92213 | 2025-10-18 04:04:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cb3b801b-98d3-3981-89e8-483139bda997 | -20.69868 | -42.5756 | 2025-10-18 04:04:00 | NOAA-21 | CANAÃ | MINAS GERAIS | Brasil | 3111705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c9cc4f27-fa1c-3776-af2e-3249eeac7d18 | -17.94495 | -44.28989 | 2025-10-18 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2e9b7ce-c4f6-3bda-a0a4-0fd52b234020 | -15.04747 | -46.60933 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 055116cf-28e3-3449-8b54-026bbf374b4a | -15.04437 | -46.6061 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0ed2690-d7a4-3e11-b329-3ff17554d353 | -15.37594 | -43.03744 | 2025-10-18 04:04:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f693421b-7550-3e68-b4bb-3f1980e08eaf | -14.91979 | -46.71357 | 2025-10-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c6f1e5a-e4f4-383b-9527-2a11fa331b62 | -14.2682 | -51.86116 | 2025-10-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d701c559-e00f-3f03-97cb-25e55067157f | -17.37219 | -46.67638 | 2025-10-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 792e29d9-dc9b-3b22-a67c-e33c495e6f88 | -16.46834 | -43.04158 | 2025-10-18 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30c1c9a0-3f8b-36d2-9513-ae6a9bbb13fa | -15.08718 | -44.0045 | 2025-10-18 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bce73dd-3995-3e4c-807b-42825f208f27 | -15.575 | -42.12858 | 2025-10-18 04:04:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17b7151e-f7de-35e2-beaa-eaba9e8279dc | -17.96443 | -46.74655 | 2025-10-18 04:04:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README35.md)
