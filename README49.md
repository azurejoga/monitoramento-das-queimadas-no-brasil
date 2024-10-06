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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 318d4645-6a69-3c1c-b554-68afde3aa605 | -7.74319 | -43.04817 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a0af8302-f7d8-3da6-bd4c-08fbe7643bf6 | -7.74272 | -43.0502 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f5189ea0-0eef-30c7-84ee-fcbb88f940a2 | -7.73881 | -43.04955 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fa58e86d-2c4b-3340-8cd8-4c2df2bb52d2 | -7.73846 | -43.05248 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| aaba2ce3-a276-3ae4-9d86-8b4b13efbb93 | -7.73796 | -43.05452 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c03bffd0-6fb5-3cb3-ae0b-7c1d6e34d8d4 | -9.24339 | -43.5153 | 2024-10-06 03:53:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ed752eb0-170f-30b9-9623-56626e23ff96 | -9.24253 | -43.5204 | 2024-10-06 03:53:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d5fc3256-5716-38f0-9515-e9e2f8fc7172 | -9.23943 | -43.51479 | 2024-10-06 03:53:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c702c70b-a02c-349c-98c0-2a2b34eb2088 | -8.29589 | -42.83065 | 2024-10-06 03:53:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eef4d2bb-eb4a-3f49-a826-6e62cf4b5000 | -8.19488 | -43.71157 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0c5449ff-a239-33ce-b684-cc81e8b337df | -8.19182 | -43.72937 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0e4c005-f38b-3c37-b22e-d2e6b7e70fe8 | -8.19121 | -43.73298 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 82890c6c-9406-3c1a-b2ee-e2d9a0029194 | -8.18839 | -43.72506 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fdf24637-8183-3b08-90fe-a83e8a50a348 | -8.18435 | -43.72436 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd58632b-5871-3192-805b-8a8e8daa91b8 | -8.18092 | -43.72007 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 396804a5-f853-3ff9-a5b4-76e47ff956c3 | -8.1803 | -43.72366 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b90f8c23-4c52-3151-9473-884709da7444 | -8.11575 | -43.78794 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1fef107c-db72-34b0-86c7-472f08120595 | -8.11512 | -43.79166 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12666e8b-ecf4-3310-bc1a-e1b4c5df2da5 | -8.11105 | -43.79096 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 710a149a-d130-30ce-898c-90dc1aff868e | -8.10697 | -43.79027 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7613ecc3-c7b9-377c-a78f-901c429ceccb | -10.1627 | -42.89907 | 2024-10-06 03:53:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fcaca295-bacb-3b5e-8321-dd0aeacdc7f6 | -9.95078 | -44.10062 | 2024-10-06 03:53:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f3fd351-43dc-391d-8f6f-48fd3213c386 | -9.94674 | -44.09991 | 2024-10-06 03:53:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 990fca0c-dda2-3867-8e9e-508b1c8fdc5f | -10.24848 | -43.58993 | 2024-10-06 03:53:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 875063be-0f0a-3448-b39e-d19c87ffe894 | -10.24781 | -43.59195 | 2024-10-06 03:53:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 922e067c-682d-371f-84a3-76d0cbd022ee | -4.13496 | -43.80972 | 2024-10-06 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d5c1863-7743-3856-86f3-7354c3b28c6d | -4.13131 | -43.80478 | 2024-10-06 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6240c3cc-27f3-3058-bfa7-e169401764db | -4.13063 | -43.80894 | 2024-10-06 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43119f6b-fed2-33af-9c7d-a4e34e1f18bf | -4.12995 | -43.81311 | 2024-10-06 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c6ad4a9-4aa3-3689-b1c2-73285400d1f1 | -4.81888 | -44.35519 | 2024-10-06 03:53:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d724c17-27cf-3f8e-9650-de8b45b42d03 | -5.89694 | -44.66997 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef20d32a-3cb4-33ab-bb81-f4aa6e165ed7 | -5.82467 | -44.13437 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32bda965-757b-375d-9c08-4a0d6c4a4d5a | -5.82258 | -44.12938 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6e96f7de-53da-362b-a05a-abaaad08a00b | -5.82188 | -44.13346 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f484be85-aae7-36a9-8326-45caa5be7ccc | -5.82102 | -44.12952 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c44b4b73-a3fb-36e7-9a43-5d99f42535b2 | -5.82035 | -44.13362 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 865c2f53-a8ef-3019-8eba-ed59631d68b6 | -5.81968 | -44.13773 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9916c6ad-07fb-3400-a4f4-0555cbb0aa31 | -5.81826 | -44.12866 | 2024-10-06 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6deb0eaf-420c-34be-8c71-bb9ef28c5846 | -5.81756 | -44.13275 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 43111b77-b7ed-3c00-96b7-9ccbba040d96 | -5.81685 | -44.13686 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9e1a7310-a799-37a9-942e-a5beaa4bd0a3 | -5.8167 | -44.12881 | 2024-10-06 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e2e69f08-a451-368c-8130-3e8a1d7110e1 | -5.81602 | -44.13291 | 2024-10-06 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3b14ae05-943d-3ef9-8660-3684a83dc4db | -5.81534 | -44.13705 | 2024-10-06 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 228a813b-ad39-3efc-9eb9-4a53634400cf | -5.58123 | -44.87567 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 83f97e28-fa30-361b-94a2-b72c314e4ce4 | -5.58049 | -44.87743 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5a33c3f1-cb40-330a-8b6d-141a223d61a6 | -5.58046 | -44.88035 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5bb15256-68db-3851-8e50-2596c0592805 | -5.57968 | -44.88508 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bd4e89bf-bdff-35e4-ad30-698b3fa19c85 | -5.57968 | -44.88212 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 774e0e2a-f3ae-31ae-94b2-c9b7199cf101 | -5.57667 | -44.87488 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 17a466f4-32eb-382c-b8f5-a1366b4bc5cc | -5.57589 | -44.87956 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f4f76e93-a93b-358e-9ff5-57d74f8722c3 | -5.57511 | -44.88427 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 153e463e-8692-38e4-b724-bcbc4e4e5fba | -5.5721 | -44.87416 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b901535d-b112-3b23-8e7b-37e594e4da84 | -5.57133 | -44.87879 | 2024-10-06 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 88ac257c-47b8-35c5-a1de-c49c35204813 | -7.24539 | -44.93737 | 2024-10-06 03:53:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 95cb2a74-b0aa-3aa0-8cb6-ed5e546f85af | -7.06785 | -44.4023 | 2024-10-06 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 811275d3-1aa4-3850-8fb3-a219a09eaaee | -7.06592 | -44.40325 | 2024-10-06 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 130074df-36fa-3a3c-b552-43a715dfbb76 | -6.73262 | -44.56723 | 2024-10-06 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af38dfb1-070a-394d-ad79-3e70cb4d5177 | -6.73189 | -44.57146 | 2024-10-06 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 043ce1aa-076c-3b17-8c66-bb536437776c | -10.05214 | -45.28388 | 2024-10-06 03:53:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7103aa5a-e952-3daa-a329-96b52d225369 | -10.05159 | -45.28595 | 2024-10-06 03:53:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5b162a5b-6dad-30d2-8b45-6ecf0f698965 | -10.05134 | -45.28831 | 2024-10-06 03:53:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a7e6fa4d-e2b4-3754-af42-a86dd8be1059 | -5.05075 | -45.12982 | 2024-10-06 03:53:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c9ba0d0-6d82-33a5-9423-23e9f870651c | -5.04462 | -45.19454 | 2024-10-06 03:53:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e80270c5-cca8-3276-ac60-21f00130ed49 | -4.9522 | -45.51297 | 2024-10-06 03:53:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3f965a0-6194-3498-beca-be37e842eb02 | -4.86898 | -45.77312 | 2024-10-06 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dc50c60-2337-3896-a9a7-128e230e8a27 | -4.86177 | -45.84642 | 2024-10-06 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1647af06-9745-398f-8202-563fce6128f3 | -4.83115 | -45.81726 | 2024-10-06 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83af6e0a-5191-3a83-a525-60aefe6a2f2d | -4.57842 | -46.06942 | 2024-10-06 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90ad7586-01ec-3e26-9fdf-1edc178d5d7c | -4.57796 | -46.07217 | 2024-10-06 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b8eaf91-5d5f-355c-88c0-acf25e5a6fe3 | -4.13295 | -46.10129 | 2024-10-06 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c4ae422-5831-3f44-8cd2-c67204aae4e2 | -4.12789 | -46.10027 | 2024-10-06 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feecec6a-0e3e-3e22-8282-cc6db1785ed6 | -6.41102 | -45.82633 | 2024-10-06 03:53:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92a38817-f62b-307b-ab69-cbc26174e8fe | -6.41067 | -45.82271 | 2024-10-06 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5d8b14d-af9f-3f36-a0c0-9c5c3ad43558 | -6.40976 | -45.82788 | 2024-10-06 03:53:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be821247-4dd3-3f76-ab49-d2598a509a15 | -6.35219 | -45.70866 | 2024-10-06 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25f23c35-fadc-3019-ba49-f6aee55ed293 | -6.34734 | -45.70832 | 2024-10-06 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ed7e5f0-fe52-34fc-a0b7-a6faca3a3609 | -6.34637 | -45.71394 | 2024-10-06 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 053291da-dbcc-30e9-9d97-9f76e5804fab | -6.3425 | -45.70789 | 2024-10-06 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5e838a3-ce9b-3768-a6b5-05e039d2ed5d | -6.34154 | -45.71343 | 2024-10-06 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c61aca6-bbe5-3628-a76d-8e971e5153d6 | -6.33767 | -45.70741 | 2024-10-06 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24d1e320-01f3-37a0-9543-403ca5742884 | -5.18214 | -45.24624 | 2024-10-06 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10817bf9-cb5e-31ce-9597-51060271e139 | -5.72841 | -46.47521 | 2024-10-06 03:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8087a34a-f1e7-32c9-b0ff-61e3dd0922e9 | -7.7568 | -46.14391 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2f7528c-3989-3cde-aea2-b27faa5a26e4 | -7.75625 | -46.13976 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2ca847e-c31e-3da8-9cf0-4af84f74cbb3 | -7.75535 | -46.14477 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 717cf6e1-86ab-36aa-ba48-21d965809b84 | -7.46635 | -46.06314 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58a4d5ee-07f2-338b-9330-1151de74bf8b | -7.46544 | -46.06828 | 2024-10-06 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7acd9961-af4c-3ba4-8870-07f4787a5d1e | -7.34301 | -45.51041 | 2024-10-06 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3284e642-ebcc-3e3e-bb87-646b6ce653b5 | -7.34133 | -45.52002 | 2024-10-06 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 346ab31d-e297-320c-9e1a-c507189c864f | -7.07461 | -46.59558 | 2024-10-06 03:53:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffca63b9-3a3b-3bee-81e3-02547afe3221 | -6.99969 | -45.38558 | 2024-10-06 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05b1e391-a307-3537-b956-0d6f680fcc32 | -6.75511 | -45.64662 | 2024-10-06 03:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1dd71c86-fd5e-3e1c-ba17-f372a85797ae | -6.75473 | -45.6451 | 2024-10-06 03:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2899e99b-449b-3e02-898c-c53ce6871e43 | -6.7504 | -45.64576 | 2024-10-06 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a48e2f1-f94f-3817-ab74-c37ab1db3ed8 | -9.34604 | -46.5473 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 487cdc9e-877f-3fa6-a75e-14c8a6c165c3 | -9.3451 | -46.55258 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b31a6f2-d953-3b02-9b9e-002c199ecba0 | -9.34416 | -46.55782 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f2f0efa-8229-3afa-8b46-03bf03241d14 | -9.34314 | -46.53591 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 18b4e78d-1b6f-30cf-a3ab-13566795966e | -9.34221 | -46.54108 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8fb86fe5-f4d7-31d1-94c9-2d6e9428cc45 | -9.34127 | -46.54631 | 2024-10-06 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README50.md)
