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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbd320c9-deb4-38d5-9796-eb775fda109d | -13.0899 | -47.44049 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 717d2a34-10d1-3856-aa5e-d949bb4f1e84 | -12.01763 | -50.95774 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f84ecf1-fd33-32dc-af6f-25888a224268 | -13.35096 | -41.32903 | 2026-09-29 04:17:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d39551d-abd1-3d59-a6cb-a02b0ff5407c | -13.34415 | -46.8127 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 91be8eba-160a-3adb-8429-227c520d9f6e | -11.53057 | -47.1643 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a8c81ce-f3b2-35af-9452-9d63688e071e | -9.14608 | -49.96983 | 2026-09-29 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ef14ccf-0503-33eb-8b40-39a87a9d8df8 | -12.01147 | -50.99214 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9fbaef42-e552-38a7-9cc1-fd42ec6ee52f | -10.20943 | -50.00872 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72551736-b3d0-3648-8b59-112a5d847a36 | -13.5265 | -46.90161 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e5eb820-7188-34eb-a273-3db5ffc4ad34 | -14.21923 | -48.50993 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 98841c0e-712f-34b3-87aa-773bedab0f3f | -13.19213 | -48.5603 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60c01566-e43e-3b7c-8ae1-f752ada750d7 | -12.90965 | -52.03688 | 2026-09-29 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26f9804d-6035-318e-bb79-434d69185e87 | -11.85511 | -50.47654 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58613994-210a-3546-bbca-b67a001e0f5f | -10.25431 | -44.60493 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13b2f9c1-e867-3ca6-8b5a-c4b02af4a13c | -11.36702 | -54.04507 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ef6fc88-ae27-3692-8679-d3ea37b33a58 | -12.0184 | -50.95345 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39089023-32f3-3f4f-8b5a-10da0f04c077 | -12.05933 | -46.49919 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeb30a3a-065c-35ee-952a-ee0040ec3c7e | -15.86466 | -43.08526 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94a2e9ec-2498-33fa-a1ee-88e6a0761a25 | -11.38459 | -43.39077 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee00fd0e-5a2e-36ca-a91a-13f04ea87996 | -12.02763 | -50.97731 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22eba427-f3ea-368a-9296-0fc6b6894684 | -12.03352 | -50.96952 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d042dfe3-cf10-3894-af22-172ae0f69bbb | -10.81162 | -48.7163 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b6e96d36-d4d6-33a9-bbbc-2ae10ae57d9b | -11.18039 | -45.14072 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 230fa25d-22c7-37cd-909b-f6df93ad3b5b | -12.06478 | -46.46544 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eec4d981-2d18-386f-a569-69a64955d153 | -12.06758 | -46.46977 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 017b8e55-03e5-3610-97d0-a3a17c179295 | -15.21273 | -46.17152 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52d60544-1d14-3710-806c-b993781363f6 | -12.74006 | -47.2757 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c33b3b07-7ff8-3622-84de-788f46b3c1ad | -10.43743 | -49.37317 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11905e90-c720-3299-8271-a224ee4325bf | -15.00864 | -51.40222 | 2026-09-29 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43179d70-a82d-3af2-bee1-f1d0f4f98587 | -12.69062 | -45.01541 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f3a2530-0a1f-395e-aba8-afd4f14a4ac1 | -11.38793 | -43.3913 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42143699-35ea-37d8-a5da-9bbf6851f671 | -12.02328 | -50.97651 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce698664-f7a0-339a-97fe-d86a872a845a | -11.4031 | -43.44853 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f2401fc-bde6-3201-bfa7-0f34a9c26f97 | -11.86358 | -47.10811 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d7ce65d-9cbd-3854-bad0-65c9268c80ba | -12.15551 | -50.40223 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75366dab-9663-3e70-b662-011b4f8139ed | -12.00024 | -44.92795 | 2026-09-29 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7699f80-974d-3171-b3f1-498889e978df | -11.95865 | -50.93079 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0f5eef5-d75e-3c45-bd12-b816bc5c8ab1 | -16.7789 | -39.42197 | 2026-09-29 04:17:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9b48790c-f200-38e2-81e8-4dc3d2574cc7 | -11.62445 | -44.15271 | 2026-09-29 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 330e1a5c-ceed-376c-be71-ddf86e5acd5d | -11.1901 | -44.8213 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dd0e03f-e7eb-3cca-bbf9-60bfcda4e960 | -11.19034 | -45.14232 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c5f34e9a-3149-32ba-be72-15f1416673ed | -11.97006 | -50.92255 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba3920c3-497b-3fc4-a1b7-411c629f9188 | -11.37826 | -54.05441 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65416cc5-6834-3737-8f6e-e528a3978ea3 | -12.678 | -46.99261 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2151b266-2f6b-3792-a256-6d97bc0f1d88 | -13.1995 | -48.56162 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b6da56f-b73d-3033-8d6c-ffc919d61a80 | -11.90266 | -50.62238 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 988467c9-a92d-3801-ae2f-6ba39085763f | -12.73105 | -48.26542 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 109897c7-db4e-324d-8fb7-8b65b50b303b | -11.4014 | -43.43729 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5db39d4e-0683-3c32-a581-401403e43dea | -14.21633 | -48.50496 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ec40f3bb-0090-3c26-ac93-36fee1580f4f | -21.23724 | -44.33646 | 2026-09-29 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3adddaa8-6416-338d-89f7-2ca0aaf409bc | -9.79373 | -48.20091 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 968a8a8a-efea-32e5-8519-385334d399f6 | -12.31485 | -50.15269 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cc13043-9342-397b-8d66-b3b6b52ff55c | -12.31897 | -50.15343 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aef5391-1c0e-3c0d-8ec8-50bc0f0bc191 | -12.07429 | -46.47448 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 572af8fa-0d75-362c-a189-e8e3c49dfa07 | -10.78641 | -48.74821 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c075a4ff-4426-386a-a158-7e26d0d34056 | -9.07575 | -49.8749 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2fb17dc4-042a-36a4-868c-eeb66a18999b | -9.79297 | -48.20548 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d90d4390-32c3-37e0-ae88-1b932bde947b | -11.3835 | -43.39792 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 010fa34b-7c9d-371a-bfd7-d8b14a08cbe9 | -8.71898 | -47.61095 | 2026-09-29 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34158437-91a2-3f4e-8551-279bc6fb47cb | -10.43494 | -49.38759 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0199e85d-ec8d-32d1-9e9a-73ab7452d2d1 | -11.61913 | -46.78267 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1fc530b-32aa-3a99-a83e-9b82925b9ad1 | -10.27965 | -44.6377 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f47241b6-aa21-3313-9e94-3a9819449542 | -10.90232 | -44.65979 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc8f95f-3947-3b7e-b089-eb1dc3cdbdce | -13.16507 | -48.54102 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6ce3ef48-deaf-3407-813d-b31da4776e75 | -11.93406 | -50.91744 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7651cb58-3ec9-338d-b16a-429e5891b8e6 | -9.14678 | -49.96575 | 2026-09-29 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52e9ef5d-4b22-3e88-9ddb-08d299fdd8e5 | -12.73022 | -47.27014 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4d79ff1b-183d-3adb-8e9b-480af5a65cb3 | -11.40174 | -45.41706 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7b34e97-db09-3d29-8e40-21917e223243 | -12.76944 | -50.6748 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7c94390-7878-36e3-8c39-f68917a5c9a9 | -11.39249 | -54.03885 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb9a3b67-6d2d-3b54-81f4-348c9807f5c9 | -14.52757 | -48.29303 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0767ed5-8d97-3fa8-b738-7083a332994c | -15.39159 | -47.91179 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ebf32d5-c23f-3628-80bf-d7a626a16a0c | -11.50597 | -47.39749 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1c296ec-2640-3928-8add-7da173892c0d | -12.04017 | -50.95745 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c06a871c-c5fe-3e08-bb1b-7267ddc09245 | -13.14281 | -48.54375 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e174532e-c0cb-3853-88fe-163e9273e52e | -12.28213 | -50.27575 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37ae5e3d-7c26-398d-8d87-9f60662f97fe | -16.79601 | -43.01229 | 2026-09-29 04:17:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e14583e6-a2ec-3289-bfac-95427264678d | -11.62947 | -43.50189 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b09c481e-04c8-37cb-a070-5981ebb63c20 | -16.34987 | -42.56995 | 2026-09-29 04:17:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c2dc346-dc35-31a9-8532-7d89b5414dba | -15.45425 | -49.07412 | 2026-09-29 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 998b69e7-17e1-3ff3-ac77-f732dcec1d73 | -13.74082 | -43.6694 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f2f9812-35ee-3695-9080-7f844827f9ae | -12.93863 | -46.64866 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c134ffac-6bbb-3731-8e81-005d999c966c | -12.01224 | -50.98783 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b96d05c-705d-37aa-8f2a-bc60b8b1c765 | -15.3861 | -47.92314 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 88564f63-5e4a-3d12-b7f9-35f5de97bef5 | -15.45561 | -46.14289 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b52dbf7d-93a5-37c4-b4c3-ad48fc8e91d4 | -14.79193 | -48.55108 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27272654-0d25-34a5-9c68-ef9b38642b12 | -13.92703 | -47.84795 | 2026-09-29 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 754cb3f9-a948-3dd9-989f-fb57530b28b4 | -11.9598 | -50.9295 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a56a8092-6508-3d83-8f70-d680fb0fcb9c | -21.06639 | -48.83411 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1d6f3b8f-4f39-3352-8618-43865269ade2 | -11.39861 | -43.43321 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| deb456cb-9bc6-370a-9322-d8beabd9d9c1 | -11.34895 | -47.33836 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e725a41b-e7cf-38ce-8264-c78d3a05db91 | -11.64558 | -43.50808 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba3e0f35-04f9-3928-b0f0-8f64727fc8c5 | -11.41085 | -43.44243 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7efc5e8-82b9-313e-8ea0-f066d5b3ce7e | -11.39202 | -43.45409 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ade832a5-0ace-30b8-a288-4613a800b37a | -15.45287 | -46.13871 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 53cfef47-6df5-321e-9dff-9b3d2d8aef12 | -10.82427 | -48.72269 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a1734c00-12e8-3750-8b03-e4c141038b14 | -11.90082 | -50.61456 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f54036b7-1e12-389b-8f39-3b7bc25e8d9f | -11.39113 | -54.04584 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fa56535-498f-3f90-945f-fe8efa5e18ca | -11.37491 | -54.04282 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1901160f-2c35-3cca-8a8d-9471e15578d1 | -13.5368 | -49.18166 | 2026-09-29 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README21.md)
