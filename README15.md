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
| 0d522bb2-7b7f-3294-b809-2d8c6c7c46d2 | -4.6707 | -45.99081 | 2026-09-27 04:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee9216b8-86dd-3123-bae1-e9e0fc136ebd | -5.60913 | -44.1749 | 2026-09-27 04:08:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3a6cfa7-10cd-3ded-a93e-c75cb02b6bd6 | -8.35615 | -44.18031 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| c71431c1-d14d-3622-b7ba-c55a638c5c95 | -6.84006 | -43.51758 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 583e6ec0-bf03-36b0-a6d4-fbed527fa8ee | -9.78698 | -44.83261 | 2026-09-27 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e37904c9-29c4-336a-802b-ad030a7794db | -4.78607 | -43.65816 | 2026-09-27 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7124598a-3ff5-381c-b4b6-021bb879460e | -5.43174 | -43.44215 | 2026-09-27 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7c835b23-2569-3e24-b189-ced86880e9ef | -6.84077 | -43.51334 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dbc8d57-cbd4-37bd-be3c-16e29a1f44fa | -6.93037 | -42.86561 | 2026-09-27 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ad036553-5ef9-3bd3-a486-ad5f4f07c22f | -3.84322 | -45.1386 | 2026-09-27 04:08:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b19abc46-f8f3-361c-b9b0-f93154b49333 | -4.2579 | -51.05265 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bffcb6eb-9704-3145-9ab8-25b11a96d52c | -3.18957 | -51.04051 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ace6ea00-118b-3cb8-826b-7a063f781f52 | -3.19343 | -51.03467 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f6f7969-3575-3487-ac55-80a8206c8607 | -6.18068 | -44.27857 | 2026-09-27 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d317cf81-7ac1-3dd9-bab7-9a5a8177aba0 | -8.36354 | -44.15905 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e97fec86-fa8a-3ab7-9118-92e4dbd31327 | -7.18881 | -46.50957 | 2026-09-27 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e92cb33-fc4f-3540-be2b-b38af48ce42c | -7.30613 | -46.03704 | 2026-09-27 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01520215-5fb6-39c0-9629-5960db589931 | -6.9433 | -41.61069 | 2026-09-27 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2b6f397-acbd-343d-9c8a-2f3b965f9df2 | -5.43101 | -43.44649 | 2026-09-27 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9e3db3dc-ab48-31d2-8ddf-deb46ac574da | -7.33913 | -42.08828 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f728af9-f4ee-35a4-aa57-b2075e7766ec | -8.34379 | -44.17075 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb0fc585-5c78-39fa-b4da-00d137e5e883 | -3.96371 | -50.71555 | 2026-09-27 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 918c4fb8-6a61-3d0a-9ed0-397b73be370f | -5.75528 | -45.29435 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cf177af-970f-3b31-91c3-8371e097542d | -8.33779 | -44.13812 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6318075-1421-3403-a58a-35361bdf261e | -7.33573 | -42.08773 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 599929e1-5854-32da-bff5-d0b6ac5e50cb | -8.35543 | -44.16217 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 8d3b253c-4aa1-3d3d-a5f1-4e33076e018d | -5.7347 | -45.01637 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c5b03fad-f7e2-3c77-ae8a-1565e30d9e74 | -3.10492 | -50.32726 | 2026-09-27 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1b82f14-5610-3089-ad3c-e809e12af14b | -6.13161 | -53.06158 | 2026-09-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85b7d5c1-ca39-3935-ae01-6c06ee853bf8 | -8.34069 | -44.15972 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4595fd2f-f0dd-3258-b525-eacd0146d1a5 | -7.34772 | -42.07834 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4476547c-50cf-33d3-91d2-51a50921763a | -6.77505 | -48.66584 | 2026-09-27 04:08:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f749da0f-30bc-312a-8c42-1785a9492d69 | -3.96041 | -48.12074 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c272a066-0fe5-31ab-9a49-6f22519fbb2f | -5.94208 | -42.72478 | 2026-09-27 04:08:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f57b0307-16ec-3483-b5bf-c27d1b715534 | -6.93877 | -41.6173 | 2026-09-27 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5806128a-ed8a-38db-bb60-3d7d91445515 | -3.01021 | -51.53546 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c494838f-1629-35f9-b53b-dd62519c5d7f | -8.34596 | -44.15753 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7ffa0ac-daf7-31f3-b0be-2534cd5d643c | -7.36101 | -42.12587 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 666d9287-c0da-32c1-898b-9cb85ee821b5 | -4.25233 | -51.0547 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1da60be4-9d0e-3b64-bff9-8faf714a4c90 | -8.35618 | -44.1578 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b659e1d9-a8a8-3add-83c4-9218cf708cc4 | -9.93811 | -49.37029 | 2026-09-27 04:08:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00025868-3dd6-3be6-b09f-62e8e1013c94 | -3.87339 | -52.28634 | 2026-09-27 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eebe94d3-094e-31a7-aacb-71588f5a2b5e | -6.15404 | -47.2824 | 2026-09-27 04:08:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ddeab12b-f1ae-3fa4-96fc-a4d853b098b2 | -4.28534 | -48.55937 | 2026-09-27 04:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e40c2e0-649d-39d2-aee9-5f523829678e | -8.35108 | -44.14939 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a5837ca-b52d-3534-8302-952edfc59389 | -4.73769 | -43.47658 | 2026-09-27 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 311e9634-fc83-38a2-a907-9458c52aa66e | -6.31447 | -43.34243 | 2026-09-27 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| faae025f-ba44-37dc-8534-14c645d25d08 | -3.50636 | -50.48511 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b27c98c-fa10-3853-81f9-d1441ac39015 | -5.74249 | -45.06875 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0799c002-0842-32cc-a72a-b143b4a5967d | -8.34212 | -44.17353 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40de7cbc-1d70-35e2-9166-23891fc8610f | -3.42103 | -50.43114 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2eb2d82-a87d-328a-8dd8-5c7ef34fe9e6 | -8.35469 | -44.16655 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 158.0 |
| b5da1861-7fdf-363c-a56a-26f03dffb195 | -3.96555 | -48.1215 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f58bd03-c7ef-3d77-bc23-c12a72e27993 | -8.35912 | -44.1628 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 816c376a-d704-3fdc-858e-b67b33ff5e22 | -7.1229 | -43.66524 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 45c80c89-a051-381f-b206-36006d1c28cc | -3.10568 | -50.32287 | 2026-09-27 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a9be45f-f69e-3895-b122-2d94ccba6f18 | -5.18379 | -41.14329 | 2026-09-27 04:08:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 62b55a6e-5300-345d-ac66-b365f065084d | -6.83714 | -43.51276 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc516c73-c765-3a57-aa78-5f958377ea6d | -8.34507 | -44.1785 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0dcf789f-e794-30b7-882d-63f8b3261fb5 | -12.22913 | -39.29881 | 2026-09-27 04:08:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb149052-cc1f-3b4c-9c32-fb17ec6743e7 | -8.35838 | -44.16717 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 158.0 |
| d6bd2400-6c5b-34a9-86cd-97de5047d358 | -4.25876 | -51.0478 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff119a72-06fd-3663-b131-d34ed1e37d4a | -8.24978 | -43.78695 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c306dbf2-bb7e-3e4e-bc66-2f62a2bfc411 | -7.33633 | -42.08404 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 40b1fa82-11f3-32ce-84dc-539e9686abd2 | -6.84147 | -43.50913 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58e72eaa-463e-3f8c-bead-682fa750910e | -6.78012 | -48.66675 | 2026-09-27 04:08:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0f69eaf-1ecb-3c61-a5dd-2e81bd6948f8 | -3.43116 | -50.3365 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a39ca1c7-fca1-3794-9bf3-665163a695e9 | -8.3481 | -44.13844 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbcbcc0e-032b-31d3-acfe-9bacb659e22c | -10.22478 | -36.3316 | 2026-09-27 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d0d9e493-62f2-363b-9192-2650b148df29 | -5.75588 | -45.29068 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b7e9528-7e4c-35cd-a278-853ecd318d9e | -5.50683 | -38.00701 | 2026-09-27 04:08:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb278ba4-7368-3b37-a24c-2ee09e17c42b | -2.88635 | -49.48378 | 2026-09-27 04:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac2dcd34-7b67-3242-bd4c-80f7f5650cbd | -8.05803 | -39.1239 | 2026-09-27 04:08:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46763b96-640b-3741-960c-723f74144e56 | -8.34955 | -44.15217 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 22468583-5d16-3bbf-80e4-18418467bcd6 | -2.89138 | -49.48864 | 2026-09-27 04:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91b496d3-fec9-3b36-839a-3cc15678c6c6 | -9.83696 | -44.94833 | 2026-09-27 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d79fb98-45ea-39a6-83d0-6de3aae2d5b8 | -3.67639 | -50.84879 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b773be64-2459-3c16-8c35-f82257db7869 | -7.32892 | -42.08664 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f5a0774-461a-3094-bed5-2dc5ea5dfda1 | -7.33973 | -42.08459 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f3dcedd7-d09e-3a03-b9a8-b2640d9f9860 | -6.80931 | -46.24788 | 2026-09-27 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e3a5da8-6a6b-3afa-b6f7-9aad0855028c | -8.37387 | -44.14282 | 2026-09-27 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27bb2e13-ce92-35cc-a6c6-3d4cf36a32be | -8.34806 | -44.16093 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96c31b56-9060-3af5-897a-20122b19127c | -5.50741 | -38.00331 | 2026-09-27 04:08:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d24dd92-f2bc-3396-b962-fda1d009d5fa | -5.89303 | -46.58105 | 2026-09-27 04:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 822ea7d3-4a7d-3d98-afa1-2796967ddb3f | -8.33713 | -44.16516 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 969b2b18-7abd-3bf9-8939-cef1c66956e3 | -5.72431 | -46.46118 | 2026-09-27 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ba1584b-bb44-3f98-9198-08e047963ffa | -3.76301 | -51.81121 | 2026-09-27 04:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e66d356-884a-33db-98b5-b45d1ebccbe7 | -6.39955 | -42.78725 | 2026-09-27 04:08:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b824b55-0eb9-3832-abe2-2077b7d01724 | -9.08164 | -49.87334 | 2026-09-27 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f54f3ba-7667-3d66-be7d-561fbad620fb | -4.25313 | -51.04996 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f026d5a2-98af-365a-9682-17f96cfb0b11 | -7.20141 | -40.12409 | 2026-09-27 04:08:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a511117-3485-344b-8d37-4ff3b29754fd | -8.34517 | -44.13345 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 481c2679-10dd-3dd4-adfc-6b32417b2034 | -10.01648 | -52.097 | 2026-09-27 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f32666cb-5b1a-3898-9c09-32bf7a0ab72d | -6.93541 | -41.61674 | 2026-09-27 04:08:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7a191b33-b4e5-30ab-925f-b5a420ad6e00 | -8.35398 | -44.14843 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c68c5c5c-028f-3cb3-91ed-56189fb943ad | -10.45875 | -48.3208 | 2026-09-27 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e23d27d3-57c6-3dc4-b030-ab4ea0102e5b | -8.35171 | -44.18409 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 550c38d5-e25d-3606-b689-d803084cabb0 | -8.34951 | -44.1747 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 2cf4341f-8b3c-3112-a810-45471953d1cc | -8.34748 | -44.17135 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c6cbe7c-a939-3463-bdf7-002f5413dbe2 | -3.19583 | -51.04163 | 2026-09-27 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README16.md)
