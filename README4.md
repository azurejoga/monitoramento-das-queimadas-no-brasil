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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04dcaba9-7b31-3e84-bf1b-6ce444088338 | -11.5261 | -40.7724 | 2024-10-27 00:12:02 | METOP-B | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 00281531-81d7-3f78-847d-93b21c4f0aa1 | -10.158 | -36.1576 | 2024-10-27 00:12:06 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42223a37-7c37-3cd1-a8f8-a94d01e5b795 | -10.161 | -36.170101 | 2024-10-27 00:12:06 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 20fad2be-a80a-3e63-846e-4776deee72d4 | -10.1483 | -36.16 | 2024-10-27 00:12:06 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a945cee-300f-38ef-9032-dc8bf47bdf96 | -10.1513 | -36.172501 | 2024-10-27 00:12:06 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa5dafa6-df80-3250-9763-eea914818abc | -10.1746 | -36.3102 | 2024-10-27 00:12:06 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98ddfe30-26bb-3221-88f4-5b149bbc05ba | -10.1775 | -36.3223 | 2024-10-27 00:12:06 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d25eb61-c6c6-3a11-a10a-a4f08be5e833 | -10.1649 | -36.312698 | 2024-10-27 00:12:07 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eac3a6ef-a84e-3582-870e-9b4371427cce | -10.1678 | -36.324799 | 2024-10-27 00:12:07 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bc696ad-8aec-3840-aa90-f10e2c86aa0d | -10.1708 | -36.336899 | 2024-10-27 00:12:07 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d22655bb-42cb-39bc-bd39-c1504b31bb56 | -10.1066 | -36.454899 | 2024-10-27 00:12:08 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 4c7cec7e-d975-3528-a16d-c133cf7b376a | -10.1095 | -36.4669 | 2024-10-27 00:12:08 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| fe4a7fb7-5a57-321d-a7c2-e161ec5f0741 | -11.8568 | -45.284401 | 2024-10-27 00:12:12 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fcca4ede-835e-3ef1-847d-fd016686354a | -9.6451 | -36.0434 | 2024-10-27 00:12:14 | METOP-B | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8cf36f9-10e7-3c20-aed2-49751255bc87 | -9.6482 | -36.056301 | 2024-10-27 00:12:14 | METOP-B | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da3b2bed-ee27-3c89-a76c-6485fba0ccf2 | -9.6354 | -36.045799 | 2024-10-27 00:12:14 | METOP-B | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f71e3d8b-238f-3c40-877b-541f76b7559b | -9.6385 | -36.058701 | 2024-10-27 00:12:14 | METOP-B | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10c0e0f7-393e-3735-b930-c2bb3cb5030a | -11.2718 | -45.0863 | 2024-10-27 00:12:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 239ccf01-9084-3634-b229-c6675eb9a489 | -11.2735 | -45.094501 | 2024-10-27 00:12:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0192241-55fd-3d29-a05a-d01e2cf4af51 | -10.9494 | -43.9221 | 2024-10-27 00:12:22 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d41bbaec-2212-3668-bdec-6fe7a2137c9e | -11.0866 | -45.0835 | 2024-10-27 00:12:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d269a60a-2aa5-39a4-a99b-5d3f814a7613 | -11.0884 | -45.091702 | 2024-10-27 00:12:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4bba49e9-669c-31a1-bdc8-108b2d737f36 | -10.8728 | -45.138302 | 2024-10-27 00:12:28 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e683d79-cde7-3bc5-99c0-a98d6e400301 | -10.8745 | -45.1465 | 2024-10-27 00:12:28 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a5b4c87-a3ae-38d6-b5c7-f176b4aaa2c4 | -10.7659 | -44.783501 | 2024-10-27 00:12:28 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d4cb9106-c2fd-3223-8c87-87639cc989a7 | -10.7676 | -44.791302 | 2024-10-27 00:12:28 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09dd5eb3-2c37-3b3e-bd00-2e2bcc1c1cee | -10.6024 | -44.263699 | 2024-10-27 00:12:29 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9d8e9795-bf50-381e-a356-c9401b32f0df | -10.604 | -44.271198 | 2024-10-27 00:12:29 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a297a6ec-0263-3516-9110-fc2001b79d01 | -10.591 | -44.2584 | 2024-10-27 00:12:29 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ac0d50d-9494-3fe2-aa51-e21c5521d26f | -10.5926 | -44.2659 | 2024-10-27 00:12:29 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a56b3fc2-8398-35b8-9a1c-ebd35ca6408c | -10.5942 | -44.273399 | 2024-10-27 00:12:29 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 210d5f8c-1b3f-3a6a-8767-2dc4a3a54da7 | -10.5714 | -44.262699 | 2024-10-27 00:12:30 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f6275009-4003-3317-97bf-f7eda891ef9a | -10.573 | -44.270199 | 2024-10-27 00:12:30 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 65e5a9b6-ce30-3c1d-b76f-4284d4ade2a6 | -10.1601 | -42.441002 | 2024-10-27 00:12:30 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1073b6b1-e3b2-35f4-b403-7c3eac187c0a | -10.5599 | -44.257301 | 2024-10-27 00:12:30 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 94c0d32f-35d1-38ef-91d3-d9f92ffdd1a4 | -10.5616 | -44.264801 | 2024-10-27 00:12:30 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b6f622c1-12db-394f-b150-fb35e4cc7b0a | -10.5632 | -44.272301 | 2024-10-27 00:12:30 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5adbe3c6-80c7-324f-8417-ec324844b6dc | -10.6755 | -44.935902 | 2024-10-27 00:12:30 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13743fab-9f4e-37a7-8209-21be0a2b8fed | -10.6772 | -44.943901 | 2024-10-27 00:12:30 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c86eb141-9797-3db1-a330-191a4e77ebbf | -10.6685 | -45.0466 | 2024-10-27 00:12:31 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b0012a4-37a7-3b7f-ad65-34ae7d9f5b56 | -10.6668 | -45.038502 | 2024-10-27 00:12:31 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 122646dc-c013-3acf-9f19-ffdc9fd3e33b | -10.4393 | -44.553699 | 2024-10-27 00:12:33 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b46a7bb0-795b-384a-9385-f5f31d13ba6e | -10.441 | -44.561401 | 2024-10-27 00:12:33 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bccaafe0-e99a-39d4-8e04-7bd3461de874 | -10.4426 | -44.569099 | 2024-10-27 00:12:33 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76cad52e-7cfa-36c3-850d-ee70b5976d1a | -10.5319 | -45.126999 | 2024-10-27 00:12:33 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc74545c-03dc-39a2-8d9b-e4c273b89d03 | -10.5336 | -45.135101 | 2024-10-27 00:12:33 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06ca3ad2-6dfd-34e3-96dd-b59ca83d22fc | -10.5354 | -45.1432 | 2024-10-27 00:12:33 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a32b4c35-e2cf-3cde-8173-4f8b6a3b312d | -9.4659 | -40.379501 | 2024-10-27 00:12:33 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e57f9ca1-7676-3f54-8b8b-803ee79a1fb1 | -9.4676 | -40.387001 | 2024-10-27 00:12:33 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cc6e32ee-29f3-3f66-a9da-902ad6416b28 | -10.2874 | -44.137699 | 2024-10-27 00:12:34 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 311c7e8e-4e0a-373e-957b-8145ee4d69af | -10.4475 | -44.877499 | 2024-10-27 00:12:34 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f18e2b9e-1ce3-3c19-ac71-630cf7ffdb98 | -10.4377 | -44.8797 | 2024-10-27 00:12:34 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc587084-2c01-3695-adaa-85290196c46d | -10.4394 | -44.8876 | 2024-10-27 00:12:34 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79f4b0f5-7e56-3bb5-80bd-d620fb6e7cdc | -10.4496 | -44.935101 | 2024-10-27 00:12:34 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 83bffb87-6050-3d95-b424-991fafa59824 | -10.4881 | -45.1619 | 2024-10-27 00:12:34 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ec21693b-63e8-3120-99da-90e77dbb46d0 | -10.3757 | -45.0681 | 2024-10-27 00:12:36 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 923e6c3d-eb94-3b81-9062-bf95d0c0706d | -10.3774 | -45.076099 | 2024-10-27 00:12:36 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0eb34b9f-9bc8-311a-a866-5be9cb1deefe | -10.3676 | -45.078201 | 2024-10-27 00:12:36 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 306106af-9eed-36e0-8c4b-30180c662182 | -10.0149 | -44.0667 | 2024-10-27 00:12:38 | METOP-B | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d536f051-87a6-3edf-887c-9540d9a96cad | -10.0165 | -44.074001 | 2024-10-27 00:12:38 | METOP-B | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a6df4f5-9d01-3d59-8958-91dfe86209c2 | -9.9607 | -44.1479 | 2024-10-27 00:12:39 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b32656e-8a9d-365a-9ea2-5c5bfde704e0 | -9.9624 | -44.1553 | 2024-10-27 00:12:39 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c20afbbb-8f92-3f7e-a936-ed4fb38f38e4 | -9.9831 | -44.391899 | 2024-10-27 00:12:40 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f0a9a28-1ade-32e6-9245-3bdad05194e2 | -9.9814 | -44.384399 | 2024-10-27 00:12:40 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dee69fb7-3825-3cf6-880e-d439cad7690b | -9.6991 | -44.739601 | 2024-10-27 00:12:45 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 141ec11f-7d2c-3479-a30c-488d1226a104 | -8.7916 | -40.8568 | 2024-10-27 00:12:46 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 9904089b-0b3e-386a-bd9f-6cc7ee51b081 | -8.7933 | -40.864201 | 2024-10-27 00:12:46 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 2817aa29-9a73-3b5d-9f46-2a3715715573 | -9.5064 | -44.232498 | 2024-10-27 00:12:47 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0858042f-b178-3278-8655-18692f16df78 | -8.6666 | -41.0317 | 2024-10-27 00:12:49 | METOP-B | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5d6d4ee1-54aa-3a26-8d45-d4b17ecfce94 | -8.6245 | -41.1633 | 2024-10-27 00:12:50 | METOP-B | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 0538e20a-a1d4-3640-9788-ccada535ebf1 | -8.6261 | -41.170502 | 2024-10-27 00:12:50 | METOP-B | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f983e7bc-7cb3-3856-8b13-4fe09cd3a2d2 | -7.7086 | -37.4198 | 2024-10-27 00:12:51 | METOP-B | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 7beed856-0f97-3f64-8839-9c40bf4f0200 | -7.7113 | -37.431 | 2024-10-27 00:12:51 | METOP-B | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5bbb8b8c-e41f-3e07-88a7-d95f63f6f3ee | -7.706 | -37.4086 | 2024-10-27 00:12:51 | METOP-B | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 52007f46-8cd0-32dc-88bf-08ad90b58578 | -8.5317 | -41.752602 | 2024-10-27 00:12:54 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c31dcaf7-849e-3de5-8410-0a0c2f9d8d89 | -7.8834 | -39.162701 | 2024-10-27 00:12:54 | METOP-B | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| a28ecba5-adc1-3ca0-af37-adf7c4f4116f | -7.9417 | -39.323799 | 2024-10-27 00:12:54 | METOP-B | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| c8f67a57-c5dc-3737-aee8-835151547fa1 | -7.9437 | -39.3325 | 2024-10-27 00:12:54 | METOP-B | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| af6bd16f-4575-3e92-a650-22d2e0e2b72e | -7.8813 | -39.1539 | 2024-10-27 00:12:54 | METOP-B | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 1235567d-c5db-3b36-81b9-ec5e48aed004 | -9.13 | -44.720699 | 2024-10-27 00:12:55 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 340b4fb9-312b-3a56-9c3b-5c7728978e67 | -9.1317 | -44.728199 | 2024-10-27 00:12:55 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d88d824e-16ab-3d46-bcfb-c8ffb04e9ea6 | -6.9961 | -35.616402 | 2024-10-27 00:12:55 | METOP-B | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 12ce8ca9-85e0-378b-8992-9464b43ebd60 | -9.4133 | -46.080101 | 2024-10-27 00:12:55 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4fb86c6-f967-31d8-816a-df5e40cec207 | -9.4152 | -46.088799 | 2024-10-27 00:12:55 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d06c0139-a681-3e8f-b580-42f9e5e2fcc0 | -9.1202 | -44.722801 | 2024-10-27 00:12:55 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18cee5d5-876b-33b9-9fa2-4bf6f4b35e00 | -9.1219 | -44.7304 | 2024-10-27 00:12:55 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7224259c-920c-3a40-8224-b058e1acb11d | -7.5576 | -38.741001 | 2024-10-27 00:12:58 | METOP-B | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 39ee4149-4ab2-3cb1-9864-4102b5c22a16 | -7.5598 | -38.750301 | 2024-10-27 00:12:58 | METOP-B | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2dbf8e4c-f033-3a10-9934-56573195e3e8 | -7.5455 | -38.733898 | 2024-10-27 00:12:58 | METOP-B | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 18efdc27-6c0a-3a66-b0ab-c90500fa1d86 | -7.5478 | -38.743301 | 2024-10-27 00:12:58 | METOP-B | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9f8e058e-2d12-345e-a660-c2f5b4ee8a8c | -8.3466 | -42.2556 | 2024-10-27 00:12:58 | METOP-B | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8c21eda-74b5-39ad-8f3e-4845dc7bb29f | -8.7177 | -44.011902 | 2024-10-27 00:12:59 | METOP-B | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bfebb043-8eed-3141-9d7f-7b5fc16a3eb8 | -8.7192 | -44.019001 | 2024-10-27 00:12:59 | METOP-B | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce418df-2a0e-3cbc-a8ce-30bb3a47a892 | -8.7688 | -44.7131 | 2024-10-27 00:13:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ecc19ff9-3db6-3e26-9322-ae28d094dbd8 | -7.9511 | -41.150002 | 2024-10-27 00:13:01 | METOP-B | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66058627-6d62-3095-b3ee-d345d75c8e87 | -7.2591 | -38.919201 | 2024-10-27 00:13:04 | METOP-B | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c434db8d-805f-3ee6-9b79-4a5d8a88e169 | -7.9895 | -43.327599 | 2024-10-27 00:13:08 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f9ce967-54ce-37bd-8a49-d68aebb30ee8 | -7.9911 | -43.334499 | 2024-10-27 00:13:08 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ecf86ca4-1ac9-3219-914f-0f622bebdac9 | -6.9722 | -39.235699 | 2024-10-27 00:13:09 | METOP-B | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1b1f65f9-eb9f-33bb-a737-21f082ae2577 | -6.9624 | -39.237999 | 2024-10-27 00:13:10 | METOP-B | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README5.md)
