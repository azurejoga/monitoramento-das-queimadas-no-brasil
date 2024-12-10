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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2426ab37-c976-39b8-99b8-985f5d8daccd | -1.70598 | -52.60985 | 2024-12-10 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e95a582-d573-3c09-af63-4cdc62ef37f2 | -3.1858 | -54.33317 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a28f866-96cb-3314-a3b4-29636748323c | -3.68559 | -54.32034 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27be38e0-c00a-3979-ac51-c18eaeaeaf4b | -3.08851 | -53.35597 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e032bd4-1b4c-34ba-b0a7-dd33f082113f | -2.80601 | -53.06476 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf6f3c54-b49b-3b00-9edc-ae555e803d89 | -5.70995 | -46.54375 | 2024-12-10 05:16:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0d20d3f-6d3d-3e86-95df-fde8d001aaee | -4.39469 | -47.75655 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 670d3127-3345-3b00-82d3-f0cc74837cde | -3.05733 | -54.24389 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0fae22c-561e-34e4-8256-e0f2892a8eaa | -2.99067 | -53.02165 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97f242a1-3189-3c6b-b148-69d70a630db7 | -3.37208 | -51.1921 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6532fc76-1155-36a0-ae4a-7361375b4797 | -3.43604 | -50.15249 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43c67779-3372-3484-838b-95e949831980 | -2.99607 | -53.04099 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d258befc-64c1-365d-94ea-bdc988a756b7 | -3.39404 | -52.66768 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a47c3c27-4a5f-3290-a9a7-18c2350d0562 | -2.99553 | -53.04454 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34be2eae-16f2-3640-8086-029f994b23b7 | -2.78354 | -53.24114 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 712de44a-79e6-3ba8-9732-da71bbc52103 | -2.62037 | -48.05574 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6387e58d-f30a-35d2-873f-fab747561454 | -3.06851 | -54.24329 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 448fa8ef-fe45-3e43-b141-5e2efae4e9ab | -7.59846 | -46.63865 | 2024-12-10 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1d9502a2-52ed-3180-afed-f0b3a20068a9 | -3.29658 | -51.63111 | 2024-12-10 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3dbc360-334d-38c7-b4bb-9d0fab068769 | -1.72931 | -52.48386 | 2024-12-10 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4b9a57a-91c8-337c-96b2-5b8a15ab651b | -7.59176 | -46.63777 | 2024-12-10 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 275abccd-16b5-3a57-97ff-90b421b8b49a | -2.17438 | -53.65409 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cca70f5-8a25-39ac-85d3-490e75c7e7da | -3.61243 | -50.56977 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3e82601-17fe-3d7a-8ed3-a55e8d1ca162 | -3.10025 | -53.2543 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bb492f5-3075-3da0-a8e6-678c221447e4 | -2.88412 | -49.01114 | 2024-12-10 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 256f9bd4-fa55-3e4d-8249-e2b3bae30dc8 | -2.81696 | -53.04812 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ff7795d-c8ad-3165-ade1-30304d9f04ff | -2.81752 | -53.04454 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99d662f5-87f7-3eb9-845d-6ac7b259d9a3 | -3.10947 | -53.24804 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 844b2192-4896-3325-a7e7-e62abda94884 | -3.11237 | -54.0301 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25d603b8-bec9-3013-938b-7bcb343f93a7 | -3.11361 | -54.07387 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60111115-d38b-3a17-aa2c-fa5624044585 | -3.5284 | -54.68737 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13cf3004-e862-38b7-89f0-0d3d1c86f881 | -4.03398 | -50.80444 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7af667d4-a6d2-322d-ae88-25a654a86ff2 | -3.52826 | -53.94314 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b6d768c-5d3b-351f-9008-6ce175f0201d | -3.21144 | -46.80714 | 2024-12-10 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 138943b4-dbb0-37c9-bc5a-e3395557c37b | -2.99058 | -52.85622 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa596d17-c45e-3eb8-932e-7235d1fb2abd | -2.95193 | -53.1114 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df615d67-6590-3fa6-8a53-c3aa99fad443 | -3.11816 | -54.06976 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83f26cf0-ee0b-37b9-ae28-287f277353d0 | -3.67099 | -51.31189 | 2024-12-10 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4b43e23-8eb8-3d33-89e7-58b564ceda6d | -3.8343 | -54.29958 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1d20b2f-04f3-3d6c-95b4-b196b9982a45 | -3.80981 | -52.26997 | 2024-12-10 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32dae31d-657f-322a-8ba3-7f55194fdb4f | -3.06025 | -54.24655 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d304ebfb-aa68-3d7f-96e6-ef5d2ddeae5e | -4.54605 | -48.0146 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 049afbf2-d4f9-3896-a135-07336ef8e272 | -7.79508 | -55.02134 | 2024-12-10 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fafadbcc-7c6e-392d-9008-b06e6e906105 | -2.58077 | -51.92196 | 2024-12-10 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de6fc411-a268-3611-8bf5-355133acb024 | -3.07512 | -54.08006 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 540849dc-fe59-35bf-b024-f0831d491c7d | -2.96319 | -53.72202 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e8b07e1-7c2d-3687-a48c-d7cfbd0ebde8 | -1.31763 | -54.949 | 2024-12-10 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 46713c39-ee78-3e17-acf8-24ea25c20255 | -4.07406 | -54.1128 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ee01f58-7dd3-32b7-9a02-70863e2b0eb5 | -2.81744 | -53.06969 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ef5cc5b-5d1b-3511-9a65-42a308a8c2f7 | -3.26344 | -53.87344 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1830a9d9-df54-3ef3-87de-b565f25514d1 | -3.35398 | -53.80454 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d63add0-b1a5-3b95-874b-326c6bc36aa4 | -3.11432 | -54.06919 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62023678-1abb-3bce-9f9f-0062e524d2dc | -3.1563 | -54.47673 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbf16ccf-26f5-3118-8aba-056718b86889 | -3.7885 | -50.95121 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f932f14-265e-3432-8476-d9461720e447 | -3.00017 | -53.04159 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b5cafd6-ff5c-336d-9b3a-e4ebec5ad3a7 | -11.65918 | -58.26952 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dcf801f-d9fd-3bd2-860a-c926fb479b69 | -12.85841 | -58.21608 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ba7d3b8-3e2d-3b4e-91c1-8232478f860a | -12.56333 | -58.35396 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be10f1ad-80c3-3693-83d6-f911eba58e91 | -12.85493 | -58.21555 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54141d50-2ba4-3e36-8f30-379401d1af6f | -12.54779 | -58.36337 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 10eb1bc2-7b98-30a9-8f82-6480717f1888 | -12.85436 | -58.21944 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab2d3444-0e1a-3414-b4c4-66ff33adc9fc | -12.53995 | -57.74216 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f26af53-f9ee-33b9-bc83-c5558eecc889 | -11.41662 | -54.31825 | 2024-12-10 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cf24a83-732d-3519-adce-cabd65a72cab | -12.36218 | -54.17166 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e779acb0-fdf5-3579-a1db-660220758d0d | -12.36767 | -54.16378 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15b85604-91c8-353b-8641-98d8f31cd2d7 | -12.049 | -62.79174 | 2024-12-10 05:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35bcfad5-861d-37ad-9465-1740b7a972d0 | -12.53973 | -58.34643 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 944f2b42-9371-3499-9bf2-262e1fd63294 | -12.557 | -58.34907 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2335b19b-7bb4-39b6-a695-9781bf511207 | -9.71551 | -54.89341 | 2024-12-10 05:18:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af6568f3-475d-30e3-836f-ef7963232758 | -10.35779 | -57.24816 | 2024-12-10 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 434b599e-6329-32d3-8e11-c4603c0f4854 | -12.56229 | -57.76204 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3664ce55-f76a-3988-aae0-c23ec1b3ab3d | -12.56504 | -58.366 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e360bb96-ed80-3c6b-8e0e-fdae3d660686 | -12.56824 | -57.76572 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32012a72-2760-3e6d-a506-0ecf65fa13da | -12.5334 | -58.34151 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 03bc0ddf-a89a-39ca-8f4b-11294afa16cd | -12.53641 | -57.74164 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bdf41684-d792-3634-9928-2e94c1ddf05e | -12.25096 | -52.44825 | 2024-12-10 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bd2e5e6-b4ac-3db0-b9eb-8fe303ebfb2e | -10.02657 | -53.74884 | 2024-12-10 05:18:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 46ff2772-bc74-37dd-aa87-a241b9aa936b | -12.56169 | -57.76607 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d3a5676a-d019-353a-9bf5-58f071ba91ea | -11.35079 | -54.29246 | 2024-12-10 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| deaf5065-64ff-3f5f-bd7d-22bbda7bdf8f | -12.90434 | -55.04961 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37f5523b-8679-3f1c-8358-6da9c9f28a6b | -13.75138 | -53.27798 | 2024-12-10 05:18:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dad360d5-edd0-396b-9b35-afd785771908 | -12.55124 | -58.34036 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1601ad2d-711f-3cbf-a16f-20bb97d058a6 | -12.56893 | -51.30658 | 2024-12-10 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29ed5a7a-68a8-3c8b-b93a-75867d4b50cb | -12.56045 | -58.34959 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 36cfe8e2-c8e3-30d6-b71a-59670462fa35 | -7.92617 | -61.55823 | 2024-12-10 05:18:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11586d94-e30e-3fc3-90ef-40be86131ba1 | -11.82609 | -57.82634 | 2024-12-10 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4f1b2b3-d64c-3850-bc15-1e8fb5c6325a | -12.53941 | -57.72142 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 949313bf-f19d-3996-b1f6-6450190e0f73 | -11.32062 | -54.04832 | 2024-12-10 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9aeb0da6-471d-313f-9305-3f8437aab621 | -13.48635 | -60.34749 | 2024-12-10 05:18:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1127a47d-8f97-356d-bd59-9b679d9ab07f | -12.3671 | -54.16803 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd49376c-a608-3550-b395-29e7dbb067ea | -11.78243 | -55.1306 | 2024-12-10 05:18:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b554f74b-ac19-3dc8-8186-8fbd3cb2061e | -12.54204 | -58.35464 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 74cfa999-1b59-3303-a4ea-e75a420abbe2 | -10.02484 | -53.74921 | 2024-12-10 05:18:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01ecc588-b59d-38a0-b05e-cc1197bf6e9f | -12.54606 | -58.35135 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9daf85be-2dfa-3018-a960-dc6b5c43437e | -12.56562 | -58.36217 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb21b31c-0fde-335d-88b1-cc8117413f70 | -10.67648 | -55.92563 | 2024-12-10 05:18:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29c597cc-fed5-35f6-a0fa-ca0c8e49bacb | -12.53232 | -57.72039 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 654bd8bf-d297-34ff-95b1-35adb8f985b3 | -9.3992 | -62.57384 | 2024-12-10 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2498735-38b0-3616-ab18-72e72f372133 | -12.55412 | -58.34471 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f48877ea-7c8a-3de7-949e-3ba5aabd2bdb | -12.56363 | -51.3059 | 2024-12-10 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
