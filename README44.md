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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0df6559e-340e-3a51-8f6a-974f94417de4 | -3.70757 | -50.4556 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0ee0f66-ceaf-305b-bee2-9807f56f5ff6 | -2.34989 | -53.86641 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49f87b09-e9d7-39ff-844e-84c9c2f32a1e | -2.76399 | -54.02466 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41768bc0-87de-3a0d-8d48-dc07e387860b | -3.63804 | -54.43947 | 2024-12-04 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d811bfa6-8dc3-3887-b024-c13833e31ffe | -1.458 | -54.46352 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a4be2f0-37fc-3086-bcb1-9e5e097f0a74 | -1.96662 | -51.54331 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b16fa586-1ee6-335c-9f14-fba6acc5cad6 | -2.89643 | -53.98325 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0b3f8b8-944d-3bab-ac82-5e5f71063950 | -3.70459 | -50.44803 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc4a6cac-4c40-3d3f-a497-449d71bf78fb | -2.86803 | -54.01151 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93c08650-a835-3e80-bca2-3cdfab3a6738 | -2.81442 | -53.06479 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33b62ab7-3652-3a85-b453-3b0e39817879 | 1.08695 | -55.98664 | 2024-12-04 05:03:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72da04ec-2e1a-3c09-9438-ec7e84b0646e | -3.85366 | -51.24728 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdc8abe3-f09a-33ff-9c54-21826968a68c | -2.0047 | -54.11899 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ce4c06e-3ff7-3267-8bc5-39ea481fdd85 | -2.83524 | -54.04626 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c28614fb-72f4-36b9-a53d-0278735f1a03 | -2.6367 | -54.0118 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cdff934-ba58-3707-ae3c-c355a05321be | -2.80638 | -54.03845 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aa95984-7848-30e0-8018-b713a810e0de | -3.98204 | -51.92876 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3564c933-508f-365f-89a9-fddf082c21fa | -1.49484 | -54.44448 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdbd58a0-b8fc-3dda-9a4d-52cab5dcad9a | -3.73825 | -54.07896 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 493bf3fa-28f0-3705-b65b-1d9499ecd7c3 | -3.92669 | -52.39865 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7ae0d7f-3459-355e-a3d7-b1951c97f21b | -3.66777 | -50.19085 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b52c6b28-90eb-3287-b7c8-ccce05194c91 | -3.10143 | -53.29509 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d6819fa-8e72-3d6e-812b-e2ef0c0727df | -2.02174 | -59.77601 | 2024-12-04 05:03:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e730fca-b0ab-3bd6-b3e8-87de387eb2c1 | -3.00923 | -54.74384 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d91f1001-7b70-39d1-bd8b-958e14bf533c | -3.13474 | -54.17537 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35778ba3-e638-3f6f-a198-69c2aebb6edf | -2.6388 | -45.73812 | 2024-12-04 05:03:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8ba71ef6-f381-3dfa-ab46-84c80a78a215 | -3.26402 | -53.65031 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e199a154-54f6-3876-83c4-1f1e3eaa4bbb | -2.56477 | -53.40682 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a2b3db8-e99e-34b1-8843-05041b56d1c1 | -2.69267 | -52.91914 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efb52a2d-6b36-3d92-8fc6-5ff5bede740d | -2.88812 | -54.01461 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 738a8358-10be-3718-b581-87b1a2cfc1b2 | -2.84328 | -53.94963 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c05f027e-43b0-3ea1-886f-bdb26e34d06d | -1.94731 | -53.34259 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d25b647-3199-3ce6-8717-602f79490b6c | -2.45197 | -53.97647 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81ba93a8-7328-37fc-82f2-a09fd45630d3 | -3.29556 | -54.1493 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0095d483-5cc1-3a78-a3dc-44ba918774ee | -1.72746 | -52.81042 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a54a9265-ced7-3cae-b1fd-adac3b7c17fd | -3.54891 | -50.17744 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89ba3521-e295-35fb-b09e-64831ee1a14e | -2.85702 | -54.06046 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1d849a6-b708-304f-9610-69a415460e1c | -1.3349 | -54.64176 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd76f560-bb52-3c12-9d9a-50ba28e04f40 | -2.76926 | -54.12289 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67f2f00e-b6c9-3af6-9326-37d18f070cce | -3.64309 | -54.31804 | 2024-12-04 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d24308c4-dc3a-342d-890c-3cb02bd926b8 | -3.77496 | -52.20841 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 283b13e2-85be-30c7-81c7-a6216e788938 | -2.66091 | -54.09835 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbc19c54-266c-3875-a389-783c18a6fc96 | -3.11734 | -53.98406 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b7a58cf-e604-3ba2-a4a7-8c34e461fe56 | -3.5413 | -50.17256 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7209cace-578b-30b9-86e2-4252029985da | -1.94954 | -53.32804 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08f3768a-ae22-36b4-9fcf-37d2b8c6d53f | -3.06661 | -53.2935 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d32a0b9f-5fd7-3659-b165-4b403227970e | -1.74907 | -52.64684 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 967758ac-0529-337b-9c0f-31f23a2ca32e | -1.70065 | -52.60123 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 702f5b44-7159-3cf7-9471-1cddedb06040 | -2.61072 | -54.22359 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e80b4612-b1a7-3caa-a17e-f94bbb18752c | -1.9507 | -53.34311 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b600698-2bce-3638-b6de-b1aa0abfe8fa | -2.00155 | -53.28383 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad5b1ab1-1c65-3693-ac21-b9692e4e418b | -3.22181 | -53.72169 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96676597-c4d7-3b0f-b9d2-db1a1be7411c | -3.71205 | -53.93594 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a44dcf4-7929-3992-962b-40e7e8d0b00c | -3.25668 | -53.6529 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0f0b1bfa-7d66-3110-af1b-44c5eb1d9dc3 | -4.71176 | -47.20481 | 2024-12-04 05:03:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79092f3e-2729-344e-b4bc-5be59733fc19 | -3.26457 | -50.21219 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eebf8071-2531-354c-92a5-240efd573830 | -3.04329 | -54.06343 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4338476d-f5dd-3960-9821-06ee858e10d8 | -2.95145 | -53.88588 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e68ac52-0e7f-3120-b696-ef2bfc4a3cc1 | -2.45049 | -53.63012 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a74fa84-5a9e-32dc-a88e-36814f4ab462 | -3.33863 | -53.30392 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9751fafb-4a0f-31bb-ad40-b0dfc21960ec | -0.85531 | -52.71083 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a3819c48-c014-32de-903d-c822b07b0418 | -4.10625 | -48.25203 | 2024-12-04 05:03:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7173bf65-f318-3844-905c-e3309e79e0e2 | -2.54143 | -53.99023 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d945a62a-c39e-3d88-94c7-fdfea2e808d5 | -2.8219 | -53.06208 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 30441fa7-4fc5-328a-918b-cd5ff5930198 | -2.91696 | -52.21057 | 2024-12-04 05:03:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86c33dec-3e69-3a5b-ac62-331053dea527 | -2.46528 | -53.7133 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79e0ccd9-94cb-33c6-b61f-29132631cb23 | -3.11573 | -54.0165 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9471dc30-fe44-38bf-a57c-f4e15bea5cf9 | -3.85644 | -52.16081 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 67864102-7721-3545-8d8c-cc777f383993 | -2.72706 | -54.30635 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2cf5786-0c7b-376a-951d-3245f7b53f1d | -2.41532 | -54.0141 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92e54d65-8d0c-32b8-9d4b-1e6dfcf3dcd6 | -1.9503 | -51.20359 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37a51b97-860e-3c9d-bf39-36e2dec5b012 | -3.24131 | -54.10109 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18dcccb7-92c7-34b1-b8c8-b01dee7eb5cc | -3.12354 | -54.01043 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05df26c8-2578-31fc-9e3f-54bd78b32056 | -1.68183 | -52.51571 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ce3e4ec-bc64-336b-8c33-1226db86ba98 | -2.79606 | -53.04653 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dedb518-3454-3d98-9bb8-e187cb49cecb | -2.87175 | -53.94311 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98513521-c8d5-32b1-9326-672e6e38ebc4 | -3.25043 | -54.15314 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d5efae5-4b19-3f18-93ae-18ded4c9da68 | -3.53115 | -53.51026 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1cf1856-71a4-36fd-8acc-7f5c2d5282ab | -3.78345 | -50.96964 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5f03852-8fda-3fab-b898-bd9d8ee17c96 | -2.59502 | -46.27624 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d66b6c46-b985-3d5b-b8f5-6be0751a866d | -3.49359 | -53.82931 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6148e8d8-a321-3765-9b79-b90ef261169c | -3.12753 | -54.61745 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e6e25d09-83f3-35ba-a510-e1552be46e7b | -2.97387 | -53.89674 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7442acc9-0977-3d2a-ab99-b7e922c7907f | -2.8584 | -53.96288 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5df6384-66a2-3288-bca7-f2c8a1349c2b | -2.43489 | -54.0423 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bea7c0d9-a8bd-3bae-98fb-70b2dfb6d097 | 1.08873 | -59.64766 | 2024-12-04 05:03:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37512450-2c54-3dde-ace5-fa23e095f175 | -1.36723 | -52.11274 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35466647-d4bb-32d9-82af-bdedf19cc757 | -3.57465 | -50.30978 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7ca4a7c6-b06f-378e-8703-b1d3816304e3 | -2.781 | -55.33519 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14eb1d1d-e45a-37cf-89b9-e19c18ca0d26 | -1.62678 | -53.52991 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebfb6d86-61cb-3d1a-a103-72438456f034 | -2.62525 | -54.08578 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a262494-4c1e-3639-be7a-eb0fee03d5e1 | -2.57956 | -54.33668 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b178b2a3-4e1f-31b7-baa2-e770e8ece1a2 | -2.25212 | -53.64004 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23d1fbd1-d94a-3f62-97e5-125b9fa0ab47 | -3.81775 | -46.94976 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90d81ba4-3ef0-3939-8500-f7cb7762ed24 | -3.8391 | -52.33163 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8350107-1e78-3480-84bd-2b432405abf3 | -2.25561 | -51.23492 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 254a435c-810e-32c8-96c7-5a101e7454c0 | -3.69711 | -51.08332 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df195037-e2d2-398c-8892-8b39e7f8025c | -1.62801 | -53.89628 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a701f10-6269-33cc-a11e-3d667c5734d0 | -2.67355 | -53.04379 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 277f202c-1616-3880-9e86-70229592121f | -3.19773 | -51.17769 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
