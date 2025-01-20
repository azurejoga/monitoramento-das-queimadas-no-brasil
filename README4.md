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
| 234d989e-8d17-3d24-9be3-7049cf7e8ef3 | 4.99806 | -60.30467 | 2025-01-20 05:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df1a11e-5560-3dea-a76c-6dd850fd185a | 4.13739 | -59.99208 | 2025-01-20 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18197e21-9ca0-3a39-97c4-afd028977f44 | 4.77338 | -60.73037 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c1d6cbd-18f1-308b-b8c0-4c76a9e45b80 | 4.1382 | -59.997 | 2025-01-20 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86579775-a29d-3bc5-bc9e-e33c5928a78e | 1.35038 | -60.02539 | 2025-01-20 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c704e57e-8dfa-36ba-bef7-68743743a36f | 0.70127 | -59.68721 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c3a9440-e1a4-3e8a-8932-1e64b662eaf4 | 4.0934 | -60.96591 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 57c1c871-a220-3491-8892-3e975af197a4 | 0.80842 | -59.90079 | 2025-01-20 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0f98632-3ccd-3b7d-89aa-35712b3e0371 | 3.91465 | -61.00865 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66be5704-477d-30a2-be0f-9f8a607ac7bf | 3.87383 | -61.21262 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09a386d7-9740-3554-9887-f2a816c4b294 | 1.00694 | -60.57426 | 2025-01-20 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5908905d-19b8-3738-a980-db76da075399 | 2.94956 | -60.18507 | 2025-01-20 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6a8e1ffd-234b-3543-8ecb-d91b528b0f24 | 0.80363 | -59.89766 | 2025-01-20 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d4ee120-2c8d-3e22-817f-662b83c5afdf | 1.3363 | -60.04279 | 2025-01-20 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0605a89d-a86b-3b9f-a3c8-86c007a1fa9f | 4.02769 | -60.82217 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e340f78-e641-3cb5-8786-6b42e0055158 | 4.35951 | -60.82242 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b80cb56f-2b3b-3b5b-92ab-732239c11ffa | 2.94558 | -60.18574 | 2025-01-20 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ee07df14-497d-36f8-8026-bd67e3e21fb5 | 0.89381 | -60.09102 | 2025-01-20 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02807c90-6e48-3467-994e-240219696e8e | 0.89852 | -60.09409 | 2025-01-20 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a28ff851-ba2f-327b-a938-f804b7c4e6c2 | 4.51126 | -60.6855 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3e816b2-5041-336b-9c90-391b4d818230 | 1.35509 | -60.02839 | 2025-01-20 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 215eca63-c459-316a-9b6b-6d45f75c908d | 3.89507 | -61.22709 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53ee3fd3-280a-354d-a022-d53cde003637 | 4.10898 | -60.84898 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9ba71aa-49dc-3533-881b-cf24eba0088a | 0.70977 | -59.53077 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76ef31ac-fd2b-36e2-86aa-07bbc78bc8ab | 3.89708 | -61.22805 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47f0eff9-478e-3004-b70f-989ee3787c8b | 3.85465 | -61.2112 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45cc98a3-76ee-3bf0-94d0-ec4f394525f2 | 4.15009 | -61.17359 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a17e6689-63b2-3bf4-8e4e-9f24152c8ae1 | 4.50746 | -60.68599 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5dccbbad-58ac-3543-972a-cacbfcfa16e2 | 1.12253 | -59.41681 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 629cb594-f3b9-33dc-826b-3fc39e635cb9 | 3.89268 | -61.22431 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a193328-0e75-35ba-9e79-ced92a6b8788 | 3.2078 | -60.98524 | 2025-01-20 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 393604e6-469f-3548-9dde-aaaa24d6241d | 0.71754 | -60.11549 | 2025-01-20 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1895074d-39c3-33eb-b646-44a197690249 | 4.10753 | -60.84001 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 93cfd6a5-64d0-3b53-8a5d-6f2e6cf0a02b | 3.20872 | -60.98727 | 2025-01-20 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ce326b6-e759-3d55-9230-a35c241a334c | 0.89556 | -60.0916 | 2025-01-20 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b31b429-e39f-3b34-83ce-6785716a5060 | 1.35097 | -60.02907 | 2025-01-20 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8eb91bd2-565e-3b34-9152-57a8c8e29512 | 1.12053 | -59.41674 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f273e8f8-df14-30f4-b0e6-1078df92f8c8 | 0.89439 | -60.09474 | 2025-01-20 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b01bf004-4d63-3542-b65b-08b06a9ba7ea | 3.89069 | -61.22333 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b23f0c2b-614c-3fb5-b2fa-dcaac4a04510 | 3.71637 | -60.44978 | 2025-01-20 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38cba5cc-6add-3068-aa4c-34b0a73c4979 | 0.70188 | -59.69109 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cd1d81e-aa9d-3a13-8dc3-0a11f99fcc88 | 0.80782 | -59.897 | 2025-01-20 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f27ef53a-2b32-317c-947d-d4c9488edff8 | 0.89616 | -60.0953 | 2025-01-20 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 445947a4-aee5-383c-b9e5-c2f6348d680e | 0.94931 | -59.48783 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53b8bcb2-f341-395e-a56e-72fcd7aa507f | 1.05268 | -59.65192 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d1f6498-c8a8-325b-8858-683720f93121 | 1.3545 | -60.02472 | 2025-01-20 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95301407-55f9-3f4e-8516-748684befcf5 | 4.9973 | -60.30003 | 2025-01-20 05:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 933812d4-4c84-3c06-9766-3cdf5fc24b74 | 0.70614 | -59.69043 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7964898-0d68-3e83-ad63-b1da1350f73e | 5.00189 | -60.30404 | 2025-01-20 05:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 577d7920-958c-3246-ad24-998c1dcc7ce0 | 0.06913 | -60.54793 | 2025-01-20 05:48:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55913f26-4798-38d3-b7c5-450f1d7cf601 | 0.06508 | -60.5486 | 2025-01-20 05:48:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 852496b4-a8b3-3b58-b78e-2ce26158636b | -7.34754 | -72.59541 | 2025-01-20 05:50:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79ddc56f-714a-39f1-a632-0e267842e0d0 | -7.34899 | -72.56155 | 2025-01-20 05:50:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a213ebe8-4907-3d11-ade9-365e6d2ecfd7 | -7.34961 | -72.55788 | 2025-01-20 05:50:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f6ed08e-b9e6-3904-86c0-2aa66ed61da8 | -7.35166 | -72.59612 | 2025-01-20 05:50:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 486b4e5b-8337-326a-a13b-f54fdd85ea03 | 3.90842 | -61.26536 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e704b601-07de-328c-b691-ff97408bdb8b | 3.89592 | -61.22635 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41a30bc1-246d-3c21-a42d-be376f710d02 | 3.85916 | -61.20843 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f76f687-5a65-3e25-967e-d6cd3f10497a | 3.91079 | -61.24635 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f87a595-04ea-3db5-a248-6bf28b0eef39 | 4.51085 | -60.68532 | 2025-01-20 06:07:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc9bf721-a71d-3a00-b754-201140657d6e | 3.89529 | -61.22272 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87169f3c-608a-3236-aae8-e65f3220c05c | 3.90835 | -61.26414 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f1ae842-b3f8-3901-b695-b3528ae8c758 | 3.9156 | -61.00853 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5d31eb0-e474-35ca-ab15-e43452bf989c | 3.85424 | -61.21302 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22d352c6-6372-3ad8-9933-72df28e25516 | 4.51171 | -60.69032 | 2025-01-20 06:07:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34dcba7e-460a-36a9-b75b-c002003365d5 | 4.13645 | -59.99276 | 2025-01-20 06:07:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e008098-dc7f-3813-bbf6-22286a9b8db7 | 3.89609 | -61.2587 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1dc606f0-ab59-3b50-ba74-288bfcd7bba1 | 3.91016 | -61.24273 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c96857a0-8899-30b1-8427-19c9e7696613 | 4.51743 | -60.68961 | 2025-01-20 06:07:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7014876-7603-3e6e-87f0-a0973a4a9079 | 4.50593 | -60.69062 | 2025-01-20 06:07:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c61384d4-e329-3783-b7e3-c049c0eaad7a | 4.03231 | -60.82488 | 2025-01-20 06:07:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4b231df6-f3ec-32fa-acb7-0f67ac07ccca | 3.75016 | -60.63624 | 2025-01-20 06:07:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 941b39ec-7927-3510-acd6-dfe9b86ec726 | 3.8967 | -61.26236 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d0f919b4-52a2-3ba6-aea6-27c580968dc4 | 4.50506 | -60.68566 | 2025-01-20 06:07:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da4fed2c-9c18-320c-9938-2d0ba13c88c2 | 3.90227 | -61.26265 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee765a4e-0f50-3acf-b299-c765c3d992c8 | 3.86471 | -61.20752 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8db32726-b596-30ed-9038-624785c97f54 | 3.89655 | -61.22998 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1003fb8-915f-350e-ae6f-b9c5b49a1574 | 4.14334 | -59.99722 | 2025-01-20 06:07:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2ee08ed-0ad1-3c43-855b-fb22fdafa07e | 3.7451 | -60.64131 | 2025-01-20 06:07:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e2eb1bb-877b-3296-82fb-cf0e8bf76466 | 3.90774 | -61.26051 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 596a75d4-0c6c-3522-bba5-c91c36f519f3 | 3.90222 | -61.26144 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f616c9b1-0b16-377d-8f99-a2315beed4dd | 4.99981 | -60.30455 | 2025-01-20 06:07:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c1a4cbac-0cff-3ab5-bb84-fb4846029003 | 3.91624 | -61.0123 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 145bdd2b-4b09-32cf-84f2-9bf7abca4a8a | 4.13954 | -59.99376 | 2025-01-20 06:07:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfce416b-100f-3d1b-8153-8ec6bd59f380 | 4.14027 | -59.99794 | 2025-01-20 06:07:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e349e9a1-9f41-3bce-825d-414e2b5c740f | 3.90779 | -61.26174 | 2025-01-20 06:07:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3245d18-f57c-3de0-b33e-bafc9c4f45d4 | 0.89485 | -60.09356 | 2025-01-20 06:09:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 132299be-faed-30ca-bfc5-d39f71f7a1fe | 1.35575 | -60.02691 | 2025-01-20 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3a5a20db-7cb0-3f85-9fbd-5c2504ddad4d | 0.81218 | -59.90245 | 2025-01-20 06:09:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87bff17d-0c6e-3a5a-b5da-a00266ded51f | 1.36072 | -60.02793 | 2025-01-20 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfde09b7-be0d-396d-b05e-863f4f8bd26d | 1.35991 | -60.02308 | 2025-01-20 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1b7ea2e-97aa-3e1f-a051-8262d71f807b | 2.94808 | -60.18807 | 2025-01-20 06:09:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0158096b-f75e-3104-aa4a-383e04608d1e | 0.81136 | -59.89745 | 2025-01-20 06:09:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f2a992d-008c-3edf-8d81-ff37889e500f | 0.70346 | -59.68876 | 2025-01-20 06:09:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33b6ab2b-872f-3de5-a609-e71e968f764e | 0.89565 | -60.0985 | 2025-01-20 06:09:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b79a612a-72da-3bb1-9fc8-3fe26a7b7d13 | 1.3545 | -60.02892 | 2025-01-20 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95fda34b-c5f8-3184-b713-ddc9c91f2e55 | 0.80901 | -59.89965 | 2025-01-20 06:09:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa28d6bf-1dd4-3ce0-8189-36c6e90f7672 | 0.80504 | -59.89848 | 2025-01-20 06:09:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c18860ab-089c-3d1b-a7b7-ec9f1f0e5542 | 1.35369 | -60.02405 | 2025-01-20 06:09:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a554c5d-d6c0-3f82-ba6e-8eae102e4272 | 0.70428 | -59.69383 | 2025-01-20 06:09:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
