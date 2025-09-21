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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b30ec4e-e8e2-3413-9777-d92c53499605 | -14.4466 | -46.5139 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6a9ba17-c34f-3fda-9fce-479c094eb21f | -15.7717 | -59.43695 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46009b02-f94c-3ff0-857b-5150af9e0f44 | -16.59919 | -45.09833 | 2025-09-21 04:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb0cd4c4-2341-3b5c-8a37-81ec87b1106a | -15.93772 | -59.42513 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d9915a3-b592-3ca2-aa9b-ef91b5a8e123 | -15.9365 | -59.43111 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6b1e3ab-985b-3db8-b32c-f2f0fae9f097 | -15.96405 | -59.43075 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98460980-2751-3330-89bd-66cf1613f598 | -14.97646 | -44.42826 | 2025-09-21 04:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98d1f15a-8534-3533-9463-5f888d44588f | -15.68973 | -46.98861 | 2025-09-21 04:38:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53d70802-3ff1-3835-b770-fd7927e35f72 | -15.97235 | -59.41669 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 39f53c2c-38d4-361e-bdad-13cbf0a33309 | -17.63856 | -44.18925 | 2025-09-21 04:38:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19df1ebe-6400-3d15-9109-a759d30f2050 | -15.95806 | -59.4332 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71d30937-28cb-3a3f-adde-b0ab5c52c953 | -14.81237 | -51.38346 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3baec5c3-a1cc-31a0-b460-c7a860ce92f6 | -13.62421 | -47.41678 | 2025-09-21 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a0ae7c9-193f-3b58-8e67-0fffd02363ec | -15.96338 | -59.43407 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01d46856-c89a-3d9e-875c-69711d0bf9b0 | -12.47703 | -46.6937 | 2025-09-21 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2efd2d0-9319-357d-9015-4318b374b3a5 | -18.73848 | -53.28785 | 2025-09-21 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 20a4a945-1bcc-32ae-98ab-7c5c7bfb4611 | -12.41899 | -45.11578 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa6b50d4-0154-3213-bb57-e217a9c4766e | -14.97335 | -44.42008 | 2025-09-21 04:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a103e22b-eb26-370f-8767-4705c970f452 | -18.46411 | -47.23911 | 2025-09-21 04:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90ab72e3-2f8d-3e15-8ea9-b5bfc26eb937 | -19.07722 | -49.00104 | 2025-09-21 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 241f231d-306a-3073-b515-bf510ce49506 | -15.96473 | -59.42737 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6a3060a-6f6b-3d29-bf7a-c47e95909952 | -14.80216 | -51.38168 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6435539e-d932-3e3b-9209-63f3387ce208 | -14.47023 | -46.50422 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1bd11c8-d5b7-3df0-9818-c7b45a1adf01 | -12.96735 | -46.95253 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d25c2f3-cc16-335b-97ce-6f6b5c834de4 | -20.27105 | -42.70522 | 2025-09-21 04:38:00 | NPP-375D | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7fcafb6-79e2-3a3f-962e-d464b7c294a0 | -14.45208 | -46.50146 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 800d6908-84fc-3607-9020-237a33ec2f69 | -16.87315 | -43.90422 | 2025-09-21 04:38:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 800ee184-d37f-35b6-a71c-5c958e52b331 | -12.42526 | -45.12652 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3262aff-710c-3fde-b268-fa4d128dc9cd | -15.48377 | -41.91929 | 2025-09-21 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f3efc81b-c52d-3af9-a1a4-4cb76b7e8be3 | -18.23812 | -43.79753 | 2025-09-21 04:38:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93842747-924b-3301-84ad-b90321e19507 | -15.92336 | -59.44165 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 618a9545-1f2e-352d-bfc0-ccac6a25d33e | -13.5363 | -42.99706 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 2e683c4d-9a94-3790-a858-55beb766e291 | -15.29071 | -59.418 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da73b75f-419d-33bd-922f-4bbc6f85980d | -18.77164 | -53.34806 | 2025-09-21 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 783e2ab8-fbb6-3df7-b0da-2aca0046d4c4 | -13.25302 | -44.11132 | 2025-09-21 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e979fb85-39cf-31e4-b86a-cc40aada7aaf | -14.97234 | -44.42768 | 2025-09-21 04:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f19cccfa-1b72-34f2-bb7c-ba62e4906a56 | -15.89442 | -59.40153 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c119e6fd-8fd9-3faa-8546-e20ec34d9c15 | -15.92926 | -59.43969 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab3f714f-6f1a-342f-b648-62e787dd390f | -14.79876 | -51.38108 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df629da1-b5ed-3b86-af4b-0e998c9aeab7 | -13.36224 | -44.2811 | 2025-09-21 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cde2dc2-e036-391a-9ff4-ab7472bcfabb | -14.31919 | -47.79873 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 093c6623-48c4-3c1a-8934-6ab28438db76 | -11.62638 | -50.58855 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 433fe990-5dd5-3fc9-8f01-00ba8a548f2e | -17.44442 | -44.03317 | 2025-09-21 04:38:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c00d4cb9-be7b-3fb3-a1d1-2eb4d410f84d | -18.36455 | -43.70568 | 2025-09-21 04:38:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 716222ec-5a1d-3df8-959d-7dea6aa857d5 | -14.15345 | -44.07428 | 2025-09-21 04:38:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 156dcd32-428b-33a0-af8c-71125b093053 | -15.41888 | -58.7782 | 2025-09-21 04:38:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab442b4a-ea22-37ba-9001-fca3dd7795cf | -14.43542 | -47.57704 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5dfd85ee-fdd6-3031-abb9-f01ef838b177 | -15.9299 | -59.43655 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e84008da-e83d-3bef-b063-e2adb857ee22 | -14.60998 | -49.7618 | 2025-09-21 04:38:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cced49a2-56fb-3c13-99d9-e4b5cd6ce167 | -15.92272 | -59.44482 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dfa1702-da60-3c8a-a51d-e8c9fb7d2aba | -14.60942 | -49.76538 | 2025-09-21 04:38:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da72b747-5b34-3911-8088-c918757e67b1 | -12.48409 | -46.69477 | 2025-09-21 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59d9fd9f-3fb8-3f0e-b9be-78170141c3fc | -13.79243 | -44.33424 | 2025-09-21 04:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdd0efd5-37e2-34c2-8315-dfcb5db7a2ef | -15.95212 | -59.43541 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afdf1680-5dfd-3803-a00a-1a1caf8cac66 | -15.97698 | -59.42097 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 201523e9-cf13-3eca-a78b-f1eb87f45eb6 | -14.31575 | -47.79819 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52b36371-60c6-3bc2-862e-f8f02d31b50e | -18.4635 | -47.24348 | 2025-09-21 04:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 525fdd68-7aaf-352e-8616-84054b079625 | -16.28532 | -47.08784 | 2025-09-21 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd0674a0-44b0-3632-85e2-e6a79179eaf1 | -13.68188 | -43.81524 | 2025-09-21 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3ef7a72e-5c1a-3493-b29e-da0d74c45143 | -15.82299 | -59.51059 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bcfd3ba8-00f5-3202-a25c-f515c7c553c8 | -15.97305 | -59.41321 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e73e76e1-8d9e-3ece-9fb7-478593d1d0df | -13.53574 | -43.00138 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 49af3c5c-df94-374d-a70b-10bbcf4ea12e | -13.25696 | -47.2815 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c307951a-2a75-3467-b84c-f56f86cfbe71 | -15.8184 | -59.50591 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4958c6e3-33be-3682-a149-1c870bf18908 | -15.77461 | -59.43482 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc656309-5ce0-38e0-96ed-5b83038ca092 | -14.78763 | -51.36374 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87eebb98-d4af-338c-8940-ed777275fe0a | -14.79196 | -51.3799 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edd5f67a-6152-364e-a552-193d402c8fce | -13.53906 | -43.01068 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 37.4 |
| 095332f0-973c-30d8-a95b-c62b1a889f53 | -13.25291 | -47.28485 | 2025-09-21 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65511505-521e-3b21-a86e-573cff329c99 | -14.97747 | -44.42068 | 2025-09-21 04:38:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e254dfc0-d620-3dac-808a-4907dfea2712 | -11.62518 | -50.59593 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8401c000-06b5-3a78-95d5-51b7cffc30e8 | -14.44658 | -49.05984 | 2025-09-21 04:38:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa5041f6-56b2-30f7-b6a2-14c441cadf44 | -14.45389 | -46.51474 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3483d357-aa93-394b-b871-07aabe9a390d | -17.63916 | -44.18462 | 2025-09-21 04:38:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44c4b968-b2c4-3d16-a9b5-4418be637e49 | -18.76813 | -53.34737 | 2025-09-21 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 364fb8fb-177b-3979-8038-0db0bde85aba | -15.93461 | -59.44041 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cf6832f-a783-359b-9c5c-df5ab2c7c205 | -12.48056 | -46.69424 | 2025-09-21 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b574bda1-f695-3e40-a06f-3b96cb741487 | -12.43557 | -45.10901 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 488146f4-310a-32f7-a9a7-32fd3b24004d | -17.63918 | -44.188 | 2025-09-21 04:38:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15d981df-2a5a-3fd5-8990-04fd6bde5911 | -13.64664 | -45.69741 | 2025-09-21 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05387017-757e-355f-bdfb-f7f5032f92ac | -14.46236 | -46.50737 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 336b2a5a-e612-3413-860f-355cf8faeba2 | -15.94296 | -59.42636 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f065a74-1a6f-3361-9f66-e1c7fd949c09 | -17.63975 | -44.18333 | 2025-09-21 04:38:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbe04561-b2dc-35f5-b1a5-4513417ecc0e | -15.53184 | -42.17421 | 2025-09-21 04:38:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad99942d-fb91-3926-875b-11a5b80abaf1 | -17.16733 | -46.83399 | 2025-09-21 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b58bbcc2-a9be-31e7-a631-9fdc830ff600 | -15.93589 | -59.43413 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cd6e01a-1a0d-3ffa-bbd6-e07b1c6693c2 | -14.62768 | -48.26945 | 2025-09-21 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d00ffd8a-b3cb-3fa7-93e3-da429cafb2a2 | -15.96771 | -59.41249 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| abb1ace3-6531-3ffe-bbe0-ae02e72fca22 | -11.58817 | -50.28888 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f2fd01d-5620-39f1-ab91-c4f70c4adcba | -14.78918 | -51.37556 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0320811-9131-3078-bdb8-6a7bab1e2f28 | -12.4322 | -45.13248 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 159c48fe-79e9-36c0-95ee-eb3d2915af7b | -14.61331 | -49.76236 | 2025-09-21 04:38:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5889705-0b68-3e72-88d5-5f2d62f6eea7 | -17.70517 | -44.0849 | 2025-09-21 04:38:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d031cb9-1a73-3a30-9eb2-283b9034e2de | -14.4666 | -46.50368 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37d157fe-25ea-3bed-9e36-6b969c10b5c6 | -14.80896 | -51.38287 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e85f3b69-8275-33fa-8f60-2e82bdf1fb37 | -14.78856 | -51.3793 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54ff03c4-8d65-36b7-8326-ea1c5a2f7ad6 | -15.90778 | -43.04712 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af18d2c9-95c7-3fbf-afdf-0388e3e23d1f | -12.49643 | -46.68441 | 2025-09-21 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e094a3b5-e7ba-34ae-bca6-0c0771946faf | -11.62739 | -50.60389 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a1e5fa70-f943-3a2d-9784-3ae7c25419c6 | -15.93118 | -59.43027 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README31.md)
