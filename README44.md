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
| fec94527-a68c-3c24-abfe-e797609aa088 | -3.53403 | -45.25998 | 2024-12-03 04:29:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bb5c746-6dcf-30eb-ac5e-328db9b03fa1 | -3.90265 | -46.65705 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce9b1438-4c01-3915-a241-b729871da295 | -3.78679 | -46.7024 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29dae30e-6c2c-35d4-9030-29d516e31906 | -3.96828 | -46.6282 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c40036df-c300-35c5-8923-1449b476985a | -2.6768 | -46.61055 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c5a79f4-adfa-3b0c-9e16-43410b62a01a | -3.83061 | -46.59585 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1db02cf3-ba3d-3540-8d72-9ff4af49cbfe | -5.54118 | -43.894 | 2024-12-03 04:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77a69b5b-bee6-387a-8ed6-b99ec7332cc5 | -3.80226 | -46.5382 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dbe0dfe-108a-3600-b386-1a6c77df4d18 | -3.29037 | -47.03031 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4420cec5-9648-3d25-8c38-9e14322acc65 | -4.45175 | -47.61516 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd6b3794-69b6-32ce-8166-e60a5ef91cb9 | -4.05079 | -48.08852 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db7fcf74-7539-3e62-9cd7-768dee3f1025 | -6.74822 | -46.83155 | 2024-12-03 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ab8f1b1-e5bc-3e6e-a196-1001f6319818 | -2.66293 | -44.98223 | 2024-12-03 04:29:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68e31043-2c44-30b9-b86c-543a83bf6b65 | -4.43786 | -45.35001 | 2024-12-03 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b73d8f5-c975-359e-b6d2-8f785c6e7a3c | -4.19386 | -51.18184 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fde6daa-0939-3eca-95c8-3bfb3d27c68a | -4.31478 | -48.09421 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ba4cb79-0d75-3cd1-b341-9b8918f560f1 | -4.75182 | -48.08102 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e6ddb5a-749b-35a7-8800-a22881179d99 | -3.85012 | -46.66623 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50e64162-dc6e-33af-a49f-d998bb79c6f3 | -1.70111 | -52.77202 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aadbaf73-bc55-31be-ad2e-633b83be08cf | -2.5635 | -46.40201 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a4df252-dc1a-338f-8866-0f0b5c9f5d81 | -3.95652 | -46.91998 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9828cac-7770-35bd-b329-d328544a575f | -1.72894 | -52.65086 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 238c1b80-643d-368d-ba20-a6c5d5be76e6 | -3.55123 | -50.17815 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 551a6195-0c7a-3b92-97b9-0ee2e7d17553 | -2.55239 | -46.55912 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 057ae23b-3e9d-365b-8287-ae46cdd25d24 | -3.77023 | -46.69982 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 416d292a-2852-37f7-b675-0b86ec9f8501 | -2.79684 | -53.05554 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eba7a2c5-03c4-30a2-9c36-701adc0187d5 | -2.82675 | -51.83837 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 857c7d14-fc95-3843-beb8-05407db6e1fe | -2.41398 | -48.88297 | 2024-12-03 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98852526-ff01-3699-b818-afddc8b5753d | -4.90276 | -47.14611 | 2024-12-03 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39248268-f9a8-33e8-84f0-31398d6c4d91 | -3.47323 | -49.9259 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cb36c6e1-599d-3ef4-add6-254834e71a62 | -2.75623 | -46.12718 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9f7e00a-2b22-3284-8ec7-f7db9fa893aa | -3.17667 | -54.33406 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2997e78a-77fa-387e-97e1-c755ecc94287 | -3.56098 | -47.38344 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f26821d5-f4f3-36f7-ad88-274fd9f8f6b3 | -3.86532 | -46.35215 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a86863c1-9db3-3b93-98f5-b7de9203b5fe | -3.89278 | -46.6768 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbc2d9a0-4ba1-3331-9956-2e9aed41aff0 | -4.74266 | -45.71239 | 2024-12-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cd7622b-87b9-30a6-9e82-ed74b79b2ce2 | -3.99744 | -48.29586 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02d16df8-ade3-3ece-8957-bc31bb51a925 | -4.04714 | -46.81757 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9557eac-be9a-3aae-bd49-ec0d415baff4 | -3.11891 | -53.99223 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08002a53-b50e-308c-aad7-f88124cadc35 | -4.00078 | -48.29639 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7e83ecb-6b7f-39ef-a6f4-acb3793bbcca | -2.68619 | -46.61553 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ec0412f-4f09-3a36-8c3a-cd1fe62d1d95 | -3.07771 | -53.38012 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 035342f5-3f22-3ebf-801f-d57bcd40d667 | -1.99881 | -52.09418 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c4976f4-6e5e-3321-ad51-d7314c6a3f36 | -3.98344 | -46.72635 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4378177-3f7e-3276-9cfd-6b201d6898fc | -2.66235 | -44.98592 | 2024-12-03 04:29:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a04fbceb-17a0-3c26-89ce-968860d15b97 | -3.25274 | -53.63346 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 005f4691-7560-3c36-a2fd-e5dd6e61ac25 | -3.02558 | -54.18464 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9425ae44-1d5c-330f-a729-722c5f3fbc80 | -3.98019 | -46.53061 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b308a649-8a03-327f-a1a0-48df84a8a7a1 | -2.71851 | -47.55465 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2919f90a-11fc-396c-8c56-380ede96bfb5 | -5.11422 | -43.20959 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 42c876a5-1e83-3e00-86da-72b823063c40 | -6.6846 | -48.8722 | 2024-12-03 04:29:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9160a29-22de-3c06-819a-8f165ad4ef46 | -5.73936 | -44.43411 | 2024-12-03 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90c9cf2d-ac75-34b7-88b9-699f9cb950d0 | -3.76759 | -44.05618 | 2024-12-03 04:29:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1528fe78-c0e3-3ac8-a121-c2d815cfe21f | -4.18182 | -51.18462 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 891666c5-0124-3dcd-a4d6-363e4640e6a4 | -3.61363 | -42.74219 | 2024-12-03 04:29:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d89b82f4-fcc9-3ffe-a4f4-90dab0a135db | -3.20564 | -53.12239 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09955754-60ff-34c8-a662-1f588304d5d4 | -4.09398 | -46.12573 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38b61af3-c957-3d37-9101-c769c7daaada | -4.01408 | -47.00649 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83c2175f-0ed0-301c-94dc-1ca96679bde6 | -5.81519 | -46.47761 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7204f129-ea6e-3978-bac8-ae9d8e6d7e72 | -2.68011 | -46.61106 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39e2b4f5-3450-39ab-9fcb-2f1e7af8a40c | -2.73907 | -46.12808 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9d8cd9b-ad4e-33e3-9cdd-9bda1edbb4de | -2.56681 | -46.40252 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6865652a-81a9-3abc-9843-ed4c1f1813f9 | -3.33961 | -50.07504 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d205a5db-1939-3abd-b9db-8a96c73aa246 | -5.58609 | -45.14782 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99f005e4-0bb6-3db7-a80d-cd71a7b93445 | -3.26243 | -46.45073 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 123382ed-ddde-359e-bade-236d19baf220 | -3.31478 | -44.91149 | 2024-12-03 04:29:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cd8e70f-1ed6-3236-acf4-5ea1be823386 | -2.67572 | -46.61743 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f91531dd-af66-3e4f-b3bd-b5de98465555 | -3.97859 | -47.66448 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce845cfa-9528-349b-a91c-53d6f25c7ef6 | -5.37278 | -44.04435 | 2024-12-03 04:29:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bf5b205-ec10-3def-9079-d228378e7b0a | -2.56439 | -46.33146 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f8fe6fd-6028-3fbd-9411-f02834bfe055 | -3.51199 | -53.8328 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74015340-0166-3e06-ac7f-78d1fde5db60 | -4.15097 | -48.22948 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aa851ff-03c7-30ab-bd57-c6da80b054e2 | -2.32929 | -45.86035 | 2024-12-03 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e00cac-0463-30ac-b83e-80f2de117eb8 | -3.80172 | -46.54166 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea0181d8-cc01-36a1-a747-1a8a8a836307 | -3.99966 | -48.30345 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16dd4115-99f2-385d-a5da-6b4aa56fed20 | -3.55415 | -50.18286 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d9fb6d8-edfa-3ae5-8af7-a82a8c82540d | -3.85304 | -46.51771 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cf7f88c-8930-30bc-946a-36beedb66e87 | -2.62222 | -46.95757 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8226ea8a-2c19-3e7f-8715-9c9811aebe43 | -1.70103 | -52.605 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe48fa37-3efe-3b55-bcb0-e103825d4efd | -4.1901 | -51.18124 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f66a62c8-7850-36ff-b4a5-f03c3f07d1f1 | -2.65951 | -44.9817 | 2024-12-03 04:29:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8063d88-d02e-329c-baff-7dd224747fce | -3.50524 | -50.06265 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c58eea9-8304-3629-9b02-7d18f7dc0e4a | -2.7291 | -45.20998 | 2024-12-03 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 823d6eb8-63d5-338b-8474-e9d79574eeca | -4.0348 | -46.93924 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66feb358-c361-3a42-859f-ae0ce1dbac92 | -1.69675 | -52.60431 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddec8167-1990-3fe7-8bdb-1ba3f9cc228a | -2.8357 | -46.85342 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88c6ef16-d531-30eb-826b-d2a1a91a2ef7 | -2.75619 | -46.10578 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d016f11c-0c17-3a69-a6e7-c45652257684 | -3.06575 | -54.05693 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd3cb3bb-5538-31bd-9e9e-313b81db3a2f | -2.92161 | -48.02986 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68b9fd81-01b2-3d47-933d-2b50b23af531 | -1.22832 | -53.36331 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbcd84b3-def1-3ac7-98a3-925f91f216a1 | -2.65365 | -46.60696 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 214aa4dc-ee90-3e2a-9f26-cce141231fac | -4.11336 | -49.0653 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed08e750-bb54-3346-9125-08250dbf40b5 | -3.98182 | -46.73669 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc227e6e-63f2-3605-849e-eb537b3f37db | -6.02412 | -44.00779 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8bcdcbfa-eede-3a40-83c5-2229318578fc | -2.80954 | -53.03211 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c849d7b-d428-391f-b4c6-fd27c822e50a | -2.85107 | -45.39211 | 2024-12-03 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1458645a-3232-3f60-a7c7-333ed3103d1e | -3.16845 | -46.63796 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 580c572c-84d5-354c-b5c8-56fbde9ef7ac | -4.29253 | -48.21249 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02352b70-96a1-365a-a03d-20554dba97af | -3.26617 | -53.63566 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 779a7a3b-b142-3319-b248-26f9521b0571 | -3.25009 | -53.93685 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README45.md)
