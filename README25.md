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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d18df20-405b-325f-8290-2536a90183d2 | -6.37783 | -45.59728 | 2025-08-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b56fed61-f76c-3646-8f94-bf96af4ac706 | -6.04579 | -44.38091 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ed95ec9-e0b1-3e95-9788-109dc333354d | -7.2886 | -44.52819 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ef7fbf0-3fc4-3f60-b031-694516b0b47c | -2.7814 | -41.88198 | 2025-08-25 04:14:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fb74a16-bd2d-38dc-a7e0-34c7c2e05cfd | -9.52732 | -40.31435 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ab73fe0c-8b25-37dc-acee-e85dacfa5be8 | -8.32406 | -47.25942 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c133531-d2cc-3504-afc6-eb9b71041685 | -6.49886 | -44.79027 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2339e16-ed67-3fdf-a4fb-17adef2520f0 | -8.12389 | -47.1308 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1902802-9972-3300-8110-0b9c2b664b52 | -6.79727 | -44.32283 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 548d5527-88bc-37d8-8b50-e42d40511451 | -7.32745 | -43.41736 | 2025-08-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78f96574-5210-3be6-bf79-8487276b360f | -6.29723 | -43.76051 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8c2ee34-5fee-3b4c-a5d2-b2719c9334ac | -7.29084 | -44.51404 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d4438a4-af11-3265-888d-8853b594fc26 | -5.48873 | -37.26118 | 2025-08-25 04:14:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 351c146e-126f-38aa-b9bd-1ee6b1407cf7 | -6.23065 | -44.78115 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4807a2e6-355b-3bdf-acfd-f8aaa3712749 | -6.90788 | -44.41676 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26759323-f12c-3bae-9ad5-e7b2c88aaf76 | -6.31601 | -43.77049 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57d90f59-c829-3fb6-9718-a51a254a0909 | -6.52861 | -44.4287 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bc0ebf49-e1b5-3fce-b11a-499a093247ae | -6.03925 | -43.99397 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b04821b9-bd5f-33c2-b18a-171875ed442c | -4.95927 | -55.81982 | 2025-08-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05fa3c85-93ff-3e03-b1f3-737bbe4bf480 | -5.29913 | -45.26896 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fffa0f5d-88df-3c76-bb8b-a19aa2269af3 | -7.50817 | -45.83765 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2847c341-4ead-38ec-a0b9-244c1e7da794 | -6.79284 | -44.32933 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10ae723f-91b7-3547-b37e-da6d3eac9048 | -7.96538 | -42.63557 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e2c5ef5-2cad-3151-86d2-cadd427acb9f | -9.51992 | -40.31324 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a144471-15bc-37ec-877a-858431df9077 | -6.56429 | -44.11702 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8d57faa-b789-30e2-9650-94fb90dd00d1 | -5.74903 | -51.70093 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b0b4ce-d3be-39d5-b095-cd7941562aca | -8.54726 | -48.85823 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7968c433-3191-36ac-b7f9-c93c20412b37 | -7.30224 | -43.66495 | 2025-08-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d307f32b-fdfd-3911-924a-032a87a78243 | -5.73675 | -45.38823 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 230ef123-e0bd-3acd-a5e3-412eb417769f | -6.48975 | -43.42225 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5957041-ef1b-3cb1-b037-f11ca07648f2 | -8.22463 | -49.56271 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2b8fe9cc-9097-3f78-88f7-4499532f8e0e | -6.02515 | -42.80402 | 2025-08-25 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 075f85c3-a939-3956-8f23-600ff8ac5d06 | -7.91452 | -45.88617 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c0b614-d829-393e-a934-7e8137dbaa5d | -5.50284 | -41.41618 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 77ee5681-a286-3784-b897-6c507af2eff1 | -3.43328 | -49.04727 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5f428667-a94e-3772-b83a-e35d2c98540d | -6.30884 | -43.77293 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 342111a0-84be-390e-97c3-18f9830ac936 | -6.4265 | -42.78242 | 2025-08-25 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7e80ac0-c037-300f-8f06-00de5230e6b4 | -5.84527 | -45.16901 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c50e318-2329-35f4-ad9a-e2b440404e80 | -6.44125 | -44.55276 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d6e283d-7b84-32e6-8968-8944513c2222 | -3.44214 | -49.04868 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 968c1caf-4b8c-3112-9432-c71eb876cc9a | -6.28673 | -43.74105 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 843f7f0d-eec8-3fe6-8f6a-bde946c9df4c | -7.30807 | -44.53487 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1c0f926-f60a-3bb7-9792-e56caa8a77e8 | -3.79402 | -51.18693 | 2025-08-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 772ff1ad-1d6f-31a4-b467-fae8bdbbc13a | -8.23986 | -45.09004 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ab46d38-8d60-3953-8739-c951db305f06 | -5.49097 | -41.40322 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| afe35cb9-c9b2-39ab-8b85-eb76540fc07c | -5.36625 | -41.21243 | 2025-08-25 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e72092cb-da86-35c2-ad45-07df93e38c75 | -7.64883 | -44.98078 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ee69b9c-bd3d-37ac-b255-b0c500098b43 | -7.47107 | -45.02288 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f677decc-6367-36ad-8e0f-86833342387b | -3.43334 | -49.05215 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 86433fe0-185a-34d2-833d-2311658e438d | -6.79172 | -44.31477 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5576dcbd-09ee-309b-a74d-8ed3cda4136b | -7.57657 | -45.23759 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0944b5de-64d1-3217-92a6-516000eb2120 | -5.39413 | -42.35726 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d7596c46-667c-3422-ae8a-ed9023201fb3 | -7.66149 | -42.66773 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a853649-6695-362a-b0d6-390f374887c8 | -4.41593 | -45.23549 | 2025-08-25 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa8dd78b-241a-3658-b453-c4f5bcf25cd0 | -5.49213 | -41.41818 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 75a96c1f-35e8-3b0b-ab21-cf166a5c6f58 | -3.5983 | -47.52539 | 2025-08-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1479f704-1e49-3dc3-91a7-03cc0a90d0c5 | -7.3153 | -44.53239 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 092bee5d-f916-342a-821f-1cc7673cfe77 | -5.39028 | -42.36021 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2a08536d-d70f-318f-b3af-5a28487846ef | -6.89052 | -47.92546 | 2025-08-25 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5153ee8a-a8a6-3ca8-ae31-b1241a5ad684 | -8.12681 | -47.13582 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12fbdd61-a3ab-3a39-a8c4-e6552a45bcdd | -5.10444 | -43.21001 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d9066a42-cc4a-336d-b324-512f7fe8a14b | -8.15842 | -45.06967 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b3b415c-b96f-3ba6-b5cd-61087da37ca0 | -3.43404 | -49.04776 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 05602447-0f3f-3161-83ee-34556e02067c | -6.91845 | -44.41483 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de715347-01de-3741-9367-5ae118183f28 | -5.9055 | -43.4178 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c29719e-c3bb-31c3-8043-dcdc39eddf05 | -8.11586 | -47.13388 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0bb487c-6391-3f2d-84df-0216a10fa870 | -6.67597 | -44.42303 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac1ca6f2-f0e8-388d-a9c0-84270af1ec66 | -6.87334 | -44.40039 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ae9ea7e-9168-3304-8d89-0343bbcadadd | -6.69912 | -44.01681 | 2025-08-25 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4dbe3ca-8dbd-3a6e-8099-38d0cff5e2b0 | -6.89041 | -45.66132 | 2025-08-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 35da6c45-dfbe-32b0-babd-dd38f06223f1 | -8.9056 | -47.33074 | 2025-08-25 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47346cf4-f333-3962-b36e-1a1f1ae0719d | -7.08083 | -44.07761 | 2025-08-25 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dd406f9-0d71-32d8-9984-a152b826f3c6 | -7.92145 | -45.88724 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31274aa4-5651-3491-b2c4-582f65d312d2 | -6.24645 | -43.73833 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af253e7d-181a-342b-8ca9-2c0c5a4560c2 | -8.59665 | -43.99947 | 2025-08-25 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc16766b-e69e-30f0-9eb5-cc508415f5a8 | -5.68556 | -45.13631 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ae8e9b5-aec9-3845-b3f8-166a637ac8c1 | -6.43341 | -44.55888 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97224b0b-f6fa-3d80-ba35-90ddccb22ea1 | -3.93297 | -55.75797 | 2025-08-25 04:14:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8dc923d-5394-346e-a5cc-9425592792a0 | -8.06746 | -49.66887 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de3bfea4-7d1f-3ac0-8b4d-b3f792f767f9 | -4.95819 | -55.82597 | 2025-08-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| afba370c-4809-32ad-8af5-fd6191e5387f | -6.67988 | -44.41996 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 116a1875-a893-3a8c-8d55-be563bf4132d | -5.53282 | -41.28991 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f83a436-f888-37b8-9491-744c553388fb | -7.74651 | -43.91313 | 2025-08-25 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cba07e5-b913-3c51-a904-a47d65e12d00 | -6.02899 | -42.80106 | 2025-08-25 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 699195d0-01f9-34c9-a53f-436cab4dbcd2 | -6.0529 | -44.44391 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5579aac2-81e9-3149-a8f0-fb3b7f298aeb | -7.20372 | -49.61296 | 2025-08-25 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46c8d7b2-3e81-3528-ac73-ba29ca64a627 | -5.49229 | -37.26408 | 2025-08-25 04:14:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99040205-33cc-3b52-a2d1-03f2b1607c64 | -7.09249 | -44.62438 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bcee440-889c-3d48-9607-a133593f3d82 | -7.59016 | -45.23965 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10e147f6-358e-39c2-8a24-f3341e222a5c | -7.92429 | -45.89162 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60510eb7-5bac-3743-a055-16f837dc9af0 | -8.06248 | -49.67222 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e1dab9a-cd63-3d8e-a75a-732a8b8bc821 | -5.52923 | -44.2051 | 2025-08-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6be02af4-675a-3fee-a44b-21b2b0746225 | -6.45392 | -44.61748 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 81eefe3b-0d8f-3c38-b74a-856a885abe3c | -6.14182 | -44.39658 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a30b976c-d50c-359e-b48c-6b0bff02536c | -7.33095 | -43.78667 | 2025-08-25 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 275b54f2-5033-311e-bbc8-08df91632b4e | -8.28262 | -47.23997 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f324a04-a099-334b-8189-fb9dcb2e6dcd | -6.05716 | -43.68676 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7be2e27c-0afe-3728-9cd1-7d879df2312c | -7.96818 | -42.63961 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fd252c0-e71d-3d4c-a5e6-973b8b15b3c5 | -7.29583 | -44.52572 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a0e489c-10a2-3806-9fa6-90b4cd0d11f2 | -5.68497 | -45.14005 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README26.md)
