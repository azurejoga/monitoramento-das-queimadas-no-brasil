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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4b6e5a7-a955-3175-b251-c48659d65b79 | 3.14172 | -60.71281 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 345ee0a4-8092-31f8-a0ad-6e11bcc463cf | 4.11273 | -59.97416 | 2026-02-05 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17632c67-a861-31f6-af25-195c8422a822 | 4.34333 | -60.94282 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6ef4029-1094-3242-965f-581d2e63605d | 4.44498 | -60.38033 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c772966d-c041-3c32-ad9b-149018af1563 | 4.35146 | -60.93436 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f69d4599-4c67-3f33-af05-684bed64909f | 4.30308 | -60.36396 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83f0bae0-cf8a-35fa-8003-fc27dc42de2d | 3.30976 | -60.89624 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15c1b5b0-882a-33a6-89b9-6886a149c120 | 4.34666 | -60.94227 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07888016-4ddc-3e09-9d95-b9e7677ba4a1 | 4.33444 | -60.95152 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97a89cf6-ca78-3cf4-bc6f-2768fab345e8 | 2.93108 | -60.75611 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dcbc1f1-7830-3e1b-82f8-ff88f5e35558 | 3.74907 | -60.40509 | 2026-02-05 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f83f725-98e8-3005-81d9-e28514907a7e | 2.92391 | -60.75367 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa92b392-ffb4-3d2e-b6d5-075cf40915a9 | 3.42891 | -60.72435 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40e57563-6688-3104-a4d6-989daea85157 | 4.23166 | -59.82521 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 424650f7-5df3-31f6-85f8-6d6461adfcc8 | 4.2322 | -59.82865 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dd78db9-49bc-3e74-aff6-16bdb51af79d | 3.14504 | -60.7123 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69e31986-4939-3455-b469-26ec9bef6420 | 1.93019 | -61.19691 | 2026-02-05 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7eac26d-de9e-347a-85e4-11781fcfe92a | 3.74506 | -60.63976 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f5e335a-250a-36db-ace0-85714a67dccc | 3.82169 | -60.7377 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aca8f43d-c284-3d72-957a-d1f22a0523e4 | 3.91107 | -60.18175 | 2026-02-05 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5be5dfd-a743-3e37-87ec-f738d9f9c721 | 3.74284 | -60.6472 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aa5f07f-6215-3cf9-904f-ae677bb24ec3 | 4.07628 | -60.30453 | 2026-02-05 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02e8715b-ed1f-36f7-9ee8-896e419ada07 | 3.75823 | -60.70165 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0862b12-e00c-3aeb-8eec-673545faf268 | 3.42778 | -60.73873 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9ed8e906-5fc2-382a-8df5-49f3ddc0abc2 | 4.33722 | -60.94746 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b21479d-1d02-319c-a771-4bfa530958cf | 4.40252 | -60.62902 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d55329c-6eb8-3df9-b589-6acc644467c6 | 3.42724 | -60.73526 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee682abd-d452-31d4-bd63-617eb9d4fee0 | 3.91161 | -60.18519 | 2026-02-05 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a5c6186-5cc1-3dfc-8c5d-9ef842973e55 | 4.2355 | -59.82812 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22985bbe-cbc9-3ec3-9a3b-c0ff428dc82e | 4.33389 | -60.948 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c633323c-41dc-3d54-937b-aee4bb26fe07 | 4.73334 | -60.78808 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45f198f8-ee50-399f-b962-59b711337501 | 4.34055 | -60.9469 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f90992de-8c34-36d7-bffa-9110407a2619 | 4.07574 | -60.30107 | 2026-02-05 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f944668c-4f60-3678-9b3e-47a2baf47381 | 4.34388 | -60.94632 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 018a6dff-ceb2-3b02-8d3f-523e1fc6d4e2 | 4.38709 | -60.59583 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2463d799-7d28-3681-bea6-2bd451edbebf | 3.74455 | -60.61501 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa8da268-f54f-3804-a8c6-3b59eb6afae8 | 3.29326 | -60.57589 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0123a472-032e-3a62-9a80-db2dff57f409 | 4.39865 | -60.62608 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2d2be4c-9392-363b-a6f7-a31b2fedc11e | 4.40307 | -60.6325 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40925e96-30ee-3727-82c0-b86968584d29 | 3.87594 | -60.715 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4407ee15-17fb-30d2-a24f-637455341b89 | 3.30698 | -60.90025 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b83e9f4-51d3-3b86-b233-be9475cfd97a | -9.11803 | -62.55212 | 2026-02-05 05:31:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ca1be822-7c5b-3900-b7b1-936fd49312b9 | -9.11858 | -62.54863 | 2026-02-05 05:31:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c065b0f-504e-3a4f-b420-4e0fd1789ed1 | -9.03131 | -63.65456 | 2026-02-05 05:31:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eced84a6-a240-350d-b942-c1337bd4c35d | -16.22363 | -59.531 | 2026-02-05 05:33:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ce52710-7328-3c8f-be67-d22b137e9fa3 | 3.4248 | -60.73895 | 2026-02-05 06:18:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 501b9e4a-6679-32b4-be53-b104f1cf6624 | 3.4239 | -60.73367 | 2026-02-05 06:18:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8ce8f6c-f5a4-39d9-9979-d136822d291c | 3.42938 | -60.72725 | 2026-02-05 06:18:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55bc230c-e302-3a86-a34d-d9db4e119d7d | -9.45122 | -36.78225 | 2026-02-05 11:34:00 | TERRA_M-M | ESTRELA DE ALAGOAS | ALAGOAS | Brasil | 2702553 | 27 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e65f6fdd-269d-33f1-a82c-c2ba8ba2bb29 | -10.64345 | -39.21521 | 2026-02-05 11:34:00 | TERRA_M-M | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8523d916-fb0d-33ec-afd9-0d9387c83762 | -8.60783 | -37.70212 | 2026-02-05 11:34:00 | TERRA_M-M | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 4fd0c3b5-5e71-36e8-b950-553759496d47 | -9.3908 | -36.90703 | 2026-02-05 11:34:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 9.2 |
| d1e5e1e9-8709-3e43-b47c-94a443a5dfe8 | -11.40955 | -40.75035 | 2026-02-05 11:34:00 | TERRA_M-M | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c6bea7c3-5a79-3b75-b496-47fd8c37a070 | -15.42652 | -41.42734 | 2026-02-05 11:34:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 4904a9e7-4dd2-3051-a1ed-66277e11ed15 | -8.65878 | -39.60971 | 2026-02-05 11:34:00 | TERRA_M-M | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7fb01747-ca60-3649-8b9a-2d2e4a14c4ab | -11.10495 | -38.16142 | 2026-02-05 11:34:00 | TERRA_M-M | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6a6845b5-b86f-3a48-bdf5-54deceacde39 | -9.01697 | -37.67719 | 2026-02-05 11:34:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b1e270dd-ae30-3bf6-b9ae-3626c2614c68 | -10.57967 | -38.62851 | 2026-02-05 11:34:00 | TERRA_M-M | BANZAÊ | BAHIA | Brasil | 2902658 | 29 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 2f7ffe95-d6d2-3f46-84bd-66c13b63afab | -11.5004 | -40.57444 | 2026-02-05 11:34:00 | TERRA_M-M | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2f15e711-6339-3b3a-b7a8-7dc2c6c78a1e | -9.09569 | -36.68984 | 2026-02-05 11:34:00 | TERRA_M-M | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6dff31df-9188-3f33-815a-089650c4c9cc | -7.58726 | -37.15798 | 2026-02-05 11:34:00 | TERRA_M-M | OURO VELHO | PARAÍBA | Brasil | 2510600 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e7475100-abe9-3353-a7f8-c8c9dd2548b9 | -15.19554 | -41.17645 | 2026-02-05 11:34:00 | TERRA_M-M | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| b86ce4a6-c531-31b6-866a-67149172fbed | -6.9774 | -35.41883 | 2026-02-05 11:34:00 | TERRA_M-M | MULUNGU | PARAÍBA | Brasil | 2509800 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0c5da817-b248-37f6-a121-672a38b140c2 | -9.39224 | -36.89657 | 2026-02-05 11:34:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 361dd007-97b8-3a60-b136-38a9b4219bd5 | -17.08284 | -39.55319 | 2026-02-05 11:36:00 | TERRA_M-M | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 4375ff08-4c83-30b6-aad8-89e78871b0b7 | -9.234 | -40.0228 | 2026-02-05 14:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 143.1 |
| 96a9affd-5911-30f1-9716-14fe2de43861 | 3.7493 | -60.6394 | 2026-02-05 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |


