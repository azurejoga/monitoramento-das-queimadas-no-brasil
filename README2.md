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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22f18fb7-11c8-3ad3-a435-5d9f08e4912c | -13.6222 | -45.5838 | 2024-10-29 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 502d0e61-2bee-3fe6-8fd4-7fa420ffd120 | -13.6227 | -45.5606 | 2024-10-29 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 15b22687-9038-3f61-9e82-bae446c82eec | -13.6416 | -45.5805 | 2024-10-29 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 6c4de8c8-8996-33fc-9b7d-d8dc1861117c | -13.6421 | -45.5574 | 2024-10-29 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7481bc39-1de4-378a-a8ea-d04ef8498f93 | -13.6887 | -46.1247 | 2024-10-29 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4f16d3de-a978-3123-8044-8dde8c1e90bc | -13.6891 | -46.1017 | 2024-10-29 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ef2f4db0-1b5e-39a6-873f-c100025e46f2 | -14.1386 | -44.09 | 2024-10-29 00:16:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 19435d41-d645-3b9c-b585-36de017386c4 | -14.1391 | -44.0662 | 2024-10-29 00:16:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 10f357d2-bc9f-34d0-961f-3c6d0dbc9c90 | -18.3615 | -40.004398 | 2024-10-29 00:24:03 | METOP-C | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 796338e5-f252-3999-a391-6b94030316f6 | -17.1754 | -39.418701 | 2024-10-29 00:24:20 | METOP-C | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7681b06f-84c4-371f-b681-0b509473441c | -17.177099 | -39.426102 | 2024-10-29 00:24:20 | METOP-C | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d8e6d08-e2a5-38c8-8c5d-7aa3a1cc7532 | -15.9359 | -41.9744 | 2024-10-29 00:24:49 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b5ed5826-57ed-3a57-80f1-cb7741b77156 | -16.054701 | -43.7159 | 2024-10-29 00:24:54 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7b7a5ee0-f05f-3110-bce3-f6b91591d32b | -15.6941 | -43.2271 | 2024-10-29 00:24:58 | METOP-C | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| bfef3091-348a-3a1b-8065-c79fa8a4701e | -15.3471 | -41.824799 | 2024-10-29 00:24:58 | METOP-C | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f796803-8c6a-30bd-b34c-c9a2486a4c31 | -15.8364 | -44.776901 | 2024-10-29 00:25:01 | METOP-C | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a6d43294-0b6e-3185-b969-76cf4ef99f74 | -15.2181 | -42.359402 | 2024-10-29 00:25:02 | METOP-C | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8cb1a713-ef57-332d-884e-6822ceca7409 | -15.4605 | -43.622002 | 2024-10-29 00:25:03 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 56fb6eda-b6ae-3bf0-a457-66df26ed890c | -15.4622 | -43.629902 | 2024-10-29 00:25:03 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1135d660-4fb1-36d5-94d2-8c3139509f58 | -14.9594 | -43.343601 | 2024-10-29 00:25:10 | METOP-C | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 96da354c-2be5-37bd-a696-f76e391a31b3 | -14.9611 | -43.3512 | 2024-10-29 00:25:10 | METOP-C | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| c238326b-2662-3d82-a1ce-52a85f644e16 | -14.8875 | -44.109699 | 2024-10-29 00:25:14 | METOP-C | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f8077e50-2884-3573-b475-351e5a86edbc | -1.714 | -54.5335 | 2024-10-29 00:25:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 8f014da5-bef6-39c9-9284-43856c30ecf8 | -1.9166 | -46.6025 | 2024-10-29 00:25:17 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 861f9f5e-418e-31ca-b2e4-ca9ff0c2229b | -2.1762 | -46.5522 | 2024-10-29 00:25:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b9bc7928-b0bb-39ab-9382-9c458594c87b | -2.1947 | -46.5517 | 2024-10-29 00:25:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6229b377-cd37-33bb-9f1f-b5e9bed9a4c7 | -14.4875 | -43.345901 | 2024-10-29 00:25:18 | METOP-C | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 918e4ffc-7bf9-35a1-a37e-9ae7195ae8e9 | -14.4891 | -43.353401 | 2024-10-29 00:25:18 | METOP-C | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a4d5aa74-3aa0-32c7-b1e6-6b609db02e5e | -2.3353 | -48.9137 | 2024-10-29 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6d6b16c0-49d8-3457-8698-e4a88131b92d | -2.3537 | -48.9133 | 2024-10-29 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| e592233a-b4b4-3fb2-8989-f36949b34383 | -14.611 | -44.2561 | 2024-10-29 00:25:19 | METOP-C | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9b1dbe09-f8a5-3e08-bc8c-b8a279b3478d | -14.5995 | -44.25 | 2024-10-29 00:25:19 | METOP-C | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3c7e3765-97b0-30f3-b992-260c0bb9ce5a | -14.6012 | -44.258202 | 2024-10-29 00:25:19 | METOP-C | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d3ebfc92-f490-3541-9735-d34422aa216e | -14.603 | -44.266399 | 2024-10-29 00:25:19 | METOP-C | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1448aef4-2dae-32ae-b468-56d7fb483642 | -2.5251 | -47.442 | 2024-10-29 00:25:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 41077a28-b6db-316c-bff5-a76740c07aa4 | -2.6398 | -51.758 | 2024-10-29 00:25:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b76ec937-d8b1-3a1c-9fc5-c4bed58d213a | -2.6399 | -51.7374 | 2024-10-29 00:25:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b3c6cbd6-0ac1-34cd-9f61-ad10dbf2b2ea | -2.8146 | -49.2206 | 2024-10-29 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ab5b2bf8-915f-3eb7-b0e8-67a1f5b948e2 | -2.8555 | -53.3459 | 2024-10-29 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 31b901aa-60a5-3f8e-a3ce-740f4e973511 | -2.8739 | -53.3454 | 2024-10-29 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 45fcddaa-bb2e-3a55-8840-c3a5f45ddb5b | -2.9619 | -54.5304 | 2024-10-29 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 8e9f305a-886e-3128-b1be-b59c03c7b007 | -2.962 | -54.5104 | 2024-10-29 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 33095146-2ccb-3ea7-ba4b-9041ec7633be | -2.9803 | -54.5299 | 2024-10-29 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 223.5 |
| af7dcf0d-9582-3cc9-aecb-f1da7cd72e70 | -2.9804 | -54.5099 | 2024-10-29 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 287.8 |
| 45ee061b-9f45-3ac5-aee6-609a9af4bb06 | -3.0734 | -54.167 | 2024-10-29 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b2b977d6-1a62-33e9-94e5-693d4af5d278 | -3.0913 | -54.287 | 2024-10-29 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 012c860f-94e8-36b6-b986-2aaa0b6877fd | -3.1097 | -54.2865 | 2024-10-29 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 691aa3af-91a0-3d10-ad09-2024d2b1ef66 | -3.1098 | -54.2665 | 2024-10-29 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 1d564db1-cbf2-3cad-ab31-73a9a8f64c6c | -3.1281 | -54.266 | 2024-10-29 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 681e013b-a241-3e56-af80-b6086f32bab4 | -3.1794 | -50.3922 | 2024-10-29 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 3b8b927c-92d6-3c69-96c2-3e7da000a377 | -3.2503 | -46.8709 | 2024-10-29 00:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5db04f1d-180f-3859-8d00-e97649527d95 | -3.2548 | -45.9186 | 2024-10-29 00:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c3b815f8-1b2e-3d54-99ea-2fd50b17ec12 | -14.1606 | -44.067902 | 2024-10-29 00:25:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78ac10ca-645e-3b88-9cf6-418d0b8915ba | -14.1623 | -44.075901 | 2024-10-29 00:25:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1689a16b-14f7-37ff-93e9-4b3de8f9614c | -14.1491 | -44.062099 | 2024-10-29 00:25:26 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72039960-c24b-34e1-b939-8ab40645af8b | -14.1508 | -44.07 | 2024-10-29 00:25:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e698839-bccc-3356-821f-761fad68ac8e | -14.1525 | -44.077999 | 2024-10-29 00:25:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c431f1f-d76b-3b36-8ea9-3c35c4d24b39 | -14.1542 | -44.085899 | 2024-10-29 00:25:26 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf20bcc2-4860-348f-8e7a-a36a40804cff | -14.1374 | -44.342899 | 2024-10-29 00:25:27 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fadd0dc2-451a-3c89-b870-e67273679d86 | -14.1391 | -44.351101 | 2024-10-29 00:25:27 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcd05f66-19a2-348a-ac8b-2e02f7f4fda0 | -14.1409 | -44.359299 | 2024-10-29 00:25:27 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 610a49f3-9d2b-34ba-8642-fa88471c9162 | -14.1715 | -44.6479 | 2024-10-29 00:25:27 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac0fd0b-1b86-39d0-b05f-18d44466526d | -14.1733 | -44.6563 | 2024-10-29 00:25:27 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15baa615-7919-33f2-97c5-54a4c53eab63 | -14.1751 | -44.664799 | 2024-10-29 00:25:27 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0af4496a-363f-330f-96ea-c4099bd7b7de | -3.9289 | -48.3458 | 2024-10-29 00:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6583e2b8-0eae-3193-9942-f26ec2d49d84 | -14.0048 | -44.0112 | 2024-10-29 00:25:28 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02efee04-93aa-3294-ad46-60f649d16f99 | -4.1024 | -50.5271 | 2024-10-29 00:25:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a0fac189-5ef7-35eb-8d78-fbce27739b24 | -13.9031 | -43.9678 | 2024-10-29 00:25:29 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e675bc5c-71b8-38a8-9fc6-1e03f24aed1d | -4.3473 | -43.779 | 2024-10-29 00:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b3b704cc-92e5-3f62-b585-880ef1abaa71 | -13.8933 | -43.969898 | 2024-10-29 00:25:30 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18d7e43f-f66c-36b6-a322-71d97fad28bf | -13.8639 | -43.976501 | 2024-10-29 00:25:30 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7e0a55b-6e45-34c5-9ef5-254dc6b07d50 | -13.8656 | -43.984299 | 2024-10-29 00:25:30 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c83e91b2-2322-39b3-8b7c-6be63a315d9b | -4.6431 | -44.1992 | 2024-10-29 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 48f9de76-e8d3-3ccd-90ef-63018e3eb390 | -4.6432 | -44.1762 | 2024-10-29 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| c3c91ad0-5427-3c75-8bf4-926468fb91b6 | -4.6434 | -44.1533 | 2024-10-29 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 33bfc631-9320-3b53-87e7-57c3e75263fa | -4.6618 | -44.1981 | 2024-10-29 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 37a1a041-8afe-385e-ac9f-7e5d52b7964b | -4.6619 | -44.1751 | 2024-10-29 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 347.1 |
| 751009e0-2672-31cc-afaf-f4406af9ff7d | -4.6621 | -44.1521 | 2024-10-29 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 5ce6ccfe-3aea-3aa9-98f9-4bc10f43b978 | -13.7467 | -44.051701 | 2024-10-29 00:25:32 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26900c8d-2819-3fef-9d45-959adf4ac3b8 | -13.7369 | -44.053902 | 2024-10-29 00:25:32 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 333efc8d-e952-37b0-b2ef-ac8f270a5b38 | -13.5666 | -43.410702 | 2024-10-29 00:25:33 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f04ed899-49cb-31c4-b98e-4caf5e74b510 | -13.5683 | -43.418201 | 2024-10-29 00:25:33 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6fc561dc-4dc4-3f14-843a-632499257600 | -4.9326 | -45.4321 | 2024-10-29 00:25:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| f93c5ffa-89b2-315c-b223-e61830c01cf0 | -13.4171 | -43.150101 | 2024-10-29 00:25:34 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fdecc9be-002c-326f-b6d8-99b741e2624d | -13.4187 | -43.157398 | 2024-10-29 00:25:34 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 707ac47b-c55a-31c4-9ec4-2b5c40cf6daa | -13.2573 | -42.798901 | 2024-10-29 00:25:36 | METOP-C | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 40cf0d86-477e-3447-887b-988dccae3dc4 | -13.3134 | -43.569199 | 2024-10-29 00:25:38 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c121e2c2-f3b2-3428-9996-31693c484447 | -13.3151 | -43.576698 | 2024-10-29 00:25:38 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0db9e23b-c94c-3d77-9a93-ef53468f5d53 | -13.4033 | -44.410801 | 2024-10-29 00:25:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac069b1a-232c-35e0-80eb-1b45784c3414 | -13.6396 | -45.573299 | 2024-10-29 00:25:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 817a5b38-d0c1-3a2c-8395-4186536ce672 | -13.6416 | -45.5826 | 2024-10-29 00:25:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3b4ed9d-5a26-31b1-82f0-95ecda1f1ebd | -13.6435 | -45.591801 | 2024-10-29 00:25:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59aecbe2-213b-3782-aa3f-92d9adcddaff | -13.6279 | -45.5662 | 2024-10-29 00:25:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf8d4e72-2626-3488-aac4-047b16e6752d | -13.6298 | -45.575401 | 2024-10-29 00:25:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31c2a35a-7693-3ea1-96f9-51e804ff6671 | -13.6318 | -45.584702 | 2024-10-29 00:25:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59b0ddbc-6305-31d9-9dd7-38bfeb7b1a30 | -13.6337 | -45.593899 | 2024-10-29 00:25:39 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f535994-69a0-305e-8cd2-c5626a7b46b5 | -13.62 | -45.577499 | 2024-10-29 00:25:40 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 220faabd-988f-3463-95bd-850256d70e33 | -13.622 | -45.5868 | 2024-10-29 00:25:40 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6ceef8b-87c6-32f8-8f8d-5fd6891c9c8e | -13.6239 | -45.596001 | 2024-10-29 00:25:40 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1319397a-bdd5-3cf1-b7c9-242af7b562b0 | -13.6083 | -45.5704 | 2024-10-29 00:25:40 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
