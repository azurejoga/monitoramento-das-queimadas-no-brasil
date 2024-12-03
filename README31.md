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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9701286a-8de8-382a-bf6f-1772e27220ee | -5.56715 | -44.88766 | 2024-12-03 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7479ad8f-2dfe-3c38-a0d9-6155cb7f1bfc | -2.21417 | -45.7368 | 2024-12-03 04:06:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 10736e67-e22a-3bdd-9e32-7125d45cc74d | -2.77462 | -45.22045 | 2024-12-03 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42abcd3a-6321-3db4-9171-cecbf0010ed1 | -3.37143 | -45.84417 | 2024-12-03 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e18318d-881b-3481-9dde-4b86d6c253cd | -3.90154 | -46.65018 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d18956ef-c768-3ebb-b93b-225e26abc394 | -2.29116 | -46.36637 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c945c07-65e5-3948-be9d-a99816f74a34 | -3.32125 | -42.78513 | 2024-12-03 04:06:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a628672-4180-3e77-9ccc-06d6b1d46a6f | -3.19214 | -51.17331 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92cefd4a-0148-308d-a408-b3d7bafc7c27 | -2.85402 | -45.83011 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1cdc9ca5-bda8-3d0e-8def-f2cd4e7a0836 | -4.19217 | -51.19299 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df445583-c277-3f2e-961a-ecb72230b7ff | -3.70199 | -51.82061 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33518356-73a0-3bba-b6ab-a2fe9fc995d0 | -4.4841 | -46.36089 | 2024-12-03 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8679d9d8-0c82-3475-bf59-3222c974c459 | -2.72294 | -46.20499 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5e3503a-4ae9-3c3e-8e4c-6be200eaeeff | -5.1709 | -44.80334 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83f7dc26-ecf2-388c-a805-0e04f605df11 | -4.34804 | -45.99527 | 2024-12-03 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9319d0df-4080-392d-a2f9-cb2101583821 | -5.80797 | -46.48856 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 62934f60-30aa-3e9e-87a5-d8feb49b2a64 | -4.23268 | -47.5715 | 2024-12-03 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62180350-315a-3cdd-ba26-0b8f8fca1145 | -4.01951 | -38.25114 | 2024-12-03 04:06:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dfbb751f-d601-33f0-90cd-0374ea58bee9 | -2.85551 | -45.38998 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4906bf4-6491-39c1-8063-5bfd9e208c66 | -1.9081 | -46.3001 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8223a296-1f70-3aff-82d1-5a4515cc2cd5 | -3.8146 | -46.54911 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 813c017a-eca4-37f9-822e-2870beeb8637 | -3.5403 | -50.17677 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90f784d8-0878-3f75-9208-07ac79da5009 | -3.98222 | -46.63581 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c949174-7c71-3e62-b5ee-33702d89fadb | -2.6776 | -46.61868 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24e8c889-ebcc-3f86-815b-e2cf01bf8a3d | -2.9268 | -49.43807 | 2024-12-03 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da349e67-714c-3964-9ca2-140b764cfc4f | -3.92972 | -47.98261 | 2024-12-03 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3274b112-cc2a-3601-9533-ce526966eebb | -2.67328 | -46.61801 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ace489f1-fe1f-3e60-8e00-270d1885db59 | -1.9916 | -45.38782 | 2024-12-03 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc3bc053-6912-3b1c-93d4-99201e6d7176 | -3.81517 | -46.54935 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e901acd-04f4-3ba7-8713-1e39afd6b849 | -3.58335 | -53.04962 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4e45cb8-c269-385f-b118-618edfc5a715 | -6.02335 | -46.24802 | 2024-12-03 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cdb2c65-fe9d-3d75-953f-9456963fde2c | -3.84933 | -46.52248 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af4fd098-e2e4-3967-ad0f-8419f02a1bb4 | -3.52031 | -45.01128 | 2024-12-03 04:06:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dfb3d43-6192-3cca-ad19-2008a165748a | -3.28326 | -53.24764 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9297a4e8-4069-3e32-a816-3dd777edb0fa | -1.74349 | -52.62387 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a4ac97-1278-3a93-aaa7-e760076a36c1 | -3.81499 | -46.67695 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32e69df6-ea45-3046-be1a-703a1cd84103 | -3.08351 | -53.37576 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a04f52b3-6cde-36a3-a054-8299d1c62d1a | -3.59873 | -41.66958 | 2024-12-03 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93ddf7c6-2ac4-343d-9c64-6fc7b5f38858 | -0.60333 | -51.68636 | 2024-12-03 04:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 753830d5-4af5-3342-ac9b-9196c62f9a7b | -4.21055 | -44.3694 | 2024-12-03 04:06:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 40314f0b-8df0-3f89-a88b-94a3823590a8 | -4.08113 | -47.35093 | 2024-12-03 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abcc8341-b8fc-3fea-8575-5744e3ff16e3 | -2.05285 | -46.28991 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 486655b4-e191-3e35-ba88-7018d1f49f1f | -5.49548 | -44.99866 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53cab807-cf91-35a2-a7ab-a2128922a1f8 | -5.11343 | -43.21117 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ac1cb5c2-7dcd-3dfa-841d-77bf6ebf305e | -2.67979 | -46.12062 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 787ad0d4-ea8c-3b3b-a4eb-6618d65c2b39 | -6.17935 | -42.61947 | 2024-12-03 04:06:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9b073636-50b5-3b29-9107-c9c04437c7ee | -3.55252 | -50.17878 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 345c278d-301c-32d4-835b-55ab7c198289 | -4.18134 | -51.18718 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 461722e0-7242-3694-ad89-d179855f8825 | -10.09538 | -47.38049 | 2024-12-03 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b9dd817-c9f2-39d6-ac80-6dfdd544876e | -10.6627 | -44.49595 | 2024-12-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 969caa39-e2a7-3288-a4ef-4a68fa3fd598 | -10.6865 | -40.54061 | 2024-12-03 04:08:00 | NPP-375D | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe31a32c-4ad8-3e63-9774-72a9d0193e53 | -12.69951 | -47.63377 | 2024-12-03 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e293a08-fc73-30ea-bed9-e1bb053eb43f | -12.4344 | -46.67358 | 2024-12-03 04:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7831319-cb5e-3fc3-8ea9-a9d1885e6bc4 | -6.98864 | -43.52394 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5c15c1fb-06b1-32a7-96a0-6e7545e7870d | -12.63562 | -46.71925 | 2024-12-03 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8e072a4-f210-396d-81c8-0c49b320991a | -6.74835 | -46.83441 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bae0a30-d609-3cf9-aaad-da6548df3a29 | -10.653 | -44.49043 | 2024-12-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ca81bbb-e281-367a-b3c6-02d722f62f57 | -6.98298 | -43.51537 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| bc886ac7-26d5-3618-90e2-ef330ae56617 | -10.65989 | -44.49158 | 2024-12-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 193bb89a-4177-31f3-bae9-8fa249373161 | -9.16425 | -43.11792 | 2024-12-03 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1db3e3d-ab80-362f-9e74-9672cf60c241 | -6.82004 | -46.77482 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 371ef45f-c9c0-3dff-8666-bff0cf9c456c | -7.80232 | -38.73018 | 2024-12-03 04:08:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ff56f2fe-95f8-316e-afaf-b7a10a910c15 | -10.45019 | -45.0788 | 2024-12-03 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d98ccc09-4aeb-3fa8-a958-131fc4602ce5 | -6.74897 | -46.83074 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6925cc33-20c9-3f94-b1ef-e2dc82773330 | -6.81941 | -46.77851 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f8685ef-e469-3dc1-bd23-ca0654ebd22f | -6.98641 | -43.51593 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 94a8500e-aeab-3484-9dde-22300bf5e581 | -7.10271 | -46.45745 | 2024-12-03 04:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8575679a-9a94-3b96-9013-2f76d922643b | -6.6616 | -46.55677 | 2024-12-03 04:08:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e13df182-3c55-3cf2-8168-d7097466506f | -10.49154 | -36.71018 | 2024-12-03 04:08:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aaafdaf6-c75f-33c9-a412-39622f1a18e3 | -6.97955 | -43.5148 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8f9cefa5-43d7-333f-9bfa-110d4f080189 | -10.92072 | -40.58316 | 2024-12-03 04:08:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 721d2b42-9bcb-3e27-84b2-128dd0633544 | -8.11744 | -41.18427 | 2024-12-03 04:08:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ec461df8-f7b1-3b78-91d3-c5ed74f9e473 | -8.87878 | -47.26375 | 2024-12-03 04:08:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5ea3eaf-7607-3310-8ba4-0d43e1a0458b | -6.62348 | -47.13956 | 2024-12-03 04:08:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e195a26a-9c36-3dbe-8a18-b072c4844d1d | -6.98238 | -43.51909 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d266ad61-094d-3a73-859d-87547d552e78 | -12.50047 | -46.34901 | 2024-12-03 04:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddad559c-841c-3269-b656-e86ec8735813 | -10.49522 | -36.71465 | 2024-12-03 04:08:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2503df58-b270-3b4a-9f7f-a7f99f132c29 | -8.60573 | -41.0143 | 2024-12-03 04:08:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2ae57976-58a0-37ba-b4a4-3831f5f444dc | -13.57538 | -44.51609 | 2024-12-03 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f86019e-6e89-36e1-9cef-b226d394b0ff | -10.64892 | -44.49364 | 2024-12-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4ad99afb-2750-3151-b32d-ba0e347687d7 | -6.99148 | -43.52823 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ea080408-239a-39af-bf48-dda2aa57f441 | -12.43517 | -46.66901 | 2024-12-03 04:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2f5eb6f-a37c-39a6-a660-7840ad8e458b | -9.64793 | -42.16431 | 2024-12-03 04:08:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1a7dbdf8-8577-325e-99b7-f971dae469fa | -7.8944 | -39.55354 | 2024-12-03 04:08:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 191f24ab-db3c-36b4-9a96-e288fc4389a8 | -6.67821 | -46.38501 | 2024-12-03 04:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4748095-4fe8-3d80-98e2-9c73e8197d29 | -9.16482 | -43.11437 | 2024-12-03 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c5bebaf7-f4f5-3332-b36c-94f51d0b4c48 | -8.13544 | -44.46793 | 2024-12-03 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71848d8d-5fc5-30f1-8a4a-470af963595d | -6.74959 | -46.82706 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aef96801-9dcf-385f-b180-b4078fa417a1 | -9.87185 | -37.64713 | 2024-12-03 04:08:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 239fe45d-8fed-35de-ac12-c07f6d3f7463 | -6.98924 | -43.52022 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2eb1b0ff-9411-324c-9bf2-a6c68d79ffc0 | -6.81187 | -46.77347 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 742c4925-9c53-3c96-b539-b96adc33ebe7 | -9.53612 | -45.35834 | 2024-12-03 04:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 782f8da8-44c0-3568-9c03-4f1a3e102ef5 | -10.49945 | -36.71519 | 2024-12-03 04:08:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 215723eb-26d3-3ac6-82f3-42e5198b1443 | -12.35821 | -43.76243 | 2024-12-03 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50cbf846-de5b-38e8-897c-5539a52f2baf | -6.98581 | -43.51966 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 857c7a0f-7f38-3e03-980f-c5297fcc62b5 | -12.25226 | -43.87767 | 2024-12-03 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 475e7130-7e24-3c4c-bcfa-038187a4038d | -10.1031 | -43.94542 | 2024-12-03 04:08:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbf27269-b8b1-3955-bb9f-e0313e2c7f23 | -10.65926 | -44.49537 | 2024-12-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca7dde28-206f-31ff-b04e-53691c3cfe32 | -6.97611 | -43.51424 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a4fc7248-1bae-3d86-bb50-99fc383cdbe8 | -7.28038 | -46.19074 | 2024-12-03 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README32.md)
