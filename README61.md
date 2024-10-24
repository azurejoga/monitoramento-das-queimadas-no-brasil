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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30067433-c9d7-36ae-8739-f9db85f7228b | -4.53368 | -46.73333 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50a806e2-35b0-30c3-82f0-888b7cf37793 | -4.42692 | -46.46646 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04c64029-ecef-36c2-84fc-a20a5fa9ffcb | -4.42573 | -46.46503 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 472da224-db16-37ab-96aa-a7a19d0646c1 | -4.35577 | -46.80214 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7e9a27b-cf24-3fe0-b4e6-fe12f3fc2a82 | -4.35189 | -46.79683 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6bfaf55-24c4-3d8b-b500-e646e5386f05 | -4.35118 | -46.80151 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21c7a1ab-d96d-3eb1-9466-47a9ab97924f | -4.28315 | -46.75608 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 940a43f8-41a5-3364-9127-2df8006b45e7 | -4.27923 | -46.75097 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2eae9df3-d84f-3d48-827f-0944e43754f1 | -4.27869 | -46.75286 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42c877cd-78fd-3291-8da3-b209fdbd3a3c | -4.27854 | -46.75552 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b093cd4c-9b28-37b0-989c-0fafee6082af | -4.27803 | -46.75742 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ab88b89-b140-3ba8-b69d-6a6960792e5e | -4.19526 | -46.63017 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10ba5c13-1e37-346f-81e9-0c132965f633 | -4.1934 | -46.63152 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b149a74c-6351-33e3-aeeb-8241b64bed01 | -4.17955 | -46.85496 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02576510-5df0-304e-84d5-2264f9099a1a | -4.17888 | -46.85954 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0baf2dc4-fef2-35ac-9b4e-43d243cb7b5b | -4.17791 | -46.80251 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9909e8e-83d6-3296-b3c8-f64941d3ef95 | -4.17338 | -46.80152 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ef713c7-1560-37d4-9d8f-a6ca1e632d06 | -4.15871 | -46.86862 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d15dc153-7384-3ec7-aaf6-d71cb66749dc | -4.14998 | -46.83444 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8141457d-3ec9-3182-9d8f-7d502db1d1c0 | -4.14971 | -46.83615 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18cefc0e-c110-39d5-b6fc-21963dc03a27 | -4.14931 | -46.83881 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2a6d089-f100-3c17-bbac-f19d5c4ea72b | -4.0447 | -46.2445 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07fda118-1d4b-3dcc-88c6-ab4541925d81 | -3.99534 | -46.43871 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a69747d-b9da-3d8d-bbad-70e8d255319d | -3.95368 | -46.3978 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b426b94a-5e1f-343c-99ba-e8cfb0ea8e86 | -3.94848 | -46.43275 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f5432a4-65b0-3e64-8729-3c3ca47cd7d3 | -3.94452 | -46.42727 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 19843ff7-3838-3dd0-bf2d-2a06ac50fc1d | -3.94379 | -46.43217 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 940496af-e94e-313e-aa2e-3bc8f9243247 | -3.93985 | -46.42658 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 2dfcd01c-a8cc-3038-bbc3-914cfe524dc6 | -3.93912 | -46.43152 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| c33655de-51b7-37e3-979d-28d897b2a583 | -3.93519 | -46.42579 | 2024-10-24 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d9f23279-120f-3152-8968-a9c54d721297 | -3.82378 | -46.92873 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fbf15ca-b282-3134-af86-b67a2ce6349b | -3.82315 | -46.93301 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91eda98f-2697-3327-ac1d-6e30ec7860df | -3.82227 | -46.92635 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f85a104d-af1f-3855-aede-e71297297ecc | -3.8216 | -46.93071 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1d3676fa-6fca-3e5e-ba4b-9af68d081520 | -3.81926 | -46.92813 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99aa6428-4f55-3970-bbdb-38b286b24549 | -3.81777 | -46.92565 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 703bc991-0a5d-3cc6-bc19-fb26aa53f3bc | -3.81709 | -46.93009 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81cd7870-f177-342f-bef2-f32452fc5a88 | -3.81543 | -46.92282 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2be72a0c-99b4-3fb6-b4ec-15d0bfd8e80e | -3.81329 | -46.92485 | 2024-10-24 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a919798-aa78-3782-b87f-3b9444f8706c | -6.03145 | -47.96681 | 2024-10-24 04:55:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 287a3b4a-1ef2-3cc8-a11c-4c70590f1288 | -5.84746 | -47.28633 | 2024-10-24 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da362d6f-4c34-3c72-abf0-64027135479d | -5.84358 | -47.28115 | 2024-10-24 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2564b99e-8c7d-3a3a-a4a9-27b4ab1957b6 | -5.84293 | -47.28569 | 2024-10-24 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fdf3a782-11be-3776-961b-c54942315879 | -5.69973 | -47.34512 | 2024-10-24 04:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc1292ca-efad-3437-b23b-9fa529dccbe8 | -5.6982 | -47.34271 | 2024-10-24 04:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6c0e4f2-913f-32e5-827b-ad4dc99f2c33 | -5.69753 | -47.34716 | 2024-10-24 04:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36ee87d0-3cce-32f2-add7-af207b8d9a16 | -5.69523 | -47.34445 | 2024-10-24 04:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3c70980-f7e9-3b26-9213-8069de08f0ef | -5.44594 | -47.6808 | 2024-10-24 04:55:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 392c54b5-901b-33bd-9329-a5d1b4a1d16a | -5.44157 | -47.68006 | 2024-10-24 04:55:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a6ac34eb-074f-3896-9673-517d8a7dba70 | -5.44095 | -47.68431 | 2024-10-24 04:55:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0ac6569a-5595-37fd-8055-3dcdc3247f35 | -5.07512 | -47.89219 | 2024-10-24 04:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b87430d-e090-32c2-bf48-c75e490600be | -5.00799 | -47.64601 | 2024-10-24 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 330fd7a7-25a0-309b-a4a7-86ce509e575a | -5.00763 | -47.64343 | 2024-10-24 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7556a614-c49b-3739-847d-52059259cb59 | -5.64978 | -46.97339 | 2024-10-24 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9794d62c-d7af-344a-af40-725fc4561297 | -5.64687 | -46.97128 | 2024-10-24 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| eeca256d-5dea-3c50-b73b-cc3cfe86f205 | -5.64616 | -46.97605 | 2024-10-24 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 267440ba-1747-3597-8035-8bd2136528a3 | -5.64515 | -46.97277 | 2024-10-24 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 70bf99b9-b8fb-328c-baa6-0558e55938a2 | -5.43059 | -46.56221 | 2024-10-24 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40bdef5a-a6ab-330c-b41f-36c2d975bed8 | -5.42587 | -46.56145 | 2024-10-24 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fda93ce-9c0c-3cef-b41f-ccfd2566ce36 | -5.30585 | -47.0012 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 800035b8-3c3b-39de-91b4-5ea95f190325 | -5.30541 | -47.0032 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d99f41d-cc09-3ddf-9aed-f92ac49c8c5e | -5.30515 | -47.00587 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86038a49-5ccb-3543-af56-ebecd773fe61 | -5.30475 | -47.00786 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c55f038a-2a90-306e-8362-97ff10e178cf | -5.30128 | -47.00039 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0520951-ef80-35cb-86a0-dc096a8c909a | -5.30085 | -47.00235 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d088227d-676d-3ec3-8964-3f6dbebc668c | -5.29989 | -47.0097 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b90813d9-0fe7-3539-a457-13400fbfc33f | -5.29953 | -47.01169 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c40d51d-4202-358d-97e7-328353ef9604 | -5.29603 | -47.00418 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac2974a5-4aa9-35b5-8c4a-f5616a351eee | -5.29533 | -47.00887 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 869817bd-4270-35fc-a757-cd51476b9d27 | -5.29464 | -47.01355 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 088a1e16-472e-3cd9-a9bc-f9e4b8c42fa9 | -5.29076 | -47.00813 | 2024-10-24 04:55:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ead3ad7b-912e-3640-bc7a-04667ccbc077 | -6.52182 | -47.26605 | 2024-10-24 04:55:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5c175cfa-91d8-3851-854b-b12ed1d78017 | -6.51723 | -47.26542 | 2024-10-24 04:55:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 789b9ca5-9d5a-39a9-a7de-e1154fd88555 | -7.37497 | -47.23091 | 2024-10-24 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3e97fb1-50b2-3a68-9e45-bea1c1aed95d | -7.37031 | -47.23028 | 2024-10-24 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e62e3c47-d6b3-3286-94f2-51ee0d1b5b07 | -7.05066 | -46.94819 | 2024-10-24 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c21e5f1a-3c40-3c49-bb77-23cc5c01d1dc | -6.88673 | -46.96726 | 2024-10-24 04:55:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3238ed5c-4599-31f8-8848-6c0d39c935b5 | -6.74665 | -48.05919 | 2024-10-24 04:55:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2418028c-3d95-32de-9a13-c6d388972065 | -6.63111 | -47.35085 | 2024-10-24 04:55:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce6af2ff-1e23-3d80-b314-54e16e04c7d0 | -2.11533 | -48.37215 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b65dc9dd-f70c-30c3-95d5-87efcb209512 | -2.03154 | -48.07825 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c65e112-1143-3170-9b45-45b7a7a4ba52 | -2.03129 | -48.07766 | 2024-10-24 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f2a82c2-a9f8-301a-8aae-2166ac3170bf | -1.87762 | -47.80706 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4d819f4-59b1-3b6a-8bb5-739b825d4dd5 | -1.87706 | -47.81072 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a1c49772-0caf-39ba-a64c-b010ede9829b | -1.87294 | -47.81011 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f91d071e-055b-39a8-8dd9-cb6ffc788100 | -2.92072 | -48.95833 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff91ea60-c6f3-361d-b935-ec0dc638832d | -3.46126 | -47.67343 | 2024-10-24 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8866e2fe-2b9e-3777-9077-c714e908bb6a | -3.45703 | -47.67263 | 2024-10-24 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3dad59e2-18d0-3adf-9b8f-c4e9eb164133 | -3.14546 | -48.56641 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c6c6584-aea5-360c-bb92-120545375baf | -3.12216 | -48.65324 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58016a93-7e51-3259-84a7-0662d137dbb9 | -3.11119 | -48.60309 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da48c8cb-7679-3d46-aeff-d0bf7e96d1cf | -3.108 | -48.59739 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10ff2205-fc7e-32dc-8723-22c45c8b147e | -3.10176 | -48.66404 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf3cd8e2-e0f0-356c-ab9e-4ff5535d3fcc | -3.09779 | -48.66345 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d262b450-6f76-32bb-a29d-e72c9e1d8c2d | -3.0472 | -48.0486 | 2024-10-24 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 139ebce2-2a69-3775-bf53-a114518613a9 | -3.04665 | -48.05225 | 2024-10-24 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92efbb22-827f-359e-b11a-f021abf7e72b | -2.90775 | -48.06176 | 2024-10-24 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6147b82-d6d8-32c1-b8f8-bb0d2fbf4606 | -2.89108 | -48.28355 | 2024-10-24 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f45816b-3e77-3dd1-87a0-f3f7c1114f48 | -2.77746 | -48.69613 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0de41976-c45a-3e68-ad50-95c856994559 | -2.77669 | -48.70108 | 2024-10-24 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README62.md)
