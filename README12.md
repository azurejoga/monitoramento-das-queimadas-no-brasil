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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d93b06d-3023-37ac-bfc1-4076fae956f6 | -17.90633 | -54.13754 | 2026-01-06 04:55:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f497f713-d774-3783-8e4b-7fc8367691f2 | -20.53388 | -58.00795 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 57df8f53-37da-35cf-80b4-5ae041f52aef | -17.65421 | -56.45425 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d39c43c6-d425-3046-98d5-0bbe9e0c37ed | -14.92632 | -59.90252 | 2026-01-06 04:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 302f149e-1992-3730-953b-ce08d80e5837 | -16.06468 | -60.07008 | 2026-01-06 04:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 572645b5-ddd2-31a1-8f14-5843a2fd9058 | -10.68078 | -40.40077 | 2026-01-06 04:55:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5380b73a-921d-36b0-984b-78fefb6428e9 | -15.38828 | -59.1912 | 2026-01-06 04:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3e21ea4-ba16-3b78-87ae-a409a624448a | -16.04084 | -59.21752 | 2026-01-06 04:55:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e579c05-e656-369f-8e3a-c36233ebd6b5 | -16.04376 | -59.22312 | 2026-01-06 04:55:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dbd016a-8cc0-316f-88e1-e91388bb734c | -20.9879 | -54.47767 | 2026-01-06 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de99f097-b23e-3047-8963-ef60cd8bf09d | -20.51538 | -57.99228 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 18f1176a-ee30-33d4-b7e5-428a7972f0be | -22.49798 | -46.94036 | 2026-01-06 04:55:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79aff4bf-299f-3c4d-9fe1-8bceed82bb83 | -20.53585 | -57.99619 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5add9faa-1c58-3180-9f11-df7895cf5242 | -20.52298 | -58.0099 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 334b2b0c-3dc7-3fe4-9dfa-9daa968f749d | -17.65481 | -56.45056 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| eaa358a8-fa69-3b94-be26-2569f80ff1ec | -20.99131 | -54.47823 | 2026-01-06 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93fe2c0c-9d10-3c1f-a93c-784a6b89d4a3 | -20.53453 | -58.00403 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5ebdfd6a-df17-3d4e-92ed-cc1f68a310c4 | -20.51957 | -58.00926 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7a3f0beb-badf-300e-8c83-444a64ebd467 | -20.51208 | -58.01187 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 95716ee5-59a6-3cad-9437-a44b96633512 | -20.49918 | -55.19564 | 2026-01-06 04:55:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8edddbd0-c96c-3392-a2b1-f883b4467b4b | -20.81445 | -54.54158 | 2026-01-06 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b406ee3d-0674-39e6-ba51-9acc6fd669c7 | -20.52639 | -58.01057 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6d5dbae0-86ea-320f-a211-da58081765c6 | -22.49266 | -46.9398 | 2026-01-06 04:55:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46cac82a-0d28-32cc-b380-ecce57f6aad9 | -20.73684 | -55.69992 | 2026-01-06 04:55:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de954b1b-c09b-3faa-992a-098e48b97a76 | -20.53026 | -55.54354 | 2026-01-06 04:55:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c73f1ecf-e527-3469-92c1-ffa81a2bd596 | -15.68806 | -59.65974 | 2026-01-06 04:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cb8490a-02c0-3ddb-bc05-534674008b76 | -16.59609 | -58.21656 | 2026-01-06 04:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9d356e0e-a577-331b-9d70-f908737b5556 | -15.68415 | -59.65897 | 2026-01-06 04:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 095e21fe-ca18-352a-9139-727b7543395b | -20.53047 | -58.0073 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1265a96b-c68a-37ce-86e0-b765608acc4f | -20.53795 | -58.00468 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9343a903-8f83-3acb-a341-3aa262ade352 | -16.59966 | -58.21723 | 2026-01-06 04:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ed9cf509-4a90-3822-a950-72d0625b1cb7 | -19.36028 | -54.67865 | 2026-01-06 04:55:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89461313-0b4b-33eb-8901-a62b59288411 | -10.68013 | -40.40619 | 2026-01-06 04:55:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1a9bc063-b517-3f2a-825d-df65c61e4fcf | -17.65086 | -56.45365 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 5b6756e5-ebaa-3cc4-a777-35a86093991a | -20.51891 | -58.01318 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 27446e2f-f08b-3adc-8d14-bccba2e148f2 | -18.54843 | -55.4366 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cef567a7-fa10-39fc-a075-8e5f042b1254 | -18.54568 | -55.4324 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a0d0ae3e-ad9f-33e3-84c3-9c09a9e103a6 | -20.52286 | -57.98966 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ea0a70f1-bd8a-394c-8b57-22e2abb72eb0 | -22.86479 | -52.28292 | 2026-01-06 04:57:00 | NOAA-20 | SÃO JOÃO DO CAIUÁ | PARANÁ | Brasil | 4124905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99772f02-463e-3613-a0f7-de56583659df | -22.03031 | -56.30558 | 2026-01-06 04:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13618968-1a98-34c8-8b33-23ed92b1b3d0 | -22.03663 | -55.51546 | 2026-01-06 04:57:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78f30fbc-8df1-3017-9927-ffd5cd0e1c78 | -23.69536 | -55.27143 | 2026-01-06 04:57:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 36f5a108-6ea2-3179-907a-e22d497725b3 | -27.51055 | -53.68819 | 2026-01-06 04:57:00 | NOAA-20 | MIRAGUAÍ | RIO GRANDE DO SUL | Brasil | 4312302 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5ed343ee-de0d-3c6c-a390-cf5ca1ff26cb | -27.51117 | -53.68326 | 2026-01-06 04:57:00 | NOAA-20 | MIRAGUAÍ | RIO GRANDE DO SUL | Brasil | 4312302 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 738fb23c-8f87-34b9-9c04-70f0af63e679 | -21.53644 | -57.53535 | 2026-01-06 04:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07892c1a-09d7-3078-b6cd-82246b4d5352 | -26.19881 | -53.1495 | 2026-01-06 04:57:00 | NOAA-20 | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7605e6c7-76a4-31f8-a3cc-b1c22e347c14 | -22.91406 | -47.07852 | 2026-01-06 04:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bf6216b8-f05b-3be4-a9bc-e73f94fe7a41 | -22.02757 | -56.30126 | 2026-01-06 04:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09991edc-36c4-355a-ae2c-6d3ba16ac6ed | -22.91372 | -47.08197 | 2026-01-06 04:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7911d95c-5a94-33f0-8b37-0a73a0f854ad | -21.53979 | -57.53597 | 2026-01-06 04:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 784aab83-20e7-3a68-837f-050942b7e6f0 | -23.69875 | -55.272 | 2026-01-06 04:57:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 458f421d-003b-36ff-8821-77e58939f7e9 | -22.02699 | -56.30498 | 2026-01-06 04:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a5bf95-0c6d-30d1-83ac-b98cee196015 | -21.54041 | -57.53222 | 2026-01-06 04:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 61b17a0c-b072-3dfa-870e-64350a0076f5 | -22.03605 | -55.51925 | 2026-01-06 04:57:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a851dd9-2960-3ce7-b512-80ef6e05a7cb | -31.75333 | -52.98751 | 2026-01-06 04:59:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| c937eccb-6767-321d-929e-093c7b180c66 | -29.78297 | -55.81462 | 2026-01-06 04:59:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 97256108-a7ae-3048-9141-7794196f326e | -3.6962 | -43.4432 | 2026-01-06 05:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7d89176d-62f4-3635-9801-220b80ebac79 | -3.6962 | -43.4432 | 2026-01-06 05:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 97eeb60a-156b-354d-b556-a237d63f5b7e | -3.6962 | -43.4432 | 2026-01-06 05:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2a4e13b0-b879-3737-8024-70bc926a2891 | 4.27508 | -60.68849 | 2026-01-06 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5467381f-3ade-30e9-88e7-173ddb311f83 | 4.51474 | -60.62565 | 2026-01-06 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ab58387-00ce-3057-a893-ba3b0c65ee44 | 2.54552 | -60.3559 | 2026-01-06 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ff95c1-7b95-386e-90e1-bfc05eb3ac82 | 2.54194 | -60.35649 | 2026-01-06 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae61c070-2e7e-3fe4-b99f-1164665bb8b1 | 4.52108 | -60.62086 | 2026-01-06 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72091642-7f84-3bfe-884d-ab1a23d8ec11 | 3.42704 | -61.18442 | 2026-01-06 05:40:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89c189f9-60d9-3fba-9982-05ffec1554ea | 4.52049 | -60.61718 | 2026-01-06 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13fcca1d-cb68-366d-98c1-ea93f8b91096 | -0.09133 | -51.27725 | 2026-01-06 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bc03a9b-5db5-3a0c-9cd9-914fc8304709 | 2.79015 | -60.30391 | 2026-01-06 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d77e03d-7fc5-3631-8448-349ebbf90848 | 4.5182 | -60.6251 | 2026-01-06 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ed6d3ac-2a65-3520-9382-8cecdb42fda7 | 2.54255 | -60.56824 | 2026-01-06 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33542974-6197-3898-a4f0-e0c20e1155ed | 2.53623 | -61.32534 | 2026-01-06 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7c5a5c0-cf7a-30ba-a839-f52f6dc4d0ee | 3.16304 | -60.95896 | 2026-01-06 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9488fd98-5884-3292-8dde-e36e8f00c76e | 2.69124 | -60.2048 | 2026-01-06 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d107a440-5858-30cd-bf91-8bdb4f25acaf | 2.54673 | -60.57167 | 2026-01-06 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f236ea28-2aa8-34d3-8d5f-9e48ab7c7a58 | 3.61929 | -60.79844 | 2026-01-06 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4875d074-bc08-3d85-8758-203f65240508 | 4.52167 | -60.62456 | 2026-01-06 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 219069f4-279e-3f02-923f-8f7d1316dbae | 4.50778 | -60.62656 | 2026-01-06 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 713d764b-8bfc-3a19-bd45-fd9749e601d4 | 3.61809 | -60.79964 | 2026-01-06 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6ff59bc-6351-33d6-9af3-f7ac1e693dc8 | 4.22643 | -60.86616 | 2026-01-06 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e5a2d40-ae90-350c-8eea-a886f679dde1 | 3.61869 | -60.79461 | 2026-01-06 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88278c82-ca26-3ed6-9cc7-e2bd73689681 | -0.0877 | -51.27821 | 2026-01-06 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30acf70a-9ebd-35f2-8fef-fe5fc6a57a2a | 4.27159 | -60.68892 | 2026-01-06 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b23095a0-0d66-3f4a-a91d-12f32859830e | 3.47582 | -60.25609 | 2026-01-06 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 719a3029-1bd8-3f65-bf80-a3332ab2d6a5 | 2.54616 | -60.36003 | 2026-01-06 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdbfeac8-350b-302e-b939-35a64fec409d | -0.09039 | -51.28326 | 2026-01-06 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac2313ea-0ca1-3a76-8a64-658928701dd6 | 4.50489 | -60.63066 | 2026-01-06 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6572ce0e-911a-3f1e-a06c-8f3dfc5c606e | 2.83833 | -61.32505 | 2026-01-06 05:40:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8964c61a-ffc8-369c-8263-3905803e04a2 | 4.14998 | -60.47731 | 2026-01-06 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d65fed25-497e-3763-a4a5-e7492d26c895 | 2.54319 | -60.57224 | 2026-01-06 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d830657d-6b60-3e46-805b-bec648379086 | 4.51127 | -60.62614 | 2026-01-06 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ddf62d4-e76a-3391-96d5-fb0f21a4f7ac | 3.61748 | -60.79582 | 2026-01-06 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5bf403f-bbf3-32d9-b08f-343516a85e99 | -3.33353 | -52.70191 | 2026-01-06 05:42:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7077045-07f9-323b-b0a2-a09496778142 | -2.09513 | -53.51772 | 2026-01-06 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c48630f-8451-30c8-bc5f-5995e9ec7633 | -3.33297 | -52.69933 | 2026-01-06 05:42:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c851081b-2a34-394a-9514-56689fd00d66 | -1.59706 | -53.98858 | 2026-01-06 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2906fbf-0e16-3f26-8aeb-2acd8a929515 | -2.88096 | -52.56623 | 2026-01-06 05:42:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 816d077b-da44-3f9b-8d16-607373dc88de | -2.27459 | -53.78975 | 2026-01-06 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac77d6e9-0849-368e-9778-8a22be83a17e | -2.86012 | -52.79831 | 2026-01-06 05:42:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a074abcc-6f95-3a5f-91be-a58f8227ca28 | -1.81951 | -54.16785 | 2026-01-06 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 44df85a7-8c81-31b9-a4c6-c5d83da51a14 | -3.33425 | -52.69675 | 2026-01-06 05:42:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README13.md)
