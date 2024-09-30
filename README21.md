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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e78287a6-7b22-3b91-affb-559bdf3118e1 | -10.40177 | -46.19294 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a7323dd-8bf3-39ca-82a0-7da36f6095cb | -10.40103 | -46.19679 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f2847fe4-f326-3668-ab45-e202cb13aaea | -10.22976 | -46.86693 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2627f4c-11f0-3cfb-a971-543051c3ed3c | -10.22892 | -46.87125 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96ec8794-ffa5-3e36-935f-d1b714b5d027 | -10.19806 | -46.88071 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd8f167b-1c23-38f8-bcd1-204224c35526 | -10.19722 | -46.88513 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5784808-49ec-38bc-8524-58745844de30 | -10.1971 | -46.85383 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3eca523b-5adb-3e62-999a-f469bfa7cb54 | -10.19637 | -46.88955 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eacebdb0-6033-38bc-9483-9ac2a1d097ac | -10.19629 | -46.85811 | 2024-09-30 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 385dd9d3-297f-3864-b708-bcf2e6716470 | -13.47589 | -48.61636 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb2869a1-00aa-30a1-9cd3-3aa6e206b360 | -13.4864 | -48.59675 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c24b93b-47a3-3a79-bbd5-cc928edc0ccf | -9.28727 | -45.64179 | 2024-09-30 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c1af3ee0-8cb2-35b1-88b3-c2c3acb983dc | -9.28206 | -43.51283 | 2024-09-30 03:45:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b650f53-2718-36ed-b59c-c2419d739b4d | -9.28099 | -45.64484 | 2024-09-30 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5e94d44-ffbd-374c-8dca-44183e200855 | -9.26005 | -40.8227 | 2024-09-30 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c6c0923-a2c1-3cad-93a3-e830acc5c233 | -9.25843 | -40.82218 | 2024-09-30 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5524b695-737c-3946-a54a-cb68de733180 | -9.25605 | -40.82201 | 2024-09-30 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d33c702-459c-37ad-be94-7c7df324b2ee | -9.25543 | -40.82554 | 2024-09-30 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 213f081d-389f-3917-a86b-34362fe5c787 | -9.25384 | -40.82503 | 2024-09-30 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 77a9ef14-8f40-31fc-9df0-dbb5f700aaa5 | -9.01744 | -40.57314 | 2024-09-30 03:45:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 307d6615-dc0b-3e20-bb47-c78ba5dfb642 | -8.93451 | -45.67 | 2024-09-30 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d185087d-76d1-3bb3-b381-262988fce448 | -8.93012 | -45.66781 | 2024-09-30 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e207744f-430a-3d80-a4b7-91eb3504dc02 | -8.92966 | -45.66528 | 2024-09-30 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e2c14e7-b59e-3377-9be4-d758a7b3db1c | -8.92944 | -45.67156 | 2024-09-30 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe7d745f-2d4f-3e16-980e-537dd4204c2f | -8.92895 | -45.66901 | 2024-09-30 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9486ec4-9ad5-34da-82ba-bc0f31e785ce | -8.91676 | -45.64672 | 2024-09-30 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0af9f6ee-1977-3111-814b-c3a32874602a | -8.82168 | -45.20938 | 2024-09-30 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2f9349b-81ae-3200-bbf5-bce7ab30ec17 | -8.76237 | -45.15536 | 2024-09-30 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec8c51ae-2dc5-359b-85b7-4e9618ef857c | -8.76173 | -45.15882 | 2024-09-30 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14ec5ad2-a1b6-3ce6-a64b-2ecd10e695c7 | -8.7611 | -45.16229 | 2024-09-30 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3e882b8-893e-314c-b521-94a8f9a878be | -8.71611 | -40.47219 | 2024-09-30 03:45:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c92d384d-2460-33c5-9718-bae1534af71a | -8.69 | -41.06495 | 2024-09-30 03:45:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7a783d2d-caf5-3277-bc36-96529ab0f26a | -8.68589 | -41.06427 | 2024-09-30 03:45:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 77ab549e-d1cc-3f5b-ae95-acffebc0f61a | -8.64274 | -44.05485 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b30d5c8f-a713-3327-b8bf-98cfa10f2bbc | -8.64224 | -44.05766 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0423a35-8cc5-3090-a4fb-e755a53bd1c9 | -8.53071 | -44.73613 | 2024-09-30 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b01bca49-2d46-3ce9-ae19-51ffed3aac24 | -8.53011 | -44.73946 | 2024-09-30 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cdfc694-fc77-32d0-95d7-ac9441602596 | -8.52605 | -44.73185 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89d1d32c-1a43-3e34-af69-2978d3dfe05c | -8.52378 | -44.71438 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 365acc1f-21bb-384c-9fa8-04562ec56226 | -8.52318 | -44.71769 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 977b96e1-2a72-3627-8a46-1c8be52c4a48 | -8.52258 | -44.721 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 304242cf-29b6-37cb-84c7-bc4255c809e4 | -8.5197 | -44.70694 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99580c34-81de-37fc-b8b8-fe74c20847cf | -8.51911 | -44.71023 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46040c80-5431-3d4a-9aa1-2ea9ee65f6d8 | -8.51851 | -44.71352 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c22f9e9-ea73-3864-bf5a-c82ff9031136 | -8.51443 | -44.70612 | 2024-09-30 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a7a8dcf-f074-3606-891f-003927d25db2 | -8.4335 | -41.93341 | 2024-09-30 03:45:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cfeb0afd-a994-31bd-98ef-690e8466a49d | -8.40388 | -41.27756 | 2024-09-30 03:45:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 287dad36-8c0d-31d5-89da-6cba98c28714 | -8.33224 | -41.17037 | 2024-09-30 03:45:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f30f1e0-dac6-3ceb-86d2-1dfb8e7bd941 | -8.33046 | -41.17056 | 2024-09-30 03:45:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3ab22e1-e76b-369a-8aeb-bc82f244caed | -7.96089 | -41.37867 | 2024-09-30 03:45:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 98f4f4c3-4481-3824-98be-55f57d718055 | -7.96079 | -41.37778 | 2024-09-30 03:45:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 76f88302-9beb-35b2-861d-0cd624b09044 | -7.96009 | -41.38179 | 2024-09-30 03:45:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 423f1d2c-9e1a-3ee2-8257-0edf5e1d4b70 | -7.92328 | -42.76821 | 2024-09-30 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ced6ce85-2d60-3239-aa0e-d2d8ca15e071 | -7.91862 | -42.76738 | 2024-09-30 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2af3c291-3e35-3259-afb6-4f6c8c11ce01 | -7.91779 | -42.77217 | 2024-09-30 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 32515fe6-1e78-3283-9b68-c4b7f7f815f8 | -7.91478 | -42.76185 | 2024-09-30 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0ac25367-6331-300a-8b3a-a61ca65f699e | -7.91395 | -42.76659 | 2024-09-30 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 053e5923-fb1a-3693-a77d-03a03a808355 | -7.91012 | -42.76101 | 2024-09-30 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 038bed80-8e39-3abc-932e-b83c2b82fe38 | -7.9093 | -42.76578 | 2024-09-30 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3b9f2251-a975-3058-a042-80564ff168bc | -7.90464 | -42.76495 | 2024-09-30 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0cdb67ab-97a8-3cfb-921d-2e3381fe6484 | -7.88906 | -42.66252 | 2024-09-30 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9dccc33c-b4ee-3736-a6e7-e5c9a2ed4579 | -7.88443 | -42.66171 | 2024-09-30 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c44778ea-0bc0-3964-a8c3-0022d0084d1f | -7.88359 | -42.66648 | 2024-09-30 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1e851eee-f5d8-3cf4-ac21-7ffb15460561 | -7.87627 | -45.33437 | 2024-09-30 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5562818-a526-356f-bf85-6ac076585389 | -7.87139 | -45.32978 | 2024-09-30 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ddd640f-8768-36e4-a18e-231d65113756 | -7.59479 | -43.85654 | 2024-09-30 03:45:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 994fcdf0-00b1-3b02-add2-27ff7cddf88c | -7.56951 | -43.85243 | 2024-09-30 03:45:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1c498b0-300e-3ade-9c02-63d9894035d3 | -7.56835 | -43.85889 | 2024-09-30 03:45:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 617f9ad2-0ba2-375d-aa66-2a846200beca | -7.50388 | -44.9726 | 2024-09-30 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f72aa6be-01b1-3a80-844f-5dc1775cbe39 | -7.50321 | -44.97631 | 2024-09-30 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c718411-0a30-37a2-bc3b-60c62d22cd3c | -7.50256 | -44.97995 | 2024-09-30 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01628e9a-f743-3ffd-82d0-cc1b4ee04a0b | -7.49773 | -44.97554 | 2024-09-30 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4f93bfa-e2a2-3390-9d32-9c85e7c805d7 | -7.49709 | -44.97912 | 2024-09-30 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b6537d3-5c0b-39cb-a2fd-f2bb8249ed84 | -7.49286 | -44.97139 | 2024-09-30 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 723b9500-1fdb-349c-82b8-cbdd528fe7a0 | -7.4859 | -43.85942 | 2024-09-30 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eec989f4-4da3-3e0f-bc9c-f2efa4787e88 | -7.48538 | -43.86235 | 2024-09-30 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88eeae91-7248-34a2-853b-e0a435faf0cc | -7.4814 | -43.85542 | 2024-09-30 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb6c4b56-1b01-3e62-9263-74cc458760b2 | -14.64267 | -41.68932 | 2024-09-30 03:45:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f5be194c-a3c2-39c6-a352-ac16870b819e | -14.59596 | -45.74729 | 2024-09-30 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3d3d765-982b-3fe2-a587-1523adf55e36 | -14.54479 | -45.40123 | 2024-09-30 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36618b1d-24b9-32d0-87b2-4101f560dbdf | -14.52667 | -44.98785 | 2024-09-30 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47c7c77a-0d20-3041-a584-690d8b638688 | -14.49063 | -45.25192 | 2024-09-30 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43b6f92a-86b4-3b09-abda-cd5fb3a17f2e | -14.17974 | -46.45019 | 2024-09-30 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b8a9cc3-bc77-3f90-a573-3e8aef390b4f | -14.17902 | -46.45385 | 2024-09-30 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27031d9a-f8c5-3fed-a29c-c8e328af5b2f | -14.1783 | -46.4575 | 2024-09-30 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed356a4f-3e78-3dd6-92e8-d3639b026266 | -14.17759 | -46.46114 | 2024-09-30 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35c0edcd-a10f-30ca-8a96-4f20ce705c92 | -14.17307 | -46.45596 | 2024-09-30 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 141e2788-9118-30fb-a5f0-f5157a8fddc8 | -14.17235 | -46.45963 | 2024-09-30 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6538453-a183-3f85-883a-035d82b323f2 | -14.17165 | -46.46315 | 2024-09-30 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ee108bc-e3a9-3252-8757-b69b52252b16 | -13.87595 | -43.56516 | 2024-09-30 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 324e174b-69c2-3c6c-85b6-7c0830ca532a | -13.75445 | -42.6007 | 2024-09-30 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e9beacab-fe5b-3504-ba98-1960d5f44b4e | -13.75374 | -42.60459 | 2024-09-30 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 329c97b2-0d42-31a7-9b03-201ede50f96b | -13.49378 | -48.5921 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 484e2489-4999-3943-8419-62646262a563 | -13.49261 | -48.59776 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d7cdae1a-f99d-3c8f-a842-93aa678405dc | -13.48764 | -48.5908 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7c8385bb-130e-33e2-902c-a448b4da176d | -13.48313 | -48.61244 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 03d5ec38-f563-3099-98cb-46e62c333fe7 | -13.48202 | -48.61777 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 068f0565-7976-3a0d-9fe1-cd444e851176 | -13.48025 | -48.59545 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 782e93c1-37ec-3e5a-9b8d-46f9a35c62be | -13.47702 | -48.61094 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6c646e3-4676-350a-834f-7d12c420ab5f | -13.45808 | -48.6146 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README22.md)
