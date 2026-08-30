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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f13beef5-eb93-32cd-a451-2a424a7b7916 | -11.23315 | -45.0941 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94c95378-1ea4-3935-8ca7-8384ebbabf4e | -8.62037 | -54.72839 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c3942da-c405-3c75-9cf3-b6c65c52b033 | -12.08715 | -47.18906 | 2026-08-30 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecf7d417-bed8-326c-8361-bdf25c2e299c | -16.27632 | -42.57578 | 2026-08-30 04:34:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b99747d5-57b9-3805-be51-cc0c3fbe6d37 | -11.29396 | -54.02942 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0810fddc-00cc-39f5-b4c9-f586775591ce | -14.45434 | -58.43999 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39255338-91c3-3303-b103-4363c32b082b | -10.56702 | -59.61557 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea037859-0c1f-3e72-a264-0e2498a7e40f | -11.82065 | -51.04829 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| ed66fc6e-8191-3bb0-8711-6aeb99046ed4 | -11.29593 | -54.04342 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 04c48fb2-2eef-3a05-9813-11419a26f46d | -12.90541 | -45.85178 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d42dcc7b-6dd5-3a0c-9623-72bde4af5b3e | -15.13431 | -50.63275 | 2026-08-30 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 02cee767-e27e-3102-b494-08596fa93b1a | -17.2889 | -46.01092 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8100fe1d-33b4-376d-b353-9e037fb27f3c | -14.14205 | -52.84278 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 154a80f9-6df9-358c-9e6a-8262b1854334 | -11.21336 | -45.083 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93ebe735-d3f6-321b-9af2-96944f6ea08b | -16.36338 | -51.00758 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5dcad0dd-3849-3863-b917-39ee7cbd2836 | -9.17165 | -59.61578 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 710e6de2-55f0-32b1-bd46-ff6fc1ebcb23 | -14.7623 | -48.74179 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd9546bd-792f-3443-a188-913a413205d3 | -14.20705 | -52.86044 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 370f6d64-3faa-37df-a5ce-8e25a44cdca0 | -11.80253 | -51.04196 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 837a0570-b02c-3fa0-8ab0-b69658da0f5b | -10.814 | -50.50577 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0f9a27c-94ad-3219-9c15-cfdf4cc457ad | -9.93254 | -60.52222 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8bf53da4-b1e8-30da-96a2-493ef761a7cb | -11.23542 | -45.10262 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99374f2a-94cd-3dc2-8702-cafa7996219b | -14.27898 | -57.04404 | 2026-08-30 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7510fa75-b260-3161-8198-e1a7b1ab5bb8 | -10.79006 | -45.33388 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07be1be8-c58e-3068-a42d-6ed6423b3806 | -10.74949 | -54.04206 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00b22c0e-2188-337e-b627-ae1f9bae7306 | -11.18907 | -55.10029 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4819dfa-d3cc-3c0d-970e-b3072f512318 | -9.10019 | -50.60997 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39ddafbe-d634-3514-9984-7ccb8127526f | -9.15368 | -59.50284 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78d91eb8-d157-3b6e-b925-49ab1f2f47e9 | -10.76534 | -44.86845 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17014567-2d2d-3783-87da-e377cf00fe92 | -8.49688 | -55.3026 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 480f36bc-4576-3fbb-baab-47cefe87bf24 | -11.00531 | -49.68891 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56aa7bcc-8aad-3268-bd97-a1cba2a9befc | -7.30335 | -60.59774 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fb0305b-7470-3677-bd37-f04600376d06 | -14.67785 | -48.05248 | 2026-08-30 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cf9cf79-5ac2-3ff2-86c8-0b292bf0ae50 | -13.85545 | -54.10963 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d43f9bd6-be75-31d7-8931-63818b1cad46 | -15.12959 | -50.63987 | 2026-08-30 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71b6d30a-709d-331a-a01b-9fcc1e5d5aa7 | -10.7538 | -54.0361 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 075ff18a-8fed-3548-898c-446504b777e5 | -11.79747 | -51.0499 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| b968d242-8e74-34cc-a7c3-e27526a601fe | -12.90539 | -45.87537 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8859a5b-fea5-3602-89d7-2574e5d6348b | -14.45091 | -58.4786 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fe4be29-fbb7-3f68-ba4a-d8730fabb113 | -9.88592 | -60.28598 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eafc01cf-99bf-3379-ac40-46b4880b0081 | -10.7415 | -50.66179 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b921b00-6fa6-3b44-a550-9f60abf6ff89 | -9.42065 | -51.58824 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee348d42-8e4c-3c6e-abcf-f153ef3ddac9 | -16.3522 | -50.98952 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e64944bc-00b2-3fb9-9ba9-506f44791941 | -10.81107 | -50.51048 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c74e4fd7-1ace-3a33-8eb7-abc33564b825 | -10.79121 | -45.32626 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 558845b0-0610-3ddf-baba-aa472e0dba81 | -10.14624 | -45.70124 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9db4be31-6e76-3bd8-92e8-33843796a8c1 | -11.81051 | -51.04209 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| ea28140e-ef91-3e1e-8941-aa4dd08a32d5 | -10.8133 | -50.50991 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45bc2aa1-5866-358c-8195-ab57d085cd9d | -11.22093 | -45.08027 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 996f5492-fbc2-3e1c-8a94-133df01d41f1 | -15.22764 | -57.65712 | 2026-08-30 04:34:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d534dec6-ea80-3fde-96d9-f1ef814ca3ea | -12.37292 | -48.1966 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff3b8a1f-9747-36b5-98b9-7dbeb33add42 | -15.10134 | -48.16633 | 2026-08-30 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adb93460-6e75-32c5-ac6e-5a14b84ffac6 | -11.35967 | -45.17184 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f9887d3-aa12-32c0-adca-76aa54bfcf80 | -11.24074 | -45.09124 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6c0b7ad-e14c-3325-a21a-3a9dc1561bd8 | -10.79178 | -45.32244 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c471fc24-9d72-3b55-ab15-95c33f595153 | -8.22959 | -54.95612 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21b3f916-a653-3128-b272-9bcbe27044e4 | -14.15905 | -52.81479 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d1eb549a-09ff-3991-9379-38c493036dc6 | -14.41521 | -52.55416 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e9b19b6-8103-3cf4-a6f7-334ae3531e5e | -11.6553 | -46.756 | 2026-08-30 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38b55d71-ddc1-353f-b14f-a6936ce11ceb | -9.70529 | -60.73101 | 2026-08-30 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d3ca311-c2e4-3601-bc49-a642e828e9f0 | -9.41516 | -56.98477 | 2026-08-30 04:34:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee3785d7-12e4-3f3a-bfa3-d4617e4bca2c | -9.66391 | -50.8512 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 160aae70-bb53-33e9-8223-8c2f3458a203 | -12.93177 | -45.88731 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d47a4a8-b525-3446-8201-9de3a4f5b9bc | -11.82213 | -51.03973 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 04e4974b-9f9f-3d5c-a3db-e2e33460466f | -17.27569 | -46.01067 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b88d8a3-6cc9-38c3-950e-d99f388e7d98 | -9.66464 | -50.84678 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 330b3242-6ffa-36cb-8b60-46ed8631298c | -12.08604 | -47.19614 | 2026-08-30 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fb1b588-8d0d-301a-baf0-e8525c283702 | -9.20417 | -51.53635 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6125122-6842-357e-8246-f5fd400982fa | -11.35036 | -45.1624 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b82d464b-7401-3451-a4f9-a21a7522ad87 | -12.89794 | -45.87816 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b51af1dc-6278-3cfc-a43f-ee0f7ce35aaf | -14.90286 | -47.74126 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc630c25-de54-3397-8706-af7c8620a978 | -9.65975 | -55.11015 | 2026-08-30 04:34:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ecf8fe23-94be-3665-ba11-222af041713d | -16.35004 | -50.98127 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fbedb1c-e18e-3cef-86f7-b0bec8a21c20 | -11.52957 | -45.55695 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9476664-32f9-32f4-aa65-a64888972021 | -14.27838 | -57.04712 | 2026-08-30 04:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4983959a-d2ec-30a4-986b-3ebf5ab9af1c | -12.07607 | -47.19453 | 2026-08-30 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9af4ae4-cea3-3d55-8d41-48c0d9603bcd | -14.13879 | -52.81625 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8473ddcf-ea29-3a5a-8a0f-a5aeda7f6758 | -12.37904 | -48.1795 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a1adeb4-9bd6-3a4d-9a4a-36ee4f36c10a | -9.83227 | -47.83157 | 2026-08-30 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02c07364-566e-3f07-be1c-ab85d1d03f4f | -9.68563 | -46.54608 | 2026-08-30 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bc18df8-84e7-3704-a96c-ef29a56fdb8c | -14.19761 | -52.86856 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 88ee6c9f-5766-3f17-8b43-9085476ae6bb | -10.81881 | -45.33047 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03689f8f-996e-326a-beb4-58c8b15f453d | -11.4804 | -45.06484 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 977f8d11-46bb-35a7-96f1-32b575d989e7 | -10.12938 | -45.69802 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fe49cb3-80cf-325d-abde-c939492c398b | -11.63426 | -54.59106 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7dd67e9-56e8-3bee-af33-31f735352432 | -14.55931 | -52.08288 | 2026-08-30 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7512387-1bbd-3cbc-bf97-658061729214 | -11.03727 | -57.21802 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 917448e1-e22c-3c23-ba1d-e260ce056138 | -10.86258 | -50.50141 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3195473a-f2b9-3eea-a20e-4d5e7a8798b3 | -14.45821 | -53.41389 | 2026-08-30 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8b48af8-1041-398b-926d-61136315e486 | -11.34979 | -45.16629 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fc42134-857c-3cfc-bfe8-28304790591f | -11.2427 | -54.01227 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 22374b58-6263-3008-b907-718e4e717506 | -15.97242 | -44.87626 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6cca0c0-8eff-327d-a9ac-074946b696e7 | -9.4665 | -51.58311 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6833e8f6-d3d2-308b-af68-b819fc610783 | -10.94518 | -43.02435 | 2026-08-30 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a820eae9-1253-31a2-8ec0-e6c844f806ae | -10.74897 | -54.06255 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fbbd4c3-3e8e-3f5b-bcd0-4be5a8cf805a | -14.24647 | -54.65267 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7b4fd68-0f29-3c90-9a19-de9bc1581066 | -12.91972 | -45.89717 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e9d7d960-8e2f-35e7-841b-2ed58232acd2 | -9.17184 | -59.61889 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e793b653-45b9-3e60-bd47-49200b281953 | -11.02381 | -49.68417 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b0fa714-f85c-3e0e-9bb3-7108332d32fc | -11.8185 | -51.03909 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README45.md)
