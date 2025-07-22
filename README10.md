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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 832748a3-bd61-3775-bc0e-66489394b64a | -8.50958 | -43.30388 | 2025-07-22 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3dca911a-21e4-31b3-8cc7-f7109d88f2ce | -12.47493 | -45.86966 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19412a05-95f7-3c12-a6de-916020dfca90 | -11.76949 | -44.3043 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca8f33b7-4521-346b-85f9-03948109cb38 | -13.61888 | -47.7335 | 2025-07-22 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4733de4-d6d8-39c3-a7f9-ef7060cc67d5 | -9.63272 | -40.59197 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a1a44f6f-5207-3b87-8b29-d45e24580514 | -10.61866 | -45.23 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f17646e8-24af-30aa-b410-0fa505b4086e | -11.73147 | -48.18044 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 01252c98-4bfb-3847-9e22-8a283e43a4c7 | -13.68747 | -45.68512 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| decd48ec-a62f-3a9f-97d3-f146f9351dd0 | -14.59439 | -46.38867 | 2025-07-22 04:02:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c214baba-e913-3719-be58-b912d4fd900e | -11.73435 | -48.19044 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a99d5f0b-5b07-3aad-961c-e395934347e1 | -12.68533 | -45.65988 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 398aecaa-8108-3b7c-af74-4222bd577473 | -11.95891 | -47.02551 | 2025-07-22 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aedc695-a745-3a3d-b46d-0bf20d1fb957 | -12.71516 | -47.79575 | 2025-07-22 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af790098-2979-3e0a-b07e-5471d4684479 | -15.61125 | -41.33739 | 2025-07-22 04:02:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9ec6e17-20e0-3f4a-9a27-262964f599e3 | -15.9301 | -43.51959 | 2025-07-22 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e26e8cc1-60c1-3e64-9e36-a12c617e240f | -13.66503 | -46.53164 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a8a1026-f019-3659-a2f1-e2974e22bb0a | -11.73599 | -48.18129 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c0c4c4ae-138b-30a5-b37a-ea92a5e69bbd | -15.61457 | -41.33794 | 2025-07-22 04:02:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 50b147e1-0229-34d7-9a29-e68029fda171 | -8.91478 | -47.3623 | 2025-07-22 04:02:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b731f62-7b9f-3d4e-8288-1fe6873561e7 | -9.62942 | -40.59145 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c82ad93-6e5a-3838-a8f6-d43c9381a1db | -8.91109 | -47.35697 | 2025-07-22 04:02:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08633051-12a8-31b4-91e2-5e1e19f10720 | -15.92811 | -43.52032 | 2025-07-22 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 070575c5-4f31-3939-922a-3d8d9848c9fb | -13.43337 | -43.4783 | 2025-07-22 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f44923c6-3c6b-39b5-b89b-25abc97b6a0b | -12.65764 | -45.05578 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd230145-3d2b-3d91-96a6-d4c7b0f0c3cc | -9.5694 | -44.50316 | 2025-07-22 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3c37e01-998f-3021-b00c-9849f9d8fbe4 | -10.62547 | -45.23611 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eab0070a-1d9d-38aa-ab14-15be543ff732 | -11.72613 | -48.18417 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 21b3d9fd-ccdb-3327-9274-30508647d1ee | -9.49799 | -40.56303 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16b930d5-baf7-3a4b-b3fb-361fa07a5332 | -13.68906 | -45.67589 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f830226e-f9e2-34b8-8539-ddcb146852ef | -8.29006 | -44.96101 | 2025-07-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41605b34-a6d1-3f1d-a97c-9236607446e4 | -9.49745 | -40.56651 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f26262a7-8413-347e-8dad-7117c96cdb55 | -8.92547 | -44.45062 | 2025-07-22 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05c40d53-b949-35d4-8a59-55656ba46c4d | -12.47409 | -45.87452 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74b213c4-34dc-3ab3-b935-ffa1f63374ec | -11.56686 | -44.25862 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f58c9c3f-b856-3b95-b59c-f44121f2e26a | -13.36654 | -44.77448 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80b17adb-22f3-3c91-9d3b-3a7a5a2dd8c5 | -11.57177 | -44.84182 | 2025-07-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4022e5f8-e57e-3188-9eab-e40806dcdaba | -13.70005 | -45.7017 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 756fe5da-8bf1-31ef-877f-7db31cba4ab4 | -9.33313 | -37.98163 | 2025-07-22 04:02:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31c486ad-4cd0-3a6a-85e2-bba658842f6c | -13.692 | -45.68119 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a0a5a4e3-b3b8-30dc-ba6c-4b5d93047325 | -10.77447 | -42.71762 | 2025-07-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 15e984b8-fabc-37fa-9ded-cfdd01651fc8 | -13.68453 | -45.67982 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 46e1e2ff-271a-3fbe-81bd-872fdcad091f | -14.74711 | -46.29824 | 2025-07-22 04:02:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36ad8549-e407-342f-8a16-de2a137fb06f | -13.65327 | -45.72671 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3eb4ae2c-e4d0-3a88-a3c7-7b5a9e73b96f | -13.61812 | -47.73768 | 2025-07-22 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1496c9dd-89e3-327b-87e6-0b0a5131aadd | -10.61405 | -45.23412 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f64f9a3-0fbc-3838-8294-6892cda3b33e | -9.06615 | -45.06062 | 2025-07-22 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47d2c36d-7fbc-35fb-b8eb-dfc21b214948 | -14.38385 | -47.76257 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e195924c-154b-3ab7-abed-6034e805847c | -14.38115 | -47.75354 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b70b542-9eaa-3650-87b2-e2ca406905c0 | -8.09968 | -46.82635 | 2025-07-22 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d60a2cf2-bddc-34fa-8749-08c1452644bd | -12.63222 | -47.12605 | 2025-07-22 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9acaf1d3-c80b-3724-8e77-4dddc63dd246 | -7.87545 | -47.7543 | 2025-07-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14a5f96b-e5d7-327b-9715-0ecf18899e4d | -11.95767 | -47.02561 | 2025-07-22 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d260687-d6b4-39fa-8579-12cd5f8c44d2 | -11.56733 | -44.84556 | 2025-07-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ea9746e-7f8e-3d95-be1a-80ddf00468c7 | -11.56876 | -44.84333 | 2025-07-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d688b84d-059d-3889-9558-b8eb1acf7a08 | -9.59359 | -43.84959 | 2025-07-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc2a3373-951a-3a21-80c2-04cd93733492 | -11.19031 | -48.61567 | 2025-07-22 04:02:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8379eae8-6705-3c7d-9af3-2dd167ca216f | -8.92766 | -44.46027 | 2025-07-22 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7926cc64-88ff-3bae-a962-4f79875a9706 | -14.74627 | -46.30303 | 2025-07-22 04:02:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 937b685b-4b02-3867-adfd-66980efc43e6 | -12.63636 | -47.12684 | 2025-07-22 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 659e98b4-0a21-341f-8752-ee632db9285b | -12.65475 | -45.05068 | 2025-07-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a6cc51b4-7262-3f14-97a0-fb130cf89374 | -10.23297 | -48.06755 | 2025-07-22 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b3abab8-74e0-34d3-8a5a-fb33c66d0a33 | -9.49029 | -40.56894 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f278d894-5ae7-3e93-aef8-0ec83f3bb71d | -9.63218 | -40.59545 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c97c6155-8493-374a-b2c8-3f1b49ec7040 | -8.2925 | -44.96448 | 2025-07-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 214207bd-124a-3815-9c7c-cb821652cf86 | -11.90783 | -44.06752 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64c642eb-302b-303b-933c-2a677f14b635 | -9.63548 | -40.59598 | 2025-07-22 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| fcec2c98-72c8-3a61-abfb-f7ff83a83269 | -9.60871 | -43.86922 | 2025-07-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d02fbb4-ced6-3ffa-9c27-c227e1a5e618 | -8.51664 | -43.30506 | 2025-07-22 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 4d9af85b-6faa-3d98-b704-3314fbf933bb | -9.06533 | -45.06543 | 2025-07-22 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8d244ffe-20c0-3ece-8ec6-c55f033ef6ad | -13.64951 | -45.72605 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| db1791ec-a39e-33dd-925c-d3a7605201bf | -8.37513 | -47.61924 | 2025-07-22 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fae10365-c18e-311c-b7f1-05d0062b48b7 | -14.76412 | -47.1152 | 2025-07-22 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98028c53-5e65-3ae8-a5ca-451876d7987e | -8.91028 | -47.36153 | 2025-07-22 04:02:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1e03c82-03c3-397d-868a-017429713b5b | -14.77802 | -48.28845 | 2025-07-22 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 527d6be4-c30c-3950-82e9-a94f6482647b | -14.38273 | -47.74486 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62e05724-2b81-3455-834b-4a8a44208f08 | -15.93345 | -43.52018 | 2025-07-22 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 23547f6e-f510-3390-94f2-46d76d15c40d | -14.77455 | -48.28319 | 2025-07-22 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a673a6e-2b72-3aed-93b4-869e3834d13d | -11.72696 | -48.17959 | 2025-07-22 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 253184cc-dbbb-3003-95c7-8f9cbb49d81a | -11.19408 | -48.6216 | 2025-07-22 04:02:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aff402b0-3c89-3099-b0f3-516f62f6d45b | -10.6295 | -45.22935 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f28b7d2b-ea33-3401-a629-6677e8276c72 | -11.71822 | -47.77414 | 2025-07-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34e9164f-f61a-3f98-969a-c16f601ce76e | -13.68373 | -45.68444 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 658a0946-598a-3a77-a22f-c8f2760b087f | -11.57244 | -44.84398 | 2025-07-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b3652d2-c07c-3726-92c8-1deedb91126c | -8.92393 | -44.45966 | 2025-07-22 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e91ac579-37d8-3c8e-af1b-aab6ce5bc886 | -11.96308 | -47.02628 | 2025-07-22 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4f299c9-1616-3adb-b4c0-ad40fe54f151 | -13.65783 | -45.7227 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 85f4a82b-72f1-3c1f-b8ba-7190af85e4d3 | -10.68269 | -46.76322 | 2025-07-22 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f61f0742-3986-3a28-9a49-b62e3b92e655 | -11.75779 | -46.29578 | 2025-07-22 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 598851c0-fe6e-3f22-b5b0-7222b81a0263 | -18.64679 | -47.92195 | 2025-07-22 04:04:00 | NOAA-20 | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05e9d071-ebd5-3822-ae93-7c459d098b03 | -18.99542 | -45.78344 | 2025-07-22 04:04:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f963887-756b-3b8d-92d4-3ae993a05f20 | -21.01817 | -56.00629 | 2025-07-22 04:04:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdb9d2aa-81b4-3d74-806c-541f5802d13c | -18.47675 | -44.35757 | 2025-07-22 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31584b4a-5204-3b1c-93e9-b42666fef307 | -18.9947 | -45.78762 | 2025-07-22 04:04:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4b87516-7e26-39ad-aa64-f2cee315a191 | -21.34482 | -48.67539 | 2025-07-22 04:04:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 482fc2cc-87fe-3dc2-b101-d98321f17a58 | -18.61524 | -44.26203 | 2025-07-22 04:04:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a636a2a-7235-358a-9bab-137c600d53bc | -20.06102 | -41.40107 | 2025-07-22 04:04:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 5497c4bc-93df-313e-a595-1a23e2de21e0 | -21.34306 | -48.67647 | 2025-07-22 04:04:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 80c163dc-ad1e-3a76-84c7-82da32c68d5d | -18.66071 | -55.72422 | 2025-07-22 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fdfdc632-9800-3385-ba09-33d04423bbff | -17.98449 | -46.00138 | 2025-07-22 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fd6e8a4-bd62-37c5-9656-0068b7dba9b8 | -16.64486 | -40.69017 | 2025-07-22 04:04:00 | NOAA-20 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README11.md)
