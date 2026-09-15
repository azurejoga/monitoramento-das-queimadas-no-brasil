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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b674370-cc45-3a4e-8a39-f91c42a20cfe | -6.16019 | -55.70338 | 2026-09-15 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf38ef42-29c7-3a0c-af21-f7db371caf37 | 4.29331 | -60.9469 | 2026-09-15 05:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82d8808e-f5f6-3105-82d3-bfeb90d7f8e6 | 1.74096 | -60.28825 | 2026-09-15 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c19f3e6-f465-37f9-a91c-5853c727ab35 | -6.11399 | -57.67706 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b2d6536-5dfe-3ae2-88ff-dee053702e1d | -6.32719 | -59.99242 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d00e6894-f47f-3997-8776-5b601724175e | -3.3351 | -54.19063 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23fd13d4-37e4-3c49-8512-03a728120476 | 0.09567 | -60.6356 | 2026-09-15 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b18d367-a077-30dd-99cb-03e5cf26f4a0 | -3.08157 | -50.57307 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88cc008e-4f87-34ff-9ac3-26e5ed81a9b4 | -8.08506 | -61.79835 | 2026-09-15 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07c34275-256a-3aa3-8f28-dd38df884d0c | -6.15928 | -59.94156 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f01e71b1-1541-3814-8c46-0c5ec46c9bc1 | -5.59342 | -60.18699 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3a0bba0-4089-302e-bed7-16fe1dafb8d7 | 2.69915 | -60.30047 | 2026-09-15 05:53:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1f889c8-a86b-3bd7-bb1b-2095da8e1c6a | -2.82079 | -51.33682 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5bae0d-906f-3a67-9d56-95fffdce290a | -6.15969 | -55.70687 | 2026-09-15 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 798d656b-c0b7-3068-b8fd-ebac13e62697 | -9.57199 | -55.14053 | 2026-09-15 05:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f93c6c0-1a4d-3472-b28c-f417e6482bb1 | -6.84233 | -55.53715 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4fb25b5-da8e-3bd6-be98-4d1fcea212bb | -7.5619 | -62.3264 | 2026-09-15 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c04c1e49-4e1a-3924-a6aa-15bdbc36c1f0 | -6.01276 | -59.95052 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc030ff0-c74b-32be-b508-979972c6ee2f | -7.56126 | -62.33064 | 2026-09-15 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7da200c-6fba-38d4-acaf-4416f6062781 | -2.83973 | -57.638 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21284fd4-4820-3f07-96de-bb43fcd6f167 | -2.65047 | -59.37385 | 2026-09-15 05:53:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2657ea6f-760d-3548-8d42-f1c413f121d3 | -6.69175 | -58.69311 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9499e46f-6589-3346-866e-0a0ebfe6cae1 | -7.41847 | -55.54282 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0111cfb6-1057-3012-987c-4df6f5f8b270 | -6.11277 | -57.67814 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79950265-462a-336d-8d5f-59a14ae5f403 | -6.79386 | -58.78941 | 2026-09-15 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5501a01-b321-356c-af35-b2b709c4fd9a | -2.69815 | -57.58563 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 100b3d00-7c15-3f0a-8d7e-a222188ce7d7 | -3.26298 | -54.51972 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e855dc9-bf53-3c40-821c-2da09566cec4 | -2.7092 | -57.6095 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02abdcfa-04a5-3a10-b489-d4be297cf8eb | -3.4831 | -54.67397 | 2026-09-15 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 299b5e76-d078-38c1-bb7a-86910c578d8e | -6.13014 | -59.88034 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b176212-b1d5-328e-8c7c-446b07c484f5 | -6.11204 | -57.68338 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b7bbd3c-e737-3682-ac6f-2b1248087010 | -6.64596 | -59.96248 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 495733b6-0ca7-3cc6-a419-043dfc7917b4 | -3.48995 | -54.66693 | 2026-09-15 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 335928a6-7cab-3fd9-86fa-69ab43908b96 | -9.68979 | -54.34443 | 2026-09-15 05:53:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db193505-1851-3b6b-985c-6067eea71f57 | -2.8198 | -51.34325 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfab04ee-7061-3d77-888d-f0c499e0a192 | -8.77601 | -61.4242 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edf37f51-d145-3325-9df7-bb2fd3956e76 | -3.39359 | -50.75377 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78cf7755-19d9-3dd2-8443-76a2850b6c54 | -6.10638 | -59.88906 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beaad3b1-ba25-3525-96e3-0e035fbfffce | -3.53929 | -53.9798 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2290a55-be9d-3da2-a4f2-6123600b6585 | -1.68584 | -55.89972 | 2026-09-15 05:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0725d4e2-7fe9-36b4-a0c8-a4c94e85f98c | -3.39216 | -50.75583 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0420ed0-b45a-3c8e-bd22-ba5bf23614a0 | -2.70846 | -57.61127 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7fa82a65-3573-364f-9d65-6e486b72326b | -6.58672 | -58.86283 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fec5cc5e-0f71-3ced-b1aa-2dcb694b750f | -6.11051 | -59.88976 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d16c7b21-98c4-3299-a0f7-614624603ae8 | -6.69042 | -58.7022 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea4ab844-85c5-347c-9cdd-e73582fee2ed | -6.84641 | -55.54961 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7ff67406-8841-3dbd-bd37-7b02a911ea4e | -7.87694 | -61.40755 | 2026-09-15 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a75d543-7ab7-3737-9b21-119484158902 | -2.65995 | -57.50047 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f187b69f-fb66-3ccf-a8f0-6184e85beec9 | -6.58355 | -58.85336 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 022e8636-c3f3-302b-9d7f-eaddab99ede0 | -2.70387 | -57.61347 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a764581-628b-3fa1-83ee-ac9c86cea08f | -2.67919 | -57.59054 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeaf68a1-8a54-34bb-b52a-dc77f8950541 | -6.32546 | -59.98766 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5467df66-2a33-3127-b4ca-4373ac8a0cd4 | 2.76703 | -60.21832 | 2026-09-15 05:53:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee583847-a89b-3441-96b0-772d3ea9d9b0 | -5.4393 | -60.22105 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec309452-8742-341f-951e-4d0a74474f8c | -6.10993 | -57.67117 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cd28d3f-2a5c-3d31-89f9-f8b018d60161 | -6.07699 | -57.86174 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f061af47-d86d-368d-a57a-4de39761bc65 | -2.70776 | -57.61597 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99a9fa48-c94a-3715-91d7-02444906d662 | -6.01795 | -59.94382 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2f2d726-d413-3c05-b760-99ed06c16d39 | -6.1592 | -55.71033 | 2026-09-15 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5271bbce-b07e-39b2-a483-37b700478ffc | -6.74526 | -59.43241 | 2026-09-15 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68a985c3-35a8-3926-9e07-8b9898766fe5 | -6.11322 | -57.68231 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acd2dedd-5982-3d35-878a-cffb1825d437 | -6.15469 | -55.70242 | 2026-09-15 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7fe20ec-e5de-3adf-99dc-49e1f2641fad | -1.22767 | -54.12532 | 2026-09-15 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98cd2644-8991-3a19-b06f-eb677c340932 | -6.43514 | -58.14518 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0527cc55-8d41-31c7-8682-61e239226c1a | -8.37449 | -54.72456 | 2026-09-15 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a71349d0-3bf7-3a9b-af5b-e08e26a9dede | -5.44331 | -60.22166 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b58ca4fb-c922-3cee-9fd5-9a3443a442ca | -8.12225 | -54.80191 | 2026-09-15 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e64c9b7-285e-3e61-bd9d-366f6ecd135a | -6.8413 | -55.54489 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1f117a61-25c1-3355-b162-ba237ef0b205 | -3.25606 | -54.52674 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d3a6b53-b1df-3b47-b2c3-88710b8ca634 | -3.07431 | -50.5719 | 2026-09-15 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 942c925d-1b79-3934-921d-251777381cd3 | -2.70846 | -57.61419 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72b6b1cb-7c79-36e5-964a-35cb73bd0d24 | -6.84078 | -55.54874 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d810c533-e071-3a70-a2f0-1b21d13f672f | -6.02423 | -59.92969 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 5bb730df-70ef-3743-a64c-7b3a8d978f24 | -6.90732 | -57.62973 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b07820d-2d4e-3478-9ee3-a457a73d7db4 | -6.69496 | -58.70284 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c501ddef-c263-33e8-b858-81fb7e46af9f | -2.78177 | -58.14117 | 2026-09-15 05:53:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b044bf7-31f7-3d43-9051-d12d80631567 | -5.4599 | -60.22057 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f240f502-839a-3103-84f0-f328c384a2a7 | 0.00277 | -60.58807 | 2026-09-15 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b76f9fdf-ac76-3693-b635-30d16e52cdeb | -2.65092 | -59.37353 | 2026-09-15 05:53:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 785e658f-052b-3d29-b142-e8bf6984c7c2 | -2.66439 | -57.56419 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 715989c0-350c-3e13-8815-eadb2534d5d3 | -6.70015 | -58.69899 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d83f5afe-dc36-38bb-9674-c5eda69fba8f | -9.57612 | -55.14448 | 2026-09-15 05:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52e45f52-8570-3b1d-8005-ca25cfeb77e3 | -6.83847 | -55.54193 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11eb2f99-20c4-34bd-8972-8b7ccec7c169 | -6.32854 | -59.99559 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a65cfcdc-262b-332b-8386-df62b4c0a1a0 | -6.8441 | -55.54274 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00c9d070-55c2-3106-9335-069287ba15ce | -3.53865 | -53.98405 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7887f3ce-2d07-3244-940d-1ec6c7e3da5f | -6.0149 | -59.93582 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 68da977b-06e6-3e04-b935-3e6f6f1be99a | -2.65878 | -57.53917 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ca1b49f-b081-3d04-97de-f89d503b36a7 | -6.84573 | -55.53122 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b29924fe-1b0c-3657-8dab-117cdd91c65b | -2.65459 | -57.50453 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e56ea98-08c2-3174-bcf9-596bf69c73d9 | -6.69241 | -58.68853 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be082f10-b73e-3b09-8092-bf85ebb89430 | -2.68457 | -57.49448 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87b30148-4f15-32ce-bfe6-368425f1525b | -3.26335 | -54.52209 | 2026-09-15 05:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ffe0714-5f08-3419-9d47-cf7bba27fb9d | -1.19802 | -54.12091 | 2026-09-15 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d1c6288-e011-3daa-af80-0628e2ca59e9 | -3.11227 | -53.95029 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86de7177-3cbb-3d37-bb02-21d6717d30c6 | -6.69949 | -58.70349 | 2026-09-15 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3895d2c2-62ca-3ff2-8c43-a4bc3e80eecd | -6.84849 | -55.53411 | 2026-09-15 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4479c522-7c48-3402-b491-d84a14be5dd7 | -2.66511 | -57.55949 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d1686448-43e7-32eb-81a0-7a096e019ce6 | -5.17996 | -59.76221 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9de246f-db8f-346e-b117-4679ba601b63 | -3.48938 | -54.67079 | 2026-09-15 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README65.md)
