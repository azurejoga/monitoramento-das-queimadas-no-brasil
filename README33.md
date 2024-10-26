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
| 19eb1d9f-a25b-3255-812f-3ee337c20c28 | -4.57093 | -48.03163 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5f635c2a-51d7-388a-8c35-06143e6a99e8 | -4.57018 | -48.03586 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d9be3f08-e269-3514-b26c-e41599d5bca8 | -4.56999 | -48.02193 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 449d1527-724c-3e01-977f-bee138fc2914 | -4.5693 | -48.02599 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4e9e6bfa-caac-3ea2-8981-07840df8486c | -4.5686 | -48.03009 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 02ac2945-598b-303d-b747-a55fd92e3f24 | -4.5679 | -48.03424 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 38634b31-1a92-33d2-850e-6b3648d3cb7a | -4.48833 | -48.12169 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fb6ad0f2-b862-376c-aa45-cc02397c40fb | -4.71683 | -49.0913 | 2024-10-26 03:55:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1edebea-bea1-3b48-99eb-aa0163e7621f | -3.90376 | -49.0781 | 2024-10-26 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 224bec3c-b4f8-3680-a942-652896d6a1d5 | -3.82318 | -48.9613 | 2024-10-26 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4eb8b04-7415-3cd8-964f-6f9607a039e2 | -3.82238 | -48.96593 | 2024-10-26 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb9b0756-83f0-30c6-ba59-4ac69acdb5e5 | -4.33895 | -48.64006 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bacae7c-ae11-343f-8d35-f41078e3afed | -4.33376 | -48.63478 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f07712fa-d254-3c8d-899f-74e85e2df39d | -4.333 | -48.63918 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4187211d-5326-370e-be66-58b6f6030481 | -4.30104 | -48.64759 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 276621f0-32ae-3f36-a504-5f3109233fe6 | -4.30025 | -48.65209 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| af72bed6-8fab-32dd-80ac-c28e6d0184ae | -4.25258 | -48.55204 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cf3ba4c-9e04-30c2-b51a-681cc85c6697 | -4.2474 | -48.54682 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a86444fd-72ea-3217-9d1b-ee4513a5a3e1 | -4.24668 | -48.55106 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2776d821-ffff-336e-a3a8-ce05bb2d7a05 | -4.24076 | -48.55016 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7984269-0568-31c5-bda6-937b69a1fde7 | -4.24004 | -48.55433 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3599c686-bf7a-320b-874b-6ea5f032e582 | -4.23932 | -48.55855 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7281954b-1065-3913-97aa-f1102dffb017 | -4.2201 | -48.56428 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bf35ec2-10b9-30ac-b1a5-43b43183d3b8 | -4.17108 | -48.60089 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e590ae02-c721-35e0-a435-aefb9f7aeeac | -4.16754 | -48.59965 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8db604e0-c079-334f-b5ec-decb76927c03 | -4.09729 | -48.23717 | 2024-10-26 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef18b830-8d03-38b5-9fea-ae3940c58125 | -3.9306 | -48.33905 | 2024-10-26 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dc4142d-6a13-3d75-9dd0-4554c1bc5ea3 | -3.92988 | -48.34325 | 2024-10-26 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa103008-1b2a-38a7-b0bb-a5b3f9811801 | -3.90789 | -47.94715 | 2024-10-26 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46972116-0604-3ae3-baa5-15e86d1bd50d | -3.9072 | -47.95124 | 2024-10-26 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 307def98-ee6d-3329-b3d5-bbaf21acda8f | -5.21352 | -48.21982 | 2024-10-26 03:55:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 853ac843-7d93-3e6e-85dd-30ae4db844d5 | -5.21282 | -48.22374 | 2024-10-26 03:55:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e3c8461-4f19-3f44-a627-111f2100a62a | -5.21075 | -48.22226 | 2024-10-26 03:55:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c157a87-fa91-32a9-bb08-4e7d9f34d9d9 | -6.40617 | -48.34559 | 2024-10-26 03:55:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f94360d9-af7c-34ac-863d-3e7eb5f7bb49 | -6.40551 | -48.34924 | 2024-10-26 03:55:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fb10318-0aee-316a-b7f7-80ec2516f5f3 | -5.66126 | -49.10378 | 2024-10-26 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a9a4b58a-eb66-3150-9302-0172e3d09894 | -5.66049 | -49.10815 | 2024-10-26 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 49070ca6-1960-36e9-a408-a7d8e05b966b | -5.49566 | -49.5041 | 2024-10-26 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39bc0ad7-fa52-3667-bed9-e49a3f238631 | -5.49546 | -48.94961 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fac7250-7b53-39ea-b9ca-92656c911dda | -5.49222 | -48.94659 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983ffd83-cbb8-331b-95f3-86e438e1695c | -5.30195 | -49.49526 | 2024-10-26 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 655ba613-53e4-3ea9-a5e7-55b0bb3450ca | -5.30127 | -49.49551 | 2024-10-26 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4d4a7fc-4816-3a73-85e3-5adf6c6ff37a | -7.72799 | -49.54317 | 2024-10-26 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96093315-81b9-37ef-a574-4fc63241e342 | -7.2947 | -49.29056 | 2024-10-26 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2acc5331-0d5e-33bb-88f5-575337b6072d | -6.68644 | -48.75136 | 2024-10-26 03:55:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd891022-120d-3a3d-8e93-996edb9f9ae2 | -6.68573 | -48.75533 | 2024-10-26 03:55:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f34efe28-7192-3c93-b1f0-e9deb7d141b5 | -8.60517 | -49.03768 | 2024-10-26 03:55:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36f41001-6493-349f-809d-ab967030f340 | -8.56351 | -49.20753 | 2024-10-26 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d8d2be2-7523-3519-8748-5d9cc4f2ce2d | -8.54468 | -49.5594 | 2024-10-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 09032016-9e3e-38a5-aadd-20ae9212c739 | -7.98654 | -49.69326 | 2024-10-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8448dc97-c454-3f62-bef4-ab78bd62db1d | -7.9857 | -49.69775 | 2024-10-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9b0cf4d0-9ebc-30a2-a854-bea7cf72883f | -7.9746 | -49.69114 | 2024-10-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18d3e02e-345f-3e60-936d-945c344fd518 | -7.97376 | -49.69563 | 2024-10-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afbe2af2-fda8-3a17-8381-d9ee903da120 | -9.56489 | -49.62009 | 2024-10-26 03:55:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9abb0730-d0c0-3695-8a3c-94e9e269edf3 | -10.19907 | -49.1477 | 2024-10-26 03:55:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93dffcd9-897e-3331-bba1-10c2d73604dc | -10.19834 | -49.14705 | 2024-10-26 03:55:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8068b3f5-f9e1-3220-9ee3-2f1cfc8b38ae | -3.4679 | -49.26675 | 2024-10-26 03:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 990f9a12-2315-30ba-92be-966abc3446eb | -3.44703 | -50.15901 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44a0596a-d354-3173-8d7f-15073ed439cc | -3.44038 | -50.1582 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04a64ee7-8571-3f69-bac7-0f797f16375d | -3.3858 | -49.7073 | 2024-10-26 03:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64a60298-97ae-31c3-8235-973c7ff589aa | -3.37727 | -50.21873 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4c8ebf37-d284-3f6e-8646-7478ed77eeed | -3.37627 | -50.22446 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b888f14-e20d-3373-ab93-8bc299dab4f5 | -3.25431 | -50.20801 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a480a2a-705a-38d7-99d9-695f77cbd271 | -3.23484 | -50.18795 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2fcf45c5-cc58-357f-ac3a-0f3e0959c9a6 | -3.23074 | -50.18612 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 78ee2dd4-b4e4-398f-873a-7510fac7856f | -3.22976 | -50.19188 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e776a76c-b954-3931-882d-7eb7427a078e | -3.22817 | -50.18708 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b9b839fa-6bb0-3439-857a-d095ec233929 | -3.21951 | -50.17205 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e8e7073-ba1d-3281-82dc-8e7558a32b57 | -3.21289 | -50.17093 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1da0598-8917-3846-a953-a5b78381d9b0 | -3.15565 | -50.46438 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e66f0e32-e8e4-3012-8de2-a0d8d66e0e39 | -3.14994 | -50.45725 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6122673c-f873-3631-a1a0-b317f72395cb | -4.40992 | -50.7349 | 2024-10-26 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb432994-8303-357f-a3e8-1b95db8e1edb | -4.4063 | -50.73262 | 2024-10-26 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a1d2cf4-8a41-3eee-95c2-478afadb9239 | -4.40324 | -50.7335 | 2024-10-26 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e41840a3-d6d5-3221-ad79-b651cecb51e0 | -4.39871 | -50.52594 | 2024-10-26 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1f868f56-2775-3f3f-bde6-a24e80a1039f | -4.29648 | -50.73281 | 2024-10-26 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f5e4d09-cd23-3489-a5d1-089a345f80b5 | -4.2954 | -50.73898 | 2024-10-26 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ffcf63c5-d97f-3eac-bb17-a19f777f5bb0 | -3.92111 | -49.38482 | 2024-10-26 03:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b0ba8c6-2be5-3dcc-8891-66623ae4a8f7 | -3.91959 | -49.38161 | 2024-10-26 03:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad13edc0-1f8e-370e-8c9c-8ea217c83098 | -3.91873 | -49.38647 | 2024-10-26 03:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02feabe0-1b23-31ea-990e-baa28654e2e8 | -3.91484 | -49.38392 | 2024-10-26 03:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c6f532b5-4288-351c-8242-846b4ec2eaad | -3.91245 | -49.38562 | 2024-10-26 03:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 231bd6e6-5a56-3144-bfe2-335e9c2c94eb | -3.82187 | -50.23695 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfb612b8-f1cb-38cf-806d-dc220d6221d3 | -3.77892 | -49.83191 | 2024-10-26 03:55:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6680a284-a2a7-35b8-b2ee-fb9d1314f336 | -3.77244 | -49.8311 | 2024-10-26 03:55:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ac42bd56-76f0-3450-a74b-585d418f83a1 | -3.69427 | -50.16171 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ed4447f-8603-394c-a4ea-916631574da4 | -3.66798 | -50.12674 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8f23ae5-21c6-3b7f-a4eb-b5d950b4f393 | -3.66643 | -50.12811 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f571567-2088-3059-89ea-c3584d741bf9 | -3.66235 | -50.12025 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84b8c699-bd13-33de-a917-52d684d8d83f | -3.66141 | -50.12568 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c2a6d48-432f-312d-91bd-e0cc5cdb1c7f | -3.66083 | -50.12163 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f285b792-ca93-3fb3-a996-2df091de26b7 | -3.65985 | -50.12709 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d3b201b-780f-31c9-9489-d060f1a700bd | -3.65577 | -50.11926 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d8d16c0-6b3a-3730-a50d-0fd12cb23d7c | -3.65483 | -50.12473 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da0d723e-ab2b-3348-9d72-5731b879264e | -3.65387 | -50.13029 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9821553-4337-3d02-9695-db695b845175 | -6.19836 | -50.85784 | 2024-10-26 03:55:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 037fe403-2198-3c9b-bbe7-8f3e9694de5e | -5.25183 | -50.69194 | 2024-10-26 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55f3a10b-e879-3e36-8385-41842747c44c | -5.25078 | -50.69778 | 2024-10-26 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ed12291-3f5f-3561-a238-72c9d1d3e6b4 | -5.24518 | -50.69094 | 2024-10-26 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4716a7c0-da3c-3389-ae83-75a5f434deea | -6.43522 | -49.89935 | 2024-10-26 03:55:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README34.md)
