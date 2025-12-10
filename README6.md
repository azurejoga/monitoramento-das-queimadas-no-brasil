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
| aa2b8396-9861-3348-8453-4115f4e1f008 | -6.48978 | -43.7114 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 936b6f8b-c589-3f80-bcb0-7f4233221871 | -5.9915 | -41.88448 | 2025-12-10 04:08:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d67c4fa-97ce-3cfa-9414-72df9c985e3d | -3.83508 | -43.31934 | 2025-12-10 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de68e28c-1112-3255-93fd-00c5e02810bc | -7.17631 | -35.99972 | 2025-12-10 04:08:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b30e5047-6e97-31fc-99b1-4ee61ff35fb6 | -6.94327 | -38.60717 | 2025-12-10 04:08:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b717174a-db28-3133-8dff-ed1b80b624e1 | -4.80962 | -41.82806 | 2025-12-10 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a9feb9a-66fa-313f-85f7-1b473dd36ab1 | -6.36082 | -39.49709 | 2025-12-10 04:08:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 29e7716e-b082-3b6f-a4af-5698b3afdc22 | -5.65019 | -37.42949 | 2025-12-10 04:08:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61c15436-6827-329b-9c70-714bc3543346 | -5.16112 | -44.09993 | 2025-12-10 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9736f32a-ae9c-336c-b2aa-ff3c13c26795 | -6.94687 | -38.60769 | 2025-12-10 04:08:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 11f1b023-18fd-3496-8ce9-d74b8e8f0747 | -5.35564 | -38.0599 | 2025-12-10 04:08:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b854f55b-6431-3eea-b56a-ca8e9ad6770a | -5.16973 | -43.11845 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| fe0b8e2d-a54a-3794-93af-12490aabcc13 | -6.00578 | -40.37554 | 2025-12-10 04:08:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e4de87a1-85ad-378f-b62c-1962f8e7a544 | -3.02873 | -51.13498 | 2025-12-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8554b208-ff99-3d6d-bfbb-a908d15b1e48 | -3.68168 | -43.82744 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c887323-0855-3af0-ada8-6e46e3dbfc6e | -4.74356 | -44.44014 | 2025-12-10 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35f16819-fd2b-34bc-b646-99931c2c21db | -4.50374 | -40.52504 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb130184-02ae-3fe5-ba6a-6cc58e0e0efb | -7.18006 | -36.0016 | 2025-12-10 04:08:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| aa1bead9-56ec-3d00-b606-fc4a7cdd325f | -9.03129 | -36.66346 | 2025-12-10 04:08:00 | NOAA-21 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 85c9197b-f5a2-32f1-a447-7fc2d019506e | -4.18543 | -41.94693 | 2025-12-10 04:08:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1a27e4b1-97bc-347f-ae3a-22617bb08d97 | -11.78039 | -40.92407 | 2025-12-10 04:08:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6e496796-3b33-333f-ad46-7e15e3d1ebd6 | -5.3437 | -43.43602 | 2025-12-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37d85e2f-7f4a-3a1d-b90b-03a6cf2ebe0d | -6.29507 | -41.9223 | 2025-12-10 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ed1ccb60-762e-3455-bdb3-135416af771a | -4.00327 | -43.23574 | 2025-12-10 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64c6b16b-f664-3f80-b249-c05d62d7c67a | -5.9338 | -38.12603 | 2025-12-10 04:08:00 | NOAA-21 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a9602d6b-2f97-35e0-a4c9-37ef7be11bb1 | -3.69517 | -43.80788 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb8f15f1-8da5-39cf-930d-79b8f41135a8 | -8.37047 | -39.65362 | 2025-12-10 04:08:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6de019e0-c967-3476-ba77-a6fbb9a1e8c8 | -5.75714 | -35.73957 | 2025-12-10 04:08:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 83749ec1-15aa-3e4a-a739-8b937cf7b672 | -7.2927 | -39.0047 | 2025-12-10 04:08:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f44c2366-fc88-30e5-bc9b-df6d8eee974b | -9.4315 | -40.3951 | 2025-12-10 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c58aa979-7334-3f4f-9e37-930c7a364ee4 | -11.78095 | -40.92034 | 2025-12-10 04:08:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 339b3fee-4be1-3ad5-9c10-0c550637724f | -5.15757 | -44.09938 | 2025-12-10 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fadde9b-d6fa-37ca-83fd-2086d7214754 | -6.32212 | -43.747 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4c63fe8-57fc-3cde-ae83-fa5f4925ea7f | -3.69426 | -43.817 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98ffbd94-232d-3da2-9a29-1839d6a478c5 | -3.8261 | -43.35333 | 2025-12-10 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a434933a-d308-3abc-85a9-383f4a049419 | -7.17584 | -36.00099 | 2025-12-10 04:08:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 54d5c81c-5f67-3247-8215-d8cfa64832d4 | -4.84008 | -42.98407 | 2025-12-10 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce34f269-c287-3cf8-bd2d-58a71e1dd33e | -6.23443 | -40.63462 | 2025-12-10 04:08:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2cdba5e-4079-30fd-85b0-aed7d22e42cd | -9.08878 | -40.87714 | 2025-12-10 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 43cd6781-29fd-3e01-9d9a-0a9c6fa2cd8f | -5.33965 | -43.43926 | 2025-12-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 86497cc9-e331-3499-85f3-c2048df01284 | -6.60363 | -39.53749 | 2025-12-10 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e167a98f-ec02-3323-8ec6-9d9644bf34a3 | -3.23286 | -47.46943 | 2025-12-10 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3aa2e317-e424-36a4-bd5e-c5ac5e61e13f | -6.60478 | -39.52998 | 2025-12-10 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 77d27551-94b5-324c-abd2-035a587ddcbf | -6.47742 | -43.54799 | 2025-12-10 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1f5f35d-42a7-3a79-9747-5f750dd6d5e9 | -7.55256 | -37.49495 | 2025-12-10 04:08:00 | NOAA-21 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 748081ed-cc01-3ee9-b354-bea2cdfbb477 | -5.85132 | -42.44884 | 2025-12-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 943db7b8-4554-364c-b34a-359a5bab832e | -7.1295 | -39.99997 | 2025-12-10 04:08:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0c8834b-0918-3b84-844f-af79d606796c | -6.63621 | -39.6451 | 2025-12-10 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44cd3fcc-9916-3caa-8f32-2afdcaf11728 | -5.32716 | -43.56157 | 2025-12-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a51426d-b05e-3a24-82d6-afb4f47b2435 | -7.89467 | -43.5612 | 2025-12-10 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 314964d3-02a0-3b92-ae9d-b55f5e8b5097 | -11.11182 | -40.28226 | 2025-12-10 04:08:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 78ac119d-d4d3-3796-acc0-e999449d3f3c | -4.50813 | -40.51862 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd67988a-600c-34c5-a77b-6c9fdfb7a05f | -6.90095 | -42.84058 | 2025-12-10 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a339edac-be80-3b1a-927c-46cdc6d2b109 | -5.74682 | -42.05528 | 2025-12-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1b1db899-16ff-359d-93df-faebbe420b78 | -6.54941 | -41.71128 | 2025-12-10 04:08:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c373d08-4912-35ea-818b-efd15b4c180b | -5.69916 | -42.37733 | 2025-12-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b99bedb-7800-383c-868f-76c564cd12a8 | -6.11847 | -42.6944 | 2025-12-10 04:08:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 76d4c7f8-39a0-3ce9-83e8-af3664a3c2a7 | -8.15784 | -43.17324 | 2025-12-10 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8e35bc5-878e-30b9-8ff1-2c292577b8e1 | -9.92745 | -37.09187 | 2025-12-10 04:08:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1cb1b222-aa54-377e-aeff-24047f453b0a | -6.00992 | -42.3261 | 2025-12-10 04:08:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3bb2fb9f-2389-37ab-955f-3649fbefd7b9 | -4.53981 | -42.64625 | 2025-12-10 04:08:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6c28cb6-773b-334e-ae2f-5c01e7d29a9a | -3.69236 | -43.82911 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98281895-4e40-335b-a983-13dd6eb9361f | -5.89037 | -42.39355 | 2025-12-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 430610b2-404b-3b19-bb07-3c85d90e77fc | -5.41761 | -37.92484 | 2025-12-10 04:08:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 23c4e444-1c01-3979-9b03-ad7844c888d3 | -7.12228 | -39.99508 | 2025-12-10 04:08:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54d7f22f-bd8b-3795-928e-d688ed91816b | -5.70398 | -42.58431 | 2025-12-10 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db442e31-38a4-36cc-bdbf-9d7ed5b6bf27 | -5.35499 | -38.0641 | 2025-12-10 04:08:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5a1316b0-aad1-34c6-8505-528a0cdae8ed | -5.70477 | -40.8271 | 2025-12-10 04:08:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2979ec8-ca4a-3d70-9ef0-50866065dce9 | -6.07393 | -41.92241 | 2025-12-10 04:08:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d6f8d6cf-222b-3437-9fd5-b172d81996cf | -6.60191 | -39.52572 | 2025-12-10 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5826340a-ce1e-3b6f-8c0c-a45080f7b418 | -4.29374 | -40.38891 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab389cfc-8da9-3bf2-907c-6f5eef250a20 | -3.6907 | -43.81645 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c5ac6b0-13df-370b-bd0e-aa87a4feb44e | -3.68714 | -43.81591 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6937f448-01c2-3dd4-a65d-50a867115bfc | -6.00243 | -40.37502 | 2025-12-10 04:08:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 70926c3f-8571-3ae7-afff-2fb883e88ee7 | -4.91421 | -43.46586 | 2025-12-10 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8bdb3205-d635-322a-a92a-c9a29354eda9 | -5.04292 | -40.22653 | 2025-12-10 04:08:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1e8409ea-d9e4-384c-ad24-f8262d813dc9 | -6.86857 | -39.12947 | 2025-12-10 04:08:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 15bcc671-ca08-3343-8a8d-561a0d5ffb35 | -4.93125 | -38.75227 | 2025-12-10 04:08:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a71a567-6418-3227-b31f-44f43233dbe6 | -3.69452 | -43.8119 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcdd0bbc-d939-326e-b954-3214c0c26cee | -5.24258 | -42.63937 | 2025-12-10 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42f19b78-9d02-364d-ad90-f32463c6f9a1 | -5.16914 | -43.12214 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c48ec73-9309-3537-9596-95f71fc663d9 | -6.76141 | -44.20792 | 2025-12-10 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b1b0b06-1a1f-3215-8090-4b38a3d494b1 | -6.07728 | -41.77022 | 2025-12-10 04:08:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7543578e-6995-394b-9fdc-724cbb7590da | -5.53022 | -41.65856 | 2025-12-10 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d730e567-93c6-392a-9283-e92216c513f0 | -6.90635 | -38.09978 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88a75f8d-1fd0-35be-b1af-2c94a229631c | -6.68986 | -43.68956 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c0566db-d9e5-3434-9ed7-187bb78ee410 | -5.0028 | -41.29278 | 2025-12-10 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30d877c2-e2ec-3b21-a810-7d00d69622ce | -4.17246 | -40.70697 | 2025-12-10 04:08:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| dbdba03b-9b8b-3527-a789-2412590a6f36 | -4.4921 | -40.51258 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0e5006ee-ff85-30c3-96bc-804059fa0b42 | -3.68231 | -43.82341 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60fca057-2370-3dd1-ab08-791d91222395 | -5.53298 | -41.66253 | 2025-12-10 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| da4058a7-67f1-3904-af5f-e35bbaf983bf | -6.65012 | -35.10715 | 2025-12-10 04:08:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0c9709ef-6cff-37fe-8162-a7b93a36d432 | -6.11512 | -42.69388 | 2025-12-10 04:08:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 297fe567-f734-3a87-b6fa-b2b948ff6dae | -6.69047 | -43.68579 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78c0fc31-b4ba-32c2-a573-e2dcc8c05a79 | -5.00506 | -42.93842 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c82ca274-d6ba-3967-8811-6fa8f4fc1bf9 | -5.36338 | -38.06371 | 2025-12-10 04:08:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bd7eec6f-6f46-34e1-8d65-3921a42b83b8 | -4.11125 | -46.48367 | 2025-12-10 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fc57b42-180f-396e-b534-f856bffe461b | -6.47573 | -39.73126 | 2025-12-10 04:08:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 826bebd8-1cea-38f9-badf-c52ff22d1678 | -4.50759 | -40.52208 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 33c27989-ead9-3a3f-b4ca-d2c4b0d220a3 | -5.41179 | -40.72067 | 2025-12-10 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
