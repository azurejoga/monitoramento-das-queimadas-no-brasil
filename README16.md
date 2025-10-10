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
| b00739c3-69b4-3419-ab94-8f428762d36b | -18.01991 | -45.01583 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5e27c235-be20-34c0-b1dd-f1467e13d365 | -15.33085 | -43.1889 | 2025-10-10 03:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6466fac1-a705-3db9-b55a-fc59a4509452 | -13.84399 | -45.84362 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a5053b4e-68a7-3c38-81d5-f58d80a90ad5 | -13.32365 | -47.74811 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 61de4361-0244-3840-b924-a60c5da5d97e | -17.99405 | -44.9676 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00c205c4-1050-3f46-aadd-ac1b566345ad | -19.83648 | -41.80711 | 2025-10-10 03:42:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26b22c20-8ddc-3ff2-a3d6-74c0018df8b5 | -14.92882 | -46.78721 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a238d5c6-bab5-3458-bb06-3840ff33064d | -19.10094 | -43.88357 | 2025-10-10 03:42:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49b20ece-57f8-3ecb-b681-35b2bba0ffdd | -18.54232 | -45.06673 | 2025-10-10 03:42:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15e7e2eb-f0c5-32a6-8213-87ff41a7ef37 | -15.38482 | -47.29459 | 2025-10-10 03:42:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3132f5a9-523a-30c6-902d-368be4814c28 | -15.61955 | -45.25624 | 2025-10-10 03:42:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7dc552de-41ed-36a8-9700-bba190553275 | -13.34194 | -47.75715 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17cc2a05-4b78-3d2d-a878-87470041d88c | -14.9383 | -46.77173 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ebe610b7-97f1-39d3-88d2-e5cb9b6ed15e | -14.26972 | -45.89724 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| adc50674-f2d9-378b-b593-67efcbbb7d20 | -15.09179 | -46.59524 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e05f0e19-0c2f-35d5-b306-8fce8df6e6a9 | -15.62024 | -45.25282 | 2025-10-10 03:42:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09ac615d-96dd-3769-9ab3-80f9bb20bca3 | -14.2702 | -45.89902 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae34ceab-5ec7-3f34-a319-dd10c4b30273 | -13.83581 | -45.88571 | 2025-10-10 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76ad44e4-78dc-39de-8dc6-62b6ea4c9cd9 | -17.65961 | -44.44792 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72ade313-74a5-369f-a946-7fe11df1af0b | -17.93461 | -45.02868 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4375f5be-51a4-3d66-9c74-769258c19af6 | -14.57001 | -47.46586 | 2025-10-10 03:42:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7f97dfb-154c-3695-9d67-a118a99ece22 | -13.84186 | -45.82756 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d060eac-bcb3-3be8-9132-469ea633db2b | -14.26894 | -45.90113 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72cc36e4-af85-3c86-b6e6-0ee315961b71 | -14.4484 | -47.98066 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4ed6bfa-e0a6-3dc2-9552-95af907b776b | -14.98599 | -47.20261 | 2025-10-10 03:42:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dc2524c7-4848-3f9e-ab9f-50732212e5f4 | -13.88027 | -44.25034 | 2025-10-10 03:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a31e56f-7f32-38d6-b4b5-a1b7062fab50 | -14.11716 | -42.76999 | 2025-10-10 03:42:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb077d24-9638-39b8-95b7-3e57d0d40521 | -13.84644 | -45.86124 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 22f05772-f0b7-300a-a6a0-f92f580c539b | -18.64417 | -43.94433 | 2025-10-10 03:42:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2a4e128-98fe-3953-8b7d-c51b7abe9b0f | -18.74503 | -48.08158 | 2025-10-10 03:42:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f1c3b48-d054-324e-9d81-b0f9130d07f9 | -13.27285 | -48.02514 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11f4c106-b679-3702-a848-8e123de95985 | -16.29782 | -47.15193 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66092bb3-106f-35c8-91aa-fac87daf8808 | -13.28977 | -48.49066 | 2025-10-10 03:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f099ab90-ec9a-3a1e-a957-561e8379a533 | -14.42908 | -48.00835 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b73b652e-c4b6-3813-8424-dd65f22982c5 | -14.2677 | -45.88249 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5825d8a7-4a04-3979-91dd-04dc8736c64c | -18.64536 | -43.9385 | 2025-10-10 03:42:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f584df05-7ce6-39b9-a8ee-a23f3e13fdd2 | -18.53616 | -45.07155 | 2025-10-10 03:42:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21cd3eb0-7645-351e-8cb9-868eef9215e3 | -15.32985 | -43.19397 | 2025-10-10 03:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 080c4ebe-5f77-30ac-88ce-29b57ef5a460 | -13.38634 | -44.23236 | 2025-10-10 03:42:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4218dc0b-f5b5-369f-b3d3-cbb102ec38de | -16.27614 | -47.16646 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b7bf24b-cf66-3d4a-b494-b19ef5c12f0b | -14.94861 | -46.24218 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68a71462-c511-3c59-816e-323a75635574 | -16.05122 | -48.07504 | 2025-10-10 03:42:00 | NPP-375D | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c019a4e-546d-3ad6-8489-448f5ffcef5d | -13.32471 | -47.74321 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7cc70360-0cd1-3e16-bac9-45ecab4c9979 | -17.93555 | -45.0241 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| acfcf54a-8799-3acf-a852-8c9ecc2715ce | -15.28375 | -46.15467 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6bfe7eb-71b5-3189-b845-43c5975cbe6e | -15.24449 | -46.37693 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b3b7e23-e487-390d-9d0e-3c26293f99fa | -15.33453 | -43.19491 | 2025-10-10 03:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0ae5eb52-b58b-3c75-ac48-34dac3035942 | -13.23073 | -47.61605 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a980895e-477b-3c24-8151-d2224443b756 | -13.84078 | -45.86161 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7db0d9f2-535d-3f8e-a414-db3af5310b4f | -13.84416 | -45.84518 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 350ccdff-0afb-3ced-a237-00888d3ea8c9 | -14.73082 | -47.44795 | 2025-10-10 03:42:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1dd9c79-6edc-33b3-9400-217b372c555e | -15.9148 | -43.29704 | 2025-10-10 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf689d4-b61a-30e8-8fd6-8d42cdca4e5d | -15.09195 | -46.61604 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8fef531-0db6-3f77-b952-2803778bf220 | -14.97431 | -41.68478 | 2025-10-10 03:42:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 02e7f6f7-78af-3e30-bad9-8acba29b31cb | -17.66334 | -44.45461 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81b8d3d5-324d-3656-a1ee-9e34176f6eb6 | -14.97073 | -41.68029 | 2025-10-10 03:42:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 029a05ee-631f-3884-a169-68fbf317b189 | -14.92976 | -46.78278 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c93d1c4a-7b1b-3834-af5c-cb3b78c3154b | -18.06987 | -44.97579 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc9cb922-652b-3e4d-935f-c86961289854 | -15.08622 | -46.61425 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0196f00-0822-3449-b059-b0b6253f7401 | -15.09309 | -46.61871 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 431d7353-c873-3a13-8a91-c6eba084874f | -14.67269 | -48.06301 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 803af183-528d-3ac2-8d6c-033330aca20b | -13.31858 | -47.74049 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69435bf0-be15-3d9e-9fa1-b4eeeb33a668 | -14.44246 | -47.97687 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6e26277-efc5-3df8-b9fd-76c40768f128 | -15.91586 | -43.29156 | 2025-10-10 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62b4d689-d1f9-396e-b12d-49d97394ea82 | -14.57111 | -47.46061 | 2025-10-10 03:42:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20e43c8e-9de9-377d-8a33-3aa73aa108b5 | -15.09102 | -46.62043 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8513fc8d-b927-39a9-ad6c-e3849e78ebee | -14.38694 | -46.00076 | 2025-10-10 03:42:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5802b04-8546-371d-a063-1c316214016f | -15.08011 | -46.59274 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39ae582e-5c56-3669-b8c9-d067ff9ccc68 | -16.29686 | -47.15644 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75cdef48-68d4-332b-81ce-0304223025f1 | -15.07902 | -46.59067 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baa1ea6b-ada6-33bd-a328-e5c085c488c3 | -13.31107 | -47.7442 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 199c7ac8-3967-3c45-9605-bda8405e2594 | -15.74736 | -48.99439 | 2025-10-10 03:42:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ec46d16-bec5-3afa-936c-3abb4b27b74b | -17.3907 | -46.87458 | 2025-10-10 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7626379a-e47f-399b-be4e-652724441caa | -14.26785 | -45.87695 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 020624d4-be3c-3c7b-9fab-212e88a6c3a6 | -17.66821 | -44.45562 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7143c9f4-02e0-3a80-a160-954055486b0f | -15.09288 | -46.61166 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 686e9848-2a51-34fd-bd34-22fa3061ebfa | -15.39977 | -48.03551 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1101504e-37cf-3015-ab97-99287320098c | -15.0058 | -46.28369 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a6a5c63-d0cd-3fd4-8ebc-2e3ae25d654a | -13.84808 | -45.85294 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 0fe5d3e1-83fd-3a8c-88a7-5a32185c6e99 | -17.38947 | -46.87512 | 2025-10-10 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95fa59b7-becc-3a5b-b576-58153cb8c81d | -15.23701 | -46.3842 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6559e421-3375-3530-a21b-fc8178cdec76 | -17.21783 | -47.65824 | 2025-10-10 03:42:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8efe37c0-25a0-3863-96b6-68cb8bb0cf73 | -17.92964 | -45.02738 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5405ecb2-59bb-3e36-b6f4-1e226445e793 | -13.36302 | -47.75311 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f23d332e-d8d3-3d71-8210-7f8ac7c4bd5b | -13.83748 | -45.81666 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76924254-3ffd-3f0e-ae69-656e8bee8a43 | -13.34907 | -47.75581 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdeb12ee-ab57-3f54-b08e-00e34fe30552 | -14.94301 | -46.7664 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa46e82d-b969-315d-90df-bc0431f8a5ce | -14.92958 | -46.77173 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8592fd7-fc24-3ecd-a39b-8466adf52a63 | -13.32803 | -48.48177 | 2025-10-10 03:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b12f8517-d456-39c6-b581-f8141a41150a | -13.8465 | -45.86272 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95bc1366-583f-3f37-bfc3-7083e47bbd69 | -14.88287 | -48.2406 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c56dcb6b-fac5-3da7-bb45-9d668313d702 | -18.02133 | -45.01367 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| eb4d554d-cecf-3c68-9d60-a22945797204 | -14.94215 | -46.77063 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 77501195-21fd-3b90-bfe0-061f59ea5e1d | -13.34977 | -47.75204 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9afbee6-5bb3-319c-8582-77c0f2c07b4f | -14.8861 | -48.22576 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2f927fc-7da6-3dfd-8c1f-13acc264aad9 | -13.29024 | -48.00732 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46add798-8e7c-3116-ad69-e21dd58ad5d2 | -14.86071 | -48.46789 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93cb5239-2b0f-3c5e-8d8b-981b329ad047 | -14.68623 | -48.06213 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0dd2b600-3608-39b6-bed0-bc815d84cbcd | -13.23071 | -47.6161 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3607fd8-2a57-3fd8-ae44-32507c981635 | -14.87896 | -48.22749 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README17.md)
