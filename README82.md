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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa1ae5e1-1034-3733-a319-0661f6bbd610 | -14.88757 | -48.12953 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d58358b4-c345-3614-ab26-9f6c88cc31ed | -14.9233 | -47.22644 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2353e2b0-bd40-3256-9292-ade14d534219 | -15.16791 | -43.62725 | 2025-10-02 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 31e8303f-26d7-3c31-b873-44d1a24b3ee3 | -14.89984 | -48.32547 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8d79a84-a71e-379e-919a-7055dbf49063 | -14.04212 | -48.00149 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9ea89693-07f0-38ab-9191-693be516b70d | -15.83261 | -42.6226 | 2025-10-02 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 19c88735-c16b-308b-a1d2-b98751c254ad | -15.23328 | -50.12099 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b5fef0cf-5d2d-39cd-b880-ad9cb85ea0f0 | -12.76391 | -48.25142 | 2025-10-02 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e8952bf-257e-3f6f-afaf-816bb5d49507 | -12.64308 | -46.95739 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d983bce-e4a9-3370-99c0-eec30c34ceb1 | -17.39641 | -47.16824 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07839408-5896-390d-8a0a-4eba1a69659c | -14.86496 | -48.29442 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c74a79d0-5167-30b9-b271-87ea7b69e99d | -15.2546 | -49.28598 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 775ba5d4-5daa-325d-9af5-e4b6c7920e8a | -14.79652 | -44.88961 | 2025-10-02 04:32:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb35e215-e15c-3f2c-9c7b-012a9ae876e9 | -14.41669 | -46.1345 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cb8490b-cb3d-33bc-9d4e-a846893f6961 | -13.42259 | -47.79122 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f66504b-b8f3-35ef-be12-111a694137d9 | -16.01319 | -50.91314 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09da485a-4478-36b7-8ba5-b32886417fdd | -14.61352 | -48.23473 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1caf8b2-6482-388b-89d9-f958daa7a60f | -14.41323 | -46.11037 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc362c57-7117-3f46-a421-f17f8a6c61a2 | -14.98719 | -46.90542 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59cab80d-8795-3d6f-8ec0-2c5a22483a98 | -12.77598 | -44.9077 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 877c0c99-6988-3873-b001-4e8c43009040 | -14.31008 | -45.88881 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01ceea2c-0286-38f6-8c50-d70288edd31e | -12.8682 | -47.01119 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba0bb206-ec1c-3b50-aba6-9059220399b8 | -13.5548 | -47.28609 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1785c765-e6d1-3d46-9546-cb9ef438fc7d | -11.82416 | -48.07903 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4fbc254-546a-3183-9095-82fd1b6e25f7 | -15.55815 | -48.18098 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38306f30-449e-31ae-ac48-230cdb5074fd | -15.20662 | -48.16374 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53e89f27-51cd-30b3-b1d8-37ba2d912823 | -12.25641 | -47.82635 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbb8a7a1-7d4a-3e50-b827-cd8f0dfe3935 | -13.68887 | -48.64592 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a831f139-a8c1-30d7-9765-45a3b6a5458e | -15.25283 | -49.29694 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a03d1d86-39ee-3104-abd7-82ef27e9891f | -14.54731 | -48.22698 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc45c076-ff94-3a1a-a57d-e5e19de59365 | -13.46175 | -47.23462 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 627f0888-47d3-3c32-8982-2faafc8084ec | -13.95149 | -48.09968 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6205d98b-6633-3e49-9cd8-b3b89a864f28 | -15.29022 | -46.39076 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b4fcbcd-8a18-3586-8dc2-1928569773a6 | -13.31398 | -47.85733 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b2eb6ae-5409-3458-a195-8104a8bf56cb | -14.65063 | -48.25918 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d575d84-c99c-3a29-8778-cdcea9728c65 | -13.04971 | -47.05877 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e80f75a-a338-3546-870f-110991ca0975 | -14.91027 | -47.83229 | 2025-10-02 04:32:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6b47261-f141-3af9-bf72-07f73d0709ea | -17.9542 | -45.03589 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70477f8a-f39c-3699-a089-07d40c5afbaa | -13.68135 | -48.07703 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc9d6788-ec0f-310f-9503-1f252b0cb265 | -11.62291 | -52.24789 | 2025-10-02 04:32:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b39db37a-274c-3100-87bc-0172bb761c10 | -17.51395 | -43.48714 | 2025-10-02 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e095faad-24ea-333b-bf37-bd0917482128 | -15.24003 | -48.7241 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f0b708c-c9c6-3a19-9dc3-58b61853b5b9 | -11.98086 | -51.4023 | 2025-10-02 04:32:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 249de2ab-bcc1-3254-8dd9-476d4a003626 | -14.47399 | -48.43085 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 54089f34-dae5-3491-a2b5-76787a6fc8e7 | -15.21885 | -47.16781 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 207f2183-0a44-3a2e-9a74-9ff27a424f66 | -15.84045 | -46.24262 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfa7e1e4-782b-3e82-8fde-8d1cd62d4856 | -13.01636 | -45.22311 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6219abec-4174-3702-9694-cb67af2381b3 | -14.31592 | -45.99322 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 91a131e4-8405-365c-be4e-72ace0cae8e0 | -13.81316 | -47.53675 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98d48cc7-14c6-3b74-a9eb-502341f1f17c | -17.32809 | -49.38876 | 2025-10-02 04:32:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a425cb0a-5d60-3af5-9b40-9cef69b8ecbf | -15.22726 | -50.1203 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9728261b-f566-3ea1-9945-606b8ee9ea24 | -15.40894 | -47.06608 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3df4d1a-20b8-345b-88ac-18be7509b9a0 | -14.98407 | -46.92065 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e6815ff-e174-36ce-88f9-e02def137f52 | -12.27798 | -45.37572 | 2025-10-02 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8d75c1d-4496-3a85-9510-e69b58a66349 | -16.0484 | -45.72353 | 2025-10-02 04:32:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 846d2d83-f909-3db4-b22e-83a35781e881 | -15.86409 | -48.1318 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b65ef03-606f-323c-b0cc-26041c3e7a35 | -12.18094 | -46.60458 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01518ee4-56eb-31af-99f3-62324d4bdbd9 | -14.41381 | -46.13013 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93489ae2-5e02-3427-bc99-7efd918a2949 | -12.49132 | -54.40184 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1797c33-3c03-3672-abd1-807996d4522f | -16.28321 | -42.54912 | 2025-10-02 04:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ca3a8f8-2e9b-36fd-b437-2d12ec072b82 | -12.21128 | -47.79304 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30173c8e-9f24-36c6-8758-813a62be4317 | -13.23582 | -47.34106 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7357ff8-5242-3171-be61-09e2847975b5 | -15.22295 | -50.10373 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62a0867a-8e61-32c7-9d86-26b6ac50d198 | -16.04127 | -50.85319 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc1628e2-8df5-3bca-9870-2d1b31c8e2d0 | -13.52693 | -47.26699 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 640b3eae-41a9-3ae1-9992-9d19cd413281 | -12.91063 | -47.16857 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3afd8d2-39e0-3b20-aefd-571823785a82 | -15.34828 | -47.07162 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a1baaf6-a581-3deb-8e9b-f5dc445fc1c5 | -12.02352 | -46.63541 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2915da9-2500-3343-8103-eb98cbc3f7d8 | -14.31823 | -46.0015 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6028d10d-1109-3ca4-8fd2-fdaa15501095 | -19.9498 | -43.66918 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4ef1d98-bc5a-3330-839a-dee6a3f723de | -14.92274 | -47.2301 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 860d360c-8b8a-3198-8bb5-794830df82d2 | -13.32312 | -47.23119 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e0aef93-a9d0-39f5-936e-2c2e2aa259d9 | -11.58685 | -50.16727 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77b62c8f-9d66-36b0-9fad-5480db2adde4 | -13.42868 | -47.79586 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d9bcdff2-d8c7-3451-960c-6b59eb5067dd | -13.81038 | -47.53264 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e0178f5-fd1a-3596-b7ff-9d79507bf852 | -14.98439 | -46.92401 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 363d168e-c643-3e40-91ee-23d375b1ccff | -15.79819 | -43.73007 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6557369-b8ca-306f-bd1d-82d670ddf303 | -13.6974 | -48.61414 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87c39d0c-0e1d-3e95-bcd9-f41b895f28a3 | -13.37549 | -47.29084 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bfba9f3-f0a0-3b5c-b65e-6aa4dd0897b4 | -13.0657 | -49.17096 | 2025-10-02 04:32:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f6a63fb-4652-3daa-82df-dc1fc073b864 | -13.52748 | -47.26344 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 926a0ab7-6ee7-3174-8c58-aa901371c171 | -19.71575 | -45.87901 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7121ee1-76d7-3708-b4d9-b5bac670f892 | -12.57264 | -49.89154 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39f13ec1-641c-34e7-9ef3-5ad1a64a0f76 | -13.08319 | -47.08618 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 742958e3-e009-3708-b61f-44b4970d68d0 | -17.95714 | -45.03923 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4841dd7-7b3e-3354-9987-53d8be144d6e | -13.18832 | -47.84 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aff0cb4e-0d6a-3274-990c-fe7390a31585 | -14.41495 | -46.12248 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ef0e8d8-183a-3927-a8c9-a09382c49b73 | -16.36816 | -47.05475 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2131f124-e5b6-36e3-8601-6e410b00aa75 | -13.80421 | -47.53491 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61c792e3-da68-3198-913f-e0c14baa59af | -14.02439 | -47.98395 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56d526c0-f577-3130-8e06-9f834b936237 | -13.66756 | -48.03466 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9f94417-49c1-31c1-bd5e-8fa6cf1e33d6 | -12.57199 | -49.89542 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c04fe8d-b346-3051-8edb-bc5d2ac4a51d | -16.0624 | -51.0084 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d895fd7a-481c-35b9-91b9-cf971320750b | -14.79656 | -46.98863 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2727502a-33d6-3b2e-9333-1bff621eae6b | -12.40924 | -47.49923 | 2025-10-02 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39752384-5f97-3d66-835a-27a5ae028181 | -13.30682 | -47.85977 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3cfa8149-fb74-365d-bd38-dc21f7176307 | -14.58609 | -48.32167 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b22093f9-bd2b-3b7e-8b88-90e4c036cb53 | -15.25736 | -49.29021 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d20b31c-4091-334d-bb68-9f2d1701d740 | -13.24416 | -47.33141 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04e618f6-7922-3fe4-b779-51af867a1e9c | -13.31343 | -47.86089 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README83.md)
