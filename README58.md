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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c557f40c-332e-3887-a2f8-e1a00d8a7a3a | -3.48313 | -52.82603 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d849f969-ba7f-3310-8856-a58a01da35a2 | -3.48259 | -52.82948 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1160910-d6c2-3717-b3c7-f5d1ab5a5d33 | -3.20656 | -52.8746 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b75009aa-ffba-39b7-b15c-7a29838d4ac3 | -2.68312 | -52.4346 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 400bca62-f876-3721-b2db-c85b96543798 | -2.66465 | -52.5315 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5dd3455-a145-3a14-a0e0-5f78c7a43113 | -2.66411 | -52.53498 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baae76aa-9efb-3685-973e-a6e6219f7c91 | -2.66133 | -52.53098 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2504b1c0-55de-37a5-bb30-cdeb4000c37c | -2.66079 | -52.53446 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 945b75d2-e268-31fc-8ccb-5b7e9a9970d2 | -2.64258 | -52.54165 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b0af059-1380-30f4-b322-0b049a2fc2e3 | -2.63872 | -52.54459 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff10ec2d-8918-383a-b0dd-6dd6dbc4000d | -2.63818 | -52.54806 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58882d98-d087-3f2c-95d7-81f0713601a9 | -2.63486 | -52.54755 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 515654da-4f7e-36c6-beca-72d7413ec517 | -2.25806 | -53.4745 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6986e1c-3001-3dfc-a47c-cb9de2729846 | -2.25752 | -53.47793 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35eb6230-9e2f-3cc8-bb32-95d303aecaeb | -2.25476 | -53.474 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d20b67d9-4e2e-3083-84f4-95a301139a1f | -2.25423 | -53.47742 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0003184-1443-3fba-bd66-fde26bf48a8f | -2.25369 | -53.48085 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d545f2c-bd71-3ef4-8ca4-8967086121fe | -2.25315 | -53.48428 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08e3ee16-6d8b-376d-bde5-efc8cdf3d460 | -2.25093 | -53.47691 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 513b910e-1b40-3629-87bb-e5152fb93132 | -2.25039 | -53.48034 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad029a0-13ca-362b-9cd9-c15c829c8316 | -2.24985 | -53.48376 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95dc813d-a372-3ac7-a18d-22f3820af272 | -2.24709 | -53.47983 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d5ca52c-35b9-39b4-ba57-46644f7aa54c | -2.98747 | -52.90425 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 34bdbf09-6d66-35c7-b645-59807e616b96 | -2.98693 | -52.90769 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8935d139-52bb-34d8-850f-74164cd3b8c7 | -2.98639 | -52.91114 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82a50050-8531-3960-98ea-ff0d7ffcba8b | -2.98417 | -52.90373 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 32202794-4d01-35df-810c-99cdd822fe81 | -2.98363 | -52.90718 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02e54fc3-4889-30cb-9701-814aee6713fe | -2.98309 | -52.91063 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a87efb81-fbf7-31e8-9ef9-9d422d952631 | -2.98086 | -52.90322 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89ee010e-f849-37e3-8cd5-c549d4310d8e | -2.98032 | -52.90667 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec5ae4e9-266f-30c9-8ff2-febcd50695e4 | -2.97978 | -52.91012 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3e4d46e-f09d-37e5-823a-df7b6dcd23bf | -2.97756 | -52.9027 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb908eac-ab4b-3022-9c6c-a9e07c55c1ec | -2.97702 | -52.90615 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b854677-8407-368b-bc76-f3194297ae04 | -2.97648 | -52.90961 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5866a038-59cd-302c-8374-13486d3bd7a2 | -2.97425 | -52.90219 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e28a979-06a6-3f85-a010-4ade5aab5219 | -2.97371 | -52.90564 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26e875f2-b27a-3d0b-9103-ec7edc22bed7 | -2.97318 | -52.9091 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 582204dd-2dfd-3ee9-b129-31ea637e9251 | -2.97095 | -52.90168 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c51fc10e-e8ad-306d-b0dd-6bd0f777a5d1 | -2.97041 | -52.90514 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33b25534-dc70-3da0-a10e-52a8c8d227a6 | -2.96987 | -52.90858 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eddd8f7-8f34-346d-b73b-d77d1d3c91de | -2.96764 | -52.90118 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 144febde-6226-3857-a35b-a6e902bb7e8f | -2.96711 | -52.90463 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb282fdc-ce31-3d81-ae42-033161b09e50 | -2.96657 | -52.90808 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65720790-e682-3bdf-a541-57d7cfe4c3a5 | -2.96603 | -52.91153 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7815afa0-71b9-3b36-bb32-a25ce682b434 | -2.9638 | -52.90412 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 632397f1-6ad8-32dc-8305-47faa16f8674 | -2.96326 | -52.90757 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a081b3f-b667-3392-b245-e2f84d5041a6 | -2.96272 | -52.91103 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da106f28-63ed-3cf4-b979-f592107959b0 | -2.9605 | -52.90361 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d83bb766-da49-3ff1-b323-a9507ec5e725 | -2.84942 | -52.93871 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ec1908e-0112-33c8-ae92-99eab1f197e4 | -2.84666 | -52.93476 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d09f5eba-3c74-33ff-b4ae-98d9831ef85c | -2.84612 | -52.9382 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2a16737-ab24-3648-a8d8-8609f41b5df4 | -2.84336 | -52.93425 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf9c5ffa-6db1-3463-9223-4f05dbc0c287 | -2.84282 | -52.93769 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c2e6dd6-bb50-3e5b-9e9e-ba1cb6402282 | -2.7971 | -52.92347 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47db7c0b-b945-3ac0-98e0-1f31d7d0805e | -2.78412 | -52.48581 | 2024-10-12 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5d6424d-4b53-38df-a6e6-5499b893d591 | -2.78134 | -52.48182 | 2024-10-12 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcbde61e-fa00-339b-b63a-2c7f98924f36 | -2.7808 | -52.4853 | 2024-10-12 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 984d21c7-b6b4-3838-b726-c63c98ac24a1 | -2.77802 | -52.4813 | 2024-10-12 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dca95b68-de94-3df2-9377-7a76b603c21e | -2.77748 | -52.48479 | 2024-10-12 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5841a6ed-e707-345a-9aa3-9ede8e5222ad | -2.74848 | -52.45189 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 899c1c75-bbc2-3f9b-9597-035de5e255b4 | -2.74515 | -52.45137 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e1cf7c3-3251-3921-ab1a-ab01771fa62b | -4.26941 | -53.69386 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05c5b699-1779-3a1d-a6f9-eeb9a7345f21 | -4.25218 | -53.63142 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12f70503-d8ad-3574-a318-d00a5ece8db3 | -4.25164 | -53.63485 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70569001-feba-376c-889c-4194c3b9aff3 | -4.24835 | -53.63434 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f38ce69-d9de-3741-a381-271516741cd0 | -4.1979 | -53.54198 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2878217b-5654-304a-812d-42bb9ce40b98 | -4.08406 | -53.57293 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 536604f2-481d-30b0-929b-bc784d1a9ac7 | -4.08077 | -53.57242 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa7a66a7-13a1-3481-a5ac-44c2623731ca | -4.02681 | -53.41624 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a38c3932-bd3b-314f-b53a-0be843193a5e | -3.98401 | -53.43065 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6683d2c-160f-307c-ba3e-b8954cba1222 | -3.98071 | -53.43014 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbda0057-7acc-3eed-a8c4-2912da558c65 | -3.87587 | -53.79694 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b6a4a29-5ca1-3703-a581-bc66ca125fa5 | -3.73491 | -53.30688 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bebad985-5130-35ca-9037-5cd9f66d0002 | -3.89629 | -52.37756 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e198ee5-37ef-308a-b636-8788cffc9a73 | -3.88994 | -52.30756 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5daadf42-cfc2-32ae-a8f4-91ceca4583f5 | -3.83553 | -52.33223 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9224acf7-a5f5-3bcf-8a2d-d0087b3b6f09 | -3.81713 | -52.34032 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2bf98fe5-3659-3c81-992a-0be280d94ec1 | -3.81658 | -52.34388 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5f8945f-74b3-3f30-be7b-df2ef7751db4 | -3.76839 | -52.43402 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67205126-bc4c-30c5-8970-f7fb3f6a9f7b | -3.76559 | -52.42999 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb538900-3843-30db-ad6a-070120dcf04c | -3.76505 | -52.43351 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25774132-3de7-30c1-90f5-db2c553b4daa | -3.76276 | -52.34284 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3519c9a8-9928-38e2-9334-0a2eceb75f4e | -6.22438 | -53.33308 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac8df18e-2f0a-3a4f-b688-cd180d49bdd4 | -6.11627 | -53.24071 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61284b96-9130-3893-94e8-83dc8e430755 | -6.11591 | -53.33016 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66aa8647-7466-3b47-a2fb-b708716b9461 | -6.11294 | -53.2402 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81cb3443-ca95-39b7-b031-a589f2ca5f91 | -6.10569 | -53.22123 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed382600-300f-3da6-bda7-b990c4293163 | -6.10236 | -53.22072 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f58c666-2cb3-340d-8c44-d294b8c8e01e | -5.91617 | -53.43443 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c751afc9-eb19-39cc-86f1-dbcbd08bd97f | -5.81778 | -53.67091 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8254b638-617b-3ea3-8190-f4494de90add | -5.67069 | -53.74268 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02a2aa0f-090e-38dc-a352-25544f1d5bab | -5.66739 | -53.74216 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 82b3e547-3b53-3229-a862-604a353f85eb | -2.24507 | -53.53571 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20373878-c344-3d74-88f2-9ad9af140273 | -2.23611 | -53.65733 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e93eb59a-91a9-394c-8fcf-bf56a43715b3 | -2.10203 | -54.69949 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e93b9b0d-8c33-34ed-8731-03c1a57462dd | -1.9194 | -54.58649 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fcd848c-8a84-36c2-91c8-bbdb5f289f20 | -1.91604 | -54.58596 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acc60cb2-91dc-3446-9c4b-2e6ee2790ee6 | -1.89753 | -54.42688 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 99b0b0fb-f0da-3d2e-aa8c-07df079576b2 | -1.89698 | -54.4304 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b252e23c-3462-3a24-8355-b0ee2f47a808 | -1.89523 | -54.63027 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README59.md)
