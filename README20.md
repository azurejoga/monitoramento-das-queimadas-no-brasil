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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0e91357-4925-3e2f-97f0-cc3e9eb1739d | -9.30357 | -44.35064 | 2026-09-10 04:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d69bb2c-f095-3e92-b679-8633a424650f | -7.46055 | -42.12381 | 2026-09-10 04:08:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd4b5d2b-ae0f-3efc-ae87-0ff1c1db35e2 | -7.98073 | -43.98988 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10fb97f1-8720-32df-aafb-63275e2ff901 | -11.86363 | -44.87366 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd2ecf3c-62cb-3973-ae83-a70ba19201bf | -9.68993 | -43.47624 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f223a37-382a-34cc-aafa-62ae63d3e3a8 | -9.70722 | -43.39991 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ff8b7869-ff45-38b3-b6bc-9772638718b6 | -7.9902 | -43.95073 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddda1338-5151-3e8e-a70d-8b00ecfd10b6 | -7.48722 | -45.28004 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0a36df4-d095-335e-ab34-5d5a84ee5763 | -11.18912 | -42.78868 | 2026-09-10 04:08:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b85f4971-6a52-35f5-972e-86dd52d95222 | -7.02473 | -45.11036 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31448907-5a3f-3b80-9ff9-fa13b0124908 | -10.7368 | -45.92138 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 29c44921-64cf-349d-b252-242fd81f4715 | -9.69721 | -43.45734 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 17b8c6a3-71bb-3edb-913d-61ea59cfa2a6 | -10.43089 | -42.74268 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 041bc362-854c-358e-b765-5c3732a257a1 | -7.98172 | -43.9752 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a643c61f-c75a-34dd-b663-cc9c41d3ec61 | -11.86872 | -44.84517 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8917d703-853c-3f12-a2ba-697551e96121 | -7.25863 | -45.35244 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a75a6c4b-4297-3a64-9f29-39b4f7744991 | -10.23197 | -45.20986 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a171eaa9-a9a4-3dc5-99d3-70c58b229d6a | -2.7331 | -57.6465 | 2026-09-10 04:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 70dc9d9d-6896-30f7-96ae-55c9d4519b5a | -6.5453 | -62.8914 | 2026-09-10 04:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 71de4c82-6f4f-3a38-a44f-eec07e199b57 | -2.7331 | -57.6271 | 2026-09-10 04:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 837e971d-9df9-3e85-bd95-5e3b4d12e97b | -2.7332 | -57.6077 | 2026-09-10 04:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d52ffe9a-88b4-31dc-abd7-6bd8e86abb3f | -16.39551 | -43.21133 | 2026-09-10 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c00be08-64b6-30fe-b5bc-a1b3d2bd74fe | -15.78549 | -43.56487 | 2026-09-10 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 316e3695-925f-3be1-9708-3871964b0fb8 | -14.91192 | -44.67127 | 2026-09-10 04:10:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f8f1114-1204-399e-8aea-343781ef1ac8 | -16.35676 | -45.06181 | 2026-09-10 04:10:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26a2ac4b-017a-3ad9-aaf3-85c71dc8cbef | -14.90023 | -44.68179 | 2026-09-10 04:10:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e877dfd8-2ff0-33de-81ed-c325ebeb67a3 | -14.90722 | -44.67538 | 2026-09-10 04:10:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9207353-f41c-3551-9b85-a37ddf56c681 | -15.71912 | -42.24611 | 2026-09-10 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 107759e9-64c8-3831-8053-4899067e567f | -18.94114 | -46.82306 | 2026-09-10 04:10:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bb31f5a-f639-357a-8c56-6b9a082dbc31 | -14.90108 | -44.6769 | 2026-09-10 04:10:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca446114-11f0-330d-a140-d345fdd10165 | -14.90959 | -44.6735 | 2026-09-10 04:10:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00649308-1e6f-3984-a466-ca7ead7944c0 | -14.91279 | -44.66642 | 2026-09-10 04:10:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 806ab8ea-a015-3bfa-8b81-2f02423e50e4 | -14.91575 | -44.67199 | 2026-09-10 04:10:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e4d047a-3be7-39f2-8028-59b96ea8732a | -14.90251 | -44.67953 | 2026-09-10 04:10:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0837d0ff-29f2-3128-b253-8b251b9f0a89 | -15.45511 | -41.87702 | 2026-09-10 04:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6945e174-2e8a-37a3-a939-cf9d1f1b6e73 | -18.89121 | -46.84067 | 2026-09-10 04:10:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebd32338-932d-3065-86d5-743a2186e9b2 | -16.61538 | -43.3203 | 2026-09-10 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0cdc7cf-44f2-34ef-aa01-925a88884e30 | -15.78907 | -43.56554 | 2026-09-10 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f2c1645-558d-39df-948e-fefb938c8c33 | -12.83 | -44.4 | 2026-09-10 04:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92a97070-fbc9-37b2-8ef5-f311376be5b0 | -12.83 | -44.35 | 2026-09-10 04:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 214a7e23-74a6-3fcf-b1ce-b3712de36c92 | -12.86 | -44.36 | 2026-09-10 04:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5ce6943-6d41-36f3-bea4-87683b5ac16d | -12.86 | -44.31 | 2026-09-10 04:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cc93d02-d98c-3af4-93ba-f6350786e313 | -12.83 | -44.3 | 2026-09-10 04:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e969e4b6-57a5-3604-af4a-1a36abfc8045 | -2.7332 | -57.6077 | 2026-09-10 04:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b984d872-e05f-3fe0-a942-688f0bf25c3c | -2.7331 | -57.6271 | 2026-09-10 04:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 9722cfcd-4f40-3be8-ba49-620f54116f31 | -0.88546 | -47.57029 | 2026-09-10 04:23:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe454e0f-d7ce-3b77-9d39-e39af17fb6a4 | 1.00873 | -51.10685 | 2026-09-10 04:23:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3a6b309-695c-3648-b1f4-29f5eda8145a | 1.37045 | -50.68838 | 2026-09-10 04:23:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d155ac4-e95e-3651-86b0-ba410d207ba2 | -1.47207 | -47.27579 | 2026-09-10 04:23:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cddf97f7-cf30-33b8-9b83-fb0bfba17dd3 | 2.51261 | -50.85856 | 2026-09-10 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4d6a4133-194d-3b45-859e-9cfb49e1441a | 2.5167 | -50.85219 | 2026-09-10 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0ee3fc2c-2e53-3782-9e0e-2f0c398a081c | 0.26235 | -51.45373 | 2026-09-10 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0d0f946-fc48-316a-a2d7-7373de3fc104 | 1.01366 | -51.10616 | 2026-09-10 04:23:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9f10b980-e46e-3a5f-8747-886a6111a968 | 1.36566 | -50.68914 | 2026-09-10 04:23:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee0cfb05-b51d-3901-b019-2efefe217710 | 2.51176 | -50.85299 | 2026-09-10 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e449e1e0-59d9-3432-afd8-b4f91a5f8d53 | 0.25738 | -51.45455 | 2026-09-10 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be5213ab-db06-3079-8d48-8110ef49686b | -1.09959 | -48.05491 | 2026-09-10 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dfb9b4b-364d-31e1-ab3f-cb3fde3abe27 | 0.25331 | -51.461 | 2026-09-10 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99f5cb89-677c-34f6-ab16-44b65bb2cf83 | 0.25242 | -51.45539 | 2026-09-10 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3d8a91d-dab5-3da1-9f2c-b8b9d40023a6 | 2.51092 | -50.84746 | 2026-09-10 04:23:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 42602dbd-caaf-3ac9-b107-fea842b5b943 | 1.36626 | -50.69141 | 2026-09-10 04:23:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a37b8d5f-6148-3993-aba4-f8082d7b21c9 | 0.24835 | -51.46183 | 2026-09-10 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70338663-efb2-3c70-bfb4-11b9c7cd6011 | -1.47277 | -47.27147 | 2026-09-10 04:23:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e12b94f6-a7d8-339d-b3b0-affb588122a9 | 1.00957 | -51.11234 | 2026-09-10 04:23:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8db05a68-b3b0-32f6-9f09-4efbc000199e | -6.77143 | -58.61212 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccf92f85-0df4-38fe-aa6d-22bd240dcd43 | -6.79428 | -58.89561 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 718e5cd1-1806-366d-bb56-ba656ee34668 | -5.75351 | -43.26915 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdb4f995-1f1c-3d8f-87fc-a84993b74534 | -5.67892 | -43.39368 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de2ac210-b7be-3df0-a089-ad75a8306d44 | -7.14586 | -42.10317 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3adf5ec5-7fac-366e-bac1-9a5a7b78d7cc | -9.70643 | -43.40364 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e9e948df-ce58-3201-940f-66e4c580bef7 | -8.94311 | -44.40644 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 413f28a2-0f45-32cf-a711-572615224601 | -7.10579 | -42.12627 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04e9e2d8-5e60-3e46-a813-f5e0cf351d7c | -2.89165 | -48.27866 | 2026-09-10 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e27db13d-0603-3ee3-80fa-d8db4f7c0965 | -5.39263 | -44.162 | 2026-09-10 04:25:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82f77efd-22b3-35ae-9334-4d0038df70ec | -6.82514 | -43.04518 | 2026-09-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa2d375d-a631-3b46-b5b5-4660bc69f719 | -5.27793 | -55.97002 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40736176-fe20-30ea-9f91-aec697f5f951 | -4.001 | -51.02927 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9df1daf2-b34b-3923-af6d-17f527e49390 | -6.85809 | -44.86201 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f62828ad-07aa-3bd0-84bb-805d538ba7f0 | -6.71666 | -46.32811 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db3ba524-0093-3217-90b2-111d3f5be9f5 | -6.09922 | -44.13779 | 2026-09-10 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0125a7b2-2f19-349e-8595-fd39d0e6893b | -5.62613 | -45.87624 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b423741-e37e-34d5-9d0d-5e4844e77aec | -5.9903 | -46.02581 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99e32a0d-339e-3861-a2ca-4093cf595252 | -9.77911 | -43.4536 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6492941e-3fd1-334e-b79c-4b22cc8d1be0 | -5.11666 | -46.00758 | 2026-09-10 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c5e4f590-86f8-36ab-8b74-891ac6780eb7 | -3.41972 | -43.16397 | 2026-09-10 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d5455fb-509d-3167-8ad9-9cba192438b2 | -9.78834 | -43.48637 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d72f7d4-9b18-3ba2-8999-d6f8dea02ead | -2.21262 | -48.23292 | 2026-09-10 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c90d220d-efad-3444-8b8f-100b15d8f2fe | -6.71283 | -45.45647 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd35eec8-8a66-34dc-94d0-8c1f79dcd790 | -8.24084 | -44.75052 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1fe7173-cf3a-36ae-99f9-53ce8750ed87 | -6.76473 | -44.57067 | 2026-09-10 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ee1e7c5-654b-32ff-80f1-4692da022d30 | -7.50329 | -45.27026 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08c97f0e-c631-3fbd-9af6-0a1d188bd1ce | -8.94366 | -44.4029 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b08c3a9-2a36-3d34-b151-ed1ccbe18133 | -6.17087 | -44.63287 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 45fbcfcd-2850-3f20-8047-df3abd750ddf | -8.9799 | -44.97479 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31c4d2de-be11-3b9b-9e80-5f5615b581d2 | -7.48288 | -45.27056 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69d73561-ec76-39d6-ac6d-091d5d492c9e | -2.93782 | -50.4841 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dbe027f-01ca-3c25-b03f-04d1f34ba80d | -9.5466 | -45.68741 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75b59ce6-147a-3bb4-93f1-d4b4f76467d4 | -9.72318 | -43.38662 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 85859f47-bc2b-3b0d-94ef-bda5f0f691ff | -6.76401 | -58.62364 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dac2b9d-9e78-3b73-b3bc-6600330254a9 | -7.11773 | -42.11976 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README21.md)
