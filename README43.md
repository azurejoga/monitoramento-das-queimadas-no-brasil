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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f646e52-0d1d-3a45-8aef-f77da6a5d798 | -3.66219 | -54.42517 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6a9103d-f751-3954-942b-43c3b95299f3 | -3.65583 | -54.4202 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adc1e6c4-1214-3b40-83f5-8f43cb88b0ce | -3.65065 | -54.79711 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d8237cf7-69f3-3c00-b9ba-409cb54b4e7b | -3.64777 | -54.79247 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9bc1e3f6-8ee1-3efd-a7fb-51a287c2ed3c | -3.64712 | -54.7965 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4c96fc08-ec8e-304d-afa1-3f396037fcf1 | -3.64423 | -54.7919 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43af5c42-1d39-3fcb-a12b-8991bea98741 | -3.63972 | -54.68518 | 2024-10-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7763354b-ecd3-3311-8039-c99b73cb5b51 | -1.99723 | -56.51551 | 2024-10-23 04:51:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fc7872a-059b-3354-9683-5569e3711de7 | -1.99324 | -56.51486 | 2024-10-23 04:51:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff676722-3f08-3047-a675-179b75e52f93 | -1.59736 | -55.8338 | 2024-10-23 04:51:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c375457e-af08-311e-aef0-16b7fcb622d4 | -1.54504 | -55.3479 | 2024-10-23 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68cad9de-46d4-31c2-a032-c3e8d4aa738e | -1.54129 | -55.34732 | 2024-10-23 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138adcde-6199-39c6-8903-2453ebde562d | -2.20975 | -55.05321 | 2024-10-23 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3d3075e0-bb9a-312a-a9c9-9227c9254dcc | -3.56844 | -55.51846 | 2024-10-23 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3c855e8-3834-3fd4-baec-976912a558a9 | -4.87841 | -55.83765 | 2024-10-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94efdb86-b77d-3c83-bcbb-0fb9c0808e38 | -4.12165 | -55.57754 | 2024-10-23 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bcfd66a-682a-3c6a-adf9-5ebc0cc150e7 | -3.90314 | -55.39565 | 2024-10-23 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b28acee-2c6c-39ab-a92e-e3ff1330af1a | -3.90246 | -55.39989 | 2024-10-23 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e17faa8-3f7e-3671-8d6f-8f113fdb520e | -3.86105 | -55.58744 | 2024-10-23 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e603b555-16ef-3efc-8c47-dc91706b4dda | -1.989 | -56.56752 | 2024-10-23 04:51:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9218faa3-64ea-35e7-86df-7f17be6acae4 | -2.1062 | -56.58987 | 2024-10-23 04:51:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2a46396-00d7-3a28-8130-0649b609c1aa | -11.37547 | -61.27533 | 2024-10-23 04:53:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f8ef2b0-b2e0-35e8-bbb4-4d5fcff71089 | -10.42804 | -58.82121 | 2024-10-23 04:53:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca8cf1b5-af12-3c17-865e-5be8aead22bd | -10.42681 | -58.82839 | 2024-10-23 04:53:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fba6d090-e5eb-3f21-a3bb-7e141a5b7dc3 | -10.20654 | -59.15191 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17dcee73-4a1a-3721-931b-510f7af82edd | -9.98349 | -60.00081 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d013b94c-f603-3ee9-bb81-cdce12facede | -9.97906 | -60.00002 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2993045a-e741-3dc4-b733-a9bda5314042 | -9.97463 | -59.99922 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce0784e6-b3f9-3062-a338-5f848f789165 | -9.87282 | -59.98643 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 323a0015-0343-3226-92b5-bf0005642ca0 | -9.86838 | -59.98561 | 2024-10-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea3838f3-023d-3572-b3b3-14185277fb1f | -11.99698 | -43.0848 | 2024-10-23 04:53:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 84c07abb-57aa-3593-a7cc-1c663c9f466f | -11.99529 | -43.08575 | 2024-10-23 04:53:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 727bdb16-c31e-3564-9fe3-73fd5e1dd72e | -13.10259 | -43.36649 | 2024-10-23 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cea0425c-29f9-353a-93cd-e44ce381f079 | -16.68156 | -43.8856 | 2024-10-23 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a718a7f-a5f3-383c-9039-fb17f5d5798d | -10.60798 | -44.28088 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0fdf938-3b02-3380-aeee-87fe3858308e | -10.60307 | -44.27671 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 824f4579-c630-311c-9acf-bdfcbd66e29d | -10.60263 | -44.28022 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0a7fe7da-455d-3e4b-962a-e98b60581333 | -10.6022 | -44.28365 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65eb768e-e6f0-3eff-8870-5679c1a9f948 | -10.60177 | -44.28708 | 2024-10-23 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc201130-6084-3b5c-9a7e-c9085271b196 | -10.58528 | -44.28846 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9e28bc4-d584-3495-b15f-32c0a69eda85 | -10.58486 | -44.29188 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 979bd4d5-98c8-3ea7-a7fd-b957b76e812e | -10.5818 | -44.2891 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f8b5e33-999d-3734-a02d-84990f6b9f0a | -10.58135 | -44.2925 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ad393c5-2636-3963-93ab-c138cfc0c79d | -10.57993 | -44.28773 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d487c287-8024-3e52-b509-4b9daca5554e | -10.57951 | -44.29114 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98666186-bf6c-3baa-a226-f9218381497c | -10.57909 | -44.29452 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68b862f0-68e4-3ce7-8a94-c77c70560067 | -10.57601 | -44.29177 | 2024-10-23 04:53:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e627f583-a43a-35c7-8c91-0556f8f14ffa | -10.70216 | -44.38318 | 2024-10-23 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44fa3a82-4d6e-3cb8-bc44-77f94330ff8f | -10.88031 | -44.539 | 2024-10-23 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e545cbb-c085-38dc-b159-fe38bef8a0e5 | -10.75965 | -45.01985 | 2024-10-23 04:53:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4209fb6-e4be-3ff8-b7f1-1f92f90f1521 | -10.75926 | -45.02285 | 2024-10-23 04:53:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18d8cbb3-8842-3b39-8a60-e2ddb304ce98 | -10.62717 | -44.59377 | 2024-10-23 04:53:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32218cf7-efd6-35e3-8154-dc42b6090b05 | -11.1333 | -44.9566 | 2024-10-23 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f70a2e2-bfe6-3a4a-a1d7-7859ea17472b | -11.13155 | -44.95347 | 2024-10-23 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22961747-77cf-3f67-a649-e5e4ac955f25 | -11.13113 | -44.95669 | 2024-10-23 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49af80a1-f757-3414-afbe-33b7dbdff115 | -10.99853 | -45.2626 | 2024-10-23 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a91ebc3a-8cb5-39b8-b9cb-9edd2d46854f | -12.02719 | -47.79271 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f62369eb-f021-3463-91e5-bed87a1ede46 | -12.02662 | -47.79687 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 302c8790-e20d-32bd-8454-d784d4281fc8 | -12.02292 | -47.79189 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 388a0e31-aa7b-352c-80fe-06d9091c7739 | -12.02236 | -47.79605 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daefb224-4e91-3520-9270-e91a3a9f212f | -11.88653 | -47.71046 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7b848d6-5b98-3407-b8aa-a262cc69067a | -11.88221 | -47.70988 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6bc1d830-cffd-30ba-89b8-7849b4cb35bf | -11.8243 | -47.07422 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66a28660-d9f3-37ae-9a3d-01003ee24bf3 | -11.82368 | -47.0788 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b21c465-9beb-3a55-a955-290a53c06b3b | -11.82187 | -47.07534 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2c51e1d8-3508-3a3d-a07b-eb771e41d48a | -11.82128 | -47.0799 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 12e34c97-b699-3c94-a4fd-dec8cd9dd711 | -11.8198 | -47.07363 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 630e2635-cc45-3037-a283-15a7590ae6ac | -11.81918 | -47.07817 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b5643ec2-ba23-3732-b308-9c7b49c107b9 | -11.81855 | -47.08275 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3f1fcd66-40f7-3053-8a88-7a483c750109 | -11.81736 | -47.07474 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dd1997af-e5f9-392d-950f-48a48125d5a7 | -11.81678 | -47.0793 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 02ff826e-4162-3695-b5c2-a44f910a4d7f | -11.81529 | -47.07304 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d06a1f34-2678-3fb5-bc82-0046bc85fc6a | -11.81467 | -47.07759 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7cb9f700-6a73-3d88-a591-e6dbe62c13cd | -11.81286 | -47.07415 | 2024-10-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fbe47cfe-3d26-34e1-b192-0c195c44fd9d | -11.6335 | -47.58218 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2952839c-d9a2-3613-8628-76479605c598 | -11.62975 | -47.57734 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| df5ebe06-f173-3ec1-960c-4a9b48e9c763 | -11.62917 | -47.58159 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f9f7cf5-8849-3d1a-8c46-b2854742e0b8 | -11.62541 | -47.57674 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7e6ee128-2a83-33bf-ad95-f62c633fb242 | -11.62483 | -47.58099 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b80add9-5cd7-3760-a244-efef4f497fce | -11.6205 | -47.58038 | 2024-10-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 98a7d6a9-b413-3405-8b5d-b46dc2434149 | -11.28356 | -47.58151 | 2024-10-23 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f190b61b-435b-37fe-9bb7-0c43016aa1bd | -11.28299 | -47.58564 | 2024-10-23 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0062cd8d-e162-324c-9683-bcdd54a47260 | -12.8055 | -47.89379 | 2024-10-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56df8877-ec8a-3a89-80a1-72eb8c972f0a | -12.80173 | -47.88897 | 2024-10-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b0b8635-b7d4-3893-ac1a-147b9a32d219 | -12.80064 | -47.89739 | 2024-10-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d653c990-cc7c-381c-ac53-0448f3f535fc | -12.71879 | -47.93373 | 2024-10-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9231c98d-f1af-3750-baf3-8cc5357e82e7 | -12.53859 | -46.80545 | 2024-10-23 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce37c6d8-0267-3f4f-b717-b5ebd319f8d0 | -12.435 | -47.19996 | 2024-10-23 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3308c705-3bb1-32d7-8ca6-1c5a9f8727eb | -15.78742 | -50.52164 | 2024-10-23 04:53:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9d304ac-cba2-33d9-8fce-d3879273f46d | -10.63761 | -49.02638 | 2024-10-23 04:53:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d5712ed-33a0-3d8b-a2e4-49f50b1c82f2 | -10.64318 | -47.68873 | 2024-10-23 04:53:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44b1845d-c2b7-3bf9-95a3-d7f95cca216b | -10.09583 | -47.71186 | 2024-10-23 04:53:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de95d6a5-c352-3264-b6b9-38e371ad5790 | -10.68729 | -47.83898 | 2024-10-23 04:53:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d63a406-b10a-36c7-918e-1d1bdf3c603c | -10.82419 | -48.32108 | 2024-10-23 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f517fe8-1129-396c-8af1-2579755f7bc2 | -11.72852 | -48.36219 | 2024-10-23 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8129b172-afff-334c-bcbe-6efcb37d95ba | -11.59653 | -48.50348 | 2024-10-23 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c771bcbe-418a-3214-91e9-e90ec6c92eb5 | -11.12522 | -48.6356 | 2024-10-23 04:53:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 448e25d8-d7a6-3af1-aa73-7daf796ec821 | -11.11269 | -48.6373 | 2024-10-23 04:53:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2609e6d-0c68-342e-ba67-de22326eaa11 | -11.1082 | -48.64022 | 2024-10-23 04:53:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7088bd48-890f-3558-95d7-17567339efff | -11.02951 | -48.27686 | 2024-10-23 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |


[Clique aqui para ver as próximas entradas](README44.md)
