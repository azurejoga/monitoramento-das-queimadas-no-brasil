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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3730b117-bc8b-3e0b-81a6-7f2cb70eaa8a | -12.71649 | -47.79485 | 2025-08-10 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69954703-48d9-3375-badc-bcfbb7057ac4 | -13.63755 | -48.98455 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51572fea-a98e-3fab-b3c2-9507ddba336d | -12.55191 | -47.0873 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6fcb226f-96cb-3041-817d-ef5293931ecb | -16.37875 | -42.53695 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| de72c572-5ace-3d83-9488-e6c36e33c544 | -14.71593 | -47.51883 | 2025-08-10 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebe1a34e-42d0-3a94-8b39-74b97065d963 | -11.09692 | -50.46087 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6964d8fa-d7a2-3ee2-ae55-3aa160bf65df | -14.4546 | -47.85485 | 2025-08-10 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34d2b6b0-2837-3963-9d1e-21ca8f648f01 | -14.28046 | -51.96159 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbba4de1-c3a7-3f75-a97a-cfb89e820c8b | -14.12046 | -42.13981 | 2025-08-10 04:23:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1867f19b-03c7-372a-9b8e-122c4eeeeece | -14.29077 | -51.97547 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dd6c83d-f3bd-3687-a943-e8401717c001 | -14.29696 | -51.98858 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b65dffaf-de3e-33d7-8dbc-e609180def8e | -16.38259 | -42.53758 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd5bbf4c-f506-3264-a5e4-b8c14e3f35bb | -16.05341 | -45.02654 | 2025-08-10 04:23:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c091b5c7-6e69-3304-b9ba-b308b5681f4a | -13.60441 | -46.93677 | 2025-08-10 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1ed281f-ea5d-3aa3-b0dd-a75802f5235c | -14.74438 | -45.15818 | 2025-08-10 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cb025b5-b157-3f67-ad24-df41b7f70e84 | -14.59481 | -47.16125 | 2025-08-10 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47bc64fc-e91d-3061-b684-3fb8e474a6f8 | -14.28459 | -51.96238 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49a11e82-bd39-38de-93cc-f4462593ba93 | -14.79951 | -40.66668 | 2025-08-10 04:23:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 42cf51ad-6687-3ec2-a4d9-ff7ba6c6243f | -14.10007 | -46.56889 | 2025-08-10 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3db25aba-25a9-385a-aec4-b80c8fbb8c42 | -16.07948 | -43.62949 | 2025-08-10 04:23:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5fa3965-7b36-38dd-aa0b-82498be698f8 | -14.39715 | -43.7847 | 2025-08-10 04:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e392603-57d1-3ac8-8e4a-67658aabb9c2 | -11.65658 | -48.32063 | 2025-08-10 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 920a2cf8-e761-324f-820b-2c2d1ca4c6ab | -16.30651 | -52.9253 | 2025-08-10 04:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d76c35de-fd1d-38f4-a7e0-cf5f785ca660 | -13.63402 | -48.9839 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f901bbca-ab51-334b-a497-4c79c59b4a57 | -14.74383 | -45.16187 | 2025-08-10 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eab2df0e-d6b5-37b5-975d-e13280f258e9 | -14.46593 | -47.84931 | 2025-08-10 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 250776ce-d40a-3a6f-94db-803a238d420d | -12.16671 | -50.22071 | 2025-08-10 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c938d282-7e7d-38d5-9449-7cb18dba2e7e | -12.02179 | -47.51078 | 2025-08-10 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f1dc8c8-3de5-3185-8d32-46aec13d3e12 | -14.03515 | -46.33945 | 2025-08-10 04:23:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b3ef927-5cdc-3436-9105-c477fc745be5 | -12.57922 | -41.28465 | 2025-08-10 04:23:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f7a7bfb-a4ce-39ca-9069-10bb6043bb53 | -18.31296 | -43.96099 | 2025-08-10 04:23:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f24bf1d7-5632-35f0-813b-1f4708924c28 | -16.05682 | -45.02709 | 2025-08-10 04:23:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9959e363-5035-3af4-abbd-595e0e83ac35 | -14.28733 | -51.97085 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 190e329b-7b92-3c24-aa31-cdffb2693b3d | -12.6429 | -44.5088 | 2025-08-10 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a3a7836-1dd1-36cd-bf02-c71637d545ee | -13.64457 | -48.98616 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c32dad6-4962-32c0-ac04-3c8b6d0e8831 | -12.57833 | -47.14725 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26257193-30f4-36d7-b2b4-ccdf1716a93d | -14.74101 | -45.15763 | 2025-08-10 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36c6c81b-845c-38bb-b55e-fb03cb1b99af | -12.52963 | -45.67318 | 2025-08-10 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a6b1caf-6445-3047-8eae-9fcd85375920 | -17.51458 | -41.73729 | 2025-08-10 04:23:00 | NPP-375D | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a6c81355-f6c9-34f9-9827-09bffc87a17f | -12.55249 | -47.08367 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f5997340-6c86-376e-97dc-26a4b5acc0ec | -16.37282 | -42.55142 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df5c42bc-b954-30b1-8ec4-2c3f2fa6578c | -14.10742 | -45.39886 | 2025-08-10 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a64a3c00-c5b2-3506-b87f-35be8e8b332e | -12.5324 | -45.67725 | 2025-08-10 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e17ecf26-dcda-39d3-9bb5-e3266a229284 | -14.71869 | -47.52304 | 2025-08-10 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db8a7c29-0489-3341-be9a-7c56ea523324 | -12.60144 | -47.13252 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 514a21a9-98d8-3dd2-81c1-8c02163d1739 | -11.43207 | -50.59146 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ac9e609-64bb-3e37-8eed-5895400cda41 | -11.38099 | -50.55541 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 077e0857-373b-3b08-aa2b-2b1e2c843e5b | -12.57774 | -47.15088 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b12e4e01-faa3-3165-9c90-7adf523e2f8b | -16.07586 | -43.62894 | 2025-08-10 04:23:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3e215ce-0bd7-3e0d-a203-b75745b9ea5b | -14.29562 | -51.97239 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fd3969e-3b4d-35fb-a5f2-3486177cc7d6 | -14.39763 | -43.78209 | 2025-08-10 04:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b88ce9b8-9b65-3899-8f09-28016b142f62 | -14.58929 | -47.15293 | 2025-08-10 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70310f32-3545-3265-a4b6-250543d843e5 | -11.76409 | -47.48355 | 2025-08-10 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0db38cac-a5a2-3519-a1b9-1b5083fb8fbf | -16.37352 | -42.54639 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 52bf964e-4838-3665-8104-20e3123b094f | -13.44692 | -47.19888 | 2025-08-10 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 032f904c-7a34-3f50-b33a-69c58da978a3 | -11.08393 | -50.51196 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e8ce7bc-5ce9-36fc-ac11-fb093222d0ab | -13.63112 | -48.97949 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 378b3f36-e764-34ec-a590-fbaec63c4dde | -14.03957 | -44.74893 | 2025-08-10 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74b11251-6d4e-33f3-82a3-a6895f442678 | -14.09229 | -46.5749 | 2025-08-10 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 374f05a5-419e-322a-aef1-f8df1dc2df5b | -12.71189 | -46.36204 | 2025-08-10 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9901fc0-eb81-3a86-b339-5f36c6bb42a9 | -12.57204 | -41.27842 | 2025-08-10 04:23:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4058c060-2674-3676-8e48-6243f7025a99 | -17.56828 | -47.50859 | 2025-08-10 04:23:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cb0bed1-6eab-34b3-a7d2-3a7b5ce5b90f | -14.60148 | -47.16238 | 2025-08-10 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eb41895-4d65-3ac6-a16b-adc6fab1fafd | -14.29907 | -51.97696 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2905a920-8fe7-30a0-ba88-41dd55574343 | -12.58425 | -47.11102 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34bb994c-45d5-34da-9d11-aef028e12bd2 | -14.29352 | -51.98394 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5a28bc4-4f78-304a-a5d9-29b320e08c9b | -17.65064 | -45.0157 | 2025-08-10 04:23:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| baebcdcf-9e87-31a1-b8b0-e7e1d5ab9df2 | -11.36878 | -50.53188 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94538a7e-ccee-3cc5-a06b-e9050aa48ee3 | -11.79849 | -46.69672 | 2025-08-10 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00ba0243-f7ce-3acc-b7e2-dff156d68d22 | -16.36968 | -42.54574 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 41ccaca6-5f94-337b-89fc-1fd7851ce19b | -13.59717 | -46.93922 | 2025-08-10 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb689cf2-5a82-3758-b8f0-83fb437655ad | -11.77565 | -47.56203 | 2025-08-10 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 868ee1ac-d78c-3872-9d6e-2a26e58710bc | -15.09287 | -46.53906 | 2025-08-10 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ad64da5-c8e5-33dd-9f4b-bf4e013fde47 | -16.37946 | -42.53182 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 66c6b689-c925-3384-989e-bd31ba6d5d69 | -12.64629 | -44.50934 | 2025-08-10 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21a43a11-c043-3eeb-8187-199c0ee637a4 | -14.29286 | -51.96397 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6edc76cb-6670-3d1b-b535-c1d112923769 | -14.58872 | -47.15653 | 2025-08-10 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac8a8853-62b0-382b-bb5b-1ce031bc3a67 | -11.10523 | -50.4837 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7f782e0-e20a-323f-b7b2-a04c7ff91057 | -15.14989 | -43.94655 | 2025-08-10 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acacaef0-4440-32d2-86e6-af21506d200b | -14.28803 | -51.96701 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fa61aed-7f65-3b08-acf1-1c2a44fd83be | -15.92033 | -47.95941 | 2025-08-10 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2389a343-46c1-3b8e-9fc6-e52226d1c4a7 | -14.28389 | -51.96622 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84544bf9-3160-32ca-88db-ab0c895999bc | -11.33541 | -51.44469 | 2025-08-10 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18fd7b2a-5aa1-32fc-8684-fbe35c339726 | -13.62711 | -49.00322 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbb459f1-dfac-3104-a48b-e4b013cfa66c | -16.37492 | -42.53624 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d208ab16-4782-33f8-8cb6-2bada12390cc | -12.55923 | -47.08461 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1afc0bf1-fd2f-3332-8f48-fe74c292e5a7 | -11.48547 | -50.28088 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a95eb47-f7d9-3a35-85bf-52c999785480 | -12.40538 | -44.21399 | 2025-08-10 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd3a13a2-6914-34ac-bea4-019548a91ee1 | -12.14237 | -45.6433 | 2025-08-10 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad017d61-3a82-3dec-8101-9203b0a8e6b5 | -12.64234 | -44.51248 | 2025-08-10 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2812c9bb-74d3-3331-8b00-9ed4e5aebf83 | -14.46653 | -47.84566 | 2025-08-10 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a954a93-3521-30ac-997c-7be650f19330 | -14.45062 | -47.85794 | 2025-08-10 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26b32c9e-a2f0-3699-852f-6e10429bff19 | -16.37805 | -42.542 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 28c4614e-bcba-3605-8f5f-ecfc8712cb7c | -16.37038 | -42.54065 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3afec9be-a48b-3b27-ab7e-acc17f3e4f4d | -14.37421 | -51.11347 | 2025-08-10 04:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8e6d66b-1842-3966-85da-31cb735a6799 | -13.06029 | -56.84971 | 2025-08-10 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09152c53-6876-3179-b99a-e92cc9099499 | -11.36969 | -50.52671 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf9079bc-47f3-35e6-a550-82a62a2c6542 | -12.57863 | -47.11409 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27b828c1-35db-3836-bc5d-6c43617d3b19 | -12.71521 | -46.36259 | 2025-08-10 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 071b1122-3ed5-3da6-915e-c331b85e8861 | -13.63691 | -48.98835 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
