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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4d040db-1cad-3cae-a15a-7047853cfe23 | -3.40111 | -49.70474 | 2026-09-17 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86032e85-cccf-3857-9f1e-634aa7ef4d84 | -3.54761 | -48.17758 | 2026-09-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7c3e293d-8d73-3d16-98f0-9ae87db1523a | -3.47847 | -54.70332 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c75d1bce-a46d-30eb-a8f9-3f6f1d654aaa | -4.5507 | -42.94574 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 143f670d-a0db-33bf-853d-b4ff19c32616 | -3.37861 | -50.45671 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ab221e8-e32c-36c0-bf96-9456c672ac72 | -1.79615 | -52.18243 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5646e0ba-cb20-394d-8fca-9a6e4131cb9f | -3.48144 | -54.71187 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2a7a8737-92dd-3618-8ded-874d5995b43a | -3.03318 | -51.22691 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eed1fac-2569-3667-9459-c068db9b8746 | -1.20113 | -54.21643 | 2026-09-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05ee18fe-f3e5-3035-bd5a-2e13ca4ba247 | -3.04744 | -51.27234 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 943f3656-814d-30d8-8e57-0abb89de1e5b | -3.47434 | -54.703 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a0d346b-7274-3119-94e8-b5f6e5a3126e | -3.50525 | -53.20986 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f917f517-b241-3c4a-8192-3fa0ae960675 | -2.96257 | -50.33337 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b8f9e6a9-76b3-3b28-96f6-19d188345f0c | -3.1751 | -48.58312 | 2026-09-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7350499-6f70-37da-9795-5292bf97fe94 | -3.17108 | -53.92912 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98e008c2-0a38-3b58-8b03-db539699b4a6 | -1.83758 | -54.92157 | 2026-09-17 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 246c388d-0cf9-3bfd-86c1-558dd106f9da | -3.4766 | -54.71511 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 78d24137-f91d-3510-9f2a-06845ee9e734 | -2.94565 | -50.46368 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e194078c-533e-3fd0-9579-ac013af22272 | -3.3758 | -50.45259 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f8285f4-58fd-3a58-84eb-8229647da287 | -2.96369 | -50.32619 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 838e6e65-f2f4-3091-9e4f-0c53dd747726 | -3.28121 | -48.79648 | 2026-09-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13ed3598-10b1-3518-8197-b7017094ea2e | -2.89901 | -54.17277 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6de40ded-1ba4-3456-aaf6-50800876adc1 | -3.27293 | -54.25898 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ef9f88c-f3c3-36f9-8f1c-b6831e84fd7e | -2.90902 | -50.43209 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c29186b-2dda-3ff5-8906-817c08c98b86 | -3.76272 | -51.14053 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10923195-494a-399c-9474-056075dd0855 | -2.91187 | -50.41402 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d874467e-9af1-34f9-aa90-7daf41f1e599 | -2.89842 | -54.17647 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a0e6507-e68a-3628-9d12-9f64c2990548 | -2.89326 | -50.42225 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d543e1a7-ba60-3d6e-a8f4-d1b656ad7f30 | -2.91582 | -50.41094 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57c8844a-61fa-3ee1-93ed-88f64af053a3 | -2.82408 | -51.34122 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66dc1463-8b83-3857-a8f6-cfcfb075fd78 | -2.90454 | -50.4166 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d746d2f4-6132-39b5-a313-87a73afa7251 | -4.81002 | -42.89355 | 2026-09-17 04:38:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 29381ce0-02e0-362d-a81b-c7e4fd09dd05 | -3.09212 | -51.29494 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b47b9d4-cf55-33e5-8b7a-69bc098e7f4c | -3.17165 | -53.9255 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a1de007-89b4-3803-a15c-e17c14003764 | -3.04396 | -51.2718 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3b5accb-781c-3b15-b1e0-58ade199866f | -3.84764 | -51.76838 | 2026-09-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 708251b6-d285-3f80-833d-068803603cb6 | -1.03054 | -53.74203 | 2026-09-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b717dde6-7342-39a0-af1e-014feae39038 | 2.71082 | -60.30016 | 2026-09-17 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf70a818-4a15-3f64-abe1-1c015cc4abf9 | -1.02347 | -53.74012 | 2026-09-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eb8968b-2991-361c-8538-614843d46f96 | -2.10632 | -52.04545 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c0a78ba-0f8b-3e4c-aa7d-539128f84957 | -2.91304 | -54.18343 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee3eb535-f4d9-3846-98c0-5f15c51b8bc2 | -4.55009 | -42.94999 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d963163b-ce43-317e-9729-7503b1396b97 | -1.81789 | -54.93163 | 2026-09-17 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf2783ae-8d6f-37af-802d-082e5a8108f1 | -2.91365 | -54.17971 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3e06b0e-f9df-34b2-bab2-fc9aabcd8bc2 | -1.03998 | -53.73567 | 2026-09-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3010bee-5a19-3c98-a0d8-436bd53dafc2 | -2.90511 | -50.41298 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b91cb380-e78f-3ba6-8c9c-7ca9b5f14560 | -4.33638 | -46.61656 | 2026-09-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ab0edfc-e066-39ed-b75c-b2bf1628a694 | -0.58746 | -50.54959 | 2026-09-17 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3abc9b6a-ea48-3170-9325-ae3d644800a8 | -3.48091 | -54.68789 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b0575df-c187-3914-9402-1784bf9ee272 | -4.50552 | -48.31541 | 2026-09-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc4605ef-fc20-3034-aff3-dc7d34bed726 | -3.48016 | -54.72008 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e78bd98-5d66-37b9-9604-561ac6f7d499 | -3.50908 | -53.21048 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38baa5eb-9ff9-3ff4-bd94-346f9c46dc67 | -2.8236 | -49.24201 | 2026-09-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbdcb3fc-9f05-3ab7-97a3-4b2028a9dd73 | -3.47363 | -54.7065 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93cfd064-fbb7-31c4-9f4a-da1d4f09263a | -3.0297 | -51.22636 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41c8fb9c-5af0-3511-96e9-c833ad9af854 | -2.91806 | -50.41869 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59953b5b-8e67-3d63-8a6f-edc8f904aadf | -2.91244 | -50.41041 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d5eb886-b649-3b3c-9b2a-4070178c29e2 | -3.46878 | -54.70978 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01c5d3a4-3ff5-3bb6-91f7-4be48b969299 | -3.47724 | -54.71157 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f4ac7f9-5b4d-3b7a-85cf-3052a8a74765 | -1.34633 | -55.84735 | 2026-09-17 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38f6cf68-96af-3999-aea1-42ac317d5bf7 | 1.25714 | -51.00348 | 2026-09-17 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a1b4851-b415-3071-923f-c8eaa891e595 | -2.95807 | -50.31799 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52397c2a-92f1-34eb-b66d-c5b22e4797fa | -3.02263 | -51.33966 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ddbd40e-c9ab-3ae1-837c-f392bf713503 | -3.506 | -53.20506 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11e536e0-a47a-37ce-a1fe-126592ff7120 | -2.62562 | -49.11551 | 2026-09-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a288dee9-77df-3b22-9960-e0d09ba21494 | -2.91468 | -50.41816 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b844ae7-dda8-3a89-953c-1432c2bb37d1 | -3.50426 | -53.20742 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e657941-e356-3080-a870-59c48381b51c | -2.89211 | -50.42947 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52467f56-c1b5-3fa3-b0aa-8dfe46d937cf | -2.89097 | -50.43669 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9589457a-da2c-3868-a3ee-fd215d25ce9f | 2.71839 | -60.30502 | 2026-09-17 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c9074505-43d7-35e4-969c-495546438f64 | -3.48146 | -54.71225 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 64acba2c-a1ec-357f-be24-cc3e3d944a29 | -3.8404 | -49.09547 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf306060-9bc6-36e8-bd4c-aab2517b1c75 | -2.89549 | -50.43 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e03b5bef-50e9-3fb3-bff6-5855c89231f9 | -2.90735 | -50.42073 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c1c09de-8e02-35ba-b958-43ea613ef670 | -4.36268 | -47.78405 | 2026-09-17 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0d872a4d-0e90-3bb4-aebd-b6cad4bf2253 | -1.18674 | -53.38479 | 2026-09-17 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06397120-e4de-32b2-b31f-f109bb540ca0 | -3.03023 | -51.33682 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e526608f-0e19-3653-afbb-ef1caec60eda | -2.91528 | -50.39238 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d5f136a-1b8d-35b4-b0d1-e4198b480763 | -1.34809 | -55.84598 | 2026-09-17 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa7b6428-f25c-37c9-b462-6c88c7f16a86 | -3.81913 | -50.63271 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfe262c4-0ef6-3cf9-85a1-877f3bfe8d4f | -2.96088 | -50.32209 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0defdfda-55b4-3190-bdbc-6a1f20933feb | -3.47548 | -54.69489 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9a2b934-2d20-3003-90ed-051663a2ff74 | -2.89045 | -50.41811 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0df40722-2baf-31d7-b8af-2936b225eedc | -3.48081 | -54.71617 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1acd0a11-060a-33e3-8958-339521614197 | -3.33723 | -54.1723 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a198e43d-9607-362b-8327-bd6bdc009961 | -3.0493 | -51.27259 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef75dba5-1e07-33da-b712-de29c829f046 | -0.16433 | -50.40496 | 2026-09-17 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd3b1146-937d-3087-aaf2-84c12201aeef | -2.86143 | -48.67462 | 2026-09-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbb73bd6-f9dc-330c-8ca2-db22e4551be8 | -3.47487 | -54.69874 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88fcd3e5-0a1e-3a12-aac7-2d7ab85f5e99 | -0.91631 | -47.20766 | 2026-09-17 04:38:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3c321a4-5925-3398-aeeb-32e8331ce7e3 | -2.91411 | -50.42178 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a76c1f25-734d-3441-b0c3-a131f4354a7e | -2.77515 | -51.37033 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2744e259-75a2-3d8a-9e97-82a609605db8 | -3.48269 | -54.70402 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 526661b1-55d3-3f18-9f2c-87b056926225 | -2.09699 | -52.05711 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03af907c-d1a0-3bf6-9bcd-f5ec38ec4324 | -3.09274 | -51.29108 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b233aa-f799-3874-95eb-4fd478563b9a | -2.10565 | -52.04971 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bfe02fd-5c2d-3e6c-a7eb-79e75a11d9ac | -3.08071 | -50.56967 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1df41c3-fa46-3ce2-be49-5bd809a4d20b | -2.88987 | -50.42173 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4154c0bd-90e8-307b-a4e6-750ffb3ec22e | -3.70819 | -51.10879 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b8e37d7-7c56-3b6e-8a92-f028ff2e7a38 | -4.36322 | -47.78046 | 2026-09-17 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README35.md)
