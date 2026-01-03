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
| 8b0a1e37-8cbf-3796-b2cb-318c57ebf2ac | -2.9728 | -49.61863 | 2026-01-03 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a22aa33c-ef2e-3e78-9546-20004560e7c9 | -0.83455 | -48.78087 | 2026-01-03 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12605410-d981-37f5-bcb5-6a70463ee0c0 | -1.93295 | -54.40761 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4c9c2f2-5925-3d3a-b438-3dfe8beb078d | -2.32098 | -44.80217 | 2026-01-03 04:57:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42a11697-a405-3e95-b1d4-d2a5de0590e0 | -5.04561 | -43.6047 | 2026-01-03 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b12e264b-30e8-3015-bf02-f7a78551d411 | -2.58054 | -54.72566 | 2026-01-03 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4452de02-1f0c-38da-abcb-e3c279361f38 | -0.73754 | -52.42168 | 2026-01-03 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 581f34f8-9295-3314-80f6-a52021285ace | -2.38928 | -56.05263 | 2026-01-03 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20e4ac40-74b9-39e4-abf7-00729b870e68 | -5.32468 | -43.56033 | 2026-01-03 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24df74b1-9703-3aae-bc58-067720679acf | -0.80221 | -48.76119 | 2026-01-03 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf2e13bb-204d-315b-94bc-f9beb206e1de | -3.84153 | -50.0202 | 2026-01-03 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d64222f-5e66-3dfa-8b31-341f0b408081 | -1.67197 | -53.92727 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 050823b8-d5e8-353f-bfd0-5f6524d8ba32 | -5.49232 | -45.41073 | 2026-01-03 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe275b92-a1aa-3e7d-9e95-e3de01019fdd | -3.35121 | -53.34987 | 2026-01-03 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5203d2b-f309-38e2-8136-5d239d29ef11 | -1.85007 | -54.35154 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a89ae38-79cf-3603-942e-b0d70a90c47f | -2.94769 | -39.92431 | 2026-01-03 04:57:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7b76b99a-9dc1-3adf-b9ee-fd04b0a906be | -1.45407 | -53.51532 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6ac5bdd-7cb7-3239-8de7-c0549e1621c0 | -2.72122 | -54.54565 | 2026-01-03 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b232f6c-e2f7-36db-976c-29da01eca92b | -3.53915 | -54.16861 | 2026-01-03 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b8662c9-48c9-3008-a442-706d3ae95cbe | 0.46572 | -60.43904 | 2026-01-03 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5d1c1a23-c64f-30d5-b210-196f36117214 | -2.44844 | -53.9438 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c40ba96-33b2-305a-a583-d29caaa29c41 | -2.07571 | -54.2582 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 613b546b-df4e-38a7-a9f2-2317407c050f | -1.51304 | -53.72582 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5300fc5f-d89b-32a2-8b9c-9ff8bf847994 | -4.17684 | -43.62542 | 2026-01-03 04:57:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d61a13d3-f531-348f-ac4d-b80f02e3874d | -2.42613 | -49.31316 | 2026-01-03 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07b3c5b6-74d8-3e80-b69c-8f0d057eecd9 | -3.70252 | -52.00355 | 2026-01-03 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5bd9542-50a5-3e61-81c1-4777b74e2a09 | -3.18635 | -51.1014 | 2026-01-03 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 979e94d6-289b-3e3b-bd61-857a6e0ee270 | -4.75765 | -46.713 | 2026-01-03 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c001a77d-3483-3eec-a5d0-e659530eb8f3 | -2.10384 | -53.49455 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f17effea-1aa8-3252-9120-f38981bf3cb4 | -1.6692 | -53.92331 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66857ad5-b678-303b-a9f8-f6c97f8fd77f | 0.46559 | -60.44269 | 2026-01-03 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eff2e4ba-cea2-3dd1-9b0d-0ed16c4c341c | -1.11943 | -47.74319 | 2026-01-03 04:57:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c518be7-6b8b-314d-98c7-9694b26bbe3d | -1.96532 | -53.36055 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b39c58e8-b75b-3571-83ec-7cae1d4b0b1d | -3.16979 | -54.97832 | 2026-01-03 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6dda3e9-17e3-3fba-bc03-9ad7d97537fe | -3.17036 | -54.97473 | 2026-01-03 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d8863a4-d8d1-3b79-ac1c-507ac52e9c01 | -5.3241 | -43.5645 | 2026-01-03 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8f578bf-20e2-3687-9b42-1cb2327b6aaf | -1.45461 | -53.51189 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc38bdd4-0774-31d1-b299-73133d8e7cf1 | -2.90033 | -54.1633 | 2026-01-03 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfb7ed47-1dc0-3797-aa95-08b99d32266c | -2.91678 | -54.12334 | 2026-01-03 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d160754b-50eb-33a8-8058-52e17239ce87 | -5.28404 | -45.83172 | 2026-01-03 04:57:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 195cba29-1421-3292-8215-f9df686d9e67 | -4.17628 | -43.62948 | 2026-01-03 04:57:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4425d95-b109-3135-adfb-2f381e9f41c7 | -0.80296 | -48.75642 | 2026-01-03 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec91db0e-7f9f-3662-852d-7e9becc4dccf | -3.02438 | -50.51233 | 2026-01-03 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9e28d4c-093d-348a-b45b-9138d1f08a5a | -4.25006 | -46.78775 | 2026-01-03 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 886f9bbd-edff-35f2-99f1-b83aecafd71b | -2.86078 | -52.80977 | 2026-01-03 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c1ae7b4-d9f7-3823-bab9-1252ba1cc6d3 | -1.69099 | -54.04382 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| afd98e33-ccd6-3fca-b93f-0360544007d7 | -2.08371 | -53.5582 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5285c7bd-f0c5-3c40-8592-8e8cb7e0dbf6 | -1.26569 | -53.47898 | 2026-01-03 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee0a94b5-3924-30db-a73c-a7a222a1e116 | -4.28143 | -48.25315 | 2026-01-03 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43429528-83a2-332c-8390-1c88ab59b26b | -3.49842 | -53.45428 | 2026-01-03 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 684e061f-e939-3178-ae5e-16c17b0b607d | -5.0466 | -43.59795 | 2026-01-03 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8fc5efe8-6d18-38c0-ad77-f512a2215c16 | -2.97534 | -49.6218 | 2026-01-03 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1011ef96-39e3-3c8a-a6a0-86314546e3f5 | -0.60884 | -52.41881 | 2026-01-03 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9911c00-e6b3-370f-a583-882dfde81c7e | -2.97158 | -49.62123 | 2026-01-03 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2a85e96-4437-381e-8fe3-3fb7e0f256e1 | -0.83639 | -48.78313 | 2026-01-03 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c27155a-0654-301a-b845-2603aad156cf | -2.97212 | -49.62317 | 2026-01-03 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72750c6c-f624-3ee6-a7f5-8247ec7f644a | -1.67251 | -53.92382 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da54730b-8baa-3d1c-a988-d3ee32c067fb | 0.46479 | -60.43741 | 2026-01-03 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db79e535-4aeb-3391-aa35-f5f69d784a47 | -2.26378 | -46.48106 | 2026-01-03 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5602901a-f26f-322a-b54a-1c216e9e219c | -13.48116 | -44.0166 | 2026-01-03 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b5a9c37-f1b4-3d4c-bd28-4a9ad2f0e342 | -16.02312 | -52.21336 | 2026-01-03 05:01:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21213de3-2754-3bde-bb19-7351899b9a6f | -26.85886 | -49.26036 | 2026-01-03 05:03:00 | NOAA-21 | TIMBÓ | SANTA CATARINA | Brasil | 4218202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9b455607-a895-35d4-938d-5055771f1cc5 | -26.85771 | -49.25821 | 2026-01-03 05:03:00 | NOAA-21 | TIMBÓ | SANTA CATARINA | Brasil | 4218202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 778adb98-99dc-3196-9303-4f4495fa159d | -26.85918 | -49.25673 | 2026-01-03 05:03:00 | NOAA-21 | TIMBÓ | SANTA CATARINA | Brasil | 4218202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04071d4e-fba5-306a-825f-13054c1bf217 | 1.28186 | -60.32692 | 2026-01-03 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bd22b589-89f8-3497-9bd2-540274731dd3 | 0.46451 | -60.43859 | 2026-01-03 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5dfa9111-4450-3c18-a21b-ae5877a9702e | 0.92219 | -60.43394 | 2026-01-03 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e050e96-da2c-3026-9086-06593aff234f | 1.07334 | -59.69117 | 2026-01-03 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66e0c0d8-6216-39e5-a47c-b1e00905987d | -1.28201 | -54.55437 | 2026-01-03 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56c47b84-561b-3e30-abaa-55ab0f9a8559 | 0.93627 | -60.47958 | 2026-01-03 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a9d5da1-a5f9-318b-b648-6e4957933d25 | 3.11196 | -60.97757 | 2026-01-03 05:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3a25fa9-10b8-313b-8d3b-851bcfcbf935 | 1.28524 | -60.3264 | 2026-01-03 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e24bf953-2fb4-38fe-91ef-501ffbc7ee99 | 2.52282 | -60.9865 | 2026-01-03 05:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8985e63b-adc2-3f1e-b507-271ed0d88172 | 1.28242 | -60.33051 | 2026-01-03 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 11ecb84e-9d62-33ec-8ca7-ffe2df5e86d9 | -0.08863 | -51.28044 | 2026-01-03 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b3b346dc-6b65-3d3f-bf3e-8a6374bbb41c | 0.46508 | -60.44215 | 2026-01-03 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ddd12146-1766-38ba-b886-769f6d20e88b | -0.60696 | -52.41972 | 2026-01-03 05:25:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d180c578-be2b-3aa0-96a1-4fdc2c748796 | 2.55821 | -60.36068 | 2026-01-03 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d90855b6-3f52-365a-a4ce-bd0614d0009b | 0.68274 | -59.55721 | 2026-01-03 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf8147b3-8658-3d7d-9430-87b73d30b02c | 2.54797 | -60.36224 | 2026-01-03 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 229a7fc2-21f1-34ed-b16c-a59fc50ba3f5 | 2.55195 | -60.36538 | 2026-01-03 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f38dbf42-a407-32e8-b2b9-2e6529edbefa | 4.3386 | -60.7976 | 2026-01-03 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bafd31a-50fb-3793-9640-b0ebffbf81ac | 2.52341 | -60.99033 | 2026-01-03 05:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc104fe6-898c-3139-8d8a-1aa86c91414c | -1.18277 | -53.78675 | 2026-01-03 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c0d8cf6-50d3-3639-ad35-276b8a93f9c0 | -1.26334 | -53.48079 | 2026-01-03 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcadfc8b-c3c0-3a8d-92a3-cdd19740e790 | 1.28129 | -60.32334 | 2026-01-03 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 07854367-0763-39a7-b892-67de2bcf3be1 | 4.20798 | -60.55595 | 2026-01-03 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb3cddef-1b58-38e3-8ee3-96f06bbe34cf | 3.13384 | -60.71968 | 2026-01-03 05:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 369fea53-7ae2-35f1-a8fe-36e1f239b7ad | -1.17917 | -53.78199 | 2026-01-03 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bc4593b-6509-314e-9748-0fdd06a9a9ec | 2.5548 | -60.36121 | 2026-01-03 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67946a72-a631-3f27-ae6a-ee0a90917f3f | 4.34152 | -60.79309 | 2026-01-03 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4791d50-e034-3775-8a2a-63a36d735c9d | 3.13037 | -60.72022 | 2026-01-03 05:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0ad208c-3bb2-3645-929d-27296aae48f0 | 1.2858 | -60.32998 | 2026-01-03 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a34d45ad-541b-3228-989c-370e4369da54 | 0.62982 | -59.90699 | 2026-01-03 05:25:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51223635-79eb-3fbb-bb06-cc6cafee88c7 | 2.55138 | -60.36173 | 2026-01-03 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d13e8f-86e9-31ed-87a1-8b3f03f88a92 | -0.08057 | -60.67672 | 2026-01-03 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc0f5a6d-8820-3846-906f-011dbd4a9fca | -1.84883 | -54.35284 | 2026-01-03 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b8c8745-e7e3-3857-945c-0019b1205ee9 | -3.81466 | -53.72792 | 2026-01-03 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5cb8723-a236-33eb-8792-60287a3bcd14 | -3.81553 | -53.72905 | 2026-01-03 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b92ea52-0b1c-3aca-b65c-1a795444d307 | -1.6904 | -54.04209 | 2026-01-03 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README6.md)
