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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e161751e-15af-3e26-81fd-ddc29def1404 | -9.66668 | -63.24083 | 2025-09-09 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f41fb320-cacb-3b1e-97b2-e72038f1e3f4 | -16.63148 | -51.85384 | 2025-09-09 05:25:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4dca9d-8ce9-36b7-8ef8-b062b8bd61b0 | -9.16896 | -59.37643 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4c92e4b-eebd-3912-b08b-202595461bd7 | -9.08544 | -65.37466 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5e4b49d3-8ed3-3065-ba72-0585028f2e37 | -11.46874 | -49.26844 | 2025-09-09 05:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccee984e-e190-34db-ba1a-251a5d227a9b | -10.01142 | -64.91857 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2caefa2-a548-3d33-931a-c0c48a62a954 | -9.87205 | -58.31901 | 2025-09-09 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b943761-5216-3ec3-8292-8cc99bfcbb13 | -9.2232 | -60.8201 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fdee17d-8289-33a7-8cf3-18c14d8875e1 | -9.19975 | -60.62255 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cf8752e-960b-3dbf-a5de-1efafe8f9fef | -9.19376 | -59.3763 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d5ddb16-593d-31fa-8c39-e83f640ef930 | -9.45106 | -60.51148 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2543d6a2-61eb-30b6-bd2d-e7257aa359f4 | -11.21188 | -54.99261 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17a1c0ed-27b1-36c6-826c-d000a7d8d787 | -10.24869 | -59.38846 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2bef9f7-ffb9-3113-b4c4-7b909c3142ab | -9.22706 | -60.81712 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80de8945-cefb-32b2-9866-e81eb4a98fd4 | -11.22155 | -55.00558 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a46399f-ef22-3898-a247-bf4c0ac09b1e | -7.55462 | -69.90764 | 2025-09-09 05:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96910c12-cc4e-3a0f-b6c1-4ed24a967be1 | -11.95294 | -50.97899 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3ed7e7f-9d80-3fe6-ab15-2353aa8cb2bc | -9.46268 | -60.50249 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea275b1a-960e-3561-abc2-ad3fc770eba4 | -19.83341 | -50.94439 | 2025-09-09 05:25:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9287dadf-c099-3d71-b2da-1568afaa1095 | -8.76824 | -61.44358 | 2025-09-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9397f593-3e3a-3d6e-85ad-022360782380 | -9.21988 | -60.81957 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6688202d-795d-30dc-b522-8ea5c5e99b83 | -10.4191 | -59.60217 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6fe6de0-4e1f-327b-8ead-3dd3be70aa07 | -10.00628 | -64.92673 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e409ab6c-50dd-3688-bc16-6889042af5d6 | -9.1718 | -59.38067 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8754d179-45bf-34cd-aa97-cbc6279480ce | -9.1271 | -58.8955 | 2025-09-09 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57c38e0f-ef07-3056-9798-96e48bfe4c61 | -9.93154 | -65.23518 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28bbb9f5-e68e-3ff1-ab7a-d21da40476f0 | -18.82585 | -49.6967 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ad39ecee-4fb2-3ca1-b645-f236d3201197 | -9.1701 | -59.36897 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 674d7803-d45c-34a3-af1a-a88a456fb0ce | -9.37249 | -65.94186 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64fef025-1f55-3518-bc86-96aa577470a5 | -9.26026 | -67.6058 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0656956e-82e5-3c1c-b9f5-2646333d7357 | -9.27301 | -60.91385 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd9413aa-1666-39e3-8384-4e5fa2139c7e | -11.55168 | -49.05266 | 2025-09-09 05:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f0dfb3a-2f2d-3bff-a708-257c3a268059 | -11.31382 | -55.12194 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39904658-69cc-3b91-b6dc-da374477dba7 | -9.47484 | -60.48996 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ff45cd2-ebd7-3983-a406-a8f8718ce810 | -9.16441 | -59.38332 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b7c9cee-6ee9-3afa-ac48-24dbc9528057 | -10.5779 | -52.03758 | 2025-09-09 05:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2deb86b2-3ce7-32dd-bd69-446ecc2d5b0f | -9.34278 | -65.45611 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efbb107b-c663-3020-8e5f-70e34ea823ee | -9.05499 | -62.3461 | 2025-09-09 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff088d3-575c-3132-b4a9-1733d932f7ef | -10.41149 | -60.79622 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8039e477-d8d8-38cf-8be9-73608db86fd1 | -9.08229 | -65.39363 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8750b68d-3271-346d-9870-6c773ad1305f | -9.98715 | -64.9958 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c94cd050-988c-3dd5-bc91-1391f536df62 | -9.44315 | -60.52084 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 862932a5-4b25-3b27-9163-b01e09745d32 | -11.93304 | -50.96525 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc7d4729-8ad9-30eb-bd99-804b0dd42bce | -9.4437 | -60.51732 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d47ac7ee-16c6-3a43-81e6-f859558c683f | -9.70457 | -64.53493 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 598cec91-2414-3225-a0ad-ad0afb2b6c0c | -12.01902 | -51.0799 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1bbdfda8-4cb5-38f7-bddb-d3bcc3461ec6 | -11.82624 | -51.40671 | 2025-09-09 05:25:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc94b0fc-a5e4-3f95-8226-a80d44a3c3a2 | -9.16801 | -60.27855 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e4bbccda-8458-30de-954b-673c5d186baf | -11.97411 | -51.0038 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a05b0d2-4460-3581-a043-1cf02944a2aa | -9.19035 | -59.37578 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c1cce11-5c62-3506-8281-430c9bc288f4 | -9.23605 | -60.43391 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 096c2c71-64b3-33f6-b575-c0a419f0a6ed | -7.91101 | -70.22346 | 2025-09-09 05:25:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4a33b2d-6aa9-33c6-bc83-cc25984e1429 | -10.9061 | -55.70443 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffe79a21-3661-33e1-9f48-d8e31985b8a2 | -9.48635 | -62.38997 | 2025-09-09 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27f4a57f-dab0-3acd-938a-ff01341608b9 | -9.94157 | -60.50152 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f1d942f-9a15-39f6-8dc2-4b0d6d3fef4d | -9.84 | -57.83378 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 645e3ffa-ed32-3afe-ba4c-c66a6f465fb9 | -9.21934 | -60.82306 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8a26e7b-101b-36f0-8cc5-da32f534a57f | -9.91954 | -65.23779 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8be8bdf-ad7f-3368-ba68-6337addf96d5 | -11.16234 | -57.18481 | 2025-09-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 847cf0e3-db4f-302d-92f4-3ed1270f28aa | -9.44543 | -61.82153 | 2025-09-09 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef283700-4eca-3a49-af1b-3f2292d78373 | -9.12999 | -58.89983 | 2025-09-09 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c33f502-6e3c-39c0-8509-54f8f0ec294f | -9.79705 | -57.44712 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e59e79e-2ca4-315e-857b-7667f287c2aa | -10.89758 | -55.7033 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d38a4732-36a6-3615-a955-1c71cdd44b0e | -11.20678 | -54.99651 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95e065db-6452-36b9-a16e-c5943ffe8933 | -10.42526 | -60.75138 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e754233d-117a-319c-b808-4ea9c86c1082 | -9.44813 | -60.51079 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da63e795-0306-31b0-ad98-d99072ca3d02 | -9.16241 | -60.79583 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07f5de3c-117c-3de7-bec2-ee3aa315f427 | -9.16691 | -61.30751 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97a3c055-e621-35a5-91c8-be1acfda8c6f | -9.12391 | -65.95804 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07622af4-22f5-3353-aa8e-8067400ffe6b | -9.16498 | -59.37962 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9c7b156-43ac-3ea4-8552-f0175da072c8 | -12.1991 | -53.8817 | 2025-09-09 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 37bb0c21-4bb9-3f42-be0f-60aaa481c46e | -22.665 | -51.3857 | 2025-09-09 05:30:00 | GOES-19 | TACIBA | SÃO PAULO | Brasil | 3552908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| fa34ad4b-a0b2-311d-a4ac-144c51a5bc76 | -12.1988 | -53.9024 | 2025-09-09 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 89fc76fe-e44d-39c6-8dce-8d8c84ffb782 | -21.4355 | -48.827 | 2025-09-09 05:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 18053fce-e5c0-385b-bbd4-b88e2e490710 | -22.8393 | -52.6307 | 2025-09-09 05:40:00 | GOES-19 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| 8e07f603-22e2-3357-bf48-ded549017688 | -22.8184 | -52.635 | 2025-09-09 05:40:00 | GOES-19 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 117.8 |
| 555579b7-5595-37bd-ac7f-fb11299d72ac | -18.8174 | -49.6816 | 2025-09-09 05:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 24041fe5-e7c5-3073-80ac-8bf4aa3833c8 | -22.8387 | -52.6532 | 2025-09-09 05:40:00 | GOES-19 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 147.5 |
| f6b28cc5-f987-3f4e-aa66-8f0e5e136991 | -21.4548 | -48.8687 | 2025-09-09 05:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 3a2b2214-b635-329d-aa77-d8db7782626e | -12.1988 | -53.9024 | 2025-09-09 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3488e1bf-eec9-3107-9043-fa71ac87807c | -18.8375 | -49.6777 | 2025-09-09 05:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| 66e0f491-b528-3e45-a78e-975874bbe15d | -18.8369 | -49.7003 | 2025-09-09 05:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 73510c79-4bea-32b4-9ee7-c02042dfc15c | -18.8168 | -49.7042 | 2025-09-09 05:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b93a34ff-0595-3c8a-864e-1779f8084a2a | -21.4555 | -48.8455 | 2025-09-09 05:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 96832f5c-69ff-3fb0-a1c5-e9f0bd818e07 | -12.1991 | -53.8817 | 2025-09-09 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 250f123b-0fd2-319c-87ce-c149aeba00e2 | -21.4348 | -48.8503 | 2025-09-09 05:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 3ba0f64f-1cd9-399d-9e84-52572547f5c8 | -22.8178 | -52.6575 | 2025-09-09 05:40:00 | GOES-19 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 224.4 |
| 8f067395-0060-3a5b-a1dd-ce8ec453f3ff | -5.45061 | -43.43077 | 2025-09-09 05:48:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7d261ce6-3535-3f2b-b028-0a37624f99c7 | -5.45158 | -42.79762 | 2025-09-09 05:48:00 | AQUA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| cc8afa15-1b8f-380f-be48-956c7c75ac96 | -5.70902 | -45.40754 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d20f1222-56d0-327c-8cf6-47e7bef4d813 | -7.65912 | -50.27641 | 2025-09-09 05:48:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d7785ae2-f814-3492-999e-69e912746853 | -5.81323 | -45.64306 | 2025-09-09 05:48:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c4cdbe47-14fc-37d7-a811-2428d9fd371c | -5.66955 | -45.3118 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 467d6c1f-d080-3581-aaf7-a5fbabb6988d | -5.84835 | -43.8585 | 2025-09-09 05:48:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| af2e3f8b-732c-3e92-a344-4de4ad5ccc82 | -6.58376 | -44.00592 | 2025-09-09 05:48:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 163b9224-2be0-3285-9f77-63ccaea6d893 | -6.87935 | -47.90285 | 2025-09-09 05:48:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 66bb27b4-c21a-3618-82dc-58e419c69051 | -5.55034 | -45.17414 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| ef17426b-1e45-37af-b700-e2f20809a06e | -4.26868 | -48.18659 | 2025-09-09 05:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1fc42407-d55c-38d7-85aa-b77a37dc2463 | -5.81434 | -43.96461 | 2025-09-09 05:48:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 613508c8-f628-3c82-a7ec-ca8d923dfb17 | -5.71915 | -45.40004 | 2025-09-09 05:48:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README68.md)
