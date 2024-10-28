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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8350f6-c6b7-3b40-b7b0-a296e647c2a8 | -4.0959 | -53.94598 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52615b05-5d8b-3f00-a8e3-6814cf6cd639 | -4.09283 | -53.93691 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f13cabfe-641c-35eb-955e-c7bed75ee389 | -4.09123 | -54.18182 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05a82ad1-d264-3a8f-9306-b995c4d349ee | -4.03318 | -54.28051 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc89d4cb-9fde-31c9-95c3-45308589396f | -3.81302 | -54.11842 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6760dc37-3c44-3973-89ed-df35b97c46f9 | -3.81177 | -54.11784 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 203b1391-fe48-3d85-bdf4-6c686ce7054a | -3.67332 | -54.29644 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4c59518-e1ff-3bb7-8b0d-0075ac5e4410 | -3.66913 | -54.29581 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ec8983e-c7c9-3584-a8ff-3c1c9feec375 | -3.66883 | -54.21366 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea1d8353-29ec-3a94-8c2c-f10de1851d07 | -3.66824 | -54.21756 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da4bb091-2f78-34b3-ac48-bcbf59c5d28e | -4.50812 | -54.96085 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c32ae5d-5e55-3607-b8c0-c690771c4680 | -4.50406 | -54.96022 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91ed9fde-dd82-3931-825b-f3a2a6dd12b2 | -4.46475 | -55.11205 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0390eac-a052-390b-b56d-b028e87216fc | -4.46073 | -55.11148 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef3eed7e-3f4e-3ded-9c13-c7a922ed1a2b | -4.42159 | -55.09847 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bcd5181-037b-3345-901a-74aa526f2ad0 | -4.42142 | -55.09161 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 685b834f-30b8-3f42-bf75-9625a52ffb16 | -4.42109 | -55.10191 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03e1212d-f2d9-39fd-98c3-a25a206a2bed | -4.42035 | -55.09854 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52a30ff0-8331-3330-9262-ca6c60593e27 | -4.42008 | -55.10879 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62441ee9-0afc-31f7-906d-746e9bf18808 | -4.41982 | -55.10197 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d74daf25-6f39-3754-a92e-d4dfbae363a8 | -4.41876 | -55.10885 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c3252a2-01e1-3ad9-8c95-b8eb1c958448 | -4.41633 | -55.09797 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef51d006-915d-3221-9bcd-2d7f86868ec3 | -4.29665 | -55.12333 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f021e5b9-364e-38a4-8d02-917e61f1da45 | -4.29267 | -55.12263 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cec6810-27f9-3bf4-bf46-544115dac86e | -4.12732 | -54.84894 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8f9cfbe-fbac-3cc6-8c45-0cbb7b9d0dab | -4.01521 | -54.82098 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d91fe24-2858-3bc3-923d-493aaff5980a | -3.98911 | -54.54897 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9472ced-ecd1-3606-a88f-0ac5956b75cc | -3.98855 | -54.55273 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77b7f3c2-4747-39b6-9eb3-0cda55237e75 | -3.92581 | -54.50936 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24a8a1f3-ef84-339d-9d44-8e91148c644d | -3.85394 | -54.76411 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36484eac-aa7c-3655-9f94-db7571773d66 | -3.84985 | -54.76358 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5620b7ae-fa58-389e-8985-58c8d971adee | -3.72148 | -54.4644 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae7a1acd-0a90-36d2-9462-d1cbb1e4e5e9 | -3.72089 | -54.46826 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1589f910-b8fc-373f-9eff-777abf1601cf | -3.63854 | -54.68045 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f24279e0-eacb-3580-be98-9c0498eb8655 | -3.638 | -54.6841 | 2024-10-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41b22977-e736-3dc4-950d-a3c7cc4f8094 | -4.22278 | -55.31486 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d850fe4-56dc-332e-a060-048a46a86028 | -3.63059 | -55.50678 | 2024-10-28 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a13e2c48-a171-344e-a53e-9abfd07a8928 | -2.36308 | -56.51998 | 2024-10-28 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c87cc79-4cf2-3dd0-acb8-37a7462f3383 | -2.28017 | -56.43564 | 2024-10-28 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b145a855-aaab-3195-8b24-9a4ff6c03460 | -4.71294 | -55.6912 | 2024-10-28 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6db5761-a08a-3dc7-ae32-aeb409652083 | -4.48816 | -56.10738 | 2024-10-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4388b9d-cf9c-33fe-9d2b-faf20810b081 | -4.48795 | -56.1089 | 2024-10-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4379910-2f61-38d2-9d32-e25dc90191db | -4.39348 | -56.32415 | 2024-10-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f47dd1c3-92ef-33ef-897c-dbf9d8622b60 | -4.39281 | -56.32855 | 2024-10-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b89adde5-44af-37da-b958-b8969f4e748f | -4.38975 | -56.32361 | 2024-10-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 055d99da-409c-3fcb-a354-c804c1b81b1f | -4.21857 | -55.50158 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c73de0a-e90f-3367-beee-96bd3e8ef971 | -4.21467 | -55.50094 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 450e8c6f-0098-334b-bcd3-c5d9b9bddd00 | -4.11649 | -56.19365 | 2024-10-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78f849b8-28ad-30ad-bfe3-4a5740782674 | -4.1158 | -56.19815 | 2024-10-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf87aee9-16cc-3293-9787-df9a0f75914d | -4.08769 | -55.87936 | 2024-10-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e10311af-8d12-3cd2-9301-7a56b0841ffe | -4.06413 | -55.57061 | 2024-10-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f73edb2b-a290-3de3-ae10-22723deb230f | -4.03826 | -56.28152 | 2024-10-28 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5206f062-250f-3868-bb16-3188e686e75a | -3.9018 | -55.88217 | 2024-10-28 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c96be41d-cd2c-3322-b7de-4538db5eda93 | -3.77538 | -55.97756 | 2024-10-28 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f68c964-546f-3e4e-8322-bf74923e26c3 | -3.72628 | -55.48353 | 2024-10-28 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99229f0c-13bb-3d29-92c8-e9050f2972f5 | -3.72573 | -55.4814 | 2024-10-28 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b11d0216-a601-3407-97b5-46e27c6ce9e6 | -2.05956 | -56.86638 | 2024-10-28 05:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 345bc5d1-cd56-36dd-a5ab-d659fbeb7a17 | -2.05895 | -56.87029 | 2024-10-28 05:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd3106b2-4d38-39e8-86cf-c972cc6d3233 | -2.05603 | -56.86584 | 2024-10-28 05:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c07d741b-7c14-3161-8d05-961e925ff148 | -2.05543 | -56.86975 | 2024-10-28 05:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c03e64a-7d7c-30d2-84c6-5e3582fdc6a8 | -3.16773 | -57.03753 | 2024-10-28 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fea28e5-5d78-38e2-b0aa-018e7081e19c | -3.16419 | -57.03698 | 2024-10-28 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f2b1aec-b30e-3556-aacb-22f8424a4aff | -3.15108 | -57.07545 | 2024-10-28 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f252639-6899-34a3-b5b5-b298167eec3d | -3.14809 | -57.07619 | 2024-10-28 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b06a95d4-ea7e-3aa8-9f1e-bf46b2a467d4 | -3.02156 | -57.54251 | 2024-10-28 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37d50834-2bd2-3915-ad11-3276917595a4 | -2.89229 | -57.67682 | 2024-10-28 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18978a34-891c-3efd-a9ac-f90d2b24fb79 | -2.88827 | -57.68001 | 2024-10-28 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd133ad-cb49-325e-aed1-aa710aa5db86 | -2.69277 | -58.08618 | 2024-10-28 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b6f62950-f0e6-37b4-a1c1-df8bfc14d8fb | -2.68938 | -58.08567 | 2024-10-28 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4beabe5c-0a09-30fc-b710-d8fe460c0ab0 | -2.68598 | -58.08516 | 2024-10-28 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9064ead2-25cc-30c2-973b-598bba6bda4a | -2.59558 | -57.56756 | 2024-10-28 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bca33667-4a9f-3cca-96cf-4ef9aebee669 | -2.40539 | -57.89016 | 2024-10-28 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3885dba-8077-3e4f-98b2-546f1e5f546f | -2.33857 | -57.13326 | 2024-10-28 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e733fe-4d51-3f51-bdf4-3479f2002dfe | -2.66921 | -59.42957 | 2024-10-28 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13974fda-1dd7-35aa-bdf8-ac3a12784047 | -3.78051 | -58.5824 | 2024-10-28 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe6c5a0-6031-3625-9ae0-aaa11f1696e2 | -11.50434 | -61.03205 | 2024-10-28 05:23:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d772d7d-3e41-305b-8062-291f9cf30b74 | -2.20471 | -60.16694 | 2024-10-28 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4802d4c-e5d3-3400-be79-30da7984517c | -2.20805 | -60.16747 | 2024-10-28 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7299a8b-99c7-3853-b9f5-0d734eee2450 | -7.64316 | -63.45347 | 2024-10-28 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdd8af27-56e7-398b-8bb8-8c6f005f6470 | -7.64091 | -63.44489 | 2024-10-28 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee254412-c797-320a-b541-3b35ec90eed8 | -7.64026 | -63.44889 | 2024-10-28 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a993b6a-7318-3c7c-9609-f24b89d88f64 | -7.63961 | -63.4529 | 2024-10-28 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b297354-72aa-3e62-9d03-9f17b0b8363e | -2.59978 | -51.77703 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9e23edcf-7ec7-3bee-83ef-a094c0e3089b | -3.51616 | -45.79996 | 2024-10-28 05:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c115d7a8-52fd-3763-b253-75cef1376372 | -3.50997 | -45.79152 | 2024-10-28 05:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 124cbe8d-8a36-3b76-bbd7-f6aa7992b75d | -3.50888 | -45.79898 | 2024-10-28 05:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 916f1c83-9cdc-3df9-9f73-c7749bc94fb5 | -3.50782 | -45.80632 | 2024-10-28 05:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| d9ee07f0-0dbf-3a1d-8d57-087ee0cba963 | -3.50161 | -45.79798 | 2024-10-28 05:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| abb7b548-0c02-3164-8ecf-f7b5da08b90a | -5.2322 | -46.21655 | 2024-10-28 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7360b87-d1b7-32c5-96af-d909643c662c | -5.23111 | -46.2245 | 2024-10-28 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a1f430fc-8a93-33fd-96b3-c33b6ee42730 | -5.22495 | -46.21555 | 2024-10-28 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 022d2727-a2fb-3a79-989a-e7ead7a5e9d2 | -5.22384 | -46.2236 | 2024-10-28 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 15c5b285-7d5e-3b77-9db2-84e2b1590687 | -3.40504 | -46.3138 | 2024-10-28 05:23:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41f74a13-7752-34d8-9dea-65f6ed313e80 | -3.40408 | -46.32042 | 2024-10-28 05:23:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e7359b7-7b59-3694-88ab-46ed82c8a3e6 | -4.7734 | -46.39462 | 2024-10-28 05:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af264c07-045c-3819-be28-01cdf239595f | -4.77252 | -46.40091 | 2024-10-28 05:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 12acd615-e9d6-3c44-817a-bc517f4ad197 | -4.76635 | -46.39296 | 2024-10-28 05:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b7f339c2-3982-3b05-9d65-1be38f5caf9e | -4.76544 | -46.39952 | 2024-10-28 05:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b85acea0-8c08-37bd-8067-d631fe2ed443 | -4.73797 | -46.80117 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a23d2a41-2fa3-3765-8ab7-bd5178ca7f28 | -4.68191 | -46.66018 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |


[Clique aqui para ver as próximas entradas](README78.md)
