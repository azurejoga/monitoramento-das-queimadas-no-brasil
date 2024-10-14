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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6d76f8d-823b-3d1b-a566-1ee4a22526fb | -18.21147 | -56.8371 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.9 |
| d6e9943b-2d5e-34bb-b603-6f897757cd27 | -18.20551 | -56.8311 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 48e174f7-9f3a-3ff5-9b54-724700c7a60b | -18.20152 | -56.81793 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| f1f78fc4-ac53-302b-be42-250e3ca5a8ca | -18.19949 | -56.83562 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| d24603d5-b76a-34ff-b307-e07308701e2e | -18.19352 | -56.82961 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.1 |
| 6878210d-55ab-355d-b8c1-fab03e862f3e | -18.02704 | -57.34745 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 6e80e06d-5d9e-353e-b01d-bb260a6e33d8 | -17.98306 | -57.32543 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 093da222-b01a-3beb-ac3d-8a7c7de6bebe | -17.97542 | -57.29171 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.8 |
| 6d458e6b-5542-3a9f-a870-2d93eba73fb9 | -17.97536 | -57.38942 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| 6a4e3311-3242-3018-85e6-fa6671cb895b | -17.96965 | -57.34002 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.8 |
| 274790c7-ee2f-3fd6-90b2-ee3df86c84f8 | -17.96774 | -57.35604 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.0 |
| 9d2d6285-af4d-3bfb-af9f-563b1390f02d | -17.96415 | -57.30137 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1368.5 |
| 1bbf0d13-8878-31ff-a924-18fb93254980 | -17.96213 | -57.31744 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1068.0 |
| 772757a6-52fc-3d6e-bfbe-ae544f86f2d7 | -17.96202 | -57.40383 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 47f82663-fc74-33be-a7f8-3570dc5a1070 | -17.96011 | -57.33348 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 866.0 |
| 7a18fb2b-a14a-3907-a613-514880d154b7 | -17.96008 | -57.32248 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 840.1 |
| c40499a9-14c1-3b3a-a7a1-db721261b7ae | -17.95818 | -57.33854 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 684.7 |
| 24ce625b-5864-3573-82bb-3b8bca138a33 | -17.95809 | -57.34948 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 713.0 |
| be7b1028-4df3-362a-b449-81eb15a97308 | -17.95628 | -57.35455 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 779.3 |
| f235f772-3bc3-3080-a328-302f298ca7b6 | -17.95608 | -57.36543 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.7 |
| 5254deaf-b394-3f7f-8019-c58fc1b27172 | -17.95438 | -57.37052 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| f3684e0c-2e6c-368b-925e-466965893113 | -17.95264 | -57.29987 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 337.5 |
| cc66675f-f46e-31e8-bcf1-88ea44c9a7b9 | -17.95249 | -57.38646 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.1 |
| e56de0ea-d515-31fe-947e-6da74bd82b56 | -17.95237 | -57.28874 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 276.4 |
| c824104e-764b-307e-91e5-07594cc2f6d8 | -17.95118 | -57.21725 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| faf86060-938a-3a43-aa97-8bda98569dba | -17.95048 | -57.30487 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.7 |
| b1ac793f-eee0-3649-b165-6e9a5e944069 | -17.94859 | -57.32097 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| cadcd5c0-1482-3931-b388-2302d6b0cb19 | -17.9467 | -57.33704 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 90d2bf8d-9eaf-3d00-8e11-6ebda08cee94 | -17.94663 | -57.348 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 431.5 |
| a56cbcb4-1b6a-39c4-bf83-df757a219487 | -17.94481 | -57.35307 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 227.6 |
| be5db7ff-f605-3b86-bf42-3c6cc4b3bbf0 | -17.94314 | -57.28225 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 191.4 |
| 25a86e63-1000-35b2-b849-36e8b2161e90 | -17.94293 | -57.36904 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| b7da7c8b-3f92-3137-afd8-0366be5dd198 | -17.9416 | -57.1994 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 5e23e39c-83e6-3596-8558-4552188baddb | -17.94114 | -57.29838 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 398.8 |
| 4efb1251-a204-32db-ac63-4de6bf3f695b | -17.9396 | -57.21576 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| e3972311-98b4-3d86-a9ac-c8d892e6749e | -17.93516 | -57.34653 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| ca3535ad-94fe-32eb-8ffb-97d14ac65e91 | -17.93318 | -57.36249 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 193.9 |
| bff4d9bb-6cd9-35b4-8141-fdbc552a1aa8 | -17.92765 | -57.31299 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.2 |
| 8da51edf-15b8-3908-913b-75e2d5d70152 | -17.92603 | -57.2306 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 2f308ec6-ab82-39ff-9356-194957dec489 | -17.92567 | -57.32904 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.5 |
| b7f0b03c-0730-30b6-8647-7d4680be1ee2 | -17.92405 | -57.24687 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| bf4be841-b3bf-335e-b0c5-7b6681292188 | -17.92207 | -57.2631 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 22521dc6-c0a6-3771-abc0-b835e194afeb | -17.92172 | -57.36112 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| e71be4f5-e579-3bfc-8968-03b889b6e981 | -17.9201 | -57.27927 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1318.1 |
| 6885f5d2-8f46-39e2-99fc-759ad9e18b77 | -17.9142 | -57.32755 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| e1e5ba57-f0c8-337c-bc76-6efe868cddfc | -17.90682 | -57.19491 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| c804ce80-57fd-3a40-a3d4-73a0b274489e | -17.899 | -57.26011 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| e5867976-e201-375b-8775-d2f8b7711352 | -17.89705 | -57.2763 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 848.6 |
| d63ff20d-5b45-3bda-a4cd-02a96b9c3a47 | -17.89511 | -57.29245 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 536.9 |
| 76e3e2d7-325b-339d-8219-b656d6076e1c | -17.89328 | -57.20979 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 9af1712f-401e-340f-bae5-59758694909c | -17.88553 | -57.27481 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 659.8 |
| df709875-8258-31d7-9673-08e58528a7b6 | -17.88361 | -57.29097 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 580.1 |
| 4a6da339-c74a-3af8-bb3f-2fd0cc51e693 | -17.87554 | -57.28288 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 299.9 |
| 33ff926a-c568-3679-9748-9a5e4aedd188 | -17.87401 | -57.27332 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.4 |
| c8b1ef85-dfd5-30a0-bce0-e9d948f06f7c | -17.87352 | -57.29895 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 4696bda6-bdee-3574-afbb-f1eaa1a22804 | -17.8721 | -57.28948 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 279.1 |
| 5b7148a4-aa0f-3237-a614-22f9b61f6173 | -17.8663 | -57.2394 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 342323e6-ae83-3b35-8e74-6b40d53d87ca | -17.86404 | -57.28138 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 165.5 |
| 9e215653-1883-3b02-b8ce-caf6ecd287f0 | -17.86345 | -57.37871 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| c9aa6509-23fe-3740-9b34-d505001e01c1 | -17.86202 | -57.29748 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 291eceaf-bbe1-3022-920d-e02e7ff03806 | -17.86071 | -57.38539 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 5ec0ba29-c437-3a63-8a1e-0eba31471cb1 | -17.8606 | -57.28798 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 1ef76a0a-8969-38ed-ba8b-7d48108e2ccc | -17.85053 | -57.29599 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.8 |
| aee77f17-aa36-3666-aa92-dabedbda36c5 | -17.84102 | -57.27843 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| e709bf01-0427-3161-81e2-66d288d67ed0 | -17.83904 | -57.29451 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 53737fdc-fa6e-3c20-a78c-bf0c02d3f17a | -17.64736 | -56.2981 | 2024-10-14 06:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| f62cc324-5c9e-3890-9840-3ea8948ea5a3 | -17.20477 | -57.43003 | 2024-10-14 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| feb191fe-1f56-3c23-875f-87cd2a454a6e | -17.19183 | -57.43847 | 2024-10-14 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 622a6abc-b81b-3d5b-9a9a-1b95e65184e2 | -17.03386 | -57.42096 | 2024-10-14 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.5 |
| d144f8d2-c75f-313f-9cf4-c4e60e910947 | -17.02069 | -57.4347 | 2024-10-14 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| 92e80308-457d-3206-b279-17d5f094a219 | -17.01333 | -57.40279 | 2024-10-14 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 2c5a8550-d0e2-37e8-89e9-e45cf557230c | -17.0114 | -57.41803 | 2024-10-14 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| c89a427b-ce83-3597-8de3-5cc7804e184a | -17.00562 | -57.46353 | 2024-10-14 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| dee46aa7-6e04-38a0-bc93-90e8d199041b | -6.93641 | -71.77361 | 2024-10-14 06:25:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b31e3c9d-38c9-3a91-8bae-512718f99340 | -6.93247 | -71.77303 | 2024-10-14 06:25:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68328254-b6be-3f9f-ae30-0a5458a43a08 | -17.196 | -57.4357 | 2024-10-14 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.1 |
| 6f1f598c-b907-3426-b4c9-41df8e143220 | -17.1758 | -57.479 | 2024-10-14 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 254ce488-d7f3-35af-9001-2e595b9f12ff | -17.1954 | -57.4767 | 2024-10-14 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 7fb38c38-434b-3a30-bfdf-940b26bef164 | -17.1957 | -57.4562 | 2024-10-14 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 106b6044-082f-34dd-82c9-b3af52b38ca4 | -18.2342 | -56.6055 | 2024-10-14 06:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 24e19603-0805-39ca-8ac7-f96414d89d14 | -18.2555 | -56.5196 | 2024-10-14 06:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| ad4319b1-b811-3c35-821c-6820a394907e | -18.2754 | -56.517 | 2024-10-14 06:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 86110b6b-10e0-348f-a9fc-69c6397a56d3 | -6.93459 | -71.77272 | 2024-10-14 06:50:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| befd3df4-41cc-3da6-8c68-bcf4ba9dcb58 | -6.93399 | -71.77731 | 2024-10-14 06:50:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 189a46dc-783e-3645-a855-f9dd9da631c3 | -6.93303 | -71.77509 | 2024-10-14 06:50:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 837d90cb-dd54-38be-a7b0-26c342c183da | -6.9324 | -71.77966 | 2024-10-14 06:50:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7071227f-cada-385a-9676-dd412ac63173 | -6.92853 | -71.77196 | 2024-10-14 06:50:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22281cea-ebdc-3490-9e36-0e5df2e7d193 | -17.196 | -57.4357 | 2024-10-14 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 50cdf203-aae9-3a4c-8201-3ff4421017af | -17.1957 | -57.4562 | 2024-10-14 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 9bb1e012-6a4c-32bc-af2f-e5688a28e4dc | -18.2754 | -56.517 | 2024-10-14 06:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 47f56b2d-b6dc-31db-88bb-c8804333feff | -18.2559 | -56.4988 | 2024-10-14 06:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 59a3585a-6934-37f5-8689-6c6e36e8d518 | -18.2555 | -56.5196 | 2024-10-14 06:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 389473ad-4dac-317f-a272-68b52019a8ed | -17.93 | -57.3 | 2024-10-14 07:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 29245050-9b02-351e-b0ee-95e07ba280dd | -17.96 | -57.33 | 2024-10-14 07:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 545e1e39-c084-3b87-9421-5cc3dbbdb12c | -3.32 | -42.83 | 2024-10-14 07:05:07 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0beefb77-c2e2-32bf-bc14-524b475361a6 | -3.29 | -42.83 | 2024-10-14 07:05:10 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56247058-0590-32b3-9eea-3431d4bd1815 | -18.2555 | -56.5196 | 2024-10-14 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 7a827f8a-6959-34dc-aa47-e03f1fb155e4 | -18.2551 | -56.5405 | 2024-10-14 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 42b8b7af-9800-38d9-b5eb-5456c62a3870 | -18.2559 | -56.4988 | 2024-10-14 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 6d3a7064-a1bf-3f4f-9846-47450edee922 | -18.275 | -56.5378 | 2024-10-14 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.1 |


[Clique aqui para ver as próximas entradas](README130.md)
