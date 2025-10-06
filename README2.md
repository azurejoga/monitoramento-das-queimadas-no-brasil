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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d0b11f6-443e-307b-ab29-3c02a13078ee | -17.8818 | -57.5794 | 2025-10-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 8525acee-b794-3007-b7ac-75d7afcdbad7 | -17.9605 | -57.5904 | 2025-10-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 38b821e2-ee36-32a7-8b57-a2022dac0359 | -18.1968 | -53.3638 | 2025-10-06 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 2cd5738c-278a-37ab-9e19-7844c8b3a4cc | -17.8815 | -57.6 | 2025-10-06 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| acd58d70-8900-3c84-a7d9-7d66d74de1f7 | -5.2858 | -43.3014 | 2025-10-06 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 68254c53-fa1a-3782-b155-2891be191496 | -14.9018 | -51.4965 | 2025-10-06 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 8dd26ab5-b3a4-334b-9b1e-05076532d4fc | -13.1325 | -47.9936 | 2025-10-06 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 3dcaf6d0-b9e4-3011-ab5b-4877f7500686 | -5.6373 | -45.9705 | 2025-10-06 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6f88ec67-2f51-3742-81ac-71152ced5226 | -8.6141 | -46.3003 | 2025-10-06 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 52d62fa4-1b03-3b00-a4c0-846356f983ec | -5.7881 | -45.8034 | 2025-10-06 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c439b364-c3fc-38b4-97ba-66f47320201a | -14.9161 | -46.8312 | 2025-10-06 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 828c6a26-e311-3606-9c57-1a0047caa270 | -14.55 | -46.6662 | 2025-10-06 00:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 2541f914-29a0-30d4-a45e-cadaca1d7186 | -18.1963 | -53.3853 | 2025-10-06 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 262189bb-1f46-31bb-8dd5-b5da64256df2 | -9.3165 | -45.9779 | 2025-10-06 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 72dd6ea1-4395-3d43-86de-b7d8da8c14c0 | -5.6373 | -45.9705 | 2025-10-06 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4f71d399-a3f6-398a-997f-00b54d5913c2 | -9.3162 | -46.0005 | 2025-10-06 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 97467608-7cdb-39bd-8571-ba402127310d | -5.8067 | -45.8021 | 2025-10-06 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 20fc0ee5-4081-3433-90b8-b7bbb3bbe8bd | -8.6141 | -46.3003 | 2025-10-06 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d86d1bd4-a419-393c-bc1e-2a5272acb076 | -17.9803 | -57.588 | 2025-10-06 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| a789c3cb-4109-33e0-b938-6998e969925d | -5.3285 | -47.2963 | 2025-10-06 00:20:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6f332ebb-8987-3dfd-bb48-53c07ee9aaef | -7.0181 | -42.7818 | 2025-10-06 00:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| a20a7745-8060-3d43-ab51-1333a3d8417b | -11.0154 | -46.5168 | 2025-10-06 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 9f468394-ed81-3d00-b1c0-7f2c9156c0d3 | -12.3793 | -63.7294 | 2025-10-06 00:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a7ca36d7-276a-3eaa-b5ab-1a9bfdb6ff9c | -5.2068 | -46.1546 | 2025-10-06 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4e5880f7-abb7-34c2-a758-156b0140b28e | -4.772 | -44.4434 | 2025-10-06 00:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 3010be68-ddb7-38b2-9803-16f243edc14c | -18.1968 | -53.3638 | 2025-10-06 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d6622140-b121-3a45-b9fa-75ae459a2e71 | -10.9851 | -51.1443 | 2025-10-06 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| cbd885ca-3c46-308a-b669-32a1a3d9ee34 | -17.9605 | -57.5904 | 2025-10-06 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 9ecb8eb5-84a8-341c-8c3e-56616081f71d | -4.6505 | -43.1805 | 2025-10-06 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9f010d63-1df8-38fd-9dba-677a2179777d | -14.9014 | -51.518 | 2025-10-06 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f02639fc-ccb4-3555-bcbe-3bfbca8d1bd8 | -14.5442 | -46.9405 | 2025-10-06 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4c6c8579-c153-3d91-990d-2823e15f3d6e | -5.3287 | -47.2744 | 2025-10-06 00:20:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8b74faaa-d2fd-3559-9cd2-23aca88582e7 | -14.882 | -51.5207 | 2025-10-06 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 6f66856f-9b8a-36d4-ac7a-867104042e86 | -4.7533 | -44.4445 | 2025-10-06 00:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 87b72f01-0569-323a-b462-ea977dd89514 | -18.1366 | -53.3946 | 2025-10-06 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a1f5b176-1828-33fd-89a4-e40457a432dd | -17.6852 | -52.2398 | 2025-10-06 00:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 9d70e388-d221-3ee7-a648-8daae30f0a41 | -14.8824 | -51.4992 | 2025-10-06 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| e012304f-819b-3faf-b5a5-06e3989d865f | -18.1167 | -53.3977 | 2025-10-06 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4b31ee74-816c-32d8-983b-bbde6eaae737 | -14.863 | -51.5019 | 2025-10-06 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 04790e3d-1a06-3c69-b610-1ed6c95ba3c2 | -11.0151 | -46.5393 | 2025-10-06 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 939b696b-fb25-335b-9130-64d26b1b912c | -5.4178 | -47.7934 | 2025-10-06 00:20:00 | GOES-19 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7e29ccf6-0ec8-3c4f-a06c-1d721750111a | -4.7718 | -44.4663 | 2025-10-06 00:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 91a4e8b1-f31d-3019-84be-9a2d253af03f | -5.1882 | -46.1557 | 2025-10-06 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 739f00bb-cb5e-354e-bdbb-0f3e79b9ac4b | -12.4468 | -45.5646 | 2025-10-06 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b98bdcf5-72ec-3b71-ab22-abfcd9e92908 | -17.8621 | -57.5818 | 2025-10-06 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| d154ee1e-d72d-3460-869c-47d5ba70df58 | -10.9848 | -51.1655 | 2025-10-06 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 700ed8fa-1e78-3038-a250-62aa6210bafa | -14.5695 | -46.6629 | 2025-10-06 00:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| af12a668-5def-32f9-bddd-f259d573143e | -14.6897 | -48.3797 | 2025-10-06 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9ca47e6c-730d-340a-bb9e-cf2297cb77f3 | -12.5791 | -46.7294 | 2025-10-06 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 77e21c8f-65a9-31d7-af8c-4a8b8807c1bc | -14.6897 | -48.3797 | 2025-10-06 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1f438c51-0c10-3bba-a8b1-fd967b00b4b7 | -11.0342 | -46.5369 | 2025-10-06 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a338fab8-bbc3-3f91-8fa4-0d96cee3fb16 | -4.772 | -44.4434 | 2025-10-06 00:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4da364f4-9392-3c2b-8de3-92d350e64c0c | -14.4932 | -47.5374 | 2025-10-06 00:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 89d6c21a-35d5-3b57-a803-ad9132d5dab4 | -14.5442 | -46.9405 | 2025-10-06 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3a5cf6b3-a24f-3a62-9d94-847f7450355f | -4.6691 | -43.2026 | 2025-10-06 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 0d6dc2ac-2c8c-332d-a813-50d7ca6b1aad | -10.9851 | -51.1443 | 2025-10-06 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| edde8f17-4b3c-338a-9356-a6d13a1bb9aa | -17.4045 | -42.6186 | 2025-10-06 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 92d14bb0-7906-346d-a0db-9d0d565482b0 | -8.1879 | -44.2283 | 2025-10-06 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 455ac693-85c9-369d-b66a-2a8f03308566 | -5.418 | -47.7716 | 2025-10-06 00:30:00 | GOES-19 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b57a4104-5c34-30de-a775-f4103ad5dc4c | -17.9803 | -57.588 | 2025-10-06 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.4 |
| db7c4a12-4dde-336c-9d88-1c210a57a1c3 | -7.0181 | -42.7818 | 2025-10-06 00:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 2aa6d4ee-05ad-39c1-8a89-07f74ede02bb | -17.9605 | -57.5904 | 2025-10-06 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| d44a47ea-6e0a-304a-9764-430d1e2c18d3 | -8.6141 | -46.3003 | 2025-10-06 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 75249745-c233-39cd-bf82-3f2115e3626b | -18.1167 | -53.3977 | 2025-10-06 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 75.2 |
| aaf30970-7ba5-386c-b2b4-f0579f479a81 | -5.1882 | -46.1557 | 2025-10-06 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 7df8e934-a4bd-34c9-b788-56d8c1d7c9e4 | -4.6317 | -43.205 | 2025-10-06 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 92bbe03b-2b5c-3c75-8409-06c61deebde6 | -18.1366 | -53.3946 | 2025-10-06 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| f6fe18f4-b1ae-3816-bd09-7d8e8748cf73 | -14.882 | -51.5207 | 2025-10-06 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4ed78903-73f8-336b-a1c5-c6654d12df7e | -8.6138 | -54.976 | 2025-10-06 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4f8b871a-b1cf-3eea-8b2a-bab3e0099ae1 | -5.3285 | -47.2963 | 2025-10-06 00:30:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 65e2c104-020b-3280-ac86-0636a0a4f607 | -17.9998 | -57.6062 | 2025-10-06 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 3307fd2e-0d79-3302-a25a-33a6ed7441d4 | -5.656 | -45.9692 | 2025-10-06 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 25e10337-d288-305d-9b24-6d7dc699d0b5 | -4.6504 | -43.2038 | 2025-10-06 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 2c6271ee-23c4-38d6-ba9b-c48166affc45 | -4.6505 | -43.1805 | 2025-10-06 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| ca19410b-6f43-33d8-99f0-e58cc5833f4a | -9.3162 | -46.0005 | 2025-10-06 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 432b7275-9404-3692-9ca0-acb5f99642a4 | -15.6007 | -52.5529 | 2025-10-06 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| faaccced-e656-3d7e-90fe-e210d0b57984 | -5.4178 | -47.7934 | 2025-10-06 00:30:00 | GOES-19 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f7f83e45-3b3a-377e-abee-1e2e03359901 | -4.6318 | -43.1816 | 2025-10-06 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 470f45bf-3722-3864-8351-2d5e3640b776 | -2.5967 | -48.134 | 2025-10-06 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1394242e-5865-32ad-95c0-9b9d4ad773f6 | -5.2068 | -46.1546 | 2025-10-06 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 2b6b97cf-1d64-34c7-95da-4dfa4277e5d7 | -14.6703 | -48.3828 | 2025-10-06 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ab6a526b-b2e4-3ce2-a756-16ae4ee5a2cb | -14.7096 | -48.3542 | 2025-10-06 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| afc08953-a7db-3f27-9829-28ea1b20678c | -4.7533 | -44.4445 | 2025-10-06 00:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 8d8dbb32-7ccb-39f7-b734-9ae873f2534c | -10.9848 | -51.1655 | 2025-10-06 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5ffab3e0-c15d-3862-98c5-5c709212aa78 | -13.1325 | -47.9936 | 2025-10-06 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f99672d7-f3b6-30c6-8400-79aeda8e6c35 | -8.1876 | -44.2514 | 2025-10-06 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 99a39205-8b25-39b4-b135-7386c6d0b31e | -14.5438 | -46.9633 | 2025-10-06 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 63c12bb0-05b5-383f-88e9-9a280e42a851 | -2.5968 | -48.1124 | 2025-10-06 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 22887e17-ac50-3c1d-acfa-053e326ce0f1 | -8.6327 | -46.3208 | 2025-10-06 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 941d1d3e-a2ca-39fa-a2c8-2fea41c5d215 | -17.981 | -57.5468 | 2025-10-06 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 5d8dcbf7-5a60-3feb-a7c8-8c053f60e42a | -14.55 | -46.6662 | 2025-10-06 00:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3286ab8c-0fff-393e-be8f-37485020a862 | -11.0151 | -46.5393 | 2025-10-06 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fed1b8d1-b596-3296-8473-2b7d1c584fb9 | -13.1325 | -47.9936 | 2025-10-06 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 0d93d358-bd54-3ca1-8f70-a69c5d9aec40 | -5.3287 | -47.2744 | 2025-10-06 00:40:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d2627835-085c-33d6-aa5c-50f7fd3164dc | -14.9161 | -46.8312 | 2025-10-06 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 9b4b45da-a388-3f6c-98e1-da00cc7da83e | -6.5735 | -49.8695 | 2025-10-06 00:40:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 6b7fe634-2581-3406-82f8-7b791b1d7504 | -4.772 | -44.4434 | 2025-10-06 00:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 6cc2d7e0-25ea-33d3-ab7a-3decdef20718 | -2.5968 | -48.1124 | 2025-10-06 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 99cd3f3d-e349-3cb5-b183-2ec13902b7f1 | -14.9489 | -47.1214 | 2025-10-06 00:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| cbd75fe6-8eb9-38b5-a9c2-85c309f96abe | -12.5791 | -46.7294 | 2025-10-06 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |


[Clique aqui para ver as próximas entradas](README3.md)
