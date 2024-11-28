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
| 855d8ffa-530b-39ab-9ddc-5bb5ffda5f6c | -3.38848 | -50.11386 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b8026e77-a230-3b93-9a09-d19be0b8442e | -1.33576 | -51.94272 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f6a9be2-7f27-3ab9-895a-c62c4433aa85 | -2.72725 | -48.89849 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 632ca2d9-75e7-3fff-9d82-3681bb6804d3 | -1.57791 | -52.26754 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43fdb21d-fc1b-3340-bf65-a92465860a56 | -2.94983 | -51.58685 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4326c9e6-35fd-3efd-98e7-724e42f45436 | -4.31244 | -48.0806 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f1b7192-2581-3cb1-9c78-667c025c551b | -3.94341 | -46.6944 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 861a44e8-e74b-38af-8fcd-19e76490538a | -4.66261 | -49.51727 | 2024-11-28 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37011d74-2d79-32d9-a18d-028a7dad11b6 | -6.43744 | -35.45825 | 2024-11-28 03:59:00 | NPP-375D | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6de2bcd-676e-3f42-af5d-a0b40adb00ea | -3.37074 | -50.82671 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a413887f-c0a7-39b5-9231-fde04145f548 | -2.80622 | -51.58503 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c1c37d7-4d5c-3ab2-9365-6ea4dfe3ae4f | -6.16452 | -42.61964 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e1901482-b522-39db-9780-9feb5e2f53b8 | -4.06097 | -48.83483 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38257bbf-5c7a-3938-a4c2-b55a319e0b10 | -4.00097 | -46.31101 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6256b205-300f-33c6-9757-6b8adcfddaaf | -6.12037 | -41.93213 | 2024-11-28 03:59:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 78b378b8-62a2-3d6f-8728-9bf4ef87870f | -3.78886 | -50.13483 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74cd8724-76e3-3057-93b8-837dc9efa66f | -2.73926 | -51.65683 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 928b9fb0-aa6a-394a-bf0a-80d4e022e89c | -3.08817 | -49.20862 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19d2935d-2941-34fe-8f51-6c0a19be73a0 | -3.26326 | -45.37631 | 2024-11-28 03:59:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50844ffa-9361-375e-81ed-9df3e6283646 | -4.5369 | -45.87915 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b54a6ba-740e-3d03-aa74-b3a1daed89d3 | -2.31235 | -51.96487 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9216d9df-b214-36bd-a6d8-76fe98ea0fcc | -5.62522 | -39.69473 | 2024-11-28 03:59:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d42f690-6ef2-3f76-90d6-84e18628ad3a | -4.01096 | -46.98876 | 2024-11-28 03:59:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb5a392d-14ea-338c-8436-c58a48e72c68 | -4.18399 | -44.25995 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e136d17-8756-3cf7-8818-c9871dda4324 | -7.308 | -42.09855 | 2024-11-28 03:59:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dcc983c1-6431-3a36-8c6d-50d9df76669c | -2.63422 | -51.77148 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ed8c37b-857d-3888-a7ad-770d757e9268 | -1.34917 | -51.985 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcbc5138-1fa5-3f48-a5cb-b6e4a3946b38 | -2.31359 | -51.95753 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f6f38f4f-50a5-31a5-91bc-cf9f89b700ee | -2.86675 | -46.87359 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7a622173-24bc-31d4-97de-46a9095346f8 | -6.71944 | -39.12495 | 2024-11-28 03:59:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7854d97-2f36-38f2-b955-51f10bc0a730 | -4.18096 | -48.62806 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 107bcba4-b8b8-3e60-976f-16af1601a691 | -7.03491 | -35.00145 | 2024-11-28 03:59:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df568699-1f09-3d3e-9d19-a699a46c1b7f | -3.70518 | -47.12685 | 2024-11-28 03:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0987206-86b6-3836-bb7b-aaa6a2f3d127 | -6.16808 | -42.6202 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 91de3d52-e3d3-3bd5-bafb-b4769824ca98 | -3.34637 | -50.51462 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df82c269-b27a-37c1-a90c-1fe0d8400d95 | -5.97829 | -45.37539 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96bc1a35-e19c-3765-a4a7-3ea76f91863a | -3.86335 | -40.71013 | 2024-11-28 03:59:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 962d0b5a-2aaf-3299-8e80-ef0c98af9226 | -5.30824 | -43.0804 | 2024-11-28 03:59:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e3978d1-9f8a-36fd-b221-ce0b0180d7fc | -6.56557 | -44.63244 | 2024-11-28 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16a0886b-818b-3ede-bf6b-1d2b9b7f2beb | -2.85784 | -46.86668 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db773369-803b-3366-8968-8877f0bb8b16 | -1.68125 | -52.49891 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b34779c-f815-301e-a847-9439b761da57 | -5.83027 | -44.10781 | 2024-11-28 03:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 88ba8d10-c95b-3350-8fbf-17a7d06282c7 | -1.68951 | -52.49322 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7c7015fa-efa3-3fc3-8e76-b20f6b3ec947 | -6.73618 | -38.78373 | 2024-11-28 03:59:00 | NPP-375D | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30c1c728-e84d-39a7-be69-aacfdc41c0f6 | -2.17293 | -47.13888 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f796661-a2bb-3198-ae21-195a5442ef35 | -6.57294 | -46.56935 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47fc831b-5032-34f3-97bb-e03f2dea333a | -4.16806 | -46.66581 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee4792fc-c24c-3871-b6ba-43bba63ac9c1 | -3.08082 | -49.20831 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71283ebe-7c41-35d1-a579-bb29560116fd | -4.88529 | -45.73176 | 2024-11-28 03:59:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1da64d6c-f150-3068-80f0-4147cc05c909 | -4.02291 | -49.54294 | 2024-11-28 03:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44504579-3d4f-300e-9766-2c8525833fd3 | -2.89441 | -51.367 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df3a42fc-1781-32db-b588-946719e61ae1 | -4.10729 | -48.24945 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64c3d861-a8e9-3b1a-82c2-dab62fdadac3 | -2.94224 | -51.59126 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9deb4ef9-f91e-350d-b154-10db3d241dbb | -2.85607 | -46.86489 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2556ef34-fd10-3aba-a392-c7437d6bfea6 | -2.84407 | -46.85883 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da183728-908f-3b40-b6ff-6411f85cf99e | -6.00931 | -38.66408 | 2024-11-28 03:59:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 906e2c5b-b523-34e3-8859-823cc31554e5 | -3.44196 | -50.02747 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e02a1b4-d754-3183-9434-4119659dc56b | -4.68778 | -45.81142 | 2024-11-28 03:59:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72b98dad-2c32-3bf2-84de-7dd45c08e580 | -2.14051 | -46.48375 | 2024-11-28 03:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a61d2fc5-9f5e-3302-86a1-f005d00b1b4a | -2.81151 | -46.82969 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 743e955c-59bd-3c0a-8f9f-339c39034695 | -5.98504 | -45.36069 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5db54487-c18d-322f-bc77-918e00fecec1 | -3.28149 | -50.55799 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 153f094e-082d-3280-944b-55ef9afc59bc | -6.70052 | -47.27151 | 2024-11-28 03:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5ad576a-0ad3-3a1a-bed9-ebeb76a1743a | -3.3156 | -50.03228 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fd9cec6-3a9b-3d09-a5b9-cb2d05148fd9 | -4.00375 | -46.31481 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2a6cdb6-92f1-38b4-8a0b-b0e43170b93b | -6.38002 | -45.68866 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3b57ff2-e098-3038-b316-024d62732e72 | -2.65547 | -48.50876 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54652dd9-0f33-395f-8749-47687ada8588 | -2.84803 | -46.85232 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5315b29-501a-3d31-a936-7829379cd85f | -8.66268 | -39.57182 | 2024-11-28 03:59:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c657f6dd-2aae-3bce-a9c2-5854da4e4c11 | -3.46283 | -43.52472 | 2024-11-28 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 757426a9-726b-39e9-a0ec-8a866908bfc1 | -2.17685 | -52.13763 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e73ac7fc-775b-3f5c-a8c3-64c910f361e4 | -3.94415 | -46.69255 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 185a97e6-ea7b-3504-96d9-a2956c1cbd61 | -8.40979 | -41.9224 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee0e3f0e-bf61-3abd-be31-e2096edb8ab2 | -3.96012 | -50.18883 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 040b3c3f-af11-3aa8-8964-3655a744cb7c | -4.51627 | -45.81239 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40046258-0e71-3291-8b37-1e4b159de083 | -6.11723 | -46.59629 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c5a343e-51c9-31fb-a5a7-19201f5ef611 | -3.98335 | -46.98856 | 2024-11-28 03:59:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3a09272-7499-347f-847a-21c9247b932a | -4.2167 | -50.89705 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b15df462-0a18-389d-809e-391aa68c243c | -2.84715 | -46.85779 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0abf0d7e-f702-3eb6-ae30-bc1fb20c108d | -2.84897 | -46.8596 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3ffb0d8-8320-3cd1-8ca2-7d638c775d74 | -8.13379 | -44.47483 | 2024-11-28 03:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47ad47ab-ba12-3b7e-9b59-ce977d702c92 | -2.5117 | -45.19399 | 2024-11-28 03:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35d80416-3f44-3877-b690-4feec854efd3 | -4.18686 | -44.2676 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b938b62f-c4c9-3f82-828c-a84cd41fc3cb | -2.85478 | -46.85493 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 383e3dab-163b-3e87-b3c1-3300be3d8e9a | -3.24058 | -50.77333 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 945c955f-3387-3623-920f-9ed0fad3c605 | -4.22112 | -50.89104 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c18ef5c-435d-3ade-970e-97b2c32e24bb | -3.8583 | -46.50584 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90431f50-e3a2-3714-9d25-42acd50c3245 | -2.53585 | -47.33186 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e90bd746-89d0-3911-b6db-2c139c186629 | -6.17521 | -42.62133 | 2024-11-28 03:59:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7a579656-8dd7-36e9-8e53-65bc4a0e410c | -1.32776 | -51.94798 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a78c4a4-34fc-3647-82f0-f037cde48174 | -3.70919 | -47.1331 | 2024-11-28 03:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17436e88-26e1-35db-96d2-3ab258ad7441 | -3.08588 | -49.21323 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9d20af1-25a3-392d-86b0-8f6ca17f7741 | -4.83568 | -44.28939 | 2024-11-28 03:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2aac996-d080-3c7e-8bf3-9c20c4d910f7 | -4.06586 | -48.83928 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e2325c7-ed04-35ce-bf33-e77d2fa72c0c | -6.18953 | -44.42784 | 2024-11-28 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| faf6d5d1-5187-3253-9cc4-d948eddaaf5f | -2.80524 | -51.59094 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3064bf99-e0cf-34a1-9d8a-ebf373710d98 | -2.84313 | -46.85153 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3aed61e1-deb6-3b24-b570-b4b40129619d | -5.88831 | -40.12999 | 2024-11-28 03:59:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0fb3586b-3929-3950-964e-895cb66d6987 | -4.14252 | -43.85103 | 2024-11-28 03:59:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d6ef7b7-ef49-3b2e-9f65-bfdbf90c6bec | -6.75509 | -35.09886 | 2024-11-28 03:59:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |


[Clique aqui para ver as próximas entradas](README34.md)
