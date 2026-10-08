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

## Dados Diários - Página 202

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3edf21df-e5ee-37e9-9351-cab683fc7e59 | -9.07543 | -65.48099 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44424b8c-7180-368d-b661-1b567d27e546 | -9.20114 | -66.09163 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be0212ff-6a81-37de-a9a8-b23812ab29ba | -8.60354 | -67.30739 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b82120e-23da-3b15-9d73-f9b7445101e3 | -7.44353 | -63.54246 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d6ca67c-b45f-3b43-8267-a7c0a42f2daf | -9.48461 | -64.36326 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16cac07f-66f5-3eb5-94a4-fd3b97ec9e5b | -9.13877 | -65.29919 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cdd2f93-4f0f-3791-8436-8353b752779c | -9.44251 | -65.43912 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6dfb281-fc41-32fe-9b4c-821f565377b5 | -9.47908 | -64.35523 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14435ae2-f89e-3c9b-9eb7-2db477c63430 | -8.61715 | -67.02477 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0deb4b76-083b-34dd-aa2f-43cec6aee60c | -9.68892 | -58.10729 | 2026-10-08 05:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5254eee-8912-3b5e-b3c1-88801d7bb784 | -9.05232 | -65.93272 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa998b10-1d9b-3b2e-b9f6-87a39efc6f63 | -8.5484 | -67.02543 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24bf7f5e-f6c9-38e0-9483-6b1b1c248062 | -9.47522 | -64.35818 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52ec97a9-794c-399d-ba1f-f773567f810d | -8.62769 | -67.02654 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 7cd4bc40-d6d4-3b86-b619-24c7f5684b14 | -9.34689 | -65.45982 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aace02d6-2b36-3db2-a162-1ec392c9231a | -9.08683 | -61.13587 | 2026-10-08 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d9c1596-0911-37fb-a5a9-aa743ca5d71a | -11.75209 | -61.06544 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4fb3b98-1d84-3fe1-9793-bad43e7facb0 | -8.62105 | -67.00105 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2faa56c8-b719-3c9a-add6-b62788be5488 | -9.22886 | -67.52985 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e88aecf4-0e7f-391d-91e5-76df18ed8776 | -8.6107 | -67.0116 | 2026-10-08 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| dcb3b28d-b343-353e-b84d-29b151e2af39 | -8.6291 | -67.0296 | 2026-10-08 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| cbc0c13b-36b7-369d-ae5a-189a4ed527ec | -8.6107 | -67.0301 | 2026-10-08 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 52506413-72bb-39e1-9727-742a3272a27c | -8.6292 | -67.0111 | 2026-10-08 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 97814971-4e0f-3e0a-bc4d-8e741c130252 | -5.73736 | -45.14699 | 2026-10-08 06:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ae955343-216c-3171-98f9-bf1ca28d5f4a | -6.32247 | -43.34716 | 2026-10-08 06:18:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| daf7e586-19d7-39b0-b710-f155e15bd146 | -6.88156 | -43.7016 | 2026-10-08 06:18:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 96dc3837-7b28-3f75-b2c8-90e2e602ab45 | -6.30417 | -43.33218 | 2026-10-08 06:18:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a400eb85-a85e-3adc-8858-8fe438d01137 | -6.9302 | -43.65925 | 2026-10-08 06:18:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| ed8af987-e8e2-3ca0-9b29-6b8e1b4d05e7 | -5.76136 | -42.07333 | 2026-10-08 06:18:00 | AQUA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a0c21eaa-2913-39ef-a247-925e06b54368 | -5.76293 | -42.06324 | 2026-10-08 06:18:00 | AQUA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| b156668b-48ad-3692-9b26-395eed59e4bb | -6.15707 | -39.43039 | 2026-10-08 06:18:00 | AQUA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3cf9e74a-1779-358d-bea5-77bbba256abc | -4.34955 | -43.79902 | 2026-10-08 06:18:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| ffcbed15-5842-38f0-8fe0-3838a6ff959e | -6.15575 | -39.43918 | 2026-10-08 06:18:00 | AQUA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2bd2fcc6-f67b-3796-9a92-a785b2721197 | -7.07405 | -40.93761 | 2026-10-08 06:18:00 | AQUA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 13085b90-7f9a-3327-b471-f47e25e40a54 | -5.72564 | -45.14517 | 2026-10-08 06:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 6424702c-0b54-3a04-b5ad-6b85c5cede95 | -5.73591 | -41.75851 | 2026-10-08 06:18:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| bfe8ac11-f7bc-3b4f-9a35-d68af6f43f46 | -5.72669 | -41.75707 | 2026-10-08 06:18:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4665707f-650c-32a7-b3ef-01b96b9f051a | -5.73473 | -45.16339 | 2026-10-08 06:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c8a5f9fc-5274-3ec3-99ed-5632c15d6c67 | -4.35175 | -43.78518 | 2026-10-08 06:18:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 46e35161-6da1-39d3-89e2-ed558575412c | -6.31239 | -43.34554 | 2026-10-08 06:18:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c2e2b3e4-b530-3f13-abde-c9b2109e00f4 | -5.48612 | -42.8474 | 2026-10-08 06:18:00 | AQUA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f5158f41-91bf-3949-a60e-388a11227366 | -6.30231 | -43.34397 | 2026-10-08 06:18:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4e54644e-7c36-3522-b71f-3a2493f45a0d | -6.88353 | -43.68924 | 2026-10-08 06:18:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 8e55bc0c-69b8-3a62-8346-62b3598c6967 | -6.63197 | -43.73135 | 2026-10-08 06:18:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| f8f0a1c6-dae5-3bd3-8570-b5c9b230a22b | -5.96731 | -40.91617 | 2026-10-08 06:18:00 | AQUA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9e040987-884e-32f9-9845-6be8b5f844d4 | -5.75355 | -42.06185 | 2026-10-08 06:18:00 | AQUA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 6e7821ce-3f5a-3c80-9a18-180e1b9428ee | -5.72519 | -41.76682 | 2026-10-08 06:18:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| dd976386-e628-3cab-b190-7cff3e3999d3 | -8.6292 | -67.0111 | 2026-10-08 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9c2b46dd-f679-3301-83ea-c334c2e495e8 | -8.6107 | -67.0301 | 2026-10-08 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 72628b96-3e87-34fb-ac6c-95b79ecf4c52 | -8.6107 | -67.0116 | 2026-10-08 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6591a369-81ea-3ec5-bb58-69158096c3f5 | -8.6291 | -67.0296 | 2026-10-08 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 2ae19d31-96e7-3d90-bd15-ae9d30b4b2d1 | -8.21095 | -46.31764 | 2026-10-08 06:20:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 7b294c11-ff3d-30a8-8546-79cdc0c56a07 | -8.72191 | -45.17779 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| a7975133-1cf2-3fa0-8123-fc7ecd38e062 | -6.9491 | -45.27837 | 2026-10-08 06:20:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 49d2cfcd-dc9b-30b8-a03c-bd6f6e7a0e48 | -8.73772 | -45.15023 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 17477ac0-798f-3e68-8953-8c6610771e56 | -7.63902 | -44.37505 | 2026-10-08 06:20:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fcf2bb36-f1ab-3f44-bdb7-0d4857dbba18 | -8.71953 | -45.19263 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 11a661b1-46f9-3131-b611-aaf05e23215b | -7.4695 | -42.85446 | 2026-10-08 06:20:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e710628e-a37a-31bc-af5c-63bae16a4284 | -8.723 | -45.18374 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| c3643a42-a25b-3c84-bb05-32830d45666d | -8.3855 | -46.303 | 2026-10-08 06:20:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 6c9c055a-9642-3ed6-a4a8-73a7bfc5ba82 | -8.72795 | -45.15431 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 47bad5c1-77d7-3a58-9863-f07efbbccb2a | -6.94217 | -45.27001 | 2026-10-08 06:20:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e090fbbc-e735-3d90-8e94-8b01484068ce | -8.22028 | -46.33754 | 2026-10-08 06:20:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 8744cd46-6813-3292-9799-49e5e6994c0e | -8.20801 | -46.33524 | 2026-10-08 06:20:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5c6fa249-07fe-3a8f-a255-1c8521f5483a | -8.72548 | -45.16901 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e47f37f6-853d-3c96-b7b2-9803df03a917 | -8.72665 | -45.14834 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2ad32d9c-cbde-3bb5-8b9a-5d0df8aa98a4 | -8.72428 | -45.16305 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 9e28cac4-3e86-302b-89b8-6788821892cb | -7.4712 | -42.84379 | 2026-10-08 06:20:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f7f04c89-5a46-3213-a0f5-366bef577012 | -7.602 | -42.37864 | 2026-10-08 06:20:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 71600fc0-e233-3144-b135-c2ecb2d2d676 | -9.9015 | -44.80531 | 2026-10-08 06:20:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 12143886-7df7-3592-9894-25e35a8c415c | -8.73902 | -45.15621 | 2026-10-08 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e06f22a9-6d53-35dd-96d6-3889efec69e6 | -9.89862 | -44.79696 | 2026-10-08 06:20:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 98ef57c5-cbe3-36b2-a71e-02af39a7db88 | -9.8964 | -44.81018 | 2026-10-08 06:20:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e24a4e13-a6b1-397d-8c54-dd86cd9a90dd | -10.42324 | -47.27315 | 2026-10-08 06:22:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 5f692f2c-96cc-30c3-8ad6-ac73287a5ac9 | -17.11918 | -41.3369 | 2026-10-08 06:22:00 | AQUA_M-M | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| ade3f80f-64c6-3ca5-8a3d-bace3ea18ae9 | -12.22826 | -44.71442 | 2026-10-08 06:22:00 | AQUA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 25f6398b-d934-3b04-a2df-56030a6f28f8 | -11.23638 | -44.86704 | 2026-10-08 06:22:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0d41a312-c742-3dc5-a8d7-687d7d009fa0 | -10.42246 | -47.26786 | 2026-10-08 06:22:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 258fe4e5-5afb-3c69-b101-72181af52f36 | -13.15831 | -43.28357 | 2026-10-08 06:22:00 | AQUA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 9348f437-0e5e-3980-bc16-5fb1454658e5 | -11.62929 | -43.7078 | 2026-10-08 06:22:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e8726b2a-3cb6-38bb-9aab-ee81efccd9df | -16.90649 | -40.88985 | 2026-10-08 06:22:00 | AQUA_M-M | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| f1b1ef7c-1b44-3ff7-b689-07752f8e3b30 | -18.25983 | -42.16652 | 2026-10-08 06:22:00 | AQUA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 2fbf050f-4144-3f80-b49e-33f5c609d966 | -11.63099 | -43.6971 | 2026-10-08 06:22:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 7073c929-f3ea-3928-8d38-4bae565d725f | -13.15987 | -43.27375 | 2026-10-08 06:22:00 | AQUA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 73c044ac-a5a1-37e8-ab6b-e0b8ec97e4ad | -10.41914 | -47.28778 | 2026-10-08 06:22:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bb88803e-c3ef-3563-8606-4bcd14f6a131 | -16.83012 | -41.0367 | 2026-10-08 06:22:00 | AQUA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| bab671b0-c7c2-319c-bae8-7a4730e914a5 | -15.59246 | -43.22417 | 2026-10-08 06:22:00 | AQUA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 21a55db8-18cd-3d28-b7cc-520b0e59d365 | -13.49994 | -44.36675 | 2026-10-08 06:22:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7168d1f7-316b-369f-b6a5-17bf99870677 | -11.23426 | -44.87991 | 2026-10-08 06:22:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 66495122-d0de-3932-9f8a-fce1bd35ac73 | -15.59098 | -43.23363 | 2026-10-08 06:22:00 | AQUA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 13.8 |
| b88930ce-c163-39f4-80bb-e53dd5398d5b | -16.82873 | -41.04619 | 2026-10-08 06:22:00 | AQUA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5194e486-5f9a-336b-b5cb-79620f9226d2 | -18.25844 | -42.17576 | 2026-10-08 06:22:00 | AQUA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| e5d33bab-cc6a-30f6-a488-72a31d7a25c5 | -14.92689 | -48.09927 | 2026-10-08 06:22:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| b5d9fc46-b7bd-37a0-ba1f-5acd88da1445 | -11.63272 | -43.68623 | 2026-10-08 06:22:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 55040ccc-e23c-3f21-9da8-0bea1c553523 | -8.62727 | -67.02785 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ff68c7e9-4b5f-38bb-8ea2-102a9f2e6f4e | -9.042 | -65.93174 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9af30a7e-0d1f-37fa-af90-6ff9b362b43b | -9.06127 | -65.9301 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d85f41c0-d38e-3fa5-8d9c-3e7ed209e451 | -8.61798 | -67.05428 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48ef5d72-69b7-3c12-8c43-2b425dfda3de | -9.12029 | -66.00507 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df1824ed-5e49-3138-a0ba-fc4ef218bd90 | -8.62213 | -67.0232 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |


[Clique aqui para ver as próximas entradas](README203.md)
