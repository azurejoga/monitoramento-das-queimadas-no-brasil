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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2c69247-aa4a-3add-bf37-40544fd11368 | -12.4492 | -50.84416 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a8041623-9464-3f45-8d54-209f65deabbb | -7.45754 | -42.10755 | 2026-09-17 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31708de4-2a9c-3f02-a75f-750b037dbd78 | -13.59903 | -46.94798 | 2026-09-17 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0ca591b5-7e70-34d7-8e85-548bee4455bc | -7.07753 | -41.78069 | 2026-09-17 03:55:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c57bf0b9-701d-332b-bed6-d497bf1bfbb4 | -7.36418 | -44.48178 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8db49fcf-cb9b-382d-bd3e-fac769f4ce7e | -9.59164 | -46.65699 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a43c9de2-9be7-3a5f-ac94-3598e0864ac0 | -10.3971 | -46.62991 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60dbeeae-5c4e-39c0-97c9-2688e8aa6b22 | -12.48168 | -50.85127 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 30d52461-0339-3fc1-b19b-1201aa91b903 | -10.6158 | -46.09135 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13e0a50d-2207-3cde-b454-f1cd724936a8 | -11.16631 | -42.79066 | 2026-09-17 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 78c6cdce-1660-3880-8068-f265e0e8e985 | -11.31511 | -46.79103 | 2026-09-17 03:55:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76a81c69-a78b-3163-bd4c-cd5501d479f3 | -8.85322 | -44.89497 | 2026-09-17 03:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b1b1764-4139-32fb-912a-5ff1da3be2c5 | -12.4275 | -48.48445 | 2026-09-17 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6b49892-a03b-3a17-95cb-0b4b89da5b9a | -11.35225 | -43.9668 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f068add4-bde7-3c1f-9f5f-db3320f8064d | -9.10162 | -45.71786 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 9fa4b4c5-74d5-3246-b8db-09cb0755802c | -9.87798 | -48.39087 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 104d29b6-5504-3582-a15e-343f58079704 | -7.94222 | -44.83695 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 68bb35d4-41c5-3c64-9e39-c62a5f9c34cf | -12.45122 | -50.80455 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| db6b3def-8fb8-3264-bc2a-0d5194eb936a | -12.43907 | -50.83036 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d7bc648-56bc-3ea1-ba95-8ad6f7f12af8 | -12.4707 | -50.87176 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b9a19ee1-2e5e-3415-a6f4-2a5b7f6c8bd9 | -8.4743 | -44.56307 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e20cc8a1-8e16-35a9-9f85-829ba515bc6b | -10.11421 | -45.57312 | 2026-09-17 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca92b7df-83d4-3ef1-ad60-dea8b197ef72 | -11.88615 | -47.59068 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c1f90807-6b6e-357c-a0cc-50931399355d | -10.50375 | -46.33241 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70fb5041-a05a-3a7f-a722-f7c68517d040 | -12.30829 | -47.95987 | 2026-09-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2a08122-8881-3b52-a815-e143da0d7672 | -12.47254 | -50.89518 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 37f98231-05a1-3a90-b88d-81ee612aeeb7 | -8.56269 | -44.54172 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4084414b-918a-3b02-8ebe-06adbb584a3a | -8.38473 | -42.20879 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| aa236602-f6ae-3af2-b563-6ea3492c7fe5 | -9.59334 | -46.64561 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c23993ff-6641-3ca7-8f3a-e57b272bc9e1 | -11.32846 | -46.77639 | 2026-09-17 03:55:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c27f65e-aec9-3f75-952d-8e7480045d1b | -9.10946 | -45.73072 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 265630a8-c1ad-3521-ab10-f286aef1ec54 | -12.47025 | -50.90619 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 502532f4-9bf7-3751-97c4-e2f384245f93 | -7.04033 | -42.06445 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8ba33a5e-5dcc-3bf4-bfb7-4cfb52cb5de7 | -12.45339 | -50.85658 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d10d50bd-f66a-3f52-bb5a-845f405808f9 | -8.52965 | -44.51897 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 499cdb43-c764-3862-967e-808638b72678 | -7.12567 | -42.1763 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8727fdf7-50cc-3858-8d77-7925bdc50083 | -7.4587 | -42.11118 | 2026-09-17 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7fd35faf-ac66-3aae-ba92-b08fd6522f80 | -7.08083 | -42.09283 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d70dc728-11dc-3e49-860d-1699b3b32389 | -12.46402 | -50.8074 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 24b0b0ca-c147-31dc-86c0-a44b570c42b4 | -8.38869 | -42.20948 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fc60ecba-4fa2-390c-b013-8378330dfe4c | -7.58018 | -46.33635 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69e7f344-792f-35a8-a9a0-222a0f5c10fa | -8.19801 | -43.67384 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d157460c-25f8-3278-9734-1738a5c45774 | -11.4785 | -45.76743 | 2026-09-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fbc0615-31f1-3d2e-ad0a-bde025b03aeb | -12.45586 | -50.81136 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| aa09526a-00a0-3960-8e1f-3bb4b2590181 | -6.65995 | -43.64082 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1efe8a62-008a-3d41-b29a-405ec135583a | -7.51178 | -44.93258 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffab4b6f-3ce7-3c9e-8a64-c07fe77dc691 | -9.61436 | -45.34446 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 43a899c8-99e8-31c3-b5d7-fa310607fb52 | -7.09453 | -43.47033 | 2026-09-17 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9b70f9f3-81ff-3d3a-8bf5-9ad3bcf945d2 | -10.37018 | -46.88957 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a1080ed-7a59-3e31-a25b-94354cd89120 | -12.46586 | -50.8306 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cb5a2c5f-bcb3-35d1-a03a-9acb12644951 | -12.43996 | -50.92281 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d7cfc57-cb65-3402-84bf-5552ce39af55 | -8.85994 | -45.88353 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c72aa225-07c7-366c-acca-802c64e9a974 | -7.64804 | -44.33286 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 53c9c18c-0c17-349e-a0b4-7f10273a1485 | -9.46725 | -45.45262 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16ad5f85-680c-395e-b39e-e7616ef9f9e1 | -7.08273 | -41.84119 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c09283d0-06c1-36c0-a0ea-bfdfe5a8b1eb | -6.79773 | -43.17249 | 2026-09-17 03:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43b3206c-f6f0-3556-9c56-ea1fe6ef8994 | -12.46104 | -50.78968 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 10314adb-302d-3539-b8e5-7dd238290129 | -10.21345 | -43.1871 | 2026-09-17 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0bc85f1a-0249-3eac-9313-02df1f21660d | -9.10378 | -45.72775 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 78b3543f-929b-333a-adde-e6a14d9191f8 | -7.97159 | -44.83694 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46c0c226-afae-3768-bcf8-0f0c3f1f813c | -12.44269 | -50.87701 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2651df21-43ae-3307-a78d-d172573c8b5d | -12.46266 | -50.91029 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38b9048f-58ff-3ff2-a6a1-e2a792c6d6a5 | -9.96157 | -45.33178 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b66b097c-ef28-3cf4-a7f5-7de1cca2d864 | -9.95037 | -45.28627 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e06ff33-1ffb-303e-8be8-f5492f01310b | -9.03323 | -47.75487 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dc5abd8-b918-3868-8bbb-9bf507aedd84 | -11.88809 | -47.60888 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa10d5e1-af36-30ff-9336-8dca694bedde | -13.15739 | -43.24476 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3314d3bd-ec35-3178-b851-4bb18015c5a1 | -9.49849 | -45.43799 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e0ae698-f5d9-3ff0-9614-bd679c670678 | -7.09149 | -41.83741 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8687fb45-daf6-3d32-a054-e587bcf4cbd7 | -12.49451 | -50.85413 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 80ee9192-ee72-36da-8fd6-efcb74e5dd6e | -9.8298 | -46.50348 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d981622-516e-3aa9-96f7-3ee892bc180c | -9.95083 | -45.30658 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dda30a05-7203-3369-adfa-f0a7e8b3c690 | -9.60434 | -45.345 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ffb64b48-f9c7-3ac3-9837-065a28037a1e | -7.58086 | -46.33986 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d879a97a-a6c6-3ba8-bfb8-1f5224910823 | -9.55141 | -45.42019 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b7bfb886-b20d-330c-886c-de58cb4eacde | -12.43414 | -50.85223 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e7e1c44-8700-34f1-a1ff-a56d1bd7c9da | -8.94666 | -44.3996 | 2026-09-17 03:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58a47acb-af97-39da-8f5e-1a153560f16e | -13.58401 | -45.47509 | 2026-09-17 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2348bb9f-f4a1-343e-8840-ddf37fb93303 | -7.38257 | -44.51544 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 613044d2-bd98-393f-847c-eb2bc7360436 | -7.10827 | -43.10337 | 2026-09-17 03:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0213dfce-29ea-3788-b832-cd2bfe6ee1de | -11.71716 | -40.17113 | 2026-09-17 03:55:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43d477ee-e3c7-35c8-86a0-8a169030119d | -9.83984 | -48.37019 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77dc5fc7-ef4c-3471-83f5-49499ce6ae7c | -8.56155 | -44.55396 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61bd010d-7283-367b-aaa7-4c9a7f9c8b5c | -8.25942 | -42.16373 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 87a59184-0e67-322e-ba4f-5369f8533e7c | -11.89809 | -47.58614 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b223200-5dee-386a-8c68-8dbec6d4db2b | -12.4545 | -50.8511 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fe7adaa-c245-3db1-9db5-3e0ea26a082e | -9.1127 | -45.73506 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9633fec9-945d-30a9-be22-0e047e77cc91 | -7.37059 | -44.48532 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f10e688f-2119-3122-8d4c-f7a100bde3f3 | -9.99501 | -45.44552 | 2026-09-17 03:55:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b3ee311-8cdd-3fd1-8a2c-1456bb887634 | -12.42983 | -50.87416 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 30936759-1057-3cc3-b3e0-2631d6e763c5 | -7.10897 | -43.0993 | 2026-09-17 03:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e628560-19dd-33b4-aa7e-63976aacacb8 | -8.78899 | -46.89879 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a0fb0c4-1676-38f9-83ee-6849ef394c82 | -7.03204 | -42.03152 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 80d3c9c0-c360-3844-b252-2c8b435093ac | -11.59203 | -46.87682 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b618a54-fc26-3183-9f2d-a7d8c112b04c | -7.04879 | -41.49704 | 2026-09-17 03:55:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 984bae98-632b-34df-b023-7bf7ce6c78b6 | -9.27334 | -44.39207 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 13ee35fa-f045-3a14-95a9-d65428be5e61 | -7.06999 | -41.82644 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c7160712-42c1-3c6e-924b-373f6a6aac83 | -9.03744 | -47.76374 | 2026-09-17 03:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1a924f4-c160-31f3-9ed4-2ef4539312b4 | -7.37358 | -44.48322 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31898402-a7fa-322a-9a0f-a17ff3b9c354 | -11.65071 | -47.32891 | 2026-09-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README30.md)
