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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 259e9fdd-5bdb-3935-9ad1-68bcbe390e3e | -12.31485 | -43.84608 | 2025-10-25 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6a4f5d4-a231-3630-b64f-fbb8c8486384 | -10.91076 | -50.17116 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 266673b3-9012-3de7-96a7-e0ddc3417033 | -6.9207 | -45.16013 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be504269-0585-3317-a3b7-c87d6a16876c | -5.65242 | -49.06899 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d4a5f25-a1d0-3ede-80fb-2cc449820188 | -8.55047 | -50.04558 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3765fb8d-414c-3935-9bae-9a867db81f45 | -10.00077 | -47.60251 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 205d526e-cf34-38ea-a869-1eca4735f92f | -9.30692 | -45.17537 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89769acb-a2d3-36a2-bfa6-76e2918a3bf2 | -13.12773 | -48.2415 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 183ef391-4384-3d5c-ad08-b21bab35b212 | -12.05663 | -46.41105 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16221f6f-440e-36d1-860d-204c2d53e30c | -12.08973 | -46.41675 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9e0d9e6-8281-3738-b396-7546895a7499 | -6.41728 | -46.18293 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2acb975-f560-338e-8eff-665fd5b8184f | -7.78523 | -48.39201 | 2025-10-25 04:19:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33ff923d-6aba-31dc-a1db-934299b2b4c2 | -10.25112 | -47.99805 | 2025-10-25 04:19:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c56014b-27ba-3ce8-bbf1-78be717b80c9 | -10.65843 | -48.07953 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69793447-2c03-3d72-bd62-68b1726e1ec3 | -8.60224 | -44.8173 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 282d33c6-ceb1-3136-a985-410d6f1cc01f | -10.70949 | -44.74264 | 2025-10-25 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcc6ea4e-a08d-34b5-b4a7-e0fe02d428fc | -6.91904 | -45.17059 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83e6793d-bbee-38ff-a3d5-559d1f984a20 | 1.64425 | -55.73497 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f92066ed-df5c-3edb-9406-c3aed95ed0ba | -12.11722 | -46.71261 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55e72d77-f8bb-3dd4-8dd1-36cf3d712e01 | -12.5361 | -49.60743 | 2025-10-25 04:19:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4822b828-983b-3cb0-850f-094f4e3da167 | -6.80355 | -45.42682 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faac5d23-880b-3a9c-96a4-f4f05a0c13ac | -10.80031 | -49.65121 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99f67195-42f8-3d74-9396-28a75af4678a | -10.62503 | -52.18919 | 2025-10-25 04:19:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e3adc5b0-e490-35ee-99a5-5f1ab4bbc026 | -12.12055 | -46.71316 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f15377b-3789-389f-906f-a5344dd79803 | -6.24605 | -46.39743 | 2025-10-25 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c5c033ce-682e-383d-ab6e-dab2ad567c5b | -13.54164 | -47.56683 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77e898b0-1abf-3b02-ab57-5cb9681639e1 | -13.00735 | -48.54488 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92e96fb4-0f11-33c5-a7c3-75219468e593 | -8.19031 | -47.87345 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffed3c04-d274-33b2-924d-ee3303848fa3 | -11.98902 | -43.31434 | 2025-10-25 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6924140-9826-33b8-b9b7-7c53fa137c53 | -7.58266 | -43.58252 | 2025-10-25 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccd02977-8689-33cd-8e18-a106871c5948 | -7.64 | -42.16783 | 2025-10-25 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 318507bd-c568-3bbc-a27e-fe1b5530e5ce | -13.22733 | -47.74607 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93b21d83-3ee3-3b78-8d56-bd93cc1c0435 | -9.28671 | -57.55236 | 2025-10-25 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dad69e75-493d-3a92-935f-9365b5073a16 | -10.64188 | -45.23957 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec8c2fb0-9967-3b58-9936-61e942d0499d | -9.49182 | -47.4535 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 257a0679-921e-3911-bdaf-31b48b3da899 | -11.52766 | -47.10237 | 2025-10-25 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6787aa80-c719-3080-b980-93ac29c92485 | -13.0363 | -47.39388 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4697894-18b0-39d9-8610-445441cf95d6 | -12.2946 | -47.46168 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 565080fc-e9dd-3875-b7e3-5caa2b22eef7 | -13.94124 | -43.81845 | 2025-10-25 04:19:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c476b6c2-f6f4-3aec-82a3-e7aefa21eb79 | -12.46888 | -44.53671 | 2025-10-25 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 422fa829-0a7d-3a28-9a52-9a678f024991 | -12.76569 | -46.03254 | 2025-10-25 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 54c9b9b0-48df-3995-bcc1-dfb2855e96a1 | -7.79061 | -45.3954 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7da6c5d6-8e7b-3635-b67f-412b6f789b35 | -7.85212 | -46.42666 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b17d3af7-b6cc-3d55-aa12-618b82733e0a | -7.01122 | -46.72019 | 2025-10-25 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6201b964-2ead-3583-89ff-9190ae75e91e | -8.83288 | -44.21274 | 2025-10-25 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1927ef91-2db4-331c-8cd5-4291b3f202fc | -6.60436 | -48.76715 | 2025-10-25 04:19:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e0687b2-561c-39ac-97f7-20c589a46b20 | -10.95784 | -50.2955 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aaedd45-c3d1-3d6c-a993-86cdc143c7df | -7.58068 | -45.34792 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12381732-61b6-301a-bf23-79f8ad5347fd | -11.76581 | -44.23263 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f47651b9-67c0-3aa8-adf1-e714b8c1ddce | -5.57285 | -49.97932 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17c6ec63-f925-3559-b76c-98d9c0112a16 | -9.49527 | -47.45407 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e357c977-b9d1-31be-b6b5-7e43131e6ff5 | -10.64298 | -45.23257 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38d50496-32db-36ed-b575-bd8ba5b83a6a | -7.47936 | -46.88309 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5de417c-957d-362a-90b3-7ee0e699b6e6 | -6.92291 | -45.16764 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b58fdf1e-32e3-3802-950d-d5417afb8310 | -6.1624 | -47.08732 | 2025-10-25 04:19:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e29a0f8-532e-3cec-bcd7-8f7121675e3b | -12.6385 | -44.30217 | 2025-10-25 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e234eb6d-bd90-31b2-99d5-f811909467ce | -9.70181 | -45.38554 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ae4603c-99c5-38e6-b9d2-5eec3164caba | -13.94182 | -43.81449 | 2025-10-25 04:19:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d47faa52-3429-31b2-9c88-612523c63111 | -5.70527 | -49.30838 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 759a9017-4e94-3e0d-a7b3-2ba696b1b372 | -10.9452 | -50.29845 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b38952d3-b6ed-32a1-bbec-7876a87c0546 | -7.35915 | -46.99593 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5de185f9-c204-309c-b190-545ca81d5bd0 | -7.55683 | -47.11762 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18cf2f38-9e5b-37b8-98ee-d9709fda86e4 | -6.56008 | -48.04837 | 2025-10-25 04:19:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1ebeefb-0635-374e-a9ec-e6bd0a46c779 | -9.30086 | -45.17083 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5eaf8fba-a9bf-30a0-8022-50e667005f33 | -10.68707 | -48.08029 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aa3ee4a-a2ed-3807-9d86-d3a6af749054 | -12.0727 | -46.39556 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af005fbb-c301-3489-a55a-29f257106e98 | -11.32572 | -53.93187 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6fa502-690e-3afa-a4ee-1f05611acfa2 | -13.07331 | -47.56942 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eca67dd-d1fc-3c85-b635-fb054fbca549 | -7.25643 | -46.33161 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 175f3ad7-c7ee-389b-a328-82d17f78c907 | -10.64716 | -48.06086 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f32edf8-b3b7-3706-8ecf-fe06f7f43d31 | -8.71666 | -49.60284 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 76ee336d-06d9-3739-983c-d58bb8d4908d | -13.06092 | -50.29149 | 2025-10-25 04:19:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 333917e1-0dfb-3be3-838e-31607e7bedb6 | -8.5029 | -44.08474 | 2025-10-25 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f4740fd-a2fb-37a8-85ef-727abb613814 | -9.32406 | -46.97575 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8667cbc8-ddc8-34af-9da8-fb72e5d74286 | -7.633 | -41.85478 | 2025-10-25 04:19:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f247d812-3621-355f-a650-dd27fd80113e | -12.05501 | -46.39987 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed8113ad-4ccd-3274-9c8c-e851afbb81e6 | -13.68289 | -43.4873 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 167f5eaa-536b-394a-a68c-71404f255301 | -6.64859 | -43.6087 | 2025-10-25 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| deb0e000-c5dc-315f-a5f8-fc9e2f2bc325 | -13.33156 | -47.94323 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff124cf6-5f70-3b18-9835-d3315dea33db | -7.64393 | -46.88631 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de86f6e8-ba45-31c0-a8a4-b858bd2c9533 | -12.11665 | -46.71617 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ce83fc7-91f1-3394-8b5f-697f012f7f10 | -9.57314 | -49.67863 | 2025-10-25 04:19:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9e20d84-f594-30f3-a0f6-2684b5d46802 | -1.30227 | -49.35025 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d81b788-210f-31e4-a3dc-3c8e175895a3 | -11.95944 | -47.64333 | 2025-10-25 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 190cddc2-cd42-3c72-9768-028b37d2aa63 | -9.49465 | -47.45788 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52921a07-5622-3b5e-8928-800ce088da47 | -12.06551 | -46.39797 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2e7d6466-377a-3bc2-b19c-000ccaf80936 | -9.28884 | -57.54142 | 2025-10-25 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d944aa7f-e86d-3b9d-8be7-a0bca2cbbab2 | -13.35946 | -47.4136 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ee03527-9dc6-3538-bb8a-61a5a5ea39e5 | 1.63837 | -55.74235 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c41cc31a-6baa-320e-9f06-7bef91f220b4 | -9.4574 | -47.72964 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f71b37d-8e77-3968-b622-eeef6f875414 | -10.92517 | -50.11418 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9233376-d819-33e7-a831-468d4c80f5b2 | -12.08645 | -46.41599 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8884ee9e-ec9a-327c-8e7c-9fb21c385d9c | -6.75828 | -44.20844 | 2025-10-25 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dbea631b-3338-3b23-a918-fcfc7487f558 | -12.21477 | -46.50571 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91c9a56d-af08-325c-a029-d39458b5cd2f | -13.41151 | -47.94933 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d015a596-6dfe-3c59-9514-fd5dc153b4e0 | -8.60939 | -44.81488 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4769d454-4e02-3dd9-83c5-bba8353de516 | -6.81607 | -45.43268 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77844413-bf28-3488-8c28-66ac04b20c3e | -10.55723 | -49.77466 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1ca6735-0d33-31e5-8197-ddffe84f5fa2 | -10.64133 | -45.24307 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 524585e2-09ba-3096-9384-279ecb6dd65b | -12.24457 | -47.44234 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
