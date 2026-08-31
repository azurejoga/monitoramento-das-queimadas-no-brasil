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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7b952b3-74aa-34f0-8233-2cdafc635c69 | -19.07952 | -57.40596 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b5c01064-c70d-3a04-8d11-e46770fa054d | -28.99348 | -52.51208 | 2026-08-31 04:19:00 | NOAA-20 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 93629bd5-231e-3326-9dfa-9664f2c451c7 | -20.36522 | -47.46485 | 2026-08-31 04:19:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aaa9d8cd-0c82-338a-a9e8-71a0938dfd31 | -20.44812 | -47.59419 | 2026-08-31 04:19:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eda1945-f5fd-32f5-aa3e-b26ca06d6f68 | -20.36663 | -47.45663 | 2026-08-31 04:19:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e61663ec-305f-35ec-9e50-d58441a00302 | -19.15627 | -57.40063 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4a5c69cf-4051-3910-8565-f861e43fdea4 | -20.36592 | -47.46074 | 2026-08-31 04:19:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65b6c693-b020-31fd-886f-5c79c5c0a93e | -19.12979 | -57.41925 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b4c41071-d5f8-3cc1-b4b2-33c272a1725d | -28.99244 | -52.51351 | 2026-08-31 04:19:00 | NOAA-20 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5848f2cb-8b96-3b23-a0b3-f1f76e74b665 | -20.3701 | -47.45731 | 2026-08-31 04:19:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 69835d42-6305-3347-a582-7ec6f0bd7d5a | -19.15373 | -57.41137 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| b19d0650-34ab-35c3-8625-ef01c35f790b | -19.11723 | -57.41593 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 722c79a9-34e5-333e-b20f-6fceffb594d1 | -19.15987 | -57.40437 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 276f4778-f299-3556-bc18-bf12c9f01b41 | -19.1536 | -57.4027 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 10ff19d1-d9ac-3e2e-a288-696bd81b37af | -20.36939 | -47.46142 | 2026-08-31 04:19:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 720f70a5-cbeb-39ba-b19e-dc7d3de2638b | -19.16128 | -57.40765 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 3f6f7499-7e3f-3661-b39b-af55ec073103 | -20.25273 | -58.1604 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9cb90e90-9ced-30fd-94f6-4d4a1908a474 | -19.155 | -57.406 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 333c4baf-9c9f-30e3-a543-28af1d7a5f8e | -8.7442 | -46.4437 | 2026-08-31 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7b1928d7-7f1c-372f-b88d-c31e0b3fcdf0 | -6.1294 | -57.6833 | 2026-08-31 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ec304f13-ffff-307d-9b6d-69c5e61d473e | -6.1295 | -57.6637 | 2026-08-31 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a1d6d592-e83f-38e1-a948-80464f9b48cb | -5.2548 | -55.8907 | 2026-08-31 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| a66bcdae-7cb1-3bbf-9397-b8035b359bb3 | -6.622 | -58.5965 | 2026-08-31 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3da72ae9-6b7d-3e9c-b70a-061e4f42bec2 | -6.1111 | -57.6645 | 2026-08-31 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 173d07f0-aa96-3abb-afa6-186aa0b67341 | -5.2363 | -55.8914 | 2026-08-31 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| fd6d8da3-f8b9-3c17-89f4-26c9cffbb3d9 | -5.2362 | -55.9112 | 2026-08-31 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 82bdec20-a92b-3cd9-81d6-bfd6acc02685 | -6.6036 | -58.5972 | 2026-08-31 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 4634d637-d440-3a46-b31b-89bf557d0d23 | -5.2547 | -55.9105 | 2026-08-31 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 149dd816-c31d-3937-9a47-46df17135e9d | -5.2363 | -55.8914 | 2026-08-31 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f63846b4-3e5d-3a7f-ba5b-2b903220d89e | -5.2548 | -55.8907 | 2026-08-31 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| f33ed732-9628-3193-96d8-04c57f96a9e8 | -5.2547 | -55.9105 | 2026-08-31 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 406bd2a1-80b1-3291-b302-276ec88aa518 | -6.1294 | -57.6833 | 2026-08-31 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d1668fa5-e042-325d-8aec-7f0c1c328ec6 | -6.6036 | -58.5972 | 2026-08-31 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 27aa3b60-8c6a-3fd6-a257-e1d368317ac9 | -7.9239 | -44.2327 | 2026-08-31 04:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 87622f57-9f09-31d3-92a3-779be1b73c5a | -6.1295 | -57.6637 | 2026-08-31 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 3e6dd57f-008d-3907-82c1-c6fb13c6c757 | -5.2362 | -55.9112 | 2026-08-31 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| e148da80-c44b-3d42-adb6-6d8109e455cd | -5.2362 | -55.9112 | 2026-08-31 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7d6b1798-1c13-326b-9c68-42f91ceb61ec | -6.622 | -58.5965 | 2026-08-31 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f5833f45-e9c0-3322-9034-5de15e3b25aa | -5.2548 | -55.8907 | 2026-08-31 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 87375c18-b548-304b-aa76-e715bec6a0ac | -5.2547 | -55.9105 | 2026-08-31 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| d6900f16-fb61-3b15-9254-d5135fb366ce | -6.1295 | -57.6637 | 2026-08-31 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 7357e6ae-7dc6-3031-835f-237f49b8cfdc | -5.2363 | -55.8914 | 2026-08-31 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5e88208f-3595-3493-bcad-63a210837c95 | -6.6036 | -58.5972 | 2026-08-31 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 9a6d06d8-186c-3e20-bac2-19cdc893f52e | -7.9239 | -44.2327 | 2026-08-31 04:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a29fcca4-13a0-3067-ac85-190018f4ba5f | -6.6037 | -58.5779 | 2026-08-31 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 0edb8e2f-b2b0-3ed3-95a2-e035be4a190d | -5.2362 | -55.9112 | 2026-08-31 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 8649084a-7f95-323a-abde-c05c25177ea6 | -5.2363 | -55.8914 | 2026-08-31 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a7c1e409-ae75-38e8-b109-29db204ffae7 | -6.6036 | -58.5972 | 2026-08-31 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.0 |
| c44ad7c5-e462-3878-80bb-bd23c4264db4 | -5.2547 | -55.9105 | 2026-08-31 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 6f0cff8f-f7c5-3d8c-9236-3a775edf56e6 | -5.2548 | -55.8907 | 2026-08-31 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 10f5e2ea-4d1d-3bb8-b39c-8c5ce65d4275 | -6.6037 | -58.5779 | 2026-08-31 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 7e719038-db7e-31fe-aa01-bbb3561390e0 | -6.1295 | -57.6637 | 2026-08-31 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e03ad6c2-c455-3bb8-a137-9740167fe8f9 | 2.22816 | -50.75399 | 2026-08-31 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f880339d-216b-37ed-b930-c3bcdf7c8fe7 | 2.22759 | -50.75037 | 2026-08-31 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9837ff97-7c79-3f0f-95e5-bc305f74faf8 | 0.09421 | -51.09117 | 2026-08-31 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 801e4c0f-dd4d-38df-86d8-2677714bc5d6 | 1.10162 | -50.9751 | 2026-08-31 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a769b6cc-2d69-3d9e-8865-e380c2f8a16b | 3.22858 | -60.13951 | 2026-08-31 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d8ce0056-8cc2-3b0d-9efb-122ff2acddc5 | -1.11963 | -47.98462 | 2026-08-31 04:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d44a1f8a-d37c-3aa5-b0ba-aa517d50ebef | 2.12912 | -50.88352 | 2026-08-31 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b32025f7-388f-3af9-b55f-d3f69dd91a43 | 2.25581 | -50.75338 | 2026-08-31 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c17adcff-8f80-37a0-8949-979102779899 | 2.2417 | -50.75187 | 2026-08-31 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26c9c92f-a649-3524-973b-7dae665879bd | -6.86394 | -56.57355 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6fa1cb5e-c582-320d-a52d-141722021bb6 | -5.94576 | -57.69154 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 86d13a4a-894c-3710-ad11-4debf917c8eb | 0.00919 | -60.59586 | 2026-08-31 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 113c3355-b68c-333c-b059-b0f5130ecc57 | -7.27803 | -60.65284 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c6022a9-6c25-31ae-9509-9b4f819421dc | -6.12193 | -57.69191 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf19a24a-0db5-314c-bee2-9c896599e621 | -8.21583 | -54.94416 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 954fe952-08fd-3745-94e5-c5519403a8df | -6.85945 | -59.42796 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f4f9a8d-f631-33b0-85db-725d8b10630c | -6.93188 | -55.64412 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2006a5d-acd5-312b-8405-7fffa031ca27 | -8.39066 | -46.47231 | 2026-08-31 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19a1a2d5-e5a5-3376-8e3a-dcd02658382f | -6.73961 | -56.34262 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e101e03-2ac5-360c-92df-363160ee9731 | -7.2944 | -60.58344 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 530c1758-97d0-3b55-9fee-e7ede3b1dde6 | -5.25279 | -55.89019 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 44e3773f-e735-3971-b06b-514893b51ffc | -6.15775 | -55.96031 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f2bb2dd-b9ec-375f-8751-b789770d8476 | -7.54612 | -47.32679 | 2026-08-31 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76f9d1b9-d2c4-3b85-9b7e-b279a6d0bfa5 | -6.02657 | -57.74723 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42d89eed-4d29-3991-9471-17e716361b45 | -8.74631 | -46.45108 | 2026-08-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a643d245-de88-3379-8552-eda2c846d192 | -5.89811 | -52.10675 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 524430ef-df32-39a6-b99a-38bf9a84bdc9 | -7.30946 | -60.59879 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c023c3d-c007-3523-ac86-093b6355a434 | -6.18917 | -55.52205 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f99c5b6-9856-3386-8e0f-8a0e78ef508f | -3.88842 | -59.40212 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acf6f269-dd35-3b64-9569-2afdaa0ee0d1 | -6.92 | -55.71891 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| af2bc4b4-b6d7-3c8a-8bc7-cb90e8eb2daa | -6.25063 | -55.48067 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c65c2a4-0d18-3274-9bf1-0d6229bf8197 | -6.42608 | -55.53078 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f98e31c0-84a1-3aac-8fe7-dee90de09ea4 | -7.52411 | -55.3406 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60300364-803c-37eb-92e3-495a5b8d2bd7 | -7.31876 | -60.59612 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f396452-490d-3a27-b20d-eb2ac1a4080c | -7.9593 | -52.44769 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d95bc50-00d4-3110-aae8-eb5d97b706d8 | -8.13145 | -45.49002 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c17f71e4-74c3-357a-95e6-272c5ca0d70e | -7.49422 | -55.31432 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 989d201a-6d65-327f-b483-0717a7633292 | -6.20758 | -52.98774 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a796c0ef-2e6c-3807-8356-e6e797e11a23 | -6.60827 | -58.60561 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6a30c554-b857-3ae0-b214-e8813a00eacc | -6.08049 | -57.89708 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9693b38c-bb26-368b-8f97-120a305cdbd2 | -8.15344 | -45.47222 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f15a518-53b8-33c7-a465-19473db4f94d | -7.61644 | -55.29479 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1aeb123-70eb-3566-8aa4-7a2dc26da5a7 | -6.86388 | -59.47562 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf2cb4ca-d734-32cc-a00e-416606550a22 | -6.75444 | -56.33753 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0636e7e0-61ff-370e-a69d-d4b90ba404c0 | -6.77975 | -55.67807 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f90a95c-fc14-3c11-a7cc-e243135f8683 | -1.62461 | -55.16726 | 2026-08-31 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8775e213-420c-368d-b1a4-813c058fde2c | -7.22004 | -60.6693 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32e58c5b-bcfd-3182-a92f-ebbbc78a977d | -4.96492 | -55.84512 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README37.md)
