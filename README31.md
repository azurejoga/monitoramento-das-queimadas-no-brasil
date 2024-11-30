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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a4ee5f1-1ff6-37a2-8785-d6a975b5b999 | -3.57266 | -52.00871 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4564beea-bc00-3ac0-bbb9-11e0916e3de1 | -2.82569 | -45.28888 | 2024-11-30 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80585292-0f97-3ef0-9a30-2cab77d44ac1 | -3.26862 | -50.56177 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 612ed757-af9e-3ffd-8c50-aa959f1083b4 | -1.71528 | -52.62654 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 485402de-24da-3f02-87c6-8a254e23ab13 | -2.77341 | -54.0472 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26985cc5-cb02-3143-9c03-e27165fada14 | -3.0997 | -53.72869 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 553ea805-5df2-3e02-a96b-6b80f216d526 | -3.58987 | -49.99014 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af238e9d-1882-3291-b9bd-4d422e0a5d43 | -3.8167 | -46.54337 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73f507cd-167f-39bf-a74a-4df9c44493fc | -3.05719 | -51.30179 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 765231d5-9862-3088-9303-f1cc04060924 | -5.18351 | -50.47457 | 2024-11-30 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fe8d32f-e112-353e-aab4-538fc53ed0f2 | -2.61807 | -51.76337 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df16b694-8481-363f-bdd9-d55cf74f3fb9 | -3.46521 | -53.87826 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 42dafcf7-214c-339e-935d-fab4c3a67c87 | -3.33374 | -46.69326 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96e14d00-8699-37e1-97e5-034fe8c3643c | -3.49879 | -50.2862 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ed3122a-f0c9-3f4a-bde7-21ad0d3f72f3 | -3.44195 | -50.02111 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87279ab9-2b7c-3749-9295-9db95ddba3ed | -4.04953 | -46.8258 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a78a2a0-5eb4-3c27-9d52-14868a02b4eb | -3.79573 | -45.85497 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e079a643-574f-3a9e-87b1-e53e8abbb733 | -3.28122 | -48.76795 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 742ae012-6398-3ba7-9cbc-e3b2d31d5b37 | -4.05159 | -48.33927 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da37e9e2-ce2d-3b7d-a47f-4033e7e9bbb3 | -3.26482 | -51.27496 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6c676f9-1f5f-3ae2-b352-368ee48790bb | -3.12116 | -45.97955 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c42c55ef-39d5-3fe7-8d38-facba7044171 | -3.70157 | -45.68681 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0247dd99-4679-365e-b4aa-7317fd6c0a52 | -3.54286 | -50.18072 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce2b6e80-bdf0-3701-8331-5df1246fde51 | -2.71313 | -48.67878 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b6c52e5-cc6e-3734-9075-0026d061fc73 | -1.33378 | -52.38885 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e2b16ec-1364-3bda-a1bc-8ea0c0ed1b29 | -3.84601 | -46.52288 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4ee74457-cbc1-357d-8be2-c994efb73024 | -3.96781 | -46.90378 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c43bd6b2-9057-33be-a0ca-ded20d702da6 | -3.03527 | -48.51088 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c90037e4-cce5-3333-859b-30cf6e759945 | -3.02285 | -49.52705 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9188cbae-9de7-34c3-b7b3-77e839d7c075 | -3.16728 | -46.54751 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adbb534f-f4a8-33e0-8e29-c9ba30f23734 | -4.12088 | -48.52789 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b75f308f-0a54-3884-898b-cf33fe10383d | -0.99771 | -51.71637 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3afce2c4-abcf-3c94-89bb-ec32f9a3dfb0 | -3.01697 | -47.79578 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3e1d09d-b9c0-3c7a-b7fd-bdbf68ff6a4b | -3.22775 | -53.63251 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54259cbe-91da-3db2-a57b-52f6510be768 | -3.04795 | -50.27441 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb28f682-f92a-3662-9249-f300ee8b900e | -2.68268 | -46.09809 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3603d183-3caf-337e-a6f0-4cef3ce6922e | -3.21706 | -49.2224 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8c68efb-0fb9-3f27-a653-d27db6c50e55 | -2.70045 | -48.67331 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb38e61f-e9c9-39f9-b93c-f1ad18a8dbeb | -3.85339 | -46.66328 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e140348-eb56-3cbb-9f39-8c7af0636b89 | -2.12368 | -46.41705 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 768470e0-bf7a-356d-8423-755f53c23cb7 | -3.5932 | -49.99065 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a489fb1-2fcb-3048-b213-79268aea1627 | -2.60665 | -54.20402 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d4d802a-e772-3253-ad1a-99001455ed33 | -2.5219 | -48.46568 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 05125465-0d38-30bd-9b9a-86f2847aa111 | -3.93957 | -46.90334 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c5c1f7d-885a-37a6-98af-0fdfada34581 | -3.39015 | -50.34964 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8f59752-f882-377d-97e8-29372965449b | -2.61935 | -54.07085 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ff67b3c-987a-318f-bd5a-9ebf1b88a68c | -2.72959 | -54.13966 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 989562c5-eeb7-34d1-bea4-2d54cdcce380 | -7.9708 | -50.68447 | 2024-11-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 105475a2-2df8-3fe8-b981-2c935ddf6b4f | -2.70857 | -46.18998 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69b12080-151e-3e46-9943-14c6c2e965fe | -1.71077 | -52.63054 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f1680921-850e-331a-b877-958f30f1fc8c | -2.63157 | -46.1955 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b005d01-2812-37a5-873e-9afde79ab555 | -3.30027 | -53.83257 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00d26601-3aad-372d-96fd-127d85dcef54 | -1.32268 | -51.67815 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39b7272e-d817-320c-9509-f1114439d807 | -3.48262 | -50.21484 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9bddd4a-6d60-3e8b-a930-01e80874205c | -3.23642 | -50.24893 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee8b71f5-b91f-3902-8bac-9f0f778a72fc | -2.44901 | -53.62203 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 828726bf-a5c7-3ceb-a6b1-66d1365e78c6 | -3.88997 | -46.68078 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6443853-342f-34c3-bc4b-2e93d563ac9e | -4.00335 | -46.94322 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30b27c54-e752-3d83-a204-7a98f24ed8a5 | -2.41364 | -56.43909 | 2024-11-30 04:40:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bffdbcb1-40e3-3721-a700-b6bc0a3a8f45 | -2.97618 | -53.92631 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 300d4403-6cba-3dcc-a10b-1c918a0f53fc | -1.68898 | -46.78092 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| adbffe34-c33e-38c9-9eb9-2d0aed7d390c | -3.41922 | -50.16534 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 066eda90-ced6-3f89-af25-66d4e0c2b5ec | -4.06749 | -49.06695 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d0038c0-303b-35bf-99a7-6696a3cd60c2 | -3.14837 | -49.41983 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c386dcc0-81b4-3d82-aaab-eb6a90642d44 | -4.91034 | -49.89871 | 2024-11-30 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 949740f0-cdaf-3c1f-92b1-f4b2480f3bfe | -1.34026 | -54.99194 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ece8319-7f19-3c46-a337-66d9ddb16ee5 | -2.28018 | -46.4291 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7d5dfb0-8e49-3c88-9f64-a297679bfd58 | -3.94359 | -46.92327 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 456d387b-f460-3063-8c9e-1dc82976e74c | -3.44256 | -59.2879 | 2024-11-30 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed2f91a1-5c3a-32a8-a334-0e97c21ba7ab | -3.59818 | -49.98067 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6b5b77c-e771-3a2f-ac8d-bc95d77c1dd2 | -1.28323 | -51.74004 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2afff23b-3201-31df-b766-04b8a6825887 | -3.05043 | -49.37218 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 272ecf93-1ade-352a-9fec-d121fbf1c13c | -3.23697 | -50.24539 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ecd4e9a7-c2cc-3964-80e0-ab3c670990b2 | -3.3755 | -50.1218 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb9aba3f-de1c-317e-addd-8755a420f17b | -1.19481 | -51.7748 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a8e8ac4b-7be0-326a-951a-02946385879c | -1.71381 | -52.6357 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a41a4105-7fae-3dc8-a580-18f4b72c7123 | -3.62677 | -42.73954 | 2024-11-30 04:40:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fd67db1-e781-373e-8d6f-529357678643 | -4.09036 | -51.11654 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 583162ca-6542-3268-aa17-c456d5ab091e | -4.02524 | -46.98503 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9082d15f-3095-353b-ac52-83848882d5d2 | -3.9376 | -52.14973 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3facf22e-c43d-3d78-b43d-7fd102c597ac | -3.15284 | -53.82034 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b108dee2-b1dc-3979-9821-290014296e0e | -5.63141 | -46.54119 | 2024-11-30 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77dabc11-1464-3973-894c-8d5afbfa6ad1 | -2.23808 | -47.13601 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9612e9c8-e5dd-3228-aa52-0347f5cc9449 | -3.29355 | -50.35966 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0243c968-8bf0-3451-a5d5-220479a02633 | -4.08764 | -49.74388 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5f36583-b697-38d4-b7b1-4585c3ea6093 | -4.87949 | -41.29567 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3962b76e-0dc5-3168-b47a-440ba26458e1 | -2.02004 | -48.06292 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be8850a9-ce72-3667-8e60-e97aba9ded98 | -5.31028 | -44.7157 | 2024-11-30 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39acd883-7098-3fcb-8fd4-234f1f471d10 | -3.14176 | -53.71964 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abb6546c-c80c-3a20-bfe0-bf987aded34d | -3.68291 | -44.70436 | 2024-11-30 04:40:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28d371ad-5f6b-36d3-96a2-d6ae18fea1fd | -1.19934 | -53.86865 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56cb7ecb-7d0c-3256-ae4f-88cd214db9e5 | -4.04662 | -46.84494 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61a52a23-6c9b-3eff-9521-3ab00a516a1d | -4.10384 | -46.9501 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92701210-f9dc-3e0a-b3ae-4f3e4f00a5ad | -3.33879 | -53.20647 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e2456ce-c3af-3c48-b2c3-43a2aae79185 | -2.0715 | -48.14865 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40fed789-8b26-31dc-85ce-995b077114cb | -3.10397 | -50.35613 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cc6e184-d925-372a-bcfd-3f77979adfba | -1.45638 | -51.49752 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb863113-61c0-313e-b00c-ba381e303ad1 | -1.2676 | -54.55026 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d9daa3c-b09f-3077-91a5-cc9013a9dabc | -2.71885 | -48.59876 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abb22a95-638a-360b-802e-0ecb992f7db0 | -2.60381 | -54.35673 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README32.md)
