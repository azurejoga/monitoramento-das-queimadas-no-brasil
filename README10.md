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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 567c4c1b-a8d4-3a48-ae33-5a618c6e4231 | -18.81352 | -42.16265 | 2026-08-09 04:10:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bd404841-a9f3-3c63-b4e8-54dc1deebdb3 | -18.63242 | -49.86358 | 2026-08-09 04:10:00 | NPP-375D | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9794119c-38e5-3bb6-8794-3a64c98fab2f | -17.71162 | -44.1881 | 2026-08-09 04:10:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 435082a6-be5e-3303-9fc0-4497658d65e5 | -22.89765 | -43.6564 | 2026-08-09 04:10:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8bca0dcc-27ce-37da-b4ce-968b79733e3a | -22.86875 | -42.71766 | 2026-08-09 04:10:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6e07094e-2b1c-3115-8e3e-111d66a8815d | -21.43819 | -43.88226 | 2026-08-09 04:10:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 833f1ce8-071d-3c28-a0d7-5ea6e98b0eb2 | -18.93363 | -43.47921 | 2026-08-09 04:10:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0879214b-5cc7-3b0d-99d2-b187e44df1fe | -21.84912 | -42.34246 | 2026-08-09 04:10:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e43cf9c-0421-35f5-9bea-e7a5b6faf304 | -20.19745 | -41.66061 | 2026-08-09 04:10:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8a4d11ba-c280-3d92-b7c2-5722d859506d | -20.12132 | -44.44376 | 2026-08-09 04:10:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ec3f2525-c38d-37bf-91bf-4ed67b65234b | -21.04607 | -45.68199 | 2026-08-09 04:10:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2744784-0b4d-3ecd-9c41-667522824361 | -21.6061 | -41.93252 | 2026-08-09 04:10:00 | NPP-375D | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 42f71d21-317e-301f-bcf6-a35d1cc01e0c | -20.54342 | -42.3989 | 2026-08-09 04:10:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 65f41b8b-1469-382e-800f-6d7ba1ca59a3 | -17.71097 | -40.75748 | 2026-08-09 04:10:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 80e89b97-1886-35cc-b6ab-6669717ac30e | -19.8751 | -44.00222 | 2026-08-09 04:10:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 92434353-8817-3d97-8f5a-d408a190dfc3 | -20.60814 | -45.1129 | 2026-08-09 04:10:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 80f07f57-97d9-3b71-aa57-fc2dbfcec657 | -20.2138 | -42.57364 | 2026-08-09 04:10:00 | NPP-375D | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c813b27a-4792-3314-b35a-24148da255c0 | -21.92211 | -43.03992 | 2026-08-09 04:10:00 | NPP-375D | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bd94dab2-da86-310b-bd04-f0bace42e621 | -22.07624 | -42.34064 | 2026-08-09 04:10:00 | NPP-375D | CORDEIRO | RIO DE JANEIRO | Brasil | 3301504 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fc2f38e7-ac39-3132-9165-fc3ad273128d | -20.66526 | -45.02061 | 2026-08-09 04:10:00 | NPP-375D | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b8c4838-64d4-3cc6-9148-51c878a6d227 | -18.64468 | -49.85398 | 2026-08-09 04:10:00 | NPP-375D | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ec95257e-a09b-371b-b274-37bd90ec887c | -22.1894 | -42.48013 | 2026-08-09 04:10:00 | NPP-375D | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a8053bd2-db2c-3a1f-8da9-905ea6a2941d | -19.15102 | -43.4978 | 2026-08-09 04:10:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 18c461d7-0d4c-3ce5-b800-17d4a9940047 | -21.89364 | -41.29922 | 2026-08-09 04:10:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7fbfcf28-0ec0-37a8-8241-93aae2d921c8 | -16.71927 | -46.40054 | 2026-08-09 04:10:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e229447a-c4d8-336f-930a-f1f4ac75c6e9 | -19.58572 | -42.59574 | 2026-08-09 04:10:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| bf82e851-c6a4-3468-a3a1-07c368798088 | -19.58025 | -42.58708 | 2026-08-09 04:10:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 06df5e71-7595-35d5-93da-461e25192518 | -22.93983 | -43.42321 | 2026-08-09 04:10:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b1a29787-c7c9-39fc-8f11-82de7684ba06 | -19.58907 | -42.59636 | 2026-08-09 04:10:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 77f2fb3f-6378-3584-874f-5392f79780b1 | -18.6399 | -49.87751 | 2026-08-09 04:10:00 | NPP-375D | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2b4dbe12-ee11-3b04-a917-b9a349a94c04 | -21.3171 | -43.77151 | 2026-08-09 04:10:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 223d5428-9e07-3b2d-9274-149ac537450e | -19.58298 | -42.59142 | 2026-08-09 04:10:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b8b09c8c-bb25-3034-b1e6-9f885d4677e1 | -22.29963 | -42.6103 | 2026-08-09 04:10:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| b7957e81-c7e3-3ff4-b71d-6bad30c94d48 | -20.57867 | -41.92339 | 2026-08-09 04:10:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee35103b-0387-37d2-b41e-260ace7f7a7b | -20.27291 | -41.65057 | 2026-08-09 04:10:00 | NPP-375D | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6de4fbf4-9e54-3c81-bac5-2894d25fc9f2 | -18.49342 | -40.06732 | 2026-08-09 04:10:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d0ea340c-1273-36f7-9f5f-726bf3485ea0 | -19.18642 | -47.19181 | 2026-08-09 04:10:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c88e4d01-a925-3954-90ab-f50b97c91295 | -15.36695 | -53.77942 | 2026-08-09 04:10:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdb8362a-95bb-3c7d-a7cb-62e472e81495 | -18.66109 | -40.78593 | 2026-08-09 04:10:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 545fd79e-0158-3f57-90d7-0e6c4c19a853 | -21.28181 | -42.93538 | 2026-08-09 04:10:00 | NPP-375D | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2b2c2f83-37f8-37f9-b0af-04345d5054dd | -21.27347 | -41.74451 | 2026-08-09 04:10:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4dea8703-1931-310c-ac38-f8c70477342b | -19.99358 | -43.97247 | 2026-08-09 04:10:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ab1da212-4ad3-3727-b75c-64c8e02e40b6 | -20.78322 | -41.15282 | 2026-08-09 04:10:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ad494af4-03b5-3591-9499-cec4c5beeb55 | -22.23022 | -43.03773 | 2026-08-09 04:10:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| cc78e66d-bfd1-3524-851c-83332f60aa9a | -19.18571 | -47.19562 | 2026-08-09 04:10:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 165fb6cd-e192-311b-a3bc-37ba0f5f4c90 | -20.96999 | -43.9219 | 2026-08-09 04:10:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 68bfd2be-62e4-3b49-b5a6-ed97ab44e63c | -9.44 | -40.3 | 2026-08-09 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3e28110f-0d2a-3fe1-a30e-f3637f8d742f | -9.47 | -40.34 | 2026-08-09 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 77f89d63-98be-3d08-915e-ffd732463b21 | -9.47 | -40.3 | 2026-08-09 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ba348ef1-f0ec-3253-86e7-70c2dc8fe40b | -9.45 | -40.34 | 2026-08-09 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 37e725ac-cf3d-3041-a9c0-85452cd61d34 | -6.8388 | -56.4146 | 2026-08-09 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2dd2a8da-02d4-3eb9-9e4b-1d164cc91a34 | -9.4773 | -40.3116 | 2026-08-09 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 283.1 |
| 4d74c8a9-894f-39a9-934f-f27b6cd1d954 | -9.4769 | -40.3365 | 2026-08-09 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 209.2 |
| daab7fe0-ba1c-3ba1-afcc-90b71e957f67 | -9.4582 | -40.3143 | 2026-08-09 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.2 |
| b5f8ddd8-955b-3d41-ae6c-5a6148bba159 | -7.5736 | -45.2062 | 2026-08-09 04:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 8c047e65-37ba-36db-be2a-f418593f6c82 | -2.96176 | -49.2677 | 2026-08-09 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7880995-8113-335a-bd2c-5e5f560ff4d2 | -2.69584 | -47.35881 | 2026-08-09 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4c21cff-6744-3558-a47a-d66c3ffb0e52 | -4.10342 | -49.2715 | 2026-08-09 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19180b6d-f925-37e6-8445-23b2aee1efef | -4.27002 | -48.18829 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0b321b40-7caa-3edc-a650-5e2d14bacefc | -3.58572 | -53.30844 | 2026-08-09 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc4b2369-9455-3bf5-9a78-af7eea49a062 | -2.69879 | -47.36361 | 2026-08-09 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e7b1ced-954a-360f-8c4d-191992a390d4 | -2.48886 | -47.08079 | 2026-08-09 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18c8137f-d939-3ba4-8300-2c74199a2375 | 2.157 | -50.70252 | 2026-08-09 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b454914-ef8a-334d-a4a5-e285cf733386 | -4.26629 | -48.18768 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b65e5101-5a92-34db-8c73-16bf01fcbce8 | -2.55649 | -48.42677 | 2026-08-09 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4c55f1a-ce7a-3548-8172-3ffceffde07a | -3.12401 | -40.10805 | 2026-08-09 04:23:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ee51dc9b-54fa-3b02-a1b9-df08aa3ba1ed | -3.82237 | -48.97194 | 2026-08-09 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f55210f8-f0af-37bc-a4b1-a01e14c129e0 | -2.59104 | -48.93148 | 2026-08-09 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ab0169c-b3a1-3e7d-b4c3-e87980f1671e | -4.2693 | -48.19276 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8da74a3b-0e72-3eaf-b3bf-c66238098533 | -3.82023 | -50.63182 | 2026-08-09 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 345f15a9-0261-39ed-bd6a-0c455ac7f36a | -4.26557 | -48.19215 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| fc7d5f2c-0abf-370f-a1d6-f714884ec6f5 | -2.3799 | -48.22574 | 2026-08-09 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b133cb5e-ac36-3e3a-8c23-09d68a08fe79 | -2.96234 | -49.26411 | 2026-08-09 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2e6270a-f941-3e0c-962e-429c069c14a4 | -3.07475 | -51.53232 | 2026-08-09 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c10aba86-eb44-3585-bf9c-593a01f49673 | -4.27482 | -48.56503 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 894a8667-8078-3fde-af14-2403c2e50f5d | -2.96117 | -49.2713 | 2026-08-09 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 757b994d-d287-3e97-82ec-9520e8adbfcf | -4.27559 | -48.56034 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6a811202-466c-36a3-9352-dfef03b425c1 | -2.69948 | -47.35939 | 2026-08-09 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42277878-35fd-39af-b914-52606ecb329a | -2.94907 | -49.57954 | 2026-08-09 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12e056e4-2c0f-3716-ab21-3a6bb15f5349 | -4.74229 | -40.4339 | 2026-08-09 04:23:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73275bc9-cdc5-3feb-a046-6e4543f36583 | -4.95231 | -37.49358 | 2026-08-09 04:23:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9564a163-2bfb-3fb5-824e-e4816343364f | -2.37913 | -48.23051 | 2026-08-09 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e4c9b35-0d4c-3bb1-94a5-77c2fb7d413c | -4.27941 | -48.56093 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3d70b8e3-7dbd-37f6-8f8a-29c33085a980 | -4.26183 | -48.19153 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d5ff2446-78eb-35bb-a665-c526b47cb4eb | -1.58916 | -50.4361 | 2026-08-09 04:23:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c6aeea-de83-3c59-bcc3-b5b483850a93 | -2.96293 | -49.26052 | 2026-08-09 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 889b2981-d1c3-3858-8f28-23c3a2fdddf7 | -4.90245 | -43.47131 | 2026-08-09 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e25a9c94-1ef4-359a-8548-446c11c5920d | -4.26111 | -48.19601 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4e399c1c-ff9e-3cf2-bd46-d0592867d976 | -1.83208 | -54.66463 | 2026-08-09 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e927811b-b2b0-3f19-bbc3-e8da02620329 | -2.42561 | -49.02795 | 2026-08-09 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1497d707-d735-3723-a5db-ea9db900ce64 | -4.27865 | -48.56561 | 2026-08-09 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 90c15670-bd77-347b-ac6a-cb4baa86c010 | -2.69515 | -47.36301 | 2026-08-09 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ed8a853-2046-3a58-80cb-3a17ea168d4e | -4.45553 | -47.91717 | 2026-08-09 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2cbaec67-a0f4-3494-9690-3ad7434093bf | -4.95302 | -37.48883 | 2026-08-09 04:23:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5df4c2ea-d76a-330c-8c94-d2b969646b76 | 2.1549 | -50.70065 | 2026-08-09 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7310f895-066f-3060-9c10-10e0666c552e | -2.95887 | -49.25986 | 2026-08-09 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a5453b-76db-35f4-a3bf-65ad601f7ef2 | -2.37607 | -48.2251 | 2026-08-09 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eac556a0-51ac-3dcb-9447-8f2aa79659cf | -2.817 | -49.62105 | 2026-08-09 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec76b098-bee6-3105-a365-cf2925f5bbe9 | -1.82846 | -54.66624 | 2026-08-09 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7d86c91-5831-31d2-af92-4adf6f6595e7 | -11.27036 | -44.86935 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README11.md)
