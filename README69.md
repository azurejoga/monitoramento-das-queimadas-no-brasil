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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1810abe7-cc6e-335b-b80f-15fae98537fa | -11.17129 | -47.26706 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6f163b5-1279-315c-a84d-4dd9daf1ec6d | -11.81569 | -45.00323 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23073d56-ea67-3c2f-8bc9-e02700bd4eb3 | -10.7052 | -48.5827 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf2c7e1e-c92a-32f4-9e38-0063581d06dd | -11.81882 | -45.00668 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c0aadf-75c6-3b14-95e3-e888eaf2afd6 | -10.22209 | -48.21913 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 963a83b8-6871-307d-b4ba-25518331d050 | -10.82326 | -49.37604 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16c7aaa5-30cc-389a-b06f-7f1e128404eb | -7.72308 | -46.21171 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0e18c69-7a60-3ab5-ac6a-c8fdcdc3a0c7 | -11.03714 | -47.81977 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1af7993e-1614-3072-9f79-5a577f7a8a49 | -12.26975 | -44.13216 | 2025-10-02 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13117eb1-831f-35ab-a795-85e0a7c9d8a8 | -10.68668 | -48.56861 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0472b386-1f79-375c-8234-dda724de20f8 | -9.81553 | -48.25659 | 2025-10-02 04:29:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34c90c0c-1ac0-36c7-9a74-e680c93d3134 | -8.89989 | -46.6166 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66cff1b1-0e86-355d-9ae9-f233b89a24a4 | -10.22397 | -50.31964 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47acd6b4-2a0a-3207-912a-897b07a78819 | -11.62054 | -45.0346 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdff0a30-1785-31f5-b326-397599e78272 | -9.44244 | -47.92852 | 2025-10-02 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f39837c8-6e82-3b0c-b42a-24b786168c3d | -10.22544 | -48.2198 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9efbc7a2-95f9-3e98-8d58-abd07f7bd352 | -9.40252 | -47.58743 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0d1917a-e52d-3f63-95fe-7d40586c23f1 | -10.64144 | -47.45595 | 2025-10-02 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc87c3cf-4883-3734-86c8-01701d046fe7 | -7.83099 | -47.25929 | 2025-10-02 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c6f2805-aff6-3213-adef-848436610b39 | -12.26757 | -44.13396 | 2025-10-02 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2b2b311-0962-38ae-90f3-a3bd4ba7a864 | -11.8049 | -47.58224 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a228f278-6953-3890-ac11-1b1380d0e7d8 | -11.61875 | -45.04669 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c8d5879-fbcd-36e9-8eb5-9030791ba574 | -11.57514 | -47.02451 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3591dd90-8f35-3b07-bbfd-d5a9390fd77d | -11.44163 | -43.88482 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1d351ae-90ba-30fa-9898-9247dff206ae | -8.57272 | -49.60368 | 2025-10-02 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3c47c669-f45b-33f1-bfdf-a6a4d8edd80e | -10.83679 | -46.61672 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6edc203c-5070-3ed0-87d0-18b73087ac4e | -7.72586 | -46.21573 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7643df6-e8c2-3fbc-8f66-b2e9a6a1b26e | -7.56343 | -42.40103 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ebbb512a-3476-322f-92bd-5fe677d4d21f | -7.79163 | -50.21776 | 2025-10-02 04:29:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d50c8eeb-c43a-3abd-8788-647e8dcb7e31 | -8.51444 | -47.80785 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b9f0a8f-32a9-3bee-bdcd-fb7380c59163 | -10.82118 | -46.60695 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3707eba7-0b74-3481-82c7-f9a9a6e048da | -10.77594 | -46.6002 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1a2ac77-d193-3964-b826-52a2cd42dabb | -11.47069 | -44.97752 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb186d31-3842-326b-8106-f8756031ee13 | -7.55891 | -42.40516 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4ba69e86-2d11-3361-890d-4317a63116a1 | -10.83513 | -45.37427 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c40509f-5e3c-33a1-ba20-26115a6c561c | -11.91185 | -46.74578 | 2025-10-02 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd6e7807-ae1c-3716-90e5-27fac61881cb | -10.26736 | -50.3271 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e1aa0e72-efde-368e-9805-9f9ab1fe20ba | -6.67458 | -42.79391 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2b53a681-dac1-3da7-b83c-4810195fdb97 | -11.07922 | -47.80466 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24308f71-43e7-3671-acd8-70240bb54af9 | -9.85652 | -46.88026 | 2025-10-02 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2757cbf-b187-334e-be81-46bd2dbf6863 | -6.28417 | -44.0684 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab82d7cd-fb39-3d02-b36c-0637d87abb92 | -10.32963 | -45.26421 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 469d6ddc-3c53-39d6-ad62-32250af39695 | -11.18735 | -47.18662 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8f99ef5-0250-384b-94cf-7f48315bacbf | -9.79567 | -45.95004 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce417eae-eba2-367d-9ffe-04a10d445c2e | -10.84377 | -45.38706 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c932e38c-c31b-392c-b935-29e5985d3a59 | -9.91843 | -43.71626 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4bd4b0b9-7f18-3a9c-8122-a8463d07c6b6 | -11.68042 | -46.97575 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7bb3451-0b23-3d56-b506-30a299c90232 | -11.58894 | -45.05074 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac35d7ab-2bcc-3b5c-8449-5e757b048dc8 | -8.71169 | -47.14548 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bd2972e-80a8-3acf-a691-1340f15fc61e | -11.19401 | -47.18769 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7325c5e-de82-3f11-932a-3d5642a0044d | -11.45083 | -44.96609 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17c22591-1801-33ec-b4b3-fdcfbbaa2eec | -12.22061 | -43.76017 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7802b260-4812-3b09-8939-41433ccd9040 | -11.79811 | -44.97628 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d89279df-541c-313d-8a61-20d29d55a999 | -11.16796 | -47.26653 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cb69a00-1f6c-3c7a-b69e-b7b4be25429b | -11.67574 | -47.50009 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d193d45b-fd17-3379-ba31-5448a148fc13 | -11.08911 | -47.84975 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9d0b5899-86d5-3a7a-b43f-60beeb73ece5 | -11.78882 | -47.576 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b98e658-7818-38a3-9eb4-d46c477f9e0a | -6.82144 | -47.97659 | 2025-10-02 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3121b57f-2a10-34b2-89c0-f93aa482046a | -8.51715 | -47.83393 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd74d7e0-4ce2-356d-b637-af8e7ce59e0c | -11.17018 | -47.2741 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70f3bc7a-659d-3831-8927-cf4b0845cf0d | -10.82252 | -47.94814 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef9cabec-da6b-36d8-ae8e-84c3a69b3e07 | -10.39312 | -45.12612 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bdfca64e-b716-35a8-89ca-56f4589f8d45 | -10.81495 | -46.59174 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6f9b637-6634-3a65-92a6-17daafe4e344 | -5.90056 | -45.64743 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90d4ea19-bc91-325f-be78-b47451867476 | -11.91241 | -46.74221 | 2025-10-02 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 832492e1-ef8f-3b60-ac98-c6f26dc213dd | -8.90757 | -47.59806 | 2025-10-02 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff2865b4-caf3-3581-8530-53e944da0ad9 | -10.85457 | -46.59046 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e380e370-cba3-3b1d-b803-c5545434781a | -11.48315 | -45.11122 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60159e2a-c0eb-3476-9c75-04950fbbd137 | -10.2485 | -50.30659 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d60de53-57dc-3258-b28b-5146f3b8f47a | -11.80435 | -47.58577 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e143e86e-bdc9-3219-85ff-96bfe68dc01a | -11.83758 | -44.95253 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3dbe9332-9e1d-32a4-a254-db7b418557ee | -9.84681 | -49.95568 | 2025-10-02 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35c74e39-e666-38b6-b3ab-df57a6961d2c | -6.2646 | -43.89197 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93e4d648-b1b9-3f1f-be5b-7f8522023c66 | -12.21706 | -43.75717 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a9c8460-05e6-3906-aeac-d7f1c110c7db | -10.22429 | -48.22696 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ec6440c-2bb1-36f1-bca9-23c78727203c | -9.93983 | -43.72381 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 15f1cbd2-7922-39a0-acfc-3cfac7d23393 | -11.37819 | -45.04446 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f8a40cf-0198-39dd-bd85-0a8e12dcff12 | -11.60303 | -45.0559 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85b36e3a-17b2-3b2b-94ae-3265c0a9629e | -11.03771 | -47.81622 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 97e3cf26-18e9-3dcf-95e8-1ef19496707b | -7.84054 | -42.85228 | 2025-10-02 04:29:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7501fdf6-0b7e-3f45-8ee7-d3b3f0931449 | -9.7923 | -45.94952 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37c6d39e-a494-3cd8-936c-e8b844c865c0 | -11.4684 | -44.96886 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3716647-ff15-363a-9d20-fea6ea4f5ea5 | -10.3273 | -45.25635 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a23393ea-3d18-3d68-a717-f11eb54fde86 | -5.84068 | -45.75168 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c089c919-044c-3889-8d00-5b35adeab40f | -11.18679 | -47.19015 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73a8239a-e0ed-37b3-af87-40594a652ea9 | -5.89389 | -45.64639 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c625dbb4-e0b2-3cd1-b95e-1feccc475cb3 | -11.60597 | -45.06028 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fae4f41-4889-376f-90d4-c17f38d03dd2 | -10.83801 | -45.37851 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60d675b1-62b2-36ed-9e60-d0794226aa41 | -11.86877 | -45.03427 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4fd01e37-9fbb-395f-8723-9a39b0a06991 | -7.5523 | -42.638 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 66728c95-d891-3a3b-a5bc-5b5eee9ff6b7 | -10.8432 | -45.39083 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 72d54ea6-7359-3026-85be-20a9862b3ae1 | -11.05492 | -47.81545 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8c758d9-9469-3412-8072-9868924721f9 | -10.23049 | -50.32508 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 32580996-cb05-3582-b0e6-b0a26bd918a3 | -11.43503 | -47.18325 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70f63e8d-9ff6-321d-a547-3031a7e1c222 | -6.26793 | -44.05823 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f42d8e3b-2a35-31d8-8e4a-d6e4e06333c9 | -8.56709 | -48.64755 | 2025-10-02 04:29:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9ac8c709-3f18-3463-8b4c-1664c2ef1bd1 | -8.46675 | -46.83393 | 2025-10-02 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46c094b5-865a-3c3c-9879-0174d4d45b9d | -11.66765 | -44.27919 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc372d84-b5c2-3aff-87e0-11d69ecad2f4 | -11.27109 | -47.81767 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb1d3e5d-59b6-3268-94b3-091b367a8125 | -8.51157 | -47.82569 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README70.md)
