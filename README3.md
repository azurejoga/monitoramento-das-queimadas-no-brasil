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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91bb1797-b03b-3135-9302-7a70a54d1bfc | -5.93099 | -43.33149 | 2026-01-13 03:29:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bef20872-c7b8-3a47-8f84-eb72c4155b87 | -3.55396 | -43.64565 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55efb8ea-7264-3bf2-ac43-58d8538a12f4 | -3.29748 | -42.53734 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 872452b1-a110-37b6-b726-bdaea019b497 | -3.28906 | -42.55008 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d8427bd8-4397-3df2-acf6-71931d05a72c | -3.29415 | -42.43653 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4fe0763-3956-318e-9650-3a957b649397 | -7.52953 | -37.0282 | 2026-01-13 03:29:00 | NOAA-21 | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b337bd4c-3b04-3baf-9403-7063fafd8899 | -6.4083 | -35.2154 | 2026-01-13 03:29:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4056041a-6e54-368c-ae42-f5831b551399 | -6.06366 | -43.25534 | 2026-01-13 03:29:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2b58bce2-0f6b-3e24-b5d6-267eaf5d3362 | -5.10502 | -39.46331 | 2026-01-13 03:29:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 28b51d3c-c758-32dc-8e50-355024a7d414 | -5.49484 | -42.1596 | 2026-01-13 03:29:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 66c21b1c-08c7-3bab-97d1-8e7846c1cf73 | -5.4955 | -42.1557 | 2026-01-13 03:29:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3564dafe-f6f5-3b66-bd12-7d84a7848880 | -4.41778 | -43.10142 | 2026-01-13 03:29:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8872496-1a95-3a32-99c5-895b43471272 | -3.29827 | -42.53277 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fd53f79b-2ebb-3b64-b59a-935232f261ed | -5.10184 | -43.2323 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| c89d3a52-77fe-3342-be19-7f211bc8269b | -5.93009 | -43.33339 | 2026-01-13 03:29:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9225bc66-39e4-33ab-b0d5-e3466f323d07 | -4.92236 | -43.42834 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdd8198d-d653-31e3-a243-d676d454e0c8 | -4.73884 | -40.82826 | 2026-01-13 03:29:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87c58c4c-be41-30fd-bf1a-2f481b1074d8 | -5.09735 | -43.22163 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 44a374a9-59c2-3100-b0d6-f8e7dce4a3ed | -5.92574 | -43.32579 | 2026-01-13 03:29:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bdf78a6-a8fc-3b9a-8a87-362f3aa350e1 | -5.42088 | -38.1664 | 2026-01-13 03:29:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| fbe1e4fe-6893-332f-9518-51d6d16f1ba3 | -3.29591 | -42.54647 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf776bee-dc9e-31c8-b036-c47c8dc1df93 | -5.09407 | -43.23876 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 14db9722-0103-306c-8eb6-a210a33c3c94 | -6.05754 | -43.25463 | 2026-01-13 03:29:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 39c93107-14ec-37dd-9950-be2db3294a31 | -5.09656 | -43.22622 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 0bb0882c-41dd-305c-8af0-60d35687888d | -3.55307 | -43.65082 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9951de14-dd24-37ae-92c6-8b9be3294cd1 | -7.42447 | -35.23846 | 2026-01-13 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| d895a7d5-5f25-3e8b-a0cb-a855b43bb592 | -5.49681 | -42.15919 | 2026-01-13 03:29:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e77cdb16-3fec-3e23-8350-12e389dbae2e | -5.1613 | -36.58916 | 2026-01-13 03:29:00 | NOAA-21 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 63aa9e22-3957-3b7a-b3d8-92c2551dee43 | -6.64807 | -35.10193 | 2026-01-13 03:29:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b8feeef6-b345-37ff-a9fa-8d399894f1c8 | -8.37233 | -35.39038 | 2026-01-13 03:29:00 | NOAA-21 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 63cbf134-fe49-3509-a08d-02363990ab7a | -6.80523 | -38.13808 | 2026-01-13 03:29:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9655cea4-03b2-34d1-b834-a9c47fff4e14 | -6.48191 | -42.94021 | 2026-01-13 03:29:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ee8a7bd-864a-31cf-8597-478115b00f76 | -5.10886 | -43.22681 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 8e9ef29a-557b-3cb0-93d5-51d19eb25427 | -5.10359 | -43.22097 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 78d260bc-9a71-35ee-9f87-576a63698e7a | -5.10276 | -43.22557 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 329a1bd5-842c-33d2-a492-1eb52b3d728b | -5.09496 | -43.23379 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 1dab1862-2677-3cec-8337-5e93299a1957 | -5.41691 | -38.16974 | 2026-01-13 03:29:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ff6bc223-0863-314e-aafb-b8c462d525dc | -3.28748 | -42.55175 | 2026-01-13 03:29:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b820a63-49ab-305c-a5e5-da304216649f | -5.101 | -43.23714 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9d77b2a7-fb3b-3572-bbb4-f68ddaa2ec64 | -7.42382 | -35.24252 | 2026-01-13 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 06f3d23b-59ae-3385-9a8b-34664356103a | -3.28823 | -42.5472 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ecb4ce63-6872-3ccd-a785-9283a2acf1d8 | -5.09667 | -43.22426 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| b06a3c13-5a02-3d9a-848c-91ca678f433b | -3.38876 | -42.11156 | 2026-01-13 03:29:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1aa4e937-dee7-3886-8a6b-2562ce18d261 | -5.10591 | -39.45816 | 2026-01-13 03:29:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 988bafb0-2a1a-3561-bbdd-b02ad29570c4 | -4.41696 | -43.10613 | 2026-01-13 03:29:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 06daaedb-ea2e-3c6e-9a7c-81b6c7ae5aa0 | -5.92481 | -43.32768 | 2026-01-13 03:29:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e684bdd-6022-39cc-8b2b-95ab31a1d778 | -7.57962 | -37.75334 | 2026-01-13 03:29:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ac7ff739-4ecf-3d08-b1f1-ebb39a10e4e4 | -5.10193 | -43.23021 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 19efc03b-95a5-3227-bf44-83bf06ddcddd | -5.41763 | -38.16556 | 2026-01-13 03:29:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5a4f400f-a435-3b18-9023-ca18752440e1 | -5.10265 | -43.22757 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 78b2e4f8-4a44-3b43-9f97-89c75c12510f | -5.10019 | -43.23989 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 162aba37-b134-3f42-baa5-fa560eb6b57c | -4.73968 | -40.82798 | 2026-01-13 03:29:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07e16276-ba57-3a3d-9efe-b3ebedafcb00 | -5.1107 | -39.45896 | 2026-01-13 03:29:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 6233f8bb-aadb-3692-9eb1-31397ab902e8 | -7.42433 | -35.23742 | 2026-01-13 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 47f1a0a0-798a-3449-9ff3-cd74b39243c1 | -5.1178 | -43.2431 | 2026-01-13 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| ecdc2664-c7eb-3508-926c-1d06cbe73c08 | -5.099 | -43.2444 | 2026-01-13 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| a31c9b4f-b079-3a89-9dd1-c2a5586b35cb | -5.118 | -43.2198 | 2026-01-13 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 44d7a17d-d384-3c58-a60b-c5fe1f9b8aa6 | -5.0992 | -43.2211 | 2026-01-13 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 228.3 |
| 65459fd9-e66d-3bbb-bebf-0d8010fa3fb0 | -9.10258 | -35.49747 | 2026-01-13 03:32:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 184e430f-1054-36e3-85a0-84484a5d58f1 | -9.65129 | -36.612 | 2026-01-13 03:32:00 | NOAA-21 | IGACI | ALAGOAS | Brasil | 2703106 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e8363a87-79e3-3739-88f1-f3c977d86d76 | -9.75978 | -36.52362 | 2026-01-13 03:32:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 06332680-8d51-3f29-8741-6a810e28a597 | -10.69789 | -38.14072 | 2026-01-13 03:32:00 | NOAA-21 | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d131352-0612-3522-bb68-db9638d151a4 | -9.38672 | -36.03814 | 2026-01-13 03:32:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7f207464-ca52-3cf0-a240-49f162e0dbf8 | -11.33016 | -37.86411 | 2026-01-13 03:32:00 | NOAA-21 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 858b9b99-35d2-3f1a-b544-3c6b50bd4a07 | -9.41287 | -35.94806 | 2026-01-13 03:32:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b28dc0b5-5bed-3b1a-b7d0-4ddb041e7e72 | -11.33058 | -37.86636 | 2026-01-13 03:32:00 | NOAA-21 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6cf5435e-0f85-3c72-bd96-740704160e23 | -8.51144 | -37.08268 | 2026-01-13 03:32:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 19f4e300-f9ba-3518-ab24-9d5e488da5dc | -8.05604 | -39.13985 | 2026-01-13 03:32:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2030c289-6f80-3aaa-988f-f3623524f61f | -21.85739 | -43.08096 | 2026-01-13 03:34:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f9062254-7cf6-38f3-8c16-3961ca4dc4b8 | -18.39867 | -39.92894 | 2026-01-13 03:34:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6311d7ba-0e56-38c1-8b78-2e08a1cb2825 | -21.38917 | -45.19559 | 2026-01-13 03:34:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0bc8842c-fab5-33ab-8dc0-f320deafbda1 | -17.89059 | -39.76704 | 2026-01-13 03:34:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c6d75cba-0871-32f3-acd3-743339fc9b44 | -16.02563 | -42.34863 | 2026-01-13 03:34:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ec7399a-8534-3aef-af0f-b81ffb0cef2f | -22.68204 | -43.72167 | 2026-01-13 03:36:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fe2ca22c-dd77-35eb-8fa8-c0f860f55305 | -22.67814 | -43.72322 | 2026-01-13 03:36:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e9de7563-6055-3ba2-b010-04f91737cfb2 | -22.67926 | -43.71769 | 2026-01-13 03:36:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5209e238-1323-3b90-992f-c1e9931f105d | -22.68038 | -43.71216 | 2026-01-13 03:36:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ea7bf97b-5768-3607-b809-0f25dcae5791 | -22.67737 | -43.72095 | 2026-01-13 03:36:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fe46fa0f-d05e-3c38-b0fc-eb9e4b59c368 | -5.099 | -43.2444 | 2026-01-13 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 4a672b0a-0e49-3af6-9e07-6cb5f7f2c44f | -5.0992 | -43.2211 | 2026-01-13 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 7095f52e-2113-332d-b5e2-29d3b5f9f109 | -5.118 | -43.2198 | 2026-01-13 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d3c401ea-4ce3-33df-be7e-8e9eebbf0cd9 | -5.099 | -43.2444 | 2026-01-13 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 772a3460-eeb7-3d91-95bd-04e2b404cde0 | -5.0992 | -43.2211 | 2026-01-13 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 268f0fd9-42c2-3847-8554-309befc5e7d3 | -9.10321 | -35.49725 | 2026-01-13 03:59:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34274114-cf0e-3c33-b144-6f3d6f9d4258 | -3.54301 | -43.66062 | 2026-01-13 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e31708c-3f3c-3b7c-a082-728751b77abb | -6.08507 | -37.31644 | 2026-01-13 03:59:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6bcb55df-078a-3fd3-92f4-f602cbbfe800 | -5.60883 | -39.3069 | 2026-01-13 03:59:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bfb21150-e45e-36f2-9181-73e61f387f2a | -7.57981 | -37.75233 | 2026-01-13 03:59:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f4de3ba5-2b58-3bbd-9af2-2e8026a0f01d | -4.95383 | -43.69637 | 2026-01-13 03:59:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e3bb894-4cf5-334b-b257-ac865e93ecf7 | -5.49859 | -42.15908 | 2026-01-13 03:59:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bc5e816f-9454-31bb-aafe-218b4689f7f3 | -2.96547 | -39.93011 | 2026-01-13 03:59:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8da20e63-8a8d-3601-9e8d-e06930c9cd06 | -4.90351 | -38.72007 | 2026-01-13 03:59:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d847259-13ad-37d8-90f9-1fe32c669601 | -3.89547 | -38.37904 | 2026-01-13 03:59:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9d4f093e-648f-30de-a291-98c9eb7f3491 | -2.01693 | -46.64869 | 2026-01-13 03:59:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3e57492-5c63-34d4-8ba4-972f16557661 | -3.1369 | -42.21158 | 2026-01-13 03:59:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7937d6f-e3d6-3af8-ad86-5816f27f6d45 | -6.21721 | -38.31297 | 2026-01-13 03:59:00 | NPP-375D | ÁGUA NOVA | RIO GRANDE DO NORTE | Brasil | 2400406 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 929ba88e-b42d-34e9-aac0-11154e376f1e | -4.73696 | -40.82657 | 2026-01-13 03:59:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21ebe402-0ea3-3745-840d-8d92956468b0 | -3.29091 | -42.54942 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9057e4e0-19ca-3238-82af-bb62294b361b | -5.104 | -43.22654 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 17c07ec4-55b9-3d35-845f-4e889d6da3dc | -5.41782 | -38.16505 | 2026-01-13 03:59:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |


[Clique aqui para ver as próximas entradas](README4.md)
