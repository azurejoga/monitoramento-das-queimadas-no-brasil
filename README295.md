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

## Dados Diários - Página 295

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30640667-af5d-3ff4-ba63-6971234e2cfc | -5.83862 | -42.41419 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 874ee47d-8061-3ae2-9190-74c2a2ba83e4 | -6.58751 | -44.8648 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d18e9b3a-fc6e-35cf-bc09-7e31ce476b99 | -7.61072 | -44.80682 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d68327a2-b958-3ec8-9162-05f37f9a1b64 | -6.0388 | -51.72628 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c7615c00-bfe2-35e5-a6fb-7c6e178c3c07 | -4.08489 | -48.95934 | 2026-10-08 16:20:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1f9da06-060e-3e77-bc12-d852acce14cf | -7.76335 | -43.82881 | 2026-10-08 16:20:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8993c04f-8e55-3981-abf2-bed213af2e4b | -6.03277 | -42.71944 | 2026-10-08 16:20:00 | NPP-375 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 2b0863da-99ce-3146-bb60-d5cbbb67110a | -3.98739 | -42.85957 | 2026-10-08 16:20:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4cdb675f-f440-3689-a1b9-49809e525e9e | -6.16015 | -52.65385 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 17a029b8-c46e-32a6-8ce8-1ed168aa88d6 | -6.66731 | -45.36624 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 24a85396-29b2-3d2d-88ce-06d55cf0b441 | -6.88758 | -43.70115 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.8 |
| e9bb337a-0ef7-335f-8530-816c3c0ee9c5 | -5.48235 | -44.59842 | 2026-10-08 16:20:00 | NPP-375 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b08171c9-d4c7-3921-b106-78b7050c279f | -6.15395 | -47.92786 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 138a4e02-1e9e-3904-903a-3f841898122e | -2.86668 | -54.16652 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cfbef6d1-b1e6-3fa4-a21e-fa16827a1719 | -6.31499 | -44.03881 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 574d701a-8dcc-347e-8707-47c38668bb16 | -5.23415 | -40.57774 | 2026-10-08 16:20:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7da9b9c6-38cc-3983-9517-05f53c4dad7a | -6.32556 | -46.54334 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4390f9f8-778e-3794-9298-4a85a6eb79f7 | -6.82202 | -38.54012 | 2026-10-08 16:20:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 91959ef2-dee0-3128-9988-5838c1d8f3e4 | -5.10336 | -46.21512 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d98851c4-3df0-3677-ab63-4658624ee361 | -3.89256 | -41.59876 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 37ebfbd9-faa7-36ea-8ef6-425bfd374b89 | -5.99337 | -44.13352 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a7d0da6f-ffa1-3773-bca1-00bc8d3fd90e | -5.72113 | -41.77219 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 46cade33-3720-35e9-85db-5b354b9424d4 | -4.09054 | -44.10885 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| c04f5e4d-0ff0-363a-84fc-ff99bdb9614a | -5.96203 | -40.91748 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| cba926e3-4d81-318f-a4c9-01173a1cd7b3 | -6.52663 | -46.12128 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 033afac3-7ea4-3316-91b2-60fa4ef79790 | -6.16276 | -39.43962 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 2a176323-16fb-3254-89d3-a641b03062c1 | -6.38143 | -45.78366 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee1af6f3-2ad1-3a31-b04f-9b3cc411cbcc | -6.93729 | -44.56803 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2545bd42-75d3-34b7-b324-80e156cac8b7 | -3.13026 | -42.932 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee629464-e418-31d4-a715-1b291d8b203f | -3.0046 | -54.08046 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 410c0e05-1b7b-38f5-95bc-67ae83f6fbbb | -7.73737 | -45.44306 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 371e5e37-0e82-3018-8ae5-4c192e1e107c | -5.77198 | -45.3892 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d40f44d7-1f4b-3ea4-a57d-077324aef795 | -6.79895 | -45.05606 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| a469a7fc-7aec-38ea-9568-00b80eca11f7 | -6.86025 | -39.15842 | 2026-10-08 16:20:00 | NPP-375 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 14a2f7b7-3e9b-31ce-86d4-c59162d436e5 | -7.25516 | -48.06638 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c71268cd-29d8-3e08-9a79-d8fde3cb5f79 | -5.38048 | -44.19651 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0454fed4-7752-3251-8768-01e856349d05 | -8.35464 | -47.64612 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16d050c4-1487-3a34-8f30-e5ef05838832 | -7.07786 | -40.93948 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 850833f9-ae53-3101-b574-1e2889412aa8 | -7.09924 | -41.74616 | 2026-10-08 16:20:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b47ccd1f-bca5-3f04-9b85-c0af56f84cf9 | -4.1403 | -43.20554 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 56c6671e-49fc-333f-bf84-56b26c28ccff | -5.76818 | -42.06369 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e4aab1e7-15a3-3bf8-b6e3-992e8fedbbec | -5.77685 | -45.39261 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5b8253a3-110f-3fc0-ae69-1d0ad78f1def | -6.64971 | -43.76632 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b59b5eb3-9c2f-376b-8547-203bcef2b74e | -4.09334 | -44.12803 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| aa060bcb-ac1c-3f92-bc78-de9ec6e71c15 | -6.50485 | -42.03429 | 2026-10-08 16:20:00 | NPP-375 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| e6c3dd47-082a-3362-9130-3e361f25fcab | -5.99082 | -37.38141 | 2026-10-08 16:20:00 | NPP-375 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 6657752b-a38f-3f7e-b85c-2899f07b4275 | -6.18637 | -53.43261 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 314a8a88-02b8-308c-b9eb-d70cfe643afb | -5.69269 | -53.4814 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 6f677e5a-037b-399a-a2cc-88c2a5c25b15 | -2.10937 | -47.96256 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a4a2d240-0c5e-3287-ba3c-5121e2f9ee99 | -6.32052 | -35.13424 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| b54d6320-2120-3bef-80c5-6c6c044de8a2 | -5.37899 | -44.1866 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1c660ebe-98c9-3db6-bf9f-f0c591b50c6f | -5.75076 | -41.73251 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 702e28cc-e30b-3810-b7a6-73847ab48be1 | -4.9432 | -42.72883 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c43be0d0-44c8-3f7a-bf0c-8ab15d5b8171 | -8.10279 | -47.12359 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f3022ede-67d4-34e1-b7f1-e74003b36305 | -3.78747 | -41.66296 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| db9ab9b9-ae69-365a-9cc6-0f38ac0d6f3f | -6.06876 | -44.3882 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 692930b4-81a4-38e5-8e0a-f9138b79cc42 | -6.92951 | -45.26431 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d7c094bd-d291-3325-a9b4-7514948c34e0 | -3.85555 | -44.12313 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| d91cca52-bb5c-3f47-91c6-ae63ff461297 | -6.69118 | -44.11181 | 2026-10-08 16:20:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 59653c1f-3d96-3176-a7b0-c040fbf0178c | -2.98072 | -54.06898 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 0fb9a1a4-ab3b-393a-9be8-d995b9d06b77 | -7.76225 | -44.1694 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1beb9e8f-25b9-35d1-89bb-2dd06c2610fc | -7.07445 | -40.94001 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9dee13b4-9363-3b75-905d-ee9ca7937333 | -2.07757 | -46.5855 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0eb09959-e614-39c7-ae7f-171b60462c18 | -7.18668 | -52.63047 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0b726e26-0296-312e-a7e7-0c35b60b8fa1 | -7.20496 | -46.53194 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d6582566-8d18-368b-bff0-79819e7d4e8b | -7.02808 | -44.72968 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1e473524-2a5e-3ecc-9af5-5b5b189d0e98 | -5.72519 | -41.77552 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 1fa641a8-f71e-3ab7-8760-358f8b0d6cc5 | -6.04989 | -35.18812 | 2026-10-08 16:20:00 | NPP-375 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f53f8630-5085-39b0-9210-125551c6582e | -5.28079 | -42.74187 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| c5c8842e-89f7-39cb-934c-9e8b871680bb | -6.16039 | -47.93647 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 969b36e2-cd88-3c82-8a2c-7221cd17f70a | -6.33435 | -35.12229 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 6c03adb8-cf21-3a26-b922-72fca95a9570 | -6.01344 | -42.26093 | 2026-10-08 16:20:00 | NPP-375 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 66b74691-f739-36f2-a164-2e1edcd08528 | -5.70498 | -41.73542 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e9b01747-bc9f-3235-bd5a-7023816d3957 | -7.74109 | -49.59586 | 2026-10-08 16:20:00 | NPP-375 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a50fde3f-4022-370b-b28f-c1dd61f95d08 | -6.09275 | -43.99321 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 05bc61a5-8c74-337b-9b6f-3c935cddc2d8 | -2.07993 | -46.5729 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 562.0 |
| 8c0450d3-a61f-3e04-ad19-196d76674002 | -2.61476 | -52.0424 | 2026-10-08 16:20:00 | NPP-375 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5a3a6503-e4f8-3b85-ad00-e41c6ecb8545 | -7.06475 | -40.9453 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 63c3038f-ca86-3fe8-ba55-aa8b14acf8f7 | -3.07769 | -53.96486 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f45b1b0f-f79c-36f9-8abe-41f78d0e2502 | -6.15479 | -47.93397 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5b5e2bc7-28ff-356e-a431-81ec6c0207f0 | -5.10398 | -46.21939 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dbe3f4d4-4f3c-331d-8fe5-4e4661fd1923 | -4.84215 | -44.09351 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d252828-d340-3331-8cfd-3c6c7fed9954 | -2.98735 | -43.28857 | 2026-10-08 16:20:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a4b96651-7851-3d70-87ad-82146fa7ec83 | -1.37624 | -48.04805 | 2026-10-08 16:20:00 | NPP-375 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bcaf6567-7c8d-3de8-8e56-759c8f6ff1df | -6.94915 | -44.41326 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a1ef0c43-0534-37a5-a6bd-d46fd89f03b8 | -5.74937 | -42.05843 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e0a81c72-8934-3e0a-a9b2-52534a638620 | -8.20358 | -46.36581 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 7f7043c3-3b83-3423-9b10-918ec76f3ecd | -6.82227 | -39.30983 | 2026-10-08 16:20:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 223b1c6c-2c62-3df6-bc43-f749cfbad9f3 | -7.25675 | -39.40797 | 2026-10-08 16:20:00 | NPP-375 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1f36ab90-8daa-3fa5-82e7-225025d73536 | -3.02154 | -43.34348 | 2026-10-08 16:20:00 | NPP-375 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d97c7a7a-8401-3ff2-923e-ea4fb9609273 | -5.77628 | -45.38859 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a4adfdd2-013e-3363-adf6-dc0c7398bb76 | -7.14463 | -45.00893 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d99636c-7bcc-3b80-ba62-9abc584be937 | -1.79962 | -47.84878 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1304543a-9943-30e2-a523-4f0ad459c108 | -6.8221 | -39.55143 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| b13d07c6-54f4-3e83-b109-569d2b7481b4 | -6.97389 | -45.1347 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8f7c1528-2310-3bae-9124-baad38d1b011 | -3.80591 | -40.45388 | 2026-10-08 16:20:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dc82082d-12e3-3deb-99b1-3a9773919e15 | -2.11547 | -46.39169 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 93c828e5-999c-35aa-b847-ef8a6e6e5431 | -3.30249 | -54.02137 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4ea18f5c-6116-33aa-b8e0-8d330273ed65 | -7.21169 | -44.27908 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4c1f49ad-d3ab-380a-9c30-7a8efb1ecbc4 | -3.55877 | -44.56259 | 2026-10-08 16:20:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |


[Clique aqui para ver as próximas entradas](README296.md)
