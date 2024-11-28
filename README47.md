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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 712879bc-8c69-38f9-adaf-56af0f29b8f0 | -2.70665 | -46.20159 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4a57279-a673-304e-97ec-1b05f8abe417 | -1.66183 | -52.72594 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68bc9a3e-f45e-3ff1-9cb1-b5b94062ce35 | -1.35114 | -51.96076 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0666929-d76b-33b9-b013-a2a721f0c908 | -1.28511 | -51.73273 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2cfb7c4-6445-38d5-9ca9-a7514aced0f0 | -1.2884 | -51.7302 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7c95518-014b-3f05-9c26-c7622e96cd66 | -1.97279 | -48.68639 | 2024-11-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c936e1da-92da-331e-bedb-9a51309bc4d9 | -1.74311 | -46.21189 | 2024-11-28 04:23:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1226a2f-b22f-35f7-9934-dfbc3f8cda71 | -1.31567 | -52.87466 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e54f663-0569-3434-a1a0-34f466645bf1 | -0.77384 | -52.39428 | 2024-11-28 04:23:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2417d24d-a0ac-3ea8-bcd8-27f914a92c9b | -6.3248 | -41.918 | 2024-11-28 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1cf0007d-2ce9-3659-8255-818ddd40f622 | -2.51481 | -45.19604 | 2024-11-28 04:23:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59ee12f1-354a-3c8c-a177-636e1e1dab80 | -2.73774 | -46.08889 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 980d0ba3-602a-343f-805a-502c84eb76d0 | -1.64582 | -52.73783 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bfb342d-b842-38f9-bca9-b866a5f4bf7c | -7.79481 | -49.99597 | 2024-11-28 04:23:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bed58b7-d425-3e23-bcf1-36c82644c458 | -0.59223 | -51.71167 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64bab8b-4800-38e5-af7e-bab6ecb84449 | -1.05779 | -53.21031 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd497085-a406-3f0a-8d23-e7650e220e0b | -1.69572 | -52.63939 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a629fbbf-67d9-35ef-b40e-2881d0be409b | -1.28569 | -52.10585 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ede3a6f0-8004-3cb3-acae-0af0ce391ef5 | -2.71568 | -46.22799 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f00e03b5-356e-368b-b74c-8652488a522b | -2.5806 | -46.20293 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d12e2eb-56e6-3812-951b-e31a3d870354 | -6.70231 | -47.26995 | 2024-11-28 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8add0f4e-d268-331a-9e8f-af27fce5f57c | -2.298 | -46.14068 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc964e84-0e0c-3560-ae8e-6c6e7f28020a | -2.7129 | -46.22399 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e563e523-fb5b-346d-a918-e88bcf1fb4ce | -1.31407 | -52.87085 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 99bc16d1-b767-31ab-bbbc-1da931a6880c | -2.63771 | -46.95674 | 2024-11-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e64b5fa6-0cd8-31ce-b0cc-71612cde0c08 | -5.86313 | -44.72311 | 2024-11-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f120197-4fe3-351d-a3a0-5e284088680e | -7.69525 | -42.9798 | 2024-11-28 04:23:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f08fba64-660b-3707-ba94-647ab2c1d92c | -0.84351 | -48.20369 | 2024-11-28 04:23:00 | NOAA-20 | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f296dec8-2a5b-35cc-9b2c-2197151dcf04 | -6.58521 | -47.9124 | 2024-11-28 04:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dd303a0-a30d-31e0-8631-a5e23e3f0ad2 | -2.58225 | -46.19248 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ad32840-c622-303a-9e21-1e1a65a53a96 | -1.3096 | -47.8157 | 2024-11-28 04:23:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 921dba4c-a34d-3ed3-aafe-c22e0a9d1759 | -2.01384 | -46.39502 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 369af5bf-2eb2-31a4-a062-d253e5455f67 | -1.19681 | -51.75266 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5925ddcb-7289-3a0a-953b-9c50d2e4418c | -8.47463 | -47.81117 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d991373-68b8-3cb4-8872-6b2a8f50f30a | -8.56065 | -49.20098 | 2024-11-28 04:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5efbbfb-fb40-3960-aa19-3219a7f07283 | -1.28319 | -51.734 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba394934-ebd6-3a37-bb3a-2321559b1216 | -1.34106 | -51.67246 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 74d8f0ab-4818-31b7-9d65-17ebe82beb16 | -6.47318 | -54.91832 | 2024-11-28 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0696e519-2ac5-310d-9e6f-d46c4f9ff10a | -1.12644 | -53.64251 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c3a0e7-223e-32f0-962f-bf49e4e22c00 | -7.19586 | -48.60612 | 2024-11-28 04:23:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63fd3c6a-7108-3506-bff0-cb8a643f3caf | -5.33665 | -50.05414 | 2024-11-28 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f16a01cc-cf0b-311b-b303-8a700f5f0602 | -2.47361 | -47.04298 | 2024-11-28 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd0d2648-89e6-33b1-9844-f6009d026e0a | -6.92146 | -38.1441 | 2024-11-28 04:23:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c02acadf-71c7-3a85-b9e7-0ce76cb17482 | -6.83263 | -44.39244 | 2024-11-28 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40e42735-6842-361a-9f79-97ebd046850d | -0.98542 | -51.72277 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 244f7061-35ab-363f-9a75-0d28d77b8090 | -8.69228 | -47.96009 | 2024-11-28 04:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4a91f51-f173-3abd-ac1b-efc4109b61b5 | -6.09394 | -48.04348 | 2024-11-28 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51dc0a23-e38e-3707-9b51-926b2d4d3d3a | -5.98164 | -45.35583 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 33af8318-d516-322b-9aed-f17402e6962f | -1.6579 | -52.71994 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6724dbe1-ccb4-3eda-8e96-9891e137141a | -1.69124 | -52.48199 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f47cc19-9ee6-3700-9d5f-69f3fae98be3 | -2.67389 | -46.15007 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ed40cad-389d-32e6-8f56-efa42524404f | -6.56517 | -44.63103 | 2024-11-28 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d919af91-e2eb-3723-a29f-8a78ae08b5a2 | -2.10151 | -46.57214 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86b91835-df8c-3b81-bff8-82c7ee258b32 | -5.50983 | -46.26294 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40bf44a8-42ed-36de-b060-eae1f1ae4958 | -9.17611 | -44.72522 | 2024-11-28 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8335a40e-c6e5-310f-9a47-84db15c6ea4d | -2.72124 | -46.27891 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d04be1b1-bfdb-363c-bec3-c92fc5fa8c38 | -3.68195 | -38.67668 | 2024-11-28 04:23:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ba0f218a-4d30-3df1-bf3e-65bf5c35035e | -2.71069 | -46.30235 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec25c5c8-a92a-3691-aeff-74e2bd9c492c | -6.09053 | -48.04291 | 2024-11-28 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3dae46b-cb48-3887-9387-8289dd86ad86 | -5.72686 | -45.83453 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54b81c53-625b-3021-b5c7-b9661d8fe4d6 | 0.33833 | -51.07562 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5de10fa4-ebc9-3bd9-8c60-525fc18cbd37 | -2.7179 | -46.25694 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc020e1-7d08-39e2-a340-02cda228be7a | -2.6024 | -46.55938 | 2024-11-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce1ba2d-5b28-3b3b-beba-c1ea2ce8656e | -2.71645 | -46.11755 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 232d3837-7197-3c20-ab49-2aebd90510ae | -1.69327 | -52.6248 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57c076b8-d735-36fe-a4f4-26f60c90b0c9 | -5.50215 | -47.16659 | 2024-11-28 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db5936dc-f635-30b5-a79b-aa7d854e2c08 | -1.04373 | -52.42225 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bad1def-657c-37bb-b1b8-6e28d72b5ab0 | -5.61354 | -44.48653 | 2024-11-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3da728cc-fcf9-3263-a24a-90b09c89a3d8 | -1.7186 | -46.15445 | 2024-11-28 04:23:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdf17cc1-c69d-3fe6-b472-b8aa8bc132b1 | -1.33121 | -51.93832 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cadc6bd4-df1c-3e22-8ece-9e174e3f0a1e | 0.97583 | -50.12576 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef39fc8c-5175-316a-9781-7da81cb5610a | -1.69635 | -52.63585 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 697efb5f-3b53-3a3d-a7b3-78efab904c48 | -8.5635 | -49.20547 | 2024-11-28 04:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7de3253-e5bc-3f80-bb5e-e0429842eaca | -2.27467 | -46.3739 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2e4c4a2-81f3-37c1-b985-e10fcef5aed8 | -1.79156 | -46.27352 | 2024-11-28 04:23:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62dee1ce-798b-3991-b786-a8d455d623e2 | -6.71345 | -47.26448 | 2024-11-28 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d539c89-933d-3c9d-ace9-1e4384790990 | -5.6438 | -46.3836 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1978a09f-dbb0-3307-9d8b-4cdc0540dca5 | -5.0481 | -47.80733 | 2024-11-28 04:23:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d805f0c2-002b-3dff-8d1c-f32450276145 | -2.71847 | -46.29639 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a597636f-d8de-3eff-a94c-a8ce9963a52e | -8.47406 | -47.81472 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57a55c1b-8d20-3525-a147-a9b1d2e44ddf | -6.17336 | -42.61724 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 805360e9-90d3-3a62-9ef1-7f04329f3c36 | -1.37452 | -53.6357 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f660118-ee2e-375f-8469-486571550446 | -2.44308 | -46.27815 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 013db407-5033-3f79-9803-8447b4b80f73 | -1.15344 | -53.57329 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1218a42e-cccb-3fe0-b5bf-c8d8e875f587 | -1.3108 | -52.87375 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7529c11-5ce0-34df-a003-c9ed8cc3fa8f | -1.34747 | -51.98418 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 721777cf-93b9-38c8-8be4-c9e5421f53cd | -2.6846 | -46.27679 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 103aa0d3-03b7-31c6-b427-2f4904b95d97 | -1.36073 | -54.98887 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28c11b45-fc89-3270-85c5-bb3c5ce849a6 | -1.65347 | -52.47581 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c4324b4-5114-3ff5-a292-cd4566de455e | -7.7941 | -50.00025 | 2024-11-28 04:23:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0e54f5c-f07e-39ea-b6c2-941b17cedd4a | -1.6098 | -52.62532 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ef6b55b2-f4ba-30f9-a4eb-7097e723a341 | -0.94799 | -51.65839 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ade9bbb-194f-3e03-8400-92a23263f376 | -1.16311 | -53.67821 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d069195-679a-3147-8ad7-001c254fc59a | -9.1721 | -44.72846 | 2024-11-28 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a2e6c15-cce6-34e8-b63b-9c0c9015ed3c | -2.07467 | -46.32859 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56156289-495c-308c-914a-91ab01ac4e90 | -4.09008 | -54.76746 | 2024-11-28 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab84c356-b6bf-351c-8b4e-206a138fa66f | -6.17402 | -42.61291 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e5e3a840-c1bb-3c85-b184-b37c28b63efc | -1.15841 | -53.6744 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 032d47ef-03dc-3eae-b39c-335d8a19b1a9 | -1.15797 | -53.67714 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a0b25f0-3304-386f-bdae-f20f56150a21 | -2.66985 | -46.6025 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README48.md)
