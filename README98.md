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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49200558-47dc-325c-971f-e6c4563cdb44 | -7.1384 | -42.1529 | 2026-09-17 15:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 224.6 |
| f6e709c8-29cb-3a20-bf13-731ce6ed7c69 | -13.2986 | -51.7501 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 9f51fe97-69e8-3ebf-9a73-adf1a1b51271 | -13.3758 | -51.7193 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8cd1a57c-6643-3bac-89a9-e19540a6e07c | -9.1055 | -60.9895 | 2026-09-17 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 33f4b4ed-9add-3fbe-b3d6-5d0207ae43ac | -7.5798 | -46.3321 | 2026-09-17 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 52b05bf5-19ee-305d-b300-3db16d6e1c15 | -12.7713 | -51.2189 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| f6138b4f-7bab-3b58-aea1-ae80e9e7e8fb | -9.5522 | -48.1086 | 2026-09-17 15:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 64d28fae-29e5-3a7f-b8a3-18baba919036 | -14.8376 | -59.5515 | 2026-09-17 15:20:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9d5d0084-e42e-3d80-bc17-5ede3d872d6a | -6.6021 | -58.849 | 2026-09-17 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| d2f28b4a-8989-320c-af80-4dab1d285ff0 | -8.58 | -44.5552 | 2026-09-17 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 248.3 |
| 9d73f79e-0b7f-3779-a4a2-5de284ea740a | -8.4796 | -57.6478 | 2026-09-17 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 184.2 |
| 400a0bdf-bf35-36f4-9b75-73d5e3559cd2 | -4.5045 | -54.9646 | 2026-09-17 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| a235b06c-9bc0-3b1b-a1d8-61b88e290d4a | -5.7419 | -51.7422 | 2026-09-17 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 286.2 |
| f904e45c-8139-3821-b8cb-d1ad74a890fd | -11.2677 | -54.1361 | 2026-09-17 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1d3f76c4-075b-38d2-be01-0e08dc4ef99a | -10.0418 | -45.5756 | 2026-09-17 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 253.9 |
| 26272a86-450a-3d86-8658-31bdb92eb486 | -9.7794 | -60.4551 | 2026-09-17 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| fe6cd39c-cc9a-3e69-b7a5-0caa68e36d3f | -10.3772 | -49.9508 | 2026-09-17 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3200e8a8-c16b-3ee4-9455-b640ec6d8741 | -13.3185 | -51.7051 | 2026-09-17 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 05bdb137-e21d-3ef8-ab12-e9319635078a | -11.2491 | -54.1173 | 2026-09-17 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 15680a23-ae90-3b55-961f-52e43996ed58 | -6.7863 | -58.8995 | 2026-09-17 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0f74b25e-16ae-3626-a072-676284c0f485 | -6.3198 | -59.9572 | 2026-09-17 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| d1e60782-7177-3177-b459-a04b0d32aeb1 | -11.2488 | -54.1378 | 2026-09-17 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| db4145a9-3aa1-38bc-adf5-3b029b24f4cd | -11.3442 | -43.9906 | 2026-09-17 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 288.9 |
| 50077eb9-bb67-34c8-b59e-7488494429ed | -9.7608 | -60.4561 | 2026-09-17 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 3e92258f-632d-3487-a767-44bc589551ee | -9.3763 | -50.1139 | 2026-09-17 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| a44951da-6c07-3014-bd58-fa531499bc32 | -5.2023 | -49.3348 | 2026-09-17 15:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 61f84e1e-369f-3255-b5c6-6e2f19263c03 | -6.7648 | -59.4408 | 2026-09-17 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 70bcadee-54c4-3f4f-9c46-47a488b70259 | -8.4797 | -57.6282 | 2026-09-17 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 385162df-c5d9-380e-a099-766e02b01112 | -6.67 | -43.657 | 2026-09-17 15:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ac3dbca9-515d-31fa-94c1-bdd507862785 | -11.3638 | -43.9642 | 2026-09-17 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| e84141b4-d433-323c-9436-b90138574d47 | -11.3629 | -44.0112 | 2026-09-17 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 62360817-d6a7-3bb5-8037-0de99d3548a8 | -8.7949 | -46.9069 | 2026-09-17 15:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| a95302d9-596c-3c40-bc94-eafd0191b7e4 | -6.0256 | -59.9293 | 2026-09-17 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.5 |
| fca929ef-27bb-3607-b153-2f030a434363 | 1.261 | -50.872 | 2026-09-17 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 8a5cf817-b2a7-3730-81eb-df0693ef8ffb | -12.0464 | -49.9776 | 2026-09-17 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| bb3bbda4-a255-3550-8407-f984644d0f6f | -9.376 | -50.1352 | 2026-09-17 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| b4b201ce-f01c-3905-944e-bf77c09fd6ef | -12.6442 | -54.7007 | 2026-09-17 15:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 08f4126c-c2ec-3a44-a5da-e89dc1bdc734 | -7.6417 | -45.8331 | 2026-09-17 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| b22affe0-f5b8-30b3-bb3d-35ee25cf6dcf | -9.3941 | -50.1974 | 2026-09-17 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 017c45c3-0379-3a90-a9ee-b62c62919d1f | -11.3276 | -47.2386 | 2026-09-17 15:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 8d991782-50de-3d00-80a3-81cdf5c9e989 | -11.2677 | -54.1361 | 2026-09-17 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 549476f1-1f5b-34de-b9b1-046b2615948b | 1.4083 | -50.8285 | 2026-09-17 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a62e8071-fb66-32f2-a975-338f819f0815 | -7.8224 | -44.8404 | 2026-09-17 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.4 |
| d326cf36-5101-30eb-a362-78b30c8a98d2 | -12.0273 | -49.9799 | 2026-09-17 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 0c4dcd24-be27-3785-b1df-8f8f98bcaa52 | -8.5611 | -44.5573 | 2026-09-17 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 165.7 |
| ba7f2bdb-4576-3bd4-97a4-34313ae8c8f4 | -12.6826 | -54.6763 | 2026-09-17 15:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 3bbba761-abd6-3acf-ad6c-4402fdccdf39 | -6.0255 | -59.9484 | 2026-09-17 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.1 |
| d0d4375c-2ab1-372f-82c4-53864291b9c4 | -8.58 | -44.5552 | 2026-09-17 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 294.9 |
| f2f6404c-e699-3eb4-97a9-5d64e0d98c20 | -9.1339 | -51.5927 | 2026-09-17 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e0f394bc-8598-31c2-90a9-153ed4e79182 | -6.2916 | -55.2895 | 2026-09-17 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d5d226d9-fbc4-31b0-994a-637751cf04c9 | -10.1168 | -45.6346 | 2026-09-17 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| beb60235-d4fd-39aa-b7fa-ea73d33bebef | -9.769 | -46.0841 | 2026-09-17 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 066d406d-531c-3cac-bd14-4e53cba5e0eb | -4.5229 | -54.9639 | 2026-09-17 15:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 1ddf18db-9b71-3cbc-a969-71ffdb4d85ee | -11.2302 | -54.119 | 2026-09-17 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bbdbc38f-8af6-3b85-9d73-a9b06c7bd584 | -7.8227 | -44.8175 | 2026-09-17 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 351.7 |
| 163f7c80-f063-308f-92f2-a187cb39ddbb | -9.3954 | -50.0908 | 2026-09-17 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 90a9dbbb-2063-388a-b81e-0e0cdb89fea3 | -9.3758 | -50.1565 | 2026-09-17 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 58204322-ada5-3de8-900b-142c1b2d2420 | 2.1818 | -50.9193 | 2026-09-17 15:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 78.6 |
| bb330cdb-83f0-3334-8a58-774697aa96ca | -8.4983 | -57.6271 | 2026-09-17 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 247.7 |
| 6be41cd2-e025-3ab4-ae0b-2ac5bbdf24cc | -8.4669 | -44.5445 | 2026-09-17 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| b6e53373-ffa5-3e38-82c2-b8d8a562906e | -14.8376 | -59.5515 | 2026-09-17 15:30:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4101c0df-573a-3a8b-af16-bb749b45e862 | 1.2609 | -50.8928 | 2026-09-17 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 45bddf38-f570-3d39-87f2-1a89372eca98 | -9.7497 | -46.1089 | 2026-09-17 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 926cdf56-763a-3f1a-9f61-ec3417259065 | -8.475 | -46.8943 | 2026-09-17 15:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b892a9c8-06e1-3549-97e8-a47066dc3674 | -9.8322 | -48.3417 | 2026-09-17 15:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 8ed9d138-c3c2-3045-94cc-c95bd0e93daf | -11.9165 | -49.7558 | 2026-09-17 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| baca9bfc-d36f-3795-a13b-c2d149ebe83c | -6.6766 | -58.7299 | 2026-09-17 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 9378ee49-b1c9-3ca0-9724-0fc9cdb883d1 | -8.5797 | -44.5783 | 2026-09-17 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| f44c5c2a-405c-3e16-8113-150f45b12a17 | -10.9108 | -48.3739 | 2026-09-17 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 04445d1d-75b4-366f-ac40-3c8ce595de16 | -7.1384 | -42.1529 | 2026-09-17 15:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 267.4 |
| 0a93c160-900a-3f7e-8004-1649d09cd3d9 | -4.3754 | -55.0288 | 2026-09-17 15:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3eb6766e-4c9c-3cb1-94fd-5c3a9a7949c8 | -10.0542 | -50.1123 | 2026-09-17 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| dc4fbfa0-e581-361c-aac5-6555eb9a096b | -14.8183 | -59.5532 | 2026-09-17 15:30:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 8fbacd9f-c3ce-3bb7-9525-ea887d38986e | -9.5512 | -45.4296 | 2026-09-17 15:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 630918b3-a681-3dfa-a0f1-7776525303da | -6.3198 | -59.9572 | 2026-09-17 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 5a27c3ec-1cc8-3733-aeb6-ccad51903c4d | -9.3765 | -50.0925 | 2026-09-17 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 880254cd-4658-3cbd-be53-41a17ba173f2 | -9.3564 | -50.201 | 2026-09-17 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 9e0304de-08d4-3bd5-948d-da4390e42e44 | -1.4578 | -54.2166 | 2026-09-17 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6c6a3f60-06be-35da-8f1d-2b9c0050a6db | -8.58 | -44.5552 | 2026-09-17 15:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 2d166b49-79aa-3e31-8d92-411c90320462 | -7.8221 | -44.8632 | 2026-09-17 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 9c146cc6-46ec-32f6-9920-a18297d0bcbf | -8.5431 | -44.4902 | 2026-09-17 15:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 164c2c3f-8bea-396f-8af8-ba43b9fab1fd | -4.5228 | -54.9839 | 2026-09-17 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1ba2602b-a09b-342f-82c0-4cac4b1051d7 | 1.2611 | -50.7679 | 2026-09-17 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5b056db7-d8ce-3c92-b2b0-5f699a6c266b | -11.2693 | -54.0129 | 2026-09-17 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4c82342c-4758-3264-8af2-724eb82d709e | -7.8224 | -44.8404 | 2026-09-17 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 207f5b34-33d8-3f29-9bf9-8bbda13a10cf | -8.8647 | -45.8693 | 2026-09-17 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 7df6ff83-748a-3c9c-bb3d-60ab9d428e5b | -12.0461 | -49.9992 | 2026-09-17 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ad61aaf2-46f9-33fd-8550-652599f4b195 | -9.5512 | -45.4296 | 2026-09-17 15:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 25016487-a648-371f-98bd-8e45beff969e | -12.0464 | -49.9776 | 2026-09-17 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| e7745707-db1b-3ea4-bccf-43945eba04ef | -6.1108 | -57.7035 | 2026-09-17 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 1c7a24f9-374a-31fa-84c5-4f3fc5ea52d1 | -9.8322 | -48.3417 | 2026-09-17 15:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 792aec92-3ef6-3acb-8fcb-b9c0b6326774 | -8.4797 | -57.6282 | 2026-09-17 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 833d6c8c-a204-37c7-baed-1b24a1faa4ed | -1.4578 | -54.2367 | 2026-09-17 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fc4c0b4e-4f6d-3c93-b310-37b470745528 | -6.0196 | -51.7893 | 2026-09-17 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 651c5390-6b44-319a-bb1f-1e0b93b7f841 | -5.1255 | -55.955 | 2026-09-17 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d790c10b-6256-3eab-b5ae-b8b975770d5a | -9.7608 | -60.4561 | 2026-09-17 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 23a8d8ae-d50d-3fa4-96c0-0cb0d219a7fd | -9.3758 | -50.1565 | 2026-09-17 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 889255fa-70a7-3f9d-9e77-47601fcba63a | -9.4139 | -50.1103 | 2026-09-17 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ad53291e-7011-3e3e-b1b4-0b9cef269d40 | -10.9108 | -48.3739 | 2026-09-17 15:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 3befc5eb-3add-3da5-96dc-cbc1739ee645 | -14.8376 | -59.5515 | 2026-09-17 15:40:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |


[Clique aqui para ver as próximas entradas](README99.md)
