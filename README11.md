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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ded83bf-6798-33d0-8251-e7d2ab144c6a | -13.04917 | -53.72553 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 774583b8-351b-3e55-bb26-3cb527a25402 | -13.37642 | -54.26596 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23059a28-0560-3128-a4f4-a3df7d9afdad | -13.04403 | -53.7212 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43be972d-e324-3ca7-a7e9-9b06e2103436 | -12.32958 | -55.16171 | 2025-05-09 05:29:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7507983b-7da5-3833-97e7-1021dc18c8ff | -13.05004 | -53.71799 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b6dd90d-3588-384e-93b2-084f1e45072a | -14.30502 | -54.65167 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b15f79c3-5df5-3ffe-b7bf-5a402f662b1d | -12.32948 | -55.16257 | 2025-05-09 05:29:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37162caf-9ecf-3025-9124-aad34355be36 | -13.36689 | -54.25422 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fcf24ff-8288-389d-b708-9affd6e65fd7 | -13.04987 | -53.72556 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd5e5532-d061-3d5e-aa59-d0eb1f5890ef | -13.05079 | -53.71803 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 311e2abf-66a7-3de1-ba61-49e00d924c89 | -13.0496 | -53.72176 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e76cc5c-cd45-3bc7-978a-1803e11d1979 | -13.05474 | -53.7261 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfa2c3f9-a307-3445-8281-9de262fcbd51 | -13.37269 | -54.25158 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d26f40d1-b49c-39c2-96b8-32d449468e55 | -13.03873 | -53.7244 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46de177c-1df4-3736-bcb2-0f02145b919f | -13.05518 | -53.72232 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13922831-447c-3958-9e09-dddb9be38e19 | -12.72451 | -54.97429 | 2025-05-09 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b05d497-10bf-305b-a00b-c7d62acbcd9b | -13.04873 | -53.72931 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae755832-7ee8-33ce-89c6-408f319eda9c | -15.36434 | -60.17269 | 2025-05-09 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bb0fbe6-2b82-399e-963c-ecde9830974c | -13.04429 | -53.72501 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a7631b9-855d-32f3-8b84-4f1fa55b717c | -13.37724 | -54.25918 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7f90962-dc65-39e5-9a09-0234f8bf4cd5 | -13.36648 | -54.25767 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8e49c53-8d93-3f2a-90d1-c934f2944c30 | -13.37683 | -54.26258 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b0e92e8d-5837-302d-8970-fbafd59cb5ef | -13.04359 | -53.72496 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9aaceb44-b5e1-3731-ae45-8afc42ff4ad1 | -13.09098 | -52.29704 | 2025-05-09 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1289a805-26cf-3087-b14c-d6b670f77f06 | -12.33456 | -55.16247 | 2025-05-09 05:29:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed9e8b6b-1e7d-37cf-af98-4448a3852398 | -15.36499 | -60.16797 | 2025-05-09 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5c5cf49-4aea-3b23-8ba7-6c21c255bfd2 | -13.04941 | -53.72932 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a44f98d-70fa-3193-8ac4-990788f9c26e | -12.7296 | -54.97492 | 2025-05-09 05:29:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c80bc6f-5b14-3699-a192-5ca2a9453d5e | -13.04316 | -53.72872 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c317e914-85be-3c9a-98c5-0c9a9801fbab | -13.04475 | -53.72125 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63396b91-9c19-35d9-a50e-d51c84bd3338 | -13.05544 | -53.72612 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0c2ea37-e07d-3ce6-a40e-89f16d9d61ff | -18.26285 | -53.00628 | 2025-05-09 05:29:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d250048-08f7-3027-8d45-7f528b5bd1c7 | -14.30993 | -54.65568 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16201786-4aaf-396b-9b57-b12ff906ffab | -13.37144 | -54.26189 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1116018-b83d-3716-9ffe-e609abaa22e9 | -13.05033 | -53.72179 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa422805-bc2d-3180-91c3-3e647a49b3cc | -13.37227 | -54.25502 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bdd3705-d0d6-3d60-bb71-4e4df2cc951a | -13.37185 | -54.25846 | 2025-05-09 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86144974-26c7-3224-92e3-90ce3ce93913 | -13.04383 | -53.72876 | 2025-05-09 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d08df3c3-6a05-386d-9460-043d53da71fb | -8.07 | -43.1216 | 2025-05-09 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| ab40baa7-e3d8-3341-9844-1a00b7e574fb | -21.78931 | -52.75114 | 2025-05-09 05:31:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4b01f39-fead-37d2-b7f9-10db2fb31ead | -21.78278 | -52.7506 | 2025-05-09 05:31:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eddd16db-8882-3936-95f9-7392a2baed94 | -19.84511 | -54.22625 | 2025-05-09 05:31:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 442e1c4e-bdf0-3c15-9f40-1232267bdc6f | -21.05107 | -55.9995 | 2025-05-09 05:31:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89ca86c5-2dff-3e76-bee0-4fd2ec919c08 | -21.78892 | -52.75302 | 2025-05-09 05:31:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbaf4693-01a5-3e17-9f0d-8311e03636fc | -21.78239 | -52.75246 | 2025-05-09 05:31:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 699c967d-e8c1-329d-a484-ba81eeb8566a | -21.05143 | -55.99591 | 2025-05-09 05:31:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eceab433-534d-3d25-ac2b-a2e4350e4f2f | -21.78975 | -52.74569 | 2025-05-09 05:31:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19835a63-3afb-359c-936a-b44179b86df0 | -21.78933 | -52.74757 | 2025-05-09 05:31:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9de46ce-d2a4-3152-b349-f3fc826567a0 | -21.7828 | -52.747 | 2025-05-09 05:31:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73e0a938-e852-3d6a-a6a0-e7157f28292c | -19.84554 | -54.22178 | 2025-05-09 05:31:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a92e64df-1b91-3b01-a529-de1fbf998ee4 | -8.0889 | -43.1196 | 2025-05-09 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 3dd401a5-ae38-364f-9574-ed2b6f343103 | -8.07 | -43.1216 | 2025-05-09 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 24c77e76-7590-3f5d-8eec-f5a66c00a6b0 | -8.0889 | -43.1196 | 2025-05-09 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| c1496f2f-8641-36f5-ba22-185b5be46c99 | -8.07 | -43.1216 | 2025-05-09 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 5920366e-f864-38ca-a697-585422500499 | -8.07 | -43.1216 | 2025-05-09 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| f30454cb-3fab-3b73-95f9-b18060929c44 | -8.07 | -43.1216 | 2025-05-09 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 444d353d-d157-32fc-9ff9-1f70951119b9 | -8.0889 | -43.1196 | 2025-05-09 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| a9e0a3d7-fdde-36aa-92e2-a8115b146bcb | -13.04657 | -53.72029 | 2025-05-09 06:29:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 865bd030-5744-3c43-96d1-ef813dc5b7b2 | -11.39583 | -52.9419 | 2025-05-09 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d716ba29-b314-3487-97b8-010b2777b028 | -13.37636 | -54.25892 | 2025-05-09 06:29:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 4a26ffe3-dfd8-3c2e-8a16-5e6ca42641b5 | -11.3833 | -52.94034 | 2025-05-09 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 09146545-3b7f-3b0d-8cfe-9eda28b589f7 | -13.37946 | -54.25397 | 2025-05-09 06:29:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 457d4ed5-9015-3978-a279-e5f3effb203a | -8.07 | -43.1216 | 2025-05-09 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 28195f6c-5d9b-3b88-a691-5ed38408f557 | -8.07 | -43.1216 | 2025-05-09 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 9d1d6994-5740-3a7e-b44b-54d2df174eaf | -8.07 | -43.1216 | 2025-05-09 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 4b93bcd3-6d02-3207-ae3f-46fdb8a519f4 | -8.0889 | -43.1196 | 2025-05-09 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 48e09c81-5671-342f-9a97-afaf28567c70 | -8.07 | -43.1216 | 2025-05-09 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 14283259-5dc5-30c2-aae3-736a40700b53 | -8.07 | -43.1216 | 2025-05-09 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| f4c1a98d-78c2-35fb-8ec5-3a1c8924d3ea | -8.0889 | -43.1196 | 2025-05-09 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| ac107e88-4c50-3ff8-89fb-2e97a5dd12a0 | -8.07 | -43.1216 | 2025-05-09 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 57341f70-c139-3b69-8262-e885214e7241 | -8.07 | -43.1216 | 2025-05-09 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 4202814d-2f4e-3570-a7de-e479668ec78d | -8.07 | -43.1216 | 2025-05-09 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| ff7c2f4f-ed96-3f79-bfbb-46805cad4789 | -8.07 | -43.1216 | 2025-05-09 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| d084a316-6f38-319b-89ec-e2377d242cf5 | -8.07 | -43.1216 | 2025-05-09 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 708032bd-207b-3ab0-b84e-93f8678d4e8c | -9.01932 | -36.65579 | 2025-05-09 11:38:00 | TERRA_M-M | SALOÁ | PERNAMBUCO | Brasil | 2612307 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| d5f14117-255f-3b7e-b8c4-003dbea384cd | -9.63358 | -37.0594 | 2025-05-09 11:38:00 | TERRA_M-M | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e4de4351-f5f6-34f9-816d-528e044903ce | -7.69091 | -36.1554 | 2025-05-09 11:38:00 | TERRA_M-M | RIACHO DE SANTO ANTÔNIO | PARAÍBA | Brasil | 2512788 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 685fc1a2-5eb7-3c71-9b16-8fc961baf9a1 | -10.9733 | -44.441 | 2025-05-09 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 46bde4b8-be93-391c-afee-522e6e78d0a9 | -11.84405 | -43.79372 | 2025-05-09 11:40:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 5a082832-2004-3567-9d65-b0381639e4a1 | -14.22863 | -45.46402 | 2025-05-09 11:42:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 88ab1b91-0791-31ec-b967-123ce8166d16 | -20.23375 | -40.23081 | 2025-05-09 11:42:00 | TERRA_M-M | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 2a4723a8-6e8f-3981-abaa-58c7808edb75 | -22.90663 | -43.73668 | 2025-05-09 11:45:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 388f73b1-0d55-3d9e-a751-fbeba8abd991 | -10.9733 | -44.441 | 2025-05-09 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 9ef65924-23c8-344c-9a91-8074b8a75117 | -10.9733 | -44.441 | 2025-05-09 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 6de5589e-2137-35c6-ae3f-50e672cecec3 | -10.9733 | -44.441 | 2025-05-09 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 199.2 |
| 53899f84-987b-3643-acd4-ca1be675d5eb | -10.9736 | -44.4177 | 2025-05-09 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 127ed17f-5259-3c35-b321-e8b943c8b03b | -10.9736 | -44.4177 | 2025-05-09 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 2936cd77-5662-3274-9a5e-411b4fa2286e | -10.9733 | -44.441 | 2025-05-09 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 6d253491-7666-3f9e-9f8b-5b31c5e4987b | -10.9736 | -44.4177 | 2025-05-09 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 58be0edf-e28b-39e2-9a8c-6d4811761865 | -10.9733 | -44.441 | 2025-05-09 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 19eb828e-07df-3197-81fe-032186efca6a | -10.9736 | -44.4177 | 2025-05-09 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 454d30d8-a776-3752-a9a3-69dbec1f3358 | -7.6156 | -46.4851 | 2025-05-09 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| dcabef27-8bbf-3bd9-8145-893085db1ce3 | -7.6344 | -46.4834 | 2025-05-09 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| dee84a0e-6f7d-38fb-b7cb-d2b083c19bc5 | -10.9733 | -44.441 | 2025-05-09 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 964e155b-0936-3fc1-923a-867477baaad9 | -10.9736 | -44.4177 | 2025-05-09 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 71a71639-89ec-308e-a9a7-b68981f44be9 | -23.6121 | -49.0181 | 2025-05-09 13:00:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 607c194c-1e4c-36d8-b85b-e237380f4fa1 | -10.9736 | -44.4177 | 2025-05-09 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 79715d2b-f010-3f00-a4ac-3f286fb9cf26 | -7.6156 | -46.4851 | 2025-05-09 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| eec7bd2d-5d06-3534-bae1-87420aad540b | -10.9924 | -44.4383 | 2025-05-09 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a388fc5a-7fd0-323c-a3b4-827eb10d685c | -10.9541 | -44.4437 | 2025-05-09 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |


[Clique aqui para ver as próximas entradas](README12.md)
