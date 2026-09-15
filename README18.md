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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e113f06-3a1e-322f-a353-b7fb9c14d1a4 | -7.1678 | -43.52869 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 75784f8b-d3e4-3c5f-8e33-56da79dfb37c | -5.55458 | -43.44254 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 70061498-76af-37a6-8dfd-2653e28a32e1 | -7.08962 | -42.13631 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 257398b6-b28b-3d1e-901a-b197920cd98e | -7.15048 | -39.53479 | 2026-09-15 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3df2bf9-9971-3da8-a93e-4f0eec89e0a7 | -6.26198 | -41.94946 | 2026-09-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8f9c40c2-7bee-3f7f-8e2b-5eaac40fc034 | -7.10034 | -41.80893 | 2026-09-15 03:36:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8d302b2e-2482-31b0-8e2c-7ffbc3cdec36 | -6.79071 | -43.18361 | 2026-09-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b59513b0-8398-314e-81ec-ed5340c5192d | -5.55588 | -43.43494 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3a9824d0-f5bf-3368-b008-ec41fb082ad4 | -7.02133 | -44.62772 | 2026-09-15 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46148ce4-10a9-3b44-993c-0511d9587fea | -6.26254 | -41.9755 | 2026-09-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b2b90cd1-1952-308b-8c39-828223a6bc40 | -2.98837 | -39.97425 | 2026-09-15 03:36:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8b517d94-bd66-3016-8f0d-f0606c54b3c4 | -7.29883 | -42.35524 | 2026-09-15 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24f8790d-e37b-3a4a-a36f-c114e0579355 | -7.08506 | -42.10765 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 53cc3100-943b-3097-a808-2ea3b0a40a83 | -4.6748 | -42.08066 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a33fa316-00a1-3512-9834-608c5a0908c3 | -7.24373 | -39.28164 | 2026-09-15 03:36:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dbee0bb5-dd2e-30c5-a305-93a97bc58243 | -6.74072 | -43.09114 | 2026-09-15 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6877f737-60bc-3719-8d88-79d2dbca83a5 | -6.76908 | -42.74614 | 2026-09-15 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b93f0d3-0eae-3ede-8fe1-872dc0a847a3 | -6.95933 | -44.54275 | 2026-09-15 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1f17ed88-bcb6-3200-bff1-3a3a8e899b56 | -6.80533 | -43.17928 | 2026-09-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| beb77355-c6b9-394a-b18e-565b2c7508c4 | -4.66805 | -42.08916 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 64d47b15-ad47-3a54-8c5c-4af64201b27b | -7.06261 | -34.96303 | 2026-09-15 03:36:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 58eb385b-835d-393f-86f8-70db42c4eafd | -6.61894 | -44.20221 | 2026-09-15 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e446cee-6306-3614-ab9e-1e2b9e8316af | -7.08669 | -42.12714 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a54ace3d-c991-38fe-95fc-8ec39c42ee52 | -7.55672 | -41.84829 | 2026-09-15 03:36:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43cff220-4f19-3103-9424-c59ee6cb1754 | -7.08009 | -42.13208 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f5420c54-4775-3b5e-959a-a8265fbd2b17 | -3.96123 | -43.1136 | 2026-09-15 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 255d389e-92fd-314e-93f9-8b41b91d372f | -7.08457 | -42.10598 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| acec7255-6ee9-3ef4-be0d-9d53bbae4c36 | -4.95587 | -45.14445 | 2026-09-15 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5e942fdc-4c67-320b-b699-db7bbd53afda | -7.47967 | -42.11792 | 2026-09-15 03:36:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cc62869e-f275-3e4a-8e77-621d4529ab60 | -7.16966 | -43.52339 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b5251943-7c61-3131-8e62-1c7462b8f488 | -5.60679 | -43.56388 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 079d5ecb-7085-3df8-8d62-1f1d83b08aa3 | -4.67838 | -42.09093 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1b8784c-5325-34c7-ab39-1c9b2033e44e | -7.16353 | -43.52611 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2a35f236-be76-39b1-acbf-c04b0023df8f | -6.6141 | -44.20076 | 2026-09-15 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6191d712-4a76-353f-a086-1272b357dce1 | -3.37145 | -45.09043 | 2026-09-15 03:36:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4476b0f0-9113-3197-9068-7fadcfed2674 | -6.25703 | -41.97757 | 2026-09-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5b807c7-eba9-3f1d-b387-912f6e4fff34 | -7.13747 | -42.12991 | 2026-09-15 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1449a3af-c224-3e9a-a7d1-b20fd5a817fe | -7.1052 | -41.80987 | 2026-09-15 03:36:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1b1b0dfb-bee6-3b88-b3b5-dae5e00d9597 | -5.60746 | -43.56007 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a37aa12-719a-31ab-b7d4-09145582433c | -8.02941 | -39.00547 | 2026-09-15 03:36:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1723d3a-b783-33a9-b0a4-564cbb170c61 | -7.01545 | -44.62674 | 2026-09-15 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d7f94e3-38ac-394d-97b5-ff44d970cc69 | -5.6092 | -44.84659 | 2026-09-15 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 29e64607-61f2-34e2-93dc-4c7211c9e373 | -5.53208 | -43.37371 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b98c7eb0-0b21-318c-a961-770f88336ce7 | -7.0776 | -42.11671 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8798a19f-8c54-3c11-bd6d-a701797af213 | -4.66963 | -42.07983 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2974da32-4e5b-3c4f-a79a-eff6afab03d1 | -7.16842 | -43.5251 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 98ced278-180f-33b9-bc22-ef11b95d0fa2 | -7.07811 | -42.1138 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a3aee0f-7c0a-3a82-b812-810ad7c605f9 | -7.02056 | -44.63195 | 2026-09-15 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e26c6060-43cf-3a3f-87d8-d3be77d980e6 | -5.61955 | -45.24844 | 2026-09-15 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bff89ea6-b692-3e24-9eb8-b2cba641e5a5 | -5.47175 | -45.118 | 2026-09-15 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2044d60-7553-3734-9ffb-7a3bbe72b28b | -6.83428 | -43.52039 | 2026-09-15 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19997f29-8da6-3e8f-ba75-fa36ef98c99c | -6.61173 | -44.20947 | 2026-09-15 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 634409ef-7cbe-3961-92f0-e7e3f88f62fd | -7.09751 | -41.82524 | 2026-09-15 03:36:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 147910f4-9f88-3972-921c-3cc0d53c9d80 | -7.09011 | -42.13345 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43da31a1-f7d5-3cf4-ba77-61207ee4fdc7 | -6.80266 | -43.1785 | 2026-09-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d1319a4e-24c6-3eb6-a6dc-7bf65541ffb7 | -5.43091 | -43.98887 | 2026-09-15 03:36:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bc4ca49-a3f6-3389-b480-17a3d4bb23d1 | -4.66858 | -42.08603 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| c6ca2f2f-e080-3a41-8571-55162069ac67 | -6.95197 | -42.56912 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 99e34207-36f9-39d2-9b28-75540bfa982e | -5.7356 | -43.28001 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75f59f94-b56a-3387-b892-764afca31707 | -7.1703 | -43.51985 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 55d216a0-5440-381b-a70e-71e5893b31f3 | -6.26122 | -41.95107 | 2026-09-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c98fd725-b6ab-3ea9-80f4-a8b4fd1b85f1 | -7.16751 | -42.10442 | 2026-09-15 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c8272df-10e7-31d3-ad81-f7eb41579a97 | -7.0878 | -41.82336 | 2026-09-15 03:36:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0a849d3e-56ef-3d8c-8216-1d3081b3df6e | -6.86128 | -38.22675 | 2026-09-15 03:36:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1330cb9e-eb5b-3097-b870-977c39e6e944 | -7.10799 | -42.09389 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d6119ca4-c5ca-341e-a32a-cd295878b3ab | -4.24808 | -38.05988 | 2026-09-15 03:36:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| a760f6de-8713-3256-8770-07ae03661c71 | -7.09294 | -43.53784 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 16357812-ab21-3cda-a090-1c2add26e0d2 | -7.09229 | -43.54145 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0bb5c765-1686-3a15-96d6-e91442b9eb7d | -5.73624 | -43.27637 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64dda4b6-35b3-383f-8d31-4764ec1a4165 | -5.55966 | -43.43915 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c3633af2-aac4-3376-ba11-5432e7a2c945 | -7.08609 | -42.12701 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 78d8adbe-3ac9-3986-b8c2-96873c2fb888 | -6.26204 | -41.97834 | 2026-09-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38d387b6-2db3-3f69-b40c-d5adbabcf3f8 | -4.67322 | -42.09005 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 43e47f91-6e83-3ef1-997b-b9da57aea4f6 | -6.40984 | -42.95306 | 2026-09-15 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 565d911a-102c-3189-b99e-24802283486f | -6.26074 | -41.95392 | 2026-09-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a0e5626a-a5b6-3e03-8498-dc5793f6adf3 | -4.67944 | -42.08465 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4cd5d1d0-cf64-3fee-825d-04b619cc4377 | -7.06316 | -34.9595 | 2026-09-15 03:36:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4ef6f77b-48e7-3e59-9c21-ef975d56c986 | -7.08208 | -42.12049 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b4f9dc29-649a-3a4e-9d0a-ca24834fe51f | -7.10201 | -42.09876 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97d1b739-336a-3c45-954e-aeb047873310 | -5.55338 | -43.44213 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 65d06e3b-40ec-3e95-8be5-c4cf5852205d | -6.26147 | -41.95233 | 2026-09-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e9796d3-12c8-3ad1-81b0-c6fe0cb4e0f5 | -6.52499 | -42.24755 | 2026-09-15 03:36:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e7dcbac8-0d20-3db8-8ed9-a5860b080761 | -7.0771 | -42.11963 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cddb9c02-c049-374d-a1fc-d701266a97b9 | -5.55523 | -43.43871 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c0e59a0b-a800-3aa5-a3f2-f1c8fc690ffc | -6.95422 | -44.53763 | 2026-09-15 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 45190751-c613-3d0c-a6f1-399ba2ef457e | -7.08682 | -41.82898 | 2026-09-15 03:36:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0eadb123-d752-37d0-8d86-a75cd5176b62 | -7.16653 | -42.11008 | 2026-09-15 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b57e8b0d-98b0-3990-8587-843e35dfb247 | -7.01466 | -44.63109 | 2026-09-15 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 556fb03c-31fb-3d49-a9ae-2182e21541fb | -5.56082 | -43.43957 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 029a5104-c3ce-3337-923b-ff543f23d90b | -4.95181 | -45.14624 | 2026-09-15 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 657b3f4b-3fd8-3612-8511-71df7c2f955e | -6.95249 | -42.56617 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 01c73f74-5a4a-3828-a37c-88b022c81f4b | -7.23317 | -46.14655 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2602f7b5-69e0-3a04-b7df-b66e4ab0c489 | -7.24771 | -46.17001 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4d0746dc-d6f0-37e1-848e-a901f8935751 | -10.58388 | -47.7369 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a77658a-90b9-31f3-a62c-1ed4d83d5995 | -11.4919 | -45.74744 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 0dbe230b-d009-38eb-8afd-b4d17a218313 | -11.49608 | -45.75142 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 01bc6649-409f-33ec-8995-16e6e0171d77 | -14.76556 | -42.94448 | 2026-09-15 03:38:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d6837b4c-23bc-3ed5-92e5-3078b0ad0d8b | -7.24196 | -46.17034 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 16ce5c38-4fd9-39e2-87d1-f2058fe8a3e1 | -13.55951 | -43.53382 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01cb83bd-170f-3b9d-bf52-b0b7ec8db754 | -13.57008 | -47.90144 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README19.md)
