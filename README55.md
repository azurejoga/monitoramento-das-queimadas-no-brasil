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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d004f22-b9e7-344c-8a0c-9a820952d2b3 | -10.82679 | -47.62785 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e39d475-a0b1-3c41-8121-da769acebaf8 | -11.35837 | -44.95864 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98685596-12a7-3f9a-bced-314579c736cd | -5.77422 | -43.83885 | 2025-09-28 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f00cfd51-0515-3ec6-9d27-9c58e7d06236 | -11.99367 | -47.89426 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cca86edd-9895-32ff-be70-06c05bbe9170 | -7.60153 | -47.33759 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c625f09-47eb-387c-b370-69d1c640bc74 | -11.37459 | -44.96924 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b411f5c1-5724-35c1-a991-b73dbe66f24b | -7.16663 | -45.50616 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5f9db0a-de39-3c90-9469-c220f2d343cc | -8.48013 | -47.81299 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3aa240ea-0577-3201-ae71-2845bfb9e694 | -10.19461 | -52.55281 | 2025-09-28 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 913b638c-c199-32b2-a915-f6f91f377bff | -12.01912 | -47.88395 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d6d44f2-6399-3120-9413-0fc050516f6b | -6.8103 | -46.39387 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dfc955c-4600-3f8c-9621-b96c4680f740 | -7.74331 | -46.98016 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97b64f33-6bbf-3f2b-a695-16b1aa762998 | -8.02118 | -49.73749 | 2025-09-28 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d999bf5e-6ca0-3856-968f-9c092cfb6da2 | -7.80559 | -47.01508 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 71230bad-fb4d-3bce-8b89-03949357480a | -7.04529 | -44.76516 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5183e72a-a03b-3695-9df5-819f07cd7a9b | -11.39939 | -46.96937 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16ee3a5a-d255-39b8-97f3-cfddff60ddfe | -7.75435 | -47.01765 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10307aad-7f7b-302d-b9fc-8e34e514084b | -6.51108 | -44.98563 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1e8b3a2-d822-3adc-8ad7-00fedcdf2789 | -11.62106 | -52.85157 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2259b653-8349-33e1-8034-b7184fb3b1d3 | -6.61137 | -44.94981 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d84adfb7-0198-355b-ac03-75a7b627ce46 | -7.92502 | -42.67828 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c02dedd6-1341-3396-8628-0ec81c4130d0 | -6.48449 | -44.24777 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b16fa9b-64eb-3f46-95ec-6f07c10b7808 | -10.99993 | -45.60172 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bbad8dd-395f-32e8-945e-8ebc424be12f | -11.98283 | -46.59831 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f576acfa-3630-3f43-a5b8-1a0866a239cd | -7.7029 | -47.67739 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aed303fd-cfbb-32df-8866-4acda0dd4941 | -10.41639 | -46.15524 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4be4f251-528d-3845-a994-62c9d72fb56e | -10.11852 | -45.66504 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1e038fe-919a-323a-8556-72a5529be468 | -6.4248 | -43.07095 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 574403f0-0a86-34f6-81f4-cc82dd372ac3 | -8.2828 | -45.46581 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db571386-070d-3ca0-9093-40b1fd740242 | -8.29336 | -45.44189 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 870a48ba-cc3d-3788-9dbb-1356147bed00 | -12.29569 | -45.64172 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c757e448-5c67-37f4-8f43-3b2c8eb19a37 | -7.86621 | -44.57572 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184b6af8-e0ac-3079-9d67-aa895bbb7394 | -7.63649 | -45.97752 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cbc5fb0-c3df-3734-b8fc-9f492d0e87d2 | -8.27221 | -45.46781 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac7b7b16-8ef1-3640-86ad-365f76f08107 | -7.43552 | -43.18811 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da7c8717-8602-3a25-b9f3-c58e10836688 | -12.06246 | -44.85831 | 2025-09-28 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 361133e8-f37a-3cf0-805e-ca978b292803 | -10.96435 | -49.5733 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70cbf7df-2e53-3d41-aae9-75e9042de3c1 | -12.00269 | -47.04077 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e31ec684-c205-3121-aab9-0a05c87e36ac | -6.14607 | -47.30142 | 2025-09-28 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfc54744-cbc8-326b-ad43-a1c851f8b501 | -9.31956 | -48.95255 | 2025-09-28 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 390d730c-fab8-347b-8550-a206329de158 | -7.78734 | -47.0229 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9d16e4b6-eb7e-3b20-8a20-bf39a8b4a24a | -6.76522 | -44.58818 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbd616a4-1c38-3ba7-9047-9fe0998e118d | -6.42057 | -43.07451 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0c762100-3290-3f4e-8df8-dff3c9277b25 | -7.74773 | -46.99515 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5d7ee7e-15cf-3259-8626-b8a670154b22 | -8.68021 | -47.06942 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4bb3468-207e-3780-a3d3-49418a6b8c3f | -11.7971 | -44.91505 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d0283f3-0573-37df-90d8-79718c6f8e07 | -11.44403 | -45.00406 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7744de6d-80ac-32e2-aaa7-12aacb4d8557 | -11.9756 | -48.00721 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8cc2bba-5980-3c0f-88af-1c21109a25c0 | -6.31126 | -43.45646 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04d79448-b5da-3e98-a71a-7e0f2099635f | -9.07033 | -45.53324 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f1293d3-edfb-34bb-b6ca-60e8524533ed | -8.25281 | -48.9751 | 2025-09-28 04:25:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 937091c1-e20e-3d12-aa4b-98095d2ba251 | -6.78464 | -44.04939 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74bec20b-2af4-31eb-bdde-e6f5a2307b48 | -12.42079 | -44.11521 | 2025-09-28 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba2b17ff-af16-3b09-bdf6-18a6230d7540 | -9.44971 | -43.70504 | 2025-09-28 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 329cc73b-6f78-3763-9ac8-906278d3656d | -7.79397 | -47.02396 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 015f0ae8-623d-32c1-8741-239e199a00c1 | -8.57816 | -47.00668 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0ee70dc-6555-3a19-bd67-305a3c352124 | -5.73792 | -43.37459 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7909b5f-1faf-3b46-b897-d56e9b0e6d55 | -5.39667 | -45.85876 | 2025-09-28 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4363b8e-0ef4-3385-8d3f-73cfdc2b62bc | -11.85647 | -48.24235 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59a7741b-836c-3255-b2b6-b4d9d1f03917 | -7.75436 | -46.9962 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b137d32-4d40-3451-ad78-0a34522275f4 | -7.37813 | -47.0326 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09895a58-8981-33c7-adea-e1cf6afd4d4e | -7.71012 | -41.28748 | 2025-09-28 04:25:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cbed515b-6daf-33e9-b774-12b579129dea | -6.58233 | -44.43302 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f254b02-fcdb-38e3-9306-b3eadcb3320a | -12.01595 | -47.0429 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51a7f300-e757-3cbd-9e9d-fec61021dfab | -11.40481 | -43.50494 | 2025-09-28 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10bcd54e-15cc-3d31-92b6-fd5f73df4e2d | -10.97502 | -54.09866 | 2025-09-28 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31eefe78-4529-3d45-97bd-55b649095f50 | -7.74772 | -47.01659 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ec899b5-7418-3d18-b277-f0b90bb14f8a | -11.94402 | -47.92974 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 602b90db-030b-34a1-bc48-7f91f26b264d | -11.56653 | -46.92041 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bab8d164-2a50-34a6-8883-4e36dcf4bedb | -11.94458 | -47.92621 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| accca8aa-429e-3f50-ae67-6bf132b1ac8d | -11.40434 | -46.95936 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efcdbd73-2fdf-317c-a067-664d21463ae6 | -6.60691 | -44.95647 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71be6305-01eb-3a71-9542-dbbf027f8b28 | -10.92521 | -44.31801 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29c35fb4-e087-3868-bf42-cd5b33542ba4 | -7.37646 | -47.04308 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57534d7b-b4ec-390a-ac6a-69a9261288b7 | -11.38116 | -46.95563 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b7ba230f-2e1e-3843-a742-a76dcdb09cee | -10.29582 | -45.39689 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91871262-f6b1-3d9f-847a-3e4dd87191c8 | -8.64847 | -48.92011 | 2025-09-28 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 455142e0-eaf8-3e9b-90a8-76726565e393 | -6.56429 | -45.09927 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70be9029-fd34-342d-8d70-8fb7c0dfd787 | -8.28001 | -45.46172 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52de8ce4-2ba1-3378-99c7-df6611a6c150 | -6.48394 | -44.2514 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c454db03-1ebe-3705-a665-540d2b96f213 | -6.6482 | -39.5036 | 2025-09-28 04:25:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33044b1f-ef07-3555-b4a5-197fae607712 | -11.44751 | -45.00456 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| ac8bf6d6-7b99-3b11-a620-8cd2da77b38f | -12.01793 | -47.91272 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8803bb78-f3b7-31b6-a383-76cb91f579b7 | -7.82711 | -45.14689 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c81ab0b-f54a-373b-9834-09ca57426e22 | -10.90579 | -45.75571 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4f38c7cc-d879-3814-abfa-f88e1a8b3779 | -11.95958 | -47.8961 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c25e7dde-335c-35b4-ac08-482c55eb79ba | -8.68739 | -47.06699 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46abccf1-9ca1-3ef1-b30e-2b556a64f437 | -11.98339 | -47.87465 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fcba94b-7edd-3b46-b672-b0c2820b7170 | -7.37481 | -47.03207 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df95cbba-49f4-32e4-ae99-b8ef95d29b08 | -6.31419 | -43.461 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c86a8e4f-f67e-3dcc-bb6d-047995cae40e | -9.21496 | -46.78042 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a61ab0f-31a8-35df-9ca8-760160e12525 | -7.35669 | -42.09851 | 2025-09-28 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 88bb2876-ec99-31e1-aa74-ed7a86553413 | -5.74174 | -43.3742 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72fc10cf-0fde-38df-a764-1e26e52ccc8e | -10.28378 | -45.2016 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 854102ef-6d01-3d93-811d-88232051e80a | -11.43644 | -48.69252 | 2025-09-28 04:25:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f7aad969-246e-3105-a11b-b92a110514fa | -6.11719 | -41.80844 | 2025-09-28 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9a761917-69c9-3753-85ff-5a97a9e3f1f3 | -9.29793 | -43.21874 | 2025-09-28 04:25:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e65f973b-a49d-359c-9beb-4e27dd39e413 | -6.14942 | -47.30196 | 2025-09-28 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81f609c8-724f-3a1a-9b16-64b7a94d2c5c | -7.99737 | -45.70816 | 2025-09-28 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b91abcda-8439-373b-841f-289ef28211f2 | -5.90606 | -43.29222 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README56.md)
