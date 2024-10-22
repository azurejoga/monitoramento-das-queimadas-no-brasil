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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98e51807-4d67-3ab4-8832-3940efb881b9 | -17.94302 | -57.22184 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 41145304-4474-3075-88ed-e865c78aa087 | -17.94242 | -57.22599 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 426e9dec-77bb-3949-a7b7-13f2a21c66d3 | -17.94068 | -57.21299 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8e7ad434-4708-31ae-9cd7-1c8705e2508a | -17.94009 | -57.21714 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| da378b84-a542-3825-9ece-a9e2b0aa85bc | -17.93949 | -57.22128 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bd19a54b-e6d0-38be-b207-7a27255454de | -17.92592 | -57.24035 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4ed0a1e5-9f80-393d-a0dc-52d465872230 | -17.84166 | -57.60182 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bf61778e-0b88-37ef-89e9-0208a427a250 | -17.84108 | -57.60582 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f3d3b5fe-715c-33ab-8ad0-c149fb143f26 | -17.8382 | -57.60118 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 741d9dc2-b28d-3f4d-9236-637779bea001 | -17.83588 | -57.59261 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 18f9ed09-62a1-3e48-9cc8-d083e27eed0a | -17.8353 | -57.59662 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f1231ec3-efd2-36bf-bf95-239f5a8ea9ae | -17.8324 | -57.59205 | 2024-10-22 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8fb0eafe-3d13-3ddd-82d0-dcdd1ed33779 | -17.79604 | -57.48813 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 18e40bea-f6d1-38c3-a677-44572a9c483e | -17.78141 | -57.56401 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 18446ca9-e9f7-3838-b259-c7e049654252 | -17.78086 | -57.5434 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0300a4c4-122c-3f22-b70e-23223dba1b4b | -17.77794 | -57.56347 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fe04ddd4-147f-329c-8343-0519adcfc9c8 | -17.77738 | -57.54285 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d71939e7-7321-3d52-b8ac-b0edd31b97b3 | -17.77042 | -57.54175 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ee3375bc-a9ba-3cba-854b-efb3f19328f7 | -17.70532 | -57.44902 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| da3fece9-060a-3aab-9edf-ecdf38b419cb | -17.70475 | -57.45306 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7fc0a2a3-c4cf-3313-bb0c-729f3a26561b | -17.70126 | -57.4525 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 356f2299-82fb-3be4-b956-d20836dfe85d | -17.70021 | -57.44976 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a56c0468-3c45-3a64-ae6a-e7c7aca467b3 | -17.69962 | -57.4538 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b3edc40c-a8c5-3d05-b2de-65a4fdbfa5a0 | -17.69834 | -57.44791 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| bc79d95c-ef69-36dd-ad60-dee21ada5dae | -17.69777 | -57.45195 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1fd1fdcc-c464-3d15-9555-80dafcf772ae | -17.6972 | -57.45599 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| df6f8727-1fd5-3995-91ca-e6a16ef57824 | -17.69672 | -57.44922 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| fd5fa454-d9eb-3770-b458-367af99cb734 | -17.69613 | -57.45325 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c5f47cc3-c682-3066-a44d-e47dfec68247 | -17.69554 | -57.45729 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2f5b2b0b-21fb-33b7-8e90-1df25657d364 | -17.69323 | -57.44867 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| f77bd0b6-a51f-3a08-bd47-fe46ee4cf031 | -17.69264 | -57.4527 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 9fff0a98-83cf-3e5e-a710-313caa54b133 | -17.69205 | -57.45674 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 44496d26-df6b-3f24-a780-168d3e35c281 | -17.68922 | -57.4025 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 537b4a6b-d58a-3efd-855c-db90f808b7af | -17.68915 | -57.45215 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| e9d78f07-0fdc-3167-aa54-ecce7febeba9 | -17.68863 | -57.40654 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| df9edb45-704c-3d74-ae54-acf8e5aac60b | -17.68856 | -57.45619 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2f7d0a9b-3baa-3f42-9532-a28eeb1d9083 | -17.68797 | -57.46022 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1654130a-5f59-326b-9d2b-d9c22ab1c93f | -17.68566 | -57.4516 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 53c77416-ff33-3d56-8aa9-a016e1c339cf | -17.68507 | -57.45564 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c47cf756-6399-3555-95cf-e3dabf4c3be1 | -17.68282 | -57.39734 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 24858135-537d-3d6f-b9ae-f4607a9fe601 | -17.68223 | -57.4014 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1e3a8706-6450-374c-aca0-4cad6d5113e4 | -17.67932 | -57.39679 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1f3b3077-cc39-35af-b0ac-1ebf5a4c93e2 | -17.67874 | -57.40085 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4bf7a4d6-9909-30ab-8f01-80f585530c2c | -17.67405 | -57.43324 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fbfedce2-e3ca-3873-b2bc-6f6c40e42695 | -17.67346 | -57.43728 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c7552ae8-0c17-3502-b0ca-3ca6a6c45318 | -17.67116 | -57.4038 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e9411b3a-56ed-3536-bf0c-6dd7366e75c0 | -17.67056 | -57.43268 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a72c7f10-61f4-3b06-be70-561547dd4c5a | -17.66997 | -57.43673 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 967016a9-8034-3ade-a1d0-d06ebf76c676 | -17.66766 | -57.40325 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a32ff1b5-b7a8-36ce-b4e0-e14451928430 | -17.26264 | -57.3032 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 6611e80f-c663-3774-8f9d-f08e3c33ccd3 | -17.26205 | -57.30725 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 40d5143e-58b9-3080-8763-e8796f406b3f | -17.26031 | -57.29456 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1d55ec2f-377f-320b-95a0-e1e1381aded1 | -17.25973 | -57.29861 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b3e7f816-d142-383b-a5ae-ed143fddf66d | -17.25914 | -57.30266 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1c05a943-9a93-3b22-81b8-01a866cb1c30 | -17.25682 | -57.29401 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7268c823-405c-3c7d-852f-64ada8413dfb | -17.25623 | -57.29806 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b25fc555-50d4-3e03-925b-4bdfbc823b9f | -17.25565 | -57.3021 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 015ad7e7-1b1a-3cc7-8dd8-854e10b22c45 | -17.25508 | -57.28131 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 44b25460-e4c2-35a9-adef-60f89916c575 | -17.25506 | -57.30615 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7bda559c-08f8-313b-9fc5-522a7fb5ae82 | -17.25449 | -57.28537 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 27063405-a6b2-305f-a612-bbb3e87d0078 | -17.23058 | -57.27747 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 91f04c61-5e57-3007-adcc-b508a629a2fe | -17.22942 | -57.28557 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 51934f4b-4646-360d-8508-80b65ca608d6 | -17.22769 | -57.32251 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9bc71dcc-a02b-312f-a0d7-7ca2f9b9ed75 | -17.22766 | -57.27287 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 26dbb3aa-6b72-3f58-a28f-a3d18c1c0ee5 | -17.22711 | -57.32655 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a4c85804-d536-3625-982f-8f6d3a6eb907 | -17.22709 | -57.27691 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7e24fd5a-ccd9-3733-bc06-712f7365235d | -17.2265 | -57.28096 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 980e3a4c-7ff8-3d79-9c66-f001d75619e6 | -17.22592 | -57.28502 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 58c8d2e3-3bbf-3a3d-bded-de5c1eee8b38 | -17.2242 | -57.32196 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| db9d4cd5-f1a1-33eb-858a-02b84b3a777d | -17.22361 | -57.32599 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d0f5f490-bb88-320f-b63e-960d4be41a84 | -17.22009 | -57.27582 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fee0057b-c423-3b11-97a4-4d07091dd1f6 | -17.18458 | -57.29919 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 044eb409-b7d9-389a-8e4d-1c9346d0775e | -17.02112 | -57.3251 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5e3cb4a7-dec6-354a-9fa5-ba88b1e0b945 | -17.01996 | -57.33311 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 4b24bc4e-48c4-31d3-ae1f-9ee262ab7c22 | -17.01938 | -57.33712 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 8394a77c-c813-3831-854c-ce8085111b4b | -17.0188 | -57.34114 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 47cdcca1-58e1-395f-8165-10b5a51f73dd | -17.01647 | -57.38172 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 632d2013-1598-30c3-94c0-728a86becc13 | -17.01531 | -57.36517 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b5ccb457-8286-3752-a4fb-3bcf98b1bf33 | -17.01184 | -57.36463 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e99fced1-385f-3732-bce5-27d58226b2b6 | -17.01125 | -57.36863 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| aa8c9808-079a-360d-be75-6b0c85bbd424 | -16.83229 | -56.68006 | 2024-10-22 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e3023d5b-f728-34ec-97f8-f4c91c0564b5 | -16.9565 | -57.52656 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 75810c7a-6bb7-3512-bc5d-e933048dced8 | -16.95593 | -57.53051 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 60cd895c-51cf-3aa0-b2bb-c97062645322 | -16.95536 | -57.53445 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| dc81f759-fe74-34a4-918d-8ea254030d4d | -16.95304 | -57.52601 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 3393831f-4e71-3d38-bb88-c57c508951b1 | -16.95247 | -57.52995 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 4189edfa-e910-3574-a89f-c43475f44fb3 | -16.9519 | -57.5339 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 64d58533-1d25-3829-9bc4-cb36a7abfddc | -16.94901 | -57.52941 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| c7017f39-a542-363f-9ade-fcb2438b3240 | -16.94845 | -57.53336 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bb2eb30c-f7c0-36e8-b1f9-5d69c9288f52 | -16.94556 | -57.52886 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6c6c31d8-980f-33ed-8a9d-64f691a73a8d | -16.9421 | -57.52831 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2db11cc8-a826-3ab5-b7fd-58acc7fa59ec | -16.9231 | -57.80468 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 824e1bb7-bb98-312d-98e9-767deeb68361 | -17.20802 | -57.50784 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c65a7486-d9cb-3da7-918a-65287fd3d03b | -17.20745 | -57.51181 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 936a106e-2c64-368a-8cdc-198092fb3b43 | -17.20456 | -57.50729 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c85e9ed1-e608-358b-9726-01b9e91194c6 | -17.20398 | -57.51126 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3a70ecf4-8eef-39a3-97fe-b46b8207c150 | -17.07585 | -57.47598 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4dc6eee4-f295-3848-bdda-bbfb4c288f9f | -17.07239 | -57.47544 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 081927e6-0b86-312d-bd85-f6feaa6f203c | -17.06835 | -57.47886 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bfdd9fa9-6132-3aa4-a1fc-36ef9a77d84d | -17.06488 | -57.47832 | 2024-10-22 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README30.md)
