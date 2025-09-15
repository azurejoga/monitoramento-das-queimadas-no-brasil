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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef067652-ac31-3667-bedc-745376078e10 | -6.26188 | -43.47238 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b9ddfca-c6c2-3341-878e-b834072e714e | -9.2367 | -45.67507 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14100a2d-2f05-34dc-bf58-34ae1f1601c2 | -8.9601 | -45.79076 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1127c60c-4aab-3304-a96f-641f87f140e8 | -7.87953 | -43.58353 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 479874fe-d984-3384-905b-e60d053cbefb | -5.59279 | -44.50001 | 2025-09-15 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b986394b-d709-3540-aab8-5fc984128c1c | -7.67771 | -44.4811 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30bb3ba2-08ea-369e-b31c-05e9506fcd2b | -5.60847 | -42.90046 | 2025-09-15 04:19:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b831626-39a4-3e60-b356-a858e1c3ace0 | -7.89296 | -43.5633 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 2add9cd3-3a90-3e83-ba49-c11e260fbd15 | -6.34349 | -42.54108 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7c127c43-a427-3b38-bfeb-907f7cf99993 | -3.3566 | -51.59602 | 2025-09-15 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da99fbd7-3e2d-396c-b9f8-db3d810b4b09 | -6.16372 | -41.17533 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45ab1a0b-0cfc-30fa-b66a-f909a7bab0b3 | -6.0252 | -43.66432 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4b569df-6c3d-3936-9403-567e4ebc7c4e | -8.91452 | -45.49537 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6518c06f-9460-3171-bc8b-af649b42b590 | -3.84638 | -38.47984 | 2025-09-15 04:19:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 77f0ded8-a89f-3931-a8c3-adf353d07b5c | -9.19511 | -45.24471 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9a8ae1d5-58cf-3b74-83c0-a8d7bb109c3b | -6.43147 | -42.60807 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea30965c-3fd3-3735-a20b-8ac3ed5eb1a9 | -8.40449 | -47.23824 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d15aac1-fa9f-3910-88e0-975979461d00 | -7.40581 | -49.98548 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5a02509-52b2-33c8-a861-979272b2ad68 | -7.98978 | -45.66348 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af283aa5-8e0f-3ca3-a7c1-1c24fc84a60f | -6.45291 | -44.52655 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca69e411-d564-3fb4-98a7-eb43e0fc9aae | -7.969 | -45.64223 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8c25fe2-3cac-332c-a05b-7f6a30b674f7 | -5.80321 | -43.93496 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 999a3fa9-0f21-332c-bf24-bd53f0a474be | -2.26365 | -47.88238 | 2025-09-15 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5667dc22-0e0b-3b5e-84ca-ed52f12f06e0 | -5.67597 | -45.05322 | 2025-09-15 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e640986-0170-305e-8780-ce6094460c8f | -5.5704 | -41.18724 | 2025-09-15 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 00cb72b6-3cb3-37a4-b176-d11ec007eb33 | -8.11389 | -44.82783 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f797dd2-3dee-3310-aecc-59bca7cf9d0f | -8.91332 | -45.45972 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c2ae52d-0089-38fa-8f03-dd8429d84aa7 | -6.44542 | -43.32072 | 2025-09-15 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3b685c6-d416-3ac6-95a6-119368dac567 | -7.46291 | -44.44056 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd4f34f1-014a-395b-9fe0-744c2760032f | -3.8568 | -51.33593 | 2025-09-15 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 689cf2ab-f463-3e1d-b6a6-63e52cd29561 | -3.59977 | -47.51903 | 2025-09-15 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 829d2a8e-bb97-3688-802f-39e5ede3bd7b | -9.00424 | -47.05011 | 2025-09-15 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b540524f-9584-36a1-9dbe-a0e510c8d720 | -7.7029 | -44.67072 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41b5920b-c47d-3fce-a1de-9cef8959f8f1 | -6.14754 | -43.35962 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45c23b14-f49f-3401-8a26-8740b5286f92 | -9.17273 | -45.58248 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14a87d66-9542-3cb7-875d-1fb30a91a4fc | -3.65149 | -54.06474 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 976702d3-d6de-30e4-9c71-f6a8dc35d925 | -7.884 | -43.5768 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| abda33fe-5af4-3b82-a353-d54b9b31f7fb | -5.28718 | -45.25409 | 2025-09-15 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f87fb669-a478-3e39-8bbc-fefc29b8b1a9 | -8.97277 | -45.81775 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ac243dd-bcb6-3f62-a6d3-8d1e04c89dfb | -8.97384 | -45.76799 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 025e7b4d-6b5e-3a49-b996-017375c7d996 | -7.65487 | -44.73708 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 675dda68-4c39-3766-9982-e46541020605 | -8.91285 | -45.48446 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24e4f2dc-7c17-30e5-9d77-35dd7dd551b2 | -7.89241 | -43.56694 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| eb95ab2e-8158-3ab7-b925-de71d42119b8 | -7.40123 | -49.98827 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59f147f-c007-3cf4-963f-2f40abbf37d6 | -8.65029 | -46.36948 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16088076-ece1-3a14-8c5a-07f1d7b2f63d | -6.42801 | -42.60758 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6d9f7bec-3ac7-3eb3-8e7c-957ebb964b0f | -8.89756 | -46.16384 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 394c61e4-e1d3-3967-a6d4-11e5605bbc35 | -8.96507 | -45.04127 | 2025-09-15 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a47bf37-60e4-300f-82dd-e5fde926a2ea | -6.4675 | -46.01237 | 2025-09-15 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0759b4df-795a-3cef-add6-e5c4ddab5f32 | -8.39978 | -45.7827 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f240c2a-1c0e-378d-98bc-9f1cfccdb233 | -8.959 | -45.79771 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2858093-e16d-3c85-bbb6-eebca4e0fbab | -6.43376 | -42.6395 | 2025-09-15 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7bfc7401-2f99-392b-98fd-0197f823cc55 | -6.219 | -43.60033 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b2f367c-0c0b-39ea-9a0a-ba18812d4204 | -5.97535 | -45.85461 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ebc0a94-0f4f-3559-a8cf-ee2219b44cfb | -7.37015 | -44.33649 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f61dc98-368a-3d6b-9eb7-9e757ca7e659 | -7.41518 | -42.08799 | 2025-09-15 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d3e1d7a-b809-3068-8dd9-c5ca43db8601 | -7.31017 | -43.93196 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e92f1c86-6e7b-32a4-84ac-e6af709bb821 | -8.61009 | -46.34505 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bb32f2a-47d6-369c-a6d7-530ea7a83e4c | -6.35069 | -43.16171 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 298c8565-c002-315d-a1b7-2a5af42c577e | -7.87561 | -43.58664 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 78cea5e4-838e-363d-ac6d-ff1a65b2e912 | -8.91234 | -45.50924 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 482a0ada-c91a-3ab7-939d-a423ead60b87 | -5.28663 | -45.25756 | 2025-09-15 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b41bf37-d17b-37e0-8838-e9f00258e2aa | -5.91652 | -45.7298 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15a5dbcf-f9aa-3152-8fde-a21656b7e466 | -7.70017 | -48.86317 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c193002-684f-3c29-a30c-d0a7e6402dfc | -8.11812 | -50.16812 | 2025-09-15 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b337ace-234c-3826-86bc-58b6a3bcb131 | -6.34675 | -43.16481 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6509b08b-4176-34e7-9ca8-ecd8def1113d | -3.38389 | -50.27945 | 2025-09-15 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4105a210-73ab-3fc0-97ab-960be71b6937 | -7.05692 | -44.11927 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1899768c-6119-32be-aad4-d28906436b93 | -7.8705 | -43.5747 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be0394e2-b92b-315f-b21d-b4c8a01e84c6 | -7.99455 | -44.82636 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c02c536-51b7-3bc5-93be-e0754e21ceeb | -6.16741 | -41.17588 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 28139e34-8cf7-348b-b9e7-71778f470f0c | -6.42776 | -44.38036 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef508208-6017-30d4-b0fd-756e83d3b76f | -7.89076 | -43.57784 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9597779d-f0fe-3b11-8248-29e43f7a781b | -8.91506 | -45.49191 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e598604b-2235-3d87-b233-6254c8913c6a | -5.08897 | -41.15435 | 2025-09-15 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4ac91e3-ee6b-3a70-bb53-63e27e97a1d1 | -6.775 | -44.72935 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3476f303-f239-3e8c-8725-d5286a18fbd5 | -6.56119 | -43.98165 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4e0f3e5-baa2-340c-aebb-8e63add1f3ec | -7.98854 | -44.8432 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18330995-9eb8-3fec-957f-b42b796bb010 | -7.5482 | -43.95447 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f868b62a-8a41-3f9a-a3d8-bc4b7b796b00 | -8.94353 | -46.04553 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdc1e607-4e66-32b6-9275-993dd07c020a | -8.59728 | -46.36116 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba63f463-256f-3c01-892d-469173d6cb97 | -6.68285 | -46.7126 | 2025-09-15 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cca6d2dc-4e3a-306c-adc1-3a66bf3b1130 | -6.15505 | -41.18288 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 26a469cd-905c-3bf9-9026-b55ce6be27cc | -8.91068 | -45.49832 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48b90c26-a456-3d95-b2ca-a135473b3b61 | -8.13056 | -43.65819 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c9dc763-0311-397e-b278-a5d266b0e583 | -6.18114 | -41.18081 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 85978124-e89f-3d78-b631-382152b62b06 | -8.13001 | -43.6618 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49c31332-ec4c-3af6-89bc-009842df4db7 | -8.9579 | -45.80468 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39edf246-22fc-3072-9c4e-81cac2a907c9 | -5.40094 | -42.83517 | 2025-09-15 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3d361dcb-07e4-3de2-8ca9-bb0ce19e19ee | -3.91448 | -47.70908 | 2025-09-15 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2ec7500-0175-3619-bd3a-9e6a895b8cf8 | -5.47463 | -44.68937 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 378b366e-355c-3494-9063-8583a0437e88 | -7.64325 | -49.72519 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f2c7cfe-ce17-3d6d-a567-9b06ef9bc2d5 | -4.3436 | -46.46925 | 2025-09-15 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df2d2316-3239-3f66-88c0-d0f888c05bbb | -6.94168 | -44.40113 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c080c23-5ab4-3fb6-a839-9cd77600d447 | -7.45058 | -44.38876 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 797227bd-2fd9-3a6e-940a-32951491b307 | -7.87443 | -43.5716 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a31fe51b-c1fc-30c9-bb24-e6173230d1b8 | -6.40845 | -42.62028 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 72dcd905-044b-3a80-abb3-1d966fa0a854 | -8.6238 | -45.69758 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae69ae89-5a22-39b1-bd7b-8eb260a0d17e | -8.91883 | -45.46769 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d89a260-71f7-332c-ad95-be725f6c8cb7 | -8.4089 | -47.25424 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
