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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcfcc1e4-ab33-3a4b-b057-5f019de95e22 | -14.52864 | -43.79445 | 2026-10-02 15:52:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2909e7f6-61eb-3842-b27c-41c809c9d344 | -14.9217 | -41.15849 | 2026-10-02 15:52:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d0cfd4eb-bc7a-3896-8b6c-1af6bda3d307 | -13.80428 | -45.24675 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4d665a51-8b92-3848-b1bc-a6eac45bb6c5 | -15.98004 | -41.44094 | 2026-10-02 15:52:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 460955a1-e1e7-35ad-9c36-09a597d10288 | -15.08255 | -41.16004 | 2026-10-02 15:52:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| d8c2d00d-b4aa-3b9d-a5ef-03710630d179 | -13.99833 | -40.47599 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 061c3ae6-a017-3539-8d18-c4ddb5fdbfaf | -14.35936 | -44.72457 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e9d25076-8563-3164-b613-8e2e27ee5df4 | -13.39038 | -43.69443 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 08b9f3c2-7061-30cd-b63f-a9a077538f9a | -13.78033 | -45.2415 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b2de7ff9-aa5d-3294-85cf-12f90afff90c | -15.38709 | -40.83517 | 2026-10-02 15:52:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8485fb45-d87a-3ebd-8af6-10746b468b74 | -15.13504 | -43.59282 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ef6bbd88-f139-3e10-af7b-7e06de54ab8b | -13.84123 | -45.26297 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44d98cac-5fca-30e8-b9df-d135c7a8320d | -16.82779 | -43.56705 | 2026-10-02 15:52:00 | NOAA-21 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06fe6c9b-31b5-3082-bcb4-c7046d705269 | -13.88263 | -43.65204 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 0aa10a50-8e43-3f81-9500-75816675376b | -16.37177 | -42.97239 | 2026-10-02 15:52:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8d72b45c-392b-3452-901e-1a8b3d281031 | -14.21114 | -41.92959 | 2026-10-02 15:52:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d77d69cd-9420-3e7a-be4f-81e2bcc8f150 | -15.04508 | -40.5123 | 2026-10-02 15:52:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 71e20fc7-8108-3328-a498-a8e09d1af491 | -15.75688 | -43.66494 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9f755a1-b61f-3a7c-800d-2af736762a46 | -14.70401 | -44.70007 | 2026-10-02 15:52:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 7cea53b2-f9f4-3aeb-a66b-e9e0041c0a9b | -15.17562 | -43.66941 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 46.3 |
| e2e105a6-db0c-332b-8c93-c8c6c637caf6 | -15.8705 | -42.51279 | 2026-10-02 15:52:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 927d86ab-c03e-3e21-9ed3-d7bb68758c32 | -13.79087 | -45.2317 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1f5dac5f-2e63-32e8-b075-76e5034b7033 | -14.07392 | -41.00687 | 2026-10-02 15:52:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ec25e038-6f34-30d7-996b-9b46f16b619d | -15.30595 | -41.42662 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| e05285e2-02a5-3e27-bb8f-3717c9d53651 | -18.12608 | -42.52776 | 2026-10-02 15:52:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fa53e796-b970-3697-ba88-f9eefcb90b06 | -14.69059 | -41.87741 | 2026-10-02 15:52:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cb255c24-6ab4-32c5-91d8-1ba44ab5d4f1 | -15.13425 | -43.58621 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.4 |
| ad7d9742-a6be-3d8e-8bb8-40f2fcaeb855 | -14.32484 | -41.32304 | 2026-10-02 15:52:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d6bee71c-2531-338d-a18d-2c3ea96f3435 | -14.2556 | -41.61628 | 2026-10-02 15:52:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 5ebd8523-0b1b-3a7e-b0e4-9496a07dd33e | -13.88225 | -43.64883 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 0333afe6-e5a9-3822-9aa5-2d0f1248a79e | -13.88707 | -43.64502 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 9ae961eb-9f5e-3604-9526-7bbc08d652fe | -14.49479 | -41.77119 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ea16e27e-11b1-3af6-93da-3ba943dc5988 | -17.15827 | -43.046 | 2026-10-02 15:52:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4998d707-91b3-3017-ae3c-6626629c4923 | -15.5766 | -44.55688 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| dc1ce832-3dce-32d6-a5fb-d6080a50c98f | -15.80486 | -40.25983 | 2026-10-02 15:52:00 | NOAA-21 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6bd4cdd6-730a-3e76-b0fb-5a444e45dbcb | -14.34855 | -44.72946 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4a60ccf9-7c97-3710-a6e0-adfc910e86a1 | -15.02892 | -40.98036 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 1a0462bc-36c6-3121-ab29-163fb494ccf1 | -13.40847 | -40.78143 | 2026-10-02 15:52:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 20d4c1e9-fa62-3006-8dc4-367f7d168d58 | -13.83208 | -45.23493 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fe12b7d5-8897-397a-9d6f-df18bfca1132 | -15.68675 | -41.3323 | 2026-10-02 15:52:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a48f4f4b-6f2a-391a-80b5-e196ca11e6a2 | -17.99747 | -43.6572 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f9f0feab-70ef-3470-939e-b3c1429e0d8d | -16.15232 | -43.63122 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d6bc417f-e6db-332b-8270-074bf29ab8ee | -17.84252 | -42.21666 | 2026-10-02 15:52:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 6082cdba-f1a7-3608-95f5-a8078d876f6e | -17.91547 | -43.61371 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4eeb48d4-1a20-38a6-940e-979d1baea7b5 | -15.30668 | -42.77752 | 2026-10-02 15:52:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| ac964195-85dd-347e-a2af-01f2d6a8b297 | -15.77742 | -43.65581 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8fec7036-18a0-3a80-8b29-d3cedde3b143 | -16.5312 | -41.90276 | 2026-10-02 15:52:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4dbc4558-203e-3f07-9846-98b6c7339e72 | -13.85053 | -45.23343 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be1dd5f6-552a-3a9d-96ca-d32aebe24d60 | -14.2667 | -42.11032 | 2026-10-02 15:52:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e5b4a944-cca5-3d0b-833a-6a7f961b492a | -15.23369 | -40.93426 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 406d2076-76b4-3102-8284-ddec8e3904c7 | -15.86714 | -44.2949 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 75055a40-3618-3242-84ff-c3642add0189 | -17.5259 | -43.74259 | 2026-10-02 15:52:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3f6f9a40-51e8-3029-a865-1467694ddd2a | -13.5522 | -43.52343 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ae475382-5960-3fbf-bc75-72ebbb6eea68 | -14.66258 | -41.61862 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6ef6089e-0902-3f47-8cfd-e9067f96abe8 | -15.86076 | -44.28794 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 34.2 |
| c3a3a03d-4f17-3b42-a9a5-2dd8ec8a8dc8 | -14.93737 | -45.47047 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c77a9d37-6e79-347b-a152-cbba98d72845 | -14.84442 | -41.15488 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8a078b89-7475-3f61-8d12-0ba64d3faa20 | -15.77525 | -43.64959 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 855df318-6340-38a4-981b-59c386dc2804 | -15.80651 | -43.085 | 2026-10-02 15:52:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6cae1982-b1d0-3b1b-a178-b5e19f043f9f | -14.36584 | -44.73149 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 008e1e2c-bcab-3c3b-b487-ab3c9d14b39e | -15.80162 | -39.86213 | 2026-10-02 15:52:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ee1f9002-b159-3302-8c13-847a3354a2eb | -15.53152 | -40.84562 | 2026-10-02 15:52:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 98e168eb-55a1-32e8-ae7b-fafb100ace67 | -14.95021 | -41.03098 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| c48093e9-3079-3103-9d18-f96c422fa4b0 | -16.76003 | -46.79724 | 2026-10-02 15:52:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39227d20-4877-36a8-9b1b-3ded0e62370e | -15.23391 | -40.93565 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| a4e3877a-90af-3e48-ab95-b7e7956e07b6 | -13.84477 | -45.23407 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ab32d0a1-a97d-393f-86d6-dc2a7661582c | -16.69456 | -41.06011 | 2026-10-02 15:52:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| 930f84f6-b9b2-35d8-b7ae-d1bd1bbae25e | -13.40423 | -40.78202 | 2026-10-02 15:52:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6d27c2a9-0a51-3750-a003-629792b24903 | -16.13263 | -43.74786 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6fd604b-631f-3b5c-8c20-d86e0d4e4994 | -15.87269 | -44.29425 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 306a0eee-6fbd-3a66-80b0-00a620228e36 | -13.81286 | -45.26245 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fdf771b5-2b07-3af0-b883-35632a7be123 | -15.9304 | -44.5126 | 2026-10-02 15:52:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| edcd7511-41be-3921-9ad4-9384417f4385 | -15.33447 | -41.7376 | 2026-10-02 15:52:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c982f005-5b27-3340-9c69-3ac46fbebec5 | -13.87633 | -40.97083 | 2026-10-02 15:52:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3c7d7f44-065e-3791-b09f-20ed517de4c4 | -18.5004 | -43.64958 | 2026-10-02 15:52:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26bc06a7-9f5c-337f-896a-7fca188ea28c | -13.50242 | -39.6032 | 2026-10-02 15:52:00 | NOAA-21 | TEOLÂNDIA | BAHIA | Brasil | 2931608 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| aec04718-0d07-321a-8a45-abbbf6616fd7 | -15.46332 | -39.10545 | 2026-10-02 15:52:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 09dc016e-31ca-3383-9645-cb422a55141c | -15.16957 | -43.6633 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.2 |
| bfdefcf3-4585-3263-b7a4-b62a2424ef3f | -15.02848 | -40.97622 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3f7f1840-8816-3514-bf91-828aad340a16 | -15.53091 | -39.65928 | 2026-10-02 15:52:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| ba121961-5466-3324-8a15-893866e18295 | -14.2614 | -40.3823 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ea251fb5-f13b-3f80-b825-8c240f6febdb | -17.48159 | -39.79677 | 2026-10-02 15:52:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 3b62ad6d-71a0-3746-badc-e76dbd0157db | -14.3286 | -40.59958 | 2026-10-02 15:52:00 | NOAA-21 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6e14b6ef-5718-3d03-851f-9c04e44757d1 | -15.77051 | -43.64275 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 907c3713-8c0a-35b5-8b32-75c53313a11e | -15.91416 | -46.01083 | 2026-10-02 15:52:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e871ecfd-908b-3fd3-98c2-6e42bf22d6a6 | -14.07234 | -40.55185 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 9b09f929-d744-3a91-8a7f-929bdd8de425 | -14.94105 | -41.34644 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 676d4986-03db-35c2-b1b6-25e197b87736 | -15.77624 | -43.64569 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8cd3cc34-c552-3538-968b-f9c638798a4d | -13.56747 | -40.67912 | 2026-10-02 15:52:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 4cab4203-1386-3f07-b9bb-bea5d06ac2e0 | -14.65882 | -41.7367 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 548b6cf1-1536-3261-9830-da24a1d255f3 | -16.14291 | -43.74222 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 0633dc4a-4f0a-35f5-aa73-fa1fd7a9cade | -15.01134 | -45.17004 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4c8723d3-7514-3bef-8dce-6d41960c6235 | -13.83785 | -45.23433 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7613d151-355f-3ecf-be73-c6f83d613f76 | -16.83079 | -43.5654 | 2026-10-02 15:52:00 | NOAA-21 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb3a174a-42ad-336f-99c2-01b974ee4ec4 | -14.55662 | -40.4995 | 2026-10-02 15:52:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 4714ba50-682c-3a46-bbeb-ec1cb922dd20 | -16.08799 | -42.62505 | 2026-10-02 15:52:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a9641cc2-d5d5-350a-8f2f-d0097dfb6740 | -15.85601 | -44.29617 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 94e93c04-b755-3d4b-a55c-1839b1260210 | -15.56585 | -44.54509 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6cd6f255-9294-3c00-a9ed-7830c043111a | -15.60388 | -41.6838 | 2026-10-02 15:52:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| a557f1e9-ce80-37b2-97e5-ad96546ca12b | -13.85629 | -45.23277 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README92.md)
