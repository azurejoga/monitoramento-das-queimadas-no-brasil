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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a879825-9fae-3e72-880f-6b364d74d94e | -5.9135 | -44.52946 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 286047e0-9bc9-3cd0-8bc6-5bb36a31aaac | -3.1189 | -50.14486 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8504b97b-acc2-3f26-98fc-ba0930396054 | -2.99026 | -52.81907 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12185cbe-0dae-35ce-9b93-b43d79c9ccb1 | -2.72231 | -47.40082 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7384d89-eb52-381f-a157-67cc0af83246 | -8.32634 | -46.26116 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41b1e827-ed61-3c8c-8f95-116e7562a048 | -3.35092 | -50.20924 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1679cda0-bc78-34a8-ba6a-7ce436253248 | -5.41684 | -44.82309 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 346c5894-a360-32da-b141-08407a175e12 | -3.01991 | -49.43705 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 530a34b5-a1e8-3326-8317-76554ec77803 | -3.97941 | -46.03248 | 2025-11-08 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dffb98d0-aa81-3669-92cf-6e067381551e | -4.26415 | -48.56065 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f67b898-6ca7-300d-ab18-dd86b50dabd1 | -6.21895 | -41.71961 | 2025-11-08 04:36:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4284842f-9051-3d84-ad25-628f5255a84a | -5.49892 | -40.78041 | 2025-11-08 04:36:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 37ed32c5-01de-356a-980d-40d161c09c9a | -4.27503 | -48.34139 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 4fb30885-0f3a-3a0c-90bb-8cae20e753a7 | -4.53217 | -43.76785 | 2025-11-08 04:36:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f358e66-9d8b-30d3-bd15-478da601a988 | -4.49424 | -55.80195 | 2025-11-08 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88b86671-9e20-39f2-a71c-1f018a0cdb01 | -2.7145 | -49.54084 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a353251-636f-30dd-8243-b0d6d0366506 | -4.65269 | -46.87547 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c4321f6-1f5d-34a4-968f-dd145c607c3c | -2.46416 | -49.37116 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83f4b264-db04-31d7-85df-201d370d2606 | -3.03072 | -50.27212 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0964d590-ca53-3fb1-b489-7fdc8435d23b | -3.09378 | -50.32339 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb5fb00e-9abc-3040-b2f7-b51946d41377 | -3.4019 | -45.43604 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37aad5ba-7b88-30d4-88b2-0296e81f274f | -6.20455 | -43.26468 | 2025-11-08 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 881e9045-abfa-3ac8-88e9-df5c09a23010 | -8.20444 | -46.98153 | 2025-11-08 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a1984f5-9f24-3932-8e45-d2a27ea92658 | -5.94943 | -46.64901 | 2025-11-08 04:36:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fed14837-b5af-3874-8d32-1d6f515d6613 | -4.61813 | -46.59444 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95cd8057-70ba-3574-9906-7e97654a08b9 | -3.63476 | -43.65289 | 2025-11-08 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d8bc6c3-3461-37dc-9798-0ac8fec223d1 | -2.69645 | -48.97384 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06c117ca-8d3c-31f6-bd30-67e0d6a7682e | -4.68349 | -46.39532 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b299ed4-f636-351d-ba07-201eff66972e | -4.62147 | -46.59494 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa23185e-6496-37e3-924d-5d5b8357e2cf | -4.33788 | -45.72372 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3acd63f-3bc4-3002-8d8a-993b2231975c | -4.64895 | -40.79264 | 2025-11-08 04:36:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 384e4b20-e772-3a70-aa6a-b174a0fdc258 | -4.91177 | -45.10563 | 2025-11-08 04:36:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5c0afe8-b9de-347e-8e20-acfc18fe9279 | -3.69948 | -49.94643 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ac8e538-9311-39ac-aa6f-ed1000eeb75e | -3.46372 | -50.22565 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16f9d174-d1ce-33a1-bfff-634f946c50ee | -4.29124 | -45.88858 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef0e902b-96c6-3820-8e9e-f9f1d9e949f8 | -4.68911 | -46.4034 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 13af4972-b1f9-3d70-8ae1-fe34dbf45a54 | -4.48181 | -46.86309 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48fea47b-0a67-3ff6-a05f-db5c622b126f | -3.35026 | -50.21334 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d239a5b4-2161-32cb-b0c3-a35f70f60bae | -3.41614 | -45.43448 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c82f759-e39c-36a7-b05a-599088159b44 | -2.61658 | -49.23065 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ad808ee-161a-366d-bc27-a0dda0caba31 | -6.85286 | -39.11692 | 2025-11-08 04:36:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 832309d0-51ae-3d70-a3a6-7554582a01aa | -5.3376 | -45.14787 | 2025-11-08 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14ba7a94-df2a-30f2-87b0-52179c202043 | -5.09317 | -44.79744 | 2025-11-08 04:36:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22884515-ff7d-321c-be63-4d20a08b8880 | -2.71036 | -49.54419 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4517ab1f-fa4b-35e5-a9c8-a8e5e67bd428 | -4.35816 | -46.81487 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cf98bf8-3c52-33be-9c07-30cc023823e2 | -2.68742 | -49.55252 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 10ea8a1c-0cb6-3e6a-bd87-da2b1f9ef66c | -3.34832 | -50.17952 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc53fbcd-7007-360c-93a7-5ad8f351d023 | -2.72098 | -49.16497 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 927f7e60-1a80-3558-88f1-937610d8ad51 | -8.44499 | -43.86974 | 2025-11-08 04:36:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3611ec78-35a4-3844-8d09-ab6eccc3f5ce | -2.98471 | -52.82635 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ed29158-8d21-314c-bd75-908d5d354735 | -3.68949 | -52.13285 | 2025-11-08 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddcdae61-92d9-3f2f-a713-29cb4b4c0ee7 | -5.75418 | -40.79063 | 2025-11-08 04:36:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3b210b0d-8e4f-3864-b7ff-74a4b9200a69 | -6.22329 | -41.71794 | 2025-11-08 04:36:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 127e7644-af33-3959-bd42-0ff68ec479da | -2.46843 | -49.90204 | 2025-11-08 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68d842fe-aa90-3461-84ac-c9ee1fbf6f26 | -5.39577 | -44.23846 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75c5c9c8-eb7a-396f-b04b-7d05ef06c5ad | -3.63173 | -43.64794 | 2025-11-08 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61634120-e6e7-3b27-ada2-ba3be40665ab | -3.45824 | -48.83899 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b3232d9-4fe9-3bdb-858b-f081b0e0ae13 | -4.68168 | -45.84758 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b679bc7f-11d7-308b-a358-e8d52bfef73a | -7.7914 | -48.53091 | 2025-11-08 04:36:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39bf37e8-0e88-3f59-8a1d-25d6a469f32c | -5.2641 | -47.16002 | 2025-11-08 04:36:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08bcbca6-60f3-3463-92c3-15f45cf8c507 | -4.52089 | -41.93123 | 2025-11-08 04:36:00 | NPP-375D | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 69d0d645-f924-3a62-aec2-7e3d781183f9 | -9.11438 | -44.67717 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe354db5-5480-3a25-a8ba-2a11baa2c664 | -2.28169 | -48.46337 | 2025-11-08 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9975bde-e1c0-3fb4-8738-aa229a96ac56 | -3.98278 | -46.03302 | 2025-11-08 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9902020-b034-3680-b23f-390c8c7ca1f5 | -4.08169 | -48.04504 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2269713e-6654-34b6-addc-716aeda1b0bd | -3.43603 | -43.16518 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d73b58ee-0c96-3e96-abe1-57816076dcf7 | -5.11771 | -45.30998 | 2025-11-08 04:36:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d10be11-bf33-3535-be51-c9d7fc23afec | -5.77181 | -40.79892 | 2025-11-08 04:36:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c241b0ab-11ec-3106-91e3-a618cec4db1b | -6.27015 | -43.68273 | 2025-11-08 04:36:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c6d4afb-49f0-3711-ac33-49b6993eac24 | -2.5284 | -49.44076 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91cac7e2-5f64-3902-930a-d498260819bf | -2.98538 | -52.82232 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd38c0bf-05fe-3126-abaa-3adb0992419c | -3.09741 | -50.32399 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3f820dc-c345-35e3-bbaf-ad652bc6e92e | -2.45717 | -49.37005 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 23447d47-cf74-38eb-8791-df1fb7a83599 | -3.45426 | -48.84207 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61736cb4-3937-366c-81fa-386f87d5a8f2 | -4.22576 | -39.17562 | 2025-11-08 04:36:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f1cb95d4-701f-31fb-ba00-e84f3e02de81 | -6.34415 | -39.83961 | 2025-11-08 04:36:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c016841-6234-3066-bf4d-1ff604ad3ee1 | -4.23034 | -46.89465 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64302612-9401-37ca-9d5a-d865d94350cd | -3.64195 | -45.88539 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88e06583-6c32-33b9-982d-13c7c98d52b2 | -3.47541 | -48.97287 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b939b84d-af0a-32ea-919d-fe099e9b2359 | -2.48676 | -49.1102 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee5facc0-d228-3f80-be5f-6c3f00b0b308 | -2.44262 | -49.34516 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d35414d-b4f7-31f9-ab75-1c50d2e0bd56 | -3.01581 | -49.44034 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20852ffd-283b-3fe2-a198-ae2861908af3 | -2.52717 | -49.44851 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dc2955a-00e4-3863-b3d6-208b3b8aa92c | -4.69191 | -46.40747 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bcb16a93-f089-3c64-b203-38a11e94f6dc | -3.33571 | -50.09805 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63161fdd-6678-3532-b1a5-5efe0ea2c504 | -7.48898 | -45.92348 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16f1af91-abea-38f7-916f-d9dac3c8fdec | -3.40393 | -50.45911 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42eacee8-4496-36c5-b106-27bb2f55c2d8 | -3.23989 | -45.60227 | 2025-11-08 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 410b13f2-6e51-3129-8eec-066a5e065dc2 | -4.33438 | -44.71665 | 2025-11-08 04:36:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96f7ce0c-87c9-3c68-8cc9-0c7894190fbf | -2.66956 | -49.46209 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5095037a-d2c0-382a-b29b-4f40ef0d7fc4 | -7.75924 | -49.26848 | 2025-11-08 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 978a8afc-dc41-34b7-9fbc-51e3f0db5e12 | -4.48951 | -46.36189 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f4d8c26-d088-34c0-810f-22b83f6a05a3 | -3.97996 | -46.02893 | 2025-11-08 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6f6a9e3-c4d1-35bf-b285-fb8e50f271e6 | -7.55654 | -47.24931 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21587b7f-8851-3c1a-97b5-0d74b409ff3a | -4.98166 | -44.81792 | 2025-11-08 04:36:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aad7417-7a1d-3cf9-804f-55fe46b92f85 | -7.53572 | -47.38321 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81a28323-5e87-3f78-b353-62aacfa5d64f | -5.93969 | -38.18677 | 2025-11-08 04:36:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 36cdf290-de3d-308a-bfc5-a4b367d67a3b | -7.75981 | -49.26493 | 2025-11-08 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51aa0ad8-d21e-3045-93bd-32315c0b31d5 | -7.32299 | -47.3824 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8f782c7-a054-3f70-abde-5bb5c446eb91 | -1.70256 | -54.67206 | 2025-11-08 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README26.md)
