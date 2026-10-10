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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0a1d4a0-1e45-3f15-8d58-a933adb5729c | -3.10884 | -53.78027 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d45b2491-3fd6-3045-8571-b59bdd54975a | -1.36023 | -48.47919 | 2026-10-10 04:44:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6b117a5-2522-3721-9042-baf105c67715 | -7.23895 | -44.17812 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3226d1dd-56ee-3f8b-8d69-04d69333e10b | -3.31008 | -53.69753 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c98a1ad4-9b20-3147-aace-3f5dc6fc5202 | -5.74838 | -45.1298 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cd2d7e75-8f8f-3092-8657-837d88b9a36c | -2.82992 | -54.81398 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f40b63ba-2077-3f51-889e-4b20418f61dd | -3.0145 | -51.01258 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2587b0ce-7424-3fe3-bb4d-04593a72c8d9 | -7.25051 | -43.70511 | 2026-10-10 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db4e4c43-fe74-3be3-8de6-fe95619f049d | -3.98817 | -54.46293 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 171a3eab-a345-33c8-8014-428cd1e3d39d | -3.12679 | -54.17531 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f7803245-43a0-3fb1-891b-628bb33782cb | -6.93414 | -44.57014 | 2026-10-10 04:44:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c982a66-5793-30e3-83b6-0b260d4e2d24 | -4.51182 | -54.89686 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99e45ed0-6605-3e33-938c-a8c2cb82c12f | -3.98515 | -54.45195 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 935bdb1a-9959-3a38-a00e-078839209d06 | -4.59448 | -55.72692 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 95dba62f-8c48-3878-8fea-3a75bca2b401 | -3.37091 | -59.38977 | 2026-10-10 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12d17e38-1318-395e-a3e5-8e81868bb396 | -3.55407 | -54.68834 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d04649e0-6316-32ee-8caf-e4621c00390e | -4.10366 | -54.02172 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76fdf414-56a2-36a2-b6a5-111eb68d1a5b | -5.59537 | -47.27547 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3fde347-20b2-3ad1-b5b3-715055f59c96 | -5.87674 | -43.40981 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dba9c69-28c4-3849-a1d2-988dabdec863 | -3.15362 | -50.58986 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4b48c16-d356-3342-b9d2-9f1bdb157e95 | -4.68905 | -48.51979 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32f2dca9-e2c2-3cae-b630-022643cf8da8 | -3.16979 | -50.44577 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97b4f8b9-5829-3f61-85c3-9185c3f504c8 | -2.79421 | -51.40765 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4e03cbda-3c62-3754-9e69-6704b2b414eb | -3.92911 | -55.72466 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7f1b7c3-8093-33c3-b6da-b25db600b66c | -2.48776 | -46.00271 | 2026-10-10 04:44:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 217519e1-62c6-3536-92d3-96916c996b55 | -4.28148 | -48.57629 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d610d4c-ea6d-3d45-8745-49caf04bdabe | -3.01736 | -54.13006 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7ea99c5-b52e-3778-9db6-690bb43c2751 | -5.88373 | -43.41568 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| defca35c-6f7e-33f5-9c75-96f3c457a5a6 | -3.98429 | -54.45713 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47eb62c1-ee7c-352f-b718-a00d1a6bebf6 | -2.07018 | -48.1451 | 2026-10-10 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a91561c-a385-3f03-9b0d-dd97981b75d7 | -7.24405 | -44.16971 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0d6bf5bc-2568-36b9-a62d-0af26f7c8354 | -4.40485 | -49.78186 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c067c575-f0bb-358b-8865-f329f90edcc0 | -3.15157 | -50.59137 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb6c442b-b7f0-380b-ab43-eef5a1bbbf0f | -3.87369 | -55.98803 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28b8f026-166d-301e-a77a-3c26f8d843d2 | -2.39149 | -51.29973 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a917250-6cd9-3cfa-af91-c69a4fd1be1b | -2.81915 | -51.95655 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c90942e-1a11-384c-b635-db995a8a8767 | -5.92871 | -51.82064 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0f3e3a1-e97b-3a68-83bc-1823b4213ebc | -3.97953 | -54.45666 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2ed34985-3f41-3dfa-975c-197fb2c06f1a | -3.59959 | -54.59464 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bf6e3168-f4d5-3def-99fa-02a0c6beff10 | -3.21632 | -50.55516 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f2ea278-d922-3656-817c-c797308260d4 | -4.27766 | -55.42576 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aca2b05b-5cff-3e86-af68-83f926499797 | -5.59705 | -47.28639 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd1c1d91-1194-3f89-82fd-70e6ca5e0669 | -3.56546 | -54.67957 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83b45843-8ae1-3464-8f8f-cd2431787634 | -1.64363 | -54.39925 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 64a1fe89-e6cc-3c06-88c3-2a9a09849434 | -3.10113 | -50.31791 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33eaf98e-9be4-367b-901a-853780f0b55e | -3.80543 | -49.93718 | 2026-10-10 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd52b36b-902e-352b-be78-46719ad392c2 | -2.53111 | -56.27285 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92e39beb-706b-37b6-b774-ee20d5d9dcf1 | -4.09928 | -53.99251 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 265eedee-d1bf-342a-9f33-4cb35cbf54f8 | -3.22728 | -49.43423 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 3a4f1fe9-f8bb-3835-befc-7bcbf55893a3 | -3.0387 | -53.89528 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b3154fe6-ace9-35d4-a4b3-2a86f761bc87 | -6.73025 | -46.45541 | 2026-10-10 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8f7e1f6-d7d3-3888-812c-4027f8c77479 | -4.81742 | -56.08289 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efba7518-5151-384d-ab71-86dc0be1fcdf | -4.4026 | -49.77349 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b7ff483c-0477-3adb-a41a-03bda82b2092 | -3.57692 | -54.37633 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| ea3d4aa1-ece2-36ce-9d18-a99feb2bb9d8 | -4.08867 | -53.99784 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc325d7c-e737-38d5-a843-675928f6115b | 0.20219 | -51.06908 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 450301f9-80e6-32c3-9808-703b4a5823da | -7.22516 | -40.35044 | 2026-10-10 04:44:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 97f09a29-8bf1-3f1b-ae21-be5da0a88d1e | -1.33078 | -55.4487 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db029a75-7af8-35df-9065-700b1246b56e | -3.90006 | -55.89321 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ea96153-ee21-35bd-8cc8-c8ba2b3f44c3 | 1.67292 | -55.62012 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8c9466a-4fc2-33ec-bd6e-f0901eff7943 | -4.43352 | -47.53927 | 2026-10-10 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| bd1d52cd-2b38-373a-b206-2b77b109c2c9 | -3.22251 | -49.44142 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9eb93fd4-6ffc-3b72-844f-63db2fae75be | -5.70359 | -53.47624 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cfc8aa4-a3ba-3bae-bdb8-61305579ff33 | -2.52685 | -56.26498 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ed9f55a-fd52-3f2b-9963-fb44915730b6 | -6.8749 | -45.03657 | 2026-10-10 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd43259e-3351-349c-a2ba-b52f15978c12 | 0.81853 | -50.76783 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5b45776-098c-3764-b296-dddab8b7b8c7 | -3.89337 | -52.1915 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7adda14-7586-3c87-98c6-e69daaeabe28 | -6.20837 | -46.64626 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d984785-bdd1-3a5e-8ca0-4ce630dbe227 | -3.00839 | -51.00212 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 783afb41-5cd0-3bab-a0b7-9dc6d828f3e5 | -1.21751 | -55.65372 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7402847-83b3-311f-b129-61b761d7b32b | -5.23467 | -45.37323 | 2026-10-10 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8131d71-3929-3d01-98ea-522a3639b299 | -6.71399 | -46.33469 | 2026-10-10 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d0da9eb-6247-36e7-b1ea-0a88ee6eb51e | -5.04462 | -49.34726 | 2026-10-10 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a85bc3e-b556-3a41-a2ba-f2a0243491be | -5.78591 | -53.80612 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59fa20ef-2c41-38f6-9f07-7334d15afdad | -2.45409 | -57.89165 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1fc0ea0-9e44-38b6-834f-16b31052117d | 1.00248 | -51.09635 | 2026-10-10 04:44:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 662d2e32-3bb0-3eef-98cf-e7003e2037ad | -6.50016 | -44.36749 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad2dd1f9-3400-31d4-9bb1-021f79a1faa5 | -3.58117 | -54.70379 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4abac70d-41b9-3905-81f3-ac8ae8f9ba94 | -3.56634 | -54.67445 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74fd81b5-7a0a-3e8b-b455-1f770343a775 | -5.14861 | -45.76773 | 2026-10-10 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9085e9d-32cb-3f73-8388-b54192ff7a7b | -4.02881 | -46.98232 | 2026-10-10 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b0dd59c-e675-3b9d-a97e-fc5f8c725f10 | -3.10258 | -53.96161 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84bb95ed-4f24-3772-801d-1e5c3ed7cd72 | -3.33052 | -50.78275 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8799fc3f-0401-3c89-98c6-3098908c3ce9 | -3.5475 | -54.69777 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5b80df7-48e2-3501-a276-4f193f4dced7 | -5.37266 | -55.88249 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40e67861-dc33-3be6-95c4-dfe71452420a | -1.27554 | -55.75407 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fce6004-663f-39df-802d-60c373c956ca | -7.3692 | -44.0523 | 2026-10-10 04:44:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9729d67-9f2d-373e-9ee4-3239f68d34a4 | -4.55731 | -54.97975 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c53567eb-d9c8-33cd-aeb0-85d30412db49 | -3.94265 | -56.05389 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c539203c-b7c5-3a9b-901e-22bf85069e92 | -1.18952 | -54.21145 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec1cc086-1101-3169-b7d9-3a47bed533ba | -6.1295 | -43.53718 | 2026-10-10 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c42991ff-a493-3ed5-916b-d0086294200d | -4.18162 | -55.68943 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e8af859-570e-3274-9ce4-97cd81151f1a | -3.89951 | -55.89639 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8826aef8-8070-3ffc-84b0-dbc892810f74 | -3.24565 | -54.02491 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 425c58ad-497c-35ac-97d3-588acdf04950 | -7.2253 | -44.16677 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98c586ee-89c5-382e-8c4b-0924b512bb9d | -3.18544 | -50.58154 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54b9e631-cdab-33ca-82e0-95fdea254a4e | -2.5704 | -48.24878 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba5d910f-5fca-33ae-b773-235f55d4fc5e | -2.45565 | -58.03363 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92acaa11-6568-3372-9f72-9e4108230127 | -3.95058 | -55.33566 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90c40c61-0d6d-3b0b-bb8a-2822ff5f5a6f | -3.57726 | -54.69764 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README64.md)
