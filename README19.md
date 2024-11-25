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
| 7cde9cf4-facf-3152-8d32-c127182ef4a9 | -5.61832 | -43.47641 | 2024-11-25 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf1b03ce-351e-328e-b59a-ca459d0e36b3 | -2.63424 | -46.20818 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93caa2d5-5cd0-3518-9226-5c6da6590916 | -1.18737 | -53.88258 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79d11488-5fe0-3ece-964f-c51912cbb884 | -4.37163 | -48.50225 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e81ac1f5-7118-3d0d-b14f-e9bfd49bf746 | -2.63091 | -46.20767 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e159f228-d4a0-3377-b71f-160eb8dd2e4d | -2.56597 | -46.56154 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59cab758-70f3-3b98-b072-3908786c5fe4 | -4.95016 | -45.32847 | 2024-11-25 04:33:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6da0f431-ed28-34c5-a333-cd3a0a7d75b6 | -3.8296 | -47.46869 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb4646dc-311c-364e-aaf4-11b4d7d028d1 | -2.68915 | -46.16264 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e75115e-5e27-31f8-9201-14cdd5429ebb | -3.24003 | -54.22535 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d170be-fa5e-3a26-a0bd-ffa784d6b73d | -3.36708 | -46.65787 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d29a770a-edbb-31de-8049-9f86071b222b | -1.44651 | -53.40101 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9ee7db3-1f17-36e0-8b11-092268d3321c | -1.62882 | -52.44629 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98d8ab98-a610-3979-b1f3-31c4660a905d | -4.20655 | -48.12371 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27d59f72-ac9c-38af-baaf-06632793d29d | -2.55022 | -46.5521 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6b725cb-fb8c-357d-a889-9a87c6b8c5f8 | -2.19364 | -52.12554 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df6b940c-94e9-390d-93d7-35794a636b89 | -2.53309 | -46.40023 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f92dd01-5489-3130-9061-d65164950f91 | -3.04251 | -54.02315 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53ec3541-b7e3-3a13-8413-ec0af3c36f54 | -3.47292 | -47.68368 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b56e78d0-aae0-378b-94d2-e405e58f3da7 | -2.73825 | -46.10567 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b4f06a0-4f6f-3aa1-a553-37838d22f83b | -2.91456 | -53.20926 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62056d1f-4b77-3f6c-babd-a15095403e4c | -2.81815 | -54.09915 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38c39905-b171-3c28-a393-42c7e50b7010 | -3.96314 | -49.95648 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab6a108e-cd04-3fba-8271-e1ed04506fc6 | -3.10622 | -53.98651 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea637c81-0521-3e5e-8788-403f372dc369 | -1.44568 | -52.58086 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d1f05ef-a90c-31ef-bd9f-1413a505331c | -3.8329 | -47.4692 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0709e848-2dae-3ee8-8121-2543320fc401 | -3.36816 | -46.65092 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98985d5c-7e29-3e51-b6a2-160b4c9212d6 | -2.58229 | -53.96159 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2fb0acf-6aef-3502-a937-8cdf7b33a19a | -3.83125 | -52.29473 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99bf6841-ae74-3790-a72f-94e082373eba | -8.21819 | -49.06954 | 2024-11-25 04:33:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd4fab85-2dca-3151-86eb-c762ed0d9e41 | -3.24229 | -53.27572 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d77491c-a434-3ccc-a0fc-051655749264 | -2.68 | -46.26538 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fea1a8a-fa98-32a4-a6e7-33f1fe1f92fb | -2.87961 | -51.58207 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8eb617f7-c749-3b50-976b-acd7635c2537 | -3.71351 | -52.41765 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 88797f2d-e1a7-3e0e-90dc-6f9106d4d81b | -4.25527 | -48.72432 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8822671e-079a-3f83-bb4d-e8a9373b8897 | -2.68503 | -46.27692 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45fcb677-8f30-3c06-8238-f260bac093de | -1.54911 | -52.58503 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d8a62f76-a386-3f61-813d-13aacc6fcbc0 | -4.09028 | -53.82917 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33e988e7-cd45-3dd6-8fab-0af5ae8d658b | -2.68356 | -46.15459 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bc3bc01-541c-3748-93ea-57e81c0c59d5 | -2.70015 | -46.11385 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d86d3d55-3d8b-3474-9699-8c51c865f287 | -3.18854 | -46.36211 | 2024-11-25 04:33:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a1a9f6b-ce32-3f88-a6ff-07cdf3a38c34 | -2.64953 | -46.13132 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f339630-d20b-3910-85f7-fd501b94e04f | -3.18713 | -46.43715 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47eb8eec-a1ae-36f3-9cd2-1d2d47e39c0c | -2.56694 | -46.42322 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ffed7b8-218a-3d57-a794-db51f0c1080b | -2.71893 | -46.27547 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d77c7b51-999c-39aa-97f0-32fac01a2eca | -3.63758 | -51.45466 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faf8c160-2290-3b9f-80be-f1b214e370dd | -2.82044 | -54.11374 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a3ebcdd-716e-3484-824e-2208b1d57006 | -2.39522 | -47.91705 | 2024-11-25 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6306449d-1441-3661-84bb-c1008e6c67ba | -1.62432 | -55.17406 | 2024-11-25 04:33:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7adb4ccd-cf10-3e98-bfb1-92c11509b0f0 | -3.45159 | -47.57773 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82afab66-e9f5-39f4-8fd3-934540affbb5 | -2.56319 | -46.55757 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cca98ce-b70c-36e5-beb3-43e056e703b4 | -3.78301 | -46.93532 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6417a43-911e-3f10-a682-eb305ad84b03 | -3.40177 | -44.74455 | 2024-11-25 04:33:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8d061521-a280-35bd-a043-e1841a9ed3ac | -1.47654 | -51.96018 | 2024-11-25 04:33:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4011e038-980f-33c4-ba78-1fdc30ef8f29 | -3.7806 | -51.87703 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d67d10c-0b2f-30cb-acf5-c30a4b96b3a8 | -2.34011 | -52.18075 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80d953fe-8d01-3279-8693-eafa3e8cb26a | -1.48923 | -52.52157 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e609544c-b2c0-3cbd-96fe-d4670a1f7412 | -3.16079 | -45.47649 | 2024-11-25 04:33:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b18e40e-8ed3-3613-b581-2457fd4bf9e3 | -4.43487 | -45.62926 | 2024-11-25 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ae79637-91e1-3af5-87cf-772df942ec45 | -5.00289 | -49.97105 | 2024-11-25 04:33:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c01005d1-3a4c-338d-afe0-644be6bc15ac | -1.77066 | -52.71767 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 062bd635-7e91-375b-a50c-aa5f6a4af65e | -4.25451 | -48.53349 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce1cfc81-81ff-36f5-9de5-508201a79020 | -3.98206 | -49.93905 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea52f893-09c3-30ff-9f23-c3656f968c9c | -4.21793 | -48.65724 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0d2b6b6-7ff1-303f-ba32-667ca9b75f2c | -3.79957 | -46.93789 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 220ecdc6-c4c8-3e91-b805-1ba582a7b51a | -2.19309 | -52.12905 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6a75cab-4871-3e96-9f9e-fe5ed96edafe | -3.25065 | -54.2175 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8fe2b61-3812-34bf-a320-d126bb208d0e | -2.79914 | -53.01347 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2751e816-d7a1-3082-bd21-0f2599a4e25c | -4.65975 | -49.4572 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e495f3a8-7fd5-3e02-93d2-1ffbdf826d04 | -3.80719 | -46.60474 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9c32250-bce6-3f05-b886-b7a12dcdc930 | -4.03271 | -48.08186 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 406bc516-4250-3208-a10f-b3fcff3db3a7 | -2.21955 | -53.61513 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e6503bd-04b5-35bc-bb53-e77f52713942 | -2.87884 | -51.58679 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a6e0434-81de-37eb-b91e-85950b97add7 | -3.64865 | -51.38913 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e91e310b-8daf-38f1-b33f-9019756067b8 | -3.77202 | -46.67794 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1400bf5-f496-3c65-ae49-bbe252e2718a | -3.72314 | -47.12398 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbc47a1c-2cf3-3b7e-827b-c161e9071f83 | -3.36622 | -51.42958 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43b13ebb-0f89-334f-ae4f-5754a95f5712 | -1.72052 | -52.76155 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6fa23ba-3218-3b3a-b48a-4c549b9913fc | -2.82479 | -54.02984 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34ad280f-f0cf-3bff-9383-b56d5d57b7db | -3.22382 | -53.93152 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b872b9a9-39b0-3ebb-98c9-50fd5ce6effe | -2.71742 | -46.11288 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0efa829e-cb6d-3f99-a450-170056606933 | -1.60679 | -52.58172 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ba6b4d6e-25ce-399d-a567-debe51a894be | -4.66178 | -46.92657 | 2024-11-25 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15ae156d-055c-3387-b761-a47f665e8343 | -4.2109 | -46.37148 | 2024-11-25 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 301f76ca-014a-31b2-96b3-2d43383f1b3a | -3.18402 | -46.50101 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abe1949a-474b-35ab-8e87-27759ffc38f6 | -2.59808 | -46.26738 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22cfe67a-4949-3566-a273-553b04c05092 | -3.24184 | -50.94174 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 483c0471-f5f2-31ef-86ad-65b4deb0cdaa | -2.79981 | -46.80682 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 825222a1-e0ad-3239-849a-41801def81be | -2.6458 | -46.85721 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7693e3ae-50f5-3a8e-9f7d-be1354cf7752 | -2.62198 | -46.1991 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2515e1e0-6617-36f1-8e3b-e3e4693709ea | -4.33591 | -45.88604 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71421254-1279-33c2-a799-ee8a0557fbf6 | -4.0824 | -46.8258 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36a1f8f9-4e0d-3019-813e-d7dd151f78c5 | -3.97181 | -46.72704 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bf65bcea-5e7d-3762-9fe6-2c0cd94c2539 | -5.33126 | -44.83792 | 2024-11-25 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0827268-5d17-3407-a77c-86ca3144a2c4 | -4.29769 | -48.23711 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0744521e-2f88-37cc-8a89-4e79409a2c09 | -2.7083 | -46.25898 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57ffab03-d46d-3f42-b910-a01d4599fb43 | -4.0564 | -46.68647 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eefed5d-12ed-3456-90b8-d2a8ea719acb | -1.38555 | -52.32869 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| deb4be48-18b7-3a1a-9759-c93abd8416b4 | -4.69668 | -47.18414 | 2024-11-25 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d535c6b-01ed-32d5-be60-2a107817cd1c | -1.39374 | -52.55713 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README20.md)
