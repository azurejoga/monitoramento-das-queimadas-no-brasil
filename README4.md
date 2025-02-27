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
| 0d7b8f2a-eef6-3439-bcd2-5245ae78d766 | 4.52575 | -61.21252 | 2025-02-27 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13a21847-ec37-3e90-b789-6d0c04c789fb | 3.98048 | -60.05796 | 2025-02-27 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2977d5d2-03d7-390f-aed9-bb807b94f7b4 | 2.80698 | -60.79923 | 2025-02-27 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ae4eec-729f-320c-8cb3-06d9b362ac98 | 2.25278 | -60.28115 | 2025-02-27 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bbfc0d4-742c-3bcc-b1ae-00683885b542 | 1.21523 | -60.1209 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18983de6-4726-3035-806b-ce8e86c2bedd | 3.96584 | -59.76575 | 2025-02-27 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7013dcfb-e801-3b2e-8cea-7fa3a335156c | 2.37357 | -61.26096 | 2025-02-27 05:08:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f54f4a59-7e1a-3dce-88b5-ad2492c3aa13 | 2.91132 | -60.43892 | 2025-02-27 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5f07ed4-9297-349f-b6d4-65a241586d23 | 2.91023 | -60.43175 | 2025-02-27 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b2a68bf-fd63-3e77-afba-7349f0976669 | 2.67028 | -61.41195 | 2025-02-27 05:08:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e91a6184-a7f2-32ac-b723-d7a005b1370c | 1.88347 | -60.41979 | 2025-02-27 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0cd869f-64c0-3568-998f-a55edeaf481f | 2.91428 | -60.43114 | 2025-02-27 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6edd7ca4-4ef0-3055-9c6f-653f79464231 | 1.28123 | -60.10273 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3f4dcc2-18dd-313a-b43a-992ddabe3487 | 2.91077 | -60.43533 | 2025-02-27 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b14bd14f-e9d1-3b00-a8b8-490bae4967a6 | 2.90672 | -60.43592 | 2025-02-27 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ed6b1025-2c1c-3b38-985d-8bc22b07db73 | 1.2887 | -60.44054 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19e6d00e-7bc2-34a6-bbb3-0733455489d5 | 2.90726 | -60.4395 | 2025-02-27 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 860f3b58-f236-360e-aabd-1204741840ef | 1.28349 | -60.10068 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 715672c9-97c6-368c-ba6f-8f0ad618eda1 | 2.10768 | -61.82529 | 2025-02-27 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baae92cd-c240-355c-bef6-813017a1af50 | 2.04041 | -60.57788 | 2025-02-27 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 729a429c-2ba6-3fb7-a62b-c2e7ce8e12c2 | 1.29187 | -60.43486 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f69593ec-9725-395d-b367-de0edb3ec866 | 1.88399 | -60.42323 | 2025-02-27 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc213052-022c-34c0-a354-77f02682c30d | 1.31552 | -60.0677 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddde24d1-f2c2-31fb-90c7-51a4f8ed35da | 3.38435 | -61.21172 | 2025-02-27 05:08:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0548927-2ebd-3fef-bb9f-dc2224b5e6d2 | 2.10704 | -61.82103 | 2025-02-27 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f54a91d5-e7af-3b05-8d32-e31fca055150 | 1.12585 | -60.52765 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19b86e60-3b05-3db0-b9bc-f1fb1da43bfa | 1.31165 | -60.06828 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f34646b-86c4-3456-834a-b66c1f435f95 | 2.44651 | -61.31549 | 2025-02-27 05:08:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 750c9a64-d9e2-3a46-a231-32ef20fa7cc5 | 1.29108 | -60.42978 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8369ce77-cb7a-31dc-9799-59af92b19f48 | 2.25677 | -60.28067 | 2025-02-27 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9384f58-459f-3903-9c61-8326201a90e8 | 2.10639 | -61.8167 | 2025-02-27 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3a4504b9-2954-3a96-9c70-bc818e4c6369 | 1.77658 | -60.37655 | 2025-02-27 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26d2447e-994e-3a63-8ad6-16cbe52047eb | 2.72353 | -60.79582 | 2025-02-27 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f3d254d-1ad9-3339-b087-d85bd30a4ac6 | 0.82771 | -59.94823 | 2025-02-27 05:08:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb6eb05d-a86e-36c3-b947-09ebe29488e3 | 1.20509 | -60.13241 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16419350-63b4-312d-a840-bfed509c9669 | 2.11582 | -61.81959 | 2025-02-27 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a39d745f-384f-327c-ae5a-3e72369464b8 | 1.20434 | -60.12754 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a880c813-cbb9-318a-a172-eb7075a50bf3 | 2.67217 | -61.4086 | 2025-02-27 05:08:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36c43cd5-4584-3e82-8845-5af6aa040829 | 0.83874 | -60.60052 | 2025-02-27 05:08:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d02d1bda-21db-302d-bc4e-98f43cb28e4c | 3.96509 | -59.76068 | 2025-02-27 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fad7fb27-8d93-3fa2-a4b9-2f5486ef4800 | 1.27296 | -60.07419 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41a004c9-c72b-34b7-bc17-c976e7794771 | 2.4471 | -61.3195 | 2025-02-27 05:08:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 687aa640-5d98-3b2a-85b4-36e1f2f31afe | 1.29266 | -60.43995 | 2025-02-27 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41d9c389-70d4-3acb-9b4a-c948fc044d6d | 2.75859 | -61.42529 | 2025-02-27 05:08:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dfa347a-1e23-3e76-87e6-4b6cab1abd37 | -3.02562 | -54.59149 | 2025-02-27 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e680b573-4165-305d-b81c-b9492f2ade8d | -3.0222 | -54.59097 | 2025-02-27 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd1c492b-3e44-3673-964a-2b14462fc91f | -21.0473 | -47.78666 | 2025-02-27 05:14:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 35a64a9e-a60b-3166-b7ec-4e0e3282382b | -21.0478 | -47.78054 | 2025-02-27 05:14:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a66c3572-c31d-3b31-82dc-ac2a94053cb1 | -22.16455 | -47.13953 | 2025-02-27 05:14:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5829728-6f39-39e8-b96c-74bc78cec04f | -21.05438 | -47.78102 | 2025-02-27 05:14:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c830b7c1-6455-3e56-8be2-26e7d095dd68 | -21.05325 | -47.78004 | 2025-02-27 05:14:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| dada0e64-d3a4-30df-a5e4-317bc64be8da | -21.04621 | -47.78568 | 2025-02-27 05:14:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d0be0fc1-c2c4-3230-9c9f-6f8e47bab503 | -21.33085 | -48.5933 | 2025-02-27 05:14:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1086359c-31ca-3122-b816-0c669dc48828 | -21.0528 | -47.78607 | 2025-02-27 05:14:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ef972fba-103a-37ea-adcd-346a89f69d38 | -21.04667 | -47.77958 | 2025-02-27 05:14:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5dec4416-84c0-32c0-acec-e1ef16f2b45a | 3.54276 | -60.80254 | 2025-02-27 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b480f6d3-6a00-3386-84b1-2b8d32a1bfe0 | 1.27633 | -60.0778 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 504ab479-7249-3a93-82ad-a4160b29e999 | 1.28814 | -60.44081 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35cc520a-9af8-3bc0-9d38-7f6ba9a683bc | 1.31595 | -60.06853 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69e6d6c8-7d1a-3165-91b6-0a9563318dcb | 1.29096 | -60.43666 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63676f0b-ef21-33fb-b27d-a3479579f74f | 3.49281 | -60.33483 | 2025-02-27 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed134567-7f3a-3ef1-afee-d0127462f929 | 2.90869 | -60.43686 | 2025-02-27 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 478de89c-b171-3c21-898c-bb63cc46c189 | 3.59069 | -60.99796 | 2025-02-27 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8241912-70f3-3702-991d-5f0da9989131 | 2.25456 | -60.28124 | 2025-02-27 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 026f338c-2368-3ded-a9cb-ed446c2a8038 | 2.11574 | -61.82308 | 2025-02-27 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9275247e-ca30-39ea-af25-f2c577465829 | 1.20662 | -60.12674 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2b06409-a092-3560-9405-fb997449c8c6 | 0.74979 | -60.59372 | 2025-02-27 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04b19e0a-02b8-395a-9ae9-3e989a0f16fc | 1.21633 | -60.12144 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1306694c-2aa8-3ac1-a792-7615b986ddcd | 3.54221 | -60.79906 | 2025-02-27 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e3a5f12-35b3-3b31-b3ce-665a610bec16 | 1.71614 | -60.7234 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2767c5db-f77a-3678-bfdd-12fbfabf703f | 1.27574 | -60.07408 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5744fe93-be38-3094-ad8b-c1bf4ffcbadd | 1.29379 | -60.4325 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cb3ac05-cd63-33c1-8012-07965f4c4c34 | 2.37533 | -61.25934 | 2025-02-27 05:33:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddeefc77-8a5c-30a6-ab57-b87d6bc49695 | 1.29154 | -60.44029 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cdbbe90-b745-38a0-8596-d2619c4b2529 | 1.1273 | -60.5289 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4843444-6e05-3602-82fc-58e9fae9ae32 | 0.59326 | -60.465 | 2025-02-27 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d75cbc9-f9b4-3637-ae9b-3d0013e250ed | 3.38439 | -61.21442 | 2025-02-27 05:33:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b936cf5-90b3-36f8-8b83-09ddabaf92e8 | 4.22774 | -59.96399 | 2025-02-27 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc264def-c37b-3c88-8474-2a65d6ffcf24 | 0.83884 | -60.60255 | 2025-02-27 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17a956b8-86d6-3152-9bca-99cfef357c1f | 3.96822 | -59.76277 | 2025-02-27 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f3e69e5-5653-35de-80d1-0c05d63f757c | 2.10823 | -61.81727 | 2025-02-27 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6632c6a1-dad6-3f09-85c2-b1aeef70eab4 | 2.04354 | -60.57864 | 2025-02-27 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52d16790-81bb-302d-b2a3-cdcaf4add0f7 | 1.20721 | -60.13045 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa2dabb2-ec0f-3e95-8d76-56c37bf5ecb5 | 1.88481 | -60.41939 | 2025-02-27 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc0dfc81-a001-3eaf-94f8-4f3121e19219 | 1.33993 | -60.04199 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61210f53-06a5-3e54-b5c8-9123236dc614 | 1.77694 | -60.37633 | 2025-02-27 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41e931bc-dced-3360-b417-675dd2944ec9 | 4.21454 | -60.47479 | 2025-02-27 05:33:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aa02272-f72a-3da7-a104-06726fb4fe40 | 2.89039 | -60.25673 | 2025-02-27 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 824ac5dc-c617-3565-bdbd-9e93dddd6ab2 | 2.76089 | -61.42513 | 2025-02-27 05:33:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7047617e-6975-3d1b-a7cf-4c648da67932 | 4.23112 | -59.96351 | 2025-02-27 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c09e391-bc42-3292-84b9-02e73c8b3e10 | 1.88537 | -60.423 | 2025-02-27 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97f8063e-ed3f-3dc9-9a5d-8a89120019ac | 0.83028 | -59.94913 | 2025-02-27 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1492cdec-c88c-3a1b-9215-a776f220cea0 | 3.78529 | -60.15395 | 2025-02-27 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38114e66-78c0-3652-a89b-84c5376794b2 | 1.71277 | -60.72393 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dae0adb3-78c1-3294-a7a4-8ea8ad3fdcb7 | 1.77736 | -60.37695 | 2025-02-27 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4acb134b-4474-3ff5-a73c-315b9f673370 | 1.9365 | -60.38942 | 2025-02-27 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eac1f08c-6200-398c-a79f-ed7a8fd822d9 | 3.38385 | -61.21097 | 2025-02-27 05:33:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0079800a-2faf-300f-bede-c3b734027650 | 1.71333 | -60.72748 | 2025-02-27 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0a29e91-4224-310e-bbb1-aba246328dd0 | 4.18472 | -61.28975 | 2025-02-27 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b912d41c-935b-32c0-87f2-647dbe949c1f | 2.44885 | -61.31522 | 2025-02-27 05:33:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
