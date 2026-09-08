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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b5bdd02-3099-30ad-acc5-5d08106cf65c | -4.93931 | -45.66999 | 2026-09-08 05:04:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ffc8a11-202c-3613-87b7-1e1b080b2c59 | -2.56281 | -54.74479 | 2026-09-08 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dea1f3f0-0b7e-39f1-bc56-a83eb317d74a | -3.79038 | -55.87798 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c961be5-c4b2-36ab-b45c-e943902ad6b1 | -3.88762 | -55.82082 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63d063cc-a373-3c40-8658-503cad37e132 | -4.16703 | -55.84914 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 63b91e8c-c12a-36ca-a685-6e81b2d60a38 | -2.55946 | -54.74425 | 2026-09-08 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 898615b5-3a4e-3f92-ac2a-39330749ffc5 | -4.27573 | -48.66076 | 2026-09-08 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6515ffc-627b-3ff4-93b9-f0279381f4bc | -3.37916 | -59.4293 | 2026-09-08 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 190bf0a1-a262-386f-b088-64e9575249cf | -7.06615 | -56.46497 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60005d72-e6c9-33cc-8742-0fc06f2280af | -5.16326 | -55.95507 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68a3d88f-022e-390c-b7db-99204d666496 | -4.04898 | -50.87623 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d27fb3fd-3794-31f3-aca5-1325a8e22a92 | -9.76101 | -43.48006 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5fc1135-49bd-3e85-b44a-fee68c46cb99 | -5.94005 | -51.69987 | 2026-09-08 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 049d77bb-0107-3c13-8f59-0a90b66bced6 | -3.15891 | -58.65482 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe91f2ef-446f-3525-a882-06c8a9b5800b | -3.45709 | -59.5085 | 2026-09-08 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| edb6b373-27d9-3552-9caa-6bc826be660a | -7.75942 | -49.98049 | 2026-09-08 05:04:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31c090a6-fdb2-3f13-b8d7-dc1ecd2d6a5e | -3.55194 | -48.17871 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| f4c4a040-eba3-353a-a04e-79d38dbbe05d | -3.79322 | -55.88228 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 444a84f7-449e-30d7-af6b-40848b033be4 | -4.6683 | -55.6298 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1039f7-25c6-3623-affb-c2ff7d135091 | -6.63417 | -59.43874 | 2026-09-08 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 12ef6b45-e37c-37aa-8e41-2cd181a3e2b9 | -9.7165 | -43.40153 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 61f8d381-ef6d-3293-af16-c6457dc0f36b | -9.70876 | -43.4381 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9143928e-accf-3c99-913c-8ec5495eda8d | -6.53208 | -58.50948 | 2026-09-08 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9649198-f892-3f04-ae9e-b36262896829 | -5.1655 | -55.96299 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f45b1e79-8660-33c7-ac4a-2969e27d5b21 | -5.98895 | -53.72844 | 2026-09-08 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc4300a1-660d-3d14-8106-aff96b1462cf | -9.76165 | -43.47503 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fb9dd486-d1f0-38fc-8d27-6c47af004ce5 | -9.70569 | -43.46315 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cee5de8d-3ff9-33da-a0d3-53765bf9fcef | -3.55279 | -54.69471 | 2026-09-08 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24f4e5dd-c4a7-3f96-855d-2b8d5c19cdd2 | -7.40122 | -56.01953 | 2026-09-08 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81c3901d-e10f-377c-9bfe-2efa7e34fd33 | -3.85583 | -51.37965 | 2026-09-08 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad088b3a-07ad-30fc-9a4c-7c7d8285f782 | -6.78398 | -48.66728 | 2026-09-08 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14f91b6b-2137-35ae-ac80-76d74c24a7ae | -5.36652 | -56.02167 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bec83da-de58-3de2-a5e2-997db385e257 | -3.70103 | -58.93617 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b21058a1-796e-3bf6-be52-535154f943c6 | -11.36498 | -45.73917 | 2026-09-08 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be4b83f8-a400-3abe-874c-dc5a93a0e3d0 | -3.54299 | -48.18117 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 812c3d0c-3162-351c-a4ea-ae5c9ea7ba1c | -4.35002 | -47.58609 | 2026-09-08 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3daf5e0b-4bd2-36f8-b653-669eb0c1142b | -9.76486 | -43.44963 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c97b8f3d-940a-306c-97b2-31c59a064c98 | -5.36711 | -56.01798 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d9b529e-fcb2-3ec7-b9ec-02f250da9de6 | -5.36428 | -56.01374 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91d39e05-64b2-3696-89e1-ecdb54dc91ff | -9.75975 | -43.49001 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac59459c-c551-3630-bf80-660aab5ca081 | -9.71067 | -43.42252 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e069b85c-527c-318d-afa7-f83924f25b26 | -5.15926 | -55.95821 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f23b6eb-ee38-3687-a216-6a7ef23b244a | -6.01193 | -45.81403 | 2026-09-08 05:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ee9cbd3-0a10-3342-85f4-39df6c6ee60f | -4.42985 | -55.09987 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e2227dd-2499-3e13-ad6d-a128e373113a | -9.70806 | -43.46656 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cb7f9272-8825-321e-9c1c-e7ff76d1f017 | -4.78315 | -44.40237 | 2026-09-08 05:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c75ebf99-51bd-380f-9e3b-5457bfd380e7 | -2.66689 | -56.46316 | 2026-09-08 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d488f89d-a62f-322c-a0af-c340e0b8130c | -9.72964 | -43.47584 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5d72b7a-e4e0-378b-a4a2-a04f239e7c31 | -3.5828 | -56.8718 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 338416d3-03b4-3cb5-8691-6cb5b12ce1f1 | -9.70941 | -43.43279 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3d1c3d31-6441-3055-9a46-776530a8b285 | -4.66772 | -55.63345 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d58b343-c1b8-3e38-9c32-f93394502343 | -4.54167 | -54.93003 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9ffd26b-d8b6-3cc2-915c-92a540eade8d | -6.64726 | -51.49292 | 2026-09-08 05:04:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7c91a16-d06b-3d23-b574-76a775329f77 | -3.06198 | -59.27506 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b678596-ff48-3408-9abd-5fd4aa2ba90f | -6.56558 | -58.98058 | 2026-09-08 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 785014f1-a869-352d-ad3c-062e31ef8b09 | -3.7614 | -59.42558 | 2026-09-08 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4fdceb0-5430-3039-a6f5-02cbbe19abee | -3.55076 | -48.18628 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0e11809d-6cc7-35b0-8703-1a14347cbb31 | -3.45645 | -59.51242 | 2026-09-08 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d7a1bcf1-4be4-31c6-9a0b-6a144e114ff0 | -3.65126 | -49.40136 | 2026-09-08 05:04:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 519a37d5-9483-3d1b-a467-c42535253152 | -5.1832 | -59.76384 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dd713d6-a285-3f10-b6bc-ab6d99cf69c7 | -3.78013 | -51.353 | 2026-09-08 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d30141e-8f0a-3e55-810f-c1397c5a2b61 | -3.63166 | -54.75361 | 2026-09-08 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd1fe9ff-c66c-3329-96fe-2753bb09b04c | -4.1696 | -50.0853 | 2026-09-08 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26631ba7-7797-322d-83c1-81defc25ed5d | -4.57377 | -47.18124 | 2026-09-08 05:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30538eaa-1b6e-3022-95c9-a6fde7a87f4e | -4.53326 | -55.61999 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25aea995-84f2-30cb-8c0f-a4e44e652f40 | -4.04602 | -50.87163 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed808b44-0a0c-38bb-9d95-6cc30313ab43 | -5.37027 | -50.56621 | 2026-09-08 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88593f87-e331-343c-b08a-d03c587493a9 | -2.98672 | -54.0252 | 2026-09-08 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6bcd75e-7c99-3984-94f4-2e4239d880d2 | -4.07698 | -48.95441 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06aa9fe2-28c0-3fdf-83ff-fe76e7f39526 | -8.51452 | -63.84767 | 2026-09-08 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d5c410e-d2d5-332d-965b-0d767b9034d0 | -3.05779 | -59.27434 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a85024d9-569b-3420-bcbd-44227536614a | -9.71523 | -43.41135 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bae796bf-42af-3998-8f6b-3091ae6eafd2 | -4.34116 | -47.58503 | 2026-09-08 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c2424d7-1c73-37d8-81bf-ab3fd53cb487 | -6.63758 | -59.44301 | 2026-09-08 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b01bba60-8f9e-3de9-a08f-401918cf4568 | -3.89046 | -55.82505 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b320b64-0e57-3d93-be41-9bd3ed9c9789 | -9.7125 | -43.4076 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2f90fb01-65ad-3e1d-b69e-b9e79d088ec4 | -9.76038 | -43.48504 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a38d24f4-2002-35af-9259-8e94096878c0 | -3.23806 | -50.60249 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c1aeca0-ed8e-38e2-b217-eb01713241ca | -6.76551 | -45.48316 | 2026-09-08 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1099de1b-864d-341f-af26-98a811e73528 | -9.75912 | -43.495 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeabf916-4dc1-3868-97f6-f46e8e630171 | -4.66491 | -55.62921 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76354ba9-85e4-3b52-90d9-e04be37da0e9 | -3.54241 | -48.18498 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 61ed0f56-d6d1-3c5a-a29f-35347bd51aa5 | -7.93144 | -49.73841 | 2026-09-08 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad5b3f1e-42ae-3a23-a43f-931695e92e22 | -9.71005 | -43.42757 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 31b69e10-2c11-3aaa-86e4-bed37aaaab30 | -4.34066 | -55.22783 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5287131f-7ab0-397a-bcab-b3cf8bb5035e | -4.34344 | -55.23193 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57c91c3c-1b15-344d-86c3-b0677024b852 | -5.37216 | -56.03017 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46d21a8f-3274-3238-b22e-9e8a51db4673 | -13.27094 | -61.78302 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e52711d8-e064-373a-89d5-318af26611cf | -11.93827 | -49.7458 | 2026-09-08 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa313610-ee4e-34b9-aab5-179716e77886 | -13.42692 | -43.8157 | 2026-09-08 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4e0dc64-1712-3b39-9394-0ac04ff627c9 | -13.27183 | -61.14935 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa68779f-554f-3f38-9c6b-4654726f6694 | -13.42611 | -43.81435 | 2026-09-08 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c275012-b3fa-371e-b4c7-cf90a1256755 | -13.26215 | -61.71231 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78d67607-2f61-3b31-813f-03d4de0e2e73 | -15.64113 | -54.17887 | 2026-09-08 05:06:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e64b14f9-865e-39ce-90b2-6af4a0724bb8 | -13.21793 | -61.71398 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c238f1c4-9c5e-3240-a9c1-039557955a81 | -13.27379 | -61.76726 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b03628a-e312-331e-bbd0-f8b73adc061d | -13.27655 | -61.77595 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6aa61449-0603-37a0-be86-f79f5d51f7c2 | -10.77559 | -60.78814 | 2026-09-08 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2979bcb-8e4c-3eac-a8b4-bf2ce79a48fd | -15.83812 | -56.60653 | 2026-09-08 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f6aa31-a76b-3bf9-b26c-f1d72dc907f0 | -13.48394 | -60.92786 | 2026-09-08 05:06:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
