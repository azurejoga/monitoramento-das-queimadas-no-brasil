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

## Dados Diários - Página 284

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29cace1d-a75a-3144-9e94-f3a1293182b3 | -1.56224 | -48.22448 | 2026-10-08 16:20:00 | NPP-375 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 535be849-25e2-3b6a-a997-6832156b532a | -3.30415 | -49.12403 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0b26e640-d4de-39c6-a1a6-a5a0d668e191 | -4.3741 | -41.82853 | 2026-10-08 16:20:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 1324cbd4-ceb0-37cd-bfc3-8cfff5ed35a0 | -6.79981 | -45.05437 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ae050b7f-1e41-30e2-9931-622c8c8796a3 | -5.28441 | -42.74128 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| f25a8bdc-ce20-38f1-892e-1d25a528ff85 | -7.57123 | -46.68608 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20daed72-4f70-36d6-b510-37b0317c7e77 | -5.38962 | -44.18259 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1de635a0-93df-325b-aa37-55cd355d803c | -3.63254 | -44.80925 | 2026-10-08 16:20:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1773bd61-41bf-3348-9ab6-d9daf2f4ee7d | -3.73905 | -45.07734 | 2026-10-08 16:20:00 | NPP-375 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ccdbc3e-6a3b-3ce2-8cb6-a6c34414acda | -5.09344 | -37.50695 | 2026-10-08 16:20:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f5e97c6d-6886-3d41-a22a-c7005098b86b | -7.76326 | -44.17664 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a9079494-045f-3f63-bf7e-ba69d7f8969f | -5.39034 | -44.1876 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9af814d1-a6f6-3139-83a6-f88e594620fd | -2.87902 | -40.40793 | 2026-10-08 16:20:00 | NPP-375 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4198ce32-a7a5-3f69-b0fc-f45ab1e10d38 | -6.70385 | -45.28144 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0addaa83-97e1-3ad8-a7fc-8784c50c108a | -7.19004 | -44.33084 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 549f3004-5057-3e35-861f-df293326e401 | -3.43983 | -45.09642 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 986a95a7-46ed-38e6-8031-16574f022f4a | -6.1329 | -47.94213 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f66e23f9-02e0-32d9-984a-175e7f17bc49 | -3.2661 | -54.02135 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 19aa02c2-ae16-3ffc-bb8d-b0c46fc23e71 | -5.85493 | -53.46518 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f9677e20-a6e5-3cf5-8aae-c215ceeb537d | -5.7089 | -53.49232 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 71c1c0f5-f794-3ceb-9eea-2bdc4d40cc24 | -6.7919 | -45.05978 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| b7985eef-0ccf-39e3-bca4-055a892cdde4 | -6.97588 | -45.11792 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 04527b0f-4eed-31c1-9e32-080abfcd46bc | -3.25913 | -41.63156 | 2026-10-08 16:20:00 | NPP-375 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f84fda88-51aa-3c03-bebb-d5e2e723e48f | -6.59851 | -37.88885 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 375eb26c-e4c9-3d99-ac37-5d7b8a925aa4 | -3.0081 | -54.06608 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| da62b52f-67c4-3a52-82c1-cc50c4c10d9f | -3.77186 | -44.35899 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b4136cf6-39cf-3d14-9891-c1427f348133 | -6.03208 | -45.09755 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76fa5bfb-56d5-312b-9d40-095f09bd0e33 | -6.99275 | -43.21186 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2c4a7854-1602-331d-97a4-3a0c0eeba269 | -5.27889 | -45.73265 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 281483d7-96a5-3f98-9894-b217d2093bf4 | -6.99824 | -43.97517 | 2026-10-08 16:20:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0bd2d722-f92d-3cd6-a9fb-07c619d21eef | -6.93272 | -45.256 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9a2bfd4f-3749-39c1-a716-3db30f7f3e51 | -5.01779 | -42.44425 | 2026-10-08 16:20:00 | NPP-375 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 49be7c81-0ccf-3a67-8aa2-d1175b988422 | -2.08811 | -46.5673 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| fbfbdb7d-0317-3ebb-b62e-b021b25242c5 | -6.22589 | -52.88112 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d7bd63be-edbf-3940-87ea-dd9a63be2d5a | -6.67631 | -45.33599 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 70f3ea0d-76cb-3c2d-adda-bb27146ea048 | -6.92883 | -43.06441 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 80379a25-e51d-3748-baac-1af1664fc901 | -6.11117 | -38.168 | 2026-10-08 16:20:00 | NPP-375 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 780143f3-08fe-334f-a410-4a24e0d799a4 | -6.88685 | -43.69616 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.8 |
| ed3055cb-1eb2-323d-8da5-424d39864d50 | -5.32721 | -35.55893 | 2026-10-08 16:20:00 | NPP-375 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a5823dcc-9e5e-3fa9-bff7-302e779e0360 | -7.26813 | -45.34808 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 493eb5c3-425b-38da-8743-717848a9c2ff | -5.92696 | -51.82216 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 65b8ef5f-a07e-3ed3-9669-fc391cee754d | -3.87578 | -42.83784 | 2026-10-08 16:20:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0744d11f-1546-3eab-a2f8-4a73554924bc | -7.19277 | -44.26334 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| e8d2c74d-ea28-3308-ac23-c9fd7cd182cf | -2.3871 | -45.99852 | 2026-10-08 16:20:00 | NPP-375 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51d8e3b7-d4fe-3f34-9882-97e9749bf639 | -6.07149 | -45.30658 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27e8db07-4853-3d0a-aa4b-3dd53c083c4c | -3.25774 | -54.01962 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 49759005-72df-30db-99fc-3f442cc295b7 | -7.19235 | -44.28914 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b21f9ff3-315c-3b99-9c54-1a2961738107 | -6.22653 | -35.34094 | 2026-10-08 16:20:00 | NPP-375 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 739d7eff-4260-3739-8a0f-805b0a7039e4 | -6.33308 | -46.9426 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3c82c17d-a24b-3c1c-9170-1bdc4998b7fc | -2.07679 | -46.58213 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 267.9 |
| 36233ba1-b647-32f5-b25e-17a7e4df3d74 | -7.57362 | -45.19767 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cb1c05a-5048-39b7-af0b-81d139d5ca49 | -5.71365 | -41.74591 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e3d4033a-c75c-38e0-a055-a1c520b8f9a8 | -5.42886 | -45.62405 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e1da798c-f399-33dc-8162-376d653ac2c7 | -3.78976 | -41.65509 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3aa710a1-ec03-3211-b586-367fac379a42 | -5.26815 | -47.92368 | 2026-10-08 16:20:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2da58690-ae40-37a3-869b-eae69393c906 | -4.0099 | -41.77303 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| f0e82498-abbf-3bd9-8ea2-9f7aca6e9d1b | -5.37109 | -44.1877 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| eb25dfeb-0456-38ee-b649-d906817d1f76 | -5.38058 | -45.94076 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0442a1f8-a40c-309c-b813-bed1206f9472 | -6.20221 | -51.432 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 02686da8-6ebc-3bcd-91ad-bd51cd0415ea | -3.02322 | -54.05556 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 45ac7bf8-0a40-38d3-8f38-c6db3f643536 | -3.2849 | -50.09275 | 2026-10-08 16:20:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 78a36ee5-5e61-32b3-b29b-800da79e248c | -3.00195 | -54.07443 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 91de224d-538e-335a-8a34-3725287b3820 | -6.9384 | -41.94787 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a3af6655-7afd-388c-8a8d-5c7dd82acb15 | -4.57278 | -38.94905 | 2026-10-08 16:20:00 | NPP-375 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 44eed898-c972-3974-9b8e-ab756990a92a | -3.94129 | -41.55022 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 252c76c3-6638-33db-9d77-3ae60cd95f7f | -3.24196 | -44.37148 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 974ca128-111c-3bca-9469-8d744f1f8898 | -6.83539 | -39.54942 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b89cbc0c-75b3-3f9f-aa2a-7d3906f41f07 | -6.6995 | -45.28192 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3fa4b5b4-c839-3a38-b7fa-58c13f620062 | -6.95571 | -43.73378 | 2026-10-08 16:20:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9738c3cf-2a1f-380d-bb9a-d255262d0a33 | -5.37596 | -44.19986 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| d34c54a6-cc78-32a6-91d7-75a53516e6c3 | -7.40462 | -44.74786 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1e81a2e0-6005-3697-a98e-846955c687b6 | -7.70576 | -45.43587 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f3a07af-9614-3bf5-a9b1-0a0774547673 | -5.82021 | -42.48814 | 2026-10-08 16:20:00 | NPP-375 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 04df9777-18c1-3271-b85b-3bf0cefe3453 | -6.11576 | -51.95704 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a6c1eb6d-04da-3afb-8fb2-e1bfa1f1d0cb | -7.92327 | -46.80709 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0ee18a4b-30b9-30fa-a30c-62725ecff394 | -6.97292 | -47.67448 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 4ee622cb-09a7-3d60-8cb6-67320414d3f9 | -3.49 | -39.4983 | 2026-10-08 16:20:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 66c65dd1-8c3b-30b9-997f-d009ca4bb238 | -5.73879 | -42.05998 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| dda54f2f-1122-3959-ba5d-c8a72e12b2b0 | -5.39451 | -45.91216 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bb139141-ac8e-3e79-ab3e-8d2d9e7793d7 | -3.73186 | -39.53093 | 2026-10-08 16:20:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 925e5c62-ef88-3293-bf02-1b192eeffa45 | -5.77817 | -42.05818 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 163a2578-df68-318a-8522-0c6d07e76ee9 | -6.33777 | -44.44629 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1bd51381-1700-35e3-834e-39215f4c46bd | -6.33223 | -43.35163 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| aad59591-6384-3b19-984d-3c00b4617a76 | -6.61772 | -37.90094 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 16.1 |
| ddeb9711-dab5-3471-bc96-4878dcbed3af | -5.96267 | -46.15633 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04e5b945-f510-3a0e-9b7a-df19d362bf7a | -5.94451 | -45.69625 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82c8b655-01b4-3787-bd7b-1d88c2b0fada | -3.59906 | -44.35238 | 2026-10-08 16:20:00 | NPP-375 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 45e56878-9d50-3a3d-a447-b131a9cc7f76 | -7.27688 | -44.18875 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76a6c245-8442-3a65-a65f-07f379e865f2 | -1.88017 | -46.701 | 2026-10-08 16:20:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 070c983c-e438-3bcf-b5ec-3df43506a927 | -5.7045 | -53.45856 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 93ea2c9e-f517-32f3-b9c0-731f72610a29 | -5.29952 | -45.72094 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c14d3a9d-8aa4-36b8-b09d-625d2e8ad824 | -3.90143 | -44.12804 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a18a8413-8ca7-33bb-8761-704b16c979fc | -3.00895 | -43.11176 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d7937cf-1082-3430-9462-df8b42ebc005 | -5.77463 | -43.33085 | 2026-10-08 16:20:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 547e27b7-87dc-3caf-b577-5b879f731ded | -5.35004 | -45.73106 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47f13f3d-a4aa-37fb-a689-2929838bfb1f | -7.01902 | -45.29581 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f25eade2-c9b4-3d74-8b89-0108db3e96de | -5.67584 | -42.59678 | 2026-10-08 16:20:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d6da671f-66d1-3e60-9da2-6b7311d820d5 | -5.38294 | -44.18605 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 21e3d711-d8a1-3270-9a25-1b33ef29515e | -8.34665 | -47.66632 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 44153b2e-af77-36e1-8190-afd63adef97b | -7.46478 | -42.82984 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |


[Clique aqui para ver as próximas entradas](README285.md)
