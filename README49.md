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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2cd3408-071a-3df1-85a6-062ccea583e3 | -21.34276 | -53.37495 | 2024-11-27 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4e42601-27e6-3afe-aed1-0bcb941a7c8d | -22.5372 | -48.8132 | 2024-11-27 04:25:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d71fbf51-d9bd-3d37-bc94-486f4e6045fb | -21.34344 | -53.37127 | 2024-11-27 04:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7f7cb22-87bb-33ac-83cf-1e83124a93a2 | -22.1065 | -49.61145 | 2024-11-27 04:25:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6a58b4cf-0bf2-3aa4-a0ed-4c00c20148b7 | -29.62565 | -51.96614 | 2024-11-27 04:25:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fbcb8c9d-c8ff-367e-84c5-064d57de2bf4 | -20.97523 | -47.21273 | 2024-11-27 04:25:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d1adab8-3051-317d-85b5-4034653f3f6f | -22.10586 | -49.61531 | 2024-11-27 04:25:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e80421e8-9b63-3099-b23d-2b08cebf3210 | -15.88895 | -43.45239 | 2024-11-27 04:27:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| aae1aec4-ab5b-3ebd-9c1d-30e0eb7f40e8 | -3.0949 | -53.2588 | 2024-11-27 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 4c98426a-74bd-38e6-8b14-330032f403cc | -3.0393 | -48.5082 | 2024-11-27 04:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8271461d-b2cb-3a44-8f03-d5abbc076417 | -2.8346 | -54.1326 | 2024-11-27 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 127b9a87-b048-3bc9-9c9c-3414402e6077 | -2.1928 | -53.7839 | 2024-11-27 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5ac2c7a6-29fa-3263-9e7a-f22ddb198a7b | -3.1691 | -48.4394 | 2024-11-27 04:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| b371fa90-d01a-3370-b011-898a3ae14286 | -2.8163 | -54.133 | 2024-11-27 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 1f5025a5-cf8b-3e0d-9439-7175b3367a88 | -4.2114 | -50.899 | 2024-11-27 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 292f235d-e0c2-3fbc-8b81-d1ca60440036 | -3.1133 | -53.2381 | 2024-11-27 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2a20ce90-6387-352f-bd32-e3d6ca4c7299 | -4.2115 | -50.8782 | 2024-11-27 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f53fad27-c871-33b1-ae5d-b55327afb188 | -3.9674 | -48.0851 | 2024-11-27 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c81cc38b-557a-362e-b829-271bae350b6a | -5.9788 | -45.3621 | 2024-11-27 04:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 342b2700-f14e-38d3-9af7-251ef6b76229 | -5.9975 | -45.3607 | 2024-11-27 04:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| bbbcd163-eeaf-365f-abe0-cdf36ff3b6cf | -3.1876 | -48.4387 | 2024-11-27 04:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0972697b-2f86-33e7-882e-0c9742e09cb8 | -2.8347 | -54.1125 | 2024-11-27 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 5bd2c05e-ccad-38a0-afed-3ab61d3bf8db | -3.9675 | -48.0634 | 2024-11-27 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| f04dc4f6-d663-308e-be48-c6ab67effc76 | -3.1133 | -53.2583 | 2024-11-27 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 774bc0dd-3918-3608-a02c-aadb95499271 | -3.0949 | -53.2385 | 2024-11-27 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2db9cde4-9f43-3b57-945f-220c89e273f2 | -3.0949 | -53.2385 | 2024-11-27 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| ee066ae6-f834-3ae0-a88c-2f0d71d9d83f | -5.9788 | -45.3621 | 2024-11-27 04:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 29bbb95d-73bc-34ed-95dd-d69e1b9b1e80 | -2.8163 | -54.133 | 2024-11-27 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| ec22f9d3-87a9-373e-8689-c15ee4d545e1 | -2.8346 | -54.1326 | 2024-11-27 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 28e0d756-2a66-36d7-8885-1538f90c2b1d | -3.0393 | -48.5082 | 2024-11-27 04:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 609c15c9-6ee8-3906-81d1-07c64ac75379 | -2.1928 | -53.7839 | 2024-11-27 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0c5c954d-a1ca-3661-8a06-526a226b7e81 | -3.1876 | -48.4387 | 2024-11-27 04:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4b1ce60a-4fc1-359b-b30d-f67ba7838bab | -3.0949 | -53.2588 | 2024-11-27 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 71837541-bd11-35fb-902d-c2b6de94f367 | -3.1691 | -48.4394 | 2024-11-27 04:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| dc8fee1c-b764-362e-a7f6-c34b65ccfd2e | -3.1133 | -53.2583 | 2024-11-27 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d6066e52-58df-3512-87a4-45dfab4a5603 | -3.9674 | -48.0851 | 2024-11-27 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a7c02ddb-fbd0-389b-9fca-82fa09047eec | -5.9975 | -45.3607 | 2024-11-27 04:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| ae6ae03e-b042-3991-81d5-9a321f743fd8 | -2.8347 | -54.1125 | 2024-11-27 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 93961b12-1d4d-3538-81fc-e5beb3088240 | 1.35836 | -50.62121 | 2024-11-27 04:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49e24571-50e8-35c3-b649-b1ddbddfadb9 | 1.36453 | -50.6166 | 2024-11-27 04:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70c47849-0e7f-3b28-b7d6-459cee2face8 | 1.36734 | -50.6125 | 2024-11-27 04:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee702325-46c8-3724-8b94-cd765fdb88bb | 4.27033 | -59.97787 | 2024-11-27 04:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c2e222e-fad5-3f9e-9561-868b2fdc0780 | 1.36117 | -50.61712 | 2024-11-27 04:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9d74b42-fc6a-3e5f-b504-fcb4e97e8ce5 | 1.36172 | -50.62069 | 2024-11-27 04:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad057194-26ec-3521-8e00-513e794b9907 | 2.08626 | -50.64183 | 2024-11-27 04:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6057a7d-b059-32c9-ad71-e3906be7fbc1 | 1.35892 | -50.62478 | 2024-11-27 04:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 543707b2-5183-3bf4-98e8-1f8a9cd3dca0 | 0.98317 | -50.06685 | 2024-11-27 04:40:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34bbc774-635c-3392-831d-9c70056314df | 2.66783 | -50.90549 | 2024-11-27 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bdf1eced-97ef-32db-b900-7c5634b24410 | 1.16003 | -50.6989 | 2024-11-27 04:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c860092-2776-383f-b07f-b7f5149c255c | 1.35555 | -50.62531 | 2024-11-27 04:40:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27479ac5-f3eb-3597-b9ad-9ddc34d37400 | 4.27185 | -60.66053 | 2024-11-27 04:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 449dbdfa-191a-33fc-b185-a2237b871def | 2.0778 | -50.63206 | 2024-11-27 04:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83e70b45-7bdf-3f05-8ed4-6af0cd99f501 | 0.97861 | -50.12448 | 2024-11-27 04:40:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f755641d-7b42-37d6-b9b8-d71402d8405b | 2.0857 | -50.63823 | 2024-11-27 04:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eda0eebb-2223-32b0-ac52-294f4001658a | 4.27092 | -60.65388 | 2024-11-27 04:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19adca40-cdb4-3ef3-99c0-1cda0381be12 | 2.07442 | -50.63258 | 2024-11-27 04:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49c06d9b-5441-306f-ba8d-cdc4bfec64ab | 2.08175 | -50.63514 | 2024-11-27 04:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6baab2fc-510d-3357-b716-3313d11b21a7 | -2.30751 | -51.3264 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 923ee2da-85e8-3c01-bb1b-698eb53b8b82 | -3.81096 | -46.60733 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a268b9a5-83f5-3245-a5d0-1c718109dbb4 | -2.83516 | -51.84935 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d15cfded-ff5f-3db5-9be4-fe16f8fdca56 | -3.09603 | -53.27126 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 002735ec-9c91-345a-a2bb-bc4ce1b63fd9 | -3.41219 | -50.20513 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e4f1cf5-130d-3270-8cef-0e5b3905ea19 | -2.83963 | -46.84277 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9b95fa45-ce51-3be3-bb12-a35fb54ff6f8 | -3.09611 | -50.35563 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ab6229a-c19f-30b2-ae45-f1235b63db01 | -3.11329 | -51.26018 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b6cf57-05da-3c88-bb3b-a273f06635fd | -4.27322 | -48.53796 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3393aa76-5fc1-360c-9be6-77bcdf1143f6 | -2.95757 | -48.61624 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 178f9468-bec6-3626-913f-ba80ad4dd208 | -2.80677 | -54.13663 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6213c0e-514b-383f-9c09-6a7b2114ad1b | -1.42783 | -52.44218 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f635f18-99e7-35e5-b821-abcbfde80018 | -1.67867 | -52.43866 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7abeba8-d7dd-342c-86cd-7c322a222326 | -2.9249 | -53.91286 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 040d51a0-3076-3c25-b2f1-de60440bf8d6 | -3.11659 | -53.25761 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2996ea0d-9212-3983-b371-5cb2ead7f29a | -2.84892 | -46.83438 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91d51043-a82a-35fa-a260-62ddb60a6619 | -2.397 | -48.96792 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6266c02-ff65-3e53-9402-119857f980bf | -1.73321 | -54.53626 | 2024-11-27 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11d9cc11-e18d-3422-b425-ecf451ef7c94 | -3.90711 | -50.59973 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7197eae5-641b-388a-9014-7186f1481d43 | -2.50256 | -52.15382 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2593f45-51f2-37d8-870b-2f948bcb4b1f | -1.45103 | -52.5944 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ca83a595-ec65-3158-a663-1e290c72e0c8 | -2.59548 | -51.83163 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2703496e-7edf-3b6a-9b38-3522f8de3e46 | -3.17483 | -48.43721 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 85adb2b7-9c5c-3f18-a09f-7b0286e852ff | -2.1146 | -46.45454 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5916640a-532d-3842-a3d0-dd1516e6dccc | -3.97838 | -48.086 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e158b5e-8d49-348b-be6d-e86e8be8332a | -3.58525 | -50.3765 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73ca083f-af50-3f51-a6df-194f00df1e1e | -2.00221 | -51.17337 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 323634cf-1066-3cf1-8c6b-9e58abd2eb2e | -0.19799 | -50.2478 | 2024-11-27 04:42:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23a730c5-426d-39e9-a52b-dd02fd3c3155 | -4.30704 | -48.18142 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d292126d-bba5-3d49-bb26-a388dd4e2ec0 | -2.00634 | -48.53412 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b8c90a2-c70e-3410-89c7-cdb10a9aa686 | -1.46918 | -52.47992 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bb96a92-ce95-3af5-895d-88b5e30fd4d4 | -2.69697 | -51.99004 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7d75df7-28a5-3000-b24d-b0abeb98201b | -2.21504 | -53.79097 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c477cfda-45a8-3b8e-8590-aaf43fb2695e | -3.4769 | -50.31025 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1eabcbf8-1a8b-3d26-8881-a53499441741 | -3.81619 | -47.46891 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef08037e-24f2-39c0-8e7e-2a854e060db0 | -3.5182 | -50.22171 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 814417e3-728c-3158-98c2-572ee04aabab | -1.50685 | -51.15062 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e9dd878-420e-300b-bb02-ee6eca6e5062 | -1.27778 | -54.54741 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b76d9b1-4fb3-37b0-a6ea-0e08c6a6dbed | -1.33324 | -52.62981 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b5a4d6d-e5a8-3b88-a0c0-ec1b296a6cd7 | -1.9413 | -45.73093 | 2024-11-27 04:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a4d07e4-290f-3270-9f6a-0a11f3736bb6 | -3.81493 | -47.47704 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b857ed-b3fd-38ad-b2a1-d279e54bd51d | -4.38002 | -48.5048 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b719c2c0-d3e5-3ee0-ab23-77948783b8e5 | -1.59712 | -52.26878 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README50.md)
