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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3533dc33-3357-3605-9046-d1d65afd716c | -7.85668 | -54.89231 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1837f072-8643-32ab-b348-6cf28ce5a1d9 | -7.68236 | -54.83039 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 049951b8-490a-3cc7-87e8-74241d0eb30c | -7.55567 | -55.35883 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49c9c399-353c-31ed-8d8d-95b63116ca6a | -7.55492 | -55.36291 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0ba2892-cefb-3931-aa1d-7e5f1c99c835 | -7.17183 | -55.54855 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2723b4e6-616b-3518-84f8-6d252c9b7f7c | -7.16899 | -55.54628 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dfc2cd5-c436-30e9-99e0-716c899ef62a | -7.16817 | -55.55066 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b44e139a-f37a-33b2-bb7e-efd944719cc4 | -7.16588 | -55.54749 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f672108a-8f00-3527-b016-b0635955a169 | -6.88001 | -55.11711 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfa4a7b7-0c96-341a-8016-c408a0b2f184 | -6.87928 | -55.12119 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66c2e41b-5c48-3efd-8627-49850cb7b93c | -6.64841 | -54.94653 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3790c33-1cbd-33c5-b8d4-04088633f9d4 | -6.64272 | -54.94625 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84c57038-3c05-3b74-a8b7-717d129581d1 | -6.64188 | -54.94976 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfe58a5d-22f0-386e-8583-7abb392e082f | -6.63615 | -54.94953 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28f8078d-75dd-3129-9f9f-cd5991cd7718 | -6.6361 | -54.94879 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58ce629c-8381-3f93-b41a-2fda1deda88e | -8.91441 | -54.92921 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8fc1cb1-c60c-3f8b-8ac6-34e06ff1b920 | -8.9129 | -54.92741 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3469041-db6e-3416-9b65-572aa39836a8 | -8.52016 | -54.97561 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ccb0dbc-0fb8-3e53-bc21-8e5a48aa477a | -8.51949 | -54.97927 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16cde2a8-97c8-35e8-98d9-cdd7d82a3a52 | -8.49619 | -55.16937 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72194ffa-f02b-3a47-9311-69e417249179 | -8.49054 | -55.16818 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 849ec4b4-beb7-3b04-a67b-267caaf57564 | -8.48982 | -55.17206 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c75114ba-96ae-39e8-a02f-5dd70a3d8139 | -8.48558 | -55.16325 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d3d3772-fd36-3bf2-89b6-de810cb3ceb8 | -8.28965 | -55.38597 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ad513a3-36f6-3271-bdef-0d12a3e5e57d | -8.28951 | -55.38711 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ffe125e-e2e4-3f68-95e8-b839090cdc7a | -8.28888 | -55.39011 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa2e3156-2d0f-35cb-855f-d3cdb8ec505c | -8.28388 | -55.38491 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a0d73cf-aaad-319a-84df-c93913fcf5a4 | -8.28373 | -55.38602 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78b50468-5f31-3512-b44f-32159197a104 | -8.2831 | -55.38902 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12acf36b-2e5d-3960-ae17-e36dd9b4c64e | -8.28299 | -55.39014 | 2024-10-10 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d53aae7b-54a8-3225-93af-b0a62c3920a8 | -8.13865 | -55.17297 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62b692bd-f5e7-3e4a-9604-290a91c49e1d | -8.13792 | -55.1769 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4390fc0a-633d-3887-a8ff-64809862f118 | -8.1372 | -55.18081 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59fa68b0-5e66-3298-a9a5-5165b584c539 | -8.13222 | -55.1758 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed3e9d70-67c3-3131-8898-d916d65b21a6 | -9.96326 | -55.33567 | 2024-10-10 04:19:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8561c2be-2614-3560-ac4f-75017e603367 | -9.95837 | -55.33083 | 2024-10-10 04:19:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 035ce5ee-b63a-3474-b266-f63ee9be8b4d | -9.95766 | -55.33463 | 2024-10-10 04:19:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cb845ee-461b-3f4c-8848-001171f9bc0a | -9.95277 | -55.32984 | 2024-10-10 04:19:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d07a0e6b-33bc-34e6-8394-6d2117a9b75a | -10.48493 | -55.61705 | 2024-10-10 04:19:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f2ba37c-1d59-3511-ab78-ce2995ae0c2c | -10.48417 | -55.6209 | 2024-10-10 04:19:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf76a17f-cb0d-35e1-b5b9-ee634b850fa6 | -10.48272 | -55.61826 | 2024-10-10 04:19:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffec0c6c-caa9-3db1-a823-e36b9717e613 | -10.47929 | -55.61592 | 2024-10-10 04:19:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c107b458-c54a-381a-9133-27ad0576155a | -10.35977 | -55.86048 | 2024-10-10 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 0b39d1da-bb33-38d7-a0b0-aeec762ae703 | -10.35899 | -55.86452 | 2024-10-10 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1bc3c3c7-c31f-3d2f-a633-60ebd20beb78 | -10.3582 | -55.8686 | 2024-10-10 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| e0834729-6a10-3b50-9c12-b1f110aec2ac | -10.35403 | -55.85934 | 2024-10-10 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4f400de8-9d1c-32de-9db1-5bf3a71181a2 | -10.35338 | -55.86034 | 2024-10-10 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5c19dc01-27df-3fe4-a1c5-a9c9b13dc58d | -10.35325 | -55.86335 | 2024-10-10 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 668122b7-ce52-35d9-8575-9fda80a538a6 | -10.35262 | -55.86436 | 2024-10-10 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40345833-95f9-3682-b5e9-59efc4698eb4 | -10.35247 | -55.86739 | 2024-10-10 04:19:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e19f29bc-02a2-328a-ae8d-d1de80e4ca51 | -11.89406 | -56.20693 | 2024-10-10 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 373d4938-f668-3a6d-b2af-6fc2b4f13325 | -11.8939 | -56.20477 | 2024-10-10 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ae5e144-4564-31a6-a4e8-a9c2f17dbac0 | -11.89326 | -56.21094 | 2024-10-10 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10408cc1-dd0f-3deb-8fe7-aec6e9f34bd1 | -11.89313 | -56.20879 | 2024-10-10 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf71c1cb-af7b-3c4b-b333-ac20e945bc99 | -11.89246 | -56.21494 | 2024-10-10 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7622cf14-2761-3359-8d50-3e78d4e426c9 | -11.89236 | -56.2128 | 2024-10-10 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 693889ca-2d69-318b-8e60-8ede74d56996 | -11.89159 | -56.2168 | 2024-10-10 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26984d8b-5ed4-3456-b591-d756364facba | -6.4761 | -56.02186 | 2024-10-10 04:19:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55bd76a2-1131-31cd-83d1-fdd3d6647230 | -6.47141 | -56.02121 | 2024-10-10 04:19:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc10efd0-bf7b-3973-8d50-377c74ce3706 | -6.47059 | -56.02584 | 2024-10-10 04:19:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3711db7-2006-3f21-a7e3-4ffe834d886e | -6.46913 | -56.02494 | 2024-10-10 04:19:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07810cca-28f7-3b95-996b-381b891e7b53 | -5.20002 | -56.02917 | 2024-10-10 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c194047-7a3b-3eba-a4dd-71b3f66e08a0 | -5.19909 | -56.03435 | 2024-10-10 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aecdc3b4-8a29-3df2-8fd7-95e7032fcd05 | -5.12844 | -56.01395 | 2024-10-10 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 901bb4aa-8099-356e-8012-f03b244e04da | -5.12313 | -56.00711 | 2024-10-10 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc19a1c4-1725-39ce-ac24-3d1bec1c4d48 | -9.27683 | -57.21711 | 2024-10-10 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aa01468-f80f-3da5-9377-fdd877e8d000 | -9.27587 | -57.22209 | 2024-10-10 04:19:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cac3ca7b-2503-3538-afb7-fde6b99be98e | -9.94858 | -58.11827 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4999ca4f-3bd0-3301-9d2c-5615f25895bb | -9.94741 | -58.12413 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 338c6b45-d14d-3b17-8338-74a46af0c4dd | -9.92092 | -57.48112 | 2024-10-10 04:19:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d774c35-9c35-3d41-b3bc-78654abacb33 | -9.92009 | -57.48329 | 2024-10-10 04:19:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e897b28-76d6-3dec-b50b-f18fd5386cb3 | -9.91645 | -58.12287 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6867140d-9698-371d-aa9b-d18cb1547ed7 | -9.91532 | -58.12869 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64e417b6-33e4-390a-ac47-d4e78d09d736 | -9.91471 | -57.47677 | 2024-10-10 04:19:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7324058f-02d6-3e77-bfce-73ff1d776276 | -9.91454 | -57.47982 | 2024-10-10 04:19:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 214b8aad-7d3d-375e-9e63-3fbd2174c569 | -9.91423 | -58.11765 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2dacb4d0-b505-3091-a662-5b86ed914ec6 | -9.9137 | -57.48202 | 2024-10-10 04:19:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bb2f09d-bc0e-3693-b0df-a718abc1ba1a | -9.91306 | -58.12347 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4484ba0-32da-39e6-a898-a54541017b55 | -9.91189 | -58.12928 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f876dcf-1c19-39c0-8437-7e735f4300a7 | -9.90982 | -58.12149 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d1a86e8-194c-39fc-852c-3e32f1e5e834 | -9.90869 | -58.12729 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f397d24-2dc7-3b6e-9a9c-2e0f7a2e5e87 | -9.90646 | -58.12199 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 031810ad-df55-3a90-aade-c6a5a317fc82 | -9.90529 | -58.12777 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75aebd4d-bf6e-3607-8833-2079e81bd5b2 | -9.90323 | -58.11995 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d414930d-002d-3113-82d1-524abd203d7e | -9.9021 | -58.12574 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4670464a-831e-3027-a9e7-3b88c142b5b0 | -9.89987 | -58.12047 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b094e650-9fea-3238-b8a9-abbc7409e71c | -9.8987 | -58.12624 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de84d634-bb00-3742-bec0-b81eec4e7518 | -9.8955 | -58.12419 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a19dd85-2c42-3dce-a63b-51a3ff811d4e | -9.89436 | -58.13007 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5cef4df8-0add-3dcb-b5a4-e704d95a1307 | -9.89209 | -58.12479 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e7462e3-d626-3c10-8637-0bf5e92a453b | -9.89089 | -58.1307 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef0c85eb-bee9-3ec2-844b-bb50e19c89b7 | -9.82228 | -57.74544 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af4863b2-846b-3354-817f-bdc8c4b1109e | -9.73255 | -57.86462 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6a9ff1d-9878-3b22-8926-2562de080266 | -9.72597 | -57.86345 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16deef33-978c-3b2d-af3e-e714c92daf25 | -10.33639 | -57.50831 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2134266-958c-3e11-b140-4e1bd1bec2ae | -10.33213 | -57.50248 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 197ef36a-b759-3e31-8f72-1ebaa40376fe | -10.33107 | -57.50771 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5a466e2-9c00-34b5-800d-a9195789c971 | -10.33103 | -57.50193 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 231168bc-d8fd-342a-a278-184276a3368c | -10.33001 | -57.50719 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 081b9b37-0846-30ee-8501-fbe473ddcc12 | -10.28492 | -57.70422 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README83.md)
