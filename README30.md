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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea400536-f790-3986-8779-a3092c606c86 | -23.23588 | -46.77765 | 2025-08-24 03:47:00 | NOAA-20 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 61007dab-cc92-39aa-9ae1-0fc71e0d8015 | -18.03485 | -50.62148 | 2025-08-24 03:47:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b956b920-dd84-3108-8eca-0d3de714bf7b | -22.14007 | -43.652 | 2025-08-24 03:47:00 | NOAA-20 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 0149cd5f-d2d2-3702-a350-cfa3ff3d9594 | -20.36803 | -46.7633 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 853115e0-1889-3556-83c4-e5d2292be6b4 | -22.94877 | -45.13473 | 2025-08-24 03:47:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a96b69b1-d26b-3248-80de-ad60dc7a1557 | -21.41313 | -47.61276 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a458381-d05c-36d4-b7fa-340a80d163d6 | -19.92623 | -44.21344 | 2025-08-24 03:47:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34c29b60-78f6-3b5c-a065-294ca298d001 | -21.94892 | -45.58836 | 2025-08-24 03:47:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 53bbc37c-0570-319c-813a-0bbeee785100 | -21.27254 | -43.75236 | 2025-08-24 03:47:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e1751ce7-992f-3a77-92d9-7e6fb0fb6aef | -23.47206 | -46.80843 | 2025-08-24 03:47:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 72b719ab-8091-3d21-a433-b87ba925c151 | -19.6795 | -43.88046 | 2025-08-24 03:47:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a2a8ea0-2e4c-3944-99cc-8eb423d4c0b3 | -23.65542 | -46.29468 | 2025-08-24 03:47:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 54e930a1-c823-34ef-829c-a91d0b980056 | -23.13129 | -47.03217 | 2025-08-24 03:47:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b50af2f2-13e2-39e1-a17e-baa572a25d9a | -20.28682 | -50.89875 | 2025-08-24 03:47:00 | NOAA-20 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e7ef6182-1a2a-3618-a0dc-b7ce7c8b000b | -23.62426 | -46.02297 | 2025-08-24 03:47:00 | NOAA-20 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f329cd1e-068b-3fa8-b5cf-ef1884299b72 | -20.94036 | -46.82272 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cab03b21-c70c-3bd6-a019-783b15ec8e69 | -20.35759 | -46.74057 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37025ed6-0893-3449-93f0-b174db1ed0c1 | -19.83459 | -47.53453 | 2025-08-24 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afb6e63a-161f-31d9-8f79-99f564b324e7 | -20.80289 | -50.13057 | 2025-08-24 03:47:00 | NOAA-20 | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 73853247-fc6b-3fa7-b34d-265a91c2e1ef | -20.34405 | -51.69479 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d582b02e-f3c8-37ab-8f95-335dc0a5b5e5 | -23.35411 | -45.80323 | 2025-08-24 03:47:00 | NOAA-20 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| db72a89a-8d72-377e-bfb1-1b29e0520b94 | -20.35284 | -46.73927 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 259e755e-ec1d-3379-921d-8071e78f10a2 | -20.11842 | -45.36421 | 2025-08-24 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 64352441-b8a8-34ac-a183-d7029c33613a | -21.38967 | -43.8766 | 2025-08-24 03:47:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 47af72a9-20d6-3789-a146-f3a12784e8e6 | -19.62737 | -43.19043 | 2025-08-24 03:47:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 786d3b0e-90b6-3d30-b373-b7f77ada1f4b | -23.49429 | -47.07212 | 2025-08-24 03:47:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ae5c215a-58e7-3077-910e-6c85cc8e0c6f | -21.29088 | -43.85201 | 2025-08-24 03:47:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4382eb22-42b5-31bd-9249-1d32ee2b0da4 | -20.35172 | -51.69116 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 60cd3edd-2618-36a4-894b-1bd94c206855 | -20.35676 | -51.6968 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 354100e9-7d0d-30d5-95a3-a6e1982e1fd5 | -19.7282 | -47.9839 | 2025-08-24 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2eb4509c-ebf3-305e-98e4-ee22b12180b1 | -18.03726 | -50.6175 | 2025-08-24 03:47:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9588b721-e5ad-3b40-b91e-0003cee00038 | -21.78166 | -42.08479 | 2025-08-24 03:47:00 | NOAA-20 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8b19e5a5-f5ed-3eb1-96f3-593a1bd62d76 | -19.86303 | -42.13161 | 2025-08-24 03:47:00 | NOAA-20 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 271c5e43-5121-3cdb-9422-b11ccf7df4ce | -19.67958 | -43.92461 | 2025-08-24 03:47:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 88ab9b3b-0e46-3d66-9607-c4ac3b4e319b | -21.41275 | -47.6143 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e888793-12c2-3e62-8d4f-326238f943ba | -21.54753 | -44.16979 | 2025-08-24 03:47:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1eac6c56-9a6b-3f86-a1cd-999a10645735 | -22.00929 | -45.00026 | 2025-08-24 03:47:00 | NOAA-20 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 068b37cf-c672-3e93-8c21-2eb397a9f0af | -23.47101 | -46.81347 | 2025-08-24 03:47:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f2b01f1c-d100-3ee3-b9e2-a0d544e7a3ab | -23.2523 | -46.62754 | 2025-08-24 03:47:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| e0c169ca-cffd-3fe3-9730-c5ecf6f64baf | -19.62807 | -42.06248 | 2025-08-24 03:47:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 61b97279-b7d0-3439-bee3-fc1f1220e209 | -19.63126 | -43.19131 | 2025-08-24 03:47:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 462ebf41-b728-3566-adc0-76685cadf825 | -23.36963 | -46.86734 | 2025-08-24 03:47:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 53f52208-147e-3893-ba34-3ffcae8bc01b | -20.73925 | -41.77171 | 2025-08-24 03:47:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0242c5d5-a32f-32e1-8c00-8adc72ce5d4f | -20.34269 | -51.70052 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9990d082-9f57-3a7f-9018-45e25cdb5d9b | -20.36345 | -46.76114 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39a3dda0-761d-3eae-97e7-2da4c178f801 | -20.34906 | -51.70243 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 22e8b4d4-5ddb-3952-9eae-58c0958a440c | -20.36465 | -46.75522 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eadb05a8-a0e5-3012-a0d0-0ee049970e75 | -21.40457 | -41.81238 | 2025-08-24 03:47:00 | NOAA-20 | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e5534814-a2fc-3581-88af-595ea02fd7ad | -22.51015 | -46.67804 | 2025-08-24 03:47:00 | NOAA-20 | LINDÓIA | SÃO PAULO | Brasil | 3527009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fde10a50-a395-3398-a80c-b2c4f45b44ec | -22.54509 | -43.71478 | 2025-08-24 03:47:00 | NOAA-20 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3ec9c6be-8832-3675-9725-221cea0c04aa | -20.35805 | -51.69318 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5e93fea6-fb1e-37fe-bd38-d446cc8f4ebf | -22.65587 | -43.60153 | 2025-08-24 03:47:00 | NOAA-20 | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56f4224b-7e86-3efb-8c0a-ac29cc10b416 | -22.71956 | -46.97987 | 2025-08-24 03:47:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 50db1dda-0085-3452-bb73-edcc60cef963 | -23.49721 | -47.0736 | 2025-08-24 03:47:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 807599fc-17b7-3150-9545-baf0a67ee723 | -20.34906 | -51.70041 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 22f373c7-0426-3f2a-be2b-826af076e4b8 | -23.30791 | -45.53082 | 2025-08-24 03:47:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 675be8f3-eb96-3775-a8ab-a83a039ea965 | -19.68751 | -48.98422 | 2025-08-24 03:47:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 401d3c4a-a56c-35b8-be53-e91d58aa3a1f | -20.34673 | -51.68348 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad7aa1fd-5016-369c-94d8-4fd1cb73410c | -22.85163 | -45.22851 | 2025-08-24 03:47:00 | NOAA-20 | APARECIDA | SÃO PAULO | Brasil | 3502507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 607530f7-5759-3e96-b62b-edabf6faf77a | -20.34537 | -51.6892 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8de7da2e-e821-380f-b12a-b5f1686e42ca | -20.08256 | -46.11153 | 2025-08-24 03:47:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8609e643-1c78-3aad-834c-205780d29033 | -20.35673 | -51.69878 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 302a6c5e-d5ff-3272-a71e-c3e9c38ad0fb | -23.31216 | -45.53148 | 2025-08-24 03:47:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| ffc5c5e0-e364-3e9c-8f92-79b30daaeda3 | -20.35643 | -46.74625 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e72b0e6-bc61-329c-83f9-0a8b6de10cf3 | -20.94376 | -46.83033 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbd95326-566a-3a06-bffc-bf8af1338c2b | -22.12511 | -43.25008 | 2025-08-24 03:47:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 16287570-ad23-31c2-ad2b-37b14d0d588f | -20.07892 | -46.11768 | 2025-08-24 03:47:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d513f0f-968a-3ca7-8909-95be22036f68 | -20.69198 | -42.316 | 2025-08-24 03:47:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8204eb02-0b18-3c48-8503-c5dc783beb27 | -20.80389 | -50.12617 | 2025-08-24 03:47:00 | NOAA-20 | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| cc6a4c07-9059-3db1-9fd1-1cebdde8b485 | -23.10609 | -49.97801 | 2025-08-24 03:47:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 84d9037b-4f65-377e-a9bb-8d37a1b5aada | -21.40689 | -47.61775 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f26e05d0-8566-393b-a1d9-c55d6c21931e | -22.72923 | -46.9668 | 2025-08-24 03:47:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1395627e-45e3-38a6-8537-f6cadc98671c | -20.7357 | -41.77085 | 2025-08-24 03:47:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 64f96fd6-2d44-308e-9c05-88e36a8aee70 | -20.37171 | -46.74519 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58746e36-62b4-3370-8b1c-b88b06e5e9fc | -21.4078 | -47.61312 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b24aea2d-542a-311c-aef5-ca101e2a9494 | -23.4665 | -46.81229 | 2025-08-24 03:47:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6d742fde-e97f-3893-89f4-9941c436c3d4 | -22.14392 | -43.6528 | 2025-08-24 03:47:00 | NOAA-20 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 93443c23-7254-3762-b79d-63d319779c06 | -23.32948 | -47.84348 | 2025-08-24 03:47:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6aac7391-35ca-30c0-a45c-a5b1f7555446 | -20.08099 | -46.10759 | 2025-08-24 03:47:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cfae4b3a-40ee-3c0a-9339-cbc1b06951a0 | -19.83389 | -47.53781 | 2025-08-24 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e019f883-d3ac-31b3-8535-af69e0137b81 | -18.03728 | -50.61062 | 2025-08-24 03:47:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 726820f5-8354-3cac-bccc-139c7cf169e3 | -20.98481 | -41.84661 | 2025-08-24 03:47:00 | NOAA-20 | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10e1f126-222d-3a02-8b65-81c4d87819d4 | -20.80105 | -40.91073 | 2025-08-24 03:47:00 | NOAA-20 | ICONHA | ESPÍRITO SANTO | Brasil | 3202603 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 73cfa5b8-39fd-3b1e-846e-a185e752cae2 | -22.94956 | -45.13069 | 2025-08-24 03:47:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e8604b08-cc65-3187-a554-ac5b0e38d546 | -20.35875 | -46.73491 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6425f369-69d9-3dee-914c-c4a68531bbec | -19.54096 | -43.8359 | 2025-08-24 03:47:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f90e02d4-f066-3a82-bdbb-2bbcb994113e | -20.37165 | -46.73885 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01736302-0b8a-3990-b662-a4cfdfde21e4 | -23.62769 | -46.02829 | 2025-08-24 03:47:00 | NOAA-20 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3d4a2f27-97b8-3449-9896-e8013f90601e | -18.0385 | -50.61212 | 2025-08-24 03:47:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 42cfcaf3-a809-3fcf-96b0-711697c3da6c | -20.35878 | -46.7594 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2aaf813b-c129-3b27-afb8-35e0c2b4972c | -18.03608 | -50.61597 | 2025-08-24 03:47:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a3cd33ee-284a-3c72-8edc-3086e839ec8b | -22.45636 | -49.01028 | 2025-08-24 03:47:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 543e96d2-4aec-3237-95ed-4fd57c4113a8 | -23.27499 | -46.56771 | 2025-08-24 03:47:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e75264f9-9e4e-3f9a-aaa1-707e025be79a | -23.3113 | -45.53585 | 2025-08-24 03:47:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d550b75b-95c2-3f82-8d71-554922ae7cc7 | -20.35938 | -51.68754 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 46d122b6-a5ca-38d2-94c7-9d3a05ff1965 | -20.69069 | -42.31778 | 2025-08-24 03:47:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 817f934c-4f8f-30c2-b7cb-c0ba767c9eaf | -23.30702 | -45.53528 | 2025-08-24 03:47:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 820786a0-a081-3fea-b875-91f82de06266 | -20.93913 | -46.82862 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 292b5ac9-df3a-3c35-8bf3-a409427b29ae | -20.35813 | -51.69118 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c02a583b-1290-302a-869d-724244f52784 | -20.35179 | -51.6892 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 17.0 |


[Clique aqui para ver as próximas entradas](README31.md)
