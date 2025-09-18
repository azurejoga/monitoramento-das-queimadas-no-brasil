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
| 52a7f15e-1c42-30e4-8d94-1d787eeb5552 | -2.57143 | -48.96661 | 2025-09-18 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8fdbd78-7e3b-3ac1-824d-33fb9025bced | -5.30015 | -43.05745 | 2025-09-18 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56c902ca-6148-3168-aba6-5f18bf0cc403 | -4.69977 | -41.9496 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 609bb579-e4aa-3515-9f44-7e5873d33b0f | -2.64034 | -48.04733 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e521ae48-d258-3066-8b06-7f886c6347af | -5.29394 | -44.71656 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a884c9ee-e49f-3bcc-9298-5793aed31065 | -5.77933 | -42.77585 | 2025-09-18 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1dd435b-1b05-3025-9ed8-9a4a6530613e | -3.73749 | -49.05276 | 2025-09-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ef17bda1-7087-30c2-a374-7cdfebcd17aa | -5.30809 | -47.23016 | 2025-09-18 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b56c3ba-5bf4-3955-b9e2-28b1806c955d | -5.81586 | -45.92148 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deae5908-2617-3b1b-b46f-ee0baf9adc5c | -6.31009 | -42.40112 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8894effd-58f0-364f-ac40-b06a278248ab | -5.18694 | -35.87132 | 2025-09-18 04:12:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7e01506-e2e8-3190-8acc-8fb28576b969 | -5.18754 | -35.8692 | 2025-09-18 04:12:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89db1fed-febb-3a28-b268-4e7fee9d7115 | -2.96173 | -48.58485 | 2025-09-18 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7da37e0-be0b-3c77-8a9a-40f76e2d2796 | -6.61252 | -44.28621 | 2025-09-18 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4fb3bcf-b0ca-348a-b900-f00085dc7606 | -7.0729 | -44.36316 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4a25f8d0-debd-38aa-b001-9929ea99331b | -4.81128 | -42.73262 | 2025-09-18 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 98bf56c6-6369-36b7-903b-eb7363dad246 | -4.91962 | -47.86134 | 2025-09-18 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 137a5100-919a-30f0-8519-4d728e388fa0 | -6.42274 | -43.60399 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 063e2acc-dcc5-3c7e-8e18-32c102cbe5b3 | -4.69543 | -41.97744 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d6eb3aad-0474-3785-bb8c-59dccdbb039c | -2.91967 | -48.31016 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1536934f-5159-3872-9050-d3cc046ff98b | -6.59081 | -45.59157 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dbd94bf5-b0f3-366b-825a-4aedae7a082d | -6.57983 | -43.03986 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 492b68d2-daf5-38b7-bc0c-78fb291fd252 | -6.68911 | -46.30391 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8a31fa9-183e-3bbf-be93-728d761b6755 | -6.22578 | -44.41524 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 915fe510-f88c-30b6-882a-f41d7915b1e9 | -5.41891 | -42.88514 | 2025-09-18 04:12:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bb2acf01-0481-30c6-ba83-250b8f810403 | -3.26945 | -43.05153 | 2025-09-18 04:12:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f6480971-20ee-3e66-84d9-80a76e1e81a6 | -6.39158 | -43.32961 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f3d6a7f-9f5d-303e-b5de-65af20140d92 | -6.18085 | -41.22441 | 2025-09-18 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 55b99b3b-c349-3de5-8055-29bcdb96a7b2 | -3.27222 | -43.05552 | 2025-09-18 04:12:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0b7e8eb-7d51-316f-bff0-82e3e847d95e | -3.26835 | -43.05846 | 2025-09-18 04:12:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01f24c3f-de45-3add-b3f5-d0a8528a3082 | -5.80419 | -45.91251 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 065790d6-e03e-3ab5-9ebd-04a34605ea16 | -3.51362 | -52.7558 | 2025-09-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 22b41d66-7ea0-3be1-8d10-8836152b9199 | -6.61371 | -45.63402 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 488a0873-41ff-3bc8-b32c-ab79670da2eb | -5.96429 | -45.83632 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9490274-7717-3cea-8fb9-b8cec72f19f3 | -5.09334 | -41.14582 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96679368-2217-3376-bf69-4284aa85b5c5 | -6.38179 | -43.45588 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fa73b79-6a25-3189-ac96-914d50284f15 | -5.50549 | -46.64434 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51486406-057c-36ea-9b63-3b0a7df3ae18 | -1.23674 | -47.02407 | 2025-09-18 04:12:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66bea5a1-a632-3970-bfa6-bf43ddf820df | -1.94932 | -47.95885 | 2025-09-18 04:12:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25a7ceb9-bbff-3290-8b51-c167d477e8d0 | -5.8755 | -42.63871 | 2025-09-18 04:12:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0f57855-6892-30a2-8b0c-3f43427102d9 | -3.79854 | -47.57658 | 2025-09-18 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd9e76d9-eee1-3be9-86e7-d2dbc267fb33 | -6.22241 | -44.41467 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3f12b0b-a624-3a08-9c74-c957ce9ac9ea | -5.56146 | -46.28132 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5a790a4f-c280-372c-a890-1afd7ff0d5fd | -3.26613 | -43.05101 | 2025-09-18 04:12:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 716ca92a-d02a-32fa-990e-f1ec7b006fd8 | -6.15293 | -45.98948 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9130eb7d-c890-301e-84d0-d441917e818f | -2.29935 | -48.14442 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ed61652-c090-37e5-bd59-a2ee902bd414 | -7.06955 | -44.36261 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e129074e-06df-3a7b-b2c4-60e29a594e06 | -3.30046 | -41.00124 | 2025-09-18 04:12:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f22d97bf-ded0-3c89-9de1-017e1c6ee2a7 | -5.80972 | -45.90083 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecced10d-0414-3655-b85c-446feae429f2 | -6.36344 | -42.8182 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb5070e0-19df-365c-8ce7-e27dddc3f322 | -4.34402 | -40.73676 | 2025-09-18 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 13841cf0-d461-3507-b3d8-d9bce8ad3d6e | -4.69574 | -41.95611 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3b67a891-1624-3574-aaf7-48f64bafef9d | -2.91844 | -48.30392 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95ab0b97-5b74-3ca1-b44b-f8b50a5675b6 | -7.05246 | -41.77348 | 2025-09-18 04:12:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3bbc8d7-8d86-37e9-877c-9c702c4b98da | -2.92207 | -48.30873 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 83e210ad-ed9a-3def-af16-9ade34ae7ff5 | -5.67183 | -43.15478 | 2025-09-18 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92cebb21-1810-347a-99df-cec34cb4e262 | -3.81437 | -41.01139 | 2025-09-18 04:12:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a4be78fe-7be5-3a5a-bbbe-7bf5268e237f | -4.69597 | -41.97395 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 55b39557-78d2-368a-9bb9-7f6cac7e8a71 | -4.34461 | -40.733 | 2025-09-18 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c3ae711-a1f2-3756-9354-9f2b8ecb802c | -5.07764 | -44.95228 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11d3b0d4-20c1-36b3-94d8-57c091e6eda8 | -5.67954 | -43.14891 | 2025-09-18 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a8c0f57-7d37-3ef6-848d-5076e61a83e6 | -5.62277 | -42.90645 | 2025-09-18 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 161c86fc-5d28-3bd8-8fc1-1c8ea32e26a9 | -4.61468 | -46.34812 | 2025-09-18 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45dc9bda-5330-31fb-8a79-7d98cb7c6661 | -3.64409 | -48.32487 | 2025-09-18 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbbcfcf3-5fd0-327c-bf63-322f21d89994 | -6.9861 | -44.44033 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1b81622-2b30-3894-9a85-622c3ba5f25f | -6.60364 | -45.64568 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50383ddf-c41e-3bd6-8606-2602d426b14e | -5.78698 | -43.75728 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c44061b5-da64-3feb-ab16-50a0ff4360e4 | -5.65874 | -45.04166 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2df8d520-9ea2-3db5-9c4a-a7e9860b31e2 | -3.27556 | -49.14724 | 2025-09-18 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27edb0ca-90d0-3548-b4f7-bf0b281100a4 | -5.88166 | -45.87788 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec8a9e32-bcc1-38a3-9d6e-fac357db1c99 | -6.5507 | -44.0151 | 2025-09-18 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e8d38ea-c80d-3e33-a1db-99ea33d36b35 | -6.42385 | -43.59703 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57a8d43c-87fc-39d1-ba58-735eaad434cb | -5.88618 | -45.8952 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57e24de2-5749-3b08-953a-017f1db2b891 | -6.99347 | -44.7704 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f240f31-25c9-329a-a9b3-75195ef82dd1 | -6.73052 | -44.14894 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1586951d-d0d1-3a6a-9178-2f4330f3b0ec | -6.58163 | -45.62617 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88b2ee3d-8556-3786-acf2-37f4025be906 | -5.36568 | -43.0076 | 2025-09-18 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1ca9f4f6-a475-3e41-ba5b-befcd22068d9 | -7.20755 | -39.96605 | 2025-09-18 04:12:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5ac10700-58e9-3c0b-b4f4-889d3c644ff2 | -4.7031 | -41.95012 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b665373b-5886-3a84-9497-3b5190cebce7 | -6.72385 | -44.14786 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 14af8dae-5b29-3687-9c12-555550820b2f | -3.51429 | -52.75189 | 2025-09-18 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| fb74a742-1968-32b3-8d28-8223efb1badd | -5.53982 | -42.20168 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0c1f3f7-5ce5-320f-b988-60eaa336b51e | -7.07629 | -44.17119 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4eb0868e-4d39-32f5-932f-257c43744f4a | -6.8638 | -45.61032 | 2025-09-18 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e51d8d8b-0f7f-3bf0-98dd-64a6b36c1c49 | -6.35574 | -46.10082 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b763a879-acf4-3761-a844-5726060f64fe | -6.31341 | -42.40164 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4137d0bd-6ed7-3fc1-a81b-d0bc8d4f74f3 | -5.36514 | -43.01105 | 2025-09-18 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1c27f243-da5d-3a96-9570-6e32263c2c23 | -7.11728 | -43.89378 | 2025-09-18 04:12:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e02910d6-7286-36a0-a915-2f7dc62b0bca | -1.23617 | -47.02765 | 2025-09-18 04:12:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e783a29e-486a-3faf-afe5-c962d174847a | -5.59327 | -43.80175 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23240b07-b734-3d10-863c-c008ed7a3736 | -5.73675 | -42.57058 | 2025-09-18 04:12:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 01f195f2-a19d-398c-8970-80d76dd5c655 | -6.99068 | -44.76619 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0db0cf5c-8784-3218-b110-84bb5b6b6ed0 | -4.66351 | -46.31753 | 2025-09-18 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c9dbdd6-ec84-3330-9abb-24df7cda21c1 | -5.89819 | -45.88885 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b2ef12b-303f-3ca6-9759-a18929857124 | -5.71539 | -43.63134 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9e74cb9-ac10-3337-bea2-1b6c1b745d88 | -5.10063 | -45.51139 | 2025-09-18 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad99ca5a-b52e-37ee-a9ca-cf0131146e77 | -6.4233 | -43.60051 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01b11a54-6282-31c4-9cb2-7ce8a1de667d | -4.91903 | -47.86494 | 2025-09-18 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24432272-55b0-3a02-8f10-7ffc6b8f66c6 | -6.58712 | -41.383 | 2025-09-18 04:12:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e539824b-376e-3ac6-ad29-6efce51fa1d2 | -5.06965 | -41.16435 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README14.md)
