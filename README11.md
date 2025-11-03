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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8298b044-4ba3-37c2-a64a-c3493816475e | -11.33998 | -54.38046 | 2025-11-03 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e54df8b-fb2c-3366-9345-62d5a74ff4d0 | -11.05558 | -45.33237 | 2025-11-03 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bf3b290-b577-302d-bd31-a1e19f3a003a | -14.20177 | -47.78584 | 2025-11-03 04:53:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| decb5195-402b-3b36-b64d-8c2a32cfa69b | -11.61792 | -58.2807 | 2025-11-03 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5b1625c-728b-38d7-b606-2949e5973b8f | -8.59704 | -44.16056 | 2025-11-03 04:53:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96fbba76-53e5-31b2-9d90-264b56b4a93d | -10.54649 | -44.90232 | 2025-11-03 04:53:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 348cd253-c5eb-3070-86ed-8baf13b57a05 | -12.42086 | -54.48567 | 2025-11-03 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d0b981-6334-3179-b614-d45d599c9b15 | -10.42818 | -44.94934 | 2025-11-03 04:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d1aead9-8cf6-3410-b102-eaac5392a638 | -9.14065 | -51.29829 | 2025-11-03 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 423482e1-ab44-3578-9095-b296364b5645 | -11.11873 | -41.09256 | 2025-11-03 04:53:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f844646f-41e9-3d0b-ad24-07e385c34171 | -12.68375 | -41.57656 | 2025-11-03 04:53:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72c41a51-9212-3235-bb78-d8034043037e | -10.30087 | -53.7786 | 2025-11-03 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 432a95a8-762b-3f6a-8353-f0a6356ff083 | -10.84823 | -56.95432 | 2025-11-03 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 834a92db-ac6b-3d86-99c4-cdbd89a7400a | -10.42347 | -44.94578 | 2025-11-03 04:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 66ceaf81-e7d7-3eeb-907e-6260ec87cf7b | -10.84749 | -56.95867 | 2025-11-03 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16302207-8c59-3fad-8247-dc603e076076 | -14.20621 | -47.78633 | 2025-11-03 04:53:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7095039c-28a6-3549-a78b-8f8673a5ab80 | -11.05597 | -45.32947 | 2025-11-03 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b33e2eb-ff6e-3a7c-a49a-36c326703814 | -9.85884 | -44.15643 | 2025-11-03 04:53:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 443ddf60-4f36-3b39-921f-9bcd3b392dfc | -12.93229 | -57.01542 | 2025-11-03 04:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d20d239e-e44e-3c5c-893d-d59b54540284 | -10.51064 | -44.89746 | 2025-11-03 04:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ddd6adb-7d33-30db-be8e-cde4a1f21033 | -10.55078 | -44.90919 | 2025-11-03 04:53:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31fcd9d8-8a27-3161-824b-91672d61dc64 | -10.49759 | -57.61338 | 2025-11-03 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1cf61f1-8233-32f4-a2ea-e41a5d07be06 | -12.68448 | -41.56851 | 2025-11-03 04:53:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a3e995f7-2669-3a7b-aa47-64d3af68c0b5 | -6.61914 | -55.02162 | 2025-11-03 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f9a373-9253-3011-ad54-930482782e72 | -8.2889 | -55.07027 | 2025-11-03 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bebcd2f3-82c0-3260-92d3-85c881f74d5e | -9.77825 | -57.41346 | 2025-11-03 04:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 986558d3-1e0e-347a-9f3a-df3f0c96aa19 | -9.56979 | -62.65617 | 2025-11-03 04:53:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ee16346-a1dc-3e96-88b4-fe254c136920 | -9.85926 | -44.15314 | 2025-11-03 04:53:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4356ea50-1139-35b2-a93b-421aaa382895 | -9.90952 | -44.82388 | 2025-11-03 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0a5b21c-2c21-37a2-8a71-2ab655d9b704 | -11.32888 | -54.38591 | 2025-11-03 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf531edb-6ae3-3a95-a534-ec57c448a9d0 | -10.48247 | -51.82301 | 2025-11-03 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25286fd3-6bb0-30f8-9b64-a5bbbf7f0518 | -9.90443 | -44.82312 | 2025-11-03 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93bbf85f-d4e3-324b-baf2-c73c00d2fcc3 | -9.85434 | -44.14923 | 2025-11-03 04:53:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 127c9cf3-b71d-3ef0-8ca4-6e61fbb1d93c | -9.14009 | -51.30202 | 2025-11-03 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9639b531-c880-375e-a73f-dec42d36f97d | -10.42858 | -44.94637 | 2025-11-03 04:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2258add1-f63c-3407-a6a0-0f7552e3c203 | -12.43078 | -63.14787 | 2025-11-03 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d035964b-4a79-3432-9d88-be37f04b7a1f | -12.42142 | -54.48214 | 2025-11-03 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25c96dbc-8956-3a3e-893c-1c166e9fc96e | -7.80875 | -61.34747 | 2025-11-03 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd34e8b1-06e4-3429-a0bc-d2c72142590e | -11.3433 | -54.38101 | 2025-11-03 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ef033e9-a261-354c-a6eb-3d0f7c4969c4 | -11.00674 | -42.74239 | 2025-11-03 04:53:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| adef2e12-85da-3468-a60a-c8647384f376 | -11.61404 | -58.28005 | 2025-11-03 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8fb8434-faca-34c2-a590-1b47066ffba9 | -12.43603 | -63.14894 | 2025-11-03 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1c68c3b-9a8a-3551-8ec5-a6adf293531a | -11.0557 | -45.33038 | 2025-11-03 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c515e64-ff08-3e40-9a7e-b3d36cc95dfb | -7.80928 | -61.34454 | 2025-11-03 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8716f2a-2ac9-335e-811e-30b23c12bd10 | -9.13668 | -51.30149 | 2025-11-03 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca519c05-8a5e-3c3d-b5da-b652172b6780 | -11.48013 | -54.60748 | 2025-11-03 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2fadccf-60d1-38e8-bd89-a5c9fb319aed | -12.43616 | -63.14492 | 2025-11-03 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e03a82df-7468-375b-8911-0dd7eda1d4df | -12.43666 | -63.14563 | 2025-11-03 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9b7e4c4-eaa9-3a25-b409-dc259d6349d3 | -12.93872 | -57.02071 | 2025-11-03 04:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe20342b-ce8c-32c5-a1be-bc48c20c38a0 | -10.42307 | -44.94877 | 2025-11-03 04:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4bbb6eaf-8569-3c3f-aedd-686f720c0438 | -12.68432 | -41.57161 | 2025-11-03 04:53:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 55cf62e4-733f-333d-9d00-f3205c647858 | -11.49924 | -54.27647 | 2025-11-03 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2e20b1f-785f-3e72-9ddf-5105aa9bf5bb | -10.8523 | -44.73627 | 2025-11-03 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 584edb33-6174-3955-9a01-74b8523cbb23 | -11.94957 | -44.8007 | 2025-11-03 04:53:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaff0026-8de4-3920-b6b0-808d915ff80b | -9.77814 | -57.4155 | 2025-11-03 04:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4309982a-67ba-39af-8ecc-a919c2c8aca7 | -9.57042 | -62.65272 | 2025-11-03 04:53:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e16b1dc6-9e7e-3c03-a566-e31e0ac03c28 | -10.54607 | -44.90547 | 2025-11-03 04:53:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ff45986-852a-3df2-937a-60d0df64ec6c | -10.40441 | -44.35755 | 2025-11-03 04:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc416f40-bee5-39fc-ab7f-2c95d1958c6d | -10.40353 | -44.36425 | 2025-11-03 04:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f65403e-178d-356b-8dca-15946a95cd44 | -10.40396 | -44.36099 | 2025-11-03 04:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87d3862e-3713-30a2-8320-12c9f67c7f7d | -8.43655 | -45.61755 | 2025-11-03 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5626668e-6da5-3eb8-a29b-d15b69be4af4 | -10.77121 | -56.81178 | 2025-11-03 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65cc9ebe-8784-3caa-b1b5-aaedb525c81a | -12.68391 | -41.57375 | 2025-11-03 04:53:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ea8f5981-50e6-3d94-9e73-c98d88defc63 | -12.43551 | -63.14824 | 2025-11-03 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fe0e137-e0d2-3790-baef-fd549c5512d9 | -6.62326 | -55.01832 | 2025-11-03 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ac435a3-1c21-397d-bfce-1986fbff3dfd | -12.43026 | -63.14717 | 2025-11-03 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 860ee941-3183-34fe-9195-e7bc72cee656 | -6.61978 | -55.01774 | 2025-11-03 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c6cf661-5a5e-3a35-a009-d8e815013201 | -10.6564 | -51.8941 | 2025-11-03 04:53:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26fd6445-a6cd-3634-b2da-1c26d394d81f | -11.6218 | -58.28138 | 2025-11-03 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac7c0238-4cfe-37a6-9ca0-c1539186d055 | -6.62262 | -55.0222 | 2025-11-03 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29c9a336-7e67-36d5-8536-0ea84bf5905a | -11.00728 | -42.73802 | 2025-11-03 04:53:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ecff627-8f16-355b-be58-77e34c875660 | -9.85969 | -44.14985 | 2025-11-03 04:53:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1eff426e-864f-3363-9612-dd6f150c05c2 | -12.57524 | -62.95701 | 2025-11-03 04:55:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7d3e5e5-6fdc-3c25-8319-1190d5326c1c | -12.58177 | -62.95536 | 2025-11-03 04:55:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fcc7cf0-b2a6-38eb-b946-e892de81317d | -12.57598 | -62.95745 | 2025-11-03 04:55:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4da50f1a-fdd2-30b2-bd40-dcf447acb4f3 | -12.581 | -62.95493 | 2025-11-03 04:55:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| beaad0fa-5b4d-3f36-bb66-31b8416d5dc9 | -10.40713 | -44.33614 | 2025-11-03 05:12:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 8acce188-db66-3e56-92c7-e1c563961af3 | 3.83938 | -60.62026 | 2025-11-03 05:37:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85867d72-9806-38e6-9e0f-ec93687b56a8 | 3.81711 | -60.41309 | 2025-11-03 05:37:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cb5c7f4-57c0-3fda-9504-00b78abcfe76 | 3.2281 | -60.75229 | 2025-11-03 05:37:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af9fb809-ccac-3e9b-a121-36f324b71ce9 | 3.22466 | -60.75284 | 2025-11-03 05:37:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c40cf0be-4c2a-3d1a-b851-34796b519d17 | -0.89637 | -52.02875 | 2025-11-03 05:40:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ee2f3314-b83c-3c12-9a1e-62a59aea183f | -2.4513 | -57.8938 | 2025-11-03 05:40:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d64bd04d-99b0-3599-ae0c-afe899142d33 | -5.18521 | -60.30873 | 2025-11-03 05:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa5a408b-6ece-38f7-b304-7872f3676f4d | -1.97108 | -52.10953 | 2025-11-03 05:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 676a31b7-dc34-3c79-ac0b-cd540753369e | -5.18596 | -60.30379 | 2025-11-03 05:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5ad8d3a-3925-3f65-a9fe-2dc7e6c973a0 | -1.26466 | -53.83281 | 2025-11-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c3a73a2-f00a-350e-8970-fad0d7ce0c9e | -1.40122 | -53.08468 | 2025-11-03 05:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdc380cc-b5e9-36cb-aeae-b1b9288ca792 | -5.18227 | -60.30567 | 2025-11-03 05:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9bc7b46e-4588-3bc2-8384-fd2ca74ada92 | -5.18206 | -60.3032 | 2025-11-03 05:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed512726-b747-38b1-a716-ffa24960e72e | 0.86136 | -51.25698 | 2025-11-03 05:40:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12958f79-270f-3a7a-92e4-263f6ef04573 | -0.89556 | -52.03395 | 2025-11-03 05:40:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d1fe3a2d-e877-3c78-b02a-e92241f783d5 | 0.8463 | -59.3368 | 2025-11-03 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae30ccc2-b651-33ec-be09-d9f9d112435d | -1.27164 | -53.86301 | 2025-11-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83906a93-2d93-3fcf-b3c5-d0fa34da14e2 | -3.23703 | -58.88764 | 2025-11-03 05:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dad340a-30e1-3705-8c4a-4292bdb0bafb | -5.18617 | -60.30626 | 2025-11-03 05:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c93d5fce-f97b-3d8b-a9ba-790b8ac5799d | -1.2741 | -53.86273 | 2025-11-03 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f3fa2f9-0acb-3a7c-b819-c925055828e7 | -1.96965 | -52.10982 | 2025-11-03 05:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 31be3630-8356-3db5-afc8-54dac26ab75d | -1.14509 | -53.56885 | 2025-11-03 05:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e195cfb6-d8fb-3be2-87fd-0f082c3ecf15 | -2.69361 | -59.81514 | 2025-11-03 05:40:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
