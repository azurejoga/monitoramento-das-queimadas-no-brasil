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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b532aea2-0238-381b-abf8-85ffef4e4ea0 | -19.807899 | -49.595299 | 2026-09-05 00:08:00 | METOP-B | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d132e59f-597c-380e-988d-2ef463bc7654 | -5.9261 | -47.884602 | 2026-09-05 00:08:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31f2b92a-9e8b-3813-b7f9-6816277e83ff | -4.6708 | -55.635201 | 2026-09-05 00:08:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1bc5fd-d3d3-348b-a566-1107f766a6e7 | -1.1779 | -53.810902 | 2026-09-05 00:08:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aca149a9-092f-31fd-99d6-f3d8699b7daa | -4.1544 | -49.702202 | 2026-09-05 00:08:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74478b80-6ebd-350d-ae16-49741172ecfa | -5.7663 | -45.055901 | 2026-09-05 00:08:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eae84120-62c6-393d-81b2-4864670f992a | -17.2314 | -53.849098 | 2026-09-05 00:08:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ced8d2df-151f-3727-aaf5-4e0da858801a | -3.2258 | -50.562302 | 2026-09-05 00:08:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5611dc34-22de-33bc-abc3-b5ae5631757b | -11.8576 | -42.5326 | 2026-09-05 00:08:00 | METOP-B | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| be954715-9b16-3610-a065-bcba8cc4a962 | -20.233801 | -51.2145 | 2026-09-05 00:08:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70dff7ac-6d26-3a38-926a-f3eb3f6e1198 | -12.9246 | -42.416698 | 2026-09-05 00:08:00 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6f0fc0b7-f1bc-38dc-879d-372981d964c1 | -4.6656 | -55.611099 | 2026-09-05 00:08:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce25c14c-4aed-3e52-a2d7-1c7b6b802ab4 | -10.481 | -46.034 | 2026-09-05 00:08:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b01939f-8410-38b0-844f-2bc1fb9639d7 | -10.7813 | -44.453602 | 2026-09-05 00:08:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 571d4b37-0d9c-3864-a3cb-ec269fdd8f2f | -9.6128 | -48.555901 | 2026-09-05 00:08:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d996f47-996c-3588-8b0c-812b8c52998a | -12.8497 | -44.379101 | 2026-09-05 00:08:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1855b91-1262-3f29-950f-ad83b4045e33 | -20.9849 | -45.7966 | 2026-09-05 00:08:00 | METOP-B | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 62a6249a-57cc-3fa4-9bc2-88a0e0a58c28 | -20.341101 | -47.594398 | 2026-09-05 00:08:00 | METOP-B | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7f00335f-c105-3aea-8b75-4e4fe048d3a9 | -20.8293 | -46.313 | 2026-09-05 00:08:00 | METOP-B | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 311dc89e-1a05-3f38-918b-2f9775954711 | -17.106899 | -56.802601 | 2026-09-05 00:08:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c956b46f-3039-3fb9-ba54-22f2729d62a9 | -15.0675 | -52.5145 | 2026-09-05 00:08:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3c94d91-55f6-399c-92d9-c7235e2c4d8b | -3.5735 | -59.389198 | 2026-09-05 00:08:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7807149f-ddbc-32c0-8f4a-c728e24bf7c3 | -21.240499 | -46.844501 | 2026-09-05 00:08:00 | METOP-B | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 184f3c18-fc66-3c66-8baa-489be8947908 | -3.1462 | -60.6317 | 2026-09-05 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| bb31e6a2-0f82-3651-93b0-c125f434deba | -6.6698 | -59.9443 | 2026-09-05 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| dfc25679-aaaf-304a-a470-82713c0fb581 | -3.7645 | -61.7548 | 2026-09-05 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 571be721-3744-37b8-b480-e8ccdeaab3ca | -3.7645 | -61.7737 | 2026-09-05 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| a196cf37-3424-3f9d-88ce-944b1d8c0a14 | -1.1832 | -53.818 | 2026-09-05 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7e6777e6-7dca-3adb-bc60-a2d1a2b96f09 | -13.4259 | -43.8401 | 2026-09-05 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| f21afeb5-06c5-3062-be75-66c74aae041d | -13.4453 | -43.8366 | 2026-09-05 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 8e55ad10-80a1-3642-9ab5-32df660f8988 | -17.1081 | -56.8098 | 2026-09-05 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| f8156378-e514-3c45-a81c-88366485ae70 | -19.8254 | -49.5921 | 2026-09-05 00:10:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.4 |
| be0390fb-9076-3724-8ba1-fb54ba06907b | -13.4264 | -43.8163 | 2026-09-05 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 237.8 |
| f72e2095-85d9-3514-8fea-f18b91768fd2 | -17.1078 | -56.8304 | 2026-09-05 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.5 |
| fd828e01-604c-37df-ac58-a328bf48534d | -4.6669 | -55.635 | 2026-09-05 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 90316c53-0917-3686-a843-8536000c14d7 | -3.7828 | -61.7545 | 2026-09-05 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 1dfc9c16-7e79-3922-85c5-0c3c72288a40 | -6.6514 | -59.945 | 2026-09-05 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 32674217-1328-3797-be9b-053400a966c9 | -5.7758 | -45.0599 | 2026-09-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| e5992526-75c6-3eea-a925-b42ab6f475d0 | -3.7827 | -61.7733 | 2026-09-05 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e753c1f9-3667-347b-906c-66a64babcdd7 | -5.7571 | -45.0613 | 2026-09-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 75a09c99-1dce-3329-9288-b927bf69323e | -3.1462 | -60.6506 | 2026-09-05 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e954bb2e-afd5-38b7-821b-64c05b1ffa22 | -5.7756 | -45.0826 | 2026-09-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 563204b9-707d-3f78-8304-5bb00ea54b7a | -13.4458 | -43.8128 | 2026-09-05 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 22da781c-17ae-324d-b12a-afc838c44036 | -19.8248 | -49.6148 | 2026-09-05 00:10:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.1 |
| 039641e4-4d6f-3fee-9711-5c17082db094 | -20.23 | -51.22 | 2026-09-05 00:15:00 | MSG-03 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3f9e822-4a1f-3998-a80c-2540b54b4b66 | -13.44 | -43.83 | 2026-09-05 00:15:00 | MSG-03 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca305be-f8a9-37a3-b42b-26388bc8d92e | -17.5351 | -50.0321 | 2026-09-05 00:20:00 | GOES-19 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 0bdd2ab2-de5f-328c-8e7c-4640d5dde5a9 | -10.176 | -36.539 | 2026-09-05 00:20:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 62.2 |
| 238a4994-0ebd-370b-b37b-2bcf68d3efc2 | -3.128 | -60.632 | 2026-09-05 00:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 15aef658-cbf1-3541-bf82-39c5f224ac99 | -13.4264 | -43.8163 | 2026-09-05 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 267.9 |
| f71c0650-1ee3-3771-9ad1-ab18bbecfe4e | -3.1462 | -60.6317 | 2026-09-05 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a2cd1057-e550-3cb4-851b-e51e9d78566b | -13.4453 | -43.8366 | 2026-09-05 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| b20b536d-7915-36d6-9f49-210aed17dfd6 | -3.7645 | -61.7737 | 2026-09-05 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6a8adb33-0ef1-3f56-8f6d-3f6388613b46 | -13.4458 | -43.8128 | 2026-09-05 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 87fcdea6-af4e-338c-9e6e-cc7494c04ebb | -5.7758 | -45.0599 | 2026-09-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 1685f7a3-4567-3ac7-a306-f2d8c2e1b193 | -5.7756 | -45.0826 | 2026-09-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 0c16b26e-9bb3-3d12-8186-2a00964474bf | -10.1765 | -36.5121 | 2026-09-05 00:20:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 44b8c752-ab11-3f48-aff1-ffe48a4304df | -3.7828 | -61.7545 | 2026-09-05 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 22f563e2-f8da-300c-abb8-e3353d48d3d1 | -3.7827 | -61.7733 | 2026-09-05 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| fa6eb671-f2b1-3363-8615-1ccbbf4a3665 | -17.5152 | -50.0356 | 2026-09-05 00:20:00 | GOES-19 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 124.8 |
| fa9005d1-7784-34ce-99f0-b7d0ad3c7431 | -6.6514 | -59.945 | 2026-09-05 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 657e8365-2d01-3625-ba43-7b379bc41585 | -3.7645 | -61.7548 | 2026-09-05 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 93c96405-995b-3aa5-8de5-539a16d298ae | -3.1462 | -60.6506 | 2026-09-05 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8af3f265-804a-3d1c-9611-dcfd601988dc | -13.4259 | -43.8401 | 2026-09-05 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| e73b4440-4930-3f72-9865-2a59e29cb5da | -6.6698 | -59.9443 | 2026-09-05 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 72b11402-6a0b-3f75-b7b1-6707d42499c5 | -15.0769 | -52.5396 | 2026-09-05 00:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b3b5f076-cde1-3ac5-b859-aa38311560eb | -5.6565 | -60.2475 | 2026-09-05 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 62002732-589e-355d-b5f6-89b379249009 | -5.6566 | -60.2284 | 2026-09-05 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| aed744ef-8d3b-3a70-a42d-9b66c27fea72 | -3.7827 | -61.7733 | 2026-09-05 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 83376250-7709-37da-81d0-360f362e1a3b | -18.1111 | -51.7786 | 2026-09-05 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 393ee273-128b-3cde-b556-69d48f347ef8 | -13.4259 | -43.8401 | 2026-09-05 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| a617f2f2-b07b-3232-8ec2-f6167a552a53 | -5.9383 | -47.8915 | 2026-09-05 00:30:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 7b70065a-3e70-31ae-9922-802af2127c39 | -4.6853 | -55.6343 | 2026-09-05 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 48698289-0cbb-3a85-b0f2-fd4d42c6b928 | -12.933 | -42.4192 | 2026-09-05 00:30:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 9369a6f4-a6a2-3520-8e27-32eb98447879 | -12.9136 | -42.4227 | 2026-09-05 00:30:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 20c48130-df06-360e-a397-99374abccf34 | -18.131 | -51.7752 | 2026-09-05 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ffb7dd5d-d301-3791-925a-a3ee72438fe3 | -3.7645 | -61.7548 | 2026-09-05 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9e444c98-1212-35fe-abd5-816938f24a57 | -18.1116 | -51.7567 | 2026-09-05 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| b24b0278-021e-39c9-82af-04086d0ea497 | -6.6697 | -59.9635 | 2026-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b98a2920-9dea-3477-8801-f816569a59c1 | -4.6669 | -55.635 | 2026-09-05 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| d8a105dc-fd9c-3914-81ad-8324b2124304 | -5.7758 | -45.0599 | 2026-09-05 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 73e14f76-0351-38e3-b1f6-56f5926f91f1 | -6.6698 | -59.9443 | 2026-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 0b6ab55c-221b-31df-bc10-7a976d4d6257 | -4.6854 | -55.6145 | 2026-09-05 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 045350ff-5b1b-3f55-8909-dfb08ef066ea | -13.4458 | -43.8128 | 2026-09-05 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 4d4265e6-d4a8-343d-855c-348f82ede12d | -13.4453 | -43.8366 | 2026-09-05 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 6b6fbd3e-f3f8-3ed8-8bbb-74da4e192d18 | -5.9197 | -47.8927 | 2026-09-05 00:30:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a0b51d38-4d1e-3d80-86c1-14aec8e4615f | -6.6514 | -59.945 | 2026-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 162f7b8b-d23e-31be-8196-2b6c0582cfab | -13.4264 | -43.8163 | 2026-09-05 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 196.8 |
| ef6053c0-5604-3b04-a618-200f77a013eb | -10.4717 | -46.0216 | 2026-09-05 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0d6dff72-fba5-3010-8139-2c499a090e91 | -12.8543 | -44.386 | 2026-09-05 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a0dea75e-5539-3b55-946a-e88a1f027028 | -3.7645 | -61.7737 | 2026-09-05 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 19d5b037-1a90-31d6-bf20-d31d2b626d07 | -6.6513 | -59.9642 | 2026-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1a5903d9-185b-30a6-a6ca-0dcc6d88baa8 | -5.6565 | -60.2475 | 2026-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9dc70f70-7b88-38bb-823e-bbeedc5cb37b | -5.6566 | -60.2284 | 2026-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| fd79f840-dc04-39c5-85ef-216484768afc | -3.7828 | -61.7545 | 2026-09-05 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 1f2e1f24-b2be-3dbe-872c-92fce15fbaf0 | -15.0773 | -52.5183 | 2026-09-05 00:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 52b1b973-b312-3d44-b003-11e7566e72a4 | -5.7756 | -45.0826 | 2026-09-05 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 8029a9d5-82ac-3770-b530-908823936e64 | -20.2586 | -46.342999 | 2026-09-05 00:31:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3203dbb4-d732-374e-af58-21586860e733 | -4.1513 | -49.702801 | 2026-09-05 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d50236f-648b-30ee-a8cf-0a350f07fcff | -13.4295 | -43.808498 | 2026-09-05 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
