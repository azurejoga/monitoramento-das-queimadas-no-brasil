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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66bc7fdf-efe1-33de-8357-a271d32a6015 | -11.62657 | -46.78568 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 88510f00-1f1c-3958-a517-bdf04d5ed9cf | -11.2057 | -44.76266 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 27710972-633e-3703-959c-7fbccecc1395 | -15.15549 | -43.60174 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 1f33c76c-2ef1-34f7-b8e0-e65da6c29acd | -12.39083 | -50.23447 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f18320c0-4c75-3d4b-864d-86ddc8adbed3 | -12.75416 | -47.34358 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 073c84cd-1361-33f5-9f2a-5de8e282b0e8 | -15.16618 | -46.14311 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 994ff665-91cd-3597-a4fd-88045f00f754 | -11.21433 | -44.78388 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8f0fa684-e38e-3486-8e75-1f5c94222485 | -11.56152 | -47.39959 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e5758dec-9416-31c9-a533-9b530e7473fd | -13.31337 | -43.96445 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 37f11d4d-a825-35eb-aac8-b12ecb64caad | -14.08946 | -46.33236 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 191acb3a-f894-358e-8893-ec3a8009b888 | -11.37817 | -43.38613 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 1e011d9d-9e71-3a7a-857b-f3538b29af76 | -15.07107 | -54.60902 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 214.8 |
| f64660f6-e1e0-3e7a-ad46-e2f17b58087c | -12.64039 | -47.31968 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 040b6898-d186-3a9c-9bde-337c77aa287a | -14.17501 | -41.83427 | 2026-09-28 16:24:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 4464ed55-3d18-3e17-92e2-ed8a486c7f1f | -16.23705 | -42.18866 | 2026-09-28 16:24:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 921081de-7287-3262-a242-93d18c5154dc | -12.64371 | -47.34425 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dbc8eb6c-0c76-3860-acdb-8c2753fc3b06 | -14.11763 | -46.29464 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 219e1670-fafd-304b-ba1b-1228b9dd8514 | -14.12284 | -46.30525 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 370b4ed3-8435-3e58-8d67-93ff162a7738 | -15.53601 | -39.92466 | 2026-09-28 16:24:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b7e53ddb-5ba5-322c-be90-21e031a5dad7 | -12.432 | -44.15929 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ad6f0fec-849e-35dc-a1a3-0cbb087180e5 | -18.03718 | -50.82582 | 2026-09-28 16:24:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e38e863c-1529-3e8b-aaab-2d7075de806f | -16.38125 | -42.95652 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 757bf06a-3b53-33db-a9cb-f0b98f9cfa75 | -14.32254 | -44.8095 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 84fb21c0-a24b-32f3-a5e9-19fb2d12fc28 | -12.21721 | -50.4321 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| dca281b0-7bd4-3b10-8157-21da1f411a2f | -13.56936 | -49.08907 | 2026-09-28 16:24:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9f93e897-5dad-3f7a-bb01-568545b4a3bc | -15.68704 | -47.60053 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d26ffd85-f5d7-3271-bfb1-a50ce31c29d7 | -14.80048 | -42.83661 | 2026-09-28 16:24:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d16e3556-e97c-3148-aa28-5831dce958fc | -16.5481 | -50.51615 | 2026-09-28 16:24:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 35d81c8b-d850-304b-83a0-d68a10f50c10 | -11.71795 | -44.51935 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44c6e3d3-0477-3f16-b60d-6265db668372 | -11.39116 | -42.55523 | 2026-09-28 16:24:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| f24d1cd9-0ae0-3310-99bb-a683f0be0023 | -15.00083 | -47.86097 | 2026-09-28 16:24:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 92a665f0-2e50-3bc4-a317-76fd5c326be6 | -17.32587 | -53.95922 | 2026-09-28 16:24:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 936b1035-3db9-36d8-a30f-b3f8a7ff508b | -11.22269 | -44.79116 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9bdbd112-efb1-3257-b107-db7abf6b1f20 | -11.21793 | -44.78335 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cc4e16ea-4d97-37be-9a03-b7e51073c3c6 | -13.93546 | -49.07282 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 60b141bc-7575-32e9-b2a6-be622f3aed5b | -15.3986 | -47.91813 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 82c388fc-fba5-3633-933e-fa3d1906c0a9 | -15.686 | -48.21784 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c17663a3-3ad7-30d3-aea8-bb43ad34b6f0 | -12.00289 | -44.95882 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0a29e8a4-f363-3d2d-be95-549a30b2832e | -16.30807 | -43.13126 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7a63970e-2c9c-3ff1-9287-ae26719fbbf3 | -11.21288 | -44.76163 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23883ff1-c2fa-3a45-80ac-58686f76eb1a | -17.32694 | -53.9631 | 2026-09-28 16:24:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 147719f6-f965-3eee-8db9-d3f11a5d3b5d | -12.3864 | -50.24149 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| afeda387-3e53-3749-8923-c81edd9035a3 | -13.57055 | -46.3567 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2170ca5-d130-3615-8b33-b4945cda60d3 | -13.36203 | -40.96652 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8309e2b4-6d66-3e67-b004-a17314f95979 | -13.3783 | -44.01777 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f743bd48-1051-3384-8b2f-f09d454f0979 | -11.68392 | -44.52775 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| d4e01190-f211-31d0-ac1e-d29b376e0865 | -11.9028 | -47.02139 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9efa1fa0-1364-3177-af58-d3d96ee2fa17 | -12.8753 | -44.80179 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| aa13d079-8143-3638-8167-5d335efab75f | -14.80774 | -41.73576 | 2026-09-28 16:24:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 288.9 |
| 6a69d4f3-7a6b-3150-ac50-a7567eea7cb5 | -14.51462 | -48.30437 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ce9324d9-46a1-3598-9fb9-2ded64b1c36a | -11.70706 | -43.45918 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2026661c-b19c-35dc-8fa8-52f14b8cb202 | -16.26422 | -41.31936 | 2026-09-28 16:24:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9775a91e-e4e6-3c09-8952-ae67399cc86c | -10.61872 | -39.91002 | 2026-09-28 16:24:00 | NOAA-20 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7037b045-0e5d-37c8-9c70-103a4caa0495 | -14.49333 | -45.23932 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7ae8b29e-6dc8-300c-928b-f5de8a5f2e05 | -12.42961 | -44.168 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1480a172-33f3-375e-8e63-5345e93cbfbf | -11.15205 | -37.65284 | 2026-09-28 16:24:00 | NOAA-20 | BOQUIM | SERGIPE | Brasil | 2800670 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c11f8702-7949-3374-8107-0af7f8c16d10 | -15.06271 | -54.5955 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c648941b-529c-3920-a5aa-f76552292d09 | -11.37448 | -43.43227 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 3c81421c-a0aa-35ab-b8d3-6bfe52d550a9 | -15.08779 | -54.71257 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5755364c-884d-3255-986e-17d20f9a6a5b | -16.25704 | -41.67953 | 2026-09-28 16:24:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| accce87c-f766-3219-8c28-eec4d7605b8a | -16.33178 | -40.66201 | 2026-09-28 16:24:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5e48411f-07d7-3668-95f1-9596315b5e9f | -12.62368 | -40.21481 | 2026-09-28 16:24:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 514aaea9-828f-3094-9ecb-fe82ae3ba483 | -13.69705 | -48.82405 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d8d4e904-9884-3d9d-a7b9-bda68c1211b0 | -15.19085 | -46.14708 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6de488ee-f657-3627-954d-b4de27480114 | -13.48424 | -48.59576 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fb12d6c7-01f2-3483-811d-a960c8ce2137 | -12.64273 | -47.34567 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e4a5636d-8925-3c04-adfe-9c6a0df9874c | -12.36783 | -50.23123 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5fea3fcb-6c80-3a8d-bb79-d7a5bd6374fe | -12.06957 | -48.53867 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 529.2 |
| 078cf9a4-58c2-3887-9b83-2104ed8cbb9d | -12.74433 | -38.16465 | 2026-09-28 16:24:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 92e4d563-d531-38e3-89cd-f91320cc3a64 | -10.60259 | -36.69683 | 2026-09-28 16:24:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 055edc8a-1f6a-3dbf-a7f5-6afcad6ac966 | -14.33 | -40.09572 | 2026-09-28 16:24:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 71916b17-3e6c-3815-b7b0-6585e9d77ae6 | -11.68928 | -44.51436 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 88b2ffe4-fec1-3e82-bb56-2096494f2415 | -11.51289 | -47.38987 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a2e9847e-25fa-3963-919e-6c0005613bdc | -12.38678 | -50.24466 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6b12c68f-f6be-368e-9fb7-640154789a2a | -15.26593 | -47.62371 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 34a6a92e-df79-3317-b341-cf06b6ebd55a | -11.68333 | -44.52364 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b8e14f91-032e-3a23-b6fc-ada296260901 | -14.58724 | -41.2367 | 2026-09-28 16:24:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7bc91933-ad99-33e0-8742-7d4551f437fc | -12.70778 | -46.98157 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d788cb13-c72b-38f8-8efe-59956007ee57 | -12.37007 | -50.23711 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2c1beec0-f6cc-3995-9d4a-e1f780b34375 | -14.32445 | -44.8233 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 8d2a8752-2ec3-3656-870b-c7a53ccb9516 | -15.42906 | -39.09539 | 2026-09-28 16:24:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| c53c164f-9019-3e57-992c-777bf2918659 | -15.40511 | -47.92441 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0a5e7f91-30c0-383b-a0e6-c0df029af66a | -11.38089 | -43.40472 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 95e27e94-255b-3820-8c89-f08a2f86f483 | -11.53721 | -47.16013 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 02319420-886f-3155-9efb-0cb2662e7eef | -12.79686 | -50.59589 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2f8ef8a7-1a79-38c9-b906-9c393a7e2ba7 | -15.1947 | -46.1775 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 49c100bf-aec4-3fc2-92ec-80346cec0b65 | -15.68616 | -47.60278 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 535d2f61-c6b0-3800-8ec3-18f238294fb9 | -13.44221 | -48.61931 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 913d2b83-bfe5-35d3-87ff-af5d9bb327f0 | -16.34919 | -42.5781 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| aa5e57c0-f570-3140-801f-fd7723d515cb | -11.52134 | -47.38878 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 1dec4aee-730a-375b-a21e-b71c01f48c07 | -15.68652 | -48.10154 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 80c9e3d7-7281-3899-aeed-9909640a840e | -14.33848 | -41.38627 | 2026-09-28 16:24:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 9a76ed7e-5d23-37c1-90a2-e7fe0c7fe24d | -13.68681 | -48.81994 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a715b8f2-a0a1-3906-8587-94e2c1250cb3 | -12.37422 | -50.24009 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a51bf63a-f6b9-3702-afd9-8feb61bcd031 | -11.87141 | -47.10351 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 906541ef-d674-38b6-91fa-150c495bc837 | -16.35468 | -41.60714 | 2026-09-28 16:24:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| eb5f1d25-cf72-3495-bb75-cf7de68cb60f | -13.97999 | -54.01519 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8bc2c611-fea3-32b5-9f0e-40b7e9bf1004 | -12.78981 | -54.07017 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cee8e3ed-762b-39f4-aa73-0e7052f79cef | -11.71485 | -44.51482 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c6354fe8-2be5-3834-a2a1-0e1d77d428f5 | -11.39206 | -43.43344 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |


[Clique aqui para ver as próximas entradas](README106.md)
