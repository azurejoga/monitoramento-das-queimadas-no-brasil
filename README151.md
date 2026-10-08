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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4b3d821-31ec-39ec-9337-f3b93e883f56 | -3.11047 | -54.14907 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebbb728a-8f9c-3921-b5b3-6a377e54e1a1 | -6.08779 | -55.72993 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a38d7130-61ce-32c5-99e5-975bef98eb3b | -3.31108 | -53.85836 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06b0e36c-5aa6-3fac-bd4a-8c261bfcdc01 | -3.12072 | -53.78638 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 89bd38a8-bda2-39e2-8e05-3f20186e826f | -3.29943 | -54.07048 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d7619fd-195b-358f-87d2-ce9b3919aa03 | -3.27816 | -53.99905 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82a98a7-6efd-3a86-8869-90dadcbbd4cd | -3.40792 | -58.91239 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c19c1f8-be18-3cec-95ed-de056ae8946f | -3.79444 | -52.32252 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9396de5-13d3-3870-8475-bbc3bdf1ae35 | -3.70204 | -58.2913 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8d07383-1130-35bf-a44e-a9735f879ce4 | -3.65871 | -50.95266 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ef4ff12-ce7b-3826-9cb1-6529124764b2 | -2.78262 | -54.08097 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87bbe74f-1c02-3cc5-a86f-718c957f2159 | -5.10949 | -47.12292 | 2026-10-08 05:23:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18cc8997-cc53-3c8e-a409-92e645c0bb42 | -1.52992 | -54.81722 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 108c6ac5-7569-398f-b807-52dad9ac3fb5 | -10.28509 | -60.53663 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62b037f7-788d-3dab-9a20-8b6b8d36e419 | -8.60217 | -67.30566 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fba85189-d35b-3e24-a928-fc3a4e9d9eae | -3.02743 | -53.94224 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8971f759-fb6d-3cbf-8df7-b3d75f11beb8 | -1.36747 | -56.92537 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78410578-1aa2-3980-8c88-7e018880d445 | -0.84731 | -51.8498 | 2026-10-08 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c940f449-62f7-3ae0-bbf0-c2cea22dade4 | -1.4769 | -54.77966 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b014f04-8168-37a3-8aa0-a7aa067eca3c | -3.0541 | -54.20864 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8210fba6-8084-3f35-a98a-1f9e383488a1 | -1.10256 | -54.16753 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfd06ce4-b0e8-3a69-92d0-967b9435ed55 | -1.28769 | -54.5623 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bcf5ad3-e001-37ab-a748-ab5271bac2f5 | -3.70902 | -54.17046 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26c34030-d883-38af-9d55-7ddb6d00bc1b | -1.29506 | -54.55976 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fc6b6e7-0b3a-3563-b272-b09b4074d145 | -1.02347 | -53.73502 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58825828-826d-31a3-b7be-bbcdb50946bf | -3.0087 | -54.06331 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 85939e9f-b702-3453-b13c-e9043f798346 | -3.92631 | -54.57893 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4e7f8e0-5d55-376e-882e-93c5ca0b5078 | -3.61745 | -55.50063 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 224baec7-9b78-32a5-b0b0-4b0bcba5b66a | -2.81643 | -54.09413 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1808700-afb7-3d84-bf2b-6a3886a23efa | -3.07808 | -54.24269 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e3673f0-b0b8-3ed3-a4e1-386def2c0b02 | -3.6779 | -59.63421 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0646167a-1b5a-381a-8c37-13246d0e5ce9 | -2.99406 | -54.065 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6076e774-f217-3cdf-8986-533422d1b6ae | -3.70339 | -60.54884 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db5d5500-b695-31a4-8f62-ea0969dbe4cf | -2.95968 | -54.14283 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94ced0a9-3b1f-33fe-8d12-e6656620baba | -2.58626 | -56.15553 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d9f4203-4f01-3b82-8c40-eb1f8ff6f87b | -3.65164 | -54.28449 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74117f3b-587a-3102-a8f5-49ad4861c384 | -3.25734 | -54.0399 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 763a6638-f46e-3685-bcc3-f08cbaaadba4 | -4.1178 | -54.01954 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fec6883-cd57-3f1d-8c39-ccffc3643a0f | -3.9401 | -55.85085 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29518d99-30d2-321d-b6b2-5907b3b684dc | -1.1246 | -54.11768 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 102eeb96-d4cb-3d40-b3d1-d34af92601ac | -4.06844 | -55.3209 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5d804fd-a13d-3bbe-b491-481c61a199c0 | -3.22307 | -54.37351 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e577724e-5f14-3dbf-87da-7511f0cf89d3 | -4.27078 | -54.87263 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1e3fa1e-5540-3eab-827c-7592025f4234 | -3.33351 | -58.17046 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ac8c581-9ef5-307e-9aa3-aa9107f332f3 | -7.0795 | -52.68005 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee21f59c-087d-3c50-b214-ca7797d76928 | -3.49542 | -60.20989 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb86d7fc-49b9-3d0d-9e91-47aa46bdfba9 | -3.30545 | -54.69284 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae8e3309-5f7b-34e8-a9af-a89d99e2a28b | -2.49741 | -56.12051 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d412b844-f1ad-3bd4-a088-33ee83293c57 | -2.99225 | -54.77358 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cb50eef-6c9f-3b86-a47b-0ae2005bd4f6 | -8.61838 | -67.05459 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 150c8865-8303-3a99-b417-6eb8dc2d16b7 | -3.52458 | -54.63071 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5893097-84db-3296-83df-0697f5d28d0d | -3.07685 | -54.27375 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a3851cd-3a5c-3aec-9e14-c44211809d51 | -4.85366 | -42.83177 | 2026-10-08 05:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dcf584b-ba06-3a87-a3c1-ebd9dc40f076 | -3.01853 | -54.09262 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6ad3cfd3-279e-3eb7-ae33-3ed84fd6ae73 | -2.98273 | -54.13843 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db1a0e3c-fcc6-3256-942a-a72b81a92881 | -3.02351 | -53.89731 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4896faae-728e-308a-8a1d-925a454b767d | -2.39049 | -56.1321 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12486620-7d38-3b38-a7a5-bd3dceea3f45 | -4.81637 | -54.73807 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74c33620-cf9d-3c3b-bc1d-71f015883ce0 | -3.04644 | -53.91296 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32824495-7449-3d31-9693-625f8f0c8bdc | -8.73607 | -45.16626 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eef916fb-7dcc-37ae-ab1c-44a0fdba7bdd | -2.65279 | -56.54887 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d29229b-60d0-3211-821c-1532e2b9a637 | -3.16233 | -50.5978 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b00975e-7cb3-3d4b-9066-07a95fb82732 | -3.04447 | -53.94893 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8e1952d-5a61-3b2a-abb3-4701ceeaf3de | -2.50524 | -56.15717 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a197e55-cf08-3f3a-a254-bae824a03b96 | -3.41202 | -58.90912 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc4b3b6a-05d8-3c8b-bcf3-ebdc54b0fa01 | -3.27157 | -54.01813 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba61136d-6626-3b06-9a70-110cbddb10b1 | -3.66291 | -57.09127 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 544f10d5-4aa0-3bd4-b379-f3e4ab443424 | -7.22315 | -55.08862 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e3074216-2e9d-3433-84d0-da10f294649d | -3.85656 | -55.97794 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 500d1306-73ab-39cc-a32d-256c264dba22 | -5.98475 | -55.69889 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a9ae30-8380-3cad-bca5-b462d0097934 | -3.26278 | -50.40897 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0359311b-c438-3863-9795-1fc95a17d2dd | -4.9289 | -55.8672 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 036e948a-7468-3642-8c42-aa2c3f07a73b | -3.03388 | -53.94728 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d844ef02-642e-394c-abf4-e0fc7d5ccb2a | -2.78642 | -56.49529 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82d51266-bce3-35c2-9eb1-ff54326de1bc | -7.22865 | -55.16888 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42527ad5-418b-3b76-99a4-c162da4a42dc | -3.06306 | -54.17461 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a0fb965-1070-3593-afff-54535ab60bcf | -5.19914 | -48.2101 | 2026-10-08 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d4981a6-4768-374f-b6c9-3eaafe103a4f | -9.84588 | -57.67075 | 2026-10-08 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c5b6a8c-0911-30e7-94d5-662cd6b40194 | -3.20879 | -50.55494 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2ef27bc6-6efa-30ec-b4e9-609425c33fca | -3.06048 | -54.21355 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 614c3779-e7d3-3e8d-acf0-f3ea46ab3fe0 | -3.26329 | -54.02487 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ed749b94-103d-33ee-93c7-ea016d025e5a | -3.29961 | -54.04649 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a8eea15-529f-397e-97ee-14698b24b9ef | -2.99937 | -54.0539 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6edecb8-f42a-360d-9691-956211b58351 | -4.10947 | -59.91761 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7924907c-0d06-313e-82aa-58d1ea6df045 | -3.05113 | -54.39391 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a56b66e6-d3ab-3fb7-bab2-4549c2646040 | -4.26926 | -54.86868 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05c797d5-1f75-3f5a-8697-73a8448a0bc9 | -3.0113 | -53.9078 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df23a044-2d4c-3722-b724-8d6eff7a8f39 | -2.78553 | -54.08537 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d93c990c-0cb2-324e-8f66-e86224164c42 | -2.88169 | -54.09135 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fcde636-8119-3d31-9c43-f1057c6cea2e | -2.87552 | -54.20059 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 739b753d-67d7-3e95-85b8-80c0039039a4 | -3.44256 | -56.45342 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9f9f7fb-b11a-363f-bb29-c22e90a91c55 | -3.06263 | -54.24511 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b38319-319a-365e-ba41-6b2fb054b987 | -9.20543 | -66.08968 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18b89910-5786-3cdb-a47a-c6c46019dc04 | -3.7718 | -59.25447 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87084a9-cb67-333b-b000-fec1dc07cf62 | -6.94511 | -45.27624 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02f4120c-8133-30a8-ab71-aeb953520d18 | -9.28037 | -60.17485 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c84bd62a-375e-3ba0-841a-1bb7fd2167e5 | -2.50747 | -56.1646 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 85224735-3e61-364d-b318-4eaddfd55fad | -2.93808 | -54.14351 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a43cfa08-3ec0-34f4-a540-cef4b81e778f | -3.02444 | -54.07767 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78b57089-0e41-3910-891b-db6e1da9ecf3 | -3.8393 | -55.97881 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README152.md)
