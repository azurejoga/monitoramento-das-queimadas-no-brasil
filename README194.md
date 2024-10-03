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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6ce4b64-eafb-3429-ab71-85d0e49b2929 | -11.67356 | -64.00098 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6aaab25-6dc5-3423-85d7-595b9c37c947 | -11.67394 | -63.99789 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e746c64-6293-3073-88ed-eab68cd223fe | -11.67853 | -64.04547 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93a7cedb-18f8-3d05-a017-c03130dbfd9e | -11.67891 | -64.04243 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f747e027-1a89-39ce-875e-209225afffe7 | -11.6886 | -64.04897 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2cfca098-c8bb-310c-80a0-e2e6843ce290 | -11.72036 | -64.27668 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ff59e16-c832-3ad4-8dd3-07c6e3815df7 | -12.01644 | -63.77945 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9039d8bd-df43-3cbf-af35-70fc2fa431dc | -12.01685 | -63.77606 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f23192db-64c5-3d53-b539-76cbba10d69d | -12.02173 | -63.78014 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1ea2e3e-4cdf-3431-a992-ee5dc00383c8 | -12.12607 | -64.74445 | 2024-10-03 06:10:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a6e79f5-4a08-3eb7-8ca4-8816e3670aff | -10.55544 | -64.48907 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 328716b6-cc70-351e-a6a0-f636d9d13929 | -10.55616 | -64.48353 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0da4dbc9-070a-31b5-806b-22322ae3f21d | -10.55959 | -64.49573 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9231ed41-d258-3fac-880d-9e8c1645caa9 | -10.57265 | -63.99619 | 2024-10-03 06:10:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1595d59e-9625-3b89-998c-e53c8202b049 | -10.57739 | -63.99981 | 2024-10-03 06:10:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 129cfd02-3aef-3051-a435-5d48365f0b78 | -10.60687 | -64.05353 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2ac5952-d933-3869-903f-3de8350669bb | -10.61151 | -64.05772 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4eb0eb4-dad7-3f72-9b02-0900b2d0e0b6 | -10.61191 | -64.05465 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1609085-bbb4-3d62-a06c-6c838eaf20aa | -10.61233 | -64.05135 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd54d36b-4224-3ba8-9f92-a92c41ecfc7f | -10.61362 | -64.51977 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 927e4e91-e4b5-37cd-9358-1861a706a01e | -10.617 | -64.05527 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef5a508c-54ff-357d-8224-cff456a69402 | -10.61743 | -64.05196 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53eb4885-a7f7-3edd-8f08-62fd80df36cb | -10.61796 | -64.35999 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 736358ce-6f58-3f84-9866-1acaabd9f0e4 | -10.6187 | -64.35999 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 822fb86b-2be9-3f03-8bd8-2a5583901a10 | -10.61922 | -64.51524 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6da9bfec-3095-320e-a18a-bb001071321c | -10.62913 | -64.51624 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 072a1c84-c925-3a79-a064-87f1f5a1d355 | -10.69051 | -64.15678 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d07a24b-1684-325c-b3e1-66cf67cc2df7 | -10.69089 | -64.15382 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21a08e65-045d-362e-bc03-55b0b6b56441 | -10.69553 | -64.15785 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a83e1db1-47d0-3402-8fe0-bafbf3f126f0 | -10.6959 | -64.15498 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63315627-540e-32ff-99a3-eb9332ce7f33 | -10.70091 | -64.15612 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 335e6671-07b6-3e04-9041-5214c4cda686 | -10.70165 | -64.15031 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da2f710f-c073-3f71-aa61-d0b2920f749f | -10.70667 | -64.15136 | 2024-10-03 06:10:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1363513-3537-3867-84ca-5e6170deb1a8 | -12.7372 | -62.90768 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0916627-ddfe-31f9-948c-9961f5efe5fe | -12.73765 | -62.90376 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 907da292-1921-3a31-a2e3-19b7d6a4c35e | -12.7381 | -62.89983 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c2c7cea-8639-3f33-a662-6d7c3c05a306 | -12.739 | -62.89197 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59f5e18b-9f90-3d72-b871-7a7ce4728bb3 | -12.73992 | -62.90666 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e8f29969-6ed4-397a-a0ef-31d19305b09c | -12.7404 | -62.90274 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9e68ca7c-b4bf-3ef4-b551-39aeefc2ea52 | -12.74088 | -62.89882 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4ea2116-932f-37ef-9d88-616c131189b8 | -12.74136 | -62.8949 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e5806a7-a876-3a81-8ddd-85c2c42e64c5 | -12.74184 | -62.89098 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b048cb8f-1af3-3112-84ed-663a352e1bde | -12.74195 | -62.91626 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2057d1b6-35e5-3269-86a8-3547b489dfe5 | -12.74232 | -62.88706 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 967edbda-7e89-3406-8b77-0be5230947fb | -12.7428 | -62.88313 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b2790e44-b06d-31e9-a6f7-773db07807c6 | -12.74286 | -62.90842 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc423884-2fc8-3182-9228-a750565724fa | -12.74328 | -62.8792 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b6f7bb5b-9338-337d-a2f9-9692a8678b67 | -12.74331 | -62.9045 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e87b1da-20b1-3c47-b8b9-11b1f8824bed | -12.74376 | -62.87526 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d9e463f1-0eac-38e6-a4c3-89afb231615e | -12.74376 | -62.90057 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 654d605e-ae72-3124-9277-22d251ac3029 | -12.74467 | -62.89271 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 96f9dd1b-a950-3a14-bdec-fe3152d076e8 | -12.74512 | -62.88879 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 994d45a4-1b00-36cc-9ef1-781f96d56848 | -12.74557 | -62.88485 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 88630830-33e3-31ef-8ef6-23bb291f4805 | -12.74603 | -62.88091 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d294fd9c-71fd-371c-bc3f-5a0699f43293 | -12.74648 | -62.87697 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ccc545ce-4ee1-39be-8ff2-fbf9d49b1373 | -12.7467 | -62.92485 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 536f4b50-8b04-3215-a990-d84c654f8635 | -12.74693 | -62.87302 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 879d4c05-5c14-3904-baf8-43935649061b | -12.74716 | -62.92093 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c13cf3c5-715c-3058-9d69-a7c4040b52bb | -12.75235 | -62.92561 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 995714c1-4684-3ef9-86c5-23e6e0696a40 | -12.7526 | -62.8738 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 144da2ea-bef7-3857-9665-30ed3eb7a496 | -12.758 | -62.9264 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e056c5db-764c-31ab-b3a7-44ba11431f8c | -12.75846 | -62.92247 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42090d25-a294-33ec-8e77-ab67e337e91e | -12.77588 | -62.92078 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83cd60d1-b123-3105-8a81-c2aac1a62ef8 | -12.77634 | -62.91686 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d0cefa5-fcef-38dc-8a48-ef9421c2729d | -12.78153 | -62.92151 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc6377bc-0bd9-3491-a5fa-96599e4bb646 | -12.8212 | -62.90083 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6874d9f-957e-33a3-a554-ff27f6563976 | -12.82165 | -62.89682 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2feaf9c6-716c-39f2-81f9-f2c90d93da15 | -12.38389 | -63.00397 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26267b87-1d51-3f23-9958-5167dc2246c0 | -12.38566 | -63.00242 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4380c195-da13-3dd6-96e3-a7d163036f6b | -12.3917 | -62.98555 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 09783b65-b716-3073-9c8a-0502d967a77b | -12.39267 | -62.99165 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0a09a4b-4d02-3ce3-86c7-7672210e753f | -12.39314 | -62.98786 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cbb5649-1238-3a90-b1ac-b6ba7c391bc4 | -12.3936 | -62.98408 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58f2bbe3-4a5a-3a0d-8b92-980ad13d8fdd | -12.39508 | -63.00544 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5bf32fe0-9c33-329d-9945-2404054b6320 | -12.39553 | -63.00158 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 752f443a-c279-3e82-a280-b57d87b3d4e6 | -12.39686 | -62.99012 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c636b21d-9f3d-3e1d-82f1-0207da53efb5 | -12.39686 | -63.00388 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dbe9ac63-3fae-35b6-b409-c4f0df82ad9f | -12.39729 | -62.98633 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 064c0df1-74f9-3cba-85ab-31647c70e122 | -12.39733 | -63.00002 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9ddea9f-be45-3676-9b21-7261b41a4c75 | -12.39874 | -62.98862 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8f966ed-1371-3524-aff3-12157ff19bd2 | -12.40113 | -63.00231 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9cd14132-fc4b-3ff3-9d20-5145c8b40ca7 | -12.40158 | -62.99846 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 61a718aa-2fe8-32c4-b5c7-be897ec6f391 | -12.40246 | -62.99088 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5eb3baa-0b80-3f8e-84fb-74630e6100ca | -12.40246 | -63.00458 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 45dd2fea-8e0c-39ab-9e03-51967fdc6614 | -12.40289 | -62.98711 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa8210aa-b664-3398-ad9d-f146581f06c2 | -12.40293 | -63.00074 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 1f5f8233-48ed-32d4-a3bd-7657d8ae1c85 | -12.4034 | -62.9969 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 7365dbd6-2ab0-3c35-9e59-23f5becfbf8f | -12.40387 | -62.99313 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 996b162f-64a9-3823-ab4c-cd14df0f0d16 | -12.40434 | -62.98937 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 6805e357-01f1-3b54-8ac8-87142d767aaf | -12.4048 | -62.9856 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a60adc3-ad60-33a8-968c-f3a62ae1d235 | -12.40673 | -63.00304 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 452fa6e4-0620-3614-8716-3566b86d35d6 | -12.40718 | -62.99921 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| cb398b35-0291-3b29-b472-063312eeabe5 | -12.40762 | -62.99539 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 794d2718-a886-3e87-a05e-cf8218a448a1 | -12.40805 | -63.00529 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b7f0a364-35e7-37bf-b234-d47b9ed78502 | -12.40806 | -62.99162 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 0ac6275b-0571-31e7-854a-a3b6ecfafd2e | -12.4085 | -62.98786 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 3cd8048e-35cc-3a8b-801a-c139286929cf | -12.40853 | -63.00147 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 2df468e9-8764-33ea-835f-d2cafd06fa0e | -12.409 | -62.99764 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| dfe961ec-4594-34db-bd33-41dc789be9f5 | -12.40947 | -62.99385 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 6813b78c-52b2-38b1-85df-1f74d758526b | -12.40994 | -62.9901 | 2024-10-03 06:10:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |


[Clique aqui para ver as próximas entradas](README195.md)
