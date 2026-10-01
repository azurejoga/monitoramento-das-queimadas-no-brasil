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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e0bec78-786f-336d-996b-e09a6f38aef0 | -4.25773 | -50.76939 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 65971fb5-809e-3d62-a8bf-8cd683a00197 | 3.27568 | -60.61645 | 2026-10-01 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 960aeb69-b62d-30cc-a1f0-4d9f4fd6a909 | 3.28151 | -60.61882 | 2026-10-01 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 09f45a13-ebbb-3874-a850-34bdbd147b0c | 3.28096 | -60.61554 | 2026-10-01 06:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2223b5ee-73a6-3f9b-9c4d-d971c84c90cf | -3.48979 | -59.53104 | 2026-10-01 06:14:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b3b856e-cdec-3924-b98f-2ffcd905dcb2 | -3.68483 | -60.54506 | 2026-10-01 06:14:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9399d01-a3be-3714-95ca-2fc1a7e3eb6d | -3.48908 | -59.53605 | 2026-10-01 06:14:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3341afb0-c000-31a8-aca3-51dbb22b84cd | -6.66083 | -58.87401 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| abee99ab-b40a-35f5-ab17-507b55118ab1 | -3.70571 | -59.68657 | 2026-10-01 06:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 624210b8-e4ba-3531-830f-64d0aab32ec2 | -3.48605 | -59.53383 | 2026-10-01 06:14:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d30579a8-a5fa-3656-9b09-95ccaa5068c6 | -6.68329 | -58.87258 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dcb83722-0ef8-3247-8b26-5e443797e169 | -6.67448 | -58.87585 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e035173f-fcda-339c-bae4-4323b97bb142 | -6.66198 | -58.87611 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ffcd9339-3a34-3353-80c7-2ce4ae757753 | -6.67646 | -58.87167 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 04ef48ba-dd92-3d31-80f6-18935a8679aa | -6.68218 | -58.87044 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75743eca-0144-3a66-8a56-bd4fa08cfcb5 | -6.66119 | -58.88219 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2fe03923-2bdd-32e8-a0c6-bf83636cf92a | -6.66681 | -58.88112 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0504805c-9505-31e8-a1e3-298f484a1ba5 | -6.68132 | -58.87672 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51a1bd8a-ee07-3b66-b721-8f16082bdc65 | -6.66881 | -58.87704 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0a13ca83-8dd9-3efd-bfc2-74046c0dae88 | -6.65998 | -58.88023 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4c566b5a-7ba0-38e6-8413-c0770930d770 | -6.66766 | -58.87491 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0fc5de4a-3b4c-3648-a830-7f6cfdeb3235 | -6.48864 | -58.53287 | 2026-10-01 06:14:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a5e95b9-6503-3d01-a8c2-5f16425293b2 | -3.683 | -60.54404 | 2026-10-01 06:14:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90f137d1-b1cc-3f7d-89e0-5642d981e340 | -6.92514 | -59.28724 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f6e7ba4-212c-310f-b66a-f1a33159bd71 | -6.92902 | -59.28405 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c563f145-d8b5-3c44-a28a-0151a2362e65 | -3.68892 | -60.54491 | 2026-10-01 06:14:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d0b9533-e2ee-3994-a2f0-a89b89e8a679 | -6.92155 | -59.28895 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bf61457-da94-3b9f-9719-1ee857b96c81 | -6.92589 | -59.28138 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75c1101a-ed16-35a9-9075-205aa11a882e | -3.59697 | -61.71893 | 2026-10-01 06:14:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1d45b41-b998-32ab-8536-fefa2e95bd9b | -6.92234 | -59.28311 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c7cce8-2e5e-3d9e-a73f-aaf59aa4b169 | -6.48783 | -58.53911 | 2026-10-01 06:14:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f00049e-5df6-3fe9-8034-096d8f79cf81 | -6.67563 | -58.87803 | 2026-10-01 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7668d18e-1d67-3996-977a-cd020b44c5fb | -7.88233 | -72.30472 | 2026-10-01 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e505c610-9829-359c-ba22-af778ed33d2a | -3.70642 | -59.68164 | 2026-10-01 06:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c28d505-7051-3123-8eb9-a6b6eda111fb | -3.49236 | -59.53465 | 2026-10-01 06:14:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57ff84af-66b0-319b-99b6-14a2992c38c3 | -3.59151 | -61.71808 | 2026-10-01 06:14:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d159bcf-a5f1-348e-90fd-249c551015af | -4.32 | -50.81 | 2026-10-01 06:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26f643c1-e53d-3dd7-bc0b-4015a010576b | -4.29 | -50.81 | 2026-10-01 06:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d8ba760-2549-31c2-870e-e3a284bf7958 | -4.26 | -50.75 | 2026-10-01 06:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abc3013b-f995-35b2-bdfe-2090fdbafbe5 | -4.29 | -50.76 | 2026-10-01 06:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b00673-487a-3ec7-acb6-7edaa4a73e4e | -4.26 | -50.81 | 2026-10-01 06:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f719a9d-669d-35c7-bec2-1a8068402826 | -4.32 | -50.76 | 2026-10-01 06:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91feb290-f059-3a43-8a48-8d3fa3e362b0 | -3.11527 | -50.2816 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b6b7fc8a-667b-3367-b269-03e1b1ea3285 | -3.16168 | -54.06052 | 2026-10-01 06:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3266d3cf-cd54-3d59-8ad6-9c32e3853d4e | -3.34183 | -42.39732 | 2026-10-01 06:46:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6ec5b448-eeb0-3250-8d19-24751210c342 | -2.99602 | -51.03534 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 11a3ca64-e4f8-3c05-b382-b351e41fb1a1 | -3.08969 | -50.25859 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 45132215-7fe1-3ca1-a14e-9d3243f1d8ac | -3.11717 | -50.26961 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 2e73b54c-13a9-3ef7-bda6-38ac3e11d591 | -3.28741 | -53.84871 | 2026-10-01 06:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a255be43-8466-3b62-8538-a82a0c913ca9 | -1.90779 | -45.80601 | 2026-10-01 06:46:00 | AQUA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73349377-28fc-3338-b545-d11d0a39b907 | -2.92212 | -46.74935 | 2026-10-01 06:46:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b838069c-a359-3ba1-8d74-e5605fcd9e70 | -3.17185 | -54.08624 | 2026-10-01 06:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c1267856-c896-3e56-af4b-e70487579a6b | -3.15135 | -54.08806 | 2026-10-01 06:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e00efa16-162e-38f7-93f4-8308919264d8 | -3.10129 | -50.3041 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 61921215-af16-3076-a44f-36f0a8afd636 | -2.41425 | -49.29454 | 2026-10-01 06:46:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 78d4fac6-ca69-3335-94a2-5003c831046d | -2.99406 | -51.02829 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 00baaf44-51fc-32a5-b94e-68ef2327f7a5 | -3.15518 | -54.06454 | 2026-10-01 06:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 14f040d6-6306-387b-ae73-fa7692c26a24 | -3.16517 | -54.09016 | 2026-10-01 06:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f1f4a1cd-17c7-3689-8be3-efb494997811 | -2.97246 | -51.02502 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 35d7e08e-bb81-3674-a68d-7f0dedcc87b7 | -3.17897 | -54.09243 | 2026-10-01 06:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3ac774ea-a9f6-3b7d-88ee-fc2b8861e71d | -3.15802 | -54.08415 | 2026-10-01 06:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 2b1d28ef-5ee3-3491-a40f-9582c91d94be | -3.1032 | -50.29203 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 3e130eef-043d-3f3b-befa-366408bc7357 | -3.16824 | -54.10973 | 2026-10-01 06:46:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 37da25c9-9b38-3cd1-9629-1c4fd44f008c | -3.10821 | -50.27369 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2a7d9c37-78c9-3c00-a3bf-5ac9e5a2ea03 | -2.98326 | -51.02666 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 04d56499-f5ef-3846-afed-ed71dfadf1ad | -2.89625 | -54.12823 | 2026-10-01 06:46:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| d4f5130c-2a1d-36ce-b42b-92e72044f0b9 | -3.10639 | -50.2857 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| a40ea03f-bb58-3dd2-8514-8b4225c04a0f | -2.98522 | -51.03371 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2c69ecdb-3a96-32e6-84a6-1abba5a5b117 | -3.10458 | -50.29772 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| dec38773-4d5e-3dd4-b8b4-3a01ad27e57b | -3.10509 | -50.28008 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4e4021ee-8c36-3db5-95c6-3c8cfa284b2e | -2.96167 | -51.02337 | 2026-10-01 06:46:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c82b3676-e173-318e-97bc-f0b0eda292ba | -5.11896 | -55.9964 | 2026-10-01 06:48:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 1a19c204-e4f5-3bcc-87a2-bb09e8dad96d | -7.84995 | -45.81627 | 2026-10-01 06:48:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f136e219-9e95-3724-8d24-143604881401 | -4.89466 | -48.36867 | 2026-10-01 06:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c715dc7e-6c5c-3908-b4da-7340301b8538 | -6.00581 | -49.54993 | 2026-10-01 06:48:00 | AQUA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b1b7e48a-9cbc-3d69-9717-ae7a6a13185d | -4.26491 | -50.74993 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| ea1afd01-6cb7-3e57-be19-d2f0f1525889 | -11.41061 | -43.39647 | 2026-10-01 06:48:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ba0c0177-8a2b-376a-8683-9eb0e3a4267e | -4.294 | -50.76712 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1116.7 |
| 8c152f45-8af7-3811-b7f8-fa65714fb71d | -4.30627 | -50.75624 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| cb482dc5-d672-3b03-b80f-3adbaa23737d | -8.84373 | -49.69136 | 2026-10-01 06:48:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 38371a4f-1418-34bd-8ffa-3c4c31a7b32e | -4.30435 | -50.7687 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 441e37a3-d095-37bb-b38f-4aae245389b8 | -3.28025 | -53.8551 | 2026-10-01 06:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6db8ead9-adf1-3509-bace-d553ab42cdaa | -5.42908 | -43.44548 | 2026-10-01 06:48:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 689f1082-342b-3233-a1d2-3bbe1cca5132 | -4.89324 | -48.37781 | 2026-10-01 06:48:00 | AQUA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 25b3dc7f-6898-330b-87eb-46820d1a2ffd | -3.29743 | -53.83463 | 2026-10-01 06:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4d405448-4e0e-3306-a5b4-958be6059837 | -11.18269 | -45.10553 | 2026-10-01 06:48:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8be47942-c779-3f7d-9503-379b3a65249f | -4.27136 | -50.77631 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 213.4 |
| a4e39a44-9f17-3aeb-9ce7-d16ca77293f3 | -8.32872 | -44.15343 | 2026-10-01 06:48:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4467aa54-a5d1-3970-9f36-0a8cbdd3629c | -4.27975 | -50.79054 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 9fd57d76-c284-32e5-9ee2-e1f27bcfdb4f | -4.24422 | -50.74686 | 2026-10-01 06:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 36d62f05-f146-3a12-bdfb-18a1a641339f | -4.28171 | -50.77795 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1161.9 |
| ac45ff57-7669-3095-bddb-7c60fb62eff3 | -4.63644 | -50.60635 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5148d86a-35b4-31c4-ad04-07f2a7a51acf | -10.55601 | -50.03962 | 2026-10-01 06:48:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cd104cfa-5b47-3397-82c9-bc6407fd3d54 | -4.26937 | -50.78902 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 141f6027-06b8-30e0-b3e2-107bbb3d09cf | -6.01355 | -49.56141 | 2026-10-01 06:48:00 | AQUA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 220b1fcc-3ff4-337e-b3b1-3ed0746a5ecd | -4.45339 | -47.92362 | 2026-10-01 06:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a0abc36e-b4ec-3822-90e3-71b0c4be7d32 | -11.18273 | -45.11139 | 2026-10-01 06:48:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1d98b3d0-d984-3d08-b86f-34030820a915 | -4.28358 | -48.55497 | 2026-10-01 06:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c04ba0b9-9b0e-312d-9087-22720f0a757c | -4.26687 | -50.73747 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 39e6d4f2-2e09-3d9f-a540-1668c1b9508d | -9.21438 | -45.82507 | 2026-10-01 06:48:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README92.md)
