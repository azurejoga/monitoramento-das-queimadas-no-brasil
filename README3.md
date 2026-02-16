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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4cb618c-627f-3b36-84f2-8c7ab0c6567d | 4.19529 | -60.44802 | 2026-02-16 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd23355b-5416-3984-96d0-9545c822a09d | 3.84378 | -60.89571 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9d897e8-60c2-3cd3-8028-f5c94ee8e5f0 | 2.66501 | -60.16143 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fa1b500-5efa-3aef-988e-d3669707c4ca | 3.93723 | -60.49815 | 2026-02-16 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d29e27b6-ad9f-322e-aded-a3890f552c23 | 2.43187 | -60.23737 | 2026-02-16 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a44d208-df95-3f7c-bd54-71897a1a22a7 | 1.12948 | -60.52243 | 2026-02-16 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c803b89-dbca-3f83-9e25-0fa94ed98cc5 | 2.6667 | -60.17222 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e79eb27-b145-3635-84b9-7eb004634729 | 3.84028 | -60.89622 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ecaf2826-74e7-3053-8323-8d9ac3029883 | 2.76607 | -60.31233 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 84703860-4520-3df7-8e9b-3cee5731a6fc | 2.71791 | -60.19007 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77818c88-e115-37f0-be28-402e857fa20d | -5.28188 | -56.01839 | 2026-02-16 05:22:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f452ef8-7445-3266-a223-b3aafbd60869 | 3.84728 | -60.8952 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c7ff493-8b65-380a-a9c4-c6738ecb28c0 | 2.71453 | -60.19061 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1d1247b-b4c7-3641-aa2c-99d90b2be0f0 | 3.85138 | -60.89856 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 523a15dc-3731-39cf-9b58-6bb5cf4fe8b1 | 2.76946 | -60.31181 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| da13437e-41b9-354e-9594-1e403e62f7bc | 2.76663 | -60.31598 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 38af2da0-3794-36eb-b153-6b80c724cbc9 | 3.72077 | -60.94856 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7399f62b-3354-3a64-8f27-ee66ede7a0b0 | 4.1984 | -60.85037 | 2026-02-16 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f77bbfc-cd60-3485-b96a-d6895834cf91 | 3.85198 | -60.90244 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 898dea6d-e3de-3f92-8864-90cadd3ed0bc | 4.19243 | -60.44735 | 2026-02-16 05:22:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33842585-af86-335f-aba0-870db96cb0c6 | 3.84788 | -60.89906 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76951ac6-d705-3e6c-9a4b-1759cd865ee9 | -5.28576 | -56.01894 | 2026-02-16 05:22:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d50a29e7-1a49-39d1-83f6-cae9e62b61bb | 2.65602 | -60.17021 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6a5013c-dd64-3bac-a9d3-2dbdfd417b77 | 3.70479 | -60.91521 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15e6ed59-2e6e-31e2-9ae4-8cf0a7faa10b | 3.72199 | -60.95636 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8fd6455-60d8-3f0a-b2d6-0599e423abb2 | 3.82743 | -60.88239 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7423f6b2-90d2-385d-86d5-3f590c5925c3 | 0.93809 | -59.41911 | 2026-02-16 05:22:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb34daa-8a25-3b76-af70-ac343b27f703 | 3.83152 | -60.88572 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6bf7b35-1816-385f-b273-a46678a8442a | 1.85026 | -60.33418 | 2026-02-16 05:22:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 867feb18-83dd-39c9-86bd-c18d5751ae3a | 2.66332 | -60.17275 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9cc6bac-3ae4-3da7-9a6a-2288beb4f1b8 | 0.93863 | -59.42254 | 2026-02-16 05:22:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aba3a6d6-6808-31d7-bffa-bfaa5c888644 | 2.65658 | -60.17381 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1e69bc3-6abb-33fd-ac7a-e1395af00117 | 3.83678 | -60.89672 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9cc7c8b-511b-32b9-bc47-0f3d9bd1fa1a | 3.64351 | -61.05253 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f67e8ec-94cb-369e-9fa5-17520dc81ec9 | 2.65546 | -60.16661 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dcaeae4-8fa7-3e7b-8137-ee5e98ff36b3 | 3.82615 | -60.88168 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b5f170e-ed68-3571-9dee-f71a8716aa8d | 3.25254 | -60.44487 | 2026-02-16 05:22:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb740de4-4b47-3444-af93-5d917c1758ca | 2.66614 | -60.16862 | 2026-02-16 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 483fc5c3-627a-3e08-9341-02713522359e | 3.71666 | -60.9452 | 2026-02-16 05:22:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58b3b7cc-2f23-3a20-a6a6-450d8793dc03 | -17.53138 | -57.27562 | 2026-02-16 05:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 887331ca-7804-37c5-a8e8-5a720c15933a | -17.53244 | -57.27301 | 2026-02-16 05:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 94302a52-4e60-325f-8c19-94054366d829 | -18.9727 | -52.93319 | 2026-02-16 05:27:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4913304-4f94-3695-b6ab-8707c5eaf370 | -21.15357 | -53.21842 | 2026-02-16 05:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 497a8bab-16d0-339e-b188-968cfdd31af2 | -18.97391 | -52.93243 | 2026-02-16 05:27:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 717d8e15-5f22-3e92-b3d7-1dcb97234e4b | -14.21267 | -58.13948 | 2026-02-16 05:27:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69d3999b-6015-3bf8-8a20-08caa70bbc9a | -18.97432 | -52.92812 | 2026-02-16 05:27:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8325d8e2-fb01-370c-9ecf-265fb5ff6936 | -17.5319 | -57.27712 | 2026-02-16 05:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 017868e0-2df0-30b2-a691-bec6f851eb18 | -17.53563 | -57.27621 | 2026-02-16 05:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1364703a-6c01-3f89-9b23-cb4adf709f98 | -18.97315 | -52.92889 | 2026-02-16 05:27:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 073a2634-0913-34ec-8cf5-acf4e066557e | 2.76565 | -60.31139 | 2026-02-16 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 184db1d8-8d68-3c9b-a560-bd5f00d346d7 | 2.7664 | -60.31582 | 2026-02-16 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 28.5 |
| ae463eac-f84f-3099-9092-2efcdadf40b0 | 2.80907 | -60.82047 | 2026-02-16 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9d575fc-6e80-3cd3-8183-a1da1bf5f9fd | 2.80903 | -60.82145 | 2026-02-16 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09fa50f9-2458-3f7f-99bb-215707dc46ce | 2.6659 | -60.17072 | 2026-02-16 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b99597e-4fda-3357-b24b-91bb09406997 | 2.76482 | -60.30078 | 2026-02-16 06:48:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 266889d9-4914-38ab-9d90-a5caf018265d | 2.76775 | -60.32069 | 2026-02-16 06:48:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 242c69f9-1ac5-30ff-883a-89b2c597b127 | 2.7634 | -60.315 | 2026-02-16 06:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 53714612-593e-3c03-bcc2-72ab9c3c03bc | -17.53648 | -57.26918 | 2026-02-16 06:54:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 889e4373-d961-3da0-b880-d094b28f04f5 | -29.41359 | -52.42267 | 2026-02-16 06:56:00 | AQUA_M-M | SANTA CRUZ DO SUL | RIO GRANDE DO SUL | Brasil | 4316808 | 43 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 139d1d9c-23f9-3b6e-9b19-f1186f549ae9 | 2.7634 | -60.315 | 2026-02-16 07:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ec98c778-5c39-39d6-9878-96a5b5ec200c | -12.2454 | -44.23534 | 2026-02-16 12:12:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c54c8cd6-c971-35ef-aac2-577d8843e073 | -12.07715 | -45.30763 | 2026-02-16 12:12:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| bc38fb35-9fc8-3070-962f-4764daf13dcc | -22.34518 | -47.15538 | 2026-02-16 12:14:00 | TERRA_M-T | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 047929e0-d97a-3b98-bb2e-4300cd6c4891 | -22.84826 | -48.65089 | 2026-02-16 12:14:00 | TERRA_M-T | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ddb975e3-d456-3393-a7ac-25df8bd378ad | -17.9931 | -46.90158 | 2026-02-16 12:14:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1cbe06ba-b447-3540-bb82-453c8b02a2cf | -22.84975 | -48.63847 | 2026-02-16 12:14:00 | TERRA_M-T | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| bc5d4099-39a2-3266-aecb-2ed6709c5321 | -19.59377 | -46.93919 | 2026-02-16 12:14:00 | TERRA_M-T | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 32b825cb-56bc-3e46-9396-383192faef4c | -13.93275 | -44.09824 | 2026-02-16 12:14:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| cf0bc6e3-bbae-3eac-8442-83c01ff28f29 | -15.77346 | -46.45643 | 2026-02-16 12:14:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0fd5ce9f-ff8d-30f6-b131-f2766f10c80b | -21.89729 | -45.58617 | 2026-02-16 12:14:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 1f64e9eb-b26b-32f3-8c78-63322381ec57 | -13.93561 | -44.10559 | 2026-02-16 12:14:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 6722c373-82ce-3122-9c59-3308a542dc21 | -22.74327 | -47.56935 | 2026-02-16 12:14:00 | TERRA_M-T | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 83fa5806-9642-36c9-957e-96e7dc6aab51 | -22.43223 | -46.57327 | 2026-02-16 12:14:00 | TERRA_M-T | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 34414518-c166-3172-8a10-a2a7b608e8b0 | -17.82246 | -45.35197 | 2026-02-16 12:14:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3aa1c3c3-c36f-3fa7-a968-f061633a5990 | -22.07914 | -46.57389 | 2026-02-16 12:14:00 | TERRA_M-T | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 31a93e32-066f-3fa4-a79c-8fa3f7691d64 | -16.23702 | -47.88473 | 2026-02-16 12:14:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 35281b1d-5f68-32ad-9fe4-2aca8b797eb7 | -21.17709 | -44.8694 | 2026-02-16 12:14:00 | TERRA_M-T | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 6b5b452e-0d81-3037-976e-3791a5e9a52b | -23.26245 | -46.59058 | 2026-02-16 12:14:00 | TERRA_M-T | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| cb080a03-d940-31de-95e0-3e75b6d2a60c | -20.78395 | -46.52642 | 2026-02-16 12:14:00 | TERRA_M-T | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8d2cbe7e-f631-3ae0-9389-957670ff20aa | -20.78221 | -46.54227 | 2026-02-16 12:14:00 | TERRA_M-T | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 099f8025-ea0b-355c-9c84-711073a9abe3 | -13.93502 | -44.07957 | 2026-02-16 12:14:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 19fa52a8-dc1a-3a83-8eed-bb35974dc5b6 | -13.93783 | -44.0861 | 2026-02-16 12:14:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 5dee1981-31d3-31ca-ac0a-e17e8242e265 | -23.35665 | -47.51078 | 2026-02-16 12:16:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 1f9f1292-3c7b-36e0-91dd-4b89412208b9 | -23.4082 | -46.82626 | 2026-02-16 12:16:00 | TERRA_M-T | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |


