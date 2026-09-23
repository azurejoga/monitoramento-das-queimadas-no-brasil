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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 679670fe-7f44-361b-b593-c3bbd7f32a1e | -6.7332 | -59.43021 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c21c14e-6460-34e2-bd79-1e07fa29be85 | -3.1785 | -61.1022 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a2f4f05-445a-342e-8f54-7d30e54bd650 | -6.61448 | -59.93108 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 26795332-30a4-35e9-938b-f4672144d35a | -3.6116 | -60.56842 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 671d6ea1-3f69-3165-bbc0-e94317593d27 | -6.60811 | -59.96225 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ca2353b-9632-347c-85b9-8994bf95a612 | -6.61025 | -59.94666 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b0fd1ba-7f0d-393c-8d23-1a25d215b3ef | -6.61378 | -59.92093 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8f498bbc-670c-33bd-bb82-c62f5f640e17 | -3.11377 | -61.08998 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91b2f600-e610-3c1e-99de-0eb0efe174c7 | -8.23214 | -62.8383 | 2026-09-23 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a35a020-0cc2-3111-bd21-f3114656e9f0 | -3.72349 | -60.57555 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44558a13-78cf-3396-9c71-b1e22c9b7273 | -9.18338 | -65.85712 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b004c98f-6d6d-39ae-8662-335ea9033dc9 | -6.31325 | -59.94796 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6899bde8-1d7f-3407-8be2-55e2cbc07c2c | -3.68351 | -60.57088 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 74f20191-ca18-3b55-b5db-dc63ed4ffc7a | -6.67825 | -58.56061 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38e1f384-d06c-3957-ac51-4a4b502afd55 | -9.48307 | -67.15583 | 2026-09-23 06:10:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d42b87f6-4bd2-31c3-9aa0-4900958e898d | -8.92361 | -72.82113 | 2026-09-23 06:10:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ced17bb0-2349-34b9-a883-eae8e8e54656 | -8.97667 | -72.61219 | 2026-09-23 06:10:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71260671-a754-3000-b996-1f0d05c75317 | -8.77165 | -72.7715 | 2026-09-23 06:10:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0580e1f4-9dcf-3172-96a7-ade8cf255a2c | -9.47947 | -67.15156 | 2026-09-23 06:10:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6faaee22-bed3-30a4-89bb-a146a0ef5d07 | -8.76779 | -72.77446 | 2026-09-23 06:10:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a358e88-8168-31db-abef-6293c3d48a17 | -8.92691 | -72.82166 | 2026-09-23 06:10:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d75504d-2cde-3197-8107-b748e1e0259d | -8.58672 | -72.41142 | 2026-09-23 06:10:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e4960c0-2366-3f73-b5f2-2d827c53d587 | -8.77329 | -72.76106 | 2026-09-23 06:10:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 402baae4-e085-3df5-b5d7-e9aaaf93ba09 | -8.87451 | -72.76701 | 2026-09-23 06:10:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26796036-a9d2-3551-b74d-346c2fe62687 | -10.40982 | -68.89843 | 2026-09-23 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9020e78-d29b-3418-a30a-eb0163804025 | -6.64 | -43.75 | 2026-09-23 06:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf7b7ff2-9951-3348-b18b-b320cee368ee | -6.64 | -43.7 | 2026-09-23 06:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d13f971-8af5-3d84-8eff-941ffeddc184 | -6.61 | -43.7 | 2026-09-23 06:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2381009-d7bd-3c8b-93e2-d189c0e2bc88 | -6.61 | -43.74 | 2026-09-23 06:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44e6b2b6-c939-3c5f-beb9-73eef6004fbd | -8.9165 | -61.4767 | 2026-09-23 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d663ca90-adc6-348b-89b7-bb73476dff85 | -8.9164 | -61.4958 | 2026-09-23 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 9d0eb4a2-ba2c-3bd6-bbf2-55f79029a72f | -8.9164 | -61.4958 | 2026-09-23 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b13e5deb-3154-3031-b31f-74a1c82cf274 | -9.1025 | -61.4299 | 2026-09-23 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3652ab01-941b-36d7-bda1-9f5d62c2ad6c | -8.935 | -61.495 | 2026-09-23 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1861b4e8-2247-306f-9281-9674c632a32a | -2.54743 | -49.0984 | 2026-09-23 06:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5188b889-6b97-3fbe-b66a-d70f7b0585a5 | -2.45075 | -49.21399 | 2026-09-23 06:40:00 | AQUA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c4e51d61-f0ce-3beb-9e32-8a49ba947929 | -10.28893 | -50.53551 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ac7705e3-7f5f-3b30-8ae3-da38ac1819e1 | -10.22963 | -50.23072 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c1b2cd0a-412f-3f1a-b7bc-c8041cff785a | -10.02654 | -50.21094 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 287cb2e7-c3a7-36cc-834a-97265808c750 | -6.94184 | -42.87965 | 2026-09-23 06:40:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| cd519db4-aa55-3a01-9030-b76a039dc958 | -6.98343 | -42.58797 | 2026-09-23 06:40:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| fbc68a78-19bc-3a6f-9b51-17d0dc7bcf74 | -5.77381 | -47.15543 | 2026-09-23 06:40:00 | AQUA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 974b38ae-a262-3919-b323-763cf83c1cbf | -7.41236 | -44.71964 | 2026-09-23 06:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9ce41f52-ac5e-3a3a-bf7c-6804b24f9806 | -7.41102 | -44.72863 | 2026-09-23 06:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dd382cc9-5d8c-3cd2-8431-180527d32308 | -6.34018 | -49.86857 | 2026-09-23 06:40:00 | AQUA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 498d9f98-985e-3096-9b73-d1c90140a2a6 | -11.4088 | -44.02185 | 2026-09-23 06:40:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 286fc31e-ad23-3615-974a-0253e3f9bfaa | -6.9932 | -42.58932 | 2026-09-23 06:40:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c17ece08-d000-308e-bb92-b8dfd4535b02 | -10.4455 | -50.35075 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5fc5aac2-fd6a-3241-af8a-24a82b06cc21 | -10.24413 | -50.20686 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1a4b27ef-7f06-35cd-b25e-826aeae0b5a6 | -7.43996 | -49.83345 | 2026-09-23 06:40:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 32748aef-7eb8-317d-900d-f65b5e164b56 | -2.44673 | -49.22219 | 2026-09-23 06:40:00 | AQUA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c116adda-a1b0-3d56-ad3a-cbb13ae3a781 | -8.77197 | -45.63831 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d2fb1024-d5e4-333d-84f7-0f44224a817a | -10.03489 | -50.22553 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 76a52e33-cee3-3a20-a53c-ffa047fe0ae1 | -6.78923 | -48.6824 | 2026-09-23 06:40:00 | AQUA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6c951212-55e4-3b8f-a562-e265b20e1d56 | -10.23845 | -50.22464 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7366b455-dc91-38c7-bdde-4f4127af5b8a | -6.71902 | -44.15369 | 2026-09-23 06:40:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 68e0caff-062f-3c7c-a093-c217c5e65857 | -10.2668 | -50.5113 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 9546e6fb-98c7-312e-952b-126c17110fda | -10.23799 | -50.24527 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| aa6becb7-a6ea-3d8c-8f83-efeed7ada650 | -8.33361 | -50.82243 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| be0974dd-9d41-3021-9e60-2711329034dc | -10.27186 | -49.96745 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ad27089d-5d87-31c9-ae94-25198d9e4d16 | -10.27742 | -50.51307 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 7167ea4e-896e-38eb-9d73-0909e6bd015c | -8.78206 | -45.63083 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| db636e30-f90d-3865-a6a6-37ce3afd72f7 | -6.67403 | -55.04409 | 2026-09-23 06:40:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 124e55c6-eb38-3ae8-9bae-3d853fb10097 | -8.77461 | -45.62071 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4c40f680-0229-3f4e-8e10-450c129bb9d9 | -10.24459 | -50.25195 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f966f91c-6a34-35f1-9690-994bef94878e | -10.24885 | -50.22635 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 1181d7f6-f836-3659-a2c6-4c6e52b07389 | -10.03904 | -50.19983 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c20e8575-34e0-306d-a7ce-194dacb7128c | -7.98295 | -47.46732 | 2026-09-23 06:40:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f7473c16-4157-3103-84c3-ac66ad992458 | -6.68228 | -55.05045 | 2026-09-23 06:40:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| ec021260-b2af-3af5-9ce4-09b9f31a07af | -6.99162 | -42.60041 | 2026-09-23 06:40:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bfbaa8bc-4d0d-3a73-b01c-a59955a688dc | -10.26989 | -49.97974 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 82a22a60-c291-3bd1-be9e-edcdb16da9dc | -10.51067 | -44.87405 | 2026-09-23 06:40:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| afdfe077-9301-303e-95c7-7786f01915b9 | -6.61392 | -43.74368 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 319ba72e-71d9-3367-93f3-6ba125d28cd4 | -7.03095 | -44.66068 | 2026-09-23 06:40:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e9509a8-853a-36ab-b27c-345eb6cf9cd1 | -10.00325 | -45.18347 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0ec80dae-f1e6-3f34-b8aa-364063ee82c3 | -10.54167 | -43.97359 | 2026-09-23 06:40:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5fafbd07-afe9-3f55-a4b8-66d2e24aff31 | -10.3815 | -51.8427 | 2026-09-23 06:40:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 4df1e42c-8c95-3052-a567-07728d7497eb | -6.66597 | -55.048 | 2026-09-23 06:40:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 428f78d5-20f0-3df8-8bbc-4ef05f8b53f7 | -6.61534 | -43.73415 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 244.5 |
| 08674e64-d850-3e6e-b920-15c6997e8a79 | -10.28668 | -50.54892 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f51ac8f2-5eb3-364c-8028-a5873b5ecd04 | -11.40732 | -44.03231 | 2026-09-23 06:40:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 73ccede7-3b86-32a1-add7-ccf9aa4f09eb | -6.57212 | -44.15433 | 2026-09-23 06:40:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7d7bdd67-52a5-38bd-8de6-9204b3dcd906 | -10.25713 | -50.24086 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 028edcdf-a9b8-3633-a228-c74afdc5af54 | -11.66037 | -43.47015 | 2026-09-23 06:40:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0035d7ea-daee-3b93-b3e3-531628c1511c | -3.22742 | -46.93625 | 2026-09-23 06:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4362f236-dcac-3141-8297-1922e6d2ce87 | -6.89351 | -46.54923 | 2026-09-23 06:40:00 | AQUA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b5b85df-2eb3-34c6-ab74-eb0cd461b80d | -9.93514 | -48.46782 | 2026-09-23 06:40:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e669a8db-8750-337e-83da-18044f9c8d46 | -2.4489 | -49.20789 | 2026-09-23 06:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 640b92e9-b049-3ab1-a640-c1ab8d008b82 | -10.44175 | -45.09224 | 2026-09-23 06:40:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed9643fb-ecb6-3c33-bbf3-494bd98f7bde | -11.35488 | -43.37911 | 2026-09-23 06:40:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bd9fb264-25df-36bd-8a1a-a65549829182 | -10.24004 | -50.23245 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 259.3 |
| 6e685868-f14e-3117-809c-2f333a7b6a91 | -10.44337 | -50.3637 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a38de9d6-d23a-3076-b952-87aea898b1ef | -6.37704 | -42.78831 | 2026-09-23 06:40:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 112dd8b5-bd46-334e-9924-43d634508c52 | -10.25501 | -50.25367 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0dfcf43e-476f-3e2f-a565-5d0daa7323a2 | -1.38205 | -49.03654 | 2026-09-23 06:40:00 | AQUA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 712bd950-a9d9-3c15-9333-11079a03fc49 | -6.62485 | -43.73152 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 160e55a2-1f9d-32f1-b0db-182679b5759b | -6.52315 | -43.54784 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18eb65b9-4df9-3acf-a1e9-552e510829e7 | -10.24209 | -50.21965 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 446ee60b-3ad6-368b-8427-68984cc9a3e4 | -6.32609 | -43.93922 | 2026-09-23 06:40:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 96a1e7ed-21d2-323d-bb81-f7f8b3895d87 | -6.57348 | -44.14514 | 2026-09-23 06:40:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |


[Clique aqui para ver as próximas entradas](README127.md)
