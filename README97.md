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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1df16c00-f094-3da9-a48a-f081bbbaf965 | -3.25557 | -48.74927 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f55eede2-ffb2-3a5b-ae7e-c42af0bfa2e4 | -4.40773 | -49.33784 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e3ed023-7b88-30fb-9e29-17a8c199ecfc | -4.06026 | -49.20494 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 555be526-eb2b-3d15-94af-ef91ddf7e703 | -4.32778 | -48.59975 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a66820b8-8397-33b5-9400-6f7c2083c0e2 | -3.08716 | -49.57711 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 714bc766-d021-327b-bca2-48a026307af2 | -2.34007 | -53.93238 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2036ec41-4fe4-397b-9075-67d2d7739d0b | -3.24604 | -50.20181 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c359ee3a-cfbe-3775-bdb3-6a3770d7030d | -2.2542 | -52.21188 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e7bb6bb-e4f5-3986-9a1f-7354d23075a5 | -3.79321 | -47.45924 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbe3edba-0df5-3b83-8f16-f42b2fbff739 | -3.03719 | -50.41693 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ee7c777-1aa2-3154-8f0e-55a7c850c55d | -2.86732 | -50.40971 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b1a0803-141f-3198-959c-c8d521b6f5e9 | -4.07358 | -46.0706 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3c204ae1-7bc6-365b-80a0-6d5f0f85799b | -4.57095 | -47.08006 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4686f1ed-724b-3e44-b756-16250430b2ac | -2.93802 | -51.05333 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 558de0ad-a88f-3879-8dbd-4895dcd95835 | -2.68211 | -51.94553 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a8be9468-4726-368e-8a7c-a986a72afe19 | -2.88401 | -49.38411 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9877fd77-dd77-3797-87a3-4c3c0fc9133c | -2.8685 | -50.40232 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43644134-da89-300b-929a-30b3e8d51f25 | -3.45241 | -50.17786 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 604610f8-5c93-34b0-b369-85a977823222 | -3.02396 | -50.36929 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf309539-1b4c-3340-9192-def6b1787c2f | -2.9041 | -49.47339 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de5e5e3a-499b-3e8d-8471-dc2e9360e115 | -3.23965 | -50.26414 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df0c2eaf-0fcf-36fa-ab78-b261edcf8bcf | -2.87176 | -49.43959 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bb2a8d97-62f9-384a-bf89-30d9df88f670 | -3.12477 | -50.15347 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a03dbe6-c855-336b-87ff-86e6d0e2aba5 | -3.24621 | -50.46387 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 587539e5-7911-3980-b631-a87b468801f2 | -2.63257 | -49.8847 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 465b7517-60f2-3fda-b96f-63f423db0b82 | -3.94706 | -48.1566 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 534a36fa-1a14-36e6-b41a-7203c33fceb3 | -3.09661 | -49.40981 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d6d2568-e602-3689-9725-cda8a25c0fa0 | -3.1503 | -45.93843 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f3e4f32-74af-38dc-bb52-d0da6d9ad2dc | -2.8528 | -49.22212 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8df36f06-0de5-3f23-bd39-36fdcf11e6cb | -3.12101 | -49.29923 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc02bb14-e218-327f-b455-dd2b4101047e | -3.35653 | -53.44415 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3248c392-84fc-3b7e-971c-fdcf8f6503a4 | -1.67024 | -53.80491 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7e3667f-d3ec-3808-90b0-422d6a71034e | -2.4262 | -51.95712 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 97197bb9-0186-3698-b396-f5b04a3480ca | -8.38088 | -44.13333 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25cfbfa4-4043-3507-807b-39fcdf061408 | -6.93134 | -52.86652 | 2024-11-10 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af0b2d4e-778e-34a3-9996-d40e900d6ac7 | -2.22372 | -50.46037 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a68b9bb3-81ee-3f6e-b3dd-9e117e504108 | -3.72889 | -54.74292 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58ba7d06-1fea-360e-ad97-d676dec86eb2 | -2.93111 | -48.31698 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61043e7d-1d6e-3ca3-99fa-c0bcd6f2e56e | -2.39553 | -49.07212 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1027199e-b36d-362b-89c4-a0680514d1ab | -4.03469 | -53.41049 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6259e045-d5be-3b5c-8192-b16bb10c859b | -3.19858 | -46.50525 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0ea067e-b03f-3479-861b-3040a12f8457 | -3.09049 | -49.40527 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56a8c6f9-f6ab-3658-852f-5afc647b2881 | -3.07705 | -50.56384 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db246a93-b87f-3f06-85c0-1b0f6ba2bd15 | -3.03206 | -51.09623 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36965ab9-71e5-3107-9c02-188bf44086a1 | -8.38453 | -44.13785 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e24a758-f8ec-3fc7-b933-d050305f63e0 | -3.25059 | -50.19509 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a42cf341-e660-3bf3-aa23-78ba18f31c33 | -2.287 | -50.26053 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f46d0e5a-7e57-37ad-87a9-23d00f53f539 | -4.11588 | -48.50588 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffda7b1a-551c-3bef-9042-a9fdc2f7ccb6 | -3.92312 | -50.24764 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a895be-9abd-367f-b9c8-6e72f80ba1b8 | -2.8703 | -51.47079 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17e6d3ae-f390-3ab6-b0ee-8da87660d0a7 | -5.23833 | -46.22856 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb34b4cb-24ea-32c0-a1c6-76ee2cf7264d | -4.11037 | -48.24258 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85a4f1cb-8336-3e59-a4ad-007c10a90da1 | -3.19458 | -48.66584 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dd32f60-3860-3ebc-9788-9f6644263d59 | -3.07822 | -49.59014 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf24b2c2-8586-37b0-a3c0-c389be1bee2d | -4.3766 | -45.57194 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ad88520-4ec8-30be-8269-c96f70e9820c | -6.61009 | -51.14251 | 2024-11-10 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d44592e-204d-3122-a43d-dc641e78aea0 | -3.9648 | -48.99525 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35c324f6-6fe5-3451-8e7c-d34585483609 | -2.24133 | -53.79327 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ac440eb-0a5d-319e-a7d8-73ae6eade8e2 | -2.13993 | -50.69588 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0217e10-5cf9-3b34-8013-cbfb17d3e65d | -2.72709 | -49.28757 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 577d50bf-717d-303e-a2cd-c921e6685295 | -2.72873 | -51.71971 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a01a574-59a1-3e1a-9439-75285b167f66 | -2.60622 | -48.189 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5069fc7a-16b4-3381-be94-24f52102352d | -5.17278 | -47.61096 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b90b2c7-e012-3051-9ce3-b9810280e631 | -4.08938 | -42.9339 | 2024-11-10 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9232b91e-7c5f-39c2-a6d9-f3b720958210 | -3.52593 | -49.99804 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 915d3111-d7b0-3c00-83ce-f7a4f53e3a76 | -3.35001 | -50.05512 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 653b2c56-872a-36e6-b2cf-e1e78f5237ad | -2.2958 | -50.39794 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ecce6ea-5e36-358b-a79a-d7de0515cdbc | -3.8508 | -49.0942 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5b291cf-de82-390d-a6bc-39ea95d5372a | -2.46533 | -50.41277 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd7a27d7-a2a4-364d-a515-567c9fe1665e | -3.08381 | -49.5766 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25d28117-c6ba-3840-9f8a-56cfc2138623 | -3.94673 | -46.40514 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaf500ec-e85c-3734-8d19-b99ade474a7c | -4.1325 | -46.11235 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62f3038f-da09-356b-bbc8-e2d15d8bd1e3 | -3.42891 | -49.97203 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55b50e56-45a3-3ad9-b34d-040debead6ee | -7.42791 | -46.65118 | 2024-11-10 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae9d2abe-69c3-3e40-a01c-34a3e9934c8f | -2.65892 | -48.64881 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce2e4585-586d-3866-9e08-e63a15307026 | -3.03724 | -48.0508 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09e8a569-26a1-38ec-a674-e4b67dbf1423 | -3.79265 | -47.46282 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060f8368-e847-30e8-9d3b-d77933da70b3 | -3.89794 | -51.92147 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 600f8ed9-f9a9-3f4e-acaf-febb9074c727 | -2.17813 | -53.70023 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 462b36ed-9bfc-3ebb-bcf7-119601ef8912 | -3.4804 | -50.37618 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0a40096-7fd6-31fc-99a9-9d23857b0baa | -4.21977 | -45.45481 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dcfe0a94-8a53-39da-864b-f4d73e2b2ec3 | -2.8392 | -49.04923 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c34c2043-4075-3deb-b0a1-913f2b31f6cc | -3.28172 | -49.62956 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bae761d-38a6-3d63-9960-85eb123ac8ed | -3.02502 | -51.09515 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9bf82b9-799f-3500-90ca-9f3f7656fb1b | -4.28141 | -48.18364 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ea2e0f9-e14a-3adb-bf72-ba5c460df526 | -8.38286 | -44.14952 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6523ef71-929f-3cd1-80ac-dedb89c4dbd2 | -4.8878 | -48.61272 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62b899df-fbb0-34a1-b948-f145df5eebc0 | -2.69171 | -49.83894 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccdaec14-405f-31e7-b083-9e610d7c61e0 | -3.54407 | -49.97927 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1d4505c-01f4-3376-9c65-9fa8ce7164d5 | -4.05958 | -48.30574 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95a06aec-de5c-330e-adf7-f0abc07c2bb2 | -2.85632 | -48.44662 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d447e2a-cd93-30fb-9966-9c6d1d3fb73b | -3.94876 | -48.16754 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| c8e7b353-6dd9-392c-9504-d6ac02f9c085 | -7.4356 | -39.76521 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ef66021d-3455-3b2d-9f1e-83a13816ee99 | -8.83858 | -47.7039 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b51472d-a758-3bb8-a5e1-4b49d8f90a1d | -2.23433 | -53.73097 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ce42991-86b7-399b-8afc-0f228b51b02f | -2.372 | -49.72027 | 2024-11-10 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57a5fc6c-8f33-3276-8c9b-21c6fbbfaca0 | -3.45184 | -50.18147 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f42cdfea-4dcf-342d-9be1-5b8bc9f46774 | -2.50513 | -50.48716 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17a804ce-bc8f-3934-ac3e-23e48a4628d3 | -3.30064 | -50.14694 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01c1874d-b056-3606-8bc2-e57a8259b128 | -8.40557 | -44.14106 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README98.md)
