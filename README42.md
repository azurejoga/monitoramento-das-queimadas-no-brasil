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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82234592-f45a-3320-b56a-4948401e7314 | -7.68496 | -63.32677 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 101663e8-e09c-37f8-9288-40a2fcea3ed5 | -6.73951 | -59.66146 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 889f1527-0b8c-32f9-8a66-d43b9c2f1a51 | -2.74665 | -60.2367 | 2026-08-24 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1c42e08-d518-3ce0-82ec-0402e59de53e | -6.9744 | -59.0792 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d28c676-b1cd-3184-8689-6130f63d6aeb | -5.81127 | -55.70738 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9535aa56-625e-3d22-8887-2f9741294cd4 | -4.93436 | -55.77506 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3703d7b3-be68-39a8-837d-af1052f44bf3 | -6.95561 | -59.08067 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88dbf3fb-0049-367d-a4c0-0c481eefc6e1 | -9.05451 | -50.76879 | 2026-08-24 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f48517cc-5ab2-3843-a23e-e893461cc549 | -6.80332 | -58.66425 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fd80462-09ad-31e0-8865-6c2a25bfefc5 | -6.12318 | -57.84178 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 403b8725-ec8c-37b2-8759-c6647ad0aa08 | -6.80027 | -59.59611 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9cf8b78-0fdb-3e2f-a111-b663c1b956d3 | -6.22053 | -55.92486 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9a0570a-fc4b-3935-8d32-cb93bf6231b5 | -6.82315 | -58.65831 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 254b183b-c563-3746-9eb7-cbf8135e022d | -6.79793 | -59.58755 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f43a0bc5-bfae-3cde-bcc7-a59067d4542d | -5.87497 | -57.57032 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d61270f3-e12b-3e3d-a5c2-e248e74ed4ea | -5.57472 | -55.81814 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e964e2ef-d9aa-3061-be48-8d1baeebc00b | -6.94503 | -59.07221 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59cf1ecf-b9b1-3365-83af-bf55e59b1e44 | -7.67165 | -63.32467 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3af68306-9838-3843-9283-c98683f43c38 | -6.79674 | -59.59557 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3438a4c-788d-37ce-be28-79128d853211 | -7.78288 | -56.28706 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d932171-a75c-3d12-a448-2419e264fe0c | -6.89929 | -55.69795 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63793a40-c3a2-3558-a01f-1f12d99fc721 | -6.82371 | -59.41452 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3cbda62-df0e-3475-b567-1da3ffc3e0cd | -5.77638 | -57.55912 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82de9669-0be3-3ba0-a10c-35afb79cdca5 | -7.67498 | -63.3252 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c208fa79-2cd9-3183-b9df-e597cf0ef7e1 | -7.62412 | -61.60165 | 2026-08-24 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d0a294-f5fa-3996-9763-3085042b96a0 | -5.9045 | -56.93011 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 495c2bd9-b551-38ea-90df-6cad23143b7b | -5.77494 | -57.56908 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d8f4ec5-a6be-3280-8b80-24298fb519b8 | -6.74484 | -59.65013 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c7b7016-8ff4-356c-a2f4-c554dc0ac110 | -7.68163 | -63.32625 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 17e66c80-f142-3666-8130-a2de9c5fc10c | -7.685 | -63.3255 | 2026-08-24 05:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d29df5b4-d5f0-33e6-ab5b-211cc5cf4b60 | -16.0919 | -52.3335 | 2026-08-24 05:30:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 50.3 |
| f78be7d0-a392-35c3-a6ef-d4d9b80e1c54 | -12.11724 | -50.55279 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d24d2306-a928-329b-9fd2-adb2c11e30ce | -14.40495 | -51.78022 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8cd0efb9-f623-3048-bb24-b9b7abcfbbad | -13.17472 | -51.39103 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b04bbbf4-d849-3a7e-8904-75ff2aacc60c | -16.09436 | -52.34597 | 2026-08-24 05:31:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e46d8e0d-4c5c-3284-834f-906bb6977a57 | -12.12988 | -50.54044 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 697d780d-fab5-32bf-b600-934d8c1ee0aa | -12.10014 | -50.62303 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 79f00a24-ec89-397b-a6b0-b59bad53b988 | -14.361 | -51.76383 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f52f500c-13cc-3627-855b-9ee51d8ea017 | -16.38124 | -51.82869 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 81cd1573-bee3-3254-8e87-f6037375f7a0 | -12.13334 | -50.52997 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 378e9cd1-f79e-3da7-a979-eafc83bb19c0 | -12.13269 | -50.53611 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea7f6cea-187b-3928-83d8-8e417cb9ea19 | -12.10602 | -50.5946 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5d22194a-f273-357d-9ab8-3a1e7b714137 | -12.11084 | -50.61367 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 9af822d2-b75f-3eb5-8ac7-e00fa5f7a2d4 | -15.26781 | -52.84599 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd4b27a4-9945-39f1-a016-8a936819d1c3 | -14.25504 | -52.13697 | 2026-08-24 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a59017dd-6a60-301d-8091-91e677835988 | -12.10216 | -50.60489 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| d8758fe9-ab64-38c3-a020-63bbb6c1e6c3 | -9.09732 | -60.91081 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9deefdf2-11e6-308b-af3b-8d0b030b28cf | -10.79717 | -50.94638 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a7251a7-894b-3064-bef7-25c8662c8ec6 | -14.41213 | -51.78567 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2c95b7ec-39a3-32b6-ac1e-274f1579deb4 | -9.97947 | -57.88554 | 2026-08-24 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2be4333-f49b-36ec-94b5-dd4e013cb5e1 | -8.82791 | -62.36736 | 2026-08-24 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 948c9cdd-aa86-3aea-845e-838222528bc7 | -12.11296 | -50.56935 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36eb1704-7a2b-3c46-a8c2-18e7fa337ac1 | -12.11501 | -50.55101 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c00b0266-235d-389e-8ec0-f40c79391d6a | -11.918 | -55.90609 | 2026-08-24 05:31:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75f4bec3-0e3f-3c7c-9de8-2afa32e79d04 | -12.12107 | -50.55796 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b65afdb5-6c55-3f7c-8100-3c815c21b987 | -12.09611 | -50.59799 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 3c1ce312-9a14-3880-b7a1-e2c99dafe13e | -11.65299 | -50.5498 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dde36ca-a57b-38b0-bba4-155191701a8a | -9.95812 | -57.86021 | 2026-08-24 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a0ab3be-1660-3978-b692-c57692393e8d | -13.18065 | -51.39744 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c829950d-4dea-3649-83c7-4418b979b195 | -15.27002 | -52.81939 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4a22507-cb84-3033-9d5d-cc061a739fbf | -15.2653 | -52.80984 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc0c3925-e006-3569-bfce-606611d3dffb | -10.81081 | -50.94258 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef4bd220-6eb9-36b4-9643-b0493d4e3495 | -10.80301 | -50.95272 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c04d0d-b73b-303c-aa18-88a0a7115793 | -11.15624 | -54.00989 | 2026-08-24 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2ddd2d6-dd7f-368e-a17f-699d696ff4b2 | -9.50942 | -60.49873 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd5a7639-1b56-33c9-ad04-f90d9ce59f55 | -12.12464 | -50.54751 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fed2bda-91ba-3d22-9508-00a9e5c780a2 | -14.41857 | -51.78645 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 83910047-5fc8-3291-9a15-05b6dd07e73a | -8.82345 | -62.35237 | 2026-08-24 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ec9ca51-a2c0-3d2c-b1dc-26415fcfd5c3 | -8.93433 | -62.14051 | 2026-08-24 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1021f65f-9768-36b1-af87-80881fd54d99 | -16.38835 | -51.82371 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ddef1278-18f5-3bc1-ab40-a7e9e795fa38 | -14.32145 | -51.7594 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bfa3272e-8329-39b4-8173-dd0dc59582c6 | -16.41283 | -51.83347 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53b61722-2cf5-31b5-8e0f-928d3273c6c5 | -9.21207 | -60.89367 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c0abf24-d038-3e10-8936-a67441af3016 | -12.11853 | -50.5405 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26d89eb3-f9cf-3cc9-bb49-874fc1069751 | -14.39978 | -51.77863 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a595a62-8134-3f2f-9aaa-cc64e001de96 | -16.08858 | -52.3395 | 2026-08-24 05:31:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 21553e1a-e96c-3587-a85b-f58ba3bcdf0f | -14.34222 | -51.75597 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41f28a39-6234-3688-8402-c4e422c44874 | -11.68669 | -54.55497 | 2026-08-24 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e432edc3-79ee-3b9c-a5d8-8c5715d1e0e8 | -12.10538 | -50.60067 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| dce4a170-fa7f-322f-8c4e-1cdef892db6e | -15.33343 | -53.95675 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c053cf0c-8aff-3d1b-af10-dc2a1bc0fbb3 | -11.65366 | -50.54379 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a49787d-2c9a-3daa-9235-a7ec1f43d161 | -16.40694 | -51.82524 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28e03d2b-41ac-33f4-ac29-9751afd068d4 | -8.68266 | -62.84323 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26ded5f5-ca5b-3080-a4a7-6ab18136e081 | -14.39851 | -51.77946 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd72454b-f438-3289-8052-1115359dae85 | -15.51458 | -53.9788 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb72a2f7-2c68-3b44-9ea2-a433e70677fe | -12.0651 | -50.56941 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91e98ed2-5723-3c7c-b1cf-6acde3632b40 | -15.26815 | -52.83662 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea7e92b7-f8fa-3b7b-962a-9c82be02631d | -15.26521 | -52.86374 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa3ec054-57d5-3eaa-b247-b966ed1d26f4 | -12.11364 | -50.56322 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de78bcee-d67c-3b77-a16c-541aa58467d7 | -14.30048 | -53.21887 | 2026-08-24 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddaaa1dd-0abd-3789-95af-4d189c53b208 | -11.91323 | -55.90545 | 2026-08-24 05:31:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f1b684c9-5951-3073-90f3-de415569a73f | -15.35459 | -52.78486 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d2aebf4-4d8f-3ca3-a30b-5c6eae4c0f2a | -12.10957 | -50.59969 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f5859049-5cb3-3282-8e5c-b0f6b4f2dac4 | -9.18899 | -66.99383 | 2026-08-24 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4f52df4-b372-34f5-bd93-826c291b8e75 | -9.39206 | -60.58125 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c30330c-7ee0-3c56-bedf-c07a897396c1 | -11.20275 | -55.04922 | 2026-08-24 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0e8c4f0-6e58-3ca6-a254-f164ad08c9d5 | -12.1182 | -50.6085 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 23d17ec7-2387-3ed4-8e96-6a10c51a04eb | -16.09487 | -52.34079 | 2026-08-24 05:31:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2c8159d2-1c98-3df4-b6db-c8c2817c9c28 | -8.68212 | -62.84671 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7973453a-2b54-35e9-b76a-295ad75bdadb | -15.40746 | -55.78222 | 2026-08-24 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README43.md)
