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
| 92ad9abd-9a6c-3220-9b37-096ed1bc8a2b | -5.22972 | -44.77457 | 2025-10-11 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69e3bf78-6188-3cec-aac7-0266859bfe53 | -4.41791 | -43.47152 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c9a7d144-faf9-3ccd-a823-3d81c44daa9b | -7.49152 | -42.75504 | 2025-10-11 04:32:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 06a6a590-3c81-3096-a663-a9eb49b3bb80 | -6.83297 | -42.79111 | 2025-10-11 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6c9fbb83-2356-31a5-8ef4-3c3ee430bc2d | -6.16922 | -42.54816 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 99137c40-bf9a-3aaa-a2e5-f6025f1b5f50 | -4.89461 | -45.95293 | 2025-10-11 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b02e411-115a-3762-8a54-ac0ed568dfa9 | -6.71841 | -42.20599 | 2025-10-11 04:32:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 26ae3866-c3a5-3f6d-a1bd-6dd973bab1d0 | -7.14419 | -44.1328 | 2025-10-11 04:32:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11730c3e-9157-3416-83f6-f864114653da | -4.89404 | -45.95655 | 2025-10-11 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ce28858a-3cac-3a47-8e11-1ae6992a2bba | -6.43287 | -45.83546 | 2025-10-11 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1b40dfd-580d-31be-b952-4c60caf74581 | -8.19583 | -43.3235 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| cd9a89b9-e818-3b0a-963b-82e423a2a478 | -7.7105 | -42.37333 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6315937d-da84-3da7-b171-0a8e29e54c68 | -5.84534 | -43.40224 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c479fbe5-db9a-352b-ac0d-b3f8fc02d655 | -5.87628 | -45.29426 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09f1b5fd-d15b-33cb-88dc-0d6b3e4f9253 | -7.6237 | -47.83036 | 2025-10-11 04:32:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dfc41e0-193f-3316-a033-481322e6d14d | -6.43345 | -45.83175 | 2025-10-11 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a2d7af3b-e2eb-397b-a673-d9b5f1926258 | -5.32621 | -43.08437 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7a5847bc-0fcf-3464-b88c-a56cda3f7e6c | -8.58632 | -44.88681 | 2025-10-11 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6535f245-0ec5-3123-a145-26c26ec32c4b | -7.57595 | -45.93081 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d848d39d-ecfc-35ae-b52a-757c6e11f89d | -2.26654 | -47.85282 | 2025-10-11 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f7063a37-b2d1-3391-85c8-31ce07bdb055 | -7.67641 | -42.40026 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4dceb564-a969-3c4c-99e5-5782922827dd | -5.61015 | -45.82555 | 2025-10-11 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41c9b32e-4c3a-3b43-94e5-ba62887977e1 | -5.2446 | -43.00955 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e740353-841c-3b2f-ad0d-50bed3664d6c | -7.86225 | -44.49208 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0792abd-d3df-3bdb-85e1-d757b507ecb8 | -5.4954 | -44.64771 | 2025-10-11 04:32:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae9cac4a-2716-3910-b47c-e675bb25a27d | -5.59048 | -41.10835 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c4c7cc4f-b14b-3ae3-88a7-6df870e660a1 | -6.7277 | -42.08212 | 2025-10-11 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 60aeeaf4-c581-34be-ad66-760bc2f33b78 | -4.41483 | -43.46641 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04b02ef0-384f-32a6-9ccc-b317212ca4e9 | -5.83284 | -49.02055 | 2025-10-11 04:32:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b408e1f8-0e24-31dc-a0f6-caf0ec654bc1 | -5.48228 | -48.65735 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 988b3598-31f9-32d7-8de7-1762993c882a | -0.75581 | -47.7632 | 2025-10-11 04:32:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 619c231b-6a35-3344-ba17-e82d16077eb6 | -7.85615 | -44.48195 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e7b0bf2-b8c8-3a69-86f4-7b287b0dd92f | -7.01919 | -42.74033 | 2025-10-11 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2e151a33-96ec-3902-8965-5826300721a7 | -6.16459 | -42.55122 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cef63d16-692d-3958-a773-cd2e7a7c65b3 | -7.67808 | -42.38867 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cb59cecc-d5d0-3929-95b8-037cdd38ac6f | -2.59459 | -48.12643 | 2025-10-11 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4524c786-8421-39c8-9ded-cb82773591fc | -7.36407 | -38.76156 | 2025-10-11 04:32:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cab9997b-d37f-3126-ab5d-5cf0155ea5ec | -5.86157 | -42.8545 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 1e83f621-ca06-3560-ad83-f14585f8478e | -3.74645 | -44.40343 | 2025-10-11 04:32:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9a55661-8e93-3234-ba94-fde09dc5079d | -5.70131 | -42.79119 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ddda6a18-981c-3e48-8b69-41077fa2f2ee | -5.94826 | -42.26583 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4e345b9a-b50e-37fa-9c23-4b1a930853a2 | -5.6871 | -47.90093 | 2025-10-11 04:32:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d7fc4ef-6104-3385-9aac-f4e5ce9399db | -6.85714 | -48.00934 | 2025-10-11 04:32:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b9591c6b-9384-38b6-9a19-676a291c2c6a | -3.98164 | -47.87791 | 2025-10-11 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c93bda31-3354-3342-81ed-e9983fbe13cf | -8.01123 | -44.449 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 75c36934-f88b-32cf-b710-0c7ff23e6d91 | -6.42945 | -45.83496 | 2025-10-11 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7f095ee-032a-3b07-88d8-01263e4ed25d | -6.9229 | -43.57883 | 2025-10-11 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 57f27226-a299-39ae-8cf8-57b36b8e0422 | -5.28502 | -45.26738 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a38f1976-1224-31c6-82de-d0a45441e635 | -2.8603 | -48.70406 | 2025-10-11 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17300c04-2417-3680-8cbc-97f1a286c0c7 | -7.53605 | -44.28919 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77497e49-57bb-3861-85f4-2d6053a3005f | -5.86258 | -42.84761 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 6f9edc15-f7db-3120-9920-734108840721 | -7.00844 | -46.99542 | 2025-10-11 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdc0b1cb-fcfb-3894-8b33-65a6cc9926ec | -7.65896 | -42.5797 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 02d23bfb-06d9-3136-962f-3e730190d8fd | -7.86813 | -44.45168 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f318cc5-5627-35b5-b8d7-229ad51c1287 | -4.19621 | -46.80986 | 2025-10-11 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 140e6035-4618-3aad-b753-751e523f5ba0 | -8.18085 | -43.31416 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d33f31fd-aa50-3f55-892d-1643cf4c8c36 | -7.62758 | -47.50049 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d44e5321-c809-356d-826d-36ce808662c9 | -7.71025 | -42.37584 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b1933edb-b63c-35ad-b433-29e9eab935b7 | -2.59624 | -48.11589 | 2025-10-11 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c1ae3ff-93cb-369b-9cf6-a25f5fd217f4 | -6.65633 | -45.98244 | 2025-10-11 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45e3a630-61de-3ba8-bb82-30cc45a827b7 | -5.64761 | -43.29928 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75161e03-ca02-35cc-98c7-0f0962ae5141 | -2.26763 | -47.84586 | 2025-10-11 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6442741-0e8a-3fc8-bb22-deb576c71b44 | -3.41006 | -52.60365 | 2025-10-11 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fac289e2-19fe-3c80-b7c4-68bccb5f553b | -3.98025 | -40.91488 | 2025-10-11 04:32:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63b46d12-6230-31c4-adb6-16d2fa7bf71b | -2.88673 | -49.60365 | 2025-10-11 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eaae4af1-8efe-3a81-8220-bc0f25488bd6 | -5.5892 | -41.11703 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a63a35d7-292d-3c43-9dd6-be69daf92874 | -3.11656 | -49.10345 | 2025-10-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87b08ee7-1bd6-3ac2-824e-b2a33bda0bf8 | -5.33102 | -41.56923 | 2025-10-11 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f82a9da4-9207-3db2-940d-8fb082a5d2c9 | -2.29535 | -47.99331 | 2025-10-11 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73b7c4bc-07a3-36e1-a497-a2e4290452c3 | -7.5354 | -44.2937 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bf640b9-2b40-3d48-97a5-e0be25ecec5c | -6.43861 | -45.82102 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6470c0f-f110-3ef3-91bb-e5bb43f7409f | -4.07215 | -48.03727 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82a1968e-fb92-36b0-8ec9-285b7e41c8c4 | -6.73845 | -42.15717 | 2025-10-11 04:32:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 11d859a1-2544-3875-8058-b2e42df4d06c | -5.78909 | -47.09113 | 2025-10-11 04:32:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68bf3d6e-e160-30a6-879d-10d9b14de3ac | -7.67851 | -42.57351 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f006492b-c901-38b9-89c2-c4c21ef02969 | -7.85679 | -44.4775 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84e3e769-8aa5-3513-9b15-b8b7cf8a2b41 | -4.94143 | -38.08812 | 2025-10-11 04:32:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1166df81-86cc-340a-81c0-a4bf7a994bba | -8.21438 | -43.35096 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b62957f3-7e1b-3928-bf2c-4569610882fd | -5.61122 | -42.57322 | 2025-10-11 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8f825f7d-c12e-3dff-b0bc-42ba82874165 | -6.25149 | -42.98364 | 2025-10-11 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59805c11-31c6-39d3-bbac-8ff374746947 | -5.85961 | -42.84014 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 625fa9c2-d02e-38ff-9202-f5a4b64ab172 | -7.8629 | -44.48764 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84568e2e-e57f-3605-964b-92d8bed48768 | -7.67489 | -42.56892 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f4f5c8ce-d963-3ee9-9918-f0f3e49933d0 | -8.01675 | -44.46312 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7e3e14e4-fecd-3613-99a0-398b0e0c5abc | -5.86463 | -42.83378 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75c31a18-38a1-31d3-8bb5-3039ad9e2314 | -5.87686 | -45.29037 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 839646d0-61b6-3590-ad21-1bc590f0b5a1 | -6.74261 | -42.81137 | 2025-10-11 04:32:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ba544581-7f52-31d2-9d29-648010a5c3e6 | -6.18531 | -39.69559 | 2025-10-11 04:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f389ab98-401a-3413-90c6-bdd912d32264 | -6.0001 | -44.20906 | 2025-10-11 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d0cc5348-4d2b-3d6d-9b8d-a0f71a6df24a | -5.63547 | -42.69672 | 2025-10-11 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3f6f49e9-61de-3b17-a22f-0bc86a71417f | -5.96959 | -42.26494 | 2025-10-11 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9e6b1680-2e7b-3508-ba33-d3050c3a290f | -6.45483 | -44.57327 | 2025-10-11 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc3dfe81-6bdc-397c-8954-4771ca8f8c8f | -4.34185 | -46.55198 | 2025-10-11 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e0b4cde-5de8-3297-a228-ee353e585644 | -7.35088 | -43.85755 | 2025-10-11 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c40cb550-9f29-320f-929b-6cad3f91d63f | -6.74044 | -42.85426 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ee9cd1c5-28b7-30cb-9ee3-b048a6a317fa | -4.40662 | -43.46988 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3199390-713f-35a5-b6c8-1ddbae151b40 | -7.26401 | -47.21151 | 2025-10-11 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9f1afc9-7ee5-3a3a-94b3-5aeeacb84d40 | -5.5845 | -42.82308 | 2025-10-11 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7ac01c1b-d221-32b8-8b10-46b757fc8e65 | -6.16051 | -42.55058 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 892a2108-8231-3811-a6bf-3051a206ab74 | -7.85809 | -44.46855 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README21.md)
