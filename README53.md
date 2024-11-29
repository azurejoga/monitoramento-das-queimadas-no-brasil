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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73873495-6e0b-345d-940a-d527dfa75a05 | 0.95191 | -50.75841 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e74877a9-0f24-3263-a395-c1e9844260b3 | -4.1185 | -54.2385 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a0e35c7-8438-3bfb-9630-899056d684ee | -1.24123 | -51.61708 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25b1b7e7-3073-3298-baeb-c1e62f773ad6 | 0.98303 | -50.25629 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be5c24a5-c5fe-3ece-a5ce-5db344a128ab | -2.70518 | -51.99821 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 90a2941e-c776-3258-bc3e-0a9f216f02a8 | -3.17631 | -53.84738 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db973274-1631-3cc1-b924-ee5a64d7e6b3 | -2.5292 | -47.4051 | 2024-11-29 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c76d0b0a-5deb-3b99-91f4-e85c203362c9 | -3.53757 | -54.08358 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e546af-ee40-3678-b05d-d13d4fb4abc9 | -5.51074 | -46.25549 | 2024-11-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4071ccb-8d20-3e41-a463-d582aa098c8b | -0.76674 | -52.4595 | 2024-11-29 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97e1c1af-03aa-3f5b-8770-ad9e65a23a2a | -1.0733 | -53.63333 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f9176d6-ac22-32ed-93b0-f4d5c988f27e | -3.04114 | -54.03707 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43e419dd-1be9-3365-ac69-f2ca0b916e9b | -1.57143 | -51.18674 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7fb4244-a775-3a3d-81f5-9d3e71a57669 | -1.63586 | -53.86622 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36b6ae56-e18c-3f82-8a62-da4271e0cc02 | -3.38455 | -50.10537 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4999cba-bd7b-3f24-9c8e-299bd2495e24 | -1.34434 | -52.13354 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26e60bf0-b7a8-394d-9729-ee7fdcbf1e01 | -2.26196 | -53.472 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc3cdecd-fce4-3cbe-9cec-720820b72f34 | -0.14088 | -54.5966 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e00be171-470e-30de-afe9-6f5236eb3a3f | -3.96391 | -48.08115 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7da67db1-d908-3a49-a23e-926044e43e3d | -2.86836 | -54.03138 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c08d4fc-a392-3d92-9431-77df6f2ecc80 | -2.77206 | -54.06237 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2123df16-4021-38a5-aaa8-c0f0fe3c7e59 | -2.23152 | -53.68866 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f528030-5fc3-39b7-be6f-36858208a2ef | -2.85621 | -54.02246 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0952ffeb-9524-34e7-8d31-a8ded2945799 | -3.92205 | -53.66873 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 939aa092-ea9d-3295-83b6-7fdea501f9fb | -3.49622 | -53.80273 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20449b11-d880-3eb5-a555-e80795f3d623 | -1.41139 | -51.58652 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 778e607c-af53-325b-a5cf-c0f916eab87d | -1.18559 | -54.20038 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1ecc665-0455-3b68-8a5d-7072954143aa | -2.76858 | -52.90541 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8749bff7-1c6e-39be-8582-4953f66eec57 | -3.67412 | -54.44765 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 834e4000-8b31-3644-a6d6-3fa391e188e6 | -1.35038 | -51.38991 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4ea106e-9159-3b6f-9725-4165585ebcea | -3.69066 | -47.13897 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aca7cf8-33e2-35e6-bc70-f3b855267ef0 | -2.85322 | -48.10064 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 174bfb18-7863-3be0-99f0-9d6236a2f1ec | -3.85049 | -50.69266 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1b19530-7189-388f-a535-3e02c1cbd19a | -3.23595 | -54.22673 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80e68487-428f-3b45-8c4a-94ad88b4fe07 | -3.16883 | -46.30392 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfe38757-c641-33a3-92b2-2321ca96f5e6 | -2.5978 | -54.0877 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6c904fa-b28b-3a1e-8f28-9777d0cd4f75 | -2.82153 | -54.59214 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5186504f-a4af-3095-b14e-7dca931f2f1a | -2.10167 | -50.34288 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d710f93-0ded-3210-bcdc-2cf2d9173af5 | -3.02089 | -58.60732 | 2024-11-29 04:57:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fafb17e0-4602-3810-8aff-0e09b688841c | -3.28189 | -50.04149 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3a9433fd-63dd-3e5b-9b87-707b76c35f6f | -2.97646 | -53.29525 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3292d6c-a9e1-3bdf-99d9-258ce7990f87 | -2.01271 | -51.1861 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 703ea92b-c97e-32a0-ae7a-05a236dc90bc | -3.2426 | -50.76741 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 760531d0-a942-3804-8218-13dcfede1116 | -1.66342 | -52.24768 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6169642-76e6-3fcf-87ae-b25fb21b96c0 | -2.5288 | -54.137 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abfc0f3f-f637-3a60-acbc-d0ad0354e236 | -1.19463 | -51.76139 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e965a07e-1be0-3d2f-81de-2880f9abdc5c | -2.73208 | -54.40338 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1be76749-17e8-376b-9268-e1bcd9668101 | -2.80446 | -54.02858 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9fe3349-068f-35f6-a808-f89d0cca25a6 | -3.04982 | -49.51923 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 13209580-5c51-369c-9763-931b4c9b82b4 | -3.31672 | -53.75316 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c902eaf-490a-3a7c-8f4b-d7f59192352d | -1.53806 | -51.19701 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c20d9bf-1099-3d78-a87a-50d32dc82912 | -6.00538 | -45.75819 | 2024-11-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bda58d7-ffd3-3f1b-b68d-f9d2b0f0305f | -2.81999 | -54.05917 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7391f2f5-3b03-3273-9112-a40b01cccb21 | -2.94962 | -60.02163 | 2024-11-29 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b9a80ea-934d-3e04-95a2-feccde83019b | -1.08435 | -53.38907 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 250f8415-89c8-3519-9441-8f2867de3616 | -4.1801 | -46.84175 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95d84292-cdc6-3882-afcc-1d6fe1cfc84a | -2.83438 | -54.0755 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7783b2b-f0d4-358b-b1d1-fead18d9996e | -2.03656 | -53.49974 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cc0cd71-d66a-3396-8a56-af7ca265f559 | -2.84492 | -54.09478 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfbc45b1-ebf3-3aa9-8f6d-844ef8f2c3d2 | -1.95941 | -49.53205 | 2024-11-29 04:57:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f0a0e69-b237-3a9c-be50-ec25dbc7a444 | -1.3145 | -51.75735 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c70d4651-f749-3031-9267-14edc2f44f31 | -2.2691 | -53.46959 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71cd5f4f-e7b0-3f63-9f33-fb469bd7a138 | -3.57964 | -52.06022 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94408aa1-22c1-3263-81bf-82f4582e0d56 | -1.64513 | -52.73741 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4554190-b189-3bd4-a423-e83accca541d | -4.09457 | -48.48459 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8729c719-de5a-36a9-98f1-7f3341c3d44c | -1.92505 | -52.88373 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3577e505-fca3-308a-91bc-1500fc6844d0 | -1.69631 | -52.47512 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5836df02-5f3e-3bb0-ab95-435b70029dc5 | -1.63457 | -52.71808 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd6c030d-97ec-3076-ab2f-4b78846688c8 | -3.0964 | -53.2679 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43aaf6c4-1fb2-3eea-a3e1-c6f0bb2ac207 | -1.50426 | -51.93692 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5ad8d8d-170b-3a3d-aab0-7a673dba4bbb | -2.05831 | -51.18923 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52c00c9a-ccf0-3ef6-b36d-c0edaefe8de1 | -3.0761 | -53.28947 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32253737-ad9c-34fa-9f7d-31da94fd5033 | -1.66595 | -52.51684 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb89b9c5-0af0-3753-9122-bf67616532a6 | -2.74195 | -54.03578 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dd43d9e-f76c-3cc9-b2e7-d416586dd427 | -3.24811 | -50.58776 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e6d8a8b-d040-345a-a3e7-51b52860abb8 | -3.26473 | -49.89077 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44317b79-bbaa-308c-a38a-c24e37d1b39d | -2.72965 | -54.13627 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a988153-8f85-35d3-ba62-d25d58dd29a9 | -1.0616 | -53.00994 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb790169-e2c3-3dfe-9d54-9c8f2fe044f1 | -2.60718 | -54.24476 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 576ff83e-5687-305e-aaf9-b81a41762926 | -1.7055 | -52.63383 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 266948c6-29d8-3cb4-bdb4-c50bd07cd985 | -3.10668 | -53.26956 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b55efb79-e3f2-304c-be39-612a02f8bf06 | -3.56067 | -52.29464 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d64a3010-3fc0-3a1f-b823-82be1494f60f | -1.78515 | -52.73473 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a986fac-37e1-33be-bd2e-238a51d77f3a | -2.83091 | -54.03267 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41c64593-cd04-37b6-9677-9f94be5cb232 | -3.63811 | -51.02183 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e75618e8-e46d-3e97-ae51-eeb90981a3f3 | -3.0323 | -54.02866 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e61c5786-ed73-3441-8884-a9c72ad5d0ca | -2.83476 | -54.02973 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d88c194e-9442-3e74-8ba6-dca3160d9582 | -2.76618 | -54.03246 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e04a607-9d43-33d0-9ff2-30ca4b106d4c | -1.21434 | -54.1689 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2ed3457-2f01-3275-8d0d-1b21949eff04 | -2.80697 | -51.58932 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf9aebd4-36c6-3016-8103-481b24d03b0d | -5.53306 | -49.60525 | 2024-11-29 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ea6575d-3def-38b3-9613-df4a83c3c8e3 | -3.09801 | -53.25757 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6805813c-b633-3aa5-a21f-ed3e37c59545 | -1.35385 | -55.39462 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d705a947-4e53-3830-bb1e-11802447c4e2 | -3.6965 | -51.37138 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c6b2d90-145c-385a-af75-9e85e8ec4949 | -3.16274 | -53.23583 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58384816-d3ff-3235-aeea-58b643d4ab3d | -1.09256 | -53.3798 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b679c2be-68bd-3fc2-a91b-4800778b4ff4 | -2.44292 | -50.52029 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9028df29-fcf6-3f60-a0d9-49df195ec1d6 | -3.71216 | -51.81556 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12fec470-9aa1-3a76-a8be-2ad618865b58 | -2.85596 | -46.82113 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73d19f8f-8b26-3614-aaf9-5e843f6698ec | -1.39226 | -52.57088 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README54.md)
