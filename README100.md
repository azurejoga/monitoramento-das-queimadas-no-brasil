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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bf41269-1b28-315d-9033-c819b1430dad | -3.03713 | -61.67737 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc0b8908-81c4-3693-aa98-fb7f509e4ec2 | -3.03382 | -61.67685 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1a9adb0-fade-3c8e-a8c7-c47bedc0fb90 | -3.02012 | -61.69939 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9181dea-88bb-31ff-af60-5fc5efc42fe0 | -3.23595 | -64.40176 | 2024-10-13 05:27:00 | NOAA-20 | MARAÃ | AMAZONAS | Brasil | 1302801 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 40f71f3a-339a-39c5-8553-198dc10d81bb | -5.99249 | -64.82872 | 2024-10-13 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d2ad16c6-fb9f-3d2e-ac62-a2a6d23bcad1 | -5.98895 | -64.82815 | 2024-10-13 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a8589cc-cde3-3f83-8a69-2bbac3e2b8e6 | -5.98669 | -64.81953 | 2024-10-13 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b04dcd2-6f90-395b-8df1-6ff00876b098 | -6.81556 | -64.33004 | 2024-10-13 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eea8e9d9-f201-3692-9282-470b753ca27c | -6.81212 | -64.32948 | 2024-10-13 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91162e3a-0be0-383e-83df-7710e40d89f3 | -6.80928 | -64.32513 | 2024-10-13 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c801d258-71ab-3327-a33b-2208a1d37aaa | -6.80867 | -64.32892 | 2024-10-13 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 058e179e-16a7-3502-92b2-03dd0ab2d389 | -6.80584 | -64.32458 | 2024-10-13 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 59948fcb-0331-3625-a002-b6d5b15e14b6 | -6.8024 | -64.32402 | 2024-10-13 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f68dafc4-b4b7-3a3f-9d16-0be2cd91e622 | -9.40817 | -64.45968 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d41165b-235f-3396-9c53-d93cdb7c9bcb | -9.40758 | -64.46337 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23944d19-7500-3713-a172-f3fdbef0e4c6 | -9.40419 | -64.46281 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a8b6473-2c4c-3e69-97c2-8d307f0dd490 | -9.38047 | -64.45883 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99885d17-4e9a-3b1b-87f8-ad1bf9f0a70a | -9.31462 | -64.45229 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8eecbb40-e1db-3487-945b-28d9b170902d | -9.27754 | -64.48775 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea46b455-80a4-3fcc-8c72-fd9c4b1e9217 | -9.27695 | -64.49146 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 222423d5-2a80-3f87-b4c7-caec60fc5b03 | -9.27534 | -64.47984 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab4fa65c-bb71-3469-a397-02022710606b | -9.27474 | -64.48351 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6efd1c42-d13a-323a-8ba3-943295e1a6d1 | -9.27415 | -64.48721 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f05fc12e-de1f-3def-bde3-4cf43688cd5b | -9.26034 | -64.37931 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b3c070-6f8d-3655-9e81-777bf3dbb6b6 | -8.9987 | -64.40911 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb26144-d6e1-3625-8710-00d4696868c6 | -9.83729 | -65.0588 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7a2fa38-7827-3077-9ca5-f717452428f6 | -9.83384 | -65.05822 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13cade12-74dc-3267-98d3-4a9e847101cc | -9.79185 | -65.05514 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bab09949-c521-3add-a6ad-a92020f4769a | -9.79121 | -65.05895 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59fd69eb-da53-35f2-be55-45836e854a56 | -9.7836 | -65.04623 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 412bd498-affa-3c6c-860c-8cf35f1b287f | -9.73097 | -65.06493 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 558dce52-895b-33f8-8724-ec344230164e | -9.73034 | -65.06874 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 848ee249-e8e0-3f8a-9455-2404ac885b29 | -9.72814 | -65.06055 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a5b186e-7491-31ed-b8dd-bef181b869c9 | -9.72751 | -65.06435 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acc83cdd-54f4-3770-b1f9-b7071e7c035c | -9.72689 | -65.06817 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7889fef-2ff9-3edc-b88f-04b167f05f23 | -9.72406 | -65.06379 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa4123de-bd95-3b33-ac70-ded0663db291 | -9.72344 | -65.0676 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd088205-f01c-31f3-811a-76d64d503316 | -9.35794 | -65.74326 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2550efa3-9d91-3768-9db3-4d3f96a207e6 | -9.35726 | -65.74732 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 39490a42-98fd-33e3-b0a4-fbf8cd46fa1f | -9.35437 | -65.74266 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a73e001b-51ed-30ba-a7dd-d37397b690b8 | -9.35369 | -65.74673 | 2024-10-13 05:27:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0d2aaa1-239c-33b0-8432-47afa223eac3 | -9.98999 | -64.78902 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb88e9ee-e651-3ad1-977e-e91dd74c5ddf | -9.98658 | -64.78845 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 646f6e08-ce4d-3f0a-ba56-c36c844a904d | -9.98597 | -64.79218 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 240a0681-70b8-3e44-baf6-a0fe24d34095 | -9.92159 | -64.77826 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96e1c9e7-d694-3edc-b85b-3ae974e9b58c | -9.92098 | -64.782 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c7b6022-f7b2-3b6b-ac51-5b00288cc6ef | -9.91818 | -64.77769 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a7ad5f3-8681-3473-84cf-532b01d59951 | -9.91717 | -64.76223 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 688cd12a-acb9-3462-b574-1e99be581fe4 | -9.91657 | -64.76595 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16f90151-b8e8-3815-99c5-eae30f946c02 | -9.91476 | -64.77714 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d955decd-9da9-3fd2-b048-aba477d0cd72 | -9.90342 | -64.89077 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65b80ce5-ad0f-3a41-977a-e65b23d196c5 | -9.89665 | -64.82407 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2e06892-944e-34dc-bdd5-db945c268d7b | -9.89004 | -64.79995 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9beca28c-4c77-3ed2-a3e8-b57663a24d2a | -9.88943 | -64.80369 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c42da81-a2f8-3443-a600-1f43ca1b7ccc | -9.88883 | -64.80743 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 133d9127-dee5-358f-ae49-70b15a1b6680 | -9.88822 | -64.81116 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bcc9586-a18c-3c4f-ae64-1a20cdc822cd | -9.88761 | -64.8149 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e0b1e8d-3974-3abf-8f00-f7dada7b49de | -9.887 | -64.81865 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69cb88fc-18da-3c79-9660-e34f00446339 | -9.88541 | -64.80686 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22506b74-72b9-33f6-9b0d-23074f34512a | -9.8848 | -64.8106 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba0c0956-bf60-3c76-9dc8-4c6c3cab5dd3 | -9.87552 | -64.93259 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d25a2cf-5adc-34cc-babd-cc2b9ddc2afe | -9.87209 | -64.93201 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95c04973-b3ba-3e0e-99cd-eb8678d250f8 | -9.79564 | -64.99351 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55a7d620-f58e-3c6d-b3c5-380d56a39dfe | -9.72861 | -64.88514 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdc20b95-ec5e-3ba2-b04c-3dd10eb61d25 | -9.72518 | -64.88457 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4d45da8-6e09-3ba1-aeba-8e6f9321c9c1 | -9.64525 | -64.94579 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0745c33a-4c21-30db-8f55-b85f97a1208c | -9.64339 | -64.95719 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b083d74-9558-332f-a15f-30d4572baa88 | -9.64057 | -64.95282 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44d0a5b2-583e-31e2-b496-553e63e973fa | -9.63995 | -64.95661 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf856b80-b799-3ec1-87f9-30ba081e38fd | -9.63933 | -64.96042 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5449ec0a-c745-3909-a367-81404df2f61d | -9.63713 | -64.95225 | 2024-10-13 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eca7728-0b59-39f6-be82-b3f30cbbf7e5 | -8.11222 | -71.33585 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09e9f7aa-9bf8-3abe-a9d5-d0b5040ca10e | -8.11165 | -71.33903 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4a0c866-efb6-3294-b9ea-05090de83ea1 | -8.10647 | -71.33803 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 738a3487-9165-355f-8aee-3714e5328690 | -8.10591 | -71.34116 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6211bcb9-be05-37b3-a943-aa31a43912d0 | -8.03064 | -71.39797 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f31936f5-6c6f-37bf-ab6e-6f2a7059a984 | -8.02599 | -71.39383 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17834702-baf0-3be8-94fb-f573aec7ecce | -8.02543 | -71.397 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57d00412-0187-3814-b569-380921cb005d | -8.02487 | -71.40018 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a262445a-e421-3be5-8888-12edd96b8876 | -8.02078 | -71.39289 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11a38ad3-0ea4-34ed-8f75-32923f94c572 | -8.02022 | -71.39602 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a33cbbe-339c-3f5b-bf22-e2280010a33b | -8.01966 | -71.39919 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a08dc71-148f-3b19-8283-e2a1aed1f18f | -8.01035 | -71.39098 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 489b1890-e2ba-37c0-bc35-e64d4da9a46f | -8.00513 | -71.39006 | 2024-10-13 05:27:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21984ad8-1566-3e89-a5e4-eb7de0c0499e | -7.33819 | -72.90305 | 2024-10-13 05:27:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf7be2d4-b78f-345e-abfa-81c5440e5821 | -7.33777 | -72.90251 | 2024-10-13 05:27:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82d4f207-50be-35a2-8a9f-d9ee3024ba5d | -7.33744 | -72.90723 | 2024-10-13 05:27:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 963164b7-cbf4-3292-b4ef-efae54ac51f1 | -7.33699 | -72.90667 | 2024-10-13 05:27:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 376a4212-61a6-387b-9611-b9b68c580912 | -7.31901 | -72.64562 | 2024-10-13 05:27:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2001934c-e6d7-375e-9c3b-e38447d663d7 | -7.31827 | -72.64967 | 2024-10-13 05:27:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36b5f28e-b642-3c6b-8af9-f7716ccaaee0 | -6.97706 | -71.77374 | 2024-10-13 05:27:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c1a467ca-a0cb-32b9-97a5-3fa2925f0f10 | -6.97644 | -71.77726 | 2024-10-13 05:27:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 42eef2b8-6f65-3e83-a62d-d2248c41cc91 | -8.00735 | -72.32362 | 2024-10-13 05:27:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b07f936a-c07f-3cce-81c2-5e3000d5836c | -8.0018 | -72.32261 | 2024-10-13 05:27:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6e4764a-609c-3343-be99-edb962ab09f4 | -10.0159 | -67.17825 | 2024-10-13 05:29:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ea86569-e748-36e3-9ded-3f37da5921a5 | -10.8007 | -68.34928 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e519553-81c8-3f13-a5b2-9090a6f0110e | -10.79665 | -68.34858 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca5b8060-cc1e-330e-9e9a-75579efcc42c | -10.64363 | -68.60113 | 2024-10-13 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c54c6ae9-f4ae-3627-b099-732e1d3929a5 | -10.52277 | -67.88308 | 2024-10-13 05:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a5ae023-e905-3b96-b366-7b8f9a54b53c | -10.51995 | -67.82943 | 2024-10-13 05:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README101.md)
