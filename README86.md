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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c135b87-b655-3ec1-90c6-5fda00bb5e0a | -8.24187 | -46.42453 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cadbf82-1c4e-3f90-8d83-ddc4d46a1ab1 | -9.27511 | -47.40388 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05e46c19-51c2-325c-a392-668b44c7ee21 | -7.51834 | -45.30486 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e9173ef6-4ff3-303d-82f6-10bb28d88c37 | -10.44864 | -47.84684 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdcbae8f-5389-30e3-9686-0c9858b3c639 | -6.43957 | -55.27308 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 812fb06a-16fa-3004-90f8-d4eeef962a3d | -10.45198 | -47.8474 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38d90e56-71c1-3065-9e43-31b1983ce0fa | -9.46582 | -44.60539 | 2026-10-10 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7aa9aab-5166-3334-a36e-05374b8206cc | -11.27103 | -47.73813 | 2026-10-10 04:46:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f79dc994-51cc-3aa0-8076-6580e05038a1 | -10.49339 | -47.33423 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b978d7c-d410-3a7c-9d98-9df50531ff57 | -8.23844 | -46.424 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0af5a4d-65bd-3137-909d-c30e6e4f3667 | -11.56631 | -43.70583 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eceb41f0-9032-32f7-9e78-92e8c647f749 | -7.50338 | -54.998 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1d8fe097-8c90-30b8-ba3f-9ae09e3c327c | -11.87593 | -47.36618 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9117c6ed-110a-3446-82f1-1079c5049ef7 | -9.94049 | -44.8838 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4d6109dd-87e2-383a-a49c-bf8b2f46a336 | -9.21559 | -45.64935 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 601125aa-f57a-3d2b-b13b-7b146341a8f1 | -8.64769 | -54.53492 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 804cdf1b-497d-370b-b4c0-274878ef7a79 | -13.38031 | -43.89734 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 74889d5e-7095-339a-af3a-bbe6bac9f032 | -14.44499 | -43.95016 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa6cb61e-6067-34fd-bfae-a00b8f8dea76 | -10.49503 | -51.9441 | 2026-10-10 04:46:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70957e65-9ad5-3649-878c-a2cab573ed6a | -7.00401 | -47.71214 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22266e80-3b18-31e6-82ed-6c3ebf830441 | -7.52189 | -45.30544 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bd2d23ff-2f9e-3db5-848c-94e1ee0c3bff | -7.901 | -54.71452 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eefac9bc-e1ee-3fb8-9675-09e48ae51fc7 | -11.73456 | -44.94968 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 89eef128-9351-392a-819d-9e5e90c6571e | -11.0888 | -44.11027 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| deee3f2c-8626-323d-b4bd-a61111009ba0 | -11.19981 | -44.87326 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ace9626-03c5-3b1d-90f5-154aa3e92220 | -11.38043 | -55.15328 | 2026-10-10 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f843509-8e86-3fb8-979a-059463df30a1 | -8.52163 | -46.89334 | 2026-10-10 04:46:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd9e264f-2b8f-30ba-9056-3725f21770a0 | -14.43925 | -43.9613 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82fb5568-d8f1-3e12-a5a2-d61e5703d01e | -13.13033 | -46.32168 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de5c7350-35cf-38ef-95b4-0c9384e5f1a2 | -11.9522 | -43.48366 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fabb77f-fe08-3fe9-91f4-a92b460c2b1b | -15.37963 | -41.93879 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 1cb52ad3-8c5c-3ca5-8607-8fbb731f0e43 | -13.25848 | -44.00814 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7866611-ba79-3692-8d66-1075add06cd8 | -9.9608 | -55.33183 | 2026-10-10 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebf6be80-5dbc-311a-b729-f6635c45045c | -13.64849 | -49.38445 | 2026-10-10 04:46:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 353e72fe-3e56-3d98-bdc0-6743fc83e1ad | -12.95982 | -42.49895 | 2026-10-10 04:46:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f08f6a5-6c0e-3bce-a92e-b3c0c0074192 | -11.08808 | -44.11539 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87b56ada-b620-30a9-9583-c0dd925d1b8b | -13.63099 | -44.42487 | 2026-10-10 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 442d87b6-7e1a-3a7c-8f6d-e04bf6462b8b | -11.00226 | -47.96414 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0fc576b-85c1-39e8-b778-e242f354d5e5 | -11.52094 | -48.72939 | 2026-10-10 04:46:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52d7c9ee-21d3-332e-aa67-e3b7961719b8 | -14.45654 | -43.95979 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 205ae518-6b74-3315-a58d-1f5f14ea42c7 | -13.91725 | -47.85091 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48c4ebf6-1848-323f-9bbb-ee34509ca35f | -12.15564 | -55.43023 | 2026-10-10 04:46:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acb1c48f-801b-395f-8057-2c147cb41302 | -11.56312 | -43.70494 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f063d0a-cf83-3e80-a400-4b93479cfd5f | -6.31666 | -55.33482 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52db3e14-b200-3909-92e3-a4a96c9debe4 | -13.7763 | -48.13628 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1415654-64f8-3578-8d73-622747dab8cc | -11.37888 | -55.1618 | 2026-10-10 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dcc36ae-662d-3644-8edf-17c903d70356 | -7.92182 | -54.72778 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 452afb38-e73c-393b-b6fb-1f30828264a7 | -7.02558 | -47.66204 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85f6d1e1-3377-3d03-bda5-7c32d1db6c5b | -6.70661 | -58.71154 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fadae48-2b28-3292-82c8-cc23dc385d3b | -7.10791 | -52.65221 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06c58aa6-1105-3d8c-8b15-8ca1ce0b4305 | -14.44339 | -43.92988 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcdd1b18-a6ea-3c36-a1c7-04d5f7e830bf | -7.08923 | -55.73283 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a540073-8d71-3aa4-b7f6-6648968d2dc8 | -8.536 | -47.35398 | 2026-10-10 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1615acf4-593a-3555-bd2c-67d08381faf9 | -10.89504 | -44.82578 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2308c86f-656f-3132-8e16-7899a307fcd9 | -8.95187 | -47.37516 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e5e147c-bbd9-36a3-853d-2cacd577f3ad | -11.03174 | -45.4453 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77b8d648-c4fd-3c97-9fbe-6f39204ef1e4 | -6.33318 | -58.30374 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a08620e4-0f71-306c-b1f2-31965baa4f6c | -8.45796 | -48.69569 | 2026-10-10 04:46:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93e58a85-8476-3c4d-93c3-a707fc843a0f | -8.64852 | -54.53286 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a6edba8-9c37-3931-bd23-75d97914caed | -8.58923 | -53.09926 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d807342a-f1e3-3be7-9786-43c6f9a17677 | -12.22939 | -44.6897 | 2026-10-10 04:46:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 782faef2-aea2-3cf4-971a-f049f7492d92 | -9.46205 | -44.60485 | 2026-10-10 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4148e9eb-9b92-3f11-9771-47b06be4e2dd | -11.98297 | -43.50731 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0248aab0-1c0a-3ba9-9af3-0460fdeb5595 | -11.96693 | -43.46957 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d52a637-fac7-386d-8601-51e406328bc0 | -11.56225 | -43.70499 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f9f1e38-ec05-32ae-b7d0-05f29f0efb36 | -15.26628 | -42.38073 | 2026-10-10 04:46:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1ab8367b-e6a5-3006-9613-24503dbd5a3e | -12.07571 | -47.3817 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eb32588-a9ee-3a6e-b060-98df54aacac3 | -7.24384 | -55.21612 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c53c39b-3823-3d20-9705-624ba70fec7c | -14.03119 | -48.76179 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 370a6c9f-a694-3cb5-bd87-994e9a2f95c9 | -6.43622 | -55.03851 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34fffc3d-10d5-3ad0-bb86-18ec0d5d1f8c | -7.03336 | -47.67754 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ec48be1-6715-3478-9fff-8be93e9600bc | -14.32384 | -44.66542 | 2026-10-10 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 544c8e9f-85c4-380f-b281-2c16a22721c0 | -14.23733 | -47.30096 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 347f68a9-4a07-3589-a23e-9dd65076cacc | -6.53469 | -54.91389 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61c5c920-c01b-3ee7-89d4-7d4fcff4e375 | -7.9197 | -54.71337 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a51f270-b2f9-3880-ba5c-abcb4333eea2 | -12.77899 | -44.88606 | 2026-10-10 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b0c3fef-b299-31dd-8112-b7d03fa0a479 | -15.26769 | -42.37694 | 2026-10-10 04:46:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2e1f09b5-08c1-3231-8eca-a81bb23ef570 | -11.83106 | -43.58605 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4decfb26-26de-32d2-b7f3-6978411e8393 | -12.36396 | -46.59843 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8cd4ce-fde6-3938-acc4-52fe67fc9ee5 | -7.01449 | -47.66743 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba0c9f76-4a25-37c4-ac61-bf926b745c04 | -13.37202 | -43.8961 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38722369-84de-3bb5-83ae-e585aa8d5802 | -13.356 | -43.92113 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf0361ae-2d61-395c-8aa0-f2fc3f4c52e4 | -6.0191 | -53.47384 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee669bc5-c4e3-3bd1-a6a6-59e223384c34 | -7.75196 | -54.788 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c367cb7-b544-3043-bb37-2c0d589a10e0 | -9.99221 | -47.9995 | 2026-10-10 04:46:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86b9eb5f-e0b0-3574-a698-51e41f8be9de | -9.75921 | -44.78242 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f51cc066-b2c8-3863-9291-cfb81b77631a | -6.37049 | -55.1638 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fa36314-e9a2-3b93-af53-474990786319 | -9.09558 | -54.703 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f69d9db4-fe08-380b-bdb7-86f449fe1789 | -11.59854 | -43.74432 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01b4844d-2785-332d-bd83-a178e05b9fa5 | -15.10253 | -43.63348 | 2026-10-10 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3cf9819-74b0-3c90-a96e-b448c149479e | -10.89258 | -44.81596 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88f06408-03ea-358f-bea8-219893ce9f75 | -9.89227 | -47.62825 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d458907-7f89-3501-9c68-3ae4f5ead88f | -14.24082 | -47.30148 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0e29e7f-0e56-33a8-bd49-ac5bb45f7aa3 | -13.46439 | -41.35037 | 2026-10-10 04:46:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b1e4d28e-f3b4-3286-be01-628c09ccaf10 | -10.24543 | -49.67599 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72b04adc-0fb3-3d2a-be6e-b1e986b3c315 | -5.89461 | -57.72657 | 2026-10-10 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f51a7b2-f324-3ec9-be7b-37e12636a2cc | -13.68729 | -49.11707 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 682dd9ed-cfe6-347e-9fb5-7faba1fb16f1 | -7.97144 | -46.88609 | 2026-10-10 04:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7323aeda-436d-3182-a4ce-b3d9e9d79126 | -6.37553 | -55.16206 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0854e46-8e66-3e87-bd3b-75171b8b20d3 | -11.73091 | -46.74 | 2026-10-10 04:46:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README87.md)
