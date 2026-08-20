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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e440c26f-bf06-33ae-be61-ca88807d39f7 | -11.2081 | -55.05172 | 2026-08-20 05:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 233f3319-4113-3f8f-9e5d-2c5adf65b854 | -7.43448 | -59.7899 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c7ddea1-e464-3dcb-afca-1bb867c81b64 | -9.15611 | -59.55347 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d975491-4984-3242-98d4-ebc8d98a92b9 | -6.70229 | -58.94073 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 165ac5b5-50d9-3e40-acbe-b114858759cf | -10.39405 | -61.21592 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 073ab19d-c69e-3927-a28b-a53f702b96d2 | -7.86303 | -63.76048 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac8e245b-3796-3958-bc54-a004c420e336 | -12.00227 | -53.44227 | 2026-08-20 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64b6ecd9-bfef-3cef-8de8-408731e48ed1 | -6.59352 | -58.96951 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb2a63db-22fa-3f82-a990-b5354b4fcf3c | -8.94761 | -60.56931 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a4218ae-8710-3e10-b566-6640d3f80c67 | -8.53403 | -54.86221 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2124f08c-ac29-3f9e-895c-ed88e23f7d9b | -6.58923 | -58.97322 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5a79c89-02e4-314a-8028-613cd53a817d | -8.64368 | -62.83353 | 2026-08-20 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95be6d78-0a74-31b5-9464-d07bc4a3320e | -7.8775 | -63.76632 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5eddffb4-3874-3063-934e-58cdc8a3218f | -6.84303 | -58.99501 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ba2dd5f-ed21-39ed-852a-0053804d3806 | -11.99756 | -53.43371 | 2026-08-20 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ddd5f54-56cf-394f-9be3-06bffd1a3e29 | -8.4974 | -54.87373 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 20c3060a-c02d-34ff-8a04-937e35be885a | -6.69494 | -58.93972 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 32e47993-4fbc-39c2-912a-ddb9fbc9f342 | -8.95112 | -60.54614 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a888f8be-8271-3713-99fe-6dbe5063bee4 | -8.28443 | -62.90084 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2814a21-1ce2-3c31-9100-8b4fa38da549 | -7.87472 | -63.7622 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cecd1f40-b142-38b3-ac8a-0865c9a1231c | -8.57929 | -54.7557 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1aacba4-db92-37d6-905a-862bbf469c67 | -9.12134 | -61.59899 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49ca8570-75e5-3264-b28f-c424ac042ce9 | -6.69861 | -58.94024 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 13f9d074-0698-35c9-ba77-05f7a459b3df | -8.57408 | -54.72834 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7f248f6-a028-3ffe-86c4-9d5d26b65129 | -7.71229 | -56.72776 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a318597d-a113-3054-bea7-8dce1d1fdf3a | -11.19075 | -54.0253 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb6b438b-130f-3e73-a326-367f71bc873a | -8.51364 | -54.86484 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4246d04-4021-30aa-9516-47e744c6755d | -8.71843 | -49.6131 | 2026-08-20 05:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8e545f5e-ea79-321c-bd10-0433b3865183 | -6.86838 | -59.02502 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffb9adce-bbba-3201-b9ef-282e812f954f | -6.77291 | -59.45351 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06edc6f9-e7ba-3ded-a038-89014fceecdf | -6.85074 | -59.01807 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d5478c4-1bad-3ea9-8fa6-b3a856a18edc | -8.52345 | -54.86624 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f35ab6f5-4689-3f06-a912-a060bf96ceb2 | -7.47718 | -55.31764 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6c01202-c370-3d75-bebe-410fa02a71df | -8.49249 | -54.87308 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 806dfa63-b292-360b-8742-afea59b4a8d1 | -11.17951 | -54.02731 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12cf0ad9-1721-3a13-b81f-c4616b7a0431 | -7.054 | -56.61048 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db860919-a9a8-3ddc-ba01-3f1f9885b2a4 | -10.33429 | -57.56733 | 2026-08-20 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 865d1dfa-05f9-3aa2-bf14-6c4a706feca6 | -11.20923 | -54.00996 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2243e82-c848-30af-8b63-7bc9c5e1cf2d | -6.71396 | -59.08581 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 511d0936-9554-3ac8-ba46-d8bab665700b | -6.87138 | -59.02983 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4869d40a-a6a1-3108-b6be-db222d015c98 | -6.70359 | -58.93207 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0075a087-be5f-3a05-b496-5574bcbd9a56 | -9.02682 | -60.49457 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3fe53a1-dc30-3081-8aa9-e214a2b1f731 | -8.66987 | -54.65574 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76ec90b3-a969-3b23-b0c6-ebc8f646d650 | -6.76701 | -59.15247 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87f55137-77ae-37f1-99eb-73f5d194c4dd | -9.42098 | -60.41515 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5196a21f-1abb-349d-b66b-a29064c6b639 | -8.566 | -54.67508 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9b75c16-c72c-31a2-a4c9-15ed91da4bef | -7.60852 | -60.95479 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8b1aad-c5a6-3931-b6a6-b818c9309c7e | -11.18624 | -54.01771 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cba6c08-7fe6-3127-ae7b-2a817a0d988b | -11.20875 | -55.05761 | 2026-08-20 05:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0f6232ab-0c33-3718-a89a-de4a7bdadc3f | -10.91098 | -56.37173 | 2026-08-20 05:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a1f5ebd-634f-3662-83cc-817ba88ebd6d | -13.40454 | -54.38106 | 2026-08-20 05:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2b9a51f7-7164-3946-aed5-6b1eadc9a322 | -6.59416 | -58.96527 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94f41e7c-3efd-359e-821d-49fe1df12838 | -6.88954 | -56.44409 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c57505f-c395-36fb-8079-80a75dcf9976 | -11.24161 | -54.82936 | 2026-08-20 05:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa6b465c-7dec-3662-981a-31edadbefc7b | -9.11349 | -61.60511 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7576d4a5-a9a8-397b-be0c-af7d6697b872 | -9.215 | -59.78134 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4bae2d93-124e-3eb8-be1d-4732a8d0375e | -11.83356 | -58.83574 | 2026-08-20 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0138ef28-c31f-3568-b6e2-911ad0a65194 | -9.10361 | -60.34906 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a60f3fb3-5e44-3dc4-9e6a-6af37f45c77c | -10.39177 | -61.20783 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8adfacf2-54bd-3d67-ae8f-c9413be8ae14 | -6.75485 | -59.15935 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7db30746-0b3a-340f-a30c-e367f4b5a9e7 | -8.56179 | -54.66865 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c9b573b-b8ce-3a46-a9bc-a2245162ac8a | -7.77188 | -61.1399 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a12b3de-58a7-358b-ae1c-f68e9d154529 | -7.54184 | -55.58024 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 829f0404-c744-3c6b-b755-38685fa45c9b | -7.60456 | -60.95789 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b64543b4-e666-37d3-9b61-38938190ac60 | -9.50251 | -51.68335 | 2026-08-20 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5fe4a51f-9b52-3046-b01c-96dff9464979 | -13.6145 | -51.79096 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d42ca3d-c25f-3d32-8328-84f85ebf4340 | -12.49706 | -54.74699 | 2026-08-20 05:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a87008d-98fb-371e-ac52-7d9d1616f8c9 | -7.7685 | -61.13936 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec79eab4-b203-355f-b85c-6ed0730c3bcf | -6.92292 | -59.3495 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d933e13-ebc2-3d10-9370-566fc70c529b | -9.20967 | -59.7677 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b44f9d2-a39b-3712-8dc0-650a177213df | -10.32592 | -57.56611 | 2026-08-20 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc05f60d-e6ca-3ec4-9373-2221ee4101da | -13.61388 | -51.7963 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 31b5ad53-0a8d-3cd9-a93a-d04a92776e18 | -8.55737 | -54.66002 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fe753f3-5240-3810-bfce-735f9112d3e1 | -8.49887 | -54.86308 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48c3c66d-e2b0-3eaa-a9b5-5443f65513bf | -9.22223 | -59.78245 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e16b7628-8945-39ca-b841-7f84973da032 | -7.60569 | -60.9506 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 456b9a2d-2173-387f-b24d-1ae60d5efe6f | -7.55308 | -55.56742 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 692b071a-1893-3898-a55a-774ee28bd6c8 | -7.10577 | -59.77097 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9bb06ed-cad9-3cc8-8ef0-e2c5da163076 | -11.41893 | -54.31265 | 2026-08-20 05:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc40f1a-62c9-356d-99e1-e087e00bbbe2 | -9.21988 | -59.77353 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 800d557c-0c84-369e-9a9e-3456170f7963 | -13.54265 | -52.23017 | 2026-08-20 05:42:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ea64c2e1-3a99-37e7-8630-0da6d24e7ebe | -6.84237 | -58.99932 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3212048d-6030-3dbc-98b9-fe55189b8746 | -10.38087 | -61.21003 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 973cde83-352b-31fc-9f2d-6cd7ef63cf70 | -8.58663 | -54.74774 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f3cf979-3471-3c9c-9475-569cfeca288f | -6.7011 | -59.09695 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d481f630-e8db-3b72-b21f-6e276184d3c6 | -11.21554 | -54.00372 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c34d4f8-f74f-383e-a876-9dee98753e8a | -7.55376 | -55.56263 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f1c58b9-9f67-3148-8888-e6a33dd5e1e4 | -6.91573 | -59.34839 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7fc2b3cc-7947-3024-b636-0dcdec3080e1 | -6.8544 | -59.01859 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdc82a9b-011e-311f-ab1c-fbacdbfd5f0a | -6.79164 | -59.58704 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9165945-94e1-3216-a6b7-0b8d3ee4e543 | -8.51288 | -54.8703 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37b117ae-84b1-3c2e-8b76-afe698105751 | -11.1984 | -54.00863 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7460e11b-7d61-37e9-8a77-0e91c70c5b1c | -6.81245 | -58.99908 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a30395b-2499-3541-b05d-80bdd110201c | -10.39119 | -61.2116 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 118acc57-d6e2-3f88-9a83-6e7e33b3e81f | -11.21224 | -54.00259 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f55fd19f-afda-343d-853a-fcd3bc3dad20 | -6.79934 | -59.58414 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ba185aa-0f05-382d-b25e-c10aca47c7a9 | -8.67609 | -54.65031 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b4bb984-51ab-370e-9cc1-b4fd634e53df | -10.39463 | -61.21215 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c80b7735-61eb-3433-8b7e-ba593d858a8b | -8.53572 | -54.86488 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c4155aa-7f02-3e1a-831f-18f5469594a5 | -8.95051 | -60.57368 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README61.md)
