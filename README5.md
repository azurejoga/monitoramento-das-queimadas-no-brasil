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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af553714-5e4e-35bc-91c2-e7769fa32ecf | -16.6619 | -49.364 | 2025-11-08 00:20:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 01929b44-253d-33ae-b901-88f0311f2b08 | -4.1161 | -48.0136 | 2025-11-08 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d84fe2d7-fbc1-3c23-aa73-069305c46d12 | -3.6601 | -50.2711 | 2025-11-08 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1cd9a509-febd-3578-8217-02b20052f20c | -4.2812 | -48.3303 | 2025-11-08 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 04647d44-3f45-3f6a-85b6-4a8aa6befb82 | -8.0184 | -38.5467 | 2025-11-08 00:20:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 191.0 |
| 92727759-cf9e-3723-85aa-1ced96d2219c | -8.0379 | -38.5186 | 2025-11-08 00:20:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 217.9 |
| 83d5f9b4-8a84-3dc5-a312-67d1594d22ef | -4.3846 | -49.6723 | 2025-11-08 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 36878807-abca-3889-8c30-e082de914bdb | -4.7021 | -46.4064 | 2025-11-08 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 73fea1b0-3474-31df-a079-9167ad96ceaf | -4.3846 | -49.6723 | 2025-11-08 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 98ad8e1b-8edc-31e1-8592-fc5c62a457a5 | -3.3464 | -50.1979 | 2025-11-08 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 725afcc8-ff9c-3b25-8440-19d5b33d74cf | -20.1893 | -47.3735 | 2025-11-08 00:30:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 3548b1c0-5fa4-3d29-8ea1-996797e23983 | -3.3279 | -50.1985 | 2025-11-08 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 13be47cc-425d-3306-a73f-e629a5edf94f | -20.2091 | -47.3923 | 2025-11-08 00:30:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 98.9 |
| cca54e62-d0fe-3ad3-b3ce-9814d95252c6 | -3.4058 | -45.4424 | 2025-11-08 00:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 3a738a6b-5cf4-3f59-9463-60b2ee33bf34 | -4.6834 | -46.4296 | 2025-11-08 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6ee0d0cd-4c3c-3e53-a53d-7509e5d25000 | -3.3463 | -50.2189 | 2025-11-08 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 89cbbd4f-eb4e-3e91-8563-2c2f4c85f4e0 | -4.6835 | -46.4074 | 2025-11-08 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 411.1 |
| dac53c09-bfb8-32a3-83a8-31f23f012db1 | -4.6837 | -46.3852 | 2025-11-08 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 142.1 |
| d4f9f574-bcdb-3d54-b849-1f909fe295f1 | -4.482 | -43.2141 | 2025-11-08 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f9c75a6c-12b8-3c08-83eb-f976df796d4f | -20.1886 | -47.397 | 2025-11-08 00:30:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 6d36ec8b-5a3a-3d19-a3fc-65e2bf8ecc71 | -4.4633 | -43.2152 | 2025-11-08 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 09dc6f43-87d0-3e69-9446-9ddb0bb85d38 | -4.1161 | -48.0136 | 2025-11-08 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| bca2ebde-13ea-351d-9797-f02eeaa64186 | -2.7026 | -49.5422 | 2025-11-08 00:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 19668508-bd9c-35f8-9d66-03831c243780 | -20.1893 | -47.3735 | 2025-11-08 00:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 96df72fc-9eec-3991-9796-6d337edb43c6 | -4.3846 | -49.6723 | 2025-11-08 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c4819a22-a946-3bf5-aa93-ed628aa96542 | -4.482 | -43.2141 | 2025-11-08 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 4a928d4e-76cf-3dcb-a70e-dfde7fc66852 | -20.1886 | -47.397 | 2025-11-08 00:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 278.3 |
| c7c0bab4-5bc1-336e-8e44-242c20bd4e31 | -20.2507 | -47.3592 | 2025-11-08 00:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 83cf6211-d485-3faa-a146-ee40e11053d0 | -4.7021 | -46.4064 | 2025-11-08 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 40f9eebd-a857-39a6-9206-47d10edfea44 | -9.6261 | -36.0973 | 2025-11-08 00:40:00 | GOES-19 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 156.7 |
| 3f6f4dcd-61b7-3c39-b657-559b1ce342ac | -3.3463 | -50.2189 | 2025-11-08 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 345870db-71ea-3dd3-a793-620d4d787e24 | -3.3464 | -50.1979 | 2025-11-08 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 00bceee3-94de-3efd-9a63-5be2e9cea602 | -4.6837 | -46.3852 | 2025-11-08 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 39dd44e0-5acd-3a32-ba29-c3ff4aba92d0 | -3.4058 | -45.4424 | 2025-11-08 00:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 467ef526-b926-3238-a9e4-573eaa103ba4 | -20.25 | -47.3827 | 2025-11-08 00:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 106.4 |
| c0365a48-7d1e-364f-970d-55da769fbcf4 | -9.6068 | -36.1006 | 2025-11-08 00:40:00 | GOES-19 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 98.6 |
| e9a67b61-ca29-3060-8a1d-75dc606feefc | -4.4633 | -43.2152 | 2025-11-08 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 13bf89d0-c436-369c-874c-a3dc9533f61b | -4.6835 | -46.4074 | 2025-11-08 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 258.2 |
| 5fc06ca6-d041-3beb-a880-19c667d4d80c | -4.7023 | -46.3842 | 2025-11-08 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 5d9570a1-69b3-35a9-a0c4-4f462e78d5be | -4.6837 | -46.3852 | 2025-11-08 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.1 |
| cb1152c6-74cc-30f5-b939-960f8c45a417 | -3.4058 | -45.4424 | 2025-11-08 00:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 9029555b-8d04-3ff8-8156-6e47fab1b97a | -20.2507 | -47.3592 | 2025-11-08 00:50:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 9d8f0b0e-efc6-347e-9eb7-6b4e1f17721b | -4.6835 | -46.4074 | 2025-11-08 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 208.1 |
| a84d6739-715e-31a4-ad4d-ab44346af529 | -20.1886 | -47.397 | 2025-11-08 00:50:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 273.6 |
| 44869e78-fd64-33db-9e35-79abf926d328 | -20.2295 | -47.3875 | 2025-11-08 00:50:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 114c10f9-443d-3c38-971e-af89b8ec86c5 | -20.2091 | -47.3923 | 2025-11-08 00:50:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 2ffdc3ea-c3d6-3906-a63a-cbba387f7d8b | -4.7023 | -46.3842 | 2025-11-08 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 234d13ca-8a70-39dc-9c64-a367ba364a87 | -20.25 | -47.3827 | 2025-11-08 00:50:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 1e4a2ea7-3811-3757-bed3-a1fdf371935a | -20.1893 | -47.3735 | 2025-11-08 00:50:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 148.9 |
| b8d5f6e4-c595-364a-9d61-f12e585d46fc | -4.1161 | -48.0136 | 2025-11-08 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 360519d8-b8e6-3038-9dd5-2bf425139fc4 | -4.7021 | -46.4064 | 2025-11-08 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 3055ec6c-4ef0-35cf-8233-4c85555efd74 | -3.3464 | -50.1979 | 2025-11-08 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 9b083568-b547-3d1a-b6cc-4e5bb47d44e7 | -4.3846 | -49.6723 | 2025-11-08 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d3f85c8a-8367-3f3a-b66e-338b03aa9902 | -9.6261 | -36.0973 | 2025-11-08 00:50:00 | GOES-19 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 130.8 |
| 72af8892-c014-3496-8eed-0beef5a3adc2 | -4.4633 | -43.2152 | 2025-11-08 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 77af6f22-6df7-3a92-9fd3-f32014918b45 | -3.6601 | -50.2711 | 2025-11-08 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b24a804a-35b3-32be-80b3-43c31774c326 | -9.6068 | -36.1006 | 2025-11-08 00:50:00 | GOES-19 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| 0c98c7a0-e56c-39d1-9e33-39679adb799e | -4.7021 | -46.4064 | 2025-11-08 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 183.2 |
| ca9da036-3acf-3c61-82d7-d2b9ddead41b | -10.2789 | -67.2815 | 2025-11-08 01:00:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 01812802-dd2f-30a4-9ed1-c606fb53e3d9 | -4.6835 | -46.4074 | 2025-11-08 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 217.2 |
| df54d8bd-e0ae-34ec-9474-0e42c02a194c | -3.3464 | -50.1979 | 2025-11-08 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a148d790-289e-3583-a1bc-a74332654e7d | -8.0379 | -38.5186 | 2025-11-08 01:00:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 68.3 |
| f9434c41-ea11-3a13-bbaa-81729843bc50 | -3.4058 | -45.4424 | 2025-11-08 01:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 8069890a-8687-395e-a6cd-d3d00c38480e | -20.1893 | -47.3735 | 2025-11-08 01:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 93009c8e-f63c-320e-aba1-eb63f0423936 | -20.2097 | -47.3687 | 2025-11-08 01:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 12c8f000-11e0-3c23-be6d-b970f7e506f4 | -4.6837 | -46.3852 | 2025-11-08 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 189b965e-eed4-337b-8d82-8852166a3ffc | -4.7023 | -46.3842 | 2025-11-08 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f63962d7-e04f-376f-8c8c-d78d30aa25d5 | -20.1886 | -47.397 | 2025-11-08 01:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 158.5 |
| a13ac43a-9613-3e16-91b6-0b0c4bebb87a | -20.25 | -47.3827 | 2025-11-08 01:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 5c15ad9f-7293-3d0d-b670-36c6f0ba6eac | -20.2507 | -47.3592 | 2025-11-08 01:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b2170ef5-04a6-3cfc-8808-a43dd53a7513 | -4.4633 | -43.2152 | 2025-11-08 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 1b7e27af-ede5-3444-b510-404c13cb32d8 | -20.2091 | -47.3923 | 2025-11-08 01:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a0a0942a-ee83-3da8-978b-23dd43cb440a | -10.279 | -67.2628 | 2025-11-08 01:00:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0978454a-067a-3771-837e-69d5174127a5 | -8.0375 | -38.5442 | 2025-11-08 01:00:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 40.3 |
| e01cb29f-9887-3cd2-aa9e-49468c021b42 | -3.3463 | -50.2189 | 2025-11-08 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 01c95318-1508-3329-9cc6-66e66d722a2c | -20.2295 | -47.3875 | 2025-11-08 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 80.6 |
| e8d33fb7-3617-37b0-a122-bfe25dc8b11a | -3.3463 | -50.2189 | 2025-11-08 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6d14c540-a093-34bd-ba4a-9cfde442a3aa | -20.25 | -47.3827 | 2025-11-08 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 116.6 |
| c106eef8-063b-3e51-88c5-28786ed814de | -4.7023 | -46.3842 | 2025-11-08 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 65472bbd-4916-3e26-87fb-3ddb65be0f4a | -4.6837 | -46.3852 | 2025-11-08 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| e9eb4a76-8ff8-300e-a10b-0c60b4bd577c | -20.2507 | -47.3592 | 2025-11-08 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 56761cd6-ab4f-304a-bfbe-161250a2315e | -3.3464 | -50.1979 | 2025-11-08 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d7a9513d-3dcb-361b-91ff-f62c4cfa842d | -4.6835 | -46.4074 | 2025-11-08 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 2fb0f779-ac64-33b9-a51a-b74f2655ff33 | -20.1886 | -47.397 | 2025-11-08 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 5a52e08e-d55e-35c4-a52f-dd7b789fcf1a | -20.1893 | -47.3735 | 2025-11-08 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 8dc01652-85af-3913-8329-41f34477ff92 | -10.2789 | -67.2815 | 2025-11-08 01:10:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 44a94487-1943-3c07-a36c-f785a12ed5f3 | -20.2091 | -47.3923 | 2025-11-08 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e8ec6c61-6ca7-342e-88ee-56fc58715517 | -5.1723 | -41.2212 | 2025-11-08 01:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| e3233353-694c-3cec-b26d-4df85bbf2f00 | -4.4633 | -43.2152 | 2025-11-08 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| c0162651-23b1-3155-96ef-d30832cb3ee8 | -5.1535 | -41.2226 | 2025-11-08 01:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 135.1 |
| e0f52169-a74f-316d-a27e-bbfade1512c0 | -10.2975 | -67.2809 | 2025-11-08 01:10:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9321a7f3-1f3d-3981-943d-086aa74c387a | -3.4058 | -45.4424 | 2025-11-08 01:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 1968c7e6-d941-3f49-9221-84e0c562d1b0 | -4.7021 | -46.4064 | 2025-11-08 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 029e4afa-32c2-3aab-8f09-f2588575fe5e | -20.1893 | -47.3735 | 2025-11-08 01:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 73fbffe0-a8b5-3eb4-89fb-539d360662ef | -10.2789 | -67.2815 | 2025-11-08 01:20:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e75631be-45b8-39e8-a02e-b8ad8f335658 | -4.6835 | -46.4074 | 2025-11-08 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 3321c0bb-2111-384d-b7eb-864e888240d0 | -5.1723 | -41.2212 | 2025-11-08 01:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 59450185-a48b-3026-a9df-069e2dc5283c | -10.2975 | -67.2809 | 2025-11-08 01:20:00 | GOES-19 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 27139bfa-ab09-3825-8db1-2d81779a753c | -3.3464 | -50.1979 | 2025-11-08 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e6a77c09-4676-3435-ac3b-46be98dcbd2d | -20.2507 | -47.3592 | 2025-11-08 01:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 83.7 |


[Clique aqui para ver as próximas entradas](README6.md)
