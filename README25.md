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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44837525-bfc1-3b7b-81cf-62a51d707620 | -11.44959 | -50.21868 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 012b8e4f-ed69-32c1-a7d4-bf7d026676af | -11.70772 | -50.96825 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ca4ee4e-335d-3e6e-9981-2101df09795c | -12.23842 | -43.78302 | 2025-10-08 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a26540f-a89c-3a4f-b26d-da9f94c49c7b | -11.80005 | -45.0417 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 459ca91f-4af2-3b76-8a05-43e9ddcb61b6 | -13.39106 | -47.56599 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40092e72-5ed4-33f2-9f87-59fb1db0303e | -10.49771 | -49.1414 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 417825f9-838f-38f3-b438-9d6dae5f6ee7 | -11.72623 | -50.96697 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0f7c313-64a7-3345-9c1e-10cf2147049b | -14.9223 | -46.79401 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c3b7defb-a193-351b-b89b-9aedac67fec5 | -3.43404 | -43.15001 | 2025-10-08 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cac1000-2a34-3a3d-9ccb-677bf43b03bf | -13.74421 | -45.76076 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4eabb9e8-b688-35d7-88a7-36e231706158 | -12.13763 | -45.59459 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c14ee9f-8088-3112-ba8b-80ef2143afb4 | -9.97641 | -48.77976 | 2025-10-08 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4464269-53c2-3710-8f80-38fa12b59e99 | -10.1747 | -45.55278 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c0801507-97ec-3be7-939b-11e73f4c8c76 | -8.25368 | -50.0901 | 2025-10-08 03:49:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2540ccdf-8829-3314-8e09-fb41aabe54d8 | -11.71384 | -46.36003 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c19a13b-26a5-3015-9822-78f70e81f8ae | -8.46302 | -47.20513 | 2025-10-08 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b56f4109-d678-3767-8704-3ebb476856cc | -15.32039 | -46.16936 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c42275b5-0f19-3051-a488-c9c304790e22 | -11.90863 | -46.75142 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c469e96-253c-301e-be20-475fce33afa1 | -12.92498 | -46.82371 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e5fc0dd-defc-3a35-a8e0-b8176695f741 | -13.80949 | -45.79445 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ae18c00e-ed29-3175-abbe-0d44db0cb71e | -14.94597 | -46.80111 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6252fcf8-91e7-3b44-983f-86cf12dff81e | -13.38519 | -47.56827 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44c7df81-57f7-38fa-9e24-394f3aedf800 | -14.79503 | -41.63063 | 2025-10-08 03:49:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c34f3288-2f31-31d5-988c-a5285307ef6b | -11.7006 | -46.34829 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9be5b7d-1737-32d3-aa8b-688ff5659c7e | -10.86373 | -47.10389 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bef5102-90bf-350b-8c2c-e49ec34642ad | -11.7233 | -50.94797 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 45fa0529-21d5-311a-bf4b-2b3b0918f3a5 | -15.06918 | -46.62737 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 756f95b0-fdb8-3746-9e26-59554958ad69 | -8.46115 | -47.20838 | 2025-10-08 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 787f70e4-7172-3ad8-b377-4a3cfe7c968c | -11.68531 | -50.96472 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 373cce22-dd9b-38c0-9d65-8b23931c31f8 | -8.47673 | -46.27767 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35178f82-16f3-3405-9c7f-6f0d3b80c65f | -11.22719 | -47.76365 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 323b8db7-ae4a-34a7-bd16-ebda37f14d5a | -13.06368 | -47.94166 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 593abb5c-225c-3716-b05a-1e9c195789ad | -11.72452 | -50.95332 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ffe01c35-fff5-3a56-938b-e288321d83ae | -14.79785 | -41.63543 | 2025-10-08 03:49:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| edea207a-b2a1-3592-9e77-244ba1fdd802 | -3.89589 | -42.5493 | 2025-10-08 03:49:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 64e71b03-7383-3fd7-a49d-f5da878f4183 | -8.19766 | -44.19981 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 721eacef-5642-3740-91e6-b339894166ae | -11.85566 | -44.91658 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 634037ea-c5cf-351d-bac4-d18d2e53cb94 | -8.41127 | -46.80562 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8975101-7bf6-3ca0-b9d4-e9d0a89a09ae | -12.93329 | -46.86226 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9fb346cd-1a6d-321e-b998-fa487bac9acc | -11.76833 | -45.13624 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69733cbb-4f6a-3a42-9848-949d06bcb602 | -12.94721 | -46.84368 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46e3be58-1d25-317f-8eeb-a6eb7ae2e9a6 | -8.51758 | -46.29232 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f74ee1c8-fa78-374b-8d71-6ac21793f3b1 | -14.5319 | -46.6428 | 2025-10-08 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50ad343f-320e-3950-a0a5-d7ac15c8e1c8 | -12.32998 | -50.26501 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1af15fce-9853-3f67-a529-5d29e3b986c4 | -11.79179 | -45.11208 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d668de5b-f8e4-3410-8296-d621f4b6c3ef | -8.22132 | -44.19907 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4dd1fdb-9b25-3018-b471-bfaf1c436839 | -13.25972 | -48.04958 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a98c52d4-6596-364a-9701-0e10e44dfc41 | -12.99508 | -46.78207 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 669d37fc-96d3-352f-a50d-6a26c9a57e8a | -11.69978 | -50.96152 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f3e81752-844f-3bd5-87c5-d6c09ca5fb55 | -12.71929 | -44.37919 | 2025-10-08 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c18149e7-4e2f-30f3-9a43-74cc88b98a74 | -8.22328 | -46.8337 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb8f6016-553a-303a-aa49-7d3c77f54d0a | -13.49928 | -43.79095 | 2025-10-08 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 321589e6-fe9d-347f-acb9-11926ff6a56a | -11.38239 | -43.48996 | 2025-10-08 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a752893d-d501-36f2-ba72-d5185924c9ae | -8.61715 | -45.09903 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14eed731-8272-3bd8-b829-a54182600c12 | -14.92894 | -46.79165 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94e43547-7337-3ecf-ba3b-6c0f95dbddd0 | -11.78713 | -45.13736 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f37402b5-1fa8-3c6b-993f-b462ed94002a | -14.92727 | -46.79424 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5bbdc8b1-f27b-3308-9b8c-06ec1d8993e1 | -3.29237 | -42.6243 | 2025-10-08 03:49:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da99828e-6b23-34a4-9091-e3035f6b9bd4 | -10.35821 | -50.28721 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46307456-a392-34f9-b7b8-9c72c65e7751 | -12.37837 | -50.29921 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9632bd7-f554-310e-9cf8-1252b5353bd2 | -8.37547 | -47.05789 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57b0d499-fa68-33cb-ab21-c8ad44f16234 | -14.24518 | -45.86708 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b539971c-5f3a-3572-a644-474349217f7b | -8.11754 | -44.77387 | 2025-10-08 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29497c33-bc28-3012-b888-5aa5a6da6bb2 | -8.23207 | -44.19397 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ece6e850-f305-3ad1-85e7-91fc7c67dccb | -13.27753 | -47.56326 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 143a95b7-2173-3df9-94df-9024185152a0 | -13.26635 | -47.78724 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3ee8e78-0be0-3f6e-9c9e-f11dd7cba0f5 | -13.3745 | -47.2315 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27cee101-fa6e-371e-b2b1-8e13b216fbb4 | -8.25699 | -50.08934 | 2025-10-08 03:49:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2deeafc-c8c2-334a-a488-6eef8225b8eb | -14.55901 | -47.00238 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75ee1048-18b8-33b4-8014-cffcef4a1fae | -3.4514 | -45.59285 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 114ad4f4-071e-3009-bfd2-7cc60f197830 | -11.72272 | -44.29745 | 2025-10-08 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 735fa0a9-7e04-35de-a43a-6a338dd649b9 | -13.23775 | -47.79254 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19f7a21b-5c85-3f7a-8fde-3715437e2fd3 | -13.37699 | -47.24606 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 408eaec1-21e5-32b7-926a-59f2802a50b2 | -10.64668 | -47.45757 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc1798d7-ae47-344a-8d89-ab2ff44b2fbe | -14.71073 | -46.06205 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fe8c2c2-c120-342a-9ce0-766d33e00211 | -8.23205 | -44.19128 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fe86a7d4-2774-3e1b-82c6-96cf7d60c4e5 | -15.95124 | -42.60402 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 0fdc2806-08a6-332e-ae88-bd4a9e30cf68 | -13.72857 | -45.66767 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2167e42c-009e-310f-a161-9ce21be62f73 | -13.28891 | -48.48571 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61733cac-c6f4-31ff-a3d8-33c86c2693bf | -13.39771 | -46.70473 | 2025-10-08 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a774e7f5-d925-3a64-87e9-ec7d444c0df5 | -8.18397 | -43.33865 | 2025-10-08 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3200d663-e95c-3220-944b-491a8cd57b6f | -14.36502 | -45.23599 | 2025-10-08 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 569f2467-4bdc-374f-b26a-fced44a791e0 | -8.51936 | -46.28266 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f874566-6e97-3bcd-b001-fa085daff9d6 | -13.34382 | -47.55709 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfb0953b-0a23-3a1e-a341-876beb8243ce | -8.23285 | -44.1866 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d0e9a131-fe2f-3501-998a-782a7bf2b376 | -13.24849 | -47.79401 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fca9287-98d2-3cbe-a5bf-68309aa48258 | -10.734 | -47.66005 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f48ebed7-e4e0-3199-84cb-24ab04839004 | -12.2433 | -43.7797 | 2025-10-08 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a28f25b-63f9-3768-beff-5d7867ced056 | -11.18442 | -49.78236 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7121e880-830d-312e-b362-299bdd1bda10 | -13.79295 | -45.80648 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d849b602-1260-33bb-81c9-49d58a1ce86a | -13.27574 | -47.15258 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e870cc61-e63c-35cb-9e9c-88dcd0bda700 | -14.71743 | -46.001 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d0a072d-7fd9-3a7a-9996-37de623a4871 | -14.77306 | -46.00554 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 718bc46c-5cce-3209-bc8d-b9ab65161264 | -13.2259 | -47.19105 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8aa55f33-8669-3b75-a78d-32a924e4a9a9 | -8.68253 | -44.72713 | 2025-10-08 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| afe39d08-1841-3c7a-99c7-0d79911cb0f3 | -8.46745 | -47.20548 | 2025-10-08 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5a4eea3-a195-32e4-bd3b-f4d6f350ab6f | -14.91604 | -46.80685 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ec486491-034a-3753-b4e3-0102ac4e28c4 | -9.97486 | -46.64477 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c289c846-f1b1-3adf-82fc-7911ed1ee854 | -11.79466 | -45.04543 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 852fd457-da46-368a-9667-42bb6b1a8e00 | -9.17223 | -47.82753 | 2025-10-08 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README26.md)
