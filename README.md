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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e498873-5689-3469-b1ea-2045f1b641f1 | 1.2856 | -60.0656 | 2025-03-04 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 332d5022-b5ca-3b15-ac00-3392fdf19551 | 1.9955 | -61.1394 | 2025-03-04 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 2f41a2a2-c0c3-3185-874b-14f96fd33381 | 2.3421 | -61.06 | 2025-03-04 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 201.3 |
| 0fd000b3-180d-3154-925d-2c5bf8842348 | 2.3604 | -61.0597 | 2025-03-04 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 160.1 |
| d26affc3-a4d1-3b02-9046-a0a974be928d | 1.2856 | -60.0846 | 2025-03-04 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5368bd29-51bc-3b06-88b4-93c1adaf06a9 | 2.3422 | -61.0411 | 2025-03-04 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 122.8 |
| d7aa5555-d1e2-3053-8387-cd602c056cb5 | 2.3604 | -61.0408 | 2025-03-04 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 121.3 |
| b3e0eeba-2f60-3d99-b49e-6b11cbc789f3 | 1.9955 | -61.1394 | 2025-03-04 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 10250920-5aab-3d68-ae8f-51016c5b285a | 2.3422 | -61.0411 | 2025-03-04 00:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 51e16f94-2825-35eb-98bd-0d0027bd7974 | 1.632 | -60.2338 | 2025-03-04 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2ce22ebf-5729-3a9d-bda8-02a211edcc2d | 2.3604 | -61.0408 | 2025-03-04 00:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 0e89d0e4-84c9-3a26-a611-1571bd4d8df5 | 2.3421 | -61.06 | 2025-03-04 00:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 79fbe732-e1bf-31d4-a15e-d1af88234410 | 2.3604 | -61.0597 | 2025-03-04 00:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 188.7 |
| 30e63284-a81d-3da1-9116-84e51cf386e2 | 2.3604 | -61.0408 | 2025-03-04 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 08436310-18cd-37df-bc4d-cf3c6d77ed79 | 2.3421 | -61.06 | 2025-03-04 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 232.2 |
| 8654434d-88dc-30aa-a32e-5d6a9ab6fe06 | -13.99 | -45.5907 | 2025-03-04 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9d5bf150-c776-3863-b29b-f97da3b3a534 | -14.0085 | -45.6338 | 2025-03-04 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| c77f5e6f-65fd-357a-bd0e-8d38a67bb0f7 | -14.028 | -45.6304 | 2025-03-04 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 0ca9adf9-d32c-32f2-bba0-69a3535ca27c | -14.009 | -45.6106 | 2025-03-04 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| fce5f7eb-cf19-38bc-a607-891b3309355c | -14.0095 | -45.5874 | 2025-03-04 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 4b84e60a-0096-3ded-832f-39519f025b7b | -14.0285 | -45.6072 | 2025-03-04 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| c9969c16-db1c-382c-ac01-7ec482c31c1c | 2.3422 | -61.0411 | 2025-03-04 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 105.7 |
| a77c32af-241f-305b-957b-e2deac77fa99 | 2.3421 | -61.0788 | 2025-03-04 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 69242520-2d1b-3a7d-8092-af513cd98617 | 2.3604 | -61.0597 | 2025-03-04 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 61c8f9a6-e88f-3871-b089-edc2f2ea1f98 | 1.9955 | -61.1394 | 2025-03-04 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 97774e25-4885-32a8-bcac-455cd66d8fca | 1.632 | -60.2148 | 2025-03-04 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4676bc62-3f8d-365d-a8e4-d01ec20caa87 | 2.3604 | -61.0408 | 2025-03-04 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 106.7 |
| a5a14ab1-592a-3e05-b769-2f252779b7d7 | -14.0085 | -45.6338 | 2025-03-04 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 89113728-aced-3f0f-a579-3ddcad1e9067 | 1.9955 | -61.1394 | 2025-03-04 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 25746cda-01dd-3dd6-a13e-d88f997ad522 | -14.0095 | -45.5874 | 2025-03-04 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 65e8edc9-8782-34c5-b285-3273cbf419fd | -14.009 | -45.6106 | 2025-03-04 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ae6656ee-c223-3615-9aa9-5bcac4ffe959 | 2.3421 | -61.06 | 2025-03-04 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 183.7 |
| bd370de7-f64c-32d9-ab94-9196b9214d39 | 2.3604 | -61.0597 | 2025-03-04 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 075f1452-a4c9-3f88-a725-eacf664eaf4f | -14.0285 | -45.6072 | 2025-03-04 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 18e37867-5339-3887-9a6e-b0427e28b657 | -13.99 | -45.5907 | 2025-03-04 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| cc40c18a-7626-328f-b75c-6ccdc1a61455 | -14.028 | -45.6304 | 2025-03-04 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 9316eeb8-2e88-3679-bc80-1e76c3c504a1 | 1.632 | -60.2338 | 2025-03-04 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 0f5f8633-9ce9-3a36-8c01-804337eb405a | 2.3422 | -61.0411 | 2025-03-04 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 770628b2-3cbb-3385-98ed-5867c15c416c | -14.028 | -45.6304 | 2025-03-04 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 20921c39-b90f-3148-ac03-ad299a88057d | 1.1393 | -60.5222 | 2025-03-04 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5a6b88de-fcc5-3fc6-8be1-70ca332e578c | 2.3422 | -61.0411 | 2025-03-04 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 605243b7-3496-33ca-ba7f-736c10e7328a | 1.1393 | -60.5033 | 2025-03-04 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a81e9508-e7ef-3b4e-8905-8172e4ff73b1 | 2.3604 | -61.0408 | 2025-03-04 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 8083c837-49bb-39c1-b060-a48d5ec1dee9 | -14.009 | -45.6106 | 2025-03-04 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 30d557cc-fd8b-3c7a-ba37-04767169492c | -14.0285 | -45.6072 | 2025-03-04 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 457c1521-662d-30cf-af99-1e256f97ad5c | -14.0095 | -45.5874 | 2025-03-04 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c9cff365-aac1-3cf3-a8b3-18de08e2c77d | 1.121 | -60.5224 | 2025-03-04 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b121ba17-6b0a-3688-b1e7-66557c04b223 | 1.632 | -60.2148 | 2025-03-04 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| eff46321-705c-3ad3-88f1-1bd62130f741 | 1.632 | -60.2338 | 2025-03-04 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6ebc36be-cbec-3fb2-97f3-e1ef93247bff | -14.0085 | -45.6338 | 2025-03-04 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ea42759f-00f1-38eb-96ce-a5300c4508fe | 2.3421 | -61.06 | 2025-03-04 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 22542c2c-e67c-3457-b9d8-c26358eb3b9f | 2.3604 | -61.0597 | 2025-03-04 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 141.0 |
| ef2fbc0c-7ecb-3a1c-a698-fe302a0096db | 1.121 | -60.5034 | 2025-03-04 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a62f91f8-0982-35ad-8c88-aab22264d5a1 | -14.0285 | -45.6072 | 2025-03-04 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5688ee03-2ddb-3876-93b5-4a677d96d469 | 2.3604 | -61.0408 | 2025-03-04 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 325bebd0-d1d5-3fa7-b70c-5579e9bb8692 | 2.3422 | -61.0411 | 2025-03-04 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 442a6f08-345b-33cc-804a-d0c01eebe7bc | 1.1393 | -60.5222 | 2025-03-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c63b7854-ed1b-308d-8b8f-62a04e84c644 | 1.121 | -60.5224 | 2025-03-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a65bfedc-bab4-3acd-aa6d-898ddbf9678b | 2.3421 | -61.06 | 2025-03-04 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 189.7 |
| a7608d96-60ea-35bc-a351-5632a52dbd00 | -14.0095 | -45.5874 | 2025-03-04 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ae30fae4-dde7-37a0-9ee4-368227ddeba9 | 1.121 | -60.5034 | 2025-03-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d9782a14-c188-3c8d-9345-80f57c8c03d3 | 1.7597 | -60.2326 | 2025-03-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8c2a4d03-a242-35d6-8eb2-3af6637ddd48 | 2.3604 | -61.0597 | 2025-03-04 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 6829b48b-d46b-3b96-8185-0fcd0e33f2b1 | -14.028 | -45.6304 | 2025-03-04 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| b60fedde-cd47-350b-ab17-fcb628f1f52f | 1.1393 | -60.5033 | 2025-03-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1d29810d-257a-329e-8645-3250f8d9be55 | -14.0085 | -45.6338 | 2025-03-04 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 164f55f7-13fd-3eb4-a772-72723298286d | 1.632 | -60.2338 | 2025-03-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| cdf911af-dfa3-3376-8bc3-58ace3f9c4c1 | 2.3604 | -61.0408 | 2025-03-04 01:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 8198c565-56b4-38b0-b050-b19b0d5e0db4 | -14.028 | -45.6304 | 2025-03-04 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 29840503-6907-39e2-b529-7e23885c4cd9 | -14.0095 | -45.5874 | 2025-03-04 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| afe410e2-4e63-3a77-8d28-bf4229ee8a2c | 2.3604 | -61.0597 | 2025-03-04 01:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 6f65e412-a22b-33e5-84ce-b564dbfef2b6 | 1.121 | -60.5224 | 2025-03-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 8ce3c9c2-c3aa-324a-bbaf-b0c0549b0d8f | 2.3421 | -61.06 | 2025-03-04 01:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 21fa81d3-1624-309f-9028-98fb5caea0f2 | 1.121 | -60.5034 | 2025-03-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 57d53cd4-1b7e-35ab-ad9a-5f397ae91563 | 2.3422 | -61.0411 | 2025-03-04 01:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a6b5c78f-e496-3b55-b27e-7af86fee2c7e | 1.1393 | -60.5033 | 2025-03-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c8bafce7-9acc-3b4f-bee7-7d3164d8e187 | -14.0285 | -45.6072 | 2025-03-04 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 805133b1-dfb3-3400-9bbe-8a897fe578d7 | 1.1393 | -60.5222 | 2025-03-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7c491e88-0f8f-32db-9665-1e08b5f3ed16 | 2.3422 | -61.0411 | 2025-03-04 01:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 7e45d9b3-a40e-322d-a03d-ce5943fd2e97 | 2.3604 | -61.0597 | 2025-03-04 01:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 137.6 |
| f1d94142-4866-3875-84cd-dddc0a3f5356 | 2.2706 | -60.2459 | 2025-03-04 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2e54db98-f443-333e-878c-011aa7c87e52 | 1.121 | -60.5034 | 2025-03-04 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| ef40aae0-5dde-3e11-ae96-0e5b2f10c2de | 1.7597 | -60.2326 | 2025-03-04 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| f11fabf1-82ad-324c-bfbe-6f0515a08328 | 2.3421 | -61.06 | 2025-03-04 01:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 12fb06b6-7779-3639-a4ed-20e1873ade4a | -14.028 | -45.6304 | 2025-03-04 01:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 1ff199b1-a89a-3313-81a1-a842b4e0e52c | 2.3604 | -61.0408 | 2025-03-04 01:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 890cf6ef-562d-3706-9224-3093cebbab21 | -13.99 | -45.5907 | 2025-03-04 01:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2778f50f-5699-3c15-a6a9-86b138ddec5e | 1.632 | -60.2338 | 2025-03-04 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 83217b84-de38-365d-add5-f6857e43ea0f | 1.121 | -60.5224 | 2025-03-04 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6469974e-1578-3926-9a1d-356cd2897bef | 1.1393 | -60.5033 | 2025-03-04 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 45761184-9ef9-3988-97df-5877450726fe | 2.2705 | -60.2649 | 2025-03-04 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 2439de67-ad19-3e2a-b2d0-ddd32dff2fbc | -9.80918 | -38.10238 | 2025-03-04 03:36:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1a7c5462-109e-3070-9c71-3f8608d7ce8f | -8.43648 | -36.34565 | 2025-03-04 03:36:00 | NOAA-21 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e466fe03-4897-3efc-b218-6a51392e2e4a | -8.10451 | -43.14788 | 2025-03-04 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 733a7f81-321f-3afc-8332-60717abecd13 | -9.80995 | -38.09785 | 2025-03-04 03:36:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 978023c1-b894-3685-b2d7-0d00fe7e2666 | -8.1057 | -43.14127 | 2025-03-04 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1ae6b19a-26bf-3b1d-a2cd-8b18458264b6 | -8.1051 | -43.14457 | 2025-03-04 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 749eda2a-63af-3780-a4bc-38059d5642d5 | -7.83442 | -36.85962 | 2025-03-04 03:36:00 | NOAA-21 | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0017ba1d-4397-3dc2-bcab-9a8cb466882a | -8.10629 | -43.13797 | 2025-03-04 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 822e9789-717a-3535-950d-e22932fc0143 | -8.43587 | -36.34946 | 2025-03-04 03:36:00 | NOAA-21 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
