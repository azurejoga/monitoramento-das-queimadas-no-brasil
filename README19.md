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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55ca854a-c6ef-3035-8667-15d76a6de6bb | -8.03247 | -43.84668 | 2026-09-11 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 620fb91d-b5a3-387b-a045-4cedb4aeffac | -6.84202 | -59.36257 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e2cef44-c2b2-3490-b9f8-1f02bdeb5c9c | -9.17271 | -49.95298 | 2026-09-11 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee7491e2-0019-364e-9123-48e6063bbf0a | -6.80001 | -58.89622 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34575340-48a5-38ff-8a36-e320d5d64b46 | -6.19598 | -55.2766 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcbf9e59-b4e9-31c2-8d39-1d5973cd4b74 | -4.36412 | -47.78311 | 2026-09-11 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 6614899d-8f84-37e4-8567-8b770dbf4cf7 | -2.71995 | -57.6108 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 755b956d-860b-3ea5-818d-9c5f0cef210b | -6.19845 | -55.26105 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 925c71af-335d-3bf2-b38b-cded476dccdc | -7.26075 | -45.35043 | 2026-09-11 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2713af8c-3589-3e88-a1ed-c8bf00e80406 | -4.29976 | -49.1091 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3816b9a0-0acd-37f2-a679-8095d49d2923 | -3.40167 | -54.07771 | 2026-09-11 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15707f8e-58fb-3fdd-a487-3505533d4685 | -4.82327 | -54.72091 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5e981e9-1479-36af-8e0a-2ca75dfaaee8 | -3.0935 | -51.29188 | 2026-09-11 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed0a1b78-9919-389a-b697-72727a5c93d8 | -8.78097 | -44.17941 | 2026-09-11 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0cfc1138-00e2-3778-8bed-41ff1f624aec | -6.6282 | -55.29558 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbe4f871-8d13-36c3-a578-e52cf43a580a | -5.29106 | -49.01497 | 2026-09-11 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce8a0ac4-7aef-32d5-8670-320225e11d52 | -10.27286 | -45.31937 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6284a7c7-5b10-3f2a-8c10-42a1b601164b | -3.53746 | -48.18461 | 2026-09-11 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf135b3c-b453-3b21-8807-cbe452a8fe3c | -4.36077 | -54.77894 | 2026-09-11 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ff3f2a8-447e-38b6-bf6a-47b6d226e481 | -8.50399 | -50.14802 | 2026-09-11 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b3f9048-739f-31cd-9a42-7f6f12338a78 | -6.79305 | -58.89499 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e5f2e74-eab7-372b-8590-58eec70bd1b1 | -2.94182 | -50.46637 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b1a31bf-a0d6-3bac-97f8-cf7939522be9 | -4.35588 | -47.56623 | 2026-09-11 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fcdbd4ac-e75e-3d81-a9bf-54951d369163 | -1.7749 | -54.94448 | 2026-09-11 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| feffcc2e-f188-381d-9c4c-490c2125c880 | -8.28002 | -47.78536 | 2026-09-11 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e4ad129-47f3-3a52-a7df-dab1381902cf | -5.86141 | -49.76788 | 2026-09-11 04:51:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b76b57fe-11b8-397d-8b29-d71c9cea2bff | -5.76237 | -45.08488 | 2026-09-11 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eff00c61-90c4-3ac1-822a-3a5986aac23c | -9.70037 | -43.46049 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f19944c9-3dc6-37bd-949d-2f39d0bd0b5d | -6.80162 | -58.89648 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5902e238-7d7b-36e8-9b2d-e8278dfc2dd4 | -2.72353 | -57.61531 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9276490-304c-31e9-afdb-040bcb4f5234 | -10.05707 | -46.28312 | 2026-09-11 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9cea5ee-9481-3696-819d-8aeb52d2e44e | -2.73973 | -57.62182 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 508b7e5f-5d48-3f70-b5e0-2a9308ca4ba1 | -4.02376 | -50.45516 | 2026-09-11 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdc57ac5-761a-32e9-a80b-c8756d3cfd13 | -10.27467 | -45.27091 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b5117d3-eecd-3c34-96f9-86423aae38c3 | -4.82837 | -42.88607 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a45af0d6-c124-3416-81ce-2fef72e947fe | -2.94465 | -50.47047 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a8e7c04-bbf0-31cb-9ec9-f851b0a903e3 | -3.26646 | -50.08561 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30be6f9d-1fa4-3c54-8f00-3adf7bfa3b45 | -3.40225 | -54.07401 | 2026-09-11 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aac6930-6677-3852-a3f6-de32d05d9dda | -4.86822 | -56.00802 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| feb20493-b74f-3d58-87cd-1d65f70abefb | -3.06642 | -49.52094 | 2026-09-11 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57d62754-b4c0-3b9b-94df-f26bc0014567 | -6.56208 | -56.01976 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 056711f8-1b94-3088-893c-27a9904d1b38 | -4.08371 | -48.95529 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b797ade8-8c2a-3c36-9d34-43e4e9f74a36 | -2.93962 | -50.48074 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4c4205-6936-3a53-89c4-b8501676dac5 | -6.8189 | -58.99229 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6ae4c16-c49f-3d29-be08-f133624bd045 | -10.22001 | -45.21689 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a796072f-731e-3a1f-b26a-ded69c3bebe5 | -8.16273 | -45.57768 | 2026-09-11 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c6a9c33-78e4-3f5d-88e4-df5819b027fe | -3.36926 | -50.76231 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebe66b59-6d8c-3a90-af92-18f7402cc284 | -8.82521 | -46.9161 | 2026-09-11 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 60a456fa-e496-39a8-885a-341b2bb5a8df | -4.52565 | -54.95134 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54f0281c-d9c9-3275-9e43-6286b285226a | -4.03715 | -50.88642 | 2026-09-11 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24ffd27c-994c-3b06-9822-7b3687a207c3 | -4.52502 | -54.95525 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c81b810c-8e52-32d4-8820-cd71d6d73ed8 | -4.82938 | -42.87922 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e49f24dd-07cc-32a7-b34a-c8d6e2899dc3 | -2.72587 | -57.62756 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 358ed2c1-d6c0-305f-97d2-25c7d668f2ef | -9.50889 | -40.33823 | 2026-09-11 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c82ec117-18c2-320e-aa38-a13dd141056e | -3.25136 | -50.8209 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c85f0cd6-63e5-3069-b63f-94a737f2404e | -9.63401 | -49.01755 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 52a3d486-9f1f-38b5-9857-09f6b3d13dbd | -2.72166 | -57.62689 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3a3fbe8-b3f2-3b3d-ab91-68ca2ecd3e10 | -10.60596 | -45.22472 | 2026-09-11 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9eaa3c91-2681-3ed3-b0ec-e7f2e2e94f97 | -4.53778 | -54.96534 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce942c6f-0769-3f69-9bd5-96e76d2f7e1e | -9.7082 | -43.39804 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 88d71022-b11a-39a5-a1a4-c09a71019033 | -4.30401 | -49.10548 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| cd73de5c-e8fb-3216-a6c7-ee6f3dc5aff9 | -4.82389 | -42.87841 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aca67d52-c960-34ba-a575-a1987500e7fc | -6.79665 | -58.89984 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6b2d990-8755-3cd2-abd8-867abdd7a0bd | -4.08039 | -56.29968 | 2026-09-11 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a53e8075-53ab-38bb-9921-522015dd9390 | -7.96921 | -44.00809 | 2026-09-11 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d958d119-754e-3645-a6fb-ce1b9da53a1d | -3.37598 | -50.76334 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74c9dfdb-0047-37e5-a143-ac2d5644cdd3 | -6.77102 | -59.43203 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f76572b8-b930-30cd-9be6-78b3e4280801 | -6.62758 | -55.29947 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41713b09-3ab7-3215-b242-a89764d0d243 | -8.50758 | -50.14855 | 2026-09-11 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b3f185b-1510-3ed3-b964-fe0d32121812 | -9.51381 | -40.34424 | 2026-09-11 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8bc4435f-c127-3f8d-ae85-958bd8f6efdf | -2.94527 | -50.48895 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32dfd38d-8a80-32c1-8118-943cc8772c3d | -4.86155 | -56.0025 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69e6622e-c805-327f-a956-d2ba049936bd | -5.37245 | -56.02037 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50214832-252a-38aa-adee-86953968659b | -2.787 | -47.61579 | 2026-09-11 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89426b3f-7b7c-3fa1-bd0d-1a1f06dac427 | -4.45393 | -55.43863 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e7b1ea4-db95-3950-820b-b8e2b0c641c5 | -6.76657 | -59.4313 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 002b0734-57e1-39f3-80eb-81c518e05515 | -4.82371 | -42.88409 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| defc5929-0812-3d5f-bb6d-6937d3b75dfa | -6.32197 | -55.8518 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a767e74f-3f76-3b7c-adcc-d7af466aad43 | -7.18003 | -43.61494 | 2026-09-11 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df342e05-405c-32a9-9c3c-05fb1dd638cb | -6.0875 | -57.90553 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c020335-4bfc-33d6-9f87-8d884fec5e3f | -2.93397 | -50.47253 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 049de269-cdfc-361a-9a0a-4268a33d183e | -3.3681 | -50.74754 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4536bc91-0114-3152-94c1-0c70e16c0e7f | -2.73552 | -57.62115 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72d8518a-6cef-3379-9123-da6f7a5b277b | -10.22866 | -45.18973 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb51081a-b595-3ce7-b80f-4f2ad178f1d7 | -4.47596 | -54.89656 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89a1a90f-1210-358e-9326-fc1b4ff3f0dd | -6.84276 | -59.35812 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97904ebe-59ff-363b-a7c5-c7c2222bd8a6 | -2.94244 | -50.48484 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0379faf5-e9ba-3f0a-a314-ae61063318fc | -5.37175 | -56.02467 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8b00a18-30aa-3d72-89c4-dee730920a96 | -5.86079 | -49.77193 | 2026-09-11 04:51:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75501d43-2169-33fd-9142-07c91852e098 | -6.82322 | -58.99298 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16916a02-17de-3b1d-a2a0-db1656dcca70 | -3.9437 | -49.4014 | 2026-09-11 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7878c770-a0fe-3de5-9296-a68556f66876 | -8.38329 | -47.60931 | 2026-09-11 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2608e5cb-6a5d-33f8-acd2-1f79ed661a77 | -2.93624 | -50.48022 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93a8c38f-88e8-3f4d-a073-e5c73e68175c | -7.17828 | -43.6092 | 2026-09-11 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8a66c04-54e0-3044-b966-9f2f660150b1 | -4.3947 | -55.77946 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fce55ad-10dc-3ea5-8745-c0b87b6115af | -6.21544 | -55.56353 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b547f9b9-0f24-3310-b1e4-83510b08f89d | -4.82879 | -55.76404 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66666275-c884-3a67-845c-89837b7d0db5 | -3.54636 | -48.1767 | 2026-09-11 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6954d114-423a-3a64-8d5b-c237ea8736e8 | -7.97008 | -44.0017 | 2026-09-11 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6267a16d-b34c-3de3-b95f-401cecb3609a | -6.19886 | -55.28105 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
