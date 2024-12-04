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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c252755b-a25e-3e3e-8537-90390c0d5adf | -1.0646 | -46.5952 | 2024-12-04 02:50:00 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| cc397626-621e-307c-9f33-5278c9b25f9a | -1.7361 | -52.6366 | 2024-12-04 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e256038d-546f-3c87-8d44-915899590771 | -1.663 | -52.3927 | 2024-12-04 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a54b68b2-1b8e-3d16-a7b9-8bcba004b9e5 | -2.6428 | -45.7394 | 2024-12-04 02:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9c94d2eb-be28-3db3-84c3-66a2d07a1b2c | -3.259 | -53.659 | 2024-12-04 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 76a2bb9b-194c-32ec-89aa-edeb3ef1a4bc | -1.6623 | -52.7599 | 2024-12-04 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 106c0977-0c17-3e05-b27c-eb1a9054cd4a | -1.7544 | -52.6363 | 2024-12-04 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 258.2 |
| 0af5e25a-dec2-397f-b247-41cecabe42bd | -1.7545 | -52.6159 | 2024-12-04 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 245.9 |
| 91590418-578b-3ecc-987c-c10219401b8e | -2.3097 | -45.4358 | 2024-12-04 02:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| b7a49bc3-d3fd-38a4-bf69-0c0dd2fdeb40 | -1.7361 | -52.6162 | 2024-12-04 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| c6cabd3b-49aa-3320-bbf0-a0f685298002 | -2.8012 | -53.0633 | 2024-12-04 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8a910355-fe90-3ca9-9649-ef533291ec48 | -3.259 | -53.6388 | 2024-12-04 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 36e0402c-5ff3-33f2-8740-5414cec80a45 | -1.7728 | -52.636 | 2024-12-04 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 43732687-0861-3f77-aa2f-be5d35124e26 | -1.7361 | -52.5958 | 2024-12-04 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 72e00398-cb5d-3d9f-9600-ba507e2634fb | -2.8196 | -53.0629 | 2024-12-04 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 87f7acd1-f1a7-3e54-86c5-5b2b0c130dcc | -2.3098 | -45.4133 | 2024-12-04 02:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 2184613e-ed3a-30fb-af17-bbf7cf631b9c | -6.086 | -48.0557 | 2024-12-04 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4ef82d2b-03f0-358b-862e-2e47f1941ad7 | -1.6631 | -52.3723 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 3f8ec839-443e-3e10-bace-1bf07fd7271c | -1.7544 | -52.6363 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 6113e142-8da2-30cb-9f27-ce9e57717daa | -1.6623 | -52.7599 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 56b56b1e-8c67-3fee-8178-57b41093751c | -2.8012 | -53.0633 | 2024-12-04 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b916ed3f-56e8-304f-9fb3-0768fde853f0 | -2.8196 | -53.0629 | 2024-12-04 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 1e5736f9-8d70-3caa-8075-c590ffa497f6 | -2.3283 | -45.4353 | 2024-12-04 03:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b3b42766-e896-3754-92a9-0955548fa7fd | -2.3283 | -45.4128 | 2024-12-04 03:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 03727d17-593b-3fbb-af1f-170924ef9f38 | -2.8197 | -53.0425 | 2024-12-04 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 381dfa47-2f1e-37e4-9ff4-5f7b7356ed13 | -3.1969 | -50.6428 | 2024-12-04 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 0d896236-c586-3b22-a5c0-2d617caba884 | -1.6446 | -52.393 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 06d1d9ce-fe99-3d73-b0c6-aea1c91267ab | -1.7729 | -52.6156 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 52813cec-3877-3a7c-98e9-8c6a666c6e1e | -1.7361 | -52.6162 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| d804ea9b-4055-3d0a-bf38-7c689a3c2faa | -2.6428 | -45.7394 | 2024-12-04 03:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c3061c2f-afa9-35df-9433-9047042cc5ff | -3.259 | -53.659 | 2024-12-04 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 6a560165-cbb2-3674-a267-6844074460d4 | -1.6447 | -52.3725 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 2194f47d-970c-3911-a454-8186663ae9c2 | -2.3098 | -45.4133 | 2024-12-04 03:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 06d80851-2055-3461-866a-f73f54d440f0 | -1.7361 | -52.6366 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c288e2ef-a72b-3f05-95fd-cd2843624257 | -6.0858 | -48.0774 | 2024-12-04 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 2a7d9dd1-f942-3108-80f4-1c6926784c72 | -1.663 | -52.3927 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2ddbe06a-b305-39c3-96af-d80be39fcf96 | -2.3097 | -45.4358 | 2024-12-04 03:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 90c5a351-fc1a-3a68-8b60-a6dacd00f9fb | -1.7545 | -52.6159 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 4a711c64-b86b-3c92-a39a-2f8699438ad7 | -1.7728 | -52.636 | 2024-12-04 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 114fcaed-85e1-356c-b42a-ff3779aec81c | -2.6242 | -45.7399 | 2024-12-04 03:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 26c9c170-c931-32d7-bc8d-9970a8f59495 | -1.0461 | -46.5954 | 2024-12-04 03:00:00 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 1af99b7e-d7cd-39fa-9fe8-febf3204b6ec | -1.0646 | -46.5952 | 2024-12-04 03:00:00 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f5cdb2c9-75c3-36e5-8630-ff04100aa54c | -3.259 | -53.6388 | 2024-12-04 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6b279407-d4c4-3ba9-817e-72dd2398794d | -2.3098 | -45.4133 | 2024-12-04 03:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 109.0 |
| a1b96125-29db-3ccd-a5af-b6839c33e2bb | -1.6241 | -53.5308 | 2024-12-04 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 0e4a7ab9-5bd6-3d05-a2c7-36158154fa9a | -2.8012 | -53.0633 | 2024-12-04 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| fe273a60-f6e5-3c3f-b8f8-d991d1286f52 | -1.7361 | -52.6162 | 2024-12-04 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| d775ee31-b524-3ddb-80ca-439a0bbec2a4 | -1.7545 | -52.6159 | 2024-12-04 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 295.1 |
| 161fc344-b760-3380-aca8-afd513d39da8 | -2.3283 | -45.4353 | 2024-12-04 03:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| b215d391-c414-39be-902e-143a493983a5 | -1.7728 | -52.636 | 2024-12-04 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| c7800e49-909b-3852-82fb-a2de57a5602e | -3.259 | -53.659 | 2024-12-04 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| bb868fb0-b19c-3c68-b67d-a531e625b977 | -2.3097 | -45.4358 | 2024-12-04 03:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 105.9 |
| f2df2cbd-731f-3c37-b6b1-f148e71931a5 | -3.1969 | -50.6428 | 2024-12-04 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8e11a06b-63f9-3f61-a14f-8afc30050235 | -1.7361 | -52.6366 | 2024-12-04 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| deb0ad56-5b3b-38f7-967a-aeca79c9c3a2 | -2.8197 | -53.0425 | 2024-12-04 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 82c397b3-c66c-33e2-8acb-85ffb72e1846 | -1.0461 | -46.5954 | 2024-12-04 03:10:00 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| af328122-6498-3ad9-8e2c-9001a0025001 | -1.6623 | -52.7599 | 2024-12-04 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 402a3e05-aaca-3574-8fc5-6e1891c9abd1 | -3.127 | -54.6063 | 2024-12-04 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| bf9a4df1-0af5-3980-9a39-a07cd339cfb2 | -1.7544 | -52.6363 | 2024-12-04 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 216.5 |
| fccbe002-81d5-3fab-9099-bb27539794a1 | -2.8196 | -53.0629 | 2024-12-04 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| e5508d93-950a-30d7-8654-3e3689e2a4cb | -3.259 | -53.6388 | 2024-12-04 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 05c2fb26-7af7-3f59-a88b-130e94e04594 | -1.7729 | -52.6156 | 2024-12-04 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 60d7e7cf-d0ae-3f84-8005-824a53cb8b8c | -1.0646 | -46.5952 | 2024-12-04 03:10:00 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d05fd27f-b685-3c61-9359-505fc45aa24c | -2.3283 | -45.4128 | 2024-12-04 03:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 6e49dc6a-bf76-349e-bcfb-dd1a01ed2d0b | -2.6428 | -45.7394 | 2024-12-04 03:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 985a7ca1-21aa-3b05-8609-efd8f5162c52 | -2.3098 | -45.4133 | 2024-12-04 03:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d18ef64c-346f-3d56-9953-49511e5109ba | -2.8196 | -53.0629 | 2024-12-04 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| eb63166f-0329-349f-9b29-d9f5811dedbb | -2.8012 | -53.0633 | 2024-12-04 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6be93d91-ed83-38f3-8595-582b45e5d6fb | -3.259 | -53.6388 | 2024-12-04 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2267be89-fd51-3b48-924c-84847725909a | -2.8197 | -53.0425 | 2024-12-04 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 977f3296-095c-3d39-af24-b68f53b556d7 | -2.3097 | -45.4358 | 2024-12-04 03:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 35a7d7c6-52dd-34e5-8bbf-7b1cc7c2367a | -3.1969 | -50.6428 | 2024-12-04 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9d28c442-fbb5-355f-a6ee-ccbb066bfcc4 | -1.6447 | -52.3725 | 2024-12-04 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| cd655db9-0d5d-360f-a6d9-013dd94b8b6b | -2.6428 | -45.7394 | 2024-12-04 03:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c5e395f1-1e97-37e9-b66e-238e8c7dd1ad | -2.6242 | -45.7399 | 2024-12-04 03:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 19182e28-edac-3a29-8a50-7d2f348cb749 | -3.259 | -53.659 | 2024-12-04 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7d69584e-c0e7-34c8-ba90-e369b3f78b6f | -1.6446 | -52.393 | 2024-12-04 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e8595733-b300-30e6-9c5d-909bbe5e17ae | -1.663 | -52.3927 | 2024-12-04 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 67d89672-6c43-3251-ad69-54bec9065ae7 | -3.13434 | -39.90569 | 2024-12-04 03:23:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a54ca29c-df17-30e6-838b-86890a0d958e | -4.98677 | -40.90694 | 2024-12-04 03:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86df3a66-eaa7-3f22-8bec-f7d755b7a669 | -5.23072 | -35.63892 | 2024-12-04 03:23:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b60dfc8-9fc7-3c24-beb8-398b9113b253 | -4.98718 | -40.90857 | 2024-12-04 03:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 01d53f8f-254c-3d24-9978-b65d359817ae | -5.23131 | -35.6353 | 2024-12-04 03:23:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4cbeca66-5bb3-38bd-bc48-0ae6d1bb82a9 | -4.98763 | -40.9021 | 2024-12-04 03:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 687df472-d8ab-33e5-b8a2-4eb350779d20 | -4.98804 | -40.90356 | 2024-12-04 03:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5dd3228c-cae0-38d3-978b-74122dd33bf3 | -3.13652 | -39.90826 | 2024-12-04 03:23:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5d32f831-502a-30fd-a9f7-074486476f0c | -5.11327 | -35.69447 | 2024-12-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ed148019-09d9-3782-9f26-26f14248fae3 | -7.44551 | -39.75293 | 2024-12-04 03:25:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 00d4a838-f894-3b41-bb5b-58dfbacaf178 | -13.80724 | -41.5767 | 2024-12-04 03:25:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4247c39c-7586-3fdb-91ea-fe964fe0952c | -13.4147 | -41.11319 | 2024-12-04 03:25:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b808283-3610-30e2-814f-fcd4963e1081 | -9.40072 | -36.02377 | 2024-12-04 03:25:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 0626369b-6927-3c42-92f1-dbd5e7a6a4f3 | -11.49344 | -37.48235 | 2024-12-04 03:25:00 | NOAA-21 | INDIAROBA | SERGIPE | Brasil | 2802809 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab7a1fe9-e32b-3615-8277-ffae5a92a713 | -11.24163 | -40.98257 | 2024-12-04 03:25:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7e98c96-bd89-309e-a019-d932e3e17beb | -9.33491 | -36.00721 | 2024-12-04 03:25:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2e28c21b-7bc2-30a2-b047-749bf1c1f451 | -11.24227 | -40.97927 | 2024-12-04 03:25:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b870e20-27fc-3d7c-8f3e-32fd9985af8c | -11.52993 | -38.01292 | 2024-12-04 03:25:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ea7d2424-8585-319a-8e13-baf0e5d04500 | -9.41416 | -35.94345 | 2024-12-04 03:25:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24d12bbb-7ea2-3f86-b55d-f24e54c074db | -9.33098 | -36.00657 | 2024-12-04 03:25:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c6eca0f3-d505-3cc9-aabb-abfdcd2b7dcb | -6.25535 | -43.56137 | 2024-12-04 03:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d77cf9cc-55b5-346c-9b3e-de459d099589 | -7.86366 | -39.50709 | 2024-12-04 03:25:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
