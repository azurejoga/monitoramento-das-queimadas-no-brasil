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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c46aba7f-beea-3805-bca2-f22a00129062 | -21.04519 | -55.98471 | 2025-07-19 04:12:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b76eec6f-7713-3cd2-9f65-22d011b6d740 | -23.23472 | -46.26238 | 2025-07-19 04:12:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 08f80d5d-4ac6-37f6-b147-a056370612d3 | -21.69158 | -45.91258 | 2025-07-19 04:12:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b95c91ef-5643-38b3-9e87-73878c61c63e | -20.71527 | -57.70797 | 2025-07-19 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1b2748ae-a90b-30ca-987b-4b1a4fcab586 | -23.60911 | -49.00806 | 2025-07-19 04:12:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c821655-9aec-3f85-94eb-8264b4d35b87 | -23.32804 | -50.13563 | 2025-07-19 04:12:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| a30433a2-2cc0-3114-8154-979e974e2e69 | -23.48341 | -45.37341 | 2025-07-19 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 28287e13-7fd4-352a-aafc-3bdbed269002 | -23.58632 | -47.03315 | 2025-07-19 04:12:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 009166a0-d942-34db-a073-295061aeecab | -23.16802 | -50.65967 | 2025-07-19 04:12:00 | NOAA-21 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6c1b2130-9a64-310f-bb64-c24d196510c3 | -23.16903 | -50.65427 | 2025-07-19 04:12:00 | NOAA-21 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1014653e-5f92-3530-a426-07a9a7cebc56 | -22.7457 | -44.75537 | 2025-07-19 04:12:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0921c348-765f-34d2-b5d6-5d967bdb84ee | -22.83302 | -46.84866 | 2025-07-19 04:12:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a9e2b5fd-366b-3632-a1be-8ad9874fd497 | -23.48672 | -45.37402 | 2025-07-19 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0229ed0a-6bcb-3bd7-a1e9-a7bf6caf759a | -21.50227 | -57.06596 | 2025-07-19 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d54e86d4-6d0b-30e9-80ed-91fa63f6f4aa | -21.77643 | -44.33513 | 2025-07-19 04:12:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 032ea4d3-4687-3365-affb-0a304653514d | -21.61748 | -46.92522 | 2025-07-19 04:12:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00c9d08d-d5c1-3eeb-a809-0e23af479382 | -19.50836 | -43.88849 | 2025-07-19 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07cea018-9ee7-3d55-8934-452eb2b5c30f | -20.53722 | -47.31928 | 2025-07-19 04:12:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fed6903d-d849-3f9b-8f44-7744e9d4217d | -18.463 | -52.15889 | 2025-07-19 04:12:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d4bae3a-ef42-3cb7-94be-f0233ccb65f8 | -19.9307 | -47.26696 | 2025-07-19 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be4dbb63-c297-3679-b7e4-424916bb9ff2 | -21.06757 | -45.75091 | 2025-07-19 04:12:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12ba96cc-cbbc-38b7-828c-15555ab424ed | -20.87426 | -43.06033 | 2025-07-19 04:12:00 | NOAA-21 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 58603154-8e96-33b0-a467-c50a0de69113 | -18.83774 | -47.68331 | 2025-07-19 04:12:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7be051ba-fbdf-3ccd-93c8-1704cf380d1d | -18.42228 | -49.74203 | 2025-07-19 04:12:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f74e783-8059-3ad8-a067-6024c1bb04f7 | -18.65987 | -55.72815 | 2025-07-19 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b94940a5-1500-3437-91fa-2b168dd4f758 | -18.84019 | -47.68237 | 2025-07-19 04:12:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b69b7833-5abb-39f6-8c05-72ce758cdf9a | -20.91291 | -43.77882 | 2025-07-19 04:12:00 | NOAA-21 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a4f9b33a-56c8-3ed2-86bd-1559c98d5e8a | -19.93014 | -41.37695 | 2025-07-19 04:12:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33c01536-26af-3cec-accc-95ea5dc73371 | -19.45413 | -45.30627 | 2025-07-19 04:12:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29aa344b-5ae4-389b-abd4-25b348a77d4d | -18.56827 | -46.54555 | 2025-07-19 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cb66b4f-3e5a-3d3e-97b8-103ad284257f | -19.50892 | -43.8848 | 2025-07-19 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1f46a9c-f43a-3329-9757-30a12716521c | -19.51169 | -43.88907 | 2025-07-19 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 551eb592-7f3b-3553-adae-c8866aca7571 | -20.25641 | -45.67496 | 2025-07-19 04:12:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 698f6876-cdf2-3ee7-b32c-6246f8d8f62a | -19.51225 | -43.88537 | 2025-07-19 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7d0f74d-afd2-30dd-a22d-ef435b073bd3 | -20.47818 | -45.41452 | 2025-07-19 04:12:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2e7aa707-cf30-3422-bcdf-50bccb360917 | -19.77482 | -45.40789 | 2025-07-19 04:12:00 | NOAA-21 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2238757d-a13f-37ab-94a4-3bfc7fe8e0f9 | -19.92954 | -41.38142 | 2025-07-19 04:12:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| edd0fb59-ae3b-3c91-805e-7ffc4ffb294c | -20.67233 | -44.4966 | 2025-07-19 04:12:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 61402e26-3568-3206-95f2-97cef87fe431 | -20.926 | -42.84243 | 2025-07-19 04:12:00 | NOAA-21 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d8d952ce-c90f-30e8-a95b-f7d1d027669a | -19.27573 | -49.38526 | 2025-07-19 04:12:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d36ea18e-919e-3c80-aea0-3ed346384d27 | -18.6618 | -55.71952 | 2025-07-19 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a453e83b-a411-3f2c-a13f-fb203c7b7180 | -18.66277 | -55.7152 | 2025-07-19 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b61c35a2-c83d-3d73-9046-729a8cfcc423 | -25.97116 | -48.95151 | 2025-07-19 04:14:00 | NOAA-21 | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 510ae046-b6be-3bf0-b5fd-b016d05ee964 | -27.68664 | -48.7505 | 2025-07-19 04:14:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 97889a02-9996-3b9a-876e-88e8d15d20bb | -25.10983 | -52.73416 | 2025-07-19 04:14:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e5fc7613-851f-3434-bda3-f66f5c8dfacf | -25.11212 | -52.73168 | 2025-07-19 04:14:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ce9af746-f28c-3333-9c50-27ea54de17c2 | -25.97394 | -48.95619 | 2025-07-19 04:14:00 | NOAA-21 | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dfa1c0db-8043-3884-9c43-1e9c9670ef4c | -25.10781 | -52.73097 | 2025-07-19 04:14:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 46dab10c-1dda-3e73-9369-7e826c795e80 | -25.9844 | -48.95805 | 2025-07-19 04:14:00 | NOAA-21 | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 39d292ff-1c4f-3f9b-9cac-7ce4fb4252f4 | -25.11072 | -52.72983 | 2025-07-19 04:14:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 39e0dec0-3732-32d0-b9a4-e7b3f119a773 | -25.97465 | -48.95212 | 2025-07-19 04:14:00 | NOAA-21 | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f24f063b-d1d1-3bbf-9bb2-119e68b7f6f3 | -5.6567 | -43.7161 | 2025-07-19 04:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a02e0a04-54a7-33d7-be0d-8b9f748efe62 | -2.9108 | -48.254 | 2025-07-19 04:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 297af823-7501-3288-85d8-ae14a2a7ffa0 | -11.7313 | -48.207 | 2025-07-19 04:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 4a3ab4e9-1d0c-3868-b3ab-21661572ad08 | -11.7317 | -48.1849 | 2025-07-19 04:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| a006f5b9-f168-36f5-992f-677d100f36e1 | -2.9109 | -48.2325 | 2025-07-19 04:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 89f4e1ee-3c4b-3a9a-abd9-5f6d59daab43 | -11.7317 | -48.1849 | 2025-07-19 04:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 81aeea87-3e04-3d55-bee0-74f786304f6d | -2.9108 | -48.254 | 2025-07-19 04:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 6ee3f5e8-ff2c-367e-96e7-cecf6c5355bd | -5.6567 | -43.7161 | 2025-07-19 04:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5a1292c7-a455-3f28-b543-eda183f66ae4 | -11.7313 | -48.207 | 2025-07-19 04:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4c3a2c17-3b78-3630-9443-33c1367103f8 | -0.74634 | -47.75362 | 2025-07-19 04:32:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52305df6-f90e-39e4-8faf-3941bf599782 | -0.7497 | -47.75414 | 2025-07-19 04:32:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41fbdbdf-6c5f-33a7-bac3-ad3c3452215a | -4.12952 | -47.65432 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 658c9e70-8600-305e-ac10-3bfa7278a176 | -5.65555 | -43.72213 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8f501bc4-4cd4-3573-8ff8-6a0de87a1a60 | -7.08903 | -49.17628 | 2025-07-19 04:34:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f003da83-6df5-34d1-92ad-fc24a0947590 | -6.37501 | -43.75301 | 2025-07-19 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9508958-ba9d-3114-920f-0d5470fdc258 | -5.48448 | -43.08058 | 2025-07-19 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8286b384-daed-3173-a2aa-c85da7711862 | -8.55119 | -47.85127 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe642b83-b795-364e-999d-e79006fa1d39 | -6.15637 | -47.76155 | 2025-07-19 04:34:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5b1fa5c-518b-3c50-b387-2e52160c6abd | -7.47033 | -44.69835 | 2025-07-19 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e99d4a5a-aed5-39b7-8b39-aaa49aa5a263 | -7.94589 | -43.95367 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4db1fc84-7bb1-3bca-87cf-e8b1b92e6ef3 | -6.44252 | -45.32782 | 2025-07-19 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ed34f2b-b8d2-370b-a5da-82d67e7f9de7 | -3.14117 | -47.01104 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11edc821-fb3c-3f63-82d4-48bd564c347b | -5.92075 | -43.46992 | 2025-07-19 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0aaf95aa-d7eb-3321-8047-921ce05814e4 | -7.48702 | -47.49776 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 37638b46-d8f1-3fe6-a813-81527d365dbb | -6.72839 | -46.31763 | 2025-07-19 04:34:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed228ce6-5f15-3a68-918e-3a09105e6b50 | -8.38947 | -44.02881 | 2025-07-19 04:34:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c15d0b4-8ecb-317f-99bb-1d32b1cc0cc9 | -3.13399 | -47.01345 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e977daa3-a9a3-3572-9627-b0a73361dcf6 | -4.03088 | -48.06225 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8543989f-1a22-3579-ab95-12242a55de29 | -5.64354 | -43.72486 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 119f3757-16a3-3078-8913-0435c67db301 | -4.10637 | -48.20301 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e7183a-5efb-31d5-acbf-6f267a06c7ca | -2.99648 | -49.31991 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 132cd7b0-a00a-31c2-ac58-088570949037 | -7.08567 | -49.17573 | 2025-07-19 04:34:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8976b77f-4f1a-31a3-97fb-75c80c9ce00f | -3.95109 | -49.44241 | 2025-07-19 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d64d456f-1880-304d-b30e-e12aad329767 | -6.16758 | -48.05431 | 2025-07-19 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7833e334-c7b7-30c9-b57e-d8ee8195c11e | -3.94379 | -46.61906 | 2025-07-19 04:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce0cb1dd-a6c2-3b14-b94c-2ffb57868cdd | -4.31098 | -48.10659 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 88faac43-b6a4-3b80-9573-46e12f7cb094 | -8.38039 | -44.0372 | 2025-07-19 04:34:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cb7cb3f-7c7e-3f0f-841d-1540d7e900f0 | -7.17818 | -44.10209 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8a77796-d1ff-3e8c-86e3-90e59da044ea | -6.75289 | -44.76508 | 2025-07-19 04:34:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1e2cacc-a965-31ad-887f-677f61cb022f | -3.58634 | -47.51211 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9112b81-2b3d-38ce-a7c6-428b6a132d8f | -8.25948 | -46.07388 | 2025-07-19 04:34:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76111c74-c218-3865-b930-2a0bf30dcd52 | -4.59265 | -47.89044 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 255be95d-e1b0-3a79-ad98-546fd2a65012 | -8.64801 | -47.75534 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35aabef6-271d-390f-8baa-797a19786c5b | -4.56286 | -48.01384 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03b78ee3-eb85-3f79-9be0-b301b8040ffc | -6.15915 | -47.76553 | 2025-07-19 04:34:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe84cee4-f302-3ad2-ad68-386781068ef4 | -4.58934 | -47.27041 | 2025-07-19 04:34:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2652ef5-57a9-344d-a25a-425e64c68f08 | -8.74168 | -46.68111 | 2025-07-19 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3e1863e-4abe-3c17-9cb8-142073d5bf82 | -7.28073 | -50.33064 | 2025-07-19 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecd68782-5cd6-3086-9417-e73c44b8ccb2 | -2.90812 | -48.24673 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |


[Clique aqui para ver as próximas entradas](README17.md)
