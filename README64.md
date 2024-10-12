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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0863800-0ce9-3951-ba37-9010842d65d9 | -4.26458 | -60.00087 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0329f890-023c-32ac-a446-654dcc4725b8 | -4.2609 | -59.9959 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81e86124-c5bb-39d9-875d-85a1f1eceda4 | -4.26021 | -60.00014 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fca7a6a-632e-3075-9d68-d99668fff07b | -4.25721 | -59.991 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a96fab29-3819-366d-a288-c811abe155fd | -4.23865 | -59.94041 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 974e44fe-d769-37a2-9aea-7db5b42e0671 | -4.23447 | -59.85809 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e023b915-4f77-35a4-86e1-7a8ec6c680f9 | -4.21843 | -59.95431 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edb45e46-2308-3df4-baa7-1b1e4fa13424 | -4.21406 | -59.95364 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e75368c5-52c4-3dc7-8bc0-031c734e7914 | -4.11781 | -58.74487 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bf1ff47-2d2d-3df3-a40c-98cd0ee220cc | -3.99008 | -59.01733 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf00e99b-c0c3-3652-92ca-b9c2bf840954 | -3.96353 | -58.89659 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7404200-e97f-3b74-92f8-72035e425787 | -3.96293 | -58.90026 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0298079b-7b4e-3e10-ba86-eda50786ecfc | -3.93123 | -59.11866 | 2024-10-12 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0e564ed-bc33-3586-be27-286cd1fc387b | -3.93061 | -59.12241 | 2024-10-12 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7294a0bc-b428-38f8-87b5-10ee7bcf9ba7 | -3.90617 | -58.63407 | 2024-10-12 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d33cb80-3102-3471-8ac0-9d8c5cb38364 | -3.89486 | -59.68819 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d54dcb0-b695-38e1-85a3-979926d13574 | -3.86963 | -59.7347 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32f74770-f4a5-38fe-a747-0d43fb1b783b | -3.86896 | -59.73882 | 2024-10-12 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6738212-f5f1-3290-99eb-16ec089ccb21 | -6.46955 | -60.02633 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09d566e7-38f3-3712-83bc-6edd4815e8b6 | -6.45916 | -59.77684 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ca3cf73-2814-39bc-be89-a787638db24a | -6.3906 | -59.97969 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 552c85a8-2f14-380e-9c68-2343471c5349 | -6.38638 | -59.97896 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be6b8d04-8d47-39e8-8d29-ffec7cf6b824 | -6.38571 | -59.98292 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddfd5929-c80c-3cf2-9e2d-5ef4603233b9 | -5.57067 | -60.17279 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc80f15f-4e5a-3474-ac20-5400d355c386 | -5.36694 | -60.09349 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c89d623-432a-31ae-b656-428431f9fe43 | -5.36624 | -60.09763 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bc2a9c0-76f7-35c7-88eb-23ef40456cdd | -5.36262 | -60.09279 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d0b2334-dbf0-3a07-9acb-926f3f20e9d7 | -5.35292 | -59.97834 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 441277ac-f54c-30a0-b5df-0555763a215e | -5.33786 | -60.12379 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31c97e64-2e58-31b3-bd3b-956f3743aa64 | -5.33353 | -60.12308 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4a16b02-8aaf-3d59-b0a0-92da367b73d6 | -5.33284 | -60.12725 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c33f742-3d47-37c9-88a6-6f8492fc83a7 | -5.33078 | -60.13975 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8028d878-8e3c-35e7-9810-459c3877b157 | -5.32919 | -60.12237 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d98584df-93f3-3d72-b45e-572cab19a76b | -5.3285 | -60.12653 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1ffb0ce-e2d9-344d-8575-659ed0a698bc | -5.32644 | -60.13905 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d394c3b5-ff87-3433-b621-5c13a4c46dae | -5.32575 | -60.14324 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c861f9e8-0374-334c-9cad-cbcc283590b3 | -5.29285 | -60.20689 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90b5420b-6a45-379e-a9a8-da565cd7e03d | -5.29213 | -60.21115 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa39e7bd-c988-3633-add5-63cb89115ff7 | -5.28848 | -60.20618 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c017a909-abe5-3e4b-8fa4-5e9fc0f21ad8 | -5.28777 | -60.21044 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c087343-f913-3cae-ae99-0ebbcd9d95e0 | -5.21311 | -60.19532 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 683c735b-3580-3fe5-a25e-945fcba526fa | -5.19778 | -60.07224 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 300dc759-8430-35e8-8968-33eff5fca48f | -5.183 | -60.13402 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f368ecf-a380-3e68-984f-5face33ef615 | -5.1823 | -60.13823 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b72e8bd-7a2f-37bc-9f7f-5de61d30187e | -5.17866 | -60.1333 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0acd5071-8b7c-3db2-b3ac-97aac6df6bc7 | -5.17795 | -60.1375 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7ea56f8-148a-364b-a3c8-61c5e672d055 | -5.1736 | -60.1368 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40df0ef4-f05b-3b60-b096-48694bc7cb02 | -5.08587 | -60.22787 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72da877b-7831-37a3-9f12-6b42f08dd643 | -6.61238 | -60.00473 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14dc6299-d102-338b-9055-02a22d9cc709 | -6.60817 | -60.00403 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65e7b403-d8c0-3f21-b75f-8ee4ca3f12b7 | -6.55571 | -60.03173 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 147157cc-4ad0-302f-be1e-da0c3e61620c | -6.5554 | -60.0324 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae70c1ce-feb9-3b5e-85e8-267bfdc14879 | -6.55118 | -60.03162 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14c4a3fd-4201-3351-931f-ae2a04754306 | -6.55053 | -60.0356 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe20ae32-bcdc-33d0-bcc3-198f478ab43e | -6.54698 | -60.03082 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89b5337b-81d2-3ff9-927a-efda4b785a81 | -6.54355 | -59.76833 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ab29774-6a57-383a-a2d5-09422d723583 | -6.54341 | -60.02618 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab6385d8-8e80-375f-a269-4044835d59c9 | -6.54275 | -60.03012 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58f336f0-d23c-38b8-8efa-4ec6f00b026f | -6.54068 | -59.76008 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eb6c5d1-5aec-3368-b1c9-beb7ffb1ecee | -6.54004 | -59.76387 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbd447d3-e06e-337a-84da-b7848abb5575 | -6.5394 | -59.76768 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80dc62f8-3186-3917-a572-1cc95bf02a9f | -6.53589 | -59.7632 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee85d6ab-620b-378e-8059-0b9069f99b7d | -6.5248 | -60.05964 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87fde6f-8e17-3400-bd42-fdb147f76955 | -6.52123 | -60.05494 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d6adf01-e04e-3cf1-b2ba-dab4f0a0dd2d | -6.52055 | -60.05902 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51b00624-aa98-3825-b02d-2d43b4f8d967 | -6.51631 | -60.05834 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af894565-c9a9-3c1f-87dc-016bcef29bff | -6.49939 | -59.97851 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ff18709-042f-3b9e-86f4-aeab972f0048 | -6.48328 | -60.07337 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ca8302f-c7d3-305b-a8c8-95b90a22d551 | -7.05504 | -59.26548 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55d8e962-bab6-3adc-bf7b-372660eaa129 | -7.05105 | -59.26481 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58e62ba3-6ad2-33f2-88ba-5d8e99077e7c | -7.04707 | -59.26415 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 963eb109-50f0-3a19-9772-facf75438ffc | -7.04648 | -59.26765 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56ca8fbb-f0fd-35e2-9334-e65fca6a523b | -7.04063 | -59.39975 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16d05213-57ed-3103-9ca2-9db7d9c3ac04 | -7.03335 | -59.36955 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba4a6cf1-694e-32c6-af83-56fc77f4dd17 | -7.03123 | -59.43098 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| edac25a5-5619-3d00-b479-a3b1636e8dd2 | -7.03063 | -59.43453 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 683ad0d8-e1e1-3018-8c25-3aa9afdafaac | -7.02934 | -59.36887 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b90b0d10-39ad-3f1d-9979-f28487dac7b4 | -6.81066 | -59.14227 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e915816-6ec3-3f46-9ac7-27f0d61d6258 | -6.80669 | -59.14161 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2973ff-4130-3d64-b665-5087ddc41c7f | -6.80613 | -59.14502 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ce9c255-5027-3cea-babf-47c29c5f57b0 | -6.80541 | -59.12465 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4d71a38-bf69-3d51-80cd-f97d416ea9cb | -6.80182 | -59.33008 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e971f990-638a-3362-b961-ef1fb617c91d | -6.80122 | -59.33358 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0f0626-1e06-3eac-bf5b-a9a8b7696277 | -6.79721 | -59.33286 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c89df95-81dd-3ca8-b148-eba64b86f37d | -6.7936 | -59.35405 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7e171a63-670f-38a9-ad4f-75c983211d27 | -6.78958 | -59.35335 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1fac7ca2-056d-3235-ba34-eccb3a8b7aff | -6.78735 | -59.30939 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28ee2ae8-1811-3f0c-852f-2dd90fa427b2 | -6.78677 | -59.31291 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c7fecd8-801d-36bf-95f4-e771ee51a1d5 | -6.78334 | -59.3087 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7e03c9c-b6d5-3717-bd4f-40f433793830 | -6.77818 | -59.31502 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46523c3a-09cc-3a7c-9220-abe922f0d664 | -6.77761 | -59.31849 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2715a94-c447-353d-8f62-caa11e0d5916 | -6.77417 | -59.31433 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d875636-7be9-3e40-8954-c5b0653629fc | -6.77359 | -59.31782 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab74ba16-0c4b-3a37-9b7a-a6eba4efcf77 | -6.77302 | -59.32132 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0963cad-0036-3a83-a82c-84bb7bf57b3e | -6.76958 | -59.31715 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb5e15b8-9433-3541-b161-4c76eb21de5d | -6.76842 | -59.32418 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2edabcd-2979-37dc-b34c-f163915c17a5 | -6.76499 | -59.31997 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b723ef1-1574-3174-ad9c-7010884f18c4 | -6.7644 | -59.32353 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad2d5c8e-c683-3844-b46e-901c20c35449 | -6.76381 | -59.32711 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f85fb0d-b1d8-3479-b9b2-2b9fd6e6d5c4 | -6.76097 | -59.31931 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README65.md)
