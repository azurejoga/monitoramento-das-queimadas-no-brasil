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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a64472dc-47c2-3b1d-a253-143ec5b107fb | -12.3735 | -45.92278 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9b02ecc-2cf7-3d2e-951e-3ca9f7a9ac45 | -15.99144 | -43.27411 | 2025-06-03 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c39f62f7-c8f8-32f3-a52d-dde06bc52604 | -10.36045 | -48.73267 | 2025-06-03 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59a95b53-acb1-357f-a1f8-8afd28537350 | -8.90801 | -50.0475 | 2025-06-03 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 089911fe-b67c-322f-935b-e5b109f67f76 | -13.4156 | -43.75324 | 2025-06-03 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d217ee45-925a-3a20-9c33-d1afd20ed7e8 | -8.91008 | -48.90176 | 2025-06-03 03:57:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2054cc1e-bf14-37a2-9d37-a445fbc488e0 | -10.23712 | -52.21947 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c524c1e-01af-3fe3-89d7-5225850df290 | -16.30499 | -42.75026 | 2025-06-03 03:57:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c696e13-3a7c-3b99-98ce-aa4a5ac17cdb | -9.39971 | -48.42155 | 2025-06-03 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5016354f-87fc-3b72-859d-ac1de72bdb1e | -11.67798 | -43.78513 | 2025-06-03 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 09a67bfd-f0e3-3e14-9065-ae5512cb5235 | -9.40033 | -48.41819 | 2025-06-03 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e3f0f5a-f558-34a4-87e6-c7cbb102ab3f | -13.3622 | -54.26777 | 2025-06-03 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d57055a0-506c-3374-a3cf-1fa76cb65cbd | -15.69969 | -43.4199 | 2025-06-03 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe224308-d282-3bb4-8a26-8a4949f80c85 | -8.90937 | -48.90561 | 2025-06-03 03:57:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a0f3339-c764-35d1-aa7c-2ed791be5e77 | -9.1971 | -49.69476 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e67bb627-fac3-312f-9a36-60cecba52876 | -11.79241 | -47.38261 | 2025-06-03 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbe72ee8-13f7-3e23-b55b-9bc686bc422e | -13.42069 | -43.75275 | 2025-06-03 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6a12531-a5e5-3408-9f53-66a73e83c5e7 | -12.37857 | -45.9267 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cf6d9c0-eca9-3473-b5b4-cb75efcde249 | -10.13736 | -52.13652 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dd11eea-aebf-31d4-972e-5cc3401cd19f | -14.6436 | -45.40042 | 2025-06-03 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 563336e9-afb2-3e26-8cb6-7726368877b0 | -13.42009 | -43.74937 | 2025-06-03 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fe8361a-a874-37cb-a7c7-d7f0daef6ad3 | -11.90679 | -47.44765 | 2025-06-03 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92c106d2-ea61-3534-8fd1-0875437a919e | -12.33609 | -46.3041 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3182bf56-2ddc-3a02-91dc-48334b10c7fb | -16.02922 | -43.68211 | 2025-06-03 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bd2e6d6-c30e-37c6-a847-0dfe86a9e83d | -12.37427 | -45.92582 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9af64406-ba3a-3b19-9c2f-0cd769799a70 | -15.69898 | -43.42406 | 2025-06-03 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8b58830-9bd2-3eae-976e-749d669f36ca | -12.36759 | -54.17547 | 2025-06-03 03:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd51a46b-b3db-3481-b7f8-961c5774b8ec | -9.39619 | -48.41052 | 2025-06-03 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e2cc878-7f2c-3b70-bf0a-584a83936446 | -11.57779 | -47.44458 | 2025-06-03 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a6717d90-7715-3bac-9f5e-d95eda643933 | -13.41856 | -43.75844 | 2025-06-03 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 765a5257-fe38-3033-ad5c-24b8b7dfc195 | -9.0709 | -47.15594 | 2025-06-03 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c66daafc-61c1-369e-9d5e-fdf1219055a0 | -13.41989 | -43.75728 | 2025-06-03 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4e5fd82-065a-3407-a9c6-1d3ce413e4e8 | -11.57372 | -47.45372 | 2025-06-03 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31ca2411-58df-3874-8902-6442c8a67327 | -8.90888 | -50.04299 | 2025-06-03 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cacc68a8-f067-3c78-8b6f-f4cb03d9900b | -8.91567 | -48.90279 | 2025-06-03 03:57:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5554476c-70b3-3277-942d-c1b60fbe02b7 | -13.00957 | -43.80005 | 2025-06-03 03:57:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d91bf0f3-63e2-38a9-b4f8-ec0b3bee4232 | -10.45654 | -47.94559 | 2025-06-03 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6aff5b2-dd71-3098-979c-663a712d334a | -14.64418 | -45.40025 | 2025-06-03 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a604a8a3-2f8a-35a2-affb-c037d3e266b2 | -9.71979 | -48.31598 | 2025-06-03 03:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fa92ad9-5629-3580-aa69-ec6b23083df8 | -9.60411 | -49.02623 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98f08a7e-aec9-3f43-944e-7510e3c0820e | -15.69542 | -43.42341 | 2025-06-03 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7771bac5-cee4-3e61-b7b9-af9123225d1c | -10.45709 | -47.94259 | 2025-06-03 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4a730df-722a-361f-858e-c876f823da86 | -10.4622 | -47.94353 | 2025-06-03 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 854b0c91-175e-3805-ac1e-0324c9f5e4ac | -10.24263 | -52.22667 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 949810af-9267-3054-a23b-71c607e75a7d | -8.91323 | -48.90096 | 2025-06-03 03:57:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1567524f-8c78-3fe5-9f6a-7507aedddd41 | -8.90291 | -50.0417 | 2025-06-03 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aae02438-85d1-3d2b-a619-a0ecd8053e38 | -12.37706 | -45.92786 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87052fd1-4503-3c79-96d7-2d4c6f752ade | -14.8681 | -45.12362 | 2025-06-03 03:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5f1aad5-8beb-3ef0-b31e-dc9bea444bcb | -9.37883 | -48.41424 | 2025-06-03 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8781632-dcce-35b4-9923-7ccb04187a3f | -8.90203 | -50.04623 | 2025-06-03 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cbeb42dd-a9ff-300d-9bdf-6013a3e7bf73 | -9.164 | -45.32415 | 2025-06-03 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9b4ab793-4945-375c-a055-49b1837f6f2e | -8.90674 | -50.04807 | 2025-06-03 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 199c55ab-ce0e-380c-ad4a-bf25362556ef | -9.1936 | -49.692 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efcd441e-9d20-3b6c-a04e-ad718960ed3f | -11.6818 | -43.78581 | 2025-06-03 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 234a9872-a700-3c06-b893-7bb7a6c7ff0d | -10.35676 | -48.73199 | 2025-06-03 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1594e54d-6b88-37f9-b224-2c7517263246 | -13.41933 | -43.75391 | 2025-06-03 03:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c794eb8-1d82-3d99-a36e-468702989d20 | -9.1928 | -49.69627 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 63516d48-4d9c-3c69-a34e-b6f08e860a5e | -12.3778 | -45.92366 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f573c5a-d500-3b44-a2b5-da397191a9bc | -8.90759 | -50.04353 | 2025-06-03 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a026df61-c9d0-3379-86a2-b6c1ce0aa801 | -12.37504 | -45.92164 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2176dc6-44f9-36fc-96c0-f61c6107042a | -12.29862 | -43.5459 | 2025-06-03 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0bf72f57-f71b-3d84-812e-b55067b6e30a | -8.97084 | -47.97274 | 2025-06-03 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1d1aa50-2cd6-30de-9973-0b8d735d5869 | -15.98848 | -43.27511 | 2025-06-03 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d135df1-5e96-399f-bab8-93684b50f272 | -15.98792 | -43.27349 | 2025-06-03 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| beaa1a89-f900-3f89-b018-0a9ba379082e | -13.00583 | -43.79937 | 2025-06-03 03:57:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf99fad0-50e5-369b-97fc-a09bfae85ebb | -11.67717 | -43.7899 | 2025-06-03 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd8d8c58-ce9b-33ac-bbb2-ae707bbaea43 | -16.02997 | -43.67785 | 2025-06-03 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 68895085-3895-34e7-baf6-9ac5da358e5d | -12.36701 | -54.17394 | 2025-06-03 03:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09143d0e-227a-35c5-81f5-dbc65f4d0f94 | -10.23595 | -52.22527 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec9d4632-94eb-3780-ae7f-cf166fd8d538 | -12.29489 | -43.54522 | 2025-06-03 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7e80b2c-84d0-3428-8b51-38bbae310a26 | -11.67598 | -43.78694 | 2025-06-03 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| af21c809-2b9f-39f9-85fa-3e8a93859208 | -11.90779 | -47.44232 | 2025-06-03 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a9001d5-b06a-394d-b6e5-c8768b2d18b0 | -9.61036 | -49.02359 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 105a93cf-f502-393b-ab76-be180beeba13 | -9.19627 | -49.69904 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a7665dd-ea31-39f1-b22d-bc51e3d606e0 | -12.37934 | -45.92251 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1d05b27-48a9-3285-8614-450dcf255ee1 | -11.57468 | -47.44838 | 2025-06-03 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0d25243-d4de-35f6-9bdc-4cc0d78e24d0 | -8.56492 | -48.8683 | 2025-06-03 03:57:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62d1505e-cb34-3966-b6a6-6f7dcb05abec | -16.30367 | -42.75801 | 2025-06-03 03:57:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daaac9ba-4dd6-3e1e-bf5c-2d0fe811766a | -10.45142 | -47.94465 | 2025-06-03 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bf0e65f-8cdb-39b1-a7d4-3772aa0490d8 | -11.90298 | -47.44136 | 2025-06-03 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9378da11-fa68-38ed-b757-4f546a2466a3 | -11.6798 | -43.78762 | 2025-06-03 03:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5d5e07be-2340-3411-a447-b4d345d9046d | -8.91251 | -48.90474 | 2025-06-03 03:57:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfa4f32d-ced1-3bd3-b824-a44a6a8a19a4 | -9.40156 | -48.41153 | 2025-06-03 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4592d55-20ef-35ef-b148-5a20440dab66 | -9.19865 | -49.69743 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bbd082e-4a62-3114-8e28-9f6c8502b841 | -14.6482 | -45.40099 | 2025-06-03 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45704d7e-81d0-39bb-9dc8-d780a72d5565 | -13.08695 | -45.27138 | 2025-06-03 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab7ccc7b-cdac-3ab4-8d85-7ab2ea665cdd | -10.45198 | -47.94164 | 2025-06-03 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05a536be-abb0-31f5-b611-7f043a0c8cca | -12.37854 | -45.91949 | 2025-06-03 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22b4079f-c15a-38f2-969e-64a3b0d78e10 | -8.9656 | -47.97171 | 2025-06-03 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfcfb78d-728d-3234-ae70-cfa9c4c26af7 | -9.40508 | -48.42256 | 2025-06-03 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce23f24b-b6a2-3b8a-96a4-8055193c7669 | -9.60482 | -49.02242 | 2025-06-03 03:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0cb3c2b-4b09-39c3-a5e9-8d6101735aef | -10.23503 | -52.21936 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e410f36d-cfb4-3618-bc06-5d6edfc58221 | -11.79519 | -47.38567 | 2025-06-03 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| edfee5d6-0367-357d-8d57-ef59793dbbd2 | -10.05158 | -49.66121 | 2025-06-03 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b2eeaea-8940-3e7b-b6ba-150744bae379 | -11.79722 | -47.3835 | 2025-06-03 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dc236ac-6e88-3606-b86d-124a49346103 | -13.42994 | -47.57938 | 2025-06-03 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ac1e832-2248-34c8-b97f-9c0b62358176 | -9.16838 | -45.32492 | 2025-06-03 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c41bc7d1-4389-35cd-a5e5-12a05d13cdb7 | -11.24678 | -49.49928 | 2025-06-03 03:57:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aeadd795-27bd-375f-8199-ac446ef02d79 | -11.54426 | -47.314 | 2025-06-03 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd25a500-ea0c-35d7-981a-6a27e31c2c2e | -11.2475 | -49.49551 | 2025-06-03 03:57:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README7.md)
