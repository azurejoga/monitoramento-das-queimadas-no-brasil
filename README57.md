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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe5c3aac-8d65-3074-9966-f2f48e765f18 | -12.19093 | -48.42994 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32626737-cf9f-3995-81aa-fca4a6b538e3 | -11.71571 | -43.4365 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aeee57c6-aa0d-3249-a8e7-8794bf7ca087 | -11.44879 | -43.41945 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0912e232-ca93-378f-a0f6-cae60f3dd7c9 | -11.44673 | -43.43376 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b6d07c4-e53e-3574-af7e-6f179fa5294d | -10.55731 | -50.05253 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ed50886-ae7a-310a-926f-8fb25e51be69 | -11.20749 | -44.84262 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c71e87f3-6def-37b1-8d1b-cb7a0ebc7c06 | -11.44497 | -43.41889 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 18aa495c-b41a-3d24-8498-ec2262eee9a1 | -11.72636 | -50.41432 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0494a1b1-d82a-3276-9332-597334325b5b | -8.15783 | -50.66665 | 2026-10-01 04:34:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1687158e-0d1e-3a92-8581-8878dfd447d9 | -10.53511 | -57.78253 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7f2f5f4-44f2-3e24-b6ed-e05c6f275bac | -6.26534 | -51.84358 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28634401-65be-31f1-b17a-678b25f3addd | -7.85433 | -45.82753 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| adfde935-7853-357e-819c-dbaa9418488c | -7.71894 | -54.76105 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 955e023c-0bec-3d8a-9416-982a9da9124d | -12.82116 | -49.6666 | 2026-10-01 04:34:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c6353a9-34e7-3eeb-92fd-188130465213 | -14.55126 | -42.74129 | 2026-10-01 04:34:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39aedceb-022a-3f13-9091-3251e219a5d5 | -11.43107 | -43.40709 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 699b030a-1d5e-327e-acac-871ed69df3d7 | -11.87977 | -40.9683 | 2026-10-01 04:34:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a429322-ae23-32b6-8838-5ae1c57476d3 | -9.31528 | -47.63095 | 2026-10-01 04:34:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ccfeb69-0337-3260-a776-a8defce0056d | -7.50062 | -45.8299 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fb66690-51cb-368c-99eb-a58480b26434 | -11.44849 | -43.44855 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e4c96145-eb9c-3268-9115-029a5744d79b | -12.20025 | -43.83268 | 2026-10-01 04:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d92d38fc-f40f-35fb-9672-617d029c214f | -13.33204 | -43.96064 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb4a3db9-3743-3669-b7e6-af176994d4cb | -11.44429 | -43.42366 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9a23011a-41c7-3989-b786-22c079a43888 | -12.77182 | -54.00549 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfe1548b-903f-3ae9-9b5b-4c1b201610e4 | -11.71676 | -43.43937 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e72f366-0584-38ed-ab33-a406a558cef6 | -6.14503 | -53.06183 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a94b456-47a7-3724-9ec6-09e12e6746ae | -11.78982 | -50.51285 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 78fc4746-fe9b-318b-9e49-6da5d78c37a7 | -6.14344 | -53.25763 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4d17a4d-1cd5-3723-8318-c2cf14510daa | -11.26297 | -54.81681 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1528caf-1150-301a-b94e-7ac2a2fe9b49 | -6.13249 | -53.29365 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3fc9d733-0ea8-3fd0-95c0-3a73b801e30b | -9.25191 | -46.76644 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b957542a-38ba-33f5-8ad5-1a12548d573d | -12.18761 | -48.42939 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e7cfd631-43d9-3bca-a552-1c522383e777 | -7.54694 | -55.02969 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81b8d84d-b571-314f-b2eb-30d26c89d4a7 | -11.42589 | -43.41606 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cca15ddc-7178-3bc1-8796-e9ac47ece73c | -13.37801 | -46.81216 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a549912c-92f1-3af8-b2fb-58f55f43615d | -10.5586 | -50.87878 | 2026-10-01 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d83f26a1-570e-33bf-b64e-806c65f0d67c | -8.84584 | -49.7043 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c54637dc-088f-3fb4-b18e-16fec9035b24 | -13.77619 | -43.22433 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c9327108-ba3d-39ce-b265-db3ce233b1b9 | -6.07756 | -53.31073 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 060cff92-dce1-3682-9f35-eaf1e9ac0d98 | -9.34943 | -57.1774 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3711bfb2-604d-3dca-8eef-24ee1d499830 | -7.54587 | -55.03558 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64fcb7e4-b175-3c09-baa8-cd45ceb4b69e | -11.7969 | -50.51408 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8052c47d-d22f-3922-a0a2-5e181f983dd6 | -10.76606 | -47.71571 | 2026-10-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1490b9ab-0d75-395d-b466-492a79df8781 | -12.69826 | -54.06836 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a75c24ed-6fe0-3bf3-8ce9-c9b34768b9ed | -6.10057 | -53.093 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bdb7eb1-4d08-3cf0-8083-c38b5b69d12a | -8.24428 | -45.43841 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a9bf712-2400-36c6-90c4-d0f9d7e07934 | -10.56083 | -50.05313 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bd0b2ce-06a0-32a8-b8f3-099ddd68400f | -7.71291 | -54.79453 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 584d53c6-d2cc-3740-b66f-b8803d2dee2c | -13.37269 | -46.83492 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 035b19fc-6c93-37d5-8746-248652f25d0b | -8.7635 | -44.91242 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12286b97-c472-3b9c-a921-37d0f13fe76f | -13.53726 | -49.16481 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2d3585c-a527-31c8-8ce0-f22c04d37426 | -7.49556 | -45.79674 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48108656-59bc-3568-9e3f-15b39f0a89c8 | -5.85379 | -57.76387 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87f2514a-b051-354a-afc5-5414cd7fe9dd | -7.48809 | -54.98465 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a4cd08a-fc88-3209-b597-79d5b6e8933e | -8.36849 | -45.38316 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f054d29-e4a3-3e9b-a821-72098ea25116 | -11.17734 | -45.118 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e11a1e58-09b7-3485-9be2-559b37d33790 | -10.54655 | -50.03021 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8d40621-ffc6-3fa5-9cdc-d290c76c6f56 | -8.62234 | -45.3769 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd3744c1-b25d-3fb9-b29e-3b7915a5c366 | -10.84395 | -48.71007 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2828376-d5a8-3950-b28d-cc0bfa30e84b | -14.36958 | -44.78093 | 2026-10-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 957236dd-d240-3127-865a-f18b86201e5a | -7.48656 | -54.99323 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee4d7ce8-9084-38d6-8ad7-2c6436dd4054 | -7.82431 | -45.82278 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ab1f377-6761-32ae-9a5b-ef48656fbfd0 | -11.38973 | -43.4032 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2577346-1c31-31b6-b625-0d8a3d54ff26 | -10.55446 | -50.04794 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe62dd1b-e742-38fa-b0ef-832d75409760 | -10.45642 | -46.77189 | 2026-10-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4bd12b47-21a0-3438-8770-11a83050b519 | -8.15296 | -54.81177 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d889a9ff-8924-338d-9a87-ebe43a07bdff | -10.51231 | -45.37782 | 2026-10-01 04:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29c73c2a-6670-3770-b158-c987fcd63a5f | -9.86783 | -44.93843 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13549a96-24ac-3da2-b652-5276dffc69cc | -11.20039 | -45.20168 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c399e21f-b2dc-3cff-b817-5d6c07d2739a | -11.72704 | -50.41029 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9598da7c-1aa0-3a6f-a2e3-976c0126fd88 | -14.37324 | -44.7815 | 2026-10-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7af71049-aeb6-3a01-a4e1-cdac501a393a | -11.20808 | -45.15081 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 230c6ddf-a127-35fc-a7ef-94ba7269592d | -7.49596 | -54.99842 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55338173-4b8e-33f1-8b61-56162c5520c8 | -8.62346 | -45.36962 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69ec39bc-3441-3649-b308-cec332b6383b | -11.17269 | -44.8092 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc460aae-7483-32e6-8bc4-1f94cec04629 | -9.07606 | -44.99755 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2215f0ed-0997-390f-869b-a2b32dee2856 | -7.194 | -46.54847 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55a43db6-ada8-3836-a567-1faf9fcaddd4 | -9.90286 | -50.17019 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2522d972-bf59-3e53-afb7-256d0f7e66a6 | -7.81023 | -49.8492 | 2026-10-01 04:34:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6fdaf7c3-c130-32a2-9712-f4ed3d465343 | -7.46999 | -45.78545 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82dde59f-a5b0-3796-9cdc-d07d3d170244 | -10.56226 | -50.87942 | 2026-10-01 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 560666f6-f176-3f6f-81be-779e2814a964 | -15.60134 | -38.98661 | 2026-10-01 04:34:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| defb9eab-a450-315a-8063-e44d972f65aa | -10.51171 | -45.38173 | 2026-10-01 04:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbbd0d23-8f80-3900-abb1-ba967558d93b | -8.62461 | -45.3847 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd820ef9-0176-34e4-8720-132bd11d2806 | -14.36654 | -44.77596 | 2026-10-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e72bd5e5-689f-3d6d-b4d1-568e29b492c4 | -7.48758 | -54.9875 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc15b2b0-9e16-3109-9ffa-ff8162534bc8 | -13.16882 | -48.51852 | 2026-10-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adbc5df0-e8b7-34c4-be4e-76e236bd5e38 | -8.39864 | -50.76234 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cba3fd4d-8445-3855-9fef-56c5792d3e07 | -14.14528 | -46.24542 | 2026-10-01 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b060f0a-51a9-3513-b921-33aa1b454a19 | -11.40524 | -42.29577 | 2026-10-01 04:34:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 805a8a63-20be-3ab9-b4cb-9ea24b3ecbb9 | -5.86405 | -53.49078 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a28e0970-8af1-357c-b04f-01e31c336007 | -10.20199 | -49.96656 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0d39abe-f842-3478-b1e1-a55a505dd0ad | -11.41893 | -43.41016 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78225450-2d59-3421-851d-009f97245d99 | -11.46374 | -43.45077 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91bcc5e3-520f-366e-a751-60f1cceb8335 | -7.49215 | -44.96134 | 2026-10-01 04:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd2b5c06-9980-3b40-90d8-76eb3b086055 | -8.12613 | -43.5283 | 2026-10-01 04:34:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9aef7e7-e4a7-37aa-b2eb-5748d4f402c5 | -6.13168 | -53.2983 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d11dec2c-eff7-3f61-aa47-15e667e0d480 | -15.60318 | -38.98739 | 2026-10-01 04:34:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0d17b4d6-9688-3f0c-a928-a63369249a20 | -9.12522 | -49.92217 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8d375a2-cdcc-326f-a895-dd2a216f86fd | -8.01684 | -47.46384 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README58.md)
