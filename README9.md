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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5551323f-e850-3b0f-86a1-604469b59521 | -5.37935 | -40.71309 | 2025-10-25 03:28:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 276b1300-97ee-3d3c-aa61-c9636c389dd8 | -6.09108 | -39.19333 | 2025-10-25 03:28:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dbe99779-033e-3cff-a858-664358c8029f | -5.82181 | -40.80939 | 2025-10-25 03:28:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa6a6a76-6831-3bf8-854c-b617e23d3c1d | -6.13001 | -41.7195 | 2025-10-25 03:28:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fc671003-7be0-3182-9908-42650f527392 | -3.99888 | -41.0196 | 2025-10-25 03:28:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c24cba3-f352-336d-85a0-fabca8f08b9c | -5.37991 | -40.70984 | 2025-10-25 03:28:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4b3e8311-2a0e-3f73-9e96-64e1e1dd85c9 | -4.79625 | -42.76594 | 2025-10-25 03:28:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f202a62-52b6-3fb8-a7fe-f3a9dd8ab240 | -6.31968 | -41.86509 | 2025-10-25 03:28:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9744e875-57de-3212-a22a-101fa15bfd65 | -5.37463 | -40.70899 | 2025-10-25 03:28:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2585cec8-2f2d-3c44-8e89-47c0023ab261 | -5.33268 | -44.72219 | 2025-10-25 03:28:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdd654f4-29f6-3505-ae05-d370432b0024 | -5.37407 | -40.71225 | 2025-10-25 03:28:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 991f8778-0ef0-3dfb-9e65-df27e7c9679e | -3.72338 | -44.28391 | 2025-10-25 03:28:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ca0f7f8-d676-3fa1-b11f-b5d0da795a5b | -5.59626 | -45.19198 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9cafabae-c726-36de-9804-ac4a7703ac6f | -5.25774 | -44.13463 | 2025-10-25 03:28:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 92f54ea0-d406-37c5-96b9-b6f5bf6d2301 | -5.28947 | -38.2916 | 2025-10-25 03:28:00 | NOAA-21 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c6b3478-df65-3569-a8f3-18170ccb5ef8 | -5.45939 | -45.405 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0ef82cd-8c74-3a23-a7d4-bfdf519daacf | -6.31679 | -41.84906 | 2025-10-25 03:28:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b65b2c63-c262-3b84-81ca-da40da84c9f2 | -6.12867 | -41.72694 | 2025-10-25 03:28:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b01c7b94-759e-353a-88dd-42daaa41bfc3 | -6.02868 | -39.62159 | 2025-10-25 03:28:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 40694904-0f60-3a6f-bef6-4a57762f4525 | -4.80233 | -42.76694 | 2025-10-25 03:28:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 04ebbb40-894c-3916-971d-66f926974c2b | -5.45723 | -45.40451 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e1147ed-4af9-3766-abf1-a5c666bb955d | -5.33377 | -44.71611 | 2025-10-25 03:28:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 867d6049-c5cc-3076-8d3c-7ff37b63d748 | -6.03194 | -39.62445 | 2025-10-25 03:28:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2fb2be43-190b-3b15-83da-1de8726163e1 | -4.27422 | -40.7037 | 2025-10-25 03:28:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8fb21980-83b3-332c-a0b5-572aa5d15011 | -5.2553 | -44.14165 | 2025-10-25 03:28:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ee5158b4-9a6b-3ff6-b63c-87c3f4e796a3 | -5.80308 | -35.584 | 2025-10-25 03:28:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1c61392a-0a4d-3727-99ff-a00ce2b3fd43 | -5.82133 | -40.81225 | 2025-10-25 03:28:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15ba2e4c-8df0-3fc7-8ff0-af51a1054acf | -5.4489 | -45.41018 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71e7921a-16d7-39d2-a252-3eb4a19a0acc | -6.30188 | -40.87593 | 2025-10-25 03:28:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2829989b-e910-3144-a6e2-a53d65f2603e | -6.28733 | -40.86649 | 2025-10-25 03:28:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6dfccd82-78c4-35ee-b0c5-22f5fc45d5ff | -3.70217 | -40.42117 | 2025-10-25 03:28:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6bfc4e67-5e39-39e2-8330-eb7d4df99987 | -5.88794 | -43.20137 | 2025-10-25 03:28:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 81a1e41e-4c5a-3500-bc59-8123701f4747 | -5.59663 | -45.19456 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 81a1e553-3777-3ddb-a09c-2f368b2a4b95 | -4.27465 | -40.70116 | 2025-10-25 03:28:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ef73ad71-1821-3cac-a364-8ceac547066f | -5.25114 | -44.13371 | 2025-10-25 03:28:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7ef5d32-db36-3c1d-9a77-ef0d648ab849 | -5.33522 | -44.71989 | 2025-10-25 03:28:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4c0a7967-22c2-32f8-9b14-d3fe0540183b | -6.07047 | -42.15011 | 2025-10-25 03:28:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5795e2a7-b43a-38b6-bc73-28589a43fb5c | -4.18342 | -42.98363 | 2025-10-25 03:28:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5574bd98-2216-3904-9594-57ecff857c62 | -4.45446 | -38.44352 | 2025-10-25 03:28:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8e8a01e8-150c-3094-8d76-646c500122da | -4.25313 | -38.6985 | 2025-10-25 03:28:00 | NOAA-21 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 025df966-7dd7-3592-ab81-415f12d20017 | -5.25636 | -44.13587 | 2025-10-25 03:28:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 67c14f91-ce9b-38cf-a335-dc55fc0b13b3 | -5.61052 | -41.1222 | 2025-10-25 03:28:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43e1767d-f877-34ab-98f3-39160dadf4cf | -6.01876 | -38.43271 | 2025-10-25 03:28:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 34a16448-2074-3ce5-81c3-c18e0ff98e1a | -5.25013 | -44.13942 | 2025-10-25 03:28:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 824b1074-d2f0-3a51-ada2-05f0e41e8b6d | -5.43676 | -43.00434 | 2025-10-25 03:28:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 933f12d7-81ee-3f47-8843-f94d94485fad | -5.80664 | -35.53876 | 2025-10-25 03:28:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 628e8f08-cf69-3905-860d-e47f7cadd4c1 | -5.45589 | -45.41171 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe2c6d73-c5a0-317c-94f4-4871e9a388c4 | -5.84005 | -40.79773 | 2025-10-25 03:28:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3134c08-809f-3f4c-8785-60027309e0a2 | -4.18533 | -42.9819 | 2025-10-25 03:28:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 539031b1-058d-3ade-a62b-3572eab142c4 | -14.8701 | -48.1047 | 2025-10-25 03:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4978d9e9-2f0e-355a-b042-f811d31d7c25 | -2.8149 | -49.1354 | 2025-10-25 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f9585300-ec55-32b9-859f-194d2e284935 | -2.7964 | -49.136 | 2025-10-25 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| ca878334-c47d-3508-b6fa-40dfafe31099 | -14.8706 | -48.0822 | 2025-10-25 03:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| fb9aea83-792e-3173-8fbf-21ec28bd4f63 | -18.1714 | -51.7466 | 2025-10-25 03:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| be913b8f-1038-3e33-bb00-b56f882dae88 | -22.8323 | -51.349 | 2025-10-25 03:30:00 | GOES-19 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 1bf7ca38-c2e5-35d8-8457-8fdf5d544c10 | -10.9605 | -44.8995 | 2025-10-25 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ddbb18e4-150c-32b1-95b8-8fc9a2f5f33f | -6.59416 | -42.07304 | 2025-10-25 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34c2f410-deb1-347d-8899-cb07ad18bc78 | -10.63617 | -45.23955 | 2025-10-25 03:30:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29121190-167a-3661-9a35-6b9bd295ee04 | -6.59511 | -44.32381 | 2025-10-25 03:30:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e46342ef-587f-3323-ab2d-d07c50ff1c43 | -7.82402 | -40.25329 | 2025-10-25 03:30:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 602437d4-159f-3754-afff-6c4f13fb006b | -6.96647 | -43.49542 | 2025-10-25 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e2ee4fa-1530-372b-a81d-af7a5acadd5c | -10.42506 | -44.49745 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1c24280-94d6-3dba-9165-d96b53f285cf | -6.91874 | -45.17079 | 2025-10-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 183ba9d3-9b3b-325a-bdaa-e5030dc418ec | -11.43071 | -44.67355 | 2025-10-25 03:30:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e8a8ae4-c359-3c0c-850a-1d2b9fe742f7 | -7.58325 | -43.58087 | 2025-10-25 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfbcaf3a-5729-39bb-8861-5849a7dd9f4e | -11.1422 | -44.93956 | 2025-10-25 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 901657a3-bd82-37e9-9cea-c9d9cff9fcc9 | -7.58933 | -43.58216 | 2025-10-25 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37dbc938-3976-31cd-b02e-952075f586f1 | -7.15457 | -44.12413 | 2025-10-25 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fec00dad-2ac6-3125-a61d-e41b9efdb90c | -6.59343 | -42.07709 | 2025-10-25 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac7a0c03-b689-3b03-895d-ef7a243fbefd | -10.56423 | -44.93633 | 2025-10-25 03:30:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fec1677-9573-343e-a848-41689fec70ec | -10.45095 | -44.96327 | 2025-10-25 03:30:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 96d950de-b7b5-30a0-908b-085caa2570d6 | -12.19387 | -43.58136 | 2025-10-25 03:30:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68584d10-5c58-34d0-8164-29133b5ca780 | -6.44889 | -44.28132 | 2025-10-25 03:30:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 19d49d24-57bb-3c72-8481-725fa6ea2307 | -6.92012 | -45.16348 | 2025-10-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bd35fe5a-06d0-340a-8394-b76c7bbead6d | -6.94022 | -43.64092 | 2025-10-25 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb7b44bc-fa67-34a6-9198-6b540d65d4cd | -6.93925 | -43.63818 | 2025-10-25 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a05db4e6-b89f-3343-863b-f192a709b6d9 | -8.67628 | -36.68741 | 2025-10-25 03:30:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a610d6b-57e2-38c4-997d-943126dd02a7 | -10.42354 | -44.49992 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 689b95b8-aae2-313a-9b32-ba7c79cecba0 | -6.59698 | -42.0736 | 2025-10-25 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6651537f-33b5-37e2-b195-bc66779dbb6f | -7.5433 | -42.51702 | 2025-10-25 03:30:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 190165c9-fcdd-38ac-b693-eb15c81de854 | -12.22369 | -43.31154 | 2025-10-25 03:30:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d23325fc-b742-310d-b2ef-ff838985e9f9 | -6.54353 | -41.69445 | 2025-10-25 03:30:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65a85d14-df84-3eb0-ae65-d9b776ea9a16 | -10.40983 | -44.74292 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9afe95f6-3ece-39dd-a81c-9c52e82f2a22 | -7.45994 | -41.90847 | 2025-10-25 03:30:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e19014f1-9833-32a3-9977-11d6e5d24405 | -10.41397 | -44.74069 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0c58518-ead1-3874-83a5-405b44727428 | -7.58496 | -43.57152 | 2025-10-25 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 893d5436-9f30-3cd8-9e06-678ec164f8cb | -6.54457 | -41.68863 | 2025-10-25 03:30:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7898401d-6003-3bb9-afb6-864771592370 | -10.40885 | -44.74799 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5362a180-a6c2-3749-89f3-e88b179db580 | -6.96559 | -43.5003 | 2025-10-25 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53ba05cf-0a57-3fbf-897e-f082b9ee7e6d | -12.0649 | -43.99063 | 2025-10-25 03:30:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6cd0840-1fe8-345b-b3a5-0089fe3e0a3e | -10.40665 | -44.74478 | 2025-10-25 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aaeab1c5-58da-3276-88e3-204d8c250eec | -7.84939 | -40.89904 | 2025-10-25 03:30:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ddd32353-4c9b-3930-b30f-71433a0d6e8b | -12.22443 | -43.30777 | 2025-10-25 03:30:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 556ce294-d75a-3fc1-89ed-4acbb5f2fd77 | -6.96466 | -43.50288 | 2025-10-25 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12a44377-df7f-39dc-9905-d6946bd95800 | -7.58239 | -43.58556 | 2025-10-25 03:30:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95c4222c-a5ff-30fc-8f00-960d91b2c2bc | -6.81783 | -45.44181 | 2025-10-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48245f2c-2e9b-39b3-aedf-f4ae6b95975a | -7.63943 | -42.16813 | 2025-10-25 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1dd7c451-e30a-36a8-a48f-bc2a8e35e7e5 | -6.80445 | -42.39621 | 2025-10-25 03:30:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 2763809c-1b4e-3620-add5-b0a63636e7b9 | -8.60932 | -44.81488 | 2025-10-25 03:30:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a35c995-e092-3afc-adac-00a88f155f11 | -9.32121 | -45.1918 | 2025-10-25 03:30:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README10.md)
