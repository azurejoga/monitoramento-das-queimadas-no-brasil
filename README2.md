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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcfa7b6f-8db6-3879-aa9d-9f363abae5c8 | -10.4912 | -44.9422 | 2025-12-27 00:08:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ddc981cd-8162-36d3-b80e-b9926b289661 | -3.6024 | -49.356899 | 2025-12-27 00:08:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccee625e-3e0e-3072-91a1-50bd24e1207e | -1.1242 | -47.744598 | 2025-12-27 00:08:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf98d0e-e98d-375e-8bab-7a4cf5ab95fa | -12.5146 | -43.704498 | 2025-12-27 00:08:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fbedda9-d94e-3c50-93ef-e7901abf49c1 | -3.5999 | -49.437302 | 2025-12-27 00:08:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa7598f-52b9-3195-a662-ffa2cf1c09c3 | -3.0013 | -40.357399 | 2025-12-27 00:08:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e9206c38-0b67-3f82-8127-15557eab224b | -3.7558 | -49.717201 | 2025-12-27 00:08:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ae42bf-6a64-34c9-b826-cb2b4e29e5b6 | -2.4612 | -47.778599 | 2025-12-27 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d302f4f5-3b0f-39bf-9b35-b2f25c96b267 | -3.2028 | -50.2337 | 2025-12-27 00:08:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 032ab7ac-a4cb-38f2-8dd4-4ca2b3fda2c8 | -2.3781 | -51.9193 | 2025-12-27 00:08:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab5229ea-3c7e-3791-8806-38cee8772e12 | -3.7475 | -49.726398 | 2025-12-27 00:08:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7379843-4c37-3e43-a706-49283f9dafcb | -11.908 | -44.156399 | 2025-12-27 00:08:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d984fe7-5d6f-3544-921e-339552a484c3 | -19.231899 | -43.054901 | 2025-12-27 00:08:00 | METOP-B | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38986298-ed38-3adb-98d0-18c91103728b | -12.6696 | -46.770401 | 2025-12-27 00:08:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 008868a2-3f66-333d-a242-923874ee230f | -3.7491 | -49.733501 | 2025-12-27 00:08:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf87ea8d-40df-3785-b640-3db1eb476695 | -20.9694 | -48.634 | 2025-12-27 00:10:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| c8f7142f-8aa2-31dc-a985-aa05c708b36e | -3.0029 | -40.3307 | 2025-12-27 00:10:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 83e33234-a14e-32de-ac98-d9cf70f47be9 | -10.2376 | -36.3398 | 2025-12-27 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| f9624f2b-8c57-3406-b6f1-974f83957cec | -10.4889 | -44.9235 | 2025-12-27 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| de409162-af7d-3a17-8bd9-b7ec9d77b1fb | 1.8317 | -60.8765 | 2025-12-27 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| cd489505-fb96-3c32-88db-2318bae8a611 | -10.4889 | -44.9235 | 2025-12-27 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7f571a00-3ce6-3da6-a120-ba8f77357bc0 | 1.8317 | -60.8765 | 2025-12-27 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 0cfb0de6-bf75-331b-8883-f27f4325c006 | 1.8317 | -60.8765 | 2025-12-27 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 85c86113-6828-33b0-bb97-7a42246ba9c3 | -10.4889 | -44.9235 | 2025-12-27 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 362598c6-ef50-3666-aa0b-da10e9e8547e | 1.8317 | -60.8765 | 2025-12-27 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.1 |
| d3131897-68ba-352c-91c8-d35f20da4eea | -20.99079 | -49.39671 | 2025-12-27 00:47:00 | TERRA_M-M | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b77f9f1e-8ec3-3d41-b222-b06b9e3a3d4c | -21.72001 | -47.10593 | 2025-12-27 00:47:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e45da5cc-6f51-3c2b-92c5-119c5ea36ad9 | -20.9696 | -48.62769 | 2025-12-27 00:47:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| b4eed753-3692-34b4-9bb3-bafc7a9233ab | -19.55623 | -49.41515 | 2025-12-27 00:47:00 | TERRA_M-M | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7b8b21ba-35c2-3303-9cb0-21858556ea14 | -20.97172 | -48.64066 | 2025-12-27 00:47:00 | TERRA_M-M | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| b34a991e-5539-3026-8273-4d5326a0421d | -24.10321 | -48.77301 | 2025-12-27 00:47:00 | TERRA_M-M | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| da6b00fd-6dbf-3415-b337-6b10ff1866da | -20.98895 | -49.38511 | 2025-12-27 00:47:00 | TERRA_M-M | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 0fd66d55-8446-37de-b24f-439778916729 | -24.10699 | -48.77837 | 2025-12-27 00:47:00 | TERRA_M-M | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 648400d3-e43e-307f-baf5-0e5dc0d43f4d | -19.19435 | -48.15629 | 2025-12-27 00:47:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 51a27836-2bde-35de-b4f1-d420b3102ab8 | -19.55433 | -49.40308 | 2025-12-27 00:47:00 | TERRA_M-M | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5e780791-db2b-38a3-a7d8-c7efe9a05657 | -18.90599 | -46.59563 | 2025-12-27 00:47:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4fab9a89-03e7-3988-9c70-b0a5c494ee68 | -10.7706 | -45.0229 | 2025-12-27 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f7289c3-edff-3220-a2b5-e63f83d6f21b | -12.6681 | -46.787498 | 2025-12-27 00:48:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd90ed5-7462-3644-85f5-08ea9d4b09a7 | -20.9729 | -48.640301 | 2025-12-27 00:48:00 | METOP-C | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 96c0422e-fe72-36b9-84e3-c490888d64dc | -3.7598 | -43.5784 | 2025-12-27 00:48:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa8ba954-19c4-36eb-a972-1b7dc9f56a49 | -15.9114 | -43.232498 | 2025-12-27 00:48:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 322db36c-6d68-3e4a-832e-5c5b66724be0 | -0.0873 | -51.294102 | 2025-12-27 00:48:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e768cfbd-8353-3989-84ff-c63f64034c93 | -19.198799 | -48.170799 | 2025-12-27 00:48:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 006be240-6884-323e-88ea-2da64c63d3bc | -3.6581 | -43.539902 | 2025-12-27 00:48:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0b65ca0-4b16-320e-b8c5-f59099ee5a6c | -0.0842 | -51.280499 | 2025-12-27 00:48:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 03f6e8d8-2361-3332-a64f-1f208bdcd674 | -15.7457 | -41.9118 | 2025-12-27 00:48:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea715315-9fe4-341b-a40b-944cf17854e4 | -3.2083 | -45.5425 | 2025-12-27 00:48:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63189f58-3126-3f3b-8cf1-d5c56fb470e5 | -20.974501 | -48.648102 | 2025-12-27 00:48:00 | METOP-C | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd95ca0f-08dc-3f35-99b1-626c713dd59e | -15.269 | -43.190899 | 2025-12-27 00:48:00 | METOP-C | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| ba5c7d62-b722-39c7-80fd-2b8005dd2739 | -10.4825 | -44.942402 | 2025-12-27 00:48:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1b89cbd-0385-36dc-8527-f4d2bdc871fa | -10.4801 | -44.9328 | 2025-12-27 00:48:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75a49df0-d5f7-349f-a094-0a757c814742 | -15.7426 | -41.899399 | 2025-12-27 00:48:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c67c39c3-1b4c-3a20-a274-eba26931a9d7 | -15.9139 | -43.242699 | 2025-12-27 00:48:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e6e2e7a0-b76e-327c-befa-0889017153f7 | -5.4536 | -46.192001 | 2025-12-27 00:48:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd97cec-0814-3174-a01c-c76302309e74 | -12.6646 | -46.772499 | 2025-12-27 00:48:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0c13a27-ee3b-3699-9ac7-84955c905227 | -12.6664 | -46.779999 | 2025-12-27 00:48:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 793dc18a-49c3-3b1c-b0bf-fe25371419df | -0.0858 | -51.2873 | 2025-12-27 00:48:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8b374e8d-bf34-3348-ac9b-c60dc2078d0c | -18.9133 | -46.5989 | 2025-12-27 00:48:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dfbe5277-6e2f-3d53-8503-4391baa32ef5 | -12.5223 | -48.393902 | 2025-12-27 00:48:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85a3439e-0fae-3f73-b3ee-89acc6ae96dc | -3.2109 | -45.553501 | 2025-12-27 00:48:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e13142e3-95cd-3d7a-a2e4-8ba5425b21c3 | -2.9011 | -52.595798 | 2025-12-27 00:48:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5333f743-2722-381a-aa8e-bf0b3d4f889a | -21.538601 | -47.1464 | 2025-12-27 00:48:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b809d328-6360-3d7a-b1de-2acd38ccbc97 | -3.2135 | -45.564602 | 2025-12-27 00:48:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fed05d52-9753-33e6-b9ee-d7c3067a2e71 | -10.4898 | -44.930401 | 2025-12-27 00:48:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d26331e9-b0bf-3825-b302-fe869378bd3e | -21.537001 | -47.139099 | 2025-12-27 00:48:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3095fa6d-909e-3dde-9436-0cc5a0bf2660 | -20.243401 | -40.2616 | 2025-12-27 00:48:00 | METOP-C | VITÓRIA | ESPÍRITO SANTO | Brasil | 3205309 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1aee2041-be04-3cd4-9519-fbea4ab06e25 | -2.3751 | -51.916901 | 2025-12-27 00:48:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11b90d0e-dad7-309a-a7e0-882f415fed22 | -10.7728 | -45.032299 | 2025-12-27 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b789886-4903-3209-a016-2311a4d25586 | -18.9149 | -46.606098 | 2025-12-27 00:48:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c6041241-9c4b-385d-8019-ab99810e4c23 | -15.9073 | -43.341801 | 2025-12-27 00:48:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b1ac44b1-d39f-3e60-9e41-cc7658fde344 | -11.3912 | -48.0047 | 2025-12-27 00:48:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab5c17d-84de-3d00-b085-2aba00b3e053 | -10.544 | -48.7192 | 2025-12-27 00:48:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3cf5a0b-f26d-39c3-b2c5-c5d3b70b8d16 | -17.985701 | -47.893101 | 2025-12-27 00:48:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0a5b2b3-a31e-3bfe-a7df-dd040fb3539a | -2.9027 | -52.603001 | 2025-12-27 00:48:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32dce780-278d-370f-bc72-9d5acfa99822 | -11.9429 | -47.8908 | 2025-12-27 00:48:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f87d5b5f-d57b-3381-af81-238bf8b8c974 | -3.7493 | -49.723 | 2025-12-27 00:48:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82723cc6-102c-33b0-a322-c6a898f79b2d | -18.830999 | -43.4702 | 2025-12-27 00:48:00 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d4d9ad7-0917-3e35-a111-9baf1c4a12f4 | -10.502 | -44.937698 | 2025-12-27 00:48:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca1f826-f424-37fa-9124-aa35f2a7bd48 | -12.5208 | -48.386902 | 2025-12-27 00:48:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 603ca8b3-c841-3b0e-bff6-6ae4995d976e | -21.719299 | -47.125702 | 2025-12-27 00:48:00 | METOP-C | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| efe72e2e-86b8-33cf-85d6-f562b1c7e0cf | -10.9527 | -49.428501 | 2025-12-27 00:48:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2d48ced-5e5e-3d97-b00a-13494cd61a8a | -3.7525 | -49.7369 | 2025-12-27 00:48:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59d16b73-efce-38a0-9102-68d938c5a76d | -19.197201 | -48.163399 | 2025-12-27 00:48:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1273e0f2-abcf-3ecf-8b1c-8ea88a9ad76f | -3.1977 | -50.240002 | 2025-12-27 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e38d64e9-db1c-3a8b-bc03-487a9f9263e3 | -10.4922 | -44.939999 | 2025-12-27 00:48:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f91eafd2-ebaf-31bd-b810-2149c98be261 | -10.9511 | -49.421501 | 2025-12-27 00:48:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34da4d33-44ee-31a5-ab3d-782a1644890c | -2.3767 | -51.923801 | 2025-12-27 00:48:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 287d9d3c-2ccb-35e8-b371-3793ff882134 | -3.7695 | -43.576099 | 2025-12-27 00:48:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1628ec1d-baa2-35aa-9593-a7438402e1eb | -12.5183 | -43.7075 | 2025-12-27 00:48:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 139edd72-084b-3ba4-976d-33206192f07e | -10.4945 | -44.9496 | 2025-12-27 00:48:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 813023b5-4bb5-3344-9831-d3e14ac53672 | -1.4758 | -54.208401 | 2025-12-27 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98989bfc-f2f0-380a-997e-3a2ebe31f07a | -3.5929 | -49.447498 | 2025-12-27 00:48:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1291f61d-b61f-3556-a912-33f008912aa4 | -3.5946 | -49.454601 | 2025-12-27 00:48:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 849c9112-6010-38d0-b0c8-0df9d407b8c7 | -21.717699 | -47.118301 | 2025-12-27 00:48:00 | METOP-C | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dba3f64c-a831-3d0c-ba34-34663531bc18 | -10.9429 | -49.430698 | 2025-12-27 00:48:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3afbe261-cbe9-363a-9b6b-b06a87b040b2 | -3.6545 | -43.525002 | 2025-12-27 00:48:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86fe821b-7bd0-32e4-992d-8a76c871675a | -12.5192 | -48.379902 | 2025-12-27 00:48:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ea32e73-cfee-373e-bd25-7cd00214331d | -20.246901 | -40.275002 | 2025-12-27 00:48:00 | METOP-C | VITÓRIA | ESPÍRITO SANTO | Brasil | 3205309 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87e70857-4c76-3bdb-aab6-38452f207854 | -12.2955 | -44.3606 | 2025-12-27 00:48:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03f17062-b1d9-38a9-b649-f7fbf87d5c4e | -3.7509 | -49.7299 | 2025-12-27 00:48:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
