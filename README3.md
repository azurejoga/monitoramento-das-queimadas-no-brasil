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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 165332ea-7070-3d82-bc75-033d40ad07e9 | -7.2025 | -43.1171 | 2025-05-27 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| ec75928a-ccae-3e76-a848-4b153085f161 | -7.2214 | -43.1153 | 2025-05-27 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| a5da6b07-3f37-39a8-b1d1-ee21d2dea8db | -18.8284 | -53.6067 | 2025-05-27 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 52.7 |
| be7a2e0a-b06b-3732-b3cb-3bc9b840426d | -18.8479 | -53.6251 | 2025-05-27 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 162.8 |
| f2cb4175-63db-3acd-a080-6ce0a7de6138 | -18.8679 | -53.6218 | 2025-05-27 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 120.3 |
| b1e5c502-d18f-3948-a390-649917f09a6f | -18.8684 | -53.6003 | 2025-05-27 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 01ba1915-832a-3f1e-bad8-d24e6194af3e | -18.8484 | -53.6035 | 2025-05-27 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 162.7 |
| accd9492-10fc-3593-9441-7d75c885bd8d | -7.2025 | -43.1171 | 2025-05-27 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 72ee3332-6b52-3be1-950a-c566b2dac8ae | -18.8679 | -53.6218 | 2025-05-27 03:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1afbdd2a-372a-3203-b709-a05ad97064f4 | -18.8284 | -53.6067 | 2025-05-27 03:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5d9d1a6d-1ee8-3c80-a84e-e5eb66516d43 | -7.2025 | -43.1171 | 2025-05-27 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 39d89bab-8705-3aea-82e9-afd6b427a9a8 | -18.8684 | -53.6003 | 2025-05-27 03:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4114d911-3661-335e-a2da-020ea9e9c8ac | -18.8484 | -53.6035 | 2025-05-27 03:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 242.5 |
| 42ab412d-6c86-3de8-b54c-43af46fb0904 | -18.8479 | -53.6251 | 2025-05-27 03:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 7090da55-3c74-3c0a-91db-df72d7491dc1 | -18.8484 | -53.6035 | 2025-05-27 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 291.6 |
| 16dd3a90-67a1-38ea-a273-aa71d68abc0c | -7.2025 | -43.1171 | 2025-05-27 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 75e10d43-8299-3d42-b672-bfbe4d32e3e4 | -18.8684 | -53.6003 | 2025-05-27 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 250e4e81-f1ff-3fc6-8e08-c8ac345c414a | -9.4964 | -40.3088 | 2025-05-27 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.7 |
| ce49da84-681c-349a-9598-0ece47aa3890 | -18.8279 | -53.6283 | 2025-05-27 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 1c4aa115-f255-3075-9dfb-76410608f5ef | -18.8479 | -53.6251 | 2025-05-27 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 317.7 |
| a1e0a655-6946-3942-8b0c-17f67c9c2bbc | -18.8679 | -53.6218 | 2025-05-27 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 60958cba-f186-3bff-8f0e-50ceefd8b986 | -18.8284 | -53.6067 | 2025-05-27 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b899a6e2-dc6c-3e07-9d59-4c20a9607021 | -7.2025 | -43.1171 | 2025-05-27 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| e63e5a2a-5b49-3f0f-bda9-eebb177a3913 | -18.8684 | -53.6003 | 2025-05-27 04:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 83.8 |
| cfefe7c7-d646-38d1-93ad-eaf42e122f9c | -18.8479 | -53.6251 | 2025-05-27 04:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 237.1 |
| e20ec30b-1c94-3080-9896-037370f00eaa | -18.8484 | -53.6035 | 2025-05-27 04:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 84ad16ed-c9a0-3c50-a51a-d8121904f371 | -18.8679 | -53.6218 | 2025-05-27 04:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 4286edf5-e6ac-32e5-b1ac-92f43e144f34 | -5.06945 | -37.71621 | 2025-05-27 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3f8a54e-e0d1-31f9-8aa6-c72124e854f0 | -4.1739 | -47.53282 | 2025-05-27 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b72922ea-7d74-3e29-978b-51240ce26bf0 | -5.23791 | -36.20042 | 2025-05-27 04:00:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 86622e1f-9325-3208-be3f-1ab5aee494cc | -5.96067 | -36.10077 | 2025-05-27 04:00:00 | NOAA-21 | SÃO TOMÉ | RIO GRANDE DO NORTE | Brasil | 2412906 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e694fe76-92e2-334a-a4a4-82aaa40fe704 | -4.72012 | -42.67199 | 2025-05-27 04:00:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12b31a63-3734-3d01-807e-b3a09b77959e | -3.4257 | -43.16435 | 2025-05-27 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14f4b656-ee25-3806-8967-6d7f4e0feeb6 | -5.96134 | -36.09631 | 2025-05-27 04:00:00 | NOAA-21 | SÃO TOMÉ | RIO GRANDE DO NORTE | Brasil | 2412906 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a8b460a-9cc5-3875-9231-7bbea621f78a | -6.22461 | -43.35207 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31c31157-b7c7-3559-b38a-dccaf3a05cb7 | -12.27533 | -44.60172 | 2025-05-27 04:02:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06d9e537-2797-378e-872d-f5978b275036 | -6.64725 | -43.20371 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 472a8526-82aa-3d38-aef8-b1fe78a537bf | -7.21422 | -43.11365 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 22f36bc4-f05e-325e-8f47-c0a7a5886789 | -12.42227 | -49.98083 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7bc2dcd-57f9-3fc5-9db7-4683e23ff291 | -8.43253 | -46.66339 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a3585c7-2e15-3e1b-96dd-dc5a01271955 | -7.2022 | -43.12006 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| d68872d4-1225-3e36-8f87-2958a5f2ae1b | -12.82975 | -47.38215 | 2025-05-27 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc7b9bed-83e6-3057-b3eb-6c1685ac3981 | -9.3848 | -48.42598 | 2025-05-27 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbef3a15-adea-39d2-99fc-53ab74a330b6 | -8.75133 | -49.74776 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28377677-1cdf-3118-bc64-f2d89762c227 | -7.60068 | -43.41305 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e33913c5-8ab2-3ad9-ba86-765ee7c455ce | -12.08123 | -47.35373 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26b8b6a0-cff5-3432-8046-e3bd7ee05ca1 | -7.48837 | -43.36599 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70e0b0fc-cb13-3219-81c4-b6f54c45a065 | -11.57384 | -47.63069 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d9de253-6053-3394-920c-67b64c6442d4 | -8.0219 | -49.68797 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23b6f447-6cc2-351b-9c63-d06aa40ebf0a | -8.42937 | -46.64688 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06307a46-5243-3f29-bf0e-c124c9416909 | -10.26905 | -46.54281 | 2025-05-27 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 281afee5-ec67-3a42-bb73-bdf82d8106a8 | -6.64714 | -41.99749 | 2025-05-27 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13e8d974-10b7-34c9-8ca0-fd214a92e647 | -9.38576 | -48.42062 | 2025-05-27 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e02406c1-d1ec-33bc-b740-9a01122cdf1b | -9.38189 | -48.41452 | 2025-05-27 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77870229-2b40-32c4-8194-24423148d06a | -7.55796 | -43.36888 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92136fd1-add6-3d0e-83e0-545c7e4100a5 | -6.65085 | -43.20432 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a224c2da-2580-3a64-ae6d-0b43e11e7ba4 | -8.4337 | -46.64765 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ecf9f337-04d0-3cc2-8401-32e52478f7dd | -12.27024 | -44.58766 | 2025-05-27 04:02:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6196e640-e9b1-36b7-bc55-b97de724318e | -8.01999 | -43.20519 | 2025-05-27 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3f194170-1e62-304a-b520-c39f44bc6faa | -7.55371 | -43.37241 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10fe0d32-00dc-37f0-9aa6-cb92d7f68684 | -11.14087 | -53.93274 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3d515ee-2fe2-36a7-bffa-426807e8d401 | -7.22558 | -43.11127 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fcb9a622-113c-3cb5-b5a6-7aae69695109 | -12.3605 | -40.40255 | 2025-05-27 04:02:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50472bd5-65be-3278-bda2-fe8231bbbf46 | -12.83325 | -47.38697 | 2025-05-27 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a70aee10-da43-3d04-9702-fac64266eeea | -6.98454 | -46.31383 | 2025-05-27 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52c8c95a-e1c4-34b0-bdc9-a4a0b601a813 | -10.81964 | -54.02759 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d62f0135-7436-3069-984c-4369807e09af | -12.06841 | -47.35146 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d469a786-02df-3672-b4a9-fcd974ba2f9f | -8.43007 | -46.64272 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48daba2b-482c-3b0a-a429-fc8f48a125c2 | -6.1615 | -48.06201 | 2025-05-27 04:02:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8b921e34-8df5-3cf1-96bf-cde41dfd9f75 | -7.18034 | -45.10318 | 2025-05-27 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f06c408-5bd5-31f6-ad86-146a821be864 | -9.9771 | -42.50854 | 2025-05-27 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aeb224f8-f9a8-3fac-9d50-7b59f5d1427c | -7.54804 | -43.18181 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfe79b42-a5bc-311f-8388-8aa821f74cf2 | -11.86841 | -52.25616 | 2025-05-27 04:02:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a4b56ce0-92ff-3a66-a7db-e0fb455e6779 | -6.98314 | -46.31361 | 2025-05-27 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 866f6d8f-2932-3df2-afa9-c388ddc1e311 | -11.56197 | -47.44006 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 260afff8-7d49-3464-9c05-a0b6d6be2da8 | -11.5664 | -47.4483 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 34817c5d-8639-3c21-a9ea-149d15e7ccf0 | -7.60274 | -43.40056 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74806020-5ed7-3ded-859c-0b149aa2feb2 | -6.64657 | -43.20788 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc4881b2-3240-3ba0-b6db-3798f735eb7b | -9.49543 | -40.30517 | 2025-05-27 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 4871fb70-233d-3580-8c81-3d13634c2747 | -7.60975 | -46.65127 | 2025-05-27 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aa48436-1f1c-3784-9527-505d3d594f39 | -8.07317 | -34.97567 | 2025-05-27 04:02:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7b635bab-de7e-3ee8-8ec1-421bedcc7a50 | -7.66933 | -46.10389 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fdc75e5-3764-31c7-a0ac-740b38b1e15b | -11.56717 | -47.4441 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b523631d-4726-3af0-9151-0e83ae5fa9b1 | -7.22981 | -43.10776 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 0858719d-0c21-3df8-9ad5-06b0d1b2308d | -8.02327 | -43.18492 | 2025-05-27 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 693234ae-e735-3ba9-8271-00fa79acdb69 | -7.15691 | -47.13998 | 2025-05-27 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3490abd9-0b1f-3118-828a-7a6700c6a98b | -10.71689 | -49.62674 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2021507a-5c98-3618-b242-a50ad91954b6 | -9.50161 | -40.35247 | 2025-05-27 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ba300395-11bd-3b8e-8489-2722fedd4407 | -12.82903 | -47.38616 | 2025-05-27 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5858dd39-1dff-372e-9614-09053e794523 | -12.15947 | -43.2056 | 2025-05-27 04:02:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a2142a40-cd6c-3257-8d7c-0b8b9d206550 | -12.27309 | -44.60062 | 2025-05-27 04:02:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b38f638-4e78-33fa-b33c-eabda1976015 | -7.16239 | -43.31653 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4a02da3-0d55-39ca-922b-689e3cfaafc1 | -9.50215 | -40.349 | 2025-05-27 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 988ba9c8-70f6-3f1c-a84a-e3575e81e354 | -7.23337 | -43.10834 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 656e26db-9939-3dd9-ad14-001c527cace2 | -12.03288 | -51.59837 | 2025-05-27 04:02:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10480f0d-fe2e-3396-8d8a-54b045e52ccb | -11.80315 | -44.26683 | 2025-05-27 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dc3030a4-e3e2-39b9-bf8d-f60352f53eae | -6.50264 | -47.48838 | 2025-05-27 04:02:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0e39e74-4bd3-3c4f-b2e3-3b996f4f8070 | -7.48547 | -43.36126 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94195608-6fda-3d5e-b49d-75d0a79e5531 | -6.63508 | -43.21027 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 49b0fcdb-7c9c-34e5-8266-1344abc93135 | -10.82088 | -54.02147 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README4.md)
