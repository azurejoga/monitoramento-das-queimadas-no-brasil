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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6a7939b-4326-321e-99cb-a30950e3a912 | -1.64498 | -53.86971 | 2024-11-30 06:22:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 22ea3ffe-e4ce-3f53-9a85-0e5a99bb8274 | -3.10709 | -53.80887 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| c2023fb4-23e7-3eb4-b79e-ab26b1339782 | -1.83264 | -54.52812 | 2024-11-30 06:22:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| da44b392-7959-3804-9519-d1ff4087b265 | -1.27123 | -54.55662 | 2024-11-30 06:22:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 64a83c8a-c9b0-338c-87c0-a725cee029df | 1.19084 | -55.95418 | 2024-11-30 06:22:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 660bd3d9-03a3-37aa-ba94-7ecb81dd02de | -1.19703 | -53.86686 | 2024-11-30 06:22:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b660c363-273c-38d7-95b9-7847020126f8 | -1.50306 | -54.94793 | 2024-11-30 06:22:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 288ee2cc-19e1-3c9d-80cf-a16f13d47c26 | -1.07247 | -53.21139 | 2024-11-30 06:22:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| f246404f-fffa-3241-80fd-37ef393a902e | -1.25372 | -54.54701 | 2024-11-30 06:22:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 525051ec-0c8a-32a7-a5d3-75c3f73a4cdf | -3.14205 | -53.83887 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| f1458f0d-af63-32b7-b06e-b7fa200cd471 | -1.64767 | -53.8508 | 2024-11-30 06:22:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 65cb511c-edd0-3a20-9363-90c747c5fca8 | -3.48592 | -53.80915 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| f21dd51e-0ae9-3ccf-b7b6-42664118b139 | -3.60409 | -49.97042 | 2024-11-30 06:22:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 218ec7d2-1228-3d75-b1f0-dcc50f374105 | 1.18247 | -55.96751 | 2024-11-30 06:22:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3c0384c7-4d9a-3fe0-b869-12feb4061b3d | -3.25319 | -53.62404 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d005fdeb-7de5-3640-99d7-8a2d765ce1fc | -1.82777 | -54.51706 | 2024-11-30 06:22:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 2758baa6-7876-3973-a3ab-d21992b20f6e | -1.07547 | -53.63051 | 2024-11-30 06:22:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 7e9c47c8-e317-3112-9b07-f2ad9957946a | -1.33467 | -55.84914 | 2024-11-30 06:22:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fb62c4b5-1a69-34a5-9fbe-a25b62e43e8b | 0.93971 | -50.73787 | 2024-11-30 06:22:00 | AQUA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 25.6 |
| a59ae7ae-b766-3b61-af30-6dc1c877a0a0 | -9.74429 | -64.63848 | 2024-11-30 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ee00a08-e193-3891-8113-b0f223f65622 | -7.89311 | -63.26529 | 2024-11-30 06:22:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa0ba49e-7f09-3f97-a47a-adfb94def704 | -7.89956 | -63.26625 | 2024-11-30 06:22:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c322b073-5e48-322b-a42e-4eff9d0c6965 | -7.89378 | -63.25991 | 2024-11-30 06:22:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a98aef8-fb23-3798-9069-796004cbd89e | -9.66296 | -65.73963 | 2024-11-30 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f824a5aa-03b4-3323-a64e-8aef0b029f9d | -7.89278 | -63.26273 | 2024-11-30 06:22:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afcfee73-2cf2-3f34-bcb5-d0187f94d455 | -7.89923 | -63.26366 | 2024-11-30 06:22:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 711b83f8-e74a-3122-8691-68f42fc7a91d | -3.44235 | -59.28877 | 2024-11-30 06:24:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 409c4776-2b08-3433-84d6-6a0a69c78ba8 | -9.66176 | -65.73624 | 2024-11-30 06:24:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d0ba1616-3a95-35cc-b11d-ddbf8d67b5f7 | -3.79315 | -58.97153 | 2024-11-30 06:24:00 | AQUA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0b85ec9a-48eb-30b6-861a-7a4092b7653b | -3.43336 | -59.28747 | 2024-11-30 06:24:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 91bb31a2-dc10-3cea-8903-209b4b7fcbdf | -7.89481 | -63.2639 | 2024-11-30 06:24:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 20700890-069d-3b56-87fe-daaa90b32ee6 | -9.41333 | -63.23041 | 2024-11-30 06:24:00 | AQUA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b98ee6b4-4643-3e1a-8606-c1a6ffad2717 | -3.6061 | -49.9784 | 2024-11-30 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 34562a80-6277-3b02-8fe4-5c604168a14c | -1.6419 | -53.8731 | 2024-11-30 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5536eda3-3782-313c-b3e3-dd28899ea92b | -3.259 | -53.6388 | 2024-11-30 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 9eac9fec-3bb1-3847-8366-5b524d856126 | -3.2591 | -53.6186 | 2024-11-30 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| c47e7cc3-8628-3a79-9eaa-e51539167c92 | -3.259 | -53.6388 | 2024-11-30 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 4fd0b9d5-9104-3f2f-9db8-7a54bcebe893 | -4.4726 | -44.5524 | 2024-11-30 06:40:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 171.7 |
| ade722d0-1cb3-3c5a-af2e-c50872529312 | -1.6419 | -53.8731 | 2024-11-30 06:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 68e157da-1f73-36b6-b8cd-6cfe0ae8b84b | -3.2591 | -53.6186 | 2024-11-30 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e20ccbae-6200-3607-8c6c-6178082324ac | -3.2406 | -53.6393 | 2024-11-30 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c2f70793-d68e-3e08-8651-b0684ef6c9e8 | -6.9341 | -43.5634 | 2024-11-30 06:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 06559595-5584-3cff-9f08-4accda3c494c | -6.9344 | -43.5401 | 2024-11-30 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 191.2 |
| b5e5ffa8-141a-3d6a-9e21-1ae1c0f98096 | -3.2591 | -53.6186 | 2024-11-30 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 6c1af781-5ef4-36fc-917b-99044e5d5d68 | -1.6419 | -53.8731 | 2024-11-30 06:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 09062d16-ac07-3f19-aaf1-e175d0856f73 | -3.259 | -53.6388 | 2024-11-30 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 80c3060b-8bca-31b3-8dd8-5d956b67f26e | -6.9156 | -43.5418 | 2024-11-30 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 421.8 |
| 059a4838-ba24-3e30-9147-f250d251a6d8 | -4.4726 | -44.5524 | 2024-11-30 06:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 90c2ef4b-e5fe-3e8d-8bd4-a3ef379581ae | -6.9158 | -43.5185 | 2024-11-30 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 663162d8-0771-3d61-bbac-a0bf805964ba | -6.9153 | -43.5652 | 2024-11-30 06:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 183.4 |
| b37c0794-9dda-3a77-97af-98e805715e50 | -1.6419 | -53.8731 | 2024-11-30 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ec97588f-a16b-382a-8365-e206a4a2396f | -6.9156 | -43.5418 | 2024-11-30 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 496.9 |
| f56504b0-0068-307f-9529-a4804306b054 | -6.9344 | -43.5401 | 2024-11-30 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 1b672f50-8d12-340d-a99f-9640db36de5a | -6.9158 | -43.5185 | 2024-11-30 07:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e56989d7-5e10-3b52-9e86-9eb2a1fd1c49 | -6.9153 | -43.5652 | 2024-11-30 07:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 5963d35a-c2d1-3209-b762-c8d0a3ea0a2a | -6.9341 | -43.5634 | 2024-11-30 07:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ac71a94f-5a96-32d0-bb57-016c8904a7f0 | -3.2591 | -53.6186 | 2024-11-30 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 4f90a5d1-1796-3c63-b983-730cec34b651 | -3.3502 | -45.4223 | 2024-11-30 07:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2fba9a41-2404-3540-a192-0e16091cc07f | -3.259 | -53.6388 | 2024-11-30 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 9f9156f0-3273-3c4b-adfc-50ea1209fde7 | -6.9 | -43.56 | 2024-11-30 07:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0b61a6ae-89fd-3ebb-836f-9adc1c834058 | -6.93 | -43.56 | 2024-11-30 07:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d3f62601-a3cd-3f23-8d41-355bc70e059e | -6.92 | -43.52 | 2024-11-30 07:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9766bc54-c745-335a-a111-3a23f7aca4c3 | -6.9 | -43.51 | 2024-11-30 07:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a10558d0-1cfa-318d-9829-5bd3cc7f1a6d | -6.9341 | -43.5634 | 2024-11-30 07:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 7947e5bf-d018-371b-ae3b-0fbb9e718d35 | -3.2591 | -53.6186 | 2024-11-30 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 28e8cb3c-219f-33b7-8463-097b4e00a066 | -6.9153 | -43.5652 | 2024-11-30 07:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 3edcd952-9239-3c52-8fff-2774cbb6cece | -3.259 | -53.6388 | 2024-11-30 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e7bc6cd2-b71d-370d-b008-d764f91dacca | -3.3502 | -45.4223 | 2024-11-30 07:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 87fc7c15-9fb5-30f4-8d1e-555491370d68 | -6.9156 | -43.5418 | 2024-11-30 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 400.9 |
| d5a8a4ea-37be-30f5-9723-5c3a50e6f799 | -6.9158 | -43.5185 | 2024-11-30 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e0cf6fd3-bed4-3047-beb5-590615a066a7 | -6.9344 | -43.5401 | 2024-11-30 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 202.6 |
| a951e154-908e-3882-820f-a5326faebd45 | -1.6419 | -53.8731 | 2024-11-30 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| efc29f0b-df90-3aa8-becf-607016b30b38 | -6.9341 | -43.5634 | 2024-11-30 07:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 66bc1619-9f58-300f-8bbb-7ad63fde6b86 | -1.5868 | -53.8537 | 2024-11-30 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 337cf7db-a594-35a7-bcb5-d72888fff58f | -6.9344 | -43.5401 | 2024-11-30 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 170.6 |
| a707dfd4-77bf-38e9-a72a-49c6991cd302 | -6.9153 | -43.5652 | 2024-11-30 07:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 155.4 |
| b15661bf-15f8-39f0-902b-e8aae2e81360 | -3.2591 | -53.6186 | 2024-11-30 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 729925ba-a95a-3c3d-aa6a-faf0083704b6 | -6.9156 | -43.5418 | 2024-11-30 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 335.6 |
| 52d2cb4b-b871-3116-bc3f-95c3f64daa9f | -3.3502 | -45.4223 | 2024-11-30 07:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b89f56da-aaed-3181-aa2b-5c3ad8eb3529 | -1.6419 | -53.8731 | 2024-11-30 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3d3cf5fd-ad82-3d51-bf7c-76838bfd9730 | -3.259 | -53.6388 | 2024-11-30 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 0c64776c-0c48-3de5-8a1d-877f1818117d | -6.9158 | -43.5185 | 2024-11-30 07:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3bd336eb-524d-3809-85eb-006ae705fc9d | -3.2406 | -53.6393 | 2024-11-30 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 548563aa-4b7d-3579-a9b7-ded7f3bc5d9e | -2.57 | -45.3606 | 2024-11-30 07:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 5dd8bdbf-0e29-3e42-b00a-bac591bda28d | -3.2407 | -53.6191 | 2024-11-30 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ea4cddf7-e87d-32fa-b75a-0e51b8ceb346 | -1.5868 | -53.8537 | 2024-11-30 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 20dc80a3-d517-3298-b91f-5ba5149f4c34 | -1.6419 | -53.8731 | 2024-11-30 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| be4aead3-b466-3ef7-8cac-2de784c50d6f | -3.259 | -53.6388 | 2024-11-30 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 6d050ffd-8b87-301a-8931-948b6df273c4 | -3.2406 | -53.6393 | 2024-11-30 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 60927ac7-e9c8-327c-94b4-53c587172365 | -3.2591 | -53.6186 | 2024-11-30 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| c923cf1f-56ff-3b9b-b720-d3884f5443e2 | -2.57 | -45.3606 | 2024-11-30 07:40:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| c64db868-00ab-3533-8c44-c9126fc23b2b | -3.259 | -53.6388 | 2024-11-30 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 2ecbe907-ef68-3df1-ac4c-81832e5b32ca | -1.6419 | -53.8731 | 2024-11-30 07:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 05aa308d-3ce8-3155-820a-2fc6eacf8247 | -3.2591 | -53.6186 | 2024-11-30 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| db176da2-962d-3dfb-8a25-d741e254966e | -1.5868 | -53.8537 | 2024-11-30 07:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b057c4a5-e10a-311d-ae80-9ca740b01919 | -3.2407 | -53.6191 | 2024-11-30 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d98f796f-d81c-329c-be70-efb40a047931 | -3.2406 | -53.6393 | 2024-11-30 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c43dbf49-3ddd-3ddc-80ec-a1b8fb5ff484 | -2.57 | -45.3606 | 2024-11-30 07:50:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 199.4 |
| 1d4115ab-283e-3f27-aaa8-46d2ea1ed345 | -3.259 | -53.6388 | 2024-11-30 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 17f44947-1e80-33ef-8b45-66a5ea2a9d62 | -1.5685 | -53.8539 | 2024-11-30 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |


[Clique aqui para ver as próximas entradas](README134.md)
