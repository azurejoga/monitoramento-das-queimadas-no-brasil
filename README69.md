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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f985f62-2a0c-3c8f-8563-ee3eed3f48ea | -10.6641 | -54.1491 | 2026-09-14 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 4466b526-82a0-3398-8848-649180c403ba | -15.5572 | -48.7953 | 2026-09-14 13:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a5f1b9ca-060d-3b8f-b74a-c1d3f153278d | -10.6643 | -54.1286 | 2026-09-14 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9d487f06-1668-36a9-a48a-d50dc05dacf7 | -5.1255 | -55.955 | 2026-09-14 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| db1ce381-78ba-3db7-a773-e5276c25e89f | -15.5768 | -48.792 | 2026-09-14 13:10:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f97afe60-573f-3989-81d8-30bdd2099d5a | -13.4453 | -43.8366 | 2026-09-14 13:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 91caaf8e-24ad-3ecc-9105-dde60204f751 | -9.494 | -45.459 | 2026-09-14 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| fb0ed7b9-6a3f-3cd4-859c-dd0af81376ef | -9.3755 | -50.1779 | 2026-09-14 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9e1d3c80-5d1a-35d4-95f8-9df60a3b5245 | -9.4325 | -50.1299 | 2026-09-14 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| f45f0ffc-b9aa-3121-991e-d7bfa07dafcc | -14.1861 | -47.3844 | 2026-09-14 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 1c77f4d0-4dee-3619-b4bd-d8ddd4ab24b9 | -10.5484 | -51.2945 | 2026-09-14 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 77c8bf16-65d8-3183-951e-392bf7926977 | -14.1666 | -47.3876 | 2026-09-14 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7365f2ac-54b0-35fc-985f-e0364023e990 | -7.0164 | -44.6413 | 2026-09-14 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 795568de-7398-3e0b-b105-ec8b4bc13a44 | -14.1856 | -47.407 | 2026-09-14 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 84a63fd5-1125-37f2-99cf-c66ce686716e | -3.8042 | -44.1072 | 2026-09-14 13:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 19cb3fa5-c82e-3036-a7ed-13b404b5a39f | -13.2867 | -51.3046 | 2026-09-14 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2c762537-11b3-39d4-92e0-7a58db6d3bdf | -8.6194 | -44.4357 | 2026-09-14 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 807.6 |
| da8ff1ea-31d1-37b7-9121-545122a2431d | -6.1111 | -57.6645 | 2026-09-14 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| bf4c4c16-b3f9-33d3-bb61-3e932f9ef6ad | -10.6958 | -47.5175 | 2026-09-14 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a6a9d4fa-6615-3765-917e-75e6658ad505 | -10.7145 | -47.5374 | 2026-09-14 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 12dbb5db-d170-3ec2-ad94-9848d824e9da | -6.6767 | -58.7105 | 2026-09-14 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 32e03c29-185d-3e3e-a10c-f5cdaf2454c4 | -2.9579 | -50.3988 | 2026-09-14 13:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b1899186-f7c5-38a7-bbec-c143026414a5 | -6.5837 | -58.8498 | 2026-09-14 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f30e5446-01cc-3eae-93ce-0ba328f796f2 | -10.6827 | -54.1679 | 2026-09-14 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| af22bee3-b44c-324e-86b8-ba8d681a189e | -7.4713 | -45.961 | 2026-09-14 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a4949f3e-4bdc-36c9-b879-337c38b053d9 | -7.1048 | -41.7971 | 2026-09-14 13:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 126.5 |
| 6d29e0f5-e6d5-3cca-b299-984bec5910f6 | -13.4458 | -43.8128 | 2026-09-14 13:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 0a6df1c9-e1b6-3356-883e-95ebf9fc0852 | -7.1051 | -41.7731 | 2026-09-14 13:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 725e96e1-331e-313b-bea0-55acf8712623 | -3.4272 | -58.2138 | 2026-09-14 13:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 88eaadc2-95a2-35a4-8130-7198d0c3e32a | -3.4089 | -58.1949 | 2026-09-14 13:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4c284501-8c83-368d-b151-d708c2bb8157 | -13.4264 | -43.8163 | 2026-09-14 13:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 7da6a692-d325-3af2-853b-7cdcbcfc93df | -10.6829 | -54.1475 | 2026-09-14 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 159.7 |
| 37550370-c151-3847-8633-606eac289cb4 | -3.4089 | -58.2142 | 2026-09-14 13:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 483a5314-c20c-3abf-85e7-19b76029fce4 | -8.8 | -45.88 | 2026-09-14 13:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6621de17-2917-31c6-8c29-2e740cfa6575 | -10.84 | -46.34 | 2026-09-14 13:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43e1006e-4616-3bbb-aeb0-64918c2ded75 | -2.91 | -50.4 | 2026-09-14 13:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de570c31-6aa6-34a0-848b-6616a7cb1047 | -13.2863 | -51.326 | 2026-09-14 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 917aae55-d3db-3bc5-afe9-8f93f7b2babd | -2.6784 | -57.5504 | 2026-09-14 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 2748e2e6-4fb4-35f8-a853-08570dc57c15 | -10.2926 | -45.3161 | 2026-09-14 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 46d4d202-1ec4-373e-b95c-24f1ca4289b6 | -2.6601 | -57.5507 | 2026-09-14 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c73097a8-67d5-3b8d-aad0-371d43114bfa | -3.4272 | -58.2138 | 2026-09-14 13:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 9ab67697-b168-38df-aad2-ead77838e275 | -11.9356 | -49.7535 | 2026-09-14 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 50300814-f6a3-3c26-90db-7c1b566b35d6 | -10.6958 | -47.5175 | 2026-09-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 61da364a-18f6-3b0c-8b92-b5fe215dc0cc | -9.494 | -45.459 | 2026-09-14 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ede2881c-d124-34ce-9b3c-2f0b95dca314 | -9.4936 | -45.4818 | 2026-09-14 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 5b8e08b7-10b8-383b-8e79-c856bfc0125a | -13.2867 | -51.3046 | 2026-09-14 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| cd888eea-2938-3567-b8c2-bb3e03e892d7 | -10.7145 | -47.5374 | 2026-09-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 15f81b58-b498-3c90-9ad7-46929245d517 | -11.2391 | -43.4413 | 2026-09-14 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| dee37762-f652-3928-8e09-6a6622ca045a | -9.5126 | -45.4796 | 2026-09-14 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 644c52ef-8bb7-3380-89fe-bae57e946f01 | -3.3493 | -59.8288 | 2026-09-14 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b383be8e-0719-378d-aa04-b829e0184b74 | -6.5837 | -58.8498 | 2026-09-14 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 1fa98270-56af-3027-98bd-5b42fd883f35 | -10.3116 | -45.3136 | 2026-09-14 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 5280a01f-bb52-3184-a386-8356d015c10f | -8.7634 | -46.4194 | 2026-09-14 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 411.1 |
| 60874e12-f73f-3037-bdad-7fa0c7957fb4 | -13.4453 | -43.8366 | 2026-09-14 13:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 0e0881fb-41fd-327d-9a64-446615276894 | -12.4901 | -41.4012 | 2026-09-14 13:20:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 111.1 |
| cfa42274-0892-3a61-8a70-d53c7afda672 | -9.4328 | -50.1086 | 2026-09-14 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 3fd521ca-6dd1-3a38-8b6b-52682995dfac | -10.6829 | -54.1475 | 2026-09-14 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 4ced378a-d22d-3eb3-8779-8704fd263ac2 | -3.4089 | -58.2142 | 2026-09-14 13:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 0230f7ba-c39b-37bf-8447-c25aeb9f50b3 | -13.4458 | -43.8128 | 2026-09-14 13:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 238e3260-edaf-3248-98a0-a0503f326eec | -4.115 | -60.6886 | 2026-09-14 13:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| b0c41e2e-a712-32b9-bdb0-09148051c86f | -12.2249 | -39.2952 | 2026-09-14 13:20:00 | GOES-19 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 139.8 |
| 1111437b-5520-368e-87f0-5b8f5dc85cee | -15.5763 | -48.8144 | 2026-09-14 13:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 9f61c65a-c1ac-3ca1-a3fe-9afbd250feff | -9.3753 | -50.1992 | 2026-09-14 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 93726e53-ba16-32f4-a695-561abd4efb27 | -14.205 | -47.4039 | 2026-09-14 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 60b31970-9e27-3d75-b51e-095a20a2cf7c | -8.6194 | -44.4357 | 2026-09-14 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 7d47c9d3-bfa4-36c1-970f-cfb8121c3094 | -2.6785 | -57.531 | 2026-09-14 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b93cb015-7248-3056-878f-d4e165eec1d1 | -8.8081 | -45.8753 | 2026-09-14 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 37c453ab-a3ea-31e6-a007-1433a8b55fb8 | -3.4089 | -58.1949 | 2026-09-14 13:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 57999379-ab07-32fd-b93c-a545bb522ba0 | -10.6955 | -47.5397 | 2026-09-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c245fd46-4264-39e3-9b98-822f72011a49 | -9.4325 | -50.1299 | 2026-09-14 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| cb19a781-eb56-330c-913d-6e63742c10c5 | -8.7445 | -46.4213 | 2026-09-14 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a09fb75d-a706-3672-864a-bb8de5397b64 | -9.3763 | -50.1139 | 2026-09-14 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 66addea2-da17-3702-b6b0-b88cc33b597f | -10.433 | -48.6474 | 2026-09-14 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 8a7ab3c7-71f1-33b4-97c1-d8ef56d17b84 | -10.6641 | -54.1491 | 2026-09-14 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| bcc5ea1c-9407-30f3-9563-0d66aad64a00 | -2.6602 | -57.5313 | 2026-09-14 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7963bb3a-9a51-3de9-9906-af150cc9280d | -13.3059 | -51.3022 | 2026-09-14 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 74cad194-d756-3693-9995-9f75cfc8a998 | -10.6643 | -54.1286 | 2026-09-14 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 0e328728-fa22-3340-88f7-7ddb1a6509c6 | -3.1697 | -58.6437 | 2026-09-14 13:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c6bf0102-7ddc-381f-a8fc-0bb7e086d8b2 | -9.3758 | -50.1565 | 2026-09-14 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 6d5e738a-27f5-31b4-b1cf-0d360ee2982c | -7.0859 | -41.799 | 2026-09-14 13:20:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| b83eca36-a0ff-356e-ba4c-48cc04a5f381 | -13.4264 | -43.8163 | 2026-09-14 13:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| b365cd39-8f10-3801-b741-cc0d3e601cf8 | -5.1255 | -55.955 | 2026-09-14 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| c98b5241-77d3-3418-b378-162d008daf3c | -9.3755 | -50.1779 | 2026-09-14 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6a624608-bbd5-3da1-a6b4-72967f95a88f | -7.0166 | -44.6184 | 2026-09-14 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a454d559-b56e-3917-aeeb-90eaad85ef68 | -2.6784 | -57.5698 | 2026-09-14 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| fe476b02-1dd4-312a-bfce-ef055924bb74 | -10.6827 | -54.1679 | 2026-09-14 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| e8c44898-a5a8-3bc9-8637-461c278dd0d4 | -9.4513 | -50.1282 | 2026-09-14 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6474853f-3b00-3402-8ab4-32b5c2da63aa | -15.5768 | -48.792 | 2026-09-14 13:20:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f56bd71d-87b8-397c-a199-569a4e1a6720 | -13.3055 | -51.3235 | 2026-09-14 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 0762159e-c3d5-38bc-a41b-716432232fb0 | -6.6767 | -58.7105 | 2026-09-14 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 143.5 |
| bae67715-e82b-3ec6-bcba-3d4f35cb888c | -3.8042 | -44.1072 | 2026-09-14 13:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| acd6e203-cf56-3990-927d-7afc0e04673d | -6.1109 | -57.684 | 2026-09-14 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 378f35b2-861f-3515-9832-d322999642ef | -3.7855 | -44.1081 | 2026-09-14 13:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1837b008-e93b-371c-b34c-0c1086b80cfe | -10.6638 | -54.1696 | 2026-09-14 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9f8f69a4-ce38-3e0c-bf7d-5311c9fc61e0 | -15.5572 | -48.7953 | 2026-09-14 13:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| b54ea140-88ec-31db-a6dc-1e9dff0c3ca9 | -10.2922 | -45.339 | 2026-09-14 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 90227ebf-33d5-30e3-be96-33d723ed958e | -7.1048 | -41.7971 | 2026-09-14 13:20:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| e0778dac-8deb-31ec-aafe-d6b706fac40d | -15.5572 | -48.7953 | 2026-09-14 13:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 8c9a14da-98cf-3124-af69-d07a2a5632f3 | -7.0164 | -44.6413 | 2026-09-14 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 895bca0e-ea50-39e3-8488-b5c4e24cc15e | -9.3758 | -50.1565 | 2026-09-14 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |


[Clique aqui para ver as próximas entradas](README70.md)
