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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa35bbba-0b3a-3b16-a0e9-e58baa54db75 | -22.82166 | -47.72626 | 2025-09-04 04:32:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 761f4a67-966c-337c-b9d8-50026ab56aef | -23.78965 | -48.59401 | 2025-09-04 04:32:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 58148d4e-b498-3d44-bef0-576c48dfd286 | -22.46414 | -47.54856 | 2025-09-04 04:32:00 | NOAA-21 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2f6f3b35-083f-3269-8c93-4164356e7d26 | -23.3642 | -47.16983 | 2025-09-04 04:32:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 45796c8f-badf-3663-a757-406adc7396c4 | -23.2981 | -46.16129 | 2025-09-04 04:32:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f9237958-0dbb-36fa-9a8a-42d799095d51 | -22.45958 | -47.5495 | 2025-09-04 04:32:00 | NOAA-21 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 503077b9-9ee2-3914-a65e-3e4aabd04b30 | -22.55056 | -43.56056 | 2025-09-04 04:32:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d8764413-ad89-34fd-8c1d-55e0f38c3da9 | -23.01395 | -47.08804 | 2025-09-04 04:32:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5b233a7b-32ae-3ac4-b4fa-9114ce64a728 | -23.36779 | -47.17043 | 2025-09-04 04:32:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 307e5d06-5c55-3316-8fd8-3b39f5b82eac | -22.26244 | -49.55534 | 2025-09-04 04:32:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 51e938c0-a162-37c2-b73d-2d62dee5fb64 | -23.31354 | -48.81311 | 2025-09-04 04:32:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c401ff2-4dc3-3858-a8b6-0c11b7ee6fdb | -22.2236 | -55.97512 | 2025-09-04 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cb8554d-02fb-3ac2-ab78-4d3380e036a9 | -23.40106 | -46.84294 | 2025-09-04 04:32:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c8225b1c-cbe1-3f9f-b1d9-ee8d773c3997 | -22.8703 | -47.16199 | 2025-09-04 04:32:00 | NOAA-21 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e96731dd-8285-3cf6-9b4d-113bd861d6ca | -22.6655 | -43.68973 | 2025-09-04 04:32:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 36076835-8ea0-3c77-b547-5dace78d134f | -23.76954 | -47.44992 | 2025-09-04 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 7b24d05d-4fa1-3ae5-a453-ceffa095e162 | -23.2487 | -45.97423 | 2025-09-04 04:32:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a9618fd0-23f4-3950-ba6f-48f8ae03333d | -22.26519 | -49.55965 | 2025-09-04 04:32:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d966e220-bb8c-32b3-a494-7f328bad7244 | -22.82108 | -47.73044 | 2025-09-04 04:32:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8a65467-9bdb-3fa9-b9d3-c3fd9ef3d749 | -23.8852 | -50.77669 | 2025-09-04 04:32:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b2c3fe6f-7e9f-3e38-9729-df10925705cb | -23.40168 | -46.8383 | 2025-09-04 04:32:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 05c663e1-207f-38af-8d17-672d269da416 | -22.58362 | -50.78683 | 2025-09-04 04:32:00 | NOAA-21 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf498b2f-60b6-349a-8665-b7d92789b12e | -23.00435 | -48.26491 | 2025-09-04 04:32:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6bf62935-07df-3157-a642-3fe32b0e5642 | -22.22438 | -55.97104 | 2025-09-04 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1890b77-e290-3aa8-943c-9a3bda8cbc34 | -22.81817 | -47.72567 | 2025-09-04 04:32:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e712eae0-8f84-30df-9516-2f5fe35c280f | -22.6482 | -43.68647 | 2025-09-04 04:32:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f85c6aa8-1c2e-3e85-95da-73d50d681589 | -23.01036 | -47.08744 | 2025-09-04 04:32:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| eabc30ee-bb80-32c6-a3f2-f1e610f86aa6 | -23.42884 | -47.05516 | 2025-09-04 04:32:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a0ee9a01-60f4-39f5-9d94-a916e627ac8b | -6.7833 | -63.1286 | 2025-09-04 04:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 55770901-9346-3678-a37c-47d84da259e4 | -6.7503 | -58.7462 | 2025-09-04 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8cb63bd5-656a-3b60-a3ee-09b41577ae64 | -5.0135 | -56.2553 | 2025-09-04 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e11d288b-88e2-338f-957e-12baabfe6521 | -6.7649 | -63.1292 | 2025-09-04 04:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9c1cc0b9-d2e0-3452-afde-97f4916abaca | -4.9951 | -56.256 | 2025-09-04 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d139381c-15c1-3633-81b1-90613cb7b8fd | -6.7319 | -58.7276 | 2025-09-04 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 9c53a2e4-ce0f-324d-aee6-ff0a6cfec618 | -6.7504 | -58.7268 | 2025-09-04 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| b0ecc2ae-73d6-3662-b1ae-176979716db1 | -6.7833 | -63.1286 | 2025-09-04 04:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b9c1b21a-6a96-3df4-9647-eaec15fe2256 | -5.0135 | -56.2553 | 2025-09-04 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d6960db3-a131-3531-8398-db92dc24e944 | -6.7649 | -63.1292 | 2025-09-04 04:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d7590406-c592-3572-ae33-91ce4fb551d2 | -4.9951 | -56.256 | 2025-09-04 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 4765f2b7-cc49-3610-a29d-4413bdf88cde | -6.7503 | -58.7462 | 2025-09-04 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 257c8870-257a-389e-918a-dbae62436f67 | -6.7504 | -58.7268 | 2025-09-04 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 6213c7ed-b5c8-3e5b-975b-0580bff928c9 | -6.7319 | -58.7276 | 2025-09-04 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d2738373-277d-30be-ab65-70fbc101c786 | -2.93621 | -48.82277 | 2025-09-04 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 314e4a7e-6800-3116-85b7-5901aa02876e | -3.22797 | -47.12556 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b55fbd62-543e-33db-a4fb-0aac17489187 | -3.69143 | -49.57098 | 2025-09-04 04:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58e8d372-86f7-3738-bbbf-d076cb217469 | -2.43077 | -49.31068 | 2025-09-04 04:51:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e721495-5331-3cd9-bd31-b51fc836e5d6 | -2.28534 | -48.57976 | 2025-09-04 04:51:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f919c60-7fe3-3283-be8f-7e485a31fd35 | -3.7221 | -50.94006 | 2025-09-04 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4e375c-c573-3e05-8509-3882a0e2d869 | -4.298 | -48.07815 | 2025-09-04 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d142069-2844-3280-b281-110ae81b7b6b | -3.16536 | -49.47813 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab8b6eb6-aad9-321d-a0d5-a89349ad6cff | -2.96204 | -49.34941 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7466b5c8-47f3-3949-8046-02241e051b8e | -3.16187 | -49.4776 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cf9d676-7cad-38a5-a591-a1180a3c6ce2 | -4.16239 | -48.77394 | 2025-09-04 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8b7c8dd-63c1-3065-b48f-12e21c06c946 | -4.03179 | -48.90058 | 2025-09-04 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8af6a43f-b258-3051-a7b1-4f7c1fa6bda9 | -3.47317 | -50.54193 | 2025-09-04 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e251238-4e90-3209-9818-a7af876ddd80 | -4.83394 | -42.73853 | 2025-09-04 04:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ebd7888-88a6-31f5-a9fd-0b40b341732c | -4.07267 | -48.03818 | 2025-09-04 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2698f2dc-023b-30fc-b780-6dff8ccd7d50 | -4.83943 | -42.7393 | 2025-09-04 04:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3606d22f-0ac7-3fff-9da3-5b2ec602888b | -2.95732 | -49.35659 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be2ccf7a-36a0-3a9a-990c-2c228bbb48b2 | -3.40544 | -46.90578 | 2025-09-04 04:51:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4ac3c51-7f57-3936-af38-8091d6f5a2f1 | -2.20219 | -47.99198 | 2025-09-04 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2baab339-b58e-317e-ad3d-14680915fbf8 | -4.83446 | -42.73501 | 2025-09-04 04:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a8efba1-e4f6-31fc-b8ec-df723edef4ff | -3.62246 | -53.70407 | 2025-09-04 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 814431a3-5827-3666-b3ce-4ea3d346426b | -4.03134 | -48.89774 | 2025-09-04 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b169b4f2-8370-31c5-b5c3-8544be7fecc1 | -3.22898 | -47.12898 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 552188b0-db57-37cf-ae2f-6789d9cec417 | -3.87177 | -52.1627 | 2025-09-04 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88cacca1-f85c-3ab0-bd8f-852181ae546f | -3.79294 | -49.43061 | 2025-09-04 04:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2757da58-5c03-301c-b6ae-9760d81576d2 | -3.81226 | -51.53383 | 2025-09-04 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73cc34b1-af35-3e1e-a15e-d903efe5a568 | -4.78291 | -43.82118 | 2025-09-04 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c177f42-8456-3205-8b63-8b7773e9325e | -3.79814 | -52.3322 | 2025-09-04 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d439e3f3-90a3-3b9f-8d9b-a424f044be85 | -4.18105 | -48.58589 | 2025-09-04 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f369754-9820-38f7-94d5-47aa18102ec6 | -4.8389 | -42.74287 | 2025-09-04 04:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8465d634-4468-3aa7-b183-d5d88455f9ce | -4.83911 | -42.73911 | 2025-09-04 04:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0d7f42e-52c8-3434-bb4c-d56c4299cb17 | -2.96311 | -49.3654 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 92ff890c-b3d4-3c68-8b4c-b707096e105d | -2.96082 | -49.35712 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 134a200d-6819-3a38-8d2d-cc9973476e2b | -2.58663 | -51.92163 | 2025-09-04 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab27d280-f4ce-30ec-94d7-3526e717c8bf | -4.84407 | -42.74362 | 2025-09-04 04:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fc5ac2d-932a-3f8b-baea-6a355a6076a6 | -3.16046 | -48.60492 | 2025-09-04 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 368d4e5b-cc90-3912-ac7f-36abba71f802 | -2.96143 | -49.35327 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 388b2192-abfd-3093-ab6b-a3b1ae55f745 | -4.03069 | -48.90191 | 2025-09-04 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddd9bd1d-29d4-31f2-b8bc-f1822ebf568f | -2.96022 | -49.36098 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 96ab895e-290d-3cfe-92f6-c26ed9e29171 | -2.58608 | -51.92508 | 2025-09-04 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1704e53-24e2-38c6-9f51-5f6697b490ab | -3.22106 | -47.12774 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 104c780a-5780-3ca8-81fb-9ffe79876428 | -3.22401 | -47.12493 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19725032-84f6-3beb-b7f3-69e16f248ab4 | -4.78481 | -43.82114 | 2025-09-04 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3145b739-454d-314a-83ef-86a951e331b7 | -3.1641 | -48.60548 | 2025-09-04 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 428a4dba-4573-36b7-a2f5-fcb8b301c155 | -4.17968 | -48.58424 | 2025-09-04 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b09698bb-d50d-31f9-be4b-2eba45e57377 | -3.32713 | -54.90771 | 2025-09-04 04:51:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1472ba01-c2ad-351c-9c3c-7224a7e0d3d7 | -3.38251 | -47.61116 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abcfa236-9a0c-34c6-8cb1-c48df67f2567 | -3.16597 | -49.47426 | 2025-09-04 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 661d2927-438e-3737-a06b-3915c999c2c4 | -4.83861 | -42.74268 | 2025-09-04 04:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d29ce9c-2458-3a4b-be4f-b1b3149c4b61 | -3.32647 | -54.91181 | 2025-09-04 04:51:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d6d54f0-2b62-3ab8-ae0a-b557d9923da8 | -5.02878 | -42.47461 | 2025-09-04 04:51:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27ca0f7d-b326-3c47-a4bf-17b81b73a955 | -3.47655 | -50.54244 | 2025-09-04 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ac46dcf-98b6-3bf3-9baf-583ef4a5e3bf | -3.22325 | -47.13001 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbfae190-1c7c-3e24-961b-5a8c67f3220b | -4.83362 | -42.73833 | 2025-09-04 04:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57337ac1-f849-357e-abd4-de04101026aa | -3.22721 | -47.13063 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 844dd455-ca29-33e4-af87-42488e6ce05d | -3.22582 | -47.12328 | 2025-09-04 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3840b96-5af6-35d6-9143-8037ae381e26 | -3.40141 | -46.90516 | 2025-09-04 04:51:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c852d45-84aa-3711-89d9-e3ab025bf24f | -4.06888 | -48.03757 | 2025-09-04 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README54.md)
