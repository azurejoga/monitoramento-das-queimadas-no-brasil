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
| 05edb102-8131-35d3-a247-1798c20fcf5f | -6.80106 | -45.41067 | 2025-10-26 04:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8120453-3842-34f3-8d59-cf70f317318f | -3.69233 | -51.97142 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65730958-589e-3f41-95c6-f6ffa81e9056 | -3.84742 | -43.17071 | 2025-10-26 04:49:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d55cdfd-1709-38bd-9cf4-27a6c3aff0ea | -2.89994 | -53.13208 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf35be7c-63b9-3bb4-9294-b0d61b6ba2da | -5.11543 | -43.20074 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 115b185b-4cea-3937-9606-6ccfd511803c | -3.10326 | -49.44701 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b681878d-80ba-302d-af41-3cd18d972799 | 1.43223 | -50.89505 | 2025-10-26 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4e74ce5-d0fe-3e74-aa58-d0c95f7a0931 | -6.5839 | -48.76746 | 2025-10-26 04:49:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2c90438-bf23-3a0e-8abb-2059a050efd8 | -3.74436 | -51.63874 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e940f57-a1c0-3e55-b9a4-acc22ab662fa | -6.2205 | -42.53296 | 2025-10-26 04:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 847a47f9-daa1-3310-9d40-08e7cb48cb6e | -4.15537 | -46.79082 | 2025-10-26 04:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6123994-fa14-3033-a868-a0d0ca842778 | -3.60581 | -49.34676 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e207ca7-c02d-33b1-a2e1-e22c6b800d0e | -4.10617 | -50.44817 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2cfb3d6c-6eb5-3cbf-8954-04f8ed18369f | -5.60898 | -45.18922 | 2025-10-26 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 707c77ac-e26f-3e29-a4ce-9d467ef22223 | -6.82908 | -41.5543 | 2025-10-26 04:49:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1696ccd5-bdfa-3909-982c-c2f7eceacf09 | -7.35318 | -42.44606 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f30637c4-920e-3dcc-aa9e-f43963477992 | -5.10531 | -43.19599 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5b999e5-1dcb-38f0-9cfc-0bdd278cf53e | -6.21443 | -42.53541 | 2025-10-26 04:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aa46ff13-2343-3c24-8304-9c2f94c88d8b | 1.54382 | -55.99015 | 2025-10-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e090e62c-d343-3ca8-9df1-c9df15b42a23 | -2.98101 | -49.12011 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c2ed7f37-aec0-38d3-ac85-d1388bde13fa | -5.67551 | -48.86727 | 2025-10-26 04:49:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f36198a-b9ff-3f7b-9c55-a57a53b5217d | -6.73209 | -44.1503 | 2025-10-26 04:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bf773e9-6b62-327b-b00b-24cfa5da7154 | -2.76497 | -45.08993 | 2025-10-26 04:49:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60452218-b7c0-3e4d-84a9-1712065f3686 | -5.73306 | -44.52145 | 2025-10-26 04:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64b810d2-2b78-333a-b5c2-a954cd9b2a9e | -6.30286 | -42.95627 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 262620c0-38bf-3898-a89c-676fc75187c7 | -3.78475 | -49.84878 | 2025-10-26 04:49:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 099cce55-43dd-3297-82a0-20dc0f948b06 | -3.61004 | -48.91814 | 2025-10-26 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d4e667a2-0f84-3636-a77c-712605ba75fe | -4.70994 | -55.98577 | 2025-10-26 04:49:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feb8bb7c-3bf5-3f88-b85a-000251957ea5 | -4.41278 | -48.94745 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11d318b9-2402-31ec-ba4a-c5e98fc3097d | -3.78485 | -52.04897 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cba0ae9-dafd-30d3-9650-cff7163fc328 | -3.12065 | -51.20615 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 897737eb-4fd2-3d08-97af-514592feadaf | -3.1006 | -49.45741 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8db2e119-4809-3993-b3de-bcfb884d2634 | -3.09861 | -49.4541 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1a67f0a-d0b7-3771-872d-5c9566289731 | -3.15851 | -49.1699 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b96477a0-3168-3d7f-a5b6-caf6addd7554 | -5.60297 | -51.65413 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d0fd9f5-5587-301a-978d-d70538272386 | -6.30837 | -42.95673 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c74ab162-45f4-302a-befd-57e2c29f555d | -2.95181 | -51.52439 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce89a4f5-a4e1-368b-9300-dac85000659a | -4.88847 | -43.2466 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e9f7fac-5275-3f0d-ab24-bc003331caf1 | 1.16255 | -60.6729 | 2025-10-26 04:49:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67b0538e-3e78-3c7e-bb0b-a2f62b832a20 | -6.66446 | -47.74126 | 2025-10-26 04:49:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b72be6bc-5025-3878-b7f0-b07315c7e9c2 | -3.94564 | -52.21885 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b0907e-5b61-311b-9df1-315edd5fb795 | -2.92183 | -52.71285 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 744736d0-0e05-3af4-a0b6-e3348ccb8d06 | -5.88605 | -41.3051 | 2025-10-26 04:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 77bc4896-40dc-3a64-bd8b-dbd658346ae1 | -3.10522 | -49.47368 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57bbd789-1f33-3ec4-9dce-ad8ae820174a | -5.41566 | -46.00711 | 2025-10-26 04:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 547f4dab-2cb2-3784-bd3c-98b3901991e4 | -6.39836 | -45.77121 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99b786cf-4ded-3351-82e3-992195ae9a95 | -5.84942 | -47.19231 | 2025-10-26 04:49:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b01cccd3-0e3d-3ba2-8eb2-d56255350243 | -3.90642 | -47.72404 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebf3bacb-95b6-3c73-b78b-86dbf0da558e | -5.69505 | -48.48699 | 2025-10-26 04:49:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7906d745-8e17-3ac0-ac68-d432e4e40e18 | -5.23164 | -48.53058 | 2025-10-26 04:49:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f7327929-ea93-30f1-905a-9d7cac328c6a | 1.60937 | -55.76292 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8087469f-2492-3e3d-994e-c0583cf16ccc | 1.61526 | -55.74752 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66bad227-3c90-3889-b265-7fd746efa1ad | -7.05199 | -43.88445 | 2025-10-26 04:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dfe6884-bbc2-3551-a986-402a12660696 | -3.89533 | -45.16993 | 2025-10-26 04:49:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e62f28c2-f523-398b-abab-101df1410d98 | -5.44468 | -48.85811 | 2025-10-26 04:49:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 781347ab-74be-373f-bb73-39cfe37ded19 | -4.20105 | -48.36747 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 016f4cf5-1729-312f-9a69-6814ba6bfaf2 | -7.0248 | -46.07898 | 2025-10-26 04:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d015de78-411e-3f04-95dd-441bf51931e2 | -4.9319 | -48.55938 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48044d75-e405-3622-9650-e26876e968d9 | -5.65498 | -51.0988 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ef9c8cf-9eef-3f42-83f6-5a16a3d77225 | -4.79481 | -49.39027 | 2025-10-26 04:49:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b05e55a1-3d85-3ef2-af3d-0cfda4ee1069 | -2.66718 | -49.49397 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce75cbcf-2e82-3584-8f44-4e2ae96cfcb1 | -4.1984 | -54.93936 | 2025-10-26 04:49:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a3612b1-d9fd-379c-9018-7928913a5352 | -3.48197 | -49.90178 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7d47bdd-527f-3d12-80e9-d2308a1670e4 | -4.89076 | -43.23119 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddf5600c-554a-3aea-9c79-2c525329217d | -4.72852 | -49.08805 | 2025-10-26 04:49:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8029d899-1bb9-3a20-be1d-d39ef7255cc4 | -4.20163 | -54.93891 | 2025-10-26 04:49:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8b55bce-d229-3b77-868e-c155b2b9e078 | -3.1644 | -48.60749 | 2025-10-26 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d113ec0-0714-368a-9124-6691440914e2 | -7.14844 | -44.84824 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 880b5ea5-d79b-39f9-8b72-cabb20fa38d3 | -3.76165 | -52.26696 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d017a71-6cdb-3257-884a-c055c8fd32fb | -3.3319 | -44.85273 | 2025-10-26 04:49:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea17752b-40c6-31a2-8d4a-a46ea3020881 | -5.66179 | -47.4435 | 2025-10-26 04:49:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eac4499f-5410-3470-a7b5-94e4e0064f30 | -6.62721 | -44.63856 | 2025-10-26 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2968352c-9678-3800-82e1-3d5f61c1de22 | -4.22388 | -48.3666 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd56bbaf-dd11-36f3-92e8-906106bae631 | -6.38803 | -45.77911 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74154ab3-bdbc-3c15-bfe9-0d80cd0f90bf | -3.1058 | -49.4465 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0851f7a-fbdd-3122-9930-d73bf5a55058 | -6.09274 | -47.06337 | 2025-10-26 04:49:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4e5588c-503e-3517-98dd-f3b58fcf5009 | -3.1135 | -51.20857 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ae1953-7395-337a-9ebb-399c66aa22ba | -5.11057 | -43.19244 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5665c5d5-23a5-3fed-8c7a-7ed3325f933a | -3.83552 | -50.1995 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07a5e726-b1bc-36a0-89a1-da591d1059c9 | -3.78368 | -43.41051 | 2025-10-26 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04a08570-11ad-3ac6-83a4-2836ad551b41 | -4.2017 | -48.36318 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f896722-4c57-3422-8168-626ebd2e3172 | -4.48733 | -48.67583 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef660d0a-2268-36ce-ba98-57f29f3b6335 | -6.39192 | -45.78415 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| be96a2b0-9dd0-3de8-8c1d-0628028d88d3 | -7.04376 | -41.64888 | 2025-10-26 04:49:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7f76c75d-4f18-3ca2-969b-a68f38d32fd5 | -2.47768 | -52.16307 | 2025-10-26 04:49:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95752814-6204-3752-a07c-36d81538f763 | -4.89858 | -43.25216 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9fcc42eb-2271-3949-a884-809b60d1d4c2 | -3.10292 | -49.44213 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c03fbb-ac34-3b3b-9987-ee32d3af715f | -2.79003 | -54.41982 | 2025-10-26 04:49:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d347fce5-58e1-3255-ae44-9573c37aabac | -4.51155 | -47.64469 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 132f1e5d-3be7-337b-af41-ec5ffc7a55e5 | -4.8913 | -43.22734 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 439fead3-ff05-3bdc-8ed1-cc71d9743b99 | -6.02299 | -43.30547 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d043185d-ee86-3b21-84b9-4faf94feb3a6 | -6.98676 | -44.01192 | 2025-10-26 04:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d62abb03-0401-3670-bf20-ac5c64806a75 | -4.70796 | -46.43737 | 2025-10-26 04:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95c51ff8-165c-3a30-b29d-a1f472d0d997 | -2.65506 | -48.50616 | 2025-10-26 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 029b812f-5f0b-3d6c-980a-1dea7cda1aca | -6.70844 | -42.04236 | 2025-10-26 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7aa88538-4dad-3576-9db3-ed0fc17cda45 | -3.31569 | -50.11003 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30767257-f690-3476-b3be-3242f4e4ec7a | -5.10579 | -43.19274 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6a8484c-9db2-39cb-b4b1-8088095a697f | -3.21098 | -46.83751 | 2025-10-26 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5d97bb0b-66cf-3d80-aef8-ee4e2bb37fef | -6.54859 | -41.59922 | 2025-10-26 04:49:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53d74173-8229-3dd9-bb4e-40755505d93e | -3.38757 | -52.37007 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README32.md)
