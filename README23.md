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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b99beb8a-fdb7-31c9-b9e9-88de18bf0cfd | -2.82072 | -51.79258 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ff443ff-b14a-30b1-b410-372377c23b10 | -7.57635 | -49.40639 | 2024-11-25 04:33:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1a8b7c6-138f-3d4a-955f-ac4afe9966d1 | -4.04256 | -46.6879 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cad6b6e4-dc00-3d4f-aa62-c97b5cbed8bc | -3.28184 | -53.00983 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 442b36cb-e7c8-3e84-b9c6-596598d533d6 | -4.49685 | -49.64351 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 646999f5-ab44-3f9d-9f8c-e47729979b1a | -2.62144 | -46.20261 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ba3490-0698-394d-b3d2-7ecaa6280b26 | -4.23739 | -48.64225 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 797da247-3ff1-3eb2-be62-7e7caad96d19 | -3.04524 | -51.44647 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab05227a-7ea4-358c-b83f-5603066263b6 | -3.10155 | -54.00038 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 429225f4-bb29-36ce-b9f6-2a7d5e31907f | -2.70684 | -46.11488 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4638db00-a1f1-385b-882d-fdce420ad0f5 | -3.8911 | -50.07222 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e763ba2-321a-3b3d-95dd-3a36dcaef35a | -3.53835 | -50.44326 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bce390f8-bec3-32b5-961c-0eabe1ed618d | -9.02388 | -47.7579 | 2024-11-25 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01e9a390-3bed-3b24-9476-b29fdf738404 | -4.30474 | -46.57393 | 2024-11-25 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00124348-ac66-306f-85bb-bba034119aa8 | -1.44175 | -52.44475 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3e3dff1-db55-3dfc-b9ce-3b967f42f720 | -3.25295 | -54.23208 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 989dbd08-e8af-32f5-89d0-a6daec60ce53 | -2.61919 | -46.19508 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4485ff26-bddf-361a-a463-92a7bac154e2 | -1.73292 | -52.32267 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3438adb7-7713-3e8a-9735-de9e30d94750 | -4.01772 | -46.19227 | 2024-11-25 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4e5a45f-d5fe-3132-b901-8b1cf78ac0ee | -1.60158 | -52.52317 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ae91c6e-d582-3a59-8429-0ce11b1bb3a6 | -3.9505 | -46.90868 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66d7a446-9c2e-3e5f-8ae2-7b5a0f319df9 | -3.3354 | -46.62099 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e7e2548-ea02-3e66-8065-2540f743db32 | -3.06149 | -53.21537 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 02486e7d-cc3c-34ef-8eb4-d4078036086a | -3.24521 | -53.28453 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3119d5bc-5504-3d08-83ed-3aaea9656095 | -3.50158 | -50.46687 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 456dbb81-7e4f-3b69-9bc4-5aa6752c3f0e | -3.84 | -46.63475 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc9891f3-d7c6-3ef5-856e-0bfe203aa62e | -1.64102 | -53.87136 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 908fb73f-8266-3a67-8cd1-338aaba0a566 | -4.07522 | -46.82827 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4de95ce3-94d1-3e6b-9092-634de563b6e7 | -2.81435 | -54.09384 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 075e441a-a2de-3f56-b080-023e9362148c | -1.61576 | -52.5792 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f253598a-5444-3477-b20d-8298ba5f4a3d | -4.24802 | -48.70512 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 391bbc80-5f1c-3f58-9a0f-3baca172c099 | -3.69435 | -51.36848 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6d15aca-bceb-3770-a8de-81f152518366 | -3.84906 | -49.89971 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bd9daad-3a58-36d5-abeb-542d8df394b8 | -2.71722 | -46.26444 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09bb8e2a-8a04-3c72-95b5-ad838e6eb844 | -4.04643 | -46.68493 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f59579b2-c0ca-3599-8ceb-9cda654ae33e | -4.51122 | -50.77169 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5573dfc-a166-3637-b71f-7e7f0f321126 | -1.77214 | -53.62833 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a0d7733-3bb3-3bae-9530-d86c3b626fe5 | -2.69 | -46.26693 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02c4544d-36b7-3361-8563-40b6431752ca | -2.65442 | -46.25431 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb7bf3ab-df49-3b5e-a562-507b35c29bd7 | -2.70569 | -46.29494 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f6354a4-7793-3379-a847-735f01418d8a | -3.67481 | -54.58618 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd18bc28-8de3-340c-823b-689b66eaa179 | -4.23964 | -48.67138 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6bbc8cc5-7e2a-3d3b-b463-50a11ca4f414 | -3.71009 | -52.41351 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 85ec3666-b684-3b23-970d-b1e3e204f699 | -2.70903 | -46.29545 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1497397a-dbcd-38b4-89e9-86e0c31ea92e | -3.15504 | -46.59988 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6736f87d-d54f-374e-a6c9-92f199976faf | -3.61327 | -54.21379 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2be87baa-3550-32c4-b02e-adc49cea085b | -4.01947 | -48.07982 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f647e26b-9053-3c1f-8e61-4c8ebc7844c5 | -2.93917 | -54.07848 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2abaa93a-c96a-34db-bc53-9d634d8a4ae5 | -5.58697 | -45.20858 | 2024-11-25 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1051016-fd5a-3d10-90d8-caa780509711 | -3.77524 | -51.91101 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57a4a006-97ff-3be4-97b2-9c44ab900cd8 | -3.72368 | -47.12054 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 310637e0-5ea7-3aa1-acf1-1ded499910d7 | -4.05162 | -48.30909 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 901acb18-d6ae-3e36-9a8b-4be66351b408 | -4.24523 | -48.70107 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ebdcbe8-ad1c-35fd-bd1f-706e2e62a393 | -1.63281 | -54.46265 | 2024-11-25 04:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 239aad1e-c8b7-3ff6-8878-644588edb3a0 | -2.53201 | -46.40718 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f6e850-f0a3-3ed6-8028-100c9cd44583 | -2.55709 | -46.55309 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5279dd67-c5fe-30bc-aea2-38f1030478de | -2.80037 | -53.00576 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84d22d94-35b2-345c-a7f9-7a9a2d8b070d | -2.33609 | -52.18012 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4529b5fc-40ca-36c5-8cb2-de3dd1d30fc4 | -4.29438 | -48.23659 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72fd1de9-f34b-33e4-87cd-378978ad7ac5 | -3.81278 | -51.38024 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afe40437-e64a-3ef3-af98-73599f6648a8 | -4.29502 | -46.90173 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 34f84183-d969-329d-a9b6-f11d31719194 | -3.10328 | -53.73421 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33598823-c6ad-3d1d-a9df-2cd13559dd01 | -3.24689 | -54.24067 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a08f500-cbe1-30b8-a71b-b0fb0e6667fc | -3.14185 | -46.61919 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f1b46a-a9fb-3669-897a-13f5a85ae020 | -1.75988 | -52.70413 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b982401-675a-37c1-ab21-64e25295b34b | -3.71766 | -43.8704 | 2024-11-25 04:33:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 872426a4-19c0-3f01-ad7a-bb5e3d20b829 | -3.39472 | -44.74346 | 2024-11-25 04:33:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57c2387b-1326-308e-b9c9-12c78ef64403 | -3.93673 | -48.15194 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 962e25df-d9b3-343c-93ca-4517ae41250a | -3.50743 | -53.80322 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27735762-78b9-3699-96d5-c4dbede37a71 | -1.13211 | -54.17829 | 2024-11-25 04:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d62a347-40d9-3f6a-a284-a5ac06ad96b0 | -4.27263 | -46.43146 | 2024-11-25 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 521e8409-a7d3-3bb1-8b98-46453ffcb3a6 | -1.62806 | -54.46183 | 2024-11-25 04:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ef7204-626b-31cc-86f8-928791b9a09e | -2.61916 | -54.25327 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 664ea01d-772e-353b-b469-66442e1221f5 | -2.7007 | -46.11033 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13737b98-0b4f-3628-bb64-8be4bd5af366 | -3.95381 | -46.90919 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51c02909-0ede-37ec-b94f-787fe6edcf14 | -3.96044 | -46.9102 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f510bea0-d8e8-3ecf-bd28-6864da2768a9 | -2.67633 | -46.15707 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5fcf766-a54b-3777-bb62-581cda3f3703 | -1.80781 | -50.90585 | 2024-11-25 04:33:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb6c713b-1bcf-3474-b5f7-74f9dc7d6103 | -1.60323 | -52.57728 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 617d64d3-6d5c-32f5-a194-cf7f5985d639 | -2.71623 | -46.29298 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a171e0f6-92f7-3e07-a499-309400c319e0 | -3.17366 | -46.54578 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e110db97-d290-3379-88a0-700f5fc3d0d2 | -2.80458 | -53.0065 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a954e3b5-75cf-31f6-bf2b-f2ad187269e5 | -3.61967 | -55.30054 | 2024-11-25 04:33:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ee5cdf2-1bda-360d-ada3-14e0124f212e | -2.33665 | -52.17667 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f57f9c1-08b0-3b2a-b155-f5f07d5a72c7 | -2.69502 | -46.27846 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cc1ef1a-3f7d-3d1d-8760-81640200c665 | -4.25471 | -48.72786 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e15ffb4-a66f-3d34-bc81-916407cab163 | -3.52791 | -53.81612 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65f49f4f-6960-311e-94ea-92d0c7765083 | -4.17836 | -48.75584 | 2024-11-25 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bcfa83d-7b9b-32eb-8023-162bcc636b96 | -1.46708 | -52.69116 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dffd949-d5c5-37b3-b82f-1b9539488558 | -4.42075 | -43.9689 | 2024-11-25 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa97c020-69c5-3f2e-afd9-ad635922ee48 | -3.00285 | -53.23169 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c239db6-db5f-3265-820b-50ab04503f3c | -5.55007 | -45.33193 | 2024-11-25 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d2c842f-3834-3203-b1a2-11536fc64bef | -4.1817 | -48.75636 | 2024-11-25 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f2ee52c-498b-3e1f-87e3-67327b00d9d2 | -1.69208 | -52.61054 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8d41843-339d-3271-abdb-3593f5cb008c | -3.93341 | -48.15142 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23b6771d-1c93-3049-b668-1cc99b770543 | -4.51408 | -44.59348 | 2024-11-25 04:33:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 672cb116-6a9a-316c-8ffb-71cac5c68f49 | -5.91254 | -45.57094 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13b69edb-f23f-3df0-80a1-340cab9d872e | -4.61366 | -45.81146 | 2024-11-25 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70fcda8b-63ed-3050-aac6-a2cef3388042 | -4.79665 | -48.99813 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d023011-c95a-3a06-a687-cfa5656c9aa3 | -2.68557 | -46.27342 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README24.md)
