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
| b7a17927-580a-30b4-bc59-c12b5d9a89e1 | -4.8397 | -45.3926 | 2026-08-28 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 312.3 |
| 434fc22f-1a53-3882-a8fa-5c754605a278 | -12.7797 | -44.2576 | 2026-08-28 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 942c9b94-7bfc-3f78-b250-6fb42dcef2d5 | -13.5991 | -45.772 | 2026-08-28 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0049b073-868a-3e98-b95f-722f83110087 | -7.6029 | -61.3606 | 2026-08-28 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 518557be-2765-33bb-9b17-ed258dde8eac | -10.7596 | -54.0384 | 2026-08-28 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 90605eff-ad09-3ce7-8bd1-ae5117c3044a | -11.6586 | -50.4532 | 2026-08-28 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 12b327ea-1c63-30cd-bbc0-c7047ee2d326 | -6.1656 | -57.7988 | 2026-08-28 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| d4b1a5d0-ca55-370d-aefe-1aff0c74dc3a | -4.8398 | -45.37 | 2026-08-28 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4ab4b751-c145-396a-9835-2aaf5acac9cf | -6.7698 | -55.6844 | 2026-08-28 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ef622dbe-b3e7-32f2-b8e9-787081887094 | -15.5205 | -41.9219 | 2026-08-28 00:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| 1e060a5c-7559-3ba3-970c-3bf622ba79a7 | -13.4552 | -54.0174 | 2026-08-28 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e07079fd-440c-3c94-9f37-f2bb911b6b38 | -7.603 | -61.3415 | 2026-08-28 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8b6d9872-faf7-3bb4-abe5-509fc6450c9f | -6.1472 | -57.7995 | 2026-08-28 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| a534aaaf-224d-318c-aa9f-4b59dc14878b | -9.621 | -55.1266 | 2026-08-28 00:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 33575ed0-62c0-35ea-8ed5-030ef54ee1f8 | -12.43 | -43.4182 | 2026-08-28 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 337.8 |
| 0f8c4435-87fc-32ae-ad0a-f93774cab6b1 | -12.4305 | -43.3944 | 2026-08-28 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 21d4878c-9703-355a-a06f-9c09ddc0535e | -11.6583 | -50.4746 | 2026-08-28 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 07fcc63c-3447-39e5-9b46-35039ed717c8 | -11.2317 | -53.9958 | 2026-08-28 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 6082bd94-8f5f-3e8c-9489-a5d33da4e323 | -12.4498 | -43.3911 | 2026-08-28 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 0ab14c99-d9b5-3c4b-a296-8a83ed6ff2b3 | -12.5187 | -43.8063 | 2026-08-28 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 0773fc53-251a-30a6-af30-f34b8d18bf85 | -6.7513 | -55.6853 | 2026-08-28 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 30eed5ba-a03e-39d0-ab02-7f42feb0f851 | -11.2314 | -54.0164 | 2026-08-28 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0fdae266-f8ad-3a10-aca1-2a04c9b814f7 | -12.4107 | -43.4214 | 2026-08-28 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a353188b-8bd0-3082-9a25-033b8097239a | -4.8395 | -45.4151 | 2026-08-28 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| a759293b-d64b-391f-8aed-7a8910956ece | -11.6396 | -50.4553 | 2026-08-28 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| dc76784c-b727-33b4-b7d3-377fa0be2ee8 | -10.5168 | -64.4997 | 2026-08-28 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c4ef54ff-4db3-38a8-ba92-316e3f84c504 | -12.4994 | -43.8095 | 2026-08-28 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 19ca188a-99cf-3dbb-96e0-96ab6906d7d9 | -7.8828 | -46.1028 | 2026-08-28 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 9a9f51bb-c7e9-3c9b-b591-ae5d8f15673b | -11.2693 | -54.0129 | 2026-08-28 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 018b4987-440b-3ac5-8290-e3e368baad47 | -9.6022 | -55.128 | 2026-08-28 00:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| fa1dd3ab-76c4-3826-8d27-f1405bd09f36 | -4.8582 | -45.414 | 2026-08-28 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 414cf4e2-db8e-3237-a9b5-3efd4c877143 | -11.7354 | -54.5431 | 2026-08-28 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8a47a88d-44d6-31fc-aa8c-c1488a2b51f7 | -11.7165 | -54.5449 | 2026-08-28 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| dc046214-38f8-3e27-9e4a-fe36b3bc74c7 | -15.5403 | -41.9175 | 2026-08-28 00:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| 59e067a0-c9cf-3a0f-81e3-5fe94d6dbf12 | -2.7304 | -47.0424 | 2026-08-28 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fa023233-a957-3580-a73e-d74843168c19 | -12.4112 | -43.3976 | 2026-08-28 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f7413a65-21d8-3854-b772-625c748afc4f | -7.603 | -61.3415 | 2026-08-28 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| abe5aa54-636a-3769-b138-a9a6d2579297 | -8.87 | -66.9121 | 2026-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7b9c2719-8bf0-32c8-a430-28d59a68ca4e | -12.7797 | -44.2576 | 2026-08-28 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| bf31e82b-316b-3a35-aedd-5fedeaa523e2 | -4.8397 | -45.3926 | 2026-08-28 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 229.1 |
| fedc5d1b-d12c-3d6a-9c7b-a98b8edd3a70 | -10.7596 | -54.0384 | 2026-08-28 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 10570867-0bf2-3832-acec-34c6fd0c0d09 | -4.8395 | -45.4151 | 2026-08-28 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 771ce555-a6cb-3010-a6f4-184885f8c937 | -12.4107 | -43.4214 | 2026-08-28 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 111d638f-a95c-3ba0-87f4-158e21b6dd50 | -11.2317 | -53.9958 | 2026-08-28 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 3b7ab2aa-5c70-3aa0-a53a-e1a99c666fb0 | -12.4494 | -43.415 | 2026-08-28 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| b4dadc1d-4219-3848-bb40-c4b141498470 | -12.4994 | -43.8095 | 2026-08-28 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f313ac5e-f55b-33e7-87d1-5fa471f2d428 | -11.6586 | -50.4532 | 2026-08-28 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3d5f8f38-d05f-3922-98cb-e27a9421e3f3 | -4.8398 | -45.37 | 2026-08-28 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 4857cc52-0f6c-3e8c-baa0-acd8dde8ceb4 | -12.4305 | -43.3944 | 2026-08-28 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 254.4 |
| edc4060c-6d9c-38ba-bdcb-07fd55ce79a3 | -4.8582 | -45.414 | 2026-08-28 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 54cf5032-4815-3dd0-aff6-8fb840b6cf74 | -5.906 | -52.1261 | 2026-08-28 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 78aa9317-b854-3119-9d8f-1b25a391085d | -13.5991 | -45.772 | 2026-08-28 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 65cb6776-cfa8-3583-83b0-7c7a0bd575c4 | -20.3458 | -47.5939 | 2026-08-28 00:30:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b95ca8fe-326a-3a95-8f28-557c00453daf | -11.6583 | -50.4746 | 2026-08-28 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6e7c7a87-350d-3e16-8bce-c1e64ec6d6da | -11.7167 | -54.5244 | 2026-08-28 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0c34a203-587d-3d11-9a8d-ea7c9490d823 | -15.5205 | -41.9219 | 2026-08-28 00:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.1 |
| b6a2997e-45bb-373a-8947-2256f251fdd7 | -4.8583 | -45.3915 | 2026-08-28 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 193.6 |
| d8277c1c-2b3e-375e-865c-1baa9b086f39 | -12.5187 | -43.8063 | 2026-08-28 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 931a9aa7-6b5d-3d03-b0e7-7025663b19f6 | -6.7513 | -55.6853 | 2026-08-28 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e7c639ff-7139-3aec-94c6-b99d2586f09b | -11.2314 | -54.0164 | 2026-08-28 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| bd669c88-96a1-3b66-9760-4474f1f26d9d | -10.4981 | -64.5005 | 2026-08-28 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| b95f08ef-7fae-3427-95c1-b00365399843 | -13.4552 | -54.0174 | 2026-08-28 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4d80fbe2-db99-3b6c-abe6-fdd21472f0c6 | -8.9873 | -65.4379 | 2026-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 7edbae8e-1373-3791-8c0f-50ecca19edea | -10.3895 | -61.231 | 2026-08-28 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e79c8f0a-4d8d-393f-892c-3da1639fdcd3 | -10.7975 | -54.0146 | 2026-08-28 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| e391bb42-1c5a-3b36-8fe4-2b7da1c94521 | -6.1657 | -57.7793 | 2026-08-28 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 12491d02-0148-3f18-ab17-04966e626270 | -12.43 | -43.4182 | 2026-08-28 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 286.7 |
| 2c776e87-368b-3d7a-ad17-8254edf3367d | -6.7698 | -55.6844 | 2026-08-28 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2426ce6e-5a96-3887-b547-a61109833940 | -12.7603 | -44.2608 | 2026-08-28 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 181e0b0d-21d5-3d16-9845-243b194a17c2 | -5.9061 | -52.1055 | 2026-08-28 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| b28985eb-53ed-3070-870f-b278fd480919 | -11.7165 | -54.5449 | 2026-08-28 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b027f39a-2c00-31ac-ac1c-6aa81ade312c | -10.3894 | -61.2502 | 2026-08-28 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8e614cec-40b8-3de9-930f-cdeb0e196124 | -6.1472 | -57.7995 | 2026-08-28 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 9a0a3877-2cc2-3b0f-9878-d4b128634c83 | -11.2693 | -54.0129 | 2026-08-28 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 521f069e-1f6c-3213-b27a-f979bfdb0942 | -6.1656 | -57.7988 | 2026-08-28 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| df84211d-51da-3457-a457-259d854ad485 | -12.4498 | -43.3911 | 2026-08-28 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| e33ac2c6-1871-3c78-b6a4-ab3c0f27fcaa | -11.2693 | -54.0129 | 2026-08-28 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f3515d86-517b-3105-b903-7afea4767389 | -11.7357 | -54.5227 | 2026-08-28 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| abf932b2-0613-303b-b221-eabecba83847 | -16.1444 | -58.6073 | 2026-08-28 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| b7e06885-4462-3f0a-bbcc-53bed59798ff | -15.5403 | -41.9175 | 2026-08-28 00:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 8b0b3175-64d7-333f-a93d-80f7f8871374 | -7.2659 | -45.8668 | 2026-08-28 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 733.2 |
| b22b299e-75a3-3311-a2cf-41883ccb808d | -8.6154 | -54.7945 | 2026-08-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3582b6c9-3bab-321d-b51f-b74277ff1ce2 | -11.2317 | -53.9958 | 2026-08-28 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a89438dd-3862-3697-8eb5-2fb6c55df032 | -9.621 | -55.1266 | 2026-08-28 00:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2bcb0aab-885e-3dca-bdbc-93263d7d8328 | -11.7354 | -54.5431 | 2026-08-28 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 90753b76-afbe-370a-b663-0f42c8792bf7 | -7.2471 | -45.8685 | 2026-08-28 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 537.3 |
| 154d7aac-872f-34d7-b436-8b2f619bcee8 | -16.1638 | -58.6053 | 2026-08-28 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| dd28f9bd-16f9-3135-974e-92e69049bbc6 | -4.8395 | -45.4151 | 2026-08-28 00:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0c5764d6-2c15-398c-a25a-d59fc8141702 | -7.2469 | -45.891 | 2026-08-28 00:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2d5f4104-713a-3d4c-bef0-1e22eff0bfbc | -12.7603 | -44.2608 | 2026-08-28 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d490ab27-9362-3059-ad92-ebe9906e0646 | -14.8627 | -52.6106 | 2026-08-28 00:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 48cf73ba-8aa5-3228-9b24-673d16be0cb0 | -10.3894 | -61.2502 | 2026-08-28 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 98dfdd5d-5273-3b38-8b06-498afe2360d5 | -7.2661 | -45.8443 | 2026-08-28 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 460.0 |
| e2dc1eaf-4cd9-3230-9c7a-98e3bb63b678 | -8.6156 | -54.7743 | 2026-08-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 688b6199-f964-3b70-9fc3-6dbe3a441176 | -4.8582 | -45.414 | 2026-08-28 00:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c00f7fda-44a7-3c80-b364-d1cb0f597589 | -8.5781 | -54.797 | 2026-08-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e4ce21c3-8225-381a-873e-1cbb3002c8a7 | -11.6583 | -50.4746 | 2026-08-28 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 616a75f5-14aa-34cc-afc3-a440fcd5cfa9 | -12.7797 | -44.2576 | 2026-08-28 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| bba81280-f4a3-3ac9-963b-9614fbe6ff6b | -10.5168 | -64.4997 | 2026-08-28 00:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e82b7290-2697-31ab-99a2-1c607d545c8f | -12.43 | -43.4182 | 2026-08-28 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 328.7 |


[Clique aqui para ver as próximas entradas](README3.md)
