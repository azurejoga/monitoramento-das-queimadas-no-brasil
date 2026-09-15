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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e8d573a-486c-37bd-ab82-ee5d7062c148 | -9.36098 | -50.09462 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21d68ce7-090d-3d88-bc3d-1d7c525583ff | -7.7639 | -45.18076 | 2026-09-15 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eb05385-88c0-374c-9934-54bfbba4493e | -12.78792 | -47.56188 | 2026-09-15 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48642c6c-5f46-3088-9eec-7f47f45d24ed | -7.46706 | -46.15038 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a67ed3c-9487-3218-af18-d6c4c40f761c | -9.35793 | -50.17699 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cabf8a7a-4eaf-3ac6-9238-f7dc23a98b6e | -7.08435 | -42.12457 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5240c64e-4037-3790-9df2-201e2010b726 | -7.24527 | -46.15848 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d47628b3-9349-3382-97c1-99fb220670c9 | -11.26845 | -54.13039 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e5a0047-28ba-389b-ba7d-b38d73377e5c | -7.23598 | -46.16093 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afc1bdbf-1350-3cb1-a60d-17b2755bb8f2 | -9.35558 | -50.09354 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49703cfc-3904-3153-a7dc-4095a73a8fda | -8.99641 | -39.98199 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| daa7b53c-5252-32b9-a4f8-741dd266dffb | -9.45311 | -48.90638 | 2026-09-15 04:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8263b0ef-14c7-32b1-b77f-b706c897abb4 | -12.49527 | -41.42136 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 399c6ff9-eac3-38ff-a229-fcccff784c24 | -8.40068 | -42.21907 | 2026-09-15 04:14:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7217f1ce-7763-3e13-a7b4-6090d3f3bf22 | -9.42314 | -50.09898 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e28feb8d-05e3-377b-a40e-6feb158b6f80 | -8.20936 | -43.78536 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e1c9c64-3783-3850-8555-94e358c82bc0 | -9.35697 | -50.0934 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 823f84be-6a4e-3deb-b29f-38c0a90c6703 | -15.04957 | -48.5874 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef360fc2-1af7-3e97-a198-1b33e688f3d9 | -15.53944 | -41.78637 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 13a3af22-4ed7-31e4-8e04-f44274926e22 | -14.15707 | -47.39622 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33c7bf56-53d5-3032-973e-f32b9583b9f9 | -14.86524 | -48.14283 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d00eafac-438c-3eb6-90cf-0cc922fd0871 | -17.98597 | -44.3287 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed2eb70b-f900-3df9-8a65-94646c17ed9c | -13.22769 | -51.65187 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c59a6e1e-6068-3bd1-a57a-7d2b03c2fae9 | -13.63509 | -47.88618 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f3504d1-2478-3bb3-8c22-ffa3dab58b09 | -16.00318 | -40.68548 | 2026-09-15 04:17:00 | NPP-375D | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 41b1ea34-94b6-3f3a-9e73-fd0b7472c10f | -18.1663 | -51.76694 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 818fcbcd-ff7e-3bea-84c4-d17627d27319 | -13.64021 | -47.88265 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f0d79b2-46d5-392c-a34e-27ef16bf4c73 | -15.04576 | -48.55835 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e805feb1-3da6-3125-993f-182effa04efa | -17.35392 | -47.17329 | 2026-09-15 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14478cba-6819-3230-b530-2c89b98dcdff | -15.5369 | -48.80604 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af9bb89a-93cf-3168-b700-3057999228ec | -14.85749 | -48.13647 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 856d4523-159b-39f8-8fc5-897dff07f966 | -15.44639 | -44.84393 | 2026-09-15 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0af64d6-dee6-387f-9007-e2e924d6ef1e | -16.56536 | -51.62212 | 2026-09-15 04:17:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f48ef6d0-7fc7-3125-8665-523602e132b2 | -13.29909 | -51.29106 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47198e53-3904-3e26-86f4-a28f9398df55 | -15.55235 | -48.82225 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e6e6f56-65ca-3843-b5b4-ad41e408ce89 | -18.16696 | -51.76374 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ae55bcc-9c4e-38b2-8b6f-1b358061787b | -13.26172 | -51.27935 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4860ebde-d570-365c-86c8-b1ef7718204d | -16.62884 | -39.18976 | 2026-09-15 04:17:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| baed9949-cc05-3264-9dc6-223d6156afd1 | -14.19079 | -47.42912 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cf2e753-89f4-3846-b579-efc096dc0f2d | -15.04826 | -48.56253 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb778e6a-a672-35d7-90f2-ce8d605da243 | -14.1991 | -47.43082 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 975bef04-780f-3822-94ff-1189f99c449b | -14.86097 | -48.14179 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2bca457-f347-3171-9439-4ff7a6301781 | -14.21174 | -47.38565 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| de0975d4-727a-33e1-9cc3-3858a7be2a07 | -18.16763 | -51.7605 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f0a052c-af0d-3dae-bfea-fea917297f82 | -15.54343 | -48.82054 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8736059-0699-39ab-83e0-b4e690de5c1e | -14.67381 | -48.00608 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f73d5b1f-6a1a-302f-ac03-91424b411a40 | -14.85905 | -49.9427 | 2026-09-15 04:17:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecd747df-fa09-3fe7-a1d2-9477b9b45c8e | -14.20535 | -47.42031 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| efdb48cf-f0de-3b4b-842e-60256508a4f8 | -13.26573 | -51.28767 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45399bba-ee27-38c1-961e-e1d4078ee7b4 | -13.231 | -51.66446 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90f8797d-1c7f-3708-8f1d-1a163b7b190d | -13.29768 | -51.29821 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bd813ff-8459-348c-8ce0-8cf53791c44d | -15.25482 | -40.9919 | 2026-09-15 04:17:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60ca2207-cb01-3fd9-9a84-a6ccac23c838 | -14.20321 | -47.43192 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 898f97c3-6ef6-36f4-924a-a8d4fb708def | -16.48529 | -47.82244 | 2026-09-15 04:17:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4f5ff83b-d815-3d5f-adfe-3889fe4e0811 | -13.29979 | -51.28749 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60194471-4d72-370d-8e87-f40c39c3e47f | -15.2009 | -47.94631 | 2026-09-15 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69325068-f1b3-3760-b4c5-b513bddcb3e4 | -18.16831 | -51.75724 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73749ea2-86c5-3318-92f0-3134d59adccf | -16.97215 | -43.35631 | 2026-09-15 04:17:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09fa4672-2a7b-3582-a1ba-205bc3acfd86 | -17.46805 | -43.65874 | 2026-09-15 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfb0461e-b887-38f2-81c7-439f915f4886 | -14.16453 | -47.40265 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fa51db9b-fb75-374f-9e4a-cc2cb21eb024 | -18.16323 | -51.75589 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53ca6434-7aef-3521-b1b0-1c562220609b | -13.57754 | -47.90599 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 679f363b-dd83-33db-a934-8536a7823009 | -15.59392 | -42.56845 | 2026-09-15 04:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 70afba7b-ec0a-341e-96f4-5779ea3460c3 | -15.25704 | -40.99978 | 2026-09-15 04:17:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| eab9ad5e-464f-38e0-9f8f-b0520b1b63fd | -17.31306 | -49.22975 | 2026-09-15 04:17:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c89107d-c60f-3b19-aaf8-1fee62c44d90 | -16.86477 | -50.15741 | 2026-09-15 04:17:00 | NPP-375D | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c8875e7-93f7-3343-991a-7661bb09c304 | -14.96099 | -47.53044 | 2026-09-15 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ac8b2cf-a183-37e2-91cf-311544eaf500 | -15.54096 | -48.79513 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a278ca29-bbd6-3081-ad81-5d901529b9b2 | -18.17206 | -51.76501 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5da3a8f8-a12d-3216-ac9e-4d38479e6e5e | -18.17338 | -51.75862 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 602150ac-e28e-3628-944f-ca1c7b9724b0 | -13.27189 | -51.28523 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 10291b29-23bf-3f2b-a172-2dcee37a6555 | -14.63833 | -42.45187 | 2026-09-15 04:17:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1992d0bb-c90d-3819-b78e-649c6bb77b1c | -13.63587 | -47.88186 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 664ff3ba-8e6d-30f4-ba25-49a4c622e254 | -15.58109 | -48.82657 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b504743-3214-3e1a-b6a4-8aedc9751f45 | -13.72966 | -48.97839 | 2026-09-15 04:17:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70e23223-936e-369d-a80f-f1119a528e28 | -15.5974 | -53.78431 | 2026-09-15 04:17:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df459a3a-5b6b-3e6e-be7f-8ae25d3dbaa4 | -14.16038 | -47.40177 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76350be7-5061-3e6f-880d-ff6ca08b8ca0 | -13.27662 | -51.28997 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 09e5c28b-f185-378d-ba58-bbb6b2d77985 | -13.57318 | -47.9052 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9241cb8-f9c5-3d6f-a5a7-25cabd07bb6f | -14.85323 | -48.13534 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8fee65d1-6df2-3512-b3a2-80756b4c0e61 | -15.57842 | -48.79225 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecc27bb1-aab3-3c40-bc8f-f82f1d250144 | -14.67521 | -42.84825 | 2026-09-15 04:17:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9fd64258-92ed-372d-84f2-048df5ffc204 | -15.5537 | -48.82477 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c70b09c9-2b6c-38f2-b51f-5d84c4590626 | -17.98872 | -44.33318 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9212abc-d15d-3672-a801-1cd680f96b6a | -14.04301 | -43.29332 | 2026-09-15 04:17:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| afa87c7d-3cc0-3fc8-85dd-fd3512e8a8e4 | -15.25425 | -40.99556 | 2026-09-15 04:17:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d18d62e6-8b86-3ef6-adae-808587079a8e | -15.59001 | -42.57147 | 2026-09-15 04:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 6165f67b-882c-3944-a323-93c385e5ab75 | -15.59334 | -42.57205 | 2026-09-15 04:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 16f80ad6-49ae-3fba-9a1f-78e34ea0c389 | -13.64184 | -45.98312 | 2026-09-15 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaa6ef1c-8c3b-35cf-9224-1fea692f2a20 | -15.24577 | -43.92081 | 2026-09-15 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 514daf20-dece-31ff-84f9-d40c048b01ee | -15.05447 | -48.55402 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 664caeca-0e06-3ccb-9270-f23db87a6bb7 | -13.58101 | -47.91152 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7dcf0e7-ba4f-3afe-add1-e91e08fcc074 | -14.7644 | -42.94553 | 2026-09-15 04:17:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1600f3e0-56d8-394b-bb02-bdb5ac6ac6df | -14.8625 | -48.13356 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fcfab031-31ec-376a-aaf0-1c6d90318853 | -16.64655 | -40.83271 | 2026-09-15 04:17:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 16c6f006-1a93-3c18-b0f9-9aa10e6729cd | -15.9803 | -43.66997 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7074740f-6f1f-3e91-89be-232b98397346 | -14.86445 | -48.14713 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 393dbee7-6942-396d-97e1-ffd743958e8d | -15.55685 | -48.57687 | 2026-09-15 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3411427f-d8ef-3d64-bfed-b049f99c784e | -15.2788 | -42.78562 | 2026-09-15 04:17:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f8bea56-5dde-3ec3-b9e6-a81a21ad9cb6 | -14.8619 | -49.95404 | 2026-09-15 04:17:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README32.md)
