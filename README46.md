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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4294f2d2-910c-347b-b279-1dfed1573380 | -7.55393 | -61.33607 | 2026-09-28 05:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b7d11b8-90c4-3ca2-8459-e5b36aac5d41 | -2.9629 | -54.09488 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe1a7185-3acd-31c1-836a-1f820127b1ff | -3.03814 | -57.51049 | 2026-09-28 05:10:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09fd97a9-2876-344c-ac11-2841f9c44801 | -2.91047 | -54.12959 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 031d5982-367a-3c27-a756-8ee38414c456 | -5.89759 | -42.43425 | 2026-09-28 05:10:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a427520a-395c-35db-854f-c11b49f21a81 | -6.7086 | -45.60945 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 821a153c-4e40-3439-ab8f-22543b018881 | -3.69781 | -51.3732 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f861095b-35da-3e4b-bc36-18857a095f1f | -2.11722 | -56.8844 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58232be0-6033-3400-89c9-4f0933ea7db4 | -3.00579 | -54.21272 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92966eb5-8a44-3b87-9831-b4c2dc7d62d7 | -3.09973 | -59.93509 | 2026-09-28 05:10:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2c53ed5-865a-39b7-8f2d-cb0193f43782 | -8.43711 | -44.87415 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1228049e-4942-3c4d-b84b-e0391614c272 | -11.18525 | -44.79167 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 129b388e-c141-3678-b556-82555a8f3b08 | -1.81139 | -57.10318 | 2026-09-28 05:10:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6de208a6-8e36-39fe-9fef-3e1fbec966d2 | -2.99691 | -54.75177 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47af8fe5-404b-3601-85b0-7af9bc09c927 | -3.01248 | -54.21376 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a72e8e1b-e765-30b5-98a3-975dd3c21bad | -7.99081 | -44.82239 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 545c7320-f1f1-357c-8f26-6e07fe4d3c7f | -7.33682 | -42.07818 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df89a099-3c09-3291-b8c4-0482c820c882 | -6.71671 | -45.58897 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e0bdf7d-673e-395b-852a-28415b79839b | -7.26869 | -45.34255 | 2026-09-28 05:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfa2ab09-666f-3e30-95b1-de0445118aeb | -9.15101 | -45.63605 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b37bada2-8762-39fe-b440-7aa42ff8d385 | -7.51968 | -46.61298 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec5899cc-3b3e-3979-95bd-78a438e01f0e | -8.36145 | -45.44264 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc31e966-5e9a-3c43-be2c-1cbee23f8ed7 | -10.88477 | -43.68471 | 2026-09-28 05:10:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e368869-0fd5-3835-a8db-6360361de4c8 | -6.7016 | -45.61764 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d25260b1-9539-340e-980b-61b0cc35394f | -7.27693 | -55.57256 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f8c9255-4e09-3579-9d29-6ed9a9091bcd | -6.06528 | -57.82823 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dcb76ce-11e2-3d85-bc55-8c75c6552590 | -11.19486 | -44.80999 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9ac56a0c-d157-3804-a418-b05a64956f74 | -6.64639 | -59.94721 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3e8522c-ceae-3a89-9fa6-7c0140760d96 | -3.1985 | -51.033 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95691d71-1605-3526-afe1-35e7a409725e | -2.97569 | -54.14347 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25425881-53f7-3049-b2ad-d9d581f8d2af | -3.6984 | -51.3694 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65bf19a9-d0d7-3ca3-8e7a-b443e6a53122 | -8.22786 | -45.4804 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7381cce-5a7c-3782-8016-416389200975 | -8.03197 | -54.89776 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d16af25-fbf4-316b-866d-b6028a698ce5 | -5.72392 | -53.45676 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143d009e-1a2f-3a06-8878-d2a7030a4517 | -6.06903 | -57.82879 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c854039-c888-30fe-8473-fdc4e37109d8 | -3.01638 | -54.21078 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cfde5b4-3835-3ceb-b26f-09633527d3ea | -3.14628 | -54.09498 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3305ca1-0a5f-32f7-a1d1-8b009274f885 | -2.89764 | -54.08105 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47f412e3-70ae-330f-b9d5-511707dffa69 | -2.90768 | -54.12556 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c4b6ee3-b13c-301c-9224-af792f407256 | -2.78532 | -57.70237 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13643b6d-63a8-3837-a82e-2c1429c3f74e | -8.02976 | -54.89024 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6031072c-4afc-38d3-9f1d-a97bfefaf4be | -2.96234 | -54.09837 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 35a09d0c-9e99-3634-84aa-7eb1af400936 | -3.1524 | -54.09952 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8275325-6b89-3531-a01a-cbc3089812cf | -8.22513 | -45.44249 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e5866ce-afda-303e-8304-b6c340546c97 | -2.86758 | -54.11925 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51d988b0-73d2-38de-bb87-5f421878d0f1 | -10.12379 | -45.13918 | 2026-09-28 05:10:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43b0a6c9-8679-3ef3-af24-592ed436b8b0 | -2.97903 | -54.14399 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 842de4d4-339d-324a-9e71-6422c651104a | -10.88299 | -43.68569 | 2026-09-28 05:10:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ddaf6ca6-1089-3dbc-85c4-48e1bcb727f1 | -6.78205 | -59.38021 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cc767c2-bbc5-3e56-98c7-bfed38271743 | -6.63796 | -59.94563 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f086eed-c566-3184-a1de-67f929d175fc | -3.97166 | -48.00369 | 2026-09-28 05:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 563360ee-2459-393b-b76c-6f1287b4ec10 | -6.77397 | -46.68167 | 2026-09-28 05:10:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 357f9eda-dee3-3b21-979f-65e87dc99c86 | -2.89765 | -54.10251 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ca66590-3300-33c5-8e4a-20d43d436f92 | -9.17341 | -45.77876 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51453979-d05a-30d9-a07a-7f1e7f33d677 | -9.66557 | -48.90744 | 2026-09-28 05:10:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5eafd1ee-660f-37f8-a8b7-7f27820f6239 | -6.81883 | -46.1423 | 2026-09-28 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 303538d1-ab28-3429-a35e-032f1590cc10 | -2.85866 | -54.13218 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6795e906-5e92-3851-b8ef-47a0ede0b093 | -3.14237 | -54.07651 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09e0f8a7-13a9-3fb1-8c4d-af4b9284ae2c | -8.25554 | -54.79007 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51ab7152-7a66-383e-8421-8a419d30c81c | -3.01458 | -51.53576 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c709e83e-2fa6-39b5-937a-58c6c4c0884e | -8.0292 | -54.89373 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 788eb7ad-5679-33b9-8fd6-85d000bb6f84 | -4.97993 | -56.15015 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2ba1923-fb38-3bb6-ac14-68edafc88ca8 | -7.99204 | -44.82148 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d67d0e7-206a-314c-98e7-dfb2956d7a7e | -7.71439 | -54.76435 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 191c37a7-dc07-369b-9aca-ea14b69b67d0 | -6.77879 | -46.68235 | 2026-09-28 05:10:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e573ed4-726f-383f-9241-091cc5e4cb63 | -9.98018 | -50.14715 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7ce53d34-6781-3fec-bab9-5840e22bb5ca | -3.68281 | -47.49005 | 2026-09-28 05:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5f1a3c9-4c97-31a0-8b37-4046832c99b0 | -7.88329 | -45.4426 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ad8c1ba-516d-38fe-b7a1-3ba184f5e70c | -9.79246 | -44.8234 | 2026-09-28 05:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75e2c24d-26dd-364b-a854-8ae806ba2ec3 | -10.25594 | -44.61464 | 2026-09-28 05:10:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36002641-c656-367d-848b-e0338b036c4e | -10.71251 | -44.42868 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a07655e-51ce-39ab-b272-2730673bb80d | -4.84991 | -42.89029 | 2026-09-28 05:10:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6e4c17a-43b4-3974-a094-93fa8a9cdb1f | -5.1276 | -56.02402 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a02f8411-ebfd-388b-ab4d-8969244e3e5c | -6.05779 | -57.82706 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c118f11-4a8b-3f22-846d-a8a01cfe651c | -10.21784 | -49.9891 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a6cf7cf-0a1f-3f6b-8ca5-fe54e9d7afb6 | -8.28162 | -54.71198 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9bc01305-e08f-3948-a597-aecd13d4db4e | -10.20872 | -49.99504 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b729596b-cc40-33d1-9603-2b668cf5f858 | -10.26059 | -44.6164 | 2026-09-28 05:10:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b003108-41bf-3215-b78b-dd27cf31e2ae | -3.43163 | -50.33636 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99e5cdce-7794-312c-a0f1-88ef23d8c448 | -6.63904 | -59.946 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f814a0a7-6142-36ff-a0e5-8be9ae2c7b2b | -7.27914 | -55.58026 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b38efe1-b8ef-3d37-b4d7-0152038b4239 | -10.00871 | -50.11944 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95cc87df-e3d9-36b7-8de2-91303c243a85 | -3.0069 | -54.20571 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1396f75-fe9c-3624-b18f-838b4df51b11 | -2.79775 | -57.69944 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1d6b230-f363-3ba9-99b0-8ac77b3843ae | -8.1399 | -44.44714 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac59d947-efdc-37ff-afdc-d84fa318131c | -10.2158 | -50.00336 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4035fbe-9b9b-3fed-b899-ba0935d87451 | -6.99438 | -62.97184 | 2026-09-28 05:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c7cdce9-dfc2-33cf-96e2-e16101d7d571 | -8.59863 | -54.65185 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| badc8b21-43e7-3c8f-96d4-457509f16e34 | -8.23565 | -45.40641 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f80288f1-0ec3-36c4-8d4a-23a6a408205f | -2.92611 | -54.20378 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 869e4975-bee9-3903-bf72-e6401df4589c | -2.66074 | -51.74044 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39afd30c-8345-31b4-b5ec-91e7a51c3054 | -3.00093 | -50.47335 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99910b75-3fa4-3b99-b534-31234edfb960 | -6.14578 | -44.13469 | 2026-09-28 05:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47255525-3724-3bbd-96a3-cd07bd6cbc70 | -7.68445 | -54.85288 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66a73a10-3fbd-3774-b778-d4041ab46645 | -7.71716 | -54.76838 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc130bd3-84c6-3ca6-b10c-a15f46d6b329 | -3.44111 | -56.93243 | 2026-09-28 05:10:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26462601-41b1-3cf4-8eff-a8c50e72cee0 | -5.97493 | -57.69578 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b61f1f2f-c39c-3708-a662-29376bdc01a0 | -10.20569 | -49.98732 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aedfcca4-f418-36ac-8ba1-f348facf573f | -2.89709 | -54.08454 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3025accd-f69d-3600-abc3-908426875884 | -8.23251 | -45.44543 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README47.md)
