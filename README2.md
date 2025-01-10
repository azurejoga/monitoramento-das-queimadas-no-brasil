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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2e1fdc8-8d8c-36e0-8f7a-6dc11d2fee30 | -10.0834 | -36.3406 | 2025-01-10 01:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 247.4 |
| 1cbfb3b9-2475-3621-aa44-0f7ca190ba5d | -7.7279 | -34.9243 | 2025-01-10 01:00:00 | GOES-16 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 20f6421a-4656-34dd-84ce-ce6bdd176474 | -9.7226 | -36.0805 | 2025-01-10 01:10:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.5 |
| a93c7687-1711-3f01-b308-6ba40d36b903 | 1.9236 | -60.4019 | 2025-01-10 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e5d3a194-8030-3e9d-8281-76244060abab | 1.9419 | -60.4017 | 2025-01-10 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1bff5513-76f5-3651-81de-d57f6d828c46 | -9.7221 | -36.1077 | 2025-01-10 01:10:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 193.8 |
| 88694ac4-b040-3a8b-b18e-c2887412ef5d | -20.9787 | -49.7789 | 2025-01-10 01:10:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.9 |
| 0b2690da-87f0-39f8-bb33-84fe331424e3 | -7.7279 | -34.9243 | 2025-01-10 01:10:00 | GOES-16 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 107.9 |
| 6b2bd290-e4f1-393b-9d69-b43820669aec | -20.9787 | -49.7789 | 2025-01-10 01:20:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| 8cf7ebbb-0ba5-3302-9fd0-51d154c9a59d | 1.9236 | -60.4019 | 2025-01-10 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e4d79040-c2c2-37e5-89a3-97ee47886aba | 1.9236 | -60.4208 | 2025-01-10 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 22720b8b-aa17-3e79-9297-a3c0dcdebaf9 | 1.9236 | -60.4208 | 2025-01-10 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 60f62b8b-85ad-37bc-abce-16eb977a7938 | 1.9236 | -60.4019 | 2025-01-10 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e78e3a3a-9b85-341a-b4d5-185fe57a86e3 | 1.9419 | -60.4017 | 2025-01-10 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 41ff7135-7ae7-32c0-ab6e-53581c2bce14 | 3.513 | -60.581902 | 2025-01-10 01:49:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 031ff1cc-4746-3e1c-8ae2-d7b5f2a7a920 | 3.5165 | -60.566399 | 2025-01-10 01:49:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff7b0f7-6b83-3df7-9119-9666e5d86fea | 3.4959 | -61.344799 | 2025-01-10 01:49:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e99ab4ee-b445-3005-a300-0e2ce07e7ba7 | 2.1352 | -60.439999 | 2025-01-10 01:49:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6770fb65-afd6-3c62-8af9-4541eda1a4b9 | 3.9125 | -60.2994 | 2025-01-10 01:49:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 889271f4-f326-3fc4-a1dc-f4c14d7ef3cd | 2.1386 | -60.4249 | 2025-01-10 01:49:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 90c179fe-7376-311e-9cce-1c9cf3f71f08 | 3.9028 | -60.297298 | 2025-01-10 01:49:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c1f4a64-c0b1-3cdb-b48b-9bc18fae7fff | -20.9787 | -49.7789 | 2025-01-10 01:50:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 3b28ab3d-d81b-3e16-98d7-41e11e8bd85a | 1.9236 | -60.4019 | 2025-01-10 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bbf5b7c1-de5b-318c-acc7-d81c37ca2cbe | 1.9236 | -60.4208 | 2025-01-10 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 4740fa4a-b9a3-3f9c-8d79-853dc09d73cb | 1.9419 | -60.4017 | 2025-01-10 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| c6a020d8-438e-3060-bf19-c4d338aba7e6 | -20.9787 | -49.7789 | 2025-01-10 02:10:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| 5b5f5451-ee1e-3a79-8b47-2343c55f5d22 | 1.9236 | -60.4019 | 2025-01-10 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.4 |
| bace62f1-6ebe-3641-880c-1a36a02c2655 | 1.9236 | -60.4019 | 2025-01-10 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3d70a0c1-9ed5-3a24-8a46-4b8883dc4b3e | -8.9078 | -35.4293 | 2025-01-10 02:50:00 | GOES-16 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.4 |
| d42e5926-ceb8-325f-815e-4f517a40acb4 | 1.9236 | -60.4019 | 2025-01-10 03:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| c88dcb7a-9f17-3bc9-a3d4-6956752951cf | -7.1725 | -35.0015 | 2025-01-10 03:00:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 130.3 |
| 06b4054a-f5e8-3e8d-8971-6f28139bbd47 | -7.1722 | -35.0291 | 2025-01-10 03:00:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 124.9 |
| 9b62c59e-82b9-30ad-9c63-8c917917d88d | -10.0651 | -36.29 | 2025-01-10 03:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 123.1 |
| a12d4282-4e8d-34f2-be09-a42e09c8b7c7 | -10.0458 | -36.2935 | 2025-01-10 03:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 126.6 |
| eedda03b-24f1-3e33-99cd-408aa7ce38f9 | -7.17023 | -35.0199 | 2025-01-10 03:29:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9cba85f1-e378-3183-80f0-64a3365eede7 | -8.00104 | -35.08843 | 2025-01-10 03:29:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4a0b0440-0237-367c-a461-72443976d454 | -9.45726 | -35.92856 | 2025-01-10 03:29:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d13d5461-647d-38a5-b4b8-b2019831aa71 | -7.5627 | -37.03717 | 2025-01-10 03:29:00 | NOAA-21 | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9c9befb-684c-367f-9e13-cdf7c14cc1bf | -5.3821 | -36.46133 | 2025-01-10 03:29:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c999aceb-7ea2-36c3-9365-1dd0ff256d5f | -9.45297 | -35.93216 | 2025-01-10 03:29:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 616efd88-9730-3e9b-87f1-fdb67b326af9 | -7.37684 | -34.88569 | 2025-01-10 03:29:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2bcde6fc-8fb8-3e50-9a87-4a8338b2f11e | -9.19023 | -35.36909 | 2025-01-10 03:29:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a229f16e-542f-348b-8ab2-d3cc09fe5a2f | -8.63801 | -35.79189 | 2025-01-10 03:29:00 | NOAA-21 | BELÉM DE MARIA | PERNAMBUCO | Brasil | 2601508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4c54788c-432a-3456-97ea-4687cdeae1f0 | -7.66031 | -35.06346 | 2025-01-10 03:29:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 45cb1243-247b-380d-892e-477c7deecef0 | -7.60384 | -35.38926 | 2025-01-10 03:29:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bed7b736-e1bf-3662-924b-04a77c0917f6 | -7.65679 | -35.06292 | 2025-01-10 03:29:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52c36450-3257-33c2-ae76-c492f496aec5 | -9.44381 | -35.96511 | 2025-01-10 03:29:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7e07020b-7269-38af-b3a7-2df0086409c3 | -7.23213 | -35.10809 | 2025-01-10 03:29:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 55942d40-5e2f-3eab-aff7-ad8682da07d3 | -6.77957 | -37.52292 | 2025-01-10 03:29:00 | NOAA-21 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 599f70c3-17d4-30f2-beda-35b14f4e7d91 | -8.42298 | -35.23972 | 2025-01-10 03:29:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 85991493-0fa1-39cd-bd4c-e9f92b94e885 | -7.8068 | -35.1679 | 2025-01-10 03:29:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 92fcb6c4-c416-3470-b810-b09cef7f2959 | -8.33708 | -35.14126 | 2025-01-10 03:29:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 63791944-ce1d-3ad5-99cd-0f5898843105 | -8.4811 | -35.1963 | 2025-01-10 03:29:00 | NOAA-21 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 55f8b777-bfb3-3ef8-9cc8-9babca001b22 | -7.60026 | -35.38868 | 2025-01-10 03:29:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f5b2c5b-104c-3d9e-b6ab-2c1af33f32c1 | -6.3484 | -36.1048 | 2025-01-10 03:29:00 | NOAA-21 | SÃO BENTO DO TRAIRÍ | RIO GRANDE DO NORTE | Brasil | 2411700 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 262feb2e-bb52-382e-841a-934fa9ac5836 | -8.46509 | -36.96225 | 2025-01-10 03:29:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a7714ad-9ca4-373a-b01b-12943b8a91db | -9.45657 | -35.93276 | 2025-01-10 03:29:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b88ddd78-2172-388f-b825-0436bc58880a | -9.87778 | -36.29041 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| df649596-b991-3ffc-9bcd-083b76ef7778 | -9.87708 | -36.2947 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5f8e7797-946b-3b60-903a-c4a429f3e5f0 | -9.86614 | -36.29285 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eb56e810-7359-3e7b-a3cc-3cd34354e35a | -9.7478 | -36.63869 | 2025-01-10 03:32:00 | NOAA-21 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 72e1edb4-0139-3c49-8629-896091ce08b4 | -9.87637 | -36.299 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3520f87e-2fd5-37a5-8794-3f7b60a1a9e0 | -9.86685 | -36.28856 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bc29eec3-d61a-3a6b-8b99-d60178bc2e5a | -9.86979 | -36.29347 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 195.1 |
| ea57c7aa-ff9c-3f2e-8c9f-96ec4881b0e9 | -9.87414 | -36.28979 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| f068aae9-c906-3dd4-ab71-c072b852ab57 | -9.86466 | -37.09987 | 2025-01-10 03:32:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1bb13b09-aa39-3001-acaa-7176ed5bb2f7 | -10.62427 | -37.06588 | 2025-01-10 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c074f42d-db1a-34f3-8df1-e1eab2bcdfad | -9.87049 | -36.28918 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 9202bf8f-96d0-34f8-b487-b57840cb75dd | -10.45423 | -37.12954 | 2025-01-10 03:32:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20be4a81-099b-394c-8206-cc89cf8650b6 | -10.62805 | -37.06648 | 2025-01-10 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1eb3a027-1656-3a7c-9c45-b46ee67ba619 | -9.8625 | -36.29224 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ba85925c-4a38-3eb2-b049-9e1b8370db39 | -9.86908 | -36.29777 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 195.1 |
| 0c43b786-531d-306d-a1df-d07f27fa1908 | -10.62898 | -37.06432 | 2025-01-10 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a60d51bb-b6bf-35c7-8132-ea3a6e3c962f | -9.86707 | -37.10298 | 2025-01-10 03:32:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1ccdb823-c823-38dc-a00a-92b265251f63 | -9.87272 | -36.29839 | 2025-01-10 03:32:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 195.1 |
| b36e76bd-c352-3caa-86d7-d613cfd97e8c | -22.01425 | -49.12537 | 2025-01-10 03:34:00 | NOAA-21 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 10a7645c-74d9-3fb3-a384-88560be5bc64 | -22.74975 | -42.95166 | 2025-01-10 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99ccb05a-c749-3fe2-ac34-e07179712587 | -22.01563 | -49.1198 | 2025-01-10 03:34:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d9e9552-fe50-352b-ae5b-ec7193643a5f | -22.74594 | -42.9529 | 2025-01-10 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8bd26b03-a8c0-3a75-8827-579cd7824cd3 | -22.54592 | -47.25861 | 2025-01-10 03:34:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bd3c23e-c88e-3210-8618-ac69127c2a77 | -20.98189 | -49.78345 | 2025-01-10 03:34:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d1e7bb58-ece6-3b16-a526-cfe4bcf865f9 | -20.98237 | -49.78432 | 2025-01-10 03:34:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| a42bc3e2-6732-3cf2-9fe9-41d05499f9bb | -20.98409 | -49.77748 | 2025-01-10 03:34:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 6291110c-5999-3105-a304-5be1699e0b9a | -20.98357 | -49.77657 | 2025-01-10 03:34:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 857d1ecd-c553-3a79-99a5-14abd39561f3 | -22.01603 | -49.11825 | 2025-01-10 03:34:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fccd9d91-7d29-34cc-939e-b3007dc51930 | -20.97732 | -49.77572 | 2025-01-10 03:34:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 3937e834-a89e-37de-87d9-e87495fc5817 | -22.78797 | -43.75861 | 2025-01-10 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2b7ff1ab-a945-3149-86d4-70c2edf37bb9 | -20.97681 | -49.77475 | 2025-01-10 03:34:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 719a4e44-1c87-323b-b155-3eaab6d1c433 | -22.01469 | -49.12379 | 2025-01-10 03:34:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 78f7c990-9220-3338-b3b0-f39e6f12e217 | -20.97905 | -49.76886 | 2025-01-10 03:34:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 0d1520c4-f5a5-37f2-8629-132f05aa9294 | -23.35235 | -48.53358 | 2025-01-10 03:36:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3e7f9ede-125a-35eb-9f3f-2922c6312ede | -23.35355 | -48.52861 | 2025-01-10 03:36:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 71a4e9c3-5eb1-3194-90f6-c67c4db04c35 | -4.55071 | -37.92475 | 2025-01-10 03:53:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a955a25b-5801-3145-b8f3-50d8bd7921ef | -3.04771 | -40.08594 | 2025-01-10 03:53:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e17a608d-51c2-3c9a-afcc-a6f20b01b4ac | -5.13464 | -39.85133 | 2025-01-10 03:53:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 25c501d6-398a-31a4-8275-77d650d1b793 | -5.66374 | -35.7588 | 2025-01-10 03:53:00 | NPP-375D | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7fcb37b1-401a-31d3-bd94-88b83853481b | -3.82945 | -45.36058 | 2025-01-10 03:53:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5477559-759b-3bc1-881a-9b9cc624f251 | -4.77607 | -38.55278 | 2025-01-10 03:53:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d39effb-2f31-359c-88f8-c3a73ead21e0 | -5.13522 | -39.8477 | 2025-01-10 03:53:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f929400c-ce0e-3123-8583-dcaffa9c38a2 | -7.96464 | -35.20089 | 2025-01-10 03:55:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
