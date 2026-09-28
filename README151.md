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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c4cdb72-c677-346c-a112-a19d5cac751a | -11.07384 | -48.89019 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1ba22d86-c23c-33b7-a472-faede56be435 | -7.68831 | -54.7656 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 43a769a1-7d82-3dd4-a4f6-9e16085b2072 | -7.42619 | -55.63396 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 3d2c5b3b-63a5-35db-b72a-c9467131cae9 | -7.37391 | -41.79251 | 2026-09-28 17:09:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 19d9bfea-5393-3f09-82b2-7fe0f991cae7 | -10.10061 | -43.94734 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9a75c7b0-272d-31c4-a0c9-d657e258a387 | -10.99919 | -50.7007 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 951e5678-98ce-3347-904b-84c431582d00 | -9.611 | -50.78841 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ab803087-ea13-3dd2-8511-8337dcbd2b71 | -11.5765 | -47.39806 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| db408ed6-4d68-34a7-a14c-a941b894c68c | -9.36283 | -46.82475 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 58b56245-79f5-3a6b-ab41-7666bb301de6 | -10.21472 | -49.99493 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 551327fb-4c08-3077-a082-359f3f95e905 | -6.12722 | -48.77679 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 024af243-6afb-394a-9c0f-a7f3bfcd7885 | -9.32161 | -46.55939 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 233e6beb-5651-392c-b58f-2655a44ce028 | -8.19007 | -54.79912 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c0abad73-4ec5-3f9a-9a55-dde4e991ab24 | -11.47842 | -49.74552 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f42e4663-fae6-35c2-805a-444fe792b693 | -10.82815 | -57.19251 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 87d0101c-ef71-335d-b497-42048ce3f918 | -11.15178 | -48.33369 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 64599ce9-4463-3f3a-8154-c9b30e98ab93 | -7.36928 | -60.58479 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 016051df-c868-3f71-a4fd-3a862e180bed | -5.57034 | -47.39062 | 2026-09-28 17:09:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b2bfc360-55fc-3a10-9ddd-b0bdc7c0cffc | -12.06452 | -48.53652 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b3d8e494-e279-33c9-b9ca-6b5491bb4a18 | -10.82235 | -57.17695 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6efd55cd-16e5-3ac3-bf24-31b8f0c54184 | -11.17698 | -44.806 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 4cea7fa5-1407-3366-9693-2bebcbc342e9 | -8.66607 | -45.37962 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 40154c7d-a12a-3703-987b-1f3fc58e6cb4 | -7.41958 | -55.63498 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 28b2d079-28da-342b-9d13-486bfbc6059a | -11.1948 | -44.80184 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| cb9ebb26-0b06-3f7c-a88f-646df466ccd9 | -11.44129 | -44.92924 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 71b746f0-c172-37af-880a-ff75be0a4439 | -8.7372 | -44.90156 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0cb2a67b-0587-391f-bb3c-598ca63bf000 | -9.81972 | -46.28376 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6839cf53-fb7b-32c8-853d-6ee0f90f42ce | -6.41865 | -56.09435 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 95f5c332-b332-31f8-952e-fddb4b1ef7e4 | -9.64274 | -46.76843 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2d0cc04-6b03-3f7d-aec9-a1015897dbb1 | -10.17139 | -63.05802 | 2026-09-28 17:09:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a8508432-e7dd-3946-a542-97abb04b99af | -7.45901 | -64.33475 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| fd2ad968-c94e-3ec8-bdc1-daed2386c88c | -9.51107 | -46.37799 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6b2907a-4495-3c81-bb25-cae0ad0f9c7b | -7.69717 | -54.7571 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5bba514f-baf8-3f47-af3d-85287834ee29 | -6.8962 | -55.56492 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 26288aae-88a7-3c3d-9c06-a6e6a70ad75d | -11.86739 | -50.89263 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 0553c634-1505-3bb7-a896-a4f978f373d0 | -11.23524 | -54.13026 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0e426651-ad3f-3fa1-a2dd-9fcac357695b | -5.65151 | -44.23148 | 2026-09-28 17:09:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f52fc23e-5ff5-3c81-8dce-bc286a2ec55b | -6.33832 | -55.31707 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 81e8beae-ecfc-327d-9205-b017c192169d | -10.82053 | -57.18953 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0e7c725a-540d-3ae6-8a36-711e7a91a88b | -10.94669 | -43.88525 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 36c8d1df-2159-3d17-88d5-7ebbadc74a0a | -5.7315 | -43.27825 | 2026-09-28 17:09:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| fe3b0179-38ae-36f0-9a30-0defcb8cf66b | -11.39165 | -45.41809 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1b7ee795-3d6f-3e8c-a361-71aa2d0d8f27 | -11.11802 | -47.72037 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| edcb8da9-8067-3084-b912-abb5b41fcbfe | -11.46287 | -49.74827 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 8dce2865-2a8d-3163-9b77-6e2208c85f4b | -11.43536 | -44.92717 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87601d8c-f1ea-3a4d-9593-d5f9e6c4f9e4 | -9.16436 | -60.78559 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 68314dbb-aaac-32f3-bf0d-af546c052f62 | -10.60404 | -49.98392 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8a7bcf76-11ed-336a-a1be-aac7136037c8 | -6.73257 | -43.0039 | 2026-09-28 17:09:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 3b0ccb34-0c8e-30d8-a5d7-58eebfdec223 | -6.73269 | -43.0011 | 2026-09-28 17:09:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 5deedc79-e3fc-3c6e-99c8-7bebe41841d4 | -10.45702 | -47.47828 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2a44f78-2093-3782-b4a6-3b08162d3ab8 | -11.09941 | -51.17252 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e52fb692-f536-305c-b0c4-8ebd15f17469 | -10.92422 | -50.66265 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 18ccfef8-a415-3d0f-9460-e972906e2015 | -12.38447 | -50.23356 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3a8b6f29-fc92-3296-9a67-e47a4325e4a7 | -9.19539 | -60.41788 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| e96ed4f0-b9be-39db-ab9e-4cb6299f6658 | -6.15756 | -52.89598 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8e42abac-1398-3c85-b71a-516f7e784f36 | -9.10697 | -49.89611 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 03916f3d-7f26-373c-a8a0-9438e796c3a9 | -9.4439 | -41.82288 | 2026-09-28 17:09:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 53784647-bb1c-3f41-bf59-ff21c0b38a7c | -7.36307 | -45.4052 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fbb84821-735c-3af0-835a-5cf12c1ad678 | -8.67021 | -45.37167 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f2eb5d43-8978-3359-ab41-3c4764b2a6c7 | -12.13714 | -61.1577 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 97986bc5-baf2-37bd-b606-7019a34c7876 | -7.36929 | -45.40797 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5e32154f-feef-361e-a9ca-9bc99d7b2812 | -11.13829 | -51.18334 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| b7815389-9510-3ec5-a4f0-14f833c05edb | -10.81917 | -41.33506 | 2026-09-28 17:09:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 638a2b4f-d156-336d-a565-3cbbd02342d8 | -8.6695 | -45.34264 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 42b6a433-7f37-3049-ab8f-fd3f6eecdc1f | -5.11174 | -45.8036 | 2026-09-28 17:09:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f15e333b-b3e3-33a1-9cb8-da4842db1d00 | -11.18198 | -44.79335 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 51c84246-5eab-3416-bd5b-3f431015c89a | -10.21222 | -49.97989 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 48234547-853f-3976-9d31-c0ea92b66226 | -10.20635 | -50.01699 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 277112c1-8b93-3250-8b84-3dedfa03595f | -8.50399 | -46.89623 | 2026-09-28 17:09:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3ac8d909-e653-3a73-98e8-c98f56b2fd40 | -10.20858 | -50.00631 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 84fc2e83-ed91-340a-9ec7-362305e50603 | -13.0415 | -56.596 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 03fe5b4f-ecf3-3349-b127-9f76063d306d | -11.52989 | -47.37292 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6fba36b6-409f-30e5-8b7e-08700b063021 | -7.34928 | -54.94735 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e37de19a-0382-31d0-8fa9-4a9dd1c69c5f | -10.97341 | -49.66684 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| f2f122be-e9fc-3978-8aea-6d818dad7876 | -8.63696 | -49.47888 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5167e848-25f4-341f-a101-0f6639bee1c7 | -8.62805 | -46.98812 | 2026-09-28 17:09:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f2d50db1-9ea5-3d0f-86a4-4ffc56550358 | -5.76934 | -49.24136 | 2026-09-28 17:09:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 21c4c903-dadf-3e56-9d34-4d26c0c26841 | -6.17288 | -52.90167 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4db6439a-8b04-3784-8acd-8572ec2ee7ce | -9.82113 | -44.94883 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b3cab92c-322c-33ab-b1dc-f4e65d4a5f30 | -10.65125 | -50.70875 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ab97cbbb-b8dc-3529-b03e-79feadee6402 | -11.15586 | -50.65416 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4a1b4bc7-e6fd-3f50-989c-857a498f464c | -5.74427 | -47.38473 | 2026-09-28 17:09:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2889f96a-dec3-3df2-b47e-67921d619153 | -8.00004 | -44.971 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cfaf5e1c-71f7-31ca-ae3f-5e6de0ef7ada | -9.77583 | -44.82878 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5383c2cb-ab51-3fef-8f2f-b5a55efba03d | -9.93211 | -50.23452 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| c81bfe26-1f85-363e-9b4d-f852d792d21a | -7.3154 | -44.59631 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 47edb7a9-edae-3a79-bcc4-7a01bfc92c42 | -6.73374 | -43.00692 | 2026-09-28 17:09:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 16.9 |
| c98da04b-ef7f-33a2-85ad-640c2c58e512 | -7.37335 | -41.78633 | 2026-09-28 17:09:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 162e55ac-4c85-3110-80d3-d8820a3fefe0 | -7.53745 | -50.93285 | 2026-09-28 17:09:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6fac176a-2f4a-3009-b9a7-a2f9155e211c | -4.94742 | -45.10356 | 2026-09-28 17:09:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 7eed0dea-f84c-3f5a-91a8-03ebe4d7e88c | -11.05757 | -47.66557 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f3bbb7f9-8593-36be-a4e3-343c2bc36cb1 | -10.81344 | -60.73272 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| bf123267-d764-3edf-84ab-3831c21712bd | -11.57489 | -45.46806 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 790f0770-5e92-3b19-8628-2f7cea6ccada | -6.70183 | -45.68031 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 0194a71f-be0f-3408-a7b8-486044f56a99 | -10.86453 | -48.5134 | 2026-09-28 17:09:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94d3a2d6-2aa2-3d58-b3bc-aaeb4cb6ddcf | -10.91175 | -43.85881 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| bbef02b1-a511-3fb5-bc7d-2b6ebe7cbcd6 | -9.2171 | -59.04914 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d3f777bc-e5f7-3e9f-9041-0d4a15517ba0 | -11.53155 | -47.38916 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| ce59cca4-3348-30ba-89b4-8ed434faa674 | -12.36582 | -50.23682 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e3125a65-4040-3d14-b27a-c3c9cfddf9c8 | -7.26624 | -45.33696 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README152.md)
