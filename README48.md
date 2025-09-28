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
| 0bc01dc2-8574-332f-92ae-88b5d7566508 | -11.52412 | -54.31171 | 2025-09-28 04:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac4eaf37-cfc0-327e-9fbf-3331db7e6ac3 | -11.8564 | -48.24524 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a69463a-ba91-32b1-8afe-0fcb398f840a | -15.08938 | -48.33433 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34af79e6-a0ef-35b5-8c18-dcfaaa4fd5cc | -14.83527 | -45.57179 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 892fd2ed-2245-3f81-ade0-0ee6b0000774 | -15.2955 | -49.48433 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e159bee-b00a-3d9e-ae7f-49bdc4b565f9 | -13.62101 | -48.07139 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f95d563b-5380-38b8-94b3-efa21db298f8 | -14.71072 | -45.2053 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caa3e044-3f05-3cd9-8216-3b9037f4f922 | -11.67202 | -44.46289 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bb6354b-1668-3d92-836c-2586d51b615d | -15.87535 | -46.22804 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39de397d-3496-3123-b1c7-702eeac201f3 | -11.98741 | -47.88397 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26f4a680-8a12-350c-b444-3d0958ec312d | -13.61856 | -47.31645 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ebd65373-75ee-301e-ba59-aedc0217af28 | -12.00536 | -47.88671 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ccb2fd9-d426-3262-ab0f-694d3df488e0 | -11.7994 | -44.91365 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e04df65b-caaa-3736-9ff1-e4353de2d07f | -15.6221 | -48.35487 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db136b09-432c-36ba-b327-2cf7e8ba6662 | -16.40273 | -43.72206 | 2025-09-28 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de1c8276-397e-307b-922b-167e4c5ee11d | -10.91157 | -45.74288 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f79df79-d17a-3314-b67d-caff804cc4f7 | -15.08631 | -48.32658 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01f15a36-6b3f-3ad8-b5f7-7e4323c0a5f4 | -11.15406 | -54.31107 | 2025-09-28 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ebe3987-3d9f-392f-a6fc-fd48d22ab327 | -11.44314 | -45.00386 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d02806e9-42b3-31b1-9a5b-3a2bbb865e9f | -15.19831 | -48.47583 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bddc52a7-5f8e-3797-a066-c0816fb2f83c | -12.94902 | -45.15407 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 19212aba-2b88-37c8-ae5e-6efdf84c6c42 | -15.583 | -42.40737 | 2025-09-28 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27c1d896-f9d6-3828-80f1-6d846a0ba0ce | -15.8112 | -46.04112 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a2ace76-4cbb-3a54-ba58-154c3f3ad5e0 | -11.6179 | -52.84903 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8675554f-6d65-3398-a367-4d4c7893570e | -14.322 | -52.92411 | 2025-09-28 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e68a0e0-d569-39b1-b8d7-ef51c4386ac2 | -11.97601 | -47.08051 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed0fccef-65eb-3590-b5de-c5123d365f09 | -13.7854 | -47.89385 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 798ad6b8-a747-3122-80e7-0d2cca989df2 | -12.89985 | -45.173 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8d9bab15-cc5d-3bf2-af20-714d1a7beae8 | -11.35508 | -45.00036 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed85d3ab-1327-3131-b1ef-2f748671fa92 | -11.68733 | -44.43915 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e05a5d9-a9a7-3c1f-913a-847beeedc440 | -13.33748 | -47.28966 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af2dc5ef-7ab6-3b40-9a52-9d8fe3aab258 | -11.9696 | -48.0076 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed8038ea-5eba-3e80-84b3-fd69f560deb5 | -11.60033 | -44.35928 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5734fab-5c48-3dec-ac66-64d6c1f58f0f | -11.54124 | -47.04049 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6a470cb-18ed-3f33-ba44-036489309306 | -12.017 | -47.04699 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4485fea8-cb07-3c94-9f7c-4d36a30564b7 | -13.59049 | -47.30441 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93fd3029-f830-34db-888a-b95469f6cb79 | -13.78051 | -47.87205 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e8d8418-f2d3-3571-81cc-4d114cd47aa5 | -13.59931 | -47.32735 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 19cccd78-4938-35ac-a83a-d6b049794d6b | -11.09696 | -54.27955 | 2025-09-28 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87d5404f-c294-3591-8073-7b2ebbc92264 | -13.61359 | -47.3201 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7934bba9-a4b7-30c0-9f41-2aec703e34ca | -13.3738 | -47.92248 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3aa72ef3-d8c3-3ddf-9ebc-c31fbaa2f7a3 | -14.53604 | -48.41577 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e562594-1278-32c3-b36f-7480cafffb99 | -11.35054 | -45.00431 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92bfd177-ac08-326a-a63a-517fb89abf7b | -11.70188 | -44.41973 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2245c945-7f64-382a-ae46-9f94c0495933 | -14.71967 | -45.15366 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c31024bd-4d84-37a8-9778-1944431c6ff7 | -11.99518 | -47.04708 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a6b29ee-4297-3597-b75d-29045908b0ce | -11.61998 | -44.41971 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 806122ef-a4c8-305c-8665-345df426271a | -15.43977 | -48.21737 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36edd57a-db0f-3ee5-91b9-28466d62bb93 | -11.97356 | -46.58748 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef2f4079-0ebe-3deb-beb8-728dfcecdb7a | -11.99011 | -47.99706 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d181f107-05e6-37ae-babf-01ddbd9086ce | -11.44766 | -45.00003 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d899eaef-878a-3a5f-977e-287c09ccd852 | -13.24973 | -44.11152 | 2025-09-28 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e26652e-fcc5-3e28-96aa-fa5f5dc78a09 | -11.98392 | -46.60066 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c3b9e1f-c637-3d58-bd0a-29582d473ce7 | -12.95279 | -46.38165 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 22c53e3e-e499-3604-8f53-fb75b1126d25 | -11.43939 | -45.00317 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 282f1b2c-0f61-3bce-9e93-104a0eb21624 | -15.62172 | -46.25998 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7795e25-e7a5-3960-813f-8682f71ef2e8 | -21.84977 | -50.55663 | 2025-09-28 04:08:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| b0cfd441-36bb-3b75-bc73-039f89c3fed6 | -17.72802 | -46.70235 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fdcd001-32ea-33ff-a215-50b245bcd393 | -20.12495 | -41.71825 | 2025-09-28 04:08:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9f0e1cfa-cb51-33ae-aa7a-bf57bb3f9e42 | -19.85508 | -42.59321 | 2025-09-28 04:08:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2d67012c-bfa2-318b-adbb-e1993a3ff06a | -21.35785 | -45.78595 | 2025-09-28 04:08:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a298584d-faba-3d93-b68d-fa5ad600ee38 | -20.41079 | -46.47394 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92f52f30-1bbd-3c43-b6eb-bd489558f542 | -19.31594 | -43.81563 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e15475bf-c601-3807-990f-1c94092c67ce | -20.69775 | -50.71313 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e93615cb-5503-3269-84a6-53af6b0fcb1e | -17.73554 | -46.70399 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1bf9760-08bf-3262-b830-20c799e9d764 | -21.09825 | -46.35855 | 2025-09-28 04:08:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d57da1ff-aadb-3125-9cd0-a75f25ac9285 | -19.94405 | -41.64667 | 2025-09-28 04:08:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a32342f3-ab9e-33a8-893c-4ea847d914ed | -18.20413 | -53.32605 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 466c6f29-ef20-3823-919e-b508aa384585 | -19.49532 | -44.25562 | 2025-09-28 04:08:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 703c8751-c576-3648-9c31-6ddd15081887 | -16.59292 | -50.66374 | 2025-09-28 04:08:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fc12992e-9ede-3475-b147-7b8230c9c991 | -22.06005 | -43.01776 | 2025-09-28 04:08:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f5c083e1-83f2-3102-9004-b0e3863e91be | -19.53423 | -45.03012 | 2025-09-28 04:08:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee584f00-043c-35ce-a87a-0d9f15283a5e | -19.87296 | -43.8032 | 2025-09-28 04:08:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 271e33c8-fdcc-3917-9a28-7af4c51f2578 | -19.94688 | -41.65103 | 2025-09-28 04:08:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 57d16c02-2930-3161-a940-9f35fd946e8c | -18.17379 | -53.32293 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7d8cb75-e6f4-36db-806f-33ac6a87812f | -21.44699 | -44.90473 | 2025-09-28 04:08:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 58d0a9fb-f0cd-35eb-998e-76cc7dcea142 | -18.17821 | -53.32992 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1fce5928-6243-3436-ba83-44fbdf553efd | -20.92247 | -43.09383 | 2025-09-28 04:08:00 | NPP-375D | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 84bbcd7c-316e-37c7-8d80-d6efd247c146 | -18.20338 | -53.32291 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89274e3a-461b-3a0b-811b-383ad0099ea9 | -19.96183 | -41.4324 | 2025-09-28 04:08:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b78fdb2-9c52-367d-8214-2d4f11af29c3 | -22.87183 | -46.40081 | 2025-09-28 04:08:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cff03d8d-71a8-3296-a690-aa9bac898ce6 | -18.06493 | -42.3939 | 2025-09-28 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 523f8953-4d63-38fc-b734-c25018b3976a | -22.94423 | -49.8774 | 2025-09-28 04:08:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 244cb949-a9aa-30ab-a917-88ab6e36c569 | -16.96908 | -53.69681 | 2025-09-28 04:08:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 10b20a43-a03a-3e7d-8633-02e4f9b320a9 | -21.11844 | -42.90281 | 2025-09-28 04:08:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2afe485e-031e-3503-9dfb-3d21907c1a59 | -19.31654 | -43.81192 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0a6be29-aeb3-3a17-90f1-84b74f5de564 | -19.66064 | -45.9744 | 2025-09-28 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1541bd67-3a4f-31b4-9e2d-d9730ff71833 | -20.44667 | -41.26009 | 2025-09-28 04:08:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d6af83ac-0fff-3bd6-be21-2b50f3239a3b | -23.52017 | -46.97639 | 2025-09-28 04:08:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| f1f2ffdd-7dff-33c1-abb3-22101299eb3f | -21.96634 | -44.23031 | 2025-09-28 04:08:00 | NPP-375D | BOM JARDIM DE MINAS | MINAS GERAIS | Brasil | 3107505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 03c3b56f-4f3f-326f-b2b4-4a568ce39a3e | -19.9632 | -41.72787 | 2025-09-28 04:08:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e4e7e5d8-0578-3f0c-bcfa-ffc52df86491 | -22.3428 | -41.78675 | 2025-09-28 04:08:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ef9ee30b-0637-355f-a982-eb011b62d0aa | -19.98343 | -41.45191 | 2025-09-28 04:08:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5bf3e2cb-2947-35a1-8e62-27e2436fdb03 | -19.9598 | -41.72732 | 2025-09-28 04:08:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd1ad178-17b4-32ff-85f1-4387b9ed1657 | -20.41513 | -46.47036 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4bf4d9c-639e-3c64-951d-1bfbcfa75817 | -15.95489 | -50.42057 | 2025-09-28 04:08:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88494432-dbf2-3aae-8771-16d69537f73f | -19.32516 | -44.16647 | 2025-09-28 04:08:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e43b5c91-31f0-382a-b6b1-b4ef8601b42d | -21.40062 | -40.99931 | 2025-09-28 04:08:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1181fbfe-262d-3dc1-8024-c03daf6766ee | -23.44207 | -46.70001 | 2025-09-28 04:08:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d2222cdf-1c1a-3d25-85bd-bd04daf6bfa8 | -20.69518 | -50.71914 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README49.md)
