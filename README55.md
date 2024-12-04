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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13c6b7be-4172-3d06-a7ce-8fee75209db2 | -3.24648 | -50.42009 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28b10f70-e91e-3250-b57f-2a5f62f2307c | -1.08028 | -53.45435 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe5b794a-a975-3232-a203-4746528edd43 | -2.43997 | -54.03925 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 733ec209-fca4-32b7-88fa-38b6184eb843 | -3.20761 | -50.64857 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 502049fb-bb9d-3c87-81f9-59386889e2e4 | -2.20329 | -53.7702 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6d424a5-66ab-3106-a390-ec53a65599af | -1.31376 | -54.57318 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5c7bc8c-751a-392c-b651-a7f5b4fb5272 | -2.8828 | -51.80049 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 93932139-3eaa-3b6f-8311-9a41a5e66de3 | -3.12125 | -53.98638 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee78d394-ee34-3a1c-8e3a-af4c1235f686 | -3.9819 | -50.51914 | 2024-12-04 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59bc13ec-52d9-35fa-9c5b-bda961b25692 | -2.90288 | -51.8171 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9f726c6-49f9-3bec-937c-9ba747967f8d | -1.07627 | -53.44852 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ede43d0-e9ad-3f47-96d2-1463ee5b256a | -1.66293 | -52.74905 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42ef3f02-55b9-3909-b6c3-ff879dc75317 | -3.06703 | -54.05537 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0173f257-dee8-39f0-8dbf-e4ee37056edc | -1.6501 | -52.38213 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 69ce71a4-bd01-37be-a1b3-c2fc4f3c851e | -2.72775 | -51.82529 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9c40414-983a-3ea9-94bd-4f385a9fe049 | -2.79618 | -54.14259 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fd159b6-3201-3f0e-bf6a-bd5ac420c881 | -1.65417 | -52.39241 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e36921-3b7a-3e9e-95f9-24180bff77c7 | -1.44133 | -54.84497 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d887bc47-7e36-3a06-a290-93ac8df0c937 | -1.46932 | -52.68233 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ff51ab7-ed85-359e-9c0b-f07cf870be43 | -2.69266 | -51.86755 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bd9060a-44d9-3275-81dc-4a453ae407d1 | -3.37901 | -51.09562 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e09f30c5-f932-3552-becc-0289030b054c | -3.50014 | -54.02934 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac2db208-4aa2-3be1-9acf-03333d562095 | -3.26049 | -53.64721 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6685e862-585a-3bd1-82ec-8763facbe094 | -1.55669 | -53.78871 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48b656ec-3e1b-3b3f-90ec-98b75091027f | -3.08169 | -53.38039 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8eeabf80-8193-3db4-85c8-bb5aea65ab8a | -3.12693 | -54.61755 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cc10b8b5-ab71-37a3-b464-2237f8b26eeb | -1.75631 | -52.63662 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 79cc416a-374f-34a7-9604-5c552fb3c1ed | -3.61066 | -50.79848 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a9531a8-76d7-339b-a1bb-7d95a6ccaf15 | -1.87977 | -53.30087 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39851677-448f-3219-9db2-7604a5b9cb1d | -2.72827 | -51.82178 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 238460f7-3df0-391e-ae9e-64176bdb8737 | -3.72333 | -51.08912 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c98d734-f472-3b49-abe0-4a9633eabea5 | -3.19048 | -54.50414 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24b207cf-ab0e-35bd-a6d5-d1841f6e3a28 | -1.32297 | -54.96903 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e6bdb5-5789-38b0-9779-c91561836b0a | -2.88987 | -54.15671 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c944fbf0-2263-3aa7-a9b3-5b3fdc6c423f | -1.66754 | -52.75278 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2923fd68-8924-3267-a877-d1edbc6ded9c | -2.55823 | -53.40881 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b438b3-a5ea-34c9-b8a0-773c21b8af91 | -3.06212 | -53.27385 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c3a81c-14d4-3929-8bea-9149f8aa65ec | -3.12521 | -54.62457 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8476ab22-5eb0-309a-90ae-19dbd7d15f99 | -1.46886 | -52.68528 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed823212-0b57-30b8-8426-d102d3be2eb9 | -3.05896 | -54.50634 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58f7fba8-388b-3bad-aec8-b613384f7744 | -2.8243 | -54.14671 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 848ed6d6-271f-3ddf-8662-6eb12731f56a | -1.07949 | -53.45952 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93515e13-a50f-36c1-852c-34995ff745bd | -3.27381 | -58.53301 | 2024-12-04 05:29:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d59e00-4a7f-3d86-b53c-06f3c11a5de1 | -3.0533 | -54.85312 | 2024-12-04 05:29:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f8f62b1-55e2-3091-a2d9-9ef10ab4e45d | -3.41021 | -63.49686 | 2024-12-04 05:29:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d6897f1-a586-3754-a137-bb4cbc873e8c | -3.11586 | -54.05272 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52c42c92-cbfb-3922-aebb-ae89319a0710 | -3.53861 | -50.38689 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fec2fd12-9da9-3070-bb47-3cad4d78db46 | -3.1259 | -54.62009 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| fc93d35b-9e05-35aa-b20a-70c5e17665c4 | -2.00429 | -54.10884 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a418e3c-c034-3deb-a879-631344bb4c7f | -1.55533 | -53.78668 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5ecf0c1-7dc4-3c60-a893-7d52c914dd55 | -3.00809 | -53.23012 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 080c74fe-1e73-3a76-b90b-e0ca13a84d85 | -3.13941 | -54.53244 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be69d61f-1691-3461-9c1a-c278b879637e | -1.74835 | -52.62003 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e8035d7-296f-3ffc-a24c-5f81921990be | -2.45237 | -53.6698 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c237030-dff8-33cc-9880-d84b18de2d06 | -2.69361 | -51.86691 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2baf86de-cc83-3d78-991a-35f48c3c37d2 | -3.31002 | -53.35504 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c2eadd1-63c0-3a69-9c6c-f290d6cd577b | -2.81536 | -53.05563 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97bae4f1-fa15-3a5a-adad-2de7cf476e05 | -2.82546 | -53.05715 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a794fe8-0d93-3975-a85a-2ed70a1d69b4 | -1.46362 | -54.96444 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bef3747-7bfb-331c-a6c5-5f024e3187f3 | -1.08105 | -53.44927 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7bbfc9c-9b00-3dc0-9a2a-5df57e944519 | -3.12452 | -54.62904 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ddd06b95-9303-373a-98e6-57d0a5a0bd6f | -3.18906 | -54.51363 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9508d639-3937-3c87-9d4a-ad0ef522f445 | -3.78733 | -50.96404 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c34e7e7a-5fa7-3079-ab01-973c46e561b7 | -3.02805 | -54.18629 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1bb4510-a4de-3239-ba02-bb12bdcd163c | -0.25058 | -53.75385 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1caf9ef-9429-3df8-af9a-deee7590c01c | -3.12626 | -54.62206 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f376c492-2809-3d13-982d-87475a89b32d | -1.03542 | -53.55588 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79583a82-df4d-3bd1-b76c-c353a4832a17 | -1.76188 | -52.63439 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8dfc2318-dd20-359e-84fb-98826dc06320 | -3.63577 | -59.33494 | 2024-12-04 05:29:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6d147e4-f4ea-3224-ae8c-1c697e3da144 | -2.69812 | -51.86837 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0b8c476-5238-3c15-a663-4b9e22946993 | -3.11115 | -54.05478 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3957e5bd-a48c-3e14-8307-1009bd2faf44 | -3.2934 | -53.71327 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4c7b51c9-bad4-3ce2-8bc0-d25d7f79505d | -3.37154 | -51.06531 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e373eab6-eb57-3f1c-8c0b-cb3fe724a354 | -1.61716 | -53.83378 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 413369da-ab8d-37a5-8643-b1a7935caa40 | -3.5528 | -51.52043 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc3b813b-c005-340c-a09f-8df14f271ba4 | -3.13045 | -54.6208 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 60749df8-1cee-3704-bac4-6eca69700e40 | -2.81403 | -53.06434 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 279b5efd-540b-3dba-ba1b-432bdf26aa64 | -2.80159 | -54.1384 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 005c1fae-98e6-3d60-b881-66b771dd6012 | -3.02879 | -54.18139 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1f4c9f7e-1211-3c48-b901-36afa093e39b | -1.48023 | -53.80507 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23998922-ce9b-3d38-9dd5-fa34200f6185 | -3.25886 | -53.65794 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 41e5dffa-d5fa-3b96-b3ad-c38ab90fdfd1 | -2.79517 | -53.05248 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21ce378c-cfa1-364e-b7bf-5f19940e7ea5 | -2.87915 | -54.03913 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28f36146-1cb2-3fb9-8361-6b8e711b9d61 | -2.43528 | -54.0385 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c3d9b53-491e-351b-8239-7d5ae7d9b891 | -4.07984 | -50.27594 | 2024-12-04 05:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f02f88cc-d7e7-3f1d-9ed1-297fee713184 | -3.08253 | -53.3749 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33794458-f6a0-3185-83c3-4f84cbbe9304 | -3.57483 | -50.31207 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a209ba45-9523-3de5-92c7-865166dd0a35 | -2.89899 | -51.57959 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 096cc55d-ef55-305e-a817-c7c30b0e37dc | -1.08425 | -53.46037 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71d4c81d-3b3c-3f36-a166-df92e5b58d00 | -3.24101 | -50.41827 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87eed6c7-49d1-33dd-b2fe-8daeae2c2596 | -1.74925 | -52.61402 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3f9a4ba-68f8-338c-9405-f3da526081a9 | -3.25402 | -53.62397 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5312bbf5-49cb-3543-83cb-ae86a5c5bf3b | -2.23384 | -53.69691 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecbd7d68-24bc-37bd-be98-aef7a026860b | -3.04112 | -54.06688 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3046f716-4124-330c-b615-38d7409c2851 | -1.34379 | -55.44522 | 2024-12-04 05:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 519778bd-ae33-30e2-a487-58cf5d47fd01 | -2.79933 | -53.05908 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00c98831-012b-3b80-951b-7268a0428b63 | -3.19645 | -51.17118 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55dd80fe-2960-3bbf-8a51-85d75b9f4e95 | -3.17467 | -54.33438 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96643125-431a-34ef-8cc9-194f8a303616 | -3.26378 | -53.62561 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f12919a-8dbb-32c3-871a-b421304636a9 | -2.78555 | -55.37209 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README56.md)
