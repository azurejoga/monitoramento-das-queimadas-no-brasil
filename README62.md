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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5924de18-2b8f-3a86-ab29-79461d6593f9 | -11.50285 | -48.47419 | 2026-10-07 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4b56bb9-3aeb-3b9f-86a3-a1002360944c | -10.4866 | -50.43103 | 2026-10-07 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fa70ce4e-f361-393d-b598-7830998de2fd | -12.21369 | -44.70701 | 2026-10-07 04:21:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b074efc-d45d-3b84-bf88-8dacf47d769b | -11.36806 | -46.70051 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcfc2014-0e42-3d8f-a088-51b266a4857a | -13.2685 | -43.99999 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 242552e1-251f-38ad-b902-95a3a2cf1943 | -9.81585 | -44.78714 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b4f6a76-0ad2-3ed9-b850-b467c6d00acf | -9.25936 | -45.64807 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c4101d8-00e9-3136-8b34-6cdf8e331aaa | -11.58282 | -48.59681 | 2026-10-07 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34285221-e63e-30bc-a406-4f1b1517759e | -8.74268 | -47.87444 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e95756bd-09ab-38e3-a7bd-e772cf9bf0ec | -10.96705 | -45.40175 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ae25182-6708-3e19-883e-7a7db370b9a6 | -11.23205 | -44.85591 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a2326a-727c-3931-bea3-87071ed853b9 | -11.73138 | -43.64932 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb0134f9-419c-3be3-b461-688f9a82359a | -8.91085 | -49.97964 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0bc91e04-5e75-39b3-9e72-79ea3615d435 | -13.00889 | -45.99925 | 2026-10-07 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5034a927-2fec-3ca6-92d8-2f22186a3442 | -9.80266 | -48.92344 | 2026-10-07 04:21:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a34cee64-2f68-322f-b79f-56c66321583b | -8.69168 | -45.21875 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c64f19a-cfb8-3779-b2e1-28bca30d1ae3 | -8.74948 | -47.88031 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b11a7229-b2cf-39bf-b7eb-6a7db8b24328 | -12.04149 | -43.44144 | 2026-10-07 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d8d3acd-2c4f-3fe4-a114-d6415a2f1f12 | -9.45236 | -44.5951 | 2026-10-07 04:21:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45059fcf-df6d-3cc9-8a79-2855a0ad204b | -10.38622 | -45.14904 | 2026-10-07 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43120a73-5f46-360b-85b4-1dc81b4af4f5 | -11.23368 | -44.86701 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c19e5a1e-0100-3450-8903-436f409816c9 | -13.2669 | -48.79021 | 2026-10-07 04:21:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73c23538-f20a-3ef2-8001-6ca86511ba9f | -13.63747 | -44.42126 | 2026-10-07 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2e6258d-6f4d-33e0-82b3-532a693942a9 | -15.24398 | -43.27353 | 2026-10-07 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 59b04f4e-c684-3742-80cb-2afb5513c075 | -12.17397 | -44.72212 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af60d6f3-7822-3b28-b665-0f5e7d9b1326 | -13.39323 | -43.87256 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87c1028e-8b42-3754-8cbc-54f42371d979 | -12.81711 | -44.67169 | 2026-10-07 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| baa8e49a-e258-34d0-b1af-cfb255ec72eb | -16.40751 | -43.7259 | 2026-10-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c2d702a-6eaa-3356-8bd4-ac566472da01 | -8.91374 | -43.88197 | 2026-10-07 04:21:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8410dc06-e44b-361c-a0d9-0f4b388305ed | -9.80588 | -44.78552 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 596f7d75-a115-31f3-a84d-d027690b9207 | -11.78395 | -46.70931 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 51836c14-8035-3a41-91e5-3c125f0c5692 | -10.21874 | -44.64728 | 2026-10-07 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fbce1ab-4866-315d-9988-f373ce27e8f5 | -13.5066 | -44.36703 | 2026-10-07 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b723a342-31b9-3920-93c7-5f65bf435fbf | -13.30704 | -47.53663 | 2026-10-07 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f1c56b5-8f41-362e-a13e-e847e5e4331e | -15.11321 | -43.63131 | 2026-10-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f39104cb-c325-3705-8443-b32020d5fd10 | -15.23997 | -43.27683 | 2026-10-07 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 96a6c378-7808-32f1-8647-f5e7fec2ecaf | -12.78332 | -48.61852 | 2026-10-07 04:21:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c45bb0f-23ab-335c-bb5e-04be03e3091b | -11.77388 | -46.5779 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e05a5c67-b61b-346f-823b-8d17df56816e | -9.16576 | -47.58355 | 2026-10-07 04:21:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d332ed0-37bb-385d-b946-9ea4ec4d1942 | -13.39267 | -43.87616 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c70d0d0-a0ca-3cca-adb7-a1e3b38babc0 | -11.79148 | -46.70665 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5b3c8410-52c5-363c-b538-4e73877c3228 | -13.66962 | -44.28042 | 2026-10-07 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e7ffefb-3b75-399f-8b4e-97bc2d2a4fdb | -15.33685 | -42.7668 | 2026-10-07 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| edc8053b-5b2e-3770-afae-876674298b09 | -11.32502 | -46.6811 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03980ef7-1a53-361f-a3e9-20d9ac8598a4 | -11.061 | -45.83242 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d4faff2-0015-37bb-9fd3-dcb2b3d12815 | -12.17508 | -44.71509 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a96accc-1fae-3788-93ab-10e7bea2a220 | -11.37341 | -46.68959 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d9b2a0f1-fd37-3467-84e2-f8f0f461877e | -10.36848 | -45.02599 | 2026-10-07 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d990c490-812f-38af-b4a7-b463878b1ed3 | -10.85623 | -50.66831 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c989f500-adef-304b-9984-463e09812c44 | -11.23298 | -45.25111 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 792e4f87-2f47-3f39-bbea-664c3a1a7074 | -10.59447 | -51.83926 | 2026-10-07 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f0ff64a-5fe6-38e3-bc07-447067e2bd61 | -9.34573 | -47.84694 | 2026-10-07 04:21:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee3c6c04-02d0-3e8e-9f50-5a6849532a25 | -13.38265 | -43.87455 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bd5eac0-eba7-3816-aadd-cb35d72f4eb8 | -12.82887 | -45.55566 | 2026-10-07 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15263721-35a7-369c-a8d2-5d97acc499bf | -8.70986 | -45.19206 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c5598c21-332d-31dc-972c-d84567dc45e7 | -13.50273 | -44.37006 | 2026-10-07 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 602d41ca-7ef9-335d-8b53-fa37b3c9ea84 | -12.17341 | -44.72563 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7d579ca-a699-3926-886b-e0bcda777f39 | -9.67505 | -47.89679 | 2026-10-07 04:21:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92ec84f0-7851-33ba-aa8b-d149b8bf0e37 | -9.16121 | -45.11386 | 2026-10-07 04:21:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c45ca13-7170-36f4-bfab-00f2ee0b6708 | -8.27949 | -50.27658 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b133972f-6d38-32a3-84a0-79e35793ef38 | -12.16903 | -44.71049 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 757c5b08-eb71-3065-9861-18fa3c2fd719 | -14.25354 | -41.62165 | 2026-10-07 04:21:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d4c1401c-47f0-34bc-9747-d13fa764db2e | -9.02377 | -45.18348 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 285f890c-2b05-3c70-a153-6584d0a6486b | -16.13116 | -43.75006 | 2026-10-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63aecd90-9b65-31fe-961d-254adbe2ea65 | -8.78074 | -47.58046 | 2026-10-07 04:21:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afe13d10-3ff2-3b44-b7dc-ee2d78532dde | -14.78613 | -42.8998 | 2026-10-07 04:21:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| f79b3992-cfcf-3918-89cf-e286721b8800 | -11.64319 | -43.67197 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a6945fe-723f-3c9f-a544-629262411496 | -11.66757 | -43.66468 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03e1ffc3-c455-3974-958a-9cbfe4038cb6 | -9.78091 | -44.79232 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab0d4811-685b-3b96-bb22-2d9636186f83 | -11.11078 | -45.71732 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 129ae6f4-e0f5-3127-8245-5a86b0c0d85d | -12.38733 | -49.82266 | 2026-10-07 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7c4f600-304c-3363-a342-08c45bf450c9 | -8.71045 | -45.18845 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9932c844-0520-37c2-8da2-06f5e5c2a62a | -11.01081 | -45.44939 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af7c2416-b615-3660-8a1c-48355723f910 | -11.08615 | -47.60962 | 2026-10-07 04:21:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17460e1a-7ee6-33b4-9376-4eefce6b0bda | -11.71174 | -43.42276 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8152c69-b6a2-33c8-a5cb-6b3e9d769e12 | -11.78137 | -46.57527 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16c57893-4566-32da-9b9b-2914f781937d | -9.87364 | -44.80771 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91e12eb0-204a-30a1-a236-adb11a4236be | -11.00035 | -45.4292 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8af77f2c-17e5-3777-988b-8bc304db9082 | -11.7364 | -48.42503 | 2026-10-07 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65e10de3-63ae-36ad-b2ca-dd574a72250d | -9.75984 | -44.79612 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc36031d-4d29-3966-b2a8-081cd798ee6e | -11.37405 | -46.68569 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e51c281-543c-3256-8ddf-3daf2143473b | -10.48944 | -50.44022 | 2026-10-07 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b6b4193-5677-30ef-b493-8d23f0285804 | -8.74568 | -47.87972 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7fff8059-00a7-318f-b74d-bb2264c4e655 | -13.27128 | -44.00411 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0219448-cb88-30eb-a492-35fddd09e340 | -8.88345 | -45.37663 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 464b4cae-ce19-35a1-8063-adbb50fd2310 | -11.63655 | -43.67088 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33237c6f-5597-3a66-8be3-3ab5a33ef47b | -10.84904 | -50.6581 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b8b32efa-67e4-3331-8e09-588996168047 | -8.28144 | -50.2738 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8779c64d-85b6-3d2a-b237-25eae8282324 | -11.84179 | -43.55033 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b910234-598a-3564-94b6-060f3fe26487 | -9.39725 | -45.81515 | 2026-10-07 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60a64f64-386f-360b-b0e6-febb9cf56daf | -11.70197 | -43.66285 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3493ca4a-1c3d-3e3c-8dd0-8172d0ec941e | -9.51736 | -54.73995 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e53e66f1-aefd-3888-9704-f44aea4c636f | -11.00529 | -45.44106 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 246d10b6-5c54-3269-9238-15a360cebcef | -8.70019 | -45.209 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e5a472bb-1bdf-323c-9975-d3ff77634293 | -11.00747 | -45.44884 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1fb5426-b0bd-3827-a0d1-91713ad9b47c | -12.17946 | -44.73022 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23d35444-4193-33ac-bf54-16d61a5f6e25 | -12.17066 | -44.72158 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5073519f-4c5f-318c-bd2a-a659ea050b47 | -12.16847 | -44.71401 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f9dd90a-599e-3fce-970f-5f16c89ec254 | -8.70355 | -45.20956 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f690fd7a-3faa-32e4-97b3-f68e18f73941 | -12.41428 | -40.92376 | 2026-10-07 04:21:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README63.md)
