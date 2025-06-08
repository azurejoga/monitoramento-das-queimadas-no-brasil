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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0116aefe-d327-318b-92d7-58c86bed88d6 | -11.79175 | -48.08863 | 2025-06-08 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1aa23c15-d8f1-3f60-8ed6-d38ead66b601 | -14.87474 | -48.10738 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e8e915c-0a9a-3a60-bf09-79a9e9e970cb | -11.12202 | -54.64014 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3b8086b2-2ed5-304b-ac5e-9f35d3357df9 | -13.54175 | -44.14025 | 2025-06-08 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1b517f6-d6a6-3af4-9a2c-f1bdab0e0c38 | -11.80535 | -48.09117 | 2025-06-08 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 75254d44-1e3d-3819-8455-b0e8b609f7d9 | -12.78169 | -48.71796 | 2025-06-08 04:04:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4d76dcb-57da-37a5-bdf0-6c8cc794295c | -12.06896 | -45.76688 | 2025-06-08 04:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 131ef5d8-e713-3796-8c28-6fedd90184e6 | -7.86525 | -47.90206 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7f44a0f-68f5-3850-9086-0c455df91d1c | -12.54065 | -45.41546 | 2025-06-08 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ad8634-6722-388c-ab9d-0b17b3d7c3c9 | -9.05376 | -47.91146 | 2025-06-08 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dba6e41-896e-39ed-96be-49590bee0b06 | -9.92795 | -48.695 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51c77a6a-bcbb-3880-9130-c302e7027ab3 | -9.07488 | -47.14537 | 2025-06-08 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74bd8331-0842-3b5b-a720-684b94f0bbd9 | -9.41506 | -48.45135 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 68d0f239-b253-3101-b422-f195ae44ec38 | -14.88438 | -48.1272 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32156519-77e4-3a4a-922e-c3ad5a4efe62 | -15.52558 | -42.62316 | 2025-06-08 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 17964788-07a2-3489-aea5-2d87221eea7f | -9.41021 | -48.45046 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e7698ae9-951a-3926-b6c0-791932ab8e45 | -11.12067 | -54.64678 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7cb037c0-2c68-306f-a10a-d528ea3757de | -15.52168 | -42.62618 | 2025-06-08 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1a4b2450-7751-324f-a7b4-75fe3256f50a | -12.97269 | -46.7566 | 2025-06-08 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48534694-dcee-3759-8f55-3e95941963d6 | -9.40537 | -48.44959 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 98c6c33e-cc4f-31eb-b38b-c104e0794197 | -8.54642 | -48.26074 | 2025-06-08 04:04:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9401ac66-fc2a-3d23-b715-17fd6f7629d7 | -16.40002 | -39.3559 | 2025-06-08 04:04:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| df454101-3199-3c17-af35-714b4016301b | -7.87539 | -47.89435 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b916c4e2-1975-34e9-8b45-99640e2c7e22 | -9.84172 | -48.6058 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3681aabf-47fb-3263-b0d4-3b57bd10456d | -13.54459 | -44.14486 | 2025-06-08 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e18de73a-0450-393c-a2ca-fffd41c248ea | -9.40243 | -48.43793 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 924b8b34-d813-37c0-b043-fd87e8b3e615 | -12.94826 | -46.75625 | 2025-06-08 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61943e6b-b159-3649-9cb8-6a1e29fac8b1 | -8.59101 | -45.86554 | 2025-06-08 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30c913f5-9b2a-358d-96b3-2ccea17171eb | -14.87554 | -48.10313 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f74b2a8-c136-35e5-8272-75265f324837 | -11.11931 | -54.6535 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd2ff9cc-d233-3d1b-907d-a9d88e3662e1 | -12.78076 | -48.723 | 2025-06-08 04:04:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 325eb4f8-3400-37a5-b65b-9e6ce1c742cd | -10.64238 | -44.48493 | 2025-06-08 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 245c236a-c02a-390a-ad3f-7d92b11bc968 | -13.64743 | -47.75947 | 2025-06-08 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d923152c-ac9a-39c8-acd6-32d582374fed | -14.8793 | -48.13047 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 970e5048-94c1-3ea3-8d50-f90e38b9efe4 | -11.79261 | -48.08395 | 2025-06-08 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00312636-a57a-3abe-8cb9-daa23d4b481a | -15.52501 | -42.62675 | 2025-06-08 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e128f275-9ea9-361d-b03d-c9ee511f4abb | -11.12751 | -54.64861 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e2c514d-2f17-3dfc-b539-504150ac326b | -12.98563 | -47.11319 | 2025-06-08 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ed105a8-bc45-38c5-a1bc-a5ac63dc6c66 | -7.81612 | -46.56577 | 2025-06-08 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61608b8f-277b-3ebf-9d1e-a2ebdde1e353 | -14.8852 | -48.12281 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22178005-55e8-3bd0-8f4e-43f6019e1118 | -8.37567 | -46.35355 | 2025-06-08 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d072e32e-19a1-369d-96ce-5c922ed9c349 | -12.96529 | -46.751 | 2025-06-08 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a03bb24-9a46-3591-aea2-9c35c6043f17 | -8.41119 | -47.05157 | 2025-06-08 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49e86104-ac95-333d-9eff-6551ebfec498 | -15.52283 | -42.61898 | 2025-06-08 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| da985c6c-1447-3288-a0e7-392e8d8c78e5 | -12.96934 | -46.75185 | 2025-06-08 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa86eddd-ae83-3922-88c1-ac39047dfcf6 | -15.4971 | -44.41377 | 2025-06-08 04:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c9892da-b6be-3d33-861b-2810b4d60ba8 | -9.40337 | -48.43255 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6edfae01-8f5c-312a-9c9e-3511827db0b3 | -11.7576 | -44.65487 | 2025-06-08 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f788af00-a64b-3fa0-a87b-c25f7170444f | -9.41289 | -48.4525 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2769fad5-dc10-3e29-8bb9-26f685057e5f | -7.81538 | -46.56999 | 2025-06-08 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbdec462-8504-3d9c-8567-9dab5818c4c5 | -14.88602 | -48.11843 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5deda74-3f59-3ff1-872c-d9d010a2cedf | -7.82287 | -46.50137 | 2025-06-08 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70495c30-1fcd-3bef-b05c-ca73341ebf30 | -9.06965 | -47.14902 | 2025-06-08 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ae523af-9506-3a2a-814f-0b2ac469212a | -7.87062 | -47.89344 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0abe6d92-d19e-31b6-8b27-30cd63252d56 | -10.79738 | -43.37864 | 2025-06-08 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2fea3e71-f00d-3c5a-813c-17c76082f300 | -12.96122 | -46.75028 | 2025-06-08 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 481e947e-f7fe-3ae3-b633-9f0989dc0523 | -14.87287 | -48.10767 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99c1bb23-2111-3850-8f8f-f27c5b80c715 | -12.54147 | -45.4108 | 2025-06-08 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bf877f5-c7b0-3922-bcdf-db7583d3b583 | -9.05482 | -47.9137 | 2025-06-08 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53168fd4-c394-3abe-9b23-02260c1f17ed | -7.86871 | -47.90397 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3873951a-4750-3f27-afbd-f03e9cb19df5 | -11.79714 | -48.08478 | 2025-06-08 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79c218df-bba4-37ee-84ed-3db9256cc1c1 | -11.12623 | -54.64682 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e3dc0dce-c6d8-322c-b708-f3c4d8c648a6 | -9.84562 | -48.61196 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 445c74c9-8703-38b0-aba1-62fa2f121310 | -9.05844 | -47.91241 | 2025-06-08 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc5cd06e-647e-368a-b20f-538bba66eebf | -10.64103 | -44.48239 | 2025-06-08 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 188c0158-5c77-39c1-ab98-2836c08136a7 | -11.11794 | -54.66029 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9696427e-649a-309e-ac03-56ae3b3fb758 | -12.9842 | -47.12128 | 2025-06-08 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddc5cdb6-3efe-3033-881a-ee26acd304eb | -8.5254 | -50.02675 | 2025-06-08 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 999965cb-7284-3159-b8f2-4aa5858f6d3b | -10.64528 | -47.48083 | 2025-06-08 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3537fa86-938b-3074-ac2b-9238cb05577b | -10.75383 | -48.5841 | 2025-06-08 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de548e99-e1e7-3bcf-a9da-9e83e8474a74 | -11.63012 | -48.48834 | 2025-06-08 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 30ddbbb0-74ef-3429-83b7-60ea3504b43f | -7.87187 | -47.89238 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0c96b73-3b98-398f-b9c7-8ee715c42f3b | -9.41388 | -48.44708 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 17e4c332-68d7-31e0-844e-48dd6c26ac9c | -13.55201 | -43.49631 | 2025-06-08 04:04:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed2f92ba-9596-3042-a6bf-8ae27acef72c | -11.79629 | -48.08946 | 2025-06-08 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24f0ab26-9f79-3669-9a55-d66124f9f9d5 | -13.95322 | -43.52068 | 2025-06-08 04:04:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdca0100-4a92-3e14-87e9-01987c58fcee | -14.433 | -50.64948 | 2025-06-08 04:04:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e7d68d8-071a-34b9-9be6-2ebe8e9eebb5 | -8.59513 | -45.86634 | 2025-06-08 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 401bec53-8da9-3260-87ab-c9987af8b49c | -7.86137 | -47.89595 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 458be698-fbfc-33c3-a277-be01d21c8b17 | -13.18894 | -43.55256 | 2025-06-08 04:04:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 324b763f-8668-35b8-a5f1-cb0625407d2a | -13.28543 | -44.18042 | 2025-06-08 04:04:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5ccfa0c-18f6-3651-982d-f32903341fe4 | -11.80168 | -48.08561 | 2025-06-08 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f07d0d6f-01fe-319a-86f0-f44ca1823ead | -14.43361 | -50.6464 | 2025-06-08 04:04:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2efb148-2b76-34c2-9ef9-5ff723a0702f | -7.87095 | -47.89766 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 268ecce1-3d92-3f89-9431-fdc2a2d8563b | -11.11799 | -54.65176 | 2025-06-08 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 21d33282-cf30-35be-a3eb-d5279df5f8cf | -9.61028 | -42.08297 | 2025-06-08 04:04:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c69f8c2e-e947-39c5-b186-80050cc0669b | -9.40904 | -48.44622 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 79fac1ed-baf0-3bf0-a469-2ee62dc8e2b5 | -8.116 | -47.61479 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3302ddd8-bc66-37cf-864f-a9f173ae79d7 | -8.52604 | -50.02326 | 2025-06-08 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 80f73ae8-cc84-320b-8d91-ad9f0fc4aa0b | -10.75476 | -48.57896 | 2025-06-08 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a51ddcf-b276-3f20-ade4-ac7e88f97050 | -14.88015 | -48.12599 | 2025-06-08 04:04:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fadbbe1d-684c-3fed-8afa-026829dd241a | -12.2104 | -49.63541 | 2025-06-08 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be78dad6-3f51-3d05-a619-1d8dd149106e | -9.40232 | -48.4284 | 2025-06-08 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf5631d7-f23d-3789-a6ab-d827e018d93b | -7.86966 | -47.89871 | 2025-06-08 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11e5b5ac-b653-3b6d-ae14-fce3dfa5f3c4 | -12.20956 | -49.63803 | 2025-06-08 04:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cf0333f-b39a-3424-baeb-2e8edfaac982 | -18.02567 | -47.38596 | 2025-06-08 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06bf6ac3-f8ed-3ed0-b73a-b6650009a3fc | -20.65938 | -50.10829 | 2025-06-08 04:06:00 | NPP-375D | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33af458a-e449-32c7-a8eb-69dd9fb944a6 | -16.26422 | -48.80967 | 2025-06-08 04:06:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caef4b91-f092-3a35-819e-fc2eaf629290 | -13.88033 | -56.20345 | 2025-06-08 04:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51e1682b-ffef-3e5d-ad1f-bf9cb4d60425 | -17.77979 | -42.80821 | 2025-06-08 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
