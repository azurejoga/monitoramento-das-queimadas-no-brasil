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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74b8c4c3-b244-3858-8827-03127c09b160 | -17.34624 | -42.61515 | 2025-09-14 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d26bc22a-627f-39fd-b280-0fb327cc9cb5 | -6.16395 | -42.76225 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba41f075-4132-34d9-8380-bf4b41681af3 | -10.73806 | -46.43944 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5494284-f0b1-3dc1-acfd-af2d2ccded1b | -12.13637 | -47.59732 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 342f27db-3e5e-3f04-9d4d-9a5bf28408a1 | -11.30301 | -50.79527 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a616d299-9b13-3fd1-b872-5b09f37fd7e5 | -12.75803 | -48.00367 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f0757b3b-558f-3728-98cd-d6b4533782be | -13.94503 | -44.80629 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d40cb5d0-4840-32e8-b366-70da06cb801e | -10.75382 | -46.46857 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1492c759-2054-3516-81c8-db67190a4106 | -17.31764 | -46.08779 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b322e0a9-3d4d-366a-aeb7-7ca1c14cd198 | -17.2776 | -46.10415 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 84d3e0b2-c487-3952-86af-a06e04331074 | -10.32103 | -48.82466 | 2025-09-14 03:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9edcb306-a0f9-3348-beac-39ecc2cbbf49 | -12.81291 | -47.95538 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 928c5148-c073-397a-9892-12077cbc77a6 | -17.58915 | -42.7327 | 2025-09-14 03:49:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c30b758f-bd91-3907-9d80-bb943f89eafd | -15.91588 | -49.97106 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c5e3c0d-37aa-344f-bc31-b22261122f19 | -11.46835 | -48.70909 | 2025-09-14 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3647879e-449c-39b8-a3d0-5e38278ad52b | -13.93028 | -44.86137 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 87a9ea98-8f24-3212-aed7-46f77cf55197 | -15.76202 | -52.22615 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f726f10b-5e08-385a-99e8-8ee4db2ebe90 | -15.43879 | -47.35053 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ad412b6-ac95-3e2e-a9b8-049d45dc800d | -13.28734 | -43.7851 | 2025-09-14 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0ce93b4-9699-37b9-b6b8-6e77e9636fbb | -11.79641 | -44.69082 | 2025-09-14 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9c76f06-edfe-32b5-b5e5-e4f447353f5b | -6.17786 | -41.1576 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 16230755-f04e-3814-bdaf-c4bb9bceaee0 | -11.77999 | -46.63068 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5399c3ba-32b2-33f1-aa81-43ac19800f90 | -12.95488 | -47.9854 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ae0de81-57de-360a-80fe-e433c3f1cd90 | -17.41699 | -49.23913 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46be45c4-0a82-3081-b9e2-fbd1e3b7b9e7 | -5.21108 | -45.45735 | 2025-09-14 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a46f49a4-c8c3-3228-bb3b-ea6654cacf3b | -10.96051 | -49.5676 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20102c90-dcaa-35f6-8ec1-ceb1715285fe | -12.57231 | -45.66393 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b21f53fc-6e62-3736-b718-003b38dafb2a | -11.29456 | -50.8367 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c25a858-f6c0-3db4-a491-48edae2a6288 | -11.47555 | -43.60395 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c295ae14-e6cb-3819-8395-701916223f6b | -12.7997 | -47.96508 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17f079ac-9c26-3b48-b6de-4d0b36aac7dc | -13.88163 | -48.28539 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52b82a8b-bf1c-3616-b1bd-9b0d9a2e039c | -11.38412 | -47.71784 | 2025-09-14 03:49:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3b26719-0e0a-3e65-a513-1ad02e47a5ef | -15.20069 | -52.48915 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b719c4dd-b605-3a9c-8490-4e353afac00f | -12.08933 | -47.5686 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2a808d4-05ab-37b1-9f2a-8337998bce49 | -11.49732 | -43.70136 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 387c64cb-9e76-3d40-96d5-861225487b5d | -17.27845 | -46.09976 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4986fbc-df70-348c-8574-39a982a80beb | -14.36708 | -52.9444 | 2025-09-14 03:49:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 033747a6-b91c-3cfa-a729-c0cd6a0851cc | -12.25395 | -46.79419 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b164f44d-6caf-3f19-8218-341ad1cab907 | -6.92265 | -41.34532 | 2025-09-14 03:49:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42716758-941c-3fdf-9bf5-dab74baf2595 | -11.39847 | -43.52296 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d250e5a0-06d2-35a6-a9f3-35ce09476cc5 | -15.05169 | -42.25043 | 2025-09-14 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c3531af2-c862-36cd-977a-2df5ca886122 | -11.88432 | -50.54637 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0534d449-90b4-3e81-9888-25c236b0d85c | -7.17836 | -38.6777 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cf301090-964d-314c-9441-2bb27a67fe22 | -11.28254 | -50.8278 | 2025-09-14 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dad7cbff-70d9-3a83-9d76-d58c542dbbe4 | -11.46889 | -50.77763 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 00c534de-2bf0-3bb9-9fd3-6927f0604971 | -10.89452 | -47.21577 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f4681e1-4f80-3f00-9230-17c3d5eed220 | -5.94102 | -42.77176 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6444f5a6-597a-30a1-ad08-1f571d1bda9a | -15.03053 | -50.16355 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 50050148-e183-3b98-9575-6997fd9965ce | -15.75936 | -52.2518 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48d65034-fcce-352b-b2aa-9ad632290795 | -15.60337 | -47.94428 | 2025-09-14 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 23c87321-4318-3741-98fc-00bd4e6d55f3 | -14.33113 | -46.61843 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c03cd8ab-56b1-3ad1-8520-f7a638730989 | -6.68313 | -45.52158 | 2025-09-14 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e511ca31-1f95-3941-822d-61ac6175e443 | -16.83653 | -40.84988 | 2025-09-14 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 41d62c4c-4f6c-3e4d-9583-01aa7c57fcec | -14.43998 | -43.19904 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63d3b4af-68d3-3ff0-b06f-6854784cedd2 | -11.438 | -43.54909 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b50406a-e509-3225-88e3-1b3d4b44ecf4 | -6.33547 | -43.87558 | 2025-09-14 03:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 64066083-a397-3b59-8068-61fd76e11fc4 | -16.84056 | -40.84662 | 2025-09-14 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aeef4d60-8750-36e3-9b60-e05f1945a489 | -16.32617 | -51.53329 | 2025-09-14 03:49:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a182e17b-94b6-38e3-8314-a2874347596d | -12.61582 | -44.20129 | 2025-09-14 03:49:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2b9f522-d71f-3057-b291-68401f92ad73 | -6.42915 | -42.63352 | 2025-09-14 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 305085f9-f187-3573-8293-d652cafa1f0f | -12.806 | -47.96178 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a4e168e-a090-3252-a484-8b7f578d2ece | -11.35468 | -47.33407 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ca58f82-49bb-3169-a3ac-677e2c521cfd | -10.97289 | -49.57022 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 92ec974f-2bea-3307-89aa-272b8cecccbf | -6.17399 | -41.15688 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d8e3737-afcf-392d-87a2-64bc0f046b76 | -11.33002 | -50.83232 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0bdc799-ccd2-306a-b1bc-89a40f580f55 | -17.26023 | -49.27437 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b0a155b3-ec62-338b-a5a7-827c7d3f4fa0 | -12.61768 | -44.19883 | 2025-09-14 03:49:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acb24102-cf4f-359d-bfe8-140ef84f4e1c | -17.58475 | -42.7364 | 2025-09-14 03:49:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed14e3a5-c309-37ba-bbf9-5ab11bf138c4 | -13.93188 | -44.85277 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 314a740e-56dd-35ea-8fe6-8f252d19500e | -14.59902 | -46.33426 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6a49044-da6f-3999-b186-e72179668557 | -12.10083 | -44.85783 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8f24f3a-4dba-34c5-94be-1e07e96344da | -14.63133 | -52.03919 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d82710d3-d420-39b1-abbd-e48a35073dd6 | -11.49575 | -43.6362 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6d9641a-ee9a-36ea-9cbe-3109c9403d5b | -5.12903 | -45.11952 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0d5f5b7-f0cc-302d-b3da-0a31edc2d669 | -11.43041 | -43.53672 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97f494f1-bfc6-3bb0-8bdd-85dd5f7bec9e | -11.28374 | -50.82195 | 2025-09-14 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f7822b0-cdf3-3237-991c-ca8141ef27b2 | -12.72963 | -48.03089 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd4d4d81-0dee-3915-8c42-624e2b4049e8 | -14.61363 | -52.03452 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa63a410-c718-3fa6-89e7-08f23b606e93 | -12.06633 | -45.63128 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81315c90-70f2-3e69-bfe6-a4cf010c9023 | -15.04867 | -50.15651 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea044517-b894-307d-be84-c8d819edfb84 | -14.62866 | -52.11691 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0d701d5-6b2a-3b2b-9b0b-de74579e2bae | -11.3956 | -47.33675 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d51e96b-de8d-3622-afcd-3d51ae883ebc | -5.2222 | -45.45571 | 2025-09-14 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b47cc2e-9a12-35f1-a911-5e2123fb0705 | -14.43429 | -43.20834 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a37bab15-60d0-3c9f-aae2-f7b2154407be | -14.69347 | -45.14306 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96c4bc6e-06d4-3214-ab85-27b0785f5be8 | -17.27933 | -46.09527 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 251e7031-472e-3ece-9f19-26a54aae65a5 | -12.56033 | -45.65802 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff358999-f35c-3719-b112-5adf44c49163 | -6.1075 | -45.94586 | 2025-09-14 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e2e4b8d-df88-3545-be86-6f3a7ef5e946 | -14.19131 | -44.79622 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5845a9b-e999-3d2f-be4c-4d19e6d9f9f3 | -11.78727 | -46.64788 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e25a739-3dae-354a-afb7-e5485613d7a3 | -12.69949 | -48.30365 | 2025-09-14 03:49:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2450418f-1209-35ce-8df4-4ccb36b5db81 | -7.25117 | -39.39013 | 2025-09-14 03:49:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 98aab1dd-24ab-338e-9656-4967a72f092d | -5.94536 | -42.77243 | 2025-09-14 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 043328b4-3d40-3b56-b597-3a1b1104fff0 | -16.65555 | -49.78014 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 881a0e4e-3cc7-38c5-a2a9-b805d05a8d2c | -16.44061 | -45.69197 | 2025-09-14 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 268b0a0b-886e-397c-8370-2ae683f499e4 | -18.29623 | -45.11062 | 2025-09-14 03:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa4a03fb-2b3e-3b9b-9a71-e66ba0e0fcab | -17.26826 | -46.11475 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f03743f-3de0-3923-82ed-2f40690b7d70 | -14.10778 | -43.20713 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b63ab2c7-e5af-34cd-9c77-b30b93c6b71f | -11.38089 | -47.34237 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e97d666-098e-3987-a034-77c09bab7626 | -11.4726 | -50.78089 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README20.md)
