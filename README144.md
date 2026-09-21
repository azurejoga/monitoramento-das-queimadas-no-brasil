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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d6a4ed9-47c0-3401-ae74-b9a991f17b71 | -9.3986 | -48.3213 | 2026-09-21 15:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c81ea0ce-1d31-3ebd-8136-4a89b40442e0 | -7.5661 | -61.3239 | 2026-09-21 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5d1d2e38-62e4-3785-8149-50ccb0534275 | 1.5469 | -55.8255 | 2026-09-21 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6f675c3a-3571-3655-a44e-939f6997a2cd | -11.8362 | -50.0244 | 2026-09-21 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 37507e84-a8f4-3a18-a927-d65c11fd2deb | -9.8686 | -48.447 | 2026-09-21 15:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| dea0b31e-86b0-319a-8502-bf615cd4362d | -10.6883 | -50.7084 | 2026-09-21 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| b3b293fe-93b4-35fd-8efd-e61139b4bcac | -10.6376 | -50.266 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| be687dbf-70d4-3be8-90b1-755adbe43d81 | -3.3823 | -50.4486 | 2026-09-21 15:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5147a637-7355-3cfd-ad86-ea876ba02a5e | -6.4485 | -59.9909 | 2026-09-21 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 0bf52287-007c-340f-9a17-892536f29f87 | -10.7466 | -50.5959 | 2026-09-21 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9587828a-1ec9-332e-bff9-367acac4f358 | -6.8468 | -55.2617 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 556b6d93-dbea-3861-af04-7c25c3a07bb2 | -6.183 | -47.6133 | 2026-09-21 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4f4a1fc7-d170-3371-a64b-3e6d8015d850 | -3.2817 | -57.8685 | 2026-09-21 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2e773323-86d3-36d0-ad3b-d80887872609 | -7.2333 | -55.6004 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 1c856632-cecc-3cbf-aa2f-39f58ee2589f | -8.4922 | -47.0257 | 2026-09-21 15:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4c9debf2-744c-3463-8262-cd82f56850ea | -12.8899 | -50.9695 | 2026-09-21 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| bd663ec2-8f06-3d51-89db-f8872659619b | -10.6189 | -50.2466 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1665b9f6-0a9a-33aa-8afb-6973cd0f9500 | -6.8651 | -55.2807 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 54e04cae-0dca-3efb-91d0-b9db96efd090 | -10.6758 | -50.2406 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| f805a1d7-f4f4-3b77-a790-4737d26b285f | -4.4303 | -55.0867 | 2026-09-21 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 880c93c6-03c7-3f98-b1d8-89b308b26497 | -6.9223 | -42.9323 | 2026-09-21 15:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 176.0 |
| a6d4e940-f8b0-3905-bb43-9f8ab60baedd | -11.8359 | -50.046 | 2026-09-21 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 360c15a7-7fc5-39a0-875d-eee8cdeeaf3a | -10.3549 | -50.2099 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |
| b0cd76a7-7d68-3a29-a9dd-0b6a8858128e | -6.4486 | -59.9717 | 2026-09-21 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| ba399e59-06f5-302b-af08-6db7834c7031 | -9.8689 | -48.4252 | 2026-09-21 15:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 95c874f4-b238-3d3e-bb1d-5759f356849f | -3.3322 | -59.4086 | 2026-09-21 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d8548589-0a92-3a62-883f-1a34a9091047 | -10.6694 | -50.7103 | 2026-09-21 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 356b44e9-eacd-3e1b-b532-a85a2776a5be | -4.6112 | -55.7558 | 2026-09-21 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| be76aadb-c815-3b3c-9bd7-0a456dd39f6c | -5.6408 | -43.392 | 2026-09-21 15:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 43e52e7a-7782-33a0-9339-d4981f3245fd | -8.1496 | -54.8049 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d53d4323-a202-3791-a337-a3e509788dfd | -6.7863 | -58.8995 | 2026-09-21 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e8d9ced1-862a-3058-9b09-167cfe4487ef | 1.2059 | -50.7685 | 2026-09-21 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4863a6bf-761a-3d48-85dd-bd26da135bff | 1.2239 | -51.018 | 2026-09-21 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 89.8 |
| c8fb4793-b5b3-3bba-bd49-871bcd9bb6c8 | -3.6631 | -58.8835 | 2026-09-21 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| d5956682-3bbc-3ab5-a6a1-6f9ea7e3194f | -4.3542 | -55.6455 | 2026-09-21 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 996f7d27-48a4-3ef4-9466-9a48b3c1d42c | -1.1345 | -49.2123 | 2026-09-21 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5c68aaaf-149d-3640-bfdb-0fe5bda516b8 | -3.0788 | -58.3948 | 2026-09-21 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ae304d10-1e96-3c4d-80f4-c76c9c7119c5 | -8.7706 | -45.8567 | 2026-09-21 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 25318fe5-a1c5-3db7-87da-f3f088bcd288 | -6.8058 | -55.8217 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 9e4cb311-3152-377e-a2c9-afddb1c750d3 | -7.2704 | -55.5983 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c93bc4d6-82c7-3fe5-b50d-46412f02687c | -9.5595 | -66.0172 | 2026-09-21 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f0abdf90-3fed-37cf-82dd-c461da215e3a | -9.5779 | -66.0539 | 2026-09-21 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b7058301-4ef9-334d-9a6b-1c9e9958eefa | -10.473 | -51.2808 | 2026-09-21 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 4fe6ccf1-9c7c-35b8-947d-07494a0eeec3 | -11.7823 | -49.8152 | 2026-09-21 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 59d53a4e-a6a5-327b-9ae3-fa9507a24760 | -6.5451 | -44.8643 | 2026-09-21 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 245.0 |
| e0557994-513c-39d1-b230-91cf55750645 | -7.3444 | -55.6142 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e3df5084-bd4e-3d97-bbc5-5deabe4b358b | -5.2168 | -56.1096 | 2026-09-21 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ad81851d-6dfa-3e37-84ec-ad0c3d1cffaa | -6.5571 | -45.5434 | 2026-09-21 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 44f71623-0714-32cf-a066-c75f2aa311d0 | -11.8014 | -49.8129 | 2026-09-21 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 336d89d7-45ad-3af2-94e0-9e721efe180f | -9.1057 | -60.9511 | 2026-09-21 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 9d25ffac-9d08-3a3a-b69d-4379098fdb06 | -6.3657 | -58.2771 | 2026-09-21 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 42d94281-c31f-33b4-ae05-aae9bb912bfb | -7.5476 | -61.3437 | 2026-09-21 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6ba37f6f-bacc-39d9-b9fa-328b0fbc1e49 | -10.4294 | -50.2877 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 0838606b-7f6e-3c9d-93f4-afcfb8696d74 | 1.2055 | -51.0182 | 2026-09-21 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 4e8b8fca-90c0-32d4-98bf-9b42c9855e92 | -10.9358 | -50.5972 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d495550e-b9bd-38a5-9e81-bdd2a5f5ce26 | -2.9709 | -57.7197 | 2026-09-21 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b3fb1dc0-9096-3cbd-9382-885b73ecc18d | -10.8282 | -50.1601 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 221.8 |
| c3e6f650-9bff-3786-9927-f3f01097a04a | -10.2982 | -50.2158 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 06750979-3d8c-3427-86c5-dab76d0d59f7 | -11.0804 | -49.7456 | 2026-09-21 15:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 342b450e-8fd7-37b6-99d5-dc293f5953b5 | -10.7073 | -50.7064 | 2026-09-21 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0789c53f-3cbf-34be-9eb9-93cefc011a10 | -10.0714 | -50.2387 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 76830a69-1c36-31f2-9885-4c448ca70a99 | -6.0993 | -59.9076 | 2026-09-21 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 4a0e3815-56a3-3bb5-95b9-09761fbb45db | -8.1688 | -54.7432 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| dc0f6638-6e53-3ae6-8a22-9861e02b4bdc | -4.3754 | -55.0288 | 2026-09-21 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 27eba1bf-5c07-3575-b381-e6f5a3a2b247 | -10.2979 | -50.2372 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| cf62ca1a-96ef-3c9e-ad90-591fee395826 | -7.3289 | -55.2155 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e605ae62-0200-34bd-8847-00607a8ffb71 | -0.803 | -48.6397 | 2026-09-21 15:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8e67d1d0-9a77-33aa-8795-e69e43b8a3d7 | -9.1711 | -49.9835 | 2026-09-21 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 606e6482-f624-3caa-b73b-44e0889931c1 | -6.737 | -55.0674 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e8f76b31-d609-3eec-bbe9-f2a40b3d5c4d | -1.3792 | -57.9747 | 2026-09-21 15:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 6693efb2-9a42-3814-8813-e63ebaad3b7a | -4.0925 | -62.0874 | 2026-09-21 15:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7c16db19-0779-30b8-9694-c5e50c0144c3 | -3.4461 | -58.0199 | 2026-09-21 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 18524824-e539-39b4-b08c-55a911a1644a | -3.6448 | -58.9031 | 2026-09-21 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| afcbd32c-4e63-344b-b478-2d90047d418b | -3.3867 | -59.5223 | 2026-09-21 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b79e618f-4d5f-3b10-8621-6a67611ab6e0 | -10.43 | -50.2449 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 45e2f223-77bd-3ed1-a363-22fd1760981f | -10.4919 | -51.279 | 2026-09-21 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 890c31dd-2d76-3803-9553-ce627f1f3479 | -7.3125 | -54.9359 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c44ee08d-b77f-347b-be53-73d21dab4acf | -10.3357 | -50.2333 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b3cb6322-6db2-3f1e-9833-ef74b6d82de2 | -9.8404 | -46.3911 | 2026-09-21 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 195.1 |
| fc1d4825-73bc-3399-8a9d-8bca4823dcb0 | -10.6143 | -50.5884 | 2026-09-21 15:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| df23a4ec-2853-33c5-b0fd-33ef61182b0e | -10.955 | -50.5738 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| bc0e3872-7abe-3f3f-be9c-2af5809d3af3 | -3.8392 | -61.1682 | 2026-09-21 15:40:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b4e82498-cf6f-38ef-a578-f82708b5d6d4 | -6.2585 | -41.6617 | 2026-09-21 15:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1154.5 |
| 5711139a-dd9b-37f5-8a3e-ada96f590a00 | 1.2423 | -51.0178 | 2026-09-21 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a60d8404-3aa0-31f9-a727-a204e3463150 | -3.4828 | -57.9803 | 2026-09-21 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 452d0ecd-5cb2-3c64-812c-941b71c0d963 | -12.026 | -50.0663 | 2026-09-21 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 96fd6e92-21e4-33ff-9552-45f49a5f10f8 | -9.84 | -46.4136 | 2026-09-21 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 76ba12b3-0c8f-36d8-bd68-7dc25ca6d4f3 | -7.5477 | -61.3247 | 2026-09-21 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 555d1168-3f68-308f-8fbc-b431be5442d6 | -1.6766 | -54.9327 | 2026-09-21 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| ab7e0f0a-5870-37e5-9994-0c2960a4d706 | -0.803 | -48.6611 | 2026-09-21 15:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| d2e18f14-e8a3-302b-bf70-766e6b717b84 | -8.6171 | -54.6126 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| a72b5d80-0fd9-3553-b2f0-1638155b2d74 | -6.2831 | -59.9394 | 2026-09-21 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f1f86c96-8294-3d6e-978d-a023a7089850 | -6.5634 | -44.9084 | 2026-09-21 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 48ba1e46-7d8d-3b9b-af69-cbba6dcd4bc0 | -4.4112 | -55.2466 | 2026-09-21 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| dd80e29a-ab34-31a1-8bcd-03dca40aa7aa | 1.2607 | -51.0175 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 11d84987-986a-366b-b1cb-9d303e7e4ee7 | -10.4483 | -50.2858 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a8f676b0-4fa9-3304-acbe-21bc1668189f | -6.2948 | -47.6274 | 2026-09-21 15:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 7b984913-8b2c-3aff-9c68-e93eafa63e3e | -10.8093 | -50.1621 | 2026-09-21 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 163.7 |
| b0c69165-045a-318e-91f5-70cecc1c812e | -7.3289 | -55.2155 | 2026-09-21 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 33eff9cc-20f3-333a-8035-4c3db69a3afe | -3.3505 | -59.4082 | 2026-09-21 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |


[Clique aqui para ver as próximas entradas](README145.md)
