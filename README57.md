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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03764261-873a-3a47-8c29-d07aa42e8162 | 2.7367 | -60.39043 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4fff0685-e159-3d59-b7de-21c5709d90ed | 2.72937 | -60.38785 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8558e8c7-d9e6-3b56-9952-e615c81ec1e4 | 1.3288 | -60.72336 | 2024-12-03 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8526b934-4660-3284-ba66-27ddaebfeff4 | 1.10046 | -55.99086 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 194b0152-f431-33a5-9715-69c4b4fc9e91 | -2.61698 | -60.02243 | 2024-12-03 05:22:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0e0d75e-c1d6-30a0-b74a-49736446252c | 1.32541 | -60.72388 | 2024-12-03 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32cd1f3e-4760-34b4-b5dd-f1f393f9e38d | 1.10745 | -56.03617 | 2024-12-03 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a25e5816-952a-321d-829d-715ad47232ca | 1.30791 | -60.41033 | 2024-12-03 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd4a6bf1-171f-34f0-9feb-e36e82f41fac | 2.57692 | -60.69557 | 2024-12-03 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25dc43c4-c94c-3b91-91f9-e86ea7df2be8 | 0.91003 | -59.44882 | 2024-12-03 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9d36224-1abf-3277-862e-d67a28959f21 | -2.82012 | -53.0602 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0853e4d0-7883-3096-ac54-59497bb2a188 | -3.08602 | -53.37819 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b6fde06b-a737-394d-9539-4eff0883abe8 | -3.05132 | -54.85197 | 2024-12-03 05:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a129e387-731a-3ed0-b2e2-64cd4cb0b570 | -3.31023 | -53.36756 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b482aaa-e920-3f89-9870-889a77a6aa5f | -2.81185 | -53.05251 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb5e3739-85f9-3bd1-b42f-900656cee857 | -3.02124 | -54.01883 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a90ff78c-7aaf-3fcc-a03c-8aa68c3bd1d1 | -10.0549 | -59.12147 | 2024-12-03 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3e00ca3-f2cc-3e34-8518-dce903cc9cd2 | -1.07415 | -62.6432 | 2024-12-03 05:25:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 79c7e94a-5ddd-36e0-8580-d991d979511f | -2.26714 | -53.60585 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f793800c-e040-3cd2-8cd1-87a6a9d64c16 | -2.33506 | -53.81085 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bb15fc9a-bb31-33fa-a4c9-6cec849afdc3 | -2.79033 | -55.35204 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61825b16-eaee-39f7-bd6c-828d719c4982 | -1.51806 | -60.32611 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 614b6630-5be9-30f1-817a-aa92b9a46a39 | -2.81113 | -53.0572 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3cde9636-736a-3ca4-8ac9-6a5bfbf5ca42 | -3.26623 | -53.34087 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb506996-9e39-33e4-b0e4-baf6d6c8456a | -10.45458 | -58.68498 | 2024-12-03 05:25:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a06d809-7dae-3456-bffb-574f242eec54 | -3.03141 | -54.18492 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf79472a-a5ef-38da-be4d-08d20363aba4 | -3.25555 | -53.65404 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54c0875b-949f-36a2-a2f4-c747aec06190 | -3.07711 | -53.09874 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 492170d1-f0ef-343d-a383-d6ad0abddb5c | -1.2569 | -54.53932 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3cf3a081-132f-3c73-a805-0b08b2b3b549 | -12.57818 | -57.80677 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8f0824e4-c5bf-302c-bc70-015bdca95814 | -2.4354 | -54.03497 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a596076-e454-33b6-9ac0-2afaa6511f1f | -3.37907 | -50.70403 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f1c9b53-bf4f-30ff-a723-b08285f7b39c | -2.8925 | -54.15715 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27b20dba-4ee7-3882-b8fb-55b7f63d9fee | -3.28447 | -53.25006 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e805bf19-ea2e-3460-9823-b2e7b9d4a15a | -2.77716 | -55.35888 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 552e4fc3-1944-3397-b547-d44f8dcd77bf | -3.05349 | -54.50124 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c64dc667-4682-34e8-a990-66b447c99f00 | -2.3873 | -53.71072 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a84c9e84-0393-3f43-8272-8b775e0ac9ac | -3.07894 | -53.37875 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8c748315-3647-39e7-b336-1498833092f6 | -4.16845 | -48.5923 | 2024-12-03 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 154e0483-3aa6-3968-a3b8-06874c8524b9 | -3.02521 | -53.87184 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 26cf820e-957d-31f7-84b4-f5b884604d3c | -3.25423 | -53.6627 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 33600c98-8abb-31c1-b111-e660da58bf3f | -2.79425 | -53.04495 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9073d50f-97b7-3d58-a91d-0247bf37f54a | -3.15563 | -51.11559 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f726c1b2-804e-3013-89b5-dccb3f950e44 | -2.74752 | -54.17221 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9a89344-1c5e-3693-8673-5150df1d0e41 | -4.16148 | -48.59607 | 2024-12-03 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bb42a2e3-a5c1-300d-9b4d-6e68ac188cf4 | -3.23323 | -51.7319 | 2024-12-03 05:25:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dbddd775-6b6c-3a04-be56-9971e6503459 | -2.7252 | -54.17735 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b14a2c8-82bf-3c79-9a2b-b19f527e68e6 | -2.65038 | -51.89504 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cf4881d-9499-31c4-a7fd-0d18d4e8774e | -2.89627 | -51.7969 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae11b4ba-d25e-349d-9807-b811fccdfbba | -2.81644 | -53.05323 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15c53d65-923f-3e90-8cc9-372c78e14f37 | -2.78026 | -55.36588 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dc47edd-0891-35c4-afba-d85a219dfd4f | -3.11107 | -54.05275 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 867dcdc8-f9f6-3f1e-aee4-50b4c7cd3157 | -3.21029 | -54.17324 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac4a2431-cacc-30a3-a570-bfba9bd025cf | -3.18162 | -54.33797 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 671a8c75-e486-33f8-8d97-d45ad0660aeb | -1.81213 | -52.73922 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d55dcea-f56d-3290-a386-cf870e201107 | -2.80911 | -53.03921 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa44052c-67f9-38d1-b319-c20eaa62b9c4 | -3.11936 | -53.80875 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbe628e3-3462-3f90-8dde-de0b1e70a478 | -1.36386 | -53.64986 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 382349fc-6b3f-39c9-a661-3413d0a3ea54 | -1.42759 | -55.30736 | 2024-12-03 05:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07100e13-f467-362d-9da0-56ac4bfcc678 | -2.781 | -55.36088 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cfc1c34-cde8-3937-9030-b4784d0185ff | -2.76433 | -54.05734 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5900bef9-8192-3e36-8633-d3d9e9573001 | -2.80198 | -53.05576 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0238736-a39b-35d9-aaac-8050815ea50f | -3.11698 | -53.98247 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79dd44b2-a165-3cbb-af6a-b2eabab314f2 | -3.40378 | -50.23348 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c354e8ae-51ea-3563-a558-d51c02ae2102 | -2.26276 | -53.60522 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e70d7a7c-705f-39cf-9d9f-e8f348887c57 | -3.17661 | -53.63683 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dda808d-f37f-3a04-9403-aa3ec72f8e45 | -2.61312 | -54.08894 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 88b1834c-607d-3c02-a96e-746a6624cc38 | -2.33937 | -53.81152 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6482267f-1abb-37cc-84bb-1eefb5cd29a0 | -3.24699 | -54.21955 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d20ef634-0bc6-3b6f-90ed-684ae43847eb | -9.18443 | -62.38875 | 2024-12-03 05:25:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8817bfe6-c087-33c8-8b86-8f18b26fb014 | -3.25887 | -53.63231 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b79dc719-e2e0-33e0-b2ff-1db21a70bdad | -3.25377 | -53.63598 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e299380e-6281-317e-9bae-55e2726d4fea | -3.09923 | -53.23104 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8f716e0-056b-3064-b4c7-eb2d8e0b5f6d | -3.47951 | -50.25095 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21be6ab0-069f-379f-b7b9-fdc123ebb7f8 | -8.96332 | -63.64007 | 2024-12-03 05:25:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d77cbfd1-ef07-3f51-afea-259e053bf050 | -3.3796 | -50.7005 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 763ec9c7-d675-3e83-ac13-df4cece47e37 | -3.36491 | -54.06611 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11d1270b-43e4-3bff-827e-55d1c45eea50 | -3.10678 | -54.05204 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0807a5a8-f6b0-3b38-bfd3-ab2a7860eede | -10.68874 | -58.61562 | 2024-12-03 05:25:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82f7a7aa-6da5-3b61-96f4-e074933252b0 | -3.38713 | -51.14846 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55ae646c-1dec-35b8-87ab-2c5f7725763b | -2.8208 | -53.05549 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fda45c6a-b1ae-3a61-b394-4514982821fb | -9.18777 | -62.38928 | 2024-12-03 05:25:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f01470a4-78e0-35cb-a489-0189bab6c0db | -3.26428 | -53.6214 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7554828c-a7d7-361a-85ad-a01c49f9772e | -1.78766 | -52.74513 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2484eb7d-4485-3aaf-a694-8615b8d69c92 | -2.90291 | -51.37166 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe4b1e2f-cdb0-3231-8e72-c350bc7d85dd | -1.25635 | -54.54286 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c297edf-1eac-3e32-8a63-22a33c12f81f | -1.24882 | -54.53798 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8cc71105-d947-39c3-9d9a-64356bd09bb7 | -2.78566 | -55.35647 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d3a4d58-2cde-3985-b55c-abf2bbcefdc3 | -1.79963 | -60.06968 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f914f76-8eed-3659-982a-854db86981b9 | -3.34991 | -51.21856 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06fd8caf-9d7e-3dc5-adb4-14057db8de49 | -1.27152 | -54.1152 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dabfb4d0-2df7-3e21-9e8f-4de16cbda555 | -2.81759 | -53.04536 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71993c24-83be-3ebd-ac46-9a4487a09498 | -2.55791 | -53.40719 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c12944c3-7b37-364a-86b4-d8e0c8343b01 | -3.31101 | -53.70387 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91415a2a-3eba-31fb-9aaa-aea0bb68978f | -2.77953 | -55.37086 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46ab5969-4619-3d69-939e-76ec867209fc | -3.26364 | -53.62581 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92c45e49-8f3c-3c55-82f8-9df9178f09f5 | -3.55225 | -51.52048 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09876f0e-9792-383a-bcbb-e2545da1a8df | -1.46876 | -52.68349 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95193fd0-f296-3d9c-9fe8-c34547d2ca99 | -2.63447 | -54.40842 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5152931a-5859-39e5-b6f5-1707335e7940 | -3.34607 | -51.20818 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README58.md)
