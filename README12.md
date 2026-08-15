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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d54d752-b882-3bbe-be63-60c4ce1537f6 | -5.11915 | -41.1038 | 2026-08-15 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cfd533e6-843a-32c0-a2ef-d3683495876b | -4.95015 | -37.93874 | 2026-08-15 04:12:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05ab1b4f-b383-3b6e-aa6c-a698739e65d3 | -5.04468 | -43.26086 | 2026-08-15 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5719afa4-73db-30dc-b1d4-6d293fc975f1 | -2.85911 | -46.80072 | 2026-08-15 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79a25b20-e7c2-3f20-8c05-62a8c6dec000 | -6.83474 | -41.66227 | 2026-08-15 04:12:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8585bcf1-3019-30d4-a81c-9859025d2bac | -5.491 | -45.12231 | 2026-08-15 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b704b379-bc1d-3e1d-a16e-dcc96ddb4903 | -5.34204 | -43.17987 | 2026-08-15 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 626cd25a-c587-3d7e-b1e5-a5c0bc506548 | -5.9334 | -43.64513 | 2026-08-15 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40e1596a-e991-38ea-850d-776a070057cc | -2.64709 | -47.98122 | 2026-08-15 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a63bf0dc-aa27-3c50-a25c-217d307e90c7 | -4.10626 | -50.99618 | 2026-08-15 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e93c6fc6-9d13-3702-940b-3e8d094acc82 | -4.1015 | -45.90024 | 2026-08-15 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 753acefd-219b-3aab-8518-c5348cbcccb7 | -4.10759 | -50.99712 | 2026-08-15 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95cb797e-62a8-3af4-9210-c24f3559afdd | -4.10439 | -42.50352 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1300aa6b-1b0c-354f-8e1f-c1b69b8c6322 | -4.4594 | -37.82431 | 2026-08-15 04:12:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5d7ab75-ce98-33a7-a81c-11c50065520b | -6.83528 | -41.65881 | 2026-08-15 04:12:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f5d92ff-2a86-3c38-b4b8-16551ca85153 | -6.08955 | -40.722 | 2026-08-15 04:12:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02fcc94a-cef4-3595-a090-dbdd83bdc53d | -5.1351 | -50.84943 | 2026-08-15 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a2973c-18b0-38f7-8a9e-57c97da0863e | -2.62532 | -47.99769 | 2026-08-15 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8154e049-fe6d-35f7-a0c6-198882b68eb9 | -4.01685 | -38.2509 | 2026-08-15 04:12:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2a27a378-b2a3-3476-9b54-4eebd0912edc | -5.19244 | -35.85144 | 2026-08-15 04:12:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ffce418-36e8-3a36-b02c-700c24682f8b | -5.11639 | -41.09983 | 2026-08-15 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1fcacf21-249c-3b88-a198-a9e7215cf93e | -2.80739 | -48.59249 | 2026-08-15 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 34232ad8-4693-3832-8cf9-4e2c245d8c0b | -2.68762 | -48.21823 | 2026-08-15 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a44c118b-2804-320f-8441-a09d2a15cbeb | -2.64788 | -47.97635 | 2026-08-15 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26441645-6839-3d9b-ad3d-250fcf93e8fb | -1.5878 | -50.44161 | 2026-08-15 04:12:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47c40b41-0a8c-32ff-b87a-882d7ce7744a | -4.92773 | -37.91335 | 2026-08-15 04:12:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d45d2a81-3be2-34a3-8984-6af4739f4e0e | -5.33864 | -43.17933 | 2026-08-15 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b3004be-8d7c-3554-870b-68570c7562f2 | -6.26681 | -43.27722 | 2026-08-15 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 67a1fb41-4ded-3ad6-836e-6d1d2a06bf58 | -4.10818 | -50.99356 | 2026-08-15 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a5c8d52-7b29-3af5-9ca2-0c140bd82388 | -2.95272 | -41.95273 | 2026-08-15 04:12:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 379db045-6e98-3a58-a0b1-b0b2c058ba43 | -6.85881 | -41.64104 | 2026-08-15 04:12:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 005e6f7d-9e73-37ca-894c-352309fa1b18 | -6.12032 | -44.03242 | 2026-08-15 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 713e6677-70a1-365f-a233-31edcddbf85d | -4.09178 | -42.505 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a7b1cb4-88b9-33da-bfd3-59df96982e8c | -2.9555 | -41.95677 | 2026-08-15 04:12:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc6808eb-b3c4-3b45-9a5b-b9089f9ecc44 | -5.66783 | -43.5722 | 2026-08-15 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2146597e-2958-3c03-bcec-3783e1235239 | -2.62998 | -47.99842 | 2026-08-15 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90a603dd-006a-310a-82d0-832cbe2ac378 | -3.18329 | -41.87019 | 2026-08-15 04:12:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bcc4467-2003-3d02-9746-457499ceb1b1 | -4.1026 | -50.99268 | 2026-08-15 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21d6d328-1b38-351a-b004-cf9cb8ee7693 | -2.87637 | -48.85673 | 2026-08-15 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0ba95f94-121c-32fa-801e-b2d386322de2 | -3.2591 | -49.52431 | 2026-08-15 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4252eff2-9f16-3a17-ae8d-c81431aef311 | -3.23684 | -43.22545 | 2026-08-15 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 664b7c7b-6e20-308e-9378-e8a00d68e759 | -4.10775 | -42.50404 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4a161f04-54e6-39da-83bc-5ca706a89797 | -3.2586 | -49.52735 | 2026-08-15 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39621c26-485f-391f-abcc-a53a8f180ba2 | -5.4935 | -43.67595 | 2026-08-15 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cacac103-6f51-30b3-9d66-d6444282865b | -5.04409 | -43.26456 | 2026-08-15 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b1b862b-ee70-34ca-a71d-4eb7d71565ca | -6.11746 | -44.02804 | 2026-08-15 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a750366a-aa99-3b46-8589-5d7662b68dce | -6.34094 | -44.07892 | 2026-08-15 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36ac219f-4b64-3812-885a-ed3f7aed6181 | -6.33808 | -44.07451 | 2026-08-15 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af90c6c0-c984-3c17-9eb0-726d5c7aa087 | -2.79234 | -49.58157 | 2026-08-15 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c414b48d-3a23-3bc1-a947-173697954594 | -5.66722 | -43.57593 | 2026-08-15 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 385848e0-09ad-3397-b9d8-f64904283fd9 | -5.26207 | -45.28874 | 2026-08-15 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e61f3b13-3d85-32f8-b11b-5a48953ba7e4 | -3.42263 | -43.16503 | 2026-08-15 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bab2d09-d824-3133-8551-20bb6df862e7 | -4.92795 | -37.91509 | 2026-08-15 04:12:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52488e16-3ae3-32dd-ac47-2aa9448df125 | -6.41299 | -39.25253 | 2026-08-15 04:12:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 93ec93e1-9c6a-36be-a088-26c30ea4d0f1 | -6.27358 | -43.27831 | 2026-08-15 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49d72c5b-4df1-346a-94f5-e30525376523 | -5.14052 | -50.85038 | 2026-08-15 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc7e380b-7792-31c4-ad06-e6d2be094550 | -5.93724 | -43.66506 | 2026-08-15 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0823c723-9588-32ba-8568-6587a9da6761 | -4.95381 | -37.9393 | 2026-08-15 04:12:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 503254fb-ef40-3f9c-9c1f-6e6a2f09f381 | -5.19661 | -35.8521 | 2026-08-15 04:12:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5d05d90-aeff-3040-a106-64ff511ceecd | -2.81597 | -46.71567 | 2026-08-15 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a16a126e-0d8f-33a5-b1b1-d59a173ef31f | -1.57563 | -47.75032 | 2026-08-15 04:12:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 09fd7998-da3e-382c-bb0b-6a9bf263cde0 | -4.09235 | -42.50143 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8b8a778-44c9-34f0-8d01-17e3cb297f7a | -6.3387 | -44.07068 | 2026-08-15 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0465cb0c-cd9a-3bb4-a997-370f9b8b3cb4 | -1.96143 | -48.37259 | 2026-08-15 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ddd6c87-0daf-3c98-ab18-8d2b1c2b9c2b | -5.04751 | -43.26511 | 2026-08-15 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59cc5dc8-3952-32e7-8dc6-170648c2e390 | -3.41918 | -43.16448 | 2026-08-15 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4c69123-0ad3-3e5e-b86c-f6dcd665261a | -6.83914 | -41.65588 | 2026-08-15 04:12:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76758c46-74a8-3f59-b835-f4635251b611 | -2.85792 | -46.79928 | 2026-08-15 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ded6c33-9b23-3aab-9eab-fd79309f71aa | -4.10832 | -42.50048 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6df255db-aa8e-34b5-a124-6912f334c29a | -3.66977 | -48.93167 | 2026-08-15 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec5f099b-6ab2-32c4-acc4-817f08e4448c | -3.11434 | -47.9073 | 2026-08-15 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c27e3661-3b90-3693-b08f-a674b5bcc4bb | -6.34156 | -44.07509 | 2026-08-15 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80f71627-6dd0-3083-aa97-258e2294dbbd | -5.50358 | -45.25652 | 2026-08-15 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10e4a882-e419-31f9-937e-9fef170821e3 | -4.10717 | -42.50761 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 23d853cb-5819-3730-a467-8e3fe2fbcf25 | -5.93785 | -43.66127 | 2026-08-15 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd8fbba3-005d-3d1f-9285-93b3d8188f85 | -5.93401 | -43.64137 | 2026-08-15 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| df997da7-a210-31ad-b169-eba320fafb01 | -3.97201 | -49.46148 | 2026-08-15 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5253362c-6def-31cb-945c-bba785db874c | -1.58107 | -47.74619 | 2026-08-15 04:12:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4eab0c8-3076-38dd-8151-bbc2dcd5da00 | -6.33931 | -44.06686 | 2026-08-15 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6cddd481-9a81-3b75-80fc-802beaa59e1e | -6.32573 | -43.75607 | 2026-08-15 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1c610a7-980d-3c73-b6d0-f7ce487891ec | -11.40667 | -46.33668 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8cc8f08d-63f7-35c0-87c0-de191a898a45 | -7.2659 | -44.69947 | 2026-08-15 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 423c8259-038f-3d48-ac99-281fdc88c0b7 | -11.591 | -54.67487 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b842dc2-59e6-3d66-8295-683db7257955 | -11.40452 | -46.32703 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c941963c-e3d3-3b7d-ab7c-149b5e4955b5 | -6.79325 | -55.84843 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 747aaf34-aabd-3af6-9c00-f3bd577fdddf | -12.72276 | -48.4272 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7df9af21-5201-3c6f-8795-bbc379171069 | -6.84297 | -45.3752 | 2026-08-15 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c9e0624-6ad7-30b2-8517-9593d6b34446 | -7.72648 | -46.24181 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c753fa1-de99-3505-837c-2d61a7068171 | -8.4522 | -45.11382 | 2026-08-15 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4667cb14-be98-3fcc-897f-caed0ad0dae6 | -10.51387 | -50.15599 | 2026-08-15 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da1ed189-ede3-32de-ae3b-0a1385464b5d | -11.41036 | -46.33711 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91cb0e37-a146-3dad-a348-07b60279aa59 | -9.48157 | -51.61671 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde1e242-ef60-3c4e-a7a7-b74ff5eb68b6 | -13.65752 | -46.25092 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d27206dd-421e-374d-9219-11df19be110b | -11.40961 | -46.3416 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf03109c-33f7-37ee-8c05-5298b13976a7 | -11.39058 | -46.32043 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f585b7a6-f07f-3d3b-851b-b0a5258ced07 | -6.91689 | -43.63648 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5ad985a-a001-3ba7-9036-8d4b90ac6506 | -11.41404 | -46.335 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 938b1bda-be91-3a23-abfe-8bdb75b9061e | -7.00907 | -41.44117 | 2026-08-15 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd268516-1aec-3c7d-87fb-7ee9ab502edd | -12.76356 | -44.55505 | 2026-08-15 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcbef6a5-ac22-356d-9171-5d7788bab705 | -7.27377 | -44.20564 | 2026-08-15 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
