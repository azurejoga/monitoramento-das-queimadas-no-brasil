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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b864d87e-7b73-3c5c-aaab-27baf7a5fd4a | -6.67873 | -58.76823 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b274b054-3442-3ab8-87c3-131a33b89b38 | -8.50762 | -54.65722 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 24a52edf-3248-31d5-a3da-deb40f5d44ec | -8.4349 | -54.6911 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6de8a0f-ce3f-399a-b39a-99060ce7df6c | -10.64961 | -50.39394 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3091b41e-5347-39ae-9da4-25bc5bdaaff0 | -10.91343 | -45.3471 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5496000-d1d9-33eb-b6f4-e7c4922cbf66 | -13.41382 | -43.87642 | 2026-09-04 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85fd952e-eede-38ce-a5b0-d2ca88ff41e6 | -10.00099 | -50.2845 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8014a196-ecda-3098-b0a7-511b47b8288f | -6.67211 | -59.94545 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9bfe192-bf3f-31dc-b1fb-3b4e34f6c01e | -8.43341 | -54.69949 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90435cd2-4b5e-3f82-af9e-64dd1d9394c6 | -8.48819 | -54.64116 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fa87226-46f3-35ea-85a5-b3a6e63cd62d | -7.55083 | -61.35225 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 52e0628c-890c-3866-940a-957caeafe922 | -8.50043 | -54.64741 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f6eeff34-b9b6-3663-9046-91ed6accf246 | -13.09832 | -44.49662 | 2026-09-04 04:40:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fae238c-369a-324c-a54e-e883f40f03b6 | -8.4319 | -54.70078 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 376fcc1b-e199-38b0-8d88-d534d03df444 | -7.61334 | -57.61684 | 2026-09-04 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c3d24b0-6183-3b5e-bf53-c9a8e7918680 | -7.5502 | -61.34368 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 78eab114-024b-36e4-bfa9-80d8e65a3d5c | -10.65298 | -50.3945 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c362b54-1a89-32c9-be2a-1b102d649f63 | -10.44802 | -61.20782 | 2026-09-04 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 621f10bf-1de6-343c-a504-12d8c2dd5b1b | -7.55199 | -61.34623 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9bd855ae-9fc4-3ef1-b5c0-bf40b6689d09 | -7.54908 | -61.3497 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 63c025ca-83e0-3e49-a67d-0787154b149d | -8.43474 | -54.68409 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b01f41f5-dbbf-3f35-9c0f-c67fa3a75f66 | -7.55315 | -61.34024 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7f63f224-a9a0-3523-9db6-c85ce2320733 | -6.59619 | -59.1211 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b71cddd-c990-3777-be62-9cbc1e5c386e | -12.95271 | -49.13754 | 2026-09-04 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 299cc7c1-62f1-30c4-8f15-b3a08bbd3b59 | -8.43333 | -54.6924 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3513b80d-e145-3d04-b321-5e29fb2b9eeb | -10.57531 | -50.03123 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9c5d6a51-44d9-3b83-8923-03ad63b5610d | -7.0909 | -56.51918 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f36428-f076-3abe-beb9-e2dfadaab819 | -10.62193 | -50.41542 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 203dffad-1274-32b2-a9b4-1654e7158e9b | -6.37209 | -58.28766 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4631e168-e152-395e-a080-6c7094e5b740 | -6.67801 | -59.98422 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 28392b98-2a7e-3867-aece-c02190fea443 | -6.67705 | -59.98943 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2cc7cbdc-7250-3e64-b3af-9440631e284e | -8.43262 | -54.69659 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88ea1e93-ab96-3db8-bade-be0bd32b5e78 | -7.55869 | -61.34776 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c60eb78c-7497-3b8b-a480-7319147a1632 | -8.4997 | -54.65158 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cffdead5-e862-324d-8927-8a1c776e9bd9 | -6.37037 | -58.28739 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c3ee75f-73bd-3510-bd7e-d51d02b6a3e5 | -6.67741 | -59.95205 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 941820bb-5ffb-32d1-9c6c-3eb17f9dfa01 | -10.86808 | -45.33269 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d901c87-7c27-34f1-b5b2-d8ea75256ba0 | -6.68025 | -59.93658 | 2026-09-04 04:40:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebab1111-9f65-39d2-84f9-4f89e53c87c5 | -8.42469 | -54.71701 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7f20966-44d7-32fb-9c63-441bc8151de3 | -6.67517 | -58.75457 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23eeaa88-43cc-35f7-a1ed-f0b5f2f0943e | -10.90781 | -45.35987 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84d6f2bb-e0e1-3d4b-b048-d0b329d58388 | -9.57672 | -40.35031 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 112f5a8c-d189-3e57-aac1-241f1d6814bb | -10.50074 | -51.32855 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a98df49-5a11-3e2f-a992-b240dc7f511c | -8.49828 | -54.65981 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1f342b10-9b51-31f6-b2a4-8bb39a910f11 | -6.59699 | -59.11671 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e066f7dd-10a5-355e-9f88-af23d4ccf2e4 | -6.67554 | -59.96218 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f76c0ef7-d720-34fa-b432-563deeed4b20 | -13.37656 | -51.33719 | 2026-09-04 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42660a37-5236-3664-9582-1a495f8892d4 | -10.57865 | -50.03178 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c5b68b1-9d83-35a4-8357-be13982a7c42 | -6.37606 | -58.28848 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ce4e776-c1ce-3645-8837-f515818cadff | -8.43416 | -54.69529 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43a3dabe-ddb1-3765-acdf-ca8dafaf5c3a | -7.55753 | -61.35377 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ca520bd1-c60e-39ae-9099-57fd15407139 | -10.39038 | -49.95685 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00ce777b-2071-3316-8da3-d1f5fba2adf2 | -10.9088 | -49.60587 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 026e7d4e-3b23-3f9d-b352-d71b35b85829 | -7.55986 | -61.34167 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 384b5f22-0ece-3212-88d0-c76b315c530c | -6.77698 | -58.95457 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c4f5521-737f-3c98-88f0-11b654958967 | -6.68713 | -59.97002 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| abf89c9b-3e94-3e4d-8d66-e63d16f5b6ab | -6.67117 | -59.9506 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 537703da-496c-3f92-a4d7-5c71d5a56a6a | -9.2018 | -43.23375 | 2026-09-04 04:40:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ac760ab-8606-3468-8e62-71a1041cf6e7 | -13.41329 | -43.8804 | 2026-09-04 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4a79081-3ba4-36ef-82cc-020488143c67 | -8.49899 | -54.65571 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d39db587-8b3e-3914-bd91-8a08ce371dee | -10.4966 | -51.33204 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 607a8003-fdfd-3e02-887e-de2691d83572 | -6.67304 | -59.94044 | 2026-09-04 04:40:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f87e2c39-a15a-39c0-a946-b9f6829fc00f | -6.78288 | -58.95572 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d31b11b-06ea-3918-828b-44b475820603 | -10.3109 | -50.3422 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71d71ee5-4635-3213-9a7a-c787b64c8780 | -10.49529 | -51.34006 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3739cd0d-cf3d-37db-924c-b5cabbffb6fd | -14.79679 | -47.13377 | 2026-09-04 04:40:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92435ffd-dece-3eac-9ac5-ab7fdc06fddf | -8.44432 | -54.68827 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c736c9b6-621b-354c-80db-ae4409e28d64 | -12.99343 | -44.11358 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed5e1c4f-82a7-3b50-a249-eca164654aed | -6.68621 | -59.97506 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e4a5c5ca-9f00-37f3-915a-87af92a91958 | -8.42397 | -54.7212 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 564feb44-4d15-3605-8c53-bf437becab9e | -10.83336 | -51.81761 | 2026-09-04 04:40:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4dd6f82-e105-3104-aa9d-2f98b7116126 | -7.08032 | -56.52057 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8de1e7b8-cb00-37fb-a29c-e390545b7f07 | -13.40372 | -41.88289 | 2026-09-04 04:40:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e05020c4-7546-3bb3-ae66-7967352e071b | -10.91005 | -45.35735 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1773aa0-976e-3981-bd21-3df19bd3ab51 | -7.08692 | -56.51244 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e4f6787-6506-394c-aa34-2a0cc0b751b3 | -8.42909 | -54.69868 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aedfc90d-03a1-372c-b5e4-497d434a870d | -6.88201 | -56.50756 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2102d665-8bbc-3c74-863a-807969eea441 | -6.68431 | -59.98543 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 83659821-54d3-3f30-a597-789c7782662a | -8.43404 | -54.68821 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a438d25-55ea-3eab-9a95-1bb3b6e11f09 | -10.34927 | -49.93546 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc1795ee-b218-3a3b-a7ac-0da7162b01e7 | -13.58362 | -47.87271 | 2026-09-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21e4664b-7c6a-34ee-baa2-120e4fbc060a | -6.68682 | -58.75688 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a76f6be-8ba7-3a7b-a694-18814cd0c29c | -8.48893 | -54.66243 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a6ae04-45ca-35de-9530-1fde65a6523a | -10.55918 | -50.02491 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7053971-6433-30b0-91bc-608a31586df6 | -10.56252 | -50.02546 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0e536fe-6e05-39f3-a0bf-4c8c3c6980b5 | -8.42829 | -54.6958 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 158cb80e-a3f7-3984-ba82-92f37452b0ce | -10.91071 | -45.35291 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ecb945c-98b5-398b-829c-00b4d1fab80a | -8.10241 | -54.78087 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6794bc4-552e-3193-8b50-47d2844e426d | -10.00436 | -50.28505 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e15c61cd-b379-3d4d-96f7-f3f7211a16c1 | -12.54131 | -57.34669 | 2026-09-04 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8be5f8eb-8190-3e13-8b09-b65b447c9554 | -6.68527 | -59.98017 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b62184af-da7d-3527-b435-60df4472518e | -6.66929 | -59.96079 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ba102ae-02d8-35f6-acd6-c69d864de905 | -9.01339 | -41.0024 | 2026-09-04 04:40:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 494a5360-381a-3399-bd9e-8e456090ce51 | -6.68102 | -58.75561 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bddad72-95c2-37f7-8c53-913e81623b51 | -8.10679 | -54.78163 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6e061556-0772-393c-8e17-11b4f337138d | -7.09142 | -56.5162 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8aedb53-6083-3d6d-a4d8-49f71bf7e541 | -10.65239 | -50.39813 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6029f8c3-68dd-3ce1-b050-25fbeb4fc5ed | -10.86254 | -50.89688 | 2026-09-04 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 587d229b-3681-3d52-bdec-5f4c1b018fea | -8.41602 | -54.71544 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcaa7f7b-744e-382c-9c65-b1bb4e83deee | -7.09592 | -56.52 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README20.md)
