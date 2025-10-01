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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b47ab0a-5d47-3753-a244-fc30d2308d64 | -15.04205 | -48.06561 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3533843-2074-3d30-ad05-00b5582b1a73 | -10.82682 | -47.95717 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6fcd78a5-4714-3bf1-aaec-f6160e8bad7d | -12.87984 | -46.77059 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c192a824-06d5-37ad-9be6-770acb88218f | -13.45185 | -47.24118 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14ea97ac-36d2-3e87-ac9d-dd9be4f10f3e | -15.27283 | -49.28898 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0fe36f4-82a0-3589-b6f3-29d5cc43d829 | -12.46184 | -50.24645 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 733f31f5-43fe-33d6-ac61-f9d04597ce40 | -14.9666 | -46.8774 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a02dbf8-a81e-31db-875d-2f21bcac8a62 | -14.50376 | -48.43608 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c9f17ed-0774-3cb1-afc4-a41acc1d7e56 | -10.11892 | -45.67371 | 2025-10-01 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0fab2e66-f75d-341a-b11a-86253cf6571e | -16.08537 | -51.04587 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b785ced-cae8-30e7-8022-0e6edaae78af | -12.66282 | -46.87256 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 975a1568-be1b-39aa-aa33-4426953a2d01 | -12.7563 | -46.88463 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ca4efaf-d77e-3ca5-976b-84fe0041c287 | -11.37085 | -45.06058 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1e21549-db8d-3ea8-b2c4-c1348873dde6 | -14.79407 | -45.79439 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dffe4617-45a7-30c5-aedf-45aa214c753f | -11.82973 | -44.97243 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6663cd32-08e8-3c01-b612-bbd204a7ecdb | -13.84704 | -47.93605 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2765827c-119f-302a-b09c-eb9a70f35d6c | -10.07147 | -50.27048 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e84b4378-526f-371c-a7f8-7f80d76f707b | -16.19948 | -50.00009 | 2025-10-01 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d8e25137-2656-370a-93d1-248698f0d34f | -11.45321 | -43.51049 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e975adb2-69ef-37b2-baab-3629f8fbdd1f | -13.33046 | -47.86734 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1dfd02ee-9eb5-3a9d-a538-e403726c28d9 | -12.37954 | -50.20436 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4c87a0a-eac7-3802-b2eb-b8ae5cee719b | -13.17024 | -47.78842 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 578e23ed-0e6e-3ea1-9d19-ed00e56a3ee1 | -14.06253 | -44.36991 | 2025-10-01 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43cdb3bf-14ec-3217-a1b5-dd12e285cdf8 | -13.31211 | -47.22123 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41304f85-7e9c-377a-a976-6d3bdf953d38 | -9.58434 | -54.59847 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 314ded28-abde-3b09-9918-ebafcd0bb34c | -12.70004 | -48.56235 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c4a7536-d235-3360-941f-b628b6b23c4d | -14.61528 | -48.31613 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60aa125a-279f-3547-ad30-403ee49a50d2 | -14.35647 | -45.9221 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e86be055-1397-3b28-b629-0dcf33b62ef5 | -11.8436 | -44.97095 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| acda195e-fa5a-3e21-9b45-bf452a7d75df | -10.70844 | -47.9929 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da3fbbc-b8bf-3ced-b584-3e0dcadc8bad | -14.67495 | -45.29974 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 056ec920-651c-3d4d-8ab5-77052297ea69 | -11.83972 | -44.97403 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55efd884-e4a5-3215-862e-fc8368bc33fd | -13.23125 | -48.45205 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe387d79-2512-3f5d-8b9a-d2fa2c182020 | -14.99114 | -46.95791 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe1e5d8b-7399-3e52-bedd-c2fefff04bd6 | -13.32685 | -48.14613 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1332c07a-5667-3e0d-b3d6-dbb95735eadc | -15.28378 | -56.78744 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c301f211-0eb0-3985-9158-b22c88002f1c | -15.66484 | -45.24079 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de777007-b604-3380-8954-b9f7662e4205 | -9.32321 | -50.62433 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6254b60-3fc9-3fe6-9c5e-983ec5423daa | -10.90753 | -46.56579 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 311f1f64-95b3-3906-b101-11c1c6c6751f | -16.76299 | -51.33781 | 2025-10-01 04:21:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d46a37ae-1b8e-3736-a9e0-678563a760df | -14.94979 | -47.51828 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fad3097c-7628-35e6-a822-8ce435b85da1 | -15.2465 | -49.72595 | 2025-10-01 04:21:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f13cafd-b15a-3bdc-8787-8b1ad8f86df9 | -14.36084 | -47.13342 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b728a8f3-4e9d-36f6-a165-bb3861f5615e | -13.78438 | -48.01239 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1df46fa-acc0-3c19-8bd9-dac972d07e50 | -14.7913 | -45.79025 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d36beb88-c466-3302-867f-af47eb647891 | -14.0474 | -44.82454 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 27e55223-4a5b-3493-881b-4fe8f1046203 | -13.56011 | -48.20796 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d404198c-29f6-378a-b4a5-70c8bf29883f | -13.70271 | -48.6415 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce662639-e9f0-34a4-8206-d3f387fde097 | -12.77347 | -46.86203 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dbd21c78-1c14-34f0-af78-57fd428b9eaa | -13.73969 | -48.69577 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24f0f985-ce60-361e-9f54-9dbd549ad699 | -14.14642 | -49.20213 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daa09069-2786-31a0-85f5-0de0e4f52c1e | -10.82619 | -47.96106 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8980d0c-c1ee-3ec7-9447-a5ae4856003a | -13.71171 | -48.65112 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a8f39cb-ddae-3963-84cd-972a1801889e | -14.51389 | -48.4804 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2f7ce0c1-e394-3364-9aa5-05e95e5ce8e9 | -11.94518 | -47.06071 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16e88335-5ffc-3fb3-b74e-51434e1ec662 | -14.90197 | -48.10902 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be6d2a87-d57f-330e-a1b7-4927362958a3 | -13.93924 | -48.10245 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40ebfea6-d6b4-3c18-aafe-c2b1492ad7b4 | -14.55607 | -48.24527 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0934a501-b562-3168-8729-5cf3828f861f | -15.63809 | -46.25401 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 333b8d55-a211-311e-8451-d23cd41bed77 | -15.45187 | -48.57447 | 2025-10-01 04:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64d9326c-6167-3028-b06e-c78b955604bc | -11.43329 | -55.05791 | 2025-10-01 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eb81c65-3090-3ab4-a2d9-45746cb2f853 | -13.24132 | -47.32359 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf35d05a-933d-3b66-bb34-cb8d8186e81f | -14.14263 | -49.1981 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c016ae0-fec1-38ac-94ea-273f245d8000 | -9.5192 | -54.74715 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 846693cf-db97-3153-b990-4ce27f691bcb | -16.22201 | -48.80663 | 2025-10-01 04:21:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc370624-3101-32b1-9ee4-952bb09b85d5 | -11.83904 | -48.06548 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f7e6193d-c487-34e4-9420-517ff0a8f4fe | -14.75861 | -45.75914 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 343917dc-82bc-3b9d-9591-ec527dc7b678 | -17.40196 | -47.16019 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5307c946-be87-3363-b08e-15d8d6e47c31 | -11.72053 | -44.6607 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4dca6450-3d93-3cef-9f03-4430737f8412 | -13.29985 | -47.23389 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5e0bb69-09a0-306f-851a-6aef26a5b80d | -14.79862 | -48.32826 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 92ec3bfe-36f9-33e7-8ad5-b2afc73243bd | -15.82154 | -41.89409 | 2025-10-01 04:21:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9f45afbc-d1a9-3755-bc6b-035b43255c05 | -11.64162 | -47.48598 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0df8c2eb-2028-31cd-8e97-c64329450b33 | -11.39923 | -44.89759 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53ff4e89-d073-32c3-8770-394cc5ea2b3c | -15.1192 | -50.04242 | 2025-10-01 04:21:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c22b90f-fa57-351c-84d8-1ade0f05a4f0 | -12.7984 | -46.89875 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f37a2e3-ced9-36df-9392-9b7ce7d539d3 | -17.40812 | -47.12067 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf3f36f4-8b33-399d-a00c-b87c8824a0f7 | -14.35261 | -45.92512 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89821e52-11c9-302a-b8a4-d9d18411a721 | -13.33191 | -47.83712 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edcdd9ab-2670-3e1c-b608-8a102386b75a | -11.46397 | -45.09681 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6f8884a8-9893-37e6-aced-3096fd1c5c40 | -11.65334 | -47.49903 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ee048614-e7da-3ef6-b2cd-be006a2f4318 | -13.33253 | -47.83335 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a7f7a88-0e06-3a20-96c5-9920d377cc9d | -14.03614 | -47.98636 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30bfa362-1bba-3972-9b30-012db6f56692 | -13.77639 | -47.97619 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ea4b5996-98e6-39e4-9c78-5bfe0f8d317d | -11.46319 | -45.0131 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac301e7d-7caa-3026-8b9e-57b083cdaf36 | -16.76592 | -51.34322 | 2025-10-01 04:21:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| cd1cb3e1-1446-3695-b980-f24c5e433efa | -15.01254 | -46.97249 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4b13eaa-f863-3ab5-b3b0-46434428807d | -11.92733 | -47.89046 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f7dfaff-eae5-3593-9565-3bbc8fc6c056 | -17.38989 | -47.15076 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b44f66c-674e-33d3-988d-da2e869feae8 | -13.56233 | -48.05942 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 916f2421-a89e-3c24-aebe-1979fb91f494 | -14.57674 | -46.36578 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bef19805-9f06-3bf6-a912-56c4d5cc2ef2 | -14.58719 | -46.36386 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 900ef265-9fd8-38b2-883b-091a37921386 | -13.08101 | -47.06964 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bdee447-9026-32ee-a00b-0410052ee907 | -11.4387 | -44.95121 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d4c7667-59da-3990-9c9d-c1f0a6b086cf | -10.17216 | -44.89591 | 2025-10-01 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef8b6d2b-24ff-35a1-b2b6-3ebf0f910ee2 | -15.36037 | -46.11356 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2683601f-c40b-3795-a2a1-d40621d0c66f | -12.66781 | -46.86249 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55ec4c95-eeb3-3cad-9650-f38a4744b7ff | -10.74009 | -45.3811 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 986956c6-7462-306f-a401-8ad1acc8968d | -12.22661 | -43.75634 | 2025-10-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f381ef9-3a70-330b-9c91-af68487fcfa9 | -12.83489 | -47.03244 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README70.md)
