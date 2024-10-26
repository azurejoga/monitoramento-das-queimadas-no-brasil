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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d431ebdb-6dac-388b-b0b2-ef2f57fe0ba2 | -18.25743 | -56.00199 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 8d6c7cbb-4d62-3195-a412-74a543791de8 | -18.25701 | -56.00602 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| f54b2f3d-3c48-3fdc-adc3-e2cef7be2445 | -18.25659 | -56.01003 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 71265e5c-4f11-3c37-8c3a-6ef0b1d98502 | -18.25438 | -56.00113 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| e6a39620-777d-32e2-98e4-eddfd2e7eb0a | -18.25399 | -56.00516 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 67975568-69ce-33ff-8ab3-36f8ddf6afe9 | -18.25359 | -56.00918 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 7a30a2a5-b246-3ce1-a3ae-7d38bc93341d | -18.25135 | -56.00533 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| d4e7751d-3fb5-39e6-b48f-e76480cf9dd2 | -18.25093 | -56.00936 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| b84bc787-bcb6-35ac-9450-c0707ff31659 | -19.53085 | -56.70542 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| cb5feec0-1f4c-32d8-bf32-0603f198d94d | -17.94637 | -57.54225 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 8d12a5d7-232d-3aef-8bda-306845c4cecd | -17.94591 | -57.54641 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 50de2a49-c028-339a-9bf2-15d117a00997 | -17.94542 | -57.55082 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 910c0892-8bf0-378f-94bb-ec8f82ab3e9e | -17.94498 | -57.55479 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4b6b1d70-4783-35af-983c-45a725a61635 | -17.94464 | -57.55784 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 43cb20e3-41e8-354f-81c4-0810bbf9e827 | -17.94432 | -57.56076 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7ebf2be5-3809-3b89-a320-cb455256ece3 | -17.94401 | -57.56354 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| b3c28436-6d41-3d78-a4fa-6fb316bf7863 | -17.9408 | -57.54572 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| d10fefb5-5bff-3156-8db5-1597a3c6959a | -17.94029 | -57.55035 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9b087c02-b5b1-3f03-bc7b-100bf6ad4c27 | -17.93852 | -57.56641 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c851fb46-27a9-3b89-b2e2-9a75ed76b2d7 | -17.93473 | -57.5539 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| de7f0253-a051-3b8b-8ea9-70d7763c8af4 | -17.93272 | -57.572 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8f5c8550-7cbf-313b-a200-801c9d056643 | -17.9297 | -57.55256 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 07671682-9e35-33e8-a2e3-cb9a852719fa | -17.92297 | -57.56677 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ea472db4-fb3d-3f5c-9b40-dfe355fd66f2 | -17.92266 | -57.5696 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| eda8a449-4d4a-39a9-899d-3b0bc7bcab54 | -17.89673 | -57.5702 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ee6aa843-7d65-36f7-961a-f92094c7468c | -17.88775 | -57.57521 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 86960d11-6aa6-3329-a763-eccb0b93e52b | -17.88272 | -57.57395 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3f223f7c-458d-33eb-92ed-176b08099771 | -17.87861 | -57.56466 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5dd813a0-a690-3dcc-b408-1f7b0b423d47 | -17.87662 | -57.58216 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3e6f8ce1-8679-3f4e-b7b4-aa91d35f62d5 | -17.86648 | -57.58045 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b99ceb8e-da8f-36f9-8404-0ca43ac0c607 | -17.85932 | -57.59801 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 56fed265-b29d-3248-a341-7c8ab2a1861b | -17.85239 | -57.61366 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ec0e0a7d-5c21-3083-a87e-143b2bda2d37 | -17.84224 | -57.6122 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dd99783f-9144-3933-8bd9-16bc6ff3f5e2 | -17.83718 | -57.61142 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6c4e287c-9d62-3a80-80b7-829614522245 | -17.81421 | -57.58612 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 53c9cca6-33b4-34b2-b2bb-6d6f7958c67f | -17.81387 | -57.58923 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| cae179c2-4ee4-340b-9059-267f5f8b6f29 | -17.93359 | -57.56427 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 936d7e37-4cfd-387b-a5ab-4c6deb1e93fc | -17.92782 | -57.56964 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 974f0972-4741-3b5a-a4fb-55b98053d330 | -17.87484 | -57.58155 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b1d97121-90f9-30fa-9e50-ffbac42565fb | -17.85903 | -57.60057 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e268e7a1-ac58-3070-b23a-2bbfdf8678a1 | -17.853 | -57.60821 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 638408a5-ecef-314e-8b1b-469a0b0bd820 | -17.84764 | -57.61003 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 369573cd-f559-3691-bbf5-61aa03f83c2e | -17.84412 | -57.54947 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 03069777-b9f7-35bd-8012-c4e0bbac021b | -17.83907 | -57.54837 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 1ad8284a-9bff-3978-9df1-78bfc28bea53 | -17.80643 | -57.56302 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| caf23443-b173-3cb3-b756-26b028d62ba9 | -17.80302 | -57.59412 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c18a4be1-b0c6-3f13-8f6d-05e89ace251a | -17.79759 | -57.59655 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| cfd11bfc-c02a-357a-af67-32e7b9817163 | -17.78743 | -57.59524 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 42ce55d0-2cbf-38b2-b7c4-01c03b6705b4 | -17.78709 | -57.59834 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 56cd8c6e-319b-36f4-b97f-bdee10c938fb | -17.77927 | -57.58865 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b4f9809f-4c24-320f-97d2-5206f9260e10 | -17.77419 | -57.58798 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1eda8ee6-7ea0-3297-ab33-e52c8ac5ef1b | -17.74861 | -57.54055 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b13b1f88-3ba0-31b6-9f1b-67488fe24df9 | -17.74264 | -57.59335 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 68085a97-5507-31f8-b4ab-a802a2acc1fc | -17.74211 | -57.55237 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| dae14e30-fe23-399c-abf1-93e6fb2361bc | -17.74195 | -57.59954 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| dbff7cfc-d7df-31a9-b7b3-a84d9261a456 | -17.74176 | -57.55548 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2dbe9c51-a0bc-3c94-8465-77173f66ae32 | -17.73757 | -57.5927 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 11528d04-7c8f-307f-8dbd-82cbe46c9f5d | -17.73722 | -57.59579 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b79bddf8-af50-36af-a618-4b3ff0e5cdfa | -17.73318 | -57.58584 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 00bf7649-8605-322e-8fbc-3cc0da81358a | -17.72984 | -57.56967 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 0e66c4f8-3fd8-313d-9eed-54f87b7ee8e3 | -18.10818 | -57.28209 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 855c8f64-08cb-3247-b343-bc2ccd4cd2c5 | -18.10782 | -57.28538 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 526b0b6a-a5d7-3429-b295-4d6018bd8d5f | -18.10261 | -57.28471 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 52961587-0a58-3ae0-8afd-ea8b96701bb3 | -18.08874 | -57.3624 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e6e6c853-b3ed-32dc-87c4-217dfe9726db | -18.0832 | -57.36498 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| ed761a97-e8f6-31ad-930a-eaa9699b9a2b | -18.08286 | -57.27222 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0419fc1e-e8c0-3ef1-ba35-30fd68c8c3a8 | -18.0825 | -57.27551 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 17c07a70-5fcd-3dfd-9f19-de5e7534f659 | -18.08214 | -57.2788 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 01ef5922-a92f-3a0e-8291-bf859aaee289 | -18.08178 | -57.28209 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e921ef68-63d1-32e9-9fb3-f39fc36fecf8 | -18.07802 | -57.36433 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 6f51f9ab-a675-36ee-a089-beb625a2107f | -18.07766 | -57.36757 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| f4bd25f7-eabb-3cf5-81ff-d03282f0818b | -18.07746 | -57.22462 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1679f530-ef02-396e-bd85-85b03bbab93b | -18.07731 | -57.37082 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 451e92df-832e-37f9-9688-97473b7355a4 | -18.0771 | -57.22794 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| aa700d88-cb96-3231-bf29-94fa12c2ee38 | -18.07695 | -57.37405 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| ef3a66b0-24d8-3bec-bda3-f43c59d4497c | -18.07284 | -57.36368 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 7d4aa966-21e7-3fda-bd99-ab2b65f11daf | -18.07248 | -57.36692 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 778bb254-9a93-32a4-8bc7-7b3dc6fa410b | -18.07213 | -57.37016 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 6c481dc4-f04e-34f3-acd7-38705b7e35d5 | -18.07178 | -57.37339 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 283e767a-4f34-3e37-8cc2-e1dfdcf738e1 | -18.07142 | -57.37662 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c451fbe0-9d7a-3a9e-b6b5-bd08dc994a61 | -18.06731 | -57.36626 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| c4c27813-fac0-3fcd-92f2-91e8c1ff7a75 | -18.06664 | -57.22661 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d69ef48d-0ea5-3a65-a479-1d773bbc76c1 | -18.0666 | -57.37272 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| b385bd82-dbc6-3eaf-8c64-64c314f92fc3 | -18.06629 | -57.22992 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c1e2bdfa-45b7-3cb7-b71c-eb2ed9717d42 | -18.06625 | -57.37595 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 9174e49b-458b-3929-947c-6b1dc4417559 | -18.06213 | -57.36559 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 8cc91fc7-da2e-32db-b1b1-f8bbbd03d74a | -18.06106 | -57.22925 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| df00d313-7b0b-3266-8ac3-578238347831 | -17.70312 | -57.48384 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 48f789f9-a38f-3a06-b4ac-b051038846f1 | -17.70278 | -57.48698 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e0f249f7-6dec-35a1-aa16-3b9f2f98fdca | -17.69801 | -57.48317 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e4e8e0c8-a110-3312-9864-fd3cb7f9f965 | -17.69323 | -57.47937 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 84ad45b4-2cd8-365f-9831-5851dfb27102 | -17.69289 | -57.48251 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 48896443-a856-3a2e-8ef6-c40aaf19ae81 | -17.68812 | -57.47871 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fb0b1857-1790-3a3b-a762-03592fefe12c | -18.03454 | -57.32911 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 08eeee53-1bef-30d8-8b07-8c6708836132 | -17.68778 | -57.48185 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 70a6f80c-2e29-3c33-8aff-0a579151c579 | -17.68744 | -57.48498 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a7446158-179a-3a30-b908-17760122f848 | -17.68506 | -57.48037 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 39a86aab-4c3c-33b5-b75f-8d696f35eb43 | -17.6847 | -57.48349 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 71535ae8-04ea-32ad-bb76-9e894521cc5d | -17.68434 | -57.48663 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 5b4c910f-3342-3331-9ee7-ceabb8d7e4d9 | -17.68398 | -57.48976 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |


[Clique aqui para ver as próximas entradas](README98.md)
