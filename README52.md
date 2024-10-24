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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54f38c5b-b598-3741-aec4-f3ff43db18b5 | -17.05714 | -57.47533 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 65d87818-5586-3d64-a5dd-6f51ea7d8258 | -17.04723 | -57.45332 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 610993eb-dad3-3050-82d0-a17c6463551b | -17.04631 | -57.45811 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 930c09b6-1363-39ed-8d3a-929495b2ba3b | -17.04356 | -57.4725 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5b5de96a-74f9-357e-8ddf-a0cac72c799d | -17.04271 | -57.45238 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 19dc7760-1584-3a41-9d5c-e28410e627a1 | -17.04179 | -57.45718 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 797e3aa9-73e6-36ad-9df3-4947a2881ab3 | -17.03995 | -57.46677 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b494b0b0-6a82-3453-876f-59481b216128 | -17.0391 | -57.44667 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 57aee2ad-85a3-34f9-bea7-8e7099fb0888 | -17.03903 | -57.47155 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ff9b51ae-f07e-3c17-bffe-048d474d9492 | -17.03811 | -57.47636 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3619ccec-2b3b-3eb4-a4af-31da36874d04 | -17.03726 | -57.45624 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 62da3171-2d46-3810-a3a1-ad79b42fd20d | -17.03634 | -57.46103 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| dc87ac5d-aa75-307f-9c06-5f126df22589 | -17.03542 | -57.46582 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bbe10546-75d2-389c-b808-62e51f94a30a | -17.03526 | -57.51585 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.2 |
| 144594e1-306b-3cbc-8bd9-f368aa8bfbd3 | -17.0345 | -57.47062 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| bf10950b-693e-3632-a480-41016bdb1bd0 | -17.00895 | -57.50536 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 82967e7b-5492-3f3e-bbc8-2060ad20c84e | -17.00721 | -57.48996 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 175798e9-127f-3d7a-9629-11b6182881f1 | -17.0052 | -57.5247 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2c224e8c-b810-3edd-918c-9f9470e6b124 | -17.00347 | -57.50926 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9323cbe4-8c76-3746-9187-846cf1ade076 | -17.00253 | -57.51409 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e6a8b6d6-6601-36f4-b210-ac9a828eb986 | -16.96883 | -57.51718 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 846da561-860b-3903-9e51-4d4002bea2ae | -16.96788 | -57.52202 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 7454ecb7-c96f-3a1e-b6d8-99ea08e606b5 | -16.96429 | -57.51624 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 1084f30c-e93e-373e-9859-b86a4850de86 | -16.96334 | -57.52109 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 8aaee789-d4c1-3f62-9ccb-86b34e1bb0bb | -16.95137 | -57.53375 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2989c6ee-c9b6-3936-9ba3-3f14931e6f22 | -16.95041 | -57.5386 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 872a0730-01e8-37d6-ae73-bbeaa77aada9 | -16.94995 | -57.54089 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 118c8156-9cb9-372a-836a-39097f42ab62 | -16.94682 | -57.53281 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ef088f41-7525-3c20-ba2f-2faefe3be415 | -16.94632 | -57.53508 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| badb493f-9e78-3c92-93f4-9eac84ba7a61 | -16.94586 | -57.53766 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 86968393-3592-3493-897a-844ec4a9bba1 | -16.9454 | -57.53994 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| cf3ec959-155b-38ba-980f-24bee5a71138 | -16.94514 | -57.51734 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bde829f5-c520-37cf-b402-5e3bc7d10e9a | -16.94454 | -57.51955 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3491f7bb-b353-3b2d-93dc-5a6fe2534058 | -16.94226 | -57.53189 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| c0057d0c-2779-352f-acec-3dd6bdfc351a | -16.94177 | -57.53413 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 63eb43b4-d92a-3623-85b9-08185db114fd | -16.9413 | -57.53672 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| e43f7948-2d05-3989-9816-0dd641c198e0 | -16.94084 | -57.53899 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| a24e360e-0ebe-371c-9c34-3af7271dacdb | -16.94059 | -57.5164 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 38747530-5bf2-32aa-ba66-9646c19b5ddb | -16.93999 | -57.5186 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 56203a20-5a36-3775-b871-4ebe773a4ffd | -16.93963 | -57.52124 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 92c813f2-eec9-3fa7-a927-f1d625bcd154 | -16.93771 | -57.53094 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| e699b210-d663-3a1d-9ba8-b4a34531ce12 | -16.93637 | -57.51282 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 215e2302-f417-3919-94dd-85f0657878de | -16.93544 | -57.51766 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 03c0f8c5-8aa7-360e-b03d-404df3c15aa8 | -16.93452 | -57.52251 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a7f721ff-0cbe-3f87-bc09-c20ae212d45a | -16.93359 | -57.52737 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e5cac864-423d-3bdd-bee4-e9a31b2cff66 | -16.93182 | -57.51187 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1c335d91-d752-3c01-83fa-6ca37eb3925c | -16.92904 | -57.52643 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0676227e-e716-384e-8cdf-ef9e4e9b880c | -16.92179 | -57.51484 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5e95c45b-42ae-3a32-82c1-ac49bef3c8ca | -16.91642 | -57.49357 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0398ff7e-0a08-344a-86e8-e3b7dcfc2f37 | -16.91188 | -57.49263 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 02e5173f-a7ef-39b3-a7a1-d3a86a4f45b8 | -16.91094 | -57.49747 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f1c41dcc-6028-3c81-81ef-af8cf10713ad | -16.9064 | -57.49652 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1786fa1a-cc84-3774-85de-e1b3dc26be62 | -17.03358 | -57.47543 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 741138c6-e988-3c53-89dd-62268a224e4f | -17.03274 | -57.45531 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 0e90070a-c7f3-3367-b9d4-2767cf7287a7 | -17.03266 | -57.48023 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0f0f111e-da9a-3521-92ce-6f3d3fdbb396 | -17.03182 | -57.46009 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 3695cf41-d8c5-3f02-ae10-8a404e13a50b | -17.03165 | -57.51006 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 07db0e6d-caf1-3dc2-ac4f-fdbac68c0676 | -17.0309 | -57.46488 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 51eb9218-e29e-32aa-96e5-38db88ded361 | -17.03072 | -57.5149 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| e5ddf828-56f2-3738-8a8a-ae17b79c6880 | -17.02998 | -57.46969 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 89cbb019-4698-335f-b0c0-84d950e515d6 | -17.02979 | -57.51974 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 7f82febc-de84-3fbe-87ae-d8dcfaee783f | -17.02905 | -57.47449 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| e31b9ff5-9a31-3a3c-b185-2021208c94a9 | -17.02896 | -57.49948 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 182c34e7-d6f5-3d5b-bc35-18223fc470d9 | -17.02822 | -57.45437 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c0aa22fa-91d5-32a2-8774-1922e747c8d9 | -17.02813 | -57.47929 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5ef23496-8085-32c9-9adb-e1fd1e34c15c | -17.02804 | -57.50428 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| b2f9d568-9ece-3727-8d3d-94a5b4d1e7ce | -17.0273 | -57.45916 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 89207971-5cdb-3fb2-b869-be84c25e237f | -17.02711 | -57.50911 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| f06b782f-46eb-3cc8-afe5-889bb80b11d6 | -17.02637 | -57.46395 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 4082e810-71b2-3717-b8e8-176fdc0c5778 | -17.02628 | -57.4889 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7e3d58e8-2963-3bf6-9607-0fbb5c7f6a00 | -17.02618 | -57.51395 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| d207a54a-29bb-3b1e-9f51-ed48f183bcd9 | -17.02545 | -57.46874 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 38e8b302-9c53-32b4-896d-20865d47ab41 | -17.02535 | -57.49372 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dabceb66-4c0f-3375-88aa-9f2e2438a0b7 | -17.02525 | -57.51878 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 74cff6cc-ce2d-3212-bb75-5f0cd87f7b12 | -17.02452 | -57.47354 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 6a4c4ef1-e885-3bb6-b5e0-b22201a1d717 | -17.02442 | -57.49854 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 43d8c1d4-d98f-301c-afa2-68c144a9477c | -17.0236 | -57.47836 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 34b3d0e3-f4be-3777-b182-70973b19f59b | -17.0235 | -57.50336 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 4b5e682f-ac51-3407-821e-ca2b08e6fd38 | -17.02267 | -57.48315 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 57f5f1d2-31f5-36fe-a391-c4aa212642ff | -17.02257 | -57.50817 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 73e0dd69-8e1e-3dc3-9077-776b79c5e4a3 | -17.02184 | -57.46302 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 445da3a0-e422-3703-930c-b4e38181c394 | -17.02175 | -57.48796 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 01f753b2-30a1-3568-9edc-fd2ed9ff83b7 | -17.02164 | -57.51301 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 7a73eeec-7eba-3597-8f48-f071a3db8410 | -17.02092 | -57.4678 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 23ad0e8e-bc1d-3b8c-8841-5ca9e38eb40e | -17.02082 | -57.49277 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 8320320e-4054-3d16-8b7b-71252d6526ea | -17.0207 | -57.51784 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3ff517fc-eb98-3363-9300-41ae5f00c940 | -17.01989 | -57.49759 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| c3f16d21-95c4-3c6d-ba81-e0e2dcbf5bdd | -17.01977 | -57.52269 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dac384c4-a82e-3a1a-b247-c8c81668a9ea | -17.01896 | -57.50241 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| ecf318db-f654-341f-b7b7-7c6ddc29dd02 | -17.01721 | -57.48702 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2a2caa5a-47f2-3698-9589-325476efc9db | -17.0171 | -57.51207 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 7c784914-ed81-316e-b075-0059899369ff | -17.01628 | -57.49183 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| cadf9cc8-9ec0-3150-969c-4fb053f07883 | -17.01616 | -57.5169 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 20a514e2-cf3d-3ef5-8202-dd1fef719719 | -17.01535 | -57.49665 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4f0943d8-4c54-3060-8587-b589821aa06e | -17.01523 | -57.52174 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| a27a54cf-2c53-3b5a-8c50-84f6bf30a189 | -17.01442 | -57.50147 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 898acb04-2ef1-3eab-a6c4-847caa10783e | -17.01349 | -57.5063 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a6bad0d7-3070-3be6-8f21-95512179510c | -17.01255 | -57.51112 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fd63cf6c-3bc2-3360-9777-887840a846b8 | -17.01162 | -57.51596 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d80ad3bf-e6c8-3fd5-bacf-d2ed808f4972 | -16.85453 | -57.69019 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README53.md)
