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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a56fc5ff-1d82-30d8-bdda-6b9b4068da4d | -2.7939 | -46.6366 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb977805-7233-34cf-b1cc-1a2f8c57e385 | -3.2946 | -46.0686 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f15e19be-e74d-3ce8-9615-cfa18789ba89 | -3.2931 | -46.061798 | 2024-11-15 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8997b7bd-275a-3a7b-84eb-f595aa7f2795 | -2.6813 | -46.823101 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ad5e29-2301-3dd6-a9d8-7361be3bca3b | -3.2308 | -45.373001 | 2024-11-15 00:08:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea77b3a6-8e01-3a4a-ba54-8dfeb97eae4f | -2.6423 | -46.191299 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4c06d1-be09-3ab8-9495-7ffa8ac4d97b | -2.3344 | -46.288101 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5de25729-59e7-3aec-91c1-3419a5a0090c | -2.6632 | -46.8344 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75850e48-4f74-34f4-b5b6-32b6c23c86d8 | -3.7735 | -41.602001 | 2024-11-15 00:08:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b4ec5b4-631f-3f29-bf9d-62e76d6d0cb9 | -2.3217 | -46.872898 | 2024-11-15 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 029228bc-0d51-3c6f-a1e6-4e4e092b3bac | -3.0686 | -45.065201 | 2024-11-15 00:08:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa7c80e-c02e-30f0-8eef-2a3a30be0096 | -2.1744 | -46.172501 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab4a2abd-c3ff-3e8d-9f44-911fdaa9595a | -4.3739 | -43.006401 | 2024-11-15 00:08:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6839d8e-87be-3ec4-9502-4a6f84c89379 | -2.9794 | -45.858101 | 2024-11-15 00:08:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae1af36f-7532-3d97-9d93-530c2b052788 | -2.4917 | -45.157501 | 2024-11-15 00:08:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54cc368b-dbb0-3e15-9cdc-91f454b4c511 | -1.3426 | -46.550598 | 2024-11-15 00:08:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac84c87-2c98-3022-bc9d-a7a0fbd1a0ad | -2.2884 | -46.449902 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3acb0c7a-a385-3327-93e8-67d6f9ab124a | -2.0943 | -46.319599 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa1861e-c61a-3743-9e73-47f3a079e0a4 | -3.7134 | -41.698898 | 2024-11-15 00:08:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c60f3636-ceb9-3a15-8d90-1fab265c6c87 | -2.3185 | -46.858799 | 2024-11-15 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b344692-b837-36f1-a14b-d91664f0ec12 | -10.722 | -40.525299 | 2024-11-15 00:08:00 | METOP-B | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7e5feeab-bbb5-3e1d-b10b-b5af636c6305 | -2.6518 | -46.829601 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08745e85-b558-362b-ab12-b813415fffab | -2.2858 | -47.906601 | 2024-11-15 00:08:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dfad842-755c-31fe-b8da-37a34a8ae262 | -2.3315 | -46.8708 | 2024-11-15 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 885038e8-8ae9-373b-812f-4bff11393edb | -2.6361 | -46.163898 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a05e492-9818-3040-be17-e9e63d67d2c4 | -2.3201 | -46.865898 | 2024-11-15 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af3c2a7-08bf-3425-b19f-fe5389129a37 | -1.7081 | -46.160999 | 2024-11-15 00:08:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 952f380e-98b1-3880-ba0d-219733548818 | -3.7637 | -41.604198 | 2024-11-15 00:08:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 01257822-38e8-32d9-aff7-5d9dee2f5daa | -2.1894 | -46.147701 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89b4f719-2f5c-3d2c-ab69-e38c5de83317 | -3.6996 | -41.683601 | 2024-11-15 00:08:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 15b21a81-cc05-3c3f-9a70-93067bcdb9ff | -4.0044 | -43.2388 | 2024-11-15 00:08:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88103bd4-a54f-3e45-ac43-133cb959eec4 | -1.4642 | -48.190399 | 2024-11-15 00:08:00 | METOP-B | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfba7dec-cc7e-3f34-bad1-92837212fd9b | -2.9472 | -45.120899 | 2024-11-15 00:08:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 851dd81b-97fa-3596-9252-ab596fd1bd40 | -1.3441 | -46.557499 | 2024-11-15 00:08:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7b87bf-0121-3206-98ce-0933d41ed7d5 | -2.9032 | -46.848099 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99be8f11-8241-3087-a304-1a4e6536eeb4 | -2.4803 | -45.152802 | 2024-11-15 00:08:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9e5cebc-d7ca-3584-865d-5486b41951ad | -3.1189 | -45.562302 | 2024-11-15 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02e56058-ae31-3e46-9233-f5a9bf41bf0e | -2.6715 | -46.825298 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54671628-de84-33e5-bb87-0e01ceae6bfc | -2.5599 | -46.008301 | 2024-11-15 00:08:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32950980-2dcc-3b3d-a83a-1ef4631fcee1 | -1.9554 | -47.947701 | 2024-11-15 00:08:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f784fe99-52c0-36bc-a1ef-cb6f51f07378 | -2.981 | -45.864899 | 2024-11-15 00:08:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79111eb4-3fca-3ab1-aa55-6e8ff2f33542 | -3.1174 | -45.5555 | 2024-11-15 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8412c1e-2780-3a87-868c-eb16417d0d30 | -2.8682 | -45.044998 | 2024-11-15 00:08:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f55770a-c082-3369-98ad-96496a683384 | -1.855 | -47.821201 | 2024-11-15 00:08:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e3cfe34-513c-3872-b383-67e21627fb47 | -2.9482 | -45.170898 | 2024-11-15 00:08:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69d7b964-9e66-385e-adf1-5ad4aa7c080b | -2.0958 | -46.3265 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8315ac01-47e1-36a9-9e79-ee2e33d5620c | -4.3722 | -42.998901 | 2024-11-15 00:08:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09edd525-c4d6-30c2-a43e-1be6e6c2162d | -2.8182 | -46.653198 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a782e1f-fc62-3d03-b148-d513043a3f83 | -2.276 | -47.908699 | 2024-11-15 00:08:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5496187-69e9-345b-a5e3-9c09d0fc2661 | -3.2376 | -44.309502 | 2024-11-15 00:08:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98ab93c8-b57c-3144-920d-1c0d9783e404 | -2.6294 | -46.179699 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b975c3d8-cbba-346a-9531-58886a6a5605 | -2.3375 | -47.2187 | 2024-11-15 00:08:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a62f83-6f2c-3674-aa42-f4ae30b04a97 | -2.6192 | -46.821999 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb7db7e1-a36f-3bba-92b5-50bcce55265d | -1.9811 | -46.366199 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d4a4a66-6f21-3052-991f-5df8a877d17e | -2.1422 | -46.3955 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1ca40a3-f258-32d6-abd7-9b77863d3039 | -2.0696 | -46.210098 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5b71e6-7b80-3aca-8269-2f4669d1106b | -2.0829 | -46.5895 | 2024-11-15 00:08:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff78076-9586-3119-bcd2-c4f6792bde02 | -2.8666 | -45.0382 | 2024-11-15 00:08:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 984176f0-a44b-35f9-ab3d-8db37c7f6607 | -1.4709 | -45.748901 | 2024-11-15 00:08:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d0e7701-beb2-37f3-8f5c-9ce3f29ef63d | -2.068 | -46.203201 | 2024-11-15 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64ac5395-e6f4-3dc4-ab86-8960931f0625 | -3.0947 | -45.775299 | 2024-11-15 00:08:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6378ad2-e92c-336e-b963-d75b12c1b344 | -2.9825 | -45.8717 | 2024-11-15 00:08:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67eea633-1a72-399b-b37b-740ab0122640 | -3.7867 | -43.912498 | 2024-11-15 00:08:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d3640e3-d37a-33e3-a941-41c274787122 | -2.5584 | -46.0014 | 2024-11-15 00:08:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81ea86e2-22d0-3f4f-baf2-844372c58d89 | -2.6279 | -46.172798 | 2024-11-15 00:08:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57e61b36-e04c-3c32-aea8-5290dbb3d7fc | -2.3962 | -47.7099 | 2024-11-15 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee3b89a-5a61-365c-be3d-3bdc98539862 | -3.7948 | -43.903198 | 2024-11-15 00:08:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61f33f42-09e7-319c-b6fa-8e94bd6810bb | -6.3154 | -39.5135 | 2024-11-15 00:08:00 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d221f622-0adc-3830-b501-dc488e9e488e | -2.5568 | -45.994598 | 2024-11-15 00:08:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51fc6f3e-625f-31cb-bc2f-b9bc78e37f68 | -2.6683 | -46.811199 | 2024-11-15 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0453469a-a224-3568-8c25-9f7e7e98575c | -2.3407 | -47.2288 | 2024-11-15 00:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 542ba0d2-3697-3cc4-965f-a5f452da9856 | -3.7867 | -43.9011 | 2024-11-15 00:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 96422299-5b3b-3b7f-bb8f-0183cf86847d | -2.9825 | -53.8677 | 2024-11-15 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 16926130-e981-32b9-ad83-1f525e2d38aa | -3.7066 | -41.6997 | 2024-11-15 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 1b282f55-3d15-35b9-8faf-e793aaabb563 | -1.9198 | -45.4459 | 2024-11-15 00:10:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 3283eb0e-8ec6-3ed6-9703-e49634d1d9be | -3.0883 | -45.7687 | 2024-11-15 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 12d42bc1-fdd6-3679-9ad8-c6826f93eba7 | -2.8534 | -53.9915 | 2024-11-15 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4ec756c2-e77a-3655-9fdb-9a4150600b61 | -17.2347 | -57.4721 | 2024-11-15 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 989c42be-160e-3cf1-a373-50550d526d4d | -3.7254 | -41.6987 | 2024-11-15 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 118.4 |
| 62ad464b-3297-32f1-a182-6ca5431d6d9e | -17.5879 | -57.4917 | 2024-11-15 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 72236b66-cb95-374b-87d7-e8d55e82fb6a | -2.641 | -46.1849 | 2024-11-15 00:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| d47a0ad4-1301-3d57-8a03-d74fc9a0b528 | -1.9012 | -45.4687 | 2024-11-15 00:10:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 9d76a874-8fc3-3db3-b26c-1ba4f16e6dd4 | -17.7052 | -57.5392 | 2024-11-15 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 9396c9e9-1e1a-33da-b35b-64d36ba6180e | -2.9825 | -53.8476 | 2024-11-15 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b40aff55-31f5-3648-bf33-1416263ffee5 | -1.9013 | -45.4463 | 2024-11-15 00:10:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 7e3501e1-f29a-3021-984b-8e3c914d0a31 | -17.7048 | -57.5597 | 2024-11-15 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| dcdddacf-2a68-3462-a220-3fe2e13fb654 | -2.3408 | -47.2069 | 2024-11-15 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 59dff0fe-174b-3727-a2c5-17620dd2240f | -3.0882 | -45.791 | 2024-11-15 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 300cc498-fa97-3605-97df-9975c819a50d | -2.6596 | -46.1843 | 2024-11-15 00:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 121.6 |
| e571dde8-be82-3611-b6f8-92c22095efc2 | -17.5885 | -57.4506 | 2024-11-15 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 960ed646-3009-3090-9feb-cf67668cd26f | -3.7866 | -43.9241 | 2024-11-15 00:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b1afe4e6-e278-3413-b1ce-87bd935c1449 | -3.7068 | -41.6758 | 2024-11-15 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| ff5e97d6-e90d-31c3-8fd9-9f3dcdbfa6ef | -17.235 | -57.4516 | 2024-11-15 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 11ad9023-5d8a-3d6a-a38f-17e613c4d551 | -15.3025 | -56.5268 | 2024-11-15 00:10:00 | GOES-16 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0d29f5c4-a08a-3659-a5a7-8303a3ac65aa | -2.3233 | -46.8786 | 2024-11-15 00:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 5e0c8827-baba-38c3-adec-e73e99fc6af7 | -17.2547 | -57.4493 | 2024-11-15 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.6 |
| 8ef08ccd-bf15-3726-bc7a-59f97e6c11e2 | -17.274 | -57.4675 | 2024-11-15 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| f9829089-9b39-3ec9-8bed-a9d8cc4201e6 | -3.8054 | -43.9002 | 2024-11-15 00:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| aa6f2cc5-f4f1-3014-93e4-0a0002c5fe48 | -2.8535 | -53.9714 | 2024-11-15 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 48969b8f-582a-318c-be7b-5ed6092a7706 | -2.3234 | -46.8567 | 2024-11-15 00:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |


[Clique aqui para ver as próximas entradas](README4.md)
