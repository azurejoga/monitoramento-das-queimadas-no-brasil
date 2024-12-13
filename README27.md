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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3155dd77-8628-380d-a532-d2791187b520 | -6.92072 | -43.5333 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.1 |
| a71959d9-5480-3214-9fbf-333a8aff6783 | -2.00383 | -54.51112 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 751e3507-2ba6-3877-acd8-f7dddf6bc7df | -2.31274 | -53.75059 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdb06bb4-709c-3ae5-9cf3-3e317f73e102 | -2.41965 | -53.68776 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99f1e0e9-d811-3403-ba37-7af41a0dcd1c | -1.68522 | -55.00435 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3563693-7144-35d3-bcb1-ff78bfaac012 | -5.62685 | -45.39101 | 2024-12-13 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fc33d7f-1485-30a6-8a0c-5d23bdbcc601 | -2.82733 | -53.08043 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b725135e-f3a3-3655-ad26-49b876a30afb | -4.16174 | -42.44662 | 2024-12-13 04:42:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d8d6c864-7614-318d-876b-f834a3a2ea53 | -3.29053 | -45.59229 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0f379c3-90ee-3417-b559-4a65ab8849b1 | -1.96526 | -48.39154 | 2024-12-13 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cf7f0ce-92d0-35f3-b2f3-ec22e87d36c7 | -6.96675 | -43.00125 | 2024-12-13 04:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| daf9d5a1-ca6b-35ba-a43e-293fb3f3761a | -3.2257 | -49.3625 | 2024-12-13 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bec0e7ee-2df1-36ac-ba3e-0a5982e6a843 | -2.45542 | -53.71371 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5da5849b-407f-30f8-9480-fdc2991882fa | -2.55998 | -53.41766 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88941ab5-27bf-3a00-afb3-a4dae3f464b7 | -4.72873 | -46.49996 | 2024-12-13 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bcb2aff-ca1e-3824-a02f-bb73c1853e89 | -2.86168 | -44.37234 | 2024-12-13 04:42:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d68960-8983-3de4-8b93-de3cc5ef265c | -3.67068 | -39.5817 | 2024-12-13 04:42:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e20dcb3b-2b50-3e07-9f6a-eb5dc0ccfddf | -2.91245 | -48.00618 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c987624e-5e3b-397b-869f-28810d74a784 | -1.81356 | -52.69489 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03a62e27-afc9-3302-95df-04fb389a9442 | -6.08988 | -43.54071 | 2024-12-13 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca7b946b-4dcc-3069-885c-8ec0182e8155 | -5.20585 | -43.29162 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| c5794591-4be0-3c91-b460-46ccfe3ec10e | -7.42834 | -44.73718 | 2024-12-13 04:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20f89eac-8d4e-3c04-9dd7-2af627d61852 | -3.00371 | -48.02768 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ac911ff-8474-30ff-9047-4a4871f9fa57 | -5.45064 | -36.87762 | 2024-12-13 04:42:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88a085fb-da10-3901-a949-a65f1ed5515d | -6.12687 | -42.54356 | 2024-12-13 04:42:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9055fdc2-c6b5-33fd-b885-fca83cca9ce2 | -2.30792 | -54.00249 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d383355-7048-394b-b17b-0b5839b91090 | -3.26647 | -46.92033 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fbb1c784-dc4d-3ad3-84e6-db9f8b9c7a78 | -2.23114 | -53.72543 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 48c74ec9-e89a-30db-9f2f-cb8606f574c3 | -5.37607 | -43.50245 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cf96422-7cd2-3159-8f42-6ae2ebe00af6 | -1.99206 | -54.50903 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 678b0922-d5fc-3360-b0de-6ceae6519f3d | -4.05229 | -46.67341 | 2024-12-13 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ada48ca7-ae0a-39e2-ab76-08c6f4f1d302 | -5.4539 | -44.80584 | 2024-12-13 04:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81f9ae2b-89c0-3154-aea7-309a8b14e790 | -2.55427 | -53.42995 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a16d9994-f0e6-329a-b09b-d1e716e16e26 | -4.47998 | -47.98823 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75690c81-1cec-355d-9a3d-d9e699df82df | -1.23496 | -54.14312 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 021a303b-2483-3450-80b6-fd57310686b4 | -5.94481 | -43.77485 | 2024-12-13 04:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adcedb59-37a5-3dd4-8bb4-c460af17ccd4 | -2.45784 | -53.71183 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a5ee584-25bd-3a8c-885a-e454d3851302 | -1.73476 | -52.02089 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c84809c-c90c-344a-89c0-13feec2575b6 | -3.13868 | -53.28613 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79eacf65-eb13-37b8-ab77-981e5d1f89d6 | -2.0786 | -52.28002 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e7be485-899d-3d63-8eba-052dff134c33 | -6.91669 | -43.52753 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1e36a76c-b5b3-362d-aeb2-fd3984a439ed | -3.01344 | -48.03302 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23afd137-88cb-3777-a73c-2f433fca6daa | -2.51283 | -51.79662 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 596390bc-da60-3b23-9059-065d5926d790 | -2.48947 | -51.81177 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d68b9290-3df4-34a2-8df6-8fdb65a00767 | -5.20982 | -43.29739 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| ae3ebe2e-d040-3771-9beb-d56ee6ba993d | -2.73965 | -52.97169 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 345e2be2-8b52-3fc9-b14a-5cf4d6f23b7d | -1.89768 | -46.81773 | 2024-12-13 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 546bfa18-e57b-3c05-aab3-589c41bd1983 | -3.18226 | -45.61907 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c9e8402-f030-32a2-8bd9-6a3cec338a8f | -2.00305 | -54.51609 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c017676f-c220-3f0b-bce3-1a5b16507c92 | -2.90433 | -46.69838 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 868f90d1-9bc0-3067-8cf0-706ecd6e9a3f | -1.74563 | -52.03357 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 514125bb-f4c1-3537-b849-cbd75735d02a | -5.45159 | -36.87056 | 2024-12-13 04:42:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9487edf8-c7ab-3cc6-8f0d-550ad0f8900b | -1.74682 | -52.03443 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 070ec875-5af0-3be1-9f8d-ef941d6f5c04 | -2.338 | -53.59097 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2725c9a-194e-3880-af35-e44d255cca4f | -2.79785 | -47.42182 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6c53b67-eab9-3962-b85d-b2c5dc70b6e1 | -2.29261 | -45.73563 | 2024-12-13 04:42:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05aa66cd-df6a-30a7-9c35-3795f1c3d4ea | -3.47206 | -45.7999 | 2024-12-13 04:42:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 346271fb-ea6a-3924-bddd-5c70a2b8dbd2 | -2.73736 | -52.96316 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30f235dd-a7a0-3580-a2bd-d9288c26e782 | -11.89992 | -49.6203 | 2024-12-13 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8ce3c2f-61c9-335a-be6b-9f5d432be445 | -11.2002 | -53.82017 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d7fbee05-94e7-37f1-8a7e-96a700e12e86 | -13.05787 | -52.03582 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fe39525e-fcf9-35d1-af94-e315b309f2a7 | -10.35018 | -57.25097 | 2024-12-13 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e57ed76-ab39-3744-ad9f-4232ba9a138c | -11.62478 | -57.49192 | 2024-12-13 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7eff315-964c-34e7-a3fe-c1f196afa51d | -11.44113 | -55.92324 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afd969e7-f482-3eb4-bffe-d0aa5c8f8139 | -11.4965 | -52.93023 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 20337d98-b1fb-3ee0-bfa8-ac37a457c0b9 | -9.15985 | -49.47696 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a35d973-561f-3329-b021-a79d87c38e7d | -9.16672 | -49.47797 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6dee50d0-d6fe-37c6-9809-1a6d2e86f39d | -13.69731 | -54.76893 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c287c73c-aa7a-339a-b467-0153633b03ce | -11.85865 | -46.95139 | 2024-12-13 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f01c33db-cd0c-3ea6-a597-cb4c94ca3b37 | -13.69858 | -54.76122 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1109164b-ab5e-39ea-8d24-d819b4e49ca4 | -7.57915 | -47.11336 | 2024-12-13 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2555d4a-bcf2-3462-b7ea-b5485f80dc43 | -10.6784 | -56.55552 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e9cda70-49cc-3b06-96dd-3979fe62ddeb | -13.23584 | -54.17922 | 2024-12-13 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73338a46-4cd5-318d-8f23-8d76364e27dd | -10.86841 | -44.94197 | 2024-12-13 04:44:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65c9c85f-028a-33c1-8fbd-a173b7f2b112 | -12.5344 | -57.73603 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4639245e-7ade-33a1-a805-62fd09d9a0dc | -9.19136 | -49.47783 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1459cc96-f71b-391a-b140-526133934cfd | -11.20984 | -53.82558 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb2b22af-71d5-3b56-82eb-ad24dfb90c58 | -13.07058 | -52.04151 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c4e907f-204d-33cf-bf9a-c2fafe481fec | -13.69231 | -54.75615 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d89bb2c5-9f1c-33de-b633-22156d72d133 | -12.38135 | -51.45179 | 2024-12-13 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2c75739-d04f-38b4-8e3d-cb5c0e1fc73e | -12.38081 | -51.45536 | 2024-12-13 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2eb24dbe-76f0-3043-8fc7-09cb0230f923 | -11.20581 | -53.82876 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 79726623-fe5f-368e-a76f-fc662d884015 | -13.23517 | -48.23866 | 2024-12-13 04:44:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 977ca41e-e866-38df-8126-a8e9924d1075 | -12.5385 | -57.73685 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4754e45a-1904-3506-9b82-8cf6cfaa3874 | -11.19557 | -53.82708 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fdab0ced-de83-3f9f-bbf1-de2cbbd8ba6d | -11.19898 | -53.82764 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5b16a09c-637f-3175-9c6d-1ce6f5cc3e96 | -11.20301 | -53.82446 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 844cfab6-7bed-3fc4-b25d-82ca43ccdc68 | -11.53679 | -56.45372 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c96a78f1-0a7d-3c14-8293-8e612c021f5b | -7.25235 | -48.41989 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c840c18-2989-3db5-9d13-e0f8509d0846 | -13.07555 | -52.03144 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f553b62-3641-3318-b64b-069f3bd83f39 | -11.43707 | -55.89608 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2097f14d-8bcf-3a89-b15c-5b3e773af05e | -11.36605 | -49.24727 | 2024-12-13 04:44:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f344f097-6fe8-3b54-a515-bc9dd024fd47 | -8.26802 | -48.02673 | 2024-12-13 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5453ad9a-b237-352e-b428-53cf667805f9 | -7.97089 | -48.16203 | 2024-12-13 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a63fe067-3c0b-3ac7-95b5-2579b5777ef2 | -8.71432 | -44.00583 | 2024-12-13 04:44:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 874ec013-e468-3358-9074-a0603c1b9c32 | -12.01924 | -49.54124 | 2024-12-13 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e380863b-5d81-3ab1-9484-4f7711cdd2a5 | -12.53299 | -57.72041 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e673c733-e6b7-38c3-8ae5-96222abde2d7 | -12.53764 | -57.72683 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3c81cc7-55af-3d14-bc26-b7cd9923aa3d | -12.35616 | -44.71632 | 2024-12-13 04:44:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e8e67d2-e8c5-3fb3-abb3-7cb5644914c1 | -11.15678 | -49.43809 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README28.md)
