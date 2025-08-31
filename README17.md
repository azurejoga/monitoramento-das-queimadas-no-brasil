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
| 646b13cc-ae0d-3f1c-a6d5-5497eb1439f4 | -8.95523 | -50.00859 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fef6ed68-5968-3e21-87bf-6c771b8b31fc | -7.96629 | -46.41212 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d5309c7-ed73-372c-9ecc-0ec0bfbd43e4 | -7.49138 | -45.05701 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b308504-df31-3ad1-939e-354f7143a898 | -10.04307 | -46.02511 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6e19a0d-690c-34db-8fa6-28be0d322d2e | -8.9709 | -50.03101 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceb5fa7d-887d-3f3f-9183-3aaa85aee886 | -4.91451 | -42.09018 | 2025-08-31 04:02:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 357d21c6-e98b-3003-95ed-3060086c3aa1 | -11.26938 | -44.932 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3824ec7c-d0f6-31b8-a8b7-6ea44eb6bd0c | -11.02301 | -46.99625 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e4c5d68-7035-38e6-985d-28b1ffa5514b | -5.55057 | -44.2992 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bd8c4b7-1791-3de0-9dcf-d2136362630e | -6.49248 | -44.16962 | 2025-08-31 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc0260a1-323c-3a9a-8ef8-3b1ebda138b7 | -6.20212 | -42.74793 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f828a14-35cb-3317-9db0-650142c3fbd1 | -9.59047 | -40.36448 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4693d38-e17d-3dc6-b271-52f0261e3ac1 | -7.95911 | -46.38257 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fecf3b73-5145-34f8-ad43-e700c40a117f | -11.36312 | -43.59722 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cddac397-b5a5-3b4b-9298-527f99259cf9 | -11.20993 | -45.04472 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65b7f9ea-1e30-33c7-8635-f6e12657da8a | -11.33591 | -43.63274 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee727823-6825-3afa-84a0-0a02be7527c3 | -7.65685 | -42.7066 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9dead826-3488-3887-9e7e-5a805c3864fe | -11.30099 | -43.67117 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49550899-5ca1-303a-890d-042997cf9e12 | -9.68395 | -47.04537 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be29aa67-fffe-3855-a4ea-cd4122acab90 | -9.62351 | -47.80156 | 2025-08-31 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de2444a3-c233-3d26-88f1-d68eb5492bbf | -8.32983 | -47.42397 | 2025-08-31 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 175b112d-bbf3-371f-85c8-6f305c46bcd4 | -11.01291 | -46.95391 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a1c9085-92f8-3a12-b60c-b621629e4883 | -5.99247 | -43.36214 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ddcd379c-ed06-3291-9f6c-271799583759 | -6.83977 | -44.25505 | 2025-08-31 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bccdb015-a7dc-387f-a56b-9ea5858f0746 | -6.9655 | -44.31703 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56cbc59c-14a6-35df-aad4-461dbe220240 | -7.0574 | -44.88182 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6808034-e85f-31a5-83f6-89614dad080c | -5.59087 | -46.3222 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d217c4d3-d9fc-36cd-a2b7-764d2bf083a7 | -6.36129 | -43.56269 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b81f016f-7390-39ca-a3b3-ca098f2d5f55 | -10.77838 | -48.81812 | 2025-08-31 04:02:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbb59a80-cb39-389a-9ce5-b1ef50adbd83 | -5.25109 | -44.45546 | 2025-08-31 04:02:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45dafe19-96be-30d2-83a0-021d6fb363aa | -6.57702 | -43.68716 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ef3170a9-0169-385c-b399-c04984c45eaa | -6.52788 | -42.95381 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c65602a-63d8-3e55-8552-6d85ff7b6520 | -11.29573 | -43.63814 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dc8c651-a191-312f-8311-02da189baf6e | -5.46043 | -42.57684 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f41f2a31-bf5f-373f-9d96-0bcccb7168e5 | -5.79916 | -43.87383 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f9b5b7a-99a4-32ed-9b40-56b50c2ba4a9 | -11.36597 | -43.55795 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1caedc9-0e65-3522-9b12-6393f30165a7 | -7.9615 | -46.42059 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23734080-b86f-37ad-85d4-af90d6d64756 | -8.95582 | -50.00528 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bef85f9-5aec-34b5-8c6d-71b92c5e06c5 | -6.57674 | -43.69315 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b01f030e-5680-30dc-bd4a-15a57ed0b4c9 | -7.6256 | -42.65834 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5902935e-d628-38de-8c86-fb566d4b7873 | -11.34333 | -43.52239 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33d1b67a-2a0e-39f0-8c72-274c5331189f | -11.29694 | -43.56627 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07579e91-0514-3a3b-81b1-db7e6fd12982 | -6.50484 | -43.55693 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff1b858e-c625-3f8e-8fe9-3d8aa9978379 | -10.41569 | -50.85838 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf7fc498-db6e-39fe-bb43-48b3d2b9dda5 | -4.07609 | -47.95817 | 2025-08-31 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbcb0318-6894-3538-bf18-e560bcf0389b | -6.27785 | -43.54427 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7317b09-6f9b-3089-85dd-a6aff2d5da95 | -6.51789 | -42.94812 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c37e81fb-d06d-3055-aded-7146a9284691 | -7.78676 | -45.46333 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81e304be-f378-3af8-83cd-5598b108ad15 | -8.2952 | -44.92358 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0613f667-7049-3e4e-a787-64af30b6c62b | -8.85508 | -45.73129 | 2025-08-31 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e0520e5-a779-377b-a509-275f35177663 | -7.40556 | -49.5153 | 2025-08-31 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c967e154-fdce-3f34-b345-5f5883f12591 | -9.95739 | -46.34941 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 385236cf-31d6-35c1-9eb9-ed97861c6fe2 | -8.73037 | -50.37401 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a6a42480-0c99-3458-87df-92fb21a204f4 | -6.2506 | -43.38881 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5be88439-2666-35e5-ac9e-434eb852d424 | -4.94459 | -47.58056 | 2025-08-31 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f66e0f1f-9a0c-3a0f-92b0-a914e2d6758d | -6.18367 | -43.31439 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f010bcce-51d4-3e09-b830-bd820711f635 | -8.54527 | -45.80363 | 2025-08-31 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 238ce1a9-0c8f-3b73-8e40-bd7f7a2ec9e7 | -7.33258 | -44.09421 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eb9adc3-62a3-381c-9437-c54fb40c3deb | -6.25629 | -43.37671 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56918f59-a545-3c84-94a7-ab6b4fc06168 | -9.68898 | -47.04202 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d478a0fb-51ae-3a53-ac93-28a1606bc223 | -11.29791 | -43.64657 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84acec54-750c-32e4-8e31-cee492e7dfca | -11.3158 | -43.68987 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 712a8c51-05dc-3bba-8145-0b2e5e1fa791 | -11.32445 | -43.659 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3b68439-3333-382d-8737-5700589d9eb2 | -11.34397 | -43.51853 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eabc5099-a11c-3e32-8d22-c462c7d1c5a9 | -4.55185 | -50.47664 | 2025-08-31 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cc30c32-a0de-3662-b8cc-7f0d6927dd28 | -6.31199 | -43.51941 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 070a2574-d8ff-3243-8c9d-be26ec225439 | -6.23986 | -41.82137 | 2025-08-31 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 28dd2d1f-59dd-3e87-a722-660c4d4f63e4 | -6.95261 | -44.30081 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e57c9481-f9f3-325b-befb-02fc0f89ed5b | -7.18646 | -43.84228 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16186d56-b7d9-3407-86da-b1b1b25f36b0 | -5.91171 | -43.44277 | 2025-08-31 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfc2b84d-6c24-3346-b387-9c713396e0e1 | -6.70697 | -51.417 | 2025-08-31 04:02:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| d1245d78-c00d-3a98-baf5-d276d38988f4 | -6.88656 | -44.43864 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64e15de3-e99c-3ea1-b9cc-2fe7b4bcb14e | -5.53033 | -36.85249 | 2025-08-31 04:02:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 32cc25bd-80c4-3481-89c2-184ceeae92ff | -11.34679 | -43.52296 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6783fd03-478b-3f7c-8414-460a7abff9a6 | -9.58932 | -40.35001 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| feb9cde6-c050-38d1-b771-9e23920694e1 | -6.62132 | -43.73933 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0c62a8c-f211-36e2-8b99-cb4bf7286314 | -11.30642 | -43.65995 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e0c365c-742d-3475-9f26-d39a37d4f676 | -6.57923 | -43.69656 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aaf1ff47-ef1c-3fc6-8558-99e0c24109ce | -8.29986 | -44.9194 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 209378d6-637e-3215-bce0-d8f64b17a439 | -6.83306 | -43.33585 | 2025-08-31 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 806e3580-f906-3a8e-ba42-3ef9ebe1f820 | -7.11313 | -44.76419 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fce38101-fdfd-3450-9714-5c8b58ea503f | -11.07348 | -44.62721 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9921b251-d807-3125-ba23-0890473626c1 | -11.3606 | -43.61273 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00264db4-0c13-3dc3-adaf-0c79bb112255 | -11.41691 | -44.68518 | 2025-08-31 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fed82fef-a075-3735-9163-d8209985d4bf | -9.59155 | -40.3575 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 5e3f262a-ec99-31c7-886a-8349dcfa4136 | -6.17763 | -44.79781 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35148fde-ad53-333b-a489-31fec03f2674 | -5.80443 | -43.86531 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6283aebc-9ab4-3ecb-a3b8-3905975b4032 | -7.96416 | -46.42431 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f0db606-8e0b-32b2-810f-06d634c3ebc2 | -4.55779 | -50.4776 | 2025-08-31 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7fb2b77-31fc-311f-ab35-f0dd17ef5db8 | -7.58864 | -42.71981 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c2b401a9-8091-3d80-95ca-3eb6dff3f167 | -7.63314 | -42.65566 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 260f7345-e618-3c24-b0d7-d686e5b2869a | -6.44523 | -43.96274 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 387218f3-f127-32d7-9419-c88b284ce29c | -9.68955 | -48.29527 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8319f6bb-18b3-3a5d-9cfb-13ffcb88bc0a | -10.04034 | -48.08782 | 2025-08-31 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe0bd8e0-2ea8-35f2-9f30-f74a8db7fbe1 | -11.02369 | -46.86671 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 130e7546-890f-3483-8b72-f0ea1d6e6d8c | -7.61805 | -42.66105 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 755595a4-fa22-3712-89f1-b72c0ad0fc82 | -6.43245 | -43.97025 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b9a4d5-b2a2-3426-9839-ab91c8fd2d08 | -8.46389 | -43.63214 | 2025-08-31 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7ab2b15-4fa6-3de3-8e2a-34e0a8f76cbd | -7.95353 | -46.38969 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8fe258e-5a86-3ce7-8e2e-787105eda921 | -6.4452 | -43.98613 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README18.md)
