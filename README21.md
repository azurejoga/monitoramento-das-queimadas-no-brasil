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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a728e19-d033-328e-8b3d-4b9699941ca0 | -11.18099 | -54.90185 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4f37829-f502-36a1-a72b-8153623ca4f3 | -11.17123 | -54.90705 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d43e3af3-b17a-37ef-a058-2230d0943292 | -15.41013 | -59.50565 | 2026-08-05 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35119e0c-d51e-38bb-92df-84d139f5ffdb | -6.56604 | -55.14425 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 587deb66-1bd3-3d87-9b47-61fe6f4d5471 | -6.54848 | -55.1653 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91007193-5180-3323-a4be-17e8f5af469a | -11.18355 | -54.88393 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdad158d-8253-3121-b1c6-3799fd56c5e1 | -11.17736 | -54.87384 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f638468-3650-3836-8d0b-78df8e4b044b | -6.55837 | -55.17078 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93c22ce7-342f-3ce4-9f69-9bf052957d0e | -6.01289 | -47.40106 | 2026-08-05 05:23:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28bce630-78d4-3e08-a58d-8697b6d43311 | -11.17106 | -54.89127 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fef89a3-cb14-3189-9f10-f2ab589bbdb8 | -11.16948 | -54.89315 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2556d978-d161-3411-982b-b040c47a8457 | -8.35383 | -45.98456 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1522b82a-c918-3823-9755-c37c2ccccdf7 | -6.58221 | -56.54268 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1938d54-87f9-3c22-b424-0062fdb1bb11 | -17.45116 | -47.86675 | 2026-08-05 05:23:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a496f060-f057-323c-bdd2-97278fb05e72 | -11.1698 | -54.90018 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a5cc157-df22-30e3-a216-7b09eb8fe81f | -11.17496 | -54.90762 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06c6bc35-2b9d-3612-87fc-e8372ac72ced | -11.2071 | -54.90574 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e07eb866-98f2-32e9-a0c1-fc18aaadb681 | -8.38204 | -48.21152 | 2026-08-05 05:23:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fe43f20-a79d-3053-b88b-f3278d370915 | -11.18987 | -54.86637 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04b59bfa-c71b-35ee-b39b-75141d8fee0f | -11.17471 | -54.91915 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2dae689-96ca-377a-a0d4-1cf979c4c0b4 | -11.20173 | -54.86356 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be6a1e3e-2e91-31a3-a5bc-d55a956b9173 | -11.17695 | -54.89423 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d30529a7-75de-31d1-a746-04fc32e5b406 | -11.21149 | -54.90178 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6eaeee79-ffd9-3571-af9c-fb1f66b937a9 | -11.18716 | -54.91192 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7219a655-9052-3beb-af73-c6e31b08ad52 | -6.57534 | -55.15359 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cb2704f-a79e-37d0-bbea-1cd95d3f85cc | -11.18664 | -54.88896 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e92f23d9-e56f-39b7-a3ff-1b967088fff4 | -11.18045 | -54.87891 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb2dc0b7-a89d-3c01-b6f9-867495e7203b | -14.1895 | -54.43989 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a16ca6b-b9ed-3bc7-a5a6-9f8209c6a612 | -11.16685 | -54.91091 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5aae062e-a373-35a2-87fe-052f589189bc | -11.17629 | -54.8987 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d20229d-1126-3019-94cd-11c2c18f767a | -7.241 | -59.45355 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4942e4c9-0501-3841-ba05-cd3c8c30d961 | -11.22548 | -54.85785 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fab1a8f-216f-3d68-8443-f11c6df20233 | -8.49633 | -46.85959 | 2026-08-05 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ac9fb84-1cc3-39f3-b898-e319d99b83dc | -11.20158 | -54.89112 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b73f4f16-7830-365e-bc11-c5a1d60b2775 | -11.06948 | -50.57227 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c9ca738-8f27-38f5-bbb4-ba7821049bd9 | -17.98381 | -47.16466 | 2026-08-05 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 60b2a157-5e5d-35ca-8a5b-b9de3ac33724 | -11.17544 | -54.88735 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d9bd6cf-7dca-357d-9ea8-e45d02623eb6 | -14.19825 | -54.43542 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47dcab60-9ad4-303e-9058-50277a834f2c | -11.19965 | -54.9046 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bbf96dc-6410-38cf-8d7b-48d84f7c5afc | -6.22383 | -55.59458 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3632e256-7245-39ed-bade-c56a4035d9e8 | -6.5374 | -55.16751 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5512b153-8aac-3a40-b697-2f6c814630eb | -6.4103 | -55.78881 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 507df583-8489-3a27-a7da-cf5dc81b96ed | -6.61962 | -56.37013 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec600ad2-d018-3891-bf3e-ecc0beec0ecc | -11.11267 | -50.398 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7ff345a-27f1-325f-a05f-348e4f72e50c | -11.11191 | -50.40379 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa3470bf-f0d9-3f00-90a1-824b35cc00e6 | -11.17761 | -54.88978 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 486127e0-2dd3-3b81-8d28-045e072e4c61 | -6.61738 | -56.36246 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d108fdd7-0073-39e9-93a4-fca93639ba3d | -6.56658 | -56.53296 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab06137-5e76-351b-a6f1-a7db7fcfcad8 | -11.19463 | -54.91299 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d421b83-e4d3-3c8c-aab9-dd77b4f960f8 | -11.21392 | -54.91129 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62a28341-1d12-3fd7-85be-469fad28a9e7 | -6.56099 | -56.52482 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96ad8d5c-a8c6-39f4-8ff4-e9ce79a9a0c8 | -11.16842 | -54.87463 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc2e2a3a-a6cd-3144-b890-698a605526b2 | -8.3528 | -45.98365 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1c97404a-bfde-3613-a54c-a85d25f41c5f | -11.19154 | -54.90798 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9f8ed79-b176-3206-9273-a16e7d3e2aa0 | -11.17416 | -54.89627 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bfb1259-bcf1-3113-bbf2-6700ccb8de81 | -11.19412 | -54.89001 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec403b78-5421-362a-a51f-c06e96285782 | -10.88481 | -50.15503 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 659fe283-f2a8-3dfc-8e7b-771ae773c3b1 | -9.48719 | -57.32551 | 2026-08-05 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9dd23b0-9b17-3480-98f0-902efca55fe2 | -6.65108 | -56.42226 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74891e2d-d366-3142-a7b7-e1993c5e461a | -14.0311 | -54.08725 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccc301f3-7780-37ab-bef2-d36f6e5bc932 | -6.54498 | -55.16476 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab9c46cd-28ab-3ac4-80a6-788c16303e97 | -11.20841 | -54.89671 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e968aed9-e953-3579-9820-2f3b97971e4b | -7.57646 | -49.55877 | 2026-08-05 05:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a716a7f-b968-3018-b796-a731df572221 | -11.17298 | -54.87781 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3992f8c2-4844-31c1-aae2-38a3f980847f | -6.55547 | -55.16637 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c853f969-9d2d-3f89-8e34-df5d9774fc9b | -11.1748 | -54.89181 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a76266b3-5c98-399e-8a5e-f1dce41c8345 | -6.53918 | -55.1559 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dee29e80-5ec9-3e8a-8ea5-55a163474519 | -11.18097 | -54.86725 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17441f48-71dc-3f28-ba72-8e8ec0d495c8 | -11.19118 | -54.85727 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cb15360-bc42-3afb-bb06-ae08ca362ac1 | -11.20517 | -54.91912 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6e12915-388e-3f00-9c6d-57031c78b09c | -11.19025 | -54.91691 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 250a1f11-301a-3198-b35b-e077e3d66e52 | -6.56993 | -56.53348 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fcf30c3-35f0-3ac5-a67a-fcb84789674e | -11.17669 | -54.92154 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a77168bd-1083-30f1-8605-d25f1ab54cbc | -6.55026 | -55.15366 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92c79c35-4419-32ff-80c2-546a903c7eab | -11.1743 | -54.91206 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7c81283-cfaa-39e3-8dc2-954dd64f9140 | -11.1651 | -54.89703 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13ad4fe3-43d2-3f23-b758-603d5f404823 | -14.16162 | -54.3968 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 918c43c6-5a41-3876-8d6b-dd39ea069404 | -11.19527 | -54.90851 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20c354ba-ffe5-32e0-8ee9-2f4922bb7019 | -11.10386 | -50.42623 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2611a811-6463-3bee-be52-f534d3067bbb | -6.55078 | -55.17356 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ff22053-6acc-329e-a1f5-127deccd4e7b | -11.18343 | -54.91137 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fcac4498-9ff4-3eb7-bbed-18f06672730e | -11.16909 | -54.8701 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21db6bc8-c6a0-3bc0-8f43-42ac3565266d | -6.58277 | -56.53913 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc8f1fe0-979d-387b-9470-a2dd55a4e826 | -11.1717 | -54.88681 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7d7d657-f6ab-315c-90a8-4a65afff3dca | -11.18471 | -54.86778 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8759407e-c736-3201-ba88-9a678ceac978 | -11.17148 | -54.87973 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f0656d2-98db-375d-98e2-66c75edc74ec | -11.17935 | -54.90372 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 141d3eb2-ce31-3d7b-bc6c-b6bdaecdb791 | -11.16816 | -54.90204 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4893863-d0f7-31e0-9c48-b878f46e95f4 | -14.02703 | -54.08668 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f4f900b-59ee-3fe1-bb6c-396a491446b1 | -11.20029 | -54.90012 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c68ea18-22e4-3bb8-8fa6-3cf69dfad1ac | -6.54148 | -55.16422 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5d1e897-3e90-3c9c-aba1-88247f19f57e | -6.53219 | -55.15477 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7adbac5b-0e35-322a-b69d-687e82976f52 | -8.34099 | -45.98257 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b6a537f-6bcc-3b60-82c0-3bd0760b0ac1 | -6.55904 | -55.14315 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c400c2f9-23fa-346c-ad6b-34dbbaf0c8cd | -11.19053 | -54.86181 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e177c4e-539c-34fd-bff0-cb0b13d11e7b | -6.33496 | -55.73632 | 2026-08-05 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53d0f7e2-f572-3147-b238-cea993472c8a | -10.46367 | -50.23339 | 2026-08-05 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b43f220f-1099-30d7-bbcd-c3da63e7c73e | -11.1797 | -54.91081 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb037389-0ca9-361f-af69-35f8154d527a | -6.56945 | -55.16853 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e5d5c12-9b8a-38bf-af7c-dbaedff2a1b4 | -3.39727 | -59.57128 | 2026-08-05 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README22.md)
