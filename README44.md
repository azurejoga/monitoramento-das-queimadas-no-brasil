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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07fb3129-e030-3127-a3cc-b3a40ec1ca09 | -9.08096 | -67.84263 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7b041f5-70e0-31eb-89dd-3294ee3c0a9a | -9.04157 | -67.45232 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa9cd64a-6baf-34a8-8563-ac7ceb223853 | -9.04061 | -67.45776 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1e75cd3-bdd6-3894-9b7b-f1c44f3bbb6c | -9.03932 | -67.45409 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c1b02f8c-fa9e-32ce-8fb1-d9c1e7e53340 | -9.03832 | -67.45953 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49bee300-f288-3ddb-b3a8-26896622931b | -9.03671 | -67.45142 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0da214e1-f04b-3749-8362-84f707b04c9e | -9.03282 | -67.44508 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 549a28f3-334f-3453-8790-8a08a5d00b78 | -9.02796 | -67.44421 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b77f6b3-715b-387e-9d4c-e36427f93b1d | -8.97658 | -67.73388 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18628e93-31bf-334d-973d-da955ba0e628 | -8.97556 | -67.73961 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7940143c-6980-39f5-a50d-3029758096a8 | -8.96172 | -67.73113 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c063c254-777a-352b-ad77-769d5e0e5ccd | -8.9607 | -67.73685 | 2024-10-19 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e501b7eb-82e2-3e2a-950b-a360298ecc14 | -9.41324 | -68.85188 | 2024-10-19 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e897448-e4cd-35c9-aab7-d26cdb5c8be2 | -9.40733 | -68.85424 | 2024-10-19 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9144f84-988b-3782-b4f4-0c9ddbdf9923 | -10.76297 | -68.80912 | 2024-10-19 05:16:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fde86047-54e8-33f6-a88f-86c9a86fc990 | -10.76175 | -68.80751 | 2024-10-19 05:16:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deb07fda-f7df-3e87-a82e-0de39523cd7d | -10.76118 | -68.81063 | 2024-10-19 05:16:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b961f9ba-2ae5-3a59-a961-7c6caf98bbbf | -10.75781 | -68.80814 | 2024-10-19 05:16:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c41c742a-e7e1-36c5-ad89-8c4cefb00d1a | -10.54092 | -68.571 | 2024-10-19 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0218246f-367d-3a83-9da7-6d952d576a6d | -7.68191 | -47.31318 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6e5d9d53-8e99-3754-873f-25e6a57d18ad | -7.68126 | -47.31834 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af8fc82c-8ea4-3904-a070-884f0f297568 | -7.68041 | -47.31154 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3acff9d3-177b-3a01-8fc3-692662cf0b35 | -7.67972 | -47.31671 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a6091762-af4c-3ddd-9ffc-f16ff35a5dcb | -7.67903 | -47.32185 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0187cce8-3c89-3a18-91ed-18898be9c5f0 | -7.67422 | -47.32268 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a84443d3-9fdd-347b-9fb3-f5d32a418044 | -7.67357 | -47.32783 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eb23b238-9ddf-3d0f-acb2-f1729cf7a12e | -7.67265 | -47.32103 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a519b2b0-0bef-34a2-93a9-9f59549118af | -7.67196 | -47.32619 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b5479b94-cb99-354b-8587-c861fc17b5cb | -7.67128 | -47.33135 | 2024-10-19 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 14c31caa-7c0c-3f6c-b41a-134c3d9f9bba | -10.26545 | -54.25858 | 2024-10-19 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5ea2035-4cce-3060-9a1f-f6540adeadeb | -10.26491 | -54.26244 | 2024-10-19 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53729538-b2d2-3dd3-8a31-0c9ecedd9d8e | -11.9164 | -55.27206 | 2024-10-19 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3df266fb-67c4-3c73-bef6-3dc0550535e1 | -11.27852 | -54.22945 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 251924f6-6eb7-3e04-b973-3cf218939c4c | -11.27799 | -54.23345 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8078ef0b-93a5-3f77-b9f1-7755c5935a5c | -11.27745 | -54.23745 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bb17dc50-8b4b-308b-aa37-b24440b15f4c | -11.27504 | -54.2259 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0a579da-90e7-31c4-9786-8abe99c1b228 | -11.27447 | -54.22989 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7a47f32-405e-371a-b422-7ba68d69c0ec | -11.2743 | -54.22873 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73daacaf-8453-3b48-9a99-b8ded671d4b7 | -11.27391 | -54.23389 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6b2a78e1-b46a-338e-886f-1fbc3c231a7c | -11.27376 | -54.23274 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e2ee3f08-6241-3a9d-822c-60a4ab63f6d1 | -11.27323 | -54.23675 | 2024-10-19 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d4a8b960-666f-36db-8835-facc191f6595 | -13.13641 | -54.92509 | 2024-10-19 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4c090a7-4c13-3132-a3df-9aa70d9a17e9 | -12.50031 | -54.43316 | 2024-10-19 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64e80497-aed6-30c9-b29b-c1c82e788275 | -12.49976 | -54.43719 | 2024-10-19 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ae8cc37-a6a3-3448-9cd2-df7ad7d8a33d | -12.44081 | -54.42466 | 2024-10-19 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31e7142e-9153-3bff-b6ab-5380ea3d8751 | -12.39509 | -54.69373 | 2024-10-19 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb2ccf17-708f-3614-a009-585e7383fe2c | -11.91085 | -56.19358 | 2024-10-19 05:16:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0a88399-b1ba-35f0-a93a-b2eb355e237f | -11.90641 | -56.19769 | 2024-10-19 05:16:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea8fe76e-4b78-319e-b518-1ba7cfa5e40b | -9.35523 | -57.60455 | 2024-10-19 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31f71c97-0023-30dd-892e-2aaff0ce27cb | -9.3518 | -57.60404 | 2024-10-19 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71e9a9ec-d55d-36b2-a885-aaf296a8d60a | -9.18012 | -57.62827 | 2024-10-19 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb3a60cd-1195-3274-aa7a-3d874029d021 | -6.34524 | -58.17162 | 2024-10-19 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1d1c2ac-52c1-3e24-b991-51984e21551c | -5.12628 | -59.82565 | 2024-10-19 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dea0d034-bd68-37ff-8950-1df37d49a3de | -7.29932 | -59.73169 | 2024-10-19 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b95a8c2-e853-3c80-8c3f-0dbf41559ec5 | -12.68205 | -60.90734 | 2024-10-19 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a506f2-f14e-3865-a8c0-5c230b8cffc6 | -12.46937 | -61.68033 | 2024-10-19 05:16:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d09d7a52-2086-3408-8b5c-efe85a32543a | -12.46877 | -61.68399 | 2024-10-19 05:16:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 603d18ad-f557-3e66-87af-5b3df808b062 | -12.16782 | -62.15049 | 2024-10-19 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b703a8f0-8182-3cd1-b30d-52f7ec7ab2bf | -12.16719 | -62.15426 | 2024-10-19 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b83f0156-5bbb-34f8-add8-56928919cbcb | -12.16657 | -62.15803 | 2024-10-19 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68240790-6117-3f20-86c9-a35fb7784951 | -12.1644 | -62.14993 | 2024-10-19 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19dea067-36c5-3b76-9eb7-a7ec7b248209 | -12.16378 | -62.15371 | 2024-10-19 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4432ed24-1268-30c8-a0ae-83bd879a4358 | -12.03454 | -63.14637 | 2024-10-19 05:16:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 148a0928-9aac-32b2-a56c-9e4879e3b725 | -6.81345 | -63.15526 | 2024-10-19 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7e32efd-1451-323a-8f28-f185724e633e | -6.69662 | -62.85505 | 2024-10-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64f1ecce-6a89-3fb5-b925-fdc064136978 | -6.62495 | -62.93375 | 2024-10-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78b8797f-0db9-3438-a56c-778869d6dfa8 | -6.6242 | -62.9383 | 2024-10-19 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ca3c947-8078-3ea8-acc3-91307e9ab1e9 | -9.06177 | -63.66238 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42afa9d7-00be-369e-b072-12c882797b41 | -9.061 | -63.66706 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f7baf42-fd31-3d39-acdf-787009ee9ee5 | -9.06099 | -63.66503 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e8aba47-516b-363a-b08a-c799242d01d4 | -9.06023 | -63.67174 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ce6990d-7ed0-30b4-8f4a-ba54c54291c8 | -9.06018 | -63.6697 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b67f3ef-2ac5-3b24-baee-0afc4a5f3d59 | -9.05946 | -63.67644 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4438b431-2bf9-3342-8a3c-01a4e29013ee | -9.05938 | -63.67437 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e968b18-f4a7-3d51-8f1c-6013d307b2b4 | -9.05858 | -63.67905 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e20bd605-8bb0-3c84-b553-07c1c34de07f | -9.05721 | -63.6664 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65262c94-85be-388e-8dbf-c230ffbc2f7f | -9.05644 | -63.67108 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 056e2314-bf05-355d-a83f-94872b13b660 | -9.05639 | -63.66904 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf6b9480-00d4-3fc8-9c30-196cd9d4934f | -9.05567 | -63.67578 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f68863d-cd03-3c6f-a7b5-93d1e91a2f95 | -8.58672 | -63.43793 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae5af64e-5400-34ea-a053-e47948d3b626 | -8.55078 | -63.42001 | 2024-10-19 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d425c4e-39d0-3ad6-abe4-93e57d0c6817 | -8.12602 | -63.87473 | 2024-10-19 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd598b90-631e-350e-8227-28c804fe38dc | -9.69922 | -64.18894 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 429a5b2c-2260-38de-a952-dfc16c70be1c | -9.69839 | -64.19388 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2bd15d1-8e8f-32bf-a265-802affe514eb | -9.69535 | -64.18826 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 177390ec-cebe-3e0e-adef-d8644943c8f1 | -9.69452 | -64.1932 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d90a9aa-f9a2-3c7e-a31b-811b073d13d5 | -9.69369 | -64.19812 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d78b52b-1bd8-3d7f-98f8-e66da7cc7976 | -9.54954 | -64.12476 | 2024-10-19 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88c81e10-0872-37f8-b6b6-eaec878dd22f | -10.34263 | -64.40607 | 2024-10-19 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 522cd8ba-9493-36d5-b7da-04b086cbe6e3 | -12.0216 | -63.51656 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27964f90-f8fb-3fef-a634-23f7a30fdc25 | -12.02124 | -63.5138 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eca319b-68eb-364d-9823-a6f7b97761b6 | -12.02053 | -63.51807 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 772679ce-320a-3d5f-afe0-de6787dd6b6b | -12.01982 | -63.52234 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 35d58f84-819f-3052-9a27-92d681d87dce | -12.01872 | -63.51165 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1824ec44-70a5-34a7-af37-2ae51ebc1ef3 | -12.01833 | -63.5089 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6a7eaf3-f266-3d6f-b95b-d3b7777f1457 | -12.01799 | -63.51591 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9d4c790-9842-3728-9ecf-c7677aae91c1 | -12.01762 | -63.51315 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f45149d-cae3-394f-ab07-bf47043c436b | -12.01725 | -63.52019 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ebfc946-bbdd-3162-acdd-a4c70ef7bb81 | -12.01691 | -63.51742 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 907c1a65-e257-3a8c-91fb-505b32cd5d45 | -12.0162 | -63.5217 | 2024-10-19 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README45.md)
