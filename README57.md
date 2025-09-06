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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6f7d53a-f9a9-3362-9a9d-57717c759614 | -7.05888 | -50.86192 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d4ba6df-3ad1-3fc5-9f9f-919db01c706d | -6.19375 | -44.77241 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8a2eb6c-8b09-37af-a5c7-a705c3c65457 | -6.40493 | -55.55808 | 2025-09-06 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecbfab40-e907-3c41-b4c1-aeaaa6dc6b87 | -7.04382 | -44.35228 | 2025-09-06 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de0946e5-c2fe-399a-a0c7-8172a2c5b4aa | -6.40197 | -46.09392 | 2025-09-06 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f33b5041-3b9f-31c8-8af4-6ad69403b758 | -8.08175 | -50.19681 | 2025-09-06 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce58b99-7309-3aee-ab3d-7a472d19186a | -3.2467 | -50.80169 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| abd2b6a3-0255-3c7f-9454-a1e6acfd002b | -4.5021 | -42.88298 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d6207f2-d8d5-393a-a465-2033b3c0d137 | -6.21633 | -43.36417 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 272e5bd5-b82b-3a07-9a27-8eb48ad7874b | -8.85886 | -52.01278 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fda3f43e-0aaa-3a52-acee-e5350b177eec | -5.9482 | -53.80344 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec8eb40d-0852-3dcb-9eb5-9314a261d10f | -7.9886 | -44.50916 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8a0cfa9-7b7e-37c3-bbed-4019a65e5de4 | -8.88082 | -47.25649 | 2025-09-06 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e946952c-2ab3-315a-87f1-1733183a1125 | -5.88493 | -51.96927 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3464cccb-b726-3905-864c-f19c7d0bd006 | -9.18053 | -46.03379 | 2025-09-06 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d67126c1-02a7-321f-b9cb-300b5e52045a | -8.64293 | -45.74503 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2be8c24c-e01d-321e-8401-eb2f58367dfc | -8.87991 | -47.91301 | 2025-09-06 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca04bc4e-a7a9-3532-8727-2edbf1ae1cf3 | -5.95677 | -53.79992 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd546844-bf7d-3659-b8a5-7b352f10e435 | -7.98239 | -46.34238 | 2025-09-06 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e2cc49c-f6e6-3189-9597-17d365b7f3a0 | -6.3134 | -47.75871 | 2025-09-06 04:38:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe9dd712-13d2-39fe-82a1-2cf9e448a9be | -4.09202 | -50.69049 | 2025-09-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c934634f-b62c-36b4-9407-667cb4563a59 | -5.7639 | -56.51718 | 2025-09-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e40758cd-809c-3b34-ac32-0f51eebea083 | -4.79287 | -47.2635 | 2025-09-06 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d223e2c1-7e5b-3735-986c-975730796054 | -5.86842 | -46.03891 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78422d5b-9a6d-3ca7-9d3c-1ece64f73f2c | -6.04553 | -51.69264 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1af35af8-4e8e-35dc-aab7-a2a6458a8eb2 | -9.05677 | -50.45329 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97884092-d116-3b3c-9adf-1e2289eb8743 | -6.01139 | -43.70279 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdf2abee-3e9b-3184-9843-c627ac8cb270 | -4.35372 | -48.72429 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ad4edea-c62d-3c2d-80b7-5f6b58cddce6 | -7.19907 | -46.57706 | 2025-09-06 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0f74353-7177-3b73-a695-e6150ec088ea | -6.40802 | -44.46515 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c03b5f01-84b0-36ca-b2bb-9b90f32aae72 | -5.9343 | -43.01612 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ea9c95f5-f776-37da-ad9c-4dad0d5c73d9 | -8.07109 | -52.34256 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d056e37-df17-3b2f-b26d-73f71aa065c1 | -8.77449 | -49.63748 | 2025-09-06 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e24d26c9-7367-3cd1-8ab6-caf23a2c5009 | -8.51385 | -51.32345 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 125e0689-23cb-3755-97ef-d85f1452a5fa | -5.55976 | -46.53962 | 2025-09-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3b33f26-79b1-37b7-b5af-72c282ac8b0c | -3.23923 | -50.80434 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b7e6679-efe4-372c-9822-310641198d54 | -4.8256 | -42.73665 | 2025-09-06 04:38:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45a09dc6-79fa-3bdf-9835-0a5d7a0961e7 | -5.86269 | -52.1741 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c48db27-db6c-3b3c-9b37-01438c20efe5 | -6.07485 | -43.35208 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1ada82f-8b9a-3029-ae9a-0cfc24bacc27 | -5.96447 | -53.60072 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbf8b7ee-d098-3a06-9a3c-7234a623c5e8 | -7.38459 | -50.90701 | 2025-09-06 04:38:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0920eb73-e48d-3c8a-aa7b-591db9538eb1 | -6.16226 | -43.17763 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b06f6552-4749-3186-b66e-d14f3bbb3393 | -7.77066 | -50.95396 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce93b519-87ae-34d9-931b-c70fc5739498 | -7.05665 | -50.85438 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e071e00-7a58-3281-bb34-a45852293099 | -8.35473 | -52.55644 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02b5de97-fea6-3a35-b8f1-b3dfb91a31e4 | -9.78037 | -46.90684 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b2388d7-fe3a-33b2-b626-9cad96b462ae | -6.16569 | -44.30684 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b552eede-dca3-36bc-acb9-89f4e1554be0 | -8.34296 | -47.4902 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd90d746-94ff-392f-baa4-011bc09a5a22 | -5.87439 | -46.04848 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8da5b2d2-3e96-3547-b434-c57566bd34c4 | -6.18821 | -53.25405 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e018fead-6d3b-3609-8ae8-7cdf1c002917 | -5.73183 | -45.36501 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25f629b9-1233-3196-a878-c41ad82b4fff | -7.42884 | -49.47111 | 2025-09-06 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fff5ce9e-a6e3-3e18-b8e4-bb5e70bfb331 | -7.76027 | -50.74125 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86c7ac28-1d5b-3515-af05-7bdd20bcc7a8 | -6.3203 | -58.17449 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 688bcd31-9951-37d3-8d31-3d6cc533b284 | -7.21249 | -43.993 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1174364d-4d8e-34a2-962a-c53a986714fd | -5.98209 | -53.58908 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61c84f6a-d456-3532-8c6d-0f519a841f2e | -7.41405 | -44.94322 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9790a69b-63e3-3ae6-b3c3-c15f290dc67b | -6.51049 | -44.07622 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a737f09-a747-37a7-885a-1588ec840cbe | -7.34239 | -43.95908 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a61785e5-f27c-37a1-81d9-41c4ca2e3355 | -2.85144 | -49.50301 | 2025-09-06 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b9baed6-a5b1-32a7-8f96-e30fa12c905a | -5.94858 | -46.17399 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 682b2dc8-62df-346a-b243-93266d204d31 | -8.36878 | -52.55888 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12398a48-4f5e-374c-8663-986b1d3d6895 | -8.37296 | -52.55548 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d641b5ae-803a-3ae5-b987-23c993773bf0 | -3.48228 | -43.33134 | 2025-09-06 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 476a91c8-429f-3d0b-a432-4b1cfb7e2418 | -5.87909 | -52.09504 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8706941b-38e0-30b1-b487-bd17a20c2c91 | -6.06682 | -43.4388 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85d0056f-3d74-36de-9317-5322c65a0f78 | -5.068 | -56.07215 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a958cc82-acf4-3787-8d2e-d58fc6db0c00 | -6.16327 | -53.6886 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0d68022-aceb-3d59-96e0-94e79c220bdb | -6.77956 | -52.80692 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 131fd22e-d266-3837-bdd7-20934c1cfb63 | -6.20712 | -43.36686 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77af6da2-3787-3f44-80e5-8bd1c5282c44 | -6.25225 | -46.12116 | 2025-09-06 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9754aca2-982c-31ce-945b-a59c9945e097 | -7.71132 | -50.32668 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e316df5-d691-3cf9-bea0-e9aa9e49425d | -7.05203 | -44.35329 | 2025-09-06 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 11b4ce40-4acc-34db-a8fa-e57c11c111b9 | -5.93171 | -43.7185 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e667eb7-036e-3919-939e-5d4966d6a2b2 | -6.39896 | -46.08918 | 2025-09-06 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bf6c64a-f091-3647-ad5e-24d6b863e23c | -5.03572 | -49.762 | 2025-09-06 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a67c1d0f-573d-3a38-a56a-5ea25462e1ee | -6.27144 | -53.4533 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd80076b-a1fa-37d7-8c28-73338725b78f | -5.06343 | -56.0714 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35b4b728-cbaf-37e1-aae3-2686ae1ab7d2 | -6.87112 | -58.9343 | 2025-09-06 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73a1b8e7-690e-30db-b963-685423e4119f | -7.00755 | -44.95788 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ff812bd-079b-3688-b31b-ef899fb72e3e | -5.91029 | -57.7323 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc5e99eb-5bc7-3b4f-848d-b9f154c670cb | -5.97289 | -53.59732 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 344a1821-6cec-34bb-8838-6b4a872598f5 | -5.98091 | -44.72443 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac2ee8ec-f00f-3a22-a28f-abfb4ecc4eda | -9.87814 | -46.54676 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f85229a-25a6-3eb2-a550-1ee2531f38a0 | -3.31341 | -48.70895 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d9d234d-06d1-330c-a6e3-a7b0c53d0acb | -6.8713 | -52.79178 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0963c33-0c33-365f-8cbf-35cbdb25d0fa | -4.8936 | -41.75747 | 2025-09-06 04:38:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 94633181-bd77-3f22-a6e8-c04aedc1f0cb | -5.75343 | -45.5328 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6c87ce2-980f-3945-a95c-fd0a8c133d51 | -7.33987 | -43.94678 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 480f93f3-a93f-31bd-b358-c0567ee055f7 | -6.76147 | -45.93421 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7190b2e9-0707-3255-a02c-496fa0d2350b | -3.96519 | -47.97385 | 2025-09-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77442784-175d-320a-828f-7a5fe70381c2 | -5.10807 | -56.14197 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b704cb9-0a48-3e30-977e-a5f6165a6628 | -2.99102 | -47.45167 | 2025-09-06 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 361c2bae-c36b-3696-a6eb-0727697777b0 | -4.99512 | -56.25644 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39140a26-7958-3d3a-9318-1ed1f0aaf6dc | -7.96614 | -44.94779 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7a2de01-21de-3504-8949-cfba2e9ceace | -7.73643 | -47.42151 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bbfb49f-dd91-3357-a744-86cc91f7f5f5 | -7.63903 | -46.5602 | 2025-09-06 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb990c34-dbd2-3c33-a176-fd263790c36d | -8.93536 | -48.64846 | 2025-09-06 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0778825-c87b-3289-bdbf-ba4b164ba1d9 | -9.0645 | -50.44739 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d92861d3-6161-374c-9692-f8583a242833 | -8.3771 | -52.55226 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README58.md)
