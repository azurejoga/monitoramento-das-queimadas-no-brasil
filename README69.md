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
| a3a82289-4abb-36fd-b5ad-4fe4246c5e51 | -10.8492 | -46.1998 | 2026-09-16 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 903b2f44-e0e6-38ec-bff0-a4c031a08db5 | -10.8495 | -46.1771 | 2026-09-16 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 05bc79bf-1b62-3503-8091-a2d778c2ffbe | -8.5428 | -44.5132 | 2026-09-16 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| f0ca574c-2792-32f1-8929-42daa1895e0c | -10.8571 | -50.8183 | 2026-09-16 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 15debbfd-8e1f-3588-8758-bb02f9b3fb35 | -11.4167 | -51.4371 | 2026-09-16 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 131.2 |
| ef1a3ad3-cd7a-3498-9e88-0b62dff1c4c9 | -8.8585 | -44.9149 | 2026-09-16 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 27f2044c-a3dd-3bab-bd5e-19f4f1e2465e | -10.876 | -50.8163 | 2026-09-16 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 65dfb242-083d-3a73-ba56-4c0b162c7905 | -12.3277 | -47.9513 | 2026-09-16 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6b9b8512-3857-38d7-ad2e-2515ee68e0f5 | -9.2311 | -46.7055 | 2026-09-16 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d2ce69e7-0fd5-34a5-b385-23c6cd9bf42a | -10.0982 | -45.6141 | 2026-09-16 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 0fa2f057-e7cf-3b54-8076-8916987a2634 | -6.8032 | -59.1693 | 2026-09-16 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 60a78f14-8113-303b-acff-cf58a1cd4799 | -11.5436 | -46.852 | 2026-09-16 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d48565cd-a795-30e8-bd30-19992fb5915b | -7.3561 | -44.4956 | 2026-09-16 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.0 |
| d0f0a506-ccdb-3925-95a5-daa4d3734fc2 | -5.144 | -55.9345 | 2026-09-16 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7cd07d73-7f0e-3703-8bf0-1339a1971f3d | -7.0265 | -42.0446 | 2026-09-16 12:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 21f775a8-952a-3d78-a6de-80cbf4aff41b | -13.1855 | -51.6365 | 2026-09-16 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 260.4 |
| ac5fa0e3-193b-37c1-be8e-58877d9051e9 | -3.48579 | -54.6726 | 2026-09-16 12:44:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 0c115f35-cfca-3dbd-9151-84c44e27d70e | -6.60733 | -58.59582 | 2026-09-16 12:44:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b12511b6-3ea0-3f5e-9512-f48bbae73273 | -3.59058 | -58.54468 | 2026-09-16 12:44:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e9020659-156a-34e3-b277-7b47a5c6db7a | -5.96925 | -57.78051 | 2026-09-16 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 61f58b0a-f2ad-3359-a758-83d55370b2d5 | -6.02638 | -57.77329 | 2026-09-16 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 06028d70-add2-391d-92c8-6e0ee57b4cf6 | 1.43618 | -56.09396 | 2026-09-16 12:44:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| bb3f0f1d-7339-3616-bc3d-551b8cd154df | -3.17571 | -61.11051 | 2026-09-16 12:44:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a66a720f-d86a-3909-8d85-e0b08fb1001a | -6.02832 | -57.7589 | 2026-09-16 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 830afbc7-6ba6-3227-82cc-da68be1abe52 | -6.71476 | -58.795 | 2026-09-16 12:44:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1d3e25e7-63fc-3342-ae4d-5b3cf5400507 | -5.14613 | -55.9459 | 2026-09-16 12:44:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 549f53be-1e74-3df2-980c-9ece0e5e761a | -3.59982 | -59.07352 | 2026-09-16 12:44:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 81b9327c-ad6f-36c7-af35-864ec61c9c30 | -3.12776 | -61.25712 | 2026-09-16 12:44:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d1d87b3-c46e-3809-bcdd-8640bc4882dd | -2.43874 | -57.86452 | 2026-09-16 12:44:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 991ee0a0-11ac-34f9-9906-2d4e059ed221 | -3.53774 | -59.07012 | 2026-09-16 12:44:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 643a21ef-9455-3eed-9d5f-2c9e4595eba2 | -1.29137 | -55.71189 | 2026-09-16 12:44:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| ffd95a0f-8e47-3149-b650-53ba6b994dd7 | -6.85272 | -62.88574 | 2026-09-16 12:44:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 3437056c-e8b5-3bc0-8472-a174dcd92964 | -6.81776 | -59.16293 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1ebc96eb-553b-3c20-9991-bd5b4415e9f0 | -6.35453 | -62.68837 | 2026-09-16 12:44:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e8367166-3dd6-3e05-a903-84705dc7ce3d | -6.80612 | -59.17331 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 207.6 |
| 543d4cbf-94f1-3b5f-ab4f-e0d39645f50c | -6.32684 | -59.99729 | 2026-09-16 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8ca21d5f-1e19-3766-b49d-ffbd312377c8 | 1.32472 | -60.71479 | 2026-09-16 12:44:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa868eaa-0a87-36bf-b700-9ace1f8a0517 | -4.12284 | -60.67842 | 2026-09-16 12:44:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aa094232-2335-351b-a092-28da9e612731 | -1.73474 | -55.24116 | 2026-09-16 12:44:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 3a0684ae-f84f-3cf7-9584-780dfb75ecaf | -4.12155 | -60.6876 | 2026-09-16 12:44:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 53bc26a6-8f97-3c31-a496-e9d75fab0b32 | -6.02557 | -59.9318 | 2026-09-16 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ca13e03d-82d6-3375-927e-536d746b195c | -3.59217 | -58.53313 | 2026-09-16 12:44:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d9e303e2-73d5-3bad-9690-b3caabc46205 | -6.71308 | -58.8073 | 2026-09-16 12:44:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 32aeb241-0e33-3c99-bd30-a8ed73e6a4ac | 1.39511 | -50.80428 | 2026-09-16 12:44:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 0829e215-eb09-3940-9706-a496a3b6410d | -6.76302 | -58.80735 | 2026-09-16 12:44:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| bd179f3b-2752-38bb-9a37-8d1593981e36 | 2.70588 | -60.2997 | 2026-09-16 12:44:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 3e43f771-5204-3c8e-a22e-d1c9d20026fe | -3.18457 | -61.11172 | 2026-09-16 12:44:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e00fd61d-3ea6-3ef7-bee9-0daa8f0e77e4 | -1.61218 | -55.55957 | 2026-09-16 12:44:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 8eeb4f5d-ef87-31cc-a749-1207035f6e4e | -6.85145 | -62.89458 | 2026-09-16 12:44:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 435d1e04-f51d-3f21-960e-3e0748e9ee54 | -5.4577 | -60.22292 | 2026-09-16 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3e9e44f9-8b85-37be-ab9b-e549d5bec6d5 | -3.12283 | -61.41795 | 2026-09-16 12:44:00 | TERRA_M-T | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8230d72b-5f03-360b-9b3b-f11e8f362075 | -3.12901 | -61.2483 | 2026-09-16 12:44:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| def1bd6d-0cd8-394f-acf6-fabb085c5d83 | -6.79451 | -59.18359 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| cac9131d-2212-3a61-ac60-2812cbdff101 | -6.77588 | -58.94533 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dd4948f1-ca30-364e-980c-0497eb026db6 | 1.43836 | -56.10201 | 2026-09-16 12:44:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 37057b74-0f4b-3749-9c09-df8d65f0204e | -6.81462 | -59.18629 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 1678d347-2547-3dac-8f3e-27592a68f06e | -6.81618 | -59.17468 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f615de9e-da25-312b-a9d6-e4cb543a0ae8 | -6.79606 | -59.17191 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e862f343-8b7d-39a1-a764-fe49dbcaf005 | -6.78409 | -58.88472 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3172ca30-5443-33d2-8d74-4bd789512c4f | -1.28412 | -55.72258 | 2026-09-16 12:44:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 9530d100-f899-3109-a448-cbe2b8ebc69f | -6.32806 | -62.68467 | 2026-09-16 12:44:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ff2b6bf7-80a8-3aaf-a948-23533c375000 | 1.43823 | -56.10857 | 2026-09-16 12:44:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 8780c06b-da21-3f44-b083-844469aea84e | -4.52059 | -54.97002 | 2026-09-16 12:44:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 14f23d9e-4acd-305f-9e15-1590e7fff2da | -5.79373 | -59.85688 | 2026-09-16 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2a9a1aca-d8ab-3741-ab0f-445eb08e2452 | -6.78244 | -58.8969 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9aebd356-d5d1-3e14-96d3-874321f9132c | -4.28215 | -55.75101 | 2026-09-16 12:44:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1629b3c9-78e6-3e69-97f5-cce80eda7a08 | -6.35327 | -62.6972 | 2026-09-16 12:44:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 5b4d2e78-84af-3480-8f2e-6d72b79f184f | -2.4405 | -57.85214 | 2026-09-16 12:44:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3d2de6f8-d3e0-3d00-ae31-b668e2943524 | -5.80323 | -59.8582 | 2026-09-16 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 372d8959-8e38-3c27-b7a4-ceffd6f9d43a | 2.71468 | -60.29848 | 2026-09-16 12:44:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 737ed9dc-fc1c-3f9d-94aa-ef1f828c8aed | -1.28659 | -55.70544 | 2026-09-16 12:44:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| a33b4945-4edc-3239-8ff2-2bbec9ac2d66 | -3.70692 | -60.61866 | 2026-09-16 12:44:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| dbb6146d-515a-3722-8c34-276acb85bd2d | -1.73408 | -55.23536 | 2026-09-16 12:44:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 7c15e704-95a3-36fd-a0b3-707ecf30fd2c | -1.60975 | -55.57724 | 2026-09-16 12:44:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 38ad91ef-cbf5-39d4-924c-e1a78f7f7779 | -5.75338 | -57.58724 | 2026-09-16 12:44:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 17caaebc-d55d-3986-b398-b4610d8b07a2 | -5.14871 | -55.92641 | 2026-09-16 12:44:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| da307e01-660e-353e-952b-dd859dd1d7b9 | 1.39207 | -50.81185 | 2026-09-16 12:44:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 6786d101-d91f-3589-84d5-661ecd324529 | -6.80456 | -59.18494 | 2026-09-16 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 0a058209-af06-3753-9369-ec21a5b3358c | -3.3524 | -61.29152 | 2026-09-16 12:44:00 | TERRA_M-T | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9163d945-2094-3de2-babd-0e368ea57920 | -9.10599 | -65.56318 | 2026-09-16 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 84ebb105-7ebe-34c2-b9d4-1fbb1b862065 | -7.65778 | -67.16444 | 2026-09-16 12:46:00 | TERRA_M-T | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f27c1cd5-114b-38e7-a52c-a2c4f863414c | -9.08929 | -61.0133 | 2026-09-16 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 260f5ae1-3e14-3754-ab3e-cbc2000cad25 | -9.14278 | -65.84209 | 2026-09-16 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 2843b7c7-737e-3ce1-b3bc-7d5522238542 | -10.95225 | -58.59785 | 2026-09-16 12:46:00 | TERRA_M-T | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 62133839-d4ad-3cb3-8174-dc9ec993cbe0 | -12.10588 | -57.18967 | 2026-09-16 12:46:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bac4f566-f50c-3400-bdf5-f263c3c36f41 | -9.09446 | -61.04409 | 2026-09-16 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| b29e92ff-29b1-3a5c-a10c-221dd9b74d27 | -11.81221 | -60.46336 | 2026-09-16 12:46:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3b7ce8f9-516f-30c2-9da0-1277de734dcc | -9.37976 | -57.9947 | 2026-09-16 12:46:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 63491dfc-c978-3ea1-a217-698dfe7daec9 | -9.13307 | -65.84064 | 2026-09-16 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 3441deb6-7b8e-3fe9-b1dd-c137abe2fb07 | -7.5605 | -62.32558 | 2026-09-16 12:46:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ba79e396-9284-3724-bd5a-73895bc5a35c | -10.39144 | -58.32172 | 2026-09-16 12:46:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 240.8 |
| 6cc149f5-ca94-3a11-97fb-91d93e5ed0bf | -13.45878 | -54.57508 | 2026-09-16 12:46:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| d1587f68-fb14-337f-8daa-6cc8334258e9 | -9.0695 | -65.93204 | 2026-09-16 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 78b54688-11e3-39da-8236-36f5e9c8d217 | -9.02172 | -61.02414 | 2026-09-16 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ccaa79d5-ccc9-3d8e-baa1-121067b5eeae | -8.9276 | -61.44674 | 2026-09-16 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8c3e6c1d-6107-3933-a4f8-e11da84db49c | -10.39331 | -58.30663 | 2026-09-16 12:46:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 673.5 |
| f38d8bc4-2a17-330f-a6bf-6af8d2a6c240 | -9.09582 | -61.03428 | 2026-09-16 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| c5d6fb88-fc94-3e02-b7d9-ba12afe6a050 | -9.39336 | -60.30754 | 2026-09-16 12:46:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 541fe472-b816-3e8a-afc6-ff5bafc2a55b | -12.11865 | -57.19136 | 2026-09-16 12:46:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| b5429a30-0214-31db-a151-e07d817c5f56 | -10.89533 | -54.01576 | 2026-09-16 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |


[Clique aqui para ver as próximas entradas](README70.md)
