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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8115889f-b3d3-30b3-aebd-5f89172906d3 | -6.086 | -48.0557 | 2024-12-02 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 188.0 |
| ba25534c-96ee-38cb-822e-d133ad6406e8 | -2.008 | -54.3091 | 2024-12-02 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3878480d-ead3-3587-b81a-0041ea681d28 | -3.2774 | -53.6383 | 2024-12-02 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 55e38905-141e-3c1a-aacc-cc705bfe9ee4 | -3.3848 | -49.8596 | 2024-12-02 00:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 23abb14e-3c70-3dc2-99d6-27cbb94fc5ad | -3.2184 | -45.7637 | 2024-12-02 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 9c5f785e-67d6-3be5-a016-4c212298ce20 | -2.8197 | -53.0425 | 2024-12-02 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d897f03e-e1c8-3e45-9948-dd6cddc6b45e | -3.3664 | -49.8602 | 2024-12-02 00:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| edd2453b-bd7c-348d-9e97-cb71bb5140ac | -3.1268 | -45.476 | 2024-12-02 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8cc3cb60-cec5-39f9-887d-119c565439c3 | -3.2591 | -53.6186 | 2024-12-02 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c83081ae-f046-3cef-b609-62f656911a77 | -2.8012 | -53.0633 | 2024-12-02 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| fa5acd5f-4ee5-3601-9004-15bb2f8f2e3d | -3.259 | -53.6388 | 2024-12-02 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 00d18d50-6175-3b95-85aa-7286cbe582c0 | -3.8709 | -46.575699 | 2024-12-02 00:14:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 919632d5-f5c0-3bbb-bcf1-6eb8b6d66a2c | -4.7645 | -46.4352 | 2024-12-02 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6730706-a80f-3b26-8048-26d6a8e02439 | -6.8186 | -46.763 | 2024-12-02 00:14:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d907ca8-8433-3872-a361-7f8959ce7e2c | -4.0163 | -46.993999 | 2024-12-02 00:14:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff765afd-0c66-3c22-9953-d089e169333a | -4.5053 | -42.0686 | 2024-12-02 00:14:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0a8054ac-ca8f-32d5-a9cf-39da36cb1ed6 | -4.5812 | -43.3452 | 2024-12-02 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f9c2b5b-773b-364a-b963-1f0b25d1a1b7 | -4.7324 | -43.239498 | 2024-12-02 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8381ef45-6c5a-3642-a25a-24ca1e232a90 | -8.8731 | -40.7822 | 2024-12-02 00:14:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 50bcf934-7d14-36d1-9c13-9ee50e6d3919 | -3.4813 | -46.0798 | 2024-12-02 00:14:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad35870-bffe-33f2-a6f7-c02f908e9847 | -3.3634 | -42.172901 | 2024-12-02 00:14:00 | METOP-C | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 596759b8-a407-370d-9f10-38bbea45917e | -11.0743 | -44.3088 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a12e0054-6638-3d2d-8ea5-8fa50542f43a | -6.0727 | -48.034801 | 2024-12-02 00:14:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| facad744-1418-315f-ac0f-831c31009a50 | -5.1941 | -43.864201 | 2024-12-02 00:14:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f00fe11-8920-3bc7-bfdf-bf5e9785d427 | -4.5491 | -43.2948 | 2024-12-02 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e89d5760-0299-39ba-b197-693a2eba57b6 | -4.1336 | -44.821701 | 2024-12-02 00:14:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e5aa0ee-f8f9-39bf-a3e6-57fc1f1addfe | -3.9946 | -47.264 | 2024-12-02 00:14:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8dfc9ec-c8d7-30d1-8999-3170df64f7e6 | -3.365 | -42.179798 | 2024-12-02 00:14:00 | METOP-C | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 13e5746a-7e09-3aed-b87a-3328bd60cc51 | -4.7496 | -38.4678 | 2024-12-02 00:14:00 | METOP-C | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6617d1cc-a609-360d-8022-6fbd05040480 | -5.5758 | -45.144699 | 2024-12-02 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 142a87aa-5b1f-3857-a9d1-59d5d9a47bad | -2.8656 | -46.723801 | 2024-12-02 00:14:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a9847ee-ba48-35d8-bed5-bd2d213a8826 | -2.8675 | -46.732399 | 2024-12-02 00:14:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d561e4a0-6922-36b5-99f6-84bb057d12e1 | -4.5699 | -43.340599 | 2024-12-02 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b1010da-e842-306c-9b56-6a6c2c6d9417 | -3.1392 | -45.977798 | 2024-12-02 00:14:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23a71d2e-2c4d-31f3-b707-e509a84d46e4 | -6.3622 | -47.345901 | 2024-12-02 00:14:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3a5a514-54cf-3f05-b2ce-5ea8c21e53a3 | -3.9827 | -45.884602 | 2024-12-02 00:14:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9945f8ee-40fc-3a3d-b780-2c5104e652c8 | -3.9463 | -47.0481 | 2024-12-02 00:14:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a169d97f-9038-3d3c-95d1-212f5bfbd92c | -4.796 | -44.7449 | 2024-12-02 00:14:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b098b135-957f-3e4d-80a3-6406838d9bcd | -4.322 | -48.086201 | 2024-12-02 00:14:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a93483e9-a7eb-3f1a-9574-058186ea2abe | -1.9594 | -46.4496 | 2024-12-02 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc7912f8-a118-36c2-b775-d7d8a55f068b | -2.9544 | -39.960499 | 2024-12-02 00:14:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 47d6879d-ca42-3564-be22-ffc3719f80a3 | -5.3216 | -40.423 | 2024-12-02 00:14:00 | METOP-C | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dffb2242-cfc2-380f-980d-3d900d53554a | -4.395 | -49.754299 | 2024-12-02 00:14:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79bcc909-d9a4-3a1d-ac7d-a46d10c43427 | -5.0204 | -44.7808 | 2024-12-02 00:14:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff6ff4b1-f8d6-3959-b9e5-7cb6c2de9ecb | -5.5775 | -45.152401 | 2024-12-02 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8df538b-a708-3876-b6af-04cf70bd01d8 | -4.0664 | -47.080299 | 2024-12-02 00:14:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab5e60e-cb26-3a16-a71f-5daca07db505 | -4.2562 | -50.836899 | 2024-12-02 00:14:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1c33b81-2f87-3147-949c-94acd7ebae92 | -5.3667 | -44.901199 | 2024-12-02 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b9813d8-9d7c-3380-8164-e9cd52e1e99c | -4.7626 | -46.426399 | 2024-12-02 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 521a9b97-0bad-3f57-88d0-6f6ec80a1abd | -3.6167 | -42.736401 | 2024-12-02 00:14:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4ed7767-8f92-3457-a387-d91ba9cec217 | -9.1966 | -43.205299 | 2024-12-02 00:14:00 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b52003b9-fb14-34dd-b646-029ae0b6ee26 | -4.5672 | -45.4645 | 2024-12-02 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bce7e5f1-5575-3ee6-ad78-9cd08d8e6b45 | -3.9593 | -46.0089 | 2024-12-02 00:14:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f91ca6a-c161-3b21-b823-c9f9f39e9c89 | -6.085 | -48.044201 | 2024-12-02 00:14:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 839c7650-bf3c-38ee-b299-659e7c2922d0 | -4.5507 | -43.301701 | 2024-12-02 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8b6b32-1f81-3edf-8218-6982580b9d3d | -4.7606 | -46.417702 | 2024-12-02 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 834f9a1d-9436-30f9-acc6-e5361414267d | -1.9576 | -46.441502 | 2024-12-02 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab27e35-dedd-37ad-ac47-4ac60d6028c2 | -4.2525 | -50.8204 | 2024-12-02 00:14:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bcdd725-a920-386c-aea7-1b7b7a606f13 | -3.8514 | -46.5345 | 2024-12-02 00:14:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 431357cd-c86a-3c68-88a6-6f64c2d0ea59 | -4.0481 | -46.815201 | 2024-12-02 00:14:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4e8be5c-7c64-3242-aa4f-4a2be510d747 | -5.022 | -44.7883 | 2024-12-02 00:14:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ac0bf32-6f26-3a05-893d-62da39dcf773 | -3.9553 | -46.493599 | 2024-12-02 00:14:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42b95069-8a95-3bb1-a532-b5f6a3f6b88f | -4.7339 | -43.2463 | 2024-12-02 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 535c4ff2-0fd7-3714-a0ac-789742fba477 | -3.4832 | -46.087898 | 2024-12-02 00:14:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46d4000b-25a0-3346-b654-44df70c472cb | -4.0878 | -44.847198 | 2024-12-02 00:14:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94719736-da29-3add-930f-78d5e75add5d | -4.0457 | -46.987598 | 2024-12-02 00:14:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e58d6cf2-e1b8-3b16-b086-9ac260dad601 | -9.9868 | -44.735901 | 2024-12-02 00:14:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0682921e-5bae-3d1f-8f31-2faf8e158f02 | -3.9808 | -45.876499 | 2024-12-02 00:14:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f327b23-3af6-3647-9f02-989644f7756a | -3.4795 | -46.071701 | 2024-12-02 00:14:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 838978b7-ed0f-3369-ac90-05df18795f93 | -4.7743 | -46.432999 | 2024-12-02 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 612d4214-a60e-37c6-a472-3e4ac1052284 | -6.676 | -39.329498 | 2024-12-02 00:14:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 65cb18b0-bfdc-3c31-a010-cfd507584d3f | -6.0752 | -48.046299 | 2024-12-02 00:14:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5066dcd5-c8cf-348c-b4e8-7321b0abe3f4 | -3.9906 | -45.874401 | 2024-12-02 00:14:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 514826c3-77cc-3422-a7b6-e65c75365316 | -3.9611 | -46.016998 | 2024-12-02 00:14:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06046ed2-5045-3e33-806b-cfd45664acc2 | -3.1417 | -44.356899 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10491b33-ab4b-3f6a-ab35-42b6e3eeaaec | -4.0895 | -44.854599 | 2024-12-02 00:14:00 | METOP-C | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88b8a493-dfa5-3ca8-b19e-c6913be60f3a | -3.9572 | -46.5023 | 2024-12-02 00:14:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92289463-57c9-3e44-bff8-0c8fd6ab16c1 | -4.5689 | -45.472401 | 2024-12-02 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91a407be-b0e2-3103-9c11-a807909d12db | -4.6417 | -46.8964 | 2024-12-02 00:14:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38cb3aed-9f0e-3ba0-8dea-5e9e792c3c17 | -3.9925 | -45.8825 | 2024-12-02 00:14:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 422ce250-ba77-36c8-8939-05d601c29729 | -4.9691 | -42.022099 | 2024-12-02 00:14:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cea505ef-3be0-3bec-9dba-9ce6b6849070 | -3.6183 | -42.743198 | 2024-12-02 00:14:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6720ee71-4108-3e4a-8aee-ebbda999b1d9 | -11.0725 | -44.300598 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25824924-9749-3f1b-bae7-d5c260d99f81 | -9.9077 | -44.327 | 2024-12-02 00:14:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c0b643e2-ddca-3e7d-81ab-8807d7919c88 | -4.7724 | -46.424198 | 2024-12-02 00:14:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 118096cf-c8fb-3be3-8433-36e365add3e3 | -3.9968 | -47.273499 | 2024-12-02 00:14:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c58a39b-ed3e-303b-a5b2-778c17dd6ef5 | -4.5591 | -45.474499 | 2024-12-02 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3eabbc31-f541-32cb-af9f-383829147525 | -4.5574 | -45.466599 | 2024-12-02 00:14:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de56ae3f-df73-30b4-b6be-275a6e522bd1 | -4.5714 | -43.347401 | 2024-12-02 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43d35416-1f32-3336-b82b-9d70beeafb0a | -11.0579 | -45.376202 | 2024-12-02 00:14:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92a60ecf-a1e8-3a17-97fe-25c29fc43575 | -4.8172 | -48.609402 | 2024-12-02 00:14:00 | METOP-C | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9328b0f5-5d09-349f-bea0-5b88a1a29153 | -10.6628 | -44.493301 | 2024-12-02 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8138d7-b6af-3d1a-b497-dc59d3309452 | -9.195 | -43.198101 | 2024-12-02 00:14:00 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82491d7b-a072-3df3-90c8-7b546f18023a | -1.9907 | -46.451302 | 2024-12-02 00:14:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab418ac3-d573-3eec-b64a-07c5e4cd3f54 | -5.574 | -45.136902 | 2024-12-02 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1581a0ac-a23f-30ce-a5a9-6c8bea89dc02 | -11.6227 | -43.244202 | 2024-12-02 00:14:00 | METOP-C | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5fce5be2-def4-3234-9267-1d4c74e982e8 | -4.8101 | -48.623402 | 2024-12-02 00:14:00 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e73a7914-380a-3360-8ae0-1f151718f227 | -11.6244 | -43.251701 | 2024-12-02 00:14:00 | METOP-C | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 49180843-748b-3175-97dd-1a9cec6586fa | -4.2465 | -50.839001 | 2024-12-02 00:14:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40685ec1-26d4-31ce-bee4-2a3efe330c55 | -3.8494 | -46.525902 | 2024-12-02 00:14:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
