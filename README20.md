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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3f7af79-8a05-3a76-9ea9-dde147d3e744 | -22.21173 | -43.30458 | 2025-08-22 04:00:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3a328460-e22a-3382-bef7-1ff50690af1f | -18.75182 | -43.85334 | 2025-08-22 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60b02888-0f29-366d-a110-1b7c6f918331 | -16.19109 | -47.99009 | 2025-08-22 04:00:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5c5b1ec-cf15-3a8d-9bb3-0b1d9b2f38a9 | -20.30219 | -46.63198 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4aa3bf2a-8450-3d81-b5cb-83ff31e57561 | -18.28992 | -45.52901 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3007cc0-5891-34f1-81db-18b04c512726 | -20.27154 | -46.57545 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 838e33cf-8231-3e9a-bce9-a39600829c92 | -16.15528 | -44.16052 | 2025-08-22 04:00:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c39830f2-d8ff-3c65-bca5-856a445e54c2 | -20.35613 | -48.34349 | 2025-08-22 04:00:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b19b41d6-8dd8-3a50-858d-3de6519a0d85 | -17.3951 | -44.25367 | 2025-08-22 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e0c93f1-3e77-393d-b634-f904936b0246 | -18.28516 | -45.53313 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23983040-ad3e-3525-8b72-16c80730f572 | -21.96235 | -44.97284 | 2025-08-22 04:00:00 | NPP-375D | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| e9a6dc6a-964f-3387-9492-7d2fb479f655 | -20.33417 | -46.54981 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb3caf77-fcd5-348e-80f3-61758a3ae602 | -15.83063 | -48.27262 | 2025-08-22 04:00:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef4f9c50-2d3c-36d0-a60a-48ea6cb0262d | -20.24068 | -46.59993 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4f46801-566a-3345-965f-58b685428ded | -18.26485 | -45.5532 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b589a1a6-4f3f-3c94-9bfd-1c3cb73066c5 | -19.98718 | -46.23196 | 2025-08-22 04:00:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddab86fb-72c3-366f-a2b9-f3a65d7b03cf | -20.40649 | -40.83963 | 2025-08-22 04:00:00 | NPP-375D | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36e62aef-1da8-3492-832a-31eb0ef1be5a | -21.43073 | -45.97237 | 2025-08-22 04:00:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 78370075-7c7b-3c92-8a75-53a0e1afa79e | -21.43163 | -45.96745 | 2025-08-22 04:00:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| acbb9940-ee9a-3b6c-8694-e33ec5dc7308 | -21.75571 | -41.46989 | 2025-08-22 04:00:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b967680d-8ad6-3120-aba0-47a801c79028 | -17.39589 | -44.24915 | 2025-08-22 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 956feb60-b42d-3661-980f-38b75af09cac | -20.29854 | -44.51265 | 2025-08-22 04:00:00 | NPP-375D | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0d7183aa-af9e-307d-a2e2-969cd0b837c2 | -20.23861 | -46.61106 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e049545f-8c0e-34a6-ab89-7070d5c19313 | -20.86917 | -48.53193 | 2025-08-22 04:00:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c37f271-c702-36ca-92ea-3d7256bdb858 | -16.5243 | -42.51298 | 2025-08-22 04:00:00 | NPP-375D | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1ef148b-2f15-35ce-a040-cbda3c4009e8 | -18.28797 | -45.51797 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 622b8685-d313-3c0a-b546-c2637d05c46e | -15.73817 | -49.44949 | 2025-08-22 04:00:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0efb5ad-823e-30b6-be1b-1cec1dd1e00e | -21.41031 | -47.97432 | 2025-08-22 04:00:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa263220-9da0-3edd-b1c0-cd58d61b4ad0 | -20.3072 | -46.62737 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58ae45d5-a47f-3e9d-b82c-6273bda9a8d3 | -20.23966 | -46.60541 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 564ff761-08c4-30fb-b310-373084f1d2d0 | -20.24656 | -46.65763 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a912c71-148e-3e8c-9f55-4e98b1a36b7d | -19.5882 | -46.35942 | 2025-08-22 04:00:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb469c3e-d2d6-361b-a643-c06c9508de33 | -14.97576 | -54.54356 | 2025-08-22 04:00:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3a900a0-9819-3ef8-adb5-5baaace89f5e | -16.1902 | -47.98846 | 2025-08-22 04:00:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56bb09d5-325c-3c0b-a0a1-bb04300eb244 | -14.66593 | -54.86059 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c73d725-95ac-3b6b-9fa7-93cf8836668d | -19.56453 | -44.02671 | 2025-08-22 04:00:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af3614bf-aa07-36ac-a67a-54987c597408 | -17.404 | -44.24597 | 2025-08-22 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 195cd3ed-8d2a-33c8-a5be-020bd70c6acf | -14.62119 | -54.85616 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69501ba7-6fb2-3837-b171-8d81dd91ce4c | -21.95877 | -44.97215 | 2025-08-22 04:00:00 | NPP-375D | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 42393302-8b6f-3266-ad1e-532260b79663 | -18.74969 | -43.8446 | 2025-08-22 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ead0a445-e295-3cf8-89b5-0147ba0f47e5 | -15.82925 | -48.27391 | 2025-08-22 04:00:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbebbb5f-19b3-386a-99bd-60b5e0410702 | -18.88325 | -45.02363 | 2025-08-22 04:00:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 153d09f5-cc2a-3551-8cde-bc1487b32b6d | -21.10357 | -45.08521 | 2025-08-22 04:00:00 | NPP-375D | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e93499bc-8f64-32d4-8a8e-d09795d6c780 | -20.24775 | -46.69612 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe97aff7-6752-3423-b7c5-7c9f5bc4e1c8 | -20.35522 | -46.56946 | 2025-08-22 04:00:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ced8868d-3321-3545-b5b6-9bce25bbc7ba | -18.61696 | -44.26257 | 2025-08-22 04:00:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e10048e4-b570-335c-8652-453f584cf2be | -18.28703 | -45.52302 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bd7d501-4f4d-3de4-826b-34a80feb1fea | -16.28493 | -48.73084 | 2025-08-22 04:00:00 | NPP-375D | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a55cb027-0e55-3c01-8528-26e6220e4b3f | -15.90771 | -48.41053 | 2025-08-22 04:00:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bf6ba1b-fc99-36f3-a1dc-eaadeef4efcd | -21.18876 | -47.13596 | 2025-08-22 04:00:00 | NPP-375D | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0edddd07-f856-31c9-9dad-9a117a6d22be | -17.39876 | -44.25431 | 2025-08-22 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cf8d106-2e7b-38f7-8e2f-1e0852d59936 | -20.33071 | -44.24291 | 2025-08-22 04:00:00 | NPP-375D | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ecb0ebe-101c-3b15-9030-2dead176dc10 | -16.78584 | -47.65556 | 2025-08-22 04:00:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 29cdbf5f-1ba4-30cd-a98b-5d6f32ff96d6 | -14.66768 | -54.85273 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7eb20090-f386-337f-8933-d1be63a581ff | -17.72747 | -42.38282 | 2025-08-22 04:00:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 557180a1-e97d-37a4-bf8e-e82a90f7de59 | -18.29704 | -45.50771 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1427278-4af8-3f06-adaa-7eb0a37fb9f8 | -16.78133 | -47.65452 | 2025-08-22 04:00:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 440fb458-3d73-345c-abed-7115c258a65b | -20.33832 | -46.57163 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ce12cc4-5ac7-34f5-8138-345be371539a | -16.15734 | -44.15877 | 2025-08-22 04:00:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb111ffb-8dbe-315d-aef6-eca3fd3d4365 | -16.55975 | -49.26714 | 2025-08-22 04:00:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 46977c9f-6c89-3e26-924f-60c09a587c08 | -22.48259 | -43.18764 | 2025-08-22 04:00:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63cd7f56-2053-34fc-bf17-1e4b8e74a46d | -15.73301 | -49.4483 | 2025-08-22 04:00:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d98de0d-247d-37b0-9998-5c24138fc687 | -15.55585 | -51.70002 | 2025-08-22 04:00:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f56b23dd-7b3d-398e-8648-c1f577cbf05c | -18.87663 | -45.01752 | 2025-08-22 04:00:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 5d23b894-df8e-3e38-9aca-2aa74ede94d4 | -19.90049 | -45.29864 | 2025-08-22 04:00:00 | NPP-375D | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01d7dd47-515c-3e17-b2fe-d9ac4bcea914 | -16.50168 | -46.74306 | 2025-08-22 04:00:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abda88d1-fd79-3bdd-a57e-ebbedddf1d2f | -18.28782 | -45.53693 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e18c150e-49c0-36f1-8446-f252153b8538 | -20.36227 | -46.50938 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb903321-0b53-3d3a-b0e8-c96c01fef177 | -20.43461 | -46.50507 | 2025-08-22 04:00:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60de3122-f855-37eb-89b5-c90f9ac0dcda | -14.6219 | -54.85567 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4389f431-c9c4-3d9a-90ae-74224a931b5a | -14.97745 | -54.53611 | 2025-08-22 04:00:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27aafec5-ed3f-3f80-8f6b-ac5f4f381952 | -18.62057 | -44.26324 | 2025-08-22 04:00:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 149529b9-7c63-398d-af8e-ea31c8743bf8 | -17.61297 | -46.69604 | 2025-08-22 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6771c959-4f0f-3b58-9c0d-359767129ba7 | -15.19686 | -48.69991 | 2025-08-22 04:00:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e4a5762-aeef-3c2b-b069-65e4611729dc | -19.7377 | -45.31818 | 2025-08-22 04:00:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4faf7520-e9f8-3642-82a7-743fe9a61c31 | -19.45872 | -44.73273 | 2025-08-22 04:00:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ba63c76-65f8-305a-be91-b8227266eff2 | -16.55532 | -49.26305 | 2025-08-22 04:00:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d331261-c234-3b7f-a800-e5bb1807afab | -19.28013 | -40.05987 | 2025-08-22 04:00:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f52859c0-d681-304e-9c6b-7b784784eb50 | -21.2408 | -44.58387 | 2025-08-22 04:00:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 922b5ec0-39b8-3456-bedf-6c8b6f8d0058 | -19.93984 | -44.57314 | 2025-08-22 04:00:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 0b68b489-65f0-39a3-887a-f8f1c5b983aa | -20.2727 | -46.56943 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 886cd6a1-0d9f-377e-b2fc-4acb0bd4f15a | -15.55293 | -50.32874 | 2025-08-22 04:00:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7cf44c1-7cc5-322d-92bb-a5fe23a63e5e | -14.99565 | -54.85896 | 2025-08-22 04:00:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a85c26a-94d4-3e3d-a57a-670b9a7de65b | -18.94292 | -48.35088 | 2025-08-22 04:00:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 302b9be5-2ca3-36d4-aba6-e7f86fe7f1d5 | -21.32122 | -44.87177 | 2025-08-22 04:00:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e7ec1e27-3a57-32e4-8ef5-b7990e288710 | -14.6306 | -54.84823 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c7b7088-5178-3196-aebc-bafe7adb14da | -16.78848 | -47.66639 | 2025-08-22 04:00:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| faef8e8c-38f6-3be4-8267-75a143e9184d | -18.26282 | -45.54222 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a95c43d-cdb8-36b8-ac2d-6ce93ca193ba | -20.27081 | -46.68797 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44e3445d-9da6-3c35-9b8b-d4c8e4059f18 | -20.6714 | -41.41992 | 2025-08-22 04:00:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a7e948b1-bc64-3e16-99d3-743a0c58eaa1 | -20.18729 | -45.23806 | 2025-08-22 04:00:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c995f2bc-a1df-3236-9e69-d8144218601b | -15.55912 | -50.32657 | 2025-08-22 04:00:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb087c40-b06d-34b5-a11f-b4d97cb61afa | -15.55757 | -51.70039 | 2025-08-22 04:00:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 133676aa-49fa-324e-b618-ffe36430cfc6 | -14.66126 | -54.85038 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 529b0c92-2e0d-3247-9751-4f90fe12042d | -15.9051 | -48.41094 | 2025-08-22 04:00:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd7ba20-47c2-3a89-bb8c-c7617dbf1397 | -20.67473 | -41.42051 | 2025-08-22 04:00:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| fc1eb599-1910-3854-b628-e5145f127d6e | -20.45507 | -41.67829 | 2025-08-22 04:00:00 | NPP-375D | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5fd2d39b-15d0-34a3-8f37-1f69a38ac3e2 | -18.28396 | -45.53607 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f52b96b-fe08-3bb2-9052-609a8e72d06e | -16.7804 | -47.65941 | 2025-08-22 04:00:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39faf230-9534-3ef3-800f-af162e416e93 | -20.27046 | -46.57307 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README21.md)
