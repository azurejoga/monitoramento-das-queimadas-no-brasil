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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11eca329-3103-3fe9-bd37-d26e45c53aa8 | -12.33661 | -45.71196 | 2026-08-04 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e123e305-fcae-32f3-9ead-5a0d1ce62721 | -10.82331 | -48.4822 | 2026-08-04 04:19:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a9345df-1d11-39b0-a340-e0294308a8fe | -10.61466 | -49.9822 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3f02ab2-5a87-3452-b2b3-e6b031bf1ba9 | -8.92685 | -45.20754 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3dea39f-a029-3302-8c19-d960fdcdf593 | -6.57775 | -55.17208 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf6aae5e-9b35-3340-8d54-d7b1494be65c | -11.20332 | -54.84085 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92d48352-1c34-319b-a914-a9b3b50f7fc3 | -6.53026 | -55.1659 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd2963a5-ce6c-37b8-82e4-fcaa0fc9677f | -8.73105 | -44.1446 | 2026-08-04 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ada79af-061b-3d79-9e85-6bb0e0bf8257 | -6.53659 | -55.16694 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05af1d12-fc80-3527-b863-63daaa7384a9 | -8.93475 | -45.20142 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33c55fbb-0bad-3e80-8950-915326825add | -11.20935 | -54.8712 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8296455a-a427-333e-8c28-1da566018202 | -11.21015 | -54.86705 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21aeda78-b41a-3ad8-93c0-444f6412f6df | -10.56717 | -46.77749 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f99466af-4539-3b52-a930-32cbc96f157e | -11.21132 | -54.86583 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6bdd1f8b-e78a-3bd2-b99f-eac26f7be186 | -6.09983 | -55.80947 | 2026-08-04 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3c85c04-7d94-3312-b160-fbe8cd201cf4 | -12.8525 | -52.81987 | 2026-08-04 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56991a1a-14da-3d55-9c15-e75aac3e0991 | -10.56367 | -46.7769 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6d823e9-6656-3b89-8a39-f03149e24e38 | -11.18802 | -54.85854 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c403a620-8ab8-3cd6-bd75-37fe506dbda0 | -11.23649 | -54.85881 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f056b9e-c996-319d-ace6-ef0d420cde37 | -7.60975 | -46.46455 | 2026-08-04 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fa2afc19-f08c-3200-a9bb-95162e49ef35 | -8.34361 | -45.98508 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b88e495e-03c8-3e59-a816-60fca3e1698e | -11.46122 | -45.11371 | 2026-08-04 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00f7c254-7d59-322a-a468-607432f22a2f | -6.55693 | -55.17886 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 111cac2c-6f8d-3071-8fea-df87c6ef43f7 | -11.21503 | -54.87254 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6affb4c-6a11-392d-922d-2c6ad00ffde1 | -7.1112 | -46.71893 | 2026-08-04 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4bb20ea-596a-3105-b7b5-00dd52d584a3 | -8.93811 | -45.20197 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20e271d7-51a4-3fd2-8703-aa167469cae5 | -8.34077 | -45.98067 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 2e72205c-8d6c-376b-9c34-20520fdcc393 | -6.55828 | -55.15497 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41a4fa84-e369-3f2a-ab35-9a7bf8824fd2 | -6.54387 | -55.1627 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 32df8e7e-c6a7-3427-b8bd-fe052a74e70a | -6.95689 | -52.82024 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 107188e0-4676-3ecb-b893-060d2825367e | -7.60619 | -46.46395 | 2026-08-04 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 49617193-4757-30de-b932-afccfd7ed5bb | -11.20045 | -54.88654 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 033c99eb-887f-3496-8e87-01813362ef4c | -7.51846 | -47.00038 | 2026-08-04 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6601a2a9-d84d-3884-9a2b-3d7e9a1f9e53 | -6.55347 | -55.16242 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c758fd3d-6a92-31c1-9866-6dd409d8c311 | -7.93519 | -44.91188 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f953e1f-6f3c-352f-8a6a-5239653b72a8 | -6.95623 | -52.82386 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f9a0d8-a627-3060-af1f-f4c3eb88e2c7 | -11.24615 | -54.83999 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d69e869e-3e50-36cb-b1d0-12d2ecdb4842 | -10.56017 | -46.77631 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f53214b0-8eb9-363f-acd4-307e2265a2c4 | -7.60553 | -46.46802 | 2026-08-04 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 994ab8a4-8e8b-3d23-be97-43533c38b095 | -11.12805 | -50.39372 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2863c4f-6561-382a-a9a9-41a429693d93 | -6.53118 | -55.16082 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b55ea18-ba32-38f4-857c-bb39a2941f99 | -7.91493 | -44.9307 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1eb7964-d16b-3d9d-a294-4f99967fbbca | -6.56183 | -55.17152 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f70e3d7-c8dc-3883-ac2c-7cba774522ef | -9.61399 | -47.76189 | 2026-08-04 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa4d59b8-db6f-36f0-96c5-1a614b7becd4 | -8.35832 | -48.24879 | 2026-08-04 04:19:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad9028ee-8015-3038-b20c-38c275e6d7eb | -6.53844 | -55.15664 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c48bb71-9076-32f9-87fc-5c4530dfb217 | -12.7451 | -44.45438 | 2026-08-04 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b848629-eb38-32c5-8e7c-f9f2e090c836 | -7.56857 | -46.00559 | 2026-08-04 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cd76ca6-b8a0-38dd-9306-21c00fbf45c2 | -10.56782 | -46.77356 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d06c86b-d4e3-375f-b03d-41e1f8526a52 | -6.5492 | -55.16927 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0038ef3c-fa96-3fe6-901d-074a3eb0d5b5 | -7.24331 | -43.32663 | 2026-08-04 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02731a38-54a4-3cc9-8f4a-e40f11fbf02d | -11.1152 | -49.90362 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ff85421-eaa3-3715-9383-9c029db019cd | -8.92875 | -46.99538 | 2026-08-04 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c016d98c-1d29-3b84-84ea-ee949efa14cc | -11.20443 | -54.86586 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cac8787-e442-3f6f-aae6-11b37f735205 | -11.20905 | -54.84193 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4e83e30-8752-3289-a428-21c4ff3726f9 | -6.57333 | -55.16079 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d50fab3-444b-3f83-bce1-720366362f1a | -8.3477 | -45.9818 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 808f006f-ef66-303e-92d3-525e8fff4751 | -12.03775 | -47.65436 | 2026-08-04 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7777c591-796e-3816-8e9b-5e6f8796029f | -6.54087 | -55.16008 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 079458a1-4f36-3118-8d08-762affbc50d7 | -12.10966 | -45.68515 | 2026-08-04 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e53a41d6-b32d-3265-842e-fdd436b99d4f | -11.71978 | -48.39733 | 2026-08-04 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d90c4fc9-9e0c-3ba9-b789-28dd3604a963 | -8.93416 | -45.20502 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe2db147-5eb7-33a4-a9fd-1f2f0017e8bc | -7.1119 | -46.71465 | 2026-08-04 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 259bad09-7f24-3bda-aa06-828887fc084c | -8.35462 | -45.98294 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 65f534ed-cca9-3ef3-8d71-c39d03d0e5c5 | -6.54198 | -55.1732 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6e88d8a-6076-36ce-80cf-57b1478c7399 | -6.56704 | -55.15953 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b92e5c2-6f15-3e02-b915-c6f01fe05ce1 | -6.55738 | -55.16 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1127be63-39ac-3e78-9251-f0af17f7d9b6 | -6.53452 | -55.15917 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f020296b-7680-356e-aca1-a56fbda2d307 | -11.22152 | -54.86972 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3379b736-77c9-33fb-9da4-dcec0d1d68d6 | -8.35689 | -45.98291 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f83d9c62-c622-3cb1-a259-67cf3ee45728 | -6.56277 | -55.16624 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f800a059-f88c-3652-8235-e0cbaa46e2f2 | -10.64501 | -46.76985 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fcb789ac-8f10-3cd9-848e-695c84ad91a3 | -7.11482 | -46.71954 | 2026-08-04 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04668fb5-e878-365d-ac48-86ca50583fab | -6.56092 | -55.17659 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f069f955-28aa-3e2b-aa58-18d778010277 | -11.21094 | -54.86291 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5205d3b5-56a1-3d92-b52e-5733a38247ef | -6.55062 | -55.17768 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2565e685-aa06-3cf2-8f97-319dacb37848 | -9.93308 | -53.32771 | 2026-08-04 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb477c54-4285-39db-b3e7-c867159b03d3 | -7.49616 | -45.84721 | 2026-08-04 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6691836c-55ac-355a-8aa5-6c7d17dab435 | -6.56512 | -55.16986 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e586acc7-c9f5-33b8-88ab-bd95529b4122 | -11.53145 | -46.88976 | 2026-08-04 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 523fbe19-e24d-37d8-aeae-42154b80cf1a | -11.7559 | -50.28556 | 2026-08-04 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87573a45-e242-3896-8061-e9f7d6b9edb3 | -11.217 | -54.86712 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e1e73fa-b6cd-3553-800d-e0842bc635aa | -11.83172 | -38.2627 | 2026-08-04 04:19:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bc27f819-a6fc-3a2a-8619-91ed5390e12e | -6.5661 | -55.16464 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4273df88-727a-36af-bd50-0fe99777cf2b | -7.625 | -45.31219 | 2026-08-04 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb02fca1-af52-359c-acba-dd265dae4589 | -7.95678 | -46.88765 | 2026-08-04 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fee87743-6c2c-3acf-89d3-7e4b6a374b77 | -7.3216 | -45.2565 | 2026-08-04 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57e301c5-ab7c-39ac-89f4-405a98c88e07 | -8.5591 | -47.75073 | 2026-08-04 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25297b25-af9a-3d2a-ae98-eaecd18fe909 | -11.21452 | -49.9572 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b79c762c-df80-3949-9bf2-de33634f1122 | -12.85145 | -52.8254 | 2026-08-04 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1d572da-0a0c-34f2-85bc-8dc38f3c78f4 | -7.91609 | -44.9235 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d272cf36-1e92-37fd-88e3-818796c678c1 | -8.27518 | -47.54429 | 2026-08-04 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86ebe689-5813-3bad-b4b4-3d299f0e829e | -11.11933 | -49.90438 | 2026-08-04 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81646592-57a1-3192-ac78-50c24ed0b455 | -7.62439 | -45.31589 | 2026-08-04 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1e99a88-3886-3934-bd35-e8937675b135 | -8.9308 | -45.20448 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd59c068-6843-352b-8a30-bfe64d6cdf3f | -12.14944 | -48.45198 | 2026-08-04 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ac4268a-7352-31d0-ab68-941c8cf2cc1a | -11.83229 | -38.25839 | 2026-08-04 04:19:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c172b861-4327-345f-a6b3-a5acb795ca49 | -11.21248 | -54.85492 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c5aadae-e5b8-3d49-82ab-3ddeabd9059f | -9.97601 | -47.98132 | 2026-08-04 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be4443f4-dc5b-3ca2-84c3-798296ba2f1f | -11.2018 | -54.84875 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README9.md)
