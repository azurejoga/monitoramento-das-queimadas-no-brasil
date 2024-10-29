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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ded6cb60-062f-3ce1-b1a1-f943822b1ea0 | -3.67217 | -54.07581 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c7ce1f9-5fb6-33d5-88b1-1c1794029989 | -3.61203 | -54.03524 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f8a2120-a24a-3569-b4ca-a3b40813413d | -3.61144 | -54.03891 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1322bc5e-1bf2-320a-b2eb-d0203fe89ea4 | -3.59424 | -53.78629 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cbd877e9-c7c5-32fb-8cc4-cb2f4ce13f3b | -3.59005 | -54.68381 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b01b5898-de52-3264-a9c9-055ef2a511cf | -3.58478 | -54.66245 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb8fe2ab-9747-3cab-8fdd-6a6db5a73e19 | -3.57002 | -54.6724 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98924949-d8a9-344d-9346-306e1f950d00 | -3.56937 | -54.67635 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fdaf95ef-68b3-353a-9609-87a138b9f728 | -3.55196 | -53.9926 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ae38dc7-14e9-38ff-86fa-de776599115c | -3.54522 | -54.74286 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da8693de-f712-3064-89c3-89404d08022e | -3.51171 | -54.52464 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6178c4a-f91a-338e-9d4e-a2f70f49c263 | -3.50796 | -54.03395 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab82d747-237e-3dbd-9e14-f86f5015307c | -3.50783 | -54.6293 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07d32a45-65a5-36ff-a932-f7b0b2d8f25d | -3.49975 | -54.43884 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd3958a5-a12a-37d6-b478-d77b604ad9a9 | -3.47368 | -54.57112 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6976227-2231-3a04-8af7-28a4c1d45b84 | -3.47197 | -54.15305 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e4fa1eb-3bb7-38bb-a308-fec03bd4dc95 | -3.47136 | -54.15681 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2604b17e-dcba-3f7b-8b57-a4063031f96e | -3.47068 | -54.83178 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7485b13e-b1be-32cd-8f50-2191b61b68dd | -3.46879 | -54.57436 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da6da4ed-c604-31fb-9e02-981b9678d803 | -3.46636 | -54.83107 | 2024-10-29 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbe9d71f-3436-3bb6-8585-b7986cf1a29e | -3.46162 | -54.61788 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 11809fa2-ec38-388d-adc4-261c0ac90884 | -3.45519 | -54.20434 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e8ec013-97cc-335a-afbb-6bd6b2b0713a | -3.45093 | -54.10035 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c984a28b-3c2e-3251-a1be-64f2dc640a02 | -3.44669 | -54.25687 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 546d7ea7-8474-3641-a4fa-ceb7dc6486d8 | -3.44252 | -54.25623 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9441bc0-7a04-37a1-a036-0a0eed92a2e7 | -4.50793 | -54.96128 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9f269939-af38-3243-8431-388a1c444356 | -4.34472 | -55.12985 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1800e7c-e8b4-3198-a81c-01778fffc30c | -4.22336 | -55.31366 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 245ac445-62b2-3fbd-8676-f9ba31c33ed3 | -4.13317 | -55.04316 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec230293-875c-3933-9ff5-ddd301598bbd | -4.11041 | -54.28515 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9f9ef9c-74aa-3ea2-ae3f-3d41d4874def | -4.09983 | -53.94132 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a60bc788-cd86-34a7-bce4-8dd86a67429b | -4.05603 | -54.28128 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7a6adc2-e74c-3da6-9ee4-2b650d897d3a | -4.05454 | -54.34162 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6d535b9-abe2-3844-996e-925fac576ed3 | -4.05086 | -54.11018 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40bdbd12-1d74-3f9a-bc19-d2ed7082ef72 | -3.99377 | -54.127 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26c4811b-bb87-37ea-9379-258d57913136 | -3.98851 | -54.1335 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f08f96d-947e-36d6-877e-13756bdeb09b | -3.9856 | -54.12567 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99430ae1-8895-3dc7-9d39-d36521dbf4f8 | -3.985 | -54.1293 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28026774-bc3f-32e5-9b97-85eac7ad3d78 | -3.97793 | -54.12132 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f791fb4-4062-3656-b343-08b4d8535699 | -3.93153 | -54.55916 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e5ab84-d672-34eb-938d-3a31a9e20e00 | -3.92336 | -55.38174 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25254d21-845c-39f6-83d7-fa73922f38bf | -3.8138 | -54.48409 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54d5bb0e-1902-3ca3-b064-e74fbdb8522e | -3.72058 | -54.46903 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59367bcd-e739-343d-aa3c-0d6763f7ff20 | -3.70588 | -54.42756 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1937e8b6-32f7-3f5b-ab15-4fe1b82c2ae0 | -3.69854 | -54.06857 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b397e03-5fd5-3e57-aaa6-8232119f029e | -3.69343 | -54.25762 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb536329-1acd-3e71-82d9-43995b51389a | -3.68866 | -54.26088 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35ae34c8-6bc5-37eb-ac77-bc9f197f2d94 | -3.67477 | -54.32076 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4f19355-f7a8-3297-bc96-475fbd158ded | -3.67061 | -54.32011 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e9e3d17-ce78-31ff-a405-f451414eac78 | -3.67051 | -54.21553 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7077e9c5-9317-3c47-ae64-5f0444ee7b49 | -3.66767 | -54.31192 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b90ec0a4-e799-389c-9d6a-47eaf178d492 | -3.66118 | -54.51279 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72f66976-2450-3ecd-ab2d-488defab3167 | -3.63836 | -54.68292 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b54c91a7-8ca1-3059-918f-45f8375df7d0 | -3.63819 | -54.67796 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e07fe664-135a-31bb-89ee-c35bc6d86ff1 | -4.4995 | -54.85392 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a601359-5684-3153-b1b1-e980fa5f260f | -4.35685 | -54.93466 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d956d3a-642d-3112-9870-60695dcfce58 | -4.3562 | -54.93871 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66542237-5589-3e6f-8621-51cd42016f88 | -4.29521 | -55.12341 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 049d194f-f8b2-349a-8a3f-9eca339d9d72 | -4.23064 | -54.88171 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cf5e36d-2dc6-3831-98b5-8c84d75d508a | -4.11392 | -54.28964 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85c68027-c83b-312a-a224-8a73a2f727b2 | -4.10979 | -54.28901 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a73752b-8713-3201-bcbb-05e95e761808 | -4.10385 | -53.94207 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55ce54ea-d8dc-3d78-86cc-008f51a4c601 | -4.10328 | -53.94551 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15176888-65cc-3169-bc6e-88392ed4e1e0 | -4.09926 | -53.94477 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e82defa-9870-3e6d-b077-079ad4a62304 | -4.09696 | -53.93373 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8a77859-c33c-3645-9766-3fcd9902a3b4 | -4.09235 | -53.93657 | 2024-10-29 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95186c40-e39f-3b62-8d63-7df4c4e838a1 | -4.07313 | -54.28027 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 686e745c-1884-3247-8b00-fd00faa612c9 | -4.01443 | -54.82344 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 883de25c-b98b-356c-b692-7b44ab7c1ed8 | -3.98441 | -54.13291 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb36d8b6-4c3f-3b95-ab95-6013fb7cdff0 | -3.97382 | -54.12078 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c66af96-6570-3066-b38c-30120608bd02 | -3.96311 | -55.38205 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 334089c8-10e3-33de-b998-7da33f2fb2bb | -3.92657 | -54.51051 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50fff2df-e038-35c6-b637-767f4bc05d65 | -3.92238 | -54.50975 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3891773f-0a44-3072-98cc-1d34f5fdbfc3 | -3.88664 | -54.14406 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd8d9266-1d3b-3f31-9b75-eb6e531034ef | -3.88254 | -54.14343 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f89c458d-e503-31c1-afdd-b4f20a2d3663 | -3.85384 | -54.76566 | 2024-10-29 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d692a2eb-dc43-3528-a998-5bc8200fc10d | -3.81445 | -54.48018 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc07ff45-965c-33b3-a362-b63e14419fd7 | -3.72119 | -54.46529 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89102702-463c-3de8-b603-8dde525d39ab | -3.7065 | -54.42381 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 845b7427-eafd-32ac-9e88-99c4300756db | -3.7023 | -54.42324 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25ed0198-19ac-30cb-97f4-e595b4fb9da2 | -3.69281 | -54.26146 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8b3dd62-e311-3444-911d-59ea9fff34a3 | -3.67122 | -54.31634 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28e84094-5693-3edc-ac1d-089733b491d5 | -3.66351 | -54.31125 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d1d5b96-f33f-3807-82cb-0b9c2423ea6f | -3.66161 | -54.51217 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89775ebc-fe69-3f76-83d1-32a26120c280 | -3.63899 | -54.67897 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c265730-a130-3ab4-870a-b058cfa440fa | -3.63754 | -54.68188 | 2024-10-29 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4af9331d-d507-3221-b9eb-1cb4f16fdb8e | -7.49921 | -55.36074 | 2024-10-29 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abb15756-8fed-3c50-a1c0-87a1d6a21d58 | -6.55544 | -54.95574 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac5ec68-58cd-32e5-9503-23e75a55d7c1 | -6.55479 | -54.95953 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d54a2ec-0fd9-3a58-a5de-215a0e14475b | -8.30704 | -55.11007 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8f72f9c-c11b-3b26-a6b5-637f3e377fa4 | -8.36972 | -55.15813 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 213a835b-4aaf-3024-b5e6-ae46760b77de | -8.3691 | -55.16176 | 2024-10-29 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91e3be3b-9e9a-3339-ac96-30e6a389bfb4 | -9.75344 | -55.33979 | 2024-10-29 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a80e3bd4-971e-39d5-8af4-5f9427fe9b98 | -9.75282 | -55.34335 | 2024-10-29 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e4bc9af-3a45-3c58-a6b6-a2e41bfeceaf | -10.08978 | -55.40318 | 2024-10-29 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c414e45-921c-317d-a277-c47d5e07db2e | -10.08934 | -55.1919 | 2024-10-29 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65dfb528-424b-3f82-b1c1-68514b4f4181 | -10.42677 | -56.26775 | 2024-10-29 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c915cbac-704e-3d60-88b4-8ea81d5cd272 | -10.4264 | -56.26685 | 2024-10-29 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cffcbcc-be79-3e98-9a36-fc10d2899379 | -3.62101 | -55.45367 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25b52db8-89e8-3509-83f9-04fb3b9722fe | -3.62303 | -55.45604 | 2024-10-29 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README66.md)
