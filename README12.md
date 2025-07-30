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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9034daef-aa68-3a02-9ead-bcc71a650721 | -5.74043 | -39.77051 | 2025-07-30 04:02:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2201f22f-9fcf-37c9-aa8c-595e8fa10828 | -9.27074 | -40.55339 | 2025-07-30 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0f50dd75-f9d4-31ec-ad6d-7c438753bbbb | -6.12999 | -44.43878 | 2025-07-30 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b299bac-43da-3b86-9905-01308c38adcb | -9.75114 | -37.00152 | 2025-07-30 04:02:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f8ba53ad-f04b-3041-a220-a4a9b6a596c1 | -7.06547 | -44.96056 | 2025-07-30 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcc0052b-557a-375c-afb3-9d3adfb6437e | -5.24517 | -45.21846 | 2025-07-30 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a765f77a-7bc5-333b-af11-b128c58f92c0 | -7.93915 | -44.08564 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e478e48-8f78-3042-96e6-5c31a4e9f67c | -10.41233 | -47.2548 | 2025-07-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7e67af0-e2e5-32f8-bfeb-1d4a3be288f8 | -8.45217 | -43.86857 | 2025-07-30 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a78edd9b-2669-3819-b4e1-cedf25220d5e | -6.14645 | -44.35091 | 2025-07-30 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b963c15-2c55-3870-bcd6-26ea18006e73 | -7.93473 | -44.0894 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2f9162c-5a4a-3e39-8239-51be803e2226 | -9.22771 | -48.59994 | 2025-07-30 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faf1c097-9fdd-3b08-8d6b-5d46f79942fb | -7.31529 | -43.40985 | 2025-07-30 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e20feb88-25b3-36b6-b4c6-0a482f8e99e9 | -7.05754 | -44.95962 | 2025-07-30 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5539dde0-7896-3a93-970b-c933491b448d | -6.89402 | -44.73266 | 2025-07-30 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ded8d74-8f0c-38c1-bfae-02c028d7735d | -10.62164 | -45.2392 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 45602737-a115-3ba5-b6e5-db86ba68e5d3 | -5.40493 | -49.12066 | 2025-07-30 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efc79fa7-cad0-3ab5-a6bf-d5bd88d4c6ad | -7.78046 | -44.99895 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4bcb03c1-389e-35f4-b486-4976e66cd06f | -9.14424 | -49.84578 | 2025-07-30 04:02:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69b083b3-9d8a-325a-98ff-0a0f6b926fcd | -7.13754 | -44.36554 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bb5794b-5aaa-34f4-a2b9-35e434b5bdec | -9.7455 | -48.57616 | 2025-07-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| baa96dd6-8f19-32a3-aa52-77549c8be312 | -5.4236 | -42.63852 | 2025-07-30 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd96cfcf-eb37-38d1-8465-c1eaef5e4a6f | -6.38547 | -53.33405 | 2025-07-30 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66950be1-7e9a-3ef7-8c03-4aaee4e114d2 | -10.43584 | -48.32759 | 2025-07-30 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 125f99ee-6439-372d-a26e-ae171cca22f8 | -11.46392 | -45.11612 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7d4df87e-c9ce-31b0-bde9-29b4b17e01af | -9.63521 | -43.84635 | 2025-07-30 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6635f098-a661-3718-836a-013f39655143 | -6.15825 | -43.8029 | 2025-07-30 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae29724e-4d70-3812-9b79-6f092b27f88b | -7.28274 | -44.54726 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a6a79ff-d5a0-31bc-835f-f373d9f858ef | -8.03205 | -46.91364 | 2025-07-30 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 091ca1c5-8c85-3339-80f7-b00c55c94110 | -7.77571 | -45.00327 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8261ef93-3e37-3ba7-8704-7989116040a0 | -6.57478 | -41.51511 | 2025-07-30 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11d6ee8e-d492-3e63-b180-802889ac9b62 | -10.62544 | -45.23986 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1eb006b8-b058-326b-873a-6e043cf2b78a | -7.10486 | -44.37709 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5efb5269-7755-367c-8223-019c5383bc4a | -6.69752 | -42.04638 | 2025-07-30 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7ab6996-c347-3b1b-bbb6-eb0fb1d59b9e | -4.65199 | -43.12604 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0c37ed5f-5859-3d6e-bcbd-26eba5d73914 | -11.47135 | -45.11752 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 75fbee5e-5477-3eca-ba94-14627a76fe30 | -5.40091 | -43.24975 | 2025-07-30 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 953f59ce-5c62-33b4-bcd8-63f78da26be3 | -4.65703 | -43.11808 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60994c4a-2789-3f29-bd1f-591626bfa124 | -7.06943 | -44.96106 | 2025-07-30 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3df2b073-bdc3-3310-bf1c-323a66d4fe4e | -7.14968 | -44.05486 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ff76b73-f42f-3d8c-87ed-fc1af0726a2a | -5.24713 | -45.21498 | 2025-07-30 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8be69127-43d6-33bb-b4d9-827f22774578 | -9.59462 | -46.32465 | 2025-07-30 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46709eea-6424-3db2-b516-3fc431a82334 | -5.98919 | -45.51945 | 2025-07-30 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03c53a88-5df4-3d9f-b782-2d0add8e43a4 | -7.0039 | -42.37132 | 2025-07-30 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93db6383-b74c-3ffd-892c-0c9bb7218714 | -10.08674 | -46.97398 | 2025-07-30 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12e5d19e-2db8-3711-a673-44d5327e4983 | -10.61865 | -45.23382 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ddce0de3-2396-319f-8816-a3666227f4cd | -4.85423 | -42.99139 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7cbb2ab-b081-3644-bb52-ec6dcdd60f45 | -8.62715 | -45.88995 | 2025-07-30 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a022ec12-95fd-39ce-abaa-b8657af5ec66 | -8.40619 | -50.11632 | 2025-07-30 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c411f8a5-929c-31fd-a10f-2829f387ea56 | -6.91971 | -38.56456 | 2025-07-30 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e57f892-3f65-31e4-bea5-1ffba2ae2a77 | -11.80962 | -44.26677 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6459b3ec-6462-34e8-9053-dfb49cd4e117 | -8.23756 | -44.91859 | 2025-07-30 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdafdc33-82a4-3825-9474-2e4fce3030de | -5.40552 | -49.11721 | 2025-07-30 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38eb64f7-8c53-395d-8988-8815a4cba2a5 | -8.23837 | -44.91383 | 2025-07-30 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff382743-50a5-3c6a-815c-dd7d1bc0e02b | -8.01554 | -47.68275 | 2025-07-30 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7e17db5-cfd0-337f-b244-71124d17d295 | -4.77981 | -43.37526 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd6c2eab-19d3-3941-8416-29ef8e17fa04 | -4.65268 | -43.12177 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0358a7c0-bcff-35e1-beef-abcc01eef818 | -8.637 | -45.51037 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13b578fa-7062-3e4d-bb29-072f0b51daac | -9.22951 | -48.59824 | 2025-07-30 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a219a8a1-de6e-3c18-86e2-b8fe30408a86 | -5.32414 | -42.75857 | 2025-07-30 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 96d3ae34-fca0-3af1-bb2a-b317457327c2 | -10.82509 | -49.38083 | 2025-07-30 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dcb1679-28d8-357c-835e-e27672882072 | -6.45194 | -53.36039 | 2025-07-30 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ecf405a-7936-3af7-9c0c-a1a880cbcafd | -5.24992 | -45.21539 | 2025-07-30 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be0f3953-09ac-38f3-a5db-d6e6e49416cb | -10.47962 | -46.66926 | 2025-07-30 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e609cb46-4d30-355e-b8bc-c9f2228e95d5 | -5.74411 | -47.96131 | 2025-07-30 04:02:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a028ce99-68ce-3314-9465-f546a63d3ff4 | -10.94272 | -45.79049 | 2025-07-30 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ab96760-928f-34d5-a25e-7167dc1996c9 | -5.76445 | -43.95087 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adfb6356-21be-3726-94d2-b053f3561d5a | -7.33527 | -44.69596 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67a93a35-3ccb-325c-a55f-030145fb0bcc | -4.37484 | -49.0339 | 2025-07-30 04:02:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 730692f5-2f80-39f2-97bd-3674c32770d9 | -10.05511 | -46.55931 | 2025-07-30 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9e1643a-7e5f-3df8-84c4-0e8178d8f7d2 | -6.12395 | -43.96383 | 2025-07-30 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 268ada76-0750-3080-996d-e6653c04cd2c | -8.62505 | -45.50845 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b52b4e9d-6888-3b5a-b8d4-910ca29d022d | -8.37291 | -43.96116 | 2025-07-30 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67e388b4-9429-36e2-81c6-a78954ac951f | -4.89946 | -44.96297 | 2025-07-30 04:02:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c267e76-0d70-37e5-b86d-01ec7c2322c9 | -6.4162 | -53.35922 | 2025-07-30 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9111e208-655a-3c93-8f51-e0b0a8d39851 | -9.04852 | -45.07305 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55bf946f-bb94-38b1-9656-22c8e9d51d4d | -7.73775 | -51.0941 | 2025-07-30 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7726723c-df19-3a7d-bcff-ae27740fbdbc | -11.46843 | -45.11222 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 10d8f591-cf3c-3881-9013-92d02c983c26 | -5.74373 | -39.77102 | 2025-07-30 04:02:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0222dbb-592e-3b72-800a-85d0c907bf7f | -6.92027 | -38.56091 | 2025-07-30 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a31004e-d9d1-319e-a7bc-bbe5fc8b0397 | -4.10005 | -48.20126 | 2025-07-30 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ceee05f-e0ed-315e-8520-599308c0df73 | -8.52178 | -43.31345 | 2025-07-30 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e23cf02-f3cd-32a9-9aa0-c3c671f9707d | -5.68051 | -43.67867 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa273d24-cdad-3fef-a98f-2b3510d6250c | -5.2458 | -45.21474 | 2025-07-30 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fef7e60-39dc-3203-962e-c57a57b044bf | -10.47489 | -46.69627 | 2025-07-30 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c72cd2b8-9357-3c2e-a8df-4c70e12debae | -6.89508 | -45.25426 | 2025-07-30 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f078995b-025e-3687-8a69-516a3419070c | -7.15556 | -44.04221 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f5681bc-87de-3d75-b443-2425168c83cc | -7.20224 | -44.09389 | 2025-07-30 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a6626fd-a298-3678-9d6c-a050970e4f7d | -7.1041 | -44.38178 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51e52d89-61c6-37da-bd66-3ea85add2bc1 | -4.65634 | -43.12235 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 81e3e6ac-121a-3d0b-b1cb-3c81fef6b2ba | -9.23177 | -50.047 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3def594e-ea96-370a-ae63-98df3e8ac5bd | -6.98933 | -41.62502 | 2025-07-30 04:02:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9466b124-6ebb-380e-8bea-be1dd165c9d3 | -8.03648 | -46.91426 | 2025-07-30 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6df797ae-0a6e-39cc-a0ad-01f90d6737f5 | -6.37863 | -53.33284 | 2025-07-30 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 821e4e11-d7d1-3c13-bef9-c73c5f58b3c9 | -5.0634 | -43.72718 | 2025-07-30 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90dad9be-9138-33bf-b7d5-af897087974f | -7.94285 | -44.08622 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 568fe9bf-8019-33cf-a712-e2bc232e3a75 | -9.62733 | -48.54773 | 2025-07-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 238f0f21-64fe-36ad-8c34-a999290fcf6d | -4.59898 | -43.31293 | 2025-07-30 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3b4aa1d4-1cdd-3297-a76e-012df96a5e61 | -7.1383 | -44.36101 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2778032-2276-3198-9f1a-05bdd5ac53e2 | -5.7432 | -39.77447 | 2025-07-30 04:02:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
