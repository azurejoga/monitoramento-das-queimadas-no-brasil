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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a99aac3-73b4-3266-ace4-67a9c0efcacf | -6.35385 | -43.64837 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f0a306db-e98d-31aa-8eb5-766399e12f08 | -6.35804 | -43.64909 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3023cd3c-5246-3558-821a-764b2a3259fd | -6.34906 | -43.65182 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3dd8df3e-8097-35e8-92a5-543392c9e508 | -6.36222 | -43.64978 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3fdd5924-56e2-392d-8097-75293f8b0b26 | -7.4469 | -45.52032 | 2025-04-15 04:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a906b57a-b6ec-31aa-9ee5-4c68b4d94235 | -7.07356 | -44.38127 | 2025-04-15 04:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0037df62-99f0-316e-9c78-451afa054ea9 | -8.11212 | -43.12236 | 2025-04-15 04:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb3d9327-4936-39e8-8f7f-253af906c952 | -6.35744 | -43.65317 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ee208173-3cc8-31ec-9ae8-6cbc8c82dd97 | -7.44759 | -45.51574 | 2025-04-15 04:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c637e09f-a0ce-315d-8514-b4968063fd75 | -6.35863 | -43.64501 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c0e1821-72a1-3bb8-b8c1-ee4bf8741856 | -6.66364 | -47.59074 | 2025-04-15 04:36:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cea1ecee-9c82-3f63-918d-e46d32e4f98b | -5.56752 | -44.53471 | 2025-04-15 04:36:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0b10c9b-d6f6-3830-9f64-87b1d9ecfe91 | -5.5636 | -44.53413 | 2025-04-15 04:36:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| acabb340-0c73-3621-aefa-6b47d87b79c3 | -6.34848 | -43.65587 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8e32478-02d3-3912-844c-9cd0c93d5188 | -7.44829 | -45.51113 | 2025-04-15 04:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16a69ad0-41a7-3d57-9953-09590cf01a51 | -6.36281 | -43.64577 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aac0df1d-3373-3420-8ea8-ea8455afb03a | -3.39466 | -41.63959 | 2025-04-15 04:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a8a05048-c81b-3834-8e0c-62a2c0e3591d | -8.11414 | -43.12143 | 2025-04-15 04:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 72a11787-fc31-3c48-b07f-23bb17da5d41 | -6.70028 | -44.3495 | 2025-04-15 04:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01516219-c01e-37e7-a5d5-17dc62e2f65f | -6.35267 | -43.65653 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2762b47a-9196-3925-b042-bfe8148392ad | -6.36107 | -43.65773 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4e2c8502-7e24-31c0-8a36-d099cc04b41f | -7.44789 | -45.51378 | 2025-04-15 04:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb5dc2ea-fd11-388c-951c-1dd09bd5beeb | -6.69976 | -44.35303 | 2025-04-15 04:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7092398f-a97b-3aca-9fda-bdf47b6dad42 | -6.35325 | -43.65253 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 92c4688c-8c12-35ad-b3b9-78293ab546d0 | -6.36699 | -43.6465 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02b55f4b-f447-3479-b055-f053abf7f3a1 | -6.36164 | -43.65379 | 2025-04-15 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0b22f23a-70b4-318b-b28c-97c7362fc9ef | -6.66307 | -47.59441 | 2025-04-15 04:36:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a47781d-5acb-395e-a96c-66feba592329 | -7.44722 | -45.51839 | 2025-04-15 04:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 610c42fd-57d0-387c-ac3e-0c0738f251c1 | -8.93752 | -44.22347 | 2025-04-15 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4b28ed4-ca99-3ad7-8df9-75ae71a35641 | -9.60959 | -37.03717 | 2025-04-15 04:38:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8cf8976-f513-360a-bf04-ebbfca7be205 | -11.78858 | -40.92996 | 2025-04-15 04:38:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4bafe643-0d48-3ef1-bde1-88c742cd8c8f | -8.93845 | -44.22325 | 2025-04-15 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 198fa99e-b875-3e56-9a1d-7b84943852f7 | -9.61717 | -37.03158 | 2025-04-15 04:38:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 418252c2-081d-3ae9-bfe2-af5ae6a74296 | -8.93695 | -44.22737 | 2025-04-15 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cf36aa5-1ca8-3f05-af74-17939e50eaec | -9.61034 | -37.03093 | 2025-04-15 04:38:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 74ddbcce-3d2f-33d4-aa75-f54c4a2f4716 | -8.93791 | -44.22716 | 2025-04-15 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4dee100-aead-3805-a176-6a65573b9835 | -8.9421 | -44.22783 | 2025-04-15 04:38:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e5f60f6-2c73-32d3-aa21-67cfa59030f2 | -14.9946 | -48.97695 | 2025-04-15 04:38:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cd2fcf6-4221-3141-9c4b-d3f06b0a3ebb | -11.78815 | -40.93344 | 2025-04-15 04:38:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5773455-4aad-338a-91c0-73f81a63d28e | 2.3964 | -61.3048 | 2025-04-15 04:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 577f6fb7-ebf4-3182-9cb2-4ace239f4904 | 2.3965 | -61.2859 | 2025-04-15 04:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f943f90e-db7c-3c6b-9c7b-dea67b786806 | -21.19491 | -44.93446 | 2025-04-15 04:40:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 66b41d68-9e73-322a-b9f9-78b8d0490fbf | -18.80999 | -48.52513 | 2025-04-15 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7770d1ca-9cb7-3d10-ab14-84a5bee6a758 | -21.35057 | -48.59191 | 2025-04-15 04:40:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58ddc1f5-dd30-3d0b-8455-98996848b904 | -18.8106 | -48.52057 | 2025-04-15 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9eabedfe-1d53-3215-8e88-33232815a02e | -19.93619 | -47.60574 | 2025-04-15 04:40:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 13e371b1-17b6-3bef-8f0c-9ff4c8856168 | -19.94013 | -47.60632 | 2025-04-15 04:40:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 60baa305-0646-3b1f-94ce-fbebfe52167c | -18.80778 | -48.5224 | 2025-04-15 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b16643c2-2a92-37cf-956a-38b7c9ab24d3 | -18.14491 | -47.79921 | 2025-04-15 04:40:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d04b8d49-0760-39cc-a531-8243bb944c61 | -19.45358 | -45.30483 | 2025-04-15 04:40:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca22007c-714c-30d2-a255-bdee5281284f | -19.96466 | -47.66393 | 2025-04-15 04:40:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a4c5fdd-da27-3f24-aec0-3c9f0e65206d | -20.23044 | -46.55993 | 2025-04-15 04:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95f4500e-b2cb-3e3e-aa38-8717d1d755f8 | -20.22994 | -46.56393 | 2025-04-15 04:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e8e887ea-d7a5-395e-b8dd-e6babef75376 | -21.95701 | -44.8783 | 2025-04-15 04:40:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 14de7a11-e58d-32c2-b881-b1bad133cdbc | -19.93943 | -47.61175 | 2025-04-15 04:40:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2086cbc0-3bfb-3cb6-99c5-805affb59ddd | -20.23415 | -46.56449 | 2025-04-15 04:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44b6b7f8-501b-3daa-8bea-7f0f3360f568 | -21.19382 | -44.93837 | 2025-04-15 04:40:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 103d32c3-7b7f-33b1-afc9-a518dbc195a7 | -18.62166 | -49.19091 | 2025-04-15 04:40:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cc7be91f-b7bd-3eaf-b10f-04b271229d3f | -19.16224 | -55.39488 | 2025-04-15 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 98d0e45b-6422-3c86-b721-f22937a616c2 | -19.70801 | -44.7674 | 2025-04-15 04:40:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9efedf6a-67af-3a0a-8fda-9dd6a2b4eaec | -19.99478 | -49.67861 | 2025-04-15 04:40:00 | NOAA-20 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e5c2c0a3-22a7-3d0c-b636-0cbb972206cb | -19.96531 | -47.65894 | 2025-04-15 04:40:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dfd84c6-86c0-3825-88c4-d18776ed48cd | -23.10909 | -49.8983 | 2025-04-15 04:42:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9d939c4e-71d0-3172-b296-cd72114e5c77 | -23.59255 | -47.43827 | 2025-04-15 04:42:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2305d35b-80fb-3ec0-be75-66119b24dce3 | -24.24247 | -50.74095 | 2025-04-15 04:42:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 05b7c68f-5c4c-3f63-940e-e0ef5cfc0743 | -22.64699 | -51.05216 | 2025-04-15 04:42:00 | NOAA-20 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09ba5eba-8e1d-34f6-a641-1fcffe921dd7 | -30.34395 | -53.76474 | 2025-04-15 04:44:00 | NOAA-20 | VILA NOVA DO SUL | RIO GRANDE DO SUL | Brasil | 4323457 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| b06d3194-6622-3ef8-b5b5-e4e92b74228b | 2.3965 | -61.2859 | 2025-04-15 04:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 626aab52-7de0-3b69-a347-b9fefcdca3ee | 2.3965 | -61.2859 | 2025-04-15 05:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4b7c2351-c7f6-3e46-bd41-fc2e3c8c8ff1 | 2.3964 | -61.3048 | 2025-04-15 05:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8cc00fe0-a26e-3673-aa07-941c4a34d5d2 | 2.3964 | -61.3048 | 2025-04-15 05:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 98145e18-53f9-3ecc-a900-d37eba5537d2 | 2.3965 | -61.2859 | 2025-04-15 05:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| bcef35e3-893d-3ee5-b89b-9c871d553ac6 | 2.39388 | -61.28622 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8ffb4c0-1590-34b6-8a54-904d5e9a2235 | 2.64568 | -61.41834 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f4965aa-30c6-3845-89a8-2f6c6824d22c | 2.405 | -61.29166 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89140abb-4ddb-3204-95b6-b57b50b7278f | 2.39722 | -61.2857 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7accda4-2086-3768-8795-1a3164d2c146 | 2.39442 | -61.28974 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd0947c1-9941-3ca7-a6f2-ef10f253b369 | 2.40166 | -61.29221 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56c01eaf-7ca2-3711-b966-161e155a2664 | 2.4022 | -61.29571 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5d7b59a5-caef-3fff-80e1-3e9646103072 | 2.80472 | -60.05804 | 2025-04-15 05:25:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaf62e89-26fb-3503-958e-49f3a1ea6e6c | 2.79812 | -60.05906 | 2025-04-15 05:25:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a344a63-5f7f-3c46-be0e-9fdaf5375c02 | 2.39108 | -61.29026 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2e9cd87-7cc3-3e71-a438-fbb3fc9da2b4 | 2.38882 | -61.29784 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4092bc95-fadc-33ba-b8c2-62acb223a066 | 2.40446 | -61.28819 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c47251b2-04e8-312c-a39b-50692fa77103 | 2.39995 | -61.3033 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97377b6c-22f5-30a1-a4ad-dac14c0b5b52 | 2.39271 | -61.30085 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 675a0f02-4758-38fb-bc43-31583e137ab0 | 2.39886 | -61.29626 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2bb7edba-df4f-375d-b605-9db52f26ad6b | 2.39777 | -61.28923 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78356858-b41a-3382-a65b-ea24bafaa687 | 2.40274 | -61.29924 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51a174b8-0d86-3c70-9c72-129f172e40a3 | 2.40111 | -61.28871 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4a0535b-89fd-3d00-83b8-14957ca7b0d5 | 2.40002 | -61.28167 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e12fae6-bfa6-379f-8396-2a4e104911c0 | 2.39606 | -61.30033 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1a708f3-e1cb-3a01-abbb-c28a2632c332 | 2.39831 | -61.29275 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c79e3763-f719-3707-95e8-fbe99cd1c5cf | 2.64904 | -61.41783 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe1875d2-cb8f-3606-806e-8fe43ad4e412 | 2.3994 | -61.29978 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b085389a-9706-3602-b25d-039161b6c904 | 2.39217 | -61.29732 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 55193e69-3463-3c26-9c9a-4f9b50097636 | 2.39497 | -61.29328 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e5e80768-76e2-34c2-88c9-39811d31ce31 | 2.40057 | -61.28519 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcea18ad-eb73-36ec-b9bc-d3944b0534b2 | 2.39162 | -61.2938 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 82573f87-18e9-3fa5-8565-d543e8c82d6b | 2.39551 | -61.29681 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README5.md)
