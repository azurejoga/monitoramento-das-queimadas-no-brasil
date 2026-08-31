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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f975c95f-5037-36fe-8964-784d2f0952c2 | -16.69021 | -49.89782 | 2026-08-31 16:48:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2ddc4d24-528e-30c0-a4a3-f986720d0a1a | -19.21005 | -57.34257 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| a997087b-a637-364d-91a4-685815973945 | -19.21127 | -57.35614 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| c61fc007-409c-349c-8ded-985a315bf7ce | -19.13776 | -57.37894 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.6 |
| e1e389cc-6dfe-358c-9d6e-e77c270b9fdd | -15.65 | -40.95788 | 2026-08-31 16:48:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 31832c80-b17e-3db6-99fa-1551272018e1 | -18.00781 | -43.48029 | 2026-08-31 16:48:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36b44d15-07a4-38c9-9608-2baab262674c | -15.65253 | -56.37414 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 458b1df6-0aeb-3a32-b2ed-0a6b4c81f76e | -17.86016 | -52.08913 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 145.3 |
| eb943352-e5b7-3924-ab41-fdfb59c1332c | -16.98456 | -51.84076 | 2026-08-31 16:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dd593675-47e7-35ac-ae5d-125242e90dde | -16.57745 | -52.51525 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cae9404a-2238-370b-a032-16b0f9c315bf | -17.53807 | -41.31622 | 2026-08-31 16:48:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 54fef9b6-6c1e-3f81-aeeb-fcdde5c95f69 | -19.12156 | -57.39896 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.9 |
| 593fb145-93ec-3c38-8d49-4416d7be0e6e | -17.85507 | -50.50364 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a6801e01-ceeb-3ac8-a6ee-0da68199dc35 | -15.02066 | -48.18086 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 9e82697f-647e-3638-812b-50331db24bb3 | -14.21871 | -48.64822 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6929a5bc-5a52-3ff6-8923-948e11ecd876 | -17.8652 | -44.25077 | 2026-08-31 16:48:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0dea8caa-3f14-3af8-9607-4eb38636ee15 | -16.69381 | -49.89732 | 2026-08-31 16:48:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 41d096d2-ef38-342a-b8b3-21fde6563089 | -15.67709 | -45.9475 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |
| dc4472e6-ff6a-305b-80cf-d01b629e5421 | -19.08895 | -57.40498 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 04b0603b-246b-3e66-bde4-720b89cac295 | -17.18223 | -54.29391 | 2026-08-31 16:48:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fbe145e-73d4-33b3-8870-1c73e00bbf5d | -15.23937 | -56.38803 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 70909bc8-4f6b-3e8e-9a3b-3aa8d7549ec3 | -19.14076 | -57.3814 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.7 |
| 9dff153e-c724-3664-96cc-6888cfd8718b | -14.21535 | -48.64875 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b0c91fa4-4b96-30c4-a065-a62e7e4e6d70 | -19.13306 | -57.39317 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 68d06f26-aef6-36d1-a2af-2607c68fb5f0 | -18.91298 | -50.87716 | 2026-08-31 16:48:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| fd303f7f-a616-3f89-adf3-dbdcf38515fb | -15.67375 | -45.94807 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8a7871b5-f0c4-3822-a3a3-55b1b442d072 | -19.15604 | -57.38163 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 96d1847d-5350-3505-96f2-f1d70d7a5b8c | -14.58103 | -54.0843 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d3d55aa-7341-37c9-97e2-70eeee06e802 | -13.55142 | -48.23593 | 2026-08-31 16:48:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0dabe680-212f-3054-a256-6401a5a454e1 | -19.11909 | -57.37172 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.9 |
| 906b1ef6-57e8-34be-abe8-41c83636bb5d | -14.97793 | -48.13937 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| cefebce1-78d0-35cc-8117-185119052711 | -19.7488 | -47.89304 | 2026-08-31 16:48:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e8924ef-6366-3680-8ad4-e113d7c0936b | -15.45609 | -53.96316 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8eec4e50-3e63-3fea-ae0f-da9d9dc4b358 | -18.83418 | -46.77342 | 2026-08-31 16:48:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f4d78ff1-e3f2-325f-b843-084aee775577 | -13.66339 | -48.89652 | 2026-08-31 16:48:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7649a15c-7326-336b-8453-5c8902d2f5a3 | -19.11437 | -57.38589 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 906cd630-e188-30af-9309-675c09422c9e | -18.2166 | -43.9715 | 2026-08-31 16:48:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a83f97b1-b35c-3774-8882-85d293052268 | -19.42147 | -46.89333 | 2026-08-31 16:48:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b4798970-cf96-3673-a974-17851e9606d4 | -15.93741 | -48.07471 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 32b46011-90ed-3252-b13f-9423e8556dbd | -13.61195 | -40.65025 | 2026-08-31 16:48:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 058cfaeb-b016-3106-a915-bf6e0125ac05 | -16.39962 | -40.91755 | 2026-08-31 16:48:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 5fec32a7-ac01-3d92-b34b-505bc179dae7 | -17.3681 | -44.87863 | 2026-08-31 16:48:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8aa81c4f-95cd-3d71-a6fe-d5b6416a1ae9 | -19.22829 | -57.34523 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 64168730-c57a-3ee2-b151-b31e911d4418 | -15.22497 | -56.35568 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e1068222-c7ef-3a6d-a2b9-a07c6ff93ebe | -19.15857 | -57.40889 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 96409d79-743e-3e85-8e23-efd2ac69fb9b | -15.8296 | -42.61302 | 2026-08-31 16:48:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| e5b53d81-7688-39f6-9ee2-5bb9d62b391c | -19.1807 | -57.38825 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 5503e58f-90a3-3e61-885a-e37edde4f6b8 | -14.82891 | -55.72753 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c8eda1be-647a-3750-9063-79f7b2c89e00 | -19.2287 | -57.34976 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| b9460441-165f-3f3e-8451-243a1f6da75c | -15.78504 | -47.80187 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 7de553ad-e672-3b44-b77a-97cc83e68e84 | -13.54917 | -48.24359 | 2026-08-31 16:48:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c98ad501-8542-3b60-894b-a6e7db403fe6 | -19.11189 | -57.39343 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| b7f53017-85d9-3354-a816-92941c83c8d7 | -19.55408 | -48.27295 | 2026-08-31 16:48:00 | NOAA-20 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 306ca133-6e73-39e6-8e0d-ad30262e7de1 | -16.56859 | -52.5123 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 517fb48e-da01-37fb-a19d-fc99f6f959be | -17.8458 | -48.75072 | 2026-08-31 16:48:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 67855407-7945-344b-a265-e4616a587bf8 | -14.45395 | -53.16335 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fa9366c0-e386-302a-8bd9-0458d5590592 | -19.19002 | -57.35983 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 06bd2ef8-397a-3281-9263-6210b5a3e7df | -19.46916 | -46.8742 | 2026-08-31 16:48:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9bb50722-e91c-3efb-b7fa-23ddfc555d8f | -18.2683 | -52.75103 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 78310198-2d90-34af-aed7-9945920eb448 | -19.12073 | -57.38982 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 6830a488-3438-376f-9cd3-c216a60fe369 | -16.44092 | -51.40532 | 2026-08-31 16:48:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9be8c9ad-7bde-303c-9c7c-278dfb4d25bf | -17.85651 | -52.09356 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77e562e5-87b6-300f-b8ec-c035f0481df3 | -16.86727 | -48.28105 | 2026-08-31 16:48:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0541a374-e74b-39f6-9b38-0a28ea3e4436 | -14.95116 | -54.58508 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3ca91ff2-522d-39d4-89be-48c4d2f57452 | -15.6246 | -56.41643 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f5923323-0706-3b10-99dd-117c2a9d0f91 | -19.13615 | -57.3956 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e016a689-86ff-3627-8e03-6fcb3b8f5b5e | -15.19253 | -48.97765 | 2026-08-31 16:48:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 34e3d43d-1df9-3a74-8230-bb2ff168e82e | -18.72139 | -44.5057 | 2026-08-31 16:48:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46fba963-18eb-302f-84b7-fabf7bb4ab93 | -15.62497 | -56.41983 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7508d326-5104-3ebb-a081-772a4da4ddbd | -17.87625 | -52.0832 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 6cff9037-022b-3d0f-b4f1-c9afb8dc006c | -15.41186 | -52.71488 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| ebac34a2-23b1-3cd7-8d91-c7e21d3f9d1d | -19.09824 | -57.37655 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| aca3c307-5986-3998-83b1-41dd070ed317 | -18.27446 | -52.69322 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 4213714d-4e30-38cc-a3ac-5d05c7b524b6 | -19.11785 | -57.39283 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 0ff322a8-fd1e-384c-a6f7-ff7c150729e8 | -15.65825 | -56.37688 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2985b82c-cdaf-3024-b479-04624b58ce24 | -14.99296 | -48.15524 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bacfc253-9a7f-35bd-9e9b-bcb63661fb54 | -19.12886 | -57.38256 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 906d6f62-306a-32a1-b51e-11e584fc30ac | -18.29598 | -45.02565 | 2026-08-31 16:48:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dca67bb-ae89-3c05-ad50-633238542e2d | -19.15008 | -57.38224 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 3f223f41-744e-3ac7-a64c-15a598662f80 | -19.11696 | -57.38375 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |
| 8b10f7e8-46db-379f-afa8-659186199a57 | -15.40481 | -52.70438 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d66425f1-11e6-373a-9ade-92f60abd8bec | -17.87872 | -52.10265 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 9792b900-8682-3c82-bbb9-66764269e0c9 | -15.64795 | -56.38181 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f87d3d59-881c-303c-884d-c625d1b159ad | -18.10436 | -43.75087 | 2026-08-31 16:48:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d042018-a944-3df2-92f6-e6bd2fd1a58c | -19.22317 | -57.35491 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 70d19d01-a884-3e11-9990-fa7c2c13a4ee | -13.66676 | -48.896 | 2026-08-31 16:48:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb8724cf-fbdb-3722-b591-ac18e6cf29dd | -15.65291 | -56.37761 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7fc3dc26-a16b-3bfe-8d63-44b05e67ea3c | -15.7817 | -47.80238 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e61e511b-4be8-3b99-b406-a43d5a5050f7 | -15.6844 | -41.07609 | 2026-08-31 16:48:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 4a7b2cc8-e9f3-364d-bf76-b615947689a2 | -15.64808 | -50.09745 | 2026-08-31 16:48:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5fd9815-6860-375a-a552-47d37c49bea7 | -19.14882 | -57.36865 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 99bdbaed-7d13-3892-a981-627a01bb145b | -19.21599 | -57.34196 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 9f439513-f070-3ffc-a624-77193587b011 | -14.23269 | -51.94332 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| cba1bb8e-5972-34d3-99e6-5b5099b80d5f | -15.97311 | -55.95545 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 3d793706-38eb-3a82-a16c-7a973d5749a5 | -16.15391 | -46.6775 | 2026-08-31 16:48:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57fe7078-7653-3a09-87c0-fdb196cf690e | -17.88287 | -52.10218 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 6a00d66e-9920-3946-909f-5862b79d7c65 | -15.2261 | -56.36573 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 169028d9-41c2-370b-a811-4b9a9973d717 | -17.86699 | -50.50674 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 255.2 |
| ed087ba7-3e43-3673-a56f-5df5cc9f847f | -19.15754 | -45.49719 | 2026-08-31 16:48:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa3076f3-73ef-3979-9b68-824d680d0253 | -15.39548 | -52.68542 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README147.md)
