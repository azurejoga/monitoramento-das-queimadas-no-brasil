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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d210c43c-203b-3527-a701-fbeccc55f623 | -2.45405 | -53.98365 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63c0e5b6-357f-3ebf-89cd-20673da1f8a6 | 2.73672 | -60.39405 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d2f63e4d-f264-3d97-9a22-5ed845c0a688 | 2.75822 | -60.64283 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6fdfb0a8-99c4-38cb-aff5-b5aa2f1b3404 | -3.07073 | -54.08369 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dd0638a-4ec3-3d44-b736-8598bdcd8341 | 2.75777 | -60.63979 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3d94235b-da58-31a2-a5fa-4f0a27a6e2b0 | -3.12897 | -54.06073 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f028fb7a-466c-3577-aa76-722c3f24d2a6 | -2.83285 | -53.06227 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1ccbedf-4ef3-3882-9f76-0c94239d95c0 | -2.57042 | -53.95546 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fab3db0f-2d39-35e8-ba36-eec75bb85d9d | 2.75308 | -60.64361 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7ced9e47-e3a9-3616-8a4a-22b74ac85c44 | -2.96511 | -53.72673 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a07605f0-50e9-36a7-b7db-f3aa225d805a | -2.41381 | -53.66163 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 188fae32-6a4c-3892-ac0c-e0c8d519391c | -3.11624 | -54.07654 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94844fcd-0e0c-3f92-88b2-6f8ae30b5f1d | -1.41521 | -55.14103 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24248a78-78c0-3aad-95a0-cc52dc61b124 | -3.12513 | -54.08505 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8546e5cd-8500-3eda-9ada-c66674afbc2f | -2.83563 | -53.06624 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 748bd490-8d56-3d53-bd80-22249f284819 | -3.10625 | -54.07498 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f29d7f74-5c27-35c8-8c84-75e7a3edb177 | -2.83007 | -53.05829 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63859028-c54f-3083-87b3-df47da04bda7 | -3.10903 | -54.07898 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38444f91-f7ec-3dc3-ad14-f216a0cdc474 | -3.06892 | -53.79958 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a04bb48-2731-3cd7-963b-8e3a40c0457e | -2.47937 | -53.62925 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3766cd9-a6c0-388e-a5f2-85e2630bebeb | 2.75732 | -60.63677 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5902a710-089e-34a0-a2fc-7a5e09888d8d | -2.5833 | -54.34016 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c01e98ff-3624-3c77-98a9-30f09eed772d | -2.4089 | -53.69273 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9675c15-4c59-3f02-8dd1-713786edc1de | -3.17836 | -53.8555 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c25d805-9595-370f-9de9-f99fa1f6e9d7 | -1.94298 | -54.41068 | 2024-12-11 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d942163-b6d9-3cc4-979d-765d4435aecf | -2.96086 | -53.1111 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b055cdd4-b0d8-328f-b058-c4112d649632 | -2.95313 | -53.11697 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0390ca55-53a6-383e-b15b-a20dcb9e89f7 | -2.83727 | -53.05587 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c32e10b-ede6-335e-95ae-718daded29f1 | -2.45804 | -53.64022 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f7b3d35-8fc7-3a81-84f7-517874e6a063 | 2.75264 | -60.64058 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b9c6c3d4-9371-32a8-bc55-ff7a21a5e04b | -3.24381 | -53.91242 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9f987fb-231e-3001-961d-a2c7bb57328c | -3.59831 | -53.7233 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2240ea95-0a03-3d19-a60a-c30ebf172918 | -2.83672 | -53.05932 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d34aa00-afe4-3697-a495-0e311b6a775b | -2.81128 | -53.06953 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 677195ad-9fc0-3105-a4e8-d176e87133a0 | -2.8334 | -53.05881 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3022763a-587a-3ed0-887c-3f711479a350 | -2.95846 | -53.72569 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd4d62e0-8a49-309e-b091-7e18d4c43279 | -2.80144 | -54.18832 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91de5087-8efe-3d69-b84b-941c6522b4c9 | -3.17504 | -53.85498 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26c1c33e-7c56-3226-a22e-27dcee5bd860 | 2.75687 | -60.63375 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 980f29cb-1747-3c52-86d4-890deee56887 | -3.12404 | -54.092 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe3e3ae0-d2c2-34f6-a409-3446291b9738 | -2.47496 | -53.63563 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db472418-bd2c-3521-9047-a14c89161dee | -3.12842 | -54.0642 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc28aa8-a920-32e2-a5d1-5dde6be20f10 | -3.06795 | -54.07969 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cf18455-0560-3d0a-8d68-c8aa2b4abc18 | -3.51623 | -54.17861 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 302309f6-5a26-3a31-addc-303675c521cc | -2.78729 | -52.86016 | 2024-12-11 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 317f235b-e162-32ff-9339-6b742ffb8776 | -2.81502 | -53.02406 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5bbf633-e39f-3654-a811-0f48cfaa00c5 | -2.64632 | -54.28886 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d7d90eb-1b08-34fa-b2d3-2577946c667a | -2.47605 | -53.62873 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd262c16-e464-317b-86eb-c488dc0bdd0c | -2.4829 | -53.71474 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2a8139f-22ab-3c4a-a5b5-3e222fc008fb | -3.09533 | -53.73994 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 694b7d48-797d-3770-a190-c1955b237b5b | -2.957 | -53.11404 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a29435ac-d82f-3e9f-9e7a-58011eeb951a | -2.64967 | -54.28938 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72ad878f-cfa4-38ed-b63d-e79ff6b58acf | -3.03001 | -53.40105 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 209a0bea-3dd3-3534-a9ea-41bb090bd462 | -2.83394 | -53.05535 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dea321f-0f49-3f7b-92e1-f3054d0a4d5c | -1.72335 | -53.18933 | 2024-12-11 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2965d846-bd29-37a8-b35c-d0bd362075e3 | -2.10754 | -55.30832 | 2024-12-11 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b740128d-fa13-3f53-82d1-76e5a91d4935 | -2.61618 | -54.24107 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ff7432f-766d-3a43-a88a-81f4296375a5 | -3.10848 | -54.08246 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf5aa61-4699-36a0-aeb9-aabf597761e2 | -2.80186 | -53.06453 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6834987-0645-357a-a43f-80c68f0b9a6e | -2.47957 | -53.71422 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9efa691f-80b9-33ed-8eef-8634cf3f8c6e | -2.6736 | -54.26801 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7b05f65-cbc9-37ed-acd4-24a3e34bab93 | 3.22696 | -61.19779 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a13e3fa-e869-3b71-bc99-a64972662c3d | -4.59195 | -47.83594 | 2024-12-11 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 66d04577-4e9c-313b-bdd5-a5f66e777c88 | -1.90238 | -54.55751 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b13bdeca-9178-3eab-964c-12baf9dc892a | -2.64473 | -54.38593 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72e880d7-c70b-3c19-b01a-98666623a2ec | 3.22595 | -61.19112 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17daade3-5db7-36be-9b38-13195ecc1a6b | -3.10119 | -53.76197 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52ada1f1-e1c6-390e-8345-6d0ea140474b | -3.48153 | -53.82188 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a61b5904-93a6-3d7c-971d-b80e44cf263e | -2.95754 | -53.11058 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fcf5468-d4ca-3eed-beb8-30ccdee21af5 | -1.39934 | -55.0852 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3781bc30-5a5b-30d4-a6ce-8d0b8e90efa5 | -2.47328 | -53.62476 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a3b888-2eba-3778-820e-be99666e51e7 | 2.75867 | -60.64585 | 2024-12-11 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3dab63ab-4e00-31ba-9bff-66b5999991d2 | -3.12454 | -54.06715 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8e8f63c-10ef-3868-88fe-ecc384728f85 | -2.83231 | -53.06572 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e3ee4d4-0cea-3350-9680-baf86d493434 | -2.48012 | -53.71077 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12f70f27-1325-349e-8c9b-4d259a9f9b13 | -2.81183 | -53.06607 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb807c0d-5365-3e11-85ce-111be926095d | -1.34287 | -55.00428 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f8d768f-7cbc-3884-b8b2-197ad660abd5 | -2.81266 | -53.96537 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90ac60bd-f8ad-3417-9405-736b7e9bb0ac | -2.81461 | -53.07005 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c596b4ab-183e-38db-a256-15ec85da0139 | -2.82403 | -53.07506 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 152e0000-51a0-3c82-b5d1-cf70e4a64f42 | -2.82566 | -53.06469 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24dd252b-a5cf-3aeb-8f71-fec978bc63f9 | -2.34554 | -53.85658 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fab28be3-96a9-3b94-b8ed-1c9c994f22e3 | -2.26242 | -53.84722 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dc87f56-829a-3ded-a846-c9fa37a03446 | -2.96032 | -53.11456 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5512ff17-0a97-3862-b250-5abd8905eb90 | -2.56988 | -53.95893 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b11b1114-931b-3722-ab43-8b0fe8c2db14 | 3.22966 | -61.2016 | 2024-12-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bbf395b-f4ce-3e11-a81d-4d30f3d617fd | -2.5794 | -54.34315 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57a0c732-d43c-3ea1-b786-0f92484c0df2 | -1.4158 | -55.13726 | 2024-12-11 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b8c0cb5-09d4-3777-93db-2f331e37d599 | -2.47442 | -53.63908 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81a91e13-b6c8-307c-bbf5-c532a60e98a3 | -2.7862 | -52.86709 | 2024-12-11 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1200aeba-521f-3a72-98a8-d98b7026eef4 | -2.81237 | -53.06262 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95aa9ef8-d51f-30bf-9801-c6a42b6166c1 | -3.10958 | -54.0755 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18d64574-3ea9-31a4-9899-92df31f45c03 | -3.12126 | -54.08801 | 2024-12-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb7c0409-6798-365d-8968-4a7ff72c1f8f | -2.47551 | -53.63218 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e151274d-9737-3041-903b-5a2ab1b1eb83 | -2.96178 | -53.72621 | 2024-12-11 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d138824-619d-3d5f-a9e3-6782f1de2643 | -2.45738 | -53.98416 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5977bf80-e1e7-366c-96bf-2422f5e968b8 | -3.10451 | -53.76249 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e626cd-82cc-3cdb-b9f8-29109fb96a4a | -3.60218 | -53.72037 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2ba77019-be12-3157-a62e-3d6c0b148fb5 | -2.82926 | -53.94663 | 2024-12-11 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f1fceef-a1fd-3447-97c9-23a204f7d9b7 | -3.09725 | -53.74374 | 2024-12-11 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
