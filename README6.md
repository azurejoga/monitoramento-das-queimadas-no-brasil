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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf14493e-642d-3058-9a1a-a6d2750b76ba | -15.00792 | -46.58355 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91382e9f-cbd1-3b4d-9916-d6c0822cfd83 | -15.52371 | -42.66781 | 2026-08-11 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4add9b9e-a877-38f9-9dbd-d2713e76d3ea | -16.65866 | -43.63622 | 2026-08-11 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 32289ad1-bee3-3395-9a66-60c9d279c7b9 | -15.00133 | -46.58946 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5818b49-16c6-3c48-863f-55eeb59e2a17 | -6.31384 | -44.82596 | 2026-08-11 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3f68618-1452-33de-b2ae-6d19793c6ab5 | -14.12013 | -45.61705 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baab2463-91f2-3830-8813-625104769952 | -12.47292 | -45.3429 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fe2cbb0-dbe3-32d9-b692-99bd1f4c56e0 | -13.38188 | -41.33747 | 2026-08-11 03:49:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 067f3f08-f412-3a1e-a4e9-8362141999b1 | -14.28062 | -45.30159 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce9906fd-07e6-35a7-8427-6efe9397a110 | -14.45183 | -45.69265 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9158143c-7421-3fd8-bf9e-a5e185297650 | -17.9975 | -44.37242 | 2026-08-11 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b5b96552-6b20-37ee-9fb7-4d4dda9592b9 | -13.5591 | -46.3104 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc8db5b2-90b6-32b1-af9e-d6f7814102c6 | -14.4568 | -45.6937 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 91c9124d-37a3-3110-b9f6-8d283d90e07c | -14.64114 | -47.65219 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23e3d082-6c3a-33bf-9235-233b0cf8f950 | -13.56771 | -46.29461 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db215009-4216-30c5-ba04-d37de76988f2 | -13.6012 | -46.31909 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a009a1de-4209-3599-8b26-e59a806f9fd6 | -12.11908 | -43.21532 | 2026-08-11 03:49:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 848f5a9e-fa74-30f3-b356-3051dd8c4761 | -15.51969 | -42.66703 | 2026-08-11 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2e8a8194-f132-3680-8980-da5bb8217914 | -12.45719 | -45.34301 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40896b5a-5b46-32f4-89fb-684b9bfb3fdd | -17.03709 | -45.89656 | 2026-08-11 03:49:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73c8b393-8a06-368f-b522-467f0198fbaa | -6.31448 | -44.82231 | 2026-08-11 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d14b45c-f5ca-389d-90f0-30315fe42f42 | -12.4932 | -45.29136 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd5c3529-5c19-382d-99fe-820fecbd1dea | -11.46757 | -46.65417 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd2f433b-214a-3741-805a-dcbaaf5bd4c5 | -17.45808 | -47.14757 | 2026-08-11 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18c221f5-b10c-3fa1-843f-d6b9d1f17f55 | -12.48594 | -45.30205 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 7cd3b2a8-b5dc-347b-b42c-09038abc2a4b | -12.49878 | -45.28942 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| f3aead52-f0c4-3f6b-a300-04bfa6a4e246 | -10.41844 | -46.67752 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ca02c7e4-782c-3c98-9e7f-899d459bc408 | -11.45093 | -46.67994 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7a65c78-d8ea-3cc3-a795-5ac2c17fe36d | -14.27466 | -45.30615 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc6840d6-c64a-3b0e-b224-cf561e64eb7b | -10.42567 | -46.67054 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3f886496-b062-3423-988c-2df349e4ae0d | -14.62837 | -47.65731 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 51c5aef3-a5ac-34db-a5fa-ac7416c3f4a2 | -13.5545 | -46.30596 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59188963-7e4d-37e2-9e66-0ff6a86ced10 | -15.00693 | -46.5881 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63750d4d-2cac-360c-886f-746103346beb | -12.4814 | -45.32588 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 515ea011-0c2c-3cca-9b02-4c411a01fdc0 | -12.3528 | -38.77598 | 2026-08-11 03:49:00 | NOAA-20 | CONCEIÇÃO DO JACUÍPE | BAHIA | Brasil | 2908507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 146bb7cb-3f87-3bd0-8a97-9e190e473db9 | -14.12158 | -45.63601 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2e3aedc8-9173-39de-a6b9-2413485b1982 | -12.4634 | -45.33795 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e04ec7d0-703c-3046-827f-2af2ee9bc9ad | -15.00661 | -46.59028 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bac95b3-b9b8-3b31-9455-f7a3d075bb06 | -12.47464 | -45.33389 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| df2a02aa-b734-3b14-909f-3001d4301257 | -12.19123 | -40.40619 | 2026-08-11 03:49:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9db665a-d136-3093-aecb-40db59a84145 | -11.95077 | -46.3356 | 2026-08-11 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d673dfd8-ccb6-3ddf-8b72-e0cdb28af060 | -15.02736 | -46.56779 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 811dc56e-a36b-3519-ae96-91c0fd746997 | -13.5743 | -46.28894 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 960abf9a-8b77-30d9-9919-b00dbbe8b835 | -10.41121 | -46.6844 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bc81b65a-3e6a-36cf-83b4-8c533af584b8 | -12.46007 | -45.32805 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54d7f33a-0a6f-3dfb-a6aa-c864b7c99371 | -13.39189 | -40.06054 | 2026-08-11 03:49:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e3de1fd8-9731-3e18-be8f-973002a9cc47 | -6.0058 | -47.40943 | 2026-08-11 03:49:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa5da209-03c9-365a-a586-6ed613326da7 | -11.45169 | -46.676 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 465f41c9-677b-3fde-b29c-b2873db9c860 | -15.75691 | -47.77152 | 2026-08-11 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15d14fdf-9247-3deb-9fcd-e01c5b86bed7 | -13.57371 | -46.26437 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 169e2c27-eed2-34a8-85ea-4653d6ed4ffe | -12.48529 | -45.33289 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 6069ada5-3b1c-3d3b-80d9-a2ea0b3ceec7 | -11.25713 | -44.89288 | 2026-08-11 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b976e80a-9bcc-33f4-962d-6f289b904a63 | -14.45938 | -45.68055 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83df5411-2636-32a6-9a62-061915b3f23b | -11.47092 | -44.57235 | 2026-08-11 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a71f02c-5517-3e0d-be5c-4ab7b8a89962 | -13.56905 | -46.28786 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afeb7ff0-933d-33a9-b707-1f6dae9e5a7f | -11.46116 | -44.57045 | 2026-08-11 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5484d0d-9738-3ce3-b8fb-27c7105f5878 | -12.4657 | -45.32597 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82ac3ed0-23f3-3742-adf0-b6f6a60acb1e | -14.99352 | -46.60155 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 756be02e-5009-3697-9ce5-b749cdeb1dbf | -13.56849 | -46.26315 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 77d55b3c-1a85-38b3-9da8-a78e177a1a4b | -10.42262 | -46.68669 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c145c408-01fe-3bd6-832e-6f96f32bab22 | -15.04543 | -46.55892 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c350b3e-60a5-3c86-aab1-079ca762822d | -12.49488 | -45.2825 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3d947e2-2a64-330d-9941-ee7f744ff861 | -17.45297 | -47.14618 | 2026-08-11 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e103b6aa-44d7-3f59-ae4c-592bb9a37499 | -10.41767 | -46.68156 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bbfc0da8-d9b2-3b9a-a0af-5bb2e37c9514 | -12.49043 | -45.27851 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bed6203-a976-305d-986e-f5ee117a157a | -12.48538 | -45.30501 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| bc246b4e-5d95-339b-90c0-d40349ec1de0 | -13.56838 | -46.29123 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0652e7d8-3d5f-3be8-819a-1906df55a19e | -11.46802 | -46.62201 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a71cdc0-ff51-3519-b6e3-3d6dbc30c8a5 | -6.00723 | -47.40691 | 2026-08-11 03:49:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b63394df-7952-38bf-8f62-8ee61182ebdf | -12.47808 | -45.3159 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7fed0d6c-64e3-3abd-9e68-336e56e90285 | -14.46119 | -45.69767 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 49e56d91-3ec5-3a9f-8dc7-7574f7e0b911 | -14.45508 | -45.70246 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 638bf2f3-d5b6-35c7-b336-ed605d901e8b | -10.42645 | -46.66643 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 477dffd4-fe61-3eb3-a1d7-982d12039c1c | -14.27952 | -45.30716 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b981fda7-8812-30a3-a315-247d53df82a2 | -12.47017 | -45.32991 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| ef789db2-7362-3f33-ba71-a69915f5806e | -10.43412 | -46.6357 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24c4eb91-307d-3e28-a040-31178015baf4 | -17.04186 | -45.89774 | 2026-08-11 03:49:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0edb527-6032-3d16-9ad0-03b5aebff15b | -16.89386 | -49.37835 | 2026-08-11 03:49:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4e74a20-997a-3356-8b0f-3c3125df2e63 | -4.25932 | -48.19984 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 381d6ef0-794b-30eb-8232-cf00fb499f5f | -12.47636 | -45.32488 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 04bab932-70a4-3c09-a26a-9e84ea529d3d | -4.2697 | -48.18188 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fb34f3a4-1a51-3a8b-8689-3a5045858379 | -14.46502 | -45.70457 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b11e543b-e77c-35a1-9b5b-09fc4b94538d | -14.62763 | -47.66091 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4ca41e4b-f6a8-3ff1-9822-04daf0fe7a7f | -10.43961 | -46.63783 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54609015-5ad9-3979-a764-387c9d5d8103 | -12.47796 | -45.34391 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b89f02ff-5036-3efa-bc8e-f2a42479f837 | -10.41751 | -46.65124 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fd195aa-0d78-3a12-bfcd-a46cb49d471e | -15.00859 | -46.58011 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91aad8e7-7b3c-36d5-9d04-16e966d95073 | -14.46005 | -45.70352 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb63065f-25d3-3dcc-a816-cf4ccb0366c4 | -18.00104 | -44.37718 | 2026-08-11 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c223f847-93ee-3892-876e-c74533e426f6 | -13.64603 | -46.25708 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46adc76f-f2a4-31c0-ac02-0f183824fee6 | -4.25991 | -48.20017 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1a3e51b0-9f0b-3c7e-9796-9fbb304b0274 | -12.46455 | -45.33197 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c4c4ba0-e3ae-3082-880b-acc5bf3f8d25 | -13.57417 | -46.31725 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e14ce686-e0d1-3195-a749-79b672e9512b | -10.41994 | -46.67769 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 031f2e16-b39a-309b-b1ba-1d45bcf5b2bc | -14.46616 | -45.69873 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43c9adb9-ed34-3257-be70-91da33bf0c41 | -11.02367 | -45.64253 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3df7cea8-3883-3e11-858e-c4f72a95c189 | -13.56177 | -46.29692 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a298ff0c-b411-3484-a251-338e4934add9 | -13.64796 | -46.24709 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7c9615c-78ca-304e-b932-dd590d68419d | -6.00677 | -47.40399 | 2026-08-11 03:49:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca96c306-bb92-3f33-b268-912503b53fd3 | -4.26216 | -48.18722 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |


[Clique aqui para ver as próximas entradas](README7.md)
