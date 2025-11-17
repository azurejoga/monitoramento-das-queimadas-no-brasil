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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 674a8a7b-cf5c-3689-ac67-f5e7b366c4e4 | -7.15899 | -41.76541 | 2025-11-17 03:46:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fe0428eb-b2c4-3742-abd7-c8b84ceb1006 | -3.47192 | -49.69519 | 2025-11-17 03:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7f5e8f7-8501-3ce0-9ed3-13a566f79cfc | -7.24357 | -42.57277 | 2025-11-17 03:46:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a0136d06-1777-3ca6-8b99-898b39b0ef5e | -4.73785 | -46.38297 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6426339c-5a8a-3d3a-a528-4b51297a0c59 | -4.05724 | -47.49921 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7401c97d-4341-3f73-b35e-d8c445f74e05 | -5.7485 | -39.69726 | 2025-11-17 03:46:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 62609726-fe1b-39c0-8d9c-f16807e13200 | -6.65761 | -39.28417 | 2025-11-17 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0da98ece-5d4b-3066-89c6-1c3e23bf5f8a | -8.20788 | -43.56446 | 2025-11-17 03:46:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94777dfa-44a0-30f0-8a67-517569382cdf | -8.24822 | -41.42454 | 2025-11-17 03:46:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 723c3381-84bf-3572-bddf-3a4cf0cf7792 | -6.3548 | -41.74886 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76d42604-2d32-34b2-a541-66280aa552ea | -6.4836 | -39.76625 | 2025-11-17 03:46:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 470c4193-5388-3e8d-a19e-a5ae9294deb0 | -4.40302 | -45.83077 | 2025-11-17 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cc35d83-5842-3a15-9b70-aa22e9d33d08 | -3.30522 | -50.07531 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 251403fe-dac9-3e21-9a78-67beedfa0a36 | -8.24596 | -41.42144 | 2025-11-17 03:46:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d25e9c6-8fd8-377f-9657-923ad28898a0 | -5.51881 | -40.96659 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0beb5776-81da-3df8-b8da-5610309a94c1 | -6.35744 | -46.15936 | 2025-11-17 03:46:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce0964d5-7216-336d-b466-fa092dd8f242 | -4.06242 | -47.50499 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f31f7411-aee5-33cf-8661-65f4ed4283f8 | -6.67889 | -42.03653 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 7a445293-8c7b-38ee-af82-f53796c8ffe3 | -8.20812 | -43.56274 | 2025-11-17 03:46:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06af1dcb-40ac-3ce6-8aec-1e01166dcc2e | -4.74505 | -46.40826 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3cc157b-cb52-3c2f-8c4d-6a2046076361 | -8.45958 | -41.11791 | 2025-11-17 03:46:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5af2fa3-28c1-334b-929d-cb614a5c9da3 | -4.89286 | -44.86389 | 2025-11-17 03:46:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00359a82-d286-3533-88e4-1665af2d6e52 | -7.17866 | -39.70735 | 2025-11-17 03:46:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c8b0a3b7-53f6-3731-9030-b81350d16af8 | -3.81837 | -47.49577 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebdfc469-cc32-3d64-86b4-f386b92854ca | -5.05534 | -40.46445 | 2025-11-17 03:46:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 83a0e34d-0d12-3633-8fe9-76c1d137741e | -8.4292 | -40.3293 | 2025-11-17 03:46:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8642da9f-6508-3ccf-a9da-53572ba2a179 | -5.91699 | -44.02158 | 2025-11-17 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a90ae819-5b5a-360a-b540-004ebf62c6d1 | -4.68882 | -46.31247 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1f169be-f9f2-3d99-a028-dd7a88e8c9e6 | -4.94028 | -44.5279 | 2025-11-17 03:46:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fac2d3f-c083-3c7c-b740-87382ef6be20 | -4.09807 | -47.11526 | 2025-11-17 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73eb8265-7ba9-36b4-b9c6-c3dac9aef605 | -3.47411 | -49.69615 | 2025-11-17 03:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 712310ab-3678-32d5-828d-bd690c11c340 | -6.39391 | -42.28708 | 2025-11-17 03:46:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d86171e8-4de2-3ddf-ab43-caeb29c9fde4 | -4.10475 | -47.11208 | 2025-11-17 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a5ea46d-290b-32cf-b845-0a6e6e5514ac | -6.61789 | -41.46668 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 243623bf-4e2c-359f-aa38-d1d57705033e | -6.68641 | -42.04149 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 8ec8d156-06e9-3e3a-82ff-e19b94e7c756 | -4.01766 | -48.81369 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdd187de-1f21-37ac-9726-6c0c3e6b429e | -5.88085 | -43.97874 | 2025-11-17 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56dffa3b-3642-30aa-b492-570d1038c74a | -5.03806 | -43.60285 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e9767b1f-dfa0-3aae-892f-28008fc40177 | -6.61341 | -41.46778 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 089dc7e2-f6d6-3585-9d09-cb057b3c6cd2 | -8.11858 | -43.53128 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca492009-8135-3485-8d45-74ea7822d4b8 | -6.6736 | -42.04313 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a0404258-27c3-3712-89f0-9ce1c4dcf4cf | -6.67706 | -42.0474 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5a29b00e-370a-3e50-a0ba-f0e9463182d4 | -5.46977 | -40.96572 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b2fb758e-f7c6-3327-98e9-ca4b9da7e841 | -4.69372 | -46.31756 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9766571-429e-3efb-b280-5116e60ed125 | -4.09665 | -48.02475 | 2025-11-17 03:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84ea9217-4fbe-3abf-b316-9d7a73676373 | -3.77688 | -50.14404 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7352b29e-3cd4-323d-bb61-c382053d035f | -3.4586 | -50.00024 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ad47058-6e6e-3328-9224-a0e6d4a5267a | -5.47445 | -40.96138 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b5364be-6294-3264-bf1b-1f8ea99648d9 | -6.68459 | -42.05235 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3eb2445f-e293-3cff-bbfb-c14a48c266ab | -6.34563 | -41.75453 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 041e36bf-3d4c-3845-bcec-b92a2bdaf3c2 | -7.08715 | -35.04932 | 2025-11-17 03:46:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca6951a1-ef8d-3931-bf64-93c6e3f441d4 | -6.68296 | -42.0372 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 390d77da-924e-36f9-b9ec-2fdb3e800784 | -6.48277 | -47.19325 | 2025-11-17 03:46:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b995a98c-f206-38be-a17e-b5214e88a663 | -6.82067 | -39.14835 | 2025-11-17 03:46:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e6c6808-4111-328e-80c1-7c198b2bfb54 | -8.77983 | -40.59375 | 2025-11-17 03:46:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 812d359f-ca41-334a-bdcc-3a456e5211a2 | -5.27093 | -44.1787 | 2025-11-17 03:46:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34772dac-04f8-3714-98ad-886cd9709b18 | -6.37057 | -42.29866 | 2025-11-17 03:46:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5d21ffe3-0766-3f4e-8a13-640c079f8902 | -6.34384 | -41.79063 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c7216f9f-0e7d-3fe6-8936-6ef97a516553 | -7.84825 | -40.58253 | 2025-11-17 03:46:00 | NOAA-20 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5f37b2d5-c3ea-3652-8cbe-535c64c61c98 | -3.41011 | -50.12339 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ad1b790-39a2-36fd-b756-c2ab0f51d0d4 | -7.71354 | -42.94644 | 2025-11-17 03:46:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 372756b9-28d5-33a8-a47c-75abb03a70f6 | -6.815 | -39.13954 | 2025-11-17 03:46:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 61b92405-9f9b-3e39-98e4-4fe4078ef154 | -5.92722 | -38.11986 | 2025-11-17 03:46:00 | NOAA-20 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80ecc255-a352-308a-bad9-99900c378126 | -6.22313 | -47.24317 | 2025-11-17 03:46:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec6e6ea9-e3b4-3c6f-bfec-916f6a953a94 | -6.35615 | -41.74889 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f73ae23e-ca95-34cf-8ebb-54d276e23b7d | -6.0822 | -41.61281 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7509bee-b7e2-3e4f-8df5-83a93f8f09aa | -7.55407 | -36.43213 | 2025-11-17 03:46:00 | NOAA-20 | SÃO DOMINGOS DO CARIRI | PARAÍBA | Brasil | 2513943 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 37e66b69-be90-3822-9927-e05d8e2bc5d5 | -6.93637 | -41.53396 | 2025-11-17 03:46:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 474f790d-1ff1-3c22-8c17-a42e7c891654 | -7.26436 | -48.02401 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75f2448e-df3e-3540-aa8d-b084e912f951 | -4.42316 | -45.55369 | 2025-11-17 03:46:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2c0bb10-e677-3540-ba66-82b3ce22ed83 | -4.25964 | -46.41195 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 462619df-de98-3c6e-94d0-1e9df2c3c7ef | -7.09004 | -42.73438 | 2025-11-17 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b64037d1-3f2b-33e7-bfc5-045361d15339 | -7.86778 | -37.56625 | 2025-11-17 03:46:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11637bdb-e14c-3577-b45c-ad8753847576 | -4.65767 | -46.74061 | 2025-11-17 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 33292226-3e41-3e29-accc-18aa23c0eeaf | -7.22144 | -47.98835 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 59e35fce-dc13-3957-9b50-373cfc381db2 | -5.76174 | -43.02273 | 2025-11-17 03:46:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 16926e75-aa92-39fb-8707-808ab0af86ee | -6.67991 | -47.39259 | 2025-11-17 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c86cdc7-dd2c-3eaf-a750-cef56a88cfc2 | -7.25918 | -48.01852 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10bf659d-9b30-301a-b906-8095237d0f1d | -7.2473 | -39.35299 | 2025-11-17 03:46:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae869df6-8c6d-3d70-8951-f61cd1de4da0 | -5.8824 | -46.44622 | 2025-11-17 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5893045-87ff-3082-bf95-e9569bf6c09c | -5.58946 | -41.06866 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 496054f8-9957-3b30-9882-64e5c28f334d | -6.81658 | -39.15159 | 2025-11-17 03:46:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 440905ba-b59e-3d54-92dc-ff21bddbb744 | -6.68113 | -42.04803 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 57e0ef1c-253a-339f-9ed2-ad8e8ad40013 | -5.04269 | -43.60367 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c96606ad-1a3d-3d75-931c-80d4f7cf80b7 | -6.44334 | -44.22009 | 2025-11-17 03:46:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9de2c3d6-f23e-3809-88a1-f7b8a094f110 | -5.46428 | -40.97501 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3d44a199-f4c5-3811-a973-1efc9f24ae18 | -5.47365 | -40.96627 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f27fead2-7036-3ed3-ac59-7011cc5a0448 | -5.11003 | -46.23161 | 2025-11-17 03:46:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9e4a08b-9675-396c-aeca-55133abc68c7 | -3.81147 | -47.49918 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a77033b-3000-3080-aee7-3382e1692bca | -3.80915 | -48.92349 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9f13014-2760-3c35-8b3f-7d291461d973 | -8.38321 | -41.85505 | 2025-11-17 03:46:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2afe41b6-02ac-3a58-ad86-d57ad24737e9 | -7.12828 | -41.66314 | 2025-11-17 03:46:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 644fe4cd-a1c6-39a8-b978-02e891e390f8 | -3.83584 | -49.80988 | 2025-11-17 03:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a405d4a-1cdf-33ed-a215-b0badcd1ed86 | -6.61398 | -41.46596 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ec026d77-fb6d-326e-b5d7-a36235877acc | -4.68814 | -46.31644 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2840569f-6163-3d55-9048-3f58d4bb0a41 | -6.93128 | -39.62448 | 2025-11-17 03:46:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 270a7ee6-09bd-33cd-8210-d8b43287dd2e | -3.77779 | -49.25434 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb715488-1229-3154-a1a0-09ba026b807c | -5.88288 | -46.4479 | 2025-11-17 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f0b3c55-8cd1-3570-bdb9-9d7d2e424727 | -7.7051 | -42.94476 | 2025-11-17 03:46:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c4a99f51-a0d5-3b0c-a78a-4afc75316a5a | -6.67829 | -42.04011 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |


[Clique aqui para ver as próximas entradas](README15.md)
