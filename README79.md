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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 671b9612-f32a-357e-b2ab-41b875d84246 | -7.60381 | -60.95149 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c4cebf8-c4be-315f-b80f-824c1ab4dafe | -6.36458 | -58.33358 | 2026-08-21 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c24e092d-d086-36a5-9ceb-e78a39aae534 | -10.39223 | -61.20351 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 168588b6-5e5c-331a-b3d8-bd621de1c1da | -9.39603 | -60.55748 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a1fc153-2840-3759-83fd-ed91c1f221c2 | -6.55385 | -56.26038 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45ab7c5e-f33c-3089-b18a-da4148abb152 | -10.24598 | -54.37328 | 2026-08-21 05:42:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 490eb5db-386f-3fbc-bfdc-4b09a5a8755a | -7.86153 | -63.76276 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc22725e-970f-35a4-a075-3eb508316f9a | -7.05533 | -59.84469 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30b9d7ae-3dac-30cf-b7eb-97ff0b9dd5e2 | -6.83152 | -59.40675 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 323c89fb-8e28-3037-8208-2920572fcc3d | -10.39962 | -61.20465 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 295d7c13-ef0d-3e2e-8005-82faf28598bd | -6.57754 | -58.99162 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5945b80c-eea3-39fd-9cb0-d7a4530bfdf7 | -6.86226 | -59.44191 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6ffb742-ee12-32be-a274-c72f4705d963 | -9.05476 | -60.43568 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0607c6d7-0cce-303b-92e0-294a147d2d7f | -9.41244 | -60.42351 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0a8946c-b6c8-3b69-ab86-dd12d69aed49 | -6.38011 | -54.94977 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 321522c8-35e3-374f-baab-d956f9aa2d07 | -6.70128 | -58.94179 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78c97832-a353-3793-b7f4-daaa2489e58a | -6.10781 | -57.73952 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 142c7030-70fb-3e0e-ad0c-b32f1d5d90a0 | -6.5972 | -59.11921 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a16e577-9f09-3d1f-a2fe-5ffde1ab9e09 | -9.40933 | -60.4182 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| e68ffdc6-c74b-3a6b-8a5b-58fec164d4be | -6.86529 | -59.42202 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc3ab93c-c4b9-313b-a6d4-5bc0d615b832 | -6.90896 | -59.34365 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f6e6a66-e6a8-3184-924c-18b338790603 | -9.40873 | -60.54985 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2da3732f-83b9-36d9-96b8-04752ec28b26 | -6.64619 | -56.40554 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f254535-7f5a-3ccf-b1a1-38900e4a21b0 | -9.40722 | -60.43234 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6be3047a-65f0-3dff-94f4-1a63518a10b8 | -6.77324 | -59.44893 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a09956ac-ae0e-3b96-8021-61a0c84e1f88 | -7.87425 | -63.76834 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd70d89b-8059-3fae-97ac-4e6961a02eec | -6.60755 | -58.3914 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4e32c3e-8847-3111-a6aa-aa479c8b2a87 | -6.35926 | -58.3406 | 2026-08-21 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6cf75e3-5708-30be-9202-31ebd22e9d0f | -6.70477 | -59.09521 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14082ff7-36be-35ef-80e4-16845429d2e5 | -6.89421 | -55.71688 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d313796e-1731-3bb1-a58a-c83f5f05578e | -5.8104 | -55.72319 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73cca352-543f-3d05-923a-a27bc9cf547d | -7.88711 | -61.6689 | 2026-08-21 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34c21df6-4928-3bd1-95d6-866df491bb82 | -9.2099 | -60.77223 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 172db5cb-f80b-387b-859b-973339741de2 | -8.39158 | -62.69363 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3db043e3-566f-3c5b-981b-b29be206d2f4 | -6.7178 | -59.08986 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 335a7be9-8c89-3969-b6cd-e928de684941 | -6.71329 | -59.09279 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8544d62-3041-3cc1-85ab-f59090573b66 | -6.66307 | -56.35448 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 87e7f8cd-7d77-3581-8c66-cfe3fc938999 | -6.86575 | -59.41943 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f43eae5-151e-3e63-a00d-fa30269d5a00 | -7.77755 | -61.15579 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b39f65bf-e202-3bb4-895a-068c25ddca2b | -6.10223 | -57.71735 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcdc8ab9-90a2-3814-ab71-a5a7684dec29 | -9.22315 | -59.77817 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a6e6c0b-d5cd-3c30-b8b1-cbb9c9add011 | -6.87607 | -59.43111 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 812e0909-1ad8-3088-98a3-8b1ed6aef196 | -9.17384 | -57.00933 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0a45e61-b7c0-33c4-a77d-b52ba8e51610 | -6.24935 | -55.41037 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2c919b7-ddf0-31d1-b7a9-4d5f527d85d3 | -6.56968 | -58.96185 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fca8e6b-b92c-3f28-9428-344dabd37305 | -9.41547 | -60.42136 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6537af54-3463-33f7-8669-b9ded741a245 | -8.57916 | -54.75155 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa671289-ca4c-31c0-9512-336f3e278a07 | -6.70078 | -59.09463 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1df52399-c798-38f6-b07a-502487b8444c | -8.58521 | -54.74913 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f58b5c2-7b28-3084-b9a4-bfa93bdc1a97 | -6.89248 | -59.42842 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b60cc95-b863-3f09-b8b9-838827275ded | -6.42339 | -52.74792 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f4aeafb-e0b7-3c79-80f7-1c60e767defb | -11.16669 | -54.0343 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ede1acee-db80-33cd-8a74-7320e4d65500 | -6.8673 | -59.03002 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4444ad62-c049-3790-86fb-8715a5063c90 | -9.21054 | -59.78151 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e63dd26b-0cbd-371f-bbbb-2aecbc6a5666 | -6.20681 | -55.48919 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f4f02e9-8b5b-3bbd-a7c7-7b057ac28045 | -6.85986 | -59.4314 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8164314c-d0e2-388c-907f-b0534a59c5a6 | -9.20618 | -60.77165 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abcff576-f736-39f2-a74a-49c1e91c82e9 | -6.16112 | -55.44604 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f9f54ef-26ee-3498-89ae-5f7d7e40bf79 | -6.5805 | -58.99917 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5dbc9ac8-61be-3806-87b0-5538d952b9b9 | -6.83544 | -59.40734 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 610ef194-65e8-37db-b2a3-f658b997badb | -9.21919 | -59.77759 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dab29c28-b53f-337c-b77b-e0734a693e00 | -6.22487 | -55.61359 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8089af1f-178d-3a83-b81e-fb3f73e98a7f | -9.41074 | -60.40874 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 93763e14-e437-3f19-9d06-36c5b8fdee25 | -5.49638 | -60.13214 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 684fc51e-8835-3718-8fa4-d1142b895fc0 | -6.92791 | -59.35171 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22e1e8ec-37a4-3d7a-99f1-a4af313150e3 | -9.39158 | -60.56157 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c1fb254-9ee7-3c80-8b91-75b2c465ea3d | -9.40561 | -60.5446 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c272c205-400c-3c16-8a81-acdce4f9ae1b | -6.4335 | -56.18634 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f997bdb8-ba52-3c36-8bef-49dd9a6bcb5c | -6.87183 | -59.02713 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 454d7c46-1224-3153-9e27-35a1fde3324e | -7.05595 | -56.51177 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18cc197c-b87c-3386-b8a4-914eb43481e5 | -8.28592 | -62.8972 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 755a9a1a-ae0f-3951-99ab-b9d6f0842cab | -6.08658 | -57.91179 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84000c45-9a51-3ca1-9294-b8ff59a619f5 | -9.212 | -59.77129 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6186c811-a673-3374-8ddc-b3b882fc45c5 | -6.86542 | -59.44746 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0407f9b-53e5-3072-90f5-1f41ca2c53ef | -9.24964 | -59.81861 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74824a52-7d5d-320c-83c7-b499bce419d2 | -6.42668 | -52.72674 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a331dcc-4917-38d9-86b4-72240b44f1a8 | -6.86677 | -59.43995 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e379d581-0ff5-30e3-9b80-61ce4469cce2 | -6.20217 | -55.48548 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5d764eb-fda6-3e7a-ad6a-17435031b49c | -8.38648 | -62.7041 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88999d9c-d1b0-380b-b462-4ff8a1758cc7 | -8.54726 | -54.77995 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 997cb55e-662f-3c09-9fca-174a2f8a6856 | -8.37969 | -62.70304 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7d7d77c8-ed7d-3ab1-82b1-522e3e72cc84 | -9.39354 | -60.55007 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b546cc2-cef6-3386-803f-5a6c98809234 | -6.70236 | -58.93464 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0809c7ad-f816-3a6e-aa75-335177c8de6c | -7.60342 | -60.82716 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| feb71e0f-7508-34dc-a6bb-fe8b8afe35cb | -6.42604 | -52.72916 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e92fbcf-8b8b-3f16-be61-277f19530aa5 | -9.42379 | -60.41778 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5550f44a-779c-399b-aebe-af931816a928 | -6.89339 | -55.72281 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e78797a-3c2b-3a02-8d50-cf39e9c00696 | -6.7686 | -59.45329 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6dbce696-c574-3887-aa47-b1f3420e6e99 | -9.41794 | -60.43136 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04f75f46-dee0-32e1-af33-407f352d6a20 | -8.57978 | -54.78814 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba04c0eb-44ae-3b18-88c7-d5c502db72e4 | -8.56903 | -54.6598 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2441364a-4814-3519-a257-fb2e828f622e | -7.77629 | -61.16404 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7a3e7da8-1aca-35e7-a301-ef93d8a1dc2f | -9.20766 | -59.65874 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e21312f-ae1d-307d-971a-c4f500cee9a8 | -10.38896 | -61.20952 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 870dbdfc-d793-3ed2-a181-624b3a2110d4 | -6.90229 | -58.98837 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8eaf5d7d-fce7-33c0-8b5f-2aa8f1b3febd | -7.60277 | -60.83143 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72d3aad9-1f19-3015-bffa-a92aa24a7e80 | -7.74254 | -61.09539 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52983556-9ee3-398a-9ba8-ede7f518f015 | -6.43282 | -52.72527 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da23e099-c4d8-33ca-b637-1756c757e4aa | -7.77459 | -61.1511 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 030bb84c-3eea-3c69-9349-255fba3dbf44 | -9.39594 | -60.55989 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README80.md)
