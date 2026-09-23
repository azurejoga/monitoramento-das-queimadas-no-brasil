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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5240af83-9d17-3d0b-b016-141bbea7ef23 | -2.92668 | -57.77997 | 2026-09-23 12:23:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 01fcfce6-e75b-3903-aabe-7db4b4432d74 | -4.41808 | -55.4752 | 2026-09-23 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8b2e8038-516c-3465-9a30-2e6a57f2cb4a | -8.80658 | -48.77243 | 2026-09-23 12:23:00 | TERRA_M-T | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 31.5 |
| ffa842c1-d49b-30a0-9328-f11c32b1f100 | -4.07326 | -56.22026 | 2026-09-23 12:23:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 80e2236b-868d-3b4f-bf57-37686465fdc3 | -8.49745 | -57.60528 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 63c37a8f-6a8c-3334-8f1e-dd22840af4a8 | -6.56556 | -55.40937 | 2026-09-23 12:23:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7be6a056-7560-3e65-a73a-9819338efaef | -3.81971 | -59.0161 | 2026-09-23 12:23:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 56b6ea6f-2b59-343b-a41d-a124054b6a6f | -3.55302 | -59.04947 | 2026-09-23 12:23:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a14f7798-5179-3809-a016-79f7e112df32 | -2.72364 | -57.64898 | 2026-09-23 12:23:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 281743be-b3ec-3444-b85e-7de75066502a | -4.41939 | -55.46603 | 2026-09-23 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d3b332c1-5a17-397c-9e46-e9b97d2925da | -3.02459 | -57.932 | 2026-09-23 12:23:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9d10abb7-bc6c-3d3a-b8b4-382e3cc3895d | -6.36033 | -58.28523 | 2026-09-23 12:23:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 16c1c1b8-a592-3a1b-a95d-562f886dbcc8 | -6.69021 | -55.05627 | 2026-09-23 12:23:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 83ecc451-310f-34fe-becb-761200eb8ac3 | -4.27703 | -55.43089 | 2026-09-23 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5f6bc3ca-159c-3b51-8d41-c117ac86e118 | -4.83746 | -55.76846 | 2026-09-23 12:23:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 88966e1f-c4f6-39f4-aa52-c3fcf598f0a9 | -6.2073 | -55.26699 | 2026-09-23 12:23:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 57388f6f-949a-3da2-971e-da82b48037b9 | -5.3653 | -56.02224 | 2026-09-23 12:23:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d685a791-0980-3aac-99e7-c693afb0f7cf | -6.17675 | -52.04349 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| f4c039b8-fc7d-35a3-9419-658fdd2d12bf | -4.27832 | -55.42169 | 2026-09-23 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bd0f16ec-f47f-35cd-a3cc-8e073221a20a | -9.24463 | -59.57629 | 2026-09-23 12:25:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ec157973-f378-37c7-b0ca-00e0bde8b1ca | -10.8495 | -56.21404 | 2026-09-23 12:25:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5536d3bc-8844-3d8a-ac7e-f9a4839376d5 | -9.90061 | -60.36288 | 2026-09-23 12:25:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9a24249c-f5b9-30f4-b7bf-ff2a595ba6c7 | -10.61379 | -53.99716 | 2026-09-23 12:25:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 534bff48-71cd-38f9-b69b-a16f28746080 | -10.38836 | -54.40769 | 2026-09-23 12:25:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 194e5ad5-86b3-3ee8-be88-a62e6e70bb51 | -10.91688 | -53.94694 | 2026-09-23 12:25:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6924704a-9e74-333e-9839-bfd6ebc6e87d | -9.70422 | -58.13461 | 2026-09-23 12:25:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fea2f52d-d750-3dd4-8565-1ca4b2cae9ce | -9.70294 | -58.14351 | 2026-09-23 12:25:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8771471e-86ac-390c-b828-f1135e94219c | -10.39863 | -54.40881 | 2026-09-23 12:25:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d9f0228f-3e4b-3228-b490-2c2719a271e0 | -7.0164 | -44.6413 | 2026-09-23 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 864d52dc-bd33-357a-95a3-e611828b036e | -7.0352 | -44.6396 | 2026-09-23 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 208.0 |
| 4c6a755b-01cd-38b5-b7c7-b1f2cb71f388 | -6.9416 | -42.8834 | 2026-09-23 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 57534433-9657-3d80-9e9a-d4d9ea6b6f30 | -7.0349 | -44.6625 | 2026-09-23 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 5e3e44c0-bb0c-349c-8a71-a2124ae46b68 | -8.3783 | -45.581 | 2026-09-23 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6ca32ee3-2799-3ff8-8511-4eb9932c4e9f | -11.3596 | -44.1989 | 2026-09-23 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 3847dff1-4f5f-31b9-83ea-7a8da983d493 | -8.8105 | -44.2757 | 2026-09-23 12:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| b362b968-7de5-378a-b84b-a0b8578ffc94 | -8.0923 | -44.3307 | 2026-09-23 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c238a6ac-8ebf-3b21-9c15-26b51e772e10 | -6.8152 | -47.8735 | 2026-09-23 12:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 48f4557f-b8fc-3aa8-8d4c-b69534c1aea1 | -8.9205 | -45.931 | 2026-09-23 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 3cb1f901-d70e-3c07-afae-c98d3dd3a712 | -8.378 | -45.6036 | 2026-09-23 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| da4254b8-ddb4-35b9-8ec8-729961f7030b | -9.5924 | -46.5316 | 2026-09-23 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 44128e86-7431-3501-b201-789718ad8893 | -9.5857 | -48.433 | 2026-09-23 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 06a0eac2-10ef-3868-9d0a-af447526028c | -11.6601 | -43.4714 | 2026-09-23 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| be5854fe-7433-372b-b58b-11a7de3b3b33 | -6.6331 | -59.9265 | 2026-09-23 12:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 056cef59-0a99-3daa-9365-5c51048f6c95 | -6.6146 | -59.9272 | 2026-09-23 12:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| efc4abac-5f12-3ab5-b347-9721b8cfdcdf | -9.6043 | -48.4529 | 2026-09-23 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f13c2802-c0cd-3989-8ef5-87515abeeed6 | -8.5992 | -44.5301 | 2026-09-23 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a3299776-667b-3353-ad63-002b74f3a17a | -6.6129 | -43.7317 | 2026-09-23 12:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 336.8 |
| 56cb66ad-3a56-320d-be97-c1ab9e3eedc4 | -8.3591 | -45.6056 | 2026-09-23 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8538e92b-fe6a-344b-941e-89703e1580f8 | -8.9019 | -45.9104 | 2026-09-23 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 22545e9d-8e5f-322a-b984-b3c429eac31e | -8.9202 | -45.9536 | 2026-09-23 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6a6dc061-3caa-3368-9cb7-8a1a90d61101 | -9.5735 | -46.5337 | 2026-09-23 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 122164cc-146b-3e8c-bcd9-ff16414c8809 | -12.2975 | -46.3857 | 2026-09-23 12:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a875376e-bec9-3638-b7e2-37d91889e409 | -3.847 | -58.6675 | 2026-09-23 12:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 227784e3-c0d6-34c7-8d87-00866d4d819b | -8.8105 | -44.2757 | 2026-09-23 12:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 09927e85-3db1-3536-b0a2-0cd8bf1336fb | -8.0923 | -44.3307 | 2026-09-23 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 2d6ef975-2e1f-32a6-aed8-c1dd07d9d55a | -7.4153 | -42.6479 | 2026-09-23 12:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 565c3073-5041-3eae-b286-00acfd7539db | -7.0349 | -44.6625 | 2026-09-23 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 24c074a1-9d24-3ddb-ac0b-218db75386a8 | -8.9205 | -45.931 | 2026-09-23 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 262.6 |
| 90fbcd65-482b-344e-9dac-5843bbce24da | -9.5731 | -47.9529 | 2026-09-23 12:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 05894789-eb63-33df-beff-292109cf9f7d | -11.3596 | -44.1989 | 2026-09-23 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3b96d687-43b5-330b-85f4-e481c06441a4 | -7.1392 | -42.0811 | 2026-09-23 12:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 4fe4c746-161d-332c-9f87-77821a5f5e27 | -3.847 | -58.6675 | 2026-09-23 12:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 722ada15-c366-354f-800b-91080e0d8eb8 | -7.7634 | -46.6944 | 2026-09-23 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 96de27f1-83b3-3666-ba8a-0defa661775e | -6.6775 | -58.5748 | 2026-09-23 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 76b234f7-2f55-38e4-8982-936f4974901a | -9.5735 | -46.5337 | 2026-09-23 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 38c050ab-5bdc-3344-9799-7b4fc3475d89 | -6.6129 | -43.7317 | 2026-09-23 12:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 361.2 |
| 7f0f36f7-894e-3cd5-8c05-a2e3adf79f2b | -7.0352 | -44.6396 | 2026-09-23 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 93209548-d635-357c-ab37-7a69a8fd97b5 | -11.4009 | -44.029 | 2026-09-23 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| d19c4d1b-03e7-391e-8414-d66290203495 | -9.5854 | -48.4549 | 2026-09-23 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4841454c-a7ee-312e-8fd8-f79b5097ffc5 | -7.9904 | -44.9608 | 2026-09-23 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| e3a13a65-3f2f-3344-9fcb-e992d4fc4fa6 | -9.6108 | -43.9477 | 2026-09-23 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 6b15bb75-91df-32df-a2ed-e2a48017e969 | -8.9016 | -45.933 | 2026-09-23 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 9f084677-97be-3911-ab89-58bb1767b6db | -8.9202 | -45.9536 | 2026-09-23 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 245.6 |
| b462fc22-e165-388c-93f1-1752f3e1bff2 | -8.378 | -45.6036 | 2026-09-23 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 8fc2f9b3-3063-3c9e-91f9-6ec14d9efefe | -10.5087 | -44.8748 | 2026-09-23 12:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 64553dbb-df3d-30d0-8ab9-8ed4107bfcb8 | -7.0164 | -44.6413 | 2026-09-23 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| bc3c1dc6-966e-3900-9737-4fba24ef5ad6 | -11.4005 | -44.0525 | 2026-09-23 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 98d073a1-8099-3d2b-b3fc-a554a35c7d31 | -11.6601 | -43.4714 | 2026-09-23 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 56036f69-c3ae-3c75-a0f3-81efa4957c24 | -6.6331 | -59.9265 | 2026-09-23 12:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 7ed7226e-4622-32fb-b647-472871d5dd9a | -8.0921 | -44.3538 | 2026-09-23 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 09300a50-db51-35d1-8c4c-fd1186151fd4 | -7.7822 | -50.2284 | 2026-09-23 12:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0eb75e30-575d-3f99-8ab8-5dd70bb792b6 | -8.9013 | -45.9556 | 2026-09-23 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 163.4 |
| a3275ecc-5f81-3479-be01-30d53a54801f | -9.6043 | -48.4529 | 2026-09-23 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 5a6dad4c-c2f9-3ea7-b1c3-4ce1add64b0b | -6.6146 | -59.9272 | 2026-09-23 12:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| ce6588cf-9acd-37b1-b687-9e13db72df6d | -9.8694 | -48.3814 | 2026-09-23 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 06f0b005-a710-306a-93dd-039302cb70c2 | -6.659 | -58.5756 | 2026-09-23 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 96c6bf66-613f-3813-8381-834c6e0bbaed | -6.9416 | -42.8834 | 2026-09-23 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 1c4a9cca-f2d7-310c-9f24-760fa8fc1296 | -8.3783 | -45.581 | 2026-09-23 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f44e5d3b-cd67-32f5-9f48-3430ec2986ce | -8.3591 | -45.6056 | 2026-09-23 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| efd12f9e-3153-3cf8-a84c-4769ab6ae5d6 | -6.1846 | -52.049 | 2026-09-23 12:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d0271d19-104a-350e-a78b-0ff0244e0f42 | -10.7524 | -46.3025 | 2026-09-23 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1e3db555-5a0c-375f-b938-2fe91493cf38 | -7.0352 | -44.6396 | 2026-09-23 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 30799753-387a-3790-a345-4a58973178b9 | -9.5735 | -46.5337 | 2026-09-23 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 49c77c99-c495-3d17-a147-95c708bc33c9 | -9.6111 | -43.9243 | 2026-09-23 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 556ea252-8c3e-309e-9893-d2d0eeddb16b | -7.0164 | -44.6413 | 2026-09-23 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| ce5d7c04-ef95-31c0-8a52-81338acbe9ae | -9.5549 | -46.5134 | 2026-09-23 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| ee80b655-6630-3ba5-9b06-a3d5d5e157a1 | -8.0923 | -44.3307 | 2026-09-23 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| e9768f2c-a820-3b59-a3da-fd36f71fd4ec | -11.6601 | -43.4714 | 2026-09-23 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| e5f7b326-861e-3dca-9c0f-88542093bef6 | -6.9174 | -41.6957 | 2026-09-23 12:50:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 59c76607-bff5-3f3f-9fe3-53e809fb7afb | -7.7822 | -50.2284 | 2026-09-23 12:50:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |


[Clique aqui para ver as próximas entradas](README134.md)
