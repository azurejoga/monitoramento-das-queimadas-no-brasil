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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5d98c32-2ea5-36a5-bf38-6a303774cd13 | -17.29621 | -46.06079 | 2025-06-29 12:29:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6e1aa809-1890-3e81-adfe-1be01d32ffc2 | -13.48129 | -47.72188 | 2025-06-29 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7bd122a3-1e5f-36d6-9945-4c34717bc4fb | -11.57026 | -44.83806 | 2025-06-29 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5125abf6-3c15-3d48-9597-65a5a37b1da3 | -9.55029 | -50.7733 | 2025-06-29 12:29:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6ad026d3-d4b3-3d84-83ff-00b9ad29442c | -12.10635 | -54.5787 | 2025-06-29 12:29:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3d8987b8-7d51-3220-9c63-8f4b8861da86 | -10.94754 | -45.59978 | 2025-06-29 12:29:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f3553c4-958d-3aec-adb9-6c49b800becc | -12.90758 | -48.06572 | 2025-06-29 12:29:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de49a290-c004-3b40-8c9a-8c6f238fe0e0 | -14.6704 | -47.98075 | 2025-06-29 12:29:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e4c021e-062d-35f6-a558-d398eae3998e | -20.24765 | -46.73402 | 2025-06-29 12:29:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4972a95b-a97b-3ba8-99df-49dadab02f9d | -9.53912 | -50.78244 | 2025-06-29 12:29:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| d5f3d61b-c627-3800-8c31-87ce15033f4a | -12.94261 | -46.95308 | 2025-06-29 12:29:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 62e2cad9-280d-33f4-b362-c14ce073f863 | -11.54021 | -52.77534 | 2025-06-29 12:29:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 0d75d879-fa8d-3598-8171-aebc5c6ea97c | -10.98209 | -45.11902 | 2025-06-29 12:29:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dcf8a8cc-b49a-3191-9fc4-3011704cd552 | -11.57204 | -52.11192 | 2025-06-29 12:29:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ab1f811a-3eb1-338b-b8bb-8fc00a1b0b7f | -11.03484 | -56.27197 | 2025-06-29 12:29:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 65d60ea4-605f-3549-94b6-5e3840311567 | -10.65676 | -44.47763 | 2025-06-29 12:29:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 60fed2d6-0ce8-3c72-b378-13efe60774a2 | -11.55085 | -52.77699 | 2025-06-29 12:29:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 1cedb747-ad7f-3550-ae8f-e276a5e65aad | -10.64927 | -44.48386 | 2025-06-29 12:29:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 0b5bdad1-5a6d-3b60-9d5e-0c3dcb04af0a | -10.6483 | -44.4861 | 2025-06-29 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 3bf6b529-cf82-37c7-9e28-188ca51a7c9b | -21.01704 | -50.1656 | 2025-06-29 12:32:00 | TERRA_M-T | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 6ec091f7-eadd-327e-b328-ee9e1a12c625 | -21.01571 | -50.17508 | 2025-06-29 12:32:00 | TERRA_M-T | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 2480e437-8600-31a5-af92-a25912273dbd | -21.72481 | -48.67544 | 2025-06-29 12:32:00 | TERRA_M-T | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d4b884dd-e0f4-360e-bd20-e739c0b2b5ed | -23.66748 | -51.67441 | 2025-06-29 12:32:00 | TERRA_M-T | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| fa8461ab-f380-3018-a16e-3ba1ad477555 | -23.65863 | -51.67291 | 2025-06-29 12:32:00 | TERRA_M-T | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e1157f8a-05cf-36f7-846f-cb9b82f0d1d9 | -21.72343 | -48.686 | 2025-06-29 12:32:00 | TERRA_M-T | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6066fbd7-cc30-39f6-a893-4abdee8946d9 | -12.4843 | -58.4795 | 2025-06-29 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 26ae8163-f7ae-3f85-8739-cbea61c59dea | -12.4843 | -58.4795 | 2025-06-29 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 7e5ac1de-28ae-3e63-a679-1f12e282200f | -12.4654 | -58.481 | 2025-06-29 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 7af84e96-c457-366a-ad9a-c2270cf5a282 | -12.4843 | -58.4795 | 2025-06-29 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 86b033f3-9830-3c66-aeb3-2c9933f1508f | -12.4654 | -58.481 | 2025-06-29 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 88854aaa-91a8-3e6b-8d6c-1edb239406e4 | -12.4654 | -58.481 | 2025-06-29 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| f9adb06e-20e5-3911-8baa-69675be96fd4 | -12.4843 | -58.4795 | 2025-06-29 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 298.4 |
| 99c48570-0b16-38da-a153-420bcbe3de13 | -12.4845 | -58.4597 | 2025-06-29 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 303e9746-2198-3658-b926-e303ee01930c | -12.4841 | -58.4994 | 2025-06-29 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e772afac-9652-3b48-a517-63c201e438f9 | -12.4841 | -58.4994 | 2025-06-29 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a3cec13c-fcf9-38cf-8312-116cfa83d962 | -12.4845 | -58.4597 | 2025-06-29 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3faa272b-563b-3927-abe7-21256513c476 | -12.4654 | -58.481 | 2025-06-29 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 76d4eaa7-d946-380a-b423-df51679fa9a0 | -12.4843 | -58.4795 | 2025-06-29 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 299.1 |
| c1654fda-4b86-344b-afbc-e49bde59ad9b | -12.4843 | -58.4795 | 2025-06-29 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 349.0 |
| 82e5bda7-0f56-3fe0-bac4-99987e272c6c | -12.4845 | -58.4597 | 2025-06-29 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d94f7cde-04e6-3be9-a088-42001132eadd | -12.4654 | -58.481 | 2025-06-29 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 996e5413-5df8-396c-8552-d054d5e9a22f | -12.4841 | -58.4994 | 2025-06-29 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| b9366538-3472-3e38-aeff-b3da47ee3416 | -12.4845 | -58.4597 | 2025-06-29 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e62a4c96-c7b1-3b27-8c2c-679a0434e2a0 | -12.4654 | -58.481 | 2025-06-29 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 9f87d624-b61d-31c6-93b3-ad92460bccea | -10.876 | -53.7614 | 2025-06-29 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 51d704c6-435a-33ed-8673-c6f27f073a06 | -12.4841 | -58.4994 | 2025-06-29 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 6ccae804-2bf3-393a-af05-b01b4f5ac039 | -12.4843 | -58.4795 | 2025-06-29 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 363.9 |
| 2b5f09bf-5a88-3672-a7b9-687135ccafbe | -11.1903 | -55.9101 | 2025-06-29 13:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f8ed3ad7-d671-31b1-a7cf-99d4dda5a2ed | -12.5048 | -58.3393 | 2025-06-29 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8593d286-6d30-3c47-b0af-3a4dbe8c3622 | -12.4845 | -58.4597 | 2025-06-29 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| fa38bc0b-fd04-39a1-a888-8587704e4487 | -12.4654 | -58.481 | 2025-06-29 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 00f67c7b-6456-3107-8823-916f6a6400a2 | -12.4843 | -58.4795 | 2025-06-29 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 307.6 |
| be1dd7a9-0e28-3787-af5a-9472573158fb | -12.5048 | -58.3393 | 2025-06-29 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 98b162b9-2d66-3236-9ba2-1014ebd2739a | -12.4841 | -58.4994 | 2025-06-29 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| c76739ae-3eef-3e87-a055-084e6bb54597 | -11.5499 | -52.7867 | 2025-06-29 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| ec448091-7cbe-34e8-8c54-2652c22120dc | -12.5046 | -58.3591 | 2025-06-29 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 264d5e13-48ca-3f08-8961-43ec4c99f02e | -11.1903 | -55.9101 | 2025-06-29 13:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| f1f7260f-1a05-328e-b822-005d8681d5ef | -12.5033 | -58.4781 | 2025-06-29 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| eb564fe0-39f4-3d51-8a4e-040beced68ad | -10.876 | -53.7614 | 2025-06-29 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4a014369-3c94-382a-a5d3-8bf9a38186fb | -12.4843 | -58.4795 | 2025-06-29 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 388.9 |
| 01838208-c8d0-38ed-928d-e979a1958608 | -11.1903 | -55.9101 | 2025-06-29 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 74971d14-9352-3904-adaa-42c15b4fdc89 | -11.19 | -55.9303 | 2025-06-29 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6d162095-e8ec-334b-9c99-a7963de5e93e | -12.5048 | -58.3393 | 2025-06-29 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| da5e97ca-5294-3a36-8c05-a3793fb9b7fc | -12.4845 | -58.4597 | 2025-06-29 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d8765bb0-e4bc-30eb-b2ab-5ed454e0fa0e | -12.4654 | -58.481 | 2025-06-29 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4f3ccb1b-4aa8-306f-934c-2b3367abef80 | -12.5046 | -58.3591 | 2025-06-29 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| e4474542-a3c2-3286-9b24-d46e2b7c8e92 | -12.4841 | -58.4994 | 2025-06-29 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| afb203f1-3fa2-3b25-bedb-8c1758c947a5 | -10.876 | -53.7614 | 2025-06-29 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| b833e905-e21c-352a-bf82-6778562235eb | -12.4654 | -58.481 | 2025-06-29 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| c72eddd7-072e-3c64-87af-777d336c9d43 | -12.5046 | -58.3591 | 2025-06-29 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4ec4a4d4-c3b5-3b0e-b210-89f479545976 | -12.4845 | -58.4597 | 2025-06-29 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 6b110574-118d-3c9e-957d-17174ccc0c70 | -11.19 | -55.9303 | 2025-06-29 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 5200e2ce-9cc6-37d5-aa71-29dd44e4ac2c | -11.1903 | -55.9101 | 2025-06-29 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f355c166-7cd9-3472-bbca-8559408c2dd5 | -10.876 | -53.7614 | 2025-06-29 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| b8322495-7901-37da-b851-eedadb01947d | -6.9108 | -43.9834 | 2025-06-29 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 90ea565a-0b60-3914-ace0-b8b721697d8a | -7.2588 | -43.1351 | 2025-06-29 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 900e8c4c-bfd2-35de-b497-b93370b87d0f | -12.5048 | -58.3393 | 2025-06-29 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 02dcd13f-a983-3d90-b2a7-124d43df2864 | -12.4841 | -58.4994 | 2025-06-29 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| df0dc85c-9907-329f-9757-df4308638810 | -12.4843 | -58.4795 | 2025-06-29 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 466.1 |
| a0c2dfc9-b25e-302a-bdd9-c8af21a77dc7 | -12.4843 | -58.4795 | 2025-06-29 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 511.7 |
| 2cb660e0-2aa6-3cc7-9496-a203b6c80d64 | -11.1903 | -55.9101 | 2025-06-29 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| ade9e38c-a198-3518-ad56-ea47891cf710 | -12.5048 | -58.3393 | 2025-06-29 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| d44fbe51-47be-35e8-b8e1-94b400ce868f | -12.4841 | -58.4994 | 2025-06-29 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| dcdb55b5-bc74-35e0-8997-ad3be2814e5d | -12.5046 | -58.3591 | 2025-06-29 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ec6f7812-7b24-35e6-bdab-52ce9e2d5e5a | -10.876 | -53.7614 | 2025-06-29 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 073da163-75ba-33c8-ad2a-0c6c0c87acb2 | -12.4654 | -58.481 | 2025-06-29 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 98a6d12e-97d4-3d33-9141-5e9dd3ce342b | -12.4845 | -58.4597 | 2025-06-29 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 604d6f13-5223-360a-ad22-bb8235be062a | -10.8762 | -53.7408 | 2025-06-29 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8c21a6f0-05cd-31bc-af7a-ecc66ac5ea0c | -11.19 | -55.9303 | 2025-06-29 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 826a93fa-5e0c-3d56-b132-4339d865bacd | -7.2588 | -43.1351 | 2025-06-29 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 558fcd68-124f-37f2-895c-66f0a08e0714 | -11.19 | -55.9303 | 2025-06-29 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| b198b426-e7e1-332f-8264-181535c517f4 | -10.8762 | -53.7408 | 2025-06-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| dd3ae2c0-3b54-30fa-afd5-1ece92624633 | -12.5048 | -58.3393 | 2025-06-29 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7e9b07f9-f303-36f0-8405-f3b8c816af97 | -12.4845 | -58.4597 | 2025-06-29 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 28ed7fd1-42c3-3bc7-ad2e-a987389ebb38 | -12.4841 | -58.4994 | 2025-06-29 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b26e49f0-65b0-3ef7-85ca-21f96f6928b9 | -12.5046 | -58.3591 | 2025-06-29 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 47e15f61-09ed-383c-b8c5-565a56f90164 | -12.4654 | -58.481 | 2025-06-29 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e4899546-23fe-37f9-9540-eb9672d6192d | -12.5033 | -58.4781 | 2025-06-29 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| b9ce2c79-f87e-3694-8802-a7a5c24a5077 | -10.876 | -53.7614 | 2025-06-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 78c27eac-4377-3eb6-a75b-b18b26134522 | -12.4843 | -58.4795 | 2025-06-29 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 389.6 |


[Clique aqui para ver as próximas entradas](README31.md)
