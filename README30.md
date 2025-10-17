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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7263a1b2-eb5e-36c1-8bdb-be8199ad5d52 | -11.47395 | -44.28143 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 366b8b9e-7ef7-3292-bcc3-c78a5f37f7d2 | -11.46645 | -44.25589 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 853a4cd8-49bc-35c5-b916-c3f260e612dd | -11.47939 | -44.29182 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42f0f3bb-a8c2-3274-9077-ad81e26a4bab | -11.27347 | -45.29531 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4767d485-08d0-32bb-a329-f69f5a8ece77 | -11.45061 | -44.20964 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0738232-266c-3a37-b06c-c604dbe4f799 | -9.26332 | -45.27509 | 2025-10-17 03:30:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce797c8c-3949-3f46-b74d-9344e30bf9dd | -11.5251 | -43.49866 | 2025-10-17 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f8034b3-b72a-37aa-b10b-b7284843c6f3 | -12.9094 | -41.85241 | 2025-10-17 03:30:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 67218d09-a6fc-3f74-9474-75a2589716b6 | -11.39537 | -44.23603 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 35a12206-0eb6-3e39-8bff-9e0c891783a8 | -11.48032 | -44.2872 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e86ce815-607c-36d7-a767-1fa10fd98d11 | -11.58697 | -44.06514 | 2025-10-17 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bb21f8d0-5070-3c8c-ae50-98a32af5d14b | -10.5365 | -44.50631 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47b9f682-a0ee-3f48-9b07-136f65d9b544 | -11.46487 | -44.04399 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bbfd1cb4-8681-306b-b5f6-60a260f9dcdf | -11.44245 | -44.25078 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f96eb153-1e62-3043-bc3e-38a5500b0346 | -10.49629 | -43.4196 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2a598c6f-f289-3420-8ca4-9d0b41d61a7c | -10.11852 | -44.55991 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdd19509-1823-342e-94e6-62d800de2c42 | -10.81739 | -43.93761 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c2b53b3-120d-36f5-ae6f-e13b44784f6b | -11.39952 | -44.23823 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| ea5fe72a-e109-3ce9-b115-c510c017237f | -10.26917 | -44.02802 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f968d95c-2948-3247-b819-24facf65cbfa | -10.4269 | -45.02764 | 2025-10-17 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9a102216-caf4-37be-8f44-eff0a1b87ca1 | -10.50208 | -43.42077 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cce6849-dbd9-3adc-acfd-576aaeb58819 | -10.28727 | -44.03189 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c44a1dd-170b-3526-85ac-440e8b064e22 | -10.81325 | -43.94043 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a393c5cf-2a94-3300-9b51-7019d3fc063a | -10.27347 | -44.03814 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8288d374-26b0-3a4d-80e8-6df0557322c7 | -11.46225 | -44.24547 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7cfdbb4-e84b-3709-ab08-b37d7adfd1d5 | -10.50028 | -43.43008 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2859912e-828b-3374-a8bc-6fd341caa233 | -11.45983 | -44.03833 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dbb39588-4eb0-348a-83ec-7e737892e3e4 | -14.15437 | -44.31606 | 2025-10-17 03:30:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 809afb34-ea65-3305-b308-7a26d0353a4c | -12.9086 | -41.82907 | 2025-10-17 03:30:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 51fc5302-087f-3ebd-99a2-ddad848e914c | -11.48258 | -44.17381 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7b58616-c93c-33c5-81bb-460320718cbd | -10.05481 | -43.86295 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b276c4c9-9655-3ff9-b90e-0203af0c76ed | -10.49735 | -43.41413 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e9a4c8f5-07c3-3a82-a64a-ff4180bec5c1 | -11.97418 | -46.5681 | 2025-10-17 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 190e8247-d103-3c19-8ec6-0c0640669090 | -11.40749 | -44.19707 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 46f5b62d-42fd-3f1b-930d-1208ccbac90b | -10.14148 | -44.5428 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da5a75f1-1af3-3664-8ffe-21b1ad80181b | -15.28988 | -39.66336 | 2025-10-17 03:30:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c60444a5-f3de-3b34-968b-18bee51927fe | -10.2622 | -44.03149 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51eec731-2263-3c67-87da-55cba18e3d04 | -12.61982 | -43.43662 | 2025-10-17 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41dccbdf-3561-380a-b0dd-4fbb7f72ed46 | -10.1496 | -44.53472 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d9e988a3-85f8-3835-83f3-a751f72741ae | -11.47043 | -45.08926 | 2025-10-17 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f5e1436-5173-3e0d-9a0e-bc2a70c55994 | -10.1447 | -44.54198 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f7e5ad0-84f2-307c-9dd6-9c2ec994f9ba | -11.44789 | -44.22335 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c35196c-394a-30a9-9d53-4b7ceffe80da | -11.45083 | -44.27168 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5fa025e-1084-3c38-89f5-c37d1ce4c642 | -11.41259 | -44.20293 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c6a7d861-baaa-3b38-8562-8e63ab6bedb3 | -11.47215 | -44.19522 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 836c41e7-e5e2-356c-ad8c-8eb742de2c8d | -13.82427 | -42.35088 | 2025-10-17 03:30:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3294d79-ad81-3cd4-92a8-d7949b79fa65 | -10.50694 | -43.42681 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c509f94-b539-3be4-a52a-2928be1feaa7 | -11.37758 | -44.19065 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fe2ff96-ed88-3738-9f8f-389dae8b87e3 | -13.27306 | -44.4879 | 2025-10-17 03:30:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 367c0e4e-c476-3201-b3ad-be396ddd803f | -10.08031 | -45.34681 | 2025-10-17 03:30:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 389a95a1-9052-362a-87b2-acd1356a992f | -10.28439 | -44.0466 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e0c0c5ce-ed43-377e-b012-6eb0d182f646 | -11.40229 | -44.23273 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4620fc8e-3db0-35f2-aa17-a5569a5ccdf8 | -10.1269 | -44.55059 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c644491-59bd-3c6e-8959-d70b2d608d90 | -13.92184 | -45.62356 | 2025-10-17 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95ed1681-9247-307c-bbb4-93edd4520413 | -11.4064 | -44.23494 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3d895d51-f3ac-35da-b98b-7f853718995e | -11.47036 | -44.20433 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47a93444-6996-371b-b0ee-031f767ae49c | -12.91416 | -41.82721 | 2025-10-17 03:30:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7abadc2a-8792-3b63-95f4-d42f6e8f8cab | -11.40181 | -44.20407 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| ecd267db-8a84-3898-9f53-b66f83c0e439 | -11.40151 | -44.19579 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d7f8254-57f3-3094-a316-3649297ee66a | -11.39642 | -44.18993 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 933fa66f-6382-3e37-9663-321dc3224ed1 | -10.25662 | -44.05714 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51665002-8981-3801-95f0-96f7beab360a | -9.12685 | -46.63366 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1623a7f6-f2e7-3372-b161-ec68b55e1f67 | -11.5259 | -43.49464 | 2025-10-17 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14b8a4db-ae0b-3edf-a17a-8463bff54b1c | -10.50608 | -43.43126 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3450ae7-8dec-3fdf-bc23-a23b74c4fb74 | -11.39108 | -44.21737 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 18abbca2-51c9-3dc2-8d09-720bdb57173c | -9.14516 | -46.65396 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0113c515-a925-339d-9dea-5fc57ce13375 | -9.28366 | -45.38176 | 2025-10-17 03:30:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c710c18-4b6b-31dd-9f49-dfd4e2163be5 | -11.40573 | -44.20619 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 612ec5de-c3a3-353c-acd2-3afcfa797efb | -11.39674 | -44.19826 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b34959a5-b5ea-3208-ac64-988bc3349d45 | -10.10459 | -44.62904 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 731b3fe0-c16f-32c7-8987-c003ee058ae7 | -11.49274 | -44.0591 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aeb9746f-e626-3121-bcc0-ca54d4d1909c | -9.24775 | -44.36437 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eff1a3a9-dae4-3da9-8e7e-1ca2fa3f1724 | -10.29335 | -44.03293 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a298e94d-d560-3a28-9047-878ac6dac335 | -13.71303 | -40.99023 | 2025-10-17 03:30:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7c093f80-f8fa-3fec-9b5f-5169f9551e62 | -11.58609 | -44.0696 | 2025-10-17 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7ffc4a80-bc8c-3f34-8ab6-3aacbbf3804f | -12.13164 | -42.15605 | 2025-10-17 03:30:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0b1f7c4b-ea5c-375d-82ff-32f45528ad64 | -11.41103 | -44.22032 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62abab5c-32e5-3183-b448-a73ad0a3c313 | -10.12295 | -44.55361 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ef73ccd-cac7-3579-a3b3-59f34b261189 | -11.38799 | -44.21068 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be0e7653-ce11-354d-b92b-bfeca3abcaef | -11.38107 | -44.21399 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 868d80a7-1e5e-3767-81bb-05dedc70c791 | -11.39441 | -44.23237 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4ccd9e19-4072-3b41-81bc-ddd5febca163 | -10.28327 | -44.05235 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0035686d-097a-3a01-8e15-0d320ebe6389 | -10.49859 | -43.43876 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8260448b-0135-3a54-87ca-c93ece804261 | -11.49187 | -44.06356 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5534af8-97f3-3b6e-a077-14e2e9411357 | -10.26743 | -44.03689 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9222300-82fd-3182-96ab-4ee2093de033 | -11.48411 | -44.19774 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c32d2c94-ce46-36fc-8902-d9ae8e757aa5 | -10.27437 | -44.03355 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cbfc1b4b-90b6-3545-9761-7c669162cf7e | -11.46943 | -45.09418 | 2025-10-17 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd50e2c2-7d63-35c2-8d2c-f6549ed8150c | -10.05221 | -43.83606 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| df072a4a-fe30-33ac-94ac-4b1b1992ac0a | -11.41194 | -44.21577 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1fbc5d3a-0583-3870-931f-d058af64a50a | -10.25752 | -44.05243 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 729bdd79-7c25-3f06-9476-21f6369328fe | -11.96737 | -46.56664 | 2025-10-17 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1078d97c-e278-3b82-867b-6486d39e9cb2 | -11.38598 | -44.21149 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccc739ab-d9ed-3fe4-b9c3-14ca5b56f143 | -10.16005 | -44.5475 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5f584c33-20e5-342c-b5f3-393f9d886a0e | -11.46465 | -44.26506 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e250dd57-839e-35bc-bce9-ce5fe1ad7645 | -13.27663 | -44.4879 | 2025-10-17 03:30:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 993603b7-cebd-33d1-bea5-ac07108b3592 | -11.4817 | -44.17832 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84c5942e-990a-36b9-bdfe-8ae8d64294ba | -10.15793 | -44.54073 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bc878a4b-a091-3d3b-83a0-aef083068d57 | -11.59356 | -44.09429 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d0a44fb-5ee2-34af-b340-95770a5b7eed | -9.23953 | -44.37309 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README31.md)
