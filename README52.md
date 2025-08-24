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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db178a1b-daca-3e83-a3cf-3e49c0a56363 | -3.24959 | -46.90687 | 2025-08-24 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 606b1447-6cfb-34fa-9e7e-b4d7535f281a | -2.93242 | -53.69762 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dcc54cf-702d-3177-9d02-9b34637986a2 | -1.55585 | -54.54075 | 2025-08-24 04:57:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33821ef4-3c94-3b50-b8fb-1729b4908cb5 | -2.63259 | -58.10973 | 2025-08-24 04:57:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bda558a3-5adb-3c1d-8957-7a219f9873de | -3.43823 | -49.04332 | 2025-08-24 04:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3dfbd6cb-7c79-3d81-826a-034258e3acfa | -4.48473 | -47.66619 | 2025-08-24 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6aefb499-2077-3e59-9e9a-5b37d7d71c15 | -3.73496 | -48.92976 | 2025-08-24 04:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fa28f81-31da-30ca-ac7b-7b98af74193c | -2.93296 | -53.69416 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6918d197-485e-3ad2-af27-3fd3f0ebeda8 | -4.09429 | -48.74685 | 2025-08-24 04:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df8a16e1-56e9-3c0b-b77d-cb515a843ef7 | -3.66295 | -54.75756 | 2025-08-24 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1728f88d-afa6-3a8b-8559-dd4ff5796f53 | -3.44136 | -49.04875 | 2025-08-24 04:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 315bba96-e758-3f78-96f8-9257ab3cbd5e | -4.56002 | -43.22388 | 2025-08-24 04:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0540745-2056-31f5-8a26-483dc4f8e899 | -1.55982 | -54.53768 | 2025-08-24 04:57:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db154a9f-3d92-36cf-96f3-5f9f9e31fb4c | -3.51486 | -47.20412 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63d828b6-11d7-3c9a-b7fc-55745caa473e | -2.25741 | -47.85017 | 2025-08-24 04:57:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d72988b5-3a89-3767-9136-d57be6418a12 | -3.79071 | -47.5652 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e999371a-296e-32e0-b449-1dba43c0a6d7 | -4.78336 | -45.32791 | 2025-08-24 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d8c2d5a-9c63-35c0-b5e6-3d11039be5a4 | -3.45247 | -44.1386 | 2025-08-24 04:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2def193-26e2-3651-b6ae-1129431a6db5 | -5.40778 | -44.98909 | 2025-08-24 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a938c6b4-a6f2-3ca3-a205-c9fa11dcae4b | -3.13052 | -58.04239 | 2025-08-24 04:57:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16c3c7dd-5bd2-3423-8bde-0acc6014fb6b | -3.60142 | -47.52614 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ba3c3679-ec03-3bf2-a60d-a9d1431930e2 | -4.7838 | -45.32484 | 2025-08-24 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 687e541b-27f5-367c-9bdb-800e115a3f5f | -2.70866 | -48.20903 | 2025-08-24 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8adf8f2-0be7-32b0-8ef6-9c04584626f2 | -4.29801 | -48.07739 | 2025-08-24 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c70781d8-b05f-30c9-a7ec-cfa05da28c5d | -5.58468 | -43.24961 | 2025-08-24 04:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bd45f53-8075-3bf7-8232-11b3d5df03c9 | -3.79204 | -47.57223 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96ca104e-752a-3880-bde1-f6301814a750 | -2.91354 | -48.30531 | 2025-08-24 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e486e8a3-011a-304c-9da7-94f5dd6afd97 | -2.95188 | -48.05886 | 2025-08-24 04:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88363dfd-f474-31a1-8bfd-8836bbe6fdf4 | -3.59517 | -47.52249 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f70b2554-2c61-3e4c-8265-4949c495d3b8 | -3.85126 | -49.29092 | 2025-08-24 04:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e78770da-26df-3227-aaf4-a0f0716a3a28 | -3.78579 | -47.56866 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 020b8d8e-657c-3a24-9d53-0ef40ba42ec2 | -3.59225 | -47.52877 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 94c9a2ac-e9bc-3539-8814-c542ebceaeda | -3.65957 | -54.75704 | 2025-08-24 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2441e36e-ed6d-3b15-812e-90ca41be9bc5 | -2.26565 | -47.85147 | 2025-08-24 04:57:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce997bcf-01e3-323f-a6ae-d15d7b95e3ef | -2.98796 | -49.30524 | 2025-08-24 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f842bf4-812a-38b8-9905-7761eb079c3c | -3.83903 | -55.96943 | 2025-08-24 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d629c821-0f72-34b8-b563-5283118ec37b | -4.47981 | -47.66959 | 2025-08-24 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2624910d-025b-366e-836b-ff998ba34e98 | -3.59284 | -47.52479 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dd2e1e91-a6fc-31b9-9625-cff5eaa627ca | -3.13679 | -58.04185 | 2025-08-24 04:57:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c914c34c-ac39-336d-8a26-4d9c33d6021e | -3.59773 | -47.52144 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cac496c2-8001-3fd4-a223-d240915717e1 | -2.25686 | -47.85384 | 2025-08-24 04:57:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7664dd61-4e9d-34a6-8f47-a08cb873446e | -2.71271 | -54.95444 | 2025-08-24 04:57:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 333ef47a-8be6-33f2-8b38-18cc8f7a9322 | -3.59655 | -47.52942 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d8a5c8b7-aee6-3741-bef4-70cf4e284624 | -3.13282 | -58.04121 | 2025-08-24 04:57:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 316aac0e-2a2a-3610-9d61-dc12ecf6f0a9 | -2.92522 | -53.70004 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4eb35811-d625-31c0-9bff-03cb4e358c8a | -4.22542 | -47.21147 | 2025-08-24 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 222b6bb6-70cc-3297-a7c0-d8cec48703b2 | -2.91703 | -48.30941 | 2025-08-24 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c5a6d5a-70f4-3190-a72f-ff44e50396f8 | -2.78816 | -41.88267 | 2025-08-24 04:57:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09addb14-10dd-3885-bd78-b57491aede77 | -4.31188 | -48.0989 | 2025-08-24 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3b699b7-0f5d-377e-817d-8add1d3ad19a | -3.38683 | -47.61082 | 2025-08-24 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09143caf-b2a5-343c-8488-79b459422f22 | -3.63421 | -54.4335 | 2025-08-24 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4905e8d-8127-309f-97e9-340a6ffdc12d | -3.13533 | -58.03793 | 2025-08-24 04:57:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d37a097-baf8-3c86-9b9c-344742ba1705 | -4.01795 | -49.50728 | 2025-08-24 04:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae2aef28-2beb-323c-8196-4add1f444ec2 | -2.928 | -53.70402 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 277a57ae-cd3a-3c79-81ad-f71c464dd3d9 | -2.58184 | -51.91144 | 2025-08-24 04:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fafe5fe6-2b1d-317a-9e68-6e41aafa18ba | -2.62858 | -58.10907 | 2025-08-24 04:57:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc9b9e13-0b08-3b29-ab41-fcb765c1ca4a | -5.40825 | -44.98583 | 2025-08-24 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abfb904e-5d6f-3a25-ae98-80d03ef0d172 | -2.98937 | -49.30342 | 2025-08-24 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ab84951-3d6d-3fd8-ab45-3cedd70c2087 | -5.5853 | -43.24529 | 2025-08-24 04:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 743ce68d-b1a6-3c05-93aa-3193f05fe9e7 | -2.92855 | -53.70056 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 425d824f-d1e4-3c90-96c1-bc430c720d81 | -2.71271 | -48.20967 | 2025-08-24 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13aac469-05cc-3467-86bd-6127ccbad3c0 | -3.44707 | -44.13768 | 2025-08-24 04:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74524159-324a-3acf-8b3d-829863e143ae | -2.7093 | -54.9539 | 2025-08-24 04:57:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a5407867-dfd9-32e9-a30b-781901b92595 | -2.92577 | -53.69658 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 049d367f-7991-33d8-9c6b-8c2e1cd24857 | -3.79009 | -47.56924 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82b8951a-33c9-3dce-841a-e6aebce7af30 | -3.43748 | -49.04816 | 2025-08-24 04:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9402a980-ea05-361c-bd5f-4950479934c4 | -2.29151 | -48.5744 | 2025-08-24 04:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48a4e876-9c6b-3964-abf2-32c61a36b3c8 | -3.40266 | -46.90515 | 2025-08-24 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27ee4eb8-8387-3c7c-8110-11a1718fff6b | -2.62803 | -58.11249 | 2025-08-24 04:57:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34781d31-b531-327d-a71c-739f40d2a8fe | -3.59455 | -47.52647 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ee0c6535-791c-3ad9-9a32-2412b6d2cec7 | -2.79437 | -41.88361 | 2025-08-24 04:57:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80ab8208-bb14-3983-86c5-95deba63f604 | -3.78641 | -47.56461 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61c2cd16-8eba-3ab6-a567-8ef6cb952fa2 | -4.3077 | -48.09829 | 2025-08-24 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa334660-a068-3562-8739-dd2f8658ebd9 | -4.48411 | -47.67029 | 2025-08-24 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 518009b4-55dd-3159-b62c-ff67f8a8bc33 | -4.78847 | -45.32858 | 2025-08-24 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34bee6f8-0c46-3372-8d2f-98b709abc4c1 | -2.58746 | -51.91962 | 2025-08-24 04:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82588d7e-f4cd-398f-b7e9-cdec3f31a1b3 | -3.83966 | -55.96553 | 2025-08-24 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcc59c16-1af4-3ba6-b680-5c2f89af0c28 | -3.12885 | -58.04058 | 2025-08-24 04:57:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83f2a9fd-eef0-32cd-9a07-0ffb74f35794 | -3.79264 | -47.56817 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d95df418-4592-3d08-976b-f09a54ad9fa7 | -3.59025 | -47.52585 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 799017ba-222d-380e-9dc8-25bc1157a688 | -3.78947 | -47.57331 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b2960fd-35a6-3372-87e2-e54f40515d76 | -2.58846 | -51.91932 | 2025-08-24 04:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa637e0b-6b6c-389b-ad97-1e775aab89fd | -4.55419 | -43.22292 | 2025-08-24 04:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d382d5b-93f9-31e7-8ae9-a3ead9c97b77 | -3.9003 | -54.69297 | 2025-08-24 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 373df872-d8cc-3489-8c54-5484f7de606f | -3.90087 | -54.68942 | 2025-08-24 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99f5c477-c834-3f1f-8197-9fdeb75d05dc | -3.69943 | -49.5461 | 2025-08-24 04:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5ac24a0-dd96-3565-a491-c165a4e847a4 | -4.09828 | -48.74749 | 2025-08-24 04:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61340708-22c3-324b-8cb9-55d365419d1d | -3.1393 | -58.03856 | 2025-08-24 04:57:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 777dc378-ad38-350d-8d25-be62cfdaded2 | -2.04811 | -52.52614 | 2025-08-24 04:57:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8b2ea46-6432-3d67-89c6-97dba184e0d0 | -4.92851 | -47.54438 | 2025-08-24 04:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60286dc3-8c1f-3631-a06a-eea26a74cc6d | -2.92909 | -53.6971 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8318a0a7-c244-3f16-90df-c09458032dad | -2.92964 | -53.69365 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad720b25-b774-3617-8331-3153c995320c | -3.59713 | -47.52544 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7ab61813-31c6-365f-b220-47e9808de3a1 | -3.73422 | -48.93465 | 2025-08-24 04:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58dd40d9-a501-38eb-95a1-b69576bc8d6d | -4.584 | -48.0359 | 2025-08-24 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52ee05e4-2d0f-30de-9044-c14e42698ec2 | -4.48042 | -47.66549 | 2025-08-24 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30a8a4b3-c649-3014-8f41-a4823eb46366 | -3.51421 | -47.2083 | 2025-08-24 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 546b45f0-3608-38ac-994d-bed150d4b86f | -2.58521 | -51.91196 | 2025-08-24 04:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 231749be-f93e-3507-97ec-61fa658df6ee | -2.91409 | -48.30177 | 2025-08-24 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb98c6e2-ee76-34b0-b6cd-65f4fc344c4b | -2.91813 | -48.30241 | 2025-08-24 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)
