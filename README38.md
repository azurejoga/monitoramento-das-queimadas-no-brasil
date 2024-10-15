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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a3dd787-e0d0-33a3-a4bb-dec2e7f675bb | -1.13034 | -54.11381 | 2024-10-15 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85ba8f34-98f3-3627-97ce-a1620a8f6b99 | -1.12498 | -54.11282 | 2024-10-15 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca598de8-1d2d-333c-9dd8-85181eb101da | -3.12493 | -54.22851 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ed2008c-487f-3149-9e89-48b05291f608 | -3.11967 | -54.22767 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5f453f45-73fe-32cc-b24d-1f6f68c25d83 | -3.11915 | -54.23085 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2dfd106c-157c-33b5-9b7b-1946096f486a | -3.11813 | -54.23706 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09bfa08a-4c55-361d-83a6-d591ba830dd5 | -3.11807 | -53.74016 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dde98e0-6eae-366b-973e-97599b91fa5b | -3.11759 | -53.74312 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac17eb8e-ecab-3a71-a7ab-a700c9ae041a | -3.11499 | -54.22338 | 2024-10-15 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9519dbf-eecd-3a94-b183-313e2c3185c3 | -3.11445 | -54.22668 | 2024-10-15 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eb1a33a2-c0c9-3a74-b953-247273ee97af | -3.11347 | -53.73636 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41d8c6f1-77f6-3551-a6eb-36e9b2203f8c | -3.11299 | -53.73931 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1407ec09-08cb-38ee-a98a-badc14e311d2 | -3.11251 | -53.74226 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 196ea953-af0a-3b2a-b900-c4d6e6b6dd78 | -3.11203 | -53.74522 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f9d4d2e-20de-3cd6-9938-9bca850f8742 | -3.11199 | -53.734 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d2a816-93ef-3fb2-8f17-1dbc09455f15 | -3.11149 | -53.73694 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 305c6531-298a-3e5a-8313-ef1c77b49e76 | -3.11048 | -53.74284 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0277973-e378-3d59-9e6f-5df844c5ffd3 | -3.10792 | -53.73845 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d96ceff-e51d-322a-a0a2-782343d44c5e | -2.82743 | -54.04671 | 2024-10-15 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a79dee6a-bb54-317f-87b2-4de666e481b0 | -2.51909 | -54.25639 | 2024-10-15 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc49099-78db-3e2c-b4d8-f55ab132085c | -2.51851 | -54.25983 | 2024-10-15 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39612460-f347-3481-ba57-574433c1e109 | -2.25651 | -53.76322 | 2024-10-15 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17ec0cd7-b8a8-30b5-9ed7-888027d12c78 | -3.5881 | -54.66863 | 2024-10-15 04:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 646a5a22-da62-39a6-aea0-25433d3f214b | -3.42673 | -54.66446 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e04f9e-5e10-32e8-a73a-d4f5443e9737 | -3.42615 | -54.66788 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e76e2007-0f2e-3e1d-871e-d0b73c4a3cb6 | -3.42557 | -54.67134 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68f07b56-cc37-3edd-8b3f-7b18b7364b8b | -3.42495 | -54.67497 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51d4503d-e376-3736-87dc-9ff7269b0a11 | -3.41956 | -54.67413 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5c06de7-f128-3e0b-b64e-20d5cb6d3e36 | -3.35091 | -54.80827 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc0f089e-1952-34dd-b64d-1d3a912de846 | -3.29465 | -53.84532 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 63064c98-a5d4-391f-af49-75850432bc42 | -3.29416 | -53.84832 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b027dfe6-f2f4-3f50-bba5-2bb0212057c2 | -3.12863 | -54.23884 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d873c2e-1b36-37c4-83cf-ab474214f545 | -3.12811 | -54.24204 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 551d5bbf-e351-35b0-b01a-55e9b63e189a | -3.12441 | -54.23167 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 018fad20-2084-3441-8056-b8bcb4960d76 | -3.12389 | -54.23482 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50e6a5e7-bc69-3bb2-a974-62416b22c5bd | -3.12338 | -54.23795 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff1b4ba7-e28c-3ea7-b192-500b4fc3d1c7 | -3.12287 | -54.2411 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7ac5a08-a6b2-3447-9d85-82c6400c10ae | -3.12113 | -53.74157 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b04467ba-367a-3ca8-9d49-238f824d7f71 | -3.12074 | -54.2212 | 2024-10-15 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 982de6ac-3a44-3d13-a042-f7e6a84fda2d | -3.12021 | -54.22443 | 2024-10-15 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 37f98704-147e-33d1-a599-49d32b65f2f0 | -3.11864 | -54.23396 | 2024-10-15 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f28ddfe-f303-397b-a43c-600c5693950d | -3.11656 | -53.73777 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2874e8a8-d208-37aa-b2b3-a16645835940 | -3.11606 | -54.21686 | 2024-10-15 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c413198-39c8-3b74-b72b-81718d2e0c36 | -3.11606 | -53.74072 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f589251-8c44-38a0-9475-c19d02fd5c23 | -3.11556 | -53.74368 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 662c2670-f1cb-3bdc-90e7-81c8627908f9 | -3.11553 | -54.2201 | 2024-10-15 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8553c637-1d9e-3ec2-943e-7a0db60f33c8 | -3.11099 | -53.73989 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a34ef35b-6566-3b70-b2e8-e97ae7c6628a | -3.10744 | -53.74141 | 2024-10-15 04:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c698096-d8e2-308b-9691-849d6f0276f5 | -2.57123 | -54.00804 | 2024-10-15 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cee3d9bd-0a18-320d-82e7-6d60e5bc77bd | -2.5707 | -54.01122 | 2024-10-15 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46b09506-15aa-34a5-a688-290cb3427568 | -2.257 | -53.76017 | 2024-10-15 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8844813b-8218-3ce7-b596-a6b8ccb45cdd | -3.62317 | -54.67286 | 2024-10-15 04:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 540a8a1c-f47c-3030-afdd-d577016d9e8a | -3.6178 | -54.67201 | 2024-10-15 04:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fd3a7de-9377-310a-aceb-ad0b9398b954 | -1.18294 | -55.81779 | 2024-10-15 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be14aca6-1e38-3176-a2f5-f07aea6c77b9 | -1.17694 | -55.81674 | 2024-10-15 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 710f583b-0bee-3994-ada4-a2af59c349aa | -3.52158 | -55.4366 | 2024-10-15 04:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87bf6d1f-1572-3309-8fc9-4299441ed8a1 | -3.52093 | -55.44041 | 2024-10-15 04:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f071d9de-d3c0-3c19-a22f-a51004c2aa20 | -3.51594 | -55.43561 | 2024-10-15 04:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b00b77f-2961-3e60-a829-47ef5dd61788 | -3.48251 | -55.46094 | 2024-10-15 04:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5bebbd8-b52f-3539-9dd2-85e6effcccc5 | -3.48038 | -55.45929 | 2024-10-15 04:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef365a32-eb86-336f-9975-82d73085b021 | -2.2093 | -56.89264 | 2024-10-15 04:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de66a747-908d-3e11-8635-751307616875 | -2.20842 | -56.89793 | 2024-10-15 04:23:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbeee16b-4665-310a-85f9-f0479062d70f | -5.48245 | -42.77543 | 2024-10-15 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 04106015-b3c1-357f-8bc8-3b97967d41ae | -4.72307 | -38.45749 | 2024-10-15 04:23:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b2a56cb2-f0f9-3116-be41-6d44829b62ec | -5.04643 | -43.667 | 2024-10-15 04:23:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 608ad7b4-009c-3a5e-97f4-c315f7ef7b3f | -5.04355 | -43.66266 | 2024-10-15 04:23:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6f14f6f8-1e52-3445-af72-28521be10392 | -5.04296 | -43.66647 | 2024-10-15 04:23:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f01ee361-a8a1-3522-9fb3-764602881ea9 | -4.94042 | -43.67472 | 2024-10-15 04:23:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45aafe33-a1c0-373b-b282-8225cc0327cf | -4.65117 | -43.75814 | 2024-10-15 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92507427-1dfc-372b-9fff-913c594c517d | -5.22885 | -43.7242 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b41697f1-f14b-3073-ad8d-3a1d0be41777 | -5.22827 | -43.72797 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0cfc7b3-e8cc-33de-9881-f1dfcdc40800 | -5.22539 | -43.72365 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dad8ee84-695b-3e48-b277-0b64f3c19c08 | -5.2248 | -43.72743 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0f5ab9c-c816-399f-af53-e5ff83e038fb | -5.22134 | -43.72689 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20f38372-3d7b-3d26-b44e-99a521a47a42 | -5.21788 | -43.72635 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fbd4fc4-72f7-35db-a032-659861e130b6 | -3.17684 | -43.24749 | 2024-10-15 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ff44818-70ca-3e2b-85d9-3c4f2a25a1f4 | -3.17626 | -43.25127 | 2024-10-15 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e35cfe1-c91a-370e-b3b0-662e62575c04 | -3.17535 | -43.24806 | 2024-10-15 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7c2d05b-9f53-3d61-a6c4-2f609b9dc644 | -5.47993 | -42.79197 | 2024-10-15 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dd222674-7678-3569-b830-20065689bf8a | -4.71834 | -38.45676 | 2024-10-15 04:23:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b5f43d2-c0df-3644-b1f2-b3bd5636f991 | -4.79139 | -39.77887 | 2024-10-15 04:23:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ac596ef-1270-31b3-8b95-dd7ad911ecfb | -4.79068 | -39.77621 | 2024-10-15 04:23:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71769f0e-60c6-381c-91e7-818987b34ae2 | -4.79005 | -39.78033 | 2024-10-15 04:23:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 15785c60-22b1-3f47-abde-e05e0244312d | -4.78767 | -39.77409 | 2024-10-15 04:23:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc649feb-3c4e-3493-ae39-5f53101bacd1 | -4.78393 | -39.76933 | 2024-10-15 04:23:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 963593f2-405e-3666-854c-9670cb9d5cc9 | -4.66681 | -40.27892 | 2024-10-15 04:23:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ff6585b5-912b-3c6c-8ba8-b2acf38e8184 | -4.57274 | -41.2469 | 2024-10-15 04:23:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 91047805-20e8-3d1f-a191-302f7a1d1feb | -4.57271 | -41.24368 | 2024-10-15 04:23:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f26ba20-6958-37f2-b808-d2d6781d67dc | -4.23246 | -40.38643 | 2024-10-15 04:23:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6ea669d3-073f-395b-8cd7-ffb037037497 | -4.23191 | -40.39007 | 2024-10-15 04:23:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 43573bc7-3797-3a79-b32a-177727c27bdd | -4.22779 | -40.38944 | 2024-10-15 04:23:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 650706ae-3078-3456-8fb6-6eee1950bc49 | -4.012 | -40.39171 | 2024-10-15 04:23:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5255d93d-2f4b-3c7b-afd6-4c95ff989f16 | -3.6561 | -40.96828 | 2024-10-15 04:23:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b3c40339-8719-3878-86b9-07e3f7c5e60a | -5.66056 | -41.25123 | 2024-10-15 04:23:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54b8e9bc-9724-3fde-b191-ae49a38430d2 | -5.53113 | -41.45544 | 2024-10-15 04:23:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a6f16798-e399-3d53-8963-458f57112c41 | -5.12635 | -41.67656 | 2024-10-15 04:23:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7fb5e3d9-2416-3ae5-bab7-13f84a6a68eb | -5.1225 | -41.67603 | 2024-10-15 04:23:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dc5a8697-fd42-35aa-901e-77672e1dd7ed | -5.11939 | -41.67073 | 2024-10-15 04:23:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 51e0f3c2-3320-3d07-ad19-78fb4d3622e6 | -5.11866 | -41.67548 | 2024-10-15 04:23:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc748b39-4797-3b0d-89ad-2fdb0dbcbe5b | -5.11482 | -41.67493 | 2024-10-15 04:23:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
