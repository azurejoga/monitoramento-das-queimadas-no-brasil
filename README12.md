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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b42f68a4-ce8e-3b05-be81-f5181202a335 | -19.27448 | -45.06841 | 2025-06-28 04:04:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f6fe79c-4d2e-3411-b415-707dd263a717 | -13.66607 | -43.66497 | 2025-06-28 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 118f9116-9e3c-3397-8380-3634941e2d18 | -17.75493 | -52.43113 | 2025-06-28 04:04:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98b382a0-6652-3fb6-aafc-346d46635778 | -17.68878 | -54.00819 | 2025-06-28 04:04:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d83e66f-93fd-3c6f-b3a9-6648bfa954a2 | -10.83731 | -53.75422 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8066a98e-6ec7-3b54-9793-0703ae0b4e71 | -12.26312 | -46.77111 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a7b16be-09ef-3b82-b1ff-b1ed48913d42 | -12.0364 | -48.75354 | 2025-06-28 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 542f5910-98dd-3cee-9860-573918a56c9a | -19.19892 | -48.40813 | 2025-06-28 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93943196-638a-3d1e-b88b-a27b7784f155 | -16.34989 | -43.69548 | 2025-06-28 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b29f7d17-9d39-33a4-8045-71e94e1aee51 | -15.07804 | -48.9432 | 2025-06-28 04:04:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 271e78ae-f0b1-3a03-bb4f-88435baef0d3 | -19.16555 | -49.13733 | 2025-06-28 04:04:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25fcbc33-7db3-35d8-b5ed-0ce13e82d89b | -10.82962 | -53.75853 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9fdbb390-3cf0-3941-9a27-1720a1b2fc22 | -11.58065 | -52.12206 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8c3901ea-eb39-3534-a5ab-fb42c1d2de86 | -11.05092 | -55.07934 | 2025-06-28 04:04:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bbdb473c-81d6-38c2-a99f-04fb105232fd | -10.84382 | -53.75559 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 350b14b0-c1d8-3734-aa55-0da1ccab7eff | -17.78116 | -42.81016 | 2025-06-28 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07c62b0f-58f4-37be-a604-6fecaf62b40d | -12.20067 | -49.64363 | 2025-06-28 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 074219b1-ae92-341a-ac54-93f08171ac14 | -11.57741 | -52.10794 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35d06a87-c4b8-3e77-8b3d-82cb3c2bacbf | -19.43853 | -44.33909 | 2025-06-28 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a13bfc0e-2ffe-3cd8-b912-232103639fae | -13.57226 | -45.25786 | 2025-06-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d1b9d8e-4810-3345-9e32-3fc6a98d0a88 | -16.2592 | -53.68008 | 2025-06-28 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8edeb5d5-c30b-3aa1-9a79-90909a6953e1 | -13.99919 | -44.03216 | 2025-06-28 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9be67717-7553-3cc6-9725-25da5f66bdce | -14.68999 | -53.39053 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b786346e-4337-31c1-a0d3-799d725f4e89 | -16.42587 | -44.51782 | 2025-06-28 04:04:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bf62d87-b3a0-3162-b711-d3a157abc021 | -19.53949 | -44.0778 | 2025-06-28 04:04:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0071e43e-18e1-3ff9-8cec-fe16263b69b7 | -16.25599 | -53.6819 | 2025-06-28 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b37e3573-437e-3718-aeeb-79db6ad13d58 | -13.99638 | -44.0277 | 2025-06-28 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce321450-1899-3bce-9da4-161548fca1b3 | -14.89224 | -48.40216 | 2025-06-28 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 947227c7-7189-3c6e-95b6-e6a6d07925c1 | -19.51425 | -44.27572 | 2025-06-28 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c308ca7-67b8-362e-b01b-4e5cef0b53a1 | -15.2627 | -51.47276 | 2025-06-28 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f59031c3-399e-32fa-a29c-e7442d76fca3 | -11.26782 | -52.75821 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f056c0ca-a1df-3134-bb15-3af56bdc24fa | -11.27584 | -52.74989 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c481aceb-2975-3e84-875b-5723da00a787 | -17.77842 | -42.806 | 2025-06-28 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a109237f-d33f-3836-b991-0feb4d556c6c | -12.11322 | -54.58765 | 2025-06-28 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dae22f42-c3e2-320a-8c78-7a10a38e8b7f | -11.57676 | -52.11787 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9730ae47-d49f-32b3-89f4-3da06b557b74 | -13.07668 | -48.83673 | 2025-06-28 04:04:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15b85f70-be6e-3ee4-8c78-25c12f8d6716 | -14.69092 | -53.38615 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b2d4d42-e589-32ec-89d7-0fb1fe28b4e2 | -13.93849 | -54.49652 | 2025-06-28 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1909dd7-e8ee-3e88-bd9d-44c62b201906 | -10.84922 | -53.76247 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 793b1f5d-b76b-3653-8b6a-4533c98ef2bc | -16.45725 | -49.51928 | 2025-06-28 04:04:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f015a31-c2b8-3cf8-ab8e-db02629e6dfa | -13.65082 | -46.81295 | 2025-06-28 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86759035-a4b5-3db6-b366-7342182126d5 | -12.25594 | -46.76617 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 45f9c2ba-906c-3eef-9e61-a80a847b1e5c | -15.35695 | -49.05049 | 2025-06-28 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fe71b8a-5f39-31bf-8d46-34e8a8573cf2 | -15.05662 | -39.12198 | 2025-06-28 04:04:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 775c59df-5cdf-3ef3-8990-3b8ae51b9d88 | -12.02135 | -47.77462 | 2025-06-28 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc740ba2-f18e-3955-b028-645f8e3f5772 | -12.11192 | -54.59388 | 2025-06-28 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2600bb99-e5a1-3da3-960f-b663500ab7c4 | -12.25937 | -46.77061 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ca610d92-ef39-3778-b65a-2e98734a844f | -10.82543 | -53.74583 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d16da51b-22c1-3e92-a9d6-b16c7d9d975d | -17.13845 | -46.59587 | 2025-06-28 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bf16e49-e613-33e7-b5c8-8fea16f75583 | -12.25873 | -46.77432 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a75017b1-6a19-3014-938f-e8831103488c | -11.58239 | -52.11337 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8e3b43ee-9fb7-35ca-8777-e9c1ec56e42a | -14.89306 | -48.39763 | 2025-06-28 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 680aec13-92a6-3071-baa5-f5ffae24881d | -11.43976 | -54.48515 | 2025-06-28 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b2e89ea4-8187-3620-81f1-7bfe4c01c7d6 | -19.88069 | -44.76406 | 2025-06-28 04:04:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7725c50b-236f-39a9-86b2-befd446e7483 | -19.55002 | -46.43372 | 2025-06-28 04:04:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abf509ee-3536-33bb-9679-28fe041917fe | -11.05225 | -55.07291 | 2025-06-28 04:04:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0bc30dff-f250-388a-956a-083d7ffa5de7 | -18.59508 | -46.55384 | 2025-06-28 04:04:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e1374b9-f52c-3bd4-8702-38f9ace36453 | -14.69326 | -53.39356 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64298b05-ce39-3278-a93b-f409b614bffd | -11.27072 | -52.74376 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 6ac6d753-8c26-3124-98c5-55f73f4b3537 | -19.16211 | -49.13248 | 2025-06-28 04:04:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b986de08-61c3-3e4f-8414-c0f5e8876d7e | -16.25328 | -53.67883 | 2025-06-28 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c91c39b-9950-3ebb-9bfd-6fa0d59e9efb | -17.66747 | -46.84324 | 2025-06-28 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df818d66-3328-32db-997a-da2d51f99bfe | -14.69496 | -53.39651 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1c7c37b5-9c37-317f-98d9-272b0be814b7 | -11.27489 | -52.75468 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c34eb90a-be01-3fb5-856c-ddea5da81743 | -17.04413 | -43.77765 | 2025-06-28 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 248da48e-d598-35f1-bca8-02312ad128d6 | -13.1235 | -48.58501 | 2025-06-28 04:04:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bb7ca33-19ea-3537-8324-967870f1d2f5 | -12.2563 | -46.76225 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8443dd19-ee96-3877-beb9-263d820168cd | -11.27679 | -52.74514 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 38bbcaa0-9cc2-30a1-ace7-15fd722d2127 | -11.57654 | -52.11227 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4c38d1c-8d98-35f1-bb5a-9cd8419d4f23 | -10.83079 | -53.75286 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7fed622d-5d58-340e-961b-fcfdc7c8ee07 | -15.12423 | -44.01024 | 2025-06-28 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bbb6bd1-4699-33e7-aeda-83d43c5e5946 | -19.71848 | -40.35429 | 2025-06-28 04:04:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a616b63b-4a6f-3ca2-aec3-e653e7392dc4 | -16.25692 | -53.67764 | 2025-06-28 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da0094c0-a848-3f5a-b50f-6bb618caa261 | -11.58262 | -52.11897 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08eeace3-8fa3-3b20-84a9-361a4f53d0c7 | -12.02572 | -47.77542 | 2025-06-28 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af145d0a-cc8c-37c3-bec2-13e57bffd3a8 | -12.26001 | -46.76691 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f13be755-bce1-3785-a7ee-e9c02451a17d | -19.63432 | -45.18863 | 2025-06-28 04:04:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21c6f7d9-6859-3afb-a2b3-c2c9f807bf65 | -10.83192 | -53.7473 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7d8c8cdf-23f4-3ff6-8317-de0580f20e9f | -12.03734 | -48.74847 | 2025-06-28 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30874c72-f2bf-3df3-bbd2-b5cab444ccf6 | -12.25563 | -46.76595 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e998cfef-1287-3b20-87ec-a5260d1ef30b | -16.18608 | -40.26521 | 2025-06-28 04:04:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e0a824df-e2c6-39b6-a8ec-dc6e25e6a14b | -15.56835 | -47.85414 | 2025-06-28 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78f99d36-f306-3740-81e3-f334dc35ed16 | -15.26204 | -51.47611 | 2025-06-28 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 946d7c8b-d0ec-372f-8d32-3a5b6bbb83bf | -12.26129 | -46.75949 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 667ad1a4-deb6-35fd-a2d2-9fb952d353c3 | -12.26065 | -46.7632 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| afcb38ac-900d-3f77-82b3-fd3dca0afd96 | -12.65849 | -54.10307 | 2025-06-28 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b412cae0-8e63-3e6a-af1b-3daa923d7c92 | -19.16633 | -49.13329 | 2025-06-28 04:04:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2a52cb2-e1c3-35cb-88c0-3ff041c40ed4 | -14.53777 | -53.83691 | 2025-06-28 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33bfcac5-32f4-3f8a-a352-00d7e1fdd5c7 | -14.38317 | -50.33067 | 2025-06-28 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09821ee2-f075-3514-b0df-b590a755bc63 | -11.58177 | -52.12334 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78474ab5-9a70-3665-a0cb-a32b902016ce | -16.25238 | -53.68312 | 2025-06-28 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddc81b4a-b19f-3926-8b37-2be689d92de7 | -19.44904 | -44.15368 | 2025-06-28 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f2d33f0-98f7-31af-8ae5-28f173126039 | -12.25971 | -46.76668 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c2bcbeb3-8542-30f9-a779-548805bfd13a | -12.25838 | -46.77407 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16407fdf-5bc3-3c64-b00e-a0244179e44b | -19.77833 | -43.9266 | 2025-06-28 04:04:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 109c9695-5770-384f-be83-67e8dc6410b9 | -11.58153 | -52.1177 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 782d40b9-ddaa-3a81-9d21-6acf64eb6abc | -19.5536 | -46.43442 | 2025-06-28 04:04:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dee783dc-ef66-3d5e-95e2-33183501a8e6 | -13.9451 | -43.24138 | 2025-06-28 04:04:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7ce07154-b11a-38bd-b37c-54c3db60ac2e | -14.69417 | -53.38912 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2e7f57a-68de-3d74-a02e-5ac67bfb6a41 | -13.07543 | -48.839 | 2025-06-28 04:04:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README13.md)
