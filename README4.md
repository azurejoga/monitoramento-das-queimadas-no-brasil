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
| 321c91b2-fd8d-31b2-a5c2-c748f6573031 | -7.62345 | -39.23555 | 2026-03-05 03:25:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a05ce2d2-8547-32b5-9f5d-bb28b3a9bdbe | -9.86999 | -37.16764 | 2026-03-05 03:25:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 71ee870e-a2be-36f5-8c7a-73a0ee0373bd | -9.56088 | -36.92153 | 2026-03-05 03:25:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f585baf2-658b-3a00-bd76-c7810990c778 | -9.32136 | -41.24656 | 2026-03-05 03:25:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| d1f1ba02-8481-3d92-9d83-1c7c6b0d913b | -8.21711 | -35.9599 | 2026-03-05 03:25:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 46339ae8-0e1f-3975-b391-3749ab328a8e | -8.58538 | -43.60745 | 2026-03-05 03:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0fbf55b-7049-31f9-b335-d568dfc694ac | -19.31324 | -40.25946 | 2026-03-05 03:27:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0e22451f-921b-35e6-9258-b0a7e02fe5dd | -13.58566 | -43.44542 | 2026-03-05 03:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06b12a09-d3cc-3e90-be3c-ccd2473ef2b5 | -17.42121 | -41.79065 | 2026-03-05 03:27:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| edb92907-48bd-3f44-8ee5-2f459a91faf9 | -19.31758 | -40.2605 | 2026-03-05 03:27:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f781f43d-d2db-3856-a9b7-e9af0146d74b | -17.00672 | -41.89489 | 2026-03-05 03:27:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| ba47201f-3b2b-30e6-a7df-1e8ccddbb413 | -18.04622 | -43.35575 | 2026-03-05 03:27:00 | NOAA-20 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44cbcb07-553a-3464-adcd-cb15d3b2d6c9 | -19.318 | -40.25907 | 2026-03-05 03:27:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d5d28d15-c39d-39e2-ac01-610167952e74 | -16.296 | -44.34969 | 2026-03-05 03:27:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 10a45b92-590c-300b-920d-ab69e848e598 | -19.31367 | -40.25803 | 2026-03-05 03:27:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 16879483-f6b8-35d6-8110-4e5f6981536d | -15.78472 | -42.90105 | 2026-03-05 03:27:00 | NOAA-20 | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec061534-f4f5-35e9-b2c9-2d0dcc1888db | -15.83566 | -43.98395 | 2026-03-05 03:27:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0170e4f-6573-34ea-b8da-76d2087115d2 | -18.38018 | -44.97388 | 2026-03-05 03:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b738c55b-9cc5-3ff2-977e-2058e276ca62 | -15.59062 | -46.65319 | 2026-03-05 03:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| af8cd2b3-3149-331e-8d51-86599046e213 | -16.31771 | -43.97652 | 2026-03-05 03:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a29e90fb-c93e-3307-b0c5-b31b14292765 | -21.29674 | -48.59911 | 2026-03-05 03:29:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3e8f71d1-fc90-301c-8c81-b1b1af3e049b | -24.79048 | -49.63678 | 2026-03-05 03:29:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 987f3f80-9012-3239-87e2-6ddc883d20ce | -20.9329 | -48.71801 | 2026-03-05 03:29:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9e55d448-272e-3d4c-98c5-215315fffa4f | -20.93527 | -48.71763 | 2026-03-05 03:29:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fcba301e-f479-393f-b1f7-be10c47cef61 | -22.92189 | -48.61284 | 2026-03-05 03:29:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ef14a6f-0ce3-3deb-b88d-30e3534bb3ea | -21.643 | -46.54618 | 2026-03-05 03:29:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e71b8c98-2d85-3942-aa34-477eae745e71 | -21.39049 | -45.20129 | 2026-03-05 03:29:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2058769b-0c51-3cf8-ac38-39e2448cdbbf | -20.93974 | -48.72025 | 2026-03-05 03:29:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e2e6193e-cf34-3790-ad70-e42f2b3d9f8e | -21.29755 | -48.59999 | 2026-03-05 03:29:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e90066e5-2ab0-3c1a-aa2e-eedbc7e022e1 | -22.91903 | -48.61339 | 2026-03-05 03:29:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0af0ab9c-b4ee-3cdd-89c3-fcfeb4ce8909 | -22.80017 | -48.01887 | 2026-03-05 03:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c6ce5f0f-0786-3e53-95ff-6c4a086da4ec | -25.00347 | -49.29635 | 2026-03-05 03:29:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bec2a611-b5d8-3152-b3d3-036b28571877 | -23.21974 | -46.56386 | 2026-03-05 03:29:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a94b897-c1f9-322a-bb6e-b77a6887a9ba | -25.01024 | -49.29753 | 2026-03-05 03:29:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7521aa9d-b261-3402-93c5-8ae24e699c67 | -23.80457 | -49.42092 | 2026-03-05 03:29:00 | NOAA-20 | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| f564305a-20b0-3cb0-82aa-d5b181032658 | -22.96221 | -49.91426 | 2026-03-05 03:29:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 04b839fc-7a5b-3833-bfc4-f11cf9855be1 | -23.25692 | -46.7569 | 2026-03-05 03:29:00 | NOAA-20 | FRANCISCO MORATO | SÃO PAULO | Brasil | 3516309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| d9352c2c-2f08-3204-ba30-438ddc8efc84 | -22.52506 | -44.40405 | 2026-03-05 03:29:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 723aaf14-9b8a-3121-8274-3f8628b6afdc | -24.27212 | -49.72403 | 2026-03-05 03:29:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6319141b-6078-34c4-b4ac-2338cbad1eea | -20.63035 | -44.28803 | 2026-03-05 03:29:00 | NOAA-20 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| efcf4dda-5393-3faa-b981-6dbcf3e046c5 | 0.0455 | -60.9799 | 2026-03-05 03:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f34e3f99-c53f-3142-837a-3bea21d4ef2a | 2.7816 | -60.3528 | 2026-03-05 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 09b349fa-5afe-3d02-86a1-4bf723ae697b | 0.0455 | -60.9988 | 2026-03-05 03:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| ead1f1ab-6c9f-38e6-bbe5-6de317bdc78d | 2.7816 | -60.3338 | 2026-03-05 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 42f3036d-edd8-343a-97ce-bec5ea762f4f | -29.67325 | -49.97698 | 2026-03-05 03:32:00 | NOAA-20 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 73865ceb-7b59-33ac-b20d-69024c8b705b | -29.67041 | -49.97507 | 2026-03-05 03:32:00 | NOAA-20 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| c2d0d68c-9085-31e5-a916-e7e274073604 | -25.0132 | -49.29832 | 2026-03-05 03:32:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7e3a501d-1409-3a2a-836d-3f70d26ed524 | -25.00643 | -49.29713 | 2026-03-05 03:32:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7ba4027b-1093-3458-bf9e-4a7b819ba4f3 | -31.8168 | -52.34587 | 2026-03-05 03:32:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 58868203-3e9d-3e06-acff-5e893e5d2e66 | 2.7816 | -60.3338 | 2026-03-05 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 21581883-7d0b-3d69-a8d7-4333550d9489 | 2.7816 | -60.3528 | 2026-03-05 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 124.6 |
| f6452537-6af6-31dd-98e0-b82b1da8736a | 0.0455 | -60.9988 | 2026-03-05 03:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 28.6 |
| dda5d984-553a-3089-b5e0-989b04d1e7ee | 0.0455 | -60.9799 | 2026-03-05 03:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 9fc7948d-931b-364a-bec3-5ef2c16fb5da | 0.0273 | -60.9799 | 2026-03-05 03:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 1bd12794-ab96-3a4a-9a7c-96b617bc8b01 | 2.7816 | -60.3528 | 2026-03-05 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 81c25077-3f32-3fc6-8b95-b0775b36b338 | 2.7999 | -60.3335 | 2026-03-05 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 584cc975-677c-3832-960b-2810311474bc | 0.0455 | -60.9799 | 2026-03-05 03:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6d8b5bfb-21cb-3269-8f3a-846bb6a146cb | 2.7816 | -60.3338 | 2026-03-05 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 137.2 |
| af02dcc1-dd68-341b-840b-a5caac1c16de | 0.0455 | -60.9988 | 2026-03-05 03:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 2ef51614-5d64-3bee-a321-6bea8a728f3b | 2.7816 | -60.3338 | 2026-03-05 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 45df97d8-fc9b-38a0-8f07-1b9b820176d9 | 0.0455 | -60.9799 | 2026-03-05 04:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.9 |
| c240d672-1ef4-36e2-a186-0ee0153df762 | 1.5047 | -59.9116 | 2026-03-05 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a7a098d9-01b9-31c9-8e89-866d6ba5eb0e | 2.7816 | -60.3528 | 2026-03-05 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 38bfde18-fc23-322f-92cb-fe5794a6863c | 0.0455 | -60.9988 | 2026-03-05 04:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 12730bd8-8933-311d-978d-15dfc514c587 | 2.7816 | -60.3338 | 2026-03-05 04:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 78eeb3ba-7553-3f1b-8699-dcbd1f07613b | 0.0455 | -60.9799 | 2026-03-05 04:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 49ef007a-7f30-3171-bf2a-14626218280a | 2.7816 | -60.3528 | 2026-03-05 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 28e533c9-a665-3687-b90c-cd3fe9ef545a | 0.0455 | -60.9988 | 2026-03-05 04:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 3671b8a4-76e9-38af-bcea-58e20d35e71a | -5.89789 | -42.55103 | 2026-03-05 04:14:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9dc757d2-6c56-319d-b19f-73674386f38b | -4.53052 | -37.99805 | 2026-03-05 04:14:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84c01e70-c1ec-39db-bf7b-cb3b0bf7e0ca | -4.52656 | -37.99747 | 2026-03-05 04:14:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b85c08cd-bad1-3316-bd40-7923303bef32 | -9.66143 | -35.72915 | 2026-03-05 04:16:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1d6f2789-c8f4-3aa3-9098-6dd4a6584692 | -11.11783 | -38.60651 | 2026-03-05 04:16:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b7bb529-e1c9-3d5e-bd1c-233d1161fd26 | -17.57955 | -53.07335 | 2026-03-05 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4b96fab-19bd-300b-beac-79b054b6ba70 | -19.90562 | -49.41413 | 2026-03-05 04:18:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dd3935f9-f607-3dd0-9088-9ad00a316d3f | -19.69394 | -47.96876 | 2026-03-05 04:18:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 947fae95-27eb-32f3-ba2f-017189c0ff87 | -19.90917 | -49.41483 | 2026-03-05 04:18:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fdfd488b-3c0b-35dc-9f12-3318de0463d0 | -19.32022 | -40.25806 | 2026-03-05 04:18:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| afd917ad-2957-30e2-bc15-b40ba39eeda6 | -17.52603 | -53.69903 | 2026-03-05 04:18:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9e157a6-97fb-3d38-87a3-e86b52772180 | -18.89666 | -54.7252 | 2026-03-05 04:18:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7017d311-50b0-3d39-8207-9b60ba1eb97f | -19.69459 | -47.96492 | 2026-03-05 04:18:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 729ca76e-2b11-31fd-bfd2-0aa8a80fdfa6 | -19.316 | -40.25753 | 2026-03-05 04:18:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c2d8701f-975b-3211-a674-7ee0f8d77ea8 | -18.86579 | -51.64072 | 2026-03-05 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7340ad45-49d5-312b-b1e1-a4f82dfb8ace | -17.31288 | -44.92968 | 2026-03-05 04:18:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068104f6-33db-31b0-85da-0ca4de8b2510 | -20.08678 | -40.21772 | 2026-03-05 04:18:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 84b5cb96-c67b-3c58-a940-773b4512442b | -19.79301 | -47.9666 | 2026-03-05 04:18:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36248351-94b2-3d97-8c8f-9b0a6143bbd2 | 0.0455 | -60.9799 | 2026-03-05 04:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 338359da-c3ca-3467-bde3-939757ebcf79 | 2.7816 | -60.3528 | 2026-03-05 04:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 983d28bc-4965-31e9-bd94-d64c60943a84 | 0.0455 | -60.9988 | 2026-03-05 04:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 14d7fe19-327c-3f5f-8e5c-83da07c1f1ab | 2.7816 | -60.3338 | 2026-03-05 04:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 149.5 |
| e60af49f-45a2-3b1c-bf8a-41d6bec9365f | -23.01936 | -49.26859 | 2026-03-05 04:21:00 | NOAA-21 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e6ff5a39-7fad-3ac3-95c9-84fd2264466f | -21.70115 | -47.16985 | 2026-03-05 04:21:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c6224daa-77aa-34ad-a03c-29a4a814efb3 | -22.9233 | -48.61089 | 2026-03-05 04:21:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63c54b07-71d8-39f0-aa84-103d4b1511f3 | -20.96057 | -47.1818 | 2026-03-05 04:21:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82a82620-2b3c-3e57-97b0-bad3ba145d6b | -22.61 | -47.46776 | 2026-03-05 04:21:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0521b65f-6317-35d6-ae84-7a539c7619b2 | -21.48587 | -48.65654 | 2026-03-05 04:21:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b046136-79b3-32f4-a34c-eb00350611d5 | -21.23438 | -48.52096 | 2026-03-05 04:21:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb2ece84-eedc-3c2b-b8e5-b6a39258d27a | -20.94104 | -48.7142 | 2026-03-05 04:21:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f89a5878-3631-36ba-bd1b-c553cdcb321d | -27.07981 | -49.55558 | 2026-03-05 04:21:00 | NOAA-21 | IBIRAMA | SANTA CATARINA | Brasil | 4206900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 17e91983-fc3a-36f7-8c21-d72086f41fe5 | -25.00798 | -49.29641 | 2026-03-05 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)
