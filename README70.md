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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d273f9d4-f073-3d2f-9a01-2826c2b531e3 | -4.34337 | -49.77054 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dd3932e-02eb-3f33-a3f7-f00c37df12e6 | -2.81254 | -51.80405 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95e2b61d-b606-394a-9160-997962ddd7bb | -5.6253 | -44.83008 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f7c5c56-655a-32d4-92dc-70780f14df91 | -3.0918 | -54.56126 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 080ef64e-884f-3f17-bba1-255f6cc02bc7 | -2.25915 | -53.72735 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9af52085-1a6f-3052-b480-1b1ab840f1cf | -2.10702 | -52.28325 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb9e3381-5dcc-3f30-ad09-7c670ed9e4ee | -2.11467 | -50.15421 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3abe08d8-57d4-36e2-a306-3955b0b7c6ee | -1.34551 | -51.40717 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb5dd5ed-6e63-3202-b8a4-7844095bae31 | -1.22371 | -56.17148 | 2024-11-09 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89569e3-95bc-365a-bead-fd171f44ab77 | -1.6268 | -52.24099 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e64231eb-1676-334b-a898-0575b87a4ee3 | -2.96694 | -53.87397 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73b99dcb-6328-3fe7-9984-6897283b66ff | -6.2775 | -44.73734 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8968b7f1-6593-3eb8-8ddf-65f3e1737cab | -4.07071 | -50.01249 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5744895e-fe31-3978-ae80-4720bdb036b8 | -2.25228 | -50.41355 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c8992c-e4f2-3868-b1a3-2470893333b4 | -3.70767 | -54.35039 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72cbd2ae-4c10-3c66-b183-6a3bfd9ddfd4 | -1.21805 | -51.75719 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfd2896e-cb8e-3333-8deb-34f1c83935eb | -3.70433 | -54.34984 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e39b535-1206-3bab-9d9c-5dc70cb88b84 | 1.16485 | -52.4532 | 2024-11-09 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3648a188-f9c8-3738-8833-1642396e6480 | -2.33493 | -48.86093 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c41d9ea0-838a-323a-acf1-6242e052d0a7 | -1.36524 | -49.35448 | 2024-11-09 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31600fac-9b7b-314c-85d6-066bd19b12ae | -2.6222 | -46.16384 | 2024-11-09 04:55:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff44e731-ccdc-3978-a137-617d68af1661 | -1.59859 | -53.32604 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34889fcb-3847-3bec-ab81-c03ece019ea5 | -1.16895 | -54.15636 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4907a155-9ad2-350b-81dc-7502d1aaafcc | -2.6215 | -51.91443 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43499885-7a59-3820-b32d-abe01141b8f0 | -3.24264 | -51.30442 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5916bb3-4877-3705-963e-346139ca8f6b | -3.26185 | -51.01244 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 870ac2a5-dec6-3311-9403-9efe7ba049d8 | -2.17302 | -46.43901 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb3ac30d-b017-3058-a707-c96a6cbf6f34 | -3.8946 | -50.08501 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1b14b4a-bbb9-3066-af96-047e232e9f06 | -2.49295 | -47.22584 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f214ec76-5a2b-3de2-ba4e-b02704094c6c | -3.15168 | -51.12483 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13369e19-11ec-3144-91a3-cbf5d4db617c | -2.14296 | -50.13765 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a80a1fa-8902-377a-88d2-4a2d3473cfce | -1.67057 | -50.46612 | 2024-11-09 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8650c981-646b-3d4a-987e-26cea496f899 | -5.17702 | -44.00335 | 2024-11-09 04:55:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cb017d4-a38e-31c7-8b75-a91f9d59514a | -2.69067 | -51.69325 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdae7233-1dfd-3e34-a14c-6cab89d27bfa | -3.04882 | -50.37073 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7ed1f7-bc69-3c0e-9021-49ebe3471b50 | -3.16979 | -49.09841 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d5ce833-d4ff-3e3e-89c0-6951755620d9 | -5.13525 | -60.36241 | 2024-11-09 04:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6992745-31f5-332c-8304-7104cc7edeb5 | -2.98477 | -51.46055 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b0c62a2-4116-36c7-8d49-ac24b3c90ee8 | -2.92669 | -49.35386 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da137fd7-cf1b-3591-9405-de66827b76ae | -3.04818 | -50.3748 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74bcec87-ab2d-3d54-97fb-c15d90a5ad5d | -2.68051 | -51.82461 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b628fe6d-69a3-3fc9-a45b-120c7185e3a9 | -2.23317 | -46.55913 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58febadf-a665-39ea-9382-59091e1c1997 | -3.23835 | -50.44764 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e289282-6a20-3d75-b9a9-d4e37f72ced1 | -6.27651 | -44.54027 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 124049fa-e973-3bb1-9084-f9dd1c4c29ac | -2.80191 | -51.49322 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cce30f0-e9b0-31fd-b219-78a60fe09c42 | -2.27635 | -50.67392 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4424cc20-c855-3e12-83c3-8a1e8c515ede | -3.03605 | -50.41816 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b174a7c-48c1-37b3-86d2-a170f6e3328e | -2.6112 | -51.7737 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf0d33bf-7715-3f3b-975b-9bd4a71b04c3 | -2.23485 | -46.61734 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 657c4ab4-7e08-3e35-a722-f268c2b066e9 | -3.2203 | -53.10351 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe3eb9d2-8fa1-371b-baf2-167d9c652cdc | -1.9417 | -50.67225 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fb8741d-272f-33d5-bc99-f530ba0e909c | -3.3924 | -51.24247 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e094de67-4dc5-3f18-8203-4d94e9cceaf8 | -1.23205 | -51.75574 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dca9449-ea59-393a-90c1-61fe66105470 | -3.17324 | -53.85283 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6cb95113-ef5e-379f-95cf-79b887e09fbf | -3.23575 | -50.2751 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 139a205a-501f-3b95-9963-cd59666495da | -3.2791 | -53.67802 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a5a2be0-258e-3824-a6bf-62d300b34f48 | -4.31501 | -48.6521 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37cc3094-fc4f-3191-af71-a71478338869 | -0.21723 | -51.62854 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f84b08b7-ad77-3176-bf7f-2501f9ffcf85 | -2.84704 | -49.4465 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8193a1e4-7c17-33bd-948d-a61412d0d0eb | -1.73841 | -52.69197 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ab3434b-7829-3a81-8369-f71aa47cfd83 | -2.93463 | -51.05038 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 070e4843-6394-38d6-8c91-ba2d4f88182a | -3.48515 | -50.80621 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65797e9a-3d67-337a-979f-34802d6fc445 | -3.47914 | -54.67635 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 116bb2e5-6de7-3ed9-bf02-8071ebdc0fd3 | -1.41442 | -54.76368 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa657f95-b891-3b61-9118-42632de72240 | -2.18747 | -53.73402 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aed62c39-960f-3873-9581-11928494a1cc | -2.92072 | -51.04825 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c26bcd59-f382-3e1d-b377-237637940399 | -2.87083 | -53.96864 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49d88798-c8ef-3b7d-a4a5-76601f05bb21 | -2.19131 | -50.52575 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44c72830-dd80-33c7-90cd-bfc6debc963f | -6.23487 | -47.28346 | 2024-11-09 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 391c8028-e3c7-37c9-a7b5-073681d8e016 | -3.47735 | -52.62785 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cedd9816-f859-3302-89f5-ac49b9d67219 | -5.46479 | -43.65108 | 2024-11-09 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7224f835-b0b3-397d-8824-bd6ef2e295bd | -3.04283 | -50.37343 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 139c4ebb-e505-3aa6-b3b8-2f88a1817646 | -3.22304 | -50.63364 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1948a588-2d82-3b48-bce9-3c3eca049af8 | -3.76809 | -51.38226 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4938fe4c-8b64-39f7-9b06-1675a43efd38 | -2.91771 | -49.36187 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d6d0834b-47e9-3e79-8728-d8c6654f3ee1 | -2.04682 | -52.08368 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e80473df-aa6e-30cc-9e45-286f39103cfa | -2.93119 | -54.12148 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe567b0-5e70-3903-93e3-720c282c6d49 | -2.27136 | -49.15003 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c118300-5091-3d33-9852-0d15c7421db2 | -3.04455 | -53.27422 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bb9231c-ab8d-3afd-9dc0-54811937fef2 | -1.8813 | -52.17352 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dc2c0e0-bf36-3854-9636-d21756212dfc | -2.9586 | -53.86203 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4936237c-8e43-3b12-a8d0-832878190f85 | -3.75317 | -52.4011 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 172a9b1e-1e81-3af9-b61b-3adf27eee5f3 | -2.75944 | -53.21513 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bf01649-b9d1-32e6-873d-a4eb10f67d74 | -3.34313 | -49.93953 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83406c4d-d878-33ef-8ddb-00ff298e8f97 | -3.58933 | -50.2784 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4d0e36f-fab6-362e-9aad-682f88d1ed2f | -1.1998 | -53.91871 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2054482d-a8f7-3ad2-ab0a-f9e191e07a61 | -2.30223 | -46.74485 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0acae823-6897-319e-a61e-fb42eb7a0bbb | -3.94953 | -48.15816 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3878d7bf-b275-3cc4-bdcd-c58199afa710 | -2.58467 | -51.92001 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb24f4d2-7f97-337a-bba1-c4c44c09db38 | -2.60124 | -54.02304 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32d13289-3c77-30dd-b86e-59fdb6e4482d | -4.06734 | -48.28916 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fc2b1fb-90b0-36e6-a3cf-6659a7c249c4 | -1.49809 | -54.06295 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a67e4361-2995-39f4-ae4e-8160b836d491 | -3.34691 | -50.25665 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ea3e618-8273-3ec7-8284-8812e3bcfa27 | -4.11322 | -48.50554 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5e065e2-f801-3620-abcd-c443092a02fd | -2.17961 | -53.69728 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f26964d7-77d2-357f-b4ee-1de631658346 | -2.67863 | -50.96183 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a10ffcc4-5128-33ce-991e-d98c8d062410 | -2.58004 | -49.1302 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1c4aa9a-db31-3e13-bbc1-a22ea54f9aad | -3.64912 | -50.13029 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a987b4c8-9e0a-373a-bc0a-64d375443a70 | -3.21298 | -54.05473 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6746c1e9-0eb9-3dee-b5a1-bdfd47d1fc8e | -3.76616 | -50.78056 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README71.md)
