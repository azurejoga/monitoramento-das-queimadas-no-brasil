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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80d54a6c-5258-31f2-af9b-bf33c6d8d6af | -11.93207 | -48.06098 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ce5da5e-24a6-3478-bb03-3a2ea850a152 | -10.84355 | -47.78216 | 2025-09-29 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f451e8b-5236-381c-8cb0-8de7fcc00bfc | -8.86859 | -45.03552 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94a6d725-bb80-3526-94c5-851eefcbde5c | -13.83401 | -47.94036 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff4a3b2f-fd4f-3127-ba00-3e2cb3d2cb1e | -15.29141 | -46.41541 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4c0c666-7450-3258-9a67-1992c65b2e37 | -15.06081 | -45.05581 | 2025-09-29 04:08:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2dca684e-a3ff-341d-8539-10ecbf5c1ab1 | -11.66847 | -45.33105 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b702828-cd30-3d0a-926e-02c3f9dd8a1d | -9.44087 | -47.60236 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba21de0c-9b87-3e41-bd03-1258f63dcb0f | -8.73172 | -47.14083 | 2025-09-29 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b2fcfc5-34ae-3f97-93ee-5385e558c005 | -15.34233 | -47.90896 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0159aa3c-4443-3791-b44e-33d7a1f47e0e | -11.99102 | -46.5975 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db2651fc-54f9-3ff3-8b16-5d625802a6d8 | -15.16438 | -46.41417 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 925ab9e8-8b25-36fd-bb3a-c4240758bf32 | -12.90045 | -47.10982 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96a02171-a18e-39de-9273-379008ff58cc | -8.66411 | -49.43466 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cbe83d8e-e0b0-3c79-97f1-e4129eca2130 | -8.66505 | -49.4295 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a43a6e5c-eefb-3f60-a68b-bfe57ec662d9 | -12.2074 | -43.74731 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49f6f1de-7791-3796-a648-7a80d630d51d | -13.22965 | -50.95466 | 2025-09-29 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7f7132c7-b402-3646-bb44-6999835d1382 | -9.09492 | -45.85712 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce1f5658-9f90-3e09-9cee-83af8550cb4a | -13.76229 | -47.90955 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82e08b52-3a96-343b-a51e-f558020fe51a | -13.77526 | -47.8595 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a7499d9-6351-32f6-8ef9-395370ef90b3 | -13.35826 | -47.29555 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8072f26-b858-3291-80bc-34ff27ed30a5 | -8.81814 | -49.23788 | 2025-09-29 04:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a08f50c9-9070-3c5a-9c6a-96a3f07364b2 | -11.34573 | -45.06979 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 832eaa1f-5122-36f2-989d-816dc0b206f0 | -13.49491 | -47.40762 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39a6802a-96fb-3200-aa6a-f84dc8849856 | -11.86433 | -56.89144 | 2025-09-29 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bd9dd8f-0b73-3705-92ef-ae2aee0ec6f0 | -10.03736 | -52.10849 | 2025-09-29 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f182f661-7bb4-3d41-a396-cc74e8572e29 | -13.16884 | -47.41607 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f7dd8c0-6164-344b-88f3-69a198f89b60 | -10.53518 | -43.63823 | 2025-09-29 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eae8c306-d0f1-3d2e-95af-8e95e842f850 | -13.35735 | -47.30083 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62431287-9072-34a9-bb95-fc71a8da1fae | -11.34921 | -45.07047 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc408bda-b92d-3498-a9f5-33624f779b12 | -12.96371 | -45.19527 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9da66f38-5b98-3d3a-b717-4940ceb6ca76 | -13.7958 | -47.90353 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5007a8e9-e068-3044-bf8e-2003b39e355d | -12.9648 | -46.24432 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04ced9a0-bfb5-3082-8ba1-5e796ce23d43 | -15.0889 | -48.3368 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad9feedb-cfa2-3293-bea5-1d855e5cbc25 | -9.40627 | -54.71103 | 2025-09-29 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 12bda35b-abc4-360f-846a-94ed42d897c6 | -13.35934 | -47.81853 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed1f895f-1e28-3993-9a60-9fac41812eeb | -12.21016 | -43.75148 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ac3cc85-6fe5-3007-a111-ec388ff2968b | -11.93315 | -48.03074 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a22ead67-638c-320b-848b-332e597242c6 | -14.83937 | -45.56571 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27e6d465-88eb-3a32-8c32-245e883239e8 | -15.26158 | -48.76767 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45c2929e-b4e3-3d99-ac30-54a5cd8c9396 | -13.17901 | -47.44845 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 422dfcca-8450-3663-ac4d-d93611ae97ee | -11.50856 | -43.55119 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6db3723-dffa-3791-bb88-b9ae7d181019 | -12.42622 | -44.11253 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd5bf904-df13-3617-ac3f-748a07a35246 | -9.54606 | -47.76864 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05cd014e-04b6-30f0-a8a9-c9ddc3db47c4 | -12.15381 | -51.42641 | 2025-09-29 04:08:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 913b515d-357f-3133-b438-913361aebdc3 | -14.08902 | -44.08994 | 2025-09-29 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c73103c8-121f-3a0d-a35a-4212fc6a16b0 | -10.75704 | -45.38378 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1a1af77-30fd-3f75-9a9d-c64b7b645732 | -15.15369 | -47.45402 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be5cf811-228d-3b21-8dfd-7edb46474387 | -15.60795 | -46.25817 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1084c47-9d4b-3c68-9be0-6c7abaa40f1e | -9.46813 | -45.4916 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5015eb0-758b-372d-bc39-243b88c6daac | -14.44361 | -46.35794 | 2025-09-29 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 926a3d7c-0edc-3b5c-8285-361ad27ce90f | -14.57049 | -48.2825 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc508fa7-9a5b-30fa-9071-bb51097fba42 | -13.78811 | -47.92417 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b4555fc-50b8-3938-9b72-131d9f34f370 | -13.01036 | -49.43145 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 295cf348-c3d8-35cc-b8cf-b329b1e43df0 | -13.02919 | -49.45063 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77dc9096-9fb1-31c0-91fe-5c9c9d621624 | -10.4197 | -46.14743 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cbf5f1c-b6db-3ac5-a1f2-c5cdb421f7a0 | -13.81085 | -48.01897 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0daa8416-dce9-37a7-a5b6-31c9df279023 | -9.7742 | -46.20062 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71dfa75c-d6ab-345f-9898-a917bdfd18c4 | -11.69701 | -44.46989 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0c69c97-ebbc-3eca-b82b-a61b01663372 | -9.64085 | -48.12176 | 2025-09-29 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff6e78b4-0b20-3404-905f-4a721650b7ac | -11.98089 | -46.5839 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a1967ff-bcce-344d-a2f4-4eaf7ad78d16 | -10.83443 | -45.39659 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4292333-5329-34c0-be44-9d75dd06ce7b | -10.71663 | -53.79325 | 2025-09-29 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 534b3c37-5475-386c-a223-a65bdc6cf874 | -9.54014 | -51.36542 | 2025-09-29 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a170be3-dce3-3131-a79b-b75017a48ae7 | -11.36381 | -45.0691 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01a38cb8-08e8-3945-a194-22d2e5182679 | -9.7267 | -48.30423 | 2025-09-29 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02dda971-9063-3cdc-8822-f8325e0508ba | -12.58608 | -41.28592 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 383fa496-9a7a-3541-9c28-07ae529f7c1c | -16.40634 | -43.72485 | 2025-09-29 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 007dcea7-5614-3e17-9123-b7c395c5e857 | -11.36926 | -45.05782 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 024d127d-396b-3e00-b4fe-d36301013aa1 | -15.277 | -47.87541 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbae0947-8253-378c-bb7e-9ffd7ce8d3f9 | -13.39188 | -48.15541 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c8d65962-72c6-35b8-9971-65f6ea58128c | -9.46448 | -45.49099 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c49ec19-e09a-3ead-8d06-334d5b0f30a6 | -13.49362 | -47.4051 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 88a20c2b-67ab-3adc-923b-d2d3d7edc9df | -10.7655 | -45.37698 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39046ede-2a2f-3aaa-9de4-589b61663ef9 | -15.27787 | -47.87057 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e41a9012-5790-3aae-8df5-225d65a8077c | -10.44999 | -50.85878 | 2025-09-29 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5cb921a-9bd5-3988-a27d-e0e3388d6b21 | -11.41975 | -44.91272 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8a8c9c0-60e3-334a-a57a-7deaf66db710 | -9.45984 | -45.49778 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ba33072-0465-361a-a1c3-4a3df85cdf11 | -12.00142 | -46.60415 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b9006ac-c769-30f4-95da-fda01b600206 | -11.36604 | -45.07735 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b8d9042-c79c-3889-b2b3-79e199aaff70 | -11.76495 | -47.56051 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b84488bb-cfdf-3ed6-a2af-36b3777a246b | -15.90576 | -46.23667 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd935dc9-3d85-3642-b850-60d32529122f | -10.9461 | -44.31967 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17a36cce-1172-376c-946f-72c3c8d7eb62 | -10.30923 | -48.19906 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 886f4fbc-2bb8-3469-97a5-80641fb15458 | -9.98419 | -43.60782 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a64314e1-3413-3719-9def-dbc1a490f0ba | -11.35746 | -45.06408 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e8a8efd-dbef-303d-a82e-266e99798e25 | -12.21743 | -43.74886 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5bdc2d25-3d7e-3fe0-b1fe-ed252a8b9387 | -11.51637 | -43.54517 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9663e75e-f7d5-3598-bbb1-a6a58c410172 | -9.31099 | -45.71814 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a344e9c4-384c-349c-87f3-7eb7237a55ea | -9.0784 | -47.60596 | 2025-09-29 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 956da006-6625-39d5-b9b5-8994120409f7 | -15.40295 | -44.98005 | 2025-09-29 04:08:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9fe538a-a929-39a5-8ea5-558e2e21e1a8 | -11.98464 | -46.58451 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 799ff15a-892f-3af6-89af-8f10370cf349 | -11.82024 | -51.7834 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b21b4994-a202-3cd6-b273-a0edb64f57d5 | -13.57488 | -47.30136 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6b83653-7d3d-33f8-a6e6-9216b71f3cee | -11.71763 | -44.43053 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95499c83-dcfe-30ae-96a9-a3b53c7da508 | -15.91398 | -46.2096 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6be0f42a-851c-34ac-a62a-7a64c96b796a | -11.62808 | -52.85032 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deb76672-fa80-3ff5-83c3-871d90ecee52 | -10.76973 | -45.37353 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fa53409-a53c-376e-8719-fe4952128547 | -13.65722 | -48.0728 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb6b101d-fc7c-3a3c-a7ad-6277b9478c80 | -15.23812 | -46.66525 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README52.md)
