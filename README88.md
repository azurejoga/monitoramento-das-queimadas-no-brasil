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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37889b2c-7d8e-325e-8077-e1734d6a1bf9 | -14.60769 | -41.10667 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 476ec896-7669-336b-8c6a-9e68edbb028a | -14.63351 | -40.70523 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 2eb114f8-5f75-376b-ad1b-12ee1dd3f785 | -8.84148 | -41.12555 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 4bf208ea-b643-3af2-bd63-5d7c9a557df7 | -13.37133 | -44.00072 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 90e66b2e-cc2b-3806-98d3-bc49e2f56bf3 | -15.15867 | -43.57294 | 2026-09-29 15:46:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 09b221bf-9915-31da-b837-d33c8ee701da | -11.65941 | -43.52182 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| af136719-ce1f-31bd-816f-b052da84da0d | -13.32875 | -42.69554 | 2026-09-29 15:46:00 | NPP-375 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 273b52d1-5074-3f21-88c1-e116289e8f2e | -12.75018 | -38.21894 | 2026-09-29 15:46:00 | NPP-375 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 1381268e-6490-3ab7-acd0-27c707ddc103 | -13.22387 | -42.53759 | 2026-09-29 15:46:00 | NPP-375 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a22a3c61-5570-3417-8625-9ed0a6230984 | -11.43036 | -43.47422 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1baae14d-497d-3296-8156-f6fa38ff6ad6 | -11.26492 | -43.54887 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 29f12fe1-2074-3529-b28b-68e2c841c9a3 | -15.54909 | -40.75101 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 16ff7060-dab9-3c40-844f-996927c46d8f | -11.6761 | -43.54609 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 9d203b7f-5684-3825-870a-4299da8a0092 | -14.09518 | -41.39031 | 2026-09-29 15:46:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f129e6b7-057b-398a-b0f0-15419fc9ca89 | -15.06572 | -41.94248 | 2026-09-29 15:46:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 4a5e823c-0cd8-309c-b18d-18785b7a277a | -11.44252 | -43.45226 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 1e14a6ea-3a8e-3d9d-ae44-a4fd03d542fd | -11.63116 | -43.51982 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| ef0d7217-9aeb-3679-b8df-68f4c5285b01 | -8.98949 | -44.15492 | 2026-09-29 15:46:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9ebfd49c-eefd-3d6c-b232-dee86b9ab390 | -11.61274 | -44.14613 | 2026-09-29 15:46:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 108009a7-14a4-310e-bfcf-3542295280a4 | -14.43204 | -41.13801 | 2026-09-29 15:46:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8f70f5b2-387c-3cf7-9fe7-0d1eae747f66 | -8.98869 | -44.14817 | 2026-09-29 15:46:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 730affb6-7383-3093-8322-a69df61d1976 | -11.65192 | -43.51768 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f75d4014-ab4c-36e2-af4e-bb061e444e24 | -15.70564 | -40.59618 | 2026-09-29 15:46:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 5c851d61-5ba3-3fa2-bc44-ba606b1fe5ab | -11.41846 | -43.42313 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 1a031784-e12c-3daf-b46f-5b86b1ef9bc9 | -11.64418 | -43.51056 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4ece98ac-3820-3efd-bca1-26c556631203 | -14.60419 | -40.77467 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| e1424561-1ebf-349c-81c6-c009522714bc | -10.11505 | -43.92287 | 2026-09-29 15:46:00 | NPP-375 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 149a29ee-8357-3169-93c1-732a8712bee2 | -15.16337 | -43.57321 | 2026-09-29 15:46:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6be860a6-8a9d-3dbc-8032-db20b7dd3688 | -11.41091 | -43.41763 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 9763241f-0754-3d21-9ebb-7b97e992aad9 | -9.79822 | -44.82759 | 2026-09-29 15:46:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| cc447600-2b7c-356d-8159-6c5d7646e0e5 | -11.41227 | -43.43009 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 902eeb6e-89e8-30e8-bd7c-434a21ba6484 | -9.44466 | -41.82039 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ff0c7e1f-66c5-3608-9772-64a84f68f9e9 | -15.98278 | -43.00774 | 2026-09-29 15:46:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7520b249-c9e9-379d-bba4-8dbd2eae82ff | -14.67464 | -42.84188 | 2026-09-29 15:46:00 | NPP-375 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 92466c6b-31e8-340a-b3c1-f23f850cc469 | -9.61097 | -41.61442 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 88af88c4-062a-3bc0-bd00-8692547f5eec | -15.5343 | -40.84692 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 39.0 |
| ab012698-7304-363a-a1e4-0daad4803047 | -12.32164 | -39.06232 | 2026-09-29 15:46:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 57c1d839-332d-3077-85cd-af63feaa4ea7 | -9.44522 | -41.82499 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ab8efa1a-0878-3194-a452-3bbfe947847b | -11.62897 | -43.50071 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 6e0677a2-a6aa-33c2-8ecf-eed58bee28a2 | -13.4789 | -42.48123 | 2026-09-29 15:46:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| bc8c7d96-653e-3a44-b4a2-586c4dd5e403 | -15.5055 | -42.87667 | 2026-09-29 15:46:00 | NPP-375 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| dda16a2f-3857-3ed5-b007-7dc2b9b54290 | -14.66182 | -41.32642 | 2026-09-29 15:46:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 4090952f-dbcb-3abf-a334-e7c2ed790fa4 | -11.3134 | -43.55132 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 49f21280-c77e-38a2-ae4c-195ff0064d7b | -14.26794 | -41.39588 | 2026-09-29 15:46:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 59f09540-dee2-3c80-8d6f-a33f159637c4 | -13.37281 | -44.01562 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 513f80f0-f3c7-3b34-b92d-2453c5c329ba | -8.37302 | -36.96001 | 2026-09-29 15:46:00 | NPP-375 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7a71b139-c59a-3bd2-b8d3-f35810478638 | -12.44094 | -44.14157 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 81d2a34e-1d03-3d8a-a20c-69086db02f0a | -10.28887 | -44.63006 | 2026-09-29 15:46:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 372c7274-8788-34e3-8242-95d749d189da | -14.71513 | -41.5939 | 2026-09-29 15:46:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4057d1bd-57e3-3e0d-9f77-cda06625196f | -11.63035 | -43.51208 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 3c6e4684-8e40-3b86-8eba-8058010d702d | -9.87583 | -43.62217 | 2026-09-29 15:46:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b6f6a52a-36d5-36a5-9d4c-86dc876a72cc | -12.48223 | -40.20703 | 2026-09-29 15:46:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 710c6d06-4667-3b31-a950-e18e4291a8f0 | -11.61668 | -43.3218 | 2026-09-29 15:46:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bfb19eba-a5c0-3c28-b982-1c7efc8b7a26 | -8.05773 | -37.78768 | 2026-09-29 15:46:00 | NPP-375 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| b874d6be-ebe9-3d48-b2fe-46487b958a40 | -15.30414 | -41.77218 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| 934ae797-442e-37ef-9656-2ef39689f0ba | -11.40123 | -43.45647 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 54fcd617-481d-39c0-b3fa-41be87ef7666 | -15.22814 | -41.73937 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| 827df5ae-63ce-3e1b-8245-ca3d35b8d9f4 | -11.83579 | -42.10999 | 2026-09-29 15:46:00 | NPP-375 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 90fb362f-9908-3a59-b89a-5d69a6431c77 | -11.30771 | -43.55637 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 91527d24-c300-35c2-beb1-1fb7338cadab | -8.31112 | -39.37946 | 2026-09-29 15:46:00 | NPP-375 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 290ea121-3207-3879-856c-1ba7e4f2f5ce | -11.41513 | -43.46301 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 167e43ab-250f-32da-a1f4-038d3708f069 | -11.4336 | -43.44223 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 09b1ca77-406f-3289-9a9e-7975267110f3 | -10.48728 | -39.52606 | 2026-09-29 15:46:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d0a65723-2bd7-30d0-be83-5768731c92a2 | -13.67687 | -41.01837 | 2026-09-29 15:46:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 7d92ed79-ff21-3894-bff9-9fad079ed947 | -11.26278 | -43.52986 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 81dae361-2f27-3ae8-b5e1-ebfdb9375c43 | -9.42509 | -37.77264 | 2026-09-29 15:46:00 | NPP-375 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b7bfdf7a-8ee0-326d-aef3-948d2edf23fa | -11.27038 | -43.53539 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 8807656f-c0f2-3866-8fb1-be5d4d63918a | -15.22945 | -41.74748 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 157.5 |
| 8fd0e477-fb91-3169-a139-adb909a5386f | -11.44194 | -43.45401 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 544cb534-f293-39c3-b450-b87b3c443ade | -13.52375 | -40.71648 | 2026-09-29 15:46:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 02abf8d5-1adf-3b48-8e4a-a1929ef73416 | -13.53458 | -39.95969 | 2026-09-29 15:46:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9e46865e-aa11-3b58-b307-879ec1c88fd6 | -13.35238 | -40.67153 | 2026-09-29 15:46:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b8e1ac63-2744-3e37-a7d3-052641955049 | -8.65685 | -39.26053 | 2026-09-29 15:46:00 | NPP-375 | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ec183fd-c387-3acf-8c0f-c11bddbb61b5 | -11.7221 | -43.45678 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 0879bfb5-60eb-3084-ad29-43be5aa71e02 | -15.08434 | -41.4147 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 471e3ef0-04fd-39d2-b6bf-a7f4dff96584 | -9.05895 | -45.00833 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9dd29560-4995-3d67-a581-8b5bbd2f4c29 | -14.15527 | -41.03146 | 2026-09-29 15:46:00 | NPP-375 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dce1072d-f616-3a9e-99cf-dbf2373ed807 | -16.16384 | -42.8519 | 2026-09-29 15:46:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 319c9cc2-0313-3aee-9698-a7abf891d77c | -11.66491 | -42.61496 | 2026-09-29 15:46:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e85e8919-298b-399f-bb3b-479de8f45942 | -13.33739 | -43.95316 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b56b7077-d314-3fe1-a010-8e0a42402399 | -14.65602 | -41.33176 | 2026-09-29 15:46:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| a68aec3d-2546-3b9d-8a2c-a3452c71c25a | -11.42395 | -43.4733 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| d124a004-a2e1-3fea-86b3-607052d47c25 | -12.4417 | -44.14895 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 0c10934c-05fa-3645-a237-fa0e06403671 | -11.31418 | -40.6604 | 2026-09-29 15:46:00 | NPP-375 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d973275a-dd11-3525-b14c-8cc2dfc937e6 | -12.22331 | -38.90885 | 2026-09-29 15:46:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1ffd1f0f-2fce-3074-be1a-f4f41c795a18 | -16.15695 | -42.85358 | 2026-09-29 15:46:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 88d2c950-a387-364b-9aed-4df89868276b | -14.38998 | -41.37132 | 2026-09-29 15:46:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 56edb9ce-e713-38a3-8ed5-c914ac6e605d | -8.3705 | -36.96072 | 2026-09-29 15:46:00 | NPP-375 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 19503b29-1c2d-3169-a6b2-e0674b5adde9 | -11.71475 | -43.45879 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 96956c83-d74e-3582-95b8-280383c5fe07 | -11.42526 | -43.43039 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 15f2186c-24a4-355e-805c-41387350a303 | -13.85543 | -43.94611 | 2026-09-29 15:46:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 948cc127-25b8-3b6b-a9ca-06f46db706df | -11.26966 | -43.529 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b20307c6-8468-3a1d-9446-ab6793f4515e | -14.61387 | -41.10583 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1dc2443f-6fcd-30b1-a121-2b487ee0f3be | -14.24218 | -41.30667 | 2026-09-29 15:46:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 7b863ed7-fea7-3068-b3fd-6a1d413002b9 | -15.30342 | -41.77238 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 34048898-b9ea-3190-950d-433a6b5fa054 | -14.51773 | -40.77481 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b0d34acf-1198-33e4-b8d5-6e6ea2451297 | -15.54113 | -40.61319 | 2026-09-29 15:46:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 6a26221f-60fc-3992-bcb0-08c0ca51b11c | -8.21771 | -36.29053 | 2026-09-29 15:46:00 | NPP-375 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8b1a8b77-4d63-3f91-a06a-268b459d765f | -11.28488 | -43.54006 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e3078bac-f108-3628-95dc-327ec73c5174 | -14.16141 | -41.03089 | 2026-09-29 15:46:00 | NPP-375 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |


[Clique aqui para ver as próximas entradas](README89.md)
