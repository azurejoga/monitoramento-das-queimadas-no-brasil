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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b86bfed-2047-3ccc-834e-954800897d67 | -11.82021 | -47.07164 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4668278-0a6c-31aa-94e6-bbea45dcc929 | -7.1805 | -39.11631 | 2024-11-18 03:49:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bda56cbe-0647-34f3-8dfd-efc7d910a811 | -6.00481 | -46.4008 | 2024-11-18 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bed39aa1-9a87-3d85-a141-891ed197615d | -7.53824 | -35.31724 | 2024-11-18 03:49:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 09ad0685-3fc6-3292-b991-13affdcd0092 | -6.58927 | -48.03943 | 2024-11-18 03:49:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d300fdf7-66a4-3379-a510-3056d79074e3 | -12.72115 | -43.95953 | 2024-11-18 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a168398-9797-3e3b-b96d-36dfc296e2fd | -7.39721 | -42.76752 | 2024-11-18 03:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 39665eeb-496a-39cd-ba6b-298db69a1361 | -10.86465 | -47.69384 | 2024-11-18 03:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbf0ffaf-92fa-3329-9792-37d55e82f757 | -12.45948 | -45.35866 | 2024-11-18 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee267be6-8444-30b2-b699-aabbbbcc3836 | -17.00895 | -49.7824 | 2024-11-18 03:49:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee05a1c5-c14b-3db8-83be-0972b7c28c1e | -11.85353 | -46.93436 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b58d02af-8080-3083-8750-7dc86deee889 | -7.5354 | -35.31309 | 2024-11-18 03:49:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa3a0221-319c-3640-8867-3fe802d66f47 | -11.85708 | -46.93833 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d75afa67-c60b-36f2-95cf-df63c2b94f97 | -11.81559 | -47.06717 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc5b76ea-5edc-3abf-9462-f2e7d00b2f33 | -5.33037 | -44.93375 | 2024-11-18 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2adc6270-8687-3a5c-9eb4-fd94dabef3c7 | -7.09454 | -39.26659 | 2024-11-18 03:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e66033ae-f04c-34cb-918e-f9447df139e2 | -6.99037 | -39.65899 | 2024-11-18 03:49:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 359dcd31-eca2-3761-9c8d-e4d41680234c | -11.96712 | -44.22643 | 2024-11-18 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acda747e-d085-3c11-be41-37fb658e0d9c | -5.24053 | -44.75601 | 2024-11-18 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6362c8cd-bc59-36f2-b59b-3953ff7be239 | -7.6877 | -35.07201 | 2024-11-18 03:49:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 31617cbf-19e9-3f25-bb3c-1243a32991ef | -7.25282 | -35.04109 | 2024-11-18 03:49:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad287f2c-7c20-33e1-94fb-47f7f6e0f1b5 | -6.13656 | -44.72324 | 2024-11-18 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60e00940-f689-3b02-b57e-eaffb72940cc | -6.48958 | -47.50357 | 2024-11-18 03:49:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f2b29c7-7e60-386c-86a0-e2806ba51aaf | -12.72187 | -43.96065 | 2024-11-18 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7d45bfd-d37c-3c99-9543-b454b11b7cb3 | -6.86082 | -38.87809 | 2024-11-18 03:49:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f6e7938e-bd21-3f38-8dfc-57de706dd7f8 | -7.18398 | -39.11689 | 2024-11-18 03:49:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ad6f6124-d522-38d2-8570-e1430fd014c6 | -5.75131 | -46.26283 | 2024-11-18 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e075735-dabf-35b6-b02c-3993a913b827 | -6.31126 | -39.48925 | 2024-11-18 03:49:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| df0be0f8-86cf-3900-b27c-0253bc87a1b6 | -7.30355 | -35.18822 | 2024-11-18 03:49:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 281f2b7d-a2bd-35c1-aa77-b77e651e0af9 | -7.74551 | -37.78499 | 2024-11-18 03:49:00 | NPP-375D | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3688bd7-595f-3426-8bf8-62439123df94 | -7.09935 | -39.30365 | 2024-11-18 03:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 78de2125-4ec5-3a34-86a6-ab7a6d2bebed | -6.31192 | -39.4852 | 2024-11-18 03:49:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 461ad89c-52ce-3bd3-829f-0bac06fd5870 | -11.81702 | -47.07113 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d723dd7e-3362-3f10-892f-3f2a04146038 | -5.57168 | -46.42734 | 2024-11-18 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41180dbd-1ae5-3693-9c7f-27ef2c673bb1 | -5.75065 | -46.26654 | 2024-11-18 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55495256-f616-3970-be72-fe3c8af44f26 | -7.66768 | -39.29139 | 2024-11-18 03:49:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ebc6466-34fd-3faa-a763-8bfb29f02130 | -7.40216 | -42.76431 | 2024-11-18 03:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0e4066ac-6594-3ad1-a258-dca955021d0f | -6.84218 | -35.10339 | 2024-11-18 03:49:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9aec9890-91db-3bd0-9755-c89638c81689 | -5.24151 | -44.75018 | 2024-11-18 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f841011e-ed6e-31b5-af6d-a17d63cbd70b | -17.36596 | -52.00797 | 2024-11-18 03:49:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f47919f-52e7-3d57-a2da-bc7dacb2496e | -6.98678 | -39.65848 | 2024-11-18 03:49:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6e7c74bf-e505-32df-ab1b-20f2aaa53be2 | -7.68427 | -35.07148 | 2024-11-18 03:49:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b64910e2-71b2-3460-9744-da5c11dbea8e | -12.01805 | -43.00772 | 2024-11-18 03:49:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fe264764-7be2-3a91-8bb7-2959180bd81d | -11.83344 | -47.08836 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca4ba676-2e48-3726-9c69-4dbd6478920a | -11.85183 | -46.93737 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3f91bf9-62cf-386f-bf63-1b66224d722e | -5.57101 | -46.4312 | 2024-11-18 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5155a089-a881-35de-97a6-3531ea2b20d6 | -11.82292 | -47.06895 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cca074d-2e28-3bcf-b0aa-87e7e335d588 | -17.6066 | -57.551 | 2024-11-18 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 99395f5c-18e4-3de1-b6c9-a3518bc40fb5 | -1.2964 | -51.7616 | 2024-11-18 03:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 74f59ae2-4981-3fcb-b899-bd2c1984bbda | -17.6059 | -57.5921 | 2024-11-18 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 3dbb1256-df59-30f4-b727-e951f9374172 | -1.2964 | -51.7204 | 2024-11-18 03:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b6664aa7-5507-35b3-96ed-60bed707ec39 | -17.626 | -57.5692 | 2024-11-18 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.7 |
| 963b83cb-09ef-34e4-8f84-80e1a713612c | -2.5847 | -51.7181 | 2024-11-18 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2d502d10-7b33-3465-bf91-b9376437544f | -1.3148 | -51.7408 | 2024-11-18 03:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| a7208e46-bdc1-3d95-a61d-88dc8f3edfb9 | -17.6256 | -57.5897 | 2024-11-18 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 03e61a9b-c14e-3140-a055-6d25fa313bdd | -17.6063 | -57.5715 | 2024-11-18 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.7 |
| 8925da73-0d44-3e59-95a7-c98ebca4161a | -1.2964 | -51.741 | 2024-11-18 03:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 313ff8f4-305a-39f6-8729-88ea19a51b57 | -3.0542 | -54.4081 | 2024-11-18 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 02c85231-8ee4-38dd-b408-5d9938a09741 | -3.2932 | -45.6713 | 2024-11-18 03:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| ff26930c-cd1c-369b-8ed5-6c25537d42a5 | -22.53895 | -48.8139 | 2024-11-18 03:51:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64980d5f-2dd5-3bb0-bb34-130cdfd68d37 | -22.90167 | -43.75314 | 2024-11-18 03:51:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f653c3dd-50d6-3d84-8b53-09dd95ded4ad | -25.03823 | -50.05997 | 2024-11-18 03:51:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7dbb89a9-a6a1-37a1-b5fe-034dad8bbda6 | -19.8501 | -43.84698 | 2024-11-18 03:51:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8690f991-6aaf-3e8f-b05f-62775ad48c14 | -23.4066 | -46.55725 | 2024-11-18 03:51:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 782ba4c0-23cb-3e54-b4bf-8d083e1771e1 | -25.19197 | -49.33043 | 2024-11-18 03:51:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e2115a1d-cad9-3412-a4a0-0b298fc620e5 | -23.93439 | -54.14248 | 2024-11-18 03:51:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 31a8b1b3-615e-3899-9006-5a2555b430cb | -21.17975 | -43.97998 | 2024-11-18 03:51:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7395c2df-1d91-3a42-b109-ce67e9b6a915 | -22.67511 | -42.85625 | 2024-11-18 03:51:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6049ecab-9430-3d14-b7a6-889039d4d97a | -20.89933 | -43.81926 | 2024-11-18 03:51:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 33d63e4c-f1a2-3df3-8d93-a186a6727539 | -21.18048 | -43.98257 | 2024-11-18 03:51:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6720ac49-f1f0-3f45-a836-9d5e6eb9376d | -23.93423 | -54.14209 | 2024-11-18 03:51:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a23f6027-6b38-3213-854b-15b1e2c52f73 | -23.93566 | -54.13641 | 2024-11-18 03:51:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 61286761-729f-32ab-96fe-41d51a242fb1 | -23.9279 | -54.14019 | 2024-11-18 03:51:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c63028af-cde9-34fd-9610-7c3ecf0376d7 | -23.92934 | -54.1345 | 2024-11-18 03:51:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| db77984b-3d04-35e3-945a-f573d2c4b650 | -23.92806 | -54.14056 | 2024-11-18 03:51:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 69177704-0d8d-380c-a921-aecf5ece8732 | -27.66298 | -50.82675 | 2024-11-18 03:53:00 | NPP-375D | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| b48606b3-e953-38d9-b31c-01c8e41f5fdf | -27.57552 | -50.8411 | 2024-11-18 03:53:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c427381a-b7a0-3712-9ff9-d58f223e7462 | -2.8791 | -51.7932 | 2024-11-18 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| c84544f7-05ff-39aa-8107-b359c48730dc | -2.5847 | -51.7181 | 2024-11-18 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ea92221a-3b54-3b78-aeb2-3de2cea5cdf2 | -17.626 | -57.5692 | 2024-11-18 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.1 |
| 59d0ef4b-683e-3e1e-a85a-b40543d9da7c | -17.6256 | -57.5897 | 2024-11-18 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 632fa599-1fce-3311-aa61-19f67202fad8 | -1.2964 | -51.7204 | 2024-11-18 04:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 96206928-9e27-30e1-8274-fb648294d351 | -3.0542 | -54.4081 | 2024-11-18 04:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 097d49a3-e4c5-369c-a25c-c5d599240620 | -3.3452 | -50.4917 | 2024-11-18 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 5aa339c2-3934-319f-84ff-ddf86d82c6f7 | -17.6063 | -57.5715 | 2024-11-18 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 0f6541c7-b68b-303f-a3ad-5d0fdc97ce07 | -17.6059 | -57.5921 | 2024-11-18 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 6a140953-7e07-3e27-8a4b-68fa144816d1 | -1.2964 | -51.741 | 2024-11-18 04:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |
| eda30c52-e6cd-3b85-a36a-ccb1c9d9a515 | -2.8607 | -51.7937 | 2024-11-18 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 31ff22c9-4394-31a8-9833-2e4c4f3027a5 | -1.3148 | -51.7408 | 2024-11-18 04:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ce54e053-1c4d-366a-b31b-0022eb963409 | -1.2964 | -51.7616 | 2024-11-18 04:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 84d9d8c6-b6d5-3a5c-a280-10da5c06484b | -3.3452 | -50.4917 | 2024-11-18 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6f570058-d5e9-3aba-8c78-5315ad177771 | -2.5847 | -51.7181 | 2024-11-18 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 873e5109-033a-331e-a427-21636ed94d0a | -2.8791 | -51.7932 | 2024-11-18 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 2c800e25-3824-3582-aa24-3aecedeaf9c1 | -17.6063 | -57.5715 | 2024-11-18 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| fe1eb2b1-04fe-3a64-a27c-4faa062bdb06 | -17.6059 | -57.5921 | 2024-11-18 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 0eca355f-dfb5-3b6b-bd6a-1f13eb50f535 | -1.3148 | -51.7408 | 2024-11-18 04:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f4d7b2b2-6c1d-3032-98af-66546c7693b7 | -2.8607 | -51.7937 | 2024-11-18 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 00280f99-9140-3008-9084-ed89651c6be0 | -1.2964 | -51.7616 | 2024-11-18 04:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 989917a9-a6aa-34f5-8895-88f28037298b | -1.2964 | -51.7204 | 2024-11-18 04:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 162ae3fd-19e4-3bd1-b05f-1882fb54a421 | -17.626 | -57.5692 | 2024-11-18 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |


[Clique aqui para ver as próximas entradas](README18.md)
