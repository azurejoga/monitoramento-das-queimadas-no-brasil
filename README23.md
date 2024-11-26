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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 443b5216-0409-3695-9700-209e90689b76 | -3.391 | -50.09121 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 84af544c-3303-3c0e-8a3a-62986a1ea0d1 | -2.59792 | -46.25687 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dfaadb2-d573-36e8-afe4-d722330dc27f | -3.41976 | -50.37408 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d31ba9c-55fc-34f5-8fc6-da9f3a77b59c | -2.78904 | -48.56344 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d21b462-8be7-3e46-906d-e78e350b1b44 | -4.76353 | -45.5929 | 2024-11-26 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7f50651-b72f-3550-bf1a-36db9534b826 | -4.35578 | -48.56459 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b237181a-650e-36a9-8078-c0e16865db5f | -2.49793 | -48.34811 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6fdd998-e608-3d2c-a222-03578ba6ada9 | -3.062 | -53.22525 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4228657f-c8e1-31e8-9c75-58a56a839a95 | -2.80195 | -53.02897 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58a4996b-164d-3d06-b0e0-e17819d273ed | -8.21819 | -49.06842 | 2024-11-26 04:38:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02a35aef-d6af-3c50-8c00-d4342358a1fb | -3.54115 | -50.40017 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 475046ac-c13e-3311-8e1d-e169cbf01ab7 | -2.5885 | -47.45142 | 2024-11-26 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb4e7f63-37e0-3cf8-a4c8-108793a0193c | -3.38978 | -44.16511 | 2024-11-26 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 59a9fd0b-f0e5-3d92-bf3a-be227612c0d0 | -3.30204 | -47.01858 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cd95c7b-3389-39cc-8bdf-3f450f816e38 | -3.28927 | -50.75727 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e9f3fb1-0ea5-3337-81b4-36190c4ce40f | -2.7957 | -53.01787 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0319943b-0696-3302-9a82-6b829d51662f | -6.07922 | -48.03499 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7e71b746-8278-310c-b34d-cc38c73cf381 | -1.98701 | -53.29487 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 126e3405-5218-3dd5-a37f-3039e84437fd | -4.37648 | -49.63287 | 2024-11-26 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed5bc9ff-6555-3edd-bdfd-004e67290893 | -4.27056 | -48.61149 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 711833f2-a37e-3d6e-8ac7-8621861fe0ef | -6.37422 | -46.77893 | 2024-11-26 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8a963ec-98e5-3700-aa01-2746d2d1c767 | -1.79113 | -52.74311 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 790322a6-3801-361a-8e15-3928c91f13ba | -3.38438 | -44.17432 | 2024-11-26 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9a2b011-f982-3481-9337-076f593702fd | -2.7732 | -52.90948 | 2024-11-26 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64de40bb-baf0-3757-bf9a-9789c50d3c2a | -4.66246 | -47.94477 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11c6982c-0458-3fc4-bcac-bb06e6eb0e47 | -2.80743 | -53.01978 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 850335da-7632-3631-9eb7-1af03562be3e | -3.98035 | -49.97052 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd44d1e2-4a60-348d-9b7b-f49cadd65971 | -2.8004 | -53.01358 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cf06ea5-72e9-3e35-897b-3ecfa4341109 | -6.37224 | -47.35762 | 2024-11-26 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3e823d2-cfb9-34a9-b4a0-9134a66fc7b9 | -3.68039 | -50.2281 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07266080-be6d-3445-a8ab-8b1592417427 | -3.97288 | -48.09246 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c75932fd-3e32-3a28-867e-7fd16341ea4d | -3.82954 | -47.46785 | 2024-11-26 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5891ee89-85d7-3b64-8bb5-fc95f288d218 | -3.53925 | -50.45626 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 350a9881-4051-3d7a-8bd9-5db3bf370287 | -3.29107 | -51.1579 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d1eeb93-ad59-3149-8e18-a4c746ffd973 | -1.72327 | -52.48674 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 414a4374-e350-32af-9f5d-cf36acbc1fd5 | -3.93326 | -48.15408 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d89ef4d-b4f2-363b-bbb7-ddd733d611cb | -3.38591 | -50.10146 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8998250d-6768-33c6-9c89-a614f49279c0 | -4.37886 | -48.50437 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c678e162-0fce-3a3c-992d-0879d089e8aa | -3.93752 | -48.14403 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7711c296-aa48-3758-8388-0bc06c008b4f | -2.93776 | -48.82321 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abbc190b-3bac-3f92-a865-bd1af2e73531 | -4.30887 | -48.60334 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 845d4d78-aea1-3350-ac1a-2ba23621f381 | -6.08204 | -48.03906 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 547ac719-31cd-38c3-bef2-153a38140c73 | -4.32092 | -47.53588 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c44b353d-d5cd-3fb4-8bec-4e38ee3a22f5 | -4.37553 | -48.50385 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 599d74c4-4bb1-371b-91ba-456b924d5868 | -4.29327 | -48.22802 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d5cf58f-3aa3-322f-97b1-ec9d72f3a534 | -1.57775 | -54.39442 | 2024-11-26 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13a0a081-1425-3909-b918-38f78631bec4 | -3.97227 | -48.07451 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 847b356a-1b20-36e3-a9c4-6a07054b35ed | -3.18604 | -48.42784 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4759a19-fbdc-3d46-a73e-c77fc14e6a38 | -3.25223 | -53.285 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dcc722f4-7cc7-346e-ba35-6fc3150598c4 | -2.93486 | -48.77679 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3ec858c-35aa-369c-947e-977f45cdcf0c | -3.96893 | -48.07398 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2f211469-2e84-3eab-b7c8-3dc8d3bbbecd | -2.3204 | -48.5535 | 2024-11-26 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8d1d6a3-6195-3157-b773-44b41cec8bf9 | -1.72072 | -53.24822 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7493b25a-24ec-3c99-b930-08c786b93640 | -4.54192 | -43.28793 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00acbe08-b1e8-36a1-b4df-57cfad5c8ed4 | -2.69271 | -46.87458 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca89efc0-c629-33ce-a052-dd14e10b5116 | -3.07733 | -49.50048 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37170fbf-2bde-3df7-a3b7-81594f470783 | -3.32794 | -50.05176 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50291418-f017-3034-b54c-2b2c72fd8992 | -3.29145 | -50.54305 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24db37c7-d960-32a1-947b-f7d93e32d6cd | -4.86361 | -38.38534 | 2024-11-26 04:38:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b04cefde-1c8d-38aa-add0-252951076d8f | -3.98731 | -48.08757 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 707eb093-fc07-3f66-b75f-efc7b257d3c0 | -5.20911 | -47.95241 | 2024-11-26 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b560ee9-9616-3386-9c5f-d9d54f155ce9 | -3.97724 | -48.06455 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 61c33bef-839c-34f3-b407-780ad9ebfbbb | -2.70291 | -51.9852 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ca41db02-049c-31de-bdb3-1c7ec326bd1d | -3.97451 | -48.08201 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 193ad821-7ab8-3a69-9443-48684a934d1e | -4.2772 | -48.61253 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4d2712b-7c73-339a-b69c-98d8ab9fe24c | -3.97839 | -48.07904 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6f8ecdc9-dc59-35d4-9c54-d008a70f9f7b | -3.50087 | -53.79712 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18811b40-a940-32ee-b7b6-387ed552a3b8 | -4.24417 | -48.67111 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c582b37a-5e14-3b65-940f-425da1fef985 | -2.7885 | -48.56689 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bbe5cc3-46d9-348a-84ab-ddbdd6966f72 | -1.36016 | -54.63463 | 2024-11-26 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d118091-0009-3c7f-ba3d-da900a0e0d0e | -2.71738 | -46.2617 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c698571a-a5ae-3726-a30b-a60a9c84c7db | -3.97118 | -48.08149 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7767c5b3-afff-3be9-898f-519cb2e71a51 | -3.06015 | -53.28674 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a79ff9d9-c21b-3c84-a808-22e7795df5c8 | -3.22847 | -50.78249 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d82bc5a-4b0a-3411-b47a-1bb702198827 | -2.25903 | -51.87394 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06bdde6f-ea7b-34da-9fef-0a59fdb0c875 | -3.38253 | -50.10093 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f0b2ece-c4ec-320d-99df-6f00d50ab2e5 | -6.37626 | -47.35442 | 2024-11-26 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a99faf6-31a8-37d2-9980-cd4382840240 | -4.76324 | -45.59109 | 2024-11-26 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ce9372a-dc8c-340c-b82a-9a0409504de8 | -4.54015 | -43.29961 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7a53a8f-03f5-3463-abfc-381fb9abfdd7 | -4.29381 | -48.22453 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66b7978f-6b84-3f9d-b929-5bb50e347cf3 | -2.25041 | -53.62095 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 424820e8-a172-35ea-8a4a-1d47dfbf4c62 | -3.93922 | -48.15498 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bf7b335-715c-3d09-8e18-4534b7a89f99 | -6.06396 | -44.15231 | 2024-11-26 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61606f1f-850c-3526-a1fe-3c2bf46fdece | -3.18001 | -48.44458 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f838b5c8-8588-38f5-8cbe-8b264b87652f | -3.23194 | -50.78304 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47a37425-1406-3a1a-9e57-032d5a3aa245 | -4.31641 | -47.52048 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e53d40af-3ffe-3fd4-adde-dbf8c5931d05 | -4.11896 | -48.52078 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30933d4f-7fd5-359b-a14e-eab3c86f5b5d | -3.9156 | -42.41765 | 2024-11-26 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2fb0c219-408b-3243-829a-8256f23e3a38 | -3.2317 | -53.92624 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d676063-bfb3-3da8-9511-c45acca7c878 | -3.99004 | -48.07006 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50f643d9-47bb-3219-9726-3f7fb1c86ee7 | -3.97469 | -46.73081 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de70ecba-a699-3984-99e5-d0ddfa3c06a1 | -3.34249 | -50.50928 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d02b7129-047a-31b1-920b-32a91169c494 | -4.37608 | -48.50039 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1596c602-a21f-381e-b735-768b3f9efd0f | -3.23374 | -51.60746 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19377723-3613-3ae0-a1e4-e4b93a2f1d75 | -3.68321 | -50.23226 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f746dbf7-2544-30e0-8a30-9ff1a4d4fbd0 | -4.05318 | -46.85311 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4677a9f3-9106-3009-96f2-996bc0a99010 | -2.71969 | -46.26987 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1bf9ba5-a536-3d7c-a47a-6eae41f4e4ae | -3.97669 | -48.06805 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4dcb3646-697d-3177-b797-0528d1ee9bb4 | -5.23672 | -48.06174 | 2024-11-26 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a91a596-3355-3e8a-8967-2a554b9d3359 | -3.82562 | -47.47091 | 2024-11-26 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README24.md)
