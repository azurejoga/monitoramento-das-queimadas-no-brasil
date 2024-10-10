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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1796753-999e-3d54-a43b-38125bc9f195 | -8.23253 | -61.20106 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9bf44a6-c8c3-3ffe-a566-5f2eba228a69 | -8.2317 | -61.17434 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d675c69b-1585-3fa6-8c1f-86fa08ae4282 | -8.23104 | -61.17796 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55ecd61f-ffd2-3cb7-a1d8-44574c83ad0c | -8.23037 | -61.18163 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a62a80a5-5392-39b8-a103-0bf6ce5340a1 | -8.2297 | -61.18531 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4b89110-dbe1-3078-be83-2f0a58673dcb | -8.22903 | -61.18899 | 2024-10-10 04:44:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eec7ccda-c63f-3553-bb06-668823f1717f | -8.56532 | -40.66174 | 2024-10-10 04:44:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8dddb813-21be-3c2b-8207-678d272c6bda | -8.56472 | -40.66615 | 2024-10-10 04:44:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e776ceb5-a653-34c5-8145-88cb07ce4bb1 | -8.15171 | -42.96038 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 669ccf30-0611-361e-b3c3-6981b9b5e64b | -8.15131 | -42.96341 | 2024-10-10 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 4cc526b8-a678-3e74-8457-eafa46556392 | -5.92297 | -39.21916 | 2024-10-10 04:44:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c6c20fbd-b41b-3b7d-a48f-79f49f22c005 | -5.91669 | -39.2182 | 2024-10-10 04:44:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 509fd45a-22ae-3469-800c-c2697b32514b | -6.30121 | -41.7676 | 2024-10-10 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 78e810f9-fc35-3b74-b60b-d1898431c6e8 | -7.36166 | -42.18929 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9f9374f-ff65-30b0-b121-57116f70b552 | -7.3612 | -42.19253 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4062c0fe-9ca3-34fd-a8fd-5976489137cb | -7.35637 | -42.18853 | 2024-10-10 04:44:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9423f51c-9c42-3bb2-a6db-cd3c37b44c92 | -8.14509 | -42.32394 | 2024-10-10 04:44:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f0fc3014-126f-3cd0-bd7a-9d14c062ddca | -8.14466 | -42.32718 | 2024-10-10 04:44:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 46a7d7be-edac-356d-a046-df2d5302d819 | -10.21148 | -42.45906 | 2024-10-10 04:44:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 31af0599-6d9a-32b7-b479-a64109ae8409 | -10.20653 | -42.45486 | 2024-10-10 04:44:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 187162ee-a2b2-3952-b8aa-9468d4f64474 | -11.02932 | -42.89531 | 2024-10-10 04:44:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 171aa69f-9b26-31d5-b27a-7c7f4b48cc4b | -11.08625 | -41.53851 | 2024-10-10 04:44:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 80f8a75a-f253-3cf1-b94e-875fbf784c6b | -11.08606 | -41.5391 | 2024-10-10 04:44:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ff13eeb8-110b-313e-9316-de770766047a | -6.28302 | -43.43485 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c7c2bc1-1c8b-36d6-9b9d-ab65d1d2653a | -6.26466 | -43.4267 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 287f50df-d8d2-3338-b32a-26e25266669a | -6.26409 | -43.43013 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 901a4d2b-21fe-3f85-bf67-537fbcf3c5dc | -6.26393 | -43.43191 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60b43a79-c0f3-3b5f-96e1-3fe706ca104f | -6.24676 | -43.52016 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92b828ba-6c79-3018-a1d3-c63a33de036f | -6.48605 | -42.17197 | 2024-10-10 04:44:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad0487f8-438d-3013-8db7-362bd26b47f1 | -6.48563 | -42.17501 | 2024-10-10 04:44:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4be3e685-0716-3de0-9378-9fad805a5de4 | -6.42259 | -42.01533 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42b5d76c-7fe8-3633-860f-19e4f12af06b | -6.42211 | -42.01868 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c373da28-fd4f-3a20-a289-3befba7ecc3d | -6.42026 | -42.41667 | 2024-10-10 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8c81d85b-b19b-37ac-ab41-57c68701f926 | -6.25458 | -42.5147 | 2024-10-10 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d3d32f2-7e3a-3d1e-8976-37c782117c0a | -6.25414 | -42.51773 | 2024-10-10 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dbe9023f-8c09-3a51-9c80-427d6fa39446 | -6.24861 | -42.52014 | 2024-10-10 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 086d4202-3e42-34a2-a567-d274179dd66f | -6.08333 | -42.37843 | 2024-10-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf7af696-e464-3928-a08c-e32ab7502544 | -6.08036 | -42.37967 | 2024-10-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc765605-a7cb-33aa-83fa-b3bf7dad3a58 | -6.07819 | -42.37781 | 2024-10-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7108709-4850-3838-8951-f9a78ba255f4 | -6.0007 | -42.90253 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 45fdbd8c-7774-38b5-909a-55ebc18044d6 | -5.99928 | -42.90052 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 551ec32d-7ee0-3a5b-86a9-037f7398db78 | -5.99852 | -42.90576 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e121e366-6d09-34f9-90bf-f2545edbb7aa | -5.99575 | -42.90191 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0ee3b217-03d7-32a1-a7b2-ec565d1692a6 | -5.99433 | -42.89989 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5552f5f6-49cc-3ba7-a9c1-8cdb3e3af553 | -5.99357 | -42.90516 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1212d815-d9f9-38d9-b0ca-ad26d215c047 | -5.99079 | -42.90131 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6f6398a7-1536-3ead-ad14-e3bff4e17eb8 | -5.99006 | -42.90662 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0993aea1-7406-3fa5-ad88-d68e8edce2c0 | -5.98938 | -42.89927 | 2024-10-10 04:44:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a09c2fae-7241-3569-9611-9ea6599d6e44 | -5.87392 | -41.95509 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a2f9bde9-71b7-3c79-9f9f-51f24cb9b2f2 | -5.87347 | -41.95826 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 300e0d87-0b8f-3c8f-96bb-670cb89ae1a0 | -5.86819 | -41.95768 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7ad9f569-b175-3c0d-97e0-bc2ee425786a | -5.86245 | -41.96031 | 2024-10-10 04:44:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9cb9f10a-3315-34d8-a5f6-b8974fb160f8 | -5.75609 | -43.19329 | 2024-10-10 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ee0fab6d-df23-3c64-8402-965c401d8ee1 | -5.75515 | -43.19551 | 2024-10-10 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ff4c45de-bf2e-3c62-a114-a162dcf641a3 | -5.75127 | -43.19255 | 2024-10-10 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ad76040e-4b3e-320f-b3af-c1bdfaeaf6d0 | -5.7511 | -43.18931 | 2024-10-10 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c04a4e96-ef8d-334a-a97d-b7a273889975 | -5.75033 | -43.19478 | 2024-10-10 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d13ac7b9-b3bb-3425-9c38-3ce4d677ff90 | -5.74647 | -43.19173 | 2024-10-10 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7282e3ee-b193-3abd-9f34-74c243da3eb9 | -5.54007 | -42.92945 | 2024-10-10 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 06dd2422-7aa9-3de9-b828-226d3cd631b8 | -5.53706 | -42.81158 | 2024-10-10 04:44:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 50c9fa9f-1d22-31c6-8042-f4c4ccfc345c | -5.50903 | -42.79624 | 2024-10-10 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e9d2855-0287-314b-bf43-d0c2ff1d8703 | -5.50409 | -42.79552 | 2024-10-10 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a059f04f-a4e8-35cb-8a5a-65d045adc7cd | -5.48591 | -42.78145 | 2024-10-10 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0a170181-7283-3e67-b438-f7762ca447fb | -5.48476 | -42.78 | 2024-10-10 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 99535945-11fd-3424-86da-53ef6bc39970 | -6.44119 | -42.92968 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bff0d476-41d1-35a0-8b24-e1d57a35f71e | -6.37199 | -42.98109 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24101487-074f-3899-8e5e-305f57ab241f | -7.73037 | -43.80642 | 2024-10-10 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b54c82b3-d1e7-320c-9907-7857163f601c | -7.7256 | -43.80581 | 2024-10-10 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3746e7d9-93f9-392a-9a9c-225ede52f453 | -6.72416 | -43.56174 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d43793cd-860d-36ec-b36e-b6e72a84142f | -6.7201 | -43.55602 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71f67af7-7907-30ff-908a-db3ce219797d | -6.71938 | -43.56109 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a004f008-5a80-36b9-975a-7b31ed509fde | -6.69078 | -43.45499 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a24f3cf-60e5-3c5b-9d23-965ff54f3593 | -6.69011 | -43.45658 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35869d0c-2c62-325f-9a3f-6ea81cf241b5 | -6.68596 | -43.45439 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f5fb6d7-b943-34ff-a5ab-1a1a2095ea19 | -6.49176 | -43.34524 | 2024-10-10 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7957a8d2-02e0-30c4-b38f-d34da4db61c3 | -6.47268 | -43.33392 | 2024-10-10 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75b44cd3-0431-3d49-8492-5663a9c3d616 | -6.46909 | -43.33184 | 2024-10-10 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8e4fdeb-8ddc-3228-8ae0-f19928560454 | -6.46786 | -43.33317 | 2024-10-10 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebbd2017-ca9c-3e40-8f5a-cc799ed8dcc6 | -6.43806 | -43.34227 | 2024-10-10 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 564a179e-9c87-355d-b1ba-63f336d69d4b | -7.82713 | -42.46336 | 2024-10-10 04:44:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 13ffede5-606b-3995-b6ba-772cdf9a10b7 | -7.82667 | -42.46674 | 2024-10-10 04:44:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 35f2b9f3-630a-35ac-9536-42e371223dc7 | -7.79826 | -43.08585 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3835950-3a44-32d1-9890-8b5abe73bb0d | -7.79804 | -43.08669 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c89af098-d7a0-3f03-a4d6-e7f315639a86 | -7.79787 | -43.0886 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| da765281-f6ce-35ee-b6c5-278544161433 | -7.79767 | -43.08944 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 84b89af8-d976-3bf0-a744-df3ef23d7538 | -7.79748 | -43.09135 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8fd269e5-1f49-3189-913e-a8bbc4d492ee | -7.7973 | -43.09221 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6fe8e57f-6208-3a39-8a6b-b4a34e3a5db3 | -7.79129 | -43.09911 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 582ccc58-11f0-3246-9744-bb2db4b6d5cb | -7.79089 | -43.10189 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9431c1fc-1c56-304c-af05-ab8b490a3b07 | -7.72821 | -43.03822 | 2024-10-10 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41b40fb4-5175-399a-b0a1-d8d46beb4b84 | -7.72782 | -43.0411 | 2024-10-10 04:44:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c1ea62f-420c-3517-a9e5-6b61b0f33970 | -7.68887 | -42.99079 | 2024-10-10 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4e49a95a-ce8d-3c37-94d8-774134043458 | -7.68847 | -42.99362 | 2024-10-10 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b043163e-764c-3156-b3de-f09a936129d8 | -7.68808 | -42.9964 | 2024-10-10 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 23977bf0-ade1-3d85-97d9-ce1b8cd23814 | -7.68345 | -42.99285 | 2024-10-10 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dce7c3e0-9a3e-37b6-98f7-1103201a2dd6 | -7.67367 | -42.49157 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 00a5d653-df63-3d62-8895-4c477d2785ea | -7.67325 | -42.49469 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97433ac7-a58b-3276-a3fb-0821bddc9e21 | -7.67296 | -42.49094 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3aaa64d4-aede-37a6-9ee7-4ad82ac001bb | -7.67284 | -42.4978 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a978639-3820-34c3-ab77-3e742683c792 | -7.67252 | -42.49405 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README96.md)
