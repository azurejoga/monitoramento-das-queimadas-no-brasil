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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1368216d-0c17-33d0-9ce2-575f37d4c1b8 | -14.4309 | -53.0252 | 2026-08-12 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| e86d407c-8804-343e-9247-1fd011e1724e | -15.3019 | -48.8818 | 2026-08-12 14:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 9a663cd5-b901-3fa2-8664-9bffa8b0076d | -7.0008 | -42.6417 | 2026-08-12 14:00:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 0980e8ee-f74e-304b-961b-01aa58c7f1f6 | -15.152 | -52.678 | 2026-08-12 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 5e04e9d6-f487-3c64-8e76-a1a71e08d69d | -14.2877 | -45.2835 | 2026-08-12 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8068cbd8-0af6-3350-b03a-74245ce9e273 | -6.5443 | -43.1078 | 2026-08-12 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 347.5 |
| 03980342-c9ab-3c29-ba34-d274e6e5fe97 | -6.9516 | -42.0042 | 2026-08-12 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 31c4fe0c-89c1-3288-8fe8-502ea61f8893 | -14.3897 | -52.0361 | 2026-08-12 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 67588c97-8fac-3c95-b4fe-681fa032031d | -14.3509 | -53.2033 | 2026-08-12 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2080b6a3-310a-3143-8c36-0dfbd8da44b0 | -14.3901 | -52.0148 | 2026-08-12 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| d80f2ce7-e998-3fdb-b55a-c8fd744852e5 | -11.9719 | -46.3871 | 2026-08-12 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ae4dbc4f-198a-3053-bf8a-577a0746a5db | -14.8433 | -52.6131 | 2026-08-12 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 6164cce0-65c5-3994-9b76-54c55f15ac37 | -11.9535 | -46.3444 | 2026-08-12 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| f0c46c2e-5734-35c6-93ee-1464282a977c | -14.5233 | -52.1248 | 2026-08-12 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 90019201-dfc3-3de0-be7e-a31d3b4de71e | -11.0286 | -45.6993 | 2026-08-12 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| f7130889-758a-3842-b781-f8dbe0129e00 | -14.5229 | -52.1461 | 2026-08-12 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 18a0b285-61bb-3ad3-b366-9935c2e5e627 | -11.8859 | -45.831 | 2026-08-12 14:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 91be2c7d-ebcb-32d4-bbd5-f6302169315b | -11.9343 | -46.3472 | 2026-08-12 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f4ed9602-5a62-36da-b5b6-4ea188c2fac1 | -13.6273 | -46.2948 | 2026-08-12 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 280.6 |
| 7a202641-ceae-366e-85b6-d52ddf275a70 | -12.1771 | -50.1557 | 2026-08-12 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ff0fd90b-1253-340b-a7e3-fa088ef7b412 | -15.1714 | -52.6754 | 2026-08-12 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 0752508b-a688-3b3c-9694-52bc8401f135 | -14.3695 | -53.243 | 2026-08-12 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 072e0e39-8907-3bc6-8e93-2e9586a6ac91 | -14.4313 | -53.0041 | 2026-08-12 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| d8b76602-c568-3b57-954d-9f5ee4cd1209 | -14.3702 | -53.2009 | 2026-08-12 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 8354cb83-11e0-3890-9034-c7b82ef698dd | -14.2941 | -51.9848 | 2026-08-12 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f65d4bb5-59cc-3dd7-8731-16d295798476 | -15.171 | -52.6967 | 2026-08-12 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 8a0d2e90-0e13-3570-ae78-e25773496c2b | -9.3339 | -47.4937 | 2026-08-12 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 73eb1224-bf0b-37d6-86b4-f42cee373c9e | -11.9911 | -46.3844 | 2026-08-12 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 5bf263c0-fc54-341f-ae9b-295a2b57e5cb | -6.544 | -43.1313 | 2026-08-12 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 641.6 |
| 313b8ea8-ebf6-30d7-a23a-4853554021b9 | -6.5438 | -43.1547 | 2026-08-12 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| e2eb6f14-d7e5-3e68-816f-fdc0ca436bd4 | -9.3534 | -47.4475 | 2026-08-12 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e462319f-d5c1-30c7-ba4e-c1a78fea51ff | -14.3699 | -53.2219 | 2026-08-12 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c199b3ec-cf6f-3d8e-8739-ab5e3605d46f | -14.4309 | -53.0252 | 2026-08-12 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 38169c9b-208e-3750-8048-b6bdc709e4eb | -14.3893 | -52.0574 | 2026-08-12 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 42354a71-e0ed-3d83-83a5-a802e78ec72b | -14.3135 | -51.9823 | 2026-08-12 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| ba63a581-80bb-3192-87aa-5238dc2455b9 | -9.3534 | -47.4475 | 2026-08-12 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 7e7a3e54-ce74-3faa-8e83-d3bbf7810c11 | -8.4935 | -45.4104 | 2026-08-12 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 0e458e9e-4714-3d50-9462-60c439abac79 | -9.3336 | -47.5158 | 2026-08-12 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b7d1e4e8-cba5-365d-8620-6458af124d34 | -9.3531 | -47.4696 | 2026-08-12 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 29155955-0f14-3d4a-ad81-7fd28a6c54ee | -10.8256 | -50.3529 | 2026-08-12 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| fa3118d2-8a70-392c-8e7b-0bb37268bc07 | -11.029 | -45.6765 | 2026-08-12 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e6919208-ed68-3754-a823-09a7405c3698 | -14.8433 | -52.6131 | 2026-08-12 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 227.5 |
| f56edab9-f590-39a2-825f-6fd046279f57 | -14.4313 | -53.0041 | 2026-08-12 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 466024c1-65ce-34ce-9a2c-03cf16204e44 | -12.1771 | -50.1557 | 2026-08-12 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 333914b1-37d3-301f-a6c1-e4b8bcecb018 | -14.2877 | -45.2835 | 2026-08-12 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d33d6b7f-c47d-3968-bc38-85e92d9a4879 | -14.3509 | -53.2033 | 2026-08-12 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| cd9ec24c-842a-3bca-9407-837d17cdeef7 | -14.3695 | -53.243 | 2026-08-12 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 186410aa-db7f-329b-bf0b-4f3ccde77764 | -6.5443 | -43.1078 | 2026-08-12 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 285.4 |
| 6cf35cca-8ede-3ac3-b8b8-213d4de57307 | -11.0286 | -45.6993 | 2026-08-12 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 368.7 |
| 5057db38-4090-3aa8-9a1d-fcfacee8e316 | -11.9535 | -46.3444 | 2026-08-12 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 1929e5e5-4bb5-3f10-bfd8-e0edec2c0792 | -14.2941 | -51.9848 | 2026-08-12 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5f34c082-6fb1-3395-ab9d-7feb127622bf | -6.5631 | -43.1061 | 2026-08-12 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 93b6c0e4-9282-3b98-a5d1-cef5e164f81a | -10.8445 | -50.3509 | 2026-08-12 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| cd6caff1-7728-3ccd-a000-118b91245045 | -13.6273 | -46.2948 | 2026-08-12 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1ee855f0-e03a-3dbb-bd09-7a84087daa9d | -15.171 | -52.6967 | 2026-08-12 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 9ac4b68c-550a-3591-bc34-dd6ca288d98a | -11.8859 | -45.831 | 2026-08-12 14:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 37f6208e-8829-3191-a300-b899f9c23e86 | -14.3631 | -53.6417 | 2026-08-12 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| c1578445-6a6a-39eb-ac99-7c2dbe423c52 | -15.3019 | -48.8818 | 2026-08-12 14:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6882d63f-ce68-33d3-9f95-65b0b4578ac7 | -9.3339 | -47.4937 | 2026-08-12 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0400afaa-f9b8-3e98-a1c8-c153ba1b8403 | -14.3506 | -53.2243 | 2026-08-12 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 92195c1a-fb3b-37f4-b9fa-d1a9fe677ec9 | -15.3808 | -52.9015 | 2026-08-12 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c3a1fe97-1a66-320b-9889-29d478d43f68 | -11.9911 | -46.3844 | 2026-08-12 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 280.1 |
| c0589173-62af-32ca-ba95-0338a18ebafb | -11.9343 | -46.3472 | 2026-08-12 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1275493a-121d-3e7e-a86a-bb55d596b342 | -6.5438 | -43.1547 | 2026-08-12 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 6386578d-ade0-31f0-8007-5c33b7248d9c | -6.5255 | -43.1095 | 2026-08-12 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cda16042-1850-3b54-b55e-213dac7e7610 | -14.3502 | -53.2453 | 2026-08-12 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f56eb3ac-238b-3264-a033-aa1e686542ab | -15.1714 | -52.6754 | 2026-08-12 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3493fb91-6c69-337e-b28c-983538ba1e99 | -13.6268 | -46.3177 | 2026-08-12 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9e10af0d-a2b4-3462-9ae3-f5bdc3aa08ec | -14.3699 | -53.2219 | 2026-08-12 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| b05386d2-5ef2-3d2a-bbce-54f477971567 | -6.54 | -43.15 | 2026-08-12 14:15:00 | MSG-03 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b029857-a6bd-3166-8457-15f801500419 | -11.83 | -51.88 | 2026-08-12 14:15:00 | MSG-03 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b48f70d-231c-3d1c-9add-71d20343567e | -6.54 | -43.11 | 2026-08-12 14:15:00 | MSG-03 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a42db435-8d24-3167-9341-9fa399ad6f50 | -14.2941 | -51.9848 | 2026-08-12 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 443e6433-a953-3b1a-ab1d-bfeaf4e9d8b2 | -7.0008 | -42.6417 | 2026-08-12 14:20:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 284f523c-d753-32ed-b25f-f2dbcb955c20 | -14.3109 | -52.1314 | 2026-08-12 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 3c11c12d-c61a-3768-bedf-16f8387be22e | -14.3893 | -52.0574 | 2026-08-12 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 82f60c33-8f79-31a3-b031-fa9f594da307 | -14.3502 | -53.2453 | 2026-08-12 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 151.6 |
| a1ce85f6-a565-3390-b25d-e1b1f55f057c | -14.3695 | -53.243 | 2026-08-12 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 039a0f98-c652-3244-ac9c-1e4e6560efaa | -10.8445 | -50.3509 | 2026-08-12 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 8a67d7e5-1775-3dfa-a0fe-a5de7a8eae4f | -14.3135 | -51.9823 | 2026-08-12 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 531.6 |
| 596b3fb8-66a7-3421-8b39-605ad43da962 | -14.2938 | -52.0061 | 2026-08-12 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3a183907-d3a5-300a-a1fc-04c53c0c33c5 | -7.9133 | -45.1053 | 2026-08-12 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 86ac4f1a-057f-3172-a332-67a1d40e69c5 | -13.6268 | -46.3177 | 2026-08-12 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 352.1 |
| b7e3d314-4f83-3b16-86d0-a98616e90b12 | -14.3699 | -53.2219 | 2026-08-12 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e3c7f162-4ce5-3c83-843e-9fe6bba311a1 | -9.3534 | -47.4475 | 2026-08-12 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 188.6 |
| a5460f20-bf48-3287-a89e-483bd361318c | -15.3808 | -52.9015 | 2026-08-12 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 857cfbe6-279c-3c4b-a9d1-143ba351400c | -11.0286 | -45.6993 | 2026-08-12 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 1aa2123f-4ab3-3836-8b28-7c4b74750b42 | -14.8433 | -52.6131 | 2026-08-12 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 6e9a3dd2-888f-3882-88b0-521070047f38 | -15.4428 | -53.7997 | 2026-08-12 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 31057c7e-f799-3b2b-842b-d123a35fb2fe | -11.8859 | -45.831 | 2026-08-12 14:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c9a98128-4f6c-32ed-bb36-c6152fd2566b | -9.3531 | -47.4696 | 2026-08-12 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 61ac49ae-a12c-311e-a13e-1539e818aa95 | -14.3631 | -53.6417 | 2026-08-12 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| d5c193e5-7df6-303b-8d9f-9a02508bf546 | -14.3131 | -52.0036 | 2026-08-12 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 347.9 |
| 65342930-9649-312b-849f-e2d5601dfac2 | -9.3339 | -47.4937 | 2026-08-12 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 1a93c6dd-b595-33fd-94f4-c3a629d2a11d | -10.8442 | -50.3723 | 2026-08-12 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| a63b7dd2-815e-3029-bab5-7e6dec069de1 | -14.3897 | -52.0361 | 2026-08-12 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 51f3b5c0-fce6-31b7-a62b-94f4a3321323 | -12.1771 | -50.1557 | 2026-08-12 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 082f9132-41e1-33e4-befe-49141687695d | -15.1695 | -52.7816 | 2026-08-12 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| f4848a9d-5219-3abb-bd87-7f2703741430 | -9.3336 | -47.5158 | 2026-08-12 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| ad0e5aed-63fa-3526-8743-6c3bf703a549 | -15.1714 | -52.6754 | 2026-08-12 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |


[Clique aqui para ver as próximas entradas](README38.md)
