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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b232e2ff-1883-32ca-b28c-7dcbe9efed0e | -13.13209 | -60.25972 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71a173e2-9a88-3041-9eed-4c2b15a33552 | -12.96747 | -60.05558 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dc067eb-e49d-3e3f-a5a8-91dd0589a402 | -12.96684 | -60.06004 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08bd9a20-8237-38c2-ad99-6b91095bac8e | -12.96317 | -60.05951 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e4575b2-4be5-3200-bb58-d180410773d0 | -13.1321 | -60.26273 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7252184-8335-3551-8f5a-d7c01e15ed7f | -13.12967 | -60.25357 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08835850-3c3a-395e-9bb7-06775ddb1a4a | -13.12908 | -60.25488 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15aae8a7-d65d-3e64-98d6-36c9980d9822 | -13.12846 | -60.26219 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f52e8bf-b5cd-37d5-836b-82d96f4785f8 | -13.12844 | -60.25919 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37aa37fa-d490-32ad-99c1-ce06bfc26f3d | -12.33618 | -59.87879 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9cd126c6-1714-342e-b30f-26c54168a655 | -12.31563 | -59.81841 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bd2b19d-8710-382b-b9b1-815528509628 | -13.73445 | -60.5925 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a82f47a-ee8e-34ca-a2b5-67abde353699 | -13.73025 | -60.59621 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c6fb205-47c5-3ee5-8144-8cf661e7c3bd | -13.76816 | -60.56277 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbb92db0-c2bc-3e5b-ae02-6f8268576a90 | -13.76454 | -60.56224 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28429541-417f-33d5-9033-416f46a62093 | -13.75671 | -60.5654 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 045ffca0-1dc3-3598-aed1-fb2d7f2e8c41 | -13.75611 | -60.56967 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 43449a5b-3f23-3ac1-9571-40c01ca963c0 | -13.7531 | -60.56486 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28c6d1d0-2cea-3800-ba2e-0bef70ed81df | -13.7525 | -60.56913 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53a92249-12a5-33a7-be85-1dbdb8be03fc | -13.75189 | -60.57338 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b373ab9d-fd33-3570-8cce-ac9130621479 | -13.74708 | -60.58135 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7e5ab52-7f51-33d1-b5ca-167e75b00c11 | -13.74648 | -60.5856 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35ef1c26-42db-39b4-8b5b-2a1818a2820d | -13.74347 | -60.58081 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 45d65717-6a42-338a-98dc-216f275c0e14 | -13.74287 | -60.58507 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e3d15e94-6739-3a94-8b02-584f9135d269 | -13.74227 | -60.58932 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efddee4d-c483-3040-9310-7eb9ace9242d | -13.73866 | -60.58878 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1550f898-9fb2-3dce-8838-20b0a7665d07 | -13.73806 | -60.59304 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2a6babf-80a1-3ca1-8813-dc8040b9c755 | -13.73746 | -60.59728 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ba4e27f-737f-3462-aff2-6452e4c81cfb | -13.73704 | -60.58975 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce0d389c-8315-3a5e-a411-4a7729575dcb | -13.73642 | -60.59399 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89e4b6f6-06b3-3536-b07c-0bcfa875b0ef | -13.7358 | -60.59822 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72d5e0fe-c00b-3f20-9a5a-c5b2292cbb9e | -13.73385 | -60.59674 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e11f10cf-c001-3b9f-8d9d-55bb9814f781 | -13.73281 | -60.59346 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b9aacbe-6bfa-3c7f-abd5-9b53f14e21da | -13.73219 | -60.59769 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a8ba0c1-a8cc-3fe1-b715-bfd5aaf0ac59 | -13.74781 | -60.10166 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 65f89fa4-c1ea-3d0b-a1b7-f6cc36b8a7dc | -13.74157 | -60.11909 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c79e8038-48bc-3784-8030-cb00f1b2c8db | -13.74094 | -60.12355 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14cc8ac2-8d37-3444-94b7-bf8f41a7f95c | -13.74041 | -60.10061 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5417060-d4ff-31a5-b4d3-acfb17c63766 | -13.7403 | -60.12801 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 665994df-2654-34b9-a58d-e88f12638ae2 | -13.73787 | -60.11855 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89724e20-183f-3da6-ad42-df38b0dd4e66 | -13.73734 | -60.09562 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6952f2b9-9357-3ba9-b2a2-8ac531b3ffbe | -13.73724 | -60.12302 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fffe97e4-52c5-3b8d-9a80-cbae54b33d95 | -13.7367 | -60.10008 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23ec2661-21f8-37a3-a704-4ac30be92bd3 | -13.73417 | -60.11802 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e86a0d4-7adc-32bc-8f4c-2bcb19b48915 | -13.73363 | -60.0951 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e6acc28-9b2d-38a6-bae5-792346caef07 | -13.72992 | -60.09461 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a39e0756-bcc0-3ed4-9f44-51075ee74d39 | -13.72985 | -60.12195 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65cf720b-0439-3ae1-9f3c-da3f12f9a671 | -13.72683 | -60.08974 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2664e974-6a50-32f4-ae87-ec5e87b24be1 | -13.72615 | -60.1214 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcaeaca6-cb2f-305b-a1dd-5dad240bfabc | -13.72314 | -60.08909 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d539f384-d6a2-3c01-ba07-bb1bb7987dad | -13.71698 | -60.07912 | 2024-10-13 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b4703e9-c763-3064-b8e2-5975a8c4eb31 | -14.52964 | -59.83893 | 2024-10-13 05:29:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29f91be3-3815-35a8-a765-9dc0a0805bff | -15.65912 | -59.94823 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75c8558b-ad43-386b-b93d-3dab947ea05a | -15.65621 | -59.9507 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| def6a96a-affd-3e36-8afd-67179001cbe7 | -15.6553 | -59.94764 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbbc7d5f-2135-3b8b-9476-6937dcad173b | -15.65464 | -59.95256 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dc6307a-f92b-3c18-9125-6ef77a4d0ea8 | -15.6517 | -59.95501 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 295c1190-f7db-3501-b232-5a70b93292fb | -15.649 | -59.97435 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4df9263a-db89-3960-aca8-6e6dde174f36 | -15.64832 | -59.97918 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 53b14d28-508d-331e-b350-fc52e92d11be | -15.64814 | -59.92465 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 334a2a21-b8af-339e-946b-fe57b639052c | -15.64765 | -59.98397 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f029eb15-5e8c-3370-9ae6-b31e0d7db3c5 | -15.64585 | -59.96899 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7bfaade-42ed-3bde-9a91-5858ab22ec56 | -15.64518 | -59.97381 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2dc3a431-16ea-3e1c-87bd-b985d5fc182e | -15.64451 | -59.97863 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dfc02a90-c25c-3bdc-916d-8b74d6952712 | -15.64432 | -59.9241 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57341092-96b4-3c7e-99b5-3ee3021cac21 | -15.64384 | -59.98341 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0b635b26-cfaf-396c-993f-aaf0ba217c75 | -15.64364 | -59.92896 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 023e60da-0276-3284-b39a-d84076bd1f3e | -15.64317 | -59.9882 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8ab6c065-68e6-3d10-bf26-0c5ca87f6ed0 | -15.64272 | -59.96357 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f61858f-8627-3311-9dbd-287b14e14fc9 | -15.64205 | -59.9684 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d038700-cd17-30dc-891f-ae2e7112c38f | -15.64137 | -59.97323 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6ce12a5-ef3b-33fb-abd2-e9e8dc7bf51a | -15.6407 | -59.97806 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27f0bf64-e253-3d50-8f37-70df862dd4d7 | -15.64003 | -59.98286 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23843f21-dc54-336e-899c-5bd20098dc8e | -15.63982 | -59.9284 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c6c4976-6978-325e-afc3-b44e94c36c71 | -15.63958 | -59.95813 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bdc14ad-b817-3098-af6d-b7a63479d7dd | -15.6389 | -59.96298 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89791720-fefe-3937-8507-1d3b2a08cd0a | -15.63823 | -59.96781 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ad5e650-159e-3499-ae47-4a4809535e66 | -15.63756 | -59.97264 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5852e93-25eb-3d09-b28f-650ffd9a9d8d | -15.63688 | -59.97748 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da96d0a3-44e5-3614-ae68-8c8a6c77349f | -15.63621 | -59.9823 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 256b76ea-f79f-37ca-b55e-fd4fba9970fe | -15.63599 | -59.92785 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ecb56ed-19ae-3086-9451-b0c8007c13d1 | -15.63577 | -59.95755 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f407652b-489a-32ea-abce-abdd0db410a6 | -15.63554 | -59.98709 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c9040842-9ec0-3f8b-add3-d639fee3d4de | -15.6324 | -59.98174 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93ba32fb-4352-3bcb-b990-f226df9fb0c6 | -15.63149 | -59.93214 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91808a0c-ddce-35a8-a35e-5ddafdef383c | -15.62859 | -59.98118 | 2024-10-13 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 802e4466-a29b-3c77-a96d-e3037275b301 | -11.56123 | -60.15605 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 355a16d6-37c2-318b-a79a-71cbfa70c7d6 | -11.56031 | -60.28785 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae6d5006-1861-3d7f-9709-1aad759495f6 | -11.55762 | -60.15558 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9848f778-20db-3bf0-829e-8b0d42507fda | -11.55673 | -60.28735 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ec974b0-28b4-3d5a-b018-a2b2d8eb3e96 | -11.55613 | -60.29142 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91073c9e-f651-34b2-a357-f2cde62aab30 | -11.55402 | -60.15508 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8e8688b-d7f6-3826-a839-1048839d5b07 | -11.55316 | -60.28682 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef3015fd-a38e-3248-95fa-e49cc32853c6 | -11.55256 | -60.2909 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 906eb7fc-3688-3d0f-a99a-43081007b49c | -11.55043 | -60.15453 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bbb94f2-0ed6-38a8-9935-592d735251d2 | -11.54899 | -60.29036 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d0f1023-a8a1-3fb6-83f2-4e233a633d78 | -11.54839 | -60.29443 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fbf2cf7-7aa0-345b-8a22-e3eea250bb77 | -11.54672 | -60.23072 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3b68ca4-8519-3306-a93a-ecd07c2f4bed | -11.54542 | -60.28981 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a99cc85-c3f1-32d8-afbf-1d14f02b7f9f | -11.54482 | -60.29388 | 2024-10-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README103.md)
