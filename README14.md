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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a506967-8280-39ad-bd00-e27acaf779bc | -11.84287 | -43.79909 | 2025-07-08 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cbbe471-11a7-3b8a-ae04-eb2fe47fdda2 | -14.18971 | -45.50976 | 2025-07-08 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8d24477-f599-3661-9c02-927215ee0393 | -10.21524 | -52.15829 | 2025-07-08 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29f1ee73-4ef7-3b66-8861-2ab23408b25f | -12.03627 | -47.6629 | 2025-07-08 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51317e5f-5800-37e1-a317-1e8ae455d6d4 | -9.70353 | -56.18735 | 2025-07-08 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efef78b0-31ce-39bc-bb7c-ba4f6b86c371 | -12.58233 | -56.98613 | 2025-07-08 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62e31eb5-c015-3d46-8797-bb3ff9b79464 | -9.33949 | -58.84398 | 2025-07-08 04:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0440d76b-9796-399b-b470-20b3da89f800 | -10.64004 | -49.46889 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6429bb8-fbde-3043-b8fd-f14a885e713b | -10.26777 | -46.64786 | 2025-07-08 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 240c6c3d-86b6-3a81-82b4-76d0c2e26315 | -11.32682 | -51.44273 | 2025-07-08 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3418cf38-9376-375a-8990-a3a145fae5d5 | -11.42866 | -45.10693 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| defb9057-b930-3168-97a1-7b03c97320a0 | -11.81301 | -44.27041 | 2025-07-08 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94ccb0ec-6ed5-3487-b798-4b8086754784 | -12.02723 | -57.08034 | 2025-07-08 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 108db809-cbaa-32b8-b097-a621537944d6 | -12.98515 | -44.88977 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37256b90-d367-3e8d-b740-c9348c1f0c3a | -10.27756 | -49.55753 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 688c9ea6-9a2f-3a56-ac15-138139788aa1 | -11.44755 | -45.10476 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fefb3c2f-b82d-3361-a9a6-83be81f948c7 | -9.70176 | -56.18415 | 2025-07-08 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f045ab68-b6c2-3d0f-9d44-216fba44e1f8 | -10.82187 | -54.01696 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98571af0-39ab-396c-9d69-0a47b1faf448 | -10.48197 | -55.58313 | 2025-07-08 04:42:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db632914-f88f-35a6-bce9-862625037496 | -11.81243 | -44.27479 | 2025-07-08 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bbc36b9-7b01-31c3-bd01-eb3b4e3c72cb | -10.94784 | -49.25563 | 2025-07-08 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 682914bc-a64a-3db5-af9b-8b5bf666ea5c | -10.83146 | -54.02774 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f6ed776-d1ce-3d1f-b08a-b808d6e4db9f | -12.23602 | -44.10157 | 2025-07-08 04:42:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d563e5a2-9470-36d4-9b69-4b27b39eec4b | -10.36389 | -48.72198 | 2025-07-08 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79cc78b5-d379-3125-9b2b-214ccd85c9d6 | -11.42812 | -45.11073 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| a0f2ee04-38af-3a85-a53e-aaa1c5849525 | -11.32348 | -51.44217 | 2025-07-08 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59dcdf12-ee43-3d6f-b566-391e989486f5 | -12.58157 | -56.99027 | 2025-07-08 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5083645b-da35-3923-ab57-a519ea6a2b91 | -10.63274 | -49.44946 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d6b6fecc-b564-35d9-89ac-055b93579c74 | -11.43589 | -45.11571 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 925cea84-480d-3608-adae-29169688b03b | -13.4052 | -47.88691 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4558927d-dd7e-3645-95bb-0301096f8a2c | -10.17453 | -51.65679 | 2025-07-08 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76bfc2d2-d5bd-3744-88fb-f8a3973c802e | -12.33319 | -49.31982 | 2025-07-08 04:42:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03cf36d3-e352-3637-b103-2f95ffd159a5 | -9.2223 | -48.59348 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 997da8f0-92fe-3f03-b31c-82c33648f384 | -10.23093 | -56.76806 | 2025-07-08 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9874b5a3-907f-3729-a16b-c69708a9e5a4 | -13.4065 | -47.8781 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e75669e-698c-3b39-9505-e8e42f2b3b5d | -10.8178 | -49.49636 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7142dc3f-438c-38c8-824c-d54dc6d804a8 | -10.83146 | -54.01632 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e609ddf1-6195-3e6c-930a-1c5a967f6e84 | -11.42919 | -45.10314 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 130a2304-dbd8-32ca-9047-d19f3b2e8ebe | -10.82629 | -49.55254 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ec51b64-a266-3a87-8c83-2d6983d76f17 | -10.35007 | -49.92013 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1d79421-6a24-38d1-8ad0-65e797df33fd | -14.37116 | -46.83274 | 2025-07-08 04:42:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce74b184-689f-3576-b713-7e5dfeadc4e1 | -13.6489 | -46.81283 | 2025-07-08 04:42:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7f0d2ff-9c8f-3a8b-bced-e4f58c81cc4a | -10.41867 | -49.76505 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1255788-e6d4-3445-a4ea-5c54e3a6e79f | -10.98067 | -45.11684 | 2025-07-08 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8dab2ecf-6cf4-3a62-a767-19bda875cf3b | -11.35152 | -55.40412 | 2025-07-08 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d46b341d-7e38-3c61-9d9e-d465035400dd | -8.9838 | -49.18446 | 2025-07-08 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 544fa427-421a-342b-b018-fc56acb9d924 | -9.22285 | -48.58985 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 01d8e304-422a-367f-bc0d-56309b2b3242 | -10.64449 | -49.46229 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 02dbca45-290a-3317-96f4-6b37b92c724e | -10.58118 | -49.12523 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a80ff54-190a-3708-ae06-653d4169b90b | -10.63102 | -46.37624 | 2025-07-08 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd6d2355-39ee-3f13-b987-1c573283b47f | -14.04997 | -46.24867 | 2025-07-08 04:42:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a4ed25f-ffed-3ae8-81ff-cb75307ee21a | -10.8226 | -54.01255 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eefdac3f-3676-315f-9463-e4697505fc49 | -11.32568 | -51.44986 | 2025-07-08 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9dbb2242-fea5-3abb-9811-65dbb0f13a86 | -12.94235 | -46.53724 | 2025-07-08 04:42:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14fde194-417f-3e65-bffa-fa4cdcd314f5 | -10.82925 | -54.01822 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b3b08de-3523-3e70-ace7-6507ddf20eba | -10.34674 | -49.9196 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcb3c57c-b0b0-31cc-8082-8b5fa01c2dcc | -10.41811 | -49.76857 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2b30341-654f-3ed7-8369-b954743e4971 | -10.96526 | -48.20473 | 2025-07-08 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a73233c3-d581-3412-b793-2fcf0109ac23 | -10.64283 | -49.47299 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1dd86e9b-1956-398e-bc70-c06c06944ea5 | -7.72339 | -55.14016 | 2025-07-08 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2793c63-4edf-3781-b62d-ad4db834828c | -10.21585 | -52.15456 | 2025-07-08 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9a355f55-678d-333a-9fa2-3f10fa813e8c | -9.00752 | -48.72015 | 2025-07-08 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1c8941a-65f5-36c5-8f73-a2a1131a88b5 | -12.98624 | -44.88142 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56102f66-9b7b-3ea7-8ab2-93a896f74b63 | -10.63948 | -49.47246 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1942b73f-c7cf-30e5-bcbb-525462502abb | -12.98796 | -44.88667 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 891937a3-e8fe-33eb-aa38-cc901c77f5a3 | -12.02668 | -57.08569 | 2025-07-08 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 797a0b49-bcf1-3be4-afb8-8a156c74ada5 | -13.40821 | -47.89161 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8b347729-b3ca-37a9-8809-3a29d0f21dc0 | -9.34004 | -58.84578 | 2025-07-08 04:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7b93fcc-4cd2-3b2a-87d8-ae8b9f80b29b | -12.02644 | -57.08463 | 2025-07-08 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dd32ba2-7e06-36a5-9850-fc3109902da3 | -10.82629 | -54.01318 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8932dbc-69b0-3322-b000-13cdef9d7d93 | -9.37445 | -48.95738 | 2025-07-08 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05442ba0-ac57-37b1-b4f9-973ad20d2331 | -11.46896 | -47.91893 | 2025-07-08 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7aeb001-7e61-375d-89bd-a97c0ae17512 | -8.86705 | -47.27137 | 2025-07-08 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 540b9ae4-60a8-32c1-b3b1-ddde1aab2edb | -8.7129 | -50.00297 | 2025-07-08 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 254d138b-e759-3d46-96f0-4d5711867100 | -9.21836 | -48.59659 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0af1d640-ccb6-38f9-924f-d88b5885802a | -11.34756 | -55.4034 | 2025-07-08 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 435db551-f289-3085-9d8f-25037dc8847c | -10.39463 | -52.17171 | 2025-07-08 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13e4b397-5ff6-3e13-a862-bd30d15f7cc2 | -11.43804 | -45.10051 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c33749c1-2363-3324-9910-1c5c5637173e | -11.83892 | -43.79206 | 2025-07-08 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bec2615-4240-312a-9c1a-762dd2ed7b3e | -13.41182 | -47.89215 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5f6c9037-bafb-342a-b6bc-dc7d95309ec3 | -10.64394 | -49.46586 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c7b0852-8fc1-3008-947b-f38339480eb5 | -13.01091 | -46.75831 | 2025-07-08 04:42:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89c40f3d-16c2-3156-8638-6ea4d51e31a0 | -9.33893 | -58.84708 | 2025-07-08 04:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b780533e-816c-3949-a24a-a8a4eb95c3aa | -8.95889 | -47.28056 | 2025-07-08 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a58dd909-b8f9-3b69-a33d-b886fe98654e | -11.42557 | -45.09875 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd692099-7479-37f7-b253-c3ac8dbe21df | -11.84741 | -43.79808 | 2025-07-08 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70fdc98e-800f-327c-b638-6b6ab3c06fe8 | -12.99 | -44.88624 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ab7f2d1-39a8-37c2-95db-a36bf8d4d278 | -10.62884 | -49.45249 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7f1dc1ed-7bb8-35ed-aa61-b35fdee87376 | -9.22624 | -48.59037 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 10274f68-9305-3bd1-92b9-51e93d988904 | -10.57781 | -49.12469 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| bb486d0b-c789-3004-8d40-de3581a7c271 | -10.36048 | -48.72147 | 2025-07-08 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6864c767-c354-3c53-96d2-5cfb4d32789e | -11.83828 | -43.79675 | 2025-07-08 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c18a3b00-58ae-3fb2-aac3-84bd81bee9e0 | -11.41981 | -45.10952 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41266e41-9516-3304-ab63-b525baeefac6 | -11.29816 | -45.27222 | 2025-07-08 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b09c6944-1960-3683-b0c4-ff362dc50a44 | -7.9116 | -55.40131 | 2025-07-08 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 072706b6-ac4d-3faf-b319-043af68c453f | -13.00962 | -46.76744 | 2025-07-08 04:42:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c3f2025-1688-3ab6-94e6-a7f6eca01efa | -10.41478 | -49.76805 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc1ba80a-ba77-3915-a6f4-c1b18ab24170 | -10.26911 | -46.64574 | 2025-07-08 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a016118-bfe7-387d-a0a9-4d6c3fac50b5 | -11.96714 | -49.56971 | 2025-07-08 04:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d1df9ee-ec84-3e57-803f-83474a58123c | -10.95177 | -49.25254 | 2025-07-08 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README15.md)
