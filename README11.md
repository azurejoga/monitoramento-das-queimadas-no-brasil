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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a3b4481-9e7d-3197-9d60-74017dd04e99 | -17.75276 | -42.89617 | 2025-07-14 04:32:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6d7ee9b-d418-39e9-8e34-ba1d7c643bf4 | -16.72842 | -51.76345 | 2025-07-14 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5aaedebc-71ca-3a6a-9cc7-5ffe347f7f73 | -21.49154 | -54.27153 | 2025-07-14 04:32:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 82dac12c-c9b4-370b-8852-3ca69d7ce3f4 | -21.48771 | -54.27077 | 2025-07-14 04:32:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 59fd19e2-8ec5-3866-b453-10731f3c1398 | -19.88993 | -42.60974 | 2025-07-14 04:32:00 | NPP-375D | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4c6d7550-1028-35d6-9961-25b277353e73 | -17.22875 | -49.56049 | 2025-07-14 04:32:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a9a32e0-5d29-3d3c-b109-06e4e0d4da32 | -28.128 | -54.94255 | 2025-07-14 04:34:00 | NPP-375D | ROQUE GONZALES | RIO GRANDE DO SUL | Brasil | 4316303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4f0fa25-58df-36c0-933f-45d5065acd09 | -25.19061 | -49.3264 | 2025-07-14 04:34:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b719708d-6dbf-34cb-9b95-1a8cda99b65e | -27.21335 | -50.6675 | 2025-07-14 04:34:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 76d7cded-7ef4-3d4e-b593-7dd6d1c4fefb | -28.47575 | -49.03065 | 2025-07-14 04:34:00 | NPP-375D | TUBARÃO | SANTA CATARINA | Brasil | 4218707 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d2cab909-77aa-3f38-8d9f-5fe14ce043e1 | -8.5022 | -43.3085 | 2025-07-14 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 55d7ea44-cab6-3135-8156-bebfd8536569 | -8.5211 | -43.3063 | 2025-07-14 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8787c362-c750-3fda-b38c-648a29bb25c8 | -5.41566 | -47.57006 | 2025-07-14 04:49:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64479bca-5e23-3da7-b3fc-29f3866d746d | -7.0434 | -44.37579 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a672a81-d94c-372c-9671-cfa066546d80 | -7.58087 | -44.72919 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fa6e568-9dc4-3bfb-bd31-24fcd6785d15 | -6.83833 | -42.77243 | 2025-07-14 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2dc2b848-befa-397b-a353-5962624e1db9 | -6.46437 | -45.36197 | 2025-07-14 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4da8d640-c546-3565-b029-b11793a6a139 | -4.30526 | -48.10205 | 2025-07-14 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 401c6369-13e5-35a8-9974-fa504a0ddc60 | -7.58131 | -44.73112 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9dfecc34-f4f6-3ed1-b9b4-fa2bcced12ea | -7.5863 | -44.727 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bdb999c-2887-3667-b0d6-b285a686f35d | -4.86634 | -43.2235 | 2025-07-14 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba7f8e85-060f-3080-b8e9-40b313b6bff0 | -4.00776 | -49.47071 | 2025-07-14 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52bf44da-c1a7-372c-9a06-688789ecf8f6 | -3.78677 | -47.0864 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1052d5dd-6fa5-36db-8569-c4711b9e9f3f | -7.27329 | -45.30472 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d50308d-231f-38fb-a025-74894d4d1005 | -5.62563 | -44.35904 | 2025-07-14 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6bd68f2-ef78-3fb5-8c7a-89bdd65250d5 | -3.58595 | -47.52504 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2773af50-9d3d-36a6-9689-74c24de22ad5 | -3.58203 | -47.52447 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a1fed521-2d0b-342b-8fb6-3ae290a4af64 | -8.24693 | -41.93521 | 2025-07-14 04:49:00 | NOAA-20 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b40cdc7-fe3f-3e79-a40c-e72ff68df72a | -7.03026 | -44.35768 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0718dc74-fc66-3fef-8336-b19c6160c749 | -6.26181 | -43.36757 | 2025-07-14 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afedce4f-12ad-3e7b-a10c-adfa63b8a721 | -7.58127 | -44.72621 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e446de9c-d629-3455-aa58-c902447f151b | -6.46838 | -45.36772 | 2025-07-14 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d9fadec-fe3c-3f5a-ba91-7c8d7bd4363a | -7.26317 | -45.31237 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f6df40cc-0c59-3915-af76-58dc569204dd | -7.02128 | -44.38482 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a8d28fa-c97f-3d29-bea7-efe94e2a7a6c | -7.33591 | -45.31369 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47059e9c-03d6-3b66-894b-ddbc2dacfe7f | -6.43338 | -45.34164 | 2025-07-14 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5e44481-4a10-3dc2-ba6a-1f3358b8f6e5 | -7.02476 | -44.35969 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d4eb280-07d0-324b-b002-1aeccf8e79f6 | -6.2558 | -43.35826 | 2025-07-14 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66c5cccb-9b35-3b41-b580-023c4ac55bb1 | -7.35555 | -44.62877 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20a780ef-ba7a-3865-a92c-68be03bf1e1e | -7.26704 | -45.31453 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5a447f9d-6725-3c14-b075-bc5969b9c595 | -7.27279 | -45.31376 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eda62f06-8616-34ad-a80b-c90b75e40053 | -3.58672 | -47.52008 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1097211d-a752-3e10-b46c-0fd09d77aded | -2.58654 | -51.92102 | 2025-07-14 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81b8259c-048d-30c8-84a4-fedefafed651 | -7.05877 | -43.95786 | 2025-07-14 04:49:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42acb26e-9ab2-3c4b-9856-e4adaef5b44f | -7.03825 | -44.37529 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66b95ea1-b6a0-3491-894b-c28256b1ef74 | -4.5105 | -38.55257 | 2025-07-14 04:49:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5ac73fdd-7a9e-3e1b-baf1-9aa9d93a1756 | -6.43808 | -45.34262 | 2025-07-14 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1550d35-5dc8-34b5-9d77-17e1dcbb2057 | -7.58048 | -44.73206 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55ad8859-8fad-37d7-bcd6-25d47fc36ab7 | -3.5828 | -47.51949 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 880e49fe-b949-3411-9ebd-db6dc268f999 | -6.27287 | -43.40779 | 2025-07-14 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 616207bf-6c37-3b25-a476-06db1536bbfe | -7.0452 | -44.3255 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7afe66a2-fe09-3d18-ad07-74731d0dbfbe | -7.58671 | -44.72396 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca41af25-634e-3a5e-b0c9-d0791a34b961 | -6.83886 | -42.7686 | 2025-07-14 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 39497dfa-d29c-3040-a8ca-dddf15a0b7f7 | -4.86633 | -45.3161 | 2025-07-14 04:49:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dba719d-7414-3e59-b6f1-6bda71cfa982 | -6.12026 | -44.2272 | 2025-07-14 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28a00076-f98b-3b0e-bae7-989b26c85c85 | -5.27005 | -45.12769 | 2025-07-14 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a48c3604-8b19-300d-aae8-7a96e56f4030 | -6.2573 | -43.3601 | 2025-07-14 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 495ef226-a444-37e0-95c6-d0d872e56362 | -7.26722 | -45.31836 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29129839-bc6c-345d-b9f2-66740cb59d40 | -2.29383 | -48.57289 | 2025-07-14 04:49:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb90c77c-9994-3c83-a566-9a1b5200e325 | -4.584 | -47.26432 | 2025-07-14 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0941888-9088-3dd4-bfec-930fe103f300 | -3.97906 | -48.41504 | 2025-07-14 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e50a3c0-7b9b-3d91-a39c-d40aaf8aa0f8 | -6.46366 | -45.36694 | 2025-07-14 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd30a3df-5408-33e9-a747-b277e54afa58 | -8.24754 | -41.93065 | 2025-07-14 04:49:00 | NOAA-20 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00cb656f-9e1f-314c-91d7-7e252f20c256 | -4.30456 | -48.10675 | 2025-07-14 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8ea75706-8037-313e-9e21-6e63e9f3b551 | -6.27237 | -43.41137 | 2025-07-14 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f22d5318-b054-3c92-bc47-54d4a0e8b7eb | -7.26698 | -43.49779 | 2025-07-14 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8938dace-bc6a-3ddc-ae77-38cf8d28dd16 | -7.02518 | -44.35664 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52b36ce7-2e5d-3b1c-beb9-79bca6cc11a0 | -5.27111 | -45.13042 | 2025-07-14 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3046e44-05e2-3f30-aff8-6c0452a42257 | -4.24697 | -46.63244 | 2025-07-14 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e47ca18-7f89-305b-b493-51807fcac582 | -2.2902 | -48.57233 | 2025-07-14 04:49:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ca8adc7-50c6-33cd-ae97-be2f06dc9bf9 | -3.58126 | -47.52943 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2365a18f-76f0-3cd3-a9be-badee6363956 | -3.58519 | -47.52996 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 21422bf3-e8d0-3b5f-aa69-900d63359dff | -7.03068 | -44.35465 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75f8e244-9440-3102-9a89-13f6355ab529 | -7.27202 | -45.31913 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 964d4668-4c54-39f5-a9a8-518e51e2128d | -3.9828 | -48.4156 | 2025-07-14 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2aace3d-911d-368c-9ee1-1b1cf04cf2cd | -7.58215 | -44.72522 | 2025-07-14 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f848065-9078-377a-b6b3-b820682cc559 | -6.74999 | -50.92703 | 2025-07-14 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23dd6510-7d24-3ec0-b0c4-e78f12c16160 | -6.75057 | -50.9233 | 2025-07-14 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db264e66-3984-390a-b0cc-d47c0668bd12 | -3.78676 | -47.08984 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d831652e-6bbc-3c68-b5fb-894ba3ab9ae8 | -6.26124 | -43.35889 | 2025-07-14 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35e0e464-0aab-38ec-aa60-8641e95bc7a5 | -3.57888 | -47.51889 | 2025-07-14 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9e5f926-6aaf-3663-b4cd-a508ee5e7051 | -6.45963 | -45.36129 | 2025-07-14 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08271ca9-7889-3e23-8ccd-3d7e628e7db1 | -6.14022 | -44.0886 | 2025-07-14 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95fae8aa-8e91-35e3-a9c3-85116117e0af | -6.14529 | -44.08989 | 2025-07-14 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50a52ad7-edbc-3886-b5ec-758c4365c334 | -4.25116 | -46.63313 | 2025-07-14 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 562d351b-fefa-3150-82cf-5d1b8909f397 | -5.27743 | -44.88185 | 2025-07-14 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63900a5d-23f1-341c-a4c4-b3f7bb8deb52 | -7.26798 | -45.31307 | 2025-07-14 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8795a67-7bc7-3a85-91f8-a1718c642f33 | -7.01579 | -44.38681 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba173c69-daab-3910-8f28-e7241eb1e4b9 | -6.84401 | -42.77327 | 2025-07-14 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8a9687c-d707-389c-84c1-581244a72229 | -5.44541 | -43.58944 | 2025-07-14 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ead9acbc-1b1a-33f8-addb-a2b24a5be100 | -6.70923 | -43.89371 | 2025-07-14 04:49:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07bd7ada-9240-3f1c-a2e5-735e18124ded | -6.68397 | -43.68827 | 2025-07-14 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7371e11-1259-31c3-9d12-1cfed3908de7 | -4.58347 | -47.26781 | 2025-07-14 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dfc6a0a-a896-3db8-a710-d9c23e873ee3 | -6.46767 | -45.37269 | 2025-07-14 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c53585ec-221e-3458-b095-550deb539b1d | -7.59894 | -46.26763 | 2025-07-14 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 256a6568-6fba-3eed-b3d0-d639a42328be | -4.53351 | -48.02409 | 2025-07-14 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50cbabbf-0514-328d-9630-cd7fa7a6d74f | -5.62522 | -44.36193 | 2025-07-14 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5445e972-a74e-381e-9186-122ad2ee3462 | -7.24565 | -46.97881 | 2025-07-14 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d998b28a-f657-3c06-92ff-631e5a3893d0 | -2.91395 | -48.2406 | 2025-07-14 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 75760bed-26fc-3365-9272-9bc6d8f4f5c4 | -7.02173 | -44.38155 | 2025-07-14 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README12.md)
