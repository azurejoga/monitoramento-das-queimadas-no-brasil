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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b4db912-fc5d-3c0e-bbfc-a2b99b23dd5e | -6.50854 | -58.29271 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aaa13bbf-8654-3f2e-a9b8-88274110df69 | -5.35449 | -56.03049 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d18c6ad5-62be-38e3-9ba1-93c9bca6bef7 | -5.3656 | -56.03247 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9879e2ba-3e84-3449-a8f1-e070b616d4d7 | -5.3532 | -56.03793 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ed992b3-ff32-3dea-a3dd-c4b36b49d115 | -11.32481 | -45.08472 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a77f03b9-eec7-3f6c-bd79-d141985e9eb6 | -13.84998 | -43.65014 | 2026-09-07 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 411439e6-8308-3574-a949-524a0c754733 | -11.03868 | -44.34159 | 2026-09-07 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b057f755-3ac2-300a-907b-b730a5d8b0c5 | -11.33182 | -45.11002 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75db73d0-3f22-34d8-a138-2e5d7ffe9816 | -11.3219 | -45.08018 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 920d1958-2b31-31e6-a31f-cf1ecccf5b7b | -11.3253 | -45.05685 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72c32353-74d7-3b8f-8214-70aec816fa22 | -5.35086 | -56.01835 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf55728f-19bd-31ff-a921-ba685f92b118 | -5.35577 | -56.02306 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a701ea63-748b-3b6a-a571-15edab684740 | -9.74825 | -43.39173 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| dcff09dd-a8b3-3278-80e3-2eeca9b1e04e | -10.67568 | -45.16856 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5fe5ff0-0ced-32f4-b108-211deb073fc1 | -5.99067 | -57.7053 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3bd5e3b1-8b9f-3b6c-895a-a29e9027392a | -9.75377 | -43.40635 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 7dfa999c-8935-325f-9435-81c67fdbed86 | -9.72887 | -43.42099 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57697e89-f646-3df2-a10b-61d2d53e6a69 | -9.7494 | -43.41029 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 487b2479-a177-3946-be89-335a03ac3b03 | -11.31152 | -45.10256 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19f4ed9b-88ab-37d1-9619-808fc649eec5 | -5.36926 | -56.04458 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c241fdc6-de6b-3175-8659-de38d93eac90 | -11.33815 | -45.09109 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c11bd168-1b55-3468-8855-d17fb3765928 | -13.45153 | -41.8926 | 2026-09-07 04:27:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8dee524e-d7e7-3adc-b66e-b4a5afb98c2f | -10.74135 | -45.08401 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| aadc751e-c1cd-30ee-b243-70d5fc48d2f1 | -13.3155 | -45.23912 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05dc02d6-a6f2-379f-bfd1-8142ef728d6b | -12.19539 | -45.03812 | 2026-09-07 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46976ba8-89ad-36f0-a3d6-c47fa46fd012 | -5.30317 | -60.13476 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9e32e490-7335-3808-9564-552e6ee10486 | -12.75944 | -52.84885 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6552178-c2e0-38c8-a7b5-402f26abe33a | -12.76219 | -52.85662 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65c05794-bd76-3446-96ea-f0b375ec9928 | -5.29471 | -60.14054 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcc6b481-0e7a-33d3-b959-3558092d7a23 | -7.69758 | -55.38479 | 2026-09-07 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59f590cf-5ecd-31ab-bbac-0bacca3bc9bf | -11.32311 | -45.09637 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51cc5ec2-5358-3ea1-aa7a-797238fc3688 | -9.51711 | -41.99004 | 2026-09-07 04:27:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5421621b-e9a0-3c43-bfcc-562741525311 | -11.32763 | -45.06535 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| dca8f985-ea4a-3712-9c34-d68ab7b02cb7 | -5.30768 | -60.15014 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3f856b5-23d9-3510-804d-a5a062f9c0e8 | -11.32124 | -45.0602 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecd38527-32a4-37bd-af41-03f529f965e6 | -9.73771 | -43.38557 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d4a46e73-7e91-3e1c-8127-6d3f50241a4f | -5.30477 | -60.14951 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 090d9cef-5cb0-3a6c-a9b3-7531f857ba2d | -11.3189 | -45.05164 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 365f1131-3c41-331b-a86e-e2aa0b66a8e3 | -12.76158 | -52.86013 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 617cf754-7e19-3654-a5e7-02456dcc4ce7 | -11.03508 | -44.34106 | 2026-09-07 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a0a2471b-85d6-3fdf-9b7e-3c77c3bc84b6 | -12.75547 | -52.84811 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 581989bb-219b-3598-9d6c-cd7cd6cf4312 | -11.32067 | -45.06409 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50ae7436-d14b-381b-9c37-4ea35819d3ef | -13.29843 | -45.23235 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77ab247b-c73b-3a39-bf67-a838d0fe6a84 | -10.67512 | -45.17242 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9135946d-7b3c-3444-bb2b-17cbc0f4fd31 | -5.28717 | -60.12437 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 552c1552-0521-35ac-9f88-e4354fd009ef | -11.28254 | -45.09517 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1898b18e-b78c-311b-a51a-053cc4fad746 | -11.19256 | -44.62483 | 2026-09-07 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e686a0e-bd92-37ba-98d9-25610377e3f8 | -11.52626 | -49.62226 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ded7b4c9-8172-3828-90fb-f1b16e616646 | -11.31719 | -45.06347 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c00ea0e3-3701-3c3b-bfe9-66ef3a913399 | -8.84627 | -47.08019 | 2026-09-07 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f497243f-26a4-3aa0-ba90-a8fd33981ab7 | -9.98765 | -50.27758 | 2026-09-07 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f219f14-e082-3ecc-b2ed-7f474179242d | -10.6682 | -45.17137 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f97f3f8-3cd7-303d-983d-e477f22dd2fa | -9.7382 | -43.40887 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a304a389-ea9d-340a-8ca8-6ced5d80a011 | -6.05772 | -57.79105 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 494cf47a-5078-3417-bdb5-5fff71fa93b3 | -9.7364 | -43.39481 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b8430e4f-628b-33f5-a2b0-fa4e5e233e00 | -9.73321 | -43.41718 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 0fa2cd1c-dcfe-3f65-8e3f-38d053472106 | -7.10889 | -56.50827 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 464bec14-fe4f-3504-86eb-f41fa1b1e0be | -5.28307 | -60.12391 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d660480-a1fc-35a0-98d1-e2182941f76a | -11.32716 | -45.09307 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3549a23d-bb95-3a63-a63d-09cbd7470d1d | -11.50911 | -49.61942 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 353e3124-d5e3-39b0-ae5b-ee9197968f2c | -13.31315 | -45.23049 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| ea387518-d8ec-3f3d-bd07-bea6ac8f1df2 | -6.06393 | -57.79178 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c080a29-f9a6-3e80-9e16-5e5a16242bcd | -11.51254 | -49.61998 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 312951a7-aa2c-3da5-8469-1d0c358cfb7f | -6.12949 | -57.74189 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03ca11c3-02cc-3826-ae80-5394a8f5288f | -12.75669 | -52.8411 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d889ce6f-c78e-38a7-94fa-566ba951423d | -7.11382 | -56.51291 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 256ac506-79de-3f33-96b8-dfc52196820c | -10.74251 | -45.07625 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84e063ca-7046-35d7-9697-526aede803d6 | -9.74452 | -43.39119 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 07ff29cc-d3cc-38e6-87ec-218a88170a66 | -9.73705 | -43.39016 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 46795089-44b6-30b9-a62f-aebdb5b4583f | -5.29889 | -60.14115 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2fdd22a-3864-37d9-8e8c-ad91b7aa1a5f | -5.36068 | -56.02777 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f274f41d-7635-3e16-86b6-9b71c541c89d | -10.37642 | -45.01459 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95318266-07c7-3adc-a2d2-cba577189682 | -5.99233 | -57.69611 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e69d22fc-bbaa-3326-9196-53f5248af845 | -11.3445 | -45.07208 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e46888e-1fd1-3484-a279-aa29aa4f14f9 | -10.73846 | -45.07959 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e959b19-590a-3a51-860b-25c37beb983a | -12.76402 | -52.84608 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f895229-1672-3400-a688-a60555f412b6 | -5.99759 | -57.70201 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bea958b0-ffeb-33ad-9c74-026cf596a6f2 | -9.23793 | -46.68291 | 2026-09-07 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9def4e1-1f89-32de-b210-3861689a249b | -13.38226 | -43.67939 | 2026-09-07 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0fc916f-0527-3383-b79a-919e9de1f488 | -11.31568 | -45.06432 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84ca0afd-3873-30aa-b622-e281201eb516 | -6.0551 | -57.8028 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba86ae27-5d57-32f6-913d-2c3a73c244e3 | -5.31839 | -55.87852 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b909751f-66e0-3fc0-84f0-393355ab39f2 | -13.85385 | -43.6507 | 2026-09-07 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| af54869f-0c84-3589-994f-8ae1de8a6b4a | -9.74761 | -43.39624 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 07258f4c-981c-36ac-acf4-581bd15a373d | -11.51535 | -49.62435 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff8b376a-71b1-3b1f-8cef-0cfe2d667132 | -5.29021 | -60.12516 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 365ed818-fdc0-3261-ac4a-8c3dacee5f3d | -7.11946 | -56.51351 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 430ced3e-b92d-3c56-9ef3-b9be1b57c397 | -7.91394 | -47.66406 | 2026-09-07 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c52030f4-b91d-3b9a-9d2a-31f781922e08 | -9.74503 | -43.41427 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5984532b-ea4e-35fa-8555-f39a83d97a8d | -11.33227 | -45.05799 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d6f15a8-1de0-38ff-85d4-0533df64e7ad | -9.52116 | -41.99063 | 2026-09-07 04:27:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5293be25-2efe-30fa-8ee7-ea58af1882b7 | -5.36687 | -56.02508 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5114df3f-e40b-3bb4-a2db-2929988e2dfa | -12.76005 | -52.84535 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 864e41e7-74b5-3740-94fd-634c691ee72f | -7.10127 | -56.51874 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e71fa593-8e2c-325e-a2fe-f288c1b6fd87 | -5.30017 | -60.13406 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d08bfb95-f21d-3f67-aef6-a0c2993d92c2 | -9.74002 | -43.42277 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 91f4ac15-4992-3d6a-8901-f4789e20b110 | -7.69246 | -55.38386 | 2026-09-07 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c33e961-2a42-3b2b-979b-67ffdedbb1f2 | -6.06306 | -57.79398 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd884206-d385-312f-8878-06cab38e3aa2 | -11.32181 | -45.05626 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36de4e45-94e5-3a47-b17d-e7127862d9d2 | -5.36004 | -56.03148 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README17.md)
