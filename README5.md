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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 375e047a-7821-32d6-80d2-2a03faa8f5a7 | -13.37126 | -53.56326 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af73ce4a-b692-375f-bd08-83aeed5c1065 | -17.29456 | -42.67962 | 2026-01-12 04:42:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eb5db6b-ec27-3832-a0e9-5f3cba709d04 | -13.3782 | -53.56449 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0e46fa4-9521-37de-beac-3d75ec645b9f | -15.51572 | -47.99178 | 2026-01-12 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da01afbc-13d8-3e81-837b-5641a8b3f926 | -13.38233 | -53.56117 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f539794-c824-3bd4-99c5-68aeb7622375 | -16.30777 | -45.10606 | 2026-01-12 04:42:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51b463f8-61d4-37bd-bf68-14a49dab667a | -15.51942 | -47.99233 | 2026-01-12 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c279265-d732-3fe9-87f2-4973eee80a7c | -13.37538 | -53.55994 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bed2f37-03b5-3e38-bf5d-7aa98517cd40 | -13.37191 | -53.55933 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f22577fe-b57d-35b7-980c-4093367889a0 | -13.37256 | -53.55542 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6846a91c-c1e9-3c4f-b6d0-01fce7fa1249 | -13.37473 | -53.56387 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8deba315-e36b-3ed0-9a72-e43347ffce55 | -16.31225 | -45.10667 | 2026-01-12 04:42:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3325054c-4351-3851-abd5-f78753e39d64 | -16.12583 | -49.89199 | 2026-01-12 04:42:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58b2f098-9663-3af6-800a-85d993148f58 | -15.52006 | -47.9878 | 2026-01-12 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49785b03-201f-3473-83b9-f4eb0064f732 | -17.29804 | -42.6807 | 2026-01-12 04:42:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b152ae3-8592-3dec-8922-d51f0e9fa68b | -17.29988 | -42.68048 | 2026-01-12 04:42:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec2b46f0-12c4-3aec-8237-ead931a86bdc | -16.05199 | -47.21614 | 2026-01-12 04:42:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 889f492b-63cf-387a-9da7-9f75a3c1b179 | -15.51203 | -47.99115 | 2026-01-12 04:42:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d66229-828a-3cea-a998-dc0d74ddea8f | -14.43574 | -46.24138 | 2026-01-12 04:42:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e4553be-eb17-334c-9e29-3de65f65d184 | -22.56974 | -46.98491 | 2026-01-12 04:44:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09ddef14-b1fe-3a2a-885e-2c48b2340add | -22.56762 | -46.98603 | 2026-01-12 04:44:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a1e2390-b1d8-38a9-8cc2-fff1d35a03a7 | -20.35735 | -40.95294 | 2026-01-12 04:44:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d18e156a-5216-3a27-ad37-e8bf4e9752e2 | -20.12036 | -46.8525 | 2026-01-12 04:44:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63157045-a94b-3dba-957d-93c8cb4a9e14 | -20.35789 | -40.9469 | 2026-01-12 04:44:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a7b6f587-5231-37ed-b719-67c9c902ebb7 | -17.32551 | -48.79126 | 2026-01-12 04:44:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 287062ce-90f1-3164-9e6f-c5e8f603a55a | -20.11928 | -46.86089 | 2026-01-12 04:44:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29a69b62-8a99-30b7-809a-47845a9c9966 | -20.11929 | -46.86271 | 2026-01-12 04:44:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5816a5a-8bd9-3a50-bd5a-0cb895f20e62 | -22.68017 | -45.10517 | 2026-01-12 04:44:00 | NOAA-20 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ff50ac48-9f80-3725-b6e5-848eb971f25a | -20.12031 | -46.85427 | 2026-01-12 04:44:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad2d0018-ba4f-3c5d-9133-d38c632c8d2a | -20.39863 | -50.87276 | 2026-01-12 04:44:00 | NOAA-20 | NOVA CANAÃ PAULISTA | SÃO PAULO | Brasil | 3532843 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4be86d4-ef90-32b7-b150-fedd89caa22b | -20.11983 | -46.85664 | 2026-01-12 04:44:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aba1bd1c-46c3-3ef3-a5a9-114ae32db519 | -22.56543 | -46.9843 | 2026-01-12 04:44:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31dfbc17-2edc-3524-a505-ab2473b544d7 | -20.1198 | -46.8585 | 2026-01-12 04:44:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e9e96f5-3194-393c-8cc7-620234ee0ea6 | -22.56493 | -46.98863 | 2026-01-12 04:44:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 091fdda2-5602-3da4-a6d0-6ecbc67fcc1c | -22.68209 | -45.11029 | 2026-01-12 04:44:00 | NOAA-20 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 96287dc5-ee7c-3f38-a243-2492410c0641 | -0.08932 | -51.27731 | 2026-01-12 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a20e31c2-b993-30de-b9db-c13632467486 | 1.3542 | -60.03383 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ea2687c-acda-38c7-820b-68e554c8d111 | 1.35305 | -60.04811 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aa8b26e-fcc3-3dae-8f94-8efedee7f0f9 | 1.35198 | -60.04123 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3b4c652-39d9-30eb-bfe3-68ff0411be74 | -0.08874 | -51.28092 | 2026-01-12 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cfb21ea5-ad72-34d7-a1b3-a077850e9a78 | 1.35582 | -60.04415 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cdead1d-fb66-3660-b79c-ccf1b2d3943b | 1.35643 | -60.02644 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b27e0aba-1ac1-3986-9679-65f16ef7eaed | 1.3482 | -60.01714 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5a98147-ed22-3892-b1be-7677eeac93c5 | -0.09479 | -51.27828 | 2026-01-12 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e818c2cd-f3ac-3a3d-b20b-a6714023893d | 1.35973 | -60.02593 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ff87a87-5952-32c5-aada-f4926dcada38 | 1.35251 | -60.04466 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d64d334-2379-31b7-af63-edce77d64a24 | -0.0899 | -51.27372 | 2026-01-12 05:29:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa2f4096-1c3d-3fe8-959c-f69a5d314702 | 1.35474 | -60.03727 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 044434f4-e298-38b1-b85a-d3741007f805 | 1.41542 | -60.74754 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 592554d8-ab78-3fc8-99db-47fbb74e0e7b | -0.08999 | -51.27597 | 2026-01-12 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f6793add-6ae7-3f08-8da4-7f079a9d6527 | 0.73891 | -59.31863 | 2026-01-12 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06dcde7e-0b84-3397-908f-81ce663a0f16 | 0.68469 | -59.27969 | 2026-01-12 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a662ff33-136f-30d3-aa51-ea2fe36dae7a | 1.3515 | -60.01662 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64f7a87a-d7f3-301b-801d-dff3f6081dff | -0.08944 | -51.27958 | 2026-01-12 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 94d912e2-be61-32e5-bc8f-2adfebca7e85 | 1.35144 | -60.03779 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89481e43-0b56-3189-8e86-5cf30807b760 | 1.35481 | -60.01611 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7013f562-8cfe-317e-9369-a16653a9ce5c | 1.35528 | -60.04072 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa5dd067-282c-3768-88db-06d004c2cbb3 | 1.35636 | -60.04759 | 2026-01-12 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b78c92d-466d-39f6-8bf7-5a01d5027a02 | -5.18576 | -40.73523 | 2026-01-12 05:46:00 | AQUA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 854a70c9-0a45-32ce-92fd-ca5d457908dc | -5.49655 | -42.14787 | 2026-01-12 05:46:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7808c2e1-e2a1-3e07-8892-5323b45c6656 | -5.49516 | -42.15703 | 2026-01-12 05:46:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b1dbb978-6371-3265-a4ec-fc96c2b67ba1 | -3.71929 | -43.31799 | 2026-01-12 05:46:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 544f8c49-e143-3f5e-84b0-9e536f7c231f | -7.05205 | -45.05299 | 2026-01-12 05:48:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e8beec86-3dda-347a-8762-28ebfaa13651 | 1.35358 | -60.03981 | 2026-01-12 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca181aeb-4aa5-3376-9d3a-908f1b7dd45a | 1.35282 | -60.03517 | 2026-01-12 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15f9e194-5164-3673-b8fc-c519fbd59007 | 1.35815 | -60.03908 | 2026-01-12 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d0c9c16-2b34-3eb5-999a-405a9eaa8ac1 | 1.35433 | -60.04439 | 2026-01-12 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03c12c02-5f58-3a63-b2cd-3873f5572559 | 1.35508 | -60.04898 | 2026-01-12 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba81398f-f673-355b-9703-976dfaf60ffb | 1.36044 | -60.02436 | 2026-01-12 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e38a937d-2c2c-33d6-a9c4-40fa31b58a98 | 1.34976 | -60.01652 | 2026-01-12 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74fe6b4f-99bd-34d8-aff5-9eea630f01cb | -2.85017 | -42.02243 | 2026-01-12 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| fb432fe8-b58f-317b-882f-6bbf6b6bb9e3 | -9.42573 | -40.26566 | 2026-01-12 12:14:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 8008af85-7851-3892-8271-ffd3e2b41c89 | -5.82876 | -39.58923 | 2026-01-12 12:14:00 | TERRA_M-T | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 43.2 |
| 327d6e07-113d-3827-883f-f817b243a711 | -4.27747 | -45.24929 | 2026-01-12 12:14:00 | TERRA_M-T | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3a61435e-73df-3357-9cab-6d1edd2d04fc | -4.04057 | -45.62583 | 2026-01-12 12:14:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7b06d9bd-e3d7-3540-be2e-8e4b95e37fc2 | -2.18083 | -47.74449 | 2026-01-12 12:14:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5143b5fa-ce09-3d33-aa59-a24bf4296d1b | -3.2804 | -45.41407 | 2026-01-12 12:14:00 | TERRA_M-T | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a6633c22-dd27-3b99-9d11-f42d0e530b9e | -4.27596 | -45.26015 | 2026-01-12 12:14:00 | TERRA_M-T | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1369e853-8321-3396-a52e-07b0a850edae | -4.16929 | -38.36282 | 2026-01-12 12:14:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 0cd4c6af-271a-3f6d-9937-5efc8c8d0c50 | -5.19609 | -40.61216 | 2026-01-12 12:14:00 | TERRA_M-T | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 0f96ae06-e7cf-3e4e-a2a9-16e063acd680 | -3.94456 | -38.38857 | 2026-01-12 12:14:00 | TERRA_M-T | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 39.6 |
| 346a1719-48c2-38aa-8c77-1ee6d793a5a6 | -4.70973 | -44.48214 | 2026-01-12 12:14:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 01938c37-9ca1-371c-ad67-83e34e7058b8 | -4.65959 | -40.78773 | 2026-01-12 12:14:00 | TERRA_M-T | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 206cac29-dd65-3a16-afbf-9c17bae40929 | -3.94947 | -38.39586 | 2026-01-12 12:14:00 | TERRA_M-T | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 38.9 |
| 01f5b6ed-5e44-39cc-8575-75040ad439a2 | -7.78261 | -44.05433 | 2026-01-12 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2da2e71d-b029-3d73-a010-fa1865fc3d9e | -2.84651 | -42.0162 | 2026-01-12 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ca9ff10b-10b9-354c-9d38-4a4709cab4ac | -3.28545 | -45.41005 | 2026-01-12 12:14:00 | TERRA_M-T | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cc63e12b-8c83-391e-b01c-608db05f291c | -9.42079 | -40.27048 | 2026-01-12 12:14:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.1 |
| 690b98c2-d63f-3149-b454-591b282c7c89 | -7.83793 | -43.80335 | 2026-01-12 12:14:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fc9d377b-9bd8-378c-9e0f-b06ba2675c7b | -4.16452 | -38.35528 | 2026-01-12 12:14:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 76.8 |
| a6975ba8-2afe-3560-be0d-dcad8fb50760 | -4.04202 | -45.6155 | 2026-01-12 12:14:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b454c82b-3f6d-3ee4-90e0-d4bffedea0f2 | -5.89871 | -42.7959 | 2026-01-12 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| d6e8c963-5a45-3cbd-9466-dea35c20a322 | -2.96366 | -45.56076 | 2026-01-12 12:14:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 259c660b-ba3f-3af8-81e4-a53fed115049 | -5.53065 | -39.20092 | 2026-01-12 12:14:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 327f6bcb-c7dd-311f-985b-a7bd07fa1d8f | -4.6542 | -40.78161 | 2026-01-12 12:14:00 | TERRA_M-T | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 5528117b-7581-3d72-a4e8-9a64a92ffedc | -3.97482 | -42.51775 | 2026-01-12 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 9853d401-f1d0-3c44-b76d-9c06a2e13565 | -17.69911 | -45.51359 | 2026-01-12 12:16:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| bdccb99a-6dee-3874-a43e-2a290899bd85 | -17.6972 | -45.53044 | 2026-01-12 12:16:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8ef2713f-c75c-34f3-a542-80e6de31a490 | -12.66325 | -46.76483 | 2026-01-12 12:16:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| e4195aec-65d5-3ef6-b534-d9dc461ab2b6 | -12.66502 | -46.75924 | 2026-01-12 12:16:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |


[Clique aqui para ver as próximas entradas](README6.md)
