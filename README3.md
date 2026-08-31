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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f0f4af8-8b60-3c2f-90c0-5fce58a70d36 | -3.6089 | -60.521099 | 2026-08-31 00:11:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33281dd4-fd2b-3e83-a3f2-795743569713 | -9.431 | -45.685501 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67bfa2b7-bddf-3893-a036-d2a1e534ac27 | -7.9761 | -44.2953 | 2026-08-31 00:11:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 077b8dc2-d74d-3862-886a-261bcee5df7e | -9.6598 | -50.851601 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8e44663-1d5e-3306-84af-1e9c28eb21c4 | -9.6662 | -50.8806 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 834eb949-24a9-3d95-a7a1-d5839711e151 | -5.2561 | -55.9142 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac6c0419-9b0c-320d-a271-49e42efa2253 | -9.415 | -45.661098 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a3b8cbd7-f689-3aa2-b4fa-83e6f798d176 | -14.2198 | -52.837002 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 947e62c5-1915-35f7-93c4-b365cab008a4 | -12.104 | -45.028801 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d01f6f2c-709e-3b4b-8c2f-df33ac590cfe | -18.3002 | -52.675999 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 353d93ca-1eb7-34e7-8d57-dac3683cfa0f | -5.2462 | -55.868698 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02758000-923d-380d-ace4-7e1a246cb2ed | -14.6426 | -53.571301 | 2026-08-31 00:11:00 | METOP-B | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 877a8439-da8a-3a10-8931-4cc9091a6033 | -10.744 | -54.0466 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9f5f9e-0d2c-31c0-909f-25d54fe5e3ce | -19.1441 | -57.354198 | 2026-08-31 00:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c41321ff-5291-362a-a95e-f1a8adc16468 | -19.1576 | -57.375801 | 2026-08-31 00:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7cfbcfda-c11a-3732-bd4c-afd6815bb5e5 | -11.2129 | -45.103199 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13a1daaf-f203-3acd-9112-e8650ce39e5e | -6.2791 | -53.325199 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc8d3f8d-7303-398f-aa24-e07a9c8e658e | -3.6235 | -60.541401 | 2026-08-31 00:11:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9ba95f7-14e8-3387-b6ac-6a95adaf23d8 | -6.4828 | -49.896702 | 2026-08-31 00:11:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7420b1b7-cdc4-37d8-9a12-deba058d5770 | -7.1137 | -42.770599 | 2026-08-31 00:11:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3601c671-dd28-340a-a053-fe3b1bc0a04f | -11.9241 | -45.053902 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c615c550-8af9-39ba-ab71-517e9457b67a | -14.1887 | -52.885201 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 037e4631-f5fa-3252-b761-98d5fedfa4d4 | -7.3463 | -55.176998 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76335266-2000-3822-be94-285896e7c4de | -10.7462 | -54.056999 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1291c47d-ba1c-3992-937e-18d0bb4f1273 | -4.953 | -55.837502 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f17383-e773-38ec-b03d-8a291ba13e2e | -7.7767 | -44.065701 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a13dc309-d4ef-3e1c-91b3-f54c10053a64 | -10.7429 | -44.863701 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0384ca94-8e55-3c05-a126-5a355ed01016 | -8.0837 | -45.4841 | 2026-08-31 00:11:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0268958a-6797-3643-bc9f-289a194008d0 | -5.2487 | -55.8801 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0355901f-a8c7-3153-8c7f-b190032ae37b | -5.9594 | -57.662899 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2855147a-c3ac-3d80-851e-d0e5e2c4bde2 | -10.8393 | -45.356098 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b669191b-df00-3db5-a347-cd1f119f7b05 | -15.2296 | -56.359001 | 2026-08-31 00:11:00 | METOP-B | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f629c2d5-dd45-3301-8eaa-c022b9b4a7dc | -6.3859 | -45.497101 | 2026-08-31 00:11:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a7d940b-e591-3a71-9933-42ce80504954 | -9.198 | -51.5564 | 2026-08-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d357470-9515-39e4-a382-f9630f0aabc5 | -15.6189 | -56.393398 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef4dfea-885d-3bbf-801a-28b4a4f987d5 | -10.5508 | -46.191399 | 2026-08-31 00:11:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b11fd9e8-ac15-3327-b836-956f4ea82ed2 | -14.4125 | -52.530998 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a791cef5-6b9d-3181-b21b-c992df1b2c7d | -6.9299 | -55.618099 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 476c2e4b-2697-3acc-a6e9-28dc7c242363 | -5.3121 | -55.8428 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20ec36fd-fc27-3e33-a9db-9e4aa5975d1f | -4.0657 | -48.962799 | 2026-08-31 00:11:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a357cfd-7818-3c95-bda9-7f14736d6cf3 | -12.1061 | -45.037701 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9c09c88-a38f-3928-ab99-61eee63fc506 | -11.0872 | -51.5117 | 2026-08-31 00:11:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e6b48f0-eb38-3937-aa46-186ee1f4b53f | -14.1968 | -44.576302 | 2026-08-31 00:11:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3d339b-1888-34d1-9c58-9c7ebf38b151 | -15.6597 | -45.9226 | 2026-08-31 00:11:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 96b9ea6e-1a24-370e-b4c8-50d7ab1fce6a | -8.7429 | -46.446201 | 2026-08-31 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae1944c4-39a4-3d53-a075-9c830cc3553c | -9.4226 | -45.649899 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4979fd09-0ee8-3f10-a567-63ba952f290b | -6.6031 | -58.5919 | 2026-08-31 00:11:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2ecb2ee-d80e-31d3-994a-1d9632e8cfc7 | -12.7804 | -46.459099 | 2026-08-31 00:11:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a3bd408-378f-329a-893e-79bf5d630913 | -9.5781 | -47.602699 | 2026-08-31 00:11:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c08c839-b3c9-3de1-96c7-dd352ffe1162 | -10.7473 | -54.013199 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47e56cc6-169d-338a-b40b-57b85f5ad788 | -15.6337 | -50.085899 | 2026-08-31 00:11:00 | METOP-B | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6af5bd5b-1239-3a01-a1c3-a3dec04d472b | -10.7436 | -47.964901 | 2026-08-31 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f18529b8-bfda-37ef-8525-7b81edf11c07 | -10.7695 | -50.8508 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9dbbd48f-f9df-3424-a70d-363cd3723a7b | -11.3503 | -45.203602 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cecf7003-1a7a-390b-ac6a-ed9d123e9054 | -10.5981 | -52.2416 | 2026-08-31 00:11:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 632e5bfc-4dea-321e-9cd3-9809b0e301ec | -1.5952 | -54.392101 | 2026-08-31 00:11:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14b5583c-9ae3-3f10-bd65-fe225d0c6ef0 | -4.1378 | -60.671501 | 2026-08-31 00:11:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f102ddf-6fb0-3488-a4c8-d65688d6eee6 | -8.9384 | -50.194302 | 2026-08-31 00:11:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65270e86-f205-3eac-8e71-fdd1fce99d2c | -11.1587 | -45.048801 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3f6b3b4-7f16-323c-b661-3b3f26bf5ac4 | -11.4971 | -46.932999 | 2026-08-31 00:11:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f995268-fb90-36b0-834a-b3d6d654ebfb | -6.9323 | -55.629601 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c43d6ec-2f60-33ae-bc13-74c29d2be576 | -8.1294 | -45.503101 | 2026-08-31 00:11:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 08fc9d02-1982-38db-bb7b-8003bc678643 | -19.1285 | -57.380901 | 2026-08-31 00:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 56c468fa-8796-3b6d-88d1-4a445fc83922 | -11.0889 | -51.519501 | 2026-08-31 00:11:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f58a1d73-7760-3aa5-ac81-e2ef4ac1d32e | -13.9447 | -54.409698 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84486bda-1b1a-37c8-bd40-becdc9dcf484 | -10.8094 | -50.657501 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13f28788-dc39-3f8c-8371-bd1bc81f9214 | -3.6596 | -52.176998 | 2026-08-31 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 686596d3-6cf4-3a7a-9748-30b6c80e74d7 | -10.1527 | -45.7262 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2ade1fdc-7f5c-3bb4-a0bb-4edbe179c803 | -11.9143 | -45.056301 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff01db1f-4fb2-3ece-8096-3c9796bf54b3 | -8.089 | -45.462898 | 2026-08-31 00:11:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9c14bf9e-afa2-3b82-abc1-5a6ca639d8d9 | -12.7902 | -46.456799 | 2026-08-31 00:11:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5e9d6c9-2787-3807-97bd-25198df60208 | -11.7422 | -47.6418 | 2026-08-31 00:11:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0f137a4-7872-3017-bff8-b16e5279cce5 | -11.0791 | -51.521702 | 2026-08-31 00:11:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc31865b-a8c4-3899-8ad6-5fead3fde480 | -10.8242 | -50.631199 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb2334a5-14da-3f4d-afec-f9476daf9912 | -10.8126 | -50.6721 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b49f30ff-b13b-3208-a8c4-4f04c5078e42 | -9.4247 | -45.658798 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e41a15d7-08d4-3380-b954-5e96102935dc | -13.3617 | -46.922199 | 2026-08-31 00:11:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 38c42b18-41d7-308a-afa7-141cfb2bae54 | -10.7495 | -54.023701 | 2026-08-31 00:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26d958f2-dd84-3462-a70e-34639df4227c | -12.9332 | -45.917702 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6324b76-f71d-3401-9a82-918e6865240e | -7.6141 | -55.282902 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54578e70-8272-3330-8928-0d543b1233e2 | -6.2809 | -53.3335 | 2026-08-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 474eace6-1f82-3dda-adb5-b5ccdfda1a63 | -7.9236 | -44.2486 | 2026-08-31 00:11:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33ee9232-6310-3be0-bb1a-67aa31919ef5 | -12.8947 | -45.8419 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f6a3cb2-f002-3030-b4fe-375aa75bfc03 | -9.1498 | -59.529099 | 2026-08-31 00:11:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1a78e0-89d6-3672-9c39-208c63266861 | -5.9496 | -57.664902 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd727a67-e15c-3a9b-a39a-06eec8b37c19 | -14.4341 | -52.536499 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe11069-8959-39d8-8f3d-490714872876 | -15.6353 | -50.093601 | 2026-08-31 00:11:00 | METOP-B | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37f6d5aa-9f19-3727-8213-56d8ced2e0a9 | -15.1973 | -46.244499 | 2026-08-31 00:11:00 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d83e3850-e235-316d-a7a6-b84c887fcd84 | -10.7727 | -50.865601 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0ca45dd-ac46-34f1-9d64-2184fd1cb6d8 | -12.0943 | -45.0312 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 427b35cd-27f3-334c-aaee-e3119cc2b06d | -13.3731 | -46.927299 | 2026-08-31 00:11:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45f60d65-b944-384b-bfb7-f5c7b165d6ed | -14.1847 | -52.8652 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2ad34aaa-f088-31e0-ad01-63ec23f49177 | -8.7449 | -46.454498 | 2026-08-31 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 845dc242-b184-33f9-9866-7318e99c7966 | -6.2635 | -55.418598 | 2026-08-31 00:11:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d203059a-2579-3742-9108-68371cf345b7 | -6.9473 | -55.699402 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba5bdb7c-c7b8-3f3c-b7cb-884e2f45da69 | -14.1989 | -44.5853 | 2026-08-31 00:11:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79244955-4f8f-3c67-add4-9e4021587b0b | -7.5431 | -47.318501 | 2026-08-31 00:11:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 854e1ea9-84c0-3be6-8686-cd7135ae4f12 | -14.1769 | -52.877201 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc2d321a-5b3e-38a7-842a-ff53a556b183 | -3.541 | -49.463699 | 2026-08-31 00:11:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08900a50-a98b-3256-a1ad-46ec7c6c0d08 | -4.8577 | -55.823002 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
