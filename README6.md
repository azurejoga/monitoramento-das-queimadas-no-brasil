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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edd68ce2-b1c8-38ea-915a-d6869e6010bd | -11.60306 | -47.4447 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1ddc919-fbae-3e96-b22b-83ccab73349f | -10.84264 | -46.92809 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bf1b362a-51b6-3824-89e3-4bc460b4aea4 | -15.80717 | -58.68102 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bfe1d739-a368-3b16-a095-3eafc295d09d | -11.99875 | -47.76593 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e2cfd2f-1b02-3830-82d6-83c00af494f9 | -17.83909 | -42.6155 | 2026-05-30 04:38:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 487e9212-0bd3-3327-b687-c3b3289aefea | -11.92701 | -43.92375 | 2026-05-30 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49270e78-e2d9-3874-87cb-500c126c66ee | -11.97857 | -47.89304 | 2026-05-30 04:38:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 721c211e-3f8a-3357-9783-be0bb970d76e | -10.38574 | -49.44347 | 2026-05-30 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 438ad032-115c-36d9-92dc-0b31255ad5b8 | -11.59029 | -47.43901 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca7d4563-1fcd-315c-96e2-8380409690ac | -11.4737 | -57.11156 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba8aaee6-b8cd-3852-983b-1d0d4d955f15 | -10.84042 | -46.94225 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| b4035761-deca-3983-9630-e6b548a295ce | -15.82515 | -58.61935 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 81150643-e5fa-3af5-8236-66903c3c4b08 | -11.58751 | -47.45667 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a789cea0-013b-3094-92e1-1a09524dc5df | -11.17075 | -46.79495 | 2026-05-30 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba90fd09-1165-3d92-9ea8-eeebf3eb8c12 | -10.80369 | -46.91459 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 792c6d98-8692-3b5d-a16b-e1b2d4e88150 | -11.62854 | -56.8609 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68925413-b3a3-3c64-870b-b131ecf76169 | -16.1739 | -58.47245 | 2026-05-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 30e67050-8a0d-3504-bf90-85d03c198a4d | -10.77592 | -46.96088 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bed32630-2e00-33e3-95f7-5f0e49d1bb8d | -10.7965 | -46.96054 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89000b17-bfe7-302a-8f50-82fdb979926a | -12.44914 | -44.74944 | 2026-05-30 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e123a1e1-e40e-34c3-94d5-88a62ac0b136 | -15.8267 | -58.61196 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 87ba5729-97a2-320b-8063-aec1e6499065 | -14.06436 | -53.37376 | 2026-05-30 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37020acf-e58c-3948-bd91-f671883232bb | -11.1713 | -46.79139 | 2026-05-30 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcc6bdc9-a594-35b2-9c2b-00fb2673cd21 | -12.67951 | -54.58355 | 2026-05-30 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ce29572-06c9-33f1-906c-c02187062fc7 | -12.00271 | -45.35914 | 2026-05-30 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40d31d25-29d0-37d4-9ebf-63d398bbc741 | -15.30645 | -47.38364 | 2026-05-30 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd13f10e-0c2d-3b64-9fdd-d1bb4e11bc1e | -10.78092 | -46.95082 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76ab6fc4-f97d-3ebc-945d-488078491790 | -11.7645 | -47.06014 | 2026-05-30 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 402b93e8-3789-3751-88d7-be62b221b062 | -10.84431 | -46.93925 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| f02f08f3-d60e-3af7-8345-ceb13b6e16cd | -10.62733 | -48.32644 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1568844-6214-3afc-9149-41750446bc0a | -10.84516 | -48.34033 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac261e46-cbb6-3ad3-b4e3-b907fd6f0475 | -11.97191 | -47.89196 | 2026-05-30 04:38:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36d349ae-27a1-3fda-b73f-796405168418 | -12.12872 | -47.21301 | 2026-05-30 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4734a2d1-7f5f-3f2d-a8a4-6bde0ce54542 | -10.82041 | -46.96075 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b97b948-5e77-3d4b-9d96-798fc2258513 | -11.53704 | -46.43706 | 2026-05-30 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46a312c6-f193-3522-8df5-2f4b15d46c82 | -11.16516 | -46.78676 | 2026-05-30 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24920576-6781-3e17-ac7b-a723b58b2292 | -10.77426 | -46.97148 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44dc87be-f36a-3cb3-9063-7c6844708019 | -12.00208 | -47.76648 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7813bbdb-60af-3900-86da-62b55f587d1b | -15.82684 | -58.61228 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2751a450-bbf4-3d58-837f-e7a941b60552 | -10.84208 | -46.93163 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8aca5a18-8cbb-3511-b380-db019297c24a | -12.42351 | -47.88232 | 2026-05-30 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f04fc03e-e4e4-37e6-b1dc-c047fd1b8368 | -10.78257 | -46.9402 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 663fc74c-a7f5-32f6-a3b0-ec040dce0c2b | -10.77148 | -46.96742 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b0d9f53-71fa-3ae5-9d5a-907cfcc63750 | -16.1689 | -58.47443 | 2026-05-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 79726fd1-d217-341d-bc1a-4507e324fca2 | -15.80642 | -58.68473 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9ac06b0d-bc42-38b2-8f43-ba8049d15cb0 | -10.78036 | -46.95435 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d253de4-6eda-37b2-9cf6-ed61e3c42ac0 | -10.78591 | -46.94074 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56099379-2a21-3c28-8cd9-e900ea92b3a8 | -16.24221 | -47.90122 | 2026-05-30 04:38:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 396d2ac8-2ce5-3198-98a7-ae83ac661622 | -11.58474 | -47.45259 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e15ae02c-91bb-3a6b-90c2-2166e7dea60b | -16.67503 | -49.13429 | 2026-05-30 04:38:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3414900-eacb-3e8c-9fbc-6d1a3b6c5d77 | -12.1354 | -47.2141 | 2026-05-30 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6789698e-1207-35b5-9d12-f0b83178a49f | -11.79912 | -57.01131 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aea07c9f-868e-3946-9a02-188eaa36c074 | -15.82593 | -58.61563 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b983c8b9-5443-33b6-a86c-f5f62f98a5e6 | -10.77093 | -46.97095 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6471492-1df5-3489-a601-99806c317bce | -10.77647 | -46.95736 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71e8f003-e541-39e0-b039-cb9214d490fb | -15.69288 | -48.02417 | 2026-05-30 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec78e981-d611-3c07-87a5-e5789a54ef4f | -10.83986 | -46.94579 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 004ef550-1137-3772-9663-211a30a50d0d | -10.84152 | -46.91341 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 32f2d78f-5f1c-3e14-a19c-768d252095ce | -10.76872 | -46.98506 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b79e424-ef3e-303c-94fe-aef9446d5769 | -10.81424 | -46.89091 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1b3c0ff-e3ad-3394-92ac-76fb1e964aed | -10.77703 | -46.95382 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58cde501-7964-3807-80eb-016f3ae1af8e | -11.58641 | -47.442 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9344b8b-0229-3469-85ee-d6fdc05c6be0 | -11.63257 | -56.8686 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b085f10-42fb-35c5-aa19-99dc948a5e02 | -11.80572 | -57.00561 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5f0d5ee-9dc3-396f-9d06-8840d471ddb0 | -10.83379 | -48.75886 | 2026-05-30 04:38:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 330698ed-f9f3-3e5a-937c-8066ef59c914 | -15.82201 | -58.60709 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cec341f6-f9d4-3858-a33c-41142a0bf6bf | -11.62664 | -56.87094 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0dee691-ac5b-3aa1-88f6-e0f83149a6ad | -15.41909 | -56.3136 | 2026-05-30 04:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13af3a48-1276-3ab4-be37-d269970d6b07 | -12.31933 | -47.89803 | 2026-05-30 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05fa15af-c1e7-32e8-a707-2463255ac73e | -10.83873 | -46.90934 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79413ef5-0ced-3bd4-9c7b-45d9e9b72b2b | -12.13484 | -47.21766 | 2026-05-30 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 970699dc-e004-3860-84bd-6f5c6a94a328 | -11.96493 | -44.19346 | 2026-05-30 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1adf5fb2-7b4d-34f4-96ae-eaa0bf5d37b2 | -13.5559 | -43.59067 | 2026-05-30 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbec73e5-fda4-34a3-8cd6-8b710bef3388 | -18.53549 | -43.24215 | 2026-05-30 04:38:00 | NPP-375D | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e28b72a7-e048-3ac8-a72c-7f5e5c4fbb83 | -16.16094 | -58.48084 | 2026-05-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9765c2aa-7f6e-3514-b606-4c1a256e31a1 | -13.47552 | -47.51416 | 2026-05-30 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 868ad8e9-8527-3ebe-b1fa-ef57076ba77e | -11.63383 | -56.8619 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4b6fdfa-1f5a-3802-b667-5d810184be0c | -11.59307 | -47.44308 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f06aeb3-e787-3a9a-8e9c-ef35dcb6a61f | -11.63202 | -56.86374 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d693a6e0-eb3a-347f-865b-7c2e81e4e437 | -14.24149 | -47.99355 | 2026-05-30 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d3d81bb-dadd-3455-9095-ffc7384a8d1e | -10.84542 | -46.93217 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3776623a-2395-3290-991c-6bef8c0fa5ba | -15.78275 | -58.66019 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5d2952e0-804c-3df7-9d13-925d45bcfda4 | -10.78092 | -48.54642 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b05e954a-a0d3-3339-97ba-ab3854afd7cd | -16.16167 | -58.47726 | 2026-05-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 51cb59a4-6f83-33f1-80cf-c74dccea567e | -12.70269 | -44.79316 | 2026-05-30 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec0869d4-48ab-32df-8473-8c307cd0a7e6 | -10.6279 | -48.32287 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d6370200-f371-3d0c-aa47-8380d4fc1aca | -10.78821 | -48.54398 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10bc2842-60bc-3bb8-b118-dd933adc4291 | -10.63725 | -49.72985 | 2026-05-30 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9533beb7-30f5-3dc7-95ec-8c827181dc45 | -14.06034 | -53.373 | 2026-05-30 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eae191d4-9410-35ab-a9f4-9efe225c1317 | -16.17428 | -58.47564 | 2026-05-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 64a20240-6164-3e7c-98e1-e160cf5da993 | -10.84097 | -46.93872 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 3334bd48-f2c5-3fb7-aba1-6f6b12c78a83 | -10.77981 | -46.95788 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a01b656b-79da-306c-8ade-e904a358ae03 | -11.60029 | -47.44063 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98e6b746-f41b-323d-8748-6b6ca2f73ed9 | -10.84486 | -46.93571 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| f2cd2e62-34f9-3134-b6c0-93632e030f78 | -10.81368 | -46.89445 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9efd3cd-ff82-30fa-8707-8ad74485fb1b | -12.13206 | -47.21355 | 2026-05-30 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55fb889a-7ad0-385a-a770-c3fcb6b3a84b | -11.6332 | -56.86524 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f1da694-1175-38a5-add8-aacab6f643fe | -14.24205 | -47.98999 | 2026-05-30 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39ed47ff-4006-315d-b13a-6367e30e6091 | -10.84598 | -46.92862 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ee227cc1-3772-373c-9515-a4ce15ac6bfd | -10.76982 | -46.97801 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README7.md)
