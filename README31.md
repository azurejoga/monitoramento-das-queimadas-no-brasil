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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e49be2ee-4722-36cb-8996-af16f0ff7f92 | -2.29949 | -48.57501 | 2026-09-18 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5268412-0390-3d82-a5c2-4ce58e7f14af | -5.76318 | -45.8021 | 2026-09-18 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 314d5fb0-d35f-3b32-a76e-7f02347a19cf | -6.65864 | -50.91994 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41b6f826-37e5-3e4b-9fb8-1cff4a9c01fc | -7.75934 | -46.6502 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bde27ca-9806-38a4-88e8-e3218f8889be | -3.07195 | -49.51832 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c59e438-18c1-3a96-a020-6b4cd06aefc0 | -4.43148 | -55.51833 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2317b4a4-9afe-3bbd-a542-e05ae40205b1 | -6.66225 | -50.92461 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| feb49b85-7fb7-32ce-9e55-e1dcc09113c8 | -3.57338 | -43.46925 | 2026-09-18 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 351d0bd7-d7a3-3359-afbf-dd2299623e5d | -6.55005 | -44.38441 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f51f3745-8a27-3021-a22d-7c67e08ed2af | -5.16001 | -45.24765 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ac87bf-9fdc-309d-ad77-a4b3dc65f3be | -5.35367 | -43.19477 | 2026-09-18 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20e5c059-d8e4-3b9b-b4ce-611448ca398f | -7.79513 | -44.90686 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ccb6e58b-727d-3c5d-a55e-34ff15789c7f | -4.37867 | -46.24774 | 2026-09-18 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4422ee37-63ae-397a-bfe4-a17a0009d050 | -4.58431 | -42.95568 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5cec10c4-04c2-3ed1-89b8-331254a010d9 | -7.79929 | -44.83653 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ab5a6d7-8982-38e1-b4bd-ee7cad00e38e | -7.47616 | -45.29585 | 2026-09-18 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 330929e1-9830-3048-baaa-00e865c2eb0f | -7.63503 | -44.40426 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 665b913a-7620-3177-a100-d72302b867dd | -4.5691 | -42.94227 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee1f4600-37b3-3c70-9189-a6f9b380b93f | -2.81315 | -50.47146 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b093aed-0f6d-37a9-81fa-a529faf300fe | -5.27186 | -43.34658 | 2026-09-18 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62d7cc68-fddf-32b2-9248-4fb540287a32 | -2.90575 | -40.39625 | 2026-09-18 04:19:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f234f79-0558-3829-9761-9ddf2df7d669 | -7.79567 | -44.90339 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 07665f1c-1bc1-3af9-b987-318ee1213753 | -4.79311 | -56.12343 | 2026-09-18 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9f29d97-38df-31ee-a6db-3105cbb9c6a2 | -7.0119 | -43.63826 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ef9f81d-f368-3e64-95c6-8daa39f27795 | -5.43094 | -43.44351 | 2026-09-18 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f0d9154-f3ff-3feb-968d-5dc449995177 | -6.13237 | -43.74323 | 2026-09-18 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b25f420d-3a55-3dc4-b8f3-dadf3f15b026 | -7.72697 | -42.48582 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2aca9dc8-aaca-3f45-8420-3a0122f21156 | -4.56614 | -47.76453 | 2026-09-18 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54f46390-2b3b-3a75-b7d8-10b3bcf2bdaa | -3.49938 | -51.24874 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80fef768-ad27-3560-8f13-2f534bce4476 | -3.47076 | -54.70852 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48d623db-58e9-3928-82f3-87bd02522784 | -6.55667 | -44.38544 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba8b54aa-28ad-3df7-9fd3-1627098fb19f | -7.09795 | -42.09352 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 083d1a7f-f04e-3f10-8436-809c1a11e2c8 | -5.55115 | -35.75809 | 2026-09-18 04:19:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a0ac480-c8b0-36a3-9266-9af11f187d78 | -6.36988 | -43.56959 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d8f8670-3b58-340a-8375-88c27f9530d3 | -7.01859 | -46.44995 | 2026-09-18 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b1257c8-658a-3025-b8a6-b5d800ad1851 | -2.90716 | -40.43696 | 2026-09-18 04:19:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9201ddf8-9e84-30ee-957c-aa10873c2b7c | -4.87963 | -56.0684 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c34d10eb-75bc-3fa2-ab2e-a1a45caf045b | -6.65864 | -43.63542 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c034992-4120-365d-be00-b308a1df60e3 | -7.04209 | -42.08158 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 761d4c4a-4d48-39b0-970a-ada93ca28706 | -2.89669 | -54.17995 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2cbb984c-0b07-344c-b4fb-bbef113b35ee | -7.51186 | -47.08083 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5fd0c2e-c08d-33cc-915d-4c78f10d5a6a | -7.19157 | -44.54534 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5222fd9f-b870-30f4-a139-86c20f395c25 | -6.30828 | -45.69059 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b07028ed-145d-342d-9950-2603f0351424 | -4.36656 | -46.17083 | 2026-09-18 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04a4dacb-902f-3e69-bbb9-426502bc0db7 | -7.86412 | -44.83607 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0000140-9586-311d-9bac-5244d5991c04 | -4.56463 | -42.94897 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f33d33c-8334-3bbc-9058-737d77fd7005 | -4.58093 | -42.95518 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0e69e6bf-81d4-3a6d-9c43-ce7da978367c | -5.63844 | -44.79936 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30a66319-01bc-3fd3-86b9-c3fa1750d2ec | -4.43813 | -55.52584 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c9e98428-ea3e-31b8-9a05-be428d07be76 | -2.95548 | -50.32161 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a554affe-06ef-33f2-ac33-7bfc3aaaa2e6 | -2.63906 | -54.691 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eff3b889-8b1b-3c56-acd9-a6df7a3ce451 | -4.42735 | -46.29318 | 2026-09-18 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73256750-d7c1-37df-ae45-a57062326b06 | -2.61013 | -54.75622 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| c6f80cf6-448a-34c9-b067-6878862c3939 | -3.36633 | -50.46021 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f28128ce-8a3d-30ea-b593-cf70cd3c1ef3 | -7.17072 | -44.57056 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fd3993e-6f9d-3009-9c87-4bda63f7a054 | -7.95925 | -43.97768 | 2026-09-18 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7941bf65-e1be-31e2-9ed7-d10c2998f6c6 | -5.12705 | -37.71445 | 2026-09-18 04:19:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bc5119b0-acd9-322e-bd39-ef9ceec40c3e | -7.68107 | -46.0892 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8088ff13-4087-3a1c-b4de-a9a84f79881a | -2.90346 | -40.43637 | 2026-09-18 04:19:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f203380b-9d5a-35da-8ee1-a9d26575e99d | -7.3666 | -44.46982 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36fb19a3-ccff-3483-b54f-0eeaa6ac1581 | -6.30884 | -45.6871 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f76cde3-a9f1-3c80-89f9-079a489acce3 | -3.3707 | -50.46093 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30d85f3d-2de0-3a0a-b10d-ea162c5adf80 | -5.65434 | -43.38347 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2df4e1d7-02a2-35ab-98b6-aceda28abb94 | -6.66569 | -50.90447 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9354339-c1cb-3483-b0a0-ac413c3aee9a | -3.70593 | -54.17664 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 911e6588-57a1-3e44-b302-a4f19637d973 | -7.19562 | -41.80835 | 2026-09-18 04:19:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0767a564-fcce-39a8-a3f2-35d266d008f3 | -4.87771 | -56.07055 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 699a68d9-1ea1-3be3-8fab-3bec1358d386 | -6.49733 | -43.82188 | 2026-09-18 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9acd5b2c-d045-3c0b-a4a7-1df9fc2e1075 | -7.19804 | -44.10666 | 2026-09-18 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98c17e46-551c-3d34-95a2-996ebeb549ea | -4.01238 | -42.45298 | 2026-09-18 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2e13ced-1a0a-3d35-9bac-68e2100d1007 | -7.67995 | -46.09624 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a7449be-8703-3fe9-b7e2-896741710a4f | -5.19451 | -49.33435 | 2026-09-18 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bf67678-d84a-3e2b-8381-64f12b9a5c85 | -7.66275 | -46.09712 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da70c62d-c8d1-38b1-96da-3f973a20fa88 | -7.33582 | -44.62521 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 634ad1fc-4ca8-39b2-8425-b7d8c6776464 | -7.62924 | -45.83654 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a539dfd-fe3f-3e33-b961-c9dcc0acf690 | -5.41437 | -42.9442 | 2026-09-18 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3d8c3ca0-12e2-32b1-a838-203470d323a7 | -2.82868 | -50.48739 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b7af278-f71f-32b6-a5c2-4d8ffe5885eb | -4.36059 | -47.78197 | 2026-09-18 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c4ae939e-7c34-382c-a31d-a12fd77dc2bf | -4.81517 | -42.89109 | 2026-09-18 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1b2472fd-2695-3462-a2b2-c283028313a6 | -2.81347 | -50.47295 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4634ce61-baa3-38fb-844b-8ab13dfd984b | -7.06118 | -47.482 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 494f744e-e81f-36ba-9137-84feb4384c32 | -6.93305 | -41.71638 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 351245ed-d32f-3128-acec-1c45b1132af3 | -3.57284 | -43.47272 | 2026-09-18 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 363a65bd-d2a4-38db-b4d9-a36187bff552 | -7.45572 | -46.15846 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1fafb4d-226c-3fab-bee2-c82e07057e89 | -6.12903 | -43.7427 | 2026-09-18 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34afa257-7ad6-37ee-a6be-1ba4602f2493 | -3.26247 | -54.3069 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e1976d4-0dc9-3765-a3df-00b52b911380 | -7.09499 | -42.08894 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ad396eda-8945-33b7-aa4f-696237a9ea5a | -7.37054 | -46.80089 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c558455-9ae2-33d5-ba6f-619923199814 | -4.51712 | -56.08266 | 2026-09-18 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 33394c53-465f-3f7f-9afb-a7d2919df4c5 | -7.93402 | -44.8221 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6852783-1eaf-3770-aa84-b2af9ed74895 | -6.52336 | -49.89233 | 2026-09-18 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0ace780c-ad95-34ca-999c-531f43a1ac98 | -3.37648 | -50.45313 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c626f976-27eb-340f-ab31-15eb793ce793 | -6.94976 | -42.54996 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a20b7c2e-64e6-3c7e-8406-7bbb3f17afdb | -5.33616 | -45.14455 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bcf22209-d7e7-3967-b1c8-560ed54cd25f | -7.00799 | -43.64132 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 273fba53-31ef-3f3b-bf60-1c43dde80cfe | -3.47004 | -54.71277 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b70cbca-0716-30a5-85e6-34aa60e14486 | -7.35666 | -44.46827 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8f3ff922-68ac-3509-8cf1-af610440818a | -1.70145 | -49.85529 | 2026-09-18 04:19:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 802f8c40-535b-3b1c-b7a9-e36ddbe2f7f3 | -3.16692 | -48.60975 | 2026-09-18 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e67c4d64-5914-3e0e-865e-85211fbbf3b6 | -2.89865 | -54.16819 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README32.md)
