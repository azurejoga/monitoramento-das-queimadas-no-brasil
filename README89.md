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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c63b1d5f-a512-336a-9dcd-52e95556b552 | -11.4828 | -58.5159 | 2026-08-31 13:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 241.6 |
| b81789ee-d9fd-3158-aacb-94996ef951a5 | -5.5943 | -42.3142 | 2026-08-31 13:50:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 7a466898-f0cb-3936-b6eb-a0ed6a2134b5 | -6.9176 | -55.7166 | 2026-08-31 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7594d8ff-9478-38d2-b3c5-ad4bda90a26d | -10.8046 | -50.5046 | 2026-08-31 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 7dcfa65a-4175-380a-95d8-3df2e0a0102f | -11.3423 | -45.1982 | 2026-08-31 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| c7396bf4-8b24-350b-8b96-68a66e257b3e | -7.1126 | -42.749 | 2026-08-31 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 6f3bdfcb-f426-3f53-addb-ad9451eba05d | -9.5961 | -47.6424 | 2026-08-31 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2e61195c-07f8-3780-bd3e-d56c58cd3c1a | -11.3615 | -45.1955 | 2026-08-31 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 4e377263-ca54-3dae-a085-53a61d94db6c | -11.0747 | -51.5153 | 2026-08-31 13:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 322a28a1-f949-3c79-bdfb-2e300fb8ec90 | -5.2547 | -55.9105 | 2026-08-31 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 8587eb78-9354-3a0a-9c40-7b3ebbd9983c | -13.9667 | -54.4157 | 2026-08-31 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 54597d14-3f09-3522-8402-5b9a7dea905d | -6.1109 | -57.684 | 2026-08-31 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| f3983fee-722d-3bc0-9aa3-febe99a0710e | -7.5844 | -61.3613 | 2026-08-31 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 99be2f47-3683-3be7-9700-debaf27d324d | -10.8212 | -50.6732 | 2026-08-31 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 662cd3d6-eea0-3118-8c5a-f42e7d00e3c3 | -14.4394 | -52.5176 | 2026-08-31 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| aead1490-2c7c-3da3-b6e2-c732f86c3318 | -11.3427 | -45.1751 | 2026-08-31 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 9be2ae0b-55c8-38d3-8cc7-126e048e0325 | -10.8987 | -50.5372 | 2026-08-31 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 760aea93-e3f1-3a08-879e-50eeeefcc59d | -7.7752 | -44.0628 | 2026-08-31 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 41a33cb7-f6fa-373a-af6d-1bcb95854d55 | -11.5279 | -45.5162 | 2026-08-31 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 81ee6e13-39fb-368b-832a-5fada0e0012b | -11.2298 | -51.2456 | 2026-08-31 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 6c8e903a-b66e-38ed-849f-9429f940aa12 | -9.5964 | -47.6204 | 2026-08-31 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 321.6 |
| c79b685c-e4cd-36a2-8f7e-fb35c165a6bd | -11.1824 | -50.5706 | 2026-08-31 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 88739ee1-df1c-3aad-90e3-41acc21b5b25 | -14.4007 | -52.5226 | 2026-08-31 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 1edfac16-3514-304e-b849-b688a94b353f | -10.8209 | -50.6945 | 2026-08-31 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 7c73dbf4-10b3-3b46-a98b-9ccc3c6e81cc | -8.7628 | -46.4642 | 2026-08-31 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 67ba4014-ec2f-31e4-b3b5-a90a50cc8c55 | -18.2695 | -52.7284 | 2026-08-31 13:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 05c1eb8e-0f6e-3094-b7ac-d4a2f6539431 | -7.3118 | -60.5897 | 2026-08-31 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 7e02f7c7-6dce-3b49-a972-b52906ca360c | -11.7973 | -47.6672 | 2026-08-31 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| bc7e182a-1f50-3427-ae7b-456500595fe4 | -14.2792 | -52.8758 | 2026-08-31 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 1cb670ed-5040-3868-97a6-19de1f00f2e3 | -7.1189 | -42.2025 | 2026-08-31 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| cf51029d-70fe-34f0-99b9-5eb239b4221c | -11.1821 | -50.592 | 2026-08-31 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a6313fa0-2f6d-3334-af62-2264b4e084eb | -9.4342 | -45.6704 | 2026-08-31 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 523.7 |
| 044195af-1087-36c8-b329-cd613f921cee | -9.4345 | -45.6477 | 2026-08-31 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 496c5b52-faba-3733-8991-3e3bef956adc | -18.27 | -52.7068 | 2026-08-31 13:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 160.4 |
| ce3b3a8f-6ea0-3fc5-abd6-7cf6f8df788d | -8.8175 | -62.4898 | 2026-08-31 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 89febbaf-573b-3695-8d82-35f29ab385df | -13.9474 | -54.4179 | 2026-08-31 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e2d45be6-a460-3af7-95cd-c8e1616689ac | -6.1295 | -57.6637 | 2026-08-31 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 1a611f06-18f0-3d65-8365-101dcd27cc51 | -18.2899 | -52.7035 | 2026-08-31 13:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 1fb6dcd9-bde5-33c2-bf19-38b34d245198 | -7.3119 | -60.5706 | 2026-08-31 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 362516a8-1f52-3516-a0c7-fd103fdd0fc6 | -7.1123 | -42.7727 | 2026-08-31 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| f91ec224-7dd1-3414-91b5-9dbf1a9306c8 | -6.6221 | -58.5771 | 2026-08-31 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5d58569d-ade7-3f6b-b30f-ed43b58b509d | -11.7378 | -47.8082 | 2026-08-31 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e0c7da6e-87ae-32f3-ac86-7cbace185cd6 | -7.5659 | -61.362 | 2026-08-31 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e2ca73a4-1a02-3ffe-ba0f-23b536bf41a0 | -5.9451 | -57.6906 | 2026-08-31 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e49f214d-d744-37df-9f66-50fc604c5981 | -14.2796 | -52.8547 | 2026-08-31 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a8e8c659-b8ac-3e0a-8b23-34a646de145d | -11.1634 | -50.5727 | 2026-08-31 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4a439c22-2094-3c31-8771-ae09d1534346 | -8.7442 | -46.4437 | 2026-08-31 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e6ffd510-bffb-372d-9c36-628d38f80f7c | -8.7631 | -46.4418 | 2026-08-31 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 324ba6b8-5d19-306e-8faf-dbae9e9faa23 | -7.7938 | -44.084 | 2026-08-31 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 219.7 |
| c533b90e-b5fc-3645-9a7a-9f6f627014a0 | -13.4379 | -51.4348 | 2026-08-31 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| dfc5da9d-94e7-3b1a-8947-062f611f75b8 | -8.799 | -62.4905 | 2026-08-31 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 572727bd-39ca-3d64-b6a0-5b25650cc113 | -14.5868 | -54.1153 | 2026-08-31 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 098544a1-a2f7-351f-b6c6-40c157f9fd4f | -10.7596 | -54.0384 | 2026-08-31 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 3dda51b4-146d-3283-b25a-b81975f31df8 | -6.9367 | -55.636 | 2026-08-31 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ada32b6d-cbb5-3a21-9515-e3320c611306 | -5.8973 | -46.1313 | 2026-08-31 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a4b03ee8-cc37-339f-8377-ac0f8921f1c1 | -6.6035 | -58.6166 | 2026-08-31 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 4c2411a3-aabb-3543-a27a-2dfb54013050 | -5.5647 | -60.2312 | 2026-08-31 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f87a5ef8-db0e-3662-840c-c392c62f6586 | -7.5658 | -61.3811 | 2026-08-31 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 27ec996a-eaa3-3767-9908-f7d8f88d24c0 | -10.8541 | -48.3587 | 2026-08-31 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 96d6c20b-4d06-3181-80e3-f62a447a3e8c | -10.8624 | -45.3789 | 2026-08-31 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 20691b95-149b-36dd-a198-5ae14517baff | -14.4201 | -52.5201 | 2026-08-31 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 73ea1f89-40b0-39a7-8dc6-41634ab3281e | -18.2904 | -52.6818 | 2026-08-31 13:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 87afe928-b427-3667-b19e-7690316f8944 | -15.8041 | -51.0627 | 2026-08-31 13:50:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| bcd9bd62-13ab-3ed8-b70d-0c152d88840b | -3.6215 | -60.566 | 2026-08-31 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 0c6e4815-2c60-398e-9076-066e276b3c01 | -8.7439 | -46.4661 | 2026-08-31 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| cc09df0d-9a1c-3a9e-a746-11ae1196f481 | -7.2933 | -60.5905 | 2026-08-31 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 70b7db36-c342-30e3-8cc6-7afebef3ccca | -18.2704 | -52.6851 | 2026-08-31 13:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 990451f9-5ee4-3761-95f8-bb869ca74e70 | -12.9032 | -45.8382 | 2026-08-31 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 78909cbd-9076-3011-bf6a-067aa7958914 | -6.2469 | -53.6826 | 2026-08-31 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c6eef81e-9ffe-3735-8bae-9a7fb8b1f936 | -5.9451 | -57.6906 | 2026-08-31 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| bcf8d601-9f92-3c4d-b627-26c61766daf4 | -7.3117 | -60.6089 | 2026-08-31 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| deeacced-81b8-3273-84cc-2f6792156c43 | -11.9186 | -45.0685 | 2026-08-31 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 4bf85cf8-0f2f-3bd3-a51e-d8a47d28cc9a | -7.5844 | -61.3613 | 2026-08-31 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ba163f43-cd07-3e9e-abf7-b43dcabef0bd | -5.2547 | -55.9105 | 2026-08-31 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 2a21061d-8fae-34df-9bd9-47947d9bb73e | -14.4004 | -52.5438 | 2026-08-31 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8024549b-7e1c-31bb-bb80-f232c3ea0ee0 | -6.2656 | -53.6614 | 2026-08-31 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 1b914e78-713b-354e-a9c4-a50637511348 | -11.2103 | -45.1017 | 2026-08-31 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 1125ae65-dc49-32d8-810a-d681ca5590a0 | -7.9239 | -44.2327 | 2026-08-31 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| ab57f5f6-9731-387b-b815-442192bfe239 | -12.9401 | -45.9241 | 2026-08-31 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f38ba10a-eaaa-31fb-9795-12d20d7c536b | -4.9604 | -55.8424 | 2026-08-31 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 687eeda4-4e23-30e9-9b1f-0a0a677fbfa1 | -9.5967 | -47.5983 | 2026-08-31 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 14286a82-4317-3407-8439-64a6531f35e5 | -10.8541 | -48.3587 | 2026-08-31 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 396872f8-485b-3484-8179-2cb623d1131e | -6.6221 | -58.5771 | 2026-08-31 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bf1f56bb-9dcb-30c0-8226-d30b170fb4da | -14.4197 | -52.5413 | 2026-08-31 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 73c5d585-860d-313a-93be-c4033474928f | -11.2286 | -45.1452 | 2026-08-31 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| b3c57181-88f8-32ea-85ec-3b7451a688f8 | -6.1295 | -57.6637 | 2026-08-31 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| bcaa0dc9-dee7-3f1e-b275-903d27cc15b0 | -6.9367 | -55.636 | 2026-08-31 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 815e9a4c-5304-3dec-b985-4ee8a22e3778 | -11.2298 | -45.0759 | 2026-08-31 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 2234a61b-84ee-3e19-b071-55d56ce8b369 | -7.6317 | -46.7284 | 2026-08-31 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0ba557ed-adc7-352a-86a7-3f96ba06b74a | -6.2469 | -53.6826 | 2026-08-31 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a1c63ee1-9d2f-388f-9056-82315216f92c | -6.1109 | -57.684 | 2026-08-31 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7f348af2-4e94-3012-85b8-4450e31729ab | -18.27 | -52.7068 | 2026-08-31 14:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 989ea42d-1ee7-30eb-85ae-049d6c76d6b4 | -18.2904 | -52.6818 | 2026-08-31 14:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 394c78cd-acac-37ff-868d-d55dbd1fdbab | -10.3205 | -49.9567 | 2026-08-31 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| aebd85b7-efe0-3836-8965-6303391569c1 | -7.1123 | -42.7727 | 2026-08-31 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 5c5b8dbc-816e-3d4b-8fa0-666107fe74ef | -11.2485 | -45.0963 | 2026-08-31 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| d328df9b-f0fb-3f61-9b80-3278f3febaf9 | -14.4007 | -52.5226 | 2026-08-31 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 89286003-bc72-33d3-961c-201cad8882c0 | -9.4345 | -45.6477 | 2026-08-31 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| e091322e-61ab-362f-8b23-d9bef6b086fa | -7.9797 | -44.2962 | 2026-08-31 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 228d301d-6d36-300f-9409-8daf5692f809 | -9.5961 | -47.6424 | 2026-08-31 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |


[Clique aqui para ver as próximas entradas](README90.md)
