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
| 6a1abf90-b4c7-3009-97f0-e148a970a08a | -7.25274 | -59.99558 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24f65c56-9ece-34cb-a95a-e07fd2017c02 | -3.43389 | -49.03946 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfd4ae99-6372-37ea-a359-1ad98de6dbe9 | -8.57667 | -54.71282 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2d00b78f-f9d8-38a5-87ba-0a8c8dfb39ee | -8.57277 | -54.69441 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11cad4b7-88f4-347c-849e-89fe683624ed | -4.3104 | -48.10306 | 2025-08-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| efd51301-21fa-3a94-884b-d5400c86e9ce | -8.56952 | -54.71525 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2141c3b8-0a16-3c01-9cf4-536db9126f42 | -5.84667 | -59.91311 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5a751a2-bfd3-3e2f-9831-b7256faea3db | -7.13334 | -60.12306 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2fd19c08-c201-3abc-a393-68a070a261f4 | -7.05827 | -59.19339 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b95cd93c-89b7-369f-895e-4ad57f910aab | -7.2085 | -46.25094 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf43d0ae-d299-35e8-91c7-c15e2178084c | -7.54153 | -49.54877 | 2025-08-12 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37e123ee-5cf4-3ee7-a4b7-cca9c0c2785e | -9.99999 | -46.32408 | 2025-08-12 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab36999-9658-3ca2-b24a-a72b97686991 | -9.06522 | -45.0569 | 2025-08-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1dfe2f4c-acbd-34eb-97a0-298f26302938 | -8.57054 | -54.68694 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c5ad4e6-61c0-3812-950a-2e09866092f4 | -4.0697 | -47.97491 | 2025-08-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91dac5ab-1575-36fa-8d33-e0890eda19b2 | -6.61592 | -43.89342 | 2025-08-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 152b7f36-019b-3739-923e-f204d4e125b2 | -5.49417 | -43.9893 | 2025-08-12 04:57:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3133607c-6d62-3968-bf52-fc674b5576df | -7.45884 | -60.40404 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d1a211d-f77b-39cc-99af-b21df7c926fe | -7.0653 | -59.19976 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b810c30-d720-3ed1-b845-6fdb31ce1580 | -3.4292 | -49.04392 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5e41200-0133-39e4-8a66-e514296e7efd | -3.88287 | -54.21362 | 2025-08-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abc54bfa-0120-3a1d-b396-884d31724661 | -8.79379 | -52.06283 | 2025-08-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4859b138-3a22-3175-9e58-7b19f223d7fd | -5.48521 | -44.38359 | 2025-08-12 04:57:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aaf9a855-336a-3233-8c87-c8169a3c6838 | -9.92218 | -46.18095 | 2025-08-12 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7502f5f-e0e3-3fbb-b84c-4be90ff05335 | -6.97366 | -59.28882 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6b3187c-e581-3582-b794-7e0b2964a885 | -9.71773 | -49.47428 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d0eda69-781d-3982-ace1-2e2a650e3227 | -3.50401 | -49.05536 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 685e496e-3cec-3c19-8a76-9375c11092dc | -7.21293 | -46.21817 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ee49bf7-83fe-34d0-b3d0-cde7b8738ea0 | -9.06983 | -45.0656 | 2025-08-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2140c63-5c47-3e08-8e0d-e98cc5bbd692 | -7.21173 | -46.22703 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ead6d77-26e4-3db3-b4f3-ad0eedf6e882 | -5.48468 | -44.38733 | 2025-08-12 04:57:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 325ab1eb-6cbc-3550-9f4e-d0ed52a5d178 | -3.97069 | -47.88319 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 27ed93ce-54cb-3bed-9a1d-10d015aaf4ba | -9.71664 | -49.482 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9df7849b-7948-3b5a-951f-a9325db57c3d | -6.97761 | -59.28951 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9aaccf90-6e47-3f6c-9d78-4c5a0d5fc74f | -6.61648 | -43.88928 | 2025-08-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2034d3fa-367c-33bb-a119-df9842c0405e | -8.51827 | -43.32067 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 6bdc5e53-7d9d-3aa9-b631-7ad6090a76af | -7.07245 | -59.20404 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| caf62e35-27f6-3471-b526-0cf3f8b8095c | -7.07552 | -59.20976 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8dded41c-c167-37ac-81b4-492c612eb14f | -9.06575 | -45.05271 | 2025-08-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09fe270a-1568-3a98-9275-6659ce74d0f5 | -7.07637 | -59.20472 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b05c2788-0bab-379c-89e5-f38cf7d5144b | -8.57223 | -54.69788 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7796b86b-67d1-3b0b-90fd-fe6a9ee20b6d | -7.20822 | -46.21494 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd465b69-7605-3009-8461-4cceceb28c31 | -9.06937 | -45.06921 | 2025-08-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f3e56a8-30ae-32ae-abd0-520561e10061 | -8.57283 | -54.71577 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04c05b6b-7c3a-30c2-a607-2c928f3240af | -6.2514 | -53.63828 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15a73e22-dc6b-3490-9949-e7fb33a22c35 | -7.21721 | -46.22462 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d2c1ea8-3c4c-3c5b-8839-e71698810c57 | -8.52387 | -43.32654 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6c9d705-183e-37f9-9e6d-63cc1a18aa06 | -6.97055 | -59.2831 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a45e81c1-8e0e-3323-b4ad-a8bd134550ef | -8.57337 | -54.7123 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0eb8aa4f-ff81-36f5-99b7-d5ee15164f44 | -7.07722 | -59.19968 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4650f681-7e30-3457-941c-ba93fb9598b5 | -7.06301 | -59.18901 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cccd222-ed5f-3ab9-aded-a5bbbd5fada7 | -7.56798 | -49.30816 | 2025-08-12 04:57:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb560efa-9624-35cd-b11b-aa982770c325 | -9.06724 | -45.05558 | 2025-08-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5a6e16e-96b9-3298-9ae4-add11f3dfd2f | -9.7161 | -49.48583 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90b6da51-76d8-3245-aee9-825b2fde025c | -7.08507 | -59.20101 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65f21e43-dc9b-3830-b20a-087cc60fe961 | -8.56892 | -54.69737 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6627a97-a13f-31bd-832b-f1b5fbe0e6b6 | -7.20887 | -46.2482 | 2025-08-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 792cf8a8-c10c-3467-bdd7-e035eed8de2f | -3.42995 | -49.03885 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58e771ef-3a32-38cf-bad6-cf49a613e0cc | -8.56621 | -54.71473 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6dc83a79-9097-3dac-ac22-2d5bf82076a4 | -8.5667 | -54.6899 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01241db6-0932-3843-bbb4-f950b8879785 | -8.56399 | -54.70726 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e96e474-6023-3788-b01c-2636c1071eb1 | -9.21683 | -48.52407 | 2025-08-12 04:57:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d6a8a0a-4a3f-3840-a3cc-1a69ac30f495 | -8.57391 | -54.70882 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5af50347-8070-318e-b4f1-9b4635a117ff | -5.1124 | -43.15519 | 2025-08-12 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd260710-479a-3d3c-9038-b7cf42b8bec0 | -8.57721 | -54.70934 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e95182e-e72e-3975-aa2d-9330d139f124 | -2.58691 | -51.92122 | 2025-08-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4f5e1cc-99fe-35dd-8f11-ed52d3bbeca8 | -8.56663 | -54.66853 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c7772e6-b4e0-3a48-a7bc-d84334615928 | -9.91654 | -46.18319 | 2025-08-12 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31051330-c76c-3f4f-9cc5-aece07a6b7db | -7.12917 | -60.12241 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad1107df-d8b5-3043-b6e1-258043099d5c | -9.72137 | -49.47876 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4160f779-4ef0-387d-9716-581e519ba882 | -6.21703 | -43.33296 | 2025-08-12 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abc26dfc-d465-34d0-89e9-8cb8b9e1a62e | -6.9666 | -59.28245 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 569430b7-00f1-3798-bfcc-25f9f9c2d150 | -8.57114 | -54.70483 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ae5d08c-621d-3cd4-b568-432f4be061f6 | -3.07391 | -52.4887 | 2025-08-12 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e211c9a-e932-3f4f-b083-40ad33d7e5fd | -8.52008 | -43.30583 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a768cf57-0e52-3203-bea4-1843ebac6a01 | -3.10879 | -47.01283 | 2025-08-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02b2222b-f646-3406-9932-1f26b0aaac5a | -9.713 | -49.47752 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8d3ad9be-3f32-3d26-a1e8-4e869efb560f | -3.17979 | -48.8074 | 2025-08-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cf84e38-d269-39a0-aa5d-43c5fafa5d3b | -4.59277 | -56.0756 | 2025-08-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1238634-9021-3c8b-8115-101bed435d5d | -7.06853 | -59.20335 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ae82758-2dde-3770-92a2-f668988303c5 | -8.56453 | -54.70379 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82595d72-fdb5-3f04-8213-90d9a471aa55 | -5.83265 | -44.11071 | 2025-08-12 04:57:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8ee665a-4553-3464-8d29-5b3b0ca9400a | -8.56345 | -54.71074 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3eff7bb1-1536-3376-892f-7f7bae2cea5a | -3.43314 | -49.04452 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 22dd2b10-4515-3fd1-8aa0-b60e63181e23 | -3.42847 | -49.04895 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4ad7eb4-6011-342c-8eb7-5b6f84b03d3d | -1.89077 | -54.70644 | 2025-08-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 796c8ee7-8d73-3f56-8bd0-eab9580564eb | -8.56832 | -54.67947 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 830c14a2-8ce2-39b5-824a-0ea8dc6c8106 | -8.52082 | -43.31107 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 85bc0e08-6e17-3552-af66-fb0868a7adb8 | -7.13751 | -60.12372 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 74b00b9f-49c1-36cf-b83d-19540f764599 | -8.57228 | -54.71925 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 736eb232-248f-3f23-9822-3b6fded04b66 | -3.43752 | -49.04386 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c54fa6cf-4fc2-31f1-892e-7226985d3629 | -9.71718 | -49.47815 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed73490d-1600-367a-9a53-31a76fb5abe1 | -7.14038 | -60.13198 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f8f257aa-0ddf-387b-bfeb-06855409e1a4 | -6.69228 | -59.14161 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 598ccdf6-695c-3624-952d-15c816836855 | -3.96701 | -47.87838 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| dc81ac81-d409-3d01-9f96-991cc439501f | -3.48486 | -51.19015 | 2025-08-12 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 180a6285-6d0b-3934-93b9-0a4bea78ef81 | -2.58297 | -51.9243 | 2025-08-12 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 812194c0-1fa1-3131-9d08-369b7f32acc1 | -8.57168 | -54.70135 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1393392-2782-3d1d-b98e-611da02754fc | -8.56946 | -54.69389 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2c967d6-b4f1-32f4-9e89-02659b960455 | -8.56332 | -54.66802 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README23.md)
