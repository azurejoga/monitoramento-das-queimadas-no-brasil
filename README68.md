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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ee96ebc-1260-3ea6-91d1-c32e88cbdcd8 | -11.81948 | -45.13377 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 559398c0-2802-316e-b1f6-f1f79694846c | -8.97724 | -47.47988 | 2025-10-08 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cd36650-eb82-3427-907d-42fd35782df0 | -8.18879 | -43.34698 | 2025-10-08 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 175121f0-11fc-326b-803f-61a738a2cf6f | -5.71676 | -43.61795 | 2025-10-08 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5d6459d2-8434-35dd-8b3f-33a795398cad | -4.68794 | -45.84565 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5eaf656-a327-3dcb-a43c-90bc9ae11412 | -7.67315 | -42.58493 | 2025-10-08 04:38:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7d64370-d9df-3a79-9528-30a6fd004bd4 | -10.64604 | -47.45663 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5244ba16-9a21-3624-8b1c-eb91d68d5ce9 | -5.81237 | -45.8488 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ed30c3b-2917-3358-8bd5-d53e2eb62460 | -9.2593 | -56.28919 | 2025-10-08 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c812c733-a6dd-324f-8a60-6ab5b547a6c8 | -10.43488 | -51.63021 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7718ebf-06be-3a0d-b3ee-70903a18ca35 | -4.94661 | -45.78934 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6472609a-dfb8-3084-8c4c-a4c6a094453c | -8.28875 | -44.80771 | 2025-10-08 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64caf166-1f35-305e-aa00-5be31d67ce58 | -7.24499 | -48.48031 | 2025-10-08 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61fcf9f8-9f60-3f8f-9659-6a3093f9c7df | -5.17133 | -45.12985 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d3c1b5a-9b34-360e-9136-22f21137da81 | -7.22145 | -47.18071 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 310b0f71-5448-38a9-bde7-c0d3cb1baf52 | -7.81058 | -44.1807 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 627127c5-b568-3b01-8512-dd11753131e9 | -5.74282 | -44.40731 | 2025-10-08 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02e3ab86-b69c-3591-b5e2-81e383e7a8c8 | -6.00471 | -43.74734 | 2025-10-08 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df4ee4c6-baf8-3a77-854c-0093a1fac1e0 | -8.46543 | -47.20632 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe2ef3ec-a74b-37bf-878c-da0d85ea6dff | -11.22594 | -47.75979 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2662b55-3a96-38b8-a848-ac88eedb5224 | -5.49962 | -45.52124 | 2025-10-08 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 421d7251-5e9d-3ee2-8f08-936ca35f3971 | -9.18839 | -46.91131 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17efe6fc-0c0c-306b-bc49-c8ef516cac0c | -4.69637 | -45.83851 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 345830e0-4772-3f4e-83a2-e74223df1c4f | -3.82853 | -50.96979 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c630df92-03e1-36e6-90e4-991c83f01739 | -5.13833 | -44.9654 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6411cb65-0fcc-3eb8-b7af-841aec694bd5 | -6.11274 | -43.88829 | 2025-10-08 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eccb2986-2d36-344f-8398-e75946062620 | -6.68502 | -58.81577 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f252fb46-ebe6-329f-9178-e05b0da7aa29 | -4.68406 | -49.49475 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d64bc069-b881-3ddb-9531-bef36942a011 | -10.0433 | -48.27842 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60459db7-5850-326b-b647-24d36345eff3 | -4.08376 | -48.04553 | 2025-10-08 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd8339c1-6c1d-302b-99d8-c3a2bdc59737 | -4.30842 | -48.0839 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b12f7cbc-d7be-3a3d-bfea-1414f7dae821 | -8.71009 | -47.86079 | 2025-10-08 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55b23427-18bf-3068-a49d-7359cc858e96 | -9.1848 | -46.91081 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99ce6b8d-b444-3536-b8c2-89f84b9c32ff | -7.77133 | -44.18938 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0238de85-219e-3e4f-9eb7-2c03ad6b16b7 | -3.5753 | -49.43709 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afaef5aa-b965-3783-8431-d62c97368271 | -5.30139 | -45.84603 | 2025-10-08 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8695cb15-0309-3a05-8e7f-f97c93263c06 | -8.62342 | -45.10028 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19c312a6-90da-345b-b64a-2cf499a89207 | -8.15841 | -50.16589 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 817a060a-701b-32b9-869d-70db4fe72040 | -10.61697 | -48.64478 | 2025-10-08 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c82c6765-080a-371d-999f-d14838867009 | -11.14432 | -47.74856 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69843461-6cbb-3ca7-96b5-112b2fb42fd3 | -8.23327 | -44.18571 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21146362-706f-33f9-9c14-ee662761ce2f | -4.68918 | -45.83752 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ac71d647-9113-32a9-bfc4-ada34017907d | -7.44093 | -43.14727 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 55517143-6853-3c0c-ab23-a6f51e2597e9 | -10.91028 | -47.13494 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77f68b8b-2fdb-3454-bd65-89b705e88ffa | -4.92214 | -48.5458 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35facaaf-d993-32d1-840c-5f18d9af56e6 | -9.04354 | -50.62421 | 2025-10-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c377fce3-5da8-33d6-962d-ce9837bc4f27 | -10.64792 | -47.80271 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccc721ce-4dd1-3941-9322-a3850db6d689 | -7.44347 | -43.1301 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 75d0f6e4-1d29-3fb2-be27-6dd71d9bb4a8 | -6.42083 | -47.24075 | 2025-10-08 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3b0b79b-987b-31b5-8ff4-249008ece22a | -8.67567 | -47.07928 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c67bad9-5de6-3502-bfff-3c14b08c5bd2 | -10.29353 | -48.24309 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5dd12d0-6a4e-3fd8-b101-fb7d5071a65b | -6.69167 | -58.80982 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce65941b-9634-3e3b-8df3-bfbb3392e2a8 | -7.44894 | -43.15106 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6578b21f-0bd2-3805-8c34-7478dcded1ee | -8.60096 | -48.25205 | 2025-10-08 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9db33cd0-d005-3bfe-9edf-0caedb806912 | -8.85706 | -46.78001 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 467ee83d-ce52-3727-8361-b566cd55fc32 | -10.29408 | -48.23944 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 713aa1d5-9847-3349-9ec8-64d81de566b7 | -8.61516 | -44.90551 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d20dcfc5-7d0d-3359-80a9-0cfc3fa95482 | -10.49963 | -49.13814 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80a0afb7-1c51-341e-b786-434f2a4a24b9 | -9.9196 | -49.96274 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 063a9b71-21d4-3758-9578-84fd03a65558 | -4.87391 | -46.82764 | 2025-10-08 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b85ee00c-5ed5-30e5-93e6-768c4b1fe65d | -10.37899 | -47.98103 | 2025-10-08 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 936f597b-4b93-3de0-b42a-212eef2d93c6 | -3.83547 | -50.97081 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d098629c-0df5-3e9a-bfad-a0eac541762c | -5.28116 | -48.11702 | 2025-10-08 04:38:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed7fdcc8-b005-304e-94a4-a2eff1707abd | -7.78312 | -44.1953 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3589b0d8-9318-31a6-a3bc-26ed58d4b0ea | -5.68344 | -46.38278 | 2025-10-08 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d20048-dc5a-390d-b2ec-3211fb7dd2f8 | -10.39019 | -50.23175 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 335be433-1a77-3b32-8460-7db966026be8 | -3.45702 | -50.09166 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea8b889d-2756-3d76-adc5-b0bc49c139d9 | -9.00479 | -45.50326 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 698b5a46-64df-3ca8-99cd-afb8f028592c | -9.30221 | -60.60315 | 2025-10-08 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c2a83f5-fac6-396e-9fa5-269c02f934e8 | -8.22109 | -46.83323 | 2025-10-08 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da7be9f8-7fed-3529-a819-cba16b6e1251 | -10.94138 | -49.48454 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3555d6a8-8d9e-3435-ab4d-2b73abc7f08f | -11.18423 | -49.78059 | 2025-10-08 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74de55a1-a162-378e-96ae-39d03117aefa | -5.53168 | -46.55062 | 2025-10-08 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dd36df3-7ad6-373c-a93f-560aa944ae3d | -6.19306 | -44.35954 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03b1bc0d-a766-3592-b0a6-a2cf7c960210 | -4.90661 | -45.63733 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10b2cb28-a216-36c5-98e7-8d4a66878ec2 | -7.52336 | -44.08934 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8a4102b-dc34-3862-a79c-0e6dc7d70afb | -5.86485 | -44.30434 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9110bde9-fb69-393e-9a87-25ed4d08a240 | -7.24221 | -48.47627 | 2025-10-08 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5811cae7-a86b-331c-a535-05e8157ff232 | -9.68052 | -49.92838 | 2025-10-08 04:38:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a62fc95-1432-3c91-938f-a04a7656037f | -8.53467 | -46.22955 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28704003-ea53-3674-a460-24d50a7a4800 | -8.55305 | -46.23245 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a2be32f-8f04-30ac-898c-c49fd6130094 | -7.25588 | -44.10924 | 2025-10-08 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f06d5f9-e234-3dbc-bfda-d49f9a09d208 | -5.48976 | -44.61925 | 2025-10-08 04:38:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 891f2ba7-a33b-31cf-9b87-52cb8633de36 | -9.21007 | -47.84288 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cbf3ee5-0de8-31d4-bf91-063b335577ab | -9.18197 | -47.79596 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20b34e7f-bbbd-3ec8-824c-a20597e7ea6a | -10.22755 | -52.69944 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0da8023d-10de-3300-bf16-5f814351a685 | -10.81148 | -48.58796 | 2025-10-08 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96032e8f-4b4f-36a0-a66c-e889f89df0bb | -5.9133 | -44.1969 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98f3f424-18c1-397a-9c03-ae0721378f83 | -10.6829 | -47.54857 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f55692e-aaaf-3d2c-b9e3-f2184c44d051 | -7.80889 | -44.24909 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aac11bf3-7ffc-36d5-8db2-bbd357105172 | -11.78402 | -45.14804 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aa25cd5-c209-3a18-9158-ebfdc217dcf1 | -4.90603 | -45.63877 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a74d1a5c-00dd-329a-aabe-aa017e1167b6 | -4.06903 | -51.03764 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddedb3fb-c570-398f-a27e-f3689e030ad4 | -5.7767 | -46.15357 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 936f23aa-959f-383f-8d5c-b99d56e8cfbc | -11.156 | -47.74255 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d51e8798-a9fd-3915-99eb-ae9f41014635 | -8.89305 | -46.0268 | 2025-10-08 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 992e9ccb-9e8c-3e42-9324-9db8ac46132d | -7.51866 | -42.71859 | 2025-10-08 04:38:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 817cf756-d3c7-3e65-b367-422103fd6b1e | -9.1758 | -46.9222 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ed6c03b-b540-3029-92e9-dd5f3564160d | -11.34082 | -44.87955 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 136e677f-dbde-3aa3-9f8f-963dfda0af9c | -6.13397 | -44.60191 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README69.md)
