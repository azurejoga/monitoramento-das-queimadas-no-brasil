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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fced7315-1a66-36bc-815a-55b983aed543 | -16.97375 | -56.77577 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| e1b36562-e77b-3481-a511-4b1a2f794968 | -16.97074 | -56.76595 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 55879883-abfa-3641-9860-2c8c900c1476 | -16.97009 | -56.77304 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| d230fd80-9626-323e-a72a-61c189f6296c | -16.96942 | -56.78014 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| ad913171-178c-3b33-8a52-34bcd08410f1 | -16.96725 | -56.76794 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 6c497ca1-fba0-381b-975f-e10efae63704 | -16.96663 | -56.77504 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5cc69923-c296-3e28-9832-6dd064351dad | -16.75715 | -57.48729 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5365cd4c-c58f-334a-b518-6ae9e92fca9b | -16.75656 | -57.49356 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2635f0b0-d21a-30ec-837b-45ea2bd308f2 | -16.74974 | -57.49284 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b48763c5-b36d-3245-be22-756c5645d63c | -16.73788 | -57.47249 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6759f561-2aa3-394f-a5db-2ae2cbf7488d | -16.73165 | -57.46542 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fccce347-c947-3d18-a166-9a65dd05a1a0 | -17.16844 | -57.40152 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 02919a4b-86d9-3e3e-b77e-7953a6d11ffa | -17.16097 | -57.40732 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 04f00e65-0647-3fae-9ede-e5273e01608a | -17.15468 | -57.40008 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2d6b9ab9-57a1-348e-a455-5afd1ebfdf64 | -17.15409 | -57.40657 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 29da94f1-5360-39b6-88c3-343b792507a8 | -17.14722 | -57.4058 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6b0353b0-f277-3a09-9086-e717c8fad5d1 | -17.14338 | -57.36674 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d802bab0-c817-3db1-9636-253e6b2def1f | -17.14092 | -57.39865 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3d6581f8-5dd8-3e2a-9e63-d814d9a77c60 | -17.14034 | -57.40508 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6374bc7d-8801-3bbd-b8d6-327f0f8e7c8b | -17.14026 | -57.39914 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 247bd646-d7f0-3104-8f04-ae572ac2ed92 | -17.13976 | -57.41157 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8994ace7-fbf9-3213-8d88-f176acc4a690 | -17.13964 | -57.40556 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8e8e4a4e-b2c5-3e40-9ee8-0fac048ad3f1 | -17.13902 | -57.41204 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 556f9ecc-1e5e-3563-9b93-0f173ff25e6b | -17.13404 | -57.39793 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8e70ec8d-be09-3fa3-a9b9-bb338269c306 | -17.13338 | -57.39845 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a43127b0-f6c1-3d71-b062-b45bc51e7031 | -17.13288 | -57.41085 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| bcefca79-c702-3186-8f39-223a92807c2e | -17.1323 | -57.41734 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 90de66c1-0f75-33af-b5c5-9c91783da41a | -17.13214 | -57.41135 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 96fa408b-844c-361a-9684-7150fc311f31 | -17.13152 | -57.41782 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4ec9b63f-0dd0-32cc-8900-4277536ef20a | -17.12774 | -57.39071 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d25bce9f-3b6f-3427-9ec8-38beebde1548 | -17.12716 | -57.39724 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d2c4284e-6ce5-3a79-a586-943137175846 | -17.12712 | -57.39128 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| ed9a00e5-cd1a-3e7b-a84f-ca39496e9682 | -17.12658 | -57.4037 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c3861f71-bca1-3bed-8e0c-bd6662005eea | -17.1265 | -57.39778 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| dcc4b8e3-5cc0-37dd-9d21-72309aecdb93 | -17.12601 | -57.41014 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| ad0995ec-584f-3207-88ea-c4c9d14dc33c | -17.12589 | -57.40423 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5fcf0291-ff46-3f6f-8d8e-f6032e8bdb34 | -17.12543 | -57.41661 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| f0397c63-c35c-3274-a945-851402d54272 | -17.12527 | -57.41066 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 70369a31-6096-3d67-9aad-b7f4a9f4f54d | -17.12465 | -57.41712 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 0bc5bcdd-1d38-3aa7-96a8-ea9278298340 | -17.12143 | -57.3835 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c27a8502-f2c9-394c-b2f6-c9b343442ff5 | -17.12086 | -57.39001 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 9d8b4550-5f4b-38c3-9a39-566c11e9b5b8 | -17.12086 | -57.3841 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 2ce7a9b6-0d4e-3dba-8296-627090251aed | -17.12028 | -57.39653 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 0fde79f8-fb3a-3c88-96b7-8f637d7febfa | -17.12024 | -57.39059 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| b70b6b47-0e07-38a2-8a49-0874c9778d14 | -17.1197 | -57.40301 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 98736d01-0a3f-3e4d-919f-8d547647751a | -17.11962 | -57.3971 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 6fb73199-7dc8-3277-97f6-8d6b55160014 | -17.11913 | -57.40944 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 59dd2094-1a6a-3c8d-a3c8-38695b7106d5 | -17.11901 | -57.40357 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5fda974e-e440-36ad-a69b-58906f6a8e5e | -10.36725 | -69.25206 | 2024-10-05 05:55:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a40a70ec-4e1d-3f67-858e-c95fcbaf2f02 | -10.38342 | -69.2724 | 2024-10-05 05:55:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57fd67d5-9053-3de0-8cee-69121bcbfa4f | -10.70523 | -69.42146 | 2024-10-05 05:55:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a911a6f4-8d8c-372a-a307-32d33df4cebb | -17.11856 | -57.41589 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 922f28b0-292d-305c-a0b0-55820643b5e8 | -17.11839 | -57.40998 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 09b2d0ac-cec7-3edf-af33-87746525268a | -17.11778 | -57.41645 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| d83341b3-8ad7-3dfe-8892-dd28d7f2b4f1 | -17.11455 | -57.3828 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 038f63bd-d78f-3eb6-9494-fe384b30f309 | -17.11397 | -57.38929 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| d379d452-699d-3571-bdce-2b26345891e5 | -17.11397 | -57.38344 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bb903131-9930-3105-8939-d902f7ee3655 | -17.11336 | -57.38991 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 25107c1d-1497-3bdb-8973-56b77539aef5 | -16.92513 | -57.70165 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4287d74a-b0b4-3fac-bbe7-606b538fae72 | -16.91896 | -57.69477 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 89a1532a-9f3c-37a1-89f1-152241dea5c7 | -16.91221 | -57.69405 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 94b82af4-500d-3065-a1d2-73b904acc9f3 | -16.83573 | -57.46263 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f2e1f80d-a6d3-3485-9789-b16e09506cb2 | -16.82948 | -57.45553 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a50f247b-ff4d-38c8-abc4-29c8b0b09760 | -16.82889 | -57.4619 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4ee2fe98-6514-31cf-bf13-3e4929b50d74 | -16.82772 | -57.47461 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 79f62121-06c4-32db-8a4e-fd00238750df | -16.82264 | -57.45483 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1658240d-2b62-3922-9b64-63d45642c40e | -16.82226 | -57.45565 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8ae7ebe6-b5d1-3b5c-9e02-d6ab8d729b2f | -16.82206 | -57.46118 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5c397d3f-7001-343c-b7ef-998eeb70b18b | -16.82163 | -57.46199 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cc71eea9-5964-34f7-83e6-eee50966ba3e | -16.81602 | -57.37764 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6f0c5de8-a443-36a7-a472-b96e62d11786 | -16.81593 | -57.37661 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 28f74c5f-0f0c-3541-afce-b06089548bef | -16.81581 | -57.45409 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f5d63be3-c25c-3935-ab02-b5013663e631 | -16.81542 | -57.45494 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 619fb587-6aff-3f03-96b9-7f0dc9f6a761 | -16.80916 | -57.37694 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8f2b14f7-5dad-3481-9ce8-738fdcd7d256 | -16.80906 | -57.37589 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 913e082d-ec61-383b-abac-622ba72bbde3 | -16.80854 | -57.38336 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e2567518-2809-3c2d-9d9f-e71c40cb529b | -16.80848 | -57.38232 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7c64ed7a-f9c5-30d0-a246-705aaee41ac3 | -16.78676 | -57.47018 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dc698fb5-07d0-3c49-91d9-d57d1dea77a3 | -16.78625 | -57.47114 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aadc4512-d7f2-313b-99dc-aa0607b34563 | -16.78277 | -57.43771 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 138a14fe-4c3a-3544-982d-6554748e9321 | -16.78246 | -57.4387 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2b740288-656e-3a6b-8591-c03fe62b2404 | -16.77937 | -57.47577 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a8ce9ed2-d8fa-3299-b64f-61849f7232de | -16.77882 | -57.47675 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 137d7684-b1a4-3da7-88b7-6d6cb93083d3 | -16.77824 | -57.48842 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b968da85-b3ad-3787-b280-4623f87c2757 | -16.77822 | -57.48309 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 63cb0b0b-48b9-3fdc-b3a9-0b850e3f142e | -16.77768 | -57.49469 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e504b16c-a232-392c-a19a-e067fb724bef | -16.77761 | -57.4894 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 22d09d1b-3dbd-39f1-a80a-92a01b723475 | -16.77711 | -57.50101 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8ab7ecf0-baf5-3d0b-83e8-e465edc53409 | -16.77701 | -57.49567 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| b9893783-29db-31d1-899e-51fb75bb86ae | -16.77536 | -57.44334 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 728e6684-2878-3771-bf0c-f42892b4374e | -16.77502 | -57.44436 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6c4b7205-e685-3f57-991d-28c4448949d3 | -16.77254 | -57.47506 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fdffcdd0-7f99-3bbf-a1df-7e7fe2cae8dc | -16.772 | -57.47607 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f223fe80-c690-3b1c-a8e1-37830690bab8 | -16.77142 | -57.48769 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 917bf2c5-d511-30d6-934d-5222b4b80982 | -16.77139 | -57.48239 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 176bac6b-e76b-3a59-83fa-0e8370e14544 | -16.77079 | -57.48869 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7ea90533-8e46-3fa4-95f2-b8e885b0403a | -16.76909 | -57.43624 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9d4cfa7f-2281-3045-8771-87002e531dbf | -16.76879 | -57.43728 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8ac28bc7-d452-3d53-a183-6e37b3d7906b | -16.76852 | -57.44261 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5f0ce115-a8cc-3484-bbf4-0130c5bc7c38 | -16.76818 | -57.44365 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |


[Clique aqui para ver as próximas entradas](README152.md)
