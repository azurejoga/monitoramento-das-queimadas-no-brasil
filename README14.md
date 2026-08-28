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
| 832024b8-1d4b-389e-8e16-ebeb548ad719 | -12.43172 | -43.4099 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 33683a88-de47-3089-bd40-b88414e99043 | -15.57877 | -41.77947 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c96f440f-7015-3218-9b83-9fe2f5328353 | -15.5337 | -41.927 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b2a0bbbd-9a4a-3b9e-acdc-b0daa1167447 | -15.53438 | -41.92368 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b3d20afb-3992-39b2-8d42-048f0def3bce | -12.77924 | -46.45605 | 2026-08-28 03:32:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa5d7fd6-9ada-3e10-b44c-5cccd9fb96e6 | -12.42383 | -43.41799 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 03f255b8-cb01-367b-baf9-b7b1ec2050fe | -12.42984 | -43.41938 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| f88984ec-802d-39de-9681-50f1e007b557 | -15.93733 | -38.90083 | 2026-08-28 03:32:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ed8a4ee0-c6d5-3f82-8533-15c42d71805c | -12.76791 | -44.26591 | 2026-08-28 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20f65fab-7592-30c4-bdc0-b8ce3e30424b | -15.14783 | -43.8017 | 2026-08-28 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4b23a4c-9752-3f15-a90b-d2c84dd2009d | -15.57999 | -41.78 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| adf6f375-9c3b-3813-9c73-f46fe9928448 | -12.43224 | -43.41202 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 2fd430e8-9bf5-3a1d-ad28-2e94c834b129 | -13.3688 | -41.3514 | 2026-08-28 03:32:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5e17faf1-ba5a-373d-99bb-bdb97c674ef8 | -16.83543 | -39.33592 | 2026-08-28 03:32:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 489f3441-763a-3650-98fb-2295a7121535 | -12.43029 | -43.42149 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4f0c2961-cec1-3b1f-bec0-d13865155e9e | -15.53421 | -41.92345 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c7505b29-c8dd-38fa-80e0-649b3f2004ca | -12.42477 | -43.41326 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 18eef8eb-59fb-36e5-8ab0-f0cd7eab1172 | -14.90928 | -43.41219 | 2026-08-28 03:32:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9b1ccf05-8fe7-36b2-b2ad-888f620a9b05 | -17.53048 | -42.47613 | 2026-08-28 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd5fb92d-1d2a-3fd5-8f5f-bfb0b0392e24 | -13.60192 | -45.78544 | 2026-08-28 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12b457e2-90ee-37e4-a855-f06664fb6165 | -15.53355 | -41.92678 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e15bc955-aace-35da-8369-aa60fa058bdc | -12.50195 | -43.81536 | 2026-08-28 03:32:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 61fc73a5-aa75-3779-9892-92cbf5dfc74f | -12.43078 | -43.41463 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 3128f4ae-e288-3c34-840c-b8b60b399f3d | -12.42429 | -43.42011 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3524e7a3-d423-3c51-bd1f-db77c14072fd | -16.83622 | -39.33181 | 2026-08-28 03:32:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 27f26838-7286-372b-a4e5-f5dee449ac97 | -12.43127 | -43.41675 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 024f3146-514d-3cdf-b886-6d04bc6fce0e | -13.37403 | -41.35233 | 2026-08-28 03:32:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0072739-b08a-3eb4-b440-68fe9bc21842 | -12.41924 | -43.41408 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 779d724c-9c36-38ff-ba5b-476e7a60f830 | -17.7942 | -39.7082 | 2026-08-28 03:32:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c56886cd-caeb-369f-ae0a-9a5495ecf5de | -17.53551 | -42.47801 | 2026-08-28 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12856a79-db21-32c7-a1c7-405b247533f6 | -15.52248 | -41.92801 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 827ad620-32a6-30d9-85d1-4f485ae9b223 | -12.43321 | -43.40732 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2158aa5a-d9ab-3030-8696-1d481ae3e5a9 | -14.11049 | -44.38422 | 2026-08-28 03:32:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbd93cd3-e615-3431-8be9-5c1ffc4468cd | -19.6799 | -43.92745 | 2026-08-28 03:32:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d23c9462-fcd7-3c10-b35e-52eb8cb0e553 | -17.79502 | -39.70388 | 2026-08-28 03:32:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 91b8fdc2-2719-3721-bb49-e8602555b328 | -15.52901 | -41.92239 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 1ef31858-5905-3da2-8bd6-6b4024143106 | -15.52768 | -41.92909 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| fb198a7d-6bb5-38fc-8567-423e6797c285 | -15.14874 | -43.79728 | 2026-08-28 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d6aadc6-a047-3ab4-8829-d82e93887dff | -15.14592 | -43.79895 | 2026-08-28 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f71cd04e-e18d-3364-82d6-f872615abb00 | -12.50812 | -43.81667 | 2026-08-28 03:32:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8550bc1b-fb02-3d2f-b68b-f89750144c53 | -13.37466 | -41.35012 | 2026-08-28 03:32:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2212577-79a4-30a4-b8c0-9b77ebb4b618 | -12.42526 | -43.4154 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 451d197d-ce8c-3e94-85ce-0504aeb007af | -13.36874 | -41.35266 | 2026-08-28 03:32:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4f90e7fb-01d8-3428-b909-e987266b42cc | -13.59646 | -45.77786 | 2026-08-28 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84fd634f-69ff-37eb-8388-487861f2092b | -11.97258 | -45.49851 | 2026-08-28 03:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c453b6f1-ba23-3067-845d-ee0a04b52f0b | -13.36942 | -41.34924 | 2026-08-28 03:32:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4590abe1-6e66-3a84-a8e0-e409f6fbdeab | -14.11664 | -44.38583 | 2026-08-28 03:32:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ba9c117-eec8-38a0-8a32-97726bec7646 | -23.81822 | -48.71078 | 2026-08-28 03:34:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddaf918e-6e73-3a68-9965-8943c47a67d0 | -23.63963 | -48.27665 | 2026-08-28 03:34:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cf145fbf-75a9-3c28-8cee-31214ba0cbba | -20.3404 | -47.60302 | 2026-08-28 03:34:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1359785-91cf-3cfe-9e8f-8d5144f58f43 | -21.08703 | -46.34343 | 2026-08-28 03:34:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 787f6fb3-7615-30af-bae8-be2c2c8ee393 | -20.43148 | -47.53048 | 2026-08-28 03:34:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 787b5efc-ce81-3340-9ff9-1ea2252e2b89 | -23.82472 | -48.71273 | 2026-08-28 03:34:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89088e4e-74b6-3845-ad57-7c1a10d4982c | -23.82198 | -48.71217 | 2026-08-28 03:34:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5cac9a22-fcf7-3ca4-a7e6-c5e051a2248d | -20.34192 | -47.59671 | 2026-08-28 03:34:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9110cc33-5b79-3f8a-b039-355b53a815a1 | -19.52389 | -47.63118 | 2026-08-28 03:34:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 607f6ace-c624-366d-bc2e-90f6a1926b7e | -23.70827 | -46.89811 | 2026-08-28 03:34:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 52d80b76-e875-3bcc-ad03-15677a999746 | -19.5226 | -47.63092 | 2026-08-28 03:34:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a124ac2c-4ea7-3a45-9470-ba519ba5793f | -20.42357 | -47.53429 | 2026-08-28 03:34:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f591a7-38ef-352e-ac87-7c36f1dbacac | -28.67036 | -49.90707 | 2026-08-28 03:36:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1ae1a74e-4327-3a6b-b033-34bb02c92ed8 | -28.66309 | -49.90213 | 2026-08-28 03:36:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 652406e3-1152-39c5-ae83-990f375d323c | -29.03382 | -50.37217 | 2026-08-28 03:36:00 | NOAA-20 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ad16af4c-567a-39e7-8e7a-f68152767f88 | -28.66782 | -49.90988 | 2026-08-28 03:36:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 970502a9-e8bc-34a3-959b-a5436dc2f6b6 | -28.66413 | -49.90502 | 2026-08-28 03:36:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0d207fa9-3bb1-3d8d-9b83-671447b362c4 | -28.66567 | -49.89931 | 2026-08-28 03:36:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 55825923-21e9-32cf-928c-3362d81faa3f | -28.66885 | -49.91265 | 2026-08-28 03:36:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 994f2df6-1d12-36d1-8571-b67d59617200 | -28.66263 | -49.91054 | 2026-08-28 03:36:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ca3164cf-3444-3aec-a977-5e9cd5f0cc86 | -28.6616 | -49.90776 | 2026-08-28 03:36:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 73fd7cf7-9795-35fe-9121-337c6055173c | -10.3894 | -61.2502 | 2026-08-28 03:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| abbf0952-7c23-3c47-afe9-bd7c6170e062 | -16.1638 | -58.6053 | 2026-08-28 03:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.5 |
| d8f971d4-f217-389c-8b1a-77d2dac33ff1 | -7.2661 | -45.8443 | 2026-08-28 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 68be4f0b-bfa3-34eb-b6d4-fbc9d6564145 | -16.1444 | -58.6073 | 2026-08-28 03:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 627b5005-36d1-3f5a-b19f-cf769ed609ae | -16.1644 | -58.565 | 2026-08-28 03:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| a52515fb-1807-3092-9ed8-263e91d75c22 | -7.2471 | -45.8685 | 2026-08-28 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 4711bb1b-3dae-3bd4-844a-3284134626ee | -7.2474 | -45.846 | 2026-08-28 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2e4c4523-4760-393d-9050-0455f33a50fe | -6.1656 | -57.7988 | 2026-08-28 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| cdf38a94-b084-3ca1-a7b9-08e81a72d9c5 | -16.1641 | -58.5851 | 2026-08-28 03:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 260.7 |
| ada7faa6-0f00-39b2-ad9a-4ef16fd38876 | -16.1447 | -58.5871 | 2026-08-28 03:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 187.1 |
| 3fde7ec1-edc8-3cfc-ae1a-e93631217810 | -9.6212 | -55.1064 | 2026-08-28 03:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e43e9e3a-a39f-3ef6-9e4f-294341d901d1 | -10.4981 | -64.5005 | 2026-08-28 03:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2d363e2d-2d11-355a-8e81-aa7a288837c6 | -7.2659 | -45.8668 | 2026-08-28 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| c5876283-8f33-3bc6-b405-8b0199541bfd | -6.1657 | -57.7793 | 2026-08-28 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 3411df18-6118-38d1-b1f9-5d6afa2766e7 | -4.8397 | -45.3926 | 2026-08-28 03:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| bd36ef00-9802-3adf-976e-8e4513201499 | -11.2879 | -54.0317 | 2026-08-28 03:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| fb9e3bd1-e4ff-3f90-ac33-161e83a2e887 | -10.7596 | -54.0384 | 2026-08-28 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 43c37d46-65c9-3f32-8e00-236c814eff9a | -16.1444 | -58.6073 | 2026-08-28 03:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 463bf157-9cdd-3283-8e05-0c04e74970b4 | -14.8821 | -52.608 | 2026-08-28 03:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 95c17f3e-a180-3b7b-9a9c-1bb9db3e036d | -16.1638 | -58.6053 | 2026-08-28 03:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.7 |
| d9240682-f177-308d-8c50-5b635a6cf9df | -16.1447 | -58.5871 | 2026-08-28 03:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 176.0 |
| 78761b6f-4c61-3f25-8d78-9c874d982c63 | -4.8583 | -45.3915 | 2026-08-28 03:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| ff512564-d657-3a8a-9d38-b1cf2a75052f | -6.1657 | -57.7793 | 2026-08-28 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 9081be9f-6a5e-3cef-a3d5-aef39e298b83 | -7.2474 | -45.846 | 2026-08-28 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 1aba608d-cf4d-3c58-8433-ac5c642a2c90 | -16.1644 | -58.565 | 2026-08-28 03:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| 61a86534-3f65-3d6d-9306-bb61d90ca7fe | -7.2661 | -45.8443 | 2026-08-28 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 012a62e8-db7e-3dfb-bbb4-f60793d895ec | -7.8828 | -46.1028 | 2026-08-28 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| c04e6fea-b346-35c3-99cf-ff8979f763a3 | -16.1641 | -58.5851 | 2026-08-28 03:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 340.5 |
| 6311749e-f22b-301d-84ce-2f2d7cebf535 | -6.1656 | -57.7988 | 2026-08-28 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3fa73065-58f6-33d3-9d51-f3a95c2a75ca | -4.8397 | -45.3926 | 2026-08-28 03:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 307a9fcf-fc11-35c6-95c8-56d58da5fe4a | -10.4981 | -64.5005 | 2026-08-28 03:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5c674783-62d7-3acb-a497-f21810d2293e | -7.2659 | -45.8668 | 2026-08-28 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |


[Clique aqui para ver as próximas entradas](README15.md)
