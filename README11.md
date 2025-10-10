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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97ded8e0-cf49-3bf8-9045-78794488152f | -17.9029 | -57.4947 | 2025-10-10 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 5d4f0aca-b05c-3021-83bc-3ff667bf4087 | -17.9369 | -45.0388 | 2025-10-10 03:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ce6c70e0-b360-30aa-99c9-ce601ba826b1 | -18.6497 | -43.9301 | 2025-10-10 03:40:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 53ebca98-a55f-3267-b16e-16cc57b07017 | -4.8595 | -42.7688 | 2025-10-10 03:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 33ad43d8-4537-348f-873e-c40398a9883d | -17.9026 | -57.5153 | 2025-10-10 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 124bd636-4f9f-3630-93fa-15e2b04fb10a | -10.1707 | -44.5959 | 2025-10-10 03:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| a2bf37a1-84b2-3ed2-af46-98a098ee5fc7 | -8.20838 | -43.37617 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16741f52-6611-376d-85a4-d835a98d2473 | -7.25851 | -44.09877 | 2025-10-10 03:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 725990cb-797c-31e3-8ca1-1fd40c3a8ca5 | -7.73758 | -42.41542 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77a2f643-47b6-30e2-b885-5bb4ab77f56d | -5.33756 | -45.57425 | 2025-10-10 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 404d85d1-0228-3467-83e0-ec03694cb77d | -7.14566 | -42.19815 | 2025-10-10 03:40:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93fb0fc8-d67b-356d-a501-50ba8145d125 | -12.63038 | -45.05835 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1f2cd7a4-6b45-3641-94d0-976d66327e8d | -7.71297 | -42.37738 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d0a7f4d-dd5f-380d-ad11-2442b3d05808 | -7.42468 | -42.98807 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee8abcad-6eb3-3567-9e2f-68925eeaa183 | -7.77475 | -44.04334 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ccd47ac-bbcf-3563-ac06-9f16ea16b52d | -7.41771 | -45.15817 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fdf8909-6c48-3c7a-afa2-bfa254860fa1 | -7.45118 | -37.33062 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5f408d9-e36d-35f2-b71a-a74afa8462ea | -8.15991 | -43.32489 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f8e876f3-b520-3e97-94b1-a0239facddd9 | -10.16012 | -44.59351 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0ffd3942-2285-389a-bc3f-ce44deed55f1 | -10.16783 | -44.5836 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a4235c0-076b-3ee2-8b5f-545e0c8b46c0 | -13.0584 | -43.8418 | 2025-10-10 03:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f06a0b9d-9b66-39e0-9aa5-818e3a4299a2 | -8.50944 | -46.18695 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd722cc8-09a1-3b48-8e18-748dac5854b7 | -10.16084 | -44.5897 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 19d2499e-cb1f-3b18-83a5-c4c0be1fb565 | -8.20256 | -43.34742 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dbf9641c-c6dd-32f1-bef0-e835202a3cda | -7.26279 | -44.91076 | 2025-10-10 03:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31d5c946-38f1-39ec-b269-fe7a5dff2b58 | -8.50844 | -46.19226 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bab8f2f4-6ea0-34e1-86ce-d9f8c808edd8 | -6.81803 | -42.80304 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 14454879-011f-385a-9291-266b4c3e3b7b | -13.05899 | -43.83879 | 2025-10-10 03:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 804d78cd-6df8-30b7-8c46-88972c18d4d8 | -12.23046 | -43.78968 | 2025-10-10 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 800070ee-0a3f-341b-94fd-bdbf8b9e2b5a | -7.77424 | -42.41599 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a217bfa0-43cc-3ac1-80aa-e0c771c91794 | -8.20777 | -43.3795 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 27fad21c-7a79-3989-9de9-39f337b1e013 | -6.98803 | -41.93096 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 848d2d51-96c7-334f-867e-b5dc3190ab9f | -8.49276 | -46.20516 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afffae5c-83fc-36c6-aec8-d5eaa95a2944 | -8.51142 | -46.14888 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d1110da0-3735-3533-85fe-47337f156f97 | -11.46826 | -41.89313 | 2025-10-10 03:40:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa23a446-4ba0-3986-97ed-0b25da151d33 | -7.66381 | -42.58076 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 628c9c7b-2d9e-38e6-a642-f252e23d7912 | -9.30439 | -40.23076 | 2025-10-10 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 755c8a48-edb7-3a44-a173-cdab7b7d4373 | -8.51664 | -46.19005 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3459842-f933-3588-bb67-de49551b831a | -10.16094 | -44.5585 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61cb5ad4-d688-3975-bcb6-a7e943e8d6c1 | -8.20194 | -43.35076 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b3c38b2a-b274-3b67-b147-5d012091ac0c | -11.77744 | -45.04083 | 2025-10-10 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f678b0a3-903e-3f29-9196-35ae79c247ea | -7.79969 | -44.19698 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd83e805-3daf-32b5-8565-c9920c6ada15 | -7.77826 | -44.05613 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0b5cec6-4116-3f01-b1e6-e0b3b488666b | -8.84216 | -46.06416 | 2025-10-10 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 051b1e49-43f4-3ff3-a2ad-595e415f4f39 | -5.97898 | -45.91987 | 2025-10-10 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da1dc73f-95d3-3d07-a26a-4d439d107681 | -8.50916 | -46.19441 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11b43577-54b2-37dd-b189-a0257ca06ef4 | -10.93781 | -42.85181 | 2025-10-10 03:40:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b6f88d97-d9be-3ebd-84bb-3075ecad44ce | -7.40446 | -45.92791 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eaf10434-d4a2-3526-8092-88163d39bf3f | -12.43751 | -45.78175 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1be8e476-16ab-3af7-8f4c-d074fd164226 | -11.0949 | -41.05593 | 2025-10-10 03:40:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 64322d35-230a-34d4-bd2c-c6ffbd1a5880 | -8.51343 | -46.13047 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b0b1fffd-1299-39ca-a1a4-c22727e0afc4 | -6.74046 | -42.85051 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25e64681-89e4-3fc7-93b5-f4c58d6e357e | -12.62406 | -45.06114 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d0bbe204-83d9-3f13-940f-6193c1e65930 | -12.92688 | -45.05733 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c334dd83-53bf-3f21-8e10-5f63b03a07bd | -8.19906 | -43.33629 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1cde4e30-a411-39a2-bb9e-f589ba0eb19d | -7.57505 | -44.38508 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1e8ee0a-fbfb-3cab-bff5-362b13b70755 | -7.31936 | -42.94286 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 391e1b79-6b89-377f-a78f-502e11e0eb21 | -8.51483 | -46.19349 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e6146b9f-4428-3324-9fda-f29c0480906f | -12.62178 | -45.07264 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6a902f27-e1b7-391d-b34e-17a586e6cc85 | -5.74358 | -43.37935 | 2025-10-10 03:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26521255-a5c7-383e-9603-86c6e0300c50 | -7.53657 | -44.3036 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79971795-471d-3d08-84c6-a918bec23504 | -6.73987 | -42.85392 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 10db684f-0067-3e4d-91a4-4d4b1f9c7c39 | -7.26346 | -44.10415 | 2025-10-10 03:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d8f94ce-1254-381d-a91d-38bad0c35017 | -7.76457 | -42.4113 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a7b33f8-69be-3316-ac65-4cd1b87b383a | -8.17948 | -43.32219 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9a3185ff-02cb-3e82-be29-cd6f15c71e01 | -7.77899 | -44.05212 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55237567-b8f7-36ef-8636-b01d62fed934 | -6.74997 | -42.82756 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48792b76-07ce-3ee5-9f19-ffccbc03d6d9 | -7.26722 | -44.91415 | 2025-10-10 03:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc32b41d-85fd-31c5-99f0-c6e899178da7 | -5.74919 | -43.38033 | 2025-10-10 03:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5a9ad31-21b0-33e4-aa3b-752bbb64c17f | -5.33852 | -45.56874 | 2025-10-10 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2677605a-5199-3b8c-bc58-e10684e41129 | -7.53008 | -44.30642 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14a007e0-832c-39f9-833a-f45c7b7c6d22 | -11.46735 | -41.89799 | 2025-10-10 03:40:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9788744d-6f58-3c09-b3f2-9789c5f551e7 | -9.30011 | -40.23 | 2025-10-10 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 0a15417b-d35d-3a28-b109-4c2a6549b669 | -8.19493 | -43.32859 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 049d708a-1572-3753-8e37-b79e0b348c7a | -7.39584 | -45.17342 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f185c16f-3bf1-37e2-911b-6d0d440e951a | -12.63113 | -45.05455 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 93ebf6ed-c155-3ca7-b95f-ee44c0c08ea5 | -12.72118 | -45.83493 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 176a764e-0049-394b-b607-ff833bc480c3 | -8.50197 | -46.1563 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15ad2df2-d129-37ba-93e6-74b2e3f16090 | -8.07206 | -42.94483 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 338404a0-164d-332f-b825-e1e8297dace0 | -11.63854 | -47.53854 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94187903-3282-3045-94e7-660cb5cd12ef | -12.22566 | -43.78685 | 2025-10-10 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d92e2cce-1727-380a-875e-53a2fc0a43ea | -8.20669 | -43.35512 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7fd59189-d1c3-38b9-8ddf-5e710ce7f0f6 | -11.97085 | -45.21297 | 2025-10-10 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c48c211f-4ca1-388a-91c0-6a4377a5d0af | -6.75411 | -42.83532 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c860bd8d-dcd8-361d-8bc8-b63a90b830d9 | -8.51018 | -46.18919 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56e934cf-27e4-33de-8945-be3615cabee1 | -7.57582 | -44.38095 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7796e7e5-e34b-3a8b-8cfb-0d5ded51e863 | -11.53181 | -47.1058 | 2025-10-10 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80165aa6-ae27-36c5-9e4f-d8c8917f910f | -10.17278 | -44.55743 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46eb6e7f-a947-3121-96c2-98fe928efc8c | -12.6233 | -45.06497 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4896e5c4-5667-3b48-860d-7f20312e1e0c | -6.66113 | -41.98355 | 2025-10-10 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6863e1e4-a75d-3d6f-a194-dce651e4929a | -12.74552 | -45.85572 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d43f3677-94a9-3064-b5b1-e37dfea407f2 | -6.8186 | -42.79982 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f21391c5-3a4e-32b5-ae5f-ec2153ff6f0b | -6.45518 | -44.57852 | 2025-10-10 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a92634d0-6c9b-3fbb-b918-3bc7252acef6 | -7.26116 | -44.91315 | 2025-10-10 03:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ad91e92-fc34-37f7-bf61-e41d5c54bf74 | -8.51898 | -46.17801 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a82b78ab-2c1b-37af-b096-ae6c7e7c3a5d | -7.78964 | -44.05795 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7772370f-44e9-3ea3-a5b2-94b319b6a907 | -7.79474 | -42.60553 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebf2a71e-6aeb-360a-beaa-81641689d56f | -8.51248 | -46.14345 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b36affe-dd80-3f5d-9444-159c6024c142 | -7.79986 | -42.6066 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e85742c0-0586-39b8-a827-79d6f58fbdd4 | -12.62733 | -45.07378 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README12.md)
