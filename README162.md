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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1049a5c0-e3da-3a55-b10c-577e402a5b15 | -4.58888 | -40.29189 | 2026-10-07 16:03:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| d91aaa91-7963-3d92-8462-867d77379164 | -6.90673 | -47.39563 | 2026-10-07 16:03:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 66619d64-7c0e-373b-9a7c-2896573f2a6d | -3.23264 | -42.63198 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| eab4f4f2-4166-3483-bb8f-5d5dffe68e49 | -6.60159 | -37.88757 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 3951430e-a5fd-375f-9dfb-6111564fa44d | -5.20939 | -48.34488 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8d745412-06ae-34d5-b2a1-5805c236c958 | -6.12281 | -44.13439 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bfdaf114-bf4a-383c-b83d-a66b1caea577 | -4.27674 | -39.54382 | 2026-10-07 16:03:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 20.5 |
| f035d8fe-7adf-3670-b7f6-ae533585a1bb | -6.93674 | -45.27714 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 1f4835c5-cd91-3245-8ba7-e7b342a85946 | -7.80847 | -45.50021 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a104135a-11fd-32c8-9f90-8a3db188882a | -6.69866 | -44.01647 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7e98f99c-7f68-3075-a371-a3bc392011b9 | -3.74626 | -44.69712 | 2026-10-07 16:03:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cae2511d-1e7b-3d21-bb0e-0511788cd25e | -5.99783 | -44.12669 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8ef69a52-3ef9-3247-961a-c0fd409795d0 | -3.47959 | -39.48508 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2a255a7a-8d64-3e00-926a-892af38d862b | -3.49551 | -39.50048 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| bf70dce1-66a1-3f87-9b1b-d44a4ddee6f0 | -5.9491 | -46.39493 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 463445a1-2ea9-3db0-991b-ab3237eaa932 | -5.73708 | -41.73863 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 50.3 |
| cc1f16a8-6829-3457-abd0-b052f6bfca54 | -4.0901 | -52.06893 | 2026-10-07 16:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e72b98a8-ad50-363f-a590-d2dc628208cc | -5.97705 | -41.3628 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c58d6faa-1d87-3ef4-af8e-fbcd6d44891e | -3.39771 | -42.83001 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a1d2b133-0e8f-367e-8d4e-e239eb16b141 | -6.68289 | -44.96209 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6e635d1c-4c02-3b34-ac02-777a81c9f5f7 | -7.74809 | -43.8356 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18d2c151-a1a6-35ad-9211-a01d2356db1d | -6.79501 | -41.25119 | 2026-10-07 16:03:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 18ec36f8-8a80-36aa-b2c6-17af97d7f1fb | -1.22233 | -49.04102 | 2026-10-07 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1df04752-aad3-32a5-a513-25488cea69d7 | -3.78692 | -45.24501 | 2026-10-07 16:03:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3f282da5-5632-3713-908c-853974113397 | -5.68011 | -47.93782 | 2026-10-07 16:03:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e082274-18f5-3fde-bfb4-75604300f75d | -6.34039 | -43.83857 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| fc93eb7b-39a8-31f6-b5dc-9b3979e2568c | -7.73811 | -45.45504 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7e175b39-742f-3127-b92f-cba8f5cef94f | -7.8165 | -45.49614 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b8d41bde-9c86-3355-8f82-6b579a24705f | -3.18471 | -50.56958 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f064a5a1-8ef5-337f-bb35-c7384f164806 | -4.36551 | -41.82115 | 2026-10-07 16:03:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 7f8ce220-0388-36a4-b295-0d0ed6e1b20b | -6.84025 | -39.55651 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| f8832c07-e5f3-3523-9e1c-83bf15a7cf71 | -5.96605 | -40.94486 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 8d00d69f-38cd-31d2-b955-170418575cc3 | -6.93062 | -44.64896 | 2026-10-07 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d870c52c-9212-3491-a847-b784e18c0bf4 | -7.7772 | -48.24334 | 2026-10-07 16:03:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 133a2137-8025-3a8c-b8f7-73e7bcaae6fc | -2.41326 | -51.3013 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a9535a8b-de48-37a2-a4a5-c02c8e6cafc9 | -3.78019 | -41.64385 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 90415c67-1bb9-35b0-adf5-c178f461dd82 | -2.41249 | -46.03307 | 2026-10-07 16:03:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 78adf4c7-bdc0-3b5f-ab98-e86c3af373c9 | -7.12455 | -44.06857 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b0dcdab7-12b5-3ce2-8f4f-a0b33014142f | -6.43277 | -38.1405 | 2026-10-07 16:03:00 | NOAA-21 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 8ce6bacd-a533-3faf-8ef5-c04f551547bd | -4.58666 | -40.77071 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| a85fa0ae-46c4-3004-9bba-a81f11d5c16f | -5.98507 | -40.92582 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| b224b6ed-a0c2-350c-99de-a15769fff88a | -6.19082 | -44.65424 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 65d245c3-bc22-3a6d-9fb6-a6b1816b1d87 | -3.49994 | -41.94495 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 070cc032-65ca-358c-a889-cbe800e9500e | -7.21483 | -44.29705 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 90b41140-e92d-39ef-b430-2608bb77dbf6 | -3.87566 | -44.13327 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0a935f9e-3628-347e-a4dd-295773c6fffa | -6.82901 | -39.55072 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 44.2 |
| 562ca03d-1494-3ab2-8fea-eebfd4c518f7 | -4.56544 | -40.72339 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 5fb81b57-dd85-3cab-b634-e0f76d69b4ac | -5.72669 | -41.7446 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| ea1dc718-ba25-3e77-985e-81f6c7aa4969 | -5.95199 | -45.68926 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e020ffbd-9e67-3459-91a0-7b19d3e9ad59 | -6.8324 | -39.55026 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| faa7fba7-475f-330c-ba90-e262b178645c | -6.70352 | -44.0198 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9ebeecce-ab40-3f60-8135-36d369713bf6 | -6.75762 | -44.33569 | 2026-10-07 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bff533f8-6c57-3754-9898-ab55c34afc42 | -4.87149 | -38.71538 | 2026-10-07 16:03:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| feb5fd02-36d4-3794-82b3-3eed4a3b515a | -6.99138 | -47.52621 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b33df93-70cb-35f1-9b7b-57b541d8dde0 | -3.87761 | -44.11758 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 467db6c7-b8d2-3525-aa32-cea141605430 | -6.60437 | -37.88361 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8cfb655b-54f2-3d1d-898c-c2e52761b19e | -7.29028 | -47.28594 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e05d1bcc-3b73-3657-bc32-ac424c4d5be0 | -4.91764 | -43.22897 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 34d45dc9-49d7-3dd9-aeac-794e701cc0ec | -5.96796 | -41.3512 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 1f38da7d-5f5f-3224-909f-57783d433692 | -5.01016 | -50.94316 | 2026-10-07 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6771d9d7-b115-38d4-98b7-fd13c807b4dd | -7.00212 | -44.06017 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1a6d9a89-e1a4-3ccd-b20a-ba1ba2d1d16d | -5.97046 | -46.40117 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0da40b35-4b0b-3ab2-ad84-a9262acef360 | -4.04758 | -50.98376 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8e016f83-37aa-37d0-a3b3-b7552be842c9 | -7.28978 | -47.2823 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 44bdc156-df54-35ea-a7d8-6df1e3f54c0f | -5.33991 | -45.68981 | 2026-10-07 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7b3ac83e-9ecc-321d-a570-65692bc11f94 | -4.17731 | -42.042 | 2026-10-07 16:03:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0dc89420-f58b-3740-a68c-8ed5a26d5205 | -6.99415 | -45.11806 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| da2eb977-5d1c-3c53-a185-756880879e5f | -5.96088 | -46.36973 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cb6bc2be-532d-3130-af3c-c937b07972b6 | -3.86788 | -44.13823 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b7702e81-3f44-38fb-8501-573d76584497 | -5.93943 | -45.39803 | 2026-10-07 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 433fb166-e05a-30c8-a642-7e8aa00aba8b | -3.79221 | -50.87029 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| eb6fac70-5c20-369f-9ff3-cb028de096a9 | -5.33498 | -48.5557 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed088823-60a7-320c-a673-69dfbd521168 | -7.81332 | -45.49952 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 43d56859-3afc-3927-9c97-9914969ab9cf | -3.50782 | -41.94804 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 5147da6f-252e-3bf9-b2b7-56b6fbe5f617 | -3.20373 | -42.80257 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9950c8f3-ac53-380c-b209-b62c3316c57c | -6.20256 | -40.80596 | 2026-10-07 16:03:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 548dbd04-525b-3bd3-9e12-ac7814dc8e8f | -3.59386 | -42.90024 | 2026-10-07 16:03:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 11f16be6-917c-3949-92a5-b57dd145a3f2 | -3.58786 | -39.14557 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 28.0 |
| ed2de77e-7d18-36dd-9000-c884c26f902f | -7.56535 | -46.717 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3acee628-2ade-371f-988b-15bc513a0fda | -2.93793 | -40.87636 | 2026-10-07 16:03:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| de070161-169c-3961-8b80-772364883ffa | -5.10232 | -42.92531 | 2026-10-07 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8b01af73-f6ab-3a91-b674-4473c06251dc | -5.40722 | -45.64281 | 2026-10-07 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ea62d60-d2a9-37f5-a46f-3dad339f95f3 | -5.28586 | -42.69777 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| ad2c46ad-82fb-38b8-9afc-2072615f1289 | -3.22889 | -42.63253 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ba8a50aa-5f97-32c1-b919-d5cb487bd472 | -7.53501 | -45.87548 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| fb08ff43-e0d8-37c1-808c-121515beb051 | -7.40729 | -45.64857 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f5023cc5-35e3-30e8-a17c-0abf4024125f | -1.87888 | -45.43584 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a5c1a9e3-673d-3584-a7bc-60de5c0a0335 | -4.57028 | -43.87948 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1cd5bf30-23ec-3ec8-b519-5d4590aacd95 | -3.18063 | -50.56068 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 627cdce3-6552-3ef0-8abd-225e0929c1a2 | -5.95126 | -45.68414 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8ce7e740-2836-3578-ad52-ecdbf6fa4ce0 | -4.23507 | -49.98162 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 27819758-3f35-371d-adbc-72ebaf9099ac | -7.00646 | -44.05952 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7a32e3b7-764c-388e-a442-5f3ea8651565 | -3.18884 | -50.55327 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 61e0c166-b017-3256-90d4-ea8ea8be2120 | -3.20417 | -42.95925 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| cd32fb8a-0b0c-352b-bd79-c3cf924ed718 | -3.87599 | -42.2084 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b7cf084e-29d5-3880-96c2-ce69c20c64e2 | -6.68593 | -45.34483 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 935bbdc8-7964-314c-bc3c-1fda10c7facd | -6.83633 | -39.55341 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 28.5 |
| cd7b86bd-e19e-3800-87d7-b99f1a554b1b | -8.11121 | -50.93222 | 2026-10-07 16:03:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 21fbfe52-3073-3370-b9d3-5e5078b20948 | -4.76911 | -43.67047 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2105a060-2460-3f19-a236-c2937637304b | -3.74686 | -44.70122 | 2026-10-07 16:03:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README163.md)
