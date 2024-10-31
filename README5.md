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
| 6dfea83a-1f28-3289-ae6a-10d82c718161 | -2.1954 | -47.9408 | 2024-10-31 00:31:36 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7303a2e4-b3b1-3335-8e0b-009c0780a4a0 | -2.197 | -47.947601 | 2024-10-31 00:31:36 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39bc7645-34c8-38bd-b624-734cfea73149 | -2.906 | -51.287998 | 2024-10-31 00:31:37 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0902eef9-1671-3fc8-acbd-0f11946240cb | -2.9078 | -51.296101 | 2024-10-31 00:31:37 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a64b4e11-0048-3384-b7be-032148cd132a | -1.8145 | -46.8951 | 2024-10-31 00:31:38 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c09292f-bbcb-3e80-965a-e0e8fffb9f65 | -1.8161 | -46.902302 | 2024-10-31 00:31:38 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81aeb2f4-3374-341d-bf8d-845a61e684b1 | -1.7603 | -46.701698 | 2024-10-31 00:31:38 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37bd269e-e636-3092-8ca9-c2c2ccbb8158 | -1.762 | -46.709 | 2024-10-31 00:31:38 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a737a43-77e3-3968-8316-f29c6c9c56fe | -1.9898 | -47.943298 | 2024-10-31 00:31:39 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae044f70-cc2c-3751-b274-3b6cb033d85d | -1.9914 | -47.9501 | 2024-10-31 00:31:39 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0329e4e0-84b9-31d0-8bee-7914822a1286 | -2.5958 | -50.636501 | 2024-10-31 00:31:39 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c13bd9ea-5be2-3338-8edc-4b1653a93dce | -2.9672 | -52.532799 | 2024-10-31 00:31:40 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5f053da-0feb-3928-b0b2-b86ace557f48 | -2.9693 | -52.542198 | 2024-10-31 00:31:40 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec662479-0c5a-3708-9408-d0ab22fa1be8 | -1.9815 | -48.682301 | 2024-10-31 00:31:42 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a60664-cbb9-3f2b-b439-7f866e11796c | -1.9717 | -48.684502 | 2024-10-31 00:31:42 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a13db35e-b83c-34bc-aa06-a352a07aa5d5 | -1.6902 | -47.757198 | 2024-10-31 00:31:43 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c96d373-750a-3094-b07f-215bb7dbbfc3 | -1.6917 | -47.764099 | 2024-10-31 00:31:43 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a33ef3b-d0e5-39bd-b51c-baf0191a288b | -1.3524 | -46.584 | 2024-10-31 00:31:45 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 353c5eed-0cdb-3f60-a5ac-45e0863b5a16 | -1.354 | -46.5914 | 2024-10-31 00:31:45 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4d6634-2e87-3577-aa05-1807d087b387 | -1.2722 | -46.594002 | 2024-10-31 00:31:46 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb413105-1495-3726-8834-6a709d437c93 | -1.2739 | -46.601501 | 2024-10-31 00:31:46 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b3791f2-78dd-3b1a-99f4-f2190f4e5c53 | -1.2755 | -46.608898 | 2024-10-31 00:31:46 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e911a08-36e1-3cae-9c1d-d9b4ba3b8298 | -2.0435 | -50.239399 | 2024-10-31 00:31:47 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a82aae5-54bb-3cb6-ae8f-210b7fab361d | -1.377 | -47.7397 | 2024-10-31 00:31:48 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca28dee-3f9e-33df-ac04-7f57b9ac5264 | -1.1647 | -47.3022 | 2024-10-31 00:31:50 | METOP-B | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4caa322d-1659-38c1-a7c1-8127c6877288 | -1.1663 | -47.309299 | 2024-10-31 00:31:50 | METOP-B | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d8a5ad-35ec-3632-9ca9-2889dd2420c4 | -1.0811 | -47.615799 | 2024-10-31 00:31:53 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf68bfe-d2ac-3fcb-b527-39a142bf9db6 | -1.0826 | -47.622799 | 2024-10-31 00:31:53 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 773d21e3-1e5a-3838-af58-92184d5b0dc2 | -1.0842 | -47.6297 | 2024-10-31 00:31:53 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1d43b2-2349-31d0-8e49-cc12930274e0 | -1.9116 | -52.0383 | 2024-10-31 00:31:55 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c165f92-7ec2-3f93-9d09-cf6946e0cce8 | -1.9136 | -52.046902 | 2024-10-31 00:31:55 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d5f4ce5-11b7-3f8a-8efe-4366b2ba414f | -1.8863 | -52.016899 | 2024-10-31 00:31:56 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a092d207-8eb0-374f-b5a0-03da94803b2b | -2.2217 | -53.564999 | 2024-10-31 00:31:56 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf2e1250-16b5-35a3-898f-d46bfe989d9f | -1.8723 | -52.091999 | 2024-10-31 00:31:56 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ad00d4-c5cc-3254-bb50-ff9b8a2b68ee | -1.8742 | -52.1007 | 2024-10-31 00:31:56 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abb7d157-fd00-3b9d-a7c4-12ed46e1a13a | -2.2309 | -53.698002 | 2024-10-31 00:31:56 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e20b1bdb-de64-3621-ba9d-3bf93b993a59 | -1.8625 | -52.0942 | 2024-10-31 00:31:56 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b5d8ad-3b86-3799-a83f-63d6f60d26f3 | -1.8644 | -52.102798 | 2024-10-31 00:31:56 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 082cab97-a7b3-3629-9093-900e49a9d46a | -2.2211 | -53.700199 | 2024-10-31 00:31:56 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 975f5f48-bfc3-303d-a277-c38693f85356 | -2.1871 | -53.639702 | 2024-10-31 00:31:57 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba62efa8-24d0-3128-b0cd-0472474a188e | -1.5511 | -52.081501 | 2024-10-31 00:32:01 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 343496ea-aff2-3aee-89d8-6457b7db0b17 | -1.553 | -52.09 | 2024-10-31 00:32:01 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 611191dd-ad3d-350d-a5c2-1439f24d7468 | -1.5628 | -52.087799 | 2024-10-31 00:32:01 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a809479-253d-3d3b-a32d-0ea382c36d1c | -1.5647 | -52.096401 | 2024-10-31 00:32:01 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caaa7d6f-a1e4-352e-b824-1546e9d923ea | -1.5667 | -52.105 | 2024-10-31 00:32:01 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35ea7d9d-d82e-359e-8022-498d3edbec3d | -1.6675 | -52.554798 | 2024-10-31 00:32:01 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5617f7e3-d7ef-3747-81f8-b22892011a02 | -1.6695 | -52.5639 | 2024-10-31 00:32:01 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0331b81-c543-30f5-8857-296fcedfedcb | -1.4508 | -52.184502 | 2024-10-31 00:32:03 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dfb29f5-9de1-3868-9e21-e868dc4e9309 | -1.4528 | -52.1931 | 2024-10-31 00:32:03 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e63b23ef-6a9c-3905-b3af-8e7451d59315 | -1.4547 | -52.201698 | 2024-10-31 00:32:03 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa50edaa-b92a-3b41-b4eb-a92c62be61b1 | -1.4644 | -52.245098 | 2024-10-31 00:32:03 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcce89f6-c518-3bb1-80f8-e7e4896bbed0 | -1.4664 | -52.253799 | 2024-10-31 00:32:03 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77dccbcb-fd2a-3d8c-8d39-9e35d491fc30 | -1.4683 | -52.262501 | 2024-10-31 00:32:03 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47c98001-ef97-350d-813e-80a66a1c26fd | -1.4136 | -53.576302 | 2024-10-31 00:32:09 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0c11e0-8f2c-3d61-acc3-da48bcddd2d5 | -1.1177 | -53.630402 | 2024-10-31 00:32:14 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1318fdf-baa9-303d-8360-91bf5bf20771 | -0.9099 | -53.665199 | 2024-10-31 00:32:18 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dcefdf9-853f-3daa-8553-91c4ca6be414 | 0.4237 | -50.261799 | 2024-10-31 00:32:27 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1109317-3395-30e0-a436-4c552cf34b92 | 1.0734 | -50.943298 | 2024-10-31 00:32:40 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 31d23e1f-2d0a-37f3-9758-1a8e22f3cddb | 1.0717 | -50.9505 | 2024-10-31 00:32:40 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 066129a2-5103-3d9b-b6cb-06397a89c478 | 1.0701 | -50.957802 | 2024-10-31 00:32:40 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| da5bf7bf-26fd-3e5f-a0e0-d71a9217bab1 | 1.0881 | -50.923801 | 2024-10-31 00:32:40 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e7d74aac-6475-3f0b-9e6e-3e13b0f5a0b5 | 1.0865 | -50.931099 | 2024-10-31 00:32:40 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4752bbc2-d487-3bfe-abac-ea37efcc6fd2 | 3.4102 | -51.229801 | 2024-10-31 00:33:19 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0211e1ba-24ee-3e60-b346-6281260f64c1 | 3.5067 | -51.258801 | 2024-10-31 00:33:20 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1321debf-b34e-323d-b4f3-c850517dded5 | 3.505 | -51.265999 | 2024-10-31 00:33:20 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e50ef83f-181d-37f2-a479-eba98edb51f3 | -0.7552 | -62.8933 | 2024-10-31 00:35:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| ed0779f4-78d2-3e71-866e-03a8b8db86fe | -0.7734 | -62.8932 | 2024-10-31 00:35:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| f89535a9-ac3c-3230-a929-f4bf26d4af15 | -1.2497 | -46.6147 | 2024-10-31 00:35:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| d7131fcc-4286-3f7c-a653-adbcc495a77b | -2.1718 | -47.9506 | 2024-10-31 00:35:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| afe4b936-09a6-3f9f-9671-41e82269c2f5 | -2.5031 | -48.4596 | 2024-10-31 00:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8b5dc7b3-8a58-3269-a159-6613ddbfe913 | -2.5215 | -48.4806 | 2024-10-31 00:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 7239cdc6-310f-3fcc-881d-900f4079b11b | -2.5216 | -48.4591 | 2024-10-31 00:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| cb965a9b-d4b7-3452-b028-87d3a224fd01 | -2.8109 | -45.4875 | 2024-10-31 00:35:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 09c2f783-1ec4-3c57-8007-6cae32050379 | -2.811 | -45.465 | 2024-10-31 00:35:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a1dc52da-2f7b-30e4-a0fb-26f6a32f7ce5 | -2.8838 | -45.8207 | 2024-10-31 00:35:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 87f7ea50-936a-3302-9a8c-0260dab8f749 | -3.2945 | -45.402 | 2024-10-31 00:35:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6e1c95b4-7ad3-3e89-8afb-834b750244e0 | -3.2366 | -45.83 | 2024-10-31 00:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 78ddc230-4137-3a32-a013-f2b0c8008f47 | -4.2563 | -43.4368 | 2024-10-31 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 8f648b1c-75e6-3807-8a3d-b7dc622ac6ac | -4.2749 | -43.4357 | 2024-10-31 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| a478da4f-4265-3c27-8942-baf36630454f | -4.2751 | -43.4125 | 2024-10-31 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| bdbe318d-e27c-3009-9fed-d3e93f19f4d6 | -4.3353 | -48.5862 | 2024-10-31 00:35:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9fd4a7c7-e25a-3d5b-9231-f57a9e2b0cf1 | -4.6511 | -43.1104 | 2024-10-31 00:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 7a7880ee-6815-3ad5-a517-5bc0b0ad0b33 | -5.0464 | -45.1768 | 2024-10-31 00:35:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 1c59e339-9f6f-327e-ac36-f14972649866 | -5.0466 | -45.1542 | 2024-10-31 00:35:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d42c8024-83c7-3c5d-899a-a79133af9858 | -6.1229 | -43.9578 | 2024-10-31 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e13aa4d5-1da9-3a81-92d1-b151e2d91eb5 | -6.1416 | -43.9563 | 2024-10-31 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 26683b1a-9825-337c-88ba-086c24cd5bdb | -12.424 | -43.7274 | 2024-10-31 00:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| ae5eb62e-e91f-369c-83a6-b249822790eb | -12.4433 | -43.7242 | 2024-10-31 00:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 212.7 |
| b38008d4-343d-3296-b25a-f014507bca00 | -12.4438 | -43.7005 | 2024-10-31 00:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 539042c2-a6d4-3a04-a56a-2c2be0993cb8 | -0.7552 | -62.8933 | 2024-10-31 00:45:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| b554feb7-5b65-378c-aa2d-70143822f35a | -0.7734 | -62.8932 | 2024-10-31 00:45:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 7b356202-3450-3f2f-bcdb-3f4f6226e937 | -2.1718 | -47.9506 | 2024-10-31 00:45:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 0e185cb8-eca0-37f0-9d6a-c8ac5c165338 | -2.5216 | -48.4591 | 2024-10-31 00:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 8db1e7f5-3c8d-34cc-a189-5049c0bcdd2c | -2.503 | -48.4811 | 2024-10-31 00:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5a533ffa-bec9-3273-af4d-7b2c43429eae | -2.5031 | -48.4596 | 2024-10-31 00:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1d4ef9af-5faa-35f6-b09e-3caadfa9575a | -2.5215 | -48.4806 | 2024-10-31 00:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 744335c6-af66-30d4-ad95-4326b5f22881 | -2.54 | -48.4801 | 2024-10-31 00:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b0550c98-0965-313a-8502-e6dbbda44490 | -2.5401 | -48.4586 | 2024-10-31 00:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4eea37ed-4e49-3bab-a6e9-c35f0fa68730 | -2.8109 | -45.4875 | 2024-10-31 00:45:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 2b89deaf-5d7c-33c4-bb95-3c24eaab6aa2 | -2.811 | -45.465 | 2024-10-31 00:45:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |


[Clique aqui para ver as próximas entradas](README6.md)
