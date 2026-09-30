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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6ae5920-be01-312d-a9f8-ef9cf794d51f | -4.12366 | -46.87535 | 2026-09-30 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cea61580-0f59-3966-aa5c-5f8708576fcd | -7.4565 | -45.79075 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78531b21-2d9e-3d2d-9be3-21e5b0ff5427 | -10.56119 | -50.87063 | 2026-09-30 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50884aba-fd02-3993-9b20-43ca4a87fffe | -7.03056 | -44.29332 | 2026-09-30 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7115af33-59a9-300d-86be-d2901b47f12d | -7.83888 | -45.81509 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 796988cf-0dca-34b9-81e0-035315b145e7 | -4.36172 | -47.77196 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e02d0bae-7fc8-361f-ae15-e5f685f673a6 | -11.62456 | -43.50166 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c74e4c2f-e11d-3ca9-8a82-8cd66049858f | -5.73436 | -43.28217 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c6ad6d0-4e03-3af8-89a0-dde3113de82f | -10.51705 | -45.37285 | 2026-09-30 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 629ec824-f229-340d-87d6-ebe6bbde959e | -4.82024 | -45.63861 | 2026-09-30 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71dea2bd-0668-3f84-8a99-42694f3cceb2 | -10.25793 | -44.59446 | 2026-09-30 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e630807-2ee1-3727-8782-8a774390d710 | -5.8714 | -50.16263 | 2026-09-30 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 67a0e0dd-c1ea-3e77-8249-a5e416693a70 | -10.66287 | -50.74317 | 2026-09-30 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 104e67ab-1f53-34ff-92ad-ed329994bd58 | -9.76732 | -44.82074 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72ed28e1-2473-3d6a-874e-292110464b51 | -7.38296 | -44.78057 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 313c2dae-9659-3fa5-afbe-4468b1c16a48 | -9.77525 | -44.81461 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e6f1ff4-366d-3488-9e19-5b9b7dc5718b | -9.65972 | -40.59068 | 2026-09-30 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 20ca84f3-030c-3a00-936e-f0f9df4791b1 | -5.7372 | -45.16858 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6eab4c9b-f21f-35f9-9e89-6de6b89b935c | -10.05595 | -46.85981 | 2026-09-30 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25ee617d-751e-325a-8fe1-3e5045c0dd16 | -11.1629 | -44.78133 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3676c6ac-0bb0-33ba-abe0-3746090f013c | -11.43625 | -43.42957 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 42749dde-4521-39f0-bc48-ee91eede203d | -6.2136 | -42.51366 | 2026-09-30 03:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 51deaa83-03a5-342a-b267-8556eb3b3605 | -5.76348 | -45.17804 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 91fa4827-ef30-325d-883e-396f0ea8b112 | -5.76424 | -45.17345 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 505daab3-66b5-3e1c-9608-88179d99842a | -8.55847 | -47.78971 | 2026-09-30 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e945704-3e53-3f18-ba6b-a828000c0335 | -10.90541 | -43.85075 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d8e24d6-9091-31cb-834e-ec2483b46fc9 | -11.16883 | -44.81944 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| df489f86-08de-3b1f-9e01-ca8268951039 | -10.56029 | -50.87526 | 2026-09-30 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d8721a2-bf6a-391b-be39-2814a254c126 | -3.91449 | -49.37259 | 2026-09-30 03:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22d26c64-1be6-3d7b-ac84-98a2b3d6d43e | -5.73766 | -45.0565 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 24831ca1-0514-39f1-9100-dc26b60e0e50 | -9.125 | -44.74931 | 2026-09-30 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a64b49e5-d8db-3a56-91c7-1c92c4839e1e | -3.37807 | -50.93822 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9a53d5f7-5723-3d53-aca5-41662806deac | -11.17695 | -44.82472 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf84d1f1-4def-38a2-9123-af3af0c39543 | -10.29134 | -44.64177 | 2026-09-30 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb197a2b-c146-37b2-ad85-5a16f6ab4528 | -11.22545 | -41.62517 | 2026-09-30 03:55:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6e9b1ed0-b993-38e3-8cab-a3d3a97efcff | -6.71555 | -45.62764 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 684c26ab-866a-30b6-9cad-744cb354cff5 | -11.38179 | -43.46813 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c9ee7b6b-9c94-35a5-a022-0bb42331ce34 | -10.70791 | -50.84002 | 2026-09-30 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e488044-d2e3-368f-8ddb-8ddee65936f1 | -3.38376 | -50.94571 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| eec86bb6-1d94-3ac1-bb47-02be90453cd8 | -7.5059 | -44.54595 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d90454b5-2fed-3c8d-b808-1d5ec759d9e6 | -11.26648 | -43.5287 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 794428f1-6df2-3fd0-841d-805e65abb566 | -6.33463 | -51.16164 | 2026-09-30 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9a9dadcc-df6c-3cee-abb6-c5b983bb3765 | -11.39292 | -43.47002 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f8c9d6d-6b52-3865-b962-19177f7fe383 | -9.65637 | -40.59014 | 2026-09-30 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8f33b386-aa93-3d7c-ae1a-48ee0241e97b | -10.77994 | -47.724 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a778d6c1-aa38-3edf-9e3e-e357d30a8ffb | -7.27349 | -44.30445 | 2026-09-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02c07188-4aba-300d-82d3-c504e06b4fbf | -5.75072 | -45.171 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9ea2c67f-3dde-3efb-8904-51b77259ed92 | -6.72385 | -45.57974 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccab33b0-4a68-3a57-a43b-4f795f21da93 | -7.82434 | -45.8178 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f9012b95-64b7-3c9c-b61b-67db88823f90 | -8.98936 | -44.17511 | 2026-09-30 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf728278-2fd0-3344-803f-8bbdc45163b7 | -7.27105 | -45.3248 | 2026-09-30 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b25da708-3608-3a5b-9c8a-bab911cd9a42 | -8.98416 | -44.18153 | 2026-09-30 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c10c2878-2e11-37fb-b726-beb05f2f115f | -7.5367 | -44.54626 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c4eace4-0396-3cb9-a464-ea0aac9609ec | -11.42628 | -43.4878 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c202d54-fded-3eb5-8fcd-7260bea6c454 | -11.83171 | -44.73834 | 2026-09-30 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28992d9f-df0c-3b7c-9b29-922fc8e35d0f | -3.38319 | -50.94141 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 35635c5d-cf1e-3abe-b127-ab74890675b3 | -3.3821 | -50.94781 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 100d47cd-101e-3cf6-93f5-0f5dcd61195b | -9.9222 | -50.23473 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 289b4c7f-b37f-34a3-8e34-4d921fd72c20 | -5.75897 | -45.17724 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b3dbba5c-fbae-3077-9e9e-53901af60669 | -11.38127 | -43.38057 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed438ea7-d179-30da-b0e0-c8e6b520bd33 | -11.67221 | -44.5158 | 2026-09-30 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c046e967-48d4-3772-b388-1a0d0993a914 | -11.19524 | -44.83899 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3b9219e8-a8ee-3dad-8870-7f5331d7b7cb | -10.72198 | -44.43216 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e1c4f18-8160-3b9a-8a8c-1a463583ee08 | -7.84556 | -45.83105 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ff83f58d-2abf-31fd-b3b4-9700aa8a4d12 | -5.47075 | -44.65714 | 2026-09-30 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24abfbf0-ecb6-30c0-a7b2-e32ed8dee526 | -11.45758 | -43.46092 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88fffed2-e20c-380f-9dc6-992429e70550 | -10.29194 | -44.63829 | 2026-09-30 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5378f698-9078-33ca-a344-ca315f6decc4 | -10.77841 | -47.25392 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 602b30b5-c243-3a58-92f0-6406ffea6ba1 | -6.07774 | -47.28735 | 2026-09-30 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd57e70b-7857-39d6-b3e3-4a4a50338229 | -3.37992 | -50.96057 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 631f4112-7769-3fde-900d-ce112101b94a | -4.31237 | -46.77605 | 2026-09-30 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 018f2e0a-6830-30b1-9364-639a091d57ab | -11.79472 | -44.31673 | 2026-09-30 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efd2e630-22e2-3ccd-8188-eadec4f4b27f | -12.5655 | -43.07213 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 153cdb1c-b140-3d46-8450-130bc4814fb6 | -14.32182 | -44.90408 | 2026-09-30 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae986adf-1f69-3a18-827b-d9023f67ea42 | -16.86719 | -43.92583 | 2026-09-30 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8a21accf-dab1-3454-94b0-da9a9499de50 | -14.12647 | -46.26019 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 84f9988d-4d23-3572-a151-95ae717b7f24 | -15.76017 | -46.04005 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 297f2830-a665-32c5-8d08-7ec4754d0d5b | -12.24366 | -50.25753 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdd32157-f1ff-3b32-87a8-a2a8aaaa81ab | -18.89294 | -43.80229 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 233b6087-62f4-3b3d-99de-87477f4fd40c | -12.25318 | -50.25586 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c352ea09-0ed1-37e5-80b6-cfe541418b02 | -18.89566 | -43.80717 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a9db541e-14fe-3058-b7da-0ab5ef121531 | -13.0732 | -43.28227 | 2026-09-30 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 88fc3bdd-7fb5-389f-a83c-12c1cf192ca7 | -19.53534 | -42.94368 | 2026-09-30 03:57:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 36f42eba-b926-3291-92ec-ad9426b92094 | -15.99763 | -48.0144 | 2026-09-30 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 635b617c-162b-3af5-981c-b9e07a0998cc | -17.90984 | -45.05304 | 2026-09-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7057e52-1d17-3afb-a2d9-7f1c380fe0d1 | -15.63628 | -43.27291 | 2026-09-30 03:57:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bfe6fff9-3f80-3b1b-a46f-782de0176001 | -13.38199 | -46.82991 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f6dce3ac-ce0e-3c8d-b43a-e267a4c2472c | -13.36881 | -46.82684 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a094d6f-3246-3331-ab26-e3d2ba7bff20 | -12.2434 | -50.24565 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14f696ba-9b25-3b28-bd4a-acbcbf754ce0 | -17.3414 | -47.06623 | 2026-09-30 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82528b65-633f-3212-9344-ef98f0cee923 | -16.10597 | -39.08276 | 2026-09-30 03:57:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 606a7959-20b5-364b-9cd7-ffa228f8c4aa | -12.79322 | -54.00554 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19e52568-ecfe-3743-9000-72e10d8534c7 | -19.38783 | -44.70563 | 2026-09-30 03:57:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af9950e6-c102-344b-813c-d8769bdb72d6 | -12.24932 | -50.25865 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98ade051-19c9-3374-bc88-c76da2c0d8b3 | -13.89999 | -43.93009 | 2026-09-30 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f966391c-4e39-3452-8e1f-b148018fe1dc | -14.10242 | -46.2725 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9be85f90-3bec-30bf-8c44-cb8f18577332 | -12.26723 | -50.28694 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c58405a-bfc1-32d4-b59a-ffeed3737f47 | -12.24905 | -50.24679 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3cc3bf5d-fc9d-3380-9051-f2e1947b31ab | -14.12469 | -46.29391 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad54d006-f391-34a4-9992-9c287661d1bd | -12.51314 | -43.08598 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README17.md)
