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

## Dados Diários - Página 308

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 111daf08-bb0d-331b-8dc5-ae1432262307 | -15.82945 | -40.48381 | 2026-10-08 16:35:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| e9299226-d132-3e8f-98fa-ab553a80674c | -16.29312 | -49.14359 | 2026-10-08 16:35:00 | NOAA-20 | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b83b7d85-6ef7-30e0-a914-9f9c061a5d64 | -15.63102 | -40.13154 | 2026-10-08 16:35:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 2ad62dbf-9f3b-3bd2-b940-ea87022050cd | -14.98577 | -39.49894 | 2026-10-08 16:35:00 | NOAA-20 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 7b53564e-3403-3000-a1f8-554baeadfb76 | -15.62806 | -40.13647 | 2026-10-08 16:35:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 36.9 |
| 28297228-73af-39a6-a64b-cb4e4aecc7e6 | -24.8682 | -51.99212 | 2026-10-08 16:35:00 | NOAA-20 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3b1f6350-3f6d-3928-a19d-eb41d75c93f0 | -13.86832 | -44.05319 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6745ea12-b6eb-333d-a5cd-f695bab700db | -19.95905 | -42.1369 | 2026-10-08 16:35:00 | NOAA-20 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d3885c9f-5d7c-37bf-9691-2ccd0bfae2a5 | -14.60123 | -44.9076 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49c74e9a-f7d8-3f6f-abbb-197c2ab69b66 | -19.60488 | -40.10717 | 2026-10-08 16:35:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 71599d7e-7019-3370-b199-2915f884464b | -14.2453 | -44.4346 | 2026-10-08 16:35:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1018f465-76c5-3f09-a1d1-9d172206f080 | -16.97713 | -41.23158 | 2026-10-08 16:35:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| c1c3e188-58ba-3fed-9141-a2d975d86f93 | -14.45252 | -41.20117 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 31.6 |
| df36a48c-0504-39cd-a8ce-cc6d7a8e144a | -14.46993 | -40.72204 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 84e35eb0-3229-314a-9c3e-9226226ff5ae | -15.45661 | -39.76615 | 2026-10-08 16:35:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| f84fbd5f-5a56-3ece-8ac1-142a713565bb | -14.75035 | -47.13952 | 2026-10-08 16:35:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 995a80dd-9c59-3880-bbbd-4b37594cb1b7 | -15.98969 | -53.70299 | 2026-10-08 16:35:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 08c5a859-a5ce-3e62-b04c-9c633711b6ca | -15.90153 | -50.69839 | 2026-10-08 16:35:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b711f182-9bb0-3bf4-9fda-2e151f3b48ba | -15.24024 | -50.25917 | 2026-10-08 16:35:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 942bcdc4-d423-3256-ad74-1edcd741dff7 | -14.10831 | -41.86129 | 2026-10-08 16:35:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 08f0506d-5413-3b54-b90f-16e0cb7fd6a8 | -14.82017 | -40.50718 | 2026-10-08 16:35:00 | NOAA-20 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4181a2c0-1357-3119-aaa1-8922a2c68870 | -15.57196 | -44.52911 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c8389559-adb5-30a1-900c-811146cf2370 | -15.39111 | -44.34135 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ec28a85a-67fb-3d1e-88e7-8188edcc3e40 | -16.12783 | -43.7424 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d6d9c47a-a76d-32da-b70e-dc30bf45f574 | -13.58695 | -39.77989 | 2026-10-08 16:35:00 | NOAA-20 | WENCESLAU GUIMARÃES | BAHIA | Brasil | 2933505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 78485907-5103-385a-bdde-dea2d82840e0 | -20.76736 | -42.22847 | 2026-10-08 16:35:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 76d44d5d-5718-3792-8904-87153c29fdbe | -15.47883 | -41.00634 | 2026-10-08 16:35:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 6737a775-6257-310f-8f99-3f823f662487 | -15.4033 | -44.33207 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 77e0d48b-0141-3feb-b654-7b37c1d011a0 | -15.24773 | -47.99398 | 2026-10-08 16:35:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cfc2564c-b365-3b95-a016-b50116908cf1 | -16.02943 | -45.12905 | 2026-10-08 16:35:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fe1e337b-a225-3b72-ac06-3fa0ff398765 | -14.80556 | -45.37057 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bc5aef05-4bd1-304f-bbf1-4c89e2d728ab | -15.68699 | -40.7757 | 2026-10-08 16:35:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9982dba8-daf9-3b6b-b19e-51732417757b | -15.70421 | -40.592 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| a8ad0529-87a2-39cc-ad5d-6059cb0fdcf3 | -16.81923 | -40.39197 | 2026-10-08 16:35:00 | NOAA-20 | PALMÓPOLIS | MINAS GERAIS | Brasil | 3146750 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.4 |
| e1f1587e-9c28-3125-b684-aa70b74a614c | -15.86047 | -40.79615 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 310a91e6-94b4-38c4-a4e6-291e7996f6e9 | -22.96265 | -52.58141 | 2026-10-08 16:35:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f3f2b94c-eb5a-395a-8a77-e341f4968bb0 | -15.40052 | -44.33618 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c0a16172-7b44-3e62-b960-e954ebc3d37e | -14.67496 | -42.48111 | 2026-10-08 16:35:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2efab78d-0dc5-3f86-b966-8e75f2713360 | -15.79477 | -44.68219 | 2026-10-08 16:35:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 7b51acd7-e573-39e7-af37-1fb2fed2c4bf | -20.33841 | -40.93129 | 2026-10-08 16:35:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3face225-b57b-38a2-ab60-8b2d1151bdee | -16.71831 | -44.89867 | 2026-10-08 16:35:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4443fb9d-02cf-3926-84f1-21d1da68ba62 | -14.6393 | -44.95697 | 2026-10-08 16:35:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac6da829-a440-3d2c-9337-1b5d85e21235 | -14.13718 | -40.79454 | 2026-10-08 16:35:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 33.9 |
| b577b5c4-5cc8-3b18-9cc8-d2126ae77987 | -15.50905 | -49.57024 | 2026-10-08 16:35:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ea5aa3c2-b628-3c38-9eb0-46f8021cbdf3 | -16.09317 | -53.01914 | 2026-10-08 16:35:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43c67025-c6c0-38af-9cdb-e8f475ab4f4f | -15.69081 | -40.46674 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a8cf228f-c254-30b9-a8ef-b4e6a666bc34 | -15.11049 | -43.63482 | 2026-10-08 16:35:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 168.4 |
| 9f2bc1d1-3012-37e2-b253-5e31f59ce7cf | -15.54439 | -43.17176 | 2026-10-08 16:35:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 14411387-915c-3a06-a740-0282f39ed59a | -15.26065 | -42.34687 | 2026-10-08 16:35:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c22c4698-f61e-31b0-8f8b-3884136ba223 | -16.12893 | -43.74957 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ec903b28-6c7d-3a5e-b473-84ab947c9eb6 | -14.4084 | -41.28467 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 5fb492e2-4bdb-3a9b-9844-4b04472e83a7 | -14.47137 | -41.249 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| ad5a7673-258d-3453-9ca3-9a37c87730c0 | -14.27459 | -40.39114 | 2026-10-08 16:35:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| e07c4331-3ecc-3264-8cad-e1134bb354b8 | -15.54863 | -42.35493 | 2026-10-08 16:35:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f729f3c-fde6-3821-8e9f-f4dbd373ac97 | -15.5609 | -44.52347 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0988b759-cc59-32b1-897b-f555b9159bc6 | -16.31894 | -44.5601 | 2026-10-08 16:35:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1494eb9f-b645-318b-97b9-2f229b236db6 | -15.63288 | -40.12779 | 2026-10-08 16:35:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 29a4d2da-7961-3e80-9cd9-2c62a1375b7c | -17.367 | -45.44217 | 2026-10-08 16:35:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58116e63-21a7-354d-861c-66838fa4aa56 | -15.06457 | -41.35263 | 2026-10-08 16:35:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 21d750a0-c4ac-3fd5-9443-d10c1037a14a | -15.68344 | -40.77637 | 2026-10-08 16:35:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| c2b85cf6-e6ae-3154-adee-e883cd5b0ea1 | -14.9845 | -39.50166 | 2026-10-08 16:35:00 | NOAA-20 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 61419d22-4fae-3939-b95e-e1b0e9fb0b8a | -15.85839 | -40.80059 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 2b6af419-5f0e-3a59-9380-135f3c8217c8 | -17.00524 | -42.37956 | 2026-10-08 16:35:00 | NOAA-20 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 052a671b-a8b6-3c28-aeda-afd4f2649641 | -15.1138 | -43.63428 | 2026-10-08 16:35:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 32.2 |
| abd86575-cbbd-3b91-a432-24f2dba1a4fe | -16.24583 | -41.73795 | 2026-10-08 16:35:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| cec94d80-2d51-3e97-b292-785427dea641 | -15.11215 | -43.62358 | 2026-10-08 16:35:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.3 |
| af3a7a03-bfd0-36e0-84ce-449cef2f9612 | -13.95866 | -44.84932 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 78dc22ec-6e83-3e40-b234-141e575e52e5 | -14.55669 | -44.07341 | 2026-10-08 16:35:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 2700166c-17b3-3e54-8be6-4ee5b1d830ae | -16.43455 | -40.2683 | 2026-10-08 16:35:00 | NOAA-20 | SANTO ANTÔNIO DO JACINTO | MINAS GERAIS | Brasil | 3160306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1489a7b1-db44-39cb-b5a7-9a4582a2980d | -16.05329 | -40.64993 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| c58d758d-59c2-3d47-a3b9-c67ae436cee3 | -14.75395 | -47.13898 | 2026-10-08 16:35:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c854a127-a0d7-3e4b-9619-009c894c2b81 | -17.10874 | -41.34917 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 723f467c-12b4-3164-bbdb-a73169fe4820 | -13.72881 | -39.00336 | 2026-10-08 16:35:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 658f32e1-bfa5-39df-8a5d-82c96f58efd1 | -22.56617 | -46.59855 | 2026-10-08 16:35:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ff8bf524-dee9-3832-9e71-f0891fc7ab5d | -14.56001 | -44.07288 | 2026-10-08 16:35:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 8954743b-7d8b-3d6a-82cb-874a411c9540 | -17.96332 | -47.7032 | 2026-10-08 16:35:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 98d99ca9-3a64-3484-be64-2d2d0b7172f0 | -14.99828 | -44.05482 | 2026-10-08 16:35:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 43.0 |
| e5fa15df-5ab9-3ae2-8d8a-0d0cf25d76c7 | -16.41719 | -50.49234 | 2026-10-08 16:35:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 95c1c165-fb4d-3e57-85ba-0edbff5f9348 | -16.97647 | -41.2276 | 2026-10-08 16:35:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| fabcc677-a301-3034-b0f1-40dac046bdc3 | -15.95318 | -41.08867 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 05251bc4-bb80-3b89-9b4d-b1479cead1a2 | -15.57189 | -42.89293 | 2026-10-08 16:35:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 91d3ef02-78b0-3ad6-ab6f-4ea96af4ccf5 | -17.38719 | -52.11837 | 2026-10-08 16:35:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2e1e651c-171b-32e3-8d4c-bb337cd264b7 | -16.93826 | -42.07885 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| e946994b-ef04-3702-a454-e34503ff2a00 | -23.02443 | -52.4679 | 2026-10-08 16:35:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| da09b860-3da3-313a-9cc2-6c78bb143ed6 | -16.13169 | -43.74545 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 34b39669-5698-395b-95e4-40aeb6dc3129 | -16.20628 | -40.1637 | 2026-10-08 16:35:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bacc8b57-63d7-3cd8-ba4f-21633a2b866c | -14.75772 | -39.81457 | 2026-10-08 16:35:00 | NOAA-20 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9f15a732-0e56-332f-a7bf-22c788f2d6b7 | -14.54011 | -41.77633 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 4a85ccf3-4456-3c46-9769-5060d5df343d | -16.92953 | -42.11094 | 2026-10-08 16:35:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e475e1c1-89f3-3e58-82d3-a37fdb854c1b | -16.14826 | -43.74274 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d19804f2-54a2-371b-83ad-3f7b131612fb | -14.62119 | -41.88291 | 2026-10-08 16:35:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 3d7303cd-dc31-3ad4-9c01-f9cb9453e2c8 | -14.05768 | -43.54391 | 2026-10-08 16:35:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f3503df-1054-32d6-9b02-304e2f78adef | -15.3933 | -40.70722 | 2026-10-08 16:35:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 772e0d4f-6db4-3e65-b61d-c2a1c013228a | -13.77117 | -39.74855 | 2026-10-08 16:35:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 268542e3-b367-3a6b-bc0f-2ab3cdf20edf | -14.05016 | -43.82314 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| e4fdb438-83d0-3b90-b858-70f07dc08bf5 | -14.43971 | -43.92904 | 2026-10-08 16:35:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 362dcb81-7a8e-3afa-9392-ab953ffd1040 | -15.95237 | -41.10553 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 9048c050-ef45-3cc0-b55b-b719b658acff | -14.05071 | -43.82669 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| a7d87c24-ee78-380d-b712-f1f330534660 | -14.99136 | -40.47717 | 2026-10-08 16:35:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 467f80e1-6d3f-3dc1-a090-3b4f29160242 | -21.70363 | -56.00481 | 2026-10-08 16:35:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README309.md)
