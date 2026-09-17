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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b26310c-58e5-37d3-908b-6d5379ee4d5c | -9.59163 | -60.51427 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec1eab1c-7c6b-3a62-b250-131a371d131b | -6.10417 | -57.62459 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ff68c2f-ac8b-3782-b64b-5756312639f0 | -7.61154 | -67.24356 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae152985-2586-31fc-a2b2-b43a276619c5 | -8.76211 | -66.56313 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15206213-4132-3bd5-9766-3aa3d73cda58 | -4.37891 | -55.02941 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37255f0a-ee35-3b2c-96c4-4fcb25b08b4b | -6.02593 | -59.93095 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c189ca2-f8d1-3fc7-89f1-f800c467a7c6 | -6.33085 | -60.01947 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 334783d5-f017-3894-9ebb-a6fdf49bf2e9 | -9.0848 | -61.00793 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 269b8be2-b093-39d5-ab35-6236ce078b0b | -9.41016 | -62.70683 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d0b983c-17b5-33e9-aafc-ae2ae47211a0 | -6.67898 | -62.98572 | 2026-09-17 05:36:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1af12f39-bf60-37a7-8c25-c8ac45d914dd | -9.40575 | -62.71328 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70ebe49e-5baa-3a88-9aa3-2cf2877ba466 | -9.59241 | -60.51342 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8424dcde-5d07-3e86-ac64-6d1d17a6b46e | -8.48873 | -57.63971 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| edef0623-e2e6-32cc-8df4-43caf091dbe2 | -9.00873 | -57.12613 | 2026-09-17 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc794f01-89ca-34b5-87e4-2d3474b096d5 | -9.27822 | -60.60846 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c4e1b8-ac32-3219-b276-e8800bfc2f48 | -8.64777 | -66.59552 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4cfdf1f-8884-395c-832c-dc87827b7310 | -9.28112 | -60.61286 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04b90530-b217-3158-92a5-39d7532e3099 | -9.40685 | -62.7063 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6409470-a943-3829-8f8b-4f1178a654ab | -6.84625 | -62.89507 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d58dfd07-7ee1-3233-ba18-1401df33a094 | -3.7129 | -60.62933 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f07fa67f-93d6-3709-996f-2cf635b54465 | -4.54336 | -54.93214 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5de3cae3-2490-3f20-ad11-85eabca7474c | -7.79769 | -66.92052 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 107c5367-e5e7-394a-8ec2-b3cd193c5413 | -6.44244 | -58.14616 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 760735d7-141d-305c-a06e-0b3f1531d943 | -4.51826 | -54.94276 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f6b057d-eb76-3cda-ad92-f4d0c0fbfea6 | -9.10131 | -60.96828 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4b8e0b7-11c5-3aa5-b604-5eac56d52201 | -9.38484 | -60.30643 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 939a87cc-da72-3eed-9532-4df2fcf8ed6c | -5.15093 | -55.94681 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bab543a4-d739-334e-8404-60de5f60f5de | -6.83648 | -55.76663 | 2026-09-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f15b4fda-e09d-3d60-b5b2-00e49e3c302c | -6.35985 | -58.2823 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be9e6bba-e8b3-3e35-8601-47f07a433dca | -9.25097 | -60.78938 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aa66852-b83d-3dd3-9c0d-cc5e3cb9280e | -7.00865 | -62.98551 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bdfd3a1-d8db-31e3-a5da-96e9f76adcbb | -9.86152 | -57.96594 | 2026-09-17 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1682aeb-ce0f-3657-833a-cc29b449ae29 | -6.93783 | -63.02418 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 262a6670-63f6-3310-a197-3835d8262aa5 | -3.70621 | -60.6283 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b47ec95-5d73-3049-970d-c4e1737234ad | -9.86195 | -57.96519 | 2026-09-17 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6a0f435-1cf3-3855-90d6-690aea709e0a | -6.81198 | -59.1838 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 677370a0-3e9a-3ce7-90bb-0a6249708afd | -8.48061 | -57.63845 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 02acda71-e535-3b19-98a2-134d44c17429 | -6.10659 | -57.63519 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 918261ed-b25c-3b29-b435-c86405710ee4 | -7.30204 | -64.67584 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dbbafe1-8976-3e3f-8a7b-b204e49837af | -9.90937 | -57.06073 | 2026-09-17 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68b74266-7dc6-3b11-9ce3-c36a8918ce82 | -9.10304 | -60.98009 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dd75ac9-8824-3304-b621-3f281d4d3044 | -9.77306 | -60.46349 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b52e0833-18a3-3807-a458-78ebc48b3110 | -6.28349 | -59.92208 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f00839e3-8f1e-3fae-a9cb-dee26d0ea0f8 | -9.28343 | -60.62117 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6226281f-80eb-36ad-a2af-6f530a1d66c8 | -6.14309 | -59.94473 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecf994cc-2ba2-31c0-af4f-7eb46117b7f2 | -3.69896 | -60.63078 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b575bb87-4ca5-3fcf-bdaa-e17b49d2849b | -8.22316 | -55.46181 | 2026-09-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cac8c2de-90e6-30f6-8afc-782eba0857b5 | -6.11862 | -51.70506 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd47042c-985f-3f1e-8a19-cb57b335d0d1 | -3.69618 | -60.62673 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b13d323-1ad5-3197-bd52-7fe4da0289d6 | -6.93008 | -63.03008 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf54b37b-ea33-3608-8bd5-e0d215414ded | -7.06322 | -63.04715 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1411dc6e-5f04-38b9-b6cc-cfe8e0bb445d | -9.28285 | -60.62505 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e2f23eb-2573-3758-ad16-a6607394f561 | -6.71597 | -58.80221 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b86fb78-ed03-318a-b862-e4e0d4673e0a | -6.83121 | -58.98203 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff4bf703-211a-3ca4-8d34-c456da2c8bf0 | -9.38837 | -60.30696 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ca32419-e5df-3c1a-8022-bb446ddd4aa6 | -7.06598 | -63.05116 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e59f9208-fcbb-30b6-b6d9-b8b6ed66661d | -9.40961 | -62.71032 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6d13706-33b3-3b5d-8ff2-bac7259e2a1a | -8.4953 | -57.65145 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d8846ad-cc29-3225-a853-154dcdc453b2 | -5.926 | -51.6439 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f508ea37-9beb-334a-be41-00300badcdb1 | -7.80492 | -66.91465 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5778717b-61ca-3b19-8c7f-50a249670cf5 | -5.90596 | -59.93689 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfbbc896-bada-36c4-bb20-24689f0524e4 | -6.79169 | -62.98263 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f6741c9-72f7-3c54-b3a4-2f01423d8f5b | -6.43292 | -60.01418 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6c707a4-ad63-3262-832f-30e43d32202f | -9.59182 | -60.51737 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88e58655-abce-3772-90fa-9ec7600c934d | -9.10015 | -60.95271 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ca0b706-f7c7-3163-ae51-b4634e6b0da5 | -3.70621 | -60.60662 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 454c1496-96ec-30d0-91ed-b9bf11d1bee1 | -9.27652 | -62.69237 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17c68f4e-94c5-3ffa-addf-e962d46d9ca8 | -9.09216 | -60.95917 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 863f0ba7-6bb6-3e10-865b-a8886dc5e49f | -5.89844 | -59.93963 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1f52a1c-957a-3c12-ad37-77817bad9b13 | -8.63889 | -66.58025 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dbc2ea3-9e9b-3c42-b41d-877753433b70 | -9.09275 | -60.97848 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d878969-f391-31b0-9fff-8e2e8e78647a | -4.51019 | -54.9656 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e6c0a51-8dc0-3240-bddd-9e8c9d276233 | -4.37824 | -55.03395 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41418023-9957-32f4-8844-8d1cec2067c5 | -6.94003 | -63.03167 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5331bcc-02a1-347c-be24-df3d4ae52e49 | -8.11048 | -64.12319 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be8ce291-638f-3116-905a-d3a12e1e3bac | -8.59953 | -64.09845 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0a40527-108d-32ab-b899-14987792e64f | -9.41014 | -60.35419 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4748e54-b7ed-3ba6-bc07-891a0151b9a9 | -6.71098 | -58.81037 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b55663bc-dadb-39b3-bc86-183173c318a6 | -5.88814 | -52.08895 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 172aff4c-289f-391b-a416-2d2aa833e123 | -4.49359 | -55.50001 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24249eba-2763-3f7e-a7a9-a771643b8ff6 | -9.09677 | -60.99831 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdb81678-dd84-32c3-9554-18ee4ef7a3b7 | -8.3711 | -54.73565 | 2026-09-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe3ed043-5c6a-3faa-9f21-b8c3ef65f9d0 | -6.42714 | -60.00542 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efcea8eb-7fb9-390b-828f-c69ff5ea77eb | -8.91851 | -62.39933 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8dc52dd-225d-3650-b963-9a799783937d | -4.47803 | -55.08889 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1babfbd8-9685-3423-b61b-4e120deff244 | -4.39444 | -55.44143 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c03ab8b3-91bf-3a3f-99b6-1a7096e94257 | -6.71163 | -58.80602 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b43562a-64e6-3d20-b9ff-e2ae81714272 | -7.67039 | -67.0103 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58cac9ff-a5bf-3c84-ada3-860034288bb4 | -6.14635 | -57.68929 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 897d9697-dc90-357d-9cc9-0e7afaf09455 | -4.37438 | -55.0285 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 044d6feb-5398-37bf-ae5d-08dd67e055b5 | -6.35144 | -51.77873 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0cfcc61-9594-38de-a2e9-fe97efc5bbb3 | -7.60281 | -67.31989 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94969bde-79a6-3ef3-9a4f-9de6da02f607 | -9.38959 | -60.29894 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ac97841-9f1c-3676-ae34-62626bdf0425 | -7.77401 | -63.34081 | 2026-09-17 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24f56900-6645-3c8c-b67d-56eabdb3229b | -9.38545 | -60.30241 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74b1c0a6-308e-3e07-9685-c4fff4ac13f8 | -9.09165 | -61.00901 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e971f1f-50a2-3c3a-b083-b5f3d610ef36 | -8.65989 | -66.50159 | 2026-09-17 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0ecb38b-1b11-31a9-b6b4-6cd1791033f0 | -6.43351 | -60.01035 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87a9d3e6-ee33-3a65-973e-4222f9ad6db8 | -7.11749 | -55.12579 | 2026-09-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22e23a15-aa70-3be9-9a9a-6ec246e21956 | -9.00841 | -57.12502 | 2026-09-17 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README78.md)
