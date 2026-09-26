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
| 29a43747-7c0f-306b-a4ae-d60090b71e4a | -12.01872 | -50.65142 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35a06aba-f431-3256-9fa3-6f7896fc6367 | -11.85844 | -50.5473 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c2da2926-c6fe-3596-8595-2ace7224eeca | -9.47859 | -40.35708 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce946444-e63d-31bf-80a1-95d335f4019b | -10.76132 | -50.84331 | 2026-09-26 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b18ea89-2167-3e1b-bd25-21f430517516 | -9.47196 | -40.33367 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 4bb57dbf-cfc2-3508-ba46-debe08bfd203 | -11.77384 | -50.64598 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a916fe7-a72b-3b43-a90d-e99cfccc3c04 | -9.48606 | -40.33228 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa431661-48db-3558-86ce-30fecd3b0dc0 | -12.26257 | -50.72382 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c83fd04e-cbbc-3354-bcc8-383d91ed61bd | -7.40407 | -39.79156 | 2026-09-26 04:08:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 73ebbf67-2de6-3693-9d45-796708188a0e | -11.77979 | -50.64724 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da480d18-3e8b-3893-ab44-c0b94831edc5 | -7.36551 | -42.09486 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 518c60c0-8fee-353b-93e7-55a03019a173 | -7.36255 | -42.08986 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 67ac8024-2b00-3b56-81cc-439ee6c45d57 | -11.93086 | -50.58534 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce1a63e3-2cbc-37c0-b84d-04c83c25afcd | -7.40465 | -39.78798 | 2026-09-26 04:08:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 19.6 |
| bf56c643-8e26-36db-a286-852717b0aede | -12.2724 | -50.71921 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5669b5ae-3791-38da-b820-86bae06d2dec | -11.93416 | -50.59974 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c2011bc5-4cf7-39f3-922f-f4e1959c5a0f | -7.35071 | -42.09241 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ad98636e-1617-3e53-8281-62145cb99754 | -7.37217 | -42.07795 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0873451d-8481-34e1-877f-a10bfc5c46a0 | -11.78485 | -50.65292 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 044a46c8-46ce-3242-9096-ea15a30ab1cc | -8.11821 | -40.7471 | 2026-09-26 04:08:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 66921cd8-34b0-3c50-824b-6b4cba9c2793 | -7.40185 | -39.78384 | 2026-09-26 04:08:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f95fd151-1d7e-37fc-9145-d13c261e95a8 | -12.41178 | -40.924 | 2026-09-26 04:08:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f3f94a1-46c8-3a81-a1e6-cb9670d007cb | -9.47709 | -40.32337 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f64609f9-b2ef-351a-b72d-16de0f08bf38 | -6.70698 | -45.99456 | 2026-09-26 04:08:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8e63c72-afae-3844-9424-56afc8efcf63 | -11.84913 | -50.54717 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5aed5729-6082-37c6-8310-8b6fe6afa19f | -7.3581 | -42.08194 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b8a4c435-7f40-3045-9f44-dee775f7a060 | -7.40697 | -42.62559 | 2026-09-26 04:08:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2521986e-cf45-3239-8ccb-729288e4284c | -11.8618 | -50.54531 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c00664a-7f1f-3c9e-9320-d89def565083 | -11.92912 | -50.5941 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 776198d5-908d-337b-a043-4f07fd49162b | -8.34227 | -44.14028 | 2026-09-26 04:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cfb9c4e-3ab5-341b-93bb-4478d1329eec | -9.21623 | -40.55376 | 2026-09-26 04:08:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4a2912e1-5005-3f95-b734-765164b27ed9 | -10.75615 | -50.83727 | 2026-09-26 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c8b557a-351c-313d-92e3-84e0703f0361 | -9.47254 | -40.33005 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 193.4 |
| e6c759ba-5687-3a1b-af98-403172f07680 | -7.24517 | -45.26033 | 2026-09-26 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33551e9b-6d42-3e12-8e5e-dfc7f8e0d949 | -9.46182 | -40.33201 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| b928caf1-b8c5-3d5f-b675-daf9b8b58cc6 | -7.3522 | -42.08363 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 94faca21-f090-36d3-95b9-03581f6c353d | -11.92803 | -38.29763 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 4ffba1dd-d9be-36c8-89b9-ed7aeba82b7f | -8.14653 | -44.4473 | 2026-09-26 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9ce9ffd-b62c-33e9-be01-3e5ceafdb38a | -7.37291 | -42.0736 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e0cf1448-690b-31a7-b7cd-0933773ab37a | -12.26849 | -50.7251 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 026d8059-3112-3b41-b5e1-9f88c2f4dc55 | -7.35296 | -42.0901 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 742ce6c2-961d-3c9d-a5f5-fe41d641f80d | -10.76228 | -50.83853 | 2026-09-26 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efa533b1-dc5a-378c-8eb9-9021f2cd8326 | -13.06759 | -43.27673 | 2026-09-26 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cc034c4e-77a1-346b-bdaa-e36afa2091a0 | -13.57868 | -42.54322 | 2026-09-26 04:08:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c723d45-7d41-32f4-a46e-a5a5a40b63f5 | -12.25994 | -50.7371 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3df729e0-189d-3666-b3c5-0c57c7199415 | -9.47638 | -40.34927 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 30784f13-b96e-3835-bf2e-035aded703f2 | -12.27067 | -50.34585 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a4460a5-f450-3974-a273-24fa5e90f98d | -13.42541 | -43.67154 | 2026-09-26 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cd515e8-0b7b-3f8b-9793-06fd016c84fa | -12.34785 | -48.19814 | 2026-09-26 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23d4c82c-c69c-349d-bfd2-2552cd62144d | -9.47871 | -40.33479 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 096ee2e9-2270-36a7-a554-cfaf76ad08d3 | -8.34162 | -44.14399 | 2026-09-26 04:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8eacfb5d-cb59-3597-9f65-1a83c751cd04 | -13.42817 | -41.33428 | 2026-09-26 04:08:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9fa67693-eb23-3c9b-8911-878e2bc3a456 | -12.26937 | -50.7207 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3810023-fd0b-31d4-ab1c-85f8c33dea35 | -9.47813 | -40.33841 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 639ef796-d907-3465-b674-170d6ef6e017 | -9.46682 | -40.34398 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d8866761-e5a4-3bcc-899d-fb1252958a3a | -7.35664 | -42.07988 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 698975c0-0d95-3a82-a865-0f41f71f0c7f | -11.87941 | -50.56534 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64e638b0-a7d9-3c67-bc5a-4b077b36481b | -9.48664 | -40.32866 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ceeba77-83be-3b55-b1bf-488134636c23 | -12.25602 | -50.73874 | 2026-09-26 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6524e8e5-43a4-3c0d-a6a6-25c4189ce8fb | -11.76283 | -50.63904 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7fe537e-6fd4-3ac2-9fa6-5bab492f7d0f | -13.42878 | -41.33054 | 2026-09-26 04:08:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb60df44-ced9-3823-a5c7-30a7d10df2cd | -11.49668 | -42.33839 | 2026-09-26 04:08:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f78bf01c-15f3-3ce6-b1d1-735bd008b30e | -9.47079 | -40.34092 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 25564d08-6845-326d-af97-a9ef93d97ca3 | -7.3544 | -42.08132 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b79c958c-9303-3497-a9bf-2cc03e54297e | -5.86003 | -46.25886 | 2026-09-26 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fa6cdc9-4c25-3325-940d-d0b6399752c2 | -7.35146 | -42.08801 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fef076a1-f7c6-3d0b-9f6a-0a609e962116 | -9.48151 | -40.33897 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9f0ecab-d37f-32c4-af3b-3f680882d963 | -11.85164 | -50.55043 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2e6ea1d1-1036-3fd7-8e17-8ae749613f26 | -11.9393 | -38.29194 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 51f4ac76-4a20-3f5c-9d56-c37b7eda2cd2 | -9.48092 | -40.34258 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3653b86b-ff9d-335c-9b2a-6855002eea3e | -9.48489 | -40.33952 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca03f505-d6e8-34fa-988d-98265657a5c5 | -8.52073 | -40.23152 | 2026-09-26 04:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1996c48-ca2d-318d-a85c-29d3e281bdee | -9.46637 | -40.32532 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| b5edb29f-7810-3694-b04d-6279af906ed1 | -8.34639 | -44.14101 | 2026-09-26 04:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d307684d-d607-37cf-8a6c-a06a3c610dfd | -9.47592 | -40.33061 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 579ff589-d3ed-3e62-9cb1-5f8547aff752 | -12.65397 | -43.1602 | 2026-09-26 04:08:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 044a1840-a901-33a0-8215-2ba2fc961305 | -7.36034 | -42.08049 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 037535e5-4109-3492-aa02-351e43874948 | -11.92824 | -50.59848 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 64615a18-970e-3be0-b2a0-8052653092fc | -7.60934 | -46.45921 | 2026-09-26 04:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a824c2a-689a-3a39-bd93-346cf9f8c504 | -11.93197 | -38.29453 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b0afa8df-3170-3800-bcda-bf851db5047e | -11.8559 | -50.54407 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1fc7d321-aed8-3e58-bbdc-2c3e94380275 | -8.33659 | -44.12405 | 2026-09-26 04:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ccf2120-2f15-36cf-82af-f280680a115d | -7.36922 | -42.09547 | 2026-09-26 04:08:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ebae094f-5413-30e7-a6e4-7ee9251e8b9a | -9.47033 | -40.32225 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8f16490a-f302-3e18-a143-e480dd50bf21 | -9.47579 | -40.3529 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b8dafb3d-3275-3959-af0a-3885048d350a | -10.75696 | -50.83768 | 2026-09-26 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06c035df-4b67-3afd-8467-cae0259945d9 | -9.4765 | -40.32698 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3aad32e7-6684-3336-ad16-c71ed3a101c7 | -9.47417 | -40.34147 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0edcf60-13a6-37f6-9627-302a09025f91 | -12.03057 | -50.65395 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93a0ee92-d3a7-31de-8b93-d579d9a3bf6e | -11.8584 | -50.85443 | 2026-09-26 04:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84ee3052-e023-3655-95a0-79f3286953fe | -11.94324 | -38.28883 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fce6b864-1ed2-3dbc-9055-554d548ba765 | -9.47533 | -40.33423 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 54e0395e-e120-3066-9f97-a51ee8909b3f | -11.94663 | -38.28935 | 2026-09-26 04:08:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2db60a32-8d81-32e4-8f06-069e6f901d3c | -11.76373 | -50.63461 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e0b4280-3a6c-3454-9c14-e94fbd5abea6 | -12.13538 | -50.30419 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55fc71af-e8ba-3904-b10c-4719a5b9d6a9 | -9.48034 | -40.34621 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8306c21d-d10a-3394-80ba-b11290534d4c | -9.47371 | -40.32281 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 503407cd-53d3-30cb-9438-8d3fd8575cfc | -7.38189 | -44.76867 | 2026-09-26 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 969393ba-fa79-3294-807f-4665bacc4060 | -11.93503 | -50.59536 | 2026-09-26 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 396dd787-9cda-3339-876e-7991102c0f7a | -9.47696 | -40.34565 | 2026-09-26 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README10.md)
