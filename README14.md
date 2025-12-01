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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e7ee992-a43a-3841-b1cf-e0c929ea7e56 | -2.44749 | -47.0842 | 2025-12-01 04:25:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a01eb1ad-6c02-38ac-ad56-f0c91cd5bcf3 | -2.48864 | -48.17699 | 2025-12-01 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee824e40-037d-3085-860c-2356b547735d | -5.23967 | -41.23783 | 2025-12-01 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3e158dc-4f8b-323b-95ef-96a5290c9356 | -2.16966 | -46.45369 | 2025-12-01 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec1ec27f-f825-3da8-915e-0db8fd3b2f00 | -2.17403 | -48.4215 | 2025-12-01 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3917338-f8cc-32ee-a912-7edc9b8366eb | -3.32472 | -45.63932 | 2025-12-01 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c408c8d3-74a5-334d-acba-537e0a0d68c3 | -2.60786 | -47.77393 | 2025-12-01 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91312767-9115-30cb-96ef-a51c3b6c6a2a | -3.59247 | -47.27406 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7353b66d-c652-3a63-8537-195638bed95c | -4.37842 | -43.1506 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d0502a76-eba7-3be2-a9af-7ad45acc4815 | -3.23639 | -50.25274 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9565c63c-804c-39d5-b085-c3492cf4d013 | -3.4121 | -52.83387 | 2025-12-01 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bd1f6bd-753b-3c2c-b981-07a2c8dae6f9 | -3.60751 | -50.36695 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| febffd90-f5de-3cff-9828-e4aa9b335156 | -4.37516 | -43.33831 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8135d661-af9f-3443-b462-e845d87989dd | -1.35151 | -53.2259 | 2025-12-01 04:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8d3c4cd-eeeb-31a0-9bc0-4a7c0cdf6f61 | -3.35836 | -50.48852 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74adf6e7-187a-3538-ab84-076c585dd298 | -3.22276 | -50.57888 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2c30f468-308d-388d-ae1f-24ff4412432a | -1.41079 | -48.96183 | 2025-12-01 04:25:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3135860f-a461-3b15-85da-53038e7698b3 | -3.60095 | -47.26432 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c406c60-cde0-32f2-8e7c-a9b5dbf9a1fc | -2.73744 | -49.34858 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9709ea32-f09e-3ce6-8519-ba873f854df5 | -3.42986 | -50.32342 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5697b5ba-ec9e-39d7-b02f-d788e9c6151b | -4.38396 | -43.32769 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38106752-49da-305d-85bc-cc9b1dce323f | -2.87473 | -48.70209 | 2025-12-01 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 989ed28e-492c-3c58-8b5f-5a3083a287a0 | -4.38627 | -43.33608 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fb37e7c-ea83-3d14-9ee4-9a7436c3fa4b | -3.59922 | -47.27518 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 798c811f-b994-3be5-a066-caf8f4ee4e5d | -4.38217 | -43.33942 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5842f694-d278-34b0-93c2-4fcc4e55d6bf | -4.14364 | -43.73174 | 2025-12-01 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77cfe14a-0850-38bd-accd-80619d156bd4 | -0.65073 | -52.36361 | 2025-12-01 04:25:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f921788-c25d-3a1b-8c52-ea142f312409 | -4.44161 | -42.97379 | 2025-12-01 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06e64cb1-2d62-3d1c-8731-dae0e6884a50 | -3.50059 | -44.21629 | 2025-12-01 04:25:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7200b3c7-5bd3-3b82-be9e-f9c21899204e | -3.26166 | -48.57487 | 2025-12-01 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c20dada7-2446-38e1-91fd-16fbaa7c0302 | -2.57142 | -49.09827 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f902ff25-268b-3082-a5b5-3a86ad63f885 | -2.86397 | -45.22181 | 2025-12-01 04:25:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc14f38b-6fec-3e53-9dd4-5b567b162111 | -2.38871 | -47.60821 | 2025-12-01 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b010a3a1-a104-3f72-994f-de4925c5785f | -2.90438 | -46.81417 | 2025-12-01 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f50c9d35-0c2f-371c-94ee-ebab904effa7 | -3.59305 | -47.27044 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f64d86a8-bc66-343d-b198-e97ba3853b09 | -3.37258 | -50.50137 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f66e4c3-5b6c-350e-8955-b76ffb6f3224 | -1.98086 | -46.42389 | 2025-12-01 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70bd9ba4-148a-3625-9d51-869b07bfec81 | -2.90724 | -46.73121 | 2025-12-01 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4038cece-d4f9-32e1-8dd3-444332076cee | -3.59757 | -47.2638 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ba76948-c760-3dee-81d1-3c7cd39fdca4 | -4.69631 | -45.64741 | 2025-12-01 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5986cbf2-dc0d-3cba-93ee-0ddffe360e34 | -3.17871 | -50.31002 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4edc491d-dfd9-349a-a927-375d711d887f | -2.24336 | -46.52282 | 2025-12-01 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ce1bbed-ea09-385a-966a-ca99837d171d | -4.39088 | -43.35279 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0dc5979-b2f4-32fb-93f8-0f97bddb7c08 | -3.21489 | -50.13742 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 993ddf65-b3b8-3296-a709-a2f451ce4640 | -3.11091 | -54.17739 | 2025-12-01 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6d0c065-3f1e-3323-9b69-77272070231d | -1.18059 | -47.7948 | 2025-12-01 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e396f889-42ba-3205-b955-578902257f8a | -3.22598 | -50.3177 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec17c45f-5d7c-3581-af4a-fb03b26d8bda | -2.74029 | -49.33064 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2eaab08d-9cf1-32ee-9c9b-dd4c38b8e46b | -4.39037 | -43.33271 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b06ed9ea-f935-392d-90a0-c245a29a178f | -4.13046 | -43.72585 | 2025-12-01 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49c64f49-d7f7-3fa0-b68e-88b5e6f9027a | -3.69031 | -50.62443 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64d18c92-67ea-3122-bcfe-047f0e644546 | -2.46519 | -52.13195 | 2025-12-01 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce5736b9-1f47-3a9e-8190-a2b7756102ee | -2.59657 | -49.26379 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7054501f-2531-347e-99ba-023b12f73cae | -4.31006 | -45.38152 | 2025-12-01 04:25:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7da7579-a2d9-3e3a-ae5d-cd5819cc4fc4 | -3.25435 | -50.68839 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21d098ad-c61b-3e4c-a862-ad65b812bdd4 | -3.53668 | -43.87213 | 2025-12-01 04:25:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43fd87b6-1c73-33dc-a48f-ca8f0adcca6f | -2.83829 | -48.83003 | 2025-12-01 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d63e6e9-84cb-354c-84b9-77360b604ad9 | -3.58491 | -40.42906 | 2025-12-01 04:25:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a7861e6a-0b2c-38c5-b512-2e60bcbdab90 | -3.70925 | -50.65929 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd869127-251f-3a18-a0e4-2e00f1751894 | -2.25087 | -45.61786 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e738f49-b13c-3d94-855d-a5f28dba14d0 | -4.58324 | -45.97497 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d790c354-786f-3f07-a591-41a4f8e1b611 | -5.49177 | -42.1696 | 2025-12-01 04:25:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a15d4c8a-36b3-3f2e-80eb-ccec379d7ad9 | -2.93833 | -53.29173 | 2025-12-01 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c484732-210f-3533-a8bb-98ab9a2a16db | -2.92217 | -45.28385 | 2025-12-01 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e90633b-a1ae-3218-9e05-0c71449f489d | -2.93349 | -53.29092 | 2025-12-01 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9137e96-49d7-3c69-8dff-c6e0caee686b | -3.17394 | -50.31443 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49f1c03f-f709-3e90-b73f-3f684292a091 | -2.44807 | -47.08058 | 2025-12-01 04:25:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0efb4f22-5273-3954-b036-f3d2c4a86c14 | -4.31392 | -45.37859 | 2025-12-01 04:25:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c8e2e35-bc46-3d85-90de-39ef7df4f8d1 | -6.30272 | -43.81051 | 2025-12-01 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f937453-4b70-3ce5-8597-5dfb7229cac9 | -2.24372 | -45.62026 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0e0303a-754a-38e4-9c49-c3eca4a1b8c8 | -3.28424 | -50.50378 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cc65c26-44c3-3618-aefe-85589405cecc | -2.64678 | -48.55052 | 2025-12-01 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2c7296c-d527-33c8-8364-981e90e42ff1 | -2.34681 | -45.7424 | 2025-12-01 04:25:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c1e3dc7-e3aa-305f-aebc-98339a66d5e7 | -5.33068 | -43.56932 | 2025-12-01 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c1161b58-4c75-3252-9151-e49c04188da0 | -6.35311 | -43.97987 | 2025-12-01 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46f30c30-f735-3b1d-b9ce-6f845e4dfb4f | -2.51018 | -49.10189 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1456b0c5-5945-357a-9ae3-e31d5af3cfe1 | -3.03349 | -50.24103 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fd19146-f4ed-341d-acc0-0f8910cff1d9 | -3.22679 | -50.31268 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfafbea7-c887-3ac5-8458-7e01678613dc | -4.37426 | -43.15404 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5ddb1c65-c74f-31a6-b440-5783c3f9f794 | -3.70981 | -50.65585 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb5ec322-dda6-313c-bff5-46a44361abef | -3.28863 | -49.90183 | 2025-12-01 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15984858-5a4d-3289-b0fa-9b35aa022525 | -5.48896 | -40.9275 | 2025-12-01 04:25:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d4ec726e-fe95-3e71-914c-03c7367c98e8 | -3.4483 | -50.55222 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e32d6c5-b8be-3000-8aa6-6fc3b2fa3506 | -5.52255 | -42.60138 | 2025-12-01 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a38674af-2c6d-3863-85ba-6915545fc358 | -3.71324 | -50.65998 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7437a79-67fe-3654-bb70-eca37d2ff351 | -2.44129 | -47.07952 | 2025-12-01 04:25:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3235f9a7-0732-3a16-a84c-de6a71581030 | -1.40908 | -48.95877 | 2025-12-01 04:25:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4adc8fdf-24bc-335a-9cff-4d12ea49219f | -6.31611 | -43.81662 | 2025-12-01 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7db67445-d7cf-30f6-a5f9-4605660c8e5b | -3.70109 | -45.90286 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6183714-6e8c-3988-ab74-c34d57cb1c37 | -3.93671 | -45.85218 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cd077853-2015-325f-95e6-4e4c9eeaea3f | -3.25378 | -50.69195 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6e29807-8db6-37f5-b77e-58cee08af2ca | -4.38918 | -43.34054 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32aacc21-02f3-3339-a72b-a932b30c9401 | -1.88459 | -48.40076 | 2025-12-01 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07bbc048-e955-3d9e-a1a3-e639c2eab4f2 | -2.3435 | -45.74189 | 2025-12-01 04:25:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7d8d59e-434d-3168-8fb5-b066624d9370 | -2.98481 | -52.63105 | 2025-12-01 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 199850c5-d927-3a6a-b373-49e44284977b | -3.19901 | -45.23203 | 2025-12-01 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c38c3f9-c50b-3958-adc2-2515ce3d62bd | -4.38687 | -43.33216 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| c06d1abe-6b4f-3182-8c07-4d09200d90c9 | -3.57539 | -50.29347 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22dab7c6-5510-3425-baa1-6fd05e74ac3d | -4.57994 | -45.97445 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15ff8ce7-cbb0-3f5d-b859-b6624a8303f0 | -2.24648 | -45.62421 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README15.md)
