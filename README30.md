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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcdb517d-ed03-3ad2-8d0c-d8a0994e0af4 | -7.45396 | -44.39726 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6e59209-851b-34b9-9b9e-392ff94affea | -8.95608 | -46.07502 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57afa1d3-16d4-3652-893e-ca9dc90aa3c0 | -11.41946 | -43.70891 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e5778ae-490b-3bff-a9e9-d06c9a7a497a | -5.28925 | -48.13151 | 2025-09-12 04:04:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3568233-b126-387a-85b7-0a53cb4e3bd3 | -8.89529 | -49.92982 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 75c7709c-6e94-3787-bc5a-1bf02f768bb6 | -11.94198 | -44.30575 | 2025-09-12 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd22af5f-727a-3c99-b9d4-6f0c5bd4b8fc | -9.97074 | -50.38386 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdf4c3ad-8a61-30ab-9f63-83c78e1bcc4f | -9.78042 | -47.85516 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e2f57c0-3b26-3101-8458-a98fd0b6896c | -6.54096 | -43.70799 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f655c886-2b47-3c2f-8e4c-7ef22e7c80fa | -8.40363 | -47.27722 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a426e75a-f874-3e35-9bec-8a8d802a25b2 | -5.95152 | -42.78539 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d5ca891-ea11-3807-9155-b8a4dda4fc25 | -9.0346 | -47.08282 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1987d706-0aab-3c63-b824-655d230d6f7f | -9.11469 | -46.96543 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dd1e0cc-ffc4-3ef3-b77b-7c2cdf0e1065 | -8.4801 | -47.27159 | 2025-09-12 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 092dfc64-48fe-3394-aab4-5373b74e90bd | -7.78718 | -50.7776 | 2025-09-12 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68097322-fbaa-31ad-96f9-30aabb4a702a | -7.56151 | -44.37846 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8598d385-7d3a-338b-ae41-c917c30c8516 | -10.21632 | -46.23564 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37fc69f0-b884-3622-810b-37d8abedb770 | -6.33187 | -53.46498 | 2025-09-12 04:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 067242c9-8445-3781-b5df-a585750a8a6b | -11.66905 | -46.5901 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e0be64c-8997-30e0-b72b-2305a49fc0e0 | -4.49076 | -48.11758 | 2025-09-12 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40a2b3bf-b03d-3790-885d-fa1686129ac1 | -9.93942 | -42.33068 | 2025-09-12 04:04:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 113e48c4-03d8-31fd-a87f-b5065e8128f1 | -6.68315 | -44.13669 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0491510-8ea7-3980-b711-6279e62d9b9f | -6.25126 | -43.4287 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67286184-096a-3eb3-bc57-5463a85810d3 | -8.33482 | -45.41484 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78a96f29-76c5-3d45-94cf-81fec2c87567 | -6.2957 | -44.23225 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 918afcc5-4668-3486-ab70-692277953b7d | -10.08606 | -48.17273 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a56e21e9-2b84-3bdf-978f-f7c9b95d15e4 | -9.52242 | -54.63993 | 2025-09-12 04:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7bbc08d-b731-37e0-b47f-f37cca94c65f | -6.68923 | -44.12349 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84908b77-e2ec-3d85-a946-2f87908ba8f1 | -5.95085 | -42.78947 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc3307ef-c00c-3483-a493-7fb343b02c81 | -9.07076 | -46.95541 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9d64dc58-55fd-3d04-ab14-541927f0cf4f | -11.67562 | -46.5631 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb2981b9-9d02-3a7b-ab2a-8f5cdf7c3698 | -10.74385 | -48.18034 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e918b8fe-3dad-3ef2-b7b0-55b0e7abb68f | -10.53507 | -51.53432 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5c7f721b-bcae-3218-aab2-582358e2257d | -7.44849 | -44.4063 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70c4484a-8a00-3b9b-8613-158d0ff5b730 | -12.13084 | -44.84163 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5e93b25-9360-37fd-8244-8ff553462adf | -8.18867 | -46.10749 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0563ddfc-ba84-3cef-ab70-2b86023d64d1 | -9.71763 | -46.88712 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3368cb7e-d8e5-3478-90bd-94733cf77699 | -7.43504 | -44.98459 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 891eac84-3093-3833-8f85-37ec2b9a5280 | -5.40472 | -45.9326 | 2025-09-12 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5885551-fd55-31b5-a793-933de64c6243 | -6.9449 | -44.7812 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff8484df-7d7d-36b0-95b8-72c3ce5a2e77 | -8.47471 | -47.27544 | 2025-09-12 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82a8f27f-7507-348d-b91e-0a881c51893c | -8.88732 | -49.93556 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8473e0a6-0b66-39ff-844b-235f5a5ae06b | -3.83342 | -48.95287 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64dbf62c-83f1-3db0-904e-7697aea24aa6 | -11.88943 | -41.2771 | 2025-09-12 04:04:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6e25425-a6ee-31c1-95ac-a5c1e25d7cb3 | -10.42505 | -50.61315 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f9caf8c0-871f-31e1-a0a1-a44308bf3a7a | -11.37373 | -43.50983 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af2803c4-e364-37f2-ad95-5a98d09fd421 | -6.33103 | -44.84423 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 285b07d7-7954-3716-8779-96408dcc4ee5 | -6.45003 | -43.58047 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c713f9f8-b68d-34fa-af21-324088f78399 | -6.83121 | -45.65847 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f1c4ca58-0f66-3f8c-ac66-e99ab210aed7 | -6.10145 | -44.9262 | 2025-09-12 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c836e15-6417-35f3-9a5c-fa517b28ffaa | -11.49569 | -43.64376 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5458df7e-be1a-3aa6-80ab-f3e1f4868bc7 | -10.70554 | -48.62772 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 82c7687e-9579-35a5-8595-5679a6a4aba6 | -10.53759 | -51.52107 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d884cccf-e126-38c1-81bd-e5aa899aee6e | -5.08241 | -41.15454 | 2025-09-12 04:04:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9329ae58-228e-3446-9443-8cfd486f2841 | -5.6582 | -45.95017 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9874962-306a-397b-9107-c7fab3ca0779 | -9.0082 | -46.12271 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4222e126-83d8-3e82-8c1b-58665204d6bf | -9.07797 | -50.49776 | 2025-09-12 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e72bb76-e869-3fa4-ace8-fa8f5f832f6c | -9.8592 | -43.12464 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66e2b269-3c14-3899-ac05-fcc44a3df5ff | -8.87685 | -49.54125 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4daa835c-9747-329d-acbb-edd0c51c94a3 | -9.07098 | -50.50412 | 2025-09-12 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fceca3d-cd7a-3308-84cf-645775f23d83 | -11.43396 | -48.56339 | 2025-09-12 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9590399-85a8-3f08-b925-b20c177eca65 | -8.43152 | -47.25321 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbb028e5-5cb5-33ec-98ab-526c8a8250b3 | -10.41852 | -49.99602 | 2025-09-12 04:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcbb0a5b-3473-3fe4-bb52-c2dcf202faf6 | -7.91079 | -44.87439 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 519a38fa-7f06-340c-abfd-39581046c93c | -8.94068 | -46.11209 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bfe2230-803d-3283-844d-da089a61b5a4 | -6.18488 | -42.75005 | 2025-09-12 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 84f83e66-d34b-3b09-a26a-5170d1f9de6b | -9.7285 | -51.00577 | 2025-09-12 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e75ab5f4-4806-32ab-b71a-47fc458d43da | -9.6815 | -47.53863 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25102a8a-a9dd-3f9e-8218-caef274a2990 | -10.67263 | -48.59688 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e7cf09ca-00d4-3f81-ab7f-341f2a4b14c2 | -9.03827 | -47.08814 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79e20e02-6bd2-3029-8365-6823dfc736fb | -9.06505 | -47.04036 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 20afbf7b-f340-3df6-b411-265c81cdc523 | -9.7192 | -48.30748 | 2025-09-12 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1f5d1543-988d-3c42-b90e-023851dc66fa | -6.9727 | -44.786 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78d1ab7d-eefa-342f-af80-8e682de9a8fe | -10.55515 | -51.49221 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5c04af7-a3df-334e-8840-da2f6b3db62c | -5.4255 | -42.8294 | 2025-09-12 04:04:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 73243789-1868-3e8e-abe0-2c9f73db7d92 | -6.31421 | -43.43909 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52219723-37f8-36e9-9223-c4043b5490ee | -9.99584 | -51.72382 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48a89f0e-3ddb-3de0-9634-e93bbe69115b | -9.04849 | -47.05621 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e126505b-86b2-3cb3-be9f-f886a05f4d65 | -9.0554 | -47.04305 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2b6cb7f-f6aa-3e3f-8c66-d0aa05933357 | -7.07261 | -43.90246 | 2025-09-12 04:04:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b85f5119-bb53-3785-a954-72489f1ecde4 | -10.77311 | -45.99699 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6fc63e1-4a59-3437-8afc-a94038716be7 | -11.66601 | -46.61626 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28811af8-7d0c-30a8-bf0a-723354e073a3 | -6.76732 | -41.59994 | 2025-09-12 04:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2db6eec-3420-37ac-b4bd-375588e8c4db | -6.34314 | -43.03567 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb39ff4f-ede5-30b4-953e-36d53170c7e8 | -6.24661 | -44.80212 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a5f4af3-ff68-3d4b-b0bf-e0f65c473bde | -8.36586 | -44.83773 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd923025-43bc-3d5e-b6f6-5cf03c6e43c6 | -6.59258 | -41.44811 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1f5ad38-4cb0-3400-abe8-0cc147034f51 | -6.67462 | -44.15241 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0bec3863-2141-3f62-a58f-7a8839e133eb | -11.1385 | -45.24351 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3fcc8c9b-977a-324f-9f71-5c1ec1e8c85c | -9.04152 | -47.06969 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e86bc187-ff8a-32ba-847a-2af1b65747c0 | -10.54092 | -51.5354 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 582bd4f8-3e5f-3e1c-bf6d-39db58aa7a2c | -6.15655 | -47.27521 | 2025-09-12 04:04:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 822515f2-49c7-34a4-a2c8-7b9b41a02ffd | -10.56038 | -43.66175 | 2025-09-12 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba60f656-349f-3f4b-9808-df8a0dac8376 | -5.27408 | -49.29541 | 2025-09-12 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4450c0b6-6bf6-37cc-b88a-0c764bd90beb | -7.29981 | -44.38892 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05775aa0-cec6-3981-a909-26822f99d81f | -10.68336 | -48.6669 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30cc6794-9f03-3b07-8137-c086c218c26d | -8.57731 | -51.35461 | 2025-09-12 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9678ec24-7f5e-34a2-83fb-222a0f31aa88 | -11.14493 | -45.23655 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a697c52a-726c-3e84-b03b-76b0acf11f7b | -9.77974 | -47.38081 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12ebe148-7da9-3e84-bcbc-cbe425de4149 | -6.68852 | -44.12788 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README31.md)
