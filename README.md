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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83860f0d-52f6-36d5-835c-9a45201c09e9 | -6.7382 | -48.1187 | 2026-09-15 00:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 82.6 |
| eeff236f-d014-3e8c-ac5b-597533a95edc | -6.7195 | -48.1201 | 2026-09-15 00:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 239.5 |
| 5b6f8b25-74be-30f4-8627-2c8a5631d227 | -6.6953 | -58.6903 | 2026-09-15 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f0e23caa-2f90-37ac-89df-ef0c09538d1e | -4.6587 | -42.0964 | 2026-09-15 00:00:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| 5d97c5dc-8565-31cd-a288-57a5891ae818 | -11.884 | -43.8142 | 2026-09-15 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 42b18e0e-4fbb-3e16-b279-ef8478fa87e9 | -8.4938 | -50.1497 | 2026-09-15 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1d9d46fe-94ba-3421-97a7-0fe7c7ed6d95 | -18.1714 | -51.7466 | 2026-09-15 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 731c30d5-c498-3ed0-80a0-1409ca894b87 | -3.234 | -50.5789 | 2026-09-15 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 2db42d17-5cbf-399f-bc8d-ca41b3eb5b86 | -4.6589 | -42.0726 | 2026-09-15 00:00:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| cb7f0ca8-9063-3177-8a72-ec4768f7584e | -4.6776 | -42.0713 | 2026-09-15 00:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 137.4 |
| a6b8b8ac-ec8d-35c8-ad54-cf7498635c90 | -4.1865 | -48.6788 | 2026-09-15 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 0eb382ba-b081-3f16-83cf-a010e21923ea | -5.1255 | -55.955 | 2026-09-15 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0f4bcb5d-0685-3838-8aef-a6bb2b90ba01 | -18.1709 | -51.7685 | 2026-09-15 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 4a3aa6ed-20b9-3b3d-9336-1dbb23899614 | -4.5229 | -54.9639 | 2026-09-15 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f9655fd5-db32-32d7-a9b8-a168594e2e14 | -6.6768 | -58.6911 | 2026-09-15 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9c63e791-2a21-30dc-8055-3ddb3efd92fd | -5.1256 | -55.9352 | 2026-09-15 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| b64f8a90-ca41-39f1-9fcd-d62c958053ca | -6.1109 | -57.684 | 2026-09-15 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 78a1cbbc-c08d-3bfa-9858-e6b8577ae4ac | -6.0731 | -57.861 | 2026-09-15 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e7c0e494-9120-3f11-873f-c8b909f786d9 | -6.7197 | -48.0983 | 2026-09-15 00:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 6c0506d6-aee5-3018-915a-d288a6af7742 | -3.234 | -50.5999 | 2026-09-15 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| fd959703-e80a-35fe-bf21-d81a5fcf92a7 | -2.6783 | -57.5893 | 2026-09-15 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 3315b3cb-3cc0-3b50-8314-9148007f53f7 | -8.5126 | -50.1481 | 2026-09-15 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e9414d54-0eae-3676-a9c3-1cd68815af3d | -15.2827 | -42.783 | 2026-09-15 00:00:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5ab3a44f-0a09-3ee6-b734-2225a900201a | -2.9209 | -50.4208 | 2026-09-15 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f6a3b9ca-9e6a-3669-a243-0e782dc75174 | -3.1816 | -61.1235 | 2026-09-15 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 73cf7101-571e-39b0-a7dc-ec12030b4619 | -4.6774 | -42.0951 | 2026-09-15 00:00:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 230.1 |
| bc8ebc4e-7996-3975-bfdd-0fd76b9a52b7 | -2.6784 | -57.5698 | 2026-09-15 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2c637ca4-af06-3723-8116-ec72200dabb9 | -2.6966 | -57.5889 | 2026-09-15 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 67ac555b-04fd-3614-b7b2-1632123dc55f | -3.4272 | -58.2138 | 2026-09-15 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| fba5abac-7489-3a27-a580-c0d9147bd8e4 | -2.9025 | -50.4004 | 2026-09-15 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| eadade34-3649-3a69-b9d6-e74f0102508a | -2.9025 | -50.4214 | 2026-09-15 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| b7f24413-4f69-3ac0-9c59-79fd5dedc781 | -10.5788 | -47.7306 | 2026-09-15 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| d984a5da-8206-3bf7-8bda-42c1662da598 | -10.5785 | -47.7528 | 2026-09-15 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b09ef0ac-6b09-3a3e-80d1-023cc318dabe | -6.9612 | -44.5316 | 2026-09-15 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b762bca8-ff0e-38ae-bf88-20027cb9247c | -6.6952 | -58.7097 | 2026-09-15 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 31396024-313b-3c0a-8b5a-7e8f5263f5f4 | -3.4934 | -50.3819 | 2026-09-15 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8c66ea97-4f76-3f86-985f-305ddee9a15b | -4.6451 | -42.419701 | 2026-09-15 00:02:00 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5a6bb4e4-fbf7-3511-9ae7-f3471595fd0a | -10.5751 | -47.727901 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25565be3-7fde-3bfe-8523-699e64362a73 | -5.4453 | -44.0341 | 2026-09-15 00:02:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29797d38-1813-3dd0-a6dc-94025ab381d7 | -7.1493 | -42.079899 | 2026-09-15 00:02:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aebf0dc9-c297-3fe9-a94a-0bc47f14893d | -7.4577 | -46.141201 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 044ffe16-23ff-3f90-b2fd-07b172e43889 | -13.5927 | -47.898102 | 2026-09-15 00:02:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1c43a0e-9d39-33b1-9658-61a60e311aa1 | -6.3161 | -39.355598 | 2026-09-15 00:02:00 | METOP-B | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 31d96eaa-8f46-3627-b73e-d87940599544 | -1.7896 | -47.822899 | 2026-09-15 00:02:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 014db84f-ac8b-3e66-94c4-268893fc746d | -12.4768 | -41.401001 | 2026-09-15 00:02:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 49d2c3b6-6955-33c7-8118-aef26e3aafbd | -10.4321 | -48.6222 | 2026-09-15 00:02:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f00aad0-7af0-3295-96ed-3c5746358be3 | -11.9723 | -44.9137 | 2026-09-15 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 273fb05e-24ee-3606-8791-48e01ce8d506 | -10.8529 | -46.2952 | 2026-09-15 00:02:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 416715e1-55c1-3e9c-94a8-677d0344df98 | -13.5596 | -51.4258 | 2026-09-15 00:02:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c49361fa-b247-3eb3-a6a5-f854d3e15e53 | -12.9679 | -41.040401 | 2026-09-15 00:02:00 | METOP-B | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b69bf5f9-3353-3289-88a6-fc41cd7fc6ea | -17.442101 | -40.166901 | 2026-09-15 00:02:00 | METOP-B | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8a45b99-71b0-395a-a52e-efc5cd2f12b8 | -11.2421 | -47.533798 | 2026-09-15 00:02:00 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83c43e44-1555-381b-bc29-11943e46a25e | -9.8738 | -47.766602 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d86000a-1822-36e2-8573-401da2198c42 | -10.5834 | -47.718601 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ade2618-ee11-33e7-86fb-ffe6005e92b1 | -9.8769 | -47.780701 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e227a92-81c6-3c7b-8805-66062f7a3989 | -12.4259 | -47.3046 | 2026-09-15 00:02:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 870a33f1-765c-39c9-ae16-a04adc5989c6 | -11.2469 | -43.4328 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37bd56c3-0992-3e0e-86e2-fdf131105ebc | -5.1327 | -55.903301 | 2026-09-15 00:02:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a46d9c0-3f07-36ac-8aa6-9a6f0a01e5da | -13.5495 | -43.520199 | 2026-09-15 00:02:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e54341b7-2832-3994-bd23-aa19789214f0 | -17.4394 | -40.1563 | 2026-09-15 00:02:00 | METOP-B | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 318377d1-04a0-3322-8b81-7e4a1382b6ef | -8.4032 | -54.678902 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10c8c6dd-4896-33f3-85d4-a3a4a429d212 | -7.456 | -46.134102 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e8829f3-6a4b-3985-bda2-a2c0a2576f7f | -10.9801 | -48.308102 | 2026-09-15 00:02:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5fefafc-9513-3a1d-8780-7ee469d2250b | -3.4959 | -50.364498 | 2026-09-15 00:02:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7d36e90-bd8a-3430-aac9-4d6239fe5420 | -12.4793 | -41.4114 | 2026-09-15 00:02:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1523c3a4-59cd-3cd9-be23-9ef65f6c97f0 | -6.6737 | -46.184601 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b44a8d28-3cfa-32bb-9dfd-c17d9df54557 | -7.1577 | -43.509602 | 2026-09-15 00:02:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c3b5207-5ec3-3945-8e61-04cff2b5bab7 | -9.1651 | -49.973499 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e52ec2-6cae-34ac-8d48-444f73fa465d | -2.9007 | -50.3722 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037f88be-aaae-399d-8345-279f99c9f275 | -7.5484 | -46.857899 | 2026-09-15 00:02:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee9f3c90-4d14-332e-9aa5-df75b9010969 | -11.1058 | -40.4422 | 2026-09-15 00:02:00 | METOP-B | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c7a808ed-980b-3ae8-9a27-0454532ec563 | -6.1696 | -52.709801 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c117dad6-c620-3109-9681-48d17a1d74da | -9.7518 | -46.576 | 2026-09-15 00:02:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f00c05ec-13e0-3306-bdd3-3a1d60d6b944 | 0.2155 | -51.3475 | 2026-09-15 00:02:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b470dfb5-f678-32b8-8f4c-58c2aa4f6806 | 0.2172 | -51.340099 | 2026-09-15 00:02:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3a28c1b3-e07a-33f9-a36e-5b1c23487d33 | -3.8461 | -49.0345 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b95911ab-adcb-3f76-baf6-1395fc3627ad | -7.6526 | -49.490898 | 2026-09-15 00:02:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5116a113-f3dd-3e0c-a2bd-2ef3d97c693c | -10.6884 | -54.1343 | 2026-09-15 00:02:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35cac6f9-d1d2-3176-9c21-907889e55632 | -11.1633 | -42.7729 | 2026-09-15 00:02:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a9381665-2179-31e8-99b5-d64d86b3d005 | -10.9817 | -48.315399 | 2026-09-15 00:02:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cbc4722-32c9-3d65-9688-1559e1e4a67a | -8.5021 | -50.134399 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df0ea41-f3b6-3993-9032-f55a262e00f1 | -10.0447 | -44.8755 | 2026-09-15 00:02:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b201bb4c-3309-3afd-9624-32db498f54c4 | -5.9257 | -53.5215 | 2026-09-15 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e962753b-509c-3dd7-a54c-a80a93c54f6c | -5.5508 | -43.4268 | 2026-09-15 00:02:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11c5b3f3-afd7-3abe-ba73-bcd4f2adc0b3 | -11.2313 | -43.4543 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff87c75-4a32-384d-ab88-cf89169240bb | -7.4776 | -49.443401 | 2026-09-15 00:02:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8303561-0bab-3af6-828d-b6e1dc955029 | -14.8383 | -49.237202 | 2026-09-15 00:02:00 | METOP-B | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a8532b6f-576e-3956-8e0b-7241f9ecd351 | -15.5468 | -48.804798 | 2026-09-15 00:02:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1a7402b8-b35c-3144-ab9f-62a9a2091274 | -13.7255 | -48.956699 | 2026-09-15 00:02:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0b8baff2-4c38-3bf9-acdf-02acc884433b | -7.3292 | -47.255402 | 2026-09-15 00:02:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f78f3782-eb52-339a-85b5-b799b69f79c1 | -4.1864 | -48.6702 | 2026-09-15 00:02:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78f4a10-310d-36ce-b7c9-756fa08d391d | -13.6368 | -47.864799 | 2026-09-15 00:02:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ffcd60f2-05c2-3eb4-ae7e-28985add3e62 | -8.6575 | -49.1063 | 2026-09-15 00:02:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32de04f2-6f12-3233-ab87-b700e82abe3e | -11.8833 | -43.813702 | 2026-09-15 00:02:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68bb18b9-e4b9-35ca-ae60-902f1e7858f5 | -7.9281 | -49.716 | 2026-09-15 00:02:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2def902d-1d33-3b76-b773-5ae23ebdc7ab | -13.5699 | -47.8876 | 2026-09-15 00:02:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ee795cb-696e-3779-8d91-b23aba3cd120 | -14.691 | -47.996101 | 2026-09-15 00:02:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83e3d9ea-8f66-35ac-9aaf-63d0f9467624 | -11.8716 | -43.808102 | 2026-09-15 00:02:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a19ee6d6-59b9-38eb-abd9-ee063bc24cd3 | -11.2274 | -43.4375 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39f87e95-78af-31d3-bf0c-9b829c312685 | -4.6446 | -42.068199 | 2026-09-15 00:02:00 | METOP-B | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
