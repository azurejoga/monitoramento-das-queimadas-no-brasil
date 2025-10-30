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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00adeab4-d63f-3f85-8469-0c4cce547122 | -9.4734 | -45.5751 | 2025-10-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e8d5e151-9319-36d2-8ed9-34198c074025 | -9.2467 | -45.5556 | 2025-10-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 5e7d7388-993e-3e0c-907d-819f9d2f4ecf | -9.3181 | -45.8648 | 2025-10-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 39440bc9-05af-3aac-944f-5a96d727eedc | -8.0124 | -46.2699 | 2025-10-30 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 6c1463d2-693d-3008-b641-7f479af36db2 | -8.185 | -44.4593 | 2025-10-30 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 2fcf8bbc-222f-3bb8-925d-c5281b78ce75 | -7.6114 | -43.5914 | 2025-10-30 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 140.0 |
| a363ba70-69a6-3141-a803-1d2f6eff283e | -9.8997 | -44.9299 | 2025-10-30 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 0d8a5e89-dbd8-3b67-9e9d-218bdbcb489a | -5.2496 | -40.9731 | 2025-10-30 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 223.6 |
| bbbe44e7-2c2e-3c1e-ad1e-73ac5dfcc508 | -8.0444 | -45.1606 | 2025-10-30 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 3ad825c1-e858-3887-99a5-ad218820b715 | -4.4784 | -43.7252 | 2025-10-30 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 04bff393-2f2b-3df9-bf9f-72fa3f8d1662 | -9.4731 | -45.5979 | 2025-10-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.9 |
| f0862206-5ccb-35fe-9b21-dd90018882e6 | -6.0461 | -44.1484 | 2025-10-30 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 3f412839-4d4f-3904-9af4-0ab041ca0746 | -9.9187 | -44.9276 | 2025-10-30 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 92045b52-7d1a-3a15-890f-17a185fdbde0 | -7.6116 | -43.568 | 2025-10-30 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| dc57d1ae-4f55-321a-b80b-26cf43baadf4 | -4.3136 | -43.2474 | 2025-10-30 14:20:00 | GOES-19 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 99212e8e-891f-368f-8781-91376313549c | -5.8152 | -40.8296 | 2025-10-30 14:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 45818aac-d4b2-3bd7-b854-4136c286c637 | -3.6888 | -44.7295 | 2025-10-30 14:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e13639bc-89e5-36bb-b75c-a34f5dcaa0a4 | -10.468 | -45.0412 | 2025-10-30 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 51a10390-5cd4-3e21-b3ae-b8cdc235eb66 | -3.9949 | -43.4279 | 2025-10-30 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| bfee63f8-167c-342b-ae71-1a933d408cc8 | -8.2039 | -44.4574 | 2025-10-30 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 170.3 |
| bc0a956f-b6c7-3c0a-9d99-eface7709798 | -8.0633 | -45.1587 | 2025-10-30 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b20c261d-4d12-3e8e-9329-1d20ad9f1f7d | -3.7428 | -45.0444 | 2025-10-30 14:20:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d805dfac-480f-3548-9c83-abaff1c7485b | -5.6643 | -42.8755 | 2025-10-30 14:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 128.4 |
| 25246448-5c7e-3728-b2a9-c5572881824f | -10.4604 | -44.3258 | 2025-10-30 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 35ef612e-5af9-3ae5-9681-9a68dbbe07a3 | -7.6111 | -43.6147 | 2025-10-30 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 5b3e26b8-d81a-319a-8995-433317b71438 | 3.9353 | -59.6446 | 2025-10-30 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f1b80569-f4e0-3ced-a468-cdcacc4956a7 | -9.2464 | -45.5783 | 2025-10-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3debd512-b1e1-303c-b44d-dc50a9eb735d | -3.995 | -43.4047 | 2025-10-30 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7df206a3-f907-31d8-8aa6-9c44009b9683 | -4.2731 | -43.7139 | 2025-10-30 14:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6c83796b-af39-3819-b755-7fd72368da86 | -4.903 | -42.0085 | 2025-10-30 14:20:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 189effe9-1c3f-34cd-b234-775c48e7efc0 | -13.6513 | -47.0407 | 2025-10-30 14:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 8e7fe338-fc19-39b4-9c2f-6fe843aa15c2 | -10.2258 | -45.9616 | 2025-10-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 02c6af30-d1ba-30db-b0f6-dc73539674e2 | -10.7587 | -44.7258 | 2025-10-30 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 251.9 |
| f697965a-37e9-30d6-afa2-7622cc905ea5 | -3.6888 | -44.7295 | 2025-10-30 14:30:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a06f4db4-038b-3fac-b39c-8c5e0cd633db | -4.903 | -42.0085 | 2025-10-30 14:30:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 9fb008cc-bc85-3fdc-8400-7ddb73d90ae3 | -7.6116 | -43.568 | 2025-10-30 14:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| ef9fcf57-89cf-370e-8de5-0be1b0dc2d20 | -4.4784 | -43.7252 | 2025-10-30 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 82901ffc-35c2-319e-a45b-325e8c007a3c | -5.6643 | -42.8755 | 2025-10-30 14:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 540bbac8-da0a-3bab-9b9a-6855dd2969ac | -3.501 | -45.0326 | 2025-10-30 14:30:00 | GOES-19 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8f31166b-e47a-31a7-a744-7285cc3f20d2 | -10.7392 | -44.7515 | 2025-10-30 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6bf48ca9-9aa9-3ed5-a878-1a0b97f95ec4 | -11.6305 | -44.0413 | 2025-10-30 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 8d5ae811-6ad1-37e1-89a2-c137a10d165b | -4.2544 | -43.7149 | 2025-10-30 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 44d131a2-e7d3-3cd5-93c9-f567f2038051 | -5.8152 | -40.8296 | 2025-10-30 14:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 100.6 |
| a8fd69d3-3e09-379c-bfb3-ec71df6631cf | -3.7074 | -44.7286 | 2025-10-30 14:30:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1d308045-d5bb-392b-bd78-fe683f8c4135 | -10.4871 | -45.0387 | 2025-10-30 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 231d01e5-9620-3ad7-ad34-800e591722c4 | -9.4731 | -45.5979 | 2025-10-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 321ecb3c-de80-39c8-a979-525648a2f08c | -6.1462 | -41.5996 | 2025-10-30 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 8662b68f-22f5-3cda-98a5-cbb93cdab58a | -10.468 | -45.0412 | 2025-10-30 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 42d6c315-2d4d-363c-8cad-690b38cf0fba | -9.7223 | -45.3865 | 2025-10-30 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| d7b0a6f3-76ad-3c4e-9899-f07fde2beb2c | -8.0444 | -45.1606 | 2025-10-30 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 38ab56ee-12e7-32c9-8b54-f4861a7e515a | -7.3799 | -42.4617 | 2025-10-30 14:30:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 89be036a-f0c5-3f93-b18a-c47e536ba9fd | -4.2731 | -43.7139 | 2025-10-30 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2fbca0bf-f525-303f-bc8a-ea4beeec3945 | 3.9536 | -59.6441 | 2025-10-30 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e13ecb7f-f17d-304d-984c-1b99734d954c | -5.2496 | -40.9731 | 2025-10-30 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 383.2 |
| 682b5353-f207-312a-8277-efc9c1e43a66 | -10.4874 | -45.0157 | 2025-10-30 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 60c51637-22d2-3cfa-8ffb-dfdb7ffe07e6 | 3.9353 | -59.6446 | 2025-10-30 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9233db3c-24ac-3fe4-b93e-e762c0491de3 | -3.995 | -43.4047 | 2025-10-30 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 298483a5-0f8f-3fb9-b43c-0c1447214f97 | -10.2068 | -45.9639 | 2025-10-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 88bc11ea-a84c-3879-ba52-3386bb01003d | -11.5537 | -44.053 | 2025-10-30 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 824b952b-380a-3606-9f6b-ce0ec38573a9 | -9.7219 | -45.4093 | 2025-10-30 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 0688e3c4-e094-3ce8-8aa6-ba2b0d3f1ec8 | -7.6114 | -43.5914 | 2025-10-30 14:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 09cdb0ce-5702-3fc6-ab6b-b7682a57cb05 | -10.7583 | -44.7489 | 2025-10-30 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 890f8684-c803-3c4d-bc55-fef5412d462c | -3.4822 | -45.0561 | 2025-10-30 14:30:00 | GOES-19 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 180.4 |
| f0f6e3d1-c2c6-3cab-a8b5-7f14ab3cbc27 | -9.8437 | -44.8679 | 2025-10-30 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 62466a0e-3678-3778-88ef-002514e05bc7 | 0.322 | -51.1076 | 2025-10-30 14:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 133056f3-f6c9-360c-9a4d-d6a6aef89d3f | -9.3181 | -45.8648 | 2025-10-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ecf7704d-cf8d-3f50-9a86-1902bdba081e | -8.7928 | -42.8262 | 2025-10-30 14:30:00 | GOES-19 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 743a6abd-0189-32a3-b480-19fda77924e7 | -5.7963 | -40.8312 | 2025-10-30 14:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 0d3e2099-edd8-3ab0-8ad6-2f7b4728ca0a | -9.4734 | -45.5751 | 2025-10-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f1584379-894e-3b93-b105-a093b658e820 | -6.1455 | -41.6718 | 2025-10-30 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 9af5f7c4-1d62-3e21-ab7d-50a06b80b6e1 | -8.2039 | -44.4574 | 2025-10-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 7b9c2b2b-1712-3988-9e25-6d54c9b646d1 | -9.8997 | -44.9299 | 2025-10-30 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 1c93eeed-eea7-3696-88dd-9ec10184c2be | -10.2663 | -44.5603 | 2025-10-30 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 2d8f67e2-8d8f-3678-a2a6-3d88d4fdb2bc | -8.0633 | -45.1587 | 2025-10-30 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3564119a-6b49-3a42-89e6-b1e79bba486e | -9.504 | -46.0921 | 2025-10-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 93edac54-8d49-3945-bbd9-d91efb9983c7 | -9.485 | -46.0942 | 2025-10-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| c04f6827-1b7a-3cc0-bce0-feba54749ccb | -6.1658 | -41.5257 | 2025-10-30 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 5d0620ef-0a6d-3e85-8d17-d52f45c0e1d1 | -9.2467 | -45.5556 | 2025-10-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| d3a2e1ee-2676-3cf4-bb84-13e57de76ed7 | -6.5603 | -41.6099 | 2025-10-30 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 129.2 |
| 4702fb38-8344-3c9a-b023-c73aa301c584 | -9.4314 | -45.8746 | 2025-10-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| daea5946-130c-3cb0-bf72-a8fd42f203fe | -7.6116 | -43.568 | 2025-10-30 14:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| d494b218-1c71-324c-9e37-6a4a776a233d | -10.4684 | -45.0182 | 2025-10-30 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| d1a955b9-ffd1-3f00-8e1c-6f82ecfb6574 | -10.4871 | -45.0387 | 2025-10-30 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 498.9 |
| c8e3d327-28c0-3228-b6de-a986433fd4a2 | -10.4874 | -45.0157 | 2025-10-30 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 4b263bc3-83af-37d7-8aee-2d99e1ab93b0 | -10.2258 | -45.9616 | 2025-10-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 175.6 |
| d32359ff-89b6-3dd6-9db8-cc21e6d6dd23 | -5.8152 | -40.8296 | 2025-10-30 14:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 4e893bfb-7290-3265-9413-4471c67c5479 | 3.5672 | -60.377 | 2025-10-30 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4179c1ed-ea92-33c3-a30d-3e18185938e0 | -9.431 | -45.8972 | 2025-10-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 8d6c4306-fa6f-3b5e-bcf2-2ff39b56afe3 | -9.2653 | -45.5762 | 2025-10-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 3b713f69-8ccd-3f0c-88c9-d6d2bf4d6c4d | -4.4784 | -43.7252 | 2025-10-30 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 58832ecc-c71e-3e91-a0f9-4547f3caba29 | -9.2464 | -45.5783 | 2025-10-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 765178e9-31a9-359d-9bdf-f97d44750bb5 | -7.5928 | -43.5699 | 2025-10-30 14:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b10725d5-d899-3b10-ba9d-1e47431b7d11 | -4.2544 | -43.7149 | 2025-10-30 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| cf85c2f3-0283-379a-8ca6-7ed7ae2cb0cb | -10.4604 | -44.3258 | 2025-10-30 14:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 45140696-2768-32f1-91bf-f8da4704594e | -5.6643 | -42.8755 | 2025-10-30 14:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 95ee6d0a-a9be-3e2a-af14-829eb7b15f1c | -9.2467 | -45.5556 | 2025-10-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 800e27a1-816a-3a34-99a4-f1118388656d | -8.0636 | -45.1359 | 2025-10-30 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| d0a2cf93-947c-3a7f-b3ca-63205266f37b | -9.2278 | -45.5577 | 2025-10-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c5c3f2c7-36af-3c3b-bb25-6dc2651983e1 | -8.0633 | -45.1587 | 2025-10-30 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| a1f0290e-dd92-3b6d-9652-314f6bffc296 | -10.3878 | -45.3039 | 2025-10-30 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |


[Clique aqui para ver as próximas entradas](README71.md)
