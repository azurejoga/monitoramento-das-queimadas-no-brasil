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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba12449-bde4-35b3-8b09-18a2bc69d683 | -3.09444 | -54.29198 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6f9eef41-2488-34cc-a5a0-9c596d70e9d1 | -2.4981 | -48.13799 | 2026-10-07 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50952e24-d540-3805-8ce6-fc51653247d2 | -2.99013 | -54.0425 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76716bb8-2ea4-3c0e-9170-e86a5751ff19 | -3.04345 | -54.22687 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f8e51b5-981c-37a6-b5b5-0a94b0086e2b | -2.49816 | -58.06737 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abc0e12e-9e46-30f9-a5bc-55839de090fb | -3.00433 | -54.12755 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7fa6594-9f3b-3784-9ce9-160ae6d4c1fe | -5.96704 | -55.35779 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a696066-1378-39ce-a3f2-2a6b85f719a9 | -2.98905 | -54.04955 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d9c0d78-c9de-3187-9b41-f552538d6642 | -7.18462 | -52.61213 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1d6bba6-34ad-3cfd-93ff-3b8eb6ceaac2 | -1.96466 | -56.10163 | 2026-10-07 05:04:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28e6b887-efff-37d1-a035-cbb2b73acb39 | -3.02494 | -54.14864 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59538cb8-ccfd-3205-9ffa-7307db643629 | -2.57351 | -56.14641 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab817ba6-f338-3b14-a09d-020703389566 | -3.54127 | -59.48901 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43af248d-7faf-3b3b-a94b-695929a0450c | -1.46484 | -54.77268 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a31c8d2-fbf4-339b-8897-52f8674a9b42 | -2.76508 | -54.09046 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| cd279ecc-34c9-302d-ae5a-0b462f192d86 | -3.05771 | -54.15732 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28cb9d72-5ba9-3acb-9d2c-008649165057 | -2.30688 | -57.08006 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e0b9e2f-d9f1-32fc-8de0-4f1d9584da0f | -5.67974 | -53.49687 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c527fa3-ae0d-3cd4-9f52-6f910a29c5c8 | -3.09716 | -53.72768 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abb06470-6df4-3511-874f-9e371d48a9bf | 0.66731 | -59.56392 | 2026-10-07 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6b8698f-9886-3b55-bd0f-e3e9aaea1b87 | -4.35894 | -47.78025 | 2026-10-07 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7e886eed-fd71-3c83-a55a-16be45c087bf | -2.98992 | -51.05135 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ce6ca3e7-d3fc-3d0e-94ed-cb173a329135 | -2.38927 | -56.12815 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4827de2d-50c9-3be8-956c-095be215b120 | -3.17998 | -50.55084 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9ee3bfa1-1375-3bc3-a4dd-6f2c513efabb | -1.09984 | -54.12098 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cd4cb1c-6339-379f-8bc7-d3b5ef190317 | -2.99929 | -54.11598 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9348499f-340c-368e-aebd-d30067c29525 | -8.70769 | -45.20975 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ca578ea2-22c3-3ede-a44f-9d0ebc03f366 | -3.50357 | -54.65831 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b6d440e-47db-3ca4-92fb-26cc2792424a | -3.02362 | -53.89186 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4690d265-9cb5-3c88-82cf-de25c0c32fa5 | -3.13196 | -53.70361 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57166821-38cf-351b-8cab-69a894733e50 | -2.95944 | -51.04667 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24e4b862-fd3c-3c35-8467-897027020732 | -1.18848 | -54.14174 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9296abfb-6e87-3b4b-8997-38903346cd5f | -3.66917 | -60.62077 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b43fd20-1437-3a41-a20d-46208edecb5c | -4.79756 | -55.72431 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d85b1c8b-bff0-3f16-a381-5162b861a3c3 | -3.86406 | -55.98919 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b63b0f9f-da39-309c-b06a-a24674ddb19a | -2.77895 | -54.089 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c49d80c2-8219-34e2-8376-4cead5b7c63f | -2.00017 | -56.95348 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2ee29ea-f893-38e7-bf33-2d98ac2e8719 | -2.1342 | -54.80025 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 070db641-a8ec-321b-b19b-650c272abedc | -1.09869 | -54.10667 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94d50123-a1e1-3999-a123-ee6e27d4c782 | -2.57981 | -57.15268 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05eb4592-2933-31a8-9849-b6d11275b265 | -3.53052 | -54.63767 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f5a41fe-8d47-3ad2-abf1-ef4af4383de9 | -2.99983 | -54.11246 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62877077-16fd-3c29-9bda-bf441de1e651 | -3.12883 | -53.75806 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 894eecf7-c6fb-317e-a444-a97f11529e0a | -5.95542 | -55.34538 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 890fac33-d1b1-3168-bdfb-5d66cb5bf82d | -2.93966 | -54.15012 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4d31eede-89ea-3ff7-9087-9a6d818259b0 | -3.49511 | -50.10275 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba47c834-1f29-3ea7-ac0e-92ef00f5245c | -3.70036 | -58.28803 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84fc65b4-188c-3855-ba69-199d7136ec0a | -2.99373 | -51.05192 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b1c50705-ebf7-3e45-9ab8-41d481348ad5 | -2.48834 | -49.41542 | 2026-10-07 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30e522a3-2739-37b4-9926-69598f56d6c3 | -3.11292 | -53.78146 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a4695f88-4320-3819-b5b7-d56f6904604c | -5.96257 | -55.34291 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27226d73-b8ff-3ce4-8322-8a4f6c95f8cb | -3.34977 | -59.49694 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32db6a88-c5b6-35d4-ab50-e8ec8a3b6bcc | -2.56853 | -56.15638 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1afcc2d6-4ffc-3782-8ba1-08ede154d9e6 | -2.78537 | -51.66987 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a0836182-6149-380c-a6a7-0a97e3cc3dac | -6.65406 | -47.91226 | 2026-10-07 05:04:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e60b18a3-22f3-370c-a8e9-c85aecd558d7 | -8.2498 | -47.98652 | 2026-10-07 05:04:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9251df38-760b-3769-9635-25c73cff1298 | -3.0576 | -54.22189 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 112125e5-57f6-3372-8e2f-7ecd28cbe00e | -2.99045 | -54.129 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fb40b18-66ab-3e09-ad30-2d7cc15c7396 | -3.12466 | -53.70617 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3169181-a196-3622-978b-a46c94e98053 | -5.9665 | -55.36125 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a3842ab-6f8a-31cf-84c6-1d8491fe8ea8 | -3.17629 | -50.4433 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb4aa1fd-e7f6-3712-ba38-870cc10ab3a0 | -3.47904 | -59.46695 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab9f35dd-47fd-36c6-93e7-1619236ae3d1 | -4.75873 | -55.66543 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afc51483-3f9c-3608-8e4b-b2f8333099d8 | -3.63124 | -54.6034 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e62c1cd-0bb0-3001-a122-07457de23504 | -3.59409 | -54.55853 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae35dd14-4144-33dd-a465-08460c851524 | -3.03654 | -53.91929 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bacf78be-5f42-36be-97e0-441cae193ef4 | -5.95489 | -55.34884 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18b4a69e-f30f-3602-91cc-34ff261e4241 | -3.85853 | -55.98126 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88697a2b-4367-3cf3-ac73-6e76749b5010 | -4.0779 | -54.8824 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb6b0b82-f62b-3330-aed5-fa1af8e12895 | -3.08384 | -54.27246 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7da915be-d1c5-3ffb-9920-eda3db56272e | -3.96934 | -56.12313 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0845cc90-da81-3262-854d-a4bc0551bb58 | -3.64516 | -51.75613 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be469c13-23d8-3e9a-b574-6afcce291568 | -2.49217 | -56.05809 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d54bbe3-f98f-3892-b45b-937ec302acff | -3.98442 | -56.22139 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f5c3d8d-90a8-3ce0-8f0f-11d263ee5662 | -3.03544 | -53.92639 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 372a2ab5-16aa-36c5-900d-dfe0716ba7e3 | -3.49564 | -50.09916 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00b80f29-f41f-3365-b784-310d46a15583 | -4.76087 | -55.65169 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f0f2b95-846b-3b98-990b-997b37abbcc0 | -3.06146 | -54.21891 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c57758e4-8c61-3066-9957-6fde3eb50d05 | -2.98796 | -54.0566 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b6284d4-8b94-3cff-b0cc-f1d37f9e5557 | -3.1101 | -54.16896 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 54b46978-ebed-3246-9540-b320ee569241 | -3.05657 | -54.14276 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f1b9948-b90d-3428-92c9-fe5a5dad6a4d | -3.98828 | -56.21843 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4007def3-928c-35d8-b027-641a24c87868 | -3.23144 | -54.37406 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31b815fe-b351-35fe-ab08-31e1ea44417e | -4.11263 | -50.80869 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47bbd437-29ea-3dba-b086-371442525c60 | -3.04514 | -54.23787 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbd6b8ee-eab0-380c-8efb-a8ede5ed67be | -6.83572 | -52.19598 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc4e446c-a094-3dee-97cc-5f7f8b37aece | -8.71004 | -45.19109 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b2653e4d-dda1-376e-8934-9e6026c32707 | -2.82681 | -54.13226 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78cee9f6-f976-3019-8d1a-35044a92ff87 | -4.13914 | -50.44727 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16b6025a-e502-3cdc-a4df-4d5cb154455e | -3.51673 | -54.6391 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8631c2c0-6984-3e02-9912-d427ef1e2ca3 | -3.28004 | -54.0621 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 98570d09-3b4a-358e-841f-f9887ee3dcfc | -3.48803 | -50.0942 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 436b8a13-33f3-3d0f-8f38-0072f8e4bd09 | -3.18954 | -50.56417 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 86d2c60a-4f44-31c6-9ae9-4f7be57a8012 | -2.99378 | -54.12951 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3932a289-e803-3741-acee-089c18e61900 | -3.57373 | -50.35858 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61623b79-8d9d-3ea5-8af7-7c609f30156a | -4.7557 | -45.76614 | 2026-10-07 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56430abc-7b21-351f-a4c2-5c2bc268ce64 | -3.09993 | -54.27853 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d2ab03e9-6290-3b4a-988f-d7eee288cc0f | -6.83704 | -52.19464 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d66a495-1008-3c20-9b45-8f5108fd3d42 | -6.01136 | -53.50613 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4293b80f-73df-3345-bbd6-03fec6835600 | -3.26908 | -50.41197 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README92.md)
