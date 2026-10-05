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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3698417a-12f9-3563-85e5-e3b460281a78 | -6.60372 | -41.5771 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| c9a1e4b6-33cc-385e-8881-2e56a41f0b2a | -6.90325 | -43.67308 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 76b728a7-38e9-3d90-a434-e0eca77a46bf | -9.61875 | -45.83487 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3a548b2e-04b1-306b-8ea4-9be48c1f1e03 | -9.56751 | -45.05604 | 2026-10-05 16:37:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6242dbff-9644-3eb1-bc24-1acfbd806cc2 | -12.14367 | -50.99163 | 2026-10-05 16:37:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cac9f91a-92ed-31c4-af34-0d1493a8fcd5 | -8.53683 | -54.59704 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1dada723-1054-39ec-a965-323eba9f7ef4 | -7.55333 | -46.72557 | 2026-10-05 16:37:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 75601c1d-adc2-33fd-9f8b-ed311f094aef | -6.59877 | -41.57379 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0bc8ba50-7f7b-3ff5-a170-0b1951bbb8e7 | -10.50368 | -46.03945 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 49d40324-d126-3825-b91c-b983a83c661c | -7.18737 | -44.32585 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 438966a2-f86b-32a8-bf71-a619c5daa350 | -10.49982 | -46.03645 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| af4120b4-6a90-391d-9530-a20d04045e2e | -6.20746 | -41.59335 | 2026-10-05 16:37:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6d1ff8ee-fe0d-31de-8dde-52d2d4803066 | -6.8008 | -39.2958 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| abd83ac5-9fd5-300c-bf53-c8b1742d2526 | -10.3945 | -47.53572 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c15d8ca5-749f-3865-97a7-54b5594e4fd7 | -5.91039 | -38.05202 | 2026-10-05 16:37:00 | NOAA-21 | TABOLEIRO GRANDE | RIO GRANDE DO NORTE | Brasil | 2413805 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 69fad852-ec53-3333-9e1e-f4343db54b3f | -12.81575 | -43.30347 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 417a3103-a50e-3670-a0a5-db4136ff709c | -6.53948 | -39.51829 | 2026-10-05 16:37:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| f4839e67-3c26-3bb9-8b27-51a69db0bdfa | -7.84101 | -40.4747 | 2026-10-05 16:37:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2b7f3528-484e-3041-ac30-11f25f6a98df | -10.50036 | -46.03997 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 50b59908-e92e-3a99-873a-1ec66c1ab41a | -8.34541 | -44.74286 | 2026-10-05 16:37:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3005610b-04b4-319f-8f02-00c3e574d777 | -6.8053 | -39.29221 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 526e1984-f308-3367-a935-e9aea13d8205 | -17.34167 | -39.55703 | 2026-10-05 16:37:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c825b215-d97c-3e78-9fd9-b396a9142792 | -7.04635 | -44.30923 | 2026-10-05 16:37:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 86590077-336b-3053-8baa-f8bd79f2f2dd | -8.55068 | -54.58671 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| dc6238ee-b769-3a5d-8be2-84e23d027b3c | -9.74618 | -48.17391 | 2026-10-05 16:37:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 26956c3a-a623-392a-9fde-a916be9073ac | -10.96607 | -45.44777 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 06a9fce9-eda7-3391-879c-7f7f0e493398 | -7.13719 | -44.69427 | 2026-10-05 16:37:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eea75a60-ae1c-3d62-b904-3c27be8a6c77 | -12.80935 | -43.30874 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d00538d8-d833-3a76-9f22-7f57e572b60d | -12.81354 | -43.3122 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| dc1184dc-69f7-3958-9236-b3a33e176bc1 | -11.25668 | -47.69672 | 2026-10-05 16:37:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8ce8cfd7-d17f-36d8-a16b-bf5bdbb5122e | -8.7808 | -47.55529 | 2026-10-05 16:37:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa131b62-d4d0-359b-98f8-0210c75ee192 | -8.84314 | -37.74443 | 2026-10-05 16:37:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1ced57b0-b8bf-3958-bb2e-40babf667b58 | -13.00455 | -44.56897 | 2026-10-05 16:37:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 92a14b6e-781a-3640-843c-ab396cea1a45 | -8.97443 | -36.63443 | 2026-10-05 16:37:00 | NOAA-21 | SALOÁ | PERNAMBUCO | Brasil | 2612307 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 72228c51-b40a-37a4-9911-fc437dfb039d | -11.20565 | -47.14685 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3779a1a4-43d8-3cc2-b40d-d857d1004973 | -12.85602 | -40.41028 | 2026-10-05 16:37:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 21de1e8b-1f1d-3b90-b034-fe7fc64106e7 | -7.18666 | -42.00735 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1cb73895-f21f-31ef-9629-dab436ce615b | -11.43949 | -47.68785 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9c5396a4-ab76-3de1-b5e2-089390462ace | -6.68559 | -45.23298 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3b77a298-4c2e-3764-b9b5-dcbd3eb5e5d8 | -11.76776 | -44.92011 | 2026-10-05 16:37:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c3555105-a754-3138-acf4-c77c20e6405a | -12.43242 | -51.33109 | 2026-10-05 16:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f91463d-3f4b-3003-a2b2-d573f8103237 | -9.85856 | -44.81032 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 252a62e6-34e1-35a2-988a-7c40c8969f61 | -5.67737 | -37.78673 | 2026-10-05 16:37:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ec16114d-a0a2-30a0-b239-1b6440f74d04 | -11.65709 | -43.60908 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| db8b2d08-b9c9-3d04-8fe0-5aec55829ca1 | -6.69717 | -45.239 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 328aaf97-7272-3dce-b143-111b7beb6502 | -10.97441 | -45.43533 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e36c8777-eeaf-3e95-96f3-37489bd2cdae | -10.34499 | -40.0707 | 2026-10-05 16:37:00 | NOAA-21 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5cd69889-0e12-3143-b334-1ebce43d6304 | -8.03264 | -40.55776 | 2026-10-05 16:37:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ddaa751b-cc93-32e5-af51-598bb7c0aa40 | -8.55545 | -54.58611 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 7c02e322-1f4a-34a2-b00d-6f637d7c4795 | -8.30677 | -39.15434 | 2026-10-05 16:37:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8b6dc68e-950d-36c6-adf8-dacc722cc892 | -8.65025 | -45.83758 | 2026-10-05 16:37:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1fa5297b-b9a1-3edc-bb46-8996c6e13773 | -8.01429 | -46.45159 | 2026-10-05 16:37:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e9231887-16ac-34e4-9da1-10da2d82af14 | -11.09443 | -41.25835 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 54207d61-1533-361b-8588-180be2bd165e | -6.28526 | -43.07946 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e56d497a-5a18-37df-8dbc-8f8186199377 | -6.37717 | -43.63191 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4e07f15b-9018-3707-9770-0e1d3814197c | -11.09991 | -41.26447 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 15526627-cc9a-361f-a594-87628b2e0c51 | -13.31899 | -40.47126 | 2026-10-05 16:37:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6b6d9ebe-accf-3cf0-9f65-7ddab7213124 | -11.82625 | -47.16493 | 2026-10-05 16:37:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15176a55-b269-39f1-83b6-67e86331f8ea | -6.60461 | -41.55628 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 997305f4-36a3-398f-bf6c-44c909f0957f | -12.3476 | -47.06161 | 2026-10-05 16:37:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f36c7643-eb8d-37eb-8905-89b51ed4e461 | -9.85796 | -44.80653 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8f9e7047-04bf-392f-9691-e000e465e1bd | -11.66012 | -43.65017 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1da4f2c5-dfd9-3d95-be8e-d9c0f3d09d9f | -8.53207 | -54.59769 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3ff5789b-c8b5-3333-8c86-d1856d0b1da9 | -10.21446 | -46.68134 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a2b3b72a-52ea-39d1-9f79-290b354f898a | -13.0121 | -39.72622 | 2026-10-05 16:37:00 | NOAA-21 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5a6b889f-6bad-35d3-980b-e64e15985fbb | -11.67901 | -43.65513 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4a72c86e-45c6-357c-bb36-710038674376 | -11.08632 | -41.25974 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ed92c75b-a63c-3636-b796-ca8aab8555bf | -11.63568 | -43.63334 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| bf742531-b1a8-37cd-aa62-d4b90a59ff6c | -10.23136 | -46.6567 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ada5b335-47ff-359c-bd04-5ac9ee84178c | -10.9516 | -45.42087 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a41838d7-a857-3746-9e60-6057338fff94 | -6.72174 | -44.27389 | 2026-10-05 16:37:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f893a5e9-ce38-3e90-b2ca-a74c37ae57a3 | -18.53303 | -41.71536 | 2026-10-05 16:37:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2a3ec44c-7ecd-35ba-b1b1-512b495f14f0 | -9.86275 | -44.83664 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 10c9bcbb-0e59-346a-8b52-fdea43f8a24e | -13.60392 | -42.49981 | 2026-10-05 16:37:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 4fd9a98c-daa1-384a-aa6b-0a3ab8126584 | -8.97603 | -36.63412 | 2026-10-05 16:37:00 | NOAA-21 | SALOÁ | PERNAMBUCO | Brasil | 2612307 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| de410907-9a4c-3608-ae4c-8f4895e8534a | -11.68446 | -43.66654 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 0ed740d0-6c77-3999-9ca1-50c6072485f5 | -6.88161 | -43.68114 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| a9de68ec-218b-35f5-b391-83cb8be72d25 | -11.19879 | -46.27181 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f531853-e382-3796-9540-b6b12327d19c | -8.7869 | -47.55079 | 2026-10-05 16:37:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70f23b02-b5bb-3078-8c3b-506d4b29791f | -9.54009 | -41.63625 | 2026-10-05 16:37:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 26e41afe-8b6b-3450-803b-fc8bb19179e3 | -6.85716 | -38.68647 | 2026-10-05 16:37:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3c555207-4eac-34be-a8ce-3ad26cb35180 | -10.97107 | -45.41387 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 40283c60-1b10-3de7-bd69-3d1df68d080e | -9.62715 | -47.69557 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b652ba0d-c559-37eb-95bb-5ff22ce3a266 | -18.59067 | -41.28135 | 2026-10-05 16:37:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 39e2df41-dbba-389a-9679-069f01c178b8 | -7.19194 | -44.3084 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a5cedc9-f125-3293-8b8a-06a3a05b4847 | -11.95564 | -40.64137 | 2026-10-05 16:37:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e2ba6d25-e6ed-3927-a446-5339f3706450 | -8.55372 | -54.57909 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bbe6614a-26b6-38ba-8011-0114ce0205af | -11.38216 | -42.54991 | 2026-10-05 16:37:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80a45659-c1e9-32ee-bc8a-8219f236edea | -11.36663 | -41.25906 | 2026-10-05 16:37:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 69cdca95-0d0a-37ba-a34c-9001478fdd31 | -6.7703 | -39.02715 | 2026-10-05 16:37:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5ad43ded-c755-3d61-a334-142fbe851634 | -7.68498 | -40.30849 | 2026-10-05 16:37:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 67b2b340-bd50-3a71-ba31-370078740535 | -13.41635 | -40.93845 | 2026-10-05 16:37:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| d7c8f24a-7d75-38cf-8cfd-3177b2057d79 | -11.1624 | -43.49235 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7ec6a763-306c-3dfc-8b22-c4a2217e9b14 | -6.70921 | -45.22528 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 90f59ba7-8881-3918-8490-f84903052649 | -11.2107 | -47.13524 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6f09613b-678c-3b7b-92a6-fb2112de4b10 | -9.03992 | -46.89074 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1ef710f3-eb31-39d9-86d9-085876373877 | -6.90397 | -43.67759 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| dbbf8a9e-212a-3b31-959c-4e67a5baf140 | -10.48371 | -47.24686 | 2026-10-05 16:37:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 09ae456f-a78e-3f7b-8beb-c9205849a3aa | -10.4959 | -46.05505 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a90b13a-c8f0-3425-8e64-0aa87d0894c3 | -6.39412 | -38.90918 | 2026-10-05 16:37:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |


[Clique aqui para ver as próximas entradas](README83.md)
