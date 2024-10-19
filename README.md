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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 915280b5-3fa8-3839-b34a-31c532251f37 | -1.1375 | -47.3179 | 2024-10-19 00:05:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| cd6f5a91-064b-3013-8ee6-81eaddc84b0a | -1.156 | -47.3176 | 2024-10-19 00:05:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 78726fe6-751c-3117-8766-61a0bd61f956 | -2.5444 | -47.2231 | 2024-10-19 00:05:20 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 27aee8d3-98a4-3c06-9515-967241e9e3f5 | -2.7236 | -48.8393 | 2024-10-19 00:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d6b33313-d3bb-39d2-b16c-9357bd71cab0 | -2.7885 | -51.3618 | 2024-10-19 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 97e7bc9e-5b49-36b5-aef3-861cc5a83f86 | -2.8069 | -51.3613 | 2024-10-19 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 674aab8e-5e74-3396-be99-457722010e1b | -2.844 | -51.2982 | 2024-10-19 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4fa294f5-477d-3cbd-ad56-c640e323d726 | -2.8553 | -48.2558 | 2024-10-19 00:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| baabf55a-ee17-3678-89ac-c82103754f85 | -2.8738 | -48.2552 | 2024-10-19 00:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 6e9068df-0406-3dea-be62-012f5d3e402b | -2.8739 | -48.2336 | 2024-10-19 00:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 63e0cf9c-e72e-381a-87f9-1477a6a516f9 | -2.8923 | -48.2546 | 2024-10-19 00:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 85f7746a-8488-32e9-86ca-b978b640b6bd | -2.8924 | -48.2331 | 2024-10-19 00:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 69729f46-84f8-39c2-aa5a-e17466dff7df | -2.9489 | -52.9174 | 2024-10-19 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| ed1c6389-5ba7-3fda-bf89-63dcf13b1d8c | -2.9489 | -52.897 | 2024-10-19 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 4e12f762-698b-3666-9587-cad0876bca13 | -2.9674 | -47.9931 | 2024-10-19 00:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 694acead-4b62-341e-a948-87095e87ede3 | -2.9673 | -52.9169 | 2024-10-19 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| c0ae565c-73c5-3b52-9207-2edb2c9c5f91 | -2.9673 | -52.8966 | 2024-10-19 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 912c49c4-4ade-3970-a979-e0025008eb12 | -3.0541 | -49.4046 | 2024-10-19 00:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 05d10ed0-4063-39c4-a45c-c7a8231e363b | -3.7116 | -51.1261 | 2024-10-19 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 505dc6e0-b108-3564-bca8-c76b908a0abf | -3.7117 | -51.1053 | 2024-10-19 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 7c5ddf39-e4ea-3998-bb16-1aa6843e3913 | -3.7301 | -51.1047 | 2024-10-19 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 20ac1cb6-06c5-3f45-80ee-f5a2613f4e40 | -4.3982 | -50.5358 | 2024-10-19 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6d6975b6-bf0a-337c-860c-1ec305637138 | -4.4167 | -50.535 | 2024-10-19 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 8e09c354-e90f-30d2-9a8c-9b133b560a93 | -7.3637 | -72.881 | 2024-10-19 00:05:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f127b23e-9526-3305-8bfe-53d62b329d79 | -7.6815 | -47.3213 | 2024-10-19 00:05:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 7220a4ed-395d-3d36-9680-4c7706d6b18a | -7.6391 | -73.1162 | 2024-10-19 00:05:50 | GOES-16 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 88.4 |
| dc9563ec-c085-3747-b316-9fed7e332808 | -12.5147 | -63.3014 | 2024-10-19 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 100.5 |
| fc2b1904-1bd2-3df7-9228-1a1abbad8250 | -13.3717 | -50.8013 | 2024-10-19 00:06:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| d50db62c-b46e-3154-8dbc-184a72ed07ca | -13.372 | -50.7798 | 2024-10-19 00:06:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c4d66693-8195-36b4-b258-b4323404abd2 | -13.3909 | -50.7988 | 2024-10-19 00:06:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 30569bee-55c8-3f34-9fe5-928b9cc6caf8 | -14.3876 | -54.5332 | 2024-10-19 00:06:27 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5b979352-1d46-3c7f-b19e-fb8e07a1b619 | -17.0233 | -56.015 | 2024-10-19 00:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| a29f47f9-3d37-3531-971e-59ef8c76e9be | -17.0237 | -55.9943 | 2024-10-19 00:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 7b57824f-7703-39ec-8f06-860f68a94887 | -1.1375 | -47.3179 | 2024-10-19 00:15:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 2842c685-5e07-301d-b32c-04e03f86056f | -1.1375 | -47.2961 | 2024-10-19 00:15:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 90cb0387-a0fa-3230-acb2-e8b0025310de | -1.156 | -47.3176 | 2024-10-19 00:15:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 1bb379c0-6c8a-3b4a-8d06-ed196afd21bf | -2.5444 | -47.2231 | 2024-10-19 00:15:20 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 432cf3f7-ae9c-3a2c-a816-68a2146b60a5 | -2.6509 | -48.4985 | 2024-10-19 00:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 01042439-6f8b-359d-9cb0-9982012a4d8c | -2.7236 | -48.8393 | 2024-10-19 00:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6e4a4227-060f-3c62-8e56-446a37ec0ef6 | -2.7885 | -51.3618 | 2024-10-19 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 36efc34f-7307-3507-8d8b-498fc52a5afb | -2.8069 | -51.3613 | 2024-10-19 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3c172853-8fec-3ac9-91d4-9b6cd477be46 | -2.844 | -51.2982 | 2024-10-19 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| dc020561-5d50-3e7c-bbea-7505c5695e68 | -2.8738 | -48.2552 | 2024-10-19 00:15:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d42578d1-e388-3c0c-99a4-e6f1c2491b34 | -2.9489 | -52.9174 | 2024-10-19 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 8a9cab9a-31fd-3b69-a782-deae0ff86fb5 | -2.9489 | -52.897 | 2024-10-19 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9e6b1e59-3720-3699-b19d-79c101686ee8 | -2.9674 | -47.9931 | 2024-10-19 00:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| c8c4123d-61b9-3487-92d8-24895e459548 | -2.9675 | -47.9715 | 2024-10-19 00:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8cf6315e-d7e4-31df-80dc-24ea59ad6f30 | -2.9673 | -52.9169 | 2024-10-19 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| c0fda5a1-6aff-3115-8882-64a6ca4a4008 | -2.9673 | -52.8966 | 2024-10-19 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 63f4fd36-223e-39a0-b667-668137ccd2bb | -3.0541 | -49.4046 | 2024-10-19 00:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 00938f07-87a4-3cda-b502-f186a774ffb4 | -3.7116 | -51.1261 | 2024-10-19 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 1321c4e8-82e9-3775-be2e-d89e4d4b4066 | -3.7117 | -51.1053 | 2024-10-19 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 0daee1cc-97d6-308d-85be-a7d36e1f9f46 | -4.4167 | -50.535 | 2024-10-19 00:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| dddb3dca-14b6-3f6d-a9b4-d839ea62ef3e | -4.6873 | -45.8504 | 2024-10-19 00:15:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d48745b4-a8cb-3a54-80f5-12af75ff3699 | -4.6875 | -45.828 | 2024-10-19 00:15:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6528eb9b-3bf2-3bb2-b279-8f9df3ff8836 | -4.706 | -45.8493 | 2024-10-19 00:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| b2231e87-6db1-3703-a9d2-4c708e91005f | -4.7061 | -45.8269 | 2024-10-19 00:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 926b4736-3839-3edb-9fc6-d88847ab502c | -7.3637 | -72.881 | 2024-10-19 00:15:48 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d8f35624-5437-3073-af2c-03b36b0c9084 | -7.6815 | -47.3213 | 2024-10-19 00:15:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 7ad830eb-1da0-371e-8724-687261d167ca | -7.6391 | -73.1162 | 2024-10-19 00:15:50 | GOES-16 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 69f743b1-b1d1-3d73-813b-045c0946a228 | -9.0344 | -67.4641 | 2024-10-19 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| d13f2214-34a9-3637-8c69-d15e5001879b | -9.0345 | -67.4455 | 2024-10-19 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0e10b71f-4501-31cf-a58f-f56567fa1462 | -12.496 | -63.2832 | 2024-10-19 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a6eec450-7d44-3e32-93a2-c54321ea305e | -12.5147 | -63.3014 | 2024-10-19 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 2c70490d-73f3-3bf9-acb4-a98b370454f4 | -12.5149 | -63.2822 | 2024-10-19 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c199002b-f12a-3315-8c32-b189309ac461 | -13.3717 | -50.8013 | 2024-10-19 00:16:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 5c4e5414-4cf1-3cca-bcfc-f026a6df6e41 | -1.1375 | -47.3179 | 2024-10-19 00:25:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 8d601062-6fdd-3f47-975e-c4f57b99257e | -1.1375 | -47.2961 | 2024-10-19 00:25:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 24bd4e0d-3f32-37ee-a282-dd05760b8cd5 | -1.156 | -47.3176 | 2024-10-19 00:25:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0f848a20-af60-3ed7-83d2-d6ce1b61b29c | -2.6509 | -48.4985 | 2024-10-19 00:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3e1d2dd5-dbfa-30f1-9c2a-c329fc72b7f8 | -2.7885 | -51.3618 | 2024-10-19 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1f004757-acb9-3348-a9dd-41912254d916 | -2.8069 | -51.3613 | 2024-10-19 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 898a4de3-6590-38bf-a46b-3e7c633627ed | -2.9489 | -47.9937 | 2024-10-19 00:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 044c22ce-1954-3dda-877e-68ab854399c4 | -2.9489 | -52.9174 | 2024-10-19 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 818c5783-6ce6-3245-91f7-9209f4502b4f | -2.9489 | -52.897 | 2024-10-19 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c1a4ee30-48c8-33cf-91b1-af4b771e58e9 | -2.9674 | -47.9931 | 2024-10-19 00:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| bc742148-ce04-3d80-85ee-503a9f5e4d6f | -2.9673 | -52.9169 | 2024-10-19 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 01cb18d6-e55d-3e7b-a478-d536bcbfd2b3 | -3.7116 | -51.1261 | 2024-10-19 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| eef35609-b8f2-39a0-8ea9-98b5a5615aa6 | -3.7117 | -51.1053 | 2024-10-19 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 2e87edda-2164-3117-b6de-ebe38f4aa29f | -3.7301 | -51.1047 | 2024-10-19 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| cbe57455-43d0-3dee-a92c-9da00be9e8a4 | -4.3982 | -50.5358 | 2024-10-19 00:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e02faa07-306f-36f7-910b-aade1f17484f | -4.4167 | -50.535 | 2024-10-19 00:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e61b9310-6f18-3395-a4ae-3b39f820e91e | -4.6873 | -45.8504 | 2024-10-19 00:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5b07a9b0-887d-35d1-923e-d846855b3c60 | -4.6875 | -45.828 | 2024-10-19 00:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 8330dc78-eaff-36fc-8f14-c3fbc00d5331 | -4.706 | -45.8493 | 2024-10-19 00:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 742b5984-f4d0-3f02-aa04-3308a9981845 | -4.7061 | -45.8269 | 2024-10-19 00:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0713a7df-41b1-3b1b-b8dd-76a3e19e444c | -4.7434 | -45.8248 | 2024-10-19 00:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b6c87c5f-1c10-3431-9614-91ad6eb177d1 | -4.7436 | -45.8024 | 2024-10-19 00:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| cfd40b18-8dfc-3ddc-b767-6bc2a840217f | -5.1213 | -45.1495 | 2024-10-19 00:25:35 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e88b682a-e8c4-3e57-89ac-68080ae0eb71 | -7.6815 | -47.3213 | 2024-10-19 00:25:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| e5f72337-4ad5-3878-8208-1121aaffbf72 | -7.6391 | -73.1162 | 2024-10-19 00:25:50 | GOES-16 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 5af5c180-d5f1-3a0e-bee5-6538f1c4418b | -9.0344 | -67.4641 | 2024-10-19 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| aa53acd8-fb5b-31b4-8257-d514123b3fe1 | -9.0345 | -67.4455 | 2024-10-19 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| bb4a3a3d-605c-3033-bb8b-cda393ab9b51 | -9.053 | -67.4636 | 2024-10-19 00:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 3f695b00-72fb-3060-a744-2cba1ab181bf | -10.6743 | -54.902 | 2024-10-19 00:26:07 | GOES-16 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| bf0c90e4-539e-3834-8c5a-04617ebcb008 | -12.496 | -63.2832 | 2024-10-19 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d5c59f84-3bd7-3cce-93c4-b3c7c739ba51 | -12.5147 | -63.3014 | 2024-10-19 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 159c7f88-6052-35a9-8714-e091d8d9165d | -12.5149 | -63.2822 | 2024-10-19 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 20456dee-4c84-3d53-8623-ecd3277dc9c9 | -19.677299 | -42.217899 | 2024-10-19 00:31:11 | METOP-C | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d461ed6e-4f94-3cea-86ff-e2f1a6219c50 | -19.6789 | -42.225101 | 2024-10-19 00:31:11 | METOP-C | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
