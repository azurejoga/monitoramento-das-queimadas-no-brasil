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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 025a6ce6-502b-3a86-9dc2-1ce57f6651d2 | -13.8867 | -54.6312 | 2025-06-12 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 0ccb9a28-ee6f-3d89-8cf6-2803052390e4 | -13.9059 | -54.6291 | 2025-06-12 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8a127fd9-6116-35c2-ba2e-8019381d01ee | -12.5236 | -58.3576 | 2025-06-12 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 84fe6ace-4516-3920-87ac-bdf3939e77da | -12.5238 | -58.3378 | 2025-06-12 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 306.4 |
| e3f78d29-69c7-3787-a878-e1b764b59037 | -8.7996 | -45.0815 | 2025-06-12 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 4bb1d7e8-389e-39c7-8732-470a7f71c2b1 | -11.1382 | -53.9223 | 2025-06-12 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 3e75a86f-139b-3712-bd81-dff4a45aebe0 | -10.8694 | -54.3151 | 2025-06-12 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 14d93674-4f14-3da6-ad28-a829a7d9c7e3 | -12.5175 | -57.2231 | 2025-06-12 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 5770056c-efd0-3fb5-a9f5-ab0c6c1e30a0 | -13.9059 | -54.6291 | 2025-06-12 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| b0dced9e-a2fd-3eeb-8c07-24392dbb22a7 | -12.5175 | -57.2231 | 2025-06-12 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8bcb08af-6bbf-38f5-ba7d-df0b133a16a4 | -13.726 | -45.2421 | 2025-06-12 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e485ee20-2a1d-370a-8462-0ddd5a8d6759 | -8.7996 | -45.0815 | 2025-06-12 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 0e4689ea-a509-3866-a204-5e43026a5c9f | -12.5236 | -58.3576 | 2025-06-12 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| fdef4310-24c3-3d89-80bf-54e0f6284a99 | -13.8867 | -54.6312 | 2025-06-12 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 969c895f-443a-3b79-9e57-6e35a2f5c011 | -11.1382 | -53.9223 | 2025-06-12 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a2396abf-9ace-3070-b74b-7987391308b7 | -10.8694 | -54.3151 | 2025-06-12 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 0e965d55-66bf-3cda-8246-2d4bb9573ce2 | -14.0328 | -55.13 | 2025-06-12 14:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b664bc6c-cb27-3d33-8978-3b3f1bf9d092 | -12.5238 | -58.3378 | 2025-06-12 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 312.4 |
| 85f1414a-2444-37d6-b2c4-a40c5a7d6b48 | -12.5238 | -58.3378 | 2025-06-12 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 291.2 |
| 141a0d7b-9295-3cf5-82f9-8472be53bc4b | -10.3272 | -44.3204 | 2025-06-12 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4f47fb05-0854-385d-bb95-5cc6426ac636 | -10.8694 | -54.3151 | 2025-06-12 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 75e85607-2df6-3fb6-8db7-6ba31cefd895 | -12.5236 | -58.3576 | 2025-06-12 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 958e9529-48b1-3759-a3fb-1455c294ac58 | -11.9278 | -57.4717 | 2025-06-12 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 5b8ff548-abc1-3b60-8b4d-f13134927872 | -13.8867 | -54.6312 | 2025-06-12 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1b229b13-dca3-379c-9693-373b03825396 | -8.7996 | -45.0815 | 2025-06-12 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 2460f6fa-2acd-3a55-9a92-3b5a473447ee | -13.9059 | -54.6291 | 2025-06-12 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 85df35e6-c2ea-34e6-a73a-7eb57cc76e74 | -13.726 | -45.2421 | 2025-06-12 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| eaa86db6-4086-350e-9e58-74627af910a2 | -11.2112 | -48.601 | 2025-06-12 14:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a7644036-f085-3fc6-a46c-e2b6b5cd5e4a | -10.8694 | -54.3151 | 2025-06-12 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 4186581b-570f-3af4-98b2-bfebae02f0a0 | -14.0328 | -55.13 | 2025-06-12 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b28cba6e-7c0f-3890-8777-38b2cd6ed05b | -11.9088 | -57.4732 | 2025-06-12 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 230b2fbb-10eb-3c67-9bcd-5af84bd57a75 | -12.5238 | -58.3378 | 2025-06-12 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 283.0 |
| 5a812526-0c6f-3b5f-9827-bc6acf8a28ac | -12.5175 | -57.2231 | 2025-06-12 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 01d82b92-6ede-3da1-a870-cc9c9f3f9f95 | -13.8867 | -54.6312 | 2025-06-12 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| b9040043-58cb-3f2a-aa60-10dcaa65c248 | -11.1382 | -53.9223 | 2025-06-12 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 47689d54-1c10-363e-a511-f1ac81d41ad4 | -12.5236 | -58.3576 | 2025-06-12 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 789d3a61-51d1-3507-9617-a711aba9ac90 | -7.8626 | -47.898 | 2025-06-12 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 2bf36409-bc5d-3b7a-b485-e09760302e25 | -8.7996 | -45.0815 | 2025-06-12 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| d46fe797-8d18-34a3-82f6-dece1bb98135 | -7.8629 | -47.8761 | 2025-06-12 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 872b6210-3baf-307c-ba75-bb105b25c66c | -11.9278 | -57.4717 | 2025-06-12 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 155.8 |
| df0c6bd5-61b1-3488-b607-de49231b27aa | -13.9059 | -54.6291 | 2025-06-12 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| ff9ef74a-6c4a-3ea2-afe6-65a921c8850f | -7.8626 | -47.898 | 2025-06-12 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| bc32ad23-bd31-3f1f-a236-a1ec34975dfd | -11.1382 | -53.9223 | 2025-06-12 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ba67363c-9bd6-38e8-b6dc-6e6876e020e3 | -14.0328 | -55.13 | 2025-06-12 14:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 3e6cbcc8-1d0f-3620-94ca-5a38bb417231 | -8.7996 | -45.0815 | 2025-06-12 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| b38bc89d-97ff-3512-9fe6-ebe326ecaa71 | -13.8867 | -54.6312 | 2025-06-12 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.6 |
| ac701498-fe9a-3f6d-81db-7fd06fb27374 | -11.9088 | -57.4732 | 2025-06-12 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e12da6d0-3fdf-3f22-bec6-85436b1898e3 | -11.2112 | -48.601 | 2025-06-12 14:40:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2d3159ef-3dd8-3244-a252-8c372cf1d7ce | -11.9278 | -57.4717 | 2025-06-12 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 202.4 |
| 66537e5c-2fe3-37c0-bc6f-5d3440d7e586 | -12.5175 | -57.2231 | 2025-06-12 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f37631e6-85c8-3492-a62b-83eca61ea206 | -10.8694 | -54.3151 | 2025-06-12 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 78ecdffa-11b7-3bb6-a305-09ce5d14ca0a | -12.5238 | -58.3378 | 2025-06-12 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 264.1 |
| 9d5595fe-4d18-3d21-b818-968fd915ea62 | -13.9059 | -54.6291 | 2025-06-12 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 3c85cbd0-7b39-3c40-8923-8c83236757d2 | -12.5236 | -58.3576 | 2025-06-12 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 0f9f5041-e2e4-382c-9406-50cf96a9985c | -7.8629 | -47.8761 | 2025-06-12 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |


