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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df1ab351-ca45-3d73-b273-5e6ee38405a1 | -15.33878 | -47.33438 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbed3260-1e45-3cea-a1f2-c220fa961978 | -9.19926 | -59.40699 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f486fbc-cf5a-3cd4-bd52-70fb56d3fc60 | -13.12093 | -47.83384 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0bd0221b-ba51-3fb4-8722-d7825057b729 | -11.16441 | -47.75525 | 2025-10-04 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 98d4685a-8f42-39b8-84f1-87a7ac969c01 | -12.65101 | -46.97277 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 561d1263-8404-38a4-b77b-6a2aae2df9cd | -14.62746 | -48.25386 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51db5c60-88b6-3470-9dfe-78d9537b8ec4 | -12.47675 | -54.42898 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93251393-1870-3856-bd74-07c7f4b8903b | -11.12964 | -55.45982 | 2025-10-04 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cabdaa5-809f-34fc-88d7-0758dfc6abfd | -11.71148 | -47.51462 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90bb0a68-a242-37c5-ac45-1dd402d8308f | -14.66541 | -48.30266 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 554e1bf1-94ec-36d5-bfff-9874c4f9f6ff | -15.37838 | -47.95698 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64eae89e-dfb7-3d15-bd2a-3d7f62eb2b20 | -11.12684 | -55.45564 | 2025-10-04 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73eb8b54-7c9f-372f-8469-0c4ed0ae721d | -11.7866 | -46.83756 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 745b558a-3f8e-3260-ad5e-beffdd46aa1a | -13.7386 | -48.09106 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acfb316f-5a41-3021-a45c-1053324eb66a | -11.00435 | -46.68959 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aeff2c37-b74b-3cfb-ae0a-9f5456353542 | -13.74472 | -48.08519 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b59a5961-a3cd-3686-9fc2-ce7f74d798e4 | -13.12045 | -47.83778 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54885aef-7dd0-38c4-ac26-b801e3212c0b | -16.07368 | -50.90083 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8904b1e7-040f-3ffe-b190-15a9b19c0d27 | -9.6676 | -62.39207 | 2025-10-04 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e77986d-6c77-3931-9547-4cbbb3181b5e | -16.04663 | -51.00593 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d0c09dbb-6d82-3e8a-95b8-cb38fe132b68 | -14.74688 | -48.14228 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1530b3d4-3ff5-3be9-994d-641a0b33fb80 | -14.68061 | -48.26612 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10042ec7-78e5-32a2-96cf-e4aa7278fea0 | -12.27147 | -55.12319 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01e4017e-00f6-3db9-8a88-21b52367267c | -14.35259 | -46.10592 | 2025-10-04 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f490abd5-a0c0-3910-80db-525c2c0f44d3 | -9.19994 | -59.40294 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcc5927d-a413-3348-b210-ad1f2ad13bc6 | -13.25848 | -47.23996 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d6ab9e0-45c7-3ed0-931b-f0915d2c3ae4 | -12.81284 | -46.85863 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e66e5e29-c789-3324-b4b7-cf4703dc2391 | -12.39029 | -54.45285 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 057d9e63-5a89-30ac-8685-2d2cda64d414 | -11.12739 | -55.452 | 2025-10-04 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94f9b6ef-15e4-3668-bcaa-ab4374a4ed80 | -13.11915 | -47.9386 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 466a2974-b824-3a3c-98e1-ff5684cc72cc | -10.5741 | -48.69913 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eeb8f42a-1470-38ed-bc55-d8a8527ffeb7 | -11.92566 | -46.3531 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50e52456-0a5e-3b61-b525-d327d3fbd9b2 | -11.92573 | -46.36135 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66d13e87-d66b-3fc7-8ec1-132fed51809c | -13.32196 | -47.61103 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8581dd04-f2f0-34b7-95b9-17eee6d5a0a1 | -13.191 | -50.87442 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e67eb2d-3601-3cc3-b8a9-ab84a3461422 | -14.21221 | -46.0781 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4369c81-eafc-31ad-bf95-22c43dce124d | -13.33292 | -48.07087 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 696ca05d-a8a0-32dd-9e67-7adfc6eb0eb9 | -15.60241 | -52.49648 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 688edc18-cbad-3fa7-9be8-d75eb9b1fb22 | -9.25249 | -56.88182 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61e6c2d0-d809-3904-9147-98ace05c58ef | -13.74962 | -48.06693 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcac4a29-222c-3308-8227-54a7e293df49 | -11.71191 | -47.51104 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4db90468-0be1-3dc2-8c06-2bf373cd01cb | -13.32463 | -48.09407 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7eece58b-e19d-30f6-b7d0-80aa604101de | -14.92294 | -46.87492 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e6c0403-0029-3991-8d71-a88daba6e2fd | -11.91998 | -46.4087 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| bb7c6232-1d14-3559-91a8-b3fc70b6cb24 | -15.52716 | -46.83571 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c47a4e4b-5c54-3e43-8c85-9da9d6dab970 | -12.64876 | -46.99198 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5777470-0310-3488-89b7-866a9355b20a | -15.59525 | -52.48714 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13af4430-3e41-3fee-b37f-c547d2d5ffb4 | -12.08088 | -45.16703 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd40e82c-7dfa-3624-9549-8c7d902c4eb1 | -10.83351 | -57.17296 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ae91d6b2-7333-3fce-a3f8-f7b56a59adbf | -16.34981 | -47.07384 | 2025-10-04 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a985de2f-5c56-3030-aac0-b9a32ce00819 | -12.72735 | -48.5738 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1053fa31-33f7-3cde-a315-ce5d2690b1e0 | -14.68276 | -48.27417 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e876fd82-c6ac-366a-810c-a8cd495c9a98 | -13.57249 | -47.57846 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c10be1b8-1589-3f5c-929f-6cb7f37d5460 | -14.88991 | -48.30044 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3f4d72f5-c280-3a63-9e94-7e678943742b | -12.70991 | -48.56651 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66f68452-57f2-39f6-83f9-9e3535dc57b0 | -10.56853 | -48.70317 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64736229-8224-32ab-9971-3ef479e4b2f1 | -11.39586 | -55.16888 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b92f8fc2-c89d-3687-ba63-1e19ee306ff4 | -12.38092 | -54.46789 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69de8a80-a390-371c-9f33-643406ecccc7 | -13.93466 | -48.167 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5632717-6fde-373e-b210-b3a33e144d6c | -13.26928 | -46.47995 | 2025-10-04 05:06:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d58d2823-8c91-3a29-b798-59d016025ecb | -12.22779 | -43.76884 | 2025-10-04 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 300f6355-65a4-3e95-bab0-0382d5ba6cfc | -10.05383 | -63.3232 | 2025-10-04 05:06:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0461c092-725b-3579-8137-12107e3da7a2 | -11.11166 | -47.87764 | 2025-10-04 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01cba823-5474-3159-bd46-2981be3e0efe | -14.82483 | -51.74158 | 2025-10-04 05:06:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d18af18d-4c95-38db-8ee5-be2b2d2f0d06 | -12.92719 | -45.06343 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af457426-8af3-3cd9-86f3-cf2ea1f06138 | -15.73448 | -46.27596 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6220a0ab-dbdd-3e36-a5e4-3e36a864bc9b | -11.68994 | -47.49621 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0941f8b-2386-309c-b97b-7921b70bf0f2 | -13.29676 | -47.82579 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0497eda-9c24-31b5-b6e8-dee756dccfd2 | -12.92206 | -46.92315 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71bfd6d7-5cb7-32a0-a632-1cedcf583b22 | -12.81809 | -46.86392 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26a4d85a-0bb6-3734-986c-e2d5fd9eb880 | -12.38619 | -54.45634 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a549bfeb-c593-3495-a53d-bd0481c86c17 | -13.13581 | -47.81717 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1214ee67-9697-3b34-afa5-ce529a83cab5 | -12.27189 | -55.12019 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efbaaac0-696f-379b-a167-998e0ea66a05 | -10.83351 | -57.19444 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e7f0ff4-d149-3dcf-8726-cc4625b329de | -15.32074 | -46.30618 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78754d39-38a9-3c00-9734-27f5dffe64de | -11.41819 | -55.06522 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f16c0a71-09cd-36ff-ac22-054789822745 | -16.08159 | -51.06931 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3e5049b5-d595-3f4a-a1eb-1babf7761d48 | -14.94741 | -46.87025 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4c14d35-25b0-3739-9d3a-a928a4b1dcea | -9.90623 | -63.58787 | 2025-10-04 05:06:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cde4e9da-5d06-324d-add2-d4d1f16327e4 | -11.91137 | -46.37395 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c93c384a-b18e-3b81-b03b-3045c52e8799 | -12.03797 | -45.20442 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 00485d15-3e24-3d48-8f01-fbaa1a7d0c1c | -13.73318 | -47.92894 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4159fd53-680a-3fb8-9e6e-de20dcf1523d | -14.87656 | -48.36768 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d736ed0-e30d-37cd-8a0a-fe12eefd569c | -13.75088 | -48.05649 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ba282b2-ffc0-3c47-88c9-696bc5a66ba4 | -10.23919 | -54.97944 | 2025-10-04 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf87aa68-2005-3de5-b22b-2b366a7e9fbf | -12.86952 | -44.62708 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 401af2dd-0b88-32f0-9048-dc8d56fed0ab | -14.23011 | -46.08555 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5e1a5c1-ac3a-32a7-b2eb-9e2ea40d2028 | -14.20654 | -46.07285 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5daa1897-c444-3fca-80ed-75b4d7904932 | -13.13168 | -47.80499 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3d667fb8-c11e-30f3-a8cd-a7040c25df1e | -11.91288 | -46.36061 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 561bb5cb-54dd-3329-b48e-6184b53986f2 | -11.95666 | -51.48774 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a2fa54a-bc92-34cd-94cf-93e987e0d5ec | -13.74513 | -51.30323 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a384a30-7bd3-3c87-b482-71e3eece2f1b | -14.98502 | -49.9678 | 2025-10-04 05:06:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9e9c56be-ffde-3d82-9ad6-de54de7bfa23 | -13.18105 | -50.88201 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f627e24f-c697-3c4f-864a-1c6ede95ec3f | -13.13082 | -47.81253 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 48efc0d0-e36e-3dc2-8441-996d7123f94a | -10.8903 | -53.75005 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e61500a0-c925-32f4-9e14-a181c630af2a | -13.24384 | -47.8362 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40eb18fd-a7ce-3cf3-b687-b0d102d21eec | -11.91048 | -46.73904 | 2025-10-04 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9d2a79d-9a7f-35a8-a158-6584755797de | -10.89389 | -53.75055 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3397d508-d283-34a3-bdaf-5382934e83fb | -13.74326 | -48.09802 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README123.md)
