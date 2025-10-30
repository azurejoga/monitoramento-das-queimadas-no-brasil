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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d501742-237f-385d-ae83-9a991a32bb1d | -7.33004 | -47.25299 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85036dc1-a8de-32c3-8bc6-3fd844d61bf3 | -7.92378 | -45.64267 | 2025-10-30 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2df9bc45-5a42-3afb-90b9-e022d8fea514 | -6.11764 | -48.10299 | 2025-10-30 04:25:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f12bf969-f5a3-38d7-acb4-b4cf89f7eacd | -4.37591 | -46.51068 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 305445a9-7d26-3d05-a75c-22e00edd74b5 | -10.95422 | -47.83885 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 139771db-4190-308d-aff8-35968f322a31 | -6.70728 | -38.21611 | 2025-10-30 04:25:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 13b5afd3-607b-3404-a898-186e46e91d72 | -10.86729 | -44.95325 | 2025-10-30 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0fc419e-7b71-3547-9038-a707aa674616 | -11.33113 | -47.96939 | 2025-10-30 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd4c8927-cbd2-322a-bcae-236efbae0728 | -7.6273 | -43.58558 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f35b633-cca6-3046-a750-cae6595025b8 | -10.53818 | -45.04892 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ed933c5-ec64-3641-95b3-a371c5c16f46 | -6.91735 | -45.2122 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 397938ac-c954-3605-95ef-0e11b0da9516 | -11.14347 | -51.07302 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| af3a0328-4dba-3280-9b9d-25a4deea3b21 | -4.74949 | -45.71642 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 092c718f-5e08-3874-b562-fa1b4aa249bf | -4.53134 | -54.96856 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2569eb35-198a-3b92-a3b9-bb96bbc2f3d4 | -6.52217 | -46.90499 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 94b20ce7-0bd1-34e0-8a9b-01df16631424 | -5.79718 | -40.82396 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 91f75538-b060-3c55-84b0-1c00d174f02c | -5.70327 | -43.16009 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 91752cd1-0b58-3999-97ca-e65b15d92a23 | -6.61712 | -47.18208 | 2025-10-30 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a75f0d5-db05-369e-a4e9-fa2431a9bf83 | -11.55314 | -44.68762 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d8a62cd-38d7-3175-b556-eeab0ed5dd2b | -11.27967 | -47.75874 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 703670e7-a74a-3714-a1b7-629c17f5e290 | -7.33959 | -43.91299 | 2025-10-30 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cabc12ec-483e-3dad-91f5-d47886140201 | -9.84963 | -47.6916 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54f1b4ca-e664-3dad-ab89-ff023d65ed90 | -9.29 | -48.4235 | 2025-10-30 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2444b94c-1f6e-319d-9375-46b11422ae54 | -8.05212 | -45.16422 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfd41011-9571-3af0-b72e-9475ed0d3a21 | -11.02677 | -47.7893 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| defab0cb-8a6d-3a31-818d-2349f09f24b3 | -7.93526 | -45.48188 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b6916c7-c863-39f0-939d-671ecfe2d0d9 | -7.6272 | -43.61042 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fdd032ae-c82c-3a57-bbcc-51d3ef3978c8 | -5.72648 | -44.4065 | 2025-10-30 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3c94453-b99a-371c-8474-3f2bd57fa384 | -7.95689 | -46.74942 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f4fdee2-f8f4-3c20-b8ce-7637665affcc | -10.97748 | -50.11731 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a24dd70-8737-3152-8a24-452fe4f1e67a | -5.67444 | -45.88401 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70f33715-a91f-398f-a7d5-71f659cbbfe2 | -6.64392 | -44.61637 | 2025-10-30 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b2ab5d4-f317-3b84-a170-49c9dd49ecc1 | -7.95579 | -46.75636 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d80f161-3942-356e-85e6-8c8276b6bfef | -5.40594 | -46.01442 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fa91a00-c180-38b4-b4d5-5b4b61bf74bf | -11.16565 | -45.22757 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 560dd684-6926-3de7-bb0e-706d1b4c8e25 | -5.33724 | -44.84775 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a0d5296-7288-3068-80bb-b9daf6a6c794 | -7.06279 | -44.46899 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 025e4e14-0e77-3964-8617-598cea46c54b | -10.64739 | -48.79438 | 2025-10-30 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08c99f21-0711-3884-b162-3320185eaa59 | -7.30132 | -44.96834 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 772fda17-17a7-315e-b431-56c6b1c9a881 | -7.1559 | -44.70465 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 915582d5-9eca-31cb-ab48-dc5096a6693e | -10.8524 | -50.12681 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60b18459-4135-31de-b59a-c60f113951f3 | -5.42107 | -45.03035 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7529fecc-958c-32c2-b004-65cba8ee118c | -11.4052 | -47.71764 | 2025-10-30 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d29ee70-bcb7-374b-b0b9-a6239e3213c2 | -10.86036 | -47.61785 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58327a03-1c07-3e38-960d-73ef0db170b2 | -8.70493 | -47.98331 | 2025-10-30 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 600d3b20-957f-31e6-bae8-942ac2ee19ba | -11.2374 | -49.86214 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4bef101-2202-3edc-88fb-83986239530e | -7.27704 | -46.06335 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51429be0-54ca-3e56-b6bd-dda37ddeb25a | -11.17675 | -47.61592 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 284afed5-2581-340e-baff-6a05c1dc687d | -10.63282 | -47.97851 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45fbe82a-af9a-3b19-88f9-db252ab96673 | -11.13373 | -51.08529 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9fb55aad-d04d-3b88-936d-79e3362d7998 | -7.61543 | -43.59198 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b50c8e6-f3c4-3b92-a409-4486870b5691 | -10.76246 | -47.89046 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da87c7a-ba0e-364d-af50-7bc573909d81 | -10.25799 | -44.57101 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41799f15-57f1-388e-b823-4375ae47585c | -9.8247 | -47.69835 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 03d14183-0245-3edf-9948-9d10bea0941f | -7.0757 | -44.93354 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b82d2bb-0720-3a0d-80c5-842d43658d21 | -6.14007 | -41.69734 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e33efaa0-0804-36e9-94f0-5c1b051eea1e | -3.35445 | -52.80765 | 2025-10-30 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65a780e3-16b6-3622-b5a9-87882e30eef6 | -5.4244 | -45.03088 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeebeeee-71af-335d-880e-26e5d2551a74 | -7.34485 | -43.90179 | 2025-10-30 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33015a9c-e95b-3b6a-a5e2-da470b2adced | -8.32391 | -47.92574 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 924a50fe-b4fe-3de1-b6c1-41e86da0a0b2 | -7.26948 | -46.88471 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faf78b12-4123-33d7-a7fb-a5c7338adee5 | -7.79573 | -46.41457 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 92ca880c-4549-3419-bc05-0047cb5faa29 | -7.9547 | -46.7633 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8e6eab3-4e96-3c79-90c7-7de593d5d18b | -11.15163 | -47.77398 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 286b03fd-e451-313c-b9c1-5a735a632cf1 | -7.3397 | -46.89278 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 300aa6c5-26f5-30e1-b24e-44c203619d87 | -5.01628 | -43.77083 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9161b054-46e8-312c-b958-87d8ce73aeff | -6.11063 | -42.43961 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d8dfca55-0fba-3299-a28b-4be4d503c4f5 | -10.93682 | -47.79994 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a0a4aab-2157-32a1-9eb1-6879197a97c0 | -10.61988 | -47.8894 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44ab77e7-8a85-3d87-8cce-f1247cb9ac3d | -4.90862 | -45.67834 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 056c7090-e58b-355c-a086-223b21d93740 | -7.32973 | -38.85346 | 2025-10-30 04:25:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26a142c2-df60-3853-84da-82252fb562f0 | -5.43347 | -45.34301 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 8feec40a-5bf2-32dc-bcc3-8d18bdac2add | -7.30407 | -38.92838 | 2025-10-30 04:25:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f643879e-e68d-397b-83f1-99949e7776b8 | -10.33568 | -47.09215 | 2025-10-30 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d159a681-cd65-331e-935c-f3158076ab50 | -4.14341 | -50.68564 | 2025-10-30 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f40ff4-b0a7-3d4a-a096-28f9a320e20e | -5.22878 | -46.14489 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2631b605-d110-378d-b18c-455fb47413da | -6.98824 | -46.23715 | 2025-10-30 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc8fc147-2652-3e2c-a1bf-3f36562141db | -6.91655 | -42.25382 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d2203f7f-f608-36f5-8e3a-3941cbfbfd20 | -10.91745 | -47.81474 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e12aed64-49a8-37b3-ac18-4265b7dd0074 | -7.42901 | -49.67044 | 2025-10-30 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56a0ca74-d44a-3775-aa3d-fe795c84134d | -3.46126 | -52.87352 | 2025-10-30 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8a2ae5b-4b00-39d2-b733-6b738dc1ab7b | -6.09112 | -41.77643 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e8397de5-5893-3d50-b5a5-9519ff12721d | -6.88713 | -48.63985 | 2025-10-30 04:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29fe2a1d-68f5-3f64-b924-3568ebd76384 | -11.14576 | -51.05947 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8caaa386-ed50-3e65-b75c-3acf85184619 | -6.85417 | -46.28996 | 2025-10-30 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57730937-085e-3c96-96de-02b3ff3f1d56 | -7.58854 | -45.37417 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44171c49-40f3-3335-9d79-5e18aaa27222 | -6.64803 | -47.2882 | 2025-10-30 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94900007-b1ee-3ea3-9214-42222a02fd8e | -7.95468 | -46.74196 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22253c29-1b0b-3f36-8ff0-f38ad85d8350 | -11.84752 | -47.92716 | 2025-10-30 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ded41afd-319b-3184-ac2e-c1e4c155ec8b | -4.35968 | -48.72142 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 303e1595-dc9e-3512-8c90-a95c034f3b04 | -7.30357 | -44.97609 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86d5b75c-bfa3-3e0f-9f0a-afe4726696f4 | -11.12923 | -51.08916 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e2d8d5bf-222a-3ac5-9175-8fa8d90f4013 | -6.14446 | -41.68552 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d14fef5a-1983-3fbf-bf24-8e0abb574f41 | -7.06343 | -44.94614 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df6c449b-303a-32bd-a8cd-52246123cac8 | -9.70429 | -48.29628 | 2025-10-30 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c4a34c3-9fb0-33e0-b44b-808d22e733d0 | -4.51822 | -47.84087 | 2025-10-30 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaeac65c-6629-35dc-a3be-7d2d43489e68 | -6.01426 | -41.97643 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d198f78a-a1b2-3444-bded-05f60839bd70 | -4.25353 | -50.67479 | 2025-10-30 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45cb5808-0f87-3fa4-b2aa-0aae2f40e26e | -3.60674 | -52.64587 | 2025-10-30 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b791b217-fe22-3418-9c9e-76055c2e47a5 | -6.5779 | -42.6573 | 2025-10-30 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README52.md)
