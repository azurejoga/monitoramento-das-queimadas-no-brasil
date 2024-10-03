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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f7579eb-e297-349f-901b-069e9b2bc862 | -21.37286 | -46.45955 | 2024-10-03 03:38:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e5b83f2c-333a-30ad-9338-2510830ae44a | -21.3721 | -46.46302 | 2024-10-03 03:38:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0a1d5807-1598-3b7b-a699-dff0f0a3a015 | -21.31603 | -41.40239 | 2024-10-03 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5b1218b1-ea40-318d-b211-47cd0c163c27 | -21.31221 | -41.40177 | 2024-10-03 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2dbaf644-a703-361e-b1dd-5162be299302 | -21.3113 | -41.40667 | 2024-10-03 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d231007f-2849-38a5-b70b-35b8c4684cd7 | -21.14519 | -43.30691 | 2024-10-03 03:38:00 | NOAA-20 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| d5daa53e-e9a4-3238-a7f5-0b4fad206533 | -20.95656 | -43.31331 | 2024-10-03 03:38:00 | NOAA-20 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9a122ec1-c50b-37e7-acfc-0afb533c029f | -20.93087 | -43.37583 | 2024-10-03 03:38:00 | NOAA-20 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 996ecc68-e3de-3f95-bf1f-dc5e0827010b | -20.85431 | -42.23145 | 2024-10-03 03:38:00 | NOAA-20 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c6ab3aec-8cc2-34d1-9fac-a62e9d993b8e | -20.85357 | -42.23537 | 2024-10-03 03:38:00 | NOAA-20 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3a9a0c5e-8d86-3e8c-a8ee-36458852f49c | -20.85029 | -42.23069 | 2024-10-03 03:38:00 | NOAA-20 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 392b96ec-25f0-304c-a73d-8394b1dca2ff | -20.84957 | -42.2345 | 2024-10-03 03:38:00 | NOAA-20 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bd198029-0fde-30c2-9e36-34bd5a6b339e | -20.81786 | -43.67172 | 2024-10-03 03:38:00 | NOAA-20 | SANTANA DOS MONTES | MINAS GERAIS | Brasil | 3159100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9d8a5a7-0bd4-362d-9b06-5146ad861dad | -20.81758 | -41.62764 | 2024-10-03 03:38:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5dcca9c0-0e28-3fe5-884a-6ceffce06099 | -20.81474 | -41.62136 | 2024-10-03 03:38:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9e8a48c0-da9b-398a-8457-10371fbaed79 | -20.81452 | -45.2951 | 2024-10-03 03:38:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a41db907-5930-34b7-b203-6be621de84f9 | -20.80862 | -42.29628 | 2024-10-03 03:38:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da58469f-4c68-3989-9546-4ae375110ba2 | -20.77081 | -46.31451 | 2024-10-03 03:38:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6a99062-1d34-3d82-97bb-9723fe7e0c96 | -20.77001 | -46.29306 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f7f484c7-f197-3cbb-8c3d-93b358831786 | -20.7693 | -46.29637 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c409e6bf-41f2-3160-8bd7-2398af5b39ff | -20.76859 | -46.29968 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d1e898b-e944-3873-bfd3-342197fd3410 | -20.76714 | -46.30637 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93d51a3a-f91c-3056-a052-5167ecf7e850 | -20.76641 | -46.30979 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ed86df0-7a5d-3a30-b807-8f5ae1a7848d | -20.76335 | -46.29885 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6a6c45c-8b26-37f7-a29c-55a74bcb87c2 | -20.76264 | -46.30208 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 966485ff-dfdc-320e-8f80-d3bae2413578 | -20.76194 | -46.30533 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c6f453d-15ad-37d8-96bb-e6ff6f834709 | -20.69116 | -41.98165 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| aeeac305-b4ca-39c9-af99-01a87a6728f1 | -20.68724 | -41.9806 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 4260a225-848b-3634-bcdf-8071f0c7a2fd | -20.67032 | -42.00502 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b9f18650-781e-3ff2-988a-d96a87aa3dc7 | -20.66642 | -42.00384 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| af3383aa-96c2-3973-98c7-e12b3f257b6e | -20.66607 | -44.809 | 2024-10-03 03:38:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| afbcf516-4bf4-3284-ad47-c1aa7d67f7d4 | -20.6625 | -42.00277 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e4c1ac7d-58c0-32f0-bc9e-1620a6dc9750 | -20.65847 | -42.00229 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 692c34ff-0f14-3044-a3e1-f0f499e10cae | -20.65443 | -42.00187 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| d69821a9-970d-3598-9a4a-bcee2f049842 | -20.65296 | -44.03377 | 2024-10-03 03:38:00 | NOAA-20 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 92e5cc70-8d24-3a9a-9041-16daaa1470ea | -20.6521 | -44.03079 | 2024-10-03 03:38:00 | NOAA-20 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2c57f148-e2af-3267-baa9-056794ccc884 | -20.65165 | -41.9948 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| cef0a395-8fdd-3df1-bcdd-34f019f5386a | -20.65043 | -42.00125 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 57354573-26b4-3f10-a5e4-5e8b18c22a84 | -20.63188 | -41.9904 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 73ba4217-9ce5-3cd1-b468-48259ead02eb | -20.60576 | -42.07582 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1045b612-e75d-35b7-b823-58c1f0d557f6 | -20.6033 | -42.07528 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e9ee924e-e231-3f96-948f-c0c22c11c164 | -20.60177 | -42.07497 | 2024-10-03 03:38:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c17c58dd-97e4-3753-95aa-22c9f60f1e0d | -20.54938 | -43.36882 | 2024-10-03 03:38:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 18c6d44e-10b5-3de4-adf1-b098a92159ee | -20.54764 | -43.37781 | 2024-10-03 03:38:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e6cc51b1-63a4-3619-9d27-7617acdd2882 | -20.54595 | -43.36334 | 2024-10-03 03:38:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a44177e3-1c4f-3c0f-83e7-146017634838 | -20.54507 | -43.36789 | 2024-10-03 03:38:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f57351fa-1a7a-3d2c-bae3-47b84a980400 | -20.54074 | -43.36699 | 2024-10-03 03:38:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7c87cc10-0c35-3bea-badc-007603fe9375 | -20.53152 | -46.26084 | 2024-10-03 03:38:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d84619e-14a8-3002-935f-f5228e8a4c9a | -20.53118 | -46.2607 | 2024-10-03 03:38:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc0ffc63-7dd2-3887-9c99-7532ff90a494 | -20.53052 | -46.26388 | 2024-10-03 03:38:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fefba097-1dc0-35e3-8f26-78cda0a454a7 | -20.52633 | -46.25975 | 2024-10-03 03:38:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8dbf873-12ad-306a-b477-c30abf7d3c1f | -20.52561 | -46.26305 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb30daf5-5267-39e4-88d4-3ea8936cf0fb | -20.52528 | -46.26299 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cabe2c07-9383-3b7f-b577-ed1cc18572f7 | -20.51957 | -46.26584 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a388e1e-cfd8-3dde-82d6-db0760b51160 | -20.51927 | -46.26575 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efb6d7f2-39b5-3f60-b2aa-69e86dcc4bb2 | -20.51663 | -46.71281 | 2024-10-03 03:38:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdb4826f-2bf5-3b3d-b3e4-51eddcaaa70e | -20.51586 | -46.71638 | 2024-10-03 03:38:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc930117-9aec-3a8f-950d-c78047211de5 | -20.5151 | -46.71992 | 2024-10-03 03:38:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2b4bd42-6b2a-3018-8794-db7e8b7c03c6 | -20.5113 | -46.71162 | 2024-10-03 03:38:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9f8c6d5-2788-3d2d-9589-564852099808 | -20.50711 | -46.32292 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23d3af21-b809-3ed1-858d-bbd9089639e7 | -20.50649 | -46.32638 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f124090-de69-391f-a8ff-8d403adbb341 | -20.50636 | -46.32634 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4b95339-7fbe-3816-9267-5c28bffd4eda | -20.50578 | -46.32977 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f05e2262-7721-390b-ace3-e2c82f7a7110 | -20.50562 | -46.32973 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aec70880-efff-315f-9b0a-05a3f180acc6 | -20.49981 | -46.33221 | 2024-10-03 03:38:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee654ac2-985f-3ed8-bdd6-d36ffa2a06f0 | -20.48666 | -40.95061 | 2024-10-03 03:38:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59fbe3aa-2924-398b-9894-b69db3f93c34 | -20.48587 | -42.47046 | 2024-10-03 03:38:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 69ef7ece-74b3-366e-9a4c-8651fe61f3b9 | -20.48366 | -40.9471 | 2024-10-03 03:38:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a32a777d-af75-3efc-8f2e-3bbe0a161a4b | -20.48292 | -40.94982 | 2024-10-03 03:38:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f497bcce-fc4b-349c-9764-a1ef2fee49bd | -20.476 | -43.18453 | 2024-10-03 03:38:00 | NOAA-20 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 56b92e77-5d6a-32ca-9e4b-7a06f6ec9106 | -20.43738 | -41.99506 | 2024-10-03 03:38:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e2f2d938-9e95-3700-bfd7-9766339e05b8 | -20.43678 | -41.99821 | 2024-10-03 03:38:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f773e52b-e4d1-3ec1-99fa-ca16fbdb6652 | -20.37768 | -43.86668 | 2024-10-03 03:38:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5d94f503-927c-37b3-8329-4a56f37b80d8 | -20.37607 | -43.86551 | 2024-10-03 03:38:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 840db629-07ca-38d5-b31e-7809fadf9204 | -20.37341 | -43.25224 | 2024-10-03 03:38:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb6955d9-83ff-3783-b7dc-732d69b95a42 | -20.37153 | -43.25303 | 2024-10-03 03:38:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0317ccae-85bd-30c6-9225-5741aa513faa | -20.30398 | -44.04189 | 2024-10-03 03:38:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5dc9804e-902f-341e-808f-1077c156b5a7 | -20.29705 | -44.02921 | 2024-10-03 03:38:00 | NOAA-20 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0cfa0d5e-49ed-3f0d-b929-997b91d55086 | -20.28281 | -43.52404 | 2024-10-03 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 31b69964-f7af-3cea-9ecc-db2a08f62cef | -20.27851 | -43.52266 | 2024-10-03 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4ff1f9d3-96b5-3b87-b6eb-5de5bc7e257f | -20.27759 | -43.5274 | 2024-10-03 03:38:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| cec99ba6-ab45-3089-8a7f-bf1fa967eeb7 | -20.21244 | -42.46868 | 2024-10-03 03:38:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0733009f-0655-3d29-a231-3ddafd1c7d7f | -20.21168 | -42.47264 | 2024-10-03 03:38:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 7f9c4705-8a74-34cd-84e6-81c5a061dc3f | -20.21091 | -42.4766 | 2024-10-03 03:38:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 84734de1-d481-311b-b694-937c98255ce6 | -20.21012 | -42.48066 | 2024-10-03 03:38:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3246f53b-4620-3494-bf3c-060154338f77 | -20.2052 | -42.48397 | 2024-10-03 03:38:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 059a6bf3-9754-33d0-9003-fd7ae350297d | -20.20443 | -42.48796 | 2024-10-03 03:38:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 8b8b5a88-915b-3162-9fa8-20d10be9b994 | -20.20302 | -42.48463 | 2024-10-03 03:38:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 21cf8793-d831-38d8-af07-36683b676b72 | -20.16434 | -43.54881 | 2024-10-03 03:38:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 73bb6d89-7ea8-3990-b8d5-19c14d4b266f | -20.15415 | -41.86917 | 2024-10-03 03:38:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| b04221f2-1fbf-34f9-b039-8bb184f8489e | -20.15312 | -41.87466 | 2024-10-03 03:38:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| df73d003-0c88-3207-b6e0-8d0866e76d82 | -20.14829 | -43.8514 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a365f93f-b014-31d4-b95e-88149141c157 | -20.14738 | -43.85587 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 74868e97-18cb-39a3-97b7-41724d8e5036 | -20.14636 | -43.8536 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 04756821-cc22-3781-bb10-72fe9d77a78c | -20.14385 | -43.85024 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 79329b48-00b9-3a17-9936-82aeda06ddf9 | -20.14294 | -43.82332 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 60e2c45f-1552-3a62-8fd0-970da93724d7 | -20.14291 | -43.85484 | 2024-10-03 03:38:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 16acb62b-8903-3cca-aeb0-fd4c9fe250a8 | -20.14189 | -43.85255 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0c234b74-9809-3438-83ca-6257433f3579 | -20.14095 | -43.85739 | 2024-10-03 03:38:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9cc36f7b-07ca-3ea1-8e33-67d57e8282c9 | -20.13849 | -43.82222 | 2024-10-03 03:38:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README70.md)
