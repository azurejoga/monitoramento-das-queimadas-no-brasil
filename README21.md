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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2e4df2a-341c-38c2-879b-3c6977e69967 | -3.12022 | -53.12358 | 2024-10-31 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42b99d28-1db2-3536-bec6-bdaca2894642 | -2.86772 | -53.32475 | 2024-10-31 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dd9249b9-1b0e-3b99-8c48-da833209e1cc | -2.23963 | -53.72617 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef5f3be-6a0f-3ae1-a2af-586283ca6b09 | -2.20321 | -53.72338 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bb81cdb-10de-3272-ac15-026c5566d198 | -2.20272 | -53.72638 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 095455d6-b5d8-3cd5-9123-733f7a2a981d | -2.19857 | -53.71962 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae5d2c40-3e83-3fcb-a480-c2b86012186b | -2.19807 | -53.72261 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6afacb2b-1c0b-3b3d-bade-4b9882226e0e | -2.19757 | -53.72561 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ec19999-d202-318e-930f-9aa6c81869a4 | -2.19439 | -53.58741 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e5895f2-524d-33cd-a6a7-3a19efcfce10 | -2.19391 | -53.71597 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d4e5c9c-6748-37ee-8864-cf49d7c0c9eb | -2.19387 | -53.59049 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 313e3353-f05e-3eee-bd94-1b4eac0e99fb | -2.19342 | -53.71888 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e17f48af-67f9-32bb-8ff1-29e349617bca | -2.19132 | -53.58973 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e92af462-7e39-346a-93ef-8b22b12a8f9c | -2.16317 | -53.66729 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2c62d22-24d3-3f1c-a7a2-232319be83bb | -2.15755 | -53.66958 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ded5bd2-82a6-36fc-b78d-e9776e25dc46 | -1.2076 | -53.77792 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c96fb476-f887-36ce-918a-11bdd3b26295 | -1.20751 | -53.77842 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3443627a-4b6f-334c-9cc1-9f2c8d5c8bd0 | -1.2071 | -53.78106 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0362d5da-4522-388e-89b0-308a9dbb28c5 | -1.20699 | -53.78154 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da9a119b-fd65-3208-830a-b2ae71183310 | -1.20238 | -53.77697 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5ca84ea-ba72-3543-9f1f-f50713c14048 | -1.20229 | -53.77747 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddd6fcfc-4e2e-349e-8bef-6f1f393baba1 | -1.16453 | -53.38592 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec8c4052-8bae-3a82-848a-13071db2b50b | -1.16404 | -53.38887 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4582190a-3689-33cc-86ef-de0bc5d7ef2b | -1.15385 | -53.38723 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f20c468-dee6-3e63-a9b8-d18f664e0371 | -1.15335 | -53.39025 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e00dc4c1-61ac-385d-8030-3b9f4497b672 | -1.15152 | -53.38663 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b53583a-2746-3010-883e-576a8ec94dc9 | -1.15106 | -53.3896 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac988b27-664a-30a2-be8c-f06e06d12d08 | -1.0931 | -53.65644 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a072cb3b-2a26-361d-9d8d-bd316729f24e | -1.08844 | -53.65222 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18905c59-305f-30de-a76c-a3bde8942f4d | -1.08796 | -53.65527 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d71a6d0-d4e9-35d3-9b04-f678e1e5488a | -1.08747 | -53.65836 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04ce28c8-475b-39e0-bdd8-d572fb9c3c67 | -1.08327 | -53.65122 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5f161bd-83e1-3b47-9ab9-bdcebcaaec9b | -1.0828 | -53.65416 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff463406-b849-3fe6-84e5-ad57b33da5d8 | -1.08232 | -53.6572 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a368b68a-3c0f-3c6f-95b9-15fd65a3d876 | -1.06665 | -53.65508 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0dbab80c-1b74-347f-a8e6-693534b9218b | -1.06618 | -53.65802 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4685b668-e3b3-3dba-a459-bcaa0656676a | -1.0657 | -53.66101 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f69fae3-d36a-39ab-98e0-3b75af1e033c | -1.0383 | -53.73155 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72b1a937-74c0-3a36-99c9-11306d822401 | -1.03298 | -53.73129 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8debdb8-cd88-3cc5-8ee9-aa067463d94c | -0.88413 | -53.68954 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5278cbe-d27c-3da1-8bc6-7b3d3663fa83 | -0.87883 | -53.68915 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a508f69-810b-35fa-99ea-be1037994d1d | -2.31653 | -53.97978 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afce9216-cd07-3fd8-b3de-fd450f104bc2 | -2.31602 | -53.98293 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abe6c8d4-448b-38db-b927-3ba39e4721fe | -2.27704 | -53.78862 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b0c613ba-af0a-3bd9-a945-53800e230a63 | -2.27379 | -53.78753 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 946cabf1-6f9f-3b64-b9f1-ef28356f7588 | -2.27187 | -53.78786 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 353dc8df-2127-31b0-addb-27e12e95eb13 | -2.24525 | -53.724 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 894e2b11-e19a-30a8-91ae-73e63d8ff30f | -3.07975 | -54.16584 | 2024-10-31 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c7b402-189f-3a0e-8390-5fdef462134e | -3.07921 | -54.16668 | 2024-10-31 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6349107d-45fe-3469-99ff-e051bccf3aab | -3.074 | -54.16574 | 2024-10-31 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aab29d9-dfdd-36c3-9549-ea1594e06ec2 | -3.0683 | -54.16787 | 2024-10-31 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ce9a815-865b-38b4-aa8a-77bd778f165a | -2.86852 | -54.11103 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf24d2a7-c99a-3808-ac50-4754ab75f302 | -3.07455 | -54.16491 | 2024-10-31 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fd084bb-85b9-3b01-ac98-959d06e0e63d | -3.07351 | -54.16881 | 2024-10-31 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d55c8fc2-403c-3b52-9c78-6311dacbfe74 | -3.06883 | -54.16703 | 2024-10-31 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9b15d74-5ccb-314b-a584-9ebca9cdcd7c | -2.86903 | -54.10789 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a997b01-b5ce-35e8-ba77-7b2321f4420a | -2.48273 | -54.04637 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f499a875-e983-3692-826c-d2eec955f905 | -2.35511 | -56.50864 | 2024-10-31 04:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c4fae58-eb9d-3fa7-8cbd-78635ad0aff7 | 1.67341 | -55.81027 | 2024-10-31 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 383a38c4-0d69-3ba0-971b-e151ccb9b964 | 1.66717 | -55.81131 | 2024-10-31 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 66b195a9-afaf-330e-b780-49eb6b0011d0 | -8.39348 | -35.02543 | 2024-10-31 04:25:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b22c1cfe-b64b-3b53-bc99-49bebb079060 | -8.38718 | -35.02466 | 2024-10-31 04:25:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 24da4103-8ced-3f72-8b28-475926cf99a7 | -9.74974 | -36.09105 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6fbb224e-d56b-3732-b27c-49dae438305a | -9.74374 | -36.09044 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d5d414ac-16e0-3c69-ac38-1dbf9048e5ce | -9.74318 | -36.09486 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 34de4bf9-f0d0-3cb2-8427-6add6a4774de | -9.73831 | -36.08522 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 1ac9fb1c-383e-3473-a670-f532c67a54cb | -9.73776 | -36.08965 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 6d73992c-81a3-3dd6-a57d-82cfb571de23 | -9.7372 | -36.09409 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 05ce5665-b0cc-3151-a614-402d923f93eb | -9.73232 | -36.08447 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 67168cc8-ad8d-38f8-a2f6-b2a49ed6f665 | -9.73177 | -36.08888 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ec4ea8f9-3eeb-3c8c-8862-0cde2a4faa91 | -9.72634 | -36.0837 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 98ab865e-7152-3a1b-9acb-5d80e094514f | -9.72579 | -36.08812 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| dcc5a651-77af-39f5-896d-2e3c5d797527 | -11.70355 | -37.54468 | 2024-10-31 04:25:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 075fde01-ff6e-3233-8c47-f8a360b7b548 | -11.70308 | -37.54842 | 2024-10-31 04:25:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 809e3547-600e-3c81-86ef-82c18123aa4d | -11.70262 | -37.55214 | 2024-10-31 04:25:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 93cfc7a2-3d56-3545-9944-d48183546103 | -7.606 | -38.85531 | 2024-10-31 04:25:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 99a97adf-f047-30e9-a3c6-2e2f472151a6 | -7.56675 | -38.74836 | 2024-10-31 04:25:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 02444e58-56c8-3ba5-a1d4-b76c64d29783 | -7.56601 | -38.75368 | 2024-10-31 04:25:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 55954f51-ca25-3c0c-aace-cc5dd554b16d | -7.56385 | -38.76935 | 2024-10-31 04:25:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 711089f9-8d62-3b7a-9db6-1693a6d81252 | -7.55974 | -38.76331 | 2024-10-31 04:25:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee433ee9-32a0-3f82-9933-7e59d7a7f36e | -7.55902 | -38.76852 | 2024-10-31 04:25:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f43b1693-3be0-3754-bfe0-8bf278243341 | -7.25941 | -38.93314 | 2024-10-31 04:25:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a55fd78-1e3f-3190-93a6-5b4dafe31b0f | -6.68151 | -37.46652 | 2024-10-31 04:25:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a6a0808f-27d8-351e-b2d1-bbf61d66b49c | -6.68103 | -37.46995 | 2024-10-31 04:25:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a7cc03a-68e8-3581-84e4-a14aa20884fc | -6.67633 | -37.4654 | 2024-10-31 04:25:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5db2ed1b-448d-30c8-9975-e1b7b887046c | -7.06767 | -39.98476 | 2024-10-31 04:25:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 249e9d77-95b2-3660-b43b-f91ac3656da7 | -7.06706 | -39.98903 | 2024-10-31 04:25:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c678840d-72f7-347e-aa63-55ebe7526708 | -6.96767 | -39.83506 | 2024-10-31 04:25:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 137c7b5a-e7b1-395b-a01f-d9801b980187 | -6.96319 | -39.83458 | 2024-10-31 04:25:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 081b5287-84e8-3ce1-b966-a1eab7dd8a65 | -6.65628 | -39.26903 | 2024-10-31 04:25:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f2f5713-1806-30d5-a709-c4a9d46f67a5 | -7.99104 | -39.94362 | 2024-10-31 04:25:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 44557874-f612-3db8-8837-4055d91521d3 | -11.88648 | -40.95955 | 2024-10-31 04:25:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 265d4555-6a55-3fca-8f45-03d1730df216 | -11.88204 | -40.95896 | 2024-10-31 04:25:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b38213b5-b394-35cd-8ef3-24a137630aaa | -12.40432 | -41.42917 | 2024-10-31 04:25:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a84f6c78-3559-3637-bdd8-a2fa4702d71c | -5.61287 | -41.71417 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8e3456cf-1158-3616-9205-7e7ad47007fa | -5.6083 | -41.71836 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20e00df6-1347-3855-844b-f64ccf80e06b | -5.60444 | -41.71777 | 2024-10-31 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95343334-125d-3c1b-a4ab-4faa9b9ad971 | -7.31076 | -42.18715 | 2024-10-31 04:25:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7b47986-6eae-34b6-9086-e9db1770b085 | -7.31005 | -42.19194 | 2024-10-31 04:25:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e0833035-231d-32ad-ac78-3645ddc897c8 | -10.1189 | -42.40227 | 2024-10-31 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README22.md)
