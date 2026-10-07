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

## Dados Diários - Página 201

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cbcb12b-80d4-3fe9-a43d-76d0f5630101 | -7.3037 | -43.97086 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1a4ee900-99ff-3b0e-8ea3-4005735c3f84 | -8.9875 | -45.92688 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1da0da96-d371-3478-96e9-8b637e22f037 | -3.89933 | -44.10408 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6821d382-2c32-31a7-82ab-1fefe4e10766 | -7.79393 | -39.54868 | 2026-10-07 16:37:00 | NPP-375 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 67b838e0-28dd-33ca-9588-3f9cbdefaf2d | -6.21477 | -45.1875 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 68076226-9277-379d-913c-b2e81d7da7de | -5.80162 | -52.35611 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| eb204eb6-ffeb-3a2a-b02b-6b5e18be0e6f | -3.73759 | -44.97133 | 2026-10-07 16:37:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| e8e80b14-e4cd-3e0d-9c64-020faf1144aa | -6.19888 | -51.43377 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4055afd7-925e-3fe2-98a5-db92a5ed8363 | -6.67134 | -52.97378 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c74c4955-a543-36b4-ae18-4754e747a612 | -3.8641 | -40.22699 | 2026-10-07 16:37:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 12079d59-2c64-31ba-804e-0decfb654dfa | -5.42784 | -45.6344 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54282afe-c146-3c92-b6a9-67e149859ce4 | -6.21593 | -52.84314 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| eb11cbcf-7dcb-31d9-92cd-663e121e8f26 | -5.25912 | -47.93127 | 2026-10-07 16:37:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 05b196ba-9192-359c-9534-ca8c9b56492c | -4.7288 | -38.18234 | 2026-10-07 16:37:00 | NPP-375 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1db414b-64dd-340d-b8af-4f257da670ee | -9.96462 | -43.48867 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22cab4f2-4720-3171-8fbd-df62c4facb4a | -14.38357 | -40.3345 | 2026-10-07 16:37:00 | NPP-375 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 002a3855-0f17-325d-8bab-9411ce0128da | -6.47997 | -46.6146 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 794bbf94-d2f6-3a8a-8d00-ca8a42b882aa | -8.76846 | -44.15662 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 32f8ea0b-32b8-3c9c-84e5-1b373b29c49c | -5.98447 | -40.92788 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| febb4110-65a2-3b6e-9ede-99056cb8f254 | -8.78698 | -47.58025 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 68e8196e-124d-3b10-8f6a-95c2f2562989 | -5.99889 | -53.62736 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 34e0b359-3b9b-3c73-bbe5-179020c35f7c | -3.34542 | -42.9318 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4dfcdac-b7a6-3731-828c-cd3014187de7 | -7.34687 | -45.29127 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ca686d9-8f79-3eb6-a659-5ed03fe40958 | -10.88374 | -46.66954 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 532229d8-92d9-3b0e-b593-5e3d2765b789 | -6.54758 | -44.09078 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d33d209-4c3c-369a-a2fe-89f73b60da1b | -10.57538 | -47.28477 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| eb2195df-e5fc-3bc0-b74d-dc92271f4c39 | -6.20115 | -49.38209 | 2026-10-07 16:37:00 | NPP-375 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8f06438b-fb3b-3a37-afa3-393ebbb81d85 | -5.87607 | -53.62753 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5a2a2b8-f76d-30e3-ba17-a8a1fadb706e | -3.7412 | -41.72143 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0843b9e2-58f3-3245-999b-cb933c09ba6e | -5.9405 | -45.3834 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59f78a88-7faf-34b6-8df3-6586df318c19 | -7.839 | -45.50805 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 853fd8d1-b9d1-3229-88da-b290b2195deb | -4.41961 | -43.7317 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 7765be40-6c0c-39d8-a352-e639b28abb47 | -11.34547 | -51.88248 | 2026-10-07 16:37:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d1b9e902-d83e-3c57-85d5-0c14ab43a5c0 | -8.25202 | -35.03536 | 2026-10-07 16:37:00 | NPP-375 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7ec8d7dd-af4c-330d-aea6-7ac9132785a0 | -3.68107 | -38.81082 | 2026-10-07 16:37:00 | NPP-375 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7120605c-d9cc-3929-9dad-21125b7632b3 | -4.58485 | -40.77287 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 3259cfd6-9e34-3518-9717-751ff42bcbe0 | -4.56519 | -40.72066 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 8a8da10a-721c-336b-83dc-18cebd83d091 | -8.92942 | -44.94073 | 2026-10-07 16:37:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1ae31eeb-27f9-30b8-bb9e-d43170a1ff7f | -6.12218 | -52.71252 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b395f15d-fd12-3536-bc95-d982a8afd385 | -11.05879 | -45.84831 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 43813dd5-d0e1-379b-ba45-3af0a571e048 | -4.30232 | -50.78618 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3dac3361-3914-3ffb-81a2-e1aa577e775b | -6.14048 | -47.93052 | 2026-10-07 16:37:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| d6a98505-9798-3483-a899-85b5c351522c | -7.23496 | -49.38622 | 2026-10-07 16:37:00 | NPP-375 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 280bd5c1-85fe-3a6a-a204-354a684cba75 | -9.40254 | -45.88661 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 42e52450-7898-3828-a139-0a3c4378ff3b | -4.67837 | -40.82479 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 16e2717c-da2b-3e99-86be-5ab0c872d079 | -6.37556 | -55.15388 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 14e7a320-dbc0-3935-8854-1722baf50a1b | -6.8472 | -41.77727 | 2026-10-07 16:37:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 929ddc7b-79c7-3ad3-a723-112e5acb5585 | -5.73441 | -53.455 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 92f6f40a-df50-3d54-a7cc-f243fd389136 | -3.51323 | -41.95089 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a54e1331-814c-37fa-b290-eeb7dbc6ebc7 | -4.28856 | -43.02798 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b0c3163b-44e7-3a59-a3f7-706f8631c12b | -3.9464 | -40.73625 | 2026-10-07 16:37:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2f9b96e6-ac55-3cee-bd79-541fc48f7bd1 | -10.29638 | -47.82441 | 2026-10-07 16:37:00 | NPP-375 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fff3fffd-8f7d-36c4-8ac9-7685e3af53c5 | -9.95709 | -43.55077 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a5de265f-f4a4-3942-93e1-9ec3ca3bbfb4 | -7.19346 | -52.6266 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11072335-1af0-32d7-9749-35549ab399b2 | -5.36662 | -46.72842 | 2026-10-07 16:37:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad9f9a17-d717-300f-8eac-09c1c45e51a1 | -3.79154 | -40.07409 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 170976e3-75a3-3d24-bc74-4b0c692d299a | -7.30185 | -37.54148 | 2026-10-07 16:37:00 | NPP-375 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 99cb1895-7493-3f16-8c2a-97ac9f715abb | -4.56894 | -40.72011 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 8094e93e-f713-3124-82f3-07a3e1e4eda5 | -9.9255 | -45.74664 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ca8fb4a5-8577-3c81-8f35-937d6e0e9812 | -5.97653 | -41.36248 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0f3e4184-cf88-30f3-9d36-33f9ce21832a | -8.07499 | -55.29553 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 61d12cc2-d03f-3c6e-af90-3276c1df0b42 | -7.30755 | -43.97382 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 529179ec-fd1a-3612-8ccd-36da622024fa | -4.48152 | -50.6631 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1eab706d-3609-3289-b6aa-654cb469ee60 | -4.3801 | -41.8444 | 2026-10-07 16:37:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e9696318-5cbd-3c58-9dab-7172e478bffa | -3.62188 | -42.80179 | 2026-10-07 16:37:00 | NPP-375 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4d7394a5-ad00-3de6-9d9a-f6c9697acde3 | -3.2063 | -42.95736 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| d80feea4-6484-38e0-a750-330b79ef544f | -6.3461 | -38.8639 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6c13a139-ce9a-33d8-913f-992d36607b40 | -9.12132 | -45.10926 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 60e41c99-9588-3e72-95aa-cfc7eae80cb5 | -7.40102 | -38.85625 | 2026-10-07 16:37:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 45bec5cb-2d4c-37c2-92de-de4f7597120a | -3.23349 | -42.79335 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 42d98b93-b3bc-3f59-932f-f0934f6e3bf5 | -6.27507 | -52.84779 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0bfc7eb2-b6b7-34dc-aa78-56cfa65d31df | -3.74057 | -41.71736 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1c08f4f6-9e88-30a7-92b2-597f0b0d83e8 | -7.47453 | -42.8188 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| f2e2cbb7-11e3-3954-a6c8-b59340e74d7e | -8.01736 | -47.18116 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1aeb450f-a7ab-3071-a8c6-edf7403104f4 | -3.9634 | -38.69317 | 2026-10-07 16:37:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2caf402d-3c6e-3ae2-8c7d-d2c2f8637b5b | -9.21314 | -46.68604 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6d2b19ff-696e-3d3e-b4bb-1d91a8df2ac4 | -5.96627 | -40.93072 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 626c85fe-341e-3d03-ad1b-8ce28ceeb1c7 | -5.69747 | -53.47825 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8b696256-50da-3a4d-bdf3-2ef1fd29dd4f | -16.52012 | -45.27686 | 2026-10-07 16:37:00 | NPP-375 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b2e14e2d-69c8-30b3-be02-a7b23566ba60 | -5.10022 | -42.92597 | 2026-10-07 16:37:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4ea0a5b7-3d7a-35eb-aed9-96c60eeb2951 | -6.2891 | -44.89873 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dabe3ed4-1963-3537-a271-651bdf3ad345 | -6.0213 | -53.54823 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 425fdef3-e0a4-342a-8edd-568af229c91d | -3.73532 | -44.97874 | 2026-10-07 16:37:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| ae63cd0c-ff6d-391a-b368-cd024cdd21e4 | -4.57809 | -40.77126 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a9747738-871a-38a1-8e1e-40b7776f0fd1 | -16.90976 | -42.11712 | 2026-10-07 16:37:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| be134fc2-66e3-3f3f-b5cc-0f61e08e310b | -3.3602 | -41.91129 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| b9fda711-09ed-3206-8539-04e319c9f0be | -7.21059 | -55.11597 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| abd77070-4163-343a-b1b6-eeb8a323702e | -11.09783 | -45.67449 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 92693300-e580-3325-860c-ca9abdacde40 | -6.94848 | -45.26392 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86af0c0a-2ab3-3bf6-b007-0276a11f5715 | -3.80471 | -41.76608 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| fc376a8b-6e83-391e-82ce-e7f4a5efd08b | -6.68101 | -52.96571 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 30f5a7d3-f718-3259-9c09-aba08127e2d0 | -5.9835 | -40.94532 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 07d8d865-b6f6-315e-92dc-2ad2ea0d2059 | -9.98946 | -46.01323 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8a0073fe-0e3a-3d2b-be7d-f47967afd0eb | -6.32276 | -43.48606 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56aef9f1-0a48-3d87-85c4-991d752f20e6 | -9.79913 | -48.92203 | 2026-10-07 16:37:00 | NPP-375 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f895afee-c639-332b-ab26-ea9f256a0637 | -9.51451 | -46.84848 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a69bbb5-9a69-300c-8dff-df3f906673d6 | -5.72544 | -45.15158 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 5d7942f3-d705-37f8-870f-59afdc17c747 | -15.26076 | -40.96588 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| efe39ed2-ffee-3a6b-9862-eccc95c9aa3e | -5.99659 | -43.60292 | 2026-10-07 16:37:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 87da1daa-37ac-34dc-b036-de85e09e1482 | -6.47786 | -52.80985 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README202.md)
