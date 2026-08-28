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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93e8eae7-8e1a-3205-89e0-23b8a7f3fcce | -14.83497 | -45.53001 | 2026-08-28 17:26:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 550cb074-b127-3ef3-8725-f1c295982f4b | -14.19469 | -52.84121 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b1c60bfa-7ff2-3144-b20f-b159c6c5b231 | -10.09137 | -46.9872 | 2026-08-28 17:26:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dc8d0899-d6f2-3689-8fb2-e33271e16a5d | -12.38706 | -48.19062 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 20ac3d86-bde6-382a-9b72-0ffacfee0047 | -11.83475 | -50.0631 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e1c544c-9366-3f79-a071-7b800ecd9606 | -13.60667 | -45.78293 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 715a4a35-b29e-3650-988e-20cb892f4ddf | -16.79353 | -50.02268 | 2026-08-28 17:26:00 | NPP-375 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 9f0f78ca-c895-3009-9bbe-11cfc94203a3 | -9.80171 | -46.33546 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c2b2c233-b1fb-3db2-9600-7e7d936c0a1d | -13.96608 | -41.49381 | 2026-08-28 17:26:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ac42444c-b950-348b-a04e-218dd8bf87ec | -11.38237 | -45.13809 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 71dc8b96-9f38-33bb-8449-05ffa6c8355c | -10.46427 | -46.18285 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b21a4220-c25f-3119-b407-233ca0c3b154 | -11.27004 | -54.01439 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d293cf0a-f487-3944-94bf-56738f0c79de | -17.58249 | -51.64597 | 2026-08-28 17:26:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cd832dab-1da0-34e5-9bcf-65d89814815b | -13.10408 | -50.04842 | 2026-08-28 17:26:00 | NPP-375 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e3b23b28-a6c3-3a37-a5f8-37cd8ac55514 | -11.27244 | -54.02945 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ac388474-adf6-30a1-863c-3004081273af | -11.21841 | -53.99971 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b36e80c7-b43a-3ab6-a2e8-be415a8fc39c | -14.92005 | -56.32049 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| f5671a4a-5c1c-367f-975c-d04661df5bb3 | -11.66957 | -46.73177 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 199dc952-0480-344d-8771-96fb8f15be63 | -15.10926 | -48.00702 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| e650ebae-179c-39b7-8951-aa1bc58145d3 | -10.45873 | -46.18394 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8a7b1c84-a241-3b76-a9ae-17083dd32b8c | -13.61137 | -45.77839 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6af54ee4-c43e-3eab-91e9-b7dc43c70791 | -11.23557 | -53.99687 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0f10092f-1bf5-333a-830c-fe85015dfc15 | -10.77309 | -50.62318 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 40d3e1b3-45f6-3a26-99c0-c9e66616f79e | -14.92245 | -41.25444 | 2026-08-28 17:26:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 49.7 |
| c885ab11-b852-322a-801a-79c8953c2015 | -10.44612 | -43.76836 | 2026-08-28 17:26:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 49acf1fa-f15f-30c4-8e2b-d5ea5cef3428 | -11.02572 | -49.67506 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7d6806ea-3ae4-371b-b91d-695b7503e974 | -12.78239 | -45.95146 | 2026-08-28 17:26:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 348e2763-f791-357f-a32b-9ff78de80e2e | -14.80872 | -43.56134 | 2026-08-28 17:26:00 | NPP-375 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 60fbfdbb-9d2b-3370-82e7-e315b89b9548 | -11.28034 | -54.01276 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 93897f98-dd1b-3d9b-a2c9-75196aefcf29 | -15.85485 | -48.95623 | 2026-08-28 17:26:00 | NPP-375 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f15a1f4f-c6dc-3a59-b989-3ac6f344c3de | -14.4363 | -52.59563 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0a55837a-ba20-3cfe-82d3-19f07ba2cd41 | -9.86398 | -45.84182 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ec625f7-8168-3254-956b-fa1cc843712b | -14.41201 | -41.21527 | 2026-08-28 17:26:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 08f19ec8-62e4-3873-b9f1-bfed4cd632d3 | -11.2208 | -45.05067 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e6cd5bbb-abdb-3375-b184-76253974ef33 | -11.41503 | -42.30441 | 2026-08-28 17:26:00 | NPP-375 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ddbbbca5-b8cb-348c-a800-9df208cde71b | -15.13197 | -52.83045 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1329cbb3-daf1-3ea5-9ec6-1eeb461b58c2 | -10.5092 | -50.77781 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 865a20e8-0043-38c2-a778-49126d0a89a2 | -14.87729 | -52.59916 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d8d197ac-a867-3b0c-82e0-de0d7807a86d | -14.45222 | -53.3749 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b3a3128c-eca1-3ed4-8fd1-30f49fbfdc25 | -14.60133 | -53.14671 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 21f99219-0d7d-3b1a-9f8c-5e597144b360 | -11.23334 | -54.00496 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1007c480-afd6-3aaf-b597-c13141c468fe | -10.02006 | -45.81356 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc6eadf6-6090-38aa-b5d6-d84edfb45e91 | -14.24348 | -44.43521 | 2026-08-28 17:26:00 | NPP-375 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5ad6d565-de7d-39e2-9233-52c11c9870eb | -11.22871 | -53.99802 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ddb5454e-003d-3301-a630-7cc94f250340 | -11.35365 | -48.39473 | 2026-08-28 17:26:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ced81473-6ff7-3bb3-bb92-0f57167e901e | -15.63457 | -45.93323 | 2026-08-28 17:26:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01fa5110-96bd-37d3-a273-cc6d623d2238 | -13.42175 | -51.76647 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a3248431-a4f6-3d14-ac43-f472cb54f228 | -10.17541 | -48.47646 | 2026-08-28 17:26:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dd86eab9-e0c7-3b40-9b62-f01d260a737e | -14.43232 | -42.20644 | 2026-08-28 17:26:00 | NPP-375 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 8a1c268d-2eb6-37cd-a92d-38138263d52d | -10.35849 | -48.32285 | 2026-08-28 17:26:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f2e0e1b7-40f4-3936-b72d-8a4cba491147 | -10.24053 | -48.45367 | 2026-08-28 17:26:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8bb56705-9aa3-3144-a74a-edaf1338da04 | -11.23454 | -54.01247 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 15f0e818-e08e-331b-ba2f-981acfdc2dc2 | -9.8453 | -46.3228 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 59ffd15d-0b2f-3ab9-ac73-d519469bd0e5 | -18.10971 | -51.61049 | 2026-08-28 17:26:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 8617932e-f25d-38f1-bd02-6c90a46a254b | -14.46187 | -53.36942 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 811df9b6-b927-30ac-92ed-4663211080d9 | -11.27641 | -50.69186 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93b3fdec-2daf-3c78-a5a2-d8500bed0199 | -10.64436 | -50.65004 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d23b5fc5-8429-3354-9e6a-07e768df451b | -11.2402 | -54.00381 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ab0ab306-fbe6-35df-8514-ea1d0622b894 | -12.90941 | -59.87786 | 2026-08-28 17:26:00 | NPP-375 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 37a9bb97-e47b-3936-8226-bd1ba363a6d8 | -15.46569 | -53.97452 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f1e191f-c2e2-3dd8-8f45-a18a1bd46bf9 | -10.07776 | -48.66913 | 2026-08-28 17:26:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 51e8ee30-b599-38c5-b34e-65057cdaab2f | -11.24283 | -45.06952 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a6227f30-94e5-3bcd-b22c-65ef5db7148e | -12.39267 | -48.1947 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 21aab5ff-388d-3ff0-a3dd-cc8bb73e6c54 | -9.88296 | -46.34627 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5515666-7832-3c6f-87de-22c6126a0fc3 | -9.69207 | -46.56485 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| ad1d8fa7-e072-3f32-9c0b-b575118de9c7 | -11.66919 | -46.73164 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7590707-65ec-312b-beb3-c3b93f943894 | -14.33639 | -47.24451 | 2026-08-28 17:26:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5d3242ef-de3f-39a2-986d-0bf587410224 | -11.23274 | -54.0012 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0af225fb-5e7d-3fb2-8202-e3d37afd7754 | -11.2434 | -45.06051 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3b806776-90fe-3f7a-80e9-f8039efad323 | -11.2178 | -53.99593 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b3f727b7-94bf-3403-ac08-411f912dccee | -11.4877 | -46.93929 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04761da9-c3df-3d14-a5b1-a6a0aa3d95d4 | -11.18963 | -46.2463 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d836781a-76cf-326b-84c2-34b323603c52 | -9.80307 | -46.34272 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 405adcfe-93d8-3527-8841-97996f262ed7 | -10.34257 | -50.38586 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 39e6254b-46a9-32b9-a24a-0bfe814d098f | -11.2267 | -45.04966 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 323f9f26-0bd1-320d-b87a-6b89a4ad3730 | -13.42467 | -51.76136 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1d5eda86-89bc-3068-9f46-44b54e99c0fc | -11.84092 | -47.21973 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0057fbad-10a3-3eeb-8473-faa293416993 | -10.32032 | -49.96471 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c6dfdb2a-723c-3771-b43f-312527c30acd | -14.18182 | -48.77643 | 2026-08-28 17:26:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b2f77def-5fc4-3d9b-afd4-b572aff0ab36 | -14.48681 | -52.14215 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 63e94588-78b4-3bc7-a3a3-636f00013b61 | -9.69073 | -46.5578 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 5eaf9073-7aed-30e1-9147-6b61926b2627 | -14.91328 | -56.32153 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 27f8f09b-068b-3af0-89f8-73c32a5e658f | -14.45564 | -53.37432 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 49b03b67-2527-38d6-aba8-b57da25454bb | -11.83642 | -47.22367 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb2fe3ac-fd4c-3575-81d0-b4c1c81626eb | -11.83056 | -50.06384 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d1c0aac-b5db-3ce3-8ac6-2b50b46b831a | -11.71313 | -54.53953 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 3599732f-f1be-316c-843c-5b6e6d573722 | -16.15828 | -58.57798 | 2026-08-28 17:26:00 | NPP-375 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8f377283-d057-3a0f-a805-2644b71fe778 | -15.3603 | -53.79383 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 060ba11c-cfbc-390e-a888-5d9592d7c0e1 | -12.8648 | -44.3603 | 2026-08-28 17:26:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 65ddb65a-7e0c-36c1-bcb6-5c54a7155412 | -9.86662 | -45.85258 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 987f2035-6d01-3314-a265-9fbe20117915 | -14.03053 | -42.15379 | 2026-08-28 17:26:00 | NPP-375 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 91212e96-f0eb-3c4a-9c41-094ea3061d2a | -15.47739 | -53.96137 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b88fbf1c-eef9-398e-a46a-29cf0e0e2ba6 | -16.57907 | -49.78684 | 2026-08-28 17:26:00 | NPP-375 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 90b8b9a5-5eae-396e-82ae-f770a52c42a9 | -14.40736 | -41.219 | 2026-08-28 17:26:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 0026091b-e166-3014-862e-e9060d9ae317 | -14.92235 | -56.31256 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 9b1ff103-dd3b-3d93-be08-27c0d679e6d1 | -12.79772 | -46.45411 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6e3b01ae-8801-3492-88ba-d4554a16bcac | -11.65782 | -46.72683 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 935904f1-6e41-3050-8037-6be4866f0a94 | -12.77155 | -46.45884 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff4bfc06-0b38-3264-88f6-43e6ba223a5d | -14.24527 | -45.27594 | 2026-08-28 17:26:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 550449bd-9a7a-379c-800a-b4601a2db728 | -10.64193 | -50.65096 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README113.md)
