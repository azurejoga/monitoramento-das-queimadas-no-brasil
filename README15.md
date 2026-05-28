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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b75d695-620c-3c5a-a1d2-c8ccbab74fa0 | -13.20923 | -54.50686 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6089274-3e8b-39f5-9cac-25373f420c42 | -11.47429 | -52.9189 | 2026-05-28 05:33:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c147902e-0e23-33bf-b3c0-02b96b23a3be | -11.07597 | -55.05569 | 2026-05-28 05:33:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cce31db-359a-3fbc-ac52-f23455bb6ea0 | -13.22685 | -54.49519 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eae9677-9ac8-3109-846f-083ac9a8ec54 | -10.90997 | -54.12015 | 2026-05-28 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 671b72d9-b297-3d9f-8325-3963898a5d0b | -10.03223 | -59.35022 | 2026-05-28 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fd9029d-89e9-3193-88bd-f6e267f0d3e8 | -13.22642 | -54.49857 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57250edc-8561-3e0a-80ff-bce690730e2c | -11.80123 | -57.3521 | 2026-05-28 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27ee48fb-a632-3aa4-9caa-eddccb9d92d1 | -13.22032 | -54.49448 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db3ded42-855e-3ce8-b196-8fc36c08df7c | -11.78867 | -57.01093 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0963084d-3e42-3c62-aaaf-fda16c28f2cc | -13.64244 | -55.75125 | 2026-05-28 05:33:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f179fd40-dc4f-31c5-a19b-18f4bdcefaa4 | -11.73093 | -56.83955 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c21668c6-e6ab-3460-9f80-0a23bc36bf61 | -13.21992 | -54.49789 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 956ffd41-bb1a-33e1-8e23-ee4c4fcf7704 | -13.20797 | -54.51685 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6967c1a-9054-3dc0-b0db-c7bce6444683 | -12.72625 | -54.19236 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14d9c217-3f6c-372c-ac19-5e88092051f9 | -13.19739 | -54.51547 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14512e6e-00b7-3b5c-b92a-70d8c86c974b | -10.44558 | -59.43194 | 2026-05-28 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c76792e-bbc4-39f5-a976-a8d1c07fec1d | -11.27568 | -53.96687 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d952bcb3-664f-3f66-b251-7aab0d786078 | -10.0497 | -51.68208 | 2026-05-28 05:33:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3c66e93-5f32-330b-87f3-9ecf22efbb92 | -13.20771 | -54.51012 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56c911e3-dee1-3333-a624-926ab708e6fc | -12.72046 | -54.195 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d69ea38c-3931-3da4-a1ca-53d106d4fd19 | -13.20692 | -54.51678 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 203ebc70-4632-3a46-bd80-c7685586c5e7 | -16.26779 | -60.00669 | 2026-05-28 05:36:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10bad2f2-d30a-3afe-91d6-4d373ae7f064 | -17.937 | -51.33417 | 2026-05-28 05:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0ab7489-eb74-33c4-9131-775146aeb1dd | -16.23347 | -59.98422 | 2026-05-28 05:36:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88a6349b-6171-3b8e-95e3-01780e322949 | -17.9313 | -51.32096 | 2026-05-28 05:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b50951db-f793-346a-be3b-281793a626ba | -6.98987 | -42.87568 | 2026-05-28 05:36:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.1 |
| 3fd90a06-bbe8-3ce6-9781-c862dee2a52c | -7.00054 | -42.86979 | 2026-05-28 05:36:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| b35be159-ae8a-30b8-a0a8-9f4aadc6d53c | -21.98402 | -57.60468 | 2026-05-28 05:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9f697e4-34a0-394f-96ac-5f4df9e92f5f | -17.93017 | -51.33358 | 2026-05-28 05:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 455e471e-6542-38d1-bb16-c2b14555a187 | -17.93073 | -51.3274 | 2026-05-28 05:36:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7974220-a2f3-3b38-a021-00352529e60f | -16.21691 | -59.66891 | 2026-05-28 05:36:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf4ba1b2-e579-3eda-807b-27865977e543 | -16.21759 | -59.66381 | 2026-05-28 05:36:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dee45f8-82b3-36ff-8c89-e419596bcb4c | -21.97914 | -57.60435 | 2026-05-28 05:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 913a0abb-c224-3663-83b6-129939813034 | -16.26602 | -60.004 | 2026-05-28 05:36:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6198f60-6a63-3eef-bbfe-eae6431561d1 | -13.2189 | -54.4975 | 2026-05-28 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 40603077-fd38-3de4-a18e-991edb596a72 | -11.591 | -47.4496 | 2026-05-28 05:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| bc6735eb-39c4-38e0-905e-3c2a2d3a5ad5 | -10.6292 | -46.9021 | 2026-05-28 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e87a9f22-d5da-3cda-baec-f096802dd252 | -11.591 | -47.4496 | 2026-05-28 06:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 87248019-c9e1-3dd5-ac90-2b4a6e590f4f | -10.6102 | -46.9044 | 2026-05-28 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 8f282fc0-33b7-303e-a48c-573f06826abe | -11.591 | -47.4496 | 2026-05-28 06:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 294a64aa-cb11-326d-9343-6105ac1851d8 | -11.591 | -47.4496 | 2026-05-28 06:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8e71af7b-1c53-3f87-9566-d810ea8d896e | -11.591 | -47.4496 | 2026-05-28 06:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 67730bf3-5453-309b-90e9-8143cc67f933 | -11.63065 | -56.85787 | 2026-05-28 07:14:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 06535058-9ea1-3770-8c11-e6e283a7a361 | -11.591 | -47.4496 | 2026-05-28 07:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5086a474-a8a5-36c1-b380-ac3d6cc5dbe0 | -11.591 | -47.4496 | 2026-05-28 07:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c40d7c4f-4898-381e-9953-554542ef6547 | -7.6287 | -68.5278 | 2026-05-28 07:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| bd4e6004-9db4-39da-9ad2-23fc54726150 | -7.6287 | -68.5094 | 2026-05-28 07:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 10dfafab-61cf-3fb2-a759-bdb403007fc4 | -11.591 | -47.4496 | 2026-05-28 07:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 594e5c30-0639-349e-b4be-155b0e231b3c | -11.591 | -47.4496 | 2026-05-28 07:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4ce76475-31f2-337f-9638-4a471879e220 | -11.591 | -47.4496 | 2026-05-28 08:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 05e3a7d1-bfe4-3b48-9bf8-65dd8a2b4b32 | -11.591 | -47.4496 | 2026-05-28 08:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 585b05ad-372c-33bf-9808-abff43e8d4b7 | -8.854 | -46.7005 | 2026-05-28 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| d2619d11-ad73-3404-a7ec-a4f1942adfbc | -8.854 | -46.7005 | 2026-05-28 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| afed6ac2-e5e3-3da9-94b1-88a4de4d469d | -8.854 | -46.7005 | 2026-05-28 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| c1f905b5-780c-3cb7-8db6-871a4033f9f8 | -8.854 | -46.7005 | 2026-05-28 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 2c1c0187-3763-3108-b361-2184b6f4778d | -8.854 | -46.7005 | 2026-05-28 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d96b6dae-c5c3-36d8-8c31-373bedeaea22 | -8.854 | -46.7005 | 2026-05-28 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ac65d5e9-fa66-355a-bfc7-c532ddfe6276 | -8.854 | -46.7005 | 2026-05-28 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2e2afb30-b524-3bb9-896b-fba7e021373f | -8.854 | -46.7005 | 2026-05-28 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 89da3b85-a331-3de3-bcb5-936133c361b6 | -8.854 | -46.7005 | 2026-05-28 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 9c384b3e-8cdb-3242-a18e-2c89c1d9ac18 | -12.7272 | -54.1988 | 2026-05-28 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 570e6020-8085-39d5-be46-1942c3dc4d2e | -11.28006 | -53.96919 | 2026-05-28 12:34:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8f60750a-b6db-306e-a46a-8401a90f1a54 | -13.20933 | -54.50773 | 2026-05-28 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| e71d2aad-aa0e-300a-8238-224350f3f891 | -11.80855 | -57.35221 | 2026-05-28 12:34:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2eafeb3e-9ff1-342c-8289-86a0e1bc8827 | -11.48172 | -52.91703 | 2026-05-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 967007f9-1de1-31c3-85b0-d3335e0c215e | -12.71983 | -54.19118 | 2026-05-28 12:34:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 5c443d55-0942-3e1d-af0d-4dada2b4a43b | -8.16836 | -47.71754 | 2026-05-28 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8a7e1b9b-8732-3b51-b45c-1a57b79132bf | -8.53649 | -51.56879 | 2026-05-28 12:34:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c0149eb7-71c1-31d3-829f-739305545ac3 | -12.54634 | -54.59187 | 2026-05-28 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 1ad9d272-b7b9-3975-99f0-ec4046515202 | -12.54319 | -57.16716 | 2026-05-28 12:34:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2c5225db-bce9-3d83-a0fc-c675331891ee | -12.5419 | -57.17631 | 2026-05-28 12:34:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| d0dfe08d-cb48-350f-8b34-94540bc18e7a | -10.49157 | -48.89846 | 2026-05-28 12:34:00 | TERRA_M-T | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 7f4dc744-618f-399b-be74-87b588c88a32 | -11.59896 | -55.33445 | 2026-05-28 12:34:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d17966b5-0f10-3296-8202-6d49eaef0847 | -8.8519 | -46.69197 | 2026-05-28 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 0575ba4f-cb4d-354f-8df6-521e9bc4ea48 | -8.85274 | -46.69722 | 2026-05-28 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 8a735c04-7899-3cce-8e67-c48fca5b8d82 | -11.41072 | -57.80937 | 2026-05-28 12:34:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| c201f973-5781-3bdf-96d7-19a57e9e7ea1 | -12.54062 | -57.18544 | 2026-05-28 12:34:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| aad74a56-5241-3dfa-a5a6-e5d8762f262b | -9.60842 | -58.33919 | 2026-05-28 12:34:00 | TERRA_M-T | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a983d7ed-a0b6-33a4-b1de-a9337c49207b | -11.60038 | -55.32402 | 2026-05-28 12:34:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cbf344e6-03ab-3949-a20e-4c04e816ed47 | -11.63792 | -56.85616 | 2026-05-28 12:34:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c6cef4bf-a8ae-39d4-a10c-a80c5f9fd7e6 | -11.79148 | -57.01104 | 2026-05-28 12:34:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3d0216fa-9c06-3cd3-ab3d-269890eb84b5 | -12.54527 | -54.59819 | 2026-05-28 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 958dcc42-2731-3432-b4de-e2a70f8bf273 | -12.53934 | -57.19456 | 2026-05-28 12:34:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 89b2c8f1-2169-3dcb-ad99-23d941652981 | -10.37359 | -52.53475 | 2026-05-28 12:34:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1cf3c6a6-8e35-38bb-aee7-10410d7f3d26 | -11.80038 | -57.0123 | 2026-05-28 12:34:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| d437503f-043e-3bb0-ab65-2356f8cabd28 | -10.47696 | -48.91989 | 2026-05-28 12:34:00 | TERRA_M-T | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 23acb7f3-cbe3-3eaa-8b06-9679245e3a0e | -11.48122 | -52.92365 | 2026-05-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 78b1ce5a-0f0b-3f88-80fc-1342b19c66cc | -12.7302 | -54.19262 | 2026-05-28 12:34:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| e859c2fe-5cab-3f64-808f-28ed434d2d79 | -11.412 | -57.80044 | 2026-05-28 12:34:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 68bdc246-9678-3f3d-9a2d-dc5c177f1441 | -10.48046 | -48.89011 | 2026-05-28 12:34:00 | TERRA_M-T | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 762a16be-2b1e-3ce9-9d93-163267381c37 | -8.52858 | -51.57837 | 2026-05-28 12:34:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e32711fd-b66d-3202-ba7d-51942c41329c | -12.71823 | -54.20379 | 2026-05-28 12:34:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 6359528a-77f5-3446-a4cb-f67785a09b71 | -5.09728 | -48.39358 | 2026-05-28 12:34:00 | TERRA_M-T | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| db9f4707-e694-3b7e-8acc-aabb003251bc | -11.63664 | -56.86531 | 2026-05-28 12:34:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 94c6b9d0-ab78-377b-9520-ea992061b6d7 | -13.56915 | -59.82906 | 2026-05-28 12:36:00 | TERRA_M-T | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d3e99f6a-16fb-30e4-839a-8df59c99a279 | -21.29083 | -56.87303 | 2026-05-28 12:36:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7f987ce1-28a4-3ff2-8533-15f99156e6f7 | -18.08502 | -52.63699 | 2026-05-28 12:36:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 65ad4719-9d50-35c5-80c5-76ea36254e76 | -17.52814 | -53.68929 | 2026-05-28 12:36:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 79dc1ac3-9f3e-3431-b5f1-5f8d79e1fd4a | -18.08521 | -52.64364 | 2026-05-28 12:36:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |


[Clique aqui para ver as próximas entradas](README16.md)
