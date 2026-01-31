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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ee93ad9-1395-36f1-a0ca-d8ad4d78fa18 | -1.80052 | -54.48363 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7332d10-cb6d-3e4f-b53b-a9d86ea15129 | -1.80555 | -54.49536 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97979d81-ae4f-3d1e-bb62-decbdaee8c28 | -1.80275 | -54.49127 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 905019af-7a22-350d-99c6-b028946ce2fb | -2.81864 | -52.95779 | 2026-01-31 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1f5f1ba3-94ab-371a-9aef-11200176f1f0 | -1.80612 | -54.4918 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a10b4c2c-5a6f-39c6-86bb-600d148fc6d3 | -1.51876 | -53.96965 | 2026-01-31 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61bb57f5-3c63-302a-852e-9c813f7722c7 | -3.63614 | -51.94075 | 2026-01-31 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7dd3094-6d3a-33c3-b472-be80e57a788b | -1.80218 | -54.49483 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a6138ea-46c3-3f90-83ee-e84c2e83780c | -1.79995 | -54.48718 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e75011c-720e-34b6-a214-bdbb6ffbc8b6 | -2.82198 | -52.9583 | 2026-01-31 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6d259adb-6577-394a-abdf-f22d9d925987 | -1.80669 | -54.48824 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3cf993f-9d7a-398b-b390-e62cc978a011 | -3.26662 | -42.54427 | 2026-01-31 05:01:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54c4137a-66f8-36eb-aaa0-be4cdbf0cdc8 | -1.79938 | -54.49073 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b83cc37d-d19a-3be2-b16f-5696fa3f30ac | -1.8168 | -54.48983 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9597f240-45f7-3932-ba7b-148e55835e14 | -2.90105 | -49.37846 | 2026-01-31 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f848379-1c4d-3cef-96fe-09e7ac9db44e | -1.80949 | -54.49233 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80ab6c06-6523-33d1-99d1-d7cf37b5195b | -1.80726 | -54.48469 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 266ac794-d784-36a5-a865-845f9756deaa | -3.63214 | -51.9439 | 2026-01-31 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bef5904f-77ff-39ec-bfa8-f42ca5d599f3 | -2.58013 | -54.72142 | 2026-01-31 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee375734-538b-382d-a404-15f526e86bd1 | -1.84574 | -54.10438 | 2026-01-31 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e21fdf7e-331d-3544-a4d2-36f56c0f3c46 | -2.72537 | -49.78901 | 2026-01-31 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f603aac8-5efa-3de0-8951-615bd07aa450 | -3.63557 | -51.94442 | 2026-01-31 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 162076c3-0409-3819-aace-53960dbb12e5 | -1.81006 | -54.48877 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bae8c88d-1fcc-3f83-a64b-53bf476ea7f4 | -1.41967 | -45.65553 | 2026-01-31 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c73f3ea5-ef63-3372-936b-615cd78a896c | -1.81343 | -54.4893 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08250be5-15a5-38e2-9ade-475e1fc8d841 | -1.81286 | -54.49286 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf6b85c3-e7cb-302b-8d6a-b97afc6a587f | -1.80389 | -54.48416 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a10944cd-679c-35ef-b839-7f474041d584 | -1.80332 | -54.48772 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2efb2bf-8b13-32b1-90b2-77bab423e80b | -1.81063 | -54.48522 | 2026-01-31 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 232f3bbd-8e6f-356f-9a34-1868bd3218aa | -1.8463 | -54.10087 | 2026-01-31 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a7bcb12-d3d9-3e83-972a-5ce9bc9a7a3e | -8.87462 | -47.97238 | 2026-01-31 05:03:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19b69399-4116-3c2f-83b1-a1e536c2c6d8 | -8.10489 | -55.00994 | 2026-01-31 05:03:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 574ab519-8657-39b4-8136-d3074b8dff59 | -8.87921 | -47.97312 | 2026-01-31 05:03:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85ec9286-b0b1-3585-809a-6fdf8773d65e | -7.83627 | -42.05758 | 2026-01-31 05:03:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8d6df9c2-d4d3-36f2-9073-c8e9f5ad36ee | -3.85809 | -54.07931 | 2026-01-31 05:03:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73a9a953-e4e0-35b0-9ae7-450f0b683192 | -4.37037 | -55.77016 | 2026-01-31 05:03:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 929779d5-9f7f-3648-a81a-9698f570157c | -7.82956 | -42.05682 | 2026-01-31 05:03:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 67815fcc-97e3-3290-8f70-448d4fd5f932 | -4.97191 | -50.91104 | 2026-01-31 05:03:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e4cf7f4-072c-3cf9-88e4-6f66084222c4 | -8.08781 | -48.20008 | 2026-01-31 05:03:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 197ce33a-bfea-3ba0-b5d8-868baa779737 | -4.58916 | -47.54129 | 2026-01-31 05:03:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 896516ea-0c4d-3ecf-b75e-05837eb04642 | -5.73103 | -47.92534 | 2026-01-31 05:03:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0c1dad2-51ec-3c02-bcc0-aefac7649d6b | -8.4317 | -48.04361 | 2026-01-31 05:03:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f456c12e-a3e4-36f4-9365-ef48b6449181 | -16.57865 | -57.80564 | 2026-01-31 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| c2cf0b43-7a57-3376-98d3-cb8c3f1f6bb0 | -15.79346 | -59.68458 | 2026-01-31 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6800814e-07db-39e7-b4cd-4f79f8f762b0 | -11.97589 | -50.76117 | 2026-01-31 05:05:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e04ea722-ba03-3db5-8b3b-ce45d7abd2bf | -10.32293 | -59.05571 | 2026-01-31 05:05:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8a09af3-fcd5-386b-a92d-7f4e4ffb3d3c | -10.72049 | -59.22733 | 2026-01-31 05:05:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94f5d608-40bb-30e9-9409-846a647b46ea | -10.72127 | -59.22277 | 2026-01-31 05:05:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68cb8841-2da1-3ff6-bed5-1bacbaf55889 | -16.58875 | -57.80741 | 2026-01-31 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 3550478c-7c58-3d2c-96c4-2a1b4f9f911b | -12.29727 | -57.40507 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1c9d47a-1f7d-3338-8dd3-4346fddabc56 | -10.7175 | -59.22211 | 2026-01-31 05:05:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90c28fcb-31b2-3c4d-82aa-9b97b97e6fbe | -12.30809 | -57.3608 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abbe23b5-7e6e-3304-839e-bd3faad38186 | -16.43482 | -57.27005 | 2026-01-31 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 08bf65b9-3975-31b9-bc78-0803d37e2567 | -11.97115 | -50.7658 | 2026-01-31 05:05:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49e96c0b-38b5-3e16-924f-3106ed8617e8 | -11.95306 | -58.74054 | 2026-01-31 05:05:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f35e176d-121d-3358-94e3-ebbb2c3fdd88 | -12.29789 | -57.40131 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae91c9e2-f878-3bbf-8c6d-7439f97a7d09 | -16.58202 | -57.80623 | 2026-01-31 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 2af47b41-4259-3336-9333-c2eff669c84f | -12.28889 | -57.39207 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1365433-e5ce-3296-a762-5edd0c9a22c5 | -11.97402 | -50.76133 | 2026-01-31 05:05:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ceecc6b-ddb2-3567-a554-41c6c711241b | -11.97189 | -50.76059 | 2026-01-31 05:05:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff51a32d-9d8d-3f5f-b7b9-a5a43369f4e2 | -12.30747 | -57.36454 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e61465c-b0ad-3e43-8cc3-565e0e29600b | -11.96716 | -50.76522 | 2026-01-31 05:05:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a83a7b5d-b052-30c5-a67e-72fe98eead5d | -11.9679 | -50.76001 | 2026-01-31 05:05:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c156f893-fc0e-3c67-be4a-72865536503b | -15.02981 | -59.67339 | 2026-01-31 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9a190aa-88d6-3cca-8f23-2cdfe4cd5380 | -16.58538 | -57.80682 | 2026-01-31 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 4fd15f6c-22ba-300d-8ad0-e0d4447bdd51 | -11.17826 | -55.92028 | 2026-01-31 05:05:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac4e96d6-8776-3555-9677-03e7950f7215 | -12.30344 | -57.36768 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41646eb6-37b1-3c8f-b6a4-ed65c1058649 | -15.02651 | -59.67494 | 2026-01-31 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dfe92e1-cdf1-389b-b1cf-f30ffdf434f4 | -11.9704 | -50.77101 | 2026-01-31 05:05:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 855e4c1e-18e7-38e4-b9b0-8d923f20bac5 | -16.58262 | -57.80252 | 2026-01-31 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fbd44cb9-8053-348a-ab5d-1c0f34077a7a | -12.30467 | -57.36023 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 014e07d7-db14-3ee9-b658-4c69dafd9f16 | -16.58599 | -57.80311 | 2026-01-31 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a6774859-3826-3457-b376-36a68073fea3 | -12.43705 | -58.03728 | 2026-01-31 05:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fdc34e0-bf1d-3a23-abf3-17a9fc195a79 | -12.29942 | -57.37084 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7786cb7a-4ad8-303d-843b-3c185041d9f2 | -15.03016 | -59.6756 | 2026-01-31 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56f48924-8db7-385a-b957-a596e3f1baff | -12.29353 | -57.38519 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac453280-b24f-3b3b-bc06-f2460eb3d04e | -12.30406 | -57.36395 | 2026-01-31 05:05:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e2ff370-0888-3deb-88e0-519215336544 | -20.29489 | -57.369 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1ac494f3-545f-3dd0-818f-df7d2a7b7b7d | -20.30765 | -57.37505 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 27b14ae3-524a-3c32-8b94-3649b01ba804 | -20.3133 | -57.36086 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 55fe453d-6e3a-3d65-9a9b-2fc446d5ea26 | -20.30605 | -57.36338 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| aa84fa9e-c4f2-3d6f-ab72-9c3e108696d8 | -20.29213 | -57.36472 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f56af89-52dc-38af-ae5f-f432821a226a | -19.47405 | -55.46876 | 2026-01-31 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a7159158-1976-3d20-abb1-82884b4b89b4 | -20.31272 | -57.36455 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0f1f3e85-b2ad-338f-ade6-78f9384cc904 | -20.30547 | -57.36707 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1caa1d3a-5f5f-3d0d-b1d5-ec921c26fc1b | -20.28938 | -57.36044 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a901357-9abe-3802-aa60-2c4f7ae106c3 | -20.30387 | -57.3554 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2cd2850f-f706-3215-99f9-4d5c98199b32 | -19.43077 | -54.12768 | 2026-01-31 05:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8758be8-dee7-3b06-a575-7f61df94886e | -17.98174 | -53.69973 | 2026-01-31 05:08:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e6a1aaa-970f-310c-ae12-f44aa4510eb5 | -20.30823 | -57.37136 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8b6a821b-2c92-379f-a651-1974eb495279 | -20.26119 | -57.32887 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 593f9fb3-098a-3258-9b10-0b139040b042 | -20.30663 | -57.35968 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 01c22d03-6b19-33b4-8e4b-8cb270c8d87d | -20.29547 | -57.36531 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1896f615-5314-346c-abc3-a06432dead6d | -20.31664 | -57.36145 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6b22e2a2-e5ff-3a4c-b92c-402fb55113f1 | -20.30214 | -57.36649 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e6f69978-99cb-355e-85ce-48ac19aed40a | -20.31299 | -57.31904 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 66fddcc9-7ba1-3b32-9f43-5dfacc73a377 | -20.47311 | -56.72862 | 2026-01-31 05:08:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5308e4cd-16e1-309e-af47-bcbe2b72f364 | -20.26394 | -57.33315 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16fb01bd-c31e-32cf-84ed-257923b79c6f | -21.83055 | -56.28302 | 2026-01-31 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77e51d27-0104-3f2d-a5eb-ab1147370d41 | -20.29192 | -57.30774 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README6.md)
