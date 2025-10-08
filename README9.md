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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04381a5b-6920-33ad-b128-88115ef9da56 | -14.7184 | -46.0636 | 2025-10-08 01:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f4fe3be1-85a6-3865-a6e1-62030b1e2706 | -17.5348 | -40.189 | 2025-10-08 01:10:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 100.3 |
| 89928555-4ca9-3c19-8484-18a103e6d83d | -4.6873 | -45.8504 | 2025-10-08 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 8a0e1e9b-a94c-3baf-a811-482ccf4edf86 | -7.5874 | -64.5097 | 2025-10-08 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| dd131bc9-4de4-3e43-aba9-aa502475860d | -5.325 | -43.0884 | 2025-10-08 01:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| aa46cfb3-f4ac-3854-b72a-bc43f8c67d70 | -3.7937 | -49.4211 | 2025-10-08 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1e5445e7-60f3-3402-8796-67550b7bad3f | -5.1414 | -44.967 | 2025-10-08 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 269.0 |
| 9242d001-cd27-3fd9-adea-d94013d0ab3c | -4.4977 | -46.3731 | 2025-10-08 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 31804ad7-dfd1-3cec-a690-ec7b8ec1dca6 | -11.6888 | -50.9833 | 2025-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 302.5 |
| 934d9642-a4f1-39c4-a633-1f2330236381 | -7.6058 | -64.5092 | 2025-10-08 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ee855e69-0bbb-3af7-b6d7-85fa5dc1fcc3 | -5.2601 | -44.1368 | 2025-10-08 01:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| d1ab40e1-6b5f-3893-bc0a-3aa3deebfbd0 | -11.7079 | -50.9811 | 2025-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 8733c72a-855c-3029-82ce-7f813637b99f | -12.031 | -45.2132 | 2025-10-08 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 69bd5518-e2cb-3966-84e7-27dc56b66429 | -10.93 | -51.0229 | 2025-10-08 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| f95c8f50-9fc6-3423-9e34-37c8fa7dbd39 | -9.6108 | -40.3171 | 2025-10-08 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 1b29491a-b612-3949-a7c4-342be02bf585 | -11.6891 | -50.9619 | 2025-10-08 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 74b73aef-83c0-39fe-87af-16660db48416 | -4.6873 | -45.8504 | 2025-10-08 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 239c0a28-e511-3331-a1a1-241a44f88953 | -9.6104 | -40.342 | 2025-10-08 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 220.1 |
| 577aed38-0cb9-3f24-8f15-bd18a282a83c | -7.3444 | -43.8735 | 2025-10-08 01:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 44.6 |
| c07226f3-cb82-3ff7-9b96-04cdbcf19aa2 | -17.2847 | -42.623 | 2025-10-08 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 40f19650-6705-32eb-8cb4-793c9046015b | -6.9982 | -42.878 | 2025-10-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 2cb9d0f8-657b-3026-b6f1-7425be7da25c | -17.284 | -42.6479 | 2025-10-08 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 579.1 |
| 67b18374-9df1-3e6f-b886-643962bb5b48 | -5.1229 | -44.9455 | 2025-10-08 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4d7300fe-3932-375e-84af-2db71a60e286 | -7.017 | -42.8762 | 2025-10-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 169.7 |
| c3ccdd57-da77-31b0-8672-3143af8b951a | -4.4978 | -46.3509 | 2025-10-08 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 6606eda7-1355-3286-b37e-41a30745e35d | -17.2833 | -42.6727 | 2025-10-08 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| cc92e123-106e-3c60-a143-6f552fd92e95 | -14.7184 | -46.0636 | 2025-10-08 01:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 384d27af-24ca-39bc-a654-25fa724aeee5 | -5.1414 | -44.967 | 2025-10-08 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 45e0e3bb-c8f2-3a3b-bea2-706eff49566c | -2.519 | -44.1139 | 2025-10-08 01:20:00 | GOES-19 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 3133a91b-d886-378c-b5b1-ac02c426568b | -7.5874 | -64.5097 | 2025-10-08 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 07824b48-05cd-3e49-903d-8cc4355083c0 | -11.3686 | -55.1672 | 2025-10-08 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 70523aa6-7dab-328a-a6f5-77dafcd677d1 | -9.6295 | -40.3392 | 2025-10-08 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 245.3 |
| 1c91a26b-fd94-35af-973d-f1b6b93def61 | -11.6885 | -51.0046 | 2025-10-08 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 6e403d0a-912d-3946-8685-3ed18e3d5d56 | -15.7019 | -47.5117 | 2025-10-08 01:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b278618e-deaf-3f31-9e13-b5fe4af5c582 | -7.6474 | -63.4584 | 2025-10-08 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 672dffe1-b4b0-3737-a63d-ff2f995dac89 | -7.0356 | -42.898 | 2025-10-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| e1db84cc-1aba-351b-84bf-fbadcc8383ee | -9.6254 | -40.5875 | 2025-10-08 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 28304578-0f67-35ef-94cc-109ae7084881 | -17.2639 | -42.6527 | 2025-10-08 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 08f470ec-1027-3df9-9b5e-d3869da080cb | -9.6299 | -40.3143 | 2025-10-08 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 174.2 |
| 967c03a0-5ccf-3344-ac3d-b54cb8cd188f | -9.6446 | -40.5847 | 2025-10-08 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 42.6 |
| 3235f0f3-9155-3b3c-935f-9bd61a40f4b3 | -5.1416 | -44.9443 | 2025-10-08 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c25bf231-6173-3a0e-b63b-505090ce54b1 | -9.6108 | -40.3171 | 2025-10-08 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 157.1 |
| 0bac3093-4b7a-34f6-a4f7-c9508f7ce200 | -4.6875 | -45.828 | 2025-10-08 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 85d58a56-af0d-3e6e-8ce2-1eefbfdd73d5 | -3.7937 | -49.4211 | 2025-10-08 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| dd3d53ac-e351-3f00-8e6e-0dd70c508d32 | -11.3495 | -55.1892 | 2025-10-08 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 1ff52707-cfbd-361e-a999-ce9c4e0bbf1c | -11.7079 | -50.9811 | 2025-10-08 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 92073679-017b-3cb7-9862-eee1a5c7d103 | -12.031 | -45.2132 | 2025-10-08 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| ae11928d-9a03-3890-a135-cda49ff9c6d6 | -11.6888 | -50.9833 | 2025-10-08 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 304.8 |
| f9e1c2a9-6d6a-3e59-84bb-62f733be2e57 | -7.0359 | -42.8744 | 2025-10-08 01:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 74f0082a-4b50-3d1e-a4f8-9201c98416ff | -19.5148 | -44.0522 | 2025-10-08 01:20:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 9caaffb3-5478-3c98-910b-7b24f65bc5db | -11.3684 | -55.1875 | 2025-10-08 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 199b770a-71cc-380d-a444-370573fe6d2d | -7.0167 | -42.8998 | 2025-10-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| f3b34b8c-c6f6-30a2-8d92-ea095401409d | -12.3971 | -63.8811 | 2025-10-08 01:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 752fbe39-52bd-34a5-bd65-fdce1ce98e26 | -17.3041 | -42.643 | 2025-10-08 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 254.5 |
| 724d09c0-946e-3501-9d8b-3faaec2a207b | -5.1227 | -44.9682 | 2025-10-08 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| fd0d4c16-0d6e-3295-92ca-74281a4bfcad | -17.9817 | -57.5056 | 2025-10-08 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| e3b23f3d-09eb-3375-b8b9-84d4d22cda9c | -4.4977 | -46.3731 | 2025-10-08 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d04d7ce4-8f23-3ab2-bd9e-f432ea534b20 | -19.514 | -44.0768 | 2025-10-08 01:20:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0c60b03f-e32e-35ed-bc3d-1b5910952fac | -11.7076 | -51.0024 | 2025-10-08 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 47733f9d-b387-31ac-8747-1fd88fd69937 | -9.6299 | -40.3143 | 2025-10-08 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 144.4 |
| d5759561-fb95-3ded-af89-aea49cf3c5d8 | -5.1601 | -44.9658 | 2025-10-08 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b8215646-ed4a-315c-aca5-91cae20d6269 | -9.1904 | -46.9326 | 2025-10-08 01:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5685105b-31b8-3dec-89c3-455f50ee6385 | -11.1646 | -54.86 | 2025-10-08 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| c7eeb342-bb53-3330-affe-43157973f0e1 | -3.4422 | -45.598 | 2025-10-08 01:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 41.0 |
| a309fbe8-b691-3a99-a5f4-70364133777f | -9.1907 | -46.9104 | 2025-10-08 01:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| ec7e1326-8d69-3731-a555-5fb7e8d3146e | -15.9568 | -42.5876 | 2025-10-08 01:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| d6105065-2d2f-3c14-bd1b-acbf65861bfb | -9.6295 | -40.3392 | 2025-10-08 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 222.0 |
| 71397eb4-5bc7-3709-940d-95c45a902ab6 | -11.1455 | -54.882 | 2025-10-08 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 50d7737a-98af-36ce-b475-ea139b5916aa | -15.7019 | -47.5117 | 2025-10-08 01:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 490d92cf-7a27-3e28-924c-b3d5e7e314a6 | -9.6108 | -40.3171 | 2025-10-08 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 9243ea0b-833f-3209-a039-4633fb714dd8 | -17.3041 | -42.643 | 2025-10-08 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 311.2 |
| d8bf3d23-238b-3477-8706-27790ac9717e | -17.284 | -42.6479 | 2025-10-08 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 425.5 |
| 3906dfdb-bd49-392e-9dfd-ceea63b287d9 | -7.017 | -42.8762 | 2025-10-08 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 229.8 |
| f433aafe-998d-39ee-bcdc-4430bb337038 | -12.3971 | -63.8811 | 2025-10-08 01:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 648edbf9-7035-3694-aa77-ba41d9e34d0f | -11.183 | -54.8991 | 2025-10-08 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 199.3 |
| 42206b6a-02c8-30a7-a7f0-4082b5daa3f2 | -11.7076 | -51.0024 | 2025-10-08 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 7a862326-c29e-3713-a141-d9e507c8eb84 | -8.5584 | -46.2387 | 2025-10-08 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 92e32a73-142d-3f55-b517-4ce86d5243b2 | -5.1414 | -44.967 | 2025-10-08 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 65f0226a-d69d-3e93-a574-eb043a9a6eea | -5.2601 | -44.1368 | 2025-10-08 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 2b00a2c0-2d0a-3a5d-9e3f-f88eabcd9e04 | -11.6885 | -51.0046 | 2025-10-08 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4157e919-36d5-3683-a944-d4201c867cec | -17.2847 | -42.623 | 2025-10-08 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 83687ef4-bf78-3cae-ace2-3404f410df2d | -5.1416 | -44.9443 | 2025-10-08 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 071587d2-88f7-3f14-855f-58800c2f09f2 | -11.3495 | -55.1892 | 2025-10-08 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 04445513-fc96-3ce0-92fc-0d568180539e | -4.4978 | -46.3509 | 2025-10-08 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7ce461ec-cc1d-3a6c-8a31-54a117619eee | -11.4534 | -50.198 | 2025-10-08 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 4aa6a889-8617-32a8-928e-4422f172f9f9 | -12.031 | -45.2132 | 2025-10-08 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 20edae5a-5403-323e-b374-88762b9adaa6 | -7.0167 | -42.8998 | 2025-10-08 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 148.7 |
| 44e97b17-29fc-305c-a5b8-69e2c0f9f2ab | -11.1833 | -54.8787 | 2025-10-08 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 273.1 |
| 5bfb8ca7-df6b-3246-aa5a-eebc75f4889a | -7.5874 | -64.5097 | 2025-10-08 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 29b27a68-6e63-350b-8b17-b5d066883529 | -17.2833 | -42.6727 | 2025-10-08 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f9f9551a-253d-3c09-9ab8-c27b626f4437 | -11.1642 | -54.9007 | 2025-10-08 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 0ce7cd05-804b-34e1-a614-07295788a4bd | -11.6888 | -50.9833 | 2025-10-08 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 182.1 |
| ea7564e1-b9d3-3706-b765-5c86dc5d27d8 | -11.3684 | -55.1875 | 2025-10-08 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| a5105452-d3a7-3390-87c9-3ef660c88bd1 | -7.0356 | -42.898 | 2025-10-08 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 1f265d08-bb11-314d-ae19-ce8fd2379dac | -11.3686 | -55.1672 | 2025-10-08 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 9968a977-2fd5-3b4c-9c37-a5ebfeebcdc0 | -19.514 | -44.0768 | 2025-10-08 01:30:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 2740bc09-89dc-3c65-a6e5-9731ea45de49 | -7.6474 | -63.4584 | 2025-10-08 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c282e219-6829-3278-b602-0db0e712a7da | -17.2639 | -42.6527 | 2025-10-08 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 84.6 |
| b0a34ef1-9d71-3b88-9140-79d834601c7d | -6.9982 | -42.878 | 2025-10-08 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 4a31a1b6-daa9-326c-a788-47495b64ae7b | -5.1227 | -44.9682 | 2025-10-08 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |


[Clique aqui para ver as próximas entradas](README10.md)
