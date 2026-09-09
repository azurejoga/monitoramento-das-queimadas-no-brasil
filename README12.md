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
| 8b26e489-26a6-3d55-884f-686fac0d4c26 | -14.91537 | -44.67146 | 2026-09-09 03:51:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0abe6c5c-daf3-348b-9522-ad6ba6352bad | -13.77436 | -43.64608 | 2026-09-09 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| baefa65c-20ab-36b4-9d12-7f39300ae1c7 | -18.18794 | -45.23821 | 2026-09-09 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5a49b73-ff6e-30db-9e2e-c0f71d057908 | -17.50668 | -43.98594 | 2026-09-09 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b17c5b07-b5cc-3746-a379-18471d42ea92 | -17.5969 | -44.66564 | 2026-09-09 03:51:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc859972-f024-35f0-8f62-c65a334e62a7 | -13.81633 | -42.17234 | 2026-09-09 03:51:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1cf0a11b-0e1f-358f-9b5c-9bd99676ba11 | -14.91609 | -44.66753 | 2026-09-09 03:51:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0725ed55-5992-3052-8db7-303463e1f04f | -12.95373 | -48.61161 | 2026-09-09 03:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b9f8ae1-a925-3daf-a78f-26ba4eccf2d6 | -13.77499 | -43.64254 | 2026-09-09 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f428a22-0e76-321f-b325-6ffb01d819e3 | -18.02159 | -44.60398 | 2026-09-09 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9420512a-4f6f-335f-8227-bdd60ee5be61 | -13.40735 | -44.16129 | 2026-09-09 03:51:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d3e99958-228e-3757-adc1-872e9a110910 | -18.02023 | -44.60569 | 2026-09-09 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e979f7e7-09ef-3d35-9d51-7fc1f3841797 | -14.91049 | -44.67459 | 2026-09-09 03:51:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29638e96-7883-3f66-8f27-e4854d76173c | -12.95293 | -48.61568 | 2026-09-09 03:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76872466-3376-372f-ba16-077bdb942465 | -13.40911 | -44.16215 | 2026-09-09 03:51:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9c6e5bb-5b76-3b33-beb7-1385619db7bd | -21.90253 | -49.51955 | 2026-09-09 03:53:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 275d9f40-3a0f-33a3-b641-f417d08e5670 | -22.26745 | -49.32291 | 2026-09-09 03:53:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5907c145-a7be-386d-b3de-743633da7875 | -21.90186 | -49.52269 | 2026-09-09 03:53:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6e52054-4e10-32b1-adda-006fc7d72502 | -22.70132 | -43.36297 | 2026-09-09 03:53:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8bf032c5-eb53-3ae3-81b6-72f0d577c328 | -27.45477 | -48.45383 | 2026-09-09 03:55:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c86f9ce4-bfb2-3f22-828c-6144de447677 | -29.10954 | -51.91091 | 2026-09-09 03:55:00 | NOAA-21 | MUÇUM | RIO GRANDE DO SUL | Brasil | 4312609 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f0944dc4-b4cc-3dd7-b391-880da2874b18 | -27.45498 | -48.45237 | 2026-09-09 03:55:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3cca6508-8ebe-36d7-b803-e9f4c5883d93 | -2.9392 | -50.4622 | 2026-09-09 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 18b020cb-10f2-38be-b53b-ab0288ba72d6 | -2.9391 | -50.4832 | 2026-09-09 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 606c3283-ed7e-3ffc-9626-1dc10d373b84 | -2.9391 | -50.4832 | 2026-09-09 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 896f1743-d23d-3498-91a9-23375238d8fb | -2.9392 | -50.4622 | 2026-09-09 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 030592d0-b255-3383-9c30-ac3d2e919d7e | -2.9392 | -50.4622 | 2026-09-09 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c45868db-e90a-30e0-af6e-81a63dd00bfb | -2.9391 | -50.4832 | 2026-09-09 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| dd0c3499-65da-3faf-ae0c-45f4231d6bef | -1.03844 | -53.73078 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd4f91fc-5bfa-3e47-9b05-9d8f8280749a | -1.03289 | -53.73671 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 177977c6-1799-3e8d-8eaa-47dc2dba51c9 | 2.51341 | -50.85305 | 2026-09-09 04:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eb77257-a0e9-3b63-874f-53ced5a137f2 | -1.03768 | -53.73554 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2bfabad-e48f-3043-bc48-9bf7ac4a67ab | -1.03927 | -53.73769 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f56ebf94-51a5-3abf-ad6f-bf1044d309a2 | -2.93977 | -50.47655 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 963c4b00-29e5-3ce6-85ba-4bc8ee8a0be9 | -2.94573 | -50.47169 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f316a95f-21c0-3c4f-965b-3eaa9ccfc6b0 | -2.93547 | -50.47507 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25bc565b-996f-3217-ad6b-be74193dfb98 | -2.93673 | -50.46427 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bca64de3-002b-382a-8be4-d36a0f356945 | -2.94172 | -50.46511 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58e2dab2-1f0a-3d85-9162-378f37de2c57 | -2.94233 | -50.46446 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b28ea5ea-9421-3da8-b9b6-7b0b0abcf17a | -3.71482 | -38.84679 | 2026-09-09 04:23:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bbf81c04-34a0-3836-8610-015d68fd4f21 | -2.11925 | -54.38629 | 2026-09-09 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f982e89-dae5-3f37-928f-3a11be27f2d3 | -2.61126 | -51.21442 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb696c3c-5f9d-3870-8858-3c8af00ab27a | -3.24676 | -47.25084 | 2026-09-09 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb7e813e-ef69-318a-a560-15b5bd4c337a | -2.93952 | -50.48175 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f55e271-b11f-3553-9ce7-6196049d3985 | -2.93142 | -50.46843 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db43c668-ea9d-35b2-ab6b-133c1953d38b | -2.88932 | -40.52299 | 2026-09-09 04:23:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6e3ec45f-b184-3c92-95ac-b8660d8e04f1 | -2.11834 | -54.39169 | 2026-09-09 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b33edd4a-c803-3543-acc3-953cce12d0bc | -2.9414 | -50.4702 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9ea14ed-c4fc-3f17-84ae-8fd5f9dbaf67 | -3.24759 | -47.24567 | 2026-09-09 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce3ea835-9635-38b8-9463-3a0654486473 | -4.86783 | -37.44762 | 2026-09-09 04:23:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8df0d691-f013-3840-82c6-06d26e0562fb | -1.67182 | -55.66965 | 2026-09-09 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bf95dc1-b05e-3c1e-a362-b378b63a8be4 | -2.95461 | -48.58968 | 2026-09-09 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8a59562-f33b-3088-a1c9-b326fcab0fd6 | -5.008 | -38.02716 | 2026-09-09 04:23:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3b4c8139-495b-3402-80f0-ac49d914cb7a | 2.51397 | -50.85676 | 2026-09-09 04:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fa37d91-5804-38fa-b3b0-c706355f1a55 | -2.93576 | -50.46996 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72d9f588-4be9-349d-95e0-8de27f66dc47 | -1.03362 | -53.73229 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e71d6687-3e44-3401-8dcc-f96243d119a8 | -2.93049 | -50.47417 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a35822ea-8088-3355-b02e-0b1d3289d1fb | -2.93641 | -50.46931 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7a53042-d49c-349e-aaa5-5a3bca7a98e6 | -2.91791 | -41.36655 | 2026-09-09 04:23:00 | NPP-375D | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 36608c18-eeca-36a3-b658-28d46e8a1897 | -3.3199 | -44.58799 | 2026-09-09 04:23:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 191f20b5-a8a1-3f1f-8e40-c28fb40d1a43 | -2.93734 | -50.46361 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b028dd6c-5faf-395e-953a-3f79faf83100 | -2.93477 | -50.4757 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da6067a6-aee0-3fcb-91f5-23eb761d2968 | -3.24277 | -47.25019 | 2026-09-09 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2a5506c5-9048-3fb4-8615-1b58f9b983d1 | -3.97251 | -41.52259 | 2026-09-09 04:23:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26ec017a-ad6d-3474-9ccf-e2c0241d724f | -3.65394 | -40.34252 | 2026-09-09 04:23:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 655348d7-d238-39bc-b7bb-9610a68d520e | -1.03044 | -53.73997 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0269a4c8-9272-3250-b3f6-327e8234186f | -3.65047 | -40.342 | 2026-09-09 04:23:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 45ece1d6-96c5-3eaa-8a1e-8ac883c317db | -2.93453 | -50.48086 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fde33791-1e75-3daf-9a2d-1bf928d48ece | -2.94074 | -50.47083 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 527cec8b-c62b-3d91-b383-34c2c4cb2c07 | -3.97361 | -41.51553 | 2026-09-09 04:23:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f874037-2b6d-33fd-9fd2-884f6182b82f | -3.44684 | -47.27265 | 2026-09-09 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b7e8240-c6b9-3008-8d0b-1e227782cd87 | -3.51917 | -43.25696 | 2026-09-09 04:23:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 380d68ed-c57f-3fb0-a275-6f1598938bae | -2.94546 | -50.47676 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e684652-49fe-3004-8a62-a2267654336d | -2.94671 | -50.46595 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c91b21b-471e-3690-b98e-66d7b37808b4 | -1.18986 | -55.72307 | 2026-09-09 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4cfa3365-bdfa-304c-be08-793f88bd2741 | -1.03679 | -53.74114 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a37824a-d9b6-354a-9a02-1169aabb7dd5 | -2.93877 | -50.4824 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19d39b13-35a7-309f-998c-9844a19f0dff | -2.94326 | -50.45876 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3549bf3-5f0f-39cf-8c10-a5de54eee3df | -1.19236 | -55.72211 | 2026-09-09 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2fe2ce8d-ff71-3432-b0d7-f15d369c740b | -3.2436 | -47.24503 | 2026-09-09 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c56b274-79e5-37cf-82a8-17105ac02a4b | -4.46854 | -38.50395 | 2026-09-09 04:23:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9fe12699-8041-3ce0-8bec-a7f8f13ab86a | -3.97306 | -41.51906 | 2026-09-09 04:23:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4c6c9e7-8f6f-30b1-a309-bce7feb8dd17 | -3.23877 | -47.24954 | 2026-09-09 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a93b33b2-9149-389f-ba37-40bab32fcc16 | -2.93235 | -50.46276 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b7fc0fa-d379-31bb-a83b-f67bb72e8bf3 | -2.9377 | -50.4586 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e44dbb3b-c9ff-3620-b735-0bf320468d89 | -2.93827 | -50.45793 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f56b300d-59a0-3b81-9fec-e3b1648bfd87 | -3.23961 | -47.24438 | 2026-09-09 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6ceae93-b82a-3e58-8554-e37ffbe7cef6 | -1.19366 | -55.71453 | 2026-09-09 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 52d21f1b-f3b0-313e-b07d-771f939a8445 | -4.52183 | -40.55313 | 2026-09-09 04:23:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2dae988f-fab7-3b3d-a7bf-f7e7914f5e2d | -1.0319 | -53.73081 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c69779ad-241e-3dd0-88d5-f8941f1269c5 | -1.03123 | -53.73499 | 2026-09-09 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfb7bb39-59b5-3fdb-a243-59466d5fe5b1 | -2.94638 | -50.47108 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2bd83ed0-947a-330e-bbbf-c61bb72bd67d | -2.94476 | -50.47736 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c2bb78f6-e651-3423-9744-053a18113062 | -2.94976 | -50.47816 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f19cff42-af70-39ab-9791-3daf1d633a79 | -2.94269 | -50.45942 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41be27ae-667a-379b-9026-f6dfa00aec6e | -4.52368 | -37.72619 | 2026-09-09 04:23:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05b723b1-460b-3f3a-b612-6470b354746b | -2.94452 | -50.48254 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58e04dae-853f-3915-bee6-81485b5b4d36 | -1.19111 | -55.71547 | 2026-09-09 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9bc185e6-99fe-3e04-9f07-810676ba92f7 | -2.94046 | -50.47594 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f8e85db-8d1e-3cbe-bfe3-48ebbbf21051 | -2.94378 | -50.48312 | 2026-09-09 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README13.md)
