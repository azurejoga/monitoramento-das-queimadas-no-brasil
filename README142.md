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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08bd69ac-666a-31e4-8e84-d2499fde393a | -16.8505 | -55.90522 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 40f7c820-6247-3fe7-a47b-e5340e67e139 | -16.84928 | -55.88614 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 355d3450-ce19-30b8-963e-638ba17e1d7a | -16.84802 | -55.89539 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d8a35741-79c6-3ef1-ba8f-afa269bd4818 | -16.84676 | -55.90466 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f2a808c3-5c28-3ddc-8689-f9851c972af8 | -16.84491 | -55.8902 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2957918b-5205-328a-9b89-b50c76806fa5 | -16.84428 | -55.89483 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b0773d32-20a8-3d7c-8144-9a0ed6dd1cd4 | -16.84243 | -55.88037 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4f29e4c9-6632-3056-9405-3e23cbd19204 | -16.8418 | -55.88501 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 45406bab-8061-3a91-b271-50618151ca36 | -16.84054 | -55.89427 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 60ccd7d7-a13c-34bd-b7c8-f5708098bfe7 | -16.83991 | -55.8989 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5c6621ac-01b8-32ed-80c9-e6835c84f1f8 | -16.83868 | -55.87982 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b7ac3273-1cf5-3ee8-ba30-f4e029d1ab78 | -16.83865 | -55.90816 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 974bf941-ee7e-3632-9344-2df91403bc1a | -16.83805 | -55.88446 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9aa7b9a0-6a50-3f27-8117-4e3797b75ab4 | -16.83802 | -55.91278 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 09a5cbcb-352c-3c01-b645-19b11f12f07b | -16.83743 | -55.88909 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ffd647c9-e8c7-3bd3-84c9-287cf90734dd | -16.8368 | -55.89371 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 45f96932-1604-36ba-978b-7cdf7b1409ee | -16.83667 | -55.89171 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e56ff7ae-8ddd-311f-a1c2-fa4b1ce8a647 | -16.83617 | -55.89835 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 8f799e13-0bf4-3c9f-8e9a-e40670c7e432 | -16.83602 | -55.89633 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 9302ed34-394f-3a1e-9872-1ed0c840e09d | -16.83554 | -55.90298 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 95bd2f78-fb79-344f-a332-a62bda481394 | -16.83491 | -55.9076 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b235dd38-4ffa-31d7-92db-64098f356ddb | -16.83471 | -55.90557 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 1a92530d-83f9-30b4-8444-1e1b29143972 | -16.83431 | -55.8839 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fa2854ec-8321-3005-bd05-ae2a13b6b1e9 | -16.83424 | -55.8819 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 689cc006-488b-3525-a701-1c2de477e40a | -16.83275 | -55.91941 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bc5dec25-a01a-3ef1-9e67-48e89d188a08 | -16.83228 | -55.89579 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e3ae6abe-1e31-39c1-b2ad-41bc43f87507 | -16.8318 | -55.90243 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 14d6b7b6-ad63-336e-9ca3-5795b9166cd8 | -16.83097 | -55.90503 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 6a8b5929-e325-3503-b9b7-2feec26fdee7 | -16.82994 | -55.88797 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e4515d4b-b55d-3b31-9c50-d3f9308e5f9d | -16.82966 | -55.91425 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f36ecc0e-9437-3c46-b252-41e3609ef25d | -16.8293 | -55.9209 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c7963fed-ce18-36a1-acd2-a4b700714e0f | -16.82836 | -55.92345 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 98e8291c-2000-3fcb-ac63-bc5f708dabcf | -16.82743 | -55.90649 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| ebd4cc90-de56-3b9d-ba36-eb839a3fb827 | -16.82723 | -55.90448 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 9ba89dce-7ae3-34f0-a7a0-389eac8f906c | -16.82681 | -55.91111 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 5edaa0fa-b4ab-33dd-a7bd-21115a18fbc1 | -16.8262 | -55.88742 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 27fa40ff-e4d0-3d88-94c4-cb60e4c192ad | -16.82619 | -55.91572 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fb3394d9-a38f-32c1-ae91-42e3b85ff87f | -16.82616 | -55.97204 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| dee60f9d-6ccd-3be4-b764-0ab5044be672 | -16.82558 | -55.96991 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3caf92ab-0d87-3912-ae0a-8c4e72a427c2 | -16.82557 | -55.89206 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| be42a721-977c-3dcc-9b7d-dee59198e4f4 | -16.82545 | -55.89006 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0045ad86-8f31-35f2-81aa-2cca09bb5105 | -16.82528 | -55.9183 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| de7b11ec-32b4-388c-bb09-e7823f3879e5 | -16.82463 | -55.9229 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cb1cc4f3-e8fd-37cb-995d-c43d7c09d04a | -16.82307 | -55.91055 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6fc2f429-4d1b-347e-9ae8-67dc45b74a77 | -16.82301 | -55.88024 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1c67f066-a44e-3b71-befe-185ed980fb5e | -16.82219 | -55.91313 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 47840fbc-66c3-3202-8d3d-4ef41d5de429 | -16.82183 | -55.91978 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5cb5319c-0d5a-375e-aa8d-842ca43fece8 | -16.8217 | -55.8895 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7fc40976-5516-3b12-812c-8a10334569f0 | -16.82154 | -55.91774 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0ef9e99e-30f3-3b24-b370-53b08b5f7648 | -16.82105 | -55.89413 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| c448b3e5-b96f-3455-9e46-d9aac7661ba1 | -16.81861 | -55.88432 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| df6800ef-86eb-3772-bba6-76f3a8401d4a | -16.81552 | -55.87914 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5834dacb-192a-30f3-aabc-5718e096a501 | -16.81407 | -55.9166 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 26c8e032-8ec9-3633-aac6-76568686d441 | -16.81213 | -55.93042 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 00a4b1a3-53ac-35f8-938d-14cad26c2bcd | -16.81178 | -55.87858 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b97cbd14-86db-3d85-8ec0-503499fabaed | -16.81113 | -55.8832 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 170b291e-1900-3d2f-a1e6-e959787ae21d | -16.81049 | -55.88781 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 07ba4e0d-edee-339e-a4ed-2ce8fd64fd7b | -16.8084 | -55.92986 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e3056145-8c0e-31d5-a667-cb4dbaa45e15 | -16.80739 | -55.88263 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5c160ffd-d2ea-3b4d-89b6-b450cbb3fd76 | -16.80674 | -55.88726 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2a3b7d22-8a92-3f4a-856e-a35de5b481cd | -16.80323 | -55.96658 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 00e9858f-4cf0-3c71-9714-e9fd920f2152 | -16.7972 | -55.92817 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3a622969-a072-3bb8-bf05-a2c325de7ce5 | -16.79347 | -55.92761 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 376e6a89-d64e-340c-ba6a-d517f70ba92d | -17.1169 | -56.23633 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 22f9c29c-3b1c-3720-9c0f-55e89c376293 | -17.11253 | -56.40363 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0ebfcb9c-d1cc-303c-8152-69710f1d09fa | -17.11171 | -56.22857 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0a19d0d6-8faa-3b63-8c9c-290995e699b5 | -17.11052 | -56.10379 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0991d6d5-171f-370f-bc0e-53cc131049e5 | -17.10802 | -56.22801 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| af3a7bba-1a7e-38a1-9646-34a2715e1302 | -17.10744 | -56.09868 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0a20d002-2df4-3fa8-a0fc-b0559f73ed7e | -17.1068 | -56.10324 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4464343f-af2f-377a-89d1-fe7b62e85f19 | -17.10617 | -56.10778 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 06204966-6ad4-30f5-9f24-7da2761a149f | -17.10492 | -56.69486 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 03694dff-09ba-33b3-8dad-c95bcf616534 | -17.104 | -56.2206 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b6b86ada-cf86-3815-aeba-27c77cb09480 | -17.10309 | -56.10268 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d2617189-75e0-3e4c-b7e2-2005a7599c18 | -17.09875 | -56.10666 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6a936d6b-9e76-3b97-84ad-a9d6c9ab8c88 | -17.09828 | -56.71566 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9da9013f-be72-39db-b635-4bad5f913165 | -17.0976 | -56.22186 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e0e03399-8908-3f64-baf0-c0cb395d5cd9 | -17.09711 | -56.69802 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5deaef32-806f-308a-ba7b-0776ba4343db | -17.09351 | -56.69748 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6173f9c8-d4c4-3e84-a66e-49afc9e18b8c | -17.09069 | -56.1101 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f4258a8b-a679-39f1-bbe8-6b487887be13 | -17.09023 | -56.22075 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d3fbd468-bc48-31fd-a04a-d874b81a2e1c | -17.08809 | -56.70975 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7381d0da-9f7d-3ffd-8649-97d3e0401ed4 | -17.08698 | -56.10954 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 857eb805-3f96-3d73-97f1-7e15839690c4 | -17.08412 | -56.21066 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 24ccf986-6766-304b-897d-5ac0e2eecbfc | -17.08264 | -56.11352 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2d0748e0-3f49-3417-abd7-8742b21fa492 | -17.082 | -56.11806 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dc4b9183-93eb-3830-a631-17508b765d6a | -17.08043 | -56.2101 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b636f3c9-b216-3326-a812-2584678c0448 | -17.0802 | -56.10387 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0c8d29a5-496d-396b-b69c-6caf962ca091 | -17.0785 | -56.38252 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1c33b35c-c17d-38dd-abbd-e67d99ee32c8 | -17.07737 | -56.20506 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9ae6772a-ef84-34e2-8214-90ce9c0ac0d5 | -17.07485 | -56.38195 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1e304424-1307-3648-bb40-9abf48cbd1f1 | -17.07468 | -56.0891 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e029fb98-b5f2-3ae6-926b-561db3b8045f | -17.07171 | -56.40396 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e328046a-36b9-34e7-b106-7882a6184269 | -17.07159 | -56.084 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f11dd46e-f708-3112-8c2c-fc88952d9b5b | -17.0713 | -56.69844 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 281d3918-ff2e-36be-97ef-9ea203402272 | -17.07033 | -56.0931 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fcb0b051-f0e1-3d2c-a5d2-06301af784cf | -17.06754 | -56.38084 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8385a56e-95cd-32a3-b043-d5a70acfdc23 | -17.06662 | -56.09254 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9e3fc3e7-b8e7-38cb-a7a3-959b86e7f38a | -17.0635 | -56.70161 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| daa534c9-8110-3ce5-9876-0136c0e9eb9d | -17.05983 | -56.08688 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |


[Clique aqui para ver as próximas entradas](README143.md)
