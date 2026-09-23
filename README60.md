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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66348f5e-156d-3037-9629-c2dd1ae1088e | -11.14231 | -49.46119 | 2026-09-23 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94a5ab06-34fe-3727-89ef-c1485facc9be | -8.76076 | -45.8336 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb2c0590-57e2-3ce9-aab1-31ee54afb597 | -7.31483 | -55.22222 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 504b9df6-d9df-320b-aeb0-9d5ca2bd3385 | -9.71715 | -48.33714 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd4f3e62-a625-38d0-82c8-ed4a03eb9ca0 | -12.6802 | -46.396 | 2026-09-23 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db73bcf7-6e8d-3e9d-b457-ea02d7ad766c | -11.26465 | -43.41513 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e65bb06-242a-3154-b723-3fc09d04af48 | -12.12832 | -47.39046 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 091bba09-8d92-38b5-81f3-e4dae8f54bd3 | -12.4235 | -46.97372 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5919e186-6b7f-3a8e-823e-4506d99d10d2 | -8.17562 | -45.54959 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 810a2114-e2fc-3a2d-a767-97eac382a05c | -14.62384 | -45.66249 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91c5730e-7167-350c-b2a7-2c462c7e15ce | -10.26082 | -49.9874 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b244abb2-269d-364b-a3b2-33917c26e6d9 | -11.32928 | -47.34473 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8d6c21a-1e1e-3124-afe9-3e27d1d2b0f4 | -11.53813 | -45.3532 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b8723d2-c4a7-349a-8ab8-46dca1b892ce | -9.93532 | -48.46445 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3d3bac8-f006-3e73-a386-935bf9c57fdd | -8.36454 | -48.53716 | 2026-09-23 04:27:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43ec00a7-fa33-3f11-b044-c4f5ac7cdf94 | -6.73002 | -55.09568 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c902489a-72ea-3e95-9ff0-a1dbec65b4bd | -8.801 | -44.28172 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b077d39a-f171-3ed3-ab69-0c050e4c83bf | -6.68165 | -58.57003 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 022359bb-da43-3714-8488-7da9598e2193 | -11.87149 | -49.94737 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 24df350f-f1b5-33db-be93-65161ab09e14 | -11.45556 | -47.62704 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1763cb7d-c980-380a-833d-abaaf3c88cbd | -6.64016 | -59.92904 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2c7ef1c4-55d4-3201-8920-1ba3ba435d99 | -12.05668 | -50.35107 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1219f749-8358-344b-864e-eee22630c479 | -13.0173 | -50.60303 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9aa231c-cacd-3745-8d13-987322da8f9d | -12.09326 | -47.48568 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 135f0625-bbed-36b6-b51a-254baa70200e | -12.53975 | -50.06926 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62eb3e84-b310-33c8-afb7-0e14835b8b6c | -10.25139 | -49.97392 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72c97e1f-946f-3aad-816f-a6f85f2bf4d9 | -9.60233 | -43.94662 | 2026-09-23 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7db87d61-bc4e-3659-8e62-c75a6abde211 | -12.7155 | -47.01992 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c436882e-b0d4-3f23-9425-75b57bc7dd3b | -14.62529 | -45.65769 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac68ff5f-1534-3228-b7b4-803061545461 | -9.25974 | -46.23798 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b682e830-3331-3040-b2ce-67f68dab2995 | -6.67604 | -50.95272 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e29e646-086c-3f68-bb79-d2382589e07a | -12.76691 | -50.90419 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ad58c54-2d4b-396d-a459-1fc903eced16 | -14.6227 | -45.64574 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f9a36796-159b-3455-b72a-2e0d8e3cd510 | -13.8553 | -48.59259 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bb2af09-8218-3bc1-a24d-d02be7d1c1d3 | -14.62389 | -45.63762 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9f94ee44-1917-3a58-9011-67dcb27ad932 | -12.41461 | -46.96501 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 26488945-0355-33f8-93d8-1509d6a3e761 | -10.51639 | -44.86975 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c247a7f-b9dc-3c39-ae69-2cae0289f6a6 | -14.65979 | -45.59199 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7befca6-c33e-39da-9060-8a4ee1e0f00e | -11.13624 | -42.77848 | 2026-09-23 04:27:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4497ea67-1a81-36ed-98b3-6fed6c6b4fe3 | -12.80182 | -50.91447 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2feeefb4-f99e-3966-9b0e-9c22c68702f4 | -6.89372 | -46.54245 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1768389a-acdc-3734-9c5b-884293d61fb8 | -7.68834 | -45.47123 | 2026-09-23 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26cce818-6f53-3142-84f4-a27af10be48b | -6.1271 | -55.81841 | 2026-09-23 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2947b730-6ae8-3bfb-a5ad-095ae0258758 | -5.89118 | -52.28009 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d19c538-7d56-3041-9042-11702d0397d6 | -6.84383 | -55.30724 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f94b43d-2460-3dc5-a2fc-2123d8f9765d | -8.38307 | -45.59303 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11471151-f4d8-35f3-a08c-41753f1863e9 | -11.47005 | -47.382 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 284882a7-3b57-3947-91a9-6632a0a6254c | -8.45327 | -48.44681 | 2026-09-23 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84ddf39e-8d64-3728-addb-60f4aa1f5418 | -6.1921 | -57.78008 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 222bf7bd-ef64-3c4a-b009-9fc4a7ba6f26 | -14.62092 | -45.6579 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bd5bd23-693a-3428-a9b1-0ee687f68547 | -8.83067 | -50.49308 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ec94c6f-a09f-33bf-8edc-133be342e15d | -12.048 | -50.35442 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6f63503a-3398-3617-ad7f-21941b55de76 | -12.41516 | -46.96145 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f5e6c19-a2d8-3595-b3fe-c7be3e63e9fd | -6.63199 | -59.93438 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4f2ba7d8-280b-3380-910a-54346b88cb63 | -6.06742 | -57.80447 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 045bc235-7781-3b3f-bb8d-52dd1f8f759a | -8.2044 | -54.71356 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e82d0cc9-36b4-3a84-bf9d-e9e80fa89a12 | -12.66848 | -45.03699 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2558c0d8-0b28-35b3-bd43-189a81faa7ce | -14.61161 | -45.6232 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 350494d7-1e0d-38f3-be5b-d778d2f87b66 | -6.67332 | -58.55433 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43e5f99c-56d6-370d-8201-222383cb4e64 | -11.11619 | -48.31326 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1549d5f2-408d-33fa-b279-02ef4434c44c | -8.7716 | -45.62648 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9512501-eea8-3eb9-9465-6c6d229758d3 | -7.40009 | -55.2142 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8de31872-f2d9-30bd-b92c-3ce8dfc3b430 | -14.34988 | -43.7665 | 2026-09-23 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9fc71de-e56c-313f-9826-b0d781be785e | -14.62974 | -45.64681 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9daae135-39e9-3f02-a446-96cfc48b0615 | -6.93395 | -46.56641 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d905827-3437-312d-b0d5-bfea547ae9b3 | -11.82198 | -49.538 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1365651-5eaf-38ac-a8d0-2e4b077a1139 | -14.29682 | -43.1923 | 2026-09-23 04:27:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| bdc63164-5cee-3f02-a491-036c3a921330 | -14.60219 | -45.63848 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 9750581f-abc3-30ff-b0a1-1140746a3654 | -13.92335 | -47.83146 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 21638c1e-f62d-33dd-85e2-f0ce071fa6b1 | -14.61865 | -45.62426 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a08d71d9-97cd-3914-bc29-71536e14e09e | -11.28963 | -44.01169 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd2e7324-b70f-3a7f-aeee-adfe3395f82e | -6.88334 | -46.56559 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72f95d05-05b2-3b31-acfe-ecfe8cc71cb6 | -12.3043 | -46.39491 | 2026-09-23 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 74d40a65-f19b-31e8-9e22-430ae72d257f | -7.54869 | -48.69519 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03abc5fe-e56f-3602-852b-96b0681fd20f | -14.62097 | -45.63299 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da8015a7-eca9-3740-9e17-5f091b23a501 | -8.33719 | -50.86932 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2ee0616-9050-3612-85fc-ed6dbcc97404 | -11.65255 | -47.80266 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1149f22-d6a1-330b-828c-8b770717b051 | -7.10033 | -52.75806 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c4702554-8828-3523-8290-6aefe2b9cb6d | -14.69682 | -45.58516 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f91e8588-380e-31f5-b0b1-d484b5142406 | -8.75968 | -45.84075 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bff4a5d-2882-3eda-a2c3-4d1abc8d783d | -8.49137 | -57.6152 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ff6d01b-7f7d-3348-af05-546dfcbb110d | -6.64452 | -50.92736 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 090867c5-8ede-31ac-b1a3-f8fb0454580a | -6.29855 | -57.75198 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 890bf0e5-989b-3cde-8ab5-362bcbdcc0de | -11.10173 | -48.33994 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53fc9eb0-67e3-3abe-8d99-8b1d64d233e8 | -8.77832 | -45.62749 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9926f2b3-aaae-3cd2-89f3-1208ddc8d853 | -8.60295 | -44.53599 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cb3e621-a687-3c91-bd1e-9fc92d694a77 | -12.74617 | -50.87513 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ae2d306-c092-3f46-8d22-d99f3de76a2a | -12.81783 | -50.86206 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5113c617-964c-36bc-88c0-ca6727269e30 | -6.67887 | -55.06964 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d967e3ea-198b-3047-9f79-9129bf227058 | -12.79401 | -50.91738 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f7abbe83-7666-39d7-9a5e-f6604601b50f | -10.33962 | -46.53316 | 2026-09-23 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51716d7d-e53a-3343-8334-2b6f41ebe4d2 | -12.03204 | -47.8138 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50105da4-21c0-3c15-a036-64b1b127cf93 | -12.67261 | -45.03342 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3bc7c6e2-8499-3b2b-9a76-c5758cbc510a | -12.81073 | -50.86083 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 692e6d8a-8b25-324e-bd08-03a1d58ea3d6 | -6.62835 | -59.99427 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6576a7cd-73b8-33d4-bc28-18bdde70e8f4 | -6.94467 | -52.60353 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee929a1-93e3-3a58-923c-aba20e8b2324 | -11.68474 | -43.45452 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd32e844-f4e9-32c9-9fd2-25e5588cb74c | -10.21194 | -44.15279 | 2026-09-23 04:27:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e30c98f3-3bc1-3792-8741-f24238cc52b6 | -10.27048 | -49.97267 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 4dbbc32a-1109-3d66-932a-2f28e91a74ae | -11.4102 | -44.03177 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README61.md)
