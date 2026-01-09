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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5db2e33-5b48-318d-9cda-437fb33fc678 | -3.5986 | -41.59097 | 2026-01-09 03:55:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d652e3b-e167-301a-80fa-02b2af221378 | -5.1028 | -39.22157 | 2026-01-09 03:55:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5d1d7a50-4ce7-3a4e-b3ee-54ef72505ebc | -4.75342 | -43.25544 | 2026-01-09 03:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c680c4f-165c-384b-b3de-83a5d2408413 | -4.53648 | -40.46999 | 2026-01-09 03:55:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b848bd99-6775-3696-8337-c9efd5700699 | -7.3128 | -35.15855 | 2026-01-09 03:55:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1153fbaa-0a2f-3789-a8fd-6be15dab48b6 | -6.62323 | -38.48399 | 2026-01-09 03:55:00 | NOAA-20 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6a2b820e-a523-3532-bff0-977bdd041b0a | -4.26559 | -43.78445 | 2026-01-09 03:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0071ba1d-7e92-350b-b3a4-4990d809a9fd | -4.39987 | -43.57559 | 2026-01-09 03:55:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71cc7cf6-f59b-36fb-bdde-b8ede67e27b5 | -9.23648 | -37.00909 | 2026-01-09 03:55:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 75cdb1ca-5292-3ddd-8487-518f1b945f01 | -6.36023 | -40.25765 | 2026-01-09 03:55:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b122de2f-b400-33c6-bf0e-ee072ab3d844 | -4.26917 | -43.78913 | 2026-01-09 03:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 25149004-0b49-324e-86b7-32ab2f87fd69 | -5.87043 | -43.58666 | 2026-01-09 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9017422-51a4-38b4-89f9-b5042a87992b | -6.40768 | -38.32207 | 2026-01-09 03:55:00 | NOAA-20 | MAJOR SALES | RIO GRANDE DO NORTE | Brasil | 2407252 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c71889a5-13d2-3936-8a3a-6cc221770d41 | -5.0676 | -40.46974 | 2026-01-09 03:55:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fc6c6d14-0077-3def-ae4d-56ccec56bb91 | -6.26822 | -37.23618 | 2026-01-09 03:55:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5e6ee56d-59b0-31f8-bd5a-2a3baf49ec08 | -6.58726 | -44.61834 | 2026-01-09 03:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a62f6c52-0404-3937-aa5d-cc34ab2fb8d9 | -6.05801 | -43.74236 | 2026-01-09 03:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c2c03e3-6a11-3832-90a0-e5c9ada864ff | -4.68027 | -43.24297 | 2026-01-09 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93f5c850-3307-3dfe-b8de-95e0e1bc9941 | -4.31917 | -39.14884 | 2026-01-09 03:55:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b535628-b06a-3731-9fa4-811bb06551ca | -6.33406 | -43.38161 | 2026-01-09 03:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a50206a5-7f07-3604-a822-ecd348a24ae0 | -5.67644 | -39.29122 | 2026-01-09 03:55:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8991f437-3015-3b61-8924-aa9d0468afaa | -5.17617 | -43.2739 | 2026-01-09 03:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fed4d5ea-4acf-3fb5-b045-d7f9c9144da1 | -3.25612 | -42.54424 | 2026-01-09 03:55:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3b386ed-e3f5-3ad6-9b1f-a2ee683b2754 | -3.57861 | -40.97566 | 2026-01-09 03:55:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9322fd8b-9e8f-3fbf-a357-efb31a1a5373 | -10.92336 | -37.51524 | 2026-01-09 03:55:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 33cc60c3-886c-3b5b-94cd-a12e534c0793 | -6.53232 | -40.32199 | 2026-01-09 03:55:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 96edf2f4-cfe1-3010-a58b-f3cbb3e4f6e9 | -7.57587 | -34.95404 | 2026-01-09 03:55:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 30cf7982-3e4f-33d2-bd67-88f6c733963d | -6.82942 | -35.0659 | 2026-01-09 03:55:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d832f83-f527-3080-986b-e54748bf94e7 | -4.26625 | -43.78047 | 2026-01-09 03:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc82466e-1f3b-3cf3-bee5-81f32964aa27 | -5.75456 | -39.79597 | 2026-01-09 03:55:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e218f3a0-0704-30dd-a8e4-fe6ee8e29d17 | -3.89757 | -38.42708 | 2026-01-09 03:55:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3204f4b-9240-39da-9a69-9d529966bfed | -7.86319 | -41.61905 | 2026-01-09 03:55:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72644e5d-ed49-3c51-9acb-49941a2517ab | -6.46412 | -39.78376 | 2026-01-09 03:55:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f82de9de-e533-356f-a68d-1ba824d0983d | -6.95026 | -35.15845 | 2026-01-09 03:55:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 700d3ba7-9d20-33a7-887e-5d6807a33985 | -3.26406 | -42.54547 | 2026-01-09 03:55:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e7c707e-7c10-3e67-a4bc-f00367cfa3c0 | -5.70332 | -39.86886 | 2026-01-09 03:55:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dd6c5731-e1d0-3ec4-afad-e70e38207fe8 | -5.14411 | -39.72903 | 2026-01-09 03:55:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c99e18c8-732f-3657-b1cb-3000a203230b | -4.38505 | -40.06524 | 2026-01-09 03:55:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8dad917b-3b05-3edf-b5f4-b231ada0e360 | -6.05037 | -39.43721 | 2026-01-09 03:55:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b56d9af0-a327-3da9-9509-8002d52d5a52 | -5.05092 | -42.94559 | 2026-01-09 03:55:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9030b2d7-0ba5-3565-95d6-6107de970ecc | -6.24164 | -39.7078 | 2026-01-09 03:55:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6feee606-c8ed-3609-81b0-f2059e63b7c9 | -5.62961 | -38.64444 | 2026-01-09 03:55:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8550404a-f268-3367-b7ef-9638fa9a647c | -13.3379 | -40.3706 | 2026-01-09 03:57:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| fb4d8bec-424f-331b-acc3-c6ac22bb82d6 | -11.82313 | -46.61295 | 2026-01-09 03:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32e9c714-129a-35e0-abb5-219c0a150fa8 | -11.20729 | -40.73347 | 2026-01-09 03:57:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c51d9ee9-2dc6-3f9d-a099-3c874a1eccd8 | -11.84236 | -45.12157 | 2026-01-09 03:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41729cd5-8adf-33fd-ba09-f70384ef2364 | -11.20395 | -40.73291 | 2026-01-09 03:57:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e23ee9e-c772-3bf5-9d1f-c1ecf3da27e2 | -18.37022 | -39.95617 | 2026-01-09 03:57:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f85f1d6-0f0d-3366-ab24-5ae10f4a6705 | -12.14128 | -37.95174 | 2026-01-09 03:57:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4d4dd7f3-a6f7-3b1a-a89c-1be485026e58 | -11.82764 | -46.61379 | 2026-01-09 03:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 605e1540-de7e-33ce-8847-511a8cce0433 | -12.46045 | -38.06148 | 2026-01-09 03:57:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c571be9-1bad-38f2-8ff4-cfd84ac4d314 | -12.21118 | -38.98312 | 2026-01-09 03:57:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2737ed45-8f12-3676-a25f-153f80f5127e | -22.0831 | -43.17733 | 2026-01-09 03:59:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 33e223c9-88b7-3e45-8241-d4cc9de415a6 | -19.00933 | -44.33109 | 2026-01-09 03:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8a40615-12c7-38d6-9b3b-b409d96ed75b | -21.99412 | -45.43037 | 2026-01-09 03:59:00 | NOAA-20 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 593b56b0-0a64-3335-9990-bc6c91d6081b | -19.46786 | -44.76499 | 2026-01-09 03:59:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d084a48a-42be-3fe1-a23e-68cbca6a4d5a | -21.22719 | -56.25866 | 2026-01-09 03:59:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ae29f37-73f4-3b18-83bb-5feb162e95d0 | -21.22884 | -56.25209 | 2026-01-09 03:59:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80a4d37b-c9cf-3043-b843-898389da70a7 | -19.29611 | -55.26323 | 2026-01-09 03:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 604747e7-f77b-34bf-856a-2de10959aab9 | -25.57183 | -49.83953 | 2026-01-09 04:01:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5374dbda-2d91-3fcc-9731-f1be4b19c75d | -25.56845 | -49.83405 | 2026-01-09 04:01:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 991e1cd7-fbd9-39a3-b128-344a32320320 | -25.56754 | -49.83848 | 2026-01-09 04:01:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e68acab6-5667-3d89-b529-8681b179a276 | -27.31927 | -51.6706 | 2026-01-09 04:01:00 | NOAA-20 | OURO | SANTA CATARINA | Brasil | 4211801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b0d826c3-eb06-3d44-aa7d-595e3b807200 | -25.57274 | -49.8351 | 2026-01-09 04:01:00 | NOAA-20 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c19688b1-6df0-3be3-a970-09279e87aca2 | 3.38583 | -60.23266 | 2026-01-09 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1358b55b-e56b-3437-b5f3-3ed9ca17f933 | -2.43041 | -45.66523 | 2026-01-09 04:44:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f1eab6c-d15e-38d8-862d-8aaa6d1c86be | -3.26546 | -42.54372 | 2026-01-09 04:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cc6a7e2b-45ff-33dd-87db-622d15412df3 | 3.38108 | -60.2429 | 2026-01-09 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcc707bf-4b55-3633-92bf-42b6b4bed32d | -0.88025 | -52.00236 | 2026-01-09 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3829497c-0a5b-39ac-afd7-de95a05a9dba | -3.35805 | -39.12822 | 2026-01-09 04:44:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5868e297-cff6-3bb6-942a-97bb87f25e5c | -1.6127 | -50.07828 | 2026-01-09 04:44:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e213a70-b1a7-3af9-8537-0417ea47ccaa | -2.87919 | -45.22583 | 2026-01-09 04:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d2b21ff-dbec-3943-a878-2fe8e07d2ab1 | 4.32297 | -59.85593 | 2026-01-09 04:44:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96c20221-0481-3270-82d3-8283ed95f997 | -2.87974 | -45.22223 | 2026-01-09 04:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e879908-02a4-318a-a408-8a820f847878 | -3.35876 | -39.12341 | 2026-01-09 04:44:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ddbce046-1b3e-3cb4-8165-a6e550f3732e | -0.0908 | -51.28108 | 2026-01-09 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5244b353-eecb-3734-a707-88e0db5dace3 | -2.47008 | -48.06028 | 2026-01-09 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a84659e4-e028-3f0e-aa5d-a6ea980e1483 | -3.26056 | -42.54292 | 2026-01-09 04:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| be13e7d0-0961-32bd-baa9-7028a335841e | -0.88083 | -51.99862 | 2026-01-09 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a8fa541-8af8-3dfb-a9d6-c6de3d103383 | -2.43432 | -45.66584 | 2026-01-09 04:44:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cbe72e2-a029-39a5-8f06-3d4c044f8b81 | -0.16644 | -50.4073 | 2026-01-09 04:44:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59bb6ca7-7a45-384d-9e91-ba19703d6c0a | 3.38038 | -60.23818 | 2026-01-09 04:44:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95ad556b-7866-3483-8482-9e9f8cf0cb70 | -7.50595 | -45.54935 | 2026-01-09 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c374b36f-9ddc-3340-aab6-17936f82cf8f | -4.68516 | -43.24437 | 2026-01-09 04:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 504788bf-f0f5-37cb-8089-1fb64b80be72 | -7.72739 | -45.63233 | 2026-01-09 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57e81c39-abae-317d-a252-9a99e03c5139 | -3.42444 | -42.4716 | 2026-01-09 04:46:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a560a69c-b735-306c-853a-bfb775a11c61 | -4.68038 | -43.24367 | 2026-01-09 04:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a06cf447-d3fa-38ba-95c0-71694d32af55 | -7.50112 | -45.55268 | 2026-01-09 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46feb886-e50b-3b25-9360-570a77093638 | -3.85681 | -42.25494 | 2026-01-09 04:46:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0090ee06-64d6-36c9-94b5-fb533a2b07e3 | -7.50055 | -45.55659 | 2026-01-09 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94c6b300-84ff-3870-a6f0-ea5b58745639 | -4.40781 | -43.469 | 2026-01-09 04:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6948e403-f3d6-3463-8254-88381249879c | -7.72711 | -45.63166 | 2026-01-09 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c9b2707-bef9-340c-93e9-ffd463834c30 | -4.28235 | -38.71879 | 2026-01-09 04:46:00 | NOAA-21 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cfab9dae-00c0-3455-b7c0-36a637074e3b | -9.0467 | -46.98568 | 2026-01-09 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f81afa26-69ab-3b03-aba8-fff501cffea4 | -3.50609 | -54.67773 | 2026-01-09 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f5f369d-4fea-3a5a-a032-cc8b54e2e7c0 | -3.17397 | -52.67939 | 2026-01-09 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81eb555c-df51-3ee6-84ee-44a10f87b754 | -5.90319 | -42.54961 | 2026-01-09 04:46:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 06392441-a643-3a09-9b8d-d84704ab2cbe | -7.4963 | -45.55599 | 2026-01-09 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ac7703-2e0f-330a-96e6-ed095beb6389 | -9.04787 | -46.98439 | 2026-01-09 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3176431e-f60f-369c-81ee-7d9464c0f29b | -7.50169 | -45.54876 | 2026-01-09 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README5.md)
