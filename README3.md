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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 448557a3-e0f8-382f-98c8-a36c93fbd2ff | -5.82749 | -44.10902 | 2025-08-06 00:28:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 49d5bf5d-a225-3755-be84-97ab8a8e2900 | -7.52079 | -45.06303 | 2025-08-06 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35b1f859-ef6a-3ce5-ba1a-f5b9047a3da7 | -7.21141 | -41.85638 | 2025-08-06 00:28:00 | TERRA_M-M | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 74eb9b10-fc5d-3579-b2e9-20e8bd5d7902 | -6.13134 | -44.43675 | 2025-08-06 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69ee689b-dfda-382d-963b-495ed07cf3db | -7.06605 | -44.39495 | 2025-08-06 00:28:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 710f83f2-4d65-32e3-97ab-8b7cd6681317 | -7.18509 | -45.48875 | 2025-08-06 00:28:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8dabe2de-8600-33d4-8818-3dc67ca336cd | -5.10713 | -43.17128 | 2025-08-06 00:28:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8905bdf4-be08-3be8-99c0-58b340a9dd6c | -5.58065 | -46.52573 | 2025-08-06 00:28:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fc29c716-1f43-3540-b7d2-12c7a3ac4fee | -7.51063 | -44.86044 | 2025-08-06 00:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6027dc8c-00d7-34ec-b126-168d991b8f36 | -7.51435 | -47.18729 | 2025-08-06 00:28:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 88b79b4b-98c5-327d-9390-1c64254c443b | -5.78607 | -43.60807 | 2025-08-06 00:28:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9d2dcd71-83a3-31b9-9762-741c259e965e | -5.10521 | -43.15831 | 2025-08-06 00:28:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 2ed161ed-bb7e-3798-a7d5-80d9612c0dc9 | -6.50028 | -45.53371 | 2025-08-06 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1e630d4b-4ffa-3a06-971c-b3379bf7a55f | -6.27917 | -45.27223 | 2025-08-06 00:28:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4a32748b-61a5-3ac4-9ecb-b3834c4968c0 | -4.82333 | -47.31569 | 2025-08-06 00:28:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| f3b1e3d5-8e15-3894-9231-d8d349364304 | -5.58856 | -51.12899 | 2025-08-06 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e7f94db0-ec12-30ee-87af-a692ae249aa8 | -8.38122 | -45.80687 | 2025-08-06 00:28:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2d0b64cd-7d36-368d-8e1a-095e53d80ffc | -5.1033 | -43.14538 | 2025-08-06 00:28:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a94a2482-6cf6-3d7e-9a7e-a9567a61a4ee | -6.48875 | -45.58247 | 2025-08-06 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d9f11383-2a6f-3f11-8f10-24927f5380a7 | -8.00235 | -43.22987 | 2025-08-06 00:28:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 81b97843-a13b-3fe4-af09-076e570b8e22 | -7.65276 | -46.59311 | 2025-08-06 00:28:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5be21cf2-e03d-35e8-a8fd-4b1f5e5fb0aa | -7.70534 | -45.12988 | 2025-08-06 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f42849ed-0e8b-3457-a936-ce8b6323fc26 | -5.72325 | -49.10181 | 2025-08-06 00:28:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| eff6a9f0-25cf-3010-924f-dc78cf17edec | -8.24981 | -45.07079 | 2025-08-06 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e6412f17-9038-32e3-8611-e4186a98203d | -6.6864 | -49.78739 | 2025-08-06 00:28:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 75625c4f-9026-3299-a832-4b2a9984a0ad | -7.83751 | -45.08501 | 2025-08-06 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b067d732-ecc1-3754-b4ae-189504ae355e | -7.82975 | -45.0957 | 2025-08-06 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| fbf2ef0a-7b4d-3c78-aa08-b0745bbb983d | -4.77757 | -45.34331 | 2025-08-06 00:28:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36c3de85-ac98-3249-b2de-2e34d71bc4b8 | -5.77546 | -51.67678 | 2025-08-06 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| eef7564a-4c2a-3abe-b5d5-1a259e3af286 | -5.58189 | -46.53461 | 2025-08-06 00:28:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cba70a39-72b3-3dd5-9c68-93210be9f238 | -7.90884 | -45.52729 | 2025-08-06 00:28:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 8dfa5298-c533-3e83-aef1-705a634006de | -6.67653 | -49.78875 | 2025-08-06 00:28:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 4a8c999e-049d-3046-b103-fba82920ca53 | -8.01235 | -43.22831 | 2025-08-06 00:28:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 55fee714-267a-3b70-8ae7-4c7836f5d8cc | -6.41725 | -53.37524 | 2025-08-06 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| a0abe123-b36a-3d49-9fe3-70c4b72a9488 | -7.82842 | -45.08632 | 2025-08-06 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 122.8 |
| e351e6d1-3b1b-348d-b792-6c82549e14b0 | -3.8275 | -41.57336 | 2025-08-06 00:28:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 99469f71-ab5a-3094-a79b-96aa56b9831e | -4.03859 | -48.09559 | 2025-08-06 00:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e52d75d5-ed7a-37e3-a2f2-433b4c5dec9d | -6.67587 | -44.44572 | 2025-08-06 00:28:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4de0af28-32e3-3129-8558-0387bb3e89ce | -7.67406 | -45.1057 | 2025-08-06 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32d73619-0005-3044-aa23-dda1fb2ddb09 | -8.01068 | -43.21685 | 2025-08-06 00:28:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7bcdc5d4-65f9-33c1-8037-eae9ff83e0c6 | -5.80096 | -46.99373 | 2025-08-06 00:28:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 659af0bd-05b1-3811-801b-3d8cdc61c3c6 | -7.19278 | -45.47823 | 2025-08-06 00:28:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0e178b4f-d06e-3b12-827b-6bf055e497c5 | -8.52478 | -47.44523 | 2025-08-06 00:28:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae5f6ce0-70a9-3b2c-80f6-612b1e85c150 | -4.82455 | -47.32451 | 2025-08-06 00:28:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d5b5370-9470-31dd-be2a-f70a705a2b41 | -8.00049 | -43.14727 | 2025-08-06 00:28:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| e1cb784d-83ee-3e4f-8f1b-e62724e6beae | -6.72302 | -43.5784 | 2025-08-06 00:28:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c4f459f2-634c-34d8-98c4-40bc6c4797cb | -7.50547 | -47.18855 | 2025-08-06 00:28:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d7969ebe-6047-3f11-ac99-b6014cb6da13 | -6.55145 | -44.01974 | 2025-08-06 00:28:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 59874ff8-0aa5-36fd-be54-bb9e09b48281 | -6.92335 | -43.68645 | 2025-08-06 00:28:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| c5630288-c60b-3917-882f-5e992278e263 | -6.48484 | -45.5548 | 2025-08-06 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ff3d226d-4c2e-3e9b-8234-8477db988153 | -7.91012 | -45.53644 | 2025-08-06 00:28:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| c6c0ae58-f4d8-3c43-a8d3-50a8aecc6a35 | -8.06522 | -49.71783 | 2025-08-06 00:28:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8d6c1aa9-e140-3811-a7e6-c4a99fd90689 | -7.51982 | -44.85914 | 2025-08-06 00:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dda9da51-d6f7-387f-b0aa-70ab1461d66a | -7.99877 | -43.13547 | 2025-08-06 00:28:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d88bba64-0cdd-3a23-b670-891725169728 | -6.95103 | -51.64011 | 2025-08-06 00:28:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 3f60267e-9f28-371e-b1ac-35dc0c4820b9 | -7.33046 | -46.06845 | 2025-08-06 00:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 36ec8e6f-0bb5-3d87-b7b8-e95bdba0a168 | -8.24848 | -45.06145 | 2025-08-06 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 17bf0739-a340-35f1-9ee8-3def591e7705 | -7.58073 | -44.90258 | 2025-08-06 00:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 247cbb4d-2062-3166-ba3c-6b5da3e3de3f | -7.52117 | -44.86866 | 2025-08-06 00:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c3b422de-70ba-3eb7-bf42-933fdc07610b | -6.9492 | -51.6302 | 2025-08-06 00:30:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b30fc3f2-7ad7-36d3-bf97-5c18d0495c17 | -13.0728 | -56.8729 | 2025-08-06 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| bc169375-2e70-3b85-a515-80fb700040e5 | -8.9028 | -60.7498 | 2025-08-06 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 2a62e93c-0329-3167-b737-6bdbf8125b49 | -8.9212 | -60.7681 | 2025-08-06 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 6071c59b-4738-302e-b995-4962173c2b3e | -13.0538 | -56.8746 | 2025-08-06 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8f4c29aa-e072-35a1-ba71-f91b466c2b63 | -11.4393 | -45.1154 | 2025-08-06 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 75528d90-83a5-3cfe-b4b6-2eca50c37146 | -16.3268 | -50.3481 | 2025-08-06 00:30:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 00ce76bb-efad-372f-9761-a5c4379e030f | -11.4389 | -45.1385 | 2025-08-06 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| f9a778d1-73af-3623-ba18-af3c5ac4b73c | -12.7576 | -44.402 | 2025-08-06 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| d254db2f-dece-3599-adbe-a19b82754b48 | -8.9215 | -60.7297 | 2025-08-06 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c0c62220-60d5-30f0-bfd6-06623137fc4e | -10.8064 | -46.4985 | 2025-08-06 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 1b997d66-6f85-3d5c-b758-21d9ff848efa | -16.3465 | -50.3449 | 2025-08-06 00:30:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0a96affa-ecfe-3f30-8b32-0ae6e9f03839 | -8.9026 | -60.769 | 2025-08-06 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e0bb2035-d45d-3bf0-8528-4e6db2b3b3ef | -13.0731 | -56.8527 | 2025-08-06 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a26dd850-c091-311c-9e5a-0f092360e197 | -12.0189 | -44.8219 | 2025-08-06 00:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c0612bcd-c51a-3fc2-8e7b-cda0793b71f2 | -13.054 | -56.8545 | 2025-08-06 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5b8904b0-f061-3a6e-a8c6-81d44b6ab018 | -8.9213 | -60.7489 | 2025-08-06 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| a4135b60-b48f-3e7e-9101-699d70d270c8 | -8.9029 | -60.7306 | 2025-08-06 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| dd4cb718-3ebe-37d8-9b17-c31f4e2ea252 | -9.0835 | -45.0499 | 2025-08-06 00:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 87961d26-4462-35e2-ab6e-099a0fea1abb | -13.0538 | -56.8746 | 2025-08-06 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 925f2d28-7378-30ef-b5ab-0860e4481c59 | -12.7576 | -44.402 | 2025-08-06 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| b49bfa1c-8520-3b8b-b90c-4f7a94fe9e78 | -8.9213 | -60.7489 | 2025-08-06 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| f076d8b3-6225-39c9-ba63-228c1af9e951 | -16.3268 | -50.3481 | 2025-08-06 00:40:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 9425461a-72c1-3ab0-ac7e-4c2afef20cb2 | -8.9028 | -60.7498 | 2025-08-06 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 616a2db1-4ec6-3f84-947c-d0a73ada36dd | -13.0731 | -56.8527 | 2025-08-06 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 26b1df49-2029-33c3-87e7-0706c7d6939b | -6.9492 | -51.6302 | 2025-08-06 00:40:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d7b26f40-20d8-3033-8f11-c338b0bd8687 | -13.7366 | -53.1519 | 2025-08-06 00:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 62420935-960b-305b-8c11-3fa69487a695 | -7.8383 | -45.0899 | 2025-08-06 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |
| e510ca0c-7fd8-3cf5-86b8-7e902df42e1c | -13.0728 | -56.8729 | 2025-08-06 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 1724a727-e3f1-32ae-9f48-cb044f4c3627 | -16.3465 | -50.3449 | 2025-08-06 00:40:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e8383bfa-938b-3383-badd-92c864390211 | -13.054 | -56.8545 | 2025-08-06 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| addb49a0-be1e-3aa2-a294-438033231a81 | -9.0835 | -45.0499 | 2025-08-06 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 271a89e2-6664-3542-a8a2-52c7c27cd035 | -11.4393 | -45.1154 | 2025-08-06 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b79e9838-8964-3e44-9122-1b8b1195cd99 | -8.9215 | -60.7297 | 2025-08-06 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| b461b642-d5da-3b8e-8989-f44fa032f919 | -7.8385 | -45.0671 | 2025-08-06 00:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 80a502e2-f964-3478-8595-aa2fab378e35 | -11.4389 | -45.1385 | 2025-08-06 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 237898ba-043b-379c-8f3f-840d78569c0d | -8.9212 | -60.7681 | 2025-08-06 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 3da61893-6e09-32a0-92f1-a1982417e7ba | -11.4393 | -45.1154 | 2025-08-06 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 908d82e6-3467-3119-99ca-0f5d1fd67662 | -8.9029 | -60.7306 | 2025-08-06 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 801f4813-950b-3cb1-bd1b-a4b1c2bcb239 | -13.054 | -56.8545 | 2025-08-06 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3aaca9e2-bb87-3385-adb9-89581dff786b | -11.4389 | -45.1385 | 2025-08-06 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |


[Clique aqui para ver as próximas entradas](README4.md)
