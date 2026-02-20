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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83a91755-ad5c-3041-8e3e-6adf9e9fb043 | 0.45746 | -60.40526 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9f45750-5684-3e42-a752-9063b37c527d | 2.53937 | -60.72201 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8aefdff2-4991-3c28-af35-3a023cfd025b | 1.15416 | -60.33033 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9a2dfeb-e8df-39ed-bc0e-de7c80b88784 | 2.56303 | -60.56467 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 5cbde98c-98bf-33ea-a7ca-de6c0050669a | 2.559 | -60.56147 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 0ed6a387-ae03-3910-bb29-c00dfd761b13 | 0.45408 | -60.40578 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b11591a4-9435-326f-b52f-7ef4b681d58a | 2.54689 | -60.7247 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea9b510-231f-3208-8868-8d42d65bdba7 | 2.53591 | -60.72254 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bb97d5b-f4ce-3ce7-b5cd-7b8b4d14f37a | 1.36681 | -60.37164 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d143159e-89b4-338b-93de-cacaf7e6075b | 0.98072 | -60.42718 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b46648c-49db-3c12-9c95-b0a9f678d90c | 1.12881 | -60.52296 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5d6ba96-110f-32c8-b473-0f02e4282ca5 | 0.46309 | -60.39705 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72fa0da5-f579-3d2d-b74d-94571b538e71 | 1.15586 | -60.34111 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3249bc3d-bcac-3e61-a9a3-91a251a8dba1 | 1.27492 | -60.40767 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7a313a6-fc9d-3a97-8e8c-cc1704f0d9ad | 2.55842 | -60.55775 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f3a57b4-04a9-3ea4-9855-04bc809fc4f8 | 0.44958 | -60.39916 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 57e78e37-a94e-332d-af33-ed6ccdf3bf48 | 2.55498 | -60.55827 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 931fbfa8-e764-3981-8e3d-39c9b2132ed3 | 0.4507 | -60.40631 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65556be1-5f61-339d-9008-79abb4bfd9fe | 0.96123 | -60.23926 | 2026-02-20 05:27:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcd86a0d-ddab-3d23-943e-e3811fc47b98 | 0.4569 | -60.40168 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b010c96a-d215-378a-a87a-6db5c0c3f13b | 1.82848 | -60.84816 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07787d3f-82ac-3f86-af39-7c8ddf0e5516 | 2.55958 | -60.5652 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bf6be402-3a72-3b64-ade9-e08cc700e397 | 1.37747 | -60.30722 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c85fdbd-41d3-39b5-8171-4190d3e90649 | 2.55614 | -60.56573 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| b85427c6-4d80-3cf1-8657-f56142d15a26 | 0.45971 | -60.39758 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8c1e91c-592e-3fc3-96c5-4114c5d25a39 | 2.55556 | -60.562 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 25d8a8ae-c648-3a92-89e8-9ca60f7fedf8 | 1.37465 | -60.31135 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e556e174-b16a-3eeb-a479-bc8ee7a491ad | 0.46365 | -60.40063 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73da729b-3abd-3b97-981c-f6799aa1fc34 | 1.3769 | -60.30362 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f98806f-95c5-3d17-abda-7b327664b203 | 2.54343 | -60.72525 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb631a85-69fc-30d7-9d69-ad5f34ea581f | 1.73551 | -60.5836 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a9d3cc0-09d9-392b-acbb-33f54d727edb | 2.56245 | -60.56094 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 48f48834-2992-364c-abb2-4fcb82f0414d | 1.38029 | -60.3031 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e512b3c1-8eda-3600-9629-a983c6b12183 | 1.37861 | -60.31441 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 970fc864-b550-3a9b-baf2-088ca361ee16 | 0.44997 | -60.40611 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79b8f0e4-cece-3b11-ba31-c3c9322f9112 | 0.45634 | -60.3981 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceec2610-f804-3a52-8906-2c6c5985854d | 1.15472 | -60.33392 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cefcf057-bcf9-3632-a483-f909890bc7ce | 0.46028 | -60.40115 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4dfe961-dcd1-3f21-86a7-eb17f813c1ff | 1.15529 | -60.33752 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6433cf57-9fa7-373b-b0e0-1571caf33c04 | 1.82502 | -60.84869 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3cb77f28-a033-36b9-87dc-6dd8e536d912 | 1.2755 | -60.41128 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcfe6b57-4a14-3085-a4d3-ec25f00e97bb | 1.3702 | -60.37112 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc3ca037-2737-345b-bd2d-fcdf050512ed | 1.37184 | -60.31548 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 531e5aaf-507a-35ba-9624-169a5be96882 | 1.8279 | -60.8444 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c9443fd-ac24-3ed2-9b26-5ea4590468e9 | 1.37522 | -60.31494 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec5de4e0-f5f8-3f51-83ed-0903de3e778b | 1.17114 | -60.37188 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 928e3753-de40-3f5c-847b-5108a426af16 | 1.17453 | -60.37135 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f9a96ab-357b-3f58-8839-f47c876ea954 | 1.83136 | -60.84386 | 2026-02-20 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16cacb0d-8d98-34f2-a7a1-34b4c99b0259 | 2.54283 | -60.72147 | 2026-02-20 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9839f19-0be6-3cc9-a337-262661b2090d | 0.45352 | -60.4022 | 2026-02-20 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5f39f6b8-af10-3d4a-804a-a456f428f04d | -11.84646 | -49.22695 | 2026-02-20 05:29:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53f74f6e-6e2c-33c8-9d10-f2d12a3ea68f | -10.67469 | -59.3505 | 2026-02-20 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 917bd7f6-3faa-3662-94e4-edc4fa15ff8e | -9.72196 | -60.20209 | 2026-02-20 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 024bc2e9-7172-3e99-82b1-182741e32db9 | -10.67006 | -59.35764 | 2026-02-20 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b65f47b6-4f4a-3111-8677-ca2493640724 | -10.67354 | -59.35818 | 2026-02-20 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4546e8e6-6466-3d07-8624-bc50f240a1b2 | -11.84712 | -49.22125 | 2026-02-20 05:29:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cf778e2-7e95-359e-99a8-a3c898664a71 | -10.67817 | -59.35103 | 2026-02-20 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 662a8916-5e14-3e7c-a2de-07a195f009ae | 2.5621 | -60.5458 | 2026-02-20 05:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 84556c69-5e8e-30cc-b4cf-ce026c8de165 | 2.562 | -60.5648 | 2026-02-20 05:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c4fb45e1-b455-3477-a2ab-4e377a1ab5b1 | -18.97721 | -52.92934 | 2026-02-20 05:31:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 77bdce48-9991-3926-b77d-6283e6272eec | -18.97144 | -52.92878 | 2026-02-20 05:31:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de503477-f8a8-3db6-939d-488901690f88 | -18.97187 | -52.92449 | 2026-02-20 05:31:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 692ea024-0fe9-3ba7-9563-090138da6735 | -9.77301 | -71.49113 | 2026-02-20 05:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a24e6d08-289d-3546-890a-a5228b44576e | -13.49124 | -60.38368 | 2026-02-20 05:31:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e407e6f7-58ce-3e30-8c94-7ac08ba3bfe0 | -11.83609 | -58.04605 | 2026-02-20 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b0bcf7a-a036-3bab-a169-28e566ab947d | 2.562 | -60.5648 | 2026-02-20 05:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 4b134e97-67f1-32bd-b582-22f435f0c19d | 4.87213 | -60.20829 | 2026-02-20 05:46:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88ac1440-776b-3364-9b21-eeee04143ce6 | 4.97482 | -60.52191 | 2026-02-20 05:46:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 488121d7-b4dd-33cc-8b71-f20859fe210d | 1.82923 | -60.84953 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76e8a152-94d9-3de2-a15a-3e4a5dec442e | 1.37858 | -60.3092 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5c0dc2b-a452-3ffc-8c08-a20b00ac2b89 | 1.37166 | -60.31742 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 323da86b-073e-37b0-a42f-1bba3d9d5d67 | 1.82848 | -60.84473 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 24865598-83f1-31bd-99c2-d8936b7ff3c9 | 1.37512 | -60.31332 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8316839d-32b0-3291-a102-6caa253e7a7c | 1.9786 | -60.69825 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d1b70f9-565e-3efd-921b-04f33a8737b8 | 1.30887 | -60.39888 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc44e649-f481-37a1-8165-9b7c549e2d87 | 1.15382 | -60.33678 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7abca7b5-9048-368e-a4d0-c3aad7a9e188 | 0.4526 | -60.40727 | 2026-02-20 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 832b3503-0766-3d74-8296-286e76c90f16 | 1.15673 | -60.32915 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16a24cc8-edfa-3641-b9a3-793de4244844 | 1.37457 | -60.30983 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5940b631-2023-31c5-8e21-2f30da226577 | 1.15784 | -60.33615 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5b26413-2977-39b7-9e15-312ac5d4fc0b | 1.1584 | -60.33965 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02533405-86a6-34de-a25b-a02c5fa1804a | 1.15271 | -60.32979 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68da64ef-ce0d-3aac-82bb-65067adb7281 | 1.17198 | -60.37336 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e36b9ef7-bb54-3a62-94ea-307e2963c0dd | 1.37568 | -60.3168 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b618f81a-57b4-3fee-b134-ff7a09d449a8 | 1.37914 | -60.31269 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91051d3b-a708-3ef7-9569-087e313c303d | 1.13028 | -60.52132 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f5af19a-57fe-3608-8120-f33d43989149 | 0.98446 | -60.42831 | 2026-02-20 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d150a41-e1d0-3752-bd99-83eabfd9b59c | 1.15327 | -60.33328 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a609ce2-d364-3d5a-9c84-434a0f2f8016 | 1.06187 | -60.56848 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83da97ed-f890-3950-947b-a5264881f53f | 1.15729 | -60.33265 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 452ed5e3-3048-3dcc-97a3-3ac50b6735e7 | 1.82622 | -60.84324 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 221aaf98-da23-345b-bdb2-af0d50976cd9 | 1.37803 | -60.30571 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac7c913f-608f-360b-841b-bfe3108f45cf | 1.827 | -60.84803 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c635f029-44cd-35e8-b48c-943c00e2ea1a | 1.36797 | -60.37142 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01e051b7-e015-3d22-9ad3-871d3df60d94 | 1.54219 | -60.38557 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f30bd9-694b-3692-8886-36af072a4ce1 | 1.83007 | -60.84263 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b61cf5c4-d0c5-3e46-9fa1-830da11f6095 | 1.37252 | -60.37423 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45936e51-2f7a-394e-be54-6cc4cee5b807 | 1.37969 | -60.31617 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efcc3677-4b3a-397d-b026-cd4f0f76164a | 1.36853 | -60.37488 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0451438-62d8-36d0-b243-e6a36997a624 | 1.73538 | -60.58405 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
