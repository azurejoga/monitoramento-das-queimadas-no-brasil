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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7aa630c-07da-3cba-a7f0-62955319c75c | -11.24949 | -45.04161 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e8f1e3e-c1bb-3e66-8bd8-a85dae4d8a75 | -9.43563 | -51.57887 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbb833cd-6a9b-3c6b-b7f0-1f84028fcbdc | -13.61238 | -45.77799 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cecf4dfc-5d59-3065-858d-5e7acdc58cbf | -8.60143 | -54.71821 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 323ec5f7-3e64-363a-83bf-0771eaa0449e | -11.27618 | -54.03202 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 865b620f-0414-3b58-946d-5f16b8aec8f2 | -11.65444 | -46.74112 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 282ef462-39fe-34a8-b0b2-b0edd39a4ec9 | -11.50211 | -45.05756 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ae9de34-7c74-352e-bc51-73c3afe2af2f | -11.75776 | -54.52097 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70f85513-fcbf-3eb3-8b70-45cea3104836 | -11.83102 | -47.21661 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe1fb388-5b30-31e9-b312-d84d2c74a2da | -8.59604 | -54.78064 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 95dbca53-e174-31ce-a0cd-e2bb41228c63 | -12.20557 | -50.5738 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f93d7b0-7cf1-300f-8dd8-dfcabce943b4 | -13.45808 | -43.84431 | 2026-08-28 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea391a28-b415-35aa-a2a5-394e786f6a38 | -10.9326 | -50.53675 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| df35deb7-177d-3c35-b25c-8db216d2d89c | -13.28696 | -46.63838 | 2026-08-28 04:17:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d757310f-f4a1-359c-a2d3-581dd5028768 | -14.85865 | -52.62223 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aceac3af-5cd2-36da-98d5-47c44e5e7f00 | -13.32976 | -48.19716 | 2026-08-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c12a182-503a-3f8c-8409-f20f5241db42 | -11.22054 | -53.99173 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc10d39f-c139-3a7e-845c-7c39ed08cd8a | -11.66053 | -50.46188 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4d220ce-d65f-3d36-b002-14b0a1fc3e08 | -9.16034 | -49.96777 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71368df5-61e1-3867-8b06-7154da85eb74 | -12.28926 | -50.59745 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a58d42af-b349-32cb-81b8-f6d0fe934f21 | -12.28644 | -50.58854 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 92975a11-9526-3a26-a20e-9ed31f89878b | -13.4242 | -51.86492 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4690b098-4cbd-327f-b06a-8e030771522d | -15.52861 | -41.9203 | 2026-08-28 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1f6f5bba-3fea-32a9-aaed-c9b1f8517041 | -9.08088 | -53.04008 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 836976b2-0fdf-32cb-bbfd-0a937bbac1e8 | -15.85155 | -48.10849 | 2026-08-28 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a328a33c-9724-33d7-9bb0-9c410895ba21 | -14.87838 | -52.59387 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a2a5a2a1-f334-315f-ab42-5ff3ea2ca175 | -12.25385 | -50.57418 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d90a8236-4f2a-31f7-85cc-e80a7a505b4c | -9.43565 | -51.68814 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c4c2fbd6-06a0-33db-938b-38e779279ae3 | -9.65672 | -48.30243 | 2026-08-28 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c61b08ff-244f-3aad-95f8-52446a46ec40 | -10.96563 | -50.30282 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 799e9e01-92c3-32eb-8324-4c5df1a94e67 | -14.32463 | -51.70688 | 2026-08-28 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 251c5908-b244-34dd-97f7-47a55c7a0a21 | -14.89132 | -52.60184 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2f43b13b-608b-3ed7-b398-d50127f7f6ea | -10.57667 | -57.48852 | 2026-08-28 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52cc69a2-e05e-3609-b3ed-60d1d131e016 | -12.05787 | -47.1632 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3deecdf1-0974-319e-9a84-9e55403ff95d | -12.69355 | -48.43156 | 2026-08-28 04:17:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ebad54a-8ea3-3e18-b903-aa7b20f4b27d | -12.20647 | -50.57487 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 46302de8-0f0b-36d7-95e4-512f006ea27b | -8.61949 | -50.01533 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7393c82-079c-3452-be2d-3850a0a4c84f | -14.87051 | -52.60018 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a0e1f18a-ac30-31ce-b508-aa268b466c17 | -10.92827 | -50.53597 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bfbce309-e204-3f60-bbee-e55ab7afd9ca | -10.94128 | -50.5383 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1caa5e5f-056e-3ed7-8bcb-a86f798491fd | -10.75824 | -54.02794 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a72cd75a-08ed-3b1b-b7f1-b0908e12fca2 | -10.96532 | -49.57417 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89754f6a-d45b-384c-b3fa-adb803099c76 | -9.96707 | -53.93868 | 2026-08-28 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 628e35fe-8bb3-32d0-810a-ab76d7e5b010 | -12.78102 | -46.44278 | 2026-08-28 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e356012-de88-3e85-bf9b-c2de3afdf4ea | -11.21921 | -53.9988 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 516d077a-11c3-35b7-af87-552f9a5ad26d | -12.28854 | -50.60152 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 86db717d-49de-3c4a-8a3d-f96338be2279 | -13.60124 | -45.78352 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4975b47-5764-3504-ad35-144adbb1bf7a | -22.52949 | -48.7404 | 2026-08-28 04:17:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6a16326-f411-3991-9829-14565082e1cc | -11.63522 | -46.74982 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72e9e747-a21a-3057-94f3-7064f57ff36b | -14.15602 | -52.83705 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2077093-a7f7-38d0-8964-bc670a4bc77b | -20.81791 | -57.32276 | 2026-08-28 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1e57b05f-3c77-3630-9909-5a980959af31 | -11.46523 | -46.94798 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 145d378f-b25c-3ae9-9196-d652d3b13bbd | -9.16685 | -49.96883 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd8e2623-6c79-3a6d-9c67-2b0fdfd34fbe | -13.43204 | -54.01702 | 2026-08-28 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f1e4b60-6c66-31d4-b3f2-c8f3ab7fd4ba | -9.61215 | -55.11797 | 2026-08-28 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| eafa5aaf-eabf-3e94-a322-3b9ee70971b7 | -13.40672 | -51.42013 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b99304f-1710-3450-bb93-d148b97e4674 | -12.50583 | -43.80757 | 2026-08-28 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1d8814ff-98a5-313d-86ed-fe575c94af49 | -16.05037 | -47.2295 | 2026-08-28 04:17:00 | NOAA-21 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d764c499-5a50-31fe-a8d7-65ba108fffbc | -11.72146 | -54.52944 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d01f4803-afeb-33ef-9086-13a7dd1ce34f | -11.49315 | -45.11397 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f339c8b3-542b-39b4-a2e0-1164e4f20145 | -10.06842 | -46.94267 | 2026-08-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbd8d79a-b3c0-310f-802a-9070c9ac90ea | -15.53163 | -41.92521 | 2026-08-28 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 3862e2af-aaca-3093-bfc8-795efb06a8cc | -10.83501 | -50.52477 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28c5cc79-9b01-3a14-ab00-df570b68afe7 | -12.4302 | -42.8932 | 2026-08-28 04:17:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 02a6167d-7977-3ccc-9ad2-d2ccc19ffbf4 | -11.51478 | -58.51025 | 2026-08-28 04:17:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e7d2058-18dc-3c56-ae48-1da4f61d68ba | -13.61123 | -45.78516 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd3e5560-39d3-3fb9-98bc-abaa7d65aa5e | -10.53123 | -43.98431 | 2026-08-28 04:17:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e142b1a-12f2-33b1-bdc8-9c17ea1b8919 | -10.80056 | -54.0168 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51b61108-a509-359d-88b3-77952a78d833 | -11.72334 | -54.54947 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa9d8bd7-8751-3ce1-a22a-863c9447da9c | -11.28774 | -54.03052 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0d440946-f52c-308a-9813-772f5bda6e0c | -11.29385 | -54.02803 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 71c3d00d-444c-3b26-955d-257a4b853bcb | -8.779 | -49.95512 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a249c48-0ac8-3b4a-b85d-64fc53af7ce1 | -10.7617 | -54.03971 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ad50590b-79c9-3263-918e-3974ff415738 | -11.65162 | -46.73658 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1258eb59-820a-38c2-9bf4-2210b664ac5d | -15.72612 | -42.22202 | 2026-08-28 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a25bf8d7-0753-39c3-ba21-810ce68a7a99 | -11.01081 | -49.65051 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aefd2557-a0fd-34f1-a2e4-cb6543592853 | -8.81099 | -50.08186 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aea13c83-ea94-38dc-90fd-a3ac56cfde53 | -11.71925 | -54.54079 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9bd2f00-823d-3c8f-824b-a94b3372d645 | -11.19483 | -41.99644 | 2026-08-28 04:17:00 | NOAA-21 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa719bb2-5dad-3e48-8d00-715136a5be33 | -14.89409 | -46.37553 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 064db459-f994-3238-93e9-0eeb0dab6f9f | -11.27416 | -54.01323 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| faa3c9ef-9147-39ac-96f5-44be363b2a20 | -11.18547 | -51.22772 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 1982cf01-01c9-3735-89f3-c66279c78dd9 | -10.78736 | -50.63966 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 833e2ab4-7656-3084-be98-82ecce530f29 | -8.77612 | -49.94603 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c5587f6-d2ff-3cac-a969-991da8c90a3f | -11.1637 | -51.21882 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17c6a295-493e-3b32-8385-2bc022a6ebe7 | -11.82327 | -47.21954 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a9a28faa-f76f-33f6-aec4-0bce5b6bae7b | -11.70974 | -47.80053 | 2026-08-28 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a4665a0-a736-3dc5-9363-8458d9bbee13 | -12.27648 | -50.59512 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 25ae98db-aaa9-35d4-9cb3-1c063d72486e | -11.48987 | -45.11359 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff951168-c14c-3c61-962e-2041f2354041 | -8.78115 | -50.07243 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1aedc0b-652c-390a-80f1-49de30b7451a | -11.27143 | -54.02745 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49a096b9-f901-3798-aaca-0f8d87633107 | -11.01384 | -45.06894 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 435dba11-6ef7-3358-aa90-a9f3d4f6a452 | -11.53807 | -45.51285 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21cbdaab-61fa-3061-aab3-8f9e2fe7d15b | -11.83522 | -47.21318 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bc9962a8-772b-3947-aa66-9c7616a15590 | -9.99465 | -48.59739 | 2026-08-28 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b48d0cb6-561f-37f4-88cf-b31b9b227b8a | -11.53459 | -45.51916 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2c06c16-e578-311b-9038-ffa41e801a21 | -8.59522 | -54.78503 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5af9f97f-00f3-3250-b0c4-cf6b929d9029 | -8.78045 | -49.94677 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71a4c602-90fd-364e-bcda-311d10a95837 | -11.71342 | -47.80409 | 2026-08-28 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6e61903-9bcd-3bfa-b404-0b46c40fd447 | -11.98023 | -45.49327 | 2026-08-28 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
