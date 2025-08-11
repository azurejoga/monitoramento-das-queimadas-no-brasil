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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fd01ba6-8a58-3ea8-bb30-d76a793ffe21 | -15.4407 | -53.9258 | 2025-08-11 04:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 594310bf-786f-325c-ba7b-397716ca586f | -8.9401 | -60.7288 | 2025-08-11 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 1848336c-fd1c-3ffb-83af-4e205faf15b9 | -15.4216 | -53.9073 | 2025-08-11 04:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f4b466d1-dbfc-3e62-9c3f-046f00f44851 | -6.5858 | -44.541 | 2025-08-11 04:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 71023e00-3321-36c2-9fc9-9df3b5fc7585 | -5.4824 | -44.3969 | 2025-08-11 04:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d16d7e90-3f1a-32d8-901f-6a6926fa5078 | -7.0614 | -59.1972 | 2025-08-11 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 735fd055-7ed3-30ab-a513-556973ccf373 | -9.3806 | -61.5315 | 2025-08-11 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 78769e96-bc14-3c63-910f-138b665d38ad | -7.0799 | -59.1964 | 2025-08-11 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a43af08a-29d6-3460-a69e-227964c90307 | -15.441 | -53.9048 | 2025-08-11 04:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 10f89768-edcf-315e-a6db-40c8cf2c62e0 | -6.5856 | -44.564 | 2025-08-11 04:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| c92d8d9c-0255-3099-99f2-d99423c2dddd | -9.3806 | -61.5315 | 2025-08-11 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 51ab068f-4528-3115-8152-4780738062cd | -6.5856 | -44.564 | 2025-08-11 05:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 87bfcc10-3835-36dc-a7fa-e5cb049b157c | -7.0799 | -59.1964 | 2025-08-11 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 945cf552-a7ac-32db-a88f-01f619851823 | -7.0614 | -59.1972 | 2025-08-11 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1ca7d2a3-0d64-39ee-abe5-8551aa35dee9 | -15.4407 | -53.9258 | 2025-08-11 05:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| da598c3d-be9d-3093-a148-d24c08a02b68 | -6.58806 | -44.56168 | 2025-08-11 05:06:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 5f8eb8c8-edf6-3b78-92f4-fc97d4fe4ad2 | -7.46029 | -43.95928 | 2025-08-11 05:06:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 3f18ac67-74a0-35b1-ba58-54cee6b0683f | -7.46101 | -43.95418 | 2025-08-11 05:06:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 8320db24-531d-38ed-b7df-25578e338a05 | -5.48226 | -44.39401 | 2025-08-11 05:06:00 | AQUA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 8ddd49cf-f6aa-3a4d-a5fa-a653bf06570d | -6.57854 | -44.55508 | 2025-08-11 05:06:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 41a113b7-7aab-3405-ac97-464ff8c46f25 | -12.57279 | -41.27629 | 2025-08-11 05:08:00 | AQUA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 59d9e228-18ee-3a80-9708-2d675b44b07c | -7.0799 | -59.1964 | 2025-08-11 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 37d5be17-19dc-3957-99bf-74dcf02ddd52 | -8.1304 | -47.4354 | 2025-08-11 05:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e7f6d8d5-b198-3f14-86be-c917231eec6a | -6.5856 | -44.564 | 2025-08-11 05:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| bc21ee23-aefd-3786-a2d3-b2d95cffd436 | -7.0614 | -59.1972 | 2025-08-11 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 32c4a015-f908-39b4-9f2c-80e8bef3a216 | -15.4407 | -53.9258 | 2025-08-11 05:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 0dba7772-2b01-3ad5-9334-09c6a89f012b | -8.9401 | -60.7288 | 2025-08-11 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 81b08245-efce-3a26-9f87-357879639986 | -2.61948 | -54.7277 | 2025-08-11 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8a0831f-749b-33fc-af1b-df97638e13ca | -3.22408 | -49.34206 | 2025-08-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3354f197-a23f-36e0-9322-0888c29cf49f | -2.95897 | -49.06824 | 2025-08-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b6c1916-59d1-3e26-a925-f7fb9d027298 | -3.4265 | -49.04575 | 2025-08-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 81044237-5cb3-3e90-8d7b-6d2d1613645d | -2.95947 | -49.06489 | 2025-08-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f81da7f-d57a-3242-af73-73bc7e3599ee | -4.30118 | -48.07045 | 2025-08-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 107efc75-a4f6-3f92-a724-24d715ae4545 | -3.22359 | -49.34541 | 2025-08-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04036367-b8a0-3c97-9f7c-c72562bdf917 | -5.34255 | -55.90742 | 2025-08-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7628c771-3dea-3044-84e3-6a18509e75bb | -3.42601 | -49.04922 | 2025-08-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 939f01e7-b167-3bd7-9930-f519f066ef7e | -3.43145 | -49.05004 | 2025-08-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c5d446f3-89b5-367a-8231-3db94dfe358a | -5.34315 | -55.90341 | 2025-08-11 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 691563d8-df9a-3a4c-84ac-9c379c7ed5fd | -3.65165 | -48.32462 | 2025-08-11 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9047fb3-d186-39d0-8ad5-9cb0f84961da | -2.37325 | -51.91148 | 2025-08-11 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a90c11d1-4bb8-36c2-b583-6199bcec0ee4 | -2.58755 | -51.92335 | 2025-08-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63948183-c8f3-31ce-a0fb-e36cf035efc3 | -3.22891 | -49.34622 | 2025-08-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b9c4504-8cd9-3074-bf4e-87ee32519e6b | -3.43065 | -49.04431 | 2025-08-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9a405058-cc6f-36a2-be4b-f1bcb02913ed | -3.42961 | -49.05125 | 2025-08-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5a4ee956-0d36-34c1-8665-f119a3cd3017 | -3.43194 | -49.04659 | 2025-08-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8064bfb8-d28b-3f44-a9ab-7220040df507 | -3.43013 | -49.04781 | 2025-08-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a51b89d7-1b3f-36b7-8981-0ab751f73e78 | -3.22458 | -49.33871 | 2025-08-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6abc205a-ae0e-3dd4-be6f-05a1615db3f1 | -3.51043 | -50.74275 | 2025-08-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5824846b-5340-34ee-ad0a-8175d5a34b5a | -4.29657 | -48.0608 | 2025-08-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf88026c-097e-3662-ad24-96c4596b775d | -7.09433 | -59.18806 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da6a189c-e09a-3f33-8282-c1f805b6d3b0 | -11.7575 | -51.62218 | 2025-08-11 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5174fa-a10f-3733-8ab3-466f0e593eeb | -8.92138 | -60.76506 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e3ea7f2-3d5e-3073-93be-2bdfa1c2fbe1 | -8.57222 | -54.68954 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e3272b0-173d-3e20-9a86-7324afbc735d | -7.07949 | -59.19638 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d54836d-2b75-341a-adb8-689a46671896 | -11.71856 | -50.11031 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72106f66-6dca-31ac-81c4-633f5e36246d | -10.36897 | -50.80916 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6d2ed382-717d-37da-b8da-c8b5ef1458a1 | -8.5662 | -54.67425 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5b9126e-8002-34ca-ade7-9a7fc225fb82 | -8.57021 | -54.67485 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72c9d2a1-11ad-3360-9fbd-190fa4ebeede | -11.75509 | -51.61502 | 2025-08-11 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd56a08f-169d-37d1-bce2-78e3b2d56e95 | -7.07443 | -59.1637 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2621d694-26cd-3bf4-9b7e-ffd268c1b3ae | -8.90559 | -60.54121 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1916357-9247-35cf-af2a-3cc660e5f655 | -8.93965 | -60.73161 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04832b93-325d-3225-8462-02575448ec96 | -7.06356 | -59.2116 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4aa9eb20-a749-3236-b4cc-63dffe87f4c1 | -11.28178 | -60.55142 | 2025-08-11 05:18:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5ea00f4-7ee7-3709-9a2b-d615cec944fa | -11.75471 | -51.61818 | 2025-08-11 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 404a2056-40fc-33e3-a673-66a8ab47ef9c | -7.05688 | -59.1893 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22b58e43-6350-3782-9f67-723c0d5c81c0 | -8.56921 | -54.6819 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 845d1c16-a357-3de9-b88f-d65a5a5d95d3 | -7.05911 | -59.19673 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 063efcd4-10c2-3b43-b53f-cf422cf69ede | -8.56822 | -54.68895 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d462b95c-3649-3532-b070-cfb8b60b302b | -8.93013 | -60.74828 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46e213ef-6311-352c-96fc-cc94e657f965 | -8.79627 | -52.06136 | 2025-08-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14b584f1-60f4-3578-bc5a-1c870c46ac04 | -7.07287 | -59.19534 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0751d9a0-7f8b-31aa-9f01-7a840c1f74cf | -8.93908 | -60.73515 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccce9519-e7e9-3257-bfb7-fcd98c4e97e3 | -8.56723 | -54.69597 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c383ab1-0cb8-3d14-9ccb-16c3d37a756f | -7.06235 | -59.17598 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dc7755f-07de-3d4f-8f8f-386c76fc6566 | -5.78898 | -60.43678 | 2025-08-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e900497d-ff60-3109-be5a-fdee17487fa8 | -8.92922 | -60.73717 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e973d17c-41c5-3a34-bfca-e4daba618923 | -8.56071 | -54.68424 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cc7f253-d0bf-330b-a1e5-015309459544 | -11.77898 | -49.5681 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 11256e56-0d9c-3325-b08d-5f5dadd593a8 | -7.25633 | -59.99926 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58b54e5c-f240-3149-86d2-5c1c5366f313 | -8.92644 | -60.73309 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 195e57d0-4667-385f-ac00-c059830bc9f4 | -7.07112 | -59.16318 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 905a32f6-9e4d-3583-be43-bf46e85ec521 | -11.39307 | -55.41347 | 2025-08-11 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8542d811-5a37-3ff1-8933-7a67c25b3463 | -8.93233 | -60.75592 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05e56a1e-0a6d-36a6-8c32-16eae5b15cf3 | -7.0751 | -59.20277 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 58cee1cd-ec35-3ddd-b86f-d8426af20378 | -8.9307 | -60.74473 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 241ac282-dbae-3676-9cce-bd9a554e21ff | -7.07564 | -59.19931 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9ae35360-ef22-3cc8-a94b-b5cfc02886a2 | -7.08327 | -59.17216 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94b94e4b-0259-3fa6-b94f-143d63cdd5de | -11.75928 | -49.11655 | 2025-08-11 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa9feaef-34cf-3d20-968a-8c5d12629824 | -7.06073 | -59.18636 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c784403-a28f-3842-bfe0-88714294cc5c | -10.37093 | -50.83704 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e595097c-5d4e-3464-ab87-62643e89e424 | -9.37314 | -61.52761 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e816e26b-26f9-33f9-927e-a042f6437fed | -8.56471 | -54.68483 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2954855-6be9-3106-b91e-83d203ce0294 | -7.08279 | -59.19689 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91f39881-8b79-3bd5-8a8a-9881349d6291 | -9.88637 | -55.3952 | 2025-08-11 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f273ddd3-6ff6-3d8a-933d-e5d98ed0d0c9 | -10.37177 | -50.8303 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b33fdd7b-6121-365b-b3f8-dde0ad551939 | -7.08441 | -59.18651 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad0e7207-343f-339f-9c7c-35f49350dfdd | -8.13514 | -47.42503 | 2025-08-11 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 3b2fea1f-02cd-3798-b8c8-da19a3d9f2a5 | -12.60804 | -47.14628 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf1afe58-c6f3-314b-8974-29ba0c3ae13e | -8.57424 | -54.70412 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README22.md)
