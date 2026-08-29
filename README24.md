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
| c82f17cc-3a62-3b7e-af9f-f14b09376a2f | -10.92765 | -46.61195 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7fb27c7-44ec-3aae-be07-aff0265f7a75 | -7.2953 | -49.97439 | 2026-08-29 03:55:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69f79fd0-9169-3d3c-8037-22973d8d9354 | -4.28596 | -48.18783 | 2026-08-29 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a0c776a1-ea08-34e8-90fa-50b266dfa2ac | -7.09778 | -42.83682 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5a125c3a-9f89-3ba4-b0a3-b86e5cda0f8b | -11.23817 | -45.07954 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdaa94aa-64fb-3f51-9296-3f789bd64ea4 | -7.07107 | -42.21373 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68235180-256f-3102-a6ca-5c129a282327 | -6.34471 | -44.09534 | 2026-08-29 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6ebb81be-d365-329e-a2c8-c504a57e0495 | -7.5317 | -44.45394 | 2026-08-29 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eabc2f4e-34d2-390a-b614-2a348f256248 | -7.19958 | -42.73567 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bf9a2b32-153e-3862-8c3e-5b18f7e607a9 | -6.62422 | -43.74071 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2f66bfc1-9147-3508-8ca7-73e833dbd2b0 | -12.43413 | -42.88916 | 2026-08-29 03:55:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e7346e9-eb20-38c8-90bf-10bd9d1c9c77 | -6.4131 | -51.67006 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50eefc9a-1323-3b8f-9c1f-8427a78cfeff | -10.54181 | -50.47121 | 2026-08-29 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3fe9923-685c-3df6-a499-d012bf7a565c | -6.61956 | -43.74363 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 139ce126-f801-3093-85bf-afd0657a0ef7 | -6.4044 | -51.6738 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46c2cf58-a936-33b0-8020-a81b0c61883b | -11.2423 | -45.08021 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 999313e0-4bc5-320f-8aff-00365b07b552 | -5.3127 | -47.04987 | 2026-08-29 03:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a92c10d-5a41-3c60-99f4-ff933345d92e | -7.0619 | -42.15408 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c182f1de-616d-3046-bca0-6fb2d1484e06 | -7.20337 | -42.73631 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b4822ce2-f33a-3e26-b9d9-01f2db158436 | -11.25508 | -45.05571 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b879097-98ff-3a55-9b47-721baf2e873d | -5.34005 | -45.16099 | 2026-08-29 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 846269d8-b203-3462-a36d-d2dae4066792 | -7.30764 | -43.01649 | 2026-08-29 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9dc35302-28ab-388c-99f1-4c6f8321a717 | -8.16249 | -46.17596 | 2026-08-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c6f7326-62d3-366f-b1cf-50b584bfd1a2 | -8.11795 | -46.78489 | 2026-08-29 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85f8fd41-75be-3ae0-98e7-c19c12f161a6 | -11.25251 | -45.07043 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a017c9f-bce9-37f4-be0d-b78b8cb1c29f | -11.48573 | -45.10276 | 2026-08-29 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 19fefec1-dc32-3faa-8465-8ba3ab80e9c3 | -9.15581 | -43.28567 | 2026-08-29 03:55:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e1010073-583c-39e3-b49f-3b830a64f6c9 | -9.26772 | -45.64375 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a137f0c7-ec4d-3379-aa45-8116fc4baaa1 | -7.60581 | -47.29069 | 2026-08-29 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 893cdee7-9f50-3018-895a-c297e347197e | -6.92933 | -42.67704 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e691dd0a-668c-35e0-b521-789937b358da | -10.92306 | -46.61112 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c6f2270-a12f-3fda-bc61-0fd6289966ce | -10.53726 | -50.47887 | 2026-08-29 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56add121-1813-32d5-9d12-e9e89c651eaf | -6.34053 | -44.09462 | 2026-08-29 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8216ed86-c136-3284-91d2-144a32ef219e | -6.63181 | -43.74548 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7dad4f18-6cf9-35a9-bdb3-68c947c8802b | -10.90842 | -46.61359 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f855511-f645-303b-9463-ff53f4463574 | -11.23883 | -45.07578 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 361d01d4-7bc4-36a2-a8d4-5a34d59a6f5d | -10.92217 | -46.61464 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e253e70-e2cc-3bdd-bdb5-369289634257 | -9.46701 | -45.6461 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7b350d8-0929-33eb-8133-8e1a475064ca | -8.72053 | -41.13121 | 2026-08-29 03:55:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0244443b-c21f-3343-bb8c-313241d4163e | -7.28567 | -45.85489 | 2026-08-29 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 66fbf7c2-7b1c-3bcc-b4c1-0201b7b32da1 | -8.66256 | -49.54568 | 2026-08-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a86c81d2-9884-361b-8c83-988ec998d89b | -5.34461 | -45.1618 | 2026-08-29 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 614473b2-78e9-37ae-832b-396a5d4f1ec8 | -12.43509 | -42.89074 | 2026-08-29 03:55:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5faa8093-2a86-3475-880e-93893baccc19 | -6.6271 | -43.74867 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9555ce80-44e3-302a-a741-d64b35b173fe | -10.90927 | -46.60876 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80ad5563-b0be-3759-8b9d-2a60ffc94c00 | -8.66757 | -49.5509 | 2026-08-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3994f66b-7164-321e-b9b4-d8cbc82005ce | -11.36685 | -45.16043 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d8c711b6-c035-3332-a481-fe6d73cd52fc | -11.36272 | -45.15965 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e2efc2b-1b4d-31e6-abd0-dc3c495403cb | -4.91448 | -43.47096 | 2026-08-29 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 28a2390a-1fb0-3c6f-beb4-85e7b4a4ae18 | -10.85928 | -44.80481 | 2026-08-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 396f7b40-e78b-3c85-9878-d703a3f4e991 | -7.07844 | -42.2149 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3ed72f77-ac6d-3ee5-a861-35e3ab25dbc8 | -11.615 | -46.72944 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48bd0494-e013-34a5-862c-736daa2ba875 | -10.83686 | -50.50697 | 2026-08-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5af3be9-42e6-3344-b207-1791916c00cb | -10.75295 | -42.10678 | 2026-08-29 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a23c3738-632f-3c07-80ec-efc77b9bbafc | -5.60913 | -44.00193 | 2026-08-29 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da22b725-6159-340b-a546-3b1e7d63a911 | -11.49612 | -46.94487 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfbc0054-3c36-3ee5-9418-aaee7a26610f | -6.6277 | -43.74503 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 666ecf70-332a-31c8-9007-063031622111 | -6.8447 | -42.86241 | 2026-08-29 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a62b446b-a55b-36a8-a864-3e1c3dba2b01 | -8.0133 | -48.0093 | 2026-08-29 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28c3febf-de14-3d3d-92c5-59fe5080fac4 | -7.53589 | -44.45472 | 2026-08-29 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c103cf1c-fa17-3abc-be19-04b58bec19f3 | -17.05844 | -39.86154 | 2026-08-29 03:57:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67d9ee87-b3eb-3b45-b120-70d360587ae1 | -17.11051 | -43.25469 | 2026-08-29 03:57:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af853adc-dba4-30da-9176-8cb713797ee3 | -18.78424 | -45.59813 | 2026-08-29 03:57:00 | NOAA-21 | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a56d035-40ed-3fc9-9ad5-72b4978613b0 | -12.25242 | -50.53911 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9417fe77-7131-32f1-a020-5ffe878087fc | -13.65797 | -47.73505 | 2026-08-29 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3bdad12b-7e54-3942-9568-9aa8328ccca5 | -13.35206 | -43.65284 | 2026-08-29 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fb13e7e-7332-38ed-b171-0cb0f4851031 | -14.89418 | -52.62813 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc829881-b7cc-3a67-a15f-0ac3978665ac | -17.59425 | -51.61491 | 2026-08-29 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2dac5b8d-9058-3f99-8559-a85a186f5594 | -20.15708 | -40.19555 | 2026-08-29 03:57:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 261ef346-7736-3f48-af41-854ad02f8669 | -19.29074 | -45.81616 | 2026-08-29 03:57:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17f420df-9312-313f-b3e1-497a24843aa0 | -16.48011 | -49.42779 | 2026-08-29 03:57:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdf5ad0a-6d35-3371-adca-2dd843298d9a | -14.19282 | -48.75396 | 2026-08-29 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2505eb8e-26f0-3800-b54a-f36f571bf191 | -14.89536 | -52.62259 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcf4d425-5c04-3eb6-8d58-c8460ed5566f | -12.77525 | -46.45108 | 2026-08-29 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b07d45a-606d-30ad-ba01-8ff685b93114 | -17.27978 | -46.02785 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4793467-c9e5-38ed-88c7-3584234980d8 | -14.92414 | -41.30591 | 2026-08-29 03:57:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f7406a71-073c-3167-be4b-773811c5efe9 | -15.19486 | -42.38644 | 2026-08-29 03:57:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4efd4e65-cdf1-38b0-b992-cb3ad53fb37e | -14.40541 | -52.57024 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98a12908-e2f1-3b5d-ba17-9c6899299640 | -18.10256 | -47.89938 | 2026-08-29 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1cfc261-962b-39de-b44c-744529306d07 | -13.64923 | -47.73679 | 2026-08-29 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83c264c1-2877-36bf-9af9-bb896ac0a45d | -14.41261 | -51.74213 | 2026-08-29 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec0409a4-ec96-341f-82da-15595e67c3fa | -13.32109 | -48.19345 | 2026-08-29 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 917c94e8-432d-3753-b167-fac53fd3a806 | -17.29067 | -46.03562 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f1283b5-3c97-30e5-a793-b632c1fc1761 | -15.64608 | -45.923 | 2026-08-29 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5817109f-ce1b-3d15-b0c6-62f0ae31c540 | -11.17978 | -51.29083 | 2026-08-29 03:57:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af541911-7898-3664-a1f3-0b48bc061e6a | -15.10269 | -48.15643 | 2026-08-29 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b23e491-ecaa-32e5-aedb-784eda83d5ac | -14.80401 | -42.39115 | 2026-08-29 03:57:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 61b4ff9a-3fcb-35ce-9292-96a170c85a0c | -12.24087 | -50.53582 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49a2fef1-4a2a-38e5-83b7-24d6b836097e | -14.911 | -43.41264 | 2026-08-29 03:57:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96fd8325-6377-326e-b1ff-b5f0fba0c66e | -12.784 | -46.45289 | 2026-08-29 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 73476a51-9cb4-39d4-af6e-6d95b5d5bee1 | -17.28767 | -46.02957 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e99a147b-c092-3963-ac4d-d89e2aef78d3 | -20.15576 | -40.19615 | 2026-08-29 03:57:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 39d163c4-5c9e-388c-a83e-827284673a6f | -12.20285 | -50.54648 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d91fe47-e82e-38c0-bcc2-e2688b04fb7e | -14.07936 | -44.06232 | 2026-08-29 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| accdbc31-2ef0-3b19-aa3f-2ebe60c5fa69 | -14.75698 | -48.75233 | 2026-08-29 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39694072-e524-37db-aba7-1a2e90efa595 | -17.51132 | -40.26108 | 2026-08-29 03:57:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fe72945d-ae41-307a-89df-df6488fdc118 | -12.25244 | -50.53814 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b89df27d-1974-3dd8-a86a-c9f1f47db6d1 | -13.24966 | -41.32581 | 2026-08-29 03:57:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b9d1b32b-2841-3ebe-971c-bbaf2acef7fa | -17.24111 | -46.92344 | 2026-08-29 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa9d4fec-55d7-3116-9d36-d6153c306cf7 | -15.89521 | -41.88849 | 2026-08-29 03:57:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
