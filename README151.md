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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c001f50-e812-37d0-8ce2-49dba56ee5a9 | -8.34649 | -49.71294 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d3120dc2-9fbb-3c2d-9f06-b96b8d8a1e16 | -8.34595 | -49.70947 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf4af8c5-3afb-3b8c-98eb-619b6336bf7b | -8.34264 | -49.70998 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 64ac08d1-3292-3195-bbbd-d83772c1ebcf | -8.22491 | -49.98144 | 2024-10-25 16:52:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ae0f411-5299-3b29-a317-43f027995157 | -8.06956 | -49.72558 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32238ff5-e7b1-3601-a017-1b882f6a35e6 | -7.89745 | -49.82079 | 2024-10-25 16:52:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5fccbef7-2235-3a05-b443-f9be792fbf73 | -8.78427 | -48.82885 | 2024-10-25 16:52:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 3f18ba72-96f4-36f3-8376-806e0959c4b9 | -8.78372 | -48.82529 | 2024-10-25 16:52:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 9e1fd36f-705b-3327-8dce-2159e56cfa73 | -8.78248 | -48.94928 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18686722-f93f-39d0-803d-aa690cc9ef28 | -8.78093 | -48.82939 | 2024-10-25 16:52:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 08477f88-4f13-3141-8b05-66790e5bef28 | -8.76566 | -49.47758 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0117805b-dfd6-3d63-8424-e0dff78c3074 | -8.74672 | -49.15756 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cf3ae83-a43a-3d6a-b840-3655f090a254 | -8.74352 | -49.15809 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c67dc4ef-760c-3e87-880d-e342ec1c0c3b | -8.71283 | -49.00381 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b23da0fb-a844-3980-bc27-608222cafb58 | -8.71228 | -49.00027 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 14af5f82-c3e9-3aea-82f5-fd763bf3c94c | -8.7095 | -49.00433 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1962e3c-4d82-3ba6-9943-b5aaf33fd3f7 | -8.70895 | -49.00079 | 2024-10-25 16:52:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f0e8e693-ef9f-3c15-98f5-12a960abc095 | -8.63228 | -48.99115 | 2024-10-25 16:52:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0d285ebe-3905-3cad-a704-b54c8dcb79fb | -8.61342 | -49.04182 | 2024-10-25 16:52:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bd36cb98-e84f-3618-8e1e-20e821d721e1 | -8.61009 | -49.04235 | 2024-10-25 16:52:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 74d305cc-7e8b-3e11-a013-4b56e4b0c9ac | -8.59715 | -49.35429 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 31fa136e-239e-3171-96bf-c0507d52725c | -8.54935 | -49.57364 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e14a0574-c1db-30ff-b7ce-c4eb1d477e5b | -8.49114 | -49.5042 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d074675f-8c5a-30c4-8086-919a8591d901 | -8.4906 | -49.50071 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 80b36578-3823-383f-a3d3-6033f9982103 | -8.44827 | -49.16268 | 2024-10-25 16:52:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 484192ad-a735-3dbe-aff3-2c9ebf534b69 | -8.43105 | -49.1834 | 2024-10-25 16:52:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c07b4d43-5ae3-3e16-b106-bae6f04a5310 | -8.41398 | -49.00875 | 2024-10-25 16:52:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 14d39f4b-54d8-3624-ad18-473a38ddbf48 | -8.39196 | -49.43439 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b8cd9b5c-ad5a-3f54-9330-bb3cba62d514 | -8.31955 | -49.40645 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f129e306-d556-3a83-bb3e-b51b1b8c4d9b | -8.1666 | -49.16478 | 2024-10-25 16:52:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 48d48f85-4332-3c23-bf89-fa727bc8f580 | -8.16531 | -49.46359 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cbe533f3-9751-3ea7-94e0-57d94dc8f318 | -8.16327 | -49.16531 | 2024-10-25 16:52:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c9417d20-255c-38ba-b000-a2907a41b925 | -8.06384 | -49.37981 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b925aef-831a-376b-afeb-143f8c721002 | -8.06329 | -49.3763 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 05a7b422-2aa3-3530-808d-4f0215f449d6 | -8.05517 | -49.30202 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7690dec4-f0f0-3a6e-9a9b-8e695a48d6ee | -8.05184 | -49.30254 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5c0e58e-80b1-3716-ba28-f7f4f661a8a9 | -8.0253 | -49.63622 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 330baef4-a3ca-3253-b044-69828cc259e7 | -9.6692 | -49.29529 | 2024-10-25 16:52:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6c557ff-85cf-3f77-87e3-5e001489446b | -2.98614 | -50.29577 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0fa7cdd0-c2bf-3872-aa44-130fb9f5ce9f | -2.14499 | -49.48472 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9120df29-77e2-3bd3-8468-b571f8103cd1 | -2.14156 | -49.48524 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 33a26163-709f-338e-9edb-9cff7fbeb9bc | -2.13332 | -49.27577 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ba1120e-d67d-3aaf-b349-4db2441593cc | -2.13105 | -49.28384 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 704a70f4-dfbd-370f-a9f4-9737986dcc2b | -2.12987 | -49.2763 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bce77ac9-18c9-3e90-b35f-8e2e9ccb4621 | -2.12841 | -49.28419 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2dccdef6-e238-3064-a0af-693889cfb1db | -2.1276 | -49.28437 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f7886dd6-f589-3766-b8c1-6b882f11c401 | -2.12726 | -49.27664 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 25564dd7-b1d4-3d47-8bdc-c0cec516c058 | -2.12642 | -49.27683 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2c18794c-49eb-362e-bf7d-414c44edab43 | -2.12496 | -49.28472 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2bce9c6e-d63c-3375-b618-26cfc228e5b7 | -2.12381 | -49.27717 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c2270415-87df-35f2-a64c-eb0e6dd6d8f0 | -2.12151 | -49.28526 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4bb6070b-b68f-3d2e-a218-6bf9a6291aa6 | -2.12094 | -49.28148 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1a892f1d-899b-3687-8f78-0c55482f277e | -2.12036 | -49.27771 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d6944f64-1f89-3db9-8958-e7922da2b743 | -2.11691 | -49.27824 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1393bac2-a706-3c62-99b2-2114f5c9be99 | -2.11403 | -49.28254 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1d092f88-813c-385d-a95f-72d77d4a035c | -2.11346 | -49.27877 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 474fffe7-efa6-3163-b3cd-b7928aaab9c9 | -2.11172 | -49.26743 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8d7839dd-3f2b-3103-8fa1-0028ae613625 | -2.11058 | -49.28308 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 454c0c0e-58e8-388e-9c12-71bc70a6a0d9 | -2.10597 | -49.27606 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 409c1987-e99b-3e77-8395-0ff65fd9d337 | -2.09379 | -49.65126 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a3e9a741-fdd2-3602-90e4-5e4bdc7b5d94 | -2.23146 | -49.00277 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 6f9b052a-c0fb-33fd-9e50-6e72b781730f | -2.12135 | -49.06316 | 2024-10-25 16:52:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 4380cde1-232e-3234-819e-bd9b79affcb3 | -2.09422 | -48.82044 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 773bb96a-158c-3d94-b42b-0566e40feab3 | -2.05121 | -49.49121 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 49a5ceb7-edd2-300c-a259-bfa59c8ff886 | -2.05078 | -49.48781 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e656cd41-3adf-30d8-9594-501a8d60568a | -2.03231 | -49.59645 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af41735e-264f-31ac-883a-1f2ec8f69d6f | -1.99238 | -49.49646 | 2024-10-25 16:52:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| f406a360-8499-3316-83f2-dd3c39f3f497 | -2.99607 | -49.76721 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4bf48f38-8233-3c42-8c74-150351688a23 | -2.9927 | -49.76773 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9791f83b-b3a6-3750-98f5-72051b95fc26 | -2.99046 | -49.75332 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 8afaaa62-b29e-36d8-8ed5-7e1e8723756f | -2.98668 | -50.29927 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3489e413-bf97-3513-bcef-60d2b0664e66 | -2.98281 | -50.29627 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ecd56dbe-0c9c-32c2-b22b-1726d79b7a1f | -2.98258 | -49.7693 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1cc50a2-6723-37c1-a632-aa730640de81 | -2.97012 | -50.41269 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 97d28496-2cb8-3f62-9a3e-75c3b0909358 | -2.96896 | -50.42716 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ed4be475-e9c9-3f21-bb3f-7dbc04d39ae0 | -2.96788 | -50.42019 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0429c9e-1747-3c11-a669-7d90a0ba490f | -2.96734 | -50.41669 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fc981d66-fc6a-35ed-ab69-70889cbaf78e | -2.9668 | -50.41321 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c557fa65-226f-34e3-be40-a3dbb26d5709 | -2.96563 | -50.42767 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5445d72-f278-39d4-8787-eee7b12deb41 | -2.96509 | -50.42418 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46b55fad-f742-3429-be20-8cb18e0dc486 | -2.96455 | -50.4207 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 268f8e52-6d91-377a-81d0-6baf17730719 | -2.96401 | -50.41721 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ce28f2b1-8c1c-361e-9a89-10a8de8cd69e | -2.96229 | -50.42812 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 13967b30-3de6-381e-919f-d833422f35fd | -2.96175 | -50.42463 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6f80e36e-bbcf-3e16-9888-065e3be0293b | -2.96123 | -50.4212 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e6418cb7-daeb-356c-a1ad-7d058a4c21c4 | -2.96077 | -50.52803 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 77361770-5952-36fa-963c-04d89d395531 | -2.95897 | -50.42863 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2d3c0ee5-4923-3263-b165-b105762a8a0f | -2.95843 | -50.42514 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7a3d7246-601c-3489-8516-88faf84320d1 | -2.9579 | -50.42171 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 30e3a74a-600b-397b-a04b-e033ce3f6847 | -2.95745 | -50.52853 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4527125b-0a28-35df-a775-02f11b7121e5 | -2.95635 | -50.43251 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1d84bb5f-1e8a-3aed-963c-5bd0d69d6942 | -2.95529 | -50.4256 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 34f2afa8-5145-3517-b3a5-29350cacf794 | -2.93006 | -50.48289 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb4ee7cf-f7c7-3391-9a89-af763d1a1b11 | -2.90057 | -50.40179 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9672e45a-4469-394d-a018-4e367c78217c | -2.88364 | -50.46861 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e71b49ed-9682-3aee-902f-f0d0faeb67c5 | -2.88007 | -50.40135 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e2f5b23b-368e-3f32-aecc-c5ee52968f56 | -2.87953 | -50.39786 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 46c7efda-6304-3311-a419-7dc630137d56 | -2.87899 | -50.39437 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4d303144-4017-3878-a097-9e83ab11c905 | -2.87621 | -50.39837 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 83a9a005-07c9-3f6d-be69-cb586dfab619 | -2.8489 | -49.77537 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README152.md)
