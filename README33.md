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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beee4aed-91c1-3818-b994-50df1afba42e | -3.17231 | -45.03732 | 2024-11-30 04:40:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4959b892-a6dd-38a3-a35d-b1ea7f8553bf | -3.98836 | -48.94188 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 740cdac3-7471-3e02-80e2-7b539c5cb044 | -1.38015 | -53.64895 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 35522200-a615-3df9-8435-b1864ad7e107 | -0.56638 | -51.69351 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63af9b9d-4d0b-3e91-9b7a-1ed161d5e72a | -2.91275 | -51.71309 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c2a723d-0040-35e0-95a4-bab6533ed5b4 | -3.01953 | -49.52654 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecd70c49-44d7-3e28-baa9-98eed4422824 | -3.30419 | -50.37961 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fbca5b7c-1205-3d84-b323-ad6d7e6ef8b5 | -2.34686 | -50.57614 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5f9db24-c176-30ce-86cb-16a0a3cefec0 | -2.20841 | -48.38156 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac90b8a0-f08a-3710-9154-5b52daca7e2f | -2.01117 | -51.1956 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ac4d2ffa-d758-3634-807c-1a8bfb3ab55c | -1.68351 | -45.78653 | 2024-11-30 04:40:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5629a3d1-5653-34dc-9fe5-d686de52b2e9 | -2.57179 | -47.35658 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 346296e0-a10a-3eca-b224-df55c487e6e1 | -2.98223 | -48.7211 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 511a59f9-4445-331e-be7c-45ce7425e20f | -1.8418 | -47.17555 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d5ccb5a-0b75-36a2-a1a1-4b7cdeba6834 | -3.89207 | -46.4087 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42bad4ac-6f78-32bf-818c-4840dd2ebd7c | -2.56082 | -46.5639 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 351de9b1-879e-388f-ab7f-0e52beb9d4a0 | -1.60102 | -52.28983 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| faf30c6f-1759-331d-824f-507fd461d03b | -1.62211 | -53.8862 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fbb268a-e1a2-3b46-84ea-8b903d7eba9d | -1.56356 | -51.85843 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a77d7c2b-ac5f-3c13-88d1-6a6943bc4836 | -2.13615 | -49.49857 | 2024-11-30 04:40:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66ebf2e3-9b77-3c1b-9786-e2e1a03dbae8 | -1.08969 | -53.63913 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 339aabd2-19d9-3fb2-8014-93b7ffedb765 | -3.96387 | -48.09256 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feaa36aa-9c85-33c5-a3a0-39d04db15312 | -2.80142 | -45.93849 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3409652e-2845-3c98-8ca0-d24da046eb87 | -0.77496 | -52.38929 | 2024-11-30 04:40:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4ddda3f-d07d-38c3-afaa-991e443f4f6b | -4.04837 | -46.83345 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04266f15-3c35-34eb-a324-86b8f81ef513 | -3.05565 | -48.51049 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57aef899-2699-3f8e-90ff-dea70c1f86c8 | -2.53631 | -54.06939 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e9b6951-fec0-394c-a68a-fa75718fac18 | -2.3659 | -48.55073 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11143137-a79d-3871-a146-513507abae51 | -4.82056 | -44.35612 | 2024-11-30 04:40:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdb5d992-86cd-39eb-88c6-1b127f907257 | -4.05237 | -46.11512 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c23c01ea-bf08-3380-aa32-aac28ec602f6 | -1.1686 | -51.93979 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b53e7b3b-051b-3515-acab-e4c37590364b | -4.06305 | -46.69009 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a08f3882-9795-3079-a503-bfe92e29071c | -3.19929 | -46.55997 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51c50478-feca-360c-86ea-5cb69d734fba | -2.83899 | -54.0281 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a443b4f9-37b4-37f2-8a4a-f90383438357 | -2.62292 | -51.75584 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf8cb0f9-9486-379b-a71e-8e4a3b167c55 | -3.03735 | -54.04089 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32f723f5-344b-3953-a677-0cd25831dc45 | -2.58734 | -53.98402 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 364fae75-6d7f-38a2-925f-e6a0c025b4ea | -1.34698 | -55.00672 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2454d4b-dd9a-3ab9-ae82-4551a589c55e | -2.30067 | -51.98623 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c79f23b4-1b0f-3f86-bb02-00221b675cb4 | -2.85874 | -48.90234 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5df69ba1-d851-32ae-a427-f786deb333ce | -1.68291 | -47.84733 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 473afcbf-2336-38aa-bbd8-8ebbd2b9b895 | -3.14089 | -53.8434 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 786bf250-d847-3a50-8d13-a90e1acc1cb3 | -2.61786 | -54.21328 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a2bf8d7-18dc-364d-a84d-85dcb5dbcde2 | -4.94045 | -47.80498 | 2024-11-30 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57acf27b-95dc-3a46-be82-c001331cc19c | -2.46948 | -46.56561 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8f98be0-a0c2-3b4f-917a-4d5d9da535f3 | -1.75733 | -53.64274 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16724e55-5bed-3486-8624-f42711a7105d | -2.96395 | -53.72103 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| baac4df8-1bd6-3b54-8c41-106774189e05 | -1.30067 | -55.74416 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df9e1e34-46c7-3ed9-b6e8-2c4a640b7707 | -3.07369 | -50.32949 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 56334a7f-b3c1-38d8-b387-bd8d266e15ff | -3.70887 | -45.68793 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61bbe654-e667-3286-84c1-57dccb4dcd2c | -2.46664 | -46.53801 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fac1405-b708-39fa-b2aa-aecd50beaa01 | -2.87483 | -46.80325 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ca9746a-9005-3cdd-97ce-839e8fe2a717 | -1.70543 | -52.46433 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4acc66e2-294e-3c70-8796-0ec4982116bd | -2.26301 | -51.23709 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d161e19-7c1a-3bbe-b261-90f735ababa6 | -3.23368 | -50.31037 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c69248f-c076-3f1d-b47c-c0f751e0ba98 | -3.58292 | -50.5075 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cef39c2-2fcc-3ccb-b296-dedf2be5450e | -4.17354 | -48.62812 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d1b8aa8-cd22-3d99-bd2b-a523c8512051 | -2.46457 | -53.96906 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8505c61f-c9e8-3d73-9294-8aaae49272be | -3.52729 | -50.47687 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 905742ff-6e63-3865-ba2a-ab02bfe81587 | -2.67685 | -46.60804 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 021e9f3f-8489-3f4b-b141-22588eef3635 | -0.94631 | -51.65829 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5b4034c-b024-36e1-a2b1-c1456e95af74 | -2.58122 | -51.925 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28c7be7a-0e51-3ee8-ae80-97ef94f8e989 | -2.40887 | -51.98977 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b87f32d-5bb3-381d-b249-c2b9e8f06a08 | -2.11847 | -46.42796 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36e020e0-452c-32bd-888c-c2d0ee9df8c7 | -2.63974 | -54.07425 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8797d94-e1bb-34bf-bca1-10e263b2793b | -2.72764 | -46.27727 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf8e32b6-945b-3b60-9fb8-1ced3b00d603 | -1.09795 | -53.39981 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60906858-1077-34a5-8b42-39079017da86 | -1.99908 | -52.09348 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 918b6111-819c-3a63-9cc0-a40bf893f51f | -3.61428 | -49.98676 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad206ddd-710a-3db3-9b7c-5d2d989a541e | -2.98447 | -48.72848 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7a7433c-4dd7-34cd-aab4-2615a8765454 | -1.62644 | -48.53704 | 2024-11-30 04:40:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f7e90eb-a6fa-3726-b784-bc48b3a54efe | -1.89355 | -54.54659 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2f6dc7d-dd33-328b-98c4-19c4505c23ce | -3.0358 | -48.50743 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d7d6b5e-99a8-342c-9abd-d1e554a12fa9 | -3.26196 | -48.89163 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f199d6f7-d616-3019-805a-64f7480511bc | -2.34985 | -53.92837 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47d585f9-b0d6-368e-8a1c-f052e1195998 | -3.74657 | -54.67984 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80be930d-1c3f-3735-b478-603fec55e334 | -3.33228 | -53.36004 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf3e8186-96e4-30a6-9368-b8e720ecfeb6 | -2.60815 | -48.34916 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7fca4fd-d627-36de-9883-d35448a9d9ca | -2.43029 | -48.55008 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d6cec5-18b3-3abf-88c1-9bb800a91adb | -2.08979 | -48.55304 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5422dafa-b1a7-3014-956e-60bdb4afde12 | -3.94705 | -46.92377 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab46cced-0877-3b07-9719-14bac5d25b24 | -3.21591 | -54.17657 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 25be7a34-9c66-3812-ae37-98405946cbe7 | -5.13104 | -44.05301 | 2024-11-30 04:40:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 252999db-aa0e-3c43-a352-29ede4771bdb | -2.58791 | -53.98044 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa6f52ce-b451-3dfb-9d75-93b51ee83512 | -3.49767 | -50.29329 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d78498a1-0e72-3b51-96e7-ec104076aa14 | -2.67853 | -46.26965 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02731ca6-3926-31ea-9975-24a9cded0d4f | -3.58709 | -49.98612 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 185f5b07-2e25-3521-87c8-1176a53a23c2 | -1.28433 | -51.65232 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ea39280-9009-3354-a1f5-c9bec1f1bd6b | -2.98344 | -53.29462 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1237b326-bc84-3ac5-846e-929f1ddb4fa6 | -1.64128 | -53.87129 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 56fedd2f-c7b2-31c6-9518-5a91783d2cc9 | -1.00133 | -51.71692 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 654aaee6-171a-3ec2-97ee-3d201a7e9596 | -2.47387 | -50.36499 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d5f0f2a-5c0b-373f-9e50-d180408b82ff | -4.67516 | -48.15197 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4729eae4-7a60-3499-b7f3-5b430141127d | -3.7517 | -49.93357 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 576828d0-af38-300f-8c27-3a2f534d06bf | -3.84251 | -46.52228 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 02165de7-4bad-38cd-9134-b3e6b378e5fb | -3.73919 | -49.94894 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db596efc-147f-3135-b842-6e6112535504 | -3.99163 | -46.65628 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d00321bb-2145-3440-bc2a-ef7db3e4ec41 | -2.67734 | -46.27749 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49e52e0e-2931-31c5-871a-6cf22247ad5b | -3.44526 | -49.48003 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5455673b-fb16-37bb-a9cb-bb3ee27dde58 | -3.14204 | -53.83638 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README34.md)
