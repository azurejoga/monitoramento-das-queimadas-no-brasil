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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a33d7323-2dd9-3f19-a8a0-6e5a64eeeb22 | -3.41557 | -45.43816 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97201bb5-474e-39d4-956e-4692084686e3 | -3.67501 | -50.49066 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49a12bf3-1585-39d8-bb60-420b5fb79906 | -3.31741 | -49.13056 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7348cbb-fb61-337b-a41a-969f7a2ad36b | -3.47479 | -49.92918 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db62aa13-68ac-3c62-b16f-0815eac0ae63 | -6.0945 | -41.70889 | 2025-11-08 04:36:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0b063082-5920-376a-b19b-632d16ffea29 | -4.4656 | -46.42693 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6d87b94-4f1d-300b-8924-de8c7c90da1f | -3.31627 | -50.30963 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ba280d2-fcd5-3f49-a13a-f958c6350a91 | -5.12037 | -40.7576 | 2025-11-08 04:36:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e9f2f1c6-d2e7-3763-bf02-faab98cec5d6 | -3.05068 | -48.71985 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be8296f-8897-32d0-83a4-89b2780e8f62 | -6.05369 | -39.14257 | 2025-11-08 04:36:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 96ae8b8d-0f7d-3d1a-b397-e29ae0b55d54 | -4.75754 | -45.78415 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ca482ff-7f0a-3db1-a14c-12040d91f889 | -4.46946 | -45.3296 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f61ba369-ea35-38d4-b2bc-69d6e90812a5 | -3.91111 | -50.04412 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 41c8ca12-6f22-33b2-9fae-ef67e50cd57a | -5.94068 | -38.1798 | 2025-11-08 04:36:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78f07847-e6b4-324b-9fc9-c261d4cb50ef | -3.58506 | -51.24992 | 2025-11-08 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 71538014-b8cd-3cfb-8cf1-24bb6fc97816 | -3.47898 | -49.92579 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41943d4d-b607-3eb3-986f-61ede72ca608 | -4.57475 | -48.47565 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d987d3e6-5155-3b8e-9462-950ee2b2398b | -3.35386 | -50.21391 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b3ed1c80-51a8-33cc-802e-12ae643717ff | -2.71388 | -49.54474 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3847b295-2a41-3930-b986-2ee24aa48f98 | -3.09325 | -49.22286 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac769dc3-7582-3576-821b-f64939dd8ba1 | -3.17393 | -49.23879 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c02a0db2-a24d-3991-96db-0523f4a0cd6e | -5.90997 | -44.52627 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 74504281-fe5a-349c-b1ae-846db60bcd2a | -2.97646 | -48.7048 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 190b2933-43c6-3cac-93ef-0befefc0b5cf | -3.45484 | -48.83844 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc256353-0b09-380b-9842-0f74c6f463a4 | -3.44763 | -46.18951 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30549341-954a-32aa-a8cc-847abfc3bdcd | -4.24603 | -45.99971 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e862b93b-b92b-3578-88a0-32b00bb46efb | -4.21995 | -48.35075 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f869c87-1519-34b6-a2ed-3b5dc92e726f | -3.43984 | -43.16574 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c41b6f49-7db8-336e-97c9-061c4b05def9 | -3.10036 | -50.32876 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efa1e661-a89c-3ca5-a126-49203a0f10f3 | -3.39848 | -45.43551 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c6b4808-0ebc-3523-84d8-471e9a0c6ca5 | -3.59564 | -51.23281 | 2025-11-08 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d90bb6c8-072a-33df-9200-b0eb624181bd | -6.12903 | -52.63887 | 2025-11-08 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3525dba6-e509-3f99-a25b-56b143d5cedc | -3.53199 | -47.5429 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1b13b153-ee52-31d2-a1e0-07aaf9f43b8e | -2.70685 | -49.54363 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f263bc68-052c-35fa-b043-56100cb4a14c | -3.15351 | -50.29872 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64c0851d-9d05-3a3e-bbbd-07877958f78d | -4.97143 | -49.59793 | 2025-11-08 04:36:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6495cefc-2cca-37dc-9c81-21f73b70aa0e | -4.63583 | -45.89614 | 2025-11-08 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd2f802b-bc67-3760-aa3c-cdc9f0cad5b9 | -3.67796 | -50.45102 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04ce7f8f-982a-3ee6-8c43-bb69bbbed51d | -4.59495 | -45.99786 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 8d31c239-7375-3c05-af6a-4cdcbb2dd233 | -3.06088 | -48.72145 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bab6474-e733-3d66-8d30-de63f7f00a98 | -3.69351 | -52.13345 | 2025-11-08 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15662546-ffa3-35f1-b1fb-695a515cea7e | -5.94888 | -46.65257 | 2025-11-08 04:36:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39571a88-aa89-3521-99cd-5518be2e5cf8 | -4.89718 | -47.9608 | 2025-11-08 04:36:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf943a4d-ee1e-3a91-a63a-ed4275978709 | -2.98727 | -48.70237 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 377dac0c-e750-3aba-8379-b3e886a4a6e9 | -4.32843 | -45.98612 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f42c6577-88d9-327c-8361-03ebbf62e501 | -9.22245 | -48.57815 | 2025-11-08 04:38:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0312322e-e998-3f4b-aefa-642ab9ace30c | -10.61763 | -52.18101 | 2025-11-08 04:38:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bd74e1f-7128-3dc5-ab7b-8ac20b432236 | -10.26883 | -49.04472 | 2025-11-08 04:38:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26c65304-1a29-36d2-89d1-ae2f1352386c | -9.08404 | -61.69325 | 2025-11-08 04:38:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f4b8d61-8853-3379-abb1-4efc11da1f8e | -9.73196 | -48.77808 | 2025-11-08 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f02be7e-28bf-39a1-8981-830849a619b4 | -15.187 | -49.52218 | 2025-11-08 04:38:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dad4c42d-ed04-3d37-af62-b7643bb460a9 | -9.1387 | -51.29855 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eee9b8a-e501-3507-984f-f6e4869794b0 | -9.04871 | -47.00706 | 2025-11-08 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00ca8608-f1b7-3c0b-8bf9-61fed3041c71 | -11.12158 | -44.65993 | 2025-11-08 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ca87123-c5d8-3ddf-98ff-f453c0053b74 | -15.19089 | -49.51915 | 2025-11-08 04:38:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a334718-d36f-3250-8914-001700bf22d0 | -9.11 | -48.90409 | 2025-11-08 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f662d93d-a967-349e-8e1c-800bfc4af735 | -11.96593 | -44.34841 | 2025-11-08 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e094142-d171-3edc-9512-7f63e5fe0993 | -9.76722 | -55.61915 | 2025-11-08 04:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0437e544-a964-3e84-b203-3a52883c68e8 | -14.70671 | -52.84142 | 2025-11-08 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b3402d1-b44f-3073-ba2e-6d3c4087d4b1 | -11.20013 | -53.82714 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15806896-6fb8-3c79-9fcd-32415060c568 | -9.13804 | -51.30257 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff644cf2-f924-3509-8ed2-913771effd67 | -16.09175 | -49.39247 | 2025-11-08 04:38:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8668761e-e67c-3637-854a-7e74abc6049e | -9.05378 | -46.99667 | 2025-11-08 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 137b8bc0-be70-3b3b-8030-c58551cec85e | -11.19924 | -53.8323 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 445303f2-8979-38a3-a807-58eaffc6488e | -11.56121 | -61.69567 | 2025-11-08 04:38:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a59fba1-7f78-3eab-b50b-ac5134c33bea | -11.78357 | -48.79179 | 2025-11-08 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb987d5e-8211-3ff5-94a2-53134b615bc7 | -8.65688 | -50.05484 | 2025-11-08 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b4c08744-4289-3475-a68f-efdf2210cb7a | -10.9902 | -53.98189 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 794260af-3fca-3c06-b193-a9d6a4ce8b01 | -10.8159 | -49.19783 | 2025-11-08 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5be24174-06c0-32a1-8d51-17d49f97b37f | -9.14225 | -51.29914 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7134f196-2564-365c-a935-21444fe740f7 | -9.91013 | -47.41698 | 2025-11-08 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 784d47e1-fcc3-3df4-bc4e-99fdd2ba1f7c | -11.09482 | -45.19312 | 2025-11-08 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93fdfc1f-85bf-3a5e-8fd9-dd923ebfb676 | -11.09856 | -45.19366 | 2025-11-08 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b64b351c-577f-3ac9-ad42-04700b40ba88 | -11.73183 | -59.30552 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81694a25-a9aa-3b26-ae83-52006dc69a05 | -9.3263 | -47.83003 | 2025-11-08 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 210a3bdd-3318-340a-a3b3-62c1dd1511fb | -9.72471 | -48.90961 | 2025-11-08 04:38:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18ed6f5b-c005-3e00-a9bf-98f845999717 | -11.96323 | -44.35173 | 2025-11-08 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e11c4e1-2e1b-3d2f-bc2c-3440ea423acb | -10.98957 | -53.98542 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db153b0b-d1e6-3f0c-bb4d-93665662c236 | -15.23154 | -43.28345 | 2025-11-08 04:38:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 79f9b940-1aad-33fa-a7d9-bb163cf8598d | -14.97923 | -52.97817 | 2025-11-08 04:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 817c3bd7-56e6-3d8f-8800-013b39c86b1f | -11.69199 | -44.14336 | 2025-11-08 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a49d0147-0535-330e-b829-a55a94f50dcc | -9.14159 | -51.30317 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09b760d6-c150-3b9d-bd17-38c0920f7e22 | -8.74239 | -48.3191 | 2025-11-08 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbe24c29-8758-3a6a-bbe0-d963d690e889 | -9.93989 | -55.54646 | 2025-11-08 04:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d576b0f-0090-36a2-ab86-3e826e502563 | -11.73596 | -59.31422 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95e12d8c-4bfd-3e38-968a-dfbcdf7befe7 | -10.99699 | -53.99044 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 010bf6c4-c1bd-3a7a-93d7-42ccde5e192e | -11.86996 | -62.89072 | 2025-11-08 04:38:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 765764a3-5eb4-3231-9fae-19062baccae3 | -11.72312 | -59.31978 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a7b7114-dcb7-3418-8d89-228413717555 | -14.62877 | -52.45065 | 2025-11-08 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 060fcff2-b2db-3ce8-afca-55cd127c3e7d | -10.57408 | -49.25222 | 2025-11-08 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34ee5faa-ef9a-3373-94bf-8167a45a01df | -11.07759 | -54.10081 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f051406-ea85-35c6-be4f-9c3a02539f1f | -11.71005 | -61.4243 | 2025-11-08 04:38:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69ddaf7f-d7fd-3a59-a887-2446936f69b6 | -11.73452 | -59.31043 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b94ab887-97da-3040-9a00-430ed5f6c755 | -15.79764 | -50.10823 | 2025-11-08 04:38:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79671238-aafd-36d9-8697-5d909731ddf2 | -8.38195 | -54.82123 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf76aa29-3400-306a-aa61-f23130c5d7c4 | -15.18756 | -49.5186 | 2025-11-08 04:38:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b011d1a-986e-3321-9894-10b6168ed729 | -8.90741 | -47.82903 | 2025-11-08 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3c7039d-a482-346b-b428-9f383549634c | -10.53162 | -47.8632 | 2025-11-08 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b20dc9f1-e77b-334e-8019-64c319672f07 | -10.7156 | -48.54792 | 2025-11-08 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe2fff32-18ee-330c-8c5a-70fdaf8d9ddc | -10.52437 | -47.86568 | 2025-11-08 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README27.md)
