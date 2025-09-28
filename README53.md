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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc99cacd-7a63-3120-b237-d8fe9e58fc14 | -5.75124 | -42.88313 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8f5c4fed-16e0-365c-b8bc-3350d4908507 | -4.52385 | -46.22232 | 2025-09-28 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81923415-c5c1-3319-870f-79991706dbe0 | -3.03296 | -50.44016 | 2025-09-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb3ad451-5a7a-32d3-97d1-15b65ee29da7 | -5.69592 | -42.63028 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af38d12d-ff7a-3d1f-9e3b-4ecb5601983f | -5.72786 | -42.66582 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e430f2f1-f47e-313b-939a-b40600f7ea64 | -4.00438 | -46.96654 | 2025-09-28 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8796254a-928e-3f9e-b403-628060d0bcf9 | -5.60811 | -43.37164 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f68b3ee6-9a84-3c1c-bcc5-ac8f3ffce3cd | -5.28823 | -43.14753 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39ca41ab-1b50-357e-9346-5969183a2472 | -5.09505 | -46.02636 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffd2fce3-80c1-32bb-8596-b20b315eb24c | -2.97527 | -39.93108 | 2025-09-28 04:23:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 25309804-fd4b-357f-99e6-00f699f3e9a3 | -4.33229 | -48.39094 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d42bb224-e122-3fa8-8f9e-42c0d6173919 | -4.48046 | -47.66959 | 2025-09-28 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78bf515c-e19f-322d-9e7a-1a32db9b4c6a | -4.53314 | -48.65024 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b58e9e3-64ee-3ec8-b442-276032f6c12a | -4.62519 | -43.10904 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ab29069-68c4-36d6-a932-79f59aba944d | -5.29764 | -43.15718 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e85093b-39d8-3d75-ba64-42573822c833 | -4.9167 | -48.16151 | 2025-09-28 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d9e14a8-8774-3b19-a06c-7049f8b401c2 | -5.09562 | -46.04406 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 930a6dfd-eabb-315c-8295-9dbea5e16cbd | -5.69527 | -42.63459 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1359ba0b-9432-316e-9e7a-00ae01594f03 | -5.37133 | -42.30238 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b2f321be-a716-315d-aa25-e18b7298f84c | -3.64775 | -48.32428 | 2025-09-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f88ebaaa-6bc1-3bd3-abad-067564640a43 | -3.208 | -51.27694 | 2025-09-28 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6b0fe189-b31f-3a37-acbc-c6e450d8675c | -4.29106 | -48.2638 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 38ee4080-4356-3c9d-b9f2-dc5994342b58 | -5.51442 | -42.73981 | 2025-09-28 04:23:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6f6e72b0-c5f5-36c8-976e-b86123d4dbac | -5.61163 | -43.3722 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45134204-b019-3340-99b6-e02498354270 | -4.13928 | -47.65468 | 2025-09-28 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cef93e6-fe77-3a90-957c-7f2f36866459 | -5.7627 | -42.88066 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 65d17f81-a3cb-368b-b1d6-0ce61da9796d | -4.47987 | -47.67329 | 2025-09-28 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ac4f636-9c61-3d56-9832-97256871684b | -5.7434 | -42.88616 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e23e3050-40a6-3dd9-ab50-6889e983476b | -5.18667 | -43.71683 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ec3056d-46e6-3245-9413-91549b3addd2 | -4.8067 | -42.7977 | 2025-09-28 04:23:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00691125-06ac-3413-a177-df6bd5ba2ac9 | -4.14458 | -40.0028 | 2025-09-28 04:23:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1032f14e-83af-3772-9530-1e796b4b815a | -5.81202 | -42.82436 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 85f52b00-82d9-3d2b-9e91-5fc91ddc3f22 | -5.29117 | -43.15206 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36669c9c-4acd-363f-a3b1-ec3cbfef4ec3 | -2.47622 | -47.65838 | 2025-09-28 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cbf0266-4480-3c34-aa11-5e85585c0ced | -5.80625 | -42.86185 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 180e90c4-d51c-3aa7-91b4-f367effb029e | 0.27495 | -51.40438 | 2025-09-28 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff86cd47-365a-302b-be45-f9c9fc894260 | -5.76206 | -42.88488 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3c854180-4c8f-3511-ad4f-6c8bd5e5c23b | -2.96488 | -49.57249 | 2025-09-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c09b3aa7-dfc1-360b-9eb6-e3085f6bb757 | -5.46412 | -41.07621 | 2025-09-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b4694f27-4caa-3fb8-84bb-2613738c3864 | -3.30065 | -52.5884 | 2025-09-28 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f544c464-ab4d-32c5-8e7e-740d1e3532c8 | -2.29874 | -47.99552 | 2025-09-28 04:23:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef6f1921-c82d-351a-80de-0b8bdc4bfad4 | -4.82465 | -45.82515 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a9b5bbe-e2a2-3816-a88e-e4a92134f3be | -2.90991 | -40.48989 | 2025-09-28 04:23:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f9dd54b-49e8-3071-9fe2-cbf0628537cb | -4.8559 | -45.7559 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62eb35a6-a63b-3639-b328-e8ca45862ed0 | -1.35756 | -49.29981 | 2025-09-28 04:23:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d26953b2-948d-356a-9ae8-3cfbd6e098ab | -5.84631 | -42.57688 | 2025-09-28 04:23:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 35bda6c9-248c-36bf-9de1-d666b471b24d | -5.26352 | -42.88725 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a7cfe33c-4347-3496-8c15-1ef35a9f7e1e | -5.42335 | -41.32525 | 2025-09-28 04:23:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd86afc3-344e-3a6e-b3d7-4de3dc5f689a | -5.18459 | -45.39318 | 2025-09-28 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4559565e-9aa3-319f-9bc8-630bbb82d252 | -5.46361 | -41.07965 | 2025-09-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d7421b51-e1a9-35fe-953a-fd2ef3cf9c0b | -5.35522 | -45.04137 | 2025-09-28 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e20e611b-c82d-31af-be3a-5593809691bf | -4.14271 | -47.6552 | 2025-09-28 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f104d71-0dba-3950-9fd6-303177da6b72 | -4.81154 | -42.79009 | 2025-09-28 04:23:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d4ba14c-2ce3-3903-8159-31648913740a | -5.81331 | -42.81598 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 7b89e35b-fed9-35ac-88bb-e4d4b0910441 | -5.08906 | -37.60877 | 2025-09-28 04:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 831fe0ac-0922-3896-b06a-ee332ce8cdae | -5.45911 | -41.08246 | 2025-09-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e4479b27-9de5-333d-812c-e3afd70e8b9a | -2.93287 | -48.01445 | 2025-09-28 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48f9c80f-a7af-315b-a74f-aa8f6992b4e4 | -5.72906 | -42.85869 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3394106d-be0b-3bfc-9b0d-5eddd288084a | -5.41442 | -42.26818 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0f728c32-9b95-3f1d-b877-5aa265505d3b | -5.28994 | -43.16006 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2619bddb-0458-3efe-92ca-77d2e670d38d | -4.9015 | -47.14043 | 2025-09-28 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54118ec9-5ed3-3845-8bdf-f347e9140eda | -5.78243 | -42.89657 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 33111c04-c27a-35da-a3e0-6f4f2f1a4f10 | -2.58023 | -48.40525 | 2025-09-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8585d66f-6f7d-3572-aee2-7153957ca2b9 | -5.65871 | -43.30211 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3f1a5ab-2d8d-38ab-a3a2-99a46bead9d1 | -5.33541 | -45.64402 | 2025-09-28 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d74840c1-4534-34c5-95a3-80d329fcad63 | -5.69724 | -42.62162 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0947fb6-bc34-3d3e-8903-eb8660217369 | -4.48329 | -47.67382 | 2025-09-28 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3120f0ab-e3ad-32d8-bbb6-8dd2e1414427 | -4.81242 | -48.24405 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd53a98b-fded-3f00-bee8-11278ded4a67 | -3.86877 | -40.34246 | 2025-09-28 04:23:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 36a12509-f14e-3951-8b44-5fe9dd47ed1f | -5.71093 | -42.65449 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9fbf1a66-4219-37b0-84ec-6de840159fa9 | -3.80622 | -47.58785 | 2025-09-28 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5121fb1-f60f-34bf-8649-d271f7fe22bb | -5.29348 | -43.16062 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 68d84545-7b10-388d-a261-77cecf5201e1 | -4.8285 | -45.82222 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7bf8e7c-8b4b-3f33-bdcc-7328639a35af | -3.97151 | -49.46006 | 2025-09-28 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b7fd89e-d9c9-3246-81f5-4aa66839537e | -5.25552 | -46.17221 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deb3fee6-89ad-363b-8a2b-d2de63ea4032 | -5.71027 | -42.6588 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c4f4597-4c34-386e-90ef-6fc45b7aacc5 | -4.95947 | -42.65419 | 2025-09-28 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54897c8e-0b87-3f73-9517-a78433d01efb | -5.22388 | -44.63747 | 2025-09-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f65a6e1-d287-31e9-8601-1125721d9033 | -5.75909 | -42.8801 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f714e0e4-adb0-31a8-a2a8-898ecc605600 | -5.15534 | -46.41817 | 2025-09-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f5cefda-93f6-356e-923d-d3993d3db092 | -5.81395 | -42.81177 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f8d5f54d-4250-3820-a2f3-1b40bc3c7fdf | -3.27409 | -43.53934 | 2025-09-28 04:23:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1aae704-47fc-3655-beea-680306addf8f | -5.77288 | -42.8866 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4d2dc1a4-5c6c-3d29-b41b-07b3138e9f5f | -5.77883 | -42.89601 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 54ac12ba-77b1-386b-be51-29ec743a3484 | -4.82519 | -45.8217 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e833391-8988-3928-b24a-aaf0fcdbdd41 | -5.71083 | -42.60611 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d4b44932-d2e7-32cc-9c8e-1bd776995612 | -3.73929 | -39.34752 | 2025-09-28 04:23:00 | NOAA-20 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c1edb1d-9bb2-3a81-abc9-425486b06bfe | -4.19259 | -46.25554 | 2025-09-28 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ca3bedc-9d73-3273-972f-84ec15292934 | -5.77353 | -42.88234 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7708d6c3-833b-3f2e-9c36-64394a5e4696 | -3.22423 | -47.12814 | 2025-09-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ade226d8-87bd-3bb8-9d79-ca3db1ee0093 | -5.74073 | -42.65502 | 2025-09-28 04:23:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 02cf4e70-e26d-3fa3-8004-c72ad7993f55 | -5.73577 | -42.66295 | 2025-09-28 04:23:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48869f95-5f68-38ca-bc5e-dba9bc91bff9 | -2.47684 | -47.65455 | 2025-09-28 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ed95018-49f4-3690-8543-21079800af2f | -5.19013 | -43.71737 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a595d70-c8b6-3d9b-a45d-25588b936693 | -4.13099 | -44.22448 | 2025-09-28 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6889889d-5ac8-3f14-ac1d-cb88d02570a1 | 0.27947 | -51.40365 | 2025-09-28 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0990938f-0e67-36d7-aa68-4a883fab08c8 | -4.97281 | -43.19923 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ae1aa29-f287-36a8-93a6-35c6e3f11c02 | -2.44273 | -48.6071 | 2025-09-28 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 769a5ddc-26d9-3059-8616-2db39ed85c8f | -3.79086 | -48.86451 | 2025-09-28 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aceb52ce-748d-36ee-8027-90eeb5b7ea22 | -5.81459 | -42.80761 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |


[Clique aqui para ver as próximas entradas](README54.md)
