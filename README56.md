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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a11fa643-c9a8-3883-8f7e-cac68872ae86 | -8.7752 | -44.0943 | 2024-11-07 13:50:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 024d1a94-3ace-3ad4-b899-e3a6c0f206c8 | -9.1552 | -45.3385 | 2024-11-07 13:50:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3a47903c-54e7-3cdf-bd3b-586cb181d650 | -8.1289 | -44.4191 | 2024-11-07 13:50:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6ac78c1d-8b57-368a-ad67-e953a92e0931 | -8.3088 | -43.6345 | 2024-11-07 13:50:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 197.2 |
| a24de93a-0027-3839-9d2e-998acb27d867 | -8.347 | -43.607 | 2024-11-07 13:50:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| fdb0c4ba-c967-3e5a-b363-4c8b5a39ac47 | -10.2243 | -42.4476 | 2024-11-07 13:50:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 4e05e61d-59d7-3902-9dad-eceed0d1d2e6 | -8.7755 | -44.0711 | 2024-11-07 13:50:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| b488fb43-262b-3fae-b799-d55fd707991d | -8.4998 | -42.0987 | 2024-11-07 14:00:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| d0c210ff-62da-324c-be2d-1149e3ed6b1d | -9.0826 | -45.1186 | 2024-11-07 14:00:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 294544dd-e4a6-3c13-b021-5a80e671f370 | -2.2664 | -53.7221 | 2024-11-07 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| cfbbc738-db49-3169-a8f7-fd65ce5ceb19 | -9.2881 | -45.3006 | 2024-11-07 14:00:00 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 6832debc-918c-3865-86ae-117bd91c2fb4 | -8.5188 | -42.0964 | 2024-11-07 14:00:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 4c751f95-96ec-3e30-9615-0b1ce5643f47 | -8.2922 | -44.93 | 2024-11-07 14:00:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 49275104-2644-396d-898d-a8b7272b9082 | -8.7755 | -44.0711 | 2024-11-07 14:00:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| bbbdf382-bf1b-3002-aff9-922e215d879b | -8.1289 | -44.4191 | 2024-11-07 14:00:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f33745de-6c4a-3660-9195-f9fb5c35be10 | -8.502 | -44.7475 | 2024-11-07 14:00:00 | GOES-16 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d87524a2-8d09-36c2-8d79-2576133a113d | -1.1466 | -53.7177 | 2024-11-07 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e9030550-2019-3bc0-afbe-cf358569db87 | -8.3094 | -43.5878 | 2024-11-07 14:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 42c9ea2a-68af-3cc6-835e-e77b6640aa10 | -7.409 | -44.8114 | 2024-11-07 14:00:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 9fd5f91c-76ec-31da-bced-fc9fe5416ab0 | -8.3111 | -44.9281 | 2024-11-07 14:00:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 191.4 |
| d301477d-7f19-3c90-9ca2-4e1d479e87d9 | -8.3091 | -43.6112 | 2024-11-07 14:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 226.3 |
| d98c1473-dc25-399d-9015-fffca3c556db | -8.8329 | -45.4197 | 2024-11-07 14:00:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 9dbb1c1c-f314-3999-b2e1-146284ea3e27 | -8.3088 | -43.6345 | 2024-11-07 14:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 921c6022-a97b-3c5a-9990-8d6cb1fd672b | -8.3281 | -43.6091 | 2024-11-07 14:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| e04be3a4-3295-3641-8874-c256048c30ef | -8.4737 | -45.4805 | 2024-11-07 14:00:00 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c8557446-1cf2-382f-807a-e356added1d0 | -8.7752 | -44.0943 | 2024-11-07 14:00:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6a837a64-e759-3902-9bbc-a3a1154be1ab | -8.3284 | -43.5857 | 2024-11-07 14:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 5c0a678e-ebdc-3a2a-8640-c1aaa918d79c | -8.7562 | -44.0965 | 2024-11-07 14:00:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| fe7cf3fd-a524-3527-a1cb-f0864d95efa1 | -9.8617 | -44.9347 | 2024-11-07 14:00:00 | GOES-16 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d3353e6e-3a02-3f40-8304-674b0fa44a34 | -2.8167 | -48.6653 | 2024-11-07 14:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| d27b4471-7816-3552-a3d4-85144eca2712 | -8.1101 | -44.4211 | 2024-11-07 14:00:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| d4152622-90a8-3bfb-a902-c5b58eb39f16 | -9.75 | -43.56 | 2024-11-07 14:00:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 594b3901-98da-35a8-a00c-ad83263206af | -9.75 | -43.61 | 2024-11-07 14:00:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c7375a42-a25d-3942-bd0e-5fd6b76fe2fa | -1.165 | -53.7176 | 2024-11-07 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 0dfaf230-70b3-3799-99aa-55ee5b70c185 | -8.502 | -44.7475 | 2024-11-07 14:10:00 | GOES-16 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c2308648-5831-3ac1-a258-0e6c05af0e1a | -8.8329 | -45.4197 | 2024-11-07 14:10:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 3ea30914-210f-3969-9548-d4ab95ae069a | -8.4998 | -42.0987 | 2024-11-07 14:10:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 117.7 |
| 42832c98-1a14-3d96-9ea4-d93a281c0249 | -8.5188 | -42.0964 | 2024-11-07 14:10:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 0fcc6175-94ce-37b9-818a-f223f7ac0d64 | -1.1466 | -53.7177 | 2024-11-07 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 167cebac-8ab3-35e6-8edc-1fab6a1b9dca | -8.7562 | -44.0965 | 2024-11-07 14:10:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8f5cd76f-e36e-3d73-a148-2cc6bb8b8226 | -8.2922 | -44.93 | 2024-11-07 14:10:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 537b91b8-726e-3bc9-ade6-00a81000f128 | -9.0826 | -45.1186 | 2024-11-07 14:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| c3917e17-81c7-3c1e-9e89-7d0201a1160e | -8.1101 | -44.4211 | 2024-11-07 14:10:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 069b290d-5467-39cb-b6a1-edb4ca1b9d6b | -8.7752 | -44.0943 | 2024-11-07 14:10:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a7e48c3d-1621-38d0-9869-d43fcd424ecf | -2.8167 | -48.6653 | 2024-11-07 14:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| be219446-0e8c-3a94-bc28-810172afc93b | -8.0912 | -44.423 | 2024-11-07 14:10:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 614efac4-7b26-3a21-a8b3-8e107bb4aef0 | -8.5002 | -42.0747 | 2024-11-07 14:10:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 316eecf8-1c68-3183-b6c8-0c6a424caf58 | -8.347 | -43.607 | 2024-11-07 14:10:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8a333478-95a5-3b65-9d30-2a18a9472e64 | -2.2664 | -53.7221 | 2024-11-07 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| a9f00290-2389-3ed2-a7f6-1d515f06cff6 | -11.6267 | -44.2526 | 2024-11-07 14:10:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 20f86109-af5b-34e6-94c4-eb294a17024a | -8.5017 | -44.7705 | 2024-11-07 14:10:00 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| e454aa40-16f1-37de-ae51-2692f0685280 | -9.1552 | -45.3385 | 2024-11-07 14:10:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| c3e7bcf9-50cb-39ca-a12e-10456945440a | -8.8329 | -45.4197 | 2024-11-07 14:20:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 160.1 |
| b4aa74ff-2268-3362-88ed-988695834f75 | -2.2664 | -53.7221 | 2024-11-07 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 08d67148-8e4e-3203-895b-4497c6dbc9ac | -2.1563 | -53.6636 | 2024-11-07 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2c87d863-2190-31f7-beff-2bc3d4f8f556 | -10.3016 | -42.3886 | 2024-11-07 14:20:00 | GOES-16 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| fc13e29d-534d-3f30-9d8d-30ed930290dc | -1.165 | -53.7176 | 2024-11-07 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| ed57e17e-8802-341d-ae98-08a2e96f5944 | -9.1552 | -45.3385 | 2024-11-07 14:20:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 673c435a-928d-3f98-bfb3-324d691e7cd2 | -2.248 | -53.7224 | 2024-11-07 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5a5b76ae-f98a-3b49-a3dc-db37b7f68ef7 | -8.5002 | -42.0747 | 2024-11-07 14:20:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| fc9045a5-94ad-3d49-8978-2f79482dca5c | -11.6267 | -44.2526 | 2024-11-07 14:20:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| c7623920-2abd-39d9-bc10-85a03278671f | -9.0829 | -45.0957 | 2024-11-07 14:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4b2ee0d1-ccb5-360b-8188-816a7e3d537a | -16.0101 | -43.5966 | 2024-11-07 14:20:00 | GOES-16 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| ddde68df-345a-3fdb-8793-49fabfb53a53 | -1.1466 | -53.7177 | 2024-11-07 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 670b0843-bb91-3538-805a-2659dea2acf7 | -8.5115 | -45.4766 | 2024-11-07 14:20:00 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a1cf0a6e-10a1-3e7f-87b5-3df24f56c657 | -8.4998 | -42.0987 | 2024-11-07 14:20:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 73a8c28f-0e09-3085-a721-283794e393ca | -8.0912 | -44.423 | 2024-11-07 14:20:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 26791475-957f-3fc0-9b0e-05d65fda92d9 | -8.5017 | -44.7705 | 2024-11-07 14:20:00 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| da11ab5e-1590-3447-9158-ed3eb6eac818 | -9.0826 | -45.1186 | 2024-11-07 14:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 35ab0275-a785-39fc-96da-88411ec01a24 | -10.3208 | -42.3859 | 2024-11-07 14:30:00 | GOES-16 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 82.6 |
| afa88fff-f732-3750-b68d-306142648aa7 | 1.6566 | -55.9227 | 2024-11-07 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3472b21d-f58c-368d-bc8f-c2542fa40434 | -1.8258 | -53.6691 | 2024-11-07 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 11b57782-2b6f-3dbf-9122-5b4ed2c714fb | 0.1748 | -51.0664 | 2024-11-07 14:30:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 50f5a848-a764-3279-b0aa-3b4d25613daf | -10.3016 | -42.3886 | 2024-11-07 14:30:00 | GOES-16 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 86.3 |
| af93adfd-1cc9-32cc-b1ac-9cb847f68caf | -1.1649 | -53.7377 | 2024-11-07 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 382dd9fd-1845-35f7-8063-cfc7a835d19d | -1.1466 | -53.7177 | 2024-11-07 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 722c5820-3300-3db9-8d93-81ff94a63ad1 | -2.2664 | -53.7221 | 2024-11-07 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| b4fe429d-b1d1-3017-8cc7-769abf8b865b | -2.248 | -53.7224 | 2024-11-07 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 99951ae0-4906-3009-92fc-44c80e6122e6 | -2.2482 | -53.6619 | 2024-11-07 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 651dbbb3-7336-3cf4-bc73-1d1a8d114371 | -13.9211 | -43.3685 | 2024-11-07 14:30:00 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 0b1bfa78-0f5b-368f-98c4-0215c7c52973 | -1.165 | -53.7176 | 2024-11-07 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |


