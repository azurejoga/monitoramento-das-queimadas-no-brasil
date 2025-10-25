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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9b66dab-86cc-3119-a0b6-8790bdd644f9 | -10.96336 | -50.29007 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c75c7ea1-5f74-391e-b652-27dc821328c1 | -12.25662 | -47.44898 | 2025-10-25 00:33:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c8e573f-45fe-3ed6-9da8-cca83bb6e77c | -11.01833 | -47.81526 | 2025-10-25 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 39e883df-1876-338e-b4c5-b8223beaf0e6 | -14.38753 | -51.53658 | 2025-10-25 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 575a6625-9cb2-3bee-aabc-6aac58296c9f | -11.00444 | -50.3905 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2a62314c-9e28-389c-adac-313a02160eff | -10.87567 | -48.04504 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7176d4f6-c260-33b1-a7e1-244ec35d941c | -13.51437 | -43.42952 | 2025-10-25 00:33:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1c2be882-b390-3af5-aceb-d533b435f2b6 | -11.96399 | -55.26456 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| fb4198a5-8e15-3c83-b9b3-12a5d7ae9680 | -11.57238 | -51.46912 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8779f669-a882-357a-9b22-a4a31ad419b3 | -16.17079 | -45.08864 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f88b073b-763b-3c44-a9f1-8358ea48f6cc | -12.83714 | -48.63655 | 2025-10-25 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b8684ed2-8812-324c-a0db-be361c34acbc | -13.28575 | -47.49051 | 2025-10-25 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4aa0dd5e-421d-370a-b223-b93ccc8d57b4 | -15.23417 | -47.92165 | 2025-10-25 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d02d0135-3fe0-3262-8381-813650a60ded | -17.36712 | -45.49445 | 2025-10-25 00:33:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bcf56d51-dd47-3d58-b206-f2b5fe28743b | -15.01659 | -46.19961 | 2025-10-25 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 678c348a-7ea0-32dc-9f70-ab4263db67c0 | -13.47342 | -46.49543 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d60878df-5d73-3e13-af9b-179f68f8b587 | -11.96289 | -55.24958 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e543ce38-c9d0-3f97-b680-07211d56e423 | -17.37638 | -45.49303 | 2025-10-25 00:33:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 86bf7a30-eb9c-3485-85e8-c8f247dedf85 | -15.53364 | -45.69785 | 2025-10-25 00:33:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2d041728-6e71-3db8-8550-d2424a5099e5 | -14.8715 | -48.09328 | 2025-10-25 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 999ea5d8-c23f-3bab-ad51-9cfa36b161af | -12.11465 | -46.71327 | 2025-10-25 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1e488ef4-ff32-3f6d-b124-3fae9dff05b5 | -11.78279 | -47.55067 | 2025-10-25 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4c880cb7-2c48-350c-b3a3-e3cbb5f7f000 | -15.4614 | -42.98783 | 2025-10-25 00:33:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| efb5e635-49a9-3647-9d68-5cb72716d6ea | -13.65125 | -44.23127 | 2025-10-25 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 32fd06b5-e2be-3587-af8e-fe07e44774d2 | -14.19096 | -47.31075 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7b42076-f3e9-332e-8bee-d80538cedd13 | -14.52134 | -47.95121 | 2025-10-25 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0c75303e-3538-3aed-93a7-eb597946e440 | -15.31214 | -48.08054 | 2025-10-25 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75dcfc11-62be-3f32-9c9a-84a808740260 | -14.92552 | -48.14415 | 2025-10-25 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cd0c4f6a-ec7e-3d14-a632-a4f788638fa2 | -16.84906 | -50.52509 | 2025-10-25 00:33:00 | TERRA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 772dda35-ba53-367e-8772-eb012e5178df | -15.52584 | -45.70975 | 2025-10-25 00:33:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f1e5f65d-10e6-3fad-87a8-606da786047a | -11.06716 | -49.62259 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 9eafeeda-dd4f-397f-b941-6615644c57d0 | -12.0394 | -54.23744 | 2025-10-25 00:33:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3eb4641e-56c5-3def-afd5-912cee8e1756 | -9.99298 | -47.097 | 2025-10-25 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b54a04e3-08f3-3fbf-9443-aa1312564228 | -14.72751 | -46.61752 | 2025-10-25 00:33:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1882301c-ee46-3d7c-a0ac-3b103392e4ff | -14.17315 | -47.3135 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 7b3edd7d-7f55-33ff-85e8-c6670ef54f73 | -15.01804 | -46.20944 | 2025-10-25 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| da16957a-aaeb-3418-a556-0d3e937c4c3a | -10.93596 | -48.076 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dd3057f7-f2e4-3442-9ba6-b9094ec6b217 | -14.74292 | -46.596 | 2025-10-25 00:33:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6f04df4-3b20-30d4-9b6f-523cd0270820 | -11.0014 | -54.26373 | 2025-10-25 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 68b5a2ee-1de4-3ff5-b93f-bbaa63efad64 | -13.35828 | -47.41682 | 2025-10-25 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 74c1c3b6-40bf-3706-9ec3-dfa771b9b1d8 | -10.64512 | -47.84806 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 94b6ef3a-15f7-335d-a051-3dd6f879b249 | -11.05949 | -49.63295 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 083576e7-f89b-3144-941b-85413876408d | -14.88031 | -48.09195 | 2025-10-25 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7ff860b-b703-30b5-b45b-e1fa089e9015 | -12.12227 | -46.71643 | 2025-10-25 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| f824b85b-6de3-3b55-a3e9-9d60ff22c932 | -10.68791 | -48.08501 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 226cad32-648b-3ecf-8574-55c5503458bf | -10.42703 | -48.00191 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 72b9406e-5e1f-3856-8d4a-9b3f18603616 | -15.12583 | -47.93496 | 2025-10-25 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 773788dd-832d-39ef-9b28-c268f8652cb8 | -12.22719 | -43.30136 | 2025-10-25 00:33:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 38dbcb84-d149-3650-90bc-7f8866dc672d | -15.82685 | -49.0947 | 2025-10-25 00:33:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5dcd51a-c7c1-3907-a20c-d8684a089353 | -13.94541 | -43.82225 | 2025-10-25 00:33:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| adb7a2a1-3cac-3c0c-aed8-d26f219af895 | -11.96537 | -55.26988 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b825f2ad-344e-39c5-8c0f-31c705b18c9f | -13.65123 | -48.18854 | 2025-10-25 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 30101bd0-aa8f-33b0-819a-e7ae4d819ba9 | -11.06839 | -49.63168 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 69ddb9e7-3e90-3000-9b57-612873b3298e | -13.92096 | -50.26622 | 2025-10-25 00:33:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c3e993e7-049e-3ad5-b181-3bb9bcf685b4 | -10.34171 | -47.78843 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b96046a-b31f-3c41-9be0-427afacca58c | -11.42636 | -44.68114 | 2025-10-25 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a2b109ef-fcd3-3021-9b88-3f03c13ad13c | -11.59752 | -45.06675 | 2025-10-25 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6656fa84-3629-3f3d-a9e1-224f646e0bf5 | -15.55191 | -49.24011 | 2025-10-25 00:33:00 | TERRA_M-M | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0454b2e4-412b-37a9-a1d7-d23ebf14e26a | -10.91052 | -50.16943 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cf91be6e-a795-33c2-a103-c099b866e55e | -15.22534 | -47.92297 | 2025-10-25 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 91998d5f-e668-3a55-b32d-14a9c40abbd3 | -18.17029 | -51.76498 | 2025-10-25 00:33:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 172.3 |
| b8d6f351-c9b0-36a5-bc16-e4d96380561c | -15.23543 | -47.93074 | 2025-10-25 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 5d3e175c-6633-369d-8c79-ba1c15c5ff25 | -10.98372 | -44.72932 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e1bc92be-9e70-3725-9578-e0ab3a3c4eaa | -14.56491 | -49.83941 | 2025-10-25 00:33:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 792fd0e7-2b19-384c-9257-37ebe7e9ee5d | -10.0638 | -47.07981 | 2025-10-25 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a8dc4644-ae35-3430-8d15-8b011cb8a429 | -16.28262 | -58.39098 | 2025-10-25 00:33:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| c5f7f6eb-b2cc-3789-900f-be2aaf7c3938 | -11.05826 | -49.62385 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 784a2fda-5e70-31ba-b324-f606635208d2 | -18.17943 | -51.74946 | 2025-10-25 00:33:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 48123355-fba3-354b-9a86-de64b4bdf77c | -11.96096 | -47.64074 | 2025-10-25 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 37deb808-09d6-365a-8438-f85e5395810b | -10.42168 | -44.49964 | 2025-10-25 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2b2fa8f6-904d-3fa6-ac64-9fa51e0e3397 | -15.28948 | -50.76389 | 2025-10-25 00:33:00 | TERRA_M-M | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 62643b1f-7a7a-3afa-8339-2ed69894538b | -10.93442 | -50.41592 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 72541159-df86-3e75-811c-90a6afd87bef | -15.22408 | -47.91388 | 2025-10-25 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 28b8a3a7-d2a1-3525-bf11-1affeaf5d59c | -10.25193 | -48.00251 | 2025-10-25 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 64403520-2d07-3b31-b978-266199ad467e | -14.44584 | -48.07026 | 2025-10-25 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c4a418ba-f76f-34c3-a867-9a0ddb73f0af | -12.65839 | -41.26603 | 2025-10-25 00:33:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| cf82a12a-183e-37fe-8609-bed65a2507ab | -11.05282 | -48.32684 | 2025-10-25 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4aacefb5-c57d-38ea-832a-e6620c674ff4 | -12.15338 | -48.01993 | 2025-10-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 97742fb0-4f6e-37d2-97d6-938cbb2a21e4 | -10.95414 | -50.28764 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 115aaa50-c704-3326-a41e-684c5fdd53fc | -14.1549 | -44.32197 | 2025-10-25 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1becc2ae-d250-3848-82f3-af351e8465d3 | -11.14692 | -44.9449 | 2025-10-25 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 123a12b6-0c2c-32a6-9cf0-2c0832d755a8 | -10.86802 | -48.05524 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ff6f6f3-5a4f-3c65-af15-3ac1b5106ed3 | -17.36862 | -45.50463 | 2025-10-25 00:33:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e96555af-01f3-3490-b685-43a48218c45c | -11.00317 | -50.38099 | 2025-10-25 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e47849ea-4145-3415-b873-6feb400ae624 | -14.65521 | -50.18707 | 2025-10-25 00:33:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a172cd6a-d785-3119-8dbf-6ffe977fc7ed | -10.99229 | -54.25452 | 2025-10-25 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1792bfbd-3fe7-37b7-86a7-6224f7f8375b | -15.94697 | -56.12488 | 2025-10-25 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 37.1 |
| 22a6ed44-9426-3de4-8c98-8afb95b11448 | -13.02992 | -46.61607 | 2025-10-25 00:33:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cc199cb8-614f-3a09-a494-849fedae696b | -14.87024 | -48.0842 | 2025-10-25 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| e9c9c710-3965-328a-b77d-2e52dd7562d4 | -10.86676 | -48.04632 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d7efe33a-64be-38b3-8000-678e69bfecce | -10.88306 | -47.90393 | 2025-10-25 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92dbb954-d635-3480-93d6-44be99cebd54 | -14.52007 | -47.94214 | 2025-10-25 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ddb97172-6c9d-3594-91f5-f807d0d4c862 | -15.94761 | -56.11816 | 2025-10-25 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 42.5 |
| f93c9149-33c3-3336-85cf-3889bcf89aa3 | -12.46699 | -44.53423 | 2025-10-25 00:33:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2a1d3fc4-2223-39b4-a0aa-25b908581ec3 | -12.77126 | -47.37208 | 2025-10-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 526a4601-3971-3e97-9dcf-c7957471e2ce | -12.15388 | -43.94148 | 2025-10-25 00:33:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b1c4e8dc-44ad-3d0c-8c32-c36c810acf96 | -11.8543 | -49.86485 | 2025-10-25 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 570f07d7-9f11-3bf7-9969-429b2f90f2f4 | -14.5662 | -49.84918 | 2025-10-25 00:33:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| fb5aaca4-8f5b-38d2-a090-6a8da55a73f8 | -14.19226 | -47.3199 | 2025-10-25 00:33:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7d8aef6e-496d-3819-9e41-731729b232ab | -10.9789 | -47.86469 | 2025-10-25 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README4.md)
