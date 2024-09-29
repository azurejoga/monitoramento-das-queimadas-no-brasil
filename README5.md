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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fcc52b8-f5dc-38bf-90c9-45d944f5b980 | -10.7171 | -48.738098 | 2024-09-29 00:47:28 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c2c8f80-73d9-3c91-a7ac-88440aa81d38 | -10.5507 | -48.0425 | 2024-09-29 00:47:28 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d04c815-0819-362d-b9af-358edeb7f3ba | -10.5523 | -48.0495 | 2024-09-29 00:47:28 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5a4e927-6f6d-3687-8b49-9fb8c5e840fa | -10.5393 | -48.037701 | 2024-09-29 00:47:28 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc1731ae-8f9d-39f7-9656-83fc14aed826 | -10.528 | -48.033001 | 2024-09-29 00:47:28 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf8eae25-d87a-35ef-a204-8282a2496281 | -10.5295 | -48.039902 | 2024-09-29 00:47:28 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6bc36f-1d20-3c27-a203-786f82122986 | -10.9346 | -50.095699 | 2024-09-29 00:47:29 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2645b5e6-114a-36c9-abcd-91ca83c4d5ce | -10.9363 | -50.1036 | 2024-09-29 00:47:29 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a1bad80-0033-3fbf-afdc-0088c1a5de5f | -10.938 | -50.1115 | 2024-09-29 00:47:29 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64d3c1e5-51ed-3431-bf2d-732eef9f6ff9 | -9.4789 | -44.055199 | 2024-09-29 00:47:30 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91b17419-7d94-3291-9b3f-9081cc6d1870 | -9.481 | -44.064098 | 2024-09-29 00:47:30 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 29b67460-0999-3862-851d-cf92025e633e | -9.4831 | -44.073002 | 2024-09-29 00:47:30 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15a4ae16-f489-301a-9bab-002a708f7d7d | -10.4305 | -48.194401 | 2024-09-29 00:47:30 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da42f292-1270-39ed-87a9-46659d0f2b27 | -10.432 | -48.201401 | 2024-09-29 00:47:30 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca077e7-2e0a-3a23-afea-3e4b8a04a598 | -9.2785 | -43.478901 | 2024-09-29 00:47:31 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1fe61375-df50-3b76-8d8e-14a497c23b63 | -9.2808 | -43.488499 | 2024-09-29 00:47:31 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 45181109-ebb0-3e7f-b819-f10af9155295 | -9.2832 | -43.4981 | 2024-09-29 00:47:31 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3cd15a10-6817-39a2-8170-bdd9e8815ca0 | -10.5346 | -49.444199 | 2024-09-29 00:47:33 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ac3c098-ee08-3e40-b9a6-82d0d7a90cba | -10.5362 | -49.451599 | 2024-09-29 00:47:33 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27e32c9b-0ccb-37cb-92af-8d8d2bb24cdf | -10.5264 | -49.4538 | 2024-09-29 00:47:33 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79ce4e1c-29d9-368f-bb0b-9c51df687d98 | -10.6266 | -49.908901 | 2024-09-29 00:47:33 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d38c0cd-9374-33dc-a921-f3defaa2e01f | -10.1677 | -48.034302 | 2024-09-29 00:47:34 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2625ea25-2f09-308a-a890-ed6fe0fa19d3 | -10.1692 | -48.041199 | 2024-09-29 00:47:34 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04c68791-f49e-306e-858e-7bbe0b06e6cb | -11.0736 | -52.4627 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adc08a46-ed6f-3e99-b70e-14f54276506e | -11.0758 | -52.473301 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 385e4658-7d7a-352a-9182-d29d24220de2 | -11.0781 | -52.483898 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17c1e7d9-5913-3305-aeee-0849abb38fe4 | -11.0803 | -52.494598 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfabe79d-89e6-339a-8900-35be9fd38741 | -11.0638 | -52.464802 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b91a248-2538-3df1-bf4c-b653cb9647a2 | -11.066 | -52.475399 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88d9a03b-ba1d-3b16-8b64-704f761b507d | -11.0683 | -52.486 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0bbfd1-5baf-3add-949a-58d1d2f696a3 | -11.0705 | -52.4967 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e270d540-747a-3a57-bc69-ea2e40550422 | -11.054 | -52.4669 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a806b2f9-54a7-3b5e-9ede-135f6f33ff47 | -11.0562 | -52.477501 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8745e41d-fb8f-37cc-acb6-b9abdcbe6c2b | -11.0585 | -52.488098 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2430ad56-4e67-3741-9456-1debe383c6a2 | -11.0607 | -52.498798 | 2024-09-29 00:47:35 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be2d5bee-5068-3de1-a83e-ad65a94b2821 | -9.8907 | -47.4049 | 2024-09-29 00:47:36 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7a1343b-2a72-3674-8d02-532060cef32e | -9.8923 | -47.4119 | 2024-09-29 00:47:36 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9f4d51-2d0e-349f-8f1b-2792266846d1 | -9.8809 | -47.4072 | 2024-09-29 00:47:36 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebe9d2bf-5f90-379f-9c18-c8ae68e15307 | -9.8825 | -47.414101 | 2024-09-29 00:47:36 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1b2564a-821a-3f2c-b8f8-345c2b5ba48d | -9.5603 | -46.5065 | 2024-09-29 00:47:38 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea503a9-3a13-3a64-a76a-9df20723a960 | -9.5619 | -46.513599 | 2024-09-29 00:47:38 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28f0fa1c-4d53-3fe7-aae2-08ab8425456d | -9.5636 | -46.520802 | 2024-09-29 00:47:38 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97b11667-d172-32a8-b779-9a6387b78e54 | -9.5505 | -46.508801 | 2024-09-29 00:47:38 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e62a427-fe29-3983-a931-3dae82e6ea12 | -9.5521 | -46.5159 | 2024-09-29 00:47:38 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d1d7257-dc66-3c83-9b37-764af30130dd | -9.5538 | -46.523102 | 2024-09-29 00:47:38 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8428551-62b1-3b9e-ab03-a0adee8d799f | -8.4345 | -41.9203 | 2024-09-29 00:47:39 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5bb03881-d324-3934-bc3f-f87beb53fa70 | -10.4929 | -51.132 | 2024-09-29 00:47:40 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8be14dd-2fd4-3cf7-ad5d-d4e54c1225c2 | -10.4948 | -51.140701 | 2024-09-29 00:47:40 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57e1ce50-2482-3cd0-a752-31c0ec6ff365 | -10.4832 | -51.134102 | 2024-09-29 00:47:40 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1547e675-6e1b-3045-ad53-688c154cc194 | -10.4851 | -51.142799 | 2024-09-29 00:47:40 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46c9f7d7-fcdf-3f5b-a1df-075130ab9445 | -11.72 | -57.420502 | 2024-09-29 00:47:41 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb4f5bb4-2abb-3231-9d44-538a61cb2a6f | -11.7103 | -57.422401 | 2024-09-29 00:47:41 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 109bebfb-ed1e-35fc-861b-717fb633becb | -8.3428 | -42.2616 | 2024-09-29 00:47:42 | METOP-C | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 467c4a75-94ab-3c5e-87a2-c0a1b5480eb8 | -8.3457 | -42.2733 | 2024-09-29 00:47:42 | METOP-C | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 581acf6c-182f-33fc-b8f8-77bf109799a7 | -10.1121 | -49.998001 | 2024-09-29 00:47:42 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cffb018d-433b-3666-9f80-eb7ef750ca99 | -10.1023 | -50.000198 | 2024-09-29 00:47:42 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6a9ec65-8cbd-34f5-a2b1-fb359e21bbe6 | -10.104 | -50.0079 | 2024-09-29 00:47:42 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5c34b7d-e6de-3573-b1b9-bace12a4b710 | -10.0925 | -50.0023 | 2024-09-29 00:47:42 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56512084-6959-3349-8fe3-d093f5ef25b3 | -10.0942 | -50.009998 | 2024-09-29 00:47:42 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14962140-7dd3-356e-9cff-7eae609ac4aa | -9.5325 | -47.778 | 2024-09-29 00:47:43 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce74053c-ea8b-388e-a5e0-0de0496b3e8a | -9.5341 | -47.784901 | 2024-09-29 00:47:43 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4dec5c7b-d7e5-3921-b6d9-5987ef11b592 | -10.0564 | -50.305 | 2024-09-29 00:47:44 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49bd6627-8c20-32e7-bfa1-73b5a1a68d5f | -8.9051 | -45.6436 | 2024-09-29 00:47:46 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 871b13de-5a7d-36bc-af0d-61ec03af51a7 | -8.9069 | -45.651199 | 2024-09-29 00:47:46 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48298c71-11a5-35db-b1cc-bfe81a7eb609 | -8.9087 | -45.658798 | 2024-09-29 00:47:46 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dfb671f4-d602-322f-9e02-128f29824928 | -8.9104 | -45.6665 | 2024-09-29 00:47:46 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4d7beb9a-36b3-308a-9e99-e39422c5dc42 | -8.7601 | -45.158901 | 2024-09-29 00:47:46 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0ef4d4c-4730-38d7-a8a0-5022d3087025 | -8.762 | -45.166901 | 2024-09-29 00:47:46 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a9d707cb-c71d-3920-91b5-2f6887cee755 | -8.7639 | -45.1749 | 2024-09-29 00:47:46 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d382ae42-19c0-3f51-a207-887e67443f7c | -8.5067 | -44.6987 | 2024-09-29 00:47:48 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71aad3ea-6f57-3028-8345-d7eda3bf2c41 | -8.5087 | -44.7071 | 2024-09-29 00:47:48 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e603eadf-fcae-3702-b9d9-9a9e2160a7fb | -9.7338 | -50.425499 | 2024-09-29 00:47:50 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f55f1127-d6cb-30f3-b5a4-12600d290694 | -8.5494 | -45.491402 | 2024-09-29 00:47:51 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 475e2ac1-a678-3725-8565-66e99c45e1ee | -8.5512 | -45.4991 | 2024-09-29 00:47:51 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 73bee68a-aca7-3d37-a169-3be16eb88144 | -10.3796 | -53.7752 | 2024-09-29 00:47:51 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b27d8b45-20d3-3ff6-a3ec-6477a5320df3 | -10.3822 | -53.7878 | 2024-09-29 00:47:51 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1cd9c41-ee89-3ea9-a4f8-e6e52da7da91 | -10.3672 | -53.764599 | 2024-09-29 00:47:51 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8260c507-dbb9-342a-861b-2b0dd29f009b | -10.3698 | -53.777199 | 2024-09-29 00:47:51 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0646909f-d4a0-3b9d-ad57-4e287d4fe01b | -10.3725 | -53.789799 | 2024-09-29 00:47:51 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8de3b61-9da6-37e3-96ef-823fb0f65e81 | -8.8032 | -46.756599 | 2024-09-29 00:47:51 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20947c1b-f577-35f2-bae1-ebc8704d29fa | -8.8048 | -46.763599 | 2024-09-29 00:47:51 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09a2215d-17c8-307a-a6ec-018c9b230323 | -9.5788 | -50.1884 | 2024-09-29 00:47:51 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee96eea1-12d2-36c9-96f2-3e5f268e8442 | -9.5805 | -50.196098 | 2024-09-29 00:47:51 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34248863-d53d-3d47-8b0c-211e861e69bf | -8.7917 | -46.751801 | 2024-09-29 00:47:52 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26412f6b-c052-3cc9-a09b-1257172c1b4f | -8.795 | -46.7659 | 2024-09-29 00:47:52 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09fdd383-2319-3298-9074-827e7a702df3 | -9.5674 | -50.182701 | 2024-09-29 00:47:52 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f20de57-a9fe-3c04-9b37-7cbea82d524a | -9.5691 | -50.190498 | 2024-09-29 00:47:52 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 738b7817-0b48-33a7-9947-acd8a5cc5888 | -9.5708 | -50.1982 | 2024-09-29 00:47:52 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f755206-bafe-339f-86a5-c2203b504a4a | -9.5725 | -50.205898 | 2024-09-29 00:47:52 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beb42695-0d2d-32a2-b7fc-40a99735da12 | -9.5576 | -50.184898 | 2024-09-29 00:47:52 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ddddbd-b48c-317b-aaf0-b399a6246cac | -9.5593 | -50.192699 | 2024-09-29 00:47:52 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2f9b75-aa32-3497-91bd-a945f42e0807 | -9.561 | -50.200401 | 2024-09-29 00:47:52 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf0a53e-5316-3b9a-b97c-150dd5098f49 | -9.5414 | -50.2047 | 2024-09-29 00:47:52 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a40d1a5d-83a6-380f-b08f-3fdd8355085d | -8.3057 | -45.333099 | 2024-09-29 00:47:54 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ca1c896c-28cf-309f-9677-02512be5e9c6 | -9.409 | -50.024601 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd91c7b6-34a6-3f4b-b8e1-ddd9e0080a00 | -9.4107 | -50.0322 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3b3219b-045f-3a66-82fc-7b5828d096be | -9.3942 | -50.003899 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0335276-082c-3a50-b3d9-bda49c9751e7 | -9.3959 | -50.011501 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97ff988a-673b-3350-8337-91179f582798 | -9.3827 | -49.998501 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07b94c62-4816-3336-ba01-b94cd572693b | -9.3844 | -50.0061 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
