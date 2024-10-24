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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ea14cef-20bb-356a-8049-f92d7a33a7d8 | -12.2754 | -47.6473 | 2024-10-24 13:06:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c55f4736-88c8-3160-b993-f904f6c4ca58 | -17.0207 | -57.3743 | 2024-10-24 13:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 471ca382-b7b9-319b-9f9f-02b85344f19a | -17.0011 | -57.3766 | 2024-10-24 13:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| d39ffbc7-0973-3c70-8d28-9c9047ca5824 | -17.021 | -57.3538 | 2024-10-24 13:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 12dd123f-a24f-3270-a6f9-cc6dd37f7a2a | -16.9596 | -57.5245 | 2024-10-24 13:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.4 |
| 6c049f2d-f109-3532-b358-877e66153afc | -16.9792 | -57.5223 | 2024-10-24 13:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.3 |
| 4b7cf7cb-9e58-3466-9901-7cd5987b8bd6 | -17.234 | -57.5131 | 2024-10-24 13:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 756a14fd-e55a-3ad2-bd2e-0c0fce35bd32 | -17.8427 | -57.5636 | 2024-10-24 13:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.7 |
| b394a843-bc9e-3e14-9264-46fbbf86f53a | -17.8423 | -57.5842 | 2024-10-24 13:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 157.3 |
| 00f14412-8fa5-31dd-93b9-8b0f2ac63b20 | -17.8229 | -57.566 | 2024-10-24 13:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 90c060af-8bf5-3de2-935c-69c3381fcfa8 | -17.8226 | -57.5866 | 2024-10-24 13:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| f34209f2-cba3-3e92-97e1-979988dcc57e | -18.3019 | -56.1386 | 2024-10-24 13:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 60dacb41-71ef-3ba5-a32e-62503e3ef364 | -18.3004 | -56.2222 | 2024-10-24 13:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 0caf25a0-ce8d-3808-b1a1-716e1476f5c2 | -18.3199 | -56.2404 | 2024-10-24 13:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 3f4d06d0-2e82-3eea-b875-14e07d3cc1ac | -18.3203 | -56.2195 | 2024-10-24 13:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| ce29215c-48b4-3eea-9032-79643488c5c3 | -18.3 | -56.2431 | 2024-10-24 13:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 546c33bb-841e-3e9f-b9cc-c5de9c480942 | -18.3207 | -56.1986 | 2024-10-24 13:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| ceb70c11-fa47-30a8-91a4-a786cba498c7 | -23.8366 | -55.2894 | 2024-10-24 13:07:18 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 102.2 |
| 5e65d639-65f9-38aa-b68c-c5e434c2a65c | -4.0731 | -42.8871 | 2024-10-24 13:15:29 | GOES-16 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 75fa9714-939e-318d-910d-3f41c40dfa00 | -10.6912 | -50.4952 | 2024-10-24 13:16:07 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 999ebe13-bc6f-3973-9ed3-4d2e19d13809 | -11.9028 | -43.8348 | 2024-10-24 13:16:13 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| bc551da0-69d5-33b9-a56f-192bed5c3754 | -12.2754 | -47.6473 | 2024-10-24 13:16:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 03fa4aa5-f05e-326f-b810-ebd4cee084ca | -16.9596 | -57.5245 | 2024-10-24 13:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| ccd4b440-5aec-37af-bc01-038350f67309 | -16.9792 | -57.5223 | 2024-10-24 13:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.1 |
| 55da2614-423c-3704-af4e-858832c33684 | -17.234 | -57.5131 | 2024-10-24 13:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 5e497794-868c-300e-82ad-2046c8088c18 | -17.8423 | -57.5842 | 2024-10-24 13:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 171.5 |
| 8d2f0bde-0cca-3fc2-b74f-4fc919ba0db4 | -17.8226 | -57.5866 | 2024-10-24 13:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.5 |
| 53041f16-18e4-336d-9308-6816460a9d70 | -17.8229 | -57.566 | 2024-10-24 13:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.3 |
| e6567fe5-c1c9-3af0-b3be-3d66a19591ba | -17.8427 | -57.5636 | 2024-10-24 13:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 295.1 |
| b0df170d-29a1-33e2-981c-48a3dd3b14fd | -18.3019 | -56.1386 | 2024-10-24 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 52211944-6010-39d7-bbc0-cca8e0814bfd | -18.2023 | -56.1729 | 2024-10-24 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 817324f5-5ece-3745-828c-65b2565a7ee3 | -18.3207 | -56.1986 | 2024-10-24 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| a64fb65d-f35d-3007-a558-ae363c3a57c5 | -18.3004 | -56.2222 | 2024-10-24 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 1121f91a-ae8b-3e46-892d-c2f04d7a41fb | -18.3203 | -56.2195 | 2024-10-24 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 2375aced-191f-350f-9c06-981c1dc9ed8f | -18.3 | -56.2431 | 2024-10-24 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| b1010af5-f89e-3359-a7cf-f695339e49f2 | -18.3199 | -56.2404 | 2024-10-24 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 50ed77d8-a6c9-3e08-abdd-b11a9073fd6b | -18.3023 | -56.1177 | 2024-10-24 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| d4182f38-a854-35ac-b2ca-65d5aec6922a | -23.795 | -55.2753 | 2024-10-24 13:17:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 98.2 |
| 05b9a96c-1bb8-3df5-93cd-813d05e149f9 | -23.8366 | -55.2894 | 2024-10-24 13:17:18 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 112.0 |
| a313ae0f-1b20-3c25-b8b5-e988e55bb2be | -3.6091 | -42.3703 | 2024-10-24 13:25:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| d15dc324-0c81-35d2-81e3-0adde3f07f1a | -4.0731 | -42.8871 | 2024-10-24 13:25:29 | GOES-16 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| bdae1122-a74c-3ee7-9937-1f95660365fa | -10.6912 | -50.4952 | 2024-10-24 13:26:07 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 6acc71a6-4100-347c-859a-2248b1a652e6 | -11.093 | -51.5556 | 2024-10-24 13:26:09 | GOES-16 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| a892705b-0a08-3d45-88d2-2b9f0ffa2402 | -11.6863 | -49.8697 | 2024-10-24 13:26:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 862a627c-dde5-3652-9cf7-7688b897da3b | -11.9028 | -43.8348 | 2024-10-24 13:26:13 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 133ed835-2167-3a2f-a1b1-ec379e8aae28 | -12.0526 | -47.2538 | 2024-10-24 13:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 7927924f-1527-3b19-94cb-9712ab1e4dbc | -12.2754 | -47.6473 | 2024-10-24 13:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| e83051a6-3356-3bc0-aceb-3735addd48a5 | -17.234 | -57.5131 | 2024-10-24 13:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| bfb97dc1-80d9-3a9c-a5a0-d6bf43093815 | -17.8226 | -57.5866 | 2024-10-24 13:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.6 |
| 71a4dd42-7a66-37cf-a61e-4a507ced3db9 | -17.8423 | -57.5842 | 2024-10-24 13:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 317.3 |
| a4f65de4-a42c-3d13-9928-95a1c28cb215 | -17.8427 | -57.5636 | 2024-10-24 13:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 539.8 |
| 6a7ab02b-7ff8-38e5-a7f3-15756414f7a9 | -17.8229 | -57.566 | 2024-10-24 13:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 177.8 |
| 55b4c5d0-56b6-3dd4-9cdc-468c99cde3d8 | -18.3004 | -56.2222 | 2024-10-24 13:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 7433925a-bf10-3907-893f-aa06b0cdeb98 | -18.3203 | -56.2195 | 2024-10-24 13:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.9 |
| 525ea173-d745-3036-aaa4-e5feb97da3c2 | -18.3207 | -56.1986 | 2024-10-24 13:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.6 |
| 959befba-39de-3ef7-8e71-797dcfa4c022 | -18.3199 | -56.2404 | 2024-10-24 13:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 0715b0e6-0f83-3ea2-bcb2-0b20ef000fe6 | -18.3 | -56.2431 | 2024-10-24 13:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| 525ac61a-b2e6-3940-b3c7-fc62bc30e17d | -19.6465 | -56.7051 | 2024-10-24 13:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 68c2a943-aea5-3c0a-b4c4-1d7fdc60b5e0 | -19.5677 | -56.6324 | 2024-10-24 13:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| cf468661-d96a-33b3-ab46-b51ef96e1487 | -23.8366 | -55.2894 | 2024-10-24 13:27:18 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 100.0 |


