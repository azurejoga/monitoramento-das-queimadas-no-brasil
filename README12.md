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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c735f2d-2172-3d28-9261-fedaf9708288 | -8.8052 | -44.831699 | 2024-10-02 00:31:41 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6115827e-ea14-3c74-a5dd-3a2071a3217a | -8.3135 | -42.8139 | 2024-10-02 00:31:42 | METOP-B | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4e1223ef-e591-332b-a8de-3b49f9c81fac | -8.7001 | -45.227001 | 2024-10-02 00:31:44 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 036e977b-fba9-3b71-962e-d5804b0e6217 | -7.1624 | -38.901699 | 2024-10-02 00:31:45 | METOP-B | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0d820e6d-7ff2-3ec8-889e-0552e1dff7a0 | -7.1668 | -38.919701 | 2024-10-02 00:31:45 | METOP-B | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3216c648-efa3-3dd2-a1c1-5e31dbcfb59e | -8.137 | -42.8964 | 2024-10-02 00:31:45 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 35e7e198-7135-31ab-a576-6c649aab2244 | -8.1393 | -42.905998 | 2024-10-02 00:31:45 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fad11f14-bed6-3dd6-80bd-d90f906d6035 | -8.6904 | -45.229198 | 2024-10-02 00:31:45 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 935cef84-25fa-3477-b6c2-587755c60658 | -8.6806 | -45.231499 | 2024-10-02 00:31:45 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d73920f8-99ed-3d72-b545-bf359d48eebe | -8.6823 | -45.238899 | 2024-10-02 00:31:45 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4fdc6daf-dd44-373d-9800-f2eb52fe2a58 | -8.5216 | -44.719898 | 2024-10-02 00:31:45 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 175b8ae8-016f-33f9-a08f-d6d575f93e87 | -8.0694 | -42.872002 | 2024-10-02 00:31:46 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d33d786-d987-3495-bd67-fe9259c9c522 | -8.1616 | -43.659599 | 2024-10-02 00:31:47 | METOP-B | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d21a1393-30a9-3b57-891e-b63f4b26d3eb | -8.1637 | -43.668301 | 2024-10-02 00:31:47 | METOP-B | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc590cce-dedb-3afe-9714-c2a34d99e1ba | -8.156 | -43.679298 | 2024-10-02 00:31:47 | METOP-B | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b33a323e-9e88-3eb6-b723-05117456993a | -9.604 | -50.083801 | 2024-10-02 00:31:47 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a45df1a-6947-3dc4-ae0a-614a4b45c5dc | -9.5924 | -50.077599 | 2024-10-02 00:31:47 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59f52623-929d-368c-af52-77707e3594a6 | -9.3162 | -48.896999 | 2024-10-02 00:31:48 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32efe91c-238d-3767-9dce-c778947d28c4 | -7.0555 | -39.135502 | 2024-10-02 00:31:48 | METOP-B | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| def2ae63-3188-3ee5-8829-65374bc61630 | -9.5782 | -50.106899 | 2024-10-02 00:31:48 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 193c8308-d48c-3070-bc5c-b1269d8de637 | -9.5926 | -50.174198 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b68be691-7905-3d24-9f3d-4abb178f01b6 | -9.5944 | -50.182598 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 293bf5f6-fafa-3a13-9320-1032e0fa0a6a | -9.5962 | -50.191101 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01c4d328-fd07-377a-ad26-49bf161996f1 | -9.5828 | -50.1763 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fac1bd0d-c47d-3ac8-8def-2f2a71be3df5 | -9.5846 | -50.184799 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6d9aa1-2745-34c3-a3fa-3d2fd9f57880 | -9.5864 | -50.193199 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d950fb5-be56-377c-8665-146b1c699be2 | -9.573 | -50.178398 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a54f42a2-9be0-32d0-9ca7-05359fbc0260 | -9.5785 | -50.2038 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 527572db-e58e-3003-9146-9f11f6008898 | -9.5687 | -50.205898 | 2024-10-02 00:31:48 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d11dac13-5278-3a6b-b99e-665678fd897c | -8.8109 | -46.803902 | 2024-10-02 00:31:48 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d47f3604-cbe5-3515-8a6c-2e15edb54047 | -8.8125 | -46.810799 | 2024-10-02 00:31:48 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9cd9ae-33cc-3d00-a2d0-129515ebff4c | -8.2273 | -44.340199 | 2024-10-02 00:31:49 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6477de67-f9f0-3fbc-bae7-9bdf9a564e33 | -8.2292 | -44.348202 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 838440a3-c8d7-3ee0-a20d-100f5e466580 | -8.2194 | -44.350498 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1daca8c8-aac8-398e-a8ac-baa0279c768e | -8.2213 | -44.358501 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 573a8f50-5e2b-3600-aa8c-b3d7a01a6af5 | -8.2078 | -44.3447 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a0b5ef65-4a60-3cbb-bcda-8010802aa141 | -8.2097 | -44.352699 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33fe37c9-4738-32d9-8a85-4ef44130b404 | -8.198 | -44.347 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1dbe10-4a4c-3fa2-8c67-5b81d57b6d46 | -8.1999 | -44.355 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e5ebff69-369d-3197-a3f8-c42d3e79dff8 | -8.2018 | -44.363098 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ce4bee20-c8d4-3072-9650-090ee74e4ce0 | -8.1901 | -44.3573 | 2024-10-02 00:31:49 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4b996b4d-7f57-3639-a2d8-88512ab05b21 | -8.7506 | -46.810299 | 2024-10-02 00:31:49 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 418ad94e-eb6c-3789-ace5-1dc4308bcb99 | -8.7521 | -46.8172 | 2024-10-02 00:31:49 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80c96b6a-6780-30f0-838d-9a55122e8b38 | -7.8491 | -43.075001 | 2024-10-02 00:31:50 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db9cc673-036d-316a-abb9-1c76d76b0cc7 | -7.8513 | -43.0844 | 2024-10-02 00:31:50 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d3d2406-b02b-3a33-864e-caff99254005 | -7.8371 | -43.067902 | 2024-10-02 00:31:50 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83b35672-1b32-3843-852c-c71982787621 | -7.8393 | -43.077301 | 2024-10-02 00:31:50 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f37aa18-bdf1-3d03-8174-07d1ac40dd54 | -7.8415 | -43.0867 | 2024-10-02 00:31:50 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7dd3ca68-da75-3f7c-8743-3711c3884276 | -7.8274 | -43.070202 | 2024-10-02 00:31:50 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1cf4d27e-3814-333d-9e91-154b64321121 | -7.8296 | -43.079601 | 2024-10-02 00:31:50 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b093b1ed-4a14-35b8-af0a-6a0dbb17371f | -9.1695 | -48.7435 | 2024-10-02 00:31:50 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 31cf10d7-5f37-3b4a-a6f0-480995da2e28 | -9.1711 | -48.7509 | 2024-10-02 00:31:50 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7466f42e-1943-324e-ac69-8c929ad22cd9 | -9.604 | -50.851299 | 2024-10-02 00:31:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06d2c212-e058-3580-8077-30ac0f618c1c | -9.606 | -50.8605 | 2024-10-02 00:31:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b603a330-9fff-3373-8bcb-5f761edb27e6 | -9.6079 | -50.869701 | 2024-10-02 00:31:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d3e5da-ccb8-39c4-87a6-d247c0fc90d4 | -10.6243 | -55.843498 | 2024-10-02 00:31:50 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8458f05-77e9-3de4-9e75-6d1a4dfcb77b | -10.6283 | -55.863701 | 2024-10-02 00:31:50 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2233e2f-5e61-36ae-98d3-b9c59424b880 | -10.6145 | -55.845402 | 2024-10-02 00:31:50 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79717587-308e-3b78-81fc-01fc3a62f549 | -10.6185 | -55.865601 | 2024-10-02 00:31:50 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8d5b35-3ad1-3665-9b50-8c6d8d7ad6f5 | -8.6263 | -46.532902 | 2024-10-02 00:31:50 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90f2338e-9d09-3ee6-ba15-6a59ffe0a21a | -7.8176 | -43.072498 | 2024-10-02 00:31:51 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 448a30bb-9cab-39f7-8db6-c3d46465b9b6 | -7.8198 | -43.081902 | 2024-10-02 00:31:51 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95de304d-4641-394e-945a-678439e3cf95 | -7.822 | -43.091301 | 2024-10-02 00:31:51 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06c1d09f-c0d8-3b83-bd37-b881344add46 | -7.6342 | -42.427502 | 2024-10-02 00:31:51 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bebd5a09-b3e3-3c6c-bd15-421eb19fd9c0 | -7.6367 | -42.437901 | 2024-10-02 00:31:51 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f510b23-75e3-31ce-bb58-df3a141e35fd | -7.6391 | -42.4482 | 2024-10-02 00:31:51 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9a1d730-37c9-3549-bfd2-90f3fa141518 | -7.6269 | -42.440201 | 2024-10-02 00:31:51 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3aab7df-39a5-37fd-9797-df64e073b310 | -7.6294 | -42.4505 | 2024-10-02 00:31:51 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 84967b45-6568-31ad-b5c1-662b044c2e0e | -7.7598 | -43.046299 | 2024-10-02 00:31:51 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6ee11f6-1b8a-31a9-8f11-ecc871bff472 | -8.3313 | -45.327499 | 2024-10-02 00:31:51 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c3ecee2-b206-3479-a497-265218b3bdcf | -8.333 | -45.3349 | 2024-10-02 00:31:51 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01d81fd7-7634-3882-8e6c-02c07de0d10e | -8.3347 | -45.3423 | 2024-10-02 00:31:51 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc31e09c-40ef-3015-bab6-301bbf8cae1c | -8.3215 | -45.3298 | 2024-10-02 00:31:51 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bdd3ac99-0ae5-3ef7-ad57-30233bd0baa9 | -8.3232 | -45.3372 | 2024-10-02 00:31:51 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f1ba65b-c923-39ee-8ab0-7a7cb4a3558d | -8.3249 | -45.344601 | 2024-10-02 00:31:51 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2ad04458-af3e-3e5c-87af-9757327f06e0 | -8.6149 | -46.528198 | 2024-10-02 00:31:51 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2881e859-26be-3caa-8f8f-2d6e74df6965 | -8.6165 | -46.535198 | 2024-10-02 00:31:51 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf7c0ad1-967d-329a-8b41-883274c7c600 | -8.6051 | -46.530399 | 2024-10-02 00:31:51 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00d1be46-7382-326c-92b1-d997e4c5a5b6 | -8.9648 | -48.140099 | 2024-10-02 00:31:51 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5995205-b09d-3f2d-9ae8-db7d19f1f257 | -9.1445 | -48.958099 | 2024-10-02 00:31:51 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89e96c6f-cd51-3561-af7e-22fe53926768 | -8.5937 | -46.5257 | 2024-10-02 00:31:51 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a709fd09-8c86-3ae4-aa3d-445017ff5ebf | -8.5953 | -46.5326 | 2024-10-02 00:31:51 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c74e369-a07f-35f3-8dd8-169b4d523529 | -8.5969 | -46.5396 | 2024-10-02 00:31:51 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 532156a2-556e-346c-910e-4e3ddbd7afb3 | -8.955 | -48.1423 | 2024-10-02 00:31:51 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8fafb8-99e4-362f-affc-1364a9ab7221 | -8.9565 | -48.149399 | 2024-10-02 00:31:51 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bafc751f-59d9-39e4-93dc-1fdfe8d1def3 | -7.7478 | -43.039101 | 2024-10-02 00:31:52 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8bf289d5-b9d8-3029-a138-cd87a3af35a1 | -7.7501 | -43.048599 | 2024-10-02 00:31:52 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3ca149e-5749-31c3-8203-eeaff1a2fe9a | -7.7028 | -42.979198 | 2024-10-02 00:31:52 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba5e5113-657b-3609-ae29-dc34b7fe5b5a | -7.705 | -42.9888 | 2024-10-02 00:31:52 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8a582be5-3bed-36cd-b70f-7830408dbfcc | -7.693 | -42.981499 | 2024-10-02 00:31:52 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d803c27c-bcfe-30e2-9649-1ede65e5c77a | -7.6953 | -42.9911 | 2024-10-02 00:31:52 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe89eb39-b46a-3db0-aa81-0b4fce5fe8e0 | -7.6975 | -43.000599 | 2024-10-02 00:31:52 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dab7d397-35f0-3d52-9c82-9be2dc8576c1 | -8.4225 | -46.315601 | 2024-10-02 00:31:53 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2f2a0a0-ed39-3ff6-bd14-1eeb328de9d2 | -8.4127 | -46.317799 | 2024-10-02 00:31:53 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2d865c3-b7fa-3803-9017-0ae6375535f1 | -8.3732 | -46.3708 | 2024-10-02 00:31:54 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85e0d527-42a1-3f58-87ca-e149721bdafa | -8.3748 | -46.3778 | 2024-10-02 00:31:54 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53c956a5-0431-3c37-b835-6c66246a4cb0 | -8.4812 | -46.8493 | 2024-10-02 00:31:54 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1531d5c-a430-3703-88f7-f30ca134155d | -8.4828 | -46.8563 | 2024-10-02 00:31:54 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa700345-988b-3177-8e13-a8e5ffaa147d | -9.0329 | -49.813702 | 2024-10-02 00:31:56 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d97f0292-a22e-3152-b182-7a295f15e946 | -5.5256 | -35.582001 | 2024-10-02 00:31:58 | METOP-B | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README13.md)
