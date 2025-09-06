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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a5ee3ad-1519-3aa2-947c-c72b252d6648 | -10.47161 | -53.62114 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b27a670-31f6-30b3-abb1-75704a3318cd | -11.39877 | -43.57807 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d21af8b-18c6-30c7-a1ad-3ddf3e4c579e | -9.98298 | -51.61857 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b063a164-9de5-3b1e-9e7d-e7c1a8b0d820 | -21.76804 | -47.27587 | 2025-09-06 04:19:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 81eebc28-03fc-3287-b939-0647bbfb1d37 | -18.1186 | -44.48398 | 2025-09-06 04:19:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3351719-b00a-3f9e-a3ad-67560760a3f5 | -11.92932 | -46.67083 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2ca458e-7781-336a-89e1-f6aad26100d6 | -11.01507 | -52.03868 | 2025-09-06 04:19:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a98b58d6-a970-35b8-9baa-b87dfb1d0018 | -22.24521 | -48.76307 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 172.7 |
| bcb9a90b-7d67-3b1b-9e37-b076a3f078be | -17.71634 | -44.49579 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 891cf55f-5184-3825-a76c-45e5e55280aa | -21.13947 | -43.95575 | 2025-09-06 04:19:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1b8f6cd0-a295-33e7-867c-ce89f33c6cf4 | -18.08629 | -45.79974 | 2025-09-06 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 561b57fe-fe37-3e3d-bd3b-5d99a24a3b5b | -11.93408 | -46.66645 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13631111-de05-38a7-84e1-9240031dd1e2 | -10.46614 | -53.62015 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3cb576a-da37-3dc8-81a8-74b5b88e95ed | -10.22542 | -50.52704 | 2025-09-06 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de2de908-f6d9-36a6-99e4-6166b216b978 | -19.41495 | -44.31889 | 2025-09-06 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5335476c-b08d-3fb5-88cc-ff5cea7fe846 | -22.36025 | -45.55786 | 2025-09-06 04:19:00 | NPP-375D | PIRANGUINHO | MINAS GERAIS | Brasil | 3151008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c26f8805-80ed-3585-9eda-3b27df450883 | -16.32199 | -52.93673 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1714386a-8295-322f-b2cd-71230fb6dfcd | -9.99024 | -51.61754 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb029150-ae33-3df6-be2d-95f38d3f0e7d | -10.47105 | -53.62571 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f857a197-6b59-3c5c-966e-c938314b5a7c | -20.54087 | -46.46255 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5dd5d5c2-17ee-3aff-9db7-142c4c005b18 | -18.12778 | -42.71677 | 2025-09-06 04:19:00 | NPP-375D | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23612325-0be3-3a81-9f88-9a95a3e2ccce | -9.99259 | -51.6206 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baf14cf2-b73e-3864-aad4-d88061ca5414 | -19.81202 | -57.97323 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d519d965-7314-3550-b23f-806c1ed84827 | -10.79485 | -47.73759 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4e9ff88-0212-3b0f-bf9b-34b26e375378 | -11.39825 | -43.62523 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfc6e8b4-3c57-336c-bfbf-ffadb9e981e3 | -10.1384 | -55.1579 | 2025-09-06 04:19:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ab241c5-7591-3f05-af20-8b74912d24cf | -19.81093 | -57.95526 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c0b41c31-ded7-3a3a-86e5-11825178b343 | -11.63437 | -46.64523 | 2025-09-06 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f72291b-e005-3193-a848-f3b5f7e46c36 | -21.82066 | -48.00306 | 2025-09-06 04:19:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8660d66b-4a31-3f93-a8aa-5dd0ceb136f6 | -18.73336 | -46.88555 | 2025-09-06 04:19:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70da7082-ad49-3225-a491-4f70f0637b2c | -11.63154 | -46.64067 | 2025-09-06 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e43deb75-2c91-3f3a-9122-40adc6a48d5f | -22.12311 | -46.63227 | 2025-09-06 04:19:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f8deca3c-e470-3ec6-a414-fc8d237eacb0 | -13.0084 | -45.22507 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ff39911-8fa3-3d84-9345-0ebb4134b785 | -11.64267 | -47.15024 | 2025-09-06 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 327ea682-0888-31b1-a4ea-f30337c5deff | -18.55805 | -44.03845 | 2025-09-06 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08c4b523-8817-30dc-9168-89ec08f9ac20 | -20.35586 | -48.64254 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a70f486-9082-36aa-8e20-080ed7c08689 | -11.90883 | -46.64267 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fda945a-79b4-34c2-8d83-384ed7d7c3e6 | -20.36306 | -47.78921 | 2025-09-06 04:19:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e3440a0-9295-3621-83fa-0566d7268bbc | -18.83666 | -48.79053 | 2025-09-06 04:19:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e100253-aaf2-3540-8fc0-8f20dd46ebce | -22.26164 | -48.74986 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| 066480d2-7cbc-350c-960b-a82cb15ca740 | -18.4367 | -45.93782 | 2025-09-06 04:19:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ca7807c-e328-3b93-b5a3-be64169d6d2e | -16.31629 | -52.941 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2c74ab5-ed6e-3e54-b02a-3a3b007d54db | -15.72692 | -53.5897 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e152c2d5-bb00-3535-9625-35c8bcc8d04d | -15.68641 | -53.58579 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16adb018-4941-3614-8e02-42b55918ab58 | -11.22504 | -46.18938 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c26b4dcc-5abc-3f6b-b323-9328faff6b4b | -9.24773 | -57.08372 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bf284af-47ee-375f-90e8-acd4699b57f4 | -17.71296 | -44.4953 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9332147-04d4-34ba-bd81-27cc71dc377a | -9.25041 | -57.07008 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be7fc1f3-a445-3ea4-8c83-ee3acdcef54c | -20.46885 | -48.78767 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9db74dc1-d124-372d-bcce-504f25679e55 | -17.96859 | -46.90097 | 2025-09-06 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 100ebe3a-f97c-3d52-b274-5c92e026d3ab | -11.62082 | -52.20962 | 2025-09-06 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 18f157c1-8b97-3f9a-9bd0-2248bf371ee2 | -22.78336 | -50.61703 | 2025-09-06 04:19:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 290d430e-fc04-3f1a-adb9-53c9b54f8cb4 | -11.39881 | -43.62169 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40e7fe32-ce4e-3c1a-a243-325b5e51b4e3 | -23.70859 | -47.32847 | 2025-09-06 04:19:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cdf7019b-f715-3727-8c9c-7b45f4058326 | -9.97107 | -51.64104 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5367d62c-dfae-3b82-87a8-9600fcc2bbca | -18.83821 | -48.78815 | 2025-09-06 04:19:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32b3a5c2-7165-3781-b284-a79adc3dbbc6 | -10.22096 | -50.52619 | 2025-09-06 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a7479cd-e834-3b40-8ee6-3f49e847bb86 | -12.53575 | -48.06817 | 2025-09-06 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8ab7c26-3040-3ecf-8952-0eabcbde0179 | -21.99997 | -49.91359 | 2025-09-06 04:19:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 77696a7e-c5bc-3161-aacc-65230a8fd60d | -13.01773 | -46.65428 | 2025-09-06 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 699876b3-44f4-3eb1-b131-600f7fba6b11 | -17.06642 | -46.47873 | 2025-09-06 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2977455-bd39-33f9-b81a-128a6366915c | -10.22016 | -50.53064 | 2025-09-06 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edc9d0f3-6644-39f4-b368-19877724bc8e | -12.69058 | -44.97215 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3dbabac-5b98-3d69-8788-08db08e08838 | -11.986 | -46.76454 | 2025-09-06 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16013836-ddaf-305d-9f66-a4f08cde25cc | -21.93448 | -46.13546 | 2025-09-06 04:19:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1d6295b4-4e02-32aa-8013-212d80cce1d0 | -12.36004 | -45.78558 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 713882a9-45cd-3448-8a17-7fb82d2ea5ed | -18.26657 | -43.02487 | 2025-09-06 04:19:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1e0ab31c-9385-3bb1-ab8f-123d3b991ef4 | -19.63007 | -49.38419 | 2025-09-06 04:19:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0227750c-aa75-32be-a735-0bb1328d4a37 | -20.53637 | -46.46933 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 360d6839-3ded-30ab-9c01-11e981ec9381 | -12.56094 | -41.30822 | 2025-09-06 04:19:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 534ce003-dd58-37cf-8ef3-32b24e29a8e9 | -22.7797 | -50.61624 | 2025-09-06 04:19:00 | NPP-375D | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2eaaec74-e7e4-3bf9-96a9-6db979d58c1a | -21.02996 | -45.11592 | 2025-09-06 04:19:00 | NPP-375D | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34ded81f-8a08-3580-9e5c-4abb03361842 | -19.93627 | -43.60617 | 2025-09-06 04:19:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 33cbe452-6823-3eba-b863-c2330d609999 | -20.53696 | -46.46564 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed02a8f4-beba-3a04-8355-800bd1aff12b | -19.40578 | -44.3098 | 2025-09-06 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 458a3e98-49a8-3253-9477-1a6da9f05f05 | -16.32479 | -52.94763 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba22bded-0513-339c-892b-5515c5a57333 | -11.01407 | -52.04406 | 2025-09-06 04:19:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab75cc7e-0769-3aab-b195-097113fd28a0 | -18.56717 | -44.0242 | 2025-09-06 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b2eb410-08b3-3128-a1be-9a4ed8a1af04 | -20.52972 | -46.46813 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af04f5a0-b696-3d5c-89d3-95c56d6f0830 | -23.09604 | -49.84937 | 2025-09-06 04:19:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e3830e58-3169-3a3c-86d1-00ae1a3023db | -21.82869 | -47.99662 | 2025-09-06 04:19:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0caf3cf-2dd6-3c51-9f25-7cb1e38ed890 | -23.10217 | -49.84838 | 2025-09-06 04:19:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 504f735e-2fec-3b10-8ff8-1db2a8ce4b7e | -17.96523 | -46.90037 | 2025-09-06 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3d715eb-f0af-342f-9c17-5089257046e4 | -11.92994 | -46.66972 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8decd0dd-ef70-3e3e-bbba-fc1c8679483e | -20.43984 | -54.62783 | 2025-09-06 04:19:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11778542-3679-3407-a694-19ede6ce6cbe | -11.01268 | -45.92581 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1814a7c9-635f-3ed7-a421-506be96ccef6 | -23.09958 | -49.85006 | 2025-09-06 04:19:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c155d412-6256-32ae-8f67-8d487dde8d92 | -17.71014 | -44.49112 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e84253-a2d6-36d3-b9be-3787d053ed4d | -11.92929 | -46.67361 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c85c81d-9b3a-353a-9b8f-05fc85c3398c | -19.93276 | -43.60554 | 2025-09-06 04:19:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 06785608-b62f-3c47-b9b6-54348913b30b | -10.4669 | -53.6176 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 855a79f5-dd5b-3fa5-8aee-33199b55f271 | -11.39598 | -43.57399 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef28e4a1-0941-306f-976a-b30c3c9aba30 | -9.39525 | -54.75358 | 2025-09-06 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fe8ff02-4aec-3015-9525-5f5a54ae91d9 | -10.22462 | -50.53149 | 2025-09-06 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82859156-b859-3599-a849-e5cd8362fd2c | -16.3333 | -52.9542 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e6baa41-6541-396f-8782-e8b88ee183d4 | -18.14543 | -51.78008 | 2025-09-06 04:19:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f898c672-18d4-3f7b-9496-9c93260a6b86 | -17.69334 | -44.5108 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5ed50a9-7d1a-31f5-9830-6972ae17a417 | -20.5289 | -46.11124 | 2025-09-06 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4807b040-5931-303a-a603-a9eebee3eb0e | -11.93343 | -46.67033 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb837b35-449a-3293-ad68-96323a36134f | -23.33246 | -50.88154 | 2025-09-06 04:19:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |


[Clique aqui para ver as próximas entradas](README49.md)
