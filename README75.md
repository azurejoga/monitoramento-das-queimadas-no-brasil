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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e3992e4-39f2-3d22-99db-0c19698d21cb | -6.32241 | -41.62882 | 2025-10-05 04:44:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77490ed1-30ec-35d0-87b6-11663bd0d6d5 | -6.06545 | -41.24005 | 2025-10-05 04:44:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b271061a-772e-31e2-bd85-0491b5ddca99 | -5.76595 | -43.98878 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c3225a22-7a48-3ef1-ad7c-bbdfc228c9f7 | -6.151 | -44.60575 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 748abc69-8f6e-382e-9b8c-7ab9164d2d2a | -5.77199 | -45.78148 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e078284-d683-380c-86e1-e38901b1479a | -5.77166 | -45.75559 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 173a2278-d57d-3cd0-81b0-078524b1a220 | -3.81229 | -53.83929 | 2025-10-05 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77575b4f-633b-3e92-99ff-8de90f8b3df1 | -6.37045 | -42.88183 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42a799b2-d8c6-33cd-8f18-7e335532afea | -6.37508 | -42.88515 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51c8a16a-4d1b-34b7-bc8e-a7c186d480ab | -6.37233 | -43.29602 | 2025-10-05 04:44:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5eba562e-a624-3c31-966c-ee8cf7ae6183 | -5.21436 | -46.18452 | 2025-10-05 04:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7efbed3b-cf38-3ec6-b3f3-902ea9553141 | -3.6474 | -48.32093 | 2025-10-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48405433-9901-384d-8784-503788ec5790 | -5.35853 | -45.95025 | 2025-10-05 04:44:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6a9a483-77d9-3b53-bdbc-b1ed7826e592 | -5.7991 | -42.72136 | 2025-10-05 04:44:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1bf4132e-5d5d-347e-aabb-9c8d2e9c37df | -6.36207 | -43.91692 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d79fd33a-2aa3-3d7f-bcd0-e08400e2c182 | -4.80528 | -48.34003 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f638365-8e1b-3fe6-b13e-4ec1bc6f3a86 | -6.40062 | -44.77572 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 109cf574-0755-366b-ab75-86874831d3f7 | -5.77202 | -45.86498 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2eafe9d7-fb1e-376b-b80f-5355496742b8 | -4.44558 | -43.23924 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 45c362fa-a1a0-3085-9a03-1fe10691e3d5 | -3.44002 | -43.33862 | 2025-10-05 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01b4b16a-6b47-309d-a1a6-f743692bcaaa | -5.78945 | -42.9287 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 59cf7512-3b46-3c5b-a3c7-e266ff7522c3 | -5.84591 | -45.81736 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| becc77a8-e089-3341-8834-7e7064f51789 | -5.84747 | -42.88658 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9a8d5e5-f4aa-3811-9d46-883fe8315f28 | -5.97622 | -44.12604 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6eac95f7-1b91-3557-98c7-980147683407 | -2.90254 | -48.07486 | 2025-10-05 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b052f839-d928-3e5f-bd5f-d0a7ed3db408 | -6.67584 | -42.78505 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1993e507-839b-3a8f-9246-bffc9b96b3ef | -4.26713 | -46.74905 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 394eb5c8-738d-3543-ad0e-6b8793e2cd31 | -6.14479 | -44.64888 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2e1eaeff-1859-3f17-a7ef-5c979c7499c2 | -5.85368 | -42.80648 | 2025-10-05 04:44:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2bb4e9c9-daa0-3ec2-8889-7fa5146d9bed | 0.44529 | -50.80169 | 2025-10-05 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f50e2750-64e4-38e0-aec4-ad85b109c233 | -5.91259 | -42.53402 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 27b9ce26-249a-309a-9c7a-762f8ec41ca9 | -6.18829 | -42.71992 | 2025-10-05 04:44:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d3abf41-c3f9-39ca-8ad7-cb76d6bf9077 | -5.05149 | -47.67097 | 2025-10-05 04:44:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b4d5c12-024e-3277-9070-1c16f483cf08 | -3.83791 | -51.33516 | 2025-10-05 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fca14cc9-0da6-3775-92aa-4ac541c91d10 | -4.13694 | -47.65714 | 2025-10-05 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3de68566-2882-3044-bca0-2baaa190205e | -6.70588 | -42.15808 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 078a7ab9-1026-3dc2-b710-3483eacf65e6 | -6.4407 | -44.155 | 2025-10-05 04:44:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d59172b-4ff2-363f-85a5-941959f8f3b6 | -5.64212 | -43.90417 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5220b35-379b-3711-bd64-24e354a038f2 | -5.38005 | -45.69876 | 2025-10-05 04:44:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeeea1b7-9ed3-3a83-ac3c-2b0aafd9fd40 | -4.22641 | -49.78689 | 2025-10-05 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91e967f8-47bf-3ab7-9913-e114fad12130 | -3.77375 | -51.93896 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7742bbad-aecd-3d1d-bf5d-7cf8f521bd2f | -5.81729 | -45.95763 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8999a3e9-aeb9-33c6-923c-934b32647962 | -5.78865 | -42.93419 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f6d2dc33-1a12-30c7-b4f0-89789eaae127 | -2.68413 | -48.39636 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6daed9f-3f1e-3b89-8da8-59bb1acc234b | -4.2284 | -46.75235 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34e9b9e6-23c5-38b3-9077-0ad3739721b7 | -5.34655 | -45.29777 | 2025-10-05 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 950c3c02-c05b-34f2-ac5f-e58d24aa72df | -2.14545 | -53.63643 | 2025-10-05 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b5a1336a-a15d-3341-b038-d553736672cf | -5.8549 | -42.79781 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 576b0b66-42d1-308d-91ac-0ec7618189ea | -6.40196 | -43.60229 | 2025-10-05 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a415ee81-39a4-37b6-8489-66b86110600c | -6.29555 | -44.0542 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4d5baa6-b994-3d1e-877e-0f79a9c59918 | -5.76482 | -45.80202 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 302f6532-df5a-3b71-8242-19fbe5df4e0c | -0.90656 | -47.54567 | 2025-10-05 04:44:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5b6a4b5-ec82-3c90-952b-356a384ade3f | -5.79847 | -45.77061 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9402f998-d385-38c0-b284-1a7a38cb4658 | -6.25856 | -45.35664 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7850647f-477a-33ea-ae19-8fd7cd70eb7a | -3.81295 | -53.83509 | 2025-10-05 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0a0fd9d-968e-379a-bc89-45f0a600c9ae | -2.69208 | -48.39007 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec15a61f-1479-32da-a02b-57d4d5c39330 | -6.37468 | -42.88806 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 248cd2a1-377b-3a6a-9714-e8430e27aef2 | -6.40927 | -43.04941 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6ee85965-34fa-3b00-8c84-6a4e98a38fa4 | -4.63514 | -43.18628 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| e3aedaba-eac7-33e4-ab76-3fad7c6d73d8 | -4.06869 | -48.95921 | 2025-10-05 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b32cf102-918e-3ec4-b1c5-8d12590b5e6b | -6.25913 | -45.35273 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9da1ab17-70ea-3477-962a-f09f6d2fcc77 | -4.26906 | -46.74678 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3437348e-41e1-3149-970e-1f4e7bb9bedd | -5.91345 | -42.52796 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 080a29d8-2bb5-3ad5-aadd-1b9ea323b547 | -6.45847 | -43.44532 | 2025-10-05 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4451e4e3-2970-3af3-9988-e0cb921ca22a | -5.66744 | -42.74614 | 2025-10-05 04:44:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f0d4eca1-cd5b-383a-997a-d76514357f8f | -6.35285 | -43.91507 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 459e4a0d-9351-3609-ba5c-4072327e02bc | -6.14728 | -44.66277 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dea57553-f981-361d-9481-ea30e90ee7b1 | -5.78451 | -42.92801 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a1ed082a-a648-3ec0-9809-7965c5697519 | -6.52697 | -43.37497 | 2025-10-05 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 22c08ccb-f3ba-383e-8e5e-87c66d5ba2da | -5.64882 | -43.92135 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a32daac4-e55d-316d-bea7-75c83d4e8edd | -6.6592 | -41.59405 | 2025-10-05 04:44:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6b8051ea-1fd0-35a0-85b9-52107d498bbb | -4.25993 | -46.77091 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5789fe5-f3a2-3089-bdd2-3ebfebe3d60b | -4.26316 | -48.26084 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c14ae638-b5d1-34c1-8add-f4511ae6300c | -5.91302 | -42.53098 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 199a35e0-e79c-3214-b8f3-ad5ccedc590a | -6.15859 | -44.64666 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4cf6524d-dbcf-3604-bcab-4c7c02cd39b5 | -6.15047 | -44.67175 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 01a68722-4291-3081-b272-841376fa488b | -6.27962 | -44.03612 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1c5ebe7-0678-355c-86d0-14d6d43a1475 | -2.68073 | -48.39584 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8753cfec-4402-3489-804c-238c4852dca5 | -6.37232 | -44.30997 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fae22e3-461e-32cf-bcf5-a2c1e49d71e2 | -3.67045 | -41.75726 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68b18d7f-1b99-3f10-a207-7c5a53091492 | -3.77903 | -43.36569 | 2025-10-05 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62865fde-af74-3026-b7be-4c58f2bcae86 | -6.26218 | -42.45222 | 2025-10-05 04:44:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e5347f36-01cf-37b3-91df-33397a06e575 | -5.6446 | -43.91928 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2cc65bc0-5b99-3d56-bff5-247bd79c0b76 | -6.01901 | -44.0221 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be76706b-c92f-3e38-8405-8aefacc0ac66 | -5.23052 | -42.89678 | 2025-10-05 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dbefb401-521b-3986-90a6-46a031bb9e8f | -3.04257 | -51.47856 | 2025-10-05 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b88a4234-db31-3bf7-9d5c-e09451b1ec04 | -5.89031 | -42.91641 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| bf43bb52-e12e-3b67-8406-5664a4df3ac6 | -5.7722 | -45.7519 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a493e50-81f9-3e94-9a18-0a7233619b69 | -5.46212 | -51.00874 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53af2f51-3950-3749-8258-968d6f6df04a | -5.78044 | -42.93347 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4ea12866-cd7f-36b4-8b09-cc241e1ad935 | -2.89894 | -50.72695 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57e1d2b5-8fc5-3fc3-93ba-85b67e761e68 | -5.65075 | -43.20361 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03d7a519-f2fb-3ef2-a25c-eaa166607bfa | -0.90943 | -47.55 | 2025-10-05 04:44:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c778a256-7813-3b31-8d72-251fe7d6138d | -3.09367 | -47.01881 | 2025-10-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d72fa1a8-c414-3fa0-85dd-46c44bbc8473 | -5.88891 | -43.70928 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4dc4141f-777b-3ae9-a1e1-fda6e77e37aa | -4.6344 | -43.19138 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b1d712fe-4603-311d-b3a2-03a904a8b85d | -6.63811 | -42.79705 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 28ec60e0-06a1-38ae-891a-118c8482c34c | -2.89456 | -50.73332 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3737738-1948-3b40-8a18-9fa77f6b9a7e | -6.08147 | -43.48199 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de271009-fbd4-3571-ae21-f39d5f3662f6 | -4.22704 | -46.76132 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README76.md)
