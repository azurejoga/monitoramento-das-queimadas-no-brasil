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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8bce756-33ae-34ad-8dde-56d59ac5e617 | -6.17776 | -41.21877 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ad969de5-5130-31ba-9250-88dbbb825171 | -6.1762 | -41.22532 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a210dcf-aae7-3c29-988c-1267c3573cf4 | -6.40683 | -43.33401 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6deebb3-d43e-3498-9253-b4cbeb409147 | -6.45328 | -43.31599 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 879ca41b-f057-3fd8-9040-90edbdcedcf6 | -2.29661 | -48.57292 | 2025-09-16 04:49:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4f07fe3-77f2-398d-b503-9b10b01abaac | -5.78979 | -43.94898 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 653a51d1-ce9d-35a5-8189-4c6dd18b341d | -5.19574 | -45.58636 | 2025-09-16 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0a74557-a225-3cf2-81d8-711e8ac86536 | -6.9633 | -44.45242 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb95973f-c588-39b3-af2f-7de179371aec | -2.99865 | -47.45398 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 901d355c-228d-3e81-92f4-ce2f420b8991 | -3.89761 | -52.1214 | 2025-09-16 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42d1c26d-0944-349a-9b80-3495432b1b32 | -7.44317 | -46.1735 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9b94646-cf3a-32f4-9c9d-8586065939d8 | -3.82676 | -44.10778 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f860a7b1-43fe-3bfb-8a28-6c4af2a0d550 | -6.34952 | -44.31472 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1a7ae63-d2ca-3de6-b644-5d0d39693064 | -7.9339 | -47.64996 | 2025-09-16 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8ad320f-bf4d-37d4-b882-115ed0b457a4 | -7.38731 | -49.99206 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bce239b-2792-3ff6-b60f-356412c6d019 | -4.17649 | -48.57581 | 2025-09-16 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82002bc6-7551-3959-85ae-d8f16648c661 | -7.06252 | -44.17297 | 2025-09-16 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6de020cd-670d-3b92-8ce7-11ccf99f3228 | -6.19031 | -43.47326 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20053b38-57ab-3a3e-aa56-fe20edd0e85e | -7.66356 | -44.47697 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0096fdfb-2a20-3f21-8754-c470d2ced0ce | -3.65428 | -54.06 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 161542c1-d748-31ec-b8d6-f808373ce377 | -5.77162 | -45.52591 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b19d31c5-56f4-325b-82a7-3a5edd83946b | -3.00044 | -47.45187 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ea7c225-9546-3d09-b58e-c654588c95ee | -5.55095 | -44.97391 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb713c12-a0eb-348c-a990-2d2684882318 | -3.81172 | -41.56402 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d4f80c7d-1a75-339d-9fa9-14841596be25 | -3.95072 | -49.43475 | 2025-09-16 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21601e20-962a-3066-b91f-1325637d46bf | -7.00132 | -44.57957 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d762a41d-567b-31c2-af39-d71eaef37272 | -5.342 | -44.82803 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b15b3ed-a1f2-3a9e-83ea-497112a63de8 | -3.81232 | -41.55987 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ed1d108a-945f-352e-b3b0-9211d8b8f151 | -5.7794 | -45.88885 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b864a67-edc1-3481-bc2f-216b17f71793 | -5.6443 | -45.95229 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30583bf6-72c2-3c08-b25b-6fc6ec11fb61 | -4.00733 | -43.23542 | 2025-09-16 04:49:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdb30e44-c8bb-33ac-875e-aba0217718b6 | -7.203 | -44.38346 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f19bcb7c-dc72-396e-89be-9b7fd6ec19f0 | -7.40659 | -49.98115 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c18182f-3c86-3d94-8f98-3cb611652fc5 | -7.38376 | -49.99149 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2904439b-d556-305d-b9c0-3cdc396525af | -4.27109 | -51.1085 | 2025-09-16 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8215fcd7-16dd-3f09-aa9c-b4526a3a81a2 | -3.96752 | -47.57168 | 2025-09-16 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a3be73d-26b5-3a91-8606-07f4ab4bdb21 | -7.09157 | -39.67169 | 2025-09-16 04:49:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5fe55a2f-7bee-37c5-80c2-abd3003bf2e5 | -6.52208 | -51.1928 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f063221-fa06-3de4-8dd5-34b48918d55b | -7.40357 | -50.00137 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 078949b3-9982-37f6-82ef-b29f5e3f34ce | -7.67773 | -46.29555 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba91e24f-29b9-3993-93de-0d96b8241374 | -7.67126 | -44.49641 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5516312d-3873-31f7-9db8-ff4d0d5daf6b | -5.81101 | -44.86353 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66cd891b-a4e6-3d24-b1d3-977b3b04d069 | -6.5501 | -44.00681 | 2025-09-16 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 973c1732-5be8-33bc-9850-b9fa989e19bc | -3.82185 | -44.10707 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61bcaf79-c2f7-3e25-aea6-303204fbd077 | -3.83332 | -44.11013 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6da3cf2-6e28-36fe-97fe-e974a8be87b0 | -7.71149 | -45.30522 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e23ba4a4-b1ae-3e29-ba88-d6ca138734d5 | -2.3725 | -51.90615 | 2025-09-16 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf251654-e020-3ac7-b118-10d70803f66b | -7.27591 | -46.59417 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97061d24-5e7e-3b8f-9c49-2543a6bc0e4b | -6.05615 | -43.55185 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f7a48c0-d456-3264-b556-93b832f95671 | -7.30476 | -43.92691 | 2025-09-16 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad4cb65e-81e2-31e7-b8c7-78f21984170a | -2.36865 | -51.90907 | 2025-09-16 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 523d2b3f-c544-3d09-a7fc-6c48aba7785d | -3.65144 | -54.05571 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65f8c7ba-361d-3b09-a33c-775d318d4f69 | -7.97743 | -45.63498 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dad13ad-8bae-3ecd-9419-105ccfb708fc | -5.79067 | -43.94298 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38253f27-df0b-35be-bbed-4d3b529dd1ed | -8.32761 | -44.73547 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b18e6fb-da2e-3a8d-b0bd-f4200b2188a8 | -7.13537 | -47.97768 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5ad3900-d201-345a-bee9-04781e8d65f4 | -7.36252 | -44.29128 | 2025-09-16 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e597daba-0e5e-3214-a5fa-96776de41e3e | -3.23759 | -52.25729 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42c0d04a-aa24-3f7a-86d6-803e4a79cdf5 | -3.21377 | -47.12693 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b1b8f0a0-3b8c-3fa0-9746-d68043b8623f | -5.76403 | -52.37032 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08df9671-d6b7-3e44-ac17-730bbe832a52 | -5.53733 | -42.66068 | 2025-09-16 04:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| f7095261-23b8-356f-94c1-ee68517cfef4 | -6.4474 | -43.31874 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe40cdf6-ab5d-3d61-9550-3639c469b9a4 | -5.7784 | -43.91959 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 011be1e1-f09e-3ed7-83eb-21ce0766113b | -5.79206 | -45.92701 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb1057f2-3090-311c-bb0f-be370129ea19 | -5.53841 | -42.66138 | 2025-09-16 04:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 82918bd3-fe0a-3b04-876b-373596e15774 | -5.05969 | -44.32297 | 2025-09-16 04:49:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff887bc4-928d-39c5-b3f4-6f5b2091dad3 | -5.8935 | -45.75097 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97896b93-a388-3776-a93e-cce6806cf5e5 | -7.14185 | -47.98907 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7c5e0d36-4212-364d-a160-f1fe289bc3c3 | -5.59835 | -45.36144 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6ebfc8d-4285-30d1-9197-8712b3956297 | -5.77705 | -43.92882 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a1ba33e-8ed9-32d0-ae1f-d045216e6e1e | -6.44294 | -43.31121 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98053bec-9826-3c6f-af06-1c31c6be7583 | -7.38582 | -49.99862 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3720f1b0-a1f2-3e16-b28b-bb0aaae81306 | -6.63307 | -47.88519 | 2025-09-16 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ab97e97-7a54-3925-9dfe-cfd9ed9f9bf4 | -8.34041 | -44.71727 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c8e2b2c-c998-300d-bf04-d49d585932ad | -5.97894 | -45.8404 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96bd0dc8-1d0b-3f97-9fc8-9a2000063614 | -7.38669 | -49.99608 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed811f8c-d96a-3a0a-80df-7f934da2f1b4 | -3.8284 | -44.10939 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7c85d71-4a03-3e59-a84e-d1e08ecd54ee | -3.4015 | -46.90356 | 2025-09-16 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d8d03d0-7a97-3b72-926b-4294bf7afde0 | -6.17871 | -41.20661 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 492cad28-ff3b-3e1f-af7b-590c95901dcf | -7.52271 | -44.35881 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 686cadd7-ff13-3b8d-8a4c-8cbc146f2c4c | -5.78669 | -43.95238 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1dc973c-b852-3eaf-831b-21476029c7e5 | -3.42354 | -43.15532 | 2025-09-16 04:49:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b584f55c-2f9f-3e6b-bb49-a7b73451c715 | -2.68629 | -54.42903 | 2025-09-16 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 222e9c67-2e10-3abd-90cd-cc6ff10a187d | -6.34061 | -43.15628 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d45cad5a-5a4e-3f2d-8083-e7542c10fa62 | -2.67151 | -54.79358 | 2025-09-16 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76e7d53f-f015-38d2-8cee-b545df44cae0 | -5.89772 | -49.10221 | 2025-09-16 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 348ad1b6-e842-37f1-94b6-9d7a5b6a906f | -1.22486 | -54.12456 | 2025-09-16 04:49:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9c1bc10-6e62-36c6-a96a-945b0bfad135 | -5.78935 | -43.95198 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed34fa86-309a-3a2d-84c8-32db7f87e02a | -2.16025 | -46.39902 | 2025-09-16 04:49:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21c36ab2-7829-3a47-92c0-09e03a7128dc | -7.68281 | -46.29197 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b7520bd-fa44-3473-9149-0733a5fbe02b | -7.52128 | -47.65812 | 2025-09-16 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6172576-2c64-3adb-8b33-d258cc8fa31e | -6.15967 | -45.11907 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c841dcd5-5c96-3be7-8efa-dba33aff5939 | -8.12747 | -48.26114 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 441503c8-40f2-3868-a5c8-cea25243fea0 | -8.11807 | -48.27025 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f95f90be-1a7a-3cc8-a183-d184a20f981c | -8.33192 | -44.74142 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c874c8-3402-3aeb-86d5-835d092e5dab | -5.56191 | -44.96513 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f961c43a-3a9f-3b00-adaa-14fd7ad3ad8c | -8.00684 | -45.6644 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30547744-6f92-3b2a-8ff7-68f834ad03ed | -7.86663 | -48.15094 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ea24cbc-bdfc-330a-b976-d9a14ab4fc3e | -5.90138 | -49.10276 | 2025-09-16 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7174c70-6dec-303b-a280-1fd18f37b0bd | -7.68249 | -44.67559 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README62.md)
