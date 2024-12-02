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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3777e20-d801-38d8-9a56-4c1e3aa5b8fc | -3.12871 | -54.52944 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3eaa3796-5992-30f5-828a-1d09e53d8cfa | -3.50825 | -53.83081 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82569214-719f-3b54-8335-5afbaed4071e | -3.71885 | -51.79521 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21b327b4-b751-3268-9203-f37b99b6c8cf | -3.40361 | -50.23619 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80ad1042-bbd1-3c7f-a708-0637559b47c5 | -3.13403 | -54.53032 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85439638-3b07-36f5-8286-c3cca3e6e8f9 | -4.26479 | -47.61674 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3231837d-f09c-31a0-a7bd-d19e3fa8c750 | -3.2087 | -54.17466 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13e0cb3c-9047-3de0-8ad3-76ace6c1f7ed | -4.65918 | -45.65388 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c745e441-54d4-31d2-b060-3794bd29fd68 | -3.78224 | -52.03418 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f361b6b1-3a5b-3afe-8427-64e23c1fcc02 | -3.98864 | -49.71199 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4eefd93-7c59-3712-a6a6-37d1b02c2d08 | -5.58995 | -45.15306 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 159c433e-36ad-3696-bfae-0e66537c5f0e | -3.09753 | -53.74822 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efb1a3c5-1d63-3cab-a9be-14526979554f | -4.32627 | -48.09742 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af672edf-8aff-3d92-b411-e841b21d7ab2 | -3.93642 | -46.88988 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 549ac8b7-fb2d-3388-b64a-a6e30840ab5e | -3.1583 | -51.11892 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 103a350c-9486-3a91-b482-57e9c842eb1f | -3.17644 | -54.33746 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71558aaf-5967-38ee-aca3-240e4b3ab488 | -4.00353 | -46.6501 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a293496-ded0-3a22-b973-23472b2199e1 | -3.06875 | -49.48023 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 551793ed-d828-34f7-a482-44b228b391f4 | -3.25462 | -53.92204 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4789f8d-7a5e-320c-8260-46f78f49e8f7 | -4.6564 | -45.64991 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c657ff-0324-37b6-8ad7-26dfc2c0dc8c | -4.00182 | -46.65011 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc5c4ee6-16f9-392d-a27e-fe7c3a0d207a | -3.06573 | -53.81362 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e68f40e-73f3-3095-ab00-c291f496bd9b | -4.5579 | -45.71904 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c825b67-a765-32ca-b182-4dbfae006e1f | -2.90511 | -51.58127 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e7bea41-847f-30ed-99fc-e68022318783 | -3.47453 | -47.68663 | 2024-12-02 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52bba6e5-39cb-3245-8a32-af20882702f3 | -3.85306 | -46.53611 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74f3beff-2067-3325-86f0-1d77cc8222e0 | -3.87426 | -46.57539 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 490f6d0d-380f-36a2-aa87-60e3086777d9 | -3.27128 | -48.77459 | 2024-12-02 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2e3e118-4918-32f9-973d-3f40cf5040b2 | -5.17247 | -44.67158 | 2024-12-02 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a45acac4-896a-3c8b-af7d-a1c44af7c8ff | -3.8079 | -46.53988 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e6ed679-1bb1-364c-a65f-551f3bc34c25 | -11.06067 | -45.37395 | 2024-12-02 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a534b05e-80c8-3212-a76e-bdaf787fb9ca | -2.8569 | -54.06186 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65d2409f-eb21-3b2a-8e53-06c6851b0157 | -6.08707 | -48.05658 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2795e74a-cceb-31d2-b7f7-1888f8999a48 | -3.97617 | -46.66038 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70d7b22a-5f92-3b07-a033-6641c99c8b57 | -3.48416 | -52.10221 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64739d7b-4e21-3c25-8eb1-7c066811f8a3 | -3.28232 | -50.62862 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 271cd55d-94d1-3d2f-b4c5-c068536e0f29 | -3.46278 | -53.49386 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af2f2f7-8cf8-3364-a6f4-61be36ba0f4b | -3.06363 | -53.68086 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80d0eca7-7b7e-3fb2-b718-56a6d63962c6 | -3.36406 | -51.12763 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 915f7f8e-1f91-39fa-b993-2a5f24987250 | -4.87073 | -41.35419 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a9572be0-0f8a-338f-9e82-d61748957c53 | -3.25551 | -53.93061 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10d4ffba-6c09-35c5-abd8-46e23352dcd4 | -4.21068 | -46.37421 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e933cfc2-eb43-3951-baa9-bacfebc83dc7 | -3.65103 | -51.11709 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3da9bb71-eeb0-35f1-a184-1a2360bc9c2c | -3.9382 | -46.70492 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81f1719a-c6c0-34e3-b068-da9ae873de3e | -2.82778 | -51.83709 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 555bf623-04e4-3ef1-a1f0-e73d4b684afe | -3.82907 | -46.62238 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f249a958-fa97-3fb5-945a-d3bdeb394a0f | -9.19755 | -43.20403 | 2024-12-02 04:25:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed415c57-e05f-3779-8644-e7823812e6cd | -2.63598 | -54.19794 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 087bd74d-c33c-3260-91ac-4e170ff4138b | -3.97406 | -46.89907 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f237802-64f8-3fc7-b9ea-ea7d26326f88 | -3.82741 | -46.56813 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95412873-cfde-3ac0-9475-0bf2d1a4a312 | -3.97564 | -46.75074 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f541f19-2be5-3ead-9585-6ba62cde5eea | -2.78966 | -51.90339 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05791ca5-1ba1-3b04-8da7-acc7cffe8387 | -4.62238 | -47.91298 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d8bcb42-d97a-3967-bcd6-1ccf9c3340cf | -3.94434 | -46.68788 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96f491ee-7f63-3032-8fb2-2f3747aa1fe2 | -3.07132 | -53.81141 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1b9f98b-5e04-30f3-a546-2f058dbfbc39 | -4.52862 | -45.73216 | 2024-12-02 04:25:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb53dc28-dcc9-3a76-8299-3b7eb229ee60 | -2.90143 | -51.57643 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 256230fa-2707-3b58-9832-eddb3b92d360 | -3.33764 | -53.37817 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c463d7fb-cc3f-3c15-a1b7-75fd83dd6763 | -3.78266 | -46.69807 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81a2d6e6-31d9-35ab-a043-b9c80486563a | -4.18953 | -50.67006 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb6fc57f-105b-38e3-94e8-14b9bf257e00 | -3.74848 | -54.50731 | 2024-12-02 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb439fe9-5552-3e41-9bdd-a1976c56d814 | -5.05905 | -46.40099 | 2024-12-02 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9de8a8f6-8ef9-3b09-a413-b154d0174190 | -4.53351 | -45.70106 | 2024-12-02 04:25:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b3bd118-8e4d-3339-bd38-fe4e694c1787 | -3.24099 | -50.65444 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f338578-2b9a-380c-836b-b9320b679c62 | -4.32943 | -45.92413 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbd3dad4-4f13-3ff0-8d48-ff099416eb72 | -4.01374 | -46.99682 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce9bcc4d-b7c3-3699-a873-24b5c77caa9c | -3.64329 | -51.11202 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 216e2b46-18df-35fa-ad84-cc40809be954 | -3.81069 | -46.54391 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96853f79-ff8a-34fe-920a-0916d4784bd3 | -3.74672 | -52.26614 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b466015-3151-3abf-a231-19d65948b9fe | -5.20768 | -42.86824 | 2024-12-02 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9daa8c3f-b2e9-3d76-b883-d825d98e0738 | -3.83745 | -46.56965 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ad92eda-76ac-33f1-a86d-ae135f1a8bb0 | -3.9624 | -52.17854 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 622a157d-4cc7-3f97-9ec1-2365c5671b62 | -4.08841 | -46.13799 | 2024-12-02 04:25:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1244669f-75ec-39e9-a277-8565ae3641a7 | -3.50222 | -53.8358 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17c7e1dd-2c89-3d30-ba5d-fa223d4e2c03 | -8.83371 | -44.77797 | 2024-12-02 04:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3c0571a-4ea4-3286-bbf4-873ba97a858d | -3.93483 | -46.72615 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34839f04-8473-312a-9f4a-48a8a1c9e8ee | -3.93541 | -46.70087 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a525a6c4-0d0a-34e6-b78d-8a1ae904dcd9 | -5.93441 | -43.78733 | 2024-12-02 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32c4e0d0-039b-36ad-835d-9d844c535b9e | -4.77374 | -46.43053 | 2024-12-02 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15169369-119d-3fc2-bb86-72185fe54025 | -4.90521 | -41.33858 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e60a68a1-aab8-3233-8685-0808d131e12a | -4.3767 | -47.26339 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b899493-f30e-34e5-b006-411fc2107fcb | -4.19132 | -50.68454 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bfa328ab-edbd-3211-93fb-8936111f83cf | -3.45764 | -50.26738 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dda6386e-5cec-32b1-8df9-a2895d2a855b | -4.24824 | -49.19099 | 2024-12-02 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9e8f2b55-fd21-3aff-b8ab-3b31389f7d59 | -4.09781 | -46.12169 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab881b5b-d658-37cc-ad84-0b8f39e2e907 | -3.25605 | -49.90776 | 2024-12-02 04:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f77f720d-8aef-30df-8ee0-8e1a4eecb586 | -2.85136 | -54.19283 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b4695db-4482-3eb9-ad68-3454eabeae20 | -3.78209 | -46.70163 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4f34bc0-adc7-32e7-8f53-e41fefec55d9 | -3.54491 | -51.02674 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 333d46dd-f057-3c0e-8705-8f9bcfdc2619 | -3.72188 | -52.27649 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d54598ca-04f4-3d44-aa74-8bbf63b04ee2 | -3.83076 | -46.54703 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3640b1f-cad1-3d1f-8d5a-94061303d664 | -3.55191 | -51.45277 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d109089d-789e-3486-be04-f942ad3a19cc | -3.21389 | -54.17553 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eec91268-8a46-3d2c-9342-0d908392d4ff | -4.84998 | -50.49473 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8245fff-8c88-3495-85ac-f2340b317eee | -4.06716 | -46.68166 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 065f0a06-4e73-3795-bbe4-3d5bb7b6f72d | -4.0761 | -46.69025 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aa8de55-601e-3b78-b719-e1ca85a89bd8 | -3.25133 | -53.62575 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5e953e4-3040-34bf-93a3-0d142181769a | -6.40486 | -47.21332 | 2024-12-02 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57be0b62-4dbc-3b72-9cc0-0d19646b00f7 | -3.93205 | -46.72206 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 953c8e56-860d-3501-9735-8d3b26be421b | -3.50104 | -50.32648 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README41.md)
