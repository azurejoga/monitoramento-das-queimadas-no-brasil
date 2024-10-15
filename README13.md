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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2df45b95-c219-39f1-b957-702bc40c68a7 | -9.4401 | -44.144501 | 2024-10-15 01:01:38 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37aebdcc-1113-3a5a-bc20-f69a7cd72706 | -13.3679 | -61.916599 | 2024-10-15 01:01:39 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a473950-eda5-3cc2-af89-b40bba97db02 | -13.3711 | -61.933399 | 2024-10-15 01:01:39 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0f33eb4-9f19-3c35-9eb5-8d324d5d4286 | -13.3744 | -61.950199 | 2024-10-15 01:01:39 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf3cc050-4ab4-3cb5-b310-7f4e7be02b34 | -13.3582 | -61.918499 | 2024-10-15 01:01:39 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aefd8d12-b43a-3cbd-8b90-119008021277 | -13.3614 | -61.935299 | 2024-10-15 01:01:39 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e08fb86-9af7-3ddb-8490-ffe9deb331ba | -11.5625 | -53.837799 | 2024-10-15 01:01:41 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2677b8b5-2303-3c56-a9e8-5ae47a6ae33b | -11.564 | -53.844799 | 2024-10-15 01:01:41 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0955099-bb97-3947-bb8e-caf69356ed19 | -11.5656 | -53.851799 | 2024-10-15 01:01:41 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 278e8c5a-76dd-3685-b22e-31473c7401c5 | -11.5511 | -53.833 | 2024-10-15 01:01:41 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d889c9cb-2453-3e28-a8bd-b4485a60748e | -11.5527 | -53.84 | 2024-10-15 01:01:41 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69703810-755f-3cf7-a471-a683547d015a | -10.0435 | -47.624001 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee0e0682-1b3e-3d41-a48f-b7a476d50441 | -10.047 | -47.6381 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5733136c-6fe8-3eea-b493-39c4a40a8c1c | -10.0505 | -47.652199 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cbaa7c7-444d-3b63-aa6e-cac55e199d45 | -10.054 | -47.666302 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50f246ff-bc12-3ae3-a7f3-42fdea88da35 | -10.0575 | -47.680401 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb77c57a-5da2-3474-960f-4bc216a9c4a0 | -10.0338 | -47.6264 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44d283d3-cc81-3836-8d36-89b48f6f3e2d | -10.0373 | -47.640499 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65b225ed-c30f-3023-8664-3769b37fc994 | -10.0408 | -47.654598 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11fc5eee-5dda-3155-baf6-00175e8d9bbe | -10.0443 | -47.668701 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aad0e44a-3f3d-357c-988e-edb34a74d15b | -10.0478 | -47.6828 | 2024-10-15 01:01:42 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d90965c-ccbf-350c-a677-5f5457f09d9a | -10.0179 | -47.645401 | 2024-10-15 01:01:43 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab3b88f0-1f34-3c89-8b83-f2d5a03270fe | -13.1316 | -62.265301 | 2024-10-15 01:01:44 | METOP-B | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 26c30434-261e-3118-9122-61fd92a36ac7 | -13.135 | -62.282902 | 2024-10-15 01:01:44 | METOP-B | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac1258a0-6e88-32eb-9e56-2a137d0d72c7 | -10.3403 | -49.603298 | 2024-10-15 01:01:45 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2c9906b-53d8-38d8-9ab0-8f59901b0042 | -11.31 | -54.320301 | 2024-10-15 01:01:47 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee04c293-2cf2-3a95-853f-197b208be073 | -12.9618 | -62.751099 | 2024-10-15 01:01:49 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d88fda6-b62d-3d5c-b250-be353bdf3b7d | -12.9521 | -62.752998 | 2024-10-15 01:01:49 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb10255-376d-3d21-9c3d-bc24092e6d59 | -9.4043 | -46.9174 | 2024-10-15 01:01:50 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d53d3be-dd3d-3dc1-9ff2-76944b5d3369 | -11.4322 | -55.666302 | 2024-10-15 01:01:50 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac29be1f-e6b6-3a94-90a6-4d62d0aff30c | -9.5227 | -47.77 | 2024-10-15 01:01:51 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c76ae079-714b-3fab-a2fa-f41f5fc91226 | -9.513 | -47.772499 | 2024-10-15 01:01:51 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40cf206f-f203-3e67-926c-dbc24cac4db4 | -9.5164 | -47.786598 | 2024-10-15 01:01:51 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9672b98-1bd8-3a81-8f9a-95d795b9d780 | -10.8091 | -53.878502 | 2024-10-15 01:01:54 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2bc6aa7-1660-3c91-844e-f6f7de27ba7e | -10.8107 | -53.885502 | 2024-10-15 01:01:54 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8c4e479-29d7-3721-ae52-baaa213742e1 | -10.8009 | -53.887699 | 2024-10-15 01:01:54 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6960e3cc-69d9-3f3d-8987-0318309d3361 | -9.0971 | -47.6325 | 2024-10-15 01:01:57 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9ce90f0-d7ea-3eed-95e9-a88a7cb973c6 | -9.1007 | -47.647099 | 2024-10-15 01:01:57 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50fdc73d-bf52-3b98-b5b4-5f9fabe9eb55 | -12.507 | -63.221298 | 2024-10-15 01:01:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f045fbf4-9747-3771-8023-5e0d11e9cf58 | -12.4488 | -62.968601 | 2024-10-15 01:01:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eea6e3bd-e32d-3c9a-9ccb-0b0a9ea212ad | -12.4525 | -62.987801 | 2024-10-15 01:01:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a71e7256-7e39-3a17-8374-bae53f1767d6 | -12.4973 | -63.223099 | 2024-10-15 01:01:58 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ca60ec58-e909-322b-a210-18ae2d1334dc | -9.0771 | -47.760601 | 2024-10-15 01:01:58 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec8fe9f6-666f-3069-8b2d-5ac72fb1cd43 | -9.0806 | -47.775002 | 2024-10-15 01:01:58 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a2726ad-e58f-3e1c-bd3c-164940571885 | -9.1085 | -47.888599 | 2024-10-15 01:01:58 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8576556-4654-308c-ad8c-d14e7840a1ce | -9.112 | -47.902599 | 2024-10-15 01:01:58 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78d27bb2-3edb-369c-b2a3-1662e4084a5d | -9.0674 | -47.763 | 2024-10-15 01:01:58 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66b77758-01d6-3510-b7c8-3ff592df5993 | -9.0709 | -47.777401 | 2024-10-15 01:01:58 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9d22896-9a6a-338c-ada6-480cca440219 | -9.0988 | -47.890999 | 2024-10-15 01:01:58 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f45c532-59f0-3ca7-a764-d505735ba537 | -9.1023 | -47.904999 | 2024-10-15 01:01:58 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0cdbc13-eb31-3207-9f61-ff6293eb6d3b | -9.1991 | -48.639099 | 2024-10-15 01:02:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17b7aa06-03b5-331c-86bd-114df34c2ef1 | -9.2021 | -48.6516 | 2024-10-15 01:02:00 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| deb8eb66-eae3-381a-878a-455947406ab4 | -9.1894 | -48.641499 | 2024-10-15 01:02:00 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8648e561-8a96-3fab-a314-b4bcb244bf46 | -9.1758 | -48.840698 | 2024-10-15 01:02:01 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8236a7f-8448-3a10-8912-a393a0c8f859 | -9.1787 | -48.852798 | 2024-10-15 01:02:01 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c0006a7-b66b-3506-9d12-d28b02b47883 | -12.3815 | -63.673901 | 2024-10-15 01:02:01 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07d9f809-892f-38fa-a190-4982567d2912 | -8.9136 | -47.8922 | 2024-10-15 01:02:01 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba33561f-d4b9-3848-815f-f769e861a545 | -8.917 | -47.9063 | 2024-10-15 01:02:01 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b96de0c-be15-3fcb-924d-079cfcba9d59 | -8.9039 | -47.894699 | 2024-10-15 01:02:02 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5be4edba-fb7f-3f77-9dfa-fe1635f5d2fa | -8.9073 | -47.908798 | 2024-10-15 01:02:02 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d161d9c9-8eaf-3d0e-ae3f-28cbb32b7993 | -8.8942 | -47.897099 | 2024-10-15 01:02:02 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 834477f9-add7-3c70-b999-f3b98f4532cb | -10.2728 | -54.242699 | 2024-10-15 01:02:04 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93514ed9-ad01-3c36-b4f2-54e5602b9dea | -7.9182 | -44.489799 | 2024-10-15 01:02:04 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 393a32bb-97df-3e03-bec5-a8632f915a29 | -7.9246 | -44.514801 | 2024-10-15 01:02:04 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c67e92ea-301a-3c6e-97d7-85de413230a1 | -10.034 | -54.326199 | 2024-10-15 01:02:08 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 521b5f3b-a179-3e5e-93c9-cedf72b15390 | -10.0356 | -54.333199 | 2024-10-15 01:02:08 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0906ce4-5bd8-3812-b43a-4ecf83d48e74 | -7.8653 | -47.7337 | 2024-10-15 01:02:18 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36b5382f-c8c9-3769-9cad-ee7db5faf268 | -10.4262 | -60.988899 | 2024-10-15 01:02:25 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5202b4-e656-346e-8b22-c7d7122655e6 | -10.4457 | -61.234501 | 2024-10-15 01:02:25 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d504d9f-369f-33a7-bdec-f64b913f9eed | -10.4484 | -61.248001 | 2024-10-15 01:02:25 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3a82b6-4022-3f29-b697-6e587ab03411 | -7.4859 | -48.077599 | 2024-10-15 01:02:25 | METOP-B | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13e40b63-ee3d-39c6-b4ba-1116836cf4fc | -10.368 | -61.152199 | 2024-10-15 01:02:26 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0646fb9d-e050-3ace-b007-d93b5a07a678 | -10.3707 | -61.1656 | 2024-10-15 01:02:26 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf88126-072e-3c2d-aff0-8c40e79f0109 | -10.3734 | -61.179001 | 2024-10-15 01:02:26 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f235ada-955e-35ba-98ce-11636249a8c4 | -10.3582 | -61.154202 | 2024-10-15 01:02:26 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9b8e2d5-4fe9-3c0b-8dec-3c263e15be59 | -10.3609 | -61.167599 | 2024-10-15 01:02:26 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b793ba3-b0ee-3b54-ad7f-5ad95d6adc1f | -10.3636 | -61.181 | 2024-10-15 01:02:26 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c7b171d-2b9d-3b6b-9806-8b1835253623 | -7.6494 | -49.352001 | 2024-10-15 01:02:28 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac72048d-46c6-3325-8c5c-26eb638cf68d | -7.5132 | -49.471901 | 2024-10-15 01:02:30 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeb71bca-da8e-3312-87ef-8379c34172ee | -7.516 | -49.483601 | 2024-10-15 01:02:30 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dbc49f1-3a0b-309d-bfeb-1100d6604fdd | -7.5035 | -49.474201 | 2024-10-15 01:02:30 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2a3f9c-38cd-3967-b949-76c957309b4c | -6.3099 | -45.261799 | 2024-10-15 01:02:33 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3737b829-61a8-39ff-83ac-15ebdff99c79 | -10.0061 | -62.071701 | 2024-10-15 01:02:35 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 41c851de-738f-3fb3-9084-bfdfa3036de2 | -6.5611 | -48.210201 | 2024-10-15 01:02:41 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f64de9a4-0918-3ffc-9493-e3c32c7754ba | -6.5647 | -48.224899 | 2024-10-15 01:02:41 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7b38a1cc-f3e2-342c-a21e-43d55f873fe9 | -6.555 | -48.227299 | 2024-10-15 01:02:41 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6a282f78-7c54-3c66-a869-75c52657bca4 | -6.5585 | -48.241901 | 2024-10-15 01:02:41 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 74907edc-23e3-379c-9cd1-19c9297ffb8b | -6.5417 | -48.214901 | 2024-10-15 01:02:41 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b53b5830-0f7d-3651-98ef-44b7cbf14407 | -6.5452 | -48.229599 | 2024-10-15 01:02:41 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 50ca3fd6-31f5-35ec-99c9-b3e1873a8af2 | -6.5487 | -48.244202 | 2024-10-15 01:02:41 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 30737c11-827e-3356-b6dc-5a26260db575 | -6.5355 | -48.231998 | 2024-10-15 01:02:41 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 47726e09-dad5-3d11-8422-a6aea3bfdda0 | -6.0305 | -46.577999 | 2024-10-15 01:02:43 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3bba402-1028-3820-b7c0-228fd86a52e8 | -6.6632 | -49.449699 | 2024-10-15 01:02:44 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5b7ac5-1035-3fa7-ba57-7baa9d894215 | -6.6534 | -49.452 | 2024-10-15 01:02:44 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 163900e0-ab0a-3280-ad85-13e07bb08957 | -6.4143 | -49.572498 | 2024-10-15 01:02:48 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f57be01-ceb6-3c73-bcab-13d000c99b5b | -6.4172 | -49.5844 | 2024-10-15 01:02:48 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26f0646-4d02-364e-adc5-23feecef9d7e | -6.4046 | -49.574799 | 2024-10-15 01:02:49 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe023c1-4f64-3b16-8d13-752030230ab7 | -6.4075 | -49.5867 | 2024-10-15 01:02:49 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9622ee3-734d-3362-a157-1f16f71146af | -6.4103 | -49.598598 | 2024-10-15 01:02:49 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfa5654d-019f-3c86-b4fd-10c7150d9fad | -5.2087 | -44.820599 | 2024-10-15 01:02:49 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
