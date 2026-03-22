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
| 2a360276-bd34-35e6-9d29-bdd33f02be5a | 0.9943 | -59.381 | 2026-03-22 01:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 111.9 |
| f8f66bea-e6e3-3d59-abed-c4f426e31740 | 2.6336 | -61.3017 | 2026-03-22 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7953f4bd-1c53-384f-bc77-c5a702f44537 | 2.6518 | -61.3015 | 2026-03-22 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 349.7 |
| 62e71e0f-e4a3-31fa-80c7-7ba77d1c6cff | 2.6519 | -61.2826 | 2026-03-22 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 396.2 |
| 51aff6da-8df1-31fd-a63e-bda502edf14a | 2.6336 | -61.2828 | 2026-03-22 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d0c54910-bb6a-37a4-881b-f630446d66a7 | 2.6518 | -61.3203 | 2026-03-22 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 3f1bffe7-6265-30fa-83f0-a190b3861ca6 | 0.9943 | -59.381 | 2026-03-22 01:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 5d2da313-4746-3b08-9bda-71eeb9c1b47e | 0.9761 | -59.3811 | 2026-03-22 01:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 82c1a9d3-99a5-3eb5-b402-fce0bfa5285e | 2.6336 | -61.2828 | 2026-03-22 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 9713394d-b475-3862-82ed-b86611d4fc40 | 0.9761 | -59.3811 | 2026-03-22 01:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 120.4 |
| cb1f8600-53e0-3a27-bc40-40b7cfcfc1dd | 2.6519 | -61.2826 | 2026-03-22 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 357.1 |
| 4de0754a-70c2-3ca2-aa47-4165df769b6f | 2.6518 | -61.3015 | 2026-03-22 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 323.3 |
| 95ee10eb-17e5-390b-87c6-8e88567a4e4b | 2.6336 | -61.3017 | 2026-03-22 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 83cb5899-6d3e-3670-810b-2a1dafa3c18e | 0.9943 | -59.381 | 2026-03-22 01:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 64c8ab0d-8b91-37d9-8106-8b65963964db | 2.6701 | -61.3012 | 2026-03-22 02:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0b23ff39-5390-3827-b207-df167a82c5dc | 2.6336 | -61.2828 | 2026-03-22 02:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 181.2 |
| d5ab0796-4f3d-3884-afee-2dc01d5ba423 | 2.6518 | -61.3015 | 2026-03-22 02:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 315.8 |
| 20099518-308b-3988-a109-171f2428127e | 0.9761 | -59.3811 | 2026-03-22 02:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 94.8 |
| a8455c21-2c55-333c-b52d-072ef81fa257 | 2.6519 | -61.2826 | 2026-03-22 02:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 384.8 |
| 8833c138-90eb-32a4-a902-f2d3ff59a85b | 2.6701 | -61.2823 | 2026-03-22 02:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| db82b693-c293-3ec7-8932-f44bcafd7b31 | 2.6336 | -61.3017 | 2026-03-22 02:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 80848926-27d0-3a81-a081-ab186ddb9b84 | 0.9943 | -59.381 | 2026-03-22 02:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c9a88da6-c558-3958-a55d-15402e414f7a | 2.6336 | -61.2828 | 2026-03-22 02:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 063b2da8-6ca8-30ee-913f-b7c4d6802574 | 0.9943 | -59.381 | 2026-03-22 02:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 9a2133d1-7fc5-3e7a-ae1d-2b47a680ab4c | 2.6336 | -61.3017 | 2026-03-22 02:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 89946fb2-16d1-308a-b786-421853870923 | 0.9761 | -59.3811 | 2026-03-22 02:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 2d55047b-eb9d-362f-8aba-b93d9f3c1ee3 | 2.6518 | -61.3015 | 2026-03-22 02:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 448.3 |
| 93eca399-5bc5-3c9c-8925-533f819533fc | 2.6519 | -61.2826 | 2026-03-22 02:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 483.1 |
| ad26184b-22a9-3ad0-8b37-33fff6fbecec | 2.6519 | -61.2637 | 2026-03-22 02:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| da38d647-8838-33fe-8b18-cdde36083ac9 | 2.6701 | -61.3012 | 2026-03-22 02:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 105.5 |
| cea9cd59-6917-3025-a3c9-cc09df72d6eb | 2.6701 | -61.2823 | 2026-03-22 02:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 36e20d2c-c055-368c-a864-b402159ab1de | 2.6336 | -61.2828 | 2026-03-22 02:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 3a3e5895-2b2c-3c47-8cdb-5dfe9ccece14 | 2.6336 | -61.3017 | 2026-03-22 02:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 65053650-c386-3d9d-8852-6a6a1cc295de | 0.9943 | -59.381 | 2026-03-22 02:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 02e46f1e-4d04-3f7a-9b56-36c32644a622 | 2.6519 | -61.2826 | 2026-03-22 02:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 471.6 |
| 705309af-077c-33d2-b6a8-46fd5d1a053e | 0.9761 | -59.3811 | 2026-03-22 02:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9b6be319-4378-31d8-874a-20b95e53119a | 2.6518 | -61.3015 | 2026-03-22 02:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 335.4 |
| 1aad6249-dbd4-3a67-b765-6950497df54a | 2.6701 | -61.2823 | 2026-03-22 03:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 3303d301-fc22-3855-b555-1d87f4d8e8ac | 0.9943 | -59.381 | 2026-03-22 03:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 94.8 |
| fd44b116-2546-325f-9617-b4b08653d80f | 2.6336 | -61.3017 | 2026-03-22 03:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 16de169d-c0ea-32f5-81a5-22f80e86e9cb | 2.6519 | -61.2826 | 2026-03-22 03:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 529.4 |
| 31b590b6-be81-3d46-a8dc-f63a5ced5446 | 2.6701 | -61.3012 | 2026-03-22 03:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 95150e6a-93c5-31f5-8618-6c71db7aec8e | 2.6336 | -61.2828 | 2026-03-22 03:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 3f689c0f-6260-3d4b-9be6-9551b31a0f15 | 0.9761 | -59.3811 | 2026-03-22 03:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| efe833a9-4879-3d58-9d59-ad558a110bfc | 2.6518 | -61.3015 | 2026-03-22 03:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 486.7 |
| 182c9e15-9ca9-31d6-a92f-06fd25e1a84c | 0.9761 | -59.3811 | 2026-03-22 03:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ab35ce74-f4b4-3057-9ee0-3f96522c67a8 | 2.6336 | -61.2828 | 2026-03-22 03:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 013dfc92-3792-3cd8-818e-7352405b1cf9 | 2.6701 | -61.3012 | 2026-03-22 03:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 80.6 |
| f42e9d3c-a8eb-339d-9156-8f4694470532 | 2.6519 | -61.2826 | 2026-03-22 03:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 399.2 |
| 7104d4a0-d164-34f1-ad38-6447fe82a5c2 | 0.9943 | -59.381 | 2026-03-22 03:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 99.8 |
| afd21967-4ec5-32f6-8e0d-142418748704 | 2.6518 | -61.3015 | 2026-03-22 03:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 411.1 |
| bc384b02-93df-3e88-b0c1-454afa8e0fa0 | 2.6701 | -61.2823 | 2026-03-22 03:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 053a0db1-77d0-394f-a80a-9b2da1ed3e78 | 2.6336 | -61.3017 | 2026-03-22 03:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| ec2102c3-27af-3cab-aff3-b50209e95839 | 2.6518 | -61.3015 | 2026-03-22 03:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 364.8 |
| 3ca3af6c-f84d-3f63-b0f4-9a560790eae0 | 0.9761 | -59.3811 | 2026-03-22 03:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 18c0cdd7-9935-38bb-a407-b9d13dc86fe7 | 2.6336 | -61.2828 | 2026-03-22 03:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2014a461-be32-3cd3-be4a-2843c7abafe6 | 2.6336 | -61.3017 | 2026-03-22 03:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a814a4a8-ccab-3229-b6fb-730c907f7787 | 0.9943 | -59.381 | 2026-03-22 03:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c9628c6c-b4bd-3ef9-942b-cd858e1ada1f | 2.6519 | -61.2826 | 2026-03-22 03:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 381.2 |
| cdddd52e-3ada-3ab1-b0c2-3e3df0aa15af | 2.6518 | -61.3015 | 2026-03-22 03:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 301.9 |
| 8b00995f-2a21-3bc8-a79e-003c9caeeb36 | 0.9761 | -59.3811 | 2026-03-22 03:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3bf6d127-971c-39fd-b4f9-205d5401755f | 0.9943 | -59.381 | 2026-03-22 03:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1b2c8aae-1e51-3395-8302-fb2e83ebf738 | 2.6336 | -61.2828 | 2026-03-22 03:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3ce2dd39-7e54-3aac-a81a-73dcf2b76bd7 | 2.6336 | -61.3017 | 2026-03-22 03:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 34dad357-68a8-35e0-b68c-56bab1f22608 | 2.6519 | -61.2826 | 2026-03-22 03:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 320.6 |
| 6dd2cf22-048b-35b7-9c03-1bbbe7839039 | 2.6336 | -61.3017 | 2026-03-22 03:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| a0f18106-b630-3391-aab7-cea589702b79 | 2.6518 | -61.3015 | 2026-03-22 03:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 252.1 |
| a933bf98-10c1-3037-937a-38f152cd2a98 | 0.9761 | -59.3811 | 2026-03-22 03:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| cb5d3325-7c51-392e-aced-d77567225baf | 0.9943 | -59.381 | 2026-03-22 03:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6a965a7c-0d8a-3797-bdd4-44cc497e30a3 | 2.6336 | -61.2828 | 2026-03-22 03:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 95fa55b8-3af7-35b9-954c-8d7566b48074 | 2.6519 | -61.2826 | 2026-03-22 03:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 234.3 |
| 167c7784-5c7f-3f91-a29e-4604be3b4213 | 0.9943 | -59.381 | 2026-03-22 03:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 553cc1d2-a073-3257-bb27-f88f2681b8f5 | 2.6336 | -61.2828 | 2026-03-22 03:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 06d49795-9d7b-3dad-8b0b-e4b480e1bfdf | 0.9761 | -59.3811 | 2026-03-22 03:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| afc70814-38d6-3586-812f-f2c134b0a27c | 2.6518 | -61.3015 | 2026-03-22 03:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 280.0 |
| 8688f26e-8c34-356d-9f88-45397d5e4240 | 2.6519 | -61.2826 | 2026-03-22 03:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 208.6 |
| cbb44242-29dc-307d-85cf-d9dfbd844e73 | 2.6336 | -61.3017 | 2026-03-22 03:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 20e0fd6d-7a01-3053-ae0b-157b044474b7 | -7.87402 | -39.92181 | 2026-03-22 03:55:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 533883c6-dec3-3546-9f76-662ba6248074 | -9.06096 | -36.57271 | 2026-03-22 03:55:00 | NOAA-21 | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 429425a2-3b20-3d6a-bc85-2de631fe7aeb | -9.77239 | -42.02174 | 2026-03-22 03:55:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 10e6b08c-b4dc-3c88-81a2-8be603488fa0 | -9.02751 | -36.93346 | 2026-03-22 03:55:00 | NOAA-21 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ae0c5f52-d42f-3228-9839-65bb835e3922 | -9.77273 | -42.02227 | 2026-03-22 03:55:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c8de0b38-d3e3-311a-8f0c-e1b60bb64af0 | -5.28437 | -35.56537 | 2026-03-22 03:55:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 062781df-dd26-350e-ac3f-2f28dfc56e87 | -10.73687 | -36.98484 | 2026-03-22 03:55:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7f860028-9deb-34d6-999a-aaa8aa582949 | -9.7717 | -42.02581 | 2026-03-22 03:55:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c07263fe-41a4-3c97-9fed-c0c193b8c08e | -10.33262 | -37.55137 | 2026-03-22 03:55:00 | NOAA-21 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33fb2891-2636-35b8-88b4-f80cedec6ba4 | -11.05069 | -38.78492 | 2026-03-22 03:55:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fcc8f018-febc-32b3-a7ad-89a1653838ab | -11.78393 | -41.19365 | 2026-03-22 03:57:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5524948a-5071-3a57-be10-bcaf05a8e82f | -11.84152 | -37.93905 | 2026-03-22 03:57:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d64790ee-974e-3088-9eb6-b2a6f6bd4a44 | -12.49954 | -43.64434 | 2026-03-22 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ff5a24d-b98b-39e5-a974-db764c184b59 | -12.50447 | -43.68295 | 2026-03-22 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f7465d5-4806-3ccf-bef0-a4bb19a1fb71 | -12.50821 | -43.68361 | 2026-03-22 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8978e539-6c31-3c4a-adfd-9eb2f7d9db85 | -12.49503 | -43.64824 | 2026-03-22 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6e227d2-71ca-35b6-be04-7b7def1a6b30 | -13.15664 | -53.25748 | 2026-03-22 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14ea69b1-eeaf-3c60-b673-46a10b35311a | -12.50249 | -43.64958 | 2026-03-22 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff5abe73-09ac-3eb1-b2ca-6fc6b4420bad | -12.50526 | -43.67836 | 2026-03-22 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49d40173-734a-3689-81a3-74695b0680fb | -13.68083 | -42.67527 | 2026-03-22 03:57:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d39e893e-59e3-3549-ba09-f069e7375478 | -16.92648 | -43.60129 | 2026-03-22 03:57:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f51599b-2ba9-3d87-ab37-18ce7376cba3 | -13.14994 | -53.25594 | 2026-03-22 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdee1b5f-2fed-3202-a6c6-d8634761ef53 | -12.50622 | -43.65024 | 2026-03-22 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
