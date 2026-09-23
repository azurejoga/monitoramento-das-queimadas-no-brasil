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
| 50893340-77e3-3a5c-944b-e381b3624bcb | -3.8079 | -52.362598 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4a4c8d0-aba0-3674-8eb9-1119fb092a5a | -3.2363 | -46.926102 | 2026-09-23 00:58:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2729d5c9-8ffb-318b-b271-02ed6bfc7dd6 | -5.6206 | -45.2453 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bce8ff2a-0342-3857-bf4c-b899e5c2f309 | -3.6842 | -60.5546 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| baaa51a0-ee2f-3474-9715-a5a8124dc7e8 | -6.5665 | -55.399799 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68db5d30-663d-3856-8f87-d69c6f995cf2 | -3.156 | -60.072201 | 2026-09-23 00:58:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29012df2-9414-39b1-a6ce-5ce4a5ec9868 | -3.4506 | -50.610001 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d713a2d8-078f-3223-b406-8f1f979998c3 | -6.6775 | -58.5748 | 2026-09-23 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 8e285890-6526-34d8-9592-d45fb2236e02 | -10.6094 | -53.9902 | 2026-09-23 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 8c9b4e43-0454-3e46-90bf-2a755c9074fb | -6.6816 | -55.0502 | 2026-09-23 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 8ea415e1-8a36-3d79-a081-30f5780c2653 | -8.4985 | -57.6075 | 2026-09-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 3731e9e4-e47d-3464-8d44-1e9f90d9edec | -6.9214 | -46.5663 | 2026-09-23 01:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| afe22707-9a93-3533-bff9-380710183d5b | -6.728 | -59.423 | 2026-09-23 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 8f450f86-b54e-334d-a187-3deb2a3e6f81 | -4.3357 | -55.6659 | 2026-09-23 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 1796a448-9ec3-3a90-aef7-d5b3379ad32a | -6.7211 | -44.1618 | 2026-09-23 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 97e9edb2-ab4e-3d9a-99f8-b467dcc618bc | -3.2129 | -46.9383 | 2026-09-23 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3c5eaf83-42e3-3dfe-9c2c-b49552b705de | -8.4726 | -48.6927 | 2026-09-23 01:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 63636498-86b3-31ab-b84f-104b7c02c119 | -5.7565 | -45.1293 | 2026-09-23 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 5c6cb085-4cb0-3f68-9e8d-bca3d297e680 | -8.2062 | -54.7207 | 2026-09-23 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ae801f8a-dfe8-30e5-9a86-363da160210f | -3.2128 | -46.9602 | 2026-09-23 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 80de5f6a-34e6-3015-830f-42dbb6c07a8e | -8.8105 | -44.2757 | 2026-09-23 01:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 65802915-da1b-3261-ab3d-489996343144 | -6.6815 | -55.0703 | 2026-09-23 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| e2b4fbfc-17a4-384b-b421-3fe448dfa3e9 | -4.0925 | -62.0874 | 2026-09-23 01:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 4e5c0edb-a790-3f7c-b5cf-5e266f37ba23 | -3.6946 | -60.5835 | 2026-09-23 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| b35bc432-da3e-3c8c-80de-6bc87993e943 | -8.8108 | -44.2525 | 2026-09-23 01:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 28b5ed45-b3c8-363c-b2fa-a3958feabb0a | -8.5982 | -54.6341 | 2026-09-23 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3c6a6c72-5633-3bfa-a69e-69468559cd5a | -8.9108 | -62.391 | 2026-09-23 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 550cb669-1a2a-3ad3-8c02-8edc701e5bf0 | -6.6776 | -58.5554 | 2026-09-23 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 061cbfd2-34e7-370c-8a11-41d452e9df85 | -5.6246 | -45.2518 | 2026-09-23 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 7388746a-1277-393b-b885-5ed72705ca84 | -5.7752 | -45.128 | 2026-09-23 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 829761ef-6c6c-32e7-b531-66f7160bedc5 | -7.8811 | -61.1779 | 2026-09-23 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 15bcb4f9-ee84-34de-9288-19cb10372df0 | -11.7107 | -50.7891 | 2026-09-23 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 5d2bf5ae-e1a5-3611-8e37-338d2988738a | -9.1025 | -61.4299 | 2026-09-23 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 74e1a197-01ba-3017-94ae-95c95acfde77 | -6.1109 | -57.684 | 2026-09-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 758167da-6ec6-3a59-86f9-33e01c4a4cda | -12.4216 | -46.9551 | 2026-09-23 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 3433f421-2ed3-33d2-85b9-7dcdcc47b063 | -6.0925 | -57.6847 | 2026-09-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b1b12943-7b09-3238-8ad7-974d4a6c0669 | -3.2314 | -46.9376 | 2026-09-23 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 276.3 |
| 2e173269-5214-3fdf-94a2-335de5342892 | -12.402 | -46.9804 | 2026-09-23 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 79db28af-f5fb-3f05-b160-36b6b36b9e28 | -8.4799 | -57.6085 | 2026-09-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e7943bc3-db56-3b1d-ace6-011b5854b80e | -5.7567 | -45.1067 | 2026-09-23 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 905e5956-ec88-35ba-b1ac-3607c15d94c9 | -12.4212 | -46.9777 | 2026-09-23 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 233.9 |
| 0eba7676-ec6f-3809-803b-8a6744cb3fb2 | -3.478 | -59.5779 | 2026-09-23 01:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 063d2eaa-43a7-3dcb-a0b4-1adc122d14ee | -3.2313 | -46.9596 | 2026-09-23 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 1c5966ff-a009-3927-8159-98f4c83cfb87 | -3.6947 | -60.5645 | 2026-09-23 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 937d4e7b-5c3e-32ed-b315-993bdf9bb17a | -11.7297 | -50.7869 | 2026-09-23 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| b9b87ac6-ff8d-3b10-b205-2b1bac28c428 | -3.6947 | -60.5455 | 2026-09-23 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| d27d78a2-7f67-3a7d-998a-bbe6c7144443 | -12.4024 | -46.9579 | 2026-09-23 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ac316375-be54-3786-957f-6eba5171624f | -6.3134 | -57.7537 | 2026-09-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 2f3f152f-63ee-3945-a46f-4890cbfd1670 | -7.0349 | -44.6625 | 2026-09-23 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 8a08a6be-bb32-3495-972a-ba2f327d2e4a | -11.5307 | -45.3553 | 2026-09-23 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 90789e5c-fb2a-3f38-9eba-0d4013724ec8 | -15.6574 | -43.527 | 2026-09-23 01:00:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 5c867033-31f3-3d16-9020-d4d4d70aa634 | -8.4538 | -48.6944 | 2026-09-23 01:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 6612e09b-b0b9-3ef9-ab03-2a19a8436bc5 | -6.3293 | -43.9411 | 2026-09-23 01:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 94b1d3fd-6fbf-3fa0-a419-87a842255c39 | -6.3105 | -43.9426 | 2026-09-23 01:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 77fad404-5258-36f0-9377-903b4043b14a | -5.7754 | -45.1053 | 2026-09-23 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 7284bcfc-6de4-32f1-a1e3-e7ecbc03b7c4 | -8.791 | -60.8127 | 2026-09-23 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 20fad234-555d-325f-a67e-a35660046ae7 | -8.1876 | -54.7219 | 2026-09-23 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 13e51b11-57aa-3976-9259-697254c4fbc8 | -5.3453 | -45.1576 | 2026-09-23 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5f96ce08-a380-3808-aa46-9357da48e098 | -3.2313 | -46.9596 | 2026-09-23 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| ef2ecb1f-31cb-3642-a3a5-8ee616a93e16 | -8.7919 | -44.2546 | 2026-09-23 01:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 7789fbf8-9065-3f8e-a4fa-581ee6a1a2e7 | -12.402 | -46.9804 | 2026-09-23 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| bbfa88d3-e306-3689-8bf0-d1e8abee6f61 | -8.2062 | -54.7207 | 2026-09-23 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 37a42d24-3f10-3db2-b269-8263e8dc40ac | -9.1024 | -61.4491 | 2026-09-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8f8c7899-de57-3945-8c96-fca470164b33 | -3.2128 | -46.9602 | 2026-09-23 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| bb6a114a-b81f-3242-adbc-6b7be2b4b0bf | -8.8108 | -44.2525 | 2026-09-23 01:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 220.2 |
| b9e11e60-8de1-3e59-86e2-41338a21ebf0 | -12.4212 | -46.9777 | 2026-09-23 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 185.3 |
| cedcb0fa-5250-3487-8165-7de609b14140 | -7.8811 | -61.1779 | 2026-09-23 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 7040d660-2ace-3114-a8e3-bfd0f1fc6143 | -6.3293 | -43.9411 | 2026-09-23 01:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| dd042845-f084-3a9a-8cf2-41bea8619894 | -12.4024 | -46.9579 | 2026-09-23 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5d0a5514-d593-3a94-aacf-09a22b1ece32 | -6.6816 | -55.0502 | 2026-09-23 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| e7b21e23-dc71-348c-a03c-f705b538c59f | -9.1025 | -61.4299 | 2026-09-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 89a8c24e-15b7-3d8a-a78d-68cfcf59b5ec | -4.0925 | -62.0874 | 2026-09-23 01:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4a32cd1a-123b-34a7-a482-7fc0b3f0f72d | -6.1289 | -57.7613 | 2026-09-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| f9a3f9ce-f49f-3308-979e-b55a4e4c7e3c | -12.1385 | -45.6339 | 2026-09-23 01:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 1f2500a5-f01f-318a-82e8-d55d312cef5d | -12.1481 | -50.8026 | 2026-09-23 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2d37c41d-86cc-3d31-9241-c43e048e8287 | -5.7754 | -45.1053 | 2026-09-23 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| c695152f-1507-37a0-a8b7-b7f5aba059f6 | -8.7916 | -44.2778 | 2026-09-23 01:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0ad76f5d-01eb-3d5d-8ed0-da392cb65451 | -15.6376 | -43.5312 | 2026-09-23 01:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0f5159da-ec77-377f-936d-81f0cf1348cc | -8.4985 | -57.6075 | 2026-09-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 0de7aa78-a508-38f5-a2d0-15c1f7f46afc | -4.3357 | -55.6659 | 2026-09-23 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 24c88c40-2d22-3a34-9caa-de0ddd5b8b04 | -6.1109 | -57.684 | 2026-09-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9a507a97-d590-3591-95e8-267969492666 | -3.2129 | -46.9383 | 2026-09-23 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| c94d8aa9-1738-3a64-ae57-3bbb00d243b1 | -12.129 | -50.8049 | 2026-09-23 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| cb815e20-1d4c-30ed-ac5b-424c3eed9979 | -10.6094 | -53.9902 | 2026-09-23 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 44235f5a-e282-3fc7-8b12-376fcb3af0dc | -12.3679 | -50.1539 | 2026-09-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 925a1ae2-ae10-32d8-a911-fc30134557da | -3.6763 | -60.5839 | 2026-09-23 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 7bbe2202-b7b7-36de-81cb-68dd6232c7a4 | -3.6947 | -60.5455 | 2026-09-23 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 4cf8f165-7120-399b-833b-2731103881f5 | -8.1876 | -54.7219 | 2026-09-23 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 0949d873-c23a-3c3a-bea8-4f25c048437d | -5.7567 | -45.1067 | 2026-09-23 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| c8b7197f-d7b4-3b35-8f3f-025d338bb6d4 | -6.9214 | -46.5663 | 2026-09-23 01:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8f392476-4f82-3008-952d-3468c05de0ae | -6.6775 | -58.5748 | 2026-09-23 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 00f2348f-c942-3fe5-ab74-c4b493522deb | -12.1192 | -45.6368 | 2026-09-23 01:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 3542c312-9c29-399a-8045-58448a9b456d | -5.7565 | -45.1293 | 2026-09-23 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 046f73d8-6b06-3ff9-b8de-9296b5b9b1f5 | -3.2314 | -46.9376 | 2026-09-23 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 226.2 |
| b9b38812-2cf6-3282-862a-9ab927725c0f | -3.6946 | -60.5835 | 2026-09-23 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| e3d6a916-42ba-37a6-8379-0520b88f4719 | -12.3676 | -50.1755 | 2026-09-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 07a5f36a-cd1e-3bdc-8738-e362ce805335 | -15.6574 | -43.527 | 2026-09-23 01:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 46a2b955-55ce-3c27-9f8f-603de12732c5 | -8.4538 | -48.6944 | 2026-09-23 01:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 25edbcb3-00e6-331b-9466-0a50a4bdf16f | -15.6568 | -43.5512 | 2026-09-23 01:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 98f7f0bd-798e-3d14-96d4-084ac541bd1b | -8.4726 | -48.6927 | 2026-09-23 01:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 77.2 |


[Clique aqui para ver as próximas entradas](README32.md)
