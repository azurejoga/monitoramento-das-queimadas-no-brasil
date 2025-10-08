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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f7976f4-1ae2-33e8-9014-f4854856b988 | -14.45086 | -48.79054 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9049e308-ea49-3a73-9bb8-10d974671b58 | -8.89521 | -47.66232 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59e73afb-7a64-33e1-a154-1dcb3a571a6f | -19.44836 | -44.18639 | 2025-10-08 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8dc5bfd-3aaf-3d7b-9862-5d3189de8372 | -8.44843 | -44.71764 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21f6ebfa-2a8d-3eec-8769-9760cfd3863f | -15.37034 | -47.32469 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03eb53f1-4480-3bf8-9fc4-6c66e219db6f | -15.79856 | -46.24856 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3e261a6-a490-379b-8a45-f9d70e8663e1 | -14.92178 | -46.79977 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ca40986-d7bc-30a5-8086-4ad272f24f1b | -19.26729 | -44.11871 | 2025-10-08 04:19:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acfd685c-7fa8-3fcf-89f9-06290904a0b8 | -8.7829 | -48.00169 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4dea1cb9-959f-3011-8a4b-9553c4088938 | -17.97477 | -44.97856 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17c5e015-1320-36ab-9a30-0948ba3f0ac1 | -7.58365 | -47.20571 | 2025-10-08 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e995b647-9fa3-3d0c-bbdb-635081f99007 | -7.79606 | -44.20924 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 806b8ce1-8d79-3821-b58a-82f2b79f6448 | -15.38787 | -46.28025 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6cbc7d2-c2ff-3d56-bf2a-bacae4eb3e65 | -15.14586 | -45.81115 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e40fb65-5c3f-35ff-8cc9-6411308e33bc | -15.38848 | -46.27649 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d98360f6-4c17-3f1c-85dc-531d378710b5 | -14.95966 | -46.82507 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 062812e7-e7b9-3db7-9084-510dd10b03a5 | -19.13113 | -43.51917 | 2025-10-08 04:19:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2478d83d-17d6-36fa-a574-5b0c68161316 | -13.7431 | -45.75723 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a59bbae-c11e-3d8d-b7ce-35c7733546a9 | -15.2629 | -46.3418 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f2ce274-c7fa-3d3e-a7d3-1e0f9020ec6c | -14.7078 | -48.40192 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 287e009d-08a4-316c-b9dc-75e70d88bb3a | -18.0419 | -57.52888 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f714eb41-0fb5-3625-a9ce-e25f5bd9faaf | -14.44714 | -48.78987 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5984c94f-7346-3d24-a087-8f9a6b77d9bd | -19.38827 | -44.38611 | 2025-10-08 04:19:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c60cb503-2576-3e79-8337-67cab2a2058b | -17.56042 | -46.06738 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4db693d2-7c20-3f9d-886f-48b10fd498f3 | -17.38107 | -45.05783 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee047be8-26ef-34e5-9f3e-bc560fb8db12 | -7.7905 | -44.20115 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b7034d1-e5a1-351a-bc9b-e183222fc679 | -12.17858 | -57.23739 | 2025-10-08 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2346d307-8736-38f8-a6ce-5df16715b879 | -8.61694 | -45.09925 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9186facb-6ead-35c8-9536-5ec864fd5b36 | -20.20741 | -43.95204 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 640825ac-8a46-3803-95f8-881f61807efb | -14.95437 | -46.83586 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e557ce8-bdc5-356d-9e6f-68c88988214b | -14.39047 | -46.02928 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3949fcf5-d37d-38ec-bc5d-fee851cf0b62 | -17.29692 | -58.07067 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 39d5bfac-0482-3fbe-a06d-054dc6401483 | -8.64128 | -47.16894 | 2025-10-08 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e2e97c5-e1c7-3a75-8fd5-6ff58fc5d8c9 | -8.15832 | -50.16299 | 2025-10-08 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e43cb0bc-2447-3994-96ff-87d34aa72859 | -18.35043 | -42.39114 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f5a0153b-3a26-3db4-9eae-e0691e6d5296 | -14.71161 | -46.0608 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 623d330c-7152-39fb-8e50-ef34b19f1bf1 | -17.94635 | -57.53102 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 17dab285-9986-3a8a-b5b1-9e5432030c05 | -18.04955 | -44.46464 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3a16646-46ef-3cb4-9b10-144691b89ede | -17.27409 | -42.64884 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b77c9358-1222-3f97-b697-5a22eb174248 | -7.62632 | -46.55727 | 2025-10-08 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abe885e5-f84a-3ed3-ba8e-cc46a9da4748 | -17.55592 | -46.07409 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d86b7295-249f-30b1-840b-f0b9c3bd8408 | -18.51588 | -43.90017 | 2025-10-08 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dda66c9-1c4e-3795-af4e-bdaf351b06e3 | -8.75253 | -44.23631 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f7210f6-5260-37a3-a885-a172a0fa3926 | -14.38216 | -46.01665 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b24b9dab-0a44-352e-a8c4-01a3bf18efe3 | -9.42253 | -47.65281 | 2025-10-08 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d0b6c44-d149-35d9-b66a-46eb8f77ab70 | -15.86236 | -44.8316 | 2025-10-08 04:19:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08bda21c-2ed3-391b-8382-9a0af45b768f | -19.8487 | -46.16335 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6d67ed5-8d12-33e3-a113-861832505aba | -17.15494 | -43.43758 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f0efd39-365b-35e4-98f5-4ca58ce69128 | -8.92156 | -46.58466 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f322fbe-9a41-3128-bfd4-2f243bbbb522 | -8.56557 | -46.228 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d470251-18d3-3a65-b1e4-dbeaf564482c | -14.70455 | -46.01142 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a6a726f-f1bd-36bd-85f6-58671670b9df | -9.39591 | -45.93836 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec7e497c-6b39-3a65-9055-ce4a9a40518e | -18.04142 | -46.4454 | 2025-10-08 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 176f56ae-072c-3bb4-ab16-5296ea8213db | -7.42812 | -46.62688 | 2025-10-08 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a472493d-5b6f-32c1-8e9d-f6066ce72a10 | -20.39291 | -43.0676 | 2025-10-08 04:19:00 | NPP-375D | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2345efb0-9c8e-32e6-829d-bfcd89f4ea10 | -17.8335 | -57.63827 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ce27a820-9a64-3f02-a7fc-315752c901d7 | -17.28296 | -42.64863 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f2c6a91d-b802-3d85-8881-c24699b2dad8 | -15.37076 | -47.30063 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 29e216f7-4673-327e-b0bd-6a8e1fcb9778 | -15.93974 | -42.60589 | 2025-10-08 04:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b5c6b436-eed6-3526-85dc-25e0f468e5d6 | -15.75652 | -48.73793 | 2025-10-08 04:19:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c075f46-8475-3f2f-80bc-dc576ce664ee | -20.16747 | -42.21112 | 2025-10-08 04:19:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d8e7162-9693-3292-8f38-a8a93da055b8 | -13.75708 | -45.7559 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e652081d-6391-364b-86ab-d0b787a56d19 | -16.58792 | -46.55302 | 2025-10-08 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5734cfd-37da-394b-bd01-8c608eb10c97 | -17.45696 | -43.3926 | 2025-10-08 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7efb8098-989a-3897-a28e-10855bf8479d | -13.72564 | -45.69501 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a951d655-8100-330f-8822-5635b8baf8b4 | -18.19373 | -43.0491 | 2025-10-08 04:19:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3fccf38c-550d-3b82-b020-1d8a783ad343 | -13.7961 | -45.80308 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6ca01cb-93f8-358f-b129-fb1abfe1f086 | -18.40228 | -45.21102 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 637f2a5d-1000-3f66-9281-1d7effb6a758 | -18.6578 | -43.91016 | 2025-10-08 04:19:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7053774-02cb-3641-b253-f6589ba4482b | -18.5113 | -43.93166 | 2025-10-08 04:19:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f32b8379-035f-3e05-8e24-16b169cc2ec6 | -18.00436 | -44.98732 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f0e72b7-2303-3163-90a0-b7f77bd7ccac | -19.82815 | -46.1635 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f129e72b-86a4-37bb-9397-b16fa8d14730 | -19.51053 | -44.07515 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f036cfc7-478e-3508-a4a9-27b58bd2a7e2 | -20.49833 | -46.9921 | 2025-10-08 04:19:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dabdd8f1-c312-360a-b5b0-700e2a0ef1b6 | -13.80792 | -45.79393 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d3ca590e-cf03-32ac-b6cd-30b5ae18f778 | -15.95097 | -42.60346 | 2025-10-08 04:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 357ef469-3987-3e28-a368-9ad161d322c4 | -18.29418 | -46.49718 | 2025-10-08 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5589f8ae-eac3-3d27-9cf8-e9a0c64cb9a2 | -18.01523 | -57.56385 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7687aa83-8676-35b9-97fb-5cf53b065d66 | -7.24537 | -48.47451 | 2025-10-08 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0c8d103f-d25c-3ab9-8843-5e0e8181227a | -16.11435 | -48.06114 | 2025-10-08 04:19:00 | NPP-375D | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38dac0ac-d1b4-3a4b-bc65-82563249107a | -13.73001 | -45.71054 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87ce2cc6-6d53-3f9d-9696-8d1eca5ce2c9 | -19.57821 | -44.65315 | 2025-10-08 04:19:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be462440-6b18-3023-9aff-379c9320e080 | -17.9324 | -57.50813 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ac9da64f-483f-3d63-8b40-14b89e422341 | -19.34037 | -43.08408 | 2025-10-08 04:19:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a4fd6d16-48bc-33cf-b89f-4b1123f00829 | -14.7079 | -46.012 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cf9c380-bffa-3793-b58f-5c2e755b0f71 | -19.97193 | -43.21184 | 2025-10-08 04:19:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d5ae5c01-fb7e-3e7a-98ae-006d178abe13 | -18.00592 | -45.04403 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05a37ae7-2bf6-3f37-866f-54a4979d8656 | -7.80771 | -44.2436 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a40406af-8dfe-36c3-928d-8d0705fd6b28 | -17.14104 | -43.45955 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da8f0c06-5b46-319e-a2f1-4e5018fccfb2 | -20.22202 | -43.80175 | 2025-10-08 04:19:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4be54ca1-d89c-3284-949d-a20099094910 | -17.28484 | -42.65067 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| deb453a9-27c9-31c9-a73e-6489efc73ad7 | -13.30621 | -48.02862 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5d462e57-fa7b-3bc7-a45a-f3b535a0640e | -16.32936 | -47.05978 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e747b823-8619-36cb-9bec-89bc7fcef87d | -17.26327 | -58.12188 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a355c876-8af9-305a-8eab-7121333e5801 | -13.78764 | -45.81274 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc4fa9d3-c22b-336e-a6ea-25275ef94ac9 | -17.55 | -46.76072 | 2025-10-08 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c778fee-10ca-38e4-a6a8-ab2398aff32d | -19.85261 | -46.16026 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41a40b7d-b617-37de-95f2-5ff669028774 | -15.03616 | -49.44571 | 2025-10-08 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| feb80088-0305-3f7c-9ec9-744d01da3364 | -13.80516 | -45.78975 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96e4d9f3-e1b2-39ef-8f95-3cde29273607 | -13.72841 | -45.69918 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README58.md)
