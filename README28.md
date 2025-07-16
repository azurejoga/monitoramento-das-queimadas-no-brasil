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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99357925-4df2-3b4b-b0d9-3da3ebc78c1c | -22.37046 | -46.83368 | 2025-07-16 12:14:00 | TERRA_M-T | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cf0dbb76-ce81-38b5-a0f3-04fe4d79f5d2 | -20.421 | -46.59657 | 2025-07-16 12:14:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc490589-518f-3b6f-9703-52ac144c306e | -19.54131 | -45.05394 | 2025-07-16 12:14:00 | TERRA_M-T | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e4f92768-b31e-38e5-a9e3-e413d1247d50 | -20.35796 | -46.59614 | 2025-07-16 12:14:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| edd9da09-c9be-3ec1-a363-6f80d9e079c8 | -12.4121 | -45.3628 | 2025-07-16 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 056dd468-4cde-3be6-8f46-7516cc671f61 | -12.4117 | -45.3859 | 2025-07-16 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 954585bd-bd1d-3355-b6c2-9a2b4a40b45b | -11.9531 | -46.3672 | 2025-07-16 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 596d6dbf-66ff-3476-8ddb-31c278fa8994 | -12.4797 | -46.9243 | 2025-07-16 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| f34eb7c7-c52c-3139-86b6-12fab0472f65 | -12.4117 | -45.3859 | 2025-07-16 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| bcddf03a-df02-368a-9546-034f9d5f6661 | -12.4797 | -46.9243 | 2025-07-16 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 50c0c013-4146-3654-b801-dbb2f9d905f4 | -12.4121 | -45.3628 | 2025-07-16 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 5bce29bd-963e-3cd9-aff7-cbd16329b38d | -11.9531 | -46.3672 | 2025-07-16 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| aeb2b633-4c8c-315b-b9d0-c256b85e2f5b | -12.4797 | -46.9243 | 2025-07-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 8bb49bab-2090-3bc8-91fb-8b151e81aec9 | -12.4121 | -45.3628 | 2025-07-16 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| d5fdb919-471a-3e3c-a7e0-18e394e12698 | -12.4117 | -45.3859 | 2025-07-16 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ee64ca00-e0e6-319f-83be-1d46a4372c69 | -12.4121 | -45.3628 | 2025-07-16 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 7c35605f-5a09-354f-9466-33e981917596 | -12.4801 | -46.9017 | 2025-07-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 70bcfa12-938e-3502-9e23-ab56d7611d8d | -8.7611 | -46.5985 | 2025-07-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3087382c-9c29-3195-9671-4a6c19225bb3 | -12.4797 | -46.9243 | 2025-07-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e9fa7723-effc-36f8-aa81-7797635d53fe | -12.4121 | -45.3628 | 2025-07-16 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| f7dd94eb-5db1-3303-9ccf-3106d88fafa6 | -12.4797 | -46.9243 | 2025-07-16 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 9b60902e-cbaa-3356-af3c-e625abb868c6 | -6.6488 | -45.7388 | 2025-07-16 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| fb719345-b4df-3033-85c3-ff265102716f | -12.4121 | -45.3628 | 2025-07-16 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 151021c9-cab3-3532-b213-8b10caa308a4 | -12.4797 | -46.9243 | 2025-07-16 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 2dc80a75-fcb3-3e0f-ac8b-fbc264e3d60d | -6.668 | -45.6922 | 2025-07-16 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c9d3b71d-90af-3238-84dc-97c694af17e7 | -7.5985 | -46.3304 | 2025-07-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 3e337686-1dbd-33cd-bfdb-88faeda3cda0 | -12.4801 | -46.9017 | 2025-07-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d16b20c2-9d24-3139-9cc8-337b9a2fbb27 | -8.7611 | -46.5985 | 2025-07-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c1f78b20-d493-33b9-a2d4-4955adf65a9f | -6.668 | -45.6922 | 2025-07-16 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 59f96ad0-ef53-3570-9b68-2161cce093d6 | -7.5798 | -46.3321 | 2025-07-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 0ba4dd54-2fc2-37cd-9fbc-3c3b021a6011 | -10.3211 | -49.9138 | 2025-07-16 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 5e50bcc4-e0b6-387a-a637-3b0b67f70b24 | -6.7194 | -44.3231 | 2025-07-16 13:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 23c3f66a-ecc3-3d8d-8bd1-89300dae0be6 | -12.4117 | -45.3859 | 2025-07-16 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| cd1b4168-7490-3fd4-b353-05b0215047c4 | -12.4121 | -45.3628 | 2025-07-16 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.4 |
| a374948d-ec3c-3c20-9639-ff27d56a9798 | -12.4797 | -46.9243 | 2025-07-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 976a387e-82c2-3d9a-83bf-873a7ccab712 | -12.4117 | -45.3859 | 2025-07-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e72b78ec-98ac-3a88-a70f-12c5cade8d50 | -6.6678 | -45.7147 | 2025-07-16 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5de634b5-cc16-3503-bc12-f6c2b90812bf | -10.3211 | -49.9138 | 2025-07-16 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f8236ad4-d846-3629-8075-53c4e6c917a8 | -12.4801 | -46.9017 | 2025-07-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f18984c3-8572-3001-904e-63b67237691d | -8.7611 | -46.5985 | 2025-07-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e0bf4a3b-df0e-33ea-b9b5-003fb470295b | -12.4121 | -45.3628 | 2025-07-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 9560577d-a3d4-3ae4-9007-a629b31b2d17 | -6.668 | -45.6922 | 2025-07-16 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 9550f67f-9443-309e-882e-ab0ef6e38566 | -12.4797 | -46.9243 | 2025-07-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f6521b28-5b55-3797-8d26-4e031b315a90 | -7.5985 | -46.3304 | 2025-07-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 85d7da41-3674-35ed-84fc-476092e000d4 | -6.7194 | -44.3231 | 2025-07-16 13:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 9d7a80b5-2903-3068-a69f-d9e582ca586a | -12.4989 | -46.9215 | 2025-07-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 75708df4-2db2-3248-9a86-b430725b4b7e | -13.1613 | -50.764 | 2025-07-16 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 6e2ff2f0-84af-39c2-a8a2-cee1d91ad211 | -7.5985 | -46.3304 | 2025-07-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d1f05383-28da-3e53-8c0c-d6300ed18d58 | -6.7194 | -44.3231 | 2025-07-16 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 59feff14-4879-353f-90d4-abfa224fa236 | -12.4117 | -45.3859 | 2025-07-16 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ecbb207e-5a3a-30dc-96b6-dfb42d972ec1 | -12.4797 | -46.9243 | 2025-07-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| b8da5440-d26c-369e-aa73-299149348860 | -12.4121 | -45.3628 | 2025-07-16 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 1e8f26f6-a9e5-3429-a44b-bd6362024491 | -6.7192 | -44.3461 | 2025-07-16 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 889c49b3-1855-33d4-88ad-2a6a2926caf4 | -10.3211 | -49.9138 | 2025-07-16 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 40327148-6183-3c46-984f-dcc97df64963 | -12.4801 | -46.9017 | 2025-07-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 588585ec-6efa-3d76-b010-6c7ba3f90e58 | -6.668 | -45.6922 | 2025-07-16 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| b2cff14d-b118-3572-84de-5a53a6eed071 | -6.6678 | -45.7147 | 2025-07-16 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| cae1a425-66c9-310f-ad5e-d1e364a128d5 | -13.1806 | -50.7615 | 2025-07-16 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d29c6ef1-4536-34fd-a42a-5a0bdc29967d | -8.7611 | -46.5985 | 2025-07-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 08a5cb87-7df3-3462-a15a-27f0ba72b459 | -6.668 | -45.6922 | 2025-07-16 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ba186ebd-346e-3f11-a2b2-90668fcdbc4c | -13.1613 | -50.764 | 2025-07-16 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 3959819c-3ac8-3c12-9450-a01d491ef5fc | -6.7192 | -44.3461 | 2025-07-16 13:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 236d65cd-45ec-334b-b9f2-9b3b535cf8af | -12.4117 | -45.3859 | 2025-07-16 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3c51ef05-d81a-3217-800d-bae9d37d7aee | -6.6678 | -45.7147 | 2025-07-16 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 70409cf2-ba21-34c1-abd9-f52a2880d5cd | -8.7608 | -46.6208 | 2025-07-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 56f78a26-b74a-3217-8858-fec213be7d36 | -6.7194 | -44.3231 | 2025-07-16 13:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 58894b93-98b2-3a06-bda4-72e0a8849081 | -12.4989 | -46.9215 | 2025-07-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b31307f2-0b7a-302a-9594-6132aab4214f | -10.3211 | -49.9138 | 2025-07-16 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ebbed237-4e9b-3386-80c5-ea95834f1f50 | -13.1421 | -50.7664 | 2025-07-16 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 3e2486df-1e3e-39b9-aa62-9a1324644179 | -12.4801 | -46.9017 | 2025-07-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c176c1be-9e50-31b2-956b-fc6b5f2db3ce | -10.6015 | -46.2314 | 2025-07-16 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 9fbaacd0-9caf-3a5a-b3b2-74321ecda2e0 | -10.5824 | -46.2338 | 2025-07-16 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 9c2046a0-0a74-3c81-ad30-dc99988f03d3 | -12.4797 | -46.9243 | 2025-07-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 3fb13bd1-0aaf-3eaa-b763-60e5dcb0d1da | -12.4121 | -45.3628 | 2025-07-16 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 12fa1782-ed5f-352b-ac11-30dc5a7611f4 | -10.5824 | -46.2338 | 2025-07-16 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 7f7e3822-98d5-3425-8860-e317aa3f5c00 | -12.4082 | -50.0195 | 2025-07-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 98412636-1b6c-3832-8868-04790c775fcb | -12.427 | -50.0387 | 2025-07-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 731.6 |
| 1639e198-afec-3b0a-b5da-9c1a5471db74 | -11.4789 | -47.3082 | 2025-07-16 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8241ded1-e227-3485-a332-d6d7a4f0baa4 | -6.6678 | -45.7147 | 2025-07-16 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 37fd5222-3eda-34b6-9189-78569c38e5b8 | -12.4121 | -45.3628 | 2025-07-16 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 3c2d9a3d-56c3-3e7b-bf22-58c58bea6b29 | -6.7194 | -44.3231 | 2025-07-16 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 157.6 |
| a6eb3e73-657a-3845-bbd3-2b862507987c | -10.6015 | -46.2314 | 2025-07-16 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 7ce3322b-6c89-311b-a86d-9edb220ecc48 | -10.3211 | -49.9138 | 2025-07-16 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a1253ec6-7c9e-3b6f-952b-e411e923651a | -12.4267 | -50.0603 | 2025-07-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 05c8fac5-8797-3a68-a89b-99367f3b365d | -12.0825 | -43.4753 | 2025-07-16 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 2c62db87-8e9b-3374-9b6f-98a03431d916 | -8.7611 | -46.5985 | 2025-07-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1de66aa1-e9d6-3702-8135-7f44bf1a6f2d | -11.4786 | -47.3306 | 2025-07-16 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 89fc99d0-fc3b-3de6-a1f7-87f3ad2b3c9e | -6.7192 | -44.3461 | 2025-07-16 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 8d886f58-c16e-3beb-bf8a-14d717b68a7c | -12.4797 | -46.9243 | 2025-07-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| b97c70e6-f07a-34f5-8178-37b183ad8186 | -6.668 | -45.6922 | 2025-07-16 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 03254791-ca23-3e9d-bbbf-306584bed423 | -12.4079 | -50.0411 | 2025-07-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 315.1 |
| 8ef03c59-d181-3080-b230-e5e865f22ed0 | -12.4274 | -50.0171 | 2025-07-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 9dc89f7e-ff24-37b7-a155-d1822ce510cf | -12.4801 | -46.9017 | 2025-07-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| df4add3a-ce21-39d5-93ac-64c163c5b75b | -12.4989 | -46.9215 | 2025-07-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 4d551359-fdbf-3a1f-9bfa-7bc8391d4ba1 | -10.3211 | -49.9138 | 2025-07-16 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f24a33a6-158b-3a46-b258-55f9fd0e93db | -6.668 | -45.6922 | 2025-07-16 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 93e3718b-70e7-3427-95df-f53679fc4071 | -6.6678 | -45.7147 | 2025-07-16 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| dc93e1a8-668d-345f-8e70-e3dc2636c3f7 | -12.4797 | -46.9243 | 2025-07-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| ebb3a9be-5732-3a14-bf17-2f448d7709d0 | -6.7192 | -44.3461 | 2025-07-16 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c6f52615-5fe2-3aa5-874e-b8a78bba4890 | -8.7611 | -46.5985 | 2025-07-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |


[Clique aqui para ver as próximas entradas](README29.md)
