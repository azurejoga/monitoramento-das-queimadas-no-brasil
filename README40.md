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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb938698-0daf-30f1-8f29-66782a80b983 | -6.81704 | -58.6482 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0abd9dc-56c8-3d3e-b84a-822b758891a2 | -6.74364 | -59.65805 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c093b81e-db0c-3e05-8704-d56592f3d38b | -7.78862 | -56.28246 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2df97db-b816-3261-89ec-0d2bdefe7b33 | -5.78101 | -57.55476 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0495f19-3817-34fd-8eb3-5dfa99b562b2 | -5.00825 | -56.13626 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa31f4bf-c4ef-3a23-adbc-0a372baeeb5d | -6.33613 | -55.87307 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39ae8698-dea2-31fe-aad2-899c12d234b5 | -6.14572 | -57.94485 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5becda45-3356-3328-b185-e62a7cb77bbc | -8.54794 | -55.28672 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90804b58-e540-3a23-b14c-cab113d304f4 | -5.7771 | -57.55415 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a40d350-8c05-3576-a19d-72a5cc88c7dd | -6.61556 | -58.38099 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dcd52f8-28dd-36de-b1e1-7aea95003b33 | -7.68053 | -63.33327 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 95dd8260-bc87-37c3-8ff8-518cb39e6454 | -6.86478 | -59.40833 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18e4e5db-d6c3-3f12-949c-c782533883c9 | -6.1784 | -53.5308 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2411a65f-62fb-3945-8e89-262a049e4f8e | -6.19949 | -53.53075 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f99d537-9c20-3efb-af61-574042722a11 | -6.79344 | -59.80931 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fe1e174-fb03-3051-8dad-2a68737a3899 | -6.94958 | -59.07114 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88e588dd-61c1-3854-9549-5c7a203f612c | -6.97077 | -59.07866 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 884b182c-d1eb-3ee7-ac32-d7ff8694920b | -4.93262 | -55.77589 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29300cd2-d753-3099-a439-60d97d6fd938 | -6.77591 | -59.44617 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f4b69d9-da4e-31a4-bf8c-3232765ea34b | -6.95623 | -59.07645 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d3c73b9-2fbf-335a-aade-3a4690302877 | -5.94379 | -57.73416 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c5694e2-5e40-355e-ae82-37b13f5be3cd | -6.96536 | -59.06488 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73681d59-31b0-33bb-8e14-9faf4b908098 | -6.84301 | -52.50646 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d1786b2a-926f-3f4d-ab1c-6eb99ad882c1 | -6.15338 | -57.94604 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 32a930cc-e823-3a44-a69e-d36b7f17b46a | -6.86059 | -59.41187 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e901177c-ebd4-35d5-8694-856dc7f6d84b | -7.76412 | -61.08331 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a962b717-4acb-3ab5-bafb-b7e3bbb2a917 | -6.64026 | -58.47947 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25169469-1ca7-3eac-90f2-db2966992798 | -6.61863 | -58.38612 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e8b26ca-2650-3c20-a6eb-f520f6295c95 | -6.1239 | -57.83699 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b60435c8-6c4b-38aa-adb9-36406e9aab40 | -7.68441 | -63.33028 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f2a097d1-fb87-3fcb-ad77-40fb7f650aa6 | -6.63652 | -58.47892 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ccbe3ad-138c-3c42-bc8d-58dfebf88161 | -7.67775 | -63.32924 | 2026-08-24 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86e64fdd-62f1-3d6d-a628-8885c1208fa9 | -5.81066 | -55.71169 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 526e442a-161a-3b2b-bbe5-921ce96bec96 | -6.38597 | -54.97873 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ecdb8e6-4dc0-3379-9e12-53657f395e19 | -6.79135 | -59.65583 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8146ee3f-061d-393e-ba45-99c7b7ba235e | -4.47263 | -55.66387 | 2026-08-24 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fae767d-3b81-3860-bcd6-af898b3e7a61 | -8.57856 | -55.27523 | 2026-08-24 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7c84e47-3adb-344e-b547-8807912e58c9 | -6.38059 | -54.98296 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b323996-2734-3473-a02b-9fe492fd8b99 | -6.13232 | -57.83341 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6de0a766-0369-3ae2-8874-f85765265fed | -4.6094 | -55.73984 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 930c40e4-6382-3062-9720-6f9b09342b48 | -6.78031 | -59.43694 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5a5565e-54eb-3bad-a067-603a3880a5f8 | -6.38994 | -54.98455 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50757855-b029-367d-aa4f-e4fd88d9abf5 | -7.27116 | -49.91641 | 2026-08-24 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 214885fa-123b-3f81-b1bf-b00e7b1aa21e | -5.8756 | -57.56364 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f175ba9-d453-315b-b033-170ed71b2a10 | -6.63586 | -58.48343 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 637fb07b-118b-3e92-bdad-fe8b5da4299d | -7.76529 | -61.09832 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b445bae1-8ec3-3a17-987b-5e361c55ceed | -7.72051 | -61.10957 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d14849c-bc88-3e4c-b9be-5cb6c0a83088 | -6.19433 | -53.52999 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ca0710-2fb2-38a9-a31e-b430febd4a21 | -4.99497 | -56.13828 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19241621-f18d-3cb0-b17d-5f2083431b57 | -6.17883 | -53.52773 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7904c084-c599-30f6-bfe4-1cde6d237779 | -5.78347 | -57.56529 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a349e604-2aea-3f9d-ade6-026c575ea957 | -6.1939 | -53.53306 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d593beca-1fcf-3892-9a71-ebf2a8cadb4a | -6.12704 | -57.84238 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd824e06-45ae-3420-a6c1-2a1b71dddeaa | -5.94273 | -57.73138 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c585f0d5-d9fb-3bea-81ba-e7dcdfb7e8d4 | -5.78029 | -57.55973 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f5c6087-e2cc-32b4-a6a6-69066814684b | -6.95987 | -59.077 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68683394-62db-334c-9605-c000382c818d | -6.1392 | -59.91949 | 2026-08-24 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b0f4092-eafc-3668-8390-84db57707cff | -7.26051 | -60.61427 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 378ef272-fe1c-388d-8810-c4af9f387308 | -6.19519 | -53.52384 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9e321b3-922d-381c-b5cd-801865a65939 | -6.34555 | -55.87003 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f83a2815-2494-3e86-8424-64336dd772ac | -5.81121 | -55.71011 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db63f807-243e-3b76-8652-d39d98a4f208 | -6.26277 | -55.41789 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eff371bb-8cb6-3ae4-995a-1353706c9073 | -6.3335 | -54.75755 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1c93c59-ea5e-38c4-9c57-c530853b3ba5 | -4.4816 | -54.86695 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8cb49e4-d6fe-3539-b15c-829daff13cc7 | -5.8781 | -52.10719 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee27a155-67c1-3f38-bd1d-261e5c22e234 | -6.34227 | -54.76414 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 247cce1f-fd8a-3224-b366-94fc440c8fd3 | -6.82834 | -59.67356 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fec40262-8bda-3fc4-b05d-4aaca1b51148 | -6.79968 | -59.60009 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91b8e9fa-1ab6-3188-928e-cea23d2e01a0 | -6.38129 | -54.97797 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfc1c344-e0a0-3e41-9456-a7b2d02bb678 | -5.9466 | -57.73196 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 675e8dc8-428c-3a5d-9656-94d977b6ad25 | -6.61112 | -58.38492 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d66d59fa-fc02-3950-8f2a-12b03f137bd9 | -4.99987 | -56.13651 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d07aca7-cd51-374d-b667-edacbfe85e2f | -6.6396 | -58.48399 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2682362-56f9-3e48-9c0e-b197dbdca20a | -6.84248 | -52.5104 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2d83d3c4-56a0-3461-a6a8-8908e2fe69f6 | -6.61487 | -58.38552 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4ec984a4-0655-396c-820b-fe70099ba679 | -5.69395 | -53.73961 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ef557ac-8f40-3fdb-bdda-3f1e372e4940 | -5.87483 | -57.5687 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eaee481d-c8d9-3d41-ad63-5fdeaeb3e8bd | -6.70314 | -52.08899 | 2026-08-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4a94756-faa7-3f66-b05d-9a8396ce7dd7 | -5.87106 | -57.56975 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07def947-a669-3400-9ee6-fb18748307df | -6.96651 | -59.08232 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52213190-b8f9-3151-b0f4-5b2ae79567dc | -6.94595 | -59.07058 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75c7622c-fabc-3a00-9966-a509b313acc3 | -6.14641 | -57.94004 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37ad653e-ff68-3888-bbcc-cb647909f01e | -6.85641 | -59.4154 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae515066-aa56-3f64-bb3b-553426a3d252 | -6.82542 | -59.66905 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a84da000-cbbc-3cc1-9a97-e787c1fb7693 | -6.86519 | -56.41541 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 315cdabe-8d3b-3af0-a200-ad08151ff206 | -6.34703 | -54.76485 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ced243b-82fc-36b2-9eb8-f65d8913d867 | -6.69428 | -58.72113 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a4b1e7-a797-37e4-a352-336e43aaed58 | -6.54902 | -56.17738 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 620342de-687a-33fe-bb3e-eed5a9f87384 | -6.34447 | -54.74866 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 427583d5-d685-318e-8be1-d090796bc66a | -6.35055 | -55.86643 | 2026-08-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41275533-0457-3cf6-9064-5f1681638a65 | -4.99289 | -56.038 | 2026-08-24 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3565d7d1-5fc8-38c4-ba89-3183661f4a93 | -7.02234 | -59.56269 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd9ed654-2edb-3b07-8c9b-14ea081b60fe | -6.12846 | -57.83283 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 004f0aae-aa40-34ef-a636-fa853fb944d0 | -6.7008 | -58.95613 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06f93c3a-9891-3f07-9906-47c2424f86c8 | -6.74303 | -59.66199 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdf1cfef-7660-3f5d-8610-1c41d496a57f | -6.35251 | -54.76044 | 2026-08-24 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65f36c3d-351f-3b68-a26d-bd8a0d83eaa7 | -6.89194 | -59.02944 | 2026-08-24 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d38722c1-e570-3ccb-8e5d-0677a8fd4d08 | -6.60805 | -58.37977 | 2026-08-24 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88e49ca8-1846-3d3f-aad8-9da78dedf5d5 | -6.8201 | -58.65324 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 139a0347-3f9a-3c30-a350-ee040336caed | -6.80768 | -58.6604 | 2026-08-24 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README41.md)
