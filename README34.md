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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5935ac4-54b4-3800-b8c1-f1b359034583 | -2.67514 | -46.2002 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f8326da-88b7-384a-8ce9-a41521ea2202 | -4.24037 | -41.93147 | 2024-11-17 04:06:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b5e55e2c-949e-3b5b-8da3-c6ad8bc19f3b | -4.14211 | -42.12634 | 2024-11-17 04:06:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af3cc60d-d0e4-3bf2-a5bc-0a5f2937eb83 | -4.29653 | -48.06615 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2593f44-de7c-35d2-9b85-ef4148a400f6 | -2.09746 | -46.45615 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7b8aab0-42a4-310c-b1bd-4735192724d8 | -2.67258 | -46.2157 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a630909-c782-3f19-8adb-15e2c94910b4 | -3.61621 | -50.14853 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a08cc1a3-82d3-38cd-be53-4f7a94d83c61 | -6.9906 | -39.65929 | 2024-11-17 04:06:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c028cc7f-ac7d-3331-85b3-c8578a852871 | -4.55905 | -43.20512 | 2024-11-17 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d3b81cd-4455-3382-8d77-0278605f3fea | -5.46432 | -42.15641 | 2024-11-17 04:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cabd8e69-8402-30f3-aa8b-f95068d60725 | -3.03992 | -45.75625 | 2024-11-17 04:06:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 558d6db9-a44f-3207-be6d-e1c63ed36b9c | -3.81055 | -46.51579 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c42b2852-fb95-31d6-8852-3e14b2ced61d | -2.6336 | -46.5583 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a8993d6-dc5e-3121-976a-ba6d2a6e5b2a | -2.61319 | -46.18283 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8faa695e-b51e-3af0-84d1-214ad2bc2f66 | -6.00064 | -42.63107 | 2024-11-17 04:06:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f6ab457a-e4d4-3fee-8207-d9f1cfb70130 | -2.25794 | -49.05181 | 2024-11-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddeb4e8f-d3ae-3d76-ab4a-f3ad4e77f99a | -4.44816 | -45.91095 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d16d2793-3001-3fa9-b65b-4e7d6f8a0f7e | -2.65528 | -46.21773 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1007fa8e-4560-3ea3-b8c2-79155b5c5efc | -3.58193 | -50.52818 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7a31f2e-651f-3ad5-a3e5-bda021c83ffe | -2.68166 | -46.21324 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d07bf447-a96e-31bd-b64e-7947d14c64ce | -5.11942 | -45.15348 | 2024-11-17 04:06:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1897bc1b-362e-3220-83e0-f31a01a5d6ba | -6.3841 | -45.68986 | 2024-11-17 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cf5a2a9-806b-3b4d-83a9-3d674db88690 | -4.2944 | -42.18354 | 2024-11-17 04:06:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 707cfc30-4b25-3c15-a005-1f9ed63b2b21 | -1.20843 | -51.78485 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e57956e-a037-3d13-bb74-a7d5b4aa042b | -4.3934 | -45.27716 | 2024-11-17 04:06:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 673f66f7-d980-32c6-a02d-4b48b5e48edb | -6.00121 | -42.62748 | 2024-11-17 04:06:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8a957670-02e2-3017-9936-6bb68800c35f | -3.69873 | -51.08036 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70940fe3-1560-3947-8475-4a5f952be211 | -4.14154 | -42.12991 | 2024-11-17 04:06:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b0918ef7-d6d3-3cb7-87d5-0f6363f10505 | -3.14329 | -45.98246 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc948761-f794-3ccd-854d-44402653e5dc | -1.62719 | -48.68345 | 2024-11-17 04:06:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fd5984b-758c-3211-b2b4-b1f00814b8e9 | -3.6746 | -50.10432 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3c944b7b-990d-3f53-a80b-ad77cf325303 | -2.62794 | -48.57169 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 10a45913-30a7-3147-bf6e-b75c241c18ee | -2.33058 | -53.56989 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78cbd921-75ef-3fe1-a8b7-8faef55cecb4 | -3.71074 | -51.84007 | 2024-11-17 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35412257-3bf0-357f-a932-0c9f839f51d9 | -2.70817 | -49.11749 | 2024-11-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 860dc599-930b-345f-8f59-877206e63ca6 | -4.28797 | -48.21417 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db376d44-322f-3b1e-9f0d-5e4e64ccd4eb | -2.1467 | -50.70166 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06334b4-4970-3148-a7ae-3b98655bed49 | -2.82763 | -46.66295 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cdadb94b-6892-3fcc-87a8-b870869ffade | -3.78226 | -43.91053 | 2024-11-17 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02262339-cee5-39eb-9301-89cdaa021259 | -3.52227 | -50.23792 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78874428-f78c-392e-89f1-9c9d5e1af454 | -4.44874 | -45.90746 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bcb1958-47f9-3136-8ea2-4dda893ae83f | -2.34821 | -49.12087 | 2024-11-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75788c23-4c16-373a-8550-da88e3a12cd3 | -2.98769 | -52.60127 | 2024-11-17 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b118f0c0-ac90-3814-90bc-80a8c6ccfb88 | -6.99003 | -39.66302 | 2024-11-17 04:06:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f3f583a-29e5-38f9-a13e-bd904a20b457 | -2.60259 | -51.79294 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| db444970-43f9-3b94-8eba-14f8aa2c590f | -3.46895 | -43.8857 | 2024-11-17 04:06:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77de5530-010a-3179-9d32-b30eef1a84fb | -3.81142 | -46.5172 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2fabb9d-9473-366d-9da1-1250bc1195e6 | -3.33323 | -50.4953 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8dacc01-42b7-3695-8ccc-e665079031e0 | -4.31075 | -48.60684 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f61a5423-bb17-3b26-bc5d-73cce11019c9 | -5.59032 | -45.20676 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7cf45576-31cf-3313-9dad-203b6f8bb065 | -4.22039 | -44.04234 | 2024-11-17 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 649c9a8d-9012-344d-84b4-7abcb7a543df | -2.62164 | -46.18419 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e123ca8-2c3a-33d3-8f9c-7bf91957e83e | -3.17516 | -46.5982 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 335d8248-3da0-3c97-a2eb-6284ba4f1a6c | -1.46093 | -48.19855 | 2024-11-17 04:06:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e348422-74db-35e8-a7a5-1332885913af | -2.67351 | -46.18393 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c40cfea-305f-3743-8334-116f84c563c7 | -3.53223 | -50.24651 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b0b93f3-6c18-31f7-a8fc-8c7ab416093b | -2.07131 | -48.53669 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6510b979-bb80-312c-952d-d5f8952929a6 | -4.58351 | -48.02539 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 027bbba5-e325-329e-a050-1a18a31321d1 | -3.89478 | -45.91643 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c9f4d0f-b233-378f-821b-182b7db4f18b | -3.33138 | -52.76773 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe3610c4-24ab-3320-97e8-fe6c4e71c38f | -3.91836 | -46.52126 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f3b43aab-36f7-33c9-a50a-54b4b2d5d877 | -1.68839 | -48.18099 | 2024-11-17 04:06:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6865702-5a26-3449-8965-8d05582f442c | -4.10051 | -46.87767 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea0d21b-4737-3755-8e4c-2ecaf7d0deea | -3.35476 | -46.06128 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27679752-32f8-3439-b885-670e7ac08d3a | -2.62581 | -48.55331 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0d34d81-f8fb-35a0-a993-63e2109ee7d8 | -3.56512 | -50.25238 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0c33645-b1f7-3586-9ded-a2cc63e69843 | -3.58043 | -50.52253 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2afb3264-8a5a-3c16-87bb-37280cf8a911 | -3.52051 | -50.24865 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aefd1b7f-6855-3bea-980f-2d851d89cb95 | -2.60483 | -47.55689 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c8478c57-310c-31e0-9f07-3827633145a4 | -2.2937 | -49.12786 | 2024-11-17 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf7b7086-a096-36c1-81f6-ba83f1f89cb0 | -6.49203 | -47.5008 | 2024-11-17 04:06:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e732ade8-cec0-36b3-822e-e9aa2ade28a3 | -2.60174 | -47.54664 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ddf4021-98b0-3839-b17c-aabd79de1742 | -5.87768 | -40.15363 | 2024-11-17 04:06:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 860b77c2-a4a2-3f64-8c2b-e7489042b98e | -2.61256 | -46.18673 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9d59f46-fac7-3392-ae81-5b7ecaf70320 | -4.91299 | -44.81265 | 2024-11-17 04:06:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd619f9f-650c-35c3-8d5f-d0ac09bf29bb | -2.59396 | -47.56501 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7612d4cf-d8cc-3d06-8ea0-749d9ad76cec | -5.35788 | -40.88169 | 2024-11-17 04:06:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2bf0296-2834-390d-8b39-18225de3a97f | -7.4761 | -47.18264 | 2024-11-17 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 605ddad3-c933-303b-aae3-4ea963844ffb | -4.02522 | -46.54919 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2327b282-90f2-391f-8773-321b9520f96f | -1.14609 | -51.69349 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d2f985a-fd99-3426-826d-b1a6f6486eef | -0.95388 | -52.41407 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b65c3c10-b180-32e5-9b3f-102ebeb17ecf | -3.62703 | -50.21901 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c7ba45d-b843-301f-906b-27c0beaefac1 | -3.03842 | -47.98784 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30174b30-8336-39e0-81f4-d8b4a20e12b5 | -2.66772 | -46.21885 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 19e6d47e-42af-3494-878c-05bf3a5f9898 | -4.66526 | -49.5181 | 2024-11-17 04:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd7d661a-f130-310f-a47a-f3e077e4a17a | -4.53696 | -45.25302 | 2024-11-17 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 01c0fdac-acc4-309e-8436-562756597f42 | -2.47503 | -45.62551 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad809a3e-75c0-318c-87ec-7017536eb0b5 | -3.62589 | -50.2252 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f286e135-b76b-3f45-92be-f06d1cbed6d0 | -6.17207 | -41.16935 | 2024-11-17 04:06:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6d9fd35-3926-3fdb-9924-30dca35bb393 | -3.56213 | -44.029 | 2024-11-17 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0219297-1882-38ac-84b7-73dcd4d16931 | -7.36064 | -43.53724 | 2024-11-17 04:06:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d260d2e7-0ded-37b8-a80b-574c812beca0 | -5.99726 | -42.63053 | 2024-11-17 04:06:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c7653d4d-2ed6-36eb-9e92-cc18ee2b77f9 | -4.10623 | -46.87001 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e13d3a7f-fc32-3314-b217-1ee2bd2eaeb9 | -4.33127 | -43.0461 | 2024-11-17 04:06:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e45caac-7ecd-36f8-91ad-30b4c87cdae7 | -2.63478 | -48.56129 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a0aa9e3-0c00-3c64-bb4d-569d93eeba9d | -3.7853 | -46.04712 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cadb0bbc-bb1c-3bb6-8e06-ed26decf1ab5 | -3.55846 | -50.25839 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa462ad6-9e07-3e4a-acd8-4188d9fa44d5 | -4.30511 | -48.07249 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d489a77-0d4f-3c36-9346-44a3af294c10 | -2.36369 | -48.53096 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bcfc557-9d4c-3ac3-93b7-4a647a6d34a4 | -2.32906 | -53.57853 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README35.md)
