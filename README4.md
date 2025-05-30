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
| 85533a2c-d624-3918-b61c-1ebebd3c3d25 | -4.48593 | -47.79267 | 2025-05-30 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 205a9ab9-9399-3160-899b-a5bc29a8d270 | -4.46798 | -41.61237 | 2025-05-30 03:51:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d993d53-848f-3615-b0f0-35844059eda6 | -5.76625 | -43.48211 | 2025-05-30 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c7460d8-abb7-3774-b9c1-c3111fddd651 | -4.97924 | -38.5996 | 2025-05-30 03:51:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f8bd6f73-4baa-3e73-b628-fa7297a387b9 | -3.9578 | -41.48178 | 2025-05-30 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73ba886b-04da-3f23-82ae-8de2c245d52d | -4.89405 | -37.52452 | 2025-05-30 03:51:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd1d4f09-fc94-3eab-aeca-1859a147a869 | -4.53932 | -38.03104 | 2025-05-30 03:51:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1066b87c-86dc-3ff7-aae5-418ef1cc5c0b | -4.25011 | -47.58104 | 2025-05-30 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5a33030-c2fd-3f08-acf0-63627bf5ffe4 | -5.30051 | -43.0689 | 2025-05-30 03:51:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a91d0a0b-3174-3fea-99f5-65e3eea8fffc | -4.89351 | -37.52798 | 2025-05-30 03:51:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 4704ebbb-56c3-30ce-aeae-7927dcc0f576 | -4.24949 | -47.58457 | 2025-05-30 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6de36f4b-92e9-38c9-b307-bfb85a3f1398 | -4.25102 | -47.58188 | 2025-05-30 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 462ac2b8-e955-3015-b241-a887afa322b4 | -5.7663 | -38.90642 | 2025-05-30 03:51:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ffdcb6fa-a944-3322-9c65-2c52fac6e893 | -6.34141 | -43.38458 | 2025-05-30 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb93299e-ecef-3c13-802d-2501a2ec6359 | -6.34545 | -43.38523 | 2025-05-30 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22140929-d509-339b-8240-fbca1766dbc5 | -6.24349 | -43.3715 | 2025-05-30 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 31532ebd-c2f5-3e1e-8e7d-3427f5da9ca6 | -3.95852 | -41.47733 | 2025-05-30 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe7e20a0-154d-3083-b3ea-256ba20f1e21 | -4.82136 | -44.35543 | 2025-05-30 03:51:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8788dada-5f1a-3c9c-8f28-a0c86be02777 | -6.34603 | -43.38171 | 2025-05-30 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 721aee9d-b486-3183-848c-4f1a7373874a | -5.30453 | -43.06955 | 2025-05-30 03:51:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf6776c4-4baf-302a-bf81-3d10712be8cc | -5.58714 | -43.5742 | 2025-05-30 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00a5a97e-9b1b-3a6e-9b15-61a3b07cfd90 | -8.1965 | -49.81429 | 2025-05-30 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dfd50060-d358-3eae-8041-749fadac703b | -11.79588 | -44.2828 | 2025-05-30 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c94e640-4800-3b80-9e5e-a23ddca39a4e | -7.08377 | -46.04731 | 2025-05-30 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f19247c-ddab-3350-b3a0-341b8932c4f4 | -7.18722 | -43.10691 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08df140f-0878-3a24-9471-08fb32f819a0 | -6.60403 | -44.73225 | 2025-05-30 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31b1f541-dafb-3bc3-8f75-ccaf9b4306c7 | -7.18331 | -43.10622 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 1d85f9b5-a7e9-3976-ae4b-7fb42c1e2e0d | -7.95535 | -46.18119 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e1a3d34-8cbb-3970-84e3-ab083b9db512 | -8.6268 | -45.3412 | 2025-05-30 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 070cbbbe-f509-3b0e-bb14-70e4d57b732d | -9.60332 | -49.02705 | 2025-05-30 03:53:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40b03c56-e304-3ed1-a984-36f85273d499 | -9.19517 | -49.46621 | 2025-05-30 03:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 552de540-8c96-37e3-8e09-9b2d6339065b | -8.9054 | -44.77657 | 2025-05-30 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 378f2179-08f6-3b6c-b3d5-1eb2ad116139 | -7.18695 | -43.11006 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dcc1ce3d-99ea-3d86-8857-3cb9f9378480 | -11.80283 | -47.37893 | 2025-05-30 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14f0ec9a-3b39-32f1-94ae-43f139ea59df | -9.60559 | -49.0244 | 2025-05-30 03:53:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 886c2c8a-6acf-3724-8c80-4389e969d1aa | -9.85104 | -48.15049 | 2025-05-30 03:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f261a24-65ae-37f2-9090-6e6237f72d80 | -11.81248 | -44.28053 | 2025-05-30 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b10fa614-7477-3bf4-83a2-caa978dd33ba | -7.68834 | -46.86377 | 2025-05-30 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac56bcde-7c48-3d61-a78e-c0a9b09089a7 | -7.23755 | -43.09492 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9e0a0f31-a491-3d96-be7d-eed4fbd9a993 | -7.27726 | -44.22333 | 2025-05-30 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d3265d2-6b02-30da-b9ec-e98bf5c1170e | -7.18248 | -39.2931 | 2025-05-30 03:53:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 58d6d26b-16e7-3045-a1e0-d9a319ea0518 | -7.58839 | -45.94844 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fff8d8e2-8bcf-30b9-b878-beb8a39fa6c8 | -7.70069 | -49.39376 | 2025-05-30 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40b98986-0237-35cb-a4b5-811ff703bf20 | -6.98272 | -46.31361 | 2025-05-30 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f613ad24-e0ef-3eb8-9084-3a50a3b07ad5 | -11.57117 | -47.4585 | 2025-05-30 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 325aa4ce-ff94-31c9-866f-0cf68dff378a | -11.79499 | -44.2879 | 2025-05-30 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 248bc35d-5350-3ec3-9a09-a0ae4f96e4a1 | -7.68784 | -46.86666 | 2025-05-30 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dbcfde8-126d-379b-9619-93edea3eff1a | -6.63223 | -47.34518 | 2025-05-30 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb1e33b8-8b23-3963-9198-8ff5efae6dc9 | -7.96766 | -45.94131 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1dc9ba8-1933-311c-8ae8-e77bf178befe | -7.24454 | -43.10122 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 40bf1c41-9ecf-38ed-9dfe-e3319dddf891 | -7.63756 | -46.11716 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3001373-41a3-3b97-857a-854c6ec15157 | -7.58751 | -45.95345 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5236bc6-be1b-336f-b8c7-178fa806f6d8 | -9.84122 | -44.68497 | 2025-05-30 03:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5833fa39-949d-3b07-a17a-1dcdecd4d935 | -7.58173 | -45.86441 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e28c230-3a38-3d22-92f4-a0354ed3155d | -7.94801 | -46.19786 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bccc4913-4b29-3bbe-9f8c-19b2d167bfd1 | -7.5838 | -45.86533 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c8f46e1-fe2d-34d3-bfd8-c16d69aaa7af | -11.56145 | -47.45673 | 2025-05-30 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6f4b4fc-3d24-3bb6-81bc-e990a5b448e2 | -7.96178 | -46.17218 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b51b138-215d-3323-b50e-8797dcfb3448 | -7.49267 | -43.1338 | 2025-05-30 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51709c08-3cc3-3dc8-a9d8-eb3ebc364717 | -7.55096 | -43.31422 | 2025-05-30 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 674151d5-8484-3a69-bf7c-afc14d732a9a | -7.22861 | -43.26957 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3fcc0b6-7228-3557-a53d-d1bad25e5ded | -7.23364 | -43.09424 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41d643a6-e978-32aa-9946-837e06c01f26 | -6.75514 | -44.93532 | 2025-05-30 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 779ab67d-90c1-33f7-9da9-fc6a793d479b | -9.40226 | -40.36529 | 2025-05-30 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| d808a1d2-7629-3965-af32-758804a443c9 | -7.18384 | -43.10442 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d54b9f7b-f292-371b-b7eb-3546dff1b0fe | -9.25377 | -48.86533 | 2025-05-30 03:53:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f648707b-a041-3ab9-88e1-196bb2a8bfc9 | -6.63165 | -47.34846 | 2025-05-30 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d97c27f9-ea5e-3e2d-8cfe-5bf3da0d9f2f | -6.60329 | -44.73653 | 2025-05-30 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fae6f2d-a5c0-3fb0-a198-83df47f24b7f | -7.62325 | -45.75086 | 2025-05-30 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d924535e-4019-37ed-9d1d-005617a322d6 | -10.66897 | -44.41236 | 2025-05-30 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85d397e9-1499-3225-9910-dabbf0daee4f | -7.6082 | -46.64737 | 2025-05-30 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6d7a583-5616-3e40-93fa-66b498612567 | -7.33043 | -43.70962 | 2025-05-30 03:53:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 625296e2-1402-3200-9753-0cf36c0a579a | -8.78719 | -47.94071 | 2025-05-30 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a7825ef-879e-3cf4-9441-47f8e00e8f96 | -7.69282 | -46.86759 | 2025-05-30 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bba1497-6b6e-3754-99eb-a40b51e1385c | -8.542 | -46.42837 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 628aa618-fc61-3278-ba22-f8a3869f1d34 | -7.23837 | -43.08997 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 001165b7-be85-341f-98a4-95701925909d | -7.9668 | -45.94628 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cef91d4-dffc-311e-af0b-17af815acb00 | -11.45566 | -49.10089 | 2025-05-30 03:53:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e93245c5-0618-3692-ab45-93a6ef4f82f4 | -9.39574 | -48.41337 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8da6ccc1-b1a0-3381-9673-61624e5ab0a2 | -7.07386 | -44.91795 | 2025-05-30 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9ba6c15-01f0-38f5-994d-e16d44bc1bfe | -10.66495 | -44.41162 | 2025-05-30 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 133f937c-7992-319f-8456-af5814417a8e | -7.49658 | -43.13444 | 2025-05-30 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6359b7fc-1f2d-35f4-8a07-483db05b6774 | -7.51697 | -43.13262 | 2025-05-30 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 323f3aa7-6207-3917-a433-90ac521d7f47 | -7.49657 | -43.13281 | 2025-05-30 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a9b8e2c5-0066-3822-b3f2-a7aec18d4487 | -7.957 | -46.17162 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1572ffab-f7e4-3d48-9d94-926d3d2b4f5a | -11.79802 | -47.37802 | 2025-05-30 03:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 31509a92-d6a2-348e-bd78-3396ff725b3b | -6.8257 | -44.6525 | 2025-05-30 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd1de7aa-7462-36ca-8f16-0e5360bb63c4 | -9.55713 | -37.16461 | 2025-05-30 03:53:00 | NOAA-20 | OLHO D'ÁGUA DAS FLORES | ALAGOAS | Brasil | 2705705 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1e357aad-0d23-37dc-bcfd-6155933ba5f4 | -10.45446 | -47.95248 | 2025-05-30 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 202787a6-4947-3dea-88ff-af0bbc902f29 | -7.96212 | -46.1738 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e057e103-4cc7-34be-a476-32a8c0c11b1f | -6.83047 | -44.91457 | 2025-05-30 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d024702-f97a-3c4c-ba43-a20b0cb19534 | -7.57705 | -45.86362 | 2025-05-30 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c6e78a9-0387-33ff-9e02-4c4f283f62f1 | -9.39382 | -48.42356 | 2025-05-30 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a19e04d0-a0b1-32c3-9952-95337986f270 | -7.61483 | -45.74448 | 2025-05-30 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 821f0672-be85-3475-a730-41a84de329b5 | -7.52954 | -43.32094 | 2025-05-30 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f36659f6-e80e-3fa9-bd77-1ac1e63bef30 | -9.40167 | -40.36891 | 2025-05-30 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74a5f79d-66df-39fb-b144-2c1c780eaa3e | -10.45683 | -47.95188 | 2025-05-30 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8dc0a4f3-dd30-360e-be29-75ae904831af | -7.18303 | -43.10938 | 2025-05-30 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d8415c60-3fb5-3a64-9763-e14bd021feb6 | -9.84581 | -48.14946 | 2025-05-30 03:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f6261bf-df44-3b51-903c-3374b15c6c38 | -9.20095 | -49.46721 | 2025-05-30 03:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README5.md)
