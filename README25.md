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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffbd6937-c874-35a4-8b33-237348746f9f | -6.23783 | -42.58153 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8276f370-f924-3817-8507-83878a2f342b | -6.19453 | -42.62174 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6d77b75d-9507-3b6a-b873-abe35917e155 | -5.43856 | -42.80529 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ca594e6e-126f-3d52-aa5a-6163d42774c1 | -6.07777 | -43.54969 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccf6a028-cd1c-375c-a29c-3797ccf211f8 | -2.43129 | -49.30864 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7408dda4-cc41-3b59-84fa-9fb77c6cc3fa | -5.75743 | -43.13387 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd24adcf-65d4-330c-8d9f-a83f9e263170 | -5.83022 | -44.1226 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92bd4592-16aa-337e-8669-6e31a26993f3 | -6.21935 | -41.78651 | 2025-09-07 03:55:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9826cf8b-1a95-3926-91dc-c086e964c8d5 | -6.23107 | -42.59312 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5a37f80-45a7-3d7a-bfff-272afa8169bb | -5.99372 | -44.14442 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2aecc0b2-ce7d-33d0-99e0-05472d4bb17c | -6.19681 | -42.63223 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3ea87e84-8476-3766-9b29-29363f533e87 | -5.31282 | -42.80205 | 2025-09-07 03:55:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 548d3e4d-e73b-3d17-8a89-b5e32dbf5c78 | -5.4848 | -45.90955 | 2025-09-07 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b44de5a3-3fb5-318f-9236-f0e5c5568e9c | -5.98803 | -44.15185 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3626c7fa-536c-379a-bad3-bc1e2b39c731 | -6.20779 | -42.64124 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 40d2612b-1a89-3ec9-b036-5dfd860b1a44 | -4.17147 | -42.02291 | 2025-09-07 03:55:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 25fb6915-0b14-39a0-8eb7-f241a6c2f1aa | -5.83089 | -44.11856 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e570d56-abf8-37ca-b9e2-9fa7717d7b2e | -6.18351 | -42.64024 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 27864fcb-7d48-3364-9832-a782870b0564 | -6.16541 | -43.18032 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5222a00a-1137-34ba-b554-81f3d90689d9 | -6.19841 | -42.62242 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 52c7aecc-b37e-31f5-859a-3016a1313821 | -5.46157 | -42.81413 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ef96e4b1-7b2c-35e5-a268-0bca57ff1a3f | -4.4464 | -44.1422 | 2025-09-07 03:55:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31bd6b6d-c6e9-3547-9b3e-73a7a280d10e | -6.22766 | -42.59462 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5c74b90e-8d45-3473-bfef-e3534e54fd48 | -5.94325 | -42.96036 | 2025-09-07 03:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7184a786-2c42-3141-9217-bcde0a0abc71 | -5.97873 | -44.15445 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7fc036b-cfb5-3bf3-9bc4-3fdc316f5633 | -2.8152 | -49.2016 | 2025-09-07 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c855b2b6-f95b-39eb-8a4c-82fe67a0db9d | -5.76204 | -43.13105 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13bed65a-70e4-3f93-8d63-66bda5ebb048 | -3.59213 | -47.5139 | 2025-09-07 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9ec7a8ca-ac04-34b1-b735-9f93ec71b71b | -5.75916 | -43.12344 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56f323ba-9695-303f-acb7-8bf50c95ce62 | -5.82954 | -44.12667 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7b31a6a5-3f9a-3ebb-8533-91bac0a2239d | -6.16707 | -43.19508 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9660df01-4609-3885-9736-c8bf3debc88a | -5.98373 | -44.15108 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5fc8ce44-c6f9-3b12-a4a6-921d35ef37ff | -5.45049 | -42.80717 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f0257913-65d5-3172-a4ce-fe8afb3ff752 | -3.58651 | -47.51293 | 2025-09-07 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ce47c21b-d70b-3c61-9aba-2e91449d6862 | -6.21544 | -42.64032 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e852be1e-6c97-37f7-a6d6-ece480bbf759 | -6.16942 | -43.18107 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6984a8d4-7780-3180-b728-593e2c46d71f | -2.43817 | -49.31005 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13632d93-4d14-39f6-ab1a-0f79d22124c0 | -5.35326 | -42.65273 | 2025-09-07 03:55:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 48b72608-7289-3de0-a96f-326148199377 | -5.99301 | -44.14854 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cc7a9e23-ff5b-3cca-bde9-a4722b1abe83 | -6.25053 | -42.43597 | 2025-09-07 03:55:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cddd6525-03bc-3195-bb53-ed9914662fd4 | -2.43044 | -49.31389 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f4d4b02c-8519-3226-b4cf-2e511df8e619 | -4.67621 | -41.0181 | 2025-09-07 03:55:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30dd73e5-af46-3892-b11a-9fe122a31b32 | -5.99091 | -44.16086 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcab74e0-6742-32f5-8cb0-07ef0de7d882 | -6.17168 | -43.19223 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f980491d-1f4e-3946-b96f-594f22294bdd | -6.22053 | -42.46321 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2121fb6c-0018-35fe-99e0-698ea6ebebba | -3.58587 | -47.51667 | 2025-09-07 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 32f77113-e800-3ce4-84f5-7d99f0f03823 | -6.23234 | -42.59051 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ed77e42d-0564-36ea-ad39-44458261f817 | -5.63415 | -43.12388 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cf0a5f4b-e372-3605-a440-a300dd65948f | -5.30738 | -42.78527 | 2025-09-07 03:55:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 41ab87d1-e0fe-3d69-a5a0-6923e58140ca | -6.20845 | -42.63424 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4f408152-6c55-3691-a062-de517941e333 | -2.98475 | -49.30194 | 2025-09-07 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0b8d5d3-4fca-33ec-b2ce-8a7c6e309163 | -5.98951 | -44.16907 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd5b1034-7355-3891-9b66-e1098442dae4 | -6.0009 | -44.15416 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d60eb29d-efdb-335a-8b53-edbd472323ff | -5.43623 | -42.80858 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 750eeb15-14dd-3cac-950a-c0f6e0994a09 | -5.76713 | -42.34976 | 2025-09-07 03:55:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 00e1353d-2f89-3b33-95fc-575df6d73bcd | -4.1528 | -43.88301 | 2025-09-07 03:55:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f37fda16-cfb6-32c9-83ef-ea713e52532d | -2.89427 | -40.24164 | 2025-09-07 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9f0dd098-2f75-34f5-bdeb-ae3f76a635da | -5.98303 | -44.1552 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4d6029c5-e974-3f11-994a-4b2f828b21cb | -5.86486 | -46.05491 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 437b570a-1ae6-3fb9-9806-a95529e93386 | -11.51969 | -43.24899 | 2025-09-07 03:57:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9526665f-4569-3398-83fb-3c70133f6269 | -6.79657 | -50.84216 | 2025-09-07 03:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6979f511-e166-3586-b317-5659f391f8fd | -7.2731 | -39.32286 | 2025-09-07 03:57:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a88a98bf-b8e9-3f96-9901-b9961f766552 | -6.34319 | -43.78925 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 996e65a7-826e-365b-9311-12a14a0f3b8a | -6.21013 | -44.19357 | 2025-09-07 03:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84dc407a-c2fa-33ca-bc36-26a183b15b51 | -11.30639 | -46.5371 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83f654b6-4676-367d-ba9f-8eb07b06cccf | -6.2151 | -44.19032 | 2025-09-07 03:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96deb773-462e-3bfc-8fb3-273a0bf71c0f | -7.7719 | -50.75452 | 2025-09-07 03:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f2e4c35-8483-3330-a359-f68920871778 | -7.81277 | -45.43282 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcfb9890-4b34-38ea-83bc-32c8db6e7746 | -6.91492 | -45.20011 | 2025-09-07 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e66f4f0-9d69-3f6d-813d-4adb686cf05c | -8.35392 | -48.26745 | 2025-09-07 03:57:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41963bc7-2306-30cc-a994-139d9cfb3eaf | -8.4419 | -45.03286 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e40140f-9b78-33e6-80e9-6046e7a89ccd | -8.14482 | -44.87638 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f133018f-8ced-3a4f-847b-75264721f4b0 | -8.46025 | -45.03117 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7f998c9-7884-3c10-a8e2-83ceb3c00724 | -6.80316 | -50.84328 | 2025-09-07 03:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 372df6da-3663-3d88-b244-bdb7d6ba8cf3 | -7.73545 | -50.30895 | 2025-09-07 03:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c25400c-c091-3fbe-88f4-097bc5004ef6 | -11.37326 | -43.54216 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c67e0bca-1956-3175-9a9e-9b92ba22969c | -6.59759 | -43.97264 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cffbb752-86ad-338d-8aab-96d2c175c318 | -6.20319 | -43.596 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c20f46c-c12c-3b94-92dd-b3a0b7cc79a4 | -11.1592 | -48.39183 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bf72170-f538-3f23-8318-9315fc2f38ce | -7.83711 | -44.94016 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 513a25a2-a93d-33d4-b033-dff810ca0c4f | -6.52561 | -42.41422 | 2025-09-07 03:57:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3431416d-7da6-3890-b569-9c9cc7ac75d8 | -10.80342 | -47.72808 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e7af82a-5c88-3678-a1a7-dad94f3dff98 | -11.41183 | -43.60425 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3717e302-bf6f-3361-8e24-43418b2650e0 | -10.34095 | -44.90787 | 2025-09-07 03:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a893b679-766c-3025-9a96-042231622ec0 | -11.14811 | -48.39307 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97407a94-d3a5-3db5-8ed0-59bfea788eaf | -8.1102 | -45.31247 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b2da673-663b-3c81-a3b0-c23dd1d6c622 | -12.93427 | -48.03853 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6161308-d3f2-3c63-8bea-d0973e31e44a | -7.74714 | -48.8279 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c872f1ab-cf7e-300f-ab0b-0b4232164b4b | -13.04199 | -48.03898 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9ce3736-f223-3926-abe4-736d793e2f75 | -6.21684 | -43.59052 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 665ed7c2-005a-3b73-91b3-6bff2104ab36 | -8.0341 | -44.03753 | 2025-09-07 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 152aafe6-f331-325f-9128-583a788e612f | -13.02457 | -48.05239 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34b63dec-9f41-3d8d-b94d-c0ee9828a3b9 | -10.79902 | -47.72368 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c63acd70-8e7f-39fc-8ac2-000b405d0c1f | -12.01151 | -47.78074 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d081e593-143a-323f-94a7-85f43057cb45 | -7.40261 | -44.98182 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 683b467d-3034-35bb-9de6-b48c3b7b3117 | -10.35139 | -46.46731 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 387a9525-f665-3818-a5f2-df7a6d669479 | -8.68049 | -45.28421 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2feeced9-c60e-3a91-9980-7813240105e0 | -12.73488 | -45.11136 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f353b9e-1082-3cdd-a646-d96e90cdbf1d | -10.15121 | -48.7394 | 2025-09-07 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75863e3f-2ac5-37b7-80a0-5393e3f04988 | -11.35573 | -45.57335 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
