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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b42711d-eeeb-3a0d-b17b-abaf2d405300 | -4.60136 | -43.31546 | 2025-08-14 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85df8c47-80e5-3877-aaa3-e80694a8f8a9 | -2.89813 | -40.44196 | 2025-08-14 03:28:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d16231a0-12ed-33e9-a0ee-b950df80b61c | -3.82054 | -41.56954 | 2025-08-14 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e0cc89f-5618-3ca0-8e6e-74c92ee6bfed | -5.78876 | -43.61134 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afc7411b-e5ba-390f-b27d-0a9e8bee89ed | -3.67131 | -39.58223 | 2025-08-14 03:28:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ed7df720-c039-3278-8650-e0346722f9fb | -2.90404 | -40.43946 | 2025-08-14 03:28:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c25c2dcd-4958-3c76-ae2a-9bb388ff06bd | -4.17327 | -42.45598 | 2025-08-14 03:28:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 184df412-ec8d-309f-b5c4-fcdd74a6099e | -7.39188 | -39.6842 | 2025-08-14 03:28:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 07a5f93b-d1c3-363b-87bc-af87964a2aec | -5.1551 | -39.50861 | 2025-08-14 03:28:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8eb68278-2893-37a5-ba84-194fff54824a | -2.90018 | -40.44229 | 2025-08-14 03:28:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5053a0ea-717e-31a1-af96-bebce8828c8a | -3.82187 | -41.56183 | 2025-08-14 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c49bfaa9-6ff9-3f20-b33f-c0ecf14fefdb | -4.72261 | -38.39347 | 2025-08-14 03:28:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53af986e-c10e-3af9-bcd1-05253b7a568a | -5.98213 | -44.15639 | 2025-08-14 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c80cbf3c-2f0d-3c48-8b59-4d71397665f5 | -5.15599 | -39.50342 | 2025-08-14 03:28:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 43014824-731a-32d1-8311-c9724e6756ea | -3.81753 | -41.55321 | 2025-08-14 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 662a2afe-74e8-3ebf-8bb6-75428278d69d | -5.77859 | -43.61017 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee40612-ba47-3c92-9e53-413c6167f952 | -2.90072 | -40.43895 | 2025-08-14 03:28:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c9c835b4-403c-36cb-80c2-6e13be75bfce | -5.79641 | -43.61871 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1da04d4b-e90d-36f8-966e-aa2521502ff6 | -5.78254 | -43.61011 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef50e9a7-cb1a-3406-a01b-ffcf7f986a4a | -5.47226 | -36.7888 | 2025-08-14 03:28:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 21.5 |
| faff2f0c-6535-3aeb-b5b3-67ae67191bf2 | -5.79018 | -43.61749 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e0899da-9dc3-3ea0-aace-7b9dc9528a23 | -5.87722 | -43.92705 | 2025-08-14 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2995339b-664a-3fd1-8340-0344fa0732ba | -3.81688 | -41.55702 | 2025-08-14 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 20951cc6-723f-31c8-a2a8-ce005d8b5060 | -6.61559 | -43.88531 | 2025-08-14 03:28:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e9b9f083-5815-3318-aac2-7f01dee4e529 | -5.37445 | -36.84786 | 2025-08-14 03:28:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 74551933-c463-3d16-9d48-eb891f7a0241 | -3.67227 | -39.57642 | 2025-08-14 03:28:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3944a3f-961e-37f9-a70e-e7e27f05b6da | -5.37846 | -36.84852 | 2025-08-14 03:28:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66fbe5fc-f377-3a50-936f-6d987b1e1380 | -6.61248 | -43.8831 | 2025-08-14 03:28:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 87bf497d-6f23-3d4b-b0d6-ed7dcb9e3103 | -4.59511 | -43.31441 | 2025-08-14 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b1ee950-3034-3804-9b46-2ed920e323a6 | -7.07062 | -39.47213 | 2025-08-14 03:28:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9dc49f57-2329-3db2-9c94-71d66bafe88c | -5.68662 | -43.65476 | 2025-08-14 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6255e22b-6439-3e24-9f69-475638cf928d | -6.18405 | -43.31655 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d61ae2b0-1934-33f4-a498-d2192b03ea47 | -6.19017 | -43.3175 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e0eb31c-832a-3677-a91d-09d999650816 | -5.79409 | -43.61741 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 416f1dca-37c5-34cf-aa97-ed8db7d7a560 | -3.82121 | -41.56568 | 2025-08-14 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8eba9abf-74c3-3a18-808b-819de285e3ee | -5.97668 | -44.14979 | 2025-08-14 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41f35d5f-1fd5-317c-a052-6e10634f80ab | -6.17802 | -43.31221 | 2025-08-14 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 103fe58a-1438-3503-84c7-87eb0236af2e | -4.17404 | -42.45159 | 2025-08-14 03:28:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7f785fe-ade2-3f81-bcf9-6dfa4a731133 | -2.90347 | -40.44282 | 2025-08-14 03:28:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 59907e27-2499-3332-b399-d0ab2ee2955b | -5.79103 | -43.6127 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce1e910f-390d-3f02-92a1-29d320522342 | -6.18416 | -43.31303 | 2025-08-14 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a48891d-6266-31d3-b0ca-b2c591414bbd | -5.37386 | -36.85135 | 2025-08-14 03:28:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c6f0726a-d901-3f19-a8a0-0f67c9e51ba1 | -5.78565 | -43.60666 | 2025-08-14 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64ffd84d-263c-3b5d-ae3b-21f758f3b9b0 | -5.47625 | -36.78951 | 2025-08-14 03:28:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aa34284a-aa70-36aa-b0b7-1e76617f8d47 | -6.61158 | -43.88808 | 2025-08-14 03:28:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b2c4d2de-0670-3609-89c4-351eb6e9cf93 | -4.93243 | -37.38918 | 2025-08-14 03:28:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2274de35-5ce8-3bf3-9cc5-d678c0a52bac | -4.17096 | -42.45182 | 2025-08-14 03:28:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a10b1043-be3e-3ed2-8b87-a17c4ad26cbb | -6.18493 | -43.31177 | 2025-08-14 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adb0fc9f-135f-30ca-971e-89bf32d5d428 | -5.98313 | -44.15086 | 2025-08-14 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01b17155-7ba5-3a98-8f6b-21bf7e49b9bc | -2.8987 | -40.43863 | 2025-08-14 03:28:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0edd8d23-3a56-3303-bbdb-dd07b16964e3 | -6.0991 | -59.9459 | 2025-08-14 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1786d580-99a8-3da3-9d38-e37da7d1906f | -6.8771 | -59.147 | 2025-08-14 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 7362ec67-13c7-3d5f-99f7-eaaa7d1c461d | -9.1336 | -59.6588 | 2025-08-14 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 68908fd7-c833-3680-ab75-3eec1ad09dc8 | -6.877 | -59.1663 | 2025-08-14 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 217174b9-ddc1-33e2-94e2-1d286b4286c9 | -6.914 | -59.1455 | 2025-08-14 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 1d41a3a1-50d6-3b36-b137-4c3f1b40a34b | -7.8775 | -61.8063 | 2025-08-14 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 8a3e6db8-fa81-3d16-93a2-3ed97910948a | -9.553 | -40.3503 | 2025-08-14 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.6 |
| ef61a4af-75df-320b-90de-e0cddc5546ba | -6.0807 | -59.9465 | 2025-08-14 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3a29bfae-078c-3f1c-8b9a-d79cbde5e992 | -9.1522 | -59.6578 | 2025-08-14 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3ee2fd7a-d829-33eb-9447-1e82d6638fdd | -7.8774 | -61.8253 | 2025-08-14 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cc97bf3c-615e-36cb-b5ab-5f6cc21aa372 | -16.3153 | -52.9201 | 2025-08-14 03:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f7e56627-96e9-33d9-93f7-d818ca446b7b | -6.8956 | -59.1462 | 2025-08-14 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 0f2903d0-c2ed-3547-aa47-55ed0ef9a226 | -6.8955 | -59.1655 | 2025-08-14 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 1a47b8cf-bc75-35cb-a5d9-667ff5cbc946 | -9.5721 | -40.3475 | 2025-08-14 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 44191cc2-f45d-3d55-beea-4488aa39b211 | -8.51875 | -43.29745 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 35318b45-3a95-31a2-a7cb-a900f3c4ccf9 | -11.80593 | -44.27014 | 2025-08-14 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51bc0993-8bdc-353d-8d9e-ac9215975bcf | -8.73811 | -44.02385 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce60d5c7-92c6-315a-ab0d-9a4ed3e9c080 | -8.51789 | -43.32722 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 646cc68b-fe42-3ec8-a8c4-a3034debb4e1 | -6.94591 | -44.55437 | 2025-08-14 03:30:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c69bd29a-79a4-3ce5-aa56-dce5f54ff3f1 | -10.53142 | -42.55133 | 2025-08-14 03:30:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ef91d245-d470-3357-9873-9853f9f4cdf2 | -8.52305 | -43.30699 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1861a68d-5bcd-3127-805e-480f3eb50273 | -11.35898 | -41.39484 | 2025-08-14 03:30:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b16c2962-d64d-31d8-9f9e-8844b4e36d05 | -8.73723 | -44.02863 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1d530fa-7c6d-3962-97b7-befb2e80c4b4 | -8.52503 | -43.32922 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 973c8d81-539c-35e6-abdc-045d65cd4c2b | -9.55843 | -40.35036 | 2025-08-14 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.2 |
| fd83cda6-61ca-312f-b1a7-d4425b9aeb29 | -6.94395 | -44.56484 | 2025-08-14 03:30:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 974acdb0-f90d-3661-ae26-1f11c8e35b72 | -8.51995 | -43.32387 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 95a630f6-d740-39ae-a01f-b0aaae86c262 | -8.73862 | -44.02098 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c143f50-cb59-357f-9ca4-62bbb9851b73 | -12.31404 | -46.05127 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4d5db3d-baac-3160-bcf1-9f7c8f6dd799 | -6.94494 | -44.55959 | 2025-08-14 03:30:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9b7f2051-e05f-3837-81f9-d3322731c28f | -8.51721 | -43.30585 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2346106d-0939-3a87-a39a-fcac68888580 | -8.52192 | -43.30619 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a78cad85-9493-3976-bbb1-705b7332b77b | -8.74047 | -44.01134 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e4dc6cb-56bd-3b88-a171-ce943120f503 | -8.74337 | -44.02957 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7851f26f-6ee2-3a0d-93d0-f2956b084085 | -10.74539 | -37.51646 | 2025-08-14 03:30:00 | NOAA-20 | CAMPO DO BRITO | SERGIPE | Brasil | 2801009 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e761c57-ca8e-3051-b674-93cdd1959918 | -11.75928 | -43.38242 | 2025-08-14 03:30:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 892a6868-2bb5-354b-8037-6e5d031f3087 | -6.95341 | -44.55014 | 2025-08-14 03:30:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 675fdc2c-9cdd-3452-9ef8-5b5862c366fe | -8.7377 | -44.02576 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be844648-338e-3ebc-8206-54756dba04c7 | -8.52072 | -43.31965 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 013b9327-d8fa-34c0-a288-4eca734631bf | -12.3129 | -46.05687 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e420df22-e767-3089-bcbd-ae31a8438838 | -8.51798 | -43.30165 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4f445a38-6f69-384c-8662-040dab5af4e2 | -8.51917 | -43.32809 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| b0126807-5ac4-3c5a-bbfe-c3bcc7d7ac19 | -6.94685 | -44.54935 | 2025-08-14 03:30:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a3998b50-7de6-398a-a326-a3bb8afd0d24 | -8.51951 | -43.31881 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e1e8c271-e2cb-3ae7-91af-f3bd859e48d4 | -8.74383 | -44.02673 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| edcfdfcd-d4e5-3d66-bb94-5b34c299c2a3 | -9.04868 | -45.08639 | 2025-08-14 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6af8fed-37d2-3b0c-9595-73a97560afd9 | -8.5258 | -43.32499 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a3df763e-5ab9-3069-993e-2aeff27a5be2 | -8.74079 | -44.00938 | 2025-08-14 03:30:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 689181b2-73fa-389a-ab26-326438fe4d87 | -12.3132 | -46.05376 | 2025-08-14 03:30:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a20a08e-04d3-300e-a4ac-7ba15d58f7ee | -8.52273 | -43.30199 | 2025-08-14 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README10.md)
