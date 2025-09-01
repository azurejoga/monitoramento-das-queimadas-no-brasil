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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5e04482-8317-34d1-9f58-c4852c9df663 | -13.37601 | -46.95002 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d9a0d3e-5337-3e45-a661-ac31624e4b76 | -15.72458 | -48.99333 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a900cf44-7ce9-37ae-be3d-d2ec53ff0471 | -12.6019 | -48.21311 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc442337-e2eb-3d1c-866d-7b7314cc6929 | -11.37014 | -43.58034 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a506e9be-d923-36ee-847b-339bf80aaeec | -11.3317 | -43.68596 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 513112b6-7e74-3c63-a389-c26b4a2f2572 | -15.72513 | -48.9897 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ed3286f7-9c80-37c5-bb73-c2218121da76 | -17.23687 | -46.91714 | 2025-09-01 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ecc9e09-268e-319d-8e68-0fdf42e9674a | -11.41857 | -46.90426 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ab5592a-5354-339e-a38d-73479578a2f3 | -14.82104 | -46.73513 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a137edb-4a1f-3ba7-9122-a1f865fcc03d | -14.788 | -46.72364 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5250837-9918-31e7-820f-c79d1fd49822 | -12.62538 | -57.0057 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7155deb6-630d-3963-85c4-6942e13509b6 | -15.60013 | -48.33798 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29e20437-cde5-308b-bf43-1172b4a6b4d4 | -11.0299 | -46.86296 | 2025-09-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2741108-42e3-305e-8e29-b2dda7d655bb | -15.68946 | -48.95394 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18385023-1c8a-316e-9a1f-3fd3c8876e7b | -14.75258 | -46.7654 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 84a23836-dcd8-3474-9408-0d7e1116e3fe | -14.4636 | -53.05414 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 194d38b8-09b8-351f-ab5d-221b7fb54e4c | -8.71405 | -62.42012 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14a197ed-2a1e-3873-8532-ec3fab6f2e38 | -14.79034 | -46.73275 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 46819fb5-7b60-3dab-a8f8-fb7e57ed999f | -15.69556 | -48.91378 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20e2af83-9d94-323d-a9f7-dcc3bfde765d | -18.12134 | -44.99162 | 2025-09-01 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b01e222f-3264-3a4b-97d6-bc1d15d26fb9 | -11.894 | -46.69202 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91069925-0410-3fcb-8f83-2ace08c36b7e | -14.64322 | -43.95803 | 2025-09-01 04:34:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b465c742-40f8-3f3c-9487-2f0ad9b5ffb4 | -15.69501 | -48.91742 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4ba42ba-ddef-386c-86f8-fbe7ba2a15e6 | -12.63183 | -48.18804 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8caf855-af66-3162-9141-7912459fe120 | -12.8008 | -48.08519 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e3941fb-d11e-397b-8e5b-0a23ca92dd3d | -14.22535 | -51.64916 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55bd97de-c138-3be9-a0b1-0d12f4305c03 | -14.75618 | -46.7659 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08aafcfd-1a59-302c-b012-c57134675379 | -11.37889 | -43.63923 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1feee7cc-a910-35e8-9dae-03675017e989 | -11.04594 | -46.96629 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0269394d-418f-32e4-97d0-d6be94918b93 | -11.42778 | -46.91349 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea392ef8-3beb-339c-a0fa-31a449351f7e | -10.7213 | -49.57256 | 2025-09-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a52a0a72-fd3c-3876-9779-d85b95d513d0 | -13.69625 | -46.90665 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93b830ee-762f-3e2c-a616-087e0ef5d3be | -13.37033 | -46.31656 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8466612e-f4c6-3277-aed8-23e4f6145d7f | -12.87365 | -48.09254 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc90fbb2-7912-3a0a-91bd-ac8045adb068 | -14.81155 | -46.7244 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49da5ea0-c0eb-36f8-8b70-15b677945023 | -14.56053 | -52.99516 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95a86928-4317-3743-b01e-24b0c03a25fb | -8.71976 | -62.42867 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32179071-4e6c-3ee5-a223-779b367cb866 | -15.08384 | -48.11891 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbd0d44a-0490-39f6-8880-515c0abdf09d | -16.50836 | -55.02992 | 2025-09-01 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf4efb30-ec83-344b-a133-945f2d1de9d5 | -11.03166 | -47.06025 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a5f861c-a611-3972-8d83-18c618556f22 | -13.68668 | -46.87299 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f154ca60-d819-3049-a05b-382a208ffd36 | -15.70111 | -48.89984 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bb5379c5-bba5-33f4-9d12-bda8699cb8d0 | -15.6007 | -48.33422 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4f9b0135-4c96-3ed0-996b-5245d63cc72d | -12.79744 | -48.08462 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8631d395-0a40-321f-9635-956577f25008 | -12.57461 | -44.80682 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d111e2e0-131c-3462-9107-ac7e6cf0864e | -13.47477 | -46.94088 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49325979-d43d-3d61-8350-dca5e124842b | -15.29315 | -52.79197 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1272b72-8662-3244-b614-8c328b3707b3 | -11.02358 | -46.85814 | 2025-09-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e87bfde0-af0b-3928-ba4b-fedb8d14a72d | -11.37171 | -43.56888 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7ec7290-652c-3fe3-9566-325f3224a72d | -15.58769 | -48.32828 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d6a8116-0e6e-3d3d-bb75-2e4dc6d2c046 | -13.16231 | -45.28252 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 68ed5a41-27b3-3f60-9dd5-b3928b65cd66 | -12.77899 | -48.09281 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4791737a-c204-3e36-a153-2f1381f65475 | -14.75439 | -46.75295 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5125b95f-ecbd-33a4-916b-7a7583b81c8c | -15.31384 | -46.07958 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be42664a-97a6-3886-bc59-12aed9653431 | -10.92799 | -50.8527 | 2025-09-01 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b97a768-83d2-3b77-8d31-4514d0b2a61d | -14.74427 | -46.77227 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63bb4369-d9a0-390a-92d8-90cc808de72f | -14.74194 | -46.73766 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b306fb91-2660-377d-994e-cc302d36ca53 | -10.67531 | -51.56735 | 2025-09-01 04:34:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7e90d74-9256-3e25-b7c9-5827334689df | -8.6301 | -62.59726 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 348b1fb3-5523-3018-971d-9c242d1902f3 | -12.09564 | -44.71903 | 2025-09-01 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 641f8c4d-4e39-3d40-8d07-dfab8d89e7ce | -11.52412 | -54.45845 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c88e7ccd-219d-33bb-a5bd-afff8810554c | -13.97731 | -44.55038 | 2025-09-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5cfecdf-31c1-3063-8eb0-e31aeb27ea3c | -18.11108 | -45.00589 | 2025-09-01 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b175e234-2c73-3aa9-8927-cf489844742d | -11.35418 | -43.52825 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3ed862a-4f5a-36e3-93cb-86537863e08b | -14.02612 | -43.90734 | 2025-09-01 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4264cac0-235f-372b-ba15-9319b4588dfb | -15.22933 | -53.78841 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65672f3d-2612-348f-b64b-9b5849b95753 | -13.33293 | -46.99243 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ab626d29-a77c-33b7-8b14-7405d1fefd5e | -17.16728 | -46.0863 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6418cd7e-bd03-38e5-8908-1b2d7d3186fd | -11.8777 | -46.70576 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c362085-d651-30c1-9b51-b4906989e6ca | -12.78289 | -47.64845 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4fe4591-c4bc-3a1e-b950-9817ab54199b | -14.74551 | -46.73833 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49a2cc32-2a09-38f3-8b6b-0f2de823214b | -15.72236 | -49.00785 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03211aaa-188f-3648-9852-c283f6134f3f | -14.74365 | -46.75118 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39d9f601-d412-32eb-b9b6-fb72f324217b | -12.95156 | -48.10106 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8aba126-eb5f-398f-aeee-3d6490c3e621 | -11.37066 | -43.57651 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf08fc10-ffe4-32e9-8ffd-1621c72749e1 | -12.86545 | -48.16914 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e786c7c6-2205-3c87-9ce4-09082fda3a08 | -11.37532 | -43.57328 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c76a682a-9234-3e3a-a83c-9dab87bd6df5 | -13.29332 | -46.89692 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec9f36dd-5fab-3c0d-ad9d-1e4eef22fbfd | -11.01736 | -46.94627 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 626d22d6-11c2-3021-bcc3-21ad38fd2742 | -13.37094 | -46.31229 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86f67249-625f-344c-a84f-0df226cf4980 | -8.75732 | -61.43403 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 40db6012-57ce-3b86-a557-dc3b4eaf97cb | -15.15835 | -52.34606 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff163a76-d13d-3256-a54c-a7e1a9ccbe2c | -15.70172 | -48.96345 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b0ce9a3-7fd8-3024-8425-02f35452184a | -12.85067 | -48.07433 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71aa7428-8a81-3d82-9ea1-650728983670 | -14.2258 | -48.05599 | 2025-09-01 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6da0b79e-e301-3775-974f-fcb953c2c34a | -13.68304 | -46.92157 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0db4d1e3-001f-3075-a3c7-845a58580db3 | -11.80395 | -46.41999 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 776faba7-e665-3585-8730-eb4ea059efc6 | -13.33938 | -46.97326 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6767ad8a-1f67-30be-8e10-400e480f2743 | -11.80454 | -46.41607 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 53aef3a6-556f-317d-bd26-29807a533a71 | -15.6917 | -48.96173 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 548b75c1-e2fb-32e9-ab9e-7a8e39ddddab | -13.17021 | -45.27661 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5fba4203-4e6f-31f5-8895-60b6f05909b7 | -12.0205 | -49.71267 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef33cc32-25d9-37d0-981f-02fe524ab3d3 | -15.71559 | -48.89494 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 596d5f41-aa30-366c-af4d-6d70c7e14f30 | -10.8423 | -47.27087 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ca648ac-f4df-3460-99a6-25dd55827fd6 | -10.76803 | -48.82883 | 2025-09-01 04:34:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 167857b5-13c7-361a-9838-aa5d9508dfd7 | -11.48531 | -46.81247 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2ab66f2-cd89-3282-96f3-ff317c037c81 | -15.73764 | -49.95878 | 2025-09-01 04:34:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 97d39059-14ef-3e7b-8e17-24e21dc49499 | -11.92643 | -50.62913 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdffc43d-e8f8-3179-b200-81765ff912f2 | -15.71623 | -49.00308 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 50694604-f84b-3373-9fea-e1103d7e4bfc | -15.70723 | -48.90474 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README69.md)
