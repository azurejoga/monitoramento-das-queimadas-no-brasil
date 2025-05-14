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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34b5d751-f8f4-35e0-9360-f2ba93ed55e2 | -10.00109 | -47.84726 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51faff32-6514-34f8-a790-3daec39ea5a2 | -6.95673 | -47.93199 | 2025-05-14 03:53:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e22a7f5-8dd5-30f2-b9a9-0df915e65828 | -10.00678 | -47.84515 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a72ed593-4949-3d95-b79b-22009cb62a8c | -11.79986 | -46.64404 | 2025-05-14 03:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cab10a73-656c-319b-a936-1779ff483d5b | -11.39551 | -43.14506 | 2025-05-14 03:53:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0927c3e-cb50-34e5-ab53-51eeb53a7f7d | -11.40455 | -48.7062 | 2025-05-14 03:53:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de8edd8c-a93b-3cfc-a5d6-ce6794ffe462 | -8.06181 | -47.12558 | 2025-05-14 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35241ce5-e367-3be5-9a79-5bc3d5f89520 | -9.46922 | -40.31398 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ccd24f23-1bca-3b4d-ba1f-548c06db25e3 | -9.472 | -40.31813 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| aef1df83-b27d-32f0-ab60-2c7049dcb1cb | -9.4771 | -40.30787 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9da8d6a9-be52-38b9-b084-fb9c653d1c0c | -9.47652 | -40.31148 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eb368098-cdef-3450-8a79-c8fd93e6db2e | -12.15634 | -48.01398 | 2025-05-14 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5a3e398-1f39-3eab-ad47-766baa53cc9b | -11.79083 | -47.37789 | 2025-05-14 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 863e158d-0ab1-38e5-a452-b1eb2c142752 | -8.79958 | -49.81598 | 2025-05-14 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c02a564-353b-397f-b9a6-a57145454f36 | -9.46864 | -40.31758 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32028951-ab7d-3544-8410-5b0553d77479 | -10.00165 | -47.8442 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 147bdd49-4cf6-30c4-b58a-5c0b3148faf6 | -9.47026 | -40.32896 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0ac4953d-e567-39d0-8144-6a1beaf80ac0 | -11.69144 | -48.81898 | 2025-05-14 03:53:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79bad947-094c-34a0-ae86-d0a7de88ca6f | -11.62927 | -48.12244 | 2025-05-14 03:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 770c7a73-f0bd-3f28-aed4-2b4021b5306e | -12.35039 | -44.81847 | 2025-05-14 03:53:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84fe5f06-a3d9-349d-a4fc-64cc1ea299ae | -9.47594 | -40.31508 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f7c179c-ab7f-382e-b4bd-60e6ea82e3b1 | -11.40824 | -48.70805 | 2025-05-14 03:53:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27ff0476-ba80-3a11-9877-fd7aaa4fe396 | -9.47038 | -40.30677 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 84e48b73-b2bb-3b13-9972-293fe390c5b5 | -7.24901 | -47.04184 | 2025-05-14 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5848c14e-1f3e-35da-9067-9c827f254d5f | -12.27704 | -44.59639 | 2025-05-14 03:53:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 276eb718-f662-3640-8445-2a37bb3e0b27 | -10.45432 | -49.07803 | 2025-05-14 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d7eb578-09e3-3118-a99d-f0724a258a74 | -9.99651 | -47.84329 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 607efbf2-16c1-342f-9e2f-7da2574fd12b | -11.79481 | -44.27155 | 2025-05-14 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73b017ef-e967-3862-aa75-ac2dc874712f | -9.4698 | -40.31038 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a52f88c5-a9df-3201-bb2d-c26a839c91db | -9.47258 | -40.31453 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 98f10df9-a66f-3f0f-a9eb-95596beba11f | -9.47316 | -40.31093 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b5a85c7f-733f-3930-a8ea-d8c4da5eb80b | -12.49288 | -44.49851 | 2025-05-14 03:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba492782-9054-3788-af22-8a6d5fe81eef | -11.57614 | -47.60974 | 2025-05-14 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ce94dd6-5665-32ec-822d-bb25c75e2e9a | -10.08976 | -46.55219 | 2025-05-14 03:53:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8a3a85e-99db-32f0-86a2-09ef413b48f8 | -9.46748 | -40.3248 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dd2be80b-5144-3b2d-9049-56d3326931ce | -9.48046 | -40.30841 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5dacf89-71f7-3b71-b854-217af48fe524 | -12.1508 | -48.01591 | 2025-05-14 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46f33644-fcbc-3810-9ed0-94220dfe6962 | -9.46365 | -40.30568 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e478473f-d4e7-3089-a771-36a13640aabb | -9.26693 | -50.21405 | 2025-05-14 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbd98e2b-ea34-3d7e-af32-6974e67232da | -9.48267 | -40.31618 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6e535efb-4eae-3cd5-a429-1b6ee189b3bb | -9.47989 | -40.31203 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7e2b46a-9c95-30b0-8da2-d969e4083e4d | -11.78803 | -47.36622 | 2025-05-14 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c27f53cb-086d-3722-8d90-3fedcdb71474 | -9.46528 | -40.31703 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d538d9b9-17eb-3912-b7a0-0cacaa17e537 | -12.15135 | -48.01298 | 2025-05-14 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46c2f33e-2266-3f6d-a3ce-b8b7d30c52cd | -11.16565 | -48.68058 | 2025-05-14 03:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 618b14f6-2cbf-3ace-abf4-b16c64782170 | -9.84196 | -44.68494 | 2025-05-14 03:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cf35697-e483-398a-b7d4-278854dd78b3 | -9.47421 | -40.3259 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c4894c9c-9f1e-3437-8c1e-595b159aca1d | -9.47374 | -40.30732 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e5d7274a-f5d9-3fec-a109-7282fe021510 | -9.47873 | -40.31924 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2ace15b2-c166-38f8-8e3c-1da81900fa23 | -10.6601 | -44.49097 | 2025-05-14 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f12977e-04c2-3488-ac75-64efde5b5383 | -11.79284 | -47.36713 | 2025-05-14 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46526c93-5071-38d2-a2da-04aa365694f5 | -11.40294 | -48.70704 | 2025-05-14 03:53:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f362d86f-9d7b-3f0a-b8e0-e9504e19619e | -9.47536 | -40.31868 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 65e8cbd8-210a-3c45-823a-8cea202ff728 | -8.56734 | -38.04981 | 2025-05-14 03:53:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 085aaea2-6124-3522-bed9-9fa3ec04942c | -9.47757 | -40.32645 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 477326ad-6a13-3a39-9094-16d7f9120857 | -9.57315 | -49.1139 | 2025-05-14 03:53:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ed405ff-37ce-376c-9919-b8b801982d5e | -9.48209 | -40.31979 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f02563f-33ba-3811-98d5-dea4c9fdac2b | -11.79183 | -47.37251 | 2025-05-14 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9a3e7f0f-6177-329b-9c35-89991204178e | -7.40812 | -43.45452 | 2025-05-14 03:53:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c8206ca-a2f3-3610-9e6a-c8aee0d28173 | -11.80267 | -44.27296 | 2025-05-14 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a758f6ad-2312-3bbc-8de7-cf4aa0b09f72 | -11.55438 | -47.6174 | 2025-05-14 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb412cde-79d7-3e0a-9434-a4e3071df14b | -10.18346 | -48.03125 | 2025-05-14 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15ab9cc0-b985-34aa-9c8c-125a2dca043e | -13.04733 | -43.48575 | 2025-05-14 03:53:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33f70c3e-ec2e-30d0-bfb7-0f0b18601157 | -9.47478 | -40.32229 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 39310399-3ce5-3327-aefd-10799fe27cea | -9.46806 | -40.32119 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 31147bfa-9717-3780-9087-2512d8465013 | -11.7907 | -46.64228 | 2025-05-14 03:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62199a0d-78c5-3996-96d2-fc7e02b600eb | -10.48082 | -49.14619 | 2025-05-14 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03505e74-f6fc-316e-92a4-df816fb808c7 | -10.44883 | -49.07682 | 2025-05-14 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fd88e12-698c-35df-b872-1f35f5e5a6ca | -9.47815 | -40.32284 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 16758394-49ac-3e76-97b5-47255f41b57f | -11.79617 | -46.64048 | 2025-05-14 03:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67478c99-04c4-32a9-a832-fd25984f4ffb | -10.00279 | -47.83802 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f04a6675-9d43-3eaf-8414-356ac768f718 | -11.80177 | -44.27806 | 2025-05-14 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b960c20-3ed8-3b78-b0ad-3224f773b48a | -9.47084 | -40.32535 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a8f837e0-d38d-3748-aa11-fdb00459bbea | -12.49544 | -44.50073 | 2025-05-14 03:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9aebacb-a626-354c-b225-2422162507b8 | -11.55546 | -47.61163 | 2025-05-14 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9a7367f-ca9d-337b-81d9-3cf98ad032b2 | -10.00735 | -47.84203 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e555986-ebed-3768-b904-b6da2f919f25 | -9.57387 | -49.11003 | 2025-05-14 03:53:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95a7c281-fb27-3e35-913f-fc3aa8340df9 | -9.46249 | -40.31288 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e98f3bb2-9137-3a39-9eb2-f059caa2b25c | -9.4669 | -40.32841 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8a6e5517-bbeb-35cc-9495-b19580e70e79 | -11.63434 | -48.12344 | 2025-05-14 03:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a12c068-d625-38d1-b1ed-018b8edea178 | -7.80413 | -49.33223 | 2025-05-14 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76739f88-abcd-3980-a339-fb9bbd098298 | -10.00222 | -47.84111 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37b795e0-a9d6-38bf-9a29-eaed4606ab4d | -11.79784 | -44.27735 | 2025-05-14 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7388dd06-ef20-3d99-a453-064ce9f91aa3 | -11.29011 | -41.86321 | 2025-05-14 03:53:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 15b21463-590c-3421-a2f9-d799ff9dee76 | -12.49452 | -44.50588 | 2025-05-14 03:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6759292-37d2-39c7-b307-d32245b9bbe5 | -11.79158 | -46.63966 | 2025-05-14 03:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 583e5ba4-2172-3186-bbfb-6d8aa8df2c9c | -9.45855 | -40.31594 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e9df9ba-0c1c-3cc6-b0bb-e7bc75d50742 | -6.91055 | -47.18637 | 2025-05-14 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eba218cc-ca92-30ed-b8c8-8c7b1dfc6ff3 | -9.46644 | -40.30983 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d2123603-9663-3509-ab00-e0625e163945 | -11.79874 | -44.27225 | 2025-05-14 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d947c0f8-d406-342b-a811-2a1ef0c50c79 | -9.47931 | -40.31563 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8371cce6-b506-3683-a097-aa8e8651db5d | -7.24848 | -47.04489 | 2025-05-14 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b81dfaba-a6d1-3fb8-b891-9dcb2aa3ed30 | -13.04656 | -43.49021 | 2025-05-14 03:53:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dc500c3-1b27-3946-a69e-f77f51f91e74 | -9.46702 | -40.30623 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e37ffc8d-440b-37e0-b357-4d93328885ed | -9.4647 | -40.32064 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 43480406-b386-39a1-89b6-f7167f739141 | -9.75307 | -36.9793 | 2025-05-14 03:53:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2bd6932f-36a5-312a-a7c0-1fcbaa8cfd4e | -12.49505 | -44.50955 | 2025-05-14 03:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67aae942-d8cc-3767-b2c2-8bd558e8fb43 | -11.6908 | -48.82233 | 2025-05-14 03:53:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 670c26fb-93b5-3df7-ac61-1ad94a4375bb | -9.47142 | -40.32174 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f34c4017-eb86-3f00-8ba1-fdde7d4b6bd8 | -10.18405 | -48.02805 | 2025-05-14 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
