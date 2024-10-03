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
| 0a791192-9ec7-3128-8dac-13ec0daa14a9 | -21.5191 | -42.043201 | 2024-10-03 00:07:21 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ca2210a-2986-3d61-911c-70b2e1ddafc7 | -21.5208 | -42.051899 | 2024-10-03 00:07:21 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8fb84ed8-698d-3f8d-8da2-9b1e45573777 | -21.483999 | -42.124001 | 2024-10-03 00:07:21 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 74e819c0-90f0-31c9-9de8-97513ceee1ab | -21.485701 | -42.132801 | 2024-10-03 00:07:21 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b23982f-36e9-3f11-826f-f125516f7f26 | -21.3081 | -41.394798 | 2024-10-03 00:07:22 | METOP-B | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6a444d5-f9d7-3851-af10-e7cefe864444 | -22.3694 | -47.8937 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b7edd8ba-1dcc-359a-93f9-10b4367ea3b3 | -22.372601 | -47.9137 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2108d1f7-fe8e-3318-8395-4a490c63d368 | -22.359699 | -47.895401 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 696a6df3-7fa4-3433-8e3c-a07382e21b1e | -22.3629 | -47.915401 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1670597c-47c3-37f0-98bb-bfb9c8a99788 | -22.3661 | -47.935398 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 514c4035-8899-3806-9e36-fc6570fc3f92 | -22.349899 | -47.897099 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| abcd94cc-0f83-3fe1-a87e-28c930418b77 | -22.3531 | -47.917099 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b2bef046-b109-3a6d-ace0-446de9c4f90c | -22.3563 | -47.937199 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec0b2ef-e898-3b79-9d83-8dec91960ffe | -22.343399 | -47.9188 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 385501cc-0654-3956-94f6-74d4e6cb0257 | -22.3466 | -47.9389 | 2024-10-03 00:07:24 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c04722a4-fea3-3025-8c15-a0615e04a556 | -22.3598 | -48.210899 | 2024-10-03 00:07:25 | METOP-B | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 54cc9ad3-04f7-3b29-9e05-fed710c9763b | -22.240801 | -48.4062 | 2024-10-03 00:07:27 | METOP-B | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea794a3-9fee-3102-8891-20311ac87c70 | -22.2442 | -48.427799 | 2024-10-03 00:07:27 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ababc231-d42e-3841-bf33-1523cc155d18 | -22.247601 | -48.449402 | 2024-10-03 00:07:27 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff93d72-a102-36e3-8cae-da865c51e133 | -22.2311 | -48.407902 | 2024-10-03 00:07:27 | METOP-B | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e47d3e33-f19c-367c-bf88-2961c5644485 | -22.234501 | -48.429501 | 2024-10-03 00:07:27 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7647eb1c-663b-39e4-b4a8-a9a556f31331 | -22.2379 | -48.451099 | 2024-10-03 00:07:27 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9e9a402f-d158-3c53-b555-672d9222ee7a | -22.1705 | -48.5299 | 2024-10-03 00:07:29 | METOP-B | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a4a072ae-11b7-3512-b04d-29eb1b967ac3 | -22.173901 | -48.5518 | 2024-10-03 00:07:29 | METOP-B | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f3d3c39b-c4a3-34aa-85ba-342c4355e235 | -22.177299 | -48.5737 | 2024-10-03 00:07:29 | METOP-B | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93d11ae2-b8c0-3694-89e1-0df25c38ae7c | -21.489401 | -44.5686 | 2024-10-03 00:07:29 | METOP-B | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d75d39b-ac8d-31a6-a396-8cf5c88b6ff8 | -21.4916 | -44.580502 | 2024-10-03 00:07:29 | METOP-B | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de8badc6-f3b6-359b-a229-4051de0818a2 | -22.058201 | -48.6399 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| adfe3dbd-99b8-38e0-8c34-ed26abad6c7a | -22.0616 | -48.661999 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f9a58f39-0469-3f79-a4be-a867aca58e84 | -22.0485 | -48.641499 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee0adf7-78ab-3d54-a101-c6e6b1992b51 | -22.051901 | -48.6637 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e4f419b3-d31a-385f-bf61-4091997f0645 | -22.0422 | -48.665401 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6e31b561-a2cf-31a4-b157-29c8a6734ea9 | -22.0457 | -48.687698 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 129843d8-d6a1-3624-ad19-c7f4e4775172 | -22.0492 | -48.709999 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1bc98945-c9d0-3f9a-b144-acd716925828 | -22.032499 | -48.667099 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d6ba6907-7a04-3fba-aa3c-bcf7ded33d7b | -22.035999 | -48.689301 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 698cb65c-a31e-3792-affe-1e53153f3a28 | -22.039499 | -48.7117 | 2024-10-03 00:07:31 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9fadf4f9-4909-321e-a5fd-e06d1edac083 | -22.0228 | -48.6688 | 2024-10-03 00:07:32 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9d84e806-c53f-3c36-8adf-52f7d959f28c | -22.0263 | -48.691002 | 2024-10-03 00:07:32 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e9620f51-6c60-3ede-94e4-d8361f498759 | -22.0298 | -48.713299 | 2024-10-03 00:07:32 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d61c2c05-6401-342f-97ec-81c867e0f386 | -22.0131 | -48.670502 | 2024-10-03 00:07:32 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1bf212cd-c0ff-36f2-a8fe-b496de1fc229 | -22.0166 | -48.692699 | 2024-10-03 00:07:32 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 28e9b093-4cdd-3160-a3b3-01fb1980ad57 | -22.0201 | -48.715 | 2024-10-03 00:07:32 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42447784-82d0-3330-a370-787126475872 | -20.6992 | -41.773399 | 2024-10-03 00:07:33 | METOP-B | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5af11827-1889-3897-86b0-0a0aee5821f1 | -20.6612 | -41.9921 | 2024-10-03 00:07:34 | METOP-B | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7dd2b05-2812-395a-a326-b69a80493921 | -20.662901 | -42.000599 | 2024-10-03 00:07:34 | METOP-B | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a5187a5-f93e-312e-9aea-e760b8e36f88 | -20.6514 | -41.994301 | 2024-10-03 00:07:35 | METOP-B | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 848aea3e-30d8-304d-8166-e863540518ec | -20.4359 | -41.989601 | 2024-10-03 00:07:38 | METOP-B | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b65778fd-8ec4-3c4f-b488-0b75e676c989 | -21.393801 | -47.615299 | 2024-10-03 00:07:39 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e15782fe-f0e2-3800-87ae-030edaacea29 | -21.381001 | -47.598598 | 2024-10-03 00:07:39 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1405c7f2-1f7e-3c54-933b-24928709f2eb | -21.3841 | -47.6171 | 2024-10-03 00:07:39 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2b69ec42-5776-3bd1-8e16-3898bb6b6616 | -21.3871 | -47.635601 | 2024-10-03 00:07:39 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 355c97aa-6529-360c-91d2-e07581140677 | -21.3902 | -47.654202 | 2024-10-03 00:07:39 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 58bd9575-9b7e-3713-851d-0a95466f7644 | -21.374399 | -47.618801 | 2024-10-03 00:07:40 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7dc1cbb2-dea5-3688-b50a-35feadc120e6 | -21.377399 | -47.637299 | 2024-10-03 00:07:40 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 79111bd7-ec73-346d-945c-697d390405c8 | -21.380501 | -47.655899 | 2024-10-03 00:07:40 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c5e767af-b4fd-3a07-9d51-7019c89093d4 | -21.361601 | -47.6021 | 2024-10-03 00:07:40 | METOP-B | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9250a68-bf48-3f8b-b816-50c1807e6562 | -21.3647 | -47.620602 | 2024-10-03 00:07:40 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5be722-dbb4-3696-a98d-6a7c066cb26e | -21.2971 | -47.576099 | 2024-10-03 00:07:41 | METOP-B | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 841c872f-8138-36ee-aaf8-0013f3390d11 | -21.3001 | -47.594398 | 2024-10-03 00:07:41 | METOP-B | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0d8587bd-b4c8-3307-9ea2-dbd14427ab3f | -21.3032 | -47.6129 | 2024-10-03 00:07:41 | METOP-B | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 30c8da88-a9c4-3f6b-a4e9-055cbc03eb5a | -21.2904 | -47.596199 | 2024-10-03 00:07:41 | METOP-B | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c06f6393-a7a0-32cf-bd46-3276c53834f1 | -20.551901 | -43.358799 | 2024-10-03 00:07:41 | METOP-B | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72721f91-b83a-393b-b534-0b02adf7f454 | -20.542101 | -43.360901 | 2024-10-03 00:07:41 | METOP-B | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d53bb270-e1fe-3ffb-b44d-6f82b0b202b2 | -20.544001 | -43.370701 | 2024-10-03 00:07:41 | METOP-B | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e10b9df-6369-348b-9731-d35af6581132 | -20.3235 | -42.7607 | 2024-10-03 00:07:42 | METOP-B | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de270357-9357-300b-96b5-8affece83f05 | -20.3253 | -42.769798 | 2024-10-03 00:07:42 | METOP-B | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ecbd7790-4667-3449-bdcf-6261f7c1e9b4 | -20.521099 | -43.73 | 2024-10-03 00:07:42 | METOP-B | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d54d68a-487d-30d7-84fd-df05260ea39a | -20.5231 | -43.740299 | 2024-10-03 00:07:42 | METOP-B | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eeaffec4-ffd7-3446-b64a-cccf5a715f35 | -20.3137 | -42.762901 | 2024-10-03 00:07:43 | METOP-B | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f9765d81-0021-38c6-8821-2b1229f5eeed | -20.3155 | -42.771999 | 2024-10-03 00:07:43 | METOP-B | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ab8e295-27bd-39cc-a137-f272a24a4cec | -20.212999 | -42.459801 | 2024-10-03 00:07:43 | METOP-B | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7bfd81f8-c410-3e3c-89e3-e159c737edc2 | -20.214701 | -42.468498 | 2024-10-03 00:07:43 | METOP-B | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d3d5bb8-431d-36d6-a272-7e1ee58dda0c | -20.216499 | -42.477299 | 2024-10-03 00:07:43 | METOP-B | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44569f4d-0da9-34e7-afe4-874fbadd1621 | -19.734501 | -40.668499 | 2024-10-03 00:07:45 | METOP-B | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98b012a6-e1c1-3ffe-af31-4ac6478875d8 | -19.736099 | -40.675999 | 2024-10-03 00:07:45 | METOP-B | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93ae2f72-9bbb-3f24-ac23-b216e8248866 | -19.8862 | -41.398899 | 2024-10-03 00:07:45 | METOP-B | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2fe1b55e-d0d3-3b92-9078-50e69044dc72 | -20.287201 | -43.517799 | 2024-10-03 00:07:45 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c4ea4a26-4324-36db-abf5-690d8a674835 | -20.7752 | -46.283298 | 2024-10-03 00:07:46 | METOP-B | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 41f90d55-6676-3317-a72b-cb2b9a1c055e | -20.765499 | -46.285198 | 2024-10-03 00:07:46 | METOP-B | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 11753e53-6e74-3643-8133-d28367943332 | -20.768101 | -46.299999 | 2024-10-03 00:07:46 | METOP-B | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26bb1360-582b-371d-9ab0-247e27963e58 | -20.2775 | -43.519798 | 2024-10-03 00:07:46 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3a854de-b51b-3e7e-949a-0e3a783060f6 | -20.1399 | -43.8106 | 2024-10-03 00:07:49 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f6f04fa-6c14-3928-854c-80952f9ecff2 | -20.1418 | -43.820801 | 2024-10-03 00:07:49 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2577ec74-f6b7-30a1-8364-ff97e5706503 | -20.1458 | -43.841301 | 2024-10-03 00:07:49 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2b7893b-7653-32d1-9171-83fcc135a1c1 | -20.147699 | -43.851601 | 2024-10-03 00:07:49 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e9dcf2e-6c00-3da5-99e2-3cf9010494d6 | -20.1341 | -43.833199 | 2024-10-03 00:07:49 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b68cb53-6c60-384a-997d-c2313f0e6457 | -20.136 | -43.843399 | 2024-10-03 00:07:49 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 06ea9aa6-f21c-3a0e-9e13-58a2eebd1bba | -19.686701 | -42.026199 | 2024-10-03 00:07:50 | METOP-B | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1397ff4-09d4-3eff-82ad-c68916e025d5 | -19.688299 | -42.034401 | 2024-10-03 00:07:50 | METOP-B | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3456a201-bfad-3032-be16-edfd5dd77c2b | -19.8708 | -43.156399 | 2024-10-03 00:07:51 | METOP-B | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a50fcfb4-d0bb-3680-ae30-bf909a51dbb4 | -19.434799 | -41.345798 | 2024-10-03 00:07:52 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac30482a-2ea9-355d-b011-e2739d154da0 | -19.436399 | -41.3536 | 2024-10-03 00:07:52 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a6c9338-d2a6-3a35-ae6e-db6c3ea55bb2 | -19.438 | -41.361401 | 2024-10-03 00:07:52 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1606bddc-fbea-3f6e-9008-565f10aae9d3 | -19.4396 | -41.369202 | 2024-10-03 00:07:52 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b1836e66-885d-3792-84a2-398522a6a299 | -19.424999 | -41.348 | 2024-10-03 00:07:52 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea91ef76-0c33-3873-b4b1-21edfa70e980 | -19.4266 | -41.355801 | 2024-10-03 00:07:52 | METOP-B | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b86d1a8-d239-3639-9320-ebc7f36ef351 | -19.2416 | -40.618301 | 2024-10-03 00:07:53 | METOP-B | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09b1596c-83bf-31a4-8678-24911e7041c6 | -19.2432 | -40.625801 | 2024-10-03 00:07:53 | METOP-B | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 414596fd-cad1-39e8-adda-e35cc5027970 | -19.683201 | -42.928398 | 2024-10-03 00:07:53 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README4.md)
