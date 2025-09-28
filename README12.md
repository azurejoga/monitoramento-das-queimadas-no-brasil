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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d81a147a-462e-3c4c-8598-ead92d133c81 | -7.63149 | -43.80337 | 2025-09-28 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57c1eae7-e4a5-3b81-b518-1af20fc57380 | -6.30962 | -45.89489 | 2025-09-28 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2f4fb77-77ae-3929-a5a1-b914b4787287 | -5.74337 | -43.37411 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a052346-e9bc-31f8-9f39-b87f19a44378 | -3.42259 | -43.16408 | 2025-09-28 03:36:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdfa1b07-3fe5-39a2-9f5e-e3066a2b8b76 | -6.16753 | -43.38018 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36d705ff-5838-328b-8a1b-92cbcfc18814 | -7.56996 | -42.40928 | 2025-09-28 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 436a22c1-ed58-359f-b58f-2bc7e2770443 | -6.27628 | -43.63125 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9464f8e3-576f-3d00-a144-7857b60a0985 | -5.82122 | -44.43671 | 2025-09-28 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1f4bef5c-0537-3928-bf1c-b56ec2167db2 | -8.63833 | -44.8423 | 2025-09-28 03:36:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eab157db-d0e9-36f2-85ef-5037c40aafd9 | -7.80465 | -46.99583 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7683d79a-9e4d-336a-8c2d-88665e479de8 | -5.7267 | -42.8409 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 91396d32-40f7-3f38-ba17-83f76c512a90 | -8.28991 | -45.44579 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8175f70d-6686-3348-9e1f-315d23e260ff | -4.48361 | -40.78709 | 2025-09-28 03:36:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 254cbac7-90fe-3843-b2f9-5a98a87974dd | -7.76326 | -45.72343 | 2025-09-28 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0759ea27-648e-3cba-a06e-9bf9d2dc1228 | -5.78065 | -42.89708 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d8862368-0ab3-3502-a93a-1580fa01f369 | -7.80899 | -47.00949 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| abf8b5ec-ec64-3acf-ad79-45cefe9a1a0c | -5.78125 | -42.89367 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| aeadc13b-9c46-3e96-84df-4f7a8a66f48b | -5.85231 | -42.57789 | 2025-09-28 03:36:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cfba1aa3-7ec9-3eb8-ad0c-7ffd30ab8a82 | -7.76235 | -45.72839 | 2025-09-28 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a926e54-6b78-316e-83fc-74e1bf5f10d1 | -5.72146 | -43.33534 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f35eb6b-310c-3618-a81e-7f582642cdda | -8.49098 | -47.80589 | 2025-09-28 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b63313e-ab39-3e8d-a027-fc046dd41c84 | -7.00122 | -44.69756 | 2025-09-28 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84f7a39d-a64e-3059-a99c-98f4b3238b2d | -5.18908 | -39.30792 | 2025-09-28 03:36:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4b50a1d-64b6-39f7-90e2-8853a06c6c1a | -6.31282 | -43.45823 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| be40ef27-d63f-3c4e-aa12-20194e3090ff | -6.78862 | -44.08588 | 2025-09-28 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c5985ac6-c661-358e-bf7f-a24819ade08c | -7.32541 | -45.99128 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88c268d3-a3e7-3be8-8d67-6c2150515427 | -5.81651 | -42.81762 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| be77796d-63f2-3963-8854-a59240d78415 | -6.69997 | -44.57587 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f18f4936-6cda-3401-adf2-6241257c1ef9 | -6.25043 | -42.466 | 2025-09-28 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92a6b96a-84ad-3d6d-b719-77b3c0f1f779 | -7.17284 | -45.49741 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ce3c377-6689-3723-beed-3b85371a3600 | -5.79916 | -42.82235 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 131b421d-f835-38f3-b00a-622981640735 | -8.27348 | -45.46218 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b2a5864-8693-3286-88d4-8db12ef4f94a | -6.70419 | -44.57494 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d30dc409-ce72-3bfb-93c6-f33e361c82c4 | -5.36086 | -45.04074 | 2025-09-28 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d4e7310-767b-3c8d-820c-cbc9b54df696 | -6.07104 | -43.76996 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ccdb2e7-9b78-36e7-8f99-b8847179e6e7 | -6.60828 | -45.0892 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bebb50ea-aad5-32a2-84b1-baba3cdd838e | -6.45728 | -44.0234 | 2025-09-28 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b50b1be2-1225-338c-82f3-87ce853dedc0 | -7.16911 | -45.50918 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d548ebf1-2778-31d2-a98e-be2a50031746 | -5.81829 | -42.8073 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c1668673-dc05-39b6-b5c3-2aa6ef465d65 | -4.77882 | -41.04996 | 2025-09-28 03:36:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5e6438e8-a491-3f63-b51a-9d9d5cc54ee2 | -6.7658 | -41.75669 | 2025-09-28 03:36:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eba69cbd-793a-3657-8e48-20214f14614a | -7.10252 | -44.23546 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cf3d2967-f253-3900-b757-885121739f37 | -5.84706 | -42.57691 | 2025-09-28 03:36:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7f92a786-ab08-379f-a2a2-85ee37980269 | -6.18173 | -42.94751 | 2025-09-28 03:36:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 027e76af-7b30-319f-ad22-d6b85d868504 | -6.34566 | -44.31239 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2e78b1f-26f3-33ba-a5bf-820fa5441dd4 | -5.91382 | -42.94318 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 16b52527-a3b6-319d-a588-d099e847ce15 | -6.05024 | -43.9219 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e48b105-59b1-390e-96ec-0b9d75d39234 | -5.46325 | -41.07925 | 2025-09-28 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 0e393819-ade9-38a4-9b65-71b16d078288 | -5.80692 | -42.80932 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6a21bb46-ac79-30d2-a376-bec03adb4ea5 | -7.29322 | -38.11945 | 2025-09-28 03:36:00 | NOAA-21 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7367f967-46d2-3c1e-8973-1a091fdf0085 | -5.73715 | -43.377 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e08ca1c4-087a-3d8e-99f1-b74928aff8dd | -5.96898 | -46.45288 | 2025-09-28 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1dafd6ff-0c0b-3cac-a0ea-32c62f9b1224 | -8.28818 | -45.45487 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97a8fa56-520e-309d-9f9d-e598d23c23b1 | -6.12609 | -41.79575 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3876aa63-93de-31d3-b003-ba1797e4ab6b | -5.74548 | -42.81374 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c57af22f-07ca-3ced-a714-3c749fa8e4a2 | -6.71045 | -44.58556 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4f31f2d-f29b-3af1-b867-eec00845e2f0 | -7.16482 | -45.50618 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8e0bc69-1a48-3b51-a02e-25fe83cff180 | -4.44568 | -40.98137 | 2025-09-28 03:36:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f00e1b06-c6bb-36a6-ad03-59e4ba70aef1 | -5.37412 | -42.30994 | 2025-09-28 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4d27779c-0728-3a7d-9ac8-ebbe4ae3de23 | -7.23376 | -44.7714 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 917b8c8f-fba5-3040-a4be-b772f78340fa | -4.87813 | -45.85615 | 2025-09-28 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a82d3779-7d41-3ac6-91a7-77bf775dc1ac | -6.26889 | -44.07182 | 2025-09-28 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79a147b7-8f7c-3a33-9ff2-a2bbbaab7ba4 | -6.7223 | -47.20824 | 2025-09-28 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9209db4e-a351-32af-8f42-4a78065ccac2 | -8.27329 | -45.46691 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 65b3b7af-f3f8-3ff7-9025-eba6e07503e7 | -7.86876 | -44.56517 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d2dc8887-313d-328f-8c02-4dfed65f33be | -6.60901 | -45.08707 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f9e90c7f-cb65-3ab7-b75b-8fee0f2155ab | -7.10074 | -44.24035 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 457079d7-1186-3db4-ae7b-d5c98c210692 | -6.61519 | -43.77246 | 2025-09-28 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 124498c3-82d4-3d90-a407-2ce2ddd6b323 | -7.74125 | -47.02212 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 31141690-fb0b-3604-a746-4d8caa70cd90 | -5.80392 | -42.85867 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 085304f1-b6ca-3bb2-9de3-44a02e30e84a | -6.57505 | -43.7375 | 2025-09-28 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 968834df-9a9b-3d91-8943-9ce97c2e52d7 | -3.87232 | -40.34216 | 2025-09-28 03:36:00 | NOAA-21 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6d122b4-da00-3ceb-b90d-7b200e0ce07f | -8.83292 | -45.99542 | 2025-09-28 03:36:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56fa9205-4484-3f6a-abb5-a0d138542a18 | -5.37467 | -42.30665 | 2025-09-28 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c13a4b46-01ea-3897-86d9-e9f937cfd144 | -7.25443 | -42.99368 | 2025-09-28 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10da8ed6-f712-3a0e-90a7-b81673ab9e87 | -5.73958 | -42.84707 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| fa0b8c7a-1896-351c-b1cb-0e21699ff650 | -7.7435 | -47.02356 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| afb87919-0422-3a05-84d2-7dd4eee62b60 | -5.74205 | -43.37551 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a7fa45e6-42cc-344f-866c-fecac45942cb | -3.80391 | -41.57461 | 2025-09-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 3adbfa9e-c0c9-37f2-a573-a6db3cbcb5b2 | -6.42153 | -43.51757 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c94fd6c1-e1d2-34ba-ba9d-b7f068f35e23 | -6.98666 | -43.78501 | 2025-09-28 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ef38780-4a73-3c57-8178-e70ee0ac38ba | -7.2458 | -44.75827 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa199d31-135c-3e45-a689-46ad5e2d84d0 | -6.11744 | -41.81139 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8de4ed10-5751-3b0d-b282-b91f770db9b7 | -8.28473 | -45.43523 | 2025-09-28 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87f6eb86-a802-39f9-bdc4-bf1266276698 | -5.88712 | -43.20076 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 291d467c-4e1e-3b31-b59a-fc0e7289db39 | -5.74739 | -42.83417 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 871e94c2-737e-399d-9981-370bab81c5bd | -6.45199 | -44.22187 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 910505ac-8e7c-3a26-afe6-4bccc047817b | -6.76106 | -45.52837 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 836d1428-4c5f-3cc6-9537-e0c0fc9f95bb | -7.01958 | -40.02198 | 2025-09-28 03:36:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7620b469-527d-31b6-b390-4696b30ea6a1 | -6.60814 | -45.09175 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7af9a216-1fb9-3cc5-a314-66f8ee3da287 | -6.45777 | -44.22303 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5609b69-5620-30ef-a8cc-31917171b217 | -6.12553 | -41.79893 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b18dfb8f-f7a5-3609-b63a-fbafcbe0ebee | -6.7069 | -44.5933 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fda7a021-c673-3de3-83ec-c55f768ac50d | -7.92982 | -42.67216 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e4aab8a-3bf8-30f3-b9d1-0739c19fc7dc | -7.7131 | -41.28682 | 2025-09-28 03:36:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 75a51ff5-6ec6-3d9e-b427-a75ae41e6d32 | -6.40228 | -43.95754 | 2025-09-28 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e270a88-fd0b-3f96-8e4d-b930bc1b9823 | -6.89751 | -44.7614 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd35533b-db35-3214-8c97-6e374e5db575 | -5.75143 | -42.84259 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 841be8a4-0c09-32eb-9ae0-17dd798ad775 | -7.10218 | -44.23222 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 27b77d1b-e81c-3940-9d41-82d3a2d4011c | -8.17726 | -46.38144 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README13.md)
