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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ddd0bb6-4a8a-3a71-8803-8ec026cfd08c | -6.39206 | -53.34103 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46d39bd7-8c1f-3e97-97f2-a02d4fe8ea24 | -7.93475 | -44.09496 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 73428fc4-3385-3f05-b7cb-b37eb02fe482 | -5.40599 | -45.28837 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f13d640-9139-3701-b625-833f355a8006 | -3.0879 | -52.92363 | 2025-07-29 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 778aab44-e266-3649-911b-9d28b930a2a4 | -6.49978 | -56.21304 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63b7fc85-1efe-3fb7-9e0a-ee9d97aac851 | -3.08718 | -52.92289 | 2025-07-29 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6d6a3dc-41d9-3280-8607-db59d2e3fab7 | -7.80782 | -46.57983 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e497a894-5fdb-3106-9a3d-2a80399e9bbe | -6.50609 | -56.21173 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 987c990c-c684-38c8-be46-832462f2e9d1 | -2.56118 | -49.11685 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0e51476-358d-365d-a35e-54179c984e9a | -6.38541 | -53.34913 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d595051-158d-3ac9-9b67-0e8746950e42 | -5.41153 | -45.29636 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43f2f507-344a-3003-bd78-5eab97468a9d | -2.39213 | -47.62341 | 2025-07-29 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d8c9775-9cb5-3cb1-b0fc-a50799888321 | -7.92806 | -44.09392 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee86776a-130d-33d1-9143-e634fa0b8f0d | -6.4009 | -43.37235 | 2025-07-29 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23707a4d-5fc1-39ae-9ab6-ef6ea4dbafc9 | -6.41198 | -53.3167 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48f648dc-d0c4-3321-97a2-219dcfe8fe8d | -7.24825 | -43.05718 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bde8bc12-5ca7-394a-b506-21117ef04cfb | -7.85791 | -46.73223 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0dc65b38-b9dc-3141-a540-1317416c6749 | -6.39415 | -53.32913 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59ad4910-8f70-3d7f-a40b-9af8fbe5ee95 | -3.74307 | -49.04387 | 2025-07-29 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88ddba0f-375a-343d-88c1-19e121492c32 | -5.62156 | -45.10609 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7788fd3c-569a-3f2b-8e13-1d7978d160ac | -7.82938 | -47.08566 | 2025-07-29 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 953865e6-46e2-3227-b8e4-d68831847243 | -7.85907 | -46.72498 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a6bff653-69b2-3967-a448-0de60129b646 | -8.22597 | -44.91598 | 2025-07-29 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c0b0967-b618-3462-99d8-05a9851371d0 | -3.82369 | -41.55445 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f3b7007c-2e36-3b9f-bc86-916824a8cc54 | -6.38646 | -53.34313 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 875c27b6-590c-3964-bc14-21e2742a913d | -8.22266 | -44.91546 | 2025-07-29 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2854ec2b-f12b-33ee-89bb-182aab0e87d9 | -6.49389 | -56.20955 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2c5da49-5acf-385f-b08b-ca6beaabc3df | -6.26208 | -44.40382 | 2025-07-29 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5a9038c-0330-35bc-aae6-69e0bba69ec0 | -3.58164 | -47.52158 | 2025-07-29 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3953e18-86e1-332e-8b4e-e5f10af24bd6 | -7.11483 | -44.47406 | 2025-07-29 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d516d08-0612-39ec-828d-de2b49bfe094 | -6.38854 | -53.3313 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be58a74d-c570-353b-9e3c-f2a155b15f47 | -7.34079 | -43.73658 | 2025-07-29 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 743e4124-b36c-37f6-84f2-f744022708b4 | -6.27236 | -44.51182 | 2025-07-29 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08ec3b52-3681-371b-aaa2-d93020b0ab7d | -3.82662 | -41.55896 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 357a7cdf-29f2-33fd-944a-20d52010f5b0 | -7.92301 | -44.0822 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92448199-4ca0-3680-a842-acea54149a20 | -7.45643 | -49.39823 | 2025-07-29 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 47f79cb0-420b-3a69-836c-fa590251941a | -6.38699 | -53.34014 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc5e0d00-9be2-378c-a9ae-0372d6143888 | -7.24025 | -43.06361 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5a1dc9ca-a26a-3d7d-a7b7-94bada82c1bf | -6.3966 | -53.34495 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e929f0c3-0db0-3ef0-a5d9-2afab95f27cd | -3.18248 | -48.80579 | 2025-07-29 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dad559f6-5416-3a06-bfb4-9d7fe759e0dd | -7.20471 | -43.43176 | 2025-07-29 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 87e88623-63a9-3a98-a8e0-1a8d648469a6 | -8.48935 | -45.53734 | 2025-07-29 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 15cd9b5e-0d6c-3b7a-8925-3e0cd9766f6c | -7.73883 | -51.10644 | 2025-07-29 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a18a8b64-f5fb-3dc8-8afe-26e51b5ae598 | -7.64909 | -43.85378 | 2025-07-29 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 592229a4-7290-38fc-a2f1-1bbbebb58eff | -6.39449 | -53.35703 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e8f18e5-0cc0-39d9-a2c0-e37f6f0fb527 | -4.01886 | -41.79506 | 2025-07-29 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3de2ec4-d77f-3e53-9c99-8ee764ba1dfe | -6.50444 | -56.22106 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0225a1ab-8952-3875-9613-65200c6a2617 | -7.33835 | -44.6979 | 2025-07-29 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 883d385d-b748-3006-9d20-f40d3429f0b7 | -5.99372 | -52.20185 | 2025-07-29 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9bea067-13fd-3455-aec4-b8b466870aeb | -6.42148 | -53.35223 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69ba2af4-e7ce-3cef-8cda-a2a80675d911 | -6.09243 | -42.93378 | 2025-07-29 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c46f9e97-e7d5-3261-8aba-9ad9e1a4655c | -6.38137 | -53.34236 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 812dbbb2-1dcf-34ec-8e73-0fde04e42f4a | -7.25681 | -43.07 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 87bb8c68-e664-3aa4-b0e6-ee3aba4e1e48 | -6.38594 | -53.34613 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be403efd-ec54-3aac-a61e-60bf05f01259 | -7.2471 | -43.06466 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d2c6367d-78d4-3ace-aaae-310ff207af1a | -6.40519 | -53.35569 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8df330e-d5e9-34bc-91e6-4a92ea5c46b4 | -5.48512 | -42.15508 | 2025-07-29 04:19:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3e7d94f5-45e5-3bb8-a697-45c0a0ce4d6d | -6.49539 | -56.20271 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74622a52-2b57-30bb-b678-855608fbc9b6 | -6.50064 | -56.20843 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d26565e-180c-32db-98dd-4eb8aeffadec | -6.39154 | -53.34401 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57f9d499-9653-383c-924e-b566ba2c8b86 | -6.5 | -56.2106 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34a0b5d8-6e8f-3248-876f-54787e981b65 | -6.45141 | -53.36055 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eef4c1cb-b8c5-3dd4-b407-173d0eab7475 | -6.42096 | -53.35524 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcccf90e-2dcc-3fdf-b4be-06a8d92a3000 | -6.70407 | -44.33863 | 2025-07-29 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5fd6977-11ba-3a98-81d6-7cf496d4ba40 | -3.08843 | -52.92047 | 2025-07-29 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bb733df-ddc2-3e39-b8c3-fd910be67d1d | -6.39501 | -53.35404 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cd5f6ef-362e-3758-9c54-cef4a9725be3 | -8.03909 | -46.89598 | 2025-07-29 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68ec3810-9b0a-3d5e-b8b4-54090aa86200 | -2.48251 | -49.36934 | 2025-07-29 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a2d0cd8-cdcc-3523-b2ac-aa7d34ddcea8 | -7.03956 | -49.30186 | 2025-07-29 04:19:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96465d89-2eb2-3d9a-86db-5e38cb279dd9 | -7.30844 | -49.25443 | 2025-07-29 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 360cdebd-6720-3e56-ab03-c5a990f238c7 | -7.80502 | -46.5757 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20fc58b5-2f3f-3654-834c-28d59aff85d8 | -3.31638 | -48.72176 | 2025-07-29 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b80edc9-2af2-3a85-a2f5-3e41f421d008 | -6.45501 | -53.36085 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50fa7177-9b3a-3b4e-a5a0-fb23ca4d002f | -3.7462 | -49.04959 | 2025-07-29 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97668217-c8b3-37e5-9239-a453dfd74ce5 | -2.89102 | -48.29308 | 2025-07-29 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2cadea54-5adb-3fa9-97ea-02fbfdbe0986 | -7.73457 | -51.1057 | 2025-07-29 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9be96a85-2bc5-3875-8e3c-6c1ef4a034c9 | -7.81474 | -50.22387 | 2025-07-29 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f87fc978-1d5f-3522-88fd-631d0f86f3eb | -7.25338 | -43.06948 | 2025-07-29 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4155bde5-87c2-39b5-a57a-b71ad1f8ebb3 | -5.40876 | -45.29236 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 704aac8e-8dbd-3733-911e-3f80c245ca81 | -8.29055 | -45.00494 | 2025-07-29 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05c57b97-f4cd-3bb4-83ec-fe17ba9c2ad1 | -5.36756 | -45.22902 | 2025-07-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffead182-b722-384c-944d-dca60d62ec3a | -3.25269 | -43.26588 | 2025-07-29 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4f0fa0d1-8a4f-3098-a5f1-6d713a0edcd0 | -6.52504 | -56.21276 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 50740629-febe-3f4e-bf45-fcac6c0b1d09 | -7.92192 | -44.08933 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4864ef8-f86d-343a-b105-9fd9bc78d24e | -7.07224 | -45.46423 | 2025-07-29 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa95b214-199e-37a2-a15c-0c94c8fc2537 | -5.27483 | -44.47489 | 2025-07-29 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e36a6822-8a99-3047-b0bf-b3651fdd4d71 | -7.45901 | -49.39624 | 2025-07-29 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f15d8c55-27bd-3d58-a7c2-4fc8a7f1d025 | -7.93529 | -44.0914 | 2025-07-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3ffd6ad4-01fa-3836-8799-b82387a766ea | -2.89178 | -48.28839 | 2025-07-29 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1496fbe9-91be-3dc4-8b06-d0a9fb127247 | -6.40009 | -53.35489 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bac7319d-a631-3dda-86f3-cf522edf9110 | -3.27476 | -49.1491 | 2025-07-29 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7ffdfbf-0b62-34ef-97f9-14ecfe04afb2 | -7.80559 | -46.5721 | 2025-07-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33b2d228-dd33-3b3e-8e69-a3add8d24212 | -8.51373 | -43.31028 | 2025-07-29 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 410010ec-a1e1-374e-99fc-a917d1b0f962 | -6.39362 | -53.33211 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b2f44a3-dbeb-3800-ac97-43150b099649 | -4.10173 | -48.20256 | 2025-07-29 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d82939a4-4529-315e-ab15-ec2230136378 | -8.63604 | -45.51489 | 2025-07-29 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52d7084a-4a65-3e23-9960-6af45f340765 | -6.40027 | -53.32396 | 2025-07-29 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b487cd8-6aa5-3938-9ba5-a061e5befb61 | -7.82596 | -47.08511 | 2025-07-29 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c540be4-c1b6-3850-9b01-45039116cfbd | -6.49892 | -56.2177 | 2025-07-29 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69d67d6d-c769-344b-bd4a-52a6bd55b222 | -6.6789 | -44.06246 | 2025-07-29 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
