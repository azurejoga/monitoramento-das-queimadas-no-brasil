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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfea28d2-c111-3ab4-b702-640cb0998b44 | -12.27048 | -55.12742 | 2025-10-05 00:33:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 686e669c-d5a9-375b-bd1c-824d13aec66f | -11.10417 | -47.87701 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 17d48deb-bc0a-3356-8e49-12d64a12c014 | -10.66199 | -48.47941 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bde53f45-b2c9-3c61-a686-1c1e22483a13 | -15.30346 | -47.32954 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 216be239-bd6e-3f2d-9c21-03f39fe7bd09 | -11.69488 | -47.48932 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 46ab753b-d8d2-34a1-b233-cc1613c60b95 | -11.52754 | -47.67413 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 1b93a6c2-de4a-3e6f-a955-e691815ea51f | -13.30687 | -47.61546 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ea586f49-d535-3b37-adae-8dcd5aba78f4 | -12.95426 | -51.02953 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3243f9c3-7cc2-380a-99b1-e2539dd303d0 | -12.08156 | -45.15667 | 2025-10-05 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4f0cc9e0-2314-32b7-a531-483363284525 | -10.36028 | -48.16891 | 2025-10-05 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3fd9e4aa-833a-3042-9dfc-8a36a6fd849f | -11.50297 | -44.99445 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9c4ad436-c48b-3c18-b1e5-b3649fdd4d61 | -14.49981 | -47.51479 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46d36c5f-d79c-3809-9ca7-565eff5c31ff | -9.25835 | -51.80888 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bc044d63-d5fe-36a5-8181-1ebd6142d6ef | -13.34158 | -48.06073 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 80e21e3b-9374-3ae2-a98b-499059930f6e | -11.67587 | -47.48293 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c697c395-e967-37ad-8ff1-874fff663a69 | -12.32202 | -55.13816 | 2025-10-05 00:33:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| e0fd060b-42fb-3e24-835d-ee40cde5ed30 | -14.68385 | -48.31614 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 28ad7b04-27c0-3425-89cb-06da2cdd7666 | -15.13866 | -49.52417 | 2025-10-05 00:33:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 6e66d631-2157-3bf2-92ad-039db8efec88 | -13.0007 | -44.00638 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 5401db8d-ed70-3526-9fe7-1a58a06b0fbf | -13.1442 | -50.92253 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| fdbb3b84-93f3-3b63-9fc0-75be8fd43dc2 | -16.35363 | -47.05945 | 2025-10-05 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 005f16a4-d8ab-38d9-a220-3722aa9685ef | -13.15405 | -47.97182 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8fd6b809-1e62-3e72-9a3b-9d9e06068e65 | -12.78257 | -48.8237 | 2025-10-05 00:33:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| da91f2d0-a454-3b63-9468-26983b4f72c1 | -11.44134 | -43.49078 | 2025-10-05 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0eff0e6d-fbe7-37db-9684-59ae59acd1cd | -15.12425 | -45.75069 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| bc05959e-aa4e-392b-8a01-6b7247300b02 | -14.6585 | -48.32949 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 47ea152e-3034-3510-a287-162c5ba4f8e8 | -11.80634 | -46.84931 | 2025-10-05 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 7011db1e-69de-3683-810d-6e566a888979 | -16.05363 | -48.09966 | 2025-10-05 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d632c355-632e-3ba7-9913-c17975c70c2f | -13.08732 | -47.89626 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b1792552-1484-343a-a6ae-ad2d8caf134c | -11.11887 | -47.20131 | 2025-10-05 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 09af8ae8-a07f-3352-a6d4-9f5df6d75a77 | -13.34927 | -47.19661 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8426434e-7e08-3376-93b8-b5e690f2cad7 | -15.7714 | -46.26664 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 74b2d737-4890-30e5-94b0-c928f48d2428 | -13.30748 | -48.0905 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| de79eceb-8e36-3190-9e67-2572560039a4 | -12.81161 | -46.84855 | 2025-10-05 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9325c83b-687c-3690-b707-9b5f91ab5f49 | -14.0956 | -46.34966 | 2025-10-05 00:33:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c3255823-1ac7-3ff2-8c08-76ee0c637427 | -11.06141 | -47.77966 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4f79ad18-20de-30b6-ac0d-ae3565715e10 | -14.00632 | -48.20689 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 56e01d86-2330-3e8b-9d05-8b152313ccef | -13.00323 | -43.99869 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| d8e571b9-ee37-3ea1-8483-ce135b937695 | -11.50121 | -44.98291 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d9fd805c-124e-39da-8d8c-1c7547655f44 | -14.56799 | -52.47084 | 2025-10-05 00:33:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 532a66e8-19f1-3df0-9ec5-ea7887bc13e0 | -13.30938 | -47.63346 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eb757463-9e14-3002-92aa-1be42de515b7 | -13.09748 | -47.83969 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c4aab008-dab1-3341-bbdb-e0a5d00edca1 | -13.14151 | -47.94611 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2ece0c2b-06a7-3802-bc91-33d710e00f9b | -14.01201 | -48.66062 | 2025-10-05 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 6889ba3a-f511-31cd-9d06-8610a5af3b6a | -13.30239 | -48.11886 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3b2eca9e-9a28-3611-b4ed-419bdc960ca3 | -11.82461 | -45.08948 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| e211284c-a9b0-3807-afa4-5978141274f4 | -8.54175 | -46.3283 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| eae6676d-5d14-35b5-9d30-2aba6e6b9fb6 | -13.57693 | -48.17063 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 00eab5a8-c6dd-3e6d-987f-6b42f1b4108c | -10.57183 | -48.68967 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 90c57805-5045-3308-afe8-1ec437bb5e34 | -14.95107 | -46.85269 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b1548cf4-6f63-3911-8627-c43ef0195bd6 | -14.66489 | -48.30975 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bcad6061-1971-3c11-a163-5b493063c6e0 | -11.53638 | -47.67281 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| be74874a-946f-3e03-8997-c42a82738101 | -14.6484 | -48.32174 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a9309a7-edb2-3c26-98c4-e1d74bbe0448 | -15.13338 | -45.74925 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| bac3f009-fb89-3123-852b-573ac77d78d5 | -12.57158 | -48.16458 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| f8c3f083-c0fc-3043-8ae7-cb5e0f7555fc | -12.69326 | -47.58398 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9d5ed922-94de-32d2-93e9-1ae2202a6ee8 | -13.51311 | -47.24317 | 2025-10-05 00:33:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c3915947-1b9c-326d-8b1c-bfd99781caa9 | -11.867 | -56.88963 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 150.1 |
| f4324cdd-be09-34db-b9c6-4038bb45212e | -13.24995 | -48.47376 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c81d84ce-1bac-3fdb-a5d6-6b656527365d | -13.25119 | -48.48286 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 572cabeb-9cdc-301c-88bd-a13469b8bfd1 | -14.97083 | -47.24981 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ff48e67d-15b2-3048-8b56-e9db18b21f43 | -11.81668 | -46.85723 | 2025-10-05 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| b52f23d2-63c5-351c-80fd-ea2ada764dee | -15.1228 | -45.74089 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 00be1b95-29d1-315a-98ec-505c964400fe | -16.20846 | -49.19593 | 2025-10-05 00:33:00 | TERRA_M-M | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| eb85452b-4b44-3edf-b081-edf36630c1e8 | -15.53436 | -46.81049 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ea75d1cb-0655-3565-8c95-5f040f3a4419 | -11.24033 | -47.80522 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 8ca6b76f-5cc4-3ebd-b28d-2a958c086ad2 | -8.55015 | -46.28894 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9a8599c1-fa0e-3fa7-a08a-cbcdb295138f | -13.30675 | -47.80857 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6c04f5fd-dcde-36a6-827a-d3783532b601 | -13.50182 | -47.29118 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 37253b17-80d0-3d43-a6ec-6a1526b4e1a5 | -13.52195 | -47.24181 | 2025-10-05 00:33:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 256197ac-35cd-3530-b6d2-95b2b224e572 | -10.4915 | -48.11045 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0cc57482-a060-3fb2-bfc4-05f69f27c3b5 | -13.09873 | -47.84867 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 01c25bdb-d4df-3a04-9f53-2e9188b19329 | -12.89582 | -47.31348 | 2025-10-05 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c8a45cf9-28df-3dfa-98a1-b3e630e4477e | -13.73485 | -51.30814 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 59e2d9c6-0433-31d8-92c6-1936bb31ac38 | -12.60065 | -48.16327 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aaf36b6f-c4c2-365b-a6a0-1d23be653e05 | -8.93499 | -48.65458 | 2025-10-05 00:33:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 87e83403-e088-38d5-a408-5c0c7b06acb8 | -14.9156 | -46.85776 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| bc18e17e-f3d6-3e63-b396-8528b6044244 | -13.72445 | -48.09987 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ac7f7d90-0fdf-3c98-aac9-e83c63859902 | -14.32966 | -47.68169 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| f6cbd813-9e72-34c7-a1c0-f18f00afb7b1 | -14.33597 | -47.66231 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc0150b3-e419-37fc-bfc8-dbceae397592 | -13.03809 | -49.15277 | 2025-10-05 00:33:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 724934be-9fed-3cee-b51e-7d34d3f72205 | -16.07992 | -50.92023 | 2025-10-05 00:33:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b87efb53-2268-3469-a598-920c28e45693 | -10.35146 | -48.17021 | 2025-10-05 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| a55d00af-96ab-3546-9fb2-53b4ebc023e9 | -11.88236 | -56.88808 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 26db2126-8cff-3a52-98bf-08bb3928c446 | -13.14673 | -50.92735 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 1a4f1f39-3b0f-3650-a59e-67dd0e76003e | -9.14654 | -50.06424 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 244f9834-91d6-3196-bf2c-ae44f116fd5a | -14.60904 | -52.52728 | 2025-10-05 00:33:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8a93a9e6-5cfe-3d8a-be43-f1c489e0ecd4 | -13.13036 | -47.8009 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e0e5d33-806d-3b30-a2a0-3b3bfeb16947 | -12.4475 | -44.73524 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3ea7beac-8b63-32dc-b833-aebed8dd4f86 | -13.15238 | -50.97282 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| bb727eaf-d4e5-3570-bd60-84f123ebf6bb | -9.9144 | -45.95751 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1714d1e4-992f-3a13-a4d8-25fa48043267 | -14.32086 | -47.68301 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3c3e6ccd-84b8-35aa-b960-212f891b0e6f | -11.87008 | -56.89599 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| f7361a7f-6b96-3619-83e4-a200e7e57d78 | -14.92448 | -46.85655 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 833c41f9-a155-3515-8e5c-f9facba81311 | -14.68511 | -48.32539 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5ffce23a-3948-398f-b60b-bb8d75329590 | -11.8652 | -44.94875 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5d576f9-64fa-39da-92be-a63038ff30ec | -11.52625 | -47.66505 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8ed74a48-96e2-38b2-a1c7-243b1ebbaad0 | -13.09861 | -47.91293 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| beae7d64-df7a-30a9-af8b-9ab825d56a13 | -9.0143 | -50.72679 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c4f7cd7a-302f-3c06-a4b6-2ac58fcc1720 | -11.23907 | -47.79628 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |


[Clique aqui para ver as próximas entradas](README6.md)
