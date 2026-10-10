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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ca8c398-375d-39af-af79-eb2f4a458ea5 | -5.24245 | -60.1955 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 217017b6-f66c-3fd9-ab75-7835f5b1a603 | -5.23862 | -60.19035 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c502e6f4-5461-31e0-b390-c084e79dbc7a | -3.55744 | -54.69812 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf2d486a-639b-3025-8c77-db9de0279ed7 | -6.44476 | -55.05381 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8a2922b2-5b3f-3edf-b105-bcff4a1fee77 | -3.31624 | -54.67065 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6cfe54ab-140b-3e62-a3bf-56df88493d9d | -4.10692 | -54.01594 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f075d8e-63f0-3306-8ed7-56579c2e9d11 | -5.09417 | -60.22084 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 301d39a3-fa7c-37ed-a4a1-dd7e9a89cbad | -3.53758 | -54.74663 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 72155dc6-d24f-3f68-ae37-4295adfbd2f9 | -3.95511 | -55.336 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12007731-225b-326a-8db5-b458e2fe0ac2 | -1.64681 | -54.4028 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3e7cebf4-9f29-3517-9106-41ef6b089786 | -6.44694 | -55.28422 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82f0d277-71c5-337b-a3a8-6ea815d57a8e | -3.74385 | -59.62557 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f31e801-66b0-3547-88c2-f82509ec15c6 | -2.75239 | -54.10619 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 02e41600-05c2-3760-9f13-1947e5eb154f | -6.47548 | -55.06916 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 105d7591-eb21-3ec8-9b85-f8af3395f609 | -3.20529 | -53.86295 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c611044-4b23-3a86-a912-05e625b87344 | -1.27099 | -55.74633 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb9d189e-fb41-37ed-9e6f-0221434f8030 | -3.18277 | -58.62833 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 06f66c5d-cbb6-316a-a0f3-f7f4ac2b9df9 | -2.4502 | -58.03074 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a2c0174-57b3-3794-9d85-a080cc6b5712 | -3.18447 | -60.04621 | 2026-10-10 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e7e669c-6242-3a3b-a8e2-9e9f5033ce56 | -1.88028 | -56.30814 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a962ee-1b62-3e81-be55-443ec1e49235 | -1.63879 | -54.39685 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e6e6b2d-2f8d-35f1-8130-459d7bdf4eb0 | -5.79006 | -53.79896 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2020937a-6d6b-3f5c-926a-f1d46a9b9c55 | -3.55187 | -54.69193 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68164848-b2b1-39ec-ba67-9ad90b3d0251 | -6.47476 | -55.07455 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4996f823-b07b-3b09-86ad-3d0f25e946cd | -2.57059 | -57.4174 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7528f571-eb67-3bbe-ac49-e49a11a14102 | -4.20188 | -59.41012 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19821432-702d-324e-b91d-16d5b9a8311e | -3.43928 | -59.62716 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dc1930e-0375-3b40-aa92-ab43472e0c47 | -6.4632 | -55.49725 | 2026-10-10 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a3193f5f-97c2-315a-9c10-9e30de07e811 | -2.73387 | -54.13932 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a28589b3-1856-3f4a-b255-f9ece8d6e114 | -3.56962 | -54.37866 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b903779c-e418-3805-9824-c57bf2317626 | -3.90528 | -58.94644 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dad08775-2d3c-34bb-bd3d-4c2a3ee3c978 | -3.83836 | -55.79384 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 935fb45b-85a2-385c-b1f0-341969f313c3 | -1.2698 | -55.75414 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d7514fa-fc32-3a67-8ac6-47378f10a873 | -1.10377 | -54.17146 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8492d8ef-d363-395d-87cc-daf43148ba73 | -3.91708 | -55.82227 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9f7d651-18e3-3488-ba2e-006eece5ac9c | -4.52209 | -61.12784 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6913a2d-fdd2-33ca-9b8d-a126c0cffaed | -2.89066 | -59.20944 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19450a25-8df3-3659-8b92-b4f62cce3df8 | -3.27417 | -54.6949 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 300b696e-590a-344b-a390-78a948b68715 | 0.00327 | -60.57675 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de74136f-911d-3e28-9d1c-8e22c3f9f23a | -1.103 | -54.17646 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 595972d8-1601-3cfb-9f69-bb506817f846 | -3.7499 | -55.95017 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bb6990e-fcac-3459-95e1-56cc3c7d9e8a | -3.57495 | -54.711 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8b3f9f9-1808-3c46-ad15-b9983e01542c | -3.93068 | -55.72689 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6868e92c-d488-336b-81ef-0409b675358e | -3.75752 | -59.62774 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c1831a12-42dc-30ef-8d7c-10d99c311e05 | -2.99872 | -53.91701 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d63ddfa-0d0b-35cd-9528-47edc799e659 | -3.90007 | -55.89931 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ab0d597-5a5a-3a7c-ad14-f2038cb431f4 | 0.00382 | -60.58026 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99448af7-8640-30f1-b6ce-cb6f067d91db | -2.99359 | -53.91665 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e8d920a-a54a-3dad-ba59-6bf6caf1e3d8 | -3.98368 | -54.46195 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6e3ae804-de70-3b84-82b4-14c914d23852 | -2.62811 | -57.74023 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6318ac82-8cad-38df-86cb-c5b70cd338e4 | -2.94246 | -54.0798 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c0006649-d2d8-32d7-afb9-52949f7a87d6 | -1.2704 | -55.75024 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44d92600-0cb1-3d8f-8f1e-20198a2c1f2b | -3.11043 | -53.78431 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d983856f-c94f-3380-be7c-dfc0f628c647 | -1.32661 | -55.46047 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39cfb708-a67a-3f9b-8661-78332c5be56e | -3.95048 | -58.84028 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 175d4c2b-47ea-396a-acef-6dfd01538e61 | -2.85303 | -59.12199 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b131269-cdcf-36a1-b114-39a627366c37 | -3.35987 | -59.62267 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49529396-4bfa-3f3d-9d14-3e4fbdf298d1 | -3.87518 | -55.99004 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7612174c-a67f-3020-9aef-b90c985eeb3d | -3.06061 | -59.26364 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 657a5400-19e3-3056-b1ec-226b63d09f24 | -1.8847 | -54.68455 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 658553d2-0954-3ed3-8b74-1a0cc17848ae | -3.03408 | -59.16378 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4843a657-31af-3b19-aa57-a5b6d0c7ef97 | -6.46252 | -55.5022 | 2026-10-10 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65a881f5-a4c4-3370-a0fa-87ab0953178d | -2.56989 | -57.41637 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8fb90301-0da3-3bc8-ac10-047830de7d8c | -1.21465 | -55.65246 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 066f432d-6f51-323c-9709-5839e19b6c9e | -3.00032 | -53.90586 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddb59b92-5ef8-30b5-9dde-2963aca723fd | -1.95752 | -54.40412 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72849472-bda1-3262-b213-b1091b92a828 | -3.57084 | -54.69477 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff99db47-1879-34d7-b2bd-94727458e1cc | -3.77144 | -58.52722 | 2026-10-10 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d651f14c-dbeb-35c3-9aba-03374b3decdf | -3.2213 | -57.81169 | 2026-10-10 05:48:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d640d0c-fe0a-3392-b438-242d13b9dba9 | -2.54764 | -57.38698 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d75ec17-e1d4-37c7-b5e0-9bfb5e21fb77 | -1.32239 | -56.4064 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2856d58-b42e-3c31-b572-4191988ddcaa | -6.37022 | -55.16139 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cef2d6e2-3d68-3641-b2cc-b91443a35817 | -1.95902 | -54.3939 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff3c920c-4e08-316c-9d8c-fa7a7cb2415e | -3.77987 | -58.58708 | 2026-10-10 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83eb9787-e93b-3e47-9950-a44b0a9bfdbe | -2.40271 | -57.90211 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7cef285-812c-3668-960d-b050122a4a92 | -3.07662 | -59.13512 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5171d355-ac84-3c62-8fb8-154c2980f64c | -2.45564 | -58.02863 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21caef54-75c3-35c4-a18f-169c22d46a32 | -5.07377 | -60.21566 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91a4b457-1e62-3eb7-ac98-2574ecd145df | -6.45903 | -55.481 | 2026-10-10 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5d8858d-7937-3a27-8c64-9afea7a03a9a | -5.30228 | -60.21079 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80b8aff0-3aa6-36f3-9a59-ef27ebcbf137 | -3.10236 | -53.93571 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6398aeb0-2739-336e-ba13-d5724ad5b9f1 | -5.22736 | -60.04464 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa809ea1-cc60-3d59-9718-35cb82118fb4 | -3.87793 | -55.84285 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40c6dc34-e55c-3b62-b271-911ca09fe5a0 | -3.99263 | -59.36597 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e2d1a391-44c1-397d-9364-848bb1d5153c | -2.92837 | -54.08274 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f20377f2-8a60-3137-a162-9319c6cd36c9 | -2.45063 | -58.0279 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc85130a-9e29-39ab-a7fd-f75941af94e8 | -5.09481 | -60.21638 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be2974ff-b5d2-3d75-9b11-8b9b99f1ed0a | -2.83334 | -54.81206 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 427a96b4-b796-35ee-a12e-2e343aba0080 | -1.25238 | -55.79168 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 767debeb-0c73-3aaf-905f-86090a75a5f4 | -2.99526 | -53.90554 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69a5d1cb-a9c6-3c64-af13-070a259163d3 | -3.80559 | -59.21685 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35c63a2e-36c3-300c-8f81-a6e29c541ccf | -5.25791 | -60.33854 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12c76409-dacd-3fdc-bb31-7eaa8183059e | -2.84713 | -59.11759 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2baf0fe3-d3be-32b2-b90b-90a7d272febb | -5.09034 | -60.2157 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07fd89ec-90ef-3ab4-af82-3c13875188f2 | -3.65152 | -59.71548 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e20cdacd-dae2-3d60-94e7-e717d1948eae | -3.99146 | -54.4535 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95e22c21-cc2f-375f-84a2-b06c3f1693a0 | -1.27673 | -55.74712 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14f53f4c-1fdb-34a7-879a-dac4513e0f4d | -3.50194 | -54.61568 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e16c6780-f48c-36fd-8896-62b1ccd791c0 | -3.98129 | -59.35706 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1d221d24-db27-38b0-84fd-35320b33d618 | -2.63105 | -57.74075 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README144.md)
