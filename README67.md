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
| c16be8a4-74a7-3ba8-8285-68a2b6bf07d6 | -7.06087 | -59.22666 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7f86dd17-4cf9-3bcd-ae5e-d8e1dd9bedf7 | -7.00374 | -59.3111 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 551480f6-4bbd-31ff-8d9a-009da429fac7 | -7.01794 | -59.24261 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3381ce13-f6ea-352f-a74c-70779390d391 | -9.6743 | -55.09441 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13a61f93-e34b-3f6b-9ba5-3c0fa2a084c2 | -9.39554 | -60.59221 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c13e03bd-9b9c-34c1-9c94-743b7570cf83 | -7.51949 | -61.3922 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 325252f5-4ada-39de-b125-dda0bea1fee2 | -7.77908 | -61.56569 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83174a1f-18fb-3239-baae-4288cd6a698b | -7.51708 | -61.38192 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 3ed71f44-9a4e-3950-871f-02799dc6f5a1 | -6.996 | -59.27032 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 936e9c90-ace3-3f72-9e55-d984205a1692 | -8.81556 | -62.31471 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 067e30ab-57fa-3588-93fa-89d00e2281a1 | -7.06972 | -59.22802 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bae6a494-b769-3b79-a3cb-f4b373f7dcd6 | -9.13539 | -57.56089 | 2026-08-26 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5721efa8-b1ab-3730-9953-905799f81b9e | -9.61022 | -55.11365 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ea68ea18-85c8-3f31-a7dc-7e57c0deb2df | -6.40878 | -60.05524 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdef2567-3b9f-3a96-9f22-8a311022d24e | -6.27273 | -53.35996 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68e68d37-f50b-30f8-a108-2b55370fb121 | -6.82445 | -58.65717 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 55e7ebcf-5cdb-3ead-a68c-0477c131a6c7 | -6.26165 | -55.42065 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e566e44d-f3e7-3bed-a3fb-880713ce4b10 | -6.13287 | -57.82413 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9799f7d3-e848-36f4-8282-d6687b3d75f5 | -7.78362 | -61.56149 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec130997-e12b-382d-adec-7acc35eefdf8 | -7.05961 | -59.23538 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4130883-4a60-3d11-9cad-54be1701e254 | -6.14043 | -57.70914 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a8921f3-6bea-3c05-abbd-b5cbadeba584 | -8.81788 | -62.33589 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7d48b23-842b-31ad-ad69-6b3a332e39db | -9.09341 | -59.41503 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84bf6634-950f-3a67-a38b-879c7accca53 | -6.25189 | -53.3679 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b26b17fc-ad81-3657-a0ba-0822ca511a2e | -6.70025 | -56.14882 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6283b95c-3cf7-341f-b4e7-e9733537c5ec | -6.14528 | -57.70984 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36ec7f47-e497-32cd-9d4d-f947745c5d5c | -7.56043 | -61.42053 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e4899d-ea54-3d7d-babd-df834228949a | -8.81481 | -62.33086 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6dc3df29-8388-3dbf-8dbb-a983b0af6a62 | -8.16916 | -54.95394 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd48af5e-9c52-3f3d-a11b-bf62a2114cdd | -7.47455 | -61.37559 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbcda176-b335-3564-a225-7bfc0c7a4916 | -6.16062 | -53.68857 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f051585-47a2-3cf7-8eca-7d9ad3228084 | -6.86299 | -56.57195 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c0fbe7c-4e30-3d18-9db4-36fcf1d1d2b3 | -6.79994 | -59.59919 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2989e26a-96a9-3070-9095-eb5a887040d6 | -6.98029 | -59.2559 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58d30ce6-7821-3ecc-95c2-fead794b94de | -6.76287 | -59.44788 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 919f9c5c-5013-32fa-a585-74d0fbacd40b | -6.13212 | -57.82946 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1fe44c4b-689d-3dc0-840c-3a3490cad26c | -8.81963 | -62.33816 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d524b73-c023-383c-8a18-4649acce8936 | -8.64539 | -54.74842 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e02080d-e4b3-34d0-be34-dec1070c9743 | -6.14606 | -57.70454 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa3562bf-666e-3457-af95-abce90943c91 | -6.26981 | -53.3814 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3b929353-1f66-3c84-b9ae-bf2d2821943a | -6.62412 | -58.48823 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3331b8e3-b716-33b3-953b-893facf14887 | -8.57007 | -55.27732 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ca777c5-af87-3eae-8c94-c18c1b457cad | -6.12325 | -57.82573 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dfde9bd5-2f7f-3a99-a7ea-1b7b70de2ece | -6.13034 | -59.89234 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cdb1fa4-a396-3722-9743-3f53a8b0f71d | -6.25763 | -53.37417 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bcdaf47-bda0-3850-8cfe-96eb9141f780 | -9.20067 | -59.57994 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31742442-a487-3d42-a6d6-113186608726 | -6.75854 | -59.44719 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29ed8982-dad9-3aee-b691-b6eec24eefdb | -6.71501 | -59.13148 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ff61071-417e-3be6-add8-0d4afb26fd2b | -6.75266 | -56.33657 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b8463a3-b4f6-391a-9657-d81a0d46febf | -6.64908 | -58.51159 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1705543d-8a15-3aa1-bd0f-5a38725bf463 | -6.51133 | -55.23095 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fc72771-9bf0-329c-b462-7daa5d360057 | -7.66916 | -67.04755 | 2026-08-26 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db45ae21-9e4a-36ea-93d0-46b90a451c05 | -7.2146 | -60.61838 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5da19189-2b8a-3d83-b4fe-f9bb97e666d4 | -7.06024 | -59.23103 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00ebe4cb-e6c2-3957-8369-87f32e4de278 | -6.40823 | -60.05899 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64b453b9-ab40-3962-a90d-e1791f3e9969 | -9.66769 | -55.09788 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd6e026f-7715-3400-9ebd-56b6a127904b | -6.98909 | -59.25737 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a8bccba-5a17-3ab8-b52b-e7039ff8cdc6 | -7.47383 | -61.38045 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f313536e-bb7a-368d-94fb-3c0484a2c212 | -7.38581 | -55.15895 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d1f975c-23fd-3c9b-a458-fab291ddc660 | -6.26409 | -53.37506 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 699ebe32-90b2-343e-89ad-024431c6b633 | -6.30281 | -53.56878 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c70fa01-39d0-3635-8297-725b2311190b | -6.71947 | -59.44152 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30032f0d-585d-3fea-bc4c-9383a4121c53 | -7.40383 | -55.15826 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d0ddbf-3c5d-3f1a-8205-f5ef0e2db3f1 | -7.4033 | -55.16216 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63f1f7f7-c681-3811-a1b0-4c7204079353 | -6.33527 | -54.74337 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e1f01dc-afa6-3e65-ba7e-a346b50aed68 | -7.56288 | -61.43078 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44d8e2ce-cff3-3e77-bc96-473d17852a4f | -9.47718 | -56.91795 | 2026-08-26 05:48:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4350c37a-3ced-3454-a8ec-87e7cb326d2d | -6.99031 | -59.27955 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06f77ff8-f111-3de5-9b4e-c9dbf7d75c4c | -6.82013 | -59.58145 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cf79368-f52b-3ff1-a681-beb1d7585840 | -9.45636 | -60.53373 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28fe7dc7-8975-3b9b-b7b6-0e45fb0a8f20 | -8.81928 | -62.31528 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9917d174-af9b-3b49-aa59-8a2ffe1f939b | -6.14604 | -59.92949 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42b35e96-dec4-3870-b0ee-c03a6e86fb6d | -7.37583 | -55.18908 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ca082eb-8f05-3e4a-93ef-e1abea700af8 | -7.06656 | -59.21862 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a663c5f5-dfdf-3626-8697-c87f7f48b18a | -8.81675 | -62.31743 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b64e9790-595e-3792-867a-a0a62b5faee9 | -6.98844 | -59.26175 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb32a36c-02b4-3331-9f51-07b9d12bf408 | -9.61078 | -55.1091 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6e12ac3e-e3a7-3c72-b99c-4aaf9966173b | -6.25262 | -53.36249 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d96a5d9-7502-3c34-8697-87eedfe2d84c | -6.64978 | -58.50676 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5efc6db9-0a68-3b09-a4d5-33d7b0353243 | -6.1518 | -59.92953 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1d3dec2-ac6f-378a-b5b8-db1fa67883e1 | -9.66277 | -55.08803 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7f4d5b1-a7ec-3116-bcc6-6e6e60bc7d68 | -6.25117 | -53.37326 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5ebb812-2bb9-3da2-89aa-d89856182908 | -6.99874 | -59.31471 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 339c195c-e4b6-38f1-9419-b9e9a3615512 | -5.78787 | -57.61055 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a723ce3-c6e1-3093-a8ac-b4b51a0528d1 | -6.68533 | -56.34787 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 849306b0-6e34-3f11-b965-24c85015ca2b | -6.1743 | -57.70522 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d931fb-37e9-3827-8218-4e95d4feeb23 | -7.03244 | -59.23586 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26b57497-8a5c-3715-8fd5-79d1193ff94e | -6.22878 | -55.61967 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2f1d532e-7877-3e09-8c23-cca82c24df7c | -9.18244 | -59.38397 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1edb43bd-7243-3ed9-b8d3-fa6825bca3f9 | -6.83506 | -59.94824 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3357cf8-21c6-30d9-bd5b-1325fbbe5e3d | -6.90635 | -58.99504 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7f81b1d-5aae-3f19-9f3b-b53f98e35c9b | -9.16912 | -58.33768 | 2026-08-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08dba348-c584-369d-87f4-f2af851f56e5 | -5.77617 | -57.55378 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 792f9477-689b-3d15-b7b2-67442555509f | -7.90225 | -63.68627 | 2026-08-26 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85efa6a7-e136-33a2-a9ea-f95046b2b2f4 | -6.12727 | -57.83176 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7cb590be-85e2-3a04-9548-56f2c90778f9 | -6.9966 | -59.26603 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21e0dee0-065e-3ed3-8979-1f8d325be2bc | -7.03306 | -59.23152 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6033c253-7f49-3504-9908-97a80d325d64 | -7.3823 | -55.18524 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fab732c-1af1-3312-9e0d-768fca068637 | -8.22025 | -55.00389 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d64f863f-65ab-3820-a029-36b9e5877cf9 | -6.76943 | -59.44375 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README68.md)
