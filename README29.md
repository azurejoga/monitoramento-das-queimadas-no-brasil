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
| a2ac07f7-50f0-3459-ba0e-25e40b4dd94a | -17.08315 | -57.41942 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 49768903-e9b2-3960-a75c-9e6458860c0d | -17.0805 | -56.84291 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 61cc48b1-11e6-399b-959e-697dead81ffd | -17.07919 | -56.83299 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 869d7a95-42d9-3eaf-bcfd-2fd43426133b | -17.07788 | -56.82308 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| c3aa63a9-d19d-3cd9-a31a-4a60baa3c40e | -17.07658 | -56.81318 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 8042b5e0-f6c8-3cdb-a816-e3b3b0545743 | -17.07132 | -56.84425 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 2d110522-390f-36d2-913e-f98ef18d1f0d | -17.07002 | -56.83432 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| bf00ad56-f16a-3055-950a-eb1082fa2787 | -17.06871 | -56.82441 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 1ae9e74b-fb6b-378b-97d3-c360ac9990d5 | -17.06741 | -56.81451 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 32a72b3d-0ab3-3bf2-bb97-a996c9081e95 | -17.06084 | -56.83565 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| fde2b666-3848-3be1-a8c0-adca400f8cbe | -17.05954 | -56.82573 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| 27c5f36f-f166-3c74-870e-6f3e1bf52cfc | -17.05824 | -56.81583 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 4fe924ca-06c0-30b9-a2e0-ef6c6cd515b7 | -17.05694 | -56.80593 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 4bcb47df-61a2-3eec-9adf-b402179b7b9e | -17.05167 | -56.83698 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 1b11f129-eeda-39c0-aa5b-a411a0906303 | -17.05037 | -56.82706 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.7 |
| f3f637c9-51ed-3e1f-bab8-42e9bf0f2630 | -17.04907 | -56.81715 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| e6df8b30-cd8a-3fad-b620-035a9ecc5184 | -17.04249 | -56.83829 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 0f304a59-4517-3b91-a695-590da6945f84 | -17.0412 | -56.82838 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 05fe90cf-8c71-3e48-a21e-58edef3869c2 | -18.72965 | -57.29441 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 09d1a9b6-9ab0-3837-b0d9-b253d57a2111 | -18.72151 | -57.30662 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 5fd09a96-5d85-3db0-9c7f-a7a5c75e3a66 | -18.72012 | -57.29576 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 8d1890f0-ab22-3667-b52c-ebef50f7a7ec | -18.71872 | -57.28491 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 1eb4d333-05ed-3104-a384-ce6d7710429c | -18.71058 | -57.29711 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 99513abb-8285-3cc7-b6ad-8326049a74e3 | -18.70642 | -57.26462 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.7 |
| 48c1ebfb-4361-3d82-b611-b2c51d8dae37 | -18.6969 | -57.26597 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 2f51558e-1581-3397-ba77-43bc6a9903a8 | -18.69553 | -57.25517 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 9d3f6864-2e8b-3de8-84db-33fd3f27b184 | -18.68601 | -57.25652 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6e1dc212-d253-3747-b0c5-32d6b486ac4c | -18.6765 | -57.25787 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| e0fa80f8-87fc-3174-8e26-1cfad6010ee6 | -18.66562 | -57.24842 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 1e524691-1ebf-3788-a5d1-9d4b91a29819 | -18.65611 | -57.24978 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 96af64b1-6b5d-3f67-ad5a-3b938e4c1c89 | -18.64661 | -57.25113 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| ac33460e-6027-3b09-802b-eaf6a989bccd | -18.64247 | -57.29572 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 8a0f0b07-0f7a-3b44-8acb-3356ebb72b18 | -18.63844 | -57.26327 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.3 |
| f4e4cafc-5ae4-3d69-9050-0e7e7831d758 | -18.63745 | -57.29173 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 2552dd23-7fda-39b8-b133-f2958ba6203c | -18.6371 | -57.25248 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 553ac966-5dde-35c1-a8b5-8ff154d98b42 | -18.63466 | -57.27012 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 59817be3-ed76-3731-990c-420a340b12ab | -18.63326 | -57.25933 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 73332b86-2d94-32c3-bf89-9f37ef259496 | -15.66862 | -59.44499 | 2024-10-07 01:30:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7bc0be8b-36d7-331d-b3dd-891a162d2917 | -11.92246 | -50.09576 | 2024-10-07 01:32:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4b0193dd-d292-3ee1-ac32-89308b7ccbb2 | -11.86037 | -50.10642 | 2024-10-07 01:32:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 83b749f7-1717-3bb5-ba66-a542881469f3 | -13.59304 | -50.31728 | 2024-10-07 01:32:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| f0e2be4e-5fb9-35c7-82cd-b6e01865dcde | -13.58123 | -50.31936 | 2024-10-07 01:32:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 8a6081e3-2bd8-3b21-b089-3afd2be63842 | -13.57841 | -50.3024 | 2024-10-07 01:32:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e2ac325c-c9c9-3331-bb5a-c3317d40e779 | -13.57249 | -50.30986 | 2024-10-07 01:32:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 7533ae13-c323-3b94-b1ff-b9d87e71f04c | -13.2764 | -50.63563 | 2024-10-07 01:32:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e41a44b0-963c-3fb7-9e8b-fb1054c240ec | -13.26481 | -50.63765 | 2024-10-07 01:32:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 17c3180c-2872-34d5-80d6-4aacf344342c | -11.29106 | -51.4053 | 2024-10-07 01:32:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 85d21898-8012-38df-ac4f-fcd3e2bddee5 | -11.28864 | -51.38997 | 2024-10-07 01:32:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ce343345-7051-3f51-9bbb-a09e26e1a0bb | -11.27729 | -51.39185 | 2024-10-07 01:32:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| eee4d10c-55f1-3546-bad9-e20858eb2d7e | -11.26595 | -51.39373 | 2024-10-07 01:32:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| bef0b1a8-2224-3547-b62b-f2bd21412b37 | -11.26349 | -51.37836 | 2024-10-07 01:32:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 48a6f806-7678-36ee-85c8-c593d2ed54ad | -13.31832 | -51.32559 | 2024-10-07 01:32:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b9ffbda1-8d4d-372a-9892-823c35fe4944 | -10.95187 | -52.39225 | 2024-10-07 01:32:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a6b6585e-8a81-3e27-8524-317aa02ae7f0 | -14.80926 | -53.89815 | 2024-10-07 01:32:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 97b172b9-7849-39de-a92e-f2dcdd21baf3 | -14.33941 | -57.59388 | 2024-10-07 01:32:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| bfba441a-e6a1-3bce-b977-6a97fd67ca94 | -14.33813 | -57.58422 | 2024-10-07 01:32:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5ba0aa3f-edb8-3ecf-afea-0f9a1278c9a3 | -14.33015 | -57.59496 | 2024-10-07 01:32:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c0366820-b500-3e80-90b7-7a1ec5a299f3 | -14.32885 | -57.58515 | 2024-10-07 01:32:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 52323f92-f4f9-3ad1-b640-a0d32b4a2113 | -14.32758 | -57.57553 | 2024-10-07 01:32:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 337530c5-52b4-3329-96a9-f2306c3ec204 | -14.92587 | -57.93134 | 2024-10-07 01:32:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2d060424-ef0b-3b90-a54a-c868b960110d | -14.95868 | -57.92105 | 2024-10-07 01:32:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 12ea18f4-9315-3a29-aec5-8828f915d38d | -13.14459 | -59.70124 | 2024-10-07 01:32:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d9a29dcb-2d8b-3e5d-8841-da96b332d6fd | -10.34259 | -64.26017 | 2024-10-07 01:32:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 7c397b86-0659-313d-a80c-b0cf22dce3d0 | -3.54064 | -65.02771 | 2024-10-07 01:34:00 | TERRA_M-M | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e820f30f-e641-3ce7-8924-9c5200639cd1 | -3.03805 | -53.04598 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 57280d80-f2d1-3f95-8d8f-9fd2b3e9064d | -3.03493 | -53.04074 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9eb70ecb-d8dd-31e5-bdb8-3fe907b5c9b6 | -2.87977 | -52.91375 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 3266d43a-3daf-30c5-a9b2-58ed8c493f34 | -2.87741 | -52.89747 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| b216786d-df4b-31ac-bce0-298b5d1dc057 | -2.86806 | -52.91529 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| f88835a0-b284-30e2-82b7-6e76984e5e0f | -2.86569 | -52.89905 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 0b687947-b24c-3ae7-9fbf-c775c64acfcb | -2.77433 | -53.21362 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| e1035dde-23fa-3b12-b748-cc5200150f20 | -2.77432 | -53.22247 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b874e1f2-898b-38b3-9c47-d7ddb7de93bb | -2.77211 | -53.20765 | 2024-10-07 01:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| e1a3a353-d5d9-3feb-ab6e-9858dc92d30d | -3.74199 | -59.33439 | 2024-10-07 01:34:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| aef3f365-1339-33f3-8c14-3ce51c88cc6c | -2.22473 | -53.70812 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| f6b10bb2-67d0-3826-bad6-ac842f9c5d4e | -2.22263 | -53.69369 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 236bf2eb-c09d-33e8-b3ee-ee24be94f4fc | -2.22053 | -53.67935 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0b95e80e-02a1-308b-ae1d-ebf0200afeff | -2.21363 | -53.70962 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| beb0952c-9282-37c6-a1aa-e6d94112ffab | -2.21309 | -53.71553 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 56b816d4-e24c-3ab8-acee-d2a97a603b50 | -2.21151 | -53.69519 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0a70889e-4ff7-3932-8b55-957cc66f6c90 | -2.21107 | -53.70103 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dec6a952-a8d3-3320-9109-8b065c9db10e | -1.12087 | -53.6283 | 2024-10-07 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8be1cc58-a983-3273-924e-ea2d8cf1a870 | -1.03913 | -53.53561 | 2024-10-07 01:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d221033f-5acc-308f-be98-ed5ec7eda03a | -1.03362 | -53.74022 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 1d8a969a-9d9c-3c3f-98d5-bf662b53d8ca | -1.03139 | -53.72482 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| fce8ac50-554e-3363-aad6-09280ae266af | -1.02117 | -53.73343 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7d336454-a0b3-3077-b540-c38f748dbc8b | -1.02019 | -53.72703 | 2024-10-07 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 32000e30-11a3-3151-bbee-d5e96bece862 | -2.81195 | -54.35783 | 2024-10-07 01:34:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b10a99ac-3134-363a-abd2-79d6dc7d6184 | -3.74073 | -59.32515 | 2024-10-07 01:34:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1d060b49-bc1f-3e06-82cb-c157330aa674 | -1.0182 | -53.739 | 2024-10-07 01:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 21f19da9-a6e9-3389-990b-01d2dccfafd2 | -1.0365 | -53.7389 | 2024-10-07 01:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 390cbd2d-cc39-3dff-9c3d-bdfbf1e6b6a6 | -2.2113 | -53.7029 | 2024-10-07 01:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 40ae50e1-663c-39ec-8dbb-22ffeef773bc | -2.2297 | -53.7026 | 2024-10-07 01:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 1a544722-3b0d-3a08-badb-3be1bb05aec2 | -2.857 | -52.8993 | 2024-10-07 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 8a5e46bb-9cd9-39db-a94e-9781de09be84 | -2.8753 | -52.9192 | 2024-10-07 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 7aa47f55-cf1a-36be-83bb-86d3cc6f8bdf | -2.8754 | -52.8989 | 2024-10-07 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 207.7 |
| 2aff2498-4998-3c26-afca-7b77d0b7375c | -2.8569 | -52.9197 | 2024-10-07 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 6e6f4c89-62cb-3faa-af87-53f47c8cd9d3 | -2.8937 | -52.9188 | 2024-10-07 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 5ef533ad-e4eb-3824-aea7-22c962aa4f62 | -2.8937 | -52.8984 | 2024-10-07 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 9e425a86-4fa9-31fe-8fba-81ec4950eb37 | -3.5381 | -65.0229 | 2024-10-07 01:35:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |


[Clique aqui para ver as próximas entradas](README30.md)
