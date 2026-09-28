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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c4b0e76-ea1a-370e-9da2-cb8003c78338 | -3.23696 | -50.57703 | 2026-09-28 16:28:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5e9795f7-43f9-3a3b-a022-2dc3be223f96 | -1.58517 | -50.2548 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5dbc255c-8929-3459-b82d-e3e7c56699af | -1.43814 | -48.89673 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 1eb51072-d991-31d0-a6ff-0da688075a32 | -1.42279 | -51.41324 | 2026-09-28 16:28:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 65942237-78df-3a49-b657-51bf16381fad | -3.20653 | -51.03772 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e25da8fa-c1ba-3107-9410-8a818fd95f72 | -4.25838 | -51.04611 | 2026-09-28 16:28:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2d526396-8a70-3e4c-86f6-f3cfc3bd6f44 | -1.76419 | -53.76169 | 2026-09-28 16:28:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efcfd516-1d53-3b55-b08d-f63273b281ed | -1.48315 | -48.92229 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a91f1745-9716-3ae4-977a-133e492c010f | -3.51222 | -50.31491 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 260fc0d7-1c01-3207-a39d-8011b036c838 | -2.97079 | -43.7215 | 2026-09-28 16:28:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c9d6edf7-1483-3c91-bf93-98fd7da58c13 | 1.72542 | -50.97088 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d07edbd9-70a8-3c38-9141-3bc4efc78c5c | -1.61342 | -49.99138 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dfe148be-da00-38ff-9e95-34a67d870f71 | -1.33767 | -48.98146 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1960842a-d88a-3db2-ad84-5176a6af910b | -0.49423 | -49.12927 | 2026-09-28 16:28:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71510111-fc0a-3596-b40c-3829a5bba949 | -3.41803 | -48.33755 | 2026-09-28 16:28:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 626b68e3-7564-33dc-859f-3586a6a69489 | -1.33423 | -48.98155 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f11f784a-81bb-30ec-a650-1207a295c2f5 | -3.20575 | -51.03247 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bff7d103-17dd-3586-9e4f-f3e10dd07de0 | 1.65756 | -55.91103 | 2026-09-28 16:28:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d29d6b7b-bb8f-3079-ac75-1e7b3eb563ce | -1.58075 | -50.25546 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 70417209-4a74-38d3-b097-ba8fb51c7112 | -1.2781 | -49.3764 | 2026-09-28 16:28:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 44fbc5e9-b70a-3c6b-bede-343b20dfa838 | -3.51154 | -50.31025 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 681c3298-fbcc-3c7c-b59a-8c53126165be | -1.46808 | -48.93179 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5a0db11-6f23-3e9e-8095-73e4a7f13a89 | 0.63573 | -54.38117 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2c00f92a-de87-3c3b-b7d6-4f950e1bc403 | -2.0161 | -49.88509 | 2026-09-28 16:28:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7edee7c7-0544-3fa7-94f5-2096b6588681 | -1.55154 | -50.4252 | 2026-09-28 16:28:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9f969ee8-ea0a-3697-b008-e1e0a8ee3421 | -2.05289 | -49.4893 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65494f3c-5f6d-33b5-8698-4827bd99e91d | -1.6995 | -49.84494 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e082bd67-2a6e-3d0f-9043-83e9712f6cb6 | 1.84662 | -55.59209 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| bcafabcd-4d95-316c-badb-383d23f11073 | -3.14775 | -54.08507 | 2026-09-28 16:28:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 6605823a-235f-335a-809c-ac37f45be71f | -0.83943 | -47.78454 | 2026-09-28 16:28:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9536ae29-0351-35f4-bd32-5a400cdb349f | -0.64181 | -49.21892 | 2026-09-28 16:28:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 38bf7de8-82ba-35d0-8133-20abf6222243 | -3.15304 | -54.08026 | 2026-09-28 16:28:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 58086356-aa99-3d99-9119-6e14a2465a7c | -1.46756 | -48.92827 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 978c1b52-0177-3815-aea7-f6e3c941c36d | 2.09098 | -55.87664 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e317b47d-5287-35ed-8cc5-826688fa79f0 | -2.06444 | -49.53905 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4f324069-9cde-30f0-aba6-756ec020885e | 1.86895 | -55.58358 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 135c3d32-2033-3025-8223-bff964fa1f62 | -3.07693 | -44.35247 | 2026-09-28 16:28:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 999c217d-54ca-3048-968f-10cb2a042ebd | 1.85768 | -55.57728 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff3d9ea6-6ee7-360e-be44-bce00792f2d4 | -2.0637 | -49.47505 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 6a49266c-98e1-3597-a1ee-61bc9ab5c363 | -3.1465 | -54.07661 | 2026-09-28 16:28:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 67b7dc1d-0b2e-3b33-979a-cb20df517eb1 | -1.53395 | -50.21405 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 239a043b-5413-372f-9681-bab83d1e2ec8 | 1.95922 | -55.68454 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6ac095b0-02be-301b-8218-d12254285385 | -1.43077 | -48.88444 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 54ca1649-75c9-360a-ae73-fc3e25052368 | 2.06456 | -50.74296 | 2026-09-28 16:28:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4c620471-ecaa-3db7-959d-0d6774d371c4 | 1.72308 | -50.95742 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1222afeb-a2f7-3c8f-ad6e-e4b3993f451e | -2.06497 | -49.53966 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 77d49b22-382a-3f0b-a736-c44d13625a5c | -3.10084 | -42.92901 | 2026-09-28 16:28:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| db7e9e7d-5815-3cf3-a9f3-f6d305c28c3d | -1.27868 | -49.38016 | 2026-09-28 16:28:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 745d6bf1-5217-3d07-8f10-c83c8eb96109 | -3.51086 | -50.30558 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8919cd90-cc01-32db-942c-fdd893289f65 | -1.29895 | -49.05266 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c7fe2b8-65c9-3840-a138-1b9a2b5b82a8 | 1.15084 | -50.03663 | 2026-09-28 16:28:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cb406fc3-849e-3d9c-9abc-5ba012a6616a | -2.92463 | -42.86423 | 2026-09-28 16:28:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8e36d626-62f1-3325-a2d6-1eed9681b819 | 1.84119 | -55.60245 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d826544a-3793-3012-9245-a7418c5ae1a5 | 1.8406 | -55.5912 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 161376bf-9004-358e-bd7f-306c2cee4344 | -3.62766 | -49.62806 | 2026-09-28 16:28:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6091c38-d138-3f55-a833-06f292fa8f8e | 0.63635 | -54.37736 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2693dbc0-653c-3343-9fba-62780170e54d | -3.15761 | -54.08068 | 2026-09-28 16:28:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba6b9a39-bcb1-3aa4-aff7-8c4016d3aeab | -3.23626 | -50.57224 | 2026-09-28 16:28:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1fe58d6f-ce07-3c74-9aa7-2a8f20eee034 | -0.47745 | -51.8237 | 2026-09-28 16:28:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 56f0d4f4-6eaa-3d10-a5fb-2dcd3160ef36 | -3.1091 | -51.27414 | 2026-09-28 16:28:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c529939-919b-3528-b09d-305b2843f820 | -3.07571 | -44.52422 | 2026-09-28 16:28:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4e77176-8bab-3f21-819e-f2051cab4161 | -1.46914 | -48.93884 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 25f44e29-aa27-372e-8dc5-fedb88b76733 | 2.09019 | -55.8843 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 61c37eec-fb5d-38e6-9189-c2530081dd33 | -1.47913 | -48.92293 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8cab4a2f-47ec-3255-aa04-9789cc9ea215 | -1.97978 | -54.25315 | 2026-09-28 16:28:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| dc5cfd35-ab74-3214-9520-1a10cb4fb0d4 | -0.96303 | -47.4374 | 2026-09-28 16:28:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c2d4ddf0-1a66-39d9-90f0-d6609e1faeb0 | -3.15366 | -54.08445 | 2026-09-28 16:28:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| c94260f9-3232-34b9-bd9f-e55f250b0729 | -2.28594 | -48.75305 | 2026-09-28 16:28:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b3aef0ab-27a0-37e6-b3b2-1ffe9aab793d | 1.84721 | -55.60333 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 810ec23c-de92-3784-9314-69e92d7f25be | -2.02044 | -49.88446 | 2026-09-28 16:28:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a2af0e37-425b-3fba-84a3-e92f34071b26 | 1.66418 | -55.91174 | 2026-09-28 16:28:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0d6a1939-b95f-37bb-8592-48924d7fe00a | -3.06183 | -44.52272 | 2026-09-28 16:28:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8a74beb-c2b9-3379-be4f-8f4f4a6d1f2f | 1.90031 | -55.57998 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c8e270da-74e3-31c2-9d2f-eb7ae51f1847 | 1.71798 | -50.96103 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8d81cfc7-9ec6-3cfb-a518-e970b524b6a6 | -3.07184 | -44.52122 | 2026-09-28 16:28:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8589ec9-c72d-3707-82a3-3601cd325c1f | -2.2991 | -48.75834 | 2026-09-28 16:28:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5ebb659f-6f61-3f8f-af70-bffb4e726c94 | 1.95243 | -55.68815 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 95b4fe10-6966-3c63-8395-523d1a89a334 | -1.97389 | -54.25372 | 2026-09-28 16:28:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 839c9294-c32c-3ea8-9380-5373fe12ca96 | -0.95938 | -49.80488 | 2026-09-28 16:28:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 13897f43-fc93-3586-875b-2bd6b8f6dd3d | -3.00555 | -43.08218 | 2026-09-28 16:28:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dacfb618-0e2c-3b80-bbfe-5e43b27658e2 | -1.54973 | -50.22925 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d16cee6-ba43-3098-ad01-d8398c84ee3a | -1.6989 | -49.84089 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2faa8a3f-a3d3-34ae-a956-fda248e59ec4 | 1.83989 | -55.59566 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 4f0cf3f2-3a7c-3186-9201-7eddd06387b8 | 2.08488 | -55.87567 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3bf45af8-879c-323e-9db6-5ffcab3e0c63 | -2.44827 | -49.21904 | 2026-09-28 16:28:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 643dbf8e-702d-302a-b11a-d874c8ed2378 | -4.25351 | -51.04681 | 2026-09-28 16:28:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 64ebab52-73c8-3aae-9930-e7ee16dc410c | -1.43131 | -48.88795 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 03cf800b-1896-30db-9e30-c173b0ac2d77 | 1.89361 | -55.58335 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 223c1527-cb2f-388a-b820-c9a9e478c92d | -2.45244 | -49.21842 | 2026-09-28 16:28:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4651ee16-095b-3787-a06d-2e44c7cec7e0 | -4.25275 | -51.04149 | 2026-09-28 16:28:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 30708a9d-13b5-3953-b627-687967d8e983 | -0.66058 | -49.97336 | 2026-09-28 16:28:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22911005-e8e5-340e-9a32-87c1c35a024d | -1.62773 | -50.14826 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 36ccd05a-4dc2-3846-a7d9-27b1aabb508a | 1.84731 | -55.58769 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7564ab59-f12e-3d85-ab83-198abc57d883 | -4.25762 | -51.04079 | 2026-09-28 16:28:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ca255edd-2637-30ea-99ce-cd8bad3ded1f | 2.04266 | -50.90508 | 2026-09-28 16:28:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a918fe05-480d-3ebc-b28c-aca808a65a45 | 1.84193 | -55.59798 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8e61c4cd-b9bf-38b2-a192-cdaa95a91d4a | -1.43918 | -48.90374 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 8037e18a-d079-339a-9b06-0d7c013cab1d | -0.51071 | -49.12266 | 2026-09-28 16:28:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 101fa300-29da-33de-895a-1f1433b6b597 | -1.72918 | -46.1549 | 2026-09-28 16:28:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 925ad10c-42a0-3ee2-b971-d7088c887571 | -0.5283 | -51.87376 | 2026-09-28 16:28:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.5 |


[Clique aqui para ver as próximas entradas](README124.md)
