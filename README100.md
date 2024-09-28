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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9855a71-f7ca-3153-aff5-1cc819a19001 | -12.85028 | -62.73384 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9ae72f5-2eec-3dd9-8b29-6490bd0191c5 | -12.84827 | -62.73135 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81efcad4-cca5-3b68-95fa-80f88bc6f9e4 | -12.84788 | -62.73449 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01120a43-aefd-346b-82c4-6d8ccf1afd45 | -12.8455 | -62.73 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b9cf507-21be-387a-b2a8-8304bfb47b75 | -12.84513 | -62.73314 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed7fb0b5-d8f8-3e84-ae3d-aee945f7b345 | -12.84312 | -62.73066 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb19643a-33ba-3b3b-b29f-fe0daa9aa155 | -12.79418 | -62.78749 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a229346-753c-3936-98c6-8a119717c96f | -12.78982 | -62.78059 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebffc8d2-fa72-3427-b756-38762df78945 | -12.78944 | -62.78369 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 101a037e-5622-3922-8ddb-f68ea12a6c0d | -12.78906 | -62.7868 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 069767a2-5117-3f02-8dd6-60730ad7399f | -12.78661 | -62.76435 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de0084f8-9078-350f-9301-2166cdf701d5 | -12.78546 | -62.77368 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e9bd726-4e71-36a5-80ce-43d3c37f23e4 | -12.78508 | -62.77679 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ca1cdd7-114e-3ce9-9672-57ddd41088ff | -12.78469 | -62.7799 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cbc2bbf-eb6a-39df-9ba7-a4c70727985d | -12.78393 | -62.7861 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0223dcec-b5b2-3bbd-84c4-daf3dbb29897 | -12.78329 | -62.61977 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a0e68b95-1728-31d7-a43f-0a939d4c3349 | -12.7829 | -62.62296 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b8d9a33c-4363-379c-ab90-e52d8e904f7f | -12.78109 | -62.76675 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7619491-b135-38bf-8dab-600ae1495e84 | -12.78071 | -62.76986 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a392ee2-df77-3adb-a644-95fd8235ef46 | -12.78033 | -62.77297 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13474768-0430-39e4-8659-b2d0a1f0e5a8 | -12.77994 | -62.77608 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d10b6c9-3452-3fdb-9f4c-5498f7f5eab7 | -12.77859 | -62.82937 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f80f827-9374-3f81-8eed-b20df00489ed | -12.77821 | -62.83246 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f750ab0-2344-3e70-9b62-7e8d11836f3e | -12.7781 | -62.61908 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 75cb7a2a-e3ee-3935-835a-e71d3afb7cf3 | -12.77771 | -62.62226 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8de73028-0adc-375d-819d-4f36c52ba60a | -12.77766 | -62.79469 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e834818-352d-305b-8e44-76e87a8317cd | -12.77557 | -62.76917 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e5d6f03-727e-3548-bcae-4b1e1ba117a2 | -12.77291 | -62.61838 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cdc9655f-4144-3381-abfa-ed3a99343fdb | -12.77253 | -62.62156 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0e767f7b-9fa5-3041-bb32-2690e5f2ad28 | -12.77215 | -62.79709 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ecd5fb9-ec63-3ca1-a720-a863775a4d42 | -12.77214 | -62.62474 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8c0ca4cf-5a06-343a-9810-cebd625c04d8 | -12.77196 | -62.84099 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98de5ee5-cc63-3c21-bc9b-a374b6f99ef1 | -12.77177 | -62.80018 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 69422cf8-bc9f-3a69-9dbf-9bdeb652a73a | -12.77158 | -62.84407 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c990d259-0984-3c02-bc8d-377fac1453cd | -12.77139 | -62.80328 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6a9921a5-8c59-37b2-8807-de989c801dba | -12.77101 | -62.80637 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 868cde3c-3346-3418-82b9-ab264880e365 | -12.77082 | -62.85022 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e85a721b-212b-38e4-922c-010675aa6cbe | -12.76987 | -62.81564 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d65d153-9624-38b7-b0c4-8c2569f110f5 | -12.76733 | -62.62094 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 18d28059-715d-30d3-9a68-e030c176f96b | -12.76723 | -62.83722 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e37b6d3-138b-3b5b-9c25-75f31906a906 | -12.76695 | -62.62413 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.0 |
| e8a69ff0-c883-325d-b792-9f021f3685db | -12.76685 | -62.8403 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09477756-dafb-3e90-9f1d-e20e3e27fd57 | -12.76665 | -62.79948 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 747d6f2e-b9d0-350e-9d5d-faa1b1ea27be | -12.76656 | -62.62733 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 9337db19-d66b-3996-ab4d-a87fa3e396b4 | -12.76647 | -62.84338 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1031a713-ab7b-30d2-bb29-32b1f31b8d26 | -12.76627 | -62.80258 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 51baab06-ce86-38c3-acca-c0de884dba5e | -12.76609 | -62.84645 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b355733-3707-303a-a035-d1a07bd4fe6a | -12.76589 | -62.80567 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 832b29c6-1da8-3c52-bd27-4336fde4ee34 | -12.76572 | -62.84951 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d924df2-a6f2-3ede-a530-acacd15d50ce | -12.76534 | -62.85259 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9c54fdd-2e13-3c90-88a2-8030d5bd9ccc | -12.76496 | -62.85566 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 757844c8-8712-37a9-a873-9292bc0df27d | -12.76476 | -62.81496 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 778880a5-48dc-392f-a90a-b55aba0ac3b4 | -12.76459 | -62.85872 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4417e376-ab44-3cae-8589-b54b43e97968 | -12.76136 | -62.84268 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a5fd717-88a1-3830-a5cb-6a812ef9a07e | -12.76099 | -62.84576 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ada6ba46-0ec3-3d5b-aed2-74ffbcaa4728 | -12.76023 | -62.85189 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eaab3da3-28f4-325e-86a7-cd2a0e76b5c8 | -12.75986 | -62.85496 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0274a4e-8748-3f30-88eb-ed9575fdc930 | -12.27486 | -62.31865 | 2024-09-28 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3d5257-6027-315e-90df-3a70759b1aff | -9.11434 | -67.89139 | 2024-09-28 07:01:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 10aa4b40-88bd-31e0-a1b1-b3909264d5a6 | -9.10336 | -67.88989 | 2024-09-28 07:01:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 38264e0c-d9e7-3525-af4c-e14ceda3a4e7 | -12.77208 | -62.59557 | 2024-09-28 07:01:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 05bf62a0-b783-3c4c-9363-ff8f77f2134a | -12.77176 | -62.60375 | 2024-09-28 07:01:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a7f4601c-9442-3a33-a7d6-8ff8b769ec1d | -12.97644 | -62.72671 | 2024-09-28 07:03:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 9cc55869-d8f5-3625-b8e7-b7f58da904d3 | -10.57 | -46.13 | 2024-09-28 07:04:25 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2567d74-9249-3761-b3fc-bca254a51b09 | -10.57 | -46.08 | 2024-09-28 07:04:25 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6bd3b51-34d9-3b9a-96bf-d3e0f8405ecb | -10.54 | -46.07 | 2024-09-28 08:04:24 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0f061fb-fcfe-3e1a-b6db-40b5d6d01fb5 | -10.57 | -46.08 | 2024-09-28 08:04:24 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13894518-2dc2-392a-a0f6-8571fcb7a0aa | -10.54 | -46.02 | 2024-09-28 08:04:24 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c99a3d0-9438-3353-81dc-de95b5d930c2 | -10.66 | -46.05 | 2024-09-28 12:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f63e379-030e-3660-a185-1b694f7127b9 | -10.66 | -46.1 | 2024-09-28 12:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71726a70-da73-3381-8ea7-97762c2d73d6 | -8.99191 | -40.59012 | 2024-09-28 12:49:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 1bc3d0ba-6960-38e3-af7b-a93244da85f6 | -7.4406 | -39.6927 | 2024-09-28 12:49:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 0c2a0a21-8694-300b-8715-6e0163edddb8 | -7.43504 | -39.69862 | 2024-09-28 12:49:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 1ed00412-b811-3dda-ac87-96ee1e2265fb | -7.03855 | -42.13305 | 2024-09-28 12:49:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 16c91e19-9ac4-3858-bba9-f198fc018583 | -3.29946 | -42.62275 | 2024-09-28 12:49:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 581f51c5-6e6d-3fb6-b587-ad82f85ed002 | -3.29655 | -42.23805 | 2024-09-28 12:49:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d9b8c3a5-3b66-3471-87a1-e62905d3e48c | -3.29105 | -42.61571 | 2024-09-28 12:49:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b0ed5d17-1ce5-345b-8ae0-2c86c2120104 | -4.68161 | -41.97837 | 2024-09-28 12:49:00 | TERRA_M-T | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| fae1388d-49c1-311a-ad3f-58ff66c27891 | -4.35511 | -42.08363 | 2024-09-28 12:49:00 | TERRA_M-T | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 72879faf-a054-3cf4-a3d6-5c8ef2e0a2f6 | -4.35224 | -42.07681 | 2024-09-28 12:49:00 | TERRA_M-T | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 6316f141-3538-3588-a620-8a636491ca52 | -4.34974 | -42.09474 | 2024-09-28 12:49:00 | TERRA_M-T | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 194b953e-ca93-32a0-9557-f76244dc09f8 | -4.74194 | -42.97767 | 2024-09-28 12:49:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 320cb450-fdf8-3703-9d7b-074de77d5d5f | -4.53845 | -42.95409 | 2024-09-28 12:49:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 41d585b6-45e7-36ae-9894-439bad0caf64 | -3.98956 | -43.02891 | 2024-09-28 12:49:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d8b98a26-5ace-3fd1-9fa9-b0db82905568 | -3.73085 | -42.82209 | 2024-09-28 12:49:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 68f2c2ba-18f5-3269-b479-f006e5f2e130 | -5.97655 | -42.43767 | 2024-09-28 12:49:00 | TERRA_M-T | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 189dc7cf-b988-3573-bfb6-468c218d4e97 | -5.89278 | -42.77948 | 2024-09-28 12:49:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 2675ec1d-eb50-326a-b42a-b4524fa23461 | -6.32057 | -43.42278 | 2024-09-28 12:49:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f13c9f8a-5aff-3b74-b0b3-9439e4c6184c | -5.86813 | -43.37877 | 2024-09-28 12:49:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4ef613e4-201c-35f9-aaf2-a23872cffced | -5.72888 | -43.39328 | 2024-09-28 12:49:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 46a37b25-8c12-32aa-8ff4-a279a2a74c3e | -5.44259 | -43.30621 | 2024-09-28 12:49:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 56a79756-1b79-38bc-b0a7-c8c96626380e | -5.28882 | -43.25829 | 2024-09-28 12:49:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| afe3bd6b-4134-34eb-b3ed-adf827d0bbef | -5.27958 | -43.07077 | 2024-09-28 12:49:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d5650f79-625c-3c44-8e6b-ff8196cdee00 | -5.06358 | -43.13918 | 2024-09-28 12:49:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ab93bde9-2061-3797-9a45-6c0ca69c6b7d | -6.49708 | -42.77964 | 2024-09-28 12:49:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 31.2 |
| a6ec88ec-f8e8-3632-8884-920dc9ebc3fd | -6.3508 | -42.86902 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 27.3 |
| f9c5d014-a957-39bf-8fe3-fa342089fe2d | -5.95108 | -43.28161 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 40d73668-7139-3bff-b83d-c9041ddaf9a6 | -7.89591 | -42.67159 | 2024-09-28 12:49:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 4d661136-6596-3f04-8425-0deacbe9267d | -7.21485 | -42.47922 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| b3f6d583-8f55-3067-b011-63c65430549d | -7.21238 | -42.49789 | 2024-09-28 12:49:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |


[Clique aqui para ver as próximas entradas](README101.md)
