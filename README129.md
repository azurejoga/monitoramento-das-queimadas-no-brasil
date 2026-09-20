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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a914bbc4-a6e8-31d8-82c0-514f7847f098 | -11.4714 | -47.776 | 2026-09-20 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f16e845c-06d6-3640-a1d2-5134b970162c | -10.41 | -48.933 | 2026-09-20 14:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 431ff57d-b7f3-3621-97c7-5fad9849093e | -6.5569 | -45.566 | 2026-09-20 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b46bd50d-2301-37b7-8f88-6dc525cd01a7 | -5.9985 | -45.2476 | 2026-09-20 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 8b0d68a2-6923-3f00-963e-354e58fb238c | -11.75 | -50.6993 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 7a30e136-0a58-31b6-80d4-e73a7fec06fa | -13.9641 | -47.8464 | 2026-09-20 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| df2b08aa-ccd9-3e92-8d53-b1d24dc0f6f8 | -6.8982 | -41.7217 | 2026-09-20 14:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 281339f6-7a03-337c-8a6e-e0d7db731670 | -8.6628 | -45.4379 | 2026-09-20 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| aede57dc-1c98-366d-a570-0af73a33a520 | -8.0706 | -55.3522 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 93367349-51ed-3478-8242-6c6e2ee3303c | -8.4611 | -57.6292 | 2026-09-20 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3691d2c6-d46d-3f8d-93d1-d4bfaef34f46 | -9.0544 | -48.7469 | 2026-09-20 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 242.9 |
| bd5e5a05-8658-3135-bf01-aedca5581433 | -7.3073 | -55.6163 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 75c0c68a-5f99-3df9-b8f7-f3778ca5780a | -9.84 | -46.4136 | 2026-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 272.1 |
| 28eb6667-0a3d-3cbc-aa9a-0313d52c53ab | -8.0708 | -55.3321 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 9b002cc4-24cf-3e35-a617-3911100c68a6 | -13.0177 | -46.9125 | 2026-09-20 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3c8088a5-247c-39d1-a548-039a3d8fd814 | -8.0894 | -55.331 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2b57cbec-1fb7-36a9-b827-d042afb2772d | -7.7439 | -46.7629 | 2026-09-20 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 15c97bbc-318d-360e-93e6-08544c782877 | -11.3787 | -51.4412 | 2026-09-20 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 85c05525-2702-32b8-9cd4-6376afcd0158 | -10.5555 | -46.7544 | 2026-09-20 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 5d6982a5-f147-3888-8402-6fefdc2a6c18 | -8.4312 | -45.8693 | 2026-09-20 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5e26e6aa-6542-34fa-a796-bfc555859f10 | -6.7369 | -55.0874 | 2026-09-20 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 08cd7253-bedf-3ebd-a93d-86157a8261e6 | -11.3977 | -51.4392 | 2026-09-20 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 13f72abc-698a-33c4-bded-65355a45de6b | -3.7856 | -60.7335 | 2026-09-20 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 722149a2-7c12-39ed-9759-5017ab321383 | -13.4139 | -51.7358 | 2026-09-20 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 29b9b807-2e01-3204-8e21-92b6c5348770 | -10.8367 | -50.9266 | 2026-09-20 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 228.9 |
| 38b328b7-ec3b-3f7b-a2f4-101ec56046d7 | -10.9665 | -49.7583 | 2026-09-20 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 6f8ba7a4-b15a-3701-a3db-87cdeaaf2877 | -3.4428 | -59.0996 | 2026-09-20 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5c7edfd7-85f8-3a57-bee2-c86e57084aca | -11.0614 | -49.7477 | 2026-09-20 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 0fddd29b-f7a6-3334-910d-3874a08830cf | -13.5911 | -51.458 | 2026-09-20 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 76dd90d8-7db9-389f-a686-ace13f3d66d9 | -10.4103 | -48.9112 | 2026-09-20 14:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 1468ce3c-63ee-3928-b68b-59382c7bd02a | -3.3138 | -59.4472 | 2026-09-20 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 385e15ed-9768-383f-9a33-453a905963fc | -12.0454 | -50.0424 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 8e5ca7d5-2f12-38bd-aa5a-9b0ebcffa918 | -8.0706 | -55.3522 | 2026-09-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d84a5020-7432-34b9-84a4-2e997aabd0b0 | -12.6423 | -50.9144 | 2026-09-20 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 56e139f3-9bcd-3410-81d6-41b6759167a5 | -11.9681 | -50.1164 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| e5309e26-ce8f-32aa-baf5-0f28ab9ba157 | -12.5081 | -50.952 | 2026-09-20 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8811d296-b37b-37a4-88a6-6b723a1c9c1a | -11.8487 | -46.8781 | 2026-09-20 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 712239bc-598c-3dea-b2c9-863a44ebaf20 | -13.5907 | -51.4794 | 2026-09-20 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 4d473b1a-3a05-32b8-8c06-1196e8329985 | -6.7185 | -55.0684 | 2026-09-20 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| e6be609f-20e0-3947-89dd-dd85b769a8af | -12.8053 | -54.0669 | 2026-09-20 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 153e0682-aeae-3f9a-b3c7-7b971a3be674 | -11.75 | -50.6993 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 216.8 |
| db571996-d15c-3faf-94c5-f6a3d0b78cfb | -9.784 | -45.059 | 2026-09-20 14:40:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 38eb1aa9-1fce-3689-a1f9-2181fbbdc2c7 | -11.3787 | -51.4412 | 2026-09-20 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 209.5 |
| ac2c4381-a741-3e8a-8fd7-74b3324120ed | -8.4376 | -46.8757 | 2026-09-20 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| c9268d37-d851-374d-9d6d-28525afc77ec | -10.4673 | -45.0873 | 2026-09-20 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3cba2baf-75e0-356b-86d6-cf7f0ea9dd2c | -8.0279 | -61.3626 | 2026-09-20 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f6378543-8a50-3bcd-9a7d-a3c998eaf383 | -9.6964 | -45.8666 | 2026-09-20 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5c785dba-75ef-3a52-a556-f21160756b41 | -15.4667 | -48.4533 | 2026-09-20 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8e330c37-cf8f-3b0c-9388-664a23b118fb | -6.8982 | -41.7217 | 2026-09-20 14:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 0a72a606-7942-3e23-b66b-5d8f65ac4a95 | -11.1225 | -49.4601 | 2026-09-20 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ab906775-6cb1-314f-b96b-758e057b29b3 | -11.0065 | -48.3187 | 2026-09-20 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| d8501ea2-c676-3c30-8672-814e8f2fe5bb | -11.9493 | -50.0971 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 77110555-0c64-3d47-b1fe-673b0b8134cd | -7.2519 | -55.5994 | 2026-09-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| f4ff6190-3c5c-3d4f-9ff3-efea4b9935bd | -7.5941 | -46.7317 | 2026-09-20 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c1661b82-b307-3ac7-aa1a-52026399aece | -7.3073 | -55.6163 | 2026-09-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 96c453ec-2e0b-3dfd-8055-e6d7307957b4 | -3.3494 | -59.8097 | 2026-09-20 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 03b1b428-b562-32b9-b157-3b26c265c917 | -11.9678 | -50.1379 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| dad19e38-7718-38dd-92ad-320946938ae2 | -7.4288 | -44.718 | 2026-09-20 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 03fbf462-f02d-35de-b717-da3666b04a36 | -3.3321 | -59.4469 | 2026-09-20 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f4dced2a-42c5-30e5-b9cf-b777cf47f46c | -9.3611 | -48.3032 | 2026-09-20 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7385d54f-0d92-3ad3-b25c-89702d27aaaa | -3.3492 | -59.867 | 2026-09-20 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 80737085-3dad-3a75-9d84-afd509674e3e | -7.5703 | -57.6962 | 2026-09-20 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 91f21e82-e4d8-3a38-8727-a203e80fa6d2 | -10.8553 | -50.9459 | 2026-09-20 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 304.7 |
| b38f8b6c-98b4-32f8-bec4-3b7888bd3a67 | -11.731 | -50.7014 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 227.5 |
| 8d1bdbeb-3cb9-334d-8dc3-d9d40bd34960 | -9.0657 | -61.3743 | 2026-09-20 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 86c9554d-2f6b-3a75-8fea-7433d7fd7fb3 | -2.8974 | -57.7987 | 2026-09-20 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| e3e82342-0fb5-3d4e-94ce-ab1418454cd3 | -11.0596 | -54.1755 | 2026-09-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 221.1 |
| 3b2d6547-dba8-3796-bf56-71b69d2b60cd | -9.8502 | -48.4053 | 2026-09-20 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 64677074-6641-3e9f-90f6-84486ab4e13f | -11.6621 | -50.2169 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 5554ea4e-c1c2-308c-8984-317a9781428a | -10.0975 | -45.6597 | 2026-09-20 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 3f776133-53b4-382a-a75d-73568e903a1a | -9.0355 | -48.7487 | 2026-09-20 14:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 33e75ee2-7ce9-3134-a048-87ab1a867f73 | -11.3793 | -51.3989 | 2026-09-20 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 44518b37-f428-3271-99a0-26bc526615c6 | -10.2793 | -50.2177 | 2026-09-20 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2851f2ec-0c8d-39e3-a841-5daf5d3bc6fa | -9.0286 | -44.9187 | 2026-09-20 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| d9a7061d-5bf0-3277-9458-61da127a44a9 | -2.9143 | -58.3401 | 2026-09-20 14:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 555c819c-926c-3db9-9c00-fdd86616be22 | -11.379 | -51.42 | 2026-09-20 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 210.8 |
| d61c514d-09fc-3a7d-b9dd-d8d40ac0df8a | -9.2868 | -48.2234 | 2026-09-20 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 526cdfe7-c807-3d79-bf1a-8d7af2d3f0e1 | -2.9157 | -57.7983 | 2026-09-20 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| fa41607d-194c-3d6e-aa11-f933918024e1 | -8.4314 | -45.8467 | 2026-09-20 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 48cb529a-5857-30f0-93a1-aa5ffb294d88 | -10.8757 | -57.1554 | 2026-09-20 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c34adf0a-4bb6-37a5-96f9-b514a4d43dd5 | -9.803 | -45.0566 | 2026-09-20 14:40:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 68638d2b-e23c-3591-b67b-50abe3673b70 | -13.0177 | -46.9125 | 2026-09-20 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 4d5e04cd-2ba5-3c8a-8198-5f453247bd99 | -9.84 | -46.4136 | 2026-09-20 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 289.0 |
| 5bad6800-1428-357f-8800-47273dd8e52b | -6.7666 | -59.1129 | 2026-09-20 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e1fa4e68-81b8-361b-b8e3-2254375787bc | -11.4345 | -45.3919 | 2026-09-20 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 248ffcc9-eb98-3aa1-ba5d-0dafbc98ec6b | -10.8028 | -50.6326 | 2026-09-20 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 8433d6f2-9d01-3996-b678-0608e6bf2021 | -5.8088 | -55.7095 | 2026-09-20 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 6f1c6119-e9f2-3356-90dd-e37d9522bf8a | -10.3914 | -48.9133 | 2026-09-20 14:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 916d3e01-4fd2-38d5-9053-420cb3c72614 | -8.4734 | -47.0275 | 2026-09-20 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 30a29357-d2c7-36c2-a14b-e31ed4662e73 | -15.4174 | -53.0236 | 2026-09-20 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 9728ded7-d177-3089-ae77-e7ce66d65652 | -11.6624 | -50.1954 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 064574a1-6046-300a-84eb-b7d80404f577 | -11.1222 | -49.4818 | 2026-09-20 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 6a9abc19-1fc0-34e6-a50c-cc513578fb44 | -7.5704 | -57.6766 | 2026-09-20 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 90ba0843-a02f-32db-a13e-da2b97368569 | -10.7466 | -50.5959 | 2026-09-20 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 407951cf-33b9-303d-843b-4dcecde56c19 | -8.0708 | -55.3321 | 2026-09-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7f684b5e-2a6a-375d-af6b-37b799a0a5cf | -7.0455 | -43.6928 | 2026-09-20 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 057dff52-d04a-39b7-ba5a-c055cfc2a6dd | -7.3289 | -55.2155 | 2026-09-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 352bc398-6731-3b96-8a67-2967181beded | -10.7652 | -50.6153 | 2026-09-20 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 1f96f249-5fbe-3aa5-94a5-9cac095afec9 | -7.693 | -44.6469 | 2026-09-20 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d37badf9-d990-3225-bfed-c8b62fbbbc74 | -8.1376 | -46.8155 | 2026-09-20 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |


[Clique aqui para ver as próximas entradas](README130.md)
