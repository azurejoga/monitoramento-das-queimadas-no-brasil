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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 299d918c-7c57-3c95-a4bd-67a18e6b08bc | -2.6556 | -48.51673 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3e1ada8c-60c2-3102-8ce9-3e9d47e9201e | -2.63763 | -48.50147 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70c6e5b4-941d-3b9b-a83c-69854356f92f | -7.96731 | -50.00426 | 2025-11-05 03:51:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7305a76c-9e4b-31c3-921f-f97ca5d69820 | -8.69187 | -40.54075 | 2025-11-05 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3fa68f57-923b-327c-b7de-b2d9f95aa432 | -2.82654 | -49.42123 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd450ece-01d7-397a-9264-8ab843932e24 | -3.40936 | -44.44101 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cae96ecc-0a93-38ae-9c61-7bcaedf88130 | -4.46112 | -43.22934 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ad1541d-e42c-396c-8b27-30d2a11264b0 | -2.83584 | -49.40895 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35102180-ade2-30fd-9cce-69a9b8930653 | -5.32219 | -41.24286 | 2025-11-05 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33f7cc50-07af-3635-98c7-785ee5af508f | -4.7106 | -46.43969 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 540190ff-f26e-3a24-b06f-69af76e0b984 | -4.46649 | -43.22546 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7aab18d7-c64a-3a31-91eb-1fcf8464769b | -5.45889 | -45.39905 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c49ec4d2-e6af-39f3-82f4-10e4a72a7a71 | -3.40837 | -44.44687 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 781ff5d5-5806-38e7-ad63-76d929484350 | -7.54567 | -45.85072 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e21a0a27-aff7-35ca-bebe-565a8a580b34 | -4.66529 | -44.52599 | 2025-11-05 03:51:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37dd7153-debf-3f2a-b746-2a80c096051f | -8.3187 | -40.44896 | 2025-11-05 03:51:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5ca4287b-26d1-3a87-b9d7-a4b5d60db859 | -4.51307 | -45.42954 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f79cae1c-46d5-32cd-b153-82d1520d8fb4 | -4.41293 | -48.94942 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfe67b95-097e-3c99-b55f-886d074a0a98 | -6.06297 | -47.30845 | 2025-11-05 03:51:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dc7ed0d1-698b-3b32-bdb4-0e329db137a9 | -4.10951 | -48.01971 | 2025-11-05 03:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3520ae89-5107-384a-92d1-6e2e8984fbf4 | -2.72606 | -47.38928 | 2025-11-05 03:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3a9724f-f24a-37c5-80fa-fee2eaee8bfd | -4.30864 | -45.36997 | 2025-11-05 03:51:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1dc49fe-c0a5-3ef7-9a45-0d1e685db432 | -4.76188 | -42.65191 | 2025-11-05 03:51:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 45db9f55-b905-34fa-b0e4-c4e896566f53 | -11.01878 | -42.73064 | 2025-11-05 03:53:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8bf9e1a1-0f3e-3149-bee2-9066125c360a | -10.37978 | -47.75456 | 2025-11-05 03:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 474ccfd0-2738-348d-bb00-c286e063efb3 | -13.56696 | -42.76302 | 2025-11-05 03:53:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2869e63d-f096-392b-9c72-f21d891d2d0e | -12.32676 | -43.43859 | 2025-11-05 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa90b64e-5cc0-3420-a97a-864c8330c56d | -10.40513 | -44.38512 | 2025-11-05 03:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65daa702-86bf-3520-b9a1-64f88c48743c | -13.04377 | -43.22819 | 2025-11-05 03:53:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0d6eb01-2c20-31e0-9481-d194da9efb15 | -12.98357 | -41.15034 | 2025-11-05 03:53:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a5a6ecd-75de-3aff-8144-146f60ec35a3 | -16.08378 | -41.45122 | 2025-11-05 03:53:00 | NPP-375D | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a74ac282-4173-3c6c-85fe-9c0e4f8c9fe3 | -11.45219 | -45.14741 | 2025-11-05 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b167f9d-775f-316e-bd16-4622bddbdf33 | -10.3118 | -42.41597 | 2025-11-05 03:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 35290c49-e022-3de6-9aff-edb410210133 | -10.37414 | -47.75363 | 2025-11-05 03:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd9c3ca9-2f6a-362e-a3c8-1eef9276b308 | -11.00975 | -42.72754 | 2025-11-05 03:53:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0705308d-7356-3b62-a4b1-ad8f43d217b2 | -13.01132 | -43.64887 | 2025-11-05 03:53:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 10ce8422-6710-3d91-b0d0-61c08b548b61 | -12.87465 | -38.34932 | 2025-11-05 03:53:00 | NPP-375D | LAURO DE FREITAS | BAHIA | Brasil | 2919207 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9da416e7-cdd3-3322-8fda-6eb147de7155 | -11.29781 | -44.6187 | 2025-11-05 03:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3105c932-edf1-367c-8c2f-c440268e9c8a | -10.37904 | -47.75845 | 2025-11-05 03:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e406e9da-b46a-3a8d-9095-8f91f96427f6 | -15.30895 | -41.70979 | 2025-11-05 03:53:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 663bd8c3-fa20-36f6-b425-ce08b80e292a | -11.29699 | -44.62325 | 2025-11-05 03:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 28433a44-94c7-362b-be53-34df30778710 | -13.01403 | -43.64842 | 2025-11-05 03:53:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee192832-eb15-3a22-ae38-8b3fef562ebe | -12.33598 | -43.64881 | 2025-11-05 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51d61084-51c7-3914-bbf9-d82ceb7a2d69 | -11.26512 | -41.0794 | 2025-11-05 03:53:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| da45fe1a-305c-3201-813f-b158db88c4b6 | -12.80805 | -39.82492 | 2025-11-05 03:53:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf0c9250-6f70-384e-9810-19c49b85ded5 | -11.30146 | -44.62417 | 2025-11-05 03:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d336a145-2235-390e-bb6c-acd62c25eb1c | -11.62942 | -41.46836 | 2025-11-05 03:53:00 | NPP-375D | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 97a69c03-806f-3f3f-a6c3-388c972cdc19 | -10.30814 | -45.01954 | 2025-11-05 03:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b2a6af2-7e31-3ad7-9f4a-f53ffb732e7b | -16.81323 | -41.00053 | 2025-11-05 03:53:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 02aaee7b-57bd-3268-88b7-e244d7a234ea | -11.0099 | -42.73441 | 2025-11-05 03:53:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 39a2bf97-08e8-3fe6-b877-98f202590b5c | -9.79882 | -49.30727 | 2025-11-05 03:53:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b590ed0f-73ab-3645-98a6-77aec7c203e9 | -10.38539 | -47.75561 | 2025-11-05 03:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa9ee98d-f468-3ad1-885c-829fd30d75e0 | -11.30228 | -44.61959 | 2025-11-05 03:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1749263-ec0b-3d83-a7c7-15d28b2eb871 | -11.84722 | -43.71935 | 2025-11-05 03:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 374d5857-d6cc-345d-b595-24d60d1a0f3e | -15.81677 | -43.33223 | 2025-11-05 03:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bcc96d1-032d-3b2a-8a01-0e6a55ce9b79 | -11.01373 | -42.72826 | 2025-11-05 03:53:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0003d12b-18ed-31e6-b0b4-77341e95cfd3 | -11.01083 | -42.72919 | 2025-11-05 03:53:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c637faa1-507f-30c7-81aa-2d725c5959c6 | -10.40961 | -44.38594 | 2025-11-05 03:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7f3e41a-b75b-36d7-b100-49376d25bae5 | -11.01771 | -42.72899 | 2025-11-05 03:53:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9240011b-043b-30d4-b7cf-ee664a2fff87 | -13.10326 | -43.31684 | 2025-11-05 03:53:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb1e4827-d66e-3c48-a8ca-36c471c359e4 | -11.00885 | -42.73277 | 2025-11-05 03:53:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 5e22e747-13e5-3101-80a5-df2422b7142e | -12.33531 | -43.65258 | 2025-11-05 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15800989-b064-3697-a504-440103d650e1 | -11.01481 | -42.72991 | 2025-11-05 03:53:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 6ac30e69-6d1c-3424-b886-333a34fb0b43 | -13.5097 | -41.00699 | 2025-11-05 03:53:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6bf8ad2b-6d33-3a46-a656-beecc900d8be | -16.61593 | -41.85154 | 2025-11-05 03:53:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 101f5b59-f4c8-3aed-a0b7-fd7103ceac5d | -10.41852 | -44.38784 | 2025-11-05 03:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16f03dab-1734-321c-afac-327ed3df3843 | -10.41325 | -44.3914 | 2025-11-05 03:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc1091a1-0f7b-3e0d-b377-70b623ae70f7 | -15.7284 | -43.37348 | 2025-11-05 03:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98477273-c422-3411-9c0c-d6e567e587f8 | -12.68307 | -43.17175 | 2025-11-05 03:53:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b46a8a1a-b5d2-3d87-b5b6-1685d46bbee6 | -10.38466 | -47.75946 | 2025-11-05 03:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a5b5bb6-8742-3e04-88c6-6663dfa9d431 | -15.71351 | -40.88051 | 2025-11-05 03:53:00 | NPP-375D | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6ae1d8ce-808b-39f5-9d85-9cbe66605fa1 | -10.50313 | -42.40437 | 2025-11-05 03:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 3e0fc1a9-e75f-333c-8888-2e485427d2ef | -12.65977 | -43.92514 | 2025-11-05 03:53:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c200e021-040f-36c9-b45c-ff17bb64cd56 | -13.04775 | -43.22892 | 2025-11-05 03:53:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 743c96bb-d4ca-365b-b5d6-3a4f4fdba2a9 | -16.61239 | -41.85098 | 2025-11-05 03:53:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1b939ca3-a5f8-36ea-9b46-6864beb6bd6a | -12.33164 | -41.09347 | 2025-11-05 03:53:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 121d7ede-ff55-39b5-98fb-850f8b4f91b1 | -10.37484 | -47.74999 | 2025-11-05 03:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3193fea5-ea91-3040-bbb1-8c9e4b90117d | -12.85246 | -43.76555 | 2025-11-05 03:53:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cbf9a67-465c-317c-922a-f5bc33c1d992 | -10.38608 | -47.75199 | 2025-11-05 03:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c9f33fb-acaf-3cf8-9ee3-3a37c1fdc733 | -12.66047 | -43.92129 | 2025-11-05 03:53:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2bbf797a-c68b-3bac-8ae6-aecf889b7421 | -15.31024 | -41.71166 | 2025-11-05 03:53:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9d27341f-2df5-393b-9002-5278f39bd495 | -10.48394 | -44.30609 | 2025-11-05 03:53:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 750cdac5-5778-3e16-adf4-2085e81b4276 | -9.79257 | -49.30611 | 2025-11-05 03:53:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c963fab0-901c-3765-83aa-334922149318 | -10.38046 | -47.75097 | 2025-11-05 03:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fed319be-5db0-3542-be3e-863c0131b775 | -16.81663 | -41.00121 | 2025-11-05 03:53:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 310f7b4c-c5c6-3c4d-8d64-04b01672d321 | -11.8514 | -43.72011 | 2025-11-05 03:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 256082e9-ea9d-3702-a7cd-76e67fa9135d | -12.85179 | -43.76933 | 2025-11-05 03:53:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62fd565b-4047-3b56-8cae-28120b70b01d | -19.34234 | -45.84544 | 2025-11-05 03:55:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c400e6ce-cfc3-394a-86a6-128333830396 | -20.04814 | -44.43775 | 2025-11-05 03:55:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c76acc9a-e432-3ad6-a70a-95d7c498e74d | -19.34084 | -45.8479 | 2025-11-05 03:55:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6db85d46-2b67-351f-aad3-cb6dd77c991e | -17.98478 | -43.43491 | 2025-11-05 03:55:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb2ba6b2-b1fc-3518-aae3-91a3265cf55b | -19.34154 | -45.84972 | 2025-11-05 03:55:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c5955ef-f8b2-37b2-bd39-5d9c903f6e9e | -17.98393 | -43.43963 | 2025-11-05 03:55:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ba10fa7-63c2-36c7-9b4c-b0d2d85d3322 | -19.34506 | -45.84869 | 2025-11-05 03:55:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14061aa8-6216-3160-9d8c-49c03cf53daa | -18.6957 | -41.87305 | 2025-11-05 03:55:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01a1f9aa-2931-3dfe-b148-f71e7e064a15 | -17.78639 | -40.10089 | 2025-11-05 03:55:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3ecf5098-ff57-35ac-bdcb-fdb7f7422c8c | -19.37588 | -44.54598 | 2025-11-05 03:55:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 270e3c1b-3e0d-30fc-8fdd-3dfe7d13a485 | -2.6508 | -48.52 | 2025-11-05 04:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 8dc418e7-5388-3365-b22f-dbd27ed796fe | -4.4259 | -48.9465 | 2025-11-05 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| cab67a74-685c-3d86-813a-b5acfa0c3889 | -5.4707 | -43.5674 | 2025-11-05 04:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |


[Clique aqui para ver as próximas entradas](README16.md)
