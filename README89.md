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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8f4b40b-1710-3162-ad83-377ee224c436 | -17.39698 | -47.16442 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 188737a0-107e-3758-9d37-6cb62e634443 | -12.03025 | -47.90882 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 859f87db-edd1-340e-8fdf-482a7eca5e48 | -13.15001 | -47.84462 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8d558723-aafb-33ad-b70e-acf022964ba5 | -14.68109 | -49.61504 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02437258-a5cf-36e5-9fdc-5b3bb0166491 | -12.89154 | -46.90483 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf5edbbe-f054-3fd1-9949-c0870478946d | -13.30643 | -47.1953 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7401d433-a775-3ccc-9158-de1b56a3885f | -15.93378 | -43.30152 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da2a6c9d-5818-33b3-8f17-a2383f2bf156 | -14.98069 | -46.92013 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 669ffa20-76e2-3835-b802-6fb3dbd63ae1 | -18.49925 | -44.0454 | 2025-10-02 04:32:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fea32e7f-04a0-3072-904c-2e02f439e6f2 | -15.22511 | -50.11202 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a67e830-004a-38fb-927a-9973deb91aa9 | -14.70395 | -48.21641 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 877fc0a8-d901-390a-b748-a3caad2eb943 | -14.796 | -46.99231 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5717e5ae-7d41-3146-b21a-3c977c4797ba | -18.8479 | -43.14782 | 2025-10-02 04:32:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 11352ad1-00f0-3de8-95e8-c5c93da1c99d | -13.24011 | -48.50892 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea1a1509-6cbd-3157-8331-88cf38e8954f | -12.20127 | -47.8131 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e241e09d-2559-319a-8fac-69e8d071f267 | -13.0798 | -46.9973 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cae3003-416e-36f7-b18e-a41c281f6f25 | -12.94374 | -48.43772 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4feea78a-cdb9-3a71-80dd-afa6c4812c05 | -14.64425 | -48.14824 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9719aa82-8216-3c3e-9ba2-8167ef6b1cba | -17.08428 | -48.56332 | 2025-10-02 04:32:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ee75fb2-091e-388a-b1b4-777d15204e96 | -13.96305 | -48.13446 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e1bb060d-2f04-3a36-a3a1-5dd90a73774d | -14.21349 | -46.12011 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| afe779c3-363a-3100-b49c-879c57b386bc | -12.42426 | -45.1672 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dee50d65-7708-3311-8280-0daef6bd7c98 | -16.36873 | -47.05097 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2772b70-7559-3ac6-96c2-de799caf6d0e | -12.84025 | -46.94791 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba30ef99-526d-31bc-b9a5-f37f75b2c40f | -13.23285 | -48.51139 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cbad180-6d4f-36ab-86f1-e38454c29388 | -16.04493 | -50.87405 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1ecde2b-62a6-306c-8408-2546fd9ab984 | -14.86107 | -48.29745 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 906292b6-ccc4-34bf-a0bd-06a0d0e5ecb1 | -12.8632 | -47.02134 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7d727e9-8159-39dd-a2e0-287b3144e484 | -14.70079 | -49.6222 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da6950a2-4007-3462-9b15-23907f2fc644 | -14.89538 | -48.33206 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9e657fa4-5221-3462-b569-1e9444023233 | -15.94546 | -43.30724 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72b0149d-0557-33b2-9b74-cab5989b249f | -14.66929 | -48.11943 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3236bb6-d7cf-3e3b-9479-9eeb38d3344b | -16.00404 | -50.90354 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e944ddc5-fdb5-3ff2-8e4d-b32f16579ba8 | -14.31649 | -45.98935 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 325a2cb5-52c2-35e7-9817-bcea54d046ab | -16.0687 | -51.01375 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 694e08af-8139-35a1-8633-6555865494fa | -15.99704 | -50.90242 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a53fd10c-841c-34c1-9326-370b65457816 | -14.42014 | -46.13504 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29537dff-96d1-3998-a451-e5ae5c1400ea | -19.85398 | -44.08581 | 2025-10-02 04:32:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14a91f9d-1fee-3920-9aae-3b65264a94b3 | -12.86431 | -47.01421 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08be1057-ed59-3f6c-9380-d5b361e54ab4 | -14.90705 | -47.22005 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2536638b-463c-37dd-8c30-5468a8f23155 | -16.00688 | -50.908 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 21ff0db3-3e43-332d-9311-d987a820ff3c | -15.93824 | -57.50821 | 2025-10-02 04:32:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 972c0daa-e227-38cb-a985-02435c40a420 | -12.63212 | -44.85261 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04e9e6f5-5869-37a0-a51e-49d51a34ceb1 | -18.84418 | -43.14291 | 2025-10-02 04:32:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c4e27f9c-9dbb-34e7-8b5c-4d065253da4b | -13.56647 | -47.27706 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edae1a89-a185-3889-a6f9-29bf76e91279 | -14.90874 | -47.2091 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0680a642-0ae2-3bed-84f6-6432de09f51f | -11.91901 | -47.88353 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74c1e6dd-1703-34a4-99d3-cbd472e9c37c | -15.21804 | -48.00385 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb28a7bb-2198-3b96-bfc7-dea23e174de0 | -19.57111 | -42.58741 | 2025-10-02 04:32:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dacfa853-114f-3db0-b69a-dc1d8167ffd7 | -13.95369 | -48.10734 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 896e79f1-039d-3912-9edd-b37b3d69e1ca | -18.44223 | -43.81788 | 2025-10-02 04:32:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0acecaec-21ba-32c4-874c-6d48472caa0d | -13.80533 | -47.52777 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a948ee7e-5fb4-3820-950b-7140a93f71e5 | -15.3378 | -46.25993 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b51f0245-438e-364e-88bf-ec86a7b3c23a | -15.94622 | -43.33302 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca25fa5d-92e7-3fd5-899e-216449871533 | -15.31821 | -46.29673 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17664a7f-73c5-3a1e-b5b4-5d92a02f0a2a | -14.6783 | -49.61086 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7555b1f-e210-3065-95a4-864b0a39613c | -14.30145 | -45.97121 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bca47ba9-05e8-376b-9c49-f98d571616d7 | -12.75507 | -46.9088 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71174550-ae19-33ab-a3f1-2a056d9de71a | -11.98497 | -47.01723 | 2025-10-02 04:32:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43aff6e9-abff-3cba-b569-85d9fc0148c3 | -14.18294 | -46.66954 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e150261e-3cf2-3df3-853b-b7f844d348ec | -13.71569 | -48.62835 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac431e6c-3395-3560-988b-4477f11aef7e | -15.79749 | -43.73525 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| be5acf62-dddb-3703-a0fc-d0c5466ca56c | -12.8971 | -46.91322 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25f2e391-9b23-3a73-9fff-dfaafa6d924b | -14.30552 | -45.99162 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51b818ca-51c9-3984-acd9-340287c01030 | -17.08485 | -48.5597 | 2025-10-02 04:32:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2d3fe3f-a3af-3090-b117-b404247e1b04 | -13.1595 | -47.80613 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63d3dbbc-43bd-3363-b2dc-cdc3b1596e3c | -14.48073 | -48.40998 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b3e3e66-fb73-3518-8043-5ae0e6eebdf2 | -13.00459 | -45.22952 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7c26b3f5-e310-3801-9f7f-870a867b6343 | -15.26223 | -49.31325 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4ef0f07e-fa73-3656-84c3-3c6360ee3346 | -12.685 | -48.57166 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc9db44f-b091-320b-9f44-6cebc1625cd1 | -14.31418 | -45.98108 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b92418c4-f23d-3232-ba5d-44d5e094076d | -13.20671 | -48.51099 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70ab8c33-d5ec-39c4-93d4-08c79d2c6190 | -14.58022 | -46.36633 | 2025-10-02 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 385a1b73-7eb2-317d-bf58-ec1155131ae6 | -13.67188 | -48.0937 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21b4d2ff-089c-3cfb-b34c-d014ef6cf7b7 | -12.94707 | -48.43829 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 347a3ade-ad33-39a0-9257-0151a99d14e4 | -15.29561 | -45.08929 | 2025-10-02 04:32:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f76318cc-a9e9-3089-a643-2b77bf3f4081 | -14.58696 | -46.71669 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f773c91-61d7-3155-b915-f04fd3f95060 | -14.37794 | -45.96596 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 18743260-f7f3-3b41-bc5f-dea74790d69d | -12.76284 | -46.88073 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c9514ea-e751-3006-9d1a-a283716ab17b | -14.79263 | -46.99177 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46fe669f-6ca4-3290-b906-fa9414e66937 | -15.26306 | -49.28709 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 044ee82c-43ba-366a-8dde-9b3201e72221 | -13.21176 | -48.50081 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c7c9d28-64b4-325c-9ef4-2052e7e6a1de | -17.17579 | -47.03567 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| deab935b-05c2-3be0-a938-dcd5dfb52a5a | -15.15881 | -48.40184 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35edbf84-ed7b-3210-993f-53198ddf38b6 | -13.05059 | -49.15713 | 2025-10-02 04:32:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ef2c6e8-414e-3aa2-9a39-52bb9f1be8c7 | -14.46733 | -48.42976 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca3d510c-9d27-3dc4-b1aa-13a82188a2a1 | -19.57162 | -42.58309 | 2025-10-02 04:32:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d5914eaa-3691-311c-8ed8-e3981b0a16c4 | -18.50865 | -44.03636 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 51e261c5-e24d-31a8-9948-3608eb20cce5 | -13.74601 | -48.7066 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4830716f-c1b4-3498-9598-5acd066af61f | -13.79889 | -47.97649 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2725449-39de-380e-8e40-afe94db657b3 | -14.89877 | -48.31063 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c599574-fe2e-3c5e-9625-f25c0fcf6a2a | -17.322 | -49.38397 | 2025-10-02 04:32:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4e3e7ce-21c3-30ef-8b24-f4ded17ba29d | -13.40984 | -47.78549 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 336deda8-1d3a-3c5b-8407-0eb0aed15e22 | -14.70537 | -49.61553 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e2adfde-6e6f-3f76-b728-29af987cd0f6 | -14.95759 | -46.88976 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2de85e9-213b-34bb-800a-0d629c99929c | -13.3171 | -47.33614 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe1e4468-8b95-35b4-95f8-cdd3ba1e089e | -14.60273 | -48.32445 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c136254-7449-3196-8832-20cb2b6732de | -14.89867 | -48.12406 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ed37fb8-a3e9-3781-a760-10680d9b97bf | -14.80048 | -46.96283 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8390824f-6ceb-32b1-b8c6-9155e8dc3194 | -17.38877 | -46.14207 | 2025-10-02 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README90.md)
