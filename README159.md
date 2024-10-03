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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 332f7767-b61d-32d5-8695-8272f4bcf64b | -11.97332 | -50.18096 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72ad00b4-af20-3ad4-b64a-e208aaa1d04f | -11.97166 | -50.1799 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d742eb49-374a-3684-9807-6849f7ead9f2 | -11.96771 | -50.18027 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b158b315-9356-36b2-90b7-839d35994dde | -11.96605 | -50.1792 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7239b0ef-bff8-3d21-ae10-a96788234a12 | -11.94862 | -50.15091 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd858af0-0130-3741-93a7-a7643e97ae05 | -11.94815 | -50.15471 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8718e96-2b7a-3a59-a6e7-0750ff94ae70 | -11.94254 | -50.15401 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c833519-e3ac-3446-a565-11195c34e3e1 | -11.93694 | -50.15331 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 216415d5-1ff8-3ca2-80cc-19da6384ddc2 | -11.93647 | -50.15711 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef2e3c34-7abe-3b1e-a52e-f1c4a1c61b3b | -11.09199 | -50.72124 | 2024-10-03 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a8655f2-e04b-3ab3-a608-dfd3a073006b | -11.09156 | -50.7246 | 2024-10-03 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb13bc11-5dbd-3632-ab91-7b0c234e432c | -13.07473 | -50.84334 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23bf0a7b-8536-3c32-ad8f-2a04980916d8 | -13.07431 | -50.84688 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 428e6cd4-d80b-346a-aff5-957e98c3dc64 | -12.79111 | -50.58773 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26b5265a-1457-317e-9536-e0bad1043650 | -12.7856 | -50.58704 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41b4ab44-027c-36de-a5f0-41d0d94423b0 | -12.42108 | -51.0106 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1c2237b-3ba6-39e5-a495-4ad078472452 | -12.42067 | -51.014 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e765ecdf-7e8c-3011-9716-3a5f5ce6d99b | -12.39964 | -51.02054 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92ae9cde-d9df-3aad-983c-6da3fb104b99 | -12.39894 | -51.01458 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab71b9ab-cabb-3e41-af95-d2458e6c43c8 | -12.39814 | -51.02133 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cea2a866-6e41-34e5-bbdd-cb75af832c5e | -12.39475 | -51.01648 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a052c0f5-87a4-333a-9894-2e977eb49b11 | -12.39475 | -50.95886 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce45cf97-a9ee-3635-b8c6-9823f0e93f0e | -12.39362 | -51.01388 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7d4966e-fbfc-318e-9c19-a1a591e3768b | -12.39321 | -51.01725 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aab14592-5c02-3eb9-aadd-97dd29a97d18 | -12.39137 | -50.95753 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6db90be1-0106-3ef7-a369-2831c482201f | -12.39094 | -50.96093 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19c5bc7a-ee43-3e77-9c31-9ef4fdf63b7e | -12.38658 | -50.982 | 2024-10-03 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ca08e70-589d-328b-b4f2-ebc2c247d252 | -13.10857 | -51.18136 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05bb0bb2-5f41-33d9-88ed-c8d2941b74c0 | -13.10484 | -51.18097 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4549783-4a77-3036-9690-ab9d40bba53a | -13.09628 | -51.16275 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e85192f3-b7ee-335d-bb39-fc54020e439f | -13.09587 | -51.16612 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fa6a24aa-431b-3e83-bc22-00cefb2c997f | -13.09545 | -51.16949 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc3c0842-66d2-3a5d-a7c7-34133efb72ca | -13.09138 | -51.15869 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1e2abad9-8dba-379a-ac6e-431e5714a9a9 | -13.09096 | -51.16208 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f25492a9-b738-3051-b082-c9537a428e73 | -13.09054 | -51.16546 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d8edda5-b713-3a62-a951-c5e27f390307 | -13.09013 | -51.16883 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 144d07c2-1989-39a9-93ed-e56328bee4a4 | -13.08971 | -51.17221 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b65286eb-cc26-3103-b6f7-3013bea6e621 | -13.0893 | -51.17559 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8904879a-8f67-386c-98aa-f776cc03afcb | -13.08563 | -51.1614 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e6b827f-0ca9-3d1e-8eec-505042239564 | -13.08522 | -51.16479 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66322f0c-9a96-3517-864c-c039abbffab1 | -13.0848 | -51.16816 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9879004e-e5a4-3c83-bf84-e02932373c77 | -13.08031 | -51.16072 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 954b16b6-0236-38d0-8ea3-c24f553ff18c | -13.07989 | -51.1641 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 016bba27-36d5-30e6-b357-b27c39d25744 | -13.07948 | -51.16748 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00da485f-5776-312e-9141-f6d0cced6bc7 | -13.07498 | -51.16003 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 322391c5-fbb1-34e1-9ed6-bbf178db7413 | -13.07457 | -51.16342 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 249c9521-b675-361b-9716-c9e5ee9c1288 | -13.06392 | -51.16208 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7858a037-769e-321f-8b87-d86ea83c9c11 | -13.05941 | -51.15464 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e67663d-8cf0-3091-af36-e33891cb2688 | -13.059 | -51.15802 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ca832d8-52ea-32f8-a432-5c58882a744c | -13.0545 | -51.15055 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 45647400-a0c9-3736-99f6-1b3eea3299a6 | -13.05409 | -51.15395 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 68db17bd-b90d-3762-8d64-8167966a2b23 | -13.05368 | -51.15733 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0a43a35a-ead0-3441-9d8f-73d5559454f2 | -13.0512 | -51.13293 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6d086d6-6ac1-319e-a1b1-ca3e38315de1 | -13.05079 | -51.13633 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 71170a8a-b805-3646-8cf0-af6667e9dc2c | -13.04998 | -51.1431 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| f9da3b2a-45f1-3e94-9e74-ffcd2eabdf04 | -13.04958 | -51.14648 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| eb3cda56-2aba-3c4b-a934-efa0abf3e939 | -13.04917 | -51.14988 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| df944272-ddfc-36a6-85e1-ec2e79484d5f | -13.04587 | -51.13226 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03d51361-aaec-3f47-86b8-2b799a4f6fdb | -13.04546 | -51.13565 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 6e03d807-6865-3695-b752-404ebdc6a75d | -13.04506 | -51.13904 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 1f33e8bd-69b0-3083-a250-0b42430722fb | -13.04465 | -51.14242 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 03a4af37-ba69-36e2-b01a-f08a21687fb1 | -13.04425 | -51.1458 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5c53877b-2c04-390d-a75a-90df8fe1a37b | -13.04384 | -51.1492 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4bc5e1a7-f0ac-316a-8801-de8fc778ac08 | -13.04343 | -51.1526 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a6e926a-8ed8-3654-af9b-6a955fbe010b | -13.04053 | -51.13158 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9f6a782-5a17-3614-a160-e5f372e8c49e | -13.04013 | -51.13497 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 53114f66-ef10-3b61-b4e2-4f3811a4968e | -13.03932 | -51.14175 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3d01734b-edec-38ba-90dd-9c3c02116f10 | -13.03892 | -51.14513 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 0c613904-f1fb-3a16-94b6-a6978669c1e6 | -13.0348 | -51.1343 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1c07e8f4-5f96-34e0-99c6-5b268950da65 | -13.03439 | -51.13768 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9ac5a161-04f9-304d-a001-1632935b850e | -13.03399 | -51.14108 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c826ccf3-000f-3b42-8b82-a7a1b1cae8d2 | -13.02906 | -51.13701 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b2f2c7af-1aac-3a82-aa68-445d7cf80643 | -13.02866 | -51.1404 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d9904b26-1e5e-3d30-a400-dc7590a9f04c | -13.02488 | -51.13911 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ea83256-e5a1-3c12-924d-3a9760f4f468 | -13.02373 | -51.13633 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 294a5db4-3730-3e13-9e52-c1f263eedf9b | -13.01998 | -51.13506 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48a044da-243a-3009-843c-251c06ffd732 | -13.01956 | -51.13845 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f50adfff-792b-341f-a6db-8f9c68dc12ef | -13.0184 | -51.13564 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d2d6dc7-3a45-311a-857d-8a85f52ade8f | -13.00483 | -51.12627 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16337e47-e683-30a2-9681-2c58b89bffd9 | -13.00441 | -51.12965 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d0f122b-eba9-3840-98e7-e6cfd12c7490 | -12.99992 | -51.1222 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54cef16a-f68f-3d09-8b74-7b61fdbcddf3 | -12.9995 | -51.12559 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08a142d2-4427-36c2-828e-458a229974ff | -12.99908 | -51.12899 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b05900dd-0967-31ef-966c-56f79b54cdc7 | -12.99866 | -51.13238 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1f75c44-0c12-34a9-99dc-b9f48b916fbb | -12.99333 | -51.13172 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0580c0af-66a8-3ac3-9454-5b4afd1b886d | -12.99291 | -51.13511 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb494d94-19c4-3aa4-b731-1a3ab7480a4d | -12.972 | -51.12907 | 2024-10-03 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb5a7c96-064a-3c79-a9b8-193314f8bf75 | -13.60508 | -51.22699 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f11283b-c414-359d-b309-986ec79c6b78 | -13.5669 | -51.22904 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7caced0d-cb92-3d5a-9580-02f083e3d40b | -13.5665 | -51.23244 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a06f6a91-95f5-35d8-b74f-c1a608e68dd0 | -13.56289 | -51.26299 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e93e4536-45b8-3728-b7b6-1dff54f147b2 | -13.56249 | -51.26637 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ffb3bc6f-ff23-30cf-bbb9-72f891756ed0 | -13.56209 | -51.26975 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5555997-ee9a-35af-837d-11e89936eb8f | -13.56116 | -51.23178 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 35d4c312-5379-3e13-951a-464a88ac9f0c | -13.56076 | -51.23516 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3822bcd9-7cfd-33e3-88c4-8753da4f0ff2 | -13.55996 | -51.24197 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2c6fc31-8cd6-389c-88aa-5945175999f4 | -13.55956 | -51.24537 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec699a0a-59b8-36d6-bfdd-49489acc198e | -13.55677 | -51.26907 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b85a9223-eb63-388e-9ee6-b0eaffb961c9 | -13.5308 | -51.14118 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f84af470-86e6-3f75-b9ae-d902272fa021 | -13.52585 | -51.13707 | 2024-10-03 05:16:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README160.md)
