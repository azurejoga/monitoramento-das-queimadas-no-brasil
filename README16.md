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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 174648ab-7071-3c09-b1d0-33e74667f27d | -16.76515 | -55.11203 | 2025-12-02 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a3639ce0-7aa4-3e5e-b66c-f183dcb1f870 | -21.92607 | -56.77034 | 2025-12-02 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 325c84b2-f918-3b73-a898-73e0d0c6dfd6 | -19.7854 | -56.66857 | 2025-12-02 05:01:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a4d7abfc-49dc-309e-abac-d34da409117b | -8.1822 | -43.2034 | 2025-12-02 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 907ce39e-6be8-378e-bd4f-40b857f244ff | -8.0703 | -43.0981 | 2025-12-02 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| ea885b4d-11d7-37db-a86e-513e9650e462 | -8.1819 | -43.2269 | 2025-12-02 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 61a6bfac-8dc7-3221-a72d-cafc1fef510b | -8.0513 | -43.1001 | 2025-12-02 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.7 |
| 40266750-4aa9-30bb-a2f9-3efc1c35a165 | -8.1633 | -43.2055 | 2025-12-02 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| e15792b7-4f01-3230-8a55-7c1d4a179e16 | -8.163 | -43.229 | 2025-12-02 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 733b1d81-0689-3995-8246-15242a3a5b13 | -8.0513 | -43.1001 | 2025-12-02 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 184.7 |
| ee83fe68-5bf8-3860-9c9f-d4c6c1fcb737 | 2.17385 | -50.8829 | 2025-12-02 05:22:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48db0dd6-c76a-3e37-bad9-baa7d960ea2f | 3.48152 | -51.25935 | 2025-12-02 05:22:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db43f68a-c1ca-3c0c-a7c7-a8ee685c9543 | 3.53659 | -51.45082 | 2025-12-02 05:22:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79bc09b5-6fa8-33ad-b20f-0e6b9a93416d | 3.47687 | -51.26011 | 2025-12-02 05:22:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 381857dd-5118-38ed-bd9b-ee29e9152270 | 2.17143 | -50.88202 | 2025-12-02 05:22:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3c8ee90-981d-339f-82b5-7c6e0fb9d9f6 | 2.17233 | -50.88739 | 2025-12-02 05:22:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ee4e5d57-4f5e-3d97-af34-d15761243f76 | -2.96496 | -51.00984 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c46c725-5296-3bbf-b822-f42fcb7f0f8b | -3.79745 | -50.61131 | 2025-12-02 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 073f87c0-bf21-3800-97cc-996ee066466b | 1.55772 | -50.79808 | 2025-12-02 05:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5425c99-0f15-3885-95d5-616a40cd745c | -2.95878 | -51.01542 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eac42b06-5872-338b-a76a-5ab5a10320d1 | 2.01498 | -55.71189 | 2025-12-02 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c3e23a0-8602-36a9-854f-cfe3e5d6ca02 | -3.22369 | -46.87424 | 2025-12-02 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e282d7f2-b4e9-3083-ac7e-479c5bd3c2fe | -2.95925 | -51.01223 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23d28420-fd97-3b54-820d-73d77df53441 | -0.82636 | -52.28138 | 2025-12-02 05:25:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6023585e-a052-37e2-8ba1-2508cbfc9f53 | -3.6032 | -47.26911 | 2025-12-02 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f0196bc-7342-3c1e-9326-95d546e502db | -3.60129 | -47.26957 | 2025-12-02 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2f0ebc1e-8cc4-3e8f-a535-90cebb45f5b5 | -3.60213 | -47.2639 | 2025-12-02 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ae5d0528-f609-3714-9fa3-693f47157617 | 2.0114 | -55.71244 | 2025-12-02 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aa11983d-15b4-3ff7-8860-5c4acf3a3dc1 | 2.01692 | -55.72395 | 2025-12-02 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c31c5432-4e47-36f7-ad3b-779003832632 | -4.04013 | -49.50749 | 2025-12-02 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f709973-8e1e-3bd9-bd4b-2976223ae4ca | -2.95999 | -51.00723 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e266adf2-4128-3845-a627-d99bdaf9e737 | -1.14926 | -53.59294 | 2025-12-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 365181ff-2afe-356f-b4db-5b3d23d2ca78 | -1.93331 | -52.12309 | 2025-12-02 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe561155-3ac0-33e0-8077-905599e1c467 | -1.21155 | -53.37346 | 2025-12-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b4fe640-30fa-3ac8-9f46-b5577493dab8 | -0.82769 | -52.28349 | 2025-12-02 05:25:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d84cd30-a2f7-34fa-a0b2-02f82afd648f | -2.96474 | -51.01123 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a675d61-8c9d-3685-950e-953f5de94868 | -2.4376 | -47.18563 | 2025-12-02 05:25:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4000b43-f029-319d-881f-5bd20c910165 | -3.79794 | -50.60794 | 2025-12-02 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf2927a0-d763-3d92-b583-de85a023fc04 | -3.60398 | -47.26358 | 2025-12-02 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e669525a-8b7a-353b-abd2-eb086dd544ad | -1.92906 | -52.11853 | 2025-12-02 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713f1da1-efef-337d-8183-cd48b198cbc7 | -0.99091 | -53.20388 | 2025-12-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d2704ad-42ce-3b7b-8c1f-93d9a8aae169 | -2.43675 | -47.1912 | 2025-12-02 05:25:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 988350a1-91fa-3d77-942c-a94e15e6aaaa | -3.47862 | -51.36499 | 2025-12-02 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c40315e-484a-3c6a-93df-acbe82fe973e | -3.59643 | -47.26842 | 2025-12-02 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b010e85f-6db9-36ce-a216-da4f68a89493 | -1.93385 | -52.11926 | 2025-12-02 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6eb4fe82-1c27-3a98-9438-76673014dd80 | -1.14864 | -53.59686 | 2025-12-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 114f7316-1dcd-3ace-b500-717f00a77416 | -2.95972 | -51.00903 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a4fc039-ffa9-3c23-adcc-ba11df690aea | -2.95901 | -51.01361 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cb5261d-9c61-3af6-b20d-6368e5981d16 | -4.04142 | -49.51006 | 2025-12-02 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6fd75c92-5c03-39eb-8214-705cb5ba132e | -1.93412 | -52.11795 | 2025-12-02 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 759eebe6-1f02-3c08-8109-d8293ed38574 | -3.80291 | -50.61213 | 2025-12-02 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 277a96f2-8845-333d-b198-0ae3806bb3c9 | -0.99026 | -53.20801 | 2025-12-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdb1a7ba-44e6-302c-8f7b-5a062cc23950 | 2.01627 | -55.71989 | 2025-12-02 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fa90894-36f5-3fae-9465-58613b65854c | 2.0078 | -55.71293 | 2025-12-02 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d7f2d3d4-dbbd-3f76-8c0b-a7784adc9b70 | -2.9595 | -51.01042 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ef6f628-b042-39ba-82c4-ecd023a882c7 | -4.03952 | -49.51175 | 2025-12-02 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 597259bc-6b20-3fb6-8250-42711179a175 | -3.46007 | -50.00266 | 2025-12-02 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 799d64d2-d269-3f8f-8897-501366cb7276 | -3.59732 | -47.26208 | 2025-12-02 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acf646a3-14dc-3a42-b01f-f5f39644b9b7 | -3.80339 | -50.60884 | 2025-12-02 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c9e00c0-681b-3128-a8de-80cddbcca5ba | -2.95851 | -51.0168 | 2025-12-02 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb4e0dcf-7bb8-380c-b61b-c985544655f1 | -13.04737 | -53.7113 | 2025-12-02 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71fa57f1-639a-3d87-a99e-d114d7d80ae3 | -13.03724 | -53.71004 | 2025-12-02 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ddd0a88-f48a-39b4-90ec-a99828678ced | -13.04107 | -53.71105 | 2025-12-02 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52ca61e4-057e-3439-9104-279c8625a6a7 | -12.04583 | -54.23944 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e3260b94-e64c-38c4-aaa4-d408a07ea72d | -11.4342 | -54.87096 | 2025-12-02 05:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b32b4e38-7106-3ea0-ad78-cb2648ec916d | -11.67167 | -54.58366 | 2025-12-02 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a1ed90a-285a-3be9-8d45-5b67c6a900a4 | -12.40813 | -54.8886 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0680cc9-e3fd-3e5b-a461-1ce5c885f071 | -12.04748 | -55.36069 | 2025-12-02 05:27:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ea01183-bde8-3fb7-833b-9283581b7c4d | -12.04808 | -55.35624 | 2025-12-02 05:27:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5abbabfa-5d3d-377c-9c7e-bcd1bcddda50 | -12.04447 | -54.25004 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e5c5da9-12e2-3a79-82e7-26c6a34bb3e2 | -12.04034 | -54.24411 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9998f58f-3037-3127-8c3c-6bd0b7883df0 | -12.04102 | -54.2388 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83a90ebb-557a-375b-9057-dc3a11fb2f23 | -11.67636 | -54.5842 | 2025-12-02 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b20bbb57-9472-3783-aeaa-f8fcfac3d2ec | -12.40288 | -54.8927 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c986b5f2-e279-3f3f-96b2-33ff4dab8379 | -11.67232 | -54.57865 | 2025-12-02 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40834eb0-2312-3dfb-a838-287a54714b1f | -11.13421 | -53.93914 | 2025-12-02 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2c7260f-8035-3b3b-95bb-6479487caffa | -13.0465 | -53.70865 | 2025-12-02 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3527eef-4e58-33e0-860b-ebcb67c95a3d | -13.0423 | -53.71067 | 2025-12-02 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3593541e-4c0e-3dac-a580-5a0255bda271 | -13.04613 | -53.71169 | 2025-12-02 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68b06fe5-fa56-33b1-b417-561dbf229d6a | -11.13905 | -53.93985 | 2025-12-02 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a226ba1-86e1-3f0d-9ed0-e1735b2df5b0 | -13.03685 | -53.71308 | 2025-12-02 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ade1a30d-97fe-3f97-8d32-5450b5997579 | -12.04515 | -54.24474 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2383342-d5a5-31b9-a1ce-5b2dd02bb210 | -12.40751 | -54.89336 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b36e4d05-0e42-3333-a98b-1eda66376f4f | -11.43877 | -54.87163 | 2025-12-02 05:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e064739-560d-3f73-a3fa-5fee2ed611ee | -12.41275 | -54.88925 | 2025-12-02 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7c989eb-0549-3249-b338-1f19b092816a | -17.50726 | -57.19633 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 55afb5e7-089d-318c-88ca-7c3e9a136e7e | -17.51151 | -57.19692 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| b38c4139-2646-328b-b7c5-7ca529a39c28 | -17.52374 | -57.2028 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e49b76f8-dd6c-3aab-b907-3013872f277b | -17.49501 | -57.19046 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a1cdd4f4-2a66-3fd9-8861-ef1e4bbc316a | -17.52621 | -57.20995 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ce895c85-8838-33d5-823f-a5a1dfd4e865 | -17.5177 | -57.20875 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f738faa5-88cb-3c3e-8062-49fc644338ab | -17.75159 | -57.2555 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3aa7df11-f23c-36eb-8f1a-0cdae453852f | -17.53472 | -57.21114 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e8507853-a8c9-3127-a193-4abbf55c7c68 | -17.52246 | -57.20523 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 40f2bdde-13cb-3865-8ffa-97ae30d0ae17 | -17.53046 | -57.21054 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 26302fdb-6082-3490-822b-1c24ed354cdc | -17.51395 | -57.20405 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a88f4ab0-b820-3cc8-9ebb-efef4695b72c | -15.12338 | -52.94855 | 2025-12-02 05:29:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04bb3d58-f3cc-3d18-83fd-868c0096160c | -13.20478 | -53.14841 | 2025-12-02 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02dc4dc7-820f-3e3c-8e7c-ac03bc163e97 | -17.51523 | -57.20162 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| eb185bb2-b07b-3a90-9a70-4f5e801c482c | -17.49129 | -57.18576 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
