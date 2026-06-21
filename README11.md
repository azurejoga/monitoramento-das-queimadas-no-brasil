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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e880f5a4-e247-3100-89a3-87a7fe2b3e18 | -10.90801 | -49.4981 | 2026-06-21 11:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 380bacba-1f82-315d-bbb8-06d37e67857d | -11.0094 | -45.20902 | 2026-06-21 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 672d48a7-0515-305d-a198-10ba3986e538 | -10.54213 | -47.72541 | 2026-06-21 11:49:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 285f07a6-2de9-38cb-98b7-01f6933db008 | -7.97173 | -47.43836 | 2026-06-21 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 970f0261-224c-34c8-8bbc-c4bb2113cf43 | -11.0678 | -52.47241 | 2026-06-21 11:49:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 036e51df-84e9-3237-85f1-04a69b75a5eb | -2.56782 | -47.20845 | 2026-06-21 11:49:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c11b771e-a6b0-3232-bc08-684ed2eabd57 | -7.96283 | -47.43703 | 2026-06-21 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7edea784-e475-3e49-9d4a-263fd09f90d6 | -6.509 | -42.22794 | 2026-06-21 11:49:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 12b9ae67-bb3a-3b97-ae0f-5b01f496bfce | -10.69358 | -47.70477 | 2026-06-21 11:49:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 38f21fd4-a5ad-3ac6-a05c-2ce8e1248b2b | -7.96415 | -47.42797 | 2026-06-21 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c12242af-d9a3-3836-a02d-6a958f41e456 | -12.51837 | -48.29868 | 2026-06-21 11:51:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3eee2ee9-b0ef-38ae-ae2a-e74e30082981 | -12.99207 | -42.39956 | 2026-06-21 11:51:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 494a385f-be57-364b-a079-d90a589023ac | -11.0976 | -54.1516 | 2026-06-21 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 124fce67-b754-3c0a-bf34-45bd216e4a5b | -11.0976 | -54.1516 | 2026-06-21 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a37e9199-e116-34d4-94b7-deedbf0eb20c | -11.0976 | -54.1516 | 2026-06-21 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 17e00562-291d-391c-b21a-0ee34553f88e | -11.0979 | -54.1311 | 2026-06-21 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 46aa57b8-e92b-36c4-9026-8bfa39e03675 | -11.0979 | -54.1311 | 2026-06-21 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 6189ce7a-705f-3608-a860-0b7d3d0cc479 | -11.0976 | -54.1516 | 2026-06-21 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 2876cfaf-1748-34a2-9507-57b8f57ec67c | -11.0976 | -54.1516 | 2026-06-21 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 2b8f130d-3973-35dc-9834-fbb6a700f0be | -11.0979 | -54.1311 | 2026-06-21 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| f51e2daa-0099-32ae-bffb-4cb487b3ed9c | -11.0979 | -54.1311 | 2026-06-21 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 37d44ce8-162b-30f3-b27c-6e22b3dd2ae2 | -11.0976 | -54.1516 | 2026-06-21 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| db0b5f13-14b3-35b5-98e1-2ac05564fcdd | -11.0976 | -54.1516 | 2026-06-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7ca76ef1-e535-32c3-803d-fab4aaf1c20b | -11.0979 | -54.1311 | 2026-06-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 01bf26e3-0897-342a-952b-ee0323227777 | -3.47517 | -66.06128 | 2026-06-21 13:27:00 | TERRA_M-T | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1a41594-166c-3cdb-9b5b-d8c7daf4269b | -11.0979 | -54.1311 | 2026-06-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| a5e4b265-cd3f-3fba-a5fa-74961faea34c | -13.3014 | -45.1976 | 2026-06-21 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 99b63570-a85e-37cb-88c9-2f1451de6e80 | -11.0976 | -54.1516 | 2026-06-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 118fab69-05c2-3fcc-a23b-26752cdf2c58 | -11.1168 | -54.1294 | 2026-06-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 244dddd7-0535-3db4-875b-6ac39599a629 | -11.1165 | -54.1499 | 2026-06-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 50b44a7f-a844-303d-a8f8-0de96275acd5 | -11.0979 | -54.1311 | 2026-06-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| bc00b05f-8c1a-337d-964e-b8a43afd8f11 | -13.3009 | -45.2209 | 2026-06-21 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b8e422df-c27f-3f77-bf4f-a5e2ad6d2d6a | -13.282 | -45.2009 | 2026-06-21 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 13703d3f-2a76-3f1c-8dae-7698ff895ed6 | -11.0976 | -54.1516 | 2026-06-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| d42b5664-3451-3dda-84fa-dc36ada60ac5 | -13.3014 | -45.1976 | 2026-06-21 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 90be08ae-da7d-3c7c-9a56-ee4f0c4b9d93 | -13.282 | -45.2009 | 2026-06-21 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 0aafffe9-4a89-3500-9e42-aa3d83064b69 | -13.3009 | -45.2209 | 2026-06-21 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6dca8f09-960d-32a8-b344-578413a889c9 | -13.3014 | -45.1976 | 2026-06-21 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 60db578e-c82f-3415-a4f3-8047fd108521 | -11.0976 | -54.1516 | 2026-06-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 38cf8a1c-336a-3e2e-92a1-cfc5fc89bebd | -11.0976 | -54.1516 | 2026-06-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 3ea3f120-694e-333d-bc53-44c48aecb12a | -13.3014 | -45.1976 | 2026-06-21 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 8420ca05-6056-3995-8821-a4061698d6a2 | -13.282 | -45.2009 | 2026-06-21 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 3b8bd9b8-8967-301e-90b3-7234d293c9d5 | -11.1165 | -54.1499 | 2026-06-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d1f41e13-a338-3e4f-8105-464a1598daf9 | -13.2815 | -45.2241 | 2026-06-21 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5413e116-0db6-3f60-97f0-74f80e3d912e | -13.3009 | -45.2209 | 2026-06-21 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c349c324-bf24-36b7-94e2-eaa0fcb9e9f1 | -13.282 | -45.2009 | 2026-06-21 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 2149fb33-0481-3836-a06f-5c0b8620a39e | -13.3009 | -45.2209 | 2026-06-21 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| ade1ac99-ce07-39f5-ba45-4ff63663f76a | -13.3014 | -45.1976 | 2026-06-21 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 407.3 |
| 8836be3b-7769-3bb7-b6f1-979710f7f472 | -13.2815 | -45.2241 | 2026-06-21 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 9663ade1-49d2-3a92-935d-3f2a93b8bde3 | -8.0527 | -46.0418 | 2026-06-21 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ed9d0cc9-6060-3141-b304-6738ddec0409 | -13.3009 | -45.2209 | 2026-06-21 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 163.4 |
| c675eb7a-eaff-3150-a65d-882d7c7912a6 | -13.2815 | -45.2241 | 2026-06-21 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 806dffb0-de9d-3bab-80d8-55ec6657a073 | -13.282 | -45.2009 | 2026-06-21 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 80f4ccee-ceea-3c8b-a5e8-816fee1a5b3c | -13.3014 | -45.1976 | 2026-06-21 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 386.0 |
| cee18169-9263-3a7a-9507-b9efd7b8198d | -13.3009 | -45.2209 | 2026-06-21 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 7e49d1c4-46a0-3dd1-b97d-eca34671ca2e | -13.282 | -45.2009 | 2026-06-21 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| da003192-a2cd-3d29-8224-5a905f101475 | -13.3014 | -45.1976 | 2026-06-21 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 342.8 |
| b0f3cce4-f06d-3119-9689-271530fd687b | -13.3009 | -45.2209 | 2026-06-21 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| d06ca2d9-df36-3f66-93ba-f226781ecc78 | -13.282 | -45.2009 | 2026-06-21 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 22f38678-51a1-3979-8d94-b508b187f6bb | -13.3014 | -45.1976 | 2026-06-21 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 43d37414-3992-393c-9772-5d64bc7e40ca | -13.282 | -45.2009 | 2026-06-21 14:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 11b27d24-9135-30fe-9826-d607e20dff7e | -10.9406 | -46.4363 | 2026-06-21 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| ececd1d7-6ec8-37b7-9388-db4b3eaaaec6 | -13.282 | -45.2009 | 2026-06-21 15:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| bcf21211-c0f4-3df8-8499-88c161c049ea | -13.282 | -45.2009 | 2026-06-21 15:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| de57b07a-9741-3f8c-a11f-b61407f98d17 | -13.282 | -45.2009 | 2026-06-21 15:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c18ad267-7ec6-3ea5-8ed1-3588666a96a5 | -13.282 | -45.2009 | 2026-06-21 15:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |


