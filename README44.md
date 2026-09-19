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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c3318ab-4198-36ff-9e32-f35398751e39 | -6.00012 | -51.78942 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2be6a0ba-bdff-3ce7-941c-eb5f21a65947 | -4.87693 | -56.07102 | 2026-09-19 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc4f50ce-ba25-3972-86dc-93badc2f8e5e | -4.56435 | -42.97773 | 2026-09-19 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f725a071-dd98-3f6d-8cf3-f50938ec3bf8 | -5.88007 | -44.97505 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17873c53-a0a7-3e78-9c86-80df9bf70689 | -3.55383 | -50.29581 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf295018-2dde-3288-99cc-7f75e182b2a3 | -4.06223 | -56.24651 | 2026-09-19 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ccbff3-6698-332b-a78d-6ea13253d254 | -2.81695 | -50.46404 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9a393aeb-f35b-37f4-b155-efe4602b897f | -1.58256 | -54.43151 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 15c5a45a-8d5c-3619-b8df-acac128688b0 | -6.57486 | -44.16374 | 2026-09-19 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 397a6431-a8df-3321-be8b-e3bc4d57f925 | -7.31049 | -42.35799 | 2026-09-19 04:38:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52edff04-2afb-3718-9896-16fe3c11cc32 | -2.29176 | -47.88447 | 2026-09-19 04:38:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 47c550be-60af-35f0-bca0-64197b077cae | -4.43033 | -55.07609 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72803a7d-9341-3c6c-ada0-833e7c2f8302 | -5.7488 | -57.58676 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e381c42-d051-3bb2-a586-79a793414f8e | -4.49595 | -54.98281 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ab86683-1466-3e94-8a96-63abd19798e3 | -4.80809 | -56.08677 | 2026-09-19 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62c21553-5f91-32b9-aea6-b5371a3b771d | -8.36024 | -47.24045 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b43f518a-07b6-3d61-81f5-a71c974f0944 | -6.36774 | -58.31394 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03489c47-90d5-3110-933a-fbcbfa36bb51 | -5.77844 | -47.17743 | 2026-09-19 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78d17f25-76e3-368c-8909-87bc03b60add | -7.88389 | -46.42344 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a03e33fc-2d08-39a8-830b-a999aa1e614d | -3.6466 | -49.9692 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6654e5d8-6911-338a-9617-eb0c37db49e5 | -5.87487 | -53.61541 | 2026-09-19 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c0bd7dc-9124-3ed1-8110-2401d89fad98 | -3.2309 | -46.94646 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eaceff79-e6c3-386a-b4c9-2cb533a7891c | -1.22426 | -55.72855 | 2026-09-19 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e5efe77-6da5-3d4a-ae72-ecefba69434c | -8.4406 | -45.69681 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da8adccc-ad0d-3530-a451-b59eefe0fef5 | -4.35798 | -55.42945 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a309a20-a1b5-3181-999c-15c9775d5d60 | -3.44993 | -50.6063 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4732214-8410-3dc6-88ee-55eac9f217b5 | -6.02134 | -51.7655 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 506029d9-2708-391b-952e-0b7d8e2270ab | -7.81862 | -44.96091 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1d22933-50e7-3044-95a9-0b6cdf547a63 | -6.67529 | -50.90609 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8448e30f-b155-3883-ba87-62db062486f9 | -1.70527 | -54.89244 | 2026-09-19 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ca247e-f63e-395a-ac8a-770c52dedac9 | -4.44637 | -55.53595 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b668759-0dc5-3c12-b1d6-295bba0370de | -3.4505 | -50.60282 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d25579b7-f25b-3379-93a7-f86b07458ae2 | -8.7765 | -46.91656 | 2026-09-19 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd3c542a-a307-33b7-8e5d-0318533cc078 | -6.94597 | -42.55186 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ade1380-acb1-3903-9cbf-551b9cac30d9 | -3.03562 | -48.41542 | 2026-09-19 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 063c5bb5-1616-3636-853d-e3b4fa2e7643 | -2.89421 | -57.79322 | 2026-09-19 04:38:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53b2837d-1909-33ec-b6a8-af7e53e49b68 | -5.94695 | -44.81305 | 2026-09-19 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b282e12-56b8-30f1-bbe3-cff19263dbe7 | -8.47082 | -47.01044 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9e17c15-caf1-3b89-ac45-353e50a455fe | -3.23597 | -46.95827 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2f3d15e-7006-3b76-a83a-6bbae7f19da2 | -2.62573 | -49.10579 | 2026-09-19 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 807566f2-b3ed-3ce7-b309-3d7aafe21db1 | -3.81731 | -50.7464 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 446d3d30-97b0-3a59-8f68-3751822ceb10 | -6.36456 | -58.28961 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b0baa48-df02-3759-b745-951a76361d2e | -2.7349 | -49.45979 | 2026-09-19 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 540b02ca-5ca5-32c9-aa9f-ecc5fa91a36a | -6.26419 | -41.67507 | 2026-09-19 04:38:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f276d48d-274c-3400-bc00-f3964d74dad5 | -3.37037 | -50.45715 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e5906a4-f9d1-3c4d-8f39-7fd6a1ddff99 | -7.02205 | -47.44086 | 2026-09-19 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b01dbc8c-6b5c-36bd-8a39-6f5080a47916 | -5.55762 | -48.44036 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ad4a923-d085-3690-bcef-1a3077b4465b | -3.73771 | -54.63907 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b672e274-9295-37c3-908d-8093b53cfb53 | -2.96126 | -52.14606 | 2026-09-19 04:38:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f420b498-f3d5-317b-9310-8a449e95fae4 | -3.4534 | -50.61048 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8088f4d5-508d-3336-aa9b-bc5f73f34731 | -8.54956 | -44.56086 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c385a379-b175-3e92-a48d-8dd6cf91c05d | -6.20132 | -45.3448 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec04836b-399a-3d80-b019-7df3f42274bb | -6.218 | -45.19536 | 2026-09-19 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec2c56fc-28f5-322c-9c55-d77d39c9710b | -4.1836 | -49.40601 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b1ea746-f7e0-3002-b873-5a2a0b988300 | -5.6517 | -51.7047 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8843dba5-2309-3c2c-a532-27500c48e744 | -7.52874 | -44.93985 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b83dd2db-2e97-3d0b-9869-f17eae07c110 | -7.64301 | -46.10974 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31e0097e-53a9-38d8-9ee4-e85afd8f3f29 | -4.27398 | -46.53424 | 2026-09-19 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c224721-e1c3-3cbd-ab88-39672c3da7d6 | -1.22496 | -55.7243 | 2026-09-19 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02469802-23f0-396d-83dc-adbe52204325 | -5.74811 | -57.60307 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42e62698-28a8-3484-bb55-8d1ba2a69709 | -7.18915 | -50.82676 | 2026-09-19 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 495a4c66-e73e-3f17-a22a-538ee84e50f8 | -7.85258 | -45.16806 | 2026-09-19 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24eb2644-d7be-3237-afb0-d25159effef6 | -4.25761 | -48.53824 | 2026-09-19 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f833ba80-f7ca-35f8-b8c8-2a65a2623b56 | -5.74524 | -57.606 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ff8ffa-1328-3757-ba2f-9a5e5058d8d1 | -5.74348 | -57.58096 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a0bf2e7-832a-33ba-a500-b0633198fe11 | -3.84866 | -50.00707 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0305205f-f20c-3501-85f0-7199df3594a1 | -4.06808 | -56.24757 | 2026-09-19 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13826f4e-216d-3504-a11d-bd712550ae1d | -5.91386 | -46.3278 | 2026-09-19 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 588938f9-ed01-3814-bcdb-86ec8511525e | -8.47161 | -44.52549 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d12ca17-0fed-3373-bd1c-0e64e66ff44f | -4.68467 | -46.39553 | 2026-09-19 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8d85504-5a76-3aac-b50b-9b42e4b3ac33 | -6.90553 | -41.70649 | 2026-09-19 04:38:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68069ba3-8a3d-3f41-8ff0-a585d7fa6d39 | -5.33032 | -48.99042 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f25ec0fd-6943-3e61-bedf-ee7c8a4c022d | -8.39004 | -45.63816 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b0c3e29-22d2-303d-adc9-33e9a886e23a | -6.17115 | -47.71338 | 2026-09-19 04:38:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9be2d5e5-106d-39d2-b868-a63693c1e667 | -6.92071 | -47.41751 | 2026-09-19 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9e7a8ac-cd88-3857-9872-d67e2723e312 | -7.76041 | -46.75742 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ceec2a59-89d6-3f93-b414-36a7be792d6c | -3.35506 | -50.45018 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f1dd45f-51e8-31fe-b0e5-9726896f8132 | -1.19922 | -54.22214 | 2026-09-19 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf3f4f76-7b88-302d-a26e-fa5f5b9676a6 | -2.02951 | -48.77835 | 2026-09-19 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5dd2d0f-6e45-382c-b7a6-427d39800a88 | -4.21211 | -56.33624 | 2026-09-19 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f709a88-63ee-37da-b5e6-8f9a62d0cc68 | -7.00323 | -43.88565 | 2026-09-19 04:38:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0d4c30b-4743-35c8-bc42-4e4317e08b31 | -7.02228 | -44.65203 | 2026-09-19 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 01346ab4-eb11-3f06-aaa2-7a5a8ab5ee76 | -3.35778 | -50.45861 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 908b5376-c0a7-3e0d-957c-4edc5f30991b | -7.60458 | -45.42084 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 865c2370-8bf2-35d5-9e83-1da38ce7893a | -3.73661 | -54.64548 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bca091f-f8bc-3c5e-a27e-e7b980f19d8e | -8.22826 | -45.60483 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d356639e-4a7c-3b85-9985-c3440c388956 | -6.31599 | -41.75588 | 2026-09-19 04:38:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6e9d1363-8e1e-39f5-897b-9253a667905a | -5.86383 | -52.03955 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f620ed75-458b-3fad-b991-6072d9257cde | -4.17781 | -51.24751 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86cbda54-53f3-3eaa-b33a-e3bfc16dc197 | -8.72076 | -44.87664 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 867793c4-b5f4-3a2c-a8a9-c76c377be272 | -6.26888 | -41.67061 | 2026-09-19 04:38:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e30ca9e0-61dc-3bb2-8337-685250350b30 | -3.15292 | -53.93659 | 2026-09-19 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0cfebc2-50bb-3850-837c-24fe579d41d1 | -6.36361 | -58.29486 | 2026-09-19 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc17612-387a-3756-a878-be1d408fc47e | -7.19735 | -47.8699 | 2026-09-19 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f2ca8df-75da-3027-8b11-5d4eb6d31ccc | -7.88223 | -46.4339 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a7277f1-45fa-32cc-a7b8-3cafae20e8c7 | -7.02113 | -44.65944 | 2026-09-19 04:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bfd0e8d7-e429-3b03-ad73-0530852b704e | -8.77266 | -44.22973 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1df7f6-128d-3255-bbc7-44792ba1f5a7 | -7.04136 | -42.08422 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1e42e2a8-3396-3227-b90a-f10eacc0269a | -5.22699 | -49.30416 | 2026-09-19 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 654e9def-49a2-35fe-9412-f7ff1d46bbfd | -7.78052 | -44.89124 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README45.md)
