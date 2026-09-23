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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93deba69-0c61-36ff-862a-9da020d9c44c | -6.0925 | -57.6847 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 434922c4-58c1-3e38-8004-f6d05a5fb3ff | -6.6148 | -59.908 | 2026-09-23 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f26ba1b9-108d-3df9-b952-682682e65c62 | -9.0839 | -61.4308 | 2026-09-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 701ccefd-41d2-3cd8-af72-c26806f45f32 | -6.1289 | -57.7613 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 5ce195af-98fc-3f5d-8b4c-be6800b44ee5 | -5.3453 | -45.1576 | 2026-09-23 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 6643eecd-302a-3663-a1df-0935c0d8c822 | -8.2064 | -54.7005 | 2026-09-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e37f1787-9437-3d69-849b-54a67b37cf1e | -6.663 | -55.0712 | 2026-09-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| a13885fc-944d-3d0e-abb5-9a9381160582 | -8.791 | -60.8127 | 2026-09-23 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 28ec4381-18ae-31b3-af98-9d507321ff85 | -8.4985 | -57.6075 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 290.9 |
| c97f026d-5fb0-3f7d-bd44-3f7878dcb2d4 | -6.6815 | -55.0703 | 2026-09-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c64bf483-2a19-333f-a95f-3a36be10698a | -8.8275 | -50.482 | 2026-09-23 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f3a1d799-ac30-3118-848e-425d782c3e39 | -8.1876 | -54.7219 | 2026-09-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| df32ef16-3353-3245-8bb3-c303265a9dfe | -8.4797 | -57.6282 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 6da6438b-33a8-3203-8829-926daf715177 | -8.4986 | -57.5878 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 39510d03-c050-33af-a45a-230f806b0559 | -14.6492 | -45.66 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6bd3c2f1-5b4b-3a0a-93af-70657b72e9e3 | -8.2062 | -54.7207 | 2026-09-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 8a3901f4-1db1-395e-a633-e54335546da2 | -8.935 | -61.495 | 2026-09-23 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.6 |
| c939b3cb-3a28-3609-b9d8-f0a35bd22262 | -8.9164 | -61.4958 | 2026-09-23 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 97.8 |
| b077700b-49eb-3e08-9152-273f9b940443 | -12.4216 | -46.9551 | 2026-09-23 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 44c174b2-30c3-39c5-8233-c98bac2bae4e | -6.789 | -48.6779 | 2026-09-23 00:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 21cf56cd-0219-36f4-8f2f-a7a1af1db702 | -14.6307 | -45.617 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 50c27196-4211-3a02-bd30-198856cbb29d | -5.3639 | -45.1564 | 2026-09-23 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a4589c7b-96d5-3c49-ad5b-554739b90de1 | -6.7213 | -44.1387 | 2026-09-23 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 111ced5a-22a7-3169-99a8-187d3a83104d | -6.6816 | -55.0502 | 2026-09-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 9f7781d1-bed1-31b1-9dc3-b502ec498d93 | -6.6127 | -43.7549 | 2026-09-23 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| c4bf2e83-2ece-3d8a-bfe5-c9d0d65b95e4 | -3.4597 | -59.5783 | 2026-09-23 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| ec260beb-8b20-3e8f-bfe9-b3e59f409a4f | -6.7211 | -44.1618 | 2026-09-23 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d7357632-16c1-3fa8-a5ba-368604620fcc | -6.728 | -59.423 | 2026-09-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| ef3aceb0-5a3b-35e5-992a-c7f929c0512b | -14.7475 | -45.6191 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 3123f5ac-2ee9-3fe2-a4f1-eb301527db48 | -11.3043 | -51.3434 | 2026-09-23 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| acc04236-904e-370c-b14a-2a78961f7eaf | -8.4799 | -57.6085 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 227.3 |
| cd15d6f9-9442-3cfa-8f61-8889263e2373 | -3.6947 | -60.5645 | 2026-09-23 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c57cc71a-7f37-345d-b435-bc617b5ab3fd | -6.6315 | -43.7533 | 2026-09-23 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 200519a5-2f10-390f-8aae-ea4f26c9ea5a | -6.3293 | -43.9411 | 2026-09-23 00:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0a4c5cc9-52f2-3a89-af1f-1a6bdb492a8c | -8.4538 | -48.6944 | 2026-09-23 00:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 104.2 |
| faba7796-408c-360d-b314-5d53cf8e870c | -14.7284 | -45.5993 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| eaf4e07d-21c1-3e6d-8dc8-2843f334ad3b | -8.4983 | -57.6271 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 171.0 |
| faf8ec23-76a5-3c1b-a489-e3b2dfe06fdd | -3.2128 | -46.9602 | 2026-09-23 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 7f253874-b823-373e-be4d-61d0d677a96b | -11.3447 | -54.0264 | 2026-09-23 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 11d27285-5945-37e5-9c2c-1c3b527ed000 | -6.6129 | -43.7317 | 2026-09-23 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a094c5b0-c38c-3fff-9bbf-b4a2f85e873f | -6.7464 | -59.4223 | 2026-09-23 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| cde76e01-2cd9-3a27-8013-772f4e50d5e0 | -8.9165 | -61.4767 | 2026-09-23 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 0c4f960f-23d5-33f1-a495-946760269ea7 | -5.6246 | -45.2518 | 2026-09-23 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| fcf82da5-1bc3-32cb-8e23-4045cc5a7815 | -12.4212 | -46.9777 | 2026-09-23 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 77cd0af0-27fc-3e07-8831-00ec9364d258 | -3.478 | -59.5779 | 2026-09-23 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 8d6bc9e4-8a52-3069-b4fa-d2e80bb74766 | -3.2129 | -46.9383 | 2026-09-23 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 6181ed13-2b91-3907-9384-37f8a5dd9c1f | -9.5725 | -40.3227 | 2026-09-23 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 276cfd7f-34b1-32f3-8f4c-666488cfecad | -6.9401 | -46.5648 | 2026-09-23 00:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| cfce8c89-ab83-39cf-8a57-6d4a83de4201 | -14.6497 | -45.6367 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 8a0d10ee-beb8-3b2c-8aad-818ef4834b4d | -14.6297 | -45.6635 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2e35b551-545a-3d2e-895a-2abb1ad64754 | -10.5091 | -44.8517 | 2026-09-23 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 178969db-b945-30d8-94f0-ce313542b6c7 | -6.6776 | -58.5554 | 2026-09-23 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| d3d49520-7142-3ba2-ad72-fb55c730e229 | -8.5982 | -54.6341 | 2026-09-23 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| d57d3c1b-8ec9-3541-bfe4-0680216f214f | -6.0926 | -57.6652 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 19d1fc48-b2d2-3d08-a2f9-4f46d0007877 | -6.3105 | -43.9426 | 2026-09-23 00:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e8b5c715-9c8e-3731-bd3c-53a98a4a80dc | -12.79 | -50.96 | 2026-09-23 00:15:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43b6db62-eba8-327e-9d83-b0b3a320711a | -11.77 | -50.95 | 2026-09-23 00:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7a542bd-8269-3eed-83c4-805e71cfd206 | -12.79 | -50.85 | 2026-09-23 00:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4577210-9fc5-3372-80bf-80e04a5290df | -12.82 | -50.92 | 2026-09-23 00:15:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 80175bd9-8ebb-37b7-bc8c-2bee8cefecee | -12.82 | -50.86 | 2026-09-23 00:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 308b2f4a-5471-31f6-8f07-0085b885cbd8 | -6.92 | -46.59 | 2026-09-23 00:15:00 | MSG-03 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42e18300-8deb-3171-8cfd-b012bff31832 | -11.71 | -50.93 | 2026-09-23 00:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1f4a901-60e5-33ca-ba21-57bbaa0af72c | -12.76 | -50.9 | 2026-09-23 00:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc660ac1-a7e3-3c29-b81d-636c0aa5a337 | -12.79 | -50.91 | 2026-09-23 00:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84d293f6-5d8b-33a0-ab29-9a20eefbe603 | -11.74 | -50.94 | 2026-09-23 00:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 028c9776-6e5c-3866-a405-0515cb05a0d0 | -11.3043 | -51.3434 | 2026-09-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 051c03da-c322-3f53-be27-0eeb9e69b589 | -3.2129 | -46.9383 | 2026-09-23 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b2361a84-babd-3a6a-aff8-610836ada8aa | -3.4781 | -59.5588 | 2026-09-23 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f5acdab4-0a6c-3ba5-bf25-9a823d972f34 | -11.3229 | -51.3626 | 2026-09-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| cad79178-56be-3f41-a73a-70c732c5ece8 | -6.6815 | -55.0703 | 2026-09-23 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ceee6364-f851-3519-833e-987174263fcd | -6.3293 | -43.9411 | 2026-09-23 00:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b4b3ccab-742b-356f-a441-a27320779187 | -8.9351 | -61.4759 | 2026-09-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 56431d69-3e03-35ef-90e5-e68e101c66e1 | -7.0352 | -44.6396 | 2026-09-23 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 29134939-2d41-3270-8735-04fc1dc67d57 | -3.2313 | -46.9596 | 2026-09-23 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| a30e9c1b-3e58-321c-8919-9c1d9495ad1d | -6.1111 | -57.6645 | 2026-09-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 21e6d5a1-e2cd-3f59-ae18-9e24bb869154 | -15.6376 | -43.5312 | 2026-09-23 00:20:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 7dc40aa5-1050-32de-afba-e435245560eb | -6.789 | -48.6779 | 2026-09-23 00:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0aa7741a-f415-350f-a4ad-d353119585cc | -7.0349 | -44.6625 | 2026-09-23 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| d14bd703-ad57-3767-9f09-70678a189ce4 | -3.4598 | -59.5591 | 2026-09-23 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c29ea52e-af8d-31e0-9532-60cab63d435e | -8.8463 | -50.4804 | 2026-09-23 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2687b9d9-c417-356f-ba60-eae28651e3f7 | -8.9108 | -62.391 | 2026-09-23 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8b542885-5583-3d61-b9be-890843383bb7 | -14.6302 | -45.6403 | 2026-09-23 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 0de9a6f2-4456-395f-aa9c-81e54a38b953 | -3.2314 | -46.9376 | 2026-09-23 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 2f7dfe1a-b00b-30e2-9b23-cede37b8cb64 | -6.1109 | -57.684 | 2026-09-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3e1eedea-9ba0-384e-861d-9584446577e0 | -5.7754 | -45.1053 | 2026-09-23 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 6160a3ee-7de2-35b5-a9f3-2b92eac64e7b | -14.6497 | -45.6367 | 2026-09-23 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ebfbe2c1-7422-371e-a0c7-a3a43dff8b5b | -6.9403 | -46.5426 | 2026-09-23 00:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| f0e0b6f2-8d9e-3501-9edc-2235a10ed728 | -11.7085 | -50.9385 | 2026-09-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 168763e4-3546-38c5-a227-1d79ac4913e9 | -3.6946 | -60.5835 | 2026-09-23 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4070fc03-67a9-3369-a1c1-69f64c5e15f5 | -10.6283 | -53.9885 | 2026-09-23 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 34d9fb53-5e62-3591-8fd7-0f8e5c27d79c | -3.478 | -59.5779 | 2026-09-23 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9311341f-f0dd-3eca-a34c-7214554e89e8 | -11.7281 | -50.8937 | 2026-09-23 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0cae1d89-fe3e-34c6-81ed-2f2754164733 | -6.9216 | -46.5441 | 2026-09-23 00:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5773df1f-c53b-3738-bf25-ae96772aa96f | -3.6764 | -60.5649 | 2026-09-23 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a98622b4-b0c6-3421-a484-c5f5e381c30b | -6.6127 | -43.7549 | 2026-09-23 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 5b7acd34-48b2-3e87-a99d-7e862d5b2b88 | -11.3447 | -54.0264 | 2026-09-23 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f943ee17-4f66-3273-8b97-a748b05eae6a | -8.5984 | -54.6139 | 2026-09-23 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 26fad618-8782-3f49-8672-27c8c60cb21d | -9.1025 | -61.4299 | 2026-09-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c4251cbf-b322-3476-8f9d-ab893de43d21 | -9.1024 | -61.4491 | 2026-09-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 90cc56c8-2ec4-351c-a132-4a605b0b50d5 | -6.0925 | -57.6847 | 2026-09-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |


[Clique aqui para ver as próximas entradas](README9.md)
