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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbb6bbbd-9b9e-3dfb-b618-20fd7d40d335 | -6.58993 | -39.13679 | 2026-09-22 04:46:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24eb1535-8896-3086-bc27-061c19a73c8b | -8.61444 | -54.62621 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1efca0ea-e4ec-3148-93de-7ddc06b9f5ee | -3.41789 | -60.19759 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da8d2dfb-4ea0-3eb5-8358-fc92af1cbd73 | -6.7292 | -55.06737 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc5c934c-e3e8-3f73-8be6-df8395a9fd8e | -6.12129 | -59.95131 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46329490-5a70-36df-b9c4-5e454f9055c2 | -6.44816 | -59.96635 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fefd4972-93c1-3eee-9441-ed491d7e3517 | -6.10046 | -57.62529 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 521ec83f-1885-38e0-aa95-381805c374f8 | -3.44902 | -51.54881 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccec69e5-e171-3efd-a9e6-6b5f7c36b673 | -6.82896 | -49.09716 | 2026-09-22 04:46:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21944811-4716-352d-b092-1b40f347877b | -5.8702 | -52.03395 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1feb57cb-cf86-3de5-accd-b95a5b16b8ce | -6.46454 | -59.99491 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9a3954e1-cefa-3432-9e7f-9659284bd18c | -3.43615 | -58.02634 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d655f79a-f44c-3620-98ac-fc89a05c37ea | -8.78726 | -44.28374 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1874fc0d-5610-33b4-b08c-2b09215d2651 | -8.42426 | -46.89034 | 2026-09-22 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c3eb9fd-cb08-38f9-bcd9-067bd627bb18 | -7.52076 | -45.44285 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa289c9b-6940-37ee-a14d-c03b502d4e3f | -6.57167 | -44.16166 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9322d1b-1b6f-3e3a-9113-9eddd9dc7589 | -7.58127 | -57.66624 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d84f17cd-25d3-3778-a05c-eee984585288 | -7.33073 | -55.59665 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 260fe84c-5bb1-3367-8430-62a8f1d4b5c9 | -6.60695 | -45.52045 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 754de93c-662a-31bd-8df8-92609404167d | -3.05879 | -54.41711 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a036783-3338-33f6-9b61-dffab0c21205 | -5.3229 | -43.4192 | 2026-09-22 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e2d84b11-0096-31f1-9dbe-c853c9c6c58f | -6.40224 | -55.26235 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f19be5b-f793-3f52-a869-d02b289bd4f9 | -4.68167 | -55.62814 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 711f93c4-bef2-3e83-ac22-74c66e63554d | -9.61062 | -43.9214 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f3948024-0051-3813-a7a4-abc4bf8a029c | -8.79334 | -48.73333 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1c540b7-0fb7-3872-99f6-a42b9942f8c3 | -3.8238 | -59.3331 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37a966a8-46e1-3dba-ad8a-76c235897377 | -6.5818 | -44.15088 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 30bd9e42-1ba4-33cb-9d51-7df7f518b191 | -6.90002 | -41.69592 | 2026-09-22 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 379fd9fc-4227-31a5-8694-1d75eb9ee994 | -6.72993 | -55.06283 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e553615a-de72-3331-b077-0a957a89c421 | -6.20131 | -57.78144 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21bcfab3-c8f2-3b78-8a98-f1f2be730c67 | -6.85053 | -43.72209 | 2026-09-22 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 246aadfa-cad2-3b20-b029-5f44aeb528d8 | -6.65095 | -59.92035 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 92a63234-9880-3d13-bf45-d4712016a80c | -3.01152 | -54.18364 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2f8bf4a-451d-3572-8d3a-bc4356f7fb61 | -5.82912 | -43.84893 | 2026-09-22 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ea25748-cba7-3f96-ba89-ab47f1d6c793 | -3.51256 | -59.58257 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| abaa7e45-d37f-3692-b5eb-3bf881142038 | -10.47136 | -51.29791 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39e9f141-bff2-382a-acf4-7f19feb66efb | -3.05372 | -54.40512 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa5c7fba-b763-385b-a861-d1d062df55d1 | -5.20297 | -56.07418 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 322a6001-cdd6-3e0d-bb3f-0b2a1c543ad1 | -6.58644 | -44.15151 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7760a65d-fdb2-31aa-90ff-fcc2c89fc832 | -7.42772 | -49.84435 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58145c50-5a55-3064-b873-f567c2615682 | -9.28982 | -46.1891 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c2d26d8-7a2d-3aec-bff5-27719660409f | -4.18685 | -49.40958 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49794fad-8e8f-3f49-85a1-f67110e112e6 | -9.61954 | -43.95101 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 3b85c69a-4129-3225-9bcc-1175a23926f3 | -5.98314 | -57.77744 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfadcf59-24ce-3fd9-b921-9946a8a9fcd2 | -7.50789 | -45.44079 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcf2938d-318c-3e5a-9512-e8aa3e5da500 | -9.95575 | -53.98838 | 2026-09-22 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5297a810-b553-3a6c-bd35-a5e3356b40eb | -7.14253 | -48.44422 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57b3e027-41c6-3ab8-a253-c7795f631ac3 | -7.13135 | -48.42743 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50550a5e-4f75-30ba-a812-1bf31e361c93 | -2.85791 | -57.80761 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81126975-5e6e-3a19-8d94-392c99570118 | -4.63455 | -55.76748 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e6984fb-9e5d-3d1e-a76a-8dcc4b918506 | -5.05132 | -46.06961 | 2026-09-22 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aded9ac8-f27d-3650-a25d-8ec5d6bf1bb5 | -6.78262 | -48.67209 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd7666c6-1bf0-3f4f-b151-4600b395f381 | -6.14643 | -43.85615 | 2026-09-22 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 920f6edb-86fa-3230-8442-de32bf0a3abc | -9.94609 | -53.98298 | 2026-09-22 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd1f0914-e7de-33c6-963e-e8b785d1a7c3 | -8.17289 | -54.81986 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a76599b9-a13a-33fd-8948-027ad3a076a8 | -10.47523 | -51.29483 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f99a6be-c15d-39b7-89d9-d6c6877abb9f | -4.66224 | -42.09193 | 2026-09-22 04:46:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 016e751d-fd15-3379-acdc-9f0e42dcb2cc | -5.75285 | -45.08903 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 9593f2ad-298c-393d-a5c9-a9d22b296eaf | -5.89464 | -52.29084 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68d1ceaa-9342-386a-a8e5-36784e62b35b | -3.37536 | -52.79352 | 2026-09-22 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fd12480-89c9-3bfa-8cb1-2bed2e9d1b31 | -6.46654 | -59.99287 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 88a772b4-5d8b-32e5-b192-9db4486fc536 | -10.10279 | -46.08511 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2f9b349-d323-3bab-9a00-550c59bea18d | -7.33254 | -55.60443 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6eddc6f2-78ac-34b0-b55b-eacc354859c9 | -7.61314 | -55.34486 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f171909f-663a-33a8-825c-e88ba8dfb504 | -3.3844 | -50.44186 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cc6b262-6843-3b05-aff6-a067f8f51630 | -6.4586 | -60.03732 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5c1f033-0d7e-3d25-9d69-86c7d05edf81 | -8.62088 | -54.63146 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd76e50b-5db5-348b-87a8-0f77e8ae1b56 | -8.34939 | -50.74995 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9959f7d-aa88-338a-af2a-0fa17895bbbe | -6.3511 | -57.77149 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97216b8b-717a-35d1-84c1-639790b40cec | -6.13463 | -59.96696 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6c8990e3-176d-3dfc-b5bf-61d6f96e5e5b | -10.78866 | -54.03181 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e1118c0-4970-3a66-959f-0fb1716060c0 | -13.92777 | -47.84765 | 2026-09-22 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cafcbc5a-26ca-32ab-94b6-1aa5c44b8031 | -12.35726 | -50.22632 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 495a307a-8de9-379d-a385-81af2dde120b | -11.46697 | -47.75079 | 2026-09-22 04:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3622c244-c108-3580-9b45-5017f24e08fe | -11.15006 | -51.10398 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9f94eeb-361c-33f4-b60c-4eec1780f692 | -12.39463 | -47.06377 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4544538-3995-3d12-bee9-1bded78d8be6 | -14.11447 | -49.87167 | 2026-09-22 04:49:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd27659e-f029-3786-9062-b6ac6596b506 | -11.1601 | -51.10555 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| dada86d1-2aa9-3901-b2ed-ea7de1ff5d2a | -11.15676 | -51.10503 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 10a0a730-929e-3d51-b63e-20f4737f08b1 | -10.71834 | -54.00866 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ff82585-71b3-3395-85aa-4f8f9de0696f | -11.43991 | -47.33635 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a282867b-d0ed-3c4c-9c2f-499cd64bec87 | -12.02327 | -47.81226 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fe682b97-f047-3ba5-b1b9-01e4fb164148 | -15.26455 | -47.60088 | 2026-09-22 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b255568-0128-3037-a819-59c114e5084e | -12.56835 | -45.97182 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 83009f82-9623-310c-b92e-39518186fa74 | -12.3148 | -50.18811 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6abad097-4454-3848-ab90-11efb319ccda | -10.54245 | -57.44376 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 845e75fc-1d5f-36aa-b925-325cdbc5091c | -16.38803 | -49.49457 | 2026-09-22 04:49:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ab86b82-15eb-3bf8-abc0-abba12df5b60 | -12.40496 | -47.08075 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bccd627f-835e-33c5-a8a7-4795dee8b468 | -13.86737 | -48.58389 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1d3398b0-c796-3caa-b0e8-371f52616087 | -13.3706 | -51.30882 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0aaa347-4c0a-3e79-8022-868b4b446440 | -10.72293 | -54.00179 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e385c08-6402-32fd-b2c9-e39b3cf643bd | -11.84227 | -46.81491 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f50ae895-dd1d-374e-bc7b-09f44a6fc023 | -10.61169 | -53.99502 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e00801fa-c432-3f0d-8034-536723294c7f | -17.86933 | -44.40483 | 2026-09-22 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d24beab9-0d60-3a07-9094-071140903743 | -15.62123 | -48.32525 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce90dadd-f289-3296-9c02-3612d7e50c64 | -12.91796 | -53.89722 | 2026-09-22 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef9a433f-1aac-30bc-ad11-b94eb678ee1c | -15.99165 | -43.28075 | 2026-09-22 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d9a45bb9-2dff-3fe3-aeb5-e8283fa717be | -11.4404 | -47.33272 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1be859bb-b30b-3218-bbda-0649e799846d | -11.32755 | -51.36626 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 239aaa9a-07af-35c6-b97d-d97c691ccdd3 | -11.31723 | -54.04541 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README67.md)
