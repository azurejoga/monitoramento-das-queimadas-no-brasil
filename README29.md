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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff728188-1034-312b-973b-5025a52eaf59 | -11.98582 | -51.05788 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 52771ccd-6771-3906-b2cb-d5d35d95c152 | -11.97823 | -51.06831 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b62a5ec2-c144-3ac1-8cd6-3af9435610c8 | -11.96281 | -57.61042 | 2024-10-09 01:13:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c3d7f426-bbae-3380-8f4d-3ae03e3701b5 | -11.96066 | -57.59264 | 2024-10-09 01:13:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fb7e2383-2c28-3efe-9d15-53daf0524e8a | -11.79777 | -47.38785 | 2024-10-09 01:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8ac267d6-507b-373d-984e-7ac8584ac4df | -11.79155 | -47.39721 | 2024-10-09 01:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c79ef399-bc4f-3299-bf3c-41998b00c4bf | -11.78934 | -47.3834 | 2024-10-09 01:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| cca9aeac-dc56-34e2-b111-77aee275bdef | -11.78695 | -47.3896 | 2024-10-09 01:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2b5687cc-4623-348c-bebd-f4aeb43bc450 | -11.73741 | -48.417 | 2024-10-09 01:13:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 028e63af-a4e8-38c0-a2bf-b7eacb09bc01 | -11.69894 | -49.96158 | 2024-10-09 01:13:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f382be8b-eeba-3fda-927a-a78f6a2d443f | -11.5763 | -58.95792 | 2024-10-09 01:13:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 938ae1d2-9d57-3a6a-95ab-dfce37a61b0e | -11.5612 | -49.90811 | 2024-10-09 01:13:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| fc5588ec-69c3-3d3e-b533-148e089b1169 | -11.55341 | -49.91943 | 2024-10-09 01:13:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d30a013f-5f3a-3572-8e31-d16e238f8985 | -11.55196 | -49.90955 | 2024-10-09 01:13:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 160afaad-ca99-32ac-a126-e1ae533eaaa2 | -11.47165 | -49.49849 | 2024-10-09 01:13:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 346094ef-9db2-398e-acca-d7e472fb93de | -11.4701 | -49.48817 | 2024-10-09 01:13:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e129f666-9525-3f16-9b3e-c7e866b42888 | -11.44601 | -54.47351 | 2024-10-09 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c051f1ac-5e11-36ec-9d56-05a7d12f2581 | -11.41952 | -55.21914 | 2024-10-09 01:13:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 735fc496-3341-3a4c-9de0-2a27e54ad47a | -11.38141 | -51.08871 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 05a93e33-e625-34c2-b2bd-a434f61ece68 | -11.38012 | -51.0796 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 848f0605-7ff0-3636-9cbf-0fda6f1a2e9b | -11.36211 | -51.01701 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ee032929-6362-313a-8a2d-39c3924f4fd0 | -11.35449 | -51.02748 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 070e4adb-ba38-3980-a6a1-146745344bda | -11.35319 | -51.01834 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b023b573-eda4-38b2-87b2-c170d2b0867f | -11.32879 | -50.97525 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| aad45ac0-7849-3f07-a77c-408895344df1 | -11.32748 | -50.96609 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f1a5c35e-3e40-3541-bb8a-847fd29c187b | -11.31393 | -51.32752 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5a75e165-d319-3016-846b-7196f517b567 | -11.31265 | -51.31849 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c3c09ae6-606c-3816-832c-af4e23cadf37 | -11.3095 | -50.97513 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 0f6eefcd-09aa-3e13-a5a1-35033a1ac171 | -11.30896 | -51.42043 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f10d746a-2035-3a57-b90b-dbfdd5374d16 | -11.3082 | -50.96595 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 840b5c15-6f19-30c3-9bfe-486a2694a4e7 | -11.28643 | -54.58401 | 2024-10-09 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e0a89318-64c7-3f12-bc32-1eeb485f75c4 | -11.19061 | -54.87693 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b574cadc-0c15-3d31-a908-673912037ca1 | -11.16765 | -54.77861 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 68fc2b01-0e8d-304f-a597-1ff4d9d0cd55 | -11.13791 | -54.00777 | 2024-10-09 01:13:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1f830d23-eacd-32f0-a632-3df6d41503f3 | -11.13113 | -54.3209 | 2024-10-09 01:13:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 788711f4-f4c8-3a75-a9ea-f1c0426e1e12 | -11.12992 | -54.01919 | 2024-10-09 01:13:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 25ae6200-7476-3e1e-a982-2c4f374fb768 | -11.12858 | -54.00909 | 2024-10-09 01:13:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3bed5a09-c4b7-3fb2-9f41-d265ed6a5476 | -11.11258 | -54.0319 | 2024-10-09 01:13:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 61b59c6e-2d67-3eb1-87f4-0165f3459ded | -10.67154 | -51.53888 | 2024-10-09 01:13:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2b468e06-73e6-39d9-bc09-acdc8c16c513 | -10.67027 | -51.52988 | 2024-10-09 01:13:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3478e6cb-cd28-3b8e-b265-53031899bd36 | -10.66626 | -50.92031 | 2024-10-09 01:13:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8820f35e-4de5-39eb-bceb-adc65a156d57 | -10.66492 | -50.91107 | 2024-10-09 01:13:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ccfc6c00-6e02-30dd-880c-1bb0f9dbfa98 | -10.66417 | -51.821 | 2024-10-09 01:13:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d8df71b5-39b1-3d43-8ab8-be48c57d515b | -10.66292 | -51.81205 | 2024-10-09 01:13:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 971489d9-4515-37ee-9f14-3660e685bd14 | -10.65633 | -50.91811 | 2024-10-09 01:13:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| fe6e0f36-3cfa-3924-9fb3-62d080bc1c00 | -10.64735 | -50.91946 | 2024-10-09 01:13:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5f39ac10-4e6d-3668-be82-fc195d964005 | -10.63291 | -55.92884 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 080adea0-6743-3365-9566-1b6f4328e558 | -10.62405 | -55.943 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 296bd8e4-86bb-3c09-bd75-fdc814ea72f6 | -10.62242 | -55.93011 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 8850a619-7728-368f-9bdc-1a54945ba9f6 | -10.62082 | -55.91741 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 38e64070-9f30-3e32-88b3-92a10fb6b1c7 | -10.61732 | -54.60981 | 2024-10-09 01:13:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 265331e8-8045-31a7-8860-86d09f52edc6 | -10.61705 | -54.23969 | 2024-10-09 01:13:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4205f151-d105-353d-9744-69eca507e142 | -10.61405 | -54.61596 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 563686cc-fca3-36ee-951f-6ff7c123f8dd | -10.60654 | -57.53577 | 2024-10-09 01:13:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cb3c50ce-a82e-3fec-b66b-62171f51137f | -10.59678 | -57.55412 | 2024-10-09 01:13:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a7cedd8a-ac25-363a-a5c2-a1fef049c798 | -10.59468 | -57.53734 | 2024-10-09 01:13:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 1a5a34ec-eaa0-373d-abbb-389e1a9d91d3 | -10.54447 | -49.46844 | 2024-10-09 01:13:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5991a06f-c916-372f-b898-269277bc6047 | -10.54287 | -49.45784 | 2024-10-09 01:13:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1ac41634-9f10-3b5f-b9d4-4e5193ddd3e4 | -10.53978 | -49.4647 | 2024-10-09 01:13:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6c7564a7-d907-3502-a8a4-3d0b78eec11b | -10.5295 | -49.10513 | 2024-10-09 01:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bb29e062-58da-3ace-b5dd-ed5eb4e50752 | -10.51972 | -49.10668 | 2024-10-09 01:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2b17f32f-d6e6-37a3-a20f-ff78a1daf14a | -10.496 | -47.52901 | 2024-10-09 01:13:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0187d5ab-2ec3-382c-bb62-acd99e1282f5 | -10.42224 | -60.9912 | 2024-10-09 01:13:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 32e84d18-32e1-3ae4-9dd1-7dc0642616df | -10.39836 | -61.24619 | 2024-10-09 01:13:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 60a0be72-8212-375d-972b-461fa6d8b5e1 | -10.38921 | -61.25348 | 2024-10-09 01:13:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 2e639109-e535-358c-a85c-7f733a1002a0 | -10.3856 | -61.22203 | 2024-10-09 01:13:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cedd114f-43d3-35ae-89de-6c8377627ba3 | -10.36045 | -55.86702 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 18accec2-e74c-36b3-bc7c-d2ea43047014 | -10.35884 | -55.85447 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 433b419a-baeb-3ecc-8f87-c7fe05b88b8a | -10.32793 | -57.5045 | 2024-10-09 01:13:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 23495c25-8284-3438-94dd-523d0a65e674 | -10.25547 | -56.76155 | 2024-10-09 01:13:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ba539616-55c0-3bd5-8a33-6cf8d160a7fa | -10.22416 | -54.26685 | 2024-10-09 01:13:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cc72c509-818d-3efe-9774-88a658b872bf | -10.13093 | -56.76866 | 2024-10-09 01:13:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2456a6a0-9319-38ed-aced-bde712d59ba7 | -10.01053 | -48.85658 | 2024-10-09 01:13:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 67651c37-cfe6-3e36-b848-cc9b5ad2af89 | -10.00873 | -48.8447 | 2024-10-09 01:13:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 74d5e493-d3cb-3050-acfe-032f75ad1faa | -7.6373 | -44.822 | 2024-10-09 01:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 39e989ea-2fab-301b-8b44-59efe3d16955 | -8.35009 | -44.13062 | 2024-10-09 01:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| a0ae4f72-19af-3037-8a31-023b0249ad25 | -8.3489 | -44.12522 | 2024-10-09 01:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| c60ade41-9c28-3e1c-a114-bfa444695081 | -8.34557 | -44.10204 | 2024-10-09 01:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 87e4fdf4-4108-3e83-887d-4490f6185481 | -8.33061 | -44.10445 | 2024-10-09 01:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 790ef5be-af0d-3d0b-8b00-75f98223f738 | -8.32919 | -44.09898 | 2024-10-09 01:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 680e07be-5c40-3b5e-90c8-134539f4bbc8 | -8.00863 | -44.37937 | 2024-10-09 01:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| fff7c3a3-73d8-3f94-a21e-11b10a1cfe2d | -7.73052 | -43.06221 | 2024-10-09 01:13:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 4b948a02-8e0a-34f8-bd61-315f84e34eb7 | -7.63472 | -44.82936 | 2024-10-09 01:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| ae93adfc-8a47-3460-9ec5-ff1e637e0288 | -13.43132 | -48.83877 | 2024-10-09 01:13:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf990c4d-b576-3c52-8b8a-f3fb9b848430 | -12.98554 | -46.20996 | 2024-10-09 01:13:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e2390cfa-f0ff-3ad3-b018-57b98e5b3d3f | -12.87468 | -44.63144 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| c4580110-1626-3cf0-8a52-e2a981835bac | -12.87107 | -44.60988 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 817ab099-5701-3deb-ab0f-c086915749d4 | -12.76222 | -44.9018 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 8f74aee0-6056-35f9-b2c1-5325c8cf34b0 | -12.76055 | -44.89555 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| dfd341d4-60ab-3e1b-82e9-f3f320c76de8 | -12.75886 | -44.88136 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 68f0f4bd-a655-3073-b4be-53a58fe6ac19 | -12.75703 | -44.87506 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2e1e676f-75c2-33a7-bd8a-eb506d993d81 | -12.37881 | -44.97092 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 993b4337-f104-3560-a70a-6b9ac2206562 | -12.36687 | -44.73602 | 2024-10-09 01:13:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| bb6d5ffb-3863-3755-bc14-b8bbb089707a | -12.36683 | -44.75167 | 2024-10-09 01:13:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d70af8cb-b6b1-3c5a-baec-0fc89230bd42 | -12.36312 | -44.73016 | 2024-10-09 01:13:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| c3084e7c-bd36-39f3-ade7-1abd105cd8e7 | -11.89346 | -43.89733 | 2024-10-09 01:13:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2f9cb0be-3c8f-335c-9132-d3f8866dd9ca | -11.65057 | -45.26011 | 2024-10-09 01:13:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 458ae5f7-9201-3307-80c3-157ebc679a76 | -11.1276 | -44.95013 | 2024-10-09 01:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9a257a43-45f5-3595-9e99-0720f1d7d6ef | -9.95491 | -55.33642 | 2024-10-09 01:13:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 892e55ec-7cc1-3112-8001-00034dc56ab7 | -9.85476 | -60.6905 | 2024-10-09 01:13:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |


[Clique aqui para ver as próximas entradas](README30.md)
