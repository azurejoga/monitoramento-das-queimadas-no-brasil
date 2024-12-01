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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bf5cb58-c5e2-308b-8a33-35e3042543c3 | -1.7064 | -52.76613 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11d667d1-0c88-39d7-9d6c-4991f6ba3c94 | -4.06861 | -46.68053 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de561124-0bde-3ec1-85ab-e1aec25ccbdc | -3.88754 | -46.40643 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3f8a64b-e6ca-34c9-8311-b84990b0eff3 | -3.80374 | -52.14161 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edf77e25-74f7-3e11-ba4d-e31324d17e8b | -1.26523 | -51.58884 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb430281-026d-3c5e-aa13-116ba0e25e7c | -0.88031 | -53.6842 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cb5ca09-9320-3d02-b89f-80eb591e1ff7 | -1.49026 | -52.44107 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97683ab4-2de2-3c6b-93d4-4988483cb83c | -3.1247 | -53.25796 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc298d69-7648-3067-80c4-b41279e61fa7 | -4.08216 | -50.02345 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c650a1ba-7d86-36bf-bee2-470026e3bc1a | -1.43425 | -52.77136 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b74ab51b-757f-3629-9c62-e588c02a55a4 | -2.95979 | -53.72507 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35c7cc66-0e47-3d72-8a61-fc863be322b4 | -2.80319 | -54.04254 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba5e4654-f383-3f63-9124-9595e664bf59 | -4.89646 | -41.32101 | 2024-12-01 04:44:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5760a78f-f20a-3ec7-8ea9-48d096f55bc0 | -2.71558 | -46.13074 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b966d298-d320-3383-ad78-80e90010fc24 | -2.89483 | -55.22903 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 168e5a1e-9149-3639-bf29-00ed5f0804a3 | -2.62222 | -51.75302 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ec04b2d-04d1-38ce-9e52-ad6f59dc7b5f | -1.28719 | -51.67142 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03936e5f-43f7-340e-9b2c-b6d282f489d9 | -3.02732 | -54.01902 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70de6dea-187a-3144-84ba-87dfb1596f6c | -3.60292 | -50.37713 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b055807-5925-31bf-84c4-f9bca6126b12 | -3.75226 | -52.26578 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bbda790-63fd-31ee-bf72-d249d1f46203 | -1.29065 | -52.10963 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90d460e8-8ae8-3f2a-b76e-aa70f54d06c8 | -3.73067 | -54.23031 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4d38e49-6c6c-3d5e-91b6-e05d3903d6a0 | -3.10003 | -54.02157 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c26353f-e0c3-3081-869a-2b4f280995a0 | -0.99787 | -51.71525 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2523f1d-2f0a-3d43-8f7d-cef753e0c213 | -2.83393 | -46.85522 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8486a27-eff6-3e64-be40-a6bbf013629f | -2.46685 | -46.57106 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01ea7d8a-c428-3141-967a-d5dfd0e984af | -3.85711 | -47.05634 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a5615f-7d14-3002-8926-d3b1c2990c8c | -3.50613 | -53.83018 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2db9c1cb-fdb8-361c-bef0-7b84e804ebd4 | -3.31874 | -50.14165 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ae28912d-0438-36a8-88b5-476098559d04 | -1.09435 | -53.64798 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4a2db692-78a2-32a0-9008-8acec96befd7 | -2.64962 | -46.57933 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f9e795b-635b-31c5-a743-14c97803e331 | -1.09876 | -53.40278 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c5bce6d-f604-3b2b-8cf1-150ded3f51af | -1.97266 | -52.15105 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a446d81-2763-3a51-97fa-a704c29d8c0b | -1.18415 | -51.77369 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c970a79-dc11-337f-b6b3-7466efa997d0 | -4.14605 | -48.23811 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cfab228-da03-3a4e-b2ae-d41952857ff2 | -4.31773 | -46.53967 | 2024-12-01 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aab7f56d-d69b-39d9-adde-cad7ad4137b9 | -1.45099 | -51.49783 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08e053a3-4496-36f2-bc74-71ee2e538baf | -3.65446 | -50.22255 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4419d3b2-05c2-3b6c-b4d7-747308a0682d | -3.18804 | -45.35403 | 2024-12-01 04:44:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f90e8e1c-ef54-311c-bc03-a8e6127af815 | -4.17693 | -48.61805 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d314eb1a-34be-3622-bf42-fe1d53200fc6 | -2.87058 | -53.98385 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ca96021-820a-3afa-b3a3-ede3e2868621 | -3.50173 | -53.83396 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 77ebef8a-bc98-3101-b95e-7c104d18e928 | -3.31384 | -53.86947 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2931f838-a54a-34a4-972d-ba5c5fe9c9cc | -3.32206 | -50.14217 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d5bc925-5b67-3a72-9fad-1744a185cc28 | -3.50952 | -53.78624 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ba5c144-bb35-3147-a5a3-7d46617332c4 | -1.15632 | -51.70461 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0511a819-dd60-3aa4-ac28-687ebed3e686 | -4.25931 | -50.59309 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 677661bc-9017-36cc-8463-1df078ae0688 | -6.63825 | -47.35016 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f36d201-69dc-39c4-bfec-dbc29f3c154c | -4.07235 | -46.68113 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4915f1aa-48d9-3715-9dea-4df6d1b1b4aa | -3.68603 | -50.23808 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 534b0959-f32d-3022-ae87-f87816992420 | -6.14841 | -52.04676 | 2024-12-01 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c12d22d1-67fb-38c1-a480-2c95907d686b | -4.55125 | -43.30281 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 1cfaeefd-bb3e-3de1-83e5-3f16ef606d93 | -5.5856 | -45.21132 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 789cc557-dc55-3d0c-ba2f-b6d492f3ce87 | -1.61949 | -53.88976 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e692addc-46fc-3a29-a9a2-11dc237af634 | -1.84895 | -55.61634 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccbec286-39fa-3457-95e5-b8fd4a70f81b | -2.38822 | -50.48698 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c857bc8-c246-344d-9a9f-143b431c0f4f | -2.00026 | -51.18232 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1be1c10e-18a9-3800-af33-01ffeaaf76ea | -3.07757 | -53.80477 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f85c6081-c7e4-3f37-af68-df54f9293f36 | -3.84231 | -50.08551 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c140ad65-868b-3cac-be60-0d1e2d085339 | -3.97235 | -49.96732 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbbc7425-20bc-3ce9-b6d9-744c06235123 | -2.12228 | -50.60534 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48b06c9d-826b-3ef6-8988-4d2ff11e0e3d | -3.79545 | -58.97617 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e55560b-aea0-359f-b319-5d1cded6ff3d | -1.06401 | -53.22542 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be0d662b-569c-3695-97f2-04ec21f133de | -3.25339 | -53.6444 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 613ec425-d9ae-3e7f-976f-7fa31e6ea374 | -1.20317 | -51.74236 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3692b59c-622a-363d-b8b9-7b6fc5ce8f2d | -3.3131 | -50.50124 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 405642bd-ebc4-31e8-a66d-138473add26a | -3.25581 | -53.86684 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaeaee87-0178-3b44-a5e5-416136bcd532 | -2.02955 | -52.08265 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 162b742a-7093-31a5-9aa4-50a152aeebb2 | -3.28574 | -50.63147 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf90f20c-cb4c-308b-b8d6-9c562b792b36 | -3.73663 | -49.93793 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf16c883-f31a-34af-a9d6-84bd89bbf135 | -3.41388 | -53.22438 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d890e909-cd57-3052-8389-4e2ba2d585ef | -4.18036 | -48.61859 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d0ab215c-cc84-3250-92ed-0990b53a1673 | -2.61585 | -54.0785 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c878855-5fc1-3140-aef0-5d3b79826e76 | -2.79399 | -54.12786 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6096d49-5f66-3d6b-aea7-e1b193c86340 | -3.86145 | -52.39318 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e393a8c-3f51-3edc-b327-cba79840564e | -2.67649 | -46.60129 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 875aa122-c74a-310e-818d-666a719b58ae | -1.0894 | -53.20775 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b63cf1c-67db-3914-bd01-0f59eda578ae | -2.87855 | -46.80349 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b7a9ac0-bfe6-3a24-9c76-ac8ed02e8cc2 | -3.73312 | -49.87348 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 069ae0eb-5d7a-3ad7-9b2f-76258300c663 | -1.41282 | -46.59623 | 2024-12-01 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b40e278f-aabc-3801-8aa2-63589aa473ca | -3.36273 | -50.05656 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bfe04b5-d1b6-32b9-b044-c161be5b4eb8 | -3.86215 | -50.53773 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3f4c7cb-0379-3213-90af-941cee0bec7e | -3.0243 | -54.01394 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c4e243e-996f-3ac1-a16e-2aa1f32deb4f | -5.5849 | -45.21225 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 309779ce-4c88-3140-86d4-fd2ff558111e | -3.21643 | -53.12919 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0700aee-b971-3145-8011-db82b0b6e77d | -3.82495 | -52.25084 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5473074-da68-3acc-a2a0-4d5c786a4bdf | -4.45451 | -56.18053 | 2024-12-01 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccaff4b5-ff5f-3b95-bf83-923d4268fc47 | -2.80268 | -53.05537 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b67baec-7029-31c6-82e5-69a57fcaf5fc | -3.74132 | -51.83366 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1da96b81-a086-365f-a5d5-dae7926bf9d5 | -0.25977 | -51.5 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f745861b-c1c3-3434-bf91-106fbe358294 | -3.6159 | -51.36902 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce4d1ea3-5704-3c1b-a4dd-da8a3ef019ed | -1.48232 | -52.67558 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 153ca063-40a4-3879-b960-f4ff6bbd8be1 | -2.51173 | -51.83291 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0342ea79-58db-37c2-b2b5-2ae1e1f5dab3 | -2.37894 | -53.67891 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bed1bea1-dcbc-300f-8e4b-0783e1d952e9 | -1.07066 | -53.23117 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2bc3635-aa3e-3e46-bf06-d0fd610cac63 | -3.49055 | -53.80972 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad45c32f-affd-3e27-8015-06666a3f74e6 | -3.77216 | -51.61829 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaef28ba-201e-3f18-92b6-17be519ac0e8 | -2.47491 | -46.56782 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc0f8feb-569f-35cb-81ff-9d43ef4207b5 | -3.35139 | -50.15028 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5ecb445-76b0-345f-a08f-83cad5dd82e1 | -5.72834 | -43.98248 | 2024-12-01 04:44:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README43.md)
