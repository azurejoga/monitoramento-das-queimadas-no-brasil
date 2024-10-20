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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f92c493-b114-31f9-8b4f-580a6857edfa | -4.97734 | -46.49826 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68d1b1d3-1c61-3a95-bf7d-d0164e8ca214 | -4.97509 | -46.49075 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59222eca-6c3c-38e7-a4b9-c46852e4e30e | -4.97454 | -46.49424 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99747f33-5dbe-312f-9d11-e6bacd1e2223 | -4.974 | -46.49774 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 460dce97-853e-3cbe-87aa-c31bdd436cc0 | -4.83235 | -46.90136 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad0fa67-5d72-3b89-a5ed-28175c407a5c | -4.83181 | -46.90483 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7f1730c-169e-390e-8e78-870abe808d57 | -4.82963 | -46.90094 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2de6456-d8b7-34ab-96d1-215b28d63457 | -4.82909 | -46.90442 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96d71c8a-8d61-323b-ae37-137c033c2a54 | -4.65367 | -46.85608 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a14d05b1-54da-3668-a72d-52c627611756 | -4.63888 | -46.40977 | 2024-10-20 04:32:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1ce13eb-3fdf-3938-ad4a-5e55aeb0ada7 | -4.61554 | -46.64653 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 953b0060-d63c-30bb-8f0b-522a0d136880 | -4.61185 | -47.5335 | 2024-10-20 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c02f4c-05a8-3e5a-82b4-bd3253aa6383 | -4.60853 | -47.53299 | 2024-10-20 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 958e9de1-db8e-3f57-83a0-d59229d72a9e | -4.60798 | -47.53644 | 2024-10-20 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94719e61-e3c4-3afc-bcbb-23603a6b3d11 | -4.60466 | -47.53592 | 2024-10-20 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82eff048-3c43-306b-8d6a-47b032279098 | -4.24102 | -46.61714 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39ce03ae-ad0e-3dae-954a-2b7290077144 | -4.23823 | -46.61313 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6af8f55-046a-3e13-b8fe-c56bdfac2c18 | -4.23769 | -46.61662 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c54b582b-9b69-38a8-bccb-85e7bfef4b36 | -4.20128 | -46.63593 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 3e74e620-a526-3545-97f8-5e94d75b3997 | -4.19849 | -46.63195 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99b9c6ce-f00e-3fa9-b2c4-808b2404da99 | -4.19795 | -46.63542 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5b7fd629-6173-3678-9f0c-6e9bf47180da | -4.1957 | -46.62797 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5afd67a-1901-3889-a8ee-5d1da0999b56 | -4.19462 | -46.63491 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| fef45f6f-d4c0-3810-922c-246cc32d2a73 | -4.13701 | -46.84995 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fcf2459e-15b8-3f7e-9a03-59a4dcd979bb | -4.13369 | -46.84943 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 497cf98f-9700-3703-8eaa-3ecfcc9e90c9 | -4.12818 | -46.8628 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d1f91b4-019d-3c50-a686-db4c5f0efe80 | -4.09346 | -46.91055 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f6fc498-7402-3302-92f5-172c033b978a | -4.04189 | -46.94104 | 2024-10-20 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46cab9c9-a269-340f-96fe-8a89e92c9f37 | -4.03803 | -46.94398 | 2024-10-20 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| dcb871a4-b471-33b1-a5ee-2faf73dc9ca8 | -4.03471 | -46.94345 | 2024-10-20 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3e7f8d17-56df-3aff-8886-f12dcaf073f2 | -3.96334 | -46.40228 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa115521-64fb-32ef-9734-669d4059eb37 | -3.86575 | -46.9171 | 2024-10-20 04:32:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4307a355-c3d0-35a5-acb5-a704f1300457 | -3.81535 | -47.49649 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b3ee601-078c-3e99-b6d1-6a2fd0f25b2f | -3.8148 | -47.49994 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16ccd624-f725-3fba-80ae-fecf33cbbded | -4.1974 | -46.63889 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f9303128-795c-3c2a-a14e-7f5bd221e2d8 | -4.19516 | -46.63144 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45562789-1982-32f4-9346-de3f150df588 | -4.19407 | -46.63838 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 88fef193-d6b7-3d65-b8f5-12be5f2bfd14 | -4.19237 | -46.62745 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fee56350-9027-335c-aa4f-e8a8bab8598b | -4.19183 | -46.63092 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 496dadc7-444a-377e-8331-d83483ca2388 | -4.12764 | -46.86626 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc4ab25c-3787-36e0-8622-94fb6ca675af | -4.12486 | -46.86227 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81ca1e36-dee9-3450-ab79-39e9abb8c079 | -4.12432 | -46.86573 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f808405e-fb79-3a6b-b05e-a01b3d8f643f | -4.09624 | -46.91452 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5287cba-bb95-3ced-a352-a496ea2d00a7 | -4.09292 | -46.91401 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc77f837-045e-3c50-af6e-70f64fbd8021 | -4.09238 | -46.91747 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1397070e-96e3-3396-a811-40ee13fc1ace | -4.03857 | -46.94052 | 2024-10-20 04:32:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 874be318-86fc-32db-b9fe-950fc93ccf67 | -3.96 | -46.40177 | 2024-10-20 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3708a247-3240-327f-8111-b14da9ec6f27 | -3.86907 | -46.91761 | 2024-10-20 04:32:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cedb800-919a-3e4f-8ffd-692a9698462b | -4.4717 | -47.7344 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b40c827-6d97-37dd-9261-2735d5a25b39 | -4.3204 | -47.53352 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7863a286-2bf3-3abc-8836-2529c40f88ea | -4.31986 | -47.53698 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 963b7981-260b-3acf-a39e-7017c6fad843 | -6.31387 | -47.22516 | 2024-10-20 04:32:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d61d1d7a-5f12-355e-8d97-aafe19e7f3c2 | -5.43277 | -47.25814 | 2024-10-20 04:32:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58659083-7218-3814-804b-0d853ad0c1ab | -5.40284 | -46.90831 | 2024-10-20 04:32:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aae06569-d9e4-3dec-9de4-063eb3607a8b | -5.40005 | -46.9043 | 2024-10-20 04:32:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06da6bb1-670e-3bf6-bb43-f496a131e78b | -5.39951 | -46.90779 | 2024-10-20 04:32:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9f9d83d-5a73-3658-9312-14f097fc108e | -5.39672 | -46.90378 | 2024-10-20 04:32:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eed658d1-4827-3d9c-bac6-a79db8d1b357 | -5.39618 | -46.90727 | 2024-10-20 04:32:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f353f949-e855-35fd-9b0b-df72feae5dd4 | -5.33355 | -47.69648 | 2024-10-20 04:32:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9db17e9-d3cc-388b-bd46-e70547ac7fe6 | -5.32969 | -47.69942 | 2024-10-20 04:32:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 613ef36b-d820-3c05-be1f-f1a9bf470254 | -7.25489 | -47.91418 | 2024-10-20 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dbf769d-9e30-3663-b40f-d4a5cccd27c2 | -7.21412 | -47.33372 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7edc5ea2-3543-3690-a6ac-f081619ee18b | -7.21079 | -47.3332 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fab86fb7-3de8-32f1-a70a-bdfb0d42c46f | -7.21024 | -47.3367 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d03204ae-cefc-3d57-928d-3893e7e42724 | -7.14641 | -48.32097 | 2024-10-20 04:32:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 49a17554-74d9-3bc2-b4a0-f03c595f5100 | -7.14586 | -48.32445 | 2024-10-20 04:32:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c87ec18f-f244-36c2-923b-161a70ff0b89 | -7.10351 | -47.21623 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90c82393-10b0-3013-9613-74b8dad03470 | -7.10018 | -47.21569 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d59042b-4c0a-3c09-80e2-b54210c66f69 | -7.05893 | -46.83035 | 2024-10-20 04:32:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07099c40-4430-31e4-b05e-979c59413aa3 | -7.05557 | -46.82984 | 2024-10-20 04:32:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ee5c560-5120-3e20-b163-bcc715962313 | -6.93666 | -47.20431 | 2024-10-20 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a3beb07-be1b-3ddb-b1dd-d6f734b5e92c | -6.93333 | -47.20379 | 2024-10-20 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9211e7a0-c1d2-3813-95e1-5e76c020ff4a | -6.68746 | -47.36937 | 2024-10-20 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c812e635-4848-358e-a0d0-d624f979bbe5 | -6.63144 | -47.35706 | 2024-10-20 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 677f43d6-e3eb-3d89-b3ae-fcdab64098f6 | -8.71174 | -48.11264 | 2024-10-20 04:32:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b6ecc17-577a-381d-8490-6a6ed93a379c | -8.55875 | -47.8168 | 2024-10-20 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ec24e99-ff0e-3dca-b832-aa1bbacbb784 | -8.08231 | -48.1808 | 2024-10-20 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42261bbf-8972-30f6-bb10-d54b86c61dd9 | -10.67717 | -47.8026 | 2024-10-20 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90bc59f1-6e95-3547-b82b-7ea39e532cd6 | -10.55327 | -47.75011 | 2024-10-20 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3152b77-1ead-3237-a071-6ea7f4e703ac | -10.53307 | -47.66979 | 2024-10-20 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89a213fb-bc82-3d35-b8c2-779845215840 | -10.47335 | -48.28839 | 2024-10-20 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cb7001d-64c1-3c02-8d25-f15e36c98a2c | -10.47002 | -48.28786 | 2024-10-20 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9024dce2-c367-31ff-ad6f-267c643dfada | -11.12419 | -48.10875 | 2024-10-20 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f438d09-7d7d-3e36-be6e-db09a2b47faa | -11.12085 | -48.10823 | 2024-10-20 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47ae32e8-2214-3354-894c-5b5390d7d020 | -4.8995 | -48.28114 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30476eaf-b0cc-35b6-885c-0d87521872e4 | -4.89894 | -48.28466 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88d73034-aa38-3f33-88e9-305aa25dd5fc | -4.89616 | -48.28061 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4824ed0-f152-3ebf-bdbe-b864b43b1b0f | -4.8956 | -48.28413 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 899334f5-fbb4-3f90-a5cf-9ea6057d663e | -4.89403 | -48.56243 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f9f469b-38a5-3834-8cd9-e1afce89b9d7 | -4.89278 | -48.56252 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48d67c8e-d4ea-3e86-ac50-cb6787f48ea0 | -4.8761 | -48.21272 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dd887e1c-0404-3408-81c3-171a9b93f2f7 | -4.87554 | -48.21624 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 655a5c5d-cc78-3a20-922e-e9a854fd4fc1 | -4.87276 | -48.21219 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cc9b0ea5-010a-35e9-96be-f50af233d24f | -4.8722 | -48.21571 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 83d212d8-f986-3347-8713-00594149a6e6 | -4.86942 | -48.21167 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 05562af6-8fe7-30ed-a849-40efa9ffac4e | -4.85231 | -48.66565 | 2024-10-20 04:32:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4ed2ab2-ae75-33ea-b9ba-8f6a15daff13 | -4.83343 | -48.54563 | 2024-10-20 04:32:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2016a662-d971-33f6-9c6d-a44e3c72de2e | -4.83007 | -48.54507 | 2024-10-20 04:32:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e2688bf-dcaa-31d3-aa75-c1339a93ed46 | -4.81637 | -48.89224 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96ecda12-717f-30b2-9e57-2c9058a88581 | -4.72297 | -48.2996 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README35.md)
