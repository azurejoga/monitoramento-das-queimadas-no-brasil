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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dac26da2-a464-3c6d-932b-68159a7506cd | -1.89427 | -47.00534 | 2024-11-16 04:48:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9de17701-bb83-3128-bd31-d3e181dd72c2 | -2.08493 | -50.48389 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1be468e-32c5-308b-acff-671a364fc64b | -2.92669 | -48.32028 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fba9330-c105-33f3-8e39-8fed206258d6 | -2.47549 | -46.37164 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c782502-6de3-3fd7-accc-8481f3dd5624 | -3.27217 | -45.50163 | 2024-11-16 04:48:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 094cf1f8-d1ef-35db-9434-3e0be898805b | -2.78762 | -48.56952 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cc7866dd-1f12-3ab5-9b70-bbeed7cca79c | -2.66076 | -46.17309 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df889d0a-848d-31e7-811e-654ffe0ac374 | -1.37702 | -54.15098 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 331f427b-0657-3fed-a7f1-2050a232be33 | 0.72518 | -50.72535 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8b26a16-baf4-374a-84f4-629207743304 | -2.22774 | -53.60807 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d2fb16ea-4bcd-3d22-80b9-8d1c49d9ea95 | -2.35287 | -48.42462 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da07c5a-e801-39ff-ac25-d3cd317b9d0d | 0.75859 | -51.45436 | 2024-11-16 04:48:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9d1d73c-826f-3ad0-ac0e-b3cdc44744b1 | -3.51608 | -44.71946 | 2024-11-16 04:48:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43be7bcc-498b-363c-9e03-0065e1cf0630 | -1.8974 | -47.01095 | 2024-11-16 04:48:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82bd0941-3ac0-3f52-b6d1-8d9db522452d | -2.35243 | -49.12078 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b945bb6c-dc5c-3ab9-8f36-21222fade0af | -2.94419 | -48.01884 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd30eca9-1a2f-3756-8a65-d7d91cd5abac | -2.94793 | -48.0194 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d593f306-59b9-3a7b-aec0-75d2980f6f85 | -3.98306 | -43.71573 | 2024-11-16 04:48:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29d1fcf1-03fa-3431-bc89-21cbb8e3c4ef | -2.03006 | -46.37321 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8f92e53-d09b-356c-a9e2-74b8bc8fb2e0 | -2.14055 | -50.1504 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 973adc35-4816-352b-8ebc-766b07d28c97 | -2.45786 | -53.97392 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e8f9698-65b8-30ca-a825-2cef87930d5a | -2.47094 | -44.8407 | 2024-11-16 04:48:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 717c9fe3-475e-3179-9288-8f480dd351ea | -2.47095 | -44.84177 | 2024-11-16 04:48:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8928c80-d709-3717-8354-e6f386cf6a9e | -2.39302 | -46.31442 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cf11125-0b9e-3ce2-bd33-af6f6785f250 | -2.09626 | -50.21323 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed35411b-3216-3bad-8b71-f12ffdf2190a | -2.16696 | -46.40523 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fd81887-8bfe-3657-a14c-e095ce2aae28 | -1.68924 | -48.46539 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 808f96a1-1929-39af-8f48-f954684cdf9f | -2.10262 | -50.37086 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eaea24f-1bc2-3c89-a5ac-89cb8d7205b5 | -4.00378 | -44.33738 | 2024-11-16 04:48:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e33ee1a-6c21-3435-9d41-5acada16e0a1 | -2.45613 | -53.97721 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcfc806d-b90a-32e0-a13f-3c85bead8055 | -2.25245 | -48.15797 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b454d147-9e87-3522-8935-9b8937f1c107 | -2.14732 | -53.71872 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c286875e-63cc-3c3c-b97e-e18ec59cd84e | -3.56677 | -47.37405 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a5f9e4f-4a86-3015-b599-b5fd751059f7 | -2.81384 | -54.02337 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c8fc820-afb0-3c8a-b8f4-fc4425a0ed4d | -1.21409 | -53.56805 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae0fd0ac-8dca-31fa-9d3c-21e50882b02e | -2.73937 | -48.56353 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 499ed83b-cf4e-3153-a8f1-9556da6068f2 | -3.03575 | -47.98044 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0f12a11-de3c-3e14-bcec-d87ed984c099 | -2.94204 | -48.31823 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fe847c4-a84c-3022-a6f4-65d446de84b2 | -3.72532 | -45.65905 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd20d06d-bd28-35f1-968b-55717a41b667 | -3.19324 | -45.54905 | 2024-11-16 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 76d0e31b-a89d-3580-9812-7f9c34ea51d0 | -1.70569 | -46.15988 | 2024-11-16 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 315fa129-6617-3b39-a45c-d9f0978d9b31 | -1.9857 | -46.36679 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8ef0abf-c0e8-3361-9dcd-8f059b0e04aa | -2.51257 | -47.47715 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c7ec4a5-8b21-3434-b967-98221654a579 | 0.79605 | -50.74203 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d570ace-1b2e-38f2-81b8-0b7e756931d4 | -2.77187 | -48.57565 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fa5624fd-8063-3bf1-a2aa-f944487cb389 | -3.19698 | -45.55399 | 2024-11-16 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 7f06b697-ce46-3a35-af9c-c84b0041fe95 | -2.5716 | -54.42752 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61cdb5fa-2656-311a-b0c4-3310d4561ad2 | -1.46081 | -48.19577 | 2024-11-16 04:48:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8172f78b-411e-3616-9e13-6330e86c5ab2 | 0.08219 | -51.19421 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4b0008e6-f1b3-36ab-ab25-77826583bf9c | -2.15478 | -53.71605 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c1f81e6-a0fd-3945-acda-7049ea8ae9a8 | -2.39677 | -54.63874 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c0d6571-b088-399a-9c74-987cd0b24e6c | -2.10689 | -48.10646 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e73a3d6c-dd21-3a50-a82e-e2042d21b102 | -2.88289 | -40.39206 | 2024-11-16 04:48:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93c622e9-79c9-3ba1-a8c4-a5e5424b675e | -2.95259 | -44.29879 | 2024-11-16 04:48:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 739ebf27-02bb-38d5-95da-1a48243e223f | -2.21685 | -50.51113 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbb7782b-5f54-3e70-b152-f2fdfa4e6ee3 | -2.61659 | -46.18219 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06c4a883-93b3-3976-88f7-7a074fe361f7 | -2.13468 | -50.81738 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e400c1c-bdbc-36c3-8cae-1ef56afdf429 | -1.64268 | -50.44405 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 572dc34c-6474-37a7-9245-0aaf8daf0b47 | -1.9688 | -46.36787 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25065b51-c1c3-38ac-82e5-116807fc2377 | -2.5569 | -54.03574 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd011482-4290-3f78-bd91-7ce54467b8a0 | -2.20667 | -49.28239 | 2024-11-16 04:48:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a05ec94-8e75-3dd3-b886-076e36aebf00 | -1.1744 | -54.21823 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbe365a1-65fe-3a7a-8d5e-5ae372abc352 | -2.65606 | -46.2036 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c851737d-652f-35fa-900f-028acebe6f5c | 1.15951 | -50.69567 | 2024-11-16 04:48:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fe0aaf9-3a8e-3223-85f7-d27f5f0470ae | -1.3311 | -47.68358 | 2024-11-16 04:48:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a7c01f3-ea67-3806-b8b9-428b7d285b95 | -2.14787 | -46.55683 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c6eedb10-e725-3923-a09c-40d9aed1dac2 | -1.8635 | -54.28052 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff8488ae-ff17-3b09-9768-b08d874157b8 | -1.55425 | -54.31161 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05278f7f-2470-3f77-add7-7bd176413798 | -2.35013 | -48.96876 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f13fd48-4ba4-34d4-889f-260b6d7ecdc9 | -2.66959 | -46.84367 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b36374b1-0c6a-329f-8439-989c2405215d | -2.14908 | -53.70749 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b51ad156-83b0-3d48-b4fb-ea855bead762 | -2.58611 | -48.94159 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c43b6ebb-ddc9-349c-812c-217f7c1f1e2f | -2.03128 | -48.97085 | 2024-11-16 04:48:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c5b6d9e-40e6-31d5-960f-fc74922c7b9a | -2.77486 | -48.58037 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 3e1b81d3-f0d4-3101-a3b1-1193ccf73c66 | -2.64251 | -46.53542 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 475a2b48-c580-3c6a-a655-305ce3dd483e | -2.57928 | -54.42469 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91cb4869-36ed-3530-86fa-0977bae3e8ae | 0.12533 | -49.84672 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70711445-3b77-3fdb-ab30-fa75fa633dd9 | -0.25557 | -48.51925 | 2024-11-16 04:48:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6889fc68-ec16-3f63-bf0e-e4d5a0f08c33 | -3.4296 | -50.31298 | 2024-11-16 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed1d9c48-f838-3596-9169-994d4315c474 | -2.13368 | -48.77822 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 46e621ef-3bc0-3264-834a-df4d12be4340 | -3.03436 | -47.98946 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3cf0abe-01e6-3288-89fa-50bcc81b5362 | -1.99518 | -46.5766 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7807c7a3-e1c0-38f3-a14d-39dde12c5076 | -1.16104 | -53.50184 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52367923-a88b-37d3-a8c9-8d73d8420607 | -2.21996 | -46.36081 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6092a3c-02d9-3872-96f4-3492c8268f96 | -2.94863 | -48.01493 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe911ccc-e233-3ac0-ae06-31974d849e3a | -3.99985 | -46.49754 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f33a3cfb-2537-38e2-aeef-b8db9dc0bdd9 | -3.03645 | -47.97593 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7940c86c-a589-33a5-8cf1-08e0ced3ab02 | -3.11892 | -45.74477 | 2024-11-16 04:48:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32250409-38c3-3eb6-bee9-c2faf996d77d | -2.13992 | -48.73803 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee19bfd2-73fa-3e72-afe3-6fd53239b210 | -2.14349 | -48.73856 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 762e05ee-c305-3ed0-ba7c-a81a35d97b90 | -2.15547 | -50.70638 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e608fe70-4ba3-3e49-935e-4b842704a4e5 | -2.62855 | -46.18792 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc640d5-6de8-3b42-bfce-9da26d3700aa | -2.13383 | -50.19339 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea2fa7fc-7f12-366b-b10c-55041d084439 | -2.56745 | -54.43092 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08adf07b-7ee4-34b1-a7bf-3d65f5a2afce | -2.55375 | -46.89318 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 858b9b28-8ab6-31a4-b164-1348a4c10d77 | -1.84381 | -53.68732 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d65eb4a1-5a63-39bf-8399-e4d7571be672 | -2.77847 | -48.58092 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8a66ead-ac23-3c0a-9b32-5fed98e71e36 | -3.01482 | -48.0416 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f0c74f0-502b-3c42-b3a9-594a2d922a33 | -2.64353 | -48.48148 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 855b83ef-a934-3bfa-a681-d7be3d508da8 | -2.076 | -48.54612 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README45.md)
