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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e418a85-de51-3ee3-9fc4-0609e196f2d2 | -11.81148 | -44.25493 | 2025-08-22 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5353c150-69a8-3973-98cd-f50d37e19e8e | -6.46128 | -44.56714 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5518cf73-4882-3432-9d03-c75e746c7c38 | -6.44136 | -44.52148 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb604de2-c56a-30d4-8f10-c95e387445a3 | -12.50916 | -47.92263 | 2025-08-22 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54147a89-b467-390c-bf61-e34697947cdf | -10.49463 | -53.5775 | 2025-08-22 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea1742b1-7fc4-3825-821d-fb4825b4b9a9 | -9.16779 | -59.60816 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54fa204d-05e6-3496-bcbf-c166f318be2c | -8.51066 | -48.82784 | 2025-08-22 04:19:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51c8df3c-cd4d-35ee-a1d0-4c2c926f3b1c | -9.71702 | -45.63348 | 2025-08-22 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85eabf8d-fd9d-311c-a5d6-5f714055cc88 | -8.75475 | -45.46861 | 2025-08-22 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e23bb783-cbda-3527-8908-3ca4f71affd2 | -0.75059 | -47.75775 | 2025-08-22 04:19:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e19db06-f75a-37ea-9fe0-e037dc846d4d | -6.57499 | -44.7306 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9567ef3-e6ed-3531-9df3-386b199e2c3a | -6.94584 | -44.16329 | 2025-08-22 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c812b2e-282d-394f-a34b-125ada7c9eb4 | -7.03847 | -44.61229 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc1a9b8-5b72-3f72-b906-83c50a48cda3 | -11.27668 | -44.95377 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4bf7a92-66b8-3408-858c-04853813d8e6 | -7.16891 | -44.66868 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 010c26a3-96ea-3de2-b845-d82b3f4c84c6 | -5.42762 | -46.35973 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ffea5fe-67de-3b84-8f7e-f69253546d2a | -6.507 | -43.42966 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1196d0e5-d76e-3d0a-a267-956e330bd17f | -12.57786 | -47.08305 | 2025-08-22 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1436cc28-4751-3223-bf7c-c085629ff908 | -11.69744 | -45.52077 | 2025-08-22 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4571617c-391a-3bdb-a171-051a05971587 | -6.51651 | -43.41283 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d360bd09-775f-340a-a831-e1520b16aeac | -12.67243 | -44.96652 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11583754-8c9f-353e-ab6d-2fe491dfe189 | -8.67743 | -47.98479 | 2025-08-22 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8db170d0-2343-331d-b7fa-bbad291706de | -6.29803 | -43.89738 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a8a5731-4a8d-390b-bf7c-d17441f26f00 | -6.51007 | -44.58226 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 60079adf-7610-3991-b357-28a127d661dc | -6.4471 | -53.37469 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1438883e-064f-388f-94d8-36c82a2bb3b8 | -4.59625 | -48.9585 | 2025-08-22 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8929f9f3-cfa2-3bc6-8a40-8321d53be097 | -6.31432 | -43.74891 | 2025-08-22 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7491bdb8-240e-333b-b90f-473d43901760 | -4.32566 | -55.13335 | 2025-08-22 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2642fb02-7ca3-3095-958c-da4edacd0b63 | -6.7711 | -44.32531 | 2025-08-22 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9357d5b2-3cc4-3374-a1fb-20b536e66ba4 | -5.38774 | -51.4317 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 737ac7dc-7be5-3a5e-b27c-d64f2b5b88e1 | -9.91588 | -46.19969 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 217bc0f5-85fe-3ae2-bb5c-b2382b5b7cc3 | -7.72469 | -44.09054 | 2025-08-22 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25cd448d-5957-360f-a3f8-2f86ad852747 | -6.49928 | -43.09882 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57d39e9d-a8b9-3a49-820c-c2f9beaa603e | -9.63419 | -48.33864 | 2025-08-22 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 618be708-781d-3267-a43e-b1fbc6352708 | -6.71393 | -43.20523 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 337446a9-5023-3d18-b936-36ead059f3e5 | -6.5481 | -45.52242 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efa5b4fb-9d73-3bd7-a25a-2c665594b9d6 | -9.20232 | -59.47309 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32fff66e-dce5-397d-beb4-f793c2f1fb0c | -7.86775 | -46.99601 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcdbbd01-dd67-3f17-b175-b2b11226c29b | -10.71238 | -48.22038 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c351b7a-21f5-32a2-9a48-ba961e72b1b8 | -9.44141 | -48.86944 | 2025-08-22 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daa052cd-23f5-3670-9929-43bb57465285 | -7.6273 | -44.99328 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eb27aca-65fe-3551-843c-06012761fbb8 | -6.49808 | -42.96686 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f96721a6-3706-38c3-80e2-0bb2f8919cab | -9.18547 | -59.64299 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0114893a-12e9-39dd-b136-464de432046c | -7.84822 | -47.0082 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77c00564-7b1b-3ed9-9eae-f6b0f7fdc49a | -6.03439 | -42.84078 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8f8778a2-37e5-35b4-bb73-52a7f3439c60 | -7.14784 | -43.22967 | 2025-08-22 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3091650-62d1-3c1c-bac9-5d647507c980 | -7.58453 | -44.37781 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12a227b4-9e57-3ba0-8e93-8a9e4c1788c4 | -6.03568 | -44.35833 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a4c0511-7ab4-3da5-81c9-4f139d694abe | -8.78066 | -46.70943 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20cd6409-1a0b-35a6-afe0-9e58ca76748c | -10.49948 | -53.57835 | 2025-08-22 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c08b10c-dc99-3510-8d6e-8393749002bd | -6.25226 | -53.6839 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ec1d9f5-9ede-34ed-8438-a0315bfa0150 | -6.73803 | -50.95475 | 2025-08-22 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b29a5171-69f3-3646-ac4d-8990bf70a412 | -5.67768 | -52.21023 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bebdc69b-da99-3dde-8969-0d1bb8e4fb42 | -6.20737 | -43.5622 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 237899c3-3cc6-3d66-aae2-0072f4617738 | -6.00587 | -44.13718 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73233951-d9a0-3b07-bb7a-4a37c220a716 | -6.49751 | -42.97055 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92b0e9ed-9861-355d-8079-5be9fb28eeb2 | -6.08154 | -44.13118 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc1ecfbd-dca8-372d-a4c6-e5d866e19b65 | -11.79242 | -48.78889 | 2025-08-22 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c04097ab-937c-34b3-b092-5487db2a489b | -6.92635 | -44.39586 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38267837-90df-36a6-9e9a-cc7dd4b221e6 | -9.63946 | -44.60926 | 2025-08-22 04:19:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78cfa69f-bf82-3691-8e16-191cf6f20c33 | -6.03183 | -44.36127 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f29080eb-0023-3a01-ae0a-7933390116ae | -10.58109 | -49.16262 | 2025-08-22 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41a5b61c-0d57-3ff5-9862-94663b4fde6b | -6.49525 | -42.96265 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba205bfe-dc0b-398d-81cf-57991afea54d | -6.26944 | -53.70807 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 175da5f2-50f0-3f60-9e40-65fc2a852ca0 | -12.00418 | -44.67239 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f94c0f43-cfc1-344d-97a9-313aa4fe07e9 | -5.88827 | -53.63728 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0de5a3f4-4822-3c54-8223-3e56b941a5e7 | -7.72524 | -44.087 | 2025-08-22 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc086010-8994-3b6e-9365-09e199e2e5c0 | -8.79221 | -45.42471 | 2025-08-22 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf32acff-968b-3879-a464-7402380c8ee3 | -11.31369 | -44.95214 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1daa0c14-4bc8-32bc-bd7a-fa83c6829d1f | -7.6512 | -46.252 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7965d924-188b-3f32-a655-f1d27c69857e | -12.5076 | -47.43427 | 2025-08-22 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45d264df-c21c-39b7-8af1-e5f22b6ba1f4 | -6.50568 | -44.58865 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1fd32996-4a54-3aa9-b02c-e66ca40b8878 | -6.4347 | -53.38503 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e347700d-5887-3133-840e-48d2a094f4d7 | -11.31036 | -44.95162 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f7e84fa-5909-3dff-8fe8-1131bf22c6e8 | -7.14851 | -44.66901 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6fe5e17-b98e-3a3b-935a-06c6e2e84f38 | -11.12241 | -44.71671 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b1c38fb-2b7c-31a1-8e38-777de3aa87fa | -12.00528 | -44.6651 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c17417a8-7930-343c-8181-08f0f24ade4e | -11.28947 | -44.93747 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31218769-7f4d-3b07-b3e3-b71f6fffcdf0 | -11.32852 | -48.33278 | 2025-08-22 04:19:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17359ee4-9bb2-3053-a46f-e8f57efe1b2f | -6.51392 | -44.57932 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38aa8b4a-b380-3a02-a303-3cf8abc0f009 | -6.76724 | -44.3283 | 2025-08-22 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96019853-288d-31c7-87c8-0d2c8deef94a | -6.02249 | -44.37753 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 281f153a-a3cd-3282-819c-e8b5073ec768 | -6.0258 | -44.37805 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed7d4921-bc36-32db-9963-e5fda48be2f9 | -5.97018 | -52.22437 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd96491f-2af6-3c71-bac7-f22ff1eedbab | -6.0214 | -44.38444 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a11df900-309b-36a5-ab63-75778e7f431b | -6.21173 | -44.12352 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9287f290-55b1-3764-8dc5-94acc354e2a6 | -4.84646 | -47.57069 | 2025-08-22 04:19:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8c0720c-2f35-31d0-9b81-a2dddaec2458 | -6.3019 | -43.89443 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 135fd890-6adb-3df4-9e99-a20b1c98307d | -10.72792 | -48.23486 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8920504f-8ef2-3b2b-b2ce-e2134721693b | -6.02526 | -44.3815 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ded40f2-87f4-3d87-b5d3-b034ff154ad9 | -9.58146 | -55.35516 | 2025-08-22 04:19:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb2d161e-ecb7-3598-89cb-e5eb95b99d1a | -6.33702 | -43.42516 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ec69214-e6eb-3d8f-9329-7664b8aa8a26 | -11.30205 | -44.96125 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f007843-6a55-3805-9718-b69d1a9fc6a7 | -8.12698 | -47.14789 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 651aa56d-9baf-3e34-b8e0-d1d58d22d5d5 | -8.78403 | -46.71001 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6a858b3-d884-3a1f-9422-1b10492439c4 | -6.03514 | -44.36179 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b9ad11d-3965-3597-b7f3-d10d9aa2828f | -6.01587 | -44.37648 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbccd032-3fbc-3e75-a82e-a44887dbac1b | -9.13453 | -46.38847 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ecbc43dc-71fd-3b27-8c3b-cdcc6721abba | -7.62322 | -46.25492 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d199f951-d8c9-3279-ae8e-1e35e75bb3a7 | -8.0048 | -42.96147 | 2025-08-22 04:19:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README29.md)
