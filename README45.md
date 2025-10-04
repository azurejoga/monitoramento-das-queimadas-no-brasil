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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf131b71-3524-31f8-bb8b-4ea60b5cd0ce | -14.63475 | -48.25604 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bfa7fee4-6759-3e19-a009-bbd50fea6ec3 | -13.39405 | -47.28023 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c97a8bd8-1b18-3c60-a5f5-892b54daed16 | -17.58153 | -44.4623 | 2025-10-04 03:53:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3491e88c-e972-34dc-b69f-818bd7ec673c | -11.54478 | -47.66188 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83426231-680b-3584-b31d-c7d0a0f12f90 | -14.30414 | -43.85995 | 2025-10-04 03:53:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f3beb62-13b6-3c1f-ad57-361195efe045 | -15.21239 | -47.19181 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37f11f11-2638-339e-a4fe-c1de0da2747b | -13.21335 | -47.81155 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b148197-3dd7-38d5-abce-90d4dd1621a1 | -12.71007 | -48.57863 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af5a87aa-6520-3b37-937b-a25aa605f557 | -11.77642 | -46.8214 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64254cdf-f45a-3e08-8236-5675c5001301 | -13.98714 | -48.20158 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af29ad90-01d2-3051-8941-694f7eca7bd1 | -14.66329 | -48.28825 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f613bd3-ddd6-3572-89fb-e5a1a216c020 | -11.595 | -47.0429 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32366068-c08c-3bbe-bc81-0e37e1e768d6 | -11.90635 | -46.37082 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ebfd849-c87e-3ca6-b833-b976eb385800 | -14.89044 | -48.2886 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd94bba3-10f9-38c0-86b6-fc72bba0877a | -13.11207 | -47.91983 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50cc131e-8059-3acf-a5af-f27c32f05817 | -17.1583 | -47.04031 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4bd5a67-add2-309e-ab27-3bcc2b5d77b9 | -15.56664 | -46.96479 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56527a6e-a03d-33ce-a068-83cc5888053d | -14.94795 | -49.97567 | 2025-10-04 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 723b48c6-c272-3f4e-87a3-6baa725c1a21 | -11.91929 | -46.38433 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ccf9e42b-5eab-3a64-8bef-f8b7044c6d7e | -11.91473 | -46.75362 | 2025-10-04 03:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 579125d9-7964-384a-9034-b10c171905ec | -16.36242 | -51.47854 | 2025-10-04 03:53:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6168967e-e79f-3e7e-87e4-2c7fb61d55e2 | -13.73771 | -48.08718 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fb68160-0252-390a-8a70-ff3976869e53 | -14.91702 | -46.879 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 973f0294-eedc-388b-9bec-850fc3ba1aa7 | -13.1093 | -47.87736 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abaf0fb0-9e6c-3518-8641-41cd90732b3d | -13.12196 | -47.8418 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac97e8d3-e0bf-355f-932f-314fd4f28664 | -13.3353 | -48.08142 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1529d18b-b198-3e23-829d-29bc1ad10ce3 | -16.02315 | -50.95398 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5d1c7841-dd44-3161-8918-fbdeba7baf4c | -14.35008 | -46.1087 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 579c1635-4302-3020-882f-a2cb1948d3c7 | -13.35432 | -48.07078 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b357ab2-802e-3a8a-9be5-ac481d0011c6 | -11.79176 | -46.83228 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 134217b8-5f89-3eb7-8b72-c2b97e4a03fa | -14.20708 | -46.08044 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6ec1d3e-cd86-3592-8f4b-04ac44c507c1 | -12.64385 | -46.97626 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8093588a-2687-33bf-ba16-13d95fad4c6a | -13.10393 | -47.87622 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa220f6-a16d-3d11-a730-beb28eb27a1a | -13.25096 | -47.24208 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ddf8856-ae18-35ba-b504-bd49aae24438 | -12.80706 | -46.85325 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44ec55c5-b5e0-307a-b3de-4be4e2dbbdbc | -13.81516 | -47.58733 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a9f9a18-ab0f-3618-a581-b1318f951247 | -11.83497 | -44.91449 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1529d33-b964-3aea-bccd-3c6fa482ade3 | -11.5644 | -47.67767 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aeb0476-3eeb-3e9e-9795-de6e24460275 | -13.13304 | -47.81404 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 576ca077-d236-3113-96e1-8081b3904d13 | -12.08294 | -47.99022 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3d204b9-d3e4-369c-b711-85e2f6b294d7 | -16.08434 | -51.06756 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b969b908-65cd-3f34-8204-35f348f64ef1 | -14.31735 | -45.86053 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6777433b-99ac-3eed-b19b-17fbbec13a26 | -13.96237 | -48.18459 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d8e633f-fece-35a4-bd60-f6452f6abdcb | -13.24215 | -47.8346 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fb5d217-19dc-39c2-83fc-ffb4c8128b87 | -12.11116 | -43.44603 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71c3e914-27cb-3e50-9108-ca8b1efdb042 | -13.20981 | -47.81992 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b91788f-c5d2-31df-bb54-8cb6ce7e2e81 | -11.7879 | -46.82462 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3d309ec-e9c7-37bf-b408-3bbb00c5c00e | -17.14993 | -47.03088 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c59124d2-0478-3ef6-ac48-acb2615bd4b0 | -13.12011 | -47.93589 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 357f9f86-1433-34b7-8b47-3dced1796421 | -17.15254 | -47.04443 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0c33991-e184-3af2-a7ff-83cb9380adc0 | -12.64889 | -46.9777 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6f513e4-b2e3-38df-bf22-285daf8bc8d9 | -16.37278 | -47.00285 | 2025-10-04 03:53:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c697a8d6-2156-32fc-9a62-4275e4bdd2d3 | -11.80511 | -45.02917 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7b84612-f7fa-3be5-afe6-b5ddfa4a7996 | -13.32484 | -47.19114 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9196e26-7b7d-308e-9d1b-b3f699e093b6 | -14.91563 | -46.89277 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5f78e364-fef7-3669-8518-b9d14b29c828 | -13.22255 | -47.8212 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4288d59-c89e-3a0f-9362-acf9161622cb | -14.46548 | -48.39515 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55403755-6e95-3f4e-9d1a-079902d21b59 | -14.87498 | -48.13129 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b72cbd4-7506-356f-8061-6fcad914d561 | -13.11522 | -47.87572 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab168286-7cdc-3dae-b264-82d6d9b9a441 | -16.69733 | -48.89035 | 2025-10-04 03:53:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd5d8415-bc6a-3023-b043-23df1bbf8e94 | -16.1614 | -45.12119 | 2025-10-04 03:53:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e64b783b-d371-332e-8cba-640c1d0cab0b | -13.29251 | -47.83306 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b0739df-f38c-333f-a650-ea1de769262f | -15.78601 | -42.04526 | 2025-10-04 03:53:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| efc22429-dec2-39d9-80c4-af5a71997a35 | -12.30246 | -45.36233 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27b9b861-c398-3dc4-b97e-4bac409b9365 | -13.57767 | -48.1763 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 296655a2-7433-3561-ac84-019df6cae335 | -12.70609 | -48.56893 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3515e8e3-6a68-3327-8181-8dafae790296 | -13.7369 | -48.09124 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b273bed4-2f9b-3341-90ee-3b35bf70199b | -13.76133 | -48.05295 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d7b37fe-5e64-3373-9de1-dc3ec5119faa | -14.63853 | -48.23693 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ac83632-80e0-3979-a56d-9e16ec8cbe18 | -11.9071 | -46.39412 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f10c0eb8-9b3b-3cf1-a4c7-9050a6ed8fc6 | -17.15256 | -47.04273 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 205c40f6-a1cb-3632-8a3c-d98be49cb34f | -13.12506 | -47.82619 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23364d4c-b5f8-30a4-b533-6ba337fabf6c | -15.52985 | -46.83158 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b4d50ef-8fc2-3360-831e-121af3d65c6b | -13.32428 | -47.19409 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 427fecfa-2b6e-3dd5-b677-34f81a6ecf36 | -13.15828 | -44.63814 | 2025-10-04 03:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4027c24-1807-3579-b10b-5f1962c5b128 | -13.9825 | -48.19658 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d969a71-7a03-33ae-81e8-dd435cefc142 | -16.36276 | -49.39846 | 2025-10-04 03:53:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a6d07bd-8bdd-3a1b-942d-7045a85fe7f8 | -14.65676 | -48.32053 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0a915a8f-8e1e-316c-8091-a5277fddaf1b | -11.91202 | -46.39549 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 4ee869d6-62d1-3634-a557-95d3c7f14c72 | -14.20398 | -46.07596 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d998a51-5ac7-398b-8b50-ae53c78f5ba9 | -16.27484 | -47.10257 | 2025-10-04 03:53:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74a739cc-c14e-31b4-9389-05badf3ffc7f | -13.88616 | -46.51945 | 2025-10-04 03:53:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f2027f23-7364-3e61-85c1-1f970e2d838b | -13.31985 | -47.7929 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 579f1a11-0c10-3d5e-9209-4dbdf94c0cde | -14.28031 | -45.87915 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25117356-051d-3f23-b48e-3062b58be801 | -13.51415 | -47.24633 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6ee0c75-277e-3e37-b190-cfee0a2a5330 | -12.36776 | -46.51092 | 2025-10-04 03:53:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72b083e7-308b-3ae0-ab6d-aef0a49cddea | -13.32774 | -48.09109 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0e94d05-46ed-30c0-9528-c830a2a479ec | -11.68518 | -47.49559 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 832fe548-9537-3686-8150-baa70ceb8abb | -14.45419 | -46.33577 | 2025-10-04 03:53:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba2f433b-8c5a-337b-b9af-8b0866042347 | -13.81454 | -47.59045 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b986f213-12ce-3cdc-9650-35f8ade9a703 | -12.08047 | -45.16664 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9cb6c94-dd80-3509-a7f2-a5419bf18000 | -13.99646 | -48.18723 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d04741e1-30e3-39dd-8e0d-b0f1c7632981 | -11.79684 | -45.02255 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47ae4d30-07e4-3d47-9bbe-7b839de2c2c8 | -13.74377 | -47.94506 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f276e61d-43d5-3dd1-87b3-191035020511 | -13.21084 | -47.81462 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99c4d666-41ec-3b19-9114-62114881758b | -13.23776 | -48.48689 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c33628a-e7ef-322b-b3d0-0aca501ce3dc | -13.32268 | -47.79185 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b9f4c32-c207-3cb2-8daa-e5310523df9e | -13.33108 | -47.57779 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 615b5c75-3fba-328f-8cf5-116d350c29ea | -12.02956 | -45.21112 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 80ee34cc-53ff-335f-9a9e-dd958a7d6e48 | -11.91026 | -46.37746 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README46.md)
