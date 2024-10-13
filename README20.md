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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ef8a32e-5017-39a7-a8de-61990e44a83b | -15.9629 | -59.1079 | 2024-10-13 01:06:37 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| cac48c1f-1805-3260-8512-b700b5459c8a | -16.9998 | -57.4586 | 2024-10-13 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 02e85512-e924-3276-80e8-1537c937f37a | -17.1957 | -57.4562 | 2024-10-13 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.7 |
| bf424d82-4e09-3d8f-b191-9ce7748d62c5 | -17.1954 | -57.4767 | 2024-10-13 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.4 |
| 2bd1abfb-22c3-3d3f-a36f-abd7fc7cc97b | -17.1758 | -57.479 | 2024-10-13 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 791fc381-f3ab-3a1a-a7f2-3a3ee6db4028 | -17.1761 | -57.4585 | 2024-10-13 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 185.0 |
| 0bc8b286-000e-3179-8bf1-fc86054e3733 | -17.1764 | -57.438 | 2024-10-13 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 4d4b8948-8906-39b8-ac44-8aa7bbcb5cda | -17.6474 | -56.2876 | 2024-10-13 01:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 25769641-45b2-34bb-b471-15ee4175594a | -17.6478 | -56.2668 | 2024-10-13 01:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| d33a605b-9bfa-34ab-8898-c8b61ec77b62 | -18.1949 | -56.5899 | 2024-10-13 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| e4d88066-7605-3c3e-af98-08949af0813f | -18.1953 | -56.5691 | 2024-10-13 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 1748f586-653d-311c-92c0-a4fc8744e1d4 | -18.2147 | -56.5873 | 2024-10-13 01:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.4 |
| e8c70e17-592d-35a0-b810-3fa2c47c81a1 | -18.2151 | -56.5665 | 2024-10-13 01:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.7 |
| c01f2ff5-0924-3562-945c-a113eb78e5f0 | -18.2155 | -56.5457 | 2024-10-13 01:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 44e7ce58-4d9e-3cb7-a885-8f34dc86a35b | -18.2166 | -56.4832 | 2024-10-13 01:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 4414e0a5-d9f3-37c7-88f0-9d4936c82e1e | -18.2349 | -56.5639 | 2024-10-13 01:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 62fcbf70-9af9-3bef-82ac-3c48591489c9 | -3.0731 | -54.2473 | 2024-10-13 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| db43d342-a87d-313b-b8c4-3701222aff57 | -3.0956 | -53.0559 | 2024-10-13 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| f72404d5-5583-350e-8c60-95d566a0da7a | -3.0957 | -53.0355 | 2024-10-13 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 216.6 |
| a95c763f-d136-3800-b73d-6b997bdd9f78 | -3.114 | -53.0554 | 2024-10-13 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 498a06da-1279-3b30-8ceb-e20e80f188e5 | -3.1141 | -53.0351 | 2024-10-13 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 3f78954b-88cf-34c3-9b17-4df750111b05 | -3.1792 | -50.4551 | 2024-10-13 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c54c2357-6ed3-31d8-9c51-4c02fc1e8e4f | -3.7128 | -40.7102 | 2024-10-13 01:15:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 65.2 |
| c5fcf827-d2ab-3d96-951b-49769202d32d | -4.1149 | -48.2299 | 2024-10-13 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 3a99deed-a845-3488-828e-10fcb9e30a4c | -4.1148 | -48.2515 | 2024-10-13 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 785fc530-6318-3bab-9274-3d4ab2109073 | -4.4026 | -49.7563 | 2024-10-13 01:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 62369a1a-c50d-368a-8789-75c3eee9a521 | -4.7188 | -60.7882 | 2024-10-13 01:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 9adeeef1-23c6-38b0-be4b-af8a63c6e07d | -4.7189 | -60.7692 | 2024-10-13 01:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4772201a-c3f4-30ea-95cd-ffdef3fef227 | -4.7371 | -60.7877 | 2024-10-13 01:15:34 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c4f998f1-2a18-358b-8495-14a61f9fc188 | -5.1381 | -45.3969 | 2024-10-13 01:15:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 1122d240-cc4a-33c6-9c88-8419de8eb784 | -5.5796 | -46.1753 | 2024-10-13 01:15:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 09e9f38d-19a1-3e72-a521-051ffec60aeb | -7.3657 | -64.6656 | 2024-10-13 01:15:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c4feee54-c2a3-3edd-a5ca-638d9cb219b3 | -7.3841 | -64.665 | 2024-10-13 01:15:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 9e093389-e402-3f79-8850-e9d9d5cbdf7b | -7.3842 | -64.6464 | 2024-10-13 01:15:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 707f145a-06d9-307a-ae5a-45bfa309dc53 | -9.7359 | -64.2295 | 2024-10-13 01:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| f8ef5a73-4027-3334-9408-ececd199f23b | -10.4693 | -63.1384 | 2024-10-13 01:16:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 545ce8c2-d3e0-3815-a3d2-65d033051100 | -10.9311 | -44.6789 | 2024-10-13 01:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 1d87cd8c-dccb-3516-b196-e84bd2b5daf0 | -11.2532 | -50.9249 | 2024-10-13 01:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e9e1adcb-1563-3195-82b8-00ded50aaebf | -11.2535 | -50.9036 | 2024-10-13 01:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 09ce99b8-c546-3351-99b7-3bc7801d970f | -11.2722 | -50.9228 | 2024-10-13 01:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 698e842d-006f-3226-a2c4-66b35b46076a | -11.2725 | -50.9016 | 2024-10-13 01:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e54e36b1-ff60-3466-ae5a-88b16c811f21 | -11.6334 | -48.3736 | 2024-10-13 01:16:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 834a4b55-69e6-30f4-82e9-53a64c5c2726 | -11.712 | -64.9777 | 2024-10-13 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 99cd09e8-bd09-363d-8c2f-3977d5c4412c | -11.7308 | -64.9769 | 2024-10-13 01:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 0c811d34-c581-383a-a161-9f00dd6f8ffc | -12.2754 | -47.6473 | 2024-10-13 01:16:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| cce5b86e-a428-3b9f-8b71-d493ea826705 | -12.3793 | -63.7294 | 2024-10-13 01:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 76aca49d-9157-3c48-bf55-02653dec2891 | -12.3982 | -63.7284 | 2024-10-13 01:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 10df280f-550c-3992-9fff-1cafc983699c | -12.9182 | -62.5287 | 2024-10-13 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 80d1d69e-42a4-33b2-a001-67a82d8be11b | -12.9372 | -62.5275 | 2024-10-13 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 00ee12f5-d6cd-3747-b1ed-fb30ecd74c8a | -13.1475 | -62.3215 | 2024-10-13 01:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 49c6f6fe-8a41-3c46-b6c5-6f9a04337548 | -13.7346 | -60.6079 | 2024-10-13 01:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 43712790-539a-3116-94fc-1159047064ed | -13.7348 | -60.5883 | 2024-10-13 01:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 82a224b4-3a2a-3b61-b2b9-9424abd28d49 | -15.3047 | -41.8955 | 2024-10-13 01:16:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| ffb45d45-4e71-36da-ac9d-15f9857e76bf | -15.3244 | -41.8911 | 2024-10-13 01:16:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.5 |
| dcaa1eb5-c847-3ea0-8e27-2ef78014eb5a | -15.3251 | -41.8663 | 2024-10-13 01:16:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| 1d152b6d-08e4-325d-8b6b-2cc626f5b525 | -15.6419 | -59.9767 | 2024-10-13 01:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| d7b85204-4c23-33a2-827b-2ad3c7e31216 | -17.1758 | -57.479 | 2024-10-13 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.1 |
| c40ba891-641e-3822-9602-db15bd965baa | -17.1761 | -57.4585 | 2024-10-13 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 189.6 |
| 9a4eea46-7672-3449-8f2f-299d38757139 | -17.1764 | -57.438 | 2024-10-13 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 23f51958-05a4-34b8-b040-65891b34e570 | -17.1954 | -57.4767 | 2024-10-13 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.0 |
| d7a33d56-3a3d-33ac-9363-417bcadd7004 | -17.1957 | -57.4562 | 2024-10-13 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 168.6 |
| 6443a03b-5ed8-393f-a16c-0f3105a16015 | -17.6474 | -56.2876 | 2024-10-13 01:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 51bc8b28-5c36-3b7b-9a5f-91b9035c5bfa | -17.6478 | -56.2668 | 2024-10-13 01:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 6daf1af5-d8f8-300f-8e15-e51237f1ed0b | -17.964 | -57.3843 | 2024-10-13 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 68de1412-8477-3031-9b58-9a075916e3e1 | -17.9643 | -57.3637 | 2024-10-13 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.8 |
| 3ae3b97a-6e88-318e-8f90-40135e2bede2 | -17.9837 | -57.3819 | 2024-10-13 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.1 |
| b520fc8f-620e-3ccf-8f13-307dca9a0263 | -17.9841 | -57.3612 | 2024-10-13 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.8 |
| 041b2a6b-9962-3fab-8b6c-8cf2494f029b | -18.2147 | -56.5873 | 2024-10-13 01:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 87bcb6ad-48e4-3b7a-a55d-d0db1e4d88e6 | -18.2151 | -56.5665 | 2024-10-13 01:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.4 |
| e1c1a239-69e4-38d5-8f53-304b94b9a8cc | -18.2155 | -56.5457 | 2024-10-13 01:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| c08cefaa-b5ff-3e19-af8f-28669b1e23a3 | -18.2166 | -56.4832 | 2024-10-13 01:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 9bb09bd7-8173-32dc-a9e3-14fd454c7a83 | -18.2169 | -56.4624 | 2024-10-13 01:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| cdb2f4be-f19f-3c0e-bc51-bf21e9b30691 | -1.9217 | -61.7432 | 2024-10-13 01:25:17 | GOES-16 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| ffbd8c63-844d-3186-85cc-7789fc4f1f77 | -1.9486 | -56.4496 | 2024-10-13 01:25:17 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 609898ea-3e6a-3986-b80f-5f83d84448c7 | -2.7959 | -49.2849 | 2024-10-13 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 8069ded6-b016-39fb-89c7-29b6d5f8d9f7 | -3.0731 | -54.2473 | 2024-10-13 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 031acc14-5301-38ac-a2b6-b43221e7aa62 | -3.0915 | -54.2469 | 2024-10-13 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 232e08d4-34cc-364c-b8ae-f231769fe85e | -3.0956 | -53.0559 | 2024-10-13 01:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 93d846cb-6e53-3961-8988-1869545c9377 | -3.0957 | -53.0355 | 2024-10-13 01:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 4ffe9bb3-fdc0-3e0e-8af6-9e3b2043cfbc | -3.114 | -53.0554 | 2024-10-13 01:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| bb39295e-0274-35d2-bd34-57ea1c5e7d69 | -3.1141 | -53.0351 | 2024-10-13 01:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| d47afde1-1201-317e-af76-a05b29a5e95e | -3.2225 | -48.9306 | 2024-10-13 01:25:25 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 057887ce-f1c0-384d-a340-c5556543da60 | -3.7128 | -40.7102 | 2024-10-13 01:25:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 14e11b01-fd86-3d24-b4af-ddcb39a5b231 | -4.1148 | -48.2515 | 2024-10-13 01:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| fbdcc387-7da3-3759-a440-0e87f7bd8b84 | -4.1149 | -48.2299 | 2024-10-13 01:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 048e1cb8-95ee-3e00-97a1-78522bef4d7e | -6.1299 | -47.2884 | 2024-10-13 01:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 9aa96ac3-9b37-338d-ac57-149c89a3d940 | -6.1301 | -47.2664 | 2024-10-13 01:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 9cb6d89f-c438-378d-a9e7-99f0a4cf5d53 | -7.3657 | -64.6656 | 2024-10-13 01:25:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| de423a39-5557-3c5a-91c7-11827d1f6bb9 | -7.3658 | -64.6469 | 2024-10-13 01:25:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| dc41f4e6-1fe3-33ee-b70e-cbd3f9334e25 | -7.3841 | -64.665 | 2024-10-13 01:25:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 31293297-c840-3ec5-87a1-b74f464eda86 | -10.5281 | -49.9778 | 2024-10-13 01:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 84e93965-f5ed-3804-a955-af8a0c743ec0 | -10.5283 | -49.9564 | 2024-10-13 01:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 3bfe58dd-43cd-30de-acd4-0438fad5f4fd | -10.4692 | -63.1574 | 2024-10-13 01:26:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f0916097-1c68-3000-86c3-9b891602a5c6 | -10.8792 | -44.3613 | 2024-10-13 01:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d0e6c956-9f0a-34ff-99bc-dd1086329cb4 | -10.8796 | -44.3379 | 2024-10-13 01:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 916885ff-8f95-3034-82a4-b61ad2516428 | -11.2532 | -50.9249 | 2024-10-13 01:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 13753295-b7fa-39c4-b5df-59de730835ca | -11.2535 | -50.9036 | 2024-10-13 01:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| db57da65-d0c4-3b7f-8da4-e5abe973b902 | -11.2722 | -50.9228 | 2024-10-13 01:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| ebbc546b-33c0-31e6-9d8f-917ee199be36 | -11.2725 | -50.9016 | 2024-10-13 01:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 3c603ad3-a281-3229-a3d4-d5a9eaf49f65 | -11.6334 | -48.3736 | 2024-10-13 01:26:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |


[Clique aqui para ver as próximas entradas](README21.md)
