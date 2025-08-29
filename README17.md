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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa0eef6f-a4f2-310e-8db4-18fad6bea0af | -8.1399 | -61.2053 | 2025-08-29 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 272.8 |
| 3d5142ff-b003-3a2a-9ca7-266e938dd727 | -10.3624 | -57.8258 | 2025-08-29 01:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d2ab0c8a-17f4-3b76-92b7-c1b0c3a6ae63 | -12.9961 | -56.9201 | 2025-08-29 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 96cc99b9-8818-3f5d-94f5-2c6cc179190f | -9.462 | -60.549 | 2025-08-29 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 67ac4d4c-73d5-31e3-abf5-2c88dcdb6816 | -8.1758 | -61.3755 | 2025-08-29 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ef3fa5a5-0ebb-3513-9463-dbfb46ea8798 | -6.7074 | -49.4561 | 2025-08-29 01:50:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| e615a973-575d-3b1f-b36c-af59e998ffd5 | -9.7916 | -64.2461 | 2025-08-29 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| b285533c-5217-3f69-9af0-2f834da845d1 | -8.1028 | -61.2069 | 2025-08-29 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d9c4dde6-6c35-39bf-a188-34fc1ceac6f2 | -13.1842 | -45.2633 | 2025-08-29 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ab4f169c-2372-36ae-86c9-5d510f026a4e | -10.8608 | -60.7998 | 2025-08-29 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 3a11e1b9-6982-3441-a0ad-9b6a0e3bbd1a | -9.4618 | -60.5682 | 2025-08-29 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| bc68179c-15a5-33e4-a1f6-74fa7206fc44 | -12.4347 | -63.8983 | 2025-08-29 01:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 1c81f80d-8137-3604-9417-55b1a7cb071a | -10.3812 | -57.8245 | 2025-08-29 01:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 092413a2-c400-3c7e-84b5-27fddee1464b | -9.2178 | -60.8689 | 2025-08-29 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7e3c23e6-0154-3439-ac60-996e1137af66 | -5.6081 | -45.0038 | 2025-08-29 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| e3cd4a8f-3abe-39fa-bd44-47263d733449 | -9.5913 | -40.3448 | 2025-08-29 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 1fabca0d-7578-32ff-9b44-6aeeb9ed8530 | -5.6268 | -45.0025 | 2025-08-29 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 218c4f0f-9fc5-3eda-8c1f-4048cd021c85 | -13.2031 | -45.2834 | 2025-08-29 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 64210667-d001-3acf-ac89-ab550f11e0b4 | -8.1397 | -61.2244 | 2025-08-29 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 3f5df595-2417-31c6-b53c-d9f19a807eea | -6.7074 | -49.4561 | 2025-08-29 02:00:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 182.2 |
| 865fef6f-d38f-368d-b36c-63bbf99c0493 | -6.9869 | -59.3161 | 2025-08-29 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| af20d52e-9a49-3c54-88ec-cf2b3262e8c7 | -5.627 | -44.9797 | 2025-08-29 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 05f7114d-8490-3c9c-8d84-b2985cbdff3b | -13.558 | -46.8745 | 2025-08-29 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 2bb9b2aa-31ec-3e93-8380-fc34121ec85b | -12.4347 | -63.8983 | 2025-08-29 02:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e8956125-68be-328d-9d30-d1d8ed75ff03 | -8.1758 | -61.3755 | 2025-08-29 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e18af8aa-5ae1-35c6-b425-55d27ed1a655 | -8.1399 | -61.2053 | 2025-08-29 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 4fba00cb-4cbe-397a-938c-ff059b877db9 | -6.9866 | -59.3547 | 2025-08-29 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 31d6f5ff-6f89-3a3e-bdb1-3172917b4633 | -8.1213 | -61.2061 | 2025-08-29 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 12567a1e-68d1-38ea-ab7e-310c5a799b8b | -12.0976 | -44.717 | 2025-08-29 02:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 118037cc-ccb7-36c4-97b2-aeee1d5aa3aa | -10.3812 | -57.8245 | 2025-08-29 02:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 63100957-7e22-348e-b195-24628ff28e0c | -9.7916 | -64.2461 | 2025-08-29 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 4aafab6b-79e9-31b9-b851-90a7b761d747 | -10.4738 | -57.9366 | 2025-08-29 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c49fddf1-dddc-3ecd-82f7-d7f1a51e4bd2 | -13.1842 | -45.2633 | 2025-08-29 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| aef1c928-5a13-368a-82e1-eb1c387c9414 | -8.1027 | -61.226 | 2025-08-29 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| fa3283a4-92cf-3fd6-a36a-00dffbbf1138 | -13.2031 | -45.2834 | 2025-08-29 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 03d16fa1-d77a-3bfb-8724-6ee94b26ef7a | -13.1837 | -45.2865 | 2025-08-29 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 077721a1-d8bd-3bb1-af8f-ec6565f82927 | -13.5386 | -46.8775 | 2025-08-29 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f07f450e-a79d-3115-b942-ed53ae34be14 | -5.6268 | -45.0025 | 2025-08-29 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 37c2027e-553e-3252-8360-ecc326569266 | -9.4432 | -60.5692 | 2025-08-29 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3d2d176c-00f0-3a16-b86c-7a8eda270655 | -9.7728 | -64.2657 | 2025-08-29 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| bbf95265-0d40-3c8f-8dfe-11c90a86e13c | -13.0151 | -56.9184 | 2025-08-29 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6bcfc7fe-74cf-3f5f-bed0-abbd369b7d57 | -12.9961 | -56.9201 | 2025-08-29 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 80c49206-ebd7-358b-9507-5bf9181728d4 | -9.7915 | -64.265 | 2025-08-29 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 8abd66b3-7d13-3106-ac5d-e722b5f826ff | -12.4345 | -63.9173 | 2025-08-29 02:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 154.6 |
| cbf8fada-4561-32a8-8797-d1f4b22c9412 | -9.4618 | -60.5682 | 2025-08-29 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| ff4ae6b8-ff04-3171-9fb4-58a311313c63 | -6.5546 | -43.9221 | 2025-08-29 02:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 85685b86-cbb2-3d07-a447-4529e2002f16 | -6.9684 | -59.3169 | 2025-08-29 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7544353a-ba00-3caf-b3b3-6dfed1993b88 | -6.9867 | -59.3354 | 2025-08-29 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 183.2 |
| e33a08b3-36a9-379a-ba47-0e9bd684e84c | -9.4263 | -47.6384 | 2025-08-29 02:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 454c0946-02bb-3f11-94cc-3612d6359505 | -3.7693 | -54.8286 | 2025-08-29 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8cd0a88c-5daa-3503-8ab6-4ce737d76a2c | -6.5358 | -43.9237 | 2025-08-29 02:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 2bc2bde7-2cf8-383e-b4b8-4ffbb987a8c9 | -3.4254 | -49.0517 | 2025-08-29 02:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 70f522ad-fb26-3b60-81b1-f87ca4e096f2 | -12.4156 | -63.9183 | 2025-08-29 02:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1cab3b40-70e5-3b9b-a14d-2c380b1d2ac9 | -9.462 | -60.549 | 2025-08-29 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 8d4b61f5-c63a-3b96-b6d5-5d131a12ffbb | -5.6081 | -45.0038 | 2025-08-29 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| a55a7f62-a57d-3bcf-98c0-2ab0043a2043 | -8.1212 | -61.2252 | 2025-08-29 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 21b6cec4-cb19-3570-8a3f-b82c3db50f2c | -10.3624 | -57.8258 | 2025-08-29 02:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 269cd714-adb3-3875-9cf3-8095e0f466c9 | -6.7072 | -49.4774 | 2025-08-29 02:00:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d0e73a76-c0e2-32f1-9df3-4d73cbe9904e | -9.773 | -64.2469 | 2025-08-29 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 149.2 |
| ce833e7a-23fb-37ca-9259-aa2bcb25c8a3 | -6.9683 | -59.3362 | 2025-08-29 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 4d0cdb0e-9eea-3e7f-bed9-eb949d12f531 | -8.1944 | -61.3747 | 2025-08-29 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6d02ca72-9212-32ab-9d84-368610004511 | -9.2178 | -60.8689 | 2025-08-29 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7cd3c368-5cae-3ffd-adef-1f86b3a86dd7 | -6.9684 | -59.3169 | 2025-08-29 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 13828ebe-d461-3b94-a429-aec44a0b482d | -13.0151 | -56.9184 | 2025-08-29 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 307cb454-16b7-3ea3-ad05-5e4b6a8d295d | -10.3624 | -57.8258 | 2025-08-29 02:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 090d5247-cec9-3219-aeca-69cda71f0375 | -9.2178 | -60.8689 | 2025-08-29 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9d5dbf36-5a76-350f-a13c-8fec83a2c7ef | -12.4345 | -63.9173 | 2025-08-29 02:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 8f17e3ab-7b8c-3069-b458-06b07f9c2728 | -5.6081 | -45.0038 | 2025-08-29 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| fa9417c5-6388-38f1-a7ea-10e90cbec583 | -9.4432 | -60.5692 | 2025-08-29 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a98c10ff-870b-36ff-a7cf-e95ea0399117 | -3.4254 | -49.0517 | 2025-08-29 02:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ea68d830-fb34-3ad4-b5bd-398ce8975f6a | -8.1944 | -61.3747 | 2025-08-29 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| cb88cf51-8b07-3c9e-acf1-dc0bf0ccf8c8 | -13.2031 | -45.2834 | 2025-08-29 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 492777b4-b26d-350e-ae8d-576c728963cf | -13.558 | -46.8745 | 2025-08-29 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 785bf8b4-0ec9-36b9-ae36-84723fa29eb0 | -12.9961 | -56.9201 | 2025-08-29 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 89d56a52-9a2f-3f9f-951a-6bacef48419b | -6.5546 | -43.9221 | 2025-08-29 02:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 87c40765-a0ec-34be-9b94-fc71837c4d8a | -9.4263 | -47.6384 | 2025-08-29 02:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 1f78a5ca-7da4-3753-975f-bd89c10ef03c | -17.3442 | -42.6333 | 2025-08-29 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| b5151135-7ff9-39a6-83bd-622994f5931e | -9.7915 | -64.265 | 2025-08-29 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 174d8bdd-91c5-3b31-b830-bc0b61948d96 | -9.7916 | -64.2461 | 2025-08-29 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.5 |
| dd765132-e4d5-368e-82a8-d4a4d76178f9 | -13.1837 | -45.2865 | 2025-08-29 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| be08269a-57f4-313b-96ce-891e1ef4a55c | -6.5358 | -43.9237 | 2025-08-29 02:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0f8dda61-d6d9-3aa1-8047-ad3d3e666ac2 | -10.3812 | -57.8245 | 2025-08-29 02:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6961857a-b4bf-3b97-8cce-ea0a4ddceba2 | -5.6268 | -45.0025 | 2025-08-29 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 67e2c15b-a655-3474-bcfe-323f12822c37 | -12.0976 | -44.717 | 2025-08-29 02:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e14a28a7-9b14-3857-8b3d-fec166139c26 | -6.9867 | -59.3354 | 2025-08-29 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| ebe83ee5-a716-30ca-8112-f168dee4a13f | -9.773 | -64.2469 | 2025-08-29 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 173942e7-f99f-3e1e-9895-84279b419c7d | -6.9683 | -59.3362 | 2025-08-29 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6b41dc35-effb-3929-85ba-70c1cf75dd67 | -8.1758 | -61.3755 | 2025-08-29 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f3c5bf26-1d13-3b59-8c10-8781badce599 | -9.4618 | -60.5682 | 2025-08-29 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 1e82a221-e820-3047-b269-e3eec8fb2771 | -6.7074 | -49.4561 | 2025-08-29 02:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 0d1cd707-ee42-3be5-b861-5de312c1f13b | -9.7728 | -64.2657 | 2025-08-29 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 1efae1c4-838a-3fdc-bc71-cd323a3623f1 | -13.5386 | -46.8775 | 2025-08-29 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| f975ef1c-55a1-327b-a1d1-9320ac3fa8b5 | -6.9869 | -59.3161 | 2025-08-29 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| d3580bd5-b3e1-385e-963a-6eb28c8d608d | -9.462 | -60.549 | 2025-08-29 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| fc607ed9-7159-3dc4-b2e4-6486c968bee5 | -9.5288 | -65.697998 | 2025-08-29 02:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad8bc2ff-1b48-30eb-80f9-d72a64143586 | -6.9653 | -59.318401 | 2025-08-29 02:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf3f010-826c-34c4-8b0b-8b186e65ae2e | -8.9433 | -65.968102 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63849103-baf2-3830-8020-24641f10a82f | -9.1019 | -65.769699 | 2025-08-29 02:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3ae3c25-dc7c-3fc4-8321-545410df7cbf | -8.1778 | -61.396 | 2025-08-29 02:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 604e93d3-1a63-3b54-aa5a-a1fc1ecdc6d1 | -8.5243 | -70.740997 | 2025-08-29 02:11:00 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
