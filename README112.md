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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e3cd355-3953-31a0-a5a0-509d1c4de0f1 | -4.12143 | -54.42554 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 4274a907-3fb7-3af6-a969-9a1e13a40515 | -4.93629 | -45.1468 | 2026-10-05 17:15:00 | NPP-375 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3dcb5494-fb2c-3f31-b277-f49c980ceee2 | -5.68843 | -53.48678 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 415e5e57-5048-3d4b-a566-a079a91dafd7 | -3.63766 | -54.5093 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 66fc1b50-ab8e-3973-a377-124f98d561b5 | -2.67336 | -49.0352 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b14a6e53-3447-3384-a866-48440be17485 | -6.4032 | -44.01276 | 2026-10-05 17:15:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1bb89e20-228d-3b69-ab1f-b307aa458521 | -6.72121 | -44.28179 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9db8c02c-6d28-3ce3-8336-3afb85e457c8 | -5.67728 | -53.50267 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b768d3c9-7295-3f6e-ad35-da8d8c1fbb64 | -3.07709 | -54.16271 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 908c2789-57f0-33eb-a70e-edad69943772 | -6.59634 | -41.57674 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 1df233d0-40f0-3321-9f12-b27df53a40f3 | -4.05698 | -59.36303 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cfdd1c33-1c4d-3189-b5b2-a1999b465e77 | -5.68392 | -53.50166 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2b3b4c57-cf86-3843-b660-769e347274ee | -2.85459 | -51.29883 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a20935e2-a0b1-39a2-b9e6-9a5529c0971a | -2.70042 | -49.03452 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 43bd672e-0375-332f-8a38-dbec01a93a5f | -3.05424 | -54.16687 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 027ed61d-2c55-3439-8543-72fc6d238448 | -3.50236 | -54.62242 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 37987de2-728f-3d28-86c3-9be4ca59d183 | -8.54008 | -54.57825 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2524278c-5eaa-33be-addf-bc8989e8d9a9 | -7.82564 | -45.30608 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3eacae68-a340-33aa-9ff9-df4ffe0f158f | -5.40027 | -54.45541 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b1da922-bb24-3ef0-ac7d-6bc6f5f0b0b9 | -3.1089 | -53.71133 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 6da6448c-b4e9-350a-b90d-d3e21903e8eb | -6.69163 | -45.21746 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98c232a9-558e-3e6f-850a-210478d24460 | -9.16205 | -45.13605 | 2026-10-05 17:15:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4e18e536-c215-3e43-813e-4fe8a6a523b7 | -3.47136 | -50.0985 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 623878ed-8710-36af-950d-c28b5efb39e9 | -3.27518 | -50.01507 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3687b441-2aae-37f9-9fe7-87075aaf415d | -3.51618 | -54.62387 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47c864f8-8d7b-382e-b8c8-3e923581d1cf | -5.73135 | -45.05328 | 2026-10-05 17:15:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe740419-d9da-33c1-bfc1-5722395d6189 | -3.22348 | -54.30247 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 512b4252-a428-3891-ae10-f2f73c7a7eec | -3.08479 | -54.1686 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f58efd9f-3bf6-35c1-9e10-42346f3f9df8 | -9.15295 | -45.12844 | 2026-10-05 17:15:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94eb3f07-5b38-322a-b95e-12da0694ad67 | -2.98993 | -54.03536 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fa632359-ccf7-38f4-8d40-2b2ace3f0680 | -6.67317 | -45.22067 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 23bf701a-c661-3b27-bd99-dd20893371d3 | -3.08584 | -54.1755 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1d1fd20b-4841-3ace-af86-b49be1c5a806 | -3.09633 | -54.17744 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5e22fcac-edc2-3dfa-8442-f1a5fe58e5c6 | -3.65886 | -54.51936 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b734c8c5-1cf4-303f-863e-a8a42f2a7669 | -5.89639 | -55.52661 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b2b1a0ce-0f06-3541-933e-75e15309389c | -4.48419 | -43.9084 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c7a32fd1-d6dc-3f44-a147-35106c21d730 | -4.81386 | -54.73335 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| fb069898-59e5-33e8-8999-ce399fddcb1c | -5.95205 | -41.36299 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 174.8 |
| 14af6b46-aaa7-3e62-a23a-c7e0aebeb3ee | -7.28532 | -39.15298 | 2026-10-05 17:15:00 | NPP-375 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 60385560-1691-32f6-a54b-463cdc2b2098 | -4.45354 | -54.96173 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 65799743-e467-3fa9-b3be-da4d82aa0606 | -3.79448 | -41.76041 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 3fca61b0-7fe1-3fd7-b008-0b8a2783c82d | -9.03936 | -45.15094 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c4ca6ec-9810-38a2-b908-9ab6cb94e8f3 | -3.09195 | -54.17105 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| e6b62465-4aef-36ed-9bf4-e6cec6766aa4 | -7.2243 | -55.17871 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 331bf2af-2261-3692-b3dd-cadabb1d31e4 | -3.95345 | -42.97205 | 2026-10-05 17:15:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9232300-23cc-3a5e-bcf2-ee84101d2e67 | -5.46899 | -41.23809 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 84e28bf1-763d-3940-a5a1-805829066316 | -3.65235 | -54.27665 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e4732a4-70cb-31f8-a66f-140277c73b85 | -3.23591 | -53.87605 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0e6c103f-e158-31b5-92d9-fe013c0d76a3 | -3.50131 | -54.61551 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 83ad2e67-e853-379a-a347-29cd881271a7 | -9.50717 | -46.82165 | 2026-10-05 17:15:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 3818fabd-6630-3d13-9f65-1cfba2e56433 | -9.10449 | -65.35898 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 151a3ac5-d2f3-3aba-8d6e-c34f2a04dea4 | -8.00618 | -42.92114 | 2026-10-05 17:15:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| 84dc187e-0264-359b-afce-0bdd0bded38e | -6.04532 | -59.94532 | 2026-10-05 17:15:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 78168eb3-2362-323d-987c-5db3c84d7fe6 | -3.12448 | -53.70185 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 63cb3232-a1be-3db8-835d-ac6e93eb88aa | -3.51565 | -54.62041 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cd992a9-7a12-36b5-935c-d90449a295fd | -3.07694 | -54.18391 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c00ece3f-e2de-3514-a0a7-b3d3334036d1 | -5.88567 | -52.50692 | 2026-10-05 17:15:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 00f95fee-330b-3c35-aebf-97a5ad0c0ba2 | -3.08863 | -54.17155 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 12819204-b631-3e17-b87f-570a0afc309e | -5.27111 | -47.90822 | 2026-10-05 17:15:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| de829524-c9dd-348b-86d7-1e8d46536540 | -6.34133 | -42.54272 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b52e3dc1-763c-3153-ba29-1f879aba7471 | -6.88594 | -43.67965 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| c83d3ddf-2228-3374-b258-c11216b2d709 | -5.96054 | -55.35108 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3f3f4457-6527-39f1-b48c-98851bc3ab04 | -4.45395 | -54.89718 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 4ef54fba-12e3-3d58-926e-976ae07ca411 | -9.0008 | -54.42164 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a4458e0-b9c3-3503-a010-70d57f40c8e7 | -3.80054 | -58.34649 | 2026-10-05 17:15:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e09daed4-0300-36ff-98c1-ee981d506a1c | -2.41594 | -48.06324 | 2026-10-05 17:15:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 103c70e6-8a79-3373-ba60-99af2bc4fef4 | -5.94342 | -41.35265 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 413bac0c-d797-3234-8334-02c1228252fa | -3.38005 | -54.11134 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8e67b7b-f96c-3cb5-95f7-1a7beeb8ac60 | -4.27817 | -59.41213 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4e4b76da-dd06-33bc-805e-f8a8701958c1 | -4.6566 | -49.74488 | 2026-10-05 17:15:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| a73b50dc-1c33-37db-b22c-1f3f7c682a47 | -8.78206 | -47.56366 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 3763080a-99f8-3346-9a36-91fc44656266 | -6.08359 | -47.65407 | 2026-10-05 17:15:00 | NPP-375 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2721fab-b19f-3c5e-9ebb-6c6c4a8fdc53 | -2.99161 | -54.11279 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2b86b967-efe8-3c80-b736-257f22f6619b | -7.66058 | -44.3746 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88992cbc-b32d-34bc-8e89-c88ab4eb2bad | -3.58627 | -55.39952 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 942179ab-acb9-3ba2-baf8-9d4e4b0954cb | -2.44898 | -50.25501 | 2026-10-05 17:15:00 | NPP-375 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 41adfd73-a38e-3304-a79c-0c3099a75fc9 | -6.64698 | -55.32618 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 218aa4dc-15be-305a-8de6-c6cf410c6592 | -6.59539 | -41.57142 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 5b1362f0-7bdd-3293-9513-0802e019fa4d | -6.35575 | -55.14982 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f7ce4059-1e8d-3373-8900-1e3ebd5253a6 | -3.72736 | -55.47948 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| ad33c9af-7a2a-3d68-90c6-e2582fc3c03d | -9.50743 | -67.13216 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 36c01ce3-4199-39ee-96e5-78bd7f9db0f9 | -3.09837 | -53.70937 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 24a06bf1-8727-3991-8adc-8daef5cf29e3 | -4.3332 | -43.8255 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4bbf850f-da07-3ce6-8102-eb856dccd540 | -8.85447 | -66.7915 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| f684e84a-8ad2-3360-b620-dca507cbfafc | -4.8536 | -44.51882 | 2026-10-05 17:15:00 | NPP-375 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c9e2b3f1-6706-3caf-8d04-48c4f1f8ab45 | -7.22812 | -55.20452 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| cd64e4a7-253c-38a0-b491-bf71c5684ab6 | -4.00739 | -55.67208 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 5173a61b-36d6-392f-b4e2-e388e2ff8b95 | -8.43665 | -54.98468 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| acf3a274-43bd-39fd-9f4a-0efc1a95a13c | -3.79741 | -59.31967 | 2026-10-05 17:15:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d7ec4951-d70c-3d6d-9ab3-def828d76193 | -6.71283 | -66.49898 | 2026-10-05 17:15:00 | NPP-375 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 03823ca5-7aae-3621-a0db-1187f3d6e1c7 | -3.46752 | -50.09908 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76ce5e60-e129-349a-bf36-396570fd74fd | -7.89976 | -44.21118 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce16e2d8-02a9-3838-83ad-27cc489f1995 | -3.78966 | -59.3796 | 2026-10-05 17:15:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3c7223a8-97b0-3f29-bb90-64db6639767d | -3.07098 | -54.16716 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| efa32113-5986-3c0e-bc23-4fc3d0b55328 | -8.00547 | -42.91716 | 2026-10-05 17:15:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| 2d189683-8573-3bcc-a3c7-5bdd8f41b06f | -2.68584 | -49.03329 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c592bd65-cffd-3db6-b408-d95cb8e65b28 | -6.60796 | -41.56096 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| fdf8cffb-91bc-309f-aa0e-38c595fbb8b4 | -9.1043 | -64.37979 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bdea5ba7-ec45-3f9e-a3d0-77519470aeef | -9.96907 | -65.11844 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f5c2bf44-00e9-3aeb-8e73-99fd8b620631 | -5.68006 | -53.4987 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |


[Clique aqui para ver as próximas entradas](README113.md)
