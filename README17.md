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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e9d938b-47c6-377c-9338-f5af6b2f09c1 | -8.57839 | -46.33541 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91c99f81-2460-31b3-bdd7-2069044de0e8 | -9.15705 | -46.95477 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| c762133a-d437-3997-b113-d700c6217a38 | -7.85372 | -45.58458 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9938f08-1ba0-3afe-8086-b92ef25e2456 | -9.16866 | -46.95209 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0582e925-459a-3bb6-aa18-65bb2885c4ec | -7.37983 | -47.04408 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c01eacdc-19fd-3f86-b6bf-cc991783bc8c | -9.76206 | -46.76362 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9f3a4c8e-f1fb-375a-ba07-6747a174fed0 | -10.79032 | -44.10114 | 2025-09-18 04:14:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45eb33ad-2106-3709-aaba-8092f8c12dc8 | -8.59253 | -45.72214 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f225abfd-3dbf-306b-82bf-a578d1ce8fc7 | -13.95655 | -42.43031 | 2025-09-18 04:14:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77e6304e-2fd0-3fba-bddb-73e9fa254e3d | -9.86969 | -46.44175 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86a1fb26-1ee3-3e82-b6f1-9fa5d1480bfb | -7.32764 | -44.00222 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28123b40-63d8-32f1-a540-bae42c63f9da | -10.9249 | -47.84274 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1575a5e4-a69d-380c-b4c4-d82952e0de23 | -12.02373 | -46.72366 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 027a3c5d-b37b-3bfe-910e-2bf5ddf280d6 | -6.66549 | -47.74893 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85c1daf7-e127-3d4e-8fcf-58410ba5046a | -7.53779 | -44.72344 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffc78438-dd76-3a49-b081-21a1d65e2aec | -7.99984 | -43.81328 | 2025-09-18 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ea11fa6-303f-3161-854f-9bd506d69be5 | -8.35638 | -44.66687 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fda4182-b5bb-3438-a147-18c445cbf693 | -14.27885 | -41.42691 | 2025-09-18 04:14:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3531b956-0ae3-386e-b83c-3feb23411f38 | -11.37756 | -50.83574 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e3307820-be5d-315c-8c5a-f44227f7c917 | -7.81414 | -46.89495 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da418eca-425a-3e84-9738-a5f742ef60a8 | -11.99509 | -46.70261 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcc5d61d-199f-37c8-9680-67ab9ec7c9da | -7.98986 | -43.94009 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6ab67bb-9bf6-3ab0-9414-cae094086d13 | -10.63938 | -42.31028 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49d1320b-21b0-339d-b97f-636d7a1738fd | -7.52202 | -45.29636 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9856d157-08e6-37d8-9fa4-807af8ca70a0 | -12.41079 | -51.41981 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05eb416-a50a-3ba8-ae9d-af1389e178e0 | -7.54501 | -44.74297 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e6375ef-0d9b-37cc-a342-8fee641159a6 | -7.56172 | -44.76797 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d27bcd9b-7b30-32e2-8333-e5ba2e71b30c | -12.09582 | -44.82072 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d9888d3-70e5-3ec0-8a7c-7e2902a9b95e | -9.86338 | -46.4364 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd95973d-1bdc-30e2-95b3-c36157c32223 | -8.33364 | -50.9059 | 2025-09-18 04:14:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45e206aa-c40f-3cd9-9f62-b40069139276 | -9.75218 | -48.12494 | 2025-09-18 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 196ca8d7-dc31-3634-bd62-2d347fb63e4b | -13.2267 | -43.51712 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b6defd9-f2b9-33f0-a57a-ba86f5217453 | -9.15634 | -46.95903 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 7349df44-5700-3c75-8054-e4612c84e236 | -7.32932 | -43.99173 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e358147-f7c3-3d2d-bb95-5585baeedbbe | -11.16191 | -45.3468 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7e880bb-39ff-3f5b-9579-2e107be77bc8 | -11.37556 | -50.83849 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 91409085-54d0-3263-8570-42b967e81af9 | -10.6069 | -46.47277 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af428c38-9c32-34a4-a829-59c46f39fc22 | -8.72428 | -50.03632 | 2025-09-18 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9aa644b-1aac-3b9e-ae08-e60795805fbd | -9.06984 | -47.02785 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0ec537c7-6850-3691-8c95-93488d95e71f | -7.26602 | -44.90316 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66eecc66-6c0f-3169-8330-acea0c0a2cf9 | -7.21068 | -44.37412 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 618986e5-f0ed-3e64-a4a2-f26f1c201369 | -7.26825 | -44.91103 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 951787f9-cb10-3921-9fd1-b396506585af | -12.07907 | -46.56147 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 554bae85-d228-33c2-9301-a697f8d4dd9c | -12.90145 | -44.66739 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a30b7ed7-f7f1-336f-a9e4-480582669633 | -7.34266 | -44.58511 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f116979-2d3f-3433-b767-d38bce7fa524 | -9.06762 | -47.01867 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d51afca-9642-3f39-90b9-ccd5e8799455 | -9.16574 | -46.94727 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c5d8039d-788b-36dd-841b-637de3a3940c | -8.35303 | -44.66629 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f794eaf-692b-3341-9f7b-7c32dcf0ec87 | -14.49774 | -42.18084 | 2025-09-18 04:14:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b815344-56f7-3a6d-8950-667116f005f3 | -12.09138 | -44.82724 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39bf0b16-ebea-31be-8cb8-d435e4fe296b | -8.5919 | -45.726 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46b0e44b-a202-38bc-b9c7-78eeab6afa71 | -11.23333 | -47.43297 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a740597b-f7d0-3120-a6cd-0b824323ba3c | -8.14773 | -46.75544 | 2025-09-18 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd1f7670-cb6d-35ab-9a50-eeda4c93061b | -7.81732 | -46.89367 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a46b1256-1bac-3389-8107-a9eb4ea717b3 | -7.52083 | -45.30381 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a01c0c19-1a90-321c-b0a1-2e8a100dd757 | -8.13443 | -43.62809 | 2025-09-18 04:14:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7766c8ef-bf51-3a8b-b5f3-6fb5db6cb8ec | -8.01799 | -45.69267 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c20a16dd-f90a-30e4-89ad-a56550c53d2a | -11.17239 | -45.36707 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 543ecd0a-c5eb-3dd5-a72c-415ac66cc6be | -12.43764 | -49.73991 | 2025-09-18 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04570723-fc30-393f-88db-11300c01d44d | -7.45072 | -42.64032 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81d7d320-11f6-35e3-ae67-bc685d585be2 | -12.9009 | -44.67091 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 86d7d932-2a2e-3c66-98f2-9e94c2f4f140 | -9.03733 | -44.88673 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7f206e8-144b-3edd-94ec-eeecc3f38de2 | -13.53082 | -44.11656 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 31a63e6e-8b8f-3eeb-834d-f49eec876e02 | -13.08127 | -42.14141 | 2025-09-18 04:14:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bdf1e969-ab81-3949-b084-1750adda4138 | -8.07568 | -45.44942 | 2025-09-18 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 966197e9-e5ba-34ed-8200-75105ae68d9c | -11.18085 | -45.35735 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6056cda-5a1b-391c-80d4-d4c8ce1672e1 | -7.4529 | -42.62632 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 163b1d5c-1893-35fc-89e6-c31d22bd583c | -10.90999 | -47.8406 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d6300e0-3b21-30aa-bdd0-fc4cdc807b86 | -7.25092 | -46.60412 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 362c3814-7679-3dbc-9840-d4f4b7ba3439 | -7.54558 | -44.7394 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c89d187-c4b2-3ddf-8663-01c4a2e8ee85 | -8.6902 | -46.36131 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ff57990-10b1-3386-8cbe-792afc84a6bf | -7.81757 | -43.87007 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4accdb30-9e0f-3bec-84ce-a2d53dedfcc4 | -11.16846 | -45.37013 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 908760c3-26c2-36f6-9880-a5fd7d77d528 | -9.76138 | -46.76778 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c826e7c-bceb-3f2e-85e0-8878722c34d4 | -13.70192 | -43.57686 | 2025-09-18 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2538ef2-f8bd-3214-8fcf-e6866419ecd2 | -10.91372 | -47.84114 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0773a684-5105-38ae-876e-f1176c327cac | -10.92641 | -47.83361 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebbad8fb-515c-3655-8f98-6774f438ef74 | -8.59598 | -45.72266 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7abdd37-88ea-3206-a220-146f0e1d1517 | -7.86815 | -45.58307 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ac6279f-f818-3184-a81b-ff6b4fbe966f | -9.47036 | -47.93195 | 2025-09-18 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8a8c1bc-142f-34f4-abb0-0d5964346cd3 | -9.19248 | -46.94303 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9b986f15-b2d0-3528-b1ce-72175206406a | -13.70583 | -43.57376 | 2025-09-18 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1587316b-f216-36ee-9d7a-09716d9e47a6 | -8.90046 | -46.1391 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 560a7a1b-0fd5-3fa4-aec1-8c8b25cb7c0c | -7.85188 | -45.59587 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9168283-5ff2-36ec-b90a-7bdc1651badf | -8.01247 | -45.6926 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a222625a-84e3-3f2e-bd28-85dfe4e2ea23 | -8.07965 | -50.1586 | 2025-09-18 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47001cf5-ff86-3952-a7a6-7a88d90030f0 | -7.19492 | -48.60658 | 2025-09-18 04:14:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea18a6ef-4c27-3c54-b66e-02232c69b2f4 | -7.53953 | -44.71269 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b2a7871-5724-35e8-88ac-11ed9df59f59 | -9.13573 | -44.86618 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ae5cf50-31af-34ce-8bdc-1a5de1c1e3bb | -7.37908 | -47.04855 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b18cbfeb-c189-3ef9-80c2-06917a675249 | -7.51979 | -45.28842 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeb1d631-b0a4-396f-a401-bd728924d7b4 | -11.47368 | -48.70207 | 2025-09-18 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cfb5e18-adb0-3e85-9ef7-fc75812d837c | -10.62532 | -46.22871 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74c4a3dc-c1bb-3fb1-8809-39252e92a6c7 | -12.90863 | -44.66495 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1f283951-1732-3e6c-831a-edd8859d828c | -8.01192 | -45.79415 | 2025-09-18 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f595e344-485d-3a26-b178-0415ab6cf735 | -12.44211 | -43.56651 | 2025-09-18 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24bba1bb-d749-34e4-b1d3-ef421563de96 | -10.5361 | -51.5569 | 2025-09-18 04:14:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 933a562a-f23e-3b55-89e2-2a3596071731 | -12.01613 | -46.72636 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c135017-3a1e-344c-8f64-474c1848dcf8 | -8.05734 | -41.27352 | 2025-09-18 04:14:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 47d21eb7-ca3f-37dc-a576-09b25e6cf7ab | -11.18143 | -45.35374 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README18.md)
