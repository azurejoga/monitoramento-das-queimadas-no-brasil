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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c0d81d-e022-3e45-81a9-76f4fcdadcb8 | -8.07026 | -46.71357 | 2026-07-02 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c269ad6-db0c-3a62-9cc3-856ea3bd5d00 | -12.78255 | -44.48925 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 47c1f3a0-87ad-3da3-9f43-3aa66e1fdf45 | -11.4088 | -49.01171 | 2026-07-02 04:38:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9408aaa-369a-3a55-9ee0-153fe7e5be14 | -10.38003 | -46.67365 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6eeac4cd-3301-3b55-b252-95625aa81e96 | -10.37048 | -46.69601 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 736c7991-bfdc-3e78-910d-73113de6ba09 | -12.51577 | -48.27465 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f322ca7a-76b4-3edf-8f9e-e5c631c03fb6 | -9.18657 | -45.3158 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 155144e5-c3bb-3fd3-9ca6-b20b345d36b7 | -12.22833 | -47.48362 | 2026-07-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df69fa09-b876-355a-b22a-14dee8fb51e4 | -12.86689 | -44.35331 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 7c8c3358-03c8-31ca-98d9-325c5d89ad1d | -10.84324 | -45.05864 | 2026-07-02 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72612385-d724-3636-8801-1091f4680ec2 | -12.049 | -55.45655 | 2026-07-02 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d727118-0527-3913-9b88-8fa7ac947b1c | -12.76131 | -44.49601 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 83fc7eec-4f23-3235-8f40-6bbc238d3d1a | -12.84726 | -44.34687 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4fd3550d-9fac-33e8-a8bf-959f0f02fee8 | -12.7522 | -44.4877 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d07748e5-aa18-3437-8dce-1c6fe59563eb | -9.19746 | -45.31742 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a6a679c-326b-3da2-a312-116355c28124 | -10.37166 | -46.68833 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d9cd72ca-661b-3567-94e2-76b5427c61d4 | -12.78195 | -44.49363 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5b7507d0-46d9-3589-a3ff-08c7de04ac51 | -10.94544 | -43.04951 | 2026-07-02 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 23e20554-ba58-3d4b-84bc-7eb5c96a6e27 | -12.74423 | -44.48653 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dbdc1c28-9b24-3d84-9715-06efa61df9fc | -11.42282 | -56.0544 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0407e1df-c0a8-33aa-8883-34190b5b34d5 | -12.76601 | -44.49133 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| ef0bffd4-fcb7-33d6-a9a2-a937daaa8c3f | -9.60408 | -56.93058 | 2026-07-02 04:38:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 068465a9-c0fa-3830-9b35-ab6e68f34864 | -11.00246 | -47.18803 | 2026-07-02 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1511d4a5-2860-3813-ba61-71dca4718a3f | -13.29763 | -43.55361 | 2026-07-02 04:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dc1ebfc-16b5-327b-a4c1-096712042030 | -10.12179 | -52.09132 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 456ec9de-239e-3bf3-a3dd-521b3ad26180 | -9.25962 | -57.86329 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04ce07a4-206c-321f-b8ff-f306c6098102 | -11.79772 | -56.99989 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 436ed991-a583-3f2c-a501-9cfe6d59819d | -12.76172 | -44.52268 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 0e415214-cfad-39ca-8ca7-87d03accc5eb | -10.37431 | -46.71197 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1923f997-56a5-391a-b23a-5eee93e1c80e | -9.174 | -58.07028 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 570e5c30-0c5d-3b2b-801c-c6a0ced841b7 | -11.43265 | -56.07302 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5224f58b-6951-3b4f-956b-4fddd5b5be2e | -11.8015 | -57.00618 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4fdba9a8-7acb-3098-9887-76d32757de19 | -9.25623 | -57.86259 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf50cb2e-b6ac-353e-add3-ddd57bd88343 | -6.99381 | -46.81735 | 2026-07-02 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84d5604a-ef8c-3e3f-ae39-aeb4457f6d16 | -12.8342 | -44.35224 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 021bebe5-aa0b-3ee7-a501-ef336cb8b681 | -12.8674 | -44.34972 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 2c58ffd5-1c82-3029-8091-795c7a624776 | -9.28083 | -50.21404 | 2026-07-02 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1915c27c-42b8-3a9d-9bc1-66a937bdc4f2 | -12.85179 | -44.34387 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e414806c-f9f7-3cb8-8110-f39a278f6645 | -10.84765 | -45.05459 | 2026-07-02 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b2073f5-21f4-3a7b-bfbc-587dc61916ed | -10.946 | -43.04546 | 2026-07-02 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 496d67c6-8cdc-3ec5-abc6-396ccc7d009a | -10.66608 | -54.52882 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 759070a3-1444-31a6-b835-71675dda6dfa | -11.4055 | -49.01117 | 2026-07-02 04:38:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 694660d3-672f-347e-8174-f655435923a4 | -13.46191 | -47.86718 | 2026-07-02 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5820be25-3a5b-3910-882a-e53f3b303b9b | -11.91965 | -43.39014 | 2026-07-02 04:38:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67f87c18-8480-38dc-a373-f16a39b5b855 | -8.50038 | -47.19691 | 2026-07-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acf104ab-5c25-3d54-aaff-afa109e64663 | -10.40615 | -49.44092 | 2026-07-02 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 862ace0b-de58-34cb-a468-970f96f2674f | -13.73397 | -47.89396 | 2026-07-02 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a15c34c-abdf-30f3-b51d-4eacb16a068b | -10.37316 | -46.69608 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a1184719-1891-3830-9e59-dad868fd06b3 | -7.52106 | -46.61844 | 2026-07-02 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89e56d0a-2a01-3637-a4a5-06796e5ed531 | -10.79122 | -48.22836 | 2026-07-02 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3acbca6f-ba1d-3958-bd93-4d3d483032d7 | -6.83838 | -47.9216 | 2026-07-02 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55041ff1-6193-3c03-b8e1-c95e847e5ea4 | -12.75357 | -44.47809 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 05d41327-6369-3f12-b5e1-b0a4ee6eca06 | -9.24903 | -46.42454 | 2026-07-02 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c31181d9-cbf4-32cf-8c3e-fd84e34d6efd | -11.04658 | -56.92656 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 51201afb-0eeb-3c82-81ba-a21bb4b50c90 | -12.85129 | -44.34745 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 99e4c80f-0843-3b91-9bfe-94c48c11331e | -9.25684 | -57.85918 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05e018f0-6583-3e0a-af50-0fa382826c7b | -7.50822 | -45.85952 | 2026-07-02 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec4fcac8-de5d-3aa4-a8be-dc3302192d50 | -11.00358 | -47.18061 | 2026-07-02 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a47e1712-5f49-3330-90b5-a7af3b7c9831 | -12.41892 | -58.39051 | 2026-07-02 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b44e30f-df7e-3a5f-9394-415825a5542e | -10.67024 | -54.52953 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98247101-6f97-3f62-a489-920e45524047 | -10.37745 | -46.6736 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75a35a75-1c30-3f54-b82a-b6e35da68702 | -11.42194 | -56.05912 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 89866e05-5d56-37aa-877b-c2ac0fd04c22 | -12.76661 | -44.48696 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1254104f-c329-32f2-bbe6-2ad8d92dadb0 | -10.81634 | -58.0174 | 2026-07-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e89ccdea-91ad-3d36-a70f-060a3ce318b2 | -9.60017 | -56.92383 | 2026-07-02 04:38:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ca2ced-d956-3b9a-9ead-ece519ac16ac | -11.4216 | -56.05616 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3dc70b98-d20e-34ae-a773-a725b3a177c0 | -10.37489 | -46.70812 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 8516f3eb-7d88-39d9-a36b-4d64d8ba815b | -10.94971 | -43.05011 | 2026-07-02 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| df6081de-9813-3737-957b-279fb7af24c2 | -10.3743 | -46.68839 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4f0df4e9-fa04-3aac-9691-2c679d2ba16b | -10.37661 | -46.69661 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9c25a2be-fec0-336a-a0c8-25d0d4bbabb8 | -12.76458 | -44.50182 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2b255586-be84-367e-922f-8f0d6e50d295 | -10.37341 | -46.67688 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c746f1c-360e-324a-9eb8-7a777e3011ec | -11.431 | -56.06079 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c00590d-940a-327c-8d00-a94f75abfc66 | -8.65355 | -49.70781 | 2026-07-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f747957a-fdd8-3549-9043-f0f327bc4efd | -10.81694 | -58.01422 | 2026-07-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba6f7873-5698-32ea-8265-3e413ebfcee4 | -11.44194 | -55.91616 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cbfb82f-8e62-37a6-b29b-1bf70d51d69a | -10.37201 | -46.70374 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| ae26539b-9d44-3c97-90a3-8567eaca788b | -8.65575 | -49.71552 | 2026-07-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f7f6085-9202-36bc-8901-1cfc69d02b3c | -9.21133 | -45.32386 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1be55784-29fe-36d1-b273-d395c7a06916 | -12.75334 | -44.49484 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f5187703-d453-3798-8367-dd5f519d306b | -12.75693 | -44.48304 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 645ffcc6-162a-32c6-958a-ffca471de52b | -12.75294 | -44.48246 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c283b207-822e-3f85-9ccc-06d193ae97c5 | -10.37544 | -46.68074 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9161e916-02e3-3c19-b0cb-f685a265fc2c | -13.29336 | -43.55302 | 2026-07-02 04:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dd51206-f9f8-3daf-9020-db6724cd8b69 | -12.75608 | -44.47473 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a6546b3e-ca25-38ba-b389-350009ef78bd | -12.85082 | -44.40909 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89abe29e-5b2c-364d-aed6-ad64b5f9ea6a | -12.85381 | -44.35875 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0b9961c2-b2b4-35b4-aa6c-f8c3565a6f0b | -12.75512 | -44.48174 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| cabc0cf3-41d4-3bc9-ab5a-aba7c43a50b4 | -10.36586 | -46.70312 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6539119-6756-3317-91cf-85083dd0b13b | -11.42812 | -56.07215 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86488f01-aa6e-3648-a91b-a2fe88d61c15 | -12.21609 | -56.56322 | 2026-07-02 04:38:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 212f55c2-d745-3a63-b06a-bbae435f3a5f | -7.28899 | -49.27229 | 2026-07-02 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39f4663c-6ef5-30c6-b828-1bd70a0cc58b | -10.37775 | -46.68893 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6488d181-02ec-345a-a984-7b3e35a97774 | -12.51354 | -48.28904 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a995bf6e-9669-30cc-a239-d61d3acbdd13 | -12.86337 | -44.34916 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| bae44217-b117-32bb-bd77-79c9b923e244 | -11.43376 | -56.07119 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22f54ec3-429c-3cf4-8526-b9dfac409e9d | -12.52323 | -48.28698 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 827db879-2b35-33ce-ad2d-9cf7b6e1774e | -12.84881 | -44.3943 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5478cc9-42ac-3741-a781-c02a4d08b0bb | -12.77797 | -44.49305 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c8f6045c-8827-3f33-9854-a6b59a2173b0 | -11.36084 | -55.43344 | 2026-07-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
