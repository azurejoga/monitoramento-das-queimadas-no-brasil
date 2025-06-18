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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37b96a64-ea73-3dec-a00b-6f68d0f33a6a | -11.12994 | -53.93649 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6bd1e9a7-4346-3742-bf3b-c6c1d9e80fe8 | -11.13531 | -53.93734 | 2025-06-18 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9be129d2-2aa4-3e83-9a93-b687fe8c2246 | -11.1379 | -53.9429 | 2025-06-18 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 570e47d0-848b-3937-919c-4cc9a5fc5ed9 | -11.1382 | -53.9223 | 2025-06-18 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 87754c83-2393-3fe0-908e-d95f1a417346 | -11.96648 | -58.7319 | 2025-06-18 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d54c5ee-da31-3033-bf74-7afbd6c0e123 | -12.5271 | -57.21285 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f53da762-07e3-38f3-99de-44b09cc6536c | -11.87494 | -57.0201 | 2025-06-18 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 537b91e8-a71e-365b-a957-f222dd8e6df5 | -11.65042 | -54.13685 | 2025-06-18 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a30c636c-2620-3721-b339-392dd0a9cc91 | -13.7975 | -54.30207 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c63a816f-eccb-3513-9707-6b8cda8dd129 | -13.57927 | -59.2299 | 2025-06-18 05:31:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8b8d993-cb29-3407-9313-5a0cc669d098 | -12.16882 | -56.53889 | 2025-06-18 05:31:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28fe2944-f42c-3d1a-8258-62e6c079f84f | -16.31697 | -58.25149 | 2025-06-18 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fa1a09c0-b453-323f-a9fb-21ca2fce8aee | -12.64522 | -54.12549 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d91436e-99e3-398f-b272-baf2487adf1f | -11.95786 | -58.73602 | 2025-06-18 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90ad1e5f-2a9e-3b65-b814-cc4d9677c5e7 | -12.51414 | -58.35357 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33e3d775-d457-3a28-9d65-fc164214645f | -12.58418 | -56.98074 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d376e8d8-6e40-365b-b915-daf012e2ff44 | -12.17804 | -57.95974 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bed218a8-7919-37dd-bb46-edfa9b95ea84 | -12.22848 | -63.60408 | 2025-06-18 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d3e06f9-507f-3f48-99d7-33ab87c4822a | -14.07448 | -53.38636 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 09bd4ade-f1be-3a75-86ec-7916c100b0b8 | -11.88405 | -54.67388 | 2025-06-18 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7da25372-bbbe-31ba-8b2f-7c1155a4ba7f | -19.00307 | -52.08816 | 2025-06-18 05:31:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| db21937c-0358-375f-8b18-64b8a47bc926 | -12.17339 | -56.5396 | 2025-06-18 05:31:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23193cc6-8498-324f-9d9e-40220e1de6e2 | -12.17344 | -60.67719 | 2025-06-18 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cfebab4e-190c-3665-8e12-ce2f8381d366 | -14.0696 | -53.37724 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f8396ce8-dc21-3622-9194-fc3a3a50ccf5 | -11.64957 | -54.14375 | 2025-06-18 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1303e762-cdb6-34d7-baee-f7900e4cd845 | -12.50957 | -58.35662 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f300cece-fda1-3c09-b66c-bbace60a3e91 | -13.79205 | -54.3014 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b52fd37-2bb2-3d8c-8982-c3714cdea4dc | -12.28015 | -57.27678 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f49ba44-d40f-3945-8027-c26f4591341c | -13.29058 | -57.07403 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0597dcc-f57b-362e-a60c-35fcb16eeff9 | -12.53702 | -57.73468 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d4ce295-3fb6-3b74-88fe-55d3292c92d9 | -12.4316 | -54.86982 | 2025-06-18 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9f12550-d962-328a-80d9-25a0f32f5148 | -12.65023 | -54.12962 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca042d7a-c729-3450-b8ce-efcc2a43b3b4 | -18.99645 | -52.08724 | 2025-06-18 05:31:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 84b51eac-fca1-342d-897b-be92807905b2 | -14.03045 | -55.12576 | 2025-06-18 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4baca102-077d-36cf-aa51-9057ba1aa5a8 | -10.93349 | -56.84436 | 2025-06-18 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 172df1ae-2c93-349e-9e34-5fe64c50def4 | -12.51512 | -58.34628 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5a6993c-ca7b-3e08-a90c-0e0398442a21 | -10.92908 | -56.84374 | 2025-06-18 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73e45902-22af-3094-be72-f423d6dfd2c8 | -11.64916 | -54.14717 | 2025-06-18 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3e58f1f-4015-3bf4-9366-ef12959d4e30 | -12.65777 | -54.11298 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d03f5644-b949-330f-bfb9-9a4eaddd733c | -12.50251 | -55.74274 | 2025-06-18 05:31:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66504774-44bd-3f71-b538-98c30d1b934e | -10.6605 | -59.29284 | 2025-06-18 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8eaeb48c-ccf9-345c-a0d2-85c9b0a942f7 | -14.03006 | -55.12901 | 2025-06-18 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 991a4d0c-5b8b-3b0b-b8fe-5ed85f807db0 | -11.96326 | -58.72618 | 2025-06-18 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 686dd250-1be4-3740-8475-39a9467bd168 | -11.64421 | -54.14318 | 2025-06-18 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 768b6d57-e3f5-3405-8d84-03898545c1d0 | -11.95858 | -58.73083 | 2025-06-18 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2c1d2b13-c8a6-3a81-9963-6dda0ca19381 | -12.5192 | -58.34684 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48e600e3-df1c-3ede-884a-2fcb2fc3f1bd | -14.02489 | -55.12827 | 2025-06-18 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ccfd472-fb02-3647-aac8-12322a3d964f | -9.96648 | -64.97447 | 2025-06-18 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b195a4e-a2a2-3e93-99a9-d102ccc4b0c6 | -13.72384 | -58.68285 | 2025-06-18 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a41a939-d70b-3d82-95f1-dda058de5313 | -11.96253 | -58.73142 | 2025-06-18 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e272b79-3997-3e44-b58a-d357839459f6 | -14.02359 | -54.49397 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30736846-354f-31e0-8121-75688ca6383d | -10.92968 | -56.83942 | 2025-06-18 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4522d03-7298-3289-8f10-8d91884a1156 | -13.64933 | -53.94048 | 2025-06-18 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a516126f-3881-33fc-b07e-ee4d01a5b807 | -13.65488 | -53.94132 | 2025-06-18 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9f10c72-eca0-39bd-ae4b-cb95445bb618 | -13.58318 | -59.23051 | 2025-06-18 05:31:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e823fb6-0cbd-321b-a817-80b7ee9b7d20 | -12.43121 | -54.87299 | 2025-06-18 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ac1cea4-8f10-35a1-8d77-009261f47957 | -11.9618 | -58.73661 | 2025-06-18 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8aeb7209-029e-3d05-a64f-020d52d1334b | -12.51463 | -58.34993 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49798a67-2661-33b0-8ed5-b182461ef7e4 | -12.51105 | -58.34569 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aaec2941-bdae-383f-878f-af6f76551ddb | -11.87554 | -57.01568 | 2025-06-18 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88e54bd1-d2a6-3b45-8942-725d2d606351 | -14.02121 | -54.49306 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d40d6653-aeaa-3583-9fa2-0c16fd45e7e8 | -11.80815 | -57.34975 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2318f4f9-ba3f-3451-9447-892980930d6a | -19.00357 | -52.08237 | 2025-06-18 05:31:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ad442abe-e761-3c7f-8a35-9197304c9641 | -12.16898 | -56.54114 | 2025-06-18 05:31:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc290140-21c5-3478-8448-5d0a4bb84271 | -13.29119 | -57.06944 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7a4ab9b-8769-3f1b-a453-59733fdb99dc | -12.64564 | -54.12202 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96044d22-e226-34f8-b7ee-a08fa59d694b | -11.91817 | -54.8217 | 2025-06-18 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ce026ac-74a8-3e1a-87f8-7efdb073036b | -12.53151 | -57.77501 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01d018e7-d1d0-32b0-92a0-df472e23b69b | -12.49766 | -55.74201 | 2025-06-18 05:31:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 578e7e38-a165-3b8f-834e-531354e575da | -13.7765 | -54.19623 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62ba4a53-8a97-35ce-b9ac-14f5d85a1653 | -11.64505 | -54.13622 | 2025-06-18 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81b95e19-3b51-30bf-90ac-cf788eb064ac | -10.66115 | -59.28825 | 2025-06-18 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 609f7f79-a828-3e9a-bbb2-bb231796cc5e | -9.96587 | -64.97821 | 2025-06-18 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40be8eef-027e-3d82-829d-c06d34e5b011 | -12.42645 | -54.86912 | 2025-06-18 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f033c555-70c2-39f2-a528-a080409e5997 | -13.80338 | -54.2991 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c1f0e45-c866-3521-a634-abcce9947b4a | -11.62549 | -58.29312 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845c6fd3-b30a-3e51-aa85-8f1c69e29810 | -13.96364 | -56.79376 | 2025-06-18 05:31:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11797a59-7ef7-32b1-a6af-3b54e4f8c90d | -14.47115 | -58.06913 | 2025-06-18 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 691f785e-fbe1-3efa-af84-c243cc85c258 | -13.96286 | -56.79466 | 2025-06-18 05:31:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 425a9925-1d57-3dff-8672-bb04ee51fba1 | -12.49899 | -55.74216 | 2025-06-18 05:31:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e1557d58-393c-3547-bf7b-1c0ecbe63598 | -15.62651 | -57.30692 | 2025-06-18 05:31:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9d76407-9711-3cbe-a424-23b0fdd5d1f5 | -12.57912 | -56.98468 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3728e44-a631-3d37-b1c4-796013cb60b9 | -14.02567 | -55.12177 | 2025-06-18 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2e75e2f5-ac85-39c5-ae88-26696221bded | -13.80381 | -54.29542 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29a3b05d-2571-3383-9c6a-6ad3d44713e1 | -11.99055 | -57.1993 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e1c3ee6-f538-35bd-80f3-a3214042daf0 | -12.55605 | -57.75182 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14bcfc80-ae69-3f20-9dc6-391d5df92d43 | -12.65819 | -54.10952 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aa4c75e-6c7f-3c83-812e-331e56e0899a | -11.36626 | -56.56171 | 2025-06-18 05:31:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1646677-4d67-3207-8b00-17cb4df4158e | -12.52783 | -57.77037 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89c81c07-5db2-32ee-9c96-3e54752f037a | -13.79794 | -54.29837 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ab91c6a-a858-3926-abe9-572dcd7a065e | -12.53096 | -57.77905 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7419ea44-aaaa-34c9-a0ca-15d66e2ad873 | -11.62145 | -58.2925 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3d0ac1cf-a6ff-330f-9a84-e9685effe4bb | -12.57971 | -56.98014 | 2025-06-18 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de7eecc8-c5db-3bbd-8754-093ac48c737a | -12.52728 | -57.77443 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7a5ecf8-d12f-36fe-b5d5-0a975a2de119 | -10.93849 | -56.84061 | 2025-06-18 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a61ab6e-b8f8-3c9a-898c-80a1771c0057 | -15.57113 | -55.65192 | 2025-06-18 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d15b2fc-51a3-3333-ba0d-b57fb3b9d5f0 | -12.23233 | -63.60111 | 2025-06-18 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41625ce1-edf1-3c5e-9ea2-f70d98a4a0ec | -12.53814 | -57.72649 | 2025-06-18 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c579026b-421a-3eb8-9367-7696ab79825a | -12.02659 | -57.09439 | 2025-06-18 05:31:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1e7e2c2-b285-3c28-a839-0035c41aae8e | -13.78198 | -54.19701 | 2025-06-18 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README24.md)
