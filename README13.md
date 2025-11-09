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
| 5ea07238-1881-3852-91b7-7fb767daa388 | -3.35253 | -50.21304 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4b0fbdb-c254-32ab-928e-7278e6272219 | -2.43909 | -49.22395 | 2025-11-09 04:16:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 054ea6a4-656b-3447-a426-34ed77abf08b | -5.09583 | -37.78592 | 2025-11-09 04:16:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5e5672b8-b392-3901-a2e6-dfb6197ab0c0 | -4.13352 | -49.25755 | 2025-11-09 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a75b8a3-bd2d-3bf5-9d6d-a19af1a3572a | -3.86515 | -49.37773 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80986236-0f78-3a52-8313-3276e820f30b | -3.4522 | -45.6517 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8caaef57-784f-34c9-aa85-2c231e72085e | -4.46195 | -44.64447 | 2025-11-09 04:16:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| dd579dd1-16ea-3521-a844-0c68cec44e9f | -3.14006 | -50.16817 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da152647-5d21-3edf-98a4-a5b2190da331 | -3.76792 | -40.51318 | 2025-11-09 04:16:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b775172e-b65f-32b3-8dbd-7a70ad2c2042 | -5.635 | -43.25811 | 2025-11-09 04:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ef8636d-4f52-3b6c-978e-503ade4e1526 | -3.86436 | -49.38241 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 831718c9-44ff-3e9f-a132-23df71614852 | -4.39332 | -45.97148 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e445af11-e945-388a-a361-4289c1d11bc2 | -3.0988 | -49.67992 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df7c920e-19d4-3dc5-9f31-d844fb49d708 | -3.76851 | -40.50945 | 2025-11-09 04:16:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 29b39b39-fd52-30fe-801f-dc463b59bbf6 | -3.56221 | -51.12304 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a930594-5d39-3cb1-9f5d-894b4c6bbd9c | -4.32887 | -45.69693 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3891993-c476-3ccc-8dde-f771dd5382ac | -5.28315 | -44.94851 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f1625193-41cc-364f-a24d-7b074ca08a1b | -3.55813 | -45.01364 | 2025-11-09 04:16:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70c79193-403d-36d5-b21e-bfb197e4621c | -2.61201 | -49.22303 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 09c2c739-9224-3f0d-a40f-0967ae01cebb | -4.01825 | -44.77637 | 2025-11-09 04:16:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3904000d-c815-33c7-b8b4-d57f5ecd76dd | -3.32156 | -50.30867 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19522030-57e5-3ee6-8351-06f79e906463 | -3.7701 | -40.51272 | 2025-11-09 04:16:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0a664cae-0210-35f5-bdbe-e6a566d179c0 | -2.99219 | -40.38169 | 2025-11-09 04:16:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9817170f-4b8d-3149-a94d-b329c0078958 | -2.26102 | -47.87336 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad41d778-4df8-3695-a4bd-0749658876bf | -4.37933 | -45.49622 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2d54bd5-66f7-3b9b-9449-94ce0a87f1eb | -4.39234 | -45.95426 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c075913-3610-31dd-b6a5-6c08a7f1e9b4 | -2.10427 | -47.64342 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a391ef9a-03c5-36bb-840a-94dc406923b4 | -5.49349 | -45.85971 | 2025-11-09 04:16:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb7617e6-419e-3408-9c6e-e62bdc067ff3 | -3.62759 | -43.15427 | 2025-11-09 04:16:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ed3fb851-3b99-32c7-b5e8-eac0004bfbd8 | -4.68571 | -45.84664 | 2025-11-09 04:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 793a3f72-cfbd-32c4-95c9-78e4e2f7657f | -3.49055 | -46.11093 | 2025-11-09 04:16:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63567ece-1c65-34eb-87bf-ff7377b22da7 | -3.33016 | -49.127 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d68dc3b-ba81-3648-91a9-ae3e4ddc0200 | -2.98628 | -48.7042 | 2025-11-09 04:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ba6df2c-552d-3bb8-a9cf-b2958440e7f2 | -4.32527 | -45.69635 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2f43574-4c17-3959-bd17-84917b8f0dd3 | -3.44924 | -45.64693 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4aa62d1a-8d1f-39fd-b891-7bedfece7b99 | -4.33282 | -39.36432 | 2025-11-09 04:16:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9759f572-276c-32b7-8669-5a7c1ad80832 | -5.08415 | -45.31015 | 2025-11-09 04:16:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f3cf3c0-67bd-3fa6-b752-da40ce266162 | -4.14198 | -47.65972 | 2025-11-09 04:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99c89e04-be42-3056-b371-1ab489002df1 | -4.18506 | -45.73502 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9565734-a87f-3666-b050-e0eaa090feef | -3.14907 | -50.60759 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bbf216f-c64f-32a1-9b50-38511e6fcaac | -3.40404 | -50.46072 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 26583629-8987-3b99-8be7-f1efcbe07a64 | -4.80956 | -38.69636 | 2025-11-09 04:16:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 806c13ac-3cc5-36a1-8fee-0911c70e7d96 | -4.40425 | -45.9734 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1045aafb-41e5-3c46-ab4d-25517dce3df3 | -4.83444 | -45.44513 | 2025-11-09 04:16:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba9aeb9a-0d01-398c-ad8c-8dccd28d4a53 | -3.65158 | -50.26717 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2199c49f-34c4-3bc9-8e85-2e2b1f407d16 | -4.04894 | -46.09281 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa8165e-d7ff-3fd9-9a3b-2e3cf008befa | -5.28599 | -44.95287 | 2025-11-09 04:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6ca3d83-3a04-3906-9a1c-e883dcb4c30f | -2.97604 | -48.71132 | 2025-11-09 04:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e44c3da4-926c-3d5e-9b5f-02fc363a59ad | -6.76777 | -35.43031 | 2025-11-09 04:16:00 | NPP-375D | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8194516b-afe4-3303-b46b-bf1786f3d827 | -3.34839 | -53.22494 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da44915e-530c-32df-b1c6-d79ca3d1da94 | -4.01192 | -48.04413 | 2025-11-09 04:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75a4fe87-660f-3760-9584-0873c8422235 | -4.89126 | -48.59995 | 2025-11-09 04:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5d718bf-f355-38e0-b5a1-84f280c018a4 | -2.2604 | -47.87727 | 2025-11-09 04:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f2a45c2-d3cb-3d1a-8c85-17718422d43b | -3.03588 | -50.27324 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e557ba6-04e3-324b-afbe-634a524fa1c8 | -3.41483 | -50.27523 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efc5cc03-55c3-36a2-b801-16f4a6aca553 | -4.6806 | -45.69081 | 2025-11-09 04:16:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80863471-2071-3b46-8369-19047dff16c9 | -3.31838 | -50.10209 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cc94f815-0695-3d86-b9ae-f921873fb204 | -5.09988 | -37.78653 | 2025-11-09 04:16:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 0eb03857-a77e-3110-ad26-7e0edb33f05b | -3.64745 | -49.87877 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33215557-ec0a-37bd-be74-8319160a7eef | -5.30857 | -44.20438 | 2025-11-09 04:16:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beaad0ff-87e7-36e1-a3a3-99e6f491c7ef | -4.52361 | -48.8362 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bd0734a-08ed-3fbc-bf9e-1886b6844a6f | -3.35434 | -53.22605 | 2025-11-09 04:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c503fcd-d449-3a46-9b2a-5ddd51c90f21 | -3.09318 | -50.329 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6cdd955-4f5f-3b86-9f93-42e90e80d466 | -4.40279 | -49.66768 | 2025-11-09 04:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ec3203a-9fbf-3982-8716-c19ed8f522eb | -3.32564 | -49.12619 | 2025-11-09 04:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32992924-cfdf-34b3-82fb-d3b6bc133653 | -3.61954 | -49.27715 | 2025-11-09 04:16:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee8c8972-87de-38bf-85da-298829042f8f | -3.65697 | -50.23493 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbc47c88-e305-374a-874d-5bd2cfcc069a | -3.31512 | -50.1078 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a45533fa-a628-35ab-8e19-2771b910476d | -3.58383 | -41.65716 | 2025-11-09 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4221082e-c8f8-3ed9-8934-dad2cb53d526 | -5.12908 | -42.88029 | 2025-11-09 04:16:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ae2305a-e747-3f25-bd16-6981ced35907 | -4.63679 | -46.40174 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4968a21-3ed1-3f68-93c4-914043216704 | -3.30407 | -50.15989 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a22c5e5-b3e6-3887-8a83-e2752e7ab4fc | -4.58922 | -49.39062 | 2025-11-09 04:16:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef572e5e-90d5-3cff-b084-404ed2040e80 | -3.68906 | -51.38919 | 2025-11-09 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45bebd94-25e1-3e04-8efc-a1d6e04f5642 | -3.1044 | -50.20128 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 025e52de-c3fe-3e95-8c4d-7ae18e8c244e | -3.35662 | -51.28802 | 2025-11-09 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d3520bf-fc54-3cd1-89ae-f447405c77b7 | -3.92006 | -51.01025 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddb628f2-b51f-3446-b01a-6cc427e33227 | -4.27325 | -48.34132 | 2025-11-09 04:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 453d34b6-cb25-3916-ac85-8ad441d88b1b | -3.14488 | -50.29218 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ff5790-6c2d-36fa-b89a-195c420a90ca | -4.3764 | -45.49165 | 2025-11-09 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 551098ba-59a5-3fe7-b695-f69656d75c41 | -3.48683 | -46.11033 | 2025-11-09 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b196c8c8-19c2-3d5b-ad32-8192ea30a3a1 | -3.29309 | -50.1969 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46d6e6fd-72ab-3d98-ad68-70eece4ae7cd | -3.40687 | -50.26273 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f098c5f-faad-37ed-9d09-00f355cf6ce0 | -4.39698 | -45.97202 | 2025-11-09 04:16:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36e717c9-4596-3c9b-9c36-d624da47c7a6 | -4.67953 | -46.40678 | 2025-11-09 04:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e7b780a-04b4-3ba8-b7bb-8f88f15dd0c1 | -3.7542 | -52.1057 | 2025-11-09 04:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65e45129-848b-3a12-94fc-8d55dcca3e81 | -3.283 | -49.77738 | 2025-11-09 04:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a506e81-33c9-37cc-aae7-184d00a5e698 | -4.80267 | -45.39637 | 2025-11-09 04:16:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e905c921-7fa5-3df6-b03f-5fb8312141b3 | -5.49478 | -39.0779 | 2025-11-09 04:16:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce352d3f-9c9b-3758-9191-f3f136a7f268 | -3.62815 | -43.15079 | 2025-11-09 04:16:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0fcb6662-adf2-3974-94df-949424bd176d | -5.20474 | -44.414 | 2025-11-09 04:16:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7818a65-914f-3fd1-88cb-3c141cc7e552 | -4.90619 | -44.64126 | 2025-11-09 04:16:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e36590-d439-3b70-b850-29c87f821510 | -5.60925 | -41.07915 | 2025-11-09 04:16:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 249b79c5-24b0-3cd0-9dac-5471e0c250a7 | -5.35874 | -44.86792 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ebbbdb5-84d2-31cb-becf-7dc5fdda4e9c | -3.14265 | -50.27491 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 10f102b3-8b4e-3d2e-a2ec-b771ead8549c | -5.37063 | -44.62305 | 2025-11-09 04:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 504d4273-bd19-3f6a-b950-f2bea818758c | -3.09997 | -50.3187 | 2025-11-09 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d685648e-cdc4-3c3e-9bd6-6f376cc6394d | -4.5825 | -45.62616 | 2025-11-09 04:16:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e1c7716-9d94-3f9b-98d6-c65f887f6a96 | -4.40011 | -45.16213 | 2025-11-09 04:16:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 284a4020-ecda-3d40-84f9-20063b20ee23 | -3.5612 | -51.12458 | 2025-11-09 04:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
