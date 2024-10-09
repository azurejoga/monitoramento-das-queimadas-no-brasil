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

## Dados Diários - Página 214

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4102adba-e197-33c7-b92e-248256ac90c5 | -10.71379 | -64.16175 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6552fa0-dad1-3c77-aeb1-9a04612bc677 | -10.71075 | -64.15391 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 269efdec-ba8b-39c7-b4c6-f6af2d9e2f53 | -10.71023 | -64.15753 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4c37e95-c1bc-3ca8-9785-876f7d15d0b2 | -10.70666 | -64.15332 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f75b26a-3ca3-3201-b338-9368c9908670 | -10.70632 | -64.1264 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 364317ce-9cba-334f-baac-e2ec78a5e720 | -10.7021 | -64.15611 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 672fd5cd-de01-3020-9c1f-a39e073d3f76 | -10.64805 | -63.97242 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 095cc875-b530-3eec-bb58-fb0334366e1a | -10.64755 | -63.97609 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e060edc-2404-3f2c-994b-08a2f3c839a6 | -10.64725 | -64.54089 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a74cc91-1610-3fef-9a8a-3323487320ff | -10.64341 | -63.97553 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a06ae348-5540-3e08-a2f3-dedf6e3f1416 | -10.64326 | -64.54034 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e506609b-1e72-3f8c-bd32-812af73f3dd3 | -10.64277 | -64.54379 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf9e88b1-24a7-39cf-af3b-322e87d14e6e | -10.6261 | -64.43147 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e060d1-b570-36d0-af3b-e4de38a80379 | -10.62559 | -64.43506 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70c69945-71e2-3c1f-b51a-5965f51a5702 | -10.59563 | -64.02705 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7aca2f36-533c-3da2-bbd2-661bb8baf5fc | -10.59509 | -64.03088 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4c95387-0a9d-307e-bd99-8f2de7bebbf7 | -10.5915 | -64.0266 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49a7af03-dd81-3500-94b7-785f1b8ba048 | -10.59095 | -64.03049 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fb5ec66-1b19-381a-a0a0-16e00abc7b06 | -10.58646 | -64.00266 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 276798d9-baac-3f1c-b2ca-3a5fa436ab9a | -10.58594 | -64.00636 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 796fff00-4cea-3361-a6e6-c20d012c1724 | -10.58181 | -64.0059 | 2024-10-09 05:55:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1169964e-6742-3d1e-9bf8-9e40068150ea | -10.58159 | -64.03751 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b918a82-9185-378e-a48c-ea7d6d3ffe3c | -12.47925 | -64.0239 | 2024-10-09 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23cf2fb2-8822-356c-ba07-ac8db43e9a30 | -12.13896 | -63.36623 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6b094e0-5e39-3680-b0d4-5f2279ea9eb0 | -12.1357 | -63.35692 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e767e006-a334-328b-9936-c4b71c1c0722 | -12.13513 | -63.36127 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d26c54bf-9aa4-362a-a4c6-fb1928de6f13 | -12.13457 | -63.3656 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66f00c1a-12e0-3fed-98f3-0d1ac0f36e58 | -12.13074 | -63.36064 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30e7af84-75b6-34a8-86ee-9dfe2b37f733 | -12.13017 | -63.36499 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37b8e95a-fe84-3509-8e3c-5e73960405dc | -12.11965 | -63.84264 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f8409ee-a50c-31b8-b8f8-827b36ccaca6 | -12.1191 | -63.84668 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65787fa4-f2fc-3773-a0d6-184bb9c62c06 | -12.11485 | -63.84607 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db79c5b2-6e9e-3f7f-bfb5-bce4841cf2a7 | -18.65142 | -57.21332 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 23decafe-02b8-3381-a274-31078f23a47f | -18.64698 | -57.20836 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1d03aaab-23c9-3008-ae18-78a9c93bae35 | -16.12891 | -57.56323 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 91fa159a-abc1-3e65-b50a-1bbcaec0fb10 | -16.12847 | -57.56779 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0b7a5218-44ff-341a-902e-00e38bd60e72 | -16.12215 | -57.56266 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4bdd2f89-21bf-3eb4-98b7-3a359fbaf82a | -16.12172 | -57.56726 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2de7c8cb-d92d-3f3e-80d7-f612c693b63b | -15.95194 | -57.21365 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e0c9b695-c5bd-3e8d-bdc4-bb1afec5ad6b | -15.95132 | -57.22029 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26e4f54e-a282-3726-b15a-4f4037e3d093 | -15.94501 | -57.21364 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7ce93c8d-631f-3013-a7f3-faff2044e675 | -15.94445 | -57.21969 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 81a63369-56bf-3916-80ba-15b81376e80b | -15.93822 | -57.2122 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dce93aba-2571-356a-8e28-6b34d589bb65 | -15.93731 | -57.21357 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fadb7d3e-d42e-3784-b81d-674a08c5a0a9 | -15.60246 | -57.36298 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 963ad84f-2b3b-3b61-a7bd-3b9258f2e6a4 | -15.60198 | -57.36806 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 933a19a8-87cd-3455-9794-a5fa9864a535 | -15.60151 | -57.37302 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da3f6034-2b64-37aa-9c2e-1316bbe8284c | -15.59998 | -57.36433 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bc6a015e-39c4-3b1d-b477-99d77e95d07d | -15.5995 | -57.36908 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0747ddab-4f1e-3b55-a648-4b8126e7c9ce | -15.59575 | -57.36156 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86cf93b8-016d-3b1f-a319-9ad7450b8301 | -15.59527 | -57.3666 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a91acbd0-bde1-3f0a-8bdb-0391b400f421 | -15.59328 | -57.36283 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6c2d6d5e-398e-35ea-8950-a7aa93b7d881 | -15.59279 | -57.36768 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d2bdea04-00e0-3958-8668-83e9058fe3d2 | -15.58856 | -57.365 | 2024-10-09 05:57:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 69307d01-38ba-3ac7-a8a8-a72136c25875 | -15.55032 | -56.64323 | 2024-10-09 05:57:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e81c023-9d3d-365b-8ea8-f5ae01973f52 | -16.62431 | -57.11468 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a7105309-e019-34d7-b016-9315b58ef34a | -16.49135 | -57.74384 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| df99dc43-073c-309d-9e28-9a571fb135e6 | -16.48466 | -57.743 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d9aa0230-5df4-397b-84b0-2ad0ddde8700 | -16.39406 | -57.69627 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5179fdff-d35f-334f-81a4-b657c5b567ee | -16.3935 | -57.70205 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8724d9fd-3f0f-3b58-80f5-49d6e6b2760d | -16.39029 | -57.70264 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f263c2a5-8ec8-33c4-98ae-d0dacc607069 | -16.38304 | -57.70791 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a07c040c-6373-3c84-885c-e4895771a0f2 | -16.37632 | -57.70727 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e21b8cce-4603-3ec8-abd9-dfed5346e77a | -17.16329 | -57.41785 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 64c4963f-64bd-3005-9c9a-84b694bd7c3d | -17.16272 | -57.42437 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c4766d47-2cd5-309f-a597-14d937a7d120 | -17.16215 | -57.43089 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| d3f8eab4-43c8-3717-8c05-b27dc7b14666 | -17.16155 | -57.42926 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 5f458f4b-0f9e-39c7-8f8d-463d11fdff6d | -17.16101 | -57.44395 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 57d291b3-e466-398f-ba63-d3095ecf4c74 | -17.16094 | -57.43578 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1ef5f26a-3506-3498-b091-cae61ea58701 | -17.16033 | -57.44227 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 5141dc7b-8211-3072-ba3d-0ccb38db188e | -17.15972 | -57.44875 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 0fc69125-8a4c-3cb2-a57b-650bfa075997 | -17.15878 | -57.30951 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0402e6a4-89ab-31c6-a1f6-b418efbdd77c | -17.15817 | -57.31615 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0f730abd-b61b-32be-8633-c8fa9d8d4f64 | -16.98359 | -57.47085 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| f52addc4-0797-3df5-a94d-8ea63be5fb22 | -16.98301 | -57.4773 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| 405ffa85-4a10-3d07-b206-52c7341e1b49 | -16.98243 | -57.48373 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 96988be0-9416-3a92-aadd-e8e0e7b165dd | -16.97676 | -57.47009 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| 1a5daaa7-0e1b-30e7-a8fe-c0aa75d09190 | -16.97618 | -57.47653 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| cf1f6971-668a-34c2-922a-f8926485ad20 | -16.96935 | -57.47573 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| e7dae00c-9a48-3a4b-836e-57db8c7a8b40 | -16.96877 | -57.48216 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 355c494a-165c-3471-9164-e0439e3649dc | -16.9654 | -57.44274 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| dfad5d8a-605b-3bcc-bf51-6567a3ab2b7e | -16.96482 | -57.44917 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a52de1d4-f088-382a-b2e9-9f38b457d5dc | -16.96426 | -57.44421 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| e2715a29-0574-3d49-829f-ec3fee542e16 | -16.96425 | -57.4556 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 7dded373-1c86-3ae8-9c69-b48072ed51c8 | -16.96367 | -57.46208 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| a18ad1a0-4f3b-3cbf-90c8-9901a7271f71 | -16.9631 | -57.46854 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 9800f271-9325-37c1-a07c-b05ba7e9b789 | -16.96303 | -57.45709 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| c9c2440d-291d-3320-8634-79b92c2886e5 | -16.96252 | -57.47497 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 8c52cab0-eb0c-3fa3-8c31-9952d7901704 | -16.96242 | -57.46355 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| b6b63451-2eec-37c2-bc8e-e6bf1d3dd380 | -16.9618 | -57.47001 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 9fe88a88-53df-33cd-96c3-530c9da208d6 | -16.95856 | -57.44196 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 3c715969-765a-3129-8b59-28390b03b96c | -16.95798 | -57.44841 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| f23d297e-8fda-341f-af30-9c5db80b048a | -16.95743 | -57.44347 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| b7ce85ca-5daf-36b6-843f-453ebf672e62 | -16.95741 | -57.45485 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 85fe9089-2a32-3dab-9582-1d1af2ea5a6f | -16.95684 | -57.46132 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| f6d76303-4176-3b45-a5bf-c4e7d92e77bc | -16.95681 | -57.4499 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 977de34e-09b2-3e6d-89ef-415b4ffc7fd7 | -16.95627 | -57.46778 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 93bf75fc-be79-3441-8b85-b0de8ed7824f | -16.9562 | -57.45635 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| cdb8b952-ef28-32b8-99f3-43d6d9a3a393 | -16.9557 | -57.47419 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| e093bc23-0cb0-3337-a2b2-d34b6df662c4 | -16.95558 | -57.46283 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |


[Clique aqui para ver as próximas entradas](README215.md)
