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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffb698c8-3e50-3be5-ab46-6f0c06dea615 | -3.4899 | -43.6383 | 2025-11-06 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 75748be0-d3a8-392c-8d73-413b12bc5ee2 | -4.7857 | -45.1249 | 2025-11-06 01:10:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8eed458a-8c00-31eb-a334-9719d85d1c5d | -9.5343 | -40.3282 | 2025-11-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 120.9 |
| 3faceb36-97b3-36fe-a07a-a0fabd0b9c36 | -4.1161 | -48.0136 | 2025-11-06 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| f523be99-e289-3450-adb9-8074a52329b3 | -4.5745 | -43.3483 | 2025-11-06 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d813eed9-9a80-32c9-b809-8eb7b73a1510 | -3.4712 | -43.6392 | 2025-11-06 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 9c6d72a1-2c6d-3af3-8385-d525bcae0a37 | -4.4632 | -43.2386 | 2025-11-06 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| cf7f2b76-95e6-37e5-b87d-31347ef1bfe9 | -4.2824 | -45.1305 | 2025-11-06 01:10:00 | GOES-19 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| e7d2802f-fc19-3faa-a78b-457f4783ba17 | -3.4231 | -54.0172 | 2025-11-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 56769e77-e888-32fa-8d6b-3154deeb7c97 | -4.6121 | -43.3227 | 2025-11-06 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 91a65454-d4d9-3ffd-8abf-2fdb7e8ab8c5 | -4.0292 | -46.9923 | 2025-11-06 01:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 99a63f60-3f2e-3b6a-b1c2-7c38f87b437e | -5.1531 | -41.271 | 2025-11-06 01:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 2daaebba-5a35-33d7-9836-2c556c65854e | -3.4526 | -43.64 | 2025-11-06 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| cdd02063-5c45-3ac0-bff3-a673c793a6fa | -4.5747 | -43.325 | 2025-11-06 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d7bf00f2-19fa-3d14-a5e7-2a4054870422 | -4.5932 | -43.3471 | 2025-11-06 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 291.7 |
| 8164e618-9d04-3aa7-916a-62c97aa0bade | -4.5934 | -43.3239 | 2025-11-06 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 302.1 |
| 0d8d916e-5d20-3d9e-8325-9a2c53260aa4 | -3.4525 | -43.6631 | 2025-11-06 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 53f058d9-12e4-331f-960f-9d6249edd645 | -3.4712 | -43.6392 | 2025-11-06 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 387.9 |
| 8521ab3f-1582-3cd2-9bf3-fad30b9b4449 | -5.1533 | -41.2468 | 2025-11-06 01:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| d4a2685d-0bb1-38d8-8a80-acd88a67b78f | 0.4283 | -60.4874 | 2025-11-06 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 840ba996-efec-3d54-828d-51727bdffd34 | -9.4761 | -40.3862 | 2025-11-06 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| f1394748-780b-39ab-8290-f27e6f4ac3a4 | -3.4714 | -43.616 | 2025-11-06 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 015374ec-72b2-3054-9497-3bb3ba8ec1ba | -4.4633 | -43.2152 | 2025-11-06 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e75a8254-b3c9-38e4-b5ad-40829bb702e3 | -4.0477 | -46.9915 | 2025-11-06 01:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 4bf1afc0-6468-3561-a5ec-9d7f7757c419 | -2.986 | -52.8146 | 2025-11-06 01:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 71b2e84c-4934-3c6f-9abf-0dec2434d2c4 | -4.7857 | -45.1249 | 2025-11-06 01:20:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 0892e5ce-2ad3-3793-8745-65a8ddfe87f1 | -3.4898 | -43.6614 | 2025-11-06 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 191800f7-d6d5-399b-999c-62835fa60838 | -4.5745 | -43.3483 | 2025-11-06 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 3276da24-b432-3690-a941-cebc16baf5dd | -3.4899 | -43.6383 | 2025-11-06 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 6e5702c6-107c-3a7f-b0a9-a767e62b1cf9 | -9.5534 | -40.3254 | 2025-11-06 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 07078838-ed43-3da0-b213-8fc25fea28d7 | -4.6121 | -43.3227 | 2025-11-06 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 79ff0c87-5fe8-34ad-afa1-4eb16aa538b1 | -4.0476 | -47.0134 | 2025-11-06 01:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9f94d1df-c83c-3467-8707-8b0a59c3649c | -3.4711 | -43.6623 | 2025-11-06 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 254.6 |
| c86b2ada-3d46-314c-8700-552176bfae39 | -9.5343 | -40.3282 | 2025-11-06 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.0 |
| b9899a0b-ff83-354b-96bf-de36b0d9f156 | -4.0292 | -46.9923 | 2025-11-06 01:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| d36c0f58-18ed-3bb1-af97-876352227c75 | -4.1161 | -48.0136 | 2025-11-06 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 64fca189-ac97-38d7-b63b-bd57b87b17b6 | -4.0976 | -48.0144 | 2025-11-06 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 77b0d183-d655-333b-94e1-0cfb0542f799 | -9.553 | -40.3503 | 2025-11-06 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.6 |
| b3949dd4-7332-35fc-91a1-4e8d2087af64 | 0.4466 | -60.4873 | 2025-11-06 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 32c13720-1d5c-382e-80f5-a4e9579835dd | -4.4632 | -43.2386 | 2025-11-06 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| fc11f187-9bc2-39a6-a734-92ec73b7968f | -4.2824 | -45.1305 | 2025-11-06 01:20:00 | GOES-19 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 963423b0-6b8e-31b1-9232-58d3c7702b83 | -4.6119 | -43.346 | 2025-11-06 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 1559ed7b-2687-32f6-8a22-86f5b2c31691 | -4.7857 | -45.1249 | 2025-11-06 01:30:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9210c97d-c89a-3910-aa0f-fdba88cb6e01 | -4.6121 | -43.3227 | 2025-11-06 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 35c1828e-620e-3065-b7b1-0d77d206b63e | -4.5745 | -43.3483 | 2025-11-06 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0b43e043-e50f-38b2-a9f3-491447417e9d | 0.4283 | -60.4874 | 2025-11-06 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d09f37fb-9bea-3617-a046-c6a3a3700927 | -2.986 | -52.8146 | 2025-11-06 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 82201589-48d1-3bda-9b71-98aa4c69ddbd | -4.5934 | -43.3239 | 2025-11-06 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 261.1 |
| b023d39f-0e48-30f7-adc3-232432557db5 | -3.4714 | -43.616 | 2025-11-06 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 0b0bb95e-30db-3224-ace0-8c910229cecc | -3.4898 | -43.6614 | 2025-11-06 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| aaaff388-6597-31c5-86ad-7773168bef86 | 0.4466 | -60.4873 | 2025-11-06 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 38f3feaa-16bd-32b5-9106-a1881302a2b3 | -3.4711 | -43.6623 | 2025-11-06 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 296.1 |
| 204373cd-5175-303b-9762-df993038e37c | -5.1533 | -41.2468 | 2025-11-06 01:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 99bacc01-aa06-3d4b-9c50-aba6e3906dc4 | -4.5747 | -43.325 | 2025-11-06 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5f50f790-cc47-3f7f-875c-244fe2196c94 | -4.4632 | -43.2386 | 2025-11-06 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 78c5c08d-47e7-399b-888e-460d97b5a173 | -4.0292 | -46.9923 | 2025-11-06 01:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2bfa4a77-608a-3c55-8343-0d65d844548d | -4.0976 | -48.0144 | 2025-11-06 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a725fa52-1a37-329d-bcd3-df58ea8168cc | -3.4526 | -43.64 | 2025-11-06 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7ae1e13f-4d7a-3a23-bab8-b5cbb2673368 | -3.4525 | -43.6631 | 2025-11-06 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 8123addc-5b64-3a74-bd00-df751c6d7f9c | -4.5932 | -43.3471 | 2025-11-06 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 45132c29-ecbc-3e76-ba74-d5f34c8978a0 | -9.5534 | -40.3254 | 2025-11-06 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.2 |
| aaeaa589-f3ba-3b8c-baf8-cb1e347f7879 | -4.6119 | -43.346 | 2025-11-06 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| e56b867d-bc0d-3917-ab72-ac006b3c433a | -3.4712 | -43.6392 | 2025-11-06 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 397.8 |
| 634f0f49-f91a-3790-8ac0-7abdfb739a0d | -3.4899 | -43.6383 | 2025-11-06 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| c88703f9-e350-3319-a224-4ce4d8c182ed | -4.0477 | -46.9915 | 2025-11-06 01:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 131.5 |
| c6e1b0e2-c34c-3957-9c02-089ea2ce5d22 | -4.1161 | -48.0136 | 2025-11-06 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 219c3caf-1c70-3347-8af4-9b091cf9436c | -7.2891 | -45.4589 | 2025-11-06 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 39fac5ff-0946-3dba-a599-d4f943a49333 | -3.9324 | -47.6962 | 2025-11-06 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 89281700-de0a-3dcb-88f6-eb3bab35c1e8 | -4.4633 | -43.2152 | 2025-11-06 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6a349da4-63c2-38ed-9ddb-8c3f8011a87a | -4.5745 | -43.3483 | 2025-11-06 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 06d6edd8-7905-3716-a351-cc212adc133b | -10.087 | -36.1511 | 2025-11-06 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| f53f936d-ae97-3d95-953a-e46347f2c5c5 | -3.4898 | -43.6614 | 2025-11-06 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 93cb175a-342d-3d92-921e-ac6fee046502 | -4.0292 | -46.9923 | 2025-11-06 01:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 663aa3c9-e9b4-34b4-8e13-d07273567e4d | -4.5747 | -43.325 | 2025-11-06 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ca5a906f-b484-310c-a3ab-56590449cbeb | -4.6121 | -43.3227 | 2025-11-06 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 723bd5b8-4f80-3f99-be5c-d15afd01c464 | -9.5534 | -40.3254 | 2025-11-06 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 124.8 |
| 46f32541-b6b3-358e-8867-2f0092d5dfbc | -5.1533 | -41.2468 | 2025-11-06 01:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| b7f40cdd-1471-3dd1-81c0-c26eccdfe246 | -4.5932 | -43.3471 | 2025-11-06 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 204.7 |
| c791ccc7-0320-3133-8f5f-9e7233581b2c | -4.1161 | -48.0136 | 2025-11-06 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 31f188df-7446-3246-aebd-10c9f185030b | -10.0494 | -36.1038 | 2025-11-06 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 232.4 |
| 6193695b-50a5-3d6b-9076-c856729c4ea2 | -3.4714 | -43.616 | 2025-11-06 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 1b9a187a-ddad-37d4-822a-327b4a2d73b3 | -10.0677 | -36.1546 | 2025-11-06 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.0 |
| 185195fb-3796-3949-832e-7f707e5c2850 | -3.9324 | -47.6962 | 2025-11-06 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 1dfb272d-223a-3009-b118-26984528082e | 0.4283 | -60.4874 | 2025-11-06 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 08808db3-17c2-3b19-82d4-0381d880a7e4 | -5.1531 | -41.271 | 2025-11-06 01:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 5ce0efa0-1a7f-3f26-8964-7484b6a88fd3 | -4.6119 | -43.346 | 2025-11-06 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 07822fd0-f013-3539-8b38-8ad5e189656a | -4.5934 | -43.3239 | 2025-11-06 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 010849e1-0637-3225-a5b1-3c940104f9a1 | -10.0875 | -36.124 | 2025-11-06 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.6 |
| 69a431d6-27c9-3698-823c-bc8789120916 | -4.4633 | -43.2152 | 2025-11-06 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 768e6c71-d262-33c3-9269-1433b66ec525 | -3.4711 | -43.6623 | 2025-11-06 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 1af65564-1dc5-3d45-9b0a-dd4bce203eae | -3.4712 | -43.6392 | 2025-11-06 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 250.8 |
| afce4802-e6a7-3934-baed-9f3ed1bf2420 | -3.4899 | -43.6383 | 2025-11-06 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| aa6d1cfc-ff2a-3f68-a410-d926bab6e7e0 | -4.0477 | -46.9915 | 2025-11-06 01:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 041854c8-38d0-31c3-8976-f02ee6bd1bce | -4.4632 | -43.2386 | 2025-11-06 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 2e6a98dc-8616-3317-bc6b-9387167aded1 | -2.986 | -52.8146 | 2025-11-06 01:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 6f189b33-1128-3337-8953-3d2e980161dc | -9.553 | -40.3503 | 2025-11-06 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 3f283757-0d40-3318-8572-3febd38012cf | 0.4466 | -60.4873 | 2025-11-06 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 49bc9b36-9324-3203-bdab-e83cd5c40c5b | -9.5534 | -40.3254 | 2025-11-06 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.6 |
| c2106a1e-b025-3969-b1e1-a6bc93b741e1 | -4.4632 | -43.2386 | 2025-11-06 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| cb7a8c52-4cf6-3d0e-91b4-4155b41666ce | -4.1161 | -48.0136 | 2025-11-06 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |


[Clique aqui para ver as próximas entradas](README9.md)
