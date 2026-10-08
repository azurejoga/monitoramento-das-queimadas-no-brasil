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

## Dados Diários - Página 302

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93e126af-ea52-3e77-816a-2e3e59f51008 | -1.70923 | -49.83929 | 2026-10-08 16:20:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 77e55e98-c26e-3d9b-8d87-46705ac7b13e | -3.49333 | -39.4978 | 2026-10-08 16:20:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ff31b9a4-6939-37d5-839c-d4774947ecd2 | -6.19206 | -52.87933 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5461efd4-7bae-30d2-9586-35f41bc65eaf | -2.0856 | -46.5808 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| b39620c5-dff7-372f-bfa9-a89ddc373e40 | -6.65834 | -51.82679 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2a83e148-9778-301b-9e16-b35f120c0f87 | -6.82542 | -39.55092 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 5f583be5-77cf-3eaa-9560-ef91dc8e7ee3 | -7.68804 | -44.74542 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6af54a8d-9d55-31cc-b02c-90acecd8faa9 | -7.46104 | -42.83038 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 544beea5-d031-3e81-b5bc-ae60aefe9473 | -3.01254 | -43.1112 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bee60283-e486-3920-909e-fdbd8fcd3247 | -6.32129 | -35.13898 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| fee7ef0e-9a8b-3605-935e-ec0a117d866f | -6.38929 | -42.53943 | 2026-10-08 16:20:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| a550653a-f539-316e-9abb-350aa27392f9 | -3.01383 | -54.04193 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 531569f4-3e0c-3658-9e8b-764c85d62b33 | -6.5313 | -45.38506 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 4e31a6be-db98-32a6-a7be-605755425aa5 | -3.23457 | -42.62464 | 2026-10-08 16:20:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 825f7d61-c7c4-3f11-a99f-d19554a38cdf | -6.9132 | -43.93276 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dfe43a17-4fde-3ea1-8893-a7b11ba3b844 | -7.19154 | -44.34129 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e4c8b919-bbd4-386d-8621-cb75fa392c34 | -6.42894 | -44.84079 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c939cdbc-47eb-3b18-b37f-46e112514d5d | -5.53045 | -48.17248 | 2026-10-08 16:20:00 | NPP-375 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06c66fbb-4ff5-3e74-85e3-49bd2929fdd9 | -3.42825 | -45.04717 | 2026-10-08 16:20:00 | NPP-375 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7aa0bb19-53ce-30b5-a178-de5d39d11e98 | -5.73532 | -45.15861 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d2932987-b026-3611-ab41-f1efffc9402b | -6.79952 | -45.06018 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 6c36c500-bf16-362b-8e3d-088fb1a61918 | -6.13352 | -51.76064 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b257c45a-d683-3c94-999d-191db2597b34 | -6.53739 | -45.39687 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| cd608acc-a754-30f1-b773-265943ec651a | -4.69449 | -50.6414 | 2026-10-08 16:20:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 312d8ff1-c467-3c8b-b644-7f4fb31494c0 | -4.09017 | -44.13336 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 3b7c8905-3972-3af5-be19-3a0dcc8685cb | -6.32844 | -43.35222 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4c63cf61-e5ef-3f02-b2a4-48f52bfa6164 | -3.53292 | -44.31084 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d104917-ca54-32d5-b432-b589202ad45c | -5.37805 | -44.20723 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 57b282e4-a4a3-3bfb-a49e-462a38e3156d | -5.70581 | -53.47416 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 59b5207e-0fc9-39e8-a34b-718c6fd6617e | -7.85898 | -44.96179 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d61d003-1af1-3d4b-9cf3-0b11d22b4a9c | -7.47175 | -42.85181 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 08954dd3-13e0-3cf7-9ac3-e3fd02e62a56 | -7.13386 | -44.08365 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bf72206a-5bbb-3c25-b4ba-5f0fcead651d | -6.22008 | -44.85461 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| aaddf7ff-a7db-30e3-9a02-395cc125de22 | -6.36337 | -42.56518 | 2026-10-08 16:20:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 8f42cc0a-63b9-3a26-a8c7-0acf26618a61 | -7.72012 | -44.72826 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dfcb232b-3507-3cce-a718-ec9283858631 | -6.95272 | -44.40895 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54531df2-3cbf-32ac-8a88-ae51c5d04be5 | -6.98483 | -43.96667 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ca16f5b-dd90-3aac-a993-ab35ccfeff57 | -6.24002 | -52.8792 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 656b18aa-9d50-3362-9530-1c5a637447c2 | -5.97164 | -40.91235 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| fad6f7fc-9ff2-3965-bb07-d2eb8fdb02b5 | -5.4373 | -45.68235 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4051948f-9fc8-341e-8c66-bc0ebbf6128c | -5.8744 | -45.95752 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| e8d8c05b-41a6-37e6-bfff-2e9b6e79979d | -5.5166 | -37.49082 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f94311aa-4c0d-3aa6-b9c7-b114d3a16de3 | -6.67967 | -44.32297 | 2026-10-08 16:20:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1c917bbe-7924-395b-9a84-f80ce0e477b1 | -2.73907 | -54.11802 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5dc7f3a6-e8b9-396d-9895-b7d373d4dc42 | -6.55154 | -35.65786 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | PARAÍBA | Brasil | 2512747 | 25 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 09e49035-fd1e-34b4-aba8-f238103ac4b0 | -3.29536 | -42.28731 | 2026-10-08 16:20:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 103aec1f-4ead-3e0d-b88c-3b58e100b953 | -5.7497 | -41.59694 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 997b85d4-431b-3a76-98c5-654265ad4fc4 | -4.0944 | -44.10834 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 071580d4-e03e-35e9-b4ce-a5ddb121242b | -6.60418 | -37.90284 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 3d4c9ad9-70bc-38c0-9381-d95e852a82a6 | -5.35253 | -45.71756 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 711a1ca3-db69-37bf-b52a-221261a74672 | -4.15645 | -43.19099 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d216c6ba-27bf-33db-8ce1-43c1865d5784 | -6.79469 | -45.05674 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2373530e-4af0-39d6-b10e-6788d4e2bb55 | -1.7138 | -47.85909 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4f7b4f46-2241-3679-8d14-0a690e816ee2 | -4.15366 | -43.19484 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d07d9321-09bb-33e2-a673-1d7c6621cd81 | -5.88208 | -45.94722 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 91e097fd-9dcf-3fe8-b70d-ed31811a44a2 | -6.20731 | -52.84932 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4d54b50d-2bca-3738-b776-fcbf21dc9818 | -5.31964 | -40.89145 | 2026-10-08 16:20:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cd8719c6-46cf-3d15-9d87-f93961b01617 | -3.10666 | -53.96118 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 39114265-bf1b-36a0-b61e-0a0396ab52e8 | -5.37991 | -44.19925 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 2573799a-db4d-334b-9893-f7a89024a11b | -6.17173 | -53.43403 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2ab3bf53-d48f-3f1a-82c0-4e5009de02d3 | -3.18351 | -50.56727 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6ae25b7c-99f5-3166-aab8-167cfc6a4e49 | -7.04487 | -44.332 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f6e51e3e-842f-3a10-89e7-50a898740b7b | -7.10203 | -45.24728 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| baced09a-357f-3152-8a48-db59246cce4f | -6.14898 | -38.34419 | 2026-10-08 16:20:00 | NPP-375 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b5610adb-5ab0-3635-a6d9-02b15027a4ff | -3.89757 | -44.1286 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 33194eea-bd5a-3572-adcc-2f59e9c8ff66 | -7.26374 | -45.34869 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| d137640e-04d1-39ad-884c-7f8fa290085c | -5.10929 | -43.1611 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 069f0687-e741-38ae-8f95-1ea70e11e2ad | -6.85161 | -41.77358 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 908fd453-9aec-314f-94c3-fde74188c25e | -6.14789 | -39.43125 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c5f67bc2-637a-3386-b10b-e24c1db42894 | -6.38092 | -45.04483 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad5ee663-a1fc-3802-a978-1580ba895860 | -7.7858 | -46.7473 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0601fd71-4ba0-3e1d-b685-3aa912a2f35b | -7.74244 | -45.44696 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 194d6a1c-59bf-3a61-ba82-2f6a7de1daca | -2.07741 | -46.58637 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| eb9fc5a3-3bb4-3acd-858a-76f1fd90624a | -6.19627 | -37.86409 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 2609f674-b082-3d42-b32f-514c45160e93 | -6.23108 | -35.34499 | 2026-10-08 16:20:00 | NPP-375 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 73c8331e-0827-3b65-a9e2-7d14c0f2b1ba | -3.17548 | -50.59412 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0ef520c7-44fe-3287-a113-a9fc623515f3 | -6.12819 | -47.93158 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 31e14f26-81ce-31bf-8292-114a774a643e | -6.39977 | -44.93489 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 00a153e5-c11c-38c5-9cc0-bd9bcd61ead1 | -5.59182 | -47.26415 | 2026-10-08 16:20:00 | NPP-375 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fc604d38-bda9-34dc-94f0-e6a2eeef4809 | -5.93939 | -44.32891 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 81b56d35-af35-3c90-aa81-56bb02eb3bab | -6.20693 | -40.80262 | 2026-10-08 16:20:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8fdc6b3c-8463-38de-86a4-a18cc07afa51 | -4.43563 | -43.88589 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bd411e2d-8602-3dff-b82e-8ce69c4e1d99 | -3.30225 | -49.1267 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b36feaae-1f21-3f77-b350-5b3df8612457 | -7.10219 | -41.74172 | 2026-10-08 16:20:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 86c98abc-6472-34f8-a635-c732c590b312 | -7.63652 | -44.38582 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5f39135d-fd4f-3ace-81d5-2b7714f9fb6b | -6.97331 | -45.13068 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1a809690-157f-3570-ba8d-8c1a5c1a891b | -7.7049 | -44.7425 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 11df44c2-ee19-381a-bbae-b2612435c3c3 | -3.39576 | -43.0066 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c8ccb164-1f41-3329-b3bf-0e64efff0830 | -6.33279 | -35.16145 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 584dc39a-a621-30fb-9771-6032bcc772e0 | -4.35326 | -43.80272 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d9f98165-1adb-3a20-9771-03765e58f7a2 | -3.78461 | -41.66714 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| b67168a5-3ae9-3d1b-b41f-e34ee16fd2cd | -4.09405 | -44.13285 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 453.2 |
| c1d1cbc7-a67b-3fba-b2b9-264146ad292d | -6.05284 | -35.19106 | 2026-10-08 16:20:00 | NPP-375 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8379743b-9928-39c7-a741-10fe51f099a6 | -4.08597 | -44.10458 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 281.1 |
| 7d98ee31-2739-3500-999e-7d7af560841c | -2.05336 | -54.29845 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| ddd48130-cfe1-33db-ad97-d253aea39fbe | -7.30941 | -44.00681 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27c0f210-fc92-3245-ad26-a17443849514 | -6.46863 | -44.03219 | 2026-10-08 16:20:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a4514eca-2b22-361f-8c8e-b99d4609ff2a | -3.36686 | -42.9109 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5928a45f-e505-3435-811a-804d12f9bb53 | -6.23182 | -35.34951 | 2026-10-08 16:20:00 | NPP-375 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 01ff7efd-881e-34ed-82ed-c6d0b1210bb3 | -5.53146 | -48.17084 | 2026-10-08 16:20:00 | NPP-375 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README303.md)
