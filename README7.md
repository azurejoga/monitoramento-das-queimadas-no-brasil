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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 671d2771-cfb5-308f-bad8-4c694f768ec0 | -7.20042 | -43.13336 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 93dcc5e3-27f6-3223-836d-95bfc903e4a4 | -5.92783 | -49.99519 | 2025-07-06 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b78d59de-4217-3d4d-8145-c8e326175933 | -5.56994 | -45.21221 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 89b95b90-c762-3813-807e-83949330f29c | -10.82001 | -49.57085 | 2025-07-06 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3bcd5e2-d42d-3b7e-bc1d-afb1d54fe51f | -7.20144 | -43.12599 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d97a962a-77d9-3b7c-a513-9dde887b3ea5 | -10.64984 | -44.4845 | 2025-07-06 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9123999-ee09-3e2b-ba05-106ca8a9fc67 | -6.55088 | -43.47476 | 2025-07-06 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 437de4db-d45e-3619-ba20-b3aca59229e0 | -2.90661 | -54.48698 | 2025-07-06 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33a7bb15-dbab-34a4-8a81-b307045e1adb | -5.60267 | -45.1862 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1b55fdb-80d6-3c11-963d-42da0c23d569 | -11.45312 | -45.1059 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8f6b26cc-e4cd-3f8f-9387-dffbfede66ae | -7.89925 | -63.03976 | 2025-07-06 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9172dce4-97e1-3f9f-a2c2-72ca5565f91a | -3.97941 | -48.41261 | 2025-07-06 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15283b4f-9b18-3906-832d-46f1722b8f74 | -5.06874 | -43.72826 | 2025-07-06 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f1407c0-c3ef-343d-a191-a6efff8360f2 | -9.09161 | -47.96616 | 2025-07-06 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84dc3d8c-f81e-3368-80c2-4f5d0e8e93cc | -7.1993 | -43.13346 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 68e27094-b2eb-3882-b6fb-820a2e442519 | -3.32742 | -52.54803 | 2025-07-06 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4b2a090-c98a-3a65-b2e2-7d9d3ac93afb | -5.605 | -45.17882 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18e4af94-9d7a-3227-9aac-6c15f6ade5d7 | -5.41676 | -47.57002 | 2025-07-06 04:51:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4f20b2a-a4b2-35d8-aa21-2cbea7e230e4 | -7.20027 | -43.12609 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 235aeaa0-fab1-3eba-9fab-06276b468492 | -5.6036 | -45.18895 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4922986-755c-37ac-ad94-7f1290510502 | -7.4286 | -60.02932 | 2025-07-06 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86435ad0-e384-3603-acf3-337a75d92b5c | -7.1798 | -56.71653 | 2025-07-06 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4c84fc4-b99a-3b8d-8b2f-e357e63ef044 | -10.64753 | -46.38237 | 2025-07-06 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e1bfb9f-3721-38b6-bca2-f4a9a74b5faf | -5.59794 | -45.18548 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b225334-ab3c-375f-b66d-c27843d2ab97 | -4.45371 | -48.99182 | 2025-07-06 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9713aa8-1e71-37de-9150-cdf5566f0781 | -7.72419 | -55.13552 | 2025-07-06 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b618a37-1842-35f5-a993-45c5e0950779 | -5.60763 | -45.19469 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59c942d0-b64f-3091-aff7-ee0fb56457e3 | -10.86923 | -47.18424 | 2025-07-06 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f16f495a-af41-3fbd-a3d1-6b58366c6065 | -5.60414 | -45.17609 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9df241f-953d-3c66-b9d3-4410bbafafe6 | -7.20486 | -43.13432 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ef650ed9-ea66-3f88-a9e3-51d69b2732be | -7.20584 | -43.12693 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ab2e691a-671e-355f-b40d-3376243b6d9b | -11.44794 | -45.10518 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06add0eb-6a05-30bd-b800-7b6b55a3b360 | -11.44833 | -45.10203 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bdfd6cb1-85e3-3dcb-a8ea-fe3b431adf91 | -5.56921 | -45.21727 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c7792dc3-b42d-3331-8e72-3fb1548df4cc | -7.28391 | -44.68275 | 2025-07-06 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 363d0fb4-0915-32b5-83fa-8d4b62b8b4af | -10.57509 | -49.13345 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea33be16-1513-345b-bcd5-fe5ed68e0b4c | -6.16346 | -43.75882 | 2025-07-06 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1c57342-ea6a-30be-a116-7d060334e95b | -7.19421 | -43.12896 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 473b6d32-9d7b-32b7-a156-4cee65e495a7 | -11.4539 | -45.09958 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 718d3824-0cad-3364-9a96-c37654fb458e | -7.19485 | -43.13253 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b4fa5e95-92e3-3c9c-87a6-b7333c17a095 | -4.81628 | -47.32035 | 2025-07-06 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5055a8cd-ed13-39ae-b43b-a032a7578866 | -5.60962 | -45.1717 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cc227e8-0b30-341b-9a8a-00c700ea5e90 | -8.03329 | -45.83222 | 2025-07-06 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0e4e254-6566-3ed8-a518-4d0c301e3f1c | -10.64894 | -44.49136 | 2025-07-06 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c08adc81-5f2f-35e3-945a-27c553ca9054 | -6.00009 | -52.4054 | 2025-07-06 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f7c2c1b-333a-3c5d-84f3-37e118dd86f7 | -7.96955 | -47.22968 | 2025-07-06 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8407fc87-555d-3b9d-bb6a-a9a07b7afe2d | -5.59868 | -45.18045 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5bdc84a-98f8-39c8-b627-89a9ad55662e | -10.55948 | -49.13114 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6410497-c36a-3531-8b61-220a7e2c9d54 | -7.90483 | -63.04073 | 2025-07-06 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7a035a2-d4a0-3bbf-8744-1aab1fa98781 | -8.80998 | -45.97415 | 2025-07-06 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad5c9957-67e1-3831-a252-b13c768c478e | -3.86698 | -50.08256 | 2025-07-06 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2c3a5c5-2b0b-3200-ba8d-945a21969fe4 | -9.36077 | -58.84231 | 2025-07-06 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11262445-847e-3543-b918-0889acc55257 | -5.6057 | -45.17375 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b393e97f-99af-3b5d-a931-22a6d96ac204 | -3.65564 | -48.32409 | 2025-07-06 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73c8047b-8ee0-3a3a-876a-0315aca2967f | -7.01461 | -44.34371 | 2025-07-06 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a690b90-fd2d-3cc1-bda4-50256a057e3a | -5.6043 | -45.1839 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ab5a5ac-e557-3598-a9cb-59ce4b08306d | -7.30556 | -45.36152 | 2025-07-06 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35296146-432c-3b6c-b90d-b6e5d9ffb871 | -5.6034 | -45.18116 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e11100e-a666-30b3-bdd7-a1c3f18eff63 | -4.81679 | -47.3169 | 2025-07-06 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed11891c-8fd6-330e-8e04-09b59ec50ed6 | -7.14143 | -44.31637 | 2025-07-06 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abb96eb1-bb0f-3fb6-a438-d42a766dda34 | -4.79138 | -48.08331 | 2025-07-06 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4c0a752-5343-38e2-8636-9a7471d220e9 | -6.16303 | -43.76197 | 2025-07-06 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 100d2ae8-85a6-37f5-8405-5010ff16a141 | -11.44755 | -45.10834 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61b42a28-efe7-305e-8dff-c6767ebe6a1d | -11.4583 | -45.10659 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4d01a32-51f4-3ba7-a99a-bb9e39692f93 | -7.20093 | -43.1297 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5fd71f17-c023-3f0e-828a-3e0cd6911890 | -10.64284 | -46.38167 | 2025-07-06 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 077421b9-89bc-39e0-9fad-8c38d9b02216 | -7.19978 | -43.12981 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3ed842d9-889f-3907-9a4c-4f6cf5c0aa92 | -10.63752 | -46.38584 | 2025-07-06 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 203b3b3b-c026-3098-a5df-593e0687afbd | -4.45307 | -48.99604 | 2025-07-06 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92375ed2-476a-30cc-8238-5a826436403e | -9.92098 | -59.91436 | 2025-07-06 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bda9f0ce-d204-3709-8e64-b1e2eb515cfa | -12.01555 | -47.77202 | 2025-07-06 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb5cd0cd-cd98-3e7b-98e0-fb8ba8a80048 | -12.02382 | -57.07821 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 524438c3-4c85-3730-b215-e99997f1cef7 | -12.01497 | -47.77633 | 2025-07-06 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76784a83-95cc-3b70-9d2c-c20bf4bee746 | -11.00982 | -55.24156 | 2025-07-06 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6993d06-c0cc-3c14-9ace-259c00af6112 | -11.33256 | -51.44898 | 2025-07-06 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a01b6e8d-d075-3b05-befe-36736634fd95 | -12.0267 | -57.08295 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 258d6e36-348d-3e49-879c-0cac788eafa6 | -10.30392 | -57.14361 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07d706fa-558d-3ba0-bf10-4f7644accd1f | -12.02739 | -57.07881 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f03fde23-891c-3f2b-b9cf-bfa4e184174f | -13.00375 | -55.97527 | 2025-07-06 04:53:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c6e6cd6-b382-373a-9a4a-a405bd90cc71 | -12.57907 | -56.97116 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f40486b-38a0-39da-87af-d5a0fce75a7d | -13.0027 | -55.975 | 2025-07-06 04:53:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 768e38e7-dc55-375d-837b-ac77753bb7c7 | -16.43215 | -42.18688 | 2025-07-06 04:53:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aa6aec85-986f-3600-abf7-b2fe009127b6 | -12.06602 | -43.50331 | 2025-07-06 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41cae17d-83f0-31df-a683-f2f6f46ab849 | -9.93101 | -59.93798 | 2025-07-06 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1ef9eec9-12ee-3679-a624-5aaa2c0d98bf | -16.68296 | -43.8856 | 2025-07-06 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c636031-11ec-3ede-b4ac-afc77dd32438 | -10.30463 | -57.13929 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3372f76-01e5-3193-85f8-1e1e0df5e56c | -11.33198 | -51.4529 | 2025-07-06 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01703e4f-e3e5-34f0-b0cc-21a5c68f5eda | -12.5799 | -56.98798 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f66f7b87-132b-3995-b21f-683c4365eef5 | -11.87584 | -58.7394 | 2025-07-06 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c115d77d-0d3f-3665-91aa-a006b74517e6 | -12.03164 | -57.07531 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3ae548f3-282a-3522-9248-d88aabec992e | -13.95373 | -48.01017 | 2025-07-06 04:53:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f3e1335-00bd-3f55-a1f2-beb3449683b9 | -11.87977 | -58.74005 | 2025-07-06 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee7b6fed-c786-3c36-9381-5760507b5c9d | -12.58125 | -56.97986 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f75244-9951-3b3c-8530-34cf4215184e | -11.33141 | -51.45683 | 2025-07-06 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35811a62-43e5-3b6e-8caf-1901312c348d | -13.0033 | -55.97128 | 2025-07-06 04:53:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2193a819-2b61-3e1b-bf73-a2498c0a14d1 | -11.83877 | -57.75075 | 2025-07-06 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6ee18e0-9e88-3775-811e-3312e611e5d8 | -12.02601 | -57.0871 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b5059d90-e463-3eeb-9c52-b3b7c465bf1f | -11.8762 | -58.7375 | 2025-07-06 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d7e42c4-12e7-391d-b430-af4573c8489f | -12.05977 | -43.50634 | 2025-07-06 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e5e41cd-a7eb-35a7-a165-fb36e88ca3e9 | -15.87959 | -48.33136 | 2025-07-06 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README8.md)
