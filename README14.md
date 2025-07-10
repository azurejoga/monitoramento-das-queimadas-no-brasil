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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1e6ee25-b88d-3a39-9e1e-0c5d4c66c7ee | -11.36833 | -48.71217 | 2025-07-10 04:04:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c480e4d0-4ab5-374d-8a3c-a863ea6d973f | -8.50239 | -43.29259 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| c7fb1975-895a-3027-9cbe-664fbdf1239b | -11.95669 | -46.36017 | 2025-07-10 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 350e4dbf-2209-3892-b5c3-49b5f721829c | -13.34064 | -52.89434 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 049e9cd4-c4fb-3772-adc1-a42bb0ab8fb1 | -10.575 | -49.15224 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 474f48e5-9451-3c18-9f19-7d4ed11d1bc9 | -8.50315 | -43.32052 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 9319a5f3-a1e6-334d-aa33-f9f4b21418fa | -8.49592 | -43.28732 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 49c93de9-5a1c-3bbd-93ce-48da63555d79 | -7.19774 | -45.35066 | 2025-07-10 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69e18b97-680f-36eb-96ae-cddb4553b86a | -8.51167 | -43.31356 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cef4a44c-476a-32ba-aa41-f5f80bd0e806 | -8.23221 | -44.93105 | 2025-07-10 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fa354ab-81e7-35f2-b5a6-d28185cccc55 | -7.73992 | -43.59403 | 2025-07-10 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 564712ed-6cbd-3a66-b0db-ac8c8a355939 | -14.73086 | -41.72885 | 2025-07-10 04:04:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7410b85-7a1b-3567-8435-c1fc3080b406 | -7.46406 | -49.39939 | 2025-07-10 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ba91c5d-03c6-3dc7-a456-cc32f2b183f9 | -13.34576 | -52.9001 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 21933d62-17a9-305f-a9d2-751ef81ecda2 | -8.50741 | -43.31704 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 4a52e8f0-765d-385c-a0e3-bb5801f6cb1a | -10.64047 | -45.22594 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4adc9684-ef43-3e68-a35f-37d0a08c960c | -13.34076 | -52.89874 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c5cffef-e922-3a80-9d38-07820e14c57e | -12.22019 | -44.21602 | 2025-07-10 04:04:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a09807e0-e6e6-3ef1-9f58-634a0376fc2c | -8.50596 | -43.29319 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 4820b512-42d4-3cb4-b4e4-1ac52c858b1b | -8.4975 | -43.30014 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| f8155e16-0e6d-374c-9ca7-cb4a9f2448ac | -8.50878 | -43.3089 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| d8e162d2-fe82-376d-a3c0-0c1129a612b7 | -12.46988 | -46.91526 | 2025-07-10 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebdf6662-9e86-341b-b53e-d429d895a0d7 | -14.73527 | -40.98028 | 2025-07-10 04:04:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce09c4e4-fbb0-33c2-978a-189d490c001c | -10.57107 | -49.14558 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| cf6df3d5-1d33-3ddf-8d65-4edcb0ea6206 | -11.33191 | -51.44733 | 2025-07-10 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 914890c1-f706-357b-9d69-d6ed83a87ffc | -8.88887 | -47.33554 | 2025-07-10 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da6ab73b-a44e-31bd-9d16-77070db46363 | -9.29819 | -44.84209 | 2025-07-10 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3db33d8-f90c-3326-88fa-e192e35c747b | -10.66744 | -49.4644 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 720b535e-0f1d-32b3-87ae-8d8e623711e7 | -10.62426 | -45.22795 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4c5c5eff-5909-335d-b0b4-ba8e4a7ab1ac | -10.66124 | -49.46952 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1af4e5ac-3d3c-390d-8137-a6c91ef0e825 | -13.38632 | -47.8807 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc7c1c18-287e-342c-8e84-b0f0b314ed74 | -8.28096 | -46.31754 | 2025-07-10 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55ac6052-e62b-3679-ab6e-fee122d91c01 | -8.28166 | -46.31348 | 2025-07-10 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06250e39-5432-362a-ac31-58a057f83dce | -13.15376 | -47.2811 | 2025-07-10 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 852b46a0-57b1-303c-8ed6-b1fd91f82f2b | -14.84077 | -42.42127 | 2025-07-10 04:04:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df01dfba-684c-38a8-a439-08c93eec848e | -12.09812 | -44.73811 | 2025-07-10 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aac73e93-90d0-34f6-aa97-9921d727c504 | -8.50015 | -43.28386 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 256627ab-01c4-3ab1-8802-fc78804abcbe | -13.35407 | -47.78519 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a77715e6-3a1e-313e-ab37-9c5857f27f0b | -12.24572 | -48.80251 | 2025-07-10 04:04:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02568180-96a8-3d68-8978-d57140d23fd7 | -14.83893 | -40.90829 | 2025-07-10 04:04:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6a315160-c647-34b5-a98a-de5c1d9790a6 | -11.67152 | -43.78107 | 2025-07-10 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbc2f430-66b7-3864-a33e-1bd577a1f7e4 | -7.72677 | -46.61197 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ff6c70b-8d7d-32f1-9401-a38b205f046c | -12.98978 | -47.82822 | 2025-07-10 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfe8e08b-18d3-3326-9e7a-eec3e9fff9b8 | -8.5078 | -43.327 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| d0cd9a28-f873-33b2-9027-1088beda61ec | -13.63412 | -40.09999 | 2025-07-10 04:04:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f3b1e94d-aa9b-3a3e-ba91-ebb75a1a738a | -11.36452 | -48.70588 | 2025-07-10 04:04:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7c644b7d-44c9-3570-bbb7-4bd23453ff22 | -9.83048 | -41.49815 | 2025-07-10 04:04:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 47f288a9-efe3-3f47-b8ab-79b2caef0aa1 | -11.07949 | -45.8723 | 2025-07-10 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 715824a2-0dc3-3c69-b83d-9404651a314e | -11.90543 | -44.90957 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e4f3e4b-7c63-366c-bfed-001a2910ed8a | -13.34172 | -52.89413 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1639373b-8f6c-32a5-bb67-8db87b90ed1f | -10.9997 | -42.77864 | 2025-07-10 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5fd3c360-effa-3661-bf3b-40e9e9679d9c | -8.96064 | -47.27411 | 2025-07-10 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 20c4d1d4-6e6a-3597-b588-271f3a7e8877 | -13.38123 | -47.88382 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50a8f9c3-3d37-3765-9308-57e388b54046 | -11.82732 | -48.21725 | 2025-07-10 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efb965a5-0f0b-3881-b3ef-cc21bc9c7c08 | -10.65727 | -49.46246 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f970ef19-4137-35de-9b15-7d0243a02644 | -13.36999 | -43.75669 | 2025-07-10 04:04:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e4d098d-de09-32a3-9b4c-fa39093bcb5d | -7.64394 | -45.34694 | 2025-07-10 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8098cdbc-af5f-38d0-beab-6fa978a85bfc | -8.50384 | -43.31644 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 177d7be6-c1d2-33c9-bddc-bd1016555950 | -11.06667 | -45.87524 | 2025-07-10 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61f04e73-0de1-3e98-9872-d8b9f059dab7 | -10.96267 | -49.25079 | 2025-07-10 04:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96295bba-966a-3a42-ba03-ba33f00f868f | -9.21233 | -48.60101 | 2025-07-10 04:04:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49d808ed-f949-3741-a7e6-846dec09e734 | -8.47284 | -49.60281 | 2025-07-10 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ec75761-3a64-353b-bfef-d866e08b1ce2 | -8.50913 | -43.31884 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 5595e098-8210-388a-840f-3126489c2c73 | -12.56995 | -48.88145 | 2025-07-10 04:04:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48214d69-bb2a-3a3b-bf76-a109e4031311 | -11.3262 | -51.44617 | 2025-07-10 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f79c04e7-72f0-3b66-bb28-dc49e860a5a2 | -10.64614 | -44.48701 | 2025-07-10 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2307715-ac4a-30f9-95b8-ef93bd570b63 | -8.50604 | -43.3252 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 51b7d114-60cf-3906-a53b-2243e4ab614a | -9.21337 | -48.59539 | 2025-07-10 04:04:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa25e31a-94e7-3cb4-8a04-7f1e4e252e88 | -8.50887 | -43.29787 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| f6ea99c1-db64-37cc-ba45-c80b4525c431 | -13.29085 | -49.15558 | 2025-07-10 04:04:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e85022aa-089c-3614-a3b1-d9530e55b9b3 | -13.33786 | -52.91262 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50483f99-07af-311f-8821-6a9ede8919b5 | -12.1018 | -44.73874 | 2025-07-10 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a81ef046-4edb-37f4-95f0-080aa470a3b1 | -9.32263 | -49.22506 | 2025-07-10 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ac0bc19-4fba-38cf-9d45-9b1a57d5d444 | -8.50847 | -43.32292 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| b6c82913-a8e1-3775-b55f-bef82110a9d0 | -10.61648 | -48.07365 | 2025-07-10 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d376d028-493d-35d9-8b87-7e46c688942f | -11.83189 | -48.21815 | 2025-07-10 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30756729-acfb-36e6-8841-5e5d5bafd097 | -7.74725 | -43.59518 | 2025-07-10 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 327d5fc3-2959-30a9-998a-7e44a8dc7ae8 | -13.15868 | -47.27794 | 2025-07-10 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3865563e-dda2-3e92-bb23-7ffe9c791550 | -10.57316 | -49.13429 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a4811ee9-1854-37a8-b4ec-6545095da414 | -13.89625 | -42.13173 | 2025-07-10 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc10d002-230d-376d-b5ea-fbffe35d492c | -10.89559 | -46.73166 | 2025-07-10 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffc09634-1685-34f9-a562-d92e77003f77 | -8.50147 | -43.27575 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| c172eb4d-22a0-35a1-829d-584ae663765a | -12.47057 | -46.91141 | 2025-07-10 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40b463f9-b130-3375-8e75-8da45dcf89f1 | -8.49368 | -43.27862 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f243ea49-fe03-3e1a-a6df-4d3580e432f2 | -8.50821 | -43.30194 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| a5d7533e-6722-3591-821c-8467c0fc7226 | -7.46176 | -49.39962 | 2025-07-10 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c041940c-4ba8-39d8-9c55-f3235ab34893 | -11.9128 | -44.91131 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40bf6154-7651-38ca-8a14-e3ccb36156e2 | -11.87753 | -46.76122 | 2025-07-10 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03200b41-9d9d-3956-8eee-7917d3e25069 | -13.34099 | -52.92773 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15f33089-2ff2-3ea2-944e-4642f64d0529 | -13.3341 | -52.92672 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bc17d00-5be8-3b92-aef1-4c5e539ab95c | -13.90506 | -42.13347 | 2025-07-10 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7a0dba78-faa7-33e0-8960-217ba6752a03 | -13.87372 | -45.84386 | 2025-07-10 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5adb66d6-4ab2-3edb-abbb-dc526f198105 | -8.49974 | -43.30889 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| d4859f76-60b4-3f45-a8ec-8ee7b9240273 | -8.5053 | -43.29726 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| a3ec9b0e-acb2-3f06-861d-49cfc8f2b6a3 | -8.50173 | -43.29667 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| abbfb226-da08-3bba-8fbf-154852956d5d | -13.28988 | -49.16071 | 2025-07-10 04:04:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5787f1e6-a51c-3dc7-b4fc-80381bc504aa | -13.3439 | -52.91378 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ec46572-6f3c-386a-ada3-909de22a60ee | -10.61774 | -48.07697 | 2025-07-10 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b99d0735-ea47-39a5-b434-1b4c9797c3eb | -11.90911 | -44.91045 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f204480e-bb3b-3e5e-a64b-d73a1b5efc24 | -8.50438 | -43.28041 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |


[Clique aqui para ver as próximas entradas](README15.md)
