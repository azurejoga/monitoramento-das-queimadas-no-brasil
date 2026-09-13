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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbcd739c-f433-3dfb-9b28-18207d06c689 | -7.9645 | -43.9971 | 2026-09-13 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2f9f92bc-97e5-33dc-a21d-4a72ded8c6eb | -8.5417 | -54.6985 | 2026-09-13 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 936727c9-18f1-34df-9b24-dccc7ce19ee5 | -8.4292 | -46.0271 | 2026-09-13 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 4146794e-c986-39ad-b769-68b5edf4a514 | -9.1339 | -51.5927 | 2026-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f7b2e834-7db2-311a-bc8a-4b7f3c7703f5 | -5.2723 | -56.0483 | 2026-09-13 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5f002a27-5f69-3727-93a6-0df980f9050c | -6.0255 | -59.9484 | 2026-09-13 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 9b8a2fb2-a7ed-3aae-915b-fd19f2ddf09a | -3.7462 | -61.7552 | 2026-09-13 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 74f0799f-0b02-3cea-b61d-befd88b10aca | -7.3652 | -45.3615 | 2026-09-13 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 18fa904e-374d-38c9-ae86-a97020cba245 | -3.5345 | -59.0401 | 2026-09-13 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3f10cf7b-4954-371e-b173-2f82f0e1a9f4 | -8.2956 | -51.2003 | 2026-09-13 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 98906bb4-9f49-38cb-bf05-20bb83369d91 | -9.5129 | -45.4568 | 2026-09-13 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 402ddf88-b5fe-377c-af6e-f1eeddb874ce | -9.1526 | -51.5911 | 2026-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9ee2ca0e-c360-3c13-a832-40ea658ea171 | -13.3055 | -51.3235 | 2026-09-13 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4e9f5857-4886-3820-9d68-c0a75cecf6b5 | -10.2926 | -45.3161 | 2026-09-13 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| a19aba10-ff88-3b08-8176-d60854afbf03 | -11.3723 | -46.8299 | 2026-09-13 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 7fca9a42-4b23-3f85-bb84-e62d15258d61 | -8.5415 | -54.7187 | 2026-09-13 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 23e6f026-96be-315a-9c96-4d91d4ca3c83 | -3.1697 | -58.6437 | 2026-09-13 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 1a6cc269-bac2-3467-b8f0-831bf75d03cb | -4.1223 | -54.0158 | 2026-09-13 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 211.7 |
| 46711bab-85f5-3afa-a32e-960c11da3460 | -2.6602 | -57.5313 | 2026-09-13 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| dad28c74-fb99-3255-9a63-c21d3fbd93e4 | -10.8223 | -50.5879 | 2026-09-13 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 198c3e3e-ae7d-379f-9d08-9fd2805ad8d6 | -2.6785 | -57.5115 | 2026-09-13 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9be9defb-66c8-3b6c-8d9e-c5a8fce9ef89 | -10.6824 | -54.1884 | 2026-09-13 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| f93f347c-3cd5-3428-a54e-b93bebd3760c | -3.8461 | -58.9178 | 2026-09-13 14:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a6b7b158-ee31-3f96-8a9b-e058fe636374 | -11.3825 | -43.9849 | 2026-09-13 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 7b78a2a7-b1b4-3666-a0fe-25f4fbc5941d | -10.5667 | -51.3349 | 2026-09-13 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 7644e02e-dd5a-3dbf-a855-f1d0ed99dcd4 | -9.4137 | -50.1317 | 2026-09-13 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d13d9b84-ed47-34ec-b167-49fa3e7707e2 | -6.3015 | -59.9387 | 2026-09-13 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d3a0b55d-28f0-3b69-bc66-eda70fb964ad | -10.6829 | -54.1475 | 2026-09-13 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 370.3 |
| c513137c-2fc2-3cb0-a8d8-1b00477e68b4 | -10.7018 | -54.1458 | 2026-09-13 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 1ffe8eb2-d707-3289-827e-6273ee785728 | -11.372 | -46.8524 | 2026-09-13 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 357.5 |
| 8bbda92c-7de8-3706-b710-67e856468846 | -11.838 | -46.3834 | 2026-09-13 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 968ebc9b-ee4f-3ef1-bbb7-e716a8fa1060 | -11.8189 | -46.386 | 2026-09-13 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 6a5cc63f-deeb-3ca8-8f33-dc1d18821a6e | -1.3007 | -49.1464 | 2026-09-13 14:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6a220567-d7bf-3b73-bcd9-58b24f6ca37a | -8.6001 | -44.4609 | 2026-09-13 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| f29f53e4-86e0-329c-afb5-d48448e9f5fb | -10.7274 | -50.6192 | 2026-09-13 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7737d3e1-8ff4-30c5-b79c-f43a485a5a11 | -9.3948 | -50.1334 | 2026-09-13 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 1cc8ee16-0439-3f55-8990-ecaaf6bb7551 | -7.12 | -42.107 | 2026-09-13 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| a6478211-03de-3405-b680-89a325813ac9 | -10.2922 | -45.339 | 2026-09-13 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3d28c728-10d1-31b5-8c75-9ef7684adc7b | -3.3292 | -42.3129 | 2026-09-13 14:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 928e66a1-719b-30b5-8a43-af20a08c619d | -10.6431 | -45.9999 | 2026-09-13 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 776415ad-61df-3ff6-9b3c-527e1a283cea | -10.9861 | -49.7131 | 2026-09-13 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| d8d3988e-f8ab-376d-8fd1-b6006b048585 | -15.3793 | -52.9864 | 2026-09-13 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e4f4a781-0db4-3754-a1aa-a615e1302226 | -13.3247 | -51.3211 | 2026-09-13 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 945dbece-a719-3798-b628-965bdac34ed0 | -7.5394 | -44.9133 | 2026-09-13 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| cceb612c-2ef3-3301-9208-1b4af32085fd | -3.4058 | -59.2538 | 2026-09-13 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 8a8c23ec-3008-310c-8ca7-d655fa437bae | -11.8193 | -46.3633 | 2026-09-13 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 2f1a7045-251b-3c25-9d06-3a4a7e022cae | -13.4507 | -48.48 | 2026-09-13 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 02abdd82-467c-3c65-b4df-6542133c7cc7 | -9.1339 | -51.5927 | 2026-09-13 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| be465663-68e5-31a9-99b4-358912b09df9 | -2.6602 | -57.5313 | 2026-09-13 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 3adfa816-ad3a-32c4-88ff-e26c8c682337 | -8.5415 | -54.7187 | 2026-09-13 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 7bf3392e-7088-30d9-9bcc-85547f7bb711 | -9.3763 | -50.1139 | 2026-09-13 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 9955ecbb-adf2-3d99-b4c3-35a22f6e5a78 | -11.0433 | -47.1633 | 2026-09-13 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 195023a6-9a5f-3c8b-9ab6-aba53ccea98f | -11.3021 | -44.2074 | 2026-09-13 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5a62abea-15a4-3fdd-88aa-f54f3bd808e1 | -13.3758 | -51.7193 | 2026-09-13 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 35f2e0f8-c2fc-33d9-9a15-594fce2237ed | -8.2956 | -51.2003 | 2026-09-13 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8c014f8c-7470-3908-a360-8bc6cf648495 | -15.037 | -48.5021 | 2026-09-13 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3c75029e-1a31-3493-b67e-6938106d4fef | -9.5129 | -45.4568 | 2026-09-13 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 4b18ae88-b853-3c8f-bbaf-dcf2b2a80331 | -9.7038 | -54.3507 | 2026-09-13 14:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| af7093c2-7bc9-366a-9962-074fc0f843f9 | -9.3852 | -49.3847 | 2026-09-13 14:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a1e7496d-5e4c-32a9-9109-438ea3d7c34c | -3.8461 | -58.9178 | 2026-09-13 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 5448d65b-4791-310f-bcf7-608fe2917b2a | -3.7462 | -61.7552 | 2026-09-13 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 23d7fb79-acc6-36ad-af9c-903a1d6464a1 | -15.9184 | -42.5472 | 2026-09-13 14:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 1267adf9-7ccb-348e-807d-ef049fd1a817 | -9.6752 | -46.0273 | 2026-09-13 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e090dc40-e977-3022-814d-054ad18ac994 | -10.6824 | -54.1884 | 2026-09-13 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 62fb3f03-4718-32cd-b82b-85e7dc961db9 | -3.1697 | -58.6437 | 2026-09-13 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 68dac823-d174-3b9b-a584-ed9275cbf025 | -9.3765 | -50.0925 | 2026-09-13 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 12a85bd4-e731-35a7-b3fb-5a6693599278 | -11.8189 | -46.386 | 2026-09-13 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 5fd8742d-0fc6-3857-87a7-35e4594a93b1 | -3.354 | -58.1961 | 2026-09-13 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 152.7 |
| d856c077-2877-3b4b-b52f-2e1f032e1920 | -11.3633 | -43.9877 | 2026-09-13 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| f64df3f7-f42c-3d6b-9df8-baa5d5ea997d | -2.7149 | -57.608 | 2026-09-13 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 53f17f0f-a200-3003-90e2-0c4f2c09c2df | -6.2832 | -59.9202 | 2026-09-13 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 60bde785-6b6f-3f9f-b902-a53f28aadc2d | -8.4292 | -46.0271 | 2026-09-13 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d12e9442-555a-3790-9eed-a4f80ec6fba3 | -10.7535 | -46.2347 | 2026-09-13 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 38f10634-b5f3-3dbd-a93c-a162472788fe | -10.5667 | -51.3349 | 2026-09-13 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 54be14ea-acd1-398a-9508-c9600da7c26b | -11.0429 | -47.1856 | 2026-09-13 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 491f057f-fe06-3b12-86b0-eb5f66c304ec | -3.4058 | -59.2347 | 2026-09-13 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ffa1657a-ed1b-34af-83a5-698142e2b91f | -2.9395 | -50.3784 | 2026-09-13 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| edde6d4d-0b03-3d07-b80b-4318e53a455a | -10.6829 | -54.1475 | 2026-09-13 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 339.0 |
| c2f4ecd0-f1da-3777-ac0e-8520cd7e3d13 | -11.3513 | -45.7922 | 2026-09-13 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 7d19aa17-1265-325a-96dc-adfa78c09307 | -8.2203 | -55.2427 | 2026-09-13 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 31c61640-4801-3c65-925e-58de60d29fa2 | -2.6785 | -57.5115 | 2026-09-13 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 092ca431-dd6e-377a-a2e2-492c15eeeaeb | -10.5664 | -51.356 | 2026-09-13 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| d86860b5-d0cc-3e22-80a6-9da57efe4b53 | -10.7018 | -54.1458 | 2026-09-13 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.6 |
| f04e966a-0a46-3633-9b13-95c0b88392dd | -2.6602 | -57.5119 | 2026-09-13 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| be2aeed1-9782-31d1-9993-44c348d7a898 | -3.5893 | -59.0773 | 2026-09-13 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 1b0c7c3f-a83a-3cc7-8a1a-15b7d65c0a17 | -3.6076 | -59.0769 | 2026-09-13 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2fb311a3-cda9-3c87-ab33-43ddd39e2e20 | -8.5417 | -54.6985 | 2026-09-13 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9c0fe2c0-e6fe-3252-a219-94254d9bf3f1 | -4.1223 | -54.0158 | 2026-09-13 14:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| dc91ce5e-dbfb-3787-9231-8bdfdc396583 | -10.312 | -45.2907 | 2026-09-13 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 738decd8-36e7-312a-be7d-dd563c10a0a0 | -10.5192 | -47.9141 | 2026-09-13 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 21118473-bf9c-361c-b27e-bbf9bfabc660 | -3.4416 | -59.5213 | 2026-09-13 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b7740746-03a5-3bd9-bf12-5af741f2d04a | -1.73 | -55.843 | 2026-09-13 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 21d8038f-b50d-350c-9e0a-4258b33d4525 | -6.3015 | -59.9387 | 2026-09-13 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 36f3e27f-bf5f-31b7-8903-a4e4946bfc22 | -13.3055 | -51.3235 | 2026-09-13 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b34cdc92-3828-3ee2-a42f-1512e64d6a12 | -12.1094 | -47.2907 | 2026-09-13 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 77384b49-e396-33a0-9714-82051360d654 | -10.5854 | -51.3541 | 2026-09-13 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 7646c7f6-15cc-3af1-b217-a474d2abb9ae | -9.376 | -50.1352 | 2026-09-13 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 699ad278-ed67-3fe4-bfb4-6190ed338e31 | -5.1255 | -55.955 | 2026-09-13 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 12e7f9d4-2681-363e-8337-baada57c0f29 | -10.2926 | -45.3161 | 2026-09-13 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 8c49e5a1-9a4d-3492-bec9-19368329281d | -11.383 | -43.9614 | 2026-09-13 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |


[Clique aqui para ver as próximas entradas](README66.md)
