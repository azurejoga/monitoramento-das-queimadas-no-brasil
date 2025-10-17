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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a5271e2-44ea-3105-b120-c2d38192a1d6 | -2.81224 | -54.38669 | 2025-10-17 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c190a41-b3be-342f-a058-d8313bf37926 | -6.23312 | -41.54319 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 599fbf4b-066a-3719-84d1-68a3d6dd7746 | -6.32371 | -40.94796 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 40c78a4f-444b-315c-8dfe-a4038ad55f61 | -6.60473 | -42.0664 | 2025-10-17 04:49:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 133899a8-b0f4-3c38-b2ab-f274ef491f09 | -4.10432 | -48.02286 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a1af886-3d0b-3e61-9a58-a91fea62017e | -7.41693 | -44.75979 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4bf3ee1-f7ac-32d9-95fa-d104ed81660d | -8.21218 | -43.97546 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d44f254-13be-3131-96a1-fefe4344761d | -7.28002 | -42.3147 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff03b181-67e9-37ed-9c45-8f2a8dec536d | -4.55598 | -50.60748 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d21ce05-575e-31ba-86de-4b7c1a971c65 | -3.50656 | -52.49305 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ba662f0-52ed-39a9-be82-37475255a44a | -7.17164 | -42.51461 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e425d7c0-9acf-39b7-9cd9-4d51bfb4e936 | -6.12957 | -41.76501 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da6dabcf-f6a1-30ec-b362-56df29931067 | -7.66787 | -45.63338 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54846bbb-af79-396a-b329-0499d53a7979 | -7.57619 | -43.82722 | 2025-10-17 04:49:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38187fbd-1480-3ce7-a61f-fa6d7ea41b2e | -6.76098 | -42.36448 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b84fc69b-467c-3009-b6c6-42f634f7cba2 | -6.20021 | -41.77298 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7f57ea16-857f-33a8-9926-9dad15316a24 | -2.44162 | -49.3623 | 2025-10-17 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed2fee20-3699-3c01-aab6-b50dfda9648c | -3.60931 | -48.9058 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c32bac1c-cdb9-34ca-9e6f-8cf6a3f5d66a | -6.20709 | -41.76357 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| df068588-8b67-37db-b4c9-09a085e0c473 | -7.35943 | -41.90431 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bfb422bb-0b41-3e2d-bbeb-05d139e2471c | -5.26151 | -50.9813 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60409114-0b66-3bb0-9a67-e77ff9cdfc3b | -2.70571 | -49.85638 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a510a0bf-6a0d-3d04-9068-45c3015a0ac5 | -6.22778 | -46.08011 | 2025-10-17 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9477892d-d3ab-3ca2-8802-e9673a2a1a0b | -6.69381 | -40.8792 | 2025-10-17 04:49:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e985f489-7ebf-33cc-8425-1111a9d5fb65 | -4.43624 | -50.54964 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b09dabee-ebed-3a1f-8302-badfa6946b3b | -6.74898 | -42.37361 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d2e95510-7e0f-3d1a-9aed-eee8f401fe5d | -3.53812 | -49.00572 | 2025-10-17 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b530507e-a2e2-37f9-88c5-9db5d91cac69 | -3.24107 | -45.97739 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 54d4049c-95ee-39d3-a092-f865e804ee49 | -4.40716 | -43.39233 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 061e049a-0ae2-30c0-80a8-9858b3a80626 | -6.58866 | -47.0749 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cc54a4b7-16d7-34ee-b35d-6be5808a736f | -6.95868 | -47.71896 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf7c860e-5312-39d0-b849-1c64b82b37e3 | -2.71075 | -49.41168 | 2025-10-17 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9bb7126f-a71d-38f3-b284-32482a9031f6 | -6.75032 | -42.36419 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| efd772df-4afd-3c55-b4bb-f3364f397b0a | -3.2379 | -45.97199 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 592fd6d2-0077-3a1f-b2ff-36b6149b6ba2 | -5.69651 | -53.64233 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19905912-03b5-39f3-8031-e27d60b388b5 | -3.51285 | -52.48965 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58f39bbd-18a2-3947-b37c-59175265631d | -6.87537 | -44.70504 | 2025-10-17 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6fd3b52-034c-32bf-a7af-6d1e09df4a3c | -5.84022 | -45.54213 | 2025-10-17 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c5bf8f4-ed2c-3503-8214-ed727b06532b | -5.48379 | -48.65453 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faa236f7-8da3-369d-97a5-d467caf5f295 | -4.36765 | -44.77726 | 2025-10-17 04:49:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15aab605-02ca-3121-85d4-3a0e67b5649f | -6.7073 | -44.37593 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a28a4379-6bc0-338e-95a3-89328377a564 | -3.41546 | -50.13803 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4139be7b-9d65-357e-ac13-2b0e1a1e6ad2 | -5.44409 | -44.17368 | 2025-10-17 04:49:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 761fdc39-48b8-389e-b4e2-c99772e0fe45 | -7.0006 | -46.99213 | 2025-10-17 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 832cb2ad-9970-340b-baf2-086555917593 | -2.87186 | -50.72889 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b952b8b-9306-3cb8-8f31-043bac0eeb00 | -2.87687 | -50.74033 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48b791ab-9aad-3071-aee4-75735418bf68 | -4.42128 | -40.18063 | 2025-10-17 04:49:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 92419ccb-0b0c-3a49-8bc3-e4fab106c8a1 | -6.18707 | -52.73556 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6832ecc4-163f-39d0-9e79-6df96eca2efb | -6.97007 | -42.2032 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 54f1aa79-8883-3309-a5b3-1afe36aea3ac | -4.86308 | -44.43595 | 2025-10-17 04:49:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cda9452a-7d85-3063-9b63-2d3a44bbb73a | -5.31228 | -42.94472 | 2025-10-17 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e8d8ef6-5423-3546-bc03-0ff410e1b102 | -4.42187 | -40.17666 | 2025-10-17 04:49:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66998bf9-8baf-3603-ba3c-602097cf5772 | -7.27745 | -42.94305 | 2025-10-17 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7503ab8-4aa0-3fd9-b9fc-10ff8cfb3989 | -4.86801 | -45.78601 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85c114c4-7e57-35e7-9209-6361a6adfed5 | -5.88071 | -43.90372 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d57ac391-954f-34ff-b423-a7f11fa6d037 | -7.84206 | -45.45985 | 2025-10-17 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8206e907-0e3d-37fd-a55c-03d506b8015e | -4.86161 | -44.43795 | 2025-10-17 04:49:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61487207-b385-3609-b673-154dd3eeba5e | -5.79114 | -42.49783 | 2025-10-17 04:49:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a214e025-cfba-3998-b313-685f064dd8f0 | -6.98829 | -39.23169 | 2025-10-17 04:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92c78f06-d18e-3516-beb2-3ad3c0670a77 | -7.08572 | -44.2688 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d6fd763-7494-3053-a39d-e969d6cd5c39 | -3.66133 | -50.27205 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2617683f-ec34-3166-bbc7-7dafadf92985 | -5.24818 | -50.95789 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16b3e658-66eb-35fd-8bd7-cd86f7b9e478 | -6.54583 | -43.91826 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f7064035-6795-33be-b687-540bf58abcb3 | -5.88041 | -44.75757 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed8376d3-67f6-3b00-9820-a6949169a11c | -5.46058 | -42.94616 | 2025-10-17 04:49:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ef5ee036-0597-3ff6-9c79-5d92b25c89b1 | -5.88463 | -43.90942 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 665d6244-434f-3302-b019-f3e941c9940e | -4.28317 | -48.58875 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0799ac74-ca69-3fe0-8b56-7d4e3559580f | -6.13448 | -41.76939 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac75543c-e725-3d17-ba76-397c013df9fb | -6.38332 | -41.46926 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c9025fda-5d27-3543-a175-52f5dde78211 | -5.36149 | -44.81767 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be83537b-179f-3c7f-87e3-86246b9df6d4 | -5.89981 | -44.7478 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 098ed871-0b78-35d2-b5e2-cbf0bbbf1df7 | -4.84132 | -42.75687 | 2025-10-17 04:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4edd6670-3343-3989-97f5-d9ed3db7ab83 | -6.70396 | -44.3997 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b401637-e2e7-34cd-a6ab-ed464a8c8a95 | -3.35561 | -49.94084 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22185d66-2186-3073-a73a-7c388fb93e05 | -7.20983 | -43.84145 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c45f9fc3-75dd-3fb7-aca9-f4256e292a91 | -6.05197 | -44.52813 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c70dc0c-260a-37a6-b72b-3f74aa7154ae | -3.44969 | -52.85225 | 2025-10-17 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5842f31b-5639-34ef-8097-944e7168c830 | -8.23175 | -44.01 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60db7752-3152-3133-84b8-a6cc7ac99ee1 | -3.78358 | -49.42657 | 2025-10-17 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 15609927-d95b-39b2-b6a9-c281f541790a | -7.62218 | -47.83846 | 2025-10-17 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d32df430-7bc0-3c17-b729-621acfbdd0dd | -4.41587 | -43.39864 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 01c190ad-5e03-38f0-a067-455b0ad811e0 | -5.91219 | -44.75174 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| cdc32fbf-d26b-36d6-b5b1-c620a79ea62a | -2.70462 | -49.86331 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da5b8fbf-78d4-315c-9446-df7271010422 | -6.74855 | -42.37663 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 82884b84-5e8f-3aaa-99f9-d29a45f63fd1 | -2.8802 | -50.74085 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aac0909f-1029-325c-99ac-dc61104a8917 | -2.86853 | -50.72836 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e8f75df-c16a-3c53-b614-bd666f7c2935 | -5.8861 | -43.89944 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52030a04-701b-38e1-8572-cfeb7c1df5f1 | -1.52083 | -51.62681 | 2025-10-17 04:49:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9afacd67-ae4c-330a-bb4c-d63a95d26252 | -6.74423 | -42.36946 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 772c0640-9206-33a1-94fa-12b444e66189 | -7.94961 | -44.1161 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8a991554-5bd9-3899-8cb3-2b59f5494a61 | -5.8145 | -42.33872 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f1054b64-54eb-3172-bb82-47361a971ca8 | -5.47957 | -50.82019 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20429d79-85fb-321f-b06c-3c9c02d63093 | -6.05258 | -44.52381 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6723131-e00a-3683-b0d0-d2344d8b17a7 | -4.30866 | -48.23877 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc58fa1f-3e03-33a4-a3f2-87edb9663155 | -6.49298 | -47.22307 | 2025-10-17 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3205a9a3-b528-37ac-bbf2-000969c56838 | -2.87409 | -50.73634 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a69b4ec5-ac90-3c1e-bbd1-25c4ebffa8d3 | -3.28637 | -52.5944 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f146f8b1-c106-313d-b811-7c15a9753f91 | -2.92514 | -48.30538 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c66d845-21a6-352b-848c-4b06599a4d8b | -3.23937 | -45.96215 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 29f93c70-52fb-3ddf-8da8-1c2b7734a4e5 | -7.7484 | -42.50516 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README81.md)
