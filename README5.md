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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bbe3c8a-2996-3810-84ff-58cc2ccd11ec | -14.4147 | -52.19753 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa056419-3af0-3a16-815f-f0ab9f224e00 | -10.94978 | -50.59706 | 2026-09-06 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 96b6578b-9d18-3ab7-af06-dc796556c46d | -5.34936 | -56.01866 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a12d7a58-f97c-3291-a8f7-d758ee322433 | -6.1377 | -57.69041 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 96ee3c09-d22d-3534-9c43-b713adc0ff3f | -7.25615 | -61.10702 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bcd138c7-eefd-3e4b-876b-9e970a1ce3d6 | -5.30124 | -55.86372 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d6e70d8f-9462-34cb-9150-225ff5db2bba | -10.75154 | -60.7683 | 2026-09-06 00:24:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| e43dfc27-c27a-3820-8e08-71cf683f112b | -10.68833 | -45.95687 | 2026-09-06 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 45aa544e-1ee9-3903-bf76-0f01afa047c9 | -11.2357 | -54.10656 | 2026-09-06 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 793fd6b1-6352-39b0-83be-18dabfeb04da | -9.69992 | -57.42014 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 467e16e0-b0cb-31e9-9bbd-5878d7f48d68 | -10.7445 | -60.70959 | 2026-09-06 00:24:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 089048ce-5098-3e7d-bf82-aca56777fb5b | -13.82082 | -51.65742 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ca951906-b111-366e-8fc4-9287be73025c | -6.87854 | -55.61119 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 509a477d-a8e3-38f0-b89f-cd730f3ee7e3 | -13.81009 | -51.64884 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47b40dfa-b095-3331-ac1f-03163d4a9c0b | -5.13483 | -56.27478 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ea37a534-4398-31a3-8513-0a91ef637a17 | -14.41607 | -52.20704 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ff9fe9a8-3a79-3109-b016-1956dac28737 | -6.12699 | -57.7541 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5502877d-e733-3d50-91b9-bbb80f8365d1 | -5.35177 | -56.03633 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 261021a7-b5cd-3c64-adf8-2f1968cba669 | -5.56812 | -49.0214 | 2026-09-06 00:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 80f3a8da-156b-3a96-bd07-171921374147 | -7.34113 | -55.21276 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 162c290e-5dfc-34d5-8c63-80dd314f1d28 | -7.44376 | -49.72117 | 2026-09-06 00:24:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 199f463d-ddb9-3605-8f72-26059c1ddadb | -13.77299 | -51.65466 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 9522945d-c146-3aae-b7c8-1346cc34ec7e | -6.66471 | -59.94447 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 2c9e9064-cbf7-33ef-8880-7fd588540fe0 | -13.77151 | -51.64458 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3e19e0ef-4891-3443-b781-bce15c941fc6 | -5.30244 | -55.87252 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae242d90-c321-3572-bb4b-342c32f15caf | -4.45408 | -46.15797 | 2026-09-06 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| bf4ef461-2f9d-33e9-b717-a93bfaf46976 | -6.87975 | -55.62003 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 87f12d4c-28a1-3ed7-9523-ea45f516bedc | -13.74965 | -51.68928 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| af27ca8b-709b-3f28-bc6d-74a945294af2 | -6.07077 | -52.24797 | 2026-09-06 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ecf38794-d343-3d1c-81e4-8a9597745411 | -10.47842 | -46.07711 | 2026-09-06 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fc1ad443-64b3-3b36-b677-6c1b93989080 | -5.17012 | -56.0559 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0fc29faa-e62c-3ba3-9acc-ed3b73f4276f | -13.8252 | -51.6405 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| bdeae0be-ea74-3ec6-8b67-a609558c9758 | -6.65167 | -59.93149 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8553d766-db34-36c2-9608-423c170a3072 | -6.58736 | -58.61077 | 2026-09-06 00:24:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 83671147-2764-31aa-a26c-63e2b61d54ec | -6.0934 | -55.59038 | 2026-09-06 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bca90e07-8c1a-3188-927e-0cc9d5dfaf63 | -5.35817 | -56.01744 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 04a155ff-f003-34cd-ac78-77fbeb057b5f | -8.98311 | -44.41842 | 2026-09-06 00:24:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| af632f70-4afd-38e5-8ecb-a9711d0dfe81 | -6.09314 | -47.32874 | 2026-09-06 00:24:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 058aa8e3-678e-38ac-a29e-0aa90e887f08 | -4.4487 | -46.12167 | 2026-09-06 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 39.3 |
| c16ec67a-ed9e-3d8e-8acc-541946d9ed6e | -4.1093 | -49.09136 | 2026-09-06 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 9c930624-e933-38cb-80d5-ffdfb8421972 | -13.79007 | -51.64166 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 332c05b7-f291-3b5e-9437-0340647df8d0 | -13.74816 | -51.67922 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 76b5993a-4321-3593-9089-88b031fa86ce | -7.11568 | -55.12807 | 2026-09-06 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 53db39f9-a67f-3089-8131-468d5000152c | -6.11591 | -55.8208 | 2026-09-06 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7be82983-5426-3294-a58e-3f88017e0a2d | -5.84588 | -52.04258 | 2026-09-06 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e4fddd9a-9aeb-39e3-9329-9d1c0091ef27 | -11.29155 | -45.1123 | 2026-09-06 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6e6a7c09-94a3-3752-beae-cabc70989456 | -7.34234 | -55.22157 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 039744f3-3119-3ff8-ade8-5567202566d5 | -6.58586 | -58.59918 | 2026-09-06 00:24:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3ae2bc50-9d48-3e37-bcd5-613613ff4ac4 | -6.65395 | -59.94022 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| de005871-ca53-3c16-80f7-2ae3be15e754 | -6.08785 | -47.30854 | 2026-09-06 00:24:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 9199a8a3-d1f9-3091-a8a5-16e579de9d19 | -6.00443 | -57.78268 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ae34a33b-b9ba-3bc8-bb30-2ceea65b2b72 | -6.059 | -57.79058 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 3db69457-9d5b-355a-927b-b3522c703dab | -4.11965 | -49.08317 | 2026-09-06 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e2bbb107-8bb1-3bcc-b749-d3200ec33e63 | -6.51376 | -58.29091 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 65100521-8fea-3fd3-8285-91ba87e582a9 | -7.26823 | -55.1571 | 2026-09-06 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c5bc366-8763-3ac0-ae3c-b9c577b3ed1c | -5.14802 | -55.96008 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f5c85df3-9752-36d1-ab02-ea935296be51 | -9.546 | -60.83845 | 2026-09-06 00:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d9e22d6a-7479-35e6-8d8d-7e7a048067b1 | -7.2758 | -55.14705 | 2026-09-06 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b2bc62ea-359a-3b90-bf4f-2d550589aac8 | -6.07033 | -52.25441 | 2026-09-06 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7c828666-c8a3-38ab-a9e6-8c36236c721f | -5.15683 | -55.95885 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9e0575c7-68e1-3280-9d13-680073a746cd | -6.11079 | -57.70438 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6e99a50e-bf31-3e9b-8394-9fbd0f27000d | -10.52065 | -57.44514 | 2026-09-06 00:24:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f95c6220-1194-36a9-a880-748c2a57d96a | -2.17053 | -48.80168 | 2026-09-06 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2a790367-3268-32d9-a7e2-5fc0514868c8 | -3.76893 | -61.76027 | 2026-09-06 00:26:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 44c518bf-4c47-3ee6-b317-218d0224ba70 | -2.91531 | -61.00021 | 2026-09-06 00:26:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 554abf2a-1086-33b2-847b-4dcae01c8647 | -3.83579 | -60.76438 | 2026-09-06 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6343c28c-a77c-392b-a319-7b983ecccf13 | -2.91426 | -48.88057 | 2026-09-06 00:26:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 435cf3fa-a799-32b5-959c-a0d19cb2a70b | -2.45602 | -57.9173 | 2026-09-06 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| dc3fd796-5f5c-31e6-85c1-18f2a4628d48 | -3.23267 | -58.89868 | 2026-09-06 00:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e767200a-b87e-3221-8b5a-61d1bb21414d | -5.25945 | -59.99025 | 2026-09-06 00:26:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2c1d06d2-2520-31c7-8780-1a0b0a1440fd | -3.17407 | -61.13714 | 2026-09-06 00:26:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f3bf0966-a712-3e81-9d4a-baffa13e0b70 | -2.86347 | -50.46886 | 2026-09-06 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 06036736-c069-321f-80ae-249b3a67b87b | -3.41657 | -54.7751 | 2026-09-06 00:26:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5dd80815-c8cf-3011-b191-f258b1cd38ca | -3.79035 | -55.884 | 2026-09-06 00:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| fe431939-489e-3e1e-a1e2-8d5b20688437 | -3.7888 | -58.85378 | 2026-09-06 00:26:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8fead281-ebd1-33e8-bfa2-7eff1cb0fc9e | -1.75011 | -55.66901 | 2026-09-06 00:26:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 43f7b32f-435c-3cc7-8d3e-4453e72d4372 | -1.75132 | -55.67781 | 2026-09-06 00:26:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 70027530-6ceb-3416-8585-08cba783bef2 | -3.42125 | -58.31654 | 2026-09-06 00:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8574649f-fe9c-3313-84e2-bad71d8fc4bc | -1.39753 | -55.18062 | 2026-09-06 00:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e2272fff-8c27-3140-a21f-b90b88ee0ff3 | -4.29248 | -59.95779 | 2026-09-06 00:26:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 201a287c-68fb-3753-bf07-b11c332c62a9 | -1.49648 | -54.8267 | 2026-09-06 00:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c7a29b95-5f19-3c20-bc4d-27558f7f8b0a | -2.86883 | -50.46153 | 2026-09-06 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 28837ab5-b2fc-37e5-b184-72548f416080 | -4.4658 | -55.08963 | 2026-09-06 00:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a73c3563-128e-308f-bab4-ae8c6d93b596 | -4.46703 | -55.09847 | 2026-09-06 00:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2f6466b5-01d7-306c-8761-3ab38646178e | -3.54875 | -48.16824 | 2026-09-06 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d3b9fed3-007d-3b35-ac4a-66b43baaf26f | -3.83715 | -60.76977 | 2026-09-06 00:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c2d32dc2-fe7d-3558-8d2e-d3e4ae85e4e5 | -1.39629 | -55.17152 | 2026-09-06 00:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| f7cbab75-5378-3224-a103-410c6eee9cb3 | -1.38734 | -55.17278 | 2026-09-06 00:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b5821e23-4589-3385-985d-cb363749839f | -4.67832 | -55.63626 | 2026-09-06 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9bb61278-1756-31fa-8129-ad8ae5cfa858 | -3.8627 | -51.0383 | 2026-09-06 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| cb5e6dfe-0d40-39b1-9ea2-229916156d93 | -1.48743 | -54.82799 | 2026-09-06 00:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b2d7f118-36f4-3de4-8cfe-ce17cdec32e1 | -2.45472 | -57.90774 | 2026-09-06 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 56748041-de6a-3847-8cb7-fe635e4716f4 | -3.55255 | -48.19329 | 2026-09-06 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 7ebd9da1-cd0a-387b-8729-b27512a691e7 | -3.22018 | -53.16746 | 2026-09-06 00:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 437bd6e3-2045-3faf-8d5d-2ddf19f3958f | -3.62412 | -54.61272 | 2026-09-06 00:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2f333a1f-56ba-37c7-936b-ca30e14fb899 | -2.76462 | -48.57358 | 2026-09-06 00:26:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2a2983f4-6645-3dcf-85f2-dd6f46662989 | -3.78915 | -55.87525 | 2026-09-06 00:26:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 99fa50db-a628-35ea-9195-54915a3fa39e | -4.2946 | -55.72322 | 2026-09-06 00:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0110541e-25f9-3318-b446-8eafe3a77b4f | -3.22169 | -53.17828 | 2026-09-06 00:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4453c015-3978-3006-8577-47da4f528e08 | -3.38358 | -59.41721 | 2026-09-06 00:26:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |


[Clique aqui para ver as próximas entradas](README6.md)
