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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2592441a-4db9-39f9-ab27-8a36180c8692 | -12.68466 | -48.55685 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae881b3d-da6a-379f-a1aa-8ec27981915f | -12.95044 | -46.37146 | 2025-10-02 04:51:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f7ec7a44-2fef-3209-9570-88a2ccf49f0a | -12.86687 | -47.01434 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1524dab5-759d-3330-a4fa-6cf17814bae8 | -15.93036 | -43.34246 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 74d6722a-44d5-3ded-86ea-2e888a683cba | -10.22361 | -50.32135 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f1dc7c0-dbbc-3a6e-b90e-d8870748a14b | -13.17402 | -47.80698 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48d7e917-9154-3ee8-9479-d179d900c532 | -14.89009 | -48.33608 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4232214a-8ae2-390c-9c80-8f38e2b7a9a1 | -10.19796 | -50.27071 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 280c3869-bb03-3c94-b9c5-58288437bf31 | -11.46574 | -51.51418 | 2025-10-02 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aea10893-c797-3964-95d9-5bf1a64c3680 | -12.6657 | -48.5728 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c85d9028-8eb6-3d77-9c69-5b2c14b1ed21 | -15.70001 | -46.25435 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 127a3bed-b9ab-3644-9ef4-493f7bdc365b | -13.75365 | -48.71149 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fce0de29-5e24-3054-b38b-a4280b4a488b | -12.89157 | -46.93298 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea8d0443-eefe-311c-aa76-879fb687be6c | -9.40546 | -63.69254 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 037ab34f-9d34-39d2-9da9-5a500e30dbc8 | -15.00899 | -55.27322 | 2025-10-02 04:51:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6e2ae25-d76f-3a48-ab38-8dcd20377c77 | -14.47559 | -48.43755 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0a6316fd-6e97-380e-9195-e0e57bc2a7be | -11.34699 | -44.978 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30c31217-a1cc-3985-9f0d-544725392c8d | -15.31461 | -46.28722 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6b46c180-d758-3eaa-9365-56a2b70b9d87 | -13.64217 | -47.18957 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59ed9ae2-261f-34ec-880f-19619c193499 | -13.29828 | -47.21021 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa37273f-c490-3aad-9b86-bfd7c8e62d4a | -12.46086 | -54.319 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c241b429-312b-3661-9a2c-cdb79869de82 | -14.87404 | -48.29216 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53a309e2-86cb-3950-b95f-7aa8bcbafc5f | -12.70888 | -48.58536 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 490cf12f-fac5-36e6-9d6e-69c507d67a6f | -11.26574 | -47.81933 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db7bdfd5-0568-3d6e-ad3f-c7bf064cefc5 | -10.34662 | -43.73634 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f265cae9-c880-3c17-91e9-84657e13d7cc | -11.84406 | -45.02558 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e909891-d0cb-37ca-9678-38b5e5e21601 | -14.86397 | -48.30201 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e73450f-040a-3437-a3b6-bc451f82f1f0 | -14.32108 | -45.96537 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad76f4ca-eff7-3c0b-bed4-e844c680e028 | -15.94344 | -43.33472 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef981e38-c2e8-30bc-97d8-82a36dbbe1cf | -10.26434 | -50.31899 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2bc580d6-7a59-3290-b850-f27a89064d42 | -15.23371 | -48.72574 | 2025-10-02 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fdd8d124-e6e9-3518-8461-aa666750e5d9 | -13.69112 | -48.64428 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96405f5d-a7af-3954-bc31-7c81c133960e | -13.31077 | -47.5834 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 986d74f1-ceb8-3241-83b5-0726de17298d | -11.77538 | -46.83379 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 243c1108-9d33-3698-b1b4-68c61dc089c7 | -13.79598 | -48.04825 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e53dfe4-f880-3551-b00e-e4b9d1ca5360 | -14.417 | -46.13204 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3135aed3-ee86-3581-b3b8-fcf9f81d1410 | -11.86813 | -48.07531 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9568c867-e920-32e1-9833-0f3aa0956e66 | -14.68306 | -48.11084 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18772ede-f954-3ae2-8f4d-c417d58f70a7 | -11.81957 | -45.01187 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc35095a-aece-368f-ad00-3dcdd6616ed0 | -14.6922 | -48.25573 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61c9b1e3-06bf-39d0-86a8-88f206588773 | -15.50619 | -45.90693 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01b73a32-8c94-3c45-8a4c-ebabce0eba12 | -9.91436 | -47.70603 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43fb8090-de7e-3465-96a9-1db44e81bf67 | -16.36858 | -47.05205 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59b852e2-07fb-39bc-a040-fab88a010fdc | -14.37113 | -45.97086 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74d4eeb8-9b3f-3c0e-8d4f-674013d46213 | -12.8125 | -47.03967 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 261e3f4f-8730-33f5-a211-694a3294838c | -12.64128 | -46.95573 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cc72f4f-d33a-33b4-aee1-9307dfcc8010 | -9.94097 | -43.70608 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58be9ecd-4008-33bf-ac07-f3ae5f8539a7 | -15.23655 | -50.11946 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 93a36d6c-f592-35aa-9ed7-8fb1e17def69 | -9.92729 | -43.72597 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e879d514-4a31-30bd-8186-8d4763a4894f | -15.29176 | -46.39308 | 2025-10-02 04:51:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef94c258-216d-39d1-bd26-3061b49a1445 | -12.85534 | -47.03145 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0f38234-b9fb-3cc7-8831-71f574260f04 | -15.26307 | -49.30964 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7f8b715-9969-337e-b396-e1f48b069825 | -11.1991 | -47.77143 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 13a86abf-4b61-3021-9460-8ae314bd3fa9 | -11.87165 | -49.91087 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2fa27b2-0e5c-37ec-ae24-2e9148aa71df | -11.43693 | -43.5013 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| badc1472-996c-3d05-af7a-82081f8af636 | -15.39633 | -49.18284 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a4b5c2e-a212-3e82-9774-a40e78ad66fc | -13.52453 | -47.26292 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acd5d81f-95cf-3e79-a3a5-216a10eacd64 | -10.93731 | -46.67517 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83096fee-7b07-3e05-8b2b-9d6c8f608eea | -11.91124 | -47.88797 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6893df28-1260-3b38-87ab-3393743d2b13 | -13.75681 | -48.01126 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d699a50-b998-3938-aa5d-9b76d1405613 | -13.85496 | -51.25157 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a65784a2-2701-326e-acbb-4e5af3228cb8 | -11.82163 | -47.59658 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a33c1cf5-9c65-3c37-98b6-e988d1f4cad9 | -12.81336 | -47.02753 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f99159a-56aa-322a-a90f-c37540a75f7e | -13.3069 | -47.00372 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a5ee0bd-e866-3f17-9fbd-b76989db33a6 | -9.93288 | -43.76968 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9541a2f8-2b50-3558-bbe9-7317b710398b | -15.34724 | -46.26802 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38ec6abd-c007-30ff-b6c4-c69cac3fdec2 | -11.12287 | -47.72877 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33ffc536-4fb0-3409-a574-6d841770c677 | -10.29225 | -47.9319 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65560feb-9fbe-357e-8d1d-a4516b2a5eda | -11.35726 | -44.93977 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 855c3643-cd84-3b18-a371-ec27915e2333 | -15.02562 | -55.27608 | 2025-10-02 04:51:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28f7f549-31b0-391b-84a7-e36352fb841f | -13.40518 | -47.78544 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9f03b44-f7a8-3a8b-abd8-221aac32566f | -16.13758 | -46.6745 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19a188b1-97bb-3dbc-8ad6-037fbe2f883e | -14.89752 | -48.33033 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d5171dd-5627-3b4e-9d47-6edd692a69b5 | -12.4182 | -54.35186 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45391e45-6bd3-39fa-915e-19bd23cb1c02 | -10.6868 | -48.57648 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 382fb402-20d4-3613-9799-776ec050f772 | -13.5319 | -47.27683 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32c1dcff-7b0c-3147-ae4c-dfad2409da2a | -11.82675 | -44.99655 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ece8bf15-53b5-3f1f-a774-d32fba851997 | -13.53511 | -47.25296 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d0211bc-f78b-3141-84c5-04beac34f145 | -15.99923 | -50.90471 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 838e2a98-1eba-3820-b55e-7660146e8a12 | -13.15188 | -47.84085 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 446de022-7730-33fd-a1aa-170b97223901 | -11.84139 | -44.96401 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9275e89e-1f91-363b-958f-28063ccdbcf9 | -14.67928 | -49.60935 | 2025-10-02 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 574be8e6-d1db-3d3b-9771-d09b3ede7a88 | -11.83778 | -44.95093 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6f08b4e-d0a2-3708-b61f-0bb9fe9d6a15 | -10.24638 | -50.31629 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1f0a411c-df90-3619-9e26-cc2831bad33b | -15.22312 | -50.10259 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e442db3-5252-35dd-bd14-baaaedecd586 | -11.51453 | -43.54573 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a66bf5d-13fc-38cd-9aff-774306ebc8e1 | -12.69793 | -48.58168 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4ecf011-95f8-3008-98a5-843b6c9f4b91 | -9.93961 | -43.71678 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6721dfd3-f4f5-32b7-b99a-8f5d6eda1ef0 | -15.15663 | -48.3947 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a44ef3ed-50bc-3d87-bf36-a1d5a9a9ac54 | -12.83406 | -46.8707 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d515ef08-a2c6-3b4c-b491-ee9ddb46be8d | -9.94649 | -43.66261 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 236aa888-6ad0-3101-affb-607472db3ac0 | -14.42298 | -46.1345 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c0efd2e-cad4-3301-8dda-5c56b2e4e45c | -12.76263 | -46.88267 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad3e7a15-dfd9-3ff1-981b-d41e654af28c | -11.00858 | -46.59446 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 908f9fe2-c50f-3907-8745-c40418d3cc7e | -11.26581 | -47.66202 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69c4badb-6a12-3948-b90c-929681501ab6 | -9.93278 | -43.72665 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 85af7a92-bf8f-3f10-9fa2-ec8e98d03f39 | -14.34712 | -43.84785 | 2025-10-02 04:51:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d30d0fe1-fecd-342c-aa2f-b8e5c7a553a9 | -13.75641 | -47.94568 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 849a7749-a789-3988-aba4-9a5b1cadbc04 | -13.2426 | -48.51007 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dbc48d1-5b9c-3c07-b4fb-9ffc686e2966 | -13.06074 | -49.1731 | 2025-10-02 04:51:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README128.md)
