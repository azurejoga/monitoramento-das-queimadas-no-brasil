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
| d4747e5d-14a1-304d-a73c-31312efe7986 | -13.967 | -54.395 | 2026-09-01 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 555.0 |
| caa8f7c9-c01c-333c-897a-c2aabfbbe930 | -7.4365 | -61.4051 | 2026-09-01 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ab83df5d-66e6-30dd-95fe-d5fdcf159bd6 | -11.2478 | -45.1425 | 2026-09-01 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| f930cef4-ca79-37a0-8350-4fd109283efa | -6.1844 | -57.7395 | 2026-09-01 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8422810d-a7cd-3afd-8faa-b45ed7f2d29b | -3.6398 | -60.5656 | 2026-09-01 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 205afa76-b912-3dab-a4ec-64b016272378 | -10.3388 | -49.9977 | 2026-09-01 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e841da88-2fd6-3b47-aaad-5ae8dbd917eb | -11.0434 | -49.6851 | 2026-09-01 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 57d48a6e-53f2-3571-b520-5632ce36ed2a | -6.6037 | -58.5779 | 2026-09-01 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| c5c6421e-fd5d-3407-ab43-20a8f196c4ce | -10.2212 | -50.3303 | 2026-09-01 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 9d4fce9a-1c55-3d42-9889-ee4c1c63acd7 | -6.6233 | -58.383 | 2026-09-01 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e8134310-4537-3172-b007-f011fa2107ee | -7.5709 | -60.4835 | 2026-09-01 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 1243daea-4be8-3ba5-a9bd-06cdcbf92866 | -5.9636 | -57.6704 | 2026-09-01 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 06b6a4d3-ef59-3077-ab1b-25952a057f43 | -14.7302 | -53.5966 | 2026-09-01 15:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 7ec9f8b9-9889-313f-9a66-4d224026e1f7 | -13.0704 | -45.1661 | 2026-09-01 15:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 01c7c2db-8fe7-3818-975c-f377b4d753e4 | -10.3205 | -49.9567 | 2026-09-01 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2050f55d-ecf1-333e-9a98-479c01b372d3 | -13.3946 | -51.7382 | 2026-09-01 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 66d0e3b7-2c9f-3135-a26b-e39470797bdd | -11.5279 | -45.5162 | 2026-09-01 15:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| bf1da9a1-433a-3dbd-857d-821327a76765 | -12.1457 | -44.196 | 2026-09-01 15:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 9e0df04c-f842-3de4-b7c2-9a29ef485424 | -7.5658 | -61.3811 | 2026-09-01 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| acafc4c4-23a6-37f1-928b-9a700dc66fd4 | -6.3723 | -51.7486 | 2026-09-01 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 150b83f9-fb78-360f-95cf-aa5ae48bf491 | -14.4011 | -52.5014 | 2026-09-01 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 65be89b4-af91-3b63-8637-e7d1c679c621 | -8.9242 | -63.2804 | 2026-09-01 15:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ad9fa2bc-f663-3330-94e8-ab717db06abd | 3.9353 | -59.6446 | 2026-09-01 15:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 46b0ac48-ba72-33e8-b558-25b22c61d21d | -9.3873 | -60.5721 | 2026-09-01 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5757964a-6a5b-338c-834c-0f443b7b12a4 | -11.2957 | -50.6008 | 2026-09-01 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 3613d7df-0cdf-3be7-905d-ae25d35f9e89 | -14.4397 | -52.4964 | 2026-09-01 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c045cbd1-871a-3f83-b0a6-b95aea7a42fe | -8.7631 | -46.4418 | 2026-09-01 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6b73ce3e-9680-37fb-9510-059ad47bc5f2 | -7.2255 | -42.7616 | 2026-09-01 15:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 3b4cbdbf-1a3f-3e63-813e-398eb0ae15e9 | -3.5162 | -59.0405 | 2026-09-01 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 7053749f-377e-3457-8ab2-90e1022c62c1 | -7.4364 | -61.4241 | 2026-09-01 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 978f7df9-fb8a-33d8-9e64-09fdfc9f37f6 | -6.8217 | -43.5271 | 2026-09-01 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 171.1 |
| a0bde3b3-ad60-3437-af1b-0027a21ebfb0 | -11.0744 | -51.5365 | 2026-09-01 15:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| b8b73c88-a98e-35b4-92c0-c5961df5e27a | -8.5792 | -54.6758 | 2026-09-01 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 408f4282-0a26-386d-a447-c2778bcecef4 | -13.3751 | -51.7619 | 2026-09-01 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| d574b367-5908-3a92-b651-2a6d68f2bfd3 | -14.2599 | -52.8782 | 2026-09-01 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c4217c5f-fa23-3823-b878-cd1ae76027d9 | -13.0897 | -45.163 | 2026-09-01 15:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 665.6 |
| 288cf812-e2b3-3710-a4ea-1761e38b922c | -7.5526 | -60.4651 | 2026-09-01 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d7fb61c9-be5f-3179-94fd-1b173c716ad1 | -3.2623 | -58.2367 | 2026-09-01 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| bb6fc495-5567-3362-9560-9ed063d74456 | -10.7591 | -54.0794 | 2026-09-01 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7e7e05e3-82d0-34c0-9594-b9f6aae7f5c2 | -6.3875 | -54.7646 | 2026-09-01 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 27a12f75-c6be-3179-baf7-e48f3fca3a55 | -13.471 | -57.0373 | 2026-09-01 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 8c82c0f5-7da2-3338-b2d3-1cfdf41689ef | -7.4803 | -63.7267 | 2026-09-01 15:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| abad031c-b42a-38ec-8d40-0d4a7eadc0ec | -3.1083 | -61.2191 | 2026-09-01 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 7a6e304b-60e8-3c3c-b11f-12e207bbd58b | -11.2764 | -50.6243 | 2026-09-01 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| e00cecbf-efd1-3daa-ac9d-511bee02090f | -6.6233 | -58.383 | 2026-09-01 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 426fbaa3-e5e7-3e3b-bb7d-c9fb08079c19 | -1.4394 | -54.2169 | 2026-09-01 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| ce9f8b4a-8e8b-372c-99b8-e3f93e6911e9 | -3.1998 | -61.161 | 2026-09-01 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a5a67368-f643-3a02-8d11-3c17fbfefec0 | -8.7772 | -49.955 | 2026-09-01 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6265d685-236f-35fa-9646-2baaec6add4f | -14.5452 | -51.9729 | 2026-09-01 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1f637996-a87a-328b-9671-854379b4c128 | -1.4394 | -54.2369 | 2026-09-01 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 69c394c3-5433-3aae-8235-10ae8cb5d681 | -14.2599 | -52.8782 | 2026-09-01 15:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| fb96d522-61cc-31ef-89d1-abff7a0b8000 | -7.7522 | -61.0878 | 2026-09-01 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4bd9b218-838b-35f3-9fa8-59962ad7eb6e | -8.7628 | -46.4642 | 2026-09-01 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| cb690c91-8f65-352a-aeb0-8a9aae20fd8c | -7.5289 | -61.3825 | 2026-09-01 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| a69beeb4-aa76-3dc1-af35-78029cec3da2 | -7.4549 | -61.4044 | 2026-09-01 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 89486ad4-f24c-32d4-8a20-e84bea631e7b | -12.3814 | -48.1655 | 2026-09-01 15:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| ab980027-0930-30b5-8b3c-e44f070cae3f | -5.9451 | -57.6906 | 2026-09-01 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 5594937b-1cb1-392f-8b70-cbc65e7acbfa | -10.3574 | -50.0171 | 2026-09-01 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 11f1678d-1a50-32d0-9f81-c2324ab411fb | -8.4988 | -55.3252 | 2026-09-01 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b3962ff2-f881-3b0a-b0dd-29f6eb4ed943 | -7.0243 | -59.2181 | 2026-09-01 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 3232b733-ab26-3dc6-b4ab-80936d1bb783 | -6.3877 | -54.7445 | 2026-09-01 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 575a329d-d62d-396a-9f11-321b81fafbcd | -10.7407 | -54.0401 | 2026-09-01 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 216.8 |
| de73bf0b-d3be-35c7-8903-f42ec6b79a2c | -3.1267 | -61.1811 | 2026-09-01 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 70e4db0f-d00c-3ee2-aada-c014ad157c21 | -11.7216 | -47.6327 | 2026-09-01 15:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| f140160d-3713-33e1-80e7-60677d285b3e | -11.0747 | -51.5153 | 2026-09-01 15:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| a2c8e37f-fa0b-3f84-ae51-9efaa9ff15c8 | -6.7514 | -55.6654 | 2026-09-01 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1eda0f02-eef6-3582-9675-946e347ea255 | -13.3754 | -51.7406 | 2026-09-01 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 29fbf42a-cf63-3606-bad3-5719f8416f3a | -9.7177 | -54.8162 | 2026-09-01 15:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 4a5959b6-1779-3389-9c31-8ada49055313 | -11.0437 | -49.6635 | 2026-09-01 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 19c768d6-6387-3630-b4cc-3c993d5020c0 | -11.0557 | -51.5173 | 2026-09-01 15:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 79c6d083-19df-35ed-8797-7d17eb88b628 | -11.2767 | -50.6029 | 2026-09-01 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 23b004cf-37a4-3bca-9a51-fc6f7942760a | -5.9636 | -57.6704 | 2026-09-01 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2d7623cf-f42e-3538-a6d0-3d5f5a1c7f97 | -12.1457 | -44.196 | 2026-09-01 15:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 244.5 |
| efd340e0-7cec-3715-91a0-2a8b9a064c2e | -10.7409 | -54.0196 | 2026-09-01 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| b208b732-fa55-31c1-a276-41fd17e5f403 | -7.4735 | -61.3846 | 2026-09-01 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e2ce2353-d8ef-3d69-9222-abc28d241eb4 | -10.7271 | -50.6405 | 2026-09-01 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| eb05b6c1-fac8-3de0-8fc3-812905280820 | -6.7692 | -58.6679 | 2026-09-01 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2255723d-3cd7-3cb9-bce7-f749a40135a2 | -7.4364 | -61.4241 | 2026-09-01 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| f3708639-a029-3e05-8af3-b633b72b0e8e | -13.4707 | -57.0574 | 2026-09-01 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| fd24d9d3-536d-3575-89ef-df9aa84c9ec8 | -8.7817 | -46.4623 | 2026-09-01 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 472dfa4d-20cb-3ada-b5c1-aa0a670ec058 | -14.4007 | -52.5226 | 2026-09-01 15:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 9a225ad2-409c-39ce-9ffa-181c3a28a60d | -14.4394 | -52.5176 | 2026-09-01 15:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ac4af289-f20d-3efd-b178-2d6390df625b | -11.2954 | -50.6222 | 2026-09-01 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| d0fb4c8a-e48b-33ec-aa3b-06ebe94d5666 | -10.2212 | -50.3303 | 2026-09-01 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a964fbc2-27a9-343d-9b9b-030f26a311a8 | -6.369 | -54.7655 | 2026-09-01 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 576dd895-0cc9-337c-9dc3-c34db3835331 | -6.1183 | -53.5472 | 2026-09-01 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 31310dd4-05e3-398a-bfe6-8f56a936ce33 | -17.1146 | -46.8556 | 2026-09-01 15:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 33442430-284a-3a28-966e-410c0817d3bd | -14.6732 | -53.5408 | 2026-09-01 15:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 92f7e729-8df2-3f73-8eaf-5cb9194c71d6 | -11.0434 | -49.6851 | 2026-09-01 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| cdf72127-3c6f-399a-873d-68b7a881bbe7 | -13.967 | -54.395 | 2026-09-01 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 253.0 |
| a43b3f6e-f932-346e-bb8d-b66c5825fe1b | -11.2064 | -45.3321 | 2026-09-01 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e78a3662-5da6-35e3-8385-48fcb28112a6 | -7.2536 | -61.1074 | 2026-09-01 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a6bb91be-dffd-36cb-b45c-ebe305efc2a1 | -10.1348 | -45.7006 | 2026-09-01 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 5e8a06a5-7a57-3ded-8a95-50e3c53b26ea | -14.6535 | -53.5642 | 2026-09-01 15:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| c3bcb958-7c98-3928-8e10-623df320e43b | -7.3488 | -60.5691 | 2026-09-01 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| c57f635f-4756-3980-92d0-fc4bf7812d04 | -3.1266 | -61.2188 | 2026-09-01 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 189.7 |
| 2bfdd6c6-5aa1-3d10-adc4-7903c93b665c | -14.2792 | -52.8758 | 2026-09-01 15:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| a049c551-a77a-3e11-ace5-dd56bc69fc63 | -4.9788 | -55.8417 | 2026-09-01 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c9cb85d9-501c-351c-b652-e5fcacb6a497 | -10.1538 | -45.6982 | 2026-09-01 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 264.8 |
| 6e106d90-b0cb-3848-a541-783ae0703cd4 | -8.9242 | -63.2804 | 2026-09-01 15:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |


[Clique aqui para ver as próximas entradas](README109.md)
