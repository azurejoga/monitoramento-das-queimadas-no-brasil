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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebf830c8-c86a-3cd1-8b5e-c46c81702e47 | -17.6871 | -57.4387 | 2024-10-21 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 12ddce14-6ab4-3df6-a784-5a9e872f7b83 | -17.7065 | -57.4569 | 2024-10-21 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.2 |
| 8a31c6dd-0e0a-3bf5-9fbc-c14fcfd3fc9c | -12.4967 | -63.1874 | 2024-10-21 13:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9d8e71cb-ed55-3141-938d-96ad717f8d4c | -12.5147 | -63.3014 | 2024-10-21 13:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 217d97b3-eee5-3eec-8e71-fc836720d2d7 | -12.5168 | -63.0329 | 2024-10-21 13:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c49f20b3-f58f-32b7-8683-24aa582cbfd1 | -12.5336 | -63.3003 | 2024-10-21 13:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e76d8fae-63bb-37c9-9cba-af2fca03e9ac | -12.5338 | -63.2812 | 2024-10-21 13:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7f5df04d-ed85-3d82-892f-ae76038d352c | -17.7069 | -57.4363 | 2024-10-21 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.2 |
| f9a4ef8e-5d87-3f39-bd47-a7bb6d9ee01d | -17.7266 | -57.4339 | 2024-10-21 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| eb32553e-be2b-3777-8a40-869d00e71ce6 | -17.7848 | -57.4885 | 2024-10-21 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 68e150dc-c91f-34da-81c9-d74a6348832d | -17.6871 | -57.4387 | 2024-10-21 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 4c60a384-7034-3f0b-a24c-20f8f5e60497 | -17.7065 | -57.4569 | 2024-10-21 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.7 |
| 58c0dbd8-7741-3d18-a86d-b54f59e15789 | -17.7259 | -57.4751 | 2024-10-21 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| ad0ae985-b3e1-36e8-afa0-46f19d3d0125 | -18.0247 | -57.2944 | 2024-10-21 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 6a371b42-a6e3-37df-b1ee-bd0a9ae19161 | -19.5477 | -56.6353 | 2024-10-21 13:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 4e2609ff-64ba-3621-8d47-fc88441c17ad | -12.4967 | -63.1874 | 2024-10-21 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 91a9e9f7-b388-380f-b828-626829f3c318 | -12.5147 | -63.3014 | 2024-10-21 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 5593f35c-f3ad-3bc3-80a8-172ffce2fb1f | -12.5338 | -63.2812 | 2024-10-21 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ba014eee-c725-3aa8-9c38-06f0e20025ec | -12.5336 | -63.3003 | 2024-10-21 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 849ba38b-5bc7-31b0-8bb4-508823894e51 | -12.5167 | -63.0521 | 2024-10-21 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0ea12a7a-fd44-3152-b60e-1f9c68511baa | -12.5168 | -63.0329 | 2024-10-21 13:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| cddbdac3-d52e-3ffe-86c0-8ca6e5cee8a1 | -17.7848 | -57.4885 | 2024-10-21 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 5ea15822-1e83-3b08-a375-c51557f777f4 | -17.7654 | -57.4703 | 2024-10-21 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 9a4d6e13-ff07-35f8-84ea-c92fd42ebb56 | -17.8045 | -57.4861 | 2024-10-21 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| b84fda29-594e-3efe-890b-915950756a26 | -18.0247 | -57.2944 | 2024-10-21 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| dde402d7-c294-31f5-b7b8-01152ca0ab2c | -18.0243 | -57.315 | 2024-10-21 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 3e81bcba-b5cb-362b-8da7-89954f19436b | -18.1028 | -57.3465 | 2024-10-21 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| c60b5556-f9ee-3c38-86c0-8994820bb26a | -18.1025 | -57.3671 | 2024-10-21 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| b72e5f66-84da-3081-9ffe-8107b13ce331 | -18.263 | -56.1021 | 2024-10-21 13:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.1 |
| ecdc671f-9f3b-3088-afec-27be917a9b57 | -19.5477 | -56.6353 | 2024-10-21 13:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 1a2f083a-736e-331d-baf8-c5a7d7ee4d57 | -3.3281 | -42.5018 | 2024-10-21 13:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 701a6df1-ec6c-36d4-9b89-b9093a1b3028 | -12.5167 | -63.0521 | 2024-10-21 13:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 122d7e2e-1d42-3db6-967f-85b07184e9c1 | -12.5168 | -63.0329 | 2024-10-21 13:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| e8784b74-6ac6-3e9b-92a2-6be71062f513 | -17.7848 | -57.4885 | 2024-10-21 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 85d6c288-c6dd-3282-84eb-7811be196986 | -17.8045 | -57.4861 | 2024-10-21 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| e71cce37-55bc-3615-a8af-ae18512a04ce | -18.0049 | -57.2968 | 2024-10-21 13:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 02da9ea4-84c2-3c77-89ae-747cddfc1960 | -18.0243 | -57.315 | 2024-10-21 13:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 6f84fe12-80e3-38d4-bedd-2b35c368a731 | -18.0247 | -57.2944 | 2024-10-21 13:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 91dd39cf-58ff-3f68-bcd3-0c4d6a6fb6ec | -18.2633 | -56.0812 | 2024-10-21 13:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 8ca8abec-f681-355e-9033-25127a15ce12 | -19.548 | -56.6143 | 2024-10-21 13:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| 33f343c1-3e05-3e55-b437-71bb67a60b72 | -19.5477 | -56.6353 | 2024-10-21 13:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 134.5 |
| 94161963-2de5-38a5-a35d-1608bc6ffb09 | -19.5473 | -56.6563 | 2024-10-21 13:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| ea8e767a-2236-379e-b33b-4d2f9e4c2bb1 | -17.2373 | -57.3079 | 2024-10-21 13:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 9a779f05-521a-3890-b067-b9c7934fc4a6 | -17.257 | -57.3055 | 2024-10-21 13:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 1b35be38-6f0e-3174-8d92-25ef9a1c46f8 | -17.8045 | -57.4861 | 2024-10-21 13:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| d2d62369-1c8e-30dd-89a8-e559ae38b8bf | -17.7654 | -57.4703 | 2024-10-21 13:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| f92d4aca-dc3c-3340-afb7-4f40a94bd238 | -17.7848 | -57.4885 | 2024-10-21 13:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| cd51cfc6-ac70-30b7-97e2-c2c113507ce9 | -19.5473 | -56.6563 | 2024-10-21 13:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.7 |
| e56823c9-4268-3abc-89b0-8138dce1a28e | -19.548 | -56.6143 | 2024-10-21 13:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 3c8acb44-7495-3070-a51d-3d49ccdedd15 | -19.5477 | -56.6353 | 2024-10-21 13:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 142.2 |
| e5c8858c-dadd-300a-b866-0c695a2e0e3c | -3.7465 | -44.4077 | 2024-10-21 13:55:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| bf63e22d-120c-365a-9f54-b17efac959c1 | -13.0323 | -62.4831 | 2024-10-21 13:56:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a9853fe7-6752-398e-aa99-170a484dfc9e | -17.2373 | -57.3079 | 2024-10-21 13:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| e0af285f-6039-3cfa-924d-1068ed638668 | -17.257 | -57.3055 | 2024-10-21 13:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| aefbd655-379e-312d-b9f1-72df9a3768aa | -17.8045 | -57.4861 | 2024-10-21 13:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 7cb37d85-f34b-37aa-98df-747f46afde9c | -17.7848 | -57.4885 | 2024-10-21 13:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| f8532738-cec3-3f74-84d9-f7f4fe51d774 | -18.1025 | -57.3671 | 2024-10-21 13:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 4ebd61a7-af7e-3ede-af8f-a94d1136bc81 | -18.1028 | -57.3465 | 2024-10-21 13:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 4ed7cfb3-4957-3d91-ae8d-a5ff56b156d0 | -19.548 | -56.6143 | 2024-10-21 13:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 468ea794-b99a-3465-aa8f-a5fa0e31df4f | -19.5477 | -56.6353 | 2024-10-21 13:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 150.6 |
| 283f4a68-b244-3fb0-be2f-816b58e87d0f | -19.5473 | -56.6563 | 2024-10-21 13:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 734e3b8a-8be5-391b-b4a8-0a997493b934 | -3.0763 | -44.3684 | 2024-10-21 14:05:24 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7bc4d0b0-fafd-3300-860e-ad96eadb2a23 | -3.0577 | -44.3692 | 2024-10-21 14:05:24 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| be101910-0da5-3494-80db-857d7a64d203 | -3.5956 | -44.7337 | 2024-10-21 14:05:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| aa29a926-ecbd-3223-8dcf-e66ba8d463ae | -3.7465 | -44.4077 | 2024-10-21 14:05:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 272a0798-6fcb-3ef9-b9c1-3049adc09f43 | -4.1828 | -43.2548 | 2024-10-21 14:05:30 | GOES-16 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 0421b85e-f0c8-3810-abf6-3e7a31a178ee | -17.257 | -57.3055 | 2024-10-21 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| bc1e354e-d22f-3c0c-9b09-9267b97ffbe1 | -17.2373 | -57.3079 | 2024-10-21 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 54d612e4-ac64-38aa-aca0-dbd78c77db87 | -17.2376 | -57.2873 | 2024-10-21 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 88e0acdd-3bbe-330c-ac08-6fc8e753f071 | -17.2573 | -57.285 | 2024-10-21 14:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 375d0582-9456-3833-af50-50a492792d32 | -17.7848 | -57.4885 | 2024-10-21 14:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| f5118806-4337-38c2-a7e1-eb8e3c4b6568 | -17.7654 | -57.4703 | 2024-10-21 14:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 98d1612c-85d1-372d-9d68-81c9b20a74e9 | -17.765 | -57.4909 | 2024-10-21 14:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 2e5ab959-aafb-3ea7-800b-2a0dc7306fc3 | -17.8045 | -57.4861 | 2024-10-21 14:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| fd644a65-188a-3379-a3db-806607dd28d8 | -17.9428 | -57.4692 | 2024-10-21 14:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 32a3171e-0a8c-3d88-8648-04965fa4a928 | -17.9827 | -57.4437 | 2024-10-21 14:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 9b24e0f2-bea5-33ca-8cd6-27beda54a0a6 | -19.5473 | -56.6563 | 2024-10-21 14:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 145.0 |
| fe6570a7-1e51-3427-8f35-2083cf92f607 | -19.548 | -56.6143 | 2024-10-21 14:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 127d1f88-75cd-3b06-a5a7-0dd8fed8579e | -19.5477 | -56.6353 | 2024-10-21 14:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 179.5 |
| fc26940a-a068-3932-8f58-7f3bccc067da | 2.4029 | -50.9353 | 2024-10-21 14:14:52 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ae69a276-da67-367e-82b5-8bb3f87c5f35 | -3.0763 | -44.3684 | 2024-10-21 14:15:24 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e17dc8fd-e92a-3122-a4c7-d60d71ef0cb1 | -3.7465 | -44.4077 | 2024-10-21 14:15:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1c891803-adf4-3f49-999a-6a6e81f562b2 | -3.5956 | -44.7337 | 2024-10-21 14:15:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0d53e31f-e98a-376b-bb45-b7828c659fd7 | -4.2871 | -44.4029 | 2024-10-21 14:15:30 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 66712e6b-3620-3097-aef6-029e1eb7393e | -12.4777 | -63.2076 | 2024-10-21 14:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| e23babaf-62fd-38c5-9d44-629ff7632385 | -12.4778 | -63.1885 | 2024-10-21 14:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 4465d996-866f-32fe-a908-62c01ae37741 | -13.0323 | -62.4831 | 2024-10-21 14:16:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a78ae760-90dc-359f-9d7b-a25497cab7aa | -17.2373 | -57.3079 | 2024-10-21 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 2fe3d4d3-6a77-3212-a354-ec63b616de07 | -17.2376 | -57.2873 | 2024-10-21 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| e85a17d9-8e69-36f8-a397-f472bef97eb6 | -17.2573 | -57.285 | 2024-10-21 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 46649edf-8630-3276-8d73-691922af04d1 | -17.257 | -57.3055 | 2024-10-21 14:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| b3f71c01-dcf4-3aaa-8f63-4ee7f18236a2 | -17.8045 | -57.4861 | 2024-10-21 14:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| add6775d-7774-3bb1-addb-86a155a98d6a | -17.7848 | -57.4885 | 2024-10-21 14:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 4675401d-756b-312b-a036-534bf084e024 | -17.9432 | -57.4486 | 2024-10-21 14:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 1bd7aeef-579f-3503-868a-45f06079b153 | -17.9428 | -57.4692 | 2024-10-21 14:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| f54ae3f9-6f6e-3532-ae4c-f3fe9a873102 | -17.9827 | -57.4437 | 2024-10-21 14:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| bb4c8258-c367-3f2f-a995-19bfb81cefa4 | -18.1025 | -57.3671 | 2024-10-21 14:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 4970e461-9f46-3828-bbe7-832e030e7055 | -19.548 | -56.6143 | 2024-10-21 14:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.3 |
| b2986db3-54a8-390d-9e7b-e488cf3ad650 | -19.5473 | -56.6563 | 2024-10-21 14:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 163.5 |
| 9707df59-7eef-3091-9ff5-3cfedea0c2ce | -3.1204 | -42.957 | 2024-10-21 14:25:24 | GOES-16 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |


[Clique aqui para ver as próximas entradas](README65.md)
