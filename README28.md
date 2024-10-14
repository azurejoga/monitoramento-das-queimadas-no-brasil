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
| d82be93e-5cbd-363a-a8dc-b57208c0fb55 | -4.1149 | -48.2299 | 2024-10-14 02:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c69a0b82-9d66-3e3f-ac06-1e2b6c42265b | -6.1345 | -42.767 | 2024-10-14 02:55:41 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 46.0 |
| 2ad3b212-d273-3be9-ae6f-6a9255cb24bd | -6.1342 | -42.7906 | 2024-10-14 02:55:41 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| f9a1a508-e902-3395-93f7-ab666dc9453e | -6.2141 | -48.329 | 2024-10-14 02:55:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 61.0 |
| be199b5a-79e9-3c6f-a6d1-96d84d9a5bc8 | -7.9394 | -44.5076 | 2024-10-14 02:55:51 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 9b2c14a6-c3c8-3abd-812f-0fc4b8b34147 | -9.1043 | -61.162 | 2024-10-14 02:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2930aaee-2849-35b6-bbf4-0095f96b9c62 | -9.4888 | -45.8228 | 2024-10-14 02:56:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 55f313f4-c698-3078-8035-d32b76ad0f17 | -10.0816 | -44.2133 | 2024-10-14 02:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f7fa6fda-1d66-3a68-9c1c-bbf1e792347f | -10.0813 | -44.2366 | 2024-10-14 02:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 216.6 |
| a7b518b3-0c44-331a-9ec7-38241a65bdbe | -10.0809 | -44.2599 | 2024-10-14 02:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 179.2 |
| ffde01ef-6cf2-3028-a9a9-0ce325170303 | -10.0622 | -44.2391 | 2024-10-14 02:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| a8716260-e31c-38ab-b97c-2445c5687ccf | -10.0619 | -44.2624 | 2024-10-14 02:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 0e3b04d8-4645-3570-a0ba-71975138482d | -10.0163 | -47.3308 | 2024-10-14 02:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| dacddd9f-2c0a-3059-a3c0-cd4b71348839 | -10.0352 | -47.3286 | 2024-10-14 02:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5a0c60d2-0106-346c-a7c9-4720cd94c758 | -10.5307 | -49.7843 | 2024-10-14 02:56:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 1251fc39-0cf1-3e04-aad9-3f826d85b616 | -12.3804 | -53.1376 | 2024-10-14 02:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 14cf34b6-0bdd-3933-939e-45e124ea0efe | -12.3807 | -53.1167 | 2024-10-14 02:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 01430bab-1248-3914-b3c0-b8cef394f9ab | -12.3994 | -53.1355 | 2024-10-14 02:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| f7de1535-6805-334b-9713-ff3b65511dd5 | -12.3997 | -53.1147 | 2024-10-14 02:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 196.0 |
| 6906a873-e210-374d-a12d-f53d89c1c925 | -17.1758 | -57.479 | 2024-10-14 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| edbffa67-bbc6-35a9-bd7d-bc6ce8ca45ab | -17.1761 | -57.4585 | 2024-10-14 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 3286b976-b264-365b-b876-c1b54646c48b | -17.1954 | -57.4767 | 2024-10-14 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 4153ae38-b8be-3508-b133-dd36c791512a | -17.1957 | -57.4562 | 2024-10-14 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| afe52780-9b79-36bb-8294-eac2b412494a | -17.196 | -57.4357 | 2024-10-14 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.5 |
| e8a66789-1ab2-3f16-b788-92654f9c1ef9 | -17.6474 | -56.2876 | 2024-10-14 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 53070182-55ab-3e7c-a407-942c1e84f955 | -17.6471 | -56.3084 | 2024-10-14 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| a68aeffe-7946-3d0e-8fad-76121d921ffe | -18.1909 | -56.8186 | 2024-10-14 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 5567699e-6bcb-31e5-bad8-a1d49eb73efb | -18.1905 | -56.8394 | 2024-10-14 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| cfa247a1-449c-310b-ae7f-585af154dd90 | -18.2559 | -56.4988 | 2024-10-14 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 1da3875c-36d1-3b73-aa11-57cb2d60abcd | -18.2555 | -56.5196 | 2024-10-14 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| fb6bc0cb-e7b4-3ebd-b843-cb9a30f9a33c | -5.71463 | -35.49919 | 2024-10-14 03:02:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4a17155d-bc3c-3eca-bdea-e2d0f101214a | -5.71394 | -35.50305 | 2024-10-14 03:02:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 232a9ceb-d03e-3a91-a7ad-390d9c73f822 | -4.38122 | -37.9021 | 2024-10-14 03:02:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b99fb91a-4e64-362c-9b16-93b66c603c38 | -4.38016 | -37.90813 | 2024-10-14 03:02:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| de81dba0-0c9b-3714-b07a-6ce28a6089bd | -4.37448 | -37.90086 | 2024-10-14 03:02:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4b32acc2-e53a-3233-82ba-fc6adfd0eb60 | -4.37342 | -37.90687 | 2024-10-14 03:02:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 26c5a7d6-d031-3ca4-9c0c-81ce026ebda4 | -4.37235 | -37.91295 | 2024-10-14 03:02:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1708b3d3-a90e-39b2-b23d-830f543a1870 | -9.5211 | -36.09939 | 2024-10-14 03:04:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e29e205b-0d68-3f84-a45b-32d63ce97eb8 | -7.26761 | -35.12579 | 2024-10-14 03:04:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9b7b4bdc-b6ac-3dfa-8eec-ef297ca741a9 | -7.26731 | -35.12314 | 2024-10-14 03:04:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8fc78a45-7549-39e7-8f33-940684714535 | -7.26669 | -35.12669 | 2024-10-14 03:04:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a864a94a-2a70-3657-8a31-694dcde24914 | -7.02179 | -35.23505 | 2024-10-14 03:04:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9166a11e-aca1-30ad-855e-4deff5b7a8c4 | -7.02161 | -35.23409 | 2024-10-14 03:04:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2c35459-cf2d-34ba-8be6-277c7383adb4 | -7.02118 | -35.23857 | 2024-10-14 03:04:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3ff4e77c-a1e5-3330-9517-9d61366d9dda | -7.02098 | -35.23759 | 2024-10-14 03:04:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d610960f-8a47-3a49-97e7-be3e398ce55d | -7.02033 | -35.24112 | 2024-10-14 03:04:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fc8b7383-8299-3506-977a-6ef32522d724 | -6.7572 | -34.97653 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1a8de80-c5d3-3325-96ed-f0c48cea2f62 | -6.7566 | -34.97987 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b88b58da-d180-34c6-9208-542ec098c9bf | -6.756 | -34.98321 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d4a26638-fd14-3d61-8423-baf16361efa2 | -6.75556 | -34.97628 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8073bd51-a9da-39ba-87b2-39fd7ea16564 | -6.75498 | -34.97964 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b44a51ba-4c0e-3832-935f-9bb5df885fe1 | -6.7544 | -34.98299 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20db0c08-e125-34dd-bf7c-d2841890df32 | -6.75382 | -34.98637 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d00f44be-d935-3c3b-b1fa-cf3c7c0464d9 | -6.75321 | -34.98987 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 578d53de-ebe0-3ac8-84b5-4f5af0962cd8 | -6.75181 | -34.97544 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3bc903b8-d65d-3722-a4a5-d1ad3123f342 | -6.75119 | -34.97885 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3f48e29e-2661-3345-9232-458b58d8b548 | -6.75058 | -34.98224 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f206f38a-5721-3716-b0b9-c8a581b790c9 | -6.75016 | -34.97522 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1478619f-f1ee-3f93-bfe3-cae9fd847769 | -6.74996 | -34.98566 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a4aaa4dc-5423-337d-980e-e4df4b0e5b9b | -6.74957 | -34.97863 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 265f70a4-18ce-3799-b9e1-128cac4b6a5c | -6.74898 | -34.98205 | 2024-10-14 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9ed2bc98-d635-3a22-b52e-2aef5141714d | -11.17689 | -39.90507 | 2024-10-14 03:04:00 | NPP-375D | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 35b992c8-8ec8-39ff-96ef-7a1f26e0cba0 | -11.17604 | -39.90443 | 2024-10-14 03:04:00 | NPP-375D | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 97722e73-3950-3cb1-94ef-48590fabbf7d | -11.17561 | -39.9112 | 2024-10-14 03:04:00 | NPP-375D | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 84b02555-b2ba-346a-85bd-548a85ac07c6 | -11.1748 | -39.91058 | 2024-10-14 03:04:00 | NPP-375D | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 2cada224-53bf-3a36-8f6e-b7b89e74549e | -10.21901 | -36.33165 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| f2299127-b5c5-3be3-b736-a86a32d5e1d0 | -10.21831 | -36.33538 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 384d3301-7fdf-3213-98fa-6dec6cc30ce2 | -10.2176 | -36.33913 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 0945415d-2aad-3a39-8f17-5d1c88119af1 | -10.21275 | -36.33424 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 402f45de-1f16-39e1-914b-ed0e0eddc6cc | -10.21204 | -36.33801 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ac74c67e-dd01-3f8e-805f-3911837e9267 | -10.14144 | -36.14058 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 51dc5e3b-3b08-3217-abb6-326c78a77db9 | -10.14075 | -36.14425 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 1a9c3e55-ba36-34dc-88c0-e03cbfba4dfd | -10.14005 | -36.14797 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 293421a6-bd43-35ea-9b11-8cf1375c677a | -10.13594 | -36.13945 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2562b187-e375-3a37-9d6a-6cb586b03805 | -10.13525 | -36.14311 | 2024-10-14 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3b0b690f-8bf5-37b2-b55b-7b8487258e76 | -10.08 | -44.22 | 2024-10-14 03:04:26 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f83a6f7-61e3-3e35-b570-c6610bfc1756 | -9.47 | -45.83 | 2024-10-14 03:04:31 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 827a6064-c56c-3b1d-a767-e14443618c67 | -9.5 | -45.83 | 2024-10-14 03:04:31 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99417f53-e8f7-3623-8377-14a5a8670512 | -3.29 | -42.83 | 2024-10-14 03:05:08 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29944a6d-0608-3f6c-8d0a-4d5b40dc18cc | -2.4529 | -46.919 | 2024-10-14 03:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1769fb46-8cb4-3ef2-9ce2-08d9aa9dfbe8 | -2.6117 | -49.1198 | 2024-10-14 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| e53a779c-6415-303e-b70c-0fa92135bcb6 | -2.6118 | -49.0985 | 2024-10-14 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 82197419-0d64-313e-bf28-ad0c6180f041 | -2.6119 | -49.0772 | 2024-10-14 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 6f954582-6c2b-349d-a95a-ccbef7a8c8d2 | -3.2889 | -42.8561 | 2024-10-14 03:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| e40bdde7-6971-309a-8f18-c32b3aa657c6 | -3.289 | -42.8327 | 2024-10-14 03:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 9c9980ef-668b-3c53-8a87-5ad5526f0576 | -3.3076 | -42.8553 | 2024-10-14 03:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 66a933cd-b98d-39a9-9ec0-c5fe7a037313 | -3.3077 | -42.8318 | 2024-10-14 03:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| c305fb8a-2032-34ad-8702-c3280e60552c | -3.3264 | -42.831 | 2024-10-14 03:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| c3c52441-adf0-3bc6-b2a4-1791e11f2ba0 | -4.1148 | -48.2515 | 2024-10-14 03:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 67e5a528-99b8-31fa-9c59-ab2a1ee88925 | -4.1149 | -48.2299 | 2024-10-14 03:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d06b6e92-33c1-38f4-9540-bdff926c9058 | -6.2141 | -48.329 | 2024-10-14 03:05:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 39fbb225-27a0-3741-9f75-97c7f2dcd28b | -7.9418 | -63.6365 | 2024-10-14 03:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 1e324e11-cf2b-3614-a301-a35457dde302 | -9.1043 | -61.162 | 2024-10-14 03:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5e8ffbf5-54fa-3afb-8c4f-35c07935f38f | -9.4696 | -45.8476 | 2024-10-14 03:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 39904c15-de0b-37e8-bec0-745d179bcd36 | -9.4699 | -45.8249 | 2024-10-14 03:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 236.6 |
| 1bf9b171-09fa-38bb-abb0-2bdd377aed05 | -9.4702 | -45.8023 | 2024-10-14 03:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| aa033d6d-e575-397b-adf9-235438932af3 | -9.4885 | -45.8454 | 2024-10-14 03:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 77c45ef9-f1d4-3f50-b58d-cb5bdddaf8c6 | -9.4892 | -45.8001 | 2024-10-14 03:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 810a702d-357a-3c09-b3b9-dd44df4eee90 | -9.4888 | -45.8228 | 2024-10-14 03:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 608.8 |
| e29713a1-91c7-3c3d-9756-21bcd8b8204a | -16.62501 | -42.79276 | 2024-10-14 03:06:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README29.md)
