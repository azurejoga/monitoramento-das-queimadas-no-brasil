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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2832b1b6-b594-3214-8f91-f43434ace7e3 | -6.17831 | -48.05867 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a0f875e3-97b0-303e-97a8-0ee06dbdd4c9 | -7.01877 | -44.56849 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f78d597d-2baf-3bd5-8a17-2193422205a4 | -5.75918 | -43.39988 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fdeefe6-e5c4-30e1-bda8-c93a020fcd12 | -7.01816 | -44.57193 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8d3f81d-3630-3bd3-8a25-621879388825 | -4.74218 | -43.26535 | 2025-06-25 03:45:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b59beea-c0b3-3529-afd4-c760ead35720 | -6.185 | -48.06017 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 72b73725-7aa2-36cb-8b07-ecf1006d662c | -7.03414 | -44.5754 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74e729f1-addd-3d08-b4bf-eee61ef86937 | -7.00973 | -44.55716 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7201a0f6-b04f-3008-bbe2-f0b082571d04 | -4.01001 | -43.23911 | 2025-06-25 03:45:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83027d2c-3899-3d51-b017-ea5173ff0acd | -8.06741 | -43.11362 | 2025-06-25 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a8e70d8c-0cf7-3c59-9860-63ff9763da81 | -7.2092 | -43.09769 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7889e481-b7be-3887-9935-c1210b12e42f | -6.29759 | -44.23941 | 2025-06-25 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18cad67e-ff5f-318f-ba58-01b9838feb59 | -6.17482 | -48.07703 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 55fd1017-02d5-3155-9855-69504458d734 | -6.17725 | -48.06422 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 02b9ac45-6b55-3079-99fe-5b5167be79b3 | -7.19628 | -43.10179 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 37a113d3-0efb-353e-9949-52993e8e4402 | -7.20436 | -43.09685 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| fd2fee41-afd8-3ff5-9372-a3e128776193 | -6.17937 | -48.07974 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 97539af6-eec8-3fa6-832f-1816733165da | -4.22626 | -43.64211 | 2025-06-25 03:45:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b866082-6857-3583-894f-ddc2d5964d77 | -6.92579 | -36.45607 | 2025-06-25 03:45:00 | NPP-375D | SÃO VICENTE DO SERIDÓ | PARAÍBA | Brasil | 2515401 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2565f666-7044-3b54-8463-9fddf01beb6b | -5.73507 | -43.49804 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2224cd35-b189-35dd-9854-62fbf422d6be | -7.01937 | -44.56507 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b32ad94f-28ff-3024-90f2-02787f6392d9 | -7.00486 | -44.55352 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 007946d0-f6d4-38e0-ae50-4473e6a30299 | -7.01514 | -44.55782 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0b832beb-2f3b-3bbd-8f51-f2a36f58615c | -7.01391 | -44.56477 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 11d7230d-c7f4-3224-8b9c-f8258981f63d | -9.551 | -40.34704 | 2025-06-25 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 365ffbe6-5398-365f-a902-cc55549fc43a | -5.73454 | -43.50102 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd8b5618-5c6a-3d18-9a1d-9bd9783e0cf6 | -5.73243 | -43.49633 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8253ef7c-f967-3948-9a20-c5f69ecd76a3 | -5.36037 | -45.12088 | 2025-06-25 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c3dc9b-9ab1-3cc0-9e3c-57c59d504ebb | -5.75238 | -43.40023 | 2025-06-25 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc35db32-3629-3df6-8001-323bf7f75afb | -7.01453 | -44.56124 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0120ae8f-25a2-3758-b449-640c6ffc74fa | -6.22446 | -43.37152 | 2025-06-25 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9becc750-98bb-3b44-897d-a300831975a5 | -3.61671 | -47.53177 | 2025-06-25 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8df3e8cb-841b-301f-88bc-6123e04a207a | -8.0676 | -43.11634 | 2025-06-25 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 511dd083-83be-3c8a-9544-25d87c1131eb | -6.22646 | -43.36006 | 2025-06-25 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41094771-4437-3cb9-865b-d016fa6c55cf | -7.00544 | -44.55022 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0cff01a-a9b8-3947-abc9-f58f521b9ec9 | -6.18284 | -48.07158 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c03fe669-d4b8-3ffb-b1fe-986c9901cea2 | -6.18396 | -48.06569 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7be4063e-8d6d-32ef-becb-698da5760425 | -6.17493 | -48.0658 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2bf4e1c3-a6f5-333e-a0a8-2561e29299ad | -6.9094 | -43.96892 | 2025-06-25 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8c0eac9c-183d-33c5-a812-46f924fe5d8e | -8.53112 | -46.32883 | 2025-06-25 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d02d0dd2-b159-3846-924f-269cb68642d0 | -4.18773 | -38.36528 | 2025-06-25 03:45:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 005f4669-7382-31c7-882d-ab93d8c2e075 | -9.51399 | -45.4449 | 2025-06-25 03:45:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d92fd74-55f0-36a5-bffa-a6c4b8b9cc56 | -4.52765 | -48.01315 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bb48edc6-d142-30c0-a446-16905a104b45 | -7.43827 | -48.10313 | 2025-06-25 03:45:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bbb9c3b-daf0-36c1-9018-03809471f35e | -7.19376 | -43.10052 | 2025-06-25 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1ae7d000-9069-3369-8269-413be3744ead | -3.62159 | -47.54044 | 2025-06-25 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99defd12-5e9c-3bc1-bc34-69491fbfc7e3 | -4.53467 | -48.01369 | 2025-06-25 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 989dfc2a-3036-342d-8682-6dfba9d1ad08 | -6.18056 | -48.07324 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 824b39fa-58f8-3cfe-9ffe-fac8abe29dd3 | -8.05881 | -43.10675 | 2025-06-25 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 691afb15-e0c2-33ee-9432-c770fc4d2c74 | -7.02951 | -44.57026 | 2025-06-25 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07115c75-c547-37d0-999c-c87ff0cf7657 | -6.0249 | -35.4889 | 2025-06-25 03:45:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5ffeda60-3d47-3093-bc1e-abb04f7ed705 | -6.18161 | -48.07809 | 2025-06-25 03:45:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 83df2650-32cf-3dff-90ab-1fa3ee456fa6 | -11.10847 | -44.52266 | 2025-06-25 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d3756d4-dbca-3a50-99cb-fef4ccc0f14c | -12.79752 | -48.73649 | 2025-06-25 03:47:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eeb6ad68-6b91-3176-90a8-5d9c1452fc06 | -14.34655 | -40.90635 | 2025-06-25 03:47:00 | NPP-375D | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ba7989ab-c773-3d67-8d4d-279d5b763aaf | -14.13185 | -47.94905 | 2025-06-25 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2617b48e-6521-3449-966a-4f6162100108 | -11.18322 | -48.62315 | 2025-06-25 03:47:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d10aaf9-2642-3f9f-bf0b-0d28c6f26633 | -17.08116 | -45.95164 | 2025-06-25 03:47:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f019d287-bb3c-3a6e-9ad0-69fc0c1aac91 | -11.61255 | -46.50485 | 2025-06-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb409970-5b56-3ed8-8b11-d7ec760dd88e | -21.20004 | -48.51692 | 2025-06-25 03:47:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2efa0aa-aec8-33f8-9cc0-8aca7f3fec15 | -10.94833 | -47.39254 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04d9ce77-fd71-35a3-a5c3-f348e4deb85b | -20.92304 | -49.09829 | 2025-06-25 03:47:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ca2fb85c-7b77-376a-ad43-162caffe2445 | -13.03766 | -48.83566 | 2025-06-25 03:47:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b309eb12-edf8-3462-904f-ce9a4419569f | -11.09646 | -46.64265 | 2025-06-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6206aade-721d-336d-98bc-e6eaf11537d1 | -11.58115 | -44.63551 | 2025-06-25 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efc434b1-fdde-3aa4-bf0b-83c5618ed074 | -14.38437 | -50.33562 | 2025-06-25 03:47:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d79b9c8-da22-31aa-915e-71c22a517d08 | -21.20451 | -48.52191 | 2025-06-25 03:47:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b13e1105-469f-38a6-8352-2b684d627ea4 | -12.80491 | -48.73257 | 2025-06-25 03:47:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2601b7b7-4bd4-359e-9128-af97044fca92 | -11.56782 | -47.42767 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43bee1c4-89c1-3121-b173-c0c565c77d5c | -17.11118 | -41.57516 | 2025-06-25 03:47:00 | NPP-375D | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c5aba50d-e2f0-3e1e-9bc8-bf89679e3573 | -9.56923 | -49.1048 | 2025-06-25 03:47:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 490612f7-af53-31bf-9bd8-fd33a11391c2 | -14.13272 | -47.94477 | 2025-06-25 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4b55efd-2355-375c-81ed-e3e90136b838 | -11.57897 | -44.64696 | 2025-06-25 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79bfa61c-aae5-3e1d-9e7e-42354a5241a7 | -13.03875 | -48.83039 | 2025-06-25 03:47:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9789d5f4-464d-30c7-9b87-e761615495a9 | -14.15697 | -50.42873 | 2025-06-25 03:47:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27526c49-e677-3eae-9766-342d9c1b1833 | -14.80833 | -48.29869 | 2025-06-25 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49065569-4641-3795-8c4a-0ae6a9fe9654 | -11.58611 | -44.63647 | 2025-06-25 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f9c5fa1-5355-3e68-88db-30a3c246fea8 | -23.40551 | -46.55645 | 2025-06-25 03:47:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de56dac1-fc9d-381e-8519-7c03c5ff18bb | -20.92704 | -49.09763 | 2025-06-25 03:47:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5160e1b2-e895-35b7-bc02-9cc252322ed9 | -9.56798 | -49.11105 | 2025-06-25 03:47:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0486e053-f3a0-3f86-88c3-65d2d2946e30 | -11.12185 | -46.96967 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8d186f-8269-3f87-8757-3c66f326a95a | -11.12218 | -46.97337 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d00ea58-e5c1-3764-acb4-0e8bcd87ce08 | -17.14063 | -44.79336 | 2025-06-25 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bbbd847-3896-3213-bf58-7f9925f90def | -17.14437 | -44.72477 | 2025-06-25 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e0434ee-6da1-35ab-b706-9945f8c5c4ba | -20.92391 | -49.09433 | 2025-06-25 03:47:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5988cc0b-0ec8-398c-9b45-e6135a1dffd8 | -21.20527 | -48.51846 | 2025-06-25 03:47:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce097517-21df-3b77-b451-4d4e796661c6 | -11.08974 | -46.64344 | 2025-06-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7b58d55-588f-3688-ac4d-3cc9a7a2ad69 | -15.62321 | -42.54306 | 2025-06-25 03:47:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d73f694f-37fd-3aad-987c-6a00d9230646 | -11.09073 | -46.64167 | 2025-06-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cccd997d-484f-3c02-a12f-3d3c91735183 | -11.61406 | -46.49699 | 2025-06-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f31fe65d-bb39-3c1b-b005-31aafa3267c2 | -21.28797 | -48.55951 | 2025-06-25 03:47:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3c7d31f-e89a-3345-ab47-7109caf16ba2 | -11.11089 | -46.90644 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 188a83ad-cfae-3025-a742-df3ea5dcdfc4 | -13.6448 | -43.79816 | 2025-06-25 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4c895b8-7ea2-34b8-88de-c568282a28fb | -11.57375 | -47.42891 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48f036f1-a5ed-3615-9c0f-b5315ea82a8f | -11.57707 | -47.43272 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7155581-5232-3aad-abba-ef7eacb0a860 | -14.71599 | -48.41369 | 2025-06-25 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8daf127-3b6a-3799-aae4-4d548e7777df | -11.58038 | -44.63857 | 2025-06-25 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cde0fd0-03b1-3eb5-b3ad-1d0b52b3797c | -21.57817 | -45.31085 | 2025-06-25 03:47:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 68cd18e5-a981-30eb-a612-39aa45cd7645 | -14.7195 | -48.41663 | 2025-06-25 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42699a50-d47a-3096-8076-b9160ec5e25a | -10.45312 | -47.95176 | 2025-06-25 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README7.md)
