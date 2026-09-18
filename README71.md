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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9141506e-0503-3baf-b5e2-c2f30f9ee30c | -9.73925 | -46.11288 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd7d3dee-cf10-356d-9828-abff20a2461d | -6.43783 | -44.95219 | 2026-09-18 04:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84e9dfaa-a683-3e8b-9057-934bbb1ef997 | -11.46601 | -47.41381 | 2026-09-18 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f07c7d9a-df34-3bbc-a9f5-45b57cb2f687 | -7.19733 | -44.10936 | 2026-09-18 04:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6d74cce-61d3-3229-a586-27672d6ab0bf | -11.39989 | -47.6364 | 2026-09-18 04:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62d3515d-d639-359d-a419-51baa342378d | -10.11984 | -45.56297 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5098b22-222a-3888-95cc-ab280848a0fd | -9.46588 | -45.44437 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 619d6cf4-afe3-34e0-8153-b4452417569d | -11.27333 | -54.11901 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd421863-6d78-31ad-b170-484ea701fef2 | -12.41305 | -50.67751 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45cf8365-8acc-399d-9844-c7549b1f03f9 | -6.67008 | -50.92535 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 707a4c8d-a2f4-316b-93b6-50c75c8f1cb9 | -8.90024 | -44.97663 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 568df305-5ce1-3d1e-b688-35c4105a7d22 | -12.16857 | -46.98687 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3c365d0-8527-3181-ad4c-085a1442e177 | -12.39661 | -48.47556 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e10bfb0e-bf15-3f6a-aa79-90f4f90214d8 | -6.45619 | -46.01166 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27085567-dbab-3b64-9fe5-c322fbe61cee | -10.63814 | -50.24788 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8acee32-4420-331f-b14e-4aef5affe4b1 | -12.17435 | -46.97527 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1d931b7-f4d7-33ff-890c-80c38bfb199d | -9.92997 | -46.52525 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87184960-fdfa-3435-a7eb-7b979d5612d2 | -6.95044 | -43.10514 | 2026-09-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b13cc9f-d625-359b-ad32-4a558fe316d6 | -10.66269 | -50.27081 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a02e7ce1-330e-310d-ba84-90f7018da961 | -7.46105 | -46.84272 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dccc9f33-b0e0-311a-8dba-7eb990ccbc22 | -9.60471 | -45.35192 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4f1c373-1e69-34f5-9280-fc8854272f3a | -12.55263 | -50.72179 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0650391-1295-3978-a23d-e5871156da2b | -11.13044 | -47.70947 | 2026-09-18 04:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2aacbfff-b6b8-3b0f-8ef4-a1272d353ab0 | -7.57516 | -57.69457 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1a3b360-3c5b-3f54-99e9-029d21e48088 | -13.25456 | -46.91304 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39e85517-a287-37c8-b92b-42570e7df84f | -12.33977 | -50.76926 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb7f77ba-4d02-30e8-a44a-c70e7b064241 | -9.16004 | -49.99777 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e733e24-5b2f-3b44-bb29-a3b6006789ed | -4.88233 | -56.05866 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bafa967-27cf-31c3-b4a7-82ca54df1fb7 | -10.95297 | -54.09009 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc05ba0c-224e-3db5-a1fa-26c6537b8987 | -9.74031 | -46.1053 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 316f0dbf-6b24-351d-83ce-680d6242fc91 | -5.75383 | -51.92066 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31297a49-3e0e-3850-9800-17437b0ba2da | -12.55605 | -50.72233 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbf36dc3-47ee-3e73-9a7f-13d275444ac5 | -7.66227 | -46.08537 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae53f34f-bef9-3af1-8a11-9c24676e7291 | -6.66953 | -50.92883 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9af26fa7-6b46-3be9-939c-6fe4753c0685 | -9.9153 | -48.38845 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b86218f-85d3-3075-9d90-eee17eee4762 | -12.99632 | -46.92231 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00be498f-4d93-3655-b975-0663aed01c5a | -12.27212 | -50.75477 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43a8cfc0-77ed-36c4-a922-ae1f9ccd44e6 | -10.54271 | -44.85114 | 2026-09-18 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2fc763f-bc9e-3cff-a6b4-007befe89a46 | -6.14395 | -57.69205 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ffbc8b1-baa0-3634-bb27-93f23af05602 | -5.89173 | -52.08774 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88b395dc-3598-3461-8136-882769642cf2 | -9.91229 | -48.3834 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dc57b20-1fec-3fbb-8365-22b3f1a0060c | -12.3815 | -48.4732 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f29f6fa-8869-3ded-af04-545d67b092f2 | -9.55816 | -48.10719 | 2026-09-18 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 360fc1cb-8646-3e99-b36d-712cb9d27466 | -7.66009 | -45.84169 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e00ad985-ede1-3326-b503-bddd3e49c046 | -9.75019 | -46.57127 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3f42686-edba-3a67-93ee-35297a2ed4c7 | -11.29349 | -43.35036 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10f33948-4efb-3dd1-ac11-7b4d7231553f | -12.39452 | -48.46848 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1933bf55-750d-3097-982e-4fba1e07835e | -9.75524 | -46.09115 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f31de98-4b58-3afc-97a9-18116698f291 | -6.65733 | -50.91977 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2a3a1c9-f5a2-323f-8e97-8c100a3810bc | -6.58807 | -46.72957 | 2026-09-18 04:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 281f658f-3ff9-327e-8abc-20a2be36477d | -13.23827 | -42.32563 | 2026-09-18 04:57:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| a0f9dcf8-5633-3841-aae6-14755a472d90 | -7.58122 | -46.35233 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3cefc430-080a-3bda-8f3e-959d2d71b8e4 | -12.26818 | -50.7808 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3b50bf2-d688-3e66-bd3f-7166b59a44ae | -11.81263 | -46.79109 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da848350-4980-3efc-a2bd-04bef0d43c7c | -10.66096 | -50.46403 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5d5ae90-170a-3997-a228-e53b377d3ac5 | -8.68018 | -45.44056 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60ac6f96-c606-34b3-b99f-3f9b3da7044b | -10.38218 | -46.63313 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 572d5b00-2a8a-32e4-8a64-4a044a0b2c83 | -11.87677 | -47.58029 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac5177c8-648c-325a-97b7-4e0c3e7a0b2f | -7.82103 | -45.10087 | 2026-09-18 04:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eede04a-b4de-3a52-b571-37be2ab43e96 | -5.83807 | -52.0904 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ceec4e9-4157-3947-a8b9-796b81e59ec0 | -11.89405 | -47.57227 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a29242a0-0237-3064-8ef3-762b297ddedf | -10.67866 | -50.25803 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86e160e3-8213-38c4-8d01-03014fda6849 | -10.65069 | -50.23455 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af58493-bd97-337b-ab6b-e7e168af0e24 | -11.2814 | -43.36198 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3184216-a32d-3d2d-90c0-392b1246661a | -9.77266 | -46.0901 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ae4fea9-ebcf-3fee-bb94-379c41e28d0d | -9.71624 | -48.15176 | 2026-09-18 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d95118ed-cd3f-329f-b18b-2b2bd7fd7473 | -9.72159 | -54.8114 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ca8aefa4-9309-3a1c-8755-b13340419467 | -8.88501 | -45.89606 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13d7dfe9-4503-353d-9d08-9425fc9880c7 | -9.9401 | -46.60094 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bcfed6e-1c09-3b79-8db8-0a4db3acc8d3 | -10.90602 | -53.98882 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3b1e4c9-78c3-3d4e-b309-ccd0e0be4f49 | -9.94192 | -53.98795 | 2026-09-18 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eee9bbe8-65f2-3e71-b0e8-db698a76eef5 | -6.93418 | -43.11368 | 2026-09-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 776d9bb9-2120-3a0a-b0dc-40709f205c55 | -13.23779 | -42.32967 | 2026-09-18 04:57:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 93045b53-9d91-3529-ac81-172f5438f390 | -11.52123 | -46.87532 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af62206d-cac2-3649-b197-0ff07079c9cd | -4.51621 | -56.07888 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e39593a-e876-34f7-8eae-9a695eeb360b | -10.10403 | -45.64202 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3367d42e-0360-38a4-a8a5-7068fe922381 | -9.91161 | -48.38792 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeb30a32-7b65-3b66-9334-2a0cced73543 | -11.88144 | -47.57574 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c254c017-0874-3c36-a4cc-4bab85becdf3 | -9.55139 | -45.44115 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34132ba4-692c-35f3-917c-4d07574b9c8e | -8.84968 | -46.9685 | 2026-09-18 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 952931e6-6f91-3143-bf70-fac173e843d4 | -8.6586 | -47.46463 | 2026-09-18 04:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d08d6c2-824e-3fae-83d5-c65b77b75258 | -11.80996 | -46.81038 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b39d480f-12b9-3257-82e8-5a3c69736fce | -9.56409 | -45.44683 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b711bb1-4638-39f6-be11-03e750edb2ae | -11.32262 | -46.76138 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9623fc8e-1f50-3cd3-9679-633789045844 | -10.53805 | -44.85049 | 2026-09-18 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddb16595-e2c7-381c-8f83-07a124a70aa6 | -12.55035 | -50.71375 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87509dc7-393a-3742-a579-3c0fa51ce3b3 | -12.3193 | -50.76603 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e7521bc-ca6f-3ece-a5aa-ffd0556d3cf3 | -9.54693 | -45.44087 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b2e99e4-db1e-3aca-bd9c-0f70b26b3cff | -9.59815 | -45.86703 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1a16797d-f396-38aa-bfe0-61c7812868ed | -8.77671 | -46.8947 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94f26830-bccc-3d78-ac88-f6d206d79913 | -12.46209 | -50.70058 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56b07ab4-5432-3bec-98e1-d95150cc5529 | -11.32485 | -43.35431 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12ddb90c-0b9e-3ce4-929b-de172cf2b8fd | -9.71246 | -47.09449 | 2026-09-18 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c4ab1cf-9832-396a-bb8d-c46bb2674d64 | -8.89912 | -44.97326 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38f26ec7-5e54-3a3b-b023-8ec354010a95 | -9.19269 | -46.76086 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36274514-6f44-3069-909d-9a8a531566f1 | -11.8932 | -43.81791 | 2026-09-18 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35bce538-330d-3a89-b5d6-d78f49276505 | -12.57708 | -47.09299 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 923e322d-74b1-31a9-961a-28116d970c27 | -7.657 | -45.83368 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59669d23-fed2-31ab-81fa-1730cf9d0491 | -10.1078 | -45.64693 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d708e688-fa39-3898-a327-f8bc52574c5f | -7.29194 | -38.96331 | 2026-09-18 04:57:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README72.md)
