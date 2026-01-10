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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0d813a4-f773-3b08-9b51-c8dac5b1982e | -12.3984 | -58.019501 | 2026-01-10 00:19:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c05fd14-7406-356f-8e21-906955b5c65c | -12.2916 | -57.368301 | 2026-01-10 00:19:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aff005bf-90af-388d-9aa5-bd8b76f5d925 | -2.6247 | -51.932499 | 2026-01-10 00:19:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1586a5b-95a8-3fd3-82be-7dd48f6eb7eb | -3.4485 | -50.115299 | 2026-01-10 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ffb1103-2899-33eb-b198-532fffe5b50e | -7.4862 | -45.578701 | 2026-01-10 00:19:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63393874-4f55-3b4a-8862-5ed45423cd01 | -2.3573 | -45.5653 | 2026-01-10 00:19:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc76e1bc-03ff-3433-b0a6-b00ab176342c | -5.4481 | -39.612 | 2026-01-10 00:19:00 | METOP-B | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3e9d3d5e-16a6-3bb5-8271-9dbcb81ea87d | -3.4501 | -50.122398 | 2026-01-10 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec000d92-c16e-3e9c-bc20-f13c3ea94452 | -2.3603 | -45.577999 | 2026-01-10 00:19:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8a4b6a1-b9b5-3113-b90a-f850a850fa3c | -11.8259 | -46.5951 | 2026-01-10 00:19:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a7acce0-2eab-3a58-9115-52ff1225a993 | -1.6924 | -45.797501 | 2026-01-10 00:19:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4833bc2f-f33e-3a10-8898-79efdb31f877 | -5.465 | -39.638401 | 2026-01-10 00:19:00 | METOP-B | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 816a16d1-20cc-35f9-b8c3-13676d4bacea | -12.3949 | -58.001499 | 2026-01-10 00:19:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 810cf703-0868-31e6-b1f4-8f49feac7259 | -2.8979 | -49.375401 | 2026-01-10 00:19:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9cd34f-f80e-300b-a440-d35375ae0dfd | -1.6035 | -53.9771 | 2026-01-10 00:19:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 497c8606-63fb-329f-a207-a8e4a7c40a91 | -9.0437 | -46.9702 | 2026-01-10 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e17977ff-7402-33c6-9e3d-3e12f708ffc7 | -12.4144 | -57.9977 | 2026-01-10 00:19:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0897b9a9-6da8-327a-a4cd-34737456fb24 | -12.3852 | -58.003399 | 2026-01-10 00:19:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5158b93c-a5a3-3037-ab32-58275fd75de6 | -13.7803 | -43.223801 | 2026-01-10 00:19:00 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 15960dee-1580-3e3e-bf8e-d7034334497b | -20.712 | -47.2705 | 2026-01-10 00:19:00 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b1769c67-6de5-38ac-bddd-fdbb4727b30d | -1.7021 | -45.7953 | 2026-01-10 00:19:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e229a250-fa9c-30c7-b3be-9ff1e3da3276 | -2.3476 | -45.5676 | 2026-01-10 00:19:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a964dd69-8f46-30c2-8efd-4d3a4fcdaa3f | -20.2276 | -40.2159 | 2026-01-10 00:19:00 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e5dbfea-7252-3798-a1ef-1ae43db88b73 | -7.4884 | -45.544399 | 2026-01-10 00:19:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab4b08c9-2d06-3596-8502-e9b0e45306ae | -12.4081 | -58.017601 | 2026-01-10 00:19:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbe1981f-c785-3131-9302-073e5c27dea7 | -1.5396 | -47.1833 | 2026-01-10 00:19:00 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7f6635-b868-35a2-b5c2-6eae33d41592 | -20.3934 | -50.735699 | 2026-01-10 00:19:00 | METOP-B | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe503eb9-8093-3c51-a76c-450619ae3901 | -21.530701 | -48.689899 | 2026-01-10 00:19:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a92b94c6-528c-36a0-bd7c-93198bfadda9 | -7.4837 | -45.568001 | 2026-01-10 00:19:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 883c54ac-e560-38c1-a10c-4e2772374205 | -12.295 | -57.334202 | 2026-01-10 00:19:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae06325e-9a00-30f3-ba43-53b73107cfe9 | -1.3275 | -53.166901 | 2026-01-10 00:19:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b47ff44-7778-375d-a8d9-502687efa56f | -16.0959 | -56.707298 | 2026-01-10 00:19:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c79a00db-e2a1-3116-8975-6df2e8ce14f0 | -12.4011 | -57.981701 | 2026-01-10 00:19:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62ff6d6f-9cc7-3b17-af4c-f02413dbab9c | -1.1326 | -47.112499 | 2026-01-10 00:19:00 | METOP-B | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de6738c6-c205-3c7a-897c-3429077abde5 | -7.4909 | -45.555099 | 2026-01-10 00:19:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac854b0d-2732-332b-ab91-64df5f7a2ef1 | -0.8744 | -51.986099 | 2026-01-10 00:19:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 37957320-5968-3879-b75f-bc832d4e0242 | -12.4046 | -57.999599 | 2026-01-10 00:19:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecce54e7-0374-3f1c-ad15-9f072e42a911 | -22.132799 | -48.087002 | 2026-01-10 00:19:00 | METOP-B | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 124bd2aa-2c12-3b44-83e6-633845dd86f0 | -0.3667 | -51.611301 | 2026-01-10 00:19:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 89f22a59-d90d-3ebe-87ec-fd74b6136196 | -1.6915 | -53.181702 | 2026-01-10 00:19:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 652c0102-d420-3cc3-bb4d-0f3bfa63f537 | -7.4943 | -45.576 | 2026-01-10 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6045c93d-f113-3b61-baf0-4ae3a199910e | -12.3946 | -58.0307 | 2026-01-10 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 8a4d96fa-1f1b-3c62-9b58-fa8958a90011 | -12.4135 | -58.0292 | 2026-01-10 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 72d7d817-7874-3384-9336-1f3187c45d27 | -12.3943 | -58.0506 | 2026-01-10 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 6c4da013-ed40-3f41-a454-9afb75a918cd | -12.4133 | -58.049 | 2026-01-10 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 95aeb3d7-bb8f-3974-9340-d14890cfdcaf | -7.4943 | -45.576 | 2026-01-10 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9017d08a-cbdc-3e5c-8640-2e63fa9782d0 | -12.4135 | -58.0292 | 2026-01-10 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 100c6a7b-4684-3da2-8ea2-ca544df22514 | -12.3946 | -58.0307 | 2026-01-10 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 3e2813fd-02f0-3990-befb-daa927837a73 | -7.4755 | -45.5777 | 2026-01-10 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f1cf41e3-2c61-3f05-adf2-c6dece4b4711 | -12.4133 | -58.049 | 2026-01-10 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| d14f8ee1-981b-30d9-a3c2-ef5438424f15 | -12.3943 | -58.0506 | 2026-01-10 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 5bd544e5-09cd-3d51-a314-3e8eebb241ba | -12.4133 | -58.049 | 2026-01-10 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 52f560c6-95f9-3461-8438-c716f7f15ae1 | -12.3943 | -58.0506 | 2026-01-10 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 4388d6f2-0b37-3161-829b-61185aae37f2 | -12.3946 | -58.0307 | 2026-01-10 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 194.2 |
| a861db65-ec9a-35fe-872b-81c3195f1b6a | -7.4943 | -45.576 | 2026-01-10 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 50496114-6794-388a-82fd-579f24abcd0d | -12.4135 | -58.0292 | 2026-01-10 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| b26177bf-a122-314d-a56b-55a8dbc0dd0e | -7.4943 | -45.576 | 2026-01-10 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 3ee455a6-a2f4-3b40-8f68-76841b4d2530 | -12.4135 | -58.0292 | 2026-01-10 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| fed99364-2d74-3833-870b-3708b70f70a0 | -12.4133 | -58.049 | 2026-01-10 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 20647b3b-1eb6-3528-ac74-0e727d7011c3 | -12.3946 | -58.0307 | 2026-01-10 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 27bfaad7-0a25-3c01-a7c9-7467679389f3 | -7.4941 | -45.5986 | 2026-01-10 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 48280c6f-4b38-37a1-96f3-0bc9b77a4d86 | -12.3943 | -58.0506 | 2026-01-10 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 5cbc13e9-e9ea-3e4d-9e68-454d3f6efff5 | -7.4946 | -45.5534 | 2026-01-10 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e877ad9d-b82c-3138-925b-6c87ec6fca92 | -12.4064 | -58.017899 | 2026-01-10 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54bf3d09-d2d0-3a39-b9d7-3defdfda37c6 | -2.1462 | -54.3853 | 2026-01-10 00:58:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d21ad744-c532-3297-a750-9c90d6cf66b9 | -12.3993 | -58.033199 | 2026-01-10 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d898eff3-2e0a-3e0b-8ae6-b69eee81894b | -16.1049 | -56.741901 | 2026-01-10 00:58:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98fae1a1-710f-34e5-9969-7a009971ac08 | -7.4908 | -45.585098 | 2026-01-10 00:58:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37c1b016-f374-38a0-9685-4c352704c4c1 | -7.4936 | -45.554298 | 2026-01-10 00:58:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df82d9e0-c9d2-3988-84ba-3b46895fa0f8 | -1.3228 | -53.176899 | 2026-01-10 00:58:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62630503-9329-3988-bedf-f40e0b073af4 | -9.0385 | -46.975201 | 2026-01-10 00:58:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f92cb0dd-68b7-32fa-821c-691ae8441c7b | -3.4523 | -50.120602 | 2026-01-10 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 925caea6-c573-3071-bff7-3bd997893083 | -16.0951 | -56.7439 | 2026-01-10 00:58:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 113d55f0-812f-34e7-a1e8-7fa65f734536 | -12.3923 | -58.0485 | 2026-01-10 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7de060b-1682-3d96-b24f-6205e1b19cc2 | -11.8304 | -46.601799 | 2026-01-10 00:58:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36724503-885f-3e13-8cb0-a07d42ce143c | -3.4445 | -50.131302 | 2026-01-10 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1f9ba9-5679-3dcb-a011-2094d3e756e5 | -12.3023 | -57.356899 | 2026-01-10 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62a43ab3-a8e5-3b98-8b06-83627af933d8 | -1.7082 | -45.804501 | 2026-01-10 00:58:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2d7648d-ea8d-3ac4-9ad6-e70837056a37 | -7.4971 | -45.568501 | 2026-01-10 00:58:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4991a47f-2869-3d5b-b5d2-2e991437f171 | -7.4838 | -45.556702 | 2026-01-10 00:58:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98f776d9-5379-374f-aeda-ca9645757f22 | -1.6985 | -45.806801 | 2026-01-10 00:58:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4802e274-1051-3697-9a3e-1ba76b726446 | -12.3869 | -58.0219 | 2026-01-10 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae32094d-7b8a-3cd6-8284-6d6ef7a831e3 | -3.4425 | -50.122898 | 2026-01-10 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4b38b78-7a19-3f24-932e-e11ca4ed6f9d | -12.4091 | -58.0312 | 2026-01-10 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0c8063f-1fff-3627-9a54-90f95f96aa2c | -2.6288 | -51.950699 | 2026-01-10 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f92a626-0a95-3d9e-a3d0-0b9911a4b413 | -7.4873 | -45.5709 | 2026-01-10 00:58:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24e8509d-8d0c-3286-9bae-251ef6a728d0 | -12.3966 | -58.019901 | 2026-01-10 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d83c003f-28f1-366a-89ad-7a41fcc7bc51 | -2.6272 | -51.943501 | 2026-01-10 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8d31baa-27b1-3427-b1aa-b2571063f463 | -12.402 | -58.046501 | 2026-01-10 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9288709-72e6-3395-ab0f-45f6609a7321 | -2.362 | -45.581001 | 2026-01-10 00:58:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5025a3b0-94f7-3168-aeb6-68d819f1eca4 | -3.4543 | -50.129002 | 2026-01-10 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 618551a4-935e-36b5-bcb5-f92e76c64be7 | -1.6006 | -53.983601 | 2026-01-10 00:58:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a91c81f-aab0-3281-8af7-d6fb6d661118 | -12.2925 | -57.358898 | 2026-01-10 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59f848c8-6f16-3aaf-b92b-27acf1c5e5a5 | -20.7101 | -47.283699 | 2026-01-10 00:58:00 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 83ca87b1-8366-30ae-8ee6-0f3fdf212ec3 | -20.7083 | -47.275799 | 2026-01-10 00:58:00 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 999955c6-841c-363c-b70d-8eb4485f9e6a | -12.3896 | -58.035198 | 2026-01-10 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d421523-a070-30fa-a065-8a039909708c | -12.4135 | -58.0292 | 2026-01-10 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 83a2cfc8-6766-3553-8f93-7c764ca6ec98 | -12.4133 | -58.049 | 2026-01-10 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| dd8abe0a-43f6-3eda-88b1-45af30c413b7 | -7.4755 | -45.5777 | 2026-01-10 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c43a60aa-2a3c-39b9-a200-065b526c39e4 | -7.4943 | -45.576 | 2026-01-10 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |


[Clique aqui para ver as próximas entradas](README3.md)
