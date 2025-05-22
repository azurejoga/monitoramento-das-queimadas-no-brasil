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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f60935ca-7c65-3b63-be82-a307553c88e4 | -13.80264 | -52.89491 | 2025-05-22 01:13:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1d401e1a-3a87-3c5e-9351-263008c246b2 | -11.7986 | -49.33456 | 2025-05-22 01:13:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| bb55f76e-e79d-3544-9b77-4cb15a76a59c | -12.35372 | -49.99393 | 2025-05-22 01:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c825cabc-ffff-35b9-bb19-317aa4c9c091 | -14.01968 | -55.13077 | 2025-05-22 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 371d8bed-e83b-3e1b-a0f6-f50e6f2b4922 | -12.28386 | -52.4835 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ceb5da77-b813-3e57-a478-0148f6f6bea5 | -11.6079 | -47.63982 | 2025-05-22 01:13:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2b94f4d0-33d2-38c0-9be8-42a67f320398 | -11.6028 | -47.61109 | 2025-05-22 01:13:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 53224ef2-d998-3aaa-a102-3e5ee02c1ce0 | -17.34232 | -51.90021 | 2025-05-22 01:13:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a3cae55c-d74a-37e5-a94f-d8fadeb7803e | -12.644 | -57.18894 | 2025-05-22 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6e2fed0c-fd76-3b32-8640-64793aad61fd | -11.55911 | -47.44168 | 2025-05-22 01:13:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 2ac4e5b1-990d-3b4d-99b7-3bb7fe4fc98e | -12.28571 | -52.49564 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 43898b73-92c1-306a-adbf-b41aac1f2ed7 | -11.56452 | -47.4732 | 2025-05-22 01:13:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| b8c05b05-ab7d-31f0-a5f0-3e9cbc5e6360 | -11.86156 | -52.27147 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b94d76f5-9538-317d-9098-0a30177a5b6c | -12.29401 | -52.48186 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| be962467-43b6-3172-8b2a-437e9210cee3 | -11.41291 | -56.73485 | 2025-05-22 01:15:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f20a2420-b107-308b-9bb2-e6818ad07365 | -11.91531 | -54.41377 | 2025-05-22 01:15:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5795b441-590e-3da8-bbda-7f3a75ce3fae | -11.11169 | -54.66057 | 2025-05-22 01:15:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5f8ce530-f4ab-37ca-ac14-91cdf3bde586 | -12.48689 | -57.18527 | 2025-05-22 01:15:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 46c346bd-e774-32bf-ba29-a2c81d1d7ce8 | -8.91165 | -50.02199 | 2025-05-22 01:15:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6b640b67-3d30-30ad-b6f1-6a6a038841a5 | -12.66252 | -58.22284 | 2025-05-22 01:15:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f2a1a155-2b14-33cd-9b72-87b5f1456d5b | -8.47553 | -49.60248 | 2025-05-22 01:15:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ff2c69f4-1215-399f-89d9-7758d82305e1 | -7.96766 | -49.69937 | 2025-05-22 01:15:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3e4dde08-3da6-3a32-9bdf-6deb0e214224 | -9.29571 | -57.55141 | 2025-05-22 01:15:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 52e7f3ed-ee38-32c9-b97a-6935add26fa5 | -9.96903 | -49.81417 | 2025-05-22 01:15:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 240cb778-feac-357f-93cb-3bd6145d2827 | -9.2868 | -57.55267 | 2025-05-22 01:15:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92b516f3-2a6d-377d-b41d-b2133ba950a7 | -10.34151 | -51.69477 | 2025-05-22 01:15:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 50d3a5d0-1ee9-345c-ac27-9e544bba6341 | -11.1208 | -54.65918 | 2025-05-22 01:15:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d7393114-1f0a-3038-847a-71fd59340b45 | -11.66841 | -54.9412 | 2025-05-22 01:15:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1b1d8380-7578-374f-9741-4b24d6043804 | -11.12218 | -54.66872 | 2025-05-22 01:15:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bc4d00cf-2d7d-3e4b-b867-0f15c195e9ec | -9.95835 | -49.82169 | 2025-05-22 01:15:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9c820d7e-1bbb-3c19-9079-072d71a0aef6 | -10.31162 | -47.02834 | 2025-05-22 01:15:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| d4ff4d28-9ad2-3e9f-af92-dcf5180aa31f | -10.8341 | -56.95229 | 2025-05-22 01:15:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5b987a0c-6a6f-357c-b2ba-958424784065 | -10.36554 | -47.98429 | 2025-05-22 01:15:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| cd1d9cea-965d-30a0-9579-0dc5cc5d0144 | -11.29962 | -53.98727 | 2025-05-22 01:15:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| c5a7a7ff-7bc2-37ee-8e48-b3615d1fafa2 | -10.36079 | -47.95596 | 2025-05-22 01:15:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 5d6c6008-a9b2-386f-9985-9a67b33b2531 | -11.11308 | -54.67012 | 2025-05-22 01:15:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 54d95ecb-4d0b-3cf3-bbc4-96bb6763e36e | -10.35165 | -47.01491 | 2025-05-22 01:15:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e9d30851-737e-39a2-adcd-8b7b3a7bb0cd | -11.08291 | -54.77823 | 2025-05-22 01:15:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7209e6ae-8569-397d-a1fa-f1ebeffc8146 | -10.82524 | -56.95357 | 2025-05-22 01:15:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b45b17a0-1a4e-3e15-be87-1f46d935d06f | -10.31952 | -47.02019 | 2025-05-22 01:15:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d962416f-8099-3811-9854-9a64d77232c5 | -10.32767 | -47.02563 | 2025-05-22 01:15:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 878565b0-67d2-35ea-b414-687c6d5e0d74 | -10.65899 | -49.45201 | 2025-05-22 01:15:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b27f1ac5-47b1-3d5c-8a99-29d83a1fbc57 | -10.65968 | -49.43538 | 2025-05-22 01:15:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 81bf1e07-9139-3db0-9925-eb1363ef1138 | -12.28591 | -57.26408 | 2025-05-22 01:15:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1a544ec8-1f31-3dbf-b475-04ec2fc79365 | -10.68348 | -57.60026 | 2025-05-22 01:15:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 17271431-39b5-31c9-b940-5d60a49c8ad2 | -12.13555 | -54.66092 | 2025-05-22 01:15:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b9465e49-c1f3-3ff8-adef-d6669da593b6 | -12.02138 | -63.79462 | 2025-05-22 01:15:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 7ddaf597-5ef4-3b32-887d-c3849687678d | -11.29813 | -53.97709 | 2025-05-22 01:15:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| c97acc74-45d5-3561-a746-69249b90e032 | -9.02611 | -47.74958 | 2025-05-22 01:15:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b1ab2e13-f639-3e7e-8489-7b66b62189ac | -8.74745 | -49.74604 | 2025-05-22 01:15:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| dd6262c4-82bc-3f9b-a9c3-75dd2a183c26 | -12.27691 | -57.26537 | 2025-05-22 01:15:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 18459986-0330-30ef-9bd4-d4e433d95ab0 | -10.02684 | -48.71087 | 2025-05-22 01:15:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 2ebdecec-edaf-32c5-8cde-bb02fc2cd6d2 | -9.0457 | -47.0213 | 2025-05-22 01:15:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 01268111-591d-3111-b73d-d46f8e6f923f | -10.12237 | -58.22329 | 2025-05-22 01:15:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ef5ca79d-9ce1-3eae-b4d0-14e9de33296d | -10.68472 | -57.6095 | 2025-05-22 01:15:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 28c01d60-34e2-36a8-8137-71dfd2d97349 | -12.27816 | -57.27473 | 2025-05-22 01:15:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 650d2a8c-ea87-343e-86d5-89b7845d7cc8 | -8.75251 | -49.75174 | 2025-05-22 01:15:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| dae4e843-1cf5-3d15-b9bb-5d48959af7e3 | -10.83534 | -56.9613 | 2025-05-22 01:15:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d05287ea-fcb5-3924-a66f-ce7944a1f361 | -10.82648 | -56.96258 | 2025-05-22 01:15:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b7c0f1e3-9e84-32ac-baf3-81daf56e53a8 | -8.48228 | -49.60708 | 2025-05-22 01:15:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 6a0bfa8a-b49c-3298-918e-3d35c9dbc30e | -6.63341 | -55.00912 | 2025-05-22 01:17:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cdbca3ef-9586-363e-a152-0a0f8dd6c8b2 | -19.070499 | -53.464199 | 2025-05-22 01:18:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a3720578-c085-34ee-8854-0049a9a3cc69 | -11.409 | -56.7332 | 2025-05-22 01:18:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8680195-153d-3669-8d98-c12ca26fba4d | -22.9517 | -49.1063 | 2025-05-22 01:18:00 | METOP-C | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 98da0ff0-32b6-36ea-b468-907135c7efb3 | -6.5741 | -51.116798 | 2025-05-22 01:18:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a60a40ec-5f69-39ea-b4ed-113f0434605b | -20.943399 | -56.582001 | 2025-05-22 01:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0770c9f0-7ffa-3aab-92fc-06dfe895ddd0 | -12.2803 | -57.2589 | 2025-05-22 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d99ff8cf-1898-30d7-8e9f-f328b62c5827 | -10.8206 | -56.956402 | 2025-05-22 01:18:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41037f0d-cc4b-3fef-98e6-c9a2702ec98c | -11.2973 | -53.9916 | 2025-05-22 01:18:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c01f6f37-63df-3090-9df7-0ee772637113 | -19.1173 | -52.691399 | 2025-05-22 01:18:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0449d8b5-7799-3af8-9bc4-81d87a9be2a5 | -10.8336 | -56.967899 | 2025-05-22 01:18:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 301f20a0-473e-36aa-ac19-0619512e53ea | -12.2819 | -57.2659 | 2025-05-22 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6e55d9e-f96b-3f72-9451-21005c7bcb25 | -10.0303 | -48.7089 | 2025-05-22 01:18:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80a45759-d0dd-3630-99cf-82b4eb25fd7b | -20.958099 | -56.603001 | 2025-05-22 01:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 43fceee8-4312-35b9-9f4d-bb41e20380ae | -21.4862 | -57.125301 | 2025-05-22 01:18:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ac43ce07-ff13-3771-bb14-cb0ec504f8f1 | -10.832 | -56.960999 | 2025-05-22 01:18:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3f59d3e-cd1c-37bf-8f5e-0c328439bc7b | -20.9548 | -56.587502 | 2025-05-22 01:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d02fced3-aae0-354f-b614-dc9014049bac | -10.8238 | -56.9702 | 2025-05-22 01:18:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8a3becb-ee74-38e8-9c23-6d6c4e6c641e | -20.953199 | -56.5797 | 2025-05-22 01:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8f00c91c-dd44-31e1-acc9-b3bbf9a6d66b | -12.2834 | -57.2729 | 2025-05-22 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5cd2c30-3b4f-3e1e-9b36-fb9c4fac597d | -11.116 | -54.666401 | 2025-05-22 01:18:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15ead626-4b44-3920-9e14-2cb05f44e2f1 | -11.0791 | -54.7729 | 2025-05-22 01:18:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec95004-07e2-34c9-96ee-14411bebdc51 | -20.948299 | -56.605301 | 2025-05-22 01:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1ce2d980-3f2a-39de-99f8-32834b99da5a | -9.963 | -49.820499 | 2025-05-22 01:18:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b018ee5-e14b-33ba-b497-da8ddd91d337 | -10.8222 | -56.963299 | 2025-05-22 01:18:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9463981-1010-335b-8c7f-2ce4b1e6b6f1 | -19.733 | -54.5126 | 2025-05-22 01:18:00 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0ec6c878-30ea-3fb4-bbf8-a3f924074d80 | -8.7478 | -49.7467 | 2025-05-22 01:18:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5a1feb6-e5f8-306a-8525-ae260225275b | -11.2953 | -53.983398 | 2025-05-22 01:18:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e280bfa5-9e0f-3902-b28a-164e2d989a4e | -10.6883 | -57.5998 | 2025-05-22 01:18:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9128965e-6893-3296-bdb9-bf71a29e9957 | -11.1179 | -54.674198 | 2025-05-22 01:18:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5207b02e-3673-33c1-a61a-3429097aade9 | -19.0688 | -53.4566 | 2025-05-22 01:18:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 72065271-33f8-3401-9840-9583066620fc | -20.945 | -56.589802 | 2025-05-22 01:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9b6b4395-ca27-3526-85b7-ee4c0ed5f195 | -19.059 | -53.459099 | 2025-05-22 01:18:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 87966351-bec8-334f-8851-3a0fcb6ec344 | -22.9545 | -49.1171 | 2025-05-22 01:18:00 | METOP-C | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4124eaa2-0902-37e1-95c0-a172137c1dbc | -10.68 | -57.6091 | 2025-05-22 01:18:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 581c6ffd-f780-3360-8c16-4ccd8529bad7 | -8.7519 | -49.762798 | 2025-05-22 01:18:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 393e9d57-c38a-3278-9629-c403c42d8f04 | -20.956499 | -56.595299 | 2025-05-22 01:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 70b1c50e-87c5-3af6-9005-f9c6ba9f7f4b | -11.0809 | -54.780499 | 2025-05-22 01:18:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e68b55b-4279-39ab-a520-637280f4c1e5 | -19.060801 | -53.466702 | 2025-05-22 01:18:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b6ae627d-739c-3554-babf-f2fd934e9e9c | -11.1142 | -54.658699 | 2025-05-22 01:18:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
