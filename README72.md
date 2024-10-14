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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3715e33c-0971-3a05-a7e4-f01e15aee4a1 | -8.32708 | -42.74211 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 936ef970-5d34-3869-a777-dda2822a9ace | -8.32666 | -42.74519 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 19dedcf2-9d6a-33b4-918c-14f8ec367aac | -8.32624 | -42.74826 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5be78645-0f72-37b9-9890-27c72f45590a | -8.32278 | -42.73511 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6a00473-ef54-31db-8293-e1b9f222350a | -8.32235 | -42.73822 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8e4546ea-8dc0-3458-bdae-e3c1a4c46ceb | -8.32193 | -42.7413 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7ef72065-9b59-3b50-be4c-4e71b12b077a | -8.32151 | -42.74438 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 30aa433a-0851-3e0d-bf3d-33c9e553ebc0 | -9.4554 | -44.14706 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5d2e73fc-ac13-3136-8c42-48907814a11c | -9.45252 | -44.16768 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b966da65-0524-3f14-9d4a-3f80a124f90e | -9.45138 | -44.14109 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d67b3ca2-5d00-3df1-9fd3-6e19fca3f3a4 | -9.45102 | -44.1477 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 33eca924-e35f-328e-ae52-fb62f585a6ed | -9.4485 | -44.16179 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4389bc8c-169c-3510-a66d-36e3dd3ca42d | -9.4483 | -44.16837 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5d04b309-433e-3789-b9c5-8ba0d67dab63 | -9.44779 | -44.16689 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00a6409b-c914-35c5-a737-548ff88a86d9 | -9.44708 | -44.17199 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f52e1201-68d6-3779-a5f9-250e6d8778cc | -9.44695 | -44.14171 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 657876da-d0fc-3501-9970-6a80855bbe6c | -9.44664 | -44.14029 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7818b493-47ab-30d8-8f90-f55bea5b5b5f | -9.44559 | -44.15211 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 83c59ef9-08c8-31a5-8d28-12b20b229c25 | -9.4452 | -44.15063 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 42806160-ae67-3c6b-8133-1d83207cfc7f | -9.44355 | -44.16761 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ff80a2db-44fb-375f-b0fc-42065e2fa625 | -9.44305 | -44.16614 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27e70ef8-2871-3348-ad81-bf383313894e | -9.44288 | -44.17273 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7a0de2d5-2a16-3830-815d-004ca95d43ca | -9.44256 | -44.13473 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 50dc6e71-21be-39d9-b2c0-d8af942325f0 | -9.44233 | -44.17126 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1dc39a56-89f0-334e-9c88-3bfa1a4622ea | -9.42807 | -44.1693 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 380599a8-94e3-33d6-a7f1-2b4a652a2046 | -9.42615 | -44.14809 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3a3f3be9-216a-367a-a5d1-7028c7c7a41b | -9.42476 | -44.15823 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a144bfa1-bca8-31d7-9d3f-fa21bd3e9079 | -9.42262 | -44.17373 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8fe524ae-07a6-3f71-93c2-f049858be67c | -9.42137 | -44.14761 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5baa0562-8e1b-3df3-81cd-4fbc0726c73f | -9.4207 | -44.15244 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fbbfab48-507b-32e5-91c1-e2698b6ce198 | -9.41856 | -44.16805 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4a9b85e7-29eb-3024-a395-6055687b7ad6 | -9.41787 | -44.1731 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4c833de5-f542-3652-9da2-bada384b40bf | -10.29803 | -43.42252 | 2024-10-14 04:44:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4663008d-1b94-3f23-86b9-bf3b3b5bfd20 | -10.296 | -43.42232 | 2024-10-14 04:44:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7eef0093-5c14-3cb9-8862-298b59249abc | -10.29564 | -43.42519 | 2024-10-14 04:44:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8c54cfc-c0b0-33cf-aa80-c670458c2362 | -10.29527 | -43.42805 | 2024-10-14 04:44:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0204689-066a-3c44-8e56-6a40dd2e2c1f | -10.29296 | -43.42184 | 2024-10-14 04:44:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb15ce73-30de-39f3-9e90-128251135244 | -10.29258 | -43.4247 | 2024-10-14 04:44:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37fc786e-4e65-3a45-8139-8245fafc7265 | -10.11973 | -43.94635 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32578dde-1a84-3337-ad98-a5b8462184b2 | -10.11729 | -43.94854 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5d7bce1-7701-30aa-80b5-7467d26dd463 | -10.11591 | -43.95921 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8af1347-c1ea-3b8a-94a6-a5f70745e0e8 | -10.1156 | -43.94022 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f576246-0ebe-3aa3-ae4d-3cb34935eca7 | -10.11486 | -43.94568 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2195c47-819e-3ff9-ae34-842a758deb06 | -10.11339 | -43.95644 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a58d9aba-76e6-31aa-a1b4-043c06396692 | -10.11312 | -43.9424 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b77ba82a-2b84-387a-800a-da0dc9c55075 | -10.11172 | -43.9533 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5c60718-44d9-3ac3-9827-6cc7febad589 | -10.10999 | -43.94498 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea2969de-b3bc-30fc-b68b-4d13b1599874 | -10.10851 | -43.9558 | 2024-10-14 04:44:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ec2829e-a2bd-3a52-af65-84eae478dae0 | -10.08513 | -44.23438 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a69e246-29e6-3681-bdd6-cbf366fa5746 | -10.0847 | -44.23681 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db1a1d0b-8dc9-317f-aa74-e067f8969452 | -10.08235 | -44.21835 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9c22303-86b0-3b3e-ada4-08ae77a7ee74 | -10.08203 | -44.22084 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db9ad56d-b4ac-35e0-9707-405e5f2108bc | -10.08168 | -44.22346 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 996e55ae-e0ce-3e1c-8599-9aed116010c4 | -10.08062 | -44.23108 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ce50673d-725a-37d5-ac46-21e5f9626bb4 | -10.08035 | -44.23372 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6712f8c9-7c9e-31d6-90cf-2b60e8b12de4 | -10.08007 | -44.19966 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99eef10d-a9c3-3711-a404-7b62a12c59a1 | -10.07992 | -44.23617 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b0abb807-1c8c-359f-9c90-66666664afb9 | -10.07969 | -44.23883 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6d2390eb-03d4-337f-87f0-9301620937a6 | -10.07957 | -44.20227 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a4aed6ea-2bd7-3068-b629-53ece650c036 | -10.07935 | -44.20486 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8f82cb6-d073-3c65-88c5-94cd9c0b692c | -10.07922 | -44.24128 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 64ebb188-80c9-3a4e-838d-8777c0e5b507 | -10.07889 | -44.20745 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f2956d8-2de2-3c1e-b536-1835521989ad | -10.07823 | -44.21259 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c72ce6f4-6678-3f59-825a-0d80178de0be | -10.07756 | -44.2177 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7ad2c97-34d4-3835-b404-e29eadb15c46 | -10.07725 | -44.22022 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cfb2c6e-c516-37ad-9855-56ab43c7671d | -10.0769 | -44.22284 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66fba12a-f47c-3c50-a34d-9b6fd47f14b7 | -10.07654 | -44.22535 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3191de6c-a65b-330d-926b-bbc172f1a6b8 | -10.07623 | -44.22798 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5f6cd70e-038b-3999-bf9a-7ceb89143947 | -10.076 | -44.19373 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 120bf0aa-6d16-30be-9334-16864781370b | -10.07584 | -44.23046 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d3409b5c-dc69-3ad7-98d2-1c234ba2f7db | -10.07557 | -44.23311 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d2d1d794-fb91-3ed0-8188-73340c7590a4 | -10.07529 | -44.19896 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ee07160-5de8-3c1e-ac14-5c681bad7606 | -10.07514 | -44.23557 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c2432483-afac-373d-8847-b659b503e698 | -10.0749 | -44.23823 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 31657ea6-0fa0-3dd7-a3db-aa502ff6c963 | -10.07457 | -44.20417 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90e6048e-299f-3e00-b4f0-a011323badd6 | -10.07443 | -44.24069 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8ad6f7ca-5eba-34ba-8f4a-9cae58a1f5bf | -10.07423 | -44.24336 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a356531f-b548-3539-9fc5-89915be0f272 | -10.07386 | -44.20935 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2036e596-4ba1-3ace-9681-ab707f3e16ce | -10.07316 | -44.21451 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac90f99e-3d97-375a-8d78-0bf628a174d5 | -10.07245 | -44.21964 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec273ba6-1244-32cb-8243-cd21f77c079e | -10.07232 | -44.25607 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 212cf966-747b-3de0-b210-7ed1227bd15f | -10.07224 | -44.25876 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| dfde0ed4-d9a0-3d12-a8a0-96c4c2553785 | -10.07161 | -44.26119 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 1bc0d787-c57f-390b-8c1c-a7cd47350c50 | -10.07157 | -44.26389 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| fa3b0379-f095-3a2b-be14-06d9edcfeaf7 | -10.07122 | -44.19304 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ef66342-8c99-3cb7-a648-3d6900a962ae | -10.07091 | -44.26631 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f4686510-f7e1-3840-9bd9-23f8104794bb | -10.07035 | -44.235 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ba1a57b-0c06-33db-abbd-36327c20147c | -10.06964 | -44.24013 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 656a955f-f9a5-376c-8f03-f74d0c3c4e03 | -10.06925 | -44.1717 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04cf217d-c83a-3d12-aac3-138a97005548 | -10.06908 | -44.20869 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f8c4bd4-788e-3f54-b72b-993a5d20e9fa | -10.06894 | -44.24527 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2b30c1a-8fef-3a0c-ac23-f373f133cf10 | -10.06855 | -44.17685 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 497470fe-6cca-3762-883e-0afcd72925ca | -10.06837 | -44.21389 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e2a4eee-a581-32a9-86be-1c785571e446 | -10.06683 | -44.26065 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 62bf65f5-a7c2-309c-b588-3092569e35f8 | -10.06613 | -44.26575 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| a58ac4f2-fd0e-326f-90de-92c8280f4509 | -10.06555 | -44.23449 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebb1ad2a-55e5-3dfb-8b55-e74ad16654a9 | -10.06445 | -44.17102 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc28c558-1916-3e99-a631-aeb571c6c1e5 | -10.06414 | -44.24477 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18b4d2ae-2688-3f70-ba36-77d844e276c3 | -10.06358 | -44.21328 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5a9ff35-9010-3abe-95d1-659e217634f1 | -10.06344 | -44.24991 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README73.md)
