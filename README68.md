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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90109c6c-a2ae-35b3-a7fb-09f66dce56ab | -13.38441 | -51.7532 | 2025-08-28 05:25:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36720d8d-ba15-32a4-8ab7-7b6f43698693 | -8.99624 | -65.41805 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0b67fe5-e023-389a-b0a5-477fc58b09c2 | -10.88593 | -55.7746 | 2025-08-28 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fe11ac7-e96e-3d10-93bc-adced7553fba | -7.471 | -59.90489 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc4d6093-9ed4-369a-a4e1-0ca0603a33ce | -10.6065 | -55.40234 | 2025-08-28 05:25:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae16a7c6-5598-35e4-a626-d58d4a2c673c | -11.57198 | -47.62477 | 2025-08-28 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c4214f2-7531-322f-891a-93eb4867617e | -8.91348 | -60.71692 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18671033-0996-31cf-8d29-97b9aef49144 | -8.26082 | -61.45782 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7bb2b13-3852-3187-b473-3015964b19fb | -8.92992 | -65.93941 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cfda27d-a693-3f53-925e-5fb30fef976c | -11.23088 | -55.05324 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb566175-07e1-3f8b-b2e4-be3e8da46ea0 | -9.31479 | -57.70345 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c642db92-2ae8-3a7a-8998-11cccc38e563 | -10.49657 | -51.58702 | 2025-08-28 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23ca71b5-189f-385f-99d3-4b4c02fdf649 | -9.2529 | -65.90443 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a96324d1-9c8e-3d6d-bffa-515902c9047b | -8.97806 | -63.10546 | 2025-08-28 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccfea176-f66a-32a1-ac0a-195dff4d75e5 | -9.5335 | -62.40274 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a20c46dd-f9ee-379a-b7c6-9215b5787f67 | -9.67852 | -47.06388 | 2025-08-28 05:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 70008b78-6dca-3ffd-8636-30ed56b29548 | -9.94482 | -67.81818 | 2025-08-28 05:25:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa895d7c-ba95-3a6e-908d-aff89db55f1a | -12.79704 | -48.14902 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ed18a76-5936-3f2b-920d-0bd17ef4932e | -9.12544 | -65.76729 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4b1f5f85-0aa1-3486-ae4f-55dfc32eb05a | -10.08172 | -62.89988 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc932751-5508-36e1-8391-34bfa635c38e | -8.95555 | -65.95825 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 158fcdca-09e9-39ea-8ef7-aff89fe79ac2 | -12.82281 | -48.14993 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a800cd4-c4b3-35a6-8a16-7967e7ad19a6 | -9.40544 | -60.57185 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee1ba4f5-00e9-39e2-add3-45d545500e8c | -9.39645 | -60.51992 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c95fab58-dd90-38db-9a9b-07e8b65b4f9a | -8.34242 | -62.9427 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7879040-5e91-36b0-be9b-94acc512c203 | -9.16325 | -59.56461 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca5c7ff3-3862-3631-bc1c-2e27260b3b0f | -10.79216 | -60.76558 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffb38d7e-e0d6-33dd-8810-d4b8cc24a5cb | -9.13358 | -65.28977 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0b249d6-6776-3687-9a52-22ad4823aad7 | -10.82276 | -60.7668 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7062ef01-050a-3b96-a1ca-3f22b2573c41 | -8.72263 | -63.75627 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04e89a17-91c6-3638-a1eb-3800df91186a | -6.92613 | -62.93126 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fafb999b-c689-3d9c-81df-5aadde52e89d | -9.407 | -60.51799 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 199afe86-dec9-34fe-a262-94a4b581e1d8 | -6.57788 | -59.88374 | 2025-08-28 05:25:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 009d947f-4e58-32f0-a08b-ee2e4b44b801 | -10.03145 | -59.35811 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d54c200-2ae7-3e45-918a-0e49cc649dde | -9.40877 | -60.57237 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a0fd4a98-5a68-345f-a58a-b87b3d070c3c | -10.93919 | -63.63231 | 2025-08-28 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a552229-cfee-342e-a5c6-96ceb6d33531 | -11.15222 | -54.30561 | 2025-08-28 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc8f06e4-8328-3dfa-b3a4-d1240e21f06b | -9.40198 | -60.50636 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ce15c86-e457-392c-8d8e-5b95f1f6fef7 | -6.94709 | -60.07769 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f623456-21a2-31f3-8000-6bbafe8619f5 | -6.24063 | -60.00614 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed1cb745-1556-350b-a1a6-ae62a47cec88 | -7.54456 | -63.83905 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adf35b89-b1fc-30eb-af5e-3eae7f0d0f8d | -8.92882 | -65.9221 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72368039-ed51-3379-8a92-c07adb56487a | -10.47452 | -57.95644 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d00cb646-ca3f-38ba-8394-d6486b41789a | -9.24386 | -59.78931 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a12d0c39-74b8-3e4c-996a-e8e765ae8b88 | -9.24442 | -59.78571 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5071efbb-ca7f-30c5-8c74-9e48fc95216f | -9.13336 | -65.7686 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e2c026e-c99e-3b71-b266-67cd71a59d19 | -9.31604 | -63.44004 | 2025-08-28 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b4674dc-86a6-3225-9f72-d2826697c1d3 | -13.00005 | -56.90733 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09a02a4c-ee9f-3bd2-910d-6a405f85f8ab | -9.16853 | -60.76823 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b35a0e7c-b574-3807-a48d-cdcbee05ae1e | -9.64229 | -59.62676 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0d58a26-fa58-3b07-96a5-a8323d483590 | -9.40253 | -60.50284 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81c61838-9190-31e6-9920-2c7d6686295a | -9.40477 | -60.51041 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 243c4c79-ec2f-3dfe-a5d3-8216968f79a4 | -12.78638 | -48.1815 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8254bebe-583d-3441-a8ef-f4d6ed038174 | -8.90012 | -62.472 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23569934-b6cd-3ff2-9af0-17be5c23f4f2 | -12.70179 | -48.16898 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 966e9c3f-3516-329a-bf83-c2066c90fd05 | -9.41203 | -60.52961 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fc5a8c7-1b95-3507-b780-d8799d03f33f | -6.9109 | -62.93672 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c59780d3-20ba-3eff-bdbf-765900edb351 | -11.35633 | -63.26715 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ba89bca-dcb3-3b1a-a338-b86e1a307de8 | -9.16435 | -59.51226 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b065e342-0215-3021-a982-57cd045be043 | -8.95714 | -65.97295 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e069503-08e8-3583-9fb5-102cfce515b8 | -9.41038 | -60.54017 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9ceffb8-76ee-32d0-b171-ce3b27aaff55 | -10.47947 | -57.94834 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2127d619-518e-3045-a980-a5b25c1abe57 | -9.38978 | -60.51886 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbe5c9d3-4954-388a-8a18-68fe46215a9c | -8.92471 | -62.42746 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02bd7aae-5091-3013-a337-1a2cd482bc1a | -13.59489 | -48.22175 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55b87b18-f8e1-3a73-a539-d544044cff67 | -8.88802 | -60.7487 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55e398e9-f650-3bd8-bea9-b7623c4a2f14 | -8.24613 | -61.46995 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6c6799e-7514-3eaa-91ab-0c51ce067a0c | -8.24947 | -61.47048 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3979d1c9-1fca-3b74-82fa-1521acc308a6 | -8.71908 | -63.75567 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60d3aacb-6e59-3190-85a6-8d2248ead7b6 | -9.40646 | -60.52151 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fd31fc2-40e7-31e4-b26d-ada3487911b8 | -9.25133 | -65.90234 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa6b65e8-eabd-377b-9a7d-ec2d65a869ad | -6.91027 | -62.94061 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c127b4a-1c71-3fcb-b69a-88d512982458 | -11.23917 | -55.0589 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbf8421f-7c6f-33a8-a2b4-a3e39d935f8b | -9.41156 | -60.57642 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0434b0ab-40ec-37b6-a1b5-5330359e500e | -12.81334 | -48.13105 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c6565243-6461-3196-b76d-771b468b081d | -9.64286 | -59.62305 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7eec59c0-b0af-3c0e-a9d7-8b4634b4a5d4 | -10.47149 | -57.95154 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c77c02aa-4dfa-36f9-bd7a-ed509ce9ccb6 | -10.80606 | -60.76416 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 018f3ac2-007e-3795-84be-efd7f2df35f0 | -10.48187 | -57.95747 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5ff6512-b3a1-3217-baf7-e7bc1a0cbed6 | -8.95616 | -65.95473 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1837fe9-c621-3121-98a8-7cd4e2bce5a0 | -12.81704 | -48.13622 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cfee111a-768a-3866-bfea-e15a1777b620 | -7.34526 | -59.65405 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee20f289-a3e9-3cf9-adf6-8c50cc273ec0 | -9.18133 | -59.49237 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39e16d21-7abf-389d-91b9-34cf6d1cea86 | -9.25531 | -65.903 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b316ceff-5dc3-30c0-b04b-7f7c60566555 | -7.54252 | -63.85162 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2492c8ec-bf5c-3faf-9e35-1cb8995fba46 | -9.1421 | -65.27396 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c831c83-d858-3671-9dd3-fb4e7d85f626 | -10.48556 | -57.95794 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d95dfebe-0282-3b3c-8b8e-82c6305e6325 | -9.41313 | -60.52257 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79076db5-ee3a-3993-9595-aafaf22aa220 | -13.62842 | -48.24557 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea7067f2-bd70-3997-a54e-9dd5b150915b | -10.80885 | -60.76823 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| f9c81d53-a59d-3ea8-b4ae-aed75a3fb79c | -9.11411 | -67.70553 | 2025-08-28 05:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f06f79a-35eb-3920-be08-6cfb94212156 | -8.89953 | -62.47564 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1a58fd6-d029-3ce9-a7ac-a12cf267812b | -8.94134 | -65.94497 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b57d98df-fe97-3995-a013-580cd1b758c2 | -11.15372 | -54.30727 | 2025-08-28 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7c06b01-a1e5-31a0-9d3a-c049024b309d | -9.16293 | -62.35779 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49b86c5b-40bb-370c-b2c2-6ca0cbca071d | -9.40426 | -60.53559 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8e3242e-66d1-37f9-b7b2-1d5c5bb3305c | -10.08674 | -62.88934 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a31d75dd-5e87-3fe7-9f0f-3413bd28071f | -13.10247 | -57.12086 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fc9837e-8c18-35b8-b148-145cc6cf0a9b | -13.59561 | -48.21464 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| deca0e26-1273-39f5-8e30-6d2794c38ae1 | -6.01027 | -57.85375 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README69.md)
