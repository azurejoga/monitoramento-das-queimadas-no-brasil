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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5e8a536-643a-30f6-9a18-b9842fd17654 | -10.9324 | -57.1312 | 2025-06-22 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| db53fbd1-c7fc-39c0-a00f-6d797b6fdcb3 | -8.5907 | -51.5955 | 2025-06-22 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 120b76a1-aaf1-3045-8f6a-831b5bcc0907 | -8.0342 | -47.642 | 2025-06-22 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f4c79708-2535-3b42-bd76-014895dd2dc8 | -10.9326 | -57.1113 | 2025-06-22 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4afe7ee3-a651-35aa-bc52-41eaa16ce8af | -8.0703 | -43.0981 | 2025-06-22 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| a0bd9004-2e73-33ef-92d4-dea0c9b4311f | -8.6094 | -51.594 | 2025-06-22 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 38505d2a-14ff-34f5-991d-0f84b84bd50b | -11.0006 | -45.0847 | 2025-06-22 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| b1ff5e3a-5be6-3bdd-bf09-cb9e5fa49889 | -10.9815 | -45.0874 | 2025-06-22 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 8d46448f-4ab4-3796-befe-e86749c36af5 | -8.6097 | -51.5731 | 2025-06-22 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 91f8b80a-c11c-35c7-ab6b-6bcebe217ea9 | -9.4622 | -56.0614 | 2025-06-22 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 2e2fe8f8-6799-354f-a4b5-539b443e6213 | -11.617 | -58.289 | 2025-06-22 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c76a7f9e-b673-320b-b175-1ff226059853 | -16.2958 | -49.9575 | 2025-06-22 00:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 08c9cbaf-197d-3706-af87-0bb1aeebcb04 | -10.9324 | -57.1312 | 2025-06-22 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 89bd2382-495e-35bc-913b-534888bceb65 | -16.3154 | -49.9543 | 2025-06-22 00:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 15e2d8c3-24f9-31ee-9cbc-fd0e391fcbe2 | -8.0703 | -43.0981 | 2025-06-22 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| a513d862-7af9-354a-a20b-a6ad561e6a8c | -16.2962 | -49.9354 | 2025-06-22 00:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 03f454a2-3c53-3527-bf34-255f2e937092 | -10.9326 | -57.1113 | 2025-06-22 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 621c878c-d4a8-368c-8ea5-5b10d203d696 | -11.617 | -58.289 | 2025-06-22 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9fbeb99b-2675-36e0-9e26-74b0b1d5dc86 | -8.0342 | -47.642 | 2025-06-22 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| afa596a9-d408-3e89-bcf1-070977045331 | -11.0006 | -45.0847 | 2025-06-22 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 3dca9a70-8482-3334-a102-ed7a1536a04b | -9.4622 | -56.0614 | 2025-06-22 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ed8943a9-7434-361a-bb8f-68b148e28309 | -10.9815 | -45.0874 | 2025-06-22 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 3bafb1a7-b523-302b-ab05-407d3638d811 | -10.9324 | -57.1312 | 2025-06-22 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 17398e69-bc8b-33f6-b8fb-bbd2f452e64d | -9.4622 | -56.0614 | 2025-06-22 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f18b91b8-3e74-393c-8def-478a70705719 | -10.9815 | -45.0874 | 2025-06-22 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 70a826ad-1db7-305d-88b4-e325b495f626 | -8.6094 | -51.594 | 2025-06-22 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 530d9121-8596-38df-966e-d34e300c676f | -11.617 | -58.289 | 2025-06-22 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 833df414-8b2a-32d0-8fcb-8fea01ddcc0c | -11.0006 | -45.0847 | 2025-06-22 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| ad0d2dae-aa8a-3831-99ae-53edb95b8056 | -10.9326 | -57.1113 | 2025-06-22 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 0a91232a-51a3-3233-90b0-6b539a95b019 | -8.6097 | -51.5731 | 2025-06-22 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e6ce0129-70c6-3b33-885f-de6aa9da24e9 | -20.42289 | -42.2315 | 2025-06-22 00:20:00 | TERRA_M-M | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| c9ada0d9-2e9e-38a7-814c-e2c2120ef3da | -12.41795 | -43.81169 | 2025-06-22 00:20:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d8e9b173-632c-3193-afce-9e48f5b46e9e | -13.04013 | -48.84217 | 2025-06-22 00:20:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 84a05f92-aae9-30a6-bd7c-a4d0d1946bc1 | -20.48922 | -42.38174 | 2025-06-22 00:20:00 | TERRA_M-M | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ec0f3e01-3fa4-34d5-95c2-5f401d681881 | -20.85363 | -43.06566 | 2025-06-22 00:20:00 | TERRA_M-M | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 00f6bb9a-62b4-3aab-b98f-981109529265 | -20.4216 | -42.22191 | 2025-06-22 00:20:00 | TERRA_M-M | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 7132c99c-5fc2-3fff-83f9-e721abd687a8 | -15.40155 | -46.68571 | 2025-06-22 00:20:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fb1ac3c3-b163-3839-884f-304842619ff8 | -12.41919 | -43.82077 | 2025-06-22 00:20:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2ce935b5-7cce-362e-9ccb-fa5d71b42d5b | -13.26969 | -46.83672 | 2025-06-22 00:20:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d4ca361d-a83c-39ad-b55f-49d90fa5d861 | -17.04983 | -43.77068 | 2025-06-22 00:20:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b9a073d2-7f75-33dd-b2ff-e29e8554d05f | -14.26224 | -45.49901 | 2025-06-22 00:20:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ed89a5ae-7146-3a02-86cb-5dc79a2b2cef | -16.301 | -49.97667 | 2025-06-22 00:20:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| cb72b89d-1680-32db-b0fd-921be4ddbf2d | -16.29835 | -49.95155 | 2025-06-22 00:20:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 334.9 |
| b5a24d5c-298f-379e-8408-7b2e6dc8538e | -8.59007 | -51.578 | 2025-06-22 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 564c1a47-6113-39af-9ef0-b606177fde81 | -11.583 | -44.65067 | 2025-06-22 00:22:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6ae27b2a-533f-394b-9186-be53618cdb80 | -7.98336 | -46.21495 | 2025-06-22 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cf58ada8-1e51-3d1b-932d-7bbee440ecd6 | -9.15109 | -47.15902 | 2025-06-22 00:22:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| de58e59b-ec2a-390e-823e-93d7d3e2f45e | -8.32433 | -46.22641 | 2025-06-22 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70a5736d-467c-34e0-a8bb-7589cba2922c | -8.09595 | -43.14664 | 2025-06-22 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 916494d2-66bc-3275-9f71-b15d1f2f0f9e | -10.652 | -44.50222 | 2025-06-22 00:22:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 32a444c6-8e0b-3314-85cb-587241679231 | -10.51724 | -53.62469 | 2025-06-22 00:22:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 149e6294-3c17-3c51-b69c-ae38b91a1015 | -8.11376 | -43.14405 | 2025-06-22 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 3132b8da-468a-3330-8c1b-953d1faead80 | -9.3401 | -40.21473 | 2025-06-22 00:22:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| cb7a5863-a4a7-3066-a3f8-0a4ad62083aa | -8.60325 | -51.60608 | 2025-06-22 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| dc3fab27-b8a4-393b-b693-0c4ae8c637a3 | -10.98015 | -45.09392 | 2025-06-22 00:22:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2f1b615a-9036-399c-9cc3-a40d2f538c25 | -9.15058 | -47.153 | 2025-06-22 00:22:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 98728e49-be6d-31ad-9d2a-518893b32d34 | -10.0694 | -49.65797 | 2025-06-22 00:22:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 2e6066a9-e0ed-3f18-b6c0-40dede71268f | -8.07942 | -43.15827 | 2025-06-22 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| defa213c-f722-3b25-89a7-ae405fd26a1d | -8.02123 | -47.6566 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 92d3f991-f73b-311c-81a4-9041471ba174 | -10.51034 | -47.58677 | 2025-06-22 00:22:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 65cd606d-5b43-32e1-9ccf-901e6092131b | -7.98201 | -46.20494 | 2025-06-22 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e62a0261-8a6a-36d3-8ffa-69682e4a7f24 | -8.04015 | -47.64161 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 81823569-d0a3-37c5-86ba-a324f6ea67ee | -7.26918 | -45.35973 | 2025-06-22 00:22:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60d2e0ee-c85f-379b-916d-515236ec8d1b | -5.57204 | -45.21677 | 2025-06-22 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8a59052e-709c-3a03-8f16-031cb1281b0b | -5.3683 | -47.29177 | 2025-06-22 00:22:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2376e9e1-dd1b-37cf-83f6-2a407feaa4cd | -8.59293 | -51.60265 | 2025-06-22 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| c516b135-a131-3d43-926d-239f186ab58f | -8.07301 | -43.113 | 2025-06-22 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 9f2a1e2b-b448-3954-96c1-c1e5e849c4fb | -8.02279 | -47.66885 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d7aff25b-d217-31a4-ad7d-0a7c91611c58 | -8.02991 | -47.64301 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| c47af2ad-0425-3471-81f3-4e797527128e | -10.82304 | -46.35424 | 2025-06-22 00:22:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 53de4c46-8f66-30f1-aa9e-5932d4f8eb2c | -5.32595 | -45.22717 | 2025-06-22 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5dcce4b6-434e-3eea-abb7-ee51a1490890 | -8.07814 | -43.14922 | 2025-06-22 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| bfdd4507-25eb-3488-bef0-5995040fca3a | -6.50517 | -43.63353 | 2025-06-22 00:22:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6b694c86-503b-31b1-836e-272f920b1ac2 | -8.02234 | -47.65046 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| b8b44b18-8030-338f-b4c9-519f70fb8d54 | -5.36976 | -47.30252 | 2025-06-22 00:22:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| bea2d62c-a712-34dd-8152-adcee776e19e | -11.5724 | -52.1007 | 2025-06-22 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6685c6fa-c06f-3903-b0b5-5fb783ff333e | -10.98928 | -45.09262 | 2025-06-22 00:22:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 112b9ebb-263b-388d-8592-9433ecec3fa9 | -5.03998 | -47.65805 | 2025-06-22 00:22:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c6d648fc-9fe8-3d33-ad26-e4ae16cbbe9d | -5.07041 | -43.72575 | 2025-06-22 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e5cc57ba-7a74-33ac-8775-89e12fef9313 | -10.057 | -49.65953 | 2025-06-22 00:22:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 874790d2-4a84-38f1-98c7-3fb2f55d2c3f | -11.56859 | -52.09579 | 2025-06-22 00:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| d5894cf2-0192-383f-b657-2b203463d116 | -11.58425 | -44.66008 | 2025-06-22 00:22:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 620f316c-7fed-3e6f-9d04-c0e4eb9244b3 | -10.96783 | -40.88343 | 2025-06-22 00:22:00 | TERRA_M-M | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 2d09f799-6cd1-3def-9b24-033c19949edc | -8.02398 | -47.66268 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| f096b5c9-b273-3162-a5f1-11259ddb085c | -7.15447 | -44.06557 | 2025-06-22 00:22:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 39ab7e0c-d51a-36cd-b041-0d91fa064906 | -5.32717 | -45.23606 | 2025-06-22 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19ee909f-20f5-359d-8d58-d5cddc974e9e | -8.07172 | -43.10393 | 2025-06-22 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 21bb89a9-d8b6-3c98-811b-6d65c3523469 | -9.32991 | -40.21629 | 2025-06-22 00:22:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 54443c20-2ba6-3b34-83a7-2f2485814788 | -8.00349 | -47.6655 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a526072c-8242-3d1f-8da9-78a0fdb30e4c | -8.42254 | -48.30731 | 2025-06-22 00:22:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| bebabe75-c0a1-3904-8453-923b9d5b47e3 | -5.07167 | -43.73478 | 2025-06-22 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f46de056-46dc-3b96-99f9-4998f3ee10a1 | -7.86995 | -47.88398 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c0eac4b8-a95a-3041-98b6-dc2630a76f60 | -8.42078 | -48.2936 | 2025-06-22 00:22:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 540d6edf-556f-35b4-9e75-92b9ef941820 | -8.11504 | -43.1531 | 2025-06-22 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 070d3005-f1cd-3f05-b43f-e7976fadaa10 | -9.99751 | -48.06132 | 2025-06-22 00:22:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a0a1689f-8a26-32de-bdf8-edf79df571e1 | -8.03147 | -47.65517 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 6cd823e3-f6f8-3864-afb0-32c4e06c1e47 | -10.0158 | -44.49582 | 2025-06-22 00:22:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 758ab8c1-586b-3046-93e0-bc0766733694 | -7.90076 | -47.12114 | 2025-06-22 00:22:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 924153ab-edf7-3987-9a25-8906d288b034 | -8.60706 | -51.60038 | 2025-06-22 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2d2db97a-87d4-3e01-ae80-3b7d343c87ca | -7.22894 | -44.66818 | 2025-06-22 00:22:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README2.md)
