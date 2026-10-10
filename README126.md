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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b52775d-c961-3582-b7af-7f62452eb325 | -3.59892 | -59.42497 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec645a9b-767b-349c-adef-5840d75f589f | -2.74762 | -54.11074 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31f1913f-acf0-3bd6-9465-72835808bb59 | -3.25066 | -54.02391 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b8cb5f3-adc7-3e11-8224-75b380479b90 | -6.24104 | -53.30676 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40227ce6-09f5-3944-ba94-fd63d7db2ae2 | -5.6889 | -53.47186 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d59b2ec1-b51e-3057-bbb1-867830692d5b | -6.24049 | -53.31029 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 880f1920-8ada-3fbe-8f35-5ec8f4cd164b | -4.544 | -54.96955 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c66f58b2-9f3f-3dad-9f7a-a653d7f84175 | -3.85667 | -54.08127 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fd0e200-15da-3a4e-a845-ab594be540ce | -2.65724 | -54.31684 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f427461-9113-363b-ab47-3e661d2ca1f9 | -7.20862 | -44.35606 | 2026-10-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fd7263e-1bbd-3804-b3ea-b3ef4e32a34f | -2.99718 | -54.05843 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e084b12-0fad-37e0-b6d6-560984ba05c0 | -6.31434 | -55.33493 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccb18fbe-521c-3f85-ae0f-09c0dde51971 | -2.5716 | -57.68644 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 336c2c13-7663-39a1-be32-30d86d8e85a6 | -3.26426 | -54.68869 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 20fa355e-60bf-328c-bebf-e968eff74e36 | -6.49564 | -44.36828 | 2026-10-10 05:04:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbf47e61-fcdc-39bf-bd78-7948ee039107 | -2.98576 | -54.77092 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d619dd71-7e38-35b9-90bb-36469730e660 | -5.94606 | -55.34145 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5a85d5d-811f-3336-b359-e973e150c63d | -6.36858 | -55.16394 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46d1f0f3-a3a5-3490-92d1-8b3992b8399e | -6.45789 | -55.0529 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8cfc20f-aabe-328a-84bb-57b84374e962 | -6.04987 | -59.9169 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b8c5dc4-5953-3685-bf73-122a71cd3ad6 | -3.2424 | -54.03323 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 54f67c7e-6040-31ea-8b15-6fe11d0beb39 | -6.45704 | -55.48117 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 616cc395-db71-34b0-add4-3b83898ad013 | 0.00606 | -60.58355 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5a1792ac-36e1-38b6-9f48-4c0d19747de0 | -3.47525 | -54.72937 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2551ff59-6dcc-3dcb-9fc8-b0136c78df05 | -2.19424 | -46.83597 | 2026-10-10 05:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61d8e00f-11a8-3878-b17d-b0e38c5c5d38 | -6.99418 | -47.71985 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ff70325-f369-3b3c-b28f-5f9aa3703bf1 | -3.49068 | -54.20398 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4666ea3-6e89-314a-8bfa-37d67b751670 | -3.3085 | -54.70632 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 675298ea-1962-32b7-947c-d87f907f914d | -3.22523 | -53.97051 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f3385a9-0dfe-3116-8e6c-531496141c2a | -5.23549 | -45.37334 | 2026-10-10 05:04:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b811c55-4126-3cd1-9172-98d9f6650eac | -5.59137 | -47.28771 | 2026-10-10 05:04:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcd69ecd-b9c3-33d8-aecd-e3d45474d5e2 | -3.10142 | -50.31473 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5e46f33-6dad-3b73-b999-c30654ad4447 | -2.86061 | -59.11469 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e55d419-1ea9-3329-9cdd-6f760591b52c | -3.56077 | -54.70269 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78051ad5-526b-3150-ae6c-463a8d46b29e | -2.88857 | -54.16519 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aacc9dd-b16e-326a-8743-6f3208209572 | -5.7083 | -53.4784 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32311091-ae61-367c-8409-98192c3ccce4 | -5.04807 | -49.34663 | 2026-10-10 05:04:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bff6a1b3-740f-3699-99a9-3eaf398e0497 | -3.48029 | -50.0888 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e211fb7c-fc1a-367f-a55b-60f558fc4cf5 | -3.59856 | -54.5939 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a005edb9-cbd3-3326-84c6-a2adefffaefd | -3.5703 | -54.38622 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| d67ce2f3-960a-341e-b515-dfe6a15953bf | -3.46312 | -50.58685 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 907d2610-c3ea-389e-a83f-3ece0ad7dca5 | -5.96045 | -55.37993 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca7a57b1-7e45-3d33-ba25-f6c5bc5d63dd | -3.17251 | -50.58669 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 376d4ca2-56c8-3d35-8f3c-1bd8ddd87095 | -5.88843 | -55.52886 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 273987bb-5331-3b99-bc11-f4ab9bdde4c6 | -1.32699 | -56.39926 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8de851b0-5d3b-3fc2-a404-d26515166c86 | -5.99166 | -55.37772 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96f24e91-01da-35b4-900f-b731d33c1561 | -6.67157 | -55.09809 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e30984-cfd3-3250-aa1e-481a6fa03f03 | -5.29868 | -60.20981 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47b11371-d6c8-30c2-b1bd-53af81532aa2 | -3.92063 | -55.85367 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c5c24e9-df73-3ae2-a6cd-c5df9c3583cc | -4.72395 | -55.65431 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65109c46-13bf-3a95-9f9f-80b8da975fda | -4.51807 | -54.85841 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da6b006b-0ecc-31a5-8064-bbaba7b484cd | -3.75093 | -59.4767 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b013ebc8-8a00-3b0c-842a-a445950d2359 | -5.21299 | -56.08256 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12d0f6ec-4604-3ee6-b439-a541afc61809 | -3.29617 | -54.08093 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c448b7dd-d55c-3d92-aa7e-5a9b10d74fd9 | -7.00262 | -47.72563 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d764e33-19ee-31b7-bf7b-eaec3528b4ab | -4.57237 | -54.96329 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c502029-08a0-35af-b25d-c69ba9f14a5e | -3.57804 | -54.38033 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c804cc3f-2eaa-3f49-8093-eeb89cd32565 | -2.97126 | -54.07205 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fec49985-c1fe-326c-8eef-922c5b95edb7 | -1.88673 | -54.67131 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8e8f75da-4fe6-3ad5-b578-5c0c0fcaadfc | -7.17775 | -52.61706 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c09be5c-2561-3011-a470-1717fe53a043 | -2.50831 | -56.12362 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63044320-d7d4-3ea6-8687-cb9d2fd1b5ea | -3.58301 | -54.30651 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e77cfd5-f02e-324c-95e9-781bacdce487 | -5.6911 | -53.45785 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de29a3f7-1184-3fa2-a18a-8d62d8cca71f | -2.99178 | -54.17799 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c0c7bcb-b732-362c-8f2e-da53cc736121 | -2.5456 | -57.38883 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a95dcfd9-18db-3f20-b335-20b068b572fa | -6.75608 | -55.07878 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96417651-f164-30ce-8110-5e9512ba527c | -6.50959 | -55.40984 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 441cc535-c874-307e-a286-19318aa90b6d | -7.09319 | -55.73251 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e795fa4a-b199-3fd8-96d3-629ccbfac767 | -2.47076 | -56.06186 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69c5c443-11e2-3d6f-a1b4-dcefa34594bb | -3.59966 | -54.56548 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b140871b-2eb3-31ae-ba03-dcb6a451e28a | -7.03164 | -47.65344 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e118f45b-6e77-3ae6-b18f-6d68b7d72036 | -7.21657 | -55.15314 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 095682d5-8186-3abc-a84e-1bb09c9a5597 | -5.96215 | -55.36933 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33febdfb-85c9-38df-ae3c-1ca0b715ba43 | -4.4548 | -47.91862 | 2026-10-10 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 16c5c219-4960-390d-b592-58f71a0646bb | -5.09315 | -60.22399 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7947f53-1e1d-3700-80b1-886343b535c4 | -4.80227 | -54.67448 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5c97c92-c923-30b2-a59b-677488495d85 | -2.79085 | -51.40954 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30dc3518-46bd-3678-b97c-8858afe681ef | -3.65949 | -55.46882 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2488169-5e04-3281-bf65-49ce28425a98 | -3.26959 | -50.389 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86793c82-e2c0-375f-a5da-b50e8cb93218 | -7.38499 | -55.2048 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b4c7fb2-a0c8-3277-8e48-835afcdcd21e | -1.51237 | -54.52885 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f74f05a8-1235-3243-a2c5-4d0f7f24f9df | -6.09766 | -55.7086 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d7c1317-b6c9-3b0b-ba3d-8d60587888bd | -4.09454 | -54.0168 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d7b1e34b-fb85-3fb6-a612-2553aed8be3f | -4.11876 | -54.01357 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b74dc73-e528-323d-a1cd-39c49359d78c | -4.25113 | -55.27666 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc74cc49-cf57-3756-9095-bb75f02bd756 | -6.29411 | -55.92517 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d573bc1-9556-31b2-9899-189d1c66cb34 | -5.18803 | -60.31065 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72d27028-4fa3-3525-bac4-81f6ce615747 | -3.00865 | -51.01737 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13cd9446-ac9d-3549-8fd6-f1171ff8f62f | -5.17142 | -55.99191 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d164a423-7ffa-36c1-8dc6-39959daa74e8 | -6.62127 | -59.94794 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2020d49-172a-3c69-9012-b92a60700b7c | -5.55511 | -43.96553 | 2026-10-10 05:04:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2be603a-7072-3fd6-97f6-915a09a631ac | -6.74106 | -55.15152 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7add990-25c8-3224-8449-f6bbe245ad35 | -5.11163 | -46.22396 | 2026-10-10 05:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ed99340-c4f6-393f-ba3a-9f4c54d37642 | -1.46651 | -54.75212 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 980079c7-5cb7-34be-8ff5-a4bcdb5f9bfb | -3.64057 | -59.56765 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2f887f0-11e5-332b-9741-938add746fce | -6.46423 | -55.50044 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10bc472b-84b6-3934-9cbe-b26ceda7dc86 | -3.10509 | -50.31738 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbcd1622-63f3-3085-85ca-8363e45f208d | -7.39826 | -55.2069 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 091b3520-b8af-3f4d-8358-976afa66fd39 | -2.88802 | -54.16865 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1ebc535-c903-3f7a-9e15-ddb96c433bc5 | -3.72218 | -54.22253 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README127.md)
