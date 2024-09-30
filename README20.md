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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 617a0eb3-2b2f-3c96-823a-cb16a89ca5c5 | -13.18251 | -48.55981 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a5e1ec8b-a762-36fd-9484-11c5a5ba48e6 | -13.18133 | -48.56556 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba931906-18e9-33f6-aa2f-fb757b402086 | -13.17519 | -48.56411 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8395246c-ae5c-311b-8c5f-2350e7d5d399 | -13.0428 | -48.61834 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae7ca3bd-abcf-3c54-ba31-4ec9110dd0ba | -13.03815 | -48.6096 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41aa485e-4cce-3331-9f41-512e80b69abd | -13.03705 | -48.61488 | 2024-09-30 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6978e27d-fb72-3d47-b28b-ba5e3282f466 | -12.72967 | -46.42076 | 2024-09-30 03:45:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d3ea8b5-39e4-3f78-be01-ab18e235b0f4 | -12.72897 | -46.42432 | 2024-09-30 03:45:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41ee7d89-ec46-32ea-ade2-1608f6754708 | -12.72417 | -46.41994 | 2024-09-30 03:45:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5905cc27-9b1c-30a7-907e-1bba1807e67d | -12.72345 | -46.42358 | 2024-09-30 03:45:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b885a67e-fab3-32b0-9181-62610fe62248 | -12.68943 | -46.77049 | 2024-09-30 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 346d31fa-6c97-34b7-9b0b-dc3ac3994d80 | -12.68868 | -46.77432 | 2024-09-30 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6b7d8fb-0bb4-3c59-90c7-c289e6ccb5b0 | -12.47412 | -46.44378 | 2024-09-30 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 806c8dff-8f24-31f2-adc4-bae8dff297be | -12.47373 | -46.44416 | 2024-09-30 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e30e6330-3cfa-3605-853c-4373ea67994e | -12.08776 | -50.01558 | 2024-09-30 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fb2d6ad9-f529-36af-bfc0-8614cb3a252e | -12.0876 | -50.01419 | 2024-09-30 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b239e8e9-dde9-3094-b77a-b294d26c4478 | -12.00785 | -47.32701 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a9832cac-fa08-3a6f-8272-b566102d351b | -12.00287 | -47.32152 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 39fcfdd6-e449-3bf7-bc8f-e4c1de07679e | -12.00201 | -47.3258 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4dea768-7eb2-3291-8956-b91e9c8b595c | -11.98385 | -47.30092 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a29a5bde-0b27-34c8-805a-ec369e3f8de1 | -11.98304 | -47.29929 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee9bb3bb-44c4-3dbc-8bf0-b3f318bd2396 | -11.98301 | -47.30526 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45f0f88e-1036-3120-87cb-e4910d1965c0 | -11.98218 | -47.30953 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bcccde86-00f3-3454-9588-f99e79654042 | -11.98216 | -47.30366 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8438bd94-5630-3385-b7cf-b8031972c8ab | -11.9813 | -47.30791 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b34561a-b769-3e8d-933d-cec343ea7069 | -11.97958 | -47.31641 | 2024-09-30 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95d9dd9c-3e63-3eae-9a50-1d17a49394b6 | -11.86566 | -47.13553 | 2024-09-30 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20c75262-7020-3c70-baec-e732b3d3903b | -11.82217 | -47.62132 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fe9164e-9d52-37d5-ab57-a8e7231fa21c | -11.79859 | -47.60182 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ecf43d9d-f110-3c77-90bd-476a5a753258 | -11.79524 | -47.60101 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 36344e27-47fa-337a-b0c0-94decfa573d9 | -11.79176 | -47.605 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92b704d2-580e-3682-81ac-d4a8cd26b848 | -11.78838 | -47.60418 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 197466e5-2a0e-3ea6-9fa5-31b2fb4e27f9 | -11.78584 | -47.60357 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cba976fb-a8d7-3ffa-9f49-e0519302f3cf | -11.78489 | -47.60836 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a79e9ee-8575-343a-b8ae-2af62692c5f4 | -11.77892 | -47.60717 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f30e39ca-9cb3-3be8-9340-7506ef4401ff | -11.778 | -47.61183 | 2024-09-30 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cb523001-7b5c-3671-9989-72347d47b6d6 | -11.58257 | -48.42905 | 2024-09-30 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ad0800fa-452c-3fa0-9ed1-9fea8b09cd9f | -11.58153 | -48.43418 | 2024-09-30 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| a8e594a6-7784-36da-8574-070334c75b10 | -11.44971 | -46.95774 | 2024-09-30 03:45:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9bce383f-3826-37f4-8f25-ef3cd7506a2f | -11.44901 | -46.96132 | 2024-09-30 03:45:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53abba37-9012-3202-8758-39246f2f73b4 | -11.41456 | -47.23006 | 2024-09-30 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7840876a-3c84-3518-b833-faa8e6ca6a91 | -11.40869 | -47.22889 | 2024-09-30 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9403175-44db-39f7-bafa-2964d0d3d1e9 | -11.40282 | -47.22768 | 2024-09-30 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9867f442-38d2-351f-939a-751c99a0ae39 | -11.40198 | -47.23196 | 2024-09-30 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 52438f9d-c919-30e9-a9b4-eecf3cd3f3a6 | -11.40115 | -47.23619 | 2024-09-30 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 46647c90-1c3e-375b-8be9-71824b6676b7 | -11.39529 | -47.23494 | 2024-09-30 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 37abca7a-6d86-3c7f-91cb-55ff7e86c386 | -11.3928 | -47.2476 | 2024-09-30 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 14c98514-39a6-3a3f-b17d-50777255b945 | -11.39193 | -47.25203 | 2024-09-30 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e957281b-a429-3fb8-b4ff-ef963d4f1f38 | -10.97952 | -46.44337 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81360c9b-435b-3e1c-8038-5e2e4b84d802 | -10.97858 | -46.4482 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe0a5ae3-8847-3668-94be-29117ff18800 | -10.97756 | -46.45347 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c509e538-6e1d-37e5-b707-c2c38677a3dd | -10.97665 | -46.4581 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0546a4a7-61e9-3860-9623-2669fb83fdee | -10.97581 | -46.4624 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ff6c77d5-ba36-3382-aea9-efc8cd8d81f8 | -10.972 | -46.42208 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71f3ef19-cddf-3c18-95f9-0a8856fce312 | -10.97112 | -46.42659 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ec1c423-69ac-3fea-8a05-605bcab6ffa5 | -10.96456 | -46.41358 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6519dbf-3834-3925-ac10-d1b5d4232029 | -10.96226 | -46.41219 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b03fd515-0069-3057-89a1-f7b87434b0e3 | -10.96142 | -46.47615 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7fffc2ec-8e9b-3e03-b67e-ce74c94b37ae | -10.95974 | -46.40819 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 125d52ee-b3b6-3921-bf79-c8c7a731fa34 | -10.95927 | -46.47267 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ac9354c7-60cd-353d-9296-0d04edbd6b06 | -10.95888 | -46.41277 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 613dcaae-4a57-3854-8b11-169d197ed09d | -10.95853 | -46.4766 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3c283b9-baa0-36a7-9a11-cb324d3bdb72 | -10.95833 | -46.40256 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c8ef0f4-bdcb-32a7-8ba7-b0f4934a4427 | -10.9575 | -46.40675 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2e1a533-9d04-3148-8376-cadffae4ec59 | -10.95661 | -46.41128 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b53316de-95ef-3eed-8821-8555ba79656c | -10.95654 | -46.47115 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2adcf881-15a4-36ad-bf10-967c2dfc6ebb | -10.95641 | -46.39501 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84b512e9-7e87-3280-b803-549cd7ae6d31 | -10.95567 | -46.3989 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b7c2d36-66c3-3c21-88b2-b1d8a4466eff | -10.95493 | -46.40284 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce17a4ea-d3a3-3252-a51c-2f5f70279fbc | -10.95421 | -46.39383 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46656d58-46c9-3fdc-8302-9bff4b2773a1 | -10.95362 | -46.47161 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 58aa778d-1c6f-363d-bec4-6fd2f5689697 | -10.95343 | -46.39779 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 909e7f8b-5041-32f1-8095-36485386570c | -10.95144 | -46.39053 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dd1c783-7700-308d-8dd1-daac27c2836a | -10.9509 | -46.47005 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99b84493-5856-3df5-a4d0-c4e88027e1f0 | -10.95067 | -46.39458 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07adef5e-f71f-3245-a68a-b557495eaf1f | -10.94921 | -46.38963 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c2db614-bc51-3925-8dbb-b7ebe99e68e4 | -10.93715 | -47.30328 | 2024-09-30 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a83c4e0b-2af6-339e-be8a-526ce6f574de | -10.92051 | -46.46101 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09506b31-a303-327e-a832-b8e2841a9eae | -10.8466 | -48.15428 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dac4e544-4763-379e-a52b-a928248c57c9 | -10.84452 | -48.15017 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39fe0853-ec5c-3d42-9cf5-f0ae9cfd9712 | -10.84333 | -48.15606 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 519a7ec0-7d54-36b2-b7be-67c45704d395 | -10.84152 | -48.14694 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d671b61d-bd95-309c-bfca-745feaa7479a | -10.8403 | -48.15319 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57003024-2c83-3533-a5f6-b644182db696 | -10.83824 | -48.14899 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad9e8b6b-676a-389a-ac94-c2335c9cbbf4 | -10.83645 | -48.13952 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49da0cf1-2f40-3922-8a9a-bab05aa7cd16 | -10.83527 | -48.13153 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb5b2bae-56e4-36b7-b76f-e5022b86b444 | -10.8352 | -48.14597 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4046d8d-08e9-3cb4-8c68-0d87e9346480 | -10.83428 | -48.13638 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5be803f3-e954-3a70-9215-43e7fceda9fe | -10.83307 | -48.14236 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36a943f1-6280-35ec-ad40-614dd59437cc | -10.77329 | -46.54234 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 838f1bc4-6dca-326d-95c8-1054ef924b8a | -10.77267 | -46.54556 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40c8053f-719b-38ba-b9cf-26578137411e | -10.72006 | -47.98619 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f34d7a75-7818-368e-b908-93c2ed3072cf | -10.71577 | -47.97518 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b997f3ab-6d82-3811-ac74-c507f98d3db3 | -10.71472 | -47.98051 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f2505cf-3566-304f-ab6f-c7fbf52bbfb2 | -10.71359 | -47.98623 | 2024-09-30 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45e0ec33-c6c5-3a3c-b07a-203795c9e02b | -10.51037 | -46.37393 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 480d6004-9417-3af3-896f-26d1a67fe9a8 | -10.49768 | -46.31758 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba41ca4b-5d28-3462-acde-c480e86b1922 | -10.49281 | -46.31251 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2da52efa-4cec-3364-9cf1-86b4e7e88804 | -10.4872 | -46.31132 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ec60bd6-3e02-3e73-b867-2bef7a94c01d | -10.44627 | -48.21482 | 2024-09-30 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |


[Clique aqui para ver as próximas entradas](README21.md)
