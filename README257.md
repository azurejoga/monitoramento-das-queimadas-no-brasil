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

## Dados Diários - Página 257

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6673e37b-c399-39bf-92c8-5349911ef004 | -3.2956 | -49.1415 | 2026-10-07 19:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9a2d399d-8054-360a-8f32-385426d20170 | -3.1697 | -58.6244 | 2026-10-07 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 5174dc59-3841-3bcd-86f7-4fdedc055ea6 | -7.3935 | -46.2144 | 2026-10-07 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1de75408-cbbf-397b-be71-b04b6b9d60ef | -11.6946 | -43.6787 | 2026-10-07 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 2b795948-756a-35dd-b2ed-bb60878f0c44 | -6.1484 | -51.927 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c1d7e55b-0aed-3d36-8d35-d240cdbef2b0 | -11.6181 | -43.6669 | 2026-10-07 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e8304759-9c3c-392b-a000-6bf03df66f3f | -5.8966 | -53.4975 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 2b0bb732-1167-3ca8-9340-918b5b09b7b1 | -4.067 | -54.0378 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 932f8aad-a8df-3d76-81b1-c1cfe44f111c | -3.2949 | -53.8798 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| da154755-8ef3-31de-b2e7-e27ea419a6d2 | -3.2268 | -57.8696 | 2026-10-07 19:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| fde53950-0f91-3855-bb38-e00ad674eff1 | 1.7121 | -55.6261 | 2026-10-07 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 481f98cb-3a36-32c6-b060-e9207d21d0b4 | -12.1922 | -44.7953 | 2026-10-07 19:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 1f06e5a8-019e-354f-92fa-b98d87761436 | -3.203 | -53.8823 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 799a2b74-3e11-3320-80f5-326adf44782d | -3.1973 | -50.5382 | 2026-10-07 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| eaea8dfd-3c6a-382c-8d17-c459b6df27f4 | -5.2094 | -48.326 | 2026-10-07 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 477003ef-2324-3f4a-9db5-dffae49378e8 | -3.4763 | -50.0673 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 87eaf750-33fa-38bf-a797-faf7b99b8754 | -1.562 | -47.7465 | 2026-10-07 19:10:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 4fa12d48-aa4d-3e8e-8b34-530d5dc793ee | -6.1502 | -39.4158 | 2026-10-07 19:10:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 49248725-218b-3ead-a474-d07fce7e7b29 | -9.0406 | -65.9401 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 76009c43-dd12-3577-a075-def6afee0e85 | -5.9699 | -46.3714 | 2026-10-07 19:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| a5daf56b-d704-3625-b63d-74dded34d9bd | -9.9585 | -43.5752 | 2026-10-07 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e1e158b6-41be-3803-a70c-92c146b76fb1 | -3.1972 | -50.5592 | 2026-10-07 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 449.4 |
| 3abac1a9-696f-3b37-bb85-52ad203a6613 | -5.0325 | -49.7687 | 2026-10-07 19:10:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e629b43f-5652-3f48-b521-36f09ad1ab16 | -11.2295 | -46.2403 | 2026-10-07 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 584.1 |
| 9c87b3c0-bcf3-33c4-b0d4-b8509f108b1d | -8.9082 | -49.986 | 2026-10-07 19:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9941243d-8c98-3946-a589-42f0244a94c7 | -8.5366 | -67.069 | 2026-10-07 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| b6e860a4-c49e-332a-ac0e-eb73e7cf10cb | -6.5985 | -41.5582 | 2026-10-07 19:10:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 1db7814f-6b6e-3bed-9305-a479016d081e | -5.749 | -53.4437 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6c67c367-171d-302e-8311-848ea3df180e | -6.7528 | -52.9417 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| e812e234-8c25-386b-8820-c8e8704c627f | -3.7481 | -51.2079 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 9bf602b5-2fde-3b15-afee-fb645380cdec | -3.295 | -53.8597 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 06a74706-a385-3cf0-b03a-71cc6c6583b3 | -8.6036 | -47.1478 | 2026-10-07 19:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 3fdc79ee-9494-35ff-b69c-bfd5d48b5b35 | -5.9649 | -40.914 | 2026-10-07 19:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| e3199758-91a6-3005-9df0-683712c01342 | -3.5126 | -54.6762 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 9ec2777c-ad5a-3e4f-96e8-c0c6c3305762 | -3.2214 | -53.8818 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7795ab01-9c16-3585-94dd-8c8ee5ce8da5 | -9.3394 | -65.4638 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 2199a065-31f2-3fd8-b831-3e0eb4fd979b | -5.9835 | -40.9367 | 2026-10-07 19:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 126.5 |
| a328ea5c-1309-398c-9cc3-3a3698f87964 | -1.091 | -54.1603 | 2026-10-07 19:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 9dc7ccfc-906d-38fb-aa43-aa01278b50eb | -5.2092 | -48.3476 | 2026-10-07 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b0e4750a-c12a-33bc-ab97-7ebb1f0f9061 | -3.7296 | -51.2086 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 20495e10-b29b-3dc6-add1-92312dc2b588 | -2.4942 | -58.0768 | 2026-10-07 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7626b92c-6aa4-3bcc-a9eb-ac46f9238137 | -6.02 | -51.7272 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 157566f3-a200-3a23-84c9-3d570654b6c0 | -3.4947 | -50.0877 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 56ad8909-0118-330b-8ec4-ee02bfc7d9f1 | -1.4771 | -53.6134 | 2026-10-07 19:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5f4922ac-17db-3c80-a9a8-5a05b17eca28 | -3.5862 | -54.6541 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 295.9 |
| a99f407a-eca0-3da5-9247-22baa180aa46 | -9.2451 | -45.6692 | 2026-10-07 19:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| d03b1a07-b63b-397c-b24b-8287bc7c1a51 | -3.2357 | -50.1805 | 2026-10-07 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2cd69c46-ea48-3140-b71a-37d63075bcaf | -3.6603 | -54.512 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 40df3df7-ef5b-356c-89b2-42eb9bea370c | -11.2104 | -46.2428 | 2026-10-07 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| fc591405-089d-3eed-adb3-3f8325313628 | -9.5468 | -64.8196 | 2026-10-07 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 5edd56c2-56bd-3684-b409-cc0d7cf239c9 | -8.9769 | -45.9475 | 2026-10-07 19:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8ce18bd0-6414-387e-a1c5-11ca37ce1a29 | -4.0947 | -52.0635 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 219a8415-87e9-332e-b55a-21d4a73548a0 | -9.9596 | -43.5045 | 2026-10-07 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 77ca167c-2c1f-3a4a-829e-86eba9ba9cd2 | -9.1101 | -48.8066 | 2026-10-07 19:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d1f10add-b994-340c-99ef-95e68f68e22b | -8.5552 | -67.0315 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 78bd9994-aa18-368a-af2e-14bc8189c82a | -2.9271 | -53.9496 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 90b88d81-4bfb-309a-b74d-185634bcadb3 | 2.261 | -55.9535 | 2026-10-07 19:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8bed7faf-91b9-3c20-872e-75446dd4d038 | -3.5866 | -54.5542 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| bd5211b9-f24a-3c5a-8176-8c7f12bc5326 | -6.1402 | -53.0574 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 22526a37-bae2-3c0c-a396-91eb816a7ea4 | -3.8037 | -47.4839 | 2026-10-07 19:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 738c95e8-8850-3d19-9d28-4ef0a2d50445 | -3.1951 | -42.9538 | 2026-10-07 19:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 2380c9e4-c430-3083-83f5-a4bc72b904f5 | -11.2291 | -46.263 | 2026-10-07 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| ea303345-9101-38f5-9e90-a74d881b6701 | -16.0101 | -43.5966 | 2026-10-07 19:10:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 113.0 |
| c7e22f0b-8a52-3daf-9357-db2697ca77d2 | -9.9601 | -45.9712 | 2026-10-07 19:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 3ddf76ea-055f-3707-93dd-7afd8d443e0b | -8.2489 | -71.1583 | 2026-10-07 19:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 107.8 |
| aba981fa-441d-34f7-acf2-b0fd096eb486 | -2.9446 | -54.2103 | 2026-10-07 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8f08bcd6-8ecd-355c-a5f6-a93d68bbb3b6 | 2.44 | -50.8303 | 2026-10-07 19:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 790abc34-6136-3335-a78e-5deaed70cbc6 | -3.6931 | -40.8572 | 2026-10-07 19:10:00 | GOES-19 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 126.8 |
| b1beca1d-8c6a-353d-ad2a-d7414851bbf2 | -3.3133 | -53.8793 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 69b08c6d-f5b6-33c4-b37b-0ebd9a10b928 | -3.3318 | -53.8587 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 39fc9c12-d1e8-3d9b-9bd0-54dc777fd676 | -5.9699 | -53.5953 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| bb8af027-6d08-3f46-8dd1-9894305f2fa4 | -9.9787 | -43.502 | 2026-10-07 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 4cd542bf-bff7-395f-9b1c-81a1b72480a9 | -3.8786 | -44.1265 | 2026-10-07 19:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 2c316701-decf-33db-a230-c6dfd70b46e7 | -5.9833 | -40.961 | 2026-10-07 19:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| dda1eed9-2123-3e2f-bd55-a65697f9f38f | -6.8292 | -39.5472 | 2026-10-07 19:10:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 2964cc55-8386-3f63-a385-f7815bd0689d | -11.6177 | -43.6906 | 2026-10-07 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 216da822-ee47-3962-9815-5a11feea1c5b | -5.7305 | -53.4446 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 37eeb033-44ef-37cb-b561-19c2f1306d42 | -5.5148 | -42.8164 | 2026-10-07 19:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 63ea7d44-70f5-3ba9-b4c9-83a1217c8887 | -3.05 | -53.93 | 2026-10-07 19:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09e0999c-c6b5-3c64-b274-c5691d315fb1 | -6.9 | -43.69 | 2026-10-07 19:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47f015dd-10c2-31e0-90f4-0023e3ea7d01 | -3.2 | -42.95 | 2026-10-07 19:15:00 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7409a99-00e4-3450-b528-03003ce68c1c | -5.73 | -45.18 | 2026-10-07 19:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6c542fc-e931-377e-a865-37a2d0ede2cb | -6.05 | -43.13 | 2026-10-07 19:15:00 | MSG-03 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 50efe280-a26c-3465-a745-7654368702b8 | -4.05 | -44.27 | 2026-10-07 19:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6c87c0b-33c2-3c01-9272-ff3046c19d23 | -5.73 | -45.14 | 2026-10-07 19:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfc405e0-1fb6-3810-8c31-1617eedee835 | -6.03 | -51.74 | 2026-10-07 19:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb2fe92-d91e-35a0-bbd2-0f28022a1e6c | -2.76 | -54.08 | 2026-10-07 19:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa07e012-a512-316e-863c-288faf3c4e30 | -3.29 | -54.07 | 2026-10-07 19:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32875698-c960-377c-a425-018dfb876b10 | -3.02 | -53.92 | 2026-10-07 19:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c409288f-4f74-3f23-afe7-968fe3f65fb9 | -6.87 | -43.69 | 2026-10-07 19:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d42b11ab-b1db-3649-afb9-e5c4ca1a5631 | -5.5 | -42.85 | 2026-10-07 19:15:00 | MSG-03 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95f4d7cf-32a0-35ea-a83e-f3b6828b2f7c | -3.02 | -54.05 | 2026-10-07 19:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e342d78-eaf6-3da9-80cf-a98d7280ebee | -5.76 | -45.14 | 2026-10-07 19:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43965a1a-47bf-380b-b60e-9574ce051729 | -2.79 | -54.09 | 2026-10-07 19:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d41103c4-c42a-34ca-b8db-1a044821cd75 | -6.85 | -42.27 | 2026-10-07 19:15:00 | MSG-03 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b329c21-d203-37bd-8128-4c7acf3b742f | -6.05 | -43.18 | 2026-10-07 19:15:00 | MSG-03 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| aefb3958-ae03-3453-94a1-2b05ef2c985f | -3.29 | -54.01 | 2026-10-07 19:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 578ff5c9-0f58-3484-863d-92d7658e61d5 | -3.05 | -53.87 | 2026-10-07 19:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e300e40-4718-3f63-a26b-c61f8ca78d27 | -4.05 | -44.31 | 2026-10-07 19:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6d93bd0-101a-3967-9f08-b98ea2826717 | -3.02 | -54.11 | 2026-10-07 19:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README258.md)
