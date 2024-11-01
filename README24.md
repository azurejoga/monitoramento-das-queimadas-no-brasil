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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 443e75d2-62df-315d-a97e-0e42b164750c | -16.90875 | -57.5219 | 2024-11-01 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 8d01f136-1702-3c7f-a73e-1a1e95e7a4a6 | -16.90792 | -57.52724 | 2024-11-01 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 7f07419f-5252-3a0a-ad8f-159ca9b4f8af | -16.90732 | -57.5283 | 2024-11-01 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 5358f8a8-9982-35c0-b869-c7acd7b72f73 | -22.06692 | -47.10867 | 2024-11-01 04:10:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46f4c22a-14b2-31d8-b081-945d5342ea60 | -20.66398 | -42.20161 | 2024-11-01 04:10:00 | NPP-375D | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8583a7af-f7ac-3993-94aa-b0f1ac49c103 | -20.26735 | -42.25993 | 2024-11-01 04:10:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2bebab1b-a999-3088-89a0-e10ab4959105 | -21.62585 | -43.46666 | 2024-11-01 04:10:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e8c163c0-b91d-3915-a043-b3b57c776879 | -22.90013 | -43.75085 | 2024-11-01 04:10:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0e98d166-0282-3bb6-8e88-6e4beeb93364 | -22.85611 | -42.9789 | 2024-11-01 04:10:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e4c3d2a-ff83-3829-a739-5ca4fddcc604 | -22.67551 | -43.47809 | 2024-11-01 04:10:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c99878b7-c732-3a12-8317-d1ee311cf087 | -21.17924 | -43.97991 | 2024-11-01 04:10:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 15a1c2f0-1213-3b61-ac3e-27e335b1d10a | -22.9213 | -45.41382 | 2024-11-01 04:10:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4fc9be72-61cf-31b3-ab7a-272cb6b1d54f | -21.20361 | -45.69411 | 2024-11-01 04:10:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 694fcb27-63b1-3c51-ac64-b26f89cbf8c6 | -22.30052 | -46.53048 | 2024-11-01 04:10:00 | NPP-375D | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0d9a905-dcf4-3977-9e47-18585f7c6dfe | -17.57101 | -46.8117 | 2024-11-01 04:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94336305-3273-3ba7-8e6a-92c1f880ae9f | -18.5371 | -46.93761 | 2024-11-01 04:10:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e03f11d-1074-3483-816a-6d7d5b245afb | -20.71165 | -47.29123 | 2024-11-01 04:10:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 290e42d4-9bc1-3c3e-878c-8161dbf10369 | -20.42316 | -47.59504 | 2024-11-01 04:10:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 217685dc-24d3-3cb8-a85d-fb9f4175b43c | -20.41963 | -47.5943 | 2024-11-01 04:10:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2a7c29f-32f3-3440-9182-65e930cab4d4 | -20.40114 | -47.43476 | 2024-11-01 04:10:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4591d2d0-118e-3e6d-a92c-5d20e33f3483 | -22.04066 | -47.93381 | 2024-11-01 04:10:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec26f8fd-5c3a-35d4-bf02-ddc616f4ab70 | -22.5082 | -47.70193 | 2024-11-01 04:10:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b6ade9a5-f6de-33b9-a41a-163bc3e42db7 | -19.44243 | -48.62795 | 2024-11-01 04:10:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce09c840-5272-32f0-a6c0-1d05415762aa | -15.27639 | -51.43515 | 2024-11-01 04:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 405523b0-89c9-3a89-8622-75ed7e3e38a2 | -15.27533 | -51.44058 | 2024-11-01 04:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cea4b76-998a-3a96-adf3-ceafdd214ebb | -15.27157 | -51.43415 | 2024-11-01 04:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 302da80e-e817-3355-8fbe-170acc7bb6b2 | -16.5736 | -52.40768 | 2024-11-01 04:10:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d514bc30-03e3-344f-acbb-ca03d2514a1f | -17.60221 | -53.74292 | 2024-11-01 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3db9ebdb-0716-3447-8794-51e8b4486b47 | -17.60007 | -53.7426 | 2024-11-01 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4306e460-e3cc-398a-8ea9-d8fcbae8d280 | -17.59692 | -53.74147 | 2024-11-01 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9c0d60b-19fc-3330-b74a-8272f75aa3fd | -17.59621 | -53.74482 | 2024-11-01 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 870a7930-a6f7-3672-b946-0ee139dc1204 | -17.59548 | -53.74821 | 2024-11-01 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7837fb24-006b-3b3c-9cad-d3602d27a9b8 | -17.59477 | -53.74118 | 2024-11-01 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cd27ee4-7c34-3819-b68c-d7e9e28ecd0a | -17.59408 | -53.74455 | 2024-11-01 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b87f6dd-05d5-33b7-a1a7-556291ef592f | -17.59337 | -53.74799 | 2024-11-01 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34190045-974f-38b1-91bd-c22ad1954333 | -16.55446 | -56.23579 | 2024-11-01 04:10:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 18fbeaac-1279-384d-a7f4-1ea33247d96f | -16.55327 | -56.24112 | 2024-11-01 04:10:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 32f491fe-c8ec-31e2-874f-da1b1afd474a | -16.55229 | -56.2406 | 2024-11-01 04:10:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f84d8123-1ab3-3a61-b1bc-515bcdfa8bd1 | -16.90266 | -57.51917 | 2024-11-01 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| eee939ba-020f-3d4a-b040-a19bfe59da6d | -16.90202 | -57.52016 | 2024-11-01 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 69bd1c7e-e282-3767-b48d-d4eb6bdd8946 | -22.05777 | -52.79123 | 2024-11-01 04:12:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c94af9d7-44c8-36e5-9605-638a513c6395 | -22.05423 | -52.785 | 2024-11-01 04:12:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f6eacc9-754e-3677-8d8c-4ac088f05f4e | -22.05317 | -52.79007 | 2024-11-01 04:12:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7518c3e-96c1-3a86-84a4-4db1dda111ea | -23.63218 | -46.42586 | 2024-11-01 04:12:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 26ff1909-d87f-3f51-929d-73558d84a8bd | -23.5926 | -47.44001 | 2024-11-01 04:12:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 945cd908-61c4-3469-b7a7-227c84cc1b92 | -23.35844 | -47.93192 | 2024-11-01 04:12:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0e802ce5-37d1-3c41-b68b-4c4521b94167 | -28.58904 | -49.44138 | 2024-11-01 04:12:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bbe05eb7-9f19-31c1-ba29-b4d97186332f | -23.00167 | -49.79406 | 2024-11-01 04:12:00 | NPP-375D | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 109c0a58-c348-38ca-86c5-ff7a4f4c3022 | -23.00072 | -49.79916 | 2024-11-01 04:12:00 | NPP-375D | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2620bde8-a4c3-3c4d-8db4-63749c82ee26 | -22.99785 | -49.79329 | 2024-11-01 04:12:00 | NPP-375D | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 85bb3298-db39-3aba-971e-09e9d58559de | -22.9969 | -49.79839 | 2024-11-01 04:12:00 | NPP-375D | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 233459f8-0638-3e51-b8ab-f430e52ed6e7 | -22.99595 | -49.80348 | 2024-11-01 04:12:00 | NPP-375D | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a2ef16c7-7bc9-33be-b879-6f4e40bf3e6a | -23.83111 | -50.41949 | 2024-11-01 04:12:00 | NPP-375D | FIGUEIRA | PARANÁ | Brasil | 4107751 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d7c94940-fb2c-36c8-a0dd-14ae8a70b368 | -22.05251 | -52.78337 | 2024-11-01 04:12:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6267fa1-9178-3717-b885-2d9dc3a0ea37 | -22.05149 | -52.78844 | 2024-11-01 04:12:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 757c6c52-d22e-3b25-94a0-82a3aeb04be6 | -29.81359 | -51.17415 | 2024-11-01 04:14:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| e206d9b9-11bf-33e4-8603-faeb818372f0 | -3.0353 | -49.4901 | 2024-11-01 04:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 563a2684-ace0-3537-bbe3-a3844f3acaa0 | -3.0354 | -49.4688 | 2024-11-01 04:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| cb41056e-9263-3965-b66f-b13d597af8c2 | -3.0538 | -49.4895 | 2024-11-01 04:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 9adc9f74-a713-36f7-9341-e99716317734 | -3.0539 | -49.4683 | 2024-11-01 04:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 2fb75b54-5c28-31ae-ae51-ae36fbd56c39 | -3.1099 | -45.1165 | 2024-11-01 04:15:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1668b254-83c5-3e06-893f-419239ed26e3 | -3.5631 | -47.3847 | 2024-11-01 04:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 70790719-b899-3670-a293-38ccee7e4830 | -4.3867 | -43.4757 | 2024-11-01 04:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| f1d3bf31-6ad4-31f0-883f-ebce2c31fe94 | -4.3869 | -43.4525 | 2024-11-01 04:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ef3a7b55-ad20-3cae-8abc-f00ef89c6441 | -4.4054 | -43.4746 | 2024-11-01 04:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9ece0801-b09c-3012-b940-c11ce218901c | -9.9001 | -64.8065 | 2024-11-01 04:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| c5848803-8885-3af4-9fe5-6fd3a3000ffd | -9.9186 | -64.8246 | 2024-11-01 04:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 3f6f8809-b169-37a2-8d44-48981bdc76fc | -9.9187 | -64.8058 | 2024-11-01 04:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 2cd40141-c13f-344c-9923-60085a342c93 | -16.9204 | -57.5291 | 2024-11-01 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 4ccda772-3573-34aa-92c5-9b3b4d3153dd | -19.4855 | -56.7487 | 2024-11-01 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| e6227aa7-ca9b-378b-a2b1-f1846e1f0d79 | -19.4859 | -56.7277 | 2024-11-01 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 970296e2-609d-314b-913a-f5f45a296384 | -19.5059 | -56.7249 | 2024-11-01 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| bd3db535-787f-33cf-8192-5b2c2957f2ff | -19.5063 | -56.7039 | 2024-11-01 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 0ab1802e-18d7-365d-8001-d5604cf2f765 | -19.526 | -56.7221 | 2024-11-01 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 71e30118-84e3-3ab2-a15b-a5c88a7c95fa | -3.0353 | -49.4901 | 2024-11-01 04:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a4f24dbf-0896-34e8-87e2-27bf21389b15 | -3.0354 | -49.4688 | 2024-11-01 04:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4038014c-ba20-30c0-a0fd-bf32d80b664b | -3.0538 | -49.4895 | 2024-11-01 04:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 8c9b3f25-cfa6-36ce-b14d-a755accd3f14 | -3.0539 | -49.4683 | 2024-11-01 04:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| e0879e26-e4cf-31c6-bd80-6852c53c563b | -3.5631 | -47.3847 | 2024-11-01 04:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a565175a-5861-3ff9-bd3f-f04b0abe52a8 | -4.3867 | -43.4757 | 2024-11-01 04:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ee798032-9e44-34d2-81bb-d98d2412259f | -4.3869 | -43.4525 | 2024-11-01 04:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2017baf0-f521-378b-9135-e582c740c988 | -4.4054 | -43.4746 | 2024-11-01 04:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8f152540-1548-333c-b8fc-cbbc61ee0372 | -6.1229 | -43.9578 | 2024-11-01 04:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 74f9fe6a-b92e-3c0b-b065-48ed7bcd1bcf | -9.9001 | -64.8065 | 2024-11-01 04:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5e4a2a48-9e67-33d6-94cc-0f393291a303 | -9.9186 | -64.8246 | 2024-11-01 04:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d7eb4dc2-a200-3df5-986d-a7ac153dee6a | -9.9187 | -64.8058 | 2024-11-01 04:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 24a5df08-5c40-3c20-abde-0cfc733b9863 | -9.9188 | -64.787 | 2024-11-01 04:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c337fa3d-6b5b-3d3c-a8c4-77d5bd4bff8e | -9.9373 | -64.8051 | 2024-11-01 04:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 70e2d1a4-748f-38ef-9542-23d76d5fa835 | 1.79713 | -50.44692 | 2024-11-01 04:27:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32cbc81a-0763-324c-a5ec-45fa91afcace | 1.7925 | -50.44267 | 2024-11-01 04:27:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fa9c5a9-704f-34e1-88ca-30892440481f | 1.42831 | -51.015 | 2024-11-01 04:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42959515-55cd-3f80-8677-a90757495c0f | 1.32243 | -50.87576 | 2024-11-01 04:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f828ed0-4877-38f5-bfc4-1ff88ef495fc | 3.42656 | -51.2543 | 2024-11-01 04:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58dcba1c-d6a5-3b3d-b3ff-14be8ce1309d | 3.42598 | -51.25048 | 2024-11-01 04:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39e9542c-e73e-3585-9928-86cb91d2933f | 3.42414 | -51.26641 | 2024-11-01 04:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 276835a2-a28a-3f91-99e5-8d18790f91e3 | 3.42355 | -51.26258 | 2024-11-01 04:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4108d77b-5508-3064-8aab-4cc827d9d7c0 | 3.42297 | -51.25876 | 2024-11-01 04:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 423e62e7-d6b2-3f63-8bf2-df74f3a3fe97 | 3.35109 | -51.38382 | 2024-11-01 04:27:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a2ca15b-0d4d-3a73-a236-e43c180c9091 | 0.9519 | -52.09592 | 2024-11-01 04:27:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d0855f3-8ad1-3c1f-ae81-b7c533cb9495 | -3.2493 | -53.3423 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README25.md)
