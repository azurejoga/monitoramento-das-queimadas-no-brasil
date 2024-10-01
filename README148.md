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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23cb6dbe-ab8b-32b8-b367-e21ab9156414 | -16.77024 | -55.774 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e2cecb38-1eaa-3480-86b5-d7f3966c5789 | -16.76988 | -55.7771 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 8573116c-41f8-3e35-80a9-7b44164dea81 | -16.76964 | -57.78487 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 533be201-5ec3-30a1-ab87-6d6c289b793d | -16.76953 | -55.7802 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| bee08170-69e0-37d9-a157-01691fcb3206 | -16.74223 | -57.37 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 666f8767-7756-3902-be50-91ab4f4ceb63 | -16.76917 | -55.78329 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4f9fe6b6-3146-35e2-a02e-93e367ada84c | -16.76881 | -55.78638 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 50c4cba8-35dd-3d52-ae10-5029d4123730 | -16.76846 | -55.78948 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b038839c-d3e5-3009-8656-58a3a0d0259c | -16.7681 | -55.79258 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d865f43b-ab23-30f7-9ab9-8abe807a30dd | -16.76775 | -55.79567 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d20fbbcb-b8eb-3f5e-9030-60b2e9236920 | -16.76747 | -57.39308 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5c50dedb-4b2e-3f88-924e-72bea242932d | -16.76739 | -55.79876 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4478ed27-91f6-3420-84d0-4001de03fbf6 | -16.76703 | -55.80185 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1487fd2f-aeb0-378c-b8c0-d812a51449c1 | -16.76517 | -57.78426 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5ea4f5f7-bec3-315f-a8c7-0d8b9fb5fc5c | -16.7646 | -57.78881 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a2b0d48e-aba7-3b84-8e32-c6b42f50c97c | -16.76441 | -55.77957 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 41b58d5a-453c-35e8-9434-0fe32a310478 | -16.76405 | -55.78267 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9ce5e1f7-6c4b-3fec-84f1-f5d1a78754a8 | -16.76402 | -57.79336 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9ac22281-3f14-362d-a1c3-5113b51f4f43 | -16.7637 | -55.78576 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 70c231eb-4c4f-3ebf-bd1d-2e8b937591ed | -16.76334 | -55.78885 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d0b9091a-a7f3-312b-b463-584b3b8964b9 | -16.73424 | -57.36233 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2842a842-cccf-3398-9e33-a939987a25ae | -16.76299 | -55.79195 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| be63e9c3-d756-3c5a-8742-f1982e27e749 | -16.76287 | -57.80247 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fd1a74fb-3540-39aa-981a-dbb56b436cd7 | -16.76263 | -55.79504 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d3fccfbf-39be-3f16-9ec8-c9ba84c2a09d | -16.7623 | -57.80701 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5c813270-aca0-301c-a238-badce21d9b33 | -16.76228 | -55.79814 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| abbd51cc-df26-3942-9452-37052ad9d75a | -16.76192 | -55.80123 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d36a2073-0e5e-34f1-8b1c-1b0f4a040482 | -16.76157 | -55.80431 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b45a5a33-70c1-39ba-8532-05dca48f2054 | -16.76121 | -55.80739 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3a68d5c2-3e5d-3a14-a11f-0e72bb1e849e | -16.76013 | -57.7882 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 43f8c602-ab98-3994-a22f-e22a43f03dd2 | -16.7598 | -55.8197 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c111f1d8-660a-3a46-a369-a6e0a821948d | -16.75956 | -57.79275 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3a1da7c5-2a3a-39d6-8be9-00e6551eefa8 | -16.75929 | -55.77895 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 33c7491d-58fe-3e1b-b158-bb533c434c78 | -16.75893 | -55.78205 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 70966aa7-3ead-34af-9875-d3a7b6848bdc | -16.75858 | -55.78514 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f57d39d8-1b45-383a-a6a9-d10ceba9e881 | -16.75841 | -57.80186 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 48807496-8d08-388e-a022-9b057a492266 | -16.75823 | -55.78823 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 761e499a-bc21-3d04-a8f0-da663003d1c6 | -16.75787 | -55.79132 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 79e10f0d-6f96-337e-9c7a-fd39bcc80bdc | -16.75752 | -55.79441 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 47778fef-a5be-3aab-93cd-4bb3b150a39e | -16.75717 | -55.7975 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| aa54d683-7d3b-36a5-bbc6-0ab4de408330 | -16.75681 | -55.80059 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 66ef9567-e9f4-3f97-8b50-572c29d20b2f | -16.75646 | -55.80367 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 271e2d3b-4e13-384c-975f-3b4f721a0261 | -16.75505 | -55.81598 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3c6c73c6-a6f9-3e12-8fbd-ffe3aeb66072 | -16.75346 | -55.78452 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5a6715ca-c12b-34a8-8d58-058ceb51a564 | -16.75311 | -55.78761 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f1a3d759-38e8-3331-aa8d-0543a16b4a6f | -16.75276 | -55.79069 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 10c6929b-dd51-38a3-888e-39b9cc515312 | -16.75241 | -55.79377 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a25fdcf5-6aea-3dee-bf25-a2e09abb2191 | -16.73419 | -57.35904 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b6faa650-e33c-37e2-801e-b5fc21210e8c | -16.75206 | -55.79686 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7f99e402-7ad8-322b-ab85-fda8f2b208f5 | -16.75171 | -55.79995 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 50793ea6-3c3d-3c46-984a-1d1b56cb78d5 | -16.75079 | -57.4154 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d8d28dbc-3c86-3de1-8aac-12dcaa05374c | -16.75021 | -57.42023 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 13e61af9-bafc-35e5-8bb8-003fa948b0e1 | -16.74804 | -57.36416 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fa5b9e02-0698-348a-b7c6-04390a9ab61f | -16.748 | -55.78696 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8b3000b5-0fb6-30b0-93a1-e935304b8e81 | -16.74765 | -55.79004 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b7b62924-ac5b-3e71-a344-34147970368c | -16.74741 | -57.36576 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 270ce334-1b8f-3b9a-8804-3384e7d0fa80 | -16.7473 | -55.79313 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cb782ba9-a101-3ac1-af39-5c87f49f2b23 | -16.74695 | -55.79621 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4c78a88f-6a64-3c36-b06e-ca2a9c813dea | -16.74563 | -57.41961 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4548e7a2-9c9f-30fb-b2e5-4ba77c905a8b | -16.74484 | -55.81475 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2aa62c35-3a12-3c1d-b470-9ff20fa1a4ce | -16.74283 | -57.3684 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 07962ac2-ba67-3e38-81ca-6c6e30dbd1ba | -16.74113 | -55.80178 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4a7c9641-3d12-3b94-b3bb-7cba2243b70e | -16.74105 | -57.41898 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9471b5df-a453-3306-b8b3-4f754cc22b81 | -16.74078 | -55.80487 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e716795f-e466-3b4b-9c66-4f999af72b39 | -16.74068 | -57.4221 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| bc22c73b-a70f-3668-a6b2-6c64b1ee7f3f | -16.74047 | -57.4238 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3469e575-92f4-3280-b096-5c2b88886de0 | -16.74043 | -55.80796 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 940b2459-e6c4-3641-b316-839949e2490e | -16.73973 | -55.81413 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2a4418d8-725f-3809-889f-6ce067453f5d | -16.73823 | -57.36779 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 539942a5-f8f8-3759-9a1d-862f16a0e5f4 | -16.73821 | -57.36452 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8a5610c7-4f75-3a6e-8bf7-b1eaf5254369 | -16.73763 | -57.36938 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a5bd566a-6cd9-382e-86f9-3e599a3f5b46 | -16.73647 | -57.41837 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a2abca5a-6b35-303a-87ab-01f4e2cb426d | -16.7361 | -57.42148 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 32c01cc3-2bd5-3e00-8d27-ae83eab31e61 | -16.73589 | -57.42318 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d750f1b4-791f-30c7-b5a3-8a010a70348c | -16.73486 | -57.35748 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b220bce1-b8fb-3d5f-bcbc-6145ba8f4658 | -16.73361 | -57.3639 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e65177ba-8e5d-35d7-84d2-f954ea55b303 | -16.73189 | -57.41775 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4b576689-a518-305b-adfe-4769d77be064 | -16.73152 | -57.42088 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 92840485-23f4-3825-9383-406eaa3881da | -16.73131 | -57.42257 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c0a29bc0-d455-3374-be19-148c083bdce9 | -16.71924 | -57.37019 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| dde951e7-347a-3eea-a23c-02a8b14b9e86 | -16.71465 | -57.36959 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 3b0db5d8-4a16-3e1c-ab4d-25b8f57bb9d0 | -16.71404 | -57.37442 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 9f0bd22e-e47d-303e-835b-93204b641dca | -16.71005 | -57.36897 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| de772072-961e-33cf-9b45-697d286801b0 | -16.70945 | -57.37381 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 47c7a162-3535-34c4-aa01-5d771af0fafe | -16.70885 | -57.37865 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 113ae6a1-ac1a-3635-b4d3-f6508345a1e4 | -16.70366 | -57.38287 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4e4cb3c0-7053-346d-855c-b7f159804820 | -16.70306 | -57.3877 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2ab7694e-8b5e-3f91-bf2c-61628e3463e7 | -16.69907 | -57.38226 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| caa00794-6d17-3f36-a1f7-6568d29edf38 | -16.69847 | -57.38708 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6b05e69e-5de0-3aba-8c73-e31b44c5b4bc | -16.69787 | -57.39191 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f0530820-9a6a-3780-9399-2245279ed2c0 | -16.66439 | -57.24372 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 466edaed-9b01-3808-944f-06bde512f13e | -16.6638 | -57.24864 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 07f35b79-1a53-36c8-885c-a7581af92cc8 | -16.66104 | -55.97327 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c68f8c4f-bdb6-3cc4-9777-b3907a4cfd3a | -16.66033 | -55.97926 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 8048491c-71f2-36ae-ab32-ae07daadc176 | -16.65976 | -57.24309 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7d6fe74f-aa94-3958-b006-ead625111d2a | -16.65917 | -57.24802 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c33d5df1-f84c-39bc-9803-f89c6380b650 | -16.65858 | -57.25294 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1277d6fe-539f-3aaa-9f01-ea8a811e076a | -16.6574 | -55.96065 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 88008160-05ce-37d4-aeee-cb01eae4f127 | -16.65719 | -57.24119 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 03d03dc2-a29c-3885-952a-2d45b43b55ee | -16.65599 | -55.97263 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README149.md)
