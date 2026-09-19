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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29e6d561-c6a5-303f-a3f7-5dc5b9730eec | -3.331 | -59.8292 | 2026-09-19 13:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 223b8369-4bdd-3b3f-8b29-41cb79936a22 | -11.1038 | -49.4406 | 2026-09-19 13:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b97a42df-f348-3560-8e4d-3579866ceece | -12.4841 | -50.0532 | 2026-09-19 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 973a430d-10e2-36d8-ad61-6cf9129c9ab4 | -10.6703 | -50.6465 | 2026-09-19 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 180.4 |
| cd6a8459-2811-30e3-97de-43d78d69a68f | -6.4667 | -45.2116 | 2026-09-19 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| d8339650-db7e-3690-811b-3f3ce0597510 | -10.8282 | -50.1601 | 2026-09-19 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| a4670ad6-13b0-3c0e-b917-b4f6255008b3 | -5.6408 | -43.392 | 2026-09-19 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5c95c0f0-cd76-33e9-b766-7208359404fa | -11.0608 | -49.7909 | 2026-09-19 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| bc579416-eb97-3aab-a26b-7634953f259c | -9.0096 | -44.9209 | 2026-09-19 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 84f406e9-2a80-3fcd-844d-283f8e870925 | -11.949 | -50.1186 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 0009c129-dcec-3867-a1aa-4ae8d4f59ffb | -9.2567 | -46.2098 | 2026-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 12316e02-d87f-39a0-97e7-5bd800d69e78 | -10.567 | -51.3137 | 2026-09-19 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 194.6 |
| b9d22af7-cf52-3028-ab86-47ccb3b9cb32 | -6.2582 | -41.6858 | 2026-09-19 13:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 9a14ff7a-76a1-3fdf-9768-d73979473b31 | -11.9487 | -50.1402 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 7987d87b-6cd0-3d3e-a64a-7b3aa8d58af5 | -11.0065 | -48.3187 | 2026-09-19 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7c79ad73-0b34-331c-b845-49c2be42d6e8 | -10.8469 | -50.1795 | 2026-09-19 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 01d745b8-c0d0-3d22-b117-045591293ef1 | -12.5032 | -50.0508 | 2026-09-19 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 710ce3ed-6dab-348d-84f7-a82230123396 | -12.027 | -50.0015 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| ded6afe3-75ec-3b97-bd4c-b940b024a3f7 | -12.0082 | -49.9822 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 75b399c0-f77c-3c53-9d7d-27a849a00567 | -9.257 | -46.1873 | 2026-09-19 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ed3a3e65-3d36-34b7-95d1-2bdd4372f6f4 | -9.0358 | -48.727 | 2026-09-19 13:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 104.7 |
| f9177f5a-a3c2-319c-bf6c-6da83d0a1668 | -3.3493 | -59.8288 | 2026-09-19 13:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 88ed04de-c012-3f35-9dc3-aaaa4a875e37 | -12.0076 | -50.0254 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| de13c820-9709-3e97-81e0-27e7cc599ca4 | -11.9112 | -50.1016 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 605d6170-1278-3e39-804e-292131ba0ad3 | -12.1339 | -46.9734 | 2026-09-19 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 736e3c5d-a89a-3429-bdd1-f2cd70c36666 | -9.3611 | -48.3032 | 2026-09-19 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6a23c6fa-bb56-37ce-8c81-3f755f96d759 | -11.9299 | -50.1209 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0068ee43-6838-3032-9c9b-a506b044781e | -13.892 | -48.592 | 2026-09-19 13:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 6b0a98d0-5011-3979-a03a-a7718fa95bca | -5.9344 | -42.0966 | 2026-09-19 13:10:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| 14f09ed5-edcc-316b-b9a7-d97f1ab88639 | -8.7731 | -48.6868 | 2026-09-19 13:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 2fe30915-eff5-3a65-9a75-24f6a4d08e86 | -10.9665 | -49.7583 | 2026-09-19 13:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 3695dbdc-a261-36da-9934-4bf5b05491c3 | -10.5364 | -46.7568 | 2026-09-19 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 4ba96a76-eb36-3438-97e3-e6da2021d280 | -12.0267 | -50.0231 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 80ba961e-bfda-313c-a829-d8a00289a8f0 | -8.6628 | -45.4379 | 2026-09-19 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 2398bab5-aba2-3e34-b13d-9fda0416e6b9 | -7.1169 | -44.0339 | 2026-09-19 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| ca357344-49c2-31d1-94e8-0bd849f9cb83 | -11.1369 | -54.0251 | 2026-09-19 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 409.6 |
| 13d2e3ac-da5e-3099-999e-841786ef62a6 | -12.7085 | -45.96 | 2026-09-19 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 63c187cb-9f38-3d73-ae65-7d1aeca76e73 | -11.9109 | -50.1232 | 2026-09-19 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 17073567-96d8-3141-bb99-3f87fc5e5317 | -11.0062 | -48.3407 | 2026-09-19 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 65c600fd-87e7-39ff-832a-6e21a28aa36e | -11.0611 | -49.7693 | 2026-09-19 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 17c585bc-870d-3448-a131-23c5be9ff1ae | -11.234 | -48.3571 | 2026-09-19 13:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 175.8 |
| b30977ce-0bb0-399f-8b81-df8e1845cdb9 | -3.3311 | -59.8101 | 2026-09-19 13:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 8c701ef8-2972-35b1-9cd1-5839d8a8ad0f | -6.2585 | -41.6617 | 2026-09-19 13:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 150.1 |
| 6b073f68-5d18-3138-b536-4be798b8034a | -11.8934 | -47.6322 | 2026-09-19 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 6a2fab4f-72fb-316a-8273-a7943e69e7eb | -8.45 | -45.8674 | 2026-09-19 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 6123c970-f533-3bf4-9fb5-6730c7523646 | -8.8827 | -45.935 | 2026-09-19 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| aabace4d-ee50-3bc7-94dc-2d1d0df3dc52 | -9.0087 | -44.9897 | 2026-09-19 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0db40d28-8265-3470-93f4-c2d62a10ee3a | 1.22 | -51.01 | 2026-09-19 13:15:00 | MSG-03 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e3e68c2c-690f-3cdf-9d80-894ab24d5710 | -3.58 | -43.46 | 2026-09-19 13:15:00 | MSG-03 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28087813-ba5a-32ed-a13f-e32c63bdb75a | -3.55 | -43.46 | 2026-09-19 13:15:00 | MSG-03 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db99f8d8-efb7-3df2-976b-7c0fe6ca0411 | -12.29 | -49.2 | 2026-09-19 13:15:00 | MSG-03 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5e89a5f-5176-30af-8d43-31c0461a814e | -7.8598 | -44.8595 | 2026-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| b4ee24f1-8543-30e9-85d9-611bfaeb30f3 | -7.7629 | -46.7389 | 2026-09-19 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 03c4b43b-096f-3e3b-be94-982a9156855c | -10.8279 | -50.1815 | 2026-09-19 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 306ee885-3f5c-33de-b342-11b593323887 | -11.0062 | -48.3407 | 2026-09-19 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c1fc38a1-c82b-3657-bf8d-5f1059a282ff | -12.4844 | -50.0315 | 2026-09-19 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a795076e-9065-3eb3-adb3-22e40e1f70b1 | -9.2567 | -46.2098 | 2026-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f664decb-c136-390d-aa9f-ba589622d2b0 | -12.1339 | -46.9734 | 2026-09-19 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 172.0 |
| fd1aaacb-a206-3bab-93c2-869868e8007d | -12.4841 | -50.0532 | 2026-09-19 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 7867e761-7ddb-3920-9c89-e5d0c7031778 | -11.9109 | -50.1232 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 46a97761-c9f2-3900-abe0-89636a668120 | -11.0801 | -49.7672 | 2026-09-19 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 17828543-0d4c-308a-b22f-17bc158f09ac | -11.7823 | -49.8152 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e3a9124f-41c9-3b35-a61c-7ff108960122 | -8.8827 | -45.935 | 2026-09-19 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 66edf565-e6b1-38c2-bc3e-1c1619dc8c6d | -12.0267 | -50.0231 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 78c3e1f9-eb83-31c8-80db-cf7c21d16514 | -8.7731 | -48.6868 | 2026-09-19 13:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 127.4 |
| cc858039-530b-336f-869c-4e63bc5167d5 | -12.5952 | -49.1046 | 2026-09-19 13:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| ae19e8a1-42ba-3360-bd6e-2323089dbdf0 | -13.892 | -48.592 | 2026-09-19 13:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| ca7ed9b1-ffbd-3c27-963c-55cb3a364bdb | -10.7133 | -50.258 | 2026-09-19 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f24c21d5-b3c5-305f-b8ee-33f5b2d789bb | -6.2585 | -41.6617 | 2026-09-19 13:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 167.6 |
| ee9ba8f9-de90-3eab-811f-bda5864387f1 | -12.027 | -50.0015 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 7e1780c1-dab9-358b-9f38-539884da6cf2 | -12.5032 | -50.0508 | 2026-09-19 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| c28202be-6100-38d9-8741-8b45bbd751c4 | -8.4503 | -45.8448 | 2026-09-19 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 76f7b009-e103-38d0-9eab-241fb887bfd5 | -3.4454 | -58.2327 | 2026-09-19 13:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| b8a708d5-43ad-3c06-9f22-0031fc5398bc | -12.0082 | -49.9822 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2eebd3c8-f7a3-30cf-84a6-a5276aea4a3d | -10.5667 | -51.3349 | 2026-09-19 13:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 781d42cb-8fbc-3566-a179-6d37f05b9ec9 | -3.4455 | -58.2134 | 2026-09-19 13:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| f8c2f895-1783-3e87-bbcb-f3c77d165fdc | -7.174 | -47.4956 | 2026-09-19 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bacaafef-31ac-3f86-b96f-e4e39d484ffb | -12.0076 | -50.0254 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 5fd37ed8-edc3-3bdf-9744-4332c7261b7d | -11.949 | -50.1186 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| af21040d-91a3-3da4-bbc5-fb6cf6e3af68 | -12.1535 | -46.9482 | 2026-09-19 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 39862a29-8256-33ab-bb47-ad4e04eda8ef | -3.5654 | -43.4727 | 2026-09-19 13:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 451.9 |
| e553d8f9-3dee-3b15-aedb-a5def91e7804 | -11.1228 | -49.4384 | 2026-09-19 13:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 9a0f7294-149e-31a3-bd05-fa87a89b8f6a | -11.318 | -51.7218 | 2026-09-19 13:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 417780f4-9d44-31dd-8027-50f91eb2897f | -3.3493 | -59.8288 | 2026-09-19 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a3091dfc-e1b4-3951-bf2f-92aa0c4621b5 | -12.7089 | -45.937 | 2026-09-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 41e5ad3f-3401-3aad-b08d-c9004b24a49c | -12.1336 | -46.9959 | 2026-09-19 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f85c9c1c-c37f-3d3c-b3f0-8f8ae06b9b7c | -5.9344 | -42.0966 | 2026-09-19 13:20:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 148.8 |
| 5b6bfffb-a941-3ccd-ad98-c40bd3df2326 | -3.331 | -59.8292 | 2026-09-19 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| db6cbd4e-2a52-3336-b16e-25f6359791c1 | -11.3166 | -42.3313 | 2026-09-19 13:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 7e254838-af3d-3518-b06b-fca7ac615d8b | -3.3311 | -59.8101 | 2026-09-19 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 132.7 |
| f2222319-b1ae-309f-b579-0581b47ddaf8 | -9.9699 | -46.6004 | 2026-09-19 13:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 049f5b87-1821-37b6-a55a-3c2228133caa | -9.9706 | -46.5555 | 2026-09-19 13:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| b7b56079-5b73-3009-838a-eae23c80d323 | -6.001 | -51.7903 | 2026-09-19 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6fee1b94-3623-3313-8822-30374eef7fdb | -11.234 | -48.3571 | 2026-09-19 13:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 67385d67-6c92-3588-b234-9edace174b95 | -11.9112 | -50.1016 | 2026-09-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 49689d17-215b-3431-b757-2c6a50f4f914 | -7.1553 | -47.4971 | 2026-09-19 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 38081567-e89e-3c7a-9860-48b5f5ed6b4c | -8.6173 | -54.5924 | 2026-09-19 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2050831d-464d-3e10-a828-1a7057490851 | -7.1169 | -44.0339 | 2026-09-19 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2adcc8c4-bd64-32fa-a0bc-cfeb85ebed3d | -11.3355 | -43.403 | 2026-09-19 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 7ab5ee1a-363f-3362-9e7c-0d1d2b9c87ba | -12.7085 | -45.96 | 2026-09-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 325.9 |


[Clique aqui para ver as próximas entradas](README109.md)
