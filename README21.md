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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 515c11a5-d52a-37c8-9a3d-400e1c0aba55 | -4.5961 | -42.95 | 2026-09-18 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2c10a658-7023-37d8-80da-d375fa4238e9 | -10.6536 | -50.4778 | 2026-09-18 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 1a9bee48-4508-310e-b24c-ea34987420d0 | -2.6125 | -54.7577 | 2026-09-18 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 399773c2-4d2e-3a4b-98d6-e551c93118d4 | -9.7177 | -54.8162 | 2026-09-18 02:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 6b841f9c-fd1b-340f-aeea-3ee29ed12a20 | -19.2015 | -48.7675 | 2026-09-18 02:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 0d2194d1-46fb-38ce-b214-79d84d0ba061 | -11.2787 | -43.3643 | 2026-09-18 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 6bc42c11-1103-39c4-b86d-dc6b6a7f0587 | -3.3823 | -50.4486 | 2026-09-18 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2cfb1989-c4f0-343b-805b-1d880980528f | -4.5776 | -42.9277 | 2026-09-18 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a21dd76a-d457-334b-acb2-91f1ae95ecf7 | -19.1812 | -48.7717 | 2026-09-18 02:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 273.4 |
| bbcc47be-ce82-3434-beeb-7611ee9d1da6 | -9.7179 | -54.796 | 2026-09-18 02:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 00e2c980-bacb-3092-9a04-1e47ba7d5e59 | -19.2009 | -48.7904 | 2026-09-18 02:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 88.2 |
| bbe5fbbc-bf62-3fa7-a303-832f9b57ad56 | -4.5961 | -42.95 | 2026-09-18 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| c72d4500-a2fc-37d3-a74e-7b8b28c623d7 | -7.0086 | -43.6264 | 2026-09-18 02:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ddce1c89-0247-3930-878e-b23a0ce8566f | -13.2451 | -42.3133 | 2026-09-18 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 7c508398-6a63-33b0-9abb-e59a4ba95e1a | -2.8101 | -50.4658 | 2026-09-18 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 600a978b-ce22-31c1-81d0-2e960488826a | -2.8285 | -50.4653 | 2026-09-18 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 8b096ea7-2ab4-3901-b003-7e47268cadb3 | -2.8284 | -50.4863 | 2026-09-18 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 1c8f184b-0773-32b2-a585-1001275f5735 | -4.5587 | -42.9523 | 2026-09-18 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 06ebff17-a4c3-3abb-9bc5-e0f44bb35cf2 | -8.9108 | -62.391 | 2026-09-18 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 964fd413-9d8a-379e-a1d6-3d22f4f10c63 | -19.1806 | -48.7946 | 2026-09-18 02:30:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 20a55489-9124-312a-a1f6-4b3f1d673cc2 | -3.028 | -51.376 | 2026-09-18 02:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 764a02c5-d27b-3509-9eec-b323205c3ebb | -4.596 | -42.9734 | 2026-09-18 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 491f2155-4886-3ec0-9d12-4941b74856c7 | -4.5774 | -42.9512 | 2026-09-18 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 293.7 |
| 32781d1d-a0e6-374a-9f60-5f32812ff8d8 | -3.3638 | -50.4492 | 2026-09-18 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 0f1b9f79-cb9a-3672-94a7-64e90f930334 | -5.7569 | -45.084 | 2026-09-18 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 2120e66d-f252-3860-9bee-65b6315d956d | -13.2257 | -42.317 | 2026-09-18 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 84317713-8707-37a7-a2ce-ae50c6658659 | -8.8922 | -62.4107 | 2026-09-18 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 21addd86-cbf2-3826-a2f3-ba4d490cd292 | -3.0465 | -51.3755 | 2026-09-18 02:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d25d8b9d-bfa2-3c5f-a319-32b6b4e34549 | -13.2252 | -42.3414 | 2026-09-18 02:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 89.1 |
| ee6bca3a-4cf9-3d13-ac91-1e847c1e0c9c | -8.9107 | -62.41 | 2026-09-18 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9a42c5d2-722a-3295-99b3-59e0f6294081 | -5.7567 | -45.1067 | 2026-09-18 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 99e5be91-1429-3144-a179-5e69185a45e4 | -9.699 | -54.8176 | 2026-09-18 02:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7bd2e9c8-df27-3c2d-86b4-909577a58df8 | -7.0084 | -43.6497 | 2026-09-18 02:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6d2e8672-44bf-34a1-9302-9697495ce39b | -4.5772 | -42.9746 | 2026-09-18 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f32e9578-5c2a-321e-8c58-9a80835b6b15 | -19.1806 | -48.7946 | 2026-09-18 02:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 705994d9-64a2-3e26-b36d-743d232300bd | -5.7569 | -45.084 | 2026-09-18 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 273864f5-79bd-38a8-8fe7-a25998537b47 | -13.2252 | -42.3414 | 2026-09-18 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 97.2 |
| c152997a-c9f4-3bf5-aa14-6397f40ab2e8 | -19.2015 | -48.7675 | 2026-09-18 02:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 0233e000-7073-3b06-96d2-71610bb13ce0 | -4.596 | -42.9734 | 2026-09-18 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c3b19764-2351-3fa3-8dfe-46a02f8da269 | -3.028 | -51.376 | 2026-09-18 02:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| e8d60ed5-5d27-34d0-9973-cafb3a9ef4ca | -7.0084 | -43.6497 | 2026-09-18 02:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 12fa584d-6e28-3a1a-8e7d-bf952046c488 | -9.7177 | -54.8162 | 2026-09-18 02:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 26ad9a5f-c10d-3a05-aa35-9ca335e6347f | -13.2257 | -42.317 | 2026-09-18 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 128.4 |
| 6397b023-f4d2-3a7e-b26c-61660ff97376 | -4.5961 | -42.95 | 2026-09-18 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 6396559d-38ea-340a-8aa1-8715d20dfd4f | -19.1812 | -48.7717 | 2026-09-18 02:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 219.8 |
| baab9f04-fb34-33e5-9789-d354c8e22658 | -11.2787 | -43.3643 | 2026-09-18 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 9b75c9bf-d6eb-3c13-a897-a8d644e1b38b | -4.5587 | -42.9523 | 2026-09-18 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| a8e788f2-46c0-3294-9cc2-32bc575915af | -3.3638 | -50.4492 | 2026-09-18 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b08a17a0-b358-35d0-91db-2346a425649e | -13.2446 | -42.3377 | 2026-09-18 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 2f534ddc-59e4-3301-b699-9a8c8d43c5eb | -4.5774 | -42.9512 | 2026-09-18 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 363.6 |
| d0f07a46-229c-3363-987a-c4ece2ee6853 | -7.0086 | -43.6264 | 2026-09-18 02:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 1c02869c-da1e-3fe5-a77c-69ec5b045ad2 | -9.7179 | -54.796 | 2026-09-18 02:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 462e2cf1-7f4b-3354-a298-fa43b1b7cd4d | -4.5772 | -42.9746 | 2026-09-18 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b995ee02-85a4-3196-819b-471deef699e6 | -3.3823 | -50.4486 | 2026-09-18 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ebaab188-5af6-350a-bf3f-556fb2cf9d57 | -5.7567 | -45.1067 | 2026-09-18 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 127b26bd-06f7-34e5-9887-25d5cba626cf | -2.6125 | -54.7577 | 2026-09-18 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7d38108b-790f-37b3-b0bf-f8905e9c8390 | -13.2451 | -42.3133 | 2026-09-18 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 91.0 |
| d4343741-96cb-3d06-9c9b-488f67b831ff | -9.699 | -54.8176 | 2026-09-18 02:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e4037339-5c78-3bae-b336-e090beb5db8a | -19.2009 | -48.7904 | 2026-09-18 02:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 653b5ac4-2e42-3577-8a2e-2c2cb31e24b9 | -3.0465 | -51.3755 | 2026-09-18 02:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3c3b1df0-f83c-33ca-9038-bb375f47f35f | -12.3782 | -50.7111 | 2026-09-18 02:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f9c3b50f-722c-36ab-af62-3774f0396b4c | -2.6125 | -54.7577 | 2026-09-18 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| e1879073-487a-36dd-83be-35e1a2a72c16 | -5.7567 | -45.1067 | 2026-09-18 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 343d1920-e61b-3833-90e2-69fe4424dc7f | -11.6798 | -54.446 | 2026-09-18 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| d67e5298-e88e-37fc-bfdf-310de1a90839 | -13.2451 | -42.3133 | 2026-09-18 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 90b7b886-db06-3877-b131-e3a23b79c787 | -3.0465 | -51.3755 | 2026-09-18 02:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 3e38afa9-6255-3467-beef-999843a136d5 | -18.4467 | -49.304 | 2026-09-18 02:50:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a0568192-b4b0-374c-89db-5408ea55e955 | -4.5587 | -42.9523 | 2026-09-18 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| b2da2b07-3afa-330e-b6c5-0478f2f7c345 | -2.8285 | -50.4653 | 2026-09-18 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 560ee0a0-36db-36af-9561-9b0254f3e5c6 | -7.0086 | -43.6264 | 2026-09-18 02:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b6351fb1-47a5-3539-9c35-d3bae81dcb88 | -4.5776 | -42.9277 | 2026-09-18 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 3eaad3ef-1ae5-302c-b7ef-fed5b48653fe | -5.7431 | -57.5814 | 2026-09-18 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f200d281-9d89-3dbd-a483-35c5240f3680 | -19.2015 | -48.7675 | 2026-09-18 02:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 157.7 |
| e8c3939a-f462-3935-b0ba-430ae751a8a2 | -3.3638 | -50.4492 | 2026-09-18 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| aa6de3ae-6096-3929-b9c6-d2e299ba2029 | -13.2252 | -42.3414 | 2026-09-18 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 140.9 |
| d10fe1c7-26a7-3451-b038-1a503097e7f1 | -11.2783 | -43.388 | 2026-09-18 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7c44a430-439c-3401-9c85-68360241fae6 | -4.5961 | -42.95 | 2026-09-18 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 9e17a74b-f762-3a5f-a040-6687a2f7d592 | -5.7569 | -45.084 | 2026-09-18 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7873ea42-d371-3872-b49e-6f67dfb80d65 | -2.8101 | -50.4658 | 2026-09-18 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 831e5f65-79ca-3508-85cc-e8d0780531fe | -9.7179 | -54.796 | 2026-09-18 02:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 47051de8-72fd-3300-9186-57dcddb275b9 | -19.1812 | -48.7717 | 2026-09-18 02:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 194.5 |
| b4ea9b02-921d-3fbe-b237-67583aa2190c | -13.2446 | -42.3377 | 2026-09-18 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 6f197254-55ef-34c3-85db-979b5920a11b | -18.4667 | -49.3001 | 2026-09-18 02:50:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| be5b62b3-589f-38ff-a51d-5f48fef8f7ef | -19.1806 | -48.7946 | 2026-09-18 02:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 1cb6503a-0bd7-3543-a910-e72ce3127d3c | -4.5774 | -42.9512 | 2026-09-18 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 277.5 |
| b80a07e6-9f26-3d66-b11e-65b4e302c6a9 | -9.699 | -54.8176 | 2026-09-18 02:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 43b44677-5160-3577-8fe7-f69abd2156e5 | -4.5772 | -42.9746 | 2026-09-18 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 929ee6a3-3826-3358-9459-43330c19061a | -11.2787 | -43.3643 | 2026-09-18 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 6a49a25e-0340-37ec-9979-a28ad5f58ab9 | -9.7177 | -54.8162 | 2026-09-18 02:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| c6022952-c50d-386c-a751-5d0faf59004c | -3.3823 | -50.4486 | 2026-09-18 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c1a3b606-7759-31c2-9ce8-e035e4ce7e0b | -13.2257 | -42.317 | 2026-09-18 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 139.8 |
| 0327f051-453c-3ef3-9d68-05a0bf719bdb | -2.8284 | -50.4863 | 2026-09-18 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 70128937-2259-373c-a743-e9f595575490 | -19.2009 | -48.7904 | 2026-09-18 02:50:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 138.6 |
| af7b53df-a6a0-3eb3-92ce-e5acc834a73b | -6.3656 | -58.2966 | 2026-09-18 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| df80fd99-c318-3a98-aea0-5bbb7ce4d96d | -2.8284 | -50.4863 | 2026-09-18 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d587228e-7b7c-3ac8-b661-4a21a64daef0 | -19.2009 | -48.7904 | 2026-09-18 03:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 103.6 |
| adc11a5c-2b37-3230-a439-bc919207a7ec | -19.2015 | -48.7675 | 2026-09-18 03:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 3aaa8e4c-f7df-39bd-aecf-5f2e0383ca9a | -13.2451 | -42.3133 | 2026-09-18 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 143.4 |
| c4d5ceb5-e5c8-3d93-b395-0b917688c7f1 | -4.5774 | -42.9512 | 2026-09-18 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 206.0 |
| c09203fe-997e-3f19-8d0b-a074a6b87785 | -11.2787 | -43.3643 | 2026-09-18 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |


[Clique aqui para ver as próximas entradas](README22.md)
