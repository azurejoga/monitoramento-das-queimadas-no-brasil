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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63a9cecb-0e27-3e52-a35a-164a58cd4c27 | -7.33143 | -47.05093 | 2026-06-12 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 443164c6-bde0-39f9-adc9-2206a3681fce | -9.11251 | -47.9654 | 2026-06-12 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91c63365-14c6-3a2b-8e21-cac8c1aeeaee | -6.4353 | -44.55539 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e6a3447-9ebe-3ed6-af91-4b2350032dbc | -6.39268 | -44.17578 | 2026-06-12 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 916c635a-32d3-3dbb-8168-9471729ae57d | -6.58175 | -47.91024 | 2026-06-12 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f341397-7d5b-3262-80d9-4d50849ced71 | -9.31348 | -48.96938 | 2026-06-12 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36de96d4-9804-3b42-9f85-5f6faa3d1e63 | -9.31295 | -48.97325 | 2026-06-12 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e043885-e80d-3317-b89e-8aa1816a31f8 | -9.20794 | -47.91946 | 2026-06-12 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| faae4a68-faaa-3fd3-b939-5bce7e235d45 | -7.63934 | -45.30258 | 2026-06-12 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 501bdff7-7932-3f39-a826-9041e37d7988 | -6.73045 | -44.376 | 2026-06-12 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b89599d-05d6-372d-b795-8065e84b2ff6 | -6.19241 | -44.86374 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85f29d4b-d2f8-3bf7-ad2d-35f9a1e09a23 | -6.72489 | -44.37522 | 2026-06-12 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cf02147-ff7a-3814-a51f-e6a1e3b4796e | -6.18754 | -44.85947 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df428b51-d452-352d-972e-d35f7122b53a | -6.44161 | -44.55874 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88230071-456b-3149-9e6c-0f84055d417d | -9.21667 | -48.58273 | 2026-06-12 04:57:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| da2e42fd-2d3c-3bb3-87a1-0f2a4ceca84d | -6.19426 | -44.86197 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db950341-ea5c-30f9-89b8-303ae2c9e378 | -6.44124 | -44.55282 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bff4175-bd7d-31c8-b234-f796d66f3ad5 | -6.44025 | -44.55991 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12d54041-a512-3472-81ac-6bb001b2bff6 | -9.21247 | -47.92009 | 2026-06-12 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c056997-5e1b-3516-9ccd-3b5add261192 | -7.6398 | -45.29924 | 2026-06-12 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b368df45-e384-33fe-a78e-ea4a1178fcc7 | -9.19496 | -48.64332 | 2026-06-12 04:57:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36e4da84-8c14-352b-90e0-7d87a3fcdbc3 | -6.44074 | -44.5564 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 076146fa-10b4-3ede-b442-d36e64a5d48e | -3.49634 | -48.04008 | 2026-06-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78599989-a5fe-33cd-9866-6b486ae02639 | -6.57189 | -47.91705 | 2026-06-12 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7854186e-3875-34a9-a0b1-4299322934c3 | -7.72585 | -44.16241 | 2026-06-12 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6950dc6-3e7f-337c-88e0-e487b7e2e337 | -9.62609 | -49.01899 | 2026-06-12 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98e5bdbd-e9a4-3b2f-bdf5-646cb4ecad82 | -6.18848 | -44.86432 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09cb9d05-5579-3e99-8cfa-7dd833ea5e16 | -9.21093 | -47.91872 | 2026-06-12 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b5f188b7-c11f-3cb0-9b2b-21f8067337e7 | -9.06641 | -44.74536 | 2026-06-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9275013-7ea0-3560-9139-f4baf48d7dfb | -7.33612 | -47.05149 | 2026-06-12 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60319313-b5f9-32a9-9d3e-a39abeb0b614 | -9.21157 | -47.91413 | 2026-06-12 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5046337-2001-3d18-ab9a-29fbcc60bb82 | -7.64507 | -45.30016 | 2026-06-12 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e381a3e2-e3d5-3d8f-8ae9-ffbc14593e21 | -6.18709 | -44.8628 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e86c0721-c99f-394f-a87d-f44b48275517 | -3.98691 | -47.93791 | 2026-06-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9052180-170a-33ed-b4be-be41ea025595 | -7.34011 | -47.05708 | 2026-06-12 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9c8d738-7dee-3972-9fc3-2425f595c69b | -7.30757 | -46.29662 | 2026-06-12 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 718b1489-2a5e-36af-9bf7-230ef27cbf55 | -9.11314 | -47.96074 | 2026-06-12 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0f0bf51-b2c6-3bf6-af59-5f68241281d9 | -3.50046 | -48.04076 | 2026-06-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 083e26dc-84b5-3729-8b66-2bb3765c0f1b | -6.39657 | -44.17606 | 2026-06-12 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d21177ce-f253-3dae-aab8-8c2cd698dbac | -7.64553 | -45.29686 | 2026-06-12 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b8363ed-f322-3584-beb7-3bdea846f131 | -9.21725 | -48.5786 | 2026-06-12 04:57:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1701516-640e-3b10-ae14-16387478e440 | -7.33543 | -47.05645 | 2026-06-12 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 269125db-ea8e-3826-84d1-07cc535ff836 | -7.64454 | -45.29914 | 2026-06-12 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52984d0c-9890-339e-b16c-0ca886310d78 | -8.03197 | -45.04228 | 2026-06-12 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 917022c0-d840-3ff2-9c30-c5416cabf5eb | -7.35103 | -47.01285 | 2026-06-12 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 346a8772-f44a-3554-b209-3660c9343800 | -7.36823 | -49.87157 | 2026-06-12 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eab94207-42a2-35c0-bf9f-03b70db5b194 | -6.43976 | -44.56343 | 2026-06-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ec30cdb-b6ac-3680-8235-1b8801b2f899 | -10.99842 | -46.74553 | 2026-06-12 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a74858c0-43f4-3e67-ae61-c9633acbf217 | -12.4764 | -45.44194 | 2026-06-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a81e524a-736e-3c39-96dd-c32ddc307f4a | -12.29925 | -57.40112 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83e0523f-9ae8-3dc1-80df-7797c45394c1 | -13.45499 | -55.75368 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77ba82df-d9cc-30ee-a995-3f1c4737b78a | -12.41784 | -58.48151 | 2026-06-12 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68a59d4d-b7ab-39df-9b52-0d1567310a14 | -12.79987 | -54.86722 | 2026-06-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34f82587-e964-3742-9abc-64d34aec8375 | -12.4221 | -58.47801 | 2026-06-12 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 491bb5ed-1b45-3fbc-8516-915e5fa9a43c | -12.42567 | -58.4786 | 2026-06-12 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fd2e508b-cd2e-383c-a765-c7f87772c31a | -12.85779 | -44.37 | 2026-06-12 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 22e5c319-a122-30ef-8f05-cb03808967c8 | -13.46434 | -55.75881 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f36946b-10dc-3894-a7b4-64c097e9e3c1 | -12.85828 | -44.36541 | 2026-06-12 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7f2fe693-53b9-3946-86f4-1d2b1ca5a92c | -11.44782 | -55.90158 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b9c40cb-2f6f-35b8-b5c7-ae2802148849 | -12.15053 | -48.45153 | 2026-06-12 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a973baf0-a2a8-3656-85cb-72b45c796ba3 | -12.42141 | -58.48212 | 2026-06-12 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51d3c44f-8df5-345b-9570-ec3e47bfe537 | -10.82489 | -58.01434 | 2026-06-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0aa441-445b-3b3a-9d9c-47a84c81d5f1 | -12.35531 | -47.89955 | 2026-06-12 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c6b001c-97e4-3280-93b6-8d19d8386159 | -10.84056 | -53.74078 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04146bdf-2496-355b-a540-e43fd04a82b2 | -13.46049 | -55.7618 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bc35717-d814-3ea4-bb39-7399c261110d | -10.83104 | -53.73562 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a71dd83b-20a5-35ad-8222-5632c9af9cdd | -13.45774 | -55.75774 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88b59890-8df6-3638-b928-4caff30f05bc | -10.83159 | -53.73201 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0acf5c70-8ed5-38ec-a030-d2d19af67e82 | -11.58206 | -47.45583 | 2026-06-12 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a94a4182-1ad9-3eb3-9877-18a70a99df22 | -11.45169 | -55.89859 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48d6a221-c1fa-38ea-99f7-b7a491e79dd5 | -11.62115 | -55.18582 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6ce6d29-4e1f-30f9-b0ff-77949a0e71bd | -12.86203 | -44.36757 | 2026-06-12 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 70450404-9e13-31dc-990a-b4035714b979 | -12.8615 | -44.37216 | 2026-06-12 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bfabbb39-f932-3510-9acb-6f01771abb90 | -13.45224 | -55.74961 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc8b8193-c1cb-3917-b859-29e519969957 | -11.48691 | -52.91459 | 2026-06-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d038987-3e53-3596-b77b-7dea370a0609 | -12.30266 | -57.4017 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f892adaf-a2f1-3a08-99e4-04fbe2eefbdf | -12.14901 | -48.45494 | 2026-06-12 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 46c3b35c-eeca-32e4-b589-f517795c779d | -10.82134 | -58.01374 | 2026-06-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 19560f37-9640-3aed-8436-a511367fed3a | -12.856 | -44.36682 | 2026-06-12 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4ab630b2-a2f0-3b64-886c-ac519a382afd | -11.6217 | -55.18232 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 222a5b03-3abe-3d1f-82de-c152b003025b | -10.84001 | -53.7444 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 923428bd-d6d5-3922-bf80-0ba1282f201b | -12.4321 | -58.48392 | 2026-06-12 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 569802cb-fce6-39b3-b195-1a7f782a559e | -10.8361 | -53.7475 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 845576b2-cfe6-3ecb-814f-133dcc719c67 | -11.44838 | -55.89805 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b5fb906-5cc4-3243-9d16-339393af37b8 | -11.62721 | -55.19037 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e3c4d5f-6add-381d-abb4-32210724fe94 | -11.7467 | -48.91145 | 2026-06-12 04:59:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82100b87-20a6-3263-ae5f-f6333d03ba83 | -11.63393 | -55.17332 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9538baa0-242c-31b1-97cf-aafc0acbcc6c | -13.46489 | -55.75529 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 112216ef-0957-37d6-be37-ae98b4885fc8 | -10.84391 | -53.74129 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83a8ebb0-ae9e-32a1-a4d3-90d5d3172a21 | -10.56774 | -57.32578 | 2026-06-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67667255-1c72-381f-a286-98efbf2dc2db | -12.29987 | -57.39734 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5c228e3-da13-3867-9929-6129b826dadd | -12.85547 | -44.3714 | 2026-06-12 04:59:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 655d4c73-7ea5-3786-957c-fe91c8c09457 | -13.45939 | -55.74717 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f911abd8-be54-37c9-9c7a-2b7b6e80a8a6 | -11.44726 | -55.90511 | 2026-06-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99d79b34-eaf7-39be-9707-7e21b004a5c1 | -11.00345 | -46.74627 | 2026-06-12 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98fe6702-78d2-3c96-90a0-26f220987be1 | -13.45554 | -55.75016 | 2026-06-12 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9d9d83e-37ad-3350-8523-b06f072225cc | -11.62775 | -55.18688 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ca0c858-e55a-3347-9a89-28ccf26573e6 | -12.42923 | -58.4792 | 2026-06-12 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9229c87c-4e79-368c-8b95-f29a7901e440 | -10.83269 | -53.72477 | 2026-06-12 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fef404b9-f0ae-39c8-a27c-e1efb54b283e | -11.625 | -55.18285 | 2026-06-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README8.md)
