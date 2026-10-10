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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4b4fd53-d25f-378a-91e6-2df5dc852e76 | -11.99432 | -43.44689 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc98b5af-6631-397e-a3ed-1ce44b62f7c1 | -17.45914 | -45.08533 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5129d52-6c1a-3a8f-a36f-2a3497d7c6d2 | -15.57998 | -44.53087 | 2026-10-10 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 166f93d1-5f57-3575-a2aa-5272358d2bf5 | -11.75591 | -46.79729 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7475acd-8b49-32b0-8ae6-c9f099bb4318 | -16.60219 | -46.76005 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5171505a-7ab4-3c86-90b9-f546fa9235d7 | -8.49176 | -54.60559 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5bb56cf-fe83-374a-aa2a-11d70417b421 | -10.89384 | -44.79503 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2031cb4c-144b-3caf-979f-fb631a4f947a | -11.76358 | -43.52813 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5a73273-45aa-3b19-8c1a-2a3fd0c93666 | -13.3842 | -43.88916 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22d99c26-ac15-3a4f-962b-9ee5534676ca | -10.44823 | -47.84825 | 2026-10-10 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21932d0b-08ea-3ed8-88a7-e54e05ed037e | -14.72824 | -48.2097 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 20afd1e7-ef3f-3e17-bbd8-8839234049ff | -9.85063 | -48.0096 | 2026-10-10 04:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2138324-cbbc-3d20-8fef-a27ee2339569 | -11.66238 | -43.69263 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d9041c3-dbef-3739-89ef-37ad68e9fb48 | -16.8479 | -46.37234 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4a9b0c0-ac08-3adf-ad88-c1cc80a4d05f | -12.074 | -47.37806 | 2026-10-10 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89ebbe56-16c9-3461-a479-92cd7b567bb7 | -12.21887 | -44.84254 | 2026-10-10 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b40ca350-e4a9-3225-a711-d4a79e8512b5 | -10.89544 | -44.80688 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 28b03308-0314-3964-abe8-25508806a2b4 | -14.45956 | -43.9547 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa1f725b-5eb4-3474-940d-1f24256b6b5b | -15.55635 | -50.49353 | 2026-10-10 04:10:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef60e8dd-2c68-3b1c-81f2-076833ed2ab2 | -15.75111 | -45.70752 | 2026-10-10 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d474d9c7-c9ef-3c73-bc79-17d21bd87d6f | -13.52793 | -47.41303 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2226e6d3-77a5-3b96-874b-adee9f2eabe4 | -16.00822 | -43.60247 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1f101f6-af2c-3a8a-b1aa-f82a3f5d237e | -11.83629 | -43.58328 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8325d48a-c3a0-3d5e-9034-9ce491df03c9 | -8.50371 | -54.61336 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c10b33e-cb6d-36c5-8b9c-0f4192b85805 | -15.46492 | -44.31257 | 2026-10-10 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b3ed476-1f55-391a-ae51-4ca877783d68 | -16.59661 | -46.75053 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28af44f6-afcb-3b03-91d3-710c60d869a4 | -14.45021 | -43.94952 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c617ff0-785c-3fcf-be77-1d635a5b41ce | -14.43862 | -43.95852 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a37bc658-d940-340c-ac60-c1aa5c8df7c7 | -14.86865 | -50.30744 | 2026-10-10 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc1cd253-681c-3fa6-8bfd-91d0b6dc4027 | -11.5182 | -48.72765 | 2026-10-10 04:10:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0179f8c1-fa50-36b1-9323-4348d9fe3cd7 | -11.2133 | -45.24866 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a02bf1a1-1213-3e61-8950-ac5093be198e | -14.02921 | -48.76386 | 2026-10-10 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af3c0cf3-4a9f-3a10-8c13-34cd8a7af69d | -16.12151 | -43.74927 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5507eebc-4c1e-3e35-b64f-5a941e775e42 | -16.12095 | -43.75282 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 091bfc27-f9f7-3dc2-82e4-412d582d6b2c | -12.03841 | -43.38212 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f381793c-2f1e-3534-b32d-2dc4edec7389 | -10.94306 | -45.3699 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ea1c6dc-9cb4-34cf-9f8b-ccafe11d75e7 | -8.50476 | -54.60777 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d39c0d23-5950-38f0-aff5-b0964dcf1870 | -14.05938 | -43.83753 | 2026-10-10 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e55ec16-b105-3b30-9acd-1c7290f09aff | -11.84176 | -43.61312 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef05ca30-90e7-3717-bdb5-bc5055367216 | -13.36709 | -43.88998 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffec1af0-be35-3f54-bdd3-a6cb3d39df5b | -11.12684 | -44.02148 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39da1555-ef9a-3456-874c-aa549ae97a5e | -13.10317 | -46.36092 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 0bb1ab34-a15c-3922-b42a-1af58c7e3fce | -15.58213 | -48.18382 | 2026-10-10 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c153ea1b-810a-3e35-8f29-1280ca5f7f2c | -13.39137 | -43.8867 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e8e4365-c023-32d8-8660-c447fc905dc6 | -9.91296 | -48.1297 | 2026-10-10 04:10:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9b17988-1af1-3634-af16-7992ed841aa8 | -12.96274 | -44.58799 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7bf0850-9f44-3c98-bc49-dd1bbb547349 | -11.04822 | -44.01967 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fb6878a-29fc-3770-bb0a-f2c47de5478a | -11.73948 | -43.5062 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d78fdca8-f4d4-35e1-a46c-d94efdd6fe2e | -12.02564 | -43.48449 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b057fb9b-cc75-389b-8d4d-bf90977430cc | -11.84317 | -46.78931 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 59df9973-7501-3a20-9d5d-dbf7a53e9d70 | -14.97301 | -50.3808 | 2026-10-10 04:10:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27722e96-bfd7-3b50-b30d-7f2976137e2f | -17.46479 | -45.07137 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3d99dc0-10f2-3374-9562-689e4aeffa21 | -11.08233 | -44.1066 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3e2240f-6f03-381c-9aa7-69e9a3cecaa0 | -11.98943 | -43.45288 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 316388d4-52dc-308e-902f-9562419fd147 | -8.49072 | -54.61108 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bde20811-18ae-30df-9490-1dde5a573e08 | -11.6195 | -43.59818 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d1108df-eeab-3606-9611-7fa7f08965cd | -11.59599 | -43.74656 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5947fed2-412f-3a76-9858-4f24d7d1b9b2 | -11.0873 | -44.11853 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d3aaaa6-2874-3aa5-aa84-ef798d777829 | -11.93876 | -43.47342 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63781333-8771-3c6b-a1b4-9ae4b49c3bcc | -11.77294 | -46.80989 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9bebc9c-a20f-3cd7-ae3e-b0c5dc92df77 | -16.57981 | -46.76439 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccda0c56-20d4-38cd-ab81-1daf29731dde | -11.98557 | -43.45587 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12244802-ad84-3e38-b9fa-4c0f61245dd6 | -17.46305 | -45.08225 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecd072d8-f4c3-385c-bfc8-d187d8f91a52 | -8.49723 | -54.61217 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| afde2d32-4f2b-3fcf-a365-b4c570e1bb56 | -13.77156 | -45.34408 | 2026-10-10 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fb8f805-7b1f-34bc-8303-32cf8abb2865 | -13.90975 | -48.9187 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b88e7887-2692-319e-a066-7b7811710bf5 | -11.95196 | -43.47561 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ee5b8be-e9d6-3ee5-8a58-8dd6b85ab4f0 | -11.95801 | -43.48024 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82586775-7d61-3ad4-be41-16658f2a4853 | -11.05888 | -44.10276 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6d5bc2b-fc7e-31da-abe9-1260f4341f34 | -13.25326 | -42.25785 | 2026-10-10 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0313c0e1-4b80-38ed-a20b-ef519a6ec15d | -11.83243 | -43.58628 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1edef8f5-8226-34e4-af1a-4d6a0d0d2e05 | -11.97456 | -43.46127 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2ef1668-d433-372e-b285-45194ecd10df | -13.15447 | -54.37051 | 2026-10-10 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf21a0ae-1435-3f41-ab44-cae0584fcc47 | -10.92828 | -45.5238 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 633e6a2f-3761-3e0c-9e9d-21bce6445dc2 | -10.89984 | -44.82324 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| dab44c32-b6e6-3a9c-b9f8-47fbd65adfa1 | -13.35323 | -43.91313 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5b9c749-83b1-3ba7-9e4c-2e00143928d1 | -11.28767 | -45.20004 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8f45512-61f7-399d-b0c0-3830caacbe57 | -16.12755 | -43.75391 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed5fcf02-1944-382e-b6b9-88b26e7a4b60 | -11.0475 | -44.04541 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbd17069-ac50-3f2f-9794-687997abf099 | -15.38074 | -41.91686 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 05bb3354-d790-39f4-89dc-bb01d1ef9f4c | -14.33198 | -55.02816 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1416d494-279f-353c-8251-e6fdb14efcf7 | -11.69276 | -47.28979 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fa761832-a1fb-3fa9-b8e6-754fddb69e7e | -17.28999 | -41.2298 | 2026-10-10 04:10:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ce96c7e9-d364-3ad1-812d-14e3c958b7f1 | -13.13858 | -40.87824 | 2026-10-10 04:10:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 03924dca-ea14-3a8e-b343-ea5e104303d4 | -10.52413 | -49.46085 | 2026-10-10 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22a3808b-a877-3976-a0c2-29acfad3e250 | -13.39524 | -43.8837 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7efc2de-2c2f-345e-b24d-310fb32f9984 | -11.96298 | -43.47021 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b96ac5cc-617f-3931-83bc-18cb9db61939 | -11.84385 | -46.80796 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f253206-922d-35c2-94c7-76cba26d572b | -13.53093 | -47.41803 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b8c597b-4459-38ac-b394-d86ddd657810 | -11.97673 | -43.49049 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 892a90db-0d2e-3c38-8517-0c148f843ed9 | -15.24835 | -41.88877 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 40a3ac05-ca3d-3d1e-bb80-732700b3b7e8 | -11.22854 | -44.83388 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86c71600-4e6b-3ddf-9c93-59cbcb2153d6 | -15.85405 | -42.03451 | 2026-10-10 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35268be4-9583-3783-b546-93da1dedfe3a | -14.04961 | -44.81847 | 2026-10-10 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cce71009-2b33-3a45-8601-1bd82da0804a | -13.76985 | -48.12268 | 2026-10-10 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c435a87d-ade4-30b0-9813-f90013ece343 | -13.25727 | -44.00295 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2fa00f5-89e9-3ba5-93cc-66b760d435d8 | -11.24649 | -46.29322 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d276239e-88b4-3739-9820-aa5558752a0e | -13.25783 | -43.99941 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c609530-4752-3eb0-865a-fa5f06645a3f | -12.36127 | -46.59226 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c593ad27-3afc-35b7-9b0a-8f784139cb1f | -13.36978 | -43.91586 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README54.md)
