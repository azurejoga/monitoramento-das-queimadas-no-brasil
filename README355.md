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

## Dados Diários - Página 355

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2a49934-e828-3d9d-a9fb-556bd7e2e7e4 | -6.15335 | -52.64295 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 7dc422a6-90ee-3827-99fc-1a8e00a17f96 | -4.07921 | -59.84114 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 4962725b-18fb-38fe-9ed3-26a929d8e5f2 | -3.77386 | -59.24759 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9e001daf-6da7-3f90-8fe8-581325501144 | -6.40852 | -52.71533 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1be8cfee-fc88-30d3-8a9b-f8a9164efa3c | -4.15608 | -43.19315 | 2026-10-08 16:39:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 69dbba57-d5d5-3ae6-a347-fbdadd5cc3f2 | -3.89659 | -55.64431 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 49de5a16-ad21-3b9e-a6de-22967b85aacf | -1.32901 | -55.43824 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82d3ed4f-9138-33ec-bb56-5daadbacb609 | -2.66986 | -43.57154 | 2026-10-08 16:39:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f02e799-69ba-39bc-bd9d-091020ef0717 | -3.01567 | -54.12487 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0e115835-5a7e-3b82-a403-647aa9932751 | -4.38602 | -43.94992 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 91f438b2-d8ab-390b-9a8e-c0e354fee4ca | -3.30374 | -41.02323 | 2026-10-08 16:39:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cd5bc2aa-9ed5-394e-a80b-03dbc748ff09 | -3.94425 | -56.02435 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a553a6f5-2151-3695-bace-1d628cb3c3e2 | -3.54518 | -54.68166 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bf90fb8b-55f8-3ca9-8fc1-6db431e27f73 | -3.2552 | -57.19153 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9654a44c-6e0c-3ca2-a4f9-ffa477c70c39 | -5.46706 | -41.22362 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| d49a0bf3-a1a5-30d0-9e57-f96b25469171 | -2.62119 | -56.48758 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7b433b83-055d-3f5d-8603-49ed8292513d | -4.36658 | -40.41587 | 2026-10-08 16:39:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4a1213c4-f4c3-3f8f-9675-e3357f553787 | -2.26911 | -54.8065 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c4701efc-4e1e-357e-aab2-d95e1e376fcd | -5.28373 | -42.72484 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d3fa2942-ce1d-3ab5-a9c9-b79d1b8eb29e | -2.89983 | -59.22767 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 1d4f3bcc-f4fe-32f1-8f77-de3f7e2cb017 | -6.50395 | -55.37865 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 20cbdae4-e5e6-35ca-8244-fe8e69176f66 | -3.33852 | -59.09504 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dccdc781-a11a-3ec6-b16d-966fed5e0684 | -3.78462 | -41.67587 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 62216427-175f-355b-bfdd-9587ea2a6c5d | -2.84245 | -57.48088 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| c7422447-c144-315f-a639-d2e3bda4e803 | -2.8484 | -57.48006 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f84ff13f-bc87-350b-becb-a5790032ed4b | -6.23712 | -51.00631 | 2026-10-08 16:39:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 627a6e97-944d-37ba-aa9c-edcd11eb39ff | -5.09516 | -46.19611 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3538804e-9b36-3c91-8c7e-a156bc6e6e48 | -1.85245 | -57.04707 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 317c275f-d4d4-3d4a-a19a-b8f2c53da0fe | -3.34542 | -42.49587 | 2026-10-08 16:39:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 2d877372-caba-3920-8efb-0e46cc48e18e | -5.44069 | -45.68246 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 67618c33-2674-39f7-90c4-4a9e4dfd3b9d | -6.84805 | -59.38967 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 10273dd0-609b-398b-8b7b-d12fdabd373f | -3.06353 | -58.00177 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4151d1eb-1bb5-3cc7-966b-136b55b2f845 | -2.94718 | -54.05997 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 468292ef-d3df-3124-98e8-b785698ed7e4 | -6.11621 | -51.95299 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 776046f5-a5d5-321d-96a6-3c497b054ba7 | -3.71773 | -59.33445 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ba1e7a99-41bb-362f-acbc-7f85c9056221 | -3.29655 | -42.28924 | 2026-10-08 16:39:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c5d9e7c1-809c-37c4-ae7b-febcaf2b33dc | -1.40584 | -52.72231 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fda0b6a7-39c3-3218-8981-8e306526a249 | -6.86315 | -59.33952 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 14e5a0f7-fc97-39e9-a036-bcd929f78a19 | -5.33121 | -40.89625 | 2026-10-08 16:39:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5083a083-1432-3d5f-b877-c8b321556ab2 | -3.25185 | -57.87582 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 97d8aa9c-121b-387c-b81a-08541881521b | -4.05992 | -55.32234 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1fe9c82-39a9-323d-9e08-71acc2789bbe | -5.98861 | -44.30093 | 2026-10-08 16:39:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d9143c5-8af4-3c73-bb76-4b813254df01 | -2.81722 | -59.24762 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| f7d7bdb7-5365-3b56-90a4-3c95a5f22761 | -3.98963 | -42.62107 | 2026-10-08 16:39:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| c2141a66-a87f-33ad-bea5-30542b8023b0 | 0.53845 | -50.7779 | 2026-10-08 16:39:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b7cc05fe-a58a-30d3-955e-75c55a1e481a | -1.02458 | -49.22117 | 2026-10-08 16:39:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06f2f4a6-9909-32b1-b53e-a5e43df8c608 | -2.98123 | -54.02948 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2b3c454f-7f0a-3bbf-a77c-43e416774996 | 0.52393 | -50.77567 | 2026-10-08 16:39:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 862833ed-2363-3d5a-969a-30ad2b34d640 | -3.17318 | -44.57755 | 2026-10-08 16:39:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 28.6 |
| d59789dc-68ce-3144-9378-b2640c2701a5 | -3.06201 | -57.31897 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| a60ac8af-f1c7-36f2-a96b-5ec40e6d266a | -4.84019 | -40.40422 | 2026-10-08 16:39:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2c00b68e-ec5e-3d10-b2c5-6f968fdd2b8b | -2.56015 | -58.02901 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4d4c934-e956-32ab-8ed7-9ab065ed3c54 | -5.77644 | -45.39347 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e86559c3-8047-38ee-afae-c82aca9aa237 | -5.39312 | -42.96563 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 56409c4b-96ca-3303-b497-7648ef7c609c | -3.76002 | -58.51152 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 7b102094-93bd-3b0a-a577-d86d40542604 | -3.18093 | -54.74728 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6e8d5db4-cc31-3a2d-bb53-38335409d583 | -3.51736 | -44.31584 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| af2dae17-c68c-35ae-b20c-f425301bdc3c | -2.71394 | -57.45768 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b4585368-f7a0-38fe-b875-130af16ede53 | -5.54576 | -43.22059 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9bd8fce8-a008-3e71-911f-ac853c1e6bff | -2.73707 | -57.6142 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aaef681b-fd7a-39c8-ac06-5ee357ee7499 | -5.94457 | -45.69331 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| f3efaead-d245-323d-915e-213cbfa98582 | -5.55262 | -45.57132 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c8d2ac3a-315c-3a31-b403-61f955856e22 | -6.13615 | -51.7638 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3765fa7f-0485-30ad-a29e-caedd4ad681c | -3.01415 | -54.73115 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 33f5a60b-305d-3af1-aab4-d3597fb07ada | -3.81817 | -44.60349 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 57266c21-4b4c-3e20-ad68-855679fee089 | -6.12846 | -53.0542 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a865ad62-209d-302c-ba01-cca31cf06917 | -6.31788 | -55.32547 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 926028d2-e873-35e7-8c61-6307db85ed41 | -3.46061 | -59.46778 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2b66039b-58a0-35ee-abaa-63a74a204158 | -4.66389 | -56.21557 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c1cbe2db-4ac8-37c9-ad59-7971d7aa09bd | -7.23027 | -55.09929 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4e17f101-66b4-38f9-8405-ba2d27970b2e | -5.69485 | -53.48453 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 29b9b748-a858-30f1-9643-8d7f7a3526f9 | -4.58035 | -38.94697 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| fa1868ec-d236-3024-8942-3fc58bce5572 | -1.29029 | -52.93085 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6703c11-56f2-30cc-bf68-aeef279100e5 | -3.4415 | -45.08905 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e5d4b831-9767-35b7-a719-ce6f36f46ada | -3.70829 | -58.93851 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f04f6701-26a2-30e0-bf65-7e96896b5255 | -3.09518 | -53.94393 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 137b4d58-81e3-3617-8121-dba6897bfbf3 | -7.08143 | -52.67883 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 503748f1-86c7-3edc-8a4a-3ebf0291703f | -1.19975 | -48.92169 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49d9fa32-78b5-3842-b5e1-05dff4a289cf | -3.10026 | -59.19496 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e81af14d-cbcb-33db-9913-72d7dbc53ce6 | -5.43543 | -42.64497 | 2026-10-08 16:39:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9b69d169-478d-32e7-a865-fc29938b76fb | -1.60947 | -55.15863 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 84bb9405-6399-348a-9989-00efc0377d5a | -6.57343 | -53.02534 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 5fccec6a-8b75-3e33-8fc3-2177cdb9bcda | -3.45725 | -45.10141 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 003c15c2-1450-3015-a4b1-db9826299eaf | -5.94353 | -45.37689 | 2026-10-08 16:39:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d56cac2e-16ff-3313-8125-e636e3a764f2 | -3.23959 | -50.17482 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4721fbc0-b4b6-37e5-9d6a-55ca0afc7425 | -6.44992 | -52.6489 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a81bc0bd-1bd2-38c7-be8b-e66a1b62e171 | -3.84474 | -55.83804 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 70c96cac-0e79-3e9c-8db4-78177f0cf728 | -4.75278 | -55.6588 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c4a6124-3397-36ab-8db6-afb800dcfff2 | -3.50641 | -43.8308 | 2026-10-08 16:39:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7036cb31-a65f-3a0f-98bd-e2ddf04bf979 | -1.99466 | -56.00327 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb91db9c-98c2-3bdb-a159-8ccc802489b0 | -4.73756 | -55.65568 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4e384657-0c04-3c4c-bb79-6f4a4f2c92e6 | -5.83417 | -53.50423 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6ac869db-a39e-3b3d-a2aa-11d7102bc40f | -6.05061 | -53.47984 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| abcc9454-00be-377c-bc23-379f1c888da0 | -2.2683 | -54.80097 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 45d56b49-01ae-3ae2-af52-89a865ad33c1 | -3.2213 | -43.9755 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4e2ef74-f722-34bd-b1d9-05b67f58c77e | -2.16928 | -54.45626 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf991274-ff1b-35fa-8b48-5a8b57175f98 | -3.74137 | -48.80313 | 2026-10-08 16:39:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4b6fcacc-7e66-38f7-9159-bffff12cbfe7 | -5.61708 | -43.05461 | 2026-10-08 16:39:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c2ad5b0c-fd1b-3b4f-8006-23f050128992 | -6.57808 | -53.02464 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 0009bc95-f851-32f2-a8d0-51753d0a7cff | -2.74669 | -54.09509 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README356.md)
