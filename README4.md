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
| 3465d517-a1f5-31f0-a9f7-1a9bcb492b69 | -20.72668 | -55.15969 | 2026-02-11 05:22:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d12f3fd0-fe20-3cc8-8a4a-795d36c154f9 | 3.38161 | -60.64901 | 2026-02-11 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2e2950d-3efe-30b0-8ac3-57239261772d | 0.96621 | -60.52015 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9465d28c-ed0b-328f-89ab-3aa2a9ca4bba | 0.9596 | -60.51388 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c63a05c8-5c28-3d81-a20e-991cc9df999e | 0.65816 | -60.36089 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6899360d-8cfa-3387-9bc6-c9e007c8d700 | 0.87445 | -59.58553 | 2026-02-11 06:05:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54648906-1634-37d6-9c06-feeb0bc3fbf1 | 0.7812 | -60.66989 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74d72081-bc68-3628-86ce-6d7b8e64604b | 3.31721 | -61.03487 | 2026-02-11 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf518893-cd27-3f6c-92c9-4ca85155c07e | 0.96133 | -60.52216 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2ea3171-9d6e-3d71-a8a9-46899009da6e | 0.9541 | -60.51479 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0183a557-fac4-3f80-b623-4ad9abd4867f | 0.9247 | -60.36755 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a3c28fe-c507-35c1-8073-9f4e233db0ab | 0.9724 | -60.59626 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b573856-2885-3a3c-bab7-b0bce14fc4f4 | 3.38738 | -60.65134 | 2026-02-11 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18e62054-f9b2-3479-8936-86de18642612 | 0.78722 | -60.67252 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25b3d8fd-9f7e-3c3a-8b9d-5f527a3915a9 | 3.39369 | -60.65688 | 2026-02-11 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67a769bf-9660-31fa-b35c-87418116a613 | 0.95584 | -60.52304 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14f00b98-e02c-35bf-aa03-422765789c55 | 0.96681 | -60.52121 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63efa2dc-91c1-34c5-8a3b-926f5f285853 | 0.95904 | -60.51026 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e7dde1a-cdc8-31df-b0c1-e4d6df762d60 | 0.96074 | -60.51856 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd843d89-e37d-3ed0-b848-b07ce6606b4c | 0.65875 | -60.3646 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dff30555-b68a-3ca3-b9ca-50a3efea48ea | 0.95525 | -60.51945 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa4eacd8-1533-3178-9e76-434b48ad487e | 1.28632 | -60.43028 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e597e60c-48e7-32f5-9e70-9fd52c097509 | 1.28573 | -60.42666 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eb90417-6949-3e5e-b34f-524ad15bc69d | 0.95579 | -60.52563 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03fa50ba-55b8-3531-b693-b79336209351 | 0.95642 | -60.52664 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 436cf1e2-d2ab-3dd9-9326-15ee6740e601 | 0.96015 | -60.51495 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dff919aa-9790-3b88-8177-5a073a67f2bc | 3.38792 | -60.65454 | 2026-02-11 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15670ea0-49ea-34dd-ba28-70e69d713909 | 0.96739 | -60.52478 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fc64f62-0e69-3a0f-8f25-8f4239c11049 | 1.27571 | -60.43777 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc69a594-4db4-3b50-8ddc-b0504da1dcec | 0.95407 | -60.51225 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c28cc47-6483-3e9b-816a-7c3b1db2e842 | 1.34545 | -60.02738 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 797600bd-0453-36c0-a1cb-48d1a9b5f494 | 0.96191 | -60.52574 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffe25063-b3e5-37c3-841f-d07c92703803 | 0.96128 | -60.52471 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff5ba0d8-5c91-3e63-8761-b52cf0ed3323 | 0.97295 | -60.5998 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16502bbb-e5b3-3094-80bc-386734897266 | 0.97356 | -60.59713 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f72ccf6-e17c-36d0-96c1-df69ddae4d8a | 0.80278 | -60.27983 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fe405a2-9304-3419-a60c-33ba53d0daab | 0.95956 | -60.51134 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce18bd99-a2d7-3b92-8a24-edab455fb732 | 3.38846 | -60.65777 | 2026-02-11 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 749e25fd-7a85-3340-975d-e0826893c6c7 | 0.95467 | -60.51841 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d462b369-7b93-31bd-ba53-80051faf3f8b | 0.96676 | -60.52374 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 835fc4c0-b3c4-30ed-ab5d-00b7f1de982d | 0.95034 | -60.5239 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4799f1d-f303-3fb9-9846-a7e8e7fcfb7c | 0.96016 | -60.51749 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d234761f-f95a-326e-b7d8-f8c2be93c1da | 0.95466 | -60.51585 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30768aa0-e8db-3218-b4e6-700787fa89aa | 0.96867 | -60.60156 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f26cdf4-1c84-3d5d-87f5-138ed0b032c0 | 0.96072 | -60.52111 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 887306cf-eb76-330e-9ad8-aa2d3a903e11 | 0.78665 | -60.669 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4573cb01-1336-3fb9-9eaa-4704b834dfd0 | 3.39315 | -60.65366 | 2026-02-11 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b0ff4f3-7bc2-38e4-9e28-3fbca6aed05e | 0.95354 | -60.51118 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f84766c-997a-3681-9bcf-d3da3e893e1a | 1.11793 | -60.51091 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28987938-a3d9-38d9-b047-016a0cd2eea0 | 3.3167 | -61.03184 | 2026-02-11 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcc782f0-f50c-3d12-a272-1800073c8568 | 1.11736 | -60.50731 | 2026-02-11 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7362f33-cc2b-3666-add9-be345e8d96ca | 0.95523 | -60.52202 | 2026-02-11 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27c69c78-7602-3250-9698-642248ce4f4c | 4.40735 | -60.77789 | 2026-02-11 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b2b7196-1f5a-3c54-904d-1b8bda23bcdc | 3.71326 | -61.02715 | 2026-02-11 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b019240-3d4a-3ef0-b015-629ce64e7e02 | 4.40835 | -60.78386 | 2026-02-11 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6bdb321-92f2-37b4-ad42-1b4cab45f874 | 3.72 | -61.00448 | 2026-02-11 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ccc6d7a0-b4b9-3b99-8bf7-b199eaeb6e35 | 3.71589 | -61.01133 | 2026-02-11 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b1bec25-3e5b-32cb-a5c7-37494bb7a47b | 3.7195 | -61.00146 | 2026-02-11 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 238dafd5-066a-3215-a0bc-0e407a5890a9 | 3.71393 | -60.99932 | 2026-02-11 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6dad4a4-70ed-3dd2-b6f2-bb43c3ed1673 | 3.71852 | -60.99543 | 2026-02-11 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e331f397-e781-390c-8cb9-e8d0b228781e | 3.7154 | -61.00834 | 2026-02-11 06:05:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51b5f77f-0923-3886-821b-6e740a721af0 | 0.96231 | -60.5205 | 2026-02-11 06:54:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 8f423ad4-706f-3094-9276-751b40ab06e6 | 0.9601 | -60.50588 | 2026-02-11 06:54:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 50e6cb97-8295-3112-82e9-00721c814cbf | -27.60637 | -51.44141 | 2026-02-11 12:16:00 | TERRA_M-T | CELSO RAMOS | SANTA CATARINA | Brasil | 4204152 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 32c72eb4-6c87-3f54-b500-799f47ce15bb | -23.82215 | -53.22083 | 2026-02-11 12:16:00 | TERRA_M-T | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 65e64a7b-f46b-3dcd-b84c-53ce097f9ec9 | -21.47504 | -54.43066 | 2026-02-11 12:16:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c7e71db4-9539-3e25-98a8-7e1bf67bfdce | -32.40199 | -52.41582 | 2026-02-11 12:18:00 | TERRA_M-T | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| b34ff6c1-522b-3ad6-b6d7-b48810a2c7f0 | -29.3833 | -50.33691 | 2026-02-11 12:18:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 32.0 |
| 7d611c34-0313-30b1-ba39-2b2c00ae599f | -29.38479 | -50.32411 | 2026-02-11 12:18:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 858e848c-b3e9-3c7f-b88e-9273e3f6b590 | -30.54543 | -52.71525 | 2026-02-11 12:18:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 9.0 |
| 8289bb8b-91e3-373e-9e37-8b7fcb4b1a2e | -30.72077 | -52.77968 | 2026-02-11 12:18:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 9.2 |
| 3ce98d1f-fa11-32ba-8573-09ff9c25fbb6 | -32.4074 | -52.4244 | 2026-02-11 14:10:00 | GOES-19 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 127.7 |
| bba6d4bb-72dc-33d9-8020-4cc6eaf2a978 | -32.4074 | -52.4244 | 2026-02-11 14:20:00 | GOES-19 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 125.4 |


