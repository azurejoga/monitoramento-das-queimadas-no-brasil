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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69b88981-4c7c-3f31-b819-b4f54c188309 | -7.21718 | -43.09087 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1cb7590b-8af2-3e91-ac07-ac33e72243bb | -6.73356 | -43.13779 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d7bfd88-f9e1-3d3c-a0c4-9e6b11007dd7 | -6.90976 | -44.00209 | 2025-07-04 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9bef3ac-d010-317f-9026-d913f2261da0 | -6.72849 | -43.14146 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc1a3a2f-68bf-3137-8207-e20221052b44 | -10.64537 | -44.48765 | 2025-07-04 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c92bf0d9-c5ad-3b06-a78f-b61363729633 | -7.22343 | -43.09422 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7f4e21e3-7557-3f51-a201-30b5211b3928 | -6.2935 | -44.21661 | 2025-07-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44bb9339-7e61-36b5-98db-d327f5a18961 | -7.19879 | -43.5853 | 2025-07-04 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cae885ca-f045-3add-b04e-3226aa5ce48b | -7.22166 | -43.09152 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3a091ca2-5517-3038-aed6-7fe9ccbf2006 | -8.44881 | -49.62975 | 2025-07-04 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| be413738-30e0-32e6-aff0-1a649b6806d8 | -6.2834 | -43.67672 | 2025-07-04 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a7723300-71f5-3d30-bb35-20548d4b9e3f | -6.88812 | -43.21525 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 023e2bcc-12c0-3e37-aba7-cd90e303741a | -5.2861 | -45.16525 | 2025-07-04 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fbdc48f-7d88-3e28-a888-ea1a56419ff1 | -7.23305 | -43.09094 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 62bf159e-4364-3d48-9880-fb77450734d6 | -9.79674 | -48.24808 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e48a12c0-c34c-3a29-b8a9-c9e7a9947f6e | -8.63136 | -51.56393 | 2025-07-04 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5068de59-3b40-37c6-a445-cf74fc760d49 | -8.85451 | -47.95354 | 2025-07-04 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb359684-aeb2-38f3-9ffd-d7d6ea6227a1 | -8.737 | -50.2593 | 2025-07-04 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a24e987b-82ef-374a-bdf4-0ef8c9c5ea75 | -5.47781 | -49.57764 | 2025-07-04 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfe5bb58-11dd-31ba-8156-2664cd9a893f | -7.09753 | -49.17123 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2c6ebdac-d8e6-3aa1-b5dd-05385dcf47ea | -8.97338 | -49.85921 | 2025-07-04 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae1eac90-0f75-3814-9cae-530cab4513d5 | -9.76122 | -48.27359 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29c32e8b-a271-3101-be5c-c980524bebd4 | -6.79723 | -44.63432 | 2025-07-04 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f36fd28-d707-3601-91ef-29733c070e30 | -7.30521 | -55.30649 | 2025-07-04 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4cb4cfb0-56ef-3dd0-8ee7-d7afd403da85 | -7.2228 | -43.09873 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3622e324-9141-3d97-bb25-1265ede6e56b | -7.30254 | -45.36622 | 2025-07-04 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cf63de6-df40-3183-a757-a00e3b92ae1c | -6.72431 | -44.33469 | 2025-07-04 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b7d20e7-278d-379d-b4d0-12aaa7358cfa | -6.49952 | -43.64335 | 2025-07-04 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4afe7ea7-b402-31f9-8064-4fec270f26cf | -8.52687 | -54.77225 | 2025-07-04 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a38f140d-fe20-3263-b0e8-1db61e7f1290 | -7.00229 | -45.6124 | 2025-07-04 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9542d38d-8cb1-32ac-a8e3-187b5ac40449 | -6.6656 | -43.17411 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| feadfe7a-9313-35be-a1d6-d1e58589f1cd | -6.49582 | -43.63871 | 2025-07-04 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3a4bbaaa-1bf7-3dc8-abb7-750be260d94a | -5.91595 | -43.44506 | 2025-07-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 693d583a-f720-3a41-831d-a090a8744c57 | -6.60631 | -43.89235 | 2025-07-04 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5e0fd8a7-9735-3e32-96ce-f6ffc1f1ce61 | -9.73506 | -48.35357 | 2025-07-04 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc5c9415-2018-3993-9d5c-73ba85ada63d | -6.74184 | -43.17437 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 99724ed5-4620-3aec-b261-cc8e75ae8348 | -7.96667 | -45.93825 | 2025-07-04 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b30c5d4-bebd-32d8-bbe3-ac65a1a760c3 | -7.6583 | -44.34498 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c9bec35-f21f-38ac-b828-25cb8a6a34f2 | -6.587 | -44.19814 | 2025-07-04 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14d6d5b5-4143-359c-845d-d8dc0eb88e9b | -9.847 | -46.47635 | 2025-07-04 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7c2745a-9874-3225-8117-6d97da47a04d | -8.52294 | -54.77157 | 2025-07-04 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e795077d-d0ac-3eae-92a7-1daf403bcf57 | -6.7469 | -43.13967 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70821b30-0c1b-3283-8f64-c084705415ca | -7.94237 | -44.84803 | 2025-07-04 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cfb7f14b-a89c-31e4-9d44-b668f35f0903 | -7.30937 | -55.30718 | 2025-07-04 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ad4a80a-52cf-3723-b225-65758e0a62c7 | -7.07811 | -43.2096 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6344f4a8-1cde-3b3b-81a7-532d2b56621e | -9.73268 | -49.05827 | 2025-07-04 04:38:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4b611f9-4518-36a6-a8cb-7f19f7fab04b | -8.4455 | -49.62922 | 2025-07-04 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5795ed97-a40b-32df-b03a-ad0e6a14da5e | -7.19866 | -43.43065 | 2025-07-04 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc865ea5-1aad-36a6-ae1d-7ec192fd88d8 | -7.09421 | -49.17072 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7294b768-00a9-3a6d-844d-7ab18cd4a160 | -6.66516 | -43.17274 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e86702ed-8c5d-3ab0-ae90-06e5f3c0cfdb | -7.10871 | -47.85149 | 2025-07-04 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4abd6734-ae0d-3725-878f-c5be0985c605 | -6.27917 | -43.67594 | 2025-07-04 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1e5a2d03-6a55-3739-a5e2-b376dcec205c | -6.72676 | -44.37566 | 2025-07-04 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c739aac4-acf6-3583-bab4-00ba53f189c7 | -5.75101 | -46.08417 | 2025-07-04 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48ae9cfd-e09f-3a95-8533-c338b1f4a5c2 | -8.30408 | -49.07631 | 2025-07-04 04:38:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f781809b-d4df-3178-90c2-a3bee21a4f98 | -8.99694 | -47.44564 | 2025-07-04 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 950a623f-8aeb-39f0-8565-4cd88b8ab559 | -5.28641 | -45.16732 | 2025-07-04 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 799573db-7f03-3708-a62a-b5145b1f8cf2 | -9.08367 | -48.33232 | 2025-07-04 04:38:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 4aba315e-cb7c-32d6-81f9-f48e193cf909 | -9.58816 | -46.75971 | 2025-07-04 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a03d4db8-0e28-3b04-8ec7-4552c965a155 | -6.01313 | -44.5316 | 2025-07-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55f5d6cc-df6f-3cf6-b00e-1878aaae9bf7 | -7.62193 | -45.37445 | 2025-07-04 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 51bf5866-d526-3bf3-bdb8-f96c38270db3 | -7.7699 | -45.15765 | 2025-07-04 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda2c266-a1de-3858-9009-60da5e12ec2d | -9.87481 | -48.61062 | 2025-07-04 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96014849-3dd4-307f-8ecc-e4e3416cb305 | -6.6618 | -43.16922 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cd73114a-b4e6-3ff2-8ded-f20da30847d7 | -6.84542 | -44.94034 | 2025-07-04 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4362014-9b4e-32df-b215-5c91d01e906b | -8.99754 | -47.44165 | 2025-07-04 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc5875c6-ba26-300c-aae2-24ae0bfa42f3 | -10.47487 | -45.11123 | 2025-07-04 04:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33dd872a-b8a1-3507-8080-37de0f304d89 | -7.16292 | -49.5119 | 2025-07-04 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45737539-d520-3f24-b5fe-89e69149701b | -8.66586 | -45.75142 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b20f02a-4011-3f80-8f43-fee365b1d090 | -7.23178 | -43.10004 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d861525b-7a64-32b5-bb03-916a5069f9c1 | -6.9981 | -43.54289 | 2025-07-04 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 633365c7-39c8-3af1-9e8b-1d6ee65b0556 | -8.81226 | -48.48381 | 2025-07-04 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1778af3-d884-386a-b72f-0d812b8cdf28 | -7.23241 | -43.09549 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a94476f8-9fab-38c0-a2cd-85b46286b12e | -8.66723 | -45.75395 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e1237743-31f2-31e4-8611-40e9e787ac5c | -7.09367 | -49.17419 | 2025-07-04 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5d3a6df0-6fca-36c1-be74-2311b3e239ff | -7.22792 | -43.09487 | 2025-07-04 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| af3fedc8-c469-37c1-89cb-4f0303ed9e70 | -3.38117 | -43.12063 | 2025-07-04 04:38:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea99b65c-8f0c-3396-b753-645e76b0736f | -6.66625 | -43.16975 | 2025-07-04 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 495d6476-3968-3dbb-8f15-826c3ac6a076 | -6.6112 | -43.8941 | 2025-07-04 04:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d5ba9a3a-61ff-3fe3-b9c9-6f2b118cdd66 | -10.5586 | -49.1337 | 2025-07-04 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ece879b4-4789-3dff-9999-30659edac1c2 | -12.13312 | -44.90904 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85b89fee-820b-315f-af4b-ed64b21aec2d | -16.9486 | -46.08502 | 2025-07-04 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f8deac4-cb84-3fe4-b6ed-f7b1fb7b8286 | -10.25663 | -48.14849 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c30242a-a4bd-3df5-8979-571876192649 | -12.16972 | -56.54573 | 2025-07-04 04:40:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e915eb8-8b74-322e-b7dc-6eec6bfcf037 | -11.9225 | -45.37704 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd3c9eed-b664-327c-83cd-99db00d0c8a5 | -16.24201 | -52.90956 | 2025-07-04 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29f3dcaf-6e2a-361a-a05e-65e1eb33a3ce | -10.05226 | -59.10982 | 2025-07-04 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 319895ca-c0b9-34ea-93ab-eef6a6847061 | -11.86902 | -44.86014 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48705b9d-aa54-32cb-9292-d59c1e87cfce | -9.89923 | -55.52683 | 2025-07-04 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 249b1914-e05d-3645-bd05-0ff61d0931cf | -12.16615 | -45.5318 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 168d1516-a83e-373a-b3a3-84248e1b4a8f | -11.44537 | -45.11584 | 2025-07-04 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0d5452e7-82c6-3b2b-a8a2-0b8c31ec9589 | -13.40287 | -47.83471 | 2025-07-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 908cc3be-49d0-3110-a451-434e1b016013 | -18.04043 | -46.04676 | 2025-07-04 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b1e90e6-b7a2-3f24-bbd9-51d1ad19018b | -11.92661 | -45.3777 | 2025-07-04 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cee9b380-db85-3bd8-b9e7-a87cc5a0f34f | -11.5385 | -47.87033 | 2025-07-04 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54dae0c6-5e0f-3f83-84a2-21b78a32643f | -10.75854 | -48.25279 | 2025-07-04 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1328eac5-5f69-3349-90f7-5310fffe79ad | -14.88862 | -48.36872 | 2025-07-04 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4c3edb8-2352-32de-9b05-bda33106c349 | -14.61213 | -48.25016 | 2025-07-04 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b0aadef-272a-3e06-a578-7291546c9d82 | -10.25837 | -48.15224 | 2025-07-04 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a406ce10-64f7-38cd-8217-8fa953fd0158 | -10.9547 | -48.2255 | 2025-07-04 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
