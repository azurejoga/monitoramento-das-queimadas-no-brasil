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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebb07072-5de9-3390-b258-172d92c58504 | -8.94496 | -62.36892 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 038489a0-b592-3de1-a1f1-fa713836818c | -8.07544 | -43.61183 | 2026-08-31 16:50:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 55e4e859-1f45-3db2-8812-abd2916cb31d | -7.63248 | -44.92259 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1602ac79-b81c-3a83-9d04-7c337d4e873f | -11.62153 | -49.41569 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 13180087-cdf1-391c-ac49-62dccbf8af2b | -11.57719 | -47.71997 | 2026-08-31 16:50:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b3372ab-c940-3987-a99e-1c789bb137ae | -11.57943 | -47.71243 | 2026-08-31 16:50:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 938d8c6d-4fb0-391e-8905-e74ea18cd48b | -10.73569 | -41.84736 | 2026-08-31 16:50:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 8d8f3435-43c5-3ddb-a042-b73c71574dad | -13.48296 | -57.05597 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5c3272f6-8484-32e5-87e8-32d1b072958c | -11.79883 | -44.88655 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ecc27ddd-6f58-34c7-ba6d-f23d4d24fb6b | -9.15245 | -45.81223 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8cff344a-553d-3de0-996b-8602f09d5b08 | -13.46616 | -57.03698 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0ad0a6f0-1ef5-3031-8db3-ed3500d8b466 | -11.91593 | -45.04863 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36f0fd44-c440-333d-bec3-deb7d1711394 | -5.69542 | -43.37162 | 2026-08-31 16:50:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4e50a61e-3467-3bed-b9e2-e8b750b53698 | -9.83106 | -46.35509 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e82696a6-f0c1-38a7-a3a9-70178403e9ec | -8.76809 | -46.46099 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 31af1ab6-0409-30d1-9632-e279168513d3 | -13.46951 | -57.03598 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9fcd75f1-16d4-3fb8-9def-79b5c88e3dbf | -9.67537 | -47.95453 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1a41182c-a59c-3997-b97f-a0fa242146fc | -5.88036 | -42.64172 | 2026-08-31 16:50:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b6dae241-6a76-342d-9ade-2bef422b3a9e | -8.22046 | -50.77956 | 2026-08-31 16:50:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0bb09bf2-b810-3461-867c-ebcec066f220 | -8.94874 | -62.36903 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4f7c186d-d6f3-3d81-a604-9eb085fd87a7 | -7.88913 | -47.08398 | 2026-08-31 16:50:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ccc68bc2-4013-391d-9d4c-e33776141aa7 | -9.2036 | -60.24676 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7950187e-3e46-33e7-8743-1416d2cf1527 | -11.21397 | -45.34205 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| bb2a2a9d-0e9e-34ce-8de4-6843739f1a43 | -9.0144 | -57.54374 | 2026-08-31 16:50:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5dcf0da-6035-3ea4-a9a4-e6aa0c0e710b | -9.8021 | -59.43729 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3c0086e3-79e7-3082-84f0-495937d31b3e | -10.02481 | -45.56193 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a1250441-d2c6-3954-bc4e-4e67a58b2b47 | -13.84892 | -54.09087 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e3f15296-a49a-3218-86cd-e5af4462a94c | -7.79309 | -61.57629 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c79cbd4a-978a-3b7c-87f6-db056ac9f9ba | -7.94046 | -44.24239 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| dafdf585-4e63-3c41-a571-c360bf651ccd | -9.17126 | -59.36704 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| c058f468-0ed4-3be8-92f4-d90b19a39021 | -11.14136 | -50.58805 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 935246c0-5d6a-3c49-8fc4-91fc43a2d938 | -13.96966 | -54.41141 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 5966325f-6a5d-32ab-b7fc-48816ba86ffc | -11.37486 | -45.19637 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 983de699-3735-3114-8f64-cffa9ab0eae2 | -13.39359 | -51.35186 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 67d5524a-1028-37d9-b71f-0b9c7c28e26e | -8.42302 | -44.98758 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 800bea23-6943-30bc-b9cd-c7ca7d0e9abc | -10.84703 | -48.33821 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 70ff09da-d5f7-333a-bf65-da9dd50a8833 | -5.58896 | -42.33524 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 218c948f-a524-36cf-ae44-e9602e2a96fa | -9.20634 | -47.99486 | 2026-08-31 16:50:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 031c6188-4299-328f-89e7-9d8c000b4f59 | -11.20357 | -45.05503 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 19869eba-5fc5-3a98-a64b-335942b76e72 | -8.37706 | -45.76516 | 2026-08-31 16:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95547c4b-b5e2-3280-ac01-729b899270fd | -7.63222 | -44.82785 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| fff04a17-7f97-3db2-9710-347903768dad | -6.35125 | -35.24631 | 2026-08-31 16:50:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 07587032-3a01-33be-8e2c-8d00eb4be2af | -9.60271 | -47.61697 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ef82a93f-bcf7-322d-80a4-307dfb31b775 | -10.34987 | -49.9749 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3565e83b-3379-36b4-af28-79121017184d | -10.50878 | -45.04233 | 2026-08-31 16:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e00a5ea1-6cb5-36b6-bcb7-cad3ef23332d | -11.25406 | -45.10223 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 450a3964-d829-393d-a57b-374938cac246 | -13.47704 | -57.03592 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5f0b058a-bb7e-3750-90f9-5d97ca210a12 | -7.93192 | -61.35321 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 4f5b59c9-546f-3892-b1f6-e7dd7e388b14 | -11.19056 | -55.11128 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1975221e-0e73-3d56-9245-0eda4327d5d2 | -13.40393 | -51.6727 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e4cb83b4-6c56-30ef-b29d-3e1df01c1e54 | -11.37079 | -45.19212 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 3eaba4ea-0234-303d-a09d-f7d936a383cc | -12.09654 | -45.06556 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 661b0334-cab9-35ee-86fa-74295045f47c | -7.4361 | -44.95572 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d3a69c95-5a7d-332c-b406-b1b08d736ac5 | -9.5304 | -42.4036 | 2026-08-31 16:50:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0f683f53-3091-32d1-96ac-11dcdbb86a45 | -5.28202 | -42.78301 | 2026-08-31 16:50:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5db8e843-be02-3e4b-959f-ce282d511820 | -7.56197 | -44.33415 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7c94b385-b255-3063-9d81-555c9e41c5cf | -13.57073 | -55.15055 | 2026-08-31 16:50:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5fd36424-6af0-36ee-92ed-77ee8d63dd84 | -10.31572 | -50.00279 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6fe7f984-6b41-3cc2-97ce-ce99c5298b97 | -5.89912 | -46.12205 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a5fa78e-6f1e-3e2c-95e6-d1b7f5004246 | -8.15005 | -45.51965 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fca0431f-b935-349d-ad31-89c96a8bcb84 | -8.1392 | -45.52139 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bcf2f30b-11ca-39e7-bf6e-104dd9845505 | -10.10881 | -50.30973 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| be8cf3ba-0134-3505-a775-52adb0896440 | -13.83107 | -54.09338 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| be44cf37-09fe-31b5-82fc-c50b7c07bb89 | -12.38465 | -48.1659 | 2026-08-31 16:50:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e4693461-9209-3460-bc30-0a8583447f75 | -7.89253 | -47.08346 | 2026-08-31 16:50:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e622ae0f-6e14-3dba-8bc5-6fd14882325c | -9.15534 | -45.80767 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 76e9a110-007a-37df-aaca-043db0db8c19 | -12.10291 | -45.06007 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6182860f-fa61-3492-a2f2-33ebc38670f7 | -9.20356 | -47.99887 | 2026-08-31 16:50:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 691d794f-3ce3-3260-a59d-07de84a0b3b2 | -8.74448 | -39.00393 | 2026-08-31 16:50:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f14b8d9a-7c49-303e-83ac-633965c1c8ea | -11.92494 | -45.08114 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| dc1babbe-f78e-3f1c-acdf-0bce9002ef70 | -4.3203 | -45.23323 | 2026-08-31 16:52:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 004ee9a1-34ac-3e7d-ac60-aee7740e09c8 | -4.1582 | -60.70476 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 14996eaf-604e-3d5b-afe3-8fabceca1e40 | -5.8889 | -52.05754 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 8dc30bd8-16da-3c4a-bbc7-d21e24a63d7f | -3.62263 | -60.55323 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 92e659f4-a018-35b0-971a-949bd427c3ae | -1.04357 | -48.19195 | 2026-08-31 16:52:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b151215e-adef-3016-93b7-5e2461847e10 | -6.13227 | -56.38552 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 79cd6d5e-82e6-3dd6-8311-1c42897d26b9 | -6.25725 | -53.67517 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f55b8818-dad0-36c2-b1f0-97178f3df86a | -1.59847 | -54.40442 | 2026-08-31 16:52:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 544c3fe0-13c5-32e1-bab3-0d2ce71dfdcc | -0.80836 | -49.20108 | 2026-08-31 16:52:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d190b593-e5f2-3431-9f07-5fda2b001e91 | -6.75969 | -59.43999 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| aa686006-ef32-3bc7-80c4-11b2fac96397 | -7.31513 | -60.57068 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 988a55bb-bafc-3742-9ed7-e6446c6761af | -2.66906 | -59.37023 | 2026-08-31 16:52:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 494587d6-b063-3e43-9272-7f976952009e | -3.62009 | -59.08036 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4ae49e48-b059-3f12-b634-a0310b7e24c6 | -4.15686 | -43.09441 | 2026-08-31 16:52:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9981fde9-7999-3493-a995-2a51ff481455 | -2.65946 | -59.52935 | 2026-08-31 16:52:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e87df84-9f0e-3bda-9fe5-6be802936126 | -5.58294 | -60.23342 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 833e5286-99e2-3452-86db-bb80685ab36a | -4.15213 | -60.70555 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cdf6789f-ea1c-3abf-951b-79e9ab026814 | -7.3381 | -60.59885 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2b888d6e-d061-3a2c-8333-54f6cdff9d62 | -7.30129 | -60.58121 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ef69fe22-983a-3819-a327-b7bbdf395bad | -7.1894 | -60.66199 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4787aa23-43d7-39d4-b5e1-c2f503179282 | -5.16755 | -56.89446 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ac50840f-014e-3e67-8bd7-235e6b07c7ac | -6.1368 | -53.53083 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| fb3baaae-d6be-36a1-846b-8d79a3e34fd2 | -3.50854 | -56.31471 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 51fdc004-ebef-322f-831f-a8e2feb531af | -6.11215 | -59.94426 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8d5b4501-18dc-33a9-b8c4-ff8c1a3e0bb0 | -4.90777 | -43.46217 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5a836bd1-3615-3616-b37b-8b486cd306c4 | -1.92139 | -44.68433 | 2026-08-31 16:52:00 | NOAA-20 | PORTO RICO DO MARANHÃO | MARANHÃO | Brasil | 2109056 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4829b52f-df3a-3993-839d-ac3fbc778a6f | -6.98211 | -59.59265 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dedf627e-3c4b-3162-a713-cab069f14d4d | -6.14031 | -55.64036 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| f75f478c-707c-30cc-8682-7837545f1a6c | -4.45491 | -55.66411 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 94451fdb-908d-34a8-8c56-3387e0963f4a | -4.92342 | -55.76431 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README167.md)
