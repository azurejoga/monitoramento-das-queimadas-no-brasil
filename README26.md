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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f106a22-6ffa-3003-9879-bb9f634d8af4 | -4.98328 | -42.28165 | 2024-10-29 03:47:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f96eaf4-645d-33ef-a1df-9bb8b5cd7d39 | -4.98302 | -42.2862 | 2024-10-29 03:47:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33577c69-c3c7-3ed1-a3b9-f0b0a7cece65 | -4.86381 | -42.63554 | 2024-10-29 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 648a0529-d083-3139-a0f6-f0dcf7841812 | -4.85501 | -42.47585 | 2024-10-29 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 159cabb6-0926-3cba-92b0-ece8a760286e | -4.85432 | -42.47992 | 2024-10-29 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bce3d75d-5075-3d57-ac70-27746b56e126 | -4.50666 | -43.13668 | 2024-10-29 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ba042fe8-f577-33f3-a53c-df9d011a78f9 | -4.50213 | -43.13588 | 2024-10-29 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 36279b2a-7e88-354e-99bf-239dafc2e2ba | -4.38209 | -43.03793 | 2024-10-29 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a889238f-9f3b-3c71-8c41-f0a17c23f457 | -4.38134 | -43.04243 | 2024-10-29 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 243e4c16-f504-31f5-b95b-e8b3b8a29698 | -3.9464 | -41.49977 | 2024-10-29 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30a6543c-04b7-3e0e-8669-c88331c8aedf | -3.94579 | -41.50343 | 2024-10-29 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecc6be14-ff9f-35c1-acfc-657083325c85 | -3.86657 | -41.79449 | 2024-10-29 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8dd53031-2fe0-3206-9363-d5c396c47904 | -3.86178 | -41.79764 | 2024-10-29 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 922f5202-53b4-3e97-8df2-b91ed35e5fde | -3.86115 | -41.80157 | 2024-10-29 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3818d717-944a-320a-b2f4-e8691d348f84 | -6.13322 | -42.5144 | 2024-10-29 03:47:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 0333a5b5-615f-38d4-b2d2-891952fb5a6e | -6.13256 | -42.51843 | 2024-10-29 03:47:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 00a7edec-55d2-35a8-ac08-ae6d9b6c9b4d | -6.13236 | -42.51728 | 2024-10-29 03:47:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 64cd12b5-cefb-3c16-9848-f5d35ef07411 | -6.01751 | -42.58532 | 2024-10-29 03:47:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7378a570-f571-31ed-aca6-f5117c0e3572 | -6.0167 | -42.58461 | 2024-10-29 03:47:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aefef515-3e98-3658-bf68-829c7e620701 | -6.01325 | -42.58458 | 2024-10-29 03:47:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d50023bc-c281-3c39-8cd9-60d5688c8949 | -6.01244 | -42.58388 | 2024-10-29 03:47:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 98ed3a73-23b8-32b0-bab0-769784165378 | -5.87492 | -42.29583 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a15b5394-d7b7-3561-a075-f68bd9940a21 | -5.82223 | -42.84381 | 2024-10-29 03:47:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8968113e-4f98-3da0-aba0-16218b57c351 | -5.6215 | -42.48546 | 2024-10-29 03:47:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| afa8c9cd-8048-3539-ae19-6455889f9f65 | -5.62082 | -42.48947 | 2024-10-29 03:47:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9d56158f-a1f1-387d-8f7f-5ecacd252263 | -5.55015 | -43.2302 | 2024-10-29 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b2f006ae-34fc-3192-8079-2a4d698d9962 | -5.53524 | -42.99313 | 2024-10-29 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0b7c1cf5-29f1-37e4-85d6-83c517bc83d5 | -5.52072 | -43.32312 | 2024-10-29 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aabba3f5-6a00-36b5-ba00-61920452bf07 | -5.51696 | -43.31787 | 2024-10-29 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c3b46f9-6fec-3af0-9247-14843245f4c8 | -7.30163 | -43.0709 | 2024-10-29 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4deba64b-6bc6-342f-adff-3288d539cef6 | -7.30093 | -43.07504 | 2024-10-29 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3c6f5ddf-677b-3c2f-8e9f-38551d976e6d | -7.27297 | -42.5734 | 2024-10-29 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea2c9579-3239-3e54-b177-fddec9735394 | -7.01619 | -42.62979 | 2024-10-29 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 425839f6-cb9f-379e-8c54-8af71520f71d | -7.01552 | -42.63367 | 2024-10-29 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5c44e788-d18a-3bb9-bf06-48c4baaaa016 | -6.93778 | -42.78685 | 2024-10-29 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe54ce4a-e05e-35b2-9366-3085cf811986 | -6.90051 | -42.23243 | 2024-10-29 03:47:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1745f664-061f-3aff-a9ff-7fbf30ec909f | -6.83346 | -43.27441 | 2024-10-29 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| afbd8608-adce-3e49-b12e-cb0e4454cb17 | -6.82906 | -43.27364 | 2024-10-29 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e5c9aeb4-f0df-3db6-99e4-994b4ee96604 | -6.67351 | -43.04422 | 2024-10-29 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 91ab9de5-fc3f-39ae-b3f1-d95e277e0198 | -6.63585 | -42.80499 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8b4cbb65-a2ab-375d-967f-d8d8c9d7fd38 | -6.63521 | -42.80011 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ff456a7a-bed1-313b-a874-7d61635400f0 | -6.63452 | -42.80411 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5c831263-eb2e-3e6d-b685-3690160e908a | -6.63451 | -42.81314 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1579a9c4-17d6-340c-a68c-254e7e915e30 | -6.63311 | -42.81223 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 79c1a9b0-8b8d-3a98-9d14-728941b76a8d | -6.6324 | -42.81638 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ef7335e-6485-3d0b-be1c-93f74215bc9f | -6.63223 | -42.80028 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8bfa5d2f-b8fb-3ff6-8c66-2299b855b6a7 | -6.63094 | -42.79938 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a653bb6c-011c-36e7-85ee-fe3939a6621e | -6.62953 | -42.81665 | 2024-10-29 03:47:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3537587a-6ab7-3a4d-a843-d9da2150fd08 | -7.34179 | -43.5786 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b1bfe6be-7ea7-343d-821a-c5020ad42ddc | -7.34101 | -43.58325 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 373b6b09-21cf-32ba-a971-5ee71565ec08 | -7.33735 | -43.57776 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fb388d1e-b965-3be6-a166-b9ce0611a41a | -7.32242 | -43.58455 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0ca4a3a8-b55f-3b4c-a957-fdadeb370da0 | -7.32165 | -43.58911 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| be567f92-28ab-3b32-b6ed-d468021d5f6f | -7.2982 | -43.64525 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 655726fe-64f1-3206-aed7-a3b7429eacf9 | -7.29743 | -43.64972 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4f18eb7d-1814-3ebd-8000-6bce67f2d5b2 | -7.29371 | -43.64455 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ccdbd0a8-d5ad-358f-b704-033d50db9d4d | -7.29217 | -43.6535 | 2024-10-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 69b6ef9f-cd2a-3d19-a562-08d9a2767b04 | -9.95716 | -43.95061 | 2024-10-29 03:47:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 668a5c93-d19c-3b25-bc3e-83c4948819e1 | -10.13865 | -44.02461 | 2024-10-29 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a3fca31-d350-3fde-a994-acd66ec05d76 | -10.53628 | -44.1798 | 2024-10-29 03:47:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32c51140-f044-3723-9cf2-97e6282c8855 | -10.49827 | -44.16511 | 2024-10-29 03:47:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0b80c7a-0e43-39cd-8695-1aa51219a5f6 | -10.49386 | -44.16439 | 2024-10-29 03:47:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b28d3b08-6e23-31a5-8e3a-f1839f6c9e6e | -10.4015 | -44.17648 | 2024-10-29 03:47:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0756f311-5735-3305-9cd4-b71b5bd10c7d | -10.40123 | -44.17453 | 2024-10-29 03:47:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdd53b91-f90b-375d-986d-38d53844ff32 | -10.35494 | -44.05531 | 2024-10-29 03:47:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18e38125-c2f4-3067-a18a-d9384fa1d308 | -10.35058 | -44.05449 | 2024-10-29 03:47:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d3c3b94-61fa-36ad-8860-5bd5450078f0 | -10.27508 | -44.2789 | 2024-10-29 03:47:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a87c717-94f7-3d81-a86d-f045171164c2 | -10.27335 | -44.28054 | 2024-10-29 03:47:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a49cad84-bdb0-3f0f-9533-3e45f4d657ae | -11.84724 | -44.4672 | 2024-10-29 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59e3f276-d106-310c-a445-933f7fa65f32 | -10.86681 | -44.40757 | 2024-10-29 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a33286f-ab9d-3543-a1cf-cdbac8b54558 | -10.86602 | -44.412 | 2024-10-29 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f6d60d3-c532-3fbb-a527-1f693dcd8499 | -12.15676 | -43.49736 | 2024-10-29 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfdd36f7-8f43-322f-a17a-c77e54fecfca | -12.15589 | -43.49715 | 2024-10-29 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc62f352-db1b-3e89-b685-a8e227e1db03 | -12.05666 | -43.47289 | 2024-10-29 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94a92f5b-9f65-3dcb-b23d-3501ffe40b16 | -12.05601 | -43.47666 | 2024-10-29 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ec6811a-f3ff-3a5f-935c-c63a6f2d6f46 | -12.05519 | -43.47492 | 2024-10-29 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 117d9a24-8154-3b44-ad21-3c48ae654171 | -11.92092 | -43.85588 | 2024-10-29 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45e50e9c-828c-3164-bf8c-a397ac37bc63 | -11.90703 | -43.81253 | 2024-10-29 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21cad2d8-2b5a-367d-ad38-456804d33636 | -11.90632 | -43.81647 | 2024-10-29 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c2c4bed-aed4-3f2c-994d-5f05b1b7cb4d | -11.90213 | -43.81569 | 2024-10-29 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fbd85e7-671d-3304-8066-9425024cb8d2 | -11.54115 | -43.98289 | 2024-10-29 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 090293c3-dbbc-3cda-91a3-3696d61fc1be | -11.54041 | -43.98697 | 2024-10-29 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56742110-762f-306d-8b37-13cc4b3a6dd8 | -11.53689 | -43.9821 | 2024-10-29 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b03c6d09-27e0-333c-ba2e-6ddb2cb59eb5 | -11.10495 | -43.33671 | 2024-10-29 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| dc05b84e-26fe-36ec-8a3c-d7caafc34253 | -11.10428 | -43.34045 | 2024-10-29 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| e9062f59-1f2a-34ef-a011-8000c2965588 | -11.10242 | -43.33639 | 2024-10-29 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e413b54f-18c7-38db-a210-6cbe608fa518 | -11.10178 | -43.34013 | 2024-10-29 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ae98320b-8b17-3d67-8717-39fda31baa55 | -11.10017 | -43.33971 | 2024-10-29 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b83acf7-2b49-380c-acca-48031dc4cddb | -13.39918 | -44.41882 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0c2188b-df93-3f8d-8195-da52bcc63965 | -13.39491 | -44.41813 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a27e387f-e71b-3407-9899-87ab4d8b6095 | -13.29171 | -44.43622 | 2024-10-29 03:47:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f5c1cdf-f772-33bb-a5a6-733bac9cebef | -13.28979 | -44.43923 | 2024-10-29 03:47:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6c08c42-0fc8-3d85-bccc-1395854132e2 | -12.88846 | -44.61902 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f6943b8-23f0-3878-a51e-8c35c2a9b07a | -12.88412 | -44.61814 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33916571-5cd6-3562-88f8-16e79d7cd90f | -12.88259 | -44.62658 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b52479df-d831-3b8c-808e-05432620303f | -12.87825 | -44.62571 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 93da65c7-456f-324d-b63b-9cb8222e130d | -12.87748 | -44.62997 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99e2e4fc-06ab-366a-9e24-65bbc76083a7 | -12.87234 | -44.63351 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea38a6de-e555-301f-9a79-f4c06a13e5fc | -12.86799 | -44.63269 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 475b7fe8-2d18-3bc4-bafe-f777ee56817a | -12.86246 | -44.61375 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
