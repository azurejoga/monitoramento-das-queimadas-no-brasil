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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60bf9f4f-362b-3c2a-85b5-82cfc6c5df44 | -9.29735 | -57.14357 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29478c0f-0795-3763-b714-efc1fc3b4096 | -9.2968 | -57.14709 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eee68c3-b7ad-382c-be68-967ee495fe0f | -9.29625 | -57.15061 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 621efe70-0d7d-3f18-9586-9624ea0ad0ed | -9.29571 | -57.15413 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c67cf5f4-dc0e-37ca-871e-8bb8600e1414 | -9.29516 | -57.15763 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e181ccb-a15f-373c-81e9-05aa77a5d2a1 | -9.29462 | -57.16114 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e79738a5-7f15-30ce-b502-66e5d86a62e0 | -9.29407 | -57.16465 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84b3eb96-422e-30a4-a6e4-0c899ac63db5 | -9.29348 | -57.14655 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6b5a8e8-cf45-3b96-98ff-bbf57c31cf80 | -9.29293 | -57.15007 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b6ccac8-347f-338d-b761-dcfb4bc373c8 | -9.29238 | -57.15359 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06bec950-7ae5-3821-9113-ed9fb8ebb3d9 | -9.29184 | -57.15711 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 366911ad-3b08-30cd-ad76-3bd6bb304387 | -9.29129 | -57.16061 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68f3281c-5139-36e6-bb2d-5b7726172b87 | -9.28852 | -57.15658 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 52fffea3-65b5-3c8b-a031-21888f55ab2d | -9.28797 | -57.16009 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cde549f-1ce3-34cb-8c24-0a70fed6d128 | -9.28406 | -57.14145 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef919310-5bce-33e7-af98-f4c93eea024e | -9.27968 | -57.16959 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c05770a-c3bf-3422-980f-76cb48c1664a | -9.27691 | -57.16555 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6709e1e7-a23d-349c-97b6-5966bb677db3 | -9.27636 | -57.16907 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7bc0329-e415-3c2f-b54c-19e7dfbf2a11 | -9.26819 | -57.24341 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 274fcdcf-99c4-3466-976f-67b0e218608f | -9.26765 | -57.24692 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59973c1c-5947-3710-9210-425b2cecb893 | -9.26711 | -57.25041 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c1eb247-5ca3-3323-be9d-75683299faf1 | -9.26668 | -57.05576 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d9bcc0d-1db1-3906-b36a-6a066f02267d | -9.26613 | -57.05927 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9dd6cfb-8c08-3e20-bb60-51882c88c8ea | -9.26378 | -57.24989 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2b64ab3-c1f3-38bd-b3c5-aa455e73618d | -9.26047 | -57.24937 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa523b26-eb45-3fca-a2f1-5cb23b46e79e | -9.25074 | -56.91561 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2944636-6904-3d75-bfea-7cd60e3e15d8 | -9.2502 | -56.91916 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb60633d-8bd0-37cd-83b7-9a8ce00baae5 | -9.24965 | -56.9227 | 2024-09-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d52b220-26f8-3e27-9bd7-6b14f67346e7 | -9.23255 | -57.14416 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e8e6857-184f-39d9-951b-a014121bf786 | -9.19496 | -56.79405 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42f62eb7-9d8a-3c70-b9f8-b0a1251d09e9 | -9.1519 | -57.11688 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e541efdd-5238-37aa-a95a-745ce89b1354 | -9.11942 | -56.99622 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc61b649-5f83-3bcd-9f0e-71d94dbdcf2c | -8.4967 | -57.24779 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc92a76-975b-3cee-a2a2-fa009694656d | -8.34477 | -56.49572 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3894043d-b8a2-32a5-a443-fff3f3f2a5c3 | -8.33425 | -56.51962 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdd60de2-f01c-3789-b80a-664f08404c67 | -8.3309 | -56.5191 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71554849-a29e-39d8-8814-2c3a7c7b15b3 | -8.31691 | -56.48434 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d3299dd-d995-38bf-b512-317303fe3f0c | -8.31585 | -56.51328 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46c73c78-a6f4-3740-a57a-26e1403f9fcb | -8.31411 | -56.48026 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0c1123f-7dbb-3d24-b3a5-da6a0e102f0f | -8.31355 | -56.48383 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88f1a36a-400d-3090-9954-8afcd67f1f31 | -8.3035 | -56.48228 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15c5179c-ab68-359e-8892-b650053297b9 | -8.2996 | -56.48534 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 600dce8f-5d73-327f-9189-12740fa4aba7 | -8.29681 | -56.48125 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5d40231-8712-3caa-ab0a-59d48317911e | -8.2963 | -56.50665 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 369e1c4b-fc95-3772-8650-fdda6bed12bc | -8.29176 | -56.46952 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 21484234-09b4-3c10-a761-6a92a15f7cf9 | -8.28841 | -56.469 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25159775-30a2-33da-96e5-6987d137a3e2 | -8.28626 | -56.50509 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36b16fe2-976a-30fd-81cb-b79080ef46dc | -8.28006 | -56.47864 | 2024-09-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 05067030-1caf-3374-8ce3-906bac92209c | -8.27951 | -56.4822 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d311b78e-5b58-3cd8-886c-34eacd68f6c8 | -8.27616 | -56.48169 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 747f5ec2-b23a-3876-90f6-11cb59521cb5 | -8.09926 | -57.6829 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b7742aa-a8d7-3539-bdc1-8ecb49b93642 | -8.09871 | -57.68637 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8686d8b8-370a-39a4-8ca7-dfc8b172bb22 | -8.09595 | -57.68238 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64a2e935-e3b0-3659-82d6-b697a1f8b071 | -8.09264 | -57.68185 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc6bc315-3df7-30e2-b245-25504b7a7450 | -8.08933 | -57.68133 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec604af6-7c65-3beb-bb84-489e8dcddc94 | -8.08548 | -57.68428 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2244a91d-6dff-3f43-8939-0399743b574e | -9.02058 | -57.17598 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4456a18-8b23-3957-b5f4-011d7bd5ba91 | -9.00293 | -56.80829 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89bd1024-768f-3f15-9c8d-7a0a036248ac | -9.00183 | -56.81541 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4a6fa8e-3e48-3109-b0e4-d526de018b61 | -9.00014 | -56.80422 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d26552ee-f16a-3f19-b030-02a1cb52784c | -8.99849 | -56.81489 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| defa29e3-cf51-3517-bda6-9ca9d1db9e71 | -8.99515 | -56.81438 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 614233f7-d026-3bff-8b29-c8eee82c0960 | -8.99235 | -56.81031 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdf459c1-b971-3f39-a3ec-374a24f8875e | -8.99008 | -57.1532 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef33b511-e239-311c-ab04-99f357e3d8ae | -8.98956 | -56.80624 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1719b1ec-48fc-326e-9700-084933199900 | -8.98622 | -56.80573 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05861cc0-67cb-3577-ab96-65f651f2f921 | -8.98343 | -56.80166 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60781f54-5490-3798-ada1-0134e31612b4 | -8.97954 | -56.8047 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2e7cd2b-3c60-3458-9030-844d9ee62cb7 | -8.97511 | -56.81125 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ce700d7-eba6-3318-9d98-7d5bbb806dc6 | -8.97123 | -56.81427 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a828527a-bf09-35f6-a6bb-31e440cf13a0 | -8.97068 | -56.81781 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 718a5562-192d-3ca9-aead-83d25fbd3942 | -8.97013 | -56.82136 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e4cff54-2f22-30b2-acb2-481cbed5b329 | -8.96734 | -56.8173 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb814af0-773e-31c5-91e2-890ede10a3f2 | -8.96679 | -56.82085 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85b880c5-75d3-3a65-992a-3be11e5bfac1 | -8.96635 | -56.86803 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fe76b09-f84a-314d-8947-bbbcad6d073a | -8.96625 | -56.8244 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c883d709-b439-3bd5-9833-8c83e8c06a2d | -8.96236 | -56.82744 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3f62b53-5a53-3786-b8cd-12794db042f6 | -8.96181 | -56.83098 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc4c2711-f509-3f00-9144-713bde9f9c4a | -8.95684 | -56.84109 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 300f3405-5448-3776-9f44-b96a58b34390 | -8.95629 | -56.84463 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f76e3e7e-0624-3f89-b836-a6004e420748 | -8.95405 | -56.83702 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9056775e-fd25-3e52-bbfe-1be21f73ae66 | -8.9535 | -56.84057 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e182bb1-ff0b-3e48-afa9-544fff7bf177 | -8.92716 | -57.14314 | 2024-09-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf0bf788-ccbe-3474-96fd-5b14ca4d3b7c | -11.62843 | -57.09657 | 2024-09-28 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 518fcf43-57d2-3149-b563-43087a591666 | -11.62506 | -57.09604 | 2024-09-28 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d319f34-ce36-330e-ae09-9261d765b8d9 | -11.62451 | -57.09967 | 2024-09-28 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e305e15-8aa8-3480-bc4c-7b28aef97174 | -11.62115 | -57.09914 | 2024-09-28 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dffbc641-c91c-3a93-a957-83dee4d53dc3 | -13.54395 | -58.32297 | 2024-09-28 05:10:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79059d19-efeb-3446-8acf-722c3f73af13 | -13.53788 | -58.34019 | 2024-09-28 05:10:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 777c97e4-8939-3b38-91dc-13d03043a1b9 | -13.29268 | -58.19129 | 2024-09-28 05:10:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11b4b620-7e1e-3a32-839c-1a13ace8a4be | -13.28936 | -58.19076 | 2024-09-28 05:10:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 026df6fd-9b8c-359f-8915-10c7a827dccf | -12.48579 | -57.78967 | 2024-09-28 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afc8a827-dc47-33d8-bf0f-ed4955c65cec | -14.9228 | -57.96257 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2054f28-b29f-3ef3-bb1c-210195552476 | -14.91944 | -57.96203 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 019d3436-1756-311b-a82a-bef35a446f1c | -14.91273 | -57.96096 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52dcd9c5-43c7-3fbb-afe6-3e2576ae7db9 | -14.90043 | -57.97402 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79b3726f-648d-3e52-b029-91296f419b20 | -14.89987 | -57.97768 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18bc2b71-85e9-3603-9f4f-4ed1ab06954f | -14.89652 | -57.97715 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 54d5b144-220e-3114-9701-f2f40aac90e1 | -14.89596 | -57.98083 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 15dc3d05-19bf-3c53-8bd0-4e773c4ca786 | -14.89316 | -57.97661 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README85.md)
