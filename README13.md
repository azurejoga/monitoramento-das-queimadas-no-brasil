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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a110b108-2906-370d-a255-c4861f7a4d4a | -12.37858 | -54.15897 | 2025-06-04 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd7194b0-2277-364a-ba80-985e59b423b4 | -17.07166 | -46.49767 | 2025-06-04 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e83b53a-a0e1-37d6-bfc6-6cf9d2d0d136 | -14.56097 | -59.4971 | 2025-06-04 04:53:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 648d805b-4b92-34fd-b88a-2003f0cad3ce | -11.92089 | -54.814 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d426cc5-40a4-3a7b-93e7-a56115395286 | -17.76139 | -52.43983 | 2025-06-04 04:53:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa2c56f3-91fc-36e9-a25e-aff7f0c9ac7f | -12.17333 | -64.19856 | 2025-06-04 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 672ff5e6-5d2f-3169-9b01-78198e93f070 | -11.38613 | -56.54844 | 2025-06-04 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee9af8d2-e4a0-34e0-808a-ae25ba18aa64 | -11.71389 | -56.45472 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 497737a0-f997-3651-8167-6808c7c881c9 | -11.90552 | -54.78234 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9474ef2c-e496-3df2-a1d1-f429d1214146 | -14.0282 | -55.13452 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbf636fe-d825-35fb-95da-e84089c75a8c | -14.71834 | -45.09139 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b305e289-3030-3a16-b994-8bd2d7f895ec | -12.51659 | -57.17722 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41e61505-4792-3a00-9b35-7efc1d570b3e | -11.55388 | -56.41629 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2407ea7e-6953-3bb0-88ee-39796d42ca6b | -14.02877 | -55.13095 | 2025-06-04 04:53:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a073407a-368e-3db9-bbea-712def88f02d | -11.70258 | -54.55999 | 2025-06-04 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee3b00da-befa-30b7-a6de-458771ad1280 | -12.64914 | -54.12418 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a43d21d2-02ab-3845-a25a-69c49337ca8f | -12.27795 | -50.10386 | 2025-06-04 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d3ba3bf-ab92-3468-9e41-95f582c0825f | -12.2848 | -50.10959 | 2025-06-04 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 276bed87-3302-3ce0-b4af-28382bb742ac | -12.65024 | -54.11715 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e26b8eda-cd39-374b-8fb8-660d422325b1 | -12.52452 | -57.19567 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25628e7f-8713-31db-9d41-ba4fcf7d9f2b | -12.45662 | -54.91356 | 2025-06-04 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 927b03c0-9977-3591-b259-80a13cd1bff4 | -12.27691 | -50.10194 | 2025-06-04 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c409d486-d4a1-3ca7-b5b9-924b3e186c96 | -11.80178 | -57.35796 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ed54843-8c39-3287-a226-99bee2afe97b | -11.91757 | -54.81347 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 575f2070-6ff3-396b-9fbd-d59884f62225 | -11.80535 | -57.35582 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 790e2ac6-ac29-3810-a4d1-a6394a16ef82 | -11.82666 | -57.81441 | 2025-06-04 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6a77992-e4dc-31fd-81dd-96ce60dbef68 | -11.99562 | -52.47162 | 2025-06-04 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35c500db-fe62-3694-a305-b43c6da8b085 | -14.72294 | -45.09879 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 812ed069-379e-3f0b-98d3-e6dcbe26a693 | -11.69926 | -54.55945 | 2025-06-04 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60c1da23-7174-3933-8307-9522b23e2756 | -12.51589 | -57.18136 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11fefc45-6d2d-32f1-902d-ad5780497b87 | -12.72145 | -56.56404 | 2025-06-04 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 951f0dbb-f07e-31f8-85d8-76dbe2504e91 | -14.33167 | -54.13428 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94801974-f4d5-36d6-86e6-ecb736efe269 | -11.6415 | -58.01335 | 2025-06-04 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 563a38e6-dba7-3313-afbf-7d3288957613 | -9.62033 | -67.29256 | 2025-06-04 04:53:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a246ffb0-00ed-3c41-b472-b55de74f6cbc | -11.70589 | -54.56053 | 2025-06-04 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3a4dae9-14be-340b-a0c5-dc1a35b6a556 | -11.55607 | -56.42476 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85cc5e15-9d41-3016-8de5-4561105009d1 | -12.24533 | -51.42927 | 2025-06-04 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a503acb-b9dd-3042-99d0-c79592fa347c | -11.91368 | -54.81648 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4919c631-9f05-393c-98aa-6f6a2315e65f | -12.27859 | -50.09926 | 2025-06-04 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6521292-0b21-3a9c-ab6a-90960b0b71fc | -14.71254 | -45.09427 | 2025-06-04 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 067a4bee-9853-3509-b432-1a04676f87f1 | -11.71454 | -56.45076 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dfb77fe-2fba-3f3a-83d4-6d3eabf5c1bc | -11.80542 | -57.35857 | 2025-06-04 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10f6de77-dc37-38e8-9809-de3de6d694de | -13.59186 | -54.27462 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90841524-9d15-3962-881c-3979c15e075a | -14.684 | -52.68392 | 2025-06-04 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b8b33e2-d144-35b0-9df3-7960f5a3d583 | -12.66495 | -58.22002 | 2025-06-04 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e57de2e-7e6e-34cb-bcb0-05996e64128c | -11.90439 | -54.78944 | 2025-06-04 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb14c091-3d4d-334f-b3bb-4ca10a0c493c | -12.64584 | -54.12364 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d82c03c-540a-360f-974c-05adf60e47b4 | -11.83123 | -57.81871 | 2025-06-04 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e019405-d1eb-3a00-a035-2308e231ab15 | -11.90225 | -58.68054 | 2025-06-04 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b833970-0fe3-3b30-920c-8d9012e483e7 | -15.27492 | -51.47758 | 2025-06-04 04:53:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5bf6866c-22ef-34a3-b305-9239751d8478 | -12.04869 | -53.43668 | 2025-06-04 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b7997f8-0914-3517-a991-bd3f397a126d | -11.56086 | -56.41748 | 2025-06-04 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 986bb030-ac03-3e45-8c81-d37e2cd56d5c | -12.64639 | -54.12013 | 2025-06-04 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c954968-e965-3dd1-836b-5e3de2e13a5c | -19.93514 | -47.26986 | 2025-06-04 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69ba2ed3-c835-382c-81a2-70bfde74eee7 | -20.47749 | -53.67451 | 2025-06-04 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4865fdd-9f1d-336a-bb22-b4f93c5737b3 | -22.30025 | -55.18152 | 2025-06-04 04:55:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507206a4-70d6-3a68-b921-06cf8125e3bf | -18.40789 | -54.5748 | 2025-06-04 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 621d51e0-c58d-3736-9b3b-72a6fbd7744e | -22.53931 | -48.81362 | 2025-06-04 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88d188c2-1af8-3083-8ba3-80e56097a1c0 | -21.24399 | -56.16082 | 2025-06-04 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8132c10-da5b-3605-a5ab-b43dc532e4eb | -20.60723 | -55.70679 | 2025-06-04 04:55:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d07df783-a96e-394b-8d6f-9f6134fdaaff | -21.59879 | -57.57648 | 2025-06-04 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1161109c-f13b-3a58-9433-6f757f95503f | -21.59022 | -57.58662 | 2025-06-04 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4dfce50-9554-3612-8d2b-838ee0370175 | -19.93557 | -47.27105 | 2025-06-04 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd77ba21-341f-3c82-b186-fb38c873f7e7 | -18.71717 | -54.1921 | 2025-06-04 04:55:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 586cf62f-dccf-3a33-9f6c-d18adf5926fc | -21.48216 | -56.59322 | 2025-06-04 04:55:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cf05b07-841e-311b-9e12-0d7630fde95e | -18.71772 | -54.18837 | 2025-06-04 04:55:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cca126c0-7772-3bff-98f4-3ddb346fa196 | -20.54319 | -54.1181 | 2025-06-04 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73dc088f-3913-368c-a020-4b27843824f2 | -18.07778 | -54.30633 | 2025-06-04 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4de63ec-4718-3d79-9c91-429529a5ba42 | -23.33833 | -46.77472 | 2025-06-04 04:55:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 34edf136-3294-340e-865f-6a5c3e883aa6 | -20.54659 | -54.11868 | 2025-06-04 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22b9ee6f-59ac-3cbf-b972-11f5ace57086 | -22.04352 | -56.39975 | 2025-06-04 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22d26793-89cd-341d-a682-1803d97a959c | -21.82455 | -57.55102 | 2025-06-04 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cde5e972-f057-3804-987f-3bc5155614a5 | -21.03121 | -55.647 | 2025-06-04 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79d04fab-4e6d-367c-a5b7-e54c72a8bf44 | -19.15896 | -47.82164 | 2025-06-04 04:55:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a70f1242-5449-37e7-a873-5dc883919e9c | -19.43706 | -54.77796 | 2025-06-04 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 886a001e-9fef-3307-9c0f-6378bde11d98 | -20.54602 | -54.12257 | 2025-06-04 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95b2623a-5c0c-35e6-9867-e2bea52a85a8 | -21.24729 | -56.16141 | 2025-06-04 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ecd0583-058c-3fe5-9940-de026d7f537e | -19.43373 | -54.7774 | 2025-06-04 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e6ddda99-b4ca-32ff-b430-ad164c07d575 | -21.1833 | -54.1454 | 2025-06-04 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d598ecc2-e060-3800-b1ed-14b077361d80 | -20.8203 | -54.95184 | 2025-06-04 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16cfb506-bd60-3448-97b6-0c11c731700c | -22.15483 | -55.27451 | 2025-06-04 04:55:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70f91ea8-5741-3971-9662-68c7e6fa4a56 | -21.82121 | -57.55039 | 2025-06-04 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55ba0b6a-da75-343d-b569-5e2c32e84304 | -6.9602 | -42.9052 | 2025-06-04 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| c4408c4f-7109-31c3-a4bf-90e1a27444ed | -7.0169 | -44.5954 | 2025-06-04 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9f9e8eb7-d4f3-37de-8d1a-02fb2645300c | -6.9791 | -42.9034 | 2025-06-04 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| e4b65830-cffb-3e43-9043-59eec39cc055 | -7.0169 | -44.5954 | 2025-06-04 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 72573fa8-8ed8-3a35-8d5a-1db9a08629ad | -6.9791 | -42.9034 | 2025-06-04 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 6f4efb5b-99d2-323e-bfae-057932019f98 | -6.9602 | -42.9052 | 2025-06-04 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 22516e7c-37b2-3ffe-8e38-a18b250cb1ef | -5.22444 | -37.65871 | 2025-06-04 05:16:00 | AQUA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5349a7f8-3dce-3c1e-bd52-324cb911f8b6 | -3.13657 | -41.78546 | 2025-06-04 05:16:00 | AQUA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 7ceb7562-a1bf-300e-b692-47fc66b49738 | -2.58779 | -51.92366 | 2025-06-04 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b759f19f-c264-3dae-ba61-20716040e660 | -6.9606 | -42.90649 | 2025-06-04 05:18:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| f6bdae2a-4339-3695-8bf4-3fefa2ad98e3 | -7.02903 | -43.17977 | 2025-06-04 05:18:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| edce4673-da98-334b-8eb9-5b3417fe5bad | -7.68398 | -44.56733 | 2025-06-04 05:18:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0a0c3090-9285-3328-beca-9026d40f0a44 | -8.06763 | -43.10879 | 2025-06-04 05:18:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| d656931e-15b7-3f05-ae10-0b6c6b480734 | -7.88587 | -46.18491 | 2025-06-04 05:18:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 294290d6-f4fd-320b-94aa-6e473c8de397 | -7.21165 | -43.13071 | 2025-06-04 05:18:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 96a8dc3a-9e97-3578-a25f-77038bdfd8f8 | -6.97191 | -42.89733 | 2025-06-04 05:18:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 0cd95998-6bad-315e-8ae9-ec567164c551 | -7.2231 | -43.12129 | 2025-06-04 05:18:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 31cb4d94-4497-368b-bae1-1a61660d66db | -10.60795 | -44.76393 | 2025-06-04 05:18:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |


[Clique aqui para ver as próximas entradas](README14.md)
