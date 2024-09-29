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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0abad43a-b353-35de-933f-eff6d6570295 | -17.11905 | -56.179 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9ae98a2f-7095-3d50-a6a6-3193cb813a2e | -17.11859 | -56.18382 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 409a0d4f-c222-3bdc-a54b-68dcfe08ce67 | -17.11857 | -56.17891 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 59f33f3d-f688-3734-aca3-9632616df4f3 | -17.11813 | -56.18862 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| abd091e9-2f3e-3e14-9648-4bc08d2f2f81 | -17.11808 | -56.18373 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d38bc003-5f31-3e5a-b51b-4b19d7cce1b5 | -17.11768 | -56.19341 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 058faf81-4635-323b-8a79-63b08e39cdc8 | -17.1176 | -56.18852 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| eacbd2c3-0f22-37ed-9fd3-0f51d8d28e50 | -17.11711 | -56.19329 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| bbccb898-c7ef-3622-a594-eb3db6b7aaac | -17.11632 | -56.20782 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 5b466dc5-93ec-37f7-9b13-fbb493c1642b | -17.11586 | -56.21265 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 26b1f99e-78b9-36a3-92f6-d43ed1fd1628 | -17.11565 | -56.20768 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a4bdfbcb-6143-34f1-8b0b-c80550631112 | -17.11541 | -56.21742 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 44f9307d-a324-3f06-9474-eb49cf38e92a | -17.11517 | -56.21249 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 85aba4cc-8b19-3cf5-8c4c-f7027a1f4acd | -17.11468 | -56.21726 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 2b9a015e-344b-3235-a6d9-f552142cb652 | -17.10907 | -56.21176 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e5aaba12-d200-3d7c-9600-c70a26c7b0aa | -17.10298 | -56.21103 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 174e48bb-3f7e-38fd-8b44-86dac46eb8b3 | -17.07916 | -56.13993 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f1c1ef09-06c7-304b-a551-25a299ad9e83 | -17.07352 | -56.13434 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 60e942ae-32ae-32cd-a794-676fe4a38550 | -16.50767 | -57.3595 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d704e74e-6c64-3a90-a147-e54e34aa84ad | -16.48553 | -57.3717 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ef2ea444-2cb4-3571-9a76-2a0caf0cdf8b | -16.4799 | -57.371 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 82bf7637-5b99-3bf2-9263-e249aea44d6e | -16.47709 | -57.37956 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 196a2d15-8cff-3a71-9963-b05edf91c0e6 | -16.47385 | -57.37423 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 88c6c3b8-d1f6-3777-a46c-30d6cda8fb83 | -16.47342 | -57.37814 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5660098e-5082-3e35-b91f-4e0bb913ce91 | -16.47187 | -57.37492 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 845488a3-2e85-3703-bd92-6d78d8cfd0ee | -16.46823 | -57.37355 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bd4381db-50f1-3beb-836b-ef099dcc9360 | -16.45519 | -57.33618 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5ff7781e-87c9-309d-959b-49e89156aeb8 | -16.44955 | -57.33548 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5bc3c8ad-7e50-328d-af8d-06081ed97103 | -16.12054 | -57.53217 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| adbe94b8-8bbd-3636-86c3-aa366fa23d2d | -16.10979 | -57.52788 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a496391d-5b97-30dc-94f0-801d1839e44c | -15.94989 | -57.2033 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff0382dd-0a19-32be-9d70-561fa324f185 | -15.9447 | -57.19841 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0c0cb49-4496-379f-b2be-c59e53b6b3dc | -15.93898 | -57.19841 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1851e35b-0432-3384-977f-104321733d6e | -15.93324 | -57.19852 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 645774a3-55b8-3107-89c4-a9a1b1bdc8a9 | -15.90967 | -57.20477 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 66564b25-da3e-3280-8bb4-182c1fa5794b | -15.9048 | -57.1969 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f26cb6e4-1b91-32dc-b282-82d93d516412 | -15.83349 | -57.39465 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de4e9313-9469-3a17-9c3d-72976723d8ec | -15.83181 | -57.4019 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c77d21b-5f10-39f9-af6e-f19b0100ae26 | -15.82691 | -57.40291 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6dd89a82-6d77-3abe-88dc-591067fb9a9a | -15.82136 | -57.3514 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b47e463-5830-3e42-8fb8-132ec1f375c5 | -15.8197 | -57.3664 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf0544ee-df27-36e2-abec-0edd479448f7 | -15.81568 | -57.35163 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 248a676b-e616-326f-8562-d47ac008a79f | -16.1157 | -57.52525 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 928b5627-f4cd-33a2-948c-b1c9008434ac | -16.11535 | -57.52834 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fbdefcb4-6760-3a11-955d-871e3cffc1d0 | -16.115 | -57.53152 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 340a87c7-3499-3c36-a537-74a3749b379e | -16.11013 | -57.52473 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 940f9801-5e25-384b-9efa-f1b1163e1ef2 | -15.93374 | -57.19394 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 244f4259-480b-33c8-90c2-27f485b189bf | -15.92797 | -57.19437 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5adf4e6d-c41d-345b-81e8-3ab0e474af9c | -15.92665 | -57.20648 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6547e4fb-2eb1-3880-9d05-390321171a23 | -15.92625 | -57.21011 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e288118-ba65-3e5b-a0ee-cf48e4b64ab1 | -15.92058 | -57.20969 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ba5eb82-32f8-3769-80c4-b0b7718a7186 | -15.91126 | -57.19015 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 925357b5-6527-3100-911a-2688ab7fa91d | -15.90521 | -57.19315 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 309fae81-92df-3802-84df-8f9218b03bd5 | -15.90444 | -57.20024 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b686b662-14f4-386a-af54-ae27d8bad013 | -15.83278 | -57.40088 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba8723af-02a7-312f-9e73-514cfb2b8d52 | -15.83247 | -57.39579 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e027f22-bdaf-3935-aac6-2d18dbf885a3 | -15.83214 | -57.39888 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55c9c071-fdb4-38dd-8aea-7517c6fc4dd9 | -15.8279 | -57.39416 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fd28fa7-c2f5-3385-8cb2-71d54acbb15c | -15.82757 | -57.3971 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68ec0dfe-138d-3afb-acb9-f998eec274f3 | -15.82724 | -57.39996 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f77572d-7fe1-30d3-adb6-a553f77d0a23 | -15.82489 | -57.37058 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c47bb21-0df3-3e17-8baf-652575b333b8 | -15.8221 | -57.39542 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c61aa8a8-2384-33a3-984b-031c30b94c1d | -15.82184 | -57.3471 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 759b3a2e-29f7-32fc-b03c-c729b22983eb | -15.82175 | -57.39855 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3eff7ea6-cdcd-3503-a002-ab678e296263 | -15.81918 | -57.37109 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43403d20-440f-3bd2-bbc3-df4808043e49 | -15.81511 | -57.35676 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d495ee78-a909-340c-8e0b-40cca6d5757b | -15.81454 | -57.36192 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f3856a2-0cfb-3824-870f-192ac1b99099 | -16.78952 | -57.49231 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2c212b7c-7f02-3f73-834f-54dbd344cf01 | -16.78585 | -57.49004 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 727f06a9-2720-35d1-ad78-4d9d77f14e67 | -16.78544 | -57.79983 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1113612e-cc61-351c-961b-4ac359d70c98 | -16.78505 | -57.80353 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 515fd2e2-3c2f-3392-95e0-d1263b2c35cf | -16.78465 | -57.80724 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b98254db-287f-381b-a5ce-040c3db4edb5 | -16.70733 | -57.53516 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cb21952b-6241-3642-a2a5-0434b683d04c | -16.70175 | -57.53447 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d78e95fc-d610-39dc-85f3-8415ebe61fcb | -16.70134 | -57.53833 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2d894d16-a6d7-363b-bb5b-029ca065da30 | -16.68224 | -57.44944 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fb936e82-1383-329c-8752-16f7c171a206 | -16.67843 | -57.4477 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 055b4cf4-3cf8-3b69-ae6e-b0ecb582a457 | -16.67801 | -57.4516 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 216bea3b-05c5-3d43-a96d-bb80ae502b03 | -16.67663 | -57.44873 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 429a0ee9-3cf3-3bba-bb80-68d31302c575 | -16.6724 | -57.4509 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d67e0f29-9107-31d1-814e-4fcea4b4445c | -16.67197 | -57.4548 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c58bfb11-fe60-3dba-a56f-0a485e9c50c2 | -17.0554 | -56.73565 | 2024-09-29 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 32436a84-eb0d-314e-b40b-35f0b0cac498 | -17.04996 | -56.73052 | 2024-09-29 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 88fb3e5b-ea8e-3200-9a53-dca03593cc1a | -17.04951 | -56.73494 | 2024-09-29 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 74592b19-1862-34cc-99ff-b3bb07839f15 | -16.96667 | -57.9398 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ab51fd8f-fd1e-3b06-bbd2-c917d3ebee67 | -16.9652 | -57.94151 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d2576f04-f5fa-3072-86d3-0d0a261d29a4 | -16.96121 | -57.93913 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 822417e2-6201-37d5-a1b1-1374a7373c69 | -16.96016 | -57.93716 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 628b88ca-7c47-3316-9855-42a0e9e1688c | -16.95975 | -57.94082 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 69e32733-8354-3472-bcbe-43e1477d7fbe | -16.95653 | -57.93106 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 503230a6-956a-327c-8eb5-d0ae1445a5af | -16.95615 | -57.93473 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6c11711f-8203-32b0-90f8-43eed0313883 | -16.95576 | -57.9384 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6000067d-9337-3731-b10e-df2d72917da4 | -16.95553 | -57.92913 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bab393b1-9c64-3e83-84f5-35b8e9a084e5 | -16.95512 | -57.9328 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e706abf2-bfe1-3b1d-a55f-97ada04630b6 | -16.95471 | -57.93646 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 167a897f-10dc-3db7-8135-d6130e273983 | -16.9543 | -57.94012 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8c24f9ad-992c-3bfd-8dbc-d3f1db3c7c7d | -16.95389 | -57.94379 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| ab0d663e-544a-3c69-99ed-5d0bd05979b2 | -16.95107 | -57.93038 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d3b07939-24e0-31ca-b1be-c7c2c17fe666 | -16.95069 | -57.93404 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 57a6c35f-0b84-3568-8697-dffc2232f065 | -16.95031 | -57.93769 | 2024-09-29 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |


[Clique aqui para ver as próximas entradas](README70.md)
