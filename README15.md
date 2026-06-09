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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f3128d5-96bd-3e0d-8174-7fabe336d83e | -9.41754 | -50.68148 | 2026-06-09 12:12:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 388384e8-7dc8-3f92-a54a-d1bea5403eb0 | -9.75326 | -48.21908 | 2026-06-09 12:12:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 6348253c-3dd4-37b0-a641-899b7b7ce82d | -5.282 | -43.95415 | 2026-06-09 12:12:00 | TERRA_M-T | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 63161792-0b44-3847-a720-566e6471eec5 | -6.90595 | -42.87292 | 2026-06-09 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 39aa0e4c-5740-3ee1-bff3-d94197d3a554 | -7.60509 | -46.4668 | 2026-06-09 12:12:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f820e041-7066-363c-9d1b-b1848ad8c059 | -11.33773 | -51.38589 | 2026-06-09 12:12:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8e38cced-1498-3e2f-8d8b-8f2927e9a46d | -11.33902 | -51.3767 | 2026-06-09 12:12:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b3955eb2-2998-3d1a-915a-3547f302a7ea | -9.74727 | -48.21196 | 2026-06-09 12:12:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| be8589f5-c4b4-3219-92a7-fba87901f032 | -9.75163 | -48.23189 | 2026-06-09 12:12:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3e38e52e-7b7a-3c8c-8bc8-1304ddd1fbdb | -9.74556 | -48.22471 | 2026-06-09 12:12:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 84bc7ba4-3285-36e4-8393-cffffc46bd36 | -9.00091 | -45.73089 | 2026-06-09 12:12:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| cfb6810a-1592-36c7-bb30-75e169cda03e | -11.95407 | -43.39639 | 2026-06-09 12:12:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9a59cf20-732e-3377-b9db-cd8e09521e03 | -4.74255 | -45.19751 | 2026-06-09 12:12:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f7735bcb-36b6-396d-b13a-974369d74cf4 | -5.79762 | -45.12243 | 2026-06-09 12:12:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 55c5ad15-4763-35ec-9964-ed4bc9d400f8 | -11.33644 | -51.39508 | 2026-06-09 12:12:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| abd589d8-6ffb-34c7-9d46-f93e55a46f47 | -9.07915 | -50.59749 | 2026-06-09 12:12:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| aecb9505-ea83-3598-b692-52db505bb889 | -5.8102 | -45.12372 | 2026-06-09 12:12:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| cfc86182-bf73-3d51-9cc2-53e623ac9514 | -6.85702 | -45.01652 | 2026-06-09 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 73bcf831-e8b8-378b-abdd-a800c07022ce | -7.60192 | -46.47297 | 2026-06-09 12:12:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| aacc050a-24d1-3116-a26f-04c8b015565c | -9.9432 | -47.87513 | 2026-06-09 12:12:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c4f8c469-c90b-3f9b-b076-93be1fa3933d | -9.79284 | -47.44518 | 2026-06-09 12:12:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 5c501378-c031-3e0b-9dcf-47cb04bd410a | -10.43111 | -49.44772 | 2026-06-09 12:12:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5c00775d-dae8-3ed4-8a27-6b6542c32e45 | -5.28549 | -43.97228 | 2026-06-09 12:12:00 | TERRA_M-T | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f1812c21-db2c-3053-9f19-025588726e99 | -11.33515 | -51.40427 | 2026-06-09 12:12:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f0515c08-f161-350a-9f08-a0f4270cf618 | -8.51971 | -51.55682 | 2026-06-09 12:12:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6b9e3565-4445-31f9-ad70-1b94a798d924 | -5.80008 | -45.1036 | 2026-06-09 12:12:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 593ed62b-f4a1-3a56-87c8-c9e5f22e697b | -8.52097 | -51.54795 | 2026-06-09 12:12:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 79b3d256-6363-3924-9801-f3724fb1a3ee | -6.85808 | -45.0099 | 2026-06-09 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 87a45432-f787-3e7d-91a8-d8e1d55d8125 | -9.07787 | -50.60679 | 2026-06-09 12:12:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 12b53b29-1606-3d32-ae62-e11d9035804c | -6.85545 | -45.02982 | 2026-06-09 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c5731861-c32d-3da2-be87-08d24236788a | -9.41886 | -50.67215 | 2026-06-09 12:12:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 41f0c85a-1c59-35f9-ab32-1968dd8ab2b7 | -6.78364 | -43.00163 | 2026-06-09 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| f31f731f-55c4-3165-ba7b-efd7ba3204b9 | -5.28862 | -43.94935 | 2026-06-09 12:12:00 | TERRA_M-T | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 79182c68-d622-3dce-b4ae-46da934ee3a5 | -12.42747 | -58.47639 | 2026-06-09 12:14:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9248035a-9957-396c-b40b-593a0a337810 | -12.43951 | -58.47842 | 2026-06-09 12:14:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 330f2bc2-5b64-38cb-8854-fb41a8cba0df | -12.32014 | -57.37112 | 2026-06-09 12:14:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bb74fbad-4d28-327a-a9f5-1fccdc119ff1 | -17.15722 | -45.06536 | 2026-06-09 12:14:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 86c0ae64-8a28-3d01-a405-1c9e00c76605 | -12.84879 | -44.37099 | 2026-06-09 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a050adb6-7839-3a69-b716-9a1bb60be7cb | -17.4218 | -43.80272 | 2026-06-09 12:14:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 92be802a-7553-349c-8893-28eea3dc5572 | -16.26098 | -53.73366 | 2026-06-09 12:14:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 22c7c937-b6fb-3962-b979-811fe5d1d188 | -17.80943 | -50.6425 | 2026-06-09 12:14:00 | TERRA_M-T | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8fd3198b-451b-30bc-8f8f-a9feaa09d0b2 | -16.26229 | -53.72453 | 2026-06-09 12:14:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 93b65aca-3711-3dd1-b5e6-a4325b970174 | -18.44987 | -50.40949 | 2026-06-09 12:14:00 | TERRA_M-T | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 1a161309-1392-3773-97e0-b65bc115ad81 | -11.57592 | -54.58396 | 2026-06-09 12:14:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7b0d2312-bc1b-32fe-aa06-716e920f5aa7 | -17.81933 | -50.64376 | 2026-06-09 12:14:00 | TERRA_M-T | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fd6bf9d6-924e-3db9-b2f6-f4b8537ebcca | -12.66193 | -47.66873 | 2026-06-09 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 54c49590-22d3-3227-9335-833dc63df20c | -12.66363 | -47.66312 | 2026-06-09 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 94e4af70-e512-3095-b373-31fa51999029 | -12.73265 | -54.19716 | 2026-06-09 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 06d4fa24-a1ca-30db-b4f6-d9d347ea1a96 | -12.7236 | -54.19582 | 2026-06-09 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 9be3a257-d06d-34d3-aa2b-282973d138ec | -17.43215 | -43.79848 | 2026-06-09 12:14:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 27095877-2457-337f-9a1d-12546c68312f | -13.90386 | -51.82296 | 2026-06-09 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5f03962a-9258-336e-9f70-b485f820f128 | -11.44347 | -55.10709 | 2026-06-09 12:14:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4b2cafbd-12c4-3b23-a80e-da94631661f5 | -17.58342 | -46.65104 | 2026-06-09 12:14:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a98dbace-83f6-35ff-bd07-b4f8a4108f16 | -12.44236 | -58.46113 | 2026-06-09 12:14:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 20047c0d-8323-3782-8349-eaeb04dc11be | -12.42561 | -48.71721 | 2026-06-09 12:14:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9ed8937e-ef66-35b2-962c-32238f8659a5 | -12.05423 | -49.76435 | 2026-06-09 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| a4748618-0627-3847-bdf7-4e07cc29b79a | -12.66167 | -47.67858 | 2026-06-09 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 491e5b83-bc35-36b2-873b-84585284553a | -12.65224 | -47.66167 | 2026-06-09 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5a22cd13-0a05-3f87-a6b5-36b45bae7c33 | -12.05567 | -49.75338 | 2026-06-09 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7c47d179-7d41-3eff-852e-172999e89123 | -17.15813 | -45.06008 | 2026-06-09 12:14:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 43.4 |
| e1dcdff5-bf69-3ef8-8363-94f02ee31080 | -12.84912 | -44.36543 | 2026-06-09 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 28d244bd-2ce8-373d-aeba-1748b49579a9 | -11.9493 | -43.4019 | 2026-06-09 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1791eaf4-f5ea-37e5-9603-b78143d5bb71 | -11.9493 | -43.4019 | 2026-06-09 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 10337705-c201-3c7b-8ac7-92434d30bcce | -5.7939 | -45.1267 | 2026-06-09 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| d8081bcf-9ee9-3913-8a4b-e92e3e106eb8 | -11.9493 | -43.4019 | 2026-06-09 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8d4f225e-1e20-38ba-9472-edfb0c293b47 | -8.9985 | -45.7418 | 2026-06-09 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c0db42bc-66d7-39a2-8653-6f2bdaf8978b | -7.1543 | -44.0536 | 2026-06-09 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b9ef577d-f1cf-3e59-a8d9-02b44242b84f | -6.9042 | -42.8634 | 2026-06-09 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 9d339251-b179-3c1d-a0c5-0f83fdab10e6 | -4.7479 | -45.1949 | 2026-06-09 13:50:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 8ab864fe-0be2-332b-bce2-fd6148bc72bf | -7.1543 | -44.0536 | 2026-06-09 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 044b8c8f-43a6-346a-867c-29044cac5051 | -8.9985 | -45.7418 | 2026-06-09 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 34a1385b-f79b-35a9-bfa4-49b8238771f7 | -7.1543 | -44.0536 | 2026-06-09 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e64edb32-5040-3f0b-a023-81ea9b46d5e1 | -7.1541 | -44.0767 | 2026-06-09 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d0149b63-6cf7-3367-8fcf-710629d97dd1 | -8.9985 | -45.7418 | 2026-06-09 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 8aff359d-8c25-3a4f-bf93-2af507ed5776 | -7.1543 | -44.0536 | 2026-06-09 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d0128787-9d9b-3cab-babd-96f16ce7eb3f | -6.9042 | -42.8634 | 2026-06-09 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| f35ff02f-7ecc-3d1d-a432-bf6ead925e11 | -3.5043 | -48.039 | 2026-06-09 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9dd65d30-ec47-33e3-b991-be0141535049 | -7.1543 | -44.0536 | 2026-06-09 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 574705da-0a1d-3e04-b528-679f464476ad | -8.9985 | -45.7418 | 2026-06-09 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| af720ad7-968e-3d57-a3b3-4c56374601b2 | -8.9985 | -45.7418 | 2026-06-09 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e0fcd2ab-79a3-3165-aeb0-52a4e8a618fb | -7.1541 | -44.0767 | 2026-06-09 14:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7e68f081-3f4a-326c-9223-9511dd990be9 | -7.1543 | -44.0536 | 2026-06-09 14:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1999ab71-cc6e-3666-8881-98af18d924ad | -8.9985 | -45.7418 | 2026-06-09 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 125621aa-3806-37e8-93e6-25381291877c | -7.1543 | -44.0536 | 2026-06-09 15:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ff6d5adb-a25d-3f01-b190-75e08f653a2a | -3.5043 | -48.039 | 2026-06-09 15:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| fdd7d530-a62e-38af-b349-6825eb76666e | -7.1543 | -44.0536 | 2026-06-09 15:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| cc2487e2-d112-3648-a5d3-294c4c8495a7 | -7.1541 | -44.0767 | 2026-06-09 15:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 67f504dd-8f29-348a-8e1b-1b94d668fe10 | -7.1543 | -44.0536 | 2026-06-09 15:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ff6de2a2-959e-38ba-8e0d-4522a49d1a10 | -7.1541 | -44.0767 | 2026-06-09 15:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| acd924b0-5cb4-3234-9469-6bef9cd9520e | -7.1543 | -44.0536 | 2026-06-09 15:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d12a8e1d-070e-3c3f-8b16-caf6cab0d0d6 | -7.1543 | -44.0536 | 2026-06-09 15:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b6b0e812-f116-354b-852e-e3f40a2a8204 | -7.1541 | -44.0767 | 2026-06-09 15:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f1e4ca93-3ba6-3e81-bda3-f078f712051c | -7.1543 | -44.0536 | 2026-06-09 16:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 79dc0c63-a21e-3a9c-9dbd-29ac6e671c35 | -7.1541 | -44.0767 | 2026-06-09 16:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |


