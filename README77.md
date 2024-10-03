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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d3bdad9-7ab6-3a22-bddc-d09c4630bf19 | -6.30463 | -43.43622 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d857df53-357d-3200-bdd9-b11aeb1b0caa | -6.30231 | -43.0445 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3f01865-4b2c-39ec-96ec-55afb82428a3 | -6.30109 | -43.43568 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f72dd6f8-e645-3c43-874e-df0b682c473e | -6.29755 | -43.43513 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a040a42f-919e-3797-8f4f-26b7fe1602e7 | -6.29696 | -43.43914 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 77b31157-4df2-32d9-8c15-da4d60a4fc05 | -6.29402 | -43.43458 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f7c3ba3-7b16-3b97-b117-f77f6714dafb | -6.2938 | -43.43585 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d68c60e7-e63d-3f22-bd6a-367188c78e86 | -6.29342 | -43.43857 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 130ede0d-aa96-3e46-97ed-5a0f6433f946 | -6.29324 | -43.24968 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4369521f-1616-3cf8-a426-8b5454aab1f0 | -6.28401 | -43.09265 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2df9a811-ec14-37cf-be5a-0114632dfe31 | -6.27137 | -43.10339 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf6853a1-1a2a-3920-94b9-1c85539e5142 | -6.25688 | -43.39309 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18a18233-077e-3400-b586-7002cd5c6769 | -5.17095 | -43.05346 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 453196db-be74-3c10-bd16-fc7e03a7b05a | -5.16739 | -43.05288 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a206a8-ede0-3ac0-8460-2eacddbf8257 | -7.87382 | -42.6683 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7acd1092-f0bd-391f-b77d-7da2ae56ac1e | -7.8665 | -43.09698 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dd847d54-6c5b-357c-bca2-ebd09bbb90a2 | -7.86635 | -43.09891 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 33b40059-c5ee-3f39-811a-1a12869262fb | -7.86283 | -43.09648 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1f462385-9fd2-305c-9a76-1f0ed92a5ee7 | -7.86268 | -43.09841 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7a0866c0-251b-3517-ae7e-0d45c6c90764 | -7.86221 | -43.10078 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 61577471-a059-3410-9c2c-52de54cad465 | -7.8616 | -43.0808 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6199c1ac-7c42-3339-af7a-e75e81ee2174 | -7.86103 | -43.08314 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 9636d8e8-1dc7-3759-878b-d3a04cd523b0 | -7.86095 | -43.08511 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 66cae7ca-6c50-3dc5-a829-40c9e9e35ca5 | -7.85916 | -43.09599 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21b012e7-1957-3701-aa15-8d5c4295fac5 | -7.85901 | -43.09792 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 995e778b-7de3-3775-93f7-9c028a27cfbc | -7.85854 | -43.10027 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| aec148d2-8152-3c24-a167-db77ff921b9c | -7.85792 | -43.0803 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dec5a7aa-70e8-3ca2-8af6-ff32337b5eb0 | -7.85534 | -43.09742 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8fa3b460-b80d-3b9c-8d84-8d1710bea998 | -7.85123 | -43.07495 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f8e2cd4-50e6-3b4d-bfb0-062ac056dff8 | -7.85058 | -43.07926 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b10604ee-7a4a-3f0e-8a4b-60ecd69e8f45 | -7.81937 | -43.08761 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3969917-c8ad-38e6-a234-089a5984a8c6 | -7.8157 | -43.08709 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b93d50b0-c0d8-3d45-b0b3-c0e850f3994d | -7.81507 | -43.09135 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f0cf400-faec-3d3f-988a-54c7e9c36400 | -7.81267 | -43.0823 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c08b6c2-a354-3968-9563-6338b1373883 | -7.81203 | -43.08658 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fd7d0570-1b22-364f-aba8-50c01580588a | -7.809 | -43.08175 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ad917806-e61f-3556-b52b-bc8f5245dd29 | -7.80837 | -43.08604 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 75009cd3-2055-33f7-813b-c0c83effd51b | -7.80774 | -43.0903 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 83bd1476-d35d-369d-b6db-7b25c78f3880 | -7.76756 | -43.05783 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e4e22907-df15-3585-b851-afde2b4e60a6 | -7.7639 | -43.05728 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eaed89ea-e582-37f9-b0ae-e1d75a40652b | -7.76378 | -43.05875 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de333b80-2b3a-3174-8c39-8b883b7faba2 | -7.76327 | -43.06159 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5427b0ca-dfa9-3dff-9e29-fa01b8b2572f | -7.76011 | -43.0582 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d5be8a77-33ad-3b34-8934-f64dc3901436 | -7.7596 | -43.06104 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cdfad4a9-d80b-36c8-99d9-5a759fb9a2b1 | -7.75946 | -43.0625 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cd6ece23-763d-3bda-844b-42c03903205a | -7.7571 | -43.05333 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b8efd5f-6c5d-3c60-8cf9-f62ec77447eb | -7.75656 | -43.05617 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eb9835e9-5f39-3247-9e54-ede2bd16b1aa | -7.75645 | -43.05764 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 12aa29cf-a571-3fda-b7d0-f75f8b333299 | -7.75594 | -43.06048 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8ddd231e-83ee-3e5e-84b2-51b980f51664 | -7.7558 | -43.06195 | 2024-10-03 04:25:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ea41a008-0d63-3027-aa54-b9c90b18075c | -7.69211 | -42.98561 | 2024-10-03 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c70ff43-3c41-3ae2-acec-284f4f46364c | -7.65396 | -42.45187 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d29fd67d-ff57-3d4f-aa71-34ab0a4eee45 | -7.64059 | -42.46401 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2344696a-c1a0-39fd-baee-9f1b12594b66 | -7.63734 | -42.43316 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a529e6c2-c410-3eee-a13d-fb409a952898 | -7.63703 | -42.43496 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ef3b95e7-96c4-3505-8752-e706485d1f44 | -7.63694 | -42.46153 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5fe6b9c4-4537-364a-8ef9-0024acdafd9b | -7.63681 | -42.46341 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| aeb9e55c-a51d-39a8-ad7c-3b6ea7c51f78 | -7.63665 | -42.43777 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1210271c-242e-3f59-8f80-2a42059806c6 | -7.63624 | -42.4662 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 47bad27e-cdf3-320c-81a5-a68db3466bed | -7.63191 | -42.44359 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| de5aeb7f-852e-3f08-b841-dc9d54343cea | -7.63148 | -42.44639 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6237f9a5-3b32-332e-820e-7f677a165e33 | -7.63058 | -42.4529 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18c094e3-4468-37e2-b8b8-951e9bff056c | -7.63007 | -42.45573 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a24dd502-6a28-3c2c-8094-80f95788356f | -7.6299 | -42.4576 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a91490c-bbd3-3007-ad61-afa9a2c891f3 | -7.62699 | -42.45047 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 652982e5-5b10-38d1-b2a5-b1f5b137d79a | -7.62679 | -42.45234 | 2024-10-03 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03c4e2b0-98de-3886-b7c2-10bd74351fdd | -6.63946 | -42.1107 | 2024-10-03 04:25:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| da211f5a-cdbb-32ec-a3f4-cbe662c30e51 | -6.66028 | -43.13548 | 2024-10-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d2d568d-2b89-3b90-ad16-d3f15546c1d8 | -6.65893 | -43.13285 | 2024-10-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11bea4fe-b078-3ac7-aca4-e36f8abf5350 | -6.65108 | -43.06309 | 2024-10-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d09fd7b-8034-36b9-a1d5-606cd30eb9e1 | -6.5175 | -43.15543 | 2024-10-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 645f83af-5abb-3705-a6b6-70d3a9785ee0 | -6.51453 | -43.15077 | 2024-10-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d21cdf00-7829-32de-a83e-2cb80d01d135 | -6.51094 | -43.15022 | 2024-10-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d14e8394-771f-344d-b4ef-80fd727f7f57 | -6.46509 | -43.35715 | 2024-10-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74da8734-5673-38ac-883f-2cd256f77a92 | -7.45483 | -42.51608 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 098d9765-35f4-3c6a-a5f0-31bccc6e3c7b | -7.45417 | -42.52061 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 05453e19-477c-3280-a013-616773da8c60 | -7.29583 | -42.25543 | 2024-10-03 04:25:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3881006-a72c-31e5-a967-897c4b7ba902 | -7.29513 | -42.26015 | 2024-10-03 04:25:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5e161787-3745-336a-b824-b3ebd0a54435 | -7.03712 | -42.81431 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c36e8b37-85c3-35bb-b7d4-7c0f4be67e8d | -7.03601 | -42.81649 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 812a28cc-626e-3720-8750-99402574b4fd | -7.03344 | -42.81375 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca335c53-c2dd-3e11-a1b5-9d213c551968 | -7.03277 | -42.81815 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9f5fd350-07fa-3d64-8725-4760710b421d | -7.03233 | -42.81593 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fba50e5e-928e-3fbd-97b0-699020b28ed8 | -7.0291 | -42.81758 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b83d9fde-db1a-30b3-9467-4c06c9b5afd4 | -7.02476 | -42.82136 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93a44125-675d-326c-ada6-f9440194e00f | -7.0241 | -42.82572 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ae9adb65-7592-3887-9b97-d7f58a24039c | -7.02042 | -42.82513 | 2024-10-03 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6dad769-cab8-3b53-a546-513d2ba0c20e | -6.88036 | -43.60448 | 2024-10-03 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 716a3271-b5ef-3ade-a03d-c7b3a95e6587 | -6.87976 | -43.60844 | 2024-10-03 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b81a460d-6af2-338f-9c09-fe6e926d3d7e | -6.87916 | -43.61239 | 2024-10-03 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ae67fda-b2ef-3a4a-ae3d-28f2a0862a4f | -6.87683 | -43.60392 | 2024-10-03 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ddbedc8-5f7c-32eb-b6be-8d88542afa82 | -6.87623 | -43.60789 | 2024-10-03 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e0205eaa-512a-318c-8fa0-90061e9fd1af | -6.8733 | -43.60336 | 2024-10-03 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ab355b32-ad84-3b05-affa-ab79878955a9 | -6.8727 | -43.60733 | 2024-10-03 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b88b8a02-0b4a-31dc-9cb6-63945571abef | -3.4748 | -43.35497 | 2024-10-03 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fed5cfb3-96ae-3742-8db3-62c0e8033fb7 | -3.47421 | -43.35876 | 2024-10-03 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a19f4aa-4828-35c5-a6c8-1752d5d45a16 | -3.47076 | -43.35822 | 2024-10-03 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 95d86fc5-449b-39fb-9c02-e93eab705ec3 | -3.42725 | -44.43775 | 2024-10-03 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9a85dc5-c469-367f-b442-b1ce6081dbd7 | -5.10746 | -43.32578 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9b93e96-da5f-3ef4-878f-6919f4829b1f | -4.94316 | -43.68437 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README78.md)
