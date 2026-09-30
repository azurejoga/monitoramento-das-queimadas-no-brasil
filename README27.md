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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a175992-d494-3fa6-b10e-94a085481d06 | -6.73185 | -45.61802 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69222a26-5177-3147-ba69-77c84f2fa0a6 | -8.17691 | -44.42608 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c85ae011-1284-30ab-9497-b934351c3648 | -3.37328 | -50.94454 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4675a96a-6b13-307e-bbaa-da015a6c0566 | -6.24624 | -46.65211 | 2026-09-30 04:32:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a9db61c-d9d5-3b94-88a4-5d159d4c2f43 | -6.72749 | -45.58106 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11ce9719-4a23-3a4e-b3e3-d8315b3e0dcd | -5.33547 | -46.19522 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1a99820-9291-3d15-9ae0-cdd85bcde693 | -5.73839 | -45.06044 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfd0fab9-1e11-3767-aac1-1ea2b1d130c2 | -8.36798 | -45.39146 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f5f36a8-a71a-3419-b3ea-ffcead16e68f | -7.2699 | -45.32626 | 2026-09-30 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7778fc19-0b83-330a-a918-1a8a3173bcfa | -6.75148 | -55.09026 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1799f3e9-84cf-3b83-9d93-3b9ba7ab56cc | -8.98135 | -44.17864 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2450c73-2842-328a-ad94-dc95c1555c56 | -3.82828 | -55.79874 | 2026-09-30 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d052cacc-28f3-34db-b6c6-9e503b3a14cd | -2.86548 | -49.05532 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3c0cbbc-fc4e-37c1-bed6-e27988105861 | -6.10546 | -53.09121 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37982000-5686-3ada-9935-2a4e46636123 | -8.83614 | -49.70894 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03c4525c-18ca-32bc-aa86-2270e7df796b | -7.82582 | -45.8266 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ac050a98-a0b9-3d45-9c9a-571716277d44 | -4.8174 | -45.63889 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1d418bd-2a3a-3e0f-a2ae-701a9f492d70 | -3.38333 | -50.94132 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5e47818-fd17-37e9-853d-a2955a275039 | -9.10199 | -47.18064 | 2026-09-30 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5594b0f-7f66-3a57-addc-7642e2361914 | -8.38906 | -45.40917 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 322550a8-9868-3650-b8a3-a3f608ff78f1 | -4.81798 | -45.63527 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccf4d7a2-69be-33ee-a0a1-c24066b57753 | -2.45166 | -49.21822 | 2026-09-30 04:32:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76859dfe-a149-3665-9f20-7f1b00f87519 | -5.75613 | -45.16363 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| facd081b-1f53-3840-be1d-7192b1e14220 | -3.23221 | -46.93399 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1462ccf-9608-348f-b34f-be81f655b021 | -2.73354 | -49.41807 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15bfd728-fdeb-3b2a-a4c4-fa3712e9f942 | -10.18495 | -39.66405 | 2026-09-30 04:32:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8e6daa5a-c8be-302a-9a66-75df7a78ef54 | -7.50394 | -45.80732 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a95e14c9-a750-3216-9c4a-3fd7a56aef1f | -5.85814 | -51.79372 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 24a4c732-5e0e-36a3-b201-7cb60ac9fec3 | -8.49872 | -44.76098 | 2026-09-30 04:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9d10269-e226-354e-8408-7bba71020ffc | -9.10101 | -47.16506 | 2026-09-30 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8567d5ce-5349-3f3e-939e-e0b082088f15 | -8.27991 | -50.27154 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 578ae5ee-04e9-3bf7-ba27-1864f8c01611 | -3.14761 | -51.03708 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80cac365-1e66-3865-a21b-0ed29bacbb4b | -3.43037 | -50.43752 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3cf4a46-6c76-3d22-9436-5fafeaa443d8 | -2.98417 | -51.04494 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ab358374-6219-3154-afd6-2d9d261bf5cf | -9.66397 | -45.11891 | 2026-09-30 04:32:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2204a439-3886-3ad8-99a7-d0ea51b5159b | -4.02984 | -54.20241 | 2026-09-30 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2929347-983b-3092-9412-477273e1d779 | -3.83801 | -52.26376 | 2026-09-30 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 132ffe6a-f147-3a21-bd78-4c85a099de2c | -2.9717 | -51.03279 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e1263ad-f7ba-387b-b540-0a2726061514 | -8.98526 | -44.1756 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1302beee-553f-347c-9fd3-2025c2268094 | -6.78888 | -55.81882 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 683ba762-5d8b-31b8-87fe-02933ca842cc | -3.16227 | -54.09937 | 2026-09-30 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3c67ab6-98ef-3e50-9194-d57880d72192 | -9.13004 | -40.64211 | 2026-09-30 04:32:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 213c6cbb-6b0b-34e4-889d-bd8cc692f290 | -6.21438 | -42.51307 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3e3e2ee2-52ae-3ff7-8c7d-0a2c842bb21f | -7.50837 | -55.02797 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f96fc89-ae81-3ebf-a837-7a44a42cfefb | -6.41684 | -45.85603 | 2026-09-30 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82e20ac4-2538-365a-818e-b634d2ed0690 | -7.19226 | -46.50711 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ded25bc8-2eb2-3374-8518-e17e666dce06 | -3.51052 | -50.31244 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40961c72-0a23-3053-81e6-560fa4165207 | -3.1592 | -54.08282 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae2efe89-87fd-3817-bf3b-e33531a2cbc8 | -4.46308 | -45.58341 | 2026-09-30 04:32:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcac4e34-4daa-3dcc-8a20-32925294a30a | -3.06383 | -51.33862 | 2026-09-30 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6958712-bc8e-3578-af10-ffccf320663c | -3.23516 | -46.93868 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 4374df2b-50fe-3bb2-bfdd-7b07f3056336 | -3.27848 | -50.08645 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2211854-bd10-3b34-a330-be7da586c20b | -6.7285 | -45.61749 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| fe138b2b-56ab-3c11-837e-4036ae1878dd | -3.01536 | -53.87813 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f2022ff-f288-3307-9d72-f8eb43478811 | -3.18683 | -51.24366 | 2026-09-30 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5579fad-1f5a-364c-9885-b37b2b9701c7 | -5.75167 | -45.1701 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e38a208-db29-35cc-9a2c-36b1022b2ac6 | -6.32793 | -51.15985 | 2026-09-30 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 26cb1d0c-5e6d-367a-ba8b-9afb91a49936 | -4.5392 | -50.77639 | 2026-09-30 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b31cd415-5837-3553-9063-7f1370a9cad6 | -2.78657 | -49.41093 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36e2118d-0d5d-3bf1-a92a-59392584b8c1 | -3.56918 | -50.25507 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 677b67da-44f9-3e11-b4a8-5fa01f00626d | -7.81356 | -45.81737 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 785d45d3-3314-3159-a5b0-e84ebd4ca468 | -3.91383 | -49.37479 | 2026-09-30 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d06fd00d-d9ec-3883-9b02-5ffdf8234634 | -6.8227 | -45.05082 | 2026-09-30 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1303674-f9b7-3293-8adb-204a209f2c50 | -6.32574 | -51.16218 | 2026-09-30 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13f752f6-6934-3db3-b15d-0a263bfd989f | -3.1878 | -49.25056 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02bc206b-9f90-337a-8290-74b8f2f96c7f | -2.96781 | -51.02712 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f30d5ced-deef-369b-8382-9bde5de8b835 | -5.03055 | -43.57312 | 2026-09-30 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 680cee73-ca64-3ffd-b34b-c24d7597332a | -4.28762 | -48.61988 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a3ee1c8-c8c3-3e47-b979-f74e573d6eec | -6.69827 | -45.63437 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9ba019b-c4af-336a-9ffa-f93606096725 | -4.84539 | -50.68735 | 2026-09-30 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed052722-5c71-3457-90d9-18e1d96e49a9 | -6.5306 | -47.1213 | 2026-09-30 04:32:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8e62ef8b-50b0-3211-b9a1-48cbc77fe455 | -9.09757 | -47.16449 | 2026-09-30 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93e976f7-cf9e-3474-b214-b1833e20717c | -6.11003 | -53.09521 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9baeff28-8f16-39b6-aa32-da85337dee61 | -7.0226 | -44.62261 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8808fd3c-f018-3e5a-97b9-3fabe3f5d1d9 | -5.09188 | -46.03949 | 2026-09-30 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4d29a43-86e0-38d1-ba09-23960680e879 | -7.45103 | -44.60846 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 507f7bf6-9762-3388-a4ac-594e666e44a1 | -7.51345 | -47.33535 | 2026-09-30 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3909e2c0-50dd-384f-813c-ea41cd842f36 | -2.98345 | -51.01969 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2510434d-b309-3322-be2a-dc7678167687 | -8.37348 | -45.44252 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2952dca8-7395-3384-a858-04fec9d7181e | -6.22914 | -47.44101 | 2026-09-30 04:32:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56dcc527-485a-32be-9d49-4e023b9bdbd4 | -7.81691 | -45.81791 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bbe2de0-5d0c-3660-b739-a1a976fdf2bb | -2.97718 | -51.02866 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b66ea501-c0f4-374b-a216-61dfc79a82b5 | -8.3347 | -44.16501 | 2026-09-30 04:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13346673-33ad-39df-9897-05a56041dd2e | -3.09856 | -50.28242 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7065f8c1-3ca3-3a5e-9ef3-f726b4241b43 | -4.35006 | -48.96713 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d4ee2ac-702d-3558-b117-25b55a17e71e | -4.29787 | -48.60646 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d807e69-9c82-3151-b198-83cec0b0330e | -5.09588 | -49.05779 | 2026-09-30 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90a7e2c5-ee1c-34a2-b0bc-62ec5318cbe2 | -2.9733 | -51.023 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1458c641-63ae-31f6-b11f-17d19ff9d4ed | -3.37249 | -50.94931 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e261b841-40f8-3ffe-95a1-b34f9952d922 | -4.81431 | -46.84725 | 2026-09-30 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed745135-23cc-349f-a022-890f87e40a16 | -5.75557 | -45.16713 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| da69b0ec-5c60-357e-8ad7-ee0d38d2c2f2 | -5.0953 | -46.04003 | 2026-09-30 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80e39c6c-e835-3098-96d4-83845d9d7175 | -5.09589 | -46.03636 | 2026-09-30 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75f0e73c-057d-383b-a1b4-d03043b2ea57 | -3.09926 | -50.2781 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6694c408-8560-3f1c-b42b-f1e9d1e32c52 | -7.837 | -45.82111 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cdff4822-2e84-3774-a272-bae1d62cf10e | -7.53696 | -47.12081 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7bf2939-7407-39f0-abf8-73cbca159bab | -2.98965 | -51.04079 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d3e170b9-1130-3a1b-b7b0-9deea602fa2a | -3.22796 | -46.93749 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5ce99da7-f6ea-3263-ad4d-4d23ccc24ed8 | -6.90125 | -43.69081 | 2026-09-30 04:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7012d55-4bfe-3f05-8d71-e28213c4d698 | -3.15345 | -54.08188 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README28.md)
