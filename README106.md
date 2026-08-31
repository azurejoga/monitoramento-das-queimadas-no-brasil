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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88243619-d919-3cca-b999-0932e8f79d8e | -3.3929 | -64.7103 | 2026-08-31 16:20:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a2944291-6fb5-35f7-b068-08e4a80e1c3a | -11.0376 | -51.4559 | 2026-08-31 16:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 942072e5-22b4-3764-aabd-814abb35963b | -9.1544 | -59.3669 | 2026-08-31 16:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 940dd1e6-b3e7-31f0-b1dc-9a4165bcbf2f | -9.8927 | -60.2752 | 2026-08-31 16:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8c7465da-a3a2-30e4-adb5-c40e1f66718e | -13.4519 | -57.039 | 2026-08-31 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 5317771a-5ae0-3729-b661-d187d3952b96 | -3.1267 | -61.1811 | 2026-08-31 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1919da02-a286-3fed-b276-865b4a00c3a5 | -7.9236 | -44.2558 | 2026-08-31 16:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| eb0d3604-ccbc-302b-846f-25416bec86aa | -9.4339 | -45.6931 | 2026-08-31 16:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 297033fe-c66d-3674-b012-1aabfbc7bfca | -8.6674 | -62.8179 | 2026-08-31 16:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 1105027e-05e2-361f-baca-d98cf0ccfbca | -13.4899 | -57.0556 | 2026-08-31 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 70384b7d-49fd-3bd0-946a-f94d14c570da | -3.7566 | -65.1309 | 2026-08-31 16:20:00 | GOES-19 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 7099bba6-8a29-3b27-9aff-7ad772f8360d | -10.8025 | -50.6539 | 2026-08-31 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| bfca614a-bf39-32d0-b27b-1e62c7ce731c | -3.4185 | -61.3273 | 2026-08-31 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| eca1c49f-f585-322b-b633-b578b6c7f362 | -6.137 | -53.5259 | 2026-08-31 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d8035667-b586-36cf-8baa-6d0a5eb33903 | -13.4516 | -57.0592 | 2026-08-31 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 74021e4e-17d0-32b5-a39f-f0a7a032a420 | -6.7647 | -59.4601 | 2026-08-31 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a2a01500-9bde-3de4-9118-ec525f96bd69 | -8.5924 | -66.975 | 2026-08-31 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 32b3f114-815d-3a71-a30f-8cfb4405ee85 | -9.4342 | -45.6704 | 2026-08-31 16:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 0b45d156-a8b4-370e-a10f-ec3db2c58f15 | -3.9363 | -59.3381 | 2026-08-31 16:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c3b80f6f-ca0d-37e9-b06a-95dcadfaba4f | -10.802 | -50.6965 | 2026-08-31 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d2344520-2767-34e7-ab1d-1356bbd921eb | -9.6676 | -47.9429 | 2026-08-31 16:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 296.2 |
| 0ed1e42e-2af3-3dbf-b201-00799a32992d | -6.8201 | -59.4386 | 2026-08-31 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b9d8afd4-5a30-350c-b7fc-0eb43c301e7b | -10.5598 | -50.4236 | 2026-08-31 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| c5da3066-9d72-3d27-95d1-f9b73fdedd09 | -11.6975 | -54.5467 | 2026-08-31 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 2a269c54-7207-37a9-88a1-3dfcd1c25314 | -7.0057 | -59.2575 | 2026-08-31 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7527b8da-5dbd-34ae-9f8b-8977f3045d86 | -19.1536 | -57.4186 | 2026-08-31 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 248.6 |
| d43dd865-9fde-3a7a-9912-3fb5e0e4be42 | -3.1839 | -60.1559 | 2026-08-31 16:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 2e219732-5c30-37ae-a745-ec33cfa224f6 | -11.0818 | -47.1361 | 2026-08-31 16:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 10bd8983-9fa3-3afb-8900-b152a3e5ebc9 | -9.3873 | -60.5721 | 2026-08-31 16:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 719f00fe-f820-3a5f-9881-ca041b63af5a | -6.8193 | -59.5734 | 2026-08-31 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| f86d667a-ffe9-3e5f-8ad4-f333679e4ff7 | -6.9872 | -59.2582 | 2026-08-31 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 737d81c2-f41e-3579-823f-de08ce36abe8 | -6.1295 | -57.6637 | 2026-08-31 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 81b8b90f-171c-323b-ae82-7db0d51097b2 | -19.0744 | -57.3876 | 2026-08-31 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.0 |
| cce2df1e-57e4-38da-9bd9-b6cbe965d6ca | -9.6941 | -65.077 | 2026-08-31 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7d20cbdb-3dc3-302e-97f8-0a3b5e68c61b | -12.1714 | -50.5217 | 2026-08-31 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 742356bb-f57f-3882-a59f-a94dc4d135d9 | -8.87 | -66.8935 | 2026-08-31 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 923da2da-3c8d-3c66-bbdc-6df245f45a46 | -7.3087 | -72.8449 | 2026-08-31 16:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 281d3cfd-e12d-33c2-98d5-59e086f7d4c1 | -10.844 | -45.3356 | 2026-08-31 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| acbc096f-4af3-3716-94d9-5f596754fd92 | -19.0948 | -57.3641 | 2026-08-31 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.5 |
| ebdb12f6-e28f-31a5-b29c-3c81e44f3879 | -10.8617 | -50.4772 | 2026-08-31 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| aaa39819-69c1-3080-9f32-d52a5c6d8017 | -3.6399 | -60.5466 | 2026-08-31 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 41a4a761-e438-396e-8c9b-95dad617e047 | -10.8022 | -50.6752 | 2026-08-31 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ba23a66a-1fde-3b59-adbb-c6d1b23f04bb | -9.7126 | -65.0951 | 2026-08-31 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 23adb8f4-8b52-303e-9cd9-c08f805a5f58 | -10.918 | -50.5138 | 2026-08-31 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 1fb3f39c-7879-33f1-914c-099586137c43 | -9.5964 | -47.6204 | 2026-08-31 16:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| c76a8855-ec66-344b-a956-3c693dc98e74 | -11.0566 | -51.4539 | 2026-08-31 16:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 16fe3e9c-ec88-38e6-be3f-7a1be037ea71 | -11.1939 | -53.9993 | 2026-08-31 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 609b6a1b-b654-35f6-bf29-93755171f150 | -11.6786 | -54.5484 | 2026-08-31 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 96f16c50-de1a-34e7-8a52-719f1a0df0e6 | -10.5601 | -50.4022 | 2026-08-31 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| c0052312-aec8-3924-8c2d-a3aebe71bf12 | -10.8614 | -50.4985 | 2026-08-31 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| afa350ea-a9e6-32b7-afc4-79a4f51c9887 | -10.8046 | -50.5046 | 2026-08-31 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 12fc9980-b0c4-31a6-b105-add6b19d2ef9 | -19.0944 | -57.3849 | 2026-08-31 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 341.5 |
| 3a828cfd-5902-3904-b670-e31955d36903 | -5.5831 | -60.2307 | 2026-08-31 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 244.7 |
| a3e1432f-440a-3125-882d-e0a6c2e138b7 | -5.9636 | -57.6704 | 2026-08-31 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f1514a90-ceea-39bf-bbd0-b2aea0457a84 | -14.9858 | -48.1529 | 2026-08-31 16:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 956e9ae3-db26-3b4a-9b1e-a546239caeb1 | -7.9794 | -44.3193 | 2026-08-31 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 278.5 |
| 9f72f622-72cc-3259-a868-50de844df877 | -7.529 | -61.3635 | 2026-08-31 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 370e2df5-7605-3b23-9260-197081dbe746 | -10.3226 | -58.0847 | 2026-08-31 16:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a9281627-4415-3007-a8cf-2cb0417c0110 | -6.8203 | -59.4001 | 2026-08-31 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 000c9374-4c5d-3ed5-9aea-99b0da4d329d | -8.631 | -66.5473 | 2026-08-31 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 935cfa61-ee44-3dd8-85dd-2e494f0e1d55 | -18.26602 | -40.54873 | 2026-08-31 16:28:00 | NPP-375 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 9c425ec9-eee8-3ecc-82c5-036f12a1156c | -16.70915 | -49.35364 | 2026-08-31 16:28:00 | NPP-375 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e89bb5b7-37dc-3158-b39d-b2f260861557 | -17.53462 | -41.3163 | 2026-08-31 16:28:00 | NPP-375 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 2de4925d-00b6-35a5-be66-58e07a8a3552 | -15.02342 | -40.94753 | 2026-08-31 16:28:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ea41a66a-02be-3ca3-b74f-00d3564b14e7 | -16.4439 | -51.40595 | 2026-08-31 16:28:00 | NPP-375 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4c880301-75b6-3648-8608-384480d249b4 | -19.8281 | -47.92825 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 43fc820d-4f41-3b70-a378-ef5645b29a89 | -15.67042 | -45.91788 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| db4eb45d-875e-391a-8c1c-882f4b93d770 | -18.20735 | -43.96173 | 2026-08-31 16:28:00 | NPP-375 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 797e9f87-0304-3172-9858-150ac4221cd4 | -17.88656 | -52.11126 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 2684bcc8-a961-3ee4-8b7e-4905529e382e | -16.19564 | -49.31956 | 2026-08-31 16:28:00 | NPP-375 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68b1fa41-d199-357a-8a6c-02155d52f6c5 | -15.66989 | -45.91388 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| aab5ed56-07ae-3266-bbea-93bf66f8a0bd | -16.55773 | -52.51751 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 620b3fec-c32d-3675-b087-473e4b29ca88 | -17.20992 | -44.82812 | 2026-08-31 16:28:00 | NPP-375 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8d158d8-b5ac-380e-9614-06abb29bcbfc | -18.47977 | -43.9669 | 2026-08-31 16:28:00 | NPP-375 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ae4b016-840b-3d12-b3c9-64488340743c | -17.86844 | -52.17319 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 66b6da2e-dfbc-3b72-8013-74082f132f06 | -20.3078 | -47.83056 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 5640aab9-dafe-35e6-bf5e-edae4e502b91 | -19.82312 | -47.92883 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e4e6fabc-d70a-3f55-b5eb-1d346ea99fd5 | -18.12018 | -51.61964 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 92e13459-b755-3664-b724-eaefaa521d3a | -15.02008 | -40.94806 | 2026-08-31 16:28:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 66137151-c6ca-39a6-9b23-cc9e97adf09c | -20.28849 | -47.83872 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| ba7a4209-b8b7-3099-b537-1d8e2abb17dd | -17.85957 | -52.09718 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e466d088-180e-384a-802b-64ffdcf6fc57 | -16.70703 | -47.63907 | 2026-08-31 16:28:00 | NPP-375 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| ec02d262-aeae-3197-87cd-3b2777a6d778 | -17.3024 | -46.95954 | 2026-08-31 16:28:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 01199de9-2f6c-3926-9307-ab7d6a091f83 | -18.96076 | -39.97395 | 2026-08-31 16:28:00 | NPP-375 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 08cace8e-5672-3ec0-bb8d-2b348fa6aea1 | -17.87303 | -52.083 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f923d2d1-2112-3695-b965-151c98874e71 | -18.41706 | -47.96162 | 2026-08-31 16:28:00 | NPP-375 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8d1107e5-7ec1-3263-9d83-0924f70668be | -16.33486 | -39.50636 | 2026-08-31 16:28:00 | NPP-375 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5fad7412-0d7c-39da-a3bb-3770d509fdf8 | -20.30404 | -47.84278 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 575c6286-9a92-3eca-b842-0afa6fe14af0 | -17.88131 | -52.10345 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 220.8 |
| 31cc8bf9-fe41-37d9-8768-67241a8ea9b8 | -20.02032 | -44.20938 | 2026-08-31 16:28:00 | NPP-375 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 1d8fddd9-8841-3a18-83a5-9d2f2e9fde45 | -16.85152 | -43.29668 | 2026-08-31 16:28:00 | NPP-375 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23c7a79b-1573-3620-b2cb-4cdfa892dd14 | -20.73955 | -41.78177 | 2026-08-31 16:28:00 | NPP-375 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4826bc4c-286b-3170-8675-c2786ed22250 | -17.88815 | -52.10831 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 62265529-cc08-3f4e-b56b-59b5a4a0cab3 | -15.83376 | -42.6144 | 2026-08-31 16:28:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e0f3a324-8219-35c0-9abe-1eba30223609 | -16.81289 | -49.09068 | 2026-08-31 16:28:00 | NPP-375 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2dc83e7-3631-36ff-a423-f56fe3cd51b2 | -17.50604 | -44.2301 | 2026-08-31 16:28:00 | NPP-375 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c31df1da-7ef1-3531-9101-a8ca88e588ed | -17.75824 | -45.39841 | 2026-08-31 16:28:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f007734-095d-3b06-8399-e2a0c934ed3b | -18.73815 | -41.509 | 2026-08-31 16:28:00 | NPP-375 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 609bcc29-5114-335d-ae66-bb24d56e91e1 | -15.19195 | -46.2499 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d49148c0-b050-343f-a5cc-8ff936d53e75 | -17.53694 | -52.55322 | 2026-08-31 16:28:00 | NPP-375 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README107.md)
