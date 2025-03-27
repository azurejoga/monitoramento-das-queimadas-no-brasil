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
| 65bd91b1-12d6-373f-acfd-a52e2566bbb7 | -21.69618 | -50.36546 | 2025-03-27 04:51:00 | NOAA-21 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d1515509-fd99-3a90-96a5-ca62ce2b5cba | -25.19439 | -49.32891 | 2025-03-27 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f17b0f7d-bb67-38eb-8a94-512b7835bee9 | -23.4086 | -46.55592 | 2025-03-27 04:51:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1b53599f-cd73-33fa-8a8c-4802447ab41b | -21.09619 | -56.04385 | 2025-03-27 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74a6ceae-f2bc-30a5-8a28-bdad213f2614 | -21.23014 | -56.25555 | 2025-03-27 04:51:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25f1727e-b3bf-3b03-937d-a46039afc392 | -21.83252 | -47.0355 | 2025-03-27 04:51:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed4a2fdb-7b7e-3215-bae2-7e296f11b358 | -29.69037 | -53.85981 | 2025-03-27 04:53:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 797d84e5-51c0-3188-966d-7316bcb3ec66 | -29.34287 | -55.93215 | 2025-03-27 04:53:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 7034e710-3868-3e60-958f-c9098ae60b10 | 2.36652 | -61.01704 | 2025-03-27 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c3cd305-906b-3616-b898-c4839f8be340 | 2.02464 | -61.0927 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eb4ff16-0b1f-31a3-8dd5-290ab0e81037 | 3.97051 | -61.55039 | 2025-03-27 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48a1a765-ebef-39a6-a76b-56b363b10792 | 2.02099 | -61.09727 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc3befa0-fdfe-3ef4-ab17-904cb1f3fea1 | 2.18327 | -61.8152 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97865ee4-fc23-37ce-b69c-54d7be7d3974 | 2.03437 | -61.09923 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 159fdf5f-f547-3dab-bf6e-002d4fd21fed | 2.02038 | -61.09335 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb8d105d-6382-3d34-b316-03081775e1ce | 2.02585 | -61.10057 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50d89f07-470f-3ea0-a9b9-f60271181c57 | 2.03133 | -61.1078 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8b6420d-c453-321c-8b9f-8b9de72dcc56 | 2.17943 | -61.82028 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 777456ce-b73d-3f38-9ec7-30d09ffd5f5f | 2.03498 | -61.10318 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48a7d2f6-c6f2-3e5d-9ec1-595309ac6113 | 2.03011 | -61.0999 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ddd1f91-8ffc-3ad1-bf2d-3fea5c928a52 | 2.01612 | -61.09399 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 356311cc-692b-30f9-9afc-17724b04d04f | 2.02524 | -61.09661 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 036914c6-e73b-3aad-a15d-afd13d183033 | 2.03072 | -61.10386 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2186300-469e-3ffd-8ce7-64f98c03edc9 | 2.18188 | -61.81747 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb3e5683-11e0-38ed-aa88-2532e21402a1 | 2.0295 | -61.09595 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b0e0c03-6d32-3584-a433-1a72f914b17b | 2.03559 | -61.10715 | 2025-03-27 05:08:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e9970f4-6ac8-363a-8581-d3d0e4c8fdad | -7.2401 | -44.78058 | 2025-03-27 05:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 684168e2-7119-3d68-bf4a-756603346b8b | -4.36228 | -48.66881 | 2025-03-27 05:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 065a4a96-f919-3d1a-b5db-b5d0923cd650 | -7.23343 | -44.77954 | 2025-03-27 05:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc8c03d4-6347-3efe-a060-3875256fc2e7 | -7.23592 | -44.77894 | 2025-03-27 05:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2fbcdf3f-e588-3f5a-bd1a-191ee217e71f | -21.69705 | -50.36534 | 2025-03-27 05:14:00 | NPP-375D | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2bbf7b53-722b-3570-b4a2-90a613c8a80e | -21.23805 | -56.46626 | 2025-03-27 05:14:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fea475b7-018b-39db-b8ab-69b5ba9dc337 | -21.69415 | -50.36404 | 2025-03-27 05:14:00 | NPP-375D | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 09defdee-c4b2-3950-ba34-974e1434814d | -19.42328 | -54.78422 | 2025-03-27 05:14:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 955a85d7-a284-3c93-b4e8-53ad8a8ab597 | -21.6998 | -50.36456 | 2025-03-27 05:14:00 | NPP-375D | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 50b34776-66fd-3867-b016-30472d0fbbff | -19.42375 | -54.7804 | 2025-03-27 05:14:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac35ab35-99f7-3328-9649-b0d6f552c064 | -22.15088 | -56.12736 | 2025-03-27 05:14:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd3b38cc-8e69-3fdd-b253-290737ca3286 | -25.19124 | -49.32897 | 2025-03-27 05:16:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cb4faed8-1561-3622-9393-6e1d6ef658cb | -23.98377 | -48.90983 | 2025-03-27 05:16:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a329b8a0-8fab-3d49-9962-30ac152d1865 | -25.19787 | -49.32398 | 2025-03-27 05:16:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0998a0e4-939e-354b-a24a-12c13b821550 | 2.18072 | -61.81974 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b98ef0b-3203-32d8-b54e-cd8eb476fd24 | 2.18678 | -61.81527 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddfa29c4-838a-3385-908d-224967f88797 | 2.03319 | -61.10084 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50dbd467-a6ef-3ea7-99aa-bfcc6c0447a4 | 2.03265 | -61.09739 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0ee3908-d818-3f67-ba5c-e46cf5cfca97 | 2.38963 | -60.23995 | 2025-03-27 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42a15b58-02c4-3a71-b32b-a994834d2e38 | 2.02657 | -61.10186 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c661fe41-daf0-393f-a356-eea170f5e412 | 2.1923 | -61.8074 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4dc0a6e-fc12-3a28-af61-90b712f0ebed | 2.18624 | -61.81185 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aa2c740-ba82-3212-9dac-882516b31300 | 2.57569 | -60.27224 | 2025-03-27 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e1702e3-3e87-3194-a62c-66de78f6f700 | 2.1857 | -61.80843 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea0bb3ab-2e87-3544-8699-982c1d0f92c7 | 2.18018 | -61.81631 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 109eb31c-66f4-344a-9fa4-0b5200b28b3d | 1.16122 | -60.50626 | 2025-03-27 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20907c08-693f-3b85-9aa9-de3d9125d67e | 1.74543 | -61.06414 | 2025-03-27 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5deb783-3a67-3b0e-b641-aecbaa268240 | 2.03428 | -61.10773 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 848c1041-5e61-3ca1-b648-ef3d1a8a05cf | 2.19284 | -61.81082 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 286e1d2c-14cc-3796-bf5e-7b65bce745f0 | 2.02603 | -61.09841 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad3f6214-949d-3db3-bc42-2f535dd8081a | 2.0365 | -61.10033 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2c7e0d9-7931-3dd1-9acf-2f0429bf84ec | 2.02163 | -61.09203 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c156d3-3cc7-3369-838d-fdbb97f6c50d | 2.0288 | -61.09445 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c21cb0c2-6f76-3593-b4d5-2926f64e7c6f | 2.18954 | -61.81133 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f4a844e-4881-30de-aff9-dc5f41b1addc | 2.03759 | -61.10722 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 354cac82-4b53-33ee-b7ec-e3944a5f75c3 | 1.96696 | -60.51202 | 2025-03-27 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6e345fc-36b4-3299-a19d-73158ec1e543 | 1.96418 | -60.51605 | 2025-03-27 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d7d93bd-e7d4-3534-98c7-5af3a6f8380a | 1.23455 | -60.5643 | 2025-03-27 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2dac106-92bc-3906-a8c0-b4c882d77d67 | 2.18348 | -61.81579 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ab003f3-7d8f-3ac1-83b9-702b09aaecdc | 1.24136 | -60.10371 | 2025-03-27 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dad73771-3d6d-3a7f-9f6a-83433188400b | 2.03373 | -61.10429 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef871ac4-f7ac-3216-a152-a0692ac1b3ce | 2.19338 | -61.81425 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88aaecaf-2890-38c1-8e52-82b5cd4ac050 | 2.02934 | -61.0979 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64ded512-bd2b-3bf7-9d4e-871e977e85d4 | 2.01833 | -61.09254 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d14b2892-305f-33d3-8cf2-3e545f21a88d | 1.96752 | -60.51553 | 2025-03-27 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 148b881a-7520-3146-ab06-9a5aa68edf94 | 2.02549 | -61.09496 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42f7b362-a068-3304-97bf-a466e760a384 | 2.19668 | -61.81374 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04ea7c60-7222-337c-9c4f-bd1c382066ec | 1.11098 | -59.47437 | 2025-03-27 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3440aba6-966a-3733-ab8c-454b4bb02c87 | 2.02272 | -61.09893 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 271b2b5b-1a2c-3881-b1ef-c6141c9f9d11 | 2.03704 | -61.10378 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 982aac70-5bcc-381e-b331-b81fbe184cf3 | 2.189 | -61.80792 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2e88fef-8af1-3858-b015-6b32d1eabaf9 | 2.02988 | -61.10136 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a44dbd10-1a0c-3f24-99ac-2e13c66d3d3b | 2.19614 | -61.81031 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aeea7572-ca74-3fac-a518-8f3d9e94e174 | 2.02218 | -61.09548 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9481a95-68a5-3d62-a822-948d1a19670b | 2.01887 | -61.09599 | 2025-03-27 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


