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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bc615f2-5e0b-3ee2-bce5-98425e7f4384 | -4.94928 | -44.96238 | 2025-10-17 03:28:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83f3a469-e352-319a-8566-23fc632974ad | -7.03593 | -42.73532 | 2025-10-17 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b7c7826b-a037-37a9-b4cb-c11f74260f3e | -6.23267 | -41.54414 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a7cc1dd-d55c-3774-ac13-bf0d9e6c5a20 | -8.21414 | -43.98372 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 076d7db8-5f46-3ef7-be60-69335f183ba4 | -8.39845 | -46.22575 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9dd0fe9a-5282-3a9c-b5e5-2e57763b5e07 | -8.30363 | -43.41887 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b18836ed-87fc-3612-aa6a-619ffb10a865 | -8.45118 | -41.26562 | 2025-10-17 03:28:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31e9d492-36c9-31cc-b622-ca877bfa0b6e | -3.59174 | -42.84385 | 2025-10-17 03:28:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e2d8b8d-1a18-39f9-b2c7-dc6c8e714378 | -8.11756 | -45.54302 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66d1920a-c04b-3664-8b55-dd6643b42063 | -9.03902 | -40.58035 | 2025-10-17 03:28:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b30186c9-8fc7-305b-8d0e-e3dfe39d58c4 | -4.36273 | -44.7837 | 2025-10-17 03:28:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72f654d5-34cd-3648-9304-378f2db12943 | -4.37729 | -43.38942 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75b1d9c3-4837-3970-88c5-3ba07fd1a322 | -6.74641 | -42.38257 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd8d1c65-a04f-3c27-93ac-6b943eadba4f | -8.18804 | -42.35688 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6801ed86-a502-36ed-afc1-9612e244713e | -6.0432 | -39.68909 | 2025-10-17 03:28:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e03309ce-7ea3-35e1-8203-166e3a8a1459 | -8.30461 | -43.43886 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee92a20f-67c0-3f6a-921f-ddad5d9867b6 | -7.46814 | -42.65521 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f6538a7f-1804-3f7a-b5b3-1d41dc570355 | -8.48269 | -40.6053 | 2025-10-17 03:28:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d1e2448-9d32-3571-a4de-e85d841e53aa | -7.10596 | -44.74606 | 2025-10-17 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2175424e-ced2-31dd-a082-6103f1dfb2ca | -7.45726 | -42.15009 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 522c1a17-621c-3a35-87ed-28995522fd11 | -6.2637 | -43.90343 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2fe8a658-c4e6-3a71-9ee1-81ca2db85d55 | -5.87845 | -42.82256 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b2044b28-ac4e-3aee-a43f-20185e93f787 | -7.1775 | -42.37786 | 2025-10-17 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 86ab5598-10cc-3867-991f-c75c118b7f49 | -7.28303 | -41.95227 | 2025-10-17 03:28:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e6c9fdd8-32cd-3c79-80a4-70126a9bf02d | -6.38171 | -41.47179 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 83bd4cc2-eb81-397b-b75f-ebb1a1ace48f | -7.7389 | -42.51217 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c62e8cc2-0e72-32cb-be74-89ddd833db77 | -7.83285 | -44.1434 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b11b3dd7-ef10-30c0-bd2d-a1a9eabfe878 | -7.32705 | -44.15986 | 2025-10-17 03:28:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8657f4b4-6da3-3562-a16b-7a9c550d168c | -8.401 | -46.23177 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3073eda-5327-3daa-96c6-db57a87a105c | -6.13189 | -41.75236 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2b9401ca-2b21-3562-9455-2d332326f9e8 | -4.4147 | -43.40215 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ba754cf7-c8d2-3600-b6e3-c31a832787ab | -6.25625 | -43.90792 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccb4da61-e4c7-3740-9678-54b9ee133b56 | -8.28288 | -43.38782 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b94a4d47-a308-3273-b0e2-428275a416ef | -6.32921 | -44.31855 | 2025-10-17 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7302c07b-acf9-31be-803b-f918a363beaa | -7.95159 | -44.1513 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ba355c-4608-3340-bc9c-36d0c4f3211b | -5.25056 | -44.2097 | 2025-10-17 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c181d291-1a20-32fc-b2da-fa79a42fd101 | -5.84701 | -43.88078 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d91d977-ff6b-38e2-8d76-ce9051296872 | -7.9519 | -44.12785 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 727d36db-09e8-3295-a313-08582956ef65 | -8.38167 | -46.32781 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bd4b2da-91ef-303f-acbb-aee1d1a80d9a | -8.45031 | -44.17822 | 2025-10-17 03:28:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 115155d2-e511-386e-ab90-cefc25361229 | -6.34445 | -41.52192 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d51b8f47-c086-3d9d-a406-c91e7436ffc2 | -7.663 | -42.56934 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| be211789-0b29-3750-b3ae-a64b86d0fb23 | -7.4636 | -42.14721 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 22369664-6180-33e9-b8c3-c9dc6ab29932 | -5.86806 | -41.23233 | 2025-10-17 03:28:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| edb8f4eb-17d6-334c-a4c1-0493271ae995 | -8.46283 | -44.18104 | 2025-10-17 03:28:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5e2a9385-994e-3a74-ac42-d0a30b8c5c5c | -6.68991 | -40.88135 | 2025-10-17 03:28:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5042cd41-5990-301b-8d9b-d84bf0c98cd1 | -6.20366 | -41.74015 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36dfb2b4-3e9a-3d4b-8325-e2e68dc95a4f | -8.39622 | -46.25557 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65275d8b-1db9-321d-a6c1-d0b6edbe6700 | -7.17402 | -42.36425 | 2025-10-17 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| af96a4c8-8b62-361e-8b00-eb3324760116 | -6.12903 | -41.76808 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cfcb4f4b-1fbc-3209-b855-aa977d34fb79 | -8.21376 | -43.31557 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c8665c9c-08e2-3ca5-bc85-7d0dd7421283 | -7.6688 | -42.57026 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1cbd6dfe-5d85-39a6-b2ee-db0f1945b80a | -7.17767 | -41.68357 | 2025-10-17 03:28:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cfcb67fe-2cff-3205-be79-4f947cdff4a9 | -5.29358 | -41.0843 | 2025-10-17 03:28:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b95ebad-cab4-37c7-8386-3966acb14636 | -7.27822 | -42.94014 | 2025-10-17 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4cef2258-c7f2-3858-96bb-c2bf14a9b1fc | -8.70723 | -36.23534 | 2025-10-17 03:28:00 | NOAA-20 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dfa81564-29b3-361e-8fd1-5dcf0f2f9358 | -4.40554 | -43.4167 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5dbc9cbb-4a93-3c7c-be46-1c6114c52f79 | -5.51312 | -43.8773 | 2025-10-17 03:28:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed1cac01-90a0-3062-bc8e-3d1d729921bf | -8.38908 | -46.25434 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4865eb74-83ea-30b4-af25-58fc7e99bf77 | -3.97462 | -42.49491 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c0f3955e-5047-3623-a261-f8e028d6d017 | -7.11143 | -44.7354 | 2025-10-17 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf56e0d3-c711-3866-8e5f-87f93353fb0f | -6.94397 | -41.56153 | 2025-10-17 03:28:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2de20c24-d51b-3375-8965-4089a02a7a19 | -7.45931 | -42.1545 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d94a2289-53a1-3362-a4c3-512f48492a05 | -5.8802 | -43.91613 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71b5908a-9344-354c-8326-85f1926ca87d | -7.27741 | -42.94458 | 2025-10-17 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2fbfdaec-ebb3-3ad6-830d-75cde1706170 | -9.15383 | -41.05488 | 2025-10-17 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| a154433d-3df3-392c-939e-ec7097eb0107 | -4.40006 | -43.41022 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1639a74e-1921-33c9-9dcb-8fb995ca71bc | -7.68181 | -42.56442 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 08e416d1-4451-3f4b-ad5d-061eb4dad7e7 | -7.05708 | -45.05643 | 2025-10-17 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e6d007b-a5fa-390e-9ed5-20590b39613e | -5.25612 | -44.21671 | 2025-10-17 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 051ed57e-7765-3a79-8763-4ff7f7b6d950 | -6.26268 | -43.90909 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b1001b7-7211-3bcd-9033-38c3ce00c4b1 | -8.32963 | -46.23836 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3e7ba229-9d62-3ca2-9b49-725c0df5c240 | -6.69689 | -40.87247 | 2025-10-17 03:28:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c663676b-e23c-38c7-bce7-5b6685df5644 | -6.43948 | -43.38327 | 2025-10-17 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 677d12dd-cd5f-3d69-9ab4-7b7bfbb4f5c3 | -7.45858 | -42.15841 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8769b0d3-52c4-3ba5-88c3-0b53dfa780a2 | -6.75461 | -42.37017 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cd348e9f-7e1f-32d4-a677-f8bcde2f6daa | -7.27679 | -41.95491 | 2025-10-17 03:28:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a58fb6c8-14f0-3fe6-9b98-f9b17724e0be | -6.32068 | -44.31762 | 2025-10-17 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21f1ee00-ff1b-3dab-afcb-db9ce5488f37 | -3.62358 | -42.77248 | 2025-10-17 03:28:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be36067b-8943-36c5-a1db-34469b1be7c9 | -8.59929 | -44.93874 | 2025-10-17 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d80e5e11-245b-3dbd-8cee-6ccd68708722 | -3.9738 | -42.49959 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2c1c7acf-6bfc-37ed-8a46-762f14ba7082 | -7.46003 | -42.15061 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 675993c8-a8c9-3733-be69-62faacce9b5e | -6.43853 | -43.38851 | 2025-10-17 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59a46e76-c345-34eb-a98d-da38922da933 | -3.23382 | -42.07515 | 2025-10-17 03:28:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad756667-863a-3e66-8278-b0cc60b869dc | -5.83274 | -40.81765 | 2025-10-17 03:28:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 644b29c5-795d-36e0-91e6-2d79c5de2085 | -4.95473 | -44.96307 | 2025-10-17 03:28:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d411eff-e484-3c6b-b62b-08618822436e | -6.13318 | -41.7453 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f17c88f9-1068-371f-a0eb-f0832a17331a | -6.13101 | -41.73954 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1bb55ff8-bcc0-322d-84d6-6fc4ef1b7303 | -5.35689 | -44.82356 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4322880a-76b8-3649-97b9-ee5823d02a4a | -8.72768 | -43.88215 | 2025-10-17 03:28:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b7c63b06-233c-3758-8f96-a59c8cc08152 | -5.29947 | -35.97884 | 2025-10-17 03:28:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3c7e23be-03b9-3d49-a4a5-3eafae736e08 | -7.57576 | -43.82967 | 2025-10-17 03:28:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 696f71b4-0115-3aff-9429-7d17bc65ece6 | -8.35448 | -40.33776 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4f51fd9-677a-328b-9b41-36c607ce09c1 | -6.94338 | -41.56491 | 2025-10-17 03:28:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a834e15e-ae08-3d50-8310-c92042dfee87 | -6.01533 | -41.93063 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df75789c-8d70-3fb2-a9e7-23848ac5c2c0 | -6.42735 | -44.7257 | 2025-10-17 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e8e93ff-221e-350e-812c-516538fdc771 | -5.33526 | -44.47955 | 2025-10-17 03:28:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d53dfd87-c63f-372e-ac96-8aff648d3c58 | -7.41326 | -44.76519 | 2025-10-17 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18ccecee-9436-3ac5-8356-bc01927b1d9f | -7.47425 | -42.74653 | 2025-10-17 03:28:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ecbf945-b5dd-3129-bf31-224091835f33 | -7.45852 | -42.6751 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README25.md)
