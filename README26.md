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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd3a1f32-55a7-399f-9e55-91e3f0a9681c | -20.42528 | -47.53344 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 877caed7-386d-3d7e-8d43-afb8f86cacd2 | -11.34057 | -48.3878 | 2026-08-28 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf6b4348-e3f2-3be9-b836-a7b7afe03eaa | -11.65098 | -46.74051 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82df5926-5bc0-37a2-be2c-ecc0f8520004 | -10.88067 | -50.51984 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eefd0a54-0ad9-382b-af13-752c6e5ce726 | -11.02652 | -49.6571 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc5d60a3-5567-3e2b-be6a-d1894cb9092f | -10.76851 | -50.64232 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e89bd3bc-4691-3dfc-90ca-9985b9a93b4e | -14.93724 | -52.60349 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bb5a3eb7-5976-362c-8478-9846ad924ac4 | -9.22703 | -51.53231 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0334dcad-7109-349c-b85e-e06d5c32321a | -11.89644 | -44.86514 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ad4e42cb-e0e6-383f-8e0a-2e1c4eb58c99 | -10.80128 | -54.01312 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41238880-9c69-3d55-a8f9-e612a0ef3eab | -9.4635 | -51.69903 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e0dcf5f-56dd-3cce-b185-e71a51e424c0 | -12.01647 | -47.16947 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dc1f536-7282-3c14-bf3b-9b505ac47ca7 | -12.24959 | -50.57341 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e70ec0ff-0067-3ae9-ba9f-121a6f6fdd23 | -13.37304 | -41.34951 | 2026-08-28 04:17:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6ea131ad-2fcc-34e4-9bc4-e0e895189e0d | -11.22803 | -54.01175 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a735e2f-6371-3252-b01c-5d951524420e | -10.17747 | -48.46542 | 2026-08-28 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4043a75-fa0f-3cbd-8e54-e4a4d42d016b | -12.78042 | -46.44651 | 2026-08-28 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27977342-618c-390e-b5b6-b5528ff1edeb | -11.37899 | -45.14647 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57de3853-56b3-3700-92ea-40f5905f55b4 | -10.775 | -50.63301 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a7ae8e7-f71c-3995-ba1a-c230bdd97cd4 | -13.61514 | -45.78213 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3890bb30-d2ed-3057-ad21-5fe47a1bbe1e | -11.29316 | -54.03166 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 287d38e5-7570-30c2-8593-6df6fbaa9e2e | -8.81171 | -50.07761 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b915186-4e32-32e1-8ab0-b1581ae0cbad | -8.95061 | -50.16616 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e585ad60-1cd2-3b63-ac41-36654dcf646e | -13.86837 | -54.1179 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 791d3a8a-2b66-3658-a3dc-697884f78f46 | -15.14616 | -43.79779 | 2026-08-28 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84e4bd75-783e-35ce-9576-604f455d86e5 | -11.65225 | -46.73272 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 69f7295f-d630-3982-9545-f6926afb2aff | -13.59124 | -45.78188 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 636461e4-54e5-3188-ab73-a3230db2fabe | -20.43316 | -47.52721 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15926253-bb31-3db2-ae6e-6214ead47244 | -10.78316 | -50.63604 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8b267da-c973-3e9f-98ea-5be36037c259 | -12.27721 | -50.59105 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dc12c6ea-f8d1-36c6-817d-1f7c418e7ddc | -10.46914 | -46.18648 | 2026-08-28 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3304d5b3-e0e5-3925-996d-ee16dd99018d | -13.59791 | -45.78297 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b087f8da-46d0-3891-aa67-3ccb23691e90 | -8.60119 | -54.78619 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b7be9b3-ee4e-3e0b-9448-d3cd3a25d633 | -14.60848 | -47.98332 | 2026-08-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 772bf518-feae-3475-a668-d47761403046 | -10.75619 | -54.03872 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3c819b2b-699c-3979-bbf4-fc94bb41ed7e | -11.49647 | -45.1145 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c87e9aae-3dc8-3a80-8395-487c087f5818 | -10.7555 | -54.0424 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 67b7139a-9de3-30e6-bea7-d612cf3bc19d | -15.88198 | -39.94247 | 2026-08-28 04:17:00 | NOAA-21 | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d646314-958c-3263-9ff0-16b6e0c6db93 | -14.15123 | -52.8362 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fa445d2-ca22-3aa0-b2b0-18996c542347 | -12.78321 | -46.45086 | 2026-08-28 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f39fea00-f178-3bcf-bf6d-71ae72680036 | -10.761 | -54.04336 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 90990c42-905e-331d-aeaa-51603cf18ba4 | -10.80074 | -54.01328 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84d5480a-812d-3bb8-91f7-97c9f15b0423 | -10.99165 | -51.09639 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5b74e4e1-10c2-3c2b-8347-ee3008f0e2f4 | -10.83067 | -50.52399 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e507436-ad55-3a58-9c23-c0c289768f5c | -11.8211 | -47.21082 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 68df7e38-e068-3187-a4bc-0d949043ea8b | -11.23231 | -45.04248 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1277c146-c10f-30bc-af87-49f99602d5ae | -9.0595 | -45.7822 | 2026-08-28 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d32878e-75ce-33d7-a60c-f3b72f5984df | -9.57272 | -44.56769 | 2026-08-28 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c55a612-12de-36af-bc04-5d9223404b2d | -10.9067 | -50.52451 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 740554fc-b68c-39d8-be65-1da753fdb89e | -13.2922 | -46.62768 | 2026-08-28 04:17:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3ee82a0-4516-377e-bba0-64db56202d76 | -9.16327 | -49.96397 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 038d6bb5-00f4-336e-8c78-5cbe24340aa0 | -9.15534 | -49.97115 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e7ec8b7-ef02-3ab1-a059-5ed92624dc7f | -8.59839 | -54.78181 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 61461d87-3f57-3406-aebc-5f8f84a159bb | -14.94393 | -52.59352 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 760dc564-f766-32a4-beb6-d91a9ebb29e6 | -11.47065 | -46.2068 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b358afd7-0ddd-3685-935a-d252636b3412 | -11.57208 | -45.51468 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae14951e-7419-35dc-8694-393f2a898c55 | -11.4855 | -45.0766 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f67468eb-6c4f-3d56-afc9-ee2d03f6e2f2 | -8.7754 | -49.9502 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fb125aa-0bf5-39a8-8717-40c9b81d1d06 | -9.21369 | -51.55301 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2872d2e1-4656-3577-8fef-f2db345ab05f | -11.72261 | -54.55325 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1088b991-1e0f-3a39-b101-99537bb894b0 | -11.49704 | -45.11096 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e29c8a54-d361-3e40-ba65-6c5c18e71dd8 | -11.19204 | -51.2433 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e632ba8f-77f5-3531-8166-45cf2e493c78 | -9.45964 | -51.72068 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56f3370a-78db-3ba9-8554-f5e20745e38e | -13.60572 | -45.77689 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 633e1141-3e4f-3c5d-bbd9-0e2c70e16ee4 | -11.73886 | -54.52914 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffadb9da-5ae3-3b39-a570-e9b5df9c33a6 | -11.76992 | -44.91315 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44a01d29-1db8-30a8-bf70-7aeee95e0358 | -10.53579 | -50.77691 | 2026-08-28 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28dd3894-1812-3f47-bfa8-5c6616f0e57e | -8.79497 | -50.07044 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23209298-75ea-3411-98ba-5528b9731405 | -10.57523 | -57.48769 | 2026-08-28 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d1e342e-e5fe-3779-9d3a-75957f93c44c | -11.01361 | -49.65866 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2075f057-c730-3b07-8d73-9af2b073fe28 | -13.48874 | -42.53323 | 2026-08-28 04:17:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85b8fe50-451d-3c2b-bc07-28ae4b9525d3 | -9.65754 | -48.29751 | 2026-08-28 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd52da64-1679-3c00-b61e-7c8297ba30e6 | -10.77265 | -54.04192 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6799219-bebe-34ef-b492-15e8465907fc | -10.91167 | -50.52865 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6d23b1b4-d9dc-394a-848e-d8d15929e876 | -14.21749 | -45.30826 | 2026-08-28 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25d76d3f-c2b4-3361-93e3-0b7db943d881 | -10.761 | -53.98341 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5ebdd50-a5e0-3a36-8c83-52edc7b8887d | -11.57532 | -45.5373 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d4ab378-2b02-394c-a626-0a8b04fa7e41 | -11.28705 | -54.03414 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 88c4396b-6521-3096-8625-f648ca5cffb1 | -14.87062 | -52.63559 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73cce4f3-1958-3fba-9538-bfd42adfd99e | -13.40394 | -51.41046 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87c7dd9d-a851-38c4-a7b4-f28f34a1ed7e | -14.21804 | -45.30471 | 2026-08-28 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3a78403-25a8-30bf-a308-ff60cdc3f574 | -8.94359 | -50.7711 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec4c5a5-c670-38ad-9c1b-22a9b250dc27 | -12.02285 | -47.17467 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0219fd9d-5a8d-3f04-95e4-a05e980972f7 | -20.41672 | -54.97528 | 2026-08-28 04:17:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7321df97-5dfe-3a5e-8f7a-eda5c6a5cee8 | -9.61482 | -55.12507 | 2026-08-28 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 126d78fc-fcb1-3189-885b-f3914ce719d6 | -12.26163 | -50.57979 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0b89c330-0a8f-3ccc-a964-51c9e844f00f | -12.37836 | -43.44232 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbeb88a3-dd59-32f6-851d-293ae9ff8236 | -11.2837 | -54.02223 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 618a659f-abf4-3bbe-82d5-33fa22965326 | -10.91601 | -50.52943 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 066f6b4c-929d-3d7b-8c63-243f686d2554 | -14.93827 | -52.59801 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9e6a7e45-1874-3f82-80c6-9eb751c7331c | -11.63996 | -46.7426 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48a5a096-92cd-3654-a61c-835f8f676abc | -10.76304 | -53.97268 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 699295ac-c9cd-37fa-98f6-27c465697df1 | -9.16181 | -49.97221 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0a68af5-3925-330c-a44b-498ba945207c | -8.59924 | -54.77736 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf2d404b-bb9f-3683-b85d-4e3b5849479b | -12.23184 | -50.57438 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2187b024-c411-38ad-971c-4db012498125 | -12.6966 | -48.4262 | 2026-08-28 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c553d6e-e3b7-33f8-9893-9d1848de36ea | -13.40231 | -51.4193 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 927497c8-76ae-3356-9df7-44bb3de83d88 | -14.99271 | -52.60685 | 2026-08-28 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ac9ae16-ad60-331e-8291-1e8a20404045 | -9.21753 | -51.55749 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f0945be-55fb-35fb-a864-20e29da0265e | -9.62159 | -51.53102 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README27.md)
