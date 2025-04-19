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
| 06894b0d-447d-35ad-a074-76a1db0e8a5d | -20.47858 | -53.67556 | 2025-04-19 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31bcc13d-d8ee-31d9-bfb3-41e3cef0f8a2 | 1.99136 | -60.86749 | 2025-04-19 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 732b96e0-785c-3494-962d-2c44be9f623f | 1.9921 | -60.87231 | 2025-04-19 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 717df811-2e0a-377b-8ca8-5a909c989614 | -7.06798 | -44.38167 | 2025-04-19 05:01:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5328c4e-da0e-3027-8c26-edd92fa3b15a | -5.79864 | -43.61682 | 2025-04-19 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59e8a33b-c8f3-3577-82d1-98b20fe42b59 | -7.07555 | -44.37223 | 2025-04-19 05:01:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c8789353-4aed-311b-956a-f11894a77d95 | -3.43878 | -51.24715 | 2025-04-19 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f8d961e-a998-37f4-99a9-07f48551f7fd | -6.2184 | -55.64202 | 2025-04-19 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c438774-7c96-3d57-a488-bb19d69fd817 | -7.08041 | -44.38313 | 2025-04-19 05:01:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69b4b6c5-30ef-3d8e-a86a-e2f5660cb4f5 | -5.16006 | -45.10853 | 2025-04-19 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04d07fdf-ca69-3cd0-ac92-6c9d79bc502c | -5.7915 | -43.62141 | 2025-04-19 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0064b1bb-bc7a-3d82-b3d5-3484c5954428 | -5.7979 | -43.62226 | 2025-04-19 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b22dd00-5dfa-36f9-bf9a-7063a77f7551 | -5.93748 | -44.46867 | 2025-04-19 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59a70ea4-2aac-316c-8894-6b8c95d08b4c | -7.07486 | -44.37739 | 2025-04-19 05:01:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64e25cbc-0e11-3b72-8a8a-935283a2c763 | -11.78219 | -63.03498 | 2025-04-19 05:04:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da949d3f-9c0f-3133-a8b4-4c6a378dd20d | -9.91912 | -59.91039 | 2025-04-19 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9bd234a-2352-3935-9aa5-cb602adf34c2 | -9.93226 | -63.47317 | 2025-04-19 05:55:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38e7b356-6de4-3235-91f5-d07de25070f3 | -12.40458 | -57.6654 | 2025-04-19 06:35:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ca5e78a3-a58d-3a0b-a0b5-05c8ffe77ea9 | -6.5631 | -51.1126 | 2025-04-19 06:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 87a7c2e1-8a58-3973-9fdd-47ac754442ce | -6.5631 | -51.1126 | 2025-04-19 07:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5ea0e565-035d-38a5-a669-216ef102d842 | -10.3378 | -36.77738 | 2025-04-19 11:34:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 8dffaaea-303e-3784-a90f-f8a7b81211b0 | -5.86429 | -35.69688 | 2025-04-19 11:34:00 | TERRA_M-M | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4331e58c-1cc2-3842-9574-8a839b69421e | -10.33501 | -36.78173 | 2025-04-19 11:34:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| f930aabb-6afa-30c5-9a12-c7a37b572984 | -5.87401 | -35.69824 | 2025-04-19 11:34:00 | TERRA_M-M | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 663e1b1a-c97d-35f7-90b9-246967cb6dcf | -11.1467 | -39.1378 | 2025-04-19 13:10:00 | GOES-19 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 545ef015-cbc5-3a30-8df9-9e46f3537599 | -11.1467 | -39.1378 | 2025-04-19 13:20:00 | GOES-19 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 60456c21-91a8-37ea-bccb-b00e2d669b5d | -11.1467 | -39.1378 | 2025-04-19 13:30:00 | GOES-19 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 135.2 |
| ee04754c-315c-382b-b267-ce9b3ff7b749 | -11.1467 | -39.1378 | 2025-04-19 13:40:00 | GOES-19 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 152.3 |
| 8cfa18ac-0563-301c-9c18-9437521dcdb4 | -11.1467 | -39.1378 | 2025-04-19 13:50:00 | GOES-19 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 149.9 |
| 4431917f-a3ba-3740-a7b8-0a16cd0b290d | -11.1467 | -39.1378 | 2025-04-19 14:00:00 | GOES-19 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 151.3 |


