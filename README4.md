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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5daf7ca-bcd3-39a1-80ba-ad778bb916bc | -7.50509 | -42.45066 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 377552b4-98f1-39ab-a73d-678a20aa7a82 | -5.24533 | -45.77799 | 2025-11-01 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81ed1c54-aecd-373e-add0-f72d49c30d12 | -4.65949 | -41.96366 | 2025-11-01 00:13:00 | TERRA_M-M | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 2d651ede-ce1d-3070-ac2a-eb4f8a101070 | -6.42807 | -43.94275 | 2025-11-01 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4388c3d8-9762-384a-a0a9-0a72ed74effa | -6.94159 | -49.63953 | 2025-11-01 00:13:00 | TERRA_M-M | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2cc10a5d-70bb-32f6-90f6-e36c02dbc78d | -8.71039 | -41.59493 | 2025-11-01 00:13:00 | TERRA_M-M | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 1260eeb2-0ccb-3f11-adc8-57b8e5a04f9f | -6.4664 | -43.56289 | 2025-11-01 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 0102621e-2db4-3ecb-a19b-f8a626d46ac7 | -4.81942 | -45.75397 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a012fd21-48ba-36c7-8c4f-2a01ed2eb9c8 | -5.75116 | -49.32694 | 2025-11-01 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 09380efe-eafc-3756-beb4-dd9b9b583d24 | -7.07042 | -47.00212 | 2025-11-01 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9055e099-a3af-3995-8466-474d35106f48 | -6.32006 | -43.63498 | 2025-11-01 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 070fad8f-0c83-3e5e-8110-6f0a20e468d2 | -9.91169 | -36.30794 | 2025-11-01 00:13:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| d8d4961a-1a17-3123-a7d9-0221d1c87673 | -5.09864 | -45.91935 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a27980f0-8f63-3430-8452-69ce74f3f9a7 | -5.10698 | -43.39204 | 2025-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ccecbc4-8984-3a2c-8b06-d9a64edd2f71 | -6.98203 | -46.89022 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f0080068-fccb-350b-a816-30a0735ee16c | -5.21935 | -45.91738 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1786db9b-68d8-3d8c-8c19-9d4170d42921 | -4.74547 | -44.42987 | 2025-11-01 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2ff4cea-f32e-3c6e-9b1d-00c6ad5f6ce9 | -6.65736 | -44.66405 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 06147afa-7319-3507-945a-6cc781dc8a36 | -5.59794 | -50.05746 | 2025-11-01 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 728202c2-a051-32d0-a418-5780ffbfb167 | -7.29453 | -45.06276 | 2025-11-01 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f3482d67-6013-3c2d-af5f-6a2ac22d8d88 | -5.22517 | -46.16883 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0d9ee365-0653-32d7-9736-4f1f2ed36a65 | -11.01662 | -43.87228 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69a50b62-ac45-3093-83ca-a5e408934bda | -8.22815 | -46.24384 | 2025-11-01 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 93b56756-1bf4-3bb2-9fb6-56ce74e28741 | -5.79017 | -40.81339 | 2025-11-01 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 85928395-fa96-3672-be92-6ef93a07cde2 | -6.3278 | -43.62422 | 2025-11-01 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| a184932e-4c30-37b0-a3aa-afa487d04431 | -8.56837 | -40.91104 | 2025-11-01 00:13:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 51.1 |
| f288bf75-a3da-3bd9-820b-115e694c072b | -5.79228 | -40.82755 | 2025-11-01 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3a51e0be-b609-3f5d-9953-8925d2762e51 | -5.75632 | -45.86921 | 2025-11-01 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e09647f-6cfc-3cd7-8bb6-40462a9ac9b4 | -6.40063 | -49.17789 | 2025-11-01 00:13:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 452cf62b-e424-3817-821d-fec08b0fdd79 | -9.07011 | -48.82669 | 2025-11-01 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7fdb8ffc-271d-3144-a758-6a47a465bedb | -11.6386 | -48.56045 | 2025-11-01 00:13:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cc578502-9b35-37ba-80fc-846f840fb9a2 | -6.89137 | -34.98824 | 2025-11-01 00:13:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 125.9 |
| 71cee2aa-5c53-3aa6-9d77-6f50302c468c | -5.62484 | -47.41055 | 2025-11-01 00:13:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c42658f4-5455-3c77-8643-e86f0ef3126d | -6.61595 | -43.83788 | 2025-11-01 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4c6f4b77-e77d-3851-b489-5dbac0f278c2 | -5.51879 | -41.09908 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1a8250ef-788f-3d72-b338-a414d4d6e585 | -4.82427 | -45.78927 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c52006fc-ae8a-3845-9841-fe4e265e9879 | -6.26012 | -42.56188 | 2025-11-01 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 12fa9e30-2b9c-3064-8fd9-448752a70e39 | -6.65024 | -46.68809 | 2025-11-01 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 349ffc98-7de5-3276-b1b0-eac833a91a01 | -5.25443 | -44.31135 | 2025-11-01 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 37b6a06c-7ec5-335f-9833-547a5e206f7e | -8.15855 | -44.79486 | 2025-11-01 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9494a2f5-db8f-3427-aa3e-b7479f1d98e1 | -5.89156 | -44.52304 | 2025-11-01 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f2df406-4bf1-3cc6-ae24-26f12441709a | -11.26543 | -47.28427 | 2025-11-01 00:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cdf7d4d6-f7db-371f-b01b-bbb0cdd2593d | -6.13526 | -45.94683 | 2025-11-01 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 32e24cfd-d155-3deb-97b9-392b3794885a | -9.07472 | -48.83362 | 2025-11-01 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| db6c9f6f-d63f-36fe-bf86-02850e9a4fd6 | -4.92199 | -45.97445 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c809d037-5b5f-3a89-882d-d5a2d8c70310 | -10.73122 | -46.24905 | 2025-11-01 00:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 07916bfa-d76f-38d2-859e-b6f57cbdf456 | -6.80046 | -47.04755 | 2025-11-01 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 78f1efa7-3afb-32be-a43f-ca43b37132b7 | -5.83093 | -44.34894 | 2025-11-01 00:13:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 76b242e2-8450-3290-8082-b1f83ab699ec | -4.83311 | -45.78802 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4cea18ae-154f-3c38-86a7-dba18b410668 | -5.86415 | -43.99511 | 2025-11-01 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 96aeac77-445e-3bcd-aeba-1530347fd9f2 | -6.20095 | -43.70552 | 2025-11-01 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a0223dba-27ed-3427-8f9d-3389fa502a5a | -6.9397 | -49.62507 | 2025-11-01 00:13:00 | TERRA_M-M | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 54ace42c-9a50-386d-a47c-7ef9835f0a71 | -9.9244 | -36.31141 | 2025-11-01 00:13:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| b41d1b01-def9-3d01-9b7c-760114da9857 | -7.31396 | -44.94268 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2d03f6a2-10e9-35ef-ac10-108d043ed2a5 | -11.5632 | -47.06361 | 2025-11-01 00:13:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 60045376-50bc-3ccd-acf8-68b3d2450e74 | -4.95679 | -43.44977 | 2025-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1f987fae-b338-3ceb-9cea-fc1e2f7f8434 | -5.32805 | -47.11888 | 2025-11-01 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ac4bc83e-7ef9-3ebc-8a36-69924974b2ff | -4.60607 | -44.42495 | 2025-11-01 00:13:00 | TERRA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1cc0b27c-d7d7-3598-997b-cb1b43d90906 | -5.25984 | -45.60775 | 2025-11-01 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 6fdde3e4-4ad8-37db-abcf-2c00398bcadd | -5.72782 | -44.54037 | 2025-11-01 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0b1d9e3d-9a8c-37e9-ac9b-2b4b2b964d93 | -11.44209 | -48.18789 | 2025-11-01 00:13:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 00388166-86d1-3399-b09a-89129874a057 | -11.01786 | -43.88124 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ce6f625d-1a9d-3499-9361-84913b990361 | -7.69652 | -45.98684 | 2025-11-01 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| efd05102-7276-307a-8ed6-892be4d137ef | -5.23844 | -45.06255 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a65b87e2-4545-388f-9aae-1d0de4ef594d | -5.67193 | -46.73659 | 2025-11-01 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b2889c78-db7d-38ed-b43a-89bfdc7cee9b | -6.88264 | -42.85 | 2025-11-01 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 7559b161-8b19-3aca-a225-36c8977adb0d | -10.63865 | -42.31534 | 2025-11-01 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 87462146-a452-319a-8fc4-4f718646edb0 | -9.92017 | -36.28532 | 2025-11-01 00:13:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| 673fb363-f04a-38d9-900b-998e8100ae04 | -7.34017 | -45.00209 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89e4398b-dc78-330a-adc5-fce2b298d7a1 | -4.80639 | -45.87028 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| db3a752f-e6a9-3ac8-8f19-b2e95d95128e | -10.06485 | -44.98709 | 2025-11-01 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b72c48cc-0e77-36b4-b734-0a858f301509 | -5.83622 | -44.06142 | 2025-11-01 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 1c316869-a04d-3654-b38e-1726cebc91d3 | -4.61628 | -44.43274 | 2025-11-01 00:13:00 | TERRA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 647cd312-d583-3df1-a149-9253ff2e0276 | -11.04987 | -47.90536 | 2025-11-01 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c2cbb9ba-fd9c-3504-a002-688324d45b1e | -7.16002 | -42.54695 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8a9bfe3d-ef8c-311e-a0c2-209cf0b271a5 | -5.98515 | -43.6148 | 2025-11-01 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20265fab-3b71-3c96-9cd9-a6971320beaa | -7.51748 | -45.34502 | 2025-11-01 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ebeda8a4-0584-34bd-9018-b9565863d904 | -9.07191 | -48.84042 | 2025-11-01 00:13:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| da646de8-7927-39d9-a1c5-24921bf6c2b2 | -11.2659 | -47.29052 | 2025-11-01 00:13:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 566f29bf-6424-3053-84cc-e3a965c70d1c | -6.48025 | -44.31372 | 2025-11-01 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95282092-80b7-3e7c-bd19-c32032f37878 | -5.25571 | -44.32043 | 2025-11-01 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74b8dc36-f97e-31c5-840c-90a5d993b96f | -10.89631 | -47.50814 | 2025-11-01 00:13:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ba8797c5-7fab-320e-bfb5-36771fb145b7 | -6.54041 | -43.56501 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8c228743-4ce9-338c-bee4-ceb3653024bd | -5.82968 | -44.33998 | 2025-11-01 00:13:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 489a5158-84bf-394a-b43f-94ecb0773d07 | -6.85316 | -42.26891 | 2025-11-01 00:13:00 | TERRA_M-M | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 099333bb-def8-3078-a145-8a91013ad12c | -5.90768 | -44.63879 | 2025-11-01 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5999c936-da48-3079-8e9e-e8e4da0dcbdb | -5.18983 | -44.90724 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5f7d488e-f883-3270-8208-d996a9e0b621 | -5.19106 | -44.91609 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a3f7450a-b3b9-3a69-807d-dfbb30b33645 | -5.6202 | -41.53337 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1ccb6d68-789b-3df6-9196-9a07b285fed8 | -5.48617 | -43.08482 | 2025-11-01 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| ce0eef95-4658-3848-a6a7-5ad6d6d8b766 | -10.64006 | -42.32511 | 2025-11-01 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 6954a6e4-f706-35e8-85f0-b2bdc57956c3 | -10.63724 | -42.30556 | 2025-11-01 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| df33dc25-b11c-3072-991e-a6a8d2623a47 | -4.9172 | -45.59944 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e0a4d6d0-9e20-3e07-a3a4-ff72a63d1e88 | -10.90189 | -43.98328 | 2025-11-01 00:13:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 566972d1-f9b3-31c5-978b-683d632fe384 | -6.35728 | -42.39099 | 2025-11-01 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 561c8a78-1c9a-3cc0-8771-cae78f09d76a | -11.37365 | -48.91845 | 2025-11-01 00:13:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 47780182-bd7e-3e4b-9f79-2f31db31e413 | -7.23962 | -44.94156 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| c80ffdf5-1533-3720-98bc-874dcbed03aa | -10.3408 | -44.65457 | 2025-11-01 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85b6c980-3648-3f10-acca-f6c9348bb899 | -4.92604 | -45.59822 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| caab9eed-cb35-3b78-b2c3-517c5c52b36a | -10.87053 | -47.5476 | 2025-11-01 00:13:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README5.md)
