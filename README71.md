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
| 428cdd8c-554e-38ea-8675-3f098380a39a | 1.05012 | -51.03666 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9efcfb33-b123-3efb-b705-64a69d296a67 | -3.33259 | -53.24316 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070c0244-2ea2-3872-9c9f-0403bf7ddb85 | -4.67734 | -44.09089 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e358d513-6c56-34cc-b794-3ad50464c1a8 | -3.84363 | -44.55111 | 2025-10-16 05:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9870f172-4055-3829-bbe5-2160a02a620c | -2.86766 | -50.73524 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| adfd3af4-c443-394d-9835-85632ae32b13 | -3.73305 | -50.25482 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51e038f0-fe06-31d4-9da0-86d0ea0beaac | -3.84648 | -41.57191 | 2025-10-16 05:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9e2f3e3b-7207-3990-a265-bb0560086c73 | -4.56209 | -44.00908 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57b82a4d-ee00-3474-9abc-d4ceeef5adf2 | -4.37151 | -43.38975 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e4c3365d-90a9-3d60-867b-2716817af17f | -3.07433 | -49.50106 | 2025-10-16 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1543f967-53d8-36a5-83be-329054e791a5 | -4.37002 | -43.40024 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 68b4654d-dbff-3a79-86da-64fc4c71bdcb | -4.66693 | -44.11013 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 7077bd4b-f571-3464-82f2-00cc2c215a9b | 1.77001 | -55.75696 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e816c8e-0a8c-32eb-9a64-6e611cb14c7c | -4.67579 | -44.09212 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee729d51-a4a6-3faf-b079-958cf17ae6ba | -4.11608 | -48.02054 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 8b2cc19b-546e-3dc1-b686-e7f1ec39c9d8 | -3.5645 | -51.11367 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54c2bbc8-954a-35c1-880c-703aa65d40e7 | 1.06559 | -51.01728 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d74afe21-8682-3704-8efb-b3cf4759c71b | -2.44796 | -49.37369 | 2025-10-16 05:06:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50e3a359-61fa-3e3b-a1fd-ede9c0bcb246 | -4.39427 | -43.41494 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7cdafc1-2624-3961-b296-d7bc2f1d105a | -4.6696 | -44.09107 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa542a9e-6e9e-329a-b357-d5612a788e76 | -4.65668 | -44.10212 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 03b42ae7-60cb-3f71-854d-e07b3b432218 | -3.92617 | -47.69418 | 2025-10-16 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1fffb1e-7842-38f7-b537-5ff454aacf69 | -3.88194 | -52.07558 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57d697b9-c72d-3daa-b666-90665d9e38ce | -4.40073 | -43.41574 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b47bf65-d6d5-31e0-8177-9d9b3803700f | -4.4238 | -47.75471 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d3f0c51-a540-3b51-9432-f741e8572ceb | -3.54757 | -49.97865 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15331468-f7c1-33a0-96be-244a4a120e73 | 1.22826 | -51.02886 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f4cbde6-3c43-3d74-80b6-3a4606d07506 | -3.1347 | -50.21428 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d69a6b7-ae4b-38cc-947e-88fc73c164ea | 1.82923 | -55.73273 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 215c580b-b84e-3e14-8e89-730da67bb54c | -2.93633 | -54.1732 | 2025-10-16 05:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fa567d4-e121-3b79-a08a-06ce59811cb6 | -3.86482 | -50.04738 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4b89489-dc43-36ac-b3ce-82870365b794 | -4.39505 | -43.40951 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c4ae7827-8af8-3996-bf91-9d1ec604eb42 | -3.07737 | -49.50929 | 2025-10-16 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76a0bfdb-2683-379f-a97c-22c285497bfc | -4.35786 | -43.39305 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0db38776-68b6-39ea-9fe1-8052571ef304 | -2.81542 | -54.38342 | 2025-10-16 05:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0789c6b0-62bc-3dfa-aaa8-b1e7a043b0fb | -4.38213 | -43.40769 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c0e96ead-b84a-327b-a788-b1ec457999c7 | -3.2117 | -54.96342 | 2025-10-16 05:06:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40088cf0-4347-3f75-bac6-1afba88e77a3 | -2.44435 | -49.36922 | 2025-10-16 05:06:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d807249-b2b7-3d7a-a9b6-20f9526c4e10 | -4.66142 | -44.11293 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fbf5c18d-cee7-3a8c-be09-b9769961d52a | -4.40152 | -43.41033 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30438fbc-c296-3c6f-811a-f5b0fa4923dc | -2.273 | -47.19035 | 2025-10-16 05:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb5c54ba-6a68-3515-8623-64811f7f4c88 | 1.79791 | -55.73383 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbab9978-aa26-36c0-80ed-a37e870e5500 | 1.89874 | -55.88842 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5845b65f-7d12-3891-a072-70c7c39fac3d | -3.88336 | -52.23973 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6199898b-f713-37a1-8632-92a7242e187b | -4.66357 | -44.09832 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 80298969-b97a-327a-83c6-64ade74c7e04 | -2.8769 | -50.72679 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3090d984-30f8-3b46-b9b8-7bbd4333ee7b | -2.88077 | -50.72739 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa734da9-74a1-30e6-b37e-32dd679d6a3b | -2.70742 | -49.86441 | 2025-10-16 05:06:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7dfb488-1ef2-36cf-a917-4cbb3d232ac1 | -3.84748 | -41.56508 | 2025-10-16 05:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 943df429-6cd5-3e29-8322-c8549a157cb5 | -3.68823 | -52.10279 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4517615-519a-3b09-a706-318c2d5ca554 | -4.66765 | -44.11363 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e8f680ba-347a-3b90-b235-faae05f9aa78 | -1.49143 | -55.44445 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40e8ac9c-c1cb-349c-a009-493ce6372880 | -3.49311 | -50.08868 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f77bcc8-869f-37a6-9d43-dd6655e12cc2 | -3.16236 | -51.81687 | 2025-10-16 05:06:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4de963b-0ba7-3f19-b73c-0ddab6a69b0e | -3.87973 | -51.94556 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 179febd0-7006-3d5f-a0b9-3a107f8f8209 | -4.02116 | -48.96794 | 2025-10-16 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac9b2341-e313-3f7b-99db-429dba85aea5 | -2.70854 | -49.85718 | 2025-10-16 05:06:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 815e7694-575d-35d9-a27d-3c9db03bc00f | -4.39581 | -43.40419 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| b2ecc692-2cec-32c4-9cee-5baced84a749 | -4.36431 | -43.39404 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 2bb643e4-7c76-33c3-8bd8-be58c3d9be7b | -3.88038 | -52.23503 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73450f63-d0e9-3639-9d68-1e498f5a29d9 | 1.82928 | -55.75526 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41abc9cc-7bec-3bf2-9f4c-5e149b70a2f4 | -4.15575 | -46.79221 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ad5af509-d623-3644-8aad-6f6e83742258 | -2.42656 | -57.12124 | 2025-10-16 05:06:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 839ad4ac-18d8-3160-97d0-424672f05b4e | 1.76146 | -55.76585 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ab51f8c-f427-353b-b2ea-e0216435affe | -4.86923 | -44.57376 | 2025-10-16 05:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f271daad-4d1b-3877-937f-b4ba4e477327 | 1.73934 | -55.80319 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4828401-fb86-3529-8a1d-739056f918b6 | -4.66828 | -44.10054 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c9418427-324b-3562-8063-06896153feee | -2.81263 | -54.37943 | 2025-10-16 05:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ee463e9-669c-3abb-a584-6c4274c2b90b | -2.87854 | -50.74182 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8f7956a-9c58-3573-88b1-eca5dc0881e3 | -4.28399 | -48.58963 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 008103de-f291-3847-8fa4-75f28088ae43 | -4.66836 | -44.10883 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0ee78bf6-bd52-3e30-8713-3daf6a618539 | 1.83774 | -55.72013 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85099f9d-188b-3316-a06c-25e3dbc32573 | -4.66275 | -44.09475 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c845cf65-bfda-3f1f-afe0-fa92e7613ea4 | -3.65943 | -51.75306 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a145e6f1-bf74-31dc-a043-977f94136209 | -3.14163 | -49.0344 | 2025-10-16 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef99a64b-1595-3eba-9930-daf388d9e294 | -3.67261 | -48.3096 | 2025-10-16 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7eeca23-e2cd-344d-b53e-769cd2f34f50 | -4.11993 | -50.71905 | 2025-10-16 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 508eee8e-0209-3814-8c52-0ea6aaddfdc0 | -2.71206 | -49.86141 | 2025-10-16 05:06:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 792c9a85-14a7-3454-adb5-c627cbff7918 | -3.38681 | -50.27103 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d131133f-1f19-3375-9756-ba14d1de2a2b | -4.65807 | -44.09261 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ec69463-4fb8-3e76-ac2e-324b93eeddce | 0.99044 | -51.08342 | 2025-10-16 05:06:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da1d2184-19f2-3e60-a07f-11bd44f5ec13 | -4.10994 | -48.02938 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 17c8eddd-469a-3966-8a90-fc0648d6bca2 | -2.30174 | -48.57778 | 2025-10-16 05:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10ea2a6d-336b-3fda-8554-1b44a815e514 | -3.36953 | -51.07931 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93465ae8-26d6-3c0f-b287-a5595441ce34 | -3.28884 | -50.15168 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81d5ed50-eba1-396a-8cd4-72abba1cd55a | -4.37868 | -43.38577 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 35c49d68-3239-34c5-9627-226ec26bb531 | 1.81473 | -55.93159 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8c22cef5-6124-3678-9a92-10326569225b | -5.05318 | -44.46629 | 2025-10-16 05:06:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f894e8e8-ce47-3c93-a146-40a54f44c092 | -4.37569 | -43.4067 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0fa07ebc-6fc0-30e9-b68f-2040a80d922b | -2.87079 | -50.74064 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 291e0aa8-451e-31d8-9f34-cd9cceb0b58a | 1.80263 | -55.87649 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4804703f-8192-3150-aff3-fedb7c162621 | 1.81187 | -55.93584 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4bbfd07-80a7-330c-be66-b5a811563fda | -4.15529 | -46.79523 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 08470221-7042-352b-a6bb-65c61ce58b3a | -4.67029 | -44.0862 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5be3456b-6879-3256-adb5-e76261fb88d2 | -2.88152 | -50.72259 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a54b0275-4214-3e89-89b0-db56b67133b0 | -4.39886 | -43.38304 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 464c8d71-c6d1-3235-8dbf-e778b3a6ec9a | -4.66566 | -44.0841 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd524b60-b3fc-3aa1-be42-fc7decff8ee5 | -4.86861 | -44.57807 | 2025-10-16 05:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d214c7c4-7332-3f75-9b8f-8031844e2132 | -3.53878 | -52.70275 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7d66460-c02b-3c0b-8cb4-aaa47b506273 | -3.27185 | -45.83803 | 2025-10-16 05:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README72.md)
