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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af639120-c65e-3a0e-b715-24eac7211a1c | -9.1256 | -67.8507 | 2026-09-06 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 5dd33536-cd90-362c-b96c-cbfc1386947b | -10.6826 | -45.9041 | 2026-09-06 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| dd30a6ca-adef-3b41-8dcc-12329acff76e | -9.1442 | -67.8317 | 2026-09-06 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 8f13a6a1-f56d-3a5a-892a-99b58bb270ba | -10.7017 | -45.9016 | 2026-09-06 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 51b9875e-1c21-37ed-a951-0cd228c227e1 | -5.3647 | -56.0051 | 2026-09-06 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ed8124d0-d010-36a0-8b59-eb72cc1cae9b | -10.683 | -45.8813 | 2026-09-06 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 6f09820a-ec92-3dea-b60d-d879627c7b90 | -9.1257 | -67.8322 | 2026-09-06 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b530b523-bf87-3946-9c98-4f4537105139 | -9.1443 | -67.8132 | 2026-09-06 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e13fd836-8f81-36aa-bf52-85f2d38bb778 | -3.2239 | -53.1742 | 2026-09-06 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0c55e830-12ef-3126-ab32-bc38c0296b40 | -13.3298 | -61.1064 | 2026-09-06 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8afb078e-6ed5-32cd-8d5f-cc84cb251083 | -5.3645 | -56.0447 | 2026-09-06 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 0c377752-e628-3121-a51f-03ef405386a4 | -10.7492 | -60.7097 | 2026-09-06 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| a00e4c7d-4093-32af-9138-2d2707f6339e | -10.749 | -60.729 | 2026-09-06 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| da9825f4-5271-30c0-a963-2c564b558d7a | -18.9269 | -42.0766 | 2026-09-06 00:50:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.7 |
| 3811e52e-93cc-3cb1-84cf-6e0e3ee9d156 | -5.383 | -56.0242 | 2026-09-06 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 46da21ab-a7a0-3766-b8c9-b562043ee167 | -9.1256 | -67.8507 | 2026-09-06 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ab15e17e-54ec-3cb9-a303-f303085d5739 | -5.3462 | -56.0256 | 2026-09-06 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| b7398480-fd66-3f6b-acdf-fde19d70299e | -3.5406 | -48.1889 | 2026-09-06 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 05bb2b60-c453-3b6c-9b82-2657b1518f3f | -13.3486 | -61.1245 | 2026-09-06 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 5becfcfc-649e-3fd7-8180-de49def66f2b | -5.1438 | -55.9741 | 2026-09-06 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 56bacba4-2667-3325-a4c9-3aa85653f14c | -10.6823 | -45.9268 | 2026-09-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a0184112-675f-327c-ae84-e575d34c571c | -9.1442 | -67.8317 | 2026-09-06 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 69d384cd-e0ba-3ca6-8b4b-885d7eb413e6 | -5.3646 | -56.0249 | 2026-09-06 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 251.5 |
| 1fe48dc7-b716-3779-a692-8aae501f0f81 | -13.7608 | -51.6495 | 2026-09-06 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b593bc8f-e25a-38ee-8bad-792d10e7486e | -18.9269 | -42.0766 | 2026-09-06 01:00:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.4 |
| dca5499f-e952-3571-aec8-ada01f87f8b4 | -13.7801 | -51.647 | 2026-09-06 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 91e2b97d-6494-3061-909d-e7daaf443bb8 | -5.3829 | -56.044 | 2026-09-06 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 444a141c-415c-3356-bad7-80af77919997 | -6.6514 | -59.945 | 2026-09-06 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9da99b3f-af90-3401-8d91-92832e06a87f | -3.5591 | -48.1882 | 2026-09-06 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 3701f94d-61dc-319a-960e-703baa0e725d | -5.3647 | -56.0051 | 2026-09-06 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 370f6abb-51c8-3811-87b4-89e8ccd652eb | -10.7013 | -45.9244 | 2026-09-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| d967dffa-2618-35fd-8ed4-e990c5b76a82 | -5.3645 | -56.0447 | 2026-09-06 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 7faa5ac9-c894-3f52-aa6e-328e4b339a30 | -13.7993 | -51.6445 | 2026-09-06 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fc64e134-9638-3e8c-8ec0-5b5a2a7fc361 | -9.1443 | -67.8132 | 2026-09-06 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e39a1174-82ad-3c07-a01e-5e8b6bfece29 | -9.1257 | -67.8322 | 2026-09-06 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 366349d2-e9b8-39b5-ae4b-29cac5b4de31 | -6.6698 | -59.9443 | 2026-09-06 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 835ff60a-44d5-3c76-a8cd-aa80d9ba25ae | -13.3296 | -61.1259 | 2026-09-06 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 18536d70-89ad-308e-9a43-f4fa91401d23 | -6.8813 | -55.619 | 2026-09-06 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b4b5b06a-1668-3a5c-9f31-08a4213a6601 | -10.6826 | -45.9041 | 2026-09-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 7e73a004-3b13-3bbb-bf84-753f85e4ae1a | -14.905 | -44.6782 | 2026-09-06 01:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| d35e6c79-4885-33b6-ab8d-b71724b135de | -5.383 | -56.0242 | 2026-09-06 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 5939931c-4929-3c71-af5f-a4a0574fc975 | -10.7017 | -45.9016 | 2026-09-06 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 4c1e6138-3ca7-3855-9d2c-6be1f3dbf6e2 | -14.9246 | -44.6744 | 2026-09-06 01:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 32389793-ad38-3fd5-b99d-1baa5b0a7841 | -6.6514 | -59.945 | 2026-09-06 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d7eae23e-589c-3300-86c6-b7bb3f293c7a | -5.383 | -56.0242 | 2026-09-06 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| ca54da62-fc26-3841-a2ad-89824c51311d | -5.3646 | -56.0249 | 2026-09-06 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 221.0 |
| fe9de854-f874-33e1-ba8b-3789ef204e9e | -6.6513 | -59.9642 | 2026-09-06 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| a13fb1f8-f210-35c5-9319-20b67ce03fcf | -9.1442 | -67.8317 | 2026-09-06 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| bf149eb8-abd0-3288-aea0-6b528ae58ab0 | -9.1627 | -67.8313 | 2026-09-06 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 097c19ff-e594-3ad9-983b-48162ead3159 | -5.1423 | -56.2703 | 2026-09-06 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 094bb13a-ee4c-3524-aba9-fa6b63a62405 | -9.1628 | -67.8128 | 2026-09-06 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| bc13d385-170f-3a2f-988d-ad7444c73ebd | -5.3829 | -56.044 | 2026-09-06 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c7cfd785-de15-3709-8e9c-feb0eacc3976 | -5.3462 | -56.0256 | 2026-09-06 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 371ceacc-a26e-3e4a-a264-c832e60ab1f5 | -14.9246 | -44.6744 | 2026-09-06 01:10:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 117.6 |
| b3c32cfb-a9a6-3a19-ba42-32d352170671 | -13.7801 | -51.647 | 2026-09-06 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| f3fea527-1a93-32c5-b918-3e19a4d6b99b | -6.6698 | -59.9443 | 2026-09-06 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 231a1ef6-f2cb-3aea-95ad-ddb31c3cde97 | -6.8813 | -55.619 | 2026-09-06 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| eea7202d-a8a7-35a0-94b2-781407d074e9 | -9.1256 | -67.8507 | 2026-09-06 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 02c89ff1-b7f9-3ccf-b443-58bbb06f1673 | -5.3645 | -56.0447 | 2026-09-06 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 353291db-68c9-30f9-be14-d30a884d0b7e | -13.7993 | -51.6445 | 2026-09-06 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a3afa542-77c3-3ef3-8fe7-d21f26af640d | -9.1257 | -67.8322 | 2026-09-06 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6dec37a1-8ff3-3377-afaa-21609e41245f | -9.1443 | -67.8132 | 2026-09-06 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 39d97b39-63a7-39ad-8439-ebfd337e8d78 | -10.6823 | -45.9268 | 2026-09-06 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 109650f3-878a-3208-9bcd-fbb6786e886b | -10.7017 | -45.9016 | 2026-09-06 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| baa3d564-4bc7-3506-bc19-e636500d36f3 | -10.7013 | -45.9244 | 2026-09-06 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| ad9bf5b5-c7e3-3477-a86d-5991acd74add | -10.71 | -45.92 | 2026-09-06 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc39489e-1f7a-39ac-a3f5-474135093abe | -5.3829 | -56.044 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| fb352094-de10-3fab-ac2d-32ad5bd4f9d5 | -10.749 | -60.729 | 2026-09-06 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 923f7ff5-1560-3be6-a655-4cbcf50fca9c | -5.3646 | -56.0249 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 210.3 |
| 810f04f6-bd85-3a2f-8473-6dd64d0fc900 | -13.7993 | -51.6445 | 2026-09-06 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d1bcb403-29af-302e-9180-3a7d132b8b9c | -6.6698 | -59.9443 | 2026-09-06 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 475b24e7-b84b-3696-815c-4a6cb44d7e95 | -9.1442 | -67.8317 | 2026-09-06 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 3d730c24-fcc0-384f-ab9b-2871c74de95d | -6.6513 | -59.9642 | 2026-09-06 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c13f09d6-e015-3ce0-87e2-728c186b80a3 | -9.1256 | -67.8507 | 2026-09-06 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1f04dc57-7ef8-373e-85c3-998ccaf34e3b | -10.7017 | -45.9016 | 2026-09-06 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 32740f40-3f0d-3111-af52-72f4129139c3 | -5.1439 | -55.9543 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 19d07357-1640-3ead-b9d7-d19f4da1c197 | -14.9246 | -44.6744 | 2026-09-06 01:20:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 7441f87f-9d16-3576-80e2-6067ac8c9f84 | -13.7801 | -51.647 | 2026-09-06 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 4bb90c71-03f1-34ae-b80f-3c99af65281c | -9.1257 | -67.8322 | 2026-09-06 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 2b4c501d-c2c8-33c8-b8df-0f8e2d2ddbd3 | -5.3645 | -56.0447 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 26e7022e-498c-3a79-8aee-9920efa8ac2a | -5.1423 | -56.2703 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 0b9f6358-0508-3f0a-9cbd-041fe66d4836 | -10.7013 | -45.9244 | 2026-09-06 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 76b6fb78-e1e9-3f15-a5a9-3a836b62c61b | -5.1438 | -55.9741 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e6f482f5-5227-32df-980b-8f1652a929cc | -5.383 | -56.0242 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 67f131b8-8e38-342d-bd90-7275ba24c58c | -6.6514 | -59.945 | 2026-09-06 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 2d5168dd-a327-3ef1-bc14-a83ff11e93b1 | -5.3462 | -56.0256 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0872751e-c73c-3d6b-9a50-ff0fbcc60316 | -13.7997 | -51.6232 | 2026-09-06 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| de038071-b841-3576-80c2-498746bc91e4 | -9.1443 | -67.8132 | 2026-09-06 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 5f06d198-a924-3c52-a333-b6f42552c241 | -5.3647 | -56.0051 | 2026-09-06 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 0e9ad239-f601-33dd-8061-ee0d8ccb7fe9 | -6.8813 | -55.619 | 2026-09-06 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a84077ae-d794-3be4-8163-77305a1e6464 | -7.7985 | -70.046097 | 2026-09-06 01:28:00 | METOP-B | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f333582c-63e9-3022-881a-6575df144581 | -10.7394 | -60.766201 | 2026-09-06 01:28:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de8c3946-b253-344b-b98c-bb5ece0c1018 | -10.7373 | -60.716599 | 2026-09-06 01:28:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9610e76-6a10-32ae-9917-aa26dab6750e | -9.1344 | -67.834503 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6a3121a-f0a1-395a-9ecc-86e646ac0178 | -9.3661 | -67.810997 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| deb5e883-0548-335d-9fdb-3d0768d97ed8 | -13.339 | -61.122799 | 2026-09-06 01:28:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 476f0305-8824-3c35-ac15-35f14fb872db | -10.747 | -60.7141 | 2026-09-06 01:28:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 812b048f-65f8-3781-af59-0cee9add0cca | -9.136 | -67.841499 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef26564-92dd-3b08-af4b-d02e95232026 | -13.3356 | -61.109299 | 2026-09-06 01:28:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 244298d7-e18d-3057-a3d1-0d7cc5c49573 | -13.3293 | -61.125401 | 2026-09-06 01:28:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
