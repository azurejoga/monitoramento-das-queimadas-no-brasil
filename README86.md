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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4935f301-a42c-3bed-aad7-692f3e3fa909 | -1.71124 | -55.77101 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2620d66-fcbf-3c85-8cb2-a9e86d325e32 | -1.60874 | -55.46261 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80cf779b-529f-34be-8d2f-e265d73658a3 | -1.59341 | -55.89161 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9beede61-d398-37b9-bf9a-9fe1a46aad51 | -1.5755 | -52.16031 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a5cc001-0d43-3317-b082-459069d12409 | -1.57486 | -52.16446 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c5a11ed-00fc-39d1-ba52-9859c970e998 | -1.57422 | -52.16864 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03c4288c-af4e-31a8-8abe-9284af1f6641 | -1.57157 | -52.14695 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c512d25d-528b-3f2d-9b5c-7bf76455273a | -1.5703 | -52.15522 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f45ff00d-4e2b-3a15-aa2a-f1e2261405bc | -1.56966 | -52.15939 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67ba93a8-8058-36d3-a4d3-924289f20e94 | -1.56657 | -54.20615 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13b81a59-b582-3232-85f2-883329c15bb1 | -1.56611 | -54.20916 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 311dbf85-0dbe-35b1-b7d2-a1a739ae4813 | -1.56146 | -54.20547 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43eac289-dd17-3524-9f92-5e3a744e1967 | -1.56101 | -54.20847 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f7502ac-62e3-34d2-a4c4-cc63d602837d | -1.5391 | -54.28409 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80aef266-a568-380e-9764-1ebdfdb8aebe | -1.53865 | -54.28703 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f0608b3b-af07-3103-a8f6-b5285c80e0cf | -1.53402 | -54.28336 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1b06481-4c56-3825-84f2-94942725d3b6 | -1.5325 | -55.41398 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 802c4e44-7dcb-3244-b0b7-3793180195f1 | -1.52859 | -55.40829 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77fb8ace-f534-3b94-9477-94b1cd240a02 | -1.52782 | -55.41322 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3edf6fbf-63fd-324a-918a-7ea940e77efe | -1.51687 | -52.11782 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa353640-e697-30fe-9d47-bf0548a9b1df | -1.51622 | -52.12199 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1d0ac2c-3b89-30fc-8543-9f785af40003 | -1.5162 | -52.11713 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15711fed-67f9-36ea-bc84-9522c2bd19fc | -1.51557 | -52.1213 | 2024-11-03 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b36371f-1ada-36cd-ac76-e8c11f74559f | -1.50424 | -54.28412 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78f5d617-56e3-354e-86d0-c9a1f8f1ec1d | -1.50317 | -54.28175 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c776c95c-6234-30f0-946e-24c617e673b4 | -1.50269 | -54.28493 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aeac918a-3f76-3e41-92ff-fda2c4c09f2f | -1.49918 | -54.28336 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ca9cfe5-811a-3481-a337-834df5e4249d | -1.49868 | -54.28649 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f43fbe1-b037-3903-9800-5168f7d7e782 | -1.49729 | -54.29538 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25698265-4c6d-3adf-9d91-8d7fd0ee7df3 | -1.47535 | -55.50522 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7320822d-0bc2-3fc6-97ed-cba1675f6101 | -1.47069 | -55.50457 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 634a8fc3-2113-38af-aec6-2a1c7137336f | -1.45976 | -55.78893 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa3b7f29-ed7c-349c-a296-5724dc62780a | -1.40441 | -52.19136 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ad07234-ea55-3952-b5bc-53c77f3626ed | -1.40376 | -52.19547 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7078b254-f314-3caf-a705-b39e077c239a | -1.40362 | -52.194 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2db1141a-8975-394c-94d5-baa52ff680c0 | -1.36789 | -51.96296 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 65022166-c7e7-33bc-8025-b132c948c741 | -1.36725 | -51.96717 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a84f48e3-faa5-3ac3-b415-fdd1ed9d2b18 | -1.36424 | -53.60043 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 628cb15d-1ee1-39a0-862e-104a5d353264 | -1.3637 | -53.60386 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c60d640e-ae00-3133-a293-02e6be34ad16 | -1.35925 | -55.46499 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0260fee3-94df-3823-a295-92e41902dd89 | -1.34655 | -55.79179 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ecb7951-c174-379f-9e77-1b71eefb6ada | -1.33958 | -54.61258 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97b1cae9-3d43-3d7d-9c75-ba32db54dc83 | -1.33686 | -54.60837 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cedc57e2-21b0-3736-8802-72b970b1adc5 | -1.33601 | -54.61403 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a54eaf5b-6248-3f54-84ea-055175a7f276 | -1.33467 | -54.61168 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac9f4be0-9e02-3b37-b752-13a502891e79 | -1.3254 | -54.6386 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ee83ace8-093a-347f-a1a5-ac37508321e2 | -1.31761 | -54.22412 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8ff79a81-8260-3e22-a861-b0fecea7df77 | -1.31253 | -54.22339 | 2024-11-03 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cadc13ff-f05b-3018-a044-561ee5b63b70 | -1.30608 | -53.45838 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4b449c5-1ca6-3afb-9ba3-7fe52807c232 | -1.30465 | -53.45573 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 775e6c75-7f6c-323a-8e84-4c741632c44b | -1.30416 | -53.45902 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6708c4fb-f9d2-3523-b5ae-90b6a996fe52 | -1.30073 | -53.45763 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14f77107-641d-3082-92e0-6d79dbdf9107 | -1.29755 | -55.74654 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a689be8-99de-361a-babe-bc8cacd796b2 | -1.28225 | -53.40056 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37c01926-9d68-344b-b811-da4617ff0b6c | -1.28172 | -53.40397 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d241c89-3774-3ef5-a8e2-af7d7ae63ab9 | -1.2812 | -53.40733 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2ffc61bb-034d-3849-acdf-eeadea42efb7 | -1.28068 | -53.41066 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cae15cfd-d5d9-319a-9af1-f3beea692b60 | -1.28016 | -53.414 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 551a7f8d-ef38-398a-bd94-d44095d07771 | -1.27895 | -53.38647 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e341e6e-c764-33c3-928c-cb332ef5c7b5 | -1.27792 | -53.39309 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12b4b62b-0690-34e5-b559-d44f84d61c8d | -1.2774 | -53.39645 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 885bf1f2-1475-3346-955e-bee46c787de9 | -1.27687 | -53.39985 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4dda5eb3-d598-3d18-85ad-23cb2afe40d4 | -1.27635 | -53.40325 | 2024-11-03 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4a85365-94b2-3f65-b7b5-e31a809c1ef6 | -9.10017 | -61.7439 | 2024-11-03 05:33:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11074a7b-9efa-3ac3-8082-7e2def85d01a | -4.78893 | -55.70648 | 2024-11-03 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae559553-f6b1-32eb-8b4d-c2d42316493a | -4.53644 | -56.1237 | 2024-11-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c5acaf14-7f26-37d6-bc5f-a98b1d2ebc84 | -4.53561 | -56.12925 | 2024-11-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5b6dba4d-79af-3222-a4e0-143e454a3b06 | -4.4138 | -55.3988 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac17f5de-91c5-385c-b700-d023745cb48b | -4.33357 | -55.31689 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ec83391-cf92-3287-add2-94088dbbe78e | -4.33274 | -55.32253 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 346a4c9b-3936-3e75-abe9-9d7917a38f52 | -4.27195 | -55.14391 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2c9cded-adc0-3c8a-9d34-9ff68b1e1d9c | -4.27152 | -55.14681 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e0343bc-9843-3a38-a149-28aec9009d45 | -4.25504 | -55.51146 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 352bd07a-eab9-3d07-8db2-ea87b47ca791 | -4.24242 | -55.86422 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5004bef-b54d-3975-aa72-bf5c852f77d5 | -4.24167 | -55.86924 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cbff848-9c31-3ae5-bbb4-c218939bfede | -4.22391 | -55.05462 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2130207d-1706-368e-af88-b31d7153a686 | -4.17936 | -55.59618 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9427952-5cc7-369e-9812-84e61f38671e | -4.1149 | -59.9215 | 2024-11-03 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21938608-8b11-335e-ac72-a694aeb16a5d | -4.06957 | -55.5453 | 2024-11-03 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 46cc8e54-2207-3b83-b96e-bd0f405ebed0 | -4.06474 | -55.54456 | 2024-11-03 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bac78b9e-1e5d-3b0d-b6a4-a64a5ffb9cd7 | -4.01657 | -54.80139 | 2024-11-03 05:33:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9fb8ec08-f137-39ff-bca7-e69c7cab0a2d | -3.98844 | -55.73115 | 2024-11-03 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00202368-475c-3110-9c98-c1f439818389 | -3.98726 | -55.73392 | 2024-11-03 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76c1a925-ab1b-3f92-b484-b36a1f1e210f | -3.92315 | -55.38379 | 2024-11-03 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bd10bb9-fce3-379c-afdf-60170c7add91 | -3.85872 | -55.98126 | 2024-11-03 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21964830-bc72-3521-9cdd-ebdc668e6998 | -3.79614 | -55.64077 | 2024-11-03 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 966a7213-9c38-35d2-9033-223d23339053 | -3.73485 | -54.06661 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbc82321-4c4c-3ce8-be09-3dd21277c394 | -3.73438 | -54.06978 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c761bbb-70d6-3ae5-8b68-453cf41223c5 | -3.68389 | -58.50994 | 2024-11-03 05:33:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8607cb8-a871-3b9c-be9e-0fc47e7fb4bd | -3.62661 | -53.96314 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d7b6986-efaf-36c3-b5e5-2e8b45f9a5ac | -3.62614 | -53.96633 | 2024-11-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e388092-1edd-3f61-938b-cc18f7aad3c4 | -3.60837 | -49.32537 | 2024-11-03 05:33:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd4c6c54-8a39-30fe-b15c-6e02c3bff181 | -3.6055 | -49.31909 | 2024-11-03 05:33:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c64e9bef-cade-3afc-a710-39d35c19d8ae | -3.60454 | -49.32597 | 2024-11-03 05:33:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 25fd3fa4-0a90-31ab-bca2-e5856579a732 | -3.60219 | -49.31771 | 2024-11-03 05:33:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1604fa3-1c43-3fd1-88be-1b4503d8b3f9 | -3.60118 | -49.3247 | 2024-11-03 05:33:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1f2873f-0be1-367a-a54a-2f891d84ca30 | -3.58621 | -54.56238 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b549a14-ce2f-3d7d-b6c2-88f99177ba30 | -3.58107 | -54.56166 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be536bea-e9ba-311f-be7a-ce1d486f1235 | -3.56378 | -54.64243 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59b9086f-4914-3574-bf8f-2b1a470fc64a | -3.56334 | -54.64541 | 2024-11-03 05:33:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README87.md)
