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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80ac5fdb-329f-34da-b7db-0d3c1259b664 | -3.84995 | -51.26107 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df1d07a7-28ec-3a79-b7fc-d6ac96018c58 | -3.81846 | -52.00374 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13c41076-3767-320a-9e25-21b9fea35f25 | -3.70117 | -51.07893 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9580fc1c-27f9-39a8-90ca-b15ac939e472 | -3.68683 | -51.11526 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05d14c8f-3857-3bb2-a997-3df947f33ae7 | -3.68501 | -51.1266 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e3f8ff4-bac5-372a-a152-215d941ca013 | -3.8874 | -51.94049 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01c38b5e-64c8-334b-a988-1b2c59bb65bb | -3.88211 | -51.7803 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 708fb9ba-7521-3fce-8486-4b168df501d6 | -3.87777 | -51.77962 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 678efa6f-c800-3180-a6b1-46e584e3e3ec | -3.87682 | -51.97819 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b543cc8-73d9-3a67-80a7-e768adad9260 | -3.87243 | -51.97743 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 345df161-2e25-36e0-980e-e7aa5d488220 | -3.77248 | -51.78922 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ce1b8b9-cb3e-30a8-ad41-98b5ec38479c | -3.7322 | -51.81705 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d27ce97c-2a7c-3686-9968-72a53418d5b0 | -3.71306 | -51.77116 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c321c442-03a0-3c10-a3cc-332ec8dc2fec | -3.59105 | -52.1529 | 2024-10-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 578e8dc3-0e8f-316f-8ad8-9f23efe894b2 | -4.28801 | -50.95274 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72eb52d3-b795-3e94-8c6e-704ebcc39845 | -4.27815 | -50.96303 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6808bc7c-7323-3583-aeda-a84210361bf9 | -4.27806 | -50.9622 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86971692-bcdc-3fdf-a557-c4a72a5078ef | -4.27407 | -50.9624 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca0e426a-0b72-34b7-82c5-32b0d8215374 | -4.27398 | -50.96158 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1c23b0a-77aa-35af-b0b5-be4389403e9e | -4.27337 | -50.96518 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49bafb5d-af09-3f76-b15e-a461ca368b9a | -4.26999 | -50.96176 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e15a97e-8c33-3705-bb3c-d4de507cbc2b | -4.26941 | -50.96537 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15929830-7455-32f7-90a3-4313096b5c2a | -4.26592 | -50.96106 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d18aff69-e24a-3203-af7b-dcc83c9fb9fa | -4.26534 | -50.96468 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b6a7737-1dd1-3a3a-a45d-6e6ed18e0636 | -4.14602 | -51.1022 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6900a61b-2db3-39a8-98e7-ba87c4f84807 | -4.14341 | -51.1024 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb553dbe-02a2-35e0-b95c-d3a16b5f77df | -4.14186 | -51.10175 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b81ec13-1b56-3756-a582-cca98043f85c | -4.12733 | -50.83905 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a85d79b5-f4df-3cfd-a346-7c521d7398f0 | -4.12387 | -50.83479 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 934f0406-ef37-361e-b4a4-0e44afe9b68a | -4.09327 | -51.09855 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aae94cb-ce0d-32a7-b37f-99ddc4fde013 | -4.0919 | -51.02951 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce07c7a-995a-367e-8c28-eacc04f368dc | -4.09067 | -51.03706 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2aa1997-7adb-39f0-9657-6b05b8baf4f2 | -4.09006 | -51.04073 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e92ff1e5-dd1d-38f4-b415-a53d261fbf30 | -4.08905 | -51.02127 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bb197ab-0327-3ad8-9543-fb3fee2abfa0 | -4.08843 | -51.02503 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b464ba1b-eaae-320b-a4f1-1b4b76beeac8 | -4.08781 | -51.0288 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17a39d23-61d0-36ba-a6f4-44215a93336f | -4.08718 | -51.03259 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f266a478-30eb-30a5-a74c-ce42e858b935 | -4.08432 | -51.02438 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74d4abaa-5c5a-37d4-8a5a-d781991fd98d | -4.0837 | -51.02816 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b929bf5a-c972-34da-989a-8f04b499ddae | -4.08308 | -51.03189 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f7ba2f3-3610-3094-9e9a-5e10cb1cc972 | -4.06492 | -51.11634 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43f21ce6-b031-30b8-888e-4487b54f87bf | -4.01734 | -51.00219 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e3331c74-895a-3279-b703-17e3228f8087 | -4.01672 | -51.00598 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2494d861-a304-393d-9629-871f4a0196a9 | -6.39275 | -52.72046 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b335e5d-1508-3648-bb3b-bdc82e18aeaf | -6.392 | -52.72482 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f06974e0-c186-3f01-aa1b-8a794947b317 | -6.38757 | -52.72404 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21f0da82-56d4-3385-9157-8d36850fe653 | -6.31373 | -52.78924 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f48d8b67-134a-386d-9725-eac01b2e86cf | -6.31297 | -52.79372 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ade9334-a6c2-3435-9011-67c4d89b258f | -6.02698 | -52.48219 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e667138-bfb3-3e4e-b5f9-cef2754597d4 | -6.40866 | -51.73071 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 693cefad-95ee-3f49-b5da-ea36f5e0e366 | -6.40514 | -51.72622 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f965eb4a-794d-3dfd-b316-b0719d22b44f | -6.10082 | -51.22123 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d03bbe94-7a42-3f70-8337-58412cb4e708 | -6.09618 | -51.22418 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e4e17e9-b4d2-377c-aacd-edd4d6af7799 | -5.75276 | -51.45491 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68779062-54e2-3812-a5e8-a62c10215478 | -5.68267 | -51.29957 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c32186fe-399d-3d80-8da7-a9773172a43e | -5.63869 | -51.58969 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45e4952f-4324-3a33-9cff-070605f43602 | -5.61295 | -51.16658 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00dec720-2b25-36f1-ac7c-dbbab3ffbe9f | -5.55596 | -51.61605 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12cc6db3-e127-3dfd-8591-5d78d9053501 | -6.40928 | -51.72693 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82b00092-0bd4-3513-b47f-f5e8482b8fef | -6.40578 | -51.72234 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7dd7c5f-46a8-3ef9-bbfa-22955caa359a | -6.33946 | -51.71132 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a8450e3-3d18-3d15-88f5-d4c7a175be5c | -5.94528 | -51.5757 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdac4676-5fbf-3e52-8e77-a54adb8a40df | -5.91442 | -51.43889 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87a7dd8d-824c-321c-91e1-186661898276 | -5.90973 | -51.44184 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17684363-9f41-37ab-af7e-3f6ad4fc994e | -5.67861 | -51.29885 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 028378a8-63a1-3484-9749-838bc882c0ee | -5.678 | -51.30248 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 135d1516-99d8-38e2-abe0-f8810fc56ebc | -5.61237 | -51.17011 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cdca8d9-64be-3ddc-a210-1de5b80557bf | -3.32633 | -53.22494 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ada2078-faf3-3e01-8601-b7035ef16331 | -2.98562 | -52.90533 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 04256b98-e3ff-3caf-96ce-7589866079fd | -1.66061 | -52.14262 | 2024-10-11 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b02e321-05df-3918-b1d8-62ac5d550ef0 | -1.31968 | -52.49463 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b8877b3-0051-38d5-8239-620614ccf43f | -3.44453 | -52.72378 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11149d4c-22dd-33c4-8b26-30c2ba3d3970 | -3.33116 | -53.22569 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 848766df-07b8-333f-9477-bd269c8a9fa0 | -2.98122 | -52.90625 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 07059ad1-62b7-33f7-9034-9e121047a03e | -2.98006 | -52.90959 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| adf224f3-596a-337e-826b-68a9b458caee | -2.97926 | -52.91462 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9707a800-e0e0-35a6-a777-53da5c470eb1 | -2.97564 | -52.91043 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b0489d1d-2368-3f3a-8580-0907cb46f6a6 | -2.97257 | -52.8997 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9bd2d702-de73-3e3f-95f5-408f1c9859cb | -2.97173 | -52.90465 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a7f84339-3dfc-307b-9907-2711d47ab257 | -2.97137 | -52.90298 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e5554d0a-ffee-3b75-bec7-e17b7c38934f | -2.9611 | -52.90619 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fb63d98a-d99c-3388-b1b5-8e8ebc3094b6 | -2.84318 | -52.90681 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 832a4d40-9112-3e83-9529-a1d773d8da6a | -2.84215 | -52.9434 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a6b94d4-33e3-3049-8fd7-1acb78cf770c | -2.839 | -53.31965 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f93f4c67-eb07-365a-928a-3ebfc4b5aea5 | -2.83809 | -53.32513 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0354b80e-edcf-3c6e-8148-2240d1177b05 | -2.68057 | -53.3493 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c574e9b5-fd7b-3aee-bb37-24fcb5fdc8b1 | -2.67914 | -53.3477 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a643e94c-c6f5-3609-ab6a-f47220c23276 | -2.67422 | -53.3469 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c8929be-db0d-3801-be24-8a4b1fbcb7d3 | -2.67332 | -53.35242 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 588e9bf2-6c6a-388a-8d8b-ffacaeea567b | -2.66929 | -53.34608 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b5a3ab7-a22e-39ea-9513-695ab3b57ced | -2.66751 | -53.35715 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5074ad3b-b10b-3d34-9def-4ed04d3855b0 | -2.66348 | -53.35078 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 11579b19-232f-3cc2-8809-79c7b2448fb3 | -2.65946 | -53.34445 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7a3a10d1-3c01-3e3f-a47f-bdcd699d1c84 | -2.65364 | -53.34915 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 4ffa96e0-81cd-3e26-b312-289275b54282 | -2.25294 | -53.47678 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70d9704d-920f-3166-ab04-df2bcb5b1bfd | -2.25247 | -53.47959 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d42b694a-4b34-30e6-9a71-eaae3329e806 | -2.252 | -53.48242 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 198c0ea0-e426-31a4-90c1-57d865176e80 | -2.24705 | -53.48209 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bab9862d-7280-3260-8d48-257e6b029c35 | -2.247 | -53.48161 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f9927b2-033f-32ad-9f77-03b11fff7266 | -2.24653 | -53.48444 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README51.md)
