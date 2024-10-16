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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c77ddacf-231a-37e9-ac94-6defbaeba63e | -9.60524 | -68.55113 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36912da7-38b5-359f-9383-988d3fa2db07 | -9.59892 | -68.54704 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cdbbc0b-d542-3c61-a058-6061645e7112 | -9.59751 | -68.5462 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c92a6820-e3d3-37a0-bb3c-beca1018c4df | -9.59231 | -67.46262 | 2024-10-16 06:14:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b0e996e-73ae-305d-b6bc-9ca71736a501 | -9.59195 | -68.50786 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dc5c428-3a98-3d44-a839-c31c82859411 | -9.58782 | -68.50724 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c26b672-abdb-390a-8798-fc5d7f90dc5d | -9.54345 | -68.49329 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5debb64b-191e-36d2-ac85-2246990b51ac | -9.48441 | -68.50423 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc130046-cf77-39c2-b505-5c0a17a44f4e | -9.47587 | -68.91397 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2012ac1f-9e14-3c96-8dc4-bcf8135cb2a6 | -9.47166 | -68.47562 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3cc439b-bac5-30e0-9c8a-53543c76481b | -9.46593 | -68.48627 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4ad53d2-7fa4-3d5e-993f-37787e6b565f | -9.45951 | -68.53126 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9135e93e-b051-321c-bc20-a4f4fe7e86ae | -10.63635 | -69.01382 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eed9ef8-77f4-303c-be29-1c5732f0f8a5 | -10.491 | -69.04095 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c93453ac-4f18-3ffb-91b5-0a796ecbbe55 | -10.48695 | -69.0404 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1521bbf-38f4-3c93-8ce0-d044ca5755a7 | -10.82854 | -68.27679 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2c56143-ec1e-3c79-970a-7012c6b71096 | -10.76266 | -68.31276 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1277576-496f-36e8-b5b9-da8adc189630 | -10.7584 | -68.31219 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bca4823-d3f2-36ff-a6f7-489715d0508d | -10.63021 | -67.83841 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6686191e-522b-35cb-b346-e52ae45183e9 | -10.62962 | -67.84267 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 469e0c96-2c85-31b7-8502-21679efd591d | -10.62582 | -67.83781 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53122f97-c1b0-30ee-9c83-fcf333280862 | -10.62524 | -67.84208 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bacf7d01-99d6-3466-b52b-2be1b6d409a6 | -10.62085 | -67.84148 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 612e239d-d011-399b-9beb-e77acc815af2 | -10.61647 | -67.84084 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d814f793-1852-396c-a834-7c6a6e88af45 | -10.57681 | -67.76969 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc19f7c4-8cc0-332a-bad4-182bc9ce5f02 | -10.57359 | -67.76222 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 300d86b3-f7c6-3327-a7cf-8c43e6b987ef | -10.57357 | -67.76032 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c0f04f0-3874-3dcf-8023-0d8e6631a61e | -10.57242 | -67.769 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1a01d7-ed0b-3915-a310-7bf1089ab970 | -10.57237 | -67.77089 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd21f2b5-ef40-33df-982d-f32af269521f | -10.55359 | -67.77685 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 626d878f-e252-3ffe-8e4e-f2bd22b33e92 | -10.53558 | -67.80979 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 035967f4-41ee-3bdd-a9fb-3f7e25091416 | -10.40375 | -67.91894 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b38d8e4f-e665-3068-8e81-3bf1450f4595 | -10.38866 | -67.96406 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0d91ff4-6062-3ad9-94d8-20af37244f1c | -10.38374 | -67.90324 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0023109-9008-39fc-bbd4-6266f9cb89a0 | -10.38317 | -67.90743 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba5f0952-9b28-3898-9738-d789f98db687 | -10.3455 | -67.92384 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf9e8496-77e2-309b-a4a0-2b93563506c6 | -10.34493 | -67.92806 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71b04e2f-b4ac-3e40-8450-ba6f707b4c2a | -10.33492 | -67.95797 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a595229b-1e91-3ebe-b78d-898ca6a6ba99 | -10.33232 | -67.95612 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5faa17d6-338d-3636-ac3d-ba4e4e4a791a | -10.32882 | -67.96983 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae3b3716-b158-396e-96a3-4875d950bf56 | -10.32631 | -67.96799 | 2024-10-16 06:14:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 313dbb45-6c73-3969-9169-8263d49d37f3 | -10.28293 | -68.01434 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4af7d5f-4262-374d-ad5a-b32bc5aa4e1c | -10.18314 | -67.92467 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f28df5d-2f1e-39c2-8edc-d1114f8347d9 | -10.112 | -68.31153 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca261210-4b18-3d2e-97b3-575d56c03937 | -10.0799 | -68.2948 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 839846b2-f31e-32b2-93f5-3c8e6f3c4eb9 | -10.07498 | -68.36219 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a661ca6-cea6-3be9-a239-67bf7500742d | -10.07392 | -68.06205 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f2cef7b-71ae-3a38-9c18-42ec2626ba7d | -10.07078 | -68.36159 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3fcd056-dc99-3e58-986d-360ac4ef9ee4 | -10.06963 | -68.06143 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5834b743-ab72-38bb-ac77-2b7f9bf01d2e | -10.83152 | -68.27966 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46bfda8e-f3f4-33dd-97a4-d2accdab0fd4 | -10.82174 | -68.35242 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b82d97e-1cb4-3cce-a982-20c994a16ba2 | -10.78867 | -68.81351 | 2024-10-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 003467ac-ee05-36a5-b920-44e47a2ff548 | -10.76124 | -68.66035 | 2024-10-16 06:14:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61737ecf-87da-3de2-b7aa-da583aab27cf | -10.71686 | -68.55182 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d200762-3518-3d0f-9089-12d45a4a2227 | -10.70637 | -68.56605 | 2024-10-16 06:14:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b86ac0a-0e26-30e0-bb13-7c999e3b36cf | -10.66591 | -68.57287 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9934610-3a05-32e2-8559-7b430ae5317a | -10.66536 | -68.57674 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 095acf28-7fe2-3fc2-8a6a-58823ef6abaf | -10.66119 | -68.57611 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6e2d44b-0598-357a-ada0-200ceebe5771 | -10.66064 | -68.57999 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eadb73a4-389b-329c-9a70-ba359b9af24b | -10.58419 | -68.7933 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1a5ad9f-ddfe-3837-8136-2149930fb3d4 | -10.57974 | -68.61161 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 979e519e-b29e-3228-96ef-9a66f60940d9 | -10.57908 | -68.76973 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c625efe9-7275-386b-bd1c-5f4250a1abc5 | -10.57497 | -68.7691 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86458b36-8928-3b98-bfc2-4f95080fd0f3 | -10.57445 | -68.77283 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75aa6d3b-1f37-3f80-9168-be24a6470fa1 | -10.55854 | -68.82734 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e29ed79-f7c4-3810-8dc2-5b9583f2be4c | -10.55723 | -68.57761 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9185af14-df60-3729-a2da-d04ac578e491 | -10.51346 | -68.85516 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d197f17a-da06-35de-a597-35a0921eb9be | -10.50319 | -68.86867 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c41bd5d5-7fa0-350b-82ab-79c2b2406871 | -10.19732 | -68.31918 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5db99f4-a466-3c99-8fea-a437d39a7b90 | -10.1931 | -68.31857 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f6a0baf-76a1-384c-a45e-1e016a18140a | -10.11372 | -68.39148 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a92feff3-3b28-3ce4-8180-f88e84e467ec | -10.88434 | -68.21196 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e26aa12-893f-38b3-81a0-f05f0a94f57f | -10.95612 | -68.24986 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffbfad58-cecd-3e06-95cd-90813753be86 | -10.89874 | -68.29728 | 2024-10-16 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72e39ac2-ff4a-34c6-86b5-5bae188abce8 | -12.1348 | -64.7361 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 390c8fc1-bd82-35a2-be7f-f7cc6d9ff371 | -11.94435 | -64.87524 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93ed6fb6-7db6-3903-bce6-1a21febeeb62 | -11.94391 | -64.87885 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c89fc554-3133-3b23-a379-831c8662fcb2 | -11.9393 | -64.87108 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06bad10e-5029-3315-b2ab-ed8df0a17ec4 | -11.93886 | -64.87469 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc215347-ad78-33e5-be22-89fde7f73cd4 | -11.7202 | -65.2291 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f76b389-ba6f-3fc8-8147-6d45cd7945dc | -11.71978 | -65.23244 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ca294d1-b0dc-3233-84a6-3d8584672c47 | -11.71488 | -65.22839 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66f3c437-19c5-31d6-9f3b-59fe7ed948b0 | -11.70955 | -65.22769 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a458cfff-d697-30c6-9976-47c6917ca956 | -11.70913 | -65.23106 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fddc6002-63bd-33e1-b9e0-a69ff6b9af5a | -11.70464 | -65.22367 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06b36014-3f0c-39ec-b1a5-94f2b73f9f9c | -11.70422 | -65.22701 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecf4f4db-13c8-3c07-afd7-98fd23cc8d09 | -11.7038 | -65.23036 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cd0947f-2b77-30c7-8b54-c2d9f9a2a981 | -11.70338 | -65.23375 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee8dc707-df5a-3cbe-8bd4-3425c603b26d | -11.70296 | -65.23714 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12787152-0b90-338b-a33a-df72f0db948c | -11.69932 | -65.22295 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 844b5683-f742-3030-a8eb-c99bbdc62150 | -11.6989 | -65.22632 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9185eb7-3b1b-3919-a90e-a01cc5e3c16f | -11.69848 | -65.22969 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39529a66-b8b7-3f80-acdd-369cd63c0a08 | -11.69806 | -65.23307 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 356b5cad-d438-33bd-bd75-399637a3ffb7 | -11.69722 | -65.23981 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 313e075b-ba50-3553-a952-fde4b40113e0 | -11.6968 | -65.24318 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d4894d1-f64d-359c-a3f0-82df5f1e95b1 | -11.69483 | -65.21552 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eea7c21-a23e-3da8-9c50-95c07e5e56bb | -11.68991 | -65.21148 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e96f4f88-a160-3189-aea4-5004a4ee765d | -11.68949 | -65.21484 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b4996de-64eb-3fcb-b67d-1bd3ea93168a | -11.68908 | -65.21822 | 2024-10-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e75d5aaa-1cc4-3f04-ab45-612fd7f9298d | -9.14979 | -68.87074 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README74.md)
