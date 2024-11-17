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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e1c2975-a5df-3e9d-a522-a3b56de19b92 | -1.40641 | -52.42435 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0466804a-7267-3e10-b0c7-b27b05505011 | -2.27941 | -48.41459 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 15e2093b-29a8-3bf4-b057-eae53853d4bc | -2.60902 | -46.25386 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 369fff77-21ce-348d-8bd1-38f0a61a73c6 | -0.11385 | -51.61471 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e2a3ef5-3f98-3da1-812b-071e993a9a59 | -4.68357 | -49.63418 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f5f38635-1924-332e-9369-26a217c3fe5a | -5.3149 | -45.44757 | 2024-11-17 01:04:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f613d3e3-b4e9-3e80-bc71-081b789ca9df | -3.86858 | -51.17868 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf81b829-8888-3286-85ea-197f7adacb57 | -4.80101 | -50.80567 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3579aeb-ccdb-3c8a-aec8-dd355c30d033 | -4.41312 | -45.5322 | 2024-11-17 01:04:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4b1c625c-b9c9-312c-8ae3-1afeda4bf105 | -1.21528 | -53.56073 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 17e1bf91-d10e-34d3-aae8-31bdf55bc71b | -4.23025 | -48.03198 | 2024-11-17 01:04:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d3fd72e7-45c2-30b8-8a03-c2d0b3110b72 | -2.59708 | -47.54652 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 441bde27-fcaf-3297-97ad-106119e7453d | -2.41809 | -48.97463 | 2024-11-17 01:04:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6baaf1b0-ff47-3ae5-b834-80b89decc63c | -2.21029 | -49.28631 | 2024-11-17 01:04:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8fe84f81-1979-333a-a7cc-78e6a2a390ec | -4.58658 | -48.02994 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 5e05e19d-92b4-364d-bd7e-eba37afa23c2 | -3.58551 | -49.88382 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6dad0f4e-87b0-39fc-ad7b-59f71e3a9a99 | -4.24233 | -41.92652 | 2024-11-17 01:04:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 754110ff-e2fc-3f92-a20a-2d19db345651 | -2.1655 | -48.33407 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 90b31a36-ef54-3545-8e77-90c91da96895 | -2.84865 | -44.95031 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 0c992cdc-5d5f-382c-8535-05fa802aea13 | -3.33188 | -52.76283 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 49afce47-6b5c-33e3-a905-1f657126974d | -3.39582 | -53.02554 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a70aaf37-cdc7-3567-8353-65960655f44b | -3.32451 | -52.76989 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ab0ab752-b0ef-39e8-a1cc-3b3b9077ab58 | -4.57521 | -48.02052 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4b1d61be-d1df-3b13-9ac3-0836c71e6598 | -1.58147 | -50.44076 | 2024-11-17 01:04:00 | TERRA_M-M | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 03fd9026-aa95-31d1-985d-ac3e9114cf4d | -3.38502 | -53.2711 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 921fad7b-ec57-3917-801d-d2a55c46733a | -3.93953 | -49.00358 | 2024-11-17 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 99a17aa6-c01d-3d25-8029-67b6e156d188 | -3.53611 | -50.25095 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6fab77d5-f6df-36d0-9eb0-ba1e9a3fa6e7 | -2.67636 | -46.86523 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 26f04a23-485b-31a3-b026-f48a5618a95d | -1.22407 | -53.36766 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07808132-9e28-38f2-a7d6-7d6f63ab5c99 | -1.51683 | -55.12096 | 2024-11-17 01:04:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 17304217-88d9-3238-99f1-8b38771d3b55 | -3.77405 | -46.04895 | 2024-11-17 01:04:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 3e7459cf-f9c9-313c-ad50-9fb9402df6cc | -2.18565 | -48.26141 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fc3cb339-a2e4-30f6-90ba-ee3e9828463f | -4.21256 | -48.70935 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 18f5076a-2b07-3fee-96a2-c0423518b836 | -2.67329 | -46.85696 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9a31036f-7c6e-3bc8-be81-72eb86350faf | -1.80302 | -48.44516 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f5bf0e67-2b77-39d6-b816-2ce1cb23c89b | -3.85153 | -51.39365 | 2024-11-17 01:04:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 157aa6f7-0ba8-39a0-8182-fb05fdcb6be9 | -3.48539 | -53.99171 | 2024-11-17 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 10182a19-b2c9-3f4c-b87b-8752847d40c6 | -3.7863 | -50.39568 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 599bc102-cb99-3d5f-b4d0-3844e492f565 | -3.58299 | -50.51884 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 8e188710-b125-3306-a405-927969e68cde | -1.96879 | -48.39199 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| cb776db7-52a2-3698-8d8d-af5eb3cdb0bc | -1.50758 | -47.4546 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4c651406-ed76-3656-ad03-83311240c4b8 | -1.29261 | -51.73681 | 2024-11-17 01:04:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 93d88564-c6e7-3310-a1ec-3e193ce39bb5 | -3.02122 | -45.40053 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4ead9cc6-1714-3d76-bb1b-421043b9a584 | -1.37162 | -51.11144 | 2024-11-17 01:04:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a8c4c2a4-40d3-3638-b21a-c0a0a662a923 | -4.04129 | -44.77197 | 2024-11-17 01:04:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| bb7071ef-9a2b-35f9-b917-1e0b42eae920 | -1.62802 | -53.28696 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 386f18e9-ebd7-334a-8d18-cffa00f03782 | -3.88647 | -52.30843 | 2024-11-17 01:04:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3c3be9d7-d9a9-3bb6-8a91-6f266d15893a | -1.37802 | -51.09246 | 2024-11-17 01:04:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28267d9c-b9a0-3f18-8df2-55dbab89f3c3 | -4.57677 | -48.03146 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 99e1302f-6d98-35f4-8213-183d29a81d0d | -4.65099 | -44.98994 | 2024-11-17 01:04:00 | TERRA_M-M | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c1a97c03-08d0-356c-8412-4fdf19feca70 | -2.17624 | -49.1159 | 2024-11-17 01:04:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a7bcc0c4-a6a7-3d48-92a3-a154444a5f2e | -3.38364 | -53.26119 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b94db704-9b13-3a80-bab4-10023b95397b | -3.1792 | -53.25171 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7389e775-cc1d-368e-bbf2-d94a30eb82da | -2.69975 | -49.28759 | 2024-11-17 01:04:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3ce425c7-7179-331b-8e98-7cfdb8507745 | -3.66658 | -50.19833 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 22eaea44-bcd3-3706-aa62-b4ec41ec8e99 | -3.56423 | -50.25616 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c41b8844-317b-3a04-88ac-3ad6182861c2 | -0.78236 | -49.47439 | 2024-11-17 01:04:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f44f7549-6d8d-3207-adb8-a8d176e239ab | -4.47731 | -44.97191 | 2024-11-17 01:04:00 | TERRA_M-M | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6765cb88-f898-39ae-afbd-9a05fe9f7eab | -3.36238 | -51.44846 | 2024-11-17 01:04:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6e01e61-3dd5-31f2-8f42-90df2ffaae46 | -0.65144 | -51.69972 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c3e1d18-be61-3bf7-887e-cb4abc8088d5 | -1.38597 | -52.08293 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| daf6d5fb-ef49-39a6-8061-6bdd03c49c7d | -2.58839 | -47.56067 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 6cf277b8-ead1-397d-b2d3-6e7ad31673a0 | -0.9446 | -52.4202 | 2024-11-17 01:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 99f1bf18-160e-3802-a9a3-898cb2160ad0 | -3.5203 | -50.254799 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7444e3e7-b73a-3a8a-a3ed-f77c70b74ede | -3.5696 | -50.502701 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74c0103c-c222-3923-808d-5e4c35a1d967 | -3.5051 | -50.2342 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f67db10c-2c7c-334a-a7a0-285a7e200563 | -0.1079 | -51.622299 | 2024-11-17 01:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 844d37a4-7fab-345d-aa12-fda4617818a8 | -3.1717 | -53.2314 | 2024-11-17 01:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1259f3f3-844b-34c8-84b2-7ec782d946a6 | -12.565 | -57.821999 | 2024-11-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bfaadf0-9dc2-3219-92f6-055ff5c6d089 | -2.6199 | -54.166901 | 2024-11-17 01:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4187c595-2bc1-3ad7-a1bc-75cb30298615 | -0.9405 | -52.4025 | 2024-11-17 01:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b6657318-de72-32de-8197-6f06f9d7e0f9 | -28.9617 | -49.4062 | 2024-11-17 01:09:00 | METOP-B | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae1b21f1-c5e7-306b-8d9a-a4b994d2186a | -28.959101 | -49.395699 | 2024-11-17 01:09:00 | METOP-B | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b1badf8-11f3-31ba-b9a3-21d597fb8125 | -3.5748 | -50.524502 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f67a05c8-78cd-3074-a5ac-083b1bbfb7a7 | -1.7827 | -48.435299 | 2024-11-17 01:09:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e970d417-692c-3017-8e0b-1985e69a2fc5 | -3.5258 | -50.2775 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b95ac1c-be2e-3ef1-9439-2d6853a2f466 | -22.4055 | -54.564602 | 2024-11-17 01:09:00 | METOP-B | FÁTIMA DO SUL | MATO GROSSO DO SUL | Brasil | 5003801 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d45d3ffe-f444-3a93-9651-7a012383ef46 | -2.3253 | -53.561501 | 2024-11-17 01:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41706b15-d1ed-3232-ad94-028b77c39b9a | -3.2373 | -53.5117 | 2024-11-17 01:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc12051-450d-3721-8584-5fec4c6139e6 | -3.3219 | -50.492001 | 2024-11-17 01:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a63cc3bd-deed-323e-b314-be5c22686588 | -23.937599 | -54.076302 | 2024-11-17 01:09:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d9c64525-2c8b-3668-a470-b4128352266e | -2.3285 | -53.5755 | 2024-11-17 01:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 422ab2ec-4c00-38fb-907b-92dc06243e1f | -19.496401 | -56.6105 | 2024-11-17 01:09:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87ad6a4d-f5d3-37e9-8081-a1b3fcba9508 | 0.6233 | -51.7654 | 2024-11-17 01:09:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8abc1ed3-f880-3405-9eb0-0880fffab32c | -3.5245 | -50.229599 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a556a6c-81c2-3ad6-94f8-47978f9212a3 | -3.0226 | -54.087502 | 2024-11-17 01:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed8c714c-815a-34a8-b90d-0414e00290c6 | -1.6239 | -53.278301 | 2024-11-17 01:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25df422a-2f4b-3bea-9b0b-1a62e6d68ec2 | -12.393 | -57.514801 | 2024-11-17 01:09:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a0bd730-02d6-3681-8999-02406d45a576 | -3.1848 | -53.243401 | 2024-11-17 01:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27b358c0-eea9-354a-9fb4-181b3bf31850 | 0.6186 | -51.786201 | 2024-11-17 01:09:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba5eb7e-78c5-3284-95ad-b6eb379b43a4 | -3.5493 | -50.247799 | 2024-11-17 01:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5a7ca43-c628-3403-9f0e-c10f488d409a | 0.633 | -51.767601 | 2024-11-17 01:09:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e71269f3-f7c0-39bc-af3d-ea795f6d0052 | -12.5537 | -57.817299 | 2024-11-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94954c89-3379-3840-ba6c-52e1899aa497 | -2.614 | -54.141499 | 2024-11-17 01:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9701d5-4c1b-30a8-b93a-e66ec46c63d3 | -0.9387 | -51.731701 | 2024-11-17 01:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| da5cb4ff-9f33-37cf-b88a-38656dcb1c0e | -2.98 | -52.589199 | 2024-11-17 01:09:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0defb3df-2dc7-3e54-a41f-5feaea117eb0 | -17.8237 | -54.5392 | 2024-11-17 01:09:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c979a561-1a94-3c60-b322-4c69792ed841 | -3.3208 | -52.7742 | 2024-11-17 01:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47fc91af-42d2-3940-9650-3d47a7bdd45b | -3.0255 | -54.100101 | 2024-11-17 01:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1785f3e8-c837-3f28-b496-46ab9409c063 | -23.9394 | -54.084 | 2024-11-17 01:09:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README16.md)
