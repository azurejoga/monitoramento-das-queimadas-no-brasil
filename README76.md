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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f585abf4-fdfe-3043-b960-98449c636a45 | -8.61351 | -62.64618 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81292391-3216-32c7-ac13-c0db95a9b871 | -9.59247 | -55.37536 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e3c4876-b162-3fff-8a86-aa83cc148be0 | -8.90367 | -62.47163 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4116b2b1-87e2-31d9-8e0b-f0973ca3b050 | -9.15565 | -59.57074 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65c12c34-cfb2-36c2-a246-c10312b1a10d | -9.40308 | -60.52361 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ceaf88f3-c95c-3e0b-a88d-fc51e1f674af | -4.95878 | -55.81425 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1f45e64-c0f1-381d-836d-befce113296f | -9.15805 | -59.55348 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1fc5416-6cec-3882-b1a0-da8a7b000013 | -9.58605 | -55.37885 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b68e542a-43a6-36eb-84d3-c0ab1d9554a5 | -4.69855 | -56.06672 | 2025-08-27 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02ed7522-6b2b-39e2-af71-34b5197abc07 | -8.86607 | -62.44852 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebe9a035-e430-38e7-a7dd-d0217539ad9f | -6.70546 | -58.56232 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a96f4895-a1fd-3f34-b87d-17d04a98b931 | -7.05542 | -59.81625 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4215cafe-9877-30a6-97ad-30003bd0fd6c | -7.36655 | -70.14497 | 2025-08-27 05:44:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 478a4027-03e2-3d64-870d-c26e168aa046 | -8.25287 | -61.46566 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2041144f-894c-39d3-ad50-96bfc69d3cc0 | -8.68758 | -62.87425 | 2025-08-27 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2278643-a5e8-3990-9162-1c36b808ff85 | -9.16914 | -60.76911 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0553e6c8-d13f-33cf-8b11-f6a456cda7a9 | -7.74714 | -67.15366 | 2025-08-27 05:44:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38ac8abb-fc5f-3a92-ba9b-e11f5f84f43f | -5.35454 | -60.39714 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 735bd396-3d46-3154-8df1-951ad2dfe7eb | -9.18099 | -59.51755 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fdbc79c-9598-329e-be6c-db0ca87ab1f0 | -8.85813 | -62.45168 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0c4234a-56f6-3a7a-acfd-7401801dea2a | -7.60533 | -61.62855 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c121d4-3afc-30cc-b469-35d64d7e0f17 | -9.16779 | -59.51558 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5637bb3-8270-364a-9fd4-f1b8ad669f39 | -8.35028 | -62.93803 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab3eb403-f54e-3fe5-a0f7-6e1f3534b603 | -7.56501 | -63.86277 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cacc54e8-d8c6-3ec1-97ab-8c1b59f3186b | -8.6695 | -66.58797 | 2025-08-27 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 931925b4-3c83-3fd5-86f6-dead1b910b7b | -8.34318 | -62.93696 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f54f0d74-5d02-368e-b4dd-6931d9d03cca | -8.85146 | -62.44632 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78dc579c-0b3d-3e00-92d8-5633c9ef06a6 | -9.17219 | -59.51623 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 696e39e0-5463-3b1d-8cf1-8f3c7af27258 | -9.41153 | -62.48379 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7f8e8f6-a177-3bba-b56c-3ab2c363e09e | -8.33489 | -62.94388 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a306ccf-480d-3091-b950-3b1c8245a768 | -8.89547 | -60.77291 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaa190bb-7698-34fd-a259-de76909d3495 | -9.64347 | -59.62983 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d419d11-d68a-35e8-91d9-98d67cdfa19b | -9.40093 | -60.53849 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d41dc278-602f-3289-884f-075f8f2b1fdb | -6.31353 | -59.86345 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 838b96eb-7244-32fc-ba31-339235c94b26 | -6.87476 | -59.90236 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50bbd177-b803-3bc9-a609-15cc9533335e | -9.41688 | -60.54462 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3963609-94a7-3c3e-a4af-aeaa8d0c6b50 | -9.1924 | -59.53225 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df880ef3-b29c-3434-8553-87619b15f1b5 | -6.62317 | -53.33107 | 2025-08-27 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 05d1bbec-da26-3465-a4a0-557b809319e0 | -8.8874 | -60.77172 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f77f81f-e24a-3038-a69b-ca59d66a59fc | -8.96987 | -62.14304 | 2025-08-27 05:44:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99bf1c6b-e607-3804-8543-c1399c3794e1 | -8.58731 | -63.9532 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36c5f83b-6c88-38c7-9e12-7588d943d804 | -9.16339 | -59.51492 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 024a29eb-0de9-3932-85d5-886eaa3fe3c4 | -4.96318 | -55.82167 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2094bdc3-56d6-3001-b5fe-b35f367776d5 | -9.15429 | -60.78443 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e35e2599-3fff-3b46-b2e6-9696b0f99545 | -6.23804 | -60.01348 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eef33ac7-47b2-3d15-b9e5-4a302c06cf3e | -6.30886 | -59.86655 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c75f5f3a-7a13-3bc0-800b-febefd974acb | -5.76158 | -53.76628 | 2025-08-27 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57ca3304-3d12-3a8b-a130-5cb126a199c1 | -9.2739 | -56.90988 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95382d7e-34de-3755-8b45-01fa69cd169a | -5.4547 | -60.15632 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 332d112e-f5ec-3eb7-94cf-f73fa7896c9f | -8.85448 | -62.45113 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 629e2ee7-75bd-3573-9cbf-a76fed3bd941 | -6.90991 | -59.35851 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cc04be7-2e17-3537-a13b-8afdc4eea5c5 | -9.39483 | -60.52239 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dc86d8c-3b87-3aa6-865f-f564d43becf1 | -7.54287 | -63.84812 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 253157b1-d830-3a56-98da-3611a8ad5dc0 | -9.40721 | -60.5242 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a9a159d8-5958-3a5d-9aec-586b6209ac0d | -8.07185 | -61.54836 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3cd3538-70d1-31fb-a5ec-ca5865bcb0b4 | -9.41134 | -60.52481 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46eef734-6163-39c1-b559-1d0591ad6f11 | -9.16742 | -59.55053 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca99019a-e32b-308b-ae1a-881d8e9595c4 | -8.07254 | -61.54377 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 071f6f7e-c93a-3297-98c9-8a5b660bbd1b | -4.09578 | -55.80984 | 2025-08-27 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f5647f4-616b-32fb-95c1-1066dc481870 | -9.40147 | -60.53476 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d9005f2-d796-358c-8cb6-8a1bbcd292e2 | -9.15686 | -59.56207 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8509bf47-ed92-3cf1-b5eb-1b625e438fed | -8.89143 | -60.77232 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6f565d2-e8cf-3aad-9b13-ed1909012c26 | -7.05003 | -59.82057 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4235dc5-7249-302c-9057-a186aacb91a2 | -6.83766 | -58.95826 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9c8cecc0-1d40-3171-8e57-29eee1aea8c3 | -9.40356 | -62.48697 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0678de77-4126-3b91-acd8-23685396ac87 | -6.62834 | -58.54385 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13748f6c-b802-32c2-96c2-dd0e6961031a | -9.40614 | -60.53162 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 95938ca2-2da2-31d8-acdd-75aa83132f08 | -6.91364 | -59.3632 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06b8a04d-43b4-3c5c-8eaa-93262ff36f89 | -6.82128 | -58.9777 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d0f2fc0-e6a3-35d3-a7bd-6a8216881e00 | -8.85574 | -62.44261 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a64a195-6758-3bcb-a5ae-74ea8e79acb9 | -9.41242 | -60.51738 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d569333-cab2-3a38-b537-e82ecdb4d548 | -6.56715 | -60.05783 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151dac92-ed10-3dd2-8db5-cc275a9fd64d | -9.20576 | -59.43715 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 191237e3-a9c2-33f2-98f1-a71598ccc9c0 | -9.18039 | -59.52183 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8e1f983-4ea4-32f7-9f64-90e7c72c80f0 | -8.88369 | -62.45554 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19f4ada1-706b-386b-ab2a-7d99e9767ca9 | -7.62214 | -61.03384 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 073ea7c3-db26-3cc5-954c-9196d9330e86 | -7.37663 | -64.36143 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf6fe2d7-f58b-3045-87d9-0a8e57fa424e | -8.59709 | -63.8674 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 157cae1b-78f9-3edc-af88-52d057065999 | -9.6335 | -59.63688 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f69d9e4-1ae8-35d1-96c7-b3dcc7df5d20 | -6.24921 | -60.02237 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 257cf332-80c0-30f1-8910-5a7c574f4b63 | -8.84718 | -62.45003 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91977f84-9428-3f6c-9b31-85dc66be7a1e | -7.44507 | -63.16379 | 2025-08-27 05:44:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 10186f26-c55c-3ba0-8acb-f720a8d9ba31 | -6.83639 | -58.96686 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 96ae11ca-7dc2-3ac9-a2d4-0b30d6db4db2 | -9.26974 | -59.77415 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74a01150-ea5a-3866-8e64-9cf307ce96e1 | -9.41601 | -60.52169 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cedda4bf-1897-3b52-8bc0-e9e22feb45ec | -9.17319 | -60.76971 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7c31c14-9fca-3263-82d6-edcea06cdd37 | -7.44079 | -60.02975 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f8d61a3-ee49-3049-94d6-5239d5ea271d | -8.6511 | -67.26819 | 2025-08-27 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 277c8d8b-8eaa-3495-91b0-0c99846e9ebb | -9.18921 | -59.52301 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96ec5cfd-5581-3fc1-927c-55bd4eb7a60f | -6.61748 | -53.32482 | 2025-08-27 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ce9bdca0-77db-339f-a093-8ac698626703 | -8.97955 | -63.10898 | 2025-08-27 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b16571f6-9de3-352b-aeae-173993e05270 | -6.2636 | -60.00989 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 589f539d-bb0c-3e9c-bae0-7ef79f7d3c9a | -8.33728 | -62.92788 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5c31719-3472-3252-8ba0-b40a610f4f49 | -8.12568 | -55.37106 | 2025-08-27 05:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dec1dd51-9c39-3281-a64a-a3af587c8ca3 | -8.6579 | -67.2693 | 2025-08-27 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 645a2203-1d59-3ab1-b848-9566e5f504be | -9.39429 | -60.52612 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a3c00f2-0007-3836-8b27-4c6b3a56879d | -5.79681 | -59.22059 | 2025-08-27 05:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94b7a34b-b6df-31db-8261-00dcdd462182 | -9.40201 | -60.53102 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e51e1628-af74-3981-b289-5b759d0510e8 | -9.16303 | -59.54987 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a53e973c-0763-3f41-9aaf-139c617e5557 | -8.7217 | -64.03022 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README77.md)
