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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95fbf992-fb73-3fae-80de-434ddb2040b3 | -11.8368 | -51.2641 | 2025-05-31 03:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 5cd14200-84ea-3f9b-b57a-0e6b314f10dd | -9.78862 | -37.08312 | 2025-05-31 03:34:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 06dda16c-0c06-3e78-bf59-23a670f9f3d6 | -3.76932 | -41.60728 | 2025-05-31 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9994cbf7-2868-3afd-bf93-218e69a3aa63 | -5.8479 | -43.63825 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce5ffe28-763e-345f-9fe5-3fd446badb9e | -7.87586 | -45.99542 | 2025-05-31 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b666dc46-c737-3b00-9628-3fd4b47ac17a | -7.23661 | -43.09232 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 13a35d3f-9eaa-382a-87d3-a345aba98db6 | -6.33508 | -43.38036 | 2025-05-31 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5f36d65-2812-3eed-9647-c31bf9f863e0 | -5.83341 | -44.08913 | 2025-05-31 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e2b379d-ae08-3e5d-9c1e-e5b577d71fd1 | -6.15113 | -42.61376 | 2025-05-31 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a3222dab-e2f7-3f60-b5c1-4e8f164bcbae | -5.82756 | -44.088 | 2025-05-31 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86e5900a-cb87-3e05-b3ef-54000435782f | -5.50217 | -35.58501 | 2025-05-31 03:34:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cab9fd85-f88c-36f6-9986-d3995ed55a41 | -7.00474 | -44.62379 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 71402b55-b31a-33b8-b2f5-468aecb0e978 | -7.58502 | -45.86745 | 2025-05-31 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c752ed4e-08e1-3fde-bd9e-fcebd10d9851 | -6.15229 | -42.60705 | 2025-05-31 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 0e3e08f3-2fa0-3720-a15a-a22c280e5c00 | -7.24736 | -43.09424 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c47cd42a-98ae-3ea0-993c-2491c8337440 | -7.21438 | -43.12356 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5ee421e0-ef13-3663-8010-e8597da538d2 | -7.24259 | -43.08987 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9b611639-da88-39ad-9649-37bd864d59ae | -5.8536 | -43.63927 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 430ce4ef-9452-3250-93a9-a2119adb5b8a | -5.86296 | -42.84081 | 2025-05-31 03:34:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 55cfe8c3-6e95-366c-8771-411c8a2a256c | -7.00712 | -44.62601 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1dc629a2-41cd-3a38-a6b7-495870722af8 | -6.60383 | -39.39628 | 2025-05-31 03:34:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca69a868-a286-37fe-907c-6e208346ad47 | -5.85694 | -42.84334 | 2025-05-31 03:34:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1ed4465-1a2e-391b-a23c-90380d6b11f0 | -6.27324 | -44.20193 | 2025-05-31 03:34:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19e7f0c6-a9c7-39ae-a8a0-1cbb5ebcd763 | -8.07168 | -34.97579 | 2025-05-31 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3dc3793b-cf42-3c36-9248-9b3c66724cc7 | -7.24138 | -43.0967 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 501052cd-f15a-34d7-b4de-c0d15cd2bb93 | -6.97811 | -42.78598 | 2025-05-31 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 122e5121-7b7f-344f-83c2-d4b0baffdabd | -7.21977 | -43.1245 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8785096f-87fc-3c9c-8b34-8d18d918b028 | -6.20601 | -43.33883 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b2b0b6b-1e64-38c4-a5ae-c4775f2b1b68 | -6.55578 | -44.49217 | 2025-05-31 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f68080d-5a37-390e-a0bc-e6235ef570ff | -7.57766 | -45.87159 | 2025-05-31 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa8196a4-616e-3029-80e5-a156bf4495e4 | -6.21159 | -43.33964 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17c07851-0b14-3515-ad6e-0717a3908b1c | -5.85757 | -42.83976 | 2025-05-31 03:34:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26265b38-ed58-31c8-8ad7-a6a8097c4bb2 | -6.82401 | -44.65378 | 2025-05-31 03:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4375bc2f-0432-3b86-90db-cc4dfb16a9d5 | -6.20179 | -43.3303 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53514613-8d3d-3f63-84eb-98d278708fd0 | -7.01079 | -44.62429 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca44b41b-f703-302c-934d-fe250b36a9b0 | -7.00792 | -44.62172 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a60a4c57-8351-36e1-8d88-ba9094992e54 | -4.98225 | -37.40322 | 2025-05-31 03:34:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 10a8c278-5db4-365d-aaad-434434a01836 | -5.84718 | -43.64233 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43960340-beb0-324e-8a1b-2a13e29aed14 | -6.15054 | -42.61717 | 2025-05-31 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 8b8d60f9-a15c-31c6-887f-3c5d7e88f01b | -7.22993 | -43.12984 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7dd0f53b-92b2-3c52-bd93-a5b5396d39b0 | -6.21652 | -43.34419 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 234169a8-24b0-3dd6-a461-f1e8615f8296 | -7.23721 | -43.08892 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 415523f6-b6e6-3c63-91b8-7c31e4084d77 | -6.82477 | -44.64962 | 2025-05-31 03:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f87ab66-5903-38c7-a1ab-095044662db2 | -7.0824 | -46.0496 | 2025-05-31 03:34:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c700cea-fe70-32d2-a8ab-f783718c5ab0 | -7.21793 | -43.13481 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| dae8417c-7e49-30a8-8fd9-55fbf28bf09a | -7.00348 | -44.61253 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0d35050-1a2c-30d1-b004-c3bfec33925a | -7.22393 | -43.13231 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9be866bf-e615-3077-b19e-e3ec7136598c | -5.85289 | -43.64331 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33ea7c12-9195-3bdd-8c18-2211e2cbad87 | -7.0071 | -44.61055 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6e19afe-4f50-3d3e-98a6-3a71aa263a69 | -6.97754 | -42.78919 | 2025-05-31 03:34:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 84e3d4b1-29e0-3149-929e-ff3204aa9b7f | -7.57865 | -45.86629 | 2025-05-31 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3ff6bd57-d358-3383-bb77-0a5027166492 | -6.34 | -43.38496 | 2025-05-31 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8887040-7e98-356a-90d7-2d6a79753092 | -7.58402 | -45.8728 | 2025-05-31 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ba68d99-4c57-38c8-a4a7-05c7839dfa25 | -6.21226 | -43.33587 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 56627965-41d9-3b4a-8244-16e53907e474 | -6.20112 | -43.33411 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c95e996f-8b49-3273-a196-3aa582dd49b3 | -7.87685 | -45.99021 | 2025-05-31 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fd384e2-89a4-3100-95f2-adcb8b1ddc6a | -6.22211 | -43.345 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0897c95-40e9-3848-84e1-9b3508ccd7a9 | -6.83084 | -44.65024 | 2025-05-31 03:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afc80c78-6bb0-36e5-9054-38bfa3eb4d4b | -6.33443 | -43.38408 | 2025-05-31 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61ac15b8-66e6-35b1-a5ab-3c8917f16987 | -6.15641 | -42.61485 | 2025-05-31 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 917010ba-e6f3-307b-afd6-4c964d67f74d | -6.15171 | -42.6104 | 2025-05-31 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| fda71ec3-3c98-3d99-b3bc-3f81b113f1f4 | -6.20535 | -43.34253 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e2e7db7-31b3-3a41-b0ea-7f85710166f0 | -7.22577 | -43.12201 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d175c6e5-1055-3018-b8ac-b71a039be370 | -7.21854 | -43.13135 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4122e6fb-2782-370d-aed9-5df3a85bdffa | -7.0055 | -44.61954 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 32a0fd3e-83fd-3a35-a2f3-8983aaf4da8a | -7.22932 | -43.13327 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c3a676c-6731-3f1f-b86c-02f7fb1a802f | -7.24675 | -43.09768 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5832daa4-9a6b-37ba-b83d-714626aabd15 | -7.24198 | -43.09328 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| dccc8e77-7b45-3a0c-8083-702ceb331de6 | -7.22455 | -43.12887 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e415ffd4-6933-3491-a5c7-b5aee7bb780e | -6.22147 | -43.34863 | 2025-05-31 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d350c3d-54c4-37ee-8175-7928a356f1d0 | -3.77447 | -41.60816 | 2025-05-31 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05affbed-29be-3a5e-a8cc-907a0ce8c101 | -7.22038 | -43.12109 | 2025-05-31 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81249970-82be-369c-96f4-5ecb3615f1c0 | -6.55658 | -44.48771 | 2025-05-31 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5184560f-a322-323c-aaad-df3ae3e156a3 | -7.00957 | -44.6128 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1838766e-f464-3073-8282-2eabd7b465d0 | -6.83008 | -44.65437 | 2025-05-31 03:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1fbc466-f465-3504-b80d-5f6ba2c09954 | -7.00629 | -44.61508 | 2025-05-31 03:34:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0872bbfa-6095-3b56-a9de-96456e60efc1 | -10.46003 | -47.94247 | 2025-05-31 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bcc5a2d2-a661-351a-bf19-108b5c54fe6a | -13.09384 | -45.28927 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5607cc5-b08c-32d3-b0bd-0589d038466a | -11.89802 | -47.45035 | 2025-05-31 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c6f6918-9a6f-3de1-8e70-b20845e70297 | -15.56205 | -42.5996 | 2025-05-31 03:36:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f1b2665-65b4-3458-866f-334f416b66bd | -13.08902 | -45.28426 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbeac2b0-420a-32c5-b075-b5a65e9a363c | -12.2733 | -44.59088 | 2025-05-31 03:36:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c611dce9-482a-3189-b260-4d5adc9e49fc | -14.61634 | -47.9715 | 2025-05-31 03:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c2a6dc9-93b8-3a34-99ba-0914d2b849d2 | -14.61765 | -47.9653 | 2025-05-31 03:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94019499-3e04-3bb9-9306-7d7922539637 | -15.56739 | -42.59592 | 2025-05-31 03:36:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 326cc670-d267-3fae-b256-5f02e1ca9da5 | -13.10573 | -45.28789 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac644e17-5519-31d7-9aab-78e5b645d93f | -13.09611 | -45.27777 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05808004-00db-3174-8763-a7cda5ddfd85 | -10.45874 | -47.94875 | 2025-05-31 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c959ce4f-e3e2-30e4-9e3d-55e190ba3904 | -13.10016 | -45.28666 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d43bfc-6b93-3950-a7c6-227bb267388a | -10.69653 | -37.04965 | 2025-05-31 03:36:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 597cf9f4-9e57-3e78-a067-ead4fe96323e | -10.4518 | -47.94753 | 2025-05-31 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37597fe3-59a5-3cee-b945-c8c3201e82b4 | -13.09941 | -45.29048 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93b26636-1e6b-309b-bbee-6e74e319c403 | -13.09054 | -45.27659 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88132a07-6aba-3e4d-b6e2-d31e5df55cdf | -15.56291 | -42.59504 | 2025-05-31 03:36:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf616d1c-21e7-3613-b5f9-605cf6b29894 | -11.68764 | -48.26318 | 2025-05-31 03:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34fb779d-e374-3524-8fb5-34531122fb87 | -13.63446 | -47.44852 | 2025-05-31 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a501adb-8546-3a23-8877-914966423765 | -13.09535 | -45.28161 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82a7a8b6-431b-3684-93b7-ccc88956231e | -13.10498 | -45.29169 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ac4885f-c53b-31b3-b90a-4e05ac8d8248 | -12.26791 | -44.58965 | 2025-05-31 03:36:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14772050-d8a9-3db1-87d2-2919ab8b43b9 | -13.10091 | -45.28286 | 2025-05-31 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
