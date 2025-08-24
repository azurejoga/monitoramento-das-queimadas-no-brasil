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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00381cd8-275b-3426-a7fa-b67d6fcb43e8 | -23.32888 | -47.84602 | 2025-08-24 04:38:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 10ced1f3-63e6-3674-b515-ddd1599a948e | -22.22132 | -45.69598 | 2025-08-24 04:38:00 | NOAA-21 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| cec76e96-dd8a-3682-a1a3-2f3577371656 | -23.19442 | -46.8463 | 2025-08-24 04:38:00 | NOAA-21 | VÁRZEA PAULISTA | SÃO PAULO | Brasil | 3556503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fc6b0ed3-e0c5-33d1-a4f8-3441041ee8a6 | -22.73174 | -46.97202 | 2025-08-24 04:38:00 | NOAA-21 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a94022d2-f8f5-3368-8e95-96365f260953 | -23.26377 | -46.62645 | 2025-08-24 04:38:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ab68f533-ffd1-337f-b50b-bb76b484255f | -21.32126 | -48.67233 | 2025-08-24 04:38:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d8d427c1-5d52-323c-97ee-5576d2ab4278 | -22.2404 | -49.63422 | 2025-08-24 04:38:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f035c91e-e9b5-3a6f-9942-f7e3c21e9b2d | -23.13121 | -47.03114 | 2025-08-24 04:38:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 85bc6413-df4e-3535-ab68-f32de25a75c8 | -22.79031 | -46.71688 | 2025-08-24 04:38:00 | NOAA-21 | TUIUTI | SÃO PAULO | Brasil | 3554953 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46822c6c-4d43-3af5-94d6-c403da8a5392 | -24.25251 | -50.23735 | 2025-08-24 04:38:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4e81828f-b8bd-3aa0-945d-ce7bde0fcc28 | -22.00752 | -44.9966 | 2025-08-24 04:38:00 | NOAA-21 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a1b7269b-1c92-3146-8c10-bcb9429398e1 | -20.88156 | -49.4272 | 2025-08-24 04:38:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3a34a615-0b12-3627-9183-9c774b12328e | -24.77958 | -50.11969 | 2025-08-24 04:38:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d10ce2c0-a7f0-3085-b382-ec0f9c59814d | -22.68917 | -43.67429 | 2025-08-24 04:38:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4e077d20-9b41-3795-913e-fc11e8c15baf | -21.95065 | -45.58769 | 2025-08-24 04:38:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e169afa6-e7ed-3644-8f17-46906a169d63 | -23.80293 | -51.05966 | 2025-08-24 04:38:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2b7b4fcd-91bb-3759-8d01-64f6d82e231c | -24.2531 | -50.23329 | 2025-08-24 04:38:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ecf97065-9446-36e0-b368-3a676ccc10b1 | -22.84479 | -46.29354 | 2025-08-24 04:38:00 | NOAA-21 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ed8fb7fc-907a-3ad7-a2b1-39730eed879e | -23.50038 | -47.07519 | 2025-08-24 04:38:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33c8420f-1dd3-3d57-bcae-05298d4da157 | -20.29154 | -50.89827 | 2025-08-24 04:38:00 | NOAA-21 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ec16bba-1987-3e64-94e3-9e542469c21b | -23.62839 | -50.56215 | 2025-08-24 04:38:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| de2fd71e-31e5-36ca-a788-eb4bd43177bc | -23.18369 | -49.98315 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aaa63af2-0438-359d-9858-841b4a598226 | -23.62605 | -46.02233 | 2025-08-24 04:38:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 144f880d-feb1-3300-9e34-426c1bb7ab8c | -24.62919 | -50.24307 | 2025-08-24 04:38:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62443837-3f33-3a2b-b62e-8aedd6c95522 | -23.84606 | -50.72279 | 2025-08-24 04:38:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5d7ecda3-7dba-3b5c-8bfe-6179de2ec445 | -23.08345 | -49.97541 | 2025-08-24 04:38:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f175f44b-7f50-334f-8150-272653a8e3b6 | -21.3248 | -48.67286 | 2025-08-24 04:38:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ebeb0268-84d7-3d03-b457-981f5d156343 | -21.27748 | -43.75443 | 2025-08-24 04:38:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e2f60d7c-b02a-3add-afee-72bac56708e6 | -23.84944 | -50.72326 | 2025-08-24 04:38:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64beeead-4580-36f5-a293-1326144257b4 | -20.34587 | -51.70282 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 33c4379c-045b-3813-9e41-242020050309 | -23.84887 | -50.72712 | 2025-08-24 04:38:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 554596d1-e0b2-3fc0-94b9-860a85d70337 | -23.19139 | -47.5354 | 2025-08-24 04:38:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 218eb761-cada-3d9d-87d7-87544c225b76 | -22.30773 | -47.60575 | 2025-08-24 04:38:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c1a1db6-b51e-3682-88ef-458760681425 | -21.72972 | -46.81815 | 2025-08-24 04:38:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 83657b6b-b356-3f16-95f0-404050133d4b | -22.72919 | -46.96053 | 2025-08-24 04:38:00 | NOAA-21 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cda4a47e-12f7-3f08-96dc-b115046da8de | -21.95115 | -45.58349 | 2025-08-24 04:38:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e8a6596e-6e9c-3a5b-8b54-1fa48c10cfad | -23.32951 | -47.8411 | 2025-08-24 04:38:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 1763112f-11a2-31fa-bbe7-ab71aa28d373 | -22.14267 | -43.65776 | 2025-08-24 04:38:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 4739d99a-e140-3839-b31c-783d1a92f8b3 | -23.7237 | -47.43249 | 2025-08-24 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f736989c-dce9-31f0-979e-04fcb280a662 | -20.36261 | -51.68314 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5e170529-5275-31ab-ad0d-7323d20b5040 | -23.469 | -46.81134 | 2025-08-24 04:38:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| dd910251-3784-35e8-9478-1dbc62d9f6da | -22.41005 | -43.42833 | 2025-08-24 04:38:00 | NOAA-21 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9b78db0d-d5b4-34c7-9799-7c50cb9e80f2 | -23.29023 | -47.63557 | 2025-08-24 04:38:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9c1eda20-cd27-3009-99a2-eacbeaa17ac4 | -22.60841 | -52.49409 | 2025-08-24 04:38:00 | NOAA-21 | EUCLIDES DA CUNHA PAULISTA | SÃO PAULO | Brasil | 3515350 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 222e245f-0f8d-36a0-b051-73a0f95b78d6 | -22.95248 | -45.13035 | 2025-08-24 04:38:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 5160aa92-b9a0-3dd9-94df-460719192bb9 | -23.37115 | -46.86368 | 2025-08-24 04:38:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 30d0cb3d-b0da-3bc7-88c5-7cb1167f1556 | -23.18818 | -46.28529 | 2025-08-24 04:38:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1af5111e-998f-392c-8979-23d89c01e75b | -22.91013 | -51.14827 | 2025-08-24 04:38:00 | NOAA-21 | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 60f05157-9a7e-3ac6-9963-e1cc0c5d0167 | -22.03892 | -53.86144 | 2025-08-24 04:38:00 | NOAA-21 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f713af51-64fa-3fc1-bbc3-b4bbf492e56c | -20.87813 | -49.42665 | 2025-08-24 04:38:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9872b7e-e511-3f09-993f-1542d4e05c8d | -20.35267 | -51.68136 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1a0517b5-f26b-34f5-83fa-b0498ed62ad0 | -23.31306 | -45.53529 | 2025-08-24 04:38:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| a54d9cca-612b-3f3a-98fc-319aa89e5fcc | -20.34313 | -51.69855 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 99e8f4b2-461f-3b68-8ac4-9d09a88afd19 | -20.34372 | -51.69487 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6d9ed994-e891-3477-b91c-0fcc6c0e870c | -23.36717 | -46.86312 | 2025-08-24 04:38:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| dcafd542-0c8b-3135-ad94-d09b6fd86ba5 | -22.87342 | -42.44201 | 2025-08-24 04:38:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f50da34d-1ae1-3522-92b3-cb40041860dd | -22.41067 | -43.42247 | 2025-08-24 04:38:00 | NOAA-21 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 417fbe22-aa83-36ca-b49f-5dbc57e4bae8 | -20.34877 | -51.68444 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8d07c93f-aa00-300b-97c1-70f07b947213 | -22.00698 | -45.00123 | 2025-08-24 04:38:00 | NOAA-21 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 33a3b078-2c9e-379a-a6f1-da2627d9a3eb | -20.34703 | -51.69547 | 2025-08-24 04:38:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 07cfbdf8-cacd-3a81-84d3-7fecd45e4c4e | -10.4164 | -47.1732 | 2025-08-24 04:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ec12898c-8beb-3255-a8e7-6c750b861480 | -11.5437 | -51.8454 | 2025-08-24 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 432c100a-2243-36d4-9e9f-347c8e8baca2 | -9.1536 | -59.464 | 2025-08-24 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| b2250741-77e3-36c4-a3c8-dee0583af54b | -16.797 | -51.3419 | 2025-08-24 04:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 4cbef5ca-d917-3ca0-b4c6-190c633f2b56 | -9.0046 | -65.6988 | 2025-08-24 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 98d9fdf6-bc28-33c6-b4cf-5e1aaac826ea | -9.1535 | -59.4834 | 2025-08-24 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| dead8635-e0b2-3acf-a32f-79b092c6aa84 | -9.1722 | -59.4629 | 2025-08-24 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c128f776-32ee-31e2-820c-b4e8801863c2 | -9.0231 | -65.7169 | 2025-08-24 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b8ea5c8c-277b-3433-a62f-fff2e7878867 | -10.416 | -47.1955 | 2025-08-24 04:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 522f4486-71e6-3119-9680-f8f8615c514f | -9.0232 | -65.6982 | 2025-08-24 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 9df259af-2ea2-301a-b0e3-864b8b3adfef | -11.5247 | -51.8474 | 2025-08-24 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| aac9212f-b7a0-37c6-873a-831724e60f0b | -9.1721 | -59.4823 | 2025-08-24 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 2275bf84-bdbc-3df3-a6dd-d76844986689 | -9.1722 | -59.4629 | 2025-08-24 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a58b59f8-e123-36d3-bab6-c1557f2d857e | -16.797 | -51.3419 | 2025-08-24 04:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| bfce7151-9696-3761-b18e-4f5d1e3591fc | -11.5245 | -51.8685 | 2025-08-24 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 55c210cb-d774-393b-bdb6-bc9e02cafcb7 | -9.1535 | -59.4834 | 2025-08-24 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| bd2de34c-7282-33f5-b35a-362eea4d6006 | -9.0046 | -65.6988 | 2025-08-24 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 56ad3b7f-4f56-3d46-837f-147486efa3ec | -9.0232 | -65.6982 | 2025-08-24 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 1a89618a-054c-3afd-a2c9-d5ae8e1fbab4 | -9.1536 | -59.464 | 2025-08-24 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 4fbce8ca-8e69-38fa-a9ea-22052389281d | -9.1721 | -59.4823 | 2025-08-24 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| dc6bdaba-88e6-3192-a884-6f089963b2f7 | -11.5434 | -51.8665 | 2025-08-24 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| daac8320-8b46-3ce4-a2e6-ca746ab8091e | -17.5975 | -44.3027 | 2025-08-24 04:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| dccffc78-00fc-3b97-8a0b-aa44297604c0 | -9.0231 | -65.7169 | 2025-08-24 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c1bb255f-5d0d-3e72-90d8-253240ae6fb0 | -11.5437 | -51.8454 | 2025-08-24 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 208.9 |
| 976d5e77-7abd-3cca-8622-8a419fcad508 | -17.6176 | -44.298 | 2025-08-24 04:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 3ec7b0e8-d4ad-3a4a-a329-a6226423504b | -4.9605 | -55.8226 | 2025-08-24 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 4bf9511c-1058-3c35-8a66-712b0764185d | -11.5247 | -51.8474 | 2025-08-24 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 7599f5ba-c423-3e6b-aad7-b530414516a2 | -16.7965 | -51.3637 | 2025-08-24 04:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 645b7660-d8de-3a0d-8661-25bafaba3bfc | -3.4421 | -49.04392 | 2025-08-24 04:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 389d6bbf-8b70-3256-8200-ba3589605853 | -4.82285 | -47.3155 | 2025-08-24 04:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ccf27aa-f939-3072-8e9e-36496965d8a4 | -3.39966 | -52.83663 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15fb5ddc-5fbb-3f4c-b014-253e435f7290 | -5.58804 | -43.24709 | 2025-08-24 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9a4c9dc-14ec-3d73-ab4d-9f56779cc5f4 | -2.26508 | -47.85519 | 2025-08-24 04:57:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c2df430-c2d4-3ef4-89cd-91644a894d97 | -2.93132 | -53.70454 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a5962b6-f495-3c03-8b4a-451ea0797b0d | -3.52764 | -42.70197 | 2025-08-24 04:57:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04f0513b-f5ec-34f4-9689-a0af15d80bfd | -4.58436 | -48.03492 | 2025-08-24 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5beca07d-0b09-32e2-91cf-0bc7d26297f5 | -2.91758 | -48.30592 | 2025-08-24 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93208274-4b52-3952-aff8-63f942266848 | -3.38624 | -47.61476 | 2025-08-24 04:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89589221-30d5-39ed-a932-647d8a5cbffb | -3.84028 | -55.96165 | 2025-08-24 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b0841e3-b70b-3940-aa6c-e05482ee1082 | -3.84317 | -55.96608 | 2025-08-24 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README52.md)
