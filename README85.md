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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d04adde6-b95d-31f4-ae65-5b9aa296a0b8 | -6.33866 | -44.10305 | 2025-09-06 05:31:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8fcfe753-73a9-3d28-95f1-b9b306483b51 | -12.96119 | -54.77806 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a6dc8eb-60c4-3557-808a-5d0b477f5ba4 | -12.96603 | -54.78202 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 404e1e68-8986-3694-9dae-2d4ed093eb60 | -12.48818 | -53.85262 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f1da9eab-7480-3db0-b7a6-649f1013bcb2 | -14.33972 | -60.32655 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a04b4a4-4a44-3e34-af8b-28814dbc508f | -12.97777 | -54.8165 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56560d00-7787-30c8-818f-a8466726e75b | -13.00141 | -54.84797 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3ec1f74-3eb6-3696-9eee-97be2cb10c1b | -11.63829 | -54.53977 | 2025-09-06 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5160ce86-efe5-354f-9aa3-129722ac1ff1 | -12.96078 | -54.78138 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 320665e5-aa65-3d8c-bff6-647852203606 | -13.01109 | -54.84724 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fff74a7a-4973-3e52-880e-85c8135d9d9b | -12.48339 | -53.84635 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be9819ab-0060-30d8-b0e9-71dd1ecd383c | -13.0193 | -54.83101 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f17dfc21-f082-3743-ba17-c606d06e6259 | -12.97699 | -54.82285 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee76482f-a171-32a8-837c-06fe0f1b49c1 | -12.96928 | -54.79903 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39aecc54-98f2-3c60-a039-91bfc7bd1cca | -14.34339 | -60.32751 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1794b065-124a-3a6c-b602-32d25744d278 | -12.96038 | -54.7847 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60a1cdd3-57d5-3992-8830-cb414c8feb99 | -12.96095 | -54.82383 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e09abf8-625d-3ae0-bf0f-314223bfaea0 | -13.00811 | -54.83598 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfaa8d57-2882-37d5-a745-1a615fd669fe | -15.57457 | -52.89253 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 752ef138-252a-3af4-907b-547a3435cf5e | -11.21844 | -55.02715 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4f4674d-2a28-3468-a87d-c4eda12c9310 | -10.15816 | -61.13288 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf018368-52ce-35d8-b316-72fe29877b9b | -15.72167 | -53.58476 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a6a7fb1c-2db7-3270-9471-63c514efb01d | -12.96617 | -54.82453 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c686e821-6bf1-3ce5-9cad-6a8c770cf085 | -12.98298 | -54.81729 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06b2a954-fc36-3679-8c12-79c74beb5ea5 | -12.99583 | -54.79918 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e5057a9-ba03-3b61-9574-5bdddfa59f73 | -12.99503 | -54.80569 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c95bc295-b02f-311a-b975-d03a95f3afd4 | -12.97178 | -54.82204 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd0aeeaa-cca2-3b5b-b6ea-bcfd3255db1e | -13.01969 | -54.82771 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0171fc85-9b56-39d2-8c0b-84548015daf6 | -10.42265 | -60.74455 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da85eb84-5f61-39d5-af65-6200a0ee9d37 | -12.95612 | -54.81995 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 371488ef-8327-35fb-913f-087be486f88f | -11.21453 | -55.01772 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 857a175f-530d-305b-b51e-4b62cd0295fa | -13.01913 | -54.82538 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a287c39d-b2a5-3a29-a7e3-63b5a777e064 | -13.01872 | -54.82868 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a24bceba-e414-3d14-8e3c-1db1d428f7c9 | -11.64352 | -54.54045 | 2025-09-06 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94ea56b3-efce-32cb-8437-cf1f04f7519e | -11.64311 | -54.54366 | 2025-09-06 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bf8ac02d-2ad4-3c60-959c-d02781f6d360 | -14.18303 | -53.06886 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04e5cee4-3b84-31e6-9b44-ce93f5065c56 | -12.48775 | -53.85633 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbd15d39-39c1-3250-920a-d07092ebe782 | -12.00347 | -64.84168 | 2025-09-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 532b735b-13a8-3995-8366-035b2ebcadd4 | -12.99824 | -54.82262 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e12e2277-7d91-3a6c-8b5c-09d870c76225 | -13.00067 | -54.80304 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2de383d-814e-3350-93de-aa236b5a9517 | -14.34038 | -60.32168 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab368210-458d-3829-bb51-0f5ac12dc20e | -13.00306 | -54.82655 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92ff6565-f9a6-3eda-b31b-eb793ea6ef19 | -15.58074 | -52.89268 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dec0ac9-fe4f-3357-8682-2ee39ef60dde | -14.1776 | -53.06359 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d9a50b8d-384d-3a74-9554-d6d24db87f1a | -12.98663 | -54.83072 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99979c7d-86bd-3a59-8249-bcd2b087d741 | -12.98429 | -56.91124 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d27c1a94-50eb-3b26-9d53-c1911a3155cb | -13.00964 | -54.82297 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3961b05c-f652-3c4b-842e-535ea8b4f34a | -15.17554 | -52.40566 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c13b93b9-199c-3048-89cd-2fe86a62bb23 | -10.76656 | -59.85088 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5c225d4-b21f-3b11-ac69-2f7c7d575623 | -13.00748 | -54.83372 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e08694f1-0b49-3a55-ad52-df9ee634dc5e | -13.01229 | -54.83768 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ef684f8-c7ca-3f95-87b4-6b62527331b8 | -6.20846 | -42.62049 | 2025-09-06 05:31:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| be59f5b4-8732-308e-b8cc-cc8c1adf7b08 | -19.88696 | -57.91205 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f097f0e5-fced-3f5c-9d20-72d0a10648f6 | -19.89569 | -57.91843 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cdc94a51-1279-3948-ba31-17a809e509ac | -19.80737 | -57.94822 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6f48d0fb-44ac-3021-9586-16219475f251 | -19.81905 | -57.97047 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5692ad96-9422-3b93-9ced-6b36c36bc4ff | -19.90847 | -57.93054 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 42da1972-fb79-3e92-ab39-2acc7731cae6 | -19.8951 | -57.92356 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cf7ab77a-c416-33cb-ac34-1ebd5da8ecc1 | -19.89975 | -57.92418 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 19e5e988-ea2c-3c2d-b671-a434fffbe4af | -19.89103 | -57.9178 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| def4e80f-6b87-32f5-bd24-03a7ee9a6236 | -19.80486 | -57.94181 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1fa82fec-55a5-30d5-bc36-3751b09b144f | -19.91141 | -57.9328 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 712d8061-122f-32b2-84a0-1fcc276bba5d | -19.88637 | -57.91719 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b671515a-6934-3d27-987c-a45419ef35a1 | -19.81385 | -57.97494 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fcf272d5-d32e-3571-8574-efa2397c9945 | -19.8158 | -57.96909 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9ffca221-86e0-3d36-9eca-279601c831ab | -14.58424 | -48.00138 | 2025-09-06 05:33:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c1daded4-0a16-3255-bd39-794f0e848f10 | -19.80891 | -57.94752 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 91b1107e-876f-33bb-995a-2a979920ad02 | -18.43978 | -45.93105 | 2025-09-06 05:33:00 | AQUA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0cca036d-0e3c-3568-a9de-73155b37b4a7 | -19.81145 | -57.95394 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b75cd2fc-6914-3935-a24f-02a4e5684f90 | -13.84923 | -46.25984 | 2025-09-06 05:33:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 083b45e9-c5f8-3ab9-b072-3041503d69b3 | -19.81295 | -57.95323 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 59f885c7-f083-32dd-9fe5-de1eb19cdee5 | -12.94468 | -46.56393 | 2025-09-06 05:33:00 | AQUA_M-M | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 81816572-246b-3f21-84bf-b51831823734 | -19.90441 | -57.92479 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b0047ee0-e233-30c7-aba6-96030158a330 | -19.90382 | -57.92992 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1ad96647-7e59-3f64-b963-f1f930ef8ab5 | -14.57247 | -48.00019 | 2025-09-06 05:33:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e53f08b3-a1ee-383d-88e0-b3486c3562fc | -19.80793 | -57.94311 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b8a175b7-1070-3893-9ca7-de7fc9f2dfd6 | -14.56959 | -48.0168 | 2025-09-06 05:33:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9fa602ac-4368-30a2-9629-5d994df01211 | -19.75668 | -57.9509 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 71b06da7-ad0a-3cc3-8ec0-bdcfe995c7cf | -19.8152 | -57.97416 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 004590fa-9232-3963-a2f5-6e28f5f52d87 | -19.81201 | -57.94884 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 07ae9ace-f096-3fe6-b5e3-e16e674b757f | -19.80328 | -57.94249 | 2025-09-06 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| de358eb3-2398-3f6c-ae06-5429341ef469 | -14.82908 | -48.18454 | 2025-09-06 05:33:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 76f9ee39-73ab-3a49-b478-91303f35818d | -20.53444 | -46.47074 | 2025-09-06 05:36:00 | AQUA_M-M | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7ca61bf9-2047-3c66-8f99-72fe78fe3111 | -19.50249 | -42.57229 | 2025-09-06 05:36:00 | AQUA_M-M | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2214d8d3-fa7a-3b23-9206-222d6bebdf7c | -19.62853 | -46.01724 | 2025-09-06 05:36:00 | AQUA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f44e68eb-5011-3d65-85f4-9e0c7dc270da | -20.53629 | -46.45969 | 2025-09-06 05:36:00 | AQUA_M-M | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 42.6 |
| f2ebd704-7827-38c0-81f3-1b41f09f840a | -19.50388 | -42.56264 | 2025-09-06 05:36:00 | AQUA_M-M | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| ff05aedb-c252-3083-a575-4571fbd7fd74 | -23.42396 | -47.03855 | 2025-09-06 05:38:00 | AQUA_M-M | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| ceae3f69-5323-3cb3-b22f-5e7dd4b65698 | -5.76624 | -56.51374 | 2025-09-06 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40e05aec-1dce-3d5a-9406-97d8a80c5640 | -5.78778 | -57.54958 | 2025-09-06 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f6755e0-883d-3d57-9327-1748618b97f4 | -5.06247 | -56.07201 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7bf0e24-ab51-38c7-a466-8255f8794c5c | -5.7655 | -56.51892 | 2025-09-06 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e99306a1-9367-3530-a78c-6fe3eae7f31e | -5.78717 | -57.55399 | 2025-09-06 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65a565aa-1d72-3375-b034-b8d2c6ae6edb | -5.06969 | -56.06776 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74941020-d852-3b7f-bb42-530cee8c2e6f | -5.50956 | -60.13768 | 2025-09-06 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 672b447f-a24c-35a8-9ad5-4a770e71c234 | -5.14838 | -60.31478 | 2025-09-06 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aeed9f0-7f17-3766-a343-0b269ac3373d | -5.06916 | -56.07381 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfd26a2a-ae99-3954-a075-eb565346b4da | -5.50456 | -60.13697 | 2025-09-06 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9c69155-8d5e-3881-9b0e-7b47d12eeb9b | -5.1476 | -60.32022 | 2025-09-06 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e10f88b-50b5-3ddf-a11c-6ad6f3a22e3c | -5.50537 | -60.13129 | 2025-09-06 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README86.md)
