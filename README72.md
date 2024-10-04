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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 729cd969-f2f2-36f2-81a4-ae3edd69a99d | -14.06919 | -47.90023 | 2024-10-04 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 723c6f0c-fe19-376a-89c1-83280b5165d0 | -13.73425 | -48.14984 | 2024-10-04 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e44ad5bd-b91c-3aa8-9bcb-0f805ec1818d | -15.253 | -47.139 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a180b8ba-c86a-3e3a-b6a7-a46c9f264caa | -15.253 | -47.13795 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68822ad9-116d-3327-8464-c7dc2fb57a7d | -15.24568 | -47.13771 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83ce3702-27a8-3fe8-9572-52a97d339e05 | -15.24201 | -47.13715 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab5a7b63-f829-39cf-9d59-0893f8013975 | -15.2413 | -47.14127 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d710c5dc-8ebc-3c2f-a3b3-db8d114b7978 | -15.23394 | -47.14021 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de22b7d4-739e-3496-83c1-72c5bd8a4fb1 | -15.22878 | -47.14827 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c3bacc8-2183-3bcf-a6ad-958bdd6b3241 | -15.22433 | -47.15224 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2e0fe83-a47f-3cb6-ae09-d96b3f0bcd55 | -15.08409 | -47.17976 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b82913ca-711e-3030-8da5-cc22ab79f9d4 | -15.08332 | -47.18422 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f008d996-df18-3ea9-b1a6-919bed7f8929 | -14.94673 | -47.06141 | 2024-10-04 04:10:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dd117ed-5da2-3c2e-8d5e-44a9c4512d58 | -16.0119 | -47.82072 | 2024-10-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a9fe538-29c0-3e7a-b3f0-d810799eece1 | -16.00927 | -47.81788 | 2024-10-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52c27a89-d69e-36bf-a377-ddce15d6c059 | -16.00844 | -47.82253 | 2024-10-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bf4bd13-5790-3b31-85f7-8f5e938f6d7e | -16.00816 | -47.81999 | 2024-10-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfac197d-42bc-3b07-a329-36c00c2e9d47 | -15.80115 | -48.15585 | 2024-10-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a70eb6c4-5420-34c0-8b1d-11fb44a9c741 | -15.65048 | -47.729 | 2024-10-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 294e6709-8830-3843-84c5-9a26fdddfb3a | -15.41834 | -47.67588 | 2024-10-04 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| adbad758-e4b2-336a-b7f3-ae7e3f854fe4 | -15.41752 | -47.68052 | 2024-10-04 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 97820658-1eff-3a63-b04b-62ca5f3118c4 | -15.4155 | -47.41924 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 859140d6-0ca5-34ef-a2dd-2749c1b45983 | -15.41378 | -47.67977 | 2024-10-04 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 484434b7-7edd-38a0-9a60-f5b0cbd95866 | -15.41295 | -47.68446 | 2024-10-04 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a998219-68b5-3a19-9382-98d25434a9ef | -15.40881 | -47.41375 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50dd1f24-fe16-3266-83f7-af0dde51346c | -15.40512 | -47.41299 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3cfc1fd-cae2-3f80-b2b1-33a71cd36375 | -15.4044 | -47.41719 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e11ad142-e257-3718-8ac3-ce6f697779a9 | -15.39989 | -47.42116 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb7c419b-7b5d-368f-9e9f-c5108e56f4cf | -15.39612 | -47.4209 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 367642f6-41b0-3f43-ba2a-a0bc5200eb2d | -15.39236 | -47.42054 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b7e091-138b-34c5-9818-6731b2308a76 | -15.38861 | -47.42014 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 282c59c2-b177-3c98-95df-4e20a352d004 | -15.27258 | -47.50471 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 76e7d534-6bd5-36f8-8dc7-db465e9c3a5c | -15.2689 | -47.50381 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8241b3d-f42a-393e-9532-175d71c4793f | -15.26522 | -47.50286 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 702bf50b-0bb7-347e-a939-1c1c6a528f9b | -15.26152 | -47.502 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8cd5141b-abb2-31dd-9bb6-8fecf1d104e9 | -15.25779 | -47.50134 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 838f96cd-f3e8-336b-97e5-53f9c2bc3f17 | -15.25474 | -47.49681 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c699ce63-a34e-3925-9bb9-330f021e34d5 | -15.25406 | -47.50067 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 480e2a96-abcc-3ff4-a347-895ea6f1ac30 | -15.25101 | -47.49611 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f2e1582-57ec-3124-bcde-2037d9214ffb | -15.2473 | -47.49534 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad9ba09a-3225-36d5-bf73-4788396240b2 | -15.24289 | -47.49863 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feceaa85-894c-333a-a4f4-f532c99f58a6 | -15.23914 | -47.49804 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77053969-ae2e-3e64-97aa-66277ed30988 | -15.23538 | -47.49756 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf60a97e-fe5f-3b00-ba77-66e4f8865fb4 | -15.23091 | -47.50113 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16c9a86b-c15e-3bbb-9fc0-e7ea27ecdd81 | -15.22712 | -47.50077 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1795f27d-3c2b-3b63-bb54-2c8d7cd16f0c | -15.22333 | -47.50045 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fddedc59-56f8-3dd4-a8ca-3df2e6a23efd | -15.21884 | -47.5041 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de208076-a46e-3524-8abf-6996f074a6f8 | -15.21813 | -47.50816 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 88fb5b7a-5983-3603-9a80-d14725ea50b9 | -15.21436 | -47.50766 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae8bc5dd-edbc-38de-b882-1cc660357452 | -15.21366 | -47.51165 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca09671d-82f8-3d33-b33a-8e216d5e1a2a | -15.17354 | -48.07169 | 2024-10-04 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b530266e-c4a4-3c52-8deb-2a8cb60ef749 | -15.16968 | -48.07098 | 2024-10-04 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d14d117-a9d5-3d43-91ab-f0bbae7a4e69 | -15.61867 | -47.19916 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1a285ded-3894-3f3a-923b-6d5fa3eea8a6 | -15.61425 | -47.20292 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1fb5da0b-a23a-34d2-894c-bc3e17d1a6e3 | -15.61348 | -47.20733 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2dbec3c1-8aef-3041-8398-186a9da4bc9c | -15.47871 | -47.0941 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 680fa756-d621-340e-b667-88adbbedd772 | -16.70223 | -48.63188 | 2024-10-04 04:10:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bfd694a-e88c-364c-8b0f-b40c8aa6e0b7 | -16.68977 | -47.8275 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2e4d9693-e085-3594-a916-8ffcb2f2046d | -16.68607 | -47.82674 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 322f3570-7865-39bd-8536-3f9e26f195f5 | -10.87412 | -48.13972 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9f58b10-dee5-34e5-9cb2-2d2dcef1ccb8 | -10.8693 | -48.14275 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 689b24a5-be4f-3a1f-a8c9-df76db183975 | -10.86863 | -48.14656 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 410ef947-4151-391e-85ee-e4585ba7c9ca | -10.86795 | -48.15043 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ea8e7c1-dda4-3009-9829-1a0c24498482 | -10.86448 | -48.14582 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07635749-3f23-383e-a2d5-df981124cc08 | -10.8638 | -48.14967 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b28e4574-4da4-3eda-802d-890d87699113 | -10.83339 | -48.27248 | 2024-10-04 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82571154-2fc6-3872-965e-13d8a8cc9b91 | -10.8327 | -48.27636 | 2024-10-04 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e0480020-1e54-3b33-8d07-f104f7f20cf7 | -10.82851 | -48.27561 | 2024-10-04 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a37f6c7a-13cf-3feb-815f-9759d87a49dd | -10.76713 | -47.98489 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1be33a47-5911-33c1-b019-0de076ff28e6 | -10.76095 | -47.99579 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c293e99e-4fe2-3357-8761-a236c8a6fcc6 | -10.74589 | -47.72467 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c4f4a62-b7f2-3015-9ce3-13c4efaa3343 | -10.74525 | -47.72833 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3cb5cd9-394c-3e80-996d-c76d62aa8c8a | -10.74462 | -47.73198 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1c84d935-c271-3aa6-8e40-4741526d63ce | -10.73343 | -47.6293 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 015d453f-e72e-3ced-abcb-17a4fa0e2ffe | -10.72952 | -47.69903 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4c83b20-6b86-3978-a8e5-61851ea2a8ba | -10.7294 | -47.62864 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 174fe632-c216-3a6f-a80e-eb29969e8e53 | -13.17974 | -48.62732 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 948b91fa-2caf-33f6-8457-85d74f683d62 | -10.71638 | -47.72641 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 050d3456-334e-3634-b71b-74d552cfef02 | -10.71576 | -47.72993 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c781ec7-81a9-370f-ab4c-70dd8f814b72 | -10.71233 | -47.7257 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb537226-f737-3faf-97c2-6f249508c895 | -10.71173 | -47.72915 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82ce2033-c245-3a78-b55b-d3bb2be574ab | -10.60186 | -48.1234 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62ef23ca-c1fa-333a-b916-908be1ef55bb | -10.6012 | -48.12728 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1e96c70-8e09-3aac-b5ff-6fe848fe8d7d | -10.59502 | -48.1382 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aab42908-1f3b-323e-bce8-ba193bec11b1 | -10.59285 | -48.12592 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2519bb97-9e6c-372a-8067-311b8f451d05 | -10.59218 | -48.12978 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05ca2db4-57a5-375e-9e29-8410c2a6726b | -10.59151 | -48.13364 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b4d726e-4877-350c-9230-0dab22f89889 | -10.58935 | -48.12135 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05fc192f-9af3-30d2-81a3-265b6bf693c1 | -10.57964 | -48.02971 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76bbe8b4-6b80-3ff1-b7cd-6160a35d8b73 | -10.55687 | -49.03344 | 2024-10-04 04:10:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 09a0e0a2-dd44-3edd-8005-f8809a2629c3 | -10.55453 | -48.07534 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e4dcfa0b-2a7b-3ad2-9bb5-1fbe5ebd2700 | -10.52384 | -48.03149 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9e6996f-a1a7-3c0d-862b-ac351da54af9 | -10.52317 | -48.03527 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 370abdd3-44bc-3687-bbd1-2e000e576436 | -10.49714 | -48.18056 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 41bf5617-fbb8-3b76-b12e-ac6ff24b1588 | -10.49668 | -48.17707 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 079eb227-c4f1-3003-8e25-96dfa09aa4c2 | -10.496 | -48.18103 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8efbe23-486d-3629-8d44-188e975c218a | -10.49299 | -48.17963 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2d6475a0-b1ca-3160-9375-ce9b18fa35ac | -10.49254 | -48.17604 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7976a178-1b54-3c2b-bdab-951b47c895b5 | -10.49185 | -48.18008 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a07c74e-7a75-3845-b3a2-fc5030448c16 | -10.49116 | -48.18408 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README73.md)
