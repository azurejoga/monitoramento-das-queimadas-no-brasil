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
| de06e168-4f1b-3e5e-94e1-8088c424e1d1 | 3.56295 | -60.70578 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4af6f2d-901f-3659-a3ec-65bd3d2e336c | 4.11109 | -60.84783 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a57d2e8e-0df7-3b16-b2c2-076e1841da26 | 3.71602 | -60.44957 | 2025-01-20 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0cd641e-07c1-3ad1-86fd-1d5d8ff403b9 | 3.95134 | -61.0092 | 2025-01-20 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88da7629-1052-3e27-8100-eae96778260c | 3.65534 | -60.9706 | 2025-01-20 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ac90eb9d-767e-379e-99a0-bbb527109af6 | 4.42994 | -60.34684 | 2025-01-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd2ea34a-2e79-321d-9a32-37e644f511e3 | 4.51394 | -60.68598 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 581d9d50-b1df-3bd0-961c-3f3bf4876ab7 | 3.42127 | -60.45148 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbb92e0a-dd92-3e26-9b2c-338c3d651acb | 4.95078 | -60.5352 | 2025-01-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96631c23-d60b-3911-86da-90f98ade21a5 | 4.14077 | -59.99355 | 2025-01-20 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08dda006-1bea-3497-9d77-ffe6fe8a5574 | 2.89619 | -60.7768 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a4d5317-d580-38b3-a85c-0c2c706ef5a3 | 4.53979 | -60.70606 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c3a83ee5-9e7a-3eea-bda0-0ffa51e6f671 | 3.74542 | -60.63951 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 433c1607-e6db-3027-8116-aec4feb2e89e | 3.75186 | -60.65816 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19c84297-ce11-3576-9a94-539b37fd1de5 | 2.89678 | -60.78061 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3557986-e51f-3a99-a91e-389baf976aa7 | 3.91799 | -61.00581 | 2025-01-20 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0449aee2-1cef-395d-b08d-55fd59b6243c | 3.56493 | -60.70543 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e66b8fc-1261-34c2-ba82-f6f1aa9e9282 | 4.13682 | -59.99049 | 2025-01-20 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 260f18ea-d759-3905-9e39-fd0d8dce8227 | 3.42241 | -60.45898 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06016f12-03b2-3273-8286-7fa3718d8694 | 3.91445 | -61.00635 | 2025-01-20 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d80ed5d-46b9-3b98-bbdf-664e858a4011 | 3.20857 | -60.98766 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ec56771-d021-30d5-9d1a-ddfe640663b0 | 3.65242 | -60.97506 | 2025-01-20 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40b97055-0017-3076-b42a-80e60f71cb39 | 4.99888 | -60.30277 | 2025-01-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb39802b-7301-35a3-aa0a-f4af96c34299 | 4.13739 | -59.9942 | 2025-01-20 05:20:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f807097b-aa9e-32e8-8699-3e2549a19f24 | 4.50696 | -60.68715 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 872e39f2-d4c9-39b0-9949-049d5c2b229a | 3.42184 | -60.45523 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3f7ad2c-88c5-3caa-9794-4207645981ae | 3.88322 | -61.25458 | 2025-01-20 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 286f69cf-31f3-3e96-8d25-2b6896e02088 | 3.52981 | -60.40414 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a2aefe9-1a3a-3c12-b1d6-0cb06684c6b8 | 4.53854 | -60.70607 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5ba8a7f-3367-33f2-a01d-20f15008d6be | 4.88042 | -60.56578 | 2025-01-20 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b4b58e8-17cf-3d6a-b54d-f1cda6d3649e | 4.02783 | -60.82021 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb131d06-f661-3369-b9a5-96ca35d4eed2 | 4.51045 | -60.68655 | 2025-01-20 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8326fa3c-9c1e-3766-a416-37951a12c43f | 2.89965 | -60.77628 | 2025-01-20 05:20:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d98ecab-3e42-3d5a-b887-ad964273d84e | 3.89739 | -61.22736 | 2025-01-20 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49ef330b-7101-3109-9f1a-71959a1ef9c2 | 1.35022 | -60.02691 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc0262aa-2277-3542-a244-d0fe214acb11 | 0.70475 | -59.68386 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15d54188-469a-3666-a709-e6f5c82929af | 0.80968 | -59.89902 | 2025-01-20 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c88f0169-c43e-3cfa-b0ec-1cc8b0bad369 | 0.37023 | -60.37785 | 2025-01-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a58f29a7-a3d2-3420-8130-f9c70febaad6 | 1.3357 | -60.04357 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ece0b40-a0f3-3a6e-b7d7-74ed705dfa9c | 0.80636 | -59.89952 | 2025-01-20 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ff2281c-300b-3003-bb1c-93696de512f8 | 0.86406 | -59.61623 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2f359d7-f63c-3b42-a870-d1f25f52989a | 1.9316 | -60.00597 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9c02a7d-ecc3-3449-b446-91630385a78a | 1.12192 | -59.41327 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6aa3703-710d-3c87-86bd-8addd75c6d43 | 1.92178 | -55.83391 | 2025-01-20 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf3c1f3b-0c0a-369b-b2cb-db8420997fc3 | 0.71455 | -60.11807 | 2025-01-20 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b577d93-5872-38fa-bf54-8e2ff52b435d | 0.13503 | -60.58952 | 2025-01-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd234d1d-a758-37f3-b3e4-8b017ac0e87e | -7.34939 | -72.561 | 2025-01-20 05:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c6f5958-5ff6-3236-8197-ceaf7b7cb7e8 | 0.6499 | -60.37834 | 2025-01-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5c07e91-3abc-364b-b6b3-3bf41c0b45d7 | 0.8514 | -59.3571 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 434b8e6e-863f-3ed7-9094-99ed19ca2909 | 1.17065 | -60.49369 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0294c7cd-b338-3ec1-a99d-c67d25916d59 | 0.7081 | -59.53135 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b137666-e7d0-3f0c-abb3-a521ba991e7b | 0.20833 | -60.58217 | 2025-01-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a96fb0c-b31e-3dbe-9c2e-d072a29bfc2f | 0.7889 | -59.52524 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c043202b-f388-3c2a-ba1b-c0ab6c89529e | 0.70252 | -59.69131 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af0a30bc-4e64-3fc9-8970-f490fc2f3533 | 1.09361 | -59.47052 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ddaa737-c297-3841-aee5-b7b4ce9e5b2a | 1.92921 | -60.0063 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3caa91bf-c243-3412-af8f-3bac6dedcb36 | 0.80581 | -59.89603 | 2025-01-20 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99fb0f0b-974b-39ad-bd5d-abe155e5f690 | 0.89763 | -60.0931 | 2025-01-20 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5df6b7a3-5210-30fc-8232-2d0770bf6e57 | 1.35356 | -60.0264 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea8af937-275b-3e11-bf07-72cdc8569e6e | 1.12245 | -59.41671 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d73e25f7-8b16-32cb-bd80-d2a32d139694 | 0.89429 | -60.09362 | 2025-01-20 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c273acc8-3bfa-3345-8cc2-92084360423f | 1.35635 | -60.02237 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8dc155a8-4a78-3a97-9b62-0fc9d5c78c09 | -7.35166 | -72.59861 | 2025-01-20 05:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac43d00e-5b95-320f-accc-1009a7664858 | 1.3569 | -60.02589 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ffd31615-2cfb-3112-b259-6aa05487581f | -7.34538 | -72.59749 | 2025-01-20 05:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c398d38f-1354-335b-9481-5b9544306c4d | 1.05333 | -59.65077 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6524bb02-4668-3225-9a58-92b99576a190 | 0.99474 | -60.01708 | 2025-01-20 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6919b825-4c76-3a4d-9762-ee1db5310581 | 0.71733 | -60.11404 | 2025-01-20 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e571e11-7394-3602-b378-a61e652fa3a9 | 0.89709 | -60.08958 | 2025-01-20 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7e1a271-73d0-37ea-910d-8f88bc3c5025 | 0.76614 | -60.01314 | 2025-01-20 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f78a6b43-28ee-3e09-906b-45b236881e9d | 1.05386 | -59.65423 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c171eefb-e712-31f6-9088-105ec31d5c87 | 0.70198 | -59.68784 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1964eef-4b91-3819-911c-66f3221a072d | 1.14785 | -59.90735 | 2025-01-20 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4444da19-25f1-3e3e-a3e5-0facbb2d2b3b | 0.86858 | -59.58016 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceec852d-2cc7-3f1d-846d-0671a423e1c0 | 1.12138 | -59.40982 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81db912c-67ac-32b8-a24f-5d0eda4cf9a5 | 0.89375 | -60.09009 | 2025-01-20 05:22:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5105437-8f98-3041-8a26-f1d4d8a76322 | 1.35301 | -60.02288 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fc8c193-4aec-3421-8d20-1394434438a8 | 2.24035 | -59.95114 | 2025-01-20 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6afab544-1187-3e73-836a-4d1ef84476d1 | 0.94935 | -59.48647 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4337f943-4776-316d-87d4-0b961851b8d3 | -7.35187 | -72.562 | 2025-01-20 05:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5cde8ba-0d97-3c32-b8b3-38039c192779 | 2.17325 | -61.81985 | 2025-01-20 05:22:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 635a61ec-2a4c-3dac-a772-f1bb72074fa8 | 0.80913 | -59.89553 | 2025-01-20 05:22:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c15f55a-4cbe-3ad2-9f36-ac2c24488034 | 0.94605 | -59.48698 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dae06dce-c42b-3022-903f-b03a36e3b777 | 0.70529 | -59.68734 | 2025-01-20 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15a14a88-a293-3939-9951-e64e5a71ff35 | 1.00703 | -60.57394 | 2025-01-20 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af5bd97f-21ce-306e-907f-4011c0e2cda5 | -7.3456 | -72.56088 | 2025-01-20 05:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90aa1e89-b85c-381a-89b5-f358184765be | 3.74718 | -60.63999 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01346167-a1d9-3c36-a039-c80caf75ff53 | 1.35862 | -60.02407 | 2025-01-20 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3c97026-32e2-3406-9c7d-d8d6c1855446 | 4.15378 | -61.173 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24a92ef8-82d6-3d95-9999-9439abcdcae3 | 4.95021 | -60.53366 | 2025-01-20 05:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5341b3b-8f7d-3de5-b2a0-473afd01262d | 3.87014 | -61.21321 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5e968c8-3479-3a05-91d5-5cbea7332603 | 0.70764 | -59.53077 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6269b796-57cd-391b-bf37-5c4a7ad7557f | 4.03145 | -60.82149 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 230a6b10-c9f6-32c1-954c-8fa8882f3b51 | 2.23974 | -59.95057 | 2025-01-20 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c115f49-d527-3dd5-9842-726936185ce0 | 4.51503 | -60.68492 | 2025-01-20 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86edc563-97af-3c94-a962-e0873126c4c9 | 1.12187 | -59.4128 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc84148f-37c3-38f6-a977-f10efcd3ccb4 | 4.14142 | -59.99189 | 2025-01-20 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a939017-a028-3583-b83c-f5a8ae6fc043 | 0.70553 | -59.68654 | 2025-01-20 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e40cc716-6de8-3f62-872e-6ed9a1ae0095 | 3.89637 | -61.22372 | 2025-01-20 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebe01705-146b-31fb-a0cd-0ae2842f0845 | 2.17307 | -61.82184 | 2025-01-20 05:46:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README4.md)
