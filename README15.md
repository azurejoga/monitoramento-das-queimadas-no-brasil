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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2a31ff7-0ebf-344f-a21c-a40c02608fbf | -7.7916 | -61.178799 | 2026-08-20 01:02:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c57b63fe-52cd-33e2-900e-9f7b98126cbe | -6.8042 | -59.013901 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a310a1d-b40a-33e5-bf99-089df5c80485 | -6.8686 | -51.864498 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82675d03-313e-3b90-b50c-507750b9c113 | -6.7072 | -59.086201 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a57f5650-d26c-3185-b7e9-3f99e89f2e7a | -13.5639 | -51.6656 | 2026-08-20 01:02:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b24ed68d-5fe9-33c2-bd39-e997f9c08b01 | -17.3256 | -43.606098 | 2026-08-20 01:02:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 06a009f9-c5db-39d3-9dee-02cedc2def01 | -11.2235 | -55.049 | 2026-08-20 01:02:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f57419f3-e0f2-3dff-b672-7fd5def23678 | -17.335199 | -43.603298 | 2026-08-20 01:02:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1fa94e-a61d-325d-b0d5-ed07029b25f8 | -13.4385 | -43.840302 | 2026-08-20 01:02:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 721cfc7f-b12a-33e9-b3f6-3371a4ece08c | -8.6605 | -54.5896 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b4abbad-f641-329f-92cb-5e15e725df1d | -8.6745 | -54.651901 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9323c645-66ee-3aae-b3f1-0a72657baef7 | -6.6929 | -52.084599 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 175df033-fe2c-3eef-8d6f-69ac7a83d5e5 | -11.2066 | -54.001202 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f17dc7e6-e592-3962-ad95-703f405a82e6 | -14.2415 | -53.109001 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5315b69c-adbf-3f05-b644-ae2cd578981a | -6.6947 | -58.9352 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e502ccf1-ae65-3134-8f62-f5c1686d811e | -9.4607 | -51.603298 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee67bac-c049-3ecb-81e9-cb1eb8e1f974 | -9.4589 | -51.5956 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00903ab-c655-32db-b033-1c093395c96b | -6.4267 | -52.760502 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f4d9e5-eaa7-31e8-a78a-9b991f7d6270 | -9.5104 | -51.639801 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9106a4c-a9aa-32a1-855f-3cddce62873a | -14.1686 | -53.0592 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0bfb7526-75d3-3073-9212-786902cde45e | -6.9157 | -59.337601 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28e7bd25-5771-3550-b9d8-d4ab54724ed8 | -23.079901 | -49.156799 | 2026-08-20 01:02:00 | METOP-C | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6b9c4683-027c-391c-a52b-937764718f23 | -11.2082 | -54.008202 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52ea6391-a8d8-36e3-bf3b-4faac1196f26 | -8.5921 | -54.743301 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de6b5227-4dfd-3b0e-994e-2c2223ed0c4d | -5.8063 | -55.729099 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3e8dbc6-b274-305c-9d0c-bc9a0ea3c3c2 | -6.3111 | -55.912498 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2aec94-2255-389f-96c6-6ffb38f2a5b1 | -8.6714 | -54.6381 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ddf4700-5e4b-3dfa-82e6-95f43d65f0ce | -6.7044 | -58.933102 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1b3e5a0-9f6d-3923-8dcb-5b520e125c7e | -8.8893 | -60.538101 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ca125a5-2066-3393-bf5b-b4ba3d105d85 | -8.5289 | -54.874298 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8debdb70-69f7-349c-831c-1713f722945f | -23.070101 | -49.159401 | 2026-08-20 01:02:00 | METOP-C | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 22304467-9d8b-37b7-92da-165e5169de43 | -2.8085 | -48.585899 | 2026-08-20 01:02:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad0d9c0-2d95-3816-8603-e45cb6b61ced | -9.1305 | -51.1199 | 2026-08-20 01:02:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2206f979-cb1b-350b-ad66-3242aa92c94e | -6.5814 | -58.9799 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45c4267c-36d4-3158-80bf-a1a91bc126d1 | -8.5273 | -54.867298 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd294ac9-3e97-335d-a9bd-f7ea0357c53f | -15.0088 | -52.716099 | 2026-08-20 01:02:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56311200-9258-3e3d-9b00-70033033acbf | -9.1053 | -61.573502 | 2026-08-20 01:02:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 259c3b8b-32db-3cd9-a940-dfc9d67378e7 | -8.1557 | -55.001499 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2054ff-1d75-3104-947c-b76b58626864 | -8.5371 | -54.865101 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f4a8c5b-c608-363b-85a0-b07607cc9960 | -6.3494 | -54.897301 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac06e81-6c72-3d7b-9b83-428e611b2e6d | -6.3784 | -54.934101 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f377a600-bff4-3385-a141-e1b8d3f22c99 | -8.6828 | -54.642799 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 133e09aa-ab9a-396e-b4d4-18d8d738963f | -11.1984 | -54.010502 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acd94a1d-c15e-3f5b-a3a2-95be86f9531a | -8.5411 | -54.791199 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcac8a05-617a-347b-bfd1-054700e17fde | -6.2398 | -55.4137 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8987ae94-1072-3d1a-a389-d0edeb57401b | -6.879 | -56.424301 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5edc7c25-54cd-356f-b5c0-08fddf0ecfc9 | -4.9489 | -56.2659 | 2026-08-20 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 227d4e09-20b8-3eed-aaf4-38b6d3fd0052 | -6.4208 | -54.938999 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a901f92-d8e8-366b-914b-a399660b9927 | -5.8031 | -55.715099 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a0b40e4-4b64-3079-a0b8-7e5ebcffad79 | -7.9621 | -44.6688 | 2026-08-20 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 784abc34-352c-3710-836e-5e7512b171a5 | -8.1541 | -54.994499 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d91d5c54-7a94-3831-92d4-41c2cec4b5bd | -19.7192 | -46.212399 | 2026-08-20 01:02:00 | METOP-C | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 68f13367-8d4d-3f55-b7c3-f42ac2226a4c | -7.4384 | -60.002998 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8ecfd77-e179-3d30-b2e9-e30da36c5c2a | -11.2137 | -55.051102 | 2026-08-20 01:02:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf7cc9f-9ba1-3590-870f-ef5360167a9a | -12.0074 | -53.438202 | 2026-08-20 01:02:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4533e4-3d67-333d-a15e-cbdd73198f0f | -6.4192 | -54.932098 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d734f31-72d2-39fa-8921-d77f94e75e10 | -6.4463 | -52.756001 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 126fb791-179e-36e5-b3d8-122fb4c74e0b | -11.187 | -54.005699 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c351fe46-a658-3f06-9c43-88465e9a3b67 | -11.2219 | -55.041698 | 2026-08-20 01:02:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c310cbfe-054f-3337-b8d0-1e9dd16b86d6 | -7.5474 | -55.594002 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6816ccd-a18b-3982-81cc-be2b93b6c3b9 | -6.425 | -52.753201 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f166ab53-d11b-382f-86ed-4a58b6daf21a | -10.5177 | -50.782799 | 2026-08-20 01:02:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe6238a1-7485-3c74-a687-de7e6632dbf5 | -12.8073 | -48.4328 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3c13d6c-8d1f-30f1-89b3-8375d921ba88 | -20.7848 | -50.195301 | 2026-08-20 01:02:00 | METOP-C | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8729913c-ecae-3056-9420-18171c1e0818 | -8.5604 | -54.648399 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbdf347d-90fe-3adb-ae75-a6859243445e | -14.5249 | -53.318401 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3593c8b1-73a8-3af0-be37-b673297340c4 | -12.8243 | -48.417801 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74d211a5-1b04-328b-8abb-cabab995aa6e | -14.45 | -45.610298 | 2026-08-20 01:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a37139d-3acb-3d10-a836-33dfbafa1ade | -13.6507 | -51.7742 | 2026-08-20 01:02:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60bba516-566c-3da9-8e7d-1264b2655ac2 | -7.3635 | -55.508701 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c9c16d3-50c8-34a6-a760-0acbf0b44181 | -8.7211 | -49.614201 | 2026-08-20 01:02:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fba9ab49-94d9-3ffe-950a-f5185ac60a4e | -8.5803 | -54.782398 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c42d15fb-ecd5-3bf5-a1eb-137e8d09ecb5 | -6.4395 | -52.726799 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35dd0919-b8d1-3000-b321-b4a2147e5486 | -10.4572 | -54.6562 | 2026-08-20 01:02:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcc58761-09b2-30ef-9c4e-eecf3af26363 | -7.378 | -55.527699 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4232ae3e-b998-39b4-9c1f-b3249a285f05 | -9.4069 | -60.430801 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d07d8e3c-2855-32da-9594-6154c9effcdf | -7.3432 | -45.801701 | 2026-08-20 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b547e5e-aa27-3261-b7dd-70306ef91266 | -11.1917 | -54.0266 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c57c3ef9-2ea9-31f2-ac8f-7b87395408cb | -15.3603 | -52.768002 | 2026-08-20 01:02:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 866a3b69-2af7-32ff-aa0c-8cd65f2c7af0 | -9.4562 | -51.628399 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e22efd88-6695-3288-bf57-07f2508e5190 | -11.9945 | -53.426601 | 2026-08-20 01:02:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c71fe020-5cba-3197-964f-174033399080 | -7.5313 | -55.567799 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a8a9fd2-9827-30f9-bf13-cd0ac9c24f5f | -2.5603 | -47.235802 | 2026-08-20 01:02:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 266d4e68-8d23-3b0a-b853-5b2f17bf7a8e | -7.5971 | -45.175098 | 2026-08-20 01:02:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| efb89525-f8cd-3c9c-872f-1320936531fe | -8.5905 | -54.736301 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 021d2e5c-f387-3008-abaa-6a6e7c5ecbc8 | -8.1754 | -54.997101 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb27ca3-8492-315f-96fb-749d5852982c | -6.4429 | -52.741402 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2338beb-5614-3760-b579-e44b833a6130 | -11.1886 | -54.012699 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 043f2962-fce1-3eec-be15-9e39c13347bb | -6.795 | -59.582699 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29dbcedd-bdce-32aa-a380-c561206f99f8 | -6.8595 | -59.032902 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1e31b8c-959d-3ef5-b241-bfbb4b407edb | -8.0911 | -51.6632 | 2026-08-20 01:02:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 892eb2cb-2ed0-36b1-9bbe-136deeb0b01f | -9.2158 | -59.764099 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 848501b7-26d4-3a7c-8e61-8e36cf7af4d4 | -6.5793 | -58.9702 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 41d38145-f53b-35e2-bbce-5b3292551b55 | -17.339899 | -43.620602 | 2026-08-20 01:02:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 115f86d1-d8ca-3bf6-8965-05f40cf081d8 | -8.6647 | -54.654099 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3f18e3-e666-3c49-9fa6-090d09b3b07f | -8.5462 | -54.768101 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1a36f2e-4134-342d-99f1-d7ace095b640 | -11.1819 | -54.028801 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 023f7105-77fa-386f-ba39-32a691d5874a | -9.4138 | -60.4156 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d389f6d-cbe0-3624-8ae9-f8fb92f8b100 | -17.995399 | -49.393902 | 2026-08-20 01:02:00 | METOP-C | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63426312-92e5-322a-95a8-181ca792ac58 | -23.071899 | -49.167099 | 2026-08-20 01:02:00 | METOP-C | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
