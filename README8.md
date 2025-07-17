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
| 26752a63-f067-3258-8b35-26f1032dbb14 | -9.8857 | -68.363998 | 2025-07-17 02:00:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2a013f00-c750-3253-beca-7446c4997ba4 | -11.9423 | -63.839199 | 2025-07-17 02:00:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 738f0c73-58db-35d6-be58-c24d39cbf7fb | -11.94412 | -63.84499 | 2025-07-17 02:02:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 6cc374fa-10f1-3cc5-a5c9-fcc0bc7308c7 | -9.88731 | -68.36592 | 2025-07-17 02:04:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9a247208-d71e-3589-be85-a26e1c76055f | -8.1075 | -43.1411 | 2025-07-17 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| b881a546-50dc-3441-a81c-0e3a3a7ffe98 | -12.4198 | -50.4917 | 2025-07-17 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 689caacd-28c6-32fd-934a-f7737d12860d | -5.6567 | -43.7161 | 2025-07-17 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 429.1 |
| 07f906e0-aeb7-3ee0-99f2-79ed4bc749bc | -5.6754 | -43.7147 | 2025-07-17 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 77c2d766-113c-319d-af42-2484f1ca660d | -5.6569 | -43.6929 | 2025-07-17 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| fc6a3025-3864-34a4-b9e1-e2fb5f3b28cf | -3.3772 | -47.4792 | 2025-07-17 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 11181b85-1690-3133-8829-a9f85437ab8b | -6.7382 | -44.3215 | 2025-07-17 02:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 58c0f131-96f3-360e-8b41-29d11b079c61 | -3.3958 | -47.4785 | 2025-07-17 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 0e8dd3da-a45b-3e66-bd11-0c5951d43bdd | -12.4202 | -50.4702 | 2025-07-17 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a2f0245b-c0c8-3afd-ac5c-978b624d1e74 | -9.2449 | -48.5546 | 2025-07-17 02:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ec31c69e-48da-33db-8769-15a34958c8f9 | -6.7194 | -44.3231 | 2025-07-17 02:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e4ce06d4-e790-3b70-a16a-a95358acbe42 | -3.3957 | -47.5003 | 2025-07-17 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 9276d5ac-2576-36c5-b876-3a1724bda103 | -5.6565 | -43.7393 | 2025-07-17 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 77d34b37-3fe1-3d1b-9443-ecb37120513e | -12.4198 | -50.4917 | 2025-07-17 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1dc09c27-9bdd-32ed-85cb-a3d84d997e06 | -5.6565 | -43.7393 | 2025-07-17 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 8d78558f-cad2-3b80-8c0e-4a18325956dd | -5.6567 | -43.7161 | 2025-07-17 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 437.4 |
| 3386c3ee-357f-3106-9ba9-654ed8b18cd5 | -3.3958 | -47.4785 | 2025-07-17 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| df3882da-d591-30bb-b2eb-7ab4a135cd73 | -3.3772 | -47.4792 | 2025-07-17 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| c911ecb2-90b0-3710-a21e-655eaabab40c | -3.3957 | -47.5003 | 2025-07-17 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| df8584a6-e020-3e50-bc60-ada3e3a74afc | -5.6754 | -43.7147 | 2025-07-17 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 8d7eddfb-bbb5-3984-9f75-4eb0a88581d5 | -5.6569 | -43.6929 | 2025-07-17 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5068d46d-a4ff-3cac-b248-356ee0f71e16 | -8.1075 | -43.1411 | 2025-07-17 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| d5ebf124-cc31-3298-ad4c-fbb6dcaf8e35 | -12.4202 | -50.4702 | 2025-07-17 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 0c36dab9-5907-34bf-abfc-69a658f9d151 | -6.7194 | -44.3231 | 2025-07-17 02:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c1a93ce3-dfdf-3665-9235-dd16f149f161 | -9.2449 | -48.5546 | 2025-07-17 02:20:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 8d2cb3cb-741a-396b-af8c-57005ef3d7e6 | -11.8756 | -55.4467 | 2025-07-17 02:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 69431547-2781-3947-9f2f-d639edbb17ab | -5.6752 | -43.7379 | 2025-07-17 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e421a7af-ada4-3869-b554-7f80d923247d | -5.6569 | -43.6929 | 2025-07-17 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5d40028c-d9ac-3804-a067-51f8f3c89a46 | -5.6565 | -43.7393 | 2025-07-17 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 422a80e3-272e-31e1-8349-8450031a694d | -9.2449 | -48.5546 | 2025-07-17 02:30:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 884d96a9-5645-37a6-bc5f-e4bb98184070 | -3.3958 | -47.4785 | 2025-07-17 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 84e8aac3-de6b-3904-bbcb-45b1d96657c7 | -5.6754 | -43.7147 | 2025-07-17 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| b7f538cc-2066-3e0b-97a4-e9e28df3c6cc | -6.7194 | -44.3231 | 2025-07-17 02:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 2f044cdf-d718-3fcc-acd3-8024153e62bb | -3.3772 | -47.4792 | 2025-07-17 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 88e18990-10f5-3988-b195-2ddc94b4dfdd | -5.6567 | -43.7161 | 2025-07-17 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 355.3 |
| ab6b1a11-f4cd-3b47-b762-f670610d0e22 | -8.1075 | -43.1411 | 2025-07-17 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 4c9d8b9a-f4f2-3c6a-8d9e-e0e090dcaf4b | -3.3772 | -47.4792 | 2025-07-17 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b7b67319-2981-34df-8914-7530c8f63f8e | -5.6569 | -43.6929 | 2025-07-17 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b4ad0b73-8a68-357f-afa0-9a68c41c8a4e | -5.6567 | -43.7161 | 2025-07-17 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 385.0 |
| 1718a472-b7dc-3e6a-952f-739be3a1d88f | -3.3958 | -47.4785 | 2025-07-17 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 5ee8ce90-5a62-3f3e-abce-7357473e26c2 | -8.1075 | -43.1411 | 2025-07-17 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 6366fcdc-90de-3b00-b579-795524471063 | -6.7194 | -44.3231 | 2025-07-17 02:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6779a7a9-b262-324e-9656-26dcabf816b9 | -5.6565 | -43.7393 | 2025-07-17 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| b0151457-e0aa-3240-86be-85e101683f5c | -20.9815 | -48.9311 | 2025-07-17 02:40:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| ed2ba454-b1bb-3175-aa5f-a49fa5605fc6 | -5.6754 | -43.7147 | 2025-07-17 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 184.1 |
| d8664c76-1c68-3603-bde7-b3a08a71e918 | -9.2449 | -48.5546 | 2025-07-17 02:40:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b9165f4e-29dd-364d-8bd8-107edf7edc5a | -3.3957 | -47.5003 | 2025-07-17 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f5c1395a-7b0a-3f51-8fcb-05c779231029 | -3.3958 | -47.4785 | 2025-07-17 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 90307aa6-0863-3c4e-b96a-6fed4f1cf35b | -5.6754 | -43.7147 | 2025-07-17 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 0cdbc0e8-0a0c-30f0-a8d9-e1d21c607637 | -5.6567 | -43.7161 | 2025-07-17 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 298.4 |
| 3fb4c647-fc29-3c16-add5-970d4dcf7795 | -5.6756 | -43.6915 | 2025-07-17 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1216c88d-df12-3bfd-ae1b-3ada2e7b2fcf | -9.2449 | -48.5546 | 2025-07-17 02:50:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d36951b0-6f56-39f5-b04b-a6156cb651ed | -6.7194 | -44.3231 | 2025-07-17 02:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 33ecd0ce-faa3-326d-9588-2a1c1b87130a | -3.3772 | -47.4792 | 2025-07-17 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| dfbe33c3-5d61-357d-aaa3-3da74c18b0dd | -5.6565 | -43.7393 | 2025-07-17 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 11027e5d-9088-3409-b228-e6f387537235 | -5.6752 | -43.7379 | 2025-07-17 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6059cadf-5d5f-35af-9f0e-165d8fd6f2cf | -5.6569 | -43.6929 | 2025-07-17 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b24c0494-ecde-38a6-aced-7ddbea08a439 | -5.6565 | -43.7393 | 2025-07-17 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 3936e6d8-3c17-39e1-a2d0-234f5a41b52c | -3.3772 | -47.4792 | 2025-07-17 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 7127ef4a-b2ce-38ac-b972-f67283dec603 | -5.6752 | -43.7379 | 2025-07-17 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| cdaadd9d-dfe4-30d4-b83e-bc153fc603fe | -5.6754 | -43.7147 | 2025-07-17 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| e99c8981-8a8b-3879-804e-7f79b5a74174 | -5.6567 | -43.7161 | 2025-07-17 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 374.3 |
| 4332652e-ef5d-331c-912e-8e7bf4689f6a | -6.4654 | -45.3475 | 2025-07-17 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d87c285f-9c61-3fd0-b10c-7251ac403d73 | -6.7194 | -44.3231 | 2025-07-17 03:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 05b1b2b2-331d-3e88-b280-82d19ea47e10 | -9.2449 | -48.5546 | 2025-07-17 03:00:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| bb478434-9d76-3465-904e-4578ff1c15f1 | -3.3958 | -47.4785 | 2025-07-17 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 82f84ab3-0fa0-36d5-aeaa-4974cb34a577 | -5.6569 | -43.6929 | 2025-07-17 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3fa2d262-8f0c-3f28-a5f1-fe69a58f2736 | -3.81018 | -38.68399 | 2025-07-17 03:04:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f9c85f81-1cf9-31cc-be17-2822cb5db0fc | -19.74761 | -40.69562 | 2025-07-17 03:08:00 | NOAA-21 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| aaeaf4de-57fe-3714-b660-c28d0eccb4d9 | -3.3772 | -47.4792 | 2025-07-17 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ede750e7-23ba-3c78-96db-14f6dce6b12d | -5.6569 | -43.6929 | 2025-07-17 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4be4f96b-65a7-3d06-b362-a4c8d91b1b7a | -20.961 | -48.9358 | 2025-07-17 03:10:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.8 |
| 1409f6a7-3382-3ec1-a680-7cfe64173435 | -9.2449 | -48.5546 | 2025-07-17 03:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| d4e546a1-e925-366b-850b-882a135041c3 | -5.6567 | -43.7161 | 2025-07-17 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 385.2 |
| aa992633-e76f-3ba8-8e02-010fa4c83021 | -11.122 | -46.9969 | 2025-07-17 03:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| aa3b4cad-df1d-3e90-89a9-a5b637ac27a2 | -3.3958 | -47.4785 | 2025-07-17 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d72fe38f-6328-3e00-b834-f44f096e0813 | -5.6565 | -43.7393 | 2025-07-17 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 4d490885-2806-3a45-9c99-88960b14cd14 | -20.9809 | -48.9543 | 2025-07-17 03:10:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.6 |
| 13d4a57b-ed5a-3231-8db4-7d703e9f1cc1 | -6.4654 | -45.3475 | 2025-07-17 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 1a75b107-3c96-31ca-835d-7cde5efd5c41 | -6.7194 | -44.3231 | 2025-07-17 03:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 83a07e40-8530-3542-bd3f-985e3a07e24c | -5.6754 | -43.7147 | 2025-07-17 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 95810406-2453-3608-84bc-1822304c5613 | -5.6756 | -43.6915 | 2025-07-17 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 47a59cb9-03b6-3b04-a93c-b8a75eb5cb3e | -20.9815 | -48.9311 | 2025-07-17 03:10:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| c0f04cbc-8c67-34e9-9701-cb287c49cd0f | -22.69958 | -43.34782 | 2025-07-17 03:10:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7e042a1a-fe9b-384e-9873-2adfa481ae8f | -6.7194 | -44.3231 | 2025-07-17 03:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f05d77b8-2c31-35be-8543-9dc377bf6a27 | -5.6569 | -43.6929 | 2025-07-17 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 70276452-a9d7-32d3-a515-fbbf30a61c42 | -9.2449 | -48.5546 | 2025-07-17 03:20:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b39c4e96-618f-33c5-8f56-be0f2eba7b5f | -5.6567 | -43.7161 | 2025-07-17 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 369.8 |
| 1a328376-60c8-3a6d-8b81-5aa2a94bd57d | -3.3958 | -47.4785 | 2025-07-17 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7560dd11-8de2-34cb-8cc3-8e720a1f5675 | -5.6565 | -43.7393 | 2025-07-17 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 96d5e531-56f5-36e7-9790-ed065a270d01 | -5.6752 | -43.7379 | 2025-07-17 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c96b7e92-2d71-3035-ae40-8d334b46b661 | -5.6754 | -43.7147 | 2025-07-17 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 347d859e-3b9e-3c96-a9c6-c0ff96a983d0 | -6.4654 | -45.3475 | 2025-07-17 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c4bac810-a107-3dd9-a374-f45727293e2e | -3.3772 | -47.4792 | 2025-07-17 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 6102bf33-ceb1-361f-abd4-01c40e0be2d9 | -6.7194 | -44.3231 | 2025-07-17 03:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 40b5737f-05b4-3f6f-ab03-86c6f8614f09 | -3.3772 | -47.4792 | 2025-07-17 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |


[Clique aqui para ver as próximas entradas](README9.md)
