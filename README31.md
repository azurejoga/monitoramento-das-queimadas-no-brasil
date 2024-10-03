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
| 0a6e0d6e-3170-3ea2-9f46-66426c948f0d | -7.725 | -49.8918 | 2024-10-03 01:05:36 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00eb6f59-81a5-3b8c-87e8-9dd515a8d414 | -7.7818 | -50.221901 | 2024-10-03 01:05:37 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67ac37af-46c8-3389-92d5-0e2ef3f7120c | -7.7836 | -50.229599 | 2024-10-03 01:05:37 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a9a691-f1c0-37ea-a0f2-4456bce4ee3b | -4.6468 | -47.438702 | 2024-10-03 01:05:37 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d603640-8378-3196-8643-5a832306d14d | -9.8979 | -60.073299 | 2024-10-03 01:05:38 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae0e593-13c1-322d-9753-4f08b46805d9 | -9.9014 | -60.090099 | 2024-10-03 01:05:38 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bdedaa6-51b2-3efd-a868-823ba3973b2b | -7.1109 | -47.872799 | 2024-10-03 01:05:39 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85bbc400-2b34-36ea-b06d-1f53f5e047b5 | -7.1133 | -47.882999 | 2024-10-03 01:05:39 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc7ee1f4-ed37-3184-b25d-57aa1c3b85af | -7.1036 | -47.8853 | 2024-10-03 01:05:39 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a058a853-90f2-326b-8051-779f30cbad4a | -8.707 | -54.824902 | 2024-10-03 01:05:39 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8ea842-0e2a-3dd6-af2b-aeee2fb533aa | -10.6043 | -64.039597 | 2024-10-03 01:05:39 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cfffe58d-29ac-3ba8-a1f1-77a73c4676e7 | -6.1126 | -44.0453 | 2024-10-03 01:05:40 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc36842-3512-3534-a0bb-285060fb2f0b | -6.136 | -44.139599 | 2024-10-03 01:05:40 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c2ff462-8856-38a8-9ef0-b8b6853c995d | -7.0668 | -48.0327 | 2024-10-03 01:05:40 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b878bd91-72d0-3999-b235-d9f083774cb9 | -7.057 | -48.035099 | 2024-10-03 01:05:40 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75739612-56ee-328e-8ec3-b04d255e21f9 | -6.9461 | -47.659401 | 2024-10-03 01:05:40 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80478ee3-3912-3b37-a678-450470ff9cf6 | -6.9487 | -47.669998 | 2024-10-03 01:05:40 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5dd17d16-ad29-356b-93a2-bfd518d561e2 | -5.0596 | -49.789299 | 2024-10-03 01:05:40 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 241a831a-d19f-3aae-a16f-1c6f9c70743a | -5.0616 | -49.797699 | 2024-10-03 01:05:40 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef47d60-0f5c-3107-af89-1d4a9585d394 | -9.4643 | -58.9599 | 2024-10-03 01:05:41 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6565479-3b8f-3587-af2d-9a63f29628a4 | -9.4672 | -58.973801 | 2024-10-03 01:05:41 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5c86fdf-96a8-3cdb-a2eb-7261b067d3f4 | -4.5758 | -48.0047 | 2024-10-03 01:05:41 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0125d7b-9536-3b8b-9901-c5316be23321 | -4.5784 | -48.015598 | 2024-10-03 01:05:41 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406050e3-07a3-3a87-861d-7b6c41a5c582 | -7.1957 | -59.786499 | 2024-10-03 01:05:42 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4974d713-e93c-36d2-bb08-c28c3316f514 | -7.1988 | -59.800999 | 2024-10-03 01:05:42 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 868b3907-d396-3e38-8583-40df158dd934 | -7.1859 | -59.788601 | 2024-10-03 01:05:42 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21f3fe0c-3444-362d-9bce-235f34726696 | -6.0035 | -44.557499 | 2024-10-03 01:05:43 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da9decbc-7a9f-334e-aab7-e253e92af555 | -4.4865 | -48.105499 | 2024-10-03 01:05:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 117db50f-2d51-3588-a8ae-4207e743821f | -4.489 | -48.116199 | 2024-10-03 01:05:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc3641bd-3e05-37c8-b568-308232f2cb70 | -6.8675 | -59.019402 | 2024-10-03 01:05:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7246b713-55ce-3a3d-af5e-dfec71de6edb | -6.8703 | -59.032101 | 2024-10-03 01:05:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fbc7687-bab4-3f0b-a771-64e68aacdc85 | -6.873 | -59.044899 | 2024-10-03 01:05:44 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a53c6ad9-4400-3171-b0c7-6c692e0f3d71 | -6.8777 | -59.0504 | 2024-10-03 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 37514c34-33c6-3905-8c20-6f927de44851 | -6.8778 | -59.031 | 2024-10-03 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f2fd2567-48e4-3307-9118-4462a24b802e | -5.8486 | -44.595501 | 2024-10-03 01:05:46 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 074879d0-5d18-3432-b67a-60817932fb65 | -5.8529 | -44.613098 | 2024-10-03 01:05:46 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a955f2c6-d1b1-30f6-8856-f6eec599a76c | -5.8389 | -44.5979 | 2024-10-03 01:05:46 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe37893-7d35-3a73-8250-e56851a8dcd7 | -5.8432 | -44.615501 | 2024-10-03 01:05:46 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc733b5c-bcc3-3dc6-ad43-47e0873905c7 | -7.4932 | -35.2871 | 2024-10-03 01:05:47 | GOES-16 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| fc8763a7-c06a-3d1a-bf2d-521259c8f838 | -7.4936 | -35.2597 | 2024-10-03 01:05:47 | GOES-16 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 83.0 |
| bd10fc5b-e79d-3ca6-ae8d-236beb89f3bb | -7.2056 | -59.7886 | 2024-10-03 01:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| bccb921f-f063-3eb2-bcd0-26e289a3c894 | -6.965 | -49.4263 | 2024-10-03 01:05:47 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0614d7bd-0625-32da-ac8c-481c8b2b9c6d | -6.967 | -49.4347 | 2024-10-03 01:05:47 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 073887a5-0836-3d13-b941-4aee0934c1f5 | -6.7056 | -59.120499 | 2024-10-03 01:05:47 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c560fdca-9efd-3968-8c92-141ad0536dcc | -9.3854 | -61.033501 | 2024-10-03 01:05:49 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0a496c2-58dd-3c75-a661-41f32f422f6e | -9.3893 | -61.052601 | 2024-10-03 01:05:49 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8daf8fbf-40f1-3572-81d2-9f5886a6a1a0 | -9.3757 | -61.0354 | 2024-10-03 01:05:49 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 150a6690-65c1-3e92-8c8e-f8e39da1988d | -9.3796 | -61.0546 | 2024-10-03 01:05:49 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 834a0926-f9aa-31eb-a5dc-21dc34d4284c | -4.0998 | -48.473202 | 2024-10-03 01:05:50 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccf194f-7125-3edb-8939-02af000cd749 | -4.1023 | -48.483501 | 2024-10-03 01:05:50 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78511db-8a8c-39e1-87f7-29b445dfeef7 | -4.1047 | -48.493801 | 2024-10-03 01:05:50 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d5fca99-a1c7-3f83-9379-7e8c8023b047 | -4.0876 | -48.465199 | 2024-10-03 01:05:50 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01f792a9-eadc-345b-b647-eb239ab670a7 | -4.09 | -48.475498 | 2024-10-03 01:05:50 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa4e3f2-795c-3d31-a414-76856e94021f | -4.0925 | -48.485802 | 2024-10-03 01:05:50 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef7487ae-9bbd-3b2e-a2c7-b303420ac561 | -4.0949 | -48.496101 | 2024-10-03 01:05:50 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6ca282-ab90-346b-8352-72e5dcb7fb4b | -7.9093 | -54.750599 | 2024-10-03 01:05:51 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6601419-ea34-3115-a82e-7fdcc5b7103d | -7.8995 | -54.752701 | 2024-10-03 01:05:52 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ef56e3-6c3b-354b-a645-37cd4a38608b | -7.9012 | -54.7603 | 2024-10-03 01:05:52 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 941f7531-de41-33c2-a767-5202d2bdf116 | -9.4836 | -62.365501 | 2024-10-03 01:05:52 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd8612d-e65a-3cab-a879-96892b2e8d73 | -9.4884 | -62.3894 | 2024-10-03 01:05:52 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 502a8589-7ff7-3977-831f-5895269af62d | -6.1185 | -47.262199 | 2024-10-03 01:05:52 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 523fb0aa-3b5a-33a1-8335-0e7e43d939b7 | -6.1213 | -47.273701 | 2024-10-03 01:05:52 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48e28ed6-dfc8-3ab4-a1e4-67518a9f7e49 | -9.4739 | -62.367401 | 2024-10-03 01:05:52 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 60b00c53-a921-3c33-97a0-d65ac4d31e4c | -9.4787 | -62.3913 | 2024-10-03 01:05:52 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee0d586-9e97-3653-9a13-9f1f420f4fee | -9.4643 | -62.369301 | 2024-10-03 01:05:52 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 834b53c0-8296-3e21-9b7f-acb5ffb1cbb0 | -9.469 | -62.3932 | 2024-10-03 01:05:52 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| afbd005c-0238-3134-9332-df14b60df45a | -3.8054 | -47.795601 | 2024-10-03 01:05:52 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b52e2055-b1d2-362d-aef5-367dbc46ba5c | -3.8081 | -47.807098 | 2024-10-03 01:05:52 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae62c0ff-a968-3deb-a3d2-7c82b8596998 | -5.2362 | -43.779499 | 2024-10-03 01:05:53 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1cdf0d3-e02d-3125-b098-4df67f23c893 | -5.2412 | -43.799999 | 2024-10-03 01:05:53 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc6173a-4ced-3bab-b216-dba12b8a400f | -5.2463 | -43.8204 | 2024-10-03 01:05:53 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a5e8c81-b57f-3bfa-8e61-802cfd97db8e | -5.2265 | -43.781898 | 2024-10-03 01:05:53 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9faefa1f-b4fb-3989-b14d-ce2cb0035fc1 | -5.2315 | -43.802399 | 2024-10-03 01:05:53 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e72be144-b740-33f1-9b84-ef8ae93de30a | -5.2366 | -43.8228 | 2024-10-03 01:05:53 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c2eb456-c6c3-3f65-8d51-46a72b095eb5 | -3.7957 | -47.797798 | 2024-10-03 01:05:53 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95128103-d171-356b-a564-cabb35d404c4 | -3.7984 | -47.809299 | 2024-10-03 01:05:53 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f690220b-21e9-345f-bdea-085d89177cbe | -9.7502 | -64.269096 | 2024-10-03 01:05:54 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54e85ab5-ccbc-3767-b04a-2b2770419d5e | -9.7183 | -64.208199 | 2024-10-03 01:05:54 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f787e305-9a68-34f4-88d9-fa39be50ec54 | -9.7087 | -64.209999 | 2024-10-03 01:05:54 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fe83f761-2486-31f0-9e1b-7ac56d4fa7f3 | -5.9668 | -47.273998 | 2024-10-03 01:05:55 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f7a8568-a3e6-3711-8e38-151ab97fdc3c | -5.9696 | -47.2855 | 2024-10-03 01:05:55 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f474c074-1b1b-3c88-bf8e-43bd728f1122 | -9.1698 | -61.661098 | 2024-10-03 01:05:55 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a04de79-2622-3cf0-a3ab-d2a6a86c1beb | -9.1558 | -61.642101 | 2024-10-03 01:05:55 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e944d3f7-fb20-3535-8b12-ed8e47254afa | -9.1601 | -61.662998 | 2024-10-03 01:05:55 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf4e1549-144b-36f6-98fa-995b6c45e2bc | -9.1644 | -61.684101 | 2024-10-03 01:05:55 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a321b230-0dfa-39e0-9d39-09e443a4f2e4 | -9.1504 | -61.665001 | 2024-10-03 01:05:55 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9497c2bc-f791-3aa4-b927-850b33baf120 | -8.8506 | -45.5086 | 2024-10-03 01:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 8a1525fb-8319-3215-978d-dfbe0f9aed4c | -8.8695 | -45.5066 | 2024-10-03 01:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8ca8e0a6-806e-3745-b273-1f0d497acdd9 | -8.6488 | -66.7139 | 2024-10-03 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6649215b-d200-3770-b179-3680dd0376aa | -8.6675 | -66.6762 | 2024-10-03 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| bb93b45c-0701-3858-901f-0fb72593707f | -8.8926 | -62.3348 | 2024-10-03 01:05:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 5745d58a-df6c-3afa-b156-1c208e5089ce | -8.9791 | -67.4099 | 2024-10-03 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| f33589a6-d962-3070-b7e7-4ea564224e89 | -8.9976 | -67.4094 | 2024-10-03 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ddab159e-f882-3fab-9da2-600fbd24c612 | -9.0149 | -67.7423 | 2024-10-03 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 3b49cb66-5d7b-395c-aeff-aa23e854c548 | -9.1674 | -48.736 | 2024-10-03 01:05:58 | GOES-16 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 61.2 |
| bcf495ab-2ac9-3a83-994b-613c8f0e84aa | -9.0334 | -67.7419 | 2024-10-03 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 98d609c9-0507-3b43-8b03-4f71cfc7035b | -9.0515 | -67.871 | 2024-10-03 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a3ce362e-4ace-3c7b-b820-e5228249ea46 | -9.0516 | -67.8525 | 2024-10-03 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 7ba44364-94a5-3ec8-ac57-7db39aafa5b6 | -9.1566 | -61.6758 | 2024-10-03 01:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 2d6790e4-4b1e-3694-a688-abf993b61b7c | -4.9259 | -43.768002 | 2024-10-03 01:05:58 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README32.md)
