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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50cc55f4-a814-3f6e-9384-bd82cb42e9fd | -12.29261 | -50.28489 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8039c458-ee68-300f-8fa6-f7783c72b942 | -10.41301 | -53.81517 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96742a33-366c-3e37-a24a-fa78f8b93739 | -11.89034 | -50.51701 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32e83e37-5234-3baa-b9e1-930ee7ecfdb7 | -11.90199 | -50.51426 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ec47993-2c9d-3e87-a058-151f0fb9bebf | -11.85668 | -50.51644 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc20225d-a2b8-302f-9c7e-3c723fcc28c9 | -11.87869 | -50.51975 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 406d1559-8e72-318b-a770-e4b10e88029b | -13.38153 | -51.32018 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f61d59a5-5213-3151-9b07-31c726469a88 | -11.98423 | -50.56484 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ecd35d80-bc7d-3d29-b5c9-44c9125a9496 | -10.61232 | -53.99759 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b555df4-0f7a-3b3d-bf22-8995489ea4bb | -11.992 | -57.60619 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 376323e7-fe50-3ab0-a3da-e586a8612800 | -11.89704 | -50.52249 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 892d490a-f2e9-354c-a171-e87d59830c30 | -11.81695 | -50.50599 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf32488b-37ac-3af9-9282-5aac078da8d7 | -12.14057 | -50.32522 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e0b3034a-9672-39ed-828f-ea63e0e4e399 | -12.88915 | -61.71361 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25ac13c7-6a32-320e-a288-80a84e329af8 | -11.60924 | -49.86495 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf623a23-6311-3c63-983a-089bad3a4f72 | -11.86326 | -50.54874 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ff485da-7391-39d6-aa59-23b0b0548085 | -10.67849 | -57.63635 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3187333-9342-3654-9a14-91425aacd86b | -13.21164 | -42.23159 | 2026-09-27 04:53:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e4573a5b-d401-320c-b573-57344b4bcd6a | -10.89834 | -53.93292 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f459e2b-b0e7-3939-9e42-8369977475bc | -11.93738 | -50.49949 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0b7d7baa-de85-3467-97cb-147308582894 | -10.78642 | -48.73109 | 2026-09-27 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a59734a3-1fbd-3b38-b6c0-17540c5b7319 | -11.89264 | -50.52422 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b435a8d6-3fa4-3cc3-bdf0-67490620536b | -13.85231 | -43.99573 | 2026-09-27 04:53:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a08c176f-4f80-3d1d-90ed-693f87d43200 | -10.89892 | -53.9509 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cb50818-07f9-3aa8-a3f7-53ddb1749e33 | -14.50449 | -48.34085 | 2026-09-27 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2485518c-e1a8-32f4-a31d-ca7d94b7a5b9 | -10.02277 | -50.1445 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23667747-d12b-3ad6-a212-c4da20cc8f0a | -9.04096 | -66.05958 | 2026-09-27 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3651911-9c08-3362-a8fe-9c0f04085929 | -12.89104 | -61.71546 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93c95cde-254a-3e99-aa2a-2ed2454e72be | -12.90116 | -52.06366 | 2026-09-27 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85de96a6-bbeb-3289-93e2-f6e7bded55a5 | -10.89561 | -53.95038 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27d5b9c7-9dc7-3df2-9a2c-bd2817e21989 | -14.06662 | -41.93932 | 2026-09-27 04:53:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1f2a25f6-452a-30fe-9eb0-51c19ed3626e | -14.80516 | -45.95975 | 2026-09-27 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3baea3f5-5a98-3afc-91f9-b601e52a88d7 | -11.0523 | -51.32407 | 2026-09-27 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9715a335-29f6-3af5-9976-23c8bb9f7791 | -9.61573 | -55.10921 | 2026-09-27 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3341054f-50a9-3e62-99fd-bc3d7cd21243 | -12.26089 | -50.69423 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 66af50a6-0972-3b33-a46a-c9eea8b24961 | -11.03098 | -54.04012 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6c484f6-ae5a-311e-985f-cd2473c8d6d0 | -12.66842 | -47.30759 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cc99b57-1bb6-31fe-a179-4f1a97beb430 | -11.97071 | -50.58068 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a523179-e9a0-373a-a659-58657b9d17c4 | -11.89692 | -50.52037 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30a52178-2214-31fd-ac71-c72508ee0974 | -10.68222 | -57.637 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a53df31-4fc3-3d28-8d29-b48782b1ab8d | -11.08938 | -60.72315 | 2026-09-27 04:53:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51687828-55f2-307d-b6c3-2952f6cde027 | -10.81126 | -60.72391 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41c3bd14-39c2-38b8-99d9-a6a44f61da30 | -12.89752 | -61.7204 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e492b0be-1649-3ef4-a902-26152605b400 | -9.571 | -62.70811 | 2026-09-27 04:53:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cf3cc21-8418-3f59-8520-a8c568e9f588 | -10.8934 | -53.94286 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f84ad57-d6a8-37b4-b555-f292fd4dd170 | -10.89616 | -53.94688 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8442e85-9d4e-389a-8ec9-221ec90bf9cf | -11.98823 | -57.60648 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d98fb08-960b-37a1-8b6a-7cc89959b516 | -9.03976 | -66.05762 | 2026-09-27 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5de4e799-916e-3a77-9b93-62a1897b459a | -11.88906 | -50.52578 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39aec925-2e02-3c23-a33c-b337bb4a3db4 | -12.20917 | -50.377 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72df3fe3-895b-3bf4-832b-56b8592de5d9 | -10.92778 | -43.86706 | 2026-09-27 04:53:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b3ee7da-d30c-3b08-9efc-ca3bb3ec914c | -11.60858 | -49.86966 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79252b31-8efb-38f1-a540-17e308bed04b | -12.02696 | -50.6055 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bf459aa5-7735-3e4c-a67c-dbde7e7c333d | -12.47726 | -47.47952 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fc22013-0e92-38df-bd1a-7be14c5b42ca | -12.6711 | -54.64548 | 2026-09-27 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43bbf524-f884-3e67-b8c6-9d8ddb211e8d | -13.46291 | -48.59869 | 2026-09-27 04:53:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dffdb426-edc7-35fc-bcd1-9e127a15af91 | -13.34569 | -51.34039 | 2026-09-27 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd06d903-f798-3ead-b899-4833bb27470d | -11.05288 | -51.32013 | 2026-09-27 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 510d9c10-2043-3ee9-ab25-a65242bb5fe9 | -11.94168 | -50.49563 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e52f7a46-8140-3a13-98bf-d2ebd1199eff | -12.66782 | -47.31234 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40ec1d2d-0a07-32fb-943c-ea426d2dae9d | -11.88555 | -50.49834 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d859dcb-8d28-3a09-b307-bfb9f2e1bca8 | -12.03614 | -50.59349 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39719bbd-d1be-3a8d-9fb7-306166a9bdd9 | -11.77083 | -51.00858 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76c84eea-75be-3e5d-9535-19723fdf9bbe | -10.8978 | -53.93641 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42fdba28-d641-35ee-9ebc-7c1eb4e64223 | -12.28578 | -50.2792 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 991c4f89-ad91-349e-b21f-b3d1813de846 | -10.22281 | -49.9797 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 053feb2e-9a9c-3ecf-8268-1539c0e777f0 | -15.47535 | -46.15358 | 2026-09-27 04:53:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02afc618-2009-3554-ba7c-8c38789cf8bd | -10.92729 | -43.871 | 2026-09-27 04:53:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d05ea749-6694-3f71-8914-ae1d483b32f3 | -9.63922 | -55.13553 | 2026-09-27 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea16aee0-16c3-3f5d-966d-3465aa604896 | -11.93784 | -50.54893 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f2a7cf17-2de1-397c-94d9-4cc4384a8ce5 | -12.24018 | -50.37241 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| afbd8132-1500-318a-8b7e-7bb753fa5ad5 | -10.01769 | -52.103 | 2026-09-27 04:53:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| beb57f76-135e-38e8-8536-4b4d310e962b | -12.13908 | -50.32282 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77512839-6853-3598-8535-e82a1f619200 | -14.78573 | -45.94752 | 2026-09-27 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 562f100e-7402-3985-8842-881ef0117ae6 | -12.26517 | -50.69043 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c88c09f7-f10e-39e4-a495-5139c326648b | -12.25235 | -50.70182 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20d487f9-d62c-3cc4-96ed-6def59cb5938 | -10.67927 | -57.63184 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b546bce-1c07-3640-9d53-36671249a72f | -10.01724 | -50.15697 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 806f31ca-db7d-3f01-83ad-e46eee8091a6 | -12.70815 | -47.32268 | 2026-09-27 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6467e7d-4133-3ac1-b29d-b54ad1081bee | -15.47571 | -46.15059 | 2026-09-27 04:53:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c34da3f5-f75f-392b-9343-7c640015cef0 | -12.13777 | -50.33186 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 76c0342d-d308-37be-85b2-e73be2d7c6ac | -10.67555 | -57.63118 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89b23b6a-25a7-36c6-943b-22581d89f848 | -10.41795 | -53.80524 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11610c92-506e-39f1-8dda-f524f3119894 | -11.77023 | -51.01273 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 042a5ae1-5925-37af-be42-a726ad5afb4e | -11.89571 | -50.50224 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 746bd67b-0452-3f46-9daa-c34f662e96d1 | -12.47219 | -47.48343 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 96b95425-32a0-36b8-9d6c-453774b88f15 | -14.4171 | -52.80513 | 2026-09-27 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67528f08-8bc7-3d3d-9328-8725dcf7a889 | -12.2845 | -50.28834 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ae70099-6491-3862-acb3-6f70936e6fa8 | -12.28322 | -50.29747 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f226cce-0456-3b54-8968-733b4c56162e | -10.61177 | -54.00108 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff34fef5-a08e-36fc-8cd2-f905cfbf19c3 | -9.5725 | -62.70455 | 2026-09-27 04:53:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79d8e336-e2a0-3386-b8c1-93bfaf98a468 | -10.79137 | -48.725 | 2026-09-27 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fd9b2b5-23c7-3e2e-8051-1f481ea4e06f | -10.42179 | -53.80228 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a47de54-ce4c-3fe8-a9c9-c39460cbaf07 | -12.30137 | -50.27686 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dea69b16-08ab-3eb2-800a-bfbeea27757c | -12.13869 | -50.3388 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9596f08f-e64a-30fe-85ae-a2b7a8134372 | -11.02384 | -54.04254 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2892cc12-ff65-3c0a-a2bf-fb797c525e5e | -10.04083 | -62.45799 | 2026-09-27 04:53:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61b03d9a-0605-3565-96ae-0754f9e84fa0 | -11.95448 | -50.66703 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f02b9d8a-13d6-32ac-9137-60ba800bd458 | -11.94105 | -50.50004 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0188aac9-45b0-3ac0-8850-5ab9f195744e | -12.66354 | -47.30062 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README36.md)
