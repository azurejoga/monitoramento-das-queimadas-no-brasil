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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8aba33ae-8ae4-32d7-87ce-0bd97fcf261a | -8.31484 | -44.75723 | 2026-09-22 11:45:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 58c12361-67d5-3924-8dcc-ccf1132983e1 | -5.33577 | -43.29545 | 2026-09-22 11:45:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| fe434be7-6335-3b01-9c1b-28723d851856 | -6.61572 | -51.44013 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5b29e880-0a45-3dbf-9bd3-36d8e276f45c | -9.63445 | -45.51624 | 2026-09-22 11:45:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 493ce9bc-551f-3a3d-b632-3accf388c080 | -6.93856 | -42.90186 | 2026-09-22 11:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.2 |
| d734672c-63d6-3428-bdc8-ca2b43d9585a | -9.53994 | -45.39021 | 2026-09-22 11:45:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 509590d7-f33a-381b-8ef3-c254752c334a | -3.4432 | -50.6091 | 2026-09-22 11:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 16632f94-d076-30bb-8442-f11c633c2960 | -7.42232 | -49.84694 | 2026-09-22 11:45:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| de8f660d-09f3-3695-98ec-e56877a0ff92 | -9.38754 | -47.76801 | 2026-09-22 11:45:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd57959e-114d-3131-8f88-f70a0d5bdf0e | -6.80516 | -43.90876 | 2026-09-22 11:45:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| afe27e54-3cec-3e7a-9ab3-0a465c3117cf | -8.77827 | -48.73169 | 2026-09-22 11:45:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 67f7e7a2-2fee-3df1-8c1a-995078262c02 | -8.81758 | -45.36134 | 2026-09-22 11:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 72afa446-1941-3342-a84d-655e9fd55abc | -8.41093 | -46.51285 | 2026-09-22 11:45:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 850cf895-3205-36f5-8b68-4a64ebee4ad8 | -9.78151 | -46.06726 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f0a87db-9f77-36f4-b462-5355b982881f | -5.82397 | -44.14297 | 2026-09-22 11:45:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4525663d-137f-31eb-baaa-5c899c1c7b2a | -3.34443 | -42.78373 | 2026-09-22 11:45:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 23916522-9f4d-3e9d-aa9b-234cc5d4c7b0 | -6.93669 | -42.91608 | 2026-09-22 11:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| af1e9a76-e737-3f81-96ff-76ed188b881d | -12.40596 | -46.51787 | 2026-09-22 11:47:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 490179bf-5b7f-38d9-9b96-4f49361bd8e7 | -11.42025 | -46.80543 | 2026-09-22 11:47:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 3c4acfc9-598d-3560-9d73-5aa3dfb5c48c | -11.11488 | -48.3222 | 2026-09-22 11:47:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 522c6e47-da9a-3ba0-a27c-ffc8c2320c27 | -11.31532 | -51.35508 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 6f68dcf8-7092-3bab-a4f9-4c36badb08f5 | -12.88552 | -50.90338 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cfee96eb-e07a-3361-a21e-e73a75d9f71a | -15.36654 | -48.11082 | 2026-09-22 11:47:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8898325a-c419-3b82-90fc-b2e89873b76d | -12.45711 | -47.03196 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 852221b5-8188-3b01-9e35-72447d470491 | -12.85078 | -50.9018 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 682cbfbe-b20b-3a21-a555-f4e7bee00975 | -12.96153 | -44.57597 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c155e94a-89fb-36df-ba3a-89b45eeee2e0 | -13.40369 | -49.47475 | 2026-09-22 11:47:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ba505063-518b-32b9-b63d-826fe92fb0ed | -12.92614 | -51.01385 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 47531bec-8736-3488-a76a-398adf9a9240 | -11.89155 | -46.8619 | 2026-09-22 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a0039baa-abb3-32e3-a350-d00dff386a0e | -11.8864 | -46.83177 | 2026-09-22 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f8a1078e-2f8c-30fd-b365-e13031a571cd | -15.44022 | -48.44129 | 2026-09-22 11:47:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5e07afdc-90ed-351a-aac8-c286cc0006a4 | -10.56601 | -46.71928 | 2026-09-22 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9bb8159c-913b-3d4d-8b69-0a973258ea26 | -12.1476 | -46.19889 | 2026-09-22 11:47:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b2bd75a2-436c-33ca-9946-cda5255ef0f3 | -12.84773 | -50.92209 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0fd66cc0-1bce-3231-aa62-7b65b77fde7f | -13.47727 | -42.67633 | 2026-09-22 11:47:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 8d7e2b7c-982e-3c27-a2a0-45ffbdc1b12d | -11.15047 | -51.09361 | 2026-09-22 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 2a3d9f9f-b65d-3b8e-8d01-b3bf13393a39 | -11.95563 | -46.51726 | 2026-09-22 11:47:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 80809653-9950-33bd-9158-ac058e026cad | -11.43534 | -47.35937 | 2026-09-22 11:47:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 492cb575-74df-3f60-bfc6-751ff117b952 | -14.7665 | -48.45158 | 2026-09-22 11:47:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 521316e0-61bb-31b1-aa8b-9216e1ae304b | -13.67011 | -41.54449 | 2026-09-22 11:47:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 3eb1eaec-df7b-3492-8de7-d1c3344ab4f5 | -15.26972 | -47.60743 | 2026-09-22 11:47:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9c2fd20-b9e8-34c7-877d-81e9b1dfa7e2 | -14.8156 | -41.16215 | 2026-09-22 11:47:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 4c205d8b-09c9-3830-88c7-9b459ee01d78 | -12.56792 | -45.98463 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e361cf96-ff7d-3637-9135-b2a7679eb000 | -14.68889 | -45.67253 | 2026-09-22 11:47:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 40b4f65b-fbfe-369c-89e4-881b63a8ee53 | -13.93927 | -48.56374 | 2026-09-22 11:47:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 281d352c-5128-3f8c-b023-5b6ba1787a53 | -15.44151 | -48.43202 | 2026-09-22 11:47:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 38596256-fd17-316d-8636-1d583be81920 | -11.42641 | -47.35808 | 2026-09-22 11:47:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 81590681-51c5-3ec3-a8cd-4b5a812101b0 | -12.6701 | -47.02501 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 857771ec-c6e0-3b16-bb1c-d067c4eaabe4 | -13.47505 | -42.69529 | 2026-09-22 11:47:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.4 |
| ce25a432-9d2e-3977-a115-1f2aaa503654 | -12.10933 | -45.65212 | 2026-09-22 11:47:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b136728c-8fa5-3705-b1d4-f190760f744a | -14.82894 | -52.3251 | 2026-09-22 11:47:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ce931f69-1447-36d3-b556-14a8ae3a690d | -12.10787 | -45.6632 | 2026-09-22 11:47:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b8d1b6e2-0fd6-32d6-a5de-8de9926ceb56 | -11.10735 | -48.31202 | 2026-09-22 11:47:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 0b7a603c-455c-33f1-a706-8b7dce432f33 | -11.80406 | -49.80845 | 2026-09-22 11:47:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 372ff354-3a7a-301a-ab19-b53a6adaf355 | -12.68498 | -50.96802 | 2026-09-22 11:47:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7c1e25ac-3e68-3ebb-b5fa-e8e49d5a95c6 | -11.88507 | -46.8414 | 2026-09-22 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4fdcc2b6-eef2-34aa-b3c0-6685ceccbca5 | -13.54057 | -47.66182 | 2026-09-22 11:47:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1dc44745-f34a-3a52-91e6-2a7e6c706ab4 | -12.68323 | -46.39165 | 2026-09-22 11:47:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fbc21d8f-989a-3dfd-9f91-03a601c9c0ce | -13.4724 | -43.58649 | 2026-09-22 11:47:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ee7bdf8f-69ce-3bce-b352-9bf4fcdbb18e | -12.94028 | -51.04753 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7df6c8ff-c2b0-3830-a60b-fe5967f17187 | -10.90864 | -47.37558 | 2026-09-22 11:47:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 208f295d-a264-362d-bb2e-e5f6ff8984cf | -12.39998 | -47.04745 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0fb5fc0d-83f6-3598-bc63-2ea836824ec8 | -13.66313 | -41.5384 | 2026-09-22 11:47:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 64.7 |
| a52cdc7f-c90c-3485-b840-784aa48c6a47 | -12.14719 | -45.12859 | 2026-09-22 11:47:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 40817b3b-1af3-3a68-9f97-fa2785d844f1 | -12.85859 | -50.91338 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 77a48ef6-cad4-33be-8dc1-4111dcf927c5 | -12.95986 | -44.5893 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 02e6c7e3-704c-3ad4-adc0-5c3be2aaaae8 | -15.35885 | -48.10021 | 2026-09-22 11:47:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b7b97342-1dac-340f-9dc4-d1e28aa7132f | -11.04159 | -54.14846 | 2026-09-22 11:47:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f8acfac1-4faf-3f27-a6ff-33a8e0349127 | -12.02628 | -47.81148 | 2026-09-22 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 73cb6160-9bcf-3b36-9823-c201ab3743fc | -15.35755 | -48.10963 | 2026-09-22 11:47:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2791ad6d-428b-3d3e-8f73-9d6c98cf3542 | -12.8933 | -50.91494 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8bd00d6a-3fa8-3498-a77e-11f8d1ef287f | -11.88374 | -46.85106 | 2026-09-22 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 22dd8ee2-163d-318e-b4ed-e641a730a963 | -13.07722 | -50.6227 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f7969489-e544-3d7c-8230-db9035a98d7e | -13.02506 | -50.59467 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| db5723e4-11d6-36ff-8689-70f330c9f68f | -12.14804 | -47.40408 | 2026-09-22 11:47:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| a62d6880-831f-3506-884f-7f35869e3ede | -14.04094 | -52.0476 | 2026-09-22 11:47:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f281ff1f-2b3d-35c4-951f-5c4d364c1af0 | -12.44147 | -47.01025 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ac55eef3-80c9-3ea2-a740-7f4767e4a8a6 | -11.57726 | -47.72646 | 2026-09-22 11:47:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f0bc64f-5b01-3e51-9457-dc04ba62b6d6 | -10.56471 | -46.72877 | 2026-09-22 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 009cb6ab-75fc-3c59-8afc-2a8a2a79db33 | -11.32508 | -51.35659 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 000f21f3-c8df-32c0-a47d-fd230f2745ad | -12.8523 | -50.89167 | 2026-09-22 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a8aaa92b-931d-3acd-afe1-4be07e101afa | -12.4493 | -47.02108 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 60c2497a-074f-30cb-be6a-706c0c2b825e | -14.75891 | -48.44113 | 2026-09-22 11:47:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8f876dd1-8905-3cc0-aa73-418271f1219a | -11.1681 | -51.10732 | 2026-09-22 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 05bfcd49-3ecb-3c58-805e-ea7dc7658bfd | -11.94632 | -46.51621 | 2026-09-22 11:47:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5bc20fd7-41a6-3bfc-8725-f2a0bce2c2fe | -13.86753 | -51.84669 | 2026-09-22 11:47:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 130bb332-ea0e-3fac-8ebf-7d3fe1a52f50 | -12.94929 | -50.92355 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| e1a8d8da-7e00-3c92-ac4d-7840d95bbe8d | -11.75604 | -50.8153 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 87c74370-4151-3ce5-940e-d30380b5ba07 | -11.38658 | -44.23424 | 2026-09-22 11:47:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| d9871bbb-18c8-3570-a5d7-80eced9fb2a4 | -11.60432 | -45.37625 | 2026-09-22 11:47:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 81065a02-814e-3031-8ec1-7901cacdbd70 | -13.89655 | -45.48878 | 2026-09-22 11:47:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d51b9660-8ef7-3c17-86dd-75526a4d9291 | -12.28827 | -50.70565 | 2026-09-22 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 29820380-84e5-3cca-875a-747c7c9299f7 | -14.81277 | -41.15649 | 2026-09-22 11:47:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 5658ec2c-902c-3805-8197-797ee95e4a8a | -12.14933 | -47.3948 | 2026-09-22 11:47:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 17117e37-4cb7-3c2e-a55f-0e5fd8d9369e | -12.57138 | -47.67342 | 2026-09-22 11:47:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 7e8cbed4-4563-3806-9d1c-737748c356d0 | -12.45842 | -47.02233 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| f9c17ac3-afa9-3cd0-86d8-0eedf36b7cb1 | -10.45589 | -51.27988 | 2026-09-22 11:47:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2e21a3a2-d2ac-3cc8-a48d-0f0afdbc2ddc | -12.40644 | -47.06787 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6e6a429b-7f9b-3c36-96de-1fa5394a4742 | -11.74033 | -50.79192 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6263d74d-edef-35cb-88a3-bccc6a4561c7 | -11.14321 | -42.83078 | 2026-09-22 11:47:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |


[Clique aqui para ver as próximas entradas](README125.md)
