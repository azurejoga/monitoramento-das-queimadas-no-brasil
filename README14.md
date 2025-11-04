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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d12a453-f869-3010-8314-f9f16cd9bcf8 | -5.92439 | -41.30545 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74bc478f-2de8-3a66-b85d-5a1f4f73c93d | -6.10086 | -44.43699 | 2025-11-04 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01f6a1da-38ca-32c5-baed-1c827ef27bec | -3.48915 | -50.32005 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5dd258f8-e5e8-3f59-8587-0f69d9c623fb | -5.42887 | -44.66123 | 2025-11-04 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec7d7354-8ab4-37d1-9028-f11a754d6b8e | -5.36795 | -44.74121 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7fdcb2a-43ab-3dc1-903a-2a181b9ecb72 | -4.95498 | -44.90755 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efe47cf9-6873-38c8-8754-9cd6707079c9 | -2.49112 | -45.97549 | 2025-11-04 04:10:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a35146fc-038b-3bfc-9b1d-69df9625f90a | -1.23008 | -49.15689 | 2025-11-04 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0872bd18-d172-3814-b55c-aaa5a5e84205 | -5.9233 | -41.31238 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0b9c076-0583-3323-aa03-c248ce4bf20f | -5.52036 | -41.12102 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b22f0c08-1874-335e-8796-dd37cf53eaf4 | -5.532 | -41.13348 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d61e7cec-a1ba-3043-b03d-b3534c3de6ba | -3.04413 | -50.28123 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d385520f-f345-3118-86e9-4e7fd37bbec6 | -3.60657 | -50.62326 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61a5f579-4f8e-3d7f-a1fe-2a3209e1fd1b | -6.2693 | -42.56441 | 2025-11-04 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a005313b-ed7b-3332-831a-83481af2d785 | -4.02861 | -45.46818 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f13fc62a-1570-3974-8d21-a214a227a264 | -7.17787 | -41.95558 | 2025-11-04 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22034c2e-f249-3a53-bf2a-532955ef0002 | -5.77916 | -40.80927 | 2025-11-04 04:10:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f116a8c8-33d3-3214-a901-dfa634377caf | -6.41238 | -43.06847 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3fca7712-1d24-3a38-8c12-0728e2019752 | -3.91598 | -47.68769 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 375b3120-d827-314d-a3be-fb7b02ad52e5 | -6.13016 | -41.54045 | 2025-11-04 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b6aac3f-c3af-3487-a4d5-5efc4c028444 | -6.40502 | -43.07103 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7745d5c-b040-3d4b-b137-fd7075d10248 | -3.28956 | -50.20109 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57a0e35d-6eba-396a-ae34-5f7e1521d278 | -2.37071 | -47.71806 | 2025-11-04 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7bee5b2-fa7f-3a19-ac46-4618c99ba50f | -3.49955 | -50.45649 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77d9231d-44d3-3256-8129-f3b6b40527b3 | -5.84024 | -43.45179 | 2025-11-04 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c38d85ff-7489-377b-a42d-537a46e0d5a3 | -5.62347 | -41.08747 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41b3c3c0-8b85-33ba-8e44-5448598d8d95 | -3.97071 | -41.82173 | 2025-11-04 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f003d562-246e-309e-8f9b-bbf44c268c4d | -3.57429 | -50.64474 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2240ab62-cbdf-30d6-9786-8c0799d77037 | -3.77475 | -52.32678 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05dbef74-95d8-32d4-9a34-eb645297de8b | -2.30923 | -48.59855 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62ddf759-2cc1-315c-b35c-ab02467faef8 | -5.5225 | -41.08589 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f96ed4cc-bffc-3caa-a637-d15538d12d99 | -6.26595 | -42.56387 | 2025-11-04 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7250873f-f20c-36f2-a6e5-d206d14c2e7b | -4.3137 | -41.45165 | 2025-11-04 04:10:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5cae926b-cf70-339c-ad89-dbf8baae023e | -3.38818 | -50.28181 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 695ab22d-d53b-34ea-996d-173405fe411e | -6.12483 | -41.68161 | 2025-11-04 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b17c8d6c-36c1-33a6-9999-49fb52762ff2 | -4.88851 | -45.86174 | 2025-11-04 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33aed792-2d64-3a00-a213-7dc79337118f | -2.37536 | -47.71884 | 2025-11-04 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 68529d45-7209-39a5-8190-1013cfb020ea | -3.44008 | -50.24036 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cc949a12-b33d-350f-8b53-30e61f96b3c8 | -4.02551 | -45.46263 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d6f9cfa2-dce0-3c3f-b8f2-7f10d7a910a9 | -3.56873 | -50.64373 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e97dee9b-3b69-3b14-a8f3-f43bb8f041b5 | -6.4152 | -43.07264 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c0628390-dca9-3071-9648-7b53bd8edcd1 | -4.32391 | -40.78721 | 2025-11-04 04:10:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b2c0e7bb-cba1-35d1-9034-9f1bc5ab5655 | -4.59841 | -45.58381 | 2025-11-04 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cb829fc-0ba1-343c-a97b-0d480288959b | -5.8315 | -44.66627 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d47f4248-2f3f-3f7d-9d77-77c6c05dc4bb | -6.50147 | -38.66453 | 2025-11-04 04:10:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78e1801f-20be-3641-851e-767f49807fe2 | -5.57103 | -42.2979 | 2025-11-04 04:10:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c5b208b1-2d17-3fb7-97b9-c7c66151cb84 | -5.52922 | -41.1295 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 62e711ce-7c2a-3f08-b94a-e04910f05b99 | -5.92721 | -41.33073 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7d8644de-5cd9-3f8c-8e7b-794e1ea96974 | -2.19931 | -48.35736 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c2f8e23-25e3-3013-ba1f-496dace6a048 | -2.87558 | -45.29867 | 2025-11-04 04:10:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5e030dcc-b2ed-359b-a302-1e7369953ce1 | -3.43524 | -50.23596 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c9bcec81-d120-31df-b35b-be3ae861ac35 | -5.23708 | -44.21104 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da328936-f2bc-3b03-b8c6-b3fc8113ae1f | -6.13348 | -41.54097 | 2025-11-04 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84bb074e-0aad-3a32-ac83-97fecc655ca0 | -4.96314 | -44.90453 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1a2fae2-dde7-3353-b228-46e5406a8f28 | -4.02941 | -45.46328 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cdf08b6e-ebc5-34fd-969e-7bc81806a8bd | -6.13625 | -41.54497 | 2025-11-04 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9928acf-1ec8-3ccd-bf67-3f0531f014b5 | -6.41355 | -43.0612 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf340744-7546-3486-86f9-2a922514b32e | -5.75256 | -43.39165 | 2025-11-04 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cb8af11-3307-396b-9219-74632e222ade | -3.44419 | -53.25684 | 2025-11-04 04:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7660db48-c3f4-33db-99c9-718516efb826 | -7.29711 | -39.3514 | 2025-11-04 04:10:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e95c2268-ef0d-3e32-8489-7ef071eda1ad | -6.42314 | -43.06647 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d810491-d7f4-3c05-9d36-8c93449782e7 | -6.09813 | -41.70532 | 2025-11-04 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c7fd0eb5-0f6b-3d7d-a32f-b119868633fa | -3.61405 | -40.37447 | 2025-11-04 04:10:00 | NPP-375D | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 00a88b6c-3161-3c62-8cf1-97fe2bab9098 | -6.50051 | -42.06474 | 2025-11-04 04:10:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 885e1cdd-c719-37e1-80ae-44db905b5b52 | -6.35946 | -46.14638 | 2025-11-04 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eae2a56d-0b43-3ca0-8d91-eeb5f2b1d886 | -2.63443 | -54.58049 | 2025-11-04 04:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbdc1a0c-edfc-33df-92a3-3e7da19b4225 | -6.26539 | -42.56741 | 2025-11-04 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8121555f-34be-358a-a20b-712d0bc6ee59 | -2.31914 | -48.60013 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef7d2c5b-8564-37c2-af9e-d20fe1fc0ff0 | -5.03761 | -44.01519 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 177fe9c0-8dca-3e12-95d9-a43b03b04726 | -6.20984 | -43.70318 | 2025-11-04 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cb33e09-c1a5-30d5-9439-b0e5f6a158f6 | -4.42968 | -45.56232 | 2025-11-04 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac85b458-a5f3-35b4-9ada-fd1965420446 | -5.61078 | -41.10321 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 43a1485f-aaca-321b-851e-b5503bffddb2 | -6.34607 | -45.84284 | 2025-11-04 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 142b8a34-f113-302f-af7f-97db8dab0c12 | -4.33823 | -45.51063 | 2025-11-04 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aa10095-acd4-3b7c-b442-f9d7549d0666 | -2.36991 | -47.72297 | 2025-11-04 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5944bfa7-b2a8-3c64-9385-ed789a676d91 | -5.2261 | -38.59837 | 2025-11-04 04:10:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 29d287a9-0762-3995-b4d0-26a400db7031 | -3.18205 | -43.39289 | 2025-11-04 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 040fbb46-30d0-37b7-9b83-1a3140d38610 | -2.61816 | -49.23009 | 2025-11-04 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9119c6b2-569e-3701-bf1b-6ce537bf664a | -4.47162 | -43.2313 | 2025-11-04 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9259ebca-c014-3d8d-a1d8-c75f99e53d00 | -4.9527 | -44.89822 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abf4f6ca-488a-3ba3-a25c-1828d8ad2e28 | -6.60856 | -43.76205 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89053549-e4fd-3e0c-99c4-55f36e92b4dc | -6.2409 | -42.08486 | 2025-11-04 04:10:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 03443abe-1b20-32e9-be8d-88c336cce82d | -6.3036 | -42.87746 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65f2c245-ffc0-3463-b621-0f1ca13ca04a | -6.24367 | -42.08888 | 2025-11-04 04:10:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c092850-b89b-35d2-95f8-a5c4cd330810 | -4.22651 | -41.76861 | 2025-11-04 04:10:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 53052272-250e-37c7-82b9-631fbaee63ca | -5.92494 | -41.30199 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 995bcbb7-4590-30c4-8dce-e129064df318 | -5.61911 | -45.97182 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 97264e3d-2e37-3d7d-9723-c35297cc1ff3 | -3.947 | -38.34082 | 2025-11-04 04:10:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9173572f-fe37-3d58-a0ee-3218a3184c73 | -5.61969 | -45.97556 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f8aaa41-27ec-35cd-b619-a2375a55e194 | -3.29016 | -50.19758 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2a3512b-849d-3301-ae3b-8723fba0de2d | -3.35068 | -50.23624 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d0c7e9a-1efa-3006-8ebe-28f623bf4440 | -6.14012 | -41.54202 | 2025-11-04 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa05389b-4bfa-3542-a0b5-6de4d055a1f2 | -2.37377 | -47.72862 | 2025-11-04 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6bb445dd-03db-367c-b0e1-2e13159456cb | -5.62292 | -41.09094 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6971293e-91ea-3ab3-a5c7-d2310d7eff68 | -5.03304 | -43.61586 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 75f206eb-59ae-3e9f-ac1f-ae0ee562fb52 | -3.89787 | -45.1131 | 2025-11-04 04:10:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90477c6c-52c2-3f4f-b728-cea96a785bd1 | -5.76322 | -43.92313 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc66c458-9f7a-3cbd-9614-c64a337245c1 | -5.53191 | -41.09091 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10b8ef2a-6ff0-37ff-8132-fbf4419691be | -5.75539 | -43.39595 | 2025-11-04 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea0570a4-0a91-30e7-9727-e7e472108dce | -2.87638 | -45.29372 | 2025-11-04 04:10:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README15.md)
