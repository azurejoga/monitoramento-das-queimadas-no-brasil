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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7ca2055-7292-3800-961e-f65e541782e0 | -10.2376 | -50.5204 | 2026-09-23 08:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7397c828-cf55-3132-9e42-86ffea79752c | -12.0152 | -50.7755 | 2026-09-23 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 879bbb1c-9381-3032-92e6-daf8cf72d8ef | -6.6145 | -59.9464 | 2026-09-23 08:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 4f44606e-c31e-3601-892f-0f6813edfd4e | -6.633 | -59.9457 | 2026-09-23 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 4ab881f3-a4f3-3e9f-9ba8-904dffe9bf6a | -6.6146 | -59.9272 | 2026-09-23 08:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 236ec75f-d3b2-3029-84e3-49965f49312a | -12.0155 | -50.7541 | 2026-09-23 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1cd4c082-3752-39fd-be68-5c821d901749 | -10.23 | -50.2 | 2026-09-23 08:00:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8c313e1-c597-381f-bb8a-ffebae4bf275 | -10.23 | -50.25 | 2026-09-23 08:00:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8ce099d-a0e1-3193-bcb4-0f0dc6df9742 | -10.26 | -50.26 | 2026-09-23 08:00:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c17c713b-de83-35fa-8913-78757bf43724 | -10.2 | -50.24 | 2026-09-23 08:00:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01f95781-92a5-328b-9739-4b5c5e5935d1 | -6.633 | -59.9457 | 2026-09-23 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| eba96b14-eaeb-3ae3-98d2-f0832cc26303 | -10.0339 | -50.2211 | 2026-09-23 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 7ca314cf-f8f1-3b41-ab2c-7686618ffac6 | -10.0151 | -50.2229 | 2026-09-23 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e7d56fbc-c3d4-347b-95eb-efd59c537139 | -12.0152 | -50.7755 | 2026-09-23 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 324.7 |
| 580b0829-ca68-3f80-a9b2-d660bdaba909 | -12.0346 | -50.7518 | 2026-09-23 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 87b6a272-16f6-378e-8ec0-d7663146ba4b | -6.6145 | -59.9464 | 2026-09-23 08:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bdaf99ca-2c1b-3825-996f-2b208267d37e | -10.2376 | -50.5204 | 2026-09-23 08:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| dda763d8-7f12-3bfc-9740-7779e6fa917e | -10.2565 | -50.5185 | 2026-09-23 08:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| b2d01437-d2da-3964-a3ab-9489293f6008 | -10.0153 | -50.2016 | 2026-09-23 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 79119c18-303d-3a04-bc39-db2cb5c7c513 | -11.9964 | -50.7563 | 2026-09-23 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 24ccb686-d259-3c5d-bcd4-052d4f7531f8 | -6.6331 | -59.9265 | 2026-09-23 08:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| de1eec53-d1ce-3e01-9916-650d985df927 | -12.0343 | -50.7732 | 2026-09-23 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| b57923dc-0e8c-3998-93db-feb1e9a0cdcb | -10.2562 | -50.5398 | 2026-09-23 08:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6077a11c-8e4f-3c27-b8cf-77809903e35e | -6.6146 | -59.9272 | 2026-09-23 08:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 12c0f4c2-a13d-35c1-b3c1-552845726b37 | -11.6913 | -50.8126 | 2026-09-23 08:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 4f7aadb9-9467-3db1-89e1-ba907601bed1 | -12.0155 | -50.7541 | 2026-09-23 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 277.1 |
| ad534045-167a-323c-8010-b6f0c3725021 | -11.9961 | -50.7777 | 2026-09-23 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 5631f814-c97d-3d4f-b207-677c449f145e | -10.23 | -50.2 | 2026-09-23 08:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9484657-9c8a-385f-ac74-29626fa18994 | -10.23 | -50.25 | 2026-09-23 08:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60ad5cf7-30ba-3049-80ad-02db7a6b1b39 | -10.26 | -50.26 | 2026-09-23 08:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90c16f25-d1c4-3e9f-a7e9-760cc6262dd3 | -10.2 | -50.24 | 2026-09-23 08:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8812f20-c997-361e-bf7f-492ab3b24eaf | -6.61224 | -59.91708 | 2026-09-23 08:18:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 52b2bab5-416c-39d8-8fa4-fe88f6e555ac | -3.68667 | -60.55979 | 2026-09-23 08:18:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 28593bd9-80f4-3d8a-b002-065449b10781 | -3.68221 | -60.59127 | 2026-09-23 08:18:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 231c06b6-7a78-3c4f-93de-1b898c591051 | -6.61545 | -59.92213 | 2026-09-23 08:18:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 687d64e7-9028-3d4b-bd8a-de5cc54e434a | -6.62945 | -59.9192 | 2026-09-23 08:18:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 50a38994-1ab1-3445-91ca-a694cfa47423 | -6.63264 | -59.92434 | 2026-09-23 08:18:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e2e78d0c-e622-3414-9749-6da10e233b3f | -6.6146 | -59.9272 | 2026-09-23 08:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 9836ceb4-606f-3e72-ac49-b3a19931dcc2 | -12.0339 | -50.7946 | 2026-09-23 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 8039f0e6-2c7f-38b7-a776-e278f55b4dfd | -6.6331 | -59.9265 | 2026-09-23 08:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| fb310e3b-b317-3346-9134-1e16040dbf6b | -10.2376 | -50.5204 | 2026-09-23 08:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| bd766693-2ec2-3787-9f45-7dd98b03a3a6 | -6.633 | -59.9457 | 2026-09-23 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 28be1473-fae8-3d9b-bf8e-a04e24258c3a | -12.0152 | -50.7755 | 2026-09-23 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c854286c-c839-342e-847f-643bdbb4c8fa | -10.0151 | -50.2229 | 2026-09-23 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| dc552c7c-1ab4-370d-8981-cdd4acfca82e | -11.6913 | -50.8126 | 2026-09-23 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a52bfd97-5ad4-3dc6-8fde-683ff5e2dc06 | -10.2565 | -50.5185 | 2026-09-23 08:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 26ea131d-c869-3ad0-acad-dcb7c33f2440 | -10.2562 | -50.5398 | 2026-09-23 08:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0c3ec44a-1446-34db-9378-18c9421d179c | -11.9961 | -50.7777 | 2026-09-23 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 865e8e90-96d0-366d-902c-682f58893fa7 | -8.6117 | -66.72438 | 2026-09-23 08:20:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f3e7813f-01af-34d3-b569-c0aebef3b3fc | -11.6913 | -50.8126 | 2026-09-23 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3b8e8685-ff07-3ed1-822d-abd82371b224 | -10.2226 | -50.2235 | 2026-09-23 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| da328c2b-e3b8-33eb-a017-942949f90436 | -9.9962 | -50.2248 | 2026-09-23 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fea9f5cb-c4bb-3e49-8f39-b6619995ecb2 | -6.633 | -59.9457 | 2026-09-23 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9b34edee-056c-3070-941c-3d4463dda5e4 | -10.2565 | -50.5185 | 2026-09-23 08:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 39aecaba-cbc2-3bdf-99de-30eeb4cdea4d | -10.0153 | -50.2016 | 2026-09-23 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 4d9890c6-ee8b-3c85-b2d4-f0c943e911b5 | -6.6331 | -59.9265 | 2026-09-23 08:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| abf3a336-767c-3506-b527-2a4f5bc2011b | -10.0151 | -50.2229 | 2026-09-23 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| aa22beaa-4880-3250-ac78-add0274ee6ae | -10.2223 | -50.2448 | 2026-09-23 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| bca776bc-66ee-38ff-83ea-6e74aba1f06b | -6.6146 | -59.9272 | 2026-09-23 08:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ef86f0aa-15e5-36ad-bd44-cf25cc9a2f5c | -10.2034 | -50.2468 | 2026-09-23 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 558328ca-0e49-3dc8-be27-d4a0a3fcb434 | -10.23 | -50.25 | 2026-09-23 08:30:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10970211-b13d-3439-b652-14986deaa474 | -10.2 | -50.24 | 2026-09-23 08:30:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 095bfa0d-f06b-3c95-ac12-4a1a8a467da7 | -6.6146 | -59.9272 | 2026-09-23 08:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 4ec92311-f8dd-34db-91f4-20b551a5774a | -6.633 | -59.9457 | 2026-09-23 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 9c7642ab-832d-3be0-85db-c3b7e58b4ca7 | -6.6331 | -59.9265 | 2026-09-23 08:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 1ef6fbd9-1436-313d-9bbb-f302c2b1759f | -10.2 | -50.24 | 2026-09-23 08:45:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d149076c-5ae5-3954-8378-e98ad19f418b | -6.6148 | -59.908 | 2026-09-23 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 31b488b9-d631-306a-978c-99602b22f228 | -6.6145 | -59.9464 | 2026-09-23 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| dc85cec3-881b-3c92-9094-b63cea78139f | -6.633 | -59.9457 | 2026-09-23 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9184d6af-2f43-303e-be2c-3c85f4b440a6 | -6.6331 | -59.9265 | 2026-09-23 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 12a10c4a-ec1b-3e90-a870-dd4181524c88 | -6.6146 | -59.9272 | 2026-09-23 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e5bb767d-8d32-39b3-952e-08ad3d47eaa7 | -6.633 | -59.9457 | 2026-09-23 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6bc048b5-f4cd-3cdc-a6b5-c2b259590955 | -6.6146 | -59.9272 | 2026-09-23 09:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d0e26894-aff9-30e1-adcd-7c4ea4ee647d | -9.5735 | -46.5337 | 2026-09-23 09:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 411971fd-be33-316a-a94b-b77b5faeabe3 | -6.6331 | -59.9265 | 2026-09-23 09:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| ce0cea64-2f9f-38ff-9120-7882d15e9a0e | -6.6331 | -59.9265 | 2026-09-23 09:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 95c12ca5-fd11-32bb-a03c-212c6e091569 | -9.5735 | -46.5337 | 2026-09-23 09:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 87ef351b-2859-3450-a416-6d8171e698f5 | -6.6146 | -59.9272 | 2026-09-23 09:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 5aa57210-d9c8-3a7a-a2e4-5b6e014e0720 | -9.5735 | -46.5337 | 2026-09-23 09:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 92a03944-ab5c-3d16-9ec1-a89ccf652a82 | -9.5735 | -46.5337 | 2026-09-23 09:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 29df76aa-67a0-3b6c-b03f-a1739624dd3c | -9.5735 | -46.5337 | 2026-09-23 09:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 4ccffedb-452e-37a7-9cbd-20a81c49241d | -12.0 | -50.74 | 2026-09-23 09:45:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6924b69-1657-3b13-a0fa-45cdd4bbefc6 | -12.0 | -50.8 | 2026-09-23 09:45:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fcd886bc-0c3b-3e9c-9a71-f72e2db37d2e | -12.04 | -50.81 | 2026-09-23 09:45:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7260c6a8-7dea-3ef8-8b96-3c5b95595173 | -12.03 | -50.75 | 2026-09-23 09:45:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bcd0e65-f372-3a50-8015-48736cd8a3bc | -8.378 | -45.6036 | 2026-09-23 10:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 133b1e8f-d0e6-3bd0-9a0a-07c37fdbdb8f | -8.378 | -45.6036 | 2026-09-23 10:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 3be1f053-9fb3-3bb9-878e-5967a05bf5f1 | -8.3783 | -45.581 | 2026-09-23 10:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 143.3 |
| e540a6ea-8c68-32de-b871-df7097308e1a | -8.3594 | -45.5829 | 2026-09-23 10:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 3550dd31-5773-3a73-bf8a-0fa3d98d0b50 | -8.378 | -45.6036 | 2026-09-23 10:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 246.3 |
| 95e5be71-746c-32ad-b56f-bf24a69cea53 | -8.3591 | -45.6056 | 2026-09-23 10:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 168.6 |
| eee1edd0-0c78-30f6-aa29-dc267e78396e | -13.98018 | -41.39576 | 2026-09-23 10:47:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| fb8350e3-af75-306d-b844-93ccb0c94b54 | -8.0295 | -38.41567 | 2026-09-23 10:47:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 5902f8e8-fba5-39ff-99ff-306ebd1c4895 | -13.98761 | -41.40434 | 2026-09-23 10:47:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 9da52afd-4cb5-39de-bc6c-49069215ac2a | -14.82046 | -41.17632 | 2026-09-23 10:47:00 | TERRA_M-M | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| eb705c2c-2d71-3507-bda2-3f1c8c1d3561 | -8.3783 | -45.581 | 2026-09-23 10:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| c0b60f01-decb-3161-b2a0-30ae63033a3e | -8.3591 | -45.6056 | 2026-09-23 10:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 4c303c86-5004-3565-98c9-4446fb5bf585 | -11.2847 | -51.3878 | 2026-09-23 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 058f21d7-472c-3ca5-8fe8-35967958f92a | -8.378 | -45.6036 | 2026-09-23 10:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 254.9 |
| 2cb74820-d376-3d03-a793-997e1a105162 | -8.3591 | -45.6056 | 2026-09-23 11:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 231.7 |


[Clique aqui para ver as próximas entradas](README130.md)
