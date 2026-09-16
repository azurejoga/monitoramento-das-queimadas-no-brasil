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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59b2e5b9-d05e-3124-875c-924f4d8de2c6 | -13.2047 | -51.6342 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| bea14e4e-14e6-3a9d-9bfb-de2ec0dfca87 | -12.3085 | -47.9539 | 2026-09-16 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| e34af894-1569-3582-8f62-53588a7fad25 | -6.0184 | -57.7657 | 2026-09-16 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5775395e-225a-3b72-a3d0-286dbccd07f0 | -5.1255 | -55.955 | 2026-09-16 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b21c92b7-9f7a-3ff4-8268-31a929dd1aff | -12.7515 | -51.2639 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 923a0a8a-e7db-325c-a4fc-5923d4c1d638 | -7.2691 | -45.5737 | 2026-09-16 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bf1aad53-5278-3d36-9c91-63928bf90675 | -3.4182 | -43.1074 | 2026-09-16 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8e89a2f7-9e3c-3b8b-9dc9-1f0f1cda3132 | -15.4626 | -53.7761 | 2026-09-16 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b9ba70ea-598f-31a6-86e6-77845c8943ff | -2.6783 | -57.5893 | 2026-09-16 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ae727136-0d08-3d29-8477-430ae62c384e | -11.9033 | -43.8112 | 2026-09-16 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 6532fae0-b9d3-3890-8765-aadd0aaa7403 | -11.4167 | -51.4371 | 2026-09-16 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 759233a9-422a-3ce1-9b1e-b3dc695981aa | -10.6827 | -54.1679 | 2026-09-16 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| dc9daddf-e1a7-3e7b-a5db-c52b38b08cd7 | -9.2311 | -46.7055 | 2026-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 8156d095-0770-321c-9372-90a336ec842d | -15.5199 | -53.8317 | 2026-09-16 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 25a6f968-d00f-33ac-98ae-077853ade971 | -10.9107 | -54.0045 | 2026-09-16 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 8894dc30-a096-3069-8995-86b46c1e3733 | -6.1159 | -44.6932 | 2026-09-16 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| ed054349-0ed6-35f1-9b39-07bec7fb1b83 | -13.1855 | -51.6365 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| ba579334-0f78-3e59-b289-9599d8eeb5a5 | -10.3953 | -58.3159 | 2026-09-16 13:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 547.4 |
| bb5b16c6-1a53-3dbf-a250-7fb68ab1994e | -11.5432 | -46.8745 | 2026-09-16 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| ffd320ca-b6d4-3c1b-b101-693fef991e34 | -7.3561 | -44.4956 | 2026-09-16 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 556c1aeb-1325-3344-af71-b70f36da0ad1 | -6.789 | -48.6779 | 2026-09-16 13:50:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1d90e9df-57a9-38b5-879b-6e1beee3f5fe | -12.3273 | -47.9735 | 2026-09-16 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 09f5589a-637e-352a-bb85-ab5fbaf6ea1f | -10.3766 | -58.3171 | 2026-09-16 13:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 61f14744-b4a8-3ced-ac7d-14cbe7e613b1 | -8.5428 | -44.5132 | 2026-09-16 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 316.0 |
| 5d9756fe-98cc-3e90-bb64-bd873ebfcbe8 | -15.4817 | -53.7947 | 2026-09-16 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 7d57cf06-6c36-3352-84fd-a932d4e4550d | -11.417 | -51.416 | 2026-09-16 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| fbe2c708-e8b6-3eb1-b9bb-a9f8f237162c | -12.5341 | -47.0964 | 2026-09-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| eb33df14-9ce1-3aff-adfc-b9e386611f9e | -8.5617 | -44.5112 | 2026-09-16 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 01560fe3-1e17-358a-8ff0-f5566027e73d | -7.58 | -46.3097 | 2026-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 8ff77678-a225-3027-b2d0-cd835cef2a54 | -10.9105 | -54.025 | 2026-09-16 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 974c015a-d9aa-320c-8101-334cf57855b8 | -10.8916 | -54.0267 | 2026-09-16 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| f1d20ae1-4b4b-3949-b7e2-3036c4a331a7 | -6.8215 | -59.1879 | 2026-09-16 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.3 |
| f4fbdde8-8472-3ed3-a5e3-b1fdc7e6126f | -10.8571 | -50.8183 | 2026-09-16 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| be8b604f-1611-397c-b35c-f0d210260d8e | -10.1179 | -45.5662 | 2026-09-16 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 17939d25-7df9-3ad6-bccd-f92d795a5f01 | -2.6966 | -57.6084 | 2026-09-16 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 268.1 |
| 5c609bcb-ac22-3b5e-becc-b10beb36c14c | -8.6566 | -44.4777 | 2026-09-16 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 257.0 |
| bad86886-ed78-3f1c-852e-8fb9c01e947b | -10.3955 | -58.2962 | 2026-09-16 13:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 413.7 |
| 7da47f59-246d-3589-beea-b348e5976566 | -5.144 | -55.9345 | 2026-09-16 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| aa19dea9-9d85-35b9-812b-0cb181de1871 | -13.2235 | -51.6531 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f166eef4-faac-395b-9423-03f5df06bed7 | -9.7793 | -60.4744 | 2026-09-16 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4592e21d-8103-3923-803a-4b136581c864 | -13.287 | -51.2832 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1eb2d28d-88d4-39c3-8684-b7fd6a748ae8 | -15.5195 | -53.8527 | 2026-09-16 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 77e389e6-6e4d-32d7-ad75-bbdef88ff779 | -9.5725 | -46.601 | 2026-09-16 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 0846c7db-30bd-3ca5-9610-ab16eb51ac42 | -10.8495 | -46.1771 | 2026-09-16 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 27edbbb8-5c58-3ac2-845d-05c5f48b0a62 | -3.1661 | -53.9235 | 2026-09-16 13:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e12d55d1-9083-3ced-a7f4-2ac655ae23d5 | -15.539 | -53.8502 | 2026-09-16 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3eae609b-b4f5-37f7-9dfd-8005afe7ac99 | -13.2044 | -51.6555 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 84a7a72a-caf2-3133-8d61-678f1ccc16d3 | -12.4145 | -48.4701 | 2026-09-16 13:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| f9721f42-7264-373c-8f06-63c3a81d9835 | -11.5436 | -46.852 | 2026-09-16 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| e38c7cb4-58cd-3af3-89d8-50795b075975 | -12.7518 | -51.2426 | 2026-09-16 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8b7f0068-2456-3e43-adc6-d3f1e31f11f4 | -6.7705 | -48.6577 | 2026-09-16 13:50:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 7ee63386-176a-327c-8e6d-184922132256 | -15.5386 | -53.8712 | 2026-09-16 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 90f019c5-005b-3af2-af82-dd94597fe4cd | -15.4623 | -53.7972 | 2026-09-16 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 0bc5aa42-f988-3ec8-9811-6bddaf76ef3b | -4.8673 | -56.0632 | 2026-09-16 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 16921d1e-8325-31d6-baec-a69ca142430f | -12.3277 | -47.9513 | 2026-09-16 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 95ff4ced-d9a8-3e0c-a7eb-4448d17e2e1d | -10.3766 | -58.3171 | 2026-09-16 14:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 269.3 |
| 08969a35-9ead-3d91-ac6b-9687daf3daf8 | -2.6783 | -57.5893 | 2026-09-16 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8dbbeda6-d42c-3860-b0a6-1da8a1a2fd1f | -11.5436 | -46.852 | 2026-09-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 317a7fb2-3da8-37f3-8a90-70fcc4b93449 | -11.417 | -51.416 | 2026-09-16 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 002add8a-0775-3f8e-b900-72398acf82b8 | -8.5431 | -44.4902 | 2026-09-16 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 0ef92dd1-4eb6-3687-8d61-aaa90697ea06 | -6.8215 | -59.1879 | 2026-09-16 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 223.2 |
| 351e3096-5514-398a-bd14-975f74270bfc | -8.6191 | -44.4588 | 2026-09-16 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 298.1 |
| 323174da-fe04-39f3-b705-2796a3e75474 | -13.2047 | -51.6342 | 2026-09-16 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a85ce5b7-2b65-3c57-9696-e15cec0c6fc3 | -6.67 | -43.657 | 2026-09-16 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 80107cfd-7c3f-316b-a4fe-49739b89df09 | -13.2235 | -51.6531 | 2026-09-16 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 48373008-f0a5-3927-9ab3-04d4db94ff7b | -8.5617 | -44.5112 | 2026-09-16 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 178.0 |
| e2eb2929-ca3d-30fe-a5e8-8172b78d04d5 | -2.6783 | -57.6087 | 2026-09-16 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 190.9 |
| 8660e91c-55ee-3504-9405-aa90fabda5de | -5.144 | -55.9345 | 2026-09-16 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f4dec4a5-c6ca-3a4e-925e-e75e1d89b62b | -3.4645 | -58.0001 | 2026-09-16 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| f1daa6aa-4499-393b-ac9a-6a1bd626e13d | -13.6085 | -48.2794 | 2026-09-16 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| fb64fca2-735b-3483-acbb-10fe18571a0a | -6.7703 | -48.6792 | 2026-09-16 14:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 7a62fd83-bde6-3c06-8bf3-2b656b05ab26 | -12.3081 | -47.9761 | 2026-09-16 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 63b66e07-8c2f-3b6f-ae70-95a89ea01f29 | -10.3955 | -58.2962 | 2026-09-16 14:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 256.1 |
| 5c35e001-3e2c-3e62-9ebd-0eff27b30c76 | -10.8571 | -50.8183 | 2026-09-16 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 203.9 |
| eb57b3b9-400e-35ec-975e-faf131f6c996 | -11.5624 | -46.872 | 2026-09-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 6396d4a9-8c92-3896-a290-3b3a576f4c56 | -6.8216 | -59.1686 | 2026-09-16 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 888e6b15-4d39-3fac-886f-b6bc83df742b | -12.3277 | -47.9513 | 2026-09-16 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 241.5 |
| e41888e7-f5b0-3690-9657-0b5fff601466 | -11.9033 | -43.8112 | 2026-09-16 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 5c6aa5e8-117e-3cbd-a4e2-15a425c68cef | -11.5432 | -46.8745 | 2026-09-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 3ff57f14-63cf-36e1-9a5f-6f54e677e910 | -8.638 | -44.4567 | 2026-09-16 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 6ed43a78-3cf6-3660-841b-25dbf5f92334 | -12.3085 | -47.9539 | 2026-09-16 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 80417b93-72db-35b6-9ec4-c17cbc380cf2 | -6.344 | -62.6904 | 2026-09-16 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9da067cb-1f22-3771-845f-5ce6912afcb8 | -10.876 | -50.8163 | 2026-09-16 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 16eea59f-f0f1-3148-9ff6-12cecc104ce6 | -10.331 | -45.2883 | 2026-09-16 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 9bd6b1a6-2b69-34ae-8f95-515ca9c22903 | -8.6377 | -44.4798 | 2026-09-16 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 390.7 |
| c42ad249-799a-389d-b4bb-2e6aadfff4b8 | -13.287 | -51.2832 | 2026-09-16 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| c98a4237-7c88-38e1-a02c-a750e544d550 | -10.9107 | -54.0045 | 2026-09-16 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 358d77f8-fec6-3de3-b96a-ca9f90d833ad | -8.5428 | -44.5132 | 2026-09-16 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 407.2 |
| 32617b95-1101-30c2-b649-974c5e32a1de | -9.0866 | -61.0287 | 2026-09-16 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0cef17c9-61e8-346f-b357-5d0210aa1020 | -12.3273 | -47.9735 | 2026-09-16 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 744e45ca-67d6-3cd3-b742-7610a8d5f760 | -12.126 | -44.2225 | 2026-09-16 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f9af0644-9fb9-3db0-88d7-76dfa2330678 | -10.6827 | -54.1679 | 2026-09-16 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0aeb3d23-611a-352d-a10a-455bf82aac9a | -13.2678 | -51.2856 | 2026-09-16 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5a164b68-06ee-3604-ad38-074ea6e8dc3d | -6.1159 | -44.6932 | 2026-09-16 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 397335ec-0868-3c64-989b-8b9a1d3a9871 | -6.7705 | -48.6577 | 2026-09-16 14:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 226.6 |
| 9031811c-12bf-38f0-b47b-a038976656f3 | -11.4167 | -51.4371 | 2026-09-16 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| a1cff11e-a643-3de5-81eb-d6d2263fcf50 | -9.7793 | -60.4744 | 2026-09-16 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8e67658c-ac1a-383d-9bfc-238dbae724f6 | -15.6557 | -52.7366 | 2026-09-16 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9c3e6d86-217d-3028-b0e6-777ad2eac48d | -10.3953 | -58.3159 | 2026-09-16 14:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 369.2 |
| 0b0a9269-30ba-32b5-b2cb-000a2a2ed0fe | -12.1265 | -44.199 | 2026-09-16 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |


[Clique aqui para ver as próximas entradas](README74.md)
