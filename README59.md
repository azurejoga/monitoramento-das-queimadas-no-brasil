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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fedc7372-2589-37ee-a901-d6d3815ffaba | -3.82233 | -47.49304 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c58043a4-fcd6-3226-830a-7a268f3e1595 | -3.81245 | -52.38817 | 2024-10-05 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45e402c1-bf09-304c-a35f-d435073b9ff7 | -3.8118 | -52.39207 | 2024-10-05 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05969d62-deed-3f29-9f32-599af304e0f2 | -3.79141 | -52.3064 | 2024-10-05 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 714d206b-5f45-3e8e-a12f-54d9c72fc456 | -3.77171 | -47.60627 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf430af3-f02e-306c-a516-1e2eba75d282 | -3.77107 | -47.58395 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4e8dddb-53c0-38b0-9b73-d77430dee2e5 | -3.76961 | -47.58394 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a92adf8f-6446-3ad3-af5f-6cb94e9a7708 | -3.76796 | -50.56403 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 491c36c9-69f6-3ded-9fc0-8db6d338db16 | -3.70152 | -47.59835 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e74eb80-0049-30f2-a5e5-2fad83899a2d | -3.69743 | -47.59766 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90e4c6cd-405a-3032-9b57-1e9229f6e4b8 | -3.68437 | -51.16072 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abdc7ab3-a827-3c74-8c1d-48c734fb5585 | -3.61846 | -47.5221 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2b8e36fb-cf26-3d7e-b13a-4679d974c2f5 | -3.61786 | -47.52575 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d2c3a11c-d480-36e8-a1a5-61e047f9ff9c | -3.61496 | -47.51782 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1b47bbe7-5c6c-3145-b3ba-38acbf52af64 | -3.61438 | -47.52142 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1e813367-7b9d-3560-947d-46e511f5c002 | -3.61379 | -47.52505 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 30346dda-a2cd-3775-b8a2-24308d7d013c | -3.6103 | -47.52076 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef0b4add-f5d8-3aaf-8103-95a185b23074 | -3.6097 | -47.52437 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fff9277-aadc-3cb1-883f-b032073bc39e | -3.60621 | -47.52011 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0317fcb6-4101-3af6-a6d7-1969067dde28 | -3.60562 | -47.5237 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caf16ecf-34e6-36bd-b640-e33c4ce2a149 | -3.5713 | -50.57872 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 310495ac-f36e-37e0-af25-1644a38adb0d | -3.57083 | -50.58156 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eae990d3-d6da-317e-ac39-6b47d2978d4d | -3.56571 | -50.55003 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 808b3b73-6eb2-3f5c-8b91-7f1a410993f2 | -3.54459 | -53.01978 | 2024-10-05 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9109dc25-a2b4-33b1-9f1b-f3ab39a27570 | -3.54381 | -53.02432 | 2024-10-05 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be658cfc-4e61-35f2-8931-9003f0e7b8b4 | -3.49604 | -50.81176 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a53bada6-64ef-3305-bb97-6b18bfeb852b | -3.49194 | -50.80481 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3237c109-d4c3-3277-99fa-aacd97eaa9a2 | -3.49144 | -50.80783 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae07ab46-e0b8-3e3b-a003-1e9533bbad85 | -3.48177 | -52.83412 | 2024-10-05 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb95346c-0cc5-3de4-9b34-2a5053c51abc | -3.48104 | -52.83843 | 2024-10-05 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 025ce555-92d2-3887-aad0-50522aef8e8a | -3.46654 | -47.66315 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 006cacb6-0ba8-3345-8da9-8eeae7d69ede | -3.46241 | -47.66247 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6de695a-5899-3aec-ab09-4ac0ea1345e0 | -3.45375 | -48.82409 | 2024-10-05 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba25adb0-c946-345e-b565-26b8a772c59b | -3.45181 | -48.8214 | 2024-10-05 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c56295e3-d092-3ebb-8a17-7430102a3588 | -3.45111 | -48.82574 | 2024-10-05 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de8ea011-f095-3cac-9245-5c694fa581fc | -3.44563 | -50.6595 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da452233-f306-3fce-9391-411c79ef1a98 | -3.44514 | -50.66246 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f744421-0917-3119-811a-416a207edcbb | -3.44466 | -50.66537 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab99c117-4b0e-3bf2-9ef9-de5d7a7b19fa | -3.44008 | -50.66155 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa1d3c78-7832-305d-a60d-bf9df91f38bd | -3.43959 | -50.66447 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 647dd68f-cad1-308d-b0f4-78d71f463898 | -3.43502 | -50.66064 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4f2dfd5-4967-3b91-bf62-75527842170f | -3.43453 | -50.66356 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 292dec93-5344-36bf-8179-333b5276d45c | -3.43404 | -50.66652 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a612110e-47f5-3fc1-a789-7d45a6b200e0 | -3.3989 | -50.97462 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 483cb8a3-eb85-336f-945c-39023d8136d3 | -3.39886 | -45.28641 | 2024-10-05 04:12:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 126727df-9be0-330d-97a3-d104014a75ba | -3.39593 | -45.28178 | 2024-10-05 04:12:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 993711c1-8af8-3769-a6bf-33926aaa06d9 | -3.39526 | -45.28585 | 2024-10-05 04:12:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a0f622-fb13-3aab-af0d-4bd657a10a7a | -3.38817 | -49.24598 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f15d706e-947b-3c14-85fd-2d8e232bb290 | -3.38742 | -49.25068 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51393568-f192-31de-9a75-cd4cc4953b04 | -3.38691 | -49.24781 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ba02945-5011-3b5b-9628-46d04739eba5 | -3.38357 | -49.24524 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 779bc763-048f-330c-b5a4-fb7c22915d3c | -3.38281 | -49.24993 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb190b71-6130-32cc-bde6-b3e8c7323e5b | -3.3206 | -46.98688 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 100b0159-b8fa-33b5-8fe1-de0e8c71806f | -3.31976 | -46.99196 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c78ee3d-74af-34c6-9252-85989fa992a3 | -3.31769 | -46.9888 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d8eb77be-8815-3df9-99b9-acbfe6f2ca67 | -3.31472 | -47.02229 | 2024-10-05 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0e8040f-d69d-366d-aff5-664422f7f20a | -3.31357 | -49.47066 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4abc6c7-07a4-3562-ba9f-5e04c8a216e6 | -3.30969 | -49.465 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a538091d-a694-3b91-99a9-0ba55e187a36 | -3.30889 | -49.4699 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4025b547-3f63-3fd6-a555-128de0dd8574 | -3.30703 | -50.045 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8046c69b-0b2f-3625-9e47-286eaa1adaef | -3.30688 | -50.44913 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0f98f1b-774e-3942-850d-6334a35033da | -3.30594 | -50.45494 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0db4ead7-4e65-357d-8474-4ccdd728f61f | -3.30553 | -50.451 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 911e1eba-037a-3837-b8a3-31e84180f27b | -3.3042 | -49.46914 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 685c8a37-88b5-322f-a77c-cd8015bc4c37 | -3.30408 | -50.46646 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca77c71a-c3f3-3fc7-8772-81e80893f9cb | -3.30357 | -50.46257 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bce160c4-bd20-35f5-a514-d5514f85e5f0 | -3.30316 | -50.47217 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 578b02f4-dc45-34af-a9a3-7cddbf3a4268 | -3.30261 | -50.46824 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ac95d33-b621-3ecf-8406-3f41c131d244 | -3.30186 | -50.44835 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 137296ca-26a1-3673-b64a-49913302dbd0 | -3.30093 | -50.45409 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9bc07ed0-beca-3e46-9d24-7bdffb4a0d13 | -3.30052 | -50.4502 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21f54457-3985-35c2-9039-3962b4554bd2 | -3.29954 | -50.45594 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b24f239a-8b91-332b-90ed-fb86713347d5 | -3.29921 | -53.35083 | 2024-10-05 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6636f4d4-f88d-305b-aac5-005e3a6ecddf | -3.29906 | -50.46565 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c377fbe8-7a01-3b6c-ac32-7a31c183ba77 | -3.29844 | -53.35539 | 2024-10-05 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b400719-1d9a-3ea2-a60a-50227f605da0 | -3.29684 | -50.44758 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d6de6c8-5bb4-3b9b-95fb-dec5bc3a428c | -3.29593 | -50.45321 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a695d086-6e2e-3c3b-b83c-de7fab1665c0 | -3.2955 | -50.44941 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 869e2518-4b6b-3e2b-b0af-73b5c9e5938a | -3.29503 | -50.76121 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 878d5070-dc49-338f-a967-654c5f9f46b0 | -3.29454 | -50.45504 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 085cf52e-612c-322b-acbe-1440353ab042 | -3.29182 | -50.44676 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a376e0a-e7a7-3e53-ae9a-7f5e3c055fee | -3.29092 | -50.75429 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab6427a6-8599-33f2-b200-f8b65c2b21dd | -3.29091 | -50.45238 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28bac0fc-d136-3607-818b-44c4498f3f88 | -3.29049 | -50.44859 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f0a055c-7221-3e43-8e70-3a66d3f6e17d | -3.29042 | -50.75732 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fbadd6c-79c1-39a8-8e61-2abc87b1635f | -3.28998 | -50.45811 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 655e69a8-6d6e-3335-b0b6-7be9b3c67fea | -3.28991 | -50.76035 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22457158-6bb7-3990-8a91-7c9ba2fb5433 | -3.28953 | -50.45421 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44e67d6f-dae5-3ca8-bb22-552683108e96 | -3.28682 | -50.44591 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f725a217-5d7c-3d96-9c45-dc8e61e12987 | -3.2859 | -50.45155 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5942969f-c9b8-330a-817a-6469f22ee542 | -3.28548 | -50.44775 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8057dd5-af92-3195-bcc1-4aa685ed7ca8 | -3.28497 | -50.45722 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0593cbd-4366-3ad7-9326-443fe8685d7c | -3.28453 | -50.45334 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d3862aa6-266b-37ea-a66a-faaf34f9c290 | -3.28089 | -50.45065 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8c58a861-90b0-3381-807d-6a1810d4fbdd | -3.27899 | -48.79971 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f7fd7fb-1ef7-3a97-b2f5-b9510dc6291e | -3.27452 | -48.79895 | 2024-10-05 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63d8c527-f836-3350-b1ef-cf02f3a63757 | -3.26991 | -49.10945 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0349fe31-1907-3356-8161-3ac3d741a13d | -3.26533 | -49.10871 | 2024-10-05 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 551cf996-c2ea-3265-a4f0-ac7376afaea5 | -3.26146 | -50.13738 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ccda426c-b9de-3d85-a715-360e73cff21d | -3.25995 | -50.1359 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README60.md)
