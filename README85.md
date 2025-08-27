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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdfbf123-8ee1-390b-a6ce-0601769697c2 | -9.16344 | -59.56516 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7f0cec71-4022-3b3a-97e2-1ed7bca4cb1e | -8.89906 | -60.76177 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e805b544-16b3-31c8-ada1-0bd72a055aa2 | -8.72049 | -64.03016 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32326d53-6196-3127-9adb-465b1f61ec70 | -8.95949 | -65.95612 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 647a77eb-d158-3885-8e42-ba0938ad15c9 | -8.96213 | -65.96966 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7f79a31d-7b4e-3240-966c-e40ea1f23c21 | -8.33791 | -62.92924 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 169d183f-7ec7-3d05-9df6-f5a66e050a01 | -8.96036 | -65.9487 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1a1501ad-a29f-33ff-8921-b1fcde5e1034 | -9.04963 | -65.728 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e885f30a-4f08-36a1-a140-cfe9072a5eb8 | -10.08263 | -62.89848 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc5291e4-5f6f-3b58-9c02-ad24548b26c3 | -9.40563 | -60.50154 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 093a2965-5926-3882-b325-a04936daff93 | -8.34327 | -62.92998 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61ee16a5-a0d1-3b20-8550-07046f89461f | -9.82381 | -64.28695 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 722b63db-69c7-3fbd-82a5-e6e1ef7ca1cb | -8.51595 | -69.79266 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 466be988-19be-3053-8529-947387251bd6 | -9.04516 | -65.72733 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2494d5c-9b94-3241-9ffe-866b9f566545 | -8.90095 | -60.76022 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39726ac4-9583-35fb-9a6c-0b469cdd9cac | -8.67041 | -66.58726 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99eefd54-8917-389c-a895-e37da9cf1dbd | -10.03866 | -67.53209 | 2025-08-27 06:08:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa0acd9c-dde2-36f6-8376-4ac3a1445a39 | -10.08307 | -62.89509 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fea8c810-50f7-32e1-b1fe-545fe3ad527e | -9.69175 | -65.71816 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff3afea5-df5b-3557-a3a5-3130d44e0efd | -9.05964 | -66.07054 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03772720-de78-3e0b-a57d-5716185a06c3 | -8.07094 | -61.54246 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74b9dee4-caf5-3555-93b6-8e983279f685 | -8.94973 | -65.96026 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| c2350cb9-3427-3a8d-86f4-84809637748f | -7.48101 | -61.35106 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e875c5dc-feb4-3f8c-8e26-0162d752db9e | -7.5515 | -63.84134 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28bf545d-731c-3181-8e34-125c1b832d87 | -8.89473 | -60.75941 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8b18793-c78f-32a9-822e-5f902c2fd2a4 | -9.06401 | -66.07119 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fa81d10-f960-38b8-84f2-758e04340580 | -8.96651 | -63.3866 | 2025-08-27 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94bbf75f-b6e3-3d27-880a-f3d918b7718c | -9.80095 | -64.26451 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4e01584e-600e-37a1-b6f0-04405527dfb8 | -9.64577 | -59.62618 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d59aa8a5-3166-3d26-a1bf-02a85b72083c | -9.04008 | -65.73112 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6da63016-eb50-37b7-b055-d99940364c0f | -9.63693 | -59.64266 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb6a9821-f5f2-3160-882f-37c66e99a32a | -8.93899 | -65.94125 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 346d6560-1403-371b-839e-43f2d4d84236 | -9.28292 | -64.55788 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f441d967-6da0-3a79-8867-a264014a475c | -14.77198 | -59.71539 | 2025-08-27 06:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2127b9db-ddf5-3882-901a-0ebffd438929 | -8.95133 | -64.13361 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7dca93fb-458e-38d9-aa47-2b289b201d32 | -8.34729 | -62.94081 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b288912-6792-3c68-9c04-cbcb2fd9e5dc | -8.06486 | -69.91836 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1518a468-688f-38aa-8849-4272be0501d6 | -8.50023 | -69.80218 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7edf0c43-b0d9-35c8-8e31-f98df9cf326d | -9.07833 | -65.71851 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c455b2c8-70a3-3420-b835-3d6f9aa1de04 | -8.66987 | -66.59114 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9eed63f-8c14-3a12-8cac-ae5359946326 | -7.47881 | -61.36767 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8c25180-23b6-36b3-8223-23b287825f46 | -9.10538 | -60.31372 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfb3d5c4-3fa2-3082-8e24-b7322dcd6c51 | -9.8077 | -64.25221 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b0dc8e8-a39c-3d1c-a5e5-f439f502dc8e | -10.0932 | -62.90332 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bf3338e-7fb0-30b2-99c1-9e676200ca3e | -7.62079 | -61.03342 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae76e1f-12dc-3c8a-bddc-f44142dddcd1 | -9.00589 | -65.40176 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fecfd769-b9e9-32b7-9af7-e86dd5849278 | -8.65656 | -67.26795 | 2025-08-27 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e5bb96bb-9baf-30fe-a862-826e1cfaabe5 | -9.15753 | -59.5576 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55973458-72dd-37f0-8003-be4739512a21 | -10.08857 | -62.89587 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1206667-9ba2-3793-ae94-fbcf78c38ba8 | -9.17 | -59.51049 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac9d54fd-8826-334c-9719-5a2bf29ad143 | -7.74788 | -67.15216 | 2025-08-27 06:08:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c56b216-f30e-3b53-b4fe-dc9725d598bd | -7.60361 | -61.62765 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51d80ddd-5da4-3bfc-aabc-8a714e354939 | -9.64411 | -64.99435 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a9f9f8f-93b1-3306-81bb-4232388434ba | -9.1731 | -59.54152 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f03a409c-b823-32f7-84ed-1bd941ccc1f8 | -8.95913 | -65.95723 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c6ac9336-a15a-3e51-99ba-1671397c2b21 | -9.41514 | -60.52889 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f1df9d7a-2686-3c91-a4b0-fc75b769b1ad | -10.09872 | -62.90392 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd7ad99f-3e28-3d30-bade-958dc3cc8e29 | -9.79307 | -64.24731 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7564550a-a113-340f-a897-2aa971b6a31e | -7.38351 | -64.36147 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bdab5d7-80cb-3411-8627-d8a1d7e84921 | -9.14086 | -65.27343 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ee3ccf3-5eec-374a-8f45-88711306cf24 | -8.94216 | -65.95046 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8c9369cb-df0d-33ae-aa0c-cae888262968 | -9.16002 | -59.59367 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8caf6e6-64c8-3cf1-b107-3c9ddf1986a4 | -9.18344 | -59.5124 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d2ec2e5-b919-3d61-8836-09803284981e | -8.93338 | -65.94913 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 64fb950f-da2a-3244-8394-a239b896527b | -8.95251 | -63.37156 | 2025-08-27 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abe74c55-6fb8-3334-b0cc-72a97edc9586 | -9.17374 | -59.45702 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9eb0063-05fc-34db-b74a-b0952d2933bc | -9.40686 | -60.54359 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4191a8b6-3135-3772-b99c-c4db29e98277 | -8.06985 | -61.55048 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7a3e6e6-74cd-3cee-8695-b09e6f1b7dfb | -8.85681 | -62.44458 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a2583a5-4558-3517-ac86-377a9f9ea928 | -9.16979 | -59.54226 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa4b46bf-1fa1-312a-8a65-90b1d47c2841 | -8.65204 | -67.27088 | 2025-08-27 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c8f5a03d-a1f4-3757-b692-504f1c79b186 | -9.80709 | -64.29443 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a43959d-b67e-3170-a091-da3d7c89ed47 | -8.89165 | -60.77061 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a50e30c-e644-34fb-9b12-82487ba7d3ea | -8.9308 | -65.93569 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 9fa78ad3-b754-3daf-a1d6-ff1004249c1f | -10.09232 | -62.91005 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 82c5871a-54f5-3e27-b1c2-eb1d62739519 | -8.93838 | -65.9455 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 72d622f8-2c10-3764-bd36-be5a39e66cd6 | -8.96331 | -65.96099 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 67bfca23-680b-3c00-8cd0-6e188687101c | -9.18997 | -59.54469 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbbf2e29-e344-3b44-9033-84f713fca18e | -9.0541 | -65.72866 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1cb5272-dd74-3b32-86ae-c6952f0422a4 | -9.12 | -67.70895 | 2025-08-27 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be860364-d2e8-3134-a46a-0becd19f89ee | -8.96414 | -65.95358 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d90259e2-3955-38bb-b0bd-81112ab811ab | -7.62254 | -61.03611 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4848cd46-8cbc-35bc-8b5a-8b1365943174 | -7.47991 | -61.35938 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5058731-473d-3d45-89b6-768353b9b3bc | -8.9352 | -65.93634 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4160bc7d-e24a-350c-b53d-625e0e3080b1 | -8.96695 | -63.38336 | 2025-08-27 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a57d2e21-1ffc-3fbf-bc54-137e3858d909 | -8.84517 | -62.44682 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20bcc839-9e0b-36dc-8f84-e1ea067a331b | -8.99936 | -65.41513 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 144e557b-b30d-3334-854b-17790e2a53c9 | -7.54222 | -63.84047 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a6282f2-e92a-39ef-b7ee-492627239894 | -9.80269 | -64.25153 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3165ff62-1db1-30e2-9244-bf5b122416c5 | -8.89285 | -60.77392 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de11a3c0-a03f-3ebc-82b7-76d0804f1ea0 | -9.39673 | -60.52128 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b74435d9-9898-3051-9b40-e123658a674b | -8.46261 | -64.04889 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e635ec3c-9fce-32ef-b97c-50d0784265b8 | -9.79595 | -64.26384 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47962040-63d7-35a9-b72b-9f54c6b0ec3e | -10.27438 | -64.50398 | 2025-08-27 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3feaabaa-b4bd-37fa-a531-f2a755ea9002 | -8.5953 | -68.14977 | 2025-08-27 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52ee65a0-09a8-3170-a6fb-e4232b2dc015 | -10.08683 | -62.90929 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 062f5af8-ede3-322a-981a-ef8cc8d75dda | -9.41199 | -60.50239 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 180b44ef-12b0-3878-ac8f-aea6c44e53a4 | -9.40725 | -62.484 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e438bf4e-b7b9-3cb3-ab52-268d6480d560 | -8.93399 | -65.94485 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8ade72f9-0c6a-3634-8218-29978c6b654d | -9.15969 | -59.53957 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README86.md)
