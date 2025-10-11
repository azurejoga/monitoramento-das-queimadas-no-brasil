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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58fad51a-5cb9-3d06-9ec2-66573e989f55 | -17.20799 | -47.65752 | 2025-10-11 05:04:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d70ee4a4-c37f-31e3-999d-59bf2069b962 | -14.74337 | -46.13593 | 2025-10-11 05:04:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 329c141b-5425-334f-86c2-c32104aa8a3a | -15.221 | -46.38512 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 838694da-ddb9-3c76-b641-4a3fce6c95d8 | -18.0778 | -57.52862 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8333c099-6d52-34e1-bcd4-d0a1045daa7d | -17.26816 | -46.89906 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd069ec4-5288-3356-a050-d4630f93841f | -12.0893 | -63.86052 | 2025-10-11 05:04:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96a5f310-c085-3a66-ac78-a9e22f7cce96 | -15.17094 | -56.72944 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 755b6042-9e49-37fe-a55c-8ecdcceff880 | -15.20016 | -56.79684 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01edfa23-f1c9-38b7-8fec-b2a7381862fb | -14.27501 | -45.90497 | 2025-10-11 05:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca647f9d-df57-3760-91ac-bbe2d5e19622 | -17.82472 | -57.62749 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 96e490d7-0707-3354-9a6d-d3e6402c36cb | -15.01615 | -56.01618 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecfdc0c6-597a-3340-8d4e-1f3b7abb81c4 | -14.92785 | -46.75655 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f9dd4bb-5551-3c13-8327-8ded74d99e6d | -15.20033 | -56.85977 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a3e6cc2-3917-3d1c-ae63-1c4253202dd3 | -15.86521 | -56.7422 | 2025-10-11 05:04:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83cac5ea-c34b-3477-a979-c4fd7cf403ed | -18.07171 | -57.52375 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ec2b46f3-3de9-3565-80ed-b4b8a2d49dbc | -13.08275 | -54.8487 | 2025-10-11 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 662f3b8f-d5e1-3776-b7b3-14b7a6900f22 | -17.82197 | -57.62327 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ea1a8429-1545-3a76-9037-382d88f85335 | -19.50613 | -57.47377 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 709185fa-369b-341e-b3e8-31eeda5b4e0a | -18.06971 | -45.02408 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0f36b78-9e3e-3fd3-896d-09aa916e29ee | -12.09429 | -63.86146 | 2025-10-11 05:04:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f319aea-865a-3075-805f-53edeb086ee5 | -17.83731 | -57.65604 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7b3dfb66-6942-3671-aeac-e1b6dcaffa34 | -14.94022 | -46.74495 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4baa9c1c-182e-3434-8364-32c29f022f32 | -17.89931 | -57.66721 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d89e723c-2830-3813-9bba-2996641978c2 | -14.95709 | -46.75146 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 010a2e55-0e2f-304d-bcec-9a3d4e94557d | -14.92827 | -46.75298 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bcf55e0-13a2-378a-886b-7ae0575eeff8 | -15.70062 | -46.62936 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7a4cd7a-1bff-367b-8483-199e0235680d | -15.16484 | -56.83188 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58dd1268-1ef4-3929-b624-b1cd8e845d78 | -14.95622 | -46.749 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fecac737-ecea-35ea-8970-8506f550a826 | -14.95165 | -46.751 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76e736f6-eded-31c7-983e-83acd5c56671 | -13.07884 | -54.85176 | 2025-10-11 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94aaa367-69b6-3cc0-abe1-5c657a215364 | -14.94709 | -46.74269 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa97bcf9-3e5e-30c4-afbc-4036950cb0ff | -17.84399 | -57.65725 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3f538fe1-9fe8-3be1-8bce-2f531cbc7f40 | -17.89537 | -57.67028 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 39b48beb-33fe-389f-9323-cee6c3fb34c3 | -15.18696 | -56.85756 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f212b34-95f3-30bf-a1b5-81804d6c0ec2 | -16.29814 | -47.17189 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2076012f-8653-3855-93f5-b1a109b8ee24 | -15.40858 | -47.30333 | 2025-10-11 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e52cd9e8-64b5-31ef-b0ea-1090095f8144 | -18.24137 | -55.37893 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d4ee49d6-8d2e-3f46-b8f7-a028ed645007 | -15.18316 | -56.7534 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 948dd055-eac5-3001-ac7c-52ecbbaf73cd | -18.0364 | -57.55122 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4286c677-1109-3f30-922a-f1d7f2f0bbe6 | -13.59732 | -56.93928 | 2025-10-11 05:04:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 448dd53e-8d7f-30c5-b638-5fb870f50e58 | -18.07329 | -57.5353 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f5a00b3e-a419-3b61-bad6-6fa8046a1274 | -15.19699 | -56.85921 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f993dd38-8a17-358f-9774-bf5deb6954a3 | -15.15714 | -56.81578 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc2b5177-8fcb-3dc7-87d6-b2c79660734a | -15.42196 | -48.0281 | 2025-10-11 05:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f97eb95-5d9b-3f82-8f82-3301ec21b098 | -14.6572 | -56.21361 | 2025-10-11 05:04:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f93c22ba-82ed-3972-b5af-21bac9747ba0 | -14.65776 | -56.21004 | 2025-10-11 05:04:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5708cffa-a24f-3ad0-8ec3-5a841ed54dd9 | -15.69511 | -46.62868 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46bb2478-868d-379c-a211-b935d08174c5 | -17.8379 | -57.65233 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f6acc918-fc89-3596-94ca-3154def45615 | -15.69462 | -46.63282 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9524f2ad-73db-37db-bacb-8acebaa87402 | -15.17152 | -56.72582 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fca8020-9f23-3644-a108-f6fe1089acb3 | -14.93407 | -46.75039 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13252238-0c14-32d8-865c-a3f9494ccd58 | -12.09594 | -64.23658 | 2025-10-11 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb65846e-de28-3e01-b8ca-335b4200cfe7 | -15.18083 | -56.75326 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c0dde5e-6d59-312b-b3e5-0302fc5def00 | -15.18925 | -56.75811 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ebb0ca8-b50f-3b83-9b25-b85511a3f017 | -15.19958 | -56.80046 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4809168d-3203-3c78-97ef-51420744cd47 | -15.40897 | -47.29988 | 2025-10-11 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bcf36c3-530f-303c-9eee-70807fe08807 | -17.84184 | -57.58535 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 97f1a013-0203-3731-a2d9-c8de3ac4e2cd | -15.18796 | -56.78746 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed364b75-69d9-372b-b183-a2098296b30a | -17.83218 | -57.6665 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 04ea4608-d6d1-3ca6-bb21-1e74331c5831 | -15.31738 | -46.18652 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3dd842b1-dd8c-3cdd-8cd0-a8b219ab4871 | -17.20836 | -47.65427 | 2025-10-11 05:04:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c613560-f2ae-306a-9404-5ab6deeceb52 | -14.9266 | -46.76711 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a1f9aea-d102-30bd-90cd-bbbdf12573b1 | -14.95671 | -46.75486 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca186b08-5498-372e-80a8-4d5b699a5d8f | -14.02024 | -47.06258 | 2025-10-11 05:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ca5b98d-b55f-3d74-9e8f-753f754b6bd9 | -17.83612 | -57.66342 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9eb52464-ed48-3f61-aff0-18bf41774613 | -18.07427 | -57.55057 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cee7585e-defc-31ff-92cc-38af81171293 | -15.01989 | -56.07927 | 2025-10-11 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e881f701-b369-397a-903e-12e834467fd5 | -15.2725 | -56.9123 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62c68b7c-8833-3643-85ba-5a4bf1a7a51c | -18.07486 | -57.5469 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 880542fd-207c-3ef3-8ba5-8c42c5fe70a9 | -17.82669 | -57.65785 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4b0977dc-b71a-30ca-8b10-7d8c45a41e66 | -18.02913 | -57.55373 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 79171db9-7609-3b66-8ab5-9c342f4331bc | -15.15875 | -56.82716 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78e6d5dd-d796-364a-9b48-b3c0d0bd072b | -15.86854 | -56.74277 | 2025-10-11 05:04:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac1318fd-657f-3f68-938d-65cdc7c15c94 | -15.20548 | -56.74234 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b38b30b-76bf-3ea2-ad30-c7cf1ee32c14 | -15.1737 | -56.73359 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bbfe11f-2032-3bff-951d-060b4ddf2330 | -13.66887 | -48.74974 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbd69d4e-b905-318b-bae4-8644697e9762 | -14.43798 | -50.35074 | 2025-10-11 05:04:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e9de9f8-8838-3f93-bd38-7642827ddb25 | -16.29851 | -47.16853 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a688bd2-419c-3972-bbef-b8bf8199a8ff | -15.7413 | -48.97131 | 2025-10-11 05:04:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c69200bd-4e00-3e76-a197-e36198ebab0c | -15.18203 | -56.84562 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cf98cfb-8243-34a4-9de0-5fae721c98ff | -11.78679 | -63.18763 | 2025-10-11 05:04:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8d99cf6-04fe-334c-86b9-933abe0ca211 | -14.27594 | -45.89699 | 2025-10-11 05:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54e148c8-0c5b-3950-b503-aebb4ef31c7c | -17.26899 | -46.90001 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1917f220-dddd-3dd1-a05e-2fffa6397f3f | -12.40128 | -63.95485 | 2025-10-11 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcbbeb9d-9f83-34f1-9ad0-33e937421b9a | -15.21368 | -56.86198 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe827c41-eca5-34a1-86b9-fbefc7376e30 | -14.9467 | -46.74618 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e101635-fbc2-3050-89ba-acb25ff5ba2f | -15.69487 | -46.63178 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 190377d3-5871-3669-91eb-42f7dcc29c95 | -18.06816 | -45.00418 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afcce539-d179-3a47-a19b-16aad983d761 | -15.17427 | -56.72999 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06727949-ce62-3ee2-a66a-240d5f91631f | -15.40893 | -47.30207 | 2025-10-11 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c50f570c-7b84-3927-85b8-cb71b678fef9 | -16.31031 | -47.16021 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| decff8fb-d786-3ab1-a475-169a26d7dcb5 | -17.8261 | -57.66156 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5c128eb6-f718-3d76-b99e-bccbc8cb19fe | -13.59396 | -56.93871 | 2025-10-11 05:04:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70537df5-e2b3-3cb0-9865-c2dd0b761fc1 | -14.95502 | -46.75898 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe1fc4d0-bcc4-3b48-ac33-7802c62d9f8d | -16.30346 | -47.17284 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a5faff9-d53b-306e-9a8e-4f580a86d588 | -15.49208 | -47.98873 | 2025-10-11 05:04:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea7353b7-9087-3fb4-8886-07cf33c34af3 | -18.04796 | -57.56475 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 01e25af8-aae3-3958-96f6-32da5100f262 | -15.01436 | -56.07101 | 2025-10-11 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c93919e4-e187-390a-a0b5-e8e158ff4778 | -15.18421 | -56.85339 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 296a02b7-bf3a-3a9c-a87b-d91c4112dbe6 | -16.30421 | -47.16615 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README40.md)
