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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9d51cac-c48a-3ace-82a9-82454a342ecc | -7.01581 | -43.6352 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10fc522f-dccb-3467-a7c8-701b7d04b534 | -7.01245 | -43.63468 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ea27cde5-dfa1-3eec-9d42-8da663b54f5b | -7.79721 | -44.87172 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d03378d3-9cf4-37a1-8d15-59629d996ca6 | -6.65504 | -50.91529 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92919877-c025-37a2-b86e-46bd076930fa | -2.32621 | -47.20167 | 2026-09-18 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 901b27e8-8220-34ea-ade5-6f510dd528fa | -3.9246 | -55.75373 | 2026-09-18 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 14bc2a01-508c-3667-ad5c-4cf38456a17d | -3.37508 | -50.46162 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9c4caa7-299e-3c65-8159-78420885043f | -5.86862 | -52.03669 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d79bf09-466c-35cd-b9c9-3154487160dc | -7.82594 | -44.9046 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad0cef7d-8aa9-3134-ba26-96190302d664 | -7.66775 | -46.08711 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 640e3da0-224f-32d3-bfed-4e9c1937b262 | -7.85573 | -44.80276 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8d01211-e826-3791-a3c8-42f0762da2f4 | -7.30716 | -42.3648 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60461bdd-213b-3ed6-b3ea-195e3efa3c32 | -1.1498 | -54.17234 | 2026-09-18 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ae57be4-585a-3300-8632-c0f14e682fd1 | -7.79675 | -44.89647 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfa992bc-0832-3aed-9e77-c81251718783 | -7.35075 | -44.63826 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b77e3c2-db46-3bb5-82ef-0690c58fec32 | -7.44253 | -42.11268 | 2026-09-18 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91ad0d98-87b7-3f92-a2c3-ac67c0387685 | -6.91489 | -41.71394 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b2289f4-cf13-3a04-9e2e-15dd73d98e9d | -6.78234 | -41.47039 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 325f4ef6-8d49-312f-9712-af0a39dbc721 | -6.15233 | -47.71953 | 2026-09-18 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8156fcfb-8f87-34bd-bbdb-c47fb5470470 | -7.57509 | -46.35183 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 296d1223-b0f8-37b5-8cc3-55c648196d84 | -3.70727 | -54.18081 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c54cc00-f96c-3505-b6ea-788e67984be6 | -5.57997 | -48.10641 | 2026-09-18 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4450a5ca-c510-3d68-979b-11a070c3e918 | -5.64397 | -44.80727 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a02dae02-c8e2-3bc8-b1f4-b6bc21065de4 | -7.7956 | -44.88211 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c332973-2d95-3f32-bbe1-89e9eff95b45 | -7.08999 | -46.15007 | 2026-09-18 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67d14a25-ed4d-39c2-9164-6341b619da73 | -7.37617 | -44.51771 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e35e3cc-03ee-3255-80a3-5150c6f67ca7 | -7.62482 | -45.843 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dd91a4d-b1a1-3d63-8087-f89ffe2486bf | -7.00746 | -43.86744 | 2026-09-18 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f9756515-c9cb-3a04-9621-b1c25da94a26 | -7.60818 | -46.12093 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8563194-a920-3e9a-998b-a27ded93a0da | -7.06028 | -47.5099 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f51b2cb-70fa-3aa6-9ccd-8eb30f82e1d5 | -7.24511 | -43.64818 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61ae0068-ce8e-3ba6-8718-5e225f0b54ea | -7.67939 | -46.09977 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8397e5d5-76db-3d33-9885-794f0d22c581 | -0.78224 | -47.54879 | 2026-09-18 04:19:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b34fd1cd-d55d-3f75-9f6d-05e29e6edec4 | -7.30775 | -42.36084 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 739f20c3-cd21-3b37-863b-8e397ee9da1d | -6.61557 | -44.20248 | 2026-09-18 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0539b82a-746d-3255-b779-312bf5691f6e | -0.88394 | -47.56437 | 2026-09-18 04:19:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdb8f957-b4f4-3fc0-a450-3b4d1816fe6e | -2.81758 | -50.47211 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| e64aed80-b519-3b6c-aa7a-400c2e12f96b | -4.53652 | -54.93604 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 168ea5f6-cc9b-33af-bc63-1cbeae304cbe | -5.49914 | -45.79641 | 2026-09-18 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05f4874d-ac71-34bd-9f0e-f32c8ea88333 | -2.49154 | -49.41153 | 2026-09-18 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06fd7a45-db74-311a-8d17-bd5e74e33d3a | -4.38179 | -55.03784 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44a2b194-da82-3206-9c27-0e46be52af0d | -5.1746 | -56.18419 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb1910bc-8c71-33ef-8049-acf9e153ebc1 | -7.20788 | -47.87815 | 2026-09-18 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25a05656-af77-3090-b1bc-ce2f0ff0c840 | -3.17936 | -48.58174 | 2026-09-18 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e91db892-1334-32fe-adc2-4c6219c27335 | -7.71929 | -42.51303 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aa794ab9-e270-3c0a-8f3d-dbfb2f92848c | -3.06782 | -49.51768 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d941cea-7f9e-3c2c-8718-d719b993ef4e | -7.82318 | -44.90062 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7220d857-ce6f-3b91-a6d3-118fb1eee1fd | -7.81935 | -45.10225 | 2026-09-18 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b929384a-52fa-3964-9f42-8b9c5a7ac11e | -2.79768 | -42.48182 | 2026-09-18 04:19:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f15a0a0-2bb1-3034-b817-ff0d2db20558 | -4.61725 | -42.83123 | 2026-09-18 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a73f612e-2d98-3897-a718-e5fc79d9288d | -7.81657 | -44.89958 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d8e108a-d1da-3e09-931b-9ef074070363 | -7.14724 | -41.40717 | 2026-09-18 04:19:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bc97f414-aabb-3d94-a9d4-11454aa6b094 | -7.8169 | -44.83217 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c155ce12-bb0b-3012-bb7a-bed963ba3868 | -5.43149 | -43.43996 | 2026-09-18 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6e9c5e9-135d-3de7-a1bc-a363805786fd | -7.34906 | -44.62729 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ab515a1-a250-3296-b3d2-7c660e8bdaa3 | -4.44291 | -55.52416 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a267f0e8-ed5c-3877-ad49-99b3ff649c37 | -2.82128 | -50.47718 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4715069b-cead-3d5e-9ea5-1d45a62dec44 | -4.80641 | -56.0846 | 2026-09-18 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e36a7c58-5cd9-32c5-b0c9-d22b5de7aa8d | -6.66653 | -50.92534 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ea277de-7157-3c81-8c36-df1742c60baf | -6.77833 | -47.86457 | 2026-09-18 04:19:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecc2874d-cb0a-3bcd-919a-71f5520e8dbd | -2.82056 | -50.48158 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 89717cd6-6a13-3f57-97d5-2d79b70a572e | -4.51263 | -54.97092 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c4be6f2-fe5b-3b71-a4db-82044870e479 | -6.99012 | -43.32759 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42d9608c-5e80-3cbe-8cd2-42df71eee929 | -7.8188 | -44.90702 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d759e76-4389-3c4f-bd2a-551dd4aed706 | -5.73397 | -43.28181 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11fd3e5e-d5c3-3408-a126-dfc742322b8c | -3.37717 | -50.44897 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d24afa0-7c25-3e92-99fc-db945e46c140 | -6.77476 | -42.77903 | 2026-09-18 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e2e9f4d2-0a58-3e11-a8c9-d66abfe3cd4f | -2.96196 | -52.14645 | 2026-09-18 04:19:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0ad6e24-991c-32b0-bf39-f1c313f34722 | -4.42658 | -55.52084 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f6d66dc-5e0e-3f86-a34b-25569cbe54ed | -7.80828 | -44.88764 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 583be7c6-082d-3d81-b4c4-f1ca1a9c5b0f | -7.35148 | -38.9867 | 2026-09-18 04:19:00 | NOAA-21 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f535487d-825d-3e0a-95f4-9229ea9f36e6 | -7.79337 | -44.87467 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 360182cb-aa05-3c49-8588-e3abe2b9024d | -3.7622 | -51.13789 | 2026-09-18 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70ec408b-85cd-3aa9-a075-e7675cff036d | -5.77903 | -47.17574 | 2026-09-18 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db4add10-563e-37d0-83e0-c620ca42ec8e | -7.08786 | -42.08787 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74d6c0b4-eadf-3591-b742-75165c70c776 | -7.09143 | -42.08841 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 654aed4f-4a28-32d6-9638-e91766e78fed | -5.49841 | -45.51904 | 2026-09-18 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03c57555-9261-3d1c-bf07-2def86f58062 | -3.38154 | -50.44969 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d51f1c5-b31d-3309-9fe6-02d7daf55905 | -7.35183 | -44.63129 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9b2bc34-155d-3470-a837-3d0c3884f665 | -7.0618 | -47.47814 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7f4bb181-13f5-33f4-af66-0c7881349c1b | -7.9578 | -44.05383 | 2026-09-18 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04385ced-485c-36cb-96c5-0d99e5df00f6 | -7.79291 | -44.89941 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd9e36cc-9dfb-38dc-b348-dfb47d295b66 | -3.04126 | -51.37415 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 007d493f-77b5-33f4-9ab9-02591ba70fc3 | -3.92375 | -55.75866 | 2026-09-18 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f2097c7d-f524-3a9f-9d28-6ae65e9567ba | -4.38253 | -55.03354 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ad47bbb-3376-3137-aebe-a9421f73b4ff | -7.34993 | -43.89085 | 2026-09-18 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b10c52f0-780f-3ff8-b21a-054bc21481d3 | -7.63151 | -46.16801 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b513a8a7-404a-376b-960d-ab65f0b39267 | -5.75866 | -45.09783 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7888ee8e-b6d3-37d6-9685-3a58821b48ff | -5.14599 | -55.94917 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc2931e2-eb10-30a2-91bc-d28db32b0122 | -4.43076 | -46.29371 | 2026-09-18 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37db177a-327c-3248-a730-4d52d5022876 | -7.36713 | -44.46634 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4d3585b-6873-3e91-99b1-7bd0d21b8afd | -6.1102 | -41.80556 | 2026-09-18 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 471f50b1-21de-31a5-8827-7cbd5969c548 | -5.65732 | -43.20787 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 82ad266f-1171-3e22-8905-e7f8f83381de | -6.01758 | -51.76809 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccce7ddb-4b30-3957-a56c-09cc02bd0826 | -4.47556 | -54.97722 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36c9fa2a-f97a-3d9e-8f6e-e2a8e02d4b03 | -7.82648 | -44.90113 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6191033e-f218-353c-9ba3-3fcc7af5b9b6 | -3.37 | -50.46517 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9745402-f4ef-372c-8baa-61ad088407c0 | -1.78422 | -47.83679 | 2026-09-18 04:19:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 7e722844-2a6f-359b-b83c-42ffe3356dfb | -7.06342 | -47.49034 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31e1f3c3-88ef-352e-a902-7f857930589a | -5.75921 | -45.09437 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README37.md)
