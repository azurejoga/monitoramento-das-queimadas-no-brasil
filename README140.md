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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc743fd5-00ff-3868-932c-86e792bf8acc | -14.82417 | -41.36452 | 2024-10-25 16:50:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1619d505-af84-36a3-82fc-2ad4ed675c21 | -14.80115 | -41.66957 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| f50f5ae9-2e00-3396-ab05-843e6084cd23 | -14.79668 | -41.67049 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 53298278-2444-3f59-9796-e4913bb7279e | -14.79598 | -41.36573 | 2024-10-25 16:50:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ecc3f878-abd4-356d-832f-9570524e7073 | -14.75059 | -41.40135 | 2024-10-25 16:50:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 38861465-bf6d-370b-8357-337dc860e800 | -14.71355 | -41.70874 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e5184d3b-9e65-3d97-bf46-f18df2e16b3e | -14.70167 | -41.36673 | 2024-10-25 16:50:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| fdf27cb8-81fb-367b-a679-ea462a943b28 | -14.64504 | -41.4437 | 2024-10-25 16:50:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a9fc9404-3800-39cd-a3c0-2774e59a7112 | -14.57463 | -41.73343 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 833d7cff-6753-3834-8823-3e0660130932 | -14.5716 | -41.73101 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 69f340c3-3b95-3047-9761-2c8f0af78ce1 | -14.53938 | -41.76873 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4e0ea135-3f2d-39f5-adba-472aa2ee88c9 | -14.53488 | -41.76946 | 2024-10-25 16:50:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b5b57c0e-da63-3689-96ec-02c764359371 | -14.50454 | -41.32785 | 2024-10-25 16:50:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 73339969-af99-355f-835f-e61bbcb3123e | -14.46332 | -40.82888 | 2024-10-25 16:50:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ccaf3d2a-91e8-3626-a7b6-bb65cb2116da | -14.45696 | -41.57633 | 2024-10-25 16:50:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 70575ba3-4978-3c19-8588-0ab8d05e0564 | -14.38774 | -41.40843 | 2024-10-25 16:50:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| afa999a3-f026-348b-a76a-e321960d8e35 | -14.36526 | -41.19325 | 2024-10-25 16:50:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 89d53021-c470-34ff-b3d3-ffc7a8a349b9 | -14.36297 | -41.19531 | 2024-10-25 16:50:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 49db5bef-70e1-39b6-92f8-1aaae60679d6 | -14.36024 | -41.56635 | 2024-10-25 16:50:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 21b0b522-7750-30c4-8e31-81eee355c4aa | -14.25091 | -40.96012 | 2024-10-25 16:50:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 815e8679-6174-34c6-9d27-9290946dd070 | -14.17354 | -41.50401 | 2024-10-25 16:50:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 117970e6-b94f-3afe-be4d-60de5fe7687c | -13.88195 | -41.71883 | 2024-10-25 16:50:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 949e4bd3-1260-38c2-a00c-e92c5c9e91c6 | -15.11018 | -41.12003 | 2024-10-25 16:50:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| d25c7cc3-53f9-3fda-a5ed-a5c075a39df3 | -15.10835 | -41.11755 | 2024-10-25 16:50:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ab3e3d83-a64a-3ad6-9ab7-f01193b0c35f | -15.10448 | -41.09748 | 2024-10-25 16:50:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| fd11905f-ddae-3257-9a04-1fb9191c96c8 | -15.09903 | -41.21428 | 2024-10-25 16:50:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 6f1b7b6e-e200-32c1-b274-e74d0e7927c5 | -15.03965 | -41.30215 | 2024-10-25 16:50:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 95a7f99e-2294-3e92-9ddc-f88d23c42148 | -15.03914 | -41.29928 | 2024-10-25 16:50:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| b948579f-4c44-39fb-8d40-d4af20a7528b | -15.03875 | -41.29744 | 2024-10-25 16:50:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| afe71c06-2338-3105-ad66-9cf1ebc3b697 | -14.97107 | -41.29004 | 2024-10-25 16:50:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| daa241fd-3fdd-336b-93f1-45b1515c1a8b | -14.96956 | -41.15504 | 2024-10-25 16:50:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 58ab7514-8d84-3b39-a085-134fbec69537 | -14.93655 | -41.03044 | 2024-10-25 16:50:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| a54688ed-6928-3f40-a0f1-69be8e59e7a3 | -14.9344 | -41.29696 | 2024-10-25 16:50:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d10ac73d-194e-3f03-b879-06ec40344a65 | -14.9344 | -41.29483 | 2024-10-25 16:50:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 097eb1b1-533c-3ef4-b96b-82c7bbc74dc9 | -14.93186 | -41.03122 | 2024-10-25 16:50:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 2f7d9cc7-5056-3ff6-916b-b2d5792455b3 | -14.48981 | -40.99519 | 2024-10-25 16:50:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| c7d5733c-af36-3cd1-a547-b3ce5862cd5c | -15.96775 | -42.2211 | 2024-10-25 16:50:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 806ee123-dc4c-3f62-9de7-fe8b577971aa | -15.41674 | -40.89605 | 2024-10-25 16:50:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c7e2e67c-7754-3b71-ae75-91f1be996332 | -15.25009 | -41.36597 | 2024-10-25 16:50:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| b75b706c-5ec9-3fc4-bdf4-244a9b06eb80 | -15.24193 | -41.37264 | 2024-10-25 16:50:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2fcca1cf-49a2-3134-bb0d-0cdd721e3c0d | -11.56033 | -41.8615 | 2024-10-25 16:50:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 861a138e-b547-35b0-893c-4fd80071e2db | -8.78079 | -42.17366 | 2024-10-25 16:50:00 | NOAA-21 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 98983f33-d96b-366b-b40e-cff62133b4e8 | -8.77644 | -42.17171 | 2024-10-25 16:50:00 | NOAA-21 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| c1cef523-bcf4-381c-a9a1-4bf73e4a83aa | -8.77503 | -42.16933 | 2024-10-25 16:50:00 | NOAA-21 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| b88f8198-ba96-32c6-9a75-ad7a8f7775f7 | -9.17572 | -41.41778 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1019b74d-3c07-3b61-99fd-826ead6ce52a | -8.98192 | -41.23207 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d835beef-45d0-3795-a425-71061813085d | -8.88162 | -41.45035 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a18d6694-ecb1-3b5b-b672-e8141d062456 | -8.88107 | -41.44732 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 8fb107f1-7fc1-3685-90f1-b5127108056d | -8.8776 | -41.44998 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ab38efb1-10f1-33fe-8582-c05eab50ce3b | -8.8555 | -41.39328 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 354770ac-52b3-3148-a82c-5f1a96bbea3e | -8.8519 | -41.39277 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ee804577-01a3-3143-becc-5039d378fa0b | -8.79122 | -41.04421 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a3052736-b8bc-3a85-a510-526dc4c80491 | -8.79012 | -41.04268 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 52199747-f3e2-3bfc-9f38-a761e30dab3d | -8.77877 | -41.62208 | 2024-10-25 16:50:00 | NOAA-21 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 61973027-f98e-3ea0-a3ee-55a01cc44c0b | -8.75488 | -41.05566 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f7255cd3-9464-31b3-92c4-8f722fb6d08c | -8.75483 | -41.32009 | 2024-10-25 16:50:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 0bc0ff05-42ac-3421-8438-960beb1da53d | -8.57649 | -40.99565 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d9dd45f0-fbe3-394f-96c1-3c3741c2dad6 | -8.56982 | -41.14098 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5458d42a-806f-3b8a-af30-8410640f527e | -8.55551 | -41.4944 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 42f123bd-bdaf-3217-b236-18f0f0be2b9d | -8.555 | -41.49143 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| da98c55f-1f50-37eb-9a37-3915624a573d | -8.55432 | -41.14405 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 25.8 |
| db34753f-28e7-3f34-b5c8-7e24f36d2fca | -8.55377 | -41.49249 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 4c5966c8-349c-3bc6-a2d0-0f0399ea402a | -8.55374 | -41.14083 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 25.8 |
| edef195f-7a63-381a-86c5-eb818404bbd0 | -8.54915 | -41.14506 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 65e1f056-0731-3a01-be86-b0727c086510 | -8.54857 | -41.14186 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 17b30571-f5ec-3fb8-91cb-9c409f183f60 | -8.52803 | -41.42713 | 2024-10-25 16:50:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d9d60d1d-f442-3a3c-ac50-cc7ab8aa2377 | -8.52164 | -41.28751 | 2024-10-25 16:50:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 1d3c9626-ad07-30d1-bf8a-c3771d5ba3c7 | -8.51925 | -41.28677 | 2024-10-25 16:50:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 50953d13-2f84-367b-ab3a-2add7b648935 | -8.51432 | -41.3791 | 2024-10-25 16:50:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1f481c75-407e-3d22-91e1-5dda4b216426 | -8.44168 | -40.90661 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| cc0d62a2-3150-3f2a-b225-fbae0574263e | -8.4407 | -40.90514 | 2024-10-25 16:50:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 593ce51d-46e4-3300-95f2-44f11070f722 | -9.94928 | -42.47165 | 2024-10-25 16:50:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ab7be63f-951b-38ff-a7ec-497f6c8e61f6 | -10.29064 | -41.8473 | 2024-10-25 16:50:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 532c9322-afdc-3cdc-a994-7ba5d4a9ba32 | -10.28478 | -42.39204 | 2024-10-25 16:50:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| dc6e2779-6fd7-3abe-98ea-4eabfff2d69e | -10.20155 | -42.45449 | 2024-10-25 16:50:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 561834e5-9990-3313-af54-1ee0f457fcba | -10.16753 | -42.45069 | 2024-10-25 16:50:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a35f6934-dd60-3867-967f-f78e30019a1b | -10.16292 | -42.45153 | 2024-10-25 16:50:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a5fca8ff-c988-3cb7-a06c-0a9343bb3931 | -10.29749 | -42.40984 | 2024-10-25 16:50:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 81a4268d-61b1-3c16-b455-db293ea6c2fe | -10.29662 | -42.40497 | 2024-10-25 16:50:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| d20fb51c-223a-3bef-b7ff-61807d1fb3d2 | -10.29576 | -42.4001 | 2024-10-25 16:50:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| c4d8daa3-4143-3954-ace0-47d72346dfbe | -10.29489 | -42.39523 | 2024-10-25 16:50:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 31.5 |
| f68a4b6d-3465-34dc-8c0d-8667af43e8a6 | -10.29114 | -42.40094 | 2024-10-25 16:50:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 7da55ebe-66bf-3442-bfa2-d00bb9e0179f | -12.21718 | -42.26177 | 2024-10-25 16:50:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 52422bc4-7287-369c-b048-d09a5423fc26 | -12.2163 | -42.25693 | 2024-10-25 16:50:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 7e38a462-2e74-3274-b23b-a20acb2cf396 | -12.21183 | -42.258 | 2024-10-25 16:50:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| a272ba2c-a3ee-3f9e-b2f9-e450b0adbcda | -12.14579 | -42.26255 | 2024-10-25 16:50:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| c152fa68-8e5b-3b28-b445-46be3d84232f | -11.56269 | -41.86372 | 2024-10-25 16:50:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e249fd44-270e-3585-b748-610671800e5d | -11.41411 | -42.02886 | 2024-10-25 16:50:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 1a410a87-db30-3de2-9f29-5937a39eb7ee | -12.05682 | -42.90439 | 2024-10-25 16:50:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 75359ece-9bd7-3545-a41a-d62d8d718bec | -12.0553 | -42.90385 | 2024-10-25 16:50:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 4f6decf2-5656-3887-85bf-81e4c9624649 | -11.93939 | -42.86209 | 2024-10-25 16:50:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7c1b74d4-1d49-3fa6-8133-01dc394dfdcb | -11.80683 | -43.08208 | 2024-10-25 16:50:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 78505194-d8b5-3ad1-8be9-59a97241d690 | -11.80253 | -43.08288 | 2024-10-25 16:50:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 2c3241cf-7050-3dbe-9c81-9d4b2c5e0ae5 | -11.7353 | -43.14167 | 2024-10-25 16:50:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 431db601-f539-3727-a795-c05fe4036739 | -11.73398 | -42.52103 | 2024-10-25 16:50:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 2343ddf1-244f-3632-9713-2213cad31e94 | -11.59914 | -42.75734 | 2024-10-25 16:50:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 540efb9e-9a36-371e-9c8c-9f95a7867717 | -11.5948 | -42.75606 | 2024-10-25 16:50:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| d7da2de1-02c0-39c0-9b19-9978d8209c5b | -11.59473 | -42.75816 | 2024-10-25 16:50:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f9ebabc1-65b4-3459-92ad-7f3141976f40 | -11.46436 | -42.68315 | 2024-10-25 16:50:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 89b83431-7209-3556-bbb7-342be497d80f | -10.78983 | -42.81508 | 2024-10-25 16:50:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README141.md)
