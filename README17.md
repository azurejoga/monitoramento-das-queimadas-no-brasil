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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9729a7b1-bd17-36f6-ab6b-5f2122bb8848 | -8.90875 | -60.57668 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 963a8e03-d792-3330-af93-942edf310e4d | -5.87244 | -57.75201 | 2025-08-07 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9c7f465-eaa1-3371-bdbb-c89ae85dc788 | -9.10992 | -48.90363 | 2025-08-07 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d63086a0-5b71-3e4f-a676-b18f1d9f9422 | -8.92337 | -60.56762 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cc22565-f15f-3946-b1c3-a7f57466b7fe | -4.03296 | -48.06849 | 2025-08-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 043d101c-2da2-3ad1-8416-e0f39c8f0173 | -9.46118 | -40.38361 | 2025-08-07 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| e2823547-9aa9-394e-8651-6674d69b9aae | -8.90769 | -60.575 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca1e9c31-92fd-3559-8c32-8b7f22931531 | -8.92191 | -60.6024 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc62bd7-f060-3e95-9172-4566d9819ffc | -8.92218 | -60.73534 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 97373e5e-74da-3019-b026-09573c7f0fa9 | -6.41993 | -53.37119 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2cfda40-45f6-35b0-a6dd-a9676834a972 | -4.02603 | -48.0626 | 2025-08-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a200009-efaa-34ec-b888-909ec15e5e81 | -8.90834 | -60.55145 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 36b77732-d6e5-367a-b616-2db4bbe40a5a | -10.44376 | -44.40179 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fead1caf-3327-36ea-8424-e2503dd9c3df | -10.43595 | -44.3768 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4128f8f6-7da9-3fa1-a5d3-385575e5c338 | -8.90411 | -60.57588 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 442e223b-83f5-3a50-b7dd-1963d7a594cf | -6.81505 | -42.99959 | 2025-08-07 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e13c124-8949-3029-8eca-263d3e75f60b | -10.478 | -44.39039 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 272ae95d-d474-3a12-91af-9d6962dc17b7 | -8.52178 | -43.29975 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a912cd48-1d71-3505-80c9-55088cda50ca | -8.919 | -60.59193 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa679025-bfe6-3107-beb9-fe410a76957b | -8.90747 | -60.54983 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b407d266-ec54-311c-89fe-f4e624ae8670 | -6.85418 | -44.30484 | 2025-08-07 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f71d17a2-47d7-3eda-a7cf-60bc900ede05 | -8.52284 | -43.30666 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 80b3d248-17c4-3888-9bbf-37243731f8b7 | -6.84002 | -46.39711 | 2025-08-07 04:51:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85ea6a1e-3eb5-3624-a1de-52e9735f54ab | -7.40752 | -60.01315 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| cc7adbba-42fd-3f10-a668-733ab2b507fa | -8.90707 | -60.5864 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fd12961-7d5c-36aa-be4b-4ce6bc732f2e | -7.97539 | -55.29969 | 2025-08-07 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2aa87860-3edd-32f3-8ec6-3d7833f455a8 | -8.91719 | -60.58318 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd3cb0ce-cd5f-3423-b767-27348b7af998 | -10.43839 | -44.40105 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6ffcf3f-573a-3fda-9be4-2d88693237fc | -6.4133 | -53.37015 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 760e4726-6f8b-3bd9-8af8-bb19993e1edf | -6.92127 | -52.84057 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a307a7df-bf8f-37a9-a60d-720a1f8d2e63 | -3.88321 | -54.21263 | 2025-08-07 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 393c3cf3-2d22-3e88-ba43-f7ff3a2c7610 | -9.0181 | -51.11857 | 2025-08-07 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6a9afaf-0153-3eb5-8b36-29e5b18405c0 | -9.06982 | -45.05977 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6059557-b195-3b6c-bf3b-ed18ebfe03cf | -7.38229 | -44.25036 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f488cff-eb54-32ce-91ca-c6a6a2d6a174 | -5.40871 | -45.29157 | 2025-08-07 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23fa4bbc-3267-36ca-ade5-cd05556eaf8b | -6.92403 | -52.84454 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc19fe86-75d5-3ab7-8eb3-54a75f95eaae | -8.66008 | -54.71203 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9de0ad96-4fff-3c89-9300-02f16c0dea4b | -7.40377 | -60.00764 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 471af34c-0209-338c-9fb0-441092d12ec0 | -8.977 | -40.61835 | 2025-08-07 04:51:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b90706aa-9824-302e-af5c-4e9bf5b0af6d | -8.91813 | -60.59675 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d272fe49-5a1f-3bf9-8e8d-1134d6913e1f | -8.91382 | -60.54736 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d44b31d-35b3-31a3-afe8-922797d50adb | -8.91088 | -60.59204 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e216ae1d-0c4d-3b2a-89e6-a665b8bfd858 | -8.9054 | -60.59608 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7ea2085-6571-3eeb-830e-8d96920b7ce7 | -8.90419 | -60.59434 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74a4597d-b7d2-3fd0-b605-fa605a0787fe | -7.02993 | -42.55369 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 31b3936b-934c-35b5-91bb-28a0474f24d6 | -8.91571 | -60.74447 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1436558c-6e46-3327-a2aa-58c5ae3d7c91 | -5.88111 | -57.74968 | 2025-08-07 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed07cd51-1ebb-30f8-afa4-d87855ec3679 | -8.90919 | -60.54657 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d2ecf1be-8bc3-32ea-bebb-a9757785fb5e | -7.24173 | -44.64145 | 2025-08-07 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 332ac393-52f9-38c8-8561-4c8b0a1f0e6c | -6.42324 | -53.37172 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b1a349f-ea35-3817-b024-2c93f8b27d62 | -9.64882 | -43.8441 | 2025-08-07 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f88936c8-cd47-3fa6-a932-d30e4d4e5c0e | -8.25039 | -45.07489 | 2025-08-07 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3579bb23-8b48-3980-93e5-c4610fc4e868 | -5.85455 | -45.2204 | 2025-08-07 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a18bb59-985d-3c4a-9339-e6b11b808f52 | -7.1494 | -44.07337 | 2025-08-07 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1e7dde4-6fc4-3db2-ad51-4e7760d8cbb8 | -10.44008 | -44.38751 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f17b9afd-7b57-3688-a1d0-1ec2457725ae | -8.91636 | -60.58803 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b65baad2-18d9-390d-9bbf-41d06c05ef29 | -8.32617 | -55.10911 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b449dcc-e906-39f0-a141-be7638468e25 | -8.51773 | -43.30202 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f82035c7-1bdf-305b-99b5-2412054ef37a | -7.53532 | -45.152 | 2025-08-07 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed211f63-008c-35de-b5bf-cf32872445fb | -8.91122 | -60.5555 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e9a010ce-c31b-3bf2-b6ec-2a58818599a7 | -8.91949 | -60.7504 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 6077fca9-8c04-3a31-8c97-d91589829f48 | -8.92017 | -60.5937 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 587787e9-11f5-314e-8195-2091874a4765 | -10.64003 | -44.75304 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b84b1704-d825-374e-9414-2d80e1f8b21b | -8.91697 | -60.57661 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adf03930-fae2-3c17-a625-33d019581325 | -10.63601 | -44.7426 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c113d8c-2df1-3487-b446-27b726881a40 | -4.2943 | -48.07636 | 2025-08-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13eda85e-7313-3f2d-8930-63e8634bbf11 | -10.63364 | -47.27886 | 2025-08-07 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcb1aac2-e970-3b5e-b250-b63dca14a217 | -8.97319 | -40.62206 | 2025-08-07 04:51:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72b832f1-14e7-33d0-a161-43d8d745bc2e | -10.44501 | -44.39178 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6dfead7-0b2a-38a9-bc8e-8071a1013b29 | -8.51877 | -43.2943 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8492f9f4-40c9-3b56-86b0-beb594d6b599 | -6.41385 | -53.36668 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b2024b-299f-36e7-84a4-0284f84be8fd | -7.33073 | -44.70058 | 2025-08-07 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac62294e-3c74-3cce-994f-2b378c2422d9 | -10.43555 | -44.38003 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0f56929-0a5f-3bbd-923a-b104a2b24871 | -8.92392 | -60.54411 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74544851-94e9-341a-a059-d875098ce867 | -4.1312 | -54.89986 | 2025-08-07 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4bfcf1d-a772-3275-8f8e-c6a3946b5ded | -6.51471 | -56.215 | 2025-08-07 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1b1f4f6-c91a-3368-a31f-3feebbe0e9fe | -9.08069 | -45.05521 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab7e015f-0bf2-36b2-a2bb-7b3f25c4a0e5 | -8.90797 | -60.59997 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15a78569-2830-3715-aa00-219482c1ce72 | -8.91785 | -60.57173 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2067479a-2c11-3289-b6c5-d411dffa1841 | -7.81885 | -46.88494 | 2025-08-07 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1667373-89d9-3a5a-ba0c-72c2831e84b9 | -10.43635 | -44.37361 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d629ac4c-7388-3dba-8ed1-2f0e0ef432da | -2.83684 | -54.89651 | 2025-08-07 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56a89196-4547-357d-bb1f-20c9a69512e1 | -8.91508 | -60.56772 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 023e02af-1d11-3864-a9db-e732902b5124 | -8.92183 | -60.584 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef5f745a-09f5-3fa9-bd2e-98451ba3cc77 | -6.41551 | -53.37763 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| feaec600-1e58-3d7a-94e8-1006597f6ee2 | -9.73249 | -48.30067 | 2025-08-07 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a1b5ade-750e-3ed9-96b0-ae9f5b02017a | -8.90659 | -60.55468 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b71a8f55-6e8f-33f6-a3e7-4263f42159c0 | -8.91469 | -60.59769 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44849274-f8eb-3a26-b12d-e228531844b9 | -6.67702 | -49.79049 | 2025-08-07 04:51:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f4b6476-687d-36eb-96dd-d05540f3d480 | -10.70045 | -48.86943 | 2025-08-07 04:51:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e40d85d3-1d31-3087-b091-e67b1e2359f5 | -8.91845 | -60.54819 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6224858-fb1e-37ea-b128-abc9f842f876 | -8.90884 | -60.59512 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75d699e0-23de-310e-8661-d9e3a23e1e60 | -6.41771 | -53.36372 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4f0a3a5-2d89-30f0-8aa9-0c3c4177b5ba | -9.60287 | -63.46097 | 2025-08-07 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b1df0ce-4268-3f4f-95ba-475eb6d4c6f1 | -11.78131 | -47.5178 | 2025-08-07 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 947e3104-0a52-3d22-ae32-7cfe0dfa4923 | -12.33471 | -46.06581 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab764475-c55e-35b0-b134-c04fada2c1bd | -12.3769 | -47.04419 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dcd32d6d-4312-3287-a4d0-bf084e038b93 | -12.54462 | -47.15575 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05f81e08-0a30-3fa2-bd7b-8d65fd3b5c38 | -12.52698 | -47.14755 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da64f87a-f463-3208-ab47-a2a3b1ae05c3 | -14.35519 | -51.09389 | 2025-08-07 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README18.md)
