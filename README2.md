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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9512d171-3b9b-39d7-9f6c-bc000be11993 | -6.6195 | -59.0416 | 2026-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 95b537f7-881c-3115-afca-f8f8f5086cab | -8.5171 | -46.5338 | 2026-08-15 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 89a50963-8361-309b-ab62-6d3fba65d099 | -14.4302 | -51.9243 | 2026-08-15 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0804c0fe-0edd-3134-86a0-1b2b3a6b6647 | -6.6194 | -59.0609 | 2026-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 88c40718-9144-372a-a21c-0fbdf93bdc68 | -3.9785 | -49.4563 | 2026-08-15 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e9e2c207-8ce8-3fa9-b008-09d2b5aaa61d | -6.9686 | -59.2783 | 2026-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 525294b1-7c53-3963-94ac-56a8e4a00a31 | -9.1219 | -46.404 | 2026-08-15 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| dccd95ef-620d-3414-b086-d6712d7d865a | -8.9041 | -60.5577 | 2026-08-15 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 19e328ba-895d-35fe-9735-0fc16348bb03 | -14.4685 | -51.9405 | 2026-08-15 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6bad70ea-129d-36e3-9826-d42a5802adcd | -6.9685 | -59.2976 | 2026-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 99f757f1-130a-399e-ad20-4c2a894dbaa2 | -14.4499 | -51.9004 | 2026-08-15 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| de56bd94-fd85-31fb-8fb6-53d460d59e1d | -6.95 | -59.2984 | 2026-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0d2090b9-a4f6-3a11-8c80-3fd065d8a70a | -6.1222 | -44.0271 | 2026-08-15 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| ddfe8d7c-bdb4-301f-b826-911cb7a4ce1a | -6.6013 | -59.0037 | 2026-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 6b3c6d4a-508c-3f97-9164-776f93b55452 | -14.4492 | -51.9431 | 2026-08-15 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7681e54e-c9f3-3bed-b667-11798e2a8486 | -9.1408 | -46.402 | 2026-08-15 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d13f54c7-2b5d-3ccb-b250-aa7ae88495a4 | -14.4495 | -51.9217 | 2026-08-15 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| cfad9d20-0a4a-39ee-81f1-93a43c7c52fb | -6.9334 | -43.6333 | 2026-08-15 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 211.9 |
| f2d57c0e-441e-31ad-87c7-a2b020803b57 | -8.9601 | -60.5165 | 2026-08-15 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ae317619-2099-3dbf-b4f5-110c3798cd7f | -11.3996 | -46.3305 | 2026-08-15 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 58856eea-e7c5-3201-aa45-e834e1852a11 | -6.9145 | -43.6351 | 2026-08-15 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 1e959e0d-bd15-3e7b-a7bd-0ec22ef253b2 | -9.103 | -46.4061 | 2026-08-15 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 2c3b8ff6-3e0d-32cc-aaad-d469238fde89 | -6.6195 | -59.0416 | 2026-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 90f64acd-0d8f-3ccd-95eb-ff61808ba856 | -11.4 | -46.3079 | 2026-08-15 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| a5c69e1e-8882-3ee1-b5db-47b61e1fcca0 | -6.6193 | -59.0802 | 2026-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c637539c-3220-3fd8-bbd6-39926f09438c | -20.46121 | -54.75942 | 2026-08-15 00:48:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6228f3d7-18c4-3c1c-b535-deafd40a339f | -14.4492 | -51.9431 | 2026-08-15 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 5eb85cde-a965-39e8-9d4c-beb2290e7020 | -13.2424 | -54.1855 | 2026-08-15 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2dd0f55b-c6b5-3d6f-9311-6af62adf950c | -6.9145 | -43.6351 | 2026-08-15 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 8796d8b1-3a71-39e5-ad58-a3159e2d9290 | -6.9502 | -59.2791 | 2026-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.1 |
| b8ca4088-0f80-3011-9596-fda65eae183b | -14.4302 | -51.9243 | 2026-08-15 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| ef6b247a-638d-32a7-92c8-2b7dbe741562 | -8.9601 | -60.5165 | 2026-08-15 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 34ae12e1-f4fb-3c2c-b8ed-eb31df473d94 | -6.9334 | -43.6333 | 2026-08-15 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 8b8b1796-0c26-37d7-856d-5c2516125e38 | -6.9685 | -59.2976 | 2026-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.3 |
| b83f2895-0564-3b48-b7d5-fe761e33db36 | -6.6013 | -59.0037 | 2026-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f5d34c20-bb1d-30cd-b17e-29b50ad6e79a | -6.9686 | -59.2783 | 2026-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 37c98f59-4642-3111-a6a2-6c7cb2974def | -6.95 | -59.2984 | 2026-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 292.2 |
| 661249c8-fa5b-3a66-a3e9-4cc6951e628f | -6.6195 | -59.0416 | 2026-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9a0ec080-c9ef-3f78-9c38-84eb6bccd522 | -14.4499 | -51.9004 | 2026-08-15 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 54f130b0-e4f9-3de1-a615-8dac6d1da5b6 | -6.6193 | -59.0802 | 2026-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2af4a8b3-26f1-30fe-b80f-671d08a33740 | -9.1222 | -46.3816 | 2026-08-15 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 38478803-27c3-3e55-ac49-6c59980c4e30 | -9.1219 | -46.404 | 2026-08-15 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| f56bedc6-e323-3e4e-b49e-abe3e84ff106 | -11.4 | -46.3079 | 2026-08-15 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 0f50029d-5277-3cf1-99d9-0ac73b007616 | -14.4298 | -51.9457 | 2026-08-15 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b93bc7ac-fb83-3667-9664-c2ac4f25eff0 | -6.1222 | -44.0271 | 2026-08-15 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9b671082-17c7-37c9-a406-c7c43d08d524 | -14.4495 | -51.9217 | 2026-08-15 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 91ae5a65-e58f-35e7-a2f5-2e2ae7e4dc46 | -11.3996 | -46.3305 | 2026-08-15 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 770162fd-c2ee-37ed-8213-1d860c54ce11 | -3.9785 | -49.4563 | 2026-08-15 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 429d55cb-2cd0-3968-b822-7984e45e4b06 | -6.6194 | -59.0609 | 2026-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 7bf289ac-cb29-3375-92e5-80ae8258a8a8 | -7.58104 | -61.22781 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57d9ec43-b672-34f3-b108-80a1d17f0468 | -8.94834 | -60.51231 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c5109d58-a5ae-30cc-9388-711b80a2c945 | -8.90042 | -60.55528 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2618bc76-0c8f-3692-baa8-91e28242a74b | -8.98116 | -60.53786 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 672dbbd2-ba85-37d3-b315-f7c24b996acc | -7.42076 | -60.00154 | 2026-08-15 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b0b2edf2-0b9b-3444-9093-38aa6c4c1234 | -8.95714 | -60.51105 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 21a60c4b-9d80-3b5c-9fa8-beefdaf530d4 | -8.96961 | -60.53636 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6908647c-3a2d-31ae-b2ad-e98df40d4721 | -9.34467 | -62.34785 | 2026-08-15 00:50:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5c0f7072-bd95-3102-a15c-05fba49aeb88 | -7.59809 | -60.87751 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a5082ce0-767a-3abd-871c-0b0117171461 | -7.55493 | -61.16839 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 0d79a1c4-f765-3f2a-a3c8-4cd0f88b296c | -8.6048 | -54.67404 | 2026-08-15 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2de57b34-33f4-3c9f-9f8a-7a197c88b063 | -7.39279 | -59.9963 | 2026-08-15 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6ab89914-acc1-385d-b8be-c65393dd8d9f | -9.34595 | -62.35757 | 2026-08-15 00:50:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 18e9eb55-edd5-3a1a-8857-83fcfd52b5fc | -9.97439 | -53.94005 | 2026-08-15 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| c124c7d6-f292-3c8a-98b9-78ccadbdb5db | -6.83647 | -56.42916 | 2026-08-15 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 5ac4c395-cbd3-302d-9401-ac89cb39dfdd | -7.69265 | -55.16205 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 3aab907d-c3b3-32ca-8387-37e44fabd667 | -6.84753 | -56.42756 | 2026-08-15 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c1568c85-33ff-31ee-900c-fab677740bb0 | -8.96594 | -60.50979 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 82b31071-d9a4-3196-b6f5-f28aad2c3e7a | -8.64746 | -54.70509 | 2026-08-15 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2f2e8198-f422-3a5c-b175-dee20d09d856 | -8.03248 | -55.13801 | 2026-08-15 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 50653bbd-b503-3454-b306-670a259b120e | -8.97994 | -60.52901 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0fbef846-1ddc-365e-a557-35daf3f26f69 | -8.78905 | -64.04073 | 2026-08-15 00:50:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd849f1e-2d68-3e9d-b3a2-7feee4915805 | -6.78402 | -55.84877 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 61786c82-c0d7-3178-95c5-30a6bfe411b7 | -6.85857 | -56.42579 | 2026-08-15 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| f2ff7411-446e-3037-bb93-0e00520466c9 | -8.95836 | -60.51991 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 33d24442-fb0b-3a70-af22-bcba83be0621 | -8.26468 | -57.34631 | 2026-08-15 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d66f22c9-dd78-3829-bf96-c0392782b2a2 | -9.35384 | -62.34655 | 2026-08-15 00:50:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 84f3988b-a3df-3543-a8fd-182097269c68 | -7.58225 | -61.23666 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 70d883a9-2fb9-33a1-9560-3e1e65446a32 | -9.97758 | -53.96006 | 2026-08-15 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 5f247e20-6a66-3fec-81fa-1bd56b58569d | -6.64634 | -53.42292 | 2026-08-15 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| cbaa8f22-b17a-397a-9ad9-3d693af95a0c | -7.58929 | -60.87876 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 46258f6f-c220-3d12-bbd0-09f409edc956 | -9.85434 | -63.05816 | 2026-08-15 00:50:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 21589c5e-b06c-3360-a54c-fe1fad77f242 | -8.89162 | -60.55654 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| aafd2ee3-17e1-3f82-a323-1dfec7874317 | -8.90165 | -60.56414 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 76475776-6db7-3296-be48-65ca5f09abab | -8.96716 | -60.51865 | 2026-08-15 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 0cb29a6f-0f9a-301a-b3c5-cf648647d439 | -7.45103 | -55.30756 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 5e7979e9-7349-3f7f-a64a-fcc43df4ae45 | -6.8497 | -56.44198 | 2026-08-15 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 7c93880c-fbe3-31d6-8fca-199d0462400c | -6.79324 | -55.83106 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 72e45982-f9a9-3738-a16d-dd205a7ebfe3 | -7.59106 | -61.23542 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 96378308-f8ee-3e07-b187-c86beda33e33 | -6.79561 | -55.84705 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 5a1231d5-6ab6-37e9-b964-f1e94f9694bc | -7.55614 | -61.17723 | 2026-08-15 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 13bb4f63-51d9-3f07-95b2-9db32564307b | -6.85641 | -56.41131 | 2026-08-15 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 0ce25c00-a552-3347-9e5e-a1c25d465dd7 | -13.26442 | -54.19576 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| ff8290cd-a287-36dd-8ee3-c9f635ca9d8d | -12.13824 | -57.20631 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cbe777e8-cc26-3f99-9fd2-fefb941a630b | -14.29108 | -51.95279 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| fbc8c2ef-4b6a-34b8-bfec-745bb7337c77 | -16.88984 | -54.15506 | 2026-08-15 00:50:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 401c7f1e-4739-3668-9082-7e0296127e75 | -14.44417 | -51.93656 | 2026-08-15 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| d5273330-79fb-38bb-bdd8-85c442ea0605 | -14.12133 | -53.6781 | 2026-08-15 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 02fd6a34-7fd1-345c-aaab-ce3d7a985b0f | -16.89314 | -54.16388 | 2026-08-15 00:50:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 58ce39f5-01f3-3c68-89e4-14af2dfbb87c | -16.87654 | -54.14255 | 2026-08-15 00:50:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 8affc86b-158d-3470-8dc3-7a8315ff6e54 | -11.59263 | -54.69723 | 2026-08-15 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |


[Clique aqui para ver as próximas entradas](README3.md)
