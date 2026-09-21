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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb1db9d6-2dfd-3ed3-83bd-0b3e90688148 | -3.87578 | -40.75288 | 2026-09-21 04:00:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf7d8965-9fe7-30a5-9819-e4ab818763fe | -6.90659 | -43.72642 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf3b257a-8da5-36bd-aad1-cfa3936e5997 | -3.41219 | -39.2813 | 2026-09-21 04:00:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e8ee09ae-20bc-3ce4-80f0-81d827b9834a | -3.3489 | -42.76131 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f73bc701-1bef-3180-939e-a11453c0f098 | -6.93364 | -43.0994 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50e5c9be-7f56-35c8-b3a2-8d7d433c8b09 | -6.56048 | -45.54966 | 2026-09-21 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00c44e13-4227-3886-a02f-93e77689399b | -3.34359 | -42.7651 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13e7bddb-a04b-3332-a28e-de22300150b4 | -4.33885 | -46.37231 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d6c1f85-adfc-38a2-b0d6-e6e17b7dcd2e | -6.3799 | -35.15383 | 2026-09-21 04:00:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e257532d-0b85-35f9-ba19-b8e1b051c86c | -5.15135 | -45.64802 | 2026-09-21 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0590972-af2c-3d24-a98b-0abe49c2f2c5 | -6.99853 | -42.20329 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9b6dc84-2054-3232-a71e-8b31ee630590 | -6.98905 | -42.20936 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5caa4002-d573-33e9-88b7-18e59f9474d0 | -4.33954 | -46.37488 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57035c60-c13b-323c-899d-20390e4a4fed | -6.88611 | -41.70342 | 2026-09-21 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 35450f51-83d6-3024-8fa3-52dadfba2f00 | -7.02802 | -42.07671 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4e551ab-65b7-362b-9b70-d0ff0ec871c3 | -6.44809 | -48.44616 | 2026-09-21 04:00:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f849a151-a33e-3152-9e61-a5a066e1f158 | -6.58017 | -42.55922 | 2026-09-21 04:00:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 949f5df7-cc05-3bb0-8c9b-3fc5216c627b | -8.38793 | -37.64838 | 2026-09-21 04:00:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bb47bf75-f468-3d6b-873c-50e51bbe9fe4 | -7.41581 | -44.77176 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 18821124-acac-306f-98a7-4a81d4b120c5 | -13.89837 | -48.57804 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aef0f717-e3be-3fac-a81e-0edc1f2bfbc8 | -13.28491 | -43.54747 | 2026-09-21 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 539af4e9-0c61-37f7-901f-77491ac2026d | -9.53792 | -45.39544 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b11b85c2-4e73-3eff-ab8e-6147488449d6 | -9.46664 | -45.39836 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc0b1a1f-a1ab-3c61-ab87-349bdeb96c58 | -11.0195 | -46.54608 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c13e5fa7-4d0d-3728-afc0-a21bd1d44f72 | -7.42951 | -44.77948 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a848c22-7afd-3b20-9626-980a5730a416 | -9.82453 | -48.44436 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1e6ed720-8738-3487-88ec-f71953741065 | -11.94295 | -46.50509 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a59ec4fa-dcf5-3f04-bfce-29cec85a6cc7 | -11.94349 | -46.50221 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43c9bba2-ca44-3776-9657-11d8f131b4bc | -10.73151 | -50.71316 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed77b437-14d8-391c-92b1-5bf2f79c5ae1 | -10.37617 | -48.92102 | 2026-09-21 04:02:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5503beef-95d2-3722-8407-1d623081b1c6 | -7.76262 | -44.82456 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62bbeb3f-dd7a-3001-afc5-7e99ed41c776 | -8.777 | -44.3016 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8199c102-0d73-3b0a-a174-56bb8d495f14 | -7.43542 | -44.78688 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b80b3bbc-9915-343e-8daf-758d4c51d25e | -13.17355 | -43.56484 | 2026-09-21 04:02:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 44f7d1f2-5061-3dd1-98d1-2698cb6ad025 | -11.09261 | -48.30578 | 2026-09-21 04:02:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5081664b-a1bc-3354-b9cf-59b5a11d2314 | -10.47795 | -50.29537 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 56ecd5c6-84d8-3475-a2d3-306954718991 | -10.4618 | -50.27437 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 26da90a4-2469-3279-828f-8b95ef8377dd | -10.46238 | -50.28302 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1d75c3d9-eb2d-3d5b-803e-c2d0ae8b6dc1 | -11.67525 | -43.41316 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14fffce5-2703-3fe8-94a6-cc5725500008 | -10.76665 | -50.82829 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37a81563-f0ca-39f3-8eaf-c70590a524c3 | -10.47544 | -50.28582 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6f480a7a-9a01-3616-bbd5-068ad9d3a617 | -8.30837 | -46.00046 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f43c232-70ed-3dc8-b787-9f631d1434fa | -9.76148 | -46.06041 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da2b9fed-cf8e-31a5-93eb-dee41f486892 | -10.47758 | -50.3306 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5d3b4918-6a20-3aeb-972e-40ab5951278d | -10.67956 | -48.71881 | 2026-09-21 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ce66024-320d-3907-8b99-284261a4d7f8 | -8.76207 | -44.27866 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67b8d6f6-ef09-380e-a9b7-76f4ee7b2300 | -13.03693 | -46.97107 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18e6e5af-6058-3754-ae1d-704071d3f1dc | -9.81858 | -48.41145 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a4a4e83-7eb0-3147-a1d8-1d437d9a94d6 | -10.76604 | -50.80515 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c52d880b-4d3e-3f45-a8d4-db5cb160b516 | -11.79274 | -46.8465 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2c7eef1-afb3-346b-b3c3-3c33de960cfe | -13.89916 | -48.57408 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92b01e22-d4a9-336c-9287-c6c4656439fc | -10.45833 | -50.29124 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 80c54e5e-4109-33d3-b161-c1bd86f1e4be | -13.90941 | -48.58071 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5313f899-6a57-34ab-98ac-56baed099b25 | -10.74474 | -50.79838 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90a7fd78-13db-389d-b5ac-9500cba28a60 | -9.97665 | -50.26644 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 63d214e2-2ca5-3ca8-ba29-80ab41d5d854 | -13.06996 | -50.62757 | 2026-09-21 04:02:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23d4264a-fcc1-3227-8214-6159a9038f78 | -10.69526 | -50.75522 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cc914ce-369a-3235-ab15-0879183060a9 | -12.02834 | -47.81622 | 2026-09-21 04:02:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec557eb7-7f42-31ae-9abd-9fe4b833bfed | -8.42516 | -45.85603 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e0ab7b7-94ab-3d39-8420-cd03a93671a9 | -11.95956 | -46.50006 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 385a2ad6-7165-3f53-a403-569f39df4395 | -10.39619 | -50.23965 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 391c62d7-8c64-3f65-8083-b00c11c6b6a8 | -10.78005 | -50.83125 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d355d14-f7d7-3427-9a0a-797a652cf8cb | -13.90397 | -48.57896 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d7df058-8959-3942-9e44-2ef167621f5a | -8.77875 | -44.29161 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aa8fc3c1-a057-36d8-a90d-4e85db4e88a4 | -9.0043 | -44.34381 | 2026-09-21 04:02:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0061b96f-2042-3fab-910d-bd2ed4c99c65 | -7.44305 | -44.7444 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0e7ac29-bfb3-3ccf-96b3-2d8d214b2c8b | -13.9425 | -47.8418 | 2026-09-21 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c325b0f7-97a4-38fe-b414-10d2a8781fd8 | -7.41792 | -44.78849 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dd2f902a-34d6-3745-8d29-d8197e2da3eb | -10.75507 | -46.31773 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a3cb360-701c-3b12-b9f4-5c0ac90d6198 | -9.46381 | -45.38641 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 5220f053-a198-397f-9f75-4cf4048d4d8d | -11.62666 | -47.78236 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3555072e-bc54-38b5-ac7d-271e49850f3a | -11.93398 | -46.49724 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0245f319-965b-394b-af09-eee5738bcf7e | -11.09821 | -48.30768 | 2026-09-21 04:02:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2761621-7b2f-3e36-8cad-0bc1b5900d74 | -8.76291 | -44.27396 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6a8db853-cedb-3769-98b4-9ba53958d706 | -12.3245 | -50.69937 | 2026-09-21 04:02:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73606300-c5ff-3e6b-a4e1-d9ff290f9311 | -11.79569 | -49.81126 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9329900c-4eff-307c-8e4c-675014a6c234 | -7.43133 | -44.76889 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| edd9256e-268b-3d71-afa3-24b606287adb | -7.41785 | -44.77306 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7e431b77-c898-33e9-9f0a-6335a8573ba6 | -8.83594 | -50.48637 | 2026-09-21 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4327959-82e5-3376-82b9-bae6d0342957 | -11.43754 | -47.29608 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c23b5c8a-2259-3a69-8089-ad07111600ce | -10.47656 | -50.28018 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 77c29877-b05a-3021-859d-c3407f2d1e77 | -7.40108 | -46.14866 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f76a935-45da-3fdb-9f29-a22618b166b0 | -10.38064 | -50.22337 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61649538-d308-3640-8d2f-b2e33c843be8 | -9.82452 | -48.41245 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a61394da-8655-3ced-bb8d-120df51186df | -7.44029 | -44.7877 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 232a9f2b-171f-3b29-ba51-20980c787f56 | -7.43246 | -44.77544 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dbe79514-6a62-3d8b-8ade-08290a7b1343 | -9.44989 | -45.42789 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 538c8e9d-9046-3ba3-8467-5478f87c1a77 | -9.75004 | -46.24019 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aae700e0-1035-33ee-a721-d94e6e8cf565 | -9.02923 | -44.92791 | 2026-09-21 04:02:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f9ab2ad-1fef-36cd-bd50-dadb30c6e9d1 | -10.69612 | -50.76287 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6df7ed43-dc34-35d3-a0c0-9c1b03be5145 | -9.4617 | -45.41845 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2733719e-1a06-3d31-b0be-3f99a3bfb966 | -11.62282 | -47.77918 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6431f84d-b203-320d-bbbc-f10209ee9e64 | -12.30086 | -50.68242 | 2026-09-21 04:02:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08ae3d7b-a1d4-32c6-83a5-ca62dbef3548 | -11.78886 | -46.83857 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0c5195a-3313-3cf0-8a25-9247f7e6f63a | -9.02951 | -44.92415 | 2026-09-21 04:02:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c222493c-4988-38a0-a606-5d330198e184 | -6.66691 | -50.89017 | 2026-09-21 04:02:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7c028c2-7a4f-3be1-9169-82148e03786e | -10.44503 | -50.26756 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5f89390b-c255-3676-bb7c-27b0ca834123 | -8.00954 | -44.81721 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7af350c-2cfc-33bf-bb8e-0fb0922a9450 | -11.79798 | -51.11472 | 2026-09-21 04:02:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13be0aaa-0686-3339-a1cc-5851f15e184d | -9.25441 | -46.1866 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
