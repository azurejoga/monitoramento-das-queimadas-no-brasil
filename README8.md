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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 551a991d-d3a9-3880-bd0e-0d0dd03cea30 | -6.5254 | -46.9074 | 2025-10-30 00:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 2d5b947a-aa46-3b00-b35c-a9a8be5af342 | 0.2852 | -51.1906 | 2025-10-30 00:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e0062453-9e54-3380-8589-e2feff7bd57e | -13.3932 | -54.3345 | 2025-10-30 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 90941649-f79e-3747-b7bd-4c11b8533c73 | -4.2832 | -59.6554 | 2025-10-30 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 28c1095c-a016-3aea-add1-17e7fd8a9cce | -8.3125 | -47.9236 | 2025-10-30 00:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 05055483-0ee3-3f2f-b6bf-17f9c3932a83 | -3.2132 | -46.8723 | 2025-10-30 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f88a4f02-a652-373b-bb1c-c13280e4e83d | -13.3743 | -54.3159 | 2025-10-30 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 456d2482-1a13-3ac4-9974-f7ea21786a90 | -3.2316 | -46.8936 | 2025-10-30 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 5568fa71-0c67-3c43-ab8c-c1dad363ee07 | -3.2317 | -46.8716 | 2025-10-30 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| a5328477-ee57-33a6-9434-06907068e2ed | -6.5254 | -46.9074 | 2025-10-30 00:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a1749995-b818-32d6-bb58-6d6becfa9f69 | -11.1563 | -51.0839 | 2025-10-30 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 81c040a6-39e1-3654-a19c-2fa7fe287e07 | -12.5141 | -50.566 | 2025-10-30 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f15372fe-c95c-3894-bb22-bcce7d96138b | -12.5138 | -50.5875 | 2025-10-30 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 09bb06d9-9ec1-34fd-bce1-801c475bd4a8 | -8.3125 | -47.9236 | 2025-10-30 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7388c846-b586-3c4f-943e-3868900f8e0f | -4.2832 | -59.6554 | 2025-10-30 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 26bdb039-31a5-3525-994e-4e91166ae0ee | -13.3743 | -54.3159 | 2025-10-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 4b8685d5-65fc-3e8a-becc-ffceb6ce31b7 | -9.4952 | -40.3834 | 2025-10-30 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 109.6 |
| e08b6c50-56f5-314a-a8aa-0dd562836f6f | -8.3311 | -47.9438 | 2025-10-30 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 40130709-795b-36bc-a3d9-20274ff32186 | -13.5316 | -44.341 | 2025-10-30 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a9682f1d-8e81-31d1-95ad-638f198b8a0d | -6.0108 | -41.9708 | 2025-10-30 00:50:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 73476e09-f1cf-3177-9f71-d45b95dfa039 | -3.2316 | -46.8936 | 2025-10-30 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8e650877-df13-3641-abd3-091f3f0fa63f | -8.3313 | -47.9219 | 2025-10-30 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 211.4 |
| c9ded703-e402-38b4-86c8-697a9ee5db6c | -4.2648 | -59.675 | 2025-10-30 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| cb302901-95d8-361d-8f5e-03b8e94d1e35 | 0.3036 | -51.2113 | 2025-10-30 00:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 1890c3d0-4a87-344f-b88e-4ef2290f55f8 | -3.2132 | -46.8723 | 2025-10-30 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| cd58ae37-30ce-3fd3-b498-0dfdc010daa2 | -2.7741 | -45.3989 | 2025-10-30 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 17867b6a-e750-3289-a834-acacfd2de79d | 3.1461 | -60.6886 | 2025-10-30 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5b79c065-fdb2-3d44-a5e9-aa2ddb00908f | 0.2852 | -51.2114 | 2025-10-30 00:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 61d493c8-8da6-3a2b-85b2-2151478e6ef3 | -3.7867 | -43.9011 | 2025-10-30 00:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c536ecbf-919f-3ef2-83e2-088979be1fd2 | -4.2831 | -59.6745 | 2025-10-30 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b9c2536c-7862-32b6-bcfb-7f63b2758445 | -7.4898 | -45.9818 | 2025-10-30 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f2107274-221a-360b-9189-53458d71074a | -4.2649 | -59.6558 | 2025-10-30 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 133.8 |
| ef1a21fe-513f-32b7-8c89-885812878dcc | -9.4956 | -40.3586 | 2025-10-30 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 5e2b8ed9-bd00-3a16-9754-4316b4f16cc6 | -15.6064 | -46.5242 | 2025-10-30 01:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| dd98f39b-b7f1-36e5-a21d-c3d91b15bc2e | 3.1461 | -60.6886 | 2025-10-30 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f98f580f-0ac7-3f12-9df7-8637974bb7dc | -4.2831 | -59.6745 | 2025-10-30 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7ae85994-26c3-3653-b64d-fcfbb2668c19 | -8.3125 | -47.9236 | 2025-10-30 01:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d82fec8d-f48c-3a9b-8b97-a96d4e1bc669 | -11.1373 | -51.0859 | 2025-10-30 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 543d3993-2867-3b08-8b7b-4e2065615032 | -11.1563 | -51.0839 | 2025-10-30 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.8 |
| b94337c8-5590-380c-a3c9-27a0293611cf | -13.3743 | -54.3159 | 2025-10-30 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ce409888-9647-38ab-9a44-3d2121104414 | -9.4952 | -40.3834 | 2025-10-30 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 111.2 |
| b060b24d-841c-31a7-8374-f2a71c21dbe9 | -11.156 | -51.1051 | 2025-10-30 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| cc6e1458-5640-3831-9bc0-ce25c75cbef9 | -11.137 | -51.1071 | 2025-10-30 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 165c2be0-4640-3612-9453-aef92a1d488c | -2.7741 | -45.3989 | 2025-10-30 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d56e4815-9e29-3032-a030-2897452ba29a | -12.8345 | -43.4448 | 2025-10-30 01:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| bc89c99e-1cd5-3a41-b4f8-eda30dcf6598 | -4.2649 | -59.6558 | 2025-10-30 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 389d6f39-b821-3b37-ae2a-7d58d33ac97a | -3.2132 | -46.8723 | 2025-10-30 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 729e743b-6c56-3581-ac0b-8eeaa5f790e3 | -13.5316 | -44.341 | 2025-10-30 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 48876e2f-6c71-3326-be43-1eebd949cf7e | -8.3313 | -47.9219 | 2025-10-30 01:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 5860264e-e8bc-3a95-9d0e-1b58a8642a94 | -18.2451 | -42.6313 | 2025-10-30 01:00:00 | GOES-19 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.1 |
| 6d127d99-278e-386d-9af6-1f943809cb4d | -11.1566 | -51.0626 | 2025-10-30 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 2b9f6fc4-ec38-3037-b676-f99d7bd9ca86 | -4.2833 | -59.6362 | 2025-10-30 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d9445f26-3f98-395e-aba4-78c45d2d5850 | -13.3932 | -54.3345 | 2025-10-30 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 37d2fe03-b0bc-3c9f-a1e0-5114904a67a6 | -12.8152 | -43.4481 | 2025-10-30 01:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| fac5d942-438a-38bf-9118-d5d4e43ff186 | -12.5138 | -50.5875 | 2025-10-30 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a755d06e-2e21-3670-8a7d-aeb3971b8851 | -4.2648 | -59.675 | 2025-10-30 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3c454644-4c7e-3d90-9259-f4eef275caec | -6.0108 | -41.9708 | 2025-10-30 01:00:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| c9016b79-e1bf-3c5a-9161-8f647b5e6231 | -12.3273 | -50.3096 | 2025-10-30 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 53e9b937-e744-3c07-9fff-4cfb3927cb3d | -12.4947 | -50.5898 | 2025-10-30 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 2219148b-7c70-3e38-8109-9d113accd7be | -3.7867 | -43.9011 | 2025-10-30 01:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 7e1e5cb5-3945-39d2-85b0-02a30b250a81 | -8.3311 | -47.9438 | 2025-10-30 01:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| c4576107-1c27-3a25-be9d-5f824d6ca7ea | -4.2832 | -59.6554 | 2025-10-30 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 31822281-39bf-3d9e-a418-2e34c96fb56a | -9.4956 | -40.3586 | 2025-10-30 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 8e713c46-01b0-3c11-bfae-7d67169f924c | -12.5141 | -50.566 | 2025-10-30 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3fbc8689-25f3-3eb1-ab52-41adeb9b946a | -3.2317 | -46.8716 | 2025-10-30 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| f12b051b-becd-34c1-aa19-8b73a945a235 | -18.2458 | -42.6063 | 2025-10-30 01:00:00 | GOES-19 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| 888a12ab-a80b-35f2-a393-df512bde4b83 | -6.5254 | -46.9074 | 2025-10-30 01:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 384d1e39-1ee7-3fe1-8aa3-9c2d343147ca | -12.5138 | -50.5875 | 2025-10-30 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| cfdd2aaf-072c-3ead-a156-c6edd8d229b0 | -11.1566 | -51.0626 | 2025-10-30 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| d360ed05-e8f8-3b77-a18d-dfaebe9ad3fc | -12.5141 | -50.566 | 2025-10-30 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 2cb0af55-7138-30fc-b757-95526741dbbf | -6.5254 | -46.9074 | 2025-10-30 01:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| e92c452e-2fd9-3b1b-945a-10c5ff2c2801 | -18.2451 | -42.6313 | 2025-10-30 01:10:00 | GOES-19 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| 5fd80f24-3ca9-3232-88aa-38295c20366f | -3.8054 | -43.9002 | 2025-10-30 01:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 0664e07f-1f74-383e-96a4-35dbda77387f | -12.495 | -50.5684 | 2025-10-30 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f26bc46b-cbfb-331c-aef6-9d4928ef9195 | -8.3125 | -47.9236 | 2025-10-30 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e0ffb844-0e05-33f2-9532-e9c7b9e9ca63 | -17.6934 | -40.249 | 2025-10-30 01:10:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 133.0 |
| b4571204-7166-3f9b-9784-04fc652ddd02 | -3.2317 | -46.8716 | 2025-10-30 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 5e9c927d-706c-3461-872a-ee2cf1d0d579 | -12.8152 | -43.4481 | 2025-10-30 01:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 3f807a54-6394-39c4-b03c-be566bc6fa93 | -8.3313 | -47.9219 | 2025-10-30 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 642a30da-e475-333c-ad32-3c24df1af0b1 | -9.4952 | -40.3834 | 2025-10-30 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 3eb13341-f372-3e81-91cf-f27c1abbeea6 | -17.7137 | -40.2435 | 2025-10-30 01:10:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 114.1 |
| bd5fd9c1-c11f-3a21-b27f-2effb2fbd4b6 | -11.1563 | -51.0839 | 2025-10-30 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 3c96fd9a-bc77-3067-b038-ae1de367344f | 3.1461 | -60.6886 | 2025-10-30 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9b91dc12-dde3-3aa9-a5ca-325279e121ba | -3.2132 | -46.8723 | 2025-10-30 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f27f2556-125b-312f-9cd7-decb086eebe1 | -9.4956 | -40.3586 | 2025-10-30 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.0 |
| e5d8deea-e9d0-3d4b-8e55-b3475d3d817f | -8.3311 | -47.9438 | 2025-10-30 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| eb9d1ba8-d565-333d-90ab-eb302312d362 | -12.4947 | -50.5898 | 2025-10-30 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e9be47eb-d1a1-3193-9a42-165b8f93aaac | -15.6064 | -46.5242 | 2025-10-30 01:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5ab0506b-e05d-3faa-8175-457732f7a3cf | -10.6502 | -52.1873 | 2025-10-30 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0ec98062-6d65-3775-9185-6fb08851e867 | -4.2649 | -59.6558 | 2025-10-30 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 19acb187-c52a-39ae-89e2-6c2de880134b | -11.1373 | -51.0859 | 2025-10-30 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 4d279325-568f-3aa4-bf15-b2bc5b0bc4c6 | -10.6313 | -52.1891 | 2025-10-30 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1e40307b-6f64-32c3-b86a-38a16b1b157b | -13.5316 | -44.341 | 2025-10-30 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e4324cce-e027-3d88-8588-4031b4d276b2 | -4.2832 | -59.6554 | 2025-10-30 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 66c95214-b344-3768-8081-693e8e2521cc | -6.0108 | -41.9708 | 2025-10-30 01:10:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| e056f2f7-0971-3f92-bb30-8da9829bf1a8 | -12.8345 | -43.4448 | 2025-10-30 01:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ce7ad330-e5fb-3504-9e10-6b66b2649414 | -2.7741 | -45.3989 | 2025-10-30 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4ea5387a-2032-38fa-a271-eb373c4c6887 | -4.2648 | -59.675 | 2025-10-30 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fddc6e82-2107-3474-8155-6f4101b41704 | -11.1376 | -51.0647 | 2025-10-30 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| c18a1ebc-d523-343a-83e9-adf8ac6a0414 | -18.2451 | -42.6313 | 2025-10-30 01:20:00 | GOES-19 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |


[Clique aqui para ver as próximas entradas](README9.md)
