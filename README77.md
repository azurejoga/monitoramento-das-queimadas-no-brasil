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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8faf07d-26cc-3201-ada1-e5362c30e809 | -10.7871 | -45.3203 | 2026-08-30 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 34a9b24f-e747-3ab0-9b31-d66325f40e38 | -12.9221 | -45.8582 | 2026-08-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 86f0506e-0a80-3294-a490-64934c44aae8 | -7.6152 | -44.8605 | 2026-08-30 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e332f65e-21c7-3186-b847-265458e80667 | -4.9604 | -55.8424 | 2026-08-30 12:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| d4ef6e00-49cd-388b-815c-d2011d12ca3e | -12.9409 | -45.8781 | 2026-08-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f037d2fd-dd33-3711-8fd6-4db26b973957 | -14.1649 | -52.8058 | 2026-08-30 12:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8010aaa3-9d0b-37f6-8549-2d15fa8284e7 | -12.9212 | -45.9041 | 2026-08-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 77b0a54a-1822-35ff-af76-09c2ffb36325 | -11.8211 | -51.0322 | 2026-08-30 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 57d57717-9716-3a5f-89e6-b0797a12a8fd | -6.8752 | -59.4749 | 2026-08-30 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c57d101a-4fcf-3979-8067-b6b4d5e46699 | -4.9604 | -55.8424 | 2026-08-30 12:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9a83126e-dae1-3f44-97e0-56e1e4054ee8 | -12.9212 | -45.9041 | 2026-08-30 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 0e918c51-a3ab-30a8-ae7e-ad92cbe7e557 | -7.5136 | -55.3251 | 2026-08-30 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 4f03128c-c57b-3fd3-b1e4-76b52437781f | -6.8752 | -59.4749 | 2026-08-30 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 71e0890c-0abe-37f8-b49e-931a46442ea1 | -12.9405 | -45.9011 | 2026-08-30 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1d37a1cf-efb7-3658-a29d-0b632ce99b40 | -7.9422 | -44.277 | 2026-08-30 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 348.1 |
| 12e892a3-1a94-3643-9897-f5c08cd0ba72 | -14.4197 | -52.5413 | 2026-08-30 12:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d5b99b42-b927-3b3d-9e36-6200019967c7 | -12.9409 | -45.8781 | 2026-08-30 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5dc9a567-89be-3f52-8a7e-bde41e5b4df5 | -11.8211 | -51.0322 | 2026-08-30 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 71b05c68-0d89-3fc2-b83b-0bba9481c709 | -7.5321 | -55.3241 | 2026-08-30 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1792ac7e-9558-32c3-87ed-c7d68c726ef8 | -14.5445 | -52.0156 | 2026-08-30 12:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5ab20300-135f-3ffa-8ac0-c9d8995ae7df | -10.8253 | -45.3152 | 2026-08-30 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7e962d9f-38a1-3f4e-817a-471afd4a306b | -12.9216 | -45.8812 | 2026-08-30 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c2132c6b-fb7b-3b5f-9fe6-41e4c670cd1f | -11.5475 | -45.4906 | 2026-08-30 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 6611b773-d1da-3fa6-bc15-840ad165b3db | -7.9425 | -44.2538 | 2026-08-30 12:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b1a7495e-1f42-3db0-b694-eb903a0462b4 | -14.1649 | -52.8058 | 2026-08-30 12:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2e856caf-c72e-3bcf-ab26-e5b7113dcb41 | -10.1538 | -45.6982 | 2026-08-30 12:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 3b45666d-33e8-3d97-8f72-5eff9b16930b | -7.9611 | -44.275 | 2026-08-30 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 496.8 |
| 3dbb335b-c3a9-396e-b34f-61de1a887148 | -14.1456 | -52.8082 | 2026-08-30 12:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 3d4d9c25-d810-3420-a4cc-5880f74b3047 | -7.6152 | -44.8605 | 2026-08-30 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 67380ac4-b84e-3a6e-b6e8-11eaf35597b0 | -10.7871 | -45.3203 | 2026-08-30 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7c9d14a7-df5c-380b-94f3-9ad6661ce9f9 | -7.95 | -44.31 | 2026-08-30 12:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4e9eed5e-0e79-398e-85e6-d5f22f3b2027 | -7.95 | -44.27 | 2026-08-30 12:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 25e269e0-cb96-344b-8dbd-5657bf19fb1d | -14.1456 | -52.8082 | 2026-08-30 12:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| d681eaac-32a1-3fcd-8a9b-1ea0cc8fbd89 | -7.9425 | -44.2538 | 2026-08-30 12:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 929deeef-1296-3d9e-b338-6fa94c607a28 | -12.9409 | -45.8781 | 2026-08-30 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 20ee7bfb-c1ad-3083-847c-e8c04c651cfb | -7.5321 | -55.3241 | 2026-08-30 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 50914e89-4289-33db-b2e0-5be8d5d1b349 | -12.9216 | -45.8812 | 2026-08-30 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| dd0f9686-216a-36fe-9df2-1d61aa81cf9d | -10.7871 | -45.3203 | 2026-08-30 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b266b643-ecc2-333a-8fac-2707e37d51a2 | -7.5136 | -55.3251 | 2026-08-30 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| bd9f0f0d-60cc-3eae-96ca-bf04812f44ec | -6.8752 | -59.4749 | 2026-08-30 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 588295e1-6430-37d7-b9aa-f72edf650c07 | -7.6152 | -44.8605 | 2026-08-30 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 6221523c-f1e1-38be-9812-378d5d9c3f22 | -7.9422 | -44.277 | 2026-08-30 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 1fcf6bd2-6ad9-3fa2-bedc-3049176314b1 | -12.9405 | -45.9011 | 2026-08-30 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 95bc9189-865b-3f6c-91ab-9e8134b2ead8 | -7.9611 | -44.275 | 2026-08-30 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 0009b566-1413-3b77-8b5f-d779098ffb03 | -12.9212 | -45.9041 | 2026-08-30 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 336.7 |
| 51b8c37a-0591-3c97-96e0-0dda09ba1dcb | -14.4197 | -52.5413 | 2026-08-30 12:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 2642b3a0-464e-33c7-b561-0e7e6814e88b | -12.9221 | -45.8582 | 2026-08-30 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| b1a10174-c0db-3b64-b1be-b512c7dd857e | -4.9603 | -55.8622 | 2026-08-30 12:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 462db9d1-b16f-344e-adfb-09c4a800c2cc | -10.1538 | -45.6982 | 2026-08-30 12:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| d244b894-12d4-3442-a4a8-993db0ed4fc5 | -11.5475 | -45.4906 | 2026-08-30 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 3344a8c3-ea6f-3b76-b744-0f7b018525c8 | -12.3619 | -48.1903 | 2026-08-30 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c89d62ee-13e5-33cb-afb8-23b1d31119fc | -4.9604 | -55.8424 | 2026-08-30 12:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 226c8ace-eb68-3cfc-a97b-9926a3312046 | -7.9611 | -44.275 | 2026-08-30 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| a29d3e80-e9eb-3e52-82cb-bbfb9c20099f | -7.9422 | -44.277 | 2026-08-30 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 1f808eec-8c38-3800-a633-e5d85fdc51fe | -4.9603 | -55.8622 | 2026-08-30 12:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 771de081-df7b-365d-ac94-de490bf8e070 | -7.6152 | -44.8605 | 2026-08-30 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 299.0 |
| 5ef43386-5486-3aa2-89da-d1f20556f6fa | -7.5136 | -55.3251 | 2026-08-30 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 87fbf314-2c0a-3533-a494-bb81cbb8d307 | -10.7871 | -45.3203 | 2026-08-30 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 23b52b3e-92d3-3faa-99ce-3db57502fb17 | -10.1538 | -45.6982 | 2026-08-30 12:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 34e7d8b7-2071-3bc8-b6e5-144840d053cd | -4.9604 | -55.8424 | 2026-08-30 12:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| be40b7d5-3bec-3865-98dd-94b25582a837 | -14.1456 | -52.8082 | 2026-08-30 12:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 147.9 |
| f9c28c25-0b89-330a-940b-7329c27a95de | -7.9425 | -44.2538 | 2026-08-30 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 6498c4d5-704e-38fb-8c29-088dea2040f0 | -14.4197 | -52.5413 | 2026-08-30 12:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 8298acdd-600f-3147-81ec-1dc956ca4377 | -6.0 | -45.0889 | 2026-08-30 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ffe9618c-090c-3039-b661-505fb040d28c | -6.8752 | -59.4749 | 2026-08-30 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 3e16bac5-aed0-3dba-95bc-bb3edfdb95e2 | -12.9216 | -45.8812 | 2026-08-30 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 992306cc-ec3f-3eb6-a501-55e8943246cc | -6.8568 | -59.4757 | 2026-08-30 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| f722bf3b-9ffb-39a2-9ee5-612df4f82594 | -10.1348 | -45.7006 | 2026-08-30 12:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| c615b943-26d1-37e6-b35f-1226361ba7bf | -12.9221 | -45.8582 | 2026-08-30 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 79be4e4f-d57e-3fde-bd5c-a6c6c02535fc | -14.1456 | -52.8082 | 2026-08-30 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 780c2805-bd09-3c3d-8793-5e74281a8460 | -10.8249 | -45.3382 | 2026-08-30 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1c05ad68-65eb-38a9-9713-2f9446ba0426 | -10.8253 | -45.3152 | 2026-08-30 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| cdbe1ca3-d512-37a7-9eb1-f270d22a2416 | -7.5136 | -55.3251 | 2026-08-30 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 219.9 |
| f6988415-edc5-3ebc-bea2-833d640c799d | -11.1634 | -50.5727 | 2026-08-30 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| eca144c7-693c-3fa7-bfd0-3ff0102611df | -7.9422 | -44.277 | 2026-08-30 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 11de5e28-2099-3949-bff8-8d8e6318cad2 | -7.9425 | -44.2538 | 2026-08-30 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 62ec1212-ecc0-36d8-b617-0c9663750304 | -6.8569 | -59.4564 | 2026-08-30 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 71aaf742-c7f0-3354-b0e8-b2bf08609336 | -14.1649 | -52.8058 | 2026-08-30 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 075a1955-f8b8-3564-97fe-2db24f018368 | -7.5137 | -55.3051 | 2026-08-30 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 3063b5db-9096-3d1e-81d4-9f3444c72548 | -4.9603 | -55.8622 | 2026-08-30 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| f5daa0aa-e308-3d2a-946b-ca91287da328 | -7.5323 | -55.3041 | 2026-08-30 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7b62a2ff-43ef-3200-a10d-496393e5da54 | -7.5134 | -55.3452 | 2026-08-30 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7569f963-ba5e-3262-b6ae-c79d79b002c1 | -6.0 | -45.0889 | 2026-08-30 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f744eab2-331f-3f48-b832-d5d1c9b91a28 | -12.3619 | -48.1903 | 2026-08-30 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d116af78-c131-396f-9156-7d372fdae2a8 | -12.9221 | -45.8582 | 2026-08-30 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 4edba28a-1207-3650-8eed-04bde9f6f023 | -6.8568 | -59.4757 | 2026-08-30 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 03b07a35-2057-313c-98d5-b8b1ab0ba229 | -6.8752 | -59.4749 | 2026-08-30 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| a1e1db16-c814-30f1-a583-62bfdfae3fa5 | -10.1538 | -45.6982 | 2026-08-30 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e27ece37-722c-37e9-a291-1a1050b051f2 | -12.9216 | -45.8812 | 2026-08-30 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| ba3a62ac-a0b2-3692-bd8b-49978b0cee1b | -14.4004 | -52.5438 | 2026-08-30 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 70a7edbd-fecc-3cc2-8657-156ac7c8d699 | -7.6152 | -44.8605 | 2026-08-30 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 210.5 |
| e7d7d683-f404-3710-9e64-626d62d72879 | -7.9611 | -44.275 | 2026-08-30 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 3f5d93e5-8fca-3cc3-9128-77f3eaec056a | -14.4197 | -52.5413 | 2026-08-30 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 03baf84e-b9e0-36f7-9c5a-16bd10091a0a | -4.9604 | -55.8424 | 2026-08-30 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 7912205b-d19e-3b25-82a9-1c1660794284 | -4.9603 | -55.8622 | 2026-08-30 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1c749fa7-d2c6-3ca3-bf0b-d318717388de | -14.4004 | -52.5438 | 2026-08-30 12:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| cf6cc34f-7207-3cfb-8299-d5f076e747db | -11.2829 | -45.3214 | 2026-08-30 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f3ebbbbd-e399-3f88-a612-4eff8fee3478 | -6.8752 | -59.4749 | 2026-08-30 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.0 |
| a6d8196b-8f21-3c96-bf7b-f4e0d507bf82 | -12.9216 | -45.8812 | 2026-08-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 39bffb23-8255-37dd-9313-8a7032ac1520 | -11.1726 | -51.2728 | 2026-08-30 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |


[Clique aqui para ver as próximas entradas](README78.md)
