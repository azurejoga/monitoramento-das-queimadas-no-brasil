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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9af0dbfb-41d4-364a-954c-82f9d9ab86b1 | -12.9032 | -45.8382 | 2026-08-31 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| fae0d98e-7e8d-3fdf-b113-843eaecdb64f | -11.2503 | -54.0146 | 2026-08-31 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 52b947a4-ff8e-3626-815e-68cdf529bb54 | -18.2904 | -52.6818 | 2026-08-31 13:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 3b6a86ba-2c90-3fed-8594-62657d284222 | -10.3394 | -49.9547 | 2026-08-31 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0deb2c7a-b97d-3812-aec7-946a9520dbe3 | -11.9378 | -45.0656 | 2026-08-31 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| d5aa2cf5-0c9c-3c38-91db-6008ce2f06a3 | -11.5475 | -45.4906 | 2026-08-31 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 219.8 |
| 89db1f88-c8a5-3c72-ab16-4af59e7b0276 | -7.9605 | -44.3212 | 2026-08-31 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ea644ff0-dada-3c3b-be40-a5473aba952f | -15.6786 | -45.9332 | 2026-08-31 13:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 89.4 |
| cf95b259-4910-3ac3-965f-c32b94b60c85 | -5.2547 | -55.9105 | 2026-08-31 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| ab460cc2-553e-3345-b08e-7e6d2cd6c5fe | -5.5647 | -60.2312 | 2026-08-31 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 675c0ee8-07f5-3211-a7c4-a922299798b6 | -7.9236 | -44.2558 | 2026-08-31 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6a043fa8-0df0-3998-89b4-819f1799fdb3 | -6.6036 | -58.5972 | 2026-08-31 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 580.8 |
| edddbeec-b7b8-351f-9240-467977ca708a | -15.4594 | -53.9653 | 2026-08-31 13:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 766630a4-97ec-3fa7-9ac9-76329fc07c9a | -14.4201 | -52.5201 | 2026-08-31 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c5222a45-ac57-3991-83ba-644ef9d057ad | -7.3118 | -60.5897 | 2026-08-31 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 79f4f23d-4edc-39fc-8198-a566f7c9f3c0 | -18.2899 | -52.7035 | 2026-08-31 13:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 65d0e349-6d2b-31bf-a47e-7957beb7c567 | -14.2792 | -52.8758 | 2026-08-31 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| bab753e0-05b2-3523-b546-a22075fb283f | -11.3236 | -45.1778 | 2026-08-31 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 13ba8542-8819-3d18-b168-8851866d3820 | -14.4394 | -52.5176 | 2026-08-31 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2e3c49b5-e7d4-342c-a078-42e0181028a6 | -9.4342 | -45.6704 | 2026-08-31 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 423.2 |
| 81248cec-f8f5-336f-a40e-ef70c708beac | -10.8209 | -50.6945 | 2026-08-31 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b4ff58a5-aa03-3b90-b7da-0dc58019a3d4 | -11.2482 | -45.1194 | 2026-08-31 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6034fc68-64f7-3a92-94fb-b28955db09f6 | -15.4788 | -53.9628 | 2026-08-31 13:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 266ad49e-f5f1-3c29-958a-f86ac4ffa974 | -11.9186 | -45.0685 | 2026-08-31 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| a724c672-4de2-3389-83a1-4927c8b2b6f3 | -9.4535 | -45.6455 | 2026-08-31 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 452cfc7d-103f-318d-9155-183f348d0df7 | -11.3615 | -45.1955 | 2026-08-31 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| f81c23a3-3765-35ac-a41c-8c8887292131 | -11.2485 | -45.0963 | 2026-08-31 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 044f00eb-954a-3d23-bd63-97cbb791bd91 | -10.8541 | -48.3587 | 2026-08-31 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 7a6acc27-49a5-381f-87b7-dfcb85aab495 | -6.6035 | -58.6166 | 2026-08-31 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 109f0402-21d0-3b20-87fd-e351e3a41100 | -6.9367 | -55.636 | 2026-08-31 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c353e46a-b04c-38cd-9114-5cf72eb1d80b | -14.4004 | -52.5438 | 2026-08-31 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6eccbb20-9d97-399d-bf5a-e714f5a102db | -11.5283 | -45.4933 | 2026-08-31 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 052bd050-9151-3b1c-9587-51a998c0bc54 | -18.27 | -52.7068 | 2026-08-31 13:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 22079d45-7575-3d88-b161-836cec60f4be | -7.7938 | -44.084 | 2026-08-31 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 23c1bac2-f692-3639-a1b4-cd0220bbc9b4 | -3.6215 | -60.566 | 2026-08-31 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8b9da38d-dfe6-37cc-84fe-fcb82ba36301 | -8.8175 | -62.4898 | 2026-08-31 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 05049da5-762a-3c54-8e0b-41f968e22d7d | -7.775 | -44.0859 | 2026-08-31 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| d570515d-0c85-3d88-a9e6-cd682c60180f | -11.5279 | -45.5162 | 2026-08-31 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 8dcf684c-45e1-3faf-b069-e20d2c61a751 | -9.4345 | -45.6477 | 2026-08-31 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 278.8 |
| 3adea6c2-dba2-325b-8ecc-2486babb3acf | -11.4828 | -58.5159 | 2026-08-31 13:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 285.9 |
| cfdf9e4e-ad64-3f58-a859-6ce6ca2e5f8f | -8.7989 | -62.5095 | 2026-08-31 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 4efbd476-7544-3cd7-bfc9-10196b653b49 | -6.1295 | -57.6637 | 2026-08-31 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 2c62e706-92dc-3103-8789-f0a60a63f96c | -11.2294 | -45.099 | 2026-08-31 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 1b317db5-3890-3365-919c-8a4a22c19071 | -7.7752 | -44.0628 | 2026-08-31 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 4532f15e-09aa-36eb-898f-5b34bbf99309 | -8.1672 | -54.9246 | 2026-08-31 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 5c7b23ff-d91f-30e2-9255-76c8a683a149 | -9.4339 | -45.6931 | 2026-08-31 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5401ace5-3753-3ce6-87da-b39eaccaeab3 | -7.9239 | -44.2327 | 2026-08-31 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 0675cba0-dd3a-3967-8a4a-ee22e28fdc36 | -5.5831 | -60.2307 | 2026-08-31 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 30b268cf-90a1-31e6-b483-750a86c5eff2 | -5.3014 | -43.6722 | 2026-08-31 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| f33d49c4-8ed9-3070-a665-4a7f6044143a | -8.7439 | -46.4661 | 2026-08-31 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b8d3e334-4000-3685-ae30-259d376782db | -9.5778 | -47.6003 | 2026-08-31 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 842ce65e-c16f-352f-b308-ea2266ad68fa | -18.2695 | -52.7284 | 2026-08-31 13:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| a866f4b5-f2b0-36f8-ac74-fc966dcb7828 | -14.4007 | -52.5226 | 2026-08-31 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 01aee7ea-2ab8-3bc8-b208-10c83bcf1e20 | -7.9797 | -44.2962 | 2026-08-31 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 179.7 |
| c2105524-7385-3cff-9524-be4c59000296 | -13.967 | -54.395 | 2026-08-31 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9d8cdeaf-c2ea-309e-8ba2-bb41366243c5 | -18.2704 | -52.6851 | 2026-08-31 13:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 7517d34e-2440-3593-94ac-55b0e0adcc8d | -6.1109 | -57.684 | 2026-08-31 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 9a9bc3a2-b5e8-3d09-b852-6b5a03f2e41d | -7.9425 | -44.2538 | 2026-08-31 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| db68e641-ac3c-351d-95a8-24d489ff9fc4 | -8.7442 | -46.4437 | 2026-08-31 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| cadb87dd-4f1f-3476-9227-d6b4f4607c9e | -11.9382 | -45.0424 | 2026-08-31 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| fb914831-484d-310f-b688-a444bb156de4 | -7.0457 | -45.4124 | 2026-08-31 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 3a28f7c4-e03a-3763-9aa2-976a28653f09 | -7.2934 | -60.5713 | 2026-08-31 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 412655f1-92ae-301b-8f9a-de5f7f44ebb7 | -9.6676 | -47.9429 | 2026-08-31 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| aff8efcb-1edf-3e46-8ff6-4b5520f61492 | -6.6221 | -58.5771 | 2026-08-31 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ffa4715f-7227-3756-a44a-a4c2593f2ca2 | -14.5868 | -54.1153 | 2026-08-31 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5b283568-7d90-3538-a7dc-1e84f6de3bf8 | -10.7596 | -54.0384 | 2026-08-31 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 3b5c10b1-7697-352f-aa89-51913c1583a7 | -11.3806 | -45.1928 | 2026-08-31 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| d7ff9e84-52bd-37d6-8123-56bfb4f5c29b | -8.799 | -62.4905 | 2026-08-31 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| ebbfbed4-fce8-3871-afef-f6d52d70af6a | -5.9451 | -57.6906 | 2026-08-31 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| add28f28-f2f3-3bda-8d8a-f008d2fc9190 | -11.1824 | -50.5706 | 2026-08-31 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 509cdb48-506e-3ee3-baf5-391980bacfe8 | -11.9378 | -45.0656 | 2026-08-31 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 240be2be-fac7-3cb5-81c7-985ae9b507c4 | -5.2548 | -55.8907 | 2026-08-31 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d5626d05-2170-314f-9036-aafa61154953 | -5.5831 | -60.2307 | 2026-08-31 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 9600b18b-0036-343d-bda3-3e358ce75ef2 | -11.2503 | -54.0146 | 2026-08-31 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| f02505c7-372a-3388-bf88-268ebdf3edc1 | -10.7409 | -54.0196 | 2026-08-31 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 93513ab9-4f1f-3ec7-a82d-ec7a36758e81 | -9.4339 | -45.6931 | 2026-08-31 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 26c95292-ea29-3501-a2ba-697fd0ec117d | -8.1672 | -54.9246 | 2026-08-31 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 4d075203-ee4a-3b45-81d0-7e13c72a1fa8 | -10.3205 | -49.9567 | 2026-08-31 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 2062d6ef-2309-3e47-a010-9fb42bd3998a | -15.6786 | -45.9332 | 2026-08-31 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 219.9 |
| b73e9592-b13b-330a-b9e5-8417bf323f3f | -11.5283 | -45.4933 | 2026-08-31 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 604.0 |
| 109de95f-352f-3024-b1cb-7278d0f5f1e0 | -14.4004 | -52.5438 | 2026-08-31 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 91d15204-210c-3554-b00a-2d4c485989d8 | -10.3394 | -49.9547 | 2026-08-31 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 3705c18b-2661-3efa-af34-28457df45b3b | -13.967 | -54.395 | 2026-08-31 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b031af31-dc05-3013-b346-ccf67eb15af9 | -8.8174 | -62.5087 | 2026-08-31 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 01abe972-7f07-3b72-90cf-d4ac91a57ecf | -11.3611 | -45.2185 | 2026-08-31 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 55020536-fbff-3b8b-9448-b12f8e2345c7 | -8.7989 | -62.5095 | 2026-08-31 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 362acb26-a5fb-368f-8e15-2e2294af03e2 | -7.9907 | -46.5177 | 2026-08-31 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a772f530-2757-32e3-9b91-5d6ad33e074e | -11.3236 | -45.1778 | 2026-08-31 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 13797f1b-3d59-3976-ac00-11d367a3d2bd | -9.5967 | -47.5983 | 2026-08-31 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 63063229-346f-372a-90b0-bf227bff0e62 | -5.3014 | -43.6722 | 2026-08-31 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b20469f8-1b18-398a-bb7f-2f624194c17b | -8.1671 | -54.9447 | 2026-08-31 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 00cc7df2-dda0-39c4-bb00-5f3fe535d5e6 | -9.5778 | -47.6003 | 2026-08-31 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 84dcfc69-80b1-3928-a3f1-47fcac328c7e | -10.7407 | -54.0401 | 2026-08-31 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 199.7 |
| 84521731-ba93-3b52-84ce-be86b505f6c0 | -7.2934 | -60.5713 | 2026-08-31 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 97ac8509-5866-3025-aa8a-d95bd2c3d34b | -7.5845 | -61.3423 | 2026-08-31 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 435a35e6-c95d-36da-b0bc-dcbe8bf3c1c0 | -9.4535 | -45.6455 | 2026-08-31 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| afea961b-048f-34fc-9fef-ea06b10d585e | -5.5941 | -42.338 | 2026-08-31 13:50:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 2d2fb8bd-b907-3e96-b879-236897520343 | -11.5017 | -58.5145 | 2026-08-31 13:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7b472668-95f1-3c77-8c92-d52e6d6fbe99 | -6.6036 | -58.5972 | 2026-08-31 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 651.3 |
| 77e7a74b-673f-3f42-8f23-eead7fe301d7 | -14.2599 | -52.8782 | 2026-08-31 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |


[Clique aqui para ver as próximas entradas](README89.md)
