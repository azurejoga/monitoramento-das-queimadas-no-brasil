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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d935690e-520e-390c-bcbd-5428fd59af31 | -2.34903 | -49.2544 | 2024-10-14 04:19:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c03bf8a7-a20f-3db9-9a19-961922a85230 | -3.46397 | -50.60716 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c321283-fd7f-3ef2-8010-e83b0ca8e4eb | -3.46325 | -50.61148 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3743e31-1425-3bf9-9bfb-16ad68e76e55 | -3.45878 | -50.61076 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e37df99d-8ef0-3e36-bf89-140bbdfa8229 | -3.48238 | -50.49699 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9014205f-a541-3c7a-a0a6-6831099a8810 | -3.48163 | -50.50151 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b3113a1-e578-354d-86ff-830a13a429f4 | -3.47795 | -50.49628 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cd08b7e8-d828-30db-b907-613275850e64 | -3.47719 | -50.5008 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef73f9cd-778e-3cb4-8470-37186286a183 | -3.4595 | -50.60645 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4821e27d-a9ef-3b40-9207-c9e09a2723e8 | -3.4579 | -50.31742 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85aabd06-8878-3633-b8db-c9f0b7c542ba | -3.45352 | -50.31669 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96f17bd1-88b2-34cb-ad84-23b86a30572b | -3.3773 | -50.34013 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6224416d-0bfb-302f-9a8a-3fb99d7c7c81 | -3.3766 | -50.34446 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5614705f-99f1-3892-8d5a-1c155e3e3275 | -3.37289 | -50.3395 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| be5b6730-b51d-3929-b07a-e203e40414a5 | -3.37219 | -50.34385 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7d3c00e4-f6ba-3e7e-b813-6f16963f6f25 | -3.36989 | -50.33015 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6f03881f-6889-3820-add7-59a93adb86a3 | -3.36546 | -50.32965 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b29107d2-6118-3182-88dc-acaeae1f1304 | -3.36478 | -50.3339 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc9db2d9-87cb-3cbf-bbbf-d3f3b127998b | -3.33684 | -50.31176 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| faa07e60-3723-37e4-82ca-faa7079efee1 | -3.33612 | -50.31612 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d3cd93af-f4c5-3d91-bcad-9396b66da750 | -3.33245 | -50.31103 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3655bfe8-42f5-3dd8-bcc0-b09cda53ab7d | -3.33174 | -50.31536 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0863c08-67e8-33ca-b157-993680bc03e3 | -3.33102 | -50.31978 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1474482-2463-30de-a3f2-d614367b9026 | -3.32735 | -50.31467 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eccea21f-8b08-3b18-8516-44c6bc673331 | -3.32663 | -50.31907 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 381962b8-6152-37d5-9722-9aa8542fec62 | -3.32295 | -50.31403 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19f6fcfc-fd7e-37be-a3c9-d698441eafcd | -3.32223 | -50.31841 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2a25729-cc99-3d0f-a903-c964d7ceed2a | -3.19373 | -50.30345 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaeabff6-1ce5-318f-b143-3793b81461c7 | -3.19302 | -50.30773 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88e0831f-4a60-3cf3-8e86-cdc0cb76afc0 | -3.19231 | -50.31201 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5994f892-f0b3-3c46-b7ca-801481cf7984 | -3.19161 | -50.31626 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7892ec17-cb10-3b43-8ede-09ebe5a222b3 | -3.18632 | -50.45797 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93cf6533-c2ff-3ecf-9fb1-7244f3dbc111 | -3.18562 | -50.46221 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13fff798-3a71-3866-a84a-4bda58073933 | -3.18189 | -50.45721 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 738c9ab9-a20b-35fb-8826-28d68bfd2629 | -3.18118 | -50.46152 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3424ce47-2f16-342d-aa8d-14401b328e44 | -3.17673 | -50.46081 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ae2fbc3-ab1f-3ce0-9511-fba1e5f339c6 | -3.17529 | -50.46954 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9262952b-5b0c-3ba4-83f7-1ea0c0500733 | -3.17229 | -50.46009 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b08d2a4-f12c-3ca9-9a5c-65a08f331642 | -3.17157 | -50.46445 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd068e3d-43fd-327c-8217-7bdf49dd95ee | -3.17084 | -50.46883 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b368b485-c89e-3b59-a0ab-26ea360814c3 | -3.17011 | -50.47321 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 80da05a6-02ca-3f49-9dab-0de49779242c | -3.16939 | -50.47759 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2edea680-3d69-3b25-ad44-b003205417ae | -3.16712 | -50.46374 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a25dbfc-79c8-3aeb-967d-4e6a38bdd2ad | -3.16639 | -50.46812 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec98959e-b91c-3c6d-86ea-781af822de13 | -3.16493 | -50.47689 | 2024-10-14 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa03c7cc-a8d9-369b-b7f5-4a6f37ed0d80 | -3.453 | -49.7327 | 2024-10-14 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef11e45f-c884-3d15-8b64-c37d478b46db | -3.34018 | -49.16318 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bea474e2-cc77-3246-b801-b33566b7f085 | -3.33669 | -49.15895 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ca1c2a5-3143-32c8-8cbe-ea597b27f5bb | -3.33612 | -49.16255 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c44186ae-c7fd-39d5-ba7c-bbcc8954c307 | -3.29614 | -49.10123 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7e45896-4148-3ca5-a008-31bf5d064743 | -3.29267 | -49.09707 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a8529c6-3b98-3f46-bde7-da9cd60d7506 | -3.05968 | -49.37378 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 429b4706-fafe-38b3-b272-0baa11c24ae1 | -3.05555 | -49.37313 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36222b45-980a-3879-89c8-6b384b13c3fb | -3.03272 | -49.54041 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe63c590-69f5-378a-a028-f584de68efe7 | -3.03209 | -49.54427 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d3ad7f6-da1c-3634-9d13-58de737ecca5 | -2.98794 | -49.52551 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8203df36-17b0-34ff-90d0-0ba04c6aa161 | -2.98731 | -49.5293 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6306f3bf-209e-338d-99a7-aaad4cc8a05c | -2.79315 | -49.29703 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec4ec03c-e621-3e89-819e-34a3b8d7a05b | -2.79256 | -49.30077 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcacc78c-2f8a-32b9-8c32-093ed3cce5e5 | -2.79155 | -49.29662 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43621aec-4ab1-3fa9-b089-87a77ba49ab7 | -2.79093 | -49.30035 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d21ab4b7-8beb-330d-92da-cb3ba8934fd2 | -2.78961 | -49.29267 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34d280f8-fb58-389b-9162-f4393242c3a8 | -2.78902 | -49.29638 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 715c1ec6-527e-31d4-850c-10730862d2d1 | -2.78843 | -49.30011 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eb43f53-543e-3b33-b1a7-deb5e042d94f | -2.78761 | -49.42347 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc0f0aec-016a-35b8-8553-81a3eb435480 | -2.78548 | -49.29202 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a92c78e-86b4-30e5-8c32-4ffe4321b3dd | -2.78489 | -49.29573 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dd8a2f9-6111-3cd2-b104-70769053379a | -2.78429 | -49.29946 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c40a3264-8aa8-3a11-9f20-b5c9960e327e | -2.78344 | -49.42279 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b41b3f7e-773a-31c7-96bd-a011fa7bbd96 | -2.77354 | -49.36724 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d1b16bc-b7c6-3619-abff-ca61cb28c3fa | -2.73046 | -49.16209 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b05b164-6ee6-34ef-9ab3-9d1a30722fb7 | -4.48704 | -50.46489 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eef61e5b-1794-3a17-b33d-b1cc8a42a992 | -4.48634 | -50.46909 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcbf92aa-385d-3246-9752-ccc6216651b0 | -4.43429 | -50.53846 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c120da75-7768-30d6-a603-be91b1dce2a7 | -4.43356 | -50.54274 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba6c766d-e8a8-346b-8828-83ce2e6bbb60 | -4.42963 | -49.73485 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa5b0a39-b53e-339b-b7f3-9d9b07ec50a0 | -4.40873 | -49.75842 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5956feb0-b8d3-37ea-9496-68dee5eea7b8 | -4.40812 | -49.76217 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce61863a-7ee9-3a28-a260-bdfce3edcc00 | -4.40396 | -49.76147 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aa84070-8a50-36d9-9494-b696de776622 | -4.40334 | -49.76525 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e2e43f7-452c-386f-8fe5-3475cbafa6f9 | -4.36361 | -50.80068 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19a935db-2800-39ac-b121-0d34a0a7c127 | -4.36289 | -50.8051 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd18cacb-4260-3316-b125-3168d0148db6 | -4.34865 | -50.50873 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a021e0b-e730-386f-bdb1-d5e4d8bb712c | -4.34793 | -50.51303 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 071d2916-ed84-32a8-ace5-26d33ab7bfb5 | -4.34355 | -50.51231 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f759eed-0d38-339a-8653-8f5b91b7ff25 | -4.32803 | -50.46663 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94b037a2-3c23-3413-ba47-1f16d00a2d10 | -4.32367 | -50.46586 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56b9dd97-0f6b-3460-9609-2d774e3f39a7 | -4.26985 | -50.60184 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b76e71f-2a3c-3783-a4a6-cfdc6b0399b4 | -4.26913 | -50.60618 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b298c1a2-98a3-317e-b147-34e22aa85fd6 | -3.69845 | -50.1182 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95fd5473-df0e-321c-a3fc-cdab045bc993 | -3.69779 | -50.12224 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b8cc282-74a6-3677-a70c-62f6892ffcfb | -3.69414 | -50.11752 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fa85161-2311-368f-a017-eea5a085cd1b | -3.69348 | -50.12154 | 2024-10-14 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62d106c5-cc05-3df3-9c2f-7c5a506918ff | -3.64104 | -49.91158 | 2024-10-14 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e18b68e-a4c9-3d6c-93ac-37d59d95e22c | -4.64603 | -50.62393 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52ddbbae-1fbb-3002-b014-a310c74f0d6a | -4.64555 | -50.62411 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c812f71-f27a-3aae-897c-eef44e8aa30d | -4.64166 | -50.62314 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5599099a-812a-32f4-ad32-a6954a165933 | -4.43341 | -50.53982 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a75cc8fd-9be5-350e-994d-dbbb084616de | -4.36662 | -50.81031 | 2024-10-14 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c1873e8-5ed6-3146-804e-89cc7d5fcecd | -6.21492 | -50.89717 | 2024-10-14 04:19:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README50.md)
