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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18aaa62a-b890-3597-a34e-17bbed1aefe6 | -4.5745 | -43.3483 | 2025-11-04 12:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 50723e7c-e036-3e11-84f3-03d4795f4f76 | -3.4111 | -44.4231 | 2025-11-04 12:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| bd6e4966-83a2-3dd7-863d-db2887b240dd | -3.411 | -44.4459 | 2025-11-04 12:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 49a2284b-583d-308b-90a7-31d5d0c7b23b | -3.4111 | -44.4231 | 2025-11-04 12:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0852e43c-484e-3711-8c0f-c0096b9365be | -4.4632 | -43.2386 | 2025-11-04 12:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 426995fd-d1bd-3cb3-83f4-03753c9e728e | -5.942 | -41.3282 | 2025-11-04 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 131.5 |
| d087a019-5b89-38a7-a0a9-00a2564f7b28 | -5.9234 | -41.3056 | 2025-11-04 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 206.3 |
| ce6efcb8-9ecb-3ee0-b14b-d13e1694bc0e | -3.411 | -44.4459 | 2025-11-04 12:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 233.3 |
| c8b370cc-40e3-34ce-a106-eb29b8f75b32 | -4.5745 | -43.3483 | 2025-11-04 12:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e52e41f1-54d6-37c4-bb31-7611a5a0c4fa | -5.9422 | -41.304 | 2025-11-04 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 4829a234-51e4-3d7d-bcb1-f25a2ee002be | -5.5758 | -42.292 | 2025-11-04 12:50:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| a9e63189-c858-3158-9f16-bd8abb73bd27 | -5.5302 | -41.1207 | 2025-11-04 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 6c5fef5d-cd29-3bd4-a23b-b0769b7ecf4a | -5.942 | -41.3282 | 2025-11-04 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| c8dab5df-d56b-3339-8e30-0a178a00eb99 | -5.9234 | -41.3056 | 2025-11-04 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 177.5 |
| bb929451-6370-306c-85eb-242c8647446b | -4.5745 | -43.3483 | 2025-11-04 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f9b16b77-c25f-334b-9422-7eb0d32cecb0 | -3.411 | -44.4459 | 2025-11-04 13:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 339.0 |
| 89fedbdc-119b-3777-8017-c11cd70a0ff8 | -5.5758 | -42.292 | 2025-11-04 13:00:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 2bf7fb22-b05a-32cc-b672-8968e7c7275e | -4.4632 | -43.2386 | 2025-11-04 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3efd225b-6e6d-3094-8a83-82ec689d66c0 | -5.9422 | -41.304 | 2025-11-04 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| ecbee04a-c5be-37b7-b314-99d999342173 | -4.5188 | -45.9937 | 2025-11-04 13:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a6dafaae-913c-3456-b004-288b9c51f3bb | -3.4111 | -44.4231 | 2025-11-04 13:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 48ff8671-853d-368b-9f8b-e553e1c64950 | -4.5745 | -43.3483 | 2025-11-04 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 2573df1e-c26c-3d50-8e9e-31809c1b5512 | -5.5758 | -42.292 | 2025-11-04 13:10:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| cad278c4-07f4-3d3d-a247-a2c55f4fbe43 | -5.5302 | -41.1207 | 2025-11-04 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| e895f271-2b8d-37b8-921b-e6febb265584 | -5.6055 | -41.1145 | 2025-11-04 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 0563da85-f6e9-3699-b696-fe91ae76bfa3 | -5.9222 | -43.3703 | 2025-11-04 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 5201b264-e07a-303c-a5e3-1885fabda463 | -5.9234 | -41.3056 | 2025-11-04 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| e03010eb-ae87-3f08-846d-e0bb5cc36388 | -2.4934 | -45.967 | 2025-11-04 13:10:00 | GOES-19 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| cb17d9c1-356a-325e-8e94-b71ccaca8ca9 | -5.9422 | -41.304 | 2025-11-04 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 6cbbc5ea-ffd2-3f09-a6ef-2fac6a59eef9 | -3.411 | -44.4459 | 2025-11-04 13:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 274.1 |
| d65c05fe-f452-337c-91ec-d0e09f46220b | -1.2269 | -49.1474 | 2025-11-04 13:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 5121eb59-c0a1-3f3c-8d5c-6d60e6177a24 | -5.6057 | -41.0903 | 2025-11-04 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 4ec72174-fdea-33b2-8d23-318c60005823 | -5.5114 | -41.1222 | 2025-11-04 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 4c61bb8f-4eaa-3858-a91d-9af41d6aeebd | -1.2084 | -49.1689 | 2025-11-04 13:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a8cd54f9-9054-3adc-b374-3b8dcca4a416 | -1.2268 | -49.1687 | 2025-11-04 13:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c876b8ab-f33b-3c04-8553-a83ee1111406 | -1.2084 | -49.1476 | 2025-11-04 13:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 4642b5d4-ffd0-39cd-bd29-9cdd4efa5346 | -3.4111 | -44.4231 | 2025-11-04 13:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f423734e-e3af-3b22-a370-b191e49eb16d | -5.942 | -41.3282 | 2025-11-04 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 36a5b008-df42-384f-a0ce-332f807bd0c5 | -6.4131 | -43.0724 | 2025-11-04 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e1e5e90c-3ee0-36d6-96d1-1028886ccf2c | -5.53 | -41.1449 | 2025-11-04 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 0156fba8-26d2-304d-9fd0-bb9dd882a18d | -1.2269 | -49.1474 | 2025-11-04 13:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7e958ced-f857-3da4-8bc8-194ade7b824c | -3.4111 | -44.4231 | 2025-11-04 13:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9fd30e74-3dcc-3a4d-bbeb-7cc06e759161 | -4.5188 | -45.9937 | 2025-11-04 13:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| de14cf5f-163d-386e-8a25-cdadc0c73db6 | -3.411 | -44.4459 | 2025-11-04 13:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 1c322754-6967-30a2-a915-148b34a06d6a | -5.9231 | -41.3298 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 180.7 |
| 313131ce-c000-3a1e-8bd2-4f57fdfcd66c | -5.942 | -41.3282 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| fc03a2ff-5a21-3fac-8b1f-02782d49b2f8 | -5.6055 | -41.1145 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| bfe62fd4-a03e-35bd-9ac0-34633d16bb4c | -5.9222 | -43.3703 | 2025-11-04 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 75.0 |
| ab36cf3e-9db5-33c8-82a5-227ec71b680f | -1.2084 | -49.1476 | 2025-11-04 13:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a4b16522-dded-3d19-89f5-63bf89c4e273 | -5.5114 | -41.1222 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| bc9bf613-08ac-3409-9dec-b8711e4b47b3 | -5.5302 | -41.1207 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 1126e37d-e2b5-33cf-b0ce-bcc7e72bdf23 | -1.2084 | -49.1689 | 2025-11-04 13:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c58c6f17-4ee4-3237-8665-314729b698a6 | -5.6245 | -41.0887 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 74c34cfa-f28a-3cd4-91fc-fefac44ef0b6 | -7.1784 | -41.9576 | 2025-11-04 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 8cf62f3f-8597-3b0b-9445-3f22176ea9df | -5.9234 | -41.3056 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| ac23bcb2-2a70-344d-9087-a44679722050 | -1.1345 | -49.2123 | 2025-11-04 13:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 49eee1ab-cd1e-38f9-b8a9-0d7da7c06739 | -3.801 | -41.575 | 2025-11-04 13:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 85a3bffd-0f79-3d53-9209-a8436c7e1180 | -5.53 | -41.1449 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| b6046031-6b72-3987-b48f-bcb593753ced | -6.4131 | -43.0724 | 2025-11-04 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 85325ff9-5752-392c-bbd6-eab6dea2c1c1 | -7.7909 | -39.8875 | 2025-11-04 13:20:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 6086fc59-1d3b-3772-85d5-d1ca093d747e | -4.5745 | -43.3483 | 2025-11-04 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f72104c1-e61d-33b8-8f25-5bccf53eecca | -5.5758 | -42.292 | 2025-11-04 13:20:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 14fd7d25-1df6-3566-a510-9ad461652eba | -5.6057 | -41.0903 | 2025-11-04 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 955f4bdd-b562-3d85-a4b0-b33c0bfa62ab | -1.2268 | -49.1687 | 2025-11-04 13:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0a2119ea-7f20-3983-9685-f9a0858d2464 | -5.9234 | -41.3056 | 2025-11-04 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 172.0 |
| 44c9aa00-f990-3011-b337-94b89911fa21 | -5.5302 | -41.1207 | 2025-11-04 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 5e11556d-1d47-34fa-b77e-6171c2db3f27 | -5.5116 | -41.0979 | 2025-11-04 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 91b6e18a-d555-33fe-8a62-9ac3c61c5ee0 | -4.4632 | -43.2386 | 2025-11-04 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 977187b8-e5cb-3f4f-8997-001079bf2338 | -7.5825 | -38.4485 | 2025-11-04 13:30:00 | GOES-19 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 01540221-7782-3df1-9273-1faf0bbf61fb | -7.0515 | -43.1551 | 2025-11-04 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 948d1bfa-8985-350d-8c63-6ef342ca4357 | -5.9422 | -41.304 | 2025-11-04 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| cc641a68-fb76-3f33-9b4a-bd982db77b03 | -7.1784 | -41.9576 | 2025-11-04 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 80fda628-720b-36d8-9ae4-a9f188024d91 | -5.5114 | -41.1222 | 2025-11-04 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 0678e75d-4bca-3a53-a0c8-72f50a1600f8 | -5.942 | -41.3282 | 2025-11-04 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 35177069-05b0-3712-8f3c-cb632379f462 | -2.1597 | -45.9095 | 2025-11-04 13:30:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| ff719094-a1a8-3a35-8564-9dfdd6ba3c01 | -3.411 | -44.4459 | 2025-11-04 13:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 166.5 |
| f2171626-e22b-30f0-8498-8bf49c5c65d8 | -4.5745 | -43.3483 | 2025-11-04 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| e4d5913f-ce3d-385c-8268-5c077ed20bca | -5.6057 | -41.0903 | 2025-11-04 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 6b8c9bd9-a237-3ac2-b5c8-9665d1231d27 | -5.6055 | -41.1145 | 2025-11-04 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 111.2 |
| 651aedc8-08a3-3b13-858f-ed4f1d949e2d | -5.5304 | -41.0964 | 2025-11-04 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| e16e1414-303a-3814-8b39-4fe36bc6d472 | -4.5934 | -43.3239 | 2025-11-04 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 438855ea-9c88-345f-8bcd-87c634b10d11 | -5.5302 | -41.1207 | 2025-11-04 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 04f7ffad-5776-3cea-9fc0-34a64ab39349 | -7.1784 | -41.9576 | 2025-11-04 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| d033755f-437a-3b39-a9ce-fd11f6746c5f | -3.8387 | -44.563 | 2025-11-04 13:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| bf367713-79b1-3f8b-83d4-4cf41fef89d6 | -1.1345 | -49.2123 | 2025-11-04 13:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1ad6ffa7-84f8-3997-abf9-7b5333dcb04e | -4.5745 | -43.3483 | 2025-11-04 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 47a059dd-5195-36a3-ac48-2a6b6e635541 | -5.942 | -41.3282 | 2025-11-04 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 304a075e-73ef-3544-b90a-b0c505b5a268 | -19.0519 | -57.5356 | 2025-11-04 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 3d02e10f-f813-3901-8d46-3848814e730d | 1.5099 | -56.0426 | 2025-11-04 13:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c6e7211b-7ad7-362e-96fc-f65afa80dc52 | -7.0515 | -43.1551 | 2025-11-04 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| ba5f435f-1042-3c8a-add1-628e3228c4b3 | -5.5116 | -41.0979 | 2025-11-04 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 243487d8-382d-336a-863e-07eb847e2f2d | -5.9422 | -41.304 | 2025-11-04 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 2852d765-2731-3773-99e4-5b414ac7ebfd | -3.411 | -44.4459 | 2025-11-04 13:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 1a3ea50f-9757-3906-b153-998cc60c52b6 | -5.5114 | -41.1222 | 2025-11-04 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 169.4 |
| e4a4743c-7681-3700-b2cf-cfafb013342c | -7.7909 | -39.8875 | 2025-11-04 13:40:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 3c53fb48-67b5-318e-8295-e604c98e9b80 | -6.9938 | -41.6159 | 2025-11-04 13:50:00 | GOES-19 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| eaf85755-223a-3b21-a96b-bcb8a379d8dc | -5.6055 | -41.1145 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 6a757b57-6265-3835-85ae-9c890dbf1473 | -5.9231 | -41.3298 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 592.2 |
| c71e28d4-0478-369a-bdc6-bdf15ab203bc | -4.4633 | -43.2152 | 2025-11-04 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 4546f7f9-c550-3a23-b96b-aa0c86a4e6ec | -4.5934 | -43.3239 | 2025-11-04 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |


[Clique aqui para ver as próximas entradas](README29.md)
