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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2271d6a2-56f1-3569-a81f-46a3ea31af6f | -8.91044 | -46.59679 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d3929fe-d8a1-3035-a713-07b6b5b71cfd | -9.39403 | -45.83389 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7022afac-f5ca-31ba-90bc-1632b9eed91c | -6.00839 | -42.51641 | 2025-10-05 03:53:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a28cdd7-f091-3891-8481-8db7ed6e7536 | -9.75269 | -47.73934 | 2025-10-05 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| faa024d8-3440-3f38-ad50-78acf1f3014e | -8.5765 | -46.32131 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f04518fd-6859-3916-a70e-676254527c22 | -6.24501 | -45.35955 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d1fa204-e046-3842-bd48-42bb61a4fe89 | -7.69427 | -42.59294 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bfa06878-d0a7-39a2-b4c3-e59e1789a220 | -5.4131 | -41.34361 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72e1471e-d6a1-3c30-a05b-dcebf5db0922 | -7.63128 | -45.48615 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa36814d-c041-30c3-9c46-4a3ba5dd9e13 | -10.63766 | -46.34056 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 72bcb258-d91b-38d4-bad2-50341b11b263 | -5.88507 | -43.71188 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3ddc71c-cf17-3c0c-bb01-d7e931ad8b75 | -9.04908 | -47.0161 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9278099-aa0d-38d9-b9f8-18dfd5edbe05 | -8.16334 | -44.12756 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4b24a0c-abe3-32ca-a549-525e61b7df56 | -6.1002 | -43.47986 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e093021e-ac32-309a-8ceb-979a0caedb74 | -7.69207 | -42.58286 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 503eb653-fada-366f-8ef9-a54ebffb4c5b | -6.83577 | -45.48964 | 2025-10-05 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 450dba20-bfd1-31db-91c5-0faac24183f5 | -6.59425 | -44.3212 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc8f43fa-cc58-3912-b29d-151fead2527b | -9.29924 | -45.9955 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6f14eb84-fd1e-34a2-8417-7c3d973cad90 | -5.98404 | -44.35566 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c068c945-4964-3675-bd11-6f9847a2bf5b | -9.90487 | -45.95554 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8ab5b47b-9f92-3525-8ff4-9e58fa5017ef | -8.87352 | -46.72879 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a8dc91e-8163-3327-994d-9221a27427fc | -10.19398 | -45.53762 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86f32a78-d2ae-3cd8-9fbf-d9e04e38ed30 | -3.80914 | -51.29765 | 2025-10-05 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a39e64e-4916-3c46-a1b0-d2f57f730a9e | -6.14689 | -44.64449 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a4cac087-7da3-3417-80dd-c3eb1dedcbce | -6.2105 | -44.0751 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb0c6c6f-7db2-3ff0-9298-07207e59f81a | -5.34435 | -45.29938 | 2025-10-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2aa949fa-d16c-331a-b5ba-f5cc53b833ed | -7.77213 | -42.61334 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0f9c0968-8de1-3422-b59c-ab5019bc3ebb | -9.64547 | -45.85118 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cc3cc2a-ced7-37ab-b58d-0a12b515f10c | -8.58034 | -46.32742 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| df928887-0524-3503-bae6-da42210d763c | -6.06723 | -42.52842 | 2025-10-05 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2eb7bf67-5614-37a4-a07d-165761eec0f0 | -6.60044 | -48.05393 | 2025-10-05 03:53:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e5ca652-8ba0-35e5-bcd6-736a4f945687 | -7.72317 | -46.27679 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d07f0049-0a0f-38a4-91b3-410ba34c7ab9 | -5.2116 | -46.18349 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e00014b-bb6c-37b0-908d-642d73bd97e8 | -8.60022 | -46.27089 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2d2bf7de-e0bf-3cf0-a82b-e6fbf40c256b | -5.83716 | -42.45439 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8dd64c41-4769-3c01-8d95-53bcc5add753 | -6.20985 | -44.07902 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25c0dd5c-c116-3db6-8b3b-e8660ff2c012 | -5.91057 | -42.5232 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 32876e66-16b6-3ce1-81ec-aeabc8b68334 | -10.24232 | -40.50901 | 2025-10-05 03:53:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e054a444-b171-39be-864b-fb26e5fd6981 | -8.85801 | -46.78777 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5b25952-5571-3ad5-b044-86cba7d5a895 | -6.70823 | -42.17487 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36516c4c-8eae-3ca2-af30-c832be083463 | -7.80821 | -42.53808 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| af4b2b94-540f-32c1-8ce3-9c21a7ca2484 | -8.17033 | -43.34934 | 2025-10-05 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c72d49dc-b619-3d0e-a387-94c2817eb9b2 | -5.41379 | -41.33939 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 13334f3f-1e1a-3b5a-adac-72e49f223b6c | -6.1018 | -43.48732 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62a0cb9c-5c2b-330c-9197-a24e9107a8aa | -5.78279 | -42.92953 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 52d180c1-89d4-3883-a270-18dcb7b23f75 | -6.10115 | -43.4911 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95ede153-b7c5-3445-8a47-4bb15f8e0aed | -6.21409 | -44.07993 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4dd5479-b133-35c6-9913-a2cac5be8641 | -5.18442 | -46.16336 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1489bc9f-b9d7-3c1a-aca7-27ce0bde8145 | -7.04552 | -42.76259 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5150892-e377-3531-8777-4a632c468c06 | -5.8438 | -42.80768 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 429b3c90-1963-336a-aa5e-05b78aa607ef | -7.02131 | -42.78852 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3c1b6fd6-d933-3339-b3ae-726a808214e2 | -7.71447 | -46.26971 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e8779d1a-a19c-3d29-b0a8-bd4166db305a | -7.05472 | -42.77908 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 26e0a8b9-83ed-3f80-a93e-ac12359b59dd | -9.05304 | -47.02264 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a5bb696-9273-3c58-833c-c6017c568801 | -7.54498 | -47.27864 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e97e725-0979-3862-ac3c-be0c099b3c46 | -5.24541 | -42.6346 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3442539-9fb5-387a-bec6-6fb651f94743 | -6.55567 | -44.1581 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4291497-7c83-3332-90b0-304d41ba7a13 | -7.742 | -42.61074 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f493a931-8edf-3ef8-a649-4c0e2dddf689 | -6.69988 | -41.94796 | 2025-10-05 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c78cbbad-0f41-3d01-a573-7832eb3552f2 | -6.70763 | -42.83508 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 38c4db5c-5217-38e2-9e58-69b480802039 | -6.03569 | -42.66886 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96db3403-803e-370e-b36c-96e469c37118 | -5.92462 | -43.32696 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1d0b121-b179-3824-a25c-2bf88449888f | -6.25945 | -42.45364 | 2025-10-05 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b127c81-59b6-3ab8-ab51-583c623ffd22 | -6.60935 | -44.32218 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95e85483-1984-3ede-9675-23c98d0f6a84 | -7.05859 | -42.77974 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c8d438c7-a08c-324e-9928-76adc16081d2 | -7.24651 | -44.89844 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cecefad7-9a85-39ae-930c-ca364829ca68 | -6.37262 | -42.89179 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 61600d75-f94b-3403-a043-f9bd67730b16 | -5.81719 | -42.07375 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e7b637a-09cb-3ebd-a52d-2caabf56d06a | -3.81286 | -51.08208 | 2025-10-05 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f66d4901-a2bc-3e53-9ee6-a27c91422408 | -8.58221 | -46.31689 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| da7ccf33-6c06-3cfd-b16c-93d98258fa9e | -5.58605 | -43.40383 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b741a9d4-49cb-3eba-9257-0449df91ed63 | -5.98768 | -44.36063 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e350c1df-85ed-3a09-8e5f-312f07893c83 | -5.91364 | -42.89454 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b3916c5d-3720-37d1-a2ce-89c2c1acc683 | -8.60113 | -46.29344 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 064580aa-2ff9-3e84-bab8-d92f64891071 | -9.20005 | -46.92702 | 2025-10-05 03:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 99f99252-33fb-343b-8b61-68266e3ae38a | -6.07861 | -44.85301 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36361755-6894-362d-bf62-bcae2c62ad9d | -7.64883 | -45.49381 | 2025-10-05 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8b18d5e-b384-3251-b899-9b0ab338de5f | -6.72245 | -42.15865 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7834e687-8dfe-3357-8eb9-faee8026f4a0 | -8.23226 | -46.80592 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4b0b1636-f5a5-304d-8e86-307f13c26e53 | -9.05476 | -46.9896 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 215aabe4-cb6f-3098-a7f6-ab84b64fab83 | -5.00561 | -47.21761 | 2025-10-05 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf541d40-0352-3ba2-9068-0ab7636dbb5a | -6.15207 | -44.64085 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3aabce25-f386-36b7-9c50-3c25a00fd8be | -5.34905 | -45.30016 | 2025-10-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac1b32cc-43f4-3946-a0e6-e67394492e70 | -10.29994 | -47.94432 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 057d6782-2881-3667-b1e6-804c9ad57979 | -5.99204 | -44.36142 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8081cc0b-572e-3ef1-8924-ba29bd93d790 | -8.23472 | -46.81665 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f0f70cd6-70f3-3f08-afc7-95a2b42acd60 | -5.67427 | -42.73647 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2cec20bb-a6de-393f-b265-bf272ece32c3 | -8.57078 | -46.32577 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9e121c31-859f-315c-8023-013ac7328390 | -6.55926 | -44.16276 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f895e09-110e-3159-af3c-cda49ee23117 | -9.65368 | -45.85771 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a3d66ba-f12a-3cf5-8e97-4241b95e6c28 | -5.86407 | -42.51558 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5aa20f9-2780-381e-84ac-9ea921b96138 | -6.36007 | -41.62537 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7f21144f-72d4-3bd4-997e-3a99a0990f88 | -6.15721 | -44.66422 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a0d252cd-a8a2-31b1-afe1-abd503fcda29 | -6.30326 | -44.44399 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93c6c8c8-7301-3675-b71b-1748fe6bf443 | -7.3168 | -47.28655 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd1672cc-86ec-3ae9-a1d3-9521cd369e78 | -8.53757 | -46.3186 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 408fc4e3-79cc-3536-a055-08e58f3c4c01 | -3.61242 | -51.04587 | 2025-10-05 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39157a29-f895-34ec-aae0-d04e08dbf8d6 | -6.40051 | -43.60513 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9616ba6-597c-3132-9d91-3834bd42382a | -6.42478 | -44.47188 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60f25313-5c4f-3f37-90b4-2508a0862eb1 | -10.8676 | -45.40866 | 2025-10-05 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README50.md)
