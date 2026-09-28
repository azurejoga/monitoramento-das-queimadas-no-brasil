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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c157caba-6b2c-3356-822f-e5c57724a20f | -3.15183 | -54.08159 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc3232f8-c892-3f65-b9ba-ba8b6a2b8ee7 | -7.91409 | -61.41965 | 2026-09-28 05:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f94ed11e-7286-3524-aa7e-855d17e91723 | -8.27884 | -54.70796 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89bb662d-9ba9-33a5-80fb-b08ecb510305 | -2.88929 | -54.09046 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89968271-5956-36e7-8694-428b0307530e | -8.24322 | -45.40596 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa412ef9-d140-3a2a-9622-28fa885fa565 | -8.10494 | -44.00515 | 2026-09-28 05:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23ba2dc9-6bdf-3637-8834-b84cee8ead98 | -2.92778 | -56.57425 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 678cc748-5864-34ae-8ba9-09c0da985150 | -3.99105 | -50.52605 | 2026-09-28 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebf89eff-17c4-37e8-b108-5e313d177953 | -3.05255 | -51.27367 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a84d99a-679f-3f70-a5dd-b3f58e65c891 | -11.19435 | -44.81422 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f5845219-957e-3719-a175-6398ea1f0443 | -3.22481 | -53.96121 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb53ce0e-f854-3dc4-972a-07dc5d60f224 | -3.15351 | -54.09256 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da38c899-3545-3c21-88d0-e3ebd873c6ec | -3.41779 | -48.34104 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ad8bd56-d3ef-3567-974a-811006479a1b | -7.38433 | -42.1077 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d23e8975-8444-38f5-9297-af1c79482c0a | -3.51309 | -50.31471 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0be4557-11a2-39d2-a7b6-54ed8981195f | -2.91663 | -54.1987 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 045fc2c6-72d0-3923-8d0c-7da0f8663b49 | -2.06565 | -56.87165 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55aac54c-b37c-3b79-ba23-140dcfb2b06c | -6.07499 | -57.81602 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71fafe9f-a8e0-3faf-b7ca-8fd969ec1e43 | -3.51011 | -50.30996 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 698443a9-8884-3592-8f9a-3dd7a477f91c | -2.56014 | -54.73124 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 571437e3-42d5-3923-b223-244f6fbda994 | -3.07328 | -54.38155 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c43041e6-74cb-3fb8-8eb4-59f516473fa1 | -2.72929 | -54.20126 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9acdccab-e939-3832-b910-a344379d1e69 | -2.54086 | -56.42769 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e43c14e-b986-3cd7-b664-1c8cc1cdbaa8 | -7.2803 | -55.57309 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6875d477-6e2c-3de8-9aa1-17fc0bdb15b7 | -6.94626 | -41.61797 | 2026-09-28 05:10:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e49a7e89-d567-3e21-8e05-eb7193e77166 | -6.72104 | -45.59592 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfd4d2b9-6156-3a00-9a4e-96d9a92a1cf5 | -2.91381 | -54.13012 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54062caf-d5fd-35ab-b0d6-ffb8c2530dda | -10.21125 | -50.00633 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c24d5d70-b931-392e-878a-d3b8c9345b56 | -7.67779 | -54.85181 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c628db7-6c0c-37f3-9b92-e04b2e0a0d13 | -5.99916 | -47.38954 | 2026-09-28 05:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72490b93-4a28-3071-9917-0fc7cf32a35f | -7.81698 | -55.14313 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2463275-8686-304b-bd55-8a43818b8a52 | -3.07496 | -51.19958 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5806339-8121-36ba-80db-aa57f8a112ba | -8.23365 | -45.47785 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a88f70f0-e32e-33b5-a233-818d62fb95b8 | -7.6835 | -44.78907 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df5dd52b-7724-39c4-a919-2c56ce139967 | -7.70995 | -54.7708 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b340cb15-e447-36ed-a6ea-d332bfc5bce4 | -11.18372 | -44.80672 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 770f6cd5-9c39-373a-9d0a-b01f5685b031 | -8.06258 | -55.33799 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46ec6025-9a05-3ad3-abed-fa6bbf37803c | -11.18533 | -44.79419 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 19030982-baf1-36b3-803e-6bd26fc19f69 | -11.18426 | -44.80256 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f97895fd-eae7-32df-92fe-2e4c8a33f236 | -3.41611 | -48.33034 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4d61ee9-4f46-3dac-9339-e11a3a099139 | -7.37777 | -42.10678 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cf0183d3-7652-3609-94ff-b5c6fbff42e0 | -10.11449 | -50.18974 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c698981-f8f6-3635-94a3-7a36bcf1a3d7 | -6.71628 | -45.59208 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ab7150f-af61-3213-8cf7-aa3a7bb60766 | -11.19006 | -44.8008 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 6a128dd2-0f43-37af-8584-257fa987f113 | -8.01302 | -43.74265 | 2026-09-28 05:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fd158732-3f6e-32e3-9a8f-3ef8f02e6c9c | -2.0539 | -56.86697 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c30f73f-0566-392a-bffe-128e4adf945d | -11.18955 | -44.80501 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 95d7a100-04ce-366f-ad51-d45f41e78d49 | -9.93897 | -50.23605 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3fa58cd1-318b-3732-9b27-96b46a6b2ff2 | -8.89461 | -46.19325 | 2026-09-28 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4db2a5cd-e1a2-3928-8ee8-d1266b3ba8f6 | -2.86424 | -54.11873 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d491265-0188-309d-8ec9-d40cf417dc20 | -5.72437 | -43.28129 | 2026-09-28 05:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 48c31597-e345-3e25-91bd-b71b22746c8e | -7.06157 | -55.47966 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce5d3161-de5a-337e-859f-d5024fa7c262 | -9.48123 | -46.39492 | 2026-09-28 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b9e4513-191a-3830-a368-a929c8486624 | -8.45139 | -44.67863 | 2026-09-28 05:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ca6b0a6-9ee1-3cf0-9020-230e856532c8 | -2.95901 | -54.09784 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5fe3e695-93af-33a4-9e91-d71d0a89c745 | -3.01694 | -54.20728 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98e342c1-db77-318c-8cf1-8d7b68935bb9 | -7.71328 | -54.77133 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 971f906f-1b8b-33d2-b117-8a0e17cdb214 | -8.10297 | -44.0092 | 2026-09-28 05:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7615544-da55-3c52-941a-cb53b576e9cf | -3.01804 | -54.17876 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5feb76e5-888b-3345-966b-83e240029fe5 | -8.13875 | -44.44884 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b24e762-2f98-301b-b8a9-8f216aa87c41 | -3.01748 | -54.18226 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b53691df-7915-3d35-a4ab-c5194c17ddc7 | -3.15128 | -54.08507 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b52d9761-8f84-3cd5-90e9-d3854b720fb5 | -6.01644 | -57.6755 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77a130b9-1189-3f9e-89aa-97035325c1e5 | -4.85056 | -42.88589 | 2026-09-28 05:10:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7653fc3-57e7-3c15-bbad-f851c2228d6f | -3.28922 | -50.31697 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0d76add-a86b-3fa1-b5f7-4f1dc73b399c | -4.79527 | -49.11302 | 2026-09-28 05:10:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7165032d-6360-39b8-85d0-ce98d1986941 | -2.91436 | -54.12662 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5e2dcce-5035-39f3-a13f-0fecb60278cb | -8.03642 | -54.89131 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3436a325-1e34-33e7-a6f8-14d1ea7f60b2 | -10.2062 | -49.98373 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e649332-07b7-37d4-a7a8-2a98d4668327 | -8.45089 | -44.68248 | 2026-09-28 05:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e06a8f7-17e1-34eb-8dd2-b3e7ee96b4ca | -6.94996 | -41.61303 | 2026-09-28 05:10:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3e7b4402-cfe5-327a-869d-b99085b251b7 | -9.62148 | -55.11021 | 2026-09-28 05:10:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a76fb1d4-45ec-322c-a89f-7d19e8fb6f89 | -7.71772 | -54.76489 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee99a182-7e50-3e3b-9aa0-a8c10d0e5c9d | -2.89711 | -54.1705 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 228808be-03be-3931-be00-7eb08c5a34cd | -8.25438 | -45.40442 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3e39bb6-8986-33d0-91e3-3d6a04b89bc8 | -2.89654 | -54.10949 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb76447c-9ad8-33a4-b335-3f3f2b19ffda | -3.19439 | -51.0363 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30e0a11c-de9a-31b9-8621-a0ab015db42d | -9.77435 | -44.82864 | 2026-09-28 05:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a16c8f7a-248a-3985-b5ac-5f32431617c3 | -3.00634 | -54.20922 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1ff1fd0d-4e1c-365f-baa8-6bfcfd94142a | -7.82257 | -55.1296 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8ec6a9e-6d68-32d0-8ab5-1dee3f7fb245 | -7.37914 | -47.0151 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1c61863-5c7d-3539-b24f-596ed7c135bb | -1.81172 | -57.10558 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32bba6b7-ba0a-36e1-ae11-6da29555fa61 | -6.09962 | -57.62112 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f07e392c-6127-37d3-96c4-9e3a6e6f5c83 | -5.29896 | -55.90004 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2812a60d-7110-3ff3-af0f-cfdf3d7dcd37 | -4.98054 | -56.14642 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce373c96-60e8-3dce-8a9a-c8f8550f7d06 | -3.20429 | -51.04179 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 14547644-4a28-377c-98a9-1e93ba461644 | -7.68157 | -44.79157 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3a571ae3-bc1b-3efa-8bbe-18e63ece5f6d | -8.42692 | -44.86518 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31b25b10-299b-3487-9f02-6271eba363a7 | -4.98753 | -56.14747 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea600f84-8b87-336d-a5c7-5bbfccc7490f | -6.78551 | -59.38453 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e2e793d-9b09-3fc8-b488-b40c585c0b80 | -7.68168 | -54.84885 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49c03064-201a-3d45-b757-45f47189a868 | -6.78144 | -59.38382 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23b694ae-b8c1-34ef-aba4-f7d69840e860 | -3.35943 | -50.466 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 34810289-4038-3048-ba0f-050a2e607a3f | -7.82088 | -55.14016 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8386f579-832e-39f3-8d08-c3a849fe867e | -6.07678 | -47.30433 | 2026-09-28 05:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e19caa1f-6f81-3bda-ab33-de2d01191844 | -10.26129 | -44.61901 | 2026-09-28 05:10:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ccc2c84-5032-330f-994a-d646a3f67933 | -2.89653 | -54.08802 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bd06e31-fcf8-3c6f-94b6-07fb3e233e46 | -2.67056 | -56.45828 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d647d886-6a51-31cd-8dcd-ed0596561459 | -9.19732 | -45.76176 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f3a4b6b-0135-3435-92cc-c880e4b289f8 | -6.59495 | -47.16483 | 2026-09-28 05:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README48.md)
