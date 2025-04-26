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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23a4a7c9-2271-3d1f-ab37-10670d01ac83 | -11.4152 | -52.9458 | 2025-04-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 05621daf-b906-37a4-bc08-819c3d6fa7a1 | -11.3963 | -52.9477 | 2025-04-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| ee38b29d-fc00-3860-9eb4-6f5788b7b2b7 | -11.3965 | -52.9269 | 2025-04-26 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 7b87ca3c-3d9e-3874-bb11-ecbdb19401b1 | -11.4152 | -52.9458 | 2025-04-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| cc3a556e-320f-3b86-96ed-2154a402abf6 | -11.3965 | -52.9269 | 2025-04-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2b5b0748-a067-3ba4-8f93-6dde8b80aea5 | -11.3963 | -52.9477 | 2025-04-26 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| b243b804-599a-3c5d-ac01-302171aa1590 | -10.1015 | -37.6231 | 2025-04-26 00:13:00 | METOP-C | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 299d1fd8-0944-3db3-88ba-52a6dd953ccf | -8.9396 | -44.2253 | 2025-04-26 00:13:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 593d352e-b8fa-3827-ba20-f33ac9048760 | -9.873 | -37.104 | 2025-04-26 00:13:00 | METOP-C | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 054919e5-7eaa-3479-9a6c-289789ba7d42 | -8.943 | -44.240799 | 2025-04-26 00:13:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95385527-d909-3bdf-a8dc-6bfcf054eaba | -9.5653 | -37.800301 | 2025-04-26 00:13:00 | METOP-C | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| f38232d9-e377-39d4-b857-1135afac5dde | -11.3805 | -52.904598 | 2025-04-26 00:13:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4b2dec-16a8-3023-ace8-187c43d41aab | -10.9727 | -42.173199 | 2025-04-26 00:13:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0774e4f9-7fb9-3752-aa5c-541392400805 | -11.3959 | -52.9328 | 2025-04-26 00:13:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3333a50-8a1d-34cc-852e-adf23b0163be | -15.6021 | -41.797798 | 2025-04-26 00:13:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb37d037-48cb-3121-b21d-835b8907b3bb | -9.561 | -37.782398 | 2025-04-26 00:13:00 | METOP-C | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| df9f4620-383f-3167-b6f9-507fa5c53e60 | -15.5907 | -41.792599 | 2025-04-26 00:13:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c7ea3bf-b964-30e4-a40e-82554d85c947 | -15.5989 | -41.782902 | 2025-04-26 00:13:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a4bf002e-1f56-36ef-b2e8-e80f90b700ff | -13.6592 | -43.788502 | 2025-04-26 00:13:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b591b8d8-1d00-3992-aa83-eb2aea1fb3f2 | -13.669 | -43.7864 | 2025-04-26 00:13:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2a17bc0-d061-303b-b676-37a023ddc0b2 | -7.4357 | -45.4165 | 2025-04-26 00:13:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4260559f-985d-3178-af34-bf152c37e3af | -10.1037 | -37.632099 | 2025-04-26 00:13:00 | METOP-C | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 1587db11-ad06-31f5-b97e-048b13796223 | -15.6005 | -41.790298 | 2025-04-26 00:13:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 89536889-3d43-3c28-a194-87b9175eade0 | -8.0917 | -43.101501 | 2025-04-26 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c7ef604a-cf19-3ba1-8481-954eec197f4f | -9.5632 | -37.791401 | 2025-04-26 00:13:00 | METOP-C | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 6a09b6d6-fd40-3006-8889-a7642d5ea274 | -8.0948 | -43.115601 | 2025-04-26 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82a0c62b-24aa-37c1-98ef-84afe883e461 | -8.9413 | -44.233101 | 2025-04-26 00:13:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb92d4b-b538-3573-be03-d11078968e47 | -11.3902 | -52.902699 | 2025-04-26 00:13:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9394a4e-230a-3101-b9af-83f9ac1bc3ea | -8.0933 | -43.108601 | 2025-04-26 00:13:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 163583d4-5b32-3a76-ae21-14a54686b5db | -10.0993 | -37.614101 | 2025-04-26 00:13:00 | METOP-C | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 2a212141-adbc-3f50-9d0c-9a7ea1f749d1 | -9.8633 | -37.1064 | 2025-04-26 00:13:00 | METOP-C | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| ba49b51f-3c05-31ae-9024-211c2e4fe6ff | -11.3862 | -52.9347 | 2025-04-26 00:13:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac7a6c6-63d7-3a4c-af76-074509386846 | -11.3963 | -52.9477 | 2025-04-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 523736cd-686d-3371-aeaa-bf82ea43d056 | -11.3965 | -52.9269 | 2025-04-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 7232757a-b4d2-3e4b-98dc-7c33b9908171 | -11.4152 | -52.9458 | 2025-04-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a48bff82-2f41-3025-a823-3d490c84f39c | -15.60065 | -41.78637 | 2025-04-26 00:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| b019070e-f9ac-3b99-ba9b-caf29ab72f27 | -13.66657 | -43.79162 | 2025-04-26 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8092ed91-9a11-3652-8fd4-71ff78c2a4bf | -17.27013 | -41.85912 | 2025-04-26 00:28:00 | TERRA_M-M | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9b6e6665-4c92-3692-aa40-73682849a195 | -16.61891 | -43.36662 | 2025-04-26 00:28:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0f5edd0-5b91-398e-a0de-457309f83d06 | -13.65771 | -43.79297 | 2025-04-26 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 047080f4-5178-3b53-9dc3-99740eb33808 | -15.60211 | -41.79637 | 2025-04-26 00:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 0828c504-8946-3a9e-81c7-ed38c44b13e2 | -16.62019 | -43.3758 | 2025-04-26 00:28:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16878f69-c36f-3f86-bae3-a17ba12370a3 | -15.59292 | -41.79797 | 2025-04-26 00:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| bef7e671-de6d-3e5a-ab8e-0cf1de72051b | -11.4152 | -52.9458 | 2025-04-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 994182de-4732-32ff-9a90-a20f156e4b7e | -11.3965 | -52.9269 | 2025-04-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 10a53e80-5d17-346e-94dc-badc7d827beb | -11.3963 | -52.9477 | 2025-04-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| e4fea99a-8245-3f0a-98b5-8f54c33da829 | -11.39678 | -52.94665 | 2025-04-26 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| cbdc6ad1-bb45-3a95-86e0-da27781b37d7 | -9.5571 | -37.79809 | 2025-04-26 00:30:00 | TERRA_M-M | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 63fad2bb-f47b-3890-8a53-2c43d9422b1d | -10.96804 | -42.18352 | 2025-04-26 00:30:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 08cd09ae-0f18-3882-bb5f-98027684259e | -9.56819 | -37.81234 | 2025-04-26 00:30:00 | TERRA_M-M | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 61c736b7-1309-3b95-a1e9-23467ce23bef | -9.57057 | -37.79557 | 2025-04-26 00:30:00 | TERRA_M-M | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 29.7 |
| fb59cf55-d19f-38cd-93ea-3a7f43610f37 | -9.56454 | -37.79025 | 2025-04-26 00:30:00 | TERRA_M-M | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 638c582e-46ca-32b3-838e-159459fc42aa | -10.97177 | -42.17669 | 2025-04-26 00:30:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e0b8f091-4dcb-3be4-8733-83df884fd92f | -11.41178 | -52.9451 | 2025-04-26 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| bc933e01-5185-3a3e-a078-57f7d6952c35 | -11.40001 | -52.97528 | 2025-04-26 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| cca980f3-3d79-30c0-a45e-f49973ea4f25 | -8.93863 | -44.2366 | 2025-04-26 00:33:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8f4dcb87-1ef0-34af-91b8-29e8e71820f9 | -7.43649 | -45.42001 | 2025-04-26 00:33:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 81616561-d3d0-3afb-88ad-d4135b432191 | -8.08603 | -43.11058 | 2025-04-26 00:33:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0f7f89fb-e0ea-38b5-b0ab-1fff5fedfeb8 | -8.94882 | -44.24437 | 2025-04-26 00:33:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 45c0a6cb-7b00-3faa-a1db-f725adb9b7ce | -8.94755 | -44.2353 | 2025-04-26 00:33:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d4c1ee5a-955c-3eb6-892e-3151fd83174f | -8.09538 | -43.10913 | 2025-04-26 00:33:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 628b1030-3980-32a1-91d8-81b779711dbd | -8.09684 | -43.11922 | 2025-04-26 00:33:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c5bf7983-e6f7-3127-8b26-75beaf429ac0 | -11.4152 | -52.9458 | 2025-04-26 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7cc7e29a-cb41-34c4-906f-641ac086a8d7 | -11.3963 | -52.9477 | 2025-04-26 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 2567cff2-f125-3af1-b78f-4563a21fdbb8 | -11.3965 | -52.9269 | 2025-04-26 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 455901dc-31e8-3f6c-8032-392cf7b16008 | -11.3963 | -52.9477 | 2025-04-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 9da583cd-aa73-399f-b19c-c00178b448de | -11.3965 | -52.9269 | 2025-04-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2adc0d07-aff3-39e1-a7af-1fe10fbe0d17 | -11.4152 | -52.9458 | 2025-04-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 34d32cca-6c02-3848-853a-d10c2734b806 | -6.5631 | -51.1126 | 2025-04-26 01:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 64f7c5cb-c1f6-3780-b516-154eb32a52cf | -11.4155 | -52.925 | 2025-04-26 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 7edbbe51-efa1-3cb7-85e3-03ffbee50957 | -11.3963 | -52.9477 | 2025-04-26 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 9512528a-0f04-3b10-b986-3f4b249abbd0 | -11.3965 | -52.9269 | 2025-04-26 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fb694851-c2c3-3efe-8b93-a92b02064526 | -11.4152 | -52.9458 | 2025-04-26 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7dbb21f8-d2c8-3b45-abde-82f931e6d80c | -11.3949 | -52.948101 | 2025-04-26 01:05:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16a43fc9-411f-33d1-967f-55343f63cdde | -11.4016 | -52.933102 | 2025-04-26 01:05:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49f47316-306c-3867-9c56-7901927a5687 | -11.4047 | -52.945599 | 2025-04-26 01:05:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23dafaf1-18cf-3ebf-ba93-7c4f42df817a | -11.3918 | -52.9356 | 2025-04-26 01:05:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5d8a788-2785-35ec-8b45-5c449ab39c40 | -25.407101 | -53.012299 | 2025-04-26 01:05:00 | METOP-B | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e732bc6e-2e27-3f7c-8188-ff44e195a1c1 | -11.3963 | -52.9477 | 2025-04-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 009580ca-357e-367b-8253-049723f4a67d | -11.3965 | -52.9269 | 2025-04-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| aed8b126-ef1e-36f6-9cf3-4ed99bec70b3 | -11.4152 | -52.9458 | 2025-04-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d71774fd-f950-3272-9acb-5702ba8fa8dc | -11.3963 | -52.9477 | 2025-04-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| c83826ce-06c7-3bc9-a73d-5f9def87e850 | -11.4155 | -52.925 | 2025-04-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| a2026b45-bbd2-391f-88ed-628254ec3f54 | -11.4152 | -52.9458 | 2025-04-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fa282d29-88fb-33e9-828a-7a1d7f0dcb87 | -11.3965 | -52.9269 | 2025-04-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3cda12bc-328e-3254-ac18-4224132b4423 | -11.4152 | -52.9458 | 2025-04-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| f66ec595-05d7-3fa4-8ba2-8b498f56ae03 | -11.3965 | -52.9269 | 2025-04-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7fa4df33-37b6-33db-9861-8f551f1dcba0 | -11.3963 | -52.9477 | 2025-04-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| c0b7265f-5a8d-3a7a-9055-492a41f21019 | -11.4152 | -52.9458 | 2025-04-26 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 7e9f3acb-77c0-35b0-aae9-d15ab00c4464 | -11.3963 | -52.9477 | 2025-04-26 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e2ab68b8-c2c2-3c8e-9f2e-414b1e8a7a01 | -11.3965 | -52.9269 | 2025-04-26 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9dad81dc-8560-3113-9083-cce069dd4ab2 | -11.3963 | -52.9477 | 2025-04-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2c57d902-f065-3ead-bfdb-7afcf55a9961 | -11.3963 | -52.9477 | 2025-04-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 20e0de28-a838-328b-80d8-bf9d5a1dc27d | -11.4152 | -52.9458 | 2025-04-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3f833ca8-43f6-3e25-b360-05dcc11056a1 | -11.3965 | -52.9269 | 2025-04-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e66912dd-10f2-3901-bc82-7e5868177888 | -11.3963 | -52.9477 | 2025-04-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3bd81209-73ef-3317-8ecd-1d6318b5ef48 | -11.4152 | -52.9458 | 2025-04-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2e090fa5-55de-3de7-bcdc-edc7ed039848 | -11.3965 | -52.9269 | 2025-04-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 11abda07-4613-30b9-b749-78eddd9112ed | -11.3965 | -52.9269 | 2025-04-26 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 594c82ee-2905-31d3-9bcc-2637514448df | -11.4152 | -52.9458 | 2025-04-26 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |


[Clique aqui para ver as próximas entradas](README2.md)
