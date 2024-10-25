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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b83a1fb-6937-3ff3-a925-a0b4c70c0a87 | -4.16063 | -53.4817 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fc7d57a-e0c8-3859-8c4b-b305c76e1ad8 | -3.81521 | -52.69208 | 2024-10-25 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0699e0ee-74be-3c35-8e88-7a173293c509 | -3.81144 | -52.69142 | 2024-10-25 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 496c0e74-0b7f-3c93-b955-3a28d1b87926 | -3.79625 | -52.28628 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00e5df2c-3baa-301d-8f31-2a0108ac26f8 | -3.78727 | -52.38788 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc33568b-79e1-3b39-a034-58f2bf784177 | -3.77574 | -52.31874 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 095ce6df-9508-3f08-9651-fda2649fa474 | -3.75254 | -53.40733 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2088a65-73d4-35fb-8cbc-87d8d8a7f093 | -3.71121 | -53.71147 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d063bca-3ee0-3c94-b9a4-96dc2925d928 | -3.69033 | -53.42664 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5371987f-de25-3cbf-83ea-7ae0be7fffdb | -3.68952 | -53.43177 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99562c48-d5f3-3e80-8d81-c44ce9c296db | -3.68638 | -53.42593 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87232a50-fd62-36b8-a07e-69adbdec52a7 | -3.68556 | -53.43107 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca34625a-a52d-3316-b361-1aaa57f2b42e | -3.56358 | -53.75178 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ea016c5-e488-3cdd-bb7e-c982fcbde408 | -3.55953 | -53.75116 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea9dcd14-3552-3092-8303-c53a10643209 | -4.11856 | -53.8382 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e9a25bb-c9f6-356e-8011-bfbf7e6128c4 | -3.99338 | -53.43 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96215e8-c3f9-3823-b555-1d4e5f1e9d55 | -3.99257 | -53.43502 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3ae10d7-c86c-3ecb-bc30-a65b59cd66aa | -3.98863 | -53.43439 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0b13941-4840-3dd7-8459-283e7fd7dc59 | -3.89603 | -52.31348 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a552c05f-ee80-31c5-bddb-d59936ac5047 | -3.8792 | -52.34661 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e57d76a5-7d0c-340c-8be4-05bffc38162a | -5.70235 | -53.45784 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da906bcd-e48f-356a-be50-c98aaecf042b | -5.6985 | -53.45714 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2dc282f-38f7-3842-bd65-e856a98d398a | -2.1537 | -53.64344 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5aaf1e0-6d89-3167-a9ec-8b316de13089 | -2.14431 | -53.64954 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb18382f-2858-3916-ac48-0abd77433ccc | -1.89714 | -54.61996 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09374a5b-8ede-38f7-a2bd-ecf0c1180421 | -1.89646 | -54.62428 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 759e8411-f3e0-3a0d-bf0a-84e5929f176c | -1.89609 | -54.62249 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f04a2b5-b9b4-3b66-9d40-b6893b19560c | -3.13944 | -54.27843 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a18e3d20-3bb7-3049-bb2b-1390db4be575 | -3.1388 | -54.28229 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f485ddc-88cf-3b90-8289-741b73977954 | -3.13816 | -54.28617 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de9e285c-f252-3a37-bf57-5d4c2064c88e | -3.13641 | -54.2753 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b92ec257-d56d-366d-95e6-710788506b95 | -3.13586 | -54.27388 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bccbfc0a-8a43-3f92-9c55-943d387a4266 | -3.1358 | -54.27913 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8a7c9bc-25e8-389b-b65b-7ce0bad9d6ed | -3.13523 | -54.2777 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27f7439f-2d3e-3d99-81e0-62b0a1644c82 | -3.13519 | -54.28302 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e35a7e4-08f1-3d76-a4c6-b67fd572ffae | -3.13459 | -54.28156 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3b7714a-f7dd-34d3-9b3f-711f3d616908 | -3.13219 | -54.27456 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a711ce08-2cdb-3df1-bedc-9081369f0db4 | -3.13165 | -54.27314 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4124e3d0-f521-3a21-9917-57048b932790 | -3.13158 | -54.2784 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4707a5b-2755-37bf-aa03-5ff0c85b5b6f | -3.13101 | -54.27698 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b290b32-6e6e-3c3d-a541-9e0e5cb6f4df | -3.13097 | -54.28229 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 904b3ef7-f133-36e5-9cd8-485f94e3f1b3 | -3.13037 | -54.28083 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84e3e274-8003-38e0-8a71-065e038eeb3b | -3.12736 | -54.27769 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75b5e50d-da36-3dea-beea-8fa4451f3b30 | -3.12679 | -54.27626 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a94bda8-d55c-34d5-9d5e-a97da65d0b9c | -3.12615 | -54.28012 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6219e70-ae11-3bff-a278-fab79b392f36 | -3.11037 | -54.16808 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a7393e6-c9ef-3daa-a7a8-c976c777ed54 | -3.1092 | -54.14869 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed6c7436-3a81-38ae-9b82-8bd0b7d67d3f | -3.10859 | -54.15247 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd13d9cb-4a37-3539-9588-a5884e77ed33 | -3.10798 | -54.15622 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7057bd03-2ac2-3d68-a4de-bbe40933e0e0 | -3.10738 | -54.15994 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e5ec440-bdd2-38cb-b2f7-d3ed54cb2827 | -3.10678 | -54.16367 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 026fd657-30f1-35bf-ab2c-28a44906c1a9 | -3.10617 | -54.1674 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9b792ca-e075-3ccb-be42-7a2c22debc74 | -3.10557 | -54.17115 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79c75e0d-5073-3748-a4e5-e9720fc24770 | -3.10501 | -54.14805 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e6ded7-957c-31b5-9f02-9ddf525088e2 | -3.10439 | -54.15183 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ad374e-9e22-3709-9352-30357ebd6a13 | -3.10433 | -54.17881 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5d2dac6-4c3b-3804-b07e-6c13ad8709d3 | -3.10379 | -54.15558 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645d7e0e-e498-3a4a-8691-a393f7048f8c | -3.10318 | -54.15929 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bb28423-3ada-3bb1-ba80-b51f0a6b52e7 | -3.10258 | -54.163 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a846650-8b2b-3101-a669-1a297d73d57b | -3.10198 | -54.16673 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| add1528c-b74a-3d4a-8b62-a819ff12519b | -3.10075 | -54.17427 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a920f5d4-5ad6-3432-bda2-3fa0877a1b88 | -3.1002 | -54.15114 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15cc0595-8a6f-3de7-9261-1c975daaa5be | -3.09959 | -54.15491 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bab330bb-b802-3b89-bff1-9398c3829b71 | -3.07975 | -54.17097 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa35d67c-f9df-3a56-8f97-de3c6f55dc50 | -3.07367 | -54.78228 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d11d24d-0cdd-3257-837a-905513b30a14 | -3.06929 | -54.78156 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6db83dbb-cff3-3418-a555-58f87eaaafa9 | -3.0686 | -54.78573 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 398f2181-8579-3ed4-8d9a-89a1caafca37 | -3.06422 | -54.78506 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47249750-9559-3085-9b06-df6e0dd01056 | -3.04851 | -54.85253 | 2024-10-25 04:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f2d5c4e-4112-34ae-8b70-b94fac5eeda3 | -3.04363 | -54.18085 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6164635-02ca-3214-bae9-a9f324b73cfc | -3.00741 | -54.13631 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1d0f762-1a37-3cf7-aa34-50a1072ed39e | -2.99373 | -54.11452 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9749fa30-198a-378f-b910-2c1fb7599666 | -2.65926 | -54.62598 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c29ad100-9c4a-3336-81e4-9136da95fc7f | -2.65491 | -54.62527 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f5cce60-f84d-3bdf-b461-e127c7b56644 | -2.50217 | -54.14236 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2d1c97f-69af-306b-85da-b2cf53d73cf4 | -2.50162 | -54.14101 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1494d055-9714-3a61-9eda-820bcef846c0 | -2.49794 | -54.14167 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 813f9e18-7a1f-3959-8ffc-4ef9847b3c4b | -2.17125 | -54.47805 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b166bb-8e83-3208-85dc-fcb225f4af03 | -2.15521 | -54.92787 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f5724c8b-10b1-31c6-b7d6-08ef5f608d2f | -2.15339 | -54.92889 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 182a8850-88ba-33a5-87c0-29a2a2b749e2 | -2.99435 | -54.1107 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf839aa9-0999-3328-9d78-c42c94689a26 | -2.95265 | -54.15508 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 900e89d6-0afc-3a2f-ad67-b63dd1cdb4b1 | -2.94475 | -53.70116 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ecd7df9-52cf-3640-9128-7e9c62447ea1 | -2.93632 | -53.90953 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 170530c0-300a-3e2c-9e78-4125d8b7fc73 | -2.93572 | -53.91325 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc0a0708-321c-3d6d-b113-5cc7f1940dd5 | -2.89341 | -53.99053 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72629cbd-f67b-3fa4-be89-619e067ce85c | -2.83487 | -54.26931 | 2024-10-25 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed99098d-8900-3ca6-82c2-e44e53660a62 | -2.8007 | -54.10759 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee0e8902-b5fa-3d8e-b50c-6147a5edc060 | -2.79711 | -54.10308 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b39c0e3-46be-3c64-bef8-eda31f669b87 | -2.65995 | -54.62184 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2f14c89-98e3-31c6-b924-214b87ba7e85 | -2.65559 | -54.62115 | 2024-10-25 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 031341e8-e006-301b-bc5b-a7ff77ebff19 | -2.56528 | -54.01627 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c83ac16a-74c5-381c-8f18-ab0173a1bbf6 | -2.49856 | -54.13776 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e0c416-e8a0-329a-a3cd-f8930a92a797 | -2.49371 | -54.141 | 2024-10-25 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a89975f-f38c-37c1-abf4-56fdd32016e4 | -3.1204 | -53.7175 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff0d3957-bec7-38d3-97f4-3e14546ba963 | -3.11981 | -53.72109 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dabda51e-3914-3b6d-85fc-35bc6739f5ee | -3.11455 | -53.72761 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5d474f6-687e-39d8-bd2a-57a02b1bde12 | -3.11093 | -53.72729 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2910b0d1-b9ec-30e4-8f1c-621cdd53e0e2 | -3.11048 | -53.72696 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29fbb1ff-5925-371d-9601-beb7a087368d | -3.11036 | -53.73088 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README68.md)
