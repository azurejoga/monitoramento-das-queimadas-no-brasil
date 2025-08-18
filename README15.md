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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cac848c-d13c-3cee-a19d-6e01b9281ad3 | -18.61416 | -42.44112 | 2025-08-18 03:57:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 01647b87-2d4a-3c35-a0b3-b93df8a71696 | -22.19639 | -56.04191 | 2025-08-18 03:57:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edbf6148-255d-3862-9d4b-c93f906dbd35 | -22.13631 | -50.02667 | 2025-08-18 03:57:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3585299a-32aa-377d-9087-e73781c92aab | -19.15216 | -47.03833 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e7c19e2-095b-3f59-82e2-f36264c5b12e | -20.00884 | -46.4365 | 2025-08-18 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd7b711c-b2a6-3ffb-a122-7859093747a2 | -20.21828 | -47.03846 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd5f3845-b7b9-3734-94bd-2df827720668 | -16.79127 | -50.09834 | 2025-08-18 03:57:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89611686-1d73-3112-beda-0dedba217aa6 | -14.97723 | -54.77138 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0af04c82-70fb-316d-890d-df44e4f23561 | -23.06952 | -45.60973 | 2025-08-18 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 2323ad34-732f-3322-971d-0d0b2ad7fe96 | -21.79077 | -47.55486 | 2025-08-18 03:57:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d4051de-c1cb-3988-bac7-35e7f433fcc9 | -18.61478 | -49.19624 | 2025-08-18 03:57:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bb46bccd-5ef1-3503-97be-7b5e6e5b7766 | -18.25562 | -45.16128 | 2025-08-18 03:57:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a95bf639-4bbc-32a5-bd91-1641d3c77dc5 | -17.09668 | -49.87886 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4fa1e6b0-dda3-34ca-8fe9-aeab5542b31d | -22.21324 | -49.75108 | 2025-08-18 03:57:00 | NOAA-20 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 992f3d24-9c93-36fe-882d-07c0d4b9bdcd | -19.54107 | -45.61515 | 2025-08-18 03:57:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4ddbe91-83fa-3948-90ab-cfb37f54ec10 | -22.13964 | -50.02587 | 2025-08-18 03:57:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e7f7f2cc-1da5-3915-96e0-2ec572b9313e | -18.61356 | -42.44484 | 2025-08-18 03:57:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 82b92edd-2237-34f9-9554-2322f0e25ac1 | -17.39244 | -49.22552 | 2025-08-18 03:57:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70fb47df-32c7-3d7e-83d5-ecfafaa5b34f | -14.97753 | -54.78693 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 72d71932-98f0-368e-9e57-3985fc52030e | -21.27525 | -43.88494 | 2025-08-18 03:57:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f3b16b1e-8c33-3a43-996d-34a9fd7d40e1 | -22.21429 | -49.74599 | 2025-08-18 03:57:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4b27a500-56d6-3e8a-bbe2-bc75cc0ab19e | -18.0448 | -43.81732 | 2025-08-18 03:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a1e7dcc-88dd-30e0-940f-0667a102d953 | -21.04194 | -43.74785 | 2025-08-18 03:57:00 | NOAA-20 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e478bbd0-f835-38e4-9e4d-4eaea66a7cf5 | -18.64305 | -49.97143 | 2025-08-18 03:57:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e6a127e2-6de9-30f5-8625-6e14deda4ed1 | -20.08932 | -41.56631 | 2025-08-18 03:57:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6a520997-bc8d-3d30-b8ef-2bfce6b10104 | -19.14807 | -47.03748 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dab25ac-884d-35d7-b0c9-6b6e1d539892 | -14.98646 | -54.79573 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dc438627-1735-3743-b314-66f18b7d02ba | -23.07309 | -45.61049 | 2025-08-18 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61b20143-0037-3df7-aaee-cba51b476400 | -20.34844 | -45.3072 | 2025-08-18 03:57:00 | NOAA-20 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 9cdd2c0a-eb38-38ef-a8e5-6ac6d464196f | -17.38715 | -42.62709 | 2025-08-18 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7e1a9688-c946-336f-a8d4-a8a3d346c464 | -21.17301 | -45.12981 | 2025-08-18 03:57:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 91fcbd75-2b03-3f42-ac71-cf99d8a760eb | -23.01506 | -46.24785 | 2025-08-18 03:57:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 950b6593-a579-391c-9a43-6333ec4261c8 | -20.2157 | -47.03011 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2614952b-0612-3e49-b8cd-83d2675ce82e | -17.09094 | -49.88099 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bb80ea7b-794c-3a09-9e65-22a7d4755caf | -21.42636 | -43.88438 | 2025-08-18 03:57:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 26f84141-65b6-3b28-badd-e16dac778c8d | -18.5451 | -43.99078 | 2025-08-18 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fca39e0a-72a4-38d3-bede-b5f5c1338aab | -17.61142 | -44.67514 | 2025-08-18 03:57:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b1826db-0772-3b87-91dd-3dcffc9844a1 | -15.00052 | -54.79924 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 415fcdc6-2d2b-327f-9dd4-83928528b681 | -23.30606 | -46.8864 | 2025-08-18 03:57:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 855ffe7a-249b-35b6-82f4-ce7cdd8aa17f | -14.97196 | -54.77868 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9fe6f659-b4d8-3a2b-af05-f621a4d572de | -19.15367 | -47.03037 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f7f766c-c17e-390f-9d16-c1ab5f98d104 | -19.1496 | -47.02941 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bb50d59-60e9-33d5-bf06-e52a0d4ae1c0 | -20.32954 | -41.61514 | 2025-08-18 03:57:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 65b7ade7-b403-3a3b-aa8b-80cb1b02b225 | -16.83483 | -48.91231 | 2025-08-18 03:57:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2795d5b5-1acf-35e0-8da3-a3701a95589f | -23.37868 | -45.44181 | 2025-08-18 03:57:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c6ff3e2e-6990-39ee-b5fe-eecea6642877 | -14.96481 | -54.77748 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17ffaa27-f304-39e8-a51b-341a478a4b6a | -17.3973 | -49.22658 | 2025-08-18 03:57:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e83f73ef-0538-3ac7-84cd-1937f8383751 | -20.21968 | -47.03116 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a7330bf-59b1-377e-aa9b-668dc22d3595 | -19.1473 | -47.04151 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b4a7830-9bb2-384b-9e0b-68a7d404d377 | -22.141 | -50.02762 | 2025-08-18 03:57:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 688c0fbf-e19a-331f-8c3b-a1d282e42069 | -22.07625 | -45.05669 | 2025-08-18 03:57:00 | NOAA-20 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 154260f7-62ff-366d-8891-89fa890dc5aa | -17.89578 | -44.42643 | 2025-08-18 03:57:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e111a4b-5a1a-328b-a069-f7aa65c6f3d2 | -23.5055 | -48.31336 | 2025-08-18 03:57:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e7909934-2203-3785-826c-93617ce439e0 | -14.99007 | -54.78008 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d42adb6a-7549-3885-8aa3-60bf9a7ef8f2 | -20.21361 | -47.04104 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f17ff72-eaff-38e7-a98d-d28e75b8e057 | -18.04549 | -43.81326 | 2025-08-18 03:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 142e6a8d-f9ef-34a7-b1ec-dd53bafd01bc | -18.67011 | -44.63649 | 2025-08-18 03:57:00 | NOAA-20 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8feab0b-8bdb-3aea-ab48-66bc1bda4e4a | -21.48033 | -47.75446 | 2025-08-18 03:57:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2fbbf17-89f2-3d9e-b378-511d38a1f1a4 | -23.07387 | -45.60605 | 2025-08-18 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a082f392-1f09-36e4-96d2-4dcbbe069335 | -17.09603 | -49.88208 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 92efdb9e-c5d9-3ac9-84fa-25f6a27461cc | -18.54582 | -43.98656 | 2025-08-18 03:57:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 832cd911-853b-396c-b621-fb8ae5fcb3a4 | -16.79651 | -50.09921 | 2025-08-18 03:57:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 647a7815-0450-3f7a-bf4e-3771b5c1ffdf | -23.24101 | -46.75518 | 2025-08-18 03:57:00 | NOAA-20 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| abf3d418-a08b-3222-9055-5322a3ff48fc | -21.48443 | -47.75538 | 2025-08-18 03:57:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2145447f-89dd-380f-a72b-f32b65a51c7e | -20.28709 | -42.53902 | 2025-08-18 03:57:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f67fbb6-c108-3cdb-b186-52de4ae373ec | -17.85138 | -42.52142 | 2025-08-18 03:57:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6597f856-3d2d-3317-8f18-25fe28516e5b | -20.42195 | -43.67459 | 2025-08-18 03:57:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aad56a81-42b0-3cb9-8aa0-f8ef5889fdb5 | -18.89577 | -44.76678 | 2025-08-18 03:57:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b92a3ce-03a6-3e0f-88ea-2eae74ab048e | -15.00399 | -54.80137 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2cd8397c-fc3a-331f-aacb-028e801f98eb | -18.04411 | -43.82136 | 2025-08-18 03:57:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1257aae3-671e-37a5-9d8d-98d45f5dcfd0 | -15.6091 | -54.30593 | 2025-08-18 03:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| edd6eba1-add6-3d69-b9a9-38c5f4cfbc91 | -22.07701 | -45.05236 | 2025-08-18 03:57:00 | NOAA-20 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0126eb8c-158c-3672-9ba6-1c69e8acf00e | -21.78675 | -47.55393 | 2025-08-18 03:57:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b0a4689-3845-3b56-9c11-390deb228df7 | -20.42127 | -43.67861 | 2025-08-18 03:57:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 5cc3435e-4519-3d73-9213-4b929d147760 | -20.21898 | -47.03481 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ba25544-437d-32f4-817d-e9375863b438 | -14.99869 | -54.80724 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b85fafae-2f34-31f9-86de-c1ed255f26eb | -14.97914 | -54.77972 | 2025-08-18 03:57:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| effb51ba-b029-3d56-954b-0b5f3a0b94d4 | -16.84434 | -48.9149 | 2025-08-18 03:57:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44a15028-8d04-3b0a-abe9-ad566046d8ae | -17.39198 | -42.62335 | 2025-08-18 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 49185bfe-ef5b-3b0f-b17c-0ff268a044b5 | -19.14062 | -47.03193 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6282d19-15dc-3d09-9ed1-f81eea0e0922 | -19.1432 | -47.0407 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 512b21a2-3226-3bc9-b2b7-de80536277cf | -20.2077 | -47.02832 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e15ed93-1b1d-3bf9-9a82-778902eae650 | -20.20704 | -47.02819 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f69cd9f-1f7d-3886-ae28-3cca2db0220e | -21.48368 | -47.75933 | 2025-08-18 03:57:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 95a6c44d-c733-3ebf-8311-867eacb56848 | -17.09223 | -49.87462 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3d27bdad-b2c3-38b5-a083-2528c2bcbb11 | -17.21777 | -49.58565 | 2025-08-18 03:57:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c01802f-37c4-39dd-90a1-0ecb5328985f | -22.21077 | -49.73986 | 2025-08-18 03:57:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 59eaa2f9-1f4f-362d-8fff-167185589e4a | -18.36029 | -45.09762 | 2025-08-18 03:57:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bcaf7a7-e1ee-3a58-ae29-d30c6d3d935b | -17.69687 | -42.18094 | 2025-08-18 03:57:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8bd12acd-6ab9-3868-b375-a6c725f87a4f | -17.396 | -42.62017 | 2025-08-18 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a9f3d875-ef26-36ba-b0dd-26151134fb75 | -18.25702 | -45.15902 | 2025-08-18 03:57:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01cb95e9-7c08-38fd-8e42-ea17952b3984 | -16.7972 | -50.09587 | 2025-08-18 03:57:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7cbb041-6787-3e70-abbb-78edd8a0e4cf | -20.33012 | -41.61148 | 2025-08-18 03:57:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| daf69604-1870-3567-88af-d6afd5950ca6 | -19.14475 | -47.03259 | 2025-08-18 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 97c1d36b-00f2-3098-92ee-8fc42e16d8eb | -20.20636 | -47.03186 | 2025-08-18 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 349e6b49-dfe9-3f25-9033-0ebc78731f30 | -17.91585 | -44.43956 | 2025-08-18 03:57:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d43b04b8-d617-3710-b672-3dd72bdffe6b | -17.09028 | -49.88423 | 2025-08-18 03:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f8a6a8ec-e55d-33c7-8013-5ddab5434ec4 | -17.39178 | -42.62012 | 2025-08-18 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| b766d28e-cfaa-365c-afc1-61780ef3508e | -19.67715 | -41.97938 | 2025-08-18 03:57:00 | NOAA-20 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ade3c63b-939b-34c1-9809-3f24d0cfd71f | -16.79194 | -50.09506 | 2025-08-18 03:57:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README16.md)
