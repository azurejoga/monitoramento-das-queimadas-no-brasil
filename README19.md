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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82e0bd32-5f3e-3180-a5fe-f17e5da272bd | -11.14609 | -53.9295 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2964d16-c69b-3d43-9123-dd9ec79bce75 | -9.48986 | -56.09228 | 2025-06-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b8437bbd-1fbc-3f16-a879-dcf7d687a861 | -9.42741 | -44.72885 | 2025-06-18 04:38:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 241861d9-edb5-3102-843d-955c12721d69 | -6.03842 | -44.04782 | 2025-06-18 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 29539fde-48e3-311e-ba86-e30b97effc9d | -9.40628 | -48.41831 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdb77d9a-84d4-349b-90c2-cd4233995791 | -10.87764 | -54.31502 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9330f93-b6ca-3137-aa54-4227d12cbd66 | -9.40967 | -48.41884 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3082880b-0d85-3ae5-befa-0ad06cd950e6 | -5.1205 | -56.11708 | 2025-06-18 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e47090bb-794c-3ff8-98d6-51e1bc696e8f | -7.72172 | -55.13926 | 2025-06-18 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40a5cb24-69af-35fe-8481-2b75a31dd731 | -10.50888 | -46.4343 | 2025-06-18 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 713325ed-bc6c-3e4f-8260-661190a70d3a | -8.10726 | -45.54621 | 2025-06-18 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3ebd118-9846-34dd-ab17-05e5bc5b91da | -10.8739 | -54.31436 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1db23aa3-be3e-3274-a70f-0ac789e9ec03 | -8.72391 | -48.00094 | 2025-06-18 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e2325d1-4378-3e8d-bdf5-bf9a79b1ecc6 | -9.86421 | -47.88958 | 2025-06-18 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b37c0738-f9dc-3f0f-98c1-1cd82b840761 | -10.65738 | -49.36225 | 2025-06-18 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cc020f6a-cc79-364e-9e3b-a2a52bbc9aeb | -8.88252 | -48.52224 | 2025-06-18 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33b2870d-5600-3608-88b7-de08688be83b | -11.14535 | -53.93385 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b42ced6e-b55b-3b18-99b2-3fd08db66a57 | -11.13656 | -53.9413 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 25819bf2-834d-38f4-9b2f-bc5a7da88267 | -10.35882 | -57.23089 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 458bb710-2499-3e84-8622-9fe9e695fdfb | -8.00764 | -49.99718 | 2025-06-18 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c293790d-ff4e-336d-9e09-fc6d3b798687 | -8.72378 | -49.02445 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5389f60c-425b-3785-b854-fb0887995891 | -8.51623 | -54.7686 | 2025-06-18 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba4a5fcb-be35-3597-b6dc-0b97d42bfd39 | -6.11973 | -42.53402 | 2025-06-18 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c95c3a3b-1976-3e76-b1b9-ce7bcf7b5b55 | -11.66266 | -44.61815 | 2025-06-18 04:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97135ad6-eb07-34ec-9de0-0fed410d11ad | -11.1382 | -53.9223 | 2025-06-18 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 29d0e6a8-e1f2-3c1a-89fb-b4cc335ce6d2 | -11.1379 | -53.9429 | 2025-06-18 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 3ff46768-fcd7-30ad-bf07-db354bf13cd7 | -15.56701 | -55.65288 | 2025-06-18 04:40:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0ec44af-28f8-3e63-b55d-c139dbdc9e5a | -13.72204 | -58.68451 | 2025-06-18 04:40:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dcc984c-5081-34cd-a2c5-63af5aadb483 | -19.47718 | -49.28925 | 2025-06-18 04:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2ee80a0-0b91-32a0-aa2d-e8d304d99d3f | -12.52568 | -57.77195 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4708119d-aa9c-3ee2-9d60-315c506062ca | -15.40985 | -47.83135 | 2025-06-18 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42a32474-e6ce-349a-b11b-6cbc909b2147 | -12.27495 | -57.27306 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a250892f-fcd9-3a97-bedd-c833efaa6215 | -12.52592 | -57.21481 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab659a4c-0fe8-3cc3-aac7-88d462ab5e67 | -10.29325 | -60.53545 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab818f03-b86e-30d3-92ee-c1c315b9611b | -12.53398 | -57.73317 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0e8308c-b476-3966-aeef-0459ba31fa08 | -12.32429 | -52.47276 | 2025-06-18 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54ee2888-5633-3ca8-9c3e-5575f1a2244a | -10.65969 | -59.29166 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0973ac3d-b9d7-321a-9b8c-fe46e8b8309b | -16.30943 | -58.24925 | 2025-06-18 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a9cfaf43-2199-3d8f-ab75-cf9a1b190f04 | -14.19404 | -45.51126 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb6ed726-e4b5-321f-9e9a-4eaabf0a7433 | -13.96065 | -56.79387 | 2025-06-18 04:40:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 647a3102-a9fa-31e1-81b6-67f0cc7b03de | -17.69092 | -46.81091 | 2025-06-18 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b488c39f-28b5-32e5-b750-05b66c31f0ac | -16.68105 | -43.8857 | 2025-06-18 04:40:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 653d7ea3-774f-35b5-a069-02a583d19d35 | -11.88544 | -54.66946 | 2025-06-18 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ac96729-c5e1-38bb-8974-fa354dd3b4c2 | -12.53569 | -57.72405 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04275c81-d9d2-3d31-b467-6e202ff15280 | -14.06929 | -53.38288 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7da9d1a9-5bd3-3c31-959a-40c47f404430 | -12.42599 | -54.86981 | 2025-06-18 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cafc158-98bc-31eb-8ac0-358dbe3a1f28 | -13.79683 | -54.30104 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b22d9848-8879-3697-8794-8eed0bfb40cf | -12.5829 | -56.97721 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7063da21-1b3b-373a-9fce-4576c23d517d | -10.92695 | -56.84192 | 2025-06-18 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 762cdec1-4aa5-3459-8a71-779fe7c31698 | -14.02259 | -54.49227 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa58678f-a2ad-3f2e-b6f1-fb494c901675 | -14.84202 | -59.83476 | 2025-06-18 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 160d4faf-b3e5-3a78-8fb6-596f547b31c4 | -13.94271 | -54.49687 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41fe91de-137b-32b8-b67a-946e17b1cd79 | -12.49587 | -55.73816 | 2025-06-18 04:40:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ca86184d-9f5a-3570-a4b0-6bdfb4632fc5 | -14.67391 | -53.12771 | 2025-06-18 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f56fee78-8312-3bf7-b401-ad5a7021004e | -15.37999 | -47.69353 | 2025-06-18 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc1443a1-044f-37b5-bea5-96d8f6319fdc | -12.50972 | -58.35474 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2307b501-a074-3511-89eb-ff1c646c3706 | -15.99353 | -49.82035 | 2025-06-18 04:40:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de45819b-113e-32dc-bb9d-5bea86d4daed | -14.66988 | -53.13091 | 2025-06-18 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 40c270a5-e047-38d9-8b0c-131296665d58 | -14.02298 | -55.1199 | 2025-06-18 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ecf58e1-8085-31d0-ae34-8e63dd4dbe7b | -12.49892 | -55.74408 | 2025-06-18 04:40:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2e54b10f-f3a3-324d-b57d-f39aeb68b222 | -12.52156 | -57.21399 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e312eca4-256c-3c15-a085-8a4d8fcfddd2 | -12.71891 | -54.97303 | 2025-06-18 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eced9fd-8308-3eda-b7ac-e171f1fd4523 | -12.5312 | -57.72312 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98c81f46-d163-3761-8a1b-84ca6f2f966e | -12.208 | -49.64863 | 2025-06-18 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95e3deea-7d6d-3e2c-914b-fb0eb7bfee55 | -18.38124 | -44.5054 | 2025-06-18 04:40:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae3ce84f-4435-3cf1-b072-98d4fc2f133a | -11.95986 | -58.74092 | 2025-06-18 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d882185-7e84-3a07-ab95-dc4ecc893231 | -11.65069 | -54.13938 | 2025-06-18 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62de7283-624b-3abb-89f2-9c123c0e9522 | -12.57787 | -56.98049 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ca281c2-442b-3302-8513-181e737cf7f4 | -16.35687 | -54.55442 | 2025-06-18 04:40:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 703bdd44-e767-3d7e-af4d-8a8b742b5bb5 | -11.64628 | -54.14305 | 2025-06-18 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f0b810a-5e64-3555-8bca-2b90358b9f03 | -13.29153 | -57.07385 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36d1d298-9c0b-36af-b3a9-f87dcedd7aa4 | -14.43597 | -48.9073 | 2025-06-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f8290791-7607-35b9-9820-cef778dfba46 | -14.67453 | -53.12397 | 2025-06-18 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bb2596a-eb86-3228-b18b-ed5bd5fcd24b | -10.93056 | -56.84708 | 2025-06-18 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9d3289b-fdd2-368f-8943-960f5bb51e9b | -12.27568 | -57.2718 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54259e93-cf56-301b-ac05-8c2cbb75b536 | -10.27866 | -60.53644 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ba19c67-59c2-36d7-af42-8726225ca452 | -12.65767 | -54.11071 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 390b1cea-ff34-3a9e-8205-f6bc0ae77b8c | -10.27015 | -60.55075 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b359814-0164-3aed-8576-5ab7543e7faf | -11.95702 | -58.7291 | 2025-06-18 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2dbeb947-8cfd-3e6b-aaa8-47c0e73c886f | -16.71967 | -49.33183 | 2025-06-18 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 518745a0-0efa-38f9-a790-665d5ff63ef4 | -15.07673 | -48.94469 | 2025-06-18 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca73521c-2a2b-3bec-bdb5-39926fa21075 | -14.07274 | -53.38349 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e3e1b2b-0c2e-338f-b0ac-a632c3869671 | -12.64537 | -54.11734 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 130684f9-6909-390d-a098-655fc3acb564 | -18.53113 | -48.96524 | 2025-06-18 04:40:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b1cc0ed-7b27-3afb-828c-2460745c2de7 | -10.2741 | -60.54362 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b28f95f-2fc9-3eec-890d-f945dbb0afd7 | -12.34138 | -49.30503 | 2025-06-18 04:40:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64a2cb27-658d-35e3-a5d6-670f632c0b6d | -14.20188 | -45.51637 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad697f2e-d6f2-3b54-a799-7aab6f63978c | -19.0024 | -52.08364 | 2025-06-18 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec09f584-546f-3364-bc40-b5d1f9074267 | -18.52752 | -48.96472 | 2025-06-18 04:40:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d2a7f64-4935-3301-a489-9457f343e6ae | -14.02513 | -55.12973 | 2025-06-18 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f24fe85d-55fc-366f-a2f9-00b9163d7afb | -13.7144 | -57.47852 | 2025-06-18 04:40:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87883c84-cb30-3548-ac5d-d27d7ccbb595 | -14.02593 | -55.12515 | 2025-06-18 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abf894d8-748c-3a90-bd16-4a18096f7daa | -12.50594 | -58.35582 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e792a71-4af1-337f-a267-0fdfadef293c | -10.93208 | -56.8384 | 2025-06-18 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d8e0519-857f-3b7a-9405-31af0e5c5dcf | -12.52485 | -57.77658 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce483bea-e1c9-37c7-85f6-b6ee36c285eb | -11.91686 | -55.43376 | 2025-06-18 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a24c5b3d-aa3f-3a1c-b5c6-4718cbc8273e | -14.06715 | -53.37455 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6f2bfab2-be0c-3344-a1b4-667b5a61276a | -12.58215 | -56.98132 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33852fd1-6823-3fbb-94d4-ec615d62b5ec | -12.20744 | -49.65223 | 2025-06-18 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90d00597-ab6b-3c30-a625-02f5f158d5a0 | -16.29482 | -52.93456 | 2025-06-18 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README20.md)
