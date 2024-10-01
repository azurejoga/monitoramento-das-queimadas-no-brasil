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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca4b2861-afa8-329b-a5e6-16bc7a8e409f | -22.72147 | -46.68348 | 2024-10-01 04:17:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 42b71f26-1731-3324-a0c9-fc6bcd35dd6b | -22.71932 | -46.67543 | 2024-10-01 04:17:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 639bcbe6-cd4a-3996-a75b-8594f6364d51 | -22.71874 | -46.67916 | 2024-10-01 04:17:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| c3fe292d-3f1e-3e12-a42d-8201750e0d0c | -22.70925 | -46.23599 | 2024-10-01 04:17:00 | NOAA-20 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eb3679f9-e0a3-390d-b406-4c31dfeeba07 | -19.57489 | -46.56311 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11370951-af9d-389b-9b83-2e12d9035d57 | -19.30014 | -47.4343 | 2024-10-01 04:17:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf4edb53-e925-3312-8ea8-6eeae046e558 | -19.29678 | -47.43368 | 2024-10-01 04:17:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c8d9b3c-732b-3cdd-a285-6295daf17678 | -19.29342 | -47.43307 | 2024-10-01 04:17:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| feca2814-a933-3f5f-9259-b7370bc9e662 | -19.25127 | -47.40623 | 2024-10-01 04:17:00 | NOAA-20 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| db4a8ca5-7c09-3d0b-b0dc-65ef86c1b83b | -19.08148 | -46.65428 | 2024-10-01 04:17:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 303e8f15-666a-3a2e-8255-6d0be2a6cd45 | -18.99945 | -47.25667 | 2024-10-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b46adcc4-1963-3e06-ac13-8276196bb0ac | -18.99609 | -47.25607 | 2024-10-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 803080ea-491c-32c1-9056-f512443e1372 | -18.9506 | -46.93426 | 2024-10-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d71842ad-9926-3050-8178-f77615b8a15d | -18.92417 | -47.03265 | 2024-10-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f11fa521-0880-3011-bdd1-0f7efa506c07 | -18.92144 | -47.02832 | 2024-10-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4eafc80-5a1b-3125-875b-3336fb230321 | -18.92084 | -47.03203 | 2024-10-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17fc5a08-3040-3900-be7d-6c44d5dce34a | -18.83201 | -47.62952 | 2024-10-01 04:17:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcc7a5d5-256f-358e-ba48-87a04f0cd774 | -18.78275 | -46.62825 | 2024-10-01 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71eed957-5888-3463-9ad3-f3d612fb6e16 | -18.77766 | -46.93412 | 2024-10-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 916730a2-e2f5-303c-9ae1-14cb91f2d96d | -18.63967 | -46.31392 | 2024-10-01 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6a1844b-89a1-3f5a-8032-d7909ff7bbb5 | -18.63577 | -46.31699 | 2024-10-01 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcf66349-993c-3f29-99f3-9cf51940c2e2 | -20.88834 | -47.01785 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd49ce96-b0b9-3faa-a008-7af8e1ab505e | -20.87359 | -46.98484 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d57fb392-3b86-327d-99e0-ff933df353a6 | -20.87028 | -46.98425 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fce25e12-0af8-3f24-a3ff-a223cf32d624 | -20.86968 | -46.98796 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 276d3d6c-112b-37bc-b9cc-e689b38b2d61 | -20.51357 | -47.35691 | 2024-10-01 04:17:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8d5362e-3e4a-38ef-b3ef-b286878c24b9 | -20.22691 | -47.47179 | 2024-10-01 04:17:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b63b490a-96e4-3e16-bc03-fc17736e47ed | -20.09816 | -47.34057 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bccdbcce-45a7-3bc6-884b-4635a98b7913 | -20.09754 | -47.34432 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e877c11-6490-3fc7-abf8-423abc1de0ce | -20.09693 | -47.34808 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb1be231-08ad-37c1-9bd6-03b05b0e1d45 | -20.0942 | -47.34369 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2378e97-4af1-34cc-8e03-8417a88d1d06 | -20.09086 | -47.34307 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8cd4be3-d6b5-3434-8bbc-c8dc21e4e86c | -20.09024 | -47.34683 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a54440e1-94f7-3194-80ed-e0c4323984c5 | -19.76134 | -46.62904 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 846cf622-1e47-32ea-844f-45c0bc0c2acc | -19.76016 | -46.63639 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa394187-89f7-3b09-82c1-a3b533642616 | -19.75957 | -46.64006 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ef3db1e-7f3d-332a-b631-7d808b79edbb | -19.7584 | -46.6474 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e6b288a-6de4-3277-bf6e-571e51005b96 | -19.75803 | -46.62846 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49a34524-e65c-3cbc-bf13-334524f780c0 | -19.75663 | -46.65839 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f31ac95d-9f90-31c2-b935-6d0607f2d978 | -19.75605 | -46.66205 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfd97300-9579-35a3-9982-002999f962a6 | -19.75546 | -46.66572 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d61befdb-3e83-3838-869e-0551131bb7d9 | -19.69753 | -47.23409 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa7ee3c4-084f-3f7d-94f7-f71aa1706775 | -19.69725 | -47.21476 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd246c76-bf01-3394-82fa-ac6d3346e975 | -19.69396 | -46.71196 | 2024-10-01 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a337b85d-b2d2-3106-bdfc-f717f3c1a7a9 | -19.69358 | -47.23724 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a77081b-39c6-3b18-8e80-cfe60c04a16c | -19.68689 | -47.23601 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bc7eda1-c2b8-327d-b68b-09f838e9b85e | -19.68662 | -47.21663 | 2024-10-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 714f8a5b-f2c7-3957-ad26-52cdb415303d | -20.72434 | -46.89745 | 2024-10-01 04:17:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d53d286e-fb1d-3ff5-9a3e-ceb27f5b5316 | -20.72103 | -46.89684 | 2024-10-01 04:17:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 74ac840f-fa4a-3ea1-903b-90149d971f99 | -22.12108 | -48.56371 | 2024-10-01 04:17:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80832df1-07f7-3c10-9ac9-5ad73161eaa0 | -22.11901 | -48.55513 | 2024-10-01 04:17:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2ec98b5-b91c-3f9c-9a82-7026564d44ea | -22.11834 | -48.5591 | 2024-10-01 04:17:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86f4ddc5-a535-3a66-925e-2d27aac9afca | -21.86097 | -48.37777 | 2024-10-01 04:17:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e0dedda-b94e-3ef9-95a2-df76e84ccd2e | -21.84977 | -48.21191 | 2024-10-01 04:17:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb5c1a2b-1246-338e-b563-19c0e57b3906 | -21.84912 | -48.2158 | 2024-10-01 04:17:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f6b4b93-3f1b-3db9-b599-5f0ab0500bc1 | -21.62183 | -47.81384 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bd8e6a2-ca88-32f2-8e47-c0b2de9e771e | -21.62047 | -47.81071 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71cfa633-397f-3a1a-8159-e37d8a26fd13 | -21.61985 | -47.81453 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e545538-108f-3fe5-9e41-48faad33d6c6 | -21.6165 | -47.81388 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0d9da99-5113-31c6-b6ce-589cae79276d | -21.61315 | -47.81325 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8329d366-3e35-3a99-a860-c7bd8cd1ee93 | -21.61042 | -47.80879 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a643e1a-314a-3afd-9e93-6474e8cd71f0 | -21.6098 | -47.81259 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 601e4b92-037e-3aa7-9cc0-d2f5a596303a | -21.60521 | -47.81956 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6bff95fa-5dcc-3acb-a078-52bc90df9961 | -21.60349 | -47.78786 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3658f42b-554a-3f19-807e-a374a7275a11 | -21.60287 | -47.79168 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07c11862-1e24-3a53-bc99-f5aec9289d26 | -21.60271 | -47.83482 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f1e18b67-7ef1-3575-9285-efa6dbe44916 | -21.60225 | -47.79549 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 206d34c4-8f06-3f03-94d9-d69b08ae90cc | -21.60208 | -47.83863 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7ca49961-aed2-304f-93b5-05be3d70cf1f | -21.60186 | -47.81891 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5ef80fbe-7b11-32e8-8d6f-de7447360301 | -21.60146 | -47.84244 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 94243af1-2941-39fa-8a64-78adae0c6be7 | -21.60123 | -47.82273 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 079b1ba9-6a13-3455-a21a-b231b737f5c5 | -21.60084 | -47.84625 | 2024-10-01 04:17:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 641798db-909b-38f8-b270-d918568fb718 | -21.60061 | -47.82656 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 9167a393-a375-30f2-bba6-b18971038f0b | -21.60021 | -47.85006 | 2024-10-01 04:17:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a79ba2ab-103b-3fb0-a139-cceeba391050 | -21.59998 | -47.83037 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 6c7d4b40-6134-32fc-a599-d6a9803ca544 | -21.59952 | -47.79105 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fec727af-b13a-338d-a720-c61faa46b6e4 | -21.59936 | -47.83419 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 89d2ac69-34ed-33d6-94cc-c106bdc57231 | -21.59873 | -47.838 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7e18b008-1a47-3c51-9226-c15e7cb9d6f4 | -21.59811 | -47.8418 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5b9349f2-d110-3caa-bad2-7f989c9c17ac | -21.59748 | -47.84561 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 443b3012-30d7-316a-a40d-6c6e0e24e20c | -21.59686 | -47.84942 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f107ec05-79c5-3e3b-be72-b7e19019de33 | -21.59663 | -47.82972 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 9b2c2f24-0a0d-3e12-ba55-398b1f8609a2 | -21.59623 | -47.85323 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab42f7da-f374-3ae4-bcf7-60432c45e553 | -21.59601 | -47.83354 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 36da6cb1-4bfc-3ae5-a693-a27090d46555 | -21.59538 | -47.83736 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fc4cac3d-70bc-333d-a22d-03341bf054ed | -21.59498 | -47.86086 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b213084-7409-3712-812e-43714d5af82c | -21.59476 | -47.84116 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb328ffa-ac95-3318-ad4f-6bb0b665714e | -21.59413 | -47.84498 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7e61e6e-1a34-32cb-b8ee-17134aff08d7 | -21.5935 | -47.84879 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 22d1fff8-eb72-3332-ab95-1c3e7a325bb0 | -21.59328 | -47.82907 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 2ebe95a4-021e-3b07-be9b-c79e977f082d | -21.59288 | -47.8526 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3b36cc92-6315-3629-b952-19e5c67d4184 | -21.59266 | -47.83289 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cabd2f1d-dd7a-3b60-9516-8825a6cf6779 | -21.59225 | -47.85641 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 5e595f19-17a1-3cf9-8f1a-bb6d1c5a8221 | -21.59203 | -47.83671 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8c332979-580c-3b48-8078-ca4fe3602dae | -21.59163 | -47.86022 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b9942563-0f3f-39fe-a8f3-b6d5dc8d83e9 | -21.5914 | -47.84053 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 010ce79e-5758-31fc-8a47-61c3032837c3 | -21.591 | -47.86404 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9d1b2f4-dca5-3b07-8263-4aae16909bb3 | -21.59078 | -47.84434 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89cd942e-8ad6-3053-bdb3-41e93151fa56 | -21.59015 | -47.84815 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 33640665-af6d-3054-8c02-f32efc6a6ad5 | -21.58994 | -47.8284 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README93.md)
