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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f52de397-44e7-35c4-bdfa-2a7b80bc1b37 | -14.53688 | -50.3353 | 2026-08-12 05:12:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b68b3915-85c2-36cf-ab84-2472256cae8e | -14.34343 | -54.04959 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 029ccd65-3758-32a6-9adf-fdfcadf7ec9c | -13.8551 | -53.81477 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1517d8df-bd1e-3fc5-94c1-66e138a46b70 | -14.52825 | -52.78898 | 2026-08-12 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fad5acb-25e9-3a2a-b2f5-349ae09a9a02 | -14.02889 | -53.59552 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3030a937-5f44-38a3-a091-8a80a8430d5b | -14.98174 | -46.60797 | 2026-08-12 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efe39a7a-7236-3f58-ad24-34f67567f521 | -14.54871 | -50.39392 | 2026-08-12 05:12:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7067e555-f621-3759-9e28-86ad2f8fc2fb | -13.87626 | -53.82708 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d04db97e-9f88-3f34-95ba-2ef2a24dead9 | -13.85449 | -53.81909 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b22565b6-d278-3e32-b9da-ed548d3bcbc8 | -15.00059 | -46.60439 | 2026-08-12 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d892eec9-d029-35b7-a2d8-5523a12298fc | -13.3033 | -49.70326 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 970da4fb-478e-3f0e-a2f6-2f54bb601a3e | -14.976 | -46.60414 | 2026-08-12 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b70efe2-57d0-3245-b0ba-43460cf02982 | -14.47778 | -51.8727 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 345c82ae-2934-348f-a346-7e269e916eb8 | -13.8277 | -53.8196 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a8172aa-0d9b-3f2e-84e1-271228986fe4 | -13.53044 | -46.2897 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82b7f793-fd05-39e1-b93e-7861b3849cd1 | -14.51739 | -49.2957 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdf5aa63-e294-3a6d-a550-93921e4eb16a | -14.27852 | -51.97786 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91f8f29e-ae49-3e8e-b81c-23f3a06084f6 | -13.89712 | -53.78807 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5e7c23e-28bc-31b0-b23e-42aacccb5e42 | -13.28769 | -49.69711 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54822eab-35f1-3b90-b622-567e6acea7d8 | -11.10827 | -62.88859 | 2026-08-12 05:12:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3df9a6b7-277a-3c61-984f-0df139c5fb49 | -13.3009 | -49.70993 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a79aae0-d2a0-33d9-aee8-6716d5c451a2 | -14.52049 | -49.3028 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d5c1a2f-338f-3681-892d-4a5a9cc8a98f | -15.29511 | -48.87365 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1be56959-7f7b-34e4-be93-1fda5f09c637 | -13.59786 | -46.24092 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1d42d05-f0cf-328f-810e-7e04f1865048 | -13.54419 | -46.27729 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f3226fd-391e-3b0b-8dfd-5044b950caac | -14.48478 | -51.85278 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6eed3a2-87a3-395c-b474-2cf1ae9f6d4b | -13.86877 | -53.82608 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf839cff-1f76-3b6d-9156-2a051fb424a9 | -14.35503 | -53.06403 | 2026-08-12 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c372e6bf-2459-3369-8d04-135e2f8c7ad1 | -14.51578 | -52.1367 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2db9efdd-8356-31a9-98d6-08d680c250f2 | -13.83142 | -53.82026 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db3e2e77-4e91-3df8-a951-34075d3a638f | -13.29741 | -49.69828 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8449a39c-8c7e-3256-b9b9-5177a3b14408 | -13.29017 | -49.69046 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 497bf1b2-cb3f-363d-a72f-2dca4be9175d | -13.88656 | -53.78166 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc9afe5b-19d0-3a80-a5db-ec9652c83ade | -13.28837 | -49.69157 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72ddf775-edc2-3d32-8792-2d143e8498bb | -14.51306 | -49.28917 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22299898-83ba-37ed-8e2a-8ed4f2b1ec72 | -13.90688 | -53.8266 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf938839-f079-307e-8e3b-399f7ffc8917 | -13.87042 | -53.76042 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32b27903-3fc2-3925-9a4f-74c3368a0bd6 | -16.28259 | -56.60013 | 2026-08-12 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2cefe796-6582-37d4-af83-e80c35d5606d | -16.10362 | -49.88402 | 2026-08-12 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 67c96671-ae9a-33e6-8614-98f44599cb1b | -14.36423 | -53.23164 | 2026-08-12 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41bd7a2a-c9ea-3764-8b33-28b701e04f9f | -13.90117 | -53.83974 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 75bc4678-da9c-3505-ab28-928da3f2e373 | -15.29992 | -48.87807 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4923127b-73c1-307c-a901-0fb951fb10c3 | -13.57165 | -46.25337 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 993fa4b2-7d62-34ef-b95f-14a3bb34cf67 | -16.10787 | -49.89074 | 2026-08-12 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4876afee-d032-39c2-a2fa-563f1611520d | -13.53809 | -46.27659 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 064a0b37-abe8-308f-8a87-289a3c63d6ac | -13.85197 | -53.80986 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ed46f42-30a5-3101-b3fd-47549453dac1 | -14.34034 | -54.04455 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5a8eec38-7290-32d9-a7db-76585237004a | -12.72432 | -48.4414 | 2026-08-12 05:12:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9feca5a5-6845-32a4-92ae-79479904dd6c | -12.72922 | -48.44485 | 2026-08-12 05:12:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0fc389e-e025-3a41-9dc7-9230817e3f3b | -15.00676 | -46.60422 | 2026-08-12 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f12b3b4-faa8-3294-a357-fc2fcbfc417f | -13.87688 | -53.82272 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f524fc5c-8e85-3ebc-ad46-4ba4fd7f8518 | -14.28273 | -51.97844 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81bdeceb-eab4-335b-b491-8a1c413a6b2e | -14.99442 | -46.60453 | 2026-08-12 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54f77d8a-9246-3c95-9f29-a6f465815a7e | -13.90136 | -53.81186 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe333995-83e5-333e-a48b-0be55da243f4 | -13.9033 | -53.79835 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 633791d8-be1f-37ca-97fd-a425446f9418 | -14.51265 | -49.29243 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f1c13e9-aabc-35ee-a96b-7ffd045cfb03 | -15.6836 | -56.04338 | 2026-08-12 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aa303871-1515-3cfd-a528-fada36ff6f75 | -14.54807 | -50.39898 | 2026-08-12 05:12:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74e784b1-e302-38aa-8c36-6a81b52c623f | -14.35503 | -53.06841 | 2026-08-12 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65ddc372-8070-35cc-93c5-ee7aa8c66c69 | -13.28823 | -49.62933 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69d75a6c-d089-3591-9945-199d15711a6a | -14.30618 | -51.99697 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f4746b7-625a-33d3-ba21-5e9b3bcff912 | -14.51944 | -52.14126 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c9c151-c707-3e72-8bdd-672cdacf1543 | -16.15961 | -46.80887 | 2026-08-12 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f753af-29a4-3cd1-bb49-e7d779fe3fc9 | -14.47832 | -51.86866 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3504c1fb-ca00-3490-bf5c-9f317caec9cf | -14.28576 | -45.28933 | 2026-08-12 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a45870dd-df19-31f7-abc3-d7f9989cfb6f | -13.83017 | -53.82921 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97a48a8b-fd40-32f9-a0c5-f89c1242d7a6 | -16.10293 | -49.88986 | 2026-08-12 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| dd7423dc-f20d-3f40-ba8f-143cccbe7bc2 | -14.36103 | -53.22599 | 2026-08-12 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87bb800d-241c-351c-b566-41b1344f6b75 | -14.52218 | -49.29861 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1d189ad-4e5e-3fcd-baaf-69ffbe512f85 | -14.03268 | -53.5961 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 407e28c6-4b22-39ee-a731-750fb04d4a58 | -14.3329 | -54.04359 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dff57ae3-d1f4-3ca0-993e-ac6334f532ef | -13.90379 | -53.82154 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bba08381-12f5-3203-80ea-e9b4aea90b0c | -14.50461 | -49.27421 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ac8bcfa-7ba1-3795-a677-95223b773cc2 | -14.52255 | -49.29568 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88af51ac-d738-36dd-84cb-b09bc706556b | -13.43533 | -57.05191 | 2026-08-12 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9fccbfd-0bca-3cf5-a4d2-de3ffc70795d | -14.29512 | -51.98309 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6410e33-5026-332f-8be7-69effa33fb4d | -13.90314 | -53.8261 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c372972-353a-3051-adcf-2b35e736973c | -13.83965 | -53.78873 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72dfda03-021f-3602-b744-71afb6c47190 | -13.27842 | -49.66685 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 057e6c86-67c9-3b56-be2d-74f757f18e04 | -12.13477 | -57.99105 | 2026-08-12 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaf67882-b124-3f2b-a0a9-36093918d22a | -14.02957 | -53.59069 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c92380ab-a121-3f34-8918-b04548128a64 | -13.89826 | -53.80687 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8796f0f5-bb95-3b83-9190-ebf7f1fb7fef | -14.44274 | -52.25912 | 2026-08-12 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac1213c-0d22-3834-963b-05b7f29b53ca | -13.89338 | -53.78748 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d1c0956-b690-3cc0-a0e0-bdc94cdae1ea | -13.84031 | -53.78405 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f6f3e9b-55c7-3d6f-8b45-ad61a39b4f44 | -13.29845 | -49.70263 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 805d7f33-2fe5-34e2-9171-bff23d3516a4 | -13.86815 | -53.83046 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c921aff1-dfb4-317f-9285-6fbab8158d40 | -13.90931 | -53.83627 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8846062-6ae9-3b57-a6f1-152cab306cda | -14.35655 | -54.87173 | 2026-08-12 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc102c0f-bf7c-37e9-9907-b9cee75af12f | -13.89404 | -53.78284 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a10a139-308c-3eac-a9ac-2e152c09dbc3 | -13.87188 | -53.83104 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72cddbe9-cdcf-3372-aac4-71161acd73d9 | -15.01294 | -46.60405 | 2026-08-12 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbeb46ee-badf-3e95-a444-dfe4cfa398c2 | -13.87251 | -53.82666 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22446d5b-7d7e-34a8-907f-9603c469f026 | -15.30443 | -48.88509 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af37465b-7fc6-3e8f-8326-2038c7ad163c | -13.87418 | -53.76093 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3eb6505-97b4-3f92-9bac-9136b8b75403 | -13.25473 | -50.37931 | 2026-08-12 05:12:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 976f63cb-5ab1-35e2-a21b-3b97eba5ab57 | -14.35755 | -53.6449 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e3042e0-6e08-3541-a880-5cfc8dc48888 | -15.30107 | -48.86849 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8fe94550-d722-3471-b34b-dc17b42bbd01 | -13.90266 | -53.80283 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 004fe985-9ea7-344a-a881-ba5bacc74f9a | -13.29673 | -49.70378 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README32.md)
