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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46a641ea-18c4-3045-9ccb-7f8fc3c4de58 | -13.14554 | -47.89806 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1616edf-3eb1-3537-9a5b-8777372524c7 | -10.83475 | -41.2755 | 2025-10-03 04:12:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b8145cf5-6a59-38c1-89d8-e85d7abf8a04 | -13.20185 | -47.80138 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bd182cb-d99c-3916-98d3-b0e4bd65d349 | -12.9544 | -43.19668 | 2025-10-03 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f3ee3ccd-9372-3900-98c2-1010c6a71d70 | -9.90651 | -43.72123 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 5ea55d7d-ad73-3019-b55c-fdd2a6bece5e | -11.60044 | -47.6666 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 297e21de-f0b2-3458-b981-14088a03a43b | -14.36954 | -46.11177 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9641bd01-82a2-3457-8f28-9e3d8dae7fbb | -13.85062 | -47.92448 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5708173f-fbaf-30a1-9594-e5bf9ea35b6c | -11.47446 | -45.02703 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f81c9111-4b3e-3f1e-84f9-05350eeb6684 | -11.06082 | -47.80083 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24625fa8-9000-3af7-9e01-fad4daf03818 | -11.81954 | -51.77561 | 2025-10-03 04:12:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ef06665-6d4e-387e-9b64-2bb7e7a9e663 | -9.95124 | -48.77866 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c8a8fa5-2689-3693-8bad-c0fad39cfb0c | -9.91754 | -43.76049 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0edb8a22-37d1-3e55-ab28-0b7f22dd52bb | -13.13759 | -47.88787 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8f1be9dd-0386-37db-bf56-c8153b411836 | -9.92739 | -43.72094 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 56a6f190-b4dd-3eac-95b0-711509add6cc | -13.68129 | -48.63802 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ab9eb14-e58c-3d15-810e-3817f56f698e | -13.32707 | -47.7967 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 736a8ced-eafe-386d-ab4a-36ec7390c561 | -11.91155 | -46.74808 | 2025-10-03 04:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe1a99db-3567-3d65-ae2c-e810f83ae214 | -11.14097 | -47.19859 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ecbb9b3-5317-34c7-b3ed-2d4592111171 | -11.41456 | -43.49815 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f3dbf6d-4416-307b-bd24-9aa5e6e3d39a | -13.47929 | -47.23903 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf0ff254-9afe-33f1-a70d-a3bc873911ea | -11.11864 | -41.88177 | 2025-10-03 04:12:00 | NPP-375D | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd6ba754-6419-3097-b6e9-1ebf65596c22 | -13.21729 | -47.82878 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 995b426b-6c44-3f96-a014-75e7af6cc064 | -14.37809 | -48.47599 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c8e2c849-c0f8-3f40-96ac-38adcce1aae5 | -11.14908 | -43.38556 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0dee7cf-4e38-3485-bb14-95630771acef | -11.47228 | -45.01866 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe2f0e06-4408-3b63-b375-d15e9d41eb9a | -13.63383 | -48.67633 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b252589b-8011-3e54-9a7a-ff6d8ebacf21 | -11.72154 | -44.46654 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d2a8272-b8ae-3cde-8a3a-71350dce836d | -11.82898 | -45.0419 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 541a8218-94b1-3864-8263-6d56ee75b513 | -8.75772 | -47.33334 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| adbf4ee4-e042-3fde-b3c5-0e0f8864dbfb | -13.47749 | -47.24507 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 525fcf27-f82a-3e2b-ae34-090cb2fce473 | -10.86122 | -45.41563 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28b924af-dd57-39ab-9ab8-add35afe07ee | -9.40008 | -47.53783 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c648de5c-dfca-3317-bf41-c4bd93192fb8 | -10.79786 | -44.23912 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2d23bd5-03b2-3a81-a2db-7062a2161315 | -8.51587 | -50.03822 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9a4e5fc-39a7-3b8a-98ea-196d4abd7b15 | -13.30925 | -47.57759 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28bbb71b-f5cd-3d73-803e-7b0ac525dbf2 | -14.06606 | -45.68489 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e4b4990-fe44-396b-888a-7a3d13e020d4 | -10.96727 | -44.33566 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26bf7280-2bfd-36b8-aa81-e40fd4cac257 | -11.64731 | -46.86752 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0838377c-d159-3ce4-94d7-4d1d504e1055 | -13.32136 | -47.18799 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd095ccc-0d11-394c-8455-a9cecf775722 | -14.60128 | -46.72393 | 2025-10-03 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3e01320e-c8e8-3567-b6e4-97a432010328 | -12.91184 | -46.91648 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e415a9d-e34c-35eb-afbd-9e10443af6d2 | -11.87051 | -44.98503 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11db5f8f-761c-3322-a165-b817a6d0fac8 | -11.80729 | -45.02202 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e227831e-fca2-375d-ab45-079793f211aa | -13.20335 | -47.88486 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85774d6f-cbec-39a0-9cea-c516f4f7ca70 | -10.76824 | -45.33675 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34010e04-40e5-3373-979a-86efc8dc48ee | -14.37724 | -45.93808 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e67329b9-bc72-3454-92aa-d670045ce960 | -12.89912 | -46.90081 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d369fd3-94ed-3471-a0ac-6eb650bf11b1 | -11.81161 | -45.03891 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d9d54b9c-baec-320f-92b8-42c29f0ef541 | -13.75742 | -48.06884 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 913c6ac0-f0e3-3c00-b35d-12402493b417 | -13.13264 | -47.89269 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 77b3252e-d21f-3d9f-a992-b34f4a94c9d9 | -13.24464 | -47.34494 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfe71247-add4-35f8-b761-aefb3d032994 | -9.44506 | -50.89529 | 2025-10-03 04:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d4fa68-733c-31eb-a28b-5660d54db29d | -11.87768 | -45.00651 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1429caa7-a9ed-3c83-a1f4-996966662abe | -11.11038 | -47.84715 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33b10bae-2fdb-3274-8ee0-854894449cf6 | -9.41831 | -47.54411 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd977e7-3dcb-3fac-8296-3e11e3d659c6 | -12.9228 | -46.37678 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d800a5b4-aed9-37e6-8134-8745c8b98f24 | -13.43538 | -46.72638 | 2025-10-03 04:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 215d7196-22a4-369e-bd4a-ee6c7da3df89 | -11.11304 | -47.74039 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2b6feee-7b8e-30c7-b59c-1542165f4c5f | -13.97489 | -48.16838 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95e71d4a-adf1-3041-94c2-bc009a4ceb50 | -13.36467 | -48.0822 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dad0af97-57ce-3955-a869-e7e1a9fb27cf | -14.38006 | -45.94275 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83766280-2968-3e84-bec2-6effe696d767 | -12.62548 | -46.98278 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 984b0fbd-5467-3468-a1b7-f21dd8eee487 | -12.71632 | -48.57958 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 853c8c64-a26a-31e3-8ff1-b7d57e7a6e48 | -12.64268 | -46.99612 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0a46ed3-7660-38f8-b61f-7976ea4503e1 | -12.61359 | -46.96135 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b068f08e-a1c4-3a27-972a-d9f9ff7481b8 | -12.75972 | -44.91183 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f7abb52-40b7-3607-b837-236f9167d781 | -13.30994 | -47.59667 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 953eac05-6333-3cd6-937f-61ecdf5b7781 | -10.26861 | -50.34463 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c528395c-3147-34b7-9d09-a037aacc08bf | -13.52363 | -47.24922 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf42cfdf-394e-31bc-9878-d84272ad9dda | -13.55314 | -47.30458 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24853fda-6c4c-3794-9207-b0c460470c92 | -11.46507 | -45.03415 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b69d0da8-0531-3b6b-848f-3b69eec768a4 | -12.64646 | -46.99682 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32093523-c580-3a6e-9a60-1fb847fad6bf | -12.62759 | -46.99323 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43be3b12-00de-305d-8c3d-95ea2b58d467 | -8.72956 | -50.04613 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01fd48e1-b404-3c64-a853-4af254d70382 | -12.91624 | -46.37129 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82415005-1a9f-3d1d-9e61-7c861a0c876d | -11.55901 | -47.66282 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b41b6434-b8a5-3df1-9435-2af274a3b4c2 | -14.69598 | -45.18552 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21c7ea62-cf6c-3c63-b700-9b455cd02908 | -14.29194 | -45.88628 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df1d4a50-51da-3566-8338-da4d4ce2195c | -12.75252 | -50.55981 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96bd6bdd-e7a4-3ea9-befe-f7e3da4d136d | -10.93394 | -46.71994 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b229b39c-e8b3-3175-b697-4fd94cf3c3fd | -12.39074 | -46.52176 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae99a4f7-6f7b-320a-b021-b8265f4b4f14 | -11.09702 | -47.83389 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b39a714-c612-3547-9e95-9f9ffe909a55 | -11.29664 | -47.83341 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd02ba2f-3d84-3267-8af5-6a528966d756 | -11.2286 | -48.20135 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b04fecd2-5a4f-38c7-a148-3555635f2efc | -13.86059 | -47.93678 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 483eca8f-a17a-3b8e-98f9-858886c73022 | -11.44801 | -44.96371 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 559390f6-6010-3112-9bc5-62ce021cbf9b | -12.38184 | -46.52936 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1e8774e-0389-332d-ad62-db766400097b | -13.02167 | -43.83966 | 2025-10-03 04:12:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d14b33ca-a540-37aa-b736-601bb42b3d4e | -14.69896 | -43.88349 | 2025-10-03 04:12:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fd8f26ff-e448-3b1b-8c96-02869dfb377c | -9.95082 | -43.73246 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8cc0a0c7-2b6f-344f-aedb-d186a91c7d1d | -13.30912 | -47.25835 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9a0f5e8b-3071-3c7f-94e8-bd1fbbc0c831 | -12.8973 | -46.93332 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c87b106-d482-3d11-85a6-0986a32a925b | -13.14254 | -47.88305 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a10974d3-f001-38ff-a429-85cd3bccb55c | -11.11223 | -43.19415 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3775f6dd-92b5-369b-b9c3-501a076fb405 | -12.12444 | -43.44265 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef8c7898-245f-34f7-b2ab-4e67ab8917c0 | -9.91975 | -43.76835 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 83dea9c0-9f9e-3426-b885-2c5657dee2cb | -9.9492 | -43.65007 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25fb841d-cb3d-3ee0-a330-29a9b62ead12 | -11.21841 | -49.95322 | 2025-10-03 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f2c8d55-0316-3f63-8483-30c72fcbc464 | -13.96461 | -48.16933 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |


[Clique aqui para ver as próximas entradas](README57.md)
