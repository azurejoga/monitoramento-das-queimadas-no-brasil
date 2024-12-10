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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94e0a812-6383-3249-a9fc-dd7fad91210e | -11.72349 | -57.43965 | 2024-12-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50522736-6c79-3e50-8a67-ea9ecdb70c65 | -12.36966 | -54.16328 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ada4458-bf7f-38e1-8c4e-63951ec5905b | -3.59018 | -51.25336 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1fe2196-03d0-3dbe-b239-a8c707e3d78a | -3.10696 | -54.07621 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20b1e16b-9675-34e9-8a2b-ae15ee3b1ecc | -3.11968 | -54.04016 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f7c27bd-b3bb-341f-a6a2-eccf9af9ce37 | -2.31157 | -54.001 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f3223f5-ed39-3328-b632-5bff67580106 | -1.72846 | -52.48224 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b576adec-af7f-39e0-be49-5a2b83c808cb | -9.18689 | -63.43729 | 2024-12-10 04:53:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8893379-34ae-3334-b987-37e0a91034ac | -2.64095 | -48.64556 | 2024-12-10 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 304d94e9-cf71-3177-baa5-f7476c3a0aee | -2.82401 | -53.06703 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e35c0630-77be-3e84-9b2e-e4c7bf470fd0 | -11.14892 | -54.22825 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f72e6a6-ce17-3633-9b7d-aaf1890d1f82 | -3.09151 | -53.3545 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edc16357-a21b-3d56-a93a-e8d04e410384 | -1.60488 | -54.88506 | 2024-12-10 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc7701d-0e6d-36ff-ab02-de09150149bc | -2.79493 | -52.86224 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a52f67d3-29d1-328a-ba50-208a1898bfe4 | -2.99462 | -52.84688 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c0e47be9-6ae4-37c9-958f-23d3abe17213 | -3.94658 | -51.03783 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 046ef7c7-1836-32ab-be48-cdf1b580373c | -3.00305 | -48.04598 | 2024-12-10 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e43c0fc8-283f-3242-9268-d1aa8937ce39 | -3.92954 | -53.58412 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38b2c69f-e4c7-3aa5-a896-35711669858b | -2.83567 | -53.05805 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2e0ef41c-7e9c-3408-95ac-7b69519379ab | -13.10525 | -43.32417 | 2024-12-10 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4916da3d-0c56-31fc-9886-5f79430501d3 | -2.47406 | -53.63328 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4983984-805d-31ba-b1b4-61b901a4cc0d | -4.72768 | -50.95622 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46964a70-1228-3262-90a5-e27bd4bd0282 | -12.24669 | -52.44781 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5201d8ab-9b36-3a23-831e-93eaa15b2800 | -3.10993 | -53.23789 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 268e3f32-9835-3d16-9fb9-af58e06fe05f | -3.27893 | -53.09502 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c764b5ae-9e44-3de1-97d9-f90e2c4f2c2d | -3.26502 | -53.87487 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 93b0c151-3403-325d-bb7a-4710383073aa | -2.83233 | -53.05753 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7db6495c-0b2d-394f-8130-0857972fc060 | -3.08701 | -54.06934 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b45f458-c24e-3883-aefd-8c9aa25a4c09 | -6.06245 | -47.3816 | 2024-12-10 04:53:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e12e397-db0a-3955-a0ea-1b7affe3b19c | -3.14737 | -54.48451 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eaf16b79-60ee-3885-a6fe-35293ca6ebfc | -5.92291 | -48.04705 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef0af9e3-5b4e-38a8-bf9b-311ba42c08cc | -3.03843 | -53.43739 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78372484-74f4-3e59-9086-a8d99a90f9ec | -3.77994 | -50.05199 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ac49644-af6a-38c3-9e0b-4954ea94349f | -3.11558 | -54.06608 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe618599-5fbc-3dbf-9f76-50d4c8479d7b | -2.99076 | -52.84986 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 54e2ec93-d5d4-38b3-9171-a5322b17d74e | -3.37197 | -51.19125 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 839a3ca4-d34a-31eb-bf71-add825db3aef | -2.47576 | -47.61303 | 2024-12-10 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9d90ade3-19a5-3bc9-a38c-df349faeed6b | -4.38151 | -47.75399 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 70e3f15d-5122-3b68-bd3f-366d0ad90e19 | -3.2032 | -51.35773 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d651925b-f532-319e-a7f5-9e2b85576726 | -6.96022 | -42.99081 | 2024-12-10 04:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b7407bcd-a8d2-3a3a-a76e-2fbe5100d951 | -3.09059 | -53.21325 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb783ea4-6c09-3255-a4e2-f077e33f2505 | -10.95922 | -54.09321 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63fad151-661a-3b3b-9c90-55f300219913 | -2.47011 | -53.63636 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b2e9cf0-97ed-3e20-8cc3-2c8bba89f39e | -12.2047 | -54.30608 | 2024-12-10 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28bd38a1-bfae-3df0-aa64-e6d0513ec1b9 | -2.3047 | -53.99993 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b60af00-235d-3b29-994d-4585f4240101 | -2.82624 | -53.07456 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb9fad89-068b-32f0-bd31-29207b3cb596 | 1.97978 | -60.91166 | 2024-12-10 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c625604-9a74-3069-a874-812db7a470c0 | -1.726 | -52.78122 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d321ca49-ef26-311d-b8f2-96daf3246da4 | -3.0681 | -54.07786 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3c813e9-be61-3850-b559-9ef0e0176565 | -10.45542 | -44.89046 | 2024-12-10 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33f95c90-0391-33f1-8121-1fbf8f7d7030 | -10.44498 | -44.88911 | 2024-12-10 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fb94c0e-8935-3b57-ba06-17dd61afd780 | -5.91277 | -48.06104 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3c05b255-8d2d-3f54-9143-199f4fe336c5 | -6.83753 | -44.38703 | 2024-12-10 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e77072fa-ebf4-3449-9f32-774594b2465a | -4.39797 | -47.7513 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66ad1f23-a3d0-3344-aa37-63672fcc8d83 | -2.47608 | -53.71585 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cc412fb-591e-3fe9-9e18-b2287d2f5327 | -2.47947 | -53.71637 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6af0800-c5d0-3137-8aca-aeb90a07616c | -6.97145 | -42.99269 | 2024-12-10 04:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5eb1269a-d8c1-3947-8f0d-9faff8f7d706 | -2.81732 | -53.04445 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b701cb71-9e71-3ff5-b485-abf3294fda69 | -2.77443 | -44.99276 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bc7b3324-04e6-3b03-9623-4cf18a53d269 | 1.97414 | -60.91251 | 2024-12-10 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c16de24-f2ec-3e7f-99d6-486209497402 | -5.63279 | -44.84048 | 2024-12-10 04:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 212875bf-c5c3-3de2-b2a7-0a6f061c9906 | -3.63301 | -52.68131 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e19f914-18f8-3347-99bc-23abfb4909ab | -3.51162 | -54.49335 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2cf4fa5-34ea-3ee5-8748-8ca46a4b1708 | -3.11976 | -54.01751 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b132b71c-10ef-3387-8183-c5cd919c3b16 | -3.10011 | -54.07517 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e61bb159-e661-31ae-a610-8c76112c6a3e | -2.64827 | -54.29095 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e7271d7-e73c-3550-89ef-67fa62e5300d | -3.23792 | -42.42856 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0f771da-9e51-3f83-bedc-4243d71da10e | -3.04466 | -54.24646 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 509a355f-4e34-33a2-820d-cd7a003b712d | -3.10542 | -53.90974 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7979c1d1-c8e8-3bfd-969d-fe91c59db8d1 | -3.7022 | -54.61951 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828a5f24-5eef-31b2-9bd4-2c07513fe1e0 | -9.39136 | -56.01714 | 2024-12-10 04:53:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c006ac1-91cf-377f-b278-9eeb024e86bc | -3.04121 | -54.24591 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c110d71e-643a-30e9-a63c-b45d873db9a2 | -2.99299 | -52.85732 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b13ebd4-91cf-3e4e-94a6-49de625af251 | -2.45598 | -53.6379 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e98d4a5c-80cf-3ef3-bd7b-749a37f36600 | -3.60169 | -53.74519 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb145841-351a-3362-8d21-0676c010aa80 | -3.21373 | -53.09927 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 080c7356-0ec0-3ac4-a930-6724535c4064 | -10.02613 | -53.7533 | 2024-12-10 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c8616783-258a-31c8-a540-a9510d313ac5 | -2.62111 | -48.06027 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cbba74ce-5e50-3dbd-bc0c-9aab0d841b1e | -1.54475 | -52.67747 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96cdc51a-62ad-3af6-a1af-57241b58ef1b | -2.45541 | -53.64153 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 138842ea-5e4a-3b79-a18c-759a5d4afdc8 | -2.79906 | -53.24722 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 975dcd81-fa38-31d7-8dee-efcb6a585836 | -1.268 | -52.11986 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c33e1d3-f4c2-3438-a1ec-142b536fcdbf | -2.9956 | -53.01478 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4605636-f708-3a54-83d8-d995efd51542 | -3.61656 | -49.85243 | 2024-12-10 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75c7fc93-accd-3f67-89bc-b4565b1f2ad0 | -2.9658 | -53.72421 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ebaf80f-1b93-3c08-a038-d87419a79373 | -3.63355 | -52.67786 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 459bf020-70b6-32d3-9228-b33b17494968 | -3.76165 | -53.84747 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b3b441e-295b-3d9f-bd91-ad2e8700c884 | -3.46493 | -53.96546 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 046f2a8f-0632-36d5-9f12-32a81b6cc860 | -11.366 | -43.9052 | 2024-12-10 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 661cd42c-0843-3deb-93a7-a7f69b07f5fd | -11.74888 | -41.14343 | 2024-12-10 04:53:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 86a97f3f-e3bd-3dd2-bf60-af7de800005c | -2.98483 | -53.89153 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45efd9c5-1794-3467-96b9-c34aa3de4752 | -4.38342 | -49.83323 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2c59247-4f62-3e33-a5ef-714e086cf507 | -2.62407 | -53.36936 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 120b2b06-9102-362f-a5fe-bfba2524369f | -2.46383 | -48.3574 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd96f88c-a799-3a1e-9ad9-a64c7da9fe0f | -9.71712 | -54.88883 | 2024-12-10 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1168601-f1c6-3792-ba96-d42c933ba496 | -3.11117 | -54.02753 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b551fca8-fccb-3388-95d3-f3f70e8e3797 | -2.35434 | -53.86239 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 240fad3e-3174-3d77-b7df-296b985a36cd | -4.38862 | -47.76025 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 0e4f27e7-a7a7-3107-9aa7-e502cfe36dde | -3.48302 | -54.69751 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d172d86-18d6-3f54-9246-207f891a812e | -1.31829 | -54.94825 | 2024-12-10 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
