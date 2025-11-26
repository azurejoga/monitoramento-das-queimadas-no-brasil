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
| 72449327-8b90-3d8a-bb47-d50319b50667 | -2.64489 | -45.49806 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 86a38166-da27-3bd0-8b8d-56afb2979ce2 | -2.94065 | -48.23114 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0fdafeeb-531e-3d3a-8059-783aa1d5fe2f | -3.33007 | -49.72496 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 28605046-4418-3053-a4e7-477ed79cf256 | -2.64613 | -45.50698 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3568be0e-8403-3cbf-a395-089806a0978d | -2.99124 | -49.55117 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| ef61e66f-b875-3f98-82cc-d7bfd729134b | -4.45721 | -45.4099 | 2025-11-26 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f9f178de-2449-3775-b52a-c72e40ba2f71 | -3.17815 | -45.08681 | 2025-11-26 00:13:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1aad3a14-e24e-363f-813a-d1b8cd915175 | -4.53348 | -45.55513 | 2025-11-26 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7107352c-6035-396e-a560-1edc454f6873 | -3.33825 | -44.05948 | 2025-11-26 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de90d2d7-ab59-3bf3-9d40-10e1e048c847 | -2.83131 | -49.1271 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ab015af-d594-345d-b34e-7c339c466688 | -4.12816 | -42.91851 | 2025-11-26 00:13:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f37d64d1-c231-3d2e-ac88-5ac37af75095 | -2.71083 | -45.69991 | 2025-11-26 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab1008ce-f9b2-3677-a236-ecf3305ae470 | -3.91401 | -47.75538 | 2025-11-26 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 16437fd4-e429-3e0a-8628-4017d9f3ab0f | -3.70302 | -45.88575 | 2025-11-26 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b5ec45fb-caa1-3581-a969-8e8fd9219120 | -3.74664 | -44.54224 | 2025-11-26 00:13:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7237cd21-49ac-3a73-a321-e9b1d1861021 | -3.50053 | -43.69757 | 2025-11-26 00:13:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f7d3944-9bf3-347e-a75b-b8feb1eb8659 | -3.76494 | -47.13428 | 2025-11-26 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4508310a-095f-37e6-9123-b2f7df7d44cb | -2.72664 | -45.21835 | 2025-11-26 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d624ab0d-a517-3f6c-b8be-8587563ac5f1 | -3.13412 | -49.4005 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 5f129ba6-1c3c-3488-9150-f416334b8366 | -6.99708 | -43.15714 | 2025-11-26 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 04d63af0-c1df-3c25-9ae3-90e3e300a3ab | -4.36476 | -48.29727 | 2025-11-26 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 83394f3a-828f-39c0-ac1b-4d98c120f417 | -4.41648 | -42.91988 | 2025-11-26 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 594c8d1e-9048-3d82-8971-af8b05dc4f71 | -4.35395 | -43.62751 | 2025-11-26 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 756f2be9-b6e6-31a9-8258-c5e4abc2bbcf | -8.17224 | -43.19755 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| be069142-ef46-329f-b337-5707c902049f | -6.06226 | -43.26311 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f85eb12a-8203-3c0a-ad41-0eeed59c3052 | -4.19023 | -43.70425 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 72a74480-6ff8-3b5d-8f27-64013b2794c3 | -3.66653 | -43.56731 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| a3e8ed85-d079-38fa-ac18-2ba39b7be89c | -2.90962 | -45.47871 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 849a40d1-007f-3926-ad22-18683007d973 | -6.16184 | -41.83101 | 2025-11-26 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 76b4d8cf-497a-3a93-bd4c-aa608268ad67 | -5.70643 | -47.05658 | 2025-11-26 00:13:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9ed5f830-0c55-390e-b53e-ad223cb7c73a | -4.21493 | -45.52542 | 2025-11-26 00:13:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2f2fc184-b2c8-3a81-b28d-b2bfe1ada88b | -3.1704 | -50.60361 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b54d8af0-b8b6-3fc3-b094-0ee3b3f52d5e | -2.94435 | -49.35689 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e93153ce-c802-38fd-8744-a8c2842275bd | -2.42924 | -45.46789 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d4fab91-a155-3cc2-a39e-6217b11f31c9 | -4.53384 | -46.63107 | 2025-11-26 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 50696474-2ba1-3cd5-a573-df5fdf86acab | -4.21616 | -45.53426 | 2025-11-26 00:13:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 08ff7b5a-0b1c-38a2-b2e5-1b444aa1f95d | -3.91131 | -45.78454 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7acf98b1-849b-398f-9a82-336062dd9431 | -4.22957 | -40.39159 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| e5cdb406-23c7-3899-84b2-37f0eec56ed6 | -3.33173 | -49.71804 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f9cddbd9-be1f-31a0-aee1-af81bfc20f22 | -3.3673 | -46.25311 | 2025-11-26 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ea8ac6da-5a08-3813-bb6e-3a55f468aee2 | -3.21153 | -50.21822 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| ea6f373b-ab7b-3e2a-b581-91a340ad46b9 | -3.47112 | -43.41602 | 2025-11-26 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9bb56269-3808-3497-a8e5-bebd9b1b4c0b | -4.24717 | -48.57089 | 2025-11-26 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 35c957dd-cde0-3af2-b04c-78d799119915 | -3.96345 | -47.03878 | 2025-11-26 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 8222e8fe-3f74-3cbf-8205-430c12b9c133 | -3.39273 | -42.70792 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3d67b8a9-4af2-3ae3-8eab-4e460a2eb64f | -4.2527 | -45.13361 | 2025-11-26 00:13:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c158e772-a112-371b-8d63-0c95abca170e | -2.156 | -46.09042 | 2025-11-26 00:13:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5a2e9c68-adea-3347-adbc-02736c04737e | -2.85182 | -45.25869 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5f8baede-e507-3621-87e7-279f31fb0bed | -4.09969 | -49.06147 | 2025-11-26 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 1efd5ad7-580f-34ac-a4bb-f35751682931 | -7.52116 | -43.86552 | 2025-11-26 00:13:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce13c505-1a31-3322-9603-425fde73e0fa | -4.54021 | -44.55036 | 2025-11-26 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b2edac87-f0ec-3cf4-bd66-4e94d6bfd91a | -5.89059 | -46.45154 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 141d2f0e-42a4-34eb-b6c4-b4eb1a10ea9c | -3.69724 | -47.65157 | 2025-11-26 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c466dacd-b010-3805-af9a-6bff604201eb | -8.17084 | -43.18781 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 852bde62-44b2-360e-baef-db3770849354 | -6.07022 | -43.25165 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d57f2e33-f038-32a2-95c8-7b68714ae0d1 | -4.56187 | -43.28589 | 2025-11-26 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0562a93a-937c-3c73-8490-e764e754fe59 | -2.4782 | -45.41812 | 2025-11-26 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 9dbc4293-a0d9-3e55-ae47-e16264aa0249 | -6.58196 | -47.90474 | 2025-11-26 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 552dedcb-d08a-3dff-bf18-591d7e8ea5d6 | -3.08522 | -45.35071 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 76426725-8693-3895-b136-a4b3c0c6d905 | -4.96959 | -50.8665 | 2025-11-26 00:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 8ea4b34b-77a7-3984-befc-bf413ba35a28 | -2.92996 | -48.22256 | 2025-11-26 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 235.4 |
| 3e37e108-3aa0-3917-9460-b8231cc356b2 | -8.20394 | -43.02173 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d0bd82b4-2aa2-3732-8450-c13989120991 | -4.13955 | -42.92816 | 2025-11-26 00:13:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3bf37dd6-e476-3f16-8d51-2b8d83f9b986 | -4.14776 | -42.54951 | 2025-11-26 00:13:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 4705801e-17f3-3ac7-aaf2-54347f2b84f6 | -4.66705 | -48.8786 | 2025-11-26 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6883bb7f-9877-3800-94dc-881736c6b226 | -4.74692 | -46.50123 | 2025-11-26 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd5b881e-e8dd-3b7d-a9cb-96a8fa062917 | -4.27233 | -45.13366 | 2025-11-26 00:13:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7ff204b0-3f6b-30ea-9f64-d45dc8e9fe72 | -4.59486 | -44.41347 | 2025-11-26 00:13:00 | TERRA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 720f7b35-c951-31e0-914d-4d4aa9497b4b | -2.428 | -45.45895 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2c078f59-f3ae-3e35-85d6-93f46baf0219 | -2.65502 | -45.50571 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35063d1d-0a8d-34e0-a6ba-d98263ed065d | -3.43472 | -50.18899 | 2025-11-26 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 19412f2c-440f-3589-9f82-07f4fe67b4bf | -6.0608 | -43.25299 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 4f0af239-5f13-3a60-8ab3-4567156221b1 | -6.30399 | -43.79593 | 2025-11-26 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| f0e9f910-0da4-3b4c-beb9-ba5c08e54300 | -5.57214 | -46.27618 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07af4d9a-ce59-3f28-91e7-32784c2d7f53 | -3.70546 | -45.90335 | 2025-11-26 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 40d84e28-60c9-3654-923f-a67b5f36d8f2 | -2.91061 | -45.28105 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 62a9621f-1b45-31ab-9ed2-ef774bb3c23a | -6.0828 | -47.04753 | 2025-11-26 00:13:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7e48acd5-9bf6-304c-8e90-5496a2341c9c | -4.73803 | -46.50248 | 2025-11-26 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cbd44cf4-873e-3565-becc-ab44d3a91607 | -3.92835 | -46.18276 | 2025-11-26 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec93e371-9f3b-3b03-aec9-4f61165244b4 | -5.71663 | -47.26765 | 2025-11-26 00:13:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d696bc1-b46b-372f-b962-1e985111b2ab | -2.8215 | -49.1285 | 2025-11-26 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2760a100-22ba-3a87-a5e3-a2dd2a6f958d | -6.51531 | -38.81293 | 2025-11-26 00:13:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 286bdfea-1450-34db-b23d-93621555a489 | -4.16495 | -43.72829 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 329.8 |
| c4e40a30-0601-3cac-87ed-2bb0b4efbf19 | -3.22159 | -50.56804 | 2025-11-26 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b8690d61-1229-3aac-8f08-2496fd8b6b8c | -2.72538 | -45.20931 | 2025-11-26 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| c4baaeaf-bfb0-3708-a60c-963914a4fe22 | -3.96278 | -49.03492 | 2025-11-26 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 50720f8f-f25f-3e3e-8e3e-3fe179cef752 | -4.72114 | -46.45609 | 2025-11-26 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 3a2f11fd-f50a-3b68-8c3a-047900b62866 | -5.88935 | -46.44252 | 2025-11-26 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5de2b2f4-8821-3011-9098-cedd77f748ae | -4.16351 | -43.71828 | 2025-11-26 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 250.3 |
| f8faa005-0b96-3550-9bd6-dac01269a207 | -3.31049 | -44.38491 | 2025-11-26 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 334521bf-6ce5-3a4a-b1d4-c9cdc27fd537 | -3.03494 | -45.11934 | 2025-11-26 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2ba1225b-e4d8-3b8f-8b24-f14a3251bd05 | -8.03954 | -43.11303 | 2025-11-26 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| 9fab242e-e97e-3186-b511-b559a4b3fae1 | -6.57566 | -47.89022 | 2025-11-26 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6be0bd26-b47b-3f66-bc09-1e7701b887d4 | -3.17952 | -48.03028 | 2025-11-26 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 11600967-ab1e-3b52-a392-4fd087110caf | -2.8802 | -51.79409 | 2025-11-26 00:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0378a20a-e5e5-35b6-a991-0c4dc34fc436 | -3.73285 | -45.97122 | 2025-11-26 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8db5f569-b89c-3bef-890b-81013481c323 | -2.89696 | -49.53402 | 2025-11-26 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c8c84e47-28ed-3f5f-a942-123161970454 | -3.70424 | -45.89455 | 2025-11-26 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 72ef661e-6dac-3d9e-be01-f63579a69a78 | -2.78698 | -45.52044 | 2025-11-26 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4b07ab9b-a8d5-303b-9bb3-5aa5cf5468c9 | -2.8429 | -45.25995 | 2025-11-26 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README4.md)
