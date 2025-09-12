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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6229eaf-9a0c-3f27-8f5e-607f4e5ee4e4 | -12.10651 | -37.97866 | 2025-09-12 04:25:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| d8e51433-c308-38d9-bb22-4c4d1e5ffca1 | -7.07498 | -44.14812 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 838a8705-d93c-3296-934c-8043b793a457 | -12.50639 | -44.69767 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9aaf89d6-8579-3c20-ae5e-b28b03607022 | -10.53072 | -51.5179 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ec49eaa3-1cea-34e1-b642-c012fef2a7b2 | -7.6947 | -44.69393 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a25726ff-1a2a-30f6-ac81-21c55269fe0b | -8.16207 | -46.10832 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcb30752-ab62-3dac-8759-f80afeea91c1 | -10.78881 | -47.26381 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4ba18f9-91f9-3bfa-a969-2bb9dfddb2b8 | -9.6697 | -47.55296 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b88525aa-5cf1-34d5-9cb8-53ac8906ab7c | -9.06651 | -46.57633 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81bc8d22-d0c5-3fc5-938f-b38844b74313 | -8.06847 | -52.32018 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a68b1828-dd36-3803-bbc7-1268a3f59daa | -12.24594 | -46.7557 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11869d18-c1c3-3270-8f85-c64ad7adcbb7 | -9.01896 | -46.12074 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 700b1199-b2fa-3fa3-b9c3-160f6e4ee384 | -6.14783 | -53.687 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed4ebef5-183f-3861-aed3-6426e6d0a9c2 | -6.56915 | -44.13169 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61c4ef74-2e7e-31e7-92a0-bd299c146d60 | -11.08239 | -48.40771 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10743dbc-f4cb-35a8-a069-a909e399c3ad | -11.43359 | -48.56479 | 2025-09-12 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c7f82d6-cccb-3e7a-b63a-aade0bd87f8a | -11.53366 | -50.41047 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ece40c54-0471-3c26-b197-070518469c14 | -7.32312 | -49.63764 | 2025-09-12 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 946f91f7-6edd-3228-a0c9-a86727128d52 | -10.00259 | -51.73328 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c78e0d88-e5b5-3466-b6e8-274ce6f69313 | -6.18178 | -42.62821 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 922e9762-1c81-3435-b0c9-239905ad59ba | -9.65434 | -43.53189 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7f80947-edfb-3b43-a052-107f978617cb | -6.89386 | -44.34578 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6ea41ce-a39f-39df-8f19-dee3d41be8eb | -6.32882 | -53.4587 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c99688a-ed5c-370e-af90-0cdbd933b2f9 | -10.78263 | -45.99481 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ab84c62-9ccb-3f58-a8ed-a222d994022d | -8.94229 | -46.11193 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a821ad2b-b9fe-3d0b-86c0-c5e8535bee25 | -4.3979 | -48.91904 | 2025-09-12 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1025ca31-4fc8-3db8-ab81-307ff14c49ef | -8.49833 | -47.31347 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 261fbb72-d417-3e60-9c29-e4531a1012f3 | -7.15032 | -44.3413 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5fd449e-49cd-368d-bd3b-c6045de78398 | -5.94511 | -42.55999 | 2025-09-12 04:25:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ffa47364-c043-3d94-90ed-be0103da201e | -11.66378 | -46.59458 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 724bcd88-4267-3d9e-8668-331f8f941a83 | -6.49945 | -44.49668 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40a6cd7e-757e-3062-beb6-1bf2361263b0 | -9.96087 | -51.69437 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 921ffe1d-b2b3-33ca-a86e-c703e759e9a4 | -9.98865 | -51.72039 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f425127d-35e6-39cd-92ac-f08e493a68ee | -7.70646 | -47.29407 | 2025-09-12 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c617f1d6-eed4-370a-a1d7-1815774a969a | -10.43557 | -50.62065 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9728c28c-2931-386a-bac5-e3bdf6a1dd3a | -7.53088 | -44.68893 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f856dc3-78fc-3bed-b495-736e7281d08f | -9.84194 | -46.06848 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d70a39d4-0486-31b9-992a-1705c89c076e | -10.13183 | -47.91295 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee774824-2636-3370-ac79-881224fe859f | -9.4512 | -46.41886 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05fe0042-0656-3ef3-aa88-ef91a49f9173 | -6.65451 | -44.12873 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f61c13a3-43d6-3674-ae03-e662d60d7b4d | -6.70513 | -42.04857 | 2025-09-12 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0553ea10-f10e-3d73-8c71-7060632175f1 | -7.2278 | -43.9769 | 2025-09-12 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abcac113-7820-3767-935c-dd921f7aed6f | -10.676 | -48.64768 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76b2b09a-57a8-3905-9e6b-05920da21b2c | -11.42658 | -43.54721 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 583488f5-4b3c-3f64-ab63-f3c65cdbbf1d | -11.43521 | -43.56727 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 787bbfc1-5c99-33fe-9e3b-32e8395efb6d | -5.94869 | -42.78684 | 2025-09-12 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0976b2c-f28f-3abb-b6dc-82eb670abcb7 | -6.41763 | -44.25636 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c423a7a-e4bf-3ed4-8661-652486967875 | -11.69542 | -46.58873 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ccf873d-14e8-3013-8e70-67924d6708d1 | -11.70926 | -46.49943 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c212f38-7af1-3e51-a19f-6e37116c1cae | -6.53891 | -43.70944 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a78275b6-8dad-35d3-a9c8-6baf648322db | -10.7043 | -48.62242 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5886b043-6214-32bf-b618-9103c532a82a | -10.17431 | -46.17516 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1d8a197f-c51f-30e6-bcde-05e8a633cb74 | -11.97683 | -46.65519 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53721626-af40-3c8d-9503-a13b42fa26fe | -10.70882 | -48.61579 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6088074e-3b47-3713-8dcc-75e45a026cd3 | -9.78521 | -47.84923 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d6d368c-13c3-3915-bc8e-11c2d3b479ec | -11.69264 | -46.58463 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51aed765-0eee-3ec7-acc0-0213085b2174 | -7.07271 | -44.13982 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc93daad-7e9b-3fed-95e0-7f4c28dd26cf | -10.51748 | -51.526 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac0c60ed-cfd0-32d2-b9f2-a515523ef754 | -6.40653 | -42.59932 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 62757997-211e-3d5c-9ce6-1d8107d79c6f | -11.67152 | -46.5666 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7439cc7-4c05-30fb-b254-84cd2e2de072 | -9.05501 | -47.0385 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a717ce01-25b3-3ff2-8b07-8745a969075a | -11.433 | -48.56839 | 2025-09-12 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba59e30e-cbeb-33e3-b4d4-b46eb14c8ac7 | -8.64355 | -55.24755 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 937c4d8e-3384-3ff1-af7c-2f75f38e86cc | -6.81886 | -45.60049 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6af3b4ab-ddd3-3606-b0f4-8bad1cd2f21f | -6.73634 | -45.99773 | 2025-09-12 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20f67248-2d4b-3678-be35-524ba84b11b7 | -9.10355 | -47.11774 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f293175-a55f-3c66-91ae-9f10ebd76d5a | -8.95144 | -46.72573 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8496a968-6745-3160-8c2c-11982962e347 | -8.07863 | -54.74891 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c19db96f-ac22-32a0-b0b6-1289ebd22f82 | -7.66026 | -50.26554 | 2025-09-12 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac48968f-c1c4-30e0-94ae-03de8737ac40 | -6.63268 | -44.08649 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2da7b31e-8e4c-33f6-aeb4-1601d7d4d3a4 | -11.10344 | -51.95723 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55aa1dee-8cfb-35d5-933d-19ebe41408fe | -9.05756 | -45.71673 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12b58355-e018-36d7-bf04-95aa39037b9e | -10.78824 | -46.00304 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02f8a5bb-05a9-3b02-bd67-a46cbfe90749 | -6.9114 | -44.55068 | 2025-09-12 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54d42076-c742-323d-9720-47c26a260fcd | -12.11073 | -44.85804 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b840b699-c0f1-32c1-a3f5-b1807f1a5057 | -5.40452 | -45.93616 | 2025-09-12 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68f873f6-be50-376a-a72a-aff365d12072 | -8.89179 | -49.93681 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 169486e8-c79f-32dc-af62-9004a7278ff5 | -8.0806 | -50.17719 | 2025-09-12 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6faec3b0-44c3-390e-a755-eecfbb6f93e9 | -10.70824 | -48.61938 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f7847d3-3205-3c76-a43e-e502dafe50e7 | -8.92898 | -51.07098 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 443a0a77-179e-3299-85e2-34309a30e352 | -12.0808 | -47.59849 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd99f1fb-e400-3b4c-99ac-c7739a8d6003 | -6.65269 | -44.14044 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4045c703-0fd7-3d41-a856-cb78c0a071d2 | -8.02586 | -45.411 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a0ba071-fcb9-3ff6-a9e6-f505ad55b9ac | -9.68077 | -47.54757 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af9544f8-eaf0-31c9-bcb9-ba47145ded3e | -8.01441 | -49.02937 | 2025-09-12 04:25:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bb3a730-bf93-3897-8c42-f52d1ee39fb5 | -11.14685 | -45.23577 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e38a348c-4178-3ade-9eb8-a5feff751315 | -12.24315 | -46.7516 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ce4acc9-06ba-3362-b834-851a3fb7382c | -6.31216 | -42.22222 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e43d63ef-25b3-322e-9ef1-d86388500860 | -6.83914 | -47.88103 | 2025-09-12 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 610fcf2b-0a47-36ac-b385-5e2436c416b9 | -7.52747 | -44.68841 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af7ec225-1f84-3200-b952-6f98e5447b9a | -7.45295 | -44.39803 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34232673-b943-3f14-9744-7679e7349d7c | -5.60738 | -45.79145 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 769fc750-ba5f-3f9f-a561-6fdaecec16fa | -11.69092 | -46.52955 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b5d82c4-52cf-3735-94e7-f1809d7bdc25 | -11.74959 | -48.27213 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ee0c3bd-0f3b-3537-a5d1-7d2e97f81c13 | -6.53914 | -43.10891 | 2025-09-12 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ea20c97-6009-3169-8688-6d3d2fda3eb0 | -9.04729 | -47.04441 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1be1af8a-aec3-3451-8a93-1b796c6d28a7 | -11.68209 | -46.58659 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2496f9f0-8214-3942-a2c3-c9c24ab724d6 | -11.69598 | -46.58517 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25a8e994-b658-33f3-9111-850ccd2e81a0 | -7.56486 | -44.39946 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7007e0a6-62e0-360d-917f-8327703c96e4 | -10.67484 | -48.65487 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README61.md)
