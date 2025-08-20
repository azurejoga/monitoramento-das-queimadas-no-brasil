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
| c570e684-a547-3a5e-96b8-b12733e698ea | -6.06978 | -44.40409 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13cf5aaa-e7ed-3900-836b-04ec370cce4b | -5.99999 | -42.84863 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5c7cec7f-3d11-324c-9a7f-ba7b48107247 | -3.97581 | -42.5043 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f4e8d4b5-7b84-35f0-8250-c7944a9ca060 | -9.92518 | -49.28157 | 2025-08-20 04:08:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2150d5ef-2795-3789-8947-9b7494dcdeda | -8.09919 | -42.35386 | 2025-08-20 04:08:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2297b284-7749-3ca8-a6ca-6f482391858a | -6.35883 | -43.32964 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b60ba07a-c885-345e-8516-9a55e972150c | -4.91607 | -43.23872 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2d14c1c-a478-36c7-9840-3bc35aef9f44 | -9.29584 | -40.2395 | 2025-08-20 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd10fbb4-645f-3f54-8b5b-0d00d2d93783 | -4.39212 | -47.76744 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f822ad26-4a6f-3484-a4a3-cb99d854ccf1 | -8.02903 | -47.66532 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fadd72a3-a247-3771-ba6b-33c5ceb64b8d | -8.01935 | -47.6717 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe5e3766-8713-358c-ad6b-7a1dbc32ad89 | -6.73751 | -41.53492 | 2025-08-20 04:08:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff90b628-5336-3fa3-8455-851a3fc0829f | -6.56425 | -43.00424 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6c4914d-0bfb-306f-b8c7-66c0913c2a6c | -6.39473 | -44.25906 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a660826-b420-3a95-b5c5-410d34b84f0b | -6.46601 | -53.37663 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05d7c51d-ec9a-3d21-9c88-2612e523a244 | -6.17412 | -46.14738 | 2025-08-20 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0aee7f33-0ba3-3e0c-a044-53e3a65b7883 | -6.94528 | -42.8719 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a1b8de76-e310-3aca-9379-0af4066564bf | -6.00062 | -42.82306 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb0f6b88-0f31-3c4f-80ca-b76a8dc8bfc7 | -2.90831 | -48.29918 | 2025-08-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12792a04-011f-3eec-a802-0fab08bb98ff | -8.3029 | -46.35276 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52412b37-726f-3b93-bd5c-25b03d5df62b | -7.63701 | -45.26671 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5d2757c-18b0-355d-a084-b943913a183c | -6.85672 | -43.61956 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9246ec13-d2bc-3e67-9ba1-2895938d0550 | -6.86768 | -43.59479 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6be1a78a-717e-3715-9d9d-836d2b7dd08d | -3.98141 | -42.51247 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 65cbc240-3f06-3906-b103-e03f5e1a06a9 | -6.51913 | -45.46299 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86c55e93-8ec0-3fd7-9cf0-0b8a1e171f24 | -7.63307 | -45.26316 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86cafa3a-b357-3f64-9044-f6682d56d53d | -5.63614 | -43.38921 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee40b1e1-42dd-30c4-b4af-7dffa96054bf | -3.97525 | -42.50787 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1a1878cb-b7b3-3a40-94f4-90481da2c2cb | -7.22859 | -44.70941 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85c4a1da-2357-3a14-8f60-28fa2c26cc36 | -6.86309 | -43.60162 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17acbb30-240c-3b48-90ec-207a3ac0580f | -6.31943 | -43.75148 | 2025-08-20 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 46905ef5-686b-3f54-8f66-684e277767f4 | -2.9073 | -48.29694 | 2025-08-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e341e0c6-b505-3c51-b3df-8cb070c0bff2 | -6.01067 | -42.82466 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 111e4f7d-6858-32c0-b584-d17a7f230d4a | -7.64876 | -45.28575 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66714962-fc68-388f-9a19-7988475a81d6 | -3.83407 | -47.73666 | 2025-08-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff187472-b3e0-36f9-a51f-0ba46c735eb8 | -2.91779 | -48.30061 | 2025-08-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c51dbce6-7fc0-3775-8142-5938e95b7d46 | -5.63975 | -37.90919 | 2025-08-20 04:08:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7937c726-6d07-3143-9b64-273380770af2 | -5.98165 | -44.1432 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2c6feb49-31ac-3d13-bbfe-9b53abd07c1d | -5.63721 | -43.40456 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ab65405-1802-3b3e-be1e-edded426e748 | -9.69368 | -39.5276 | 2025-08-20 04:08:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce08fdf6-dc7d-3348-b80f-676d0ba7664d | -7.03335 | -44.59342 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8e9102b-af2b-3f70-9972-9f710fc92d41 | -5.4058 | -45.18729 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e63d9c2b-bc34-385c-a456-8dafc20a771b | -8.07153 | -43.66547 | 2025-08-20 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c387b501-034c-3f9e-ac51-7c31c26e7d0a | -6.39824 | -44.25958 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f138a56-7643-33a3-b33a-7e9e2782bf86 | -9.87353 | -45.97581 | 2025-08-20 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e9c790e-283b-36b6-8ee6-b646eb53c6d0 | -7.23053 | -44.69746 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06c4796d-a033-34d0-9f63-eb95922d4740 | -8.78817 | -45.48244 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 899a367b-afda-36bc-bb7f-2d40d325be8c | -6.42782 | -41.86064 | 2025-08-20 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a745560d-4052-3ec6-af3e-35450a088aa0 | -6.72775 | -43.98724 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e006ea8-726d-3f7b-8f06-f7c61d3256c9 | -9.99136 | -48.56787 | 2025-08-20 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f2a0555-2383-32c8-8ac5-dcd682c6bdb3 | -6.56704 | -43.00834 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 249a36cb-b608-346e-846f-76f290d78982 | -7.30357 | -43.70144 | 2025-08-20 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eeb09c63-77fe-387f-bbda-12cd92de0cdf | -3.98421 | -42.51656 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 52f34adb-b790-344a-aa89-8b71e08d49da | -5.98451 | -44.14771 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c2373e6-7b35-3a81-9e51-da9153bb3bc6 | -7.65588 | -45.26522 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c15ec35c-3489-3184-a6ca-0ae355264262 | -5.11246 | -43.21634 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5f3f7a1-5ead-3021-bf89-070f0893feed | -8.29143 | -46.35091 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e823845c-b2bb-33a6-acd1-fb6e3b569a93 | -5.38464 | -41.22562 | 2025-08-20 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 06de3a5f-7d4a-3185-b73f-21d38c234b0f | -6.03217 | -44.38973 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ac2aff9-2102-30b7-936a-de05d5ed47fd | -5.65631 | -43.50616 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62e38d74-8553-3259-8c4e-1bab8ded66f7 | -3.36013 | -43.35683 | 2025-08-20 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2169b11-b4df-3262-bdf7-9deb505dea38 | -6.02863 | -44.38919 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db79e9ff-e9cc-3a48-84ab-4e144990a52b | -3.23141 | -46.79702 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 7104f0e4-d53f-3bb7-a64a-48c76a47abfb | -7.22343 | -44.69638 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2869ac09-9274-3c45-92a1-79cbfae0f457 | -7.21357 | -43.97718 | 2025-08-20 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 886dc026-686a-3854-a4ce-11f1a29d131c | -6.00397 | -42.8236 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c9a83ceb-e7f4-3c3a-95cf-2ae5c3cf411c | -5.64014 | -43.38603 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a67b8078-255c-39e0-82cd-c3043687a744 | -10.82084 | -43.27998 | 2025-08-20 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| e49aa8c5-742f-362f-a9d4-551a914d2b3d | -5.63272 | -43.38869 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3640d7b3-a36a-3588-b414-c9f0cdcc03ce | -7.6377 | -45.26255 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d6633c8-63d8-37df-a2a8-4cddfc41b709 | -6.54355 | -43.00465 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d64db09-2d35-3388-8470-cdd2f54c2b2d | -4.87591 | -42.71128 | 2025-08-20 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b0cd35b-8991-3169-8456-fca3ca54bedb | -7.63217 | -46.22467 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6d2cf1e-70f6-32ea-aee5-cbd584c28740 | -9.27038 | -44.53401 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e553bd3-73e2-3b59-b934-0325f2956184 | -8.79547 | -45.47564 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c7354bf9-8149-3cea-8754-80d8299dfeca | -4.95787 | -43.08706 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 617b2576-17c2-3a57-8dc4-f45ecc0ae818 | -5.48611 | -42.1618 | 2025-08-20 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b8fcd4aa-3591-326c-9919-d68fed71b2fe | -6.00726 | -42.84616 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f117cda-5b4b-3dc5-9878-b38d5dfa8c94 | -6.39832 | -42.50338 | 2025-08-20 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c09e9bb-389a-3f88-aa69-da9efb696298 | -6.12946 | -42.95694 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 78a7fd2d-474c-38ea-a9a7-9619d4fcd62e | -6.23062 | -45.27984 | 2025-08-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15c0a6d7-c80f-36fb-b7d9-903b7c44f830 | -6.03911 | -44.34679 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 892ad600-714a-3a9f-b28e-b38cb421b845 | -10.46327 | -40.54044 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 47142035-0af6-32c5-a7f1-18c367928a95 | -4.01648 | -48.06244 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f75609e8-12bc-3312-a159-7ead0e921b25 | -8.02001 | -47.66785 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d6dbd0b7-4aea-347e-a280-93ff0c7615bb | -8.14146 | -49.51553 | 2025-08-20 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3be2a5db-1806-3eb2-8b30-1f38483e24ef | -5.66414 | -43.37046 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b58b6e1f-b81e-34e1-b572-e3dd496f3172 | -6.08684 | -44.4109 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5273292-b2a7-3f40-b369-8392cc0bfbae | -3.05239 | -47.01703 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbf5f0e5-5b55-338a-9540-285b57fec1a8 | -8.32383 | -47.63704 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2289dec-b5b0-3e5c-b2e6-cac2a8f9da64 | -3.81791 | -41.56456 | 2025-08-20 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7d8f410d-22a5-3828-9df8-b216c8592d0a | -9.5325 | -45.18139 | 2025-08-20 04:08:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a3eb081-0936-3f22-87b7-a9aba22daef0 | -6.55083 | -43.00213 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 357b48c4-3b95-335f-836e-93981653057b | -4.01711 | -48.0613 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 359b18b7-a41b-380f-bc88-6daae95532fe | -7.63407 | -45.262 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8ad1939-56d0-327f-ba67-729d6edfc7c6 | -6.26312 | -52.826 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0e7d917-6be1-37dc-a2e3-de3f6fb6920e | -5.69074 | -43.66531 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a83e439f-8a2c-3f1f-a460-05d1cd3157d6 | -8.29907 | -46.35214 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2eb517a4-01f4-37d0-972e-633111a8a7a0 | -7.58809 | -44.39671 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80caa13f-c3ca-3eec-80f6-f384dc2c5c1b | -3.53538 | -53.56134 | 2025-08-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README14.md)
