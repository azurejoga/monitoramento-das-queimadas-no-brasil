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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca677edf-0982-3f49-a877-a6ba3f6e9ce2 | -4.5628 | -54.20847 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06e30a89-5fc4-3cef-8fee-4845200df7fc | -1.15901 | -54.2305 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1cbc5bb1-374f-3c81-a66e-944439683a37 | -3.97532 | -56.11673 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e5534e0-620b-3698-8d20-2fa4f9511bbe | -3.07453 | -53.96571 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 982b5a9a-e0df-3b6c-a80b-a0b5e039ef66 | -2.73175 | -54.11086 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36f603a3-2f8b-35ba-95af-181951d59874 | -4.57836 | -55.72495 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17a47ca8-fc23-3428-96a2-a4bc1e79853d | -3.52275 | -50.34762 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f2f9a67f-5f61-34a9-820b-f5685273d2f5 | -3.59654 | -54.56268 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ee1187e-4dac-32dd-8ac1-b4ebd0d3331c | -5.71033 | -53.48525 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4e939b14-ab7b-3092-a683-95548b43ce9a | -1.05232 | -53.59471 | 2026-10-09 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0a4bcb9-4c14-3390-8e27-26085ff364e1 | -3.54158 | -54.62851 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b1680d0-5658-32a6-be22-9711915565a3 | -5.45441 | -42.89032 | 2026-10-09 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e1522564-e0f8-35c8-8313-7fb3a97b2202 | -3.0798 | -54.28262 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7b08780-7bcf-364f-a554-5c4498bb1c0e | -3.44699 | -59.55379 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5d4d6e92-cf54-3e01-8082-53f1895d3bb9 | -4.29537 | -54.80639 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed066520-d8e9-34e3-9993-2cd2a9c6101c | -3.01787 | -54.08848 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9807a82-0e9c-3335-af8c-e4dcffb01652 | -2.55414 | -58.03375 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80ff0508-9818-37a8-a04d-b9a24596d91a | -3.00609 | -54.07171 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab4f8093-1cc6-34d0-a2a8-7cbcf2c6132a | -5.70105 | -53.48378 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9eb3ccb-f4e5-3500-a6a5-0e0af2244782 | -3.17646 | -54.74952 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65d6d9a6-e9a3-3fe9-b7a4-9dfbfa973079 | -3.55782 | -54.69256 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 642483c7-284d-3ced-8c4b-8ab1106a98dd | -3.30793 | -53.71054 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f962770a-570d-30ca-bf76-128719f58e5c | -3.10879 | -53.94477 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f12bd9c0-5fe1-3a0b-8c9e-48492e1fddcf | -3.11057 | -54.18921 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edbd8273-6e9d-32f1-aaaf-d6e98005c494 | -5.98185 | -41.37557 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2fb255f3-fdee-37b2-8025-c233e05f2eb8 | -1.73742 | -52.24535 | 2026-10-09 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 88208f0a-f4cc-319a-a242-09389df3b7d4 | -3.11166 | -53.77206 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b32da1c-0482-32d2-a587-63436e59aa5f | -5.48944 | -44.29736 | 2026-10-09 04:25:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5c102c7-fa2a-30bf-9b1a-0353f249e128 | -4.37385 | -41.81484 | 2026-10-09 04:25:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1d045c79-d024-3b54-b4ef-f440e3de1e9d | -4.27492 | -46.54033 | 2026-10-09 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ebca0da-927a-3b04-9afa-34a238e68c53 | -3.10596 | -53.9621 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e812188a-d7b2-37e0-b650-19ca1d3f3857 | -3.78004 | -58.584 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d85b1028-c92b-3136-bbad-fa6cfc062711 | -5.32976 | -45.18419 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50212e3f-660f-37a4-891a-66b8706b2971 | -2.58513 | -56.18607 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73c9d3f1-c4c4-34b5-a990-e64c6a59474a | -3.77558 | -58.58793 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4ebf95ed-d957-342f-8515-2dcc47845207 | -2.34051 | -48.87162 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b570df74-ccfd-3d54-8669-50098ddcdb46 | -1.53755 | -54.54992 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed65673a-713c-392c-a569-58e55e2620ce | -5.70348 | -53.47708 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7d58b312-53dc-3009-8a60-ead3e7ef69b6 | -3.98594 | -59.35165 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0c2b852-b5ed-36c9-bfc8-4180d9b74104 | -3.00275 | -54.0924 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f2104f8-b8f6-307d-9dff-b08bb9eabc67 | -5.09451 | -46.21812 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baf6c450-a3f5-33be-8c27-6dc3a4f8df32 | -10.78509 | -49.71754 | 2026-10-09 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f08f85a-b7ad-3d37-86a1-531824464f8e | -11.76751 | -46.77119 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69288f00-99d8-3c28-ba42-7c0cf6a8ba5c | -12.23777 | -57.09089 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 1283566e-85ce-39cd-8183-61106261b3c5 | -9.93803 | -43.55856 | 2026-10-09 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 716d48df-7e96-3de8-81b9-b85df14652c5 | -11.24378 | -46.30179 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f9d18d4-ca93-37fe-886e-c5cd1717130b | -11.28664 | -45.20876 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47e66141-b553-3979-b52e-bb1599f35969 | -13.17178 | -54.34947 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 212acb04-cb09-37c0-90ab-f6e48cba07dd | -13.25701 | -42.25158 | 2026-10-09 04:27:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 1409a7ff-d5f2-3efe-847a-d8336487f175 | -8.79264 | -47.26492 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac47ba7e-71c1-35bc-9d34-9da8ccb80568 | -7.41196 | -44.75499 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ce1b8749-14ba-3e99-8129-5dc2c42e4b9d | -13.59501 | -48.58065 | 2026-10-09 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f10390fe-24d7-38e9-b4f6-040241c56256 | -6.72736 | -48.11963 | 2026-10-09 04:27:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 147c859b-a9a9-30d9-a2a0-faf5f9b68d63 | -6.48529 | -55.29149 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8269642-8913-308e-a3a9-15873a4d78f7 | -10.42238 | -47.28762 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27e27cb0-04e3-3610-b739-3a10b70f618f | -9.20958 | -57.72312 | 2026-10-09 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92815919-c862-329d-b705-73a54eb1de03 | -10.28384 | -47.82636 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ad25230-c971-34a8-a77f-1198a17094be | -8.75144 | -46.85367 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b533e755-eb77-33cd-bffe-b1ab20289669 | -6.1722 | -52.85545 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aec7be97-2307-39db-b963-f4390d136058 | -10.46263 | -47.85902 | 2026-10-09 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 146aab49-875a-3e10-ad09-5dcec61ef157 | -12.0105 | -43.47989 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb1e0b0e-de0c-3100-bc99-912b5db4537a | -8.99574 | -45.91325 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 439693c9-5c20-30a2-abe6-018f72854cee | -8.96937 | -45.1474 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9c9bb6a-bc8c-3956-95a5-8546d3a70c7d | -7.34393 | -45.31211 | 2026-10-09 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c37f4e77-8563-316f-8c35-0e0cf1eae300 | -7.69617 | -44.75491 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d72e6299-b05a-3e26-a4d5-15bfdf38aa25 | -7.41139 | -44.75872 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2cf3d8e5-67c0-3b87-9b06-f425bf782e26 | -6.12862 | -53.05685 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 38153711-7672-33bd-a82d-7e1ed671244d | -13.38055 | -41.3332 | 2026-10-09 04:27:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7ace529-0048-3053-be95-cae1f2638bc5 | -11.6917 | -43.65731 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c897a93-6350-32ed-b705-f223c937cb08 | -11.85195 | -43.59184 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2bbe96e-0a11-35cc-a001-74c501e55137 | -11.05792 | -44.03717 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 340470b4-0ea6-39b6-8855-1d94fe89ab3c | -8.95805 | -45.17613 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a92fa2ae-1604-30c8-bf22-32af5a85592a | -8.55628 | -46.90806 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 891b05b3-605a-330c-920c-2414d854759b | -12.29787 | -47.05875 | 2026-10-09 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f49d82c-1479-356f-a4a6-902f07fdc405 | -7.50384 | -54.99871 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72bcac23-2030-3b63-8593-230505382056 | -12.20774 | -57.13959 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ee2d568-7deb-3072-8956-ab8a370f2555 | -7.26636 | -45.34782 | 2026-10-09 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7516ff31-174c-365d-a36f-e25757f422fc | -11.61341 | -43.60945 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fdebc77-d8e4-3915-b7b2-43fff9b1379b | -11.83883 | -43.60154 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d20069be-3ef8-3b36-82d0-b9ee08f445d7 | -6.49591 | -55.29951 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4cad5b7-0388-3c71-9944-083351f3f696 | -5.81122 | -53.42318 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fb376f4-2afa-3a71-bb09-c73bc7adeb17 | -9.87061 | -50.4917 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e39de22b-6115-382a-ab69-d175bb818844 | -8.74605 | -45.1402 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20b67014-3f91-3678-ad2e-db8a1d00ae8e | -9.28377 | -47.43293 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8aacdef0-f2cd-3b4a-be86-6d96acf508a6 | -11.01416 | -45.42059 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5a24a44a-367c-376a-a255-5cee72035c74 | -7.79747 | -44.57372 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ba32e9c-5c67-35d1-905f-e664c75659f8 | -9.30142 | -47.47137 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 74c82cb3-ed16-36dd-a371-e2565532f160 | -6.386 | -55.27064 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 520d6a6c-e6cb-3f45-926a-e91ca3216b60 | -6.48962 | -55.30485 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 874792d0-8ef5-371e-a620-45270723fd7e | -13.16236 | -54.35217 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2335fc9e-334b-3086-a5d7-e7e15fbd5f0b | -12.00559 | -43.45899 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ec2df00-4a99-3556-9e33-0cb1b95c8b98 | -8.73248 | -45.1609 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5637fdb-e451-31a0-90b4-51ce95a993a6 | -11.7485 | -61.06569 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ca612dd3-12c0-3d2f-b558-565717fc3ca7 | -11.50774 | -49.89825 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7bd0ec1-d9de-3428-aca4-57f301d40419 | -11.38984 | -55.09344 | 2026-10-09 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04e29fb2-e3b2-3397-9b92-f58622b35eee | -11.85594 | -43.58969 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d0ec926-ffb9-3a5e-aa7c-c08775c4b65a | -7.51709 | -47.32817 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4669f5ff-6793-3c4a-8347-55ae63bff707 | -12.20899 | -57.13295 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee0a4d40-d553-3bf7-a5d9-9e675ed0d5de | -6.48991 | -55.29565 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b55c9eaf-a8ec-3437-ab5a-3038f3982a71 | -11.06933 | -44.08775 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README98.md)
