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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e7b5e9b-45a0-3d88-8eee-a30b669972c8 | -3.38905 | -51.14726 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19b09d1d-3ab7-39bf-a498-159ce4394c3a | -3.32746 | -45.59803 | 2024-12-10 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1ea3ff2-5f54-305e-8289-dca0e9f7eccc | -2.95845 | -53.7268 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1eaa1e8-f1d3-30dd-b795-215a8c8c8292 | -3.86075 | -40.44247 | 2024-12-10 04:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0165386f-b2b2-3d6f-8ffd-4a1fa45b9e25 | -3.10882 | -53.24493 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1e8ec27-e8b9-388c-bb49-15b5baf40ece | -3.12301 | -54.06343 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faed6b45-8eb4-3588-8dd9-83ef361ed839 | -12.85331 | -43.81633 | 2024-12-10 04:53:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56d59240-2c1a-3f4b-a802-9b0dcceb8f63 | -3.16499 | -53.6438 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92fa396c-e8ee-3b36-b8a8-ca005bd6ab76 | -2.2508 | -53.87339 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6dacab0-40f9-3ef6-b214-048c4e4d188f | -2.58088 | -54.34377 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f90efe7-36b5-325c-99b1-910155c403f2 | -2.95582 | -53.11621 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff1ca8f7-8de8-387d-bc5a-61593d0ea547 | -11.36995 | -57.57589 | 2024-12-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 506c5894-8848-36b4-87aa-be971a8a17f6 | -3.21035 | -52.85958 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48dbb1ba-37d5-362f-b404-ce403f8910fb | -2.99118 | -53.02122 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5982bb3f-ac8e-3963-b07c-1cbb731917bf | -3.4756 | -52.81602 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b6d92b6-1cfa-32b4-96d7-5298efae1a7c | -1.71121 | -52.44061 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0a743f4-4939-3780-9f1e-ff2f6897fc14 | -2.78622 | -53.24162 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 880877c8-56bb-3dac-a2d4-e8428b18b9b7 | -4.54925 | -48.02335 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f2a9380-5349-3a76-ab42-d5656c477a0a | -1.80784 | -48.7716 | 2024-12-10 04:53:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8183f9bd-af09-3218-97ea-8881ff9813f6 | -3.11382 | -54.07725 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 931c907f-2171-398d-924e-fffbdc9af8e9 | -3.51984 | -50.9833 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f1475fe-10f7-340a-bc3f-1d4b94f5503b | -2.83845 | -53.06207 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69071691-148e-3406-8410-6b0f7f176757 | -5.71245 | -46.54523 | 2024-12-10 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5cd98584-e10e-3b40-bd2d-f29b3704ab24 | -3.11327 | -53.2384 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 968ae1a5-c051-30ed-aa43-bf50dddb7a8f | -2.79683 | -53.23959 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 274d1876-ef48-34b5-9fb8-1df5bfb5d1ec | -6.91592 | -43.51488 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7cb28234-cffe-34a2-b91e-74c2d6d72035 | -2.8211 | -52.97706 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cf3cf801-5ab1-394a-9a0c-f5a183860a35 | -4.06095 | -54.43703 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 779a6723-d637-3ceb-8aac-c3d6d8946065 | -2.41289 | -53.6909 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b55d3905-8057-34c5-95b6-6add240bfe8a | -3.87618 | -50.36067 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8a0caab-8ff8-3ea5-9906-c1236160dd40 | -11.65996 | -58.27301 | 2024-12-10 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe7e2a9d-361e-3e9c-9171-4d85fc6cf1ee | -2.81777 | -52.97655 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d167a087-1d4a-3149-8b7c-e71c94301020 | -1.96447 | -48.39146 | 2024-12-10 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41c9b27a-c39b-32f9-80e8-2266ae3e85c4 | -1.39735 | -52.33825 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 916aed81-3300-3e81-9cb5-091c7d80e1bc | -6.15832 | -46.73812 | 2024-12-10 04:53:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1362562-fc58-3d74-aab3-5926a02ae375 | -2.81455 | -53.06198 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ff69f68-02dd-3ea6-9479-6d3711639f4a | -2.64481 | -54.29042 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efe66cc5-a23d-3bfb-8255-5ee1ae19eb8f | -4.3847 | -47.75964 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2c283526-ff75-3e4e-a3db-1dfaba615e2b | -3.04182 | -54.24212 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d26cdeda-a3e7-351a-903b-6b79000878f2 | -3.61037 | -53.49415 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a559a7b-e1f4-38e1-bd6e-cb3fe2fd76cf | -3.09952 | -54.0789 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a78f2692-c9b3-32f1-80c4-dc5b0cf3a2ed | -5.91819 | -48.05165 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 42edab0e-2591-3ce1-ab48-30d3697d8098 | -3.18539 | -54.33443 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 68e6ffbc-4472-3826-a23a-adf0b4cd0b67 | -6.96925 | -42.99023 | 2024-12-10 04:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bd88892a-4686-326a-8d59-044e176324f5 | -10.96253 | -54.09374 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 124d6a96-36b3-32b1-bb03-0f2455f20a93 | -3.23741 | -51.33451 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcfced6d-214a-39b5-8f64-4c69304f3542 | -3.20547 | -46.81054 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 60a414ba-6d08-3ba9-b8a2-506fa21cedad | -2.83178 | -53.06104 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e162d2b6-c608-3689-be65-503535bc4a54 | -4.38789 | -47.76524 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7098d8d8-993d-3cc6-811b-e4f3fad10dd5 | -2.75022 | -54.15531 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e8a1f1c-9e62-3f8e-acfe-e611ebf40d0e | -12.53631 | -57.74339 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c73b2f6c-13e8-3c22-9e4a-883cad036c6d | -15.1757 | -59.42715 | 2024-12-10 04:55:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad81a25e-9155-3c52-a81d-3a413ee98daa | -12.5465 | -58.36774 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d4fa82ae-13ba-3b93-9097-706e4318a198 | -15.0938 | -59.63702 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5285c20-363f-39b3-90fe-b264a0b958d4 | -12.56044 | -57.71177 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8b4125aa-b62b-3e10-95b0-3e5dbe8526d4 | -12.53561 | -57.72536 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d52460d-89a3-3452-81b0-37403a3e1d4e | -13.45922 | -53.35464 | 2024-12-10 04:55:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89043c1c-eba4-3fe9-a036-3d2c4307c496 | -12.53779 | -57.73467 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eaff8b6-25d5-3d6d-b28a-bf236e5dce46 | -19.02282 | -57.62325 | 2024-12-10 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1b771160-67d5-379b-9519-036fed7006cd | -18.057 | -50.83449 | 2024-12-10 04:55:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c9aa817-50f8-39eb-881f-7d08717a361c | -17.46953 | -47.8685 | 2024-12-10 04:55:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb2682eb-5035-3a86-886d-773ba9e2f407 | -8.97243 | -47.08313 | 2024-12-10 04:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03eabfbb-396f-3eff-b401-c4a452819231 | -15.37929 | -60.23261 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 712a0b42-c493-30a5-a779-7ff4e5b5adee | -12.90686 | -55.05127 | 2024-12-10 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf530f5f-7e9c-3988-a739-ca2ef657c51b | -12.71521 | -54.97264 | 2024-12-10 04:55:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e5df69a5-bd52-30a2-8395-43066b9debba | -12.56627 | -57.76658 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4fe34644-3f3c-3248-9898-f1b6eab82a7f | -16.37182 | -47.40062 | 2024-12-10 04:55:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4d43d1b-461f-3b0f-8566-ac12741e23ac | -15.37406 | -53.1301 | 2024-12-10 04:55:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd4282d9-9bd0-3240-9c5f-b39ff712bca0 | -12.04622 | -62.79346 | 2024-12-10 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 581ea8a6-53c2-39d1-b734-86b015b51e78 | -14.82826 | -55.91092 | 2024-12-10 04:55:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3225d3c9-01dc-3a48-82dc-94d1703afec6 | -8.71461 | -44.00533 | 2024-12-10 04:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2993fa60-740b-3b07-a755-c59ff71c4ab8 | -15.08368 | -59.62753 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 056b82de-ffd8-3bf0-b729-4704685dbb57 | -7.6016 | -46.63679 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e3d4ab5-34eb-3c43-98f2-220c94353fcf | -8.85984 | -47.6692 | 2024-12-10 04:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5eb88591-6381-3117-b66c-a11a6a6e1a5a | -12.53163 | -58.34105 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 38810e07-4763-32ba-baf1-033950d6e8d8 | -8.69628 | -50.19341 | 2024-12-10 04:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdc197e7-f3ef-321d-aad7-c228c28202e7 | -15.88186 | -53.27302 | 2024-12-10 04:55:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c5fa353-83c0-3925-97fb-6504757a1d4d | -12.56022 | -58.35575 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6b259bf8-8f10-3d9f-b0ab-5f88db68c6f4 | -7.59716 | -46.63619 | 2024-12-10 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fc032d5-17b2-3c37-975f-e82dbace8d6b | -12.54216 | -58.34766 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3c3e839c-dbe9-3909-81ef-d16af5e3e5cd | -12.53999 | -57.72169 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfcead23-9545-3adc-849e-fbe412812c2c | -19.43315 | -54.78508 | 2024-12-10 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fed6a3d-5c82-37cd-ac0d-fdd8b2a146f9 | -15.17451 | -56.78735 | 2024-12-10 04:55:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce66e070-aca3-38a1-93dd-ae7f1ad31164 | -15.61558 | -59.74685 | 2024-12-10 04:55:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 483df8b8-6f82-3ac6-a13c-d4b3e48eca0f | -12.54731 | -58.36303 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 62dcff00-7f97-3a1e-9289-1644d4d4b6f1 | -12.85632 | -58.22046 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 555c0f6a-927b-3043-9173-30efbadb7559 | -14.96891 | -44.41413 | 2024-12-10 04:55:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b596d15b-678c-37c8-a934-4edea2d626cb | -12.55804 | -58.34578 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 07d2a253-bf2a-355c-be64-34e4dacb5133 | -15.3667 | -53.13278 | 2024-12-10 04:55:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdc7cbb5-83b5-3ea1-84a1-848c367b5d84 | -15.07886 | -59.63198 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a382523-128b-3606-818f-4c58615c3a73 | -15.0867 | -59.63341 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e9f0de2-b119-3cc3-aaf7-341497a55cfe | -12.57065 | -57.76287 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b35146db-ea37-34f6-9809-04407699b9bd | -15.08989 | -59.63627 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0354d81-b1f9-3efa-844e-871f13967af8 | -12.55406 | -58.36909 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d3074a0-94f0-3890-9a6b-a1086ce727c6 | -16.34765 | -43.69757 | 2024-12-10 04:55:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3bb1ee6-88d3-38d5-8abc-cd8a70af708b | -15.06738 | -59.6512 | 2024-12-10 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc5ef129-f973-321d-93cc-a5c6eff995fe | -14.83327 | -58.07359 | 2024-12-10 04:55:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14148dfd-7211-352b-b276-642aca7fdd44 | -12.53996 | -57.74405 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 149aa763-89bb-32f6-babd-c2321b39177d | -12.55427 | -58.34506 | 2024-12-10 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2c565a65-f0d2-3c32-84c6-33b31fadbdce | -17.44733 | -48.17077 | 2024-12-10 04:55:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README29.md)
