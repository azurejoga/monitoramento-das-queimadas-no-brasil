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
| e7e84339-9825-3a70-9c48-b1cdcc308178 | -4.43771 | -43.4053 | 2026-08-25 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 488e72f9-91dd-3d9b-a39f-341145d93cce | -9.03526 | -50.81961 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20071df4-4f6d-3028-89f9-7e4b546037f4 | -6.17562 | -53.48452 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c141e10a-ec03-3104-92c0-68c0b4ad5362 | -6.13378 | -57.86014 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade5e90e-193c-3b02-9dbf-66393361556d | -6.32579 | -54.76166 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fd7881f-29b0-3a36-955f-45909c766546 | -6.32709 | -54.75422 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9186ac44-2038-3677-9090-d4015e31fbad | -7.26591 | -45.37405 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 250ab690-86ab-3aee-aee6-975c03bec5f8 | -6.97318 | -42.09127 | 2026-08-25 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cd2ab100-e0d9-322d-bd91-107d2b7aa0be | -8.57241 | -54.85937 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26c6d9da-580f-33e5-9580-183fff35091e | -6.41871 | -43.0757 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c13c98a-2793-3f94-9896-794cd398e228 | -7.31629 | -42.9767 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5fffbdc0-d83a-381c-8d2a-c2ac40cfe076 | -7.28232 | -43.01855 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83d27ca4-117f-32bd-b9ee-9b2817b0f5b1 | -10.36546 | -45.0573 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bea6755c-13de-3e33-8cbc-ab57049af9c7 | -8.07781 | -47.53215 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de010dab-ee0a-382d-971d-f2b3caa065f7 | -7.98133 | -45.25403 | 2026-08-25 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d75e0b41-e389-30f7-9955-579c19d31ef0 | -5.86431 | -50.14346 | 2026-08-25 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88f335b7-7536-3b48-b567-fa5605f6fc5c | -9.97534 | -48.3194 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bd5c4b9-23a1-3c0d-9d72-157abd29e360 | -9.05458 | -50.80524 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f0b4c98-c149-3557-ad98-3fe5bcd4e72a | -6.43945 | -54.97578 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c8b7a42-5304-363b-b7ea-7763c942ee4f | -10.04357 | -46.40583 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49158f5b-6e47-383c-beb1-7e0c9fa50075 | -5.91837 | -49.67606 | 2026-08-25 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa55e95-5c79-3cc8-8e58-2ff6ad705761 | -7.90095 | -46.37431 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 563a1f58-e04d-3801-ab94-7b7ac14ffcfc | -8.61539 | -47.14 | 2026-08-25 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18139c0b-dad2-30fc-9075-79bf631e2788 | -7.38408 | -55.17557 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4cc1137a-a136-3643-be71-24e0d1645172 | -6.65492 | -43.90432 | 2026-08-25 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7cab4f1-580f-3414-a1bd-6836513c932a | -6.98003 | -41.30975 | 2026-08-25 04:25:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c2127ea6-7358-3f71-9c7e-9150d45bd97d | -5.39467 | -43.60409 | 2026-08-25 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf1d1fee-3ddb-30fc-a5d7-ece6a0a2960b | -4.05171 | -48.9621 | 2026-08-25 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84252475-2794-3960-b9dc-4fda6a76dd63 | -4.80054 | -43.07874 | 2026-08-25 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e43035a-4652-35df-b4cc-7af82918d8e5 | -7.43604 | -43.08709 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59cffb4d-fb9e-378d-97d3-2763b438b7b9 | -10.33555 | -48.22339 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 447dfc7c-b10c-3e9e-a309-607f3a167ddd | -8.10222 | -47.46929 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e706401a-5ca3-3ad2-b871-d3a80ef1a184 | -9.03333 | -50.78193 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be9cd13f-c59f-3235-af65-27adf70ba264 | -6.14596 | -57.95193 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73f9c7a5-ef6e-3085-a83e-7f312f17a381 | -6.6344 | -58.49023 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 57669bfb-69cf-39d2-8104-b4e96564bf5d | -6.62273 | -53.19211 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6f20fbc-78d4-3c5b-bf2d-19b59c9f7914 | -6.94739 | -42.68863 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d2e21c7-6e2a-34d0-a7f1-9d6be5a9acc6 | -6.0304 | -44.91772 | 2026-08-25 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 472ff0b0-2bc5-3afa-b00d-0bb83e1b81d7 | -5.98089 | -45.33551 | 2026-08-25 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d6f5fc7-71eb-345f-9098-e5860be5eb29 | -6.33395 | -54.74782 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10497545-b79a-3ee7-8530-cdf1d975564d | -8.16129 | -46.69594 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb43c6c3-59a3-36c6-bde4-c5365350f4a0 | -7.75752 | -46.14806 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edc4ae98-1f47-3a5c-a0fe-c9398cdecea0 | -6.45439 | -43.09627 | 2026-08-25 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05bb95f2-ec5b-3154-9289-bf2ff18cda08 | -6.61031 | -58.39067 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52d38340-22ec-3da1-9662-2c29c3ac0655 | -8.57168 | -54.85282 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9352a75-0ccb-3acd-924d-8d05f8b8751c | -7.38627 | -44.56872 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3147fb09-12f1-3e27-b14c-1447838920de | -7.28635 | -44.0789 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90494844-3bfd-3c34-a2f8-0324061ad8f3 | -3.85759 | -42.94543 | 2026-08-25 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed47752f-8be5-3a3c-aa27-fb59a9e8a795 | -6.41582 | -52.72638 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c661fd1b-4b9f-37b9-9056-4324aae5299f | -3.01342 | -51.05086 | 2026-08-25 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6c8e545-6dce-3ea6-9dd7-1e6d9e0edf34 | -6.78523 | -44.69765 | 2026-08-25 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5457698-2d96-3c38-8be4-248cabafbdf1 | -6.19154 | -53.48431 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0a2e9a7-8075-3ad0-88ba-53e16a1cbe88 | -6.35832 | -54.76285 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbadb58e-3a1a-310f-a28c-35fab2982903 | -6.22283 | -55.92433 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a2b1778-5c79-3d03-90e6-cc2dafa96308 | -8.93165 | -45.75214 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7bfa42f-db4c-330b-adf9-9abc5a927aad | -5.00489 | -56.13818 | 2026-08-25 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91274ff4-de30-3379-a894-d92b91f18777 | -11.12716 | -44.47493 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd81b51a-02bf-3b44-a6be-8f436ef0f492 | -5.91333 | -52.13875 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 166fa132-45e3-39a2-a4e8-1e340527919b | -4.43382 | -43.40829 | 2026-08-25 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86e00b2e-ffd4-33f0-b95b-afa1ca67690f | -9.69555 | -46.05434 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c764d5f-edbf-3f09-a51b-75df70b036fe | -6.16744 | -43.76736 | 2026-08-25 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7817e17-0338-3019-b4b6-7eb68b393e86 | -6.6374 | -45.15969 | 2026-08-25 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 871488f8-36b8-32db-b202-a43788ce22db | -6.63052 | -58.51062 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b22d5157-92b9-367a-80a8-beb6cc591afe | -7.35475 | -55.66618 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33243164-6fe2-3169-a173-487706064dbd | -7.14679 | -42.7574 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8a8ed82e-4355-3ee4-b81b-3028b83ea9d4 | -3.54116 | -48.18436 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 609c7bbc-e53d-317d-9ff1-183ebdc935a4 | -10.7145 | -47.75576 | 2026-08-25 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95d77511-a376-3701-ae9f-d829fcd7bf60 | -11.13674 | -44.48016 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f8b46611-7b0b-3c9d-b2a4-db57e22385ff | -7.3097 | -47.33549 | 2026-08-25 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de5256d0-0453-3b65-ba16-e2f3b181947a | -6.3543 | -54.78522 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6450315-0990-36c2-a8e9-1c439e1131f8 | -6.58765 | -49.62054 | 2026-08-25 04:25:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfd0d415-2a4c-3294-83e1-5ebd724a4b5f | -7.38344 | -55.17909 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b208c2c8-9a54-3f08-ac5d-fb3c6b2c6950 | -7.15945 | -42.79078 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 00ca1bc3-0494-3047-b7bb-6d234df4c9a7 | -6.55593 | -56.55783 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fae394b8-761e-3eae-8122-9c4318453633 | -8.57872 | -54.87583 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 710d2ab8-f4d0-3832-8f54-08963302d276 | -7.06686 | -45.0012 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9ec72d8-686a-3a77-8a57-fd478cc44897 | -7.43717 | -43.10268 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 79991ec4-3a98-3c54-87b5-76384dffe704 | -6.0055 | -42.57756 | 2026-08-25 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16888414-cf70-32da-ba7f-9dd0d75d08f0 | -6.80824 | -42.67941 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc06b232-2b21-3999-a646-441a9913e31f | -6.22206 | -55.61865 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 844544fa-407d-3662-bc1a-f13bb764306a | -5.48585 | -46.62292 | 2026-08-25 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6f86303-4426-3519-8839-68067e094f52 | -6.61157 | -58.38409 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9627e54d-071d-3f9b-b1fb-f0f3763ab60f | -3.53793 | -48.18157 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| cc07065d-a2b6-3bcb-8856-8cdd1934832e | -6.32644 | -54.75795 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 501d3d99-40b1-3b40-a28f-df5934452655 | -4.18098 | -49.40212 | 2026-08-25 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41092ce1-9ad6-3af5-905e-0f0623fbab17 | -8.76211 | -45.79245 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfaa43f9-393c-37ef-898e-5dc819c26cae | -6.3396 | -54.77085 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa38585-7eda-3cae-8ec8-7c03541d3f32 | -3.53361 | -48.18318 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e9559316-0016-3dce-bd60-c951905060a5 | -4.71819 | -42.76947 | 2026-08-25 04:25:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4d41a08-d454-327c-af17-6ac8d7e651d7 | -7.28852 | -45.35988 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 50026836-3e17-3e0b-992b-f7a44b7307fe | -8.09849 | -47.49232 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23248003-dd79-387d-96d5-97485b834807 | -6.4578 | -43.09678 | 2026-08-25 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92aa2bd8-ca29-39c0-a043-088d9373bb3a | -6.94087 | -52.78734 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f11569d-69aa-3ee9-842a-2ec9205fc8d9 | -6.62485 | -58.50248 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 13d093a3-6da1-36e5-84f4-4207e824315a | -3.96909 | -41.51963 | 2026-08-25 04:25:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66419854-91ac-372b-82f4-79d591a33589 | -7.49353 | -55.36031 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c884d0b6-4a66-3e1c-82b0-5aece7baa234 | -7.15318 | -42.73872 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 17925596-20e3-3c9a-a728-23e0e3d4bd0e | -2.89146 | -48.80415 | 2026-08-25 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 837666c5-e32d-3f43-8a3c-fb584a22ba4a | -5.68417 | -43.27307 | 2026-08-25 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03a541f2-ef64-317a-8869-3fa22b3492ca | -7.48717 | -55.36301 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README35.md)
