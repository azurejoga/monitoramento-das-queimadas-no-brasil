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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a22f673d-7e7d-379e-a07a-7849aadf4f14 | -27.87309 | -51.35911 | 2026-08-28 05:16:00 | NOAA-20 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8c1ec98-3732-3fa9-8f3d-af3520d028d1 | -11.1922 | -51.2284 | 2026-08-28 05:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| faf05c28-6132-32b0-83d7-4c557e85bca1 | -6.1657 | -57.7793 | 2026-08-28 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 873ea106-1d67-3a61-8efa-feb8fec1247b | -7.2659 | -45.8668 | 2026-08-28 05:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 8913bfbe-7116-397f-be82-3b61272e7c98 | -11.2109 | -51.2476 | 2026-08-28 05:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e729986f-5040-312d-aef6-dc2ccfde59fb | -6.1472 | -57.7995 | 2026-08-28 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 06440c1c-a781-315d-8373-ec18ffa0bb25 | -16.1641 | -58.5851 | 2026-08-28 05:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 204.8 |
| 0ec42380-b0be-31b8-8f8d-6f4623bb52fe | -12.43 | -43.4182 | 2026-08-28 05:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ac35f6e2-f226-30e5-8da9-d9c6d3e3734f | -6.1656 | -57.7988 | 2026-08-28 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9a4643b4-4690-3d5a-abd6-fd8baea68a76 | -10.5166 | -64.5186 | 2026-08-28 05:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 949a32a0-3d97-3c9c-82e6-cead20c4dc7d | -16.1836 | -58.5831 | 2026-08-28 05:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 242fdf6a-e925-3155-a56a-6dc8df659394 | -10.4981 | -64.5005 | 2026-08-28 05:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 87.6 |
| cf3ad7be-d838-3da9-9d38-a69e0641ba37 | -16.1644 | -58.565 | 2026-08-28 05:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| c0fa065d-8c25-3b8f-bfdd-9b24faee5dad | -16.1447 | -58.5871 | 2026-08-28 05:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| e607f375-eb17-39d0-8f4f-ec07b7a9c2b9 | -10.9367 | -50.5332 | 2026-08-28 05:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b1b7a1c6-cb15-3dfa-b513-cb47a414a537 | -16.1638 | -58.6053 | 2026-08-28 05:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 99fe6777-df9e-32b6-9664-57344ec3e4eb | -7.8828 | -46.1028 | 2026-08-28 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ea1475c7-9458-313a-9ef9-818b2e669db2 | -11.2111 | -51.2264 | 2026-08-28 05:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 4a7d18f0-8c1d-30d0-a45b-7442ac5ae2f5 | -11.2879 | -54.0317 | 2026-08-28 05:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 25ae155e-82f0-349e-93a5-d811696b28a6 | -10.498 | -64.5193 | 2026-08-28 05:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 97.5 |
| bfe14ed3-3e27-3416-bf59-e9b3b91b56a8 | -7.2659 | -45.8668 | 2026-08-28 05:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 711f9646-9b67-38f5-9d22-c99c3133468d | -11.2879 | -54.0317 | 2026-08-28 05:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7ddb0b80-77a7-37cd-9e03-0b4c9e9a73ae | -10.5168 | -64.4997 | 2026-08-28 05:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 24e303bf-f793-3ae8-b646-acdc01d15482 | -11.1922 | -51.2284 | 2026-08-28 05:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0c9a7354-4722-3629-aa66-6c97ab0be1a0 | -12.2847 | -50.5938 | 2026-08-28 05:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 26357498-e551-3739-b0dc-4bd857f9c900 | -12.3038 | -50.5915 | 2026-08-28 05:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a4279bc9-4ce2-305a-bf6b-6b82992bb33c | -16.1641 | -58.5851 | 2026-08-28 05:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 203.0 |
| 2b348330-4944-3deb-bb04-f77cb58e50f8 | -10.498 | -64.5193 | 2026-08-28 05:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| aa723fe1-a98a-3863-8b5a-b764974b243f | -6.1656 | -57.7988 | 2026-08-28 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4cd00bee-60d0-3e6a-979d-db36da577678 | -6.1657 | -57.7793 | 2026-08-28 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 58f70dda-2f8d-3d66-b274-da3079792fa4 | -11.2109 | -51.2476 | 2026-08-28 05:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| daf610b3-955d-3a5b-a48e-e0875960bd2c | -10.5166 | -64.5186 | 2026-08-28 05:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 44df19a8-b712-310f-a60e-e5f104264c0d | -16.1638 | -58.6053 | 2026-08-28 05:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 9519a245-829d-3116-ba93-0636d523abbd | -12.43 | -43.4182 | 2026-08-28 05:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 49dc9a95-9012-3857-b9cb-93cda74de6a7 | -10.9367 | -50.5332 | 2026-08-28 05:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| fd8489f4-739b-3b4a-9832-93fbdbdf1f27 | -11.2111 | -51.2264 | 2026-08-28 05:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 24129cd5-6c76-33ee-b4db-656bc38d4295 | -10.7596 | -54.0384 | 2026-08-28 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f7266d64-dc7c-38a4-b535-ee877423aabf | -7.2471 | -45.8685 | 2026-08-28 05:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| adee4cd0-2d70-3bc9-8500-464419bf0f45 | -10.4981 | -64.5005 | 2026-08-28 05:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 345a03ec-2f0e-38d9-bfd1-581a1780d996 | -11.2109 | -51.2476 | 2026-08-28 05:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 296dcb01-84d8-34d4-9b32-1f374b9f3eb5 | -10.9367 | -50.5332 | 2026-08-28 05:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 7edb3d3c-fced-33eb-b5d2-451a55745261 | -11.2111 | -51.2264 | 2026-08-28 05:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 2b687aef-1b44-3524-9d19-40c17893a088 | -16.1641 | -58.5851 | 2026-08-28 05:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 247.0 |
| a6ad4d8f-cc72-3c68-a0f6-9e4c3c95af73 | -10.5166 | -64.5186 | 2026-08-28 05:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2ed704b6-ca73-3e93-8831-494025aeeda1 | -16.1447 | -58.5871 | 2026-08-28 05:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| c1470dce-1acf-3d1b-b699-bdb421f2f345 | -10.498 | -64.5193 | 2026-08-28 05:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 0536e3f5-4e77-3d57-be11-a73dd4692319 | -7.2659 | -45.8668 | 2026-08-28 05:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8034ba6a-7951-3fa4-8183-efa6a7906524 | -10.4981 | -64.5005 | 2026-08-28 05:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f1bd61b4-506e-3281-b03b-fd1988e7cf07 | -16.1638 | -58.6053 | 2026-08-28 05:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| d21198f1-302e-3c5a-a965-271b1f7b4a1b | -6.1656 | -57.7988 | 2026-08-28 05:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b54166ba-2e1f-3bbc-a7a7-181f825a26b3 | -10.9177 | -50.5352 | 2026-08-28 05:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2c264d8e-5bd3-3bce-a453-2abc482ad9ce | -10.3894 | -61.2502 | 2026-08-28 05:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 124ff58e-19fc-3215-b836-373cfc4262bc | -10.9556 | -50.5311 | 2026-08-28 05:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 8e3a88b0-a3c4-361c-a5da-da2fe98c3207 | -7.2471 | -45.8685 | 2026-08-28 05:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 8240c40f-ccb8-38da-a112-7a48ff2f89d3 | -16.1641 | -58.5851 | 2026-08-28 05:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 406.3 |
| fcd7cb18-1cb0-3042-9851-f90d8b028f1a | -16.1638 | -58.6053 | 2026-08-28 05:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 178.9 |
| 2c8cf056-4485-3241-85ac-242575163002 | -10.3894 | -61.2502 | 2026-08-28 05:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 79f9d78e-dabc-3977-acc2-2aa94cd6bfc7 | -16.1836 | -58.5831 | 2026-08-28 05:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 222.3 |
| dc92fc49-ef04-3d07-be45-4a6b5bdce6fc | -16.1447 | -58.5871 | 2026-08-28 05:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| da75e398-a519-34a6-b6e5-8add5fab322f | -10.498 | -64.5193 | 2026-08-28 05:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| efec06f5-8267-37f5-bbd1-c48c3446df9a | -10.4981 | -64.5005 | 2026-08-28 05:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 705ef565-3e42-3e08-9c87-c4f33ecec922 | -10.5166 | -64.5186 | 2026-08-28 05:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a14accd9-04ac-362f-8e94-85e4bb15be09 | -16.1833 | -58.6033 | 2026-08-28 05:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 0f9eaef8-1863-33df-a666-0e80887c2f7e | -7.2659 | -45.8668 | 2026-08-28 05:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c001bc0a-48ce-3ba2-a9e3-26dd407647f0 | -10.9367 | -50.5332 | 2026-08-28 05:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 8b36855f-3d9e-3484-892e-ba530f16677c | -10.899 | -50.5159 | 2026-08-28 05:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1b88258f-95be-341f-b09e-a61eeb6d9640 | -16.1444 | -58.6073 | 2026-08-28 05:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| a6452f62-5ed9-3f77-bf5b-4f6b5a84534a | 4.13011 | -61.2747 | 2026-08-28 05:53:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1845ca99-d2fe-3c52-8e4a-22527b05362a | 4.13068 | -61.27818 | 2026-08-28 05:53:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58b55dec-29a9-3161-b724-a91895c34c0e | 2.01931 | -61.47198 | 2026-08-28 05:53:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42cab623-7e0b-33ed-882a-465b0b51630b | 4.13926 | -61.25527 | 2026-08-28 05:53:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb9500e8-e505-3d5e-b0a2-f0bee44fd8f1 | 2.01521 | -61.47251 | 2026-08-28 05:53:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e818ee7-cc9f-32ba-a4d9-8ca887f36f4a | -7.39951 | -72.62504 | 2026-08-28 05:55:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fed55877-1dee-3b77-9157-1435cd35e2f2 | -7.58385 | -61.32896 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca40a459-c045-3803-ad6d-ec2e3d75a5e3 | -9.31816 | -68.15293 | 2026-08-28 05:55:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 114028ef-a403-3a3f-9e55-af6de10182fd | -6.1553 | -57.79797 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ab632d2e-f6ad-301e-97a7-8cf9e02e2294 | -8.63691 | -66.53981 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91a86ad4-4cd0-3451-b987-6a2ea166b7ec | -9.05358 | -65.44241 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdf7c84a-e2a0-3e61-9db8-a2943280188d | -8.67478 | -63.85419 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c98e8d3f-cbf0-3e4c-8106-f813105086eb | -10.39599 | -61.23596 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 387fb10c-69f6-36bb-ad96-a389b695c7bf | -9.52042 | -67.16206 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6b08789-2fa6-3be3-ad21-51b9adf43f4a | -10.50713 | -64.50748 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b6f60b0e-c4c9-3a86-a2cf-7c4217bcc70c | -9.52387 | -67.16259 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aac9fa27-151d-35b0-9c87-b37e8361af27 | -9.45771 | -60.53231 | 2026-08-28 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39ae8cfa-04de-3357-a720-1a9456c9c5c8 | -9.8548 | -65.0244 | 2026-08-28 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1783dfa1-5a20-33b1-a12e-a902b3bfb775 | -8.35472 | -70.73837 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acd072a5-c33e-303f-b48e-97a27182cd66 | -9.05423 | -65.4379 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de2e7e6a-369b-3466-9610-19eaf4e8475f | -6.00185 | -57.83236 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bead5df-ff1a-369b-9c16-a862a241fe9b | -10.39098 | -61.23528 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1c07527-9d62-31fb-a771-cb146fa9acd8 | -10.08848 | -68.29378 | 2026-08-28 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a931cd00-f001-3aae-bc6a-240c35d3864e | -8.91269 | -69.43353 | 2026-08-28 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ae06ba6-981f-3aa7-9d26-e7802f5d896a | -10.26693 | -64.50486 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17057cd8-d208-3a23-bb84-51370b544a01 | -9.24797 | -57.0663 | 2026-08-28 05:55:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 183bc857-eb44-382d-9c97-d9c30c27cec2 | -10.5609 | -69.24329 | 2026-08-28 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15f92511-af8f-30cb-95ea-e2edadb3bd80 | -8.99506 | -65.44051 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 875167e0-18dd-34d2-abf1-33533a7a7cd7 | -8.6416 | -66.53248 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1dfe495-1ef2-3b3d-b5c1-eb5d2094859f | -7.49957 | -55.28644 | 2026-08-28 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4a4f5b8-2d50-3357-aba7-a92289f0ef51 | -6.16363 | -57.78106 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9532a326-eb6b-338b-862b-378758224935 | -8.59567 | -70.21437 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a20a760-ff75-3c3f-b294-963a1f7b9b57 | -9.28258 | -68.78269 | 2026-08-28 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README64.md)
