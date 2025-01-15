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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93d75759-7d5b-31d3-bc13-aaa4f8ae65f1 | 3.04036 | -60.24017 | 2025-01-15 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4d25bde-d631-3dfb-a34c-bd3dcf88ce9a | 2.94536 | -60.18159 | 2025-01-15 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 247ba148-0bad-3d3a-8e46-a9e06903955d | 2.94592 | -60.18501 | 2025-01-15 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b5ea06f-a776-3a61-9ca0-e9180dd35125 | 3.60313 | -61.02377 | 2025-01-15 06:01:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2535d282-1233-30bd-8c97-2214f592adca | 3.04518 | -60.23588 | 2025-01-15 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49e7e624-a8a5-36d8-9ede-c9eeeda5c89f | 2.94649 | -60.1884 | 2025-01-15 06:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c925b4e-fcf4-351d-b42b-0c0cbba7a13f | 2.10899 | -61.83139 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 1d972c41-f889-39bc-802a-ab3e48b5cc00 | 1.32189 | -60.03802 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9484d06-cf15-30e6-924a-250aa398da0c | 1.3257 | -60.44477 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 783e145c-ef2b-3f8c-9fc9-9a79918f461b | 1.32499 | -60.44475 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9b790222-c917-3431-bae4-f65f42a4cf61 | 1.31359 | -60.43943 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c6c8ea6a-2194-3a25-94b1-dde168ded774 | 1.18052 | -60.49417 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 442b49f8-6aa8-32ff-ab68-68cd743bd2cf | 2.09248 | -61.83599 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c338a697-00a2-3fca-9f33-94b201742e2c | 2.51948 | -60.99071 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 29.0 |
| da852fb7-12d0-331f-9ca5-2908b0cc16f9 | 2.09642 | -61.81635 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b7e7504e-f158-331f-9182-b5f45327fbb3 | 1.31906 | -60.43859 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6cb39d98-1b62-3636-a691-3a3991180914 | 2.10716 | -61.82027 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ba31c6f6-e20d-31a8-a420-caadf3033b55 | 1.32693 | -60.0335 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5dd0a909-489d-39c2-b16b-cd9078f0a241 | 2.52311 | -60.98058 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f075b1bc-eaf1-3099-a9c2-c1b75e8341c9 | 2.5226 | -60.97748 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aba5c55-9dfa-3ee7-b508-91615fcce99c | 2.19806 | -61.80974 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb26e917-698a-35b9-9b49-234a27ed4be7 | 2.09424 | -61.84715 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db9691e6-c081-3b57-af57-c20d4a5d4865 | 1.32754 | -60.0373 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ea340bf-07b4-3b1c-a40f-8a72592dacec | 1.34939 | -60.02987 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 917c5737-c22e-3d3a-b29c-270ef99ce44d | 2.52051 | -60.99691 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 47ed89f0-2719-3f2d-b212-f01eb6d31f30 | 1.1696 | -60.49598 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4ecf4ee-0427-3282-88fb-eb102e718e84 | 2.09336 | -61.84156 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29995259-7c57-3464-995a-df90a69d3070 | 0.72858 | -60.11351 | 2025-01-15 06:03:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a8193ef-73cd-30f0-936a-0aa544eb1887 | 1.17562 | -60.49858 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e9191c2-b21f-3ebc-8268-a7abccd50587 | 1.17393 | -60.48807 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9fd9788-7fc1-38f9-bd6a-be344074f178 | 2.52516 | -60.99296 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd803a69-fd3d-37a5-92a3-9e26b8c2d139 | 1.18108 | -60.49769 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf9672ba-5ab3-3407-a739-5137e914f81f | 1.32555 | -60.44829 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac13b9b8-5721-364d-8292-d9b8ae7ea258 | 1.3222 | -60.4236 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 93adcc36-5bd4-3faa-99d5-c845937aa528 | 1.31841 | -60.43856 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3d7e401f-5d5c-3a5c-97a7-889777f3da42 | 2.52 | -60.99382 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 73d553b0-f9a1-3a79-8424-675a57f3ecf1 | 1.31965 | -60.44212 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f4eef123-ef6c-3907-aa45-776467039028 | 2.09607 | -61.84471 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 566661f0-f2a3-35e8-ac45-e9ec8a06a2ac | 2.52363 | -60.98367 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25638164-2817-3d6f-8fd8-1e1c37b6fa67 | 1.35363 | -60.03282 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae1e8d3d-d7d3-340c-b694-8ca06e9cffad | 1.32165 | -60.42353 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f18c14b3-964c-3109-b143-bc9e82d9a6d2 | 2.10134 | -61.81562 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1266da00-ef55-32c1-9b9e-3969193e4ad3 | 2.28855 | -60.21252 | 2025-01-15 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29920f7a-14cd-358a-a019-bdc394febbf0 | 0.72538 | -60.11405 | 2025-01-15 06:03:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 042f0ae0-9a53-3444-953c-2213f24e18f9 | 2.51794 | -60.98141 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45d613ac-7b9b-3262-82e7-573b1e5f763a | 2.51482 | -60.99461 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 7b9ab6a4-ab5a-3341-ac64-8f3a69616de4 | 2.28974 | -60.21972 | 2025-01-15 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 1f015059-56ca-326a-b697-3738f6525c1e | 1.32512 | -60.44125 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 217a3a80-f9a2-3915-a5c7-785837df2b51 | 1.32023 | -60.44566 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 79e11af4-0ac3-3031-8ceb-1aa28099e41b | 2.51846 | -60.98451 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| abe541e4-65d7-3613-b987-0d829ba75490 | 1.31349 | -60.44295 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87901d41-c485-3762-aed2-86140c8b5a91 | 1.1745 | -60.49156 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f2062f1-aa09-3d20-b101-cbf3f4542631 | 2.09699 | -61.85024 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1e7764f-3e03-3a52-bd90-f52932e9ff37 | 1.32278 | -60.42714 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 55746f81-bf62-3f48-aa8c-b3dc6f1b9cb0 | 1.3222 | -60.42707 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 49c879eb-ffae-31e8-91cf-1b4c21b654f7 | 1.31732 | -60.42804 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46b3fb2d-8013-356d-b8cc-7c539cb9204a | 2.28427 | -60.22058 | 2025-01-15 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ebd0670a-1f03-3e18-a7a1-f33a859fa051 | 2.28368 | -60.21703 | 2025-01-15 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 02794f01-0baa-3e20-b853-b3cc79cbdde9 | 2.51431 | -60.99153 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 29.0 |
| d008e2e3-4dd1-3488-8e4e-e9e6500f8cb0 | 2.10626 | -61.81485 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b5c56363-0a3d-364e-9a27-54abfc79228d | 1.35299 | -60.029 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99422315-4dbc-3e41-9452-9588c2a1f3fd | 2.09114 | -61.84537 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc843c24-7919-3a5e-97fe-204e44385f8f | 2.09553 | -61.81096 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0180565e-0780-33b3-a8fa-2a9eeb58b885 | 1.31674 | -60.42453 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9d0ebfd-24a2-3995-936a-7408ebbb4d69 | 2.51276 | -60.9822 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c90cc44b-e3ae-34c0-b5e9-11a2a9b366aa | 1.31418 | -60.44297 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e75e97f8-a169-3c8f-a5d2-18a09b9c8ddb | 2.10008 | -61.8385 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e68014e3-9f55-3743-9fc6-b01f3856a7f9 | 0.72922 | -60.11735 | 2025-01-15 06:03:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a998de98-21a3-3c78-bfa0-942930053899 | 0.66728 | -59.59421 | 2025-01-15 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0310dd2f-15c1-3ea0-8f20-b3888f41cb73 | 1.17619 | -60.50209 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34656cc9-098b-3a60-abb7-f8be707e5122 | 2.09732 | -61.82178 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f16f3270-403f-3584-bad1-388e6c3132d4 | 1.32443 | -60.44123 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df45871a-3503-3c2d-a4fe-243142909224 | 1.31896 | -60.4421 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4e9a013c-972f-3326-958e-918eec0371c9 | 2.10099 | -61.84399 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 27c4b2ea-1012-3e33-b8ae-ba3c17e1f352 | 1.32129 | -60.03428 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fec5a14-49ca-35ad-b58d-763af93922b4 | 2.09148 | -61.81704 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 81afa219-7a11-3284-870b-f78018a1011a | 1.32628 | -60.4483 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79e2f583-82a5-351b-ad2b-defd17ca976e | 2.51897 | -60.98761 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ecf3e320-55f5-3c02-b5a5-8717359adc48 | 1.17995 | -60.49066 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6322eed0-d9b1-3cd9-a667-107744dfaa83 | 2.10807 | -61.82581 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 64e75eca-2063-3632-a209-0d730d141411 | 1.32387 | -60.43768 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f39c9ac9-fb4d-3fa5-9c54-2f60a4e3ff51 | 0.72598 | -60.1179 | 2025-01-15 06:03:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a7f5b5e-252e-3bcd-946f-b094ef88bd26 | 2.51743 | -60.97831 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a47532b-4d44-3d91-8ba6-ce739a4f1ca4 | 2.52414 | -60.98676 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8670740b-b282-3d5a-af9f-08be5b443938 | 2.52465 | -60.98985 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c15061f7-d924-3677-b090-627b101d76f5 | 1.16904 | -60.49246 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de684f91-16de-3812-9c9a-26f894e7862a | 2.10048 | -61.81037 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba14a0a7-1b26-333d-aab5-5d7ac95cd495 | 2.28915 | -60.21614 | 2025-01-15 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 6f02acc0-2e2b-3c0c-a35c-1dd34c1b4023 | 0.66795 | -59.59831 | 2025-01-15 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e041e47b-f9c5-354f-8783-131350cf37c5 | 2.08932 | -61.84782 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1bc95dc-6e66-3198-94e5-3d5e4b50053e | 2.19647 | -61.81139 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b4f0b0a-7845-37fa-8a4a-958880123799 | 1.17506 | -60.49507 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06497469-d0be-3aab-94a8-8be5990633d5 | 2.10223 | -61.82099 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0ebca67a-6078-3477-869f-84225cf3ee2b | 1.35 | -60.03369 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b21c3e99-7fb3-32d1-a87e-2f83113bded0 | 1.32453 | -60.43772 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 126e743b-e3e7-3dc9-857a-8891ccab28f1 | 1.32249 | -60.04175 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b192373-1cfb-3e4a-bdc1-922959c5de52 | 2.09514 | -61.83913 | 2025-01-15 06:03:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba316f4e-38d6-3fa8-a63d-a7a9aab6165a | 2.51224 | -60.97909 | 2025-01-15 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff96a1bb-f421-31fd-a8da-740f2bef45d2 | 1.32813 | -60.041 | 2025-01-15 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35663e1d-f24c-3f5b-b7ee-0f19133918c2 | -7.30814 | -73.0356 | 2025-01-15 06:05:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
