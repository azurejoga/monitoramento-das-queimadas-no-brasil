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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f62455cf-26bd-3686-be41-9bdc6ebcde63 | 2.70009 | -60.23067 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7d43b558-2038-309c-9ab5-4d603c9ba7c0 | 2.70192 | -60.24255 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3aac9eec-4355-3414-8bb0-8f876ff91519 | 2.71018 | -60.22855 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 65aa82e2-3315-3ce6-acf6-f78d88070c34 | 2.55139 | -60.73514 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 09838bf3-05b0-3233-86cf-8aaea9a667da | 2.70347 | -60.22952 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| afae84ea-4708-3ea8-b892-ae656ae478f6 | 2.68669 | -60.23267 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d260b01c-eeb9-31f9-8e72-9bf0a564f72c | 2.6892 | -60.22563 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d268ba01-9bd5-3ea0-832c-21e0f703dbce | 1.94649 | -60.3689 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 99645faf-2568-37f3-9b17-300d77457be9 | 0.07151 | -60.65229 | 2026-02-21 04:38:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3f359d6-9e8e-39e5-8d04-0e1b4115f618 | 1.9398 | -60.3699 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ba4d9b6f-c4cb-32a7-8871-4d0ea9a069c0 | 2.69852 | -60.24247 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 266ec702-b13c-39ad-9047-f865b712d796 | 3.08128 | -60.09595 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb70e83e-e76b-3fbd-b35b-61d6f9ca176b | 2.56071 | -60.55892 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 95cf347e-bcf8-3f75-bfc9-363fbc3b0c70 | 2.68578 | -60.22673 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e4741525-738f-3214-b8c8-c02fca3409aa | 2.55479 | -60.56604 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d42058d-99ce-31bf-81db-e9b613838bc8 | 2.70522 | -60.24143 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| aa3b1655-0fd6-3b8e-b64c-7f582bf57c03 | 2.55069 | -60.72813 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1e5823da-ef6b-322f-8626-7988c3d79273 | 3.08212 | -60.10184 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b589fbc-6610-3625-992f-cea5afbaa4bd | 2.69677 | -60.23058 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb05c170-0d3b-37fe-9faa-8fdd2fce5e59 | 2.56162 | -60.56506 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d661d4d2-eb8c-331f-a368-7e25df5ec83d | 1.93889 | -60.36378 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca2a4850-02bd-3d22-8d68-d93a0cd488d1 | 3.07856 | -60.10314 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b3a57e3-9abe-30c0-a671-73f87741a0e9 | 2.67498 | -60.41255 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 412abbaa-a975-3840-9b38-3b764d9d721b | 1.94283 | -60.368 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a675693b-4fdb-3446-849e-419969ffc5ce | 2.68832 | -60.21966 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a212ba2-eed1-3acc-95ec-a7cd930bda7c | 2.6959 | -60.2246 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99068e6c-f463-3fb6-886b-9fab47f88c50 | 1.94375 | -60.37397 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d042575b-eb57-3406-905a-bfc541146a3e | 2.88469 | -60.59814 | 2026-02-21 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d32516a7-8f8c-3db1-a6f9-30db3a545165 | 2.89062 | -60.59082 | 2026-02-21 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa48c002-c31d-302d-9e36-9ff37e87b578 | 2.67857 | -60.40601 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 698367e8-bd95-36e1-8267-9fe7f9642bad | 2.69247 | -60.22573 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 267321bb-2cb2-3927-b99a-e1db627eb74a | 2.55386 | -60.55978 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 04fda825-1817-37e3-b485-4d96590f042b | 2.8769 | -60.59295 | 2026-02-21 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b5dd5df-38ad-3720-b040-94017d88c34a | 2.69156 | -60.21977 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6ed7b814-0d3e-36ba-9f27-6fbe962a132e | 2.68361 | -60.25747 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76bf97fa-f869-3c45-a1f3-2963007193be | -2.0376 | -47.13868 | 2026-02-21 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 785c7c51-6fae-3019-89e3-3dd80694f02c | 2.55162 | -60.7345 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ccefab35-3493-3673-b0cd-39cf323887a3 | 2.67948 | -60.41207 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 742a0c4e-dd9c-37e4-8cf7-e777c1b85977 | 0.06947 | -60.65442 | 2026-02-21 04:38:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6dc99fa3-b19e-36b5-ad37-b2329dbda41a | 2.55829 | -60.73413 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a291daa4-7189-376e-80d8-b93e5e1fd682 | 1.93613 | -60.36893 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9242b02b-e39a-31fc-8491-2729321cfc3c | 3.08437 | -60.09636 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa4eadc4-f17c-3149-9a08-61b7e3ae6ecd | 2.701 | -60.23661 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 71045bdc-a661-3833-8f0f-ac7ce05eceb3 | 2.56755 | -60.55804 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0903873-e6d4-3297-bf95-d94c85b4663d | 2.55852 | -60.73347 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dc2e8a2b-3d9a-3740-8651-06685c07f82b | 2.69007 | -60.23159 | 2026-02-21 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d81bbf00-efa0-313a-8716-a92d29ea434a | 2.68176 | -60.41155 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20541bea-b1fd-34c9-bd0d-0645ab089355 | 1.94188 | -60.36189 | 2026-02-21 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 22b21d87-3a41-34d6-8174-23379f1e55cc | 2.5617 | -60.7354 | 2026-02-21 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 1aaf69e3-1319-3c0e-a725-452a901a4aa9 | -6.61617 | -47.63564 | 2026-02-21 04:40:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30d1cd9d-d9e9-3e7a-a199-cce329613c49 | -5.66606 | -47.51598 | 2026-02-21 04:40:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae659285-a852-3df8-b920-8a86aef879ab | -2.99985 | -48.95077 | 2026-02-21 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 01d35114-237a-3e61-b465-2a8007c25de7 | -6.6156 | -47.63936 | 2026-02-21 04:40:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa2878d9-b328-3bf7-add6-38cbf18248c9 | -16.49615 | -39.86622 | 2026-02-21 04:42:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ba74cf77-5029-3b28-8cc2-a3a65086f7f6 | -16.4967 | -39.86044 | 2026-02-21 04:42:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b2ff29ba-c3ac-303f-b1a4-1bf820578655 | -15.17986 | -52.30365 | 2026-02-21 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f1a332f-e0e1-306c-b18c-caaed1e8b1b5 | -23.3918 | -51.72818 | 2026-02-21 04:44:00 | NOAA-21 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| d3e0ebfa-8b50-3f1b-a1d3-5191ccf70ed7 | -20.22821 | -50.65849 | 2026-02-21 04:44:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25fd2f97-0cdc-351e-a878-37c87f8fcdc0 | -18.97503 | -52.92582 | 2026-02-21 04:44:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a54cb30-2232-3d54-9e20-3085ec228e94 | -23.38783 | -51.73158 | 2026-02-21 04:44:00 | NOAA-21 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 9ae06ce9-78f4-32a6-9301-567048993117 | -19.71951 | -50.20956 | 2026-02-21 04:44:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| df85a2ab-12f8-3929-be72-0a8f0c624d86 | -19.49946 | -50.42159 | 2026-02-21 04:44:00 | NOAA-21 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5001d3f7-fc31-3c71-b3e6-5922d1871757 | -20.22765 | -50.66245 | 2026-02-21 04:44:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9079034e-3b66-3397-9433-b3e81c63ba40 | -20.96078 | -48.37934 | 2026-02-21 04:44:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 510488f4-41c1-3f9b-ba09-30d184ff3f93 | -31.04031 | -53.09003 | 2026-02-21 04:46:00 | NOAA-21 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| e0976011-3028-342d-bdfd-67f919683080 | 2.7088 | -60.2398 | 2026-02-21 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 02f1165d-e44c-3687-b649-f1d26281cff9 | 2.7088 | -60.2398 | 2026-02-21 05:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 661b55d6-0643-3c72-aaa4-b5c118d62a26 | 2.7088 | -60.2208 | 2026-02-21 05:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| ed00224e-e2fc-306f-bef0-a31896418def | 0.4569 | -60.39395 | 2026-02-21 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f7a17c6-0b01-326b-a3dc-917783e5ec16 | 0.44948 | -60.40364 | 2026-02-21 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df5f6ab2-1906-3e76-b222-1291d92b0376 | 3.07924 | -60.10941 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c0ecbca-c77b-337d-b4c0-d4fc91206425 | 4.26634 | -59.77797 | 2026-02-21 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5bd568e-178c-3612-8fa4-a8668b45b84d | 4.05899 | -61.09308 | 2026-02-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94fb55ab-663d-353c-bee1-d650dfe05af4 | 2.55673 | -60.73772 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 233276a0-2c9f-30c6-a25e-0d807b76e366 | 2.69373 | -60.22342 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c5686eb-9c51-3436-b0fd-aadd74792f97 | 2.70464 | -60.23516 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 571b9b45-1a94-3321-83f9-53d8e8e382b7 | 0.07095 | -60.65166 | 2026-02-21 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d4bb78b-a330-36b8-9323-5e5ad2da8d37 | 2.55797 | -60.56144 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20564ead-fb57-366e-bedd-6c12c3430f1a | 1.94122 | -60.37142 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0d13d983-28b9-390e-a442-aa1b57dc6bf0 | 2.55341 | -60.56212 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 337cb2f1-cad4-3920-8789-79b11a7b4c86 | 2.68994 | -60.22852 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89b820e3-dc88-3e74-800c-1e6b3a48d516 | 4.06771 | -61.11799 | 2026-02-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 691f496a-7da0-3030-943c-d1a61eff2fec | 4.16195 | -60.87205 | 2026-02-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b518d347-1a23-3d71-bf84-3d4459185689 | 4.03356 | -60.12015 | 2026-02-21 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9709c458-a520-345a-bc10-779baa31fe28 | 4.02803 | -60.1236 | 2026-02-21 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3b698f9-dbf3-3aea-bb20-4c3369120a43 | 2.65582 | -60.1226 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66b42ec2-e63e-3b1d-9a65-e7112fd1ba86 | 2.68615 | -60.23359 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 088c7dfa-f60f-3b69-85c7-abb2174ce953 | 2.89472 | -60.59217 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abfb456a-b955-30b5-923e-23ce77d1daac | 2.68065 | -60.41162 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89d93b21-1366-3a6b-9866-9782fcc8f43e | 0.67955 | -59.55999 | 2026-02-21 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e92a341-7735-3653-bdfb-4a4ed2813ee1 | 4.02906 | -60.12096 | 2026-02-21 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b8b0a3f-a7b3-3407-86b7-7815899e49a8 | 2.6944 | -60.22782 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17533843-9828-32bf-a85a-f5c009d86be9 | 2.88556 | -60.59363 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5524935-8bbc-3146-b42d-5b26ab7ffee9 | 2.68549 | -60.22922 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cff8799-283f-3fc3-b850-3975825b9d65 | 2.54957 | -60.56742 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3a6f1b8b-e767-349a-84e8-4910871ac4d0 | 4.27077 | -59.77728 | 2026-02-21 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2742778-abff-3d7f-a7d4-6089207a0b38 | 2.68499 | -60.25624 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36421197-54bd-3bae-8b6c-8a65e810e746 | 4.03251 | -60.12271 | 2026-02-21 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c52350e-a249-363c-876b-c73512b5c503 | 4.06533 | -61.11615 | 2026-02-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28f3d74e-69c2-3e17-a00d-6e4573cec52a | 2.68928 | -60.22413 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README5.md)
