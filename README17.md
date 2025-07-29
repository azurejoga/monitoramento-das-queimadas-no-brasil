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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3aa30d2-74cd-37bf-b6df-fe85ad9e22ba | -8.32904 | -54.75291 | 2025-07-29 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee2f6dc8-8960-3d03-9b4d-787ea2d57169 | -13.06767 | -47.37604 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1091a09-4a2d-33f0-a401-8200eb409d75 | -13.12587 | -47.37358 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 787f17f5-b10d-3395-b7f0-b5b85f226fac | -9.28258 | -46.53905 | 2025-07-29 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6030b7bf-dca7-3a84-806b-7bac76e9543b | -6.52346 | -56.21276 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 902f842a-6abd-3d4d-9148-311fb91054b7 | -8.51437 | -43.31665 | 2025-07-29 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a7d9563c-46ac-348f-bcfc-b4c534994897 | -6.49425 | -56.21151 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 296fd1cc-8b32-3a28-969c-689fa4586a1f | -9.87263 | -47.18659 | 2025-07-29 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6f3c5b3-96be-399f-9ae7-d42d2c6a95e4 | -8.63641 | -45.5176 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b6d9c90-b1b7-38c2-93cd-d212cc0e1562 | -11.74094 | -48.18209 | 2025-07-29 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| febe2a11-2bef-345a-b5c0-415804ce34e0 | -9.36507 | -45.74197 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb72157a-8adc-3a59-b027-37879fa284ac | -9.87144 | -44.69428 | 2025-07-29 04:49:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0f08126-f767-3eb8-ae10-61a0a7384bb5 | -9.62434 | -48.55471 | 2025-07-29 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c683210-39ff-328d-8c47-578cd2d1a5a0 | -10.72817 | -51.58437 | 2025-07-29 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1505d1b1-17de-3d9c-93ff-a64d31f01648 | -14.00753 | -44.62111 | 2025-07-29 04:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1827c934-2e2d-3e83-af15-bbabffce0a9c | -7.8613 | -46.73053 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| afdd4b97-614f-395c-84b8-650674afa6a7 | -10.74844 | -58.00829 | 2025-07-29 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f60109f-ae50-33b1-808d-75c20760b8c1 | -13.08823 | -47.31676 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8316c076-b714-3e3c-9194-6301d54db669 | -11.34547 | -51.25075 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7945294-5f27-39e4-90c6-9a75db9863ca | -12.94429 | -44.73345 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d8de0a0-cd76-3ea7-b1f1-85a76b005239 | -9.40096 | -45.49122 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da18f8bc-f23b-3a42-990a-4fe0706fceb1 | -6.52286 | -56.21638 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e16fcc36-9d59-3e3e-a4c8-40a0b84215de | -7.80397 | -46.57625 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fcc966f-a31b-3f9a-a731-3362b15c99bc | -13.1374 | -47.3493 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3f950a9-b560-34d1-bcf2-4c2e1164ccf3 | -14.00258 | -44.62052 | 2025-07-29 04:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24b37ae9-f104-3d04-9e3e-eaddaa3df14a | -13.07618 | -47.37424 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fc4db50-e376-3f83-816a-45a6e8f2a662 | -10.15176 | -51.20434 | 2025-07-29 04:49:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e93a02-abc3-3d09-a4cc-0fe958cb276e | -11.33934 | -51.24612 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1404324f-324c-3ed2-9861-4e0a19aed003 | -9.58129 | -44.4627 | 2025-07-29 04:49:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a65ce48-6206-32ec-9d03-23f4d1369db4 | -6.50304 | -56.20927 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 573b8894-7cdd-3322-a9f9-e4acf1698e4d | -7.73074 | -51.10801 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 555a26e5-4c0c-3f31-97f6-41b152c324e4 | -11.29241 | -55.13521 | 2025-07-29 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de9436b6-7589-3aeb-8850-727c05d20ffb | -8.94357 | -46.7442 | 2025-07-29 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbac375b-449c-32d0-9906-3ee6019911bd | -10.00485 | -48.12671 | 2025-07-29 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0d6b4c1-01f5-31f0-981b-9675e758b914 | -12.94911 | -44.73416 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fecce76-1f78-3b13-8582-dd7357abddc4 | -6.90429 | -52.86592 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e9516a2-a669-3cea-ba71-40239e3055eb | -12.94152 | -44.73095 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fa46bb4-cab7-323a-9d44-602dc92d56f1 | -6.50079 | -56.19767 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 541acf1d-8f99-374d-86f9-69ed537db5ec | -7.81224 | -50.22257 | 2025-07-29 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00312e14-beb2-3a76-b2dc-76b9abc4746f | -12.00465 | -46.96152 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cab0351e-f237-314f-a025-635b08ffeeac | -7.73792 | -51.10558 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c8a7523-1056-3e2d-80e7-7fa301a3bab2 | -6.90147 | -52.86169 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff656718-9698-336e-9bc7-4833b7ca99f2 | -6.49115 | -56.00841 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a12c47e-db0e-3630-9f52-b4b289d1ab75 | -7.45835 | -49.39684 | 2025-07-29 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d3ec380b-d832-375f-8fdb-fbb96840bc8c | -7.85809 | -46.72495 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41cb933b-9dae-3c74-9ee6-78b5dcb0d7b6 | -13.24931 | -50.13124 | 2025-07-29 04:49:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff002438-4eee-318e-a745-6a0ad82e691b | -10.93289 | -45.78891 | 2025-07-29 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a20b1257-cab4-396c-afb6-e843adb2b55b | -11.34937 | -51.24771 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4871cdb7-ed6a-3210-ac36-b08b21bb4cea | -7.85737 | -46.72997 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b6d1ec5f-a26e-3d8f-8ade-3173b65a9d0d | -12.00099 | -46.96944 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fd92a2c-ed25-349c-9361-9aeb9e77e79f | -7.72687 | -51.11096 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93e9dab0-991c-3529-b299-289b6b0776c4 | -7.74842 | -51.10367 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc79a79e-e3e7-3923-8bc5-71a3ea0cb8e2 | -6.49773 | -56.21582 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa5f0d2d-e3b4-37ec-8be9-e4cd071436ae | -9.58661 | -44.45866 | 2025-07-29 04:49:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beb1bfdd-c238-30f6-a151-f5768941accb | -8.49263 | -47.31824 | 2025-07-29 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc7e6b72-2690-3034-91bc-6a3ab6ee9bec | -11.34268 | -51.24665 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4c57363-7040-3a7b-910c-644122f8df44 | -6.52754 | -56.21348 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c69e759-29f6-3b46-bfe1-72e347567ee9 | -7.81559 | -50.22309 | 2025-07-29 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10a7f0e9-9416-3847-9af0-8bd6dde472b2 | -8.94282 | -46.74945 | 2025-07-29 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6d303d1-aa69-313e-bb69-da78e157d28a | -11.99856 | -46.97571 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecda227d-de79-3c29-85df-4059699c527c | -13.2528 | -50.13177 | 2025-07-29 04:49:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c92af69-72f5-38b5-8153-1aae50224179 | -9.9974 | -48.12571 | 2025-07-29 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d0b276c-0612-3fbb-bfbb-1413c6738531 | -13.10815 | -47.38209 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 075b3c24-7474-3321-a46b-09fa1215bcec | -11.43174 | -45.13077 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| abeb48c3-b15f-381b-836e-45ef6ea63cca | -8.13525 | -49.51013 | 2025-07-29 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fa1bc3b-31a9-34fc-b198-85c4c0605433 | -11.981 | -46.96296 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e89f8a81-6c02-33b7-b5cd-af695463ec22 | -12.99214 | -44.89585 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d849ebff-f0fe-37ca-98f5-b79a650523f3 | -12.00203 | -46.96207 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0c341047-c2a7-38e0-affa-4db943fdcf74 | -10.66962 | -56.55178 | 2025-07-29 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfd55c6b-19d0-3e17-b978-143052d8df06 | -9.45612 | -57.84915 | 2025-07-29 04:49:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 34dfe8e4-e9ea-3f06-af20-c4604dc14cd9 | -11.64369 | -55.68258 | 2025-07-29 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbc05833-a9c2-3e75-89d1-fc5241a06d4e | -9.22013 | -48.59676 | 2025-07-29 04:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dac3653-6dfe-38f2-8810-e5fade021abd | -7.86195 | -47.87348 | 2025-07-29 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ea03175-daff-3abf-9568-8fb5602c0a96 | -13.52423 | -45.62442 | 2025-07-29 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff7f68d8-40ba-3a4e-b0c1-667798892924 | -10.00113 | -48.12622 | 2025-07-29 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c7d7cf2-f664-33e3-aeef-3be7a7d8e6a0 | -11.9995 | -46.95044 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96208258-78b3-3e74-ac56-77eb172f3723 | -13.13639 | -47.35683 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b2ab120-4798-301b-a493-f13afbfea960 | -12.00104 | -46.95725 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b620d0b5-9a96-3908-94c7-d3c4f237c2a4 | -6.49895 | -56.20858 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c57a26d1-8e83-3650-a49a-d55b77a50151 | -11.37774 | -48.99993 | 2025-07-29 04:49:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61296e0d-96db-3b2f-8abf-de45967b25da | -8.2901 | -45.00229 | 2025-07-29 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71789898-8ae1-3507-97b2-0a8215e11d6e | -12.95048 | -44.7376 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d7be90b-7c8e-36bb-be16-74fec7c77cc1 | -13.13409 | -47.34477 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee4baced-944e-32ad-9790-980f4139344f | -7.35809 | -50.8103 | 2025-07-29 04:49:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7115800-864f-362b-a832-7f1b8e0395cf | -8.36965 | -51.07364 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba4f750a-2638-369a-8140-d919523a74b6 | -10.74414 | -58.0075 | 2025-07-29 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8650abc1-a48a-3ad8-9d2f-5f72b347a0a7 | -13.06844 | -49.23863 | 2025-07-29 04:49:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56314c5e-3294-3abb-a192-367c64e7af59 | -12.00055 | -46.96095 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18cd0990-7ff5-3fd5-b473-493c2df09c63 | -11.34603 | -51.24718 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a16827c5-3713-3f59-9816-8771db006554 | -13.00174 | -44.89692 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d40b1d6-68c8-3bc0-b509-8d33e9d8bffc | -11.43236 | -45.12605 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d8ec4eee-bcec-3745-a861-9bd8ba18c0f4 | -12.12729 | -56.91567 | 2025-07-29 04:49:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66f20dc4-6a69-365e-a1e4-b9aee113bde9 | -8.9508 | -46.75055 | 2025-07-29 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bc2fe78c-3df3-3041-915e-81b4fdd69596 | -9.36449 | -45.74601 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec24080f-a9c3-388e-9fe6-2dfd7638d34b | -10.62698 | -45.22831 | 2025-07-29 04:49:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdd6636f-9d8c-3a04-b7c1-e70734501ac4 | -9.36427 | -45.71706 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d51ab1b-e60b-3896-883c-1516a9709890 | -13.0687 | -47.36853 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fee4b0bf-4d02-3abd-840c-da42f8c16afc | -11.43112 | -45.1354 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 0a09e301-d349-389b-8e5e-e46ba615c4bf | -11.99584 | -46.97624 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df05839e-be1d-3dca-a071-278d1950c331 | -7.45778 | -49.40055 | 2025-07-29 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README18.md)
