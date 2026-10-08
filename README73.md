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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 818b59f8-7fb1-3281-a94e-54bd6aa83430 | -17.42938 | -43.64789 | 2026-10-08 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b6d0840-2952-32f8-bc58-781c8db835ec | -18.62414 | -41.28323 | 2026-10-08 04:04:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3b0a895e-7a22-3dc1-a188-365126a35f71 | -14.92912 | -48.10446 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| be7a4073-02b2-3e12-bcc2-e29913434193 | -11.74269 | -44.94044 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48105fb3-cc30-3c2c-abb9-e3c88ab0c525 | -14.92142 | -48.11909 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5024c6c8-0a14-34ef-9d85-2e20cebde738 | -16.84516 | -41.04366 | 2026-10-08 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 267b02e1-d11f-37b2-9a2a-a6258e11e9f4 | -11.31627 | -46.68727 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9e733bc0-e6bc-3561-b313-19344efbfa78 | -15.42306 | -43.7019 | 2026-10-08 04:04:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0b3beb82-bb62-3d12-9de3-a86ba64a219d | -11.3938 | -47.55635 | 2026-10-08 04:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b22d3bb-f60f-3c40-967d-8af1928969ad | -15.55308 | -42.97811 | 2026-10-08 04:04:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f080ac7-2886-314b-97cf-ee4424268a3b | -17.50697 | -41.91396 | 2026-10-08 04:04:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a4579585-9c4f-3b84-86b7-324a20ac93bc | -13.33743 | -43.31826 | 2026-10-08 04:04:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e248eb9c-f72d-314d-9353-67597cd03532 | -14.96571 | -41.54893 | 2026-10-08 04:04:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2ebef118-1a27-3b38-a432-4b77518c1bd9 | -13.51207 | -40.8312 | 2026-10-08 04:04:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f2962c73-157f-3485-bad9-d96b8ad80eaf | -15.41876 | -43.70546 | 2026-10-08 04:04:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1d2b607-8e1f-359e-b74d-1edd55d4d7eb | -14.93262 | -48.11167 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 56444433-6fa4-3736-9b1b-edf2abe8b24a | -12.83675 | -45.57964 | 2026-10-08 04:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1d2d593-d9d8-33f3-b7a0-91ebb7739548 | -11.34135 | -51.87573 | 2026-10-08 04:04:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54a908cd-d33e-3d90-a4e5-475669c69b46 | -12.23634 | -44.73495 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4d005e7-4dca-3947-ad08-30af83d30594 | -13.15676 | -43.28307 | 2026-10-08 04:04:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 3b247f8d-1d13-3a4c-877f-8836c6fd77fc | -16.0139 | -43.60144 | 2026-10-08 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 076433fd-b603-3d19-93f8-afb5a4cf638b | -13.17201 | -54.32955 | 2026-10-08 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b555e302-b704-3c26-bc80-faa41f78ef63 | -18.37307 | -41.96055 | 2026-10-08 04:04:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 954074b2-ab7b-358f-86fb-14b645c2f757 | -10.49315 | -51.94711 | 2026-10-08 04:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 649c6c6b-a259-3d38-ab25-718297f8697d | -18.19657 | -39.62291 | 2026-10-08 04:04:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a2a5ea6b-b72d-3f82-a839-cffd80ce7090 | -18.52739 | -39.77248 | 2026-10-08 04:04:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6e30dca0-8d22-30ac-9aaf-11c237f56743 | -18.37033 | -41.95634 | 2026-10-08 04:04:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4313768b-5bd7-37fe-b5b5-112fc483167b | -11.78278 | -46.76949 | 2026-10-08 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa958fb7-276d-330a-994f-6c65d5f2f6f4 | -15.24617 | -47.41298 | 2026-10-08 04:04:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 078d6c09-0c17-3182-8bfc-15a2c7fa4252 | -15.10863 | -43.63106 | 2026-10-08 04:04:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80ae67f0-53a9-39b5-9445-2f99bfc751af | -16.12632 | -43.74685 | 2026-10-08 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e22ed4e-20ce-3ad7-a807-91f4e7cbcba1 | -18.25758 | -42.16939 | 2026-10-08 04:04:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7b2c59d5-93c1-3762-a249-ad4e618599a1 | -16.12708 | -43.74248 | 2026-10-08 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf4358bc-74c6-37bf-a1e5-093343298da0 | -11.39083 | -47.55436 | 2026-10-08 04:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b361005-90cc-3c70-9eba-79e318617e26 | -16.0132 | -43.60559 | 2026-10-08 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c676545-e697-3c19-922a-98f846357957 | -12.99412 | -47.06374 | 2026-10-08 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77d2212c-4ed6-3e1c-8896-fd955654eaef | -18.38783 | -40.31748 | 2026-10-08 04:04:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 67d9eb0b-e0b6-30da-9f26-d4b106d3de00 | -18.22406 | -42.31123 | 2026-10-08 04:04:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 97f22f53-96ca-3a20-9631-b2d4f7dcc0c7 | -13.16036 | -43.28373 | 2026-10-08 04:04:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 41.8 |
| d312c14b-32bd-3ad7-a61c-1e4fc92a8238 | -12.15232 | -44.75571 | 2026-10-08 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43e3f2c5-427d-3bbd-95ad-4b40cb5bf98f | -13.18855 | -47.88048 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f27bef8-cc6b-39c4-be12-a16aff82ead7 | -14.76284 | -40.93457 | 2026-10-08 04:04:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 74a06007-3485-3932-8269-0d936ac074fa | -11.38812 | -46.68113 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d1c98cdc-ad41-3ada-af92-9fcb1fad987a | -10.49427 | -51.94151 | 2026-10-08 04:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbbbaf98-c847-357f-98cd-cf2beb8812b5 | -16.86029 | -40.58113 | 2026-10-08 04:04:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 695239a7-f1ec-3601-b19d-8f58eeda9341 | -13.27606 | -43.63655 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd622480-b082-32e5-afc0-e3e98e7acbde | -15.42422 | -46.11434 | 2026-10-08 04:04:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e38ece3-bec6-3725-b494-221285dc9e41 | -16.15265 | -41.46501 | 2026-10-08 04:04:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| da4461d1-24e7-33fc-9347-9ef673b25f54 | -16.90318 | -40.89103 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 5de771eb-89bf-3149-bf39-f0041f76a5a3 | -14.91113 | -48.12181 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afc7eaa3-137d-3c80-aa10-45b3abd7bad4 | -14.90888 | -48.08301 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74d3bd3b-44c5-3b42-9fa0-a48446b6ead4 | -16.90649 | -40.8916 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 9600b2ef-028a-3ed6-b75c-0a49ccd4654a | -13.15749 | -43.27884 | 2026-10-08 04:04:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 64.4 |
| c4e1d1c3-28b8-34d3-b77b-2fc64d997c8c | -11.86091 | -48.03406 | 2026-10-08 04:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb67d0ec-6bc6-3926-b656-23ab692ec55e | -11.39077 | -46.69243 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 89973b32-66e0-3038-b8bf-a1841f0b4dfd | -11.32545 | -46.68867 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0519cbb7-fee2-32f6-925c-7f29b7d6464b | -16.83136 | -41.04499 | 2026-10-08 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36933f39-a90c-3a3c-91fb-dfeb15c78158 | -13.18958 | -47.87514 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6ceb115-d9a9-3982-a036-0e5d68f1ebbe | -19.99289 | -49.088 | 2026-10-08 04:06:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fab86d93-56aa-381e-a5eb-ef1ba47e5d3d | -22.02186 | -49.57356 | 2026-10-08 04:06:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ef159c3-4c73-3b81-b745-0e23ceead469 | -22.02733 | -49.56995 | 2026-10-08 04:06:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ce0a214d-74fb-3890-80b5-11ed61bae270 | -20.4264 | -48.68484 | 2026-10-08 04:06:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32b93d84-a744-36df-b4b0-1eea236c3e54 | -22.02087 | -49.57838 | 2026-10-08 04:06:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 88c98794-5eee-3f37-9e8f-60a613239d8a | -20.3138 | -41.35429 | 2026-10-08 04:06:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e284721-b3d7-31cd-a07e-87498875ab84 | -22.01637 | -49.57728 | 2026-10-08 04:06:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d08eeb39-5f2e-3fd4-9e6c-784c0415df8c | -19.58492 | -44.72407 | 2026-10-08 04:06:00 | NOAA-20 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa48d7a0-7fa6-35a7-bf55-5afc0b45aba3 | -22.99063 | -48.65869 | 2026-10-08 04:06:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a696a7c2-810b-3c37-99a0-6181a703f183 | -29.71815 | -51.10459 | 2026-10-08 04:08:00 | NOAA-20 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| e2fa118c-5c09-38dc-9bb7-3200bad0f595 | -28.979 | -52.56193 | 2026-10-08 04:08:00 | NOAA-20 | BARROS CASSAL | RIO GRANDE DO SUL | Brasil | 4302006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a6bfec6b-e27a-332a-a8b3-74eea42128f8 | -5.7376 | -45.1533 | 2026-10-08 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 55b090a6-57f6-3efc-ac86-2dbfc1908039 | -8.742 | -45.1563 | 2026-10-08 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| db2f2ea3-2d98-3d1d-b54b-9fd14d72e6bd | -8.6291 | -67.0296 | 2026-10-08 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 9e7dbfb3-4e5a-3724-a500-8ad8b7a3cc7e | -3.1786 | -50.6016 | 2026-10-08 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 97cf2bda-ae5e-3065-90cc-87dab302304d | -3.1101 | -54.1661 | 2026-10-08 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| dd6c47d8-71d4-3d77-ac6f-e25a69333f88 | -1.5306 | -54.5359 | 2026-10-08 04:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| d2882ca1-cee9-3634-8c8b-e704a57619ea | -6.6317 | -43.73 | 2026-10-08 04:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 6a1f658c-7508-35f9-bcb7-7bade23ee7ab | -13.1668 | -43.2673 | 2026-10-08 04:10:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 74.2 |
| d80d0824-dbf6-31df-a8d0-c18358f3f1ba | -3.11 | -54.1862 | 2026-10-08 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0aee802d-9a18-3fe6-a758-150988082faa | -8.6107 | -67.0301 | 2026-10-08 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 329bd093-bb56-30e4-a90f-cdb0d66f1ed8 | -1.5306 | -54.5558 | 2026-10-08 04:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| baf87bc6-0d82-3221-b036-c0c214bb3140 | -8.6292 | -67.0111 | 2026-10-08 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5cd117b1-be6d-38bb-a868-79b0f582c22c | -8.6107 | -67.0116 | 2026-10-08 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| dc675544-5da4-3876-a674-f14cdc0c1d5b | -8.7228 | -45.1812 | 2026-10-08 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f565f967-8779-3035-9f00-ab82d0b9d178 | -6.1431 | -47.9214 | 2026-10-08 04:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 2a026d36-6eca-3c4f-ba50-d63b55138210 | -2.7797 | -54.0736 | 2026-10-08 04:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c974fb7b-96d2-3cb4-b302-e3e8ad70b8e5 | -3.1114 | -53.7839 | 2026-10-08 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2fd8450b-4a98-3fca-aaec-43f635e74543 | -2.4987 | -56.1659 | 2026-10-08 04:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 58f347fc-517b-32ca-9252-946b816e903b | -8.7231 | -45.1583 | 2026-10-08 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1f788da1-b8f4-3782-918a-4394a72fef1a | -3.5861 | -54.6741 | 2026-10-08 04:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 24ddc1fc-3eaf-3be3-9b5c-d20389e48c06 | -3.1972 | -50.5592 | 2026-10-08 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2a86ec67-9714-3c76-b772-ef8d47bd8130 | -5.6932 | -53.487 | 2026-10-08 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3f7d12d9-a92f-35f1-ba94-8e114a7f9436 | -6.1429 | -47.9432 | 2026-10-08 04:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 01cb049e-ae7d-3e03-94c6-baf5cac5b4a7 | -3.02 | -54.11 | 2026-10-08 04:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc33c21f-1ac2-3bcc-a5b3-5a8d98910b78 | -3.0 | -54.11 | 2026-10-08 04:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6454c97b-ad2c-3ebc-98b3-04f790e68b42 | -3.0 | -54.04 | 2026-10-08 04:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e74a3c9-937a-3850-b5e5-ef20559ba4f2 | -3.1102 | -54.146 | 2026-10-08 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6f99f2fc-2932-319a-91cd-b015ed191084 | -10.4151 | -47.2623 | 2026-10-08 04:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 93bbe5b7-85f8-3a77-9c6b-53f6919debb0 | -2.4988 | -56.1462 | 2026-10-08 04:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b778e35b-7e7c-3afc-a589-37afa0e0195f | -8.7231 | -45.1583 | 2026-10-08 04:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 8bfcaaf6-9a57-35c9-81ea-da4e7591179d | -3.1101 | -54.1661 | 2026-10-08 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |


[Clique aqui para ver as próximas entradas](README74.md)
