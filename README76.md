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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 935d7074-5202-3b1c-9f8b-5978bb7ba4b5 | -5.10257 | -56.97705 | 2025-08-24 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 578a24c1-de26-3750-b92c-e61d46bb667e | -6.5686 | -59.86982 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e85af22-3b2a-39ff-8605-f5a1d8fa67e4 | -7.07191 | -60.05925 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4598280-4a15-311d-9488-bc224c03aba9 | -3.13726 | -58.03806 | 2025-08-24 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40609209-1708-3d96-b1c0-cd926a1538d9 | -4.93967 | -55.82132 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97157147-cb09-3952-a703-0c3df7cbfe28 | -5.42487 | -60.16705 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 40a71725-e8c9-304d-be2d-6b6dd6ae0e04 | -6.68824 | -58.85793 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7f05330e-31ca-33ec-b7d3-76c691ecbf9d | -2.93142 | -53.70138 | 2025-08-24 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d7876216-c4df-330a-804f-b8587ac89138 | -7.44508 | -57.62191 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e24470c3-0f43-3122-b44e-11b8259108a7 | -3.44186 | -49.04631 | 2025-08-24 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ecea8c7-349b-3118-89c2-fb363920593d | -6.55884 | -60.06065 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29d201db-f058-3077-8a0e-3de47b5d835e | -5.87342 | -57.75684 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecd1174e-9162-335c-997a-cc1558de0e46 | -6.57193 | -59.87034 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd5370fb-c5b3-3861-8cda-e851a517dee2 | -5.6151 | -60.23203 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acf12a0c-1a6d-3419-8cdf-524f0fe861eb | -6.60946 | -48.04962 | 2025-08-24 05:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bf70034-e7f9-3951-851d-290533b9ae4c | -5.74669 | -57.59089 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 184260fb-51fc-3aa4-933c-c77d19f4d9fc | -14.28651 | -60.37387 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93bac275-5945-31d7-9ee7-6c16a9bdd00a | -3.78569 | -47.57722 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 172d1d30-a535-3deb-beb1-b6a5e28211e9 | -14.84353 | -48.32404 | 2025-08-24 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09aa85a4-7921-31f2-a143-693271713251 | -4.30537 | -48.10065 | 2025-08-24 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 193b935a-2865-3e48-90f6-f8f23a56ad41 | -3.06155 | -49.50562 | 2025-08-24 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ab62ec2-e122-3a1d-b3d1-e3e04ce53fdf | -7.44144 | -60.6272 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26a775ce-a566-3e8b-a8e0-84905e430041 | -6.87494 | -59.82018 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3008ff4d-095b-3aaf-89c6-82c1c8844b6d | -7.54885 | -63.84304 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61895e6a-8340-37a7-abac-1e33944f1e9e | -7.02836 | -55.43463 | 2025-08-24 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a36720a4-f652-360e-981a-c7b92878923c | -5.87773 | -59.92237 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 856858bb-2498-3734-bb3c-57c5266c1293 | -7.54685 | -63.85532 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b5b5262-a4a7-37bb-abbe-8dccd2c43621 | -4.56236 | -55.96317 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eb20cd7-80dc-3f57-ab81-de314f95ec95 | -6.62865 | -58.53941 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d95521dd-b9ac-36c1-8ed0-b4d76d3ac37a | -2.62883 | -58.11017 | 2025-08-24 05:23:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0004b2bf-6f0e-3b97-8dbd-3fe43ed4ea77 | -3.59334 | -47.52269 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d463d8c3-a60a-30d0-9292-b1003fd3b1b8 | -5.80933 | -59.2243 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c05a6818-ebd0-32f0-87b4-23cb29f6b68b | -6.68767 | -58.86161 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d21e30fb-5843-3eac-b63a-b7275c46283d | -15.06461 | -48.5265 | 2025-08-24 05:23:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e97e9e4d-dd7b-3326-8156-cb8818b4aeb4 | -5.44874 | -60.18853 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4807fd6-0669-3c98-89d7-c718b6340e48 | -12.72948 | -48.12321 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b7bf161-b412-3f16-8bf6-7ddfd1117d49 | -5.45482 | -60.19302 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9674f396-e51a-3450-87e1-cf576ff45d33 | -2.8603 | -60.91679 | 2025-08-24 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 897e12cd-2801-31fe-95e6-ff0ccc48c51d | -7.55466 | -63.85242 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b58725a-d3e9-36c6-8103-a6b30d35147a | -6.30677 | -59.89305 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f2ba6f3-c88b-3bb8-840f-9bb8339b93d1 | -4.96693 | -55.82523 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 47e1f305-fabb-3ece-b211-b4ce387760bf | -6.90201 | -62.98491 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47464151-8ed4-3ff1-b0f2-c079e7e50c7c | -9.15291 | -59.49972 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1087fc61-ecb1-3471-a97a-42b998a8e03d | -9.15859 | -59.50815 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de55ba2e-a87e-3f54-8793-f0881e18610d | -9.18993 | -64.55481 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f8a3d90-1ca9-349c-8c35-8c90674ce8f4 | -9.1842 | -59.70371 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e34c9847-cace-360c-9ffd-12ba97b705bb | -9.17117 | -59.608 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c498ce0c-894c-30fc-95f7-42d0a2adad4f | -9.1966 | -59.62327 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8930179f-8a0d-3d85-87e1-887a2f28b748 | -9.5191 | -60.51777 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6f79267-a8ca-3721-800d-beb00dd15c1d | -9.15713 | -60.81647 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b05d273-7c2a-3580-b644-497b4c5682df | -9.17148 | -60.81158 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ec87a77-27e0-35d0-ac94-3b7ce21adfe2 | -8.13906 | -62.8605 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21c66e19-a782-3d2a-b393-7d368a3c3919 | -8.89059 | -62.42749 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc70c5a-1258-3578-b69c-64b99f831c30 | -11.54878 | -51.90618 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41240570-a3bc-3f8d-9931-d26a7922dcfc | -15.33669 | -56.23519 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 462bb220-32cb-3926-b3f7-95218350b970 | -9.27002 | -61.02739 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35edd46e-281e-3fa4-98b6-463ea3191bb3 | -16.39227 | -49.64768 | 2025-08-24 05:25:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3dcb6a3-fe62-3390-99a0-9ea8a190824b | -9.15283 | -59.45425 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e5b888b-289a-30b3-af1f-de1e2391bf73 | -9.00423 | -65.70567 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 709e5851-a4ce-3bde-91aa-955117c9b8a7 | -8.4406 | -63.86064 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03359381-4670-3401-b64d-a3aafe4d568e | -9.16154 | -60.81 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 860f0673-51df-35ca-b71a-1505ae4f12c8 | -8.63526 | -62.63858 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0ecd019-9904-3dad-a931-ae9bf00c68ed | -9.17102 | -59.47225 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d1f4dfc-3159-3822-8d15-410b3c09b1aa | -9.72006 | -65.71084 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb0aa6d9-b947-3d42-8551-06040e8b7b10 | -9.18136 | -59.65465 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b11a5f12-b7bb-38d9-b09d-567b489b6c43 | -9.51976 | -60.55761 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 554a3872-0150-3237-80fb-fd9bda55429b | -10.04913 | -59.35769 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddff0918-18aa-3e06-a1d1-ec0909fccaa3 | -9.07147 | -65.71468 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f1d4ae5-6aa3-371c-82ca-ad7224a9cf00 | -9.20182 | -60.79132 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0a2d5f4b-970f-3834-9781-cf952eab4a57 | -9.0227 | -65.69619 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 503424af-f87d-3d14-9c9e-a8db9d8396e8 | -9.16136 | -59.46697 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1eaf6c66-6882-3e5b-947b-665ea288b64d | -20.34618 | -51.69065 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3a3af824-18b0-3bf8-9fc5-59595f141fd8 | -8.5868 | -62.60825 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39ea781d-7061-3d61-96cf-e5a7617bc3b0 | -9.7239 | -65.71153 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3765839-65dc-31f5-b9c3-8153374f534d | -8.69738 | -62.87807 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a274a74-b06d-3e3a-906f-d0802157fae9 | -9.16308 | -59.4786 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e6de9754-131f-358d-9daa-eef7f98172b6 | -8.88007 | -62.43729 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 943b0414-8d84-355a-bcfd-bf8d7f192cb6 | -9.20394 | -59.43938 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20293451-8152-3cce-a78d-fe620d805631 | -11.42856 | -55.01077 | 2025-08-24 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ac780e9-b0df-3fcf-bdc6-972e838dd427 | -15.29338 | -56.15543 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 76104245-b0b4-372d-ab63-bf1d76e3bb4c | -10.10101 | -57.76912 | 2025-08-24 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e94fcd4-0d04-3d6c-98ef-7685dc9663ca | -8.89292 | -62.41315 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cdc5840-cbf5-3cc9-bf76-009bda7e3adc | -9.22797 | -60.92784 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0cf9ab1-5df3-37e7-a641-70d9b30717aa | -9.15347 | -59.49602 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 926aab5f-9b97-3208-b80a-5c397157881d | -9.14039 | -60.77119 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2878fb1e-9704-3d12-8bb2-19d987c3b38a | -9.00316 | -63.63371 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3ae27c3-4e65-32ce-b9fc-a9a1e768ec0a | -8.62499 | -62.62943 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40f0356f-9247-392c-85ea-b1cce59e0a7d | -9.22852 | -60.92436 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b322261-ab23-3ef3-9e0c-0ae525f9a6ce | -9.95731 | -60.18869 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eada9bb-57b0-3f13-9a4c-98a04a0ad74f | -9.24051 | -60.47751 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecc85528-7829-3705-999c-7471ffd5913e | -9.15589 | -59.59436 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 955d691a-7733-3087-a4e7-160730e47c4f | -9.51801 | -60.52482 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a794034-0d95-3509-89cb-5fdf6d0eee9c | -8.90182 | -62.42196 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dda77d51-a367-3a88-82b9-d2c40de4613c | -8.88695 | -62.39425 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fe166d2-e74b-3a73-9d8d-b0ca265a89a8 | -15.31543 | -56.15846 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 276d30de-5165-3420-a791-1bde56bdf165 | -8.13565 | -62.85995 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abcafa99-80bf-3089-9ebd-c9a952924ecc | -9.17913 | -59.6917 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99d0a014-cd52-3db9-a603-5a940c498965 | -9.33047 | -63.19248 | 2025-08-24 05:25:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8834f210-bbf6-39e9-8ff9-9543bf62c115 | -7.94934 | -63.05678 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 322b683b-c507-376c-9b15-5292571d1f3a | -9.20568 | -60.78834 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README77.md)
