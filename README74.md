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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70a61072-5fae-39d7-821f-b05bbaafaa62 | -9.94589 | -43.73349 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 662168db-5502-3cae-83b4-39c2a5662c59 | -9.94782 | -43.72057 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 56bc7ab0-5616-3102-a808-ab4e203be97f | -5.87767 | -45.81513 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d920b5b-0f1e-342b-b059-da25af300daf | -11.9152 | -46.74632 | 2025-10-02 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8e0bb93c-ff3a-3f6a-bfc0-a12db5a49f8a | -6.68508 | -46.05568 | 2025-10-02 04:29:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b643b160-149e-39fc-a652-8012f6f8507d | -11.81824 | -45.01065 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4657abbf-fe29-37ec-882f-2dbf1c9c859e | -10.2283 | -50.31607 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 57639b81-0f37-34e8-991b-6b55645fb6cc | -6.49012 | -44.29628 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e20b10c5-ea6a-3c85-8461-035597832300 | -9.92626 | -43.73932 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 8c7c9aa9-0e7d-3663-ad95-a31191398b1a | -10.20148 | -50.27436 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| faec2637-a06e-3d25-b66f-3611954e29f5 | -11.5345 | -46.9563 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea049592-62ae-3f48-a8cc-43e0efab402c | -9.93515 | -43.78011 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 379ad73d-2153-398c-80d2-d28fe37037ee | -10.81733 | -46.63178 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c87c9726-39bf-31bd-9f21-19f5c3e3c65b | -6.26517 | -43.88816 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83b25e2f-217c-3d94-9a3d-c8e895b5629e | -10.81843 | -46.62468 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb89b404-029e-31ff-9e06-5cb418639cbe | -8.15837 | -44.13015 | 2025-10-02 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 605f421b-ca7c-3ef9-af83-27a84e2ed2cf | -11.21988 | -48.2136 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db52e645-1211-329a-b58f-cfb1c8215700 | -9.04634 | -46.65766 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07edf8be-bd14-3ec7-b64c-9c4c1692370e | -11.67629 | -47.49657 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5771f187-a4ae-3201-9b2d-dd2e194483a7 | -9.93945 | -43.77639 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1b62da00-5b58-3a57-907d-4446e38c7c3a | -10.84798 | -46.65487 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 320f1ba0-95c2-3d1d-9efa-9fd11b8c4e4d | -6.77835 | -45.59026 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5136991d-36c7-3e70-ac0c-a7468d09893b | -6.35296 | -43.29847 | 2025-10-02 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f55f7a88-61f0-30a8-932b-0eb6974c5946 | -9.9336 | -43.74042 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 67470e8a-4af0-325b-b7a2-ede60751cf4e | -6.69355 | -42.81925 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4db06eaa-8fe4-3a46-b721-e5cdd105879c | -9.94718 | -43.72488 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b8c6e215-37c8-38fa-ba1e-01373de1a85f | -11.47762 | -45.00307 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c88d85d1-7026-37cf-a63b-419d26883125 | -10.86908 | -46.6073 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c673203f-941d-3c90-bf98-7c45ffc6e951 | -9.91511 | -43.6625 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 460c4bff-03f4-3c24-add7-be8bc15e3c2c | -8.50933 | -44.70359 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61b2d85f-6a87-3295-b11a-0c3f047d3726 | -7.01447 | -44.51604 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fc32d63-a786-3c94-b332-740bfeb63469 | -8.87378 | -46.58737 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 773e9319-1b33-331e-8f6f-0be953c3c05e | -11.8171 | -47.59147 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 56593d57-c49f-3452-8480-f1c4e1fbd6d3 | -11.27471 | -47.8295 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc98d927-bf43-3a2d-be14-2660edcf5727 | -9.77085 | -46.22047 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26a535fe-b271-3e08-84b4-074ec558b120 | -11.67129 | -44.27974 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caa75ef2-7e8d-3afe-8836-aa525fc6b4e5 | -9.41309 | -47.58553 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a63c5d72-c76a-3364-8c8e-8ae6d69c0f52 | -9.80119 | -47.84392 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c91e784-46b7-365c-8543-fad4e15dd1f4 | -11.43695 | -43.88115 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbc52bf0-931d-380a-9aab-fb195367c892 | -11.84348 | -44.96156 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b99f705-abb0-3012-bd7b-1e964b9940e1 | -10.44267 | -48.08659 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5dce1aa-bec0-3861-ac20-fd57898cce51 | -6.63998 | -42.08864 | 2025-10-02 04:29:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d75508c3-aa3b-3763-958f-a6eef1172b89 | -9.84257 | -49.95916 | 2025-10-02 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba96d727-f30e-35ea-8f85-5a03d2b57ae6 | -11.76701 | -46.82941 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13f6ceb6-f09a-3b94-82fc-4d702b466596 | -11.84289 | -44.96553 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5acfea97-780b-39f4-80de-7bc744eb8898 | -11.16352 | -47.27303 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d8496cb-8bf9-3ff4-b98d-48de0d8b2cf2 | -10.70534 | -48.00484 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e11c019-2650-315b-b211-8ee2c35e0149 | -10.22486 | -48.22338 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae47994e-ad2c-33aa-9099-e6fb573d7391 | -11.18069 | -47.18556 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eb812cd-7ff2-3b12-b6ec-1cbea04925fc | -10.23624 | -50.31312 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| a362f159-98d1-3bcc-a0f9-1bf9c4d47f98 | -6.5461 | -43.93329 | 2025-10-02 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ddfe8fdb-4893-3aa0-bf42-cffbe5535ae0 | -6.71948 | -44.61647 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69b72732-3eff-327a-ad34-807076a5e777 | -10.81497 | -46.61356 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fbce4ea-0cc6-343d-b66f-79daa6bcb204 | -9.94867 | -43.68984 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3614e17-1ed2-316d-a131-6c23206f0136 | -9.94759 | -43.67188 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d2d2a35-6e1e-337e-851c-3fe47137c48c | -9.89945 | -45.95467 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d59d1fbd-8d85-31df-8b5d-88ab2c9e902b | -10.20876 | -48.19485 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c981c949-c949-3040-9536-b7e56e452f94 | -7.77398 | -45.71214 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b8d5a9a-d2d1-3da3-8029-c8c1a43bd53d | -6.89931 | -43.1338 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5b2522e-f2ac-38cf-95b9-2fc2c6153910 | -11.17184 | -47.26355 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eebd1c84-fcd7-3c4e-8ed4-77961df7df3e | -6.26808 | -43.89262 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f888cca3-827a-30d4-a6e7-02be70e18874 | -5.88148 | -46.02921 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e3dca54-3b6f-380d-8b3b-b3d43176f7a1 | -11.59268 | -47.6421 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 488fb58f-e4f4-38b7-a8eb-fcf327af42e1 | -6.85834 | -48.65284 | 2025-10-02 04:29:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab8175ea-8e48-31fb-a737-26306d573c31 | -9.45143 | -50.90256 | 2025-10-02 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 145598b8-2cc7-322a-9ec9-d218b4876afb | -10.65616 | -48.50042 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5ac680c-bcf7-35c8-b9b6-a2af0ba65f9b | -10.9932 | -46.61592 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b7880ed-258d-3211-90e4-1b495b392e19 | -7.77392 | -42.5425 | 2025-10-02 04:29:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| c6f5538c-f5b4-3256-b8a9-4a039424bc84 | -10.32914 | -48.18506 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 224ba406-9568-3c06-84ac-20922b1285f6 | -9.41365 | -47.58201 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 566ea0e4-dfbd-3e58-9d71-321ba1a9c094 | -11.74818 | -46.82664 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c6ec30f-b8c8-3475-8fe2-f3185e9f1aeb | -7.56411 | -42.39634 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e08a116f-8086-3918-ab78-7d7945a49f7a | -10.93313 | -46.67181 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7d68613-930f-3b3e-92ed-eff727a05de1 | -11.79867 | -44.99657 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8545ae7-2a3a-3d15-8748-45a16a00fe6d | -10.85512 | -46.58691 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7cb01e5-f11c-3878-b077-b5686d21c067 | -7.77062 | -45.71164 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 383a69d5-d00e-33a4-8946-005d5ff0dee9 | -11.08973 | -47.82446 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3559d581-0c88-377f-9aeb-9329fafe4e21 | -7.53206 | -46.90278 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f7ca718-156b-3f2b-9d0e-6ce9d5250ed7 | -6.50047 | -44.2979 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0b11753-da91-369e-89da-e38e83285319 | -10.24056 | -50.30954 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| ece86aec-8769-36b9-8c46-1b888fc136b6 | -11.58546 | -47.64455 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63f74550-4997-3b65-b864-d495787dbdc3 | -6.26168 | -43.88753 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d81a262-00a8-3d80-8443-fe2f35879717 | -11.43563 | -43.89001 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8d615cb-5f40-3ea1-91e8-081fcbdaecb4 | -9.94201 | -43.75935 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f7e5fb5e-da9e-3361-a00f-e69b379d7333 | -9.93074 | -43.70926 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| effc5853-e223-3fc2-91fa-7e1ca94c553f | -10.65953 | -48.50098 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7381d9c9-4333-327b-ae0e-d5c0061d7f07 | -7.02835 | -44.4721 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db57187d-2461-3a20-8b7e-9e36faa70996 | -9.08912 | -46.72578 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0468f7a-e3c0-36f7-a725-dd26f5c9d5c8 | -11.09362 | -47.8215 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fca3227-9c50-3479-a160-5cb74dcb3ae2 | -11.4295 | -47.28357 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d393d19c-3f33-3829-8cf4-bd19e6f50467 | -9.44766 | -50.90189 | 2025-10-02 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a9446da-b4a9-3e36-ab35-232d65cf068d | -11.00042 | -46.59157 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc65f182-46c9-320e-b11d-efe483b9c978 | -10.86092 | -45.41322 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d5eb2ab-c567-39dc-a286-55b310e6678e | -6.72404 | -44.60966 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2de26961-c755-3644-a923-852b6e17ac2f | -10.21813 | -50.28846 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02ad10fe-1970-3f0f-be6c-54daa74d0bbb | -6.73306 | -44.14574 | 2025-10-02 04:29:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0edeb878-b511-3304-9c04-eb7d86a67475 | -11.26888 | -47.81007 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50812c39-ffbb-3e52-b11b-068ecb44bf6b | -11.53839 | -46.9533 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 217846f1-798c-38ce-aa93-728933caa31f | -9.80731 | -47.84855 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da4b869e-6177-3505-bf7b-5d50ec58dd78 | -9.40481 | -47.55166 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README75.md)
