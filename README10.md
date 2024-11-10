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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ded4ba98-25ee-3b73-a587-5917a868db5c | -2.9328 | -51.48565 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e77d10b7-5d9b-3782-8c89-28e873a9fbd5 | -4.3818 | -48.58627 | 2024-11-10 01:19:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e63f926a-0930-339d-b888-c61c1feaf78c | -1.86973 | -48.45175 | 2024-11-10 01:19:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| a5098a86-fb91-3071-b782-b21eb744b54f | -2.93741 | -54.07814 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e9db7e1-e234-3769-8328-0c37ddaa7e3c | -2.92781 | -49.51211 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 02d2b509-b80d-35eb-b460-4d51cc91f8e1 | -3.61924 | -47.52052 | 2024-11-10 01:19:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e371d38a-de36-3069-b627-5af1e122f6e4 | -3.9511 | -48.15731 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 1e9431df-e5b1-352f-9b36-7ccdd4dc290f | -1.34813 | -51.41342 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bc0eb9f4-63e8-3952-9d7e-f8a8b699a2f1 | -0.95163 | -52.45182 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9caa1e32-7f33-3e60-9197-1afe554cf186 | -3.08699 | -51.12362 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fcf8c19e-fb85-3bbe-8d98-7bc539d312d5 | -0.04353 | -50.79253 | 2024-11-10 01:19:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d28781b6-377f-305f-93ef-ba74db6b8195 | -2.41628 | -51.95471 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| ce90cbd5-3a06-3bd9-89f6-27d7edb5de87 | -4.10005 | -48.98806 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| b57d0b4d-ed02-3532-bdd6-d8454b23bbcd | -3.4312 | -50.29414 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 99760b0b-8c95-371c-b7f5-230cfef5af45 | -3.89583 | -51.92781 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 86448793-707f-3067-9dce-b48d46c0bf58 | -3.66979 | -54.04439 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 48bd971a-1950-30eb-b1f8-a9eb658db8b2 | -1.47595 | -54.30036 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ca096586-e9b9-3ca3-b08f-0a0060daea22 | -3.95408 | -48.17801 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| a7f9f932-01da-3d94-a9a4-a6fa8b7ddb55 | -3.29457 | -52.94899 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 593f0552-48ba-3589-a4af-ce454694be0a | -5.81589 | -44.12897 | 2024-11-10 01:19:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e1905627-50e5-3663-a07a-5492e599b02d | -2.93475 | -54.12445 | 2024-11-10 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d25205da-b3dc-305b-8188-9639c4ebed80 | -3.35591 | -53.44814 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5caae46-883e-308c-b501-924c4a2ee5b4 | -2.64023 | -46.78224 | 2024-11-10 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 84ba56b4-a5cc-3ad3-a54d-12480c224b39 | -2.74052 | -54.11829 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72375538-371a-3c03-bba1-851162bf7ece | -1.1769 | -54.1384 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f67a6352-75aa-36ec-9a51-d11250ced63e | -3.672 | -54.65683 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 054ab06b-9ad7-3328-9500-eecd6ff73e37 | -3.32938 | -54.18103 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3feac788-8473-3e93-a7df-1c54c580b13a | -4.2184 | -45.44081 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 2417bd4b-cf39-3103-9fcb-650d1f9bff30 | -3.47904 | -50.38889 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2c69d7c2-8bd8-3e64-9410-8b0026919fe3 | -0.40495 | -51.47716 | 2024-11-10 01:19:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 09a87abb-e763-36df-9352-3ed98d4de895 | -1.33328 | -54.59893 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2315b415-7a3d-3838-b16d-3eb794ec5cc9 | -3.17238 | -49.09678 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a2e4933b-3246-373f-a5fd-8a257e9a4bcd | -4.68978 | -49.62634 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3a50301a-12e6-3431-8816-526fc9efa0e9 | -1.43061 | -54.50615 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18035285-7e58-34b3-959a-7c4b0470916d | -1.6422 | -52.05128 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 05b72780-7a6f-3bef-b514-ec592ee93cc2 | -2.81557 | -51.81452 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 045d5d29-44fc-3ddd-94ae-756a900f4cf0 | -3.21426 | -50.38868 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 7f4f8d86-e04a-3274-85b5-545ac05bc107 | -5.01248 | -45.05015 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| bd94d5ae-719f-37f7-9e3f-245a5e6a343b | -3.09616 | -49.40596 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e8c23c58-3153-31c5-b4ac-356d68818b50 | -4.20506 | -48.11667 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 6abe00e3-78f6-33db-a7e8-05b3b492d37d | -1.64284 | -53.38102 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8ae9805a-8467-3e00-8810-bc45d6f5f98d | -0.64351 | -52.36623 | 2024-11-10 01:19:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 41555920-16c9-35bc-b937-0af331ae56f7 | -3.29596 | -52.95877 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 5f6caa15-6f51-3944-8783-dd782e16fb4f | -1.65314 | -52.05513 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 48f81af7-6eeb-3831-bd6e-1d96c62caea3 | -2.42788 | -51.96466 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 0b08f8f0-3dc8-351c-9332-4cb8ab7d5471 | -3.25175 | -46.49526 | 2024-11-10 01:19:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 0f63727b-7a5e-35dc-b4f5-4d4e77d97fd4 | -1.48978 | -54.39955 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6d40b592-6ea2-3b5b-824c-99c9f2a2f3c2 | -1.93408 | -52.16431 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 98f97a1b-9075-368d-b316-8fed4c57e162 | -2.81481 | -51.80882 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 08c98542-a063-3894-b70e-e8bee05282d9 | -1.40902 | -54.48163 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e3218db-c37e-3423-996d-df0b7d44b041 | -2.08035 | -52.03925 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1a0bfe04-cf61-37d7-9bf8-2c203104f4e2 | -3.23315 | -50.27655 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 28676596-4e5a-313c-9e7b-bc2feb358870 | -3.05515 | -54.85854 | 2024-11-10 01:19:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| aaea1e65-13b0-31f4-ae55-ed848da436af | -4.09739 | -48.97019 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| edab3c62-124d-3bae-8a9d-643f86b7d095 | -2.68806 | -46.79821 | 2024-11-10 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 4cb8b4d6-fda7-35d2-a7e7-6c50fd45e234 | -3.48451 | -54.03713 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25df2fe1-cc1a-38a1-8194-4b66778f7d14 | -3.22684 | -53.05499 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 157.2 |
| ceddb93b-690b-379c-a8c8-e0a924b8b444 | -1.76399 | -52.68719 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 25b0d76a-2380-3978-81d1-3818236c71c9 | -4.12017 | -48.50768 | 2024-11-10 01:19:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6ea225ac-1e1a-324c-b889-6253d8f683d5 | -1.87355 | -54.17645 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 460eab23-a261-3ae7-94c6-9e871e633c0e | -4.73371 | -50.38548 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bb5bb0ff-ad89-3b5b-8d1f-ccb79aa0739d | -2.1155 | -50.57856 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 65f79e40-6a08-3372-912f-ef4df9931700 | -1.65319 | -51.91304 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cca88476-3cce-3c23-b9a9-75e8a5110b74 | -3.80505 | -49.94434 | 2024-11-10 01:19:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fdf1fda4-6fa9-3e99-ae98-d67893d627bc | -2.85052 | -53.97974 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b824616e-61d8-3f71-90bc-cdde7f8f2cb1 | -1.67317 | -52.05229 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| dbeb3ff1-baf9-351d-a732-45a1bcf7e726 | -3.04631 | -54.85978 | 2024-11-10 01:19:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e570cb18-8da4-3f89-8844-8c365c096fb4 | -2.92931 | -51.67963 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 01175874-06b2-303c-afe6-694f03bceeaa | -1.18583 | -54.20248 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 99594f69-8bc9-339e-b67c-767084738da8 | -2.53554 | -56.75101 | 2024-11-10 01:19:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9721ab32-8795-33e4-a017-e9afae2b5c75 | -3.14225 | -50.44847 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 5704f190-6782-36e8-9e8d-32d4360bb472 | -4.25556 | -48.54031 | 2024-11-10 01:19:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 84e24001-e437-3495-a769-ae91ea55770e | -1.68879 | -50.41051 | 2024-11-10 01:19:00 | TERRA_M-M | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d18e16f6-2777-330c-9779-d8b0db5fed4a | -2.97208 | -53.86367 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0a053cde-af0c-3ec8-8163-28f9928bd21f | -1.30641 | -54.66623 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d18f2bdf-aab6-3be0-8919-67fced88ae60 | -3.0291 | -51.09321 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a0643386-3888-3e3f-b07a-de6500443b1b | -2.0305 | -52.04637 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| fb378c07-14ac-3d2f-80f8-e9241bfd9b1d | -3.27212 | -53.70313 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 3b9dfbc1-a83d-3926-9463-00d51ad60639 | -1.48819 | -51.7547 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 904c9e7f-36fb-375f-b302-fac43d87a6ed | -3.27342 | -53.71231 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 504d4f87-0b8a-35e8-971a-236f2aae09c7 | -1.29751 | -54.66743 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f860b123-3171-3f06-a9f1-8a06a9e50783 | -2.71901 | -49.3027 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| b280de03-ef09-30ab-8498-782d8fa2cb30 | -1.33701 | -54.62569 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0754114-df13-36e8-8f6f-31776d2c1d8c | -2.45991 | -53.69436 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 24004d41-cff9-3c27-b7a9-42baf96a0c05 | -2.25506 | -47.06235 | 2024-11-10 01:19:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 564bf002-b930-3e4e-89e2-2392203e11d8 | -1.16459 | -51.92329 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b07d8137-9653-3094-ac65-70f47530df43 | -3.8709 | -50.08056 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d3c136d0-0b5b-3d8e-8344-2b24932a05e1 | -2.81977 | -54.09192 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 91cacbf3-a4e2-3507-857c-262d3aa7d43d | -3.87591 | -49.95866 | 2024-11-10 01:19:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 668b15bb-ad3b-3507-a0c6-0528a2b088c3 | -2.09355 | -48.8103 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 244b480c-99b4-3f74-9fce-e63c484d5aad | -2.63617 | -46.75414 | 2024-11-10 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 51a54bcf-d95e-32eb-89bf-db5f7030219a | -1.70737 | -55.02666 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 25cb1332-6fc7-32d0-96ac-2a1df3dcee4f | -3.35024 | -54.12662 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b269f304-f42e-39be-8565-45a5625396bd | -3.05637 | -54.86734 | 2024-11-10 01:19:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ee287c8a-42a4-39d0-98f7-328dc09c2e90 | -3.95867 | -49.02138 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c44beca8-9f4d-3285-936f-a42733048e8a | -1.42214 | -54.77055 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0ca4381f-0707-32ec-9864-ed21ef5e4761 | -4.06938 | -50.02357 | 2024-11-10 01:19:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c1943269-b8ab-3c22-83d1-2f99275c96ba | -3.2239 | -50.68478 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 756c7909-1685-3122-9608-05016d2bc6a9 | -2.49413 | -49.85749 | 2024-11-10 01:19:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 01f60cdf-4963-33c8-96c4-e8845a60c628 | -3.08473 | -49.57892 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README11.md)
