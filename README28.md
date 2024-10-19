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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5253445-6fcd-3a16-9d4d-842586cde3cb | -3.58342 | -48.94351 | 2024-10-19 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bce4fdd-1aec-35b4-aa04-80e6451d79fa | -4.29196 | -48.60278 | 2024-10-19 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f74a6a0c-c8ae-3cef-a659-7b7a23cfb0c2 | -4.0348 | -48.94054 | 2024-10-19 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0318d267-e6b3-3df5-94e9-596720b821ef | -3.92775 | -48.35909 | 2024-10-19 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f78f9f1-02dd-36b0-ba83-e5e69ec5ea13 | -3.90948 | -47.95256 | 2024-10-19 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5c91fad-fe23-3f53-8a0c-11176a002e15 | -3.90818 | -48.33835 | 2024-10-19 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 332452b5-a607-3a35-ab90-8b826b92a9a6 | -3.77316 | -47.73705 | 2024-10-19 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae2004e3-e13f-3b66-8eaa-00fb85117570 | -4.79089 | -48.74461 | 2024-10-19 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12f1ba1c-3a3f-3f0d-ab88-0746e9f98a57 | -4.50332 | -48.80201 | 2024-10-19 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2635c3a-d8b1-3c46-931a-9c5240bbf26d | -3.58763 | -48.94 | 2024-10-19 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa3fbed2-c422-3303-9b53-b84a0d1e958a | -3.58405 | -48.93945 | 2024-10-19 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e2761fe-ca29-32e8-98cb-1d8cf9efe7d8 | -6.01218 | -48.1804 | 2024-10-19 04:49:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9027776e-c46a-33eb-83b0-225536da5469 | -5.28748 | -48.31818 | 2024-10-19 04:49:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c2f008d-b103-3690-ab0a-b1a3994f1b0d | -5.28816 | -48.31365 | 2024-10-19 04:49:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 502d33bc-42eb-3829-ad9e-4aa7ee3a5e6d | -7.9833 | -49.69308 | 2024-10-19 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 349dc69b-9aff-33cd-94f7-05b16b8d27ef | -1.13498 | -49.04617 | 2024-10-19 04:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a89d0a58-1d1c-3b91-9c17-62451177afb4 | -1.1315 | -49.04562 | 2024-10-19 04:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06d019e5-05cc-37c1-98a5-3c4aeb382a04 | -1.12861 | -49.04127 | 2024-10-19 04:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 456097c6-c0fe-3e38-838d-b00ca4936cde | -1.12572 | -49.03691 | 2024-10-19 04:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2f7232d-2293-31d2-9456-38eee6966371 | -2.19639 | -49.12768 | 2024-10-19 04:49:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9de6aba7-0530-323f-9821-dbfc6aeeeb69 | -2.14806 | -49.66948 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dab23446-7380-3a3d-957e-2ab553fc0b1b | -2.1958 | -49.13155 | 2024-10-19 04:49:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 525ff461-fefa-3f81-9551-0feaeacfc886 | -1.91547 | -49.52462 | 2024-10-19 04:49:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91e07d22-0750-330d-9347-5b964f285fd0 | -3.53182 | -49.97142 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7b824d5-7bc5-3740-82e4-76cbb7e7fc5b | -2.66621 | -49.72415 | 2024-10-19 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69263bd0-bc57-3f34-ad0f-5ddf4dbea037 | -2.63951 | -49.26796 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 828d13e0-e37c-3ecf-b167-b84ab66cacc2 | -2.63663 | -49.07644 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bbd0391-9ac2-3ebf-a8a7-4356d11e6049 | -2.62991 | -49.0724 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1b0992a-209b-39fd-a6cd-6a56aa0c46f8 | -2.62712 | -49.11506 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2977cff1-5209-3acb-b01c-f3c0d62b3aaf | -2.60738 | -49.10097 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bfd0116-afa7-39c6-b2da-371c3061e336 | -2.57145 | -49.12343 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a85eef6-1675-3609-b533-9b9aa26c821b | -2.57057 | -48.94213 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf434f14-6f38-399f-a6f3-fc42f125ea8e | -2.56996 | -48.94611 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f3ac39e-9ef1-3c4e-85f4-ba56ac71ad96 | -2.56917 | -49.78951 | 2024-10-19 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8523f7d-b193-3a74-bd87-5bcbad0400a0 | -2.56397 | -49.21768 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c462613-adff-38a7-9f74-1e7c59609c00 | -2.56046 | -49.21713 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5eb9a32-7abe-3846-a59e-108712b51720 | -2.54859 | -49.85419 | 2024-10-19 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b07e24d9-f441-3d7e-8227-e9317a6b2790 | -2.49554 | -49.28987 | 2024-10-19 04:49:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfdbaccd-6ca6-344c-9add-88f59a5a55ca | -2.48409 | -49.10707 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a147271-65f3-3c88-b436-6ca26bb97600 | -2.47372 | -49.40068 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 825be510-c302-3d0e-b2c5-38e247e3c1f4 | -2.4115 | -48.94764 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aed507b8-3a5b-3eec-b328-12cac2f4b5db | -2.40796 | -48.94709 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc381f06-55bf-3782-bc1a-6f92c2ee012f | -2.35441 | -48.91859 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be0990e1-c2d1-3220-a4d8-86ca0ccf0f85 | -2.33655 | -49.10454 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d28d28ba-beca-369b-9ecb-a2e13d3ebace | -2.29675 | -49.92485 | 2024-10-19 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76d4a9e1-a7f2-37b9-97bc-f3c00d7efe15 | -2.20671 | -49.5645 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a34876a8-9876-368a-a67c-04b9ebc47caf | -3.27287 | -50.17672 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f417da9-43d0-3785-96b7-768a0d84741a | -3.26989 | -49.08359 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95df7c71-e918-3370-92f6-6145b70cab9f | -3.26945 | -50.13145 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a03069e2-2edc-32b2-bc86-b79ce812317a | -3.26927 | -49.08757 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd315602-ff68-313b-b3a2-0e949a1e318f | -3.26605 | -50.13093 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07b1c97c-54c8-32a4-8074-ac278bc89c16 | -3.22383 | -50.35793 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8258e401-e1b2-3996-aed0-0e5a4762c854 | -3.21989 | -50.36099 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4da46d49-8cf3-3d6f-bea9-c68906e315ec | -3.21706 | -50.35688 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4cd9ca7-1c18-331f-9817-29bcf1401639 | -3.21651 | -50.36046 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3772bb8-4671-3c65-bdf6-62a3c446bb68 | -3.19349 | -50.30516 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26d2ce08-5fd5-3e18-837b-b2c0a35ac2fd | -3.07172 | -50.36762 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 108b382b-9019-3cb5-bcb5-03d3c6bbc1e8 | -3.06947 | -50.35992 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e756069-46a9-3e02-a39e-38961fb37a3e | -3.0689 | -50.36351 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f593699-1f71-3fdf-b235-22b1cb6a2352 | -3.06702 | -50.49467 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e2ff266-b977-36ad-920c-3647d395d1a2 | -3.06609 | -50.3594 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe8a6f3b-57ec-348e-a464-901fdc5128e1 | -3.06552 | -50.36298 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bddae0f9-4c8e-3026-8521-4437fce2f22e | -2.96421 | -49.28778 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4f602b3-c075-3349-b1b5-c3eea31a1e7e | -2.90322 | -49.3775 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c388b659-ec93-3c3b-a393-cc682c6d60a4 | -2.83988 | -49.8639 | 2024-10-19 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 935bbe5d-472a-36e8-b861-27373e05489a | -2.78104 | -49.32811 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b46b78c4-fbb3-3cf0-999c-caa4f85561b5 | -2.78089 | -49.23723 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c658e0c8-e48b-3aee-9406-8e68b1bca02d | -2.78043 | -49.33195 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7ab060f-47f1-3575-828d-76c71e300350 | -2.77694 | -49.3314 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9869c77-a3d1-3168-9e7f-e91cfbf88983 | -2.76807 | -49.36532 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a651f99b-ea73-3e9f-af63-2a30b283e5c6 | -2.71312 | -49.16423 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49c0b0ba-b76b-3be8-8fe0-80ec3ef8e581 | -2.701 | -49.03399 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc1fbecb-e207-3e88-af8c-1779ad4f105b | -2.63017 | -49.07144 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c87f6f6-2e79-30a6-9836-830022626782 | -2.62701 | -49.06793 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df1dfd4d-d6b6-3806-b1df-06f70aa0a42f | -2.62639 | -49.07186 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 581e793a-c65f-3aef-aeb1-ff7c437cefcf | -2.62286 | -49.07131 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 917eca75-0bba-35de-881c-ab8f3fddf9db | -2.6109 | -49.10151 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4dc6871-44b0-3b31-afd8-18ebd30a2cc1 | -2.56935 | -48.95006 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 152381d3-88ac-3411-b119-e6e77bdba9ad | -2.55722 | -49.70808 | 2024-10-19 04:49:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a049b341-2652-3844-8626-5a82288ff625 | -2.48531 | -49.09927 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a97946b2-4b71-3139-8249-c2963290d5dc | -2.47159 | -49.39951 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4edcf45c-21ca-3f8f-9bee-0a8e3942f005 | -2.45541 | -48.9661 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92065c22-71af-3784-ac00-383dbfb99768 | -2.43643 | -49.61448 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40ae5ea1-0a3e-383e-adbe-ef4a29bab613 | -2.41212 | -48.9437 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6dd089c-f23b-3bcc-a4cb-7c58307490ae | -2.40858 | -48.94315 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc80baea-e7bd-3da3-bcec-43bfce535f88 | -2.36162 | -49.3563 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6b41bd19-9636-3fbd-bab6-86c1a489e012 | -2.36102 | -49.3601 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 015f5a8c-6815-368d-a9f6-494e5ca327d2 | -2.35814 | -49.35577 | 2024-10-19 04:49:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b1f1ff3-d70e-3063-beb3-cb983d8058cf | -2.35754 | -49.35957 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 038fa80d-b0ae-33f1-9757-d8f9c90ee1af | -2.34858 | -49.65809 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc8c5d61-636c-3d75-a49e-9284b9cd3845 | -2.34801 | -49.6618 | 2024-10-19 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbb56bca-efec-36ca-aaf0-964aef952bf6 | -2.34006 | -49.10508 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ce829d-9635-3bcc-9e89-5fdfd46f4472 | -2.33535 | -49.11231 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9aca9b02-1c86-3112-8f00-904b185b7ceb | -2.33364 | -49.10011 | 2024-10-19 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee93ed69-8365-31df-a9e8-eeb840097803 | -2.46287 | -50.24915 | 2024-10-19 04:49:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b19928e7-c795-3dac-b968-be946dcde226 | -2.46232 | -50.25274 | 2024-10-19 04:49:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1497eba-0940-3639-92c0-3378224c0171 | -2.45949 | -50.24863 | 2024-10-19 04:49:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36920264-8288-300d-9ea7-da073f23e63f | -2.45894 | -50.25221 | 2024-10-19 04:49:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15a9948d-9559-360b-82b7-0d5ef3bf4c59 | -2.42671 | -50.27312 | 2024-10-19 04:49:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0289b320-be70-3cc9-bd62-061edf7d4ffd | -2.42615 | -50.27668 | 2024-10-19 04:49:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README29.md)
