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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf536d6a-5cce-334a-bed5-0d281d04590d | -19.546 | -56.63441 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 133f3463-a663-360f-9bd6-1d31d34ae83c | -19.54488 | -56.63929 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aa197561-38db-302b-9dd0-52c594f0d939 | -19.54219 | -56.62314 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0b1ed8de-7a7e-3a9a-bfa8-176dd8f28773 | -19.54107 | -56.62802 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dd971864-6205-343b-92df-e4d70361adda | -19.53996 | -56.6329 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cd9a9283-f4dc-31e1-b3fa-7b9aa8d6fb41 | -30.01879 | -51.3162 | 2024-10-20 04:14:00 | NOAA-21 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 4f819b44-75a1-3d10-86bc-e5e7f827cc7a | -29.86567 | -51.1632 | 2024-10-20 04:14:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 9a967a0b-f076-3688-a317-071cf7f095e7 | -29.81473 | -51.17403 | 2024-10-20 04:14:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 8c5ec76e-7e0b-34dd-b82e-6ed9cb64451f | -29.67861 | -51.19368 | 2024-10-20 04:14:00 | NOAA-21 | ESTÂNCIA VELHA | RIO GRANDE DO SUL | Brasil | 4307609 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 2c936158-bd1b-32c7-8680-19471daaedc4 | -2.2993 | -48.5936 | 2024-10-20 04:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 72ed9e6e-7ac2-371c-b3fa-9636a62912f1 | -2.2994 | -48.5722 | 2024-10-20 04:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 26ba7efa-bb7f-37de-9211-33d08101c13c | -2.7958 | -49.3062 | 2024-10-20 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 631f9028-a0ef-366e-8518-52237ea21d50 | -2.7773 | -49.3067 | 2024-10-20 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| cfdf23cc-a595-3fe8-aa3c-2088f862a890 | -3.0293 | -51.0231 | 2024-10-20 04:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ac8b7471-62c1-36b9-8195-7ea70d031667 | -3.0478 | -51.0226 | 2024-10-20 04:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5394581e-8b71-37f6-a1d5-bd98973ba076 | -3.3813 | -50.6788 | 2024-10-20 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f6196292-1e69-3e6c-9e40-604885ba41ce | -3.3814 | -50.6579 | 2024-10-20 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9d85fdfb-b32e-359a-8864-ebe6647b6983 | -4.1985 | -46.6318 | 2024-10-20 04:15:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e07aa318-9118-3251-aaa3-d862ca33279e | -4.8758 | -48.2145 | 2024-10-20 04:15:34 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4a31dc16-d12e-3128-9c19-bc9f4cbbcd27 | -4.911 | -45.8374 | 2024-10-20 04:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c6d528af-9736-31b3-b73a-0c542c87f4d6 | -13.0082 | -55.9699 | 2024-10-20 04:16:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0dded68f-ccc3-3862-ac93-6dcc5ed77293 | -1.165 | -53.6571 | 2024-10-20 04:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a881545d-98fc-3f78-9e89-e393e278613b | -2.2993 | -48.5936 | 2024-10-20 04:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e1002b5a-1685-3ae3-8b4d-c7e6c01b9a31 | -2.2994 | -48.5722 | 2024-10-20 04:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 2546c6c2-8c0d-37d5-9b24-1cf82f351316 | -2.7773 | -49.3067 | 2024-10-20 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 373bd9ad-645c-362b-a14a-0111938d8fec | -2.7958 | -49.3062 | 2024-10-20 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 73238ff2-91a4-326e-b495-7f0086477ff3 | -3.0478 | -51.0226 | 2024-10-20 04:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a9e45960-83c7-3ff6-b8c3-18d586373d92 | -4.1985 | -46.6318 | 2024-10-20 04:25:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6ec5e1f1-a020-32fd-b621-6a2719093675 | -4.8758 | -48.2145 | 2024-10-20 04:25:34 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ebc050e3-f081-3528-8372-5a0d2d8f4bf7 | -4.911 | -45.8374 | 2024-10-20 04:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 27d0d129-55b4-33fe-a4bc-6bed7a2492a8 | -4.4577 | -42.90259 | 2024-10-20 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c86cadf8-b127-3e50-a427-b243bf6cfbac | -4.4538 | -42.90199 | 2024-10-20 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e12398c-d4fd-36a0-aa4b-a7f71d9fae7e | -3.51608 | -43.61422 | 2024-10-20 04:29:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f7e0da0-578d-3004-b1c4-ebad5b6e5602 | -4.16011 | -43.35769 | 2024-10-20 04:29:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 524a74b3-5c79-3d98-a062-75f20af0d4bf | -4.16458 | -43.35375 | 2024-10-20 04:29:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14a41888-d0cc-3ef7-96da-c66c21a56c09 | -4.16081 | -43.35315 | 2024-10-20 04:29:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6bfcc6b-97a5-3931-90b7-bbda6ffea7d9 | -4.16388 | -43.35828 | 2024-10-20 04:29:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bfbcbd7-0e3a-36b6-9905-76ee81dc4e4e | -3.67485 | -43.70256 | 2024-10-20 04:29:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc342145-56b2-3fea-b26e-a2ffcb6c727c | -2.30104 | -48.58751 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 928ffb16-16f5-39fa-b62f-91954edf629f | -4.2366 | -41.92999 | 2024-10-20 04:29:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 315d05c2-a3af-3c2c-9917-7889c308f729 | -3.47684 | -43.94653 | 2024-10-20 04:29:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e74ad93-ec02-32d7-805b-9552ae4ae5ac | -4.09743 | -44.22381 | 2024-10-20 04:29:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67bcd1c3-5589-3a91-b835-b2adadf920f7 | -4.0968 | -44.22791 | 2024-10-20 04:29:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3ecc5b1-1dc8-3479-9a8b-f283ff72ea1d | -4.0932 | -44.22736 | 2024-10-20 04:29:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8821d1ee-612f-3753-999b-50b04d3c11a8 | -4.05801 | -44.31383 | 2024-10-20 04:29:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0be94358-710a-3326-aefc-e5509e7368f9 | -3.77396 | -44.43395 | 2024-10-20 04:29:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d0d3b63-5d2a-362a-8eca-47c09600a145 | -1.96943 | -45.59452 | 2024-10-20 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ec671c6-a6d2-36bb-bb7f-4f6e33eda6be | -1.96607 | -45.59401 | 2024-10-20 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 417afbbb-0a49-396a-8ab8-d83af066a66a | -1.96271 | -45.59349 | 2024-10-20 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 262f86a3-71cb-3135-9d3e-283d475b51f7 | -1.95935 | -45.59298 | 2024-10-20 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5f1cebc-5989-3832-8a4f-c750ad3dfd64 | -1.95654 | -45.58891 | 2024-10-20 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 015e88c1-75f1-3ffb-aac5-152939328a29 | -1.95318 | -45.58839 | 2024-10-20 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c02799f-bae4-37ca-97fe-d858798816b9 | -1.94982 | -45.58787 | 2024-10-20 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71013367-24b7-38ca-af61-5ed87e07ae71 | -3.60335 | -44.78859 | 2024-10-20 04:29:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8962a30a-3a51-3050-b512-67715e4b5943 | -3.09339 | -45.9119 | 2024-10-20 04:29:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 208ac156-955f-3179-a3fd-4e0dd7eac1b6 | -2.99363 | -45.61253 | 2024-10-20 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6886e813-2a92-35a5-80a0-57198ed4e012 | -2.99025 | -45.61201 | 2024-10-20 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a340d97b-4a3e-352d-897f-7aa85be32152 | -2.75668 | -45.36272 | 2024-10-20 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63ae3f25-83b6-32de-be5a-972c8b5c0c65 | -2.65297 | -45.5093 | 2024-10-20 04:29:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4cb3e75-0b8b-3765-8dea-63206435fe13 | -2.65241 | -45.51289 | 2024-10-20 04:29:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d31414a-b5b6-350a-a1bd-f8df62c011de | -3.91375 | -45.75292 | 2024-10-20 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cb8650c-7d72-3468-a884-d372f79f02a7 | -3.86421 | -45.82618 | 2024-10-20 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c6de6f5-5d04-31aa-8713-6a81fcca56c9 | -3.72499 | -44.53993 | 2024-10-20 04:29:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bab251a9-e2ce-377c-886c-4ccd2408f3fa | -3.91431 | -45.74931 | 2024-10-20 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aaa1e49-c8dd-36d0-a446-0a2f91ef4234 | -3.91036 | -45.7524 | 2024-10-20 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96d32b81-1c0f-3d75-81de-ef8ba970df3f | -3.86477 | -45.82259 | 2024-10-20 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae6b16b1-ab94-3112-85fe-e45cf45fd250 | -3.86083 | -45.82566 | 2024-10-20 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a0551e6-2bfd-3f43-9288-bcfb73267993 | -3.77802 | -45.90767 | 2024-10-20 04:29:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccf15836-c393-3470-ae02-61458b6fffa1 | -3.77746 | -45.91122 | 2024-10-20 04:29:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa3fc976-b63b-37c5-9053-54ccfc1c321e | -3.69717 | -45.89518 | 2024-10-20 04:29:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be704d68-11a1-3049-8f80-28557f409200 | -3.6635 | -45.74744 | 2024-10-20 04:29:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d515c0d-061a-3c52-9c25-1cbb326eda0f | -3.54963 | -45.82918 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eabdd1a-91c9-3980-9fd8-4e6fdceac299 | -3.54626 | -45.82866 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da5aea4d-893b-3271-b645-2a4e54bf2f1b | -3.54289 | -45.82813 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b7d5425-e2b1-36c0-9661-d08352b493b1 | -2.16396 | -46.27262 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c869d3ae-bfb3-3db7-a442-a8270e78ede4 | -2.01129 | -46.21356 | 2024-10-20 04:29:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34671592-cbd7-3b97-83e0-18021aad1c1e | -2.5737 | -47.06466 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ba851d4-c24b-3e60-8d28-870a419819bb | -2.57316 | -47.0681 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7baea276-9a34-3edd-ad11-240c36647921 | -2.57262 | -47.07155 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d97c89a-ef6b-381e-b8a7-2ec1d5ac4dbf | -2.57038 | -47.06414 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39013b3d-d859-3766-82fa-ba35a870e388 | -2.56652 | -47.06707 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d62c0137-9db3-314a-a951-5b0090ca84af | -2.5632 | -47.06656 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 911f8c85-af59-3ec5-a413-0af1c7cfe9e0 | -2.56266 | -47.07 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3446a29-2783-3803-baee-c074f8608659 | -2.55384 | -47.2986 | 2024-10-20 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62bc4d00-9077-37dd-9932-f89dcfcc4acb | -2.54785 | -47.12072 | 2024-10-20 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2acdb9fd-6ba7-38af-adac-bcf9e8629e43 | -2.54731 | -47.12417 | 2024-10-20 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5423dbeb-a0bc-3ba8-afd1-497651881df2 | -2.51849 | -47.34983 | 2024-10-20 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83e7a23a-317d-376f-9ddb-ff0f0808f99f | -2.51516 | -47.34931 | 2024-10-20 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20e9ed12-0b4e-37b2-9863-3ed30e5da244 | -3.09178 | -45.94418 | 2024-10-20 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1053d9e1-9d96-3160-8d87-e3066324ef0d | -3.09123 | -45.94771 | 2024-10-20 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db723ac3-7946-3e2c-9d58-71b95bc40548 | -3.08787 | -45.94719 | 2024-10-20 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8120a80-58db-337e-9b81-ee1154cc1ea9 | -3.08732 | -45.95072 | 2024-10-20 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad16b23b-dc6b-3e68-b070-ed86d0d4709d | -3.08677 | -45.95424 | 2024-10-20 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45634a53-fd1b-381b-8565-e87cbe89e8d4 | -3.08342 | -45.95372 | 2024-10-20 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ef05704-5398-3497-9a06-25e54c17c437 | -3.08287 | -45.95724 | 2024-10-20 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6795d4dc-c3c0-3a98-a2a8-51edc362f418 | -2.65535 | -46.05307 | 2024-10-20 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6022f39-005e-37a1-a5b7-852041abfe2d | -2.65201 | -46.05256 | 2024-10-20 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 943b2e99-3827-3098-bbae-9766f929bcd7 | -2.51536 | -45.99199 | 2024-10-20 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28395f11-e801-38dc-9ae4-b30de953cbe5 | -2.51256 | -45.98798 | 2024-10-20 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a5d5da7-e689-35c7-80a0-41bc6b6f5331 | -2.51201 | -45.99147 | 2024-10-20 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
