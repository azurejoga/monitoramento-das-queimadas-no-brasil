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
| 76b5c416-8805-36f7-980c-c4434b04d80a | -7.82541 | -35.23605 | 2024-11-06 03:49:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5a516279-2904-3e8e-bc0f-a2c41f937304 | -8.50204 | -42.08779 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 578bc326-49bb-3f8b-a3c1-280ff975fc0f | -4.56177 | -48.00267 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0d293e7f-c892-3f40-ba7a-bd05beda2e89 | -7.25676 | -38.95047 | 2024-11-06 03:49:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 170a5036-b97f-34de-b8c1-8763816bc559 | -4.77162 | -48.68486 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ea340bb7-856e-3f0b-9dad-ff0bd7d39318 | -5.03899 | -46.0042 | 2024-11-06 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b648346e-f6c3-3217-9964-d6f718921527 | -6.50349 | -44.67555 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e3bafad7-0b4d-3213-93ef-59e7f2c48a84 | -6.49771 | -44.6801 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8fc3bda5-a55e-3fca-bbc0-cc6a6a485d75 | -8.79354 | -40.75193 | 2024-11-06 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 47d07183-71ca-3f0a-a72c-92d07f16a14c | -2.79272 | -48.57599 | 2024-11-06 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8e3c0681-e39f-3967-9691-23f83bb44936 | -6.50054 | -47.48708 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 3d0e09ba-efd2-3718-8ecf-c6cb4e6e14c0 | -6.91998 | -38.13505 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 02157114-5ae2-32cd-98d1-e7dff52383ae | -2.8231 | -48.55737 | 2024-11-06 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15596b19-d59f-3c96-aceb-063f04a303e1 | -3.8369 | -44.13367 | 2024-11-06 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fed72a48-50b4-379a-9da9-9d9970d1678a | -5.2308 | -44.91345 | 2024-11-06 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29e98c68-a83c-3ae7-a804-ebbc2b331372 | -3.52539 | -44.72334 | 2024-11-06 03:49:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f531817-f06a-39c4-ab6e-7f4e4434c274 | -5.12065 | -44.35557 | 2024-11-06 03:49:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 19b679b4-acda-3e9b-b6f9-5c8cd45d4d81 | -5.62363 | -43.94999 | 2024-11-06 03:49:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a88bf1b0-bf34-32cb-976d-319f6d83ff80 | -6.66109 | -47.87169 | 2024-11-06 03:49:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a78f837-9c57-36e9-b3af-e75f9308b1a3 | -4.82195 | -48.09846 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 56cd6537-a780-35cb-8363-3ade5af1e535 | -5.74096 | -35.55724 | 2024-11-06 03:49:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9279b987-8a30-36b8-867c-d99405d260d4 | -4.81899 | -48.56434 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3376a76b-6073-3bf3-afac-4189648210b6 | -6.12763 | -43.97661 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 91d27e19-07de-3753-ae82-10aa6f227c74 | -5.1495 | -43.77761 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9d10e88-d57e-3f1d-9433-bcbbda02db51 | -6.49323 | -47.49409 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| fc56e1bc-904b-3af8-b003-5685f51d2339 | -6.49904 | -47.4953 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 10347086-cf38-3ac6-8653-ce39d7e03b1b | -2.78819 | -48.57433 | 2024-11-06 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d60be5f3-b8db-3393-aad2-e1a83993bcaa | -7.03544 | -37.31797 | 2024-11-06 03:49:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bdaa05b-6d9e-33f2-b70d-708bb2072760 | -6.13313 | -43.97251 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c2968925-e2d4-3c4e-8c12-bf2d9c847d61 | -10.52425 | -42.40112 | 2024-11-06 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 936d8ba7-f4d9-3791-b912-dedfe543c06f | -8.5003 | -42.09827 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0ed034c8-6eaf-3723-970b-c73db0c2a877 | -3.75141 | -44.56492 | 2024-11-06 03:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcee56f0-6022-31e9-b59a-0ce23c73b69f | -2.85081 | -49.47588 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cb6ad358-3945-3d66-b9a1-4ba53a4ef8c4 | -3.21311 | -49.22963 | 2024-11-06 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ecaa231-3ca2-3b11-a151-6f12f9eccf4e | -5.2305 | -48.14216 | 2024-11-06 03:49:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a6d8891-9fcd-362c-a3dc-b860965f7339 | -6.50255 | -44.681 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 99ed70a8-935a-3736-8786-9f5fae9b4986 | -7.83139 | -35.03338 | 2024-11-06 03:49:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 30eea83e-7182-34ef-acee-92f14ce053b9 | -5.55771 | -43.70177 | 2024-11-06 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 25dda255-2e94-3bd5-a341-acc382a480bf | -3.76047 | -47.60115 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b08c2c58-8ee6-3a69-b5d8-5b1956a46da4 | -3.75896 | -45.93317 | 2024-11-06 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 054edf2a-9c62-3652-b3b6-01e68eb26772 | -3.24426 | -50.01562 | 2024-11-06 03:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfa4db3e-750d-3651-944a-34e57939c3c2 | -7.52873 | -42.86886 | 2024-11-06 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5bead77f-a89a-3851-b988-7585d4a2659e | -4.55979 | -48.00463 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| dab364e9-4cee-3017-a62e-5ece380bdaaf | -5.22643 | -44.91279 | 2024-11-06 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4369d0c-b7b0-3ab7-bc48-970ce57993b1 | -6.6134 | -41.65025 | 2024-11-06 03:49:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 51d49440-2a96-3f75-9249-32cd1b47b1b0 | -4.34868 | -46.52902 | 2024-11-06 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e263792-3ccc-300c-8bc0-c66e3f4dc39e | -5.89809 | -39.61493 | 2024-11-06 03:49:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 03ee9185-0073-309b-bb9a-7bada276a85b | -5.98837 | -45.3655 | 2024-11-06 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d5614956-f1dc-3605-bdea-e2b0d4d3355d | -6.85412 | -38.89831 | 2024-11-06 03:49:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb63f533-100b-39ef-9b1f-4c2b6e24e8c2 | -4.13041 | -43.56772 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7769a7c4-c145-3e15-a810-5527fce74d71 | -4.69326 | -45.64587 | 2024-11-06 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 294f8dbe-daf0-3962-961f-0e5e75d95f77 | -7.52895 | -40.14771 | 2024-11-06 03:49:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c3956db5-6261-3e47-a07f-e07a8aa727e8 | -4.14161 | -43.57338 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f75a4ed-ea40-3d60-a8b2-88424d66c28b | -6.25684 | -46.90416 | 2024-11-06 03:49:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59590e95-fb4a-34d2-bf8b-057a6c0d8d7c | -6.1407 | -43.96522 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| af90b496-f606-35d8-b85b-6ff86cfc261e | -5.65851 | -45.93715 | 2024-11-06 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9dd86cc-3d2c-386b-b5ca-cfbeae44643c | -4.82534 | -48.56581 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95854cf2-e00e-3fe0-be60-94eef4ab0c85 | -6.49651 | -47.48099 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 199d4685-b5c3-37e7-b1e3-b57758cd9b2d | -8.61401 | -40.88294 | 2024-11-06 03:49:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23d7f585-2ac2-3e4e-89f1-9b44682f3ae3 | -5.13677 | -37.38336 | 2024-11-06 03:49:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0d8d286e-1c92-350c-8df9-5a8c1d76a3b9 | -5.0629 | -44.23483 | 2024-11-06 03:49:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e06f583d-dfb6-3877-9f0a-815a2e96248b | -6.61735 | -41.65089 | 2024-11-06 03:49:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3b88090c-b524-3bb8-8a4b-159a5cf17eea | -5.66328 | -45.94144 | 2024-11-06 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4cb470be-147b-3e15-b4a0-6abb8c15dc41 | -5.13783 | -46.16167 | 2024-11-06 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeb7de85-56e9-3138-9e4c-3f1a4719a075 | -10.54749 | -45.14186 | 2024-11-06 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1bea7c88-598c-3281-a9fa-8fa72d35eac9 | -3.80323 | -44.03392 | 2024-11-06 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcd9de3d-12c2-355a-bea9-d86a4d1f9e26 | -10.46618 | -36.83565 | 2024-11-06 03:49:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fda81a9d-1cc1-3ec2-ae8d-df39bd73746e | -4.02522 | -45.66963 | 2024-11-06 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad90a374-030a-32eb-8b62-f8361d21792a | -6.12813 | -43.98323 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 217dcfc3-8d67-32dd-8915-7daac1d17df1 | -6.64771 | -37.3807 | 2024-11-06 03:49:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3bf4ef3-e9f6-3621-97f9-31ffb1446932 | -4.35937 | -46.53499 | 2024-11-06 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c2cbbac8-3ea5-3358-ab24-446f521d61fe | -4.14283 | -43.57999 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a60e38d5-d135-3993-958a-b66df282fac6 | -4.77161 | -48.68716 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9a58cdd5-b9c0-3027-b7c0-58064cc093eb | -8.05733 | -40.91737 | 2024-11-06 03:49:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 201a294b-fe3e-30c7-8831-a687c1c9bd13 | -4.09983 | -44.26164 | 2024-11-06 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea1e6fef-b5ff-3608-bcdd-ec210248072a | -11.87043 | -38.352 | 2024-11-06 03:49:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9b1ff323-ae93-3e00-a767-429a3ed517d4 | -6.95169 | -36.25888 | 2024-11-06 03:49:00 | NOAA-21 | OLIVEDOS | PARAÍBA | Brasil | 2510501 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 42c853f9-be01-383e-8128-2567a710d4c1 | -4.59248 | -44.04814 | 2024-11-06 03:49:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a46ba7d-4039-34ad-8245-46a4892a4acd | -5.83053 | -47.18861 | 2024-11-06 03:49:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f0f1b7b-d54f-3051-9620-189f62216fad | -3.83915 | -44.13597 | 2024-11-06 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 545822da-9700-3655-a1e1-cd538fd22bbc | -6.13946 | -43.96363 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8a1e7a15-daa9-398b-85b7-a8f4ca4372a4 | -4.12716 | -43.58766 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0d73b000-ec8a-3e87-ace8-aab8bd29d2d2 | -4.13896 | -43.5742 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b456dd9-7062-3761-b19d-c67d1dc14318 | -4.14078 | -43.57828 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c7620d6a-026c-3066-a156-42e022905b14 | -6.49508 | -47.48913 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| fb606774-fc7f-3ddf-a4c5-ef19d6fd3f06 | -7.79143 | -40.26951 | 2024-11-06 03:49:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11ab5e3a-9183-3651-a2e3-908e4e8a1e9b | -6.70448 | -37.47486 | 2024-11-06 03:49:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 096878de-5eb4-38fe-a59b-af2636846f67 | -6.26251 | -46.90506 | 2024-11-06 03:49:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad750416-d730-3bb5-84fe-92bb0b6d317c | -6.93737 | -47.78767 | 2024-11-06 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a644fd7-9dc1-39b1-87ea-46bd43d9ae8f | -8.61428 | -40.8839 | 2024-11-06 03:49:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7a87f54b-49c0-3a11-8788-8141d676de75 | -6.51194 | -44.13519 | 2024-11-06 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5b43499-6210-310e-a307-5d00442c8959 | -6.32467 | -39.51288 | 2024-11-06 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dec6d4be-f7f0-33b9-91c8-fc04811efb80 | -3.53792 | -47.39091 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2880fe17-616f-3cf1-8f70-066dfbd8f085 | -5.23585 | -48.14811 | 2024-11-06 03:49:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a02f076c-2d10-3e2a-b16a-5314fd3f13de | -7.01381 | -39.98972 | 2024-11-06 03:49:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 786ef141-79f5-3718-8ce7-b097cb3223c1 | -3.54716 | -47.37352 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe8d8bf7-8906-3ffb-a128-35eaed150151 | -11.52223 | -41.41594 | 2024-11-06 03:49:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45c3c5aa-1b83-3ee2-95ab-f45d6433ccbc | -3.75837 | -45.93504 | 2024-11-06 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e18de9e-13dd-374a-aa30-ea4cbf2d5c65 | -6.954 | -47.86533 | 2024-11-06 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3a21c3a-5b34-3b26-8959-172a137e7b7a | -3.54643 | -47.37778 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |


[Clique aqui para ver as próximas entradas](README25.md)
