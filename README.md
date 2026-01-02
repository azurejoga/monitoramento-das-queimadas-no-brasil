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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f152cb9-d3cf-3908-b581-f4640c7d708e | -14.4967 | -52.5526 | 2026-01-02 00:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a957bd7f-4e1d-3c3a-8229-b3a845ad3927 | -7.7821 | -35.1367 | 2026-01-02 00:20:00 | GOES-19 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 95.8 |
| 0d9c9736-2e09-3366-9fdc-3d95c659eff4 | -3.5214 | -43.614201 | 2026-01-02 00:25:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7278882d-3889-35f3-9ead-5e79fc6455b8 | -8.7191 | -38.639301 | 2026-01-02 00:25:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 28d05ffc-604d-33d0-a55d-8771f2707ddf | -4.7247 | -42.037701 | 2026-01-02 00:25:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 97ec6bfd-6634-324a-9bb7-b0a2bc99c4eb | -18.490499 | -39.8652 | 2026-01-02 00:25:00 | METOP-C | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5aa44a34-f547-319d-a69c-d8337d719463 | -5.2936 | -35.752102 | 2026-01-02 00:25:00 | METOP-C | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 85fa82b1-d810-3f00-b05b-962b1edb546b | -7.801 | -35.131199 | 2026-01-02 00:25:00 | METOP-C | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff629336-6eb9-31e4-aa4d-e7219786ed72 | -4.7265 | -42.045399 | 2026-01-02 00:25:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 575d4b2e-76a6-3816-a6ad-9be8d98d5068 | -2.8214 | -45.148201 | 2026-01-02 00:25:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce81216d-3d7d-30f1-9d55-252fcf53b55f | -1.124 | -47.735199 | 2026-01-02 00:25:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a2a4a5-c1e6-3f1e-8f20-a726c9736757 | -1.1258 | -47.742901 | 2026-01-02 00:25:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad8401f2-4862-3df3-993e-0acaabc2dbd9 | -5.2891 | -35.733799 | 2026-01-02 00:25:00 | METOP-C | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 6a8e8863-33c9-394f-97f2-a65d5b65bc8d | -8.7166 | -38.628899 | 2026-01-02 00:25:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 84b6de00-6fe0-3684-83db-f2db7474a8f9 | -3.5343 | -43.669998 | 2026-01-02 00:25:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94d39f7a-178d-3e50-acdc-f54e174870cd | -8.7094 | -38.641701 | 2026-01-02 00:25:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5f99923c-8fa2-3dc0-b6a3-3abb18272f02 | -1.439 | -46.587898 | 2026-01-02 00:25:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2fe5938-5acd-384e-adb6-f0ed7380611e | -3.6667 | -48.921799 | 2026-01-02 00:25:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 374f7464-c1c2-3691-9015-94c4a8d40912 | -8.7069 | -38.631302 | 2026-01-02 00:25:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| b6d4fe50-bea6-3259-b731-c8f39ce4e794 | -3.5327 | -43.663101 | 2026-01-02 00:25:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07b0e266-5825-340d-b94d-57f6bc5adb7e | -7.7964 | -35.1129 | 2026-01-02 00:25:00 | METOP-C | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5888928-95b5-3e83-b2b9-171859c1ea94 | -2.8199 | -45.141399 | 2026-01-02 00:25:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 777fb216-b388-3091-9463-5611b1b53061 | -6.305 | -39.5891 | 2026-01-02 00:25:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 63b741ae-22a0-3751-969a-b646cb9d0fc4 | -9.3652 | -35.941898 | 2026-01-02 00:25:00 | METOP-C | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 729d7a14-857a-373f-9d0c-d6e1a28d6111 | -6.2952 | -39.5914 | 2026-01-02 00:25:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 654912ee-9e79-3f54-b657-3ceb4c4e4fe3 | -5.0547 | -43.598 | 2026-01-02 00:25:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1985eb71-bd0b-37c9-8e4b-ef0fefb0a084 | -14.4967 | -52.5526 | 2026-01-02 00:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 04d07437-b360-3d53-a73c-4650cd561a85 | -6.5631 | -51.1126 | 2026-01-02 00:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7f057485-ece4-3882-8203-bb010a86f6d8 | -14.4967 | -52.5526 | 2026-01-02 00:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 6c283cec-6ffc-3abd-8af0-f757351467a5 | -9.8923 | -36.2668 | 2026-01-02 01:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 141.9 |
| 7c9f0dac-5852-35f5-8fc7-dbe8dbc482cf | -14.4967 | -52.5526 | 2026-01-02 01:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1f34cdb3-89c0-32b1-b495-583653898b63 | -14.4963 | -52.5738 | 2026-01-02 01:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| a5f89242-cf0e-355f-ab97-3592553e5a91 | -9.9116 | -36.2634 | 2026-01-02 01:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| 5201f878-537c-345d-a5c4-10ea2c8eb6a6 | -9.9116 | -36.2634 | 2026-01-02 01:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 135.9 |
| 0227b9b0-b315-3934-a3cd-cd605ae82684 | -9.8923 | -36.2668 | 2026-01-02 01:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| 12328016-c9a5-3d8a-841d-2231bbf925e2 | -14.4967 | -52.5526 | 2026-01-02 01:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 8322bf89-3540-3eef-b37f-f19f53c87cba | -14.4967 | -52.5526 | 2026-01-02 01:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 34086c40-0f61-3603-9a9a-8e08575f4e5e | -14.4967 | -52.5526 | 2026-01-02 01:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 9845e034-42f9-3fe4-b15c-a5e36ef24bf4 | -14.4967 | -52.5526 | 2026-01-02 01:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e5116106-a757-37c4-85aa-3a3cd74b0af2 | -14.4967 | -52.5526 | 2026-01-02 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b60dcb02-3cac-3e7b-8457-6ca072ce4931 | -14.4963 | -52.5738 | 2026-01-02 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 851163f2-9abd-3c46-9fc8-b5b4823a0885 | -14.4967 | -52.5526 | 2026-01-02 02:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c1c2a033-40a1-38bd-8a62-7121def25b8d | -14.4967 | -52.5526 | 2026-01-02 02:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 7b5a4c34-71f0-3472-a665-caa6cd5a2e9e | -14.4967 | -52.5526 | 2026-01-02 03:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ad32e4af-525a-3213-a047-7381f0804dc2 | -14.4967 | -52.5526 | 2026-01-02 03:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| eacbfe14-a5d3-375a-b2f3-0921b777bf25 | -7.09477 | -38.78601 | 2026-01-02 03:36:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 65b4266c-a45c-389a-a179-bb39dd1e70fc | -3.32965 | -39.99858 | 2026-01-02 03:36:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ff2795fa-fa08-3eb1-9651-062c5693fed8 | -6.0904 | -37.3985 | 2026-01-02 03:36:00 | NOAA-21 | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0f3e60ed-571e-326e-b6d0-35ebabe8a66e | -6.74634 | -39.27269 | 2026-01-02 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f15de3d6-441e-3594-8c3a-5ac23d1c1afa | -5.28578 | -35.75538 | 2026-01-02 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0fa40b01-3f40-3885-9839-f304438442b4 | -5.74659 | -35.37838 | 2026-01-02 03:36:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 19.9 |
| de54d214-96d0-32c4-a994-5e15753f08ed | -5.93388 | -43.39805 | 2026-01-02 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cf842f8-d7c3-3a0a-9ec4-e2323256fd0f | -5.24183 | -38.13566 | 2026-01-02 03:36:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e9756537-5909-33f6-a201-fe4fb806c947 | -5.72658 | -45.03405 | 2026-01-02 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 806012e9-7fc0-3875-8bb3-9f09072495f6 | -6.78111 | -35.11111 | 2026-01-02 03:36:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 893b8bbb-4606-3838-9822-5b33186ca3bc | -5.03064 | -39.86469 | 2026-01-02 03:36:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 412c2082-2b32-369e-b1c5-23690232a6dd | -7.71144 | -35.10683 | 2026-01-02 03:36:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a8f968cb-8c88-36ac-9861-d9ab547bbe64 | -5.93395 | -43.40047 | 2026-01-02 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7809065-b725-3220-baf9-f8342d7f58e7 | -5.28231 | -35.75484 | 2026-01-02 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 433363b6-fe15-3fa6-a188-5ccf76219030 | -5.28454 | -35.76302 | 2026-01-02 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 11.2 |
| cec7c56d-747c-33fe-95b6-0b34623c2a5f | -6.74283 | -39.26818 | 2026-01-02 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 518568b0-952b-373b-be1a-eba46d509030 | -6.7508 | -35.22406 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c98889a-5f01-3eb3-ab9d-87e84a4c0330 | -4.39384 | -40.42945 | 2026-01-02 03:36:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| edbb622a-d415-309c-8f84-3d112f9c24bb | -6.59546 | -38.37634 | 2026-01-02 03:36:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1344f0fd-8a55-3822-b0a9-d6489ac2fb84 | -5.2379 | -38.13502 | 2026-01-02 03:36:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3f44951b-36f1-3fb1-b8da-31f62863023f | -7.46254 | -35.1944 | 2026-01-02 03:36:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ddd00cf9-9b4a-3671-a552-23eb931e4fc5 | -3.52945 | -43.66787 | 2026-01-02 03:36:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2635c1ae-f7fe-3bcc-804c-68633ef77f91 | -7.69256 | -35.28998 | 2026-01-02 03:36:00 | NOAA-21 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 169d27cf-c6b4-37b6-bfb2-e3d288194d3b | -4.76902 | -37.82746 | 2026-01-02 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b149f33c-1f4c-3482-9089-b250c8a933c4 | -6.75023 | -35.22765 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 21.4 |
| a7bbe9ac-2210-386e-91da-58d628068f11 | -6.7435 | -35.22655 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| deda7ed0-a999-3bb1-bc8d-783a01db8e74 | -6.75302 | -35.23181 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 36.6 |
| dd7ea535-270b-3f26-9c62-8b4b7b611539 | -6.74013 | -35.226 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a68778ce-a117-3134-b721-2fd8b46280c3 | -6.75811 | -35.23253 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 357afb49-f8e7-35d1-9a6c-0c58353767d5 | -7.77651 | -35.4468 | 2026-01-02 03:36:00 | NOAA-21 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08bc5e43-3f83-3443-aa21-bef6bffa1645 | -7.71478 | -35.10736 | 2026-01-02 03:36:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e35b3f9d-a8e1-3d2b-a91b-07c59b70870c | -6.29151 | -39.60501 | 2026-01-02 03:36:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c3956515-8625-32f7-8dcf-49909c6f1f96 | -6.74686 | -35.2271 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 21.4 |
| eb9201b6-d447-3e0f-a305-2f280b2dcd68 | -5.7253 | -45.03652 | 2026-01-02 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 502fcb6d-2a60-3fb6-a02f-dcc2b1e8c153 | -3.52288 | -43.67115 | 2026-01-02 03:36:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dcd883c-a1f1-365e-b863-251cfe91b68d | -7.25232 | -34.99652 | 2026-01-02 03:36:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8bb19a1a-54f7-3697-ad70-5c3ab3310e1b | -6.74511 | -39.26833 | 2026-01-02 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 71c195aa-9bce-36b2-9283-a2314edea683 | -7.712 | -35.10329 | 2026-01-02 03:36:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8be3a85c-4d78-37aa-8f8d-03d9c28793df | -3.52716 | -43.67466 | 2026-01-02 03:36:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bbac365-2f67-3bb5-8869-88499a0dd271 | -5.7262 | -45.03167 | 2026-01-02 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 88a64afc-d2a1-34d2-9e20-4c40935fd486 | -6.75639 | -35.23235 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 36.6 |
| cb87083d-cda8-3e86-bf67-5d8ef582ba12 | -5.27662 | -35.74611 | 2026-01-02 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72e37f6a-354b-3562-8d66-f0bd4e0f138f | -5.72572 | -45.03887 | 2026-01-02 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0f5b7352-4098-3adf-9ba0-11afbda857e3 | -7.46197 | -35.19798 | 2026-01-02 03:36:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c5099bda-b550-320f-8e06-36e82f265bac | -6.74966 | -35.23124 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 21.4 |
| e9c7c0b0-c48b-3172-b307-bdec07cf604b | -6.36014 | -35.32143 | 2026-01-02 03:36:00 | NOAA-21 | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e1a62af-6de5-315e-97aa-bcae5d553f82 | -5.74318 | -35.37786 | 2026-01-02 03:36:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 2873ed25-f3e6-35cf-b0a7-1636ab68c4d4 | -6.75696 | -35.22875 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 36.6 |
| ada141f0-9be0-358c-b198-19e00419c949 | -6.63838 | -35.22424 | 2026-01-02 03:36:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc8a5b3a-12d8-32c2-9397-a7e183202660 | -6.29219 | -39.60097 | 2026-01-02 03:36:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 58e2460c-2f20-35ab-920c-72576e5396e7 | -6.02064 | -44.55103 | 2026-01-02 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba62c825-8340-3eed-839b-14f9507ab345 | -6.7486 | -39.27283 | 2026-01-02 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64d8bbcf-33cb-3568-8154-056c5db00adf | -7.71761 | -35.08961 | 2026-01-02 03:36:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dad84193-f9b0-3ddf-a9d2-9226af886366 | -6.08519 | -37.40684 | 2026-01-02 03:36:00 | NOAA-21 | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1f1b86c-1560-3205-84ba-2011a06e7a95 | -7.6892 | -35.28945 | 2026-01-02 03:36:00 | NOAA-21 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |


[Clique aqui para ver as próximas entradas](README2.md)
