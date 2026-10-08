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

## Dados Diários - Página 298

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b94c8f3-b903-3649-99ef-429eb0f4b6b7 | -6.13894 | -47.94754 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e13f108-06c6-3ec3-874b-277245f423e0 | -5.69431 | -53.49392 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| c810e61d-679f-34d0-8d98-d71337ba3309 | -3.90773 | -44.38726 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 881ff58e-9db4-34da-8f5e-41120aac6faa | -7.76734 | -44.17605 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5a623550-db67-3a71-984f-c5805f63d478 | -5.5434 | -43.22778 | 2026-10-08 16:20:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b6112cba-3733-357b-a125-ff5e3dc64d2f | -3.13383 | -42.93147 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55c7080c-e214-3a86-b311-7ebb7ab86154 | -3.2609 | -54.03712 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 09255b33-2de1-35a9-9e4d-afcec08aa1e9 | -6.57433 | -44.86246 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 65f6b116-4395-3313-a9f8-842196ea1219 | -3.29132 | -42.28405 | 2026-10-08 16:20:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cddf3eb5-84b2-340a-97a3-d7031fd06ff1 | -5.67842 | -46.35308 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9a1ffadf-aef9-3289-a945-d55742516966 | -5.41027 | -45.86596 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd3b50ca-0488-3574-96eb-3d6a0e69596b | -4.12278 | -38.35815 | 2026-10-08 16:20:00 | NPP-375 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 17bff1e4-ce67-3f8c-b391-503c54193884 | -5.37347 | -44.21066 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 8edef487-5a84-3b2f-8fac-6365d6196e5e | -7.20536 | -46.52929 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b30eaf68-775e-3658-960d-2f4825053202 | -6.60701 | -37.89886 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 27.2 |
| b4a30c4e-7682-3913-9a5e-26a0de4b0e78 | -3.37301 | -43.02674 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dbc95911-12ec-31d2-8611-1c15c355fe68 | -5.53232 | -48.17709 | 2026-10-08 16:20:00 | NPP-375 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 211171c6-66c0-32f3-875a-8a4a19c5eacd | -6.33626 | -44.43588 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 526b7dce-0473-3691-8859-29ede4eedf7d | -5.7064 | -53.47313 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 3c15852e-0baf-3c07-b255-0f59e13024d5 | -6.84924 | -41.75782 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| d8fd9531-d153-320a-868c-86e1a8a17cf4 | -6.8298 | -39.55735 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 5b47b855-df91-3b37-8588-7e684ac30b91 | -2.08198 | -46.58485 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c29e9a0c-4e26-3e87-aa08-f8c75ed287d2 | -7.38699 | -46.20473 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e3b494d7-63fb-3720-a665-51cbc2c8a7f6 | -5.96487 | -40.91338 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 0eee0f36-46ff-3f89-bd37-97b9e7b24da8 | -3.18074 | -50.58906 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6cf904e3-e758-3e55-b9d1-878ed4847acc | -7.10578 | -45.24252 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b69e7bc2-5437-3894-94ae-325a4d1a7116 | -5.99067 | -42.71177 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 93d6855b-afd7-329c-8e38-4c33f367956b | -3.81855 | -44.59952 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f9b07499-b534-3e1f-bf02-6fd647692b76 | -6.14836 | -47.9254 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7cc7a20c-5204-3cd1-97b7-0b3d58d3d6cb | -6.57057 | -44.10828 | 2026-10-08 16:20:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a88e7467-6957-3f87-a76b-5e25f6b1020a | -6.96113 | -47.66453 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0c990a51-b959-3ffe-9dff-5146406eaa7c | -7.58205 | -46.20307 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 655e23c5-fc7b-36ab-aaeb-a2cb44ff8ae7 | -7.70502 | -45.43833 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f1084d8f-327f-3e3b-8901-a6958f2f99e5 | -6.33203 | -35.15674 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| be09a53a-fa6c-3d8c-a099-7dde41ffa876 | -2.98634 | -54.06921 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 59ff9817-daf3-3ee5-96f9-27ee52619bce | -5.29143 | -48.10738 | 2026-10-08 16:20:00 | NPP-375 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36981b07-c423-32f0-917c-1a59b62700f5 | -3.08675 | -53.93612 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 86531f17-67c9-32f2-a31d-24e21d53088a | -4.69521 | -50.64019 | 2026-10-08 16:20:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b649e09-05fd-3c91-a935-714ba57eaa18 | -5.37525 | -44.19483 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 3fd0cd72-32f5-3ea1-9d5a-c2ea871072d7 | -2.9974 | -41.42529 | 2026-10-08 16:20:00 | NPP-375 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7ccb33c8-c139-3395-96b0-35cbdb3d174e | -5.73273 | -41.77831 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7b8b9e40-184f-3893-938c-3c0947232a6e | -7.51654 | -45.77351 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 93ed1888-b017-3238-98cf-3cad404b3fd5 | -6.53565 | -45.38444 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 5cc045d5-12e7-30b8-bca6-47817aafd3eb | -6.1492 | -47.93151 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e910803b-361e-34b0-8aa0-ccbf08053018 | -5.62779 | -43.04684 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 724aba08-10a9-33b7-90de-e69e77ebf783 | -6.79556 | -45.05505 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f029a5eb-bf20-3430-bcb3-1a528410fe31 | -4.35489 | -43.80564 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 753bb075-606b-39df-b25e-abce325385bf | -6.84807 | -41.75001 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| bf404b8c-7bf3-3f87-b1f9-90500b881d71 | -7.47898 | -42.79596 | 2026-10-08 16:20:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| b624b3cb-c2b3-3418-9d76-8d63c111072f | -3.90807 | -44.38941 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f268fe49-f75d-306b-937e-ca0880eeaff3 | -6.20295 | -51.43731 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8d085e91-bdc4-34d2-a1d0-7b2d513784ff | -4.68665 | -42.92722 | 2026-10-08 16:20:00 | NPP-375 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 07cc69f7-efb8-38f7-a7a2-a851f3b377d4 | -6.33393 | -44.87009 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6eddf187-a419-34ba-ae64-79c2a60f6e2a | -1.97207 | -46.21651 | 2026-10-08 16:20:00 | NPP-375 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4cdf952c-8327-3b26-b90d-9ec1035735fd | -6.7007 | -45.29021 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a7d40d96-dc9e-3fe1-a57f-030010dd86c7 | -5.77946 | -45.37999 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e12f9b43-3a68-3caf-9229-47a1b8ca38de | -7.06079 | -40.94215 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 319b30fb-f7a0-36c4-9ccd-23f160258c5c | -4.21631 | -44.80204 | 2026-10-08 16:20:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd33c037-f4bc-3e94-a125-faf3c8efb00a | -6.85041 | -41.74169 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5e2da9a4-f7cd-3a21-92d6-43508e593f15 | -1.92722 | -45.23575 | 2026-10-08 16:20:00 | NPP-375 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 721de5f7-50f3-38c5-bc29-e79db04b0664 | -6.93482 | -43.67126 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 0b19cc5c-581a-3c7f-a352-8773ed90ab46 | -5.53182 | -45.20789 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7de9eca-b078-38f5-9c3d-4b4933f37104 | -5.1195 | -36.86657 | 2026-10-08 16:20:00 | NPP-375 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 01f6b113-548b-3ef2-b9e0-4cb3e50217be | -5.7051 | -41.6886 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d18ae95d-aa48-3867-8729-9a52067ecb02 | -4.08914 | -44.09931 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 612fad67-715c-39d6-9fe8-75d08f3aad7e | -2.50864 | -47.37751 | 2026-10-08 16:20:00 | NPP-375 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 76b61ba5-c133-3bea-9aa9-9f7fe29d963f | -6.83032 | -39.5608 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 699b2faa-c6ee-38b2-8757-269d297c463e | -6.53304 | -45.39748 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ee9ec07c-8ef0-3a17-a50e-24b002b4d7c8 | -6.40519 | -37.79337 | 2026-10-08 16:20:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 055c6083-09a2-300f-8ff4-83909449154b | -6.97213 | -47.66864 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 11e6d56b-b3ea-302d-ab29-687c45e8e0c7 | -6.23034 | -35.34039 | 2026-10-08 16:20:00 | NPP-375 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 320ee1f9-f8be-3977-bd0a-c3cbec1970cf | -5.70902 | -41.73873 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a4cd3ad5-6bb0-3bce-98eb-7e3a06abec61 | -4.69029 | -42.92669 | 2026-10-08 16:20:00 | NPP-375 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 50bebf01-87f0-3f6a-9b16-629887421e60 | -3.29311 | -54.00277 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6ae50a9b-7581-3534-97ba-b2a4076607ac | -6.01701 | -42.26038 | 2026-10-08 16:20:00 | NPP-375 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4d9f0fb0-16d6-34cc-af36-054bb9a22cf6 | -6.88724 | -45.90588 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3b921a35-cb51-30dd-a7cb-1261608d8efd | -7.18489 | -44.3241 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dcb6e16a-3448-339d-9a86-195d4f4b7101 | -5.26478 | -47.92418 | 2026-10-08 16:20:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df018522-9cc0-34aa-87f6-cafdec84a49f | -6.95558 | -45.28638 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a6f81b3b-1c44-3a53-afe9-e345c7adced3 | -5.8816 | -43.45709 | 2026-10-08 16:20:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c7d3899a-199b-3a5a-8c10-55fbb5d4c7ad | -6.3136 | -35.14017 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| ee8eb506-c834-3cf5-bc8c-e6bdc69f0534 | -6.68815 | -41.76472 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c5fbb838-b70a-3ec3-923d-168e409a77d6 | -7.71645 | -44.73274 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 867f9489-cc45-3728-819f-4ee268651cfb | -7.87936 | -44.24042 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| eea182d6-7c0e-3667-918c-5dd40c4649c2 | -6.42667 | -44.82532 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe568019-f304-3b28-886b-7a0020eb2bce | -2.74378 | -54.13857 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 19a64e68-61e7-357b-87ca-10ac8dff9f0b | -4.79656 | -43.13678 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 96787618-a777-3d1a-bb75-8c73c6d5b464 | -6.14101 | -47.94853 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c15a23e4-2854-33de-9bbf-8bde85ae3be4 | -5.34817 | -45.71827 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a97a35db-9164-3c60-8089-75a198b9fc9f | -6.66184 | -51.82389 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0b9e3fb-9b2c-3988-88c6-ed95d18fea7e | -7.02795 | -44.7887 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5240488e-67b4-387d-bb1a-fde4f7d560ad | -6.89111 | -45.90067 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a15e9954-ec03-3082-b612-02d77acbeac7 | -7.03247 | -44.91142 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81360fe0-38b1-36ff-a214-972e62c41e6d | -7.3818 | -46.23494 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| afec9267-4cf1-3e5c-8ec9-9577033cb4d6 | -7.48123 | -45.95354 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d0ad1f6e-9a1c-3ccf-b513-d02c70e96969 | -5.55075 | -45.57303 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0668b02e-6e4f-3b70-8a81-af90f7af8ecb | -5.37653 | -44.19711 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 85ec68ec-70de-3712-815d-c5c0b13aba26 | -5.87117 | -45.96705 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| e5b2bdb8-f762-3c34-9627-66d11dcd1c73 | -6.05896 | -42.91736 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 0e934a38-6eb9-3d7a-a53c-f2d51d2fc3fb | -5.49816 | -40.53966 | 2026-10-08 16:20:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 21.1 |


[Clique aqui para ver as próximas entradas](README299.md)
