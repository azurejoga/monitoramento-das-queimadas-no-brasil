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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60ed01a6-104b-393f-8314-a7cfe88e5875 | -6.83483 | -51.22524 | 2024-10-03 04:49:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f81b5e8a-0457-338a-ac0f-09a6cde79b19 | -6.73597 | -50.96023 | 2024-10-03 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40fcbce6-f9cc-3ee0-9b12-825bee798a86 | -6.56733 | -51.12556 | 2024-10-03 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af03b218-7952-332b-988a-f565f7948d8f | -6.54811 | -51.04805 | 2024-10-03 04:49:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50945e72-7d73-3f52-a5af-979a637315a2 | -7.39226 | -50.22038 | 2024-10-03 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cab1623-30c9-3487-9c78-11ed0469c1da | -7.28102 | -50.31203 | 2024-10-03 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92474d22-7f2e-350d-bbc7-c224b6ec5eae | -6.9542 | -50.58706 | 2024-10-03 04:49:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52a586b5-c2d7-3721-acc9-5a720df0588c | -1.62274 | -50.53924 | 2024-10-03 04:49:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56cd0871-1b98-303e-a253-64a8336a0b13 | -3.49114 | -50.80559 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a1d3019-cd2d-35a3-9af3-ac7ba5001500 | -3.48779 | -50.80507 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b97dd36-4825-36f7-a3d7-893af7ab45ee | -3.47184 | -51.77621 | 2024-10-03 04:49:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93d1b4d7-fecb-3f6a-8cb9-faa7703e22de | -3.4574 | -51.06677 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32229ca1-10c2-38fd-9e0a-52d9cd0ce13f | -3.45686 | -51.07026 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85ee7912-7bdf-3486-a5b9-a7c403a19e60 | -3.32641 | -50.78348 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7078a754-a6d4-3cea-96b7-53d55138a48a | -3.32586 | -50.78701 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c28e5613-b228-34d8-9522-f1b836f6e4df | -3.32531 | -50.79053 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7ae586a-2739-31c7-9fab-56f21940f4cd | -3.30263 | -51.11042 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aabd12c6-9de2-32b1-a306-8325d0434e5a | -3.30209 | -51.11392 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c21a7b-aaf7-371d-97e5-d7c3000df573 | -3.2993 | -51.10991 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6005239b-6dbe-37f1-9830-b769ba9eb75d | -3.29875 | -51.1134 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa2a94aa-81a9-3613-83e6-2cd9992c87d4 | -3.25426 | -50.93811 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4903c3c0-e729-3513-905d-6ee0b377f390 | -3.25371 | -50.94161 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edf261f8-a732-37b9-a43e-7add52f638b8 | -3.22436 | -50.78969 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f3fe15f-3632-37a2-b1b1-76fc1f29172a | -3.22381 | -50.79322 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b751b851-4a68-39c1-87a3-226f0853401d | -3.22326 | -50.79675 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90eaa2ce-b882-3111-af2a-601d9bdd5d2a | -3.22046 | -50.7927 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f7533f7-81e4-32f9-9a0e-090ef8b94a5d | -2.90103 | -50.71434 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74b8a5c5-1209-31d2-8732-db45daa880d0 | -2.90048 | -50.71786 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 106c7593-1610-31f9-88db-1a9e59a6927f | -2.89993 | -50.72139 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9b268af-2f6e-3d17-add4-c212f9a65efc | -2.89937 | -50.72491 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54c33c96-c085-3fa4-9a3b-0e9c434e99be | -2.89767 | -50.71382 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 660dc546-ac84-38eb-9ac2-36363ec8e2d8 | -2.89712 | -50.71735 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dd80f67-c870-382c-85c4-42f161ccd7d4 | -2.89657 | -50.72087 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c4864ed-0170-3e90-815b-2b7ac50c1bcb | -2.89602 | -50.72439 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbd212b9-a8e0-3ce1-9453-577b543b11d7 | -2.89432 | -50.7133 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 905435bb-100d-30ef-b324-5b942066aa8b | -2.89377 | -50.71682 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46dc58fd-706b-373c-acc9-b7ca83d6efa2 | -2.89322 | -50.72035 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 764117b2-7513-3fe7-b149-d91115cf1418 | -2.89267 | -50.72387 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247004b9-ed90-3cee-84b2-eae5ed13c68b | -2.89151 | -50.70926 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ddab6ede-3e75-3389-b0c0-ce773e9a7519 | -2.89096 | -50.71278 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 608fec2a-51be-3465-b9f2-076a5c2d3eed | -2.89041 | -50.71631 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64dcee0-a559-3c8f-88e6-c948c4b17542 | -2.88986 | -50.71983 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f780be6d-7970-320c-8907-1cd24f551038 | -2.88931 | -50.72335 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab527a4b-ef56-3082-b65b-95b6af017ea9 | -2.88816 | -50.70874 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf9aa3be-46e4-3c77-ba90-0c24675db75d | -2.88761 | -50.71226 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7f1608e-8635-35d5-b042-2766816630db | -2.88706 | -50.71579 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 638add71-9480-30e4-b255-3918633bc8be | -2.88651 | -50.71931 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee5fe47e-3aa0-391a-827f-c903d56385e2 | -2.88596 | -50.72283 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b14c0d88-da8a-3f79-b27d-0ca7c4c3f3f0 | -2.8848 | -50.70822 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bf856264-b429-32a1-9751-6cf6a9750a10 | -2.88425 | -50.71174 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 500bbd80-7fb8-34f8-9ce6-8f32e481d9ca | -2.8837 | -50.71527 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f02b767-1aed-3172-b933-c86319b7a237 | -2.88315 | -50.71879 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06a9467-92fd-320e-92ab-ca1ec2b109df | -2.8826 | -50.72232 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b916cbc-0394-38c3-9cec-0bb36611a451 | -2.88145 | -50.7077 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be90014c-5b0f-34ef-adde-d213bf3df1db | -2.8809 | -50.71122 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce5b8657-3a23-3595-9d30-42d6bad61a4d | -2.88035 | -50.71475 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acff6282-b4f8-319a-8d26-ebc7f202eb71 | -2.90948 | -50.74813 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7f50c79-483a-3579-b0a5-30abf2191df8 | -2.90893 | -50.75164 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a2e5bef-a496-3679-9a64-bd8b8f96d4fb | -2.90838 | -50.75516 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8fc8e21-32f9-3041-95a3-bb2b0fa66ad4 | -2.90723 | -50.74057 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5abd389-0c77-39da-8f33-d9e7b2a24a79 | -2.90668 | -50.74409 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35d994a3-2e00-3bc5-a5b6-9aefce88a0d1 | -2.90613 | -50.74761 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 972ef2f8-2673-3dcd-aa66-73aed11ec575 | -2.90558 | -50.75112 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212b9c49-162b-3fc0-8bfe-9bdab4856a51 | -2.90503 | -50.75464 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a5e3ea8-f0db-3073-a752-5284edeeaad5 | -2.90443 | -50.73652 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98161172-9fd5-3fe6-b348-0f46373f710b | -2.90388 | -50.74005 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71bc954c-6627-304f-9500-810f75ab1ed9 | -2.90333 | -50.74357 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f892f3d-c493-312c-a3fd-428860599ac7 | -2.90278 | -50.74709 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ff561ff-fd65-3e68-9d9f-507c86dbd490 | -2.90223 | -50.75061 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ac7237-acba-320d-9858-102b8ff346d3 | -2.90168 | -50.75412 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd90a967-1433-334f-8dc2-8475b7f2dc17 | -2.90053 | -50.73952 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cfff191-9e4b-3e3d-9b32-dbf580b750b3 | -2.89997 | -50.74305 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 198a1bdc-9203-3d76-8826-78f3712c0933 | -2.89942 | -50.74657 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc4bd024-727d-34ee-9048-68f3b5704d1b | -2.89887 | -50.75009 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66fcb10c-2953-3905-8e94-20de9d3ef864 | -2.89832 | -50.75361 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb06b1f3-80a8-3588-abfa-f0015bcc7836 | -2.89717 | -50.73901 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b166effc-ecf6-3f5b-b6b2-1839568d9458 | -2.89662 | -50.74253 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76f33622-386c-3c77-95fd-7e120b7fc6aa | -2.89607 | -50.74605 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca10050f-9943-34f7-8df2-2fc9661daaf3 | -2.89552 | -50.74957 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a065a3a3-44fb-3973-bba8-c50b7908cf46 | -2.89382 | -50.73849 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b63ee149-a3c0-3d04-b484-33948a853231 | -2.89327 | -50.74201 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 910ed0d9-6e45-3536-81d6-55fe7105e8d8 | -2.89272 | -50.74553 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d737ab4-4ffc-3e33-8111-956cd44d53e0 | -2.89217 | -50.74905 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e73d27-5d88-3c53-a242-f5be54916fee | -2.89162 | -50.75257 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30cce633-ebfa-3d3f-9ca8-2f9ef856a5b0 | -2.89047 | -50.73797 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ad763f8-7fad-3214-934b-87972a9b7789 | -2.88991 | -50.74149 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c05d39ef-edc4-3dfc-86ee-1fbd1de7edf6 | -2.88711 | -50.73745 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f9b1de6-0553-3be6-a23f-85ad728841d2 | -2.88656 | -50.74097 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78afdc52-e38f-399e-89ff-2ec4cfbb7261 | -2.88601 | -50.74449 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f4f0d6c-b667-379e-a25c-87c2c1c112ab | -2.88546 | -50.74801 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43c5aef4-b677-3204-9bb7-5f577ad4bdc9 | -2.88266 | -50.74397 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7269846d-52bb-3651-944c-2714945ff89f | -2.88211 | -50.74749 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b09d0be7-975e-3a15-819f-13ab073c0010 | -2.86583 | -50.71972 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6945fae0-bae2-34de-94c7-a292360d0b5e | -2.86528 | -50.72324 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65227e3d-097d-37b8-b6c7-06280792997e | -2.86473 | -50.72676 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a9d0bac-8f71-34bf-80b3-70caee8e13ab | -2.86302 | -50.71568 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05334821-6f28-3f5a-ab43-f7797d834793 | -2.86248 | -50.7192 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92f02c2b-52a1-3b47-bfd1-63c23fad46cd | -2.86193 | -50.72272 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0ceccd7-e7bf-34cb-b63d-adda5b21155b | -2.86138 | -50.72625 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6951e80-ffd9-307d-805f-358018794a6e | -2.85967 | -50.71516 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README118.md)
