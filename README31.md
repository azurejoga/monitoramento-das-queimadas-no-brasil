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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f58dddf9-cf4a-3a47-afac-1d94d16e8dc4 | -11.1659 | -46.6323 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d90d1636-8b2c-3ecb-9566-cb6ce2b676f7 | -10.5137 | -47.0055 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 19c56b4c-94d2-3032-8535-0b1ce5853df5 | -11.1465 | -46.6573 | 2025-06-20 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 3006a8db-32cf-3998-b291-3a8d4b201bb5 | -10.4944 | -47.0302 | 2025-06-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b74d18c1-8f64-38f7-8f98-709611a91402 | -11.1274 | -46.6598 | 2025-06-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5fa78003-c313-399e-bcac-d051584754fd | -10.5521 | -46.9785 | 2025-06-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 55185345-8252-31a5-a9a0-bb73687ad268 | -11.1461 | -46.6798 | 2025-06-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| bcf7da15-d75d-3ee4-878c-9b24fd7b9453 | -11.1465 | -46.6573 | 2025-06-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 317.4 |
| fb9b0aa5-26aa-352d-96d6-5e17be1d5627 | -11.1659 | -46.6323 | 2025-06-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 837a0286-e3a4-3da4-8a21-f15e2dcaff74 | -14.0404 | -53.3669 | 2025-06-20 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| e5a18d1b-8193-37f8-bfb2-96a49247b3cc | -11.1656 | -46.6548 | 2025-06-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 1e4598ed-fd78-3c3f-9a32-d909bd5b596e | -11.1468 | -46.6347 | 2025-06-20 06:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| d97097de-4bbf-3d0a-8ae1-acdc697a530f | -11.1461 | -46.6798 | 2025-06-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a0b00836-d3ec-3bfb-8ca1-8a26681797ff | -11.1659 | -46.6323 | 2025-06-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ecc9f088-cb75-3396-b3b5-24d041388173 | -11.952 | -58.7376 | 2025-06-20 06:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| d3fabb59-9ce4-32e6-a5e7-1fd080241a79 | -11.1465 | -46.6573 | 2025-06-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 364.7 |
| a7dde1e5-431e-3d9d-bb93-08bd48364b98 | -11.1468 | -46.6347 | 2025-06-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| eacc74b8-e07c-3804-b1d2-4398d49ec9ee | -11.1656 | -46.6548 | 2025-06-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 200.8 |
| f6399f30-8d6f-37bb-8c03-d629fb9c8c17 | -11.952 | -58.7376 | 2025-06-20 06:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2c9143e7-5e0e-3c6d-aade-bae7040c0b41 | -14.0404 | -53.3669 | 2025-06-20 06:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8b6f7406-599b-38a3-ad71-9805447a68b1 | -14.0404 | -53.3669 | 2025-06-20 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9b3fb7f4-fa40-3833-b7f7-cdc3449902c4 | -11.1274 | -46.6598 | 2025-06-20 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e2201d49-d67a-36d8-8960-3030405585a9 | -11.1656 | -46.6548 | 2025-06-20 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| e787aa9a-e812-332a-8a30-cbbb6802a446 | -11.127 | -46.6823 | 2025-06-20 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| e8377afa-3fd6-3eca-a325-c71fc7b77f5a | -11.1652 | -46.6773 | 2025-06-20 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 9e87bd74-f464-317e-9c02-0530b0d6a619 | -11.1465 | -46.6573 | 2025-06-20 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 289.3 |
| 639e8c30-e437-3442-8b2a-5001989a6ca6 | -11.1461 | -46.6798 | 2025-06-20 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 772f59af-162f-3694-9446-ea923089094c | -11.1652 | -46.6773 | 2025-06-20 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8671634c-96d5-3c14-9816-587b01578b91 | -11.1461 | -46.6798 | 2025-06-20 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 57d5b0bc-13c3-332a-851e-230d965364c4 | -11.127 | -46.6823 | 2025-06-20 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ce022ab5-c82e-36cc-b08a-a61f233ca94b | -11.1465 | -46.6573 | 2025-06-20 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| e0e47afc-0405-3a9c-9ce3-c6920c75728d | -14.0404 | -53.3669 | 2025-06-20 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| c8c5261d-0e0b-3169-8e82-9a6ca19b3a1a | -11.1656 | -46.6548 | 2025-06-20 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| e1b279df-9e9b-3192-8cf7-4d915d30d8ec | -14.0404 | -53.3669 | 2025-06-20 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 023eb0ce-19a7-3ea3-b2f6-b0bdc9ebec63 | -11.1274 | -46.6598 | 2025-06-20 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| c2e446c1-c176-3318-b31b-f0eacfde2559 | -11.1465 | -46.6573 | 2025-06-20 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 6d78c68d-40cf-336e-8bcb-097568eef9fa | -11.1652 | -46.6773 | 2025-06-20 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 066453a4-3b2a-39f6-b3b6-f9fdf72b963b | -11.1461 | -46.6798 | 2025-06-20 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 96c4d39a-aa10-31e3-9059-c5d6359ec0ab | -11.1656 | -46.6548 | 2025-06-20 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f984657e-f47b-37b1-833f-359844622997 | -11.127 | -46.6823 | 2025-06-20 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| f9602503-0641-3090-b003-19f891358c25 | -11.1465 | -46.6573 | 2025-06-20 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5a05732b-869f-3d02-b640-81290544f7a6 | -11.1461 | -46.6798 | 2025-06-20 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 26d69334-b0dc-301e-aa18-020d12f1bfbe | -11.1458 | -46.7023 | 2025-06-20 07:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| cf456dfe-774f-374f-b537-cef35b894e0e | -11.127 | -46.6823 | 2025-06-20 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| cd7d29fd-88a5-33fd-b613-573fa989905b | -11.1461 | -46.6798 | 2025-06-20 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 15270ddc-5918-3c56-97fd-f37342822eac | -11.1461 | -46.6798 | 2025-06-20 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 5e96151c-cf2e-3954-8b6d-37db2d8a3452 | -11.1458 | -46.7023 | 2025-06-20 07:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c90c7f6e-9667-3b5c-a5ed-d103b0f68f9f | -14.0404 | -53.3669 | 2025-06-20 08:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| b2fa64d2-009d-3ab5-af5a-26ab4c05bab0 | -11.1461 | -46.6798 | 2025-06-20 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| f667265b-be06-37ea-a564-a659d726445d | -11.1458 | -46.7023 | 2025-06-20 08:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| a61bb867-1988-3887-89aa-10a4e2d8f2d2 | -11.1458 | -46.7023 | 2025-06-20 08:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| db36460b-ae24-30be-bc57-9862d37ed632 | -11.1465 | -46.6573 | 2025-06-20 08:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 17b7a89b-b1bf-3ca6-b78f-a5924aad9d6e | -14.0404 | -53.3669 | 2025-06-20 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 4f533c75-fa03-3e77-81d1-efcafd38bd67 | -11.1461 | -46.6798 | 2025-06-20 08:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 321.9 |
| 79889dca-74ac-306e-964d-4f6737dbbac1 | -11.1656 | -46.6548 | 2025-06-20 08:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| d95e345d-690d-3237-94bf-3980ea574ea3 | -11.1652 | -46.6773 | 2025-06-20 08:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 7426a16d-b57f-3289-95c7-512b27c0ddfc | -14.0404 | -53.3669 | 2025-06-20 08:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 4dcde548-1c96-3841-8a01-d94e241cf0fd | -11.1461 | -46.6798 | 2025-06-20 08:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 7cdf1be4-cb22-35ab-a554-b17a0047308f | -11.1659 | -46.6323 | 2025-06-20 08:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 925807e4-aa76-3799-ac3b-e85008e540d8 | -11.1652 | -46.6773 | 2025-06-20 08:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 51b64544-5065-37ca-ad7f-d9d4996db290 | -11.1656 | -46.6548 | 2025-06-20 08:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c5a5192e-5ebc-3b21-9efd-180266ab221b | -11.1465 | -46.6573 | 2025-06-20 08:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8b8226f0-527e-36d0-b8a7-0b78b5473be7 | -11.1648 | -46.6998 | 2025-06-20 08:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a766a408-5cb0-35b5-8bf8-c5e890bce07d | -11.1652 | -46.6773 | 2025-06-20 08:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 318.4 |
| 20fff018-9231-3e86-8eec-68f012edf0d8 | -11.1656 | -46.6548 | 2025-06-20 08:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 76f658a3-d947-33d1-b7d7-b790a51f787f | -11.1461 | -46.6798 | 2025-06-20 08:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 81fb2249-0b37-360c-9975-86727e3f9e35 | -11.1465 | -46.6573 | 2025-06-20 08:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d5078973-5abf-33ec-a256-24f5990a7077 | -11.1458 | -46.7023 | 2025-06-20 08:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1473da87-2ead-367f-a09e-6832783b6203 | -11.1458 | -46.7023 | 2025-06-20 08:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 3d3e69d2-487b-3c6e-9918-d07d4c65da0d | -11.1465 | -46.6573 | 2025-06-20 08:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 89cd72a7-6077-3a04-80fa-598b68d82306 | -11.1652 | -46.6773 | 2025-06-20 08:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 723de021-dd6e-37f4-85ee-484470ac5893 | -11.1656 | -46.6548 | 2025-06-20 08:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a7207a97-c193-30e9-b252-b23a862483b6 | -11.1461 | -46.6798 | 2025-06-20 08:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 0ca5d960-c70b-31ed-b2dc-c9dd0e0104ae | -11.1656 | -46.6548 | 2025-06-20 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| a1909107-2dbc-3304-81e5-bf8494c8fbf0 | -11.1656 | -46.6548 | 2025-06-20 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 83b87bc9-059c-39c0-9f60-0bbe0cfb783f | -11.1465 | -46.6573 | 2025-06-20 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6404b77f-421f-347f-9b5e-34d72f635605 | -11.1656 | -46.6548 | 2025-06-20 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 256.1 |
| ab8a6aa6-4b9c-3512-86b2-dd1a7646dd7c | -11.1656 | -46.6548 | 2025-06-20 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 235.4 |
| b233a430-ae31-369e-a6bb-95d11fa1dbd8 | -10.5381 | -46.6445 | 2025-06-20 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f55dcac5-fc58-3af1-bbeb-3a83fd3508ed | -10.5378 | -46.6669 | 2025-06-20 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 4022da19-9a25-334d-9981-ad9834a7df0a | -11.1656 | -46.6548 | 2025-06-20 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 6cbbc7b7-2abf-3b8e-be79-6414b3c6393f | -11.5842 | -47.8723 | 2025-06-20 12:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8d0cdf4d-0e66-3dce-8bfe-e2d9c26987df | -10.5381 | -46.6445 | 2025-06-20 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 544e6ecd-4b9e-3f69-a9dd-546f89449a3f | -10.5241 | -47.5822 | 2025-06-20 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 39022711-9300-305f-b047-2f748363e292 | -11.1656 | -46.6548 | 2025-06-20 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| c710b276-6a0f-3916-b334-646fc5dc7201 | -11.6584 | -44.6207 | 2025-06-20 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 267.1 |
| b73dca14-afaf-33b2-9fba-c998bbfb0688 | -10.5241 | -47.5822 | 2025-06-20 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| da8058f7-7210-31ba-b0eb-2e92e25315fb | -11.6584 | -44.6207 | 2025-06-20 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 369.3 |
| 7bee839b-8e46-3063-b979-6ffdbf52cf40 | -8.5724 | -51.5552 | 2025-06-20 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b79057be-4805-35c3-93f1-eb4cfae95a5d | -11.658 | -44.644 | 2025-06-20 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 50053491-b529-3d40-9592-fc73b3082eac | -8.5911 | -51.5537 | 2025-06-20 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 30799e9f-8065-3c38-83f3-ce0769c04769 | -11.5842 | -47.8723 | 2025-06-20 12:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 6cb45ad7-035d-3b8e-b156-906506b1b4ef | -11.6584 | -44.6207 | 2025-06-20 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| d34c12a2-6d30-3396-a085-f56037f095be | -10.5241 | -47.5822 | 2025-06-20 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 7660de94-04c2-34b1-8647-44e660de788c | -14.0404 | -53.3669 | 2025-06-20 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7fad7b6e-286b-39d7-acef-e22ec614436c | -8.5911 | -51.5537 | 2025-06-20 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| f3e8fb2e-30d3-37eb-a018-04ade0d32bf5 | -4.8562 | -43.1907 | 2025-06-20 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9a9a2401-cfb8-322d-8090-769addb37148 | -11.5842 | -47.8723 | 2025-06-20 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 3c9b89e6-4d2f-3258-add2-33bbf51413c2 | -8.5724 | -51.5552 | 2025-06-20 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d977a64c-7337-3416-a374-accdbdfbb198 | -11.5842 | -47.8723 | 2025-06-20 12:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |


[Clique aqui para ver as próximas entradas](README32.md)
