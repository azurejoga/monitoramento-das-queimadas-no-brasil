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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5eafaebf-ad8c-363c-89d0-4c1d25b7a140 | -12.1044 | -45.00173 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3a385f33-0eb2-32ac-8c85-2079ecdcb870 | -8.42229 | -44.98317 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f2d56a9e-b40d-3e20-a542-f5441b0e8bd3 | -8.04706 | -61.73195 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 19743529-6020-3030-bfc5-6c48d16ce739 | -11.49154 | -50.34413 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c14fc81a-3276-37e7-88f0-1a920914983d | -13.47624 | -57.02894 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2d7cb55f-be64-3faf-993f-6603773c570f | -11.31993 | -45.19236 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 581777fe-cf82-3ecf-9d04-b2d6f0eeee22 | -10.49573 | -59.60308 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0a601084-80a4-3e60-ae74-f88e5ce19de5 | -9.47925 | -57.0121 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e694efb4-ab2f-30f5-8cc2-6251883efe27 | -10.85121 | -45.31872 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0fbb9c3d-65c3-3be7-9926-980e8ad791fe | -10.18156 | -42.22484 | 2026-08-31 16:50:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 5986289b-4e2c-3ee5-a1d7-6a54523085e8 | -8.9689 | -62.38749 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8e9ec396-50e7-34d1-b9c2-98409cf0331a | -10.12661 | -45.83418 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9036995b-2e94-3cdb-8187-d7be7ae67341 | -9.20708 | -59.41172 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4e57bd79-49ee-398c-8798-b6e6788a7a80 | -9.20025 | -60.24834 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 7c0876d8-6206-3bfa-8179-10fbb7b95753 | -7.49488 | -44.88925 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee588dae-194c-35f2-9d8c-0743f2c3a7e9 | -6.35523 | -44.8935 | 2026-08-31 16:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ee0e12c-a0f8-3a0e-be98-13a03563371d | -11.2496 | -45.13612 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 086d5b44-7cfb-385b-a2e5-3adbcc864178 | -11.24766 | -45.12402 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a51e315e-c917-33db-8c7d-b1cda9bbb7cf | -8.75894 | -46.47005 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4cf7e927-c41e-310f-958c-4ff1ae8b6e62 | -6.77126 | -52.89447 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9854248b-5136-3825-9624-4e5b0e183b6a | -9.30293 | -45.39649 | 2026-08-31 16:50:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0fc3d6a9-0db9-364b-8d22-21e7c834deae | -7.78683 | -44.06424 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a3129828-0ee1-3279-80a6-2bf916fd27ec | -9.97045 | -46.30565 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dcc428a0-a36a-32ab-8344-0b4ca25d9de7 | -13.36592 | -51.67805 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 47edbe78-44f4-3dd8-b83f-1ffc168f1465 | -8.93282 | -45.03065 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ff5cc92-2074-3190-80a1-abff53c5a253 | -9.60217 | -47.61345 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 100b120c-c326-32d9-8dfd-9de9ebcff4aa | -7.95593 | -52.45117 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9af94c34-81f3-3847-a384-01f952ce624c | -10.82702 | -50.63681 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 775b9fb4-8faa-3bcb-b4c0-57c055446f4e | -11.79354 | -47.67046 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| b697cdea-15c0-3415-a95e-515d311be224 | -8.42098 | -47.72494 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2108be25-50b9-3b0e-9b06-96f7f1bb9002 | -8.76471 | -45.38183 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 9d3df3e2-381e-3f86-b02c-193f79b4afab | -7.99645 | -44.28684 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b2a2051e-b90e-34dc-9690-470a9a501289 | -5.77493 | -44.13431 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ed25217-64d5-32be-86b6-d1a20ae88470 | -11.38145 | -45.1702 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 6e7df209-8ab5-39ae-9dca-61c09aee1eae | -13.27475 | -51.60247 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 6444eee0-72b4-32a0-912a-5f202c5fbb5f | -8.38388 | -44.993 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5a090d1e-335b-3d42-a741-badd7f93d9ab | -10.84254 | -45.30735 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7a337f0b-cee2-39c7-9dd1-fd8456263281 | -11.71419 | -47.61851 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac9c56b4-edcb-3a12-a698-aa76a877cf9f | -6.39118 | -45.50082 | 2026-08-31 16:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 19d34bf8-35f4-325d-88ab-97e8ccc1dc99 | -11.23524 | -51.25015 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| de6d4f96-a89b-3240-94a0-cf2a49328adb | -9.43871 | -45.65589 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 943b2f39-c86f-3700-bc83-b1b659123517 | -10.12475 | -50.3228 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| dc5b6bf6-f350-3e07-8707-7296fec7ff67 | -11.16161 | -45.04517 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6fb092d7-45a3-33da-acae-035e2e0bfac9 | -11.2325 | -45.1432 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 10897c69-79ef-3203-9e7b-ea676603098b | -9.58757 | -47.62689 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 81497193-edc2-3702-9aa2-d509f3bc9a19 | -11.24848 | -51.26549 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 06a2ad79-814a-3f7a-ba3d-791ac2ed3f27 | -9.44213 | -60.52543 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 70d02d1d-290a-3044-b8fd-6b793e2e67fd | -7.42115 | -44.26001 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 08772b52-bb47-3098-bc48-ea9311d62c8c | -11.93494 | -45.07566 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3be7cd69-6903-3450-b349-67d0e4e5fd01 | -11.5805 | -47.71945 | 2026-08-31 16:50:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 424bb917-63aa-32b4-8ea2-1ceefad64198 | -11.48094 | -58.51378 | 2026-08-31 16:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0f461eca-a331-3ec7-b6fe-8f47bd642bf2 | -6.62276 | -53.17592 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d5c857af-dff4-39f9-838b-2332f92e7d33 | -13.47159 | -57.03637 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| aa7c3e28-c52e-35bd-9fa4-0a6865345318 | -9.65608 | -46.06606 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 10c59d86-fbe1-305f-b72f-2ca871eca643 | -7.64773 | -46.73261 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 0ac28818-c6eb-3e2f-a21e-879b042f5f5e | -12.89999 | -45.83432 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| df9c72bb-85b1-3933-839a-c936538392b4 | -11.91834 | -44.84109 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2d09f05e-5e75-3d04-ac83-52de6970b394 | -11.84257 | -41.50614 | 2026-08-31 16:50:00 | NOAA-20 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b44a5c96-95c7-3671-b62c-246bf9bb2c54 | -8.08196 | -45.46617 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47d0da7b-6d86-3a09-b716-ff812688c59b | -11.85291 | -46.76525 | 2026-08-31 16:50:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 336d5c8a-c8b4-3821-9130-56da9d1ae0c4 | -9.13348 | -60.91796 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 420ff45f-1f4a-35a4-8d51-866212a53d47 | -6.81647 | -51.14934 | 2026-08-31 16:50:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b0a4d12e-25fb-3a4d-bb5a-86ad464cf145 | -11.91426 | -45.08254 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| ce4e2bb5-69a3-3525-898e-c5e233ceb67d | -7.99561 | -44.28181 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 7e76cd52-ad44-3a4d-a956-123fc7e6e69a | -10.15342 | -45.77771 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 4c20b32b-feac-3914-8510-e3e86a09b877 | -12.10221 | -45.01067 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 257.0 |
| e529bc73-0c71-3d44-ac87-816f7bd239d7 | -5.59279 | -42.32978 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c9a92aa6-ca2a-30b1-be16-ddf6b6f84c6c | -8.87167 | -46.02805 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| a86c794b-d19f-3b18-8995-55878ed93786 | -11.07251 | -51.5252 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 22421da7-f24c-3d74-8b3d-a00026de92a9 | -6.6745 | -52.86952 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1d932d1a-9281-3cd7-88a5-26b9ea024e4e | -7.5648 | -60.4856 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d34aeceb-66b8-32a8-b3db-87f111775e86 | -11.71689 | -47.63609 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6717d4a0-71a3-389b-a687-48ac9fcdeef1 | -11.51978 | -46.93142 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99d0b716-9cfd-3705-933c-a8a23343fa7b | -10.56436 | -50.36627 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 16baaddb-4ec1-3b51-bb69-e65617f1787a | -13.46113 | -57.04119 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 8e74c204-7324-30e0-8bbe-420c3de41ff7 | -11.21699 | -46.09795 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bd9af7ed-0c0c-379a-b863-827ac2886af9 | -11.23767 | -51.24115 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6e58762c-b576-332e-9444-242b19bca9f6 | -10.09703 | -50.2768 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b14ece65-1801-3acc-ba16-954ee5b7d318 | -7.28739 | -52.36832 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| eb77b6e6-ce55-3f18-ba80-e4f36969b1c3 | -7.42111 | -44.26206 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 35f939ff-64c1-3e49-935e-f81122f3213d | -9.20429 | -59.41053 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa87e906-5539-3aea-b87e-24ee90f275a5 | -11.25345 | -45.1146 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| e357493e-4f82-3267-a52f-87da2d66aba4 | -9.64729 | -46.05554 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1f924ccd-809b-3583-8de8-83350bc0c7eb | -7.228 | -42.76234 | 2026-08-31 16:50:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6b32ad44-4ea9-3e78-921a-b000b30efbdc | -11.61815 | -49.4162 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| be74d5b9-a5fe-32e0-96fb-290e039166cf | -9.67483 | -47.95103 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 744da673-b003-38a4-a981-256135c89363 | -10.57754 | -57.49834 | 2026-08-31 16:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cdffa425-6efa-3aaf-8485-9019f6950f72 | -7.04594 | -42.18753 | 2026-08-31 16:50:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 145893c7-03b8-396f-bee3-d3be4a942aa1 | -11.6827 | -54.54453 | 2026-08-31 16:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6c55109a-45dd-310f-9aa2-587769f8dd39 | -12.07399 | -47.20101 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| c2d5b1f0-3675-31ab-a6fb-3587d3b8b790 | -12.20384 | -52.86818 | 2026-08-31 16:50:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c8f29d75-39c2-31bb-b533-0e40da78c9e2 | -10.84803 | -45.31895 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 77264116-76b2-380a-b04f-05f7df1623fa | -10.50433 | -59.61745 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6b768427-dc60-31e0-8795-93d0cf7f6d98 | -8.13842 | -45.5859 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4002689e-80d7-348c-9dd9-8c25a974a125 | -11.04 | -47.12378 | 2026-08-31 16:50:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf505566-698d-36b0-a346-6cc601b0e858 | -10.56381 | -50.36244 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 515821cf-cf1a-3370-8ccb-988964ffca1d | -11.08106 | -51.53282 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3e20179a-462f-31cc-9c58-d08a9dd591ed | -5.77437 | -44.13074 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7b3136a5-da40-3a0b-8c1c-2267fafd3630 | -7.28958 | -52.54115 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ea4956a-32fd-330e-b135-ba37c90d65c2 | -8.50585 | -55.29692 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |


[Clique aqui para ver as próximas entradas](README157.md)
