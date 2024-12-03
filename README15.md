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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c78b42a1-16f5-3cf9-a9dd-419997f0fa3a | -1.824 | -46.5824 | 2024-12-03 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 56efc2a3-9fc9-33e1-9481-b12c1086a9b2 | -3.3422 | -51.2007 | 2024-12-03 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2dc1448b-3f5d-3824-ae17-7abba4944b84 | -2.8013 | -53.043 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 241f3456-2e30-3d5c-8d8f-4667694c4aa9 | -5.8009 | -46.4941 | 2024-12-03 01:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 2da808d1-2491-3ccc-9008-df519ed7fbe6 | -3.5681 | -50.1903 | 2024-12-03 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4a984849-a406-35c2-93a9-f6d08744e0e2 | -3.0949 | -53.2385 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c5ab8a73-c355-3156-9ecf-8dc9f20d1267 | -2.8396 | -52.5941 | 2024-12-03 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1c35e128-4cab-38b3-972b-99ebfa21ffb8 | -3.5682 | -50.1693 | 2024-12-03 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f28f19ea-a07d-396a-bbf7-d4516821986c | -2.8196 | -53.0629 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5c19dbb0-8c81-3101-a09e-299aff5e64c3 | -3.2905 | -50.3257 | 2024-12-03 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f74b811a-778a-3557-ac9b-b58d1a22f219 | -3.2406 | -53.6595 | 2024-12-03 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 633fdda0-4994-3d28-bbbb-abba13f7aac9 | -2.8197 | -53.0425 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0f79b9a8-faf5-31b4-8bf6-72c54e424404 | -3.259 | -53.6388 | 2024-12-03 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e64dc195-ed5d-3772-a3f9-93102910aaa3 | -4.5589 | -42.9289 | 2024-12-03 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4bab16a9-8d1d-363e-bee8-e272ec32475b | -1.8052 | -46.671 | 2024-12-03 01:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| ca4f6b69-ecef-3378-8d3e-20eb5421c6fb | -1.7541 | -52.7993 | 2024-12-03 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 8a2cde35-9599-3186-82ed-5efb9b7cefe8 | -3.1019 | -53.227501 | 2024-12-03 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edd445fc-93ab-3f3b-8376-74467b938a8b | -1.5235 | -60.322399 | 2024-12-03 01:36:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92fc2f78-afe7-3993-a11d-e529b85a8264 | -3.0222 | -53.869499 | 2024-12-03 01:36:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb077638-069f-358a-ba62-b4ccdc813495 | -9.363 | -57.554798 | 2024-12-03 01:36:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c35a6e2-ea03-3156-9b71-2fb0e4563c3d | -3.0811 | -53.3526 | 2024-12-03 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47fb209e-b128-3735-ab48-42e72ef35d3c | -5.4314 | -60.183601 | 2024-12-03 01:36:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae37726-0ed6-3012-9ba2-abf89f242ebe | -3.0866 | -53.375099 | 2024-12-03 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e735e5b4-9d87-38bb-bda7-857fa233e50e | 2.7319 | -60.3964 | 2024-12-03 01:36:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e5211f22-73f6-393f-8891-fae5c6193aea | -3.0823 | -53.399799 | 2024-12-03 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd49057-fb44-3445-9718-7a14e6c86203 | 3.1347 | -60.297401 | 2024-12-03 01:36:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f4e4f489-c568-3d93-9e18-9d8244ca3660 | -3.0714 | -53.3549 | 2024-12-03 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 683cf865-aa50-3155-aada-ce5660d482e4 | -1.7482 | -52.7756 | 2024-12-03 01:36:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 761c2842-8705-3f12-bbdd-3e618d3f9dcd | -10.0565 | -59.122002 | 2024-12-03 01:36:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47027852-77af-3a50-9b03-34447306cb59 | -3.0769 | -53.377399 | 2024-12-03 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3b3ce2-d43a-3a5f-8cd3-45d64bda255f | -9.3728 | -57.552399 | 2024-12-03 01:36:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e44fa6d-5a1b-39f7-a6c7-5aa24c1a9cc6 | -3.2574 | -53.657799 | 2024-12-03 01:36:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afd72db5-fe32-3e3f-8d41-9e07a9705c6f | -5.4296 | -60.1759 | 2024-12-03 01:36:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69a4c555-51ad-3234-821b-ca7e827476aa | -3.1765 | -54.3386 | 2024-12-03 01:36:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60d4922d-82b8-3f65-861f-fc186f7a591d | 3.1369 | -60.287899 | 2024-12-03 01:36:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 281ca009-2650-3fe3-9c28-5706ef7e3079 | -2.8207 | -52.575298 | 2024-12-03 01:36:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91cc0c12-844a-3e7e-8d75-65829d887e50 | -9.0322 | -63.522598 | 2024-12-03 01:36:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 53937f23-69b3-3511-9148-4ce1640ed2f4 | -10.0546 | -59.114201 | 2024-12-03 01:36:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 300f45b4-e72a-3881-ab09-4cb6aaeb715e | -2.2013 | -53.771801 | 2024-12-03 01:36:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 256bd742-41ad-311c-ac7e-4eeed0c40f6e | -2.8304 | -52.573002 | 2024-12-03 01:36:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 969b05ad-f07d-3b6c-b4c8-0f991ec75c15 | -3.1862 | -54.3363 | 2024-12-03 01:36:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb819f4-c296-3fa8-82f4-84b0a0fdb050 | -3.2478 | -53.660099 | 2024-12-03 01:36:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2110f9d0-4263-3fb7-a6a4-7752b421b58c | -1.0681 | -62.640701 | 2024-12-03 01:36:00 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f16a6d7b-3c75-377a-85aa-70d6d01abd05 | 4.1033 | -61.199799 | 2024-12-03 01:36:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8be9d878-c7c8-3f0c-97a7-fe86c248f371 | -3.092 | -53.397499 | 2024-12-03 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bce64a22-3b6a-3156-bcaa-c0c943680b9f | -9.6654 | -62.442799 | 2024-12-03 01:36:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e87ab106-b6b1-30a3-a8a9-58acbd32ff4e | -10.457 | -58.674301 | 2024-12-03 01:36:00 | METOP-C | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5daf6823-06f9-344c-a913-0b6f49bc5fc8 | -2.827 | -52.601002 | 2024-12-03 01:36:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 835d4d0a-d9aa-315a-a5eb-f8c16ee19d43 | 2.7341 | -60.3871 | 2024-12-03 01:36:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 37e49187-eae2-3e7b-95c8-714fd83b7b2b | 2.7362 | -60.377701 | 2024-12-03 01:36:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 408e5a19-c693-3f88-b269-f59b1cf99e21 | -9.6638 | -62.435799 | 2024-12-03 01:36:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c312dc7-e79c-39f7-9905-62cdf061cdf8 | -3.0319 | -53.867199 | 2024-12-03 01:36:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0402e50a-2a43-375a-aefb-88d275bc9e5a | -1.7544 | -52.801498 | 2024-12-03 01:36:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4abe309-571d-3aaa-bf65-c363f6befdf6 | -3.1133 | -53.2381 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f85dad7c-9e9c-35d8-85c8-c11678571e46 | -3.259 | -53.6388 | 2024-12-03 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 57bb6c4b-ef0c-3605-9a17-4b709314eff5 | -3.076 | -53.3808 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 9adb1bf3-859f-3757-9c11-2658edf3e008 | -6.1229 | -43.9578 | 2024-12-03 01:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c9aea71d-ac2f-3561-8c24-6f08f8f0bf80 | -4.5589 | -42.9289 | 2024-12-03 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 50a9dc54-fbb4-3580-a41e-4580740b9226 | -2.8013 | -53.043 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7771e103-622d-3390-b36e-f653629fd963 | -2.8196 | -53.0629 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c98833da-3763-34a0-b727-4ecfcfd2d7e0 | -1.7541 | -52.7993 | 2024-12-03 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 5cc12777-44ae-3d37-af5a-ebd92c2df761 | -3.2406 | -53.6595 | 2024-12-03 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5730d1e6-edaa-3b8a-b350-5f56f6e12798 | -1.7867 | -46.6714 | 2024-12-03 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| e77d2bca-32f2-300a-b158-6fcae29c8c1a | -1.7361 | -52.6366 | 2024-12-03 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a1919bb2-3359-3ff1-b1af-014f0be76423 | -2.7378 | -45.1976 | 2024-12-03 01:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 55a7f795-24c5-3d9b-93e0-6abc49181599 | -1.7868 | -46.6494 | 2024-12-03 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 9838434f-84b0-30b6-997a-3390604c629f | -3.0944 | -53.3804 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 3a8ea7e5-c037-3599-8adc-65d2d25406c8 | -5.8009 | -46.4941 | 2024-12-03 01:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d1ea2fb9-689e-3e33-b46c-d93adcda78be | -3.1831 | -54.3247 | 2024-12-03 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5b0d47ab-184f-3be8-b954-64a59c4be5b1 | -2.8012 | -53.0633 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 64292ac8-84c8-38d4-8a89-360b75606d3e | -3.1948 | -51.1637 | 2024-12-03 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 0903db0f-3848-30ab-b99c-f47fa3facec3 | -5.801 | -46.4719 | 2024-12-03 01:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| ef559112-1599-3d0d-8dea-93b7c8b077d6 | -2.8212 | -52.5945 | 2024-12-03 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 490f20aa-3860-34ea-a83f-45c5df5463de | -3.259 | -53.659 | 2024-12-03 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ebb0a98e-904d-360c-b145-d03f814a19f1 | -1.8052 | -46.671 | 2024-12-03 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| c56806ee-3e85-34d5-9fca-4901676822c2 | -3.5682 | -50.1693 | 2024-12-03 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 33a61f0d-8891-3902-b454-bd9de4301d5c | -3.0945 | -53.3601 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fc315cd9-725e-3d09-9450-05a73c1f7d2d | -3.183 | -54.3448 | 2024-12-03 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 291c8191-d811-379f-bb0a-24c4ddfd94ea | -2.7377 | -45.2201 | 2024-12-03 01:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 057636f9-2932-3612-8852-6afd9eb368b0 | -2.2111 | -53.7835 | 2024-12-03 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| eee41df2-50bc-3fe2-b2be-54a23f37b69d | 2.7267 | -60.3916 | 2024-12-03 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e019e780-f2c1-3b10-83d4-5e13e25579b4 | -3.5496 | -50.191 | 2024-12-03 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| b52f62d5-af62-3dd0-9e7a-645bde6a7a09 | -3.5497 | -50.1699 | 2024-12-03 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| ffda0631-7ec6-31e4-85f0-b19a27d832df | -3.0376 | -53.8664 | 2024-12-03 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e8d75df4-574f-3b24-8f92-937c738ff0ee | -3.5681 | -50.1903 | 2024-12-03 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a4ea1912-2fa4-3e89-8af1-60d2f5bcb91d | -1.7541 | -52.7789 | 2024-12-03 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| bfe10673-3b40-3cef-bf86-5fe3f979a0be | -1.8053 | -46.649 | 2024-12-03 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 839c0b98-002f-3ff2-9de6-74798dbe3fe7 | -3.0761 | -53.3606 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b6d6ef40-bacb-382d-984d-d095b946df93 | -3.0192 | -53.8668 | 2024-12-03 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 21400a3a-6572-3ac0-a502-ee57b0f4323a | -5.8197 | -46.4706 | 2024-12-03 01:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 52cb2717-a5a9-3597-9a51-39a676dad5d9 | -2.8212 | -52.5741 | 2024-12-03 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 9b3ffe39-c6dd-3402-ab49-ff303ef1b840 | -2.8396 | -52.5736 | 2024-12-03 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a1f50af9-b532-3588-8881-968cf8861870 | -9.374 | -57.5553 | 2024-12-03 01:40:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 764d046c-b999-3b08-a417-7cf0a9c7265a | -2.8197 | -53.0425 | 2024-12-03 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b14a056b-fc2f-390c-b1ee-eaedebfa01e7 | -3.1948 | -51.1637 | 2024-12-03 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| be4f5a84-4b71-36ec-a710-b484148d562f | -3.259 | -53.6388 | 2024-12-03 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5b158d9a-188c-3787-8c31-844979f68498 | 1.1072 | -55.9874 | 2024-12-03 01:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 37449669-77f3-38f1-853e-577a3354d881 | -1.8053 | -46.649 | 2024-12-03 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| eff96a0c-1d99-3cac-9eb2-8020e1a98816 | -6.9908 | -43.5349 | 2024-12-03 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ff7b2265-7c26-302b-be9c-dfd8ca30cf12 | -3.076 | -53.3808 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 158.0 |


[Clique aqui para ver as próximas entradas](README16.md)
