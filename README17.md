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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2aa8840-5992-39be-8ac0-d1ca69ff1c80 | -8.598 | -54.750801 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91f0922d-ac2e-38bb-b5cc-e656e976fe82 | -10.7542 | -50.8699 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e57ea50-a9d0-3c01-b2dd-ffd8aba67dca | -14.7635 | -48.742199 | 2026-08-30 00:55:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8b68d4e4-7b0c-38c6-8d6f-22f80e8cbd88 | -11.0055 | -50.527199 | 2026-08-30 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 599b742b-7660-3d81-aaaa-903315dfcc6e | -6.3634 | -51.741798 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae69d4ec-56b9-3b2d-85c1-326dc306b8f2 | -14.3964 | -52.553699 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d43db51-2deb-3ed7-b922-dab7ce978eba | -10.9565 | -43.0476 | 2026-08-30 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3125f79a-2f0b-342a-a9a2-eb40bb378c7d | -2.914 | -54.108898 | 2026-08-30 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d499dae0-5ffe-3a69-8fb9-b8f26413bffc | -8.6173 | -54.698299 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3679b409-2c14-38e9-b3ef-2576e2109025 | -4.1492 | -60.670601 | 2026-08-30 00:55:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1c062da-46e6-33b6-b1f0-ffbdd4aa0433 | -14.2128 | -52.844002 | 2026-08-30 00:55:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7277581a-8099-3834-9eea-792e3bff8635 | -11.3331 | -45.135201 | 2026-08-30 00:55:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93babf0c-4191-35c1-9c54-1187519b5958 | -8.6049 | -54.7817 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c584621e-8d0a-3fb5-852d-8950d14f1ec8 | -6.7416 | -55.6511 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0171bc9-47dd-307f-8f19-6316f39c1b53 | 0.2225 | -51.441101 | 2026-08-30 00:55:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7785cf28-4451-387c-9099-63951ae4185a | -9.7026 | -60.7351 | 2026-08-30 00:55:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1612f2d3-67a7-3282-ab4c-60ac9dcebd9f | -7.4986 | -55.310398 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dcb4121-c819-30e1-9069-314b4f801f0f | -6.3496 | -44.085098 | 2026-08-30 00:55:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46461577-cc77-3a3d-95f8-31e3237b10c6 | -7.3075 | -49.542301 | 2026-08-30 00:55:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf68c91-9798-3ebb-9a9e-728068545653 | -11.2964 | -54.030102 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b278fedb-1f00-30a3-a412-f9817fee41d7 | -14.7696 | -48.724499 | 2026-08-30 00:55:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d7557b0-4a9b-3894-b993-c81bd33732b8 | -6.8599 | -59.482101 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b733c055-3ac4-3015-9434-666315450005 | -11.7218 | -54.525101 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b57f6f59-c6ea-3d1e-8a33-1725c0f38e00 | -11.2373 | -53.9949 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a500002-e9af-3faf-b7e0-c9792b8e4d67 | -15.644 | -56.393101 | 2026-08-30 00:55:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57f63e85-e74f-356b-a2fc-196b89e9b17c | -14.1655 | -52.815399 | 2026-08-30 00:55:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51e2b33e-1e0f-36b7-9be8-4d92d07bff7b | -9.8852 | -60.287601 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81c298f2-70de-393e-8266-e204fb8bcf74 | -2.0226 | -52.107201 | 2026-08-30 00:55:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a18a2b0-7a34-3517-b6a5-2814e7292914 | -7.4442 | -59.929298 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e99339d4-100d-37bf-9dac-f5bcbd92b341 | -13.8354 | -54.098999 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6aad7fd1-b395-30bc-9151-92b50f6d621b | -5.7609 | -51.678299 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69631309-cc89-3e9d-ab32-45f1e4454838 | -6.7764 | -55.6689 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f62ba6c7-f8b3-337f-8cc4-5750d490ee42 | -10.364 | -49.985699 | 2026-08-30 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1e6cc14-dca7-38af-ba70-b50bc69c064a | -4.0778 | -45.931198 | 2026-08-30 00:55:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa652870-af09-3dd6-a38b-d7a83215b791 | -5.6244 | -49.362202 | 2026-08-30 00:55:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74dfddb5-1bf1-3228-80d1-f8744d307b96 | -10.764 | -50.688499 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c5cf80e-5788-3ae1-b2aa-779574359e47 | -15.6463 | -56.4049 | 2026-08-30 00:55:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c6ba0777-f816-3e1f-94e5-2ab6735076e0 | -18.6598 | -46.8456 | 2026-08-30 00:55:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bb583fee-9588-375c-954b-1af9ec25b82b | -3.6292 | -60.535599 | 2026-08-30 00:55:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d419c89f-a76a-30c8-bf3d-0de844db4512 | -9.1298 | -50.583199 | 2026-08-30 00:55:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feeead8d-78db-3a65-a9f8-25125f40568b | -8.6032 | -54.773998 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a81c33f-7fd9-3b9f-9dc6-2563674b6d06 | -13.8505 | -54.121601 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 659f429d-c659-34d5-9d02-28bc606ff0d4 | -5.4779 | -57.133301 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14fc5e54-64cb-3ff0-89c7-fc97bd06c1a8 | -11.8299 | -51.108799 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efeade5a-8be8-3ca0-8016-b406355514cb | -6.6401 | -53.1786 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9571cf5-1583-326d-8b62-7cf4c7fde61c | -10.7657 | -50.695702 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08ad2069-46ae-3e1d-a80a-c82c5dec97cb | -23.159 | -48.663502 | 2026-08-30 00:55:00 | METOP-C | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 10f2beab-40c0-3918-9f14-3bd76a36a7bc | -11.2407 | -54.010201 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eaac1dda-6124-382d-9428-623d20656250 | -11.3428 | -45.132702 | 2026-08-30 00:55:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73a75523-b105-3284-9d57-79c497db8b51 | -10.7338 | -54.041599 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f556e563-db24-34d9-b73a-e964c5a795f7 | -14.4077 | -52.558899 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e6ee1f89-b4ba-39ab-aa33-6ab9f1fa212f | -7.292 | -60.604099 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32072100-12dd-3dd1-9d4b-8e051793992c | -10.7649 | -54.042801 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d41a3516-a231-3b2b-8b02-f5540fe52f30 | -11.4327 | -61.466801 | 2026-08-30 00:55:00 | METOP-C | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 852ec05b-4b10-3f2b-b6cc-3c036a620f9b | -14.9182 | -52.638802 | 2026-08-30 00:55:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a260340-e24e-3f8f-b981-36553b184936 | -12.555 | -55.747398 | 2026-08-30 00:55:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87bbaab6-9907-3ba4-8718-5c4eb5356b61 | -11.6327 | -54.587299 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 578d028d-9714-3627-ba4c-c035109b92d5 | -10.1372 | -45.685398 | 2026-08-30 00:55:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d124b7a1-79ce-3b4e-a439-2a8f7399d2f1 | -7.52 | -55.313999 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2a8fa07-6398-3541-928c-50dceaa1cdd8 | -9.724 | -54.825199 | 2026-08-30 00:55:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8dcd0570-cab7-3172-9105-06da79a546d8 | -11.0276 | -49.687199 | 2026-08-30 00:55:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a13a669e-c30e-33b2-ad42-861203dc4660 | -18.8242 | -47.4519 | 2026-08-30 00:55:00 | METOP-C | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1dcd7ea-3d98-3e37-80d0-19533016d2ff | -13.847 | -54.105099 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5910991-e9e4-3051-946b-11f9e85109b0 | -7.5611 | -61.304901 | 2026-08-30 00:55:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae55ebeb-aa31-3166-8719-a1ab60fc9bba | -11.1799 | -55.1049 | 2026-08-30 00:55:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d54e79d-27d3-3e0d-ab4c-55eea2b69d2a | -14.7732 | -48.739899 | 2026-08-30 00:55:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c09a3c51-a276-3f68-9f9f-23276fe6c8ac | -5.4898 | -57.140499 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63d73678-7291-3e25-8775-7c2659e39e96 | -8.5017 | -55.2934 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 170193c5-5056-3284-9115-08d34aa652a4 | -5.5043 | -44.0299 | 2026-08-30 00:55:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2bece03-3f6d-3525-804d-06dffcc90ffe | -5.8726 | -57.760601 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f3cd040-b171-3f55-8843-855f89264abf | -6.6934 | -60.1329 | 2026-08-30 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdacc79b-b041-3675-92ba-af77c4a1bafa | -11.0305 | -57.251801 | 2026-08-30 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 636e3c8d-3346-3ccb-afed-8b15873eb8aa | -9.9379 | -60.497898 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4dd78467-1d2b-3c3f-82f1-4b38874a7ce0 | -6.6763 | -52.8391 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a2f7202-f998-3bc9-bea3-8804a81ac1de | -5.8847 | -57.7686 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26aceca7-054c-3791-a67a-a213af64c273 | -6.9512 | -55.7159 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9af636c5-24f4-331c-9457-d76cc19ae7ee | -7.5084 | -55.3083 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d738fe6e-47d2-39f7-8b0f-d4095bd6f665 | -1.3859 | -49.3032 | 2026-08-30 00:55:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24a6e0a3-a7d6-3a89-b265-4aad6f301911 | -9.6155 | -55.128399 | 2026-08-30 00:55:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4cd9b2e-090c-3e4d-90ff-11e72c1f31e7 | -8.6164 | -54.7873 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 236f6d6e-d6d8-3dfe-a26f-2ef069389463 | -11.9109 | -55.894199 | 2026-08-30 00:55:00 | METOP-C | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a4f62d9-76a6-3e48-9e74-34329d0b1fed | -9.4061 | -51.6506 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49b921af-5151-34e1-be8e-651ab6294b00 | -6.6902 | -60.117802 | 2026-08-30 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8035d7d-763c-39ff-aa0d-dff775ae7a8f | -13.8487 | -54.1134 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2703fffe-8a9d-3384-ace7-8b52a3311ee2 | -9.8781 | -60.252998 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be3f02c1-4813-36f5-b0c8-fff75946309f | -11.7992 | -51.0644 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36b95406-59be-35a2-8c2d-a37895c4a800 | -7.0089 | -59.654598 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 372bba43-6773-31bd-96e1-da3d5fc6f061 | -16.344999 | -50.9781 | 2026-08-30 00:55:00 | METOP-C | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c02ec207-06d9-3aff-8a1e-591d117d17c2 | -6.6303 | -53.180801 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e6ecc9-985b-3c69-bec0-dadf2cf2a0e5 | -16.3466 | -50.985298 | 2026-08-30 00:55:00 | METOP-C | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f24be094-207e-3ab8-8582-6197538a4d88 | -5.89 | -57.746101 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 813279e8-b126-3385-b415-7d7607165bed | -20.011499 | -47.8871 | 2026-08-30 00:55:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5f2cf3-aeea-3981-9c9c-d0563187f716 | -10.764 | -50.643501 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22fe7841-2bd6-31db-89d4-a650bea2aa9d | -6.78 | -55.685101 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2801c385-4584-3a2d-a33e-38236a23e94e | -1.3882 | -49.313202 | 2026-08-30 00:55:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35221148-dee5-3f37-8626-1993e456e44e | -10.7584 | -54.060101 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad9b038c-b6bc-3b0f-8378-a5f22508d1aa | -6.1175 | -53.5555 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 525b5894-08be-306e-9050-7cfb28efb20e | -9.9282 | -60.499802 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4ae11db-c9e6-37b6-80a0-10ec2ac27975 | -5.9669 | -57.676399 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d972f12-d962-3964-b307-e9a566b33e89 | -7.2301 | -60.599499 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
