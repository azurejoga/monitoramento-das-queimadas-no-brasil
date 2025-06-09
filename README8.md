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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae7003f4-f2d2-3c05-951d-c108d0d24dd6 | -11.78337 | -54.7823 | 2025-06-09 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50ae6848-e698-3194-bd7d-4a6ca6b12e10 | -10.36259 | -57.50003 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c1a12d6-cd5f-3275-8811-e4cc9faac90b | -11.91293 | -54.82649 | 2025-06-09 05:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2debe7ef-6765-3bea-81cf-4c2900e4da48 | -12.16066 | -57.73262 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51d0e4c1-ddfe-3c70-a8f7-e82af78c6d54 | -10.37047 | -57.50367 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ef97535-a977-384b-b897-19e8b1035d68 | -10.36668 | -57.5031 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b57f1bd1-de1e-356a-8a51-f2130bb5700d | -10.36572 | -57.50525 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eff97bfe-22af-3750-b43a-6d808eca8201 | -10.84466 | -53.7772 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8581d46b-c06f-3f85-bbe7-efae7f86397d | -10.36289 | -57.50252 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a62b0a5f-4a0e-332e-b9b3-565c4f411e8d | -10.85371 | -53.78385 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe8b9695-058d-3eb2-b30d-6d68097390f2 | -10.36599 | -57.50773 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eda9a20-bee8-307e-991e-1f2f3b8c3bd0 | -10.83978 | -53.77645 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 236fb7f6-011d-3680-8bf7-c7c49beb344a | -11.78864 | -54.77816 | 2025-06-09 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8ee45fe-c9f7-3403-949b-a0f31e2e8f75 | -10.36193 | -57.50468 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81dd8b9e-d46a-3e0a-a9a2-da9d5088f511 | -10.37084 | -57.4965 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb9f224c-a442-36bf-8741-b21c21a9b593 | -12.88137 | -61.64336 | 2025-06-09 05:25:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 714eb082-5815-3093-adb2-2327fb15fddf | -14.86701 | -49.20216 | 2025-06-09 05:25:00 | NPP-375D | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ec4d8a99-037c-3f0b-b64e-20c38570b4f7 | -14.03614 | -55.13318 | 2025-06-09 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecec4764-a2bb-3a51-bd02-1183bd327e73 | -8.92775 | -63.90064 | 2025-06-09 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cd17ddd-aca9-3c6a-938f-bc0617cd07c5 | -2.58799 | -51.92189 | 2025-06-09 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 279cd4ae-9f35-35bd-aa13-3efd3417fc10 | -11.38232 | -56.5574 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8145ffbb-c478-35eb-8957-a3e7adbfb052 | -11.38282 | -56.55377 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c11d1542-9ae3-3d22-90dd-717d9aecd955 | -11.29991 | -54.70699 | 2025-06-09 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5558cbf6-d03c-3006-b1b0-4739370be388 | -11.12266 | -54.64345 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 024397c5-f86d-3949-8166-0c89aafa74cd | -12.1588 | -57.73004 | 2025-06-09 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c462939-37c6-3621-9c63-e4ebe81adf0c | -9.40411 | -48.44195 | 2025-06-09 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40d4327a-7b00-3bbd-9a27-b457f22cb521 | -10.85299 | -53.78922 | 2025-06-09 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68cc9040-7c6c-3508-aa8c-42d157b708a7 | -11.3869 | -56.55437 | 2025-06-09 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62866618-65ab-3435-b2fc-bd34cfa67c65 | -11.87351 | -56.0693 | 2025-06-09 05:25:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b484bdde-0f45-3028-99ec-71759a84efce | -12.37152 | -57.40348 | 2025-06-09 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5d8dfe5-24c3-3fc3-91e3-0facf24f0968 | -12.35163 | -57.43137 | 2025-06-09 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c7266ec-6482-3192-b267-18306a6ed2b0 | -11.38215 | -56.55475 | 2025-06-09 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e8f26c9-689f-3413-9647-7dbdb584a7b6 | -12.37136 | -57.41499 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e44047c-4b75-3cc5-aed8-f184a7927675 | -12.37235 | -57.40649 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 692d3add-a112-3df4-b204-8b2b77852a2f | -12.37285 | -57.40223 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a0f4232-196d-3440-9b16-45fb0ce9230b | -12.34716 | -57.43115 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b91afbe8-d3d7-3f3d-b67f-d54cc47dbc28 | -11.36924 | -56.55795 | 2025-06-09 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0dc84a3-08fe-3088-aef8-c8999e6c6bd9 | -10.36644 | -57.50239 | 2025-06-09 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36a9e146-5202-39e3-b390-833b4eef0cd4 | -12.53004 | -58.34816 | 2025-06-09 05:48:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8df984e8-5ec7-3c3e-8849-b41b120ea416 | -10.37217 | -57.50317 | 2025-06-09 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21fec4ce-d62b-3916-8a00-76f89696ef26 | -12.88262 | -61.64231 | 2025-06-09 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f424f7dd-209f-3047-b2a3-43b7b5becff1 | -12.37186 | -57.41071 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5babdb47-ce08-32d3-887f-a00cada62d39 | -11.38273 | -56.55004 | 2025-06-09 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78bcdb6e-c9b3-3b5e-ac70-ee5d9c25c0c8 | -12.36594 | -57.40997 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1110e9bc-2197-3caf-8b46-46f2ccd86b30 | -11.36867 | -56.5626 | 2025-06-09 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb9bd8f-1cc0-3825-9ab6-17804ae94f3b | -8.92861 | -63.89834 | 2025-06-09 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c68e01a6-f51c-3986-986a-00a3d641507c | -12.35205 | -57.42635 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51a526d3-8acf-3628-831c-dc686adcf8c8 | -12.35308 | -57.43177 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 708c4e88-ad6d-343e-aa96-26c003855442 | -12.15711 | -57.73137 | 2025-06-09 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77603b83-8e52-3c7b-83d8-83a1dcd7ce55 | -12.35154 | -57.43072 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a22e0bb-b94b-36fa-84dc-231bb49be5c3 | -12.882 | -61.64685 | 2025-06-09 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36a1f283-34d7-3292-ba8d-613f12a92476 | -12.16291 | -57.73193 | 2025-06-09 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cc30c27-0165-33f2-b4fc-8bf639d5cf4c | -12.35361 | -57.42744 | 2025-06-09 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e17e9716-b08e-39a4-91b7-e2a8e53ab36b | -7.92996 | -61.55877 | 2025-06-09 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80f88659-acc6-31ab-9f42-f4d82b9725e5 | -12.52448 | -58.34735 | 2025-06-09 05:48:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abcc7c80-0a5e-3272-8330-32201dc0d8b0 | -11.38199 | -56.55291 | 2025-06-09 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35e68513-f991-3bea-8ea3-02d58d01ec6d | -9.47529 | -63.98871 | 2025-06-09 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 946b94d5-5cc4-3640-9e3e-d2fe2ea5d0a7 | -10.36695 | -57.49839 | 2025-06-09 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3511661f-f0d3-323c-b700-ebd4c9f282f8 | -12.88018 | -61.64492 | 2025-06-09 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c07b072-6adf-3573-9e96-59db195041cc | -10.36594 | -57.50636 | 2025-06-09 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d495921-8d05-3304-85f7-b10f449e6692 | -14.2252 | -45.4804 | 2025-06-09 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 8b9adcf4-bd6b-33ac-ae6c-53d181f0b21f | -14.2252 | -45.4804 | 2025-06-09 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| ebc8d60a-c1aa-3154-8c1e-960a466b3327 | -14.2057 | -45.4838 | 2025-06-09 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 7a976cf2-7fbe-3436-af68-6a3533af2c7f | -14.2252 | -45.4804 | 2025-06-09 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| e9a92fec-f768-3a4a-b5fc-efb3c93f1fd8 | -14.2447 | -45.4769 | 2025-06-09 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 2c5dd18b-a990-3972-accc-f4fb0e60c610 | -14.2447 | -45.4769 | 2025-06-09 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9778315c-9ab2-39f8-97a8-9f597e6f060d | -14.2057 | -45.4838 | 2025-06-09 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 44819bd7-e1e3-392e-968e-0205cbd38173 | -14.2252 | -45.4804 | 2025-06-09 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 240.2 |
| 9392f199-04cc-3f2a-a3ff-4cfddebc8fe3 | -14.2442 | -45.5002 | 2025-06-09 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e2b0a702-f056-3ef6-b75c-f72a716754f0 | -14.2252 | -45.4804 | 2025-06-09 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 266.1 |
| c26ebd58-da4c-309e-b0cf-2c279269bfb7 | -14.2247 | -45.5036 | 2025-06-09 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 18058d60-83ff-3cdc-8832-636874b4beef | -14.2057 | -45.4838 | 2025-06-09 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 54d1a8a8-fc62-39c1-8731-e78f71fc8977 | -14.2447 | -45.4769 | 2025-06-09 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| a57b4ec9-02f0-34e5-a7a8-7a20e2a2df99 | -14.2247 | -45.5036 | 2025-06-09 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 900861bf-89b5-363f-97ac-c1c91878d7bb | -14.2057 | -45.4838 | 2025-06-09 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| cfae508f-b736-340c-8429-1a88d2dc9c8f | -14.2442 | -45.5002 | 2025-06-09 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7579e6a0-2755-3f04-8152-9b9aa35a9703 | -14.2447 | -45.4769 | 2025-06-09 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| c661d1d3-480e-3d34-91fa-ab4b6e75c588 | -14.2252 | -45.4804 | 2025-06-09 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 267.7 |
| b9f15093-8670-318c-adba-ef33e37185fb | -14.2252 | -45.4804 | 2025-06-09 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 291.9 |
| a69edeff-df02-3fc5-b3d1-330c22f6f984 | -14.2442 | -45.5002 | 2025-06-09 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 8f4b54e6-7fda-3190-8f06-812781d326f4 | -14.2057 | -45.4838 | 2025-06-09 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 4f464c4c-08b3-35a3-a9d6-f565cc37241f | -14.2247 | -45.5036 | 2025-06-09 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 650c4032-4073-34ad-a001-7353a2769251 | -14.2447 | -45.4769 | 2025-06-09 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 051394e1-f838-3383-b5d2-44810b23127a | -9.19282 | -38.81579 | 2025-06-09 12:23:00 | TERRA_M-T | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| c6ebe005-9621-32c8-ad63-d73fbc983076 | -7.27104 | -44.23185 | 2025-06-09 12:23:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ed6b2c47-f0b3-3080-8da9-83c8a865ce97 | -7.01873 | -44.57965 | 2025-06-09 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0c0b8dd7-b602-316a-9000-b78ebc8ac1bb | -6.97174 | -43.23448 | 2025-06-09 12:23:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7ef996fa-caac-3f24-ac3a-94e62866e1a0 | -8.98088 | -46.85608 | 2025-06-09 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2564dce-9f41-3e65-a850-dab1c54d7670 | -7.4465 | -45.79143 | 2025-06-09 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5fe6540c-a3cc-36aa-a47e-6dbe169088ac | -7.66214 | -49.12519 | 2025-06-09 12:23:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c02d11b6-cc3b-307b-a695-180d108452aa | -8.72175 | -50.2592 | 2025-06-09 12:23:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4ac16159-7dd7-3fba-9d6d-977ea5d6486b | -7.43759 | -45.79023 | 2025-06-09 12:23:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 7d3c9385-461e-3f32-89f4-621afe21e548 | -7.7988 | -46.48977 | 2025-06-09 12:23:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eb3f634d-1e02-397b-b7b6-1fdafc30c8ca | -6.65871 | -47.60271 | 2025-06-09 12:23:00 | TERRA_M-T | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| df37d75e-e0df-33b9-a18e-f296cc679819 | -3.37852 | -43.13063 | 2025-06-09 12:23:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a0b6520d-b732-3625-8966-e2123d70db90 | -8.10597 | -45.36182 | 2025-06-09 12:23:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 340dc213-edf5-3ad7-a338-72eedb920962 | -8.96707 | -47.9671 | 2025-06-09 12:23:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 64d737b7-a58f-3553-84dd-4ec632f71058 | -4.79103 | -45.33567 | 2025-06-09 12:23:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ccb654e0-5114-3259-bb3f-e3d853466600 | -7.0201 | -44.56992 | 2025-06-09 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ed524e84-0818-3ebd-8f83-5c01d5bc83be | -7.01735 | -44.58941 | 2025-06-09 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README9.md)
