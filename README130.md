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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcb23229-d568-33d6-933a-f42f68d07675 | -13.14826 | -48.53958 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 03c62816-5479-3087-a665-0e340ea73bc8 | -16.23444 | -41.53833 | 2026-09-28 17:07:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 079a175a-3bec-3690-bac1-af2b00f4ac59 | -24.73359 | -49.49268 | 2026-09-28 17:07:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 260da368-644a-3fc1-8f36-8e4cfbb68c1d | -17.16398 | -44.31638 | 2026-09-28 17:07:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f20377a-ac61-3c42-a055-8a7cd49f2c55 | -12.46248 | -45.19375 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2e345287-3596-3d15-8b10-7ebeec8d04d2 | -14.31753 | -44.82617 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a175ac21-a405-3aee-9716-e5f37b43c892 | -14.25056 | -41.29209 | 2026-09-28 17:07:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5b7c3ba9-20ab-3bf3-8eea-1d87e4e718cb | -12.70219 | -47.32915 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ab1c7b6b-82e9-3066-8978-67921bee28be | -21.29075 | -57.90364 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 61e6b108-ebd0-31ec-baff-1a8ab34050bc | -12.74405 | -47.29004 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0765c5fb-9163-381f-9c2c-9b03f4e96969 | -11.35508 | -43.36043 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 48ceba69-a799-3d02-84a7-e842632f47bc | -12.09907 | -45.22781 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2b28d950-fbbb-375f-ab7c-fda558799f2d | -15.25801 | -44.82266 | 2026-09-28 17:07:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d2bc69be-4ba7-3e5b-a11d-5763e1975ced | -15.75911 | -43.27575 | 2026-09-28 17:07:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| be18296d-50f1-3c4e-90ee-f853cfd1c0cb | -16.33772 | -53.11651 | 2026-09-28 17:07:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9eb2ce62-a274-3fae-9a7e-a01851b921cf | -16.34801 | -42.57482 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 2684a9a0-ea90-3087-b330-573edc4f5d93 | -13.19339 | -48.53668 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b31731af-85e2-3be2-9e18-247fa7534c66 | -24.63185 | -52.38568 | 2026-09-28 17:07:00 | NOAA-21 | RONCADOR | PARANÁ | Brasil | 4122503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| dfbe131b-3983-36ae-8353-996ab055525e | -18.00908 | -44.02881 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9d070c2-03a6-32a7-8f06-c48a7b7220a6 | -14.84383 | -41.47417 | 2026-09-28 17:07:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| eed71ab8-c47e-377f-a30c-cffd81dd0e9b | -12.978 | -51.09153 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| bc1775ca-299e-3f48-b8b3-848b9d283d15 | -13.69373 | -56.61037 | 2026-09-28 17:07:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 2015de6f-f0ef-3541-9631-15e37ddc2394 | -15.3716 | -39.77069 | 2026-09-28 17:07:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 4aebe7aa-5350-3073-a02f-b9dad911d027 | -16.5163 | -42.45268 | 2026-09-28 17:07:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 98f0ca31-5c52-3c47-860e-6adfbc94b58b | -17.89659 | -45.05564 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6644306a-0435-39b7-8c59-616e4ec79a9d | -14.63435 | -52.11943 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d81b31fc-9fd6-320b-ae9a-0b079e73e795 | -11.29421 | -43.53935 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d9f310aa-49da-3f61-9bec-9aaac2d988cd | -14.9951 | -47.85779 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3f03d644-60dc-366f-a245-b0a7a5a9b20b | -18.16413 | -48.01875 | 2026-09-28 17:07:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5ea94e82-2d33-3f0c-9eed-bb5a7b7f1c4f | -14.53175 | -48.30904 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 465f0074-c238-3fab-b446-43802d8431f4 | -13.3714 | -44.02234 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 68664d88-14f0-3a2f-bf0e-912ce7062b29 | -15.40114 | -47.9189 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f1f4b817-d652-3cec-a4d2-e5ce85d2b438 | -11.98269 | -41.98003 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| b03f4249-18d5-3f27-9e9a-3fbe616fa5b5 | -12.87311 | -44.81605 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2b5d7ce2-6e50-3b6c-9b16-5e6c9fdebb5f | -14.4503 | -40.74722 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 424c3cdb-f906-3c00-ad63-8fc452fd67e3 | -11.39224 | -43.42558 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 4ba7edcf-b86a-3e0a-8c3d-997f6b7d51d9 | -12.84137 | -43.39815 | 2026-09-28 17:07:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 858a4378-6a61-3713-915b-fe4c5b2684a7 | -15.07237 | -54.59592 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| a41996d6-6ba3-3a2c-adc7-94e10bd53fbf | -14.47089 | -47.05916 | 2026-09-28 17:07:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cf2e5564-a171-3631-bb2d-561c61745ce7 | -16.61963 | -41.51632 | 2026-09-28 17:07:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1727204f-e8d1-33bb-b660-920e224b3289 | -15.66949 | -41.63856 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 6699db10-ecfb-370b-8e91-3101391ad4f6 | -15.16345 | -43.60756 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.7 |
| a3882269-0da2-3ad5-8d53-b7d5c174e938 | -12.10301 | -45.22015 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1a8bea8c-8abf-34be-9ef9-20a2786ad9e9 | -17.32627 | -53.95588 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c1fe0d37-074a-35f9-b685-4a6f568fc5a2 | -14.32837 | -44.81292 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 775ea75d-9227-3a14-81c0-e2256d1c2ea1 | -13.17534 | -48.55359 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3726e07f-5903-3d88-9e55-929667265129 | -12.73801 | -47.28218 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e84e2ad0-9dbb-3b02-8e6b-a804fd1775a7 | -14.74859 | -45.65042 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1c02c885-3c52-3cef-89e8-c86c30d7565a | -19.41454 | -48.44089 | 2026-09-28 17:07:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 700b87d3-84f3-390f-afba-ea7492c46a95 | -12.68966 | -45.02129 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ef979e12-bdeb-3f70-9666-d0976877aee6 | -15.39908 | -47.90727 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 89d9c27a-5c89-39b6-9109-b0d1e76935c2 | -11.38226 | -43.43694 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0f013aaa-34a5-356b-a1cd-e9e060c69a26 | -11.90385 | -47.00907 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2842760b-68c7-39df-8878-3a26f0a8fe86 | -17.89919 | -45.04394 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b00dfc5-da03-3f59-8f27-365b3f248ffb | -13.4749 | -40.47197 | 2026-09-28 17:07:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5cc27611-3e50-3394-bfa5-e130f3d7d7ff | -15.73724 | -46.02544 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 3299ceb4-8422-3f98-9922-ef6c0fede8af | -13.06413 | -40.26308 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| d1168699-21bf-3173-bd02-c9b6e4c047ff | -17.1095 | -49.70939 | 2026-09-28 17:07:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5abc4596-ebd1-3c07-bf3d-34f116e72d54 | -15.15507 | -43.59422 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 606d95f5-b89b-3f43-9d76-f2f611f66cfe | -13.16025 | -48.56335 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5487be24-1af1-3910-8f4b-2fd9c81f66b4 | -12.2422 | -42.03555 | 2026-09-28 17:07:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| b3208dcd-565f-36a7-bd59-486b4baf6ee3 | -17.60992 | -42.54066 | 2026-09-28 17:07:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 43682ab9-c0c6-361b-b269-8f5ec33fbbd5 | -11.66512 | -43.53325 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4b45618a-6430-34a7-a5e3-a44cead0fdd5 | -15.40503 | -47.94078 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ef5f28ae-64b3-32bd-842a-ae9480355e31 | -15.02697 | -40.97839 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| cd806914-7160-349c-a9fc-e011f5d3fc7f | -12.10625 | -47.39838 | 2026-09-28 17:07:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6c080cf7-1f0f-3863-ae9f-ff3af1198fd5 | -13.93705 | -47.81837 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 15cac6af-22b2-3c83-beb1-1f5e19a3ac5e | -13.46612 | -48.58771 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2302d34f-9450-337e-b7cb-b6c5da822e0a | -11.52752 | -42.56253 | 2026-09-28 17:07:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 1a7a7c27-a485-3a31-8fea-b8c3708ef9f9 | -15.04463 | -48.03722 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 694b61ef-14ef-3474-aec2-daa2d3fb78e6 | -18.23096 | -42.12457 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 52dff609-7fe7-329b-ab15-a5c3a57c6d59 | -12.69854 | -47.33448 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 2f11ddd3-116b-3f16-84ab-87589f59e330 | -15.10794 | -53.90199 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 438219f3-174a-3f9b-a388-75fe0d6fb97c | -15.55623 | -47.92117 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0d418bab-a96d-364f-adb0-ea729015bf99 | -14.6383 | -52.12255 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b218b834-1a5d-3d37-906f-316db10606e4 | -13.70033 | -49.2257 | 2026-09-28 17:07:00 | NOAA-21 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7762135d-a2ea-3008-907d-a3f6a650f9a5 | -16.54413 | -50.5172 | 2026-09-28 17:07:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 98f7ab66-a9df-3434-856d-9b28e78d0aff | -14.64386 | -52.11403 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cb0833e8-fba0-3735-8c0f-8930f2d58215 | -15.16026 | -43.61955 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 1553e0d9-50d1-3e72-848e-f926782e26f8 | -12.69009 | -47.2609 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 30402a9f-2243-358d-bdf3-866ed50163e0 | -13.44271 | -48.62109 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4495cb8b-a055-3f09-a3bb-39176cb19746 | -11.54358 | -41.87299 | 2026-09-28 17:07:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6cc173f8-7d0f-3d37-9c7c-2d7333ae294e | -18.73816 | -49.20448 | 2026-09-28 17:07:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c7a207a-ccbc-3c9d-a11b-bc79bd8a967b | -13.31244 | -43.95364 | 2026-09-28 17:07:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 11657f6b-a7bb-3c0a-a24b-06a85897b900 | -15.15881 | -43.61966 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e881ec5e-057e-3cd9-a833-cd9bfecb8eea | -12.79785 | -50.59236 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3b8ef550-3dbe-32fe-963f-6a46dbce5c84 | -17.20854 | -42.21222 | 2026-09-28 17:07:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| d3cb6152-f23f-337a-8bb9-6ec804baa69d | -16.96499 | -46.30846 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 89c2fe6c-3059-3184-88e9-8554596f8f24 | -13.67982 | -41.0202 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 8182f810-ca1e-3160-8e31-3cd3e251a01b | -12.63212 | -41.88014 | 2026-09-28 17:07:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 703cd5a8-e53a-31f6-979a-384b21e0bcbb | -18.74641 | -48.22972 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7f6a63b4-1f22-3140-bac8-836b7cbc4117 | -14.23181 | -49.12701 | 2026-09-28 17:07:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a522da6d-fd29-3b8e-baf5-a897ba16026e | -15.78747 | -56.63369 | 2026-09-28 17:07:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0401a358-2589-33de-babc-25b010ad60f1 | -15.1534 | -43.62082 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 36.6 |
| fb929d91-e355-333d-994a-74e27d4dc8c5 | -12.98325 | -44.73909 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 521b56fa-9939-3ef2-a2d4-88f2d4e06bbf | -11.37383 | -43.42497 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6b6caa7e-bb0e-3e41-b7d6-b0c4f4a51166 | -13.42608 | -43.74693 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09793f7a-3584-3d02-b382-afe0bab71630 | -12.75457 | -47.2972 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 204f018d-7570-38d3-a04d-54a9a28f8bbe | -13.40335 | -43.4507 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5f6df994-fb9f-3b7e-be3a-ef6e938b68b6 | -11.40066 | -43.43757 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |


[Clique aqui para ver as próximas entradas](README131.md)
