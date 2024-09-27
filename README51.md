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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8ef1bb7-994c-3410-b833-9bcd720205ef | -12.47184 | -50.42525 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61086645-0067-31f3-b4f7-ca644ea8ad6d | -12.47074 | -50.43068 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 239aa54b-703b-3f21-af66-7c411aa11605 | -12.34814 | -50.50565 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1592c441-6bd2-3e0f-8bf2-525c3c1dc42f | -12.34783 | -50.50642 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31947f9b-eab8-313e-a12a-24e97a561e96 | -12.3417 | -50.50421 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 22fdef7c-81a4-3817-bbf9-a0b67ed5957f | -12.34139 | -50.50501 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 12ef425a-89fb-364c-b54c-5eabd92d4cff | -12.27047 | -50.52311 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0046474a-0ec5-393a-847f-cc73edaa0569 | -12.26933 | -50.52864 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48ceaf66-abb9-32b5-b74c-b6adf99d8c54 | -10.72376 | -51.07733 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d51fce33-abef-34df-804f-49c96eaf83b1 | -10.72376 | -51.07733 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0a1adec5-7890-36be-b641-4020c03390b5 | -10.71826 | -51.06944 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1d51aa38-60b1-347d-b1f3-210e3eb74572 | -10.71822 | -51.06939 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c71b45a2-d2b4-3e70-89a4-ce7338138c12 | -10.71693 | -51.07583 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6c036892-4aad-3317-a2b7-c5af3efbc0d7 | -10.71693 | -51.07579 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8495477e-0027-3e56-b3ac-efbae4684d66 | -10.7101 | -51.07433 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| febf2730-228b-336c-b7d1-752458dcce16 | -10.7101 | -51.07427 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d7e4da70-632e-3e55-83b0-91a6e0bef445 | -10.70882 | -51.08067 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c607e877-f149-37a4-93ea-6919fd340665 | -10.70877 | -51.08073 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7aed6592-d822-3698-b0a2-8387e99cc035 | -10.67929 | -50.98056 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ee5b7bd-7145-390f-8e1c-ed01f87756d4 | -10.47937 | -51.18707 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90bab570-67b5-39b7-be67-746f5e3d940e | -10.47492 | -50.75814 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 509e82a7-f529-3269-af8a-2b53b7c4cdef | -10.47249 | -50.761 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 767a0ad1-1b58-3a9a-8bcf-12fe6376ee52 | -10.47223 | -51.18672 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55b5c29c-b45d-36c8-9861-fa771524403d | -10.46821 | -50.75654 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9433f36d-6623-3ded-bec2-3ea3f27c081f | -10.46699 | -50.76253 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b4b5bb47-282d-33ab-8339-60eb7927ba7c | -10.46678 | -50.75439 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8db26e7c-b7a7-36c8-86c2-b3f4fab4695d | -10.46559 | -50.76037 | 2024-09-27 03:47:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b6a8edd-d7ec-30a0-b258-efa3bdff0e6a | -11.12468 | -50.8323 | 2024-09-27 03:47:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c61d344a-acf3-3d56-a454-93ed94413950 | -11.12342 | -50.83842 | 2024-09-27 03:47:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 852fff4c-6c85-3396-92db-6cefc32296b5 | -11.12206 | -50.83271 | 2024-09-27 03:47:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f648ad52-730f-37d0-932e-5dc3bdace563 | -11.12084 | -50.83883 | 2024-09-27 03:47:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 921b8e79-cf2f-3578-a616-d171d6ea8e67 | -11.05433 | -51.38243 | 2024-09-27 03:47:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99f09ffc-8019-34bf-bbd9-286cd7ca7752 | -11.05296 | -51.38908 | 2024-09-27 03:47:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b5c429a-7301-323c-894b-b90d28e2ac86 | -11.05159 | -51.39575 | 2024-09-27 03:47:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed1a297f-fc2a-3980-a599-66dffb4ecaa5 | -11.05023 | -51.40237 | 2024-09-27 03:47:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9411e5c-c10a-34f0-bd23-3cff3c9ec37d | -11.03919 | -51.42089 | 2024-09-27 03:47:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 96892eb6-5907-3e63-b4ec-e2132fd6bc21 | -11.03781 | -51.4276 | 2024-09-27 03:47:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d089383-637d-321e-8f92-9d444c839a24 | -13.21766 | -51.27103 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2222729c-3fc3-3a9b-b5ee-81817018ac3b | -13.2164 | -51.27698 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d86669ca-f5a8-3ea9-afe2-ae8384ce1000 | -13.2123 | -51.26354 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fb873855-84f4-33bb-b792-0237fe0baa73 | -13.20977 | -51.27549 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba198cad-ae8f-3121-baf7-35b4ce5ed358 | -13.1834 | -51.25162 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc5e358a-0cfa-3f7d-8682-43ca4800fa1e | -13.18049 | -51.25005 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f478e8d-2180-33bc-81e9-0488cc71230c | -13.17803 | -51.24412 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6002d533-8576-3d09-af8c-1867677b94a1 | -13.17679 | -51.25008 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b132e68d-0679-3200-85ee-3b760d394145 | -13.17514 | -51.24259 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 874784c9-7bf6-3287-808e-65280392f3d5 | -13.17387 | -51.24854 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ec37770-262b-3dd1-9ec1-fd24b594f199 | -13.21842 | -45.64941 | 2024-09-27 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c318348-792c-3a80-a740-7bdde3b4eec8 | -15.64298 | -39.27511 | 2024-09-27 03:47:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2ba931c9-465c-3ae2-9309-eca3ad3d1036 | -14.72027 | -45.50314 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d533596b-fa46-3e74-baa3-b7cd3f6319a9 | -14.71662 | -45.49762 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0549899b-7e20-396d-8c3e-3c88cb2cda76 | -11.65225 | -44.52263 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2905da6f-9292-3eb1-827e-6ecfebb6c315 | -13.05338 | -40.34842 | 2024-09-27 03:47:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5b09d3a-da69-3f29-af70-0e020496fab1 | -13.02858 | -40.33331 | 2024-09-27 03:47:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 270c2993-ce7d-3c4f-8f5e-8041cbac53ee | -15.62563 | -40.50441 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c309a843-266b-3f8c-9c61-85fb4bf82d72 | -15.46026 | -40.09561 | 2024-09-27 03:47:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b92dac1d-f727-3efa-b64d-56b815b8c9c1 | -15.45689 | -40.09501 | 2024-09-27 03:47:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e275c772-d0de-38e5-86ea-9b816d2b5f7a | -12.15856 | -40.86097 | 2024-09-27 03:47:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc284d9e-eb53-3b9d-b6a1-5d14c6586b81 | -12.15788 | -40.86502 | 2024-09-27 03:47:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d64b8712-3800-32c4-a868-7ae248cfeca6 | -12.155 | -40.86034 | 2024-09-27 03:47:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b6bc347f-b9e4-3726-a975-c6e45bec8567 | -12.15433 | -40.86439 | 2024-09-27 03:47:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4b14a71b-801d-3b70-9ffe-b6d205bd3451 | -11.95848 | -41.29454 | 2024-09-27 03:47:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc80c7b2-cc88-33e0-b9dc-b831b5aecaed | -13.40787 | -41.32843 | 2024-09-27 03:47:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 1c5e81d8-ddb8-3b2a-a2dd-a094d044a185 | -13.26345 | -41.49651 | 2024-09-27 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c63507b3-8ee8-3a49-bfba-aa53917cb676 | -13.25983 | -41.49587 | 2024-09-27 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e03241f1-5ed5-3de8-a15e-e566e5231541 | -13.25911 | -41.50015 | 2024-09-27 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f2ffaa1-6f39-3840-b185-1f1ff4a328b2 | -13.25549 | -41.49953 | 2024-09-27 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 32708f5b-95d1-36c0-9888-0dd8ac310831 | -13.25476 | -41.50382 | 2024-09-27 03:47:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 090d1928-3e83-370b-a2eb-e590977ffab6 | -14.59889 | -42.00846 | 2024-09-27 03:47:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1389bf2e-257c-3144-8f99-be5bbeb9e156 | -14.13501 | -41.69337 | 2024-09-27 03:47:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9485a554-d437-3719-8a24-c39837fc44eb | -13.90937 | -41.2106 | 2024-09-27 03:47:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef189551-6abc-34eb-a118-0a6b4192abe8 | -14.45034 | -41.08141 | 2024-09-27 03:47:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46bec567-a4dc-333c-8893-47c3dd7f7313 | -15.47584 | -41.25785 | 2024-09-27 03:47:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3c57f34-7414-3da1-a6a0-54d4e6fb36d0 | -15.8026 | -40.97961 | 2024-09-27 03:47:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 623c0a06-eb0a-3166-b8e2-e212778b35a5 | -15.79915 | -40.97904 | 2024-09-27 03:47:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0e89baba-dc51-35d4-92e6-ee742d352544 | -14.71575 | -45.5023 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 216fb958-3462-3e02-ae7c-39dd2342af8e | -13.53671 | -42.56549 | 2024-09-27 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cfbedd90-2470-334e-b732-2a12c42e2969 | -13.53753 | -42.56071 | 2024-09-27 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2f6746c-9feb-3f91-8632-11f998bc2adb | -13.53569 | -42.56299 | 2024-09-27 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| dee8b4ee-7aa9-3f74-ba1f-f53adfc5c50d | -13.5337 | -42.56005 | 2024-09-27 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ebc66ce-6b06-36f1-80fb-e568ee8fdd4b | -13.53288 | -42.56487 | 2024-09-27 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af9536e4-b65e-34f8-9558-1d550cbd8293 | -13.01318 | -42.21877 | 2024-09-27 03:47:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 77590484-538d-3397-8f24-48894152f663 | -12.58851 | -42.4219 | 2024-09-27 03:47:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 06bd8ca2-7071-3d8d-ae9a-a7b5961d5405 | -12.43234 | -41.79807 | 2024-09-27 03:47:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d33a6d25-8192-3ef8-8c80-af62939fc8ea | -5.70668 | -43.17621 | 2024-09-27 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab5d5fb9-aa0f-3cb5-b526-2bcba81555be | -5.58198 | -42.93454 | 2024-09-27 03:47:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 151e29ba-672c-3dd2-bc30-b3c35096d16d | -5.58123 | -42.93903 | 2024-09-27 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a719a5dc-93f9-3ee5-aeb8-3fb2f3bfcaf7 | -5.57755 | -42.93375 | 2024-09-27 03:47:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1afcd3be-24d5-3603-b911-61aa12f0a212 | -5.57678 | -42.93826 | 2024-09-27 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5f8dc9f2-edc6-3be6-adaa-6c65d46bbd50 | -5.29909 | -43.07107 | 2024-09-27 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e8ce360-781d-3944-b0d1-cd7cda492286 | -5.29836 | -43.07556 | 2024-09-27 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33216d6c-9923-331a-aeac-dcb9d8767112 | -7.90314 | -42.67538 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85c6cb86-7e00-3b0a-9d9c-072c67911255 | -7.89827 | -42.67857 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e1bb896-e964-3ccb-b036-32ca21d06ded | -7.89406 | -42.67788 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4e2e9ffa-5010-37d9-bf5b-c74ddbf665ef | -7.87457 | -42.69039 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cdc3159c-8b66-3b1b-a13a-8068cad11e78 | -7.86966 | -42.69368 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cd2d2de8-32e7-313c-91a8-07f5eaacc799 | -7.86898 | -42.6976 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fc3ea6ea-de61-3e1a-a8f8-2e1f20cac1e3 | -7.86476 | -42.69691 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e1b42e1-b961-38fe-bb20-5a076529e08c | -7.30714 | -43.3262 | 2024-09-27 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9516d711-2a9b-33fb-ab3d-934720c0377c | -7.30357 | -43.32696 | 2024-09-27 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README52.md)
