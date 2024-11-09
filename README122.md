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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df7fd651-0f73-3b0f-a112-e258695f2430 | -0.2299 | -51.6249 | 2024-11-09 14:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 69.6 |
| c2435356-64ca-3c91-bb28-36d52be10b85 | -5.4734 | -43.2646 | 2024-11-09 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fd344db0-5ad1-3804-8e9d-fe0097f9bd72 | -2.3556 | -54.7427 | 2024-11-09 14:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 206f5276-00bc-3baf-a3bf-0cbe787eb691 | -2.2804 | -48.7226 | 2024-11-09 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 3ff09932-fbea-361d-96ea-ae89e0f105fe | -6.1366 | -42.5544 | 2024-11-09 14:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 7c21472f-7b54-3491-9b4d-6d4faa95ebeb | -5.7146 | -43.5261 | 2024-11-09 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f6f5fc16-c0d4-3835-b0de-87ff90ddcdb4 | -0.3034 | -51.7071 | 2024-11-09 14:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4f95c56f-afb0-31c2-a23a-aa216f82c3fd | -3.5462 | -43.5663 | 2024-11-09 14:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 59625f3b-68e2-3dd4-a3c6-bfaec581d7d6 | -2.3733 | -48.5703 | 2024-11-09 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 9a1fa0af-6584-31a7-b11d-d3d03d04f0a7 | -2.3555 | -54.7627 | 2024-11-09 14:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| bd21ee0d-bd1c-3bc8-8d5b-28a6fc3e93c1 | -17.6083 | -57.4482 | 2024-11-09 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.7 |
| e7aa8320-57f5-379a-9c0b-8428338cc8b4 | -2.3076 | -46.0391 | 2024-11-09 14:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| d2917176-57e0-38c4-a5df-cac6ad4f32eb | -1.5347 | -52.1694 | 2024-11-09 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 66d31abb-4c26-3122-a41b-619b758e5121 | -11.0881 | -43.3219 | 2024-11-09 14:00:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| d32f2fd9-68cd-3592-ae23-75118ad5b6d4 | -3.9483 | -48.1724 | 2024-11-09 14:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 122a1746-0c1a-3c9e-8c39-b2f97f2c2db2 | -3.2353 | -50.2645 | 2024-11-09 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 381.8 |
| 13cef828-1157-39ca-8cf4-5f35d96ce1b1 | -3.9002 | -50.3042 | 2024-11-09 14:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 188.2 |
| c8127b5b-62aa-349d-a1b2-a86a724d0edd | -2.3604 | -46.8776 | 2024-11-09 14:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 23e5546b-2d31-302d-aa1a-ac7a375081bb | -2.646 | -49.8819 | 2024-11-09 14:00:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 1c626c27-dd94-3444-8cba-f1ea63240ac7 | -3.0319 | -50.3547 | 2024-11-09 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 199169fa-ee59-3664-b4b2-64b90ec56c09 | -0.5992 | -49.5352 | 2024-11-09 14:00:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| edfc6c09-c342-3687-86fa-3011a8f84917 | -1.498 | -52.1699 | 2024-11-09 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| b1d969ac-ab99-313a-9806-7e2cfb9b068e | -1.5164 | -52.1491 | 2024-11-09 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 1da0c612-4d4f-37b4-bd7d-d188702d0d7b | -4.5713 | -43.789 | 2024-11-09 14:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| fb0e957d-ee2c-312d-b8b0-5b31de5b67cb | -2.6758 | -46.7806 | 2024-11-09 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 139d1e84-66e7-3292-ab10-988d74e3eb3d | -2.2322 | -46.4182 | 2024-11-09 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0cc5c892-bdf8-3545-9668-5370c1eec956 | -2.2479 | -53.7829 | 2024-11-09 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 198.2 |
| bd256d4c-8009-3c9e-8585-3a9e5bd24746 | -0.2115 | -51.6455 | 2024-11-09 14:00:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 26f923b9-f56a-3a44-b1eb-093cb52bd74a | -5.4546 | -43.2659 | 2024-11-09 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 7a0fd3d6-642c-3bd3-b04f-a9ed25531da7 | -3.2154 | -50.6213 | 2024-11-09 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f75c5556-80f7-3223-981e-653875d4328f | -3.525 | -44.0286 | 2024-11-09 14:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 331.5 |
| c15aea78-f992-367f-95e7-c7fdaae4a0fb | -2.0835 | -46.5324 | 2024-11-09 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 9ef2ba59-8ba5-3572-a601-d7a173852548 | -5.4544 | -43.2893 | 2024-11-09 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ef57e171-ad75-3b2c-8734-d7e9a0cab756 | -3.125 | -50.1419 | 2024-11-09 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| ecceb191-c177-3733-96b6-8cc2b5590ea9 | -4.1246 | -43.5833 | 2024-11-09 14:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e26786b5-abea-3ee3-9837-ee60e4eff577 | -3.2153 | -50.6423 | 2024-11-09 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b5e3b553-12b6-3363-9246-09af61f73ef9 | -3.9625 | -48.9883 | 2024-11-09 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 31f4c89a-a54e-3bb6-b671-aaf3ae53c39e | -2.2642 | -47.9916 | 2024-11-09 14:00:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d3ceab5c-a93b-3412-b8b1-207474d94d6b | -17.6079 | -57.4688 | 2024-11-09 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 12fce0b9-7523-3721-b446-60def9f87359 | -2.2803 | -48.744 | 2024-11-09 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| f2d8bc31-3cf1-3475-b57d-20d78d183dc3 | -3.8194 | -44.6778 | 2024-11-09 14:00:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| c3d3e78d-af7f-3142-ad6b-93b9c65443c1 | -5.7475 | -41.9927 | 2024-11-09 14:00:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 6cb0d12b-4bec-353f-98af-f6bbf5f1caa9 | -2.4104 | -48.5265 | 2024-11-09 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 88d777a2-ad36-35b8-8e2e-cbdce5532c1f | -4.1244 | -43.6064 | 2024-11-09 14:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b27292de-1e12-3b5b-a9a1-f3faad153718 | -2.8921 | -48.2977 | 2024-11-09 14:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4375a6ac-7cb4-3634-acbe-d8cf57f2b43b | -2.4105 | -48.505 | 2024-11-09 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d5b664b6-fef0-3cab-acc7-0d68a8dab9d7 | -3.2538 | -50.2639 | 2024-11-09 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| e65f0d63-9ee7-3136-a2cc-43ecfea4a6a1 | -3.23 | -50.26 | 2024-11-09 14:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec170029-893a-397c-a73e-6b726f06b3b2 | -8.84 | -47.7 | 2024-11-09 14:00:00 | MSG-03 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6c23b94-60c2-3d99-a54c-96a35eedae08 | -2.5781 | -48.1777 | 2024-11-09 14:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| fc2ff458-5b31-3f19-a00a-f42a4004b71f | -6.1836 | -45.4597 | 2024-11-09 14:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 92b91888-1620-32f9-837a-499a8b7a46f0 | -0.2299 | -51.6455 | 2024-11-09 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 89238efc-aef2-35eb-b259-9784a9236fcc | -4.1246 | -43.5833 | 2024-11-09 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 2bdae5eb-6b9b-3d23-8512-666ed7c81947 | -2.2642 | -47.9916 | 2024-11-09 14:10:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0a6daeb2-244b-3f65-a922-c6bc8cc65168 | -0.3034 | -51.7277 | 2024-11-09 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 272b7757-d0b1-326c-89e9-4c5adb35f34e | -5.4359 | -43.2673 | 2024-11-09 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8e4c7f44-d8b0-36e5-8708-2ccf58bf329f | -3.5649 | -43.5654 | 2024-11-09 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 18afbc05-a36a-3ec9-ab7b-cedbabda7b55 | -2.646 | -49.8819 | 2024-11-09 14:10:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1c5d7584-6ccd-353f-acbe-363fd3004fa0 | -5.7475 | -41.9927 | 2024-11-09 14:10:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 147a5296-d706-354a-9cbe-d5c6794cfbd8 | -2.379 | -46.8552 | 2024-11-09 14:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 3a888620-6af5-3ca8-b355-918cc58197ea | -7.1778 | -42.0055 | 2024-11-09 14:10:00 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 4bf95e92-83da-3115-ae24-1da0d7cf38a9 | -3.1969 | -50.6428 | 2024-11-09 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 492c4fb2-6998-3daa-995b-75a327b562e4 | -3.125 | -50.1629 | 2024-11-09 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 428ba813-045c-3a7f-8950-9f2fc772816d | -3.5462 | -43.5663 | 2024-11-09 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 036b78ea-f195-3238-83aa-a9995106bbd5 | -2.0478 | -46.0903 | 2024-11-09 14:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 5f4dd525-8136-3f60-a4ca-ef9b55b441bc | -4.807 | -44.7606 | 2024-11-09 14:10:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| e59794cf-7e56-3dc5-b102-a787db263682 | -5.4734 | -43.2646 | 2024-11-09 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2ae142f1-9c6b-314a-9796-9e1f4fee55ca | -2.3604 | -46.8776 | 2024-11-09 14:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 082f7079-d99d-324f-aefb-451f57d0d284 | -0.5992 | -49.5352 | 2024-11-09 14:10:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7b8038dd-a9db-3703-8c49-e9618da865ee | -0.3769 | -51.8715 | 2024-11-09 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 6eadf30a-64dc-3a57-b8bb-8d3c2ea465ad | -3.6111 | -48.9167 | 2024-11-09 14:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 23abb4c4-93aa-3c84-ba6d-4704c3c4c91c | -3.967 | -48.15 | 2024-11-09 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 083b02d2-68de-34c4-9344-611314abef72 | -3.0319 | -50.3547 | 2024-11-09 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| a6c51db0-334c-39d9-8cfb-09f295104a3c | -5.7146 | -43.5261 | 2024-11-09 14:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c7420607-df43-3e87-b0ea-3bdd9be9c518 | -3.2346 | -50.4533 | 2024-11-09 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 94f07adf-05a1-3dfc-9c06-82b75335761e | -1.5164 | -52.1491 | 2024-11-09 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 9d0fdf05-c258-3465-bef8-2c2c8b2d3a71 | -2.2318 | -46.5508 | 2024-11-09 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 8b6ea256-ada5-33f0-abd4-9d4fe8b2eaeb | -2.3733 | -48.5703 | 2024-11-09 14:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 63c9490f-a00e-3f0d-9be7-bee93ee28cc3 | -3.2538 | -50.2639 | 2024-11-09 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 022139b5-11b7-3778-bed2-b68be7a305b2 | -3.578 | -44.5525 | 2024-11-09 14:10:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c4875c58-f993-37cc-8556-92dcdeead94d | -3.9483 | -48.1724 | 2024-11-09 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2a7f1e77-2532-3fb4-bbb0-1e9a645c6e08 | -1.5347 | -52.1694 | 2024-11-09 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 6356bdbb-db45-3caa-84ee-f85aac9ee065 | -5.4544 | -43.2893 | 2024-11-09 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 57872c7d-818e-3de9-aaf3-c1656fd802f1 | -2.2803 | -48.744 | 2024-11-09 14:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 19086a88-2234-367d-aea0-6e705b5ce8fb | -2.2479 | -53.7829 | 2024-11-09 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| c5553d37-bd81-3eec-afb8-81b933a7877e | -2.3555 | -54.7627 | 2024-11-09 14:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 218696d1-6383-36ac-ad0c-1f797dc081c7 | -7.089 | -41.534 | 2024-11-09 14:10:00 | GOES-16 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| b96a5bd9-af44-3253-9d26-706c5de239e6 | -6.1366 | -42.5544 | 2024-11-09 14:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 8309b56a-f6c5-3bce-8e20-f129098827d0 | -0.2115 | -51.6455 | 2024-11-09 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 78183b4e-4b61-3cb7-8a95-80c4680b70f7 | -2.2804 | -48.7226 | 2024-11-09 14:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| f4b7ea9c-3acf-3e5b-b98b-5476e57553a6 | -2.578 | -48.1992 | 2024-11-09 14:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 53d2fc6d-aefc-3711-8948-3d5ba2db5df5 | -6.1809 | -41.8844 | 2024-11-09 14:10:00 | GOES-16 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 2aa8e2ea-6377-3942-a6ec-afa93b9eff3f | -0.6177 | -49.5351 | 2024-11-09 14:10:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 07fcc0e4-1b36-3299-b1d8-c12f05cc7771 | -1.5163 | -52.2106 | 2024-11-09 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5bbe83bf-bbe0-3407-b9b1-8d4fc4653e10 | -6.9974 | -41.3016 | 2024-11-09 14:10:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 26ec8b25-ac2b-3d70-89be-c6cf9333dca8 | -2.2317 | -46.5728 | 2024-11-09 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c22811a7-ab33-3e76-84e9-9ebf5f58a799 | -3.525 | -44.0286 | 2024-11-09 14:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 314.8 |
| 3bdf398e-2823-3661-950c-0307acda1cec | -4.2032 | -45.8762 | 2024-11-09 14:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 0935f7c4-659a-34dc-bf9b-cee61e47827c | -3.125 | -50.1419 | 2024-11-09 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 86fe9a95-b3f0-3329-8fc2-b42fe75ef3a4 | -6.1363 | -42.578 | 2024-11-09 14:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |


[Clique aqui para ver as próximas entradas](README123.md)
