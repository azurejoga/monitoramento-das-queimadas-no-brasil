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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56a4293e-1cc7-33c5-b41a-1f43ef9268b5 | -14.9815 | -54.7743 | 2025-08-18 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 0c779804-e7a5-36fc-8b64-2963e7bbba42 | -17.0838 | -49.8899 | 2025-08-18 03:10:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f129b322-7cc5-3a7e-8462-ef679e0a0fbb | -17.1036 | -49.8865 | 2025-08-18 03:10:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 132745de-7b90-3ce3-89eb-3b42a836f548 | -12.9971 | -56.8395 | 2025-08-18 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ca0191a7-1613-37f2-b3ae-ac592ad00dd6 | -17.0842 | -49.8677 | 2025-08-18 03:10:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| a5d7ed9e-5139-366c-aa98-55e3c2f055c7 | -17.3844 | -42.6235 | 2025-08-18 03:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 31b28e70-4f17-3bbc-afc7-0c1235818f74 | -21.43042 | -43.88437 | 2025-08-18 03:10:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 29fc0c78-443e-3ba9-bc2f-498471d5a7b8 | -9.4952 | -40.3834 | 2025-08-18 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 9e24b159-b709-3ea2-af19-bb7e286f1f93 | -9.518 | -60.5268 | 2025-08-18 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 48e018ec-c4a7-3b50-87e6-a1d09e9dcb6f | -9.4765 | -40.3613 | 2025-08-18 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 1f8b40de-5467-3665-b299-7b5696df8e6b | -17.1036 | -49.8865 | 2025-08-18 03:20:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 242c2de5-b543-3b1a-867d-2871af78526f | -9.4761 | -40.3862 | 2025-08-18 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 612adcc7-1a5c-32ce-ac69-953a98c74b0e | -14.9815 | -54.7743 | 2025-08-18 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 81b158f0-7219-36d8-af7a-0e70d2747c9a | -3.9819 | -42.5396 | 2025-08-18 03:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 90e31bb7-a3bf-39be-b57b-c21e6c7c3c0e | -17.104 | -49.8642 | 2025-08-18 03:20:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 57ec3b96-515e-3822-922e-9864babff6fd | -13.219 | -50.7566 | 2025-08-18 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 215f70ee-6e97-3b19-8c8a-48603a11923d | -9.4956 | -40.3586 | 2025-08-18 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 42fe6574-7e9e-36ee-9c71-e5d1d23a05f0 | -14.9622 | -54.7766 | 2025-08-18 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 7726a3ea-d652-3c7e-8b83-4ba8e32a23e3 | -17.104 | -49.8642 | 2025-08-18 03:30:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 880a8780-3e1f-376e-8db6-7e2ef761f067 | -9.518 | -60.5268 | 2025-08-18 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| c3ab964e-0752-3b48-89db-c11737a232c6 | -13.1746 | -54.9337 | 2025-08-18 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 838cc6d6-5f9e-3a2f-b8b9-871c45a58c9e | -23.6812 | -51.6361 | 2025-08-18 03:30:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 55.9 |
| 47b4f21b-e87a-3b10-bbdd-8aecb84b669f | -17.1036 | -49.8865 | 2025-08-18 03:30:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a18620c1-3717-33f8-a5f5-0a2b7876b70b | -19.1467 | -47.0279 | 2025-08-18 03:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 8b179969-93e1-3135-a036-0415ab0b052c | -3.79199 | -41.00006 | 2025-08-18 03:30:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f4a72b6a-4517-3a97-8b30-bdb33f2ee6bf | -3.97804 | -42.52127 | 2025-08-18 03:30:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 70e14050-426e-3b2e-a82d-fd803a8a867e | -3.98336 | -42.527 | 2025-08-18 03:30:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| e49a2c39-3f90-3c66-ae78-ad3e75abfc28 | -3.98846 | -42.52918 | 2025-08-18 03:30:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 831f4298-724e-3505-bbb9-31d181d8cb82 | -3.98949 | -42.52808 | 2025-08-18 03:30:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 97b70e99-53c1-3994-8511-4c180bd3b3e2 | -4.2527 | -38.69977 | 2025-08-18 03:30:00 | NPP-375D | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6d27462a-5a69-38fc-aab8-bdf7b2e559a2 | -3.98417 | -42.5223 | 2025-08-18 03:30:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9b0a5716-e604-3356-9513-ae786e92aa6d | -3.98256 | -42.53168 | 2025-08-18 03:30:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 6c623d0c-5f4a-3041-aae8-5c125bd357c0 | -3.79262 | -40.99636 | 2025-08-18 03:30:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0e1fadad-9a86-3e19-ae28-b124da5b1ae3 | -3.79136 | -41.00378 | 2025-08-18 03:30:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 25c2c45b-20cc-362e-8622-b45994a82de1 | -3.97724 | -42.52594 | 2025-08-18 03:30:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 99e3d4d1-09d8-3204-ac40-5b67668e06a6 | -3.98177 | -42.53634 | 2025-08-18 03:30:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| f6e484fa-af4e-3aa6-9d05-cae81126503c | -3.9893 | -42.52448 | 2025-08-18 03:30:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89944af8-0e43-3728-a920-d9b309cb85d6 | -4.25356 | -38.69469 | 2025-08-18 03:30:00 | NPP-375D | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03158949-8243-3805-9317-ab1fd549c36a | -7.8309 | -38.41734 | 2025-08-18 03:32:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e437e3f1-329f-359f-8957-ab0f4cb17e1e | -6.55361 | -44.47349 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dcaf934c-590a-397e-bc9e-2e795a627ad1 | -6.4313 | -44.77884 | 2025-08-18 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8fd52ca6-a335-34ee-9d9f-03f0e396db19 | -5.66835 | -43.38728 | 2025-08-18 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4d151ed-39af-3618-b60a-f5aba7fb5b93 | -11.80111 | -44.94019 | 2025-08-18 03:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f5c0dbf-9c52-3d4a-ab63-82d888d22134 | -6.55912 | -44.48063 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| daae6d50-6a5c-3dfc-a1a3-5bc8b5b7efc1 | -6.14509 | -42.70453 | 2025-08-18 03:32:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8322818-1d97-335c-9771-84424c3510af | -11.90744 | -43.42477 | 2025-08-18 03:32:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20c9e105-e0d9-3697-9b0d-35d83cfc0af7 | -7.20064 | -43.97392 | 2025-08-18 03:32:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b158758-4036-32b9-988e-ddad2dc231cd | -7.60691 | -40.49414 | 2025-08-18 03:32:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e9331f2-dc2c-36cf-8968-1a98f51ce0c2 | -8.50304 | -44.7393 | 2025-08-18 03:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22cb7700-f58a-34dd-a814-dc80d524f096 | -5.78425 | -38.04738 | 2025-08-18 03:32:00 | NPP-375D | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6510db01-f34f-3da9-95d6-1a0ed564d646 | -6.55541 | -44.47857 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| efd62743-99a7-3718-a068-d25307042f8a | -6.98329 | -41.62755 | 2025-08-18 03:32:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bf586d21-b392-36c1-b78d-6b86ff38b220 | -4.78377 | -45.32467 | 2025-08-18 03:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ceb228e-3f48-3ce1-9f2e-a12f50cf4408 | -6.43251 | -44.77232 | 2025-08-18 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9191d1f1-f5eb-34d7-8682-ee004e33848e | -8.50468 | -44.73907 | 2025-08-18 03:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 634189bc-d730-3ae6-be5f-74fe68ace3a0 | -6.15181 | -42.70153 | 2025-08-18 03:32:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1f96551-78fa-32e4-9cd4-2d00a8fbc488 | -6.55642 | -44.47298 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1df2b36-bf60-38c3-95b5-f12f7424ffec | -7.60638 | -40.49709 | 2025-08-18 03:32:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f1d1918-896d-3e23-9212-d8db19016454 | -6.67669 | -41.76697 | 2025-08-18 03:32:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bc61f3de-014f-3315-a148-2381e619fa54 | -6.56399 | -44.46894 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b2017de-518d-389a-b385-4d51c37b7d47 | -8.49817 | -44.73779 | 2025-08-18 03:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96bb13c1-c98d-3490-9571-9a303aba2653 | -11.80421 | -44.943 | 2025-08-18 03:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f730769-a85a-379b-8704-183594b0045d | -9.74882 | -37.91596 | 2025-08-18 03:32:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 078e057f-36f2-3e51-a2d0-21757a1681ee | -6.43687 | -44.78645 | 2025-08-18 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c6b09230-fe60-3a56-b65c-6faefe0db556 | -6.98261 | -41.63129 | 2025-08-18 03:32:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1a60e2b8-19f2-349a-9e91-04a4fe220d1e | -11.00118 | -45.65194 | 2025-08-18 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6605b141-fb32-3d41-8461-7153ee3ec306 | -7.83161 | -38.41312 | 2025-08-18 03:32:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b228b08-f9bb-3023-babb-b6cd0776e222 | -6.67041 | -41.76991 | 2025-08-18 03:32:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b992e5f9-a44f-337b-823c-15ddf45fd361 | -7.5056 | -44.98635 | 2025-08-18 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 857dd901-c2e3-3294-befd-7f78e9ce329b | -11.80733 | -44.94156 | 2025-08-18 03:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d102b69-acc0-3bb6-bcb6-3a773fbd4664 | -6.43573 | -44.79264 | 2025-08-18 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c2bb58a2-dd37-387f-8ffb-72052a595495 | -6.15104 | -42.70579 | 2025-08-18 03:32:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2fd55c6d-ec9a-311b-b639-33c61ff1e832 | -6.5678 | -44.47083 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 002c0c12-e0f5-3042-bdaf-a18e6f6037c8 | -7.83138 | -38.41581 | 2025-08-18 03:32:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2d3cb93b-b20d-330b-81fe-ece79b832d51 | -4.7715 | -45.32418 | 2025-08-18 03:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3124d60d-89ba-3c46-91c4-3496cca783fe | -4.77863 | -45.32551 | 2025-08-18 03:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a624ffe-ee8a-3515-9f81-6a28a4a4e979 | -6.42349 | -44.78331 | 2025-08-18 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68e3c047-76a3-3027-add9-90d629d76e02 | -6.90301 | -39.54903 | 2025-08-18 03:32:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2379a3e0-e6e7-3afa-95aa-9f58c8d988e1 | -9.86841 | -44.69773 | 2025-08-18 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f649bab-c0b2-37a6-a709-5bb7cb6ba6e0 | -6.90782 | -39.5498 | 2025-08-18 03:32:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a90a185c-8f83-3d79-80f1-971e7829029f | -7.51322 | -44.99588 | 2025-08-18 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cf44a0b-d125-3b21-9d1c-5659a166a63d | -6.56019 | -44.47494 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b376297-3e57-33a1-8ae0-3f5a96704b18 | -5.66573 | -43.38476 | 2025-08-18 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34f69eb5-7dfb-38aa-a221-aec5f51ddda2 | -11.90182 | -43.42339 | 2025-08-18 03:32:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 432ad956-9ea8-3520-9df6-7201fda64c19 | -5.66205 | -43.38619 | 2025-08-18 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4558fc40-6dfd-3813-883e-e802935b289a | -9.48703 | -40.37544 | 2025-08-18 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 79c0af35-962d-3e3f-b7a6-74f94647bc6f | -6.56123 | -44.46935 | 2025-08-18 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7603ac46-a99b-3088-b3ef-72aafa8f9216 | -6.43017 | -44.78496 | 2025-08-18 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e0f24779-2a78-38df-b69e-43924589aa20 | -11.00256 | -45.65734 | 2025-08-18 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2bd0cfa-7d73-3421-9efe-ff180e3e45cb | -7.51459 | -44.98876 | 2025-08-18 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7936f6e-c7d3-342b-9499-c5a464a14774 | -5.67288 | -43.38101 | 2025-08-18 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e87b0c9-fc64-3b83-9756-efe7a3754aa5 | -9.49285 | -40.37096 | 2025-08-18 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ed8e7cb8-8049-3066-a1b9-86037407a33f | -6.90688 | -39.55508 | 2025-08-18 03:32:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 17ef4fe9-7a41-32c8-9818-400deb06e11c | -7.51108 | -44.99429 | 2025-08-18 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7d5d593-734c-38ab-84b0-b5d479199349 | -6.42905 | -44.79097 | 2025-08-18 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f5260305-ffea-3fe4-83f9-47b056dc6ae6 | -5.66927 | -43.38225 | 2025-08-18 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54c49e2c-4993-333d-8380-3e7b9bcd78f4 | -5.66111 | -43.39133 | 2025-08-18 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcd19833-0248-32cb-97af-cfc6ee7d87a4 | -9.87577 | -44.69383 | 2025-08-18 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4990e8bc-0f35-3c8b-b8f8-631b1fc5d23e | -4.78255 | -45.33149 | 2025-08-18 03:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f488b4e-758d-31ba-9e8c-deac23849cba | -6.98396 | -41.62385 | 2025-08-18 03:32:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
