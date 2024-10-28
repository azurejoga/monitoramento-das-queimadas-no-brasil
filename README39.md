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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c77fe67-116c-310d-b34c-43f875fd73ba | -5.65803 | -43.41574 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd605f6d-6a2f-30cb-b264-66125cf1c372 | -5.65743 | -43.41949 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cd18242-96d7-3d9c-bead-2cdcb6a47c6f | -5.6546 | -43.41521 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8705d529-8667-3ef8-a1af-307ece610c3c | -5.65056 | -43.41842 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 103bcd03-8361-3ba8-a7e8-64174762c10f | -5.54135 | -43.70979 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9cebeb1-f543-3042-b3b5-d22b4304d519 | -5.54073 | -43.71365 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0841e3a4-7c34-358f-9a34-a11d0fc78615 | -5.53787 | -43.70922 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13137eef-a62a-36b2-8786-289996151147 | -5.45675 | -43.74749 | 2024-10-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27e6141d-559a-3532-9da6-57d0be08454c | -5.26404 | -43.99525 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e7a0982-09e0-3c33-a461-3787a51f0045 | -6.49044 | -44.16609 | 2024-10-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 608ae5ca-f044-3c25-b7c5-b2f74c8d415f | -6.40538 | -44.15293 | 2024-10-28 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55e5a0e2-823a-3ea9-a60d-30fe0452214d | -6.40059 | -44.16019 | 2024-10-28 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1772888d-7fe0-32ea-a79c-77a614fddd30 | -6.13097 | -44.30207 | 2024-10-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bafc281e-23de-3351-80bd-35458bbc1228 | -6.13029 | -44.30617 | 2024-10-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d6764290-7fc1-3309-aa85-97b8c12e7971 | -6.12741 | -44.30155 | 2024-10-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28d3d9ba-030d-3e8e-855e-5af049a9fd88 | -6.06804 | -44.08878 | 2024-10-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eec5c5d3-6f25-3337-bbdf-0cafba7167f8 | -5.97058 | -44.24193 | 2024-10-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8371a357-ebf3-312d-8047-3e07c5c1d5ff | -5.92661 | -44.01971 | 2024-10-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b18977bf-c630-3469-9462-cc691628ce18 | -5.815 | -44.1282 | 2024-10-28 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01d5fae6-01ec-3823-a925-11d6f10baa04 | -5.8146 | -44.13157 | 2024-10-28 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0b8d913-ccfd-3d31-820f-155ce8933e2a | -5.81437 | -44.13218 | 2024-10-28 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a15fa74-c8f5-3fa4-b489-609e52f82e08 | -5.81395 | -44.13555 | 2024-10-28 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f297614-eb36-311c-b90c-f00ca903fc84 | -5.81373 | -44.13618 | 2024-10-28 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1941b2e2-6601-33b5-8923-c2511d4a6d37 | -5.81041 | -44.13501 | 2024-10-28 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6a478ce-76f4-376f-988c-9aa1be8bb490 | -5.8102 | -44.13564 | 2024-10-28 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bacdcc61-fe03-30b8-ae59-75933715da82 | -5.26907 | -44.16351 | 2024-10-28 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7db5a499-ef89-375a-b4f9-1ea4a83a807e | -7.82087 | -45.39939 | 2024-10-28 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 556ce88e-003e-351f-829d-49486e83e529 | -7.82014 | -45.40377 | 2024-10-28 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09f95d9f-ba0a-3d2f-ae3f-97d4b2af8753 | -7.60997 | -45.2692 | 2024-10-28 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 982679c9-324e-3553-821f-69d5a398eb18 | -7.42865 | -44.79369 | 2024-10-28 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bd862f0-a440-35dc-ae73-c8ce59bf5c98 | -7.42441 | -44.79723 | 2024-10-28 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75e86747-940d-3e1b-8035-b92c0faf028e | -7.22893 | -44.9891 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ccaaed5-af62-30af-8630-14323448404f | -7.07175 | -44.80262 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71ef1f64-39e6-31dd-9dc5-500ca2e42e8e | -6.95127 | -44.87422 | 2024-10-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 057f2bfa-c8b9-3bdc-bc47-fb58f7159a71 | -6.94419 | -45.05495 | 2024-10-28 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c01dcfb-b4c3-3df3-b2fe-26085ee026c3 | -6.72347 | -44.68939 | 2024-10-28 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38503008-d6ca-3b01-9914-a8bd7e2d63b7 | -6.74126 | -44.00584 | 2024-10-28 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48fcea2a-2f79-3e32-b00d-fa53891934bb | -9.18642 | -45.21313 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0429d65-1d40-3c81-8f1a-78714daaf2ac | -9.18573 | -45.21732 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b1b621d-ae4d-323e-9794-09b4ec94353a | -9.18285 | -45.21249 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b707929-2bc1-39f7-b999-ca46fbec213d | -9.18217 | -45.21666 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 853d015d-f60e-30cb-9220-09b550eaf8f9 | -9.18148 | -45.22084 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90d65261-f8c0-3601-9593-83a7f2c63135 | -9.18077 | -45.22514 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52119bdd-b598-39b4-99b9-131b9870a932 | -9.17928 | -45.21187 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bdb6c85b-28be-33eb-9618-4ecca515db59 | -9.17859 | -45.21604 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc7d28fc-5477-3765-8f77-d28867b375c7 | -9.1779 | -45.22022 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| decd92e6-99a0-339c-a665-201fc45fb2bf | -9.11321 | -45.49841 | 2024-10-28 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59d99398-1eb1-3a96-9a89-4cd342e4b349 | -8.77164 | -44.71578 | 2024-10-28 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82a7effa-99d3-37bb-9ce7-dd68a9cb1c29 | -8.77032 | -44.72372 | 2024-10-28 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88a5bf94-539d-3aad-968f-22605b60bfeb | -8.76746 | -44.71917 | 2024-10-28 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10e4811c-d233-3879-9546-5f1a9cc213c4 | -8.7668 | -44.72314 | 2024-10-28 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16d72034-222a-3562-a49b-d32588006783 | -8.76614 | -44.72711 | 2024-10-28 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dfab98a-4e29-373e-8797-bbfd9b32c655 | -8.76168 | -44.7066 | 2024-10-28 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0711b006-59a9-3ccc-9073-7fa2df999909 | -8.75911 | -44.72252 | 2024-10-28 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 010a4097-0fb4-3686-ab94-6d69dee63b93 | -8.75624 | -44.71795 | 2024-10-28 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c21a02ee-9b87-3cfd-a638-b3aa5adc77f0 | -7.86942 | -45.40248 | 2024-10-28 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c1d0a55-6965-335d-99a2-e8125e5588ce | -7.86575 | -45.40187 | 2024-10-28 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11934e5c-e087-3aaa-a7bf-926e81d0704f | -9.44952 | -44.46504 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da061fd2-0d20-35eb-9a14-eae7b0187d47 | -9.44013 | -44.47924 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7bc5db-d5d8-3170-87d2-541d4791f6f9 | -9.4395 | -44.4831 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a37a28b7-b55e-3435-bf77-249a3f305564 | -9.43888 | -44.48695 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 908727e8-aa49-38a2-9abb-b7fe6ceb003e | -9.43826 | -44.49081 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 667f6944-b31d-3dd9-b5d7-364678fcd832 | -9.43667 | -44.47867 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67eb1471-e4c3-34a7-91a5-dbfaedc290b0 | -9.43605 | -44.48253 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48e3b866-f1ae-3a7b-a9f9-9aaf4bd13ed2 | -9.43542 | -44.48638 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c50cc21c-68f3-3352-b94f-9a1a49889fa9 | -9.4348 | -44.49023 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c041c18-1048-347f-a26a-1724d9107138 | -9.43446 | -44.47044 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01c53d20-7b59-311a-b413-81ac8d386a89 | -9.43383 | -44.47428 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78f53ccd-a48c-3cd9-b876-ab05e16f7243 | -9.43321 | -44.47812 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac0b9fc0-6dd7-37b0-bb1a-e55138f5c509 | -9.43259 | -44.48197 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a43761f8-373a-3820-bae4-b1061a55fe21 | -9.43196 | -44.48582 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| add5ae69-ddff-3bc6-8a52-a205c8a900d1 | -9.43162 | -44.46606 | 2024-10-28 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4f88843-e8f1-3f72-9e74-8227b4ba3d4f | -9.63854 | -45.10915 | 2024-10-28 04:06:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec7a2c34-c162-3bc9-9505-d76c9c9ab5ea | -10.45558 | -44.94477 | 2024-10-28 04:06:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5f48e4c-61bb-3958-b77a-0fcf2784358f | -10.09695 | -45.38182 | 2024-10-28 04:06:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e72d7c06-00c1-3ecc-bd2c-84899140808c | -10.09338 | -45.38119 | 2024-10-28 04:06:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80e6b1d3-b392-3287-b6f4-6bbefc619220 | -9.77789 | -44.63957 | 2024-10-28 04:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25b73174-ad0e-3773-8fc5-34310af4b81f | -5.02267 | -45.54486 | 2024-10-28 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0a92af1-cf21-3738-b5bd-4e979d4e5411 | -4.90184 | -45.89288 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cc5da46-1bd1-357f-898d-d314eaf6943b | -4.89474 | -45.96027 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a06662f-f657-38d8-936a-8d4075150e50 | -4.87308 | -45.84729 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4598d4d3-7b4a-3e4b-bb62-821317434f38 | -4.87296 | -45.85002 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08faa148-dd82-3a72-a40c-41af2063845e | -4.849 | -45.77421 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9145fd78-b871-3001-b1d3-b81a12748178 | -4.84223 | -44.9367 | 2024-10-28 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8605b3fd-e593-3e48-9fef-ae41d2ea3829 | -4.8385 | -44.93615 | 2024-10-28 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffd89905-e61f-300c-8549-7ca4a38cb95f | -4.80023 | -45.72779 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed948301-20d4-3852-b679-fa508f880ca8 | -4.80012 | -45.72978 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc9ad623-c9c7-31b9-9e3d-327d601d7fee | -4.79864 | -45.73777 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 148a8822-f096-3026-9c02-105983c32a1a | -4.79847 | -45.73972 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db4d7b4c-cd78-38e3-9a92-0340c85e5874 | -4.77128 | -45.92702 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 381b6885-8a5f-3852-a955-d4de4bf40789 | -4.75653 | -44.8891 | 2024-10-28 04:06:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b3ebbf9-5f76-3827-b5a3-4d3645fa20e1 | -4.72381 | -45.80273 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc8575fb-a46e-39f2-a090-e57a8a2ca95f | -4.71283 | -46.14634 | 2024-10-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7095a0fa-82c6-34a7-bfaf-8933dfaac967 | -4.70972 | -45.7903 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72e2c371-5a9f-3dea-a950-79f4cefd8556 | -4.70578 | -45.78976 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af68584-d65d-3262-9856-76f389e49899 | -4.70265 | -45.88241 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03fee260-54ee-32be-84e0-7e84745040fd | -4.6987 | -45.88174 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9656bf44-d06e-39cd-9cca-cf4e89263551 | -4.69785 | -45.88691 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 16a7e12e-e0ce-3fae-a544-380a9a7e068e | -4.69392 | -45.88617 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a1e33a3-ee02-3793-8753-53a5a3f76e8b | -4.69314 | -45.6246 | 2024-10-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README40.md)
