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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50070f1f-b815-3991-a808-f71d602b5a84 | -7.41339 | -46.15512 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dc6ad0b-a316-37a9-a95b-463cfdf77851 | -5.42637 | -45.47655 | 2024-10-15 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f63a9f89-bf59-3de1-a25b-35808e084521 | -5.4225 | -45.47951 | 2024-10-15 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c47b18e9-9e83-342a-abaa-8f3d1584e9f7 | -5.27793 | -46.37629 | 2024-10-15 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 760dadf3-5816-36dd-9174-c0ac63833181 | -5.27738 | -46.37976 | 2024-10-15 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d99c42c-eed0-3501-a1d7-389cac03e66b | -6.8788 | -45.46314 | 2024-10-15 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ad77c95-7695-3a75-99b6-70e6a11265e3 | -6.87826 | -45.46666 | 2024-10-15 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b72306be-9034-329c-ac08-6046975c0df1 | -6.87157 | -45.46568 | 2024-10-15 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b95e5da8-af6c-340c-9250-6fe6aaf2e979 | -6.87102 | -45.4692 | 2024-10-15 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83865175-2e58-39bb-b20a-794d10808ab7 | -6.86822 | -45.46518 | 2024-10-15 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fd5930c-d391-37c8-88a4-1e0c29fb1def | -6.79555 | -46.55238 | 2024-10-15 04:25:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06693e86-fcba-3557-9246-6dbdd42a26c1 | -6.50824 | -46.55312 | 2024-10-15 04:25:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 556939a6-06e6-3ecd-93d6-fe4d42498f41 | -7.98462 | -45.46469 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d1e0483-86d3-38a5-96b5-7d28fabcdade | -7.98181 | -45.46064 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b15d3973-4259-32a5-b637-6c6be5ea972b | -7.97846 | -45.46011 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03dfa83c-8c2f-3e75-8fc5-18db8e61eeea | -7.97737 | -45.46715 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 964afb40-7c51-3d7e-a1c7-35ae20b4c669 | -7.97401 | -45.46666 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d38a795a-13b9-3ff7-be75-fcd19d7dd40c | -7.9126 | -45.66384 | 2024-10-15 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcac9627-7299-36dd-b155-0d094a2fdea2 | -7.90592 | -45.66276 | 2024-10-15 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebfe7dac-458e-3467-ba7c-8cc6b9d21627 | -7.12787 | -45.42989 | 2024-10-15 04:25:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d439ff9-7442-3808-a435-645fe3458440 | -7.12547 | -45.35714 | 2024-10-15 04:25:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29aad39c-4f22-38c5-a430-764ef791e70c | -7.69995 | -46.63474 | 2024-10-15 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ff1eb07-29cf-3704-a30d-45eb272d12a2 | -7.61482 | -46.89275 | 2024-10-15 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4700f0b7-6f1d-3e42-9488-b3799caf03c8 | -7.60025 | -46.7976 | 2024-10-15 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3891a72-3160-3fc8-8102-e33ea088551f | -7.45852 | -45.82288 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5cae4d72-5439-3692-8dd9-878bc1b3fdc7 | -7.41393 | -46.15165 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ab610bf-4def-3659-9f18-2c686fdbcda2 | -9.43797 | -46.01337 | 2024-10-15 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c4c7dbf-465d-32de-bd4a-90e77c8dd26a | -8.72808 | -46.63409 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19adb88b-cfc0-3253-a64b-e29d2708f6b8 | -8.72753 | -46.63758 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5524ca30-cb16-33e0-bdf1-68558b55c6ad | -8.72476 | -46.63356 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 051c0a41-e59c-3336-a341-9766be042b6f | -8.72421 | -46.63705 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cec8773a-9ba1-350e-ad4a-831c1d6d5184 | -8.69919 | -46.65057 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8b3bf08-a307-3581-bbff-fa82ecb8f991 | -8.46832 | -46.46066 | 2024-10-15 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4c2b09d-6372-3a65-bcde-9ae363dd5021 | -8.37918 | -46.91803 | 2024-10-15 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df0347b3-c194-3cf1-bde2-701306ef948e | -8.37586 | -46.9175 | 2024-10-15 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a7b8833-7cb6-3e69-9895-0548dbd27c11 | -8.31493 | -46.87564 | 2024-10-15 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2e18e36-0f66-3bdc-bd00-612ec07a911e | -8.31271 | -46.86812 | 2024-10-15 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f797e73d-df93-3b3a-a454-5ead199976d4 | -8.21494 | -46.80275 | 2024-10-15 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bd69496-959c-3999-9c90-4efea57c1f3a | -8.19178 | -46.9493 | 2024-10-15 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b209f5d-b56d-3e2e-a36f-76fb6980b614 | -8.05285 | -46.63041 | 2024-10-15 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76df2830-7842-3b39-bd6a-6ceb66a8ddd4 | -7.99219 | -46.86365 | 2024-10-15 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f28cd50b-dfff-35b3-bc83-f63f45fbef72 | -10.40559 | -47.36836 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0af4bc8-bae1-3f84-a14e-b4fc71d388f4 | -10.25974 | -47.28389 | 2024-10-15 04:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48b6f089-3523-3fd7-bfea-cc1b2c5ed0b0 | -10.25697 | -47.27984 | 2024-10-15 04:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4699e344-b936-3fb3-8173-3271b669a5b6 | -9.96725 | -47.25096 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db52b5ba-d67a-33d5-bee9-6837a675ce8b | -9.96337 | -47.25393 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e64cddd6-706a-34fb-9da7-8208789ea1d5 | -9.9606 | -47.24989 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d98b261-d0f2-3a5a-bd36-fcef58589830 | -9.96004 | -47.2534 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c086ab6-ce0c-351b-9a79-d355fe21152d | -9.92678 | -47.26961 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c6715c42-3562-37a8-8df1-3ce3b10c6334 | -9.92623 | -47.27311 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0647773a-c449-3499-9996-11b885d5c513 | -9.91624 | -47.29308 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 387f8e27-43f8-3d8d-8ddf-ebb96e048eb9 | -9.91291 | -47.29255 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e9110b4-e1fe-3162-9854-0122c0f87469 | -9.91236 | -47.29605 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0ad329f-a128-3f00-bb31-474cdeab44d9 | -9.90959 | -47.29201 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ccc82030-8acc-3727-9b4c-054de67f0da8 | -9.71864 | -46.94244 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53b6eeb1-4d7d-3506-ab8f-cb8f177a5e96 | -9.71476 | -46.94541 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 488f3d78-95c1-3b38-946f-cfd4ffc2238f | -9.68938 | -47.14938 | 2024-10-15 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 768c13b6-6772-3c29-9bc4-bf9787484a4f | -9.6893 | -46.48177 | 2024-10-15 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d121a8c-9be0-34d7-b397-8ad3c6ca7490 | -9.67542 | -46.91401 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5d52fb0-8ce5-3652-8404-36a3ef149124 | -9.67374 | -46.90298 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7907a3dd-7e6a-3e1a-abe1-cc6b847e87c7 | -9.67209 | -46.91348 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37201868-cc7a-3559-bc60-a365cbb97a34 | -9.67154 | -46.91698 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c97f5409-31b0-3a2a-b05c-9f2bf6d6dfae | -9.66932 | -46.90945 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea8797c7-d321-3030-b5f3-f5337a2f3168 | -9.60424 | -46.63334 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 259dd05f-4fc7-3a27-b05f-af784bb22f4a | -9.41948 | -46.56136 | 2024-10-15 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 618e0e26-09d3-3811-93af-71104d05a16a | -9.40169 | -46.93461 | 2024-10-15 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9658f6c1-4482-3155-b80d-86e2abaac50e | -12.18847 | -46.75782 | 2024-10-15 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 887bb4f5-8920-3fe9-8378-92c7fa01581e | -12.18513 | -46.75729 | 2024-10-15 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 438caf42-e853-383e-9f5d-b2cf54d83764 | -5.60624 | -47.95982 | 2024-10-15 04:25:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03fad678-2fc7-348d-8f7e-abf1fa7090f9 | -5.60279 | -47.95927 | 2024-10-15 04:25:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9da0f67-0239-385a-a9d1-6d0036cba83b | -6.27464 | -46.99652 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9ea42b6-0396-32cd-b195-084ea4d843de | -6.07633 | -47.05511 | 2024-10-15 04:25:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87222ec8-30b4-3d99-9b4e-68e554083a60 | -6.07576 | -47.05865 | 2024-10-15 04:25:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03178c3f-97b9-38c3-ba49-1fc481bc250d | -6.05117 | -46.59829 | 2024-10-15 04:25:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4178196e-4844-34e6-b4af-0cb71272b988 | -6.04396 | -46.60072 | 2024-10-15 04:25:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 369a3468-8b3f-39d2-9ba2-7a5c079f1d00 | -5.94579 | -47.63029 | 2024-10-15 04:25:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf313885-2eb9-3e73-8153-9e2132b02572 | -5.85622 | -47.62336 | 2024-10-15 04:25:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee3bfb6b-75c9-38b9-b711-1f47123e5741 | -7.09761 | -48.33185 | 2024-10-15 04:25:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16db104b-91de-37a4-8523-2b39ad1483d5 | -7.09417 | -48.33129 | 2024-10-15 04:25:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49ceeb3f-4c6d-3459-a4b0-e4ed4d3beee0 | -7.01282 | -48.20634 | 2024-10-15 04:25:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af40691a-5d28-3e6f-8ad8-a9af8fc56d88 | -6.98265 | -47.33317 | 2024-10-15 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 920c6ed0-7c49-3434-8010-3478e7c0b204 | -6.97708 | -47.32503 | 2024-10-15 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 78b0723e-cffa-33a2-86c8-55abd978d41b | -6.86324 | -48.00799 | 2024-10-15 04:25:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7961fd4f-9106-3db9-811b-292407d9919c | -8.00769 | -47.21035 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1aea5737-32fc-30d6-ba9d-75656ec0dbcb | -7.91077 | -47.83705 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c387932a-f341-3d72-9d25-d70ec7d215ba | -7.87877 | -47.75107 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bbc934a8-8ca5-321a-9d6e-2e5d4ae9637d | -7.87597 | -47.74693 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a2646e3-c0ef-34b5-add3-0080667f870a | -7.8754 | -47.75053 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fcfd3055-a794-3eb8-ae31-1abdaf6dd9c5 | -7.8726 | -47.7464 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d12fff5-1d8a-37aa-b3eb-dfc23364d2b0 | -7.87202 | -47.75 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2fba7d0-c2c3-3f6b-a3f7-a202ae73ee39 | -7.86865 | -47.74945 | 2024-10-15 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a486bf91-f95e-3138-b11d-10be065c6482 | -7.53767 | -46.89139 | 2024-10-15 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6a26175-a1eb-3c2a-b8dc-9a78da2b3848 | -7.49584 | -48.09266 | 2024-10-15 04:25:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85e998b1-c62a-3414-ae62-98a206a1f5c6 | -9.20654 | -48.66179 | 2024-10-15 04:25:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3990fd05-baa7-3204-a6b6-66050a644848 | -3.1283 | -54.2259 | 2024-10-15 04:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 67a03509-cfd1-3891-a7a3-f079805725d8 | -3.9267 | -42.401 | 2024-10-15 04:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 181.6 |
| 21b6202f-8ce1-3ae2-9300-3adb7242e64a | -3.9265 | -42.4246 | 2024-10-15 04:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| ad59bdf8-9b6e-390a-8375-8b8e00bc21ff | -3.908 | -42.402 | 2024-10-15 04:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| a7572d3a-aec1-3e39-87e7-cbb1b6897bdb | -3.9289 | -48.3458 | 2024-10-15 04:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c64ab74e-041a-3e14-9615-4f4491ef7d2b | -6.5691 | -48.2395 | 2024-10-15 04:25:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 83.6 |


[Clique aqui para ver as próximas entradas](README51.md)
