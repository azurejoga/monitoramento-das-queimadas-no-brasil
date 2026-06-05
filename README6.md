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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3340b27f-9aed-3341-8a05-ed311c821b76 | -8.24591 | -47.09374 | 2026-06-05 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dc71beb-9a44-3944-a775-f2a3adbd1c19 | -11.99829 | -45.34963 | 2026-06-05 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 199a3374-e0d3-3c01-b258-effdce29d146 | -11.04023 | -44.3231 | 2026-06-05 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fcc2f91-e456-31b1-a0c8-2cf1f475e452 | -8.72862 | -48.32922 | 2026-06-05 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 310f7e44-7b19-399a-a73e-d72b231d1eda | -8.4076 | -46.88842 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d20d03fc-08c6-3dc1-8ca1-486c892896d6 | -11.11502 | -46.00894 | 2026-06-05 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aed821b6-8269-3d20-ba06-37ca9490eb54 | -8.76667 | -48.43806 | 2026-06-05 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f319a895-5f78-3105-b4fa-4e72ff300c45 | -11.54658 | -48.26748 | 2026-06-05 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5a92dc6-2f81-3c34-9095-9c77583d6d18 | -9.89952 | -47.48039 | 2026-06-05 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d292d149-8e7b-355b-bc52-e1dab22701df | -8.73169 | -48.33481 | 2026-06-05 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ca2e182a-8998-3b97-9936-d2645bfbd4a2 | -10.52062 | -42.36808 | 2026-06-05 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e1d2bcd-8710-36b6-84ea-6815b14391cf | -8.4805 | -46.27732 | 2026-06-05 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9044414-7a90-3744-814f-e3d38bce897e | -9.08413 | -50.61744 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 420502cb-e370-31fc-80cb-b88230c10e43 | -10.38433 | -49.44736 | 2026-06-05 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5a303e4-612f-3ce8-ac07-bd14f5481e57 | -10.84114 | -53.75079 | 2026-06-05 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec9a0d7c-994e-37ec-b223-f698576d0890 | -9.90318 | -47.48103 | 2026-06-05 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67d736ae-835f-3e66-b98e-e85dbaf86647 | -11.5458 | -48.27201 | 2026-06-05 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13c5f7ee-c827-303b-8d31-51191f41786e | -9.3705 | -50.54405 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65090cb1-0195-3af0-ab93-65455842afe6 | -10.38904 | -49.4444 | 2026-06-05 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7689cb5d-50c0-3fa5-b6bb-2925728252c5 | -8.72649 | -47.98357 | 2026-06-05 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33685ec5-dc18-356d-b8a3-1b44bac647ac | -11.11851 | -46.00898 | 2026-06-05 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c4820d4-8ea6-3d8f-ad1a-de6225189913 | -11.38756 | -47.81982 | 2026-06-05 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6c82eae-8215-3b36-b052-2deaa611f747 | -9.37338 | -50.54251 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5cd6a7ca-64d2-3b7f-98b7-57f7cc327a36 | -9.18627 | -58.06122 | 2026-06-05 04:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b8d3afd-f766-3234-99e2-5d3652829d79 | -11.54207 | -48.27135 | 2026-06-05 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 888bca17-4c06-35bb-a7df-0e179ef1942f | -9.92876 | -48.00146 | 2026-06-05 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd5de9d9-16c9-3111-b300-c967de44ae03 | -8.60324 | -45.92435 | 2026-06-05 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1e38041-d5f3-3108-a387-f2fcffd49a59 | -10.38496 | -49.4437 | 2026-06-05 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| babf64ba-d00f-39a4-962f-778b08a710f5 | -8.59978 | -45.92379 | 2026-06-05 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 353cf268-6259-3a4c-aa7f-e5eb3b9e9e77 | -12.03073 | -45.88066 | 2026-06-05 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9472ea0a-1a78-3d67-b676-b769e69a3fda | -8.40689 | -46.89266 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b62f6f8d-bf27-389d-ac7a-6c2741ce61a9 | -11.60359 | -49.32745 | 2026-06-05 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d12fce8e-1e84-3085-ba4b-23230d3d2384 | -12.02676 | -45.88373 | 2026-06-05 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6a329fa-e878-32b7-b89a-2bfcab671bc0 | -8.48115 | -46.27341 | 2026-06-05 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcbda6e3-be65-3131-aad9-41d29a71d3c4 | -9.1791 | -58.05982 | 2026-06-05 04:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1b93c87-4bb9-338a-82d4-31b5e25c3c7e | -8.72778 | -48.33416 | 2026-06-05 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f89c12b1-ff47-3ed7-94ea-ae84bdf1ec4c | -10.93066 | -46.95943 | 2026-06-05 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a73f01f-11b5-391f-9625-14ed9202bc31 | -8.15278 | -47.43615 | 2026-06-05 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb3b74fc-2833-36bc-a956-83678aa0dd3e | -9.08211 | -44.36332 | 2026-06-05 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19a3f51d-9d7b-3838-bc81-47cd7c49ade0 | -10.8816 | -46.99223 | 2026-06-05 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cb9415a-99c4-343e-9173-119f0c1512f5 | -10.52005 | -42.37185 | 2026-06-05 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 00c05289-73fc-3f9b-b431-d0bca84c1644 | -9.36893 | -50.5417 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dd81b9b-fff2-3a37-a7d4-e05117ae9e2f | -10.58627 | -46.77258 | 2026-06-05 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 244ddb79-7d1f-3639-9238-112545481411 | -8.37342 | -46.79854 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9a4bb92-7b7e-31cb-a9c8-1f0f63f29d79 | -8.36912 | -46.80222 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7dd2423-1b90-3e3b-83b4-2f85b7f004fe | -9.08493 | -50.61294 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 470f00f9-39a7-35f7-92b7-e62c1b06e19f | -10.13882 | -49.15618 | 2026-06-05 04:23:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91606569-4a8e-30bc-8d9c-059ccc90e896 | -8.41273 | -46.90219 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af29c5c3-e3ff-3456-b1f5-1a6b090d808a | -11.11843 | -46.00952 | 2026-06-05 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92153aa5-211a-33b3-a488-c725dfec7af7 | -11.03689 | -44.32256 | 2026-06-05 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dee1e373-de50-31c6-85ff-8deb613f8a90 | -8.32282 | -46.99279 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e56967c5-08da-3e94-98dc-fc6728863453 | -8.24447 | -47.10231 | 2026-06-05 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e63cd18-c44f-32a0-8c0d-b99365906632 | -9.73175 | -48.4199 | 2026-06-05 04:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7783033c-35eb-3303-a773-afff3e3cd534 | -9.90242 | -47.47889 | 2026-06-05 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3d8ae99-6f76-39a6-b0fb-07fc49d898cc | -8.64285 | -45.76825 | 2026-06-05 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0a70bf-9741-32ce-91ff-db948d263f33 | -8.72388 | -48.33352 | 2026-06-05 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7d74a83-7fb0-3bfc-89cf-4c7f013ef551 | -12.03014 | -45.8843 | 2026-06-05 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66d87406-624d-3bb0-8687-21395fa9b73b | -8.05297 | -50.68546 | 2026-06-05 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2662e79-62c7-3990-996f-5dffcce2cf5a | -9.68789 | -47.04752 | 2026-06-05 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6ad0550-36a7-3d44-99bd-7c6a641a9a78 | -9.07962 | -50.61669 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7126bed-94cb-3257-9542-17dc99bdd91d | -8.05471 | -50.68399 | 2026-06-05 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9999f7b-9afa-365c-88f7-c67a37faba83 | -9.28647 | -46.5112 | 2026-06-05 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2535faae-4765-30e4-a9bc-a1379e1f922c | -10.88228 | -46.98817 | 2026-06-05 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 045321cb-7113-3377-b238-c64dc903617a | -11.56724 | -47.25184 | 2026-06-05 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7ce0a67-2ee0-3abd-8add-5b6ea66bb179 | -9.685 | -47.04277 | 2026-06-05 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79a122ad-5fa8-37bf-954d-20572e8451e7 | -11.39121 | -47.82048 | 2026-06-05 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef187fcc-a48d-30e9-931c-10b9bede143a | -8.37412 | -46.79426 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6d7e351-1e1b-35be-8818-b8e24e15410c | -9.80735 | -48.23489 | 2026-06-05 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6935f8ee-cca4-349c-a8fa-ab1f7ab6b939 | -11.3883 | -47.81553 | 2026-06-05 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ed7ed66-b767-31d4-8f10-f30797d867d1 | -10.51949 | -42.37561 | 2026-06-05 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0ad3a9ca-0d18-3bdc-b24b-8b1f6e028f2b | -12.02954 | -45.88794 | 2026-06-05 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 391d1bc5-a926-39b8-8bc6-d98378bb4b89 | -11.11903 | -46.00582 | 2026-06-05 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4dcd155-0995-3582-969a-511f6819fca6 | -12.049 | -45.91743 | 2026-06-05 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8512f65d-0e4d-3c68-a37d-56dd198f424c | -11.38464 | -47.8149 | 2026-06-05 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d621959-65ba-36e4-a5d9-c099e1361173 | -11.03745 | -44.31904 | 2026-06-05 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae5c99df-cfe2-3de2-b4b5-97f268fd9fa8 | -10.51662 | -42.37131 | 2026-06-05 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 423493a4-8cf1-3aa9-8197-535ba5952aca | -8.40467 | -46.88372 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4519fe07-d228-308d-ae17-73dfa662c272 | -10.51318 | -42.37077 | 2026-06-05 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 52956d89-9d83-312e-9d42-3be5c05d614f | -11.03412 | -44.3185 | 2026-06-05 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf0901a3-0ab0-37d2-bf33-5f4317d2ee60 | -10.51719 | -42.36754 | 2026-06-05 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6da2d47c-31b0-3dd5-9f78-310d76ce0679 | -10.75588 | -46.55487 | 2026-06-05 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7016bf65-ed5c-3797-872a-c88ebac6ff9e | -9.93174 | -48.00663 | 2026-06-05 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86f378b8-3a7f-33a4-9f7d-68af5838354a | -8.35111 | -46.79917 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3625bd25-01d9-35c2-b79f-5aa29d9061e2 | -8.36983 | -46.79789 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f94d258-178b-3969-a533-fc9be70cc2bc | -10.93683 | -46.94411 | 2026-06-05 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0e0b4c4-b596-3565-b315-f17508e3b817 | -10.38841 | -49.44806 | 2026-06-05 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78769fbf-58dd-3209-9f25-959ee01aecea | -11.04355 | -44.32364 | 2026-06-05 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5512b3cb-3366-39bd-bfc4-27cac8095bdb | -11.90503 | -46.91956 | 2026-06-05 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2cbd545-8b7d-3343-8db7-a40ed5281dcb | -8.73252 | -48.3299 | 2026-06-05 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 080e4d9b-cc1e-3bc2-8377-331b7e2e9560 | -9.08155 | -44.36682 | 2026-06-05 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d23dfa2a-a477-336c-8aa7-7f148cf60d6d | -10.51605 | -42.37507 | 2026-06-05 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 463deaa1-9deb-3efe-82bf-35770d4fe495 | -9.90607 | -47.47952 | 2026-06-05 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e177cd9b-bec1-3fb6-b187-23616ffbde5e | -9.3713 | -50.53963 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a41cc97-36b0-3f06-a574-4ea01551c1cd | -9.76173 | -50.01445 | 2026-06-05 04:23:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 297bfddd-4493-3ece-8246-b87d44a00b2a | -10.79173 | -47.0353 | 2026-06-05 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef3b8343-7a97-3e5d-9f1d-d0f2f9f3a38f | -11.75937 | -47.07743 | 2026-06-05 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ee57232-cd8a-3226-917f-9b07a91bb6d8 | -10.85251 | -48.75514 | 2026-06-05 04:23:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 021f1db2-05c2-3fc3-b678-12b915cc89ef | -12.00439 | -45.35431 | 2026-06-05 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe598a88-5306-31df-9a09-21cf4fa1b166 | -11.63585 | -47.87769 | 2026-06-05 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84060039-7aa3-3747-b62c-e1c29c6c353f | -11.94719 | -46.75135 | 2026-06-05 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README7.md)
