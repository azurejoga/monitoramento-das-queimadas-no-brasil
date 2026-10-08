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

## Dados Diários - Página 283

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c24d19e8-4f6b-3214-8106-e562b801ed9f | -7.21576 | -44.27847 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 08957f28-2ed7-325f-a60c-5fb3705bd38e | -6.81596 | -45.05317 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 91f3e7ce-405b-39ad-83c5-4dd91401fa12 | -5.77892 | -50.10339 | 2026-10-08 16:20:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9baeb57f-37a9-3f95-86b9-0690a825517d | -4.77619 | -42.67726 | 2026-10-08 16:20:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8118af98-a2d2-3c9e-8f1a-8c1802ccd165 | -3.29057 | -42.68476 | 2026-10-08 16:20:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3e9513ae-525e-322e-9ca7-492528f901d9 | -3.17602 | -50.4461 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c2e2beaa-6925-3d01-b763-9fba193f3e1e | -4.95243 | -42.73313 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6837d2b6-dcbc-352c-94ac-8a22f309c310 | -6.19823 | -52.87197 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ed35918c-8b80-3a23-acb4-d7f2e83bdc54 | -4.52288 | -44.0102 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3a259019-ab87-3716-8e64-a1fd0ddc8e5f | -8.21138 | -46.42307 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| e2812d66-6e0f-3db3-bf2e-9c871a1b52f2 | -5.51883 | -45.62832 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae335cd4-0b9c-309d-958a-7b0c612f5b51 | -5.38711 | -44.19318 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2e94fed9-6237-33ed-8a58-46a73d7d4ceb | -6.45219 | -52.70181 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 76f39c9d-6ef8-3ec7-9e53-372963d4624d | -2.0793 | -46.56862 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 562.0 |
| be686abc-5945-324f-ada4-565882a27353 | -6.82104 | -39.54449 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 20.6 |
| cdb5b4f4-0ba1-3a28-993f-3ecc3638d550 | -2.99098 | -43.28803 | 2026-10-08 16:20:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71a53b24-898d-31d0-9158-44b3a65e7139 | -5.45165 | -42.89011 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 54300346-1581-384b-852c-c599c9151cdb | -3.72623 | -38.65936 | 2026-10-08 16:20:00 | NPP-375 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d43db212-2523-3fbb-af90-3ac9995a377f | -5.74035 | -45.33986 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bc287a5e-25ba-3947-bad4-b0f2025aae09 | -5.74613 | -41.72538 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 431.5 |
| 4a634247-1e8f-3f79-ba64-0b177184ba1b | -5.78002 | -45.38398 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e60b3aab-fda6-36b3-a968-1af0cf50f684 | -5.69384 | -53.49483 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a381ef32-5709-39e4-acb1-637b9e8ccdbf | -4.35798 | -43.80042 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8320ffcc-bf9b-397a-afc0-928e7613b370 | -5.95798 | -40.93652 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| 4fad3350-ea25-3a29-a67b-535fe3fa9aa5 | -2.98673 | -43.28439 | 2026-10-08 16:20:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 5674444b-5319-34ab-8174-c91b3b57a532 | -8.37282 | -47.66289 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 580364d2-3ca0-31d1-835c-06ea38e604a2 | -6.38204 | -45.78802 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 84a3bedc-a8da-3c59-8f87-72cf8952010b | -3.08788 | -53.94362 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 10a5c5ff-085b-3fda-ab50-1bdf827bca89 | -4.89206 | -45.62915 | 2026-10-08 16:20:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b4831f0a-16d0-3dd5-adc4-aec6511d5723 | -6.92575 | -43.06953 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 06924200-eb99-3c83-a05b-639cd2b663cf | -3.78141 | -41.78452 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 68f8b563-6448-39f5-9917-2f617dda3367 | -6.85041 | -41.74174 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 08889517-e081-30d4-9aeb-a2bd865f0f19 | -4.57946 | -38.94805 | 2026-10-08 16:20:00 | NPP-375 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 95a14a12-c6be-3ba7-a750-24c522c0ad5f | -6.97071 | -43.89575 | 2026-10-08 16:20:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5b76ac0-82d2-31d2-9635-b13465836f58 | -5.95232 | -44.27081 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0f807195-c43c-356f-848c-ffc35613c708 | -3.1097 | -41.17091 | 2026-10-08 16:20:00 | NPP-375 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e663985e-e39f-3fb9-ad22-9056671128d3 | -3.17791 | -50.44972 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5a78b452-1b3d-3259-9b0d-f7d7ea81d0a1 | -3.9159 | -44.38825 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 89981b3e-1f59-31cd-bd48-3d09e21d6b6c | -6.23667 | -43.86086 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2f6e09bf-8c36-3282-9648-09197a6e71cc | -5.51387 | -45.62468 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bcb55b1c-e561-3b46-ad41-dfa93d300cb6 | -3.89882 | -41.5941 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e5e24396-61cb-3af7-8536-052325026099 | -6.16818 | -52.65472 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 879b1c50-7e5e-3332-94e0-8fdfd03cf53b | -6.46187 | -52.6492 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e53345a-e712-3f83-9d95-1495eb8ed421 | -2.07999 | -46.57203 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 480.7 |
| 7db28e85-c69a-346d-9b6e-d037ee4edbd2 | -3.94709 | -44.71395 | 2026-10-08 16:20:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5a87052c-dde9-3914-b6cb-f375b61d014a | -2.88093 | -45.75995 | 2026-10-08 16:20:00 | NPP-375 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 16e8b82f-edbe-3569-b1a3-0dfe75d6836d | -6.81922 | -38.54412 | 2026-10-08 16:20:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ec0772d0-6289-3dc8-8d48-5728d73afc6a | -3.97234 | -51.86885 | 2026-10-08 16:20:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 3a67eb8c-2f33-3df8-9cfb-d02d74842fdc | -6.16906 | -52.66109 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| bb221f6e-e2ca-33c9-a8ee-ecc3ae217cbf | -3.8538 | -44.12527 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 260a1d89-5c9e-33a1-8638-6dad4fb0dec7 | -6.59054 | -41.54555 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 65b91c38-f3a9-3457-9a8f-bb8508afa0a2 | -3.36747 | -42.91496 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| af8cd20b-6adb-35e0-9f6b-db705ffce7bd | -1.19841 | -48.92221 | 2026-10-08 16:20:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bd00dd9-6cd5-3179-a405-d770c7d67840 | -5.37848 | -44.18927 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0d07a1aa-b642-3d3b-82e6-1de10c26f44b | -6.93344 | -43.66152 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d53b90a6-e83e-3bcd-80d3-96235eed30ee | -6.06551 | -44.11001 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1bede63-db54-3636-af33-27ffa4f2b863 | -7.82245 | -44.57114 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b156c7de-db78-3ad2-83cf-74c7c7c78ef6 | -6.23762 | -43.73074 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8dbf957a-e894-3a03-abb4-ce4dcc6aca44 | -3.17204 | -50.45036 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9092944c-ff58-3f73-b927-9f34fb364e78 | -5.9837 | -41.36199 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 97724eb1-e764-39f2-954b-6c407b955154 | -5.53329 | -45.6054 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5df52de2-f8d4-3271-9a3d-fb2189af3aa8 | -2.98017 | -54.0775 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8b1c094f-9ad5-3d7f-a6d7-b64b31498298 | -4.31894 | -41.23259 | 2026-10-08 16:20:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 200a7c67-9cf9-3266-9868-60709e5003e7 | -4.14332 | -43.20074 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2dc9309d-41d1-31c0-b985-80e02c053135 | -7.8355 | -45.51188 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b2f6e9a2-ebcc-3a6b-a49d-012c10500d7c | -6.31591 | -35.1301 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 36.8 |
| 499a5d1d-bf63-31d9-b55c-74fdae6ac4bc | -5.34616 | -45.76587 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e87c4815-3ba1-36d2-af73-95511bae475c | -6.37301 | -42.90144 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2eb40a9c-d547-3c3c-95f0-ca7c62b3c623 | -2.83846 | -49.87654 | 2026-10-08 16:20:00 | NPP-375 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f3073f5a-7b49-340d-913e-0ce420dfa6a6 | -3.29328 | -53.69765 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 89973558-4601-366e-886d-e7dbfffa35b0 | -7.26313 | -45.34445 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| a6a43774-2cea-3204-870a-759d5c65270c | -5.7137 | -41.7224 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f5b10bbe-5d53-3d3b-b34d-3a67e6cdfdd9 | -7.59201 | -46.69402 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a37ba9f9-1fc2-35c9-b09b-8c584364cb1c | -2.82717 | -51.27922 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 3f859439-82f3-3a83-8a37-5919fe2deab6 | -6.95395 | -45.27471 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ce21899c-27f2-369a-bc52-a56d10237dcb | -5.38172 | -44.18373 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1b6a2d9f-10e0-3ba0-ac4c-251850ff0b8a | -6.13629 | -47.95253 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 067c1ebb-09f0-3cb7-a2f9-28301061c99e | -6.93873 | -43.6707 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| ad2d00b1-81b1-3116-b288-2b26a04103fe | -5.70675 | -53.48103 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 3feed1e5-d140-361d-a69e-ce4398e95a03 | -6.0723 | -44.38414 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3128d443-dec5-3889-b856-cf0e4816aec4 | -6.50129 | -42.03474 | 2026-10-08 16:20:00 | NPP-375 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 8dd38759-2f5b-3a16-98e6-889864c2d065 | -4.13966 | -43.20128 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e70893b9-8b67-327e-8659-6d5b761108e4 | -6.59909 | -37.8925 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 18d072b9-15ac-3f36-9c50-1d37da05fef8 | -6.97 | -43.89068 | 2026-10-08 16:20:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ad1931b3-42e2-3b17-853a-9847b3ca1c0c | -6.90513 | -45.89249 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4d0d66ff-d107-31f0-bc46-ef77bf1ac2a2 | -6.10039 | -47.65167 | 2026-10-08 16:20:00 | NPP-375 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0877ca5b-498d-30ee-9cf4-4a975700e1aa | -6.96191 | -47.67033 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0cd89ba6-c4fa-3332-94bd-d21f4390cfa1 | -5.24643 | -37.57563 | 2026-10-08 16:20:00 | NPP-375 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 5a3a90fd-407f-3e34-8e86-b65da86c22e3 | -6.40916 | -37.79652 | 2026-10-08 16:20:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| fe3f41a1-4912-385b-826f-354dc39b39cf | -6.31976 | -35.15382 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| fb8e5d61-3cd0-3b96-b1bb-cb32b06b6ed3 | -4.336 | -42.79406 | 2026-10-08 16:20:00 | NPP-375 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ab28ae0-1eb1-3dfb-962c-db60680fa560 | -3.85794 | -44.11301 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 4525177c-6005-331a-8ed9-483f70be8fab | -5.39894 | -45.91153 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| d38ffe72-e9ed-38f8-ac09-13654319d841 | -6.83959 | -45.12816 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cf7890a6-69e9-38bd-ab3e-7da37816ac0b | -2.99794 | -41.42886 | 2026-10-08 16:20:00 | NPP-375 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e9b071f1-b9f8-3df1-857d-103a7835fffc | -7.69763 | -44.75202 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 9da7822b-ea2e-3df0-9762-9d287cd88830 | -3.25987 | -54.03416 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| e04f92d6-1b8a-3be1-ace2-03142e84fce3 | -6.93019 | -43.07352 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 423f305b-2bab-327e-abe2-945f6c7a7907 | -3.00833 | -43.10763 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94a3ea78-e224-39ca-a47c-718b75097e12 | -4.43077 | -43.9057 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |


[Clique aqui para ver as próximas entradas](README284.md)
