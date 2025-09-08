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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcef7970-9344-3af1-b5d7-6ed248cb7d93 | -15.68244 | -53.55835 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16e80a08-4b0a-364f-9acc-cf392c3007cf | -19.9532 | -46.19889 | 2025-09-08 04:04:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f04ed5f9-9d80-33c8-b460-7638dd141bc5 | -21.21705 | -44.02632 | 2025-09-08 04:04:00 | NOAA-20 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8882a274-0127-363c-a61a-4ba7902dc84b | -17.66974 | -43.53763 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91fc04f8-f20c-32e4-ae43-8abe8d06eeca | -17.64134 | -44.78397 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dfb885a-ebe5-3c07-b52b-61db0bd0c277 | -16.28669 | -45.68229 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7a43d2d0-aeac-36d8-809c-e56074c77864 | -19.64618 | -44.25966 | 2025-09-08 04:04:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f668171-f607-3f0e-b034-f9c48cf8c02e | -17.22579 | -48.28522 | 2025-09-08 04:04:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e45d0cc-cafa-3b07-a02d-69a703d96301 | -19.20831 | -43.73473 | 2025-09-08 04:04:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f43e9b1c-7013-38b5-b19e-f35304171a38 | -19.95674 | -46.19966 | 2025-09-08 04:04:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 693e0519-f42e-313b-a5fc-daca1313ddb6 | -15.75084 | -53.54008 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9645468-bb6c-323a-abcf-f3f73bdd8e84 | -16.90875 | -45.819 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35719f46-ff47-3a40-8bbf-d5cdfd251923 | -15.25445 | -52.38709 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57858cbe-64db-3242-9c9b-26e35dd0673f | -17.58378 | -49.80417 | 2025-09-08 04:04:00 | NOAA-20 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcdf8c31-b3bb-35ae-b6e1-a559fbec53c3 | -18.11115 | -44.49963 | 2025-09-08 04:04:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ede1f70-fd8f-37cc-9919-2a286a6e0557 | -19.592 | -43.69207 | 2025-09-08 04:04:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48df8478-7f73-3ef3-b7b0-f0444fed4bce | -19.63392 | -42.03726 | 2025-09-08 04:04:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 552de805-f566-3cf8-bd80-62e85fd6923b | -16.44837 | -49.28466 | 2025-09-08 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ec9fb44-0f75-3ae4-b05e-e770da5a9026 | -23.15167 | -47.01791 | 2025-09-08 04:04:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2b584074-65f6-3671-8585-0029b3f3d036 | -16.89534 | -45.76644 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93c651c8-8f3c-3733-a5fc-af0dcb12a5a4 | -19.36658 | -44.50912 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e11056fd-d2c9-32b3-9fcd-638d1918eb71 | -15.83302 | -52.26867 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 765e3670-6235-35d2-bcbb-9cfd22089836 | -15.75408 | -53.55399 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed0340ca-e4a2-354d-b9c5-c0cb0fd87309 | -17.14989 | -44.4328 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| adcc4ac9-84a6-3072-9d9c-ba3eab20c789 | -22.68969 | -46.92242 | 2025-09-08 04:04:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c9ca6c8c-4d6a-3074-97aa-0ff9d458918e | -16.33331 | -52.93188 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 54a1e70a-6669-3b2a-82ea-36d411bc0151 | -18.35456 | -43.92255 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00d6c8fd-47b5-34aa-9196-6a56bd825e43 | -17.40022 | -49.31145 | 2025-09-08 04:04:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34c80512-f199-37c4-b544-4e723159aba8 | -17.2575 | -46.69735 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6f49531-45fe-3eb3-b7ab-cf0c58eff1da | -17.14724 | -48.68198 | 2025-09-08 04:04:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c810e60-c139-33e3-98f4-8b535b084469 | -17.59211 | -44.53741 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50f93dae-63fe-350a-b006-37ee6c9c9a90 | -18.78642 | -44.40592 | 2025-09-08 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf3e4273-da9f-3c44-8b09-e1f824c3bb86 | -16.94007 | -45.8556 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdc27a29-52a4-3243-b5cc-8c5ce29ef7d2 | -17.64411 | -44.78855 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b0c2f8b-f515-3531-ab54-7b066094a997 | -15.75763 | -53.55747 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f6724b7-37f0-3d88-aa7e-27b3dd4236d7 | -16.90924 | -45.8176 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b266bb1-e329-3626-9d0d-5210abb0e609 | -15.24965 | -52.38201 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8297f3e6-549d-3844-92a5-767cae4cb381 | -16.5394 | -45.11113 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 777ecc81-8ba9-33af-a092-738ab1e8f5b0 | -18.0357 | -44.33941 | 2025-09-08 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 825af888-194b-3834-9160-d15f881c76aa | -16.94053 | -45.81028 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bce3969-5cb7-3299-950e-38941a576be4 | -17.15306 | -44.43291 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5af31624-4498-3fb1-bb26-0c58562270bc | -17.25836 | -46.69252 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d17e01ea-8902-3ac3-a0dd-b6c907c00a72 | -19.69958 | -49.28466 | 2025-09-08 04:04:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16ea251c-839c-3168-b98c-a277d1436de3 | -17.66417 | -44.19112 | 2025-09-08 04:04:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27579ee2-7c41-3d2a-bc86-5f173cc4aba8 | -17.25456 | -46.69184 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eed44ff-4d72-3a06-a94a-d471e4f24ad7 | -15.75847 | -53.55344 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a38603fc-2039-34de-8e19-126d86a00c2a | -16.54435 | -45.10353 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05c3e2e2-f1fb-3ca6-818a-ccf20e97eba6 | -15.24724 | -52.36544 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bde53b8-1aac-3822-93f1-a4f0bc6c360f | -19.21224 | -43.73165 | 2025-09-08 04:04:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be4531f6-679b-3d34-bd95-6540e4475dc2 | -17.66078 | -44.19054 | 2025-09-08 04:04:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cda8308-36c1-3cd5-a4d0-f8337a4a8692 | -23.18085 | -47.24875 | 2025-09-08 04:04:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 20a075b1-cddf-3acb-81a7-9afb505fb4a7 | -15.66673 | -53.87048 | 2025-09-08 04:04:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5c2be15-aa1e-395d-ae1d-491c0dd36f4a | -16.93356 | -45.78608 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d4c18f64-bcf4-3dc7-b0c9-d511e2c30d93 | -16.27866 | -45.68534 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2da1c74-f9a1-3063-88a8-b1b61901b8c5 | -17.5771 | -44.54275 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4093d84b-6ad9-358c-896e-2e4941fa5223 | -16.90846 | -45.82198 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30c9e6ec-534b-33f1-a725-f1a62ab23c7c | -16.52457 | -45.11264 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c36853a-806f-33ec-8f75-48c3b7066b8d | -17.69544 | -48.77119 | 2025-09-08 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac690ef6-c83d-3077-b2cc-f72c712a0d0e | -19.18703 | -42.07706 | 2025-09-08 04:04:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 3142be17-08e8-35f2-ae0e-96bf91c48bb6 | -16.29653 | -45.69097 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6cf4896-c0e1-3e82-83af-88f7f2dafb76 | -16.91388 | -45.811 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39d6d940-5ced-343c-aa10-933d68e3be5f | -18.02665 | -47.1139 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 16351bff-d1ef-37ec-8d5f-cef47c23291f | -16.34768 | -52.94831 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1580d31-1500-3dad-8079-d65cb821c23b | -18.40689 | -43.89751 | 2025-09-08 04:04:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d1fab93-9e8b-3371-9a67-c735e4abe0a8 | -15.74832 | -53.54226 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f17f0ab-7a1e-3406-8a7c-1ac527cfc7e6 | -16.94262 | -45.81972 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80d9326c-6e94-3ff0-bacf-f084e2f714db | -15.75428 | -53.54361 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b0f696e-1a00-3eb4-8a31-2f5b98db6fb2 | -19.92495 | -46.17118 | 2025-09-08 04:04:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5dead6ee-7c31-311f-9fe8-73cd177d46db | -15.83778 | -52.27344 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92c49fde-aae6-368e-b0a2-9866e114103a | -16.34295 | -52.94251 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c589f89b-7602-3599-8fd5-369b2660fd50 | -17.10729 | -48.99362 | 2025-09-08 04:04:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b11ef9d1-7181-398f-9b08-889ee6026eab | -16.90856 | -45.84196 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 381c6711-c0db-37f3-80ac-3e1be0041f52 | -16.5267 | -45.10026 | 2025-09-08 04:04:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81cfb666-4b2f-35d2-95a9-da383c3287ce | -20.84964 | -54.98585 | 2025-09-08 04:04:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8aaff288-2d03-3ef4-ac75-2f892cfa39cb | -15.68659 | -53.56826 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da2bd6f7-a75b-3913-884e-99a1944cd62f | -17.66141 | -44.18677 | 2025-09-08 04:04:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77e4167b-d9d3-3e69-8fcc-8b1d5362db26 | -18.14786 | -43.39825 | 2025-09-08 04:04:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13b8624a-47db-3fd9-bde5-52d134fa6ee5 | -15.25286 | -52.39471 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee6698cb-34c7-32c1-a611-6538e84530c7 | -15.96393 | -48.11012 | 2025-09-08 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9b50bdc-9616-35eb-a7bb-210b2d1229e2 | -15.22709 | -52.3499 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| befdfcc7-4e36-3633-a600-45b0a90f71aa | -17.15989 | -44.43427 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b5e12bdb-d4fb-3f3a-922c-fa2630fd7cb6 | -19.62124 | -43.95595 | 2025-09-08 04:04:00 | NOAA-20 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b62471b-e9ee-3dbc-8e8b-266d2102e515 | -18.14393 | -43.40137 | 2025-09-08 04:04:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| befe3416-36f8-371d-aaf7-817a64b49c73 | -16.34126 | -52.95048 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33ac7eef-d0f8-3a2f-9dd3-3279e611ba11 | -18.4294 | -48.7897 | 2025-09-08 04:04:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 8c8c9566-d069-3423-97c0-a0820f65d28a | -16.93589 | -45.77287 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a84d3347-4a9a-3129-9ea7-f7bfc37e0c65 | -18.63196 | -42.76815 | 2025-09-08 04:04:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74835c02-1640-3103-8520-e6fb54717ac5 | -16.2799 | -45.67878 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8bf3f54-f839-3e29-aa70-8e06b6c8516c | -17.66479 | -44.18737 | 2025-09-08 04:04:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34669f6a-2eb4-3ee0-ab96-5f0de1443325 | -17.90145 | -43.40793 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7f8f9b86-f5d9-3cce-8ff0-4018d9d29b48 | -19.35728 | -44.52314 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93bb376e-d077-3f2b-9d96-f52cf8abe4fa | -19.40033 | -44.5153 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80a672a7-8c94-32f9-b36f-236a2668b381 | -16.90973 | -45.83598 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 483c2295-c934-34cc-9acd-c834b39fa016 | -16.51893 | -45.10307 | 2025-09-08 04:04:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8aafd52-ea89-3371-b1a2-11e08185f70d | -21.22037 | -44.02694 | 2025-09-08 04:04:00 | NOAA-20 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 96d44601-9bc1-3c8e-b4c3-940ec152b8d1 | -17.4392 | -50.22415 | 2025-09-08 04:04:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b6a583a-b0bb-3384-9aad-59c1d1acfe32 | -15.22399 | -52.34914 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f80de32-757e-3a7a-b207-92394562b13d | -19.87127 | -46.14886 | 2025-09-08 04:04:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2a916dd0-5a7b-3b86-8adb-cdff29671f11 | -19.36257 | -44.51229 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f093779-45db-3002-b40a-021cabdc3b4b | -17.23856 | -46.69376 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README49.md)
