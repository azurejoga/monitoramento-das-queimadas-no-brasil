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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16d31d98-c728-3c4e-becf-fac463fd0a2a | -9.0084 | -40.69614 | 2025-12-26 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a51b7b12-5b7a-3f16-97f0-5e4b2d015dcf | -6.39111 | -35.20518 | 2025-12-26 04:08:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c0c033f9-291c-30cd-8682-8fc05f330a68 | -8.75005 | -38.87734 | 2025-12-26 04:08:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd4537dc-3908-30ea-9877-5368de6dc54d | -8.47904 | -38.55656 | 2025-12-26 04:08:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23bb4aa2-8cb2-339c-bf3d-fd922b4a1638 | -5.13291 | -38.91411 | 2025-12-26 04:08:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b1b8960f-26b7-30dc-b875-b85a321f2cd4 | -9.30078 | -38.19835 | 2025-12-26 04:08:00 | NOAA-21 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0f9a8dd6-1213-301d-8dac-717dd45fe8be | -2.36723 | -51.90987 | 2025-12-26 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5602449a-3b16-3015-963d-8a37948e7dee | -9.94903 | -36.41101 | 2025-12-26 04:08:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 6d45a293-01f1-320b-82a1-bcc7b5584377 | -8.09933 | -40.19457 | 2025-12-26 04:08:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7f87035e-4bfa-37c8-bc14-cc26d50b3a42 | -4.57426 | -38.37799 | 2025-12-26 04:08:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65a1cf7b-1be0-3bad-9204-bda1fa9ed9a3 | -9.38083 | -40.55001 | 2025-12-26 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2f6b9e77-dea5-30f0-91f5-a7830cb54415 | -5.04066 | -40.86089 | 2025-12-26 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5420c4be-393c-3295-bd24-e49de0f12e2b | -9.28456 | -40.44424 | 2025-12-26 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 069949b3-f410-39bf-b0fa-1914b0742b42 | -5.92879 | -43.51424 | 2025-12-26 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db6f6e43-d20d-3332-a09a-e05511507c26 | -2.37411 | -51.90617 | 2025-12-26 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0693f588-0c00-3048-9b78-75574079d3c0 | -5.66543 | -39.48462 | 2025-12-26 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6bc0786c-96c3-35d5-970e-199749d61840 | -5.34232 | -37.03809 | 2025-12-26 04:08:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b01acd39-1005-3415-b882-6501ea8c073b | -5.3933 | -36.80059 | 2025-12-26 04:08:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| cc0348df-dfe5-360d-be8f-0957cf25041c | -11.84163 | -43.78987 | 2025-12-26 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36cd8b3a-6875-3c04-b8e3-f65d59c138dd | -16.14375 | -43.55741 | 2025-12-26 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 706df4f5-9099-3a0a-9b76-213d3d3f65fa | -11.84439 | -43.79398 | 2025-12-26 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40cbb90f-3648-3994-b513-e7c43cf81617 | -13.60973 | -43.56137 | 2025-12-26 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4633a9a-e618-3c04-866f-ffd942813668 | -16.16197 | -48.23987 | 2025-12-26 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cf7818e-c151-32fc-a16a-e6fb0ce96f55 | -11.84773 | -43.79453 | 2025-12-26 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c407ff0a-ee46-347b-b223-e26bbee78188 | -12.07626 | -38.98329 | 2025-12-26 04:10:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ef63cc3-b6d3-39a3-972d-dfa114c8452e | -12.07742 | -38.98087 | 2025-12-26 04:10:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 474893c4-b25f-38fb-8f75-e573ad2981b9 | -14.30309 | -57.58796 | 2025-12-26 04:10:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bda27adb-0421-3006-9208-a227b0af1d83 | -13.66987 | -46.27849 | 2025-12-26 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19cf0baa-710e-387c-b3e9-0f9d648ce228 | -16.10742 | -43.46314 | 2025-12-26 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70b63bdf-f0a0-3524-92fb-2ae1284fe7a9 | -14.29814 | -57.58744 | 2025-12-26 04:10:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 602bfa6d-061c-36d8-bc43-a804d5be91ec | -13.60917 | -43.56491 | 2025-12-26 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cc86c41-dd88-39bb-9dc4-e1e3be881851 | -13.3863 | -40.0496 | 2025-12-26 04:10:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f3b0b7ea-2626-375d-ac7b-124f4d314973 | -17.31121 | -44.92992 | 2025-12-26 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5100d2da-8786-38aa-8b2a-43be73570781 | -16.07168 | -42.00218 | 2025-12-26 04:10:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cfbd8f38-c0bc-3248-b8a8-0474b6bc8f17 | -11.84716 | -43.79809 | 2025-12-26 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d34b796-0c60-37d0-b86b-24235f98db32 | -13.36185 | -41.33929 | 2025-12-26 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5cd906d3-5cbb-3ff1-9792-9cf891c8c853 | -15.43063 | -43.24565 | 2025-12-26 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b9bf97c-85e9-3754-819d-dd9efff74cd8 | -14.29601 | -57.58682 | 2025-12-26 04:10:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ccd1e40a-451e-3352-aef3-65982dbfa90f | -16.14044 | -43.55686 | 2025-12-26 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc899e9f-a8b4-343d-8e51-5c2c726fdd15 | -11.8483 | -43.79095 | 2025-12-26 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7126207-33a0-37c8-a7d5-ac7304211eaf | -11.84496 | -43.79041 | 2025-12-26 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9ebb5fc-8a57-3b9f-ae1c-03cf21ad2878 | -14.30521 | -57.58858 | 2025-12-26 04:10:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2798777-f818-3c2e-af1c-b7b8821ee59c | -17.9377 | -41.76129 | 2025-12-26 04:10:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67ad14d4-f0a5-3ed3-bb02-fe20c078b907 | -16.13988 | -43.56044 | 2025-12-26 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83271fa0-197b-3a32-a955-7c0bfd11a0e8 | -13.49019 | -43.69373 | 2025-12-26 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cb428fe-1bc2-3db1-8653-8b252a18f514 | -20.19938 | -43.62232 | 2025-12-26 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a0f3e8a7-b402-34a0-8124-8c20c9d2d9f8 | -19.32617 | -49.38241 | 2025-12-26 04:12:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e72280c6-6479-32a4-b53d-2abac631e4d0 | -20.19772 | -43.63342 | 2025-12-26 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 636d9b30-4d87-36af-b9ef-6be8b878996c | -21.56047 | -42.18996 | 2025-12-26 04:12:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3d35a125-7595-31b4-9dd2-049fdb0b97c9 | -16.9828 | -51.89865 | 2025-12-26 04:12:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c63a7d6-c99c-3ee8-ac79-f49034ada413 | -18.75689 | -45.29344 | 2025-12-26 04:12:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 506f3576-72c3-3999-a989-015f1cccef9f | -18.75748 | -45.28978 | 2025-12-26 04:12:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c4d3ee6-1d87-363a-aa34-f147bfe10974 | -18.52719 | -41.03362 | 2025-12-26 04:12:00 | NOAA-21 | NOVA BELÉM | MINAS GERAIS | Brasil | 3144672 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5cb4fe3-3b41-375e-86d0-95f50ab7e676 | -21.25138 | -49.27607 | 2025-12-26 04:12:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2467f6a-672e-3cb9-aece-9dca66da1699 | -16.984 | -51.8966 | 2025-12-26 04:12:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e1aad66-920f-3f58-a528-8a268dfb06bc | -18.07898 | -43.25314 | 2025-12-26 04:12:00 | NOAA-21 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be959f5d-51ed-3277-be28-f3f24b1ce95b | -21.23149 | -47.04375 | 2025-12-26 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1206d625-a21d-3129-b699-9a3d6fc3bb26 | -21.24763 | -49.27531 | 2025-12-26 04:12:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 759b7151-eb7a-3104-bdcd-de648d1d2d1a | -20.19436 | -43.63298 | 2025-12-26 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a7ed7a4d-3540-377c-b4c7-97db5e3d1c9a | -20.20275 | -43.62272 | 2025-12-26 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 46505205-1670-31d5-87dd-54ac512aa06b | -19.35678 | -43.6973 | 2025-12-26 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7de31bd-7972-35f7-b7b2-40fb115b1880 | -20.20555 | -43.6269 | 2025-12-26 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5503345a-0c90-3701-9d78-4981dc16d21b | -20.20331 | -43.61899 | 2025-12-26 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d0e754c9-f3bf-32f6-9ede-17ea81a911d3 | -16.32241 | -53.78986 | 2025-12-26 04:12:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b5874f8-8518-3449-881d-276d1ea7ea87 | -19.52536 | -40.67548 | 2025-12-26 04:12:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b1766159-d1ba-342d-9205-41dd9633bb07 | -18.15871 | -46.94368 | 2025-12-26 04:12:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fdf8095-c3ad-30b8-a5bf-2c7c37aca867 | -20.19491 | -43.62928 | 2025-12-26 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8e135c25-b946-3c75-b677-f80bef2d597b | -18.15521 | -46.94306 | 2025-12-26 04:12:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d77ed20-260c-3f5d-a441-9f0d9ff91caf | -24.18001 | -51.69537 | 2025-12-26 04:14:00 | NOAA-21 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 681fd08f-c37f-3557-b63d-a19e0aac056f | -2.90535 | -51.84614 | 2025-12-26 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e24f783c-3c40-3570-8029-f8121fdf634b | -2.91428 | -40.90832 | 2025-12-26 04:36:00 | NPP-375D | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 555f100b-bd99-3d40-85c0-4f2a7465abca | -2.36758 | -51.9063 | 2025-12-26 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8eb3dfce-907b-3f08-bb32-64d7b863fbde | -2.37158 | -51.90696 | 2025-12-26 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fade102-4eed-3748-a65e-db780c06264c | -2.9014 | -51.8455 | 2025-12-26 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14f01134-5c1a-3b9b-b771-7ef55411afc0 | -3.49902 | -47.17327 | 2025-12-26 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3721274-72ce-326b-93e9-781cd68d1539 | -5.03797 | -40.85962 | 2025-12-26 04:38:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 50f7d1fd-7b88-3f09-9dab-abc20668f03f | -5.04255 | -40.86027 | 2025-12-26 04:38:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a8b76dc9-f724-3c09-a3a7-aa4b6ed5919d | -11.16782 | -43.30455 | 2025-12-26 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 734ae202-9b63-3022-8d66-212597de3ce7 | -5.66456 | -39.48426 | 2025-12-26 04:38:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5266175-cbf1-376a-afac-e6c304501cab | -5.93349 | -43.5134 | 2025-12-26 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43ed7d5f-92e0-3216-be7a-5712845f9c63 | -3.7694 | -49.30843 | 2025-12-26 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74fe1ac9-5b83-3581-a44f-aa4d9f288d41 | -6.71349 | -39.15849 | 2025-12-26 04:38:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0a34af46-7745-3649-9679-662d242836e1 | -5.9296 | -43.51289 | 2025-12-26 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58f70f82-d25e-3673-8255-4b676d39026e | -6.57307 | -43.80003 | 2025-12-26 04:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fba1276f-5049-3166-a6c7-48efd4b46bf0 | -5.66498 | -39.4813 | 2025-12-26 04:38:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 39fe085a-25a8-360e-99d2-ec3d9dad0dfa | -11.16303 | -43.3079 | 2025-12-26 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8dec83ca-1a77-3233-b6b5-1f3fbe8f52f1 | -3.65475 | -48.93231 | 2025-12-26 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec54adec-18a6-369b-852d-c90ea0a2dcd4 | -17.58391 | -52.38964 | 2025-12-26 04:40:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41b81519-8370-3082-b118-0514756c0ef4 | -18.52603 | -41.03257 | 2025-12-26 04:40:00 | NPP-375D | NOVA BELÉM | MINAS GERAIS | Brasil | 3144672 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2246e039-165f-32b2-bbd2-c0205572b1eb | -18.52588 | -41.03539 | 2025-12-26 04:40:00 | NPP-375D | NOVA BELÉM | MINAS GERAIS | Brasil | 3144672 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5d6e3def-3dcd-3395-b2a9-eebf705b67bc | -16.32453 | -53.79125 | 2025-12-26 04:40:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a64d8895-8ebd-35c6-8502-a37d1ebd6377 | -13.6078 | -43.56146 | 2025-12-26 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d41befaa-f049-3b6d-9cbc-9e31c0dae8c7 | -16.98359 | -51.89801 | 2025-12-26 04:40:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 755cc35c-aa71-3796-aa60-28aa9cf145de | -15.72715 | -55.69232 | 2025-12-26 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fd8aced-9cee-34f5-9714-86504d5d78d7 | -18.52625 | -41.03181 | 2025-12-26 04:40:00 | NPP-375D | NOVA BELÉM | MINAS GERAIS | Brasil | 3144672 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 92a85d5c-55fe-3cc7-af4c-ba0f657b2d88 | -18.1538 | -46.94209 | 2025-12-26 04:40:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd0d5179-29dd-3c60-8aa6-b0e2f1c344f2 | -13.66719 | -46.27697 | 2025-12-26 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b037f7ac-a380-3867-bf8c-94957ed203ba | -17.31297 | -44.92887 | 2025-12-26 04:40:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e21c94b-2763-32fe-8d27-2501b0246486 | -17.31052 | -44.92825 | 2025-12-26 04:40:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aee7b950-a58d-3dfa-acc2-7e8491960c95 | -18.15751 | -46.94272 | 2025-12-26 04:40:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
