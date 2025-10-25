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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 685d36b5-fe70-36ea-8c16-1326935dd52c | -9.23864 | -45.58532 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1b57307-a1f2-336c-a637-e47f292f5884 | -10.91161 | -50.16616 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0705ef17-cb32-34c9-9bef-249f1b58423f | -12.07489 | -46.40319 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b6c9dc2-6578-3667-bde5-7642a622337e | -12.15045 | -48.02061 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5ed33645-94fa-3a9c-a172-af496f4f4215 | -10.45014 | -44.96814 | 2025-10-25 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ea12f36e-ea14-3fc6-b386-2d1675da276e | -11.0484 | -47.89062 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00ea30b7-93e9-3998-9345-14280b22ace4 | -12.16494 | -46.56371 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 493d8624-9351-3f3c-b4dd-eb97e6accf97 | -11.01173 | -50.26352 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7e7d183-d24f-3e86-b940-99659c22060b | -8.72054 | -49.60352 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9868a5a3-bea0-3880-a444-3bae490ef62d | -7.39379 | -43.90102 | 2025-10-25 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46b05563-5f50-336b-934b-c4bfc0c1fb0d | -9.30416 | -45.17136 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85f22a1b-bea6-315a-968e-2383362bb5f9 | -6.79354 | -46.46065 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44c22e46-d686-39ea-a3d5-5252a305dc4a | -2.89572 | -41.63219 | 2025-10-25 04:19:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02be35c7-f5a1-352a-baae-52db0d69c2b7 | -6.95897 | -43.48988 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5b3a0a9-2766-3923-a329-fc5daa9f1280 | -10.42217 | -44.49406 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1c39699-2d84-350f-99f9-29ec001748ac | -6.8874 | -43.62023 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 956dfe64-d266-32ae-826e-19b4e44607d4 | -6.76159 | -44.20896 | 2025-10-25 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 522a524e-6ea2-37bc-8b2a-f6b862737d03 | -12.94565 | -48.4988 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd0fdd63-d204-32dd-8430-9c617b6353e2 | -10.58792 | -49.64326 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5452fb8c-57d9-3e10-8d43-d4a2209364eb | -12.48053 | -43.86251 | 2025-10-25 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fd8a0b3-eacd-3e5c-ac61-2a735fe03f2e | -10.6464 | -45.23308 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 448bf85c-18ac-3ef8-af3d-89cb3dfab42f | -6.73335 | -44.15122 | 2025-10-25 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbcb2aec-42d6-338f-965c-91b0743d7122 | -12.05058 | -46.40634 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7050f2c9-5a13-35b3-9f7b-321dff494c85 | -12.23842 | -47.0337 | 2025-10-25 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9b4a0a6-d037-33a2-a572-8d4be28dd792 | -6.95953 | -43.48632 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30b981f8-a9c3-3768-8173-b45ce26d0901 | -9.23363 | -45.63818 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55532467-6bde-3f87-a8c9-8d35f4e37832 | -6.8938 | -46.36318 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3147ba47-d9e2-3e95-8aba-59fbdc2497ed | -12.77209 | -47.37186 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2a7704a-2ae8-3797-a2b9-c4cff9d20e11 | -12.84167 | -48.64841 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ed246c57-33d0-3b04-8bd8-32dccffbce9c | -5.81336 | -50.20078 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53434d48-cb5c-30e8-81b3-8e3968938b53 | -8.00191 | -46.73286 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 730a3988-a64f-344a-b367-c7ad978bad4c | -13.06716 | -47.56467 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8a99c4e-d80b-32d1-b7c3-3c5cc99250b0 | -8.2776 | -46.87214 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc108563-052d-3d48-8cd0-843e636a4ee1 | -11.4326 | -44.67425 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0f40b18-3691-3278-b19a-0f0cbfd1d1da | -7.93388 | -43.2142 | 2025-10-25 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7519e2bd-09da-3725-8eda-24e61c1bf744 | -12.05388 | -46.40695 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4114778-5e63-3032-a830-74ce1d488ac8 | -10.55459 | -47.98557 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24f985db-97ee-3b2a-93b3-77d754cf0b56 | -14.15735 | -44.31929 | 2025-10-25 04:19:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffce356c-1722-34cc-ba61-9d4f01997d45 | -8.14486 | -41.50664 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73dc5b95-b763-3c81-a9fb-e045d3b90eaa | -12.84518 | -48.64902 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9d9c6b78-da0b-3117-8105-75f979b101af | -8.12694 | -47.04405 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b99282e-eaaf-3fd0-ad11-9463fa11e35b | -10.47225 | -49.02909 | 2025-10-25 04:19:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbe15ceb-a38b-3207-8c25-45b99592b3fd | -7.1623 | -45.84148 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 778edf02-0550-3087-8f9b-8bf1374d35dd | -7.33437 | -46.14778 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6efe5e6-d7df-37e6-bb11-09100bb04807 | -6.41949 | -46.19077 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e8efe89-3fd0-3c3d-b757-7da9638dffe0 | -7.85271 | -46.42302 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ba5fefa-3bf4-39eb-97db-3da81cb80863 | -12.81159 | -48.67678 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10191fbe-9c24-35d0-9a37-99b462561818 | -6.25834 | -47.03301 | 2025-10-25 04:19:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c4a4598-e0eb-36c8-98b7-da05ead75cca | -6.89261 | -46.3705 | 2025-10-25 04:19:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ddbd1f0-a97d-3bfe-8438-db81e16086f3 | -11.84818 | -49.86386 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f66284f9-bdf8-3cb3-aa55-e8345fbec462 | -10.68774 | -48.07621 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 020cb43e-da7a-3e2b-a1fa-9102ebfbaa3d | -11.84897 | -49.85918 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bab4627f-4cea-3ec9-be9b-84ed6a0d0070 | -12.79756 | -48.67104 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6f3f015-dd46-3e24-bab3-9d1e4104a05d | -8.24814 | -49.01402 | 2025-10-25 04:19:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9301c5c5-aeca-3358-8a70-a9817b4549f8 | -9.69795 | -45.38849 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8edd522f-0274-3ced-bb0c-b0cc7308b9f2 | -6.81827 | -45.44021 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f91b800-a64b-3dd7-b588-9bba7e71a0f2 | -11.04562 | -47.88591 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b811b2b-fe6f-3ced-a9a3-837506e92476 | -7.79392 | -45.39588 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ca2492fd-4d35-3649-912e-ebbd2b4e6c93 | 0.27363 | -51.39754 | 2025-10-25 04:19:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1e9d2cb-0bd0-3e2c-9d86-23cebb6922a8 | -7.15162 | -45.28953 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24626b8e-8d73-3743-b211-30318cd22d49 | -6.60213 | -48.75714 | 2025-10-25 04:19:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b079bf57-750e-3465-9e56-8d42f9284722 | -13.30289 | -47.45311 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5cc6ff5-bd96-32ed-8e56-18c0117f1963 | -9.19795 | -46.34799 | 2025-10-25 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b47edf6-1e5f-3cc0-abf5-8ddce61d7471 | -10.46957 | -50.20589 | 2025-10-25 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64d59f12-c696-3e8e-a21b-503b210312b8 | -7.3759 | -47.04571 | 2025-10-25 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fd951e1-0ca6-3fea-b501-d8aa128cc457 | -10.39853 | -45.31841 | 2025-10-25 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45e9c335-45ac-306a-995b-eabb95d09628 | -9.32016 | -45.19888 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea0e2697-0935-334f-8204-9f0448abf169 | -10.0679 | -47.08498 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f022883e-d6bd-3d29-94e0-f3edb4632ec4 | -11.3604 | -54.32848 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f1ffbce-8796-3ff6-82e1-fe74a7502d08 | -7.4828 | -46.88361 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e0e17a0-bea4-387a-b524-5b406233e995 | -8.23516 | -46.24797 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef9d9a28-8aa4-3e03-82ba-ed32b357b190 | -6.80023 | -45.4263 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b8f1898-d3d8-346f-9261-5094e74e9f9c | -5.70355 | -49.3188 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c604a645-a2ad-3908-828b-646a41eeec4e | -12.04174 | -54.24127 | 2025-10-25 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 309387f2-5e9b-35c7-882d-35ebcc325bbc | -9.51086 | -46.51679 | 2025-10-25 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 903035a8-bfe9-3000-8f96-3634fdf0efb8 | -13.31506 | -42.42167 | 2025-10-25 04:19:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 41fbc877-71b2-32ec-b39e-e0d129ceb8a0 | -10.10853 | -47.73843 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4d34149-e247-3652-aabc-0eae22870ee7 | -10.42107 | -44.50116 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c0e02ff-51e0-3ea7-8b24-818b886d70a7 | -12.05832 | -46.40042 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f828190-0535-33b3-ac79-8111efd0e277 | -9.71228 | -45.42644 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1384e901-c7e8-3493-89cf-163ebf47e28e | -10.66744 | -48.0686 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 80565974-bd32-35a7-8894-218ab3f09751 | -6.41611 | -46.1902 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cf01ca3-0d6a-3e28-a770-6f27a427d631 | -7.15566 | -44.12207 | 2025-10-25 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24be29cb-5eba-309b-8760-8f87ba2cd327 | -9.71668 | -45.42001 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44555ca0-6102-34a4-a8e9-84dfd1b95025 | -5.86595 | -49.80225 | 2025-10-25 04:19:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f3c4cfa-571a-3cba-82ab-0c0e549c0ed4 | -6.82104 | -45.44423 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d53428dd-2ff9-367e-ada3-c4b4066ae9a2 | -10.55529 | -49.7722 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8b8a7c0-7fdf-37d3-93ac-aa390ede6c43 | -12.83568 | -47.24794 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc352f2b-94e0-3484-9928-775a6141acfd | -6.82308 | -44.01244 | 2025-10-25 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 486e3809-2e01-3903-98e4-335adc110127 | -5.71974 | -49.0977 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6378d829-c25b-37a8-9836-5393092f27ec | -11.5748 | -49.53612 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be049004-df52-3ede-b852-d749605508e7 | -12.05889 | -46.39686 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 819f8a4f-4cf5-3b6a-9e49-962097a467a7 | -10.79838 | -47.85003 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b8b818e-e1ba-39e5-88f6-d3ef4e6e9178 | -8.60609 | -44.81435 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 148e9fb9-6ac8-35ae-bf63-3bb65707753d | -10.9963 | -54.25692 | 2025-10-25 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3c2a730-5d53-34c1-a76f-2f5299eaa724 | -7.03228 | -43.93433 | 2025-10-25 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec64c34d-26e5-38b7-a708-003b3ead2b25 | -14.15791 | -44.31547 | 2025-10-25 04:19:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a709fb8-fdff-389b-8c4c-af2ad426b30f | -8.54967 | -47.38172 | 2025-10-25 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7c6697a-3f96-3ae2-98f3-1747281af8e5 | 1.63248 | -55.74972 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d56453cf-0a58-3fa6-b94e-6aaaf3e3f442 | -6.89851 | -43.61473 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
