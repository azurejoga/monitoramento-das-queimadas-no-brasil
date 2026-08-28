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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bda82ad-6787-3c60-9b4b-ae80b88aaf8d | -12.04014 | -42.97776 | 2026-08-28 16:05:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1e85afb9-7d4a-3321-848a-7b4d11b17dd0 | -6.55881 | -45.32479 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 629dd5a1-069f-3653-9157-f77c269dd40a | -9.50412 | -48.02368 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b910bb25-d7d4-3cf9-8448-a96b37b94ea4 | -12.40186 | -41.65002 | 2026-08-28 16:05:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 674768e0-befd-343f-a650-3eaf01eaab52 | -13.32262 | -46.9052 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ab9fb1bd-ebe4-3451-9e4f-0f6ea7c72cc7 | -5.10322 | -38.06727 | 2026-08-28 16:05:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ff21806b-ee31-3428-98fe-b383b9ccab05 | -16.54889 | -42.40898 | 2026-08-28 16:05:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e2d8c66-cce4-3f91-bfbf-dc0c5092900c | -8.16772 | -46.16419 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54e6a4ad-84c9-3a63-968d-ce8e4dd09d93 | -9.49797 | -45.63028 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4bb2db35-ebd5-3bd6-b3fe-cc9d7bf998c6 | -6.37632 | -45.84042 | 2026-08-28 16:05:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9adf8d8e-0ad8-36b7-ac33-cd69861beca9 | -12.86896 | -44.35396 | 2026-08-28 16:05:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c1e61b84-1dbb-34bb-a1d7-cd9faa6b6c12 | -13.58578 | -45.78145 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9232fe80-ed57-311b-8c64-b197ace6fd64 | -16.36854 | -39.65955 | 2026-08-28 16:05:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 2eecd540-76b3-3e4f-9c12-4ceeabcd2f10 | -13.38419 | -50.22365 | 2026-08-28 16:05:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 143bad5e-3492-3cbe-8cc2-bbab0f34f8c0 | -7.08495 | -42.82679 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eb6c12c4-273e-38ed-bc19-3990107893a1 | -7.10146 | -42.20389 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| f7e5a63c-d39d-387a-8c4e-293a8af85e73 | -5.80947 | -43.64066 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5d4c6c95-ff48-307c-b7a8-2bc668c7fc42 | -16.51872 | -41.50848 | 2026-08-28 16:05:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6115b8a5-59a8-360d-a563-686eafcc9462 | -12.09107 | -47.16675 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3b8b3192-1ddb-360b-8ff5-7649a60bcf6a | -8.67104 | -49.55172 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 11db6e4e-314f-31fc-934d-70593f698e1e | -13.58237 | -45.77794 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e73501a2-de38-3b1e-8203-a0dee46d14e8 | -7.27412 | -49.85575 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b361e958-0509-3961-aaa8-bd0de54c197e | -5.87454 | -43.59298 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 053d2c3a-1d3f-3aa4-b983-4a9a2da2f051 | -9.50032 | -45.64775 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1fb7b46d-d668-3337-b9b5-c8781ec40aab | -12.86767 | -44.34323 | 2026-08-28 16:05:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f6a1e4a8-d5c8-3bb7-9b8d-2823ccb09630 | -7.10246 | -42.83494 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a7d90c4f-3feb-3316-835a-d7e2854d2af0 | -15.71349 | -41.34446 | 2026-08-28 16:05:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 27f368e8-eda5-3774-8570-d2d7daa03f84 | -8.96126 | -45.73542 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| aaa9e50e-d42b-3c45-9f07-ee2b3d081092 | -13.12661 | -39.90894 | 2026-08-28 16:05:00 | NOAA-20 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c86cb717-576d-388d-b2b4-fd544943d0a9 | -7.62631 | -44.82244 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 77b10d32-9c2f-3fcb-ad14-a58623eddff9 | -8.08877 | -45.84864 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9b022ce6-404a-3385-8940-86abda8f9243 | -13.32408 | -48.19399 | 2026-08-28 16:05:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 86a7b57d-acaf-3bec-a4fa-fa7277591832 | -7.06516 | -43.58525 | 2026-08-28 16:05:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| def91227-424b-3a81-8bfc-af13bbf8e65a | -17.57268 | -46.51351 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e5e3066-8a2c-3935-93aa-3cc2a9968cc8 | -13.45152 | -40.29391 | 2026-08-28 16:05:00 | NOAA-20 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9b9b992b-8871-3b94-a5d7-4b04a1d135ba | -8.87377 | -45.99771 | 2026-08-28 16:05:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| eec4c3ed-a1dd-38d7-8228-733cadacbd44 | -13.86437 | -43.63956 | 2026-08-28 16:05:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 00fdf3bd-d06b-3ba0-9967-d1c9fdc36f2f | -17.26662 | -46.02989 | 2026-08-28 16:05:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee7a789c-528f-3d33-a08d-a310cabd848c | -13.33025 | -46.92081 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2d069f98-1097-39ca-925f-de7b10b3ee20 | -5.95487 | -44.80373 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 57af2427-2089-38f5-98f6-ca61cd1b5d67 | -16.85781 | -46.63883 | 2026-08-28 16:05:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ba011172-bda1-3689-aa14-2f2d28652bbb | -16.75849 | -46.82779 | 2026-08-28 16:05:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fe4b3d46-647f-3c87-bf71-fa7e8acf0a2f | -13.34565 | -46.90199 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 50cc422b-2abc-3d7f-b750-2e4874a605ec | -9.50631 | -48.02663 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 69a47809-7cff-3c1e-ae3a-4d9e5e78e8f9 | -16.85737 | -46.6344 | 2026-08-28 16:05:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63dad973-b244-3128-b5b0-f15fb7030680 | -15.02027 | -39.40476 | 2026-08-28 16:05:00 | NOAA-20 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 51211f55-1459-3ffa-bb84-16a954dac669 | -5.58159 | -42.69159 | 2026-08-28 16:05:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 67e22b2f-51eb-3dd4-8a96-8264c4349741 | -9.64098 | -48.27407 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8d2eaa59-e385-37f2-a34b-3da9dfdd3d4e | -9.48362 | -45.63781 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a941c48d-3852-32af-ab48-ff531558de68 | -7.09579 | -43.71027 | 2026-08-28 16:05:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 90b665a5-7e2e-32a2-98e7-a03e7e0e995e | -13.58733 | -45.77382 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d5a85089-a65c-3d7f-bf62-5b1fc3bf888f | -19.59547 | -46.54097 | 2026-08-28 16:05:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f10fca9-aecb-34e2-bfc4-e9cb20619f85 | -16.02625 | -46.54397 | 2026-08-28 16:05:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f23d582-3628-3a0d-8a3e-4b26fceee0bb | -8.96283 | -48.16786 | 2026-08-28 16:05:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 574c076a-d480-307b-a3cc-49e9d2ca2f5c | -7.15407 | -43.20174 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2177eb7c-a721-3150-9745-6c6e23408d06 | -15.62784 | -45.93182 | 2026-08-28 16:05:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 51605c96-2421-3bb0-994c-2b9b00f4ece9 | -12.39068 | -48.19036 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d56fed78-9aca-3365-9021-85e143cffc27 | -8.94969 | -45.72541 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 523a3ded-2514-3644-a2de-68871a9e5c0f | -7.20097 | -42.73828 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 9bb12a54-b42f-37b4-afc2-c5fe0cccc293 | -6.84324 | -42.83018 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f2818bca-bd71-3fd2-be0e-a802012ca078 | -12.39185 | -48.20023 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 111a63b7-ab90-36db-a20d-89b09119d437 | -15.30694 | -41.4086 | 2026-08-28 16:05:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fc0e5ba2-c233-346c-8227-7b02cacd9aae | -18.429 | -39.94772 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| d8af8adf-40b9-317f-a132-ba70cfd31110 | -16.75627 | -46.83073 | 2026-08-28 16:05:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6e6a267f-a58f-35ab-befb-d8e02e42194c | -17.51853 | -42.00634 | 2026-08-28 16:05:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 2e2eb4e9-e4d7-352e-bb94-cb6767694335 | -9.5023 | -45.66245 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| fb056418-7e50-3f94-9baf-71a761b50c18 | -5.95505 | -44.78791 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1806a0f4-13b2-37c1-af92-a4650293b5bb | -5.95956 | -44.78736 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| db229f8d-fa4d-3563-980e-ea29b5efd943 | -16.31348 | -47.84462 | 2026-08-28 16:05:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b7b2d728-e1aa-357a-bf03-176fa394a9a3 | -16.27034 | -40.85694 | 2026-08-28 16:05:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b5523d94-729d-3766-8d34-941da3b5df20 | -9.48323 | -45.63488 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c3ed8ec6-0af1-365a-a7dc-b7de60892187 | -14.492 | -49.11522 | 2026-08-28 16:05:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4a6ded8c-41b3-30db-b085-7ded3a58ec65 | -13.59651 | -45.77987 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 103dca51-9c45-31f5-ba71-0b2c30f593be | -7.10196 | -42.83142 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 74b9e07e-53b6-3cd8-9dfe-53604b4ce837 | -13.60685 | -45.77494 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 22ef9178-b064-361b-9a3a-89fe47415666 | -5.95752 | -44.78969 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 8da7237a-6ea0-370c-bbcd-832ae1e79869 | -8.08146 | -45.83218 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 46528eff-b516-30b8-88c3-b64924e2fde4 | -13.32308 | -46.90926 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 52651b8f-15da-320d-b546-7072581b2f61 | -6.57238 | -45.33011 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c0648d41-1398-3734-b41a-1ced29beb462 | -5.8704 | -43.59358 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 755bd801-a06b-3520-b179-b3a966e4f0b3 | -17.06773 | -45.40946 | 2026-08-28 16:05:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f0c3549f-b02c-31d2-aca7-ce0ab660c878 | -12.86413 | -44.35456 | 2026-08-28 16:05:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2dd3b35d-76a3-3e31-93ed-ffae86754109 | -16.45889 | -42.4372 | 2026-08-28 16:05:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a575d18-435e-30a2-b8e7-f1b3b27233f5 | -7.61094 | -45.83185 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 47986537-b875-316f-a475-0bfb407900b5 | -13.58501 | -45.77467 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5b08bbcb-7489-3871-8b5a-be68c35bd8fc | -8.46524 | -44.8106 | 2026-08-28 16:05:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ed8d388-bde8-3264-a64c-a3ff363ad900 | -17.54817 | -46.54394 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29328068-0bb8-3c3c-a2a0-2cc9d84be319 | -11.04959 | -37.61214 | 2026-08-28 16:05:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dd35e675-9265-3a3e-8609-c1ae334c718a | -5.59363 | -42.71973 | 2026-08-28 16:05:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 487cca43-2af9-3018-a955-0cee92d40a84 | -14.75225 | -40.66322 | 2026-08-28 16:05:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 89ecb32b-ae43-3555-aa52-9e6ff0b9cc9b | -8.08088 | -45.82792 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 786c02ea-7296-37e4-832b-55bf4d849055 | -14.08893 | -41.20568 | 2026-08-28 16:05:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e1a49809-360d-3c5e-bd45-613969e46ae9 | -6.83429 | -42.85281 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae781ed9-2e83-3171-964a-4fe16c268b35 | -14.19152 | -41.24281 | 2026-08-28 16:05:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6609b9af-5b1d-3bf9-958f-0a927f42dd24 | -14.20972 | -45.27936 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aae3d977-8c54-3cf5-a147-f07d18fc84dd | -7.31551 | -42.96193 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e4f98d89-f9a7-3329-a991-bf15f4e34be9 | -8.08644 | -45.83142 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 06d683ad-ebf3-34dc-b4c5-dc9bb4e433d3 | -8.07341 | -45.84808 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| c804b57c-9616-3bcc-bd42-0223d7f6eb73 | -19.59057 | -46.5402 | 2026-08-28 16:05:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0e750a5f-09a6-3a9e-a9cf-2ad21863f622 | -8.82816 | -49.64381 | 2026-08-28 16:05:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |


[Clique aqui para ver as próximas entradas](README93.md)
