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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6a8dcd7-47f4-3dd9-b1d7-aacbe0c92a63 | -7.81018 | -46.22179 | 2024-12-09 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44fc2377-2040-3ab5-b3a1-44b7a82dda01 | -10.38227 | -51.99887 | 2024-12-09 03:55:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f25359b3-d3b5-3887-94f5-e430c5832e37 | -13.26684 | -51.09674 | 2024-12-09 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 518ce809-20e3-3e85-9901-9cec736ce2a9 | -13.26593 | -51.1012 | 2024-12-09 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1dc8563-b67c-3ef9-9f19-0812e7fdffa0 | -3.29041 | -39.24613 | 2024-12-09 03:55:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 394deaec-1cb0-344c-9e25-829bbabf7b49 | -2.03146 | -46.66741 | 2024-12-09 03:55:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb8326d9-d81e-3f29-aae3-42776e8e5df8 | -12.36416 | -45.93318 | 2024-12-09 03:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccb1f3e6-398e-3836-81ed-4a1c75c8fcba | -14.97512 | -44.41898 | 2024-12-09 03:55:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 662ffe58-d13b-3f14-879c-84866c891dc6 | -1.64622 | -45.91034 | 2024-12-09 03:55:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47641dbf-613c-3901-b2bf-b2b6e648ddab | -2.91097 | -48.0214 | 2024-12-09 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a98280bf-25a6-3b9f-b631-c8cdc8663eb2 | -8.09199 | -46.03882 | 2024-12-09 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| feda49c8-7763-31f5-808f-0834d7134a80 | -3.84195 | -41.56931 | 2024-12-09 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1f91ff1-75de-3e44-9b50-3c1895880446 | -14.97973 | -44.41494 | 2024-12-09 03:55:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d455fb3-f195-39d2-9648-33de46ada2bb | -2.74558 | -45.71595 | 2024-12-09 03:55:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47c3fb85-b455-3bb2-92f7-84fa1ca4485d | -15.97272 | -42.25037 | 2024-12-09 03:55:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e206dcf-551b-3031-96f5-1873172b667b | -4.24712 | -41.93098 | 2024-12-09 03:55:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 19f03f1d-3b99-3efb-a9d2-4fc83f08f4d4 | -2.91166 | -48.01722 | 2024-12-09 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 296c2f01-27e4-3b73-8d2e-e371e78ca713 | -12.86792 | -43.73434 | 2024-12-09 03:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9b78331-1d51-3a81-af55-b00c23479b24 | -9.36652 | -35.92881 | 2024-12-09 03:55:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5a8dcb34-0b77-373f-94fb-6a070851f17b | -10.36506 | -40.55251 | 2024-12-09 03:55:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 56cae136-ff72-33fd-9312-d031a2f0f5db | -13.48366 | -46.95559 | 2024-12-09 03:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da45ee4-6e65-3f91-a22f-4d8fb3df102d | -14.97595 | -44.41425 | 2024-12-09 03:55:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 967564f4-3350-3a30-bd7a-8ac59e6f46d1 | -12.68211 | -46.76023 | 2024-12-09 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd9bb2e9-153b-36b7-9331-318d9d46444b | -12.28434 | -45.49797 | 2024-12-09 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 63e1f59e-87a1-39b4-b532-6298b6d06680 | -14.01187 | -44.19058 | 2024-12-09 03:55:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 591ada6b-713f-384e-a8bb-f4a9d5bc9fce | -8.15379 | -49.14522 | 2024-12-09 03:55:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 260e4ce7-5a3f-30b6-be2a-eb28d18a35d7 | -2.90194 | -40.43972 | 2024-12-09 03:55:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| be195762-1746-31ac-b81f-f9f1f0214721 | -2.4701 | -47.08398 | 2024-12-09 03:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7600ef2f-71cd-3b01-a1b8-fa64567295cf | -1.64672 | -45.90725 | 2024-12-09 03:55:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02d876c4-da9d-3b55-956f-c8eeb41ab5c9 | -13.26775 | -51.09229 | 2024-12-09 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 504bf208-a55d-3764-9d02-579c53dbbcf3 | -4.57958 | -38.55742 | 2024-12-09 03:55:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3d7cb4e4-955b-30c3-9d2b-7e3b8db475d8 | -12.35179 | -38.14272 | 2024-12-09 03:55:00 | NPP-375D | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0a9f7cde-ebbc-3431-81cb-6ef3ace633dd | -2.90443 | -48.02457 | 2024-12-09 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e38f72bb-bcce-36fe-ba80-317e797c4b6f | -10.55798 | -36.96479 | 2024-12-09 03:55:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1584e956-3dfa-3e94-a6f0-b95301390f03 | -14.1996 | -44.72142 | 2024-12-09 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f83296d8-b386-3de9-872c-ac4917e3a489 | -2.14815 | -48.03954 | 2024-12-09 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9e8cbe62-ef98-389c-a65e-169db80ced26 | -12.40366 | -49.67743 | 2024-12-09 03:55:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1b91c62-f5fa-3e56-b62b-c2cba1471ad7 | -7.80926 | -46.22702 | 2024-12-09 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7c5f869-012f-359e-9747-069a926a2803 | -2.46951 | -47.08764 | 2024-12-09 03:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8721274b-db31-3bfc-a9df-f7f2241beea9 | -10.55857 | -36.96088 | 2024-12-09 03:55:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 31cbb2ba-d87b-3195-86b8-b34e3090b3ef | -13.2618 | -51.09099 | 2024-12-09 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 510f7764-e3b2-32c9-9455-8fda82b02684 | -14.20016 | -44.71841 | 2024-12-09 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc5576be-50de-3ae7-8de0-2ef1f505e2b6 | -12.40511 | -49.67627 | 2024-12-09 03:55:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66c39d31-d748-306e-8233-2df866e1d5a3 | -2.90513 | -48.0204 | 2024-12-09 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ebbb7bc-1528-33b6-9f03-9cca386e995a | -12.35173 | -38.14204 | 2024-12-09 03:55:00 | NPP-375D | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b448a626-3203-3565-9439-3b56afc0935f | -3.00015 | -40.28272 | 2024-12-09 03:55:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1ca25e6-17c3-38b7-b9cd-e7bab7c26518 | -2.90008 | -40.44083 | 2024-12-09 03:55:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 532100b2-88a8-34b6-8ef0-84c96b8a130a | -12.28364 | -45.50191 | 2024-12-09 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1ea414e-a6c3-362e-a8d0-067ab7b098e2 | -1.6509 | -45.9143 | 2024-12-09 03:55:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee754142-70ea-3693-8a1b-f6a16c7aa994 | -2.14745 | -48.04379 | 2024-12-09 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 714da9b3-fc7d-3f77-a998-3ce9d9ff1c4d | -8.7871 | -48.74866 | 2024-12-09 03:55:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03889fa7-793a-3cb3-9fa4-b908cbd80bf1 | -12.28013 | -45.49714 | 2024-12-09 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 145bc342-7396-3c52-a79e-36535425e3f1 | -2.03689 | -46.66824 | 2024-12-09 03:55:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a55fb278-9213-3368-a596-b49e65b47991 | -10.38113 | -52.00457 | 2024-12-09 03:55:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f82238df-e578-3f23-914e-ccc360b887d4 | -2.82889 | -40.40467 | 2024-12-09 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d312970-5e55-37a7-83dd-ea5740b258cf | -12.40439 | -49.68002 | 2024-12-09 03:55:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff15009c-6980-3253-9e7a-06dbbe50aaee | -1.47961 | -46.1459 | 2024-12-09 03:55:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d2fd995-dfe3-3b8b-8c52-13ab380a32f0 | -12.3687 | -45.93654 | 2024-12-09 03:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30e4a37f-b33d-32d2-8ada-7a02dc8ba6bb | -5.28102 | -35.48176 | 2024-12-09 03:55:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b2bd0c4-7baa-31da-8218-16aacfae1dff | -1.64722 | -45.90416 | 2024-12-09 03:55:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0217fda6-eee1-329a-8c2b-7a73c1c0bc48 | -3.85821 | -40.44435 | 2024-12-09 03:55:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 351da4e7-a635-3cf0-8088-7edad3e8771b | -12.27943 | -45.50108 | 2024-12-09 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290cad3b-f265-3d1f-bb13-fadb4a989179 | -3.35789 | -45.51561 | 2024-12-09 03:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1247c5d8-3785-33aa-8284-b645db06e079 | -2.9966 | -40.28216 | 2024-12-09 03:55:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f5d69a2-4422-3c4b-9735-a24aaacde821 | -16.34973 | -43.69501 | 2024-12-09 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0cb57da-0ae5-351a-b323-ccce376c2814 | -15.8387 | -45.16994 | 2024-12-09 03:57:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f469f272-924d-3122-a9b9-e67c461e7b3a | -17.46397 | -47.01303 | 2024-12-09 03:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 642c6688-f83e-3c1f-856b-627041d4a702 | -19.37248 | -43.74482 | 2024-12-09 03:57:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9036db55-d1be-3c10-941e-e1e3cf16d6cc | -20.55003 | -43.51114 | 2024-12-09 03:57:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3bc5faeb-60a5-3e48-a6aa-6d092fdc40a6 | -16.54301 | -52.45784 | 2024-12-09 03:57:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9399d97b-9f60-3f1e-9ef3-f8621b9f756e | -18.08042 | -45.28364 | 2024-12-09 03:57:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72731869-67fd-34b3-be90-de6f1f4c7564 | -19.36831 | -43.74821 | 2024-12-09 03:57:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b57e859-661c-3406-8cca-7b70bb4b3443 | -17.14783 | -43.2156 | 2024-12-09 03:57:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63b891a1-280f-39a0-9420-40e3de2553e6 | -17.46167 | -47.00958 | 2024-12-09 03:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8b7b40a-5207-326b-8a8d-a9c21568fe4b | -20.41617 | -43.5551 | 2024-12-09 03:57:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 38fcf264-2337-3cd8-a6f4-0e3889cd799c | -17.15131 | -43.21625 | 2024-12-09 03:57:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09823e56-31d1-365c-88c1-25e59754692c | -20.90015 | -43.81881 | 2024-12-09 03:57:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd61aa7f-3c59-3055-8524-3de7caed81ac | -18.30789 | -47.19587 | 2024-12-09 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f189210d-965e-3fcf-a588-96fa78c34f4b | -19.30042 | -45.54809 | 2024-12-09 03:57:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6565d187-c43d-3408-aa6c-8d34ef262326 | -21.33237 | -44.74659 | 2024-12-09 03:57:00 | NPP-375D | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 70523c77-c9ad-3d6d-a491-546416194875 | -19.36901 | -43.74416 | 2024-12-09 03:57:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6320b52-8aca-3413-bd12-0fbbd8105870 | -19.53914 | -44.07732 | 2024-12-09 03:57:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9b2b4e6-84d5-3eaa-a858-2f2decb622cb | -19.06154 | -43.61636 | 2024-12-09 03:57:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a658d546-cfe2-35a8-be55-050fc0987e31 | -20.41684 | -43.55116 | 2024-12-09 03:57:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e0d88130-464b-3256-8d53-b339dd2174fc | -15.56745 | -47.85686 | 2024-12-09 03:57:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fbba5fb-b46a-33b4-a126-542e9bb311b4 | -20.55067 | -43.50728 | 2024-12-09 03:57:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1ac00a72-2a27-3b7a-9777-52586e48a737 | -20.81127 | -44.56637 | 2024-12-09 03:57:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1395acda-bb81-3d32-9435-33ad46aa39b4 | -18.03901 | -39.92572 | 2024-12-09 03:57:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ecafb948-e953-3669-ad40-2bf2c5a49d7a | -17.46743 | -47.01797 | 2024-12-09 03:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102f14e6-b3aa-35b5-9a42-f23c1f95c77c | -17.38737 | -42.65839 | 2024-12-09 03:57:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3de47107-a16d-3589-b8ff-1ae116a25cf2 | -17.78166 | -42.8098 | 2024-12-09 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a006273-f653-3665-a7f3-037215f48197 | -18.30701 | -47.19433 | 2024-12-09 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d06ebd3-7261-3813-82da-ecd441c0e1ab | -20.59187 | -42.12178 | 2024-12-09 03:57:00 | NPP-375D | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 782dffdf-8035-3153-8e71-7b15752280f8 | -18.3044 | -47.19101 | 2024-12-09 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c906cac-3646-38d0-b45a-d40f398e1b8f | -21.91117 | -42.26349 | 2024-12-09 03:57:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d7db35c3-1bae-3c61-8f82-c51d6bd1d156 | -21.18007 | -43.98147 | 2024-12-09 03:57:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1fc3273a-9244-388d-8bc9-5340b9393702 | -17.78198 | -42.81059 | 2024-12-09 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 969f934e-2f18-3094-84cb-20d0b8c606f1 | -18.30865 | -47.19183 | 2024-12-09 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55bd910a-0eb6-397c-8d9f-2740c13ebd80 | -19.37178 | -43.74888 | 2024-12-09 03:57:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe24ddb3-fd96-3578-834e-242954f8f318 | -20.76332 | -46.7718 | 2024-12-09 03:57:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
