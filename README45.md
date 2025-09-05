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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d329328a-42a3-3f6d-9ca8-77d9496a75b6 | -11.61313 | -47.78571 | 2025-09-05 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b1ee043-670d-360c-8808-fbced2c6eebb | -11.67679 | -57.34763 | 2025-09-05 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae47002c-83fc-39c5-a817-2bef79c0096b | -12.9726 | -48.08265 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af6c9711-cbe0-3152-ac3c-5060f25db241 | -9.08138 | -47.00597 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 42fd19e2-db2e-373b-be05-e6d7235624dd | -9.97214 | -51.63761 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5bc8191-e337-3a8d-ad2b-63df5bdd282c | -11.65709 | -54.52205 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adea2288-4736-3e9e-937f-fdd3cb794c85 | -9.96724 | -51.64439 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b0aa0df6-1855-3f9c-a6bc-5a4426f2ae4e | -12.50292 | -53.84297 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8933c743-50f8-3226-8969-8d5819d51a2a | -7.05308 | -50.8555 | 2025-09-05 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ab7c32a-0740-3496-bd71-111d0f26dc1b | -12.88819 | -48.0182 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec9ca64a-f053-39b7-b095-a16aeeb58aaf | -8.17835 | -61.19548 | 2025-09-05 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 593e2963-5d47-33d9-af19-3570abcdba6c | -5.49319 | -60.12809 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06d8ce43-454e-38c4-a262-91b28c0a6304 | -8.19119 | -49.60378 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b03b40b-f253-3646-a89e-8a77157bf066 | -9.49731 | -57.81985 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb1f8eff-662b-3045-85ac-8568a6b4c3d1 | -12.94669 | -48.05641 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ec2600b-a68a-3804-ae06-64c59ada92f0 | -10.03642 | -48.13998 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a704755b-3a99-30bd-8123-cedc793bc53e | -12.97927 | -54.78927 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a22c335-5e36-36a1-91da-53ba3e7c032a | -9.06592 | -47.0101 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97b4d6ad-a72a-3dcf-97de-77d18712bf70 | -10.99812 | -46.02395 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9aef8d99-2d6c-3df4-ad52-34e5c877661c | -7.95895 | -44.95487 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1588d10-49f7-3439-8889-03ca0b0ad717 | -10.47651 | -53.63765 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f14863f-58fa-3719-a319-7ee4d7827cd6 | -10.98036 | -45.94797 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44146d96-a484-389e-bfaf-78ebd844529b | -5.91266 | -57.71605 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2082e31a-110f-3875-ac1e-5710b39fe28d | -8.92037 | -45.11635 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36156c10-6e04-33fd-9efd-215016b1ff6c | -12.98096 | -54.80058 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9211e1bd-918d-3941-9412-52d47e8aa0fe | -10.9687 | -56.21836 | 2025-09-05 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3094f439-8072-386e-b5e3-6d14b1afa5f9 | -11.00894 | -45.93822 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e719308-e51c-3856-8d26-e365e4d466e4 | -11.67905 | -52.16337 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddafa460-43bf-30c3-9731-a0a1a8ed2f94 | -6.32971 | -58.1749 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae568d0f-e3f2-3791-bf89-bda5553c3914 | -11.19858 | -55.02506 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93f4ca7c-5811-3a48-ba55-36b88ad869ff | -12.32246 | -47.04857 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa5c01d4-3889-32e7-8925-2c5dbccc62c8 | -12.61564 | -57.00816 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7961fad4-1653-3dff-b2fc-ea5a4d40b3f3 | -12.44124 | -48.08689 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a770159c-b553-303a-a931-cdacf19dfb03 | -5.9024 | -57.73222 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30692d2b-79b9-312a-b1f4-452cc5d39490 | -10.03179 | -48.14139 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e54e067-ebf8-3632-939a-853a0095dda6 | -11.62818 | -52.2079 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d90d4b80-61af-3abf-8e9a-8489c9b2525d | -7.68497 | -50.26008 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf71a859-215e-3b0a-9ac0-afee6f48321f | -12.97986 | -54.80776 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f2ac1fb-dc92-3390-8e13-88993cbac962 | -8.19224 | -49.5967 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 634d4665-78c3-3ecd-aad4-56d4fcdf89da | -12.88658 | -56.94418 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8af190e-57d2-3248-8d60-0a5a82d67945 | -10.97823 | -45.94456 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22fc9ad1-0e91-3ec2-8d04-10fd0979ccbc | -13.35103 | -46.83393 | 2025-09-05 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d38f8776-6755-3ea7-ae07-c375ef5ba6be | -5.90023 | -57.74537 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03183146-7b1c-30fc-ac35-97f4c42b83d7 | -11.60249 | -52.17531 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e7f1718c-b6b1-3ec0-afd6-40696e314ad4 | -8.91492 | -45.11501 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd6cb168-0f64-3fc1-9dd4-a0a4ba86fbcd | -9.79694 | -48.31238 | 2025-09-05 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8f6ab28-e52a-3f4a-b028-30bd9f416ac2 | -12.52009 | -48.07596 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 234a3225-fb0f-3712-bd6f-582584df2946 | -12.996 | -54.81401 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ccf10355-7dd5-3d08-9c8f-70f2c8a6d0d8 | -12.99376 | -54.8063 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 171b614b-3a81-34dd-9e2c-da5201d0f2ce | -6.74316 | -58.72341 | 2025-09-05 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b9aef2a-bbfe-3abf-8e3c-5bc7a1ae5dc7 | -7.04874 | -50.85926 | 2025-09-05 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4cafd9c-10ee-35a9-8450-e42466172668 | -8.52261 | -51.31503 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 241a2f4d-5a45-3b28-aad7-889bc3b433f0 | -8.93688 | -48.65147 | 2025-09-05 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1516f10-ab4d-38ba-8660-3df4a4e1487a | -12.98653 | -54.80883 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71946e89-25db-3f76-bc70-fe0380edc225 | -8.89844 | -45.79067 | 2025-09-05 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3f8c0da2-72bd-30e3-8073-3911896f4a3f | -7.60951 | -43.84946 | 2025-09-05 04:57:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33ddbf0e-4d32-3b8b-82a8-573934f0fb20 | -11.64487 | -54.53476 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0eb18d1a-99e5-3db1-858b-092fabe796b5 | -11.60012 | -52.16629 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bad5de23-8dbe-3717-b380-db6ff52f50d1 | -12.96145 | -48.05506 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35852954-2fac-32e0-9bb3-4891fd68a261 | -8.77795 | -49.62634 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5b53eac-0584-38da-ac59-ce33edaa3cb1 | -5.90681 | -57.7285 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7240bc8c-13a9-301a-a457-22ef79c5f05d | -10.0656 | -58.39291 | 2025-09-05 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dc5a8b0-1283-3457-816f-64c9adb11de5 | -12.9624 | -54.7942 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1efd4f99-7bd5-3cd6-aec7-757e179d9ab1 | -6.33426 | -58.17094 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b526b569-fa1b-3e11-a488-161db030ea54 | -12.93678 | -48.05741 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8161dbea-fb7c-31ff-9450-c8b859bec95a | -11.10207 | -52.02824 | 2025-09-05 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16dcfe7a-e294-34f3-9b34-421dd31e1df6 | -6.32621 | -58.17192 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8af42c4d-4424-3c56-a671-cc4ba8eb2915 | -12.90184 | -48.02608 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ba22c95-0c2d-3171-80ff-21145d4b4b82 | -11.74368 | -47.75692 | 2025-09-05 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4bd4264-ba8f-36d2-8833-f1f9c7e44744 | -6.86976 | -52.79081 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4135b203-9036-32f9-b5c1-ca3d095c3381 | -7.72087 | -61.52479 | 2025-09-05 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cc0ed21-7123-31f6-8090-fe27553359cb | -8.0833 | -45.33015 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 453ab3cb-6fe7-3494-ba02-8c0f5b996ee7 | -12.98261 | -54.78979 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 043284f0-2b65-3fcb-b6d1-3bb101dfdb9d | -5.89725 | -57.74044 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80d7f841-824b-3a92-91eb-15505e5bcf37 | -8.48303 | -45.06904 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72f0dd68-b6b9-3e37-89e7-5d10e77792ed | -10.09642 | -48.0772 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89abcf43-faf8-3c52-829f-8cd6c19c3bbf | -9.54474 | -59.73593 | 2025-09-05 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c69628b8-26c5-314b-9e6c-8ff755f793a7 | -13.2649 | -51.85059 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64d50cb0-c41a-3dee-8013-84cc6ba71b91 | -11.59949 | -52.17054 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06bd1cf7-6acf-3468-a0b1-5b992918f0f9 | -12.97094 | -54.79898 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88263c21-ccc8-37b2-99a7-b8d381b88358 | -6.87214 | -52.78376 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 370d18ae-7a8f-360f-ae78-7cb2bc2c44df | -10.23073 | -50.54475 | 2025-09-05 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e501fc9-31b3-3d00-a102-bea9729f628a | -10.0696 | -48.06775 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 488b4a6c-4410-3bf3-96e1-120f8c9c70d9 | -12.52564 | -53.80803 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcb30d8e-7ccd-3787-aebd-3c453044a1ff | -6.49401 | -55.89175 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97c64552-114a-37de-91c7-7de644307bb5 | -12.51533 | -48.07531 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df69f9d7-8bdb-392c-b0e2-65f3c2e11039 | -9.61343 | -55.02182 | 2025-09-05 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 497a947b-6c94-3766-839b-9157589a72b2 | -13.10388 | -57.11539 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30fdbcaf-7758-388d-b7a9-e0ab5945c4cd | -12.90947 | -48.04262 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f39c292f-2359-34d7-ae26-78375df55661 | -10.30482 | -46.35358 | 2025-09-05 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a151d27-e5e0-32a8-9a39-20b81e4d2d8c | -12.29295 | -50.02337 | 2025-09-05 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6765016-2daf-3e51-8d74-ece1692d6c27 | -12.29711 | -50.02396 | 2025-09-05 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78203d3d-8ce2-3acf-99fe-e7918b009372 | -12.97204 | -54.7918 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4cef17a-b139-3378-ae33-42b7e4546231 | -10.44548 | -53.61401 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b1cc8f8-2ba6-3ee4-992b-d81c6ad137b8 | -13.65863 | -47.92969 | 2025-09-05 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27ee9723-db76-3dc7-8922-7906cdc2940b | -7.61822 | -47.94783 | 2025-09-05 04:57:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 832ab98e-debd-3b80-acc2-a113dd382a34 | -5.91419 | -57.72977 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f95daf6c-f4c1-3b27-ac52-815f468e9586 | -6.77368 | -55.48623 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 326e6b66-234e-337a-b50e-2f2a6b72652c | -11.00118 | -45.91276 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b88fd96a-5965-3a83-9e45-93671fa92463 | -12.96296 | -54.79061 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README46.md)
