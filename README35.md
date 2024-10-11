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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78579a86-4431-3069-b36a-8be229029578 | -9.34472 | -35.96722 | 2024-10-11 04:00:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 72d38c13-5885-36c4-b76f-42ec51502db2 | -8.31758 | -35.12063 | 2024-10-11 04:00:00 | NPP-375D | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 466cd762-122f-3150-a4a8-4b81555c2118 | -9.714 | -35.89886 | 2024-10-11 04:00:00 | NPP-375D | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cef248b-222c-3cb3-9af4-6653d9b0d612 | -9.56471 | -35.9622 | 2024-10-11 04:00:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 51856945-2dd0-3930-b5c7-41f90d0f64ba | -9.56079 | -35.9616 | 2024-10-11 04:00:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e4263b9c-d915-3174-bbd4-f0d124204adf | -5.80029 | -43.00423 | 2024-10-11 04:00:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4746d93-5e35-393b-aab6-77bcfe96e396 | -5.78242 | -43.11182 | 2024-10-11 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52483072-5313-3c9d-afa5-20f70eae8d5f | -5.75414 | -43.18037 | 2024-10-11 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 68148f1f-5163-350d-a938-a159cb02df96 | -5.45811 | -42.39741 | 2024-10-11 04:00:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5cb6f609-06fe-382a-851a-bfa59481d95e | -5.45455 | -42.39682 | 2024-10-11 04:00:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c1208b4d-71b8-349a-9486-902ae2a0ffe9 | -5.40301 | -42.92392 | 2024-10-11 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b4b5148-5aac-32e4-a4bf-56b2d777f9a8 | -5.39934 | -42.92332 | 2024-10-11 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1e5a953-9fa0-3ec6-8bb7-906421ef741d | -5.35205 | -42.9436 | 2024-10-11 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20b9b7f6-3ee2-3bf8-bf1a-9a4c7caabcbd | -5.34839 | -42.94294 | 2024-10-11 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aebb69bc-7b92-37e9-9619-75fcab4d169d | -6.18839 | -43.43577 | 2024-10-11 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c02f1467-1856-3106-bab2-f7c0649742e4 | -5.99421 | -43.44019 | 2024-10-11 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fa34718-7417-392d-9cf4-50f89c589820 | -5.82368 | -43.22986 | 2024-10-11 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47d88716-74f6-39ad-a679-37593276faa0 | -5.81997 | -43.22926 | 2024-10-11 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21a26591-1cf3-3939-8a6e-b1ab1526fcd4 | -7.67967 | -42.49105 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 180a1948-4345-35be-98ba-01127bffcc98 | -7.6768 | -42.48657 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b35294bb-0692-3ffb-8698-704ee1984ab9 | -7.67426 | -42.50222 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 77cf43e2-9aad-3673-afac-e7fa3dc29d33 | -7.6733 | -42.48599 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d55e527d-c7f9-3628-8447-048cd4ce1b8a | -7.15336 | -43.4266 | 2024-10-11 04:00:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef4b5020-f944-32c1-9cea-0dcdac790ccd | -9.26279 | -43.53846 | 2024-10-11 04:00:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 034038f5-b6aa-3e6b-be6a-55d5954d2b7a | -9.25918 | -43.53783 | 2024-10-11 04:00:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6b9fc1e6-2c99-3bbd-b3d4-3036d22949e7 | -6.2832 | -35.05429 | 2024-10-11 04:00:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 30bcf53b-46da-3c7d-9816-6ea4b5c9da4b | -6.28097 | -35.05224 | 2024-10-11 04:00:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3fc83859-0425-3471-878f-cfaf89593063 | -7.50224 | -34.86005 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 948dbd9e-8374-362f-8dc2-56eaa867950b | -7.50173 | -34.86364 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29f6e81e-73e7-32bb-9779-4d2f075436b3 | -7.49815 | -34.85947 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1d6ef9b-5e61-3610-8fa0-bc201eebd4d8 | -7.4957 | -34.85609 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec0b3fd5-097c-3ebc-baae-e5c4b30bffb8 | -7.49517 | -34.85966 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| a4dce5ca-f78c-3b3b-98ed-3613cea93ed1 | -7.49457 | -34.85529 | 2024-10-11 04:00:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8c934231-f285-3eac-a0de-aac82883d5dc | -9.25847 | -43.54215 | 2024-10-11 04:00:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bd093a36-bd66-3a44-a025-aaf8c0972818 | -7.49406 | -34.85887 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8ec7be81-c538-360d-8b66-65f4d3536a9b | -7.49161 | -34.8555 | 2024-10-11 04:00:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c5cc1c6-dce1-3e60-ae95-5824c8b51de4 | -7.49109 | -34.85905 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| c3450481-c645-35d8-bf4d-56c81d9c0ce7 | -7.49056 | -34.86259 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 73d07f08-e598-30de-895b-0ad2ea8b0d26 | -7.49048 | -34.85472 | 2024-10-11 04:00:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e13ab73-c4e9-38df-8663-343f2a31def8 | -7.487 | -34.85845 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 72fc86c9-bfbc-3035-865e-c9dafe68d9cd | -7.48648 | -34.86198 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 15472d94-5666-3f9f-b361-c85ed7156b8d | -7.46073 | -34.97935 | 2024-10-11 04:00:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a0386b10-abbd-3b3f-aad2-4ee507d07278 | -7.18907 | -34.79652 | 2024-10-11 04:00:00 | NPP-375D | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2d4e4d78-c5d4-3aba-944e-0529abcf50ce | -7.13051 | -35.13528 | 2024-10-11 04:00:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e4e48c29-28be-3f77-b2a5-c3276abd733e | -7.12885 | -35.13134 | 2024-10-11 04:00:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 87a0e385-21d9-30ec-b831-8011e9897c6a | -7.12652 | -35.13467 | 2024-10-11 04:00:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8d6f224c-4fce-3bc0-8364-24480e311983 | -8.31696 | -35.12088 | 2024-10-11 04:00:00 | NPP-375D | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 111acafd-7420-35cb-b4dd-4706d5414d94 | -10.23302 | -36.36 | 2024-10-11 04:00:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2ef6bde0-afb4-31cd-a870-aafdfabc473c | -10.22917 | -36.35942 | 2024-10-11 04:00:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8123be11-6faf-3e28-85a2-c550059501c5 | -5.46088 | -36.71447 | 2024-10-11 04:00:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ea7e7db-5767-3d11-9263-7e389b119338 | -5.11499 | -37.41702 | 2024-10-11 04:00:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd7295fc-522c-343f-965c-9050416bf56b | -5.25646 | -37.62881 | 2024-10-11 04:00:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 11d61b98-b045-313e-89da-a2cb6fc92bb4 | -5.25154 | -37.50641 | 2024-10-11 04:00:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c1927135-6b7e-3232-88f0-5010c31c3d48 | -6.83762 | -38.57698 | 2024-10-11 04:00:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41f719bd-3c15-3084-8f58-d823581374d2 | -6.4493 | -38.82365 | 2024-10-11 04:00:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| feb057de-919e-3433-9e9e-7a0fb3abc245 | -6.44875 | -38.8272 | 2024-10-11 04:00:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ff96db3-d874-310d-9c2d-1593f1b8f577 | -6.44595 | -38.82313 | 2024-10-11 04:00:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67991ebb-1bf3-3133-a5ce-ab44c6a6bb2d | -6.4454 | -38.82667 | 2024-10-11 04:00:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a02722fc-aead-3fe9-9f65-53a2b7402640 | -6.4426 | -38.82261 | 2024-10-11 04:00:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e177bc81-456a-36d4-869a-d303291f2c86 | -8.68938 | -38.23733 | 2024-10-11 04:00:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d5a9932-bf33-3eed-b4da-64ef7f0a9cee | -6.81632 | -40.08128 | 2024-10-11 04:00:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 33d17a40-eea9-360b-95b2-9e3aa63fe0cc | -9.12236 | -40.30434 | 2024-10-11 04:00:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dfb9ccef-4749-333f-afe1-facddfec9418 | -9.11904 | -40.30381 | 2024-10-11 04:00:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 439f59bd-57bd-3039-83e9-3cdce5f58b75 | -8.61745 | -40.52433 | 2024-10-11 04:00:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 71fdf98f-d821-35e3-8a52-51649981948d | -8.61412 | -40.5238 | 2024-10-11 04:00:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1f71990-1677-3378-a592-fb23c5be04f8 | -8.58727 | -39.48775 | 2024-10-11 04:00:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0872c44e-2f94-38c8-a8c3-379f9ef2565d | -8.55352 | -40.48211 | 2024-10-11 04:00:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 70c68f4e-d129-3523-95b3-9e10d94b1b52 | -8.53056 | -40.26052 | 2024-10-11 04:00:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 531b098c-8f0f-31fd-aca4-fa829eafe6f0 | -8.42715 | -40.82745 | 2024-10-11 04:00:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8d9edc8-15bb-3e39-bd86-d0312cd78a00 | -8.41255 | -40.23468 | 2024-10-11 04:00:00 | NPP-375D | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e33173f1-cbd6-32e1-915a-a852c9e01095 | -8.37413 | -40.58588 | 2024-10-11 04:00:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e3691d8a-388f-3fbe-98e2-a02bb5e8fccc | -6.37194 | -40.4749 | 2024-10-11 04:00:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ade2cc9d-51e1-3d01-af29-b9821190f348 | -6.31243 | -41.76717 | 2024-10-11 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64336a6c-36a8-3611-bf58-139c70568c8d | -6.30268 | -41.76183 | 2024-10-11 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 74e0716f-0eaf-3457-8085-acdc221d7264 | -6.29923 | -41.76131 | 2024-10-11 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4c802c96-e250-3cef-8a6f-68e784c9c66b | -6.29519 | -41.76451 | 2024-10-11 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 62f7e46c-e0cd-3b96-9015-7909be7a0bd0 | -5.69043 | -40.98391 | 2024-10-11 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be9f596d-87c8-3f31-98ec-65aa479ca332 | -5.69023 | -40.98063 | 2024-10-11 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 49aa800f-c006-36b4-81df-3814ed5aad65 | -5.68966 | -40.98423 | 2024-10-11 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2556e613-e85d-3546-9485-bb2dc0396fab | -5.39721 | -41.24372 | 2024-10-11 04:00:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d377fdc9-b5d7-3cc1-b41c-8eff6e22fefd | -5.3938 | -41.24318 | 2024-10-11 04:00:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7573d211-4d5f-32b0-8a5a-d7a1f7593fa0 | -5.20162 | -41.28888 | 2024-10-11 04:00:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 695eaf6c-d105-35a3-b110-08b5f6469dfc | -5.20045 | -41.2963 | 2024-10-11 04:00:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ddca196-f5b6-3d92-acb5-5f6671af4899 | -8.00162 | -40.95054 | 2024-10-11 04:00:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b6185111-2b5e-3e88-8a45-8c95eb633566 | -8.00106 | -40.95407 | 2024-10-11 04:00:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7aeb6585-4331-30cc-bcce-3b4a3539cf14 | -8.00067 | -40.84931 | 2024-10-11 04:00:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8c322dba-27da-3bba-9791-32ef03812f74 | -7.9949 | -40.97118 | 2024-10-11 04:00:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 55f96238-d6e4-353a-8eee-3c5b9eb2e308 | -7.46754 | -41.24806 | 2024-10-11 04:00:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a23d5ac7-841b-3028-9f43-8499bb9f25d3 | -8.85556 | -41.43677 | 2024-10-11 04:00:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d558863e-1c2e-30a5-aadb-5cfc61484e84 | -8.43753 | -41.2564 | 2024-10-11 04:00:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a5e243c-ce2f-3860-89e6-45a67c7f04a3 | -8.14697 | -41.10409 | 2024-10-11 04:00:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 73e18069-087f-3e34-bbaf-e7bcc0c0aad7 | -8.14362 | -41.10354 | 2024-10-11 04:00:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 604c9a89-9bf5-3bc7-88a8-fda216a67f32 | -8.14025 | -42.32259 | 2024-10-11 04:00:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| efdc5cb3-d8ba-3f9d-bb25-51fc4fe40a12 | -9.74083 | -41.97176 | 2024-10-11 04:00:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0aebe77c-a62b-31f5-8ad8-0cb43a4d5eb5 | -10.19606 | -42.44253 | 2024-10-11 04:00:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72ea7f3d-83b3-3089-89e6-bd564989c486 | -10.1858 | -42.44082 | 2024-10-11 04:00:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8a05ddfe-435e-313d-9ca8-d70dd9a8df71 | -10.17775 | -42.44715 | 2024-10-11 04:00:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7b0b3b5-8222-37a0-915a-837ef62aee42 | -9.25627 | -43.53299 | 2024-10-11 04:00:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d211426-0b70-396b-8dd4-675fea741b39 | -9.25557 | -43.53724 | 2024-10-11 04:00:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0c2c1e99-00f2-30ce-b0ef-6cd0fc3ed9c5 | -9.25266 | -43.53239 | 2024-10-11 04:00:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
