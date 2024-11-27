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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea13ef32-b0ad-3193-a9ba-0508ee40c72b | -3.09472 | -53.27945 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97124811-67f8-38ee-b470-501f9a5636a8 | -1.26992 | -52.23075 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cb04f39-1426-3c81-97db-bf6bb059ed0d | -1.74287 | -55.44793 | 2024-11-27 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 109c3ae1-63b6-30c6-9b55-6bded96e0dc6 | -4.04275 | -48.32777 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaaeac61-e424-3960-8eb9-718abc55611c | -2.24506 | -53.62827 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 106375aa-4b37-3185-ba0c-ede873ac5039 | -0.95537 | -51.65097 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4194672e-49a7-3ed5-8756-67b04c6eb487 | -3.01733 | -53.41581 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc4a625f-f088-36c5-8797-4d43b01f43ff | -3.263 | -50.43837 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cea2eefa-ffc0-3219-908a-8dc89778fabb | -3.61259 | -50.76493 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33619d15-1c84-3e4d-9739-70bcbcb4b11e | -2.60084 | -53.97242 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ecd1d435-3394-31d5-a619-8347c1a8eaab | -3.80154 | -45.21973 | 2024-11-27 04:42:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf982b78-04fc-3a79-855d-3a4c6d3c45c6 | -1.0683 | -53.37557 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48fc332b-ae96-33c0-95e8-54b7b7ad54f0 | -5.50086 | -46.25483 | 2024-11-27 04:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6ca2df4-d005-3a0d-9122-685af278ce63 | -2.58868 | -51.83057 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7358ebc2-07a0-3802-a166-4e050746bbc6 | -1.96816 | -52.02987 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdb0a9dd-dab6-3cae-9453-c84c99d7cc5a | -2.84029 | -46.83857 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74346d49-1816-36d7-9c99-856509cfbddb | -1.72757 | -52.04269 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45945916-2f70-3bb7-8bd8-3db297456888 | -1.66657 | -52.72001 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e139d615-a7e4-327b-8c3a-947787f4b055 | -3.9778 | -49.97608 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2e82a8a-d5df-3549-a245-5005a48a4b8a | -0.9746 | -51.70706 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| accde3c4-dfbb-371b-80ce-e1bfe5628b4a | -0.80618 | -48.0048 | 2024-11-27 04:42:00 | NOAA-20 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1240553f-e611-3dbd-ab5e-af0c4104fe4b | -3.25791 | -53.27299 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 902f9cd4-99f6-32db-8d38-b21cb52796f5 | -3.16746 | -48.43983 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7979366b-27cb-365b-b1e1-769127255732 | -2.58977 | -54.08778 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4209f029-8e60-36f3-82da-993faf8217b3 | -3.93893 | -46.8928 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e42cdc4b-ebc3-3c3d-bb7b-05b097014a70 | -2.42477 | -44.65005 | 2024-11-27 04:42:00 | NOAA-20 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6808501-a188-3ef3-b190-edeb580d48df | -2.83855 | -51.84988 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 55325c4a-20ec-3de8-9468-a97139ac0ee2 | -1.66082 | -52.52803 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 086ea1a8-cb05-3702-a39a-8f7f04d2b1d7 | -3.73368 | -49.95186 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c14f66b-11a9-3a24-b37c-9cfa573c1c61 | -2.18742 | -53.66538 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6995f1ae-8679-3729-89df-56412d1132bd | -3.96032 | -46.90055 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2873007f-3d44-347f-8689-528743737642 | -1.68645 | -52.617 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54dbd5d1-afaa-3222-867c-c74a89186a95 | -3.03825 | -48.5063 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53129aa9-a57c-3c28-a4cb-290ceda08935 | -2.60834 | -53.97363 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b90d6a8-f6e0-37a5-a633-dcceebebac74 | -1.55196 | -52.02439 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 359b4e74-4a4e-3f1f-9f67-0adfcb5c4b68 | -3.01636 | -48.60318 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6161c450-5335-3042-bc9e-b9d61bf942d3 | 0.65076 | -50.82825 | 2024-11-27 04:42:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f48ec996-8dbf-38f8-b8ad-e25d9c3c1af0 | -4.04963 | -48.32889 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 856eb14b-fc0d-3812-adc4-b8edbe5a6f13 | -3.29012 | -50.61191 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23c3a510-346c-3f3d-96fe-b9368f11ea23 | -3.70917 | -47.66936 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82908b2e-8b95-30c7-838c-4327bd7bc9e6 | -1.27119 | -51.62757 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bec4c1f0-7c47-36e1-8e00-8facce55b017 | -2.95946 | -53.72494 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d09be2ad-4fe3-3005-ac96-dc1705aabdd0 | -3.21542 | -49.18455 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a511dd9-aa32-31fc-b44e-fb5abb092fb7 | -2.2452 | -53.46548 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdd5c3bd-8fc0-353f-b2cb-97f7fe6c5cca | -3.54727 | -50.1875 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5501678-171d-359b-b005-18f973b210ba | -3.25539 | -51.21803 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a332b1f-eb47-3482-834c-c77daee3c89a | -1.51881 | -46.07752 | 2024-11-27 04:42:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53d15608-82b9-352e-a5f5-66ab7de50a68 | -3.51406 | -50.3126 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e46546e4-becf-335b-8105-b938b9447086 | -1.64045 | -52.72409 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 576f894b-7f23-3af4-970f-4518d07b843b | -3.93117 | -47.01862 | 2024-11-27 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17117c6e-3d90-38a2-9185-8c3bb1297a98 | -1.96744 | -48.38463 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc7de3b4-531a-34fb-9cb8-1408435262ec | -1.31412 | -51.75508 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21c28f57-6853-3579-9749-7a58a1821019 | -4.31127 | -48.08411 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 990c5a04-0c06-31f1-911a-202bf1662616 | -3.71226 | -51.8047 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e40e33c0-8c9d-3276-8273-9059744103e6 | -2.69804 | -51.86985 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6abd36e-951f-3dc4-9b41-eada0dafb6cc | -2.82903 | -46.8152 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e5dbc7d-b7ee-3f5f-8621-01da23a45761 | -2.93463 | -48.02123 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30b7887c-e3ce-3565-a3d1-ec7b6906ee23 | -2.61058 | -48.36709 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 220e6793-3acc-3070-9ea6-6019be438f0f | -4.29768 | -48.24238 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2348a32b-b59c-3ce5-8797-4c013b86c993 | -1.62497 | -52.27316 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96dea323-9765-3b69-bb08-ff19d7d51b49 | -1.94482 | -45.72449 | 2024-11-27 04:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f07e441b-7496-3eb5-9d32-a3abb9546d3d | -3.67103 | -53.65782 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a0bcfad-0aa2-326e-8e21-f14b4b3a7282 | -3.4986 | -50.49681 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2313ab48-e57f-3a39-9e13-4e03c75dcb50 | -3.56722 | -50.23286 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93315a39-ac1c-3f0a-b91e-dd1423fc8b6e | -2.11024 | -46.45836 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0f489e6-7d13-3ff3-8d36-bdd197d05c3f | -3.71281 | -47.1263 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbb59292-0c06-394c-b332-412f6accd1b9 | -3.49795 | -50.45795 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ba7297-71ab-3962-bdb7-824f9dd7eec8 | -3.3928 | -50.34995 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4185beff-2325-38fa-bd1e-4259977ff924 | -3.50191 | -50.49732 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9517604b-418a-372c-887d-e421147f4b75 | -1.4475 | -52.59383 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c446d1c-b820-3923-90c7-d5efe8b19f8b | -4.09335 | -44.86038 | 2024-11-27 04:42:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a293660-8159-38f1-84ea-974bc3837472 | -3.83612 | -51.71076 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0db4a975-915a-38d5-95a3-c3390b6b8fb4 | -1.19181 | -51.77468 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a811d0b-fdbf-3486-ac64-55ca73a37baa | -1.63635 | -52.49765 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 948d3fcd-5bb1-3ccf-a149-ba7e288068cb | -3.17938 | -48.4304 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7b48539-2e26-3f6f-9e55-f8d751fe76b2 | -3.57682 | -41.95907 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a6df0e51-f3d9-3971-8add-1aea1e9210f0 | -2.48529 | -49.03186 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f04e885d-d604-3282-83a0-931050158d3d | -4.0884 | -49.33691 | 2024-11-27 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c92157a0-7ec9-30ca-bb79-ba20ce2b7695 | -3.29254 | -50.27411 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d36bb23c-7f16-3d56-ba2d-91ebcc4e9b92 | -1.70073 | -47.86858 | 2024-11-27 04:42:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fa48562-8b74-34a8-8894-a70552a8e164 | -1.75589 | -52.7047 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee0d3b4e-11a3-31bf-8e16-5c518e832ea9 | -2.83164 | -54.12651 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 59a66f0d-3422-38e6-99fe-ad416624d25a | -4.37317 | -48.50373 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5948eed-9efe-39d9-92b7-75947de3a96f | -2.88629 | -48.74144 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 685f6bf6-898d-373f-8d15-dc82ef9d4b17 | -3.28627 | -50.61484 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c2e472-6810-36fe-bb0e-5a36a86262c0 | -2.11392 | -46.45893 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85d1c4f6-de51-3555-a331-b01faf405715 | -2.61364 | -51.80458 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b31d547f-4de8-307a-b7d9-30f3922daca9 | -5.25575 | -40.60055 | 2024-11-27 04:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc0fbaa8-fdaf-3a1b-bfe7-e7c52b02dbf7 | -3.22594 | -54.08854 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d66c1f40-dac7-3df3-8d61-357060f48deb | -4.06538 | -54.38675 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09b3d223-0a95-377a-a5a2-29cd1c7e6084 | -2.70963 | -46.115 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b99656a8-2761-3ebe-bef4-a96647e39ce5 | -2.97488 | -51.57946 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c538671-8977-3d4f-845c-35889c71ef67 | -2.71119 | -48.84642 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13ef63db-5a9a-344f-b970-417d5f871826 | -3.50456 | -50.45898 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad82bc9b-b738-3b10-8011-3f87f91de3b3 | -3.27147 | -43.03762 | 2024-11-27 04:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 959fd58e-8f10-365a-8a34-e18f5c6fed65 | -4.94859 | -45.87983 | 2024-11-27 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 921410c4-4d23-3ae5-bb32-c667cc8ca135 | -3.09083 | -53.25776 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9e9ddc08-a5e5-3ca2-9a7c-bd00537faa1e | -3.50523 | -50.30419 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca72cdff-fab8-39da-a755-86f6deae6108 | -3.41718 | -53.88508 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cd36641-f396-3059-aa02-53b03e91d579 | -3.28563 | -50.27292 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README59.md)
