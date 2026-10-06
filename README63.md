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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af3b20ac-c03a-3736-ba2f-0161512df9af | 2.01669 | -61.08672 | 2026-10-06 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f1a1a01-c220-352e-9f7d-acf521cec392 | -9.5469 | -64.81554 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b831e04a-3f76-38b0-9ff8-1bed4dc23ef8 | -9.26505 | -68.37668 | 2026-10-06 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ab1e970-579b-3626-a030-b32e8e736fc4 | -4.27637 | -55.76091 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36095e16-28ba-3334-859f-ea5eda58eb0d | -10.27108 | -68.83223 | 2026-10-06 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fcb6655-ff5c-3e16-9675-00098eeee4a7 | -10.27128 | -63.83635 | 2026-10-06 05:25:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8e7871-07f9-3615-8feb-608ac0372c63 | -8.87525 | -67.0034 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b343d829-e2c4-32b4-962a-552ffd7ab10f | -9.09537 | -65.73093 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d78df77d-f903-3d90-b14d-cbca045758c3 | -9.10184 | -67.75012 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56ff2367-255f-353f-8cb5-8a8efc6b1ee9 | -9.54239 | -65.68884 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34e5e8ee-654b-3022-9d8d-67a737710ba2 | -9.16229 | -67.84532 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55c4adc8-7931-34e2-9c87-bdbed1c46773 | -5.81685 | -53.83698 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 013f4865-ee9d-3293-8f66-b6c56cacdd53 | -3.54342 | -60.52478 | 2026-10-06 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13896469-21d7-3e08-8685-1b657fe55d85 | -4.46403 | -54.97158 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05969331-b386-3079-93c4-de79d3651e8e | -8.39242 | -70.11098 | 2026-10-06 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5815841d-1ba2-3eb4-955e-dd06a13630c2 | -9.19416 | -65.33203 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0b8e8f1-3110-3521-997f-a759eea41da6 | -6.37002 | -55.15326 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0644698b-b093-324f-b005-1cf94004ff68 | -9.50243 | -67.68159 | 2026-10-06 05:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0faf484e-a44f-3361-99c4-2fb8477bd630 | -9.16424 | -68.25096 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c432787-ef10-397e-9605-521e68df7340 | -3.82648 | -59.40693 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e92bb971-28c3-333e-88bd-de07b36d3b33 | -8.61172 | -72.73071 | 2026-10-06 05:25:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e82d751f-b599-38b2-8bec-c98c72f6b7ad | -6.69098 | -55.20628 | 2026-10-06 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c1392a-5594-3c7b-8e2b-47b6e39f01e6 | -10.64435 | -68.59839 | 2026-10-06 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e541f5a-d9a5-37ed-801b-d5b910a5b34c | -9.15512 | -65.56421 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1eda28a-9d84-3537-885e-7d226dbff99a | -8.92465 | -66.84251 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 37e2e945-fb87-3d6c-aae9-471c018d5443 | -9.17088 | -68.26646 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6204b015-6e0d-364c-8de5-df042b00e3e5 | -6.00471 | -53.51248 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d56ba91-eda7-3698-b0b7-7bbb307ae0b9 | -6.372 | -55.14949 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdf09f24-7824-341f-8f38-24e9ef31e68b | -6.00569 | -47.39415 | 2026-10-06 05:25:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| acd2ceeb-ec59-3658-9205-d1676e58aaf4 | -9.44158 | -67.09888 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92c7bc6a-a0bc-3dbd-996b-c99d863fe77e | -7.81875 | -72.83419 | 2026-10-06 05:25:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b5dcd8d4-210e-33a0-8b1b-fe7864f7d631 | -8.93256 | -67.34759 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 145846ad-836a-3997-a4a9-c5ca6d4dc3d2 | -8.92878 | -66.84321 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a328d2de-eb56-3f91-adaf-7f9d82dfeb5b | -9.73412 | -65.09374 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9debf342-a4d0-32db-8a8b-b1a19f1b6fb6 | -11.99476 | -60.47318 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e6123b1-87a5-30de-9af1-790c0fa6fa4f | -9.12409 | -65.8658 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5217b123-5820-3165-8464-6ab7a2e185d5 | -9.67222 | -66.82899 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78d19723-7f09-33e7-9ec9-99e308da536a | -9.41522 | -68.17696 | 2026-10-06 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc365c36-84cc-3331-9fa2-f550f46b65e1 | -4.2863 | -55.24224 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73402023-258a-3576-8a27-d699f75185ac | -9.19326 | -66.00673 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a857af4f-2fff-351a-84ec-5d2adf66530d | -9.11734 | -67.71305 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71e2b153-3024-385d-b887-c1ea810f53f8 | -5.96067 | -55.35595 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 311f085a-4ef1-30e4-9a85-16655c8da402 | -9.60135 | -61.82127 | 2026-10-06 05:25:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 873b0c58-c17b-3b7d-aad0-16a5f8008338 | -13.50231 | -61.13918 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b3c4ffa-33cd-338f-b38f-19c240e89bdb | -9.7231 | -65.09187 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db5ba937-a027-3b17-92b7-cca5829d4caf | -12.87714 | -62.15419 | 2026-10-06 05:25:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57494983-aa97-35ef-b32c-424ac9fa7e4b | -4.46047 | -54.96718 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a5e305b-2ed3-385f-8f8a-5f4a0fdcd3a6 | -10.95405 | -60.90905 | 2026-10-06 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5139ccb8-75d6-3593-b2a2-4fd496588c77 | -4.81007 | -54.73385 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4a1de95-da4c-350b-a0d7-6b256670ab3e | -8.85386 | -66.79489 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf9e4fca-b843-3bf4-b16e-d10a01b8b9e7 | -9.10822 | -65.3567 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a78abd27-f547-3ba9-8bfa-7dba912defbd | -3.74923 | -59.29118 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a027300c-17e1-3a37-b875-181cf722e044 | -3.97293 | -59.34032 | 2026-10-06 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ef8214d-6796-3c52-bd3e-a7f9b43e7206 | -9.46626 | -66.78542 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47d33ac3-3667-3928-847a-cd1cc705540d | -12.14095 | -61.98809 | 2026-10-06 05:25:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2587a8b-5324-3a59-8e36-53bb4de655cf | -9.11275 | -65.35274 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42411542-0098-3ffd-a3c5-fffb61e7957b | -9.227 | -65.69085 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9271487c-6f00-31f8-a56f-92b0ea5b3985 | -6.00541 | -53.50753 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7e646a4-99d5-3878-bed5-0f9b1718c01a | -9.45861 | -64.3323 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbb3f441-dafe-3dee-91bd-a356fcc6c78a | -6.32778 | -55.32448 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 278ec5c5-a8ed-3abb-a7ef-44003fd873e8 | -6.00483 | -47.40062 | 2026-10-06 05:25:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f8e6284c-8e00-39d3-b4cd-018b1247d100 | -9.91536 | -65.01855 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c90fb3fb-b3f3-3662-a84e-2e4713e8ae35 | -9.72383 | -65.08746 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b451a5a-ba3d-3705-b1b9-96dc669a4a35 | -3.71334 | -58.93036 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08663d81-e640-3ce3-bbd4-ed6237860276 | -13.51957 | -61.11586 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dba2165e-2302-3e7e-a8f8-a2f643152f57 | -9.72677 | -65.09249 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a126ef11-7185-3423-a483-52bd011226cf | -9.84932 | -60.30657 | 2026-10-06 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdab745c-4222-30bb-9fc6-abc3d2ddea17 | -12.16167 | -60.74884 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4e65498-4e84-396b-a4c8-8bb0f1a1ef69 | -5.9689 | -55.35684 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebb29290-5691-359b-b65c-683a47a33255 | -9.14557 | -65.41371 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59f80ffd-891d-3329-916d-de176e509703 | -3.70945 | -58.93338 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2815dc4-7dfa-32f0-ac39-4b58f9598ef1 | -10.03339 | -61.91261 | 2026-10-06 05:25:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da030e38-6825-32f6-802b-4c0b1ea8ef38 | -10.1414 | -68.39749 | 2026-10-06 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96e01bca-593a-3829-8d77-4db56dd18a05 | -5.95712 | -55.35161 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28a9daad-5670-3198-85cb-6dfe6b5baa52 | -3.67236 | -60.6125 | 2026-10-06 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fd5e3b3-d413-3a30-ba06-c0d25c78ac6a | -9.10958 | -67.80932 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16141b34-14ba-3f63-ae1c-579d074d7258 | -3.73699 | -59.41381 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c13e15c0-d8f0-3b76-a23e-a75db579a46b | -5.8936 | -53.63573 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 510c8927-5e63-3b49-b7de-33346f732a08 | -3.7089 | -58.93691 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04dd2dba-7c8e-31be-9481-996a19192027 | -8.84561 | -66.7935 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e12891ea-a5d0-33d2-be5b-b7614e8fdd79 | -9.3367 | -68.79613 | 2026-10-06 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a6e12af-096a-3943-86e9-7b959666951b | -9.1037 | -65.36068 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bd4d509-d08a-3d37-b417-f0d44a04646a | -9.54619 | -64.81982 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1b63980-0de6-38ad-90cd-80d55db0386c | -7.89058 | -72.35111 | 2026-10-06 05:25:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 96fe8970-c47f-31e8-9288-6f2b129615b3 | -12.12963 | -63.15655 | 2026-10-06 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bfb7213-ad86-303c-a3d5-79683d9a0e74 | -3.9768 | -59.33735 | 2026-10-06 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fc580e1-978b-3023-9d99-36de2c4ce5b6 | -3.67653 | -60.54261 | 2026-10-06 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 00a6c354-06b6-3cc5-b837-175b49e01b13 | -10.44026 | -67.83871 | 2026-10-06 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d3e7006-261b-3a00-90ec-f6227832028b | -9.16877 | -68.25175 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1eeb6bd-3cd2-3a83-931c-56c72c742862 | -8.42884 | -70.11735 | 2026-10-06 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9572f38-c718-3a8f-b219-f90a832e2d57 | -9.73023 | -65.09132 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| ad11ae23-d106-335e-a3bc-fbbdbcdc09f1 | -3.8001 | -58.34771 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a5cd011-0f8d-3a70-b338-24e245668e81 | -9.14585 | -65.29235 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4a252f2-7c93-320e-a637-d94fea94cafc | -4.92056 | -55.85625 | 2026-10-06 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a56794a-be0b-3af1-a66c-930588b50b54 | -9.71227 | -67.57101 | 2026-10-06 05:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 092f94ab-727f-3dbd-98a7-380e9b6e2b5f | -8.92334 | -66.85004 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6db4a777-94ab-321c-8fa9-1348a3e1df93 | -9.82408 | -65.04871 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0fe58b20-3493-3c9e-9944-a1ce8939f3d2 | -3.7215 | -59.68734 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88c2ab81-334f-346f-bbbc-e13d2ed149dd | -4.45636 | -54.96658 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a55654db-f412-35d2-bc82-39347413610d | -4.42524 | -55.75639 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README64.md)
