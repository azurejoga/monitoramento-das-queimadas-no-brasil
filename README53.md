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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 959a23f6-cc02-3dbb-9141-af2aeb0a06ac | -13.44926 | -48.49477 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 831890e8-9b78-3695-84e6-284e1413eecd | -9.70926 | -54.36241 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff795839-b238-3ca8-be9b-bcf684a80d5b | -10.96407 | -58.95861 | 2026-09-13 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a75aee6a-8957-3185-b53a-81514b82735f | -12.49256 | -48.04176 | 2026-09-13 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d211eb22-95ad-31eb-ab19-7ad1b665bbba | -13.3479 | -51.80106 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2efa10d-f448-3e1c-a4dd-8fa3569c49fc | -13.38748 | -48.00924 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdd84464-9f8a-3bd5-a013-ee4a1065f711 | -10.5347 | -51.29909 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df4d92c2-437d-33c2-80d6-d9e58b568de3 | -10.54021 | -51.38182 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09375b5f-6842-32e4-897a-9c3020039e4d | -10.68588 | -54.16648 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 22564195-ecdf-3e04-9f79-2e563d030456 | -10.58621 | -51.35728 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 555ea35e-6b8f-3a56-91ef-8136b6188e11 | -10.51669 | -57.45372 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39536b79-9083-393c-94e9-880b4f7b3b04 | -9.1841 | -59.45018 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29f9d94f-7a0f-37de-8643-c3eb7ab06ba7 | -10.50426 | -51.30317 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42a31712-48b8-3137-9dff-26582cdc3fda | -13.60507 | -47.88024 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abf063d7-12c5-30bb-be7c-b9043facf1ca | -10.89591 | -47.80243 | 2026-09-13 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e2843f7-2271-39a0-b97d-d0a8af10e003 | -10.93736 | -48.35492 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| febdc71b-ddb6-340f-a74e-2bc510c8af03 | -13.39328 | -48.00703 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4dfca8a-81a8-3189-90d6-5299566dd8f9 | -10.93622 | -47.9099 | 2026-09-13 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f2486dc-4a6a-3a9e-b5cb-5695a4333c9d | -13.78054 | -48.79918 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fd93abef-fdd2-3524-93d1-54a0fce265ab | -10.9467 | -57.18554 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81ac2f8f-4c5e-3b66-9de7-6c9a0e82c99d | -13.44925 | -48.50104 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5df33412-a17d-3322-a20e-b82c963fb157 | -11.82501 | -46.39606 | 2026-09-13 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44f7a103-b2ee-338f-a407-16c2711f3e40 | -9.18053 | -59.62574 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03f49709-43a8-3dd5-b5f1-a1d20306d943 | -11.24763 | -54.15358 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4b37cbb-96ce-32df-ac88-5d1ead9cda6a | -8.8585 | -62.52145 | 2026-09-13 05:12:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26fe048c-273e-33c1-b93b-f10c8291d559 | -10.9601 | -58.962 | 2026-09-13 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e553aa9-c07f-3f8d-97f4-fdf0c08d9f24 | -9.89891 | -47.59391 | 2026-09-13 05:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 276dc7d2-fc6b-328c-80be-b5c92eab8f02 | -13.34422 | -51.79642 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 821e5195-a825-340c-b42c-62cb07bba06e | -10.41441 | -54.36422 | 2026-09-13 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0af2eea-9811-305f-8d14-9e53f165f3e1 | -10.45568 | -48.65195 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e267481b-037a-3bd8-b74d-00441950b47a | -13.44853 | -48.50093 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e544d6e-9ac8-32ca-b35e-cc069ef90c69 | -10.30301 | -45.27815 | 2026-09-13 05:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f38feae7-d9b4-3530-8cb7-83de3fad0270 | -10.30937 | -45.27797 | 2026-09-13 05:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b863392e-e8df-3e2b-b7d1-d5aa1ebe60b8 | -8.81718 | -61.40863 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c2b6e7a-196d-3ecf-8f37-fe7b6c2dcd6e | -9.3847 | -56.98985 | 2026-09-13 05:12:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e282246-5738-3f63-962e-032d9c909c9b | -10.62292 | -46.11023 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 147122ac-7919-3da2-a40c-69be7f28b81b | -9.71913 | -54.36781 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2971f071-2a6a-3592-9c80-fa3c8bfaeded | -9.57103 | -60.6331 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cca5cbe3-70ca-3a34-9f67-43ba085dc2c7 | -13.45607 | -48.48943 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77622783-2f74-3d01-bce0-5caca80318f5 | -10.72874 | -54.00145 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1abcfb17-4166-35e2-a764-854cb47ea6cc | -14.10913 | -46.35563 | 2026-09-13 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 453975ee-7b8c-3536-8b18-962ecde46ff7 | -10.69418 | -54.15945 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eca27ee-970a-3ed7-93a6-df2da525d8da | -13.98849 | -54.07087 | 2026-09-13 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff4ef75b-7bed-3b93-9730-4eeffedc2488 | -9.55529 | -51.36579 | 2026-09-13 05:12:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dd50fcb-6918-3ded-a027-6917d2003341 | -9.57673 | -55.15771 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1218481a-501a-3edf-b660-75dbebe63ba4 | -13.79109 | -48.79918 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58284947-9d35-3d59-8426-380c1fdb1308 | -10.50316 | -51.30397 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1b3e080-e298-3810-a780-f6d26fc73191 | -15.04427 | -48.53243 | 2026-09-13 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb8e8401-6b5f-344c-bc42-a26db1c965b7 | -15.047 | -48.53371 | 2026-09-13 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f02204ca-1af7-35f5-b4c7-63b1799d71e9 | -13.79072 | -48.80226 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bd619c3-1768-3e50-ae31-261ed7395470 | -10.94284 | -57.1885 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0323bc0a-aca0-3bea-86f5-bc7cd48726a3 | -9.894 | -47.58992 | 2026-09-13 05:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 843e1b93-db02-3f03-9972-89ee97b1024a | -10.35865 | -46.66928 | 2026-09-13 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecb47c33-a479-319e-97a5-f38cf90c2f23 | -8.86704 | -62.52296 | 2026-09-13 05:12:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 15cb78c4-5a33-30f7-a13b-1f46cda69326 | -13.46093 | -48.48679 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4330d22d-4ce4-3aab-bf03-01cf33d92cb2 | -10.75817 | -46.24627 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3722c484-7d97-3ab2-bcb0-39b1732f64c9 | -10.21801 | -45.19388 | 2026-09-13 05:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 783b6eef-7269-3c61-addc-2eab4f68f6dc | -13.60461 | -47.88404 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6400a81-80d0-3b50-a96a-db3d762c2d4c | -13.46586 | -48.49048 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dfc16cc-df3e-3e23-8bda-5b5effc012a8 | -9.18342 | -59.45423 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2ad90e58-2f8f-3614-a896-2b29172c2851 | -10.30867 | -45.28352 | 2026-09-13 05:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a853d455-0abc-3173-b059-cc04982e77ef | -12.13777 | -57.1924 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef665fed-8a48-3ee7-96b2-6955f2dd7bdd | -10.51725 | -57.4502 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d75dff44-a065-3adb-bde8-0eed3ce7cc6b | -13.61095 | -47.87791 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c743996-3cd3-38cf-8eb2-5ace3155d3ed | -10.53413 | -51.30318 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a03b0fe4-c264-3e0b-a19c-38027cd61383 | -13.38891 | -48.00975 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98932f0c-23d9-32d2-bbb6-c93bc9f37084 | -13.40554 | -57.03189 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74dc2453-746c-3b87-af4d-259f0b0c7c8b | -13.4537 | -48.50826 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93ffdb74-4525-3fef-ae43-8bcbbe40062a | -9.88332 | -47.58845 | 2026-09-13 05:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92ac6109-5850-3df2-a151-5842595bd4a8 | -13.98784 | -54.07532 | 2026-09-13 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 579a3009-538e-380a-b7d9-6c8eb84bbc1c | -10.3075 | -45.2929 | 2026-09-13 05:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc35a4b0-8e21-3536-a44d-7599e81116f5 | -10.56739 | -51.36992 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64ee2950-e986-3d97-9a93-f85afc77f303 | -9.17627 | -59.62927 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40146ef1-305e-31ad-b52f-a5048ed16346 | -13.44966 | -48.49136 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9722b773-7a5f-3b33-a3c9-7a46422dd9c6 | -13.45691 | -48.4828 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| da5d97c9-412d-392c-a04a-663e0d3a7c07 | -10.28796 | -55.06509 | 2026-09-13 05:12:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc0d08fa-cb58-3f94-9129-88e0c7095a6f | -11.81911 | -46.39507 | 2026-09-13 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9cdb488-40c4-3184-9e00-e86d210ece31 | -9.46181 | -59.19648 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d480f82-2748-39a9-a89d-15d4a8f91634 | -10.69713 | -54.16403 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d6d8972-be91-3503-bf1e-fb3b2109257d | -9.55582 | -51.36205 | 2026-09-13 05:12:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bc78732-a6a2-393f-9988-1952e64d09fc | -11.24406 | -54.15305 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a175371-815f-3d7c-9d53-3f6e913d4410 | -10.30699 | -45.29698 | 2026-09-13 05:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71c73ba4-e89c-3a9d-b225-214097b3f6ff | -10.69063 | -54.15892 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ee06ba7a-2f39-3533-9d57-5942c12ec72a | -14.95852 | -47.52614 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b19ddc5-d8ed-3257-878c-5fe4cf4d1d5e | -9.71215 | -54.36681 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfece3c3-2dd7-3cac-a6ef-287c7bf7b94f | -13.46133 | -48.48349 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c284b34-a42b-3ca5-970a-c13548924418 | -13.44817 | -48.50394 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a81e4a6c-5fa0-39f9-8cc1-fd62375d25ef | -10.56997 | -51.35168 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e68ce92-b260-3a1a-9ce4-c0fec184effe | -10.57625 | -51.36742 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd1f2f0d-3fb7-3f20-aa75-1cf45ee5990c | -10.57471 | -51.34829 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b2c4a21-0d95-3c33-9bd4-fc6f272c5a02 | -12.85511 | -44.39019 | 2026-09-13 05:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92ac1843-0d78-3388-84c9-ce7a476b0218 | -10.50186 | -53.5701 | 2026-09-13 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a66522ad-7de3-3946-ac08-48660aca9cd2 | -10.68467 | -54.17455 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 387719f5-cda3-314f-b593-83176da3b18c | -10.47105 | -48.65145 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d81d816-7dac-30b6-b06b-2766547cf2f5 | -10.35568 | -46.67709 | 2026-09-13 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e7bb378-3f0e-3e81-93d5-2cbfa77ce348 | -13.61597 | -47.88488 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a61b33d-5a76-3df9-b9ff-767bf88e294b | -10.53829 | -51.30399 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aad6e2af-b831-3199-9453-91d87ec9848d | -10.94395 | -57.1815 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8256e2bc-cdb8-3ddb-add3-bd1aa1f11e6a | -13.6167 | -47.87856 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cc85180a-5097-3ca2-8d41-d64d7be5cf4e | -13.3459 | -51.78197 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
