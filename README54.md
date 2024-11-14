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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19f12af6-80c7-3441-8c7f-08077803cdea | -17.59008 | -57.54496 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e460afb5-a157-360f-a120-e04b73195adb | -17.57913 | -57.55839 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 96413509-ca21-3d33-ac5e-a37ec8dc84ef | -17.25778 | -57.48069 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 601804f8-37a0-3899-8a04-f6cf53266ec1 | -17.70271 | -57.5367 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| fd10e903-064d-3da7-8f28-a6e42ff79352 | -17.58919 | -57.47497 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a85bffe0-e7f9-3ffb-bd45-6f73334e0aa5 | -17.5938 | -57.47558 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 032d6e92-d329-3d0e-9c3a-4bac3b351f37 | -17.24119 | -57.46363 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7fd952c7-5820-3fd9-b204-93756526b2a5 | -17.57949 | -57.43854 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 27555a30-04b9-3911-9245-c3610d0a941d | -17.2492 | -57.4746 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4f684ec2-e872-38f4-9480-beafe36de4ab | -17.70791 | -57.53239 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 9311dba8-f686-3355-be17-d123ab30ebac | -15.87789 | -59.29689 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 810dc6e0-eb2e-3c90-aaf4-5eb11017710c | -16.07323 | -59.71176 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfd19480-a911-3a92-859a-eea86192b556 | -16.09925 | -60.10028 | 2024-11-14 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 398579da-8efb-3945-8650-d7485a6ee539 | -15.86948 | -59.29891 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7aa9d115-0c18-3bd7-96b9-36bc4bd84459 | -17.58549 | -57.54436 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6f1a4926-58a7-3209-8535-505cbfd1424d | -15.93145 | -59.27494 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ab4a9db-811d-39bb-a10e-9c6c5c9ff94f | -17.58411 | -57.43914 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 39bbd29c-8bcf-3c39-b905-5201b62f14d2 | -16.00764 | -59.3923 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5794e086-5817-3a51-8855-11bae4f06dd7 | -17.57231 | -57.53765 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ac5b520b-f195-3338-8011-2182ff42d39b | -17.25037 | -57.46484 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 144016f1-58f4-39a8-aa0c-e560ebea00d3 | -15.91353 | -59.28734 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8c647e4-550c-334f-aba7-722a2c005ec4 | -17.59841 | -57.47618 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| a1873ae2-799d-34b7-a7b6-911a5a411ce5 | -17.56831 | -57.53216 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 17fe1507-26b4-36c5-b31a-ae7df5c1a54a | -17.59289 | -57.56017 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8de70094-a619-3558-bb63-7fc0f7018345 | -16.00783 | -59.40162 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 428912a0-fdb9-3447-afb6-9300ef71e813 | -15.90024 | -59.28222 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd1fbc31-25b5-3375-a20b-303364a432e6 | -17.57631 | -57.54314 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 23e8c49f-2e74-3af3-b90b-cf34ec841761 | -17.58431 | -57.55411 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| df1ae034-f3a8-303b-a66c-c7ae77e1889f | -16.10374 | -60.096 | 2024-11-14 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f87ed80-8354-3495-9816-5952a7509e10 | -17.26755 | -57.47702 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c8f35f06-1754-3e27-8958-422b937f1bc4 | -15.89785 | -59.314 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7757c8a1-2c75-3661-986b-88a2eb79e1e3 | -17.61761 | -57.54854 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ee6a3927-3397-30bf-b629-7280e028e524 | -17.56889 | -57.52727 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| cd2464b3-9e38-3052-95cc-aeea8a0ee53b | -17.6337 | -57.4474 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2091dd14-c098-332c-be96-767c7415f28b | -14.49916 | -56.91641 | 2024-11-14 05:29:00 | NOAA-20 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 722b5bb6-afb0-3c0a-baa3-80536fcf0e8e | -15.87438 | -59.29274 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2213829e-af8c-30da-aa82-d7adbfff98d3 | -17.59781 | -57.48112 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 59d4d9ed-682d-3dc6-a819-78fd63908ccc | -17.25378 | -57.47521 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ca9a1ffd-9070-3f74-b3ae-a05e96238137 | -17.2572 | -57.48556 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 44e66594-570c-3a6b-ad6d-aac2f0ab441f | -17.60325 | -57.55161 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 00e77bed-66fc-34eb-9fcb-692de341a39a | -17.36045 | -57.44075 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e6e550e0-79a2-39e5-98dd-13158f8cdf1d | -16.94954 | -57.63771 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 215b3d42-936e-3fd2-800a-7b85d5d1f973 | -17.25261 | -57.48496 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9935da26-8ac4-32d9-beb1-2c53763d32a2 | -15.41027 | -58.61045 | 2024-11-14 05:29:00 | NOAA-20 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fde87c51-3577-3f07-924a-b616273375d4 | -17.2406 | -57.46851 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f2f140a8-135b-3cf7-ac34-e528aa54889a | -16.94837 | -57.6471 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c64f8521-80e1-3249-bf42-201ee74baa00 | -17.588 | -57.48484 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 08ada0c3-8b48-30ed-b3ff-baf91d6e8f93 | -17.60242 | -57.48171 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| c922e06e-bb3f-3905-8d70-f04eec505621 | -17.63077 | -57.55523 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9da39dd8-0321-346d-9243-735d9ecf7870 | -17.70331 | -57.53177 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 1a470c91-eb8d-3b89-8756-6e9f244ee3b7 | -17.58889 | -57.55471 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2d196577-1ae5-33e3-a547-eda3e53a8aed | -16.10307 | -60.10083 | 2024-11-14 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db4b0d71-a0c5-3bfd-94ee-39c071d748f7 | -17.2093 | -57.23054 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7522fb09-f4f4-38bc-903b-ea18ee0ee536 | -16.00835 | -59.3869 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cab6725-8ef7-39a9-8b53-7ec471a89239 | -17.57749 | -57.53336 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| a1091219-307d-3e2e-83af-eebc638e7bd4 | -16.0732 | -59.70992 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d72ecaf-833f-3ca1-9c56-ecd3a91ec7ca | -17.59694 | -57.41046 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| af8513ff-066b-398b-8a12-f2edcd80b316 | -17.24519 | -57.46912 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5df8648c-4e59-31af-b45c-cc8bc3e3d6b7 | -16.94895 | -57.64241 | 2024-11-14 05:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| eab1f195-0a24-34c8-9ef3-c1e67f31a66e | -17.62678 | -57.54973 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c0112ff8-ead6-30e9-9b2d-59bfccead9b7 | -16.24178 | -58.93028 | 2024-11-14 05:29:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1efe4ba6-1b44-3af1-bc4f-0830a3726888 | -15.87487 | -59.28912 | 2024-11-14 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfccaef9-3a26-3701-9f47-153e3b1dbe37 | -17.59023 | -57.50512 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f64031f6-59fc-306e-831b-a35e5606320e | -17.59467 | -57.54556 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e9c494f0-6ddb-3208-98b1-291e81a05a69 | -17.57349 | -57.52786 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 73487c0a-53c1-3932-ab97-b40afd62ead9 | -17.61242 | -57.55283 | 2024-11-14 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 5759883f-dd70-384e-9326-88db52b1b04c | -15.23275 | -60.2337 | 2024-11-14 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cacda3dc-10b0-3c3c-b2f6-7ab373ba7dd1 | -1.643 | -53.2677 | 2024-11-14 05:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bbde2662-9367-3dec-ac7e-2b394eeb3b83 | -1.8106 | -52.1652 | 2024-11-14 05:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 50492967-0d28-3335-8864-5f97eea615cb | -1.6246 | -53.268 | 2024-11-14 05:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e5891559-0266-3411-bef1-2975abda5535 | -19.57874 | -54.88972 | 2024-11-14 05:31:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5482d2e9-98e5-304c-a2c2-444c73e8454b | -21.55388 | -55.825 | 2024-11-14 05:31:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ac6f2e3-f738-35c3-aa33-1a2a91ac97f2 | -21.908 | -56.46048 | 2024-11-14 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 000a5961-b7ca-33ed-9c8d-2fe56563d972 | -21.8471 | -56.4367 | 2024-11-14 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b419e96-087e-3f16-befb-4864b372f658 | -21.84677 | -56.43999 | 2024-11-14 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eda53b2d-732a-3487-8acc-ab0ef81bd830 | -23.96396 | -54.04877 | 2024-11-14 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1b846cfd-b725-3467-9949-408d0cb81877 | -23.95777 | -54.04819 | 2024-11-14 05:31:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 105881eb-9331-39e3-b965-2eaffe0928d0 | -19.57835 | -54.89361 | 2024-11-14 05:31:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 082f96b6-2e33-3518-a512-b51f197516a2 | -21.90765 | -56.46389 | 2024-11-14 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11ff0286-824c-325c-aab1-7d4b145ceeb9 | -21.55072 | -55.82502 | 2024-11-14 05:31:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a4a1de7-61d0-309c-aa69-b040b54b5417 | -21.90879 | -56.4612 | 2024-11-14 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13ef0b1f-9501-3cc0-87b7-2307d2184153 | -21.90359 | -56.4605 | 2024-11-14 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1727513e-a252-3115-888d-12adeab8fbb5 | -21.85199 | -56.44054 | 2024-11-14 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eb909ab-0529-389d-8e42-897eaf6a8f2a | -21.9028 | -56.45982 | 2024-11-14 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8494f90-1462-38bb-8ff0-e62195e59853 | -2.89239 | -46.85767 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9c3a1641-99c9-3c39-9f5f-a0dcd2dc6237 | -3.3024 | -43.50332 | 2024-11-14 05:35:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 116942ae-58ee-3976-bdb2-475e21f99b26 | -2.67629 | -46.81442 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c1b643a-cf2f-344f-ae55-19c922d72dcd | -2.8314 | -46.64986 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8c57efac-6cb9-3533-b1a1-39f852facf30 | -1.68565 | -48.46008 | 2024-11-14 05:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6f52e9da-a36a-3860-b3f5-4d36a599f381 | -1.3878 | -51.56192 | 2024-11-14 05:35:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6b387a7b-b9a5-3c52-9e10-12cc95b2c9c3 | 0.84782 | -50.20778 | 2024-11-14 05:35:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 74b0395a-06f3-3c2b-8b6e-82f2e3d821da | -2.89094 | -46.86747 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 86bbcb6a-895a-3428-87a5-3a9fa5619a56 | -1.79883 | -52.16566 | 2024-11-14 05:35:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| f1357dfb-fe55-36ce-b627-ada234615abe | -1.797 | -52.17759 | 2024-11-14 05:35:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cf7cfd02-51f8-3b66-b463-ad8172d51be4 | -1.39424 | -51.12313 | 2024-11-14 05:35:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| c75c8814-1fcb-3a7f-8d4e-5dddd0080a12 | -3.3221 | -44.07678 | 2024-11-14 05:35:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 19fb9ad2-eb9f-3f1b-8d34-e62979ddc22e | -3.32431 | -44.06171 | 2024-11-14 05:35:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d067d83e-3348-384d-8080-1f190b5ca6be | -2.67487 | -46.82412 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ca2d0379-168e-31cf-aab3-870924420681 | -1.38784 | -51.10089 | 2024-11-14 05:35:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 02aa5188-f83b-38a0-a29c-19dd429da00f | -2.82052 | -46.65852 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README55.md)
