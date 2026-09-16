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
| 4ca22cbf-6608-322c-a820-877816cf99bf | -6.9457 | -42.57822 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b624741-ed76-33e4-a8c1-82622d683944 | -5.88058 | -35.35128 | 2026-09-16 04:14:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4bb44e62-0e63-3b36-a5dd-89217d106353 | -5.08822 | -39.19421 | 2026-09-16 04:14:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7345eec-cabf-30ac-9ee1-fbbe39ba816d | -3.01484 | -51.34047 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02346ab6-b001-3ba5-b21f-df88f7126356 | -6.72769 | -48.11664 | 2026-09-16 04:14:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3d7e82a-c95e-3411-8712-dedbf69ebd2a | -3.15264 | -49.22828 | 2026-09-16 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9684d85-27f7-31a9-a6dd-2af040aa1391 | -9.81096 | -48.91336 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a1c516f-ecc5-38d0-bd61-47c39d0dfeb9 | -10.84732 | -46.17564 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 274f6ce7-58bb-37e2-bb6a-8a984858ca6e | -6.72844 | -48.11231 | 2026-09-16 04:14:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c672532-706a-3b33-8921-d919af9a88a1 | -10.56945 | -48.56831 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1314fddf-7520-3855-991c-1e19891ac636 | -8.8602 | -44.9077 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88324fc9-a4f4-3de6-b08c-a5f81c6e87cd | -7.35858 | -44.49643 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ab0d441-35f7-3bbc-955d-6c0fda4960b0 | -9.42328 | -47.84346 | 2026-09-16 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 892a38aa-d861-3174-9ef2-23f5adc85ca0 | -8.84457 | -44.89289 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7df6b05f-852f-30b5-b74a-dbc6d027fcca | -10.40856 | -48.6385 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9fba0e48-ce23-356a-af54-fb0b7a238eec | -8.40099 | -45.65026 | 2026-09-16 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a96247a-4b02-35d0-bdd2-790c146f6e0d | -10.10314 | -45.56399 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4b19b4b-5e6b-3fb1-86ca-59e0045fe784 | -2.91597 | -50.40093 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdb6941c-5702-3a5e-a31d-2baf47a945d3 | -5.65832 | -43.56548 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17edf3da-4b89-3ef2-975a-7d1e6647fcdb | -7.07131 | -42.13123 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e870fd24-dc1e-37e5-9abb-c45a3ed47121 | -11.20257 | -42.83228 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a169171c-742c-3770-934b-70a0d0f62530 | -6.94902 | -42.57874 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5fff66b2-f0c0-3257-9c0b-0c741cd96f9e | -10.11407 | -48.81102 | 2026-09-16 04:14:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3aee9e36-e68b-3565-8256-ecd47a36d325 | -11.36275 | -43.95317 | 2026-09-16 04:14:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab745745-0717-3471-a2cd-278259a153e1 | -3.01414 | -51.34471 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 94fa5d40-8d04-374c-b060-759dfe89f51f | -7.22138 | -44.45008 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa965f84-c0cb-303b-b4f3-ade1f3e8d41c | -11.20093 | -42.82122 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 14155c50-ee19-375a-b09b-081e8c517a54 | -5.45027 | -47.47415 | 2026-09-16 04:14:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67ca84bc-1b48-30d2-8cba-6e7df687d57f | -11.19597 | -42.80962 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ffc49fb3-81e7-3f5b-be33-f857562aa486 | -3.37718 | -50.45667 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 612d76c5-6d16-3da5-b0ef-74bc24aca378 | -8.04952 | -43.7441 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f844d75-e3a9-392d-bf60-234ec6f030be | -10.30695 | -45.32278 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d35d79d-d367-3427-80b2-06bf9cc65d3a | -4.51906 | -54.94723 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd3d676c-8d36-37e4-b759-4bcf9a2d6b02 | -10.40255 | -48.65711 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6dbcd33-5b41-37f6-84b5-1d0744716436 | -7.11873 | -42.08904 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 56c3a074-db4f-3884-bf67-13f70ac2eb93 | -5.4023 | -41.10749 | 2026-09-16 04:14:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 450269bb-f69e-393c-a7a5-b5b1982928f1 | -7.24158 | -46.17744 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52ce5993-39ff-36c6-b02a-2ec92d19142e | -10.84947 | -46.18498 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78505725-96cf-3c7f-949e-26a14c2c44b2 | -2.89913 | -50.43443 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3172ed8-15ec-332d-b97d-fdfcd669cc15 | -8.61117 | -44.45564 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c10e70-28c3-346f-8f4f-941710ca7760 | -9.09754 | -45.72193 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cba6bb8b-c066-349e-b972-d8c75e0f5b4d | -11.17224 | -42.80936 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8396d31e-9828-38d0-ba00-d4d91c15881c | -9.70371 | -52.01339 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f32e958-b82c-37f4-ac81-15e7a4fa6a40 | -8.79455 | -46.90903 | 2026-09-16 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 467cfcc6-a7d7-311c-8c05-de2f549f0848 | -2.9021 | -50.41673 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09a5fd96-5e52-311d-900f-9163ff2d1b58 | -6.78885 | -48.65665 | 2026-09-16 04:14:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb373a3e-59cd-3612-837d-46540915d92d | -7.54293 | -42.66706 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6d985cb6-119a-340a-ac9e-5a19f5c83be9 | -6.64307 | -43.5498 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30fe489b-26e2-3fad-bde9-0c6f24a212be | -5.63452 | -51.6937 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 49d0f5e0-b4e9-3285-b657-7d02689777fc | -3.14354 | -51.10443 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 814b2fc9-9837-34ee-b3b6-871015109732 | -7.09288 | -40.65424 | 2026-09-16 04:14:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 862b8a3b-f145-3536-b612-fe459b0b589d | -2.90565 | -50.39562 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcb8f7f1-44b3-382f-a224-bc222348bb91 | -4.51198 | -54.94622 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f301c8-f003-30d3-bbc7-8f4f59ff4031 | -2.91302 | -50.41861 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1136f1e-520b-366c-814c-bd413f4704a5 | -9.22717 | -46.71376 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55805828-8f2d-3529-ac97-3c3b52aa14a7 | -6.27364 | -41.67744 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d2b8fb55-b7fd-3856-9053-159226e82d22 | -5.574 | -43.5677 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ea2f8ab-206c-3655-bdb9-ecd294b10731 | -7.17331 | -43.52514 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89b5e65c-150e-39dd-981a-84cef41ed885 | -5.98862 | -46.63192 | 2026-09-16 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8167ad42-925c-37af-ab88-2118b77689de | -6.78204 | -47.87953 | 2026-09-16 04:14:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c0f646c-9fed-318d-a8f7-3b08f689afef | -4.9865 | -45.15773 | 2026-09-16 04:14:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5adaa184-9f09-3c5d-b7f1-34478f9b7dba | -7.33817 | -44.48912 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b0abe7a-ec1d-3fdf-ac41-aefe8a801287 | -9.59419 | -46.70698 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 725af7c8-e05d-34d7-8d8f-adce1a71f5b7 | -7.09977 | -41.82343 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dd96efba-2680-3853-a0a6-621084bc204c | -10.41038 | -48.66281 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b378f505-947d-3e3b-a1af-c4b982bd4725 | -4.51526 | -54.96866 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6975f0e6-10be-363d-8ef5-3619f39c9fe4 | -10.49078 | -45.28595 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd97336a-bf70-387a-90d8-4b699cf9476a | -11.16567 | -42.80831 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 557c3de8-2b24-33a6-841c-03811433b215 | -10.4107 | -48.65108 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d907427-51e6-30e7-b4ba-723bd08c7f7c | -10.79093 | -46.19975 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 77f4cc95-96ff-3733-b6ca-842ce487faee | -9.09317 | -45.7256 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95e9030a-256a-3fb2-9322-8593c218c8b5 | -9.49003 | -45.43754 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf3806ba-2a88-3800-90da-54c71f0ec83a | -9.55014 | -45.42156 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4c5ed56-0623-3f8d-b993-5c9d1d9fa633 | -2.89664 | -50.4158 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99e1285e-c45d-3713-b2fa-26f50d30fe3a | -5.99624 | -52.10391 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf28fc0d-5e11-3d84-a927-9c060ca3c4e4 | -6.78708 | -47.87603 | 2026-09-16 04:14:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2969643a-a42e-339c-b12e-a55317039d8b | -9.7533 | -46.47972 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8953808-35a8-3320-9abb-a1dab8ed5fa8 | -11.17002 | -42.82339 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0efb6fcf-f481-3236-8800-872906874254 | -4.3433 | -46.61733 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bc4d729d-2914-3d4b-85a7-b4a1ca4dfa8f | -11.24313 | -43.47353 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0109d98-9a9f-3715-a37f-152e5cc700fc | -4.33977 | -46.61296 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b7602886-526f-3642-a679-8540680e0c74 | -8.54696 | -44.50024 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5d1e9c90-4390-3769-80bd-9fc4ba501be3 | -8.05232 | -43.74834 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00d95a77-251d-3ec9-bae5-e5a56cbb207b | -9.11434 | -45.7335 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3e42165a-c431-3bf0-a8d0-92f13f8261e9 | -5.60746 | -44.84134 | 2026-09-16 04:14:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ae09079d-b590-306e-961c-127151cdedec | -7.16951 | -42.11139 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ecc68760-ae18-39ce-ab91-5563d8da04ba | -6.6737 | -43.38203 | 2026-09-16 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 493f471d-3be9-3285-9997-104f987f4b76 | -9.22509 | -46.71625 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5d4e0db-630a-31f9-88ad-3e25eedee1bf | -11.83109 | -37.57619 | 2026-09-16 04:14:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ba194fe6-845f-3a70-99a6-bbb33fe16750 | -10.17297 | -39.99671 | 2026-09-16 04:14:00 | NOAA-20 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d47cd850-2597-3973-8a86-1e4ce1f80a44 | -7.35029 | -44.50305 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c2ceeef-81fe-3893-867e-cef6b6b3aee7 | -9.23135 | -46.70246 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30eb89c9-ac08-3772-b327-2c82296e27ef | -6.01572 | -51.79251 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e26d3bb-9c61-3c9f-a1ad-d5d8f81d0553 | -3.01982 | -51.34591 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a221d0e3-dcdb-38c5-b966-b0c4a7a573d2 | -8.85383 | -44.90251 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 024e7dc6-ff37-3b36-9a19-e7ef4c506dd9 | -7.18689 | -41.80884 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20204d7f-e572-36b0-b04c-7a33f25282af | -10.0948 | -45.61345 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95b91b6d-6888-35d0-b255-955e6c855220 | -9.46865 | -45.45531 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9e35741-27fd-373a-80be-13aa3361801a | -7.1731 | -41.8102 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4446e873-702c-3c6b-bad5-e5e437a91651 | -7.17508 | -43.51421 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
