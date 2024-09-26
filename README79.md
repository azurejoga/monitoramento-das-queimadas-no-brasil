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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4555df14-b28d-3f14-b6b8-25ccd929d0e1 | -12.53001 | -53.50633 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12cc92db-63e8-3e72-8789-a0a9fe038b53 | -12.52984 | -53.5044 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 699683c2-fc5f-3347-bf60-bce8ee38fd52 | -12.52921 | -53.5104 | 2024-09-26 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecd76dec-e64a-3e79-918b-4ea61d7b7c26 | -14.78278 | -53.86637 | 2024-09-26 04:08:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 618bc69b-3ceb-3dff-a2c0-ee86cb77a12a | -14.7819 | -53.87069 | 2024-09-26 04:08:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e13c308c-9271-3307-bb2b-4187212b96cd | -16.62072 | -54.08789 | 2024-09-26 04:08:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 190dad17-ec5b-3c6c-8ad4-d32ae002b9b2 | -16.61922 | -54.0855 | 2024-09-26 04:08:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2684c72-8916-3003-803e-e276db21aadc | -16.61839 | -54.08942 | 2024-09-26 04:08:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8acfd6cd-ebe3-31c4-a549-f2d6d54455b5 | -16.6134 | -54.09516 | 2024-09-26 04:08:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3071afe-6f8c-37ca-a31b-658cbb85af6c | -16.60065 | -54.10045 | 2024-09-26 04:08:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89dbf926-51ce-3271-a0fa-4ae23cb61dd2 | -16.59432 | -54.10291 | 2024-09-26 04:08:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c90d6b7-3390-39ef-aa41-4b5b855d2c32 | -11.20585 | -54.77826 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 14a674ca-b6ab-3133-a94e-883de9e7d989 | -11.20474 | -54.78373 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 9dec5ce3-1d76-3d17-9ecd-8a177fd562ec | -11.20473 | -54.77977 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 4915b724-15d2-37eb-990d-90131492f6ca | -11.20366 | -54.78523 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5a5e2161-5cc4-309a-a5c5-cc52d5950844 | -11.20362 | -54.78922 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 0acb267a-8a5f-3166-aea2-076fec0a4c4a | -11.20257 | -54.79079 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e816d64f-49b5-366b-bfc0-3216e3612080 | -11.20249 | -54.79482 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| fd59906c-2a85-31ae-96fb-f59016f834e6 | -11.20147 | -54.79638 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3896fa49-7ee0-39af-9a48-f5c24e40edb3 | -11.20061 | -54.77128 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bfafc64f-d072-30bd-9119-b81827511440 | -11.20051 | -54.76733 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0d642115-6828-3b14-8c4d-fb281637e0be | -11.1995 | -54.77674 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 7aa96e9b-2052-3acd-a26a-084dac327552 | -11.19945 | -54.77272 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 045ce37c-3b0b-3659-85b1-f24157af898a | -11.19838 | -54.7822 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 59255885-bf0a-3910-b337-df5a3f48ed5a | -11.19838 | -54.77819 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 7666017a-0517-3725-94b5-cbbdfdae0240 | -11.1973 | -54.78369 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 33ef128d-77e7-3eb5-8ae9-c4fbaf19bf45 | -11.19727 | -54.7877 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 4ca85485-4848-34b4-8404-d9c44f0925b8 | -11.19621 | -54.78922 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 30e3717a-de4a-3fee-9fc4-1969efff3962 | -11.19614 | -54.79323 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 09a0d9af-f9de-3604-8eab-4cf1edb62397 | -11.19531 | -54.76459 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e775360c-d96c-31b2-b0cd-0976c4c457fb | -11.19512 | -54.79477 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4b27b3f2-984b-3ae9-b1cf-5b0cf72a0fbf | -11.19501 | -54.79877 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cb1cff21-9087-3333-9c3b-7261532476f7 | -11.19424 | -54.76984 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 10f0e21a-8739-3271-ba06-0cf6a8a8bbde | -11.19413 | -54.76595 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 93398dbe-8466-35c5-ae4f-e6b47617c9fa | -11.19314 | -54.77525 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6aef2363-72af-33d0-bce4-b2f4f039816a | -11.19309 | -54.77126 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eee2c813-b47d-39b7-b1c0-9f288fac34e1 | -11.19202 | -54.78072 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2823b07d-9b3f-3ece-8fcd-ae738e8697f4 | -11.19202 | -54.77669 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 394ea411-2d3a-38bd-83c4-560a0983e6f1 | -11.19093 | -54.7822 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b99b09f4-5e2b-369e-aeef-ed076f4da88d | -11.1909 | -54.78622 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3e6171f-ad3f-34b1-9058-9c10b47dda06 | -11.18985 | -54.78772 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 088a142b-15ff-323d-9abf-50f4a931c092 | -11.18978 | -54.79171 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1167477b-5f49-3dcd-8793-510d79c081c8 | -11.18785 | -54.76851 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 154de4e0-7a51-3b56-b5e1-0805e5417423 | -11.18676 | -54.77384 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 47d0b7e3-e221-3f5f-afcb-4cc69b8ebb78 | -11.1867 | -54.76988 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e803ceb-95b3-332c-b917-754813f13b9d | -11.18565 | -54.77927 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 812fea29-76dc-3023-b5b5-43b9f686bc1b | -11.18564 | -54.77526 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31c96887-ee87-35fa-9fad-ebb8959a55f5 | -11.18453 | -54.78474 | 2024-09-26 04:08:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0cc9ac8a-287e-3c8f-97b5-114c1f59bca0 | -11.32169 | -54.04902 | 2024-09-26 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0599108c-d9d9-3c41-a03d-bd46e0848cb7 | -11.32134 | -54.04831 | 2024-09-26 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab6d165c-35fd-3495-a6a1-c5c35325cc59 | -11.32073 | -54.05391 | 2024-09-26 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7664954-2d3e-3ca3-b676-60b0db205598 | -11.32035 | -54.0532 | 2024-09-26 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e650db5f-5a17-3c77-8b05-3be5518dbabd | -12.67445 | -54.668 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c71c785-8d7e-36b0-9a33-2c3febd26102 | -12.67345 | -54.6729 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b6f50fa-ac3d-35ec-bc7c-72460971d5ce | -12.67245 | -54.67782 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5e9b832-f230-3613-8159-c5013bd0a264 | -12.67146 | -54.68269 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39851631-b0af-3d0b-8dff-87581ad061fa | -12.66828 | -54.66659 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 188e3efb-c723-384f-8668-e4fcba8fe8d0 | -12.66728 | -54.67145 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25625dea-b787-32bc-b4ea-160b5ba308cc | -12.66629 | -54.67633 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e47119-9816-371a-b037-664b645abc23 | -12.6653 | -54.68119 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45a9ac24-7129-362c-a49f-df109e12f3bf | -12.66431 | -54.68605 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36ae7e93-6a4c-3e84-830c-a842afa7a994 | -12.6611 | -54.6701 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bc474c5-a305-3f8b-8024-aab3235a2865 | -12.6601 | -54.67498 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71719302-d703-37a9-a382-e60f8c61b5e1 | -12.6591 | -54.67988 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bb8f86e-4408-3690-8c4f-81093eb76fc1 | -12.6581 | -54.68479 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc2ef764-83af-3e63-8ec9-c70dc06c0e69 | -12.6571 | -54.68968 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7344be68-d37c-3d17-a306-cd7a53eafce3 | -12.65187 | -54.68361 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0458b73-7cac-396c-a8af-b34051b576ac | -16.58534 | -56.00302 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4c041753-c805-3459-8652-18871adb023a | -16.58419 | -56.00822 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1a5a3677-011b-3082-9414-9ba6b3470085 | -16.58305 | -56.01341 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c655a652-faf2-355c-a6d6-2d91ced49dd4 | -16.58191 | -56.0186 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| dc68030c-2c26-3e55-a509-29cd38ba8b72 | -16.5791 | -56.00158 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e15683ed-9d07-3c5f-ae33-a95c3642c0e7 | -16.57796 | -56.00675 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 847ed822-972b-3a4a-8554-c66be8df4e71 | -16.57682 | -56.01192 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8f80d83c-eb0f-3636-983f-70664b2bbe90 | -16.57058 | -56.01044 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5379cf30-94a0-30d5-b844-a614f61f97e2 | -16.56944 | -56.01563 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6cab5284-dbca-33a2-b984-e10e62fb202c | -17.09129 | -56.16443 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.5 |
| c3e68156-3357-35e2-819f-717cd2abafb2 | -17.09013 | -56.16967 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| f38f019f-1855-366b-9bd1-472e2e413b84 | -17.08508 | -56.16288 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.5 |
| 0132aa89-ad9b-3af8-a0b2-2bb949eacfae | -17.08391 | -56.16814 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| ab518a9f-1c76-3b92-aa22-e9a4033425e1 | -17.07884 | -56.16138 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.2 |
| ba19c11a-9936-3e06-a59b-d49f184c32bc | -17.07768 | -56.1666 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| ccf34743-3e1a-38e2-9c02-87a8103606c2 | -17.07146 | -56.16506 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 26bd10c7-9580-380f-9793-2edf178e01aa | -17.0703 | -56.17026 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 33ff8fb9-7ced-35e1-885f-c1090ff5f4b5 | -17.06408 | -56.1687 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| b5f71933-12ab-3c35-90be-b265ecfeca5f | -16.94399 | -56.11806 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 2063c719-1b20-3f74-9e2c-403d593d1c08 | -16.94167 | -56.1134 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4cfc1d5f-8309-3e02-bfd6-f72b74d9f813 | -16.9405 | -56.1186 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 249e8caf-557c-35b2-b14f-1c9adab21c4b | -16.86585 | -56.11521 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7c1ffc9a-1c6f-3fb1-afcb-4b8b26242f1c | -16.86469 | -56.12041 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 485a5bbe-2c7c-3901-878e-75ca1d318436 | -16.86353 | -56.12562 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a58b9d69-9a12-3186-a310-238bcb82c924 | -16.77595 | -55.95526 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b1089bac-dd23-3d88-afee-e317e5e1bcd2 | -16.77485 | -55.96037 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1596a15d-8b37-33a1-91f5-824ca8efb388 | -16.77369 | -55.95356 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 0f5efafc-9108-39ff-9160-8b0db86f657d | -16.77256 | -55.95866 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 1d8f3f2a-66e8-36bb-b9da-04fd16443e9c | -16.76867 | -55.95884 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5718e31a-922d-3d25-963b-8226b0ae8835 | -16.73712 | -55.92415 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 8e4c9426-3295-3057-8102-aabe3a0e113a | -16.73095 | -55.9226 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9862747f-7224-366f-a09e-fdb30a2756bc | -16.72985 | -55.92762 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| bc6648a2-464d-32e9-a9a0-a15eae438b14 | -17.05396 | -56.24346 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |


[Clique aqui para ver as próximas entradas](README80.md)
