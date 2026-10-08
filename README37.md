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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c59f92ab-4fca-34c9-8ebf-13d5f3335856 | -2.8918 | -54.1562 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b672e4a3-72c0-3cbd-b859-1987586f302a | -3.0915 | -53.766899 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3faba319-8c76-377a-bce4-b53a5fb055fa | -5.6872 | -53.498402 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9b86d38-6ac6-31a1-8c39-1d3e752d2b16 | -4.4282 | -55.1712 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 109a7728-32dc-3cea-9841-fbbc91e1fec7 | -3.2973 | -54.082401 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3af1585-440c-36e4-9886-acc1eb00dcec | -3.0389 | -54.2598 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bda7f0f-4b13-39b3-b862-d8cee942f73e | -2.9668 | -54.123699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb42304-f1e1-364a-8c4a-08732063a034 | -3.5134 | -59.3279 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d250dfb-499d-382c-9cdd-7e7f09e5f1e3 | -3.0435 | -54.2346 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f1d5f36-9999-3ff3-af4d-20bb03b69008 | -3.1483 | -51.6278 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26903ee5-849d-34a9-a9e8-f081e7bb0fae | -6.2466 | -52.875198 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39d28f5d-7cd4-337d-8568-23ac5a2fbb51 | -5.2931 | -60.103699 | 2026-10-08 00:48:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82e2baa7-e2e7-346e-aa60-0732287959f6 | -5.7988 | -52.7616 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463c7ef7-1d2d-3d70-bb61-3fe9901a52e1 | -4.3023 | -54.794701 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9454fb-1f5a-37e7-aae7-17a0bd21f04d | -3.5486 | -50.098598 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b17a7efa-a923-350e-bc6d-c1bdf63fec67 | -2.5022 | -56.2453 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbd0dda4-e228-3b5b-9901-37e3dcf42130 | -3.5033 | -51.691502 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cabb5f50-f155-36c6-b863-9c428e619674 | -3.2985 | -54.042301 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8b22bb-478e-377c-9fcc-1f0850b322bc | -3.2085 | -53.873199 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3801a8bf-6770-3efc-8629-332bbd728d02 | -3.115 | -54.1866 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15f98181-9f4d-3f8c-83f0-8a307f9e99d6 | -2.9933 | -54.1497 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de42260a-36b8-38ce-9854-9a7baf1b2e9b | -2.7091 | -57.476601 | 2026-10-08 00:48:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7336d0b4-a8cb-3d50-9917-562d299b46d6 | -3.1013 | -53.764801 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3083f17-a972-371f-9f02-ce0df302a983 | -6.1093 | -55.712601 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a709e24f-1a2e-3df1-9d65-db09c5e6c094 | -3.1081 | -54.1562 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 224ad568-0a4e-3e77-a624-81c34d66ec45 | -3.3423 | -52.518501 | 2026-10-08 00:48:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f300bb2-0938-37ce-9699-2d482b2fc60b | -11.0191 | -45.453098 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85b8a507-00d7-3383-928c-06e55d40ea94 | -7.2049 | -55.1008 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28bb804f-3169-323a-89b1-d7306e60e4cb | -3.3497 | -50.487301 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7745a1a-4d2a-3891-90bf-d2b0228db3b2 | -2.9126 | -54.1119 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbabcf17-463b-3036-9473-0dede6ddea15 | -2.1033 | -52.062199 | 2026-10-08 00:48:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73d98554-1c3d-35e9-9ffa-0d1c64ebad33 | -8.7181 | -45.1702 | 2026-10-08 00:48:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a1b0e5f-6561-3534-965c-a55265ac87ef | -17.1215 | -41.352402 | 2026-10-08 00:48:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2211855d-60cc-306c-a788-19f89cd2ee32 | -11.7613 | -44.936401 | 2026-10-08 00:48:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7b35da1-bd3e-36ff-acad-58195bc5b360 | -3.2661 | -54.670601 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee9d430-94f1-31ff-850c-f65e15209732 | -3.2453 | -56.806599 | 2026-10-08 00:48:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 208b81ad-e9c0-3635-9e2d-a63146891229 | -9.8209 | -44.7808 | 2026-10-08 00:48:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 283f2e07-6f5b-3dc4-991f-0f028083fef7 | -3.1288 | -53.7047 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122bb52b-5021-3843-8deb-e7c57e39bf58 | -2.4808 | -56.150902 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ea015c1-0c41-3a3b-b739-41139174769a | -3.2967 | -54.034698 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43a781de-b5d3-3aeb-9886-e5ce46610d6e | -3.2702 | -54.0089 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 150c2b25-f39b-3eda-8f31-e05a8d3ce0a0 | -5.8801 | -53.624199 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80c7ac54-dffa-30b0-b445-612bfb0bbde1 | -9.9309 | -48.784801 | 2026-10-08 00:48:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc130991-fac3-3312-9fd1-0e7721deeef4 | -2.7616 | -54.082199 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39b1c24e-43aa-3545-a19d-c1cdcc09a8fb | -5.2411 | -50.905701 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef025433-6155-3c63-90f4-628ba004a9a5 | -2.497 | -56.176899 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70449856-7f77-323a-a174-1dbf7a071c96 | -2.9575 | -54.173599 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c803bc1b-aa50-3e44-b0d0-4f5e22703c10 | -5.9693 | -55.358501 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0d58b15-8545-3fd1-9749-b6666882733a | -3.2557 | -54.0359 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c712bdb4-943f-3b2b-bd4c-b9a2f8d4b290 | -3.1762 | -58.6418 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94d9308c-8662-34cc-a2b4-eb3114d01102 | -3.2973 | -54.6721 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f84a2755-bf06-31ac-94a2-0f89c68ad8d9 | -2.7488 | -54.1166 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feb939d0-5a19-3c03-9dcc-498e3e1eea40 | -6.5002 | -55.392899 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2feb8a-3e05-3ff0-923d-af7225d10160 | -7.4689 | -42.868401 | 2026-10-08 00:48:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86268ff7-97c4-3dc7-af88-c9f986d49b07 | -3.0336 | -54.100899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18a625c3-c4d2-36db-87c2-4efc688ec061 | -2.9996 | -54.132301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca919ee6-b153-3396-a91f-5288129034c7 | -2.4829 | -56.160301 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01390b64-b32a-38f3-902e-9f2fd39bc0e5 | -3.2886 | -54.044498 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83a662d6-d3c5-3bea-bcee-10e436ee3018 | -5.0417 | -49.774799 | 2026-10-08 00:48:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ea311b9-999b-3ccd-a5c2-2d5aae4d5f64 | -2.4737 | -56.074001 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbb2b959-a322-347c-958d-b9d6e2aad105 | -9.8809 | -50.498001 | 2026-10-08 00:48:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8da10224-f9b2-3a47-b5e7-83b66e103cbe | -7.7469 | -54.953999 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6621b9cb-dba0-3ba7-a3f3-25f504c91a06 | -11.2653 | -45.190701 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc8f5cc2-065b-375e-8b8b-6a860d40423f | -2.9835 | -54.151901 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e95a46-e535-3b92-9da9-ef4708d7712b | -2.4604 | -56.106201 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 892c6b54-22d9-39b2-9570-55ef368543e9 | -3.0307 | -53.951801 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac2baed5-f4e9-38cc-aacd-ee32bd3b3343 | -3.0141 | -54.2411 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba47b346-496d-3573-905b-8596758dab61 | -3.0967 | -54.2873 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd93ca28-47c9-3213-98a3-2f4e64c3d0f2 | -2.9859 | -54.071899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4058270-9caa-3240-9017-167ef61ebc34 | -2.7667 | -54.104698 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45970a63-c2fb-3a64-bac6-092b6b1c3314 | -6.1567 | -52.659401 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6bb969a-3f58-386a-bdd1-080510eb0b2f | -3.1715 | -50.608799 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56a0db4f-f16c-30ba-9875-2eee5170c64c | -2.8607 | -54.155201 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2699402e-be36-3670-bddc-390e238ce8aa | -2.3384 | -55.7048 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84455e67-1645-31a9-a058-def3c135d4dc | -2.9593 | -54.181198 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa8f32f5-2dea-31d7-801e-b440e2ebcf37 | -11.8631 | -48.037399 | 2026-10-08 00:48:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21934abe-1a0f-3677-80af-2703c26f6a8d | -2.9449 | -54.073101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bee188e-5f59-3926-adf2-d1a15b1aa014 | -3.1977 | -50.5438 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2feab44b-953b-354e-9583-b34483a994e9 | -3.077 | -54.291599 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e9486c0-5ee7-381c-81fa-7f89e1c14160 | -5.8689 | -50.0938 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad7907f-72ac-3938-87ea-b726ea0748a3 | -1.7506 | -56.194901 | 2026-10-08 00:48:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6d422c-3168-33e8-ad5a-f1f5c432f1be | -5.7305 | -45.143299 | 2026-10-08 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae38af9f-412d-3e9b-abe4-f68116a774b9 | -3.2068 | -53.865799 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e91d22b-2ee2-314a-bb93-947e31a54608 | -3.2759 | -54.079102 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24ed43d2-c652-355d-9ac0-8e8d521aa120 | -6.1673 | -39.4361 | 2026-10-08 00:48:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 98bcb7bc-b227-35ab-b12f-22a13ffc5a56 | -3.1017 | -54.9893 | 2026-10-08 00:48:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b81b70fe-01c1-332a-af6c-cdaad4c45046 | -3.0208 | -53.953899 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b3dc8e4-ca60-3a06-9477-274ad091798c | -8.3848 | -46.309898 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73ed0d86-b191-3cc2-8ae3-688943e14637 | -4.0639 | -59.832699 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10525634-59b8-3817-ae04-3c7a6af036af | -3.522 | -54.664799 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 145df014-f6f6-32de-96b6-3c33979e1a8e | -2.7731 | -54.087502 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3231c2e4-f305-3eae-b7af-17c3765a9293 | -3.0994 | -53.711201 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b8fe76c-3486-3023-87ee-127fb97e1de3 | -1.1006 | -54.163101 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c514d46-2fe9-3078-b020-291cc107f594 | -6.6233 | -43.735901 | 2026-10-08 00:48:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbb10b4c-bef2-3dc4-a56f-098b76154791 | -4.2974 | -49.103001 | 2026-10-08 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ece2808-7148-3717-8c98-b71a3935b1af | -2.991 | -54.094501 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 714acad3-2ce5-3b0b-b799-5a6f9171fefa | -3.466 | -59.5732 | 2026-10-08 00:48:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7198f3-b3f5-312e-b581-ffe549ad1601 | -3.0158 | -54.1129 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f043117-5a89-3b4e-8ab2-19aa6a949b2c | -1.8224 | -54.931301 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bdbc372-46a0-38c6-b30e-fd5de706b762 | -6.2335 | -52.862801 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README38.md)
