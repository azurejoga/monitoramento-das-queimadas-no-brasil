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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bca9758f-cd67-3950-8680-2b3c0a8c7f14 | -2.3168 | -48.53909 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d0ba7c8-03eb-32a9-89b7-2aa2ac86b8ae | -3.58923 | -50.23133 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67ba5051-c5ee-3b4b-88af-e052efaa3d58 | -2.6299 | -46.77456 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 794fe1f4-d336-3614-8980-e0161de40229 | -3.09552 | -53.31747 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 933e1ac1-6e40-3f49-83f8-6a1db5f6e465 | -3.63377 | -50.75458 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc26515d-db14-31fc-90fc-608c48a62b36 | -3.0665 | -48.06329 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bec884b-1047-3922-97f4-b870f0972b49 | -2.62308 | -51.29664 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 73480776-77d9-346e-95d7-5a431c55d417 | -3.17051 | -49.09364 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c416a0b3-2b2b-34fa-bad2-99c33422940f | -3.25142 | -51.13144 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95b7a103-5f24-3bdf-a404-d08dde9c8c1c | -2.22757 | -46.54282 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e188eac-c281-38af-aab0-8550d6f2ca96 | -3.23899 | -50.44358 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b9516b1-b486-343e-b18d-6a3729bc1304 | -3.00855 | -53.43809 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4a20b5f-effa-3a1c-b745-ec8dc6f87273 | -2.24848 | -53.66535 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9b6c5fc1-14b8-3bda-a963-7b039b25e775 | -2.83531 | -53.97736 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 044bd71c-ec55-39be-88bf-838426e73b8f | -3.04786 | -53.27474 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a301cbe-6cfb-3aaf-a05c-e233006b5784 | -2.22627 | -46.54425 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5fb3323a-9f5d-3ea8-9eae-480b9215a445 | -3.2369 | -51.27268 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dea9c07-7b29-3a61-a370-3a05266acbe1 | -2.05017 | -52.0842 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3ede904-56be-37b4-9aff-1545c6e58b6f | -2.73287 | -51.73632 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8324b1b1-b9c9-3f39-a406-670b9df2431e | -3.14593 | -52.9754 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| c55aa10f-8026-3a42-9aaf-9a91fb9d78e0 | -3.07158 | -53.6423 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca92d5b5-64c6-3b86-bde8-85b92465d306 | -3.64011 | -50.18962 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b5817e4-786f-365d-b3ae-177b2ee5e1f5 | -3.0446 | -48.0413 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b0a566c-d436-318f-aba0-e32f3aae07d2 | 0.61522 | -51.6682 | 2024-11-09 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 638b1ce1-4380-3c6f-950d-adb83f1f02ba | -3.4779 | -52.62436 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b788121-63b6-3794-8df9-5826535e80d0 | -3.07215 | -50.56401 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 763743a7-37b8-3085-a47e-70f5ddafa7c1 | -3.01057 | -53.23299 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b9109a9-fe46-370f-b6ac-03de8e7c0394 | -2.68167 | -51.94928 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4684fed8-c551-33f5-a7ee-318d8cc99722 | -1.68473 | -51.91592 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0c092ba-eca3-3f8f-8bc8-cd9a08c9d52a | -2.36238 | -54.75708 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 68f83c20-7bff-3719-a367-418a712ed437 | -4.31164 | -48.61932 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 770ccb53-82b2-3696-9766-7084d402bb3c | -3.67047 | -50.25905 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5968e522-47c7-3511-bf89-181afd7bcd9f | -3.59157 | -50.24023 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d14519d2-e032-3c83-8a61-e01eec0b24cb | -2.25527 | -53.7303 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c701f5c9-dd05-35de-8fbf-c625afb27133 | -5.44816 | -43.26994 | 2024-11-09 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 62e697cc-20e7-3bee-8846-b6f621e19c03 | -5.16635 | -45.27845 | 2024-11-09 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 955e9ad9-04ac-3f6e-b091-b32e0e3292dc | -3.02717 | -51.23033 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6cc64e00-da1c-3aec-8d25-0069f480a5a6 | -2.92419 | -51.04878 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db5098a5-6e9c-3ad8-aa2a-3b43473034e4 | -4.24645 | -47.57605 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| c0fa2ba0-f489-3af6-9024-1217c515b747 | -3.0757 | -50.56456 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f7ca2fd1-a2ed-3fd3-ae62-4b597c27263d | -3.61386 | -51.20887 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3da5b0aa-ca1f-3202-986e-7da8dd5d7875 | -3.12275 | -50.21265 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72175084-0aac-3e47-ab32-94ac00a5a3b8 | -1.18901 | -51.9871 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce5e7494-8a02-328c-b84f-55bbac98297e | -3.09498 | -53.32092 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 583f62a3-18aa-3fb0-89f2-53e61e64388c | -1.51004 | -52.16598 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14f90591-0f28-3e2e-aa81-6cc1f8dc6427 | -2.93981 | -54.45795 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7cdb598-1def-3304-a3f7-0d36ee33be9e | -0.37074 | -51.43091 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a40595-b5a5-33ad-bd2c-423011abbb02 | -3.34066 | -50.07925 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ccb877f1-90fd-373a-a206-71c89e1d3375 | -2.45669 | -50.30256 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c10c5375-fa8d-3938-885b-590acb1694d5 | -2.33726 | -52.76058 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ca3c967-52a7-3def-84d2-05952399c24c | -2.45048 | -53.69308 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89de9257-f3db-33c7-9330-c7b34ea2a63f | -2.96526 | -53.86306 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8d896fb-c891-3dd9-9905-845bfef935a6 | -3.522 | -51.52967 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85694b9c-cdf6-3126-9322-f26716b63bf2 | -0.90598 | -51.65533 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff7b4b6f-fbda-380a-a65c-bfb702d4bb3e | -2.45326 | -53.69706 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f35198f-2235-3c8d-a9ab-08afbc7b24e1 | -2.79895 | -52.94218 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aee70154-3b4b-3f15-9373-2a19632c1643 | -2.52874 | -47.37961 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96a07c36-bbb0-33c5-90ff-ad1768bf0c2a | -1.59441 | -52.18595 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fafaadeb-c037-386c-8fb4-6985cf97677e | -3.84174 | -49.82462 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3df229fa-4c43-3910-a7ce-693cea056097 | -2.89005 | -48.29003 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 771c6c87-e233-35d7-bebc-d37c8b6444f2 | -5.73256 | -43.51004 | 2024-11-09 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 130abee2-b03a-3d3a-8deb-788545e8eca4 | -2.93847 | -51.05874 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2260f2a7-9816-3fd5-82e5-9b3d5c1a293b | -3.72752 | -54.22443 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2bba8710-affe-307e-8a36-3603c9445b3c | -1.38359 | -51.41275 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 323f4efb-85e8-3494-aad3-975c00155453 | -2.93029 | -49.8391 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9070ce6-4244-301e-9bb7-71337b75639a | -1.50949 | -52.16947 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62e9408b-6677-3a4e-a316-09cd494e2d10 | -3.03214 | -50.35985 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b8530b5-9c21-3806-bfa6-884bdb049a27 | -3.5353 | -49.99652 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cba7a8cb-a940-3288-b1e5-39375f62ac0e | -3.09231 | -50.2421 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4934b91e-cff9-3316-8b91-d59a5f178866 | -5.35806 | -44.14537 | 2024-11-09 04:55:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50562cf9-78bd-372d-84ae-96d015b7ee3a | -0.90894 | -52.56597 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66a427e1-a1ec-313e-a73c-b16ef7c27a9e | -3.55457 | -47.37832 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44f1c514-d138-3fad-8e78-553d9c32168b | -3.2627 | -49.47821 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee5d4a3-f004-324a-8eea-436c916b99b8 | -3.0286 | -51.0061 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff3c764e-08c3-30a8-8502-be8c586dbce1 | -1.48144 | -52.08637 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a17df50b-ada6-3065-a048-3f4f85fa1091 | -2.63984 | -49.83902 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57ba0bd8-4309-380e-a45d-ff71123657ad | -2.87804 | -53.9662 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7328514-7608-3e70-9f60-0e16edb9bf66 | 1.08258 | -51.30451 | 2024-11-09 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41e004b2-58ff-3977-8ff0-85d609a615df | -2.23864 | -53.7277 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cf7846b-0879-3b70-812a-4a1871723e8d | -2.85741 | -48.44922 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68a6e5bb-c2e9-3cbf-b109-9b67c16c1865 | -3.18717 | -50.58841 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d15c14c9-030c-3655-88cc-51d6edd8f919 | -2.23418 | -46.62181 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc2a4c87-6700-3a19-b5eb-ab217459200d | -1.68649 | -50.45655 | 2024-11-09 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d85eebdc-1e51-3003-b83c-4cebcae926e7 | -2.62652 | -51.29716 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3d5c8fc2-3b37-3955-8599-0e4fc1b91a19 | -1.68754 | -51.91997 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1daaf761-82d4-3c55-912f-65f4fbdd89f2 | -1.46906 | -52.40541 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c7e406b-2ef7-391b-8622-74a204d3716f | -5.31223 | -50.70324 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d30d9a3c-b633-3298-b18d-55ac9a9efa64 | -2.82484 | -51.34547 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 503c15a6-64bd-3232-aaac-9856d9a2e446 | -2.69124 | -51.68962 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a3ccced-88cc-3013-b8b1-9a8ed17f9fea | -1.62013 | -52.23996 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b5f889e-257e-3800-8d96-264792319729 | -2.08893 | -46.34421 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44352f0c-81d7-3b7c-ba47-6070fa3c82ae | -2.95557 | -49.36765 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecb6dc9f-9eb6-3815-b0a2-4729e5b84311 | -3.04766 | -50.36581 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afd58300-306d-3d15-ab56-697079bb8195 | -5.28833 | -50.56826 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64ac308c-0f20-3435-b082-e587c759fd9d | -1.95968 | -48.70095 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af74b88f-2d90-3b6c-b8df-e13e11e4e05c | -1.33543 | -55.46387 | 2024-11-09 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5daeb161-4f07-3f62-bc2b-1815d6b0ca04 | -3.11613 | -50.13491 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 270a2e48-8de5-3e30-b4fd-1997cd11915f | -0.38365 | -51.43656 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c897e2d9-4d22-33e9-886c-42cc3f8679cf | -2.55793 | -54.0023 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad215c2d-35d7-34a2-9081-325917767ae4 | -3.60103 | -51.24587 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README96.md)
