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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d8650f6-78dc-305f-9841-05615ac4fa6e | -5.7448 | -46.4979 | 2024-10-17 00:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 75d5e101-b59b-3681-ad2c-5953aecc92a7 | -5.9788 | -45.3621 | 2024-10-17 00:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f17f5b83-af53-3c08-8207-ca3673668ab0 | -6.7086 | -43.5605 | 2024-10-17 00:05:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1a71dca5-d1b9-3cbb-a660-711d927be399 | -6.7272 | -43.5822 | 2024-10-17 00:05:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a4f8f200-b872-3b27-ab6f-49c0879c2fbb | -6.7274 | -43.5589 | 2024-10-17 00:05:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 492ad2a1-8105-34d2-b841-1d16c280aaee | -6.7277 | -43.5356 | 2024-10-17 00:05:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 08737b5b-399a-32a2-bc88-01bfd3fc2227 | -7.8727 | -45.3593 | 2024-10-17 00:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b4dbfedf-2fa2-3252-9383-b032609f1c45 | -8.722 | -41.1523 | 2024-10-17 00:05:55 | GOES-16 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 00a35b38-0e06-3395-bb3d-e36bd94d5f0c | -8.4631 | -66.9597 | 2024-10-17 00:05:55 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 70b8ed57-047f-359f-a623-0bc36c24e490 | -9.6232 | -68.6714 | 2024-10-17 00:06:01 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 050b759d-2a8a-36ad-98cb-3aab7bf11216 | -9.6417 | -68.671 | 2024-10-17 00:06:01 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f6e9eaf0-a64a-3335-b1d7-5786c06b17a4 | -10.1288 | -56.7921 | 2024-10-17 00:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 85fdbeeb-9764-3cbc-91c2-4a1676923552 | -10.129 | -56.7722 | 2024-10-17 00:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 5f6ebf3c-03ca-3a3a-a56d-32ed08d21508 | -10.1292 | -56.7523 | 2024-10-17 00:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 32750399-d217-3e03-9bfe-1075b3d6a605 | -10.1477 | -56.7709 | 2024-10-17 00:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 92b1aff1-fa48-37b3-9ccf-a83b66eefea7 | -11.6915 | -65.2432 | 2024-10-17 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cc2eecd4-08e8-3bf7-97a6-f82a4141c0e3 | -11.7103 | -65.2424 | 2024-10-17 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 16a7cce9-c0b5-3b11-8b1a-b912d0e27455 | -11.7104 | -65.2235 | 2024-10-17 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ad4bbdff-ecd3-3700-95d1-0622fd315e06 | -11.7308 | -64.9769 | 2024-10-17 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| b8a8c1a9-afaf-3991-8027-c248c637db10 | -11.7309 | -64.9579 | 2024-10-17 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a498b416-0049-3d69-8671-86ed2e0ab9b2 | -12.3804 | -53.1376 | 2024-10-17 00:06:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 20dbb67c-c809-3f72-87ca-d6af77fc0e4d | -17.1667 | -56.8232 | 2024-10-17 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| dec3b901-5d95-3566-8a2f-59fbf6f68326 | -17.2084 | -56.6739 | 2024-10-17 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| fbf40b1e-3a7b-3fe6-9c59-58218045e6fe | -17.9036 | -57.4534 | 2024-10-17 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 2b8c050e-d116-33ff-8585-6bbbd2a5efb3 | -17.904 | -57.4328 | 2024-10-17 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 1ca23348-328d-34a4-b42e-c2fce54cc7da | -17.8049 | -57.4655 | 2024-10-17 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 5d980983-11ed-3b5b-bc56-93d9991659f5 | -17.8052 | -57.4449 | 2024-10-17 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| c6d71e0f-d89a-38ad-b48e-4162c33fa76d | -17.8839 | -57.4559 | 2024-10-17 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| f01f8cad-c8fc-35bd-8442-8ed184f4f807 | -17.9237 | -57.4304 | 2024-10-17 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| a16bb830-de79-3cf8-8ab8-2e1727f22ad4 | -20.1865 | -52.1546 | 2024-10-17 00:06:58 | GOES-16 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 12a8c7d1-a8a7-3147-bd56-e55016318cf7 | -20.187 | -52.1325 | 2024-10-17 00:06:58 | GOES-16 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 6d4e173d-261b-39f7-af0a-7b269d5341e0 | -20.2073 | -52.1287 | 2024-10-17 00:06:58 | GOES-16 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 4c8e80c1-aea3-3d13-bc90-e452ca5a82c8 | -2.8333 | -49.1562 | 2024-10-17 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7e95c9b8-e725-39a1-b54d-c4f89c348bbf | -2.8795 | -51.6901 | 2024-10-17 00:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 80484985-c669-3a4e-b46b-592850593666 | -2.8979 | -51.6896 | 2024-10-17 00:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1f3db699-da63-3387-9e5a-2249d38b055a | -2.9673 | -48.0147 | 2024-10-17 00:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a96f819b-f8c0-3db7-9965-b0b5c00d420a | -2.9674 | -47.9931 | 2024-10-17 00:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| a814ca31-4c15-365a-986a-02d19beb276b | -3.0581 | -53.2395 | 2024-10-17 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| f4688d0e-d513-337f-b930-e07a9c0f3d73 | -3.204 | -48.9312 | 2024-10-17 00:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| e50ed6a0-647e-3fde-8f2c-b1846fbc212c | -3.2041 | -48.9098 | 2024-10-17 00:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6d2b8d70-d62a-32be-b014-0b3cefb2c34e | -3.2225 | -48.9306 | 2024-10-17 00:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 09b60a31-01bd-3561-84d3-13ac770ad167 | -3.2226 | -48.9092 | 2024-10-17 00:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f5d3d7c7-0156-3b5c-a0e6-7381e6400337 | -3.6822 | -45.9231 | 2024-10-17 00:15:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.7 |
| cddd1f32-022d-36cf-b9e6-d7f4d8633e8b | -3.6823 | -45.9008 | 2024-10-17 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 3a41bf18-2153-3488-b8cd-1fedbcbcf775 | -3.7007 | -45.9223 | 2024-10-17 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 196.1 |
| be0192d9-a820-3e18-b740-8197a8769d99 | -3.7009 | -45.9 | 2024-10-17 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 150.4 |
| fa459adf-777a-3323-84b7-de246c22f4f4 | -3.7193 | -45.9215 | 2024-10-17 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| e8f66175-488e-3c5d-ae29-b2a6c410bbd9 | -4.4658 | -42.8643 | 2024-10-17 00:15:31 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| cc885bd4-b632-39c5-9c93-7665cd7ff0a1 | -4.4845 | -42.8631 | 2024-10-17 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| ed7d35cd-fa9a-347b-a9f9-99a70ceedab4 | -4.3646 | -46.8221 | 2024-10-17 00:15:31 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 638a35f1-464b-34ca-9e96-547e1d35b64f | -5.2306 | -47.9566 | 2024-10-17 00:15:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2bddaadb-c88d-37c8-94d7-b48419b10edf | -5.7135 | -45.7861 | 2024-10-17 00:15:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4d4952e1-056b-3e5c-b637-d4a0074a7fd0 | -5.7137 | -45.7637 | 2024-10-17 00:15:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6d118912-6c55-3e5d-bc5c-77603293f1d8 | -5.7448 | -46.4979 | 2024-10-17 00:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| edd62981-2ae0-3079-93d1-dae255f387d3 | -5.9788 | -45.3621 | 2024-10-17 00:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b89c6a5f-95e4-3354-b10e-2fe0c8d675f4 | -6.7086 | -43.5605 | 2024-10-17 00:15:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 85444227-117b-3de2-8caa-e4a1bc13d94d | -6.7272 | -43.5822 | 2024-10-17 00:15:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4338f431-6612-3bb8-a71c-800c6f5bc679 | -6.7274 | -43.5589 | 2024-10-17 00:15:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 232.8 |
| cc26cfc3-cf80-30c1-be21-2abd8c8f9d56 | -7.8539 | -45.3611 | 2024-10-17 00:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1c8da2aa-3710-3d29-965a-18cfea5467da | -7.8727 | -45.3593 | 2024-10-17 00:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| cce36a34-3f48-36d0-946e-7e72dacfb976 | -9.6232 | -68.6714 | 2024-10-17 00:16:01 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 267c14d8-5375-3575-aadb-2e7056c9af66 | -10.1102 | -56.7736 | 2024-10-17 00:16:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 11ace600-14e4-33a1-a7c5-f1a641b66838 | -10.129 | -56.7722 | 2024-10-17 00:16:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 150.9 |
| b6e41fd6-a3b6-3431-8310-c5bcda0cab16 | -10.1477 | -56.7709 | 2024-10-17 00:16:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 97de92e2-90fd-30e3-a9d4-11c002e9c73f | -11.6566 | -64.8288 | 2024-10-17 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ffcb2055-6837-3d15-af94-8753a416e911 | -11.6915 | -65.2432 | 2024-10-17 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 34218af4-e6c5-356c-a6cf-5ed2cb6b8ced | -11.7103 | -65.2424 | 2024-10-17 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 48f10796-5fb3-37fe-a728-01ed02407754 | -11.7309 | -64.9579 | 2024-10-17 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7c835f53-4b94-3afd-b275-acbb74893f83 | -11.9383 | -64.854 | 2024-10-17 00:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 8c3b3dfb-429b-3e6e-897a-9d93984a235b | -17.1667 | -56.8232 | 2024-10-17 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| ef5995ec-e776-3c54-bf2c-7b4a09f0c519 | -17.9036 | -57.4534 | 2024-10-17 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 74447f84-e169-3e0d-8123-bebf7bf1bfd5 | -17.8049 | -57.4655 | 2024-10-17 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 691e381a-518a-37b2-925a-91a6fabffdee | -17.8052 | -57.4449 | 2024-10-17 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 18a6a452-992d-3aa8-95e8-0075e1438b26 | -17.9234 | -57.451 | 2024-10-17 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.3 |
| dbbcb73b-d721-3f70-a5ad-d22e841fd81e | -17.9237 | -57.4304 | 2024-10-17 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 426ec469-fd72-3a56-afa8-153d962607e8 | -20.187 | -52.1325 | 2024-10-17 00:16:58 | GOES-16 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 59b3de6d-b776-3751-913d-fee62bf10183 | -20.587999 | -47.537399 | 2024-10-17 00:17:15 | METOP-B | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 28cca64b-158f-3ebe-ade9-9731d4b0f97e | -20.5902 | -47.5495 | 2024-10-17 00:17:15 | METOP-B | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4d341fbc-1563-3e06-a967-f86da1eefe0c | -19.637501 | -43.472801 | 2024-10-17 00:17:18 | METOP-B | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 09f40f83-59ec-31ac-936c-9e9a90aaeaad | -19.639099 | -43.4804 | 2024-10-17 00:17:18 | METOP-B | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe2d677-d4ec-3ec9-aac0-a270a569a344 | -20.245899 | -47.276798 | 2024-10-17 00:17:20 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6b459b15-2c35-3af8-8481-5828d29abc00 | -18.397699 | -42.193199 | 2024-10-17 00:17:34 | METOP-B | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd58176a-39fb-3613-b963-9ec02988ca5b | -20.1856 | -52.104198 | 2024-10-17 00:17:35 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0077610f-664c-362f-9ee5-c3779db3e6d4 | -20.1894 | -52.127899 | 2024-10-17 00:17:35 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c79a7735-0bb9-3ed6-80a4-67f32174bf1c | -17.842899 | -40.094299 | 2024-10-17 00:17:35 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e46cb71-571e-39de-820b-4c414ec4ba76 | -17.8447 | -40.1021 | 2024-10-17 00:17:35 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 056c56dd-a35b-3fc1-8d23-25d20a20f9f1 | -17.8332 | -40.096699 | 2024-10-17 00:17:35 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c179d582-f79c-3fd0-971b-722d97d4822f | -17.834999 | -40.104599 | 2024-10-17 00:17:35 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af9328a1-9d89-3adb-937d-f160c884ffe1 | -17.893101 | -42.1926 | 2024-10-17 00:17:42 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed3270ec-1cee-30b0-b37a-6d51cdd30c37 | -17.894699 | -42.199799 | 2024-10-17 00:17:42 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a476af9-95c8-3904-9c99-cc1f6833f19c | -17.896299 | -42.206902 | 2024-10-17 00:17:42 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea3e493e-908b-31cd-9ce9-c739fbf3c577 | -14.5572 | -43.126301 | 2024-10-17 00:18:39 | METOP-B | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c30688fd-558b-342a-a848-31c2441acc4b | -12.1487 | -40.8815 | 2024-10-17 00:19:10 | METOP-B | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a12b5cfe-08d9-3390-9a97-6be6f07d5687 | -12.1506 | -40.889599 | 2024-10-17 00:19:10 | METOP-B | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7f80eab6-d825-3760-852c-75c954269f9e | -12.1371 | -40.875801 | 2024-10-17 00:19:10 | METOP-B | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| eeb1d3b7-98bd-33d4-9367-342c8d2d1722 | -12.139 | -40.883801 | 2024-10-17 00:19:10 | METOP-B | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b58496c7-4d62-3f69-9331-db11aeb10733 | -12.1409 | -40.891899 | 2024-10-17 00:19:10 | METOP-B | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 373862a2-0ca7-38b5-add5-fde406f4fccd | -13.4823 | -49.283001 | 2024-10-17 00:19:18 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4b898357-ed99-3fbb-b836-fe6288dd8e52 | -13.4847 | -49.295101 | 2024-10-17 00:19:18 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 661dfb27-a791-32c4-838a-c50c982ff71e | -12.5272 | -46.810799 | 2024-10-17 00:19:25 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
