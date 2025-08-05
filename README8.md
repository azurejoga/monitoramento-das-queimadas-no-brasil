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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d08d5eb-2745-3185-9354-6d45f1c86cd6 | -8.74156 | -46.42 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f08391d5-509c-3a60-944e-5ee628c45a85 | -12.71501 | -48.09253 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12a39f8e-0659-389f-9fc3-8a8f3f7abec8 | -8.85011 | -47.60718 | 2025-08-05 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b95b255b-33ed-353e-8028-d3cc86b955a3 | -11.81335 | -44.262 | 2025-08-05 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41d091dd-a0e3-3799-adc7-a114b7a3a97c | -8.00762 | -43.22221 | 2025-08-05 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 391e4598-e724-31e4-83e8-32d74db98a17 | -8.01409 | -43.13242 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad4b9a9c-4435-32a3-ac46-4a9c8da73a47 | -12.70553 | -48.08351 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ed8115e-9332-35bc-889f-8d857410de14 | -6.91163 | -43.90128 | 2025-08-05 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44af059f-bb69-3bea-bdec-2a3375bb294a | -9.05686 | -45.0651 | 2025-08-05 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7536b75d-f6d4-3fe5-87a1-74cb3660cce1 | -11.91629 | -44.9492 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04732ea4-bd0f-3743-b812-2a6caabe8412 | -7.90942 | -45.53604 | 2025-08-05 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22606f07-7c57-368f-9858-f980221e7353 | -12.68439 | -48.12798 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37bc0dcf-b1e8-3bd5-8792-2dd71b5c8529 | -11.92362 | -44.95979 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 730c0356-031f-303b-8c5a-37eafd6482e9 | -8.00831 | -43.21813 | 2025-08-05 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 7af0d095-52ec-344e-a509-55f71278cc0a | -8.00337 | -43.22142 | 2025-08-05 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| dad89614-dcb0-3ab6-940f-08281706411b | -12.58839 | -45.07032 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dcbedaf-f5b3-389c-ada4-6fd5ad0866b9 | -7.11339 | -47.84232 | 2025-08-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f2bfce17-3350-3a01-9824-efd2b0f68f68 | -9.61921 | -43.85572 | 2025-08-05 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c61c9f12-d0e2-3866-a2fe-7617822f5375 | -6.97242 | -42.86941 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| ceb1cfeb-7654-3b6e-8ee7-13644b528aff | -11.03824 | -47.61501 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e89bf4c-cb79-3d8c-85e2-267ad7e74db2 | -11.74818 | -47.54544 | 2025-08-05 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0d4b472-6dc3-3437-8e76-252a2428459f | -10.91043 | -48.35929 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b31a44b8-e3e1-3c44-80a0-ba53d7807bd2 | -6.44482 | -42.85747 | 2025-08-05 03:49:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 196613ae-f268-3b84-b97f-d6e6cf765cb8 | -12.33803 | -46.04487 | 2025-08-05 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92190a78-02ef-32b8-ae31-58335e9dfca2 | -6.23597 | -45.85844 | 2025-08-05 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1faae1a8-2ec4-3aba-bda5-02d057bd0fa0 | -6.7388 | -45.30413 | 2025-08-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d0dd0e6-d105-3e88-9d41-dffad9e3eb26 | -12.71529 | -47.79132 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 543ce340-3422-36fe-9a9a-3627eb70f578 | -9.16519 | -40.59964 | 2025-08-05 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dac3777e-b494-3b9d-911a-b1f8120f4ff3 | -8.25301 | -45.06885 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbff78d7-f881-35f5-b38d-ba6d5dbf0cfd | -6.70446 | -44.09135 | 2025-08-05 03:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8508dd25-7232-3fb1-bfd0-7af86fc44436 | -12.5509 | -44.7262 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20e3dfde-5dfc-3c4f-ad31-dd5049910e01 | -7.53605 | -45.05325 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc7b38bf-f0a4-303d-839b-7d4722b27e85 | -11.81261 | -44.26611 | 2025-08-05 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a27e40f-042f-37b2-906c-8c510406a4e4 | -8.94829 | -46.73852 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b1a80c4c-ff4d-3fda-a5a7-8bd68da42c0c | -7.99936 | -43.14221 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| c85e30e9-c0b3-3c84-bfc8-849b56cddbcf | -8.9442 | -46.73104 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 239b7b12-8fea-31d2-b208-fa998dc53e70 | -12.98931 | -47.46421 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d1b9115-ef96-36db-8209-f96b180917bd | -6.67884 | -49.79862 | 2025-08-05 03:49:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d9764fb9-b409-3c22-9144-18362f5a8fad | -10.4547 | -44.35826 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cd756d8-a3c6-30a4-ae02-3026d905aa6d | -8.26273 | -45.06686 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a56f1d16-981c-3b07-8eb8-4f112b49aab8 | -6.57794 | -43.49085 | 2025-08-05 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6addb78-964a-3ccf-b664-98614862a83e | -11.92152 | -44.94582 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 752eebec-b983-3e6a-be9a-ac9a015edc5d | -12.71343 | -48.1006 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc7fcfb7-a323-370b-9a03-ec144f6f4124 | -8.23084 | -45.05402 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a811764b-fa61-378e-93cf-e607ec4e5d90 | -12.71966 | -48.09753 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d045cb3-c211-3222-b210-4b61173dc7b7 | -7.56726 | -44.87627 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fbf45c8-56f0-3287-a1cd-57a90db234ff | -12.51584 | -47.18549 | 2025-08-05 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92eb8f75-bdb3-34de-8824-01fc5b700fd3 | -10.34496 | -44.91075 | 2025-08-05 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceb65bda-39ae-3da3-b2a3-3619f7ff7e55 | -8.93961 | -46.73336 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 76263c44-db72-3822-a7ac-ee7b58801dc1 | -12.69215 | -48.12271 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04b53f65-4888-3722-b63a-25e5e1c1dd75 | -10.90326 | -48.36602 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f46548c-de6b-3d85-a52c-84cda0efaef1 | -13.37327 | -43.75589 | 2025-08-05 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66243861-90fe-36fa-ac35-9eb018c4dd63 | -11.91999 | -44.97991 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77c73a0f-6298-3563-81ca-442da4cfd198 | -10.91162 | -48.36242 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ba170d0-9ccc-313f-9ac4-5179d7fbfd58 | -10.4488 | -44.36812 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe719fc4-4039-3008-ae53-9d9272f55b1d | -6.97308 | -42.86551 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 031909a2-32b2-3a52-95ab-1eb507c9d865 | -7.98673 | -43.16506 | 2025-08-05 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| bbe78277-c954-3d83-9c2d-b2194fbfe05a | -10.45415 | -44.38651 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1dcaf2f-0edd-3be1-b765-584e201921bd | -8.26753 | -45.06768 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d7cd1c1-e9c6-33f0-aab0-9ee43275101d | -8.26848 | -45.06239 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad047c14-a1ee-39b6-81ab-70eb80dcbae0 | -12.54615 | -44.72259 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a98a8860-7048-3fa2-99f8-fec8fbec45e1 | -7.85401 | -46.73495 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 993ddd22-7a4f-37bc-a5bb-219ed1e689be | -10.78666 | -46.64556 | 2025-08-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3b713f7-be2a-333b-a835-b2b72869dfbe | -10.47272 | -44.38459 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dedffaa1-c52a-375f-98c6-1d14d4aadc34 | -12.5505 | -44.72337 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdce9035-04b2-3a58-9703-9f244efcd354 | -13.22573 | -46.84508 | 2025-08-05 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28b2f100-3168-3a5a-9923-b87417a18be7 | -12.68634 | -48.11774 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59c4dde4-5699-3826-96cc-2f686c9553c4 | -10.46746 | -44.38848 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0d8e598-9650-3ed2-805c-9934d2576092 | -11.91551 | -44.95354 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9f9d2bf-da83-35be-82a9-166f015f8baf | -12.71994 | -47.79589 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ad17ad3-fc6f-3ea6-9732-fcdf8d22fc35 | -11.80907 | -44.26123 | 2025-08-05 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 208501c2-8660-3874-a68a-c7e04eed5aec | -8.93768 | -46.7366 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d93cb0be-5105-3e1d-9a4b-4a72f5f055ac | -11.74894 | -47.54148 | 2025-08-05 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17aeb5fa-9163-38dc-9db9-02f8c9a52b4c | -8.00427 | -43.13896 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a1c1571b-4bf0-3d41-b943-c594474b9224 | -7.53362 | -44.87078 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a3b3f70-c475-3f9a-87dc-fb82b6954426 | -12.64657 | -44.49548 | 2025-08-05 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cdd3275-6713-3dfe-9003-8632faa99425 | -7.78125 | -45.21937 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25074e9c-3bae-3d10-8f3b-7695a975d77c | -12.68136 | -48.12022 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c8026e1-4d9d-3468-b3e0-1008df233afc | -11.74874 | -45.0074 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e83f018b-d9ee-31ef-8e3d-466223888837 | -10.78727 | -46.6424 | 2025-08-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef10bd86-becd-3b46-a9f3-a138fa3ad871 | -11.78473 | -44.99803 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 691b9913-9980-35f9-90d7-97e77310011c | -12.68971 | -48.07811 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7948f324-b7a8-3bc8-b289-561296f5e44f | -11.78829 | -45.00395 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2d0ae87d-fd8b-3c3e-b271-c04cb4c3bad3 | -10.44437 | -44.36747 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61d5a424-bfd3-3032-8f8b-e5c853b517c2 | -7.99869 | -43.14615 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| bcc2ba2b-d908-357c-b588-7f0bf355700a | -8.71888 | -46.4263 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa5241bc-af4a-35c7-9e2f-860ea473db23 | -10.34127 | -44.90503 | 2025-08-05 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 033f535a-c2ee-3fa3-9aeb-49dc57faff54 | -8.9489 | -46.73526 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 05912970-76ba-3bfc-a046-49a6fa2094ab | -11.15463 | -49.7039 | 2025-08-05 03:49:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e124c514-b138-3dcb-b6a8-f068cb382d0c | -12.73128 | -45.07594 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54658587-c0e2-3214-864b-bbbd2e0f48a2 | -12.71579 | -48.08858 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edea3388-2a14-3b66-be28-64f110bdc528 | -9.0625 | -45.0609 | 2025-08-05 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca73b067-7c6f-3099-b5a4-935f48c2d477 | -7.56834 | -44.89822 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b3d340a-7d84-3a03-985c-7a75f059d7c3 | -11.28089 | -40.97626 | 2025-08-05 03:49:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3f783582-cd2a-3ab5-8496-37c3063670c1 | -7.99238 | -43.15754 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5efaff54-6979-3430-a376-fd413d160951 | -6.98469 | -43.3889 | 2025-08-05 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f02244de-10fe-3c0c-8a87-4316547db240 | -8.95299 | -46.7428 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 445414e4-5cdf-389c-ade9-af846cd250cf | -6.76553 | -43.79395 | 2025-08-05 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d0d4114-9b3e-3870-baee-73ab1a45cdca | -7.39134 | -44.64332 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 01dcfcc2-7803-365e-aac0-6e93be574035 | -12.6938 | -48.07859 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README9.md)
