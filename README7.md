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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f21910e2-4e9d-3eea-964e-8b71001b803d | -10.7819 | -46.208801 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aeafab2c-f26e-3649-b1f9-affae1854a6f | -7.0642 | -42.112099 | 2026-09-15 00:02:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2d3f1f81-953e-3810-874e-6897edb2ce69 | -7.0739 | -41.807301 | 2026-09-15 00:02:00 | METOP-B | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c903e79-493d-395a-97b1-1a0fd5e75049 | -8.7869 | -45.866901 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a87e496-0edd-365f-a96a-e004c0f21d59 | -2.9057 | -50.394199 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9b5f04b-74ed-3d22-b245-e913a67de5b5 | -6.7827 | -46.4366 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1361b23-b3fd-3869-bd7b-efe8dc0fdd9c | -7.1599 | -43.518799 | 2026-09-15 00:02:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bfd2de08-8cf3-3d5b-8a7f-091cc8fac824 | -10.7835 | -46.215801 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6aa58dfe-4d82-3c44-a4bd-5ca2ad660a81 | -5.8925 | -49.947399 | 2026-09-15 00:02:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc6169f-0bdd-3bb6-a65c-277eee799ccd | -7.5468 | -46.851002 | 2026-09-15 00:02:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3463b572-ab19-3758-af27-c03412a38e13 | -7.6125 | -47.278301 | 2026-09-15 00:02:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e6f2279-7162-394d-8a2d-657565cf9a69 | -10.7506 | -44.804501 | 2026-09-15 00:02:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d93c8d2d-1c22-3eb6-9933-1956e048d607 | -4.2991 | -49.079498 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 767cc980-d2e2-3745-ab0f-ed4b3235f47c | -6.3309 | -44.118401 | 2026-09-15 00:02:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 941e365d-23c2-31f9-9f16-2ebc15e4c189 | -6.7271 | -48.105 | 2026-09-15 00:02:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 59ec4b32-0fa8-35e2-a693-87c1a184712f | -1.6839 | -55.853699 | 2026-09-15 00:02:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d8aad24-bc7b-345c-ba2d-5b5728eb97db | -4.6571 | -42.078098 | 2026-09-15 00:02:00 | METOP-B | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 90908079-2228-3438-8c55-d44391899fb2 | -7.2241 | -46.156898 | 2026-09-15 00:02:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 643b7f93-5451-3fb9-aa11-11c7a6b53605 | -13.7273 | -48.965 | 2026-09-15 00:02:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66a6f281-e16e-3470-8894-cc576034f645 | -5.0202 | -43.581001 | 2026-09-15 00:02:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cdbd584-d1c4-3de3-978c-acc6fce6ec2b | -8.5428 | -54.6661 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df67459-4ba3-3fae-9179-7b273c50145a | -9.6368 | -47.672798 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 095d4847-8c33-3c9a-981c-813bf6399912 | -6.1598 | -52.711899 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5140fbc9-7f48-32a4-8ba7-e2dffc4af013 | -10.8513 | -46.2882 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a08e6de-e7d6-3d06-846a-5977d5197abb | -14.2184 | -47.370098 | 2026-09-15 00:02:00 | METOP-B | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a23e8468-2ce4-3e29-8b6f-b36c7320cad4 | -5.5993 | -44.830299 | 2026-09-15 00:02:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61f6472a-1a82-39c7-987a-bd5a11dcf5fc | -13.3016 | -43.696899 | 2026-09-15 00:02:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8151bcbd-6485-35a5-a958-57159f7298f5 | -3.1816 | -61.1235 | 2026-09-15 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d58c0812-aba8-371e-9171-f1c72091fc53 | -13.2424 | -51.672 | 2026-09-15 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| e77af533-fd2b-3c32-af8f-7c05660c4a8e | -5.1255 | -55.955 | 2026-09-15 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 32ce1161-07af-39be-a254-07d3f86275f5 | -13.2232 | -51.6744 | 2026-09-15 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 42e5c007-88a4-326e-a419-28a5fb649ab3 | -11.8836 | -43.8378 | 2026-09-15 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4fa125d7-c17f-3399-9616-fd82841599fe | -2.6784 | -57.5698 | 2026-09-15 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 951d9a74-8880-33a5-8bf2-56ee6085f942 | -6.6953 | -58.6903 | 2026-09-15 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 7bc1bbf7-eec6-3dd5-b756-3fb9e1a84112 | -6.6952 | -58.7097 | 2026-09-15 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1da32d97-f2d6-30c1-93be-83cd9c98d1a5 | -6.1109 | -57.684 | 2026-09-15 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c3b8e7da-2581-3349-9276-82e37e07aa14 | -6.7382 | -48.1187 | 2026-09-15 00:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 107.9 |
| dcc1468f-e072-3a29-9208-9d9893bcf623 | -2.6783 | -57.5893 | 2026-09-15 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 8112547c-48b2-317c-ade8-fd7254f8e0a1 | -6.7195 | -48.1201 | 2026-09-15 00:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 159.9 |
| c0761825-24c8-342a-8289-adb45710ada2 | -11.884 | -43.8142 | 2026-09-15 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 63039662-b12d-37a8-8d1a-a224512ea04f | -6.1108 | -57.7035 | 2026-09-15 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 2f8a3e69-2825-3712-a233-2a519f37fde9 | -13.2235 | -51.6531 | 2026-09-15 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5a049b05-1c0b-30ef-b0e2-d5d419a434bd | -10.5788 | -47.7306 | 2026-09-15 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 54dc783e-ca18-395f-8116-6aff2c65a999 | -4.6776 | -42.0713 | 2026-09-15 00:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 129.1 |
| 09e348d6-f729-3df7-bec7-10ef6fb8a9e9 | -14.8474 | -49.242 | 2026-09-15 00:10:00 | GOES-19 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ba7fab26-2690-371b-84ee-657bcd399370 | -4.6774 | -42.0951 | 2026-09-15 00:10:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 148.9 |
| 2677751b-1835-3191-8a6e-9b860e372ab7 | -10.5785 | -47.7528 | 2026-09-15 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5e812d61-d27a-34be-aea0-d596ea8009a8 | -3.4272 | -58.2138 | 2026-09-15 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| df776423-6445-3dce-938d-f3064dd0e12e | -5.1256 | -55.9352 | 2026-09-15 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a88aff25-61a1-378a-a45d-ee51cad615dd | -15.2827 | -42.783 | 2026-09-15 00:10:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 87.5 |
| e220077f-b08a-3889-add6-c371fad510c5 | -6.6768 | -58.6911 | 2026-09-15 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e1d1fd68-3970-3d6b-837c-8395323bec0d | -8.0924 | -50.9642 | 2026-09-15 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 36a44849-4f0e-312c-8975-7b509b8c7894 | -18.0249 | -50.299 | 2026-09-15 00:10:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d145c638-30f4-3de8-8ec3-3d12574652aa | -2.9025 | -50.4214 | 2026-09-15 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 66527e30-c374-337b-82a7-c93232740d2f | -5.4297 | -43.9869 | 2026-09-15 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| d56095a4-2086-38f8-8e68-821e5406ff49 | -2.9209 | -50.4208 | 2026-09-15 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 54e3d5f0-0ec7-3a14-b357-49a0793e97a3 | -14.8469 | -49.2641 | 2026-09-15 00:10:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| cd8b9486-21d6-35eb-9f20-aeafca210b36 | -4.6589 | -42.0726 | 2026-09-15 00:10:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| b57bbb8a-34a6-33a3-8c1a-4b48f299e8b2 | -18.0254 | -50.2767 | 2026-09-15 00:10:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f5884605-5061-3fcf-927b-8b38ce91da38 | -3.3493 | -59.8288 | 2026-09-15 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 41382445-73f2-3ae1-8939-0d92fbe1013a | -2.6966 | -57.5889 | 2026-09-15 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 134fca52-11c1-333b-8b9a-b89a58620cae | -3.382 | -61.3279 | 2026-09-15 00:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a96bcfcb-9868-376a-bdaf-3af6c0f09af0 | -4.6587 | -42.0964 | 2026-09-15 00:10:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| 4da2d3da-f417-36a2-9fe2-1aa9860a9d44 | -8.5126 | -50.1481 | 2026-09-15 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3a72e9b6-ece2-3365-a529-c0250b195ed6 | -4.66 | -42.11 | 2026-09-15 00:15:00 | MSG-03 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4e865a8e-34fe-30fe-b3f6-6a5223a05bc1 | -6.6952 | -58.7097 | 2026-09-15 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e8553aea-cbf6-3ef3-b8b1-6ef57c9c92d3 | -5.1255 | -55.955 | 2026-09-15 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b3dde671-0991-3796-98dc-da69c2418a44 | -4.6774 | -42.0951 | 2026-09-15 00:20:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 158.5 |
| 533a41fa-7a5a-3204-931e-8ae391111a63 | -4.6589 | -42.0726 | 2026-09-15 00:20:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 1b9171fc-b46a-339e-ac89-11a8d148b481 | -6.1108 | -57.7035 | 2026-09-15 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7e066128-a112-3218-9e42-4c1b66e8811a | -3.4272 | -58.2138 | 2026-09-15 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d455b952-2a5c-3a4a-b140-1ada90f1e2fa | -13.2232 | -51.6744 | 2026-09-15 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 9569eb16-4082-3123-a08e-a8c0889ff606 | -2.6784 | -57.5698 | 2026-09-15 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2cf9a441-6059-3761-8f94-78d6e054a12b | -9.5343 | -40.3282 | 2026-09-15 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 160.6 |
| 3ff95b71-2ef9-301b-92cd-55a6623279e3 | -6.6768 | -58.6911 | 2026-09-15 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 0611c904-47af-316e-99be-59ed8218e3ee | -11.8836 | -43.8378 | 2026-09-15 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8c883952-9152-3f13-a18c-bad187573437 | -11.884 | -43.8142 | 2026-09-15 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| adb25f99-e86b-3fa8-b9f0-0cf17ce33c64 | -8.5126 | -50.1481 | 2026-09-15 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d6dc5480-c38a-38b0-9624-46837f254e1c | -4.1865 | -48.6788 | 2026-09-15 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6087b596-3253-37c2-90cf-ebcbabe019c0 | -5.4297 | -43.9869 | 2026-09-15 00:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 172.7 |
| f9d0f3fa-3e11-3fac-8f30-c01fe065b7a7 | -13.2235 | -51.6531 | 2026-09-15 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 0f386d1f-e16c-3b9a-ba75-ff2ca67b0c88 | -15.2827 | -42.783 | 2026-09-15 00:20:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 570e9d38-05e8-3a62-bc2f-16328c69b381 | -6.1109 | -57.684 | 2026-09-15 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 25a67c80-7fc7-397e-9dcb-bba485f1be98 | -6.6953 | -58.6903 | 2026-09-15 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 530946cf-5401-338e-99fd-f22a8f51a1c4 | -2.9209 | -50.4208 | 2026-09-15 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| af91132e-1cd6-3313-8048-75bd1eec91fa | -6.0731 | -57.861 | 2026-09-15 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| f9fdbfd7-88a2-3a3d-b838-d92119010d0a | -3.1816 | -61.1235 | 2026-09-15 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5db6059b-bfef-3120-8d09-3791e2bfc5f0 | -6.9612 | -44.5316 | 2026-09-15 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4d7dff23-3897-345e-948e-574d44a57d5e | -18.1709 | -51.7685 | 2026-09-15 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8f28f661-d3cb-397f-883c-5612157d582c | -4.6587 | -42.0964 | 2026-09-15 00:20:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 11633e73-d41a-3ef8-99ab-008dc87cbf87 | -3.382 | -61.3279 | 2026-09-15 00:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d51e5f4a-69a4-3116-91a9-095ac86bde1a | -6.7195 | -48.1201 | 2026-09-15 00:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 35e8a6ba-b272-3348-a8a5-c32b7fbe17d3 | -9.5152 | -40.331 | 2026-09-15 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 5b873d48-3af7-3902-ab65-af8484859279 | -5.1256 | -55.9352 | 2026-09-15 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ecd8e58b-3bee-39d7-8117-2722fed3f12d | -4.6776 | -42.0713 | 2026-09-15 00:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 3177b4a1-0b82-3e2c-b5a1-607aec4558f7 | -2.6783 | -57.5893 | 2026-09-15 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| eaedbf09-188d-3f40-9039-226438a3843c | -2.9025 | -50.4214 | 2026-09-15 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 11edea8b-4a16-3322-a01e-d385c4a2e1ab | -2.6966 | -57.5889 | 2026-09-15 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| bd94547e-ec14-36ff-8296-7bdc1f1d319a | -8.0924 | -50.9642 | 2026-09-15 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| f17336bb-c67b-3222-b70d-b5039aefcdb4 | -13.2962 | -51.2775 | 2026-09-15 00:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
