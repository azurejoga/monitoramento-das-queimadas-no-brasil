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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 401aaf5d-89e4-37bb-bbce-8108081d6727 | -10.34995 | -44.0679 | 2025-10-30 03:36:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74ef26e8-0eee-30fb-86ac-1a162d7548ec | -7.95596 | -45.44367 | 2025-10-30 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d9fc7511-9512-3ee6-b5ca-e7a1dc655227 | -6.13769 | -41.5697 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6e02439d-6719-3bef-b522-5446a4300794 | -6.92107 | -42.24995 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 24e07e04-f711-30b8-a952-b62ff1c3b318 | -6.88702 | -45.55518 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 265f3d41-22d2-3514-8120-04abfc6da364 | -10.74992 | -44.7455 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db4e93ad-7c53-333a-b159-5e21211defbb | -10.7436 | -44.74781 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a410dcd-fe52-38bd-b6e5-68136c0ce0f9 | -6.5183 | -46.90161 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 16b6f236-0bce-3233-9a1b-83b62b881716 | -10.8579 | -47.86929 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3088d255-ee19-3c12-96c0-d8c0c69798f2 | -7.61493 | -43.59325 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 165a466c-dce3-37de-a15b-b3d9c8a000a7 | -6.1416 | -41.69505 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e2cb7ef7-ee41-37c0-95e1-89551870a092 | -7.86744 | -44.23987 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2514bab5-b348-3590-a6bc-b8543dd5119a | -6.14391 | -41.71154 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58371bc7-f2a7-301d-ba94-0361b109c129 | -9.89012 | -47.45069 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 57c4f912-0bc6-33ad-8d26-234e701329d9 | -9.89946 | -44.88641 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d82eea8-e5fb-32bb-a42d-37738041358d | -8.3244 | -47.92302 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| eaa1fcf4-3067-3028-8573-153257d47da9 | -6.63552 | -44.60347 | 2025-10-30 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fb5040c-cb26-3659-a99c-6b5fa18da5f5 | -11.55362 | -44.68827 | 2025-10-30 03:36:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61697b26-fe9d-35e7-94ff-6ec136d4336f | -6.85189 | -46.29518 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8fd0e1c-f5e7-3998-8cdf-83add431add1 | -6.12593 | -42.4384 | 2025-10-30 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 23160e7b-49ca-3177-8823-173688d10745 | -8.02776 | -42.51357 | 2025-10-30 03:36:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f84cf27e-8723-3fcd-887b-76584a8837e0 | -8.6987 | -47.91262 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ff02891-e2a2-3cd3-8ec7-104557393c07 | -7.28879 | -45.6693 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb1c0e40-c6a0-3598-96af-923bf5879daf | -7.30298 | -38.92711 | 2025-10-30 03:36:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4567f8ad-6838-3ba9-a038-6323325b9f91 | -11.96046 | -43.28602 | 2025-10-30 03:36:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94013c28-9bd3-3a53-9651-c108debd2c8c | -7.95898 | -46.74812 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a3923f2e-18d2-3a7b-b296-a2ee68fb6acb | -6.47863 | -46.88701 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 449d9ed7-e41d-39b8-9f15-4ca319d315e4 | -8.32302 | -47.93003 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 729f2c66-188c-3ec7-ae58-59d3fc8d42b1 | -10.85589 | -47.87379 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ea88a36c-34b5-3c2e-8ee9-60d65be69457 | -7.79272 | -46.42001 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cf201b5d-a31e-34ea-9b3b-70d51920eb10 | -11.18159 | -45.21278 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 378c7666-9439-3e45-8559-90e75d213299 | -7.54339 | -44.04731 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e8adca3-db91-3405-9498-d685a9c5ce22 | -9.05106 | -47.81728 | 2025-10-30 03:36:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 521944a7-96ec-3c5b-811c-75aa5d58041e | -5.84472 | -45.54202 | 2025-10-30 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3c51e048-dfd6-3b9f-9bde-019606b08848 | -10.8626 | -47.87569 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cf5edd9-f497-3810-876e-157147140aae | -7.95338 | -46.74109 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e2c51031-e159-3a10-a8ae-ea6af94bc048 | -9.84856 | -47.69091 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c006c3f6-c3c8-3f5d-9fae-61778b4b27c4 | -7.91846 | -39.71697 | 2025-10-30 03:36:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 601c1307-bb89-3779-8b62-999dc5779ad0 | -6.0159 | -41.979 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8fa2ab5d-7af5-3c63-a1fd-6cdc1969e260 | -6.02154 | -41.97684 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 731f4492-be04-3f52-993a-4d2d902f60d5 | -9.84478 | -44.88978 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc42ea69-39c9-3b89-959a-c0025eef0cb6 | -11.09983 | -44.70565 | 2025-10-30 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 145e2972-76ac-3630-b5f9-ee9cb81c146c | -6.10315 | -42.44445 | 2025-10-30 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f09213ff-b0f0-300a-9a83-a45dc94782f0 | -6.92002 | -42.25599 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2f7bb23e-c071-3d8b-9a3d-4dc293b35b08 | -10.74429 | -44.74426 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb4be118-0460-3e19-920e-bf42150e0690 | -6.46426 | -41.64714 | 2025-10-30 03:36:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a0f3964-ebb4-3fc2-9388-4ebcf3e0f843 | -6.0205 | -41.98295 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 36d3db0b-f2d1-3905-9e19-039ec523ee1f | -6.13898 | -41.71017 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a21b2e41-583f-3a1c-85ff-da3c6d7a9d1f | -7.34463 | -39.32985 | 2025-10-30 03:36:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4778e2a5-b8d8-395a-907a-bee61c960fd6 | -9.88462 | -47.44319 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fedd303b-15b7-3e6c-beba-a27633a7aaab | -6.13717 | -41.69082 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ead2134-8686-3107-a93d-2c6b603bcccd | -7.16719 | -38.53253 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b99edac4-fa8f-3cee-bad1-d84860041927 | -6.13872 | -41.56383 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51195d5e-9b52-312a-b5a9-2c92cca7c1e7 | -6.02658 | -44.32994 | 2025-10-30 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8e9f98e-d0f9-384d-94e8-75134bb05d45 | -10.27516 | -44.5831 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d83518b-44aa-321f-82c3-d20b31a233cd | -10.3578 | -47.27972 | 2025-10-30 03:36:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f62af55-2575-36b6-a15b-a0253059f5f7 | -9.9788 | -37.0424 | 2025-10-30 03:36:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05c5a0ad-99ca-34bc-9f7a-af22eb9c579e | -10.43394 | -40.50613 | 2025-10-30 03:36:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3a581124-9458-353e-bb3b-21ab40e03a48 | -6.85293 | -46.28959 | 2025-10-30 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b9c21839-7daf-31ca-a828-e0a0e8e620c3 | -10.48974 | -43.32636 | 2025-10-30 03:36:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0b14cd4-3e18-3ffc-9e31-61bcae876e37 | -6.21157 | -41.82532 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d5d018fc-bd8e-3519-9e2d-48a019401009 | -7.29615 | -45.66499 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5dec005e-6553-3a42-9655-56f6422e665a | -10.3523 | -47.27259 | 2025-10-30 03:36:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d11a30d-accb-3c83-a73c-2f07d783fad3 | -6.85853 | -46.2964 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d830967-3149-3341-8f6f-cf64f6386867 | -11.55845 | -44.69314 | 2025-10-30 03:36:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d6feb2e-0430-32bc-ae5a-5bc3e46089f5 | -7.3832 | -42.45511 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41e3d916-322f-353a-86e7-fa094d271f86 | -7.96357 | -46.72384 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0bec08cd-0c63-331d-955f-9823bef13e87 | -7.50807 | -44.07186 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffa3343f-d655-33c5-a1d2-fdf7c021d96a | -7.00152 | -42.28673 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee6fd393-2106-3815-b9a5-4812f9dfa401 | -10.34928 | -44.07143 | 2025-10-30 03:36:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93fe7e3d-7f23-3177-a182-e2bd4750878e | -10.54095 | -45.04685 | 2025-10-30 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41b2f182-4bff-3a93-8a4c-b91fda098ab4 | -6.13415 | -41.58998 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1dd7bacf-b81f-3add-af77-7c94f19e00e2 | -6.13918 | -41.67926 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 657b6b16-e67d-317c-b6c4-adc047d29a91 | -6.6347 | -44.60802 | 2025-10-30 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ea450d3-a97f-3ee1-bf6a-374a6cec45f9 | -7.62339 | -43.60964 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56d6fee8-c0a5-3265-9229-2296a91140ef | -6.14566 | -41.67155 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e598758b-68fc-3c33-91bd-4518a9f2b4b7 | -6.9154 | -42.25215 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 300b6c79-5e3e-3397-8c29-68a5587baeca | -9.88957 | -47.44318 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e7f86cfa-dd6f-3754-9228-69f49e1bc6a7 | -9.31893 | -43.0959 | 2025-10-30 03:36:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ba884dc4-8fc6-3121-bdc0-6f8acc3d5d77 | -6.13951 | -41.70711 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8798af5a-9c88-33c3-ba21-8d025efece1c | -7.32412 | -42.4796 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bde67983-3711-32a6-86fd-45dc1882059f | -6.08437 | -41.78563 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c75bee9d-a870-378c-b5d3-773392255d8f | -6.15352 | -41.59645 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 86e85e9f-5e09-3faf-8ade-ea2192716879 | -10.26398 | -44.58035 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e4e5ec0-c446-362d-84eb-e51b69251a43 | -11.18176 | -45.21206 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 477c2c51-d8de-3d38-ad08-8a9091788a60 | -7.20811 | -35.77842 | 2025-10-30 03:36:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1bf4021-73ea-3865-92f6-e4e7ac9a70dc | -7.33974 | -39.33336 | 2025-10-30 03:36:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca7a05ae-f9f5-3cc0-9689-19d2831a74aa | -11.64338 | -44.04758 | 2025-10-30 03:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88adb1b4-1e23-3019-a061-69f717b4e60d | -8.32254 | -45.37928 | 2025-10-30 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dd9171b8-33ce-3496-bac2-25ab91cdf482 | -10.4959 | -44.13829 | 2025-10-30 03:36:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54c9dd31-3c18-3ff5-895f-865316929bea | -5.4383 | -45.33906 | 2025-10-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 35b899b0-bbf8-34d8-8b88-b19d9fd99a3f | -8.26512 | -43.92876 | 2025-10-30 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bbaf124-7d34-322c-8e3a-620c2bb081b2 | -7.27657 | -46.06262 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf7725a7-1470-3ffd-a76c-edec0ded5df9 | -11.18097 | -45.21606 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c52affd-3388-38c2-99d9-dc3c06812efd | -6.78875 | -39.1493 | 2025-10-30 03:36:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9df45428-7ea8-3f18-9946-69f54d35fd9b | -9.91034 | -47.91529 | 2025-10-30 03:36:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 48eb8b58-e8e6-366c-974e-babdae9932a7 | -6.10581 | -41.72259 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25e25bda-b610-330b-83ae-52cdd33b5949 | -6.91486 | -42.2552 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f78bf046-9e87-3703-93a6-13c7d3d388f4 | -7.16157 | -39.46367 | 2025-10-30 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 075be919-f609-37fa-ae02-e079b9f7a3e4 | -6.17731 | -41.60706 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README14.md)
