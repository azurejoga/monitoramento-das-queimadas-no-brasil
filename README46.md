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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4795413d-2f74-3de6-903d-c755d1f24d98 | -5.05637 | -49.86143 | 2024-11-20 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 868576bb-de7d-368d-b771-88cc6a46244f | -2.0268 | -51.1779 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f7ec38f-3184-322f-93d0-9adfe3d3adab | -1.63641 | -52.68021 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e39a73b2-4247-3700-bf58-a094cd01b362 | -2.33914 | -54.79015 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5aec0598-d1bf-32a2-b330-bffe3b9f7f25 | -1.83873 | -50.80154 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2fbc286-fcdc-3792-a072-2646762c2acb | -3.11547 | -53.70216 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a4aa296-366a-3def-a1ea-f117be2d0960 | -4.15404 | -43.97802 | 2024-11-20 04:50:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d811d94d-c954-3c78-9e9a-b37f82d42c33 | -3.98818 | -49.91305 | 2024-11-20 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e57321d2-cb6e-3f7a-be19-38b90ec6ddf7 | -2.63954 | -46.22019 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f48380f-c463-3ede-b6d6-e9b3b7ce4551 | -5.97481 | -45.36442 | 2024-11-20 04:50:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 203dbeb7-bca2-363a-b8b2-44c4f9edcf95 | -1.09279 | -51.7384 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26d9f2ec-43eb-3d7d-ac80-9c7fe395839e | -2.16088 | -46.38773 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f64e1a14-c1eb-3322-94f4-e78a635cb45a | -1.48164 | -51.97611 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b8c9a55-8005-3b58-acd9-1cfb25efde63 | -2.80569 | -51.79764 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ec33d45-bfe4-3ec8-b809-b22dfb0ac555 | -5.97942 | -45.36521 | 2024-11-20 04:50:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24fe079d-1d1d-3986-881a-6cc425af1c74 | -2.60441 | -48.21507 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6261b1d-56c8-386b-b4a7-ebc1eafc86f9 | -0.92383 | -51.65149 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebc53f92-da24-3dfa-9ec5-2923752ee061 | -6.2449 | -47.27304 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce2cd127-d1f5-3870-a248-bd424531d546 | -2.86286 | -54.03643 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 105fd6af-4a9f-3cff-b9e7-ee99d58fec08 | -1.38655 | -52.55753 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b768719a-4a9a-39e4-8375-1f65498b711e | -0.936 | -51.72052 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bf78019-6c28-3ed5-bf7a-c92f99dc7343 | -8.32312 | -45.11337 | 2024-11-20 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19be6334-86ae-3675-b39b-02cf40240e0e | -1.20832 | -51.77749 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 298af9ea-903b-30ae-9f99-c48187c06721 | -2.59619 | -48.29222 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df04378f-28da-3cd1-ad47-f52430d72268 | -2.4924 | -49.02914 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c94e619-229e-3300-b558-b48f1631bd35 | -2.77553 | -48.57741 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 327fd3a7-1923-3ea5-9599-8b107fa3677c | -3.28597 | -53.8358 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 321b565e-1088-30e7-b0a5-ed9a93595034 | -0.48675 | -52.08173 | 2024-11-20 04:50:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b557b9a-22b5-3d3d-83f6-4ad8c9cce2cd | -3.18273 | -54.31643 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37dfea4b-98d3-35af-ba1c-c393f8e0aebf | -4.13887 | -47.7342 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 394a9cc8-1102-3027-93d4-3795597d12a5 | -2.99865 | -45.4412 | 2024-11-20 04:50:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7d04813-d329-3cdc-8a04-a8060b8a75ed | -3.20204 | -54.33147 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2f3b466-d95a-3cee-97e7-5606d2067a2f | -0.96483 | -51.73209 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07f83ac1-aefe-39bc-b367-8e87630672a4 | -2.69226 | -46.07652 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf03b6a-1411-3035-a208-cd4fe3e91d6c | -3.63465 | -51.01968 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 791bfd91-abab-3888-8058-e9bf01ac8296 | -2.2814 | -53.63312 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a8020d0-21cf-3714-a37b-7c4047cad484 | -2.51454 | -44.99697 | 2024-11-20 04:50:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d90acefd-39c0-37b5-a7f3-d2c61ca280d1 | -2.76684 | -52.59878 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84f98321-fd50-336f-9fd3-2b243fcdb0a0 | -3.22249 | -53.84195 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c541f04-65e3-398a-889d-ec7803b3c3c8 | -2.11991 | -48.55164 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6a510a1-ac62-3476-80a0-fd699b2a1e2f | -2.64071 | -46.21275 | 2024-11-20 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb0cb818-7a14-398f-a1ec-a918f68b2841 | -2.56136 | -54.07045 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3432aa5a-607b-39c6-9c53-e8719ca75a09 | -1.38197 | -51.5534 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a62a2e56-7020-3789-90f6-2299dcb944d4 | -3.24052 | -48.78063 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1708163-081a-3437-bb63-0d2bbf4bd6db | -3.7768 | -53.96144 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f83379b-0613-3ac1-92a9-66e540a17636 | -0.92915 | -51.6345 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca256c50-e195-3141-93ac-20c7e344f9ca | -3.24145 | -48.43331 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 571d51bf-fd36-3ca9-9a4a-ca0eacfce325 | -2.80183 | -51.80057 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f19880a-184e-37eb-9096-da32ab190cb0 | -4.09025 | -51.0723 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3a3a061-5263-338a-80b5-23c24daa3ded | -1.15197 | -53.51535 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8defa7f3-498f-36c0-8089-6177558bca78 | -1.13777 | -51.68508 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70e9cc31-5661-31f6-bf63-0414f0de94f4 | -1.20717 | -51.76314 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c96bec9e-cfdb-3ec8-828d-197c708a385b | -2.24452 | -50.07714 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52076a70-904f-334c-8e41-5d37dc67d0b4 | -0.81285 | -51.60236 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b20e76c6-2c47-3591-8024-57d3a0927c26 | -2.53084 | -54.01395 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efb95d1c-a376-3ac8-839d-cd58ae7797d8 | -2.82218 | -54.02213 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0e9a3ad-8d58-3f71-b32a-28c9afd5bc48 | -2.49302 | -49.02522 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88af43ab-79a7-39d4-ad12-e003b8cf31f5 | -2.72883 | -49.34375 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82114b80-ca06-3bf3-9173-a481eff1b779 | -3.88368 | -52.23584 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b9286e1-9251-330d-90ce-b1e25b37464c | -2.61128 | -54.05414 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52aa0850-5631-3824-945c-d776ee64348d | -2.73825 | -48.65149 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85576de6-2205-3744-8ff5-9e8b542b6d02 | -5.44402 | -45.58094 | 2024-11-20 04:50:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a8727bf-66ac-31c2-9cba-d463d2269eed | -3.59512 | -43.62399 | 2024-11-20 04:50:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac49f60c-fd6d-3f1f-9ffc-4529d9da1f5a | -1.61895 | -52.41298 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dca66da-6bc8-3c7b-8812-f584129eb666 | -2.38419 | -49.85403 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f2c33a2-f961-37cb-8857-b156ca307c1a | -3.41402 | -51.6526 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d54162-6ec2-38d3-bfc5-bf22c25f0d99 | -9.17546 | -44.71803 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39e6cc56-2dc1-3722-b397-a6f808b82c79 | -1.39044 | -55.62676 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 338c3e28-fa05-39b9-8da2-6634b4fc61dd | -1.53383 | -52.02732 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0f85ac6-7240-3691-897e-62363979fb7c | -2.90374 | -53.05636 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 22feef6d-ac1d-350e-9b4f-7f1361498dba | -2.78723 | -51.7206 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc9c627d-bab0-3341-b102-621fc32e7a73 | -2.78391 | -51.72009 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f843ae5-df45-3f6e-90e0-df6db8707b4a | -2.59923 | -54.01255 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c59c2c0-38e5-3081-a056-1e9f6da38546 | -2.92962 | -53.06783 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d84e64bf-463a-3942-80ec-ae59e6d61665 | -2.7861 | -48.60428 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf9f8d4-9933-3acc-b7bf-626744652781 | -1.14665 | -51.69354 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 751c8c17-6356-311e-b8f0-d632eb4c203c | -3.11143 | -53.70534 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4846536-fbed-3e7e-940b-c444ed7fa099 | -5.5134 | -46.44329 | 2024-11-20 04:50:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 601b69ba-0a2b-3a77-b669-d6c9deaf3019 | -3.28761 | -53.84762 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a11cf769-19d3-318f-9376-87e23891d763 | -1.14387 | -51.68957 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d30c060-ae99-3d65-a150-f7f44a10a012 | -4.0803 | -50.03696 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df0a370b-3379-3d7a-abe2-678dae4ffc82 | -0.90898 | -51.78369 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d439119a-e37b-3f41-b331-70a93e1521c9 | -3.88561 | -52.37442 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1781fc2-9edc-3f9a-ac43-a22d6026c722 | -2.64795 | -46.14367 | 2024-11-20 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1f7d15f-d045-3ca0-ab74-075ba38da911 | -4.63003 | -49.54169 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca6a4376-7fb5-3e87-901f-361a715b1683 | -2.27974 | -48.41096 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 994488aa-4517-3fca-8a0c-8de647e7c8e5 | -3.10566 | -53.1058 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f615b00d-94f5-3505-973f-72bc8abe3122 | -1.25104 | -52.04362 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9387f953-1992-3892-9ebc-c6b472fca76a | -0.90565 | -51.78318 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ec2fd66-d483-3b1d-9416-feac5f3912fa | -1.13194 | -51.68431 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdff2ebe-7586-3199-8c86-31ce555676e6 | -2.13148 | -49.502 | 2024-11-20 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac5738ea-0cc4-3c8a-8a4f-c1fb98f7c4e7 | -2.59345 | -54.00372 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7289ac9c-b59b-39e8-812e-5851c70df7ff | -1.43273 | -52.28648 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30690c53-9f95-3b6f-9a6c-34ab0c5b2a75 | -1.35021 | -51.43568 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71a2f558-6a6c-38bd-bc99-8b01cd75e82c | -4.46294 | -46.58787 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e69830be-8d2b-39ef-97e5-c633d8218b79 | -2.74607 | -51.83073 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 17b9ee58-a0d2-3958-be2a-f89848bb9855 | -4.1206 | -46.85201 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0e5ca76-c4ac-3ed9-ad30-5e8d64f8b09a | -4.06306 | -46.84758 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d88d2faf-a8d8-3a3b-9c96-2ec30203723b | -1.85959 | -47.82476 | 2024-11-20 04:50:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a465845-f59b-3967-ac01-3b9d554aed29 | -2.26562 | -45.46017 | 2024-11-20 04:50:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README47.md)
