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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0f8ef93-0fe1-3fc9-be54-f2e9a1ebc7d7 | -6.862 | -59.3904 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27a3f35e-e0ba-3015-824e-48d81c52a4ce | -6.5746 | -56.538502 | 2026-08-29 00:52:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d058c4ed-140e-3a11-b731-7049aeca6e10 | -6.7523 | -55.672699 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7fdfe25-0f80-3f00-b365-072d8088d6f6 | -8.2331 | -54.964901 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3e5524b-5dac-3ea1-8933-0e3eaf553e02 | -7.9232 | -61.3606 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3de02220-613c-3369-a8be-27cd3e5beacf | -8.6797 | -62.838902 | 2026-08-29 00:52:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a258631-065d-3263-acf7-51034d422fe8 | -6.7222 | -59.999901 | 2026-08-29 00:52:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e149207-c7a9-33fd-8030-6435c09cd0d1 | -6.1517 | -57.7775 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b947f51f-4692-3f8f-8731-78c6b2b7364e | -5.8866 | -57.745399 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c43f79d-22e7-3325-9a26-3bcb5930e3a1 | -20.9233 | -57.569599 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 985721bc-bdbc-3d4f-b4aa-51b65e62b60c | -10.4837 | -64.479797 | 2026-08-29 00:52:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd6f7ae6-e1b4-3c14-9743-0799a13a2cd7 | -15.1145 | -53.569698 | 2026-08-29 00:52:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc5c2adf-6fee-30bd-bf8a-3ee306ef0fb1 | -7.3336 | -55.169498 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4efb58f-10a2-3002-8581-c8e3385194cf | -13.4701 | -57.043701 | 2026-08-29 00:52:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec966d63-0526-3cc4-b80f-d5e488030d0f | -9.9275 | -60.426399 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c89bcf0-421f-3da1-a9cf-5a8a7d9adb5b | -6.7644 | -55.680599 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5454d7c-730b-31a4-9e89-964cfda57065 | -14.923 | -56.319901 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f17f332-f321-36c3-83b3-c7c58a9f0111 | -8.5228 | -55.3578 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a6ecea5-f4dc-3ebc-8e79-242c2a3623ea | -3.9065 | -60.941002 | 2026-08-29 00:52:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 371826e3-f912-38b2-9ca4-d25b38ee3e53 | -9.9519 | -53.923698 | 2026-08-29 00:52:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0059220-daa5-3a40-beb3-fd6478254720 | -6.5627 | -56.531601 | 2026-08-29 00:52:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9d1177a-c174-3420-a199-d3e2160902d3 | -6.086 | -57.716499 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f97b7bf0-8d41-3388-b5af-c3cfe9a28b9a | -7.4959 | -55.288101 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed31d41-b183-371f-b953-398540b590f9 | -11.022 | -57.210098 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6120dc11-5ae7-3b82-870d-7f9ddddeeb6a | -14.9092 | -52.6147 | 2026-08-29 00:52:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5a51ef9-8982-3b8b-a687-b66dbdd00a6f | -20.9541 | -57.569801 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d4e7ebb2-507f-3908-adf6-365799ea2713 | -8.9461 | -63.263199 | 2026-08-29 00:52:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 84961c1b-4681-39c0-bd1c-d18565cbb526 | -9.5165 | -65.565399 | 2026-08-29 00:52:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 416fc58a-2f48-3b75-b0bf-db1127d2009e | -6.8846 | -59.444302 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d710472-7751-3d25-9bdd-ad88f679a740 | -6.777 | -59.4244 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bee573d-8d59-36e3-953a-c08e2ea31fa4 | -11.1774 | -51.2607 | 2026-08-29 00:52:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e3fa320-2f24-37b6-9b0b-b13c116b53ae | -11.0238 | -57.2178 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84e40eb3-e27d-3bf2-9ace-972d5efea2ec | -6.9477 | -58.952499 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| feadf6e9-38ec-392b-a53f-aec21a510671 | -8.5906 | -54.8214 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd1a2d77-793b-3f3d-ad1b-ab7d58c083d8 | -14.4645 | -58.520599 | 2026-08-29 00:52:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e05b651-0ff0-38a5-bf26-5c69b8af3668 | -8.1498 | -63.990799 | 2026-08-29 00:52:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e32428c1-390d-3f43-9a5a-d792a40933e4 | -9.9162 | -60.4216 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1083f65-c38a-36f0-bf48-9cfc923b6a4e | -4.1573 | -60.683701 | 2026-08-29 00:52:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f590b264-cbae-3b97-97ff-b910a2fa452a | -7.5334 | -61.365601 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b24870f-f521-3570-a6ca-9952cd44ec4e | -6.8222 | -59.941101 | 2026-08-29 00:52:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae1d940-50a9-3fa1-98c5-9520d41d1d69 | -20.975 | -57.618999 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0be83d0-d98a-38e7-a71c-2defc96fc8cb | -8.974 | -50.776501 | 2026-08-29 00:52:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 395ca067-dd64-3ba4-a4cc-a4a505e2e222 | -6.8832 | -59.392899 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 684ae39e-f060-3649-8415-94d05409f048 | -6.1731 | -57.780998 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97480839-5088-360f-adea-a5da54e8b45e | -6.1215 | -57.691299 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32cc09de-8fc0-31a1-b3d4-c5d0e52d3cae | -14.1677 | -52.836102 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdbefe0c-4654-3007-a0e1-1bf1f6efd822 | -12.7872 | -60.4795 | 2026-08-29 00:52:00 | METOP-B | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5036d50c-785b-31cc-a407-06a99fd5cd7d | -7.6134 | -61.355202 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab3df9f-eda8-3e0b-96ba-215bf38a4d68 | -8.9576 | -63.269501 | 2026-08-29 00:52:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dba162ab-54c4-3322-833e-d00c9d9df138 | -6.7596 | -55.660198 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5977b21-1b4d-3f35-b082-c0cd630cf037 | -8.5872 | -54.7645 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d0b00f-c074-349b-a7fd-fc03bd013756 | -6.5376 | -55.244598 | 2026-08-29 00:52:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c2b4a3f-50d5-3aa0-9685-c429d70abb09 | -9.2248 | -59.4039 | 2026-08-29 00:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1481cac5-9c8a-379d-84d3-3746a3ce1502 | -15.6214 | -56.3936 | 2026-08-29 00:52:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2f2cecd-6863-32f7-93c4-da066b67cf29 | -7.4861 | -55.290501 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f99be9d-9ca6-3b44-a883-bfffbcfd3065 | 4.548 | -60.7131 | 2026-08-29 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 27c468e8-be9b-3f7c-907e-7b125af13f70 | -9.8789 | -60.254101 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e65e1dc-4bff-38b0-9e10-c1b66c614302 | -20.9718 | -57.604198 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d239edc2-8602-33f2-881b-2a6f295d877d | -9.2547 | -57.063301 | 2026-08-29 00:52:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf2d388-00d0-3e04-b110-1411162f1fb0 | -9.2762 | -57.066799 | 2026-08-29 00:52:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99adb741-71e5-3c54-869e-0fc7468182b7 | -15.5734 | -56.2752 | 2026-08-29 00:52:00 | METOP-B | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bf86a05-b04b-3ef9-803d-2911778ee3b2 | -7.5081 | -55.296299 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a24de1a6-d45b-331a-9683-7a2a40dfd6e9 | -5.8964 | -57.743099 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6c3114-b69f-32aa-9494-7a2c2ce7a5e1 | -11.1817 | -51.277699 | 2026-08-29 00:52:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 712032f4-c902-3415-9ef8-746c57ee53f0 | -3.4205 | -52.7672 | 2026-08-29 00:52:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 433ebc26-f433-3ff8-bc32-d1c6cad984b3 | -10.4815 | -64.469498 | 2026-08-29 00:52:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6aa617d-b45e-3d37-ad69-1a4ddd2a8cfe | -9.9358 | -60.417198 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee697b8-6f96-3d63-a56d-9b00333939cb | -10.5572 | -59.604198 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c862e65-849d-3149-bb82-6021f5704ba2 | -8.9791 | -50.796398 | 2026-08-29 00:52:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28c562ca-84ac-3ec2-9ba1-6c1f8f61513f | 0.1402 | -60.402802 | 2026-08-29 00:52:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 49193cae-e140-3eab-bf68-94ebcad5bc28 | -7.5056 | -55.285801 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 717615db-9268-3b2b-914c-467dea627b49 | -14.9408 | -56.307301 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ba6193d-9ca8-3818-9339-517aa78adac2 | -8.582 | -54.742599 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d80b0ed1-9ea0-3381-86ce-6d415f01d316 | -20.9734 | -57.611599 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c084081e-7b45-3920-82ec-1de8aa490c2f | -20.2117 | -47.390099 | 2026-08-29 00:52:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 53dde39c-434d-3deb-a0c8-859918fe0131 | -14.1968 | -52.8284 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58ca9eb4-0dda-3acb-a69f-ec7c9bb49596 | -4.2939 | -59.471001 | 2026-08-29 00:52:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 174d0a61-b74b-3fce-8a39-94e58a8f54b5 | -9.141 | -61.008202 | 2026-08-29 00:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b735aa1c-d77b-3b82-a0f5-6cf3819ddb96 | -6.8636 | -59.3974 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22524b0e-83d5-35b9-9194-062f790db90c | -5.983 | -57.672001 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0f5101-a61f-3b88-af73-e3fb533794d7 | -6.7754 | -59.4174 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1aca466-270e-3959-8758-828bf822becc | -10.4717 | -64.471497 | 2026-08-29 00:52:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8d55696e-ef96-3c78-83ad-5431dfc69d2e | -11.0255 | -57.225399 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b28f851b-9eb5-35ea-a276-c0496ec1c918 | -14.9097 | -56.306702 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd851619-087d-3eef-b4e0-a103e9e199b6 | -6.8612 | -59.025101 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6ddbd80-bffd-3300-9a93-d22fc7415d4d | -14.9248 | -56.327702 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 266450cc-8fa9-3f3a-8b07-6e63e7dd6f90 | -6.2557 | -55.403 | 2026-08-29 00:52:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87430e89-9e6f-3f11-b439-67734c3c9e08 | -11.2592 | -54.036201 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58d4862c-7ecd-3d19-a4e8-fb73461b6170 | -10.4859 | -64.490097 | 2026-08-29 00:52:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 71a09e94-cb73-3104-83d9-ffdd1d91441e | -10.3937 | -61.234299 | 2026-08-29 00:52:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 008b6549-ff4d-302a-82bc-9cbc83233d46 | -17.616199 | -51.6008 | 2026-08-29 00:52:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dd3f5e8b-9ea7-35bc-8288-ad579eb6ea9d | -10.0816 | -62.300499 | 2026-08-29 00:52:00 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61457145-a64a-361a-b1dc-89fd57f14c92 | -7.5601 | -61.300598 | 2026-08-29 00:52:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39faf95e-8dd7-3b7e-81ac-ec703ae2360d | -8.5808 | -54.8237 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d493e0a0-b7d7-35a1-937a-dde6fa61c465 | -17.6259 | -51.598099 | 2026-08-29 00:52:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1837be9-53d2-3cf3-b6a2-ba8c14d76abd | -11.0176 | -57.235401 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b756058b-cc14-3779-a996-997cf9881149 | -14.3522 | -51.719101 | 2026-08-29 00:52:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3596d380-b957-3468-94f1-36fc345f7116 | -5.8903 | -57.761501 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef54bba-f363-37a7-9a2d-cb47ab333615 | 0.1517 | -60.3978 | 2026-08-29 00:52:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c7f1684f-4748-36a3-bfd3-87fca0ec2f24 | -8.9993 | -65.433899 | 2026-08-29 00:52:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
