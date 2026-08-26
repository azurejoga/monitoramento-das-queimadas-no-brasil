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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24305be2-5b4b-3c68-83f5-0b753b7019ab | -10.76251 | -54.03956 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| dbbe37c1-0c7d-308a-8e89-efaf5a63e5c2 | -12.66965 | -48.40881 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2eabbd52-a4c2-3910-acca-6f0b967888e0 | -10.76305 | -54.01451 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c61ff836-df02-3da2-a4e9-a82aca6faef0 | -14.79409 | -48.80013 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3be57898-ea2b-35bf-adeb-f22ff2644555 | -13.25479 | -51.39348 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| faef08fb-2be5-3585-98c2-c7513a82a67e | -11.79734 | -47.64458 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1f90d7b-acb1-35f6-b2d7-b13d582ca295 | -12.02243 | -46.01534 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 464e19d2-15e2-33f0-9267-e359f134f76f | -15.88271 | -48.35011 | 2026-08-26 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a890830d-e967-38bb-ba41-d3b49d26722c | -12.95037 | -56.61266 | 2026-08-26 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cff077f3-b6b1-3c70-b921-96df0b6d74ed | -13.23633 | -51.52046 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44807f40-b553-3229-af5a-f00981fa7df6 | -14.7613 | -48.78772 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0f78bd5c-06d2-343f-a79f-58fabbe6ebd7 | -12.69433 | -48.41653 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b75893e-883f-3d46-8ee1-3adbfc1267e0 | -9.11173 | -60.39219 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6043b97c-956f-34ca-96fd-c1013778fcfc | -13.27691 | -51.46252 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a39727e-6cb4-3ef5-9397-d799000133dd | -9.13505 | -57.5829 | 2026-08-26 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2c7e216-801a-3524-8a94-ca1900e2d3fc | -12.67382 | -48.40971 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3641b35e-100c-3a38-a2ef-9fc8332770e3 | -14.29324 | -51.13393 | 2026-08-26 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf9a517c-34ed-3a69-b830-068c8e707ee4 | -13.18946 | -51.34134 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 43d97761-bff4-3acf-98a6-1d61dc8fd8c6 | -9.10705 | -60.90568 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f9cee35-397b-3e93-8b6a-60f6e3a5ad24 | -13.65973 | -51.84341 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a05f67ba-ecb7-3162-bd41-58e53731f6c2 | -14.32598 | -51.73211 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6a5b56d-c901-36f5-b946-86db33fad399 | -10.76581 | -54.01855 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b68587e2-9ee6-3382-8887-56fb7b97b1da | -9.0923 | -59.40639 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 776d3f61-22eb-3519-ab98-a0ac7b626394 | -13.36932 | -48.20288 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63c21ce2-4016-3e92-9a11-9acf6eaa1386 | -10.53593 | -50.78057 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 665391c7-3d42-3a29-b59e-c317af5c3242 | -13.98277 | -54.03396 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e44b0ec-884f-3c1e-bb47-ade816d305c5 | -13.24516 | -51.53429 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a9619b9-1974-3796-9601-f2817b176dba | -10.76195 | -54.02152 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 56c72be6-824b-3367-97b9-be75d8f6a1cb | -9.60548 | -55.10991 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 468e5929-272a-3368-ab10-fc1bf9a7ba34 | -13.25895 | -51.3899 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 6e3106f3-05a6-3b3d-8012-000eedf1c930 | -14.12695 | -52.36399 | 2026-08-26 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d761e796-4424-37da-a0db-dfabf61af0ee | -9.66634 | -55.14248 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7445ef7-1f1c-38a5-b04e-565ae86dffb6 | -13.33805 | -48.20728 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a846939-178f-33de-829c-74f872fd7a02 | -14.58963 | -52.03026 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd0a5d87-2313-3ac5-bab7-172e79f3a8e0 | -13.28459 | -51.45951 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a23f952a-1434-3d67-b3aa-489eb64dd2ee | -12.79898 | -48.37635 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80f9fb85-1a96-3640-a4d6-296498b34b5a | -11.16716 | -53.99712 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 781d2893-28ee-393c-9c7c-d3046b986583 | -12.12436 | -43.3812 | 2026-08-26 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fd2b2e2-e34d-3002-86fb-1766d7604ed8 | -9.67279 | -55.10198 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e65c8229-1cf0-39a0-86ca-6f6551dd483e | -12.65451 | -48.42604 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8284f5f-8619-3ed6-ad7d-615680f632ba | -8.81632 | -62.33215 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20b6a22d-c2c6-3095-91eb-768ebb416609 | -8.64547 | -62.89223 | 2026-08-26 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97737089-e93b-3808-9c96-a33ceafd9cbc | -11.48855 | -45.11235 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f23669f-b846-341c-b1e1-231181780605 | -13.25835 | -51.39402 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4a255d8a-190f-3dcd-857e-8b0d30cea973 | -11.37507 | -45.16399 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9125b4c-4dbf-3cf4-bdbe-f1b4d086228c | -9.99545 | -53.96544 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7096872-5bf4-3cc7-b7ec-a75784105717 | -11.1633 | -54.0001 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 844b4be7-a6f0-3289-bb3b-ee5d601cebb2 | -13.26191 | -51.39457 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 3be5b1b7-126c-396f-82c0-6223138b061a | -8.81573 | -62.33541 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99d32b83-b4d8-3cd1-8cf0-f06586b99885 | -11.29144 | -47.07291 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe40fcbe-16cf-34b6-b4f2-30d608bf7ff5 | -9.66498 | -55.08565 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d02bc56c-c0ba-34f6-8019-30bae250c5e9 | -9.9264 | -53.64687 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c96dc98a-550c-30a5-bb29-f140701eab32 | -14.3189 | -51.73102 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a07ae95-980f-3b33-95f7-8cf785eac095 | -12.6901 | -48.41613 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e5eebb3f-414c-3035-92b3-56e740ba74dd | -9.10795 | -60.90053 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1e99e16-2377-32d6-8c5c-dac3f0539dd8 | -11.81525 | -47.67723 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a9f18beb-6fb1-39c9-b94f-dff8fdd2f426 | -14.12406 | -52.35962 | 2026-08-26 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7d70773-6589-382d-986a-d2603a0aa925 | -13.86011 | -54.05758 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b49fc6f-907d-3f13-bf2b-112f0010e6f5 | -9.13513 | -57.5588 | 2026-08-26 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e3034c9-5ef0-30d8-9604-af3cd701cb65 | -12.00141 | -45.94386 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5bcb983-88e7-3d8d-a7a5-8e611cf43a5a | -15.76475 | -43.37608 | 2026-08-26 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2aa6ddc-0fea-3dbd-a786-062ba7f3b7b7 | -11.16606 | -54.00413 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8498e40d-4dc0-3535-8750-9bbf2c6f09be | -13.18888 | -51.34548 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e89f9d73-8009-34e7-a816-28c6d418928e | -15.60437 | -53.12559 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a9660525-0dff-3edc-8126-70506b0ebb24 | -13.6841 | -51.77333 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e29754b-24d7-32cd-aa1b-c56324f32ae5 | -10.49932 | -49.27491 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a50fb32-6d55-3ab5-9494-6d8dca7bc4ad | -12.65968 | -48.41932 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 949c3f1d-5457-3624-b9e9-2418ebd76321 | -9.47152 | -56.9092 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f4e5398-0e73-3980-a9df-3a6d6129bca8 | -13.25461 | -51.5191 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bfb5658c-9fee-3725-b450-059c71c26f87 | -11.97316 | -45.88806 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3eb7206f-c5a8-3785-8360-9e47e66f83f0 | -10.77188 | -54.02311 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c9f458d-1dd2-3922-b8e8-a3e5d806c444 | -12.08328 | -64.24406 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a71aa12a-69a4-3dcb-9190-2d87c5d21775 | -14.78894 | -48.80659 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eda58b2a-81a9-3cb9-901b-37e1a70e738b | -9.69608 | -55.15817 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 661519f3-6a51-3f17-9538-cf859f79498b | -14.53446 | -52.28542 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f67ad7ba-c9f7-388f-a821-07cfd24eab4e | -10.76085 | -54.02853 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 965ef3b8-d188-39d5-adf4-86cf716957dc | -9.17778 | -59.38781 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9a9b456-c84c-3f18-bf1f-c7e719dba456 | -13.85789 | -54.04997 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc0ba986-d982-3dd6-81e0-e0eced1cf406 | -12.69057 | -48.41262 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 95db2495-aa23-3c4a-a548-af2f8847425e | -14.90856 | -52.69296 | 2026-08-26 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74d5f61d-f411-3a06-b6e8-c3e148de3aec | -13.65564 | -51.84695 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec70626d-3753-3ab6-9633-017a82db0807 | -10.76471 | -54.02555 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 26894926-dc13-368d-952b-5a6e069ee982 | -13.24114 | -51.41245 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90ccdf12-1792-342b-89a1-4812bbaecff8 | -14.53584 | -52.00554 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f45a5183-3099-3800-b8c1-3d81f5c85d66 | -15.68894 | -53.89545 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ff5ea7-aa29-3755-935c-3a2677fae902 | -13.28814 | -51.46004 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 06cd3d88-9c23-3ecf-b187-d5584aceb6c2 | -13.24988 | -51.52669 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e2f7b06a-0120-35fb-8fed-743855d3ef28 | -14.80254 | -48.80128 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0cc42b0f-0537-35d5-9aa1-f9201ff59a09 | -12.68216 | -48.41148 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a42d8a82-791d-33bf-add8-3b354f186042 | -13.37618 | -48.21726 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| afbb7606-04e2-346e-8d83-4eb8f1a3bf3b | -11.19601 | -55.08443 | 2026-08-26 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2545007e-0448-3133-b8e7-0ae3b889658a | -11.11681 | -49.88311 | 2026-08-26 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23082fd4-f14d-3c91-a0e2-3bbc29032c2d | -11.79353 | -47.63969 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1af76b08-0fa0-33ab-bc13-e56c8d4ebb15 | -12.73037 | -48.37246 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51fa6aaa-2e37-3f5b-a521-78eaeb0dfffb | -9.97446 | -53.94777 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fec451d-e527-3fb7-8f9a-f673583b8ad0 | -11.42584 | -44.5359 | 2026-08-26 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 908e6f98-64c1-314d-963e-5cac4158af00 | -13.60572 | -49.01031 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36905e09-c41c-3b0b-b0fc-e61918524579 | -11.84285 | -49.14559 | 2026-08-26 04:53:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc67adcc-fc75-3b8e-ba10-60883cb05a59 | -10.75257 | -54.01643 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86879c38-a6b7-36b5-93a6-70d7def419a2 | -10.91527 | -44.73898 | 2026-08-26 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README45.md)
