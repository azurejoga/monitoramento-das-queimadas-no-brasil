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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4153458a-a6ba-3b75-af3d-2c5913efb5fa | -9.27344 | -59.41343 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c3fb1cd5-2c02-3228-ab41-54578c8b9de3 | -14.21805 | -46.24683 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2efa7da2-605a-3b84-82df-da235ad77daf | -9.96116 | -57.71811 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 331a9d61-96a3-3241-abb6-8a70cc2323b8 | -12.12182 | -47.59742 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fa16a679-e81e-3bb3-b541-f79556512a6e | -14.20987 | -46.27006 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5d1cc25-9709-3c6c-a72e-cd63eae9ef36 | -15.1389 | -52.49152 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe091fe9-fba4-344c-b804-02d670a504e5 | -12.81387 | -47.99158 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c678e06-2ec3-3f5e-a360-a43c5c9a9b2e | -16.23036 | -51.27408 | 2025-09-13 04:59:00 | NOAA-21 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d6764b7-af33-3532-b363-fa28cb24485d | -14.21503 | -46.27396 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e589ded8-527d-300b-bfba-ba2d278a00c6 | -14.22484 | -46.2864 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 029eb47d-a670-364f-86e8-3241e7ab3942 | -15.695 | -50.58441 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ab94643-6981-3e0b-9783-3f636e3e5d20 | -12.06665 | -47.62122 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a7988a4-c32f-3608-b2f0-14f1392448d3 | -14.29289 | -46.08398 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 2f363b44-bf2b-3bb3-b002-2721d0978642 | -15.29053 | -53.77625 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da21d150-1ad4-326e-9245-d38a60ba71ac | -14.19616 | -46.24414 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a4a04764-be99-3b9a-936f-ea1020372805 | -11.73131 | -46.58614 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17c82514-d2f2-3ad2-a79e-2084677cfff1 | -13.13604 | -47.12852 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a40360c-3dbb-34e2-af9b-69576fd18fe1 | -10.5101 | -51.5445 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40dbf86d-ad2f-3dd3-b717-3ce3094d4775 | -14.21849 | -46.29306 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7f7c4043-3791-35ac-9d0f-679193578298 | -12.8794 | -62.11266 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb984182-4490-3496-a818-f91a50a3d531 | -14.17824 | -46.25344 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e7135a2-9428-3a59-afc3-b7fd61dd924d | -10.4142 | -50.62301 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa005e01-3e0a-3cdc-9d44-8c774869f22b | -11.155 | -50.71008 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d94dc693-437e-3a20-ace7-abb90b3a9df1 | -13.26624 | -51.70922 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fefd2a7b-21ba-3009-8d1c-1469c6289a9b | -14.29506 | -46.06506 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26f82e80-198d-35c8-b068-d56320b3a70a | -15.55488 | -54.79456 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a744889-489b-382f-a696-d4ac07db0ef5 | -15.11399 | -52.50651 | 2025-09-13 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1813f40b-52d4-38f8-a99d-bc8d1f6a916d | -11.41539 | -50.73774 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 627d409e-824a-3b98-bfaf-0a64ed6e4b82 | -12.94375 | -48.00596 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2ca7dc89-2876-3c17-ace4-8fe264b93a87 | -15.119 | -52.49786 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08e06af4-4d8c-3c1b-b8f2-6c72dc10d26e | -11.42812 | -45.60825 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 37408aad-5b0c-3332-bb15-4423afe955b8 | -12.11441 | -44.85384 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a1e8955-d449-3c34-aeeb-2fe71b3fca02 | -16.40858 | -49.03914 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e826523-ae51-3fe5-bf99-ea072454bb64 | -14.2843 | -46.05968 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff9ff317-c576-376a-8b58-7170f2764b3c | -11.85442 | -50.56975 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f78c7c66-ac4c-3950-8a49-2970e1f3460f | -11.86339 | -50.56384 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 00e07259-0fe1-36a9-b548-1d1acb19e9fb | -13.26243 | -51.70871 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f72c485-0491-3814-acb1-6bdffe31e0c2 | -14.19105 | -46.23981 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2acd25d5-f1f1-3e65-b1f0-85394e4e6274 | -15.81551 | -52.21526 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94725451-b269-3e16-aa51-ea645457a444 | -12.92555 | -54.77061 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6946b5ea-d7f8-3b70-a884-0186faa10f99 | -11.18104 | -55.08464 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b61ea39-7fbb-3a7e-9163-92d87ffa6fb5 | -14.54887 | -53.27587 | 2025-09-13 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4b88188-4f9d-3a86-939d-9aadebc45dbf | -15.08028 | -52.44821 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ec0ee1e-e5fd-3785-8f2d-fe02ec518fd0 | -14.21436 | -46.27988 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d159970f-72f6-38a2-aaf5-663998622ef5 | -10.69144 | -48.65864 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f3c077f-1b39-365a-a6d3-a0463eb2d219 | -13.40432 | -46.79838 | 2025-09-13 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cb74483-ec55-3636-b1a2-da8488911fa5 | -14.71629 | -55.63939 | 2025-09-13 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7a0138b-f41d-34af-b0b6-cec45cb5c8cd | -10.76546 | -50.52015 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf41fb42-e2e5-3d66-b28f-817805a86bea | -16.29918 | -50.03809 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50c2d1f8-49f8-3727-9dd6-00c867dbef21 | -10.40705 | -50.58758 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2602e8e6-b654-3016-8c47-13f589be6c33 | -15.69605 | -50.57632 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44f48d88-33f0-35a4-b11b-92a2a7d761cf | -14.22102 | -46.27047 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a5a945a-607a-354c-bf84-a89ca7eb6994 | -9.50056 | -55.96801 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 19b6c078-05da-392b-8e7f-0828b493a28b | -11.8384 | -50.55375 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe531bbd-d91e-3f2d-906f-f3f28b7cdd70 | -11.3194 | -50.79416 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef838f51-204d-3dc2-8994-9bf8717e6b32 | -14.75157 | -45.26449 | 2025-09-13 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8760ea51-c11a-3a85-a714-bee83b9e7670 | -11.8363 | -50.55263 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba70b40b-1d56-3b53-93f7-55f837612379 | -12.1071 | -47.59524 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 10a3e8bf-34b4-3ba7-a37e-2d42d17e574d | -11.60926 | -52.22428 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb084185-d8b8-3b28-88b1-b0bc4b57ad9f | -16.4124 | -49.24253 | 2025-09-13 04:59:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c3a3f4c1-02ae-3549-aea2-22c8de74d000 | -13.14337 | -47.13313 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2411b94f-d932-3ac7-a723-09067f9922f2 | -11.61288 | -52.22482 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 727b9f3e-3671-342d-a007-c444b9e7154a | -15.07503 | -52.48629 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f105eb45-e518-30eb-b9aa-80b5aad028af | -11.88197 | -50.57739 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e616efbb-55c7-3ce5-98c0-f15680304f95 | -11.7787 | -47.3955 | 2025-09-13 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5768d2a2-ab3f-3e90-98c1-2f0189db7ad1 | -12.87757 | -62.14742 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92d98ae1-5272-381d-ad22-db4c05f6479f | -11.09235 | -51.97014 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 170e8c15-49c4-3f04-a02a-4ce8cf395fa7 | -11.13679 | -50.69701 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 058ffec9-5801-3446-9097-2dc4a61882c5 | -14.21292 | -46.24251 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea9c09a4-eceb-34b0-99e9-39625530355b | -12.85706 | -52.97554 | 2025-09-13 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e3d7837-7adb-3e8c-8846-efcd1fcb8a12 | -10.76868 | -50.52588 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 396d2127-5da4-33f1-a831-c903a56ae9f9 | -13.23118 | -51.7381 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e938d98-61b0-3df3-ba2f-c5b7350d1f6a | -13.17552 | -47.27687 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5536c121-6837-3688-bd72-2e8ddbbac764 | -15.77977 | -52.24887 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f7c027e0-df54-35c8-aa96-2d9e83eae374 | -12.00411 | -47.76358 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 2db2c5e4-dc3e-362e-ba3a-309c8f95b8f4 | -12.09385 | -44.87592 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c510a6a-8b1b-36ca-b686-bb721afaf12e | -10.79462 | -50.53709 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dce170b6-798b-33bd-a06d-1b5a6cec7f26 | -13.45708 | -51.78108 | 2025-09-13 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b34db6e-dc53-3d89-9703-592b57749688 | -12.12771 | -44.84271 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 31fdf97b-565a-34aa-aa23-ddb7dd78ba97 | -15.06328 | -48.01035 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7b4d6c4-ee6b-3535-9b8c-59729e4d8934 | -11.85202 | -50.58744 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0eca746a-d071-3e50-8092-3fb624af19ce | -11.86388 | -50.5603 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d37fcbcc-9918-31c5-ac3a-493173a67594 | -13.08677 | -48.26588 | 2025-09-13 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d5486733-6bb0-38cb-ae76-d3c9a7d0a522 | -14.46579 | -47.3451 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bd37561-6ada-37e6-a9ae-b59157939e4a | -14.1756 | -46.27614 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 2ab4bd39-46b9-3f92-bf70-a68331f7fcd9 | -10.69757 | -54.44923 | 2025-09-13 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 413eab6d-cefd-3c31-8e34-a3d3d44a77d8 | -9.37072 | -59.48254 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5993af1c-d67b-3a60-b8b7-7cf0ea16955f | -14.43583 | -48.4337 | 2025-09-13 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 356d9f7c-761c-3080-bb03-297cb6ad0d71 | -9.25776 | -57.07115 | 2025-09-13 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0171fcc6-65d1-3a83-a1c7-42f265a0c7f3 | -12.10899 | -44.89914 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 274d9f0e-e3b7-371b-bc7f-6242249d1b2c | -11.57809 | -50.57706 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7b969e37-f991-3744-a284-c6d11e667de8 | -10.53426 | -51.53446 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38aec9e1-6e50-391c-b476-2df71bafdc3c | -14.19154 | -46.28394 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2d8db86-28ca-3cf4-82d7-3c14bd8ab9bc | -10.54189 | -57.08668 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36b2f32f-f08a-3680-80c9-dfaf3ce2c711 | -9.80866 | -61.51119 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bad78e09-1558-3939-a372-7fa023726e39 | -9.26492 | -59.417 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5df16126-18f4-302f-9a88-c0fca8b7358b | -11.448 | -45.63073 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e82dee3-2cef-31b0-8502-65ada66f58ee | -12.80996 | -47.98936 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e89cc12-74fc-3a4f-b3bb-dbebdf172336 | -15.05651 | -47.98823 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9cc03d9-a01f-39e7-97f2-aad8cf7177f1 | -10.70324 | -48.65873 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README81.md)
