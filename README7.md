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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a85db1dc-192d-3566-86ce-907a011132aa | -3.2774 | -53.6383 | 2024-12-02 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 66e0c7e7-1812-37b1-8bf8-fb66bc7f2a68 | -3.297 | -52.066898 | 2024-12-02 00:55:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6978f5b-c2a9-3a18-bfb9-1d5842fee51f | -3.5076 | -53.826401 | 2024-12-02 00:55:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac91cbd7-d892-3215-8543-4f7c8743d65c | -17.481199 | -51.820801 | 2024-12-02 00:55:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d062b1c-d465-31fa-96c8-b3361d00d9fd | -3.4027 | -50.231701 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae6b1830-bf1b-3de6-897a-d737e8767e5b | -3.5269 | -53.506901 | 2024-12-02 00:55:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98b201fe-ce94-3b90-92b2-e427e594bf7e | -3.4899 | -53.7939 | 2024-12-02 00:55:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d25b414-eb91-3dca-9932-91c334910a02 | -6.0798 | -48.0411 | 2024-12-02 00:55:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33410880-ad79-3f3d-90da-1b68e4b63a1c | -3.3701 | -49.874802 | 2024-12-02 00:55:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9477e397-aed3-35e1-97a0-f2c4179802d8 | -3.4616 | -50.264 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 173eae39-7c2d-3495-b823-23c799347579 | -3.532 | -50.1707 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7f4cd79-1d33-3034-8c2a-c25bb9167777 | -20.727699 | -54.424999 | 2024-12-02 00:55:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 88f157d0-2e06-3014-86e0-aa7ebc32d075 | -3.7038 | -52.179699 | 2024-12-02 00:55:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1d0c475-9898-3bc9-bf8b-5b80073eca57 | -3.7138 | -52.267101 | 2024-12-02 00:55:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 911d7890-0330-3d4c-b880-f3155a5a0364 | -3.2898 | -52.080299 | 2024-12-02 00:55:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b24bb43-7972-3743-a032-d2885955b72d | -4.2452 | -50.844002 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47297390-fc81-3928-82cb-0fc7e532a2ee | -3.6512 | -51.116402 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72181175-eb1c-3dee-b23b-deaa83e65a63 | -4.2549 | -50.841702 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec94bcf7-ec10-3e5b-a081-415b83759518 | -3.5447 | -51.452202 | 2024-12-02 00:55:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7595495-4b4b-3a66-9967-56d922e0a6f0 | -2.9048 | -45.823898 | 2024-12-02 00:55:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e7bbfa1-51ef-3a6b-b236-f5c7b04d8272 | -3.4947 | -50.317101 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1c6004b-f192-3fa6-8b21-895f1523e3cb | -3.4718 | -52.244301 | 2024-12-02 00:55:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65f773bd-23e0-39a4-8146-f253a20989b2 | -3.4849 | -50.319401 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5285cc93-d2c5-3650-9e53-14d024e91c49 | -3.7567 | -54.642899 | 2024-12-02 00:55:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96d17857-f403-3c6d-ab48-b924255faa01 | -6.0844 | -48.059799 | 2024-12-02 00:55:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7a9f69-d25b-3f76-ba6b-4e6f156f1c15 | -6.0747 | -48.062199 | 2024-12-02 00:55:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 270ac7a5-5f3b-3837-bdb3-79356d2f959c | -3.5335 | -51.492599 | 2024-12-02 00:55:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bad9810b-0981-3480-bcd4-66bb27a9ed0d | -20.726101 | -54.4175 | 2024-12-02 00:55:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b4fab13b-aa2d-33b0-8f89-7dbf701aab77 | -3.367 | -53.215199 | 2024-12-02 00:55:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0127afd9-57ba-3788-ab06-690b3b9e461f | -4.258 | -50.8545 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b48bb24-ac41-3b14-ad69-6f2106b9edac | -3.7163 | -52.277699 | 2024-12-02 00:55:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f8cf46-b00a-39fa-8008-f3fda7c4ae46 | -4.2318 | -48.624901 | 2024-12-02 00:55:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48ffa58c-f4ea-37ff-945b-f7fe50767712 | -3.7474 | -54.5121 | 2024-12-02 00:55:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb18269-a240-3eb2-a8a1-21bd7a29cf5a | -3.4519 | -50.2663 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa40ba01-5073-3788-bc28-b94abb939307 | -3.7456 | -52.270901 | 2024-12-02 00:55:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5115c5-6fb1-38e9-99db-087a113a28c7 | -3.7062 | -52.190399 | 2024-12-02 00:55:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a7a281-ebdd-3ab4-835f-b4ff42d4a069 | -3.3346 | -50.247601 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae3ff9c-03ed-3436-bd54-97a1166af8b0 | -4.8051 | -48.621799 | 2024-12-02 00:55:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5955ba44-2d57-319d-9f31-c50d73f1d509 | -3.5056 | -53.817699 | 2024-12-02 00:55:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f6c711-ebda-38a5-ae50-bde4cc7f6462 | -3.6955 | -51.834202 | 2024-12-02 00:55:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b83a90b-866f-3313-9c37-0184bb8e23e9 | -3.3993 | -50.217098 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 750c8d34-fd9f-30cc-9ef9-657d5c0934fb | -4.0437 | -48.952999 | 2024-12-02 00:55:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 345456b6-505c-32ed-a717-f01c2113f530 | -3.3664 | -49.859299 | 2024-12-02 00:55:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4c0ad6e-113b-32b9-8aa1-1b8a03eabe07 | -3.6415 | -51.118698 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19f075c0-9040-365f-b0bd-8223a926c1c2 | -3.6928 | -51.822899 | 2024-12-02 00:55:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d76ab76-4801-3b20-80db-1929901bce36 | -3.4998 | -53.8372 | 2024-12-02 00:55:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 390b7df3-e6da-3840-b015-06a21308e01d | -3.4881 | -53.830799 | 2024-12-02 00:55:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f4254b-b95b-3511-a77e-64bf16b27f14 | -3.7009 | -51.064999 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ce567b6-ad5a-3f20-b615-bd44842f7908 | -4.1858 | -50.678902 | 2024-12-02 00:55:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ab1fd8-460e-3c9e-b7b2-68da19068c6e | -20.7293 | -54.4324 | 2024-12-02 00:55:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 04836050-ab54-3dd1-9fa1-f9d01167a059 | -9.3485 | -58.215599 | 2024-12-02 00:55:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf673e97-37d5-35be-82aa-77511c0a2d62 | -3.1469 | -51.112499 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9b5eac-116e-338c-9306-aeef764908cc | -13.5096 | -61.512501 | 2024-12-02 00:55:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 666987c2-56e6-3c6e-a7de-cca1a2ff2354 | -3.3895 | -50.219398 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90556b2c-2cfc-3755-b1ba-b6630042674d | -3.7585 | -54.6507 | 2024-12-02 00:55:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 949ab0da-8caa-3eda-8b65-5a1edf4fce33 | -3.9604 | -52.1768 | 2024-12-02 00:55:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4e4e65a-653f-3d48-bf60-741c188a5926 | -5.5653 | -45.136902 | 2024-12-02 00:55:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e862c6f-55b5-369f-8079-f88fd14cc38e | -3.7431 | -52.260399 | 2024-12-02 00:55:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b08bf8a-8613-3989-8746-407f22de61f8 | -6.0604 | -48.045898 | 2024-12-02 00:55:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac37acd1-5fcd-335b-a943-6e8d8a349c51 | -3.3648 | -53.205799 | 2024-12-02 00:55:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06cc0d29-2561-38ad-849d-d389420058a4 | -2.9144 | -45.821602 | 2024-12-02 00:55:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52169d5a-f5cc-3fe1-b490-b96d41dd3306 | -3.7456 | -54.504101 | 2024-12-02 00:55:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c260c483-8c0d-30ef-9d27-24cb4117ecbb | -6.0656 | -48.0247 | 2024-12-02 00:55:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98ae2946-bed0-366d-a414-5410e1110725 | -3.393 | -50.234001 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc2db54-d663-3944-9c65-7016d01584c8 | -3.1567 | -51.110298 | 2024-12-02 00:55:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f7b2049-d50f-359b-bf63-b09846a7e84e | -3.0193 | -51.535198 | 2024-12-02 00:55:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51e69646-1a57-3a93-979e-5312e1b05a4a | -9.3501 | -58.223202 | 2024-12-02 00:55:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78522db7-3459-3530-bb9c-c0be34e28d99 | -6.0701 | -48.043499 | 2024-12-02 00:55:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3123083f-6f93-31e0-b8b0-bf292f437817 | -3.4979 | -53.828602 | 2024-12-02 00:55:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c69b1035-d1cb-3c29-9ef8-cf41931427b3 | -3.3627 | -53.1964 | 2024-12-02 00:55:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3708f079-8bac-31b7-89a5-84d275f661a0 | -6.065 | -48.064602 | 2024-12-02 00:55:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6aafeee7-020a-3a0e-a0d3-4ef3c36bce1d | -3.2846 | -52.058201 | 2024-12-02 00:55:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a77c358b-da0a-3b02-8693-eb2b2a5701c9 | -5.5729 | -45.167099 | 2024-12-02 00:55:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff54e023-a81b-334d-a4f9-c13548aa60e1 | -20.3267 | -48.816601 | 2024-12-02 00:55:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e57667fb-f0d2-380d-801b-7f19d0c90757 | -3.2872 | -52.069199 | 2024-12-02 00:55:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f4c30f9-0961-349c-a19e-75e280c90a3f | -2.5968 | -45.262699 | 2024-12-02 00:55:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bc91251-c209-3cf1-a4b4-22fb39f34078 | -3.7052 | -51.831902 | 2024-12-02 00:55:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb5dcf5c-e348-39d7-a2bc-9d4290b82714 | -2.0133 | -54.316799 | 2024-12-02 00:57:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc4a884-2e8c-3266-a937-b8bb3244b768 | -2.5626 | -53.388 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f44205d-230c-3eb9-a812-e5c8cdbc2c4a | 3.1822 | -60.183899 | 2024-12-02 00:57:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9b31bbd0-f49e-3f40-bff4-e3b12cc3c917 | -2.6311 | -53.372501 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1b3f0b2-ab54-3948-8b2a-38b940993bd9 | -3.2477 | -53.6362 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4c582f-33bf-3817-8800-e435a55fa4ec | -1.3849 | -55.175598 | 2024-12-02 00:57:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8763fd-2e64-394f-8162-40ed4b8ebd5b | -1.3399 | -54.977798 | 2024-12-02 00:57:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7d92fd6-2863-3a35-afcb-72969f7f430f | -2.8903 | -55.226601 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a777e51-118d-3cd7-b4c2-331e28738dbe | -1.6886 | -52.627899 | 2024-12-02 00:57:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5045aa75-3efd-3eac-a7d1-6bf2c8f4a133 | -1.5644 | -55.3312 | 2024-12-02 00:57:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16753a24-5c6b-3db2-86b4-8c4d3a8c5d50 | -2.6246 | -53.344299 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa640222-6e52-38e7-9f8e-d61e50853ef5 | -3.0143 | -54.055401 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c46d96-75d5-3dbb-88fa-ecca57ab967d | -2.838 | -54.0952 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc40497e-d958-325c-a16d-5b888dea6276 | -2.8205 | -51.830299 | 2024-12-02 00:57:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2178fe62-7fb3-30c8-a8df-cc2836de94f4 | -2.8341 | -54.078098 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b78de035-f5df-3efc-ac48-51e9d265b80e | 3.3907 | -60.4464 | 2024-12-02 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7e40dc23-3bca-327a-9f4b-fac61648af55 | -1.0751 | -53.452301 | 2024-12-02 00:57:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9620bbb-24ef-36dd-b506-93a28587b684 | -2.5451 | -53.401798 | 2024-12-02 00:57:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58246423-a909-305d-8e4c-d8dbfb60a467 | -2.8829 | -54.156399 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ef761a-751a-390b-865e-99216322615f | -3.2921 | -53.8297 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2ecca8-0f47-38a5-b241-f8e52782153f | -3.2632 | -53.613998 | 2024-12-02 00:57:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34fd897c-a731-36f9-9f91-6a04c26c8014 | -3.1812 | -54.334202 | 2024-12-02 00:57:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4be93f5f-4e7a-3fe2-80e7-4e450de4ff46 | -2.7605 | -55.3349 | 2024-12-02 00:57:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
