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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8611882-9e78-337e-ba89-12a7b1462069 | -11.0535 | -45.16331 | 2025-11-16 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a70ada64-9309-3db0-83e2-5ea058e3871c | -12.86445 | -46.45627 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa55f949-ca5f-30b0-8635-303b92a109d5 | -12.65237 | -46.74998 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16ad03fb-44cc-3900-920b-9a6b9c6af363 | -11.85703 | -44.7192 | 2025-11-16 03:49:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20f44736-0146-3d26-ae9d-5c5e89ec87e4 | -12.05894 | -48.20337 | 2025-11-16 03:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85668985-810e-3dd5-b72b-fb6e54ace2d6 | -16.50232 | -43.73471 | 2025-11-16 03:49:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22f5ec85-d52b-3c57-94e9-797435709329 | -12.20111 | -49.61916 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a7ba6032-e9e6-374c-90c3-ea88df528751 | -12.80816 | -46.45293 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb174439-0b2d-3244-a523-64d01b3161dc | -10.54805 | -47.93757 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3076be5-8465-3dca-8096-d444a72eff6b | -14.65857 | -46.58185 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d3f9dfb-54a8-3932-984d-bd5be97860f7 | -12.05995 | -48.19841 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9d1da3e-09bd-3e50-b82f-feb71139e030 | -15.37208 | -45.64079 | 2025-11-16 03:49:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5903dc77-9af1-3046-829b-679752c35bf5 | -12.80963 | -46.44559 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 427ca44c-ed35-3f95-b8c9-bb1b3ae66ac2 | -13.81584 | -42.54686 | 2025-11-16 03:49:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| de3830fe-a65c-36d7-b184-06e53c75aa18 | -16.14042 | -43.65914 | 2025-11-16 03:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f898fc-b4c0-395c-ab7d-6c0328e7ea6c | -11.70937 | -48.86033 | 2025-11-16 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 19c64284-1b34-39ca-8e65-f55e5d4bc768 | -10.62607 | -44.59348 | 2025-11-16 03:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe31874c-42d1-3a56-8733-420646bb11b3 | -12.39174 | -48.09457 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39d921f3-ef51-3ab2-84c0-592c5e27aa66 | -15.47331 | -43.18341 | 2025-11-16 03:49:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c66d98af-a091-39b6-8c23-c5dfeb5b8030 | -14.64527 | -46.5926 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c9996cc-c331-360d-bc47-7a951bc8e897 | -10.67037 | -49.36597 | 2025-11-16 03:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a927a7b-92bb-3dec-b149-bd7e24509aee | -13.97693 | -48.77692 | 2025-11-16 03:49:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 843be4a1-7919-3538-bd04-edd361e62454 | -13.27017 | -47.30744 | 2025-11-16 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2dddf5e1-18d7-3283-b545-56b7fdd21f19 | -10.44736 | -45.09036 | 2025-11-16 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1288b08c-6e76-3faa-9615-4d086b60841a | -16.47541 | -41.10452 | 2025-11-16 03:49:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d7fe9eac-7d81-3518-8ac6-2b17ec5cacdd | -12.66864 | -47.17242 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6aa7a5c-6acb-3267-9f6c-1a27d58a79bb | -11.16702 | -47.45369 | 2025-11-16 03:49:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fdba748-7164-320a-8b18-9d8d72ecea76 | -12.45799 | -43.79528 | 2025-11-16 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d22c00db-0baf-376d-a455-10b3ec4f326f | -11.70823 | -48.86583 | 2025-11-16 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| af7eb45c-0e03-3b2b-8242-31f918d9e0b5 | -13.75889 | -48.67541 | 2025-11-16 03:49:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 216ec467-c4f7-3ba6-aeaa-984afbe53ca4 | -12.05601 | -46.97413 | 2025-11-16 03:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34c83680-1c78-30b3-9634-f8425e8286d6 | -11.16099 | -47.45262 | 2025-11-16 03:49:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d130d47c-9bb9-362d-bb3f-955700052a29 | -11.03337 | -45.21251 | 2025-11-16 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73189f19-53a6-33cd-9b8c-934ccd4b70cd | -10.84227 | -44.09191 | 2025-11-16 03:49:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9616a566-173c-342b-93f5-32c40155a0cf | -15.52479 | -44.38142 | 2025-11-16 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e848e8e7-2b11-32d3-a03d-2cb0c4ab30ad | -10.66402 | -44.7995 | 2025-11-16 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3deb7f1a-7e98-3314-a51d-cc4dfbb36b09 | -11.41302 | -43.3326 | 2025-11-16 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a49a7698-9eaf-3559-9ee2-39edbacc4e62 | -12.80402 | -46.44818 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 898df0e2-2a6a-3e9b-a508-e31a8f5d8936 | -12.04921 | -43.50735 | 2025-11-16 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83d711c0-a563-3b35-94ec-7570263991d8 | -13.81097 | -42.54997 | 2025-11-16 03:49:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1ccbc6be-4c59-3500-aaf4-559ad743bd04 | -10.44795 | -45.08716 | 2025-11-16 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5184e978-d3b6-3737-b108-7159f267f68b | -12.65872 | -46.74736 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ac59fcb-6d22-34a2-aafc-fa332034f711 | -12.8589 | -46.45558 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bc9585b-0c9b-3287-a04e-ba1f455dcf8b | -11.7158 | -48.86186 | 2025-11-16 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 566cfc2c-cf09-3938-9ab0-058ee47cb5b0 | -12.67339 | -47.17997 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f814955-363a-38e3-a064-cd05583e8e92 | -12.39882 | -47.55979 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ed67044-5050-39a1-a230-14b9849ae6e8 | -10.55429 | -48.00533 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c537ec8-39a7-35ac-99b6-532cc34e0945 | -11.91238 | -46.21872 | 2025-11-16 03:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ad9d8fd-57d7-3fab-a94b-c3a611e2c5a5 | -9.72311 | -48.90239 | 2025-11-16 03:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc971fcb-30c7-3811-a03c-3a895869060b | -13.39781 | -44.14537 | 2025-11-16 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61b3ca33-03ca-357e-8377-7c6ebc1bce6f | -13.55109 | -44.27416 | 2025-11-16 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14689753-3488-3023-8747-6441f1bfe183 | -15.37927 | -39.30798 | 2025-11-16 03:49:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3226fa9a-0e74-3619-a132-a5dbb8a53f7d | -12.20901 | -49.61487 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b03d5c9c-16a7-3631-afd2-d1463b3a0ab4 | -12.06193 | -46.97436 | 2025-11-16 03:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 394fab56-943e-3697-b999-6741d0e0af80 | -14.48974 | -46.62462 | 2025-11-16 03:49:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a760da15-6196-3f2e-b2ed-7d7777a2faf4 | -11.80462 | -45.55147 | 2025-11-16 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2f18cb1-cf47-3b8d-80e1-4906bbcfd63f | -12.40347 | -48.0971 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f213b401-8242-3b58-af85-9cc7c545556e | -12.38455 | -48.09874 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f845a1d-6c63-3ce7-a761-7a29637a98ce | -14.64614 | -46.58829 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bca566a7-1830-3de3-bed6-2f5639255611 | -12.20236 | -49.61325 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 295181c7-f0a4-3d70-8700-60d53e1bdcd8 | -11.81052 | -45.54923 | 2025-11-16 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a36f0108-e71e-315f-9cf4-cbadd0672d28 | -11.80526 | -45.54818 | 2025-11-16 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bae5132e-d8b9-32ee-bb7f-195ee9281d7b | -12.00861 | -49.28542 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| eda981c2-bf5a-3610-8f27-1398830fbffd | -14.68049 | -46.55571 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a006be62-5a81-33d4-99b2-a99dbbd55504 | -16.14472 | -43.66001 | 2025-11-16 03:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a33469b-a672-3ba6-8470-b18015e52f7d | -14.20593 | -41.84724 | 2025-11-16 03:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 32f4ac69-a416-34d1-945f-a51968297ec4 | -13.55204 | -47.39323 | 2025-11-16 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c3864f17-16d0-3796-8b46-9fd056590fff | -12.67911 | -47.18128 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 759e3764-6524-3d0f-9f64-c5d6bee4fbc9 | -10.80581 | -47.99765 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 734d574c-b242-3ad7-b289-424f21d6779b | -12.19444 | -49.61764 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 19a409a6-8fec-3f66-a496-d38bd9ceb666 | -10.62497 | -44.5994 | 2025-11-16 03:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd4456c5-dfea-3201-adaf-17c547bbce1c | -12.66428 | -47.1654 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 453e5148-4e97-3c02-aca8-97f416c92d0e | -13.55701 | -44.10372 | 2025-11-16 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eae87ee0-39e2-335e-8d98-3bcb78789576 | -11.05413 | -45.16 | 2025-11-16 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59410e80-1394-3796-b017-64f598e8a339 | -13.55795 | -44.09867 | 2025-11-16 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2076dd74-5232-311f-87da-eb2ecb9507ee | -14.49126 | -46.62419 | 2025-11-16 03:49:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50ddbf45-1b1a-39fa-987d-4ed6f86bbc44 | -12.65949 | -46.74355 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90960af7-1032-3ba0-b43e-c511ad2c331d | -12.40741 | -47.54782 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 027cdecb-1c3b-3e33-b615-ce6180c9eb8b | -11.70712 | -48.87123 | 2025-11-16 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2fa9e58f-1ebd-3ad8-8038-b8c3d02e5ff0 | -12.40246 | -48.10203 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01195cc8-e5f7-35f6-87b7-e2768470144c | -11.15868 | -49.45213 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aeec95a8-9fc1-3149-a17c-08ee12c3a39d | -13.00693 | -43.2161 | 2025-11-16 03:49:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6cef3567-aad5-35d1-9272-21c144e88103 | -12.67419 | -47.17587 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8c47fe62-2108-3c2d-b89c-9fbecd6f8994 | -11.15942 | -49.44344 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3947e629-0114-3d80-84a7-55e48dcf9a0e | -10.80751 | -47.9892 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7513755f-8b1b-3483-849a-c5737fa9f19d | -11.16542 | -49.45362 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05961ac7-8c26-39fe-ac83-cdaf4a92720c | -13.87149 | -46.84741 | 2025-11-16 03:49:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35dbd360-ef97-3f25-89ed-8be5fbf2f20f | -12.64949 | -46.74825 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 766ab87e-7635-336d-aae9-aa1e07139b01 | -16.49802 | -43.73392 | 2025-11-16 03:49:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a81911f-65c6-39a8-a4d9-6810aace26b4 | -14.64684 | -46.58484 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2444f9a-22ce-3300-8382-a3911d323674 | -12.67258 | -47.1841 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22a482b9-f285-31d6-87c7-91c2f81da737 | -13.75791 | -48.67165 | 2025-11-16 03:49:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63ac1da5-fa20-301e-8279-80dee49e33ef | -11.41388 | -43.32786 | 2025-11-16 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d01ed71-9649-3084-9fdf-6ccefdef7d84 | -13.36793 | -44.06004 | 2025-11-16 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6a51c1b-2fed-3f69-a931-581daf70d8ec | -10.84715 | -44.09273 | 2025-11-16 03:49:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 818e95d0-f5ec-321c-9cd3-84c3cbeaef1c | -13.38857 | -44.37545 | 2025-11-16 03:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75d83d2e-85d4-316f-9fe1-322dad3e0218 | -15.47955 | -44.19624 | 2025-11-16 03:49:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc90789f-7f1a-32a4-afe4-9cad2b857263 | -12.87698 | -46.45042 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59241866-587c-3979-9b15-cba4a7083475 | -12.06515 | -48.20454 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1154c063-9c32-3d1e-965d-3becd59a14f0 | -11.1395 | -44.93238 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
