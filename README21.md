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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d701e44-0efa-34c3-b6b5-b2933bd45629 | -7.05396 | -59.19217 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5f2851d5-d61d-31c4-b52d-1f5140f45dd2 | -7.07798 | -59.18553 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| db663288-3380-31ad-86e1-ad64cf64938d | -13.60764 | -48.98516 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbed81a5-92ae-388c-a495-c34732df3289 | -13.61645 | -48.98989 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd16fe42-79a5-306e-b14a-d61e03a78257 | -13.04298 | -56.85515 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21ec5a32-5b90-3316-81ae-ef34f6e243d0 | -13.61502 | -49.00623 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48197bf6-5a87-3a13-be6e-4dda8dba6a99 | -12.40821 | -47.78121 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fd4f60a-f26e-361e-a7f5-872e0af7fe5a | -12.5897 | -47.17435 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc5b6d64-4753-3de0-9fa2-705eaca75146 | -9.55141 | -62.72012 | 2025-08-09 04:42:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bdc2f0a-adec-342c-ad82-a57004868d47 | -12.61278 | -48.1059 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4756708e-9512-371f-b639-30f3d7afe765 | -11.77814 | -47.56314 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cd3e214-83df-339d-ba1c-fcb56eccc3c4 | -7.08084 | -59.20131 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9774eb10-73cc-3b98-99e6-121a120d76ab | -12.60925 | -48.10534 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e60a73bd-26ab-361f-8fc5-5ee141664f7f | -10.60559 | -48.36559 | 2025-08-09 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 46432f02-70cb-3efb-942a-4ec4f0137c2b | -15.27065 | -40.33477 | 2025-08-09 04:42:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79e62312-7227-3031-8fb4-a60ff4cceba2 | -7.05527 | -59.18499 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 926aafd1-dba2-3da6-b7cd-e01c1b01cc39 | -13.63256 | -49.0238 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66eb94a8-1f59-3ca2-8da9-c1152b7547eb | -12.03785 | -47.51339 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0678b192-3eee-318a-9149-278b12cda3b6 | -7.06434 | -59.19784 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 92cc7555-d8e9-3c90-92ca-8b2e25cb407c | -7.07732 | -59.18916 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e3f1226d-54fd-3188-a6bb-2578d4aabc23 | -11.77537 | -47.40075 | 2025-08-09 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c8c1cc0-b6ab-38e0-b02a-d7823740ba09 | -10.62949 | -44.7579 | 2025-08-09 04:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87f0649a-954d-3b3c-81ed-ca93fedee34f | -13.61393 | -48.99022 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abf044df-6af4-394f-aa06-655fb02d83cf | -7.05882 | -59.19682 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c4bd75bd-61b9-3fe3-9ca9-30b0cf7af958 | -11.773 | -47.39174 | 2025-08-09 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e185bf0-3829-3f60-92b5-eb0357ad8247 | -7.07311 | -59.18094 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| cbbfdc94-3178-3033-a6ab-9c042de5574d | -13.05152 | -56.85664 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0a740ad-0073-3a1c-af84-e35b92fa6da5 | -8.87437 | -47.47729 | 2025-08-09 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a79211c-6a8f-39f2-85d5-f17a83a6f3a7 | -10.18156 | -49.50944 | 2025-08-09 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41d5fa7a-0763-357b-ac9b-2c20b910d90e | -13.62106 | -49.00643 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3d40413-fee4-3815-b42e-07cea9e13ca4 | -11.73873 | -47.49892 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bda8996-40fa-3596-a84e-b6b677b63918 | -12.56781 | -47.11701 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b17683e4-ef40-37f0-bfbd-c7aa464119bb | -9.86992 | -49.9637 | 2025-08-09 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38fb6db8-0cb0-3de1-a5e7-90cd54fce4b2 | -12.71533 | -47.79408 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee91890d-4888-3d9d-976c-005465f8531c | -13.62338 | -49.0145 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0965307-00fc-3859-8df7-a5b8b093eaf4 | -13.05014 | -43.85006 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 774d8615-20d2-3cdf-81f1-74c89dcea415 | -7.07051 | -59.19527 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 94e87811-3bf8-3af2-b78c-c16d7d937e26 | -13.61736 | -48.99084 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14b7f4b9-c149-3dc4-a4a5-a250726b880a | -11.72921 | -47.48851 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98e9f99f-6be9-3398-88b1-9d69868e55e7 | -7.05329 | -59.19586 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bfdb30f0-12b9-37c5-a5a6-5449c15925d1 | -14.16397 | -43.66673 | 2025-08-09 04:42:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6404222-b2e9-3503-a383-8e353d489357 | -13.6268 | -49.01521 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73608cde-3b04-3245-a0e0-2be67ca3a5b4 | -10.17822 | -49.50891 | 2025-08-09 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc9ae327-32a5-360c-9bc3-cff53a0b66a1 | -13.62735 | -49.01155 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82700620-8364-3e42-8f07-e123ce1734d8 | -7.06984 | -59.19897 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 883f67c4-d648-3d90-ab09-7f142a4e303d | -13.61586 | -48.99389 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 253222e1-c1b5-37e8-80c5-81076da7ac99 | -13.05724 | -56.8493 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76909a3e-bfc0-3cf2-9aa2-dab03615a083 | -7.05462 | -59.18851 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 317066e6-627a-360d-8e10-a9cceda3f7c5 | -7.06951 | -59.16933 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b6bfa503-ff7e-3526-8b6a-1d6eeeff0d16 | -7.08149 | -59.19765 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ce1723a3-bb61-332d-8e65-7aad457f19d4 | -11.77688 | -47.56401 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b00408d5-0ce1-3350-9822-b46a468faf6e | -13.04619 | -43.84462 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4118c6b6-d9f5-333e-9c4d-77b3fa2d0b20 | -12.40463 | -47.78065 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d88802c-f4d3-3b1f-8105-58f359912551 | -13.6193 | -48.99453 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b209e220-8354-3102-a28f-5acbfacada22 | -13.63023 | -49.01587 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a12d905a-2008-3ff9-bffd-7772eb98d2ab | -7.06015 | -59.18949 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 5b4f3fae-d4ed-3847-9c5d-46670d429dbc | -11.73639 | -47.48977 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4710e0e-a971-31f3-b250-7d59330e7f1d | -11.78417 | -47.49581 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f481f7b-9ee6-3aaf-b3df-009d2a7d3333 | -7.24747 | -59.99213 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5523d171-c416-3181-a675-df811ef5696d | -12.58403 | -47.20309 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bd0b3e7-6336-36a4-b0e5-156edd8764e3 | -9.86425 | -44.69981 | 2025-08-09 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5218708a-6783-3fac-8d0f-a1ee989e676f | -15.26467 | -40.33404 | 2025-08-09 04:42:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 21e21b27-2cc2-33a9-bfac-a0615fad31bb | -11.91723 | -44.85456 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03ce94dc-2906-3b72-a899-bf6f1b9b14d4 | -7.06269 | -59.17555 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0f98f86d-a8db-3950-829f-20f825027a94 | -11.74358 | -47.491 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f87adef-b322-333e-8d54-0468c69c2aff | -12.56589 | -47.13017 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c8a3188d-ebc0-38ac-a23a-31504fd9fd23 | -7.07505 | -59.1702 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c2112c6c-d0dd-39db-9518-75a297aa0b69 | -11.37899 | -54.35204 | 2025-08-09 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8bbee77-5ff9-33b3-9115-e18462d696af | -11.7478 | -45.02344 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 563c2170-5150-3dfe-93dd-41b0ce02b621 | -7.06205 | -59.17905 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| fb6de9db-5f7f-3223-a9aa-f3421552269f | -11.75438 | -47.49271 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f87406c-0ba3-3bf6-90a1-2b8a77c56b2b | -8.93437 | -46.73865 | 2025-08-09 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8011411c-0487-3f80-b0e4-35e4b6bc43fc | -13.06967 | -43.83987 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc6d93da-1572-3ddc-b433-ce19f00c4a4b | -12.71041 | -46.3738 | 2025-08-09 04:42:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3937bc1-8b7e-3100-8408-80f845d16313 | -9.65783 | -43.84271 | 2025-08-09 04:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9ca5f2b7-b752-3b84-ad47-66aa91b97589 | -13.18008 | -43.68085 | 2025-08-09 04:42:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bee2839-a416-3044-a74d-e5de87970ba6 | -13.62968 | -49.0195 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0c8545c-82ca-3a3b-9204-aab5caecf570 | -7.06566 | -59.19057 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 5e5f96f5-2be5-3100-bae6-8eabe6ca34c9 | -12.59148 | -47.17709 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 543a4df1-b226-3c89-b48c-6edc45016904 | -13.6344 | -49.84249 | 2025-08-09 04:42:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44376d9c-c70e-3a25-9185-6f68e9253a18 | -10.68477 | -56.5529 | 2025-08-09 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ebb64a1-04ee-39a5-bbd8-be1f8fc8fd32 | -7.05746 | -59.20428 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 40830d03-6f6f-306b-a911-6dcebbe23084 | -7.07666 | -59.19284 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 29339a41-aa75-35e0-bc91-9b1509d98e0a | -7.08414 | -59.18299 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 8af161bf-8fff-3dda-a481-45abdb21aced | -7.2467 | -59.9963 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13b70a33-fde7-36fd-9847-584c0a1a29ff | -13.04941 | -43.85181 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0f986d3c-acf1-3b5b-b69b-db45cd4d1436 | -13.61049 | -48.98962 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1b23cd7-8b0e-3eb6-96c3-5dbfed6e5090 | -12.5623 | -47.10271 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc91125d-548b-3203-8ac2-f101b56f7754 | -8.72739 | -49.74231 | 2025-08-09 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48b6f8ce-c27e-369c-9530-e9642fb648f6 | -13.04554 | -43.84943 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f6526e0f-d02c-30ab-a83d-c8c2e783284e | -7.06758 | -59.17998 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| cb129049-c789-33fa-a5f8-158bb7da9b4f | -9.28197 | -49.95581 | 2025-08-09 04:42:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7706b18-b601-3aad-b3cf-b77eb68d47b0 | -7.05653 | -59.17808 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2259f657-5dc7-394e-b74f-e9cce7c56ad8 | -11.73934 | -47.49478 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2a127dc-2bdc-3be0-bd22-7539172a77d4 | -11.74292 | -47.49549 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b444103e-0d40-3c35-9957-35786741726a | -7.07246 | -59.18454 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 36a0c4b0-b35c-381c-9192-37ac8266a2f2 | -11.0867 | -50.46466 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae1e1581-8360-30b6-ad8a-5a5918e14826 | -11.93381 | -44.54339 | 2025-08-09 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c36efc7-d0f5-3ed2-8f22-64e375fe7e17 | -11.24854 | -50.18781 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2ff2303-abf0-3ce2-8f60-65c11e7f3c89 | -11.09111 | -50.5014 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README22.md)
