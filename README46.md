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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81846547-0618-3452-83dc-1b81a25b1abd | -11.0806 | -44.11744 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0844c17c-744a-3171-90ac-ce9e38fa98ea | -11.96296 | -43.49181 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c520f60-05fd-3e85-9050-d70457528872 | -13.59681 | -48.5784 | 2026-10-10 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 425cfdd6-3559-346c-a1d9-a98245c51ff8 | -17.49271 | -42.42176 | 2026-10-10 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5e35504-0579-355b-be07-a388e7eef336 | -13.39581 | -43.88016 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a373e0bc-3d26-3592-bb64-2db6da5d0ab9 | -11.1808 | -45.31572 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ac085fa-b306-3c13-afe2-d61bd6793250 | -12.78046 | -44.89006 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c26dfa8-ed6a-388e-8882-2b4cdb4d9590 | -10.44879 | -47.18695 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 663ef8c9-9cfc-3706-ade3-68c8b3b96a9b | -10.89923 | -44.82701 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 631c7a22-6ce6-36b2-9cab-16c2ee02dc30 | -11.79927 | -46.71108 | 2026-10-10 04:10:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a848cf06-a230-387e-be8c-421f12e4aea3 | -11.96627 | -43.49235 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 795f1f9c-53a0-34a7-b6f1-bf4c89c830f8 | -8.50359 | -54.6144 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0eb6d718-f8bb-39f8-8eda-d19592ee366c | -13.2538 | -42.25431 | 2026-10-10 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9c581ec-7e0a-371b-bf93-f2a773989381 | -9.89213 | -47.62809 | 2026-10-10 04:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de362914-0189-3c01-9a12-4cd802e20537 | -11.51386 | -47.61051 | 2026-10-10 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9a11df4-e446-3f65-9048-247028600ad2 | -17.34846 | -42.66666 | 2026-10-10 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b88687d7-0df1-3f19-8a61-28a9f6db6ec2 | -11.75664 | -46.7929 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 821a20f8-7186-37dd-9e9f-51435534b612 | -8.64654 | -54.53577 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e38468fd-d009-3054-9856-41133fcc9669 | -10.25689 | -49.69135 | 2026-10-10 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2053f110-3a20-3016-a015-6730d1b2f095 | -10.57821 | -46.37867 | 2026-10-10 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37f0fea6-8b42-3299-bfa4-32470cc76f8c | -17.71883 | -42.04651 | 2026-10-10 04:10:00 | NOAA-21 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd8bcdfd-3ee3-3c4e-a06e-2f843bdb2790 | -12.45128 | -51.39413 | 2026-10-10 04:10:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6663cd9f-f50b-3880-8ef3-95929148fcde | -10.74192 | -48.53812 | 2026-10-10 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 449cd212-132b-3676-90b6-85b2d1a9a03f | -15.56903 | -44.51424 | 2026-10-10 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac39e9c4-f767-305a-a4be-d03c7b2cca88 | -11.37634 | -47.56548 | 2026-10-10 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34b7ab5c-7cea-32de-9215-adfae4ba385f | -11.25889 | -46.35344 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b73f542a-5524-3de1-987c-a9937987a5c0 | -13.19821 | -48.13471 | 2026-10-10 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ceee2689-ce0a-3f9c-ab7f-5e99c14350a9 | -14.46342 | -43.9517 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96c6c52e-13d9-3983-b4ec-7943ac628332 | -15.65724 | -48.13607 | 2026-10-10 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e671bc04-8f34-3022-9ced-f2b9b57aadc8 | -14.44455 | -48.12078 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e734ce8-4832-396e-9713-5c360d96550c | -11.95857 | -43.47672 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73c31cfe-b2d6-31c6-a37d-676897c4b885 | -14.53182 | -48.04199 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cdb09740-2778-36ca-8206-3ad8fc7a2400 | -17.22762 | -42.93438 | 2026-10-10 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 755dc7b8-ce38-385d-b122-fce0258799b9 | -17.94483 | -43.96405 | 2026-10-10 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72627e76-ce6a-3df1-a9e9-21556bce6f56 | -10.89863 | -44.83078 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d11546a0-b402-3ac9-a07f-3d4029eebe6f | -15.49867 | -41.47163 | 2026-10-10 04:10:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| bdf2d971-8479-3de3-bd71-68b84f81475e | -11.96628 | -43.47077 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d52adbf0-147c-376a-9a9e-b6f553a46e0c | -13.26665 | -44.00813 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b3b34d9-f052-3964-92fb-2615f0772ef1 | -14.45681 | -43.95061 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e25b60dd-cfbd-3670-9e06-0577fa4f662c | -11.08568 | -44.10715 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95c9849e-3a19-3829-96ab-bfde5540a3a8 | -9.84996 | -48.01341 | 2026-10-10 04:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea5863b1-32fc-33c5-ba9d-14c3c7876371 | -12.02676 | -43.47742 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9d8540a-a596-3723-ab36-ea00884e598f | -13.52265 | -47.4211 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e4ee32e-ac64-3017-a0f1-93dca19694a0 | -14.81427 | -42.3359 | 2026-10-10 04:10:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 221c9a6c-aefe-3dfc-9b76-af3b1b4be075 | -11.20983 | -45.24809 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fc8a906-9ce0-3193-81a7-c70ca72c5145 | -11.95527 | -43.47617 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ddb342e-c44d-31c8-bb00-6edc0d2a92b3 | -16.76006 | -47.07012 | 2026-10-10 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8041c9cb-9d59-3ca2-9eed-e515b3d1ca25 | -14.7567 | -48.22932 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| def04376-42c5-3623-bcde-05bf8e5fd243 | -16.59309 | -46.77108 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8aa89c27-2b67-3511-a29f-f26f76a8b95f | -13.90922 | -48.9179 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 79cf6ac2-387a-3433-891d-08676f5e8f38 | -14.32319 | -44.65908 | 2026-10-10 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a058e2a8-9d03-3aa8-8281-b0169e26b697 | -11.08002 | -44.12105 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 268431ec-96d0-3d53-91da-516f60289522 | -11.56073 | -43.69004 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afd6431f-f1f0-3c0c-9915-c23afe0c9177 | -10.89764 | -44.81506 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3369b6e-e577-3205-90ae-d05aa7ac5c19 | -15.85009 | -42.03778 | 2026-10-10 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 349f2151-8f38-35ef-81a1-52b9023bf8d4 | -13.91985 | -47.84478 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfaf32ce-476c-381d-b31f-fc5640a0574f | -13.52343 | -47.41663 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 695da609-2cd1-3ed7-a78e-f0ae74804787 | -14.34081 | -55.01567 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9d71096-f2e6-3cb6-8321-3e206e61510d | -13.507 | -48.61086 | 2026-10-10 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b7efa50-d5a2-35d8-b713-27e9593a7ae0 | -12.00036 | -43.45152 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bc17654-7dec-38a9-a548-412952daa13e | -11.02204 | -44.06001 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00dc5d31-66a9-31aa-bd8d-4c19e301af94 | -12.9978 | -43.34097 | 2026-10-10 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 244b9c31-47d2-337a-8a9a-80292d82b1cd | -15.02883 | -46.26167 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 903488ee-3fec-34d2-8042-d2d8f5ba3a54 | -11.84232 | -43.60959 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 802233a1-b36f-3aab-9cc6-c1faade84be6 | -10.89927 | -44.8264 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f91b7a4f-d446-3c4f-b524-8a42dc8bae12 | -14.97216 | -41.69545 | 2026-10-10 04:10:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d1a9b61b-3587-3868-969d-81e19a8524cd | -16.12262 | -43.74216 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 709e96be-2448-3eaf-bb48-d817781db2ce | -11.25784 | -45.17227 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69edf2e5-72e7-344a-b82c-0e7af40d9027 | -15.0872 | -46.94555 | 2026-10-10 04:10:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5ee02935-6f36-361e-beb8-3173c86da8bc | -12.33103 | -41.79692 | 2026-10-10 04:10:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8368e7af-9df2-3ac4-a0d7-04039d7aacd4 | -10.89802 | -44.83455 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b13269f-817c-36d0-b5fb-69549fb449e8 | -16.6395 | -40.59649 | 2026-10-10 04:10:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ce48a26e-b831-3b76-9ca6-74086877596a | -13.75361 | -48.51783 | 2026-10-10 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0094ae9-5a4d-3dad-9f24-fb14b48d48ee | -13.75761 | -48.51852 | 2026-10-10 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92611c32-55e6-3661-bd17-80c1188aeea4 | -14.0605 | -43.83045 | 2026-10-10 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d077918-6b54-37dc-8164-2a96dc14f320 | -15.3779 | -41.91254 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9d10f2e1-aea5-35f7-9937-af6ffa28943d | -14.71404 | -48.22229 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc3e4da4-0c17-38cd-a1eb-0da5f5d70f58 | -11.96573 | -43.47429 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fec80db5-5b50-388f-986b-7d92e096ef49 | -13.91602 | -47.84411 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01ed2e8b-3313-3002-824d-4194dd0b4f8f | -13.37146 | -43.90523 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b78e0064-a58c-3602-9bd7-debda74c1309 | -13.10388 | -46.35672 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f930346f-1bbf-3b79-a975-5c0cdf1154d0 | -13.77769 | -48.12394 | 2026-10-10 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e2e9990-ebb7-3680-bbb7-3545281c8df0 | -16.56223 | -46.79991 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e65bb03-8740-33a6-99c5-b0645e77cd77 | -16.64314 | -40.59707 | 2026-10-10 04:10:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 43cb2b8c-1530-3a34-9c09-48c7d22032a6 | -15.74801 | -41.56556 | 2026-10-10 04:10:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aeccc6e7-00a4-31d2-bfb3-d9891bd5e3a2 | -11.9288 | -46.76987 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07bf1ec0-a116-3a3d-8632-7aac3e56ddfa | -11.47269 | -43.38687 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6f32fe2-a092-33b0-9c04-f0b33506f923 | -11.61232 | -43.60063 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7fc152d-49eb-3d0b-810f-25f76e88e40e | -14.33261 | -44.66439 | 2026-10-10 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4ad8434-ea3d-3392-b80b-da07ba979b84 | -11.67719 | -46.85426 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41bcf2eb-8221-3836-a0dc-25e28a9e750b | -16.75935 | -47.07426 | 2026-10-10 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eadaa6fb-5bb5-3ae4-a93a-aa03ea46a36b | -17.50573 | -43.67981 | 2026-10-10 04:10:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 633c915a-335a-358d-8fb9-3c51979950e5 | -13.12808 | -46.32187 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13b45f6a-bbf7-3aa3-8d28-cab8e861df87 | -12.49629 | -51.29912 | 2026-10-10 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cbea3fac-c98e-3a61-b629-315fc13d0dfd | -16.02821 | -45.1316 | 2026-10-10 04:10:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19943150-926c-3396-8142-6bc15cc8e41a | -13.38033 | -43.89215 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 44bf4747-ccd7-3f40-a6e4-f288fa3079af | -11.96958 | -43.47131 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 268961af-d2f2-3575-9c7d-8cd73d444ddc | -14.46286 | -43.95525 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b86b0ade-5e9f-3ea5-9439-d69478948a0a | -10.89042 | -44.79444 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fcf846c-3eb1-3dd9-bf75-e296c1b116ad | -11.56569 | -43.70168 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README47.md)
