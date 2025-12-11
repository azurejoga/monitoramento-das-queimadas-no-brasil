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
| 972dfc66-e8ea-333a-b214-f1164c7207b8 | -4.73717 | -45.07227 | 2025-12-11 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 214781ef-509f-3428-a8c7-3d0ba838bad7 | -2.3484 | -45.65682 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8cb6e55e-4e1b-3bcb-bda8-35003c50d017 | -3.4251 | -41.6602 | 2025-12-11 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a3373209-a091-3a05-b6ef-96e617d7d0cb | -2.98106 | -45.77539 | 2025-12-11 00:13:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9cb9a8c9-1c65-3240-8a1b-8959ab56a127 | -4.65593 | -44.49728 | 2025-12-11 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 032c0b06-8590-33ad-aa4c-2acddb009f82 | -4.54632 | -44.04397 | 2025-12-11 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| bfb431b5-5baa-3549-a27d-f7c472c2884c | -2.53968 | -45.38005 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 83587c59-5556-39fa-9f39-f9b89a68eb05 | -3.39323 | -45.42422 | 2025-12-11 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d84691d1-ff99-3c89-9ce0-c03b5d946db7 | -3.13761 | -44.97445 | 2025-12-11 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5f9ce3f0-840a-3182-82dd-078bdd12d412 | -3.42187 | -41.65283 | 2025-12-11 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 88c8e0f5-3a19-36fd-9645-3807112bd771 | -2.46997 | -52.15528 | 2025-12-11 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0fa9dfc4-f5c6-3de1-8e7c-bb59b31b62f4 | -3.69989 | -50.95867 | 2025-12-11 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1220b7ec-5117-354e-a79d-642960c97b69 | -3.62705 | -44.65095 | 2025-12-11 00:13:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 63f6c6d5-bf2f-329c-98c7-c8b3aec6676e | -4.22994 | -45.39919 | 2025-12-11 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 6315d78f-3025-353f-b9d3-341a382e91ea | -3.22917 | -45.29806 | 2025-12-11 00:13:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 50e57ff7-7735-3f04-8449-1d9051b0805e | -2.08078 | -45.32777 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32fedf23-f451-343c-88ac-df47681b93e7 | -3.36429 | -45.34622 | 2025-12-11 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ffd981b-8d02-3890-852e-6abfac1bec17 | -2.60504 | -45.31884 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6ac5a555-82ac-35d0-8cbc-720b8c33512f | -2.9216 | -45.8018 | 2025-12-11 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 5d52c9b4-ba7b-3777-b9ba-2a9edae1b7b6 | -0.65023 | -52.38896 | 2025-12-11 00:13:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a393443b-0e5e-33a6-830e-16c94e50db8b | -4.07946 | -43.68935 | 2025-12-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a3e691c6-9c9a-339a-a5b5-d31c4665c238 | -3.66534 | -48.93467 | 2025-12-11 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6ce2960c-17f0-30e5-b4d2-8dd911c2f876 | -1.42782 | -45.66493 | 2025-12-11 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0678f25-fa96-36ae-832d-e72a10d7539e | -3.02391 | -45.41886 | 2025-12-11 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| d0a159f6-5fb6-31ce-8996-e69d0aa1a716 | -3.01457 | -45.14701 | 2025-12-11 00:13:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c47210a7-78c0-3612-abb3-13d98bfc27e7 | -2.81242 | -45.15072 | 2025-12-11 00:13:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d74cdc6d-5805-3195-b515-18e4ef7a27b9 | -2.91068 | -46.72955 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 445eecb0-977a-324b-af70-4703ea7f1d2a | -2.16757 | -46.15144 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0cfb1334-4710-3fbc-8cec-1408d68ad581 | -1.74999 | -45.60157 | 2025-12-11 00:13:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9c94e7a1-365b-3d2d-83b5-75312e75e2ba | -1.19694 | -47.53407 | 2025-12-11 00:13:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 6faa024f-3546-3e4f-ac5d-61accf599160 | -1.5899 | -53.76244 | 2025-12-11 00:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| f3b5af67-e7f2-35eb-8100-60c905b34d5c | -2.91398 | -45.81187 | 2025-12-11 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f4f2ce3-66fe-384b-b014-1091d1974d3f | -3.34696 | -46.21072 | 2025-12-11 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0c7379d1-d383-3f5a-a66d-2e00e48a9fb2 | -2.24103 | -45.67819 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d23bf458-c70d-3aaf-842d-63db34b6d61a | -2.85356 | -45.05169 | 2025-12-11 00:13:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 92881ab7-b5c6-33d2-8a07-1a158f68a646 | -2.19806 | -45.44344 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| bbaca86b-0355-3a27-a6ed-e1b586f43fce | -3.54547 | -45.45414 | 2025-12-11 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e1181edf-f308-34c5-a2de-a9b4eac11533 | -2.17919 | -45.76547 | 2025-12-11 00:13:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 962e0fef-c6f6-3a51-9596-a9311ce0553b | -4.54769 | -44.05367 | 2025-12-11 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| a70fc108-ecdb-31d8-a356-d11e901c0097 | -4.20165 | -44.47822 | 2025-12-11 00:13:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 314e0cab-52ee-3aa3-a44d-f4466f33f3db | -2.47833 | -52.16049 | 2025-12-11 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fd50b963-9698-3cea-b71c-04678a79f8ef | -4.12115 | -42.92344 | 2025-12-11 00:13:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 816a8ae4-89a1-3c5a-9e42-33f4e23baf19 | -4.31591 | -44.50384 | 2025-12-11 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 701a467b-2886-3b5e-8f8b-3809344a1eaf | -3.2538 | -46.41496 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 3feda122-801b-31c8-820a-cf77d2011945 | -3.67123 | -43.92316 | 2025-12-11 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e70a174-f074-311a-8753-85d6360a6870 | -5.17988 | -44.81288 | 2025-12-11 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86b5340a-f1c9-342a-a1d3-01d89baf3bb5 | -4.40373 | -44.80246 | 2025-12-11 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13f4c680-5c0b-306f-b0bd-44778c7ca5d2 | -3.9562 | -41.51645 | 2025-12-11 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| a6d9df1f-d8ff-34c1-a9e5-04d3f61ce8f0 | -4.31459 | -44.49448 | 2025-12-11 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a73a4fa0-d74d-3b69-9a9e-25a89f1d3822 | -4.2388 | -45.39793 | 2025-12-11 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1fbc0c3c-7b75-3468-9e1f-336210ea4fcb | -2.47588 | -52.14293 | 2025-12-11 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 163bcadc-7dcf-3877-9e46-2ed058398236 | -2.69414 | -51.64775 | 2025-12-11 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f822b12b-7eb2-3b6b-a686-f3e3d5c954ec | -4.73875 | -44.56118 | 2025-12-11 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0a832a8-07e0-321c-b7d6-8ad0476471d6 | -4.17629 | -43.83003 | 2025-12-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a20f0fe0-22bb-38e5-8f7e-58f028192d2c | -4.31828 | -45.37138 | 2025-12-11 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b2ac5d20-70e3-3dc2-9dc9-a0bdad70c0de | -2.17796 | -45.75658 | 2025-12-11 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 633d5e1b-39f1-368a-b7b0-1acaf57e6b6e | -2.13828 | -45.34111 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1418ddb3-9db7-3d9d-9fe4-7e3c083c7bf2 | -1.1167 | -53.68713 | 2025-12-11 00:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 2d0c7d20-0e49-3aa5-8d60-c0094cf1e940 | -2.19931 | -45.45247 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 12c604cd-1a48-32f6-9d58-71f72aa757dd | -3.60111 | -47.52647 | 2025-12-11 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6c93f594-cc00-320f-8496-9255fb3743a1 | -4.83066 | -44.95165 | 2025-12-11 00:13:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 39a9f398-0236-3c1d-93d8-ffc0e3a8ad39 | -2.35605 | -45.64665 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8ff4dfba-b806-3959-b65f-cb5c573455e2 | -3.13888 | -44.98364 | 2025-12-11 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9bbf67ea-1c6b-3ee1-8a59-5e9c42b25739 | -2.13676 | -47.59389 | 2025-12-11 00:13:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cca3e2b9-13ff-3efe-aa14-b3617227855c | -2.31454 | -46.48222 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ea31a19c-f05e-36f8-998b-80cabc65a815 | -4.24471 | -45.58376 | 2025-12-11 00:13:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 102a5850-9449-34ca-91d8-4e0ae58e4fc6 | -2.65672 | -51.63634 | 2025-12-11 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c1e08e81-9083-3fbd-b8c2-874dc3eef9c0 | -2.92283 | -45.81062 | 2025-12-11 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 9f8da9f1-01eb-3d80-b3c6-1dbed4c3139f | -4.23587 | -45.58501 | 2025-12-11 00:13:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 41867dbf-34f8-3838-b229-efc3257c1b2d | -3.39345 | -42.10662 | 2025-12-11 00:13:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 645b30b9-4fc4-3ee8-b4ad-20afac33e369 | -1.69138 | -46.57671 | 2025-12-11 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad697d42-7e68-35e5-aa23-f55f60f0ae6b | -3.88137 | -42.53102 | 2025-12-11 00:13:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7e69c8ac-bd3d-3936-9740-90b5bbbf482c | -2.84724 | -45.80051 | 2025-12-11 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 6ee6978d-cb9d-3f42-b2de-b2175e20e719 | -4.57647 | -49.16846 | 2025-12-11 00:13:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b7eb48f1-7b44-3a60-8131-68a49c9e989c | -2.0343 | -45.78902 | 2025-12-11 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| d1ecdcd4-9251-37ff-a802-1d4364332182 | -2.61398 | -45.31757 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3777842-6789-31ab-b653-a3617e6f1857 | -4.41272 | -44.80117 | 2025-12-11 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| dfcae284-5b51-3b7a-8e79-4be3a433fd7a | -2.03177 | -46.56722 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 887d64f1-f612-3c1a-b765-fdea91cb1d9f | -3.84556 | -47.8349 | 2025-12-11 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9aa0ecc7-8975-33b7-9801-657f62e545f8 | -2.8476 | -46.72938 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc969ae8-ad9f-3d41-936d-a1ec66a3e09e | -4.2722 | -45.24784 | 2025-12-11 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 874fd55a-1a6e-3e28-8b6d-1ff28e317a04 | -3.08998 | -44.89662 | 2025-12-11 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 7d773189-48a2-3aa2-b787-02d537382f48 | -2.2201 | -45.66893 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 8c89fde0-c65c-380e-8331-ba75bf1dfaa7 | -4.73843 | -45.08122 | 2025-12-11 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f79e38d5-f9be-39da-9b6e-b2eb4369a224 | -4.44071 | -38.97603 | 2025-12-11 00:13:00 | TERRA_M-M | ARATUBA | CEARÁ | Brasil | 2301406 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 119c3e33-d32d-376c-b789-f54a732e7535 | -2.96212 | -45.17 | 2025-12-11 00:13:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0153d8d4-ca1b-3826-acec-60ee90583141 | -3.23557 | -47.47959 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 345de596-b546-3f84-b191-5f91f8245f7a | -4.93195 | -43.96419 | 2025-12-11 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0a0b721-945a-3c07-8993-49c623f0b51e | -2.01513 | -46.38188 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 43be7691-ebf4-3566-8731-7856287de769 | -2.70132 | -45.67344 | 2025-12-11 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 715a24d4-483c-3771-bcb4-7e64535ecef9 | -3.87966 | -42.51899 | 2025-12-11 00:13:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 25a24543-d0b1-320d-8696-fff8c17462ef | -3.35365 | -46.86299 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e67438e9-ae5f-359e-b651-035208836466 | -2.98272 | -45.12069 | 2025-12-11 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 15989364-a6bb-34b1-8371-3eb4e8b1cf73 | -2.13701 | -45.33202 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fdae4130-08b1-3081-86f3-e01fab48d7d4 | -1.82447 | -46.2061 | 2025-12-11 00:13:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1e05e8a9-6b00-3cf7-9baf-a350d27622cd | -4.34412 | -42.20117 | 2025-12-11 00:13:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| c67cea9f-cce7-397b-be97-60e1f1a28fcc | -2.96338 | -45.17909 | 2025-12-11 00:13:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| e78ffa44-490f-3180-a7e1-e3a70ca251a4 | -2.91276 | -45.80304 | 2025-12-11 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 03964457-6cb5-3315-b44c-615f84d01d7d | -2.52464 | -45.27146 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f4dd14c-eb0f-3189-ab94-989f0411f0a0 | -3.25501 | -46.42374 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README4.md)
