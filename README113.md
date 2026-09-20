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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5334dfbc-155e-39ed-b2fa-a0376112fc4a | -12.7625 | -46.1572 | 2026-09-20 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 2872decd-4ab0-39d7-885f-017ecbc75b9d | -9.2603 | -45.939 | 2026-09-20 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a7fba86c-b06c-37f6-b8f6-848fd16f4923 | -9.8397 | -46.4361 | 2026-09-20 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 3c763c76-e98f-3465-ba8c-826a370ca2f0 | -14.6661 | -46.6919 | 2026-09-20 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 2455475d-b2d8-34e0-a375-3f5fc019ebdc | -11.379 | -51.42 | 2026-09-20 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 295.9 |
| 30892c4f-eece-3a4e-93f7-e40b9a92852c | -8.6357 | -47.608 | 2026-09-20 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c01ce2a1-d6f4-3948-a5dc-dffeb680328e | -10.6 | -50.2486 | 2026-09-20 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 71ca69eb-d145-3f43-abff-2ece4309a42f | -12.2847 | -47.1094 | 2026-09-20 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f803b5aa-bcf2-32ec-9740-7bec80e3a2dc | -10.3914 | -48.9133 | 2026-09-20 12:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 207a1816-c870-390c-afa6-6b150372a7e3 | -12.4841 | -50.0532 | 2026-09-20 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3d3e10d9-12f0-3de8-adfa-a42789515f54 | -14.1458 | -45.5638 | 2026-09-20 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7d250202-30a5-385b-8322-0c89dbaf9eba | -7.5337 | -45.4141 | 2026-09-20 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 41fb07e1-5382-3848-9125-70822f968226 | -10.2787 | -50.2605 | 2026-09-20 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a6018c4a-874d-346a-a6d5-a6d1d12d711e | -14.7051 | -46.6852 | 2026-09-20 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 62f3337f-4757-3235-992e-7b86c363d8e4 | -12.1328 | -47.041 | 2026-09-20 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| d3073a23-f16c-39be-ad06-80486112f97d | -11.118 | -54.0268 | 2026-09-20 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 172.2 |
| d10cec62-e789-3183-9709-0832e550b4da | -9.8313 | -48.4073 | 2026-09-20 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 945d8190-6523-3807-baf3-268ab26b8133 | -9.8502 | -48.4053 | 2026-09-20 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| ff81760a-9473-350b-9fd1-8a504fcb70d0 | -11.4537 | -45.3892 | 2026-09-20 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 163.4 |
| e1023e18-7cdf-3797-b4bf-733555621573 | -12.3404 | -50.6942 | 2026-09-20 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 99e35fb9-d5bf-396c-b77f-a837f8846349 | -11.1183 | -54.0062 | 2026-09-20 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| e5a5f7f3-75db-3b8c-9768-c05babb39211 | -12.2341 | -50.1703 | 2026-09-20 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ec8542bc-4c72-3751-adbb-9fd4304b8e6d | -12.1324 | -47.0635 | 2026-09-20 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a42a8ff7-e1a9-3b14-af41-81bbc7aa2a48 | -11.6609 | -43.4239 | 2026-09-20 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| b9fa61ab-ecc8-360c-b58e-12c5b060bc8d | -11.0991 | -54.0285 | 2026-09-20 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.2 |
| abb606de-c5e0-30ea-8115-96dc69c2d261 | -11.3787 | -51.4412 | 2026-09-20 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 776f4e70-ce9b-3e0c-b17c-a233ba72ae8b | -8.3727 | -47.589 | 2026-09-20 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ebaaba02-02f2-3549-bd0a-2a3d94d22919 | -7.211 | -44.0252 | 2026-09-20 12:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 07095e7c-e527-34c8-9665-b3de948fee31 | -8.6354 | -47.6301 | 2026-09-20 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 91bac273-e903-3911-ac9d-fd61ca693fec | -11.4924 | -45.3608 | 2026-09-20 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 29445f8c-e0d8-33fa-8b8c-8e213384d931 | -7.5522 | -45.435 | 2026-09-20 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| ab27fb96-59e0-3c67-bd40-da4a56972d91 | -12.7621 | -46.18 | 2026-09-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 404.7 |
| 69ea622e-2a54-31c9-862c-fb5e6d213194 | -12.6423 | -50.9144 | 2026-09-20 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 692f01ca-ab92-38d1-a2d9-e21e078a00ad | -12.7616 | -46.2029 | 2026-09-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 573.7 |
| 2da385fe-bd7e-31c9-a65a-cf2352dde6f7 | -8.8636 | -45.9596 | 2026-09-20 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b9ebb8e3-f2bd-3e16-bbf1-a6ada54c2abf | -12.1711 | -47.0356 | 2026-09-20 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3e25c33a-1bd2-3b47-8678-154957b32729 | -7.5334 | -45.4367 | 2026-09-20 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 32106c4a-a6c3-3012-bece-bd6fcbe7dcea | -12.7625 | -46.1572 | 2026-09-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1a9f9bf8-a658-362a-b660-d0bf98891f31 | -12.152 | -47.0383 | 2026-09-20 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| b2c421cb-1f65-3444-8a30-fbd100d9ee53 | -8.9752 | -44.6722 | 2026-09-20 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 4e598db4-ef82-3b9d-b0af-cb830ac19f58 | -12.7428 | -46.183 | 2026-09-20 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f5463472-7d34-334e-9431-940f3707d7fc | -6.9225 | -42.9088 | 2026-09-20 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| b313532c-ea11-3d46-aca3-d52cc0295611 | -11.3793 | -51.3989 | 2026-09-20 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 73c95825-0d9c-3c88-8bd9-ce3700e8a6b9 | -12.642 | -50.9359 | 2026-09-20 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 53fae80c-4dba-3c31-8853-43e4ca8683cb | -7.3259 | -55.6153 | 2026-09-20 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3737ee4a-7659-3a97-8521-220023336f59 | -12.2344 | -50.1488 | 2026-09-20 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d40163df-7a4b-3118-8cbb-427fffa74582 | -8.8639 | -45.937 | 2026-09-20 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 326b68ba-49b1-35ed-a6e5-6a0263977b6d | -9.2603 | -45.939 | 2026-09-20 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9f8b4083-0c91-35ce-99ab-25d60646512f | -11.398 | -51.418 | 2026-09-20 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| f75d89fe-b232-32cd-b05a-56230ca40584 | -11.2118 | -54.0797 | 2026-09-20 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d95a9c22-6858-3b28-8c5f-f548c7c4282c | -14.6856 | -46.6886 | 2026-09-20 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 01505a09-4c86-3548-bb58-d0993f57016a | -12.642 | -50.9359 | 2026-09-20 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 0d5cd612-528c-3ad7-a7a6-3c5bdb5c66a6 | -10.3914 | -48.9133 | 2026-09-20 12:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 36d84d3c-0be7-3cd0-936d-b0fd333c526c | -11.118 | -54.0268 | 2026-09-20 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 6ab44675-c740-387f-bc02-e2f431bc6468 | -10.3171 | -50.2138 | 2026-09-20 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 596e42b1-0bc2-3b64-8032-dfb670d7be85 | -10.3168 | -50.2352 | 2026-09-20 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 1a03d65b-f5e6-3317-a931-95ef770c462b | -9.84 | -46.4136 | 2026-09-20 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 065a11df-f4f2-3b89-bd1a-07affd4fc96d | -6.778 | -47.8545 | 2026-09-20 12:40:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| ffa96328-3e62-3bc0-821c-ace1220403ed | -10.8364 | -50.9479 | 2026-09-20 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 6bb0d6d8-b296-3394-8739-840a1d4a7016 | -11.1183 | -54.0062 | 2026-09-20 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f61b6fa7-1457-3c41-ba0a-09a4f8892139 | -14.6861 | -46.6657 | 2026-09-20 12:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f3da1857-3ba6-3eb5-8db2-46750118ab9f | -8.4317 | -45.8241 | 2026-09-20 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2c9d4a0c-242d-3814-87e3-bbb1400f6ca3 | -9.2606 | -45.9164 | 2026-09-20 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 761edeb0-cf71-35c9-b7c0-bac01f4a4105 | -11.4714 | -47.776 | 2026-09-20 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 795dbaa2-4d80-3700-abb7-c7e18f8e946f | -7.3259 | -55.6153 | 2026-09-20 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 048e8c3a-eb4a-3f47-918c-2e33a2f9a4ae | -10.8093 | -50.1621 | 2026-09-20 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 91d39457-6241-3361-a6e2-b5f199dab0cb | -12.1324 | -47.0635 | 2026-09-20 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 624d2ccd-1164-3f70-b7d2-b7f063234fbc | -12.3404 | -50.6942 | 2026-09-20 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 4d1b7810-4b07-3dca-9b53-166471f1b76b | -8.8639 | -45.937 | 2026-09-20 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| dd9db073-fa57-3655-91e3-27c57bee6e95 | -12.7616 | -46.2029 | 2026-09-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 320.8 |
| 5ea96ac8-080d-3ff7-b173-1f9472289f10 | -11.0256 | -48.3164 | 2026-09-20 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e1927190-e73a-3d14-8e1a-aa9c8274396b | -11.3793 | -51.3989 | 2026-09-20 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b043581a-2514-32ee-8d3c-1378dc76523f | -11.4541 | -45.3662 | 2026-09-20 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 200f50c8-3a62-3f66-8a53-9361689c07be | -12.2341 | -50.1703 | 2026-09-20 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 6d7a311e-03e5-31c7-b9f1-08b698cb0f0f | -11.0994 | -54.008 | 2026-09-20 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a00315f7-0f0f-3110-aed1-6b8c1ceeda61 | -10.7899 | -46.3429 | 2026-09-20 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 9766d734-a9a5-3d02-b877-90836df33feb | -11.2118 | -54.0797 | 2026-09-20 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7ab6eb06-3088-38da-9b48-58d2b8bbe750 | -11.8739 | -47.657 | 2026-09-20 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 880f9000-97c5-3f58-896f-e51d7526d897 | -11.0991 | -54.0285 | 2026-09-20 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 990f41e7-fb1f-3c7d-a37d-f7bb3dfeb265 | -11.6609 | -43.4239 | 2026-09-20 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| eba804a0-fddb-384e-b35b-04c798333159 | -10.473 | -51.2808 | 2026-09-20 12:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ce377a23-2c9c-3a0d-8c6d-e8068a686575 | -12.4837 | -50.0748 | 2026-09-20 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| f5f61abb-a916-3197-b4a0-c86c9c3d451a | -12.1711 | -47.0356 | 2026-09-20 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2b5f4bb7-8f8b-32bb-ac11-2785c933a737 | -9.8313 | -48.4073 | 2026-09-20 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 34567896-4f1b-3b94-9c7c-7a169ed39e6c | -10.6 | -50.2486 | 2026-09-20 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 7747d18a-e179-3bcf-a4ce-587ca8240a19 | -9.2603 | -45.939 | 2026-09-20 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 0264b196-3316-3a65-b13f-d5bd56109785 | -7.5337 | -45.4141 | 2026-09-20 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 74dbd2c8-2576-32ea-a70e-b1544538a4bb | -10.8367 | -50.9266 | 2026-09-20 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f99e2ee8-a265-3339-a2b9-959f960232a0 | -12.1328 | -47.041 | 2026-09-20 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e664ffa3-5b1c-33dc-9cfb-7a959d9d89af | -6.9225 | -42.9088 | 2026-09-20 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 9f5c86b9-6874-3764-a049-e9366b38acf3 | -9.8502 | -48.4053 | 2026-09-20 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d18db5bf-b3ca-3c65-9517-47341ced2eda | -10.2787 | -50.2605 | 2026-09-20 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| cdac505d-9723-3494-b661-db284e09b229 | -7.4286 | -44.7409 | 2026-09-20 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| afc8f3be-8747-3464-af3c-10188ec4d371 | -8.4314 | -45.8467 | 2026-09-20 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 9b191360-7722-3e23-9a33-3a80e927eda0 | -9.26 | -45.9616 | 2026-09-20 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 219bc288-a814-33e5-ae34-ad3e7229e144 | -11.3787 | -51.4412 | 2026-09-20 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| f5cd35f6-e9ba-3c93-893d-18a968693743 | -11.379 | -51.42 | 2026-09-20 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 245.8 |
| adeedeb8-f495-3e26-bb73-a74164bc93b8 | -12.4841 | -50.0532 | 2026-09-20 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 18160216-75b8-3a68-b2f4-3d2bce6ed3ca | -11.8735 | -47.6793 | 2026-09-20 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| cdf60b9f-bfcf-3f57-add1-69f38ccb7911 | -7.8191 | -45.1145 | 2026-09-20 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |


[Clique aqui para ver as próximas entradas](README114.md)
