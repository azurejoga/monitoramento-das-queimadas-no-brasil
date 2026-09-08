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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eec946b-ce69-3c63-8e23-efddf3abdbb7 | -11.31502 | -45.06333 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d68bbbf-747c-3b3b-a947-4b3bef665612 | -9.72556 | -43.47097 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b064eee-5b9d-3d06-a2c2-9484b677e358 | -9.76978 | -43.42508 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8545a5bc-ed06-311d-b4cd-2738dbb6e6dd | -13.43412 | -43.81608 | 2026-09-08 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be7e3773-0bb1-3666-839a-c7b9a63fd48e | -13.43043 | -43.8115 | 2026-09-08 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| affa8353-f639-33aa-9173-153ea78a43ac | -13.22298 | -61.71581 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b91c51a-1f6a-3ccd-be6e-9c7b0d4a51e3 | -11.13165 | -41.85671 | 2026-09-08 04:46:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ded8b09f-71dc-3075-86ce-b99b6c33053c | -9.71128 | -43.42411 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 39bf7743-5388-3441-8dea-533c18dea467 | -9.76198 | -43.45012 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 236a9704-010e-3ee3-ad6a-5d6af7cd9f54 | -13.25795 | -61.70715 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b116ce9-600c-34b7-876b-549eae0f7d8e | -11.36984 | -45.74056 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b118cdfe-ee1d-34ad-aee1-f7182f36880a | -9.7184 | -43.46258 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc87f327-d005-375c-804f-321726331e86 | -9.71282 | -43.41315 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 78d66e1d-3c68-356c-bce5-8b2b63bf9d89 | -9.71225 | -43.44699 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eecb7467-017e-3cc8-9a1e-238d376a9786 | -9.09031 | -47.81712 | 2026-09-08 04:46:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a1a7147-4536-38f1-bc00-75204cace126 | -10.77035 | -60.78416 | 2026-09-08 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8adad5f-c4a2-36c2-a428-280f1ae4f1d6 | -13.27406 | -61.78796 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 17d8ac8c-ea73-3923-b052-7797d9688761 | -10.76933 | -60.78923 | 2026-09-08 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42b4138d-f1f0-30cc-946d-672253338c16 | -9.76607 | -43.45072 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8842298-eee0-3067-bc69-b5c5d14996ff | -9.73619 | -43.51338 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41896b96-3a05-3f68-a95a-044cb6bb8124 | -9.76026 | -43.49097 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97d50539-2377-3a0c-90a4-33899117fc90 | -9.74444 | -43.48488 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0981a9cf-e575-3ff3-8d3d-4e3f11f68975 | -9.72301 | -43.45951 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e462703-4b25-3d98-ac75-fd9905875149 | -14.27977 | -42.69261 | 2026-09-08 04:46:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 607e2bef-4b21-310b-80ec-72cf23ab3c7a | -9.75893 | -43.4422 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2317569a-5f9d-331d-8308-c8e1ed8a522e | -9.71025 | -43.43149 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ba22cff8-ed37-3d34-bb47-8cc327d55d5a | -6.63992 | -59.44273 | 2026-09-08 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed4cfbf9-61ab-3850-89e0-b93213ea72e4 | -11.31549 | -45.08699 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e018926-6370-3177-adfc-97386996b823 | -9.73879 | -43.49522 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c2474a2-41b9-3f6b-94b2-16d8a33bdfd3 | -11.38682 | -45.75183 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 749ded65-d85f-32af-987f-edbf1d482c86 | -12.73289 | -44.84249 | 2026-09-08 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8778102-5134-33b6-a6ad-e894f26069b1 | -9.71334 | -43.4095 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a257b2e4-98fe-3ef9-97eb-9f4233fdf93a | -15.05172 | -41.33014 | 2026-09-08 04:46:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8cf04f20-ca14-3af3-b8bf-cbd2b824903b | -11.31616 | -45.08236 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 176270b1-3052-362c-8afc-da940b0704cf | -9.7097 | -43.46507 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d59e6c24-0755-3144-b2e7-13420826cf29 | -11.1323 | -41.85183 | 2026-09-08 04:46:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9c5e69fc-af16-3b1f-999c-1de0cd1665ee | -13.26236 | -61.70922 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b23eed5d-dd4f-3058-961b-a5b778ff8e5b | -11.93116 | -49.74275 | 2026-09-08 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7003d34e-7ec7-3996-9e1c-7b0336adf6eb | -9.71897 | -43.39924 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d129ce6c-4ebb-3916-816f-483e2d1ada73 | -13.26316 | -61.71379 | 2026-09-08 04:46:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 839e08f9-b5e3-3957-9de6-b8199e02e0b5 | -9.70919 | -43.46868 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 388ca142-6157-36ed-950c-7fc13af6b0b2 | -8.67795 | -49.40493 | 2026-09-08 04:46:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed43b242-2a9a-3d36-a1c4-fc10c376a082 | -9.76183 | -43.48006 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2434564d-a29c-3d6b-af82-02d92f87f310 | -13.43464 | -43.81215 | 2026-09-08 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c693fccc-6120-3c0b-9e46-a3211224b70e | -9.73775 | -43.50251 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1c13791d-92d8-3152-8e1c-f0c815cb56ab | -9.71949 | -43.39554 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 371c1c6c-5193-34c5-8bef-36b5db5ea139 | -9.72874 | -43.38942 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ad59ca43-f8cc-375f-aea9-60aac258c709 | -9.71431 | -43.46202 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a71162b-7275-380a-8e9e-369ba54f68b2 | -13.2774 | -61.77208 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d79b98ad-be65-3386-a3dc-12498d67f5f3 | -9.7281 | -43.48248 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40f43805-9636-3536-8907-9a5a9179d5c6 | -13.27629 | -61.77737 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| aa6d59fb-f5fd-338c-84a0-73411e437ca8 | -14.91205 | -44.66805 | 2026-09-08 04:46:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4ed8972e-605e-3db4-bf31-b005044e6716 | -11.9484 | -49.74196 | 2026-09-08 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b05839f2-07f1-3904-9d7e-cfd6ee411b96 | -9.74497 | -43.48123 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1552bc55-7215-3837-80a3-17e51edad226 | -13.42622 | -43.81087 | 2026-09-08 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3c177f2-0450-31bf-b667-394237dd7e1d | -11.34922 | -45.72852 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5aef0b5b-dbb6-3cae-8f88-2eff3670ec67 | -14.91107 | -44.67541 | 2026-09-08 04:46:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd706328-b084-374a-9ac8-907073b9b181 | -9.70459 | -43.47171 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 52bb8180-e738-31eb-8704-f25cadc8d36c | -12.73358 | -44.83748 | 2026-09-08 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34ba00b9-3eb5-3828-876d-c84dd9ec5617 | -9.74036 | -43.48426 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fe1680c-52ae-3dbb-824d-f5ed4a90088c | -11.31437 | -45.06787 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c37857f-0987-3cbf-bcbd-fbb5db07bbc8 | -13.24864 | -61.7116 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb248d8f-accb-348d-ade9-41ece0f0db8d | -9.95351 | -48.17396 | 2026-09-08 04:46:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40a1da43-f8fb-311b-bf7d-4271f2354134 | -9.08976 | -47.82066 | 2026-09-08 04:46:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2af95c53-2ef9-3bde-a498-2fd5957b91cc | -9.74486 | -43.51101 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 596dd39b-c8f8-36f0-82fe-5fbade4e390b | -9.70972 | -43.43523 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8fe4b5ca-444b-312a-9ee8-eede39844ef6 | -9.71845 | -43.40292 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 028c774f-22d8-38de-b933-1f783e9c1063 | -13.27517 | -61.78265 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf892792-8226-344a-9002-f5d3ae74a979 | -9.71385 | -43.40586 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 85fcc888-3acd-3b5e-98b1-e71851dfec78 | -13.25604 | -61.70779 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e42db5cc-28e0-326d-ba9e-f4e759f59635 | -9.76713 | -43.4434 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf24b9fe-c8c0-3eaa-a032-dd3c58c835a1 | -11.94116 | -49.7444 | 2026-09-08 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1d3b4ff-3ba6-33a3-aa73-4fa15d5bc8c2 | -9.72096 | -43.47403 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 349b9bda-1601-3004-9100-ede7f4c22b77 | -14.91156 | -44.67173 | 2026-09-08 04:46:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8b598e87-5fc9-37df-bc86-c484497d5492 | -11.31926 | -45.08763 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 084d9987-7071-36a2-b5a9-fcf185e0dbb5 | -13.27851 | -61.76679 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 903e8663-106c-3585-bcea-0b316817b648 | -11.34557 | -45.72795 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98b3cc10-8dd4-3abe-8cd9-f2bb3472741a | -9.72358 | -43.39631 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 660d9630-c99c-3df7-8239-ee7283c4572e | -9.71231 | -43.41679 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| a6d8607b-e984-39fc-81f6-ab654ea4cdb9 | -9.71892 | -43.45895 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ba95578-a42f-3181-93a8-53c5d56ddb44 | -9.70868 | -43.4723 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 416cd37b-827f-3ae4-a0b7-699f06be4815 | -9.76395 | -43.4654 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cc71ebc3-be4f-3f8a-af6c-7d4c7c0abcee | -9.5075 | -41.99553 | 2026-09-08 04:46:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3223d2b4-f8ec-3927-93b7-2a95614d33c4 | -9.95158 | -48.17323 | 2026-09-08 04:46:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c6216b4-203a-37e6-b0cd-2b0c80e2bb31 | -9.76131 | -43.4837 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 922d1cf2-6776-3ddb-9fee-b2a044c092d0 | -9.71794 | -43.40656 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| be34842b-8ba8-362b-b4c7-075737aa8e63 | -9.76448 | -43.46172 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ae6ca503-d203-3c67-9103-224d39a23e18 | -13.2293 | -61.71722 | 2026-09-08 04:46:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08ca23f3-ab7d-35ab-85dc-640e57eed12f | -9.95406 | -48.17044 | 2026-09-08 04:46:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1500d20-10de-334d-9d3f-91a953a16d93 | -11.93783 | -49.74385 | 2026-09-08 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2efaab53-8535-3fcc-8886-51bd74abfe42 | -9.71071 | -43.45789 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9993f51-020b-3bfa-bf7c-97327e62719f | -14.91513 | -44.676 | 2026-09-08 04:46:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d8eb7dd-19b0-3c0f-a986-303b97be5312 | -6.6357 | -59.43939 | 2026-09-08 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 688b1aad-2db6-3c0c-a9ca-c0a1aa4db3ff | -12.9447 | -44.72639 | 2026-09-08 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b5cec7e-5e69-3d06-85fc-e91f3397f85f | -9.73671 | -43.50977 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8606174b-8845-3a7f-884e-52b10762e9e5 | -9.72305 | -43.40002 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| de307f0d-cc0f-36e2-86e3-0b4e47385673 | -13.43832 | -43.81674 | 2026-09-08 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9003e838-efd4-3f6c-9b26-80c7aff1a94c | -6.63478 | -59.44456 | 2026-09-08 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 93ab4200-0787-3bde-be08-4d00acb6f514 | -13.4299 | -43.81545 | 2026-09-08 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5ce40fe-7019-349a-966c-39d96b4b5caf | -11.93449 | -49.7433 | 2026-09-08 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
