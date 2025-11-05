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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5cff8d6-3bee-393a-9799-dce8028e1c34 | -16.4626 | -45.00159 | 2025-11-05 11:59:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 0f8f74d8-d1f8-35c8-b344-a3d6924dbdfc | -6.73821 | -44.14614 | 2025-11-05 11:59:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c98cf33c-e877-3e47-bc48-7b8cfcff1c80 | -15.0271 | -43.27049 | 2025-11-05 11:59:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 15.2 |
| a3b694d7-e1c4-344d-89a9-bb058ea2d431 | -7.72963 | -41.14481 | 2025-11-05 11:59:00 | TERRA_M-M | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| be74d473-de78-3e8a-8349-a01b4c3429fc | -8.86946 | -41.03658 | 2025-11-05 11:59:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 40.5 |
| ab367eab-c106-3074-bb3c-be01a31edaf2 | -12.15252 | -42.67221 | 2025-11-05 11:59:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 1f34da1b-b305-3e44-b0df-52a4ceaf3311 | -11.66309 | -42.74526 | 2025-11-05 11:59:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 642c88ff-75ed-3a7b-ab22-7db5ce13b2ec | -9.31734 | -40.38708 | 2025-11-05 11:59:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2b1f8bc3-6643-397e-8b60-86c1e6022ba3 | -7.36315 | -42.05139 | 2025-11-05 11:59:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 9a201e56-1256-3cc2-a55d-a52dd22d2cf7 | -13.51479 | -41.01051 | 2025-11-05 11:59:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 3f5d9112-1b0f-3242-93bb-9486cee5c6d2 | -8.59868 | -43.73924 | 2025-11-05 11:59:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c8668479-4b14-3a34-a3b1-a29fdcd78540 | -9.91706 | -44.82165 | 2025-11-05 11:59:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c39e88f1-8f5c-3e2a-befd-e90207a167a6 | -7.08912 | -43.76291 | 2025-11-05 11:59:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f45be242-12a2-3d49-a74a-55254b4b6c7b | -16.54922 | -43.85683 | 2025-11-05 11:59:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5587cd11-9542-3a4a-a34c-6ce4242eb254 | -8.58215 | -43.77579 | 2025-11-05 11:59:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e1c042dd-9c4c-39ff-a9b8-7259b8ee1349 | -7.46878 | -37.5572 | 2025-11-05 11:59:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 70361f70-07d2-3480-b35e-138743ae3371 | -14.30057 | -43.26358 | 2025-11-05 11:59:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| d8e6b879-6502-324d-a733-6154243bff74 | -7.32854 | -38.10166 | 2025-11-05 11:59:00 | TERRA_M-M | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 345e1ce9-4ab6-373b-8018-70a487f13ccd | -8.87088 | -41.02636 | 2025-11-05 11:59:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 4b72c715-df33-3dab-af5d-807211d9f62d | -15.56797 | -43.42365 | 2025-11-05 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1edc03cb-2f02-31ec-8145-0425ff0650a9 | -6.79001 | -41.33796 | 2025-11-05 11:59:00 | TERRA_M-M | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 1c4731b4-0057-3c29-9a7c-a7dc524d0b49 | -12.42154 | -43.5863 | 2025-11-05 11:59:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4b405578-c48c-3e66-a045-1e4f858c8732 | -8.92198 | -45.05614 | 2025-11-05 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| e821b752-cead-3576-9c56-ea7627a971a1 | -12.16209 | -42.66986 | 2025-11-05 11:59:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| a7a6bcd8-514e-3acc-ac63-9cfc0f21d8e1 | -7.19423 | -41.86978 | 2025-11-05 11:59:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 03395a00-4d85-3eb9-8dae-e1a9482fea7c | -8.63227 | -40.46809 | 2025-11-05 11:59:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 8ee5bfd2-1925-38c5-9354-41c9cd76d12e | -7.99755 | -47.24266 | 2025-11-05 11:59:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| a9d558d6-2c1d-3696-9e9b-1a749128411b | -15.63039 | -42.48051 | 2025-11-05 11:59:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d7c8fc0e-aacd-3ff8-a46d-e4bcc5e1d7fe | -12.22468 | -50.28909 | 2025-11-05 11:59:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9d144b23-af5e-325b-9633-45b645a03141 | -14.68589 | -42.73461 | 2025-11-05 11:59:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 91d3182c-c57d-38f4-ab5d-64c9bde69991 | -12.23707 | -50.29118 | 2025-11-05 11:59:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 11f660f6-0416-38ca-8738-86a0209e9982 | -11.8474 | -43.73281 | 2025-11-05 11:59:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6d5e552f-40b8-3a6f-aec3-d9134572f8b7 | -7.19553 | -41.86062 | 2025-11-05 11:59:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 8af00e67-8593-390c-89ad-b63a44482b5d | -7.25847 | -40.87782 | 2025-11-05 11:59:00 | TERRA_M-M | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 256bb958-3a20-3d81-a34d-658e12c1c000 | -14.37524 | -43.25489 | 2025-11-05 11:59:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| d2e4b96e-0dcc-379a-b777-4c4c1d4f1f1e | -7.82767 | -40.43756 | 2025-11-05 11:59:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 05a7f181-0580-3baf-92c6-a30fed9bd489 | -15.63983 | -42.48173 | 2025-11-05 11:59:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e0a22de3-5848-38cb-9ac5-17190d68e1f8 | -12.02268 | -45.68763 | 2025-11-05 11:59:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 00733716-c12c-36bd-a463-e96e81854aea | -7.75987 | -37.95363 | 2025-11-05 11:59:00 | TERRA_M-M | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 91415f92-06c8-30d1-bcce-90eb737553d2 | -10.74353 | -44.22468 | 2025-11-05 11:59:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 821d91fa-6eea-36b8-b745-1bca794a3efa | -16.26919 | -45.57367 | 2025-11-05 11:59:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1742a0dc-6541-3ade-82b2-5c3cd8e05fe1 | -12.52655 | -42.96579 | 2025-11-05 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 58f5767d-5130-3528-9c09-5fd03c1f421d | -7.94158 | -42.13169 | 2025-11-05 11:59:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| dd373a8a-5320-3363-8ad3-6e8760015f2d | -10.05182 | -41.3254 | 2025-11-05 11:59:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 4492f3c3-8f09-31ae-9ce0-93a04275bcef | -11.84995 | -43.7149 | 2025-11-05 11:59:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cc707db3-a1c6-37b9-a3f5-59452665a9f8 | -7.25984 | -40.86781 | 2025-11-05 11:59:00 | TERRA_M-M | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| e0c65ac8-3065-305e-8aea-dc9c4a342d09 | -6.73687 | -44.1553 | 2025-11-05 11:59:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d5f13381-769b-314d-94cc-5cfdf2a63f50 | -16.46129 | -45.01071 | 2025-11-05 11:59:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 7d7b65a5-6853-3b55-9a2f-14fe092ef08c | -12.02412 | -45.67804 | 2025-11-05 11:59:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4b51e124-38ee-38f4-9809-f60cee2c50bc | -14.29156 | -43.26231 | 2025-11-05 11:59:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 2359b6a7-cbe0-339c-a009-96c58ffcd6da | -12.83744 | -42.31775 | 2025-11-05 11:59:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 535705e2-0d65-3636-8ac6-36de023034d5 | -8.94969 | -40.84172 | 2025-11-05 11:59:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7b1d9b4b-d5b1-3f87-a3ff-41d2639a9a48 | -8.03651 | -46.65979 | 2025-11-05 11:59:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 05288e85-ba75-3e25-95c4-9932fe1de2c8 | -10.50415 | -42.39779 | 2025-11-05 11:59:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0b2845ea-ed23-3600-9287-c36ddb8e5513 | -7.76206 | -37.93668 | 2025-11-05 11:59:00 | TERRA_M-M | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 32.9 |
| cd353f5d-a883-3d90-b2a2-f1520df69b05 | -10.10964 | -44.76854 | 2025-11-05 11:59:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 2c673f46-4405-3144-9052-f5b171cde6e0 | -15.46195 | -43.18945 | 2025-11-05 11:59:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f3de6a2f-7a47-3d8d-a5f0-bd8934ab58a2 | -9.91842 | -44.81249 | 2025-11-05 11:59:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9d6529b3-bade-3556-9bac-0c11d14f4177 | -7.17512 | -42.72916 | 2025-11-05 11:59:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| c1ca9fd5-f826-3839-94af-c8232fd55ff8 | -16.29168 | -45.60532 | 2025-11-05 11:59:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 54c760ca-e208-3059-a71b-c597d35c2d0b | -10.21242 | -42.24295 | 2025-11-05 11:59:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| e9151643-fdd9-3321-a6b2-f4c10c1e0235 | -14.37393 | -43.26434 | 2025-11-05 11:59:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| a4fb7464-5950-39d5-9dc1-2da08a41c9dc | -9.51937 | -40.85769 | 2025-11-05 11:59:00 | TERRA_M-M | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 8faf4e07-fcc1-3065-8e03-136d1e8a03d1 | -15.46328 | -43.17971 | 2025-11-05 11:59:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 7a7ba85a-3db4-3fdf-ac30-a65d6b50175b | -9.30705 | -44.57626 | 2025-11-05 11:59:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 893979ef-afe1-3740-b81e-73c408480375 | -8.16526 | -43.91829 | 2025-11-05 11:59:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| bd130c96-86b6-37fe-8d6f-196d4f38f4bc | -14.14615 | -43.11327 | 2025-11-05 11:59:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cea8f843-3037-34ae-abd0-e817c2b8072e | -7.9996 | -47.22946 | 2025-11-05 11:59:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| edc1c1ba-d1fe-3576-80f3-9376a1e1a80e | -8.92339 | -45.04662 | 2025-11-05 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ac7e4cf7-5d9c-3c5b-9298-3bf571b4c9fa | -12.2422 | -42.69044 | 2025-11-05 11:59:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0588e73b-d99b-38ca-a7a7-c39e39dcdb1f | -7.29053 | -38.98123 | 2025-11-05 11:59:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 9070dcc5-3204-38cd-96ea-ed402b8f950b | -8.01178 | -41.63098 | 2025-11-05 11:59:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4a8088ce-7a3a-371e-a981-0fe164692526 | -8.0383 | -46.64791 | 2025-11-05 11:59:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 2cd45c08-8ef6-3675-9237-6069484de1c6 | -16.92314 | -43.68138 | 2025-11-05 11:59:00 | TERRA_M-M | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 71493005-5119-3b0c-a044-2041fa31f95b | -11.85706 | -44.61794 | 2025-11-05 11:59:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 028adc1b-1142-38b1-ace8-a698f047389a | -7.10424 | -44.86192 | 2025-11-05 11:59:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8fbec996-e567-3a33-87a7-e93b3986f5ce | -7.51855 | -38.22253 | 2025-11-05 11:59:00 | TERRA_M-M | CURRAL VELHO | PARAÍBA | Brasil | 2505303 | 25 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 55f507f5-ffd0-33b6-bcf0-ecfcca8db56b | -10.05045 | -41.33556 | 2025-11-05 11:59:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2493fab2-31d0-3314-9b40-7444d5ba0803 | -12.79649 | -42.34229 | 2025-11-05 11:59:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 88b8c97a-a20c-3286-b5fb-04b7fa5e5ba5 | -8.17411 | -43.91955 | 2025-11-05 11:59:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1689b627-43c0-33df-98e8-0fc8952ccca3 | -12.42026 | -43.59534 | 2025-11-05 11:59:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 399ac4e1-ab42-3776-ba6a-813c8a4458b9 | -10.10828 | -44.77771 | 2025-11-05 11:59:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3d7b9cd1-9529-3b51-94a1-9101fef55dbb | -8.95114 | -40.83113 | 2025-11-05 11:59:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 23.0 |
| e7fdd538-57aa-3ab5-bfca-d624a2faa9de | -19.17635 | -44.17251 | 2025-11-05 12:01:00 | TERRA_M-T | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3f8069bc-7cec-301d-a756-6a96a0b90805 | -17.10143 | -44.52507 | 2025-11-05 12:01:00 | TERRA_M-T | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 93783672-68c8-3b61-9f7f-0210e164d989 | -19.13559 | -44.405 | 2025-11-05 12:01:00 | TERRA_M-T | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ab320fd-a3f0-3ed9-976f-4d947ccbc809 | -17.1563 | -45.3717 | 2025-11-05 12:01:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b5eb636c-498b-34fe-9742-0ea07b76abfc | -17.96943 | -39.86622 | 2025-11-05 12:01:00 | TERRA_M-T | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 6420d71a-a654-3ce3-8881-2c3f835500a1 | -17.97748 | -43.4368 | 2025-11-05 12:01:00 | TERRA_M-T | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 25834932-25ca-359d-9ca4-45d5f7c355ce | -17.98671 | -43.43811 | 2025-11-05 12:01:00 | TERRA_M-T | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 820e8054-7bfb-3b00-a412-01a337b79e1d | -20.73618 | -42.0195 | 2025-11-05 12:01:00 | TERRA_M-T | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 6101114c-0ae0-347f-8e73-29cea22d1000 | -17.15497 | -45.38088 | 2025-11-05 12:01:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 71a6f37e-4cfc-3d99-94d4-a21913155cc5 | -18.86284 | -41.11372 | 2025-11-05 12:01:00 | TERRA_M-T | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 73ec630f-3ae8-3d20-9323-0c9c1f8b43a2 | -3.6461 | -42.4393 | 2025-11-05 12:20:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 2a19dddd-e602-371d-bb6c-8afbb06d3111 | -4.4632 | -43.2386 | 2025-11-05 12:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| bb5bd5e2-f982-3cc6-a62a-0ce927b56edb | -5.9236 | -41.2814 | 2025-11-05 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 2feaaec5-b0a1-34d0-9c13-b7f56d6f0072 | -4.4632 | -43.2386 | 2025-11-05 12:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 9d48b616-7153-3ec5-8bce-001b6d5b6baf | -5.9234 | -41.3056 | 2025-11-05 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| c50d4286-3d62-34d7-8f99-ecaf3d942ffd | -6.0733 | -43.2648 | 2025-11-05 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 0d639300-6db5-3e45-ba12-d9c4c20971ef | -6.1271 | -41.6253 | 2025-11-05 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |


[Clique aqui para ver as próximas entradas](README41.md)
