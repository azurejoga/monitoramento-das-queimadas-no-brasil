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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b977d996-9c77-3d6a-ba34-84cabdaaf1a3 | -13.60531 | -47.31271 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ff68cf9-385b-382e-a682-e1ede894e152 | -16.71221 | -51.47945 | 2025-09-27 03:57:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0412388b-92e0-36f6-bbf5-b77715f2c00d | -15.27248 | -46.44512 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9acb17c6-f282-3d06-8d22-1bd0e7f839cf | -22.5799 | -48.575 | 2025-09-27 04:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.4 |
| 8ef96cc4-1c0e-3f2a-aa27-b6b8bd6b875c | -11.4417 | -44.9767 | 2025-09-27 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d1d19cba-d5e5-3b84-a8a9-ce7027f66f80 | -22.8623 | -51.7723 | 2025-09-27 04:00:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| 91853fbb-b49c-3bd9-a273-bf04da5d9e2a | -9.9328 | -59.9247 | 2025-09-27 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ff4484a4-1274-3b81-8101-2dcfd008cfa1 | -22.5792 | -48.5986 | 2025-09-27 04:00:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.8 |
| bf7b8470-6ce7-3260-970c-820dc945031b | -22.6009 | -48.5698 | 2025-09-27 04:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| add4224d-7456-3f0d-94ee-2eb503ca865f | -23.6917 | -51.78071 | 2025-09-27 04:00:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| dbf7a25b-06da-36b6-a706-ce92a064af4d | -22.52715 | -48.73531 | 2025-09-27 04:00:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78794184-5839-3936-a3f1-cc3fc0de692b | -22.85963 | -51.78587 | 2025-09-27 04:00:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 892b83b7-99b5-33ea-a379-ce13a394674d | -22.56443 | -48.61407 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 58bace28-12db-3c2c-863d-0a5d8a83c88f | -22.85533 | -51.781 | 2025-09-27 04:00:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| ddba552b-84f9-3dcc-a3b4-86d108682309 | -20.99547 | -50.00648 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4e11513f-93c7-39a0-b6ca-3419d2d9f3a9 | -22.59727 | -48.58134 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| caa0b193-a05e-39c8-ad05-0abdc6f2c0fc | -22.49786 | -52.98514 | 2025-09-27 04:00:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| cf1036d0-5f6e-3d5e-b335-f56442c24fd6 | -22.85608 | -51.77758 | 2025-09-27 04:00:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2dc2ae89-6ced-36b4-9c7d-9a91635f01ad | -22.58294 | -48.58713 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 56a14e67-f60e-359e-8b08-31ddd252aacc | -21.0047 | -50.01046 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 92c0603f-2032-33f1-82d3-34b329fe4ea0 | -22.57035 | -48.6064 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| eca09ecc-bd78-30c9-8aff-e578c49ca623 | -22.72014 | -51.39801 | 2025-09-27 04:00:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 8518e961-6717-37b5-8436-e2291ae722fe | -24.55702 | -50.69035 | 2025-09-27 04:00:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2eb1ad59-f118-3996-87e2-299c4c02295b | -22.53142 | -48.73624 | 2025-09-27 04:00:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 065d1f5e-5bc6-3790-9bea-d61b6e75b0db | -22.59389 | -48.5761 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 7c355c63-f345-3694-beff-b94f6d0bb6a8 | -20.88617 | -56.60983 | 2025-09-27 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 8658eeb5-796d-3f9a-9345-fda150d7bfd8 | -22.60534 | -49.0286 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89d83385-50a2-3ef1-9b73-edc77c6c2b13 | -22.59919 | -49.0368 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2e97bd8-1ba2-3105-a0c6-a706fa60261a | -22.61395 | -49.03086 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 249f9a2a-b910-3e7a-ae1d-7dc05fd06b8b | -22.59054 | -48.59328 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a2f08c06-bd3d-3526-89e0-e177b8f7aee2 | -22.85455 | -51.7845 | 2025-09-27 04:00:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 8c350607-e178-36e8-8a3a-660113b146f3 | -22.58211 | -48.59138 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 7e37bf79-42eb-3eea-adda-b015301b0a3d | -22.49132 | -47.03262 | 2025-09-27 04:00:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d6a06aa-cbd3-3834-84fc-4b978b4e70bb | -22.26895 | -46.42598 | 2025-09-27 04:00:00 | NOAA-21 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 634662aa-a02b-33cb-9515-3875e852f5f3 | -21.0035 | -50.01616 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b79cce4d-ca3c-38cd-88eb-f0c89c5c0297 | -22.88007 | -51.23821 | 2025-09-27 04:00:00 | NOAA-21 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ac7b239e-75f2-337a-8c15-aede79aa4a20 | -24.89553 | -49.58253 | 2025-09-27 04:00:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb5252b0-9073-3f33-ad02-69c0d70b65b0 | -22.8604 | -51.78239 | 2025-09-27 04:00:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| a8067845-129b-31e3-b557-49ea7d220210 | -21.00493 | -50.00885 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8e1e8676-c861-34b7-8215-57a7ecc75001 | -22.22693 | -49.72739 | 2025-09-27 04:00:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9364e60c-6686-350d-a140-6e196a19ba74 | -21.48799 | -46.91394 | 2025-09-27 04:00:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5788647c-215f-31a3-b293-36f3de53a488 | -22.59812 | -48.57701 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| c29ebdb2-4a33-3a3e-96c5-034704af1acd | -22.49877 | -52.98114 | 2025-09-27 04:00:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| c826ecd0-b118-367d-8c03-e6856d9b75fb | -22.57539 | -48.60316 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| dbe4a7b8-c59c-35ac-bccb-1c1c9552e495 | -22.58883 | -48.57954 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| d6d5eb41-8946-3bb8-82e7-3b303fbe5149 | -22.26908 | -46.42265 | 2025-09-27 04:00:00 | NOAA-21 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 36ac4bea-a5f2-3a11-906e-2eb2aaa50438 | -22.61923 | -49.02703 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 540fdd49-b8f5-344c-8abd-b8bd18b9f729 | -22.58633 | -48.59231 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 4fc71d2e-bd98-361f-81b5-811878933666 | -22.57119 | -48.60212 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e1e7c396-aa1d-3b59-aa44-dab89a8a072b | -22.61212 | -49.04006 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6af235c2-6de8-31d7-ad6d-2130bc9dd726 | -20.88796 | -56.6027 | 2025-09-27 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 34.0 |
| ecdec30f-7c15-3677-9d1a-7da844988831 | -21.0002 | -50.00765 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 59765728-7309-38b2-a72b-cf8aa72a90c9 | -22.5263 | -48.73964 | 2025-09-27 04:00:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 55bc8115-2260-3470-97d0-e52375c72eb4 | -20.99905 | -50.01332 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 09df7de0-2f51-3082-acd8-62543220dfe9 | -21.4841 | -46.91308 | 2025-09-27 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 064d16fa-9233-3010-bcdf-3927612956c4 | -22.588 | -48.58378 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 747585dc-ccf6-312e-ab36-6325e8213d68 | -20.98954 | -50.0112 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 72bb73c1-7481-3816-8d65-9830c1467e3a | -22.83094 | -47.25021 | 2025-09-27 04:00:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2a45c307-b912-36b7-93e9-97fc88918216 | -21.27602 | -48.32898 | 2025-09-27 04:00:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d2ddd6c-3dfa-30d4-b676-2bba34b5b89f | -21.24825 | -48.58286 | 2025-09-27 04:00:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 17dcd50c-4e53-39be-9832-ec77f51b1372 | -22.71516 | -51.39671 | 2025-09-27 04:00:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d57d874f-9dd3-33b8-83a2-6cbd0f072e63 | -22.59119 | -49.0542 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 113c1882-10e1-3164-8958-57ea35d32ab6 | -22.3181 | -48.59584 | 2025-09-27 04:00:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fb7ffaa7-5d63-3c2e-ac50-5facdec39e28 | -22.72084 | -51.39482 | 2025-09-27 04:00:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 6a14ef11-6240-39ae-ad46-63d6074bafe2 | -22.53057 | -48.74054 | 2025-09-27 04:00:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fea14ed1-fe76-39ec-89da-3c0158441e0a | -22.56697 | -48.60118 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1b30fc28-d7d9-3d28-8544-2ddf75b4ddba | -22.72223 | -51.38845 | 2025-09-27 04:00:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 4e2275db-0c81-3c76-9561-1b079b82e7b1 | -22.58684 | -49.05328 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be4b76cf-a1e3-3615-b35e-02920e2d273c | -22.72153 | -51.39162 | 2025-09-27 04:00:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| b109d040-9bad-3c8e-a297-936a8b8dde9d | -22.95335 | -49.89984 | 2025-09-27 04:00:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c06d1f6-55c1-3d3d-9bf5-217a58764a88 | -22.59306 | -48.58041 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 45c57176-333f-33b2-a090-75cbfefb048f | -22.61736 | -49.03646 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e64b006d-add7-3f9c-a435-14a6178c958f | -22.59222 | -48.58471 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 63524da6-9ceb-3ee4-9923-300881736a9f | -20.99431 | -50.01218 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 34985c09-32ed-3038-abc9-4e9c42d8aa84 | -22.50429 | -52.98253 | 2025-09-27 04:00:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 882515e7-1262-36a1-9072-4cce2cf0cb00 | -22.38132 | -49.48358 | 2025-09-27 04:00:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eafa6f88-2f6d-3c0f-9c24-77edced90469 | -23.06423 | -47.19453 | 2025-09-27 04:00:00 | NOAA-21 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a561649-4cea-3221-b56f-b66f9bc64bb4 | -22.60628 | -49.02388 | 2025-09-27 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66dcf9e7-f967-3f51-96b5-874e77fbdb4f | -22.58127 | -48.59565 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| aa6de84e-85c2-3483-b454-acfe92d826f2 | -22.57201 | -48.59792 | 2025-09-27 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 50c72fec-716a-3e7d-880e-ca7f7a9f89e5 | -21.00377 | -50.01455 | 2025-09-27 04:00:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 132839c5-ac8c-37a6-81f0-c8780b0f94ed | -24.55814 | -50.68503 | 2025-09-27 04:00:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 204991fd-932c-3714-a8ba-41c7b395b349 | -22.59138 | -48.58899 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| bae5873c-ac3d-3b5c-945b-b309224f7993 | -22.58717 | -48.58802 | 2025-09-27 04:00:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| d667e5bd-078e-31b7-bab1-429c391b2e83 | -22.86116 | -51.77894 | 2025-09-27 04:00:00 | NOAA-21 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c9b53f55-b89d-39c8-905c-ecccec2b4247 | -22.35755 | -49.46248 | 2025-09-27 04:00:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c36700f-fba9-3864-8277-998e5bf12905 | -25.1503 | -50.14898 | 2025-09-27 04:00:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6b4773c-9811-33a3-8516-f51c1311f3ab | -22.88628 | -51.23349 | 2025-09-27 04:00:00 | NOAA-21 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 31d201ce-91d0-30e0-83c9-a6279252891b | -22.35659 | -49.46717 | 2025-09-27 04:00:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a3dd8d65-40c5-3f2e-bfa3-13fbb668030a | -27.93874 | -51.58271 | 2025-09-27 04:02:00 | NOAA-21 | TUPANCI DO SUL | RIO GRANDE DO SUL | Brasil | 4322186 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4d12ad8e-d183-366a-a1ba-480bad71ebb4 | -27.62239 | -48.65509 | 2025-09-27 04:02:00 | NOAA-21 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8eba2561-1e12-3118-9023-ec9d881e5245 | -29.89666 | -54.66358 | 2025-09-27 04:02:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 28c7b015-6100-3861-970b-c83b6449d9ff | -30.40473 | -54.26495 | 2025-09-27 04:02:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| fd577dd1-b650-3690-a9e5-b9c5f82a8468 | -29.90185 | -54.66508 | 2025-09-27 04:02:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 72c71335-79ef-3a31-b519-5820290b5ff0 | -30.40285 | -54.26451 | 2025-09-27 04:02:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 0d43b96e-8fdc-3900-8925-c3ba99532db0 | -28.58249 | -50.55919 | 2025-09-27 04:02:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d943857b-2072-3ae9-a71a-21361a9dd661 | -22.8617 | -51.795 | 2025-09-27 04:10:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| 2d18859d-4473-3f74-bf66-8bcee7cbe4cf | -15.462 | -49.6303 | 2025-09-27 04:10:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0cd2ee30-51d4-36f1-bfc3-a362397e0367 | -22.8623 | -51.7723 | 2025-09-27 04:10:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| d4ba9b4b-5130-33ad-b340-f7cb475eb777 | -22.6009 | -48.5698 | 2025-09-27 04:10:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |


[Clique aqui para ver as próximas entradas](README25.md)
