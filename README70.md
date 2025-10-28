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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83da7c36-5f29-368d-ab15-11ada9c91b38 | -8.646 | -45.2806 | 2025-10-28 04:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6c21301d-57b5-3bad-a78c-1147e5db5bb7 | -11.2798 | -45.5052 | 2025-10-28 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 13eb9fb6-afc8-3fab-8629-caaf8b8ce8e6 | -4.4604 | -43.6337 | 2025-10-28 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| da795fe4-6f7e-33e8-9d70-a9f55ca90be4 | 3.95262 | -59.64803 | 2025-10-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03366c46-076a-30bd-8ad8-aedb94d7469f | 3.34777 | -51.36901 | 2025-10-28 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 212ffc21-8e90-3635-b6b3-be926c0b343c | 3.35851 | -51.34808 | 2025-10-28 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b967dd1-7746-3743-9b49-8f97c12d1200 | 3.95223 | -59.64694 | 2025-10-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10f05981-fea9-31f4-9219-0cd3338e9bc0 | 3.94783 | -59.64761 | 2025-10-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 635b588b-4798-3dce-9ada-bb9ce2972902 | 3.94823 | -59.64869 | 2025-10-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63b039ba-892b-3c61-8377-1684a5cae4ed | 3.35121 | -51.36848 | 2025-10-28 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e924260-bcb2-339e-b146-071c33724e9c | 3.37795 | -51.3373 | 2025-10-28 04:59:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81006ee9-06d1-3282-bdc4-488dce25291b | -2.7556 | -45.3995 | 2025-10-28 05:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 45.4 |
| c92cb73b-5bcd-3bbd-b949-1312ea7584bb | -7.9459 | -45.5335 | 2025-10-28 05:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| fd4dfc28-8e5a-3050-91b7-616eb6d4e448 | -3.0344 | -45.3672 | 2025-10-28 05:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b30fa1fb-5c0a-3240-b46c-d2ebf2669ab6 | -7.9461 | -45.5108 | 2025-10-28 05:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 58631d89-4473-3fd8-a87f-12b386b97879 | -11.2798 | -45.5052 | 2025-10-28 05:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f1510748-0ef9-341b-af61-b3ceaad29425 | -10.5686 | -49.7803 | 2025-10-28 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| eb5a0cbf-a063-37a1-98a3-d69924fdda8d | -11.299 | -45.5025 | 2025-10-28 05:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| a9780c00-83a4-33a6-a52a-d5176dd536b4 | -3.58455 | -43.61348 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dde02f4-06b8-3db2-b94c-93fed11c4e84 | -1.56068 | -55.41559 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95fe655f-5164-3191-907b-adebe7be6d33 | -3.13705 | -52.99973 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48389b61-f5c1-306d-824c-f46d0bf9805a | -3.2355 | -45.94935 | 2025-10-28 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbf5d1b8-e368-3e14-9b8a-ab16b58c256f | 0.99345 | -51.10783 | 2025-10-28 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbbfc108-cd11-3ef2-a38a-eba0a6d7c9b5 | -4.18621 | -46.22799 | 2025-10-28 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90f209d3-e871-3d86-9958-c1125e79a2f0 | 1.04443 | -51.31225 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb54a5fb-8e39-3d3c-9d54-8e9fe40c4721 | -6.48566 | -42.22561 | 2025-10-28 05:01:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 09e8d59f-45b9-3111-ac36-984e0ec3f160 | -2.94518 | -51.0548 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40e4bf32-7c0f-3fe0-84ba-4d54b9c60eff | -4.63099 | -56.23887 | 2025-10-28 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ed65b86-4af8-3dae-adba-a350748f6ab9 | -1.83832 | -45.29708 | 2025-10-28 05:01:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6457ca-24d3-3a1e-b664-758ff50581f5 | -3.1217 | -51.20817 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d59f5d34-1aa7-3bc2-ad4e-593b52bd1b8f | -3.57142 | -43.61654 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4303da1-8346-3347-8184-83cfbdb39aec | -1.69032 | -55.66875 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14f8a0b8-2e1d-30f4-a5bf-c569d1023225 | -3.25162 | -52.91771 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a64d4a73-1a75-3b02-8ace-8f70448fe9eb | -1.6683 | -55.37904 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5389215-8162-3a01-abdd-2202fe7b722f | -3.43001 | -50.10387 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86284810-df4a-3a09-8dd4-19739fa762d5 | -3.42693 | -52.62679 | 2025-10-28 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 959aae1f-50fe-3e64-b68f-5bee09184e9a | -2.68148 | -57.67408 | 2025-10-28 05:01:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566de097-014d-3f45-845b-c2ab5c5d6f82 | -2.8298 | -49.40184 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4cabe483-fad5-3704-9ed3-f48b31f59dce | -4.37252 | -49.67165 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f8634ed-eafa-35ea-bd2a-0128c919388d | -3.48065 | -55.45861 | 2025-10-28 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 256bc815-0460-36c7-8995-1561b8e9d43a | -2.97649 | -51.34459 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ed82f58-6980-3637-8710-53d65147604e | -4.85032 | -50.67965 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81f3a5bc-a343-3a0b-a738-bedffc1ed977 | -3.70848 | -47.64344 | 2025-10-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 99400295-b8a5-3b1e-97af-ff7abf1d895c | -3.44055 | -50.22219 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 370d72d7-6f91-3d32-9977-e496ca114084 | -2.97718 | -51.34019 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 799c6370-bcf1-3eb6-a4aa-d5f9e81180b5 | 2.26623 | -55.98323 | 2025-10-28 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 035e3dc5-6f43-3ae2-8059-0e99163d4776 | -2.90223 | -53.13349 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb6fb140-e8d6-32ef-b647-1723bd1be6c2 | -2.9028 | -53.12984 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a63782f1-9de2-3435-a85a-6017432a8f26 | -4.20397 | -49.41153 | 2025-10-28 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00c131f4-4613-3f51-88b1-54a4aa494fe5 | -3.11357 | -51.21143 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1890070-122e-31c7-b81d-784a3707366d | -3.47073 | -49.97068 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33c3d136-7cef-3c78-b339-ea73a6a4d5bb | -4.44031 | -45.98194 | 2025-10-28 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38161804-65b0-3e64-a075-8a8134bcc1d2 | -3.2429 | -50.64975 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90a51a21-e9aa-36b9-a0a6-8bda4defe528 | -6.48645 | -42.23035 | 2025-10-28 05:01:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dc9350e2-69f7-3384-9468-ad1ccb422f58 | -3.27405 | -52.56859 | 2025-10-28 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8898667-c254-3dc7-8a3a-63aca06701d9 | -3.42933 | -54.5345 | 2025-10-28 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ef460e1-0c0c-32b0-9c0f-2295a6dc4d77 | 1.69271 | -55.65796 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2e41835-807b-38a8-97c1-da2af393137c | -4.359 | -48.64978 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 028467fe-15f6-37f1-9c63-f4ae1d4c5c4a | -6.16354 | -46.09365 | 2025-10-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c412230e-cd1d-3904-8f1c-10dfb9de018c | -3.1463 | -53.14082 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f78f1b4-0a79-3dd7-ac46-83b742e381fc | -1.80311 | -55.68579 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71aca8b9-73e5-304c-a22a-e9dab8b35e45 | 0.23674 | -51.15569 | 2025-10-28 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c85eefb-243f-3d77-94a3-c9c4dd4fcd1f | -3.57548 | -43.63198 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9c16089-8fdd-3e35-b5ff-bab56f4bef31 | -1.49785 | -53.12292 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67f7b6e3-585e-3405-9f5b-c84970a06d34 | -2.42045 | -48.43897 | 2025-10-28 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d2c067d8-ed82-3405-8dbe-a4cf097b8a84 | -1.61176 | -54.5094 | 2025-10-28 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d4a330d-22d8-3886-991f-6c21b9222f68 | -1.9626 | -52.03865 | 2025-10-28 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da0d4341-374b-3a83-8b93-754a5770f151 | -2.79354 | -54.86079 | 2025-10-28 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c5cc31e-9801-36c9-a538-c0b94a7707a4 | -6.69987 | -42.05422 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ac37cb2f-6eef-324b-bfb5-bb1c748d4e0c | -1.88675 | -48.39629 | 2025-10-28 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61a9a317-586a-3815-b509-d8961982f5d8 | -2.80437 | -49.14727 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5361ac1-b08b-3342-8e9b-2378676a7df3 | -4.43488 | -45.98141 | 2025-10-28 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8882d99-9b30-3d7c-9b8d-49aaa3ffe092 | -4.20706 | -48.35587 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7d72caf-9148-31f8-a506-3b4936778a19 | -3.75098 | -51.75302 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7f0e05e-4c96-393c-bd6a-ced1057138c3 | -3.12612 | -49.10559 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6971c98-90f2-306e-95a9-7820010ecfaf | -5.70218 | -49.19571 | 2025-10-28 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 716f9dc5-acb2-3015-a476-86741af9b947 | -2.43766 | -49.75661 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 469aec34-9df9-3044-9f0e-771dcde39d4a | -4.87365 | -47.54404 | 2025-10-28 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ba06b2f-5415-3614-97c5-29b440d05a5a | -4.45805 | -43.23268 | 2025-10-28 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 84c76682-f5ff-39c5-8853-f7d52fe90abc | -3.91432 | -43.32029 | 2025-10-28 05:01:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eb14445-e140-3406-b55a-4933b6679b25 | -3.69149 | -60.55534 | 2025-10-28 05:01:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78efb563-37bd-3b9e-aa3a-10fa60af12cd | -3.69947 | -49.56773 | 2025-10-28 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8afd23eb-66d0-38f6-a0cd-ccc64dcfea69 | -2.75913 | -45.40438 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 047472f4-df66-3879-a0cd-7a0e6fae6130 | -3.57261 | -49.44058 | 2025-10-28 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b105a626-428d-3cb7-abb2-9654cf1d1d61 | -5.78623 | -47.71775 | 2025-10-28 05:01:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0829b939-cfe5-388d-b37f-925a6b652163 | 1.04091 | -51.31281 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f087c72-75cd-33a5-8629-750cabf12bba | -3.47128 | -49.96711 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6d613f8-c6e5-3c00-8cb7-c29cf7662bad | -1.696 | -53.69529 | 2025-10-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349f6df1-f4a5-3cb7-9f72-9310fd918fde | -3.25176 | -50.04096 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b022cb59-c02f-38ae-9e61-26d2dc6d6b2b | -4.37669 | -49.67229 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baf7e747-33c7-37f5-87bc-5983b8723ccb | -2.98087 | -51.34073 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd08e3f8-cda7-3331-956a-3b6a8cbfb81d | -3.49971 | -50.05025 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 343f446d-f291-3190-b67f-f49a890724cc | -3.09976 | -54.6199 | 2025-10-28 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59ba5e0c-a7ba-3367-b30e-d2ebc93f82bd | -3.02894 | -45.37513 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8f47b4fd-ef3a-3326-ab0a-0423730f271a | -1.14067 | -48.09717 | 2025-10-28 05:01:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ba49436-4098-39a6-a451-2d52ba17ac12 | 1.59803 | -55.72519 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f54bcb-25b6-3410-95f2-b9b9cba24df2 | -5.84709 | -46.4515 | 2025-10-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ddce6a0-e954-36a0-8adf-08d9b01a32e5 | -2.91693 | -48.7229 | 2025-10-28 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f4925a1-b63e-3302-bbfb-bcf7aa24f30f | -4.68215 | -56.0678 | 2025-10-28 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13f1e866-c33f-3fb7-935a-dc5ce8aba2eb | -4.88466 | -45.74243 | 2025-10-28 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README71.md)
