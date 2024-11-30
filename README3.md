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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74ea4d36-8844-38c6-9fdf-b046da31e30a | -2.8303 | -45.307 | 2024-11-30 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d80bb369-b5c0-3d30-8feb-5a2645a28584 | -17.6457 | -57.5668 | 2024-11-30 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 87a01d0e-c2bb-32d9-9a50-c83d5bfa089a | -4.8523 | -41.317 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 1d254baa-3daa-34e8-ae65-5a2c22ab023f | -1.2556 | -54.5589 | 2024-11-30 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| b0231cfa-6575-3dd2-afa6-527c2ee36ffb | -3.9697 | -41.5416 | 2024-11-30 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 58.9 |
| d3aa2508-6089-344c-8879-e83bd6c47634 | -4.6652 | -46.364 | 2024-11-30 00:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 9c366bf6-ac6d-3e7d-afe1-4324cfb22d06 | -7.1959 | -37.5144 | 2024-11-30 00:30:00 | GOES-16 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 25fc3dca-e827-395e-a935-f5e48b9ad602 | -4.8903 | -41.266 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 43cf75d5-2514-3a4e-a087-db89bcc861a1 | -3.9886 | -41.5165 | 2024-11-30 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 212.5 |
| 73017301-dc47-3f76-bcf5-360bd084d3cb | -4.6237 | -47.0069 | 2024-11-30 00:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 20c43505-883c-3fdb-8ee0-05af1765ee19 | -2.5963 | -53.9771 | 2024-11-30 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f950d16a-d32f-3404-ab4d-67c46c265426 | -3.4791 | -53.8142 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 369e1abb-8995-3494-9919-c7d33e06c0df | -4.8713 | -41.2915 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 548.9 |
| c9aba749-aa2e-3f20-9976-15ee7af7b2c1 | -3.4975 | -53.8137 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 28d19a91-b03b-3f15-9398-011769fca281 | 1.1805 | -55.9671 | 2024-11-30 00:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7e962c20-3478-3539-a24c-e5979f4b1e27 | -1.2556 | -54.5389 | 2024-11-30 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9c3edf00-1f24-318f-b8a1-4a312e48f97f | -1.0733 | -53.6378 | 2024-11-30 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b3826ca9-d038-3d77-b4ed-9dc2497b655f | -2.8304 | -45.2845 | 2024-11-30 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d1a6f2ca-2a24-3f65-b055-e45004e3e7ae | -3.97 | -41.4935 | 2024-11-30 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 3dfbe5aa-11b4-3787-8d9e-d7ed3b26dea4 | -1.6419 | -53.8731 | 2024-11-30 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a4a94920-f43f-3e50-9446-44628da5f894 | -4.8715 | -41.2674 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| fcec8dab-0752-34fe-84d0-70372fee1f46 | -17.6651 | -57.585 | 2024-11-30 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| deb8c29f-e47d-3ea1-988b-7246c8b3fc81 | -3.6061 | -49.9784 | 2024-11-30 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 43751879-cb68-34f5-9e2d-d1616c0e3f07 | -4.8901 | -41.2902 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 245.5 |
| b431dc2b-0c52-32a7-8528-15e00c528c69 | -1.2739 | -54.5387 | 2024-11-30 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| afdfdff1-3c58-3535-8bd6-3a268d311db6 | -1.6753 | -46.7836 | 2024-11-30 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 35cd8e4a-b2a1-397d-abd6-50a3cee43de3 | -6.9156 | -43.5418 | 2024-11-30 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 48f47776-1e34-33f1-a7d9-7f3acb9ca4cd | -4.6051 | -47.0079 | 2024-11-30 00:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 360.9 |
| 32668960-1cf9-3365-9cfb-e4503a763420 | -1.4379 | -55.2335 | 2024-11-30 00:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a8159976-f32e-3809-84c0-eaa44d73441d | -3.4792 | -53.7941 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 85c43f11-8264-356e-be72-5a93d974a87a | -3.9699 | -41.5176 | 2024-11-30 00:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 191.0 |
| bb6dc34c-97e6-324e-becc-dce14cce6584 | -3.259 | -53.6388 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 157.5 |
| e3eb4c97-11be-34fe-8a28-7df301400d2b | -6.0862 | -48.0339 | 2024-11-30 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 8b33784b-976f-3a6e-a3ce-1e077ba7680a | -17.6654 | -57.5645 | 2024-11-30 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.2 |
| 3cbc00e8-ffc6-3ba5-b0b9-34886f95cdab | -1.4379 | -55.2533 | 2024-11-30 00:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 801d93ec-7830-300f-9f48-58bc4ad61870 | -1.6938 | -46.7833 | 2024-11-30 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 81f9d0e5-8730-3033-8b23-b844b39f2f3a | -1.3271 | -55.8475 | 2024-11-30 00:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2636b76a-041a-389a-8f5d-7d4c33a63b77 | -3.1481 | -53.8233 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 125f0f03-9d30-30eb-a1c6-74f4284ee40b | -3.3998 | -50.6573 | 2024-11-30 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0fccffa0-56b4-3b41-b62a-b4d94392e3b1 | -4.8711 | -41.3157 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 211.2 |
| 2151de24-23c9-3569-a6ce-97802df40b43 | -3.4183 | -50.6567 | 2024-11-30 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 4105d865-69a8-3ef7-ba9d-63e4d8e13f4f | -6.086 | -48.0557 | 2024-11-30 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 22b76d50-5fe1-39e8-afac-e845c1415d39 | -2.614 | -54.2177 | 2024-11-30 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 56e0ec94-a139-35bc-a967-536b00b2e187 | -3.3668 | -49.7545 | 2024-11-30 00:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f7d68860-28f1-3ebc-92f9-82c276bb6857 | -4.6052 | -46.9859 | 2024-11-30 00:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| d223eb2b-90a3-3ea3-9b92-727b77333931 | -1.3333 | -51.6788 | 2024-11-30 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 9bea7850-e60e-3e9d-b46b-f54df1654e72 | -4.6838 | -46.363 | 2024-11-30 00:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| a84a6f0f-5a29-3343-9634-f79b0308fc37 | -1.6777 | -45.7868 | 2024-11-30 00:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7b4bf581-a5d3-3d21-a7b1-cd357ead705b | -4.8527 | -41.2687 | 2024-11-30 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| df00f209-0175-39e0-baea-a8a7f6d8ec9a | -3.4976 | -53.7935 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 474cafcc-e5d1-3d19-86aa-cc465a0f6f05 | -3.2406 | -53.6393 | 2024-11-30 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 5248a6d7-0a1c-33dc-9934-ef02965e3ab9 | -3.4976 | -53.7935 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| bba0930f-b72e-39ab-be66-d5adf9ee2baa | -1.2739 | -54.5387 | 2024-11-30 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 48a54bc1-3abc-32d8-b9db-f23c485fc988 | -3.2591 | -53.6186 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2467484a-29bf-3423-9372-66fcc433e53b | -3.1481 | -53.8233 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3b200034-b557-3153-a3b6-f67c51859985 | -3.9697 | -41.5416 | 2024-11-30 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 8fd2818e-77d0-3ecd-ad77-7d6c547c2f2d | -3.4791 | -53.8142 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 198.0 |
| d3f185a8-6562-338d-98b1-e23d7fcf0ac6 | -9.8552 | -36.1924 | 2024-11-30 00:40:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 3d543833-aba3-3c12-91c3-7e60c1945dbe | -3.7021 | -45.6764 | 2024-11-30 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 890aef36-83b4-3d5b-b22d-1261072bdefe | -1.0022 | -51.7235 | 2024-11-30 00:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 429cd7a2-d717-3a84-b332-36fbfdb543ce | -4.8715 | -41.2674 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 316.5 |
| 3ae4e4b2-44d6-32fa-b648-dc2c343a2196 | -4.8713 | -41.2915 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1624.0 |
| 85de83e0-1a5f-3997-8241-ff31bf1349f1 | -4.8901 | -41.2902 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 548.0 |
| 4d178ca9-c516-321f-84ce-c399398b0f48 | -4.6238 | -46.9849 | 2024-11-30 00:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 3d3f0a74-e8b0-3e7f-9daf-ef7c6669db2a | -6.8967 | -43.5436 | 2024-11-30 00:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| efa1f7de-66f0-3c13-9287-ceba6c491299 | -3.4792 | -53.7941 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 3800439a-34af-3b95-ac66-2b682a1760a7 | -1.6777 | -45.7868 | 2024-11-30 00:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| df736ec6-3165-3980-8c0b-5913692a57ed | -4.8527 | -41.2687 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| c3f97dae-130c-384c-b7e7-3671de722906 | -1.3271 | -55.8475 | 2024-11-30 00:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 78909f29-2e3c-35da-be10-2a15558eeac9 | -4.6051 | -47.0079 | 2024-11-30 00:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 238.8 |
| 05f1e8c9-ff29-317d-bc71-614586540ebb | -6.9156 | -43.5418 | 2024-11-30 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 341.7 |
| 94a5051d-a8ae-37d7-977e-3eba951bd97f | -4.6052 | -46.9859 | 2024-11-30 00:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 3c1b648a-2e0f-3b31-83b3-f3768b6ac89a | -4.8899 | -41.3143 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 283.4 |
| 83f438fd-5648-356d-ae58-366ba774ed49 | -2.5963 | -53.9771 | 2024-11-30 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| eca9c42b-1174-3a5a-acb0-9b4ae1e2977c | -17.6654 | -57.5645 | 2024-11-30 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 59372026-b124-3650-843b-ab9d306d29f5 | -4.8523 | -41.317 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 173.9 |
| 31f31ea4-58c4-37e0-9f63-69fba8e851e9 | -3.9888 | -41.4925 | 2024-11-30 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 792c65f6-0595-39fb-ad6c-bb29824c88c8 | -4.8711 | -41.3157 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 849.1 |
| efa9a1db-be19-3f7b-99a4-4aaaedb56d09 | -4.6838 | -46.363 | 2024-11-30 00:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| b2423fe8-8e70-3f6a-8428-802583ae9745 | -3.9886 | -41.5165 | 2024-11-30 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 162.4 |
| 9e6b5f06-6a63-3783-91ae-0c238322f3fd | -6.0862 | -48.0339 | 2024-11-30 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d1203e8f-d32d-3826-904c-77ef6cba66f6 | -2.5216 | -48.4591 | 2024-11-30 00:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 42564026-a8a2-344f-bf83-780ba0d47c25 | -6.9153 | -43.5652 | 2024-11-30 00:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 8afdc124-cba3-3018-936a-26a1287ecf86 | -6.086 | -48.0557 | 2024-11-30 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 2409adee-3799-3aa1-a3bd-bf21ee9e34ac | -1.2739 | -54.5587 | 2024-11-30 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 89645ae3-a6f8-3839-85f9-63ce04b84287 | -4.8903 | -41.266 | 2024-11-30 00:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| a088b77e-f0a6-3036-8865-9b10cd66ee19 | -9.8557 | -36.1653 | 2024-11-30 00:40:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| b89a9054-a59d-3220-a254-739cf4eb05c4 | -3.97 | -41.4935 | 2024-11-30 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 69a47486-1d29-33c2-8998-9442c3ccef82 | -1.4379 | -55.2533 | 2024-11-30 00:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 71a0090f-3e89-3f23-9e24-1c54370ee3fd | -3.148 | -53.8434 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| cdef9d3f-f659-3bf6-af8b-b51c73837e48 | -3.3668 | -49.7545 | 2024-11-30 00:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| cb6dcc3e-b377-3eee-96fa-b485ac6f3763 | -2.614 | -54.2177 | 2024-11-30 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7bfad5ff-eeea-368f-a83e-7d6ebc746f06 | -17.6651 | -57.585 | 2024-11-30 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| d6b50ad0-f26d-3b00-b92f-8c9d2b56b506 | -1.6419 | -53.8731 | 2024-11-30 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 5e43ad7c-bcc9-3bf5-871d-fb1800b8e878 | -1.2556 | -54.5389 | 2024-11-30 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 2e7ef624-e292-3e53-ba30-aaa04bbd77be | -7.1959 | -37.5144 | 2024-11-30 00:40:00 | GOES-16 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 72f265fc-6599-3f23-9a6e-e3b297beb37e | -3.2406 | -53.6393 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f3f3ad2d-0586-3ae3-8347-23bd07fbf4e8 | -3.259 | -53.6388 | 2024-11-30 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 09d08e17-489f-313b-90de-58bb8574fc4c | -3.3998 | -50.6573 | 2024-11-30 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 53f3e6ab-2b3b-3332-a2a1-0bc0d3de807e | -9.8364 | -36.1687 | 2024-11-30 00:40:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 105.1 |


[Clique aqui para ver as próximas entradas](README4.md)
