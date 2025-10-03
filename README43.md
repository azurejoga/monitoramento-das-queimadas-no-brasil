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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7039ec21-f2b2-33d9-9aea-6b0f7b057c4b | -12.6319 | -46.9923 | 2025-10-03 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 371cff9b-5c42-3641-8d78-7eccbc4ef6de | -13.7764 | -47.5617 | 2025-10-03 04:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 59f9e839-6719-379a-9737-1eeca7cf7854 | -14.2131 | -46.0596 | 2025-10-03 04:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 32fd04ed-90bc-3dee-910f-581b7d776188 | -10.936 | -46.7293 | 2025-10-03 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 7fa62d25-2c1e-3363-86fe-22eae764114a | -12.6127 | -46.9951 | 2025-10-03 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| fbef023e-020e-31bb-9bb5-10ccf2b73897 | -6.0418 | -44.6076 | 2025-10-03 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 3d3509f0-9a2a-3048-b2f8-07a8b9812757 | -6.36053 | -44.75725 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0470cd2-2b7d-38d9-b9e3-9e1c66402285 | -4.89468 | -45.72704 | 2025-10-03 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5852c332-40b6-34b2-bc42-0e08f2576e68 | -7.15811 | -44.99085 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 655f7038-0b65-3bac-bfe2-da8727750c81 | -6.23684 | -44.23489 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68cf25b3-afe9-3009-9eac-12bc3a49c0db | -6.68909 | -42.84163 | 2025-10-03 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 19ecfd46-0fb0-3649-9a4e-60d7265d527d | -7.24892 | -49.41343 | 2025-10-03 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ffd1cd4-8f2e-3550-867c-56f738fdbe27 | -6.29248 | -44.42104 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04b6d56a-a761-352e-88a0-c977946e3434 | -7.74984 | -42.57157 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbc7e7f5-51de-304b-89b1-142cc72b0650 | -6.37436 | -43.8775 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70cada75-e225-3942-ba45-abf43843b9ed | -7.52081 | -38.00702 | 2025-10-03 04:10:00 | NPP-375D | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4d9d912e-380e-31de-b6c1-29cfb9f00af2 | -6.19458 | -44.63034 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24878af2-b7a1-37e0-bbde-f66087ff29fd | -7.745 | -42.58819 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2380956f-323b-3ff6-986f-067ab671a8d4 | -2.24858 | -47.87974 | 2025-10-03 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 79188d8f-2190-3f1d-9563-35d4e8915aac | -6.87987 | -39.2793 | 2025-10-03 04:10:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d3aec43-6529-3670-ba40-32146809516d | -7.56543 | -42.62843 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bcc2c10d-bc4b-3205-b995-a9d96cfa5097 | -7.79722 | -42.53231 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ed2c7e7c-3fd3-3e14-904f-4054d7cf2f23 | -6.22829 | -45.34842 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df976c68-d9c5-30dd-842a-dcfca4bec754 | -6.26158 | -43.88421 | 2025-10-03 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 31f018ba-ad8c-316a-87fe-98391e13067f | -6.37311 | -43.88516 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfc9a003-c0dc-3755-9f1f-4efd0e0f305d | -4.63967 | -42.53287 | 2025-10-03 04:10:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93667f50-3854-302e-b71b-5a246bc7b0e8 | -6.84924 | -44.7809 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35ef2ca0-f0e6-3f86-ab8d-a3d8cf3f0522 | -4.66292 | -45.79666 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 227eb3e3-e38c-3d83-93ca-1b22d9d81576 | -4.66438 | -45.81232 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe2802fd-1495-3514-8b3f-c3bcc5237f78 | -7.78891 | -42.49861 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 25752d1d-d781-375f-9c32-1ffb4039f556 | -6.5737 | -42.12155 | 2025-10-03 04:10:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ac47e12a-97d6-33af-b352-78e6109837ef | -6.34381 | -44.30874 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8984cb08-c020-3c7f-a36b-45d23b1097aa | -7.01396 | -42.31357 | 2025-10-03 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77d1914c-6edf-3143-8aa2-a069b65af466 | -7.76459 | -46.26479 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ad94cc84-02b2-32be-af89-312cc3efed8f | -7.34466 | -44.36988 | 2025-10-03 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca5961a3-5749-34be-8160-ab9143b6aa70 | -7.27172 | -45.48986 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51c72b24-d4e4-3aed-a2c5-22071c29ff98 | -3.09456 | -47.00988 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b5c985fb-a790-39c6-8ce9-bf22f7c4ad03 | -7.74871 | -42.57861 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f0c933f4-15d1-340b-8472-54779ad63136 | -6.6807 | -42.82925 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 834922b3-e5c1-332a-9c03-22c626e0c65c | -7.50417 | -48.85426 | 2025-10-03 04:10:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9bc94b90-4940-309c-8584-86b74e6790ce | -7.90785 | -43.53783 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2bc8737-fd3f-38fe-a575-13c1848ffad2 | -6.53047 | -43.37236 | 2025-10-03 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80a15a7e-061b-37c7-bf45-3fb6bd211771 | -7.00953 | -44.49387 | 2025-10-03 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7f67f71-dc28-3b15-a248-c0c21742cded | -7.7648 | -42.6065 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6c0138d9-0d57-301b-a985-48fd983870a4 | -6.84963 | -44.77984 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ae74df0-3206-3297-beb2-2f2f5cb68efe | -6.36594 | -42.89414 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1d85410e-9af8-3541-bfed-cdf4b5f5922c | -6.87637 | -39.27876 | 2025-10-03 04:10:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d310029-a1ec-3ab3-9da5-daec01e660c2 | -7.71063 | -46.20634 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e15e9cc0-b1b5-363e-8f8c-657be528ec7d | -6.19096 | -44.62974 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b91a4ee-9575-3f74-91bd-66d8f1caa709 | -4.64704 | -45.79462 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e4c5940-af00-39aa-8f2e-e0e1865ca1a6 | -7.29942 | -45.26821 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b42f9f36-1a7a-3670-bfef-c9bcf87ba43a | -6.22293 | -44.25314 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 734c1d1f-e87e-34fa-86c6-436f54b0b8e7 | -7.75704 | -42.59077 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 470890e9-41a0-369b-ab39-6e2b054b4c01 | -5.43321 | -42.63621 | 2025-10-03 04:10:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2d0fd9ca-7e46-3074-aab1-e0c62130d29d | -5.33435 | -43.52794 | 2025-10-03 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c70faa57-650f-3093-a541-cb46cc7c01e9 | -1.08794 | -53.68039 | 2025-10-03 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| beb19eee-6f0d-36b4-ac0e-0f448887aec5 | -7.77153 | -42.58588 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93fc541d-efd9-3e51-a35b-5132b15f53f2 | -7.75647 | -42.5943 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ef32f599-a198-3207-a1d3-dff3fda5045b | -7.76211 | -46.27968 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 25a26fd9-2fcd-3d29-8393-f97b0e9c695b | -6.34687 | -43.40454 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3928ec95-3295-391a-a8c0-97113169f98e | -8.07787 | -48.22162 | 2025-10-03 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17b40e43-f62a-3b18-a257-4e30c8b7440e | -4.43138 | -40.76255 | 2025-10-03 04:10:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e68f2d45-55bb-39d5-aac7-cb80c97cd3fd | -7.25548 | -49.41287 | 2025-10-03 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa0b8c06-58ec-3067-9d9f-fb3d785df475 | -7.90163 | -43.53303 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6876434-16e7-3d03-a0f9-3b1de6aea7aa | -7.74604 | -46.25634 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e123acd9-3346-3b7e-95cd-f29f54f30e8d | -7.77934 | -42.57991 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f939978d-8dc7-3d4f-b917-095d36515567 | -6.29607 | -44.42158 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1a0b6d5-ae96-3d97-9409-c919ad1590fa | -7.48121 | -43.0452 | 2025-10-03 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1718cbd4-4e9b-3830-83ff-c9d0c474ee7c | -6.11158 | -43.43232 | 2025-10-03 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43422f06-9856-3990-84ad-363b0914b1e9 | -4.67954 | -45.79424 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52aeb9d7-dcbd-35ae-8c75-afdc17a8f9b4 | -7.79666 | -42.53583 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 99c2aefe-548c-3086-bc9f-eb4eeb39f84a | -3.22285 | -47.1288 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 118265bc-3719-3851-9f12-f33ef32f7065 | -6.23654 | -45.34526 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f97fe5f-90fb-34ce-ae1f-3c901883a04a | -5.78335 | -45.75151 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a946fa3-0747-339a-8ed5-11255b6c4f7d | -6.27481 | -44.04599 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1e09a01-6d6a-3d3a-bdd3-ee936d2bb1e9 | -6.64797 | -43.5936 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c8ea887-2423-321f-b48d-db12671474d6 | -6.27066 | -44.04934 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 202b7b0b-e281-370d-bb6a-4f80b937e6fe | -7.79108 | -42.54934 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0b19913e-e4ac-3878-9cec-89ff4cd8db69 | -7.76296 | -46.27456 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b688c50e-b33f-3e3d-ad04-d63009b814b4 | -7.76819 | -42.58534 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 20c3e56d-e967-3e6e-8c1c-0d53a5fecbe3 | -6.67116 | -42.82409 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 33e002de-606d-35ce-afb3-e8bd7b0197f3 | -7.56524 | -42.39408 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4e3b8ed-87da-3618-b1fb-af8d06ac7941 | -7.00062 | -42.31142 | 2025-10-03 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b380bd86-f92b-3499-92b7-eff9fe2b8741 | -4.66835 | -45.81287 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3813522-6842-3870-96c3-69ac4b2d7763 | -4.65262 | -47.55051 | 2025-10-03 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d77f3203-a1de-363e-bacf-82fcefcbb260 | -6.73012 | -44.61814 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82c7861e-8051-33f2-9965-a6af8ec4e098 | -7.12553 | -45.05095 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cea85d0-fc00-37b5-bd2a-dba890caa878 | -5.94362 | -43.30666 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9508103c-cb7f-36ed-875a-d65a497b5160 | -8.66063 | -39.43095 | 2025-10-03 04:10:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a91cd367-d990-3e4d-8f9e-9d330b2be0df | -4.66057 | -45.7864 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18ec0db2-911f-3158-9674-3059d7de2fcb | -7.74296 | -46.25087 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4f5faed-5c65-3180-b745-9b2d231b3602 | -6.97298 | -44.38957 | 2025-10-03 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0a323f1-b71f-3540-986f-1e1c7f8cbb29 | -1.07312 | -53.68336 | 2025-10-03 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 413dcd97-c3cb-38b6-904a-d681572fe553 | -4.64539 | -45.8045 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3bc912-6e81-3236-8b45-20eac1ad8d43 | -8.17953 | -47.01535 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b422a27-d6cf-34f7-babc-dd2a1fe267a2 | -6.17874 | -44.86662 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7592428-2bf5-338a-b530-9df0cc42a233 | -7.30539 | -45.2683 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81f0b1ac-9d59-3809-aa9d-8517fafc1831 | -6.74046 | -44.57729 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de11e55c-9948-38eb-acd5-23d05fe8a95d | -5.6158 | -51.93654 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38326802-5864-3894-a7cb-a7f65dacbb70 | -7.80209 | -49.87029 | 2025-10-03 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README44.md)
