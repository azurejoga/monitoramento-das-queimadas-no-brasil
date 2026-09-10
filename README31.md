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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08c1d11b-bce3-3619-ab23-443d10ad3f65 | -4.95106 | -55.79194 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9098c7d8-e3d3-3bd4-8a9c-f291112aafe5 | -6.18846 | -55.27359 | 2026-09-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5d0bec4-4c67-3a0a-8ce2-570cbd7d4874 | -2.72987 | -57.62616 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 774bd440-36c6-3285-b1cf-db011abf4c9a | -4.28935 | -59.95319 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69367a42-8a11-3d1d-a3d1-fc3d856f05b7 | -2.93997 | -50.47623 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b1cbe2b-3a03-3a29-8d9c-c340e2ca1de7 | -2.93688 | -50.46714 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85b178dd-e03f-3ec7-8735-a7965c809d73 | -6.102 | -44.13271 | 2026-09-10 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60aedfd0-5957-356f-a21c-4bee4bb4fb0c | -3.41036 | -59.22826 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 02d831e4-830a-3a88-ae4d-e9e47014f907 | -2.72709 | -57.62216 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c558d401-bed2-3255-9399-3f90e47694c7 | -6.19191 | -55.27409 | 2026-09-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb9aa957-8868-36d9-ba81-dd8c6b181c3b | -2.86108 | -49.53753 | 2026-09-10 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c98db233-70fc-3bdf-a634-8e9e2629b4c4 | -4.82965 | -55.76258 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0b4bec0-e860-36fe-bf65-70c709d6fe8d | -6.76292 | -44.57668 | 2026-09-10 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f6563e5-32ae-385c-8d3c-53955a328162 | -7.5077 | -45.2701 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5bb9703-fd8d-3058-8305-838e2d3c4a02 | -3.96341 | -59.36346 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9ca741e-13a5-3ea4-8ba7-9f396e52487b | -4.86271 | -56.00807 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4370bc9b-00fa-384a-b684-10fd34ea8581 | -7.50102 | -45.2697 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4478d969-39e1-3baf-88c7-ba7320c28610 | -3.58827 | -59.07639 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7970f56-bff1-3aeb-93fe-6c1a7b13acfa | -2.94435 | -50.47691 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94a81820-c9c0-35ae-8aba-2d6bd713f5e1 | -7.46902 | -46.1443 | 2026-09-10 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 927e8b22-a548-3b4b-8a33-0aacf3126ef3 | -4.28871 | -59.95724 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95a0d3df-620d-3ff0-b34a-71ef344dbe52 | -3.43627 | -59.25608 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfc857a6-9350-3a25-981a-59523e8b12ea | 0.24603 | -51.46712 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0926316-3a97-3901-844c-31f9a70c774a | -6.76722 | -45.4749 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bafc056f-5329-3cc9-91c6-5691618279ac | -2.72819 | -57.61517 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 682d2aa6-80e3-3ef4-8cce-64864a058179 | -1.70602 | -53.69645 | 2026-09-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43672c38-1637-31e8-b5db-d69ba684f25e | -6.14828 | -51.75248 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f01ad27-2736-3d5a-b231-e94a49b56ed6 | -3.40717 | -60.31652 | 2026-09-10 05:10:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 017fd4d3-de46-33e9-8c15-7e81157947b0 | -4.87186 | -55.904 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50a393de-2ed8-33d2-9c05-9a81b030636f | -5.28457 | -55.95951 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f768c8bf-c440-35b3-bc02-88df79f1fe2b | -2.93906 | -50.48637 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4868f215-39a3-39fd-a9ec-40fdd87b53d7 | -3.02925 | -57.88499 | 2026-09-10 05:10:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b134506-5667-35c8-af35-eba6f785b5a9 | -7.50836 | -45.26472 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 702e16af-76b4-3a95-bbe0-cdc7eb99484c | -6.76368 | -44.57067 | 2026-09-10 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 105a996a-da27-3656-addf-e48386fe65f3 | -3.55453 | -48.18041 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5904e25-40f2-3493-862d-203096102432 | -4.29834 | -55.725 | 2026-09-10 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 292b2a0d-08cd-3414-8129-a4254f172d27 | -6.16088 | -44.65186 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ca5dc540-ff91-3fda-ab57-56a232f339e8 | 0.25234 | -51.45361 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 145cf5af-6ecf-3958-9821-4d0d023148a2 | -2.94404 | -50.48294 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41e6419d-0f33-3337-adcc-1df6f6480f2c | -1.4718 | -47.27276 | 2026-09-10 05:10:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21ed6b24-66ec-3c17-a302-dff8633a9e9f | -3.96403 | -59.35962 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e17620a-de70-3eff-8f05-aae2d83d0326 | -1.03757 | -53.73436 | 2026-09-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3be94e59-6294-3854-ad91-7a4d75daa506 | -4.38203 | -59.49025 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6893fbc2-f7f0-32e2-a782-db9384527ec5 | -3.98335 | -56.08875 | 2026-09-10 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 472676e4-4e64-3f65-b63e-6f3f497b59c7 | -2.56642 | -54.74371 | 2026-09-10 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 080012e9-2faf-3f91-9214-df3ba164e463 | -4.86327 | -56.00445 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93aa1a0d-3925-31d2-b697-7c9627835bca | -3.75791 | -51.38552 | 2026-09-10 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe8a641-5c22-38af-9653-b5301f466bae | -1.71017 | -53.69302 | 2026-09-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c70d2208-d8f6-3bf9-9f0e-013b4b5d4f2b | -5.7587 | -45.09324 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 97f315cd-d428-3ea7-8b0f-f4c907896364 | -1.11775 | -54.08366 | 2026-09-10 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a706837f-4927-3779-855d-8b1085b236c8 | -2.94306 | -50.48526 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b085a98-7a5d-3aa8-9ee3-ef5b9b68960a | -1.03346 | -53.73776 | 2026-09-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c9b127c-6cc8-3777-9ef5-078c9f21e344 | -4.83302 | -55.7631 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae7f5e61-70f4-3d4c-9185-8f53bd19245c | -7.46274 | -46.14354 | 2026-09-10 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28156cd3-1df0-363a-89c0-d2cd2f9dce2b | -4.29713 | -49.0901 | 2026-09-10 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b7a0c6c-a7a9-3645-a455-1626b8751989 | -5.76748 | -45.07207 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e4c06a2b-a3cd-308e-836b-7172e4a5f8c5 | -5.38273 | -46.29765 | 2026-09-10 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 230bded7-19e7-3d2d-b261-6fa4a5fc9c71 | -7.26049 | -45.35015 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6b4c13e3-2247-3b9c-850c-c040d68b4498 | -3.89486 | -59.60438 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c218f295-a1d3-37dd-b700-782bb8396318 | -1.03817 | -53.73039 | 2026-09-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfb3fd1a-03db-3d65-9205-7cbfc04103ba | -6.25096 | -51.6697 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80acb95f-5f5e-3de2-9368-b045e95dee8a | -2.93529 | -50.48152 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6316c167-8264-3a4e-a4bc-49e8860b3f0c | -2.94242 | -50.48942 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c869e2da-3a84-385e-87f2-d3cd8b8e979c | -3.41731 | -59.22934 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd57b2a4-d793-325d-aad5-90cec7bf6857 | -2.94212 | -50.46539 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6c08962-96f2-3413-b2b8-d5e750f11e59 | -2.563 | -54.74318 | 2026-09-10 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce2ea30a-c83e-3423-b0e8-feaa3537c13c | -5.75952 | -45.08192 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c6f542f9-dcea-3c99-9e43-fc1468ffaa1b | 0.24843 | -51.45421 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e8467208-ebb2-3dc5-b908-c69bd6d8e42e | -3.53772 | -58.95358 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 398d24cc-228d-34d3-87f6-4db642a5550f | -2.47772 | -49.40662 | 2026-09-10 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 909411cb-e113-3166-8516-898a20359855 | -4.03584 | -50.8892 | 2026-09-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71382b47-b68f-37a9-8c58-4606ce367117 | -2.45736 | -57.95124 | 2026-09-10 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7475de8-1dee-364d-995b-f441bebba580 | -6.26686 | -53.11769 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eceb409d-f7fd-358f-88fe-fc8c69dbc2ad | -6.76866 | -44.57432 | 2026-09-10 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d10a2be1-c532-39fd-9c56-6e2075061ea3 | -4.00214 | -51.02663 | 2026-09-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35fc59b5-6d56-3020-a5a3-0d627478423d | -3.35093 | -58.17817 | 2026-09-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 121961e9-ca40-38fc-b5a5-532aca1f6d60 | -1.72824 | -57.1591 | 2026-09-10 05:10:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b252c3d-d0cf-36ee-a077-308cf0948e34 | -4.85936 | -56.00757 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2a277c2-dd41-3743-9369-536469439432 | -2.93558 | -50.47558 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b647997-1876-3f1e-97aa-14e5e959a793 | -5.77106 | -45.09533 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| fbc82a79-8325-3140-b24c-d18f19c7d034 | -2.73986 | -57.6277 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 621a21d1-1aaf-3570-884c-9d35aabee0d2 | -2.73653 | -57.62719 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 673af20e-969b-3242-af8e-d37be030196d | -5.77177 | -45.09002 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| c133ef67-8903-3ae3-8fe6-b2348294a7e9 | -2.94679 | -50.49017 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e902ee5-56e2-3b53-a28b-e2bbec8f194b | -3.98668 | -56.08926 | 2026-09-10 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5abe65b7-3203-38f7-b129-1f32c7ee2e1a | -3.32383 | -59.84653 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0665312-c824-37cc-98fb-a07cdf60d05e | -2.94842 | -50.48365 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4ad33bb-df97-3ee0-90d6-cbfaedf59f3a | -5.77475 | -45.07373 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0c9e4c45-3429-393b-9b26-f99b82a09b14 | -5.28403 | -55.96308 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c302e33-ca0b-33c1-b878-9456b0047d6c | -6.24502 | -51.68098 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 658ffbd9-3c57-30c5-8df7-f8af9711a918 | -4.45966 | -55.52981 | 2026-09-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5531932-e8ab-3219-a442-18d3c7d5f1c2 | -3.76659 | -59.3886 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa78eeaf-0e66-395d-ae3e-6ce26fa0655e | -6.16764 | -44.65269 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cccf372-f1f1-3253-820d-496b2fa5a712 | -5.28067 | -55.96256 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b823bcb9-db5e-3649-8ff3-dac089fea289 | 0.25782 | -51.43754 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d0d37b9-7a5e-364c-a1f0-b7e3d2430862 | -2.85769 | -49.54098 | 2026-09-10 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 131a687e-e13e-3849-9a61-36d1ae520917 | -3.06999 | -59.27134 | 2026-09-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c64856-4621-362e-8af9-d29f43c4888a | -2.93623 | -50.47137 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77886573-3de8-3420-a809-8ef9f801a000 | -4.86202 | -47.4095 | 2026-09-10 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 15234bbb-f302-31f6-a4a3-9eced7aea162 | -5.76592 | -45.08924 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |


[Clique aqui para ver as próximas entradas](README32.md)
