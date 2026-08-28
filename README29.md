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
| 12063b1f-fc30-3fa9-912d-600c29c944a0 | -28.84099 | -50.29975 | 2026-08-28 04:19:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b72a0a88-dbe8-3bcd-bd3f-88edc886f9d9 | -25.10595 | -50.83592 | 2026-08-28 04:19:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bc7f29e5-568e-35e8-bd64-d304bc465b79 | -16.16546 | -58.58654 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 80bfbd0e-d31f-31cb-a970-2a4088814d39 | -25.3209 | -51.89626 | 2026-08-28 04:19:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e9c5bc1a-e9b8-383c-9ebd-eaaacdbcae3e | -16.15392 | -58.60789 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 4b3e13f4-f694-3fa8-ae77-52c47e410044 | -29.03107 | -50.36372 | 2026-08-28 04:19:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5e0d58fd-93d8-364a-b534-240e4263bc8c | -16.14994 | -58.59463 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| ace88714-db97-3b82-8070-5bfaddaa57f2 | -23.45988 | -47.38363 | 2026-08-28 04:19:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c0a753d7-54b8-3f04-8505-a9810d19694f | -11.2879 | -54.0317 | 2026-08-28 04:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6550b31c-45f6-3ad5-9667-a7309a6ad96a | -11.2109 | -51.2476 | 2026-08-28 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 32e369b9-2b2d-3555-a0fe-4da5d8882087 | -11.2111 | -51.2264 | 2026-08-28 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 2cc614df-6781-3f13-9596-02432b896aae | -12.2659 | -50.5747 | 2026-08-28 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ba2a8dc2-7014-3a29-bb13-b01775861a4f | -4.8397 | -45.3926 | 2026-08-28 04:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 79d9f95f-ed67-3910-a6fd-197ef4444115 | -7.2659 | -45.8668 | 2026-08-28 04:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a925ff84-8b99-3436-978b-42dc780791c6 | -12.2468 | -50.577 | 2026-08-28 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 19fcfdd7-6165-3ceb-9265-19c29fb2f06b | -7.2471 | -45.8685 | 2026-08-28 04:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6f51e53b-43a6-34c6-9c08-0399a97126b5 | -7.2661 | -45.8443 | 2026-08-28 04:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 910a5ac2-9e19-343b-b509-9cd058475d84 | -11.1919 | -51.2496 | 2026-08-28 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 48ebf723-86de-3492-9e9f-cfbc966d6a7a | -7.2474 | -45.846 | 2026-08-28 04:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e47b6d94-df5f-3a66-a3fe-7a30b1c2660e | -6.1657 | -57.7793 | 2026-08-28 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| c4284b85-c829-3189-8470-45cbe8286fa0 | -6.1656 | -57.7988 | 2026-08-28 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 614c8042-0add-38ef-9521-278b0ea0d16c | -11.1922 | -51.2284 | 2026-08-28 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 26d73262-bdf8-39f3-a073-499c30c339d9 | -11.2111 | -51.2264 | 2026-08-28 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 61f2ac91-4b92-365a-907b-a4432090b285 | -11.2879 | -54.0317 | 2026-08-28 04:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 55788864-76a9-3d02-ae4e-8202e48d0049 | -7.2659 | -45.8668 | 2026-08-28 04:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6207d54f-ffa9-3d24-a467-32b0629efa83 | -7.2661 | -45.8443 | 2026-08-28 04:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5abcc40e-715b-37be-99ef-c74e542c0952 | -6.1657 | -57.7793 | 2026-08-28 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bf1268ca-3aeb-343f-9b62-c789f443596a | -4.8583 | -45.3915 | 2026-08-28 04:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| bff29c69-4fc0-3fa9-a142-86b97bc69b0e | -12.285 | -50.5724 | 2026-08-28 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 500d08b9-5303-34a3-92fc-f3ada6c0dcd7 | -7.2474 | -45.846 | 2026-08-28 04:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7eb0492c-7964-3315-a5e1-014781c18b82 | -6.1656 | -57.7988 | 2026-08-28 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 207c324f-8fd7-39cf-a76d-3ac94007c323 | -12.2847 | -50.5938 | 2026-08-28 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 5b2f20e4-8269-3b6c-90f9-6e9d115cc21a | -11.1919 | -51.2496 | 2026-08-28 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 68018537-b2da-3394-ae09-a9259a04e807 | -11.2109 | -51.2476 | 2026-08-28 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c34ef2a8-0349-3800-b798-bc3b54229930 | -7.2471 | -45.8685 | 2026-08-28 04:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6a76a4d3-fba2-3ff5-a186-451f23f38d14 | -11.1922 | -51.2284 | 2026-08-28 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 197.3 |
| b90c9f00-f955-3fcb-8fa4-8b4d05de3577 | -12.2468 | -50.577 | 2026-08-28 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| dc5d6de6-3dfe-345a-87b6-dd42d5aa4d28 | -8.9873 | -65.4379 | 2026-08-28 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 83256423-1562-3757-b7c3-971ecc7f3f0c | -11.2109 | -51.2476 | 2026-08-28 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| e7b23c1c-5e5d-3a87-9cce-0e0f16a88438 | -11.1922 | -51.2284 | 2026-08-28 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 734f08a9-8c5c-3a4b-af23-2b5034e37183 | -11.2111 | -51.2264 | 2026-08-28 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 174.0 |
| e2375eb2-b44d-3f10-bc3f-6d83edd37650 | -12.2659 | -50.5747 | 2026-08-28 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 16dbedcd-df15-3f4a-9f70-68af92c2929e | -10.5168 | -64.4997 | 2026-08-28 04:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 816bd086-d9ab-301b-9926-3c1fcdd4fc78 | -6.1656 | -57.7988 | 2026-08-28 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 8cafbcb3-bc4b-30e5-92a4-ab05ae0415a5 | -7.2474 | -45.846 | 2026-08-28 04:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 02574409-38b7-3b4b-a052-064c51b1bbab | -7.2471 | -45.8685 | 2026-08-28 04:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| fcf761ad-7c21-3466-a334-b8f98f8780ae | -7.2661 | -45.8443 | 2026-08-28 04:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 5ecc10f5-f7ab-30c2-aa38-a3cf38a52dbe | -11.2879 | -54.0317 | 2026-08-28 04:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a3de86de-73d0-3355-a3b3-e40d67461fd3 | -4.8583 | -45.3915 | 2026-08-28 04:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| a7b96d04-7a18-3a08-b243-35a7b7737a66 | -7.2659 | -45.8668 | 2026-08-28 04:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 7ddd3542-0326-3306-95f7-da103e2f3a26 | -12.2847 | -50.5938 | 2026-08-28 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a7bfc5b4-310a-3ef3-8e9a-7386608267bd | -10.4981 | -64.5005 | 2026-08-28 04:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f684408d-f466-3013-96ef-4c821a3374e6 | -6.1657 | -57.7793 | 2026-08-28 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 2ebfded0-9457-31ca-8953-6af8b2e086ca | 1.28205 | -50.78445 | 2026-08-28 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a798402-4a17-377e-b4ea-2e793bf6f033 | 2.51968 | -50.8537 | 2026-08-28 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6084f71-c5a1-3388-853a-e4e0451d3be3 | 2.51603 | -50.85427 | 2026-08-28 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c6d4cec-77d8-36a7-b219-81b489d90674 | 2.51902 | -50.84946 | 2026-08-28 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ef47296-f04b-394d-8f78-ef2178659e71 | 2.52334 | -50.85314 | 2026-08-28 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f8267c7-9faa-35b5-8797-760fb90ea951 | 1.27845 | -50.785 | 2026-08-28 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaa88022-cad6-30b7-a2a8-447ac2588c95 | -6.1708 | -57.78655 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0390c3b6-2e0a-3ff7-a220-e12cd1db97dd | -7.08133 | -42.20469 | 2026-08-28 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1731af01-5a46-308f-85cc-fca751d9a74c | -8.08109 | -45.81382 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc1d7367-7905-3879-a119-7675155f9579 | -4.16922 | -42.43688 | 2026-08-28 04:49:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7efa6e85-03c2-3176-8ac7-564e3bf2f063 | -8.08086 | -45.80661 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b2fdb7a-a8aa-378d-92d4-fca0f6efde43 | -7.06946 | -42.15232 | 2026-08-28 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7916cd3d-9598-3164-b9ba-5c97743def92 | -6.51188 | -55.23985 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1211329-5e43-3910-8a85-9533c8c426e9 | -6.43054 | -54.93283 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fe51f34-2aac-378e-8183-ba55537f4143 | -6.2739 | -53.32132 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ae2f4fe-29ab-3f35-8b02-6bfb8c1e235b | -5.47435 | -45.1191 | 2026-08-28 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 850e2c4f-0f6d-31d8-8ca0-a0d3ef712c8f | -7.26433 | -45.86359 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e7495cf5-c7c9-300d-ab66-105a40f28eea | -6.53582 | -55.25208 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09fda5ee-89fc-3eb8-920c-5122806df545 | -6.23055 | -55.93665 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e54f4d7e-add7-3770-83c0-b83b4bc82cce | -6.22716 | -55.93795 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0e4e4e7-4b62-3c01-88c6-dfe0ef74bb8a | -5.52199 | -45.22948 | 2026-08-28 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7c72498-d0cd-3b2f-94df-bdb1d8eb8a8a | -1.36478 | -54.63511 | 2026-08-28 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aa50f81-8f3d-35ec-8b01-320ccdcacaf9 | -4.10702 | -47.21891 | 2026-08-28 04:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cc65371-539f-36ee-bc60-dafe0331dc5b | -4.84557 | -45.39488 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b4b9086-c80f-3888-a484-2a4108f03f9c | -5.89711 | -52.11077 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2f27d531-e91f-3067-83e6-fc6b0fc1e3f1 | -8.08102 | -45.85907 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b48b4b63-cf14-378b-9e70-a3ba891e096e | -6.53095 | -55.25525 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5a4e39a-f6e0-35e3-af4b-58afa35e57b7 | -6.26264 | -55.40895 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83ca37d6-97bd-3f5e-8cc5-e1fc17885d07 | -3.45583 | -43.36202 | 2026-08-28 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a164988b-e1bb-387b-b5a2-20b3357a7af8 | -7.26955 | -49.85348 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e280448d-e667-397c-9657-b56b34526094 | -8.07637 | -45.81064 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efdd36dc-2a68-329f-a4bc-ed54d9389467 | -7.26056 | -45.86303 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 91436c38-fa03-3497-883d-fa000a815342 | -6.25633 | -55.42014 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c557fa0c-52c2-342e-a6ae-f0524b9f1c80 | -7.31168 | -42.96132 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f55f9c0c-602c-3c9b-a18b-d13ce6cb55e8 | -5.28536 | -50.93577 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de52a2fc-876b-3291-9a69-de34e1630036 | -6.13894 | -53.52633 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e1a3d5b-0601-3280-bf40-00aa4ac5d83f | -2.72007 | -49.47368 | 2026-08-28 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8048b65-8e4b-3d4d-92a5-0104e47c9c0e | -6.21723 | -53.58993 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eaa9ec9-311f-37a6-8021-a2d5854bd636 | -3.22239 | -48.60978 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd23d3c-565a-38c8-8a7a-ee731a828df3 | -2.50247 | -48.1357 | 2026-08-28 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65bd90eb-9364-32eb-8bd9-d834b081ba5c | -6.27087 | -53.36256 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb141e16-3bd3-31bd-90ea-180dce40c032 | -5.89641 | -52.10935 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 153d7473-46bc-36a4-87d3-2deb563d3b2c | -6.49724 | -53.25803 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ed0ad88-a935-38d1-993f-b9fe7684152d | -6.15715 | -57.80506 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fc7a09b-06b5-3722-b184-fad188a1f609 | -2.80971 | -48.63005 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9d7b0c3-0639-3795-9afc-14215e9df631 | -2.16856 | -48.78986 | 2026-08-28 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a971b514-8baf-33e4-a29a-22ef00a5f725 | -6.2303 | -55.49487 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README30.md)
