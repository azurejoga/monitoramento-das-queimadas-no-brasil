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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7806ae9e-2804-3f00-8d40-72436542fa23 | -15.6903 | -46.2782 | 2025-10-05 11:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 234.2 |
| 69dad69d-6431-39f9-8425-b388ede46d93 | -12.7106 | -45.8452 | 2025-10-05 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 12b5adcd-9233-3e4d-aec2-2c6e63d23c0a | -10.949 | -47.1082 | 2025-10-05 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6427b12e-535a-3a9f-b051-2df7ea91453f | -11.8225 | -45.0827 | 2025-10-05 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 118598c0-ad72-38e9-ad16-7cefc3e036f2 | -10.9497 | -47.0634 | 2025-10-05 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 13a2549c-4584-3769-9f1e-5ccd695fecf9 | -12.7106 | -45.8452 | 2025-10-05 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 6bdead87-1eb6-334c-8b82-67b9edd3f65f | -10.9501 | -47.041 | 2025-10-05 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 9b49b927-8a5e-30dc-9406-2eda03c5100c | -10.949 | -47.1082 | 2025-10-05 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| eed903c1-bf79-3580-a72c-d9e9626944b4 | -11.8225 | -45.0827 | 2025-10-05 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0199afe9-2bd7-3aac-98de-f25a33c00e6c | -10.9494 | -47.0858 | 2025-10-05 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| cc3042a4-55cb-3dd2-8b78-d2c0dfe3a11a | -10.1954 | -46.7307 | 2025-10-05 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5b8aae74-1ca9-3467-85bc-7e2b55462e89 | -11.823 | -45.0596 | 2025-10-05 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| d2442ebd-9178-323c-9232-f1048ca73068 | -15.6903 | -46.2782 | 2025-10-05 11:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f7d6e0f7-556c-3a1f-9870-811d50210dae | -12.2688 | -49.1907 | 2025-10-05 11:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 6d8464a5-8871-38e6-86ff-9681eb71993b | -8.5953 | -46.3022 | 2025-10-05 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 08d2b469-a125-3fb3-8dd1-20606acf3e0a | -8.539 | -46.2855 | 2025-10-05 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 643c3b9c-5b11-3a0f-91ca-cd492b6b2553 | -12.8765 | -47.2712 | 2025-10-05 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 110900e0-180a-325c-8790-2d9c5aeee6be | -8.5387 | -46.3079 | 2025-10-05 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d0f6bf9b-1841-31bf-85f4-7c013f0d1034 | -8.5581 | -46.2611 | 2025-10-05 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| baf89f20-6c49-3e2d-83bc-6789ca57b86e | -8.595 | -46.3246 | 2025-10-05 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 314.8 |
| 9b1cf5a0-ee83-3017-8f4e-e28fa512bd82 | -11.8225 | -45.0827 | 2025-10-05 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 2a3c196a-1fa5-376f-85dd-e776d6d00737 | -15.6903 | -46.2782 | 2025-10-05 11:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 125.8 |
| c59e5a86-7de6-3260-93fd-d8561d12d2b3 | -10.9494 | -47.0858 | 2025-10-05 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3f990a3e-4471-32c0-9f63-7a2e6bda0205 | -11.823 | -45.0596 | 2025-10-05 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 52019ca4-fc1d-3ce8-b6d4-4a7ba81ef225 | -8.5384 | -46.3304 | 2025-10-05 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1748e983-2b15-3422-accd-d5b01bc35ff9 | -9.2973 | -46.0026 | 2025-10-05 11:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2736e4f7-f4ed-3db3-bcd8-c694419cc0a7 | -11.0316 | -46.6946 | 2025-10-05 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5e0f82b5-c3e2-35e1-bf29-ffef59b8999e | -8.5761 | -46.3266 | 2025-10-05 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 869bca7e-e3c4-346a-8060-e2b2e4c77968 | -10.9497 | -47.0634 | 2025-10-05 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c4651624-f0c3-343e-8198-5f5d56c38f4f | -8.539 | -46.2855 | 2025-10-05 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 531c77e6-9f03-318e-9b36-ef2cc5678f03 | -12.2688 | -49.1907 | 2025-10-05 11:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a65bd5cb-3630-36d7-9cff-a5a25004f175 | -11.823 | -45.0596 | 2025-10-05 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| b8998545-ac7c-387f-b003-15b57b4813e8 | -8.595 | -46.3246 | 2025-10-05 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 8453dc39-436f-373a-9e22-dfbaf19c7b8b | -10.6378 | -46.3396 | 2025-10-05 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1d71ecde-696e-32a4-a36e-7c28e073469d | -8.5578 | -46.2836 | 2025-10-05 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 635342b4-0c4c-3c6e-8367-4b54fd463ef0 | -18.1769 | -53.3669 | 2025-10-05 11:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 3f5af910-4750-302f-9ced-730a63c6f949 | -8.5387 | -46.3079 | 2025-10-05 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 983c1a9c-34e9-3ec1-8606-62e7bf508dc3 | -10.3907 | -50.3557 | 2025-10-05 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 14ad7465-c8e9-36ad-9b3d-16b991b9affa | -8.5581 | -46.2611 | 2025-10-05 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9762ccc3-b7a0-30f9-bd32-06cae50bd201 | -10.9494 | -47.0858 | 2025-10-05 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 704e1aa0-be02-307f-8583-a22f16c17710 | -18.1968 | -53.3638 | 2025-10-05 11:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 81f4fca0-3353-36e5-a90a-420cbf0bc62f | -15.6903 | -46.2782 | 2025-10-05 11:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 124.6 |
| d33442b0-e77e-36b8-8fe6-5f81ea2db392 | -18.1972 | -53.3423 | 2025-10-05 11:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 89.4 |
| dc468153-8139-34ab-9d31-fef9ceabb91b | -10.6568 | -46.3372 | 2025-10-05 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 204e84b0-b89c-3d3c-a0f1-126518dec15a | -13.7473 | -51.3097 | 2025-10-05 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 633f3c9d-52da-3e16-8da4-6720d6b3d68f | -11.823 | -45.0596 | 2025-10-05 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a5cac846-5d2d-3fec-8659-dc4a816e03d8 | -10.9497 | -47.0634 | 2025-10-05 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| c1167a61-5057-39a6-b966-afe89879ea98 | -15.6903 | -46.2782 | 2025-10-05 12:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 81d9947d-a632-344a-8a0c-fa4012e72730 | -13.7473 | -51.3097 | 2025-10-05 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 9674a481-1963-3e1b-9706-674452327398 | -18.1968 | -53.3638 | 2025-10-05 12:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 379.7 |
| 9b4ecde5-a0f7-3f8c-805d-aebc722f50a5 | -13.728 | -51.3122 | 2025-10-05 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 3c523159-fcf5-3b41-bc79-dd1a5b87a0d4 | -8.5573 | -46.3285 | 2025-10-05 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4b7ebb10-f281-37c0-a8f4-795c2b5be7a7 | -18.1769 | -53.3669 | 2025-10-05 12:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 1f29bb67-00c6-34bf-8aea-52c90a7a12e2 | -10.949 | -47.1082 | 2025-10-05 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| a9bc3174-d749-30c0-9917-09c83b693145 | -10.9494 | -47.0858 | 2025-10-05 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 22da994a-418a-36ff-8244-bbd4d52b1779 | -8.595 | -46.3246 | 2025-10-05 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f8e4183f-a3ae-3361-8f3f-ea855f336a29 | -10.8093 | -48.8229 | 2025-10-05 12:00:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 45a912a8-b7c5-3ea2-a684-825a73223de3 | -18.1963 | -53.3853 | 2025-10-05 12:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b388fbb2-a53f-3192-b431-8558aba13381 | -19.0155 | -50.6045 | 2025-10-05 12:00:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 133.4 |
| bf6102df-d396-3861-9969-57db27af0f89 | -10.9501 | -47.041 | 2025-10-05 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 095feee3-1250-3b94-9d32-77b7389c2861 | -18.1972 | -53.3423 | 2025-10-05 12:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a4da7334-f116-323b-9c13-76cfb2f77c85 | -8.539 | -46.2855 | 2025-10-05 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 2732a8d4-ebda-322a-b28d-1cabddaef742 | -11.0978 | -49.8513 | 2025-10-05 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 377fabdf-6903-34c2-8c76-098030298fd7 | -12.6913 | -45.8482 | 2025-10-05 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 88bff7a6-7fc9-365a-96dc-4a972d54424f | -16.0966 | -51.0829 | 2025-10-05 12:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 137.0 |
| a6729dc2-ea1e-35c8-980c-bb4527b31c84 | -13.7473 | -51.3097 | 2025-10-05 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 202.9 |
| a9f2be24-dc5d-3175-9e52-33a6c0c964b9 | -16.077 | -51.0859 | 2025-10-05 12:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 2530aff9-7ed0-31a0-bd40-c448339083cd | -15.9829 | -50.905 | 2025-10-05 12:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| fc503662-4f08-3e1a-b396-d02b18210275 | -19.0155 | -50.6045 | 2025-10-05 12:10:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 333.9 |
| 05b5f118-5b8b-3a71-a8e0-85e89b4f6677 | -18.1769 | -53.3669 | 2025-10-05 12:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 36463dd7-378d-3517-9162-48ef48842412 | -12.7106 | -45.8452 | 2025-10-05 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 264.1 |
| e786af5d-04c8-3f56-a3bc-ec92809789d7 | -12.8765 | -47.2712 | 2025-10-05 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 27e3f9e2-882c-361e-96b5-c0a90565acac | -8.595 | -46.3246 | 2025-10-05 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e4b3ed7b-db61-3df0-8fb3-deba54dae811 | -12.5863 | -54.7679 | 2025-10-05 12:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 80211e35-757c-3911-965d-dd973dbe3e40 | -9.6643 | -42.9296 | 2025-10-05 12:10:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 92.0 |
| f86dca75-6076-373e-bb68-d06da0b5ed8a | -13.728 | -51.3122 | 2025-10-05 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 2b9cd515-700d-3da4-9a47-92469265e914 | -11.8418 | -45.0799 | 2025-10-05 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 43701cb7-63ac-3a85-846f-ce03021a49b3 | -13.7476 | -51.2883 | 2025-10-05 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 6638ec1a-d85b-37f0-9dd2-406013e3295d | -8.539 | -46.2855 | 2025-10-05 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 87a37b2d-8548-3358-bbfa-7f44f1ae727b | -11.0316 | -46.6946 | 2025-10-05 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 95cfaaae-a22d-333a-9b92-2d363821ef0f | -8.5384 | -46.3304 | 2025-10-05 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ca3b490a-6a0f-374a-abb7-4c58448f0f39 | -7.8047 | -48.0558 | 2025-10-05 12:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 6b4739ee-1182-3978-a8da-d2ee70cbdd4d | -11.0978 | -49.8513 | 2025-10-05 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 10c953b9-6843-3526-a6d7-76b05923b260 | -8.5581 | -46.2611 | 2025-10-05 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| b6728b9f-68d3-3c2f-af82-ffd826aa55a3 | -9.3941 | -45.8336 | 2025-10-05 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 32bde7bc-b468-32e6-9279-4540f107894e | -10.8093 | -48.8229 | 2025-10-05 12:10:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c6ae0d09-f196-3ce8-8231-e57e004e29a6 | -18.1968 | -53.3638 | 2025-10-05 12:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 152243c8-4aa3-3fb1-b3dc-e153c420a535 | -9.3938 | -45.8562 | 2025-10-05 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a937ea73-083c-3a1c-8a1c-fcd12cac1354 | -8.5578 | -46.2836 | 2025-10-05 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 1b66bce1-59c6-3bb5-b6a8-e6821fffdf29 | -11.823 | -45.0596 | 2025-10-05 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 1f5e853e-fef3-37c0-b4c1-573064b79c21 | -10.4051 | -45.416 | 2025-10-05 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c9e896ad-abea-3c87-8648-17b4a14289ac | -19.0155 | -50.6045 | 2025-10-05 12:20:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 379.8 |
| f5bb7a27-364a-3504-a3d1-71f992bdfec9 | -11.8225 | -45.0827 | 2025-10-05 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d8145e22-8e3d-3e7a-abcb-62235ee65589 | -13.728 | -51.3122 | 2025-10-05 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 6216621a-de97-3294-9f48-9f243a203e15 | -8.595 | -46.3246 | 2025-10-05 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 05abb298-c639-3372-bbde-607ce688ecc5 | -11.823 | -45.0596 | 2025-10-05 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 82eaa3a1-dbed-3ce9-8cf4-b5205e6fca06 | -12.5863 | -54.7679 | 2025-10-05 12:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 26806876-e687-3893-af1c-435a28c861cd | -11.0978 | -49.8513 | 2025-10-05 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| dd131118-f0b7-3095-a5dd-71d7240a5390 | -12.895 | -47.3134 | 2025-10-05 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| d1f9b0b1-5d6a-3eac-9fb1-5b7fc8596148 | -8.5581 | -46.2611 | 2025-10-05 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |


[Clique aqui para ver as próximas entradas](README152.md)
