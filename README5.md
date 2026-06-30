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
| a61690ee-9f1d-3384-8715-5ac36597f720 | -20.06108 | -41.86891 | 2026-06-30 03:38:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7a08a49e-18ed-36e2-85c4-c082f11a1b26 | -22.78384 | -49.34317 | 2026-06-30 03:38:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb7ca2d1-47e4-3f90-95ab-0e1181c02ef1 | -22.7887 | -49.35114 | 2026-06-30 03:38:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d929a304-0ff2-333d-9adb-be4ae3e0f68f | -22.78981 | -49.3479 | 2026-06-30 03:38:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85b6cb6c-90d7-3aeb-828a-e9b3e4e479ba | -10.9401 | -43.0355 | 2026-06-30 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 225aa2dd-a09b-33bd-ab3e-3b967ed7675a | -7.4309 | -49.8729 | 2026-06-30 03:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a2221e9e-8798-37f3-b7fe-72796faffa1c | -10.9397 | -43.0593 | 2026-06-30 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 43567267-f660-3ac5-a53e-0a181a0551f7 | -10.9593 | -43.0326 | 2026-06-30 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| f099caaa-50ef-35de-bfe1-d3645de70da1 | -7.4309 | -49.8729 | 2026-06-30 03:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 8337c48b-2268-3b5e-8598-1b94097fe2a1 | -10.9401 | -43.0355 | 2026-06-30 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 240.4 |
| f3e34140-64b9-3542-b5e4-70a5f4c0fb7d | -10.9397 | -43.0593 | 2026-06-30 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| d4ca02b2-d065-3750-a784-4ee4cb82e439 | -10.9593 | -43.0326 | 2026-06-30 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| fb293c2a-01fd-3e68-b142-8d154cc75955 | -10.9209 | -43.0384 | 2026-06-30 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 2d9ae3fb-e899-354d-a5ac-d751f6a2388f | -13.2643 | -56.7947 | 2026-06-30 04:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f400a5d8-0577-3448-9b17-221ffc9f7bec | -10.9401 | -43.0355 | 2026-06-30 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 378.2 |
| ad88f7d4-96bc-3740-bcb5-1cd1649e022b | -10.9593 | -43.0326 | 2026-06-30 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 37caba25-d71c-3d97-8bc2-1dde8860d197 | -10.9397 | -43.0593 | 2026-06-30 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 7f6cc2e5-a9e7-3110-a120-ce29da3be8b5 | -10.9401 | -43.0355 | 2026-06-30 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 312.9 |
| 3f148f61-27b3-32b3-8041-bcc656d7a4e3 | -10.9397 | -43.0593 | 2026-06-30 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 78116f0d-569b-3da4-9c10-fe96e8b83e66 | -10.9405 | -43.0117 | 2026-06-30 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9e46a5aa-e7ed-33fd-8a9a-31a4046b7aaf | -9.20053 | -45.32424 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 452db457-ac06-3da4-b0b8-c17ce7ce4e4c | -9.18734 | -45.32215 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 426add13-004d-32e9-a053-8261c1c0232e | -9.19724 | -45.32372 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d5a9bc7-3f9f-3ff3-a064-fcde4c8014b2 | -7.40618 | -46.82974 | 2026-06-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c337fb4-f8f2-3328-9bdd-547ced41259d | -8.2981 | -46.98649 | 2026-06-30 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d5b89d6-81b9-33d9-8d86-dc28b5638201 | -6.89486 | -43.69684 | 2026-06-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 851c1d5b-beef-3bc5-9d74-fce3507187d3 | -8.29468 | -46.98591 | 2026-06-30 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 938d450a-ac4f-321b-9404-9c2fc363769e | -6.89873 | -43.69383 | 2026-06-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4035ae7-1406-32db-8543-5200edd2daef | -8.19075 | -44.42509 | 2026-06-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff2a4e90-9b21-3470-98d7-8598d788bb37 | -8.20935 | -49.86624 | 2026-06-30 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6697b9-2a57-39de-9f3f-761e231b03c0 | -4.84665 | -42.92926 | 2026-06-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7104bcea-fffc-36b3-b56c-26e2d68f2af8 | -8.99206 | -45.72203 | 2026-06-30 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8b401be-b2c0-3629-98d6-7104afda85f8 | -9.1868 | -45.32562 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e6cd186-a760-3642-ba84-6bafbce0b951 | -7.63869 | -50.02467 | 2026-06-30 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f7ab3cc3-f581-314f-b9a2-3a30c93a028d | -6.8954 | -43.69332 | 2026-06-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 616eab3c-4503-350e-8b70-5ecad55093bd | -8.20993 | -49.86278 | 2026-06-30 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f308fe92-622c-3aac-acbf-49011876caba | -7.43326 | -49.87897 | 2026-06-30 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d97a41c3-1b54-3a10-be9e-1459da28d722 | -6.69063 | -51.96036 | 2026-06-30 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c2ae864-77b0-38d6-80e3-963b202fe161 | -9.19064 | -45.32267 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 421d41e8-5630-3091-af96-08695d3ea520 | -7.40678 | -46.82602 | 2026-06-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4db5b449-a10c-399d-948f-d5a9d17295d3 | -8.60356 | -45.98277 | 2026-06-30 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 68325013-1afc-3a04-84b9-85ecd1eac562 | -7.74818 | -44.18432 | 2026-06-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9316f3f-c6ac-3a3a-bb2b-3a525737a256 | -9.19394 | -45.3232 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a8c16f4-c0a6-305c-99fc-2832aa5fe3bb | -8.98545 | -45.72099 | 2026-06-30 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46e9d30d-6a9a-3ff5-a46a-d721774e0f1d | -8.98821 | -45.72499 | 2026-06-30 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53b87ab7-8a43-3b64-a188-27eb69b2e4e3 | -7.4096 | -46.83031 | 2026-06-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eebf1933-982c-3db6-ae32-097ecf2047c9 | -7.09324 | -41.50545 | 2026-06-30 04:19:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d4a43ce2-4335-3ff2-a31a-fb2ba3551cdc | -7.72582 | -45.91432 | 2026-06-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 231f7c2e-6438-38c3-afee-81e3aa0c9e06 | -7.74102 | -44.1868 | 2026-06-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df3d7c64-4d02-3bee-9bd8-ea8ba890bcb3 | -4.8472 | -42.9257 | 2026-06-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5886e6b4-e699-3531-a0f0-e22e0f0c00a3 | -7.72638 | -45.9108 | 2026-06-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bcb1446-8c25-3751-b1ab-7f1714485272 | -3.94653 | -45.25421 | 2026-06-30 04:19:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0b713ff-73fe-3988-bdfa-939aaf159562 | -8.98876 | -45.72151 | 2026-06-30 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 995bac89-cec8-3eb9-938d-c19510f7995a | -8.98766 | -45.72848 | 2026-06-30 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 711c8739-3b09-35e9-bf13-7d44c195ee94 | -6.90152 | -43.69787 | 2026-06-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9952950-e1dd-32be-b9d6-d537b2f3d350 | -5.50878 | -36.86594 | 2026-06-30 04:19:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 943ca7c5-0a35-3900-9e5e-8e745ea1695e | -8.99096 | -45.72901 | 2026-06-30 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77ba1573-1cc6-3673-9eaf-3adbd3681bd8 | -9.20988 | -45.32927 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b40d531-334a-347a-ae32-370bf09da731 | -8.603 | -45.98628 | 2026-06-30 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1bc156da-e0b5-3c6b-aafe-f75edcf1cd2b | -4.64229 | -42.49416 | 2026-06-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ce7761a-0e55-3395-89ac-182285316ef4 | -7.63809 | -50.02826 | 2026-06-30 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8322c2f3-b28e-3a13-a67f-dc2050de79d3 | -8.1946 | -44.42212 | 2026-06-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42342171-ad5d-3ed1-8ffd-90d2eefbb08b | -9.21318 | -45.32979 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16a7fe5c-d5f2-34c6-97de-b31e59cf67ab | -7.42994 | -49.87418 | 2026-06-30 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 26771638-5e65-3df7-9728-c1a3ce57b184 | -7.09454 | -43.39354 | 2026-06-30 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8cce883d-43bf-3873-a103-07409bbc4755 | -9.19849 | -46.63027 | 2026-06-30 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d62bf495-57f5-3761-8a8a-71f6448a0d59 | -9.20658 | -45.32875 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57a4d1a1-9da2-3edc-9ad4-accfde91a240 | -7.74872 | -44.18082 | 2026-06-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6f3d979-1f65-3fb4-943f-913154e069e5 | -9.1934 | -45.32666 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f31bb3c-8f61-343d-ac0f-0d7319b9bbbd | -8.60024 | -45.98224 | 2026-06-30 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb6e0436-e18e-325e-95fc-b90d849eb697 | -9.19999 | -45.32771 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8375d1c7-6153-3407-857c-286745b9823a | -9.19063 | -46.63634 | 2026-06-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72b8e8c5-718b-3583-bd81-2c4cceaf4bb6 | -6.90206 | -43.69435 | 2026-06-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0c58f4b-f381-35da-b3a0-caa48497e461 | -9.20329 | -45.32822 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 081db886-daa8-39a2-8198-737477410686 | -9.19456 | -46.6333 | 2026-06-30 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40a2fe2c-d0b2-3692-9790-b6b4125a7b43 | -7.42929 | -49.87805 | 2026-06-30 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 562c28e8-e467-3b5a-9e0b-32761157ecbb | -7.51287 | -49.50221 | 2026-06-30 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 62c9f412-e41d-368a-99eb-63d481d1b907 | -9.07226 | -44.7496 | 2026-06-30 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c27fed5b-9b70-39a7-938e-4bc735b004a9 | -7.74433 | -44.18731 | 2026-06-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3930d11-f873-3376-848b-c4255afa71e9 | -7.43389 | -49.87529 | 2026-06-30 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| be795652-4858-3d72-91cf-3011b117525b | -9.19669 | -45.32718 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e66a6a30-f055-3a81-96a6-2ce0457317fb | -7.74487 | -44.18382 | 2026-06-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbf5a772-e56e-3845-a0c4-df55d9f915cf | -9.1901 | -45.32614 | 2026-06-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd3d3cbc-7477-3d4e-b20e-f10847a56039 | -7.09224 | -41.50257 | 2026-06-30 04:19:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 500fe50f-d741-3a2e-bde6-7f9266a6af4b | -10.9397 | -43.0593 | 2026-06-30 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| bcde2e11-5e63-3a1b-a9bb-6469a86f02af | -10.9401 | -43.0355 | 2026-06-30 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 373.0 |
| e599edb0-b56b-3662-b9ec-9ed643b6f01b | -10.9593 | -43.0326 | 2026-06-30 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 6f9758b3-6e36-3733-93e6-9e22b78671ba | -11.63265 | -59.0108 | 2026-06-30 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 789aba8c-9769-31a7-acd6-259e9619e627 | -11.92627 | -57.40056 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbf53d3e-6ce5-30c6-8560-fe5d75f82eac | -12.44423 | -58.4995 | 2026-06-30 04:21:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8386f016-27a6-3aa8-a807-8cb14800720a | -12.45066 | -58.50089 | 2026-06-30 04:21:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26e78920-e7a5-3dc7-9a62-c8fac4f2c8b3 | -9.69116 | -47.69696 | 2026-06-30 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 856f32b9-961f-339c-9e3a-fe11a26ceda2 | -11.91869 | -43.39275 | 2026-06-30 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0ed4a970-a22c-3f72-bd6f-0341ea811cc9 | -11.77618 | -46.4104 | 2026-06-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd29e7c5-e00a-3981-a325-d4c2aa99a750 | -10.90823 | -56.85744 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4d1edf55-0c70-3689-864d-e746dd36b45b | -10.71921 | -51.66603 | 2026-06-30 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae020608-3c66-3e3a-9296-9d29918fd9b1 | -9.99526 | -49.16499 | 2026-06-30 04:21:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c60404fd-32f6-3752-8dc0-3ff8e404f71a | -11.47603 | -47.41655 | 2026-06-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 681fe8fa-6f12-3ff7-87fa-3678e6a7619c | -13.71849 | -47.87129 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 616fb7de-3432-373e-b5d8-f79136c39cfc | -13.69759 | -47.87191 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
