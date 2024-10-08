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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19e4d4cd-ef59-36d0-ab57-b5de8f03126f | -11.25937 | -60.39289 | 2024-10-08 06:16:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba444a27-62d3-3344-aff2-c25359266933 | -13.41082 | -61.93416 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75078706-c77e-3fdc-892c-063d273d8bc4 | -13.40864 | -61.92249 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d2a5b10-9a2d-33d7-87ff-bd5d642ffe7b | -13.40798 | -61.92849 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a20dd662-1cbe-39a6-925d-6a0d7bbe4222 | -13.40733 | -61.93441 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d3f0154-6d27-3839-a669-c6ca78fd88ef | -13.40474 | -61.92741 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 788a8469-6392-36d0-8943-e48e20ff073e | -13.39682 | -61.93853 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41ac9bd1-51f5-3333-ba7f-4d12fe9f4f79 | -13.3933 | -61.9388 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f13e23d8-da68-35b8-b002-f46691f016e2 | -13.39075 | -61.93169 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6fe13cd4-43cb-36ab-b895-b822b7b2707f | -13.38726 | -61.93201 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0731ee84-57a0-3ad4-9604-0b392de5cc64 | -13.38406 | -61.9309 | 2024-10-08 06:16:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4828fe51-f868-3523-ab6e-7d8b021f1bf1 | -9.74525 | -62.33317 | 2024-10-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4d474ab-da92-3407-a88f-cad99518ed27 | -9.7446 | -62.33833 | 2024-10-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bc4a3438-5515-3f86-bab9-102b92fff941 | -9.74283 | -62.3358 | 2024-10-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9179932-9ecc-3cc4-8779-a811c736bcdd | -9.74222 | -62.34089 | 2024-10-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e42b3e97-5bfb-333b-8c72-3b6e93e4c367 | -9.65198 | -62.42186 | 2024-10-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a24c0c1-6bfb-3623-95f5-7b9d9d6a0ae1 | -9.64685 | -62.42106 | 2024-10-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d934cadc-d8f1-31be-b5dd-4f9200c53d4b | -9.64579 | -62.42091 | 2024-10-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 464348e7-8d0f-3f74-b336-dd0531f31d31 | -9.5334 | -62.38008 | 2024-10-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e95adfb6-b31f-3cbd-adfd-8c513e251b3b | -11.88677 | -62.76949 | 2024-10-08 06:16:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33adaa7d-463f-32df-84d2-670acca9c0b7 | -11.88619 | -62.77446 | 2024-10-08 06:16:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89825fc8-0aa0-3e77-95d7-104f9d99b0e7 | -11.7675 | -62.88465 | 2024-10-08 06:16:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e9b9b21-d1c5-3b18-a58a-556895c3c150 | -12.85489 | -62.80227 | 2024-10-08 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38452695-ceae-3e0c-a04e-e2ad9b495741 | -12.82807 | -62.46148 | 2024-10-08 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ea5aac8-d10d-3da6-b66d-685159df6a60 | -12.82676 | -62.46184 | 2024-10-08 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 34945981-f515-3a4d-956f-2f4130970301 | -12.82163 | -62.46064 | 2024-10-08 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fb296a78-0221-39f8-a6e8-b7e8916990e6 | -12.82032 | -62.46104 | 2024-10-08 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 15bf4762-14a9-3fee-970c-19ffb3224edc | -12.75053 | -62.26279 | 2024-10-08 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| af14f2d6-a723-3c03-8b07-7027979be587 | -12.74992 | -62.2684 | 2024-10-08 06:16:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bd60f3f-f286-3a1d-bfed-a9443255fffc | -12.45745 | -63.00399 | 2024-10-08 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f9febee4-46cc-3050-a27e-a87d720ae67c | -12.4569 | -63.00888 | 2024-10-08 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1a4f246a-7f4a-34c0-937b-29a14445d676 | -12.45125 | -63.0032 | 2024-10-08 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cf317ada-ea4c-3b37-87cc-fd1fc9798ac9 | -12.4507 | -63.00807 | 2024-10-08 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d022c743-3f3e-30f2-95f0-9e12f32f7b66 | -12.44961 | -63.01786 | 2024-10-08 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 014ef037-4cae-3596-9a07-4c93cd0135a3 | -9.66833 | -63.12867 | 2024-10-08 06:16:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a866a91a-9468-3547-81f9-58d7abf09b20 | -9.66601 | -63.12744 | 2024-10-08 06:16:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1032bf0-b970-31f1-8a8d-51074e43e3c2 | -10.90125 | -64.16026 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| adec4075-a227-3b2a-982f-6ad95ae5e0d9 | -10.90083 | -64.16369 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 154b318d-7d2b-34d9-ac40-0b6c7ac7c41f | -10.90047 | -64.16675 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 21be4073-534a-305c-bf26-fa229a330bdb | -10.89764 | -64.16181 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 779b845b-0b69-3b3e-a6a9-dc35556ab2bb | -10.8972 | -64.16525 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| da169517-3333-3abd-ad9d-5e5f6af34932 | -10.89572 | -64.15842 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2c4ced97-5ff8-3f0b-b2fc-96b9484aa674 | -10.89525 | -64.16241 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c9d4b89a-5f34-33ca-a945-c93b3b5ed6bf | -10.89482 | -64.16594 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| cacb0d2e-9543-3153-b021-51ea60cf9ed2 | -10.89385 | -63.91427 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7df107f4-d2ba-3bfc-a987-9cd24c001ecc | -10.87769 | -63.90338 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 000cac88-b997-3a28-943e-b93f33bf6579 | -10.87714 | -63.90785 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6704a15-5b90-3f39-a49c-494ba207a745 | -10.87252 | -63.89792 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b9a5b2e-b35c-3c37-bc7f-0566fc127f4c | -10.87203 | -63.90195 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8bf5b85-5a33-35db-8f60-1c6940cbb4fb | -10.87148 | -63.90648 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6f1ab6d-3203-3df8-a026-992998ac6947 | -10.86525 | -63.90973 | 2024-10-08 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59a6bd33-aa19-307e-bc7a-3d1d8ea9c8d3 | -10.86471 | -63.91418 | 2024-10-08 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76b260ed-d04a-3930-b9f3-7c97609a09f1 | -10.83862 | -64.22171 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a5d223c-8c45-38bc-96e8-ae8bbbe432b5 | -10.83818 | -64.22527 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87580646-5a77-3bb2-9015-f0797dc96b4e | -12.19429 | -63.66352 | 2024-10-08 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c28bd1aa-ff07-32ee-97bb-1900c8ac3215 | -12.19377 | -63.66798 | 2024-10-08 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e2a5d17-4020-3172-a559-3afe50727da8 | -11.6869 | -64.01077 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ad8e1f4-cfab-3a2a-a8a2-1b7bddf78bb1 | -11.6861 | -64.00935 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d953a377-e8cb-39b6-bb20-6294b2c39b1b | -11.68563 | -64.01306 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc777629-e9f5-38d3-b6a4-7405149f5e61 | -11.68152 | -64.00669 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c49223bf-7bb6-3898-bf39-3029b3f9aeb0 | -11.68112 | -64.01013 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b41fda79-6f47-3611-9ef7-a4847ddc5063 | -11.6803 | -64.00885 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9552fca-9024-317d-862d-93978e3c5829 | -11.67987 | -64.01229 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c52123fa-d5ef-37e6-ac2a-a5d369bedde9 | -11.67155 | -65.21246 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 421d8d5b-e784-3ed9-9a5a-73fa7af4d7f1 | -11.67114 | -65.2158 | 2024-10-08 06:16:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ead2e3a-738a-3f23-a763-728b4b7034c7 | -8.47926 | -72.79497 | 2024-10-08 06:16:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92d45de2-f743-3dc1-b0c9-03518758d086 | -10.8924 | -64.1813 | 2024-10-08 06:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| d3583435-6f19-3f6c-a093-228df4d906ca | -10.9112 | -64.1615 | 2024-10-08 06:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 975a0854-b75a-3497-8bc2-66343cf5d35d | -11.673 | -65.2062 | 2024-10-08 06:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 68e5f2b1-5d8e-3e99-a712-71293818e433 | -10.9112 | -64.1615 | 2024-10-08 06:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.0 |
| a699595c-e8d6-3cae-a5c6-4532e475caaf | -10.8926 | -64.1434 | 2024-10-08 06:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 38fcff1d-8069-3653-b6b7-7a77437eb5c7 | -10.8925 | -64.1623 | 2024-10-08 06:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 209.0 |
| a990aef2-8cee-31a6-a7b0-2199ace3f13a | -10.8924 | -64.1813 | 2024-10-08 06:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c9918064-d006-35e5-a003-149e6b01f1c6 | -11.673 | -65.2062 | 2024-10-08 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 37a64d2d-7ea3-397b-9852-cd9f1d3c5bb1 | -18.6192 | -57.2603 | 2024-10-08 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.2 |
| 5401f616-efba-3d4b-8060-b6cfc731983c | -18.6195 | -57.2396 | 2024-10-08 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 70aeb639-a351-377f-8330-decf6c176fa9 | -2.43788 | -66.47348 | 2024-10-08 06:35:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9780df53-bcb7-33e7-a371-fcbddcc55bdc | -2.43788 | -66.4729 | 2024-10-08 06:35:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dfb4a2d-e039-319a-be5f-6abf27b577e8 | -2.43139 | -66.47251 | 2024-10-08 06:35:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 075e6324-81fa-3c13-a7c1-d30f2884bd03 | -2.43058 | -66.47718 | 2024-10-08 06:35:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15e9a2f6-b24b-3139-b7b4-b45d95881d6a | -2.43706 | -66.47817 | 2024-10-08 06:35:00 | NPP-375D | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f548428-3cb1-3f84-80a4-0e9db59bf3ef | -10.8926 | -64.1434 | 2024-10-08 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 33e15eea-9924-39da-8346-9ac54dd338c5 | -10.8925 | -64.1623 | 2024-10-08 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 90fa28b3-3ec5-30c7-a621-1883a1080e49 | -10.8924 | -64.1813 | 2024-10-08 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 275f6f38-5b6f-3be8-97a9-b042cdd87454 | -10.9111 | -64.1805 | 2024-10-08 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| f542c65f-c41b-30b3-968f-05e08678122d | -10.8755 | -63.8979 | 2024-10-08 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 397a51d0-f0ca-3f7b-81ae-d3f8fd41a8a5 | -10.8754 | -63.9169 | 2024-10-08 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| b6ec72c6-4304-3b9c-9130-fe0833a90c7e | -10.9112 | -64.1615 | 2024-10-08 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 75582b30-e6bf-3778-9e71-c9c4c97b3beb | -10.9113 | -64.1426 | 2024-10-08 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| bf1bd32e-2d96-391c-b458-67ddfc776274 | -12.4414 | -63.018 | 2024-10-08 06:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 9ed1d9e6-df24-3c5b-a857-1a913749e45b | -16.488 | -57.7205 | 2024-10-08 06:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.5 |
| 9c87e381-b6b6-36e6-8e24-140a94edf3b8 | -16.7852 | -57.422 | 2024-10-08 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| f5e8a39a-6841-3f4f-8468-b5a483116188 | -16.8048 | -57.4197 | 2024-10-08 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.5 |
| b9ec618e-a044-32f4-bcb3-698f1ef7e933 | -16.9211 | -57.4881 | 2024-10-08 06:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| bb19ef22-11c1-37e7-ab46-8ddac62c0cea | -16.9407 | -57.4859 | 2024-10-08 06:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 8bdf77ff-c55a-3bb1-928a-219775cfda25 | -17.0881 | -56.8328 | 2024-10-08 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 6b8ffcf5-0850-3750-807e-932a3ec07539 | -17.1074 | -56.851 | 2024-10-08 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| df48a6a6-a426-3f8f-8666-cfc9695226c0 | -17.1078 | -56.8304 | 2024-10-08 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 083588af-5cf5-30e4-8e53-661ba67ae765 | -17.1471 | -56.8256 | 2024-10-08 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.7 |
| ab8c6e9d-355d-3814-af9d-e83544431129 | -18.6192 | -57.2603 | 2024-10-08 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |


[Clique aqui para ver as próximas entradas](README132.md)
