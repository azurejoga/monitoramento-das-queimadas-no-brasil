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
| dcd029ca-43fb-3efc-991c-b4114f42d9d2 | -6.68686 | -43.68507 | 2025-06-12 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c16e249f-343c-3a6c-a2b7-86e548680e42 | -10.1755 | -49.35592 | 2025-06-12 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba9cb6a-c764-3885-9e38-44cb8f4db595 | -11.00875 | -47.76416 | 2025-06-12 04:27:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee4a59a0-a2de-3f4f-a33f-755e18ba20fe | -10.66315 | -49.3598 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c12b002-4c89-3c1c-90a0-7d142e05cd81 | -5.64756 | -43.6044 | 2025-06-12 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2364b79-59d2-319b-914d-74d7858d385e | -6.67871 | -43.7611 | 2025-06-12 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dca818fb-780a-3055-a11f-8295edce700f | -10.51451 | -48.69258 | 2025-06-12 04:27:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3c0a115-778e-3da5-b7b6-fcc80766b16c | -6.68637 | -43.68382 | 2025-06-12 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c49f0f3-7389-3b7f-9914-c7bd07ef2b8d | -10.65792 | -49.35982 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7213b6f3-cd2d-38e9-a7f2-57ec20c48bd4 | -6.9442 | -44.56458 | 2025-06-12 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9acc9a47-eb59-36b3-972f-ba978859e521 | -8.66498 | -47.138 | 2025-06-12 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d460b812-7524-38fb-a68c-7dcb2eb286f3 | -10.69725 | -49.51927 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8e080c7-f854-3047-bdd6-56ba2e8c890c | -5.06705 | -43.72603 | 2025-06-12 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 483b2bf8-085f-3f84-8266-bdb0f13f5d47 | -9.38727 | -48.42428 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cac5a0e6-daf0-3346-abb4-a028146183e0 | -9.25129 | -57.53447 | 2025-06-12 04:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bf676bf5-63b6-3b37-92d2-847d5f95390e | -6.94764 | -44.56512 | 2025-06-12 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c615c01e-7981-3534-bbfb-ec647d4ced14 | -6.67934 | -43.75711 | 2025-06-12 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f53bda2-dabb-3e2a-b037-c08c7a22d9a1 | -10.6536 | -49.41711 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b58938ce-d28d-37fd-b462-722ec6a8fa89 | -10.37501 | -49.91555 | 2025-06-12 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 454317ae-5ef7-3c30-91cf-bbb1826d3604 | -8.71744 | -47.8544 | 2025-06-12 04:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a78c42a0-99da-3fbc-b0f6-a0df54e2c486 | -6.74752 | -44.18346 | 2025-06-12 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f196cf5b-1fe9-3739-acdd-89a2bd04f8dd | -10.63099 | -49.43785 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d355e15-07d0-3061-9552-960fc8e8fb49 | -6.06954 | -45.64204 | 2025-06-12 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66f6a967-ea64-3fea-8421-345bb3d15070 | -10.33487 | -44.3113 | 2025-06-12 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7418928-0061-3c78-8c1c-5112c8101e16 | -10.66199 | -49.35659 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ed392e6e-545c-312b-8ad9-a413ca08178e | -10.19423 | -49.593 | 2025-06-12 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0daa01e1-3162-326f-be2c-4c893c8d7158 | -6.06675 | -45.63803 | 2025-06-12 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e863abc0-b2df-3e9a-b893-5320cccc8535 | -7.24119 | -43.106 | 2025-06-12 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 588dafc9-e950-3c90-8be8-193e1d511d38 | -5.06276 | -43.72562 | 2025-06-12 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0b00774-a3bc-3003-b9f3-f115be9c5f95 | -9.60444 | -49.02588 | 2025-06-12 04:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e6f3a49-4af2-3dbf-80c9-8568dadce4db | -6.94363 | -44.56832 | 2025-06-12 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87b42d88-6904-3fdb-86c4-a3ef336dcc77 | -10.86337 | -42.25026 | 2025-06-12 04:27:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1606032-062b-3fe9-b04a-df61880ad872 | -8.18091 | -47.60784 | 2025-06-12 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2464b723-b5d5-3ac4-bfff-2f4ae86b12ca | -9.41174 | -48.42793 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9be8bded-923d-3f9a-9ae6-14adb2a1ca3f | -9.39048 | -57.5258 | 2025-06-12 04:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6a74ee9e-4792-3995-97cb-327ea94d8dfc | -8.58787 | -47.09363 | 2025-06-12 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 374549db-a41b-3cb9-a971-b447b9fd6407 | -6.60379 | -44.25644 | 2025-06-12 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 120a79d9-7373-31e5-adc9-6321f2bcaf28 | -4.82098 | -44.35377 | 2025-06-12 04:27:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12840926-4e3a-3008-9f4f-9087a6f629f1 | -10.65643 | -49.4215 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 63ae6c5c-8616-3590-a7c2-e230596b0a6f | -6.94478 | -44.56084 | 2025-06-12 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4354270f-d89b-30db-8f82-3ed131e65968 | -8.96541 | -47.96766 | 2025-06-12 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c49d3988-c9ab-30c1-b137-a2b4aab0894f | -5.64816 | -43.60048 | 2025-06-12 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cffcaa5d-a40e-3b9b-8964-d3dce360168f | -10.19442 | -49.59019 | 2025-06-12 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 099317ef-0df8-3438-87f0-c5b61382875b | -4.71019 | -48.42942 | 2025-06-12 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea1c39a0-e491-3eec-a848-76229ccc671e | -8.95359 | -47.28138 | 2025-06-12 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce80b8c4-7c7b-31d3-83ae-1a98262d6133 | -2.90276 | -54.49152 | 2025-06-12 04:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645e88a5-7e4b-3ea4-8f0c-1eda57719650 | -5.06356 | -43.72548 | 2025-06-12 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 095cf12b-a95a-3ffe-9a66-3114436a2486 | -5.64403 | -43.60387 | 2025-06-12 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9fd9b61-78a2-3eac-8d05-85305e019f5c | -4.48649 | -48.87073 | 2025-06-12 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 872de3fa-caa1-369a-ae74-b58697c2a6c9 | -8.5851 | -47.08961 | 2025-06-12 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee1838c5-1ab4-30cc-b350-66a0f0a5deb0 | -8.96205 | -47.96711 | 2025-06-12 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6260cdcc-f1ba-397b-84fa-32becb1c2973 | -10.65926 | -49.4259 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66d68661-8a67-3b0e-997a-b040e8436993 | -7.23687 | -43.1098 | 2025-06-12 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6e190fb2-c0ca-3125-b200-71525cd68677 | -9.60625 | -48.54205 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db07badc-290d-316f-a109-50b5acfeee7c | -8.5912 | -47.09417 | 2025-06-12 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85f32f89-726a-310d-a6f4-f5db773286ed | -9.0549 | -49.5171 | 2025-06-12 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d605c6e-0fbc-3825-9530-32d2483bfdb0 | -10.79603 | -49.68672 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8db4bc3d-b571-3d7e-8ff5-9c1c3d670af2 | -9.41513 | -48.42849 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dd4290e-f9c1-3698-95d0-0df6b5ce202a | -11.33973 | -45.21889 | 2025-06-12 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93e717bc-c0eb-3414-8f6f-79c1444ea2a0 | -5.07053 | -43.72659 | 2025-06-12 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cd2ffec-4611-3a85-b881-3b1dc9cb78be | -9.40759 | -48.4276 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c11fcccf-5585-3495-bb5a-a264fad10a6b | -7.23751 | -43.10547 | 2025-06-12 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 497db104-d2ec-3b8e-801e-3cb631a51e50 | -9.85308 | -47.87777 | 2025-06-12 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 715db563-5eb3-312e-9bbc-3dd308f4f6e5 | -8.95026 | -47.28085 | 2025-06-12 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c1ab78f-1cf2-3d4b-99c9-d8e2c69214fb | -8.66221 | -47.13397 | 2025-06-12 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d967814-fc91-3cde-9dba-9780e6ebd234 | -5.91522 | -43.45621 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d55b1e3d-a25f-3ad3-afab-3f33a56b1fca | -8.96819 | -47.97178 | 2025-06-12 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3485fa41-3153-3dd8-aaef-ac40fda06f0d | -10.65427 | -49.42598 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a1c24a4-7323-3a85-b199-a5c418ed9e9c | -10.70262 | -49.50828 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0edbc5f9-b222-3dfc-b4df-ee6a6b55dd9a | -10.17613 | -49.3521 | 2025-06-12 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a88c1e86-c2f0-3fa3-8bfe-f3a5ed08625f | -10.65706 | -49.41769 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 96f75776-d32b-347b-83ed-0bd376dd9c20 | -10.13626 | -47.43888 | 2025-06-12 04:27:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10632f76-b2c8-3bb3-9726-44f7d50b41dc | -10.89694 | -42.24342 | 2025-06-12 04:27:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4ac44aec-5dec-3e21-a212-5c69c7800758 | -9.24547 | -57.53342 | 2025-06-12 04:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a70cf952-3d55-34ad-98df-bef553a4a278 | -10.28162 | -48.20619 | 2025-06-12 04:27:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec80c0ce-e732-3b8d-aee6-805c4009fc34 | -4.71433 | -48.42614 | 2025-06-12 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4910c0ad-f3af-306c-9f87-e97d3f03a4df | -10.69852 | -49.51155 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8d57ac9-3735-3a8f-b789-405d25c9187d | -8.96425 | -47.9748 | 2025-06-12 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da2f2341-e297-3da9-98eb-54e4ac79b30c | -4.71371 | -48.43001 | 2025-06-12 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddf06c40-005c-36be-8fe3-58d81d8dcc09 | -9.39066 | -48.42483 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83676f9d-4b89-31c1-a18e-97b8eab03206 | -10.70199 | -49.51213 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fef85dd5-73da-3c82-b30b-1cd1a7e620ac | -9.0052 | -48.73643 | 2025-06-12 04:27:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 029ab16c-67db-3c15-bcf0-cb390e17b458 | -10.66137 | -49.3604 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4524cad1-024b-3f59-b150-9ffa6c07cfa0 | -10.64894 | -49.43687 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee289e35-3079-368d-af0b-5035bcae3839 | -5.9146 | -43.4602 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffe3e0b5-2359-39c2-a5cf-7a45720f4e14 | -8.07352 | -46.47581 | 2025-06-12 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7e444c2-c215-3efe-b174-ed7df7db0011 | -10.70419 | -49.52043 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9b4b1aea-d735-369d-8a31-0a667c543a87 | -8.30981 | -47.91742 | 2025-06-12 04:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83daa992-518e-3d30-a05f-69549fa549cd | -10.64979 | -49.44 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c3551fb-5a97-31a5-9eb4-2a523a5a0fea | -10.69788 | -49.5154 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eefbd093-8b72-35c3-9d84-c2730f1fcd59 | -11.08636 | -43.15805 | 2025-06-12 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c20073e4-7601-3cb5-b840-ffdf632c3c37 | -7.86344 | -47.88668 | 2025-06-12 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7861abb-af2a-3c49-a4fa-793de251e1d5 | -10.65143 | -49.42159 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 86fec3fe-9bda-3ce7-b265-6c9452506e09 | -11.08478 | -43.15491 | 2025-06-12 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cf56a5f-14d7-3b18-9964-7499bc03a22f | -9.27426 | -48.26097 | 2025-06-12 04:27:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce52d2dd-4449-37f4-9e0d-73c35743f7b8 | -8.87955 | -47.66626 | 2025-06-12 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4784130-c48c-3325-8b89-7089698c21ad | -5.85447 | -43.82933 | 2025-06-12 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81a74cad-c921-387b-a83c-11ac42baeca3 | -10.65297 | -49.42091 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fc53e64c-7156-3549-bcec-695cdbd8c3e3 | -9.2505 | -57.53863 | 2025-06-12 04:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f96205c3-3cbc-3e52-8b47-4b57fd163177 | -9.85252 | -47.88131 | 2025-06-12 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README12.md)
