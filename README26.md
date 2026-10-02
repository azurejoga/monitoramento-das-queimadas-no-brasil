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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d2456f5-3c52-3eab-af8a-8c848df1870a | -7.8682 | -44.169 | 2026-10-02 03:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c6cb44d4-879b-3bcd-a640-08fbd856809b | 1.8221 | -55.5654 | 2026-10-02 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b9704f4f-2eb9-36bf-88cd-e9276fb65687 | -4.2676 | -50.7506 | 2026-10-02 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 658ce3e5-590c-3574-9623-bbcf7a030d91 | -3.1299 | -53.7431 | 2026-10-02 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 5606d490-43f0-3402-a38e-0e9b5e069655 | -3.1483 | -53.7426 | 2026-10-02 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 21095f54-81ae-36a6-9a18-e99fc9642428 | -11.1615 | -44.6002 | 2026-10-02 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 304.6 |
| 1eb9b5e3-8265-3eef-882a-98853cfe5d38 | -5.7355 | -43.2916 | 2026-10-02 03:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 9592bea5-2df4-36b8-992e-7680efe15aac | -6.1487 | -47.2651 | 2026-10-02 03:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| a2a06dd5-6e89-3611-9957-721baec8a01c | -3.295 | -53.8597 | 2026-10-02 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| db028b6c-34a5-33c0-839c-c9b36977c068 | -3.1299 | -53.7633 | 2026-10-02 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 79a7f518-8d97-34f1-8ae7-acae777be936 | -11.142 | -44.6261 | 2026-10-02 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 1de73a2a-c88e-367e-b90c-e20c5b56a583 | -6.3952 | -56.4158 | 2026-10-02 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 14cf0526-3906-3050-ae9b-c2e07d903877 | -2.0577 | -56.8591 | 2026-10-02 03:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| cf22b862-d582-3f70-8d2d-3d9074311beb | -3.2951 | -53.8395 | 2026-10-02 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 686e4370-f409-3da3-ab74-7c99810f8cf3 | -11.6767 | -43.6106 | 2026-10-02 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| b6698f11-f18f-3ceb-98a1-c52694c3bb03 | -3.2767 | -53.84 | 2026-10-02 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 25f905cc-1bf4-39ae-95f9-36ac3dd57359 | -3.1838 | -54.104 | 2026-10-02 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| eaff093e-f0fe-3f48-a7a6-685c305bc993 | -12.9995 | -51.2976 | 2026-10-02 03:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2e58c346-0205-3706-8cca-fffb022a39fb | -11.1424 | -44.6029 | 2026-10-02 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| a7ab7190-53fe-383b-87ac-bae839cf5dd7 | -10.2678 | -49.6616 | 2026-10-02 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ed20da54-cb08-3968-9c63-46ea2eefe689 | -12.9998 | -51.2763 | 2026-10-02 03:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 80d92c90-68ef-315d-832a-157fe7e51d6b | -11.7541 | -43.5749 | 2026-10-02 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 37b0086c-6f59-3556-925e-f8ed5b103eec | -4.4506 | -47.9329 | 2026-10-02 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 21584177-79f4-32cd-a0a9-0877745fc10f | -0.94189 | -47.55779 | 2026-10-02 03:51:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd712a8d-023e-3f95-a49b-6442b0dfdde2 | -6.24137 | -43.77337 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c63a9d3-db07-3b70-ad39-8c61629eb850 | -6.70965 | -44.83327 | 2026-10-02 03:53:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 633503df-b3fd-35e1-a575-eb4224be7f5a | -6.24194 | -43.77013 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a3e3bc9-08b2-3689-85b7-a225fdd00df9 | -5.74772 | -43.28416 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f5037695-2548-3c1f-8f1e-368445c33ed8 | -6.90281 | -43.6812 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0212c7dc-1acc-3975-b9b5-393734cc4895 | -6.33455 | -43.35901 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a623c80-3af0-3864-8edf-17e6f5a19b37 | -4.45307 | -47.91652 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6a8dd49a-51ba-3d7a-9b81-9dab3a15799e | -5.76735 | -45.14632 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3e90b17-4b17-35df-ad30-9bce5eb91bec | -6.15089 | -47.26853 | 2026-10-02 03:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| adde4a58-cc3b-36d2-b10c-35bcf2057db8 | -5.76527 | -45.15798 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7162783f-855a-3749-b829-3f2aa99df160 | -4.45997 | -47.91781 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 486156f8-3137-36e9-adca-bb4ae00c6101 | -5.73159 | -43.28701 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c375a5f9-029d-3b6e-8f87-732794c8cb38 | -5.7546 | -45.15162 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cc58e536-64af-3e77-b6f9-5094589e386a | -4.45703 | -47.93114 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| de39957c-49c0-31ed-98b9-6c5c0e361b26 | -5.58205 | -42.72949 | 2026-10-02 03:53:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 67bc7068-c8d6-3b85-bd39-d28179181daa | -4.0157 | -38.32201 | 2026-10-02 03:53:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1c668008-eabf-36e8-9d7c-a910920b238a | -6.72009 | -45.57253 | 2026-10-02 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4aaa1c30-e0b9-38bb-82f2-6a4dfa739bcf | -4.45078 | -47.92938 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| de670288-bc9f-3217-818d-7f0a5fbfe3b4 | -3.97826 | -41.51603 | 2026-10-02 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 24948bda-8d67-3f3e-8171-93fca06e25d5 | -4.45939 | -47.9183 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c68b46cf-9a28-32d0-b980-a9853df5615a | -6.90227 | -43.68423 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48107682-b675-38fe-a739-dd49dd4fe3dc | -6.90174 | -43.68726 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9b79e826-b5b7-3e6e-8fcf-00660f01a5b9 | -6.20344 | -43.28782 | 2026-10-02 03:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06d46e80-0250-36e6-84a1-6b15ea98f8c2 | -5.73663 | -43.28796 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 90a4c420-1962-3f1b-b2af-5795b6646d6c | -5.87467 | -43.59415 | 2026-10-02 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2809ade9-3380-3d96-af83-0049f3e77685 | -6.24708 | -43.77127 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b235a4f-31be-3050-96d6-3e17e0b36b72 | -6.14517 | -47.47257 | 2026-10-02 03:53:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c0153d3-b419-3721-a3db-4763fead05c9 | -5.74371 | -43.27736 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 992aadc3-439a-38e7-bab7-380998de80d9 | -3.41348 | -39.28341 | 2026-10-02 03:53:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 1a9c2e33-3ba4-30fe-b903-66f1d7186b8c | -2.60437 | -48.25308 | 2026-10-02 03:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0281e0c-1eca-3116-9907-d5609cc9d8b5 | -6.70901 | -44.83689 | 2026-10-02 03:53:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80438728-29a7-3870-9e64-fb0bd176534d | -6.33627 | -43.37907 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 485ab45d-22e3-3bb3-97b6-8b6048354523 | -6.24251 | -43.76688 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c5e6a3e4-408f-39ec-9a3c-81498d6a969e | -5.73371 | -43.2834 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f55fe9c-5c02-39a5-ba7a-cf4ecaf949c1 | -6.90842 | -43.67915 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 07713ed2-1d1f-3fea-8d67-34802785c015 | -5.75888 | -45.16071 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daba5ecf-912b-3e04-8c38-1152cf8c54eb | -5.74319 | -43.28029 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7451edf8-c8d2-370f-8055-5059d7b684ea | -6.24653 | -43.77441 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fdd24999-6f95-3550-8e82-33615aff6541 | -5.76384 | -45.16597 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c19eee65-a1f3-3bbc-b349-228f1ba7993f | -5.75666 | -45.14015 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d3db28aa-f27b-388e-a532-e9a405079ad5 | -4.45821 | -47.92472 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 24db6904-2dc3-36a7-897d-760fa2704085 | -6.91298 | -43.68309 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a8a3c7d0-ad25-3030-bf49-13d2b269168e | -5.75599 | -45.14389 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bd4cbddf-a01a-37fc-9b98-281dc84f6d90 | -5.74889 | -45.15055 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e427581-313e-3263-94a3-898e744e1c3d | -6.33678 | -43.3761 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f922f9be-6280-344e-9006-98dde1e4fe4f | -6.72083 | -45.5685 | 2026-10-02 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec97f185-72fd-30d6-a4aa-44aa63b111c7 | -6.14539 | -47.26198 | 2026-10-02 03:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 82b92356-62c0-318e-a03b-e36e0eb717d1 | -6.34743 | -43.3683 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16840fb9-fa70-3f8e-a512-e04188286c62 | -5.73714 | -43.28508 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| edaecc57-efaf-3a9a-a16b-da809eae6b96 | -4.45883 | -47.92424 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 64ccd799-d6d2-3e5f-93ca-0863492556b1 | -6.2128 | -47.47352 | 2026-10-02 03:53:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fff6824-ea0d-3e01-8454-525fdc01cd20 | -6.92219 | -44.56311 | 2026-10-02 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbab0f02-44da-3a38-86b7-0f6701d92a33 | -6.24764 | -43.76806 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fc989ebd-47d8-3219-b2ff-c22e62558efb | -5.7539 | -45.15554 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9014112-6a00-37b0-8070-5e281cf77f99 | -5.76099 | -45.14888 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c052f50-c047-3691-b9fd-e116ac0617cf | -5.22019 | -46.02516 | 2026-10-02 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ca5fcc0-89f9-3c55-be92-3ee6ad65dcdf | -5.72771 | -43.51768 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30bf56ee-2ca1-351e-a57c-c17239d0bad9 | -5.55063 | -45.26054 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3aba7b9-1ebc-3ae4-b40b-ea0bc216f019 | -5.11115 | -37.4457 | 2026-10-02 03:53:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d349550-6a46-3a02-89b4-d3296f860098 | -4.45769 | -47.93067 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c3ca254f-021a-3892-a316-106c5d85b67b | -6.18685 | -44.08406 | 2026-10-02 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 349127c8-bd92-352b-b6c1-a4768b4315cc | -5.9546 | -38.62799 | 2026-10-02 03:53:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45657f9f-eee2-352d-87a6-0dbbc9e8ab43 | -6.894 | -43.70131 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dec5f19-f7d7-33ff-bf9e-83e8dfe6a849 | -6.12743 | -43.72075 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1665f4b7-d6d4-36f2-a618-27c9c89c709d | -5.4209 | -36.83271 | 2026-10-02 03:53:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e81fa3b4-cca7-3d5c-808b-9bca7082bd23 | -6.3295 | -43.3582 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0f3a094c-ebba-3355-8b42-0665e8bb022d | -5.76666 | -45.15016 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdd3fe73-ed46-3dee-bc03-5a0af6a704b0 | -6.33073 | -43.38108 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d839600-d88e-3562-a62d-0bd57a428b39 | -5.7603 | -45.15275 | 2026-10-02 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4d40ce2-f583-3f43-9659-76d07f293ad7 | -5.72718 | -43.52069 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcbd62e9-0062-3729-a49f-624e08fa21f5 | -4.45131 | -47.92345 | 2026-10-02 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e44d6dc3-cb33-3812-8aa3-bcf364fbb984 | -6.12687 | -43.72392 | 2026-10-02 03:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e2403b0-858e-3c04-97e4-3eac91fee383 | -6.34027 | -43.37922 | 2026-10-02 03:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5237378d-fcdf-3ff1-b94d-d06245d600d6 | -5.74268 | -43.28318 | 2026-10-02 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e7a129f7-d06f-3434-91fc-84132eabc5c6 | -6.90121 | -43.69025 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 24874f48-4007-31e3-a277-8f7c7cf8e3b4 | -6.89454 | -43.69828 | 2026-10-02 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README27.md)
