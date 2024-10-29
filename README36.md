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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebb107fa-03a3-3646-98df-4f14df43ab06 | -2.3351 | -46.65533 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55029010-7308-31ef-842e-f0b05c8ab7c4 | -2.33397 | -46.66265 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b10e0fed-cf6f-35d4-b192-6e3fea416444 | -2.33397 | -46.64016 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e60a0c57-4c9d-30a8-b1a7-06ab84c8b558 | -2.3334 | -46.64383 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1342bb8c-00a7-34c2-a11e-476a86610085 | -2.33283 | -46.64749 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a0e082c-b7d9-37b3-95cb-6e9f528dc7e0 | -2.33227 | -46.65115 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f788643d-85ba-372f-b406-7a40e7854aef | -2.3317 | -46.6548 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08eb11e2-d5c9-3596-8ae8-3374f8c57aa8 | -2.3317 | -46.60971 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2bf9ca0-8ae2-343a-90cb-f3c271164bf7 | -2.33056 | -46.63964 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88fdf173-5450-3743-afe5-efe331db9309 | -2.32773 | -46.63544 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47205f86-1511-31d1-a624-79fec8caa663 | -2.32716 | -46.63911 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61167e5f-eef7-3d79-b22a-971270ccf794 | -2.95654 | -47.36164 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dea16bec-a4b4-3b75-901b-64648fa0424d | -2.85982 | -46.64422 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 576beecb-d5e9-3ebc-9c84-0b01d7b081d9 | -2.85926 | -46.64793 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c5de4f6-9eb6-3735-928f-46c534cd50b7 | -2.85869 | -46.65163 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef5282ad-8f1e-3e8b-b4bc-c44e61328ca9 | -2.85527 | -46.65111 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59bfc276-74cb-324b-9afb-2ff36a997059 | -2.8242 | -46.60091 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68d7ee8f-3a51-370c-bca5-df6c81abba27 | -2.73023 | -46.68851 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a1d8caa9-518c-3a65-b88f-01075c9a53b2 | -2.72964 | -46.68885 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76891f16-b1ee-307a-812c-c80b7f3852a4 | -2.72282 | -46.68781 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80b2409b-3b95-3595-84b6-4625e87dca7d | -2.72051 | -46.70251 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9b4de437-682f-31ba-84d0-d5c239440167 | -2.71941 | -46.68728 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af6f62ea-38da-350e-a1e0-2815020a66d9 | -2.71883 | -46.69096 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 983d5805-30dd-3886-be17-a982b9b5890f | -2.71826 | -46.69463 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 348fde0f-57d1-37c7-9687-0a2310aa9c93 | -2.71768 | -46.69831 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 71ddf742-4fbe-35c3-ba11-021195b230bd | -2.71711 | -46.70198 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d6519594-a209-36ff-9e2f-1a04cd5100ea | -2.71653 | -46.70565 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2de60a8a-fe1e-37b0-9dec-18399356e517 | -2.716 | -46.68676 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78339cf6-3d43-38b7-a588-ad7913c5b215 | -2.71543 | -46.69044 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63fc9904-b506-314e-a167-1f8e7744dd54 | -2.71485 | -46.69411 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d7906c8-91cc-34b4-8fa3-30a3beddf767 | -2.71427 | -46.69779 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a6c14c9c-97ac-3e75-8815-808f2164000c | -2.7137 | -46.70146 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 06babe58-3ea9-38bf-aa0d-a409755e0c99 | -2.71312 | -46.70513 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3efec86-f88f-3ec8-9de5-0ca24568de09 | -2.6938 | -46.71719 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac95f456-6bee-3a05-b095-c3d59891c249 | -2.68188 | -46.72662 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 111a8a83-c0a1-3f6f-bcb5-be8ebc727b40 | -2.6813 | -46.7303 | 2024-10-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 083faefb-2657-34fc-9652-fcf66bc390a3 | -2.6611 | -47.35962 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f79d775-991a-34bb-9587-63af5c8354a7 | -2.54988 | -47.35333 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35542dd6-2e3b-3602-aaf8-0f5fa5976146 | -2.54823 | -47.3639 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f433867-e098-3690-8734-2bdf8de27c78 | -2.54769 | -47.36741 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 126c4993-ce6a-3d4a-ad10-c6033aed6180 | -2.54654 | -47.35281 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8725355-e6fe-39c2-9d8c-74d76556baca | -2.54489 | -47.36338 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34a43fc8-a411-38f0-8cce-1d1d263632b2 | -2.54435 | -47.3669 | 2024-10-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a8cc150-15c1-304b-b94e-36b2d4d47080 | -3.19554 | -46.17531 | 2024-10-29 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cbc26c8-1e83-3bd5-b8a6-c22dfcc42e7e | -3.18208 | -46.19305 | 2024-10-29 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e80219-2b2d-3433-a5be-510309ed1c9e | -3.18038 | -46.18089 | 2024-10-29 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1f57885-bc28-35eb-9eb7-9c4b140e979f | -3.17859 | -46.19252 | 2024-10-29 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 141a3201-fb44-3bbf-aa8d-5bc8c460648a | -2.78356 | -45.98001 | 2024-10-29 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 929d6fbb-5f3d-3372-9587-e89b08a4ae41 | -2.78066 | -45.97557 | 2024-10-29 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee45691d-cd1d-3317-8901-171fa262f3a2 | -2.76773 | -45.98962 | 2024-10-29 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2806722-01a5-307b-a4c8-6f5538fce25e | -2.76422 | -45.98908 | 2024-10-29 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fac7691-2b64-32fe-b7f6-d78f4929bb0f | -2.7367 | -46.00486 | 2024-10-29 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17674edd-27eb-3926-a2fa-381aea89407a | -2.73611 | -46.00877 | 2024-10-29 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a5683a3-c270-32d3-a8d1-a3c8a1a4b868 | -2.7332 | -46.00431 | 2024-10-29 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 959d9384-54ec-35de-b569-dffd417f97a8 | -2.72664 | -45.99238 | 2024-10-29 04:38:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20c7dd05-e977-3a28-92e3-0652b913faa9 | -2.64643 | -46.04769 | 2024-10-29 04:38:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0f7afc7-7374-3e16-bae5-cb3c1f9d52ba | -2.61888 | -46.13418 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e907d22-aa94-3c31-bf4e-0aa219bda841 | -2.61829 | -46.13803 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99ca414a-1c07-33b8-86c0-da8ec2c5e803 | -2.6154 | -46.13365 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c0563a8-cc96-347a-9443-923316fd75a7 | -2.60668 | -46.14413 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02a36001-b94c-3408-902e-ce5393a03255 | -2.60379 | -46.13974 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 260b16a7-ead7-3ada-9730-9d58aed28f0d | -2.6032 | -46.1436 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0ca5f54-4b54-3f1a-8033-0396f22b5a17 | -2.59972 | -46.14306 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49fcc91c-98d3-3bac-81bf-6e675ce6f23e | -2.59914 | -46.14691 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2527f418-584b-3bf5-b4f6-18a4669e1e6a | -2.59781 | -46.14306 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 551f0ef8-53be-37a9-9b89-0441ffc12d47 | -2.59625 | -46.14253 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7af1cfe2-2cb5-3f9f-8469-f11b42b24685 | -2.59087 | -46.14198 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63d0d958-4712-318d-9f9e-1e32ec6ab81b | -2.58331 | -46.14474 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb4fd4dd-e6cf-328c-8470-76960a8caa86 | -2.57529 | -46.12776 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d81a8f7-80f7-3c46-9218-23a089f4a424 | -2.57182 | -46.12722 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e13acb3-5cec-3f3d-baa3-ee96a713244f | -2.56317 | -46.11415 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1d87093-42e2-3210-9f16-049b15acdac3 | -2.56029 | -46.10975 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5bdd43a-66b5-3f90-827d-3ebc401293b4 | -2.55969 | -46.1136 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9b24332-8da6-3eb1-a29d-c0b5937dc751 | -2.55422 | -46.17165 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36a77b3e-ad0e-3b53-a81d-72586e3dbe65 | -2.54857 | -46.13934 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ac8709e-42ad-3401-ba16-9d7456191f17 | -2.49157 | -46.27878 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f3b8ef8-5ac9-3143-a48d-dfd6c455c6f6 | -2.44667 | -46.14022 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f5f360c-67a1-3603-94c8-acf2bcf74d9a | -2.36218 | -46.16698 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87fb2e1f-8c77-3ef2-b142-40747c8f0067 | -2.35872 | -46.16646 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a1f536c-8bf5-35a4-87dd-42ff43fc44d1 | -2.31861 | -46.24184 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06660b35-5e6b-35c0-a6a3-9ee3842812e7 | -2.31663 | -46.14043 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e358101-ed4d-3ab2-92a5-638146c5c267 | -2.26926 | -46.11059 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd4ef324-bcf7-330a-bae3-45d0cdb33fd6 | -2.26271 | -46.30655 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86205cc8-56bd-3410-86c2-d87944a95186 | -2.25005 | -46.25524 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cdf77a7-84df-3e4d-a345-c65d08756412 | -2.24601 | -46.25846 | 2024-10-29 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c281d14-44ec-382b-9b8b-bc02add82a06 | -2.32037 | -46.68302 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eccde56b-85fd-3ad2-9838-1db59267506c | -2.31754 | -46.67883 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c908e27d-fceb-3dc5-a0a4-e7bc9a7a6b89 | -2.317 | -46.72738 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72193d4d-161b-373e-9b2d-9ef00be5f369 | -2.31698 | -46.6825 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d22b3b8a-a4c8-3f7a-94e4-00d0e92526c3 | -2.31641 | -46.68616 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b52e734c-7eb7-359c-a0c7-a04af5ac684c | -2.31414 | -46.67831 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 151277cc-44a9-392a-a87f-0e887d60ebdb | -2.31358 | -46.68197 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72c216e7-086c-3296-a738-7497ce58fc1d | -2.31301 | -46.68563 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ee5366e-8a68-3636-8d59-b537a067d747 | -2.31187 | -46.67048 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f19f4d77-0972-39c7-b1c5-d617269c5fe1 | -2.31131 | -46.67414 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60b77f6a-edf6-3d2a-9f25-81b9b06914f5 | -2.31074 | -46.67779 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15bbb0ca-9de1-35a0-8e81-f4a0b908a610 | -2.31018 | -46.68145 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38e4a547-deb5-3a44-a60d-2be863da0e20 | -2.30847 | -46.66996 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ddd02ed-060b-3139-86b4-454e82adfbdf | -2.30791 | -46.67361 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 659dd67c-dee8-3fe4-924e-2d511e9b0ad2 | -2.30734 | -46.67727 | 2024-10-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README37.md)
