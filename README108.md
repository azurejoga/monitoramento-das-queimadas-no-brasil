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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2d94fdc-6e49-3943-ace3-b8e5887b7c95 | -11.41669 | -64.20718 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af40e566-5582-3b59-89e3-21416eac2a32 | -11.41335 | -64.20663 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f0ccfd0-ff94-39dc-a304-18b44a0e3c86 | -11.96467 | -63.839 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e687df8d-53ab-3671-95b7-39d4f2387344 | -11.96136 | -63.83845 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4778632-c254-3c9b-b641-f4cdf4ad65a7 | -11.76368 | -63.82095 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22830544-96ef-3bc4-9c81-6e065862a467 | -11.76312 | -63.82448 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6277f68-7972-301c-99b2-d462208c5d25 | -11.76184 | -64.08906 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0de34c57-d0da-3254-a046-df3cb98f9f1d | -11.76128 | -64.09261 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae1094e0-2513-3a0f-955e-bf378952cdfb | -11.76037 | -63.82041 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96a03ecd-74cd-3c10-b157-220be604f36e | -11.75795 | -64.09207 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53ae7070-18d5-3c0a-81b9-905414592833 | -11.75425 | -63.83749 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb7e58d8-901d-3d08-a5af-d8c8501f25c1 | -11.75406 | -64.09507 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b851ca5f-0166-3b69-9569-1595d2bc3f39 | -11.75262 | -63.82638 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa4eeaa8-61fd-3f7e-a827-767c379ec2a2 | -11.75094 | -63.83693 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20fcc6fe-5583-3415-8a50-73f3c180e524 | -11.75038 | -63.84045 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40ab140c-131d-32fb-9b35-e2c430df1174 | -11.74931 | -63.82582 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9376bdc3-899d-3644-9447-603985911625 | -11.74763 | -63.83637 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d649b9b-e345-3489-ba72-b215cf178c53 | -11.74707 | -63.83989 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9be0453-4c92-3984-abd1-f51725035750 | -11.746 | -63.82528 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1c344e2-2c16-3d23-82f5-3659216b09c6 | -11.74376 | -63.83934 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6617581-f260-309b-9b97-abd71cf4060f | -11.74101 | -63.83528 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76ace338-ecbd-35fd-bfe7-815cb0c17e75 | -11.74045 | -63.83881 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f8ba648-1824-3532-b33e-1cd7eebb0d50 | -11.73882 | -63.82767 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20de582f-b9c3-333e-971d-5847323675a1 | -11.73826 | -63.8312 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac641830-5820-37b4-8ca4-2b2f8e63fa20 | -11.7377 | -63.83473 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb197820-07af-3430-b869-938337a95368 | -11.73663 | -63.82008 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cab1a5cc-f8e7-3a3b-87cd-aed89877a013 | -11.73607 | -63.82361 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82c3f6f8-650e-3cf4-bb0a-963588f748f4 | -11.73444 | -63.81251 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55568cd5-4303-3bc1-bca8-044fdbb4bfc5 | -11.73322 | -64.03341 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0bc5f6c-52e5-3bdf-a66d-cc3596f54967 | -11.73266 | -64.03695 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d631f527-ef2b-3e21-8ee1-492d875eecca | -11.73047 | -64.0293 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75773e8e-7427-3aef-a158-78a0dc416eee | -11.72934 | -64.03639 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 094abc77-f8df-3416-b0ca-853a07ed09e4 | -11.72877 | -64.03993 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09750a13-c897-3217-ad07-596524258e80 | -11.72821 | -64.04348 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5acbff2-0518-321d-b308-4196de96cc65 | -11.72764 | -64.04704 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb35082-6ef9-360a-b4aa-c1737da6d719 | -11.72715 | -64.02876 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a8c3d32-0b52-3457-a012-e0f9607d4690 | -11.72707 | -64.05059 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d280d3db-8086-3774-9ff5-663ab8580679 | -11.72488 | -64.04294 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a0a0255-e3d0-39c3-81d3-e298defda6cb | -11.69679 | -64.00556 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b24a5a79-24b1-30c4-b5b7-1503ee892778 | -11.66759 | -64.04041 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 492e8ce5-cf66-30e1-adfa-74d57facfb53 | -11.66702 | -64.04395 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3339429f-99a1-3c76-8800-80f2aab69dc2 | -11.66653 | -64.02565 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9226a79-4983-3d42-b36f-de55e4ade48e | -11.66483 | -64.03629 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81b4b1fb-ddf5-34ea-8d75-da96f28cd103 | -11.66427 | -64.03985 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 825b29b4-6970-3e8f-8de9-cc080d2a1e6a | -11.66377 | -64.02155 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45115d07-3d30-321d-ba9c-a1dbb687bd8b | -11.6637 | -64.0434 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ef37ffc-666b-382f-a194-cf10c998f52a | -11.66095 | -64.03931 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6957eae4-1c83-3784-9a23-6589d01cb1c8 | -11.66038 | -64.04287 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f298fa0-877f-31d5-ac98-94905db33c26 | -11.65876 | -64.03167 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b6cf6ff-5b8b-34f2-a95c-e940bbd836c1 | -11.65762 | -64.03879 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa0fd3e7-9c3d-3b93-bdac-f0a2294cf382 | -11.65649 | -64.04591 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e03dcb3-8bb8-350c-89d1-1157b1db38db | -11.65543 | -64.03114 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2326651a-1e47-30a7-8a7c-269939f5cba5 | -11.65487 | -64.03471 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 881fbb46-2986-399f-ac97-8680213f6e43 | -11.62906 | -63.96159 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6850764-a898-3268-bad2-05490fd84d5d | -11.62574 | -63.96104 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b847a18-d8f7-35b4-adfb-54acfcda77dc | -11.62517 | -63.96458 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 637150ef-cc5d-3087-adf7-22809065cc5d | -11.78608 | -64.16884 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79ea44cd-5a70-34d6-aaf2-125ad0b72275 | -11.78332 | -64.16473 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f3add66-8709-30bc-8b84-cbbba8fc90b3 | -11.78 | -64.16417 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31d63b54-984a-3230-8283-0db7da1da85b | -11.77713 | -64.16446 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 302ba673-dc8c-3988-b234-09d98260397c | -11.7738 | -64.16391 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 788675b5-ec4b-32b1-ad03-f7ab67bc0989 | -11.77104 | -64.15981 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6c41c8-eb51-3852-82c3-45cbc068261b | -11.77048 | -64.16336 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42396a6d-ff5c-3f4c-adab-8e78d55a2419 | -11.76772 | -64.15926 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68316590-dbff-3843-b8fb-2a4979424727 | -11.76715 | -64.16281 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 428bbe9e-8261-39c8-b801-cf27684c9c9e | -11.76382 | -64.16225 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d315809-b396-37cc-97bf-a454b24aa983 | -11.7605 | -64.16172 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ddf02f-aed5-33e0-ba86-8e825d871206 | -11.75384 | -64.16062 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a45780d-a514-38be-9a6b-8c26abc5166b | -11.75051 | -64.16009 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d4430f0-84c6-35b8-b5d5-8356080813b0 | -11.74662 | -64.16309 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de8de2d6-f5cc-3e0d-a0b3-92b32d354a20 | -11.74281 | -64.14423 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 963e8f4e-5022-33ed-b5b6-fd0b58cf7db5 | -11.73891 | -64.14722 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68967264-8060-34ef-8975-e3a2fa54de80 | -11.73664 | -64.16145 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1cea004-9725-3abc-88bd-3a222d34d056 | -11.73502 | -64.15023 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bad25994-2944-3345-bff7-af15484f8fa4 | -11.73331 | -64.16089 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4a976d6-3443-36ab-80e3-d0a53398e1f5 | -11.72447 | -64.15213 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81a0a15f-9ac8-3798-a224-62f37010504c | -11.7239 | -64.15568 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11366751-b66a-39f5-bbb3-cacdb569581b | -11.72058 | -64.15513 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f5b14c4-0eb7-3fd9-9230-a129391cef90 | -11.71782 | -64.15102 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79e734a5-bd29-310e-ab12-136465c6b414 | -11.71725 | -64.15458 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f217650-c81e-3e36-84d3-75292fc225ce | -11.71668 | -64.15813 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a16616b8-6499-31f8-aba7-a2998d5a4a31 | -11.71506 | -64.14693 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1550521-72fa-3ba2-8796-86dfdb7cb9fd | -11.71279 | -64.16113 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77b60300-68c3-3b9d-a9ea-058a66e7e1e5 | -11.70898 | -64.14228 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b3088fd-183c-3c72-b99c-c1a8688e3f2c | -11.70889 | -64.16415 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a100d772-644d-3fe2-bc27-f0e333d431ab | -11.70556 | -64.1636 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62d8fb9d-2db6-3268-a9a5-7c1e2a80be54 | -11.70499 | -64.16715 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1182e1a6-7b48-3606-aef0-4e6b8ef6f291 | -11.70347 | -64.13409 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c42c92b-f1ed-337a-b06f-e8f7fab11e0a | -11.7029 | -64.13763 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 413655ac-2a27-3d85-9231-542c652cf4f1 | -11.69007 | -64.15375 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2758bbbd-902f-3240-912a-d66e8a9889af | -11.68731 | -64.14965 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f3f38f2-e02a-3d06-9369-c810bc8c275d | -11.68674 | -64.1532 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 292211af-0f75-3744-b4e3-718834a96233 | -11.68342 | -64.15266 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3012c1e4-ffc9-3c2c-bc64-ac71c9405db3 | -11.68285 | -64.1562 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44c6ed36-06b7-3680-a512-cee2d2af7d83 | -11.67952 | -64.15565 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4bb529f-427b-3ebd-a4fa-20081322dee2 | -12.12294 | -63.37446 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74acaf8a-9466-3c4e-9362-9aa01bb03469 | -10.86375 | -63.92339 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90fce709-1052-3a7f-aa9a-e51b1ae3dc90 | -10.86319 | -63.92691 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0311db7-311c-36cf-9516-723a27e9d98f | -10.86105 | -63.89769 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8925953f-f34b-3b52-b121-590f26f78cd4 | -10.86043 | -63.92286 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README109.md)
