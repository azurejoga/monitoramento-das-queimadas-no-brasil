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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e76e75-fcbb-390e-995e-8332f849648c | -3.5083 | -43.6837 | 2025-11-27 13:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 1af0f2fe-ff92-3cd3-9bf0-5728d9d691a7 | -3.0608 | -43.703 | 2025-11-27 13:40:00 | GOES-19 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 6440f71b-768e-3609-81e9-9466e23cbc87 | -2.692 | -47.3935 | 2025-11-27 13:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 10d90c20-e928-3bec-9d5a-34a2b696d38f | -6.4971 | -38.8268 | 2025-11-27 13:40:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 94b4b98b-ced8-3de1-acd9-6c7b533d0494 | -4.9474 | -41.1653 | 2025-11-27 13:40:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 72a4ddb3-bc8f-3854-bd87-a4f0ea52d934 | -6.4971 | -38.8268 | 2025-11-27 13:50:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 118.7 |
| 0e88dd8b-d19d-34c5-9559-654fdfb71389 | -2.692 | -47.3935 | 2025-11-27 13:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 4d3950a8-da15-301e-8ccf-a89ac85ab0e5 | -3.5083 | -43.6837 | 2025-11-27 13:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 27717a09-222e-324d-8830-067f5c5a0505 | -4.9474 | -41.1653 | 2025-11-27 13:50:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 809eb52c-92c1-3549-b9ac-897d4de90913 | -4.4246 | -43.4038 | 2025-11-27 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d0e07c25-64f0-377a-bf19-b2c1fa84c5e1 | -3.7334 | -43.4645 | 2025-11-27 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9ea00fb4-ecca-34d9-9df9-c5754484fd22 | -4.3872 | -43.406 | 2025-11-27 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c868b046-2d76-32e3-acf3-6822183d1628 | -4.4246 | -43.4038 | 2025-11-27 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| eff7779e-5652-3f12-a7ed-907b54556693 | -3.8563 | -41.7156 | 2025-11-27 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| cbaf8aea-bbb0-3961-9fbc-6b6ce2ea6f8a | -3.5083 | -43.6837 | 2025-11-27 14:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 236.0 |
| b462768d-c65b-34b9-b3a4-4c1ac239e2cb | -4.9474 | -41.1653 | 2025-11-27 14:00:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 9b680111-4299-307a-a3bf-c82f0fd0189f | -4.3436 | -44.3311 | 2025-11-27 14:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d966df1a-caa3-3977-a409-2bd0edbd017f | -3.5269 | -43.6828 | 2025-11-27 14:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 4d34ef42-23f7-35e1-8381-1791fbe57cff | -4.9474 | -41.1653 | 2025-11-27 14:10:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 84.0 |
| e5ee2124-058c-335d-a357-ec2c34a6a150 | -18.4017 | -56.1041 | 2025-11-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 583b710c-bcb4-3f45-a9b1-b69e7b0bdee6 | -3.7334 | -43.4645 | 2025-11-27 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 63a53416-a260-3286-96e8-5bbb79580f65 | -3.5083 | -43.6837 | 2025-11-27 14:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9981c8ff-59c8-3908-90f0-06be588d5ad6 | -4.4246 | -43.4038 | 2025-11-27 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2efc036a-eb3f-391e-94df-83f9c8119768 | -4.278 | -42.9926 | 2025-11-27 14:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 751d5f9b-d0cf-3f63-ba51-12970cc16aae | -6.4971 | -38.8268 | 2025-11-27 14:10:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 132.9 |
| 4864610e-8477-399c-9519-6e25a34ad15b | -3.8768 | -44.4242 | 2025-11-27 14:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 67589608-775f-3681-b96c-68ddff26fe8b | -4.3872 | -43.406 | 2025-11-27 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0bf6261c-580d-3453-a5f4-8d5e3befb7a1 | -3.7326 | -40.5384 | 2025-11-27 14:10:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 901048bd-c9dd-39be-bd35-b85f07f6e412 | -3.8563 | -41.7156 | 2025-11-27 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 9bdd58bf-1de6-3311-91a1-9980a9fa7cc5 | -3.8564 | -41.6916 | 2025-11-27 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 15a49e5e-8044-361c-887a-4a2ff47d70d5 | -4.5706 | -38.972 | 2025-11-27 14:10:00 | GOES-19 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 0efbf15c-1bbf-3c04-88fe-89c50d1439be | -2.6919 | -47.4153 | 2025-11-27 14:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 182.2 |
| a7a31277-96ad-3576-a61d-17d876d637fa | -3.8375 | -41.7166 | 2025-11-27 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 640c664d-5199-3edd-9a0e-58243d47436a | -3.0876 | -42.0631 | 2025-11-27 14:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |


