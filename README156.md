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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c49d4e1-ea6c-3222-9ab2-1a305ae47c73 | -9.6266 | -67.46967 | 2024-10-03 05:16:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ac7b68f-4170-37c2-a506-d4a3dde6d3fa | -9.62563 | -67.47513 | 2024-10-03 05:16:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 57ee7d9f-df86-3660-bfa4-45e0d05ebff6 | -9.58636 | -68.59713 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b9b5f58-8c47-3de6-9029-f6a4b7bbde26 | -9.58232 | -68.58978 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ef5576b-fd51-3413-970c-7c25d9fbfb92 | -9.58173 | -68.59294 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 266b6cbc-26eb-3a5c-8d54-aa5cbb61dd5e | -9.58115 | -68.59609 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea9df006-b06d-3a31-92df-0c79c5bb990e | -9.57709 | -68.58882 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d26090e4-af13-3b58-9b81-e83f520f049f | -9.55232 | -68.57675 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e602e0b6-3ed4-3b80-a98e-4d4601ed5395 | -9.55227 | -68.57705 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 593a3942-ffdb-38b1-86e2-d17e9547aa82 | -9.54711 | -68.5757 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17e99965-d232-3843-8cae-1fd69a61520c | -9.54706 | -68.576 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b46243f1-421d-3c9b-9a5d-82365cf04f9e | -9.51129 | -68.50604 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52366933-31b4-366d-a146-1fb5e6c4636c | -9.50609 | -68.50509 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac89480d-0295-3ed6-86dd-b1ebf65ca279 | -9.49687 | -68.49677 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 250af471-21e3-37fd-9a15-bb3bfbb63256 | -9.49628 | -68.49995 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4fff5891-2657-3def-bb0e-5e0b0dbc19ef | -9.49203 | -68.55214 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a378c4e-db59-38b5-99be-4782e9221ce0 | -9.49168 | -68.4957 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e4baaf0-649e-32c6-b818-6cb64521a960 | -9.49144 | -68.55537 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dca1cf20-3864-3284-b403-5cfd928ede49 | -9.49109 | -68.49889 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a587c409-3867-3609-8673-c66494b21e3c | -9.4905 | -68.50208 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f286607-3783-388d-81e7-5aa15041d361 | -9.48683 | -68.55105 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3e982fd-9e45-3d20-b8a9-129116a608fd | -9.48623 | -68.55431 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 695d788a-b755-34dc-854a-9b4bfff270bc | -9.46624 | -68.51399 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 197e587b-adc6-391a-a375-3a65613691b8 | -9.46601 | -68.54693 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da43e75f-b9e3-3450-a3e6-2bdb382b11d7 | -9.46566 | -68.5172 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab84b5dc-30e2-3220-bf61-cb7469b5aecb | -9.46561 | -68.52013 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a2bb601-262e-392a-928c-2412d0e4b336 | -9.46509 | -68.52041 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b92c84-2b93-3262-871d-52c25a8e6f16 | -9.4616 | -68.51273 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0985e935-308a-3e85-bf07-cc9a44543281 | -9.46141 | -68.54262 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8468f4d4-33ad-3034-b7ee-19f94a4941be | -9.46106 | -68.54295 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee15e6c7-7c4f-39c8-a929-aa839e2ac71a | -9.46104 | -68.51297 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f5d1652-d24b-3062-86fd-b611e2365285 | -9.461 | -68.51595 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40ef4dce-61fc-32a4-b34e-babd83361ba1 | -9.46081 | -68.54584 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d23d6fba-424e-36e7-becb-c31946f11589 | -9.46048 | -68.54617 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d558e3-feff-3e92-b107-209710a96972 | -9.46046 | -68.5162 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebe27bb6-d4b2-34cb-b66e-98a99228b26c | -9.4604 | -68.51916 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22f62274-43b6-35f8-8f11-6fcaeb4f3288 | -9.45988 | -68.51943 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b024ba-e1f8-39b6-9ff0-4bfb4bd290a3 | -9.45979 | -68.52239 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 899a1b8b-01e1-3d2a-96ec-7317338784bc | -9.4593 | -68.52267 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 771fd180-c151-3e37-8949-903e0692de16 | -9.4592 | -68.5256 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28e08267-5cd6-3b6b-9ca5-efce1459fcd3 | -9.45872 | -68.52588 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b27bdda8-f798-3a42-9739-3d97b0fd0607 | -9.44796 | -68.55678 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64ccacc5-669b-349d-bc38-d8832836439e | -9.44772 | -68.55713 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eba370ad-5538-3d12-b17d-e84f5d9ee69d | -9.44734 | -68.56009 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6cf65b5-1dc1-3277-bc54-94acdbecd035 | -9.44712 | -68.56044 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d106711-0a4f-3dae-9663-a676180f19b9 | -9.4296 | -68.59764 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a98ef75a-9af2-3e8b-87e4-15382982dcec | -10.5483 | -69.1013 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b3229e8-d65d-3588-8e32-6ced5f36cfa7 | -10.543 | -69.1002 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c263260e-235c-3430-9da0-a347256e04aa | -10.4971 | -69.13993 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 342434d0-5528-3abd-9438-f7baee3890f4 | -10.49178 | -69.13886 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba57f237-4c89-3f37-9b22-7842ff11653d | -10.14445 | -69.02518 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27edf8d9-a44e-3d05-a061-8356bd80e83e | -10.1438 | -69.02865 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d05e2df7-bc7a-34b4-8d95-6162a643fdd1 | -10.50797 | -68.67735 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3840fa73-3b6b-3ed6-9850-171d6b18c1ac | -10.50668 | -68.67728 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65856a74-125c-3ea6-b2b7-dab2ea31a780 | -10.50343 | -68.67307 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7520da8-2522-322b-812a-96a593c77fa3 | -10.50283 | -68.67624 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 590142ff-198c-389d-a767-49eea6f87f3a | -10.50212 | -68.67297 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1fee815-1f9c-3f1d-b203-acb60c459a43 | -10.50154 | -68.67615 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbe02479-e1c2-33b9-bdf6-c936eefb6ddd | -10.47312 | -68.54122 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0113ea5-4251-3c64-b137-46e78007f43a | -10.46742 | -68.54337 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cdeebe9-66da-3bfd-916a-dc1225268fed | -10.31759 | -68.70924 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3623c23d-0ade-323c-a869-035382c8fcce | -10.31698 | -68.71252 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fff2878d-95bd-3e53-897d-03d12e26f4cd | -10.31241 | -68.70819 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 708a94ad-a9ec-3312-843e-b54da68ea356 | -10.31179 | -68.71147 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ef9a90c-1890-339c-b621-674018b00b4d | -10.27907 | -68.74205 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df5fcf64-e698-3f52-bf72-0b85527f71ca | -10.27847 | -68.74525 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 926ae804-6b06-309e-b3fe-a149252bbf7f | -10.27833 | -68.74399 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8146149-6e03-3d56-aa1b-c2eba9e47b36 | -10.26961 | -68.76345 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05155a7a-ae0b-39a3-9a21-3d8677d336db | -10.26903 | -68.76542 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 346acfa1-bf5e-3935-8180-178eaf10f1fb | -10.269 | -68.76665 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68009a78-6660-3651-b6b8-7ff50f21b835 | -10.26844 | -68.76862 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee609c06-bd48-321b-80c9-80d71e007259 | -10.26839 | -68.76984 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c2361df-be5a-3287-9ea3-c1e7c38b8ffa | -10.26785 | -68.77184 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb1e969b-fbb9-361b-bfb1-de8b945c25b9 | -10.26778 | -68.77305 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1d36022-cc7b-3c6f-81c2-6d00bff9155c | -10.26381 | -68.76441 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19d0bb47-b795-358b-a786-32eca659710b | -10.26322 | -68.76762 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d1bd573-3e89-30df-a3df-ea1bf4614223 | -10.25278 | -68.76559 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45c127b2-e1f2-3f93-b975-f45720b31b87 | -10.2522 | -68.76881 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8e3f011-052e-395d-adda-c67c490a16c6 | -10.25218 | -68.62289 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6821577-0e08-37f4-ac36-4c0d78a39ff2 | -10.25161 | -68.772 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10b1a9ca-ff92-3fd0-bbf5-8c38a5e85352 | -10.16981 | -68.42615 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39066d56-4fd1-373d-a6f4-4460ed606f81 | -10.16925 | -68.42917 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2791ce34-b9df-3866-a33e-11b2702b6e22 | -10.16869 | -68.43224 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1da44024-572d-3b1e-9c10-28ee9953b084 | -10.16812 | -68.4353 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d6ae12c-a933-39ca-b448-dd75dfd911a7 | -10.05385 | -68.58325 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d9ca5ce-5ea3-3d1c-9e0b-406ba5b840ce | -10.05327 | -68.58639 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 720051de-f8a4-3602-9d91-515aa833ae9a | -10.0527 | -68.58952 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24ff0988-1669-37d3-94b6-35d2b2a2599a | -10.0369 | -68.47278 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56839ae6-343c-3830-a1aa-b8059544762a | -10.03175 | -68.47186 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a88e268-2a0b-3d1a-b236-541f0b28ee0e | -10.64103 | -68.02667 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73e389da-df84-3145-ba12-31be1eafff95 | -10.64003 | -68.02598 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e41f1ea5-a75f-38c8-aef7-07aef4e0a407 | -10.52765 | -67.85178 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27b5acdb-6e3a-3eea-baad-2d66a7e12bf7 | -10.52664 | -67.85741 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84e54b58-4ee9-3d6c-bb1d-cdbf8101537f | -10.52278 | -67.85075 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db2145c0-6676-36a0-967b-9afed91d560e | -10.50979 | -67.89442 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92af924e-f6b8-36af-aa77-98a364741cd7 | -10.50877 | -67.90001 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ff1a3b5-bb73-3dfa-a467-757f9e3bea36 | -10.50488 | -67.89347 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56f47160-df53-303f-8965-f197d2cd48ad | -10.50387 | -67.89903 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1774270-0933-354f-ade0-ed97340d08a9 | -10.49998 | -67.89257 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71df0d56-7ef7-3879-8688-119184685151 | -10.49896 | -67.89811 | 2024-10-03 05:16:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README157.md)
