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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2b96686-e330-3bbe-80e6-6744b7776b51 | -8.97071 | -61.51484 | 2025-07-19 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a9f9cc3-8bd5-3646-a8cc-106b9da1c842 | -9.8127 | -47.7361 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0168a73a-e896-32ca-8959-3e18d566ddff | -10.90031 | -56.07961 | 2025-07-19 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b9a1649-7341-398c-92b5-c960e7d367ad | -8.01616 | -43.67743 | 2025-07-19 04:57:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b42f0011-6e14-30f0-8408-533e82271067 | -12.36976 | -50.32971 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c49fb369-d6f2-3a7f-8d95-5e3eaf2a8c9a | -7.57897 | -49.40368 | 2025-07-19 04:57:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 763e475b-ca45-3818-be89-c215f630177e | -7.17129 | -44.09824 | 2025-07-19 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da7f5ae1-9dea-3fdc-b146-349f9c8b1d5a | -10.09106 | -47.23852 | 2025-07-19 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51901686-c706-3bb0-9f39-ef9dee842c6a | -8.26223 | -46.0868 | 2025-07-19 04:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bb20553-0ee4-37e0-be1a-d2d1df16e959 | -11.45892 | -48.15939 | 2025-07-19 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b90a45f3-03ed-3f9c-b515-2553a686e9ec | -6.75045 | -45.51613 | 2025-07-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64ad0d2f-5cc5-36c5-a2c9-75082c87fbdd | -13.59995 | -45.64354 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8dbe2e7-6554-3264-9645-90a7f8e17b4a | -13.61376 | -45.64097 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c543cca2-6b24-321f-a0a8-199e2c043cb5 | -13.05085 | -49.17382 | 2025-07-19 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5a554bad-9eb9-3966-841b-4832c862a453 | -10.72256 | -46.78371 | 2025-07-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f782d746-1ad5-31a0-844c-e54038e3c39e | -12.68159 | -46.83314 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 968d4cca-293e-3a41-9950-254f9c315276 | -7.5795 | -49.40003 | 2025-07-19 04:57:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fec9214-2304-3cfe-b251-336ff19a6f8c | -7.48865 | -43.9387 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94aabf16-b134-3429-9a93-52374199c567 | -12.57861 | -56.96816 | 2025-07-19 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5452912a-6dba-3fc1-99f0-8e623e623d86 | -10.62007 | -44.76485 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| efcf339e-9457-312b-b060-db2e7d3a6038 | -11.9687 | -45.47071 | 2025-07-19 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d386c98-6252-33da-b406-914c156a8dc0 | -11.96008 | -47.01759 | 2025-07-19 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa6d5c3d-face-33fc-9954-486e3a9a5fe1 | -11.73211 | -48.52208 | 2025-07-19 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71db1b55-a1f4-3203-a87c-b321c0e82606 | -7.48273 | -43.93814 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79dda1c6-6e7a-3074-85b1-aa27de82c5f3 | -7.48505 | -47.49892 | 2025-07-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ffe450fc-18b1-375f-93c8-f61c2c7c3291 | -12.97448 | -46.92414 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8d53053-12d2-355a-8dad-d5c76f186f91 | -11.46429 | -48.15493 | 2025-07-19 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c63b4a8d-a5ab-3d5d-afcb-f10595f147ca | -12.49841 | -57.21692 | 2025-07-19 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cd8dc96-0c52-30c9-9323-ed5a65f63799 | -8.97622 | -49.85012 | 2025-07-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc745189-fa8b-3bf7-bb4d-ea6133baeae2 | -9.01533 | -59.54217 | 2025-07-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9adc4b83-18e1-31b9-b13d-84a6d7042447 | -7.71119 | -47.29019 | 2025-07-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 071d2530-dbe8-3f30-b53e-abffdf1d864c | -10.71724 | -49.48308 | 2025-07-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d382d64-318c-372f-a2ea-f55dca681988 | -9.94929 | -48.16471 | 2025-07-19 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36e68af2-eda3-3312-9054-4ad4d7065f79 | -11.484 | -47.32429 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c5b88b97-1949-3964-a745-3eb725287078 | -7.4893 | -63.82366 | 2025-07-19 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7cf9402-2336-3637-8792-13b8610f00cf | -13.05533 | -49.17447 | 2025-07-19 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d11fd1b6-cc6d-31d8-a86e-070a9b823caa | -8.97029 | -61.50792 | 2025-07-19 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f045d3d2-ff01-3ec0-a368-6050838a633f | -11.73327 | -48.19273 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| dfa0416a-d8ae-3a50-9986-bd7b6e21af7b | -11.82774 | -48.21862 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d84ac0c-cabf-332c-bcd2-454d56a76a96 | -9.60478 | -43.86303 | 2025-07-19 04:57:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8cf33ef6-1689-378e-ac68-a243a08fc106 | -9.61384 | -49.02313 | 2025-07-19 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 436b73af-b111-321a-b81f-f71792155583 | -11.82304 | -48.21799 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffa2747a-6521-3108-94c9-62b744f12903 | -10.29684 | -60.54346 | 2025-07-19 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8994d4d5-6563-3d42-8c6c-cbc2cdde1228 | -14.19507 | -45.33905 | 2025-07-19 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fe25ad9-a51f-35a8-877c-8944ef061793 | -6.75662 | -45.51032 | 2025-07-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dabce90-52dd-317c-a531-dac19b5ca50d | -9.69181 | -56.11155 | 2025-07-19 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11878ea6-f521-30a5-ab51-8eb7afe9c404 | -11.72858 | -48.19205 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| e474049e-4fa4-3cf4-9a91-f4a402b15ce9 | -13.60189 | -45.64328 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c9c012b-685e-36a1-a0be-4535606db73e | -12.3742 | -50.33428 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a06793e5-1b64-3339-8054-62d868206472 | -11.47311 | -47.32252 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6165d39-c3b6-3615-92fe-4c1f8f0aec6d | -10.68162 | -56.54789 | 2025-07-19 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e509cd9-5008-3c55-97d7-16aae36e70d0 | -10.81675 | -49.28989 | 2025-07-19 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf2675e0-eb22-34ad-9b70-816f735e7a48 | -12.42927 | -45.36955 | 2025-07-19 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12f6d8a6-0a97-3708-9720-77d2bb630fb3 | -8.96585 | -61.50713 | 2025-07-19 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d9d8da-9aa6-35bb-b9d6-13b581e27987 | -8.25881 | -46.07314 | 2025-07-19 04:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2c79aee-4a2f-316e-96fe-438aef81a6e0 | -9.9539 | -48.16516 | 2025-07-19 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aeab2c4-29ea-3479-bff4-e2d3758b8596 | -10.36651 | -57.50563 | 2025-07-19 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9af874fa-3c4f-37a0-af2b-eebb637d7234 | -13.60805 | -45.64017 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d1bda22-256e-3773-8429-5e0ed8e7d8c2 | -7.70718 | -47.28457 | 2025-07-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80e38eeb-450f-31d3-be3e-a4e7d65ff574 | -9.60537 | -43.85829 | 2025-07-19 04:57:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8aec7349-f950-33d7-a031-cfaf732b8889 | -10.29277 | -60.54271 | 2025-07-19 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4d6d755-1f88-3052-acc7-e9346dd47c6d | -11.56035 | -47.08393 | 2025-07-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cf5a3e8-c27e-3402-bf9e-cb7ccb97cdf4 | -7.17705 | -44.09935 | 2025-07-19 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eae9e084-b19f-3808-87f8-dc1e97377299 | -7.11455 | -44.38547 | 2025-07-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4758e488-1e1e-35c1-a07f-3812186c7321 | -11.48897 | -47.32492 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c45b5324-14b6-3c0f-b1ed-8e2ad5424ac5 | -12.36136 | -50.33627 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 271d4dde-99df-3492-9253-e227e9cae3e8 | -10.10645 | -58.22066 | 2025-07-19 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82fa760a-0fab-3632-83d7-584c8b375830 | -11.72924 | -48.18696 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 01e67502-cc69-3b7d-b1f8-361805f58d82 | -13.60234 | -45.63935 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbbaf34b-066f-38ce-8d50-4b3439538100 | -7.48818 | -47.50143 | 2025-07-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06ef845c-87d7-3750-aeef-2e366908e54f | -10.63732 | -44.76532 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07c6426c-f237-3d1b-a336-013852eed7b2 | -12.37009 | -50.33369 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eeed72e-fddd-3bdf-b971-cc4f70a2e59e | -11.82839 | -48.21368 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8730541b-37d4-3ab5-b38d-55ec5ecfce21 | -10.05838 | -59.09962 | 2025-07-19 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb02eb59-5b30-3383-8f77-f41cb4c0d031 | -9.69238 | -56.108 | 2025-07-19 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f4b0db4-cc93-31b8-a86b-fa03cc7f1f85 | -12.37389 | -45.73336 | 2025-07-19 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da6ab81e-9321-3148-af00-87763eff58f1 | -10.71779 | -49.47911 | 2025-07-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6752a7c0-855e-36e5-8ee7-f38ee2994ff3 | -10.6721 | -49.68463 | 2025-07-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7521779c-73d3-3138-b467-6e7333540487 | -12.06632 | -47.34924 | 2025-07-19 04:57:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37bd0218-1201-362d-b032-faa8b60b53ea | -11.96482 | -47.0213 | 2025-07-19 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f67147ca-bee5-3834-b6e9-b9f3923599fe | -11.56385 | -47.09678 | 2025-07-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 573ecf05-4ce8-38a2-9965-4e961f9c33a3 | -6.78587 | -58.63264 | 2025-07-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7244c18-2427-32bd-85b6-0d1bf385202f | -10.9269 | -55.00939 | 2025-07-19 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02df032e-18ab-36e9-a1db-acc4fc125bdf | -9.00562 | -48.72094 | 2025-07-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8dd559a-9eb8-3337-81da-7358b8184daa | -10.87926 | -47.15076 | 2025-07-19 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73ce4238-dbad-32ab-9d31-7ceb306349a5 | -9.81819 | -47.74252 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 335903c6-350c-3e72-95b1-40a451cd9c28 | -10.62516 | -44.76797 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e1e72a6b-c9a6-364f-ab5b-62f2909e816c | -6.55384 | -56.24701 | 2025-07-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd0ff141-f2e0-314e-9e26-718387534104 | -7.27822 | -50.33173 | 2025-07-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64d4d0fb-82d0-30ab-99c7-5c7bea3209f1 | -11.95933 | -47.02367 | 2025-07-19 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df894eed-9213-35fb-bf93-df35bd15fc72 | -8.53039 | -47.84234 | 2025-07-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43bbf100-73dd-3518-add0-73102355528d | -11.73147 | -48.52686 | 2025-07-19 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baae363b-f652-3a9d-a570-f4c1052738f2 | -11.48327 | -47.3301 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90d844a9-72a0-3125-986d-fa7ac48e62c9 | -12.90308 | -48.9205 | 2025-07-19 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8da8436-4378-3e29-9f89-cd305beba467 | -8.53433 | -47.84781 | 2025-07-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1add19bd-9818-3bea-a009-9f8d00b02d3e | -6.88971 | -45.24652 | 2025-07-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a153dec3-1351-364d-99e3-87263278ec48 | -7.58071 | -57.66513 | 2025-07-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76af40d7-fc3d-3be6-9f26-2dcbd2a7d1a5 | -10.88502 | -47.14547 | 2025-07-19 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e870439c-5125-36d0-9a01-a4ccff5e0809 | -8.52975 | -47.84708 | 2025-07-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70eb6d1c-f23c-348e-ab14-3f197ed0ef2f | -7.48331 | -43.93377 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README27.md)
