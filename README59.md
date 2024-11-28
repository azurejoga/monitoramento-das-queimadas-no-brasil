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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa39032e-3cdc-3eaa-b797-1f91c655c8f6 | -2.74021 | -51.65992 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be65836e-9252-33c0-8161-957aee35a8cb | -3.978 | -46.99236 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b67ba10d-20ca-3124-9ae4-72014c2a85fb | -2.77346 | -48.10648 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e13616a-e5c3-3f3f-b6ec-5e3019a18506 | -4.17785 | -48.45158 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e853bfa6-0e44-3455-8134-672e7f988ce6 | -3.09002 | -50.35812 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccce5f59-4c1c-3a32-8774-c9bac8641d55 | -2.26252 | -53.47181 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e2f67bb-ab4d-3afa-8e7d-e9a6d52a5af2 | -3.2721 | -50.62535 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c605a687-1993-3b2e-9083-7129ebfbf4c7 | -3.57644 | -54.52222 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b8c1a27-9802-32c6-9248-e01f5ae32369 | -2.98697 | -51.44865 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a9e12085-ba4e-388b-9687-45232c1df250 | -3.94706 | -47.05712 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bef089c-8d65-395d-b108-a3339d34b754 | -4.43926 | -46.6091 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d158396f-1812-33ac-a8e7-10cd768290a4 | -3.2975 | -45.51273 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| da71d0ad-a78f-3a5c-b16f-2dc745b35ccc | -2.74719 | -54.03165 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9610d92b-dae7-33f6-b5ea-07d0fcbfe55a | -4.85706 | -42.66803 | 2024-11-28 04:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e035996d-819c-3137-8425-f9df66148224 | -4.04247 | -48.08101 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c167cd53-2afa-35fd-8640-a06670ac5760 | -2.84642 | -46.83769 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef40c6e3-3cc8-386e-a8ee-cb9aa53e2855 | -3.22753 | -48.82354 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92e0b48b-4c4d-35c8-b9f1-5d184754b3eb | -3.26804 | -50.62469 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8224beb0-fc5d-3b1e-8cc9-cbb54e2d33e6 | -3.06643 | -49.20043 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 431afb58-b1c2-3944-8134-66d476bc8ea0 | -4.35399 | -43.32373 | 2024-11-28 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14a90c47-8859-3dc5-8dfe-553a330aaf21 | -3.35398 | -50.50751 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fe955f5-b651-3c3c-adb0-2c0bdf98965c | -2.8756 | -46.84962 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1e07423-765e-35ca-ba5c-bbc473d502b3 | -2.52885 | -50.10569 | 2024-11-28 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 864918fd-966b-3470-a208-6fbb23b2905f | -2.86988 | -53.9847 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9578f473-60c3-383e-baa8-d1e0b1911f18 | -3.57617 | -50.33587 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6aeed35-0df9-3fbf-84ea-ea422ef7a62e | -3.97995 | -46.65528 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41c7f7ce-72a2-3ff6-b672-f2648b3da0c4 | -3.3345 | -46.61171 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e3d3927-e826-3834-9684-c8e75e790380 | -3.83333 | -46.53154 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d54961a-fb11-39ab-a8b4-81a0fe61ffe9 | -2.65216 | -49.51087 | 2024-11-28 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c4d6cc-2396-39bd-8123-978c2827be01 | -2.9607 | -51.00104 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0d637e1-971d-3e14-b2bc-7c35c180e038 | -3.15714 | -50.58809 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fc9315d-05c0-34c8-80e5-681235071ce5 | -3.92546 | -46.39979 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d415136-3ab4-3268-a9d4-182f070a1350 | -2.80261 | -53.04644 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f9001e6-5620-3c22-80ca-cf606326eb70 | -3.51043 | -50.31477 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4348e92-966c-3c99-aa09-4cf1873a23e6 | -4.04185 | -48.32893 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0caca3d3-909d-39c0-a848-e1d458971828 | -3.64546 | -51.39735 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a5ee550-83e8-36df-bf20-250144cc98fb | -5.21885 | -44.911 | 2024-11-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 93f158d0-a6ba-38b5-94d0-056dd74660bf | -3.68963 | -54.20713 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91510af8-beef-384d-98e5-9b45695c6fd1 | -3.10318 | -53.81904 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f3598a20-023b-375a-b12f-3f582409e007 | -3.93952 | -46.90948 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2efaec28-5c1f-36f4-a0e7-241911499b07 | -2.60214 | -53.96777 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb234914-47e6-39d9-8f76-86e174c9b92f | -2.14802 | -50.61499 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7634f43b-12bd-3fc5-99c5-e8d5748f3f4e | -5.31033 | -43.08317 | 2024-11-28 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed36625e-6fe1-3e85-b5d9-87a7853aae6a | -3.74327 | -51.84108 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38b72931-9aca-3cf5-af76-827c06f1e865 | -2.63481 | -48.40791 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17974ab5-59a0-38e1-83ba-8fbdf5462e35 | -4.41562 | -48.5938 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d582f8c7-aa82-3ff2-93d7-19a94973d61f | -2.85446 | -48.09795 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b3b81cf-bc95-38c0-8271-785685a31dc5 | -3.46398 | -44.92856 | 2024-11-28 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b03e2e0-68bb-3816-8cf6-4622917bb04b | -2.59598 | -53.97303 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d4cb217-1fc0-3db8-8562-917d15f9d6e2 | -4.17595 | -48.62441 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa0e609f-90af-3f42-a38d-3e3a38532b78 | -3.9699 | -46.71849 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 019d84b6-279f-36ea-a40a-fe37ef08b678 | -4.0233 | -46.66211 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 850d6ee6-3b2d-3d48-ae10-fefa3bfd879c | -3.32501 | -46.62829 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8360a486-d9b5-368a-8404-de5eca05b3b3 | -3.30031 | -54.17831 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31380cee-32e5-36b0-9624-cd5784c837f4 | -4.19987 | -46.5539 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ba13ac-8af1-3fbc-b0e0-f7efcbfe80e8 | -3.16975 | -48.43685 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 616b8c85-f3ec-3b7e-a176-f7b1af603184 | -2.6904 | -51.7974 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8572801-6d6f-3601-97d0-d8f2a37729a8 | -4.18837 | -50.68629 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f24286c7-213f-349e-b53f-7da84e881908 | -3.19579 | -46.56871 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53e08ba0-ab22-3d68-b144-c1c6141edbab | -1.62781 | -53.87034 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e1f2fd7-3c57-3a4f-98be-3fb8fc2c67cc | -3.18112 | -48.43449 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28fb0657-086d-33b7-b336-dd2c99818a38 | -3.29718 | -51.19532 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ae88fec-c199-37fd-8c5f-d5c3a7fed2f0 | -3.12259 | -53.10042 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a196a8d-547a-3e78-8e86-145f5bb47c32 | -2.87919 | -51.58208 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ddd10a6-0b7f-354b-8d23-febfeb760186 | -3.459 | -54.48413 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f707b5ac-40e1-3c99-bca1-f18e62601338 | -5.22273 | -44.90799 | 2024-11-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d7787639-d3a3-30cc-9622-01741ad51fcd | -12.09668 | -49.48772 | 2024-11-28 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b44143c-0236-381c-bf43-04bbef9c36bb | -4.01413 | -46.99453 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7bf1e1c-5632-3d97-b3bc-8097a4b75c4b | -4.74027 | -46.51077 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac7a3a8b-92c5-3419-a03c-1ee4a8fb01f1 | -3.30363 | -50.27731 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d146f56c-78f3-38df-9a2d-51ae496bb9d4 | -3.69305 | -50.22868 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 533133f8-2c01-3f37-bf47-eac88db38f04 | -2.72065 | -48.66795 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 818dbb06-7649-333a-ad54-8fee62b13167 | -3.62403 | -51.50037 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dddcda34-dd32-324a-9d85-c3dd90c1bf47 | -5.06729 | -46.16133 | 2024-11-28 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caa2550c-177c-3374-85ff-fa706a8c8c23 | -3.33625 | -50.07611 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af38ebf2-47b4-30f8-8c8e-97cb79cca7d5 | -3.96691 | -46.9102 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d6f1fbb-7ded-3ae9-a860-5eff95aeeaa6 | -2.63193 | -51.77193 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 019256ba-a9f2-34e3-a4d7-2dcca307a4a6 | -3.36736 | -46.66388 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 978fcd44-b5a2-33f0-a1ce-66a2b5a0bcf5 | -2.60629 | -53.97477 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcfa54a3-5b94-3132-a09e-545a4b95aabc | -3.29696 | -45.51617 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 308c9360-0cbb-3d22-bd53-5c7ea7053dc4 | -2.95909 | -51.06371 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef1efead-d242-3faa-a8af-58b84724d7b8 | -2.74202 | -54.03085 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65953b58-90a5-3d8e-8a39-edb728a7a9c6 | -3.96283 | -48.07742 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c9d27093-08ae-3da2-b46c-c1743c6c7500 | -3.99976 | -47.91438 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 062a4f15-e8f8-363b-b2c0-bf4133536cde | -2.01294 | -51.1869 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c40029e1-6e5d-31e7-b7a2-e476ec1b7603 | -3.06088 | -51.29123 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a6309fe-957c-3283-9914-27a381eb65bc | -3.17557 | -48.6317 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 770d68cb-cd36-3ee9-ad28-66230d406353 | -3.69387 | -50.22375 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c37bb11-14db-39b1-bee1-6366f5da92e4 | -3.16568 | -51.09931 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd053d36-c3fc-3d32-be92-ae5fc0449373 | -3.2824 | -50.56131 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d842571f-fed4-335b-a73c-73212f991b19 | -10.9415 | -49.42759 | 2024-11-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e095a14-a7c5-3a76-a4db-0c86b6748426 | -1.84361 | -55.57226 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 795f0b74-6be4-3663-9460-002046f82268 | -3.37295 | -50.12289 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74d4d4c7-0b62-3ab9-b27c-6ceb015c4b20 | -4.12322 | -48.81787 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b685c2b6-a0f4-3e42-83d2-8aec3ac2ee87 | -4.02308 | -49.54301 | 2024-11-28 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d3407b0-6e40-3e4f-9a06-0b5ba9f35cca | -2.93901 | -49.12698 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27694b4e-0597-3e51-89bc-1d6dd859e6c6 | -5.10938 | -44.76797 | 2024-11-28 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 269b0556-6ca4-37b6-a285-be7308b0706a | -2.87223 | -46.84909 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 845688d0-512a-3d56-9a95-b1da8c4320f7 | -3.04982 | -49.52423 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e1d8e65-9693-3699-86e7-1f78ba53b25c | -3.92919 | -47.01759 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README60.md)
