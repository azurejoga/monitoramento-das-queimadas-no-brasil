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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b63abfb-abce-3ad3-8497-ce4aa6807a46 | -2.9258 | -54.159199 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c513057c-c531-3824-8579-75b6d4413226 | -3.5228 | -54.646801 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95d1b258-e7cd-35d9-ab71-63fa763fc12a | -3.0558 | -54.2313 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 507116a8-cb3e-367a-ba59-c40cf3adec3b | -3.3949 | -59.520302 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dea1190a-2932-3632-bee8-2a6f427d724a | -3.6752 | -60.5327 | 2026-10-07 00:47:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9460b2c-be29-31ba-99a1-39d004dce6db | -2.0955 | -52.053902 | 2026-10-07 00:47:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04844311-6a4a-3923-b993-1656768fc34f | -4.9168 | -55.856201 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ccb4d6-23cf-3b28-8342-9e65b6f2e3d7 | -3.4929 | -54.606701 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5b8c382-276a-3a0b-9607-8425e9b0e530 | -4.9188 | -55.8652 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74a9d0ec-90dd-36c1-96f6-fdc7ae9a5dc9 | -3.469 | -50.085602 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdf71f66-7567-3692-bd4f-8a12f02a9eeb | -6.3273 | -55.3172 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dedeec3e-b50b-3caa-a0bc-b24695d61343 | -2.9115 | -54.0979 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7d50c3-0932-3e56-b925-367d659bfd10 | -3.0457 | -54.144402 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b78feee-2433-3a31-b117-b4dc06b5d73f | 2.4505 | -50.8396 | 2026-10-07 00:47:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| da483021-49b5-31dc-8783-32bb17487746 | -2.7761 | -54.09 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 568363ed-ea12-3828-8409-c4e77fec8db2 | -3.5916 | -61.627998 | 2026-10-07 00:47:00 | METOP-B | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63ac92a4-5c1a-381e-9f37-90b0eaa72dca | -8.2771 | -50.250801 | 2026-10-07 00:47:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d378c23-0a01-368b-9954-77b8270e4e76 | -2.9781 | -54.030399 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d7e46db-1871-3677-9590-f4c9ba617463 | 1.0344 | -59.443001 | 2026-10-07 00:47:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fb10f44b-d8ef-39d4-8fde-44c2812d0815 | -3.0529 | -57.519699 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee621303-d7f3-36f9-9569-e58ac2a669f2 | -3.2948 | -54.022301 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78b3d3f0-b176-3cc8-830c-a3ca9214fd68 | -3.7563 | -61.167999 | 2026-10-07 00:47:00 | METOP-B | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 786d03dd-21f6-3b60-9cab-fd6a45d2c9b4 | -3.0575 | -59.8969 | 2026-10-07 00:47:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dedb30c-634d-3cf1-a1ba-ee7c202888a3 | -3.3799 | -58.184101 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4c04457-7137-39a9-9f01-09b15e3b4a76 | -3.1712 | -58.625702 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 679172d1-3596-381f-884f-2076b714f613 | 3.5961 | -60.330898 | 2026-10-07 00:47:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d058a9ae-d2cf-360e-80bf-aea252018f84 | -3.3832 | -58.1987 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f98746cb-e412-3330-8876-430ab8044082 | -2.7606 | -54.067501 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5253f711-f7d0-3e8a-ac30-de45c6255539 | -11.1034 | -45.721901 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89d54106-97f9-30e5-80e3-132792466ea0 | -3.7063 | -59.666401 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6cf0f1-4572-3151-9d61-4a3a544afe9f | -9.2641 | -50.6567 | 2026-10-07 00:47:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335e0f0f-8312-3930-bfdd-c7afc3b38310 | -3.1064 | -53.7878 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca8c01c-b9be-3a9a-ac9f-b5bd6d1f4c28 | -3.3816 | -58.191399 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49fa0333-10f5-3f7b-967f-d5d25b42e707 | -1.2824 | -54.560699 | 2026-10-07 00:47:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5589789e-21bc-380b-8a46-6eb35daa0eb8 | -3.9633 | -56.056198 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a101d8c-8c8c-3716-88fb-1523a4e33bf6 | -9.1061 | -67.689903 | 2026-10-07 00:47:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2b85321-4cc4-31d0-8436-112431b72e6b | -3.4848 | -57.7854 | 2026-10-07 00:47:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50b0e321-6851-3876-8662-1db577ea9c78 | -3.0039 | -54.141201 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae34eae2-2b22-3cca-b135-274666b312de | -2.1524 | -59.224098 | 2026-10-07 00:47:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11e65334-2821-3fc5-8507-01bd28245dcc | -1.5068 | -54.821701 | 2026-10-07 00:47:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20d97d21-ee7c-3771-a109-4334661578da | -3.0709 | -54.1642 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad03fa8f-8440-3666-a986-c229fc5dbe27 | -3.4935 | -54.653599 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb18ecbb-98a1-3f11-90ff-7e369df27829 | -3.5603 | -59.476299 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20f77969-959a-3e28-ae7b-c16ce14b67f8 | 2.0136 | -61.0872 | 2026-10-07 00:47:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 50a57f3a-470d-3129-a628-b2a574ecc4be | -3.5634 | -59.490002 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1796665b-4d7f-3848-87df-c198c369cfc8 | 0.9424 | -60.398399 | 2026-10-07 00:47:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 21e492af-6ce1-3b3b-9024-7e768cb4f4d0 | -3.2112 | -53.884201 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d69a51fe-5211-3141-9dc8-8e93a0b997fe | -4.0699 | -54.8741 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45c3ba2c-1539-342e-8c5f-73fcbe5fea21 | -3.3577 | -59.492599 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c47855b3-2c2f-3654-a203-f58fff5df8a0 | -11.1129 | -45.7192 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 458c0e3e-e911-3ee4-82ad-a7ba72607baf | -2.3029 | -57.079498 | 2026-10-07 00:47:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05529f71-c3ec-3db1-9d5f-0a9b84d61934 | -3.0613 | -54.255299 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3543699-5572-3556-873e-4cd8c662c972 | -2.5985 | -59.3727 | 2026-10-07 00:47:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af1d2405-460e-39c1-a5cc-29376c7889bc | -3.0876 | -54.147499 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b69f9dab-d11c-32e8-94f0-b7696d7cd716 | -3.2742 | -54.065899 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6951f6c-031b-3d19-8f59-087403e153cf | -2.7721 | -54.1171 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ad75aa2-b23d-3439-b7ac-52f460308375 | -3.0778 | -54.149799 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 200e4113-0776-3333-b7e2-791edd4e9a13 | 0.6857 | -60.0742 | 2026-10-07 00:47:00 | METOP-B | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bfb0315b-ddd2-3700-a321-553e89747e93 | -3.2627 | -54.0168 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af680e09-f24c-3b61-9b0f-ea279d2fdb50 | -2.9551 | -54.1525 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dab6dbc-9023-3792-a41b-99aa9f5e947f | -3.971 | -56.044998 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0ee2414-6f2b-3199-8eca-baf8db2f3b63 | -3.6661 | -59.625099 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 746f5a98-9557-3d87-8118-2543b30ba37c | -3.2803 | -59.560299 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 934c6182-6a94-3cc4-aafe-8cc50644a2a2 | -3.1176 | -53.703499 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b13a93cd-0e89-33cb-a8b8-e70c15e8db5d | 3.143 | -60.604301 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 133279ea-4f49-3013-afd2-86c04739336a | -2.7864 | -57.661598 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c657af8-b5d5-3e75-9d65-e6986d753fe8 | -2.5496 | -57.392502 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b158ce2c-1915-355b-b95a-179d5e1c27b9 | -3.5182 | -54.671299 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dabf525-2574-3623-aa63-84a65d7b72ab | -6.4436 | -55.021198 | 2026-10-07 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3a3a015-1e2e-30cc-906e-1e4c2cf9c86d | -3.7761 | -58.519901 | 2026-10-07 00:47:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b3bcb46-cfa7-3f46-8952-a24724576e1b | -2.8317 | -54.064201 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00e8164f-89f1-391b-b32a-b9f7aa07bdd2 | -3.8445 | -55.987999 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1d96001-2064-3c96-a820-1686f1169c2b | 3.2315 | -61.0354 | 2026-10-07 00:47:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c3c7a059-5771-3752-8e1b-b939c48c8ac3 | -3.428 | -59.6208 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3a50279-9cdd-3fb3-9659-291be3e493af | -3.0794 | -54.288799 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39e7632e-6f01-3898-b9fd-2772f6466a48 | -2.8685 | -54.133801 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58a1c3e1-b83a-3ba1-b15d-7b6c882d3253 | -3.631 | -59.5611 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 358c1eac-5f71-3b5f-90b8-36f2b26a71f9 | -3.4884 | -54.631401 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6878b82-33bb-318b-9c6c-6f3955f1e8c1 | -3.9691 | -55.813999 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feacfa52-6719-3045-a8fe-8b9b47b781ba | -3.4103 | -58.9062 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ec16ea7-bb16-39ab-af3d-3c76ab6d0153 | -3.492 | -59.5849 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 039dce91-3f69-30fc-9bef-f879f0e7e768 | -3.2753 | -54.026798 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94b2c23a-8613-3a31-b3bd-5358974f13a4 | 3.1446 | -60.597401 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5714b26f-40c2-3908-b477-4ad582e1ef88 | -11.0847 | -45.690899 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5df8d1fa-9e84-3707-af36-3c6ed94b1521 | -2.9441 | -54.193501 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed05a30-a9f9-384f-ac8a-e2f4d025ae90 | -2.9535 | -54.1012 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9487657d-b927-3a32-8362-539fc49afaa9 | -4.1311 | -54.915298 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cca2a64d-4300-320d-84d7-2b1ae693c545 | -3.2811 | -54.051399 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31ec2b5a-c0ee-3241-bf13-f4f0eb23b780 | -2.9689 | -54.123501 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d82731ef-2913-3818-9fa0-2d5113b92a3d | -3.5519 | -59.485298 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df61953a-27f9-3526-9bb5-3267d878923c | -3.6338 | -58.937 | 2026-10-07 00:47:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ef5a6b8-0d2d-3596-a71f-360c889af22e | -3.5156 | -54.660198 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51d81d29-ac76-3a0d-bab9-c0961f62c708 | -2.9815 | -54.133499 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe85cc0b-100b-314a-8e6d-eb8e1b285ebc | -4.9914 | -56.044899 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f3f655-06a3-37bb-9ba4-84a7270919bf | -5.9546 | -55.355099 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1709f0c9-ab91-31f7-a2dd-055648b864fe | -3.8522 | -55.976601 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46dfb163-50c1-3951-8095-9325782cfcd4 | -9.4708 | -62.379299 | 2026-10-07 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 063a43db-5ad4-3590-9232-b7222b907e07 | -3.8501 | -55.967499 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 681e75b9-1d47-3594-aee4-b40e5f0c94f2 | -3.0612 | -54.1665 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22471cde-8928-308f-bc7d-7ec0187c6520 | -11.064 | -45.841 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
