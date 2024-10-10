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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd56f5f4-0110-362d-9eea-7a2aaf5d6f97 | -7.16816 | -46.17847 | 2024-10-10 04:44:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8f9050a-e959-36ac-aab2-3d65397470c8 | -7.16765 | -46.182 | 2024-10-10 04:44:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d794c5e8-1eb1-3cb9-8f07-63e433d18eb0 | -6.97345 | -46.25633 | 2024-10-10 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1137978a-9c6a-333c-8ec5-cfaa3e5c52d8 | -6.84184 | -46.22306 | 2024-10-10 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36229661-507b-34d0-9c57-86e1e7f20d46 | -6.83837 | -46.21894 | 2024-10-10 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1d999ac-3805-3c66-ad4f-b92b1c43f707 | -6.83787 | -46.22239 | 2024-10-10 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0acd1d78-352e-36a8-85ac-f0197a900228 | -6.7399 | -46.29164 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ef6c5c6-4475-3dd6-b278-587ada589984 | -6.73916 | -46.29671 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df187d98-bab2-31f3-934c-175e95461965 | -7.42447 | -45.61821 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17cce091-e99e-30f5-a66b-319c21060612 | -7.39715 | -46.14527 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b4f47b7-11b6-3df7-be65-671927a1c398 | -7.39159 | -46.15526 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36373a56-70ae-361c-8e7c-bf6f58a55da1 | -7.38908 | -46.144 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8ba9dab-a450-34d4-8416-a5759ecc68cb | -7.38051 | -46.14629 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60b2e27f-7709-3d2d-a362-65c53c27b489 | -7.37698 | -46.14215 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0d3504a-4da1-3180-9e8b-eacd947b6180 | -7.29815 | -45.53786 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbf60b71-60a3-386b-b816-7d65d9dad173 | -7.00782 | -45.36736 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 402617d1-dc8c-3a26-9c71-18947a3d16f0 | -6.98843 | -45.23096 | 2024-10-10 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 716b9fc0-f138-3f6a-be7f-f804aa9505ef | -6.98785 | -45.23499 | 2024-10-10 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c4c5723-72f0-30fa-b584-878cce7d20ec | -6.98386 | -45.38391 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d35964d0-b2d5-323a-abba-8caf45f3cdfb | -6.98359 | -45.23436 | 2024-10-10 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 214a8526-d599-3ed8-9630-c98b1920080d | -6.96278 | -45.64738 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b72f8fe8-6c0c-32db-a053-425807ab02cd | -6.9627 | -45.79166 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad65f40c-b49e-3828-aac8-b0dedd341bfd | -6.95912 | -45.28449 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e963d3ee-e4c3-30fe-bc13-ec79d48ff0bd | -6.95885 | -45.28905 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 053f1ee5-515a-30ea-a3da-1b0ebac2c8b2 | -6.95644 | -45.27611 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab5dfbe5-c365-340c-a0e5-eba53ba287c4 | -6.95545 | -45.27977 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c37fe823-35b7-3380-beb4-a09c381340ea | -6.95516 | -45.28467 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7222ddf8-d988-3dff-b7b9-7a9efd0d73a0 | -6.69885 | -45.38226 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 274fd22f-f269-3afa-833a-8ce949d90c04 | -7.74647 | -46.58612 | 2024-10-10 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92619541-f17a-367b-84e7-dfd2fb82aec7 | -7.5855 | -46.80444 | 2024-10-10 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7ea9b5b-7c60-30ee-bcde-1ecce48eb1d9 | -7.33597 | -46.73359 | 2024-10-10 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b2537a6-b726-3482-a209-36e21e212d38 | -7.82171 | -46.47996 | 2024-10-10 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18c2a17e-40d4-3862-b3f3-80666bd7bc9c | -7.58477 | -46.80933 | 2024-10-10 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cf8a2b0c-29e3-3dbb-a515-bb5ba3a1aa96 | -7.58088 | -46.80876 | 2024-10-10 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9153d887-61b0-381e-b843-e0e31c5527d8 | -7.44707 | -46.68704 | 2024-10-10 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 392a4ccb-0b45-3f40-9d52-cc413981c243 | -7.4239 | -45.62209 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03bc4df6-1e50-3fae-9948-3fd9d8db42c6 | -7.39765 | -46.14174 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e32c08f3-5895-3f35-b43e-70a225b2d7ca | -7.39413 | -46.13757 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af438d66-8fc8-35f3-baaf-c1489ee57a48 | -7.39362 | -46.1411 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8d531b0-ebc9-3ddf-a1a1-f71e5ecfce76 | -7.38756 | -46.15464 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1c2bd50-6e5c-3f89-b30a-60162491103b | -7.38455 | -46.14691 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65108756-982f-321a-876d-a7639aa685a9 | -7.38101 | -46.14277 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d18fa95b-15ad-3697-b181-8e766895b866 | -7.2987 | -45.53402 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ba19899-474c-38ca-bd07-853acebd4603 | -7.01698 | -45.45193 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b24dc4b4-a2e4-3f6b-b08d-fc559d0f1e6e | -7.01642 | -45.45577 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74fb269f-7c26-305a-8706-2a721c9cbb0c | -7.01221 | -45.45522 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45fc42cc-1ecd-3003-9e0a-f13abadd6ca8 | -7.00725 | -45.37129 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd609e9b-b9fa-3d8a-9e83-f18b07f99846 | -6.989 | -45.22691 | 2024-10-10 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7c483b0-9146-322a-b34b-f6540d503a72 | -6.97746 | -46.00232 | 2024-10-10 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e960480d-206e-3855-987c-511d1460fca5 | -6.9668 | -45.79225 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d647aa8f-cde7-30c4-b613-c76bcde4952b | -6.96284 | -45.28881 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13c5e451-0a45-3f96-bb52-0d65437d0fb0 | -6.95945 | -45.28502 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 712a6e27-f457-3452-8049-372521c18004 | -6.95864 | -45.64676 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5111d400-eb19-338a-892a-52462e5556df | -6.95854 | -45.28858 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13da5bab-df11-3277-aea5-54b94b49a7b0 | -6.95581 | -45.28035 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8cb7ef4c-c7ba-3766-bc05-d0739d2be554 | -6.95484 | -45.28411 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a63483ae-023c-3d3c-9b9e-2d97ab359c15 | -6.9509 | -45.28413 | 2024-10-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f53a680-6c01-3a92-9359-37410a4487e2 | -6.84234 | -46.2196 | 2024-10-10 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55c9ea4f-9633-37b8-a130-033048ecc592 | -6.81246 | -45.96406 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abfc88e2-7304-3459-8398-0bb48e3bc65f | -6.80149 | -46.47367 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba71a735-f83c-3d34-8b63-c96e10b302f3 | -6.79615 | -46.13049 | 2024-10-10 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bff530c-4f45-383b-9c60-b0611cdbf271 | -6.74312 | -46.29734 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b499b20a-635e-3af2-a4fc-8590d569ed06 | -6.69941 | -45.37844 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69ec5234-282a-3a8b-ad69-ded97a1278e9 | -6.66167 | -46.33612 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fedef44-a2d6-3272-8890-04d146c0d806 | -6.64899 | -46.03388 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c298e6f-a403-383f-bb0a-029201e76c03 | -6.64497 | -46.03329 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dfaa399-09ef-3e57-a002-94e2732583d5 | -6.59017 | -45.94957 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c3ed77a-f250-345b-8729-bfa8326670bd | -9.1432 | -46.39267 | 2024-10-10 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f1b84796-6671-3b26-a84e-e1b126c46c1e | -9.3225 | -45.74321 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aecf9d05-844d-38f4-8fea-2e3d043a2851 | -8.87413 | -45.86396 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 673c7f75-6678-31bc-9714-3420cd71ab42 | -9.1473 | -46.39306 | 2024-10-10 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| be6b9257-cb77-356d-9bbd-2402bcaf612a | -9.14679 | -46.39658 | 2024-10-10 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46d97612-9e39-3479-89d1-519badb9e8aa | -8.96104 | -46.04041 | 2024-10-10 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99e29b16-5a5e-3faa-a620-467d05af1d47 | -8.62272 | -46.4932 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0f94e18-d838-36a9-ac87-931dd6f812de | -8.6182 | -46.4962 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4500a676-9204-37e9-ad20-8f57b3a78ac1 | -8.39923 | -46.96619 | 2024-10-10 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdf08ea6-f3fd-35a2-9e9a-f4118b3cedd2 | -8.57961 | -45.77954 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39da0cbb-11c0-3a1f-ba47-4f9c8bf76e5e | -8.70473 | -47.0422 | 2024-10-10 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19b4d804-9975-31a6-a2d6-0dc40f26494a | -8.68317 | -47.10892 | 2024-10-10 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5af57a6-b2ed-3a62-a2af-4f7ccdddeeef | -8.61869 | -46.49266 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb4b4ff0-b3e8-3e8e-ab71-b456be0b852a | -8.47521 | -46.91421 | 2024-10-10 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbfee0c1-f956-30fd-87b6-05ef62807d49 | -8.24202 | -46.27771 | 2024-10-10 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a49c1990-e621-3e8f-b59d-42e2be46a17e | -10.27735 | -46.73788 | 2024-10-10 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a35ac8b9-cfc0-37fb-8f34-6b5280ad900c | -10.27332 | -46.73714 | 2024-10-10 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebdac0b0-10a4-331b-afee-34e69155caa0 | -10.27276 | -46.7411 | 2024-10-10 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0766cf66-4acc-3dc0-ab7a-35efa49cb592 | -10.26929 | -46.73647 | 2024-10-10 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 148f27f7-3464-3c0d-8138-02f99931887c | -10.26875 | -46.74027 | 2024-10-10 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ced33b05-53fa-3d6d-8888-bfb75048c2f1 | -10.26525 | -46.73583 | 2024-10-10 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f724adf2-fec3-39e9-8ee8-1d3d6996418c | -10.61197 | -47.30693 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82d2b5e5-f8c1-3971-aec7-ff52acfd8440 | -12.28237 | -46.78259 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bd6cee2-89f4-380a-b082-b72bbb319677 | -12.20421 | -46.72191 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 197cb582-bd1c-351c-8795-86ed9021cc6f | -12.20316 | -46.72958 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81386106-66e9-361f-83e0-b7387be753b3 | -12.20263 | -46.73341 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f137437d-c837-3270-8e1b-30cb787cc517 | -12.199 | -46.72901 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 621e73c9-80eb-30fd-8f2d-43ccd3786404 | -12.19847 | -46.73283 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 966fe170-c0b2-3faf-90eb-65b1d02d1a55 | -12.19483 | -46.72843 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fa6254d-938e-3262-9eed-da360bf6ccc6 | -11.67357 | -46.47459 | 2024-10-10 04:44:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6d7d51f-7f5d-38ae-a8fe-b81cf54fed7e | -12.20368 | -46.72575 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c1d21d2-10f1-30f3-b2fd-eb19430550cc | -12.19952 | -46.72517 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7fa2ab38-8d6b-3ae2-9684-8f8e9549ed37 | -12.19927 | -47.15027 | 2024-10-10 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README100.md)
