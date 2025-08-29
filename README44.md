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
| 5c99bf99-6348-3db9-bc08-a891a4888605 | -6.88394 | -43.61589 | 2025-08-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e0f3ccb-fc3e-3bdb-b9b6-d82d0cbfd265 | -11.08798 | -45.13082 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8f65313-fcbc-3d37-ba00-b1b3c8acbeeb | -6.15404 | -44.05629 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad209f93-b1e4-3c35-b994-4b873699de6b | -6.20799 | -43.0042 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ca2f6b8-56ee-3e5e-b5f4-b30770b5a44e | -11.09265 | -45.12769 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b05b32e9-c34a-336e-bd37-b11cdfcc24b5 | -6.44433 | -44.57947 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b79755cf-4bb6-374a-bafb-dc683394edd6 | -6.23859 | -42.39606 | 2025-08-29 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 77db0818-21c3-3413-8b2f-0d4e4e82880c | -7.07345 | -44.28085 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51b7e0aa-ed92-33b3-86d1-6b5b5a799f02 | -7.54845 | -47.49869 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae5daa84-1dcc-3ffb-b5ff-e7a878833b70 | -9.45693 | -60.56977 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e9f7f4b0-e5b7-383b-a90b-c78dacafaf76 | -8.45235 | -43.72008 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 753fd64d-b0d1-3ad0-a3e7-2154d8e32010 | -11.33039 | -43.58158 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cef7600-0ea6-3e1c-93b9-98b106b3b0fc | -6.85865 | -44.38782 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f02423f3-d19d-3599-9f8a-f792b8afc928 | -9.15972 | -60.93096 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7dce405a-1c12-3dba-a596-66eb84698c05 | -12.91532 | -48.14091 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aefc4ef4-788d-3a73-96a6-1f3947218dad | -11.06567 | -44.76142 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e99f48bf-bb22-35a1-a411-4a06d841cf0c | -10.36842 | -57.81537 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e2321a35-fe97-3422-80a2-79daf8391514 | -8.70621 | -50.368 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 220ceee2-a20c-31eb-85d3-f99c533b9a4d | -9.16889 | -59.55953 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c392600a-08d0-3df0-91e7-678a37b93599 | -11.33164 | -43.57174 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4b659c6-1cea-3e88-9cfd-6fb79bcd173a | -12.70095 | -48.14882 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b3a0a94-d5fd-3983-9a12-040cb143bf0c | -12.41951 | -45.01947 | 2025-08-29 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b454f0f-1e18-35eb-904d-196f067bb12a | -10.84307 | -47.50304 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8017b654-6105-34e6-9538-0bec8e43e653 | -6.48549 | -44.09591 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b76a4420-04ab-316c-b9a5-2fe6648863a3 | -11.26626 | -45.49192 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81e61531-c64a-3197-8ce2-c6a1511105f0 | -7.67602 | -44.7759 | 2025-08-29 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27c69824-4bad-3c15-b52c-234ef6833fa8 | -9.4331 | -47.64637 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89338c11-9ced-3cff-8d05-c90f47c2f945 | -12.92379 | -46.34487 | 2025-08-29 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5d1a20db-ca70-3165-8a8d-3ad23e78de66 | -12.95918 | -44.57733 | 2025-08-29 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ef03cd1-5a33-30a0-8cf8-9e51866f73f1 | -10.46872 | -57.96917 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bf0157f-24cb-3722-a229-a2f50728f314 | -7.72426 | -50.27474 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 900d1a35-1a51-3f6a-a26a-b9ed6c8bd85c | -10.46947 | -57.93787 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a57cba57-2867-3203-bcbd-217909e87bb0 | -6.88789 | -44.44535 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2681b737-f83c-34cf-b1e6-7e05e25ca454 | -9.43721 | -47.64291 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7602fff9-2ffc-3b5f-9785-39a31a1df326 | -6.39116 | -45.22725 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| caefdc6f-4e04-3e1c-8692-fd9dc4f281e3 | -6.70909 | -43.14329 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc50fbb1-66e7-3bdf-a072-f8c7164f218b | -6.10483 | -43.31561 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4103bad4-1cc1-3bfe-93a6-d3419a4143f9 | -11.61812 | -46.20442 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 651f5603-3755-3bdf-8918-43c03289132a | -8.44361 | -43.65335 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6530012a-1973-36a9-9913-ff1e2bfe7e45 | -9.45599 | -60.56203 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e140dc10-d704-3f4b-85d6-37d7011da32d | -6.45021 | -41.92939 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f841dcde-a397-31d2-b02c-00f069e417d5 | -6.70888 | -49.46165 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 421cd4d5-0bbd-3bc9-ad7d-3924a91c3c3c | -6.81399 | -44.99406 | 2025-08-29 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 203f8655-e0dd-36a2-a9c2-c2691b5a0ded | -12.83746 | -48.10657 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f92b660-ca2f-3d88-9e32-277394feaeec | -10.37429 | -59.39608 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc6f1bc1-43bb-3d64-94f2-016fabadfa8c | -9.93689 | -46.7129 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 905cba5b-de96-32b2-b652-1d5ac74a17ca | -7.7309 | -50.29713 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5f102b5-f0c0-3d73-8bfe-5235a6ff1686 | -7.16009 | -44.16108 | 2025-08-29 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe1ba77f-c10d-3b17-8e03-2d4f88d14e3b | -11.61779 | -47.31613 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7004f84-858c-33e7-8b46-bd9395880784 | -12.88316 | -48.13666 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a1d5631-bebe-32c4-be17-8083c07c3ef8 | -10.85163 | -60.8132 | 2025-08-29 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37977001-108d-337f-a91a-caa8d8493bab | -6.94752 | -44.06983 | 2025-08-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73aa75bd-e077-3851-8798-0e1a4228b81e | -9.79417 | -56.60978 | 2025-08-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a031c85-1870-3703-a634-017126aa3c50 | -5.33084 | -51.32982 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc7e97f9-8957-38c2-a56b-14efe8ca1b22 | -9.04522 | -47.01416 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92562863-7591-32ad-9d74-acfe83673479 | -11.32364 | -43.56045 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 562e1db4-f4cc-376a-a5b0-5c96e6d30b7a | -11.5779 | -46.37504 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15ec2751-691f-3d83-acf5-e18ffae1a30f | -7.61869 | -42.70543 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 319dae1a-26fa-3f6a-8ed6-d81a8479eadc | -10.67515 | -47.08915 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9802d89a-2697-39a8-b578-4a208cf5d906 | -11.0697 | -44.76 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 762acd01-096f-3876-a0dc-9d059e6206d3 | -9.21352 | -60.86647 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77a12679-180d-37ff-a154-da345309f1f1 | -11.56942 | -46.37928 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| baec5cb5-402b-36e5-9086-48ad9767d8b5 | -9.20933 | -60.857 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29a400b5-bae8-30b1-8d28-f1e4fc06e2f7 | -5.78076 | -46.14169 | 2025-08-29 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fdc460b-b321-3f7b-8a96-3fa7ebcddb86 | -10.33053 | -46.78846 | 2025-08-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00100f89-d477-3822-9d62-8bbcd7784089 | -12.88732 | -48.13306 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3338b09f-3f4f-3151-a28a-20b3f6d0f6fd | -9.16318 | -59.53074 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3576426-5bd8-30af-b59c-08910d0fb428 | -9.45617 | -60.57373 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b9267f1b-577a-30e5-80d3-deef6237a052 | -9.45379 | -60.57395 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3a4d4e3a-fac8-3b2a-9541-3a1c1bbc0667 | -11.23892 | -44.9743 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fedc1b59-c66e-3330-a881-6d61277bb167 | -8.55328 | -51.31538 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 756e969e-ca40-317d-b7ab-61bdb6959147 | -13.1896 | -45.28761 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fe070cb-3d50-3d1f-a6e7-95505e5d9bd5 | -9.77242 | -64.24715 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 870f6500-79ec-3a5b-b669-56fee49be54d | -6.19804 | -43.32413 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfc4bc49-520d-3d89-955a-6112b04d3ed7 | -11.18541 | -48.62238 | 2025-08-29 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 778ca28c-698b-3910-9561-343cb1484b94 | -8.48976 | -43.67747 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5d7e03f-9289-3f79-b823-1cf9bd1021d1 | -10.36579 | -57.83006 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7b09003d-df9b-37d1-b09b-732f0298154e | -7.00071 | -50.41947 | 2025-08-29 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad46aa88-37b7-3c3e-9459-ec59bc2d9f72 | -8.88272 | -60.74586 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04489369-3303-3061-a8ec-1b932c1a9b06 | -7.04551 | -44.35834 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e35e17b-d09a-3e3b-833f-a5400d09a7c3 | -8.7496 | -47.40215 | 2025-08-29 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb7ad968-8a6c-372b-a1fa-4d2774ac4d4f | -10.51747 | -46.6785 | 2025-08-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b639363b-68e5-3740-b6e5-e717594f5edc | -7.79779 | -50.97183 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27873a40-2f63-398f-8230-7edacb9b730e | -7.00279 | -44.37107 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 260695cd-d98f-3dfc-a48a-6d1c092cd2d2 | -10.95124 | -46.88718 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5147b27c-5cd9-3277-b9e0-45cc3a24bce1 | -7.63216 | -46.54971 | 2025-08-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e16a741-8d1c-34e3-a919-ad587097ec7d | -7.41973 | -42.06009 | 2025-08-29 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 84499423-adf1-38ab-ad0e-c415a84ae09f | -7.62605 | -42.68658 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80058af2-3439-3409-93b2-751ff46f817f | -7.55311 | -45.23512 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62b26b24-82b5-3ed8-aff2-34f9c68ac6e4 | -8.18805 | -61.38632 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01113747-373f-31ca-9583-67fc087c6717 | -6.54133 | -43.92013 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d97147de-ee5d-35fd-9f11-e9621f292bb8 | -9.4577 | -48.27437 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 940cec15-37b6-3f76-9fd9-e09fb044056b | -9.43662 | -47.6469 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 642c3672-cac1-37d1-aeaa-7bf78c3aca2a | -11.03347 | -45.06403 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b410a907-d3f9-3a58-bade-17d2c395469f | -10.98264 | -46.89442 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 483e2448-466f-3f92-9ad7-0142e7787af1 | -6.78326 | -43.768 | 2025-08-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b35a89ef-6901-35e1-a5f6-5da15636a50f | -8.18285 | -61.38043 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0af0bdf9-0ad3-3e71-a0ab-c8373c69f8c1 | -7.7243 | -50.29607 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cdb49e2-3145-347d-9836-511f680cb81e | -11.56163 | -46.37872 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b28a68ff-e459-3172-b87d-69fff05447b6 | -11.07049 | -44.75803 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README45.md)
