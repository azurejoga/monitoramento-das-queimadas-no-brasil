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
| dc9cadc2-c205-390b-8ad5-87417a76f18e | -14.29871 | -45.27129 | 2026-08-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16dd1376-5a4c-3a57-9407-cdd372ea0810 | -15.13304 | -41.56638 | 2026-08-14 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 4c9c2b44-dce1-3c17-a1b8-db8265e3ed70 | -15.01091 | -41.94897 | 2026-08-14 03:38:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ae8195a5-648d-3c2e-9b84-e466c24d01b0 | -7.80989 | -44.11758 | 2026-08-14 03:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 419ad036-b93c-3ee7-ba83-03acce3db712 | -13.65209 | -46.25701 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83d56234-49de-32f4-a94b-2addc47d3e8d | -11.32236 | -45.2157 | 2026-08-14 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33943d80-1c5c-367b-98fd-b41d7acc0983 | -12.02291 | -47.81728 | 2026-08-14 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ae93c04-7eb8-3e47-87f9-ede51d8a0e79 | -11.47649 | -44.56276 | 2026-08-14 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7340bb4c-9a72-3823-901d-e13a425a3dce | -12.0285 | -47.82346 | 2026-08-14 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4754ac39-5be1-325b-ac54-4de5086cec11 | -14.24291 | -45.41103 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f43a64ce-3870-3598-bd50-3ea2cc832b3d | -7.45316 | -46.15598 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8f2feea-2670-36bb-b842-fcc46e17f9f1 | -14.29478 | -45.2705 | 2026-08-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3c0b8d7-64da-3552-a60a-b4aac5cb8e8b | -15.14291 | -41.55995 | 2026-08-14 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1b5c91a5-6a60-31d1-bceb-d3f249e97d96 | -11.87935 | -45.9529 | 2026-08-14 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74ac37b9-4d20-3759-ab57-cc1a348ef08d | -13.65297 | -46.25274 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22913904-775d-3385-b2e5-6fd5e1968d76 | -13.86257 | -43.64268 | 2026-08-14 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7401fe7-5cb1-38cd-b0fd-6c2db1a62b59 | -14.46885 | -45.67993 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00e46f3a-382e-3bda-85f4-8890e8d0abe9 | -13.65358 | -46.25423 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c643ea1-a60a-3338-aa40-5079b13b608e | -14.47439 | -45.68106 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23c8753a-01d6-3d13-aed2-0ce39e1f5bd6 | -13.56063 | -46.26312 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a5ee623-0260-3c2e-b25f-8c258f098b6a | -11.48857 | -45.097 | 2026-08-14 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea1ed2f5-0cb0-3ed0-842c-cf5844cad034 | -14.294 | -45.26657 | 2026-08-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b5c2550-4fcd-3254-857c-e276989e5683 | -7.45264 | -46.15444 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35c35fc8-6012-3a95-ad5d-832f88dbf88a | -13.55536 | -46.26574 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c2e8e7ee-10cd-341d-8399-6c4cfd714125 | -12.49266 | -43.77354 | 2026-08-14 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a745eba3-846e-39ed-ac3e-bc102c9385f0 | -11.31588 | -45.21862 | 2026-08-14 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54a9f898-a1b3-32a1-b2ad-e40d6c10441c | -7.71184 | -46.2409 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f4adc280-6772-3ead-95d0-ed0c13ab81ea | -11.48366 | -45.09211 | 2026-08-14 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 174dcd10-bbba-37dc-9b52-5c999b2fae22 | -13.38671 | -42.39499 | 2026-08-14 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| f1ebdc92-2878-3586-8c6b-27cb94476c06 | -12.02184 | -47.82253 | 2026-08-14 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 742e972e-8409-340f-9687-de205e467fb7 | -12.02954 | -47.81836 | 2026-08-14 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae54e28f-b088-3e26-ba26-d09b7486a9aa | -12.49773 | -43.77455 | 2026-08-14 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3e10905a-42a2-336e-86ea-1ac246c7f839 | -13.55809 | -46.25202 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 09112ce3-e521-3ffa-896a-95fe22352e61 | -13.55908 | -46.24705 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f086d345-1992-390c-a7e6-b40f6405d804 | -14.29328 | -45.27023 | 2026-08-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d881b6e-95b8-3913-aab8-a8d7318537fb | -13.55478 | -46.26196 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fa41ae77-3010-39ff-ab0d-e267cea12316 | -14.47763 | -45.69359 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f35e5281-9575-3237-9740-42c0858ec15d | -11.88055 | -45.95938 | 2026-08-14 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce27351c-5336-3ffd-b33e-58e5abae1e3f | -15.00885 | -41.64825 | 2026-08-14 03:38:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d23a657c-3a68-357a-aeb1-9f79df5c58c6 | -14.47362 | -45.68486 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d4380cc-0863-3489-864d-97ee65dfe38a | -7.71297 | -46.23481 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bd7f614b-5ded-3db8-9941-ca82143e846f | -11.31666 | -45.21459 | 2026-08-14 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3035e4e5-9289-3062-9eec-fe9a3e7d0a99 | -14.63155 | -42.52292 | 2026-08-14 03:38:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0294de5d-73cd-3299-8942-01f39fd93da3 | -15.01015 | -41.95314 | 2026-08-14 03:38:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3a4d685c-1da7-3fb0-a3a0-9f1930b3bc14 | -14.44205 | -45.69806 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b21d06f-f14a-312a-9a90-5c04b7624a52 | -11.47717 | -44.55917 | 2026-08-14 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea7f13b3-67c1-3ac2-bc63-44124e690e48 | -7.71313 | -46.2372 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 343af297-8e68-3955-9c0d-e9c014a93d6f | -13.2413 | -54.2683 | 2026-08-14 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 69d9b6f2-f7ed-3a87-995b-488ac7ee6630 | -11.4885 | -54.6273 | 2026-08-14 03:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 71f4b660-1ed6-3017-8f9c-4a22eff92212 | -4.5057 | -42.5325 | 2026-08-14 03:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| d782923d-2b3e-3e88-a3f2-f6ba41fd64b6 | -6.6195 | -59.0416 | 2026-08-14 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 07fe31c3-20e9-3775-a22b-8df1dff5a364 | -13.2221 | -54.2704 | 2026-08-14 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 01c03413-c4b8-3bee-854b-c6a56233362d | -20.96013 | -47.20702 | 2026-08-14 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c39fc285-4fd4-3340-be34-5b1eca11dbde | -20.26254 | -46.70779 | 2026-08-14 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cd6fc7e-9960-30c4-9699-88d8e1bb0af4 | -16.45032 | -43.1446 | 2026-08-14 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce84c870-bb43-315a-b3ad-f828adc70e1d | -18.85902 | -47.06913 | 2026-08-14 03:40:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7e54682-ec8e-351a-91e4-65a18e334a77 | -20.96513 | -47.41545 | 2026-08-14 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ec8ed63-bc3e-3a9a-b931-17f645e1c9c8 | -18.42263 | -45.19714 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b695c32-fc1d-3df3-a2e7-c73380584fb1 | -14.96081 | -46.60091 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5c09343-37d4-3765-a4d9-f5145ee914cb | -21.2238 | -47.13119 | 2026-08-14 03:40:00 | NOAA-21 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45652b94-dea0-3a6b-bde0-75e3f35700cf | -21.78203 | -44.04287 | 2026-08-14 03:40:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3361f6de-2c96-3939-bc33-36e99bfa583d | -20.36183 | -41.49746 | 2026-08-14 03:40:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e7f02f73-cbac-34fc-8406-63faece452c2 | -21.76376 | -44.04337 | 2026-08-14 03:40:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| ebf4076f-b418-3454-9c20-a0843ce89fb7 | -16.54456 | -39.66219 | 2026-08-14 03:40:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fb8c7838-38f3-3df8-836d-d204dce0d8ff | -21.81526 | -42.08191 | 2026-08-14 03:40:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4d917567-fcfa-36e7-ac34-54a9ec78eb13 | -20.26095 | -46.71521 | 2026-08-14 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d8c5419-9280-337b-adf0-22966108c7b1 | -14.94462 | -46.62049 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b56d9786-7c41-303f-ae89-9a14c94084b8 | -15.6325 | -42.39253 | 2026-08-14 03:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d17a084d-7a31-35c4-b85d-179f420c1934 | -18.42582 | -45.20721 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84d30a70-d403-3ac2-aaee-b0bd3061d66c | -20.31436 | -42.23483 | 2026-08-14 03:40:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dde08952-306d-37f1-bb8c-37aac9fd8c55 | -21.74722 | -44.03526 | 2026-08-14 03:40:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 882e8eec-829a-37c1-b357-dc28f996c989 | -16.5416 | -39.66273 | 2026-08-14 03:40:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 331af8ef-d111-36ba-8314-373a1c21fa0b | -21.00224 | -47.27271 | 2026-08-14 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85627e8f-09d8-3134-8375-75ac715e8009 | -21.38877 | -48.63547 | 2026-08-14 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bda7a96-325f-339f-b51b-b70743f627ab | -14.94535 | -46.61697 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b59511ea-95f7-3056-b26f-e71302f1b726 | -20.89631 | -50.5147 | 2026-08-14 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ea80de13-fd32-39d0-8f23-7e9028d912a2 | -21.59944 | -43.70232 | 2026-08-14 03:40:00 | NOAA-21 | BIAS FORTES | MINAS GERAIS | Brasil | 3106804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 976298da-8f78-3a0e-93fc-a843ea08ccd9 | -14.94351 | -46.62583 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1aebb20-7ae7-3338-884a-d2555bbf82f7 | -20.3931 | -41.63047 | 2026-08-14 03:40:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 25377109-5a4c-3717-922c-94af26883402 | -14.9528 | -46.61032 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 570882ca-1edc-3b06-bdd2-94b0f444b147 | -18.49393 | -43.39782 | 2026-08-14 03:40:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c0a3f82d-ee62-3e20-8b9f-dcf22758ef7f | -19.04368 | -40.40417 | 2026-08-14 03:40:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00b1400f-4b24-34b7-9370-6a0770d387df | -16.72122 | -46.4018 | 2026-08-14 03:40:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98063539-7c21-374a-991f-b71470ca3eca | -14.95204 | -46.61398 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c42537d-fb60-311e-9f5e-2fad23f88827 | -21.75249 | -44.03167 | 2026-08-14 03:40:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 3f3eadac-cf65-3c7e-bd66-fbd24a050522 | -22.00953 | -47.21579 | 2026-08-14 03:40:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 960100c8-f8ea-352f-a4f9-b4e9da7dadde | -20.89769 | -50.509 | 2026-08-14 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f7e5285a-29fd-360f-914e-71ac9f88fe0b | -14.73124 | -47.15441 | 2026-08-14 03:40:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa21729a-a65f-31aa-a60d-55891c6255a1 | -18.41398 | -45.18845 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0da7606b-eb65-3ec3-a619-d6a2ace60bab | -18.41832 | -45.19272 | 2026-08-14 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4b9c722-32ef-374f-87c1-8b34bd461f52 | -21.77677 | -44.04649 | 2026-08-14 03:40:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2211db50-9896-3b23-a5f6-5dd9d94bbcab | -18.16458 | -43.98272 | 2026-08-14 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad614f71-4214-3ed3-9d52-e6c3bf259100 | -20.43245 | -41.89988 | 2026-08-14 03:40:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9b03fe82-e399-3fd1-b34d-81932d684db9 | -21.00136 | -47.27671 | 2026-08-14 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76bf855c-9ecf-3af6-a46c-58111bcf2877 | -16.45049 | -43.14717 | 2026-08-14 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b44f020d-78c3-30c9-be62-62531d52be3a | -20.2663 | -46.71616 | 2026-08-14 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f859cb4f-0cae-3775-9302-6aaec7122256 | -18.49309 | -43.40213 | 2026-08-14 03:40:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b3414fd-442f-3dc6-badb-7ea5b7c34fff | -17.5801 | -46.40176 | 2026-08-14 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c52c7b63-5f5a-3a55-a532-ec0d3f2911da | -14.94219 | -46.63222 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91df7179-3360-3102-b9ae-c3bb5276b6b4 | -14.96006 | -46.60455 | 2026-08-14 03:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
