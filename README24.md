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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4a0d1f5-c1ae-30d5-ae53-329738975c24 | -6.52569 | -55.04005 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1b2f3ad-8c11-3ffd-a073-a25da8b74fcd | -11.04168 | -50.91438 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cad75ad9-10d2-38ef-97c1-41c299a96796 | -9.13853 | -50.69925 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dfcedbc-c84e-3545-bf0b-664cc8f6ec9e | -11.84783 | -45.06665 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d31d28af-3056-3b66-a4ca-d05adb890902 | -9.02132 | -50.68936 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce9b02a7-4013-338f-9966-4119ebb97704 | -8.18363 | -50.29854 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1fc6cba2-4987-393e-ab7c-3ebae29c780c | -8.61881 | -54.96616 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bce5d217-da47-3220-b766-00ca373d66ec | -10.27303 | -44.37669 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4966ca8-2867-3f51-ade9-9caf7dc0516c | -10.91906 | -47.07053 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6a8d6064-d3b0-32fa-ab4f-86aaa01fe685 | -10.92007 | -47.07323 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 47fe0e67-e73c-338b-b4f0-54e71249dac0 | -10.73744 | -50.48157 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73a57414-c6ad-3b25-a5a0-c641ceda8ef0 | -10.3978 | -51.6017 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04f65ee1-ee5c-39f1-887f-2ba214b0da5a | -11.95653 | -45.48663 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79ffb743-4240-34bd-8d20-bd3b8b8a9978 | -7.32634 | -47.28343 | 2025-10-07 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 753cc962-6116-3edc-b037-2761cffa10b5 | -9.33684 | -54.52467 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a02c9ca-8f8a-36c2-a379-92d941a42e03 | -7.89219 | -47.81403 | 2025-10-07 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c7ce43f-3d7a-3090-86db-c382e211c1ad | -5.49575 | -43.07539 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4fc2fad6-cb45-359d-9841-428c2ca17fd8 | -10.74489 | -50.48645 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a7a1397d-9e03-31ff-8e78-b9f64d6624af | -10.26279 | -44.37502 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53c97bba-4776-39c4-805b-8f76bd248f76 | -11.74305 | -43.29324 | 2025-10-07 04:08:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a9e16cf1-3f57-35ce-96bf-a79367148f06 | -8.64794 | -46.28152 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a526b2e-e90e-3423-aabe-dec8a9d012aa | -6.50036 | -41.5514 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 29138066-d592-3879-b9ef-431221f5e424 | -11.8078 | -45.05161 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2654dd12-22c5-35a0-9684-f4b8bb77eeb4 | -4.69095 | -45.8465 | 2025-10-07 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 47e409c7-96b6-3257-8dd5-5f334af5e579 | -5.65316 | -43.18604 | 2025-10-07 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 11.3 |
| f317a038-6cb8-3838-a6b1-b8c64cedb5eb | -11.10297 | -47.19986 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d6358fc-e989-347f-9f81-68883d3dfd19 | -10.99055 | -51.21627 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ef5fa3f-8851-3c6b-a28f-ac6623734087 | -11.46688 | -43.48991 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8213bd3b-0045-3aaf-a25a-14aa47e93e3a | -7.68255 | -42.58082 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 80d6a7d6-3d35-35b2-9d10-3625910d5574 | -9.91815 | -49.96193 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 55f53def-8c6f-37c1-a905-aa36dc93d053 | -11.02625 | -50.91449 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb585db3-f779-3e71-881e-d6cd806c59b7 | -11.67281 | -44.2645 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d18e0eb9-cbca-3e80-8022-bd04313c229b | -5.29874 | -42.5431 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e099bea8-76e2-3e2a-92c0-f70a9d59082b | -7.63651 | -43.06462 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e675d70-5b07-34f3-a031-7d745ff2faed | -6.64611 | -42.76083 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ff8958f9-ba8a-3339-ac92-95f47563d7c7 | -7.06672 | -42.77043 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d44573b4-4a51-3016-a1bb-78c7e0b4eaa8 | -8.66117 | -46.29115 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 419724a4-49f8-3b99-b141-7297c4b9cb0b | -11.84108 | -44.91532 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 180b409e-bddf-3bab-a636-90c2621ca250 | -5.87098 | -44.29984 | 2025-10-07 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a31b30c2-c7ae-3cc3-9007-708eeb507c16 | -5.66972 | -44.26503 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f5c42b8-4e93-3b04-bcf8-329dc30b6737 | -10.25817 | -44.38197 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19e1c945-be6d-3641-83c5-b07131ae8814 | -8.61459 | -44.91037 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2054a41-5573-3e9f-b331-91f25a337be1 | -8.5386 | -46.2606 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86e8020e-f37c-355c-8b1e-396fd3644f79 | -11.84847 | -45.06281 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ff5d44c-cd6d-376e-ad49-687e98f7fb5e | -5.89101 | -49.36996 | 2025-10-07 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9fd3b660-27a1-3c94-b6f3-2546986faad8 | -9.0143 | -41.17862 | 2025-10-07 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 10e47894-a14d-383d-a25f-89feffb69ef8 | -10.89776 | -47.10239 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef8ab618-41c5-37e3-81d4-6085ab221cad | -7.52084 | -42.9771 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 517454ec-9518-3b2f-8ffb-5638699d8b8d | -8.49482 | -46.3115 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e05e8eb8-acc6-3023-a006-a410f2ee0469 | -6.72548 | -42.83924 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1ab182a5-d5d6-3a9a-bd9c-2f122f331a07 | -7.73321 | -42.38895 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 373c00c5-c07a-3a97-9196-b16a7ef144cb | -6.14699 | -44.02959 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 098bb8d4-ba8d-3398-a5d3-837999dc8537 | -8.54019 | -46.25097 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 14e8f721-65a7-3de4-b5b9-7477378a5c48 | -5.48839 | -43.07795 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| aa5a1d0f-a28c-347c-a69e-357b28290e26 | -5.09884 | -46.15473 | 2025-10-07 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f06f2b8-eae0-3b3b-b308-8d44905c0013 | -6.70277 | -42.85686 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 3721636b-a7da-3110-aa9c-a63e6bba53a7 | -8.55463 | -46.25834 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ca3d95d-6e50-3814-bbe3-308122b51f84 | -6.25186 | -43.89964 | 2025-10-07 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc0a157c-937d-3224-8552-9b437a2e635b | -6.70163 | -42.86409 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c43a5495-5ff0-3edf-bae3-53b7efd93599 | -10.39843 | -51.59834 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69d23392-9177-3c39-9979-472bbd807375 | -7.7786 | -44.19791 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 652c52f6-9afa-32e1-8f7a-3af6e6246a77 | -6.70111 | -42.84567 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cbc4146d-2291-318d-9193-11073be07e1a | -6.1621 | -44.09172 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 015ffca1-307d-3099-a803-08b5399a11ed | -11.50406 | -44.97445 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4965c053-5518-3b89-b595-45752aac60f5 | -5.33651 | -43.38767 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63d55e90-8c7a-3e50-bfc3-1c47b59b3dc1 | -10.89667 | -43.82009 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d025eb9-573c-3ce2-afc4-f4d11906b651 | -6.64277 | -42.76032 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b129ba62-4976-3497-933d-caa9f2c409c0 | -10.38868 | -45.40742 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65ab4399-9cfb-3002-b52c-6107714836ae | -7.01781 | -42.78012 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 17f89026-e13a-3062-a399-c9c9a21b3fb9 | -6.2579 | -43.27396 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d779f24a-634f-3566-9eaf-ba7f7d619e5f | -6.64397 | -41.95953 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5e05225a-1798-3684-a3e1-4035576bf052 | -7.67481 | -42.58676 | 2025-10-07 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 66e22867-732e-3881-8a43-d931a549c105 | -6.69932 | -42.18806 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c95bf50a-45bc-32fa-9a4a-922f80bf8e46 | -11.67904 | -46.34396 | 2025-10-07 04:08:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f339be9a-c62f-3f99-96c2-2dd9b5054867 | -7.02361 | -42.29324 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f8896e9-810d-34ea-af27-981e8d466496 | -5.63861 | -42.63335 | 2025-10-07 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| efddc0c9-e96b-3107-afb8-42dd2a4b2d76 | -7.62983 | -43.06355 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c65530b-0df9-3752-8195-508e0430fcad | -7.99685 | -43.80393 | 2025-10-07 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3d6b2be9-2944-323a-bcd4-59a8534be1d4 | -7.69796 | -42.39762 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6aa51fbe-3f2e-35e1-a754-1cf549e5cc6f | -10.26901 | -44.37989 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fee2883a-97d9-30c6-89d2-a0a96bd61ec7 | -8.64333 | -46.28574 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e673922c-b3ab-37f2-a534-81f809bb70b8 | -10.89269 | -47.13235 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5917b17-a39c-3268-b92e-90f2484fccec | -7.78978 | -42.61272 | 2025-10-07 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fdedfc61-fbd4-3d6f-8033-ea5479b57622 | -5.24923 | -46.55455 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d03a4f32-5477-37f3-bc18-857a16358653 | -11.94649 | -46.42754 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e93ac12-fce5-3f61-817a-1cd9780eccfa | -8.86152 | -46.79192 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4a6a902-e8c3-30b6-be2b-3f154e2d129a | -11.03229 | -50.90966 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d07ad765-bbcf-33e4-aaf5-08bba6eaefdb | -11.77449 | -45.12995 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 21eb8ac6-6380-3216-9324-06d6575e8f69 | -5.59623 | -44.42433 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d72b9ca-bd93-32cf-be3e-fd121593e9d3 | -8.55161 | -46.25295 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfe4994d-97cf-343b-b2a9-57f348988707 | -8.52638 | -46.26346 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc2bd75f-fa25-3027-8551-b63d4cf71ae0 | -11.84565 | -45.05837 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af6816d5-03c9-3515-b92c-b800ae29e1d3 | -11.94722 | -46.44546 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| faaa342e-de16-32a8-b11e-3ad5fa65989b | -8.27366 | -43.82875 | 2025-10-07 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78ba27c0-f802-3a05-b33d-76da3424620c | -8.60909 | -44.92173 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce07fffc-baf9-3e38-a55e-ba3b32f17dfb | -6.35688 | -44.61492 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90d949ac-bf68-359f-b8f1-83c67060aaa8 | -11.88754 | -44.95433 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74d527ed-3569-3c01-b928-9409b2bba8a8 | -8.48577 | -46.29518 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51290589-8581-3975-881c-28e4d2cd432c | -10.4034 | -50.30719 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96d120f4-d9cb-3dbc-900c-b239e56abb6b | -8.54863 | -46.24724 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README25.md)
